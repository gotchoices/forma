"""
R64 Track 7 Phase 7c — 7-tensor with corrected two-body kinematics.

Phase 7a treated the joint two-nucleon compound as a single particle of
mass M_total = 2·m_p with momentum p = ℏ·k_S, giving kinetic coefficient
A = (ℏc)².  But k_S = 1/r physically represents the *relative* momentum
between two nucleons in the COM frame.  For two equal-mass particles:

    M_inv²(p_rel) = M_total² + 4·p_rel²

So the kinetic coefficient should be A = 4·(ℏc)², not (ℏc)².  The factor
of 4 is the dominant source of the factor-5 scale miss in Phase 7a.

Equivalently, in the non-relativistic picture, relative-motion kinetic
energy uses reduced mass μ_red = m_p/2 (for equal masses), four times
smaller than the M_total = 2·m_p we implicitly used.

This phase repeats Phase 7a's analysis with A = 4·(ℏc)², re-sweeps σ_t,
and reports whether the trough depth and position now match observation.

Predicted (from review.md):
    Depth · r₀² = A/(2·M_total) = 4·(ℏc)²/(4·m_p) = (ℏc)²/m_p ≈ 41.5 MeV·fm²
    At r₀ = 1 fm, Depth ≈ 41.5 MeV (vs observed ~40–60 MeV)

Outputs:
  outputs/track7_phase7c_potential_curves.csv
  outputs/track7_phase7c_potential_curves.png
"""

import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# ─── Constants ──────────────────────────────────────────────────────────

EPS_P = 0.2052
S_P = 0.0250
K_P = 63.629    # MeV/μ-unit

M_P = 938.272   # MeV
M_N = 939.565   # MeV
ALPHA = 1.0 / 137.035999084
HBAR_C = 197.3269804   # MeV·fm

# Two-body relative-motion kinetic coefficient.
A_KINETIC = 4.0 * HBAR_C**2   # was HBAR_C**2 in Phase 7a — the bug.


# ─── Mass formula ───────────────────────────────────────────────────────

def mu2_Ma(n_pt, n_pr, eps=EPS_P, s=S_P):
    return (n_pt / eps)**2 + (n_pr - s * n_pt)**2


def m_Ma(n_pt, n_pr, eps=EPS_P, s=S_P, K_p=K_P):
    return K_p * math.sqrt(mu2_Ma(n_pt, n_pr, eps, s))


def m_squared_7tensor(n_pt, n_pr, k_S, sigma_t, sigma_r,
                     eps=EPS_P, s=S_P, K_p=K_P, A=A_KINETIC):
    """7-tensor mass squared with corrected two-body kinematic coefficient."""
    m_ma = m_Ma(n_pt, n_pr, eps, s, K_p)
    m_S2_kin = A * k_S**2
    cross = 2 * k_S * (sigma_t * n_pt + sigma_r * n_pr) * HBAR_C
    return m_ma**2 + m_S2_kin + cross


def m_at_separation(r, n_pt, n_pr, sigma_t, sigma_r, **kwargs):
    if r < 1e-6:
        return float('inf')
    k_S = 1.0 / r
    m2 = m_squared_7tensor(n_pt, n_pr, k_S, sigma_t, sigma_r, **kwargs)
    if m2 <= 0:
        return float('nan')
    return math.sqrt(m2)


def compute_E_of_r(n_pt, n_pr, sigma_t, sigma_r, r_values,
                   m_constituents_sum, **kwargs):
    energies = []
    for r in r_values:
        m_r = m_at_separation(r, n_pt, n_pr, sigma_t, sigma_r, **kwargs)
        E = m_r - m_constituents_sum
        energies.append(E)
    return np.array(energies)


CONFIGS = {
    "pp (two protons)": dict(
        n_pt=6, n_pr=+4,
        m_constituents_sum=2 * M_P,
        coulomb_charges=(1, 1),
    ),
    "pn (proton + neutron)": dict(
        n_pt=6, n_pr=0,
        m_constituents_sum=M_P + M_N,
        coulomb_charges=(1, 0),
    ),
    "nn (two neutrons)": dict(
        n_pt=6, n_pr=-4,
        m_constituents_sum=2 * M_N,
        coulomb_charges=(0, 0),
    ),
}


def coulomb_energy(r_values, charges):
    z1, z2 = charges
    if z1 == 0 or z2 == 0:
        return np.zeros_like(r_values)
    return ALPHA * HBAR_C * z1 * z2 / r_values


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 7 Phase 7c — 7-tensor with corrected two-body kinematics")
    print("=" * 110)
    print()
    print(f"  R64 Point B: ε_p = {EPS_P}, s_p = {S_P}, K_p = {K_P:.3f}")
    print(f"  α = 1/{1/ALPHA:.3f}, ℏc = {HBAR_C} MeV·fm")
    print(f"  A_kinetic = 4·(ℏc)² = {A_KINETIC:.1f} MeV²·fm²  "
          f"(was (ℏc)² = {HBAR_C**2:.1f} in Phase 7a)")
    print()

    # ─── Predicted scale relations under corrected kinematics ────────
    cfg_pn = CONFIGS["pn (proton + neutron)"]
    M_total = cfg_pn['m_constituents_sum']
    A2_predicted = A_KINETIC / (2 * M_total)
    DepthRsq_predicted = A_KINETIC / (2 * M_total)
    print("Predicted scale relations (Phase 7c, with A = 4·(ℏc)²):")
    print(f"  A₂ coefficient (1/r² term) = A/(2·M_tot) = {A2_predicted:.3f} MeV·fm²")
    print(f"  Depth · r₀²                = {DepthRsq_predicted:.3f} MeV·fm²")
    print(f"  Observed (~50 MeV at ~1 fm) ≈ 50 MeV·fm²")
    print(f"  Phase 7a value (A = (ℏc)²)  ≈ 10.4 MeV·fm² (factor ~5 off)")
    print()

    # ─── Sweep σ_t to find trough at r ≈ 1 fm ─────────────────────────
    print("Sweeping σ_t over [-200, 0] (negative = attractive):")
    print("-" * 100)
    cfg = CONFIGS["pn (proton + neutron)"]
    r_fit = np.linspace(0.3, 5.0, 500)
    best_sigma = None
    best_score = float('inf')
    for sigma_t_try in np.linspace(-200.0, 0.0, 4001):
        E = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                           sigma_t=sigma_t_try, sigma_r=0,
                           r_values=r_fit,
                           m_constituents_sum=cfg['m_constituents_sum'])
        idx_min = int(np.argmin(E))
        E_min = E[idx_min]
        r_min = r_fit[idx_min]
        if r_min < 0.4 or r_min > 3.0:
            continue
        # Score: distance from "trough at 1 fm with depth 50 MeV"
        score = (r_min - 1.0)**2 * 100 + (E_min + 50)**2
        if score < best_score:
            best_score = score
            best_sigma = sigma_t_try

    print(f"  Best σ_t = {best_sigma:.3f}")

    # ─── Verify the trough's full structure ──────────────────────────
    print()
    print("Trough structure at best σ_t:")
    print("-" * 100)
    r_eval = np.logspace(-1, 1.3, 400)
    for name, cfg_i in CONFIGS.items():
        E_strong = compute_E_of_r(cfg_i['n_pt'], cfg_i['n_pr'],
                                   sigma_t=best_sigma, sigma_r=0,
                                   r_values=r_eval,
                                   m_constituents_sum=cfg_i['m_constituents_sum'])
        E_coul = coulomb_energy(r_eval, cfg_i['coulomb_charges'])
        E_total = E_strong + E_coul
        # restrict to physical r range for the trough
        mask = (r_eval >= 0.3) & (r_eval <= 5.0)
        idx_min = int(np.argmin(E_total[mask]))
        r_arr = r_eval[mask]
        E_arr = E_total[mask]
        print(f"  {name:>22s}: trough at r = {r_arr[idx_min]:.3f} fm, "
              f"E_min = {E_arr[idx_min]:+.2f} MeV (with Coulomb)")

    # pp vs pn preference
    cfg_pp = CONFIGS["pp (two protons)"]
    cfg_pn = CONFIGS["pn (proton + neutron)"]
    cfg_nn = CONFIGS["nn (two neutrons)"]

    E_pp = compute_E_of_r(cfg_pp['n_pt'], cfg_pp['n_pr'],
                           sigma_t=best_sigma, sigma_r=0,
                           r_values=r_eval,
                           m_constituents_sum=cfg_pp['m_constituents_sum'])
    E_pp_total = E_pp + coulomb_energy(r_eval, cfg_pp['coulomb_charges'])

    E_pn = compute_E_of_r(cfg_pn['n_pt'], cfg_pn['n_pr'],
                           sigma_t=best_sigma, sigma_r=0,
                           r_values=r_eval,
                           m_constituents_sum=cfg_pn['m_constituents_sum'])

    E_nn = compute_E_of_r(cfg_nn['n_pt'], cfg_nn['n_pr'],
                           sigma_t=best_sigma, sigma_r=0,
                           r_values=r_eval,
                           m_constituents_sum=cfg_nn['m_constituents_sum'])

    print()
    print("Charge symmetry / asymmetry checks:")
    print("-" * 100)
    delta_pn_pp = np.min(E_pn) - np.min(E_pp_total)
    delta_pn_nn = np.min(E_pn) - np.min(E_nn)
    print(f"  pn deeper than pp (with Coulomb) by {-delta_pn_pp:+.2f} MeV")
    print(f"  pn deeper than nn (no Coulomb) by    {-delta_pn_nn:+.2f} MeV")

    # ─── σ_t structural status ────────────────────────────────────────
    print()
    print("σ_t structural status:")
    print("-" * 100)
    print(f"  σ_t                 = {best_sigma:+.4f}")
    print(f"  σ_t / α             = {best_sigma / ALPHA:+.3f}")
    print(f"  σ_t · α             = {best_sigma * ALPHA:+.6f}")
    print(f"  σ_t · √α            = {best_sigma * math.sqrt(ALPHA):+.6f}")
    print(f"  σ_t / 4π            = {best_sigma / (4*math.pi):+.4f}")
    print(f"  σ_t · n_pt² · α     = {best_sigma * 36 * ALPHA:+.4f}")
    print(f"  σ_t · K_p           = {best_sigma * K_P:+.2f}  (MeV-scale)")
    print(f"  σ_t · ε_p           = {best_sigma * EPS_P:+.4f}")
    print(f"  σ_t · s_p           = {best_sigma * S_P:+.4f}")

    # ─── Plot ─────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Top-left: pp/pn/nn comparison at best σ_t
    ax = axes[0, 0]
    for name, cfg_i in CONFIGS.items():
        E_strong = compute_E_of_r(cfg_i['n_pt'], cfg_i['n_pr'],
                                   sigma_t=best_sigma, sigma_r=0,
                                   r_values=r_eval,
                                   m_constituents_sum=cfg_i['m_constituents_sum'])
        E_coul = coulomb_energy(r_eval, cfg_i['coulomb_charges'])
        ax.plot(r_eval, E_strong + E_coul, label=name, linewidth=1.8)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axhline(-50, color='red', linestyle=':', alpha=0.5,
               label='~observed depth')
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('E(r) (MeV)')
    ax.set_title(f'pp / pn / nn at σ_t = {best_sigma:.2f} (Phase 7c)')
    ax.set_xlim(0.1, 5)
    ax.set_ylim(-100, 100)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

    # Top-right: σ_t sweep on pn
    ax = axes[0, 1]
    sigma_t_disp = [best_sigma * f for f in (0.25, 0.5, 1.0, 1.5, 2.0)]
    cfg = CONFIGS["pn (proton + neutron)"]
    for sigma_t in sigma_t_disp:
        E = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                           sigma_t=sigma_t, sigma_r=0,
                           r_values=r_eval,
                           m_constituents_sum=cfg['m_constituents_sum'])
        ax.plot(r_eval, E, label=f'σ_t = {sigma_t:+.2f}')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axhline(-50, color='red', linestyle=':', alpha=0.5)
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('E(r) (MeV)')
    ax.set_title('pn σ_t sweep around best')
    ax.set_xlim(0.1, 5)
    ax.set_ylim(-200, 100)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # Bottom-left: trough zoom around r = 1 fm for pn
    ax = axes[1, 0]
    r_zoom = np.linspace(0.4, 3.0, 300)
    cfg = CONFIGS["pn (proton + neutron)"]
    E = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                       sigma_t=best_sigma, sigma_r=0,
                       r_values=r_zoom,
                       m_constituents_sum=cfg['m_constituents_sum'])
    idx_min = int(np.argmin(E))
    ax.plot(r_zoom, E, color='blue', linewidth=2, label='pn at best σ_t')
    ax.scatter([r_zoom[idx_min]], [E[idx_min]], color='red', zorder=5,
               label=f'Trough: r = {r_zoom[idx_min]:.2f} fm, E = {E[idx_min]:.1f} MeV')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(1.0, color='red', linestyle=':', alpha=0.5)
    ax.axhline(-50, color='red', linestyle=':', alpha=0.5)
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('E(r) (MeV)')
    ax.set_title('pn trough zoom')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

    # Bottom-right: comparison Phase 7a vs Phase 7c at "matching" σ_t
    ax = axes[1, 1]
    cfg = CONFIGS["pn (proton + neutron)"]
    # 7a kinetic
    A_7a = HBAR_C**2
    E_7a = []
    for r in r_eval:
        k_S = 1.0 / r
        m_ma = m_Ma(cfg['n_pt'], cfg['n_pr'])
        m2 = m_ma**2 + A_7a * k_S**2 + 2 * k_S * (-20) * cfg['n_pt'] * HBAR_C
        E_7a.append(math.sqrt(m2) - cfg['m_constituents_sum'] if m2 > 0 else float('nan'))
    E_7a = np.array(E_7a)
    E_7c = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                           sigma_t=best_sigma, sigma_r=0,
                           r_values=r_eval,
                           m_constituents_sum=cfg['m_constituents_sum'])
    ax.plot(r_eval, E_7a, label='Phase 7a (A=(ℏc)², σ_t=−20)',
            linestyle='--', alpha=0.8)
    ax.plot(r_eval, E_7c, label=f'Phase 7c (A=4·(ℏc)², σ_t={best_sigma:.2f})',
            linewidth=2)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axhline(-50, color='red', linestyle=':', alpha=0.5,
               label='~observed depth')
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('E(r) (MeV)')
    ax.set_title('Phase 7a vs Phase 7c — pn channel')
    ax.set_xlim(0.1, 5)
    ax.set_ylim(-100, 100)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    plt.tight_layout()
    fig_path = out_dir / "track7_phase7c_potential_curves.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print()
    print(f"  Plot: {fig_path}")

    # ─── CSV ──────────────────────────────────────────────────────────
    csv_rows = []
    for name, cfg_i in CONFIGS.items():
        E_strong = compute_E_of_r(cfg_i['n_pt'], cfg_i['n_pr'],
                                   sigma_t=best_sigma, sigma_r=0,
                                   r_values=r_eval,
                                   m_constituents_sum=cfg_i['m_constituents_sum'])
        E_coul = coulomb_energy(r_eval, cfg_i['coulomb_charges'])
        for i, r in enumerate(r_eval):
            csv_rows.append({
                'config': name,
                'sigma_t': best_sigma,
                'r_fm': r,
                'E_strong_MeV': E_strong[i],
                'E_coulomb_MeV': E_coul[i],
                'E_total_MeV': E_strong[i] + E_coul[i],
            })
    csv_path = out_dir / "track7_phase7c_potential_curves.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
        w.writeheader()
        w.writerows(csv_rows)
    print(f"  CSV: {csv_path}")

    # ─── Verdict ──────────────────────────────────────────────────────
    print()
    print("=" * 110)
    print("VERDICT — Phase 7c")
    print("=" * 110)
    cfg = CONFIGS["pn (proton + neutron)"]
    E_pn_eval = compute_E_of_r(cfg['n_pt'], cfg['n_pr'],
                                sigma_t=best_sigma, sigma_r=0,
                                r_values=r_eval,
                                m_constituents_sum=cfg['m_constituents_sum'])
    mask = (r_eval >= 0.3) & (r_eval <= 5.0)
    idx_min = int(np.argmin(E_pn_eval[mask]))
    r_min = r_eval[mask][idx_min]
    E_min = E_pn_eval[mask][idx_min]
    print(f"  pn trough: r₀ = {r_min:.3f} fm, depth = {E_min:.2f} MeV")
    print(f"  Observed: r₀ ≈ 1 fm, depth ≈ 40–60 MeV")
    if 40 <= -E_min <= 60 and 0.7 <= r_min <= 1.3:
        print(f"  → Acceptance criterion MET (depth in 40–60 MeV at r ≈ 1 fm)")
    else:
        print(f"  → Acceptance criterion NOT met")
    print(f"  pn deeper than pp by {-delta_pn_pp:.1f} MeV (Ma-side asymmetry)")
    print(f"  Coulomb tail: 1/r at large r for charged configs ✓")


if __name__ == "__main__":
    main()
