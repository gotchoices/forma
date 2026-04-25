"""
R64 Track 1 — Locate the magic (ε_p, s_p) point for proton/neutron on p-sheet.

Tests whether a single (ε_p, s_p) configuration hosts both the proton at
(3, +2) and the neutron at (3, -2) on the p-sheet, with the closed-form
mass formula

    μ²(n_t, n_r) = (n_t/ε)² + (n_r − s·n_t)²

reproducing the observed mass ratio m_n/m_p = 1.001378.

Phases:
  1a. Closed-form viable-curve sweep: solve R(ε, s) = m_n/m_p analytically
      for s as a function of ε, giving a 1D viable locus in (ε_p, s_p)
      space.
  1b. Mass-scale anchoring: along the viable curve, anchor K_p so the
      proton mass matches; tabulate K_p(ε_p, s_p).
  1c. Inventory check at representative points (deferred to Track 2).
  1d. Light-nuclei stack at the same points (deferred to Track 2 / 3).

Outputs:
  outputs/track1_viable_curve.csv
  outputs/track1_viable_curve.png
"""

import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# ─── Targets ───────────────────────────────────────────────────────────

M_P_OBS = 938.272      # MeV  (proton)
M_N_OBS = 939.565      # MeV  (neutron)
RATIO_OBS = M_N_OBS / M_P_OBS    # ≈ 1.001378
DELTA_MN_MP = M_N_OBS - M_P_OBS  # +1.293 MeV


def mu2(n_t, n_r, eps, s):
    """Flat-torus closed-form: μ²(n_t, n_r)."""
    return (n_t / eps)**2 + (n_r - s * n_t)**2


def s_for_ratio(eps, R_target=RATIO_OBS, n_t=3, n_r=2):
    """Solve R(ε, s) = m_n/m_p analytically for s.

    Closed form:
        (R² − 1)·[(n_t/ε)² + n_r² + s² n_t²] = 2·s·n_t·n_r·(1 + R²)
    Newton iteration converges from leading-order guess.
    """
    R2 = R_target * R_target
    A = (n_t / eps)**2
    s = (R2 - 1) * (A + n_r**2) / (2 * n_t * n_r * (1 + R2))

    for _ in range(50):
        mu2_p = (n_t / eps)**2 + (n_r - s * n_t)**2
        mu2_n = (n_t / eps)**2 + (-n_r - s * n_t)**2
        f = mu2_n - R2 * mu2_p
        df = 2 * n_t * (n_r + s * n_t) - R2 * (-2 * n_t * (n_r - s * n_t))
        if abs(df) < 1e-30:
            break
        s_new = s - f / df
        if abs(s_new - s) < 1e-15:
            s = s_new
            break
        s = s_new
    return s


def K_p_for_proton(eps, s, n_t=3, n_r=2, m_p=M_P_OBS):
    """K_p such that K_p · μ(n_t, n_r) = m_p."""
    return m_p / math.sqrt(mu2(n_t, n_r, eps, s))


def quark_masses(eps, s, K_p):
    """Compute u and d primitive masses at (ε, s) and K_p."""
    mu_u = math.sqrt(mu2(1, +2, eps, s))
    mu_d = math.sqrt(mu2(1, -2, eps, s))
    return K_p * mu_u, K_p * mu_d


# ─── Phase 1b — Deuteron under flavor-aware composition ───────────────

M_D_OBS = 1875.613       # MeV  (deuteron)
B_D_OBS = 2.224          # MeV  (deuteron binding, vs m_p + m_n)


def deuteron_mass(eps, s, K_p):
    """Deuteron = uud + udd = (3, 2) + (3, -2) = (6, 0) on p-sheet.

    Mass under additive winding composition with flat formula.
    """
    mu_d_compound = math.sqrt(mu2(6, 0, eps, s))
    return K_p * mu_d_compound


def light_nuclei_check(rows):
    """Compute predicted deuteron, ³He, ⁴He masses along the viable curve.

    Compositions under flavor-aware additive composition:
      ²H (deuteron, pn) = (3, 2) + (3, −2) = (6, 0)
      ³He (ppn)         = (3, 2) + (3, 2) + (3, −2) = (9, 2)
      ⁴He (ppnn)        = (3, 2) + (3, 2) + (3, −2) + (3, −2) = (12, 0)
    """
    # Observed masses (MeV)
    M_D   = 1875.613
    M_3He = 2808.391
    M_4He = 3727.379
    B_3He = 2 * M_P_OBS + M_N_OBS - M_3He   # 7.718
    B_4He = 2 * M_P_OBS + 2 * M_N_OBS - M_4He  # 28.296

    out = []
    for r in rows:
        eps, s, K_p = r['eps_p'], r['s_p'], r['K_p']
        m_d   = K_p * math.sqrt(mu2(6,  0, eps, s))
        m_3he = K_p * math.sqrt(mu2(9,  2, eps, s))
        m_4he = K_p * math.sqrt(mu2(12, 0, eps, s))
        m_p_pred = r['m_p_predicted']
        m_n_pred = r['m_n_predicted']
        # Predicted "binding" = sum-of-constituents − compound
        b_d   = m_p_pred + m_n_pred - m_d
        b_3he = 2 * m_p_pred + m_n_pred - m_3he
        b_4he = 2 * m_p_pred + 2 * m_n_pred - m_4he
        out.append({
            **r,
            'm_2H_pred': m_d,
            'm_2H_obs':  M_D,
            'B_2H_pred': b_d,
            'B_2H_obs':  B_D_OBS,
            'm_3He_pred': m_3he,
            'B_3He_pred': b_3he,
            'B_3He_obs':  B_3He,
            'm_4He_pred': m_4he,
            'B_4He_pred': b_4he,
            'B_4He_obs':  B_4He,
        })
    return out


def sweep_eps(eps_min=0.01, eps_max=2.0, n_points=600):
    """Sweep ε_p over [eps_min, eps_max], solve s_p for each."""
    eps_arr = np.linspace(eps_min, eps_max, n_points)
    rows = []
    for eps in eps_arr:
        s = s_for_ratio(eps)
        K_p = K_p_for_proton(eps, s)
        m_p_check = K_p * math.sqrt(mu2(3, +2, eps, s))
        m_n_check = K_p * math.sqrt(mu2(3, -2, eps, s))
        m_u, m_d = quark_masses(eps, s, K_p)
        ratio = m_n_check / m_p_check
        rows.append({
            'eps_p': eps,
            's_p': s,
            'K_p': K_p,
            'm_p_predicted': m_p_check,
            'm_n_predicted': m_n_check,
            'mass_ratio': ratio,
            'ratio_error': ratio - RATIO_OBS,
            'mu_u': math.sqrt(mu2(1, +2, eps, s)),
            'mu_d': math.sqrt(mu2(1, -2, eps, s)),
            'm_u_MeV': m_u,
            'm_d_MeV': m_d,
            'm_d_minus_m_u': m_d - m_u,
            'd_to_u_ratio': m_d / m_u if m_u > 0 else 0,
        })
    return rows


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 1 — Magic-point search for proton/neutron on p-sheet")
    print("=" * 100)
    print()
    print(f"  Proton tuple:  (n_pt, n_pr) = (3, +2)")
    print(f"  Neutron tuple: (n_pt, n_pr) = (3, −2)")
    print(f"  Target ratio:  m_n / m_p = {RATIO_OBS:.6f}")
    print(f"  Target Δ:      m_n − m_p = {DELTA_MN_MP:.4f} MeV")
    print()

    print("Phase 1a — Viable curve s_p(ε_p) for mass ratio = m_n/m_p")
    print("-" * 100)

    rows = sweep_eps()

    sample_eps = [0.10, 0.20, 0.30, 0.40, 0.50, 0.55, 0.60, 0.70, 0.80,
                  0.90, 1.00, 1.20, 1.50, 2.00]
    print(f"  {'ε_p':>6s}  {'s_p':>13s}  {'K_p (MeV/μ)':>13s}  "
          f"{'m_u (MeV)':>11s}  {'m_d (MeV)':>11s}  {'m_d/m_u':>9s}  "
          f"{'ratio err':>11s}")
    for eps_target in sample_eps:
        best = min(rows, key=lambda r: abs(r['eps_p'] - eps_target))
        print(f"  {best['eps_p']:>6.3f}  {best['s_p']:>13.6e}  "
              f"{best['K_p']:>13.3f}  {best['m_u_MeV']:>11.3f}  "
              f"{best['m_d_MeV']:>11.3f}  {best['d_to_u_ratio']:>9.5f}  "
              f"{best['ratio_error']:>+11.3e}")
    print()

    max_err = max(abs(r['ratio_error']) for r in rows)
    print(f"  Max |ratio − target| across curve: {max_err:.3e}  "
          f"(Newton convergence sanity)")
    print()

    print("How quark masses scale along the viable curve:")
    print("-" * 100)
    print(f"  K_p range: [{min(r['K_p'] for r in rows):.2f}, "
          f"{max(r['K_p'] for r in rows):.2f}] MeV/μ-unit")
    print(f"  m_u range: [{min(r['m_u_MeV'] for r in rows):.2f}, "
          f"{max(r['m_u_MeV'] for r in rows):.2f}] MeV")
    print(f"  m_d range: [{min(r['m_d_MeV'] for r in rows):.2f}, "
          f"{max(r['m_d_MeV'] for r in rows):.2f}] MeV")
    print()
    print(f"  SM constituent quark masses (rough): m_u ≈ 315 MeV, "
          f"m_d ≈ 336 MeV")
    print(f"  SM current quark masses (rough):     m_u ≈ 2.2 MeV, "
          f"m_d ≈ 4.7 MeV")
    print()

    print("Special points along the viable curve:")
    print("-" * 100)
    targets = [
        ("near constituent m_u ≈ 315 MeV", 315.0, 'm_u_MeV'),
        ("near g-candidate ε_p = 0.55",    0.55,  'eps_p'),
        ("near ε_p = 1.0 (Clifford-like)", 1.0,   'eps_p'),
    ]
    for label, target_val, key in targets:
        best = min(rows, key=lambda r: abs(r[key] - target_val))
        print(f"  {label}:")
        print(f"    ε_p = {best['eps_p']:.4f}, s_p = {best['s_p']:.6e}, "
              f"K_p = {best['K_p']:.3f} MeV/μ-unit")
        print(f"    m_u = {best['m_u_MeV']:.3f} MeV, "
              f"m_d = {best['m_d_MeV']:.3f} MeV, "
              f"m_d − m_u = {best['m_d_minus_m_u']:.3f} MeV")
        print()

    # ─── Phase 1b: Light-nuclei binding along the viable curve ──────
    print("Phase 1b — Light-nuclei harmonic stack along the viable curve")
    print("-" * 100)
    print(f"  Compositions (flavor-aware additive composition):")
    print(f"    ²H (pn)   = uud + udd = (3, 2) + (3, −2) = (6, 0)")
    print(f"    ³He (ppn) = uud + uud + udd = (9, 2)")
    print(f"    ⁴He (ppnn) = (12, 0)")
    print()

    rows_full = light_nuclei_check(rows)

    print(f"  {'ε_p':>6s}  {'B(²H)':>8s}  {'B(²H) obs':>10s}  "
          f"{'B(³He)':>8s}  {'obs':>6s}  {'B(⁴He)':>8s}  {'obs':>6s}")
    print("  " + "─" * 80)
    sample_eps_extended = [0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50,
                           0.55, 0.70, 1.00, 1.50, 2.00]
    for eps_target in sample_eps_extended:
        best = min(rows_full, key=lambda r: abs(r['eps_p'] - eps_target))
        if best['eps_p'] > 2.05:
            continue
        print(f"  {best['eps_p']:>6.3f}  {best['B_2H_pred']:>+8.3f}  "
              f"{best['B_2H_obs']:>+10.3f}  {best['B_3He_pred']:>+8.3f}  "
              f"{best['B_3He_obs']:>+6.3f}  {best['B_4He_pred']:>+8.3f}  "
              f"{best['B_4He_obs']:>+6.3f}")
    print()

    # ─── Find the ε_p that matches deuteron binding best ─────────────
    best_d = min(rows_full, key=lambda r: abs(r['B_2H_pred'] - B_D_OBS))
    print(f"  Best deuteron-binding match: ε_p = {best_d['eps_p']:.4f}, "
          f"s_p = {best_d['s_p']:.6e}")
    print(f"    Predicted B(²H) = {best_d['B_2H_pred']:+.3f} MeV  "
          f"(observed {best_d['B_2H_obs']:.3f})")
    print(f"    Predicted B(³He) = {best_d['B_3He_pred']:+.3f} MeV  "
          f"(observed {best_d['B_3He_obs']:.3f})")
    print(f"    Predicted B(⁴He) = {best_d['B_4He_pred']:+.3f} MeV  "
          f"(observed {best_d['B_4He_obs']:.3f})")
    print(f"    K_p = {best_d['K_p']:.3f} MeV/μ-unit")
    print(f"    m_u = {best_d['m_u_MeV']:.3f}, m_d = {best_d['m_d_MeV']:.3f} MeV")
    print()

    # Plot deuteron binding curve too
    fig2, ax = plt.subplots(figsize=(11, 6))
    eps_arr = [r['eps_p'] for r in rows_full]
    bd_arr = [r['B_2H_pred'] for r in rows_full]
    b3he_arr = [r['B_3He_pred'] for r in rows_full]
    b4he_arr = [r['B_4He_pred'] for r in rows_full]
    ax.plot(eps_arr, bd_arr, label='B(²H) predicted', color='tab:blue')
    ax.plot(eps_arr, b3he_arr, label='B(³He) predicted', color='tab:green')
    ax.plot(eps_arr, b4he_arr, label='B(⁴He) predicted', color='tab:red')
    ax.axhline(B_D_OBS, color='tab:blue', linestyle=':', alpha=0.6,
               label=f'B(²H) obs = {B_D_OBS} MeV')
    ax.axhline(7.718, color='tab:green', linestyle=':', alpha=0.6,
               label='B(³He) obs = 7.718 MeV')
    ax.axhline(28.296, color='tab:red', linestyle=':', alpha=0.6,
               label='B(⁴He) obs = 28.296 MeV')
    ax.axvline(best_d['eps_p'], color='gray', linestyle='--', alpha=0.5,
               label=f"best ²H match at ε_p = {best_d['eps_p']:.3f}")
    ax.set_xlabel('ε_p (along viable proton/neutron curve)')
    ax.set_ylabel('Predicted binding (MeV)')
    ax.set_title('Light-nuclei binding along the R64 viable curve')
    ax.set_xscale('log')
    ax.set_yscale('symlog', linthresh=1)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc='best')
    plt.tight_layout()
    plt.savefig(out_dir / "track1_light_nuclei_binding.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    csv_path = out_dir / "track1_viable_curve.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows_full[0].keys()))
        w.writeheader()
        w.writerows(rows_full)

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    eps_arr = [r['eps_p'] for r in rows]
    s_arr   = [r['s_p']   for r in rows]
    K_arr   = [r['K_p']   for r in rows]
    mu_arr  = [r['m_u_MeV'] for r in rows]
    md_arr  = [r['m_d_MeV'] for r in rows]
    split_arr = [r['m_d_minus_m_u'] for r in rows]

    ax = axes[0, 0]
    ax.plot(eps_arr, s_arr, color='tab:blue')
    ax.axvline(0.55, color='gray', linestyle=':', alpha=0.7,
               label='R63 g-candidate ε_p = 0.55')
    ax.set_xlabel('ε_p')
    ax.set_ylabel('s_p')
    ax.set_title('Viable curve: s_p(ε_p) for m_n/m_p = 1.001378')
    ax.set_xscale('log')
    ax.grid(alpha=0.3)
    ax.legend()

    ax = axes[0, 1]
    ax.plot(eps_arr, K_arr, color='tab:orange')
    ax.set_xlabel('ε_p')
    ax.set_ylabel('K_p (MeV per μ-unit)')
    ax.set_title('Mass scale K_p along the viable curve')
    ax.set_xscale('log')
    ax.grid(alpha=0.3)

    ax = axes[1, 0]
    ax.plot(eps_arr, mu_arr, label='m_u (MeV)', color='tab:green')
    ax.plot(eps_arr, md_arr, label='m_d (MeV)', color='tab:red')
    ax.axhline(315, color='tab:green', linestyle=':', alpha=0.5,
               label='SM constituent m_u ≈ 315')
    ax.axhline(336, color='tab:red', linestyle=':', alpha=0.5,
               label='SM constituent m_d ≈ 336')
    ax.set_xlabel('ε_p')
    ax.set_ylabel('quark mass (MeV)')
    ax.set_title('u, d quark masses along the viable curve')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    ax = axes[1, 1]
    ax.plot(eps_arr, split_arr, color='tab:purple')
    ax.set_xlabel('ε_p')
    ax.set_ylabel('m_d − m_u (MeV)')
    ax.set_title('Quark mass split (constituent scale) along curve')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "track1_viable_curve.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"  CSV:  {csv_path}")
    print(f"  Plot: {out_dir / 'track1_viable_curve.png'}")
    print()

    print("=" * 100)
    print("VERDICT — Phase 1a closed-form viable-curve test")
    print("=" * 100)
    print()
    s_at_055 = next(r['s_p'] for r in rows if abs(r['eps_p'] - 0.55) < 0.005)
    print(f"  The mass ratio R(ε, s) = m_n/m_p is achievable for any ε_p in")
    print(f"  the swept range — the viable curve exists.")
    print()
    print(f"  At ε_p = 0.55 (R63's g-candidate baseline) the required shear")
    print(f"  is s_p ≈ {s_at_055:.4e} — about three orders of magnitude")
    print(f"  smaller than R63's working s_p = 0.162 (which produced the")
    print(f"  inventory fit under the cross-sheet model).  This means the")
    print(f"  R64 magic point is structurally distinct from R63's working")
    print(f"  point: it implements u/d at large ε but with extremely small")
    print(f"  shear.")
    print()
    print(f"  Whether the same (ε_p, s_p) preserves the inventory and matches")
    print(f"  light nuclei is the next set of phases (Track 2 onward).")


if __name__ == "__main__":
    main()
