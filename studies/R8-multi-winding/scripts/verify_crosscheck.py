#!/usr/bin/env python3
"""
Cross-check: compare symmetry-reduced g with full pairwise sum
at r = 1/π, using small grids where the full sum is feasible.
"""

import sys
import os
import math
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha


def compute_g_full(r, N_theta, N_phi):
    """Original full pairwise sum (O(N²))."""
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


def compute_g_symm(r, N_theta, N_phi):
    """Symmetry-reduced sum (O(N_θ² × N_φ))."""
    d_theta = 2.0 * math.pi / N_theta
    d_phi = 2.0 * math.pi / N_phi

    rhos, zvals, dAs_list = [], [], []
    A_total = 0.0

    for i in range(N_theta):
        theta = (i + 0.5) * d_theta
        rho = 1.0 + r * math.cos(theta)
        z = r * math.sin(theta)
        dA = abs(rho) * r * d_theta * d_phi
        rhos.append(rho)
        zvals.append(z)
        dAs_list.append(dA)
        A_total += dA * N_phi

    dq = [a / A_total for a in dAs_list]
    dQ = [q * N_phi for q in dq]
    cos_k = [math.cos(k * d_phi) for k in range(N_phi)]

    g_val = 0.0
    for i in range(N_theta):
        ri, zi = rhos[i], zvals[i]
        Vi = 0.0
        for j in range(N_theta):
            rj, zj = rhos[j], zvals[j]
            dz2 = (zi - zj) ** 2
            A = ri * ri + rj * rj + dz2
            B = 2.0 * ri * rj
            qj = dq[j]
            if i == j:
                for k in range(1, N_phi):
                    Vi += qj / math.sqrt(A - B * cos_k[k])
            else:
                for k in range(N_phi):
                    Vi += qj / math.sqrt(A - B * cos_k[k])
        g_val += 0.5 * dQ[i] * Vi

    return g_val


def main():
    r = 1.0 / math.pi

    grids = [(16, 32), (24, 48), (32, 64), (48, 96)]

    print("Cross-check: full pairwise vs symmetry-reduced")
    print("=" * 60)
    print(f"  r = 1/π = {r:.8f}")
    print()
    print(f"{'N_θ':>4s}×{'N_φ':>4s}  {'g_full':>14s}  {'g_symm':>14s}"
          f"  {'diff':>12s}  {'t_full':>6s}  {'t_symm':>6s}")
    print("-" * 70)

    for N_theta, N_phi in grids:
        t0 = time.time()
        g_full = compute_g_full(r, N_theta, N_phi)
        t_full = time.time() - t0

        t0 = time.time()
        g_symm = compute_g_symm(r, N_theta, N_phi)
        t_symm = time.time() - t0

        diff = g_symm - g_full

        print(f"{N_theta:4d}×{N_phi:4d}  {g_full:14.10f}  {g_symm:14.10f}"
              f"  {diff:+12.4e}  {t_full:5.1f}s  {t_symm:5.1f}s")

    print()
    print("Note: 48×96 full sum takes ~20-30s; be patient.")


if __name__ == '__main__':
    main()
