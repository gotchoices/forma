#!/usr/bin/env python3
"""
R46 Track 2: Slot placement on the torus — table-driven analysis.

Compares multiple slot configurations ("plans") for ghost filtering
and magnetic-moment enhancement.  For each plan, prints field
diagnostics at every slot.  Generates combined 3-panel plots
(E heatmap + B heatmap + geodesic) with all plans overlaid.

Plan A — 4 slots at exact pressure minima (shear-corrected):
  θ₂ = 93.2° and 279.5° (where cos(q_eff θ₂) = −1).

Plan B — 3 slots at exact field maxima (shear-corrected):
  1 tall slot at θ₂ = 186.3° (second pressure peak), 2 at θ₂ = 0°.

Plan C — 4 slots at B-field maxima (pure moment, zero charge):
  θ₂ ≈ 46.6°, 139.7°, 232.9°, 326.1° where |sin(q θ₂)| = 1
  and cos(q θ₂) = 0.

Outputs (in ../outputs/):
  track2_all_electron.svg   3-panel with all plans, electron
  track2_all_ghost.svg      3-panel with all plans, ghost
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from torus_model import (
    make_grid, e_normal_unipolar, b_tangential,
    geometry_kk, field_amplitude_cp,
    alpha_cp_kk, solve_shear, ghost_mass_ratio_kk,
)
from plot_utils import plot_3panel_slots, PLAN_COLORS

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs')
os.makedirs(OUT_DIR, exist_ok=True)


# ── Slot plan definitions ───────────────────────────────────────

def geodesic_crossings(n1, n2, theta2_deg):
    """θ₁ values where the (n1,n2) geodesic crosses a given θ₂."""
    crossings = []
    for k in range(n2):
        t = (theta2_deg + k * 360.0) / (n2 * 360.0)
        t1 = (n1 * t * 360.0) % 360.0
        crossings.append(t1)
    return sorted(crossings)


def midpoint_between(angles_deg):
    """Midpoint of the largest gap between sorted angles on a circle."""
    n = len(angles_deg)
    if n == 0:
        return 180.0
    if n == 1:
        return (angles_deg[0] + 180.0) % 360.0
    gaps = []
    for i in range(n):
        a = angles_deg[i]
        b = angles_deg[(i + 1) % n]
        gap = (b - a) % 360.0
        mid = (a + gap / 2) % 360.0
        gaps.append((gap, mid))
    gaps.sort(key=lambda x: -x[0])
    return gaps[0][1]


def pressure_extrema(q_eff):
    """Return (minima, maxima) θ₂ lists in degrees.

    Maxima: cos(q θ₂) = +1 → q θ₂ = 2nπ
    Minima: cos(q θ₂) = −1 → q θ₂ = (2n+1)π
    """
    maxima, minima = [], []
    for n in range(10):
        t2 = n * 360.0 / q_eff
        if 0 <= t2 < 360:
            maxima.append(t2)
        t2 = (2 * n + 1) * 180.0 / q_eff
        if 0 <= t2 < 360:
            minima.append(t2)
    return minima, maxima


def b_maxima_theta2(q_eff, count=4):
    """θ₂ positions where |sin(q θ₂)| = 1 (B-field maxima)."""
    positions = []
    for n in range(count):
        t2 = (np.pi / 2 + n * np.pi) / q_eff
        if np.degrees(t2) <= 360:
            positions.append(np.degrees(t2))
    return positions


def build_plans(q_eff_e):
    """Return an ordered dict of slot plan definitions."""
    W = 2.0
    p_min, p_max = pressure_extrema(q_eff_e)

    plans = {}

    # Plan A — exact pressure minima (shear-corrected)
    plan_a_slots = []
    for t2 in p_min:
        mid = midpoint_between(geodesic_crossings(1, 2, t2))
        plan_a_slots.append(dict(theta2=t2, theta1=mid, width=W, height=50.0))
        plan_a_slots.append(dict(theta2=t2, theta1=(mid + 180) % 360,
                                 width=W, height=50.0))
    plans['A'] = dict(
        name='Plan A — 4 slots at pressure minima',
        desc=(f'Ghost filtering.  θ₂ = {p_min[0]:.1f}°, {p_min[1]:.1f}°'
              ' (exact minima, shear-corrected).'),
        slots=plan_a_slots)

    # Plan B — exact pressure maxima (shear-corrected)
    t2_peak2 = p_max[1] if len(p_max) > 1 else 180.0
    mid_peak = midpoint_between(geodesic_crossings(1, 2, t2_peak2))
    plans['B'] = dict(
        name='Plan B — 3 slots at field maxima',
        desc=(f'Moment enhancement.  1 tall slot at θ₂ = {t2_peak2:.1f}°'
              ' (exact 2nd peak);\n'
              '  2 half-height slots at θ₂ = 0° (B = 0, charge-only).'),
        slots=[
            dict(theta2=t2_peak2, theta1=mid_peak, width=W, height=100.0),
            dict(theta2=0.0,      theta1=90.0,     width=W, height=50.0),
            dict(theta2=0.0,      theta1=270.0,    width=W, height=50.0),
        ])

    # Plan C — B-field maxima (zero charge leakage)
    b_positions = b_maxima_theta2(q_eff_e)
    plan_c_slots = []
    for t2 in b_positions:
        mid = midpoint_between(geodesic_crossings(1, 2, t2))
        plan_c_slots.append(dict(theta2=t2, theta1=mid, width=W, height=50.0))
    plans['C'] = dict(
        name='Plan C — 4 slots at B-field maxima',
        desc=('Pure moment, zero charge.  cos(q θ₂) = 0 at these θ₂,\n'
              '  so ΔQ = 0 identically.  |B| is at its peak.'),
        slots=plan_c_slots)

    return plans


# ── Analysis ────────────────────────────────────────────────────

def analyse_plan(plan, q_eff_e, q_eff_g):
    """Print field diagnostics and scaling estimates for one plan."""
    slots = plan['slots']

    print(f"  {'#':>3}  {'θ₂':>7}  {'θ₁':>6}  {'w':>4} {'h':>5}"
          f"  {'P_e':>7} {'AC_e':>7} {'B_e/B₀':>7}"
          f"  {'P_g':>7} {'AC_g':>7} {'B_g/B₀':>7}"
          f"  {'P_g/P_e':>8}")

    for i, sl in enumerate(slots):
        t2r = np.radians(sl['theta2'])
        P_e  = 1 + np.cos(q_eff_e * t2r)
        AC_e = np.cos(q_eff_e * t2r)
        B_e  = np.sin(q_eff_e * t2r)
        P_g  = 1 + np.cos(q_eff_g * t2r)
        AC_g = np.cos(q_eff_g * t2r)
        B_g  = np.sin(q_eff_g * t2r)
        ratio_str = (f'{P_g / P_e:8.1f}' if abs(P_e) > 1e-6
                     else '     inf')
        print(f"  [{i+1:>1}]  {sl['theta2']:6.1f}°  {sl['theta1']:5.0f}°"
              f"  {sl['width']:3.0f}° {sl['height']:4.0f}°"
              f"  {P_e:7.4f} {AC_e:7.4f} {B_e:7.4f}"
              f"  {P_g:7.4f} {AC_g:7.4f} {B_g:7.4f}"
              f"  {ratio_str}")
    print()


# ── Main ────────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("R46 Track 2: Slot Placement — Table-Driven Analysis")
    print("=" * 72)
    print()

    N1, N2 = 256, 512
    T1, T2, theta1, theta2 = make_grid(N1, N2)
    r = 2.0

    s = solve_shear(r, alpha_cp_kk)
    q_eff_e = 2.0 - s
    q_eff_g = 1.0 - s
    R_phys, a_phys = geometry_kk(r, s)
    E0 = field_amplitude_cp(r, R_phys)
    m_ratio = ghost_mass_ratio_kk(r, s)
    E0_g = E0 * m_ratio

    print(f"  r = {r},  s = {s:.6f}")
    print(f"  q_eff (electron) = {q_eff_e:.6f}")
    print(f"  q_eff (ghost)    = {q_eff_g:.6f}")
    print(f"  R = {R_phys:.4e} m,  a = {a_phys:.4e} m")
    print()

    p_min, p_max = pressure_extrema(q_eff_e)
    print(f"  Pressure maxima at θ₂ = {', '.join(f'{x:.1f}°' for x in p_max)}")
    print(f"  Pressure minima at θ₂ = {', '.join(f'{x:.1f}°' for x in p_min)}")
    print()

    # Field arrays
    En_e = E0   * e_normal_unipolar(T2, q_eff_e)
    Bt_e = (E0 / 2.998e8) * b_tangential(T2, q_eff_e)
    En_g = E0_g * e_normal_unipolar(T2, q_eff_g)
    Bt_g = (E0_g / 2.998e8) * b_tangential(T2, q_eff_g)

    plans = build_plans(q_eff_e)

    # ── Per-plan analysis (console only, no individual plots) ──
    for key, plan in plans.items():
        print("-" * 72)
        print(f"  {plan['name']}")
        print(f"  {plan['desc']}")
        print("-" * 72)
        print()
        analyse_plan(plan, q_eff_e, q_eff_g)

    # ── Combined 3-panel plots (all plans) ──
    print("-" * 72)
    print("  Generating combined 3-panel plots")
    print("-" * 72)

    slot_groups = []
    for key, plan in plans.items():
        slot_groups.append(dict(
            label=f'Plan {key}',
            color=PLAN_COLORS.get(key, '#888888'),
            slots=plan['slots']))

    ghost_geo = [dict(n1=1, n2=1, color='#c04020',
                      label='Ghost (1,1)', ls='-.')]

    plot_3panel_slots(
        En_e, Bt_e,
        title='All plans — electron (1,2)',
        out_dir=OUT_DIR, filename='track2_all_electron.svg',
        n1=1, n2=2, s=s, r=r,
        slot_groups=slot_groups,
        extra_geodesics=ghost_geo)

    plot_3panel_slots(
        En_g, Bt_g,
        title='All plans — ghost (1,1)',
        out_dir=OUT_DIR, filename='track2_all_ghost.svg',
        n1=1, n2=1, s=s, r=r,
        slot_groups=slot_groups)

    print()
    print("=" * 72)
    print("  Slot colors: " + ", ".join(
        f'Plan {k}={PLAN_COLORS.get(k,"?")}' for k in plans))
    print("=" * 72)
    print("Track 2 complete.")


if __name__ == '__main__':
    main()
