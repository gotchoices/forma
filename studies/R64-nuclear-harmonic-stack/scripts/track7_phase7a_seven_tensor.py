"""
R64 Track 7 Phase 7a — 7-tensor first-principles strong-force exploration.

Build a 7×7 metric with the T⁶ Ma block (R64 Point B p-sheet plus R63
e- and ν-sheet baselines, though only p-sheet matters for this phase)
plus 1 abstract S spatial dimension.  Compute the energy of a two-
particle p-sheet configuration as a function of S separation r,
sweeping the cross-shear coupling between p-sheet and S.

The user's framing: "Ma couples to S at 1/α just as Coulomb does."
That coupling is structural; we don't derive it here.  We treat the
specific σ values as free parameters to sweep, with the natural
1/L_S² kinetic term anchored at (ℏc)² (the relativistic kinetic
scale).

Mass-squared formula (7-tensor diagonal + cross-shear in p-sheet × S):

    m²(n_pt, n_pr, k_S) = m²_Ma + A · k_S² + 2·k_S·(σ_t·n_pt + σ_r·n_pr)·ℏc

where:
  m²_Ma comes from R64 Point B mass formula
  A = (ℏc)² is the natural S-kinetic scale
  σ_t, σ_r are p-sheet × S cross-shears (free, dimensionless)
  k_S = 1/r in fm⁻¹ (de Broglie wave number for separation r)

For two-proton state: additive winding (n_pt, n_pr) = (6, +4).
For proton+neutron (deuteron): (6, 0).
For two-neutron: (6, −4).

Energy difference: E(r) = m(r) − m(r → ∞).

If the 7-tensor naturally produces:
  - Trough at r ≈ 1 fm with depth ~50 MeV
  - Coulomb-like 1/r tail at large r
  - Hard-core repulsion at r → 0

Then MaSt has produced the strong-force shape from geometric
consistency.

Outputs:
  outputs/track7_phase7a_potential_curves.csv
  outputs/track7_phase7a_potential_curves.png
"""

import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# ─── Constants ──────────────────────────────────────────────────────────

# R64 Point B p-sheet parameters
EPS_P = 0.2052
S_P = 0.0250
K_P = 63.629    # MeV/μ-unit

M_P = 938.272   # MeV
M_N = 939.565   # MeV
ALPHA = 1.0 / 137.035999084
HBAR_C = 197.3269804   # MeV·fm


# ─── Mass formula ───────────────────────────────────────────────────────

def mu2_Ma(n_pt, n_pr, eps=EPS_P, s=S_P):
    """R64 Ma mass-squared in dimensionless μ² units."""
    return (n_pt / eps)**2 + (n_pr - s * n_pt)**2


def m_Ma(n_pt, n_pr, eps=EPS_P, s=S_P, K_p=K_P):
    return K_p * math.sqrt(mu2_Ma(n_pt, n_pr, eps, s))


def m_squared_7tensor(n_pt, n_pr, k_S, sigma_t, sigma_r,
                     eps=EPS_P, s=S_P, K_p=K_P, A=HBAR_C**2):
    """7-tensor mass squared at a given (n_pt, n_pr, k_S).

    Parameters
    ----------
    n_pt, n_pr : int
        Ma p-sheet quantum numbers (compound winding for the joint state).
    k_S : float
        S-momentum (fm⁻¹).
    sigma_t, sigma_r : float
        Cross-shears between p-sheet (tube/ring) and S (dimensionless).
    A : float
        S-kinetic coefficient (default (ℏc)²).
    """
    m_ma = m_Ma(n_pt, n_pr, eps, s, K_p)
    # S kinetic
    m_S2_kin = A * k_S**2
    # Cross terms
    cross = 2 * k_S * (sigma_t * n_pt + sigma_r * n_pr) * HBAR_C
    return m_ma**2 + m_S2_kin + cross


def m_at_separation(r, n_pt, n_pr, sigma_t, sigma_r, **kwargs):
    """Compound mass at S-separation r.  k_S = 1/r."""
    if r < 1e-6:
        return float('inf')
    k_S = 1.0 / r
    m2 = m_squared_7tensor(n_pt, n_pr, k_S, sigma_t, sigma_r, **kwargs)
    if m2 <= 0:
        return float('nan')
    return math.sqrt(m2)


# ─── Compute E(r) ─────────────────────────────────────────────────────

def compute_E_of_r(n_pt, n_pr, sigma_t, sigma_r, r_values,
                   m_constituents_sum, **kwargs):
    """Compute E(r) = m_compound(r) − m_constituents_sum.

    For two protons: m_constituents_sum = 2·m_p.
    For proton+neutron: m_constituents_sum = m_p + m_n.
    """
    energies = []
    for r in r_values:
        m_r = m_at_separation(r, n_pt, n_pr, sigma_t, sigma_r, **kwargs)
        E = m_r - m_constituents_sum
        energies.append(E)
    return np.array(energies)


# ─── Two-particle configurations ──────────────────────────────────────

CONFIGS = {
    "pp (two protons)": dict(
        n_pt=6, n_pr=+4,
        m_constituents_sum=2 * M_P,
        coulomb_charges=(1, 1),  # Z₁·Z₂ = 1 (two +e protons)
    ),
    "pn (proton + neutron)": dict(
        n_pt=6, n_pr=0,
        m_constituents_sum=M_P + M_N,
        coulomb_charges=(1, 0),  # no Coulomb between p and neutral n
    ),
    "nn (two neutrons)": dict(
        n_pt=6, n_pr=-4,
        m_constituents_sum=2 * M_N,
        coulomb_charges=(0, 0),
    ),
}


# ─── Coulomb addition ─────────────────────────────────────────────────

def coulomb_energy(r_values, charges):
    """Standard EM Coulomb energy between two charges at separation r."""
    z1, z2 = charges
    if z1 == 0 or z2 == 0:
        return np.zeros_like(r_values)
    return ALPHA * HBAR_C * z1 * z2 / r_values


# ─── Main ─────────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 7 Phase 7a — 7-tensor strong-force exploration")
    print("=" * 110)
    print()
    print(f"  Setup: T⁶ Ma block (R64 Point B p-sheet) + 1 abstract S spatial dim")
    print(f"  R64 Point B: ε_p = {EPS_P}, s_p = {S_P}, K_p = {K_P:.3f}")
    print(f"  α = 1/{1/ALPHA:.3f}, ℏc = {HBAR_C} MeV·fm")
    print(f"  Two-particle configurations:")
    for name, cfg in CONFIGS.items():
        print(f"    {name:>22s}: (n_pt, n_pr) = ({cfg['n_pt']}, "
              f"{cfg['n_pr']:+d}), constituents sum = "
              f"{cfg['m_constituents_sum']:.3f} MeV")
    print()

    # ─── Sanity check: R64 Ma masses at zero-S ────────────────────────
    print("Ma masses (no S coupling):")
    print("-" * 100)
    for name, cfg in CONFIGS.items():
        m_ma = m_Ma(cfg['n_pt'], cfg['n_pr'])
        e_ma = m_ma - cfg['m_constituents_sum']
        print(f"  {name:>22s}: m_Ma = {m_ma:.3f} MeV, "
              f"E_Ma = {e_ma:+.3f} MeV (vs constituent sum)")
    print()

    # ─── Sweep σ_t (sigma_pt_S, tube↔S coupling) — charge-independent ─
    r_values = np.logspace(-1, 1.3, 200)  # 0.1 to ~20 fm

    print("Sweeping σ_t (cross-shear between p-sheet TUBE and S):")
    print("σ_t couples to n_pt=6 in all configs equally → charge-independent.")
    print("σ_r set to 0 (would give charge-dependent strong force, which is wrong).")
    print("-" * 100)

    sigma_t_values = [-0.01, -0.05, -0.1, -0.5, -1.0, -2.0, -5.0, -10.0]
    print(f"  σ_t values (negative = attractive): {sigma_t_values}")
    print()

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Top-left: pp at various σ_r values
    ax = axes[0, 0]
    cfg = CONFIGS["pp (two protons)"]
    for sigma_t in sigma_t_values:
        E_strong = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                                   sigma_t=sigma_t, sigma_r=0,
                                   r_values=r_values,
                                   m_constituents_sum=cfg['m_constituents_sum'])
        E_coulomb = coulomb_energy(r_values, cfg['coulomb_charges'])
        E_total = E_strong + E_coulomb
        ax.plot(r_values, E_total, label=f'σ_t = {sigma_t:+.3f}')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('E(r) (MeV)')
    ax.set_title('pp: 7-tensor + Coulomb at various σ_r')
    ax.set_xlim(0.1, 5)
    ax.set_ylim(-100, 100)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc='upper right')

    # Top-right: pn (no Coulomb)
    ax = axes[0, 1]
    cfg = CONFIGS["pn (proton + neutron)"]
    for sigma_t in sigma_t_values:
        E_strong = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                                   sigma_t=sigma_t, sigma_r=0,
                                   r_values=r_values,
                                   m_constituents_sum=cfg['m_constituents_sum'])
        E_total = E_strong  # no Coulomb
        ax.plot(r_values, E_total, label=f'σ_t = {sigma_t:+.3f}')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('E(r) (MeV)')
    ax.set_title('pn: 7-tensor only (no Coulomb)')
    ax.set_xlim(0.1, 5)
    ax.set_ylim(-100, 100)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc='upper right')

    # Bottom-left: pp/pn/nn comparison at one fixed σ_t
    sigma_t_chosen = -1.0
    ax = axes[1, 0]
    for name, cfg in CONFIGS.items():
        E_strong = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                                   sigma_t=sigma_t_chosen, sigma_r=0,
                                   r_values=r_values,
                                   m_constituents_sum=cfg['m_constituents_sum'])
        E_coulomb = coulomb_energy(r_values, cfg['coulomb_charges'])
        E_total = E_strong + E_coulomb
        ax.plot(r_values, E_total, label=name)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('E(r) (MeV)')
    ax.set_title(f'pp / pn / nn at σ_t = {sigma_t_chosen}')
    ax.set_xlim(0.1, 5)
    ax.set_ylim(-100, 100)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

    # Bottom-right: zoom on the trough region for pn
    ax = axes[1, 1]
    cfg = CONFIGS["pn (proton + neutron)"]
    r_zoom = np.linspace(0.3, 3.0, 200)
    sigma_t_zoom_values = [-0.5, -1.0, -2.0, -5.0]
    for sigma_t in sigma_t_zoom_values:
        E = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                            sigma_t=sigma_t, sigma_r=0,
                            r_values=r_zoom,
                            m_constituents_sum=cfg['m_constituents_sum'])
        # Find minimum (trough)
        idx_min = int(np.argmin(E))
        ax.plot(r_zoom, E, label=f'σ_t = {sigma_t}, min E = '
                f'{E[idx_min]:.1f} MeV at r = {r_zoom[idx_min]:.2f} fm')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axhline(-50, color='red', linestyle=':', alpha=0.5,
               label='~observed depth')
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('E(r) (MeV)')
    ax.set_title('pn trough zoom (σ_t negative)')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(out_dir / "track7_phase7a_potential_curves.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    # ─── Find σ_t that gives ~50 MeV trough at ~1 fm for pn ────────────
    print("Fitting σ_t to give ~50 MeV trough at ~1 fm for pn:")
    print("-" * 100)
    cfg = CONFIGS["pn (proton + neutron)"]
    r_fit = np.linspace(0.3, 3.0, 200)
    best_sigma = None
    best_diff = float('inf')
    for sigma_t_try in np.linspace(-20, 0, 401):
        E = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                           sigma_t=sigma_t_try, sigma_r=0,
                           r_values=r_fit,
                           m_constituents_sum=cfg['m_constituents_sum'])
        idx_min = int(np.argmin(E))
        E_min = E[idx_min]
        r_min = r_fit[idx_min]
        # Score: how close are we to (-50 MeV at 1 fm)?
        diff = (E_min + 50)**2 + (r_min - 1.0)**2 * 100
        if diff < best_diff and r_min < 2.5:
            best_diff = diff
            best_sigma = sigma_t_try

    if best_sigma is not None:
        E = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                            sigma_t=best_sigma, sigma_r=0,
                            r_values=r_fit,
                            m_constituents_sum=cfg['m_constituents_sum'])
        idx_min = int(np.argmin(E))
        print(f"  Best σ_t ≈ {best_sigma:.3f}")
        print(f"  Trough: r = {r_fit[idx_min]:.3f} fm, "
              f"E_min = {E[idx_min]:.2f} MeV")
        print(f"  Observed nuclear potential: r₀ ≈ 1.0 fm, depth ~50 MeV")

        # What's σ_t in α units?
        print()
        print(f"  Comparison of σ_t to α-related quantities:")
        print(f"    α = {ALPHA:.6f}, 1/α = {1/ALPHA:.3f}")
        print(f"    σ_t / α      = {best_sigma / ALPHA:+.3f}")
        print(f"    σ_t · α      = {best_sigma * ALPHA:+.6f}")
        print(f"    σ_t · √α     = {best_sigma * math.sqrt(ALPHA):+.6f}")
    print()

    # ─── Save curves CSV ──────────────────────────────────────────
    csv_rows = []
    for sigma_t in sigma_t_values:
        for name, cfg in CONFIGS.items():
            E = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                                sigma_t=sigma_t, sigma_r=0,
                                r_values=r_values,
                                m_constituents_sum=cfg['m_constituents_sum'])
            E_coul = coulomb_energy(r_values, cfg['coulomb_charges'])
            for i, r in enumerate(r_values):
                csv_rows.append({
                    'config': name,
                    'sigma_t': sigma_t,
                    'r_fm': r,
                    'E_strong_MeV': E[i],
                    'E_coulomb_MeV': E_coul[i],
                    'E_total_MeV': E[i] + E_coul[i],
                })

    csv_path = out_dir / "track7_phase7a_potential_curves.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
        w.writeheader()
        w.writerows(csv_rows)
    print(f"  CSV: {csv_path}")
    print(f"  Plot: {out_dir / 'track7_phase7a_potential_curves.png'}")

    # ─── Verdict ──────────────────────────────────────────────────
    print()
    print("=" * 110)
    print("VERDICT — Phase 7a")
    print("=" * 110)
    print()

    # Check victory criterion 1: shape of E(r)
    cfg = CONFIGS["pn (proton + neutron)"]
    if best_sigma is not None:
        E = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                            sigma_t=best_sigma, sigma_r=0,
                            r_values=r_values,
                            m_constituents_sum=cfg['m_constituents_sum'])
        E_far = E[-1]  # at r = 20 fm
        E_min = np.min(E)
        has_trough = E_min < -10 and E_min < E_far - 20
        print(f"  Criterion 1 (shape): trough at r₀ ≈ {r_fit[int(np.argmin(E[:len(r_fit)]))]:.2f} fm, "
              f"depth {E_min:.1f} MeV.  E(∞) = {E_far:.2f} MeV.")
        print(f"    Clear trough present: {has_trough}")

    if best_sigma is not None:
        cfg_pp = CONFIGS["pp (two protons)"]
        cfg_pn = CONFIGS["pn (proton + neutron)"]
        E_pp = compute_E_of_r(cfg_pp['n_pt'], cfg_pp['n_pr'],
                               sigma_t=best_sigma, sigma_r=0,
                               r_values=r_fit,
                               m_constituents_sum=cfg_pp['m_constituents_sum'])
        E_pp_total = E_pp + coulomb_energy(r_fit, cfg_pp['coulomb_charges'])
        E_pn = compute_E_of_r(cfg_pn['n_pt'], cfg_pn['n_pr'],
                               sigma_t=best_sigma, sigma_r=0,
                               r_values=r_fit,
                               m_constituents_sum=cfg_pn['m_constituents_sum'])
        print()
        print(f"  Criterion 4 (marginal preference): at σ_t = {best_sigma:.3f}:")
        print(f"    pp min binding: {np.min(E_pp_total):.2f} MeV at r = "
              f"{r_fit[int(np.argmin(E_pp_total))]:.2f} fm")
        print(f"    pn min binding: {np.min(E_pn):.2f} MeV at r = "
              f"{r_fit[int(np.argmin(E_pn))]:.2f} fm")
        diff = np.min(E_pn) - np.min(E_pp_total)
        print(f"    pn binding deeper by {-diff:.2f} MeV than pp")
        if diff < 0:
            print(f"    → System prefers pn over pp (matches nuclear stability)")
        else:
            print(f"    → System prefers pp over pn (does NOT match observation)")


if __name__ == "__main__":
    main()
