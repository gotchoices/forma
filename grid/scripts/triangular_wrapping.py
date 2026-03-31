#!/usr/bin/env python3
"""
Triangular lattice torus wrappings → MaSt geometry → α.

Enumerates integer wrapping vectors (C₁, C₂) on a 2D triangular
lattice, computes the MaSt aspect ratio r and shear s for each,
then evaluates α_ma(r, s).

The triangular lattice has basis vectors:
    a₁ = (1, 0)
    a₂ = (1/2, √3/2)
with |a₁| = |a₂| = 1 (Planck length) and angle 60°.

A torus is defined by two wrapping vectors:
    C₁ = n₁ a₁ + m₁ a₂   (tube direction)
    C₂ = n₂ a₁ + m₂ a₂   (ring direction)

The MaSt metric in angle coordinates (φ₁, φ₂) ∈ [0, 2π)² is:
    ds² = R₁²(dφ₁ + s dφ₂)² + R₂² dφ₂²

so matching to the lattice:
    R₁ = |C₁|/(2π)
    s  = C₁·C₂ / |C₁|²
    R₂ = √(|C₂|² − (C₁·C₂)²/|C₁|²) / (2π)
    r  = R₁/R₂ = |C₁| / √(|C₂|² − (C₁·C₂)²/|C₁|²)

Usage:
    python triangular_wrapping.py [--max-n 20] [--alpha-targets 137,128,80,24]
"""

import math
import argparse
from collections import defaultdict

ALPHA_MEASURED = 1.0 / 137.036


def dot_tri(n1, m1, n2, m2):
    """Dot product of two vectors on the triangular lattice.

    C₁·C₂ = a²(n₁n₂ + m₁m₂ + (n₁m₂ + m₁n₂)/2)
    Returns the coefficient (a² = 1).
    """
    return n1 * n2 + m1 * m2 + (n1 * m2 + m1 * n2) / 2.0


def norm2_tri(n, m):
    """Squared norm |C|² on the triangular lattice.

    |C|² = a²(n² + nm + m²)
    """
    return n * n + n * m + m * m


def cross_tri(n1, m1, n2, m2):
    """Signed area of parallelogram (C₁, C₂) on triangular lattice.

    Area = (√3/2) × |n₁m₂ − m₁n₂|
    Returns the integer part (n₁m₂ − m₁n₂); multiply by √3/2 for area.
    """
    return n1 * m2 - m1 * n2


def alpha_ma(r, s):
    """MaSt fine-structure constant from (r, s).

    From R19 Track 8 / studies/lib/ma.py.
    """
    if abs(s) < 1e-15 or abs(2 - s) < 1e-15:
        return 0.0
    mu = math.sqrt(1.0 / r**2 + (2.0 - s)**2)
    return r**2 * mu * math.sin(2 * math.pi * s)**2 / (4 * math.pi * (2 - s)**2)


def lattice_to_mast(n1, m1, n2, m2):
    """Convert lattice wrapping integers to MaSt (r, s).

    Returns (r, s, area_cells) or None if degenerate.
    """
    N1 = norm2_tri(n1, m1)
    N2 = norm2_tri(n2, m2)
    D = dot_tri(n1, m1, n2, m2)
    det = cross_tri(n1, m1, n2, m2)

    if N1 == 0 or N2 == 0 or det == 0:
        return None

    s = D / N1
    R2_sq = N2 - D * D / N1  # |C₂_⊥|² in lattice units

    if R2_sq <= 1e-15:
        return None

    r = math.sqrt(N1 / R2_sq)
    area_cells = abs(det)  # number of unit cells in torus (×√3/2)

    return r, s, area_cells


def canonical_key(r, s):
    """Round to avoid floating-point duplicates."""
    return (round(r, 8), round(abs(s), 8))


def main():
    parser = argparse.ArgumentParser(description="Triangular lattice wrapping → α")
    parser.add_argument("--max-n", type=int, default=12,
                        help="Max absolute value of wrapping integers")
    parser.add_argument("--alpha-targets", type=str, default="137,128,80,24",
                        help="Comma-separated 1/α targets to highlight")
    parser.add_argument("--top", type=int, default=40,
                        help="Number of closest matches to show per target")
    args = parser.parse_args()

    alpha_targets = {int(x): 1.0 / int(x) for x in args.alpha_targets.split(",")}
    max_n = args.max_n

    print(f"Enumerating triangular lattice torus wrappings with |n|,|m| ≤ {max_n}")
    print(f"Target α values: {', '.join(f'1/{k}' for k in sorted(alpha_targets))}")
    print()

    # ── Phase 1: enumerate all unique (r, s) geometries ──────────────
    seen = set()
    results = []

    for n1 in range(-max_n, max_n + 1):
        for m1 in range(-max_n, max_n + 1):
            if norm2_tri(n1, m1) == 0:
                continue
            for n2 in range(-max_n, max_n + 1):
                for m2 in range(-max_n, max_n + 1):
                    if norm2_tri(n2, m2) == 0:
                        continue

                    out = lattice_to_mast(n1, m1, n2, m2)
                    if out is None:
                        continue

                    r, s, area = out

                    # Only consider r > 0.5 (MaSt requires r > ~0.54 for charge)
                    if r < 0.5:
                        continue
                    # s must be in a range where alpha_ma works
                    if abs(s) > 0.49 or abs(s) < 1e-6:
                        continue

                    key = canonical_key(r, s)
                    if key in seen:
                        continue
                    seen.add(key)

                    a = alpha_ma(r, s)
                    if a > 0 and a < 10:  # physical range
                        results.append({
                            'n1': n1, 'm1': m1, 'n2': n2, 'm2': m2,
                            'r': r, 's': s, 'alpha': a,
                            'inv_alpha': 1.0 / a if a > 0 else float('inf'),
                            'area': area,
                        })

    print(f"Found {len(results)} unique valid (r, s) geometries")
    print()

    # ── Phase 2: find magic shear values (high symmetry) ─────────────
    print("=" * 72)
    print("MAGIC SHEAR VALUES (simplest wrappings, smallest integers)")
    print("=" * 72)

    # Sort by area (simplest tori first), then by |s|
    by_area = sorted(results, key=lambda x: (x['area'], abs(x['s'])))
    printed_shears = set()
    count = 0
    for res in by_area:
        s_key = round(res['s'], 6)
        if s_key in printed_shears:
            continue
        printed_shears.add(s_key)
        count += 1
        if count > 60:
            break
        print(f"  ({res['n1']:+d},{res['m1']:+d})×({res['n2']:+d},{res['m2']:+d})"
              f"  r={res['r']:8.4f}  s={res['s']:+9.6f}"
              f"  α={res['alpha']:.6f}  1/α={res['inv_alpha']:8.2f}"
              f"  cells={res['area']}")
    print()

    # ── Phase 3: closest matches to target α values ──────────────────
    for target_inv, target_alpha in sorted(alpha_targets.items()):
        print("=" * 72)
        print(f"CLOSEST MATCHES TO α = 1/{target_inv} = {target_alpha:.6f}")
        print("=" * 72)

        ranked = sorted(results, key=lambda x: abs(x['alpha'] - target_alpha))
        for i, res in enumerate(ranked[:args.top]):
            err_pct = 100 * (res['alpha'] - target_alpha) / target_alpha
            print(f"  #{i+1:2d}  ({res['n1']:+d},{res['m1']:+d})×({res['n2']:+d},{res['m2']:+d})"
                  f"  r={res['r']:8.4f}  s={res['s']:+9.6f}"
                  f"  α={res['alpha']:.6f}  1/α={res['inv_alpha']:8.2f}"
                  f"  err={err_pct:+.2f}%  cells={res['area']}")
        print()

    # ── Phase 4: histogram of 1/α values ─────────────────────────────
    print("=" * 72)
    print("DISTRIBUTION OF 1/α VALUES")
    print("=" * 72)

    inv_alphas = sorted(set(round(r['inv_alpha'], 1) for r in results if r['inv_alpha'] < 500))

    # Bin into ranges
    bins = [(0, 10), (10, 20), (20, 30), (30, 50), (50, 80),
            (80, 100), (100, 150), (150, 200), (200, 500)]
    for lo, hi in bins:
        count = sum(1 for ia in inv_alphas if lo <= ia < hi)
        marker = ""
        for t in alpha_targets:
            if lo <= t < hi:
                marker += f" ← 1/{t}"
        print(f"  1/α ∈ [{lo:3d}, {hi:3d}):  {count:4d} unique geometries{marker}")
    print()

    # ── Phase 5: look for periodicity in magic shears ────────────────
    print("=" * 72)
    print("SHEAR VALUES THAT PRODUCE α NEAR KNOWN LANDMARKS")
    print("=" * 72)

    landmarks = {
        '1/137 (low-E α)': 1/137.036,
        '1/128 (Z-mass α)': 1/128.0,
        '1/80': 1/80.0,
        '1/24': 1/24.0,
    }

    for name, target in landmarks.items():
        matches = [r for r in results if abs(r['alpha'] - target) / target < 0.02]
        if matches:
            shears = sorted(set(round(m['s'], 6) for m in matches))
            print(f"\n  {name}: {len(matches)} wrappings within 2%")
            print(f"    Shear values: {shears[:20]}")
            # Check for periodicity
            if len(shears) > 2:
                diffs = [shears[i+1] - shears[i] for i in range(len(shears)-1)]
                if diffs:
                    print(f"    Shear spacings: {[round(d, 6) for d in diffs[:15]]}")
        else:
            print(f"\n  {name}: no wrappings within 2%")

    print()
    print("Done.")


if __name__ == "__main__":
    main()
