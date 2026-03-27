#!/usr/bin/env python3
"""
R11 Track 2c: Convergence study for geodesic Coulomb energy.

Runs at 20, 40, 80, 120, 160 pts/orbit for a selection of q values
spanning the candidate minimum. Uses the convergence rate to
estimate the continuum limit and determine whether the minimum
location is resolved.
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


def compute_g_geodesic(r, q, pts_per_orbit):
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


def main():
    t_start = time.time()

    print("R11 Track 2c: Convergence Study")
    print("=" * 72)
    print()

    # Precompute g(r)
    print("Step 1: Computing g(r) grid ...")
    r_grid = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40,
              0.50, 0.60, 0.80, 1.00, 1.25, 1.50, 2.00, 3.00,
              4.00, 5.00]
    g_grid = [compute_g_uniform(r) for r in r_grid]
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
        if q_target < q_of_r(r_lo) or q_target > q_of_r(r_hi):
            return None
        for _ in range(80):
            r_mid = (r_lo + r_hi) / 2.0
            if q_of_r(r_mid) < q_target:
                r_lo = r_mid
            else:
                r_hi = r_mid
        return (r_lo + r_hi) / 2.0

    # q values to study: span the candidate minimum region
    q_values = [113, 121, 125, 129, 133, 137, 139, 143, 149, 161]
    resolutions = [20, 40, 80, 120]

    print("Step 2: Convergence table")
    print()

    # Header
    hdr = f"  {'q':>5s}  {'r':>6s}"
    for pp in resolutions:
        hdr += f"  {pp:>7d}pt"
    hdr += "   extrap"
    print(hdr)
    print(f"  {'─'*5}  {'─'*6}" +
          f"  {'─'*9}" * len(resolutions) + f"  {'─'*9}")

    all_data = []

    for q in q_values:
        r = r_from_q(q)
        if r is None:
            continue

        g_u = g_interp(r)
        row_excess = []

        line = f"  {q:5d}  {r:6.3f}"

        for ppo in resolutions:
            t0 = time.time()
            G = compute_g_geodesic(r, q, ppo)
            dt = time.time() - t0
            excess = (G / g_u - 1.0) * 100.0
            row_excess.append(excess)
            line += f"  {excess:+8.3f}%"
            sys.stdout.flush()

        # Richardson extrapolation using last two resolutions
        # Error scales as 1/N ~ 1/pts_per_orbit for midpoint rule
        # in a Coulomb sum. Try h² extrapolation first.
        h1, h2 = 1.0 / resolutions[-2], 1.0 / resolutions[-1]
        e1, e2 = row_excess[-2], row_excess[-1]
        # Linear extrapolation to h=0
        extrap_lin = e2 - h2 * (e1 - e2) / (h1 - h2)
        # h² extrapolation (if error ~ h²)
        extrap_h2 = (e2 * h1**2 - e1 * h2**2) / (h1**2 - h2**2)

        line += f"  {extrap_lin:+8.3f}%"
        print(line)

        all_data.append({
            'q': q, 'r': r, 'g_u': g_u,
            'excess': dict(zip(resolutions, row_excess)),
            'extrap_lin': extrap_lin,
            'extrap_h2': extrap_h2,
        })

    print()

    # ── Analysis ────────────────────────────────────────────────
    print()
    print("Step 3: Analysis")
    print("-" * 72)
    print()

    # Convergence rate: compute ratio of successive differences
    print("  Convergence rate (ratio of successive corrections):")
    print(f"  {'q':>5s}  {'Δ(20→40)':>10s}  {'Δ(40→80)':>10s}  "
          f"{'Δ(80→120)':>10s}  {'ratio':>6s}")
    print(f"  {'─'*5}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*6}")

    for d in all_data:
        ex = d['excess']
        d12 = ex[40] - ex[20]
        d23 = ex[80] - ex[40]
        d34 = ex[120] - ex[80]
        ratio = d23 / d12 if abs(d12) > 1e-10 else float('nan')
        print(f"  {d['q']:5d}  {d12:+10.4f}  {d23:+10.4f}  "
              f"{d34:+10.4f}  {ratio:6.3f}")

    print()

    # Minimum location at each resolution
    print("  Minimum-excess q at each resolution:")
    for ppo in resolutions:
        best = min(all_data, key=lambda d: d['excess'][ppo])
        print(f"    {ppo:>4d} pts/orbit: q = {best['q']:3d} "
              f"at {best['excess'][ppo]:+.3f}%")

    # Extrapolated minimum
    best_ext = min(all_data, key=lambda d: d['extrap_lin'])
    print(f"    extrap (lin): q = {best_ext['q']:3d} "
          f"at {best_ext['extrap_lin']:+.3f}%")
    best_h2 = min(all_data, key=lambda d: d['extrap_h2'])
    print(f"    extrap (h²):  q = {best_h2['q']:3d} "
          f"at {best_h2['extrap_h2']:+.3f}%")

    print()

    # Ranking at highest resolution
    print("  Ranking at 120 pts/orbit:")
    ranked = sorted(all_data, key=lambda d: d['excess'][120])
    for i, d in enumerate(ranked):
        marker = " ◄" if d['q'] == 137 else ""
        print(f"    {i+1}. q = {d['q']:3d}  "
              f"{d['excess'][120]:+.3f}%  "
              f"extrap = {d['extrap_lin']:+.3f}%"
              f"{marker}")

    print()
    t_total = time.time() - t_start
    print(f"Total runtime: {t_total:.1f}s")


if __name__ == '__main__':
    main()
