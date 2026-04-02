#!/usr/bin/env python3
"""
R46 Track 1: Baseline EM fields on an unslotted torus.
Vector model with circular polarization.

For a circularly polarized (n₁=1) mode on the torus, the E-field
rotation matches the surface-normal rotation.  The result:

    E_n(θ₁, θ₂) = E₀ cos(q_eff θ₂)      (normal to surface)
    E_t(θ₁, θ₂) = E₀ sin(q_eff θ₂)      (tangent, ⊥ geodesic)
    B_t(θ₁, θ₂) = (E₀/c) sin(q_eff θ₂)  (tangent, along geodesic)

No θ₁ dependence — the tube angle cancels exactly for n₁=1.
This is the WvM mechanism expressed as a field on the full surface.

The CP model gives a different α formula than R19's scalar model.
This track derives the new formula, solves for shear, and compares.

Outputs (in ../outputs/):
  track1_data.npz               field arrays for Track 2
  track1_En_map_electron.svg    E_normal on unrolled sheet
  track1_En_map_ghost.svg       E_normal for (1,1) ghost
  track1_charge_profile.svg     charge density vs θ₂
  track1_alpha_comparison.svg   CP vs scalar α formulas

Conventions:
  r = a/R (tube/ring, matches R19)
  s = fractional shear
  q_eff = n₂ − s
"""

import os
import sys
import math
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from torus_model import (
    make_grid, rho_factor, geometry_kk,
    e_normal, e_tangential,
    field_amplitude_cp, charge_integral_analytic, charge_numerical,
    alpha_cp_kk, alpha_scalar_kk, solve_shear,
    ghost_mass_ratio_kk,
    EPS0, E_CHARGE, ALPHA, M_E, C, LAMBDABAR_C,
)
from plot_utils import (
    plot_field_with_geodesic, plot_dual_profiles, plot_dual_lines,
)

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs')
os.makedirs(OUT_DIR, exist_ok=True)


def main():
    print("=" * 72)
    print("R46 Track 1: Baseline EM Fields — Vector / Circular Polarization")
    print("=" * 72)
    print()

    N1, N2 = 256, 512
    T1, T2, theta1, theta2 = make_grid(N1, N2)
    r_values = [1.0, 2.0, 4.0, 8.0]

    # ── Section 1: New α formula ─────────────────────────────────
    print("SECTION 1: CP vector α formula vs R19 scalar")
    print()
    print("  Scalar (R19):  α = r² μ sin²(2πs) / (4πq²)")
    print("  CP vector:     α = μ sin²(2πs) / (4πq²)")
    print("  where μ = √(1/r² + q²),  q = 2−s")
    print()
    print("  Ratio:  α_CP / α_scalar = 1/r²")
    print("  At r=1 they agree.  At larger r, CP needs more shear.")
    print()

    header = (f"{'r':>6s} | {'s_scalar':>10s} | {'s_CP':>10s} | "
              f"{'ratio':>8s} | {'q_eff_CP':>10s}")
    print(header)
    print("-" * len(header))

    shear_data = {}
    for r in r_values:
        s_scalar = solve_shear(r, alpha_scalar_kk)
        s_cp = solve_shear(r, alpha_cp_kk)

        if s_scalar is None or s_cp is None:
            print(f"{r:6.2f} | no solution")
            continue

        ratio = s_cp / s_scalar
        q_cp = 2.0 - s_cp
        shear_data[r] = {'s_scalar': s_scalar, 's_cp': s_cp, 'q_eff': q_cp}

        print(f"{r:6.2f} | {s_scalar:10.6f} | {s_cp:10.6f} | "
              f"{ratio:8.4f} | {q_cp:10.6f}")

    print()

    # ── Section 2: Charge verification ───────────────────────────
    print("SECTION 2: Charge verification (CP model, KK convention)")
    print()

    header = (f"{'r':>6s} | {'s':>10s} | {'Q_analytic/e':>14s} | "
              f"{'Q_numerical/e':>14s} | {'error':>10s} | "
              f"{'R (m)':>12s} | {'a (m)':>12s}")
    print(header)
    print("-" * len(header))

    electron_data = {}
    for r in r_values:
        if r not in shear_data:
            continue
        s = shear_data[r]['s_cp']
        q_eff = shear_data[r]['q_eff']
        R, a = geometry_kk(r, s)
        E0 = field_amplitude_cp(r, R)

        Q_anal = charge_integral_analytic(E0, r, R, s)
        Q_num = charge_numerical(E0, T1, T2, r, R, q_eff, N1, N2)
        err = abs(Q_num / Q_anal - 1) if abs(Q_anal) > 1e-40 else float('inf')

        electron_data[r] = {
            's': s, 'q_eff': q_eff, 'R': R, 'a': a, 'E0': E0,
            'Q_anal': Q_anal, 'Q_num': Q_num,
        }

        print(f"{r:6.2f} | {s:10.6f} | {Q_anal/E_CHARGE:14.6f} | "
              f"{Q_num/E_CHARGE:14.6f} | {err:10.2e} | "
              f"{R:12.4e} | {a:12.4e}")

    print()

    # ── Section 3: E_n charge distribution ───────────────────────
    print("SECTION 3: Charge distribution (E_normal vs θ₂)")
    print()
    print("  E_n = E₀ cos(q_eff θ₂)  — NO θ₁ dependence")
    print("  Charge density σ = ε₀ E_n = ε₀ E₀ cos(q_eff θ₂)")
    print("  Uniform around tube cross-section at each ring position")
    print()

    for r, data in electron_data.items():
        q = data['q_eff']
        zeros_per_revolution = 2 * q
        print(f"  r = {r:.0f}: q_eff = {q:.6f}, "
              f"~{zeros_per_revolution:.1f} zero crossings per ring lap")
    print()

    # ── Section 4: Ghost mode comparison ─────────────────────────
    print("=" * 72)
    print("SECTION 4: Ghost (1,1) mode")
    print()

    header = (f"{'r':>6s} | {'q_eff_g':>8s} | {'Q_ghost/e':>10s} | "
              f"{'Q_g/Q_e':>10s} | {'m_g/m_e':>10s}")
    print(header)
    print("-" * len(header))

    ghost_data = {}
    for r in r_values:
        if r not in electron_data:
            continue
        s = electron_data[r]['s']
        R = electron_data[r]['R']
        q_eff_g = 1.0 - s
        m_ratio = ghost_mass_ratio_kk(r, s)

        E0_ghost = electron_data[r]['E0'] * math.sqrt(m_ratio)
        Q_ghost = charge_integral_analytic(E0_ghost, r, R, s, n2=1)
        Q_electron = electron_data[r]['Q_anal']

        ghost_data[r] = {
            'q_eff': q_eff_g, 'Q': Q_ghost, 'm_ratio': m_ratio,
            'E0': E0_ghost,
        }

        Q_ratio = Q_ghost / Q_electron if abs(Q_electron) > 1e-40 else float('nan')
        print(f"{r:6.2f} | {q_eff_g:8.6f} | "
              f"{Q_ghost/E_CHARGE:10.6f} | "
              f"{Q_ratio:10.6f} | "
              f"{m_ratio:10.6f}")

    print()
    print("  Ghost has q_eff ≈ 1−s.  Electron has q_eff ≈ 2−s.")
    print("  Both depend only on θ₂ (no θ₁ variation).")
    print("  Discrimination for filtering comes from different θ₂ patterns:")
    print("  electron has ~2 oscillations/revolution, ghost has ~1.")
    print()

    # ── Section 5: B field and magnetic moment ───────────────────
    print("=" * 72)
    print("SECTION 5: B field and Poynting vector")
    print()
    print("  B is tangential to the surface: B_t = (E₀/c) sin(q_eff θ₂)")
    print("  B is 90° out of phase with E_n in the ring direction.")
    print("  The Poynting vector S = E × H points along the geodesic.")
    print()
    print("  For a standing wave: E and B are 90° out of phase in TIME,")
    print("  so the time-averaged Poynting vector vanishes.")
    print("  For a traveling wave: S ∝ E₀²/μ₀c (constant magnitude,")
    print("  pointing along the geodesic).")
    print()

    for r in r_values:
        if r not in electron_data:
            continue
        s = electron_data[r]['s']
        q = electron_data[r]['q_eff']

        En = np.cos(q * theta2)
        Bt = np.sin(q * theta2)

        En_sq_avg = np.mean(En**2)
        Bt_sq_avg = np.mean(Bt**2)

        print(f"  r = {r:.0f}: ⟨E_n²⟩/E₀² = {En_sq_avg:.6f},  "
              f"⟨B_t²⟩c²/E₀² = {Bt_sq_avg:.6f}  "
              f"(both ≈ 0.5 for q_eff ≈ integer)")
    print()

    # ── Section 6: Comparison summary ────────────────────────────
    print("=" * 72)
    print("SECTION 6: Scalar vs CP comparison")
    print()

    header = (f"{'r':>6s} | {'s_scalar':>10s} | {'s_CP':>10s} | "
              f"{'s_CP/s_scalar':>14s} | {'α_check':>10s}")
    print(header)
    print("-" * len(header))

    for r in r_values:
        if r not in shear_data:
            continue
        sd = shear_data[r]
        alpha_check = alpha_cp_kk(r, sd['s_cp'])
        print(f"{r:6.2f} | {sd['s_scalar']:10.6f} | {sd['s_cp']:10.6f} | "
              f"{sd['s_cp']/sd['s_scalar']:14.6f} | {alpha_check:10.8f}")

    print()
    print(f"  Target α = {ALPHA:.10f} = 1/{1/ALPHA:.3f}")
    print()

    # ── Generate SVG plots ───────────────────────────────────────
    print("=" * 72)
    print("Generating SVG plots...")
    print()

    r_plot = 2.0
    if r_plot in electron_data:
        edata = electron_data[r_plot]
        En_2d = edata['E0'] * np.cos(edata['q_eff'] * T2)
        plot_field_with_geodesic(
            En_2d,
            title=(f'Electron (1,2) — E_normal (r={r_plot}, '
                   f's={edata["s"]:.4f})\n'
                   f'Horizontal bands: E_n depends only on θ₂, not θ₁'),
            out_dir=OUT_DIR, filename='track1_En_map_electron.svg',
            n1=1, n2=2, s=edata['s'], r=r_plot,
            extra_geodesics=[
                dict(n1=1, n2=1,
                     color='#c04020', label='Ghost (1,1)', ls='-.'),
            ])

    if r_plot in ghost_data:
        gdata = ghost_data[r_plot]
        gEn = gdata['E0'] * np.cos(gdata['q_eff'] * T2)
        plot_field_with_geodesic(
            gEn,
            title=(f'Ghost (1,1) — E_normal (r={r_plot}, '
                   f'q_eff={gdata["q_eff"]:.4f})\n'
                   f'~1 oscillation/revolution vs ~2 for electron'),
            out_dir=OUT_DIR, filename='track1_En_map_ghost.svg',
            n1=1, n2=1,
            s=electron_data[r_plot]['s'] if r_plot in electron_data else 0,
            r=r_plot)

    # charge profiles
    e_profiles = {f'r={r:.0f}': np.cos(electron_data[r]['q_eff'] * theta2)
                  for r in sorted(electron_data)}
    g_profiles = {f'r={r:.0f}': np.cos(ghost_data[r]['q_eff'] * theta2)
                  for r in sorted(ghost_data)}
    plot_dual_profiles(
        np.degrees(theta2), e_profiles, g_profiles,
        title_left='Electron (1,2)', title_right='Ghost (1,1)',
        suptitle='Charge density profiles (proportional to cos(q_eff θ₂))',
        xlabel=r'$\theta_2$ (ring, degrees)',
        ylabel=r'$E_n / E_0$',
        out_dir=OUT_DIR, filename='track1_charge_profile.svg')

    # alpha / shear comparison
    rs = sorted(shear_data.keys())
    s_scalar = [shear_data[r]['s_scalar'] for r in rs]
    s_cp = [shear_data[r]['s_cp'] for r in rs]
    ratios = [s_cp[i] / s_scalar[i] for i in range(len(rs))]
    plot_dual_lines(
        xs=rs,
        ys_left={
            'Scalar (R19)': (rs, s_scalar, 'o-'),
            'CP vector':    (rs, s_cp,     's-'),
        },
        ys_right={
            'Ratio': (rs, ratios, 'D-'),
        },
        xlabel='r = a/R',
        ylabel_left='Shear s',
        ylabel_right='s_CP / s_scalar',
        title_left='Shear required for α = 1/137',
        title_right='Shear ratio (CP vs scalar)',
        out_dir=OUT_DIR, filename='track1_alpha_comparison.svg',
        hline_right=1.0)

    # ── Save data ────────────────────────────────────────────────
    print()
    print("Saving data for Track 2...")

    save_dict = {
        'theta1': theta1, 'theta2': theta2,
        'r_values': np.array(r_values),
        'convention': 'KK', 'field_model': 'CP_vector',
    }

    for r in r_values:
        if r in electron_data:
            e = electron_data[r]
            pfx = f'e_r{r:.0f}'
            save_dict[f'{pfx}_s'] = e['s']
            save_dict[f'{pfx}_q_eff'] = e['q_eff']
            save_dict[f'{pfx}_Q'] = e['Q_anal']
            save_dict[f'{pfx}_R'] = e['R']
            save_dict[f'{pfx}_a'] = e['a']
            save_dict[f'{pfx}_E0'] = e['E0']
            save_dict[f'{pfx}_En'] = e['E0'] * np.cos(e['q_eff'] * T2)
            save_dict[f'{pfx}_Et'] = e['E0'] * np.sin(e['q_eff'] * T2)

        if r in ghost_data:
            g = ghost_data[r]
            pfx = f'g_r{r:.0f}'
            save_dict[f'{pfx}_q_eff'] = g['q_eff']
            save_dict[f'{pfx}_Q'] = g['Q']
            save_dict[f'{pfx}_m_ratio'] = g['m_ratio']
            save_dict[f'{pfx}_En'] = g['E0'] * np.cos(g['q_eff'] * T2)

    npz_path = os.path.join(OUT_DIR, 'track1_data.npz')
    np.savez_compressed(npz_path, **save_dict)
    print(f"  Saved: {npz_path}")

    print()
    print("=" * 72)
    print("Track 1 complete.")
    print("=" * 72)




if __name__ == '__main__':
    main()
