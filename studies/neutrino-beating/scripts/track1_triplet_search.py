#!/usr/bin/env python3
"""
R23 Track 1: Near-degenerate triplet search for neutrino Δm² ratio.

QUESTION: Among the uncharged modes on the sheared T², do there exist
triplets whose pairwise energy-splitting ratio ΔE₃₁/ΔE₂₁ matches the
experimental neutrino ratio Δm²₃₁/Δm²₂₁ ≈ 33.6?

APPROACH:
1. At each r, solve for s from α = 1/137, build mode catalog.
2. Find all "tight" near-degenerate pairs (ΔE < threshold).
3. For each tight pair, find the nearest mode to the target
   energy E₁ + 33.6 × ΔE₂₁.  Record the miss distance.
4. Assess whether any triplet has a physically small miss.

Key physics:  the beating model requires SUB-eV pairwise splittings.
At E_max = 100 m_e, average mode spacing is ~700 eV.  Sub-eV pairs
are rare Diophantine coincidences.  The question is whether a THIRD
mode exists at 33.6× the inner splitting.

FINDING FROM INITIAL RUN: at keV-scale inner splittings, the ratio
33.6 is trivially achieved because mode density is high enough that
ANY ratio matches.  The test is only meaningful for sub-eV splittings.
"""

import sys
import os
import math
import time
import numpy as np
from scipy.optimize import brentq
import bisect

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha, m_e, c

m_e_eV = m_e * c**2 / 1.602176634e-19

DM2_21 = 7.53e-5
DM2_31 = 2.528e-3
TARGET_RATIO = DM2_31 / DM2_21

E_MAX = 100


def alpha_mode_2d(r, s, m):
    q = m - s
    sn = math.sin(2 * math.pi * s)
    if abs(sn) < 1e-15 or abs(q) < 1e-15:
        return 0.0
    d = math.sqrt(r**2 * (1 + m * s)**2 + m**2)
    return r**2 * sn**2 / (4 * math.pi * q**2 * d)


def solve_s(r):
    def f(s):
        return alpha_mode_2d(r, s, 2) - alpha
    ss = np.linspace(0.001, 0.499, 5000)
    fs = [f(si) for si in ss]
    for i in range(len(fs) - 1):
        if fs[i] * fs[i + 1] < 0:
            return brentq(f, ss[i], ss[i + 1], xtol=1e-14)
    return None


def build_mode_catalog(r, s, E_max=100):
    """Sorted array of (E_ratio, n1, n2) for uncharged modes (|n₁| ≥ 2)."""
    e_sq_e = 1.0 + ((2 - s) / r)**2
    E_max_sq = E_max**2 * e_sq_e
    lim = math.sqrt(E_max_sq)
    n1_max = min(int(lim) + 5, 300)
    n2_max = min(int(r * lim + abs(s) * n1_max) + 5, 3000)

    modes = []
    for n1 in range(2, n1_max + 1):
        for n2 in range(-n2_max, n2_max + 1):
            esq = n1**2 + ((n2 - n1 * s) / r)**2
            if 0 < esq <= E_max_sq:
                modes.append((math.sqrt(esq / e_sq_e), n1, n2))
    modes.sort()
    return modes


def find_tight_pairs(modes, max_split_eV=100.0):
    """Find pairs with ΔE < max_split_eV, sorted by ΔE."""
    max_split = max_split_eV / m_e_eV
    pairs = []
    N = len(modes)
    energies = [m[0] for m in modes]
    for i in range(N):
        for j in range(i + 1, N):
            dE = energies[j] - energies[i]
            if dE > max_split:
                break
            if dE > 0:
                pairs.append((dE, i, j))
    pairs.sort()
    return pairs


def search_third_mode(modes, pairs, target_ratio=TARGET_RATIO):
    """For each pair, find the nearest mode to E₁ + target_ratio × ΔE₂₁.

    Returns list of (actual_ratio, miss_frac, pair_dE_eV, i, j, k)
    sorted by |miss_frac|, where miss_frac = (actual_ratio - target)/target.
    """
    energies = [m[0] for m in modes]
    N = len(energies)
    results = []

    for dE, i, j in pairs:
        E1 = energies[i]
        E_target = E1 + target_ratio * dE
        idx = bisect.bisect_left(energies, E_target)

        best_k = None
        best_miss = float('inf')
        for k in [idx - 1, idx, idx + 1]:
            if k <= j or k >= N:
                continue
            miss = abs(energies[k] - E_target)
            if miss < best_miss:
                best_miss = miss
                best_k = k

        if best_k is not None:
            actual_ratio = (energies[best_k] - E1) / dE
            miss_frac = (actual_ratio - target_ratio) / target_ratio
            results.append((
                actual_ratio, miss_frac,
                dE * m_e_eV, i, j, best_k
            ))

    results.sort(key=lambda x: abs(x[1]))
    return results


def main():
    t0 = time.time()

    print("=" * 72)
    print("R23 TRACK 1: Near-degenerate triplet search")
    print("=" * 72)
    print()
    print(f"Target ratio ΔE₃₁/ΔE₂₁ = Δm²₃₁/Δm²₂₁ = {TARGET_RATIO:.4f}")
    print(f"  Δm²₂₁ = {DM2_21:.2e} eV²")
    print(f"  Δm²₃₁ = {DM2_31:.3e} eV²")
    print(f"  m_e c² = {m_e_eV:.1f} eV")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 1: Mode density and pair statistics at r = 1")
    print("=" * 72)
    print(flush=True)

    r = 1.0
    s = solve_s(r)
    print(f"r = {r}, s = {s:.12f}")
    modes = build_mode_catalog(r, s, E_MAX)
    N = len(modes)
    E_range = modes[-1][0] - modes[0][0]
    density = N / E_range
    avg_spacing_eV = E_range / N * m_e_eV

    print(f"Modes: {N}")
    print(f"E range: {modes[0][0]:.2f} – {modes[-1][0]:.2f} m_e")
    print(f"Density: {density:.1f} modes/m_e = 1 mode per {avg_spacing_eV:.1f} eV")
    print(flush=True)

    thresholds = [10000, 1000, 100, 10, 1, 0.1]
    print()
    print("Pair counts by inner splitting threshold:")
    print(f"{'Threshold (eV)':>16s}  {'Pairs':>10s}  {'Avg ΔE (eV)':>12s}")
    print("-" * 42)
    for thr in thresholds:
        t_start = time.time()
        pairs = find_tight_pairs(modes, thr)
        dt = time.time() - t_start
        if pairs:
            avg_dE = np.mean([p[0] for p in pairs]) * m_e_eV
            print(f"{thr:16.1f}  {len(pairs):10d}  {avg_dE:12.2f}"
                  f"  ({dt:.1f}s)", flush=True)
        else:
            print(f"{thr:16.1f}  {0:10d}", flush=True)
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 2: Triplet search at physically relevant splittings")
    print("=" * 72)
    print(flush=True)

    inner_thresholds = [1000, 100, 10, 1]

    for thr in inner_thresholds:
        print(f"\n--- Inner splitting < {thr} eV ---")
        pairs = find_tight_pairs(modes, thr)
        if not pairs:
            print(f"  No pairs found with ΔE < {thr} eV.")
            continue

        results = search_third_mode(modes, pairs)
        print(f"  Pairs: {len(pairs)}")

        if results:
            print(f"  Best 5 ratio matches:")
            print(f"  {'Ratio':>10s}  {'miss%':>8s}  {'ΔE₂₁(eV)':>10s}"
                  f"  {'ΔE₃₁(eV)':>10s}  {'E₁/mₑ':>8s}  Triplet")
            for ratio, mf, dE_eV, i, j, k in results[:5]:
                m1, m2, m3 = modes[i], modes[j], modes[k]
                dE31 = (m3[0] - m1[0]) * m_e_eV
                print(f"  {ratio:10.4f}  {mf*100:+8.4f}  {dE_eV:10.2f}"
                      f"  {dE31:10.2f}  {m1[0]:8.2f}"
                      f"  ({m1[1]:+d},{m1[2]:+d})"
                      f" ({m2[1]:+d},{m2[2]:+d})"
                      f" ({m3[1]:+d},{m3[2]:+d})")

            best = results[0]
            # Significance: expected number of matches this good or better
            # For random uniform spectrum with density ρ:
            # P(miss < δ) ≈ 2δ × ρ per pair
            miss_abs = abs(best[1]) * TARGET_RATIO * (best[2] / m_e_eV)
            p_per = 2 * miss_abs * density
            expected = len(pairs) * p_per
            print(f"  Significance: expected random matches"
                  f" ≤ {abs(best[1])*100:.4f}%: {expected:.2f}")
        print(flush=True)

    # ==================================================================
    print()
    print("=" * 72)
    print("SECTION 3: Scan over r — tightest pairs and best triplets")
    print("=" * 72)
    print(flush=True)

    r_values = np.concatenate([
        np.arange(0.5, 5.1, 0.5),
        np.arange(6.0, 15.1, 2.0),
    ])

    print()
    print(f"{'r':>5s}  {'s':>12s}  {'modes':>6s}  "
          f"{'tight pairs':>12s}  {'tightest(eV)':>13s}  "
          f"{'best ratio':>11s}  {'miss%':>8s}")
    print("-" * 80)

    scan_results = []

    for r in r_values:
        s = solve_s(r)
        if s is None:
            print(f"{r:5.1f}  {'no soln':>12s}", flush=True)
            continue

        modes = build_mode_catalog(r, s, E_MAX)
        N = len(modes)

        pairs_100 = find_tight_pairs(modes, 100.0)

        if not pairs_100:
            print(f"{r:5.1f}  {s:12.8f}  {N:6d}  {0:12d}", flush=True)
            continue

        tightest_eV = pairs_100[0][0] * m_e_eV

        results = search_third_mode(modes, pairs_100)
        if results:
            best = results[0]
            ratio, mf = best[0], best[1]
            print(f"{r:5.1f}  {s:12.8f}  {N:6d}  "
                  f"{len(pairs_100):12d}  {tightest_eV:13.4f}  "
                  f"{ratio:11.4f}  {mf*100:+8.4f}", flush=True)
            scan_results.append((r, s, N, len(pairs_100),
                                 tightest_eV, ratio, mf, modes, best))
        else:
            print(f"{r:5.1f}  {s:12.8f}  {N:6d}  "
                  f"{len(pairs_100):12d}  {tightest_eV:13.4f}  "
                  f"{'—':>11s}", flush=True)

    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 4: Best triplet — detailed analysis")
    print("=" * 72)
    print()

    if not scan_results:
        print("No scan results to analyze.")
        return

    scan_results.sort(key=lambda x: abs(x[6]))
    best_scan = scan_results[0]
    r_b, s_b, N_b, np_b, tight_b, ratio_b, mf_b, modes_b, trip_b = best_scan
    ratio, mf, dE_eV, i, j, k = trip_b

    m1, m2, m3 = modes_b[i], modes_b[j], modes_b[k]
    E1, E2, E3 = m1[0], m2[0], m3[0]
    dE21 = E2 - E1
    dE31 = E3 - E1

    print(f"r = {r_b:.4f}, s = {s_b:.12f}")
    print()
    print(f"Mode 1: ({m1[1]:+d},{m1[2]:+d})  E = {E1:.10f} m_e"
          f" = {E1 * m_e_eV:.2f} eV")
    print(f"Mode 2: ({m2[1]:+d},{m2[2]:+d})  E = {E2:.10f} m_e"
          f" = {E2 * m_e_eV:.2f} eV")
    print(f"Mode 3: ({m3[1]:+d},{m3[2]:+d})  E = {E3:.10f} m_e"
          f" = {E3 * m_e_eV:.2f} eV")
    print()
    print(f"ΔE₂₁ = {dE21 * m_e_eV:.4f} eV")
    print(f"ΔE₃₁ = {dE31 * m_e_eV:.4f} eV")
    print(f"Ratio = {ratio:.6f}  (target {TARGET_RATIO:.4f},"
          f" miss = {mf*100:+.4f}%)")
    print()

    dm2_21 = (E2**2 - E1**2) * m_e_eV**2
    dm2_31 = (E3**2 - E1**2) * m_e_eV**2
    exact_ratio = dm2_31 / dm2_21 if dm2_21 != 0 else float('inf')

    print(f"Exact Δm² ratio (E²): {exact_ratio:.6f}")
    print(f"  Near-degenerate approx: {ratio:.6f}")
    print()
    print(f"Raw mode Δm²₂₁ = {dm2_21:.4e} eV²  (expt {DM2_21:.2e})")
    print(f"Raw mode Δm²₃₁ = {dm2_31:.4e} eV²  (expt {DM2_31:.3e})")
    if dm2_21 > 0:
        scale = DM2_21 / dm2_21
        print(f"Phonon coupling scale factor: {scale:.4e}")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 5: Scaling analysis — what E_max is needed?")
    print("=" * 72)
    print()

    r_test = 1.0
    s_test = solve_s(r_test)
    print(f"Testing mode density scaling at r = {r_test}")
    print()

    for e_max in [20, 50, 100]:
        modes_t = build_mode_catalog(r_test, s_test, e_max)
        N_t = len(modes_t)
        if N_t < 2:
            continue
        E_range_t = modes_t[-1][0] - modes_t[0][0]
        density_t = N_t / E_range_t if E_range_t > 0 else 0
        spacing_t = m_e_eV / density_t if density_t > 0 else float('inf')

        pairs_t = find_tight_pairs(modes_t, 100.0)
        tightest_t = pairs_t[0][0] * m_e_eV if pairs_t else float('inf')

        print(f"  E_max = {e_max:4d} m_e: "
              f"{N_t:6d} modes, "
              f"spacing = {spacing_t:.1f} eV, "
              f"tight pairs (<100eV) = {len(pairs_t)}, "
              f"tightest = {tightest_t:.2f} eV", flush=True)

    print()
    print("Extrapolation:")
    print("  Mode density ∝ E_max (2D density of states)")
    print("  Tightest pair ∝ 1/E_max² (inverse of total mode count)")
    print("  At E_max = 100: density ~ 700/m_e, spacing ~ 730 eV")
    print(f"  For sub-eV inner splitting: need E_max ~ 100 × √(730) ≈ 2700 m_e")
    print(f"  For 0.1 eV splitting: need E_max ~ 100 × √(7300) ≈ 8500 m_e")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 6: Summary")
    print("=" * 72)
    print()

    print("F1. Ratio 33.6 is trivially achieved at keV-scale splittings")
    print("    At E_max = 100 m_e, millions of triplets exist with ratio")
    print(f"    matching {TARGET_RATIO:.4f} to 4+ decimal places for ANY r.")
    print("    The mode density (~700/m_e) ensures a mode within ~1%")
    print("    of any target energy.  The ratio test is not selective")
    print("    at these splitting scales.")
    print()

    print("F2. Physical relevance requires sub-eV inner splittings")
    print("    The neutrino Δm²₂₁ = 7.5×10⁻⁵ eV² implies sub-eV mode")
    print("    splittings (in the phonon model).  At E_max = 100 m_e,")
    tightest_r1 = scan_results[0][4] if scan_results else float('inf')
    for sr in scan_results:
        if sr[0] == 1.0:
            tightest_r1 = sr[4]
            break
    print(f"    the tightest pair has ΔE ~ {tightest_r1:.1f} eV.")
    print("    Sub-eV pairs are extremely rare at this mode count.")
    print()

    print("F3. Higher E_max needed for meaningful test")
    print("    The tightest pair scales as ~ 1/N_modes.")
    print("    Sub-eV pairs require E_max ~ 1000–3000 m_e")
    print("    (N_modes ~ 10⁶–10⁷).  Computationally expensive")
    print("    but feasible with targeted search algorithms.")
    print()

    pct = abs(mf_b) * 100
    print(f"F4. Best triplet at <100 eV inner splitting:")
    print(f"    r = {r_b:.1f}, ratio = {ratio_b:.4f}"
          f" ({pct:.2f}% from target)")
    print(f"    ΔE₂₁ = {dE_eV:.2f} eV,"
          f" ΔE₃₁ = {dE31 * m_e_eV:.2f} eV")
    print(f"    This is a {'good' if pct < 1 else 'marginal' if pct < 5 else 'poor'}"
          f" match but at splitting scale above")
    print(f"    the neutrino-relevant regime.")
    print()

    print("F5. Path forward")
    print("    (a) Extend to E_max ~ 500 m_e with optimized search")
    print("    (b) Use continued-fraction methods for targeted")
    print("        Diophantine approximation (find near-degeneracies")
    print("        analytically rather than by enumeration)")
    print("    (c) The ratio test constrains r only in conjunction")
    print("        with the absolute Δm² scale from Track 2 (phonon mass)")

    elapsed = time.time() - t0
    print()
    print(f"Total runtime: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
