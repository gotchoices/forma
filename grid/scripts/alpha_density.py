#!/usr/bin/env python3
"""
Final study: α solution density on small triangular tori.

For each torus size (1 to 60 cells), compute:
  - ALL distinct α values
  - The density of solutions near key landmarks
  - The median gap between adjacent α values
  - First size that achieves each landmark within various tolerances

Goal: honest assessment of how constraining the lattice geometry is.
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
    return r**2 * mu * math.sin(2 * math.pi * s)**2 / (4 * math.pi * (2 - s)**2)


def main():
    max_det = 60
    max_n = 35

    by_det = defaultdict(set)  # det -> set of rounded (1/α) values
    by_det_raw = defaultdict(list)  # det -> list of (1/α, wrapping) for detail

    print("Scanning wrapping space...", flush=True)

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
                    adet = abs(int(round(det)))
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

                    a = alpha_ma(r, s)
                    if a <= 0 or a > 100:
                        continue

                    inv_a = 1.0 / a
                    if inv_a > 1e6:
                        continue

                    by_det[adet].add(round(inv_a, 6))
                    by_det_raw[adet].append((inv_a, n1, m1, n2, m2, r, s))

    print("Done.\n")

    landmarks = [
        ("1/24 (GUT scale)", 24.0),
        ("1/80 (high energy)", 80.0),
        ("1/128 (Z mass)", 128.0),
        ("1/137 (low energy)", 137.036),
    ]

    # ── Part 1: Solution count and density vs torus size ──

    print("=" * 80)
    print("  PART 1: HOW THE α SPECTRUM GROWS WITH TORUS SIZE")
    print("=" * 80)
    print()
    print(f"  {'cells':>5s}  {'tri':>4s}  {'bits':>5s}"
          f"  {'# distinct':>10s}  {'1/α range':>18s}"
          f"  {'med gap':>9s}  {'min gap':>9s}")
    print("  " + "─" * 72)

    for det in range(1, max_det + 1):
        vals = sorted(by_det.get(det, set()))
        if not vals:
            continue

        n_tri = 2 * det
        bits = n_tri / 4.0
        n_vals = len(vals)

        # only look at 1/α in [1, 500] for gap stats
        physical = [v for v in vals if 1.0 <= v <= 500.0]
        if len(physical) >= 2:
            gaps = [physical[i+1] - physical[i] for i in range(len(physical)-1)]
            med_gap = sorted(gaps)[len(gaps)//2]
            min_gap = min(gaps)
        else:
            med_gap = float('inf')
            min_gap = float('inf')

        range_str = f"[{vals[0]:.1f}, {vals[-1]:.1f}]"
        mg_str = f"{med_gap:.4f}" if med_gap < 1e5 else "—"
        ig_str = f"{min_gap:.6f}" if min_gap < 1e5 else "—"

        print(f"  {det:5d}  {n_tri:4d}  {bits:5.1f}"
              f"  {n_vals:10d}  {range_str:>18s}"
              f"  {mg_str:>9s}  {ig_str:>9s}")

    # ── Part 2: Density near each landmark ──

    print()
    print("=" * 80)
    print("  PART 2: SOLUTION DENSITY NEAR LANDMARKS")
    print("  (how many distinct 1/α values within ±X of each target)")
    print("=" * 80)

    windows = [0.5, 1.0, 2.0, 5.0, 10.0]

    for lm_name, lm_val in landmarks:
        print()
        print(f"  ── {lm_name}  (target 1/α = {lm_val:.3f}) ──")
        print()
        hdr = f"  {'cells':>5s}  {'tri':>4s}"
        for w in windows:
            hdr += f"  {'±' + str(w):>6s}"
        hdr += f"  {'closest':>10s}  {'error':>8s}"
        print(hdr)
        print("  " + "─" * (len(hdr) - 2))

        for det in range(1, max_det + 1):
            vals = sorted(by_det.get(det, set()))
            if not vals:
                continue

            n_tri = 2 * det

            # Count how many distinct values fall within each window
            counts = []
            for w in windows:
                n = sum(1 for v in vals if abs(v - lm_val) <= w)
                counts.append(n)

            # Closest
            closest = min(vals, key=lambda v: abs(v - lm_val))
            err = 100 * (closest - lm_val) / lm_val

            row = f"  {det:5d}  {n_tri:4d}"
            for c in counts:
                row += f"  {c:6d}"
            row += f"  {closest:10.3f}  {err:+8.3f}%"
            print(row)

    # ── Part 3: First appearance (threshold table) ──

    print()
    print("=" * 80)
    print("  PART 3: FIRST TORUS SIZE REACHING EACH LANDMARK")
    print("=" * 80)
    print()

    thresholds = [10.0, 5.0, 2.0, 1.0, 0.5, 0.1, 0.01]

    for lm_name, lm_val in landmarks:
        print(f"  {lm_name}:")
        for thr in thresholds:
            found = False
            for det in range(1, max_det + 1):
                vals = by_det.get(det, set())
                if not vals:
                    continue
                closest = min(vals, key=lambda v: abs(v - lm_val))
                err = abs(100 * (closest - lm_val) / lm_val)
                if err < thr:
                    n_tri = 2 * det
                    print(f"    < {thr:6.2f}%:  {det:3d} cells ({n_tri} tri)"
                          f"  1/α = {closest:.4f}  err = {err:.4f}%")
                    found = True
                    break
            if not found:
                print(f"    < {thr:6.2f}%:  not found")
        print()

    # ── Part 4: Nearest neighbors at the 3-cell torus ──

    print("=" * 80)
    print("  PART 4: THE 3-CELL TORUS — COMPLETE LOCAL SPECTRUM NEAR 1/137")
    print("  (all 1/α values within [100, 180] for 3-cell tori)")
    print("=" * 80)
    print()

    detail = [(inv_a, n1, m1, n2, m2, r, s)
              for inv_a, n1, m1, n2, m2, r, s in by_det_raw.get(3, [])
              if 100 < inv_a < 180]
    detail.sort()

    # deduplicate by rounded inv_a
    seen = set()
    unique_detail = []
    for row in detail:
        key = round(row[0], 4)
        if key not in seen:
            seen.add(key)
            unique_detail.append(row)

    print(f"  {len(unique_detail)} distinct values in [100, 180]")
    print()
    print(f"  {'1/α':>10s}  {'r':>6s}  {'s':>8s}  {'wrapping':>28s}  {'note':>12s}")
    print("  " + "─" * 70)

    for inv_a, n1, m1, n2, m2, r, s in unique_detail:
        note = ""
        if abs(inv_a - 137.036) / 137.036 < 0.005:
            note = "★ 1/137"
        elif abs(inv_a - 128.0) / 128.0 < 0.005:
            note = "★ 1/128"
        print(f"  {inv_a:10.4f}  {r:6.3f}  {s:+8.3f}"
              f"  ({n1:+d},{m1:+d})×({n2:+d},{m2:+d})"
              f"  {note}")

    # gap near 137
    near_137 = sorted(v for v in by_det.get(3, set())
                       if 130 < v < 145)
    if len(near_137) >= 2:
        gaps_137 = [(near_137[i+1] - near_137[i], near_137[i], near_137[i+1])
                    for i in range(len(near_137)-1)]
        print()
        print(f"  Gaps between adjacent 1/α near 137 (3-cell):")
        for gap, lo, hi in gaps_137:
            mark = " ◄ 137.036 is here" if lo < 137.036 < hi else ""
            print(f"    {lo:.4f} → {hi:.4f}  (gap = {gap:.4f}){mark}")

    # ── Part 5: Same for 9-cell torus ──

    print()
    print("=" * 80)
    print("  PART 5: THE 9-CELL TORUS — GAPS NEAR 1/137")
    print("=" * 80)
    print()

    near_137_9 = sorted(v for v in by_det.get(9, set())
                         if 133 < v < 141)
    if near_137_9:
        print(f"  {len(near_137_9)} values in [133, 141]")
        if len(near_137_9) >= 2:
            gaps = [(near_137_9[i+1] - near_137_9[i])
                    for i in range(len(near_137_9)-1)]
            print(f"  Median gap: {sorted(gaps)[len(gaps)//2]:.4f}")
            print(f"  Min gap:    {min(gaps):.6f}")
            print(f"  Max gap:    {max(gaps):.4f}")
        # Immediate neighbors of 137.036
        below = [v for v in near_137_9 if v <= 137.036]
        above = [v for v in near_137_9 if v > 137.036]
        if below and above:
            lo = max(below)
            hi = min(above)
            print(f"  Bracket around 137.036: [{lo:.4f}, {hi:.4f}]"
                  f"  width = {hi - lo:.4f}")

    # ── Part 6: Scaling law — how does gap shrink with N? ──

    print()
    print("=" * 80)
    print("  PART 6: GAP SCALING — MEDIAN GAP IN [120, 150] vs TORUS SIZE")
    print("=" * 80)
    print()
    print(f"  {'cells':>5s}  {'# vals in [120,150]':>20s}"
          f"  {'med gap':>10s}  {'min gap':>10s}")
    print("  " + "─" * 50)

    for det in range(1, max_det + 1):
        vals = sorted(v for v in by_det.get(det, set())
                      if 120 <= v <= 150)
        if len(vals) < 2:
            if len(vals) == 1:
                print(f"  {det:5d}  {len(vals):20d}  {'(single)':>10s}  {'—':>10s}")
            continue
        gaps = [vals[i+1] - vals[i] for i in range(len(vals)-1)]
        med = sorted(gaps)[len(gaps)//2]
        mn = min(gaps)
        print(f"  {det:5d}  {len(vals):20d}  {med:10.4f}  {mn:10.6f}")


if __name__ == "__main__":
    main()
