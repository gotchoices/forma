#!/usr/bin/env python3
"""
R8. Multi-winding electron — geometry search.

Find the torus geometry (winding number q, aspect ratio r = a/R)
where the Coulomb self-energy of charge e equals m_e c²/2.

Method:
  1. Compute dimensionless shape factor g(r) at unit scale
     using direct pairwise Coulomb summation.
  2. Derive q(r) analytically from mass + charge constraints.
  3. Report the solution curve and integer-q candidates.
"""

import sys
import os
import math
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import (h, hbar, c, eps0, e, alpha, m_e, lambda_C)

U_target = 0.5 * m_e * c**2
r_e = e**2 / (4.0 * math.pi * eps0 * m_e * c**2)


def compute_shape_factor(r, N_theta=24, N_phi=48):
    """
    Dimensionless shape factor g(r) for a torus with R=1, a=r.

    Defined by:  U = g(r) * Q^2 / (4*pi*eps0*R)

    Computed via direct pairwise sum of uniform surface charge
    at unit scale with unit total charge.
    """
    R0 = 1.0
    a0 = r * R0

    d_theta = 2.0 * math.pi / N_theta
    d_phi = 2.0 * math.pi / N_phi

    xs, ys, zs, dAs = [], [], [], []
    A_total = 0.0

    for i in range(N_theta):
        theta = (i + 0.5) * d_theta
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        rho = R0 + a0 * cos_t
        dA = abs(rho) * a0 * d_theta * d_phi

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
            dist = math.sqrt(dx * dx + dy * dy + dz * dz)
            g_val += qi * dqs[j] / dist

    return g_val


def find_coprime_p(q):
    """Find p closest to q/2 with gcd(p, q) = 1."""
    p = round(q / 2.0)
    if p < 1:
        p = 1
    best = p
    for offset in range(q):
        for candidate in [p - offset, p + offset]:
            if candidate >= 1 and math.gcd(candidate, q) == 1:
                return candidate
    return best


def main():
    t_start = time.time()

    print("R8: Multi-Winding Electron — Geometry Search")
    print("=" * 62)
    print()
    print("Constants:")
    print(f"  lambda_C = {lambda_C:.6e} m")
    print(f"  r_e      = {r_e:.6e} m")
    print(f"  alpha    = {alpha:.6e}")
    print(f"  1/alpha  = {1.0 / alpha:.4f}")
    print(f"  U_target = {U_target:.6e} J  (= m_e c^2 / 2)")
    print()

    N_theta = 24
    N_phi = 48
    N_src = N_theta * N_phi
    print(f"Surface discretization: {N_theta} x {N_phi} = {N_src} elements")
    print()

    r_values = [0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0,
                4.0, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0]

    print("Part 1: Shape factor g(r) and derived winding number q")
    print()
    print(f"{'r':>6s}  {'g(r)':>10s}  {'R (m)':>12s}  {'a (m)':>12s}"
          f"  {'q (exact)':>10s}  {'time':>5s}")
    print("-" * 68)

    results = []
    for r in r_values:
        t0 = time.time()
        g = compute_shape_factor(r, N_theta, N_phi)
        dt = time.time() - t0

        R_phys = 2.0 * g * r_e
        a_phys = r * R_phys
        q_exact = lambda_C / (2.0 * math.pi * R_phys
                              * math.sqrt(1.0 + r * r / 4.0))

        results.append((r, g, R_phys, a_phys, q_exact))
        print(f"{r:6.2f}  {g:10.6f}  {R_phys:12.4e}  {a_phys:12.4e}"
              f"  {q_exact:10.2f}  {dt:4.1f}s")
        sys.stdout.flush()

    print()

    # --- Part 2: interpolate to find r for integer q values ---

    print("Part 2: Integer winding numbers along the solution curve")
    print()
    print("  For each integer q, interpolate to find the aspect")
    print("  ratio r, then compute R, a, and p.")
    print()
    print(f"{'q':>6s}  {'p':>6s}  {'r':>8s}  {'R (m)':>12s}"
          f"  {'a (m)':>12s}  {'R/r_e':>8s}")
    print("-" * 62)

    q_min = int(min(res[4] for res in results))
    q_max = int(max(res[4] for res in results)) + 1

    integer_solutions = []

    for q_target in range(max(q_min, 50), min(q_max, 500) + 1):
        for k in range(len(results) - 1):
            q1 = results[k][4]
            q2 = results[k + 1][4]
            if (q1 - q_target) * (q2 - q_target) <= 0:
                r1, g1 = results[k][0], results[k][1]
                r2, g2 = results[k + 1][0], results[k + 1][1]
                if abs(q2 - q1) < 1e-10:
                    continue
                frac = (q_target - q1) / (q2 - q1)
                r_interp = r1 + frac * (r2 - r1)
                g_interp = g1 + frac * (g2 - g1)
                R_interp = 2.0 * g_interp * r_e
                a_interp = r_interp * R_interp
                p_val = find_coprime_p(q_target)

                integer_solutions.append(
                    (q_target, p_val, r_interp, R_interp,
                     a_interp, R_interp / r_e))

                print(f"{q_target:6d}  {p_val:6d}  {r_interp:8.3f}"
                      f"  {R_interp:12.4e}  {a_interp:12.4e}"
                      f"  {R_interp / r_e:8.4f}")
                break

    print()

    # --- Part 3: summary ---

    print("=" * 62)
    print()
    print("Summary")
    print()
    print(f"  Classical electron radius r_e = {r_e:.4e} m")
    print(f"  Compton-scale radius (WvM)    = {lambda_C / (4 * math.pi):.4e} m")
    print(f"  Ratio (Compton / r_e)         = {lambda_C / (4 * math.pi * r_e):.1f}")
    print()

    if integer_solutions:
        q_vals = [s[0] for s in integer_solutions]
        print(f"  Winding numbers q with solutions: {min(q_vals)} to {max(q_vals)}")
        print(f"  (One solution per integer q in this range)")
        print()

        close_137 = min(integer_solutions,
                        key=lambda s: abs(s[0] - round(1.0 / alpha)))
        print(f"  Nearest to 1/alpha = {1.0/alpha:.2f}:")
        print(f"    q = {close_137[0]}, p = {close_137[1]}, "
              f"r = {close_137[2]:.3f}")
        print(f"    R = {close_137[3]:.4e} m  "
              f"({close_137[5]:.3f} r_e)")
        print(f"    a = {close_137[4]:.4e} m")
        print()

        print("  Note: q is NOT constrained to be near 137.")
        print("  Every integer q in the range has a valid geometry.")
        print("  The 'right' q depends on which r (and hence which")
        print("  precession rate) nature selects.")

    print()
    t_total = time.time() - t_start
    print(f"Total runtime: {t_total:.1f}s")


if __name__ == '__main__':
    main()
