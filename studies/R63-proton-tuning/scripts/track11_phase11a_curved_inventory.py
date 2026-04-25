"""
R63 Track 11 Phase 11a — Curved-donut inventory audit on the p-sheet.

Tests whether replacing R62 derivation 4's flat-torus mass formula with
the curved-donut Sturm-Liouville spectrum on the p-sheet preserves the
13-particle inventory fit.

Method:
  1. For each particle, decompose its mass-squared into per-sheet
     contributions via μ²_total = K_e²·μ²_e + K_ν²·μ²_ν + K_p²·μ²_p
     (the block-diagonal sheet structure used in flat-baseline R63).
  2. For the p-sheet, replace μ²_flat = (n_pt/ε_p)² + (n_pr − s_p·n_pt)²
     with the SL eigenvalue λ_curved on the donut metric
     (1 + ε_p cos θ_1) — solved by 10a's tridiagonal SL solver.
  3. The e-sheet and ν-sheet are kept at flat formula because their
     ε values are far from 1 (ε_e = 397, ε_ν = 2.0), so curvature
     corrections at typical mode quantum numbers are negligible at
     the precision the inventory tests at.
  4. Anchor L_ring_p by re-deriving so the proton matches observed
     under the curved spectrum.
  5. Predict the remaining inventory; compare to observed and to the
     flat-baseline prediction.

Outcome interpretation:
  - All particles within ~1% of observed → curvature preserves
    inventory; proceed to Phase 11b (deuteron compound audit).
  - Several particles drift in coordinated way → curvature shifts
    a parameter (e.g., effective ε_p); audit if parameter re-fit
    restores the inventory.
  - Inventory shatters → flat geometry is the right physics;
    Track 11 closes negatively, Reading A from Track 10 stands.

Output: outputs/track11_phase11a_inventory.csv
"""

import sys
import os
import math
import csv
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

import numpy as np
from scipy import linalg

from track1_solver import (
    Params, derive_L_ring, M_E_MEV, M_P_MEV, mu_sheet,
    SQRT_ALPHA, FOUR_PI, ALPHA, TWO_PI_HC,
)
from track15_phase1_mass import K_MODELF


# ─── Reuse 10a's SL solver ─────────────────────────────────────────────

def build_sl_eigensystem(eps, q_eff, N=512):
    """SL operator -∂(p f') + (ε²q²/p) f = λ p f on the donut metric
    `p(θ_1) = 1 + ε cos(θ_1)`.  Returns (S, W) for eigh(S, W).
    """
    h = 2 * math.pi / N
    theta = np.array([2 * math.pi * j / N for j in range(N)])
    p = 1 + eps * np.cos(theta)

    p_plus  = (p + np.roll(p, -1)) / 2
    p_minus = (p + np.roll(p, +1)) / 2

    main_diag = (p_minus + p_plus) / h**2 + (eps**2 * q_eff**2) / p
    upper_diag = -p_plus / h**2
    lower_diag = -p_minus / h**2

    S = np.zeros((N, N))
    for j in range(N):
        S[j, j] = main_diag[j]
        S[j, (j + 1) % N] = upper_diag[j]
        S[j, (j - 1) % N] = lower_diag[j]

    W = np.diag(p)
    return S, W


def sl_lambda(eps, n_t, n_r, s, N=256):
    """Return SL eigenvalue λ for mode (n_t, n_r) on donut at (ε, s).

    Maps to flat formula in the small-ε limit and to MaSt's μ²
    interpretation: λ corresponds to (m·a)² in natural units.

    Index map:
      n_t = 0  → idx 0 (ground state)
      n_t > 0  → idx 1 + 2·(|n_t| − 1) (cos-like, lower of parity pair)
    """
    if n_t == 0 and n_r == 0:
        return 0.0  # massless mode
    q_eff = n_r - s * n_t
    n_t_abs = abs(n_t)
    S, W = build_sl_eigensystem(eps, q_eff, N=N)
    # Compute only the eigenvalues we need (lowest few)
    eigvals = linalg.eigvalsh(S, W, subset_by_index=[0, 2 * n_t_abs])
    if n_t_abs == 0:
        return float(eigvals[0])
    idx = 1 + 2 * (n_t_abs - 1)
    return float(eigvals[idx])


def mu2_curved_p(n_pt, n_pr, eps_p, s_p, N=256):
    """μ²_p under curved-donut p-sheet geometry."""
    return sl_lambda(eps_p, n_pt, n_pr, s_p, N=N)


def mu2_flat(n_t, n_r, eps, s):
    """μ² = (n_t/ε)² + (n_r − s n_t)² (R62 derivation 4)."""
    return (n_t / eps)**2 + (n_r - s * n_t)**2


# ─── g-candidate parameters ─────────────────────────────────────────────

EPS_E   = 397.074
S_E     = 2.0042
EPS_NU  = 2.0
S_NU    = 0.022
EPS_P_BASELINE = 0.55
S_P_BASELINE   = 0.162037

# Sheet diagonal scaling (R59 F53)
K_E   = K_MODELF
K_NU  = K_MODELF
K_P   = K_MODELF


def total_mass_flat(tup, L_ring_e, L_ring_nu, L_ring_p,
                    eps_p=EPS_P_BASELINE, s_p=S_P_BASELINE):
    """Mass under all-flat formula across three sheets."""
    n_et, n_er, n_nut, n_nur, n_pt, n_pr = tup
    mu2_e  = mu2_flat(n_et,  n_er,  EPS_E,  S_E)
    mu2_nu = mu2_flat(n_nut, n_nur, EPS_NU, S_NU)
    mu2_p  = mu2_flat(n_pt,  n_pr,  eps_p,  s_p)
    # m² = Σ (2πℏc/L_ring)²·μ²/k for each sheet
    m2 = ((TWO_PI_HC / L_ring_e)**2  * mu2_e  / K_E +
          (TWO_PI_HC / L_ring_nu)**2 * mu2_nu / K_NU +
          (TWO_PI_HC / L_ring_p)**2  * mu2_p  / K_P)
    return math.sqrt(m2)


def total_mass_curved_p(tup, L_ring_e, L_ring_nu, L_ring_p,
                        eps_p=EPS_P_BASELINE, s_p=S_P_BASELINE,
                        N_sl=256):
    """Mass with curved-donut p-sheet, flat e/ν sheets."""
    n_et, n_er, n_nut, n_nur, n_pt, n_pr = tup
    mu2_e  = mu2_flat(n_et,  n_er,  EPS_E,  S_E)
    mu2_nu = mu2_flat(n_nut, n_nur, EPS_NU, S_NU)
    mu2_p  = mu2_curved_p(n_pt, n_pr, eps_p, s_p, N=N_sl)
    m2 = ((TWO_PI_HC / L_ring_e)**2  * mu2_e  / K_E +
          (TWO_PI_HC / L_ring_nu)**2 * mu2_nu / K_NU +
          (TWO_PI_HC / L_ring_p)**2  * mu2_p  / K_P)
    return math.sqrt(m2)


# ─── Inventory ─────────────────────────────────────────────────────────

INVENTORY = [
    # (name, tuple, observed mass MeV)
    ("electron",  (1,  2,  0,  0,  0,  0),  M_E_MEV),
    ("muon",      (1,  1, -2, -6,  0,  0),  105.658),
    ("proton",    (0,  0,  0,  0,  3,  6),  M_P_MEV),
    ("neutron",   (1,  2, -1, -1,  3,  6),  939.565),
    ("Lambda",    (-3, 2,  1, -6, -3, -3),  1115.683),
    ("Sigma_+",   (2, -3, -2, -6,  3,  6),  1189.37),
    ("Sigma_-",   (4,  0, -2, -6,  3,  5),  1197.449),
    ("Xi_-",      (-2, 4,  0, -6, -3,  6),  1321.71),
    ("phi",       (-3,-6,  1, -6, -3,  6),  1019.461),
    ("eta_prime", (0, -6, -1, -6,  0, -6),  957.78),
    ("K0",        (0, -1, -1, -6,  0, -4),  497.611),
    ("K_pm",      (1,  3, -2, -6,  0, -4),  493.677),
    ("eta",       (0, -4, -1, -6,  0, -3),  547.862),
    ("pi0",       (0,  0, -1, -6,  0, -1),  134.977),
    ("pi_pm",     (1,  2, -2, -6,  0, -1),  139.570),
]


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R63 Track 11 Phase 11a — Curved-donut inventory audit (p-sheet)")
    print("=" * 100)
    print()
    print(f"  Geometry: e-sheet flat (ε_e = {EPS_E}, |1/ε|² → 0),")
    print(f"            ν-sheet flat (ε_ν = {EPS_NU}, contribution negligible),")
    print(f"            p-sheet CURVED donut (ε_p = {EPS_P_BASELINE} < 1, non-singular)")
    print()

    # ─── Audit 1: per-particle p-sheet μ² shift ─────────────────────────
    print("Per-particle p-sheet μ²: flat formula vs curved-donut SL eigenvalue")
    print("-" * 100)
    print(f"  {'particle':12s} {'(n_pt, n_pr)':>14s}  "
          f"{'μ²_flat':>10s}  {'μ²_curved':>10s}  "
          f"{'ratio':>8s}  {'Δ(μ)/μ':>10s}")
    print("  " + "─" * 80)

    p_sheet_data = []
    for name, tup, m_obs in INVENTORY:
        n_pt = tup[4]
        n_pr = tup[5]
        f = mu2_flat(n_pt, n_pr, EPS_P_BASELINE, S_P_BASELINE)
        c = mu2_curved_p(n_pt, n_pr, EPS_P_BASELINE, S_P_BASELINE)
        if f > 0 and c > 0:
            ratio = c / f
            d_over_mu = (math.sqrt(c) - math.sqrt(f)) / math.sqrt(f)
        elif f == 0 and c > 0:
            ratio = float('inf')
            d_over_mu = float('inf')
        elif f == 0 and c == 0:
            ratio = 1.0
            d_over_mu = 0.0
        else:
            ratio = c / f if f != 0 else float('nan')
            d_over_mu = float('nan')
        marker = ""
        if (n_pt, n_pr) == (0, 0):
            marker = " (no p-sheet content)"
        elif (n_pt, n_pr) == (3, 6):
            marker = " ← proton anchor"
        elif (n_pt, n_pr) == (-3, -3) or n_pt == 3 or n_pt == -3:
            marker = " (k=3 baryon)"
        print(f"  {name:12s} ({n_pt:>3d},{n_pr:>3d})  "
              f"{f:>10.4f}  {c:>10.4f}  {ratio:>8.4f}  "
              f"{d_over_mu:>+9.2%}{marker}")
        p_sheet_data.append({
            'particle': name,
            'n_pt': n_pt,
            'n_pr': n_pr,
            'mu2_flat': f,
            'mu2_curved': c,
            'ratio': ratio,
            'sqrt_ratio_minus_1': d_over_mu,
        })
    print()

    # ─── Audit 2: anchor L_ring_p under curved spectrum ─────────────────
    print("Anchoring under curved-donut p-sheet:")
    print("-" * 100)

    # Flat-baseline L_ring values (anchor electron at e-sheet, proton at p-sheet)
    L_ring_e_flat = derive_L_ring(M_E_MEV, 1, 2, EPS_E, S_E, K_E)
    L_ring_nu_flat = derive_L_ring(3.21e-8, 1, 1, EPS_NU, S_NU, K_NU)
    L_ring_p_flat = derive_L_ring(M_P_MEV, 3, 6, EPS_P_BASELINE, S_P_BASELINE, K_P)

    print(f"  Flat-baseline L_ring values:")
    print(f"    L_ring_e = {L_ring_e_flat:.6e} m  (anchored on electron)")
    print(f"    L_ring_p = {L_ring_p_flat:.6e} m  (anchored on proton)")
    print()

    # Re-anchor L_ring_p so the proton matches m_p under curved spectrum
    mu2_p_curved_proton = mu2_curved_p(3, 6, EPS_P_BASELINE, S_P_BASELINE)
    mu_p_curved_proton = math.sqrt(mu2_p_curved_proton)
    L_ring_p_curved = TWO_PI_HC * mu_p_curved_proton / (M_P_MEV * math.sqrt(K_P))

    print(f"  Curved μ_p(3, 6) = {mu_p_curved_proton:.6f}")
    print(f"  Flat   μ_p(3, 6) = {math.sqrt(mu2_flat(3, 6, EPS_P_BASELINE, S_P_BASELINE)):.6f}")
    print(f"  Re-anchored L_ring_p (curved) = {L_ring_p_curved:.6e} m  "
          f"({(L_ring_p_curved/L_ring_p_flat - 1)*100:+.2f}% vs flat)")
    print()

    # ─── Audit 3: inventory predictions under curved p-sheet ────────────
    print("Inventory predictions: flat vs curved-p (re-anchored)")
    print("-" * 100)
    print(f"  {'particle':12s}  {'observed':>10s}  {'flat':>10s}  "
          f"{'curved':>10s}  {'flat err':>9s}  {'curved err':>11s}")
    print("  " + "─" * 80)

    rows = []
    for name, tup, m_obs in INVENTORY:
        m_flat = total_mass_flat(tup,
                                  L_ring_e_flat, L_ring_nu_flat, L_ring_p_flat)
        m_curved = total_mass_curved_p(tup,
                                       L_ring_e_flat, L_ring_nu_flat, L_ring_p_curved)
        flat_err = (m_flat - m_obs) / m_obs
        curved_err = (m_curved - m_obs) / m_obs
        print(f"  {name:12s}  {m_obs:>10.3f}  {m_flat:>10.3f}  "
              f"{m_curved:>10.3f}  {flat_err:>+8.2%}  {curved_err:>+10.2%}")
        rows.append({
            'particle': name,
            'tuple': tup,
            'observed_MeV': m_obs,
            'flat_MeV': m_flat,
            'curved_MeV': m_curved,
            'flat_err': flat_err,
            'curved_err': curved_err,
        })
    print()

    # ─── Summary statistics ─────────────────────────────────────────────
    flat_errs = [abs(r['flat_err']) for r in rows]
    curved_errs = [abs(r['curved_err']) for r in rows]
    print("Summary:")
    print("-" * 100)
    print(f"  Flat-baseline max |error|:   {max(flat_errs):.2%}")
    print(f"  Flat-baseline mean |error|:  "
          f"{sum(flat_errs)/len(flat_errs):.2%}")
    print(f"  Curved p-sheet max |error|:  {max(curved_errs):.2%}")
    print(f"  Curved p-sheet mean |error|: "
          f"{sum(curved_errs)/len(curved_errs):.2%}")
    print()

    # ─── Verdict ────────────────────────────────────────────────────────
    if max(curved_errs) < 0.05:
        verdict = "INVENTORY PRESERVED — curvature corrections within 5%."
    elif max(curved_errs) < 0.20:
        verdict = "INVENTORY DEGRADED — corrections 5–20%, parameter re-fit may help."
    else:
        verdict = "INVENTORY SHATTERED — corrections > 20%, curved p-sheet incompatible."
    print(f"  → {verdict}")
    print()

    # ─── Save CSVs ─────────────────────────────────────────────────────
    csv_p_sheet = out_dir / "track11_phase11a_p_sheet_curvature.csv"
    with open(csv_p_sheet, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(p_sheet_data[0].keys()))
        w.writeheader()
        w.writerows(p_sheet_data)

    csv_inventory = out_dir / "track11_phase11a_inventory.csv"
    with open(csv_inventory, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f"  CSV: {csv_p_sheet}")
    print(f"  CSV: {csv_inventory}")


if __name__ == "__main__":
    main()
