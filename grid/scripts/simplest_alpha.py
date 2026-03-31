#!/usr/bin/env python3
"""
Find the SIMPLEST triangular lattice torus wrappings that produce
α near known landmarks.

"Simplest" = fewest cells in the fundamental domain.
This identifies the ground-state geometry for each coupling.
"""

import math


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


def main():
    max_n = 25
    targets = {
        '1/137 (electron scale)': 1/137.036,
        '1/128 (Z mass)': 1/128.0,
        '1/80':  1/80.0,
        '1/24':  1/24.0,
    }

    print(f"Searching wrappings with |n|,|m| ≤ {max_n}")
    print()

    seen = set()
    all_results = []

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
                    if r < 0.5:
                        continue

                    key = (round(r, 6), round(s, 6))
                    if key in seen:
                        continue
                    seen.add(key)

                    a = alpha_ma(r, s)
                    if a <= 0 or a > 10:
                        continue

                    all_results.append({
                        'n1': n1, 'm1': m1, 'n2': n2, 'm2': m2,
                        'r': r, 's': s, 'alpha': a,
                        'inv_alpha': 1.0/a,
                        'cells': abs(det),
                    })

    print(f"Total geometries: {len(all_results)}")
    print()

    for tname, tval in sorted(targets.items(), key=lambda x: x[1]):
        print("=" * 76)
        print(f"  {tname}  (target α = {tval:.6f})")
        print("=" * 76)

        # Find matches within 0.5%
        matches = [g for g in all_results
                   if abs(g['alpha'] - tval) / tval < 0.005]
        matches.sort(key=lambda g: g['cells'])

        print(f"  {len(matches)} wrappings within 0.5%")
        print()
        print(f"  {'wrapping':>28s}  {'cells':>5s}  {'r':>7s}  {'s':>10s}"
              f"  {'1/α':>8s}  {'err%':>7s}")
        print("  " + "-" * 72)

        shown_cells = set()
        for g in matches[:20]:
            err = 100 * (g['alpha'] - tval) / tval
            marker = " ★" if g['cells'] == matches[0]['cells'] else ""
            print(f"  ({g['n1']:+3d},{g['m1']:+3d})×({g['n2']:+3d},{g['m2']:+3d})"
                  f"  {g['cells']:5d}  {g['r']:7.3f}  {g['s']:+10.6f}"
                  f"  {g['inv_alpha']:8.2f}  {err:+7.3f}%{marker}")
        print()

    # ── Summary: simplest wrapping for each target ───────────────────
    print("=" * 76)
    print("  SUMMARY: Simplest wrapping for each landmark")
    print("=" * 76)
    print()

    for tname, tval in sorted(targets.items(), key=lambda x: x[1]):
        matches = [g for g in all_results
                   if abs(g['alpha'] - tval) / tval < 0.005]
        if matches:
            best = min(matches, key=lambda g: g['cells'])
            err = 100 * (best['alpha'] - tval) / tval
            print(f"  {tname:25s}  ({best['n1']:+d},{best['m1']:+d})×({best['n2']:+d},{best['m2']:+d})"
                  f"  cells={best['cells']:4d}  r={best['r']:.3f}"
                  f"  s={best['s']:+.6f}  1/α={best['inv_alpha']:.2f}"
                  f"  err={err:+.3f}%")
        else:
            print(f"  {tname:25s}  no match within 0.5%")

    print()

    # ── Do the winning shear values form a pattern? ──────────────────
    print("=" * 76)
    print("  SHEAR VALUES OF SIMPLEST MATCHES (cells ≤ 200)")
    print("=" * 76)
    print()

    for tname, tval in sorted(targets.items(), key=lambda x: x[1]):
        matches = [g for g in all_results
                   if abs(g['alpha'] - tval) / tval < 0.005
                   and g['cells'] <= 200]
        shears = sorted(set(round(g['s'], 6) for g in matches))
        print(f"  {tname}:")
        print(f"    {len(matches)} wrappings, {len(shears)} distinct shear values")
        if shears:
            for sv in shears[:15]:
                gs = [g for g in matches if round(g['s'], 6) == sv]
                rs = [g['r'] for g in gs]
                print(f"      s = {sv:+.6f}  r ∈ [{min(rs):.2f}, {max(rs):.2f}]"
                      f"  ({len(gs)} wrappings)")
        print()


if __name__ == "__main__":
    main()
