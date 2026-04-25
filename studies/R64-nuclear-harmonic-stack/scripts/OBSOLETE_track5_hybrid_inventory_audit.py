"""
R64 Track 5 Phase 5a — Hybrid inventory audit.

Tests the multi-sheet architecture (Q134 §0.1):
  - Nucleons live on the p-sheet (R64's pure representation).
  - s/c/b/t-bearing hadrons live cross-sheet (R63's representations).

Method:
  1. Use R63's existing cross-sheet inventory tuples for K, Λ, Σ, Ξ,
     η, η′, φ, π (the strange/heavier hadrons that failed Track 4).
  2. Use R64's pure-p-sheet nucleon representation:
     proton = (0, 0, 0, 0, 3, +2)
     neutron = (0, 0, 0, 0, 3, −2)
     [N.B. R63's proton was (0, 0, 0, 0, 3, 6); R64's is (3, +2);
     this changes K_p anchoring]
  3. Use R64's Point B parameters on the p-sheet:
     ε_p = 0.2052, s_p = +0.0250 (chain-fit from Track 3)
  4. Use R63's existing e- and ν-sheet parameters as a starting point;
     these may need re-fitting if hybrid inventory fails.
  5. Compute predicted masses via block-diagonal three-sheet sum:
     m² = (2π ℏc / L_ring_e)² · μ²_e/k_e
        + (2π ℏc / L_ring_ν)² · μ²_ν/k_ν
        + (2π ℏc / L_ring_p)² · μ²_p/k_p
     with each L_ring anchored to its sheet's calibration particle.

Outputs:
  outputs/track5_hybrid_inventory.csv
"""

import math
import csv
from pathlib import Path


# ─── Constants and parameters ──────────────────────────────────────────

# PDG masses (MeV)
M_E = 0.51099895
M_P = 938.27208816
M_N = 939.56542052
M_NU = 3.21e-8  # representative ν mass (R63 used this for L_ring_ν)

# R64 Point B (chain-fit) p-sheet parameters
EPS_P = 0.2052
S_P   = 0.0250

# R63 working e- and ν-sheet parameters
EPS_E  = 397.074
S_E    = 2.0042
EPS_NU = 2.0
S_NU   = 0.022

# Sheet diagonal-scale (R59 F53)
K_MODELF = 1.1803 / (8 * math.pi)
K_E  = K_MODELF
K_NU = K_MODELF
K_P  = K_MODELF

# Constants
TWO_PI_HC = 2 * math.pi * 197.3269804  # MeV·fm (using ℏc = 197.327 MeV·fm)


# ─── Sheet primitive masses ────────────────────────────────────────────

def mu_sheet(n_t, n_r, eps, s):
    """μ on a single sheet."""
    return math.sqrt((n_t / eps)**2 + (n_r - s * n_t)**2)


def derive_L_ring(target_mass_MeV, n_t, n_r, eps, s, k):
    """L_ring such that mode_energy((n_t, n_r)) = target_mass on an
    isolated sheet with diagonal scale k."""
    mu = mu_sheet(n_t, n_r, eps, s)
    return TWO_PI_HC * mu / (target_mass_MeV * math.sqrt(k))


def total_mass(tup6, L_e, L_nu, L_p):
    """Three-sheet block-diagonal mass.

    tup6 = (n_et, n_er, n_νt, n_νr, n_pt, n_pr)
    """
    n_et, n_er, n_nut, n_nur, n_pt, n_pr = tup6
    mu2_e = (n_et / EPS_E)**2 + (n_er - S_E * n_et)**2
    mu2_n = (n_nut / EPS_NU)**2 + (n_nur - S_NU * n_nut)**2
    mu2_p = (n_pt / EPS_P)**2 + (n_pr - S_P * n_pt)**2
    m2 = (
        (TWO_PI_HC / L_e)**2  * mu2_e / K_E
        + (TWO_PI_HC / L_nu)**2 * mu2_n / K_NU
        + (TWO_PI_HC / L_p)**2  * mu2_p / K_P
    )
    return math.sqrt(m2)


# ─── Hybrid inventory ──────────────────────────────────────────────────
# R64-pure-p-sheet for nucleons; R63 cross-sheet for the rest.
# Tuple format: (n_et, n_er, n_νt, n_νr, n_pt, n_pr)

INVENTORY = [
    # R64 pure-p-sheet for foundational anchors
    ("electron",  (1, 2, 0, 0, 0, 0),         M_E,        "e-sheet (R64 anchor)"),
    ("proton",    (0, 0, 0, 0, 3, +2),         M_P,        "p-sheet R64 anchor (uud)"),
    ("neutron",   (0, 0, 0, 0, 3, -2),         M_N,        "p-sheet R64 (udd)"),
    # R63 cross-sheet representations for s/c/b/t-bearing hadrons
    ("Lambda",    (-3,  2,  1, -6, -3, -3),    1115.683,   "uds (R63 cross-sheet)"),
    ("Sigma_+",   ( 2, -3, -2, -6,  3,  6),    1189.37,    "uus (R63 cross-sheet)"),
    ("Sigma_-",   ( 4,  0, -2, -6,  3,  5),    1197.449,   "dds (R63 cross-sheet)"),
    ("Xi_-",      (-2,  4,  0, -6, -3,  6),    1321.71,    "dss (R63 cross-sheet)"),
    ("phi",       (-3, -6,  1, -6, -3,  6),    1019.461,   "ss̄ (R63 cross-sheet)"),
    ("eta_prime", ( 0, -6, -1, -6,  0, -6),    957.78,     "(R63 cross-sheet)"),
    ("K0",        ( 0, -1, -1, -6,  0, -4),    497.611,    "ds̄ (R63 cross-sheet)"),
    ("K_pm",      ( 1,  3, -2, -6,  0, -4),    493.677,    "us̄ (R63 cross-sheet)"),
    ("eta",       ( 0, -4, -1, -6,  0, -3),    547.862,    "(R63 cross-sheet)"),
    ("pi0",       ( 0,  0, -1, -6,  0, -1),    134.977,    "(R63 cross-sheet)"),
    ("pi_pm",     ( 1,  2, -2, -6,  0, -1),    139.570,    "ud̄ etc (R63 cross-sheet)"),
]


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 5 Phase 5a — Hybrid inventory audit (multi-sheet)")
    print("=" * 110)
    print()
    print("  Architecture (Q134 §0.1):")
    print(f"    p-sheet:      ε_p = {EPS_P}, s_p = {S_P:+}    (R64 Point B chain-fit)")
    print(f"    e-sheet:      ε_e = {EPS_E},  s_e = {S_E}    (R63 working)")
    print(f"    ν-sheet:      ε_ν = {EPS_NU},   s_ν = {S_NU}     (R63 working)")
    print()

    # Anchor each L_ring per sheet
    L_ring_e  = derive_L_ring(M_E,  1, 2, EPS_E,  S_E,  K_E)
    L_ring_p  = derive_L_ring(M_P,  3, 2, EPS_P,  S_P,  K_P)  # R64 anchor
    L_ring_nu = derive_L_ring(M_NU, 1, 1, EPS_NU, S_NU, K_NU)

    print(f"  Anchored L_ring values:")
    print(f"    L_ring_e = {L_ring_e:.6e} (fm units, anchored to electron at e(1,2))")
    print(f"    L_ring_p = {L_ring_p:.6e} (anchored to proton at p(3,+2))")
    print(f"    L_ring_ν = {L_ring_nu:.6e} (anchored to ν at ν(1,1))")
    print()

    # ─── Predicted masses ─────────────────────────────────────────────
    print(f"  {'particle':>10s}  {'tuple':>22s}  "
          f"{'observed':>10s}  {'predicted':>11s}  "
          f"{'err':>9s}  {'note':>30s}")
    print("  " + "─" * 100)

    rows = []
    errs_inventory = []
    for name, tup, m_obs, note in INVENTORY:
        m_pred = total_mass(tup, L_ring_e, L_ring_nu, L_ring_p)
        err = (m_pred - m_obs) / m_obs
        rows.append({
            'particle': name, 'tuple': str(tup),
            'observed': m_obs, 'predicted': m_pred,
            'rel_err': err, 'abs_err_pct': abs(err) * 100,
            'note': note,
        })
        # Skip anchors in the error stats
        if name not in ('electron', 'proton'):
            errs_inventory.append(err)
        flag = ""
        if abs(err) < 0.01:
            flag = "  ✓"
        elif abs(err) < 0.05:
            flag = "  ✓ (within 5% gate)"
        elif abs(err) < 0.20:
            flag = "  ! >5% off"
        else:
            flag = "  ✗ shattered"
        if name in ('electron', 'proton'):
            flag = "  (anchor)"
        print(f"  {name:>10s}  {str(tup):>22s}  "
              f"{m_obs:>10.3f}  {m_pred:>11.3f}  "
              f"{err:>+9.2%}{flag}")
    print()

    # ─── Stats ───────────────────────────────────────────────────────
    print(f"  Across {len(errs_inventory)} non-anchor particles:")
    print(f"    Mean |err|: {sum(abs(e) for e in errs_inventory)/len(errs_inventory):.2%}")
    print(f"    Max  |err|: {max(abs(e) for e in errs_inventory):.2%}")
    print(f"    RMS  err:   {math.sqrt(sum(e*e for e in errs_inventory)/len(errs_inventory)):.2%}")
    print()
    n_within_5 = sum(1 for e in errs_inventory if abs(e) < 0.05)
    n_within_20 = sum(1 for e in errs_inventory if abs(e) < 0.20)
    print(f"    Within 5%:   {n_within_5}/{len(errs_inventory)}")
    print(f"    Within 20%:  {n_within_20}/{len(errs_inventory)}")
    print()

    csv_path = out_dir / "track5_hybrid_inventory.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # ─── Verdict ─────────────────────────────────────────────────────
    print("=" * 110)
    print("VERDICT — Phase 5a")
    print("=" * 110)
    print()

    if max(abs(e) for e in errs_inventory) < 0.05:
        verdict = "INVENTORY PRESERVED — all within 5% gate."
    elif max(abs(e) for e in errs_inventory) < 0.10:
        verdict = "INVENTORY MARGINAL — within 10%, may need parameter refinement."
    elif n_within_5 >= len(errs_inventory) // 2:
        verdict = "INVENTORY MIXED — half within 5%, half outside."
    else:
        verdict = "INVENTORY SHATTERED — most particles outside gate."
    print(f"  → {verdict}")
    print()

    print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
