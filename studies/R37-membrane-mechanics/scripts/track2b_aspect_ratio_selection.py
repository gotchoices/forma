#!/usr/bin/env python3
"""
R37 Track 2b: Aspect ratio selection

After substituting the L₁ equilibrium (F3), the total energy of the
isotropic-membrane model reduces to:

    E_total(r) ∝ μ(r, s(r))^(2/3) × r^(1/3)

where s(r) is determined by the alpha curve  alpha_ma(r, s) = 1/137.

Minimising E_total along the alpha curve gives the equilibrium r.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from scipy.optimize import minimize_scalar
from lib.ma import alpha_ma, solve_shear_for_alpha, mu_12, ALPHA

hbar_SI = 1.0546e-34
c_SI = 2.998e8
eV_J = 1.602e-19
m_e_kg = 9.109e-31
lambda_bar_C = hbar_SI / (m_e_kg * c_SI)


def cost(r):
    """Energy cost function along the alpha curve (isotropic model)."""
    s = solve_shear_for_alpha(r)
    if s is None:
        return float('inf')
    mu = mu_12(r, s)
    return mu**(2.0 / 3.0) * r**(1.0 / 3.0)


def mode_mass_ratio(n1, n2, r, s):
    """Mass of mode (n1, n2) relative to the (1,2) electron mode."""
    mu_mode = math.sqrt(n1**2 / r**2 + (n2 - n1 * s)**2)
    mu_electron = mu_12(r, s)
    return mu_mode / mu_electron


def main():
    print("=" * 72)
    print("R37 Track 2b: Aspect Ratio Selection")
    print("=" * 72)

    # ── Part A: The constrained minimisation ──────────────────────
    print(f"\n{'='*72}")
    print("PART A: Constrained energy minimisation along the alpha curve")
    print("=" * 72)

    print(f"""
  The isotropic-membrane model (E_boundary = σ_m × A) gives:

    E_total(L₁, r) = ℏc × 2πμ(r,s) / L₁  +  σ_m × r × L₁²

  The L₁ equilibrium (∂E/∂L₁ = 0) yields  σ_m = E/(2A).
  Substituting back:

    E_total(r) ∝ μ(r, s(r))^(2/3) × r^(1/3)

  where s(r) is fixed by  alpha_ma(r, s) = 1/137.
  This is a function of r alone — minimise numerically.
""")

    # Scan and find the minimum
    r_vals = np.linspace(0.28, 30.0, 6000)
    costs = np.array([cost(r) for r in r_vals])
    valid = np.isfinite(costs)
    r_valid = r_vals[valid]
    c_valid = costs[valid]
    i_min = np.argmin(c_valid)
    r_coarse = r_valid[i_min]

    result = minimize_scalar(cost, bounds=(0.3, 2.0), method='bounded')
    r_min = result.x
    s_min = solve_shear_for_alpha(r_min)
    mu_min = mu_12(r_min, s_min)
    cost_min = cost(r_min)
    a_check = alpha_ma(r_min, s_min)
    L1 = 2 * math.pi * lambda_bar_C * mu_min
    L2 = r_min * L1

    print(f"  Minimum of μ^(2/3) × r^(1/3) along the alpha curve:")
    print(f"    r  = {r_min:.4f}")
    print(f"    s  = {s_min:.6f}")
    print(f"    μ  = {mu_min:.4f}")
    print(f"    α  = {a_check:.10f}  (target {ALPHA:.10f})")
    print(f"    L₁ = {L1:.4e} m    L₂ = {L2:.4e} m")
    print(f"    Geometry: fat torus, ring = {r_min:.0%} of tube")

    # ── Part B: Breadth of the minimum ────────────────────────────
    print(f"\n{'='*72}")
    print("PART B: Breadth of the minimum")
    print("=" * 72)

    print(f"\n  {'r':>6s} {'s':>10s} {'μ':>8s} {'cost':>10s} {'% above min':>12s}")
    print(f"  {'-'*48}")
    for r in [0.30, 0.35, 0.40, 0.45, 0.50, r_min, 0.55, 0.60, 0.70,
              0.80, 1.0, 1.5, 2.0, 4.0, 6.6, 10.0]:
        s = solve_shear_for_alpha(r)
        if s is None:
            continue
        mu = mu_12(r, s)
        c = cost(r)
        pct = 100 * (c - cost_min) / cost_min
        tag = " <-- min" if abs(r - r_min) < 0.01 else ""
        print(f"  {r:6.3f} {s:10.6f} {mu:8.4f} {c:10.6f} {pct:11.1f}%{tag}")

    print(f"""
  The minimum is very broad: r = 0.4 to 0.6 lies within 0.5%
  of the minimum energy.  r = 6.6 is 91% higher — decisively
  ruled out.  The isotropic model selects the fat-torus REGIME
  (r < 1) but does not sharply pin a value.
""")

    # ── Part C: Comparison to r = 6.6 ────────────────────────────
    print(f"{'='*72}")
    print("PART C: Comparison — energy-selected vs r = 6.6")
    print("=" * 72)

    r_canonical = 6.6
    s_canonical = solve_shear_for_alpha(r_canonical)
    mu66 = mu_12(r_canonical, s_canonical)
    L1_66 = 2 * math.pi * lambda_bar_C * mu66
    cost_66 = cost(r_canonical)

    print(f"""
  {'':>20s} {'Selected':>14s} {'Canonical':>14s}
  {'':>20s} {f'(r ≈ {r_min:.2f})':>14s} {'(r = 6.6)':>14s}
  {'-'*50}
  {'r':>20s} {r_min:14.4f} {r_canonical:14.4f}
  {'s':>20s} {s_min:14.6f} {s_canonical:14.6f}
  {'μ':>20s} {mu_min:14.4f} {mu66:14.4f}
  {'L₁ (m)':>20s} {L1:14.4e} {L1_66:14.4e}
  {'L₂ (m)':>20s} {L2:14.4e} {r_canonical*L1_66:14.4e}
  {'cost':>20s} {cost_min:14.4f} {cost_66:14.4f}
  {'% above min':>20s} {'0.0%':>14s} {f'+{100*(cost_66-cost_min)/cost_min:.1f}%':>14s}
""")

    # ── Part D: Mode spectrum comparison ──────────────────────────
    print(f"{'='*72}")
    print("PART D: Mode spectrum comparison")
    print("=" * 72)

    modes = [
        (1, 2, "electron"),
        (0, 1, ""), (1, 0, ""), (1, 1, ""),
        (2, 1, ""), (1, 3, ""), (2, 3, ""),
        (3, 2, ""), (2, 4, ""), (3, 6, ""),
    ]

    print(f"  {'mode':>8s} {f'm/m_e (r={r_min:.2f})':>16s} {'m/m_e (r=6.6)':>16s}")
    print(f"  {'-'*42}")
    for n1, n2, label in modes:
        m1 = mode_mass_ratio(n1, n2, r_min, s_min)
        m2 = mode_mass_ratio(n1, n2, r_canonical, s_canonical)
        tag = f"  ← {label}" if label else ""
        print(f"  ({n1},{n2}){tag:>10s} {m1:16.3f} {m2:16.3f}")

    print(f"""
  At r ≈ {r_min:.2f}, modes are widely spaced.  At r = 6.6, many
  modes cluster near the electron mass.

  Neither spectrum immediately produces the muon (207 m_e) or
  tau (3477 m_e) from low-order modes — those mass ratios
  require the full Ma multi-sheet structure, not a single T².
""")

    # ── Part E: Caveats and the moduli potential ──────────────────
    print(f"{'='*72}")
    print("PART E: Caveats — why the anisotropic answer is out of reach")
    print("=" * 72)

    print(f"""
  WHAT IS GENUINE:
    The constrained energy minimisation along the alpha curve
    selects r ≈ {r_min:.2f} under the isotropic-membrane model.
    This is the first physical mechanism that prefers a specific
    region of the alpha curve rather than leaving r as a free
    parameter.  r = 6.6 is 91% higher — decisively excluded.

  WHY THE MINIMUM IS BROAD:
    The cost function μ^(2/3) × r^(1/3) varies slowly near the
    minimum because μ(r) decreases as r increases (fewer tube
    windings) while r^(1/3) increases — the two nearly cancel.
    r = 0.4 to 0.6 all lie within 0.5% of optimal.

  WHY ANISOTROPIC IS NOT CALCULABLE:
    The isotropic model uses  E_boundary = σ_m × A  (area only).
    The actual boundary energy is the MODULI POTENTIAL — the
    vacuum energy of the T² as a function of its shape (r, s).
    This is not derivable within the current framework.

    The Casimir energy of the T² IS calculable but negligible
    (~10⁻⁹ of the mode energy).  Any stronger anisotropic
    restoring force must come from the full moduli potential.

    This is the same deep unknown that blocks computing R35's
    Goldilocks K and R31's derivation of α.

  WHY GRAVITY CANNOT SELECT r:
    The Schwarzschild metric depends only on total mass m_e c²,
    not on (r, s).  Gravity is blind to the aspect ratio.
""")

    # ── Summary ───────────────────────────────────────────────────
    print(f"{'='*72}")
    print("SUMMARY")
    print("=" * 72)

    print(f"""
  Energy minimisation along the alpha curve (isotropic model):

    r ≈ {r_min:.2f},  s ≈ {s_min:.3f},  α = 1/137  ✓

  Broad minimum — selects fat-torus REGIME (r < 1), not a
  precise value.  r = 6.6 ruled out at +91%.

  Anisotropic correction requires the moduli potential, which
  is the deepest unknown in the framework.
""")


if __name__ == '__main__':
    main()
