#!/usr/bin/env python3
"""
R12 Track 1: Spectral structure of the flat sheared T²

Can the scalar wave equation on the flat sheared torus constrain
the shear parameter δ?

Key question: does a self-consistent propagating mode at the
Compton frequency ω_C exist on the flat sheared T²?

The mode spectrum is:
    ω(n,m) = c √(n²/a² + (m − n δ/L_θ)²/R²)

With spin-½ shear δ/L_θ = 1/(2q):
    ω(n,m) = c √(n²/a² + (m − n/(2q))²/R²)

We compute:
  (A) The ratio ω_C / ω_min across the R8 solution curve
  (B) Whether ANY eigenmode sits at ω_C (for any shear)
  (C) The geodesic mode — what frequency it actually has
  (D) Shear sweep — spectral structure vs continuous δ
  (E) Phase coherence check along the geodesic
"""

import sys
import os
import math
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import (h, hbar, c, eps0, e, alpha, m_e, lambda_C)

r_e = e**2 / (4.0 * math.pi * eps0 * m_e * c**2)
lambda_bar = hbar / (m_e * c)
omega_C = m_e * c**2 / hbar


def compute_g(r, N_theta=32, N_phi=64):
    """Shape factor g(r) for a torus with R=1, a=r."""
    R0 = 1.0
    a0 = r * R0
    d_theta = 2.0 * math.pi / N_theta
    d_phi = 2.0 * math.pi / N_phi

    xs, ys, zs, dAs = [], [], [], []
    A_total = 0.0
    for i in range(N_theta):
        theta = (i + 0.5) * d_theta
        rho = R0 + a0 * math.cos(theta)
        dA = abs(rho) * a0 * d_theta * d_phi
        sin_t = math.sin(theta)
        for j in range(N_phi):
            phi = (j + 0.5) * d_phi
            xs.append(rho * math.cos(phi))
            ys.append(rho * math.sin(phi))
            zs.append(a0 * sin_t)
            dAs.append(dA)
            A_total += dA

    N = len(xs)
    dqs = [dA / A_total for dA in dAs]
    g_val = 0.0
    for i in range(N):
        qi = dqs[i]
        xi, yi, zi = xs[i], ys[i], zs[i]
        for j in range(i + 1, N):
            dx = xi - xs[j]
            dy = yi - ys[j]
            dz = zi - zs[j]
            dist = math.sqrt(dx*dx + dy*dy + dz*dz)
            g_val += qi * dqs[j] / dist
    return g_val


def q_from_r(r, g):
    """Winding number q from aspect ratio r and shape factor g."""
    return 1.0 / (2.0 * alpha * g * math.sqrt(1.0 + r*r / 4.0))


def geometry_from_r(r, g):
    """Physical geometry from aspect ratio and shape factor."""
    R = 2.0 * g * r_e
    a = r * R
    q = q_from_r(r, g)
    return R, a, q


def mode_freq_squared(n, m, a, R, shear_frac):
    """
    ω²/c² for mode (n,m) on the flat sheared T².
    shear_frac = δ/L_θ (fractional shear).
    """
    k_theta = n / a
    k_phi = (m - n * shear_frac) / R
    return k_theta**2 + k_phi**2


def find_nearest_mode(a, R, shear_frac, target_omega_over_c,
                      n_max=5, m_max=500):
    """Find the eigenmode closest to a target frequency."""
    target2 = target_omega_over_c**2
    best = None
    best_diff = float('inf')
    for n in range(-n_max, n_max + 1):
        m_center = n * shear_frac
        for m in range(int(m_center - m_max), int(m_center + m_max) + 1):
            if n == 0 and m == 0:
                continue
            w2 = mode_freq_squared(n, m, a, R, shear_frac)
            if w2 <= 0:
                continue
            diff = abs(w2 - target2)
            if diff < best_diff:
                best_diff = diff
                best = (n, m, math.sqrt(w2))
    return best


def main():
    t_start = time.time()
    print("R12 Track 1: Spectral Structure of the Flat Sheared T²")
    print("=" * 72)
    print()
    print(f"  λ_C       = {lambda_C:.6e} m")
    print(f"  λ̄_C       = {lambda_bar:.6e} m")
    print(f"  r_e       = {r_e:.6e} m")
    print(f"  α         = {alpha:.6e}  (1/α = {1/alpha:.2f})")
    print(f"  ω_C       = {omega_C:.6e} rad/s")
    print(f"  ω_C/c     = {omega_C/c:.6e} m⁻¹  (= 1/λ̄_C)")
    print()

    # ════════════════════════════════════════════════════════════
    # Part A: Compton frequency vs torus spectrum
    # ════════════════════════════════════════════════════════════
    print("Part A: Compton frequency vs torus mode spectrum")
    print("-" * 72)
    print()
    print("  The lowest eigenmode on the flat T² is ω_min = c/R.")
    print("  The Compton frequency is ω_C = c/λ̄_C.")
    print("  Ratio: ω_C/ω_min = R/λ̄_C = 2g(r)·α")
    print()

    r_values = [0.10, 0.20, 0.31, 0.40, 0.50, 0.75, 1.00, 1.50, 2.00]

    print(f"  {'r':>6s}  {'g(r)':>8s}  {'q':>8s}  {'R/r_e':>8s}"
          f"  {'ω_C/ω_min':>12s}  {'= 2gα':>10s}  {'ratio':>8s}")
    print(f"  {'─'*6}  {'─'*8}  {'─'*8}  {'─'*8}"
          f"  {'─'*12}  {'─'*10}  {'─'*8}")

    computed = []
    for r in r_values:
        g = compute_g(r)
        R, a, q = geometry_from_r(r, g)
        omega_min = c / R
        ratio = omega_C / omega_min
        two_g_alpha = 2.0 * g * alpha
        check = ratio / two_g_alpha

        computed.append((r, g, q, R, a))

        print(f"  {r:6.2f}  {g:8.4f}  {q:8.1f}  {R/r_e:8.4f}"
              f"  {ratio:12.6f}  {two_g_alpha:10.6f}  {check:8.4f}")

    print()
    print("  ω_C/ω_min = 2gα ≈ α ≈ 1/137 for all geometries.")
    print("  The Compton frequency is ~137× BELOW the lowest torus mode.")
    print("  This ratio is geometry-independent (fixed by the charge")
    print("  constraint R = 2g r_e and the definition α = r_e/λ̄_C).")
    print()

    # ════════════════════════════════════════════════════════════
    # Part B: Can ANY mode sit at ω_C?
    # ════════════════════════════════════════════════════════════
    print()
    print("Part B: Can any eigenmode have frequency ω_C?")
    print("-" * 72)
    print()
    print("  For n = 0: ω(0,m) = c|m|/R.  Need m = R/λ̄_C = 2gα ≈ 0.007.")
    print("  Not an integer.  No n=0 mode at ω_C.")
    print()
    print("  For n ≥ 1: the n²/a² term alone already exceeds ω_C²/c².")
    print("  Check: (c/a) / ω_C = λ̄_C/a = 1/(2grα)")
    print()

    print(f"  {'r':>6s}  {'q':>8s}  {'a (m)':>12s}"
          f"  {'c/a (Hz)':>14s}  {'ω_C (Hz)':>14s}  {'(c/a)/ω_C':>10s}")
    print(f"  {'─'*6}  {'─'*8}  {'─'*12}"
          f"  {'─'*14}  {'─'*14}  {'─'*10}")

    for r, g, q, R, a in computed:
        c_over_a = c / a
        ratio = c_over_a / omega_C
        print(f"  {r:6.2f}  {q:8.1f}  {a:12.4e}"
              f"  {c_over_a:14.4e}  {omega_C:14.4e}  {ratio:10.1f}")

    print()
    print("  For ALL geometries, c/a > 100 × ω_C.")
    print("  Any mode with n ≥ 1 has ω ≥ c/a ≫ ω_C.")
    print("  Combined with Part A (no n=0 mode at ω_C):")
    print("  ┌─────────────────────────────────────────────────────────┐")
    print("  │  NO eigenmode of the flat sheared T² has frequency ω_C │")
    print("  │  for ANY geometry on the R8 solution curve.            │")
    print("  │  This holds for ALL values of the shear δ.             │")
    print("  └─────────────────────────────────────────────────────────┘")
    print()

    # ════════════════════════════════════════════════════════════
    # Part C: The geodesic mode
    # ════════════════════════════════════════════════════════════
    print()
    print("Part C: What is the 'geodesic mode'?")
    print("-" * 72)
    print()
    print("  The photon's geodesic closes at lattice point")
    print("  (n₀, m₀) = ((q-1)/2, q).  The corresponding")
    print("  eigenmode has frequency ω_geo ≠ ω_C.")
    print()

    print(f"  {'r':>6s}  {'q':>5s}  {'n₀':>5s}  {'m₀':>5s}"
          f"  {'ω_geo/ω_C':>12s}  {'ω_geo/ω_min':>12s}")
    print(f"  {'─'*6}  {'─'*5}  {'─'*5}  {'─'*5}"
          f"  {'─'*12}  {'─'*12}")

    for r, g, q_exact, R, a in computed:
        q = int(round(q_exact))
        if q % 2 == 0:
            q += 1
        n0 = (q - 1) // 2
        m0 = q
        shear_frac = 1.0 / (2.0 * q)

        w2 = mode_freq_squared(n0, m0, a, R, shear_frac)
        if w2 > 0:
            omega_geo = c * math.sqrt(w2)
            omega_min = c / R
            print(f"  {r:6.2f}  {q:5d}  {n0:5d}  {m0:5d}"
                  f"  {omega_geo/omega_C:12.1f}"
                  f"  {omega_geo/omega_min:12.1f}")

    print()
    print("  The geodesic mode frequency is ~q²/2 times ω_C.")
    print("  It is a very high-frequency mode — NOT the photon's")
    print("  Compton oscillation.")
    print()

    # Verify: geodesic direction vs wavevector direction
    print("  Geodesic direction vs wavevector direction:")
    print()
    r_test, g_test = 0.31, computed[2][1]
    q_test = int(round(computed[2][2]))
    if q_test % 2 == 0:
        q_test += 1
    R_t, a_t = computed[2][3], computed[2][4]
    n0_t = (q_test - 1) // 2
    m0_t = q_test
    sf = 1.0 / (2.0 * q_test)

    geo_dir_x = a_t
    geo_dir_y = 2.0 * R_t
    geo_norm = math.sqrt(geo_dir_x**2 + geo_dir_y**2)
    geo_ux = geo_dir_x / geo_norm
    geo_uy = geo_dir_y / geo_norm

    k_x = n0_t / a_t
    k_y = (m0_t - n0_t * sf) / R_t
    k_norm = math.sqrt(k_x**2 + k_y**2)
    k_ux = k_x / k_norm
    k_uy = k_y / k_norm

    dot = geo_ux * k_ux + geo_uy * k_uy
    angle = math.degrees(math.acos(min(1.0, max(-1.0, dot))))

    print(f"    Geodesic direction: ({geo_ux:.4f}, {geo_uy:.4f})")
    print(f"    Wavevector direction: ({k_ux:.4f}, {k_uy:.4f})")
    print(f"    Angle between them: {angle:.2f}°")
    print()
    print("  The wavevector is NOT aligned with the geodesic.")
    print("  The mode (n₀, m₀) is a plane wave whose phase fronts")
    print("  are oblique to the geodesic path — it is not 'a wave")
    print("  propagating along the geodesic.'")
    print()

    # ════════════════════════════════════════════════════════════
    # Part D: Shear sweep — mode structure vs continuous δ
    # ════════════════════════════════════════════════════════════
    print()
    print("Part D: Shear sweep — does any δ bring a mode to ω_C?")
    print("-" * 72)
    print()
    print("  Fix geometry at r = 0.31 (the q ≈ 137 solution).")
    print("  Sweep δ/L_θ from 0 to 0.1 and find the mode nearest ω_C.")
    print()

    r_fix = 0.31
    g_fix = compute_g(r_fix)
    R_fix = 2.0 * g_fix * r_e
    a_fix = r_fix * R_fix
    target = omega_C / c

    shear_fracs = [i * 0.005 for i in range(21)]
    print(f"  {'δ/L_θ':>8s}  {'nearest (n,m)':>16s}"
          f"  {'ω_near/ω_C':>12s}  {'gap':>12s}")
    print(f"  {'─'*8}  {'─'*16}  {'─'*12}  {'─'*12}")

    for sf in shear_fracs:
        nearest = find_nearest_mode(a_fix, R_fix, sf, target,
                                    n_max=2, m_max=20)
        if nearest:
            n_near, m_near, w_near = nearest
            ratio = (w_near * c) / omega_C
            gap = abs(ratio - 1.0)
            print(f"  {sf:8.4f}  ({n_near:3d}, {m_near:3d})"
                  f"        {ratio:12.4f}  {gap:12.4f}")

    print()
    print("  The nearest mode is always (0, ±1) with ω = c/R ≈ 137 ω_C.")
    print("  No shear value brings ANY mode close to ω_C.")
    print()

    # ════════════════════════════════════════════════════════════
    # Part E: Phase coherence along geodesic
    # ════════════════════════════════════════════════════════════
    print()
    print("Part E: Phase coherence along the geodesic")
    print("-" * 72)
    print()
    print("  The photon must accumulate exactly 2π of phase after")
    print("  traversing the full geodesic path (one Compton wavelength).")
    print()
    print("  Path length: ℓ = qπ√(a² + 4R²) = λ_C  (mass condition)")
    print("  Phase condition: k × ℓ = 2π  →  k = 2π/λ_C = 1/λ̄_C")
    print("  This gives: ω = ck = c/λ̄_C = ω_C  ✓")
    print()
    print("  But this is IDENTICAL to the mass condition.")
    print("  The phase coherence requirement adds NO new information")
    print("  beyond what is already imposed by requiring path = λ_C.")
    print()

    for r, g, q_exact, R, a in computed[:5]:
        q = int(round(q_exact))
        if q % 2 == 0:
            q += 1
        path_length = q * math.pi * math.sqrt(a**2 + 4*R**2)
        n_wavelengths = path_length / lambda_C
        phase_total = 2.0 * math.pi * n_wavelengths
        phase_per_orbit = phase_total / q

        print(f"    r={r:.2f}, q={q:4d}: path/λ_C = {n_wavelengths:.6f},"
              f"  phase/orbit = 2π/{q} = {phase_per_orbit/(2*math.pi):.6f}"
              f" × 2π")

    print()
    print("  Phase per orbit = 2π/q = 2πα (for q ≈ 1/α).")
    print("  This is a restatement of the mass + charge constraints.")
    print()

    # ════════════════════════════════════════════════════════════
    # Part F: Summary
    # ════════════════════════════════════════════════════════════
    print()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print()
    print("  1. SPECTRAL GAP: ω_C / ω_min = 2gα ≈ α ≈ 1/137.")
    print("     The Compton frequency is ~137× below the lowest")
    print("     eigenmode of the flat T².  This holds for ALL")
    print("     geometries on the R8 solution curve.")
    print()
    print("  2. NO MODE AT ω_C: For n ≥ 1, c/a ≫ ω_C (by factor")
    print("     ~400).  For n = 0, ω(0,m) = mc/R requires m = 2gα")
    print("     ≈ 0.007 (not an integer).  No eigenmode exists at ω_C")
    print("     for ANY value of the shear δ.")
    print()
    print("  3. GEODESIC MODE: The eigenmode (n₀,m₀) = ((q-1)/2, q)")
    print("     corresponding to the geodesic lattice point has")
    print("     frequency ~q²ω_C/2 — thousands of times above ω_C.")
    print("     Its wavevector is oblique to the geodesic direction.")
    print()
    print("  4. PHASE COHERENCE = MASS CONDITION: The requirement")
    print("     that the photon accumulate 2π phase per path is")
    print("     algebraically identical to path = λ_C.  No new")
    print("     constraint.")
    print()
    print("  5. SHEAR IS UNCONSTRAINED: The flat-T² scalar wave")
    print("     equation provides no condition on δ beyond the")
    print("     mass constraint.  The shear δ remains a free")
    print("     parameter.")
    print()
    print("  ┌──────────────────────────────────────────────────────┐")
    print("  │  CONCLUSION: The scalar wave equation on the flat   │")
    print("  │  sheared T² cannot constrain the shear.             │")
    print("  │                                                      │")
    print("  │  The Compton frequency sits in a spectral gap —     │")
    print("  │  there are literally no eigenmodes at ω_C.          │")
    print("  │  The 'photon' is not a torus eigenmode.             │")
    print("  │                                                      │")
    print("  │  IMPLICATIONS FOR R12:                               │")
    print("  │  • Track 2 (curved torus) won't help — curvature   │")
    print("  │    modifies ω by ~r ≈ 0.3, far too small to bridge │")
    print("  │    the ~137× gap.                                   │")
    print("  │  • Track 3 (full Maxwell) may differ — EM          │")
    print("  │    polarization couples E and B, potentially        │")
    print("  │    allowing sub-spectral propagating solutions.     │")
    print("  │  • The photon on the torus is a PROPAGATING WAVE   │")
    print("  │    along the geodesic, not a standing eigenmode.    │")
    print("  │    The self-consistency question may need to be     │")
    print("  │    formulated as a 1D propagation problem along     │")
    print("  │    the geodesic, not a 2D eigenvalue problem.       │")
    print("  └──────────────────────────────────────────────────────┘")
    print()

    dt = time.time() - t_start
    print(f"Total runtime: {dt:.1f}s")


if __name__ == '__main__':
    main()
