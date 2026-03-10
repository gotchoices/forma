#!/usr/bin/env python3
"""
R11 Track 2: Geodesic Coulomb self-energy.

For each q in the R8 solution family, compute the Coulomb
self-energy of charge e distributed along the (p, q) geodesic
path on the torus.  Compare to the uniform-surface-charge
energy (m_e c²/2).

The geodesic has physical winding ratio exactly 1:2 (spin-½):
    θ(t) = π q t       (68.5 minor turns for q=137)
    φ(t) = 2π q t      (137 major turns)
for t ∈ [0, 1].

3D torus embedding:
    x(t) = (R + a cos θ(t)) cos φ(t)
    y(t) = (R + a cos θ(t)) sin φ(t)
    z(t) = a sin θ(t)

We compute dimensionless shape factors at unit scale (R=1)
and derive physical energies analytically.
"""

import sys
import os
import math
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import e, eps0, m_e, c, alpha, lambda_C

r_e = e**2 / (4.0 * math.pi * eps0 * m_e * c**2)
U_target = 0.5 * m_e * c**2


# ── Shape factor: uniform surface charge (from R8) ──────────────

def compute_g_uniform(r, N_theta=24, N_phi=48):
    """
    Dimensionless shape factor g(r) for uniform surface charge.
    U_uniform = g(r) * e² / (4πε₀ R).
    Computed via pairwise Coulomb sum at unit scale.
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


# ── Shape factor: geodesic path charge ──────────────────────────

def compute_g_geodesic(r, q, pts_per_orbit=20):
    """
    Dimensionless shape factor G(r, q) for charge along the
    (p, q) torus knot with p = (q-1)/2.

    U_geodesic = G(r, q) * e² / (4πε₀ R).

    The 3D parameterization uses the LATTICE winding numbers
    (p, q), not the physical 1:2 ratio.  On the sheared T²,
    the physical slope is exactly 1:2, but the 3D torus
    embedding uses p = (q-1)/2, which makes the path close
    and ensures gcd(p, q) = 1 (no self-intersection).

    At unit scale: R = 1, a = r.
    """
    R0 = 1.0
    a0 = r * R0
    p = (q - 1) // 2
    N = q * pts_per_orbit

    xs = [0.0] * N
    ys = [0.0] * N
    zs = [0.0] * N

    for i in range(N):
        t = (i + 0.5) / N
        theta = 2.0 * math.pi * p * t
        phi = 2.0 * math.pi * q * t
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


# ── R8 solution curve ───────────────────────────────────────────

def r_from_q_bisect(q_target, g_func):
    """
    Find the aspect ratio r for a given q by bisection.

    Uses the relation: q = 1 / (2α g(r) √(1 + r²/4))
    q increases with r (g drops faster than √(1+r²/4) grows).
    """
    def q_of_r(r):
        g = g_func(r)
        return 1.0 / (2.0 * alpha * g * math.sqrt(1.0 + r * r / 4.0))

    r_lo, r_hi = 0.01, 5.0
    q_lo = q_of_r(r_lo)
    q_hi = q_of_r(r_hi)
    if q_target < q_lo or q_target > q_hi:
        return None

    for _ in range(80):
        r_mid = (r_lo + r_hi) / 2.0
        if q_of_r(r_mid) < q_target:
            r_lo = r_mid
        else:
            r_hi = r_mid
    return (r_lo + r_hi) / 2.0


# ── Main ─────────────────────────────────────────────────────────

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

    print("R11 Track 2: Geodesic Coulomb Self-Energy")
    print("=" * 68)
    print()

    # Precompute g_uniform for a grid of r values, then interpolate
    print("Step 1: Computing uniform shape factor g(r) ...")
    r_grid = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40,
              0.50, 0.60, 0.80, 1.00, 1.25, 1.50, 2.00, 3.00,
              4.00, 5.00]
    g_grid = []
    for r in r_grid:
        t0 = time.time()
        g = compute_g_uniform(r)
        dt = time.time() - t0
        g_grid.append(g)
        print(f"  r = {r:.2f}  g = {g:.6f}  ({dt:.1f}s)")
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

    # Select q values to study: a mix of primes and composites
    # near 137, plus a broader sweep
    q_study = sorted(set([
        # Broad sweep (odd only)
        101, 111, 121, 131, 141, 151, 161, 171, 181, 191,
        201, 211, 221, 231, 241, 251, 261, 271, 281,
        # Dense near 137
        127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147,
        # Specific primes
        113, 127, 131, 137, 139, 149, 151, 157, 163,
    ]))
    q_study = [q for q in q_study if q % 2 == 1]

    pts_per_orbit = 20

    print(f"Step 2: Computing geodesic shape factor G(r, q)")
    print(f"  Points per orbit: {pts_per_orbit}")
    print()
    print(f"  {'q':>5s}  {'P?':>3s}  {'r':>6s}  "
          f"{'g_unif':>8s}  {'G_geod':>8s}  "
          f"{'G/g':>6s}  {'excess%':>8s}  {'time':>5s}")
    print(f"  {'─'*5}  {'─'*3}  {'─'*6}  "
          f"{'─'*8}  {'─'*8}  "
          f"{'─'*6}  {'─'*8}  {'─'*5}")

    results = []

    for q in q_study:
        r = r_from_q_bisect(q, g_interp)
        if r is None:
            continue

        g_u = g_interp(r)
        R_phys = 2.0 * g_u * r_e

        t0 = time.time()
        G_g = compute_g_geodesic(r, q, pts_per_orbit)
        dt = time.time() - t0

        ratio = G_g / g_u
        excess_pct = (ratio - 1.0) * 100.0

        p = is_prime(q)
        results.append({
            'q': q, 'prime': p, 'r': r, 'g_u': g_u, 'G_g': G_g,
            'ratio': ratio, 'excess_pct': excess_pct,
        })

        print(f"  {q:5d}  {'★' if p else ' ':>3s}  {r:6.3f}  "
              f"{g_u:8.5f}  {G_g:8.5f}  "
              f"{ratio:6.3f}  {excess_pct:+8.2f}%  {dt:4.1f}s")
        sys.stdout.flush()

    print()

    # Step 3: Analysis
    print()
    print("Step 3: Analysis")
    print("-" * 68)
    print()

    prime_results = [r for r in results if r['prime']]
    comp_results = [r for r in results if not r['prime']]

    if prime_results:
        excess_p = [r['excess_pct'] for r in prime_results]
        print(f"  Primes ({len(prime_results)} values):")
        print(f"    Excess energy: min = {min(excess_p):+.2f}%, "
              f"max = {max(excess_p):+.2f}%, "
              f"mean = {sum(excess_p)/len(excess_p):+.2f}%")

    if comp_results:
        excess_c = [r['excess_pct'] for r in comp_results]
        print(f"  Composites ({len(comp_results)} values):")
        print(f"    Excess energy: min = {min(excess_c):+.2f}%, "
              f"max = {max(excess_c):+.2f}%, "
              f"mean = {sum(excess_c)/len(excess_c):+.2f}%")

    print()

    # Find q with minimum excess
    if results:
        best = min(results, key=lambda r: r['excess_pct'])
        print(f"  Minimum excess: q = {best['q']} "
              f"({'prime' if best['prime'] else 'composite'}) "
              f"at {best['excess_pct']:+.2f}%")

        # Also find minimum among primes near 137
        near_primes = [r for r in prime_results
                       if abs(r['q'] - 137) <= 20]
        if near_primes:
            best_np = min(near_primes,
                          key=lambda r: r['excess_pct'])
            print(f"  Best prime near 137: q = {best_np['q']} "
                  f"at {best_np['excess_pct']:+.2f}%")

    print()

    # Check monotonicity
    excess_vals = [r['excess_pct'] for r in results]
    q_vals = [r['q'] for r in results]
    monotone = all(excess_vals[i] >= excess_vals[i+1]
                   for i in range(len(excess_vals) - 1))
    print(f"  Monotonically decreasing with q: "
          f"{'YES' if monotone else 'NO'}")

    if not monotone:
        # Look for local structure
        print("  Non-monotonic structure detected — searching for")
        print("  local minima...")
        for i in range(1, len(results) - 1):
            if (results[i]['excess_pct'] < results[i-1]['excess_pct']
                    and results[i]['excess_pct']
                    < results[i+1]['excess_pct']):
                r = results[i]
                print(f"    Local minimum: q = {r['q']} "
                      f"({'prime' if r['prime'] else 'comp'}) "
                      f"at {r['excess_pct']:+.2f}%")
    print()

    t_total = time.time() - t_start
    print(f"Total runtime: {t_total:.1f}s")


if __name__ == '__main__':
    main()
