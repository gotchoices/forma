#!/usr/bin/env python3
"""
R26 Track 1b: All-spin-½ triplet search.

Systematic search over (p₁,2), (p₂,2), (p₃,2) mode triplets with all pᵢ
odd (ensuring spin-½ fermion) for (s, r) values that reproduce the
experimental mass-squared ratio Δm²₃₁/Δm²₂₁ = 33.6 ± 0.9.

Extended to p ≤ 25 (S3-knot-zoo stopped at p = 10).

For each valid triplet:
  - Solve for the (s, r) curve giving the target ratio
  - Count intermediate spin-½ fermion modes between ν₂ and ν₃
  - Compute Σm and check against cosmological bound
  - Assess N_eff viability

ENERGY FORMULA
==============
  μ²(p, 2) = (p/r)² + (2 − p·s)²

  Δμ²₂₁ = (p₂² − p₁²)/r² + (2 − p₂s)² − (2 − p₁s)²
  Δμ²₃₁ = (p₃² − p₁²)/r² + (2 − p₃s)² − (2 − p₁s)²

  Ratio R = Δμ²₃₁ / Δμ²₂₁

For fixed (p₁, p₂, p₃), R depends on both s and r.  We scan (s, r)
parameter space for each triplet.
"""

import sys
import os
import math
from itertools import combinations

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, c

eV_to_J = 1.602176634e-19
hc_eVm = h * c / eV_to_J

# Experimental neutrino parameters
DM2_21 = 7.53e-5    # eV²
DM2_32 = 2.455e-3   # eV²
DM2_31 = DM2_32 + DM2_21
TARGET_RATIO = DM2_31 / DM2_21
RATIO_TOL = 0.9  # ±0.9 (generous, ~3σ)
COSMO_BOUND = 0.120  # eV


def mu_sq(p, q, s, r):
    """Dimensionless mass-squared for mode (p, q) on sheared material sheet."""
    return (p / r)**2 + (q - p * s)**2


def dm2_ratio(p1, p2, p3, s, r):
    """Δm²₃₁/Δm²₂₁ for triplet (p₁,2), (p₂,2), (p₃,2)."""
    m1sq = mu_sq(p1, 2, s, r)
    m2sq = mu_sq(p2, 2, s, r)
    m3sq = mu_sq(p3, 2, s, r)
    denom = m2sq - m1sq
    if abs(denom) < 1e-20:
        return None
    return (m3sq - m1sq) / denom


def find_sr_for_ratio(p1, p2, p3, target, s_range=(-0.5, 0.5),
                      r_range=(0.1, 10.0), n_s=2000, n_r=500):
    """
    Scan (s, r) space for solutions where the ratio matches target.
    Returns list of (s, r, ratio, deviation) for matches within RATIO_TOL.
    """
    solutions = []
    best = None
    best_dev = 1e10

    s_vals = [s_range[0] + i * (s_range[1] - s_range[0]) / n_s
              for i in range(n_s + 1)]
    r_vals = [r_range[0] + i * (r_range[1] - r_range[0]) / n_r
              for i in range(1, n_r + 1)]

    for r in r_vals:
        for s in s_vals:
            rat = dm2_ratio(p1, p2, p3, s, r)
            if rat is None or rat < 0:
                continue

            # Check ordering: must have m₁ < m₂ < m₃
            m1 = mu_sq(p1, 2, s, r)
            m2 = mu_sq(p2, 2, s, r)
            m3 = mu_sq(p3, 2, s, r)
            if not (m1 < m2 < m3):
                continue

            dev = abs(rat - target)
            if dev < best_dev:
                best_dev = dev
                best = (s, r, rat, dev)

    if best is None:
        return None

    # Refine around best
    s0, r0 = best[0], best[1]
    ds = (s_range[1] - s_range[0]) / n_s
    dr = (r_range[1] - r_range[0]) / n_r
    for r in [r0 + i * dr / 20 for i in range(-20, 21)]:
        if r <= 0:
            continue
        for s in [s0 + i * ds / 20 for i in range(-20, 21)]:
            rat = dm2_ratio(p1, p2, p3, s, r)
            if rat is None or rat < 0:
                continue
            m1 = mu_sq(p1, 2, s, r)
            m2 = mu_sq(p2, 2, s, r)
            m3 = mu_sq(p3, 2, s, r)
            if not (m1 < m2 < m3):
                continue
            dev = abs(rat - target)
            if dev < best_dev:
                best_dev = dev
                best = (s, r, rat, dev)

    return best


def count_intermediate_spin_half(p1, p2, p3, s, r, p_max=30):
    """
    Count spin-½ fermion modes between m₂ and m₃.

    Spin-½ fermion = (p_odd, ±2).  For each odd |p|, four modes exist:
    (+p,+2), (-p,+2), (+p,-2), (-p,-2).
    """
    m2sq = mu_sq(p2, 2, s, r)
    m3sq = mu_sq(p3, 2, s, r)

    count = 0
    modes = []
    for p in range(-p_max, p_max + 1):
        if p == 0 or p % 2 == 0:
            continue
        for q_sign in [2, -2]:
            msq = mu_sq(p, q_sign, s, r)
            if m2sq < msq < m3sq:
                # Exclude the actual triplet modes
                if (abs(p) == abs(p1) or abs(p) == abs(p2) or abs(p) == abs(p3)) and abs(q_sign) == 2:
                    # Check if this IS one of the triplet modes
                    if (p == p1 or p == p2 or p == p3) and q_sign == 2:
                        continue
                count += 1
                modes.append((p, q_sign, math.sqrt(msq)))
    return count, modes


def compute_physical_masses(p1, p2, p3, s, r):
    """Compute physical masses by matching Δm²₂₁ to experiment."""
    m1sq = mu_sq(p1, 2, s, r)
    m2sq = mu_sq(p2, 2, s, r)
    m3sq = mu_sq(p3, 2, s, r)

    dmu21 = m2sq - m1sq
    if dmu21 <= 0:
        return None

    E0_sq = DM2_21 / dmu21
    E0 = math.sqrt(E0_sq)

    m1 = E0 * math.sqrt(m1sq)
    m2 = E0 * math.sqrt(m2sq)
    m3 = E0 * math.sqrt(m3sq)

    return E0, m1, m2, m3


def main():
    print("=" * 76)
    print("R26 Track 1b: All-Spin-½ Triplet Search")
    print("=" * 76)

    # Generate all odd p values from 1 to 25
    odd_p = [p for p in range(1, 26) if p % 2 != 0]
    print(f"\n  Odd p values: {odd_p}")
    print(f"  Total: {len(odd_p)} values")

    # Generate all ordered triplets (p₁ < p₂ < p₃), all odd
    triplets = list(combinations(odd_p, 3))
    print(f"  Triplets to test: {len(triplets)}")
    print(f"  Target ratio: {TARGET_RATIO:.4f} ± {RATIO_TOL:.1f}")

    # ================================================================
    # SECTION 1: Scan all triplets
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 1: Scan all triplets for ratio match")
    print("=" * 76)

    results = []
    for i, (p1, p2, p3) in enumerate(triplets):
        if (i + 1) % 100 == 0:
            print(f"  Scanning triplet {i+1}/{len(triplets)}...", flush=True)

        best = find_sr_for_ratio(p1, p2, p3, TARGET_RATIO)
        if best is None:
            continue

        s, r, ratio, dev = best
        if dev > RATIO_TOL:
            continue

        n_sterile, sterile_modes = count_intermediate_spin_half(p1, p2, p3, s, r)
        phys = compute_physical_masses(p1, p2, p3, s, r)
        if phys is None:
            continue

        E0, m1, m2, m3 = phys
        sum_m = m1 + m2 + m3

        results.append({
            'triplet': (p1, p2, p3),
            's': s, 'r': r,
            'ratio': ratio, 'dev': dev,
            'n_sterile': n_sterile,
            'E0': E0, 'm1': m1, 'm2': m2, 'm3': m3,
            'sum_m': sum_m,
            'cosmo_ok': sum_m < COSMO_BOUND,
        })

    print(f"\n  Triplets with ratio match: {len(results)}")

    # ================================================================
    # SECTION 2: Results table (sorted by sterile count)
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 2: Results (sorted by sterile neutrino count)")
    print("=" * 76)

    results.sort(key=lambda x: (x['n_sterile'], x['dev']))

    print(f"\n  {'Triplet':>16s}  {'s':>8s}  {'r':>7s}  {'ratio':>8s}  "
          f"{'N_ster':>6s}  {'Σm(meV)':>8s}  {'Cosmo':>5s}")
    print(f"  {'—'*16}  {'—'*8}  {'—'*7}  {'—'*8}  "
          f"{'—'*6}  {'—'*8}  {'—'*5}")

    for res in results:
        p1, p2, p3 = res['triplet']
        cosmo = "✓" if res['cosmo_ok'] else "✗"
        print(f"  ({p1:2d},{p2:2d},{p3:2d})  {res['s']:8.4f}  {res['r']:7.3f}  "
              f"{res['ratio']:8.4f}  {res['n_sterile']:6d}  "
              f"{res['sum_m']*1e3:8.1f}  {cosmo:>5s}")

    # ================================================================
    # SECTION 3: Analysis of best candidates
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 3: Analysis of best candidates")
    print("=" * 76)

    # Best = fewest sterile neutrinos that pass cosmology
    viable = [r for r in results if r['cosmo_ok']]
    if not viable:
        viable = results  # Fall back to all if none pass cosmology

    # Show top 5 by sterile count
    for rank, res in enumerate(viable[:5]):
        p1, p2, p3 = res['triplet']
        print(f"\n  --- Rank {rank+1}: ({p1}, {p2}, {p3}) ---")
        print(f"  s = {res['s']:.5f},  r = {res['r']:.4f}")
        print(f"  Ratio = {res['ratio']:.4f}  (deviation: {res['dev']:.4f})")
        print(f"  m₁ = {res['m1']*1e3:.2f} meV  (p={p1}, q=2)")
        print(f"  m₂ = {res['m2']*1e3:.2f} meV  (p={p2}, q=2)")
        print(f"  m₃ = {res['m3']*1e3:.2f} meV  (p={p3}, q=2)")
        print(f"  Σm = {res['sum_m']*1e3:.1f} meV  "
              f"{'✓' if res['cosmo_ok'] else '✗'} (bound: 120 meV)")
        print(f"  E₀ = {res['E0']*1e3:.2f} meV")
        L4 = hc_eVm / res['E0']
        print(f"  L₄ = {L4*1e6:.1f} μm")
        print(f"  Sterile spin-½ fermions between ν₂ and ν₃: {res['n_sterile']}")

        # Detailed sterile mode listing
        n_st, st_modes = count_intermediate_spin_half(p1, p2, p3,
                                                      res['s'], res['r'])
        if st_modes:
            # Group by |p|
            p_vals = sorted(set(abs(p) for p, q, m in st_modes))
            print(f"  Sterile |p| values: {p_vals}")

    # ================================================================
    # SECTION 4: Is there a clean solution?
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 4: Clean solution assessment")
    print("=" * 76)

    clean = [r for r in results if r['n_sterile'] == 0 and r['cosmo_ok']]
    if clean:
        print(f"\n  ✓ Found {len(clean)} triplet(s) with ZERO sterile neutrinos"
              " and Σm < 120 meV!")
        for res in clean:
            p1, p2, p3 = res['triplet']
            print(f"    ({p1}, {p2}, {p3}): s={res['s']:.5f}, r={res['r']:.4f}, "
                  f"ratio={res['ratio']:.4f}, Σm={res['sum_m']*1e3:.1f} meV")
    else:
        print("\n  ✗ No triplet found with zero sterile neutrinos and Σm < 120 meV.")

        min_sterile = min(r['n_sterile'] for r in results) if results else None
        if min_sterile is not None:
            best_sterile = [r for r in results if r['n_sterile'] == min_sterile]
            print(f"\n  Minimum sterile count: {min_sterile}")
            print(f"  Triplets achieving this:")
            for res in best_sterile[:5]:
                p1, p2, p3 = res['triplet']
                cosmo = "✓" if res['cosmo_ok'] else "✗"
                print(f"    ({p1}, {p2}, {p3}): s={res['s']:.5f}, r={res['r']:.4f}, "
                      f"Σm={res['sum_m']*1e3:.1f} meV {cosmo}")

    # ================================================================
    # SECTION 5: Scaling law — why sterile count grows with p₃
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 5: Sterile count scaling")
    print("=" * 76)

    print("\n  For triplets with p₁ = 1:")
    p1_is_1 = [r for r in results if r['triplet'][0] == 1]
    p1_is_1.sort(key=lambda x: x['triplet'][2])
    if p1_is_1:
        print(f"\n  {'(p₁,p₂,p₃)':>16s}  {'N_sterile':>9s}  {'p₃':>4s}  "
              f"{'Ratio':>6s}")
        for res in p1_is_1[:15]:
            p1, p2, p3 = res['triplet']
            print(f"  ({p1:2d},{p2:2d},{p3:2d})  {res['n_sterile']:9d}  "
                  f"{p3:4d}  {res['n_sterile']/max(p3-p2,1):6.1f}/gap")

    print("\n  The sterile count scales roughly as 4 × (number of odd integers")
    print("  between p₂ and p₃).  For p₃ = 17 and p₂ = 3, that's")
    print("  4 × |{5,7,9,11,13,15}| = 24, plus boundary modes ≈ 26.")
    print("  Minimizing p₃ − p₂ minimizes sterile neutrinos, but the")
    print("  ratio constraint requires p₃²/p₂² ≈ 33.6, forcing large p₃.")

    # ================================================================
    # SECTION 6: Summary
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 6: Summary")
    print("=" * 76)

    print(f"\n  Triplets tested: {len(triplets)}")
    print(f"  Matches (ratio within ±{RATIO_TOL}): {len(results)}")
    print(f"  Pass cosmological bound: {sum(1 for r in results if r['cosmo_ok'])}")
    if results:
        print(f"  Minimum sterile count: {min(r['n_sterile'] for r in results)}")
        print(f"  Minimum sterile (cosmo OK): "
              f"{min((r['n_sterile'] for r in results if r['cosmo_ok']), default='N/A')}")

    print("\n  CONCLUSION:")
    if clean:
        print("  Clean solutions exist — Track 1b succeeds.")
    else:
        print("  No clean (zero-sterile, cosmo-OK) solution exists among")
        print(f"  all-odd (p,2) triplets with p ≤ 25.")
        print("  The sterile neutrino problem is structural: the ratio ≈ 33.6")
        print("  requires p₃/p₁ ≈ √33.6 ≈ 5.8, forcing many intermediate")
        print("  odd-p modes.  This cannot be solved within Assignment B.")
        print("  → Proceed to Tracks 1c–1f for alternative mode menus.")


if __name__ == "__main__":
    main()
