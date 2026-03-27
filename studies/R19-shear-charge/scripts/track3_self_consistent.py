#!/usr/bin/env python3
"""
R19 Track 3 (partial): Self-consistent T² electron geometry.

Previous tracks used the s=0 Compton constraint to set (a, R),
then computed the charge at nonzero s.  But shear changes the
geodesic path length, so (a, R) must adjust.

Self-consistent Compton constraint:
    L(s) = 2π√(a²(1+2s)² + 4R²) = λ_C

This gives:
    R(r,s) = λ_C / (2π √(r²(1+2s)² + 4))
    a(r,s) = r × R(r,s)

The charge formula becomes:
    α = [r² / √(r²(1+2s)² + 4)] × sin²(2πs) / (4π(2−s)²)

This is a single equation in s (for given r), solved numerically.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C

import numpy as np
from scipy.optimize import brentq


def alpha_from_rs(r, s):
    """
    Self-consistent α formula including shear in the Compton constraint.

    α = r² sin²(2πs) / (4π (2−s)² √(r²(1+2s)² + 4))
    """
    denom = math.sqrt(r**2 * (1 + 2*s)**2 + 4)
    return r**2 * math.sin(2*math.pi*s)**2 / (4*math.pi * (2-s)**2 * denom)


def geometry_sc(r, s):
    """Self-consistent geometry: R and a adjusted for shear."""
    R = lambda_C / (2 * math.pi * math.sqrt(r**2 * (1+2*s)**2 + 4))
    a = r * R
    return R, a


def L_geodesic(r, s, R, a):
    """Geodesic path length on sheared T²."""
    L1 = 2 * math.pi * a
    L2 = 2 * math.pi * R
    return math.sqrt((L1 * (1+2*s))**2 + (2*L2)**2)


def solve_shear(r, alpha_target=alpha):
    """Solve for self-consistent s at given r."""
    def f(s):
        return alpha_from_rs(r, s) - alpha_target

    s_scan = np.linspace(0.001, 0.999, 5000)
    f_scan = [f(s) for s in s_scan]

    solutions = []
    for i in range(len(f_scan) - 1):
        if f_scan[i] * f_scan[i+1] < 0:
            s_sol = brentq(f, s_scan[i], s_scan[i+1], xtol=1e-14)
            solutions.append(s_sol)

    return solutions


def main():
    E_mc2 = m_e * c**2
    lambdabar_C = hbar / (m_e * c)
    g_r = 0.5

    print("=" * 72)
    print("R19 Track 3: Self-Consistent T² Electron Geometry")
    print("=" * 72)
    print()

    # ── Section 1: The self-consistent equation ───────────────
    print("SECTION 1: Self-consistent α formula")
    print("-" * 72)
    print()
    print("With shear included in the Compton constraint:")
    print()
    print("  α = r² sin²(2πs) / (4π (2−s)² √(r²(1+2s)² + 4))")
    print()
    print("Compare with Track 1 (s=0 geometry):")
    print()
    print("  α = r² sin²(2πs) / (4π (2−s)² √(r² + 4))")
    print()
    print("The only change: r²+4 → r²(1+2s)²+4 in the square root.")
    print("The denominator is larger for s > 0, so the required s")
    print("is slightly larger than in Track 1.")
    print()

    # ── Section 2: Solve for each aspect ratio ────────────────
    print("SECTION 2: Solutions across aspect ratios")
    print("-" * 72)
    print()

    r_values = [0.50, 0.75, 1.00, 1.25, 1.50, 2.00, 3.00, 4.00]

    print(f"{'r':>6s} | {'s (sc)':>10s} | {'s (T1)':>10s} | "
          f"{'Δs/s':>8s} | {'R (m)':>11s} | {'a (m)':>11s} | "
          f"{'δ/a':>8s} | {'q_eff':>8s}")
    print("-" * 90)

    results = []

    for r in r_values:
        sols = solve_shear(r)

        # Track 1 (s=0 geometry) solution for comparison
        def f_t1(s):
            return r**2 * math.sin(2*math.pi*s)**2 / \
                   (4*math.pi * (2-s)**2 * math.sqrt(r**2 + 4)) - alpha

        sols_t1 = []
        s_scan = np.linspace(0.001, 0.999, 5000)
        f_t1_scan = [f_t1(s) for s in s_scan]
        for i in range(len(f_t1_scan) - 1):
            if f_t1_scan[i] * f_t1_scan[i+1] < 0 and s_scan[i] < 0.5:
                sols_t1.append(brentq(f_t1, s_scan[i], s_scan[i+1],
                                      xtol=1e-14))

        if not sols:
            s_t1_str = f"{sols_t1[0]:.6f}" if sols_t1 else "---"
            print(f"{r:6.2f} | {'---':>10s} | {s_t1_str:>10s} | "
                  f"{'---':>8s} | {'---':>11s} | {'---':>11s} | "
                  f"{'---':>8s} | {'---':>8s}")
            continue

        # Take first (smallest) solution
        s_sc = sols[0]
        s_t1 = sols_t1[0] if sols_t1 else float('nan')

        R_sc, a_sc = geometry_sc(r, s_sc)
        delta_over_a = 2 * math.pi * s_sc
        q_eff = 2 - s_sc

        ds_frac = (s_sc - s_t1) / s_t1 if not math.isnan(s_t1) else 0

        results.append((r, s_sc, s_t1, R_sc, a_sc, q_eff))

        print(f"{r:6.2f} | {s_sc:10.6f} | {s_t1:10.6f} | "
              f"{ds_frac:8.4f} | {R_sc:11.4e} | {a_sc:11.4e} | "
              f"{delta_over_a:8.4f} | {q_eff:8.6f}")

    print()

    # ── Section 3: Complete electron geometry table ───────────
    print("SECTION 3: Complete self-consistent electron geometry")
    print("-" * 72)
    print()

    for r, s_sc, s_t1, R_sc, a_sc, q_eff in results:
        L_geo = L_geodesic(r, s_sc, R_sc, a_sc)
        E_phot = h * c / L_geo

        E0 = math.sqrt(E_phot / (eps0 * math.pi**2 * a_sc**2 * R_sc))
        Q = eps0 * E0 * a_sc**2 * math.pi * abs(math.sin(2*math.pi*s_sc)) / abs(q_eff)
        alpha_check = Q**2 / (4 * math.pi * eps0 * hbar * c)

        E_C = Q**2 * g_r / (4 * math.pi * eps0 * R_sc)

        delta = s_sc * 2 * math.pi * a_sc
        delta_over_a = 2 * math.pi * s_sc

        L1 = 2 * math.pi * a_sc
        L2 = 2 * math.pi * R_sc
        cos_lat = s_sc * L1 / math.sqrt((s_sc*L1)**2 + L2**2)
        lat_angle = math.degrees(math.acos(cos_lat))

        V_torus = 2 * math.pi**2 * a_sc**2 * R_sc

        print(f"r = {r:.2f}  (a/R = {r})")
        print(f"  Shear:        s = {s_sc:.8f}   "
              f"(δ/a = {delta_over_a:.4f} rad = "
              f"{math.degrees(delta_over_a):.2f}°)")
        print(f"  Geometry:     R = {R_sc:.6e} m   "
              f"a = {a_sc:.6e} m")
        print(f"  Geodesic:     L = {L_geo:.6e} m   "
              f"(L/λ_C = {L_geo/lambda_C:.10f})")
        print(f"  Photon:       E = {E_phot/E_mc2:.10f} m_e c²")
        print(f"  Charge:       Q = {Q/e:.8f} e   "
              f"(α = {alpha_check:.10f}, α/α_actual = "
              f"{alpha_check/alpha:.8f})")
        print(f"  q_eff:        {q_eff:.8f}")
        print(f"  Lattice:      {lat_angle:.2f}° "
              f"({90-lat_angle:.2f}° from orthogonal)")
        print(f"  E_Coulomb:    {E_C/E_mc2:.6e} m_e c² "
              f"= {E_C/E_mc2/alpha:.2f} α m_e c²")
        print(f"  Volume:       {V_torus:.4e} m³")
        print()

    # ── Section 4: Comparison to Track 1 ──────────────────────
    print("SECTION 4: Impact of self-consistency")
    print("-" * 72)
    print()
    print("The self-consistent Compton constraint shifts s upward")
    print("by a few percent (longer geodesic → smaller torus → need")
    print("slightly more shear to compensate).")
    print()

    if results:
        r1 = [x for x in results if x[0] == 1.0]
        if r1:
            _, s_sc, s_t1, R_sc, a_sc, q_eff = r1[0]
            R_t1, a_t1 = lambda_C / (2*math.pi*math.sqrt(1+4)), \
                         lambda_C / (2*math.pi*math.sqrt(1+4))
            print(f"At r = 1:")
            print(f"  s (Track 1, s=0 geom): {s_t1:.8f}")
            print(f"  s (self-consistent):   {s_sc:.8f}")
            print(f"  Shift:                 {(s_sc-s_t1)/s_t1*100:.2f}%")
            print(f"  R: {R_t1:.6e} → {R_sc:.6e} m  "
                  f"({(R_sc-R_t1)/R_t1*100:.2f}%)")
            print(f"  a: {a_t1:.6e} → {a_sc:.6e} m  "
                  f"({(a_sc-a_t1)/a_t1*100:.2f}%)")
            print()
            print(f"  δ/a = {2*math.pi*s_sc:.6f} rad")
            print(f"  1/(2π) would give δ/a = 1.000000")
            print(f"  Ratio: δ/a ÷ 1 = {2*math.pi*s_sc:.6f}")
            print()

    # ── Section 5: The one-parameter family ───────────────────
    print()
    print("SECTION 5: The electron is a one-parameter family in r")
    print("-" * 72)
    print()
    print("For each aspect ratio r > r_crit, there is a UNIQUE")
    print("self-consistent T² geometry that produces an electron")
    print("with the correct mass, spin, g-factor, and charge.")
    print()
    print("The geometry is fully specified by r alone:")
    print("  1. s(r) from: α = r²sin²(2πs) / (4π(2-s)²√(r²(1+2s)²+4))")
    print("  2. R(r) = λ_C / (2π√(r²(1+2s)²+4))")
    print("  3. a(r) = r × R(r)")
    print("  4. Mass  = m_e c² (by construction)")
    print("  5. Spin  = ½ (topological, from (1,2) winding)")
    print("  6. g     = 2 (leading order, from 2:1 winding ratio)")
    print("  7. Q     = e (from shear s)")
    print()
    print("What determines r?  Nothing on the flat T².")
    print("The aspect ratio is the SINGLE remaining free parameter.")
    print("It must be fixed by physics beyond the flat T²:")
    print("  • T³ modular geometry (three shear parameters constrained)")
    print("  • Topological self-linking (knot invariants in T³)")
    print("  • Multi-particle consistency (electron + quarks share T³)")


if __name__ == "__main__":
    main()
