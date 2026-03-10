#!/usr/bin/env python3
"""
R8 Track 5: High-resolution verification of g(1/π).

Does the torus shape factor at aspect ratio r = 1/π equal
π/√(4π²+1) exactly?

If so, then q = 1/α exactly and δ = αR exactly:
  R = 2g r_e = 2πr_e / √(4π²+1)
  q = λ_C / (2πR √(1+r²/4))
    = λ_C / (2π × 2πr_e/√(4π²+1) × √((4π²+1)/(4π²)))
    = λ_C / (2πr_e)
    = λ̄_C / r_e
    = 1/α

Uses rotational symmetry to reduce pairwise sum from
O(N²) to O(N_θ² × N_φ), enabling much finer grids.
"""

import sys
import os
import math
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha, m_e, c, e, eps0, lambda_C, hbar

r_e = e**2 / (4 * math.pi * eps0 * m_e * c**2)
lambda_bar_C = hbar / (m_e * c)


def compute_g(r, N_theta, N_phi):
    """
    Shape factor g(r) using φ-symmetry-reduced pairwise sum.

    Fixes one reference point per ring at (ρ_i, 0, z_i) and
    sums over all (θ_j, φ_k) grid points. By rotational
    symmetry, V is the same at every φ on a given ring.

    Cost: O(N_θ² × N_φ) instead of O((N_θ N_φ)²).
    """
    d_theta = 2.0 * math.pi / N_theta
    d_phi = 2.0 * math.pi / N_phi

    rhos = []
    zvals = []
    dAs = []
    A_total = 0.0

    for i in range(N_theta):
        theta = (i + 0.5) * d_theta
        rho = 1.0 + r * math.cos(theta)
        z = r * math.sin(theta)
        dA = abs(rho) * r * d_theta * d_phi
        rhos.append(rho)
        zvals.append(z)
        dAs.append(dA)
        A_total += dA * N_phi

    dq = [a / A_total for a in dAs]
    dQ = [q * N_phi for q in dq]

    cos_k = [math.cos(k * d_phi) for k in range(N_phi)]

    g_val = 0.0
    _sqrt = math.sqrt

    for i in range(N_theta):
        ri = rhos[i]
        zi = zvals[i]
        Vi = 0.0

        for j in range(N_theta):
            rj = rhos[j]
            zj = zvals[j]
            dz2 = (zi - zj) * (zi - zj)
            A = ri * ri + rj * rj + dz2
            B = 2.0 * ri * rj
            qj = dq[j]

            if i == j:
                for k in range(1, N_phi):
                    d2 = A - B * cos_k[k]
                    Vi += qj / _sqrt(d2)
            else:
                for k in range(N_phi):
                    d2 = A - B * cos_k[k]
                    Vi += qj / _sqrt(d2)

        g_val += 0.5 * dQ[i] * Vi

    return g_val


def main():
    r = 1.0 / math.pi
    g_target = math.pi / math.sqrt(4 * math.pi**2 + 1)

    print("R8 Track 5: High-Resolution g(1/π)")
    print("=" * 68)
    print()
    print(f"  r = 1/π = {r:.10f}")
    print(f"  g_target = π/√(4π²+1) = {g_target:.10f}")
    print()

    R_exact = 2 * g_target * r_e
    q_exact = lambda_C / (2 * math.pi * R_exact
                          * math.sqrt(1 + r**2 / 4))
    print("  If g(1/π) = π/√(4π²+1):")
    print(f"    R = {R_exact:.6e} m  ({R_exact/r_e:.6f} r_e)")
    print(f"    q = {q_exact:.8f}")
    print(f"    1/α = {1/alpha:.8f}")
    print(f"    q − 1/α = {q_exact - 1/alpha:.2e}")
    print(f"    δ = αR = {alpha * R_exact:.4e} m")
    print()

    grids = [
        (16, 32),
        (24, 48),
        (32, 64),
        (48, 96),
        (64, 128),
        (96, 192),
        (128, 256),
        (192, 384),
        (256, 512),
    ]

    print(f"{'N_θ':>5s}  {'N_φ':>5s}  {'N_eff':>9s}   {'g':>14s}"
          f"   {'err':>12s}   {'pct':>8s}   {'t':>6s}")
    print("-" * 72)

    results = []
    for N_theta, N_phi in grids:
        N_eff = N_theta * N_phi

        t0 = time.time()
        g = compute_g(r, N_theta, N_phi)
        dt = time.time() - t0

        err = g - g_target
        pct = 100 * err / g_target
        results.append((N_theta, N_phi, N_eff, g, err, pct, dt))

        print(f"{N_theta:5d}  {N_phi:5d}  {N_eff:9d}   {g:14.10f}"
              f"   {err:+12.4e}   {pct:+8.4f}%   {dt:5.1f}s")
        sys.stdout.flush()

    print()

    # Convergence analysis
    print("Convergence (error reduction per grid step):")
    print()
    for i in range(1, len(results)):
        e_prev = abs(results[i - 1][4])
        e_curr = abs(results[i][4])
        Nt_prev = results[i - 1][0]
        Nt_curr = results[i][0]
        if e_curr > 1e-15 and e_prev > 1e-15:
            ratio = e_prev / e_curr
            nt_ratio = Nt_curr / Nt_prev
            order = math.log(ratio) / math.log(nt_ratio)
            print(f"  {Nt_prev:3d}×{results[i-1][1]:3d} → "
                  f"{Nt_curr:3d}×{results[i][1]:3d}:  "
                  f"|err| {e_prev:.3e} → {e_curr:.3e}  "
                  f"(÷{ratio:.2f},  order ≈ {order:.2f})")

    print()

    # Richardson extrapolation
    if len(results) >= 3:
        print("Richardson extrapolation (last 3 grids):")
        for order_guess in [0.5, 1.0, 1.5, 2.0]:
            idx = len(results) - 1
            pairs = []
            for k in range(2):
                i = idx - k
                j = idx - k - 1
                N1 = results[j][0]
                N2 = results[i][0]
                g1 = results[j][3]
                g2 = results[i][3]
                h1 = N1 ** (-order_guess)
                h2 = N2 ** (-order_guess)
                g_inf = (g2 * h1 - g1 * h2) / (h1 - h2)
                pairs.append(g_inf)
            avg = sum(pairs) / len(pairs)
            print(f"  O(N_θ^{-order_guess:.1f}):  g_∞ = {avg:.10f}"
                  f"  (err {avg - g_target:+.4e})")

    print()
    print("=" * 68)
    print()
    print(f"  Target:     π/√(4π²+1) = {g_target:.10f}")
    if results:
        g_best = results[-1][3]
        err_best = results[-1][4]
        pct_best = results[-1][5]
        print(f"  Best grid:  g = {g_best:.10f}  "
              f"({results[-1][0]}×{results[-1][1]})")
        print(f"  Error:      {err_best:+.4e}  ({pct_best:+.4f}%)")
    print()


if __name__ == '__main__':
    main()
