#!/usr/bin/env python3
"""
Recompute the solution curve at multiple resolutions
to see how q(r) shifts with grid refinement.
"""

import sys
import os
import math
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha, m_e, c, e, eps0, lambda_C

r_e = e**2 / (4 * math.pi * eps0 * m_e * c**2)


def compute_g(r, N_theta, N_phi):
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
    _sqrt = math.sqrt

    g_val = 0.0
    for i in range(N_theta):
        ri, zi = rhos[i], zvals[i]
        Vi = 0.0
        for j in range(N_theta):
            rj, zj = rhos[j], zvals[j]
            dz2 = (zi - zj) * (zi - zj)
            A = ri * ri + rj * rj + dz2
            B = 2.0 * ri * rj
            qj = dq[j]
            if i == j:
                for k in range(1, N_phi):
                    Vi += qj / _sqrt(A - B * cos_k[k])
            else:
                for k in range(N_phi):
                    Vi += qj / _sqrt(A - B * cos_k[k])
        g_val += 0.5 * dQ[i] * Vi
    return g_val


def main():
    r_values = [0.10, 0.20, 0.30, 0.40, 0.50, 0.75, 1.00]
    resolutions = [
        (24, 48),
        (32, 64),
        (64, 128),
        (128, 256),
        (192, 384),
    ]

    print("Solution curve g(r) at multiple resolutions")
    print("=" * 72)
    print()

    # Header
    res_labels = [f"{nt}×{np_}" for nt, np_ in resolutions]
    print(f"{'r':>6s}", end="")
    for label in res_labels:
        print(f"  {label:>14s}", end="")
    print()
    print("-" * (6 + 16 * len(resolutions)))

    g_data = {}
    for r in r_values:
        print(f"{r:6.2f}", end="", flush=True)
        g_data[r] = {}
        for N_theta, N_phi in resolutions:
            t0 = time.time()
            g = compute_g(r, N_theta, N_phi)
            dt = time.time() - t0
            g_data[r][(N_theta, N_phi)] = g
            print(f"  {g:14.8f}", end="", flush=True)
        print()

    print()
    print()
    print("Derived winding number q(r) at each resolution")
    print("=" * 72)
    print()

    print(f"{'r':>6s}", end="")
    for label in res_labels:
        print(f"  {label:>10s}", end="")
    print()
    print("-" * (6 + 12 * len(resolutions)))

    for r in r_values:
        print(f"{r:6.2f}", end="")
        for N_theta, N_phi in resolutions:
            g = g_data[r][(N_theta, N_phi)]
            R = 2 * g * r_e
            q = lambda_C / (2 * math.pi * R * math.sqrt(1 + r**2 / 4))
            print(f"  {q:10.2f}", end="")
        print()

    print()
    print()
    print("R/r_e at each resolution")
    print("=" * 72)
    print()

    print(f"{'r':>6s}", end="")
    for label in res_labels:
        print(f"  {label:>10s}", end="")
    print()
    print("-" * (6 + 12 * len(resolutions)))

    for r in r_values:
        print(f"{r:6.2f}", end="")
        for N_theta, N_phi in resolutions:
            g = g_data[r][(N_theta, N_phi)]
            R = 2 * g * r_e
            print(f"  {R/r_e:10.4f}", end="")
        print()

    # Find q = 137 crossing at each resolution
    print()
    print()
    print("Where does q = 137 fall?")
    print("=" * 72)
    print()

    for N_theta, N_phi in resolutions:
        label = f"{N_theta}×{N_phi}"
        q_vals = []
        for r in r_values:
            g = g_data[r][(N_theta, N_phi)]
            R = 2 * g * r_e
            q = lambda_C / (2 * math.pi * R * math.sqrt(1 + r**2/4))
            q_vals.append((r, q))

        for i in range(len(q_vals) - 1):
            r1, q1 = q_vals[i]
            r2, q2 = q_vals[i + 1]
            if (q1 - 137) * (q2 - 137) <= 0:
                frac = (137 - q1) / (q2 - q1)
                r_137 = r1 + frac * (r2 - r1)
                g_137 = g_data[r1][(N_theta, N_phi)] + frac * (
                    g_data[r2][(N_theta, N_phi)] - g_data[r1][(N_theta, N_phi)])
                R_137 = 2 * g_137 * r_e
                print(f"  {label:>8s}:  r ≈ {r_137:.4f}  "
                      f"g ≈ {g_137:.6f}  R/r_e ≈ {R_137/r_e:.4f}")
                break
        else:
            print(f"  {label:>8s}:  q = 137 not in sampled range")


if __name__ == '__main__':
    main()
