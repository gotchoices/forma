#!/usr/bin/env python3
"""
R11 Track 1: Divisor spectrum and sub-harmonic analysis.

For each q in the R8 solution range (~100–287), compute:
  1. Prime factorization and divisor count
  2. Sub-harmonic score: weighted count of divisor-related
     leakage channels
  3. Whether the sheared T² admits sub-periodic geodesic
     closure (analytical check)

The hypothesis: prime q concentrates all field energy in the
fundamental Compton resonance.  Composite q allows sub-harmonic
modes that can drain energy.  137 is prime.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha, lambda_C, e, eps0, m_e, c

r_e = e**2 / (4.0 * math.pi * eps0 * m_e * c**2)

# ── Number theory helpers ────────────────────────────────────────

def factorize(n):
    """Return prime factorization as list of (prime, exponent) pairs."""
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            exp = 0
            while n % d == 0:
                n //= d
                exp += 1
            factors.append((d, exp))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def divisors(n):
    """Return sorted list of all divisors of n."""
    divs = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return sorted(divs)


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


def sub_harmonic_score(q):
    """
    Weighted sub-harmonic leakage score.

    For each non-trivial divisor d of q (1 < d < q), the
    sub-harmonic at frequency ω_C × d/q can potentially
    couple to external radiation.  Weight by 1/d² (radiation
    coupling scales as frequency²).

    Returns 0 for prime q.
    """
    score = 0.0
    for d in divisors(q):
        if d == 1 or d == q:
            continue
        score += 1.0 / (d * d)
    return score


# ── Geodesic closure analysis ────────────────────────────────────

def check_sub_closure(q):
    """
    Check if the 1:2 geodesic on the sheared T² (with
    δ = L_θ/(2q)) has any sub-periodic closure at m < q.

    For the geodesic to close at m orbits, we need:
        n = m(q-1)/(2q)  to be an integer

    Since gcd(q, q-1) = 1, this requires q | m.
    So the first closure is always at m = q, regardless
    of whether q is prime or composite.
    """
    closures = []
    for m in range(1, q):
        n_exact = m * (q - 1) / (2.0 * q)
        if abs(n_exact - round(n_exact)) < 1e-9:
            closures.append((m, round(n_exact)))
    return closures


# ── R8 solution curve (simplified) ──────────────────────────────

def compute_g_uniform(r, N_theta=24, N_phi=48):
    """
    Shape factor g(r) for uniform surface charge at unit scale.
    Computed via pairwise Coulomb sum (same method as R8).
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


# Precomputed g(r) grid — filled at startup
_g_r_pts = []
_g_g_pts = []


def _init_g_grid():
    """Compute g(r) for a grid of r values (runs once)."""
    global _g_r_pts, _g_g_pts
    r_vals = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40,
              0.50, 0.60, 0.80, 1.00, 1.25, 1.50, 2.00, 3.00,
              4.00, 5.00]
    print("  Precomputing g(r) grid ... ", end="", flush=True)
    for r in r_vals:
        _g_r_pts.append(r)
        _g_g_pts.append(compute_g_uniform(r))
    print("done.")
    print()


def compute_g_approx(r):
    """Interpolate g(r) from precomputed grid."""
    if r <= _g_r_pts[0]:
        return _g_g_pts[0]
    if r >= _g_r_pts[-1]:
        return _g_g_pts[-1]
    for i in range(len(_g_r_pts) - 1):
        if _g_r_pts[i] <= r <= _g_r_pts[i + 1]:
            frac = (r - _g_r_pts[i]) / (_g_r_pts[i + 1] - _g_r_pts[i])
            return _g_g_pts[i] + frac * (_g_g_pts[i + 1] - _g_g_pts[i])
    return _g_g_pts[-1]


def q_from_r(r):
    """Winding number q as function of aspect ratio r."""
    g = compute_g_approx(r)
    return 1.0 / (2.0 * alpha * g * math.sqrt(1.0 + r * r / 4.0))


def r_from_q(q_target):
    """Invert q(r) to find r for a given integer q.
    q increases with r (g drops faster than √(1+r²/4) grows).
    """
    r_lo, r_hi = 0.01, 5.0
    q_lo = q_from_r(r_lo)
    q_hi = q_from_r(r_hi)
    if q_target < q_lo or q_target > q_hi:
        return None
    for _ in range(100):
        r_mid = (r_lo + r_hi) / 2.0
        if q_from_r(r_mid) < q_target:
            r_lo = r_mid
        else:
            r_hi = r_mid
    return (r_lo + r_hi) / 2.0


# ── Main ─────────────────────────────────────────────────────────

def main():
    print("R11 Track 1: Divisor Spectrum and Sub-Harmonic Analysis")
    print("=" * 68)
    print()

    _init_g_grid()

    # Part 1: Sub-periodic closure proof
    print("Part 1: Sub-periodic geodesic closure on sheared T²")
    print("-" * 68)
    print()
    print("  On a sheared T² with δ = L_θ/(2q), the 1:2 geodesic")
    print("  closes at lattice winding (n, m) when n = m(q−1)/(2q).")
    print("  Since gcd(q, q−1) = 1, the smallest m giving integer n")
    print("  is m = q.  No sub-periodic closures exist for ANY q.")
    print()

    test_qs = [131, 135, 136, 137, 139, 140]
    print(f"  {'q':>5s}  {'prime?':>6s}  {'sub-closures at m < q':>24s}")
    print(f"  {'─'*5}  {'─'*6}  {'─'*24}")
    for q in test_qs:
        subs = check_sub_closure(q)
        prime_str = "YES" if is_prime(q) else "no"
        sub_str = str(subs) if subs else "none"
        print(f"  {q:5d}  {prime_str:>6s}  {sub_str:>24s}")

    print()
    print("  Result: NO sub-periodic closures for any q tested.")
    print("  The sheared T² enforces full q-orbit closure regardless")
    print("  of q's divisor structure.  This is proven analytically:")
    print("  gcd(q, q−1) = 1 ⟹ q | m is required ⟹ m_min = q.")
    print()

    # Part 2: Full divisor spectrum
    print()
    print("Part 2: Divisor spectrum across the solution range")
    print("-" * 68)
    print()

    q_min, q_max = 100, 287

    # Header
    print(f"  {'q':>5s}  {'P?':>3s}  {'factors':>22s}  "
          f"{'#div':>4s}  {'Σ div':>6s}  {'S_sub':>7s}  "
          f"{'r':>6s}  {'R/r_e':>6s}")
    print(f"  {'─'*5}  {'─'*3}  {'─'*22}  "
          f"{'─'*4}  {'─'*6}  {'─'*7}  "
          f"{'─'*6}  {'─'*6}")

    primes_in_range = []
    composites_in_range = []

    for q in range(q_min, q_max + 1):
        if q % 2 == 0:
            continue  # only odd q (even q can't give spin-½)

        r = r_from_q(q)
        if r is None:
            continue
        g = compute_g_approx(r)
        R_over_re = 2.0 * g

        p = is_prime(q)
        facts = factorize(q)
        divs = divisors(q)
        n_divs = len(divs)
        sum_divs = sum(divs)
        s_sub = sub_harmonic_score(q)

        if p:
            primes_in_range.append(q)
        else:
            composites_in_range.append(q)

        fact_str = " × ".join(
            f"{b}" if e == 1 else f"{b}^{e}" for b, e in facts
        )
        if len(fact_str) > 22:
            fact_str = fact_str[:19] + "..."

        marker = " ★" if p else ""
        print(f"  {q:5d}  {'★' if p else ' ':>3s}  {fact_str:>22s}  "
              f"{n_divs:4d}  {sum_divs:6d}  {s_sub:7.4f}  "
              f"{r:6.3f}  {R_over_re:6.3f}")

    print()

    # Part 3: Summary statistics
    print()
    print("Part 3: Summary")
    print("-" * 68)
    print()
    print(f"  Odd q values in range [{q_min}, {q_max}]: "
          f"{len(primes_in_range) + len(composites_in_range)}")
    print(f"  Primes: {len(primes_in_range)}")
    print(f"  Composites: {len(composites_in_range)}")
    print()

    # Sub-harmonic scores
    prime_scores = [sub_harmonic_score(q) for q in primes_in_range]
    comp_scores = [sub_harmonic_score(q) for q in composites_in_range]

    print("  Sub-harmonic scores (S_sub):")
    print(f"    Primes:     all = 0.0000 (by definition)")
    if comp_scores:
        print(f"    Composites: min = {min(comp_scores):.4f}, "
              f"max = {max(comp_scores):.4f}, "
              f"mean = {sum(comp_scores)/len(comp_scores):.4f}")
    print()

    # Primes near 137
    nearby = [q for q in primes_in_range if abs(q - 137) <= 20]
    print("  Primes within ±20 of 137:")
    for q in nearby:
        r = r_from_q(q)
        g = compute_g_approx(r)
        R_phys = 2.0 * g * r_e
        print(f"    q = {q:3d}  →  R/r_e = {2*g:.4f}  "
              f"(R = {R_phys:.4e} m)")
    print()

    # Key observation
    print("  Key finding from Part 1:")
    print("  The sheared T² prevents sub-periodic closure for ALL q.")
    print("  The geodesic path always makes exactly q orbits before")
    print("  closing, regardless of q's factorization.")
    print()
    print("  This means the prime/composite distinction does NOT")
    print("  affect the geodesic path topology.  If it matters")
    print("  physically, it must enter through the FIELD structure")
    print("  (mode coupling, radiation spectrum, or Coulomb energy)")
    print("  rather than the path geometry.")
    print()
    print("  → Track 2 computes the geodesic Coulomb self-energy")
    print("    to test whether the charge distribution distinguishes")
    print("    prime from composite q.")


if __name__ == '__main__':
    main()
