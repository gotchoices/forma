#!/usr/bin/env python3
"""
Find the "magic" shear angles on a triangular lattice.

A magic shear is one where the two wrapping vectors of the torus
have a special geometric relationship — e.g., related by a lattice
symmetry, or producing a particularly simple rational shear value.

This script focuses on:
1. The discrete set of shear values available at small integers
2. Which of these produce α near known landmarks
3. Whether there's a pattern or selection principle

Also explores: for a FIXED small shear (near s ≈ 0.01), what
aspect ratios r are available, and do any give α ≈ 1/137?
"""

import math
from fractions import Fraction


def norm2(n, m):
    return n*n + n*m + m*m

def dot(n1, m1, n2, m2):
    return n1*n2 + m1*m2 + (n1*m2 + m1*n2) / 2.0

def cross(n1, m1, n2, m2):
    return n1*m2 - m1*n2

def alpha_ma(r, s):
    if abs(s) < 1e-15 or abs(2 - s) < 1e-15:
        return 0.0
    mu = math.sqrt(1.0 / r**2 + (2.0 - s)**2)
    return r**2 * mu * math.sin(2 * math.pi * s)**2 / (4 * math.pi * (2 - s)**2)


def analyze():
    max_n = 20

    print("=" * 72)
    print("ANALYSIS 1: All distinct rational shear values s = p/q")
    print("            from small-integer wrappings")
    print("=" * 72)
    print()

    # Collect all (s, r, wrapping) triples
    all_geoms = []
    seen_sr = set()

    for n1 in range(-max_n, max_n + 1):
        for m1 in range(-max_n, max_n + 1):
            N1 = norm2(n1, m1)
            if N1 == 0:
                continue
            for n2 in range(-max_n, max_n + 1):
                for m2 in range(-max_n, max_n + 1):
                    N2 = norm2(n2, m2)
                    if N2 == 0:
                        continue
                    det = cross(n1, m1, n2, m2)
                    if det == 0:
                        continue

                    D = dot(n1, m1, n2, m2)
                    s = D / N1
                    R2sq = N2 - D*D/N1
                    if R2sq <= 0:
                        continue
                    r = math.sqrt(N1 / R2sq)

                    if r < 0.5 or abs(s) > 0.49:
                        continue

                    key = (round(r, 6), round(s, 6))
                    if key in seen_sr:
                        continue
                    seen_sr.add(key)

                    a = alpha_ma(r, s)
                    if a <= 0 or a > 10:
                        continue

                    all_geoms.append({
                        'n1': n1, 'm1': m1, 'n2': n2, 'm2': m2,
                        'r': r, 's': s, 'alpha': a,
                        'inv_alpha': 1.0/a,
                        'cells': abs(det),
                    })

    print(f"Total unique (r, s) geometries: {len(all_geoms)}")
    print()

    # ── Find which simple rational shears exist ──────────────────────
    print("=" * 72)
    print("ANALYSIS 2: Simple rational shears s = p/q (small q)")
    print("            and the range of α they produce")
    print("=" * 72)
    print()

    # Group by s value (rounded)
    from collections import defaultdict
    by_shear = defaultdict(list)
    for g in all_geoms:
        s_key = round(g['s'], 6)
        by_shear[s_key].append(g)

    # Find shears that are simple fractions
    simple_shears = []
    for s_val, geoms in sorted(by_shear.items()):
        if abs(s_val) < 1e-6:
            continue
        frac = Fraction(s_val).limit_denominator(100)
        if frac.denominator <= 20 and abs(float(frac) - s_val) < 1e-6:
            alphas = [g['alpha'] for g in geoms]
            rs = [g['r'] for g in geoms]
            simple_shears.append((s_val, frac, min(alphas), max(alphas),
                                  min(rs), max(rs), len(geoms)))

    print(f"{'s':>10s}  {'frac':>8s}  {'α_min':>10s}  {'α_max':>10s}"
          f"  {'1/α_min':>8s}  {'1/α_max':>8s}  {'r range':>16s}  {'count':>5s}")
    print("-" * 90)
    for s_val, frac, amin, amax, rmin, rmax, cnt in sorted(simple_shears, key=lambda x: abs(x[0])):
        print(f"{s_val:+10.6f}  {str(frac):>8s}  {amin:10.6f}  {amax:10.6f}"
              f"  {1/amax:8.2f}  {1/amin:8.2f}  [{rmin:.2f}, {rmax:.2f}]  {cnt:5d}")

    print()

    # ── Focus on small shears (near electron's s ≈ 0.01) ────────────
    print("=" * 72)
    print("ANALYSIS 3: Small shear values (|s| < 0.1)")
    print("            and which give α near known landmarks")
    print("=" * 72)
    print()

    small_s = [g for g in all_geoms if abs(g['s']) < 0.1 and abs(g['s']) > 0.001]
    small_s.sort(key=lambda g: abs(g['s']))

    targets = {137: 1/137.036, 128: 1/128.0, 80: 1/80.0, 24: 1/24.0}

    for tname, tval in sorted(targets.items()):
        matches = sorted([g for g in small_s if abs(g['alpha'] - tval)/tval < 0.01],
                         key=lambda g: abs(g['alpha'] - tval))
        print(f"  α = 1/{tname}: {len(matches)} wrappings within 1% (small s only)")
        for g in matches[:8]:
            err = 100 * (g['alpha'] - tval) / tval
            print(f"    ({g['n1']:+d},{g['m1']:+d})×({g['n2']:+d},{g['m2']:+d})"
                  f"  r={g['r']:7.3f}  s={g['s']:+.6f}  α={g['alpha']:.6f}"
                  f"  1/α={g['inv_alpha']:.2f}  err={err:+.3f}%  cells={g['cells']}")
        print()

    # ── High-symmetry wrappings ──────────────────────────────────────
    print("=" * 72)
    print("ANALYSIS 4: Perpendicular wrappings (s = 0) and near-perpendicular")
    print("=" * 72)
    print()

    near_perp = [g for g in all_geoms if abs(g['s']) < 0.005]
    near_perp.sort(key=lambda g: (abs(g['s']), g['cells']))

    print(f"  {'wrapping':>24s}  {'r':>8s}  {'s':>10s}  {'α':>10s}  {'1/α':>8s}  {'cells':>5s}")
    print("  " + "-" * 72)
    for g in near_perp[:25]:
        print(f"  ({g['n1']:+d},{g['m1']:+d})×({g['n2']:+d},{g['m2']:+d})"
              f"  {g['r']:8.4f}  {g['s']:+10.6f}  {g['alpha']:10.6f}"
              f"  {g['inv_alpha']:8.2f}  {g['cells']:5d}")

    print()

    # ── Can we hit 1/137 with moderate r and small s? ────────────────
    print("=" * 72)
    print("ANALYSIS 5: Wrappings with r ∈ [1, 10] and |s| < 0.1")
    print("            sorted by proximity to α = 1/137")
    print("=" * 72)
    print()

    moderate = [g for g in all_geoms
                if 1.0 <= g['r'] <= 10.0 and abs(g['s']) < 0.1]
    moderate.sort(key=lambda g: abs(g['alpha'] - 1/137.036))

    for g in moderate[:25]:
        err = 100 * (g['alpha'] - 1/137.036) / (1/137.036)
        print(f"  ({g['n1']:+d},{g['m1']:+d})×({g['n2']:+d},{g['m2']:+d})"
              f"  r={g['r']:7.3f}  s={g['s']:+.6f}  1/α={g['inv_alpha']:8.2f}"
              f"  err={err:+.3f}%  cells={g['cells']}")

    print()

    # ── What s values does α_ma = 1/137 require for each r? ──────────
    print("=" * 72)
    print("ANALYSIS 6: Required shear s for α = 1/137 at various r")
    print("            (continuous, not lattice-constrained)")
    print("=" * 72)
    print()

    from scipy.optimize import brentq

    target_alpha = 1/137.036
    print(f"  {'r':>6s}  {'s_required':>12s}  {'1/s':>8s}  {'s as fraction':>16s}")
    print("  " + "-" * 50)
    for r in [0.6, 0.8, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]:
        try:
            s_soln = brentq(lambda s: alpha_ma(r, s) - target_alpha, 0.001, 0.49)
            frac = Fraction(s_soln).limit_denominator(1000)
            print(f"  {r:6.1f}  {s_soln:12.8f}  {1/s_soln:8.2f}  ≈ {frac}")
        except Exception:
            print(f"  {r:6.1f}  no solution")

    print()
    print("These are the CONTINUOUS s values needed. The triangular lattice")
    print("can only produce DISCRETE s = (dot product) / (norm²).")
    print("A match requires integer vectors that produce this exact ratio.")


if __name__ == "__main__":
    analyze()
