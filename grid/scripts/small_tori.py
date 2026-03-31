#!/usr/bin/env python3
"""
Enumerate ALL triangular lattice tori at small cell counts.

At small scales, the discrete α spectrum is sparse enough
to see structure.  This script lists every possible α value
for tori with 1 to 40 unit cells (2 to 80 triangles).

Also flags: minimum torus size for physical modes, given
the windowing constraint (ζ = 1/4 → need ≥ 4 triangles
per bit → ≥ 2 unit cells per bit).
"""

import math
from collections import defaultdict


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
    val = r**2 * mu * math.sin(2 * math.pi * s)**2 / (4 * math.pi * (2 - s)**2)
    return val


def main():
    max_det = 50
    max_n = 30  # need enough range to find all small-det tori

    # Collect tori grouped by cell count (|det|)
    by_det = defaultdict(list)
    seen = set()

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
                    adet = abs(int(det))
                    if adet == 0 or adet > max_det:
                        continue

                    D = dot(n1, m1, n2, m2)
                    s = D / N1
                    R2sq = N2 - D*D/N1
                    if R2sq <= 1e-10:
                        continue
                    r = math.sqrt(N1 / R2sq)

                    if r < 0.5:
                        continue

                    key = (adet, round(r, 6), round(s, 6))
                    if key in seen:
                        continue
                    seen.add(key)

                    a = alpha_ma(r, s)
                    if a <= 0 or a > 100:
                        continue

                    by_det[adet].append({
                        'n1': n1, 'm1': m1, 'n2': n2, 'm2': m2,
                        'r': r, 's': s, 'alpha': a,
                        'inv_alpha': 1.0/a,
                        'det': adet,
                    })

    # Report
    print("=" * 78)
    print("  COMPLETE α SPECTRUM FOR SMALL TRIANGULAR TORI")
    print("  (unit cells = parallelograms; each contains 2 triangles)")
    print("=" * 78)
    print()

    landmark_alpha = {
        137: 1/137.036,
        128: 1/128.0,
        80:  1/80.0,
        24:  1/24.0,
    }

    all_close = []  # track closest to 1/137 at each size

    for det in range(1, max_det + 1):
        entries = by_det.get(det, [])
        if not entries:
            continue

        n_triangles = 2 * det
        n_bits = n_triangles / 4.0  # at ζ = 1/4

        # Unique α values at this det
        alpha_vals = sorted(set(round(e['alpha'], 8) for e in entries))
        inv_alpha_vals = sorted(set(round(e['inv_alpha'], 4) for e in entries))

        # Find closest to 1/137
        closest_137 = min(entries, key=lambda e: abs(e['alpha'] - 1/137.036))
        err_137 = 100 * (closest_137['alpha'] - 1/137.036) / (1/137.036)
        all_close.append((det, closest_137, err_137))

        print(f"{'─'*78}")
        print(f"  {det} unit cells  ({n_triangles} triangles, "
              f"~{n_bits:.1f} bits at ζ=1/4)")
        print(f"  {len(entries)} geometries, {len(alpha_vals)} distinct α values")
        print(f"  Closest to 1/137: 1/α = {closest_137['inv_alpha']:.2f}"
              f"  (err = {err_137:+.2f}%)"
              f"  wrapping ({closest_137['n1']:+d},{closest_137['m1']:+d})"
              f"×({closest_137['n2']:+d},{closest_137['m2']:+d})")

        if det <= 12:
            # Show all α values for very small tori
            print(f"  All 1/α values:")
            for ia in sorted(inv_alpha_vals):
                markers = []
                for lm, la in landmark_alpha.items():
                    if abs(1/ia - la) / la < 0.05:
                        markers.append(f"≈ 1/{lm}")
                mark = f"  {'  '.join(markers)}" if markers else ""
                print(f"    1/α = {ia:10.3f}{mark}")

        print()

    # Summary: convergence toward 1/137
    print("=" * 78)
    print("  CONVERGENCE: closest α to 1/137 vs torus size")
    print("=" * 78)
    print()
    print(f"  {'cells':>5s}  {'triangles':>9s}  {'bits':>5s}"
          f"  {'1/α closest':>11s}  {'error':>8s}  {'wrapping':>28s}")
    print("  " + "-" * 72)

    for det, g, err in all_close[:50]:
        n_tri = 2 * det
        bits = n_tri / 4.0
        print(f"  {det:5d}  {n_tri:9d}  {bits:5.1f}"
              f"  {g['inv_alpha']:11.4f}  {err:+8.3f}%"
              f"  ({g['n1']:+d},{g['m1']:+d})×({g['n2']:+d},{g['m2']:+d})")

    print()

    # What's special about 1/137?
    print("=" * 78)
    print("  QUESTION: At what torus size does 1/137 first appear (within X%)?")
    print("=" * 78)
    print()

    for threshold in [10.0, 5.0, 2.0, 1.0, 0.5, 0.1]:
        for det, g, err in all_close:
            if abs(err) < threshold:
                print(f"  Within {threshold:5.1f}%:  first at {det:3d} cells"
                      f"  ({2*det} triangles, {2*det/4:.1f} bits)"
                      f"  1/α = {g['inv_alpha']:.3f}  err = {err:+.3f}%")
                break
        else:
            print(f"  Within {threshold:5.1f}%:  not found in range")

    print()

    # Also look for 1/24 and 1/80
    print("=" * 78)
    print("  FIRST APPEARANCE OF OTHER LANDMARKS")
    print("=" * 78)
    print()

    for lm_name, lm_val in sorted(landmark_alpha.items()):
        print(f"  1/{lm_name}:")
        for threshold in [5.0, 1.0, 0.5]:
            for det in range(1, max_det + 1):
                entries = by_det.get(det, [])
                if not entries:
                    continue
                closest = min(entries, key=lambda e: abs(e['alpha'] - lm_val))
                err = 100 * (closest['alpha'] - lm_val) / lm_val
                if abs(err) < threshold:
                    print(f"    Within {threshold:4.1f}%: first at {det:3d} cells"
                          f"  1/α = {closest['inv_alpha']:.3f}"
                          f"  err = {err:+.3f}%")
                    break
            else:
                print(f"    Within {threshold:4.1f}%: not found")
        print()


if __name__ == "__main__":
    main()
