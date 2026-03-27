#!/usr/bin/env python3
"""
R37 Track 2b: Aspect ratio selection

The alpha curve alpha_kk(r, s) = 1/137 is one constraint in the
(r, s) plane — a continuous curve with solutions for all r > 0.26.

The isotropic membrane equilibrium (∂E/∂r = 0 with isotropic σ_m)
adds a second constraint: r = 1/(2−s).

Their intersection is the unique (r, s) where BOTH the charge
coupling and the energy balance are simultaneously satisfied.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
from scipy.optimize import brentq
from lib.t6 import alpha_kk, solve_shear_for_alpha, ALPHA

hbar_SI = 1.0546e-34
c_SI = 2.998e8
eV_J = 1.602e-19
m_e_kg = 9.109e-31
lambda_bar_C = hbar_SI / (m_e_kg * c_SI)


def membrane_eq_r(s):
    """Isotropic membrane equilibrium: r = 1/(2-s)."""
    return 1.0 / (2.0 - s)


def residual(s):
    """alpha_kk at the membrane-equilibrium r, minus target."""
    r = membrane_eq_r(s)
    return alpha_kk(r, s) - ALPHA


def mode_mass_ratio(n1, n2, r, s):
    """Mass of mode (n1, n2) relative to the (1,2) electron mode."""
    mu_mode = math.sqrt(n1**2 / r**2 + (n2 - n1 * s)**2)
    mu_electron = math.sqrt(1.0 / r**2 + (2.0 - s)**2)
    return mu_mode / mu_electron


def main():
    print("=" * 72)
    print("R37 Track 2b: Aspect Ratio Selection")
    print("=" * 72)

    # ── Part A: The two constraints ───────────────────────────────
    print(f"\n{'='*72}")
    print("PART A: Two independent constraints on (r, s)")
    print("=" * 72)

    print(f"""
  Constraint 1 — ALPHA CURVE (from R19 charge integral):
    alpha_kk(r, s) = {ALPHA:.10f}
    One equation in two unknowns → a curve in (r, s) space.
    Solutions exist for all r > ~0.26.

  Constraint 2 — MEMBRANE EQUILIBRIUM (R37 Track 2, isotropic σ_m):
    ∂E_total/∂r = 0  at fixed L₁
    → μ² = 2/r²
    → (2−s)² = 1/r²
    → r = 1/(2−s)
    One equation in two unknowns → another curve.

  Together: two equations, two unknowns → discrete solutions.
""")

    # ── Part B: Find intersections ────────────────────────────────
    print(f"{'='*72}")
    print("PART B: Intersections (self-consistent solutions)")
    print("=" * 72)

    # Scan for sign changes in the residual
    solutions = []
    N = 4000
    s_prev = 0.001
    r_prev = residual(s_prev)
    for i in range(2, N):
        s_val = i * 0.499 / N
        r_val = residual(s_val)
        if r_prev * r_val < 0:
            s_sol = brentq(residual, s_prev, s_val)
            r_sol = membrane_eq_r(s_sol)
            solutions.append((r_sol, s_sol))
        s_prev = s_val
        r_prev = r_val

    for idx, (r_sol, s_sol) in enumerate(solutions):
        a_check = alpha_kk(r_sol, s_sol)
        mu = math.sqrt(1 / r_sol**2 + (2 - s_sol)**2)
        L1 = 2 * math.pi * lambda_bar_C * mu
        L2 = r_sol * L1
        A = L1 * L2

        print(f"""
  Solution {idx + 1}:
    r = {r_sol:.6f}    s = {s_sol:.6f}
    alpha_kk = {a_check:.10f}  (target {ALPHA:.10f})
    μ = {mu:.4f}
    L₁ = {L1:.4e} m    L₂ = {L2:.4e} m
    A  = {A:.4e} m²
    Geometry: ring = {r_sol:.0%} of tube  ({'fat torus' if r_sol < 1 else 'thin torus'})
""")

    # ── Part C: Compare to canonical r = 6.6 ─────────────────────
    print(f"{'='*72}")
    print("PART C: Comparison — membrane-selected vs r = 6.6")
    print("=" * 72)

    r_canonical = 6.6
    s_canonical = solve_shear_for_alpha(r_canonical)

    if solutions:
        r1, s1 = solutions[0]
        mu1 = math.sqrt(1 / r1**2 + (2 - s1)**2)
        mu66 = math.sqrt(1 / r_canonical**2 + (2 - s_canonical)**2)
        L1_1 = 2 * math.pi * lambda_bar_C * mu1
        L1_66 = 2 * math.pi * lambda_bar_C * mu66

        print(f"""
  {'':>20s} {'Membrane':>14s} {'Canonical':>14s}
  {'':>20s} {'(r ≈ 0.53)':>14s} {'(r = 6.6)':>14s}
  {'-'*50}
  {'r':>20s} {r1:14.4f} {r_canonical:14.4f}
  {'s':>20s} {s1:14.6f} {s_canonical:14.6f}
  {'μ':>20s} {mu1:14.4f} {mu66:14.4f}
  {'L₁ (m)':>20s} {L1_1:14.4e} {L1_66:14.4e}
  {'L₂ (m)':>20s} {r1*L1_1:14.4e} {r_canonical*L1_66:14.4e}
  {'A (m²)':>20s} {r1*L1_1**2:14.4e} {r_canonical*L1_66**2:14.4e}

  The membrane-selected torus is a fat near-sphere
  (tube 2× wider than ring).  The canonical 6.6 is a
  thin bicycle tire.  Both give alpha = 1/137.

  The membrane equilibrium r = 6.6 would require
  r_membrane = 1/(2-{s_canonical:.4f}) = {1/(2-s_canonical):.4f},
  which is far from 6.6.  So r = 6.6 is NOT at the
  isotropic membrane equilibrium — it requires anisotropic
  physics or external constraint.
""")

    # ── Part D: Mode spectrum at the selected r ───────────────────
    print(f"{'='*72}")
    print("PART D: Mode spectrum comparison")
    print("=" * 72)

    if solutions:
        r1, s1 = solutions[0]
        modes = [
            (1, 2, "electron"),
            (0, 1, ""), (1, 0, ""), (1, 1, ""),
            (2, 1, ""), (1, 3, ""), (2, 3, ""),
            (3, 2, ""), (2, 4, ""), (3, 6, ""),
        ]

        header = f"  {'mode':>8s} {'m/m_e (r=0.53)':>16s} {'m/m_e (r=6.6)':>16s}"
        print(header)
        print(f"  {'-'*42}")
        for n1, n2, label in modes:
            m1 = mode_mass_ratio(n1, n2, r1, s1)
            m2 = mode_mass_ratio(n1, n2, r_canonical, s_canonical)
            tag = f"  ← {label}" if label else ""
            print(f"  ({n1},{n2}){tag:>10s} {m1:16.3f} {m2:16.3f}")

        print(f"""
  At r ≈ 0.53, modes are widely spaced.  At r = 6.6, many
  modes cluster near the electron mass.

  Neither spectrum immediately produces the muon (207 m_e) or
  tau (3477 m_e) from low-order modes — those mass ratios
  require the full T⁶ multi-sheet structure, not a single T².
""")

    # ── Part E: Caveats and significance ──────────────────────────
    print(f"{'='*72}")
    print("PART E: Caveats and significance")
    print("=" * 72)

    print(f"""
  WHAT IS GENUINE:
    The intersection of two independent constraints — the alpha
    charge integral (R19) and the membrane energy minimisation
    (R37 Track 2) — selects a unique point on the alpha curve.
    This is the first physical mechanism that picks a specific
    electron aspect ratio rather than leaving it as a free
    parameter.

  WHAT IS LIMITED:
    The membrane constraint used ISOTROPIC surface tension.
    The actual stress is 83% anisotropic (Track 1 F1).  With
    anisotropy included, the equilibrium r would shift — how
    much depends on the anisotropic elastic model, which is
    not yet computed.

    So r = {solutions[0][0]:.3f} is the isotropic-limit prediction,
    not the final answer.  It establishes the REGIME (fat torus,
    r < 1) but not the precise value.

  WHY GRAVITY CANNOT SELECT r:
    The Schwarzschild metric depends only on total mass m_e c²,
    not on (r, s).  A fat torus and a thin torus with the same
    mass produce identical gravitational fields.  Gravity is
    blind to the aspect ratio.
""")

    # ── Summary ───────────────────────────────────────────────────
    print(f"{'='*72}")
    print("SUMMARY")
    print("=" * 72)

    if solutions:
        r1, s1 = solutions[0]
        print(f"""
  The alpha curve (charge) and the isotropic membrane equilibrium
  (energy balance) intersect at:

    r = {r1:.4f},  s = {s1:.4f},  α = 1/137  ✓

  This is the first physical selection of a specific electron
  aspect ratio.  It selects the FAT TORUS regime (r < 1),
  far from the historical r = 6.6 assumption.

  Caveat: isotropic limit only.  Anisotropic correction needed.
""")
        if len(solutions) > 1:
            r2, s2 = solutions[1]
            print(f"  Mirror solution: r = {r2:.4f}, s = {s2:.4f} (large-shear branch).")
            print()


if __name__ == '__main__':
    main()
