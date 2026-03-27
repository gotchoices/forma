#!/usr/bin/env python3
"""
R11 Track 2c: High-resolution Coulomb scan near the minimum.

Dense sampling of every odd q from 125–153, plus context
points, at 40 points per orbit (2× Track 2 resolution).
Also runs 60 pts/orbit for the tightest cluster (133–143)
as a convergence check.
"""

import sys
import os
import math
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import e, eps0, m_e, c, alpha, lambda_C

r_e = e**2 / (4.0 * math.pi * eps0 * m_e * c**2)


def compute_g_uniform(r, N_theta=24, N_phi=48):
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


def compute_g_geodesic(r, q, pts_per_orbit=40):
    R0 = 1.0
    a0 = r * R0
    p = (q - 1) // 2
    N = q * pts_per_orbit

    xs = [0.0] * N
    ys = [0.0] * N
    zs = [0.0] * N

    two_pi = 2.0 * math.pi
    for i in range(N):
        t = (i + 0.5) / N
        theta = two_pi * p * t
        phi = two_pi * q * t
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        rho = R0 + a0 * cos_t
        xs[i] = rho * math.cos(phi)
        ys[i] = rho * math.sin(phi)
        zs[i] = a0 * sin_t

    G = 0.0
    for i in range(N):
        xi, yi, zi = xs[i], ys[i], zs[i]
        for j in range(i + 1, N):
            dx = xi - xs[j]
            dy = yi - ys[j]
            dz = zi - zs[j]
            dist = math.sqrt(dx * dx + dy * dy + dz * dz)
            G += 1.0 / dist

    G /= (N * N)
    return G


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def main():
    t_start = time.time()

    print("R11 Track 2c: High-Resolution Coulomb Scan")
    print("=" * 68)
    print()

    # Precompute g(r) grid
    print("Step 1: Computing uniform shape factor g(r) ...")
    r_grid = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40,
              0.50, 0.60, 0.80, 1.00, 1.25, 1.50, 2.00, 3.00,
              4.00, 5.00]
    g_grid = []
    for r in r_grid:
        g = compute_g_uniform(r)
        g_grid.append(g)
    print(f"  {len(r_grid)} values computed.")
    print()

    def g_interp(r):
        if r <= r_grid[0]:
            return g_grid[0]
        if r >= r_grid[-1]:
            return g_grid[-1]
        for i in range(len(r_grid) - 1):
            if r_grid[i] <= r <= r_grid[i + 1]:
                frac = (r - r_grid[i]) / (r_grid[i + 1] - r_grid[i])
                return g_grid[i] + frac * (g_grid[i + 1] - g_grid[i])
        return g_grid[-1]

    def r_from_q(q_target):
        def q_of_r(r):
            return 1.0 / (2.0 * alpha * g_interp(r)
                          * math.sqrt(1.0 + r * r / 4.0))
        r_lo, r_hi = 0.01, 5.0
        q_lo, q_hi = q_of_r(r_lo), q_of_r(r_hi)
        if q_target < q_lo or q_target > q_hi:
            return None
        for _ in range(80):
            r_mid = (r_lo + r_hi) / 2.0
            if q_of_r(r_mid) < q_target:
                r_lo = r_mid
            else:
                r_hi = r_mid
        return (r_lo + r_hi) / 2.0

    # ── Pass 1: 40 pts/orbit, dense near minimum ────────────────
    q_dense = list(range(125, 154, 2))  # every odd q 125–153
    q_context = [101, 113, 161, 181, 211]
    q_all = sorted(set(q_dense + q_context))

    print("Step 2: Pass 1 — 40 pts/orbit, q = 125–153 + context")
    print()
    print(f"  {'q':>5s}  {'P?':>3s}  {'r':>6s}  {'R/r_e':>6s}  "
          f"{'g_unif':>8s}  {'G_geod':>8s}  "
          f"{'G/g':>7s}  {'excess%':>9s}  {'time':>5s}")
    print(f"  {'─'*5}  {'─'*3}  {'─'*6}  {'─'*6}  "
          f"{'─'*8}  {'─'*8}  "
          f"{'─'*7}  {'─'*9}  {'─'*5}")

    results_40 = []
    for q in q_all:
        r = r_from_q(q)
        if r is None:
            continue
        g_u = g_interp(r)
        R_over_re = 2.0 * g_u

        t0 = time.time()
        G_g = compute_g_geodesic(r, q, pts_per_orbit=40)
        dt = time.time() - t0

        ratio = G_g / g_u
        excess = (ratio - 1.0) * 100.0
        p = is_prime(q)

        results_40.append({
            'q': q, 'prime': p, 'r': r, 'g_u': g_u, 'G_g': G_g,
            'ratio': ratio, 'excess': excess, 'R_re': R_over_re,
        })

        print(f"  {q:5d}  {'★' if p else ' ':>3s}  {r:6.3f}  "
              f"{R_over_re:6.3f}  "
              f"{g_u:8.5f}  {G_g:8.5f}  "
              f"{ratio:7.4f}  {excess:+9.3f}%  {dt:4.1f}s")
        sys.stdout.flush()

    print()

    # ── Pass 2: 60 pts/orbit, tight cluster only ────────────────
    q_tight = [133, 135, 137, 139, 141, 143]

    print("Step 3: Pass 2 — 60 pts/orbit convergence check")
    print()
    print(f"  {'q':>5s}  {'P?':>3s}  {'40pt%':>9s}  "
          f"{'60pt%':>9s}  {'Δ':>8s}")
    print(f"  {'─'*5}  {'─'*3}  {'─'*9}  "
          f"{'─'*9}  {'─'*8}")

    results_60 = []
    for q in q_tight:
        r = r_from_q(q)
        if r is None:
            continue
        g_u = g_interp(r)

        t0 = time.time()
        G_60 = compute_g_geodesic(r, q, pts_per_orbit=60)
        dt = time.time() - t0

        excess_60 = (G_60 / g_u - 1.0) * 100.0

        # Find the 40-pt result for comparison
        exc_40 = None
        for res in results_40:
            if res['q'] == q:
                exc_40 = res['excess']
                break

        delta = excess_60 - exc_40 if exc_40 is not None else 0.0
        p = is_prime(q)

        results_60.append({
            'q': q, 'prime': p, 'excess_40': exc_40,
            'excess_60': excess_60, 'delta': delta,
        })

        print(f"  {q:5d}  {'★' if p else ' ':>3s}  "
              f"{exc_40:+9.3f}%  {excess_60:+9.3f}%  "
              f"{delta:+8.4f}%")
        sys.stdout.flush()

    print()

    # ── Analysis ────────────────────────────────────────────────
    print()
    print("Step 4: Analysis")
    print("-" * 68)
    print()

    # Find minimum in 40-pt results (dense region only)
    dense_results = [r for r in results_40 if 125 <= r['q'] <= 153]
    if dense_results:
        best = min(dense_results, key=lambda r: r['excess'])
        print(f"  40 pts/orbit minimum: q = {best['q']} "
              f"({'prime' if best['prime'] else 'composite'}) "
              f"at {best['excess']:+.3f}%")

    # Find minimum in 60-pt results
    if results_60:
        best60 = min(results_60, key=lambda r: r['excess_60'])
        print(f"  60 pts/orbit minimum: q = {best60['q']} "
              f"({'prime' if best60['prime'] else 'composite'}) "
              f"at {best60['excess_60']:+.3f}%")

    print()

    # Convergence assessment
    if results_60:
        shifts = [abs(r['delta']) for r in results_60]
        max_shift = max(shifts)
        print(f"  Convergence: max |Δ(40→60)| = {max_shift:.4f}%")
        print(f"  (Compare to spread across minimum: "
              f"~{max(r['excess'] for r in dense_results) - min(r['excess'] for r in dense_results):.3f}%)")

        if max_shift < 0.05:
            print("  Resolution is adequate — shifts are smaller "
                  "than the feature width.")
        else:
            print("  Resolution may be insufficient — shifts are "
                  "comparable to the feature width.")
    print()

    # Ranking near minimum
    print("  Ranking near minimum (40 pts/orbit):")
    ranked = sorted(dense_results, key=lambda r: r['excess'])
    for i, r in enumerate(ranked[:8]):
        marker = " ◄" if r['q'] == 137 else ""
        print(f"    {i+1}. q = {r['q']:3d} "
              f"{'★' if r['prime'] else ' '} "
              f"{r['excess']:+.3f}%  R/r_e = {r['R_re']:.3f}"
              f"{marker}")

    print()
    t_total = time.time() - t_start
    print(f"Total runtime: {t_total:.1f}s")


if __name__ == '__main__':
    main()
