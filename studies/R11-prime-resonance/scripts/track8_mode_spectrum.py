#!/usr/bin/env python3
"""
R11 Track 8: Mode spectrum and degeneracy on the sheared T².

The sheared T² is flat, so the Helmholtz equation has exact
plane-wave solutions with modified boundary conditions.

Mode frequencies (in units of c/R, with R = 1):

    ω(n,m) = √(n²/r² + (m − n/(2q))²)

where (n,m) are integers, r = a/R, and the shear δ = πa/q
enters through the −n/(2q) offset in the m-direction.

We compute:
  (a) The full mode spectrum for each q
  (b) Near-degeneracy pair counts
  (c) Spectral gap statistics
  (d) Mode density at the Compton-relevant frequency
  (e) Whether any of these differ for prime vs composite q

Key physical setup:
  - The Compton mode is NOT a single torus eigenmode (ω_C is
    far below the lowest mode).  It's a wave packet whose
    envelope oscillates at ω_C as the photon orbits q times.
  - The torus modes relevant to the electron are those whose
    BEAT frequencies match the Compton frequency or its
    harmonics.
  - For composite q, divisor-frequency beats could provide
    additional resonant channels.
"""

import sys
import os
import math
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha


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


def divisors(q):
    """Non-trivial divisors of q (exclude 1 and q)."""
    return [d for d in range(2, q) if q % d == 0]


def r_approx(q):
    """Approximate r = a/R from R8 solution curve."""
    return 0.0025 * (q - 100) + 0.10


def compute_mode_spectrum(q, r, omega_max):
    """
    Compute all mode frequencies on the sheared T².

    ω(n,m) = √(n²/r² + (m − n/(2q))²)

    Returns sorted list of (ω, n, m) tuples.
    """
    inv_r2 = 1.0 / (r * r)
    shift = 1.0 / (2.0 * q)
    modes = []

    # n range: |n|/r < omega_max → |n| < omega_max * r
    n_max = int(omega_max * r) + 1
    # m range: |m - n/(2q)| < omega_max → m in [n/(2q) - omega_max, ...]
    for n in range(-n_max, n_max + 1):
        m_center = n * shift
        m_lo = int(math.floor(m_center - omega_max)) - 1
        m_hi = int(math.ceil(m_center + omega_max)) + 1
        n2_term = n * n * inv_r2
        for m in range(m_lo, m_hi + 1):
            phi_term = m - n * shift
            omega2 = n2_term + phi_term * phi_term
            if omega2 > 0 and omega2 <= omega_max * omega_max:
                modes.append((math.sqrt(omega2), n, m))

    modes.sort(key=lambda x: x[0])
    return modes


def pair_count(freqs, epsilon):
    """Count pairs of modes with |ω_i - ω_j| < epsilon."""
    count = 0
    N = len(freqs)
    for i in range(N):
        for j in range(i + 1, N):
            if freqs[j] - freqs[i] >= epsilon:
                break
            count += 1
    return count


def gap_statistics(freqs, omega_lo, omega_hi):
    """
    Compute gap statistics for modes in [omega_lo, omega_hi].
    Returns: (mean_gap, std_gap, min_gap, n_modes)
    """
    band = [f for f in freqs if omega_lo <= f <= omega_hi]
    if len(band) < 2:
        return (0, 0, 0, len(band))
    gaps = [band[i+1] - band[i] for i in range(len(band) - 1)]
    mean_g = sum(gaps) / len(gaps)
    var_g = sum((g - mean_g)**2 for g in gaps) / len(gaps)
    return (mean_g, math.sqrt(var_g), min(gaps), len(band))


def beat_frequency_test(modes, q, r, epsilon):
    """
    For composite q with divisor d, the orbit sub-period is
    q/d orbits.  The corresponding beat frequency (difference
    between nearby modes that would resonate at this sub-period)
    is:
        Δω_d = 2π d / T_Compton ∝ d

    In torus mode units, the orbit frequency is:
        ω_orbit ≈ 1/R = 1  (one orbit per 2πR of φ-travel)

    The Compton frequency is ω_C = ω_orbit / q ≈ 1/q.
    The d-th harmonic beat frequency is d × ω_C = d/q.

    Count mode pairs with |ω_i - ω_j| ≈ d/q (within ε).
    Compare this count for divisor d-values vs non-divisor values.
    """
    freqs = [m[0] for m in modes]
    divs = divisors(q)
    results = {}

    # Test a range of beat frequencies: d/q for d = 1, 2, ..., 20
    for d in range(1, 21):
        target_delta = float(d) / q
        count = 0
        N = len(freqs)
        for i in range(N):
            for j in range(i + 1, N):
                diff = freqs[j] - freqs[i]
                if diff > target_delta + epsilon:
                    break
                if abs(diff - target_delta) < epsilon:
                    count += 1

        is_div = d in divs or (q % d == 0 and d > 1 and d < q)
        results[d] = {'count': count, 'is_divisor': is_div}

    return results


def main():
    t_start = time.time()
    print("R11 Track 8: Mode Spectrum on the Sheared T²")
    print("=" * 72)
    print()

    q_values = sorted(set([
        # Primes near 137
        113, 127, 131, 137, 139, 149, 151,
        # Composites near 137
        121, 125, 129, 133, 135, 141, 143, 145, 147, 153,
        # Highly composite
        105, 165,
    ]))

    omega_max = 30.0

    # ════════════════════════════════════════════════════════════
    # Part A: Basic mode spectrum statistics
    # ════════════════════════════════════════════════════════════
    print("Part A: Mode spectrum statistics (ω_max = %.0f)" % omega_max)
    print()
    print(f"  {'q':>5s}  {'P?':>3s}  {'r':>6s}  {'N_modes':>8s}  "
          f"{'mean_gap':>10s}  {'std_gap':>10s}  {'min_gap':>10s}")
    print(f"  {'─'*5}  {'─'*3}  {'─'*6}  {'─'*8}  "
          f"{'─'*10}  {'─'*10}  {'─'*10}")

    all_data = {}
    for q in q_values:
        r = r_approx(q)
        modes = compute_mode_spectrum(q, r, omega_max)
        freqs = [m[0] for m in modes]

        mean_g, std_g, min_g, n_band = gap_statistics(
            freqs, omega_max * 0.3, omega_max * 0.7)

        all_data[q] = {
            'r': r, 'modes': modes, 'freqs': freqs,
            'n_modes': len(modes), 'mean_gap': mean_g,
            'std_gap': std_g, 'min_gap': min_g,
            'prime': is_prime(q),
        }

        print(f"  {q:5d}  {'★' if is_prime(q) else ' ':>3s}  "
              f"{r:6.3f}  {len(modes):8d}  "
              f"{mean_g:10.6f}  {std_g:10.6f}  {min_g:10.6f}")

    print()

    # ════════════════════════════════════════════════════════════
    # Part B: Near-degeneracy pair counts
    # ════════════════════════════════════════════════════════════
    print("Part B: Near-degeneracy pairs (ω in [9, 21])")
    print()

    epsilons = [0.001, 0.005, 0.01]
    hdr = f"  {'q':>5s}  {'P?':>3s}  {'N_band':>7s}"
    for eps in epsilons:
        hdr += f"  {'ε='+str(eps):>10s}"
    hdr += f"  {'pairs/N²':>10s}"
    print(hdr)
    print(f"  {'─'*5}  {'─'*3}  {'─'*7}" +
          f"  {'─'*10}" * len(epsilons) + f"  {'─'*10}")

    for q in q_values:
        d = all_data[q]
        band_freqs = [f for f in d['freqs'] if 9 <= f <= 21]
        N_band = len(band_freqs)

        line = f"  {q:5d}  {'★' if d['prime'] else ' ':>3s}  {N_band:7d}"
        last_count = 0
        for eps in epsilons:
            cnt = pair_count(band_freqs, eps)
            line += f"  {cnt:10d}"
            last_count = cnt

        # Normalized: pairs per N² (density-independent measure)
        norm = last_count / (N_band * N_band) if N_band > 0 else 0
        line += f"  {norm:10.6f}"
        print(line)

    print()

    # ════════════════════════════════════════════════════════════
    # Part C: Beat frequency test
    # ════════════════════════════════════════════════════════════
    print("Part C: Beat frequency test")
    print("  Count mode pairs with |ω_i - ω_j| ≈ d/q (ε = 0.002)")
    print("  d marked ÷ if it divides q")
    print()

    test_qs = [135, 137, 139, 141, 105, 121]
    for q in test_qs:
        d = all_data.get(q)
        if d is None:
            continue
        modes = d['modes']
        # Use modes in a moderate frequency band
        band_modes = [m for m in modes if 5 <= m[0] <= 25]
        band_freqs = [m[0] for m in band_modes]
        divs = divisors(q)

        bt = {}
        for dd in range(1, 16):
            target = float(dd) / q
            cnt = 0
            N = len(band_freqs)
            for i in range(N):
                for j in range(i + 1, N):
                    diff = band_freqs[j] - band_freqs[i]
                    if diff > target + 0.002:
                        break
                    if abs(diff - target) < 0.002:
                        cnt += 1
            is_div = dd in divs or (q % dd == 0 and dd > 1)
            bt[dd] = (cnt, is_div)

        print(f"  q = {q} ({'prime' if d['prime'] else 'composite'}), "
              f"divisors = {divs[:6]}{'...' if len(divs) > 6 else ''}")
        for dd in range(1, 16):
            cnt, is_div = bt[dd]
            marker = " ÷" if is_div else "  "
            bar = "█" * min(cnt, 40)
            print(f"    d={dd:2d}{marker}  Δω={dd/q:.4f}  "
                  f"pairs={cnt:4d}  {bar}")
        print()

    # ════════════════════════════════════════════════════════════
    # Part D: Deep comparison — 135 vs 137
    # ════════════════════════════════════════════════════════════
    print()
    print("Part D: Spectral comparison — q=135 vs q=137")
    print()

    for q in [135, 137]:
        d = all_data[q]
        freqs = d['freqs']

        # Mode count in windows
        windows = [(1, 5), (5, 10), (10, 15), (15, 20), (20, 25)]
        print(f"  q = {q} ({'prime' if d['prime'] else 'composite'}):")
        print(f"    Total modes: {d['n_modes']}")
        for lo, hi in windows:
            n = sum(1 for f in freqs if lo <= f <= hi)
            print(f"    ω ∈ [{lo:2d}, {hi:2d}]: {n:4d} modes")

        # Pair degeneracy at very tight epsilon
        band = [f for f in freqs if 5 <= f <= 20]
        for eps in [0.0001, 0.0005, 0.001, 0.005]:
            cnt = pair_count(band, eps)
            print(f"    Pairs with |Δω| < {eps:.4f}: {cnt:5d}")
        print()

    # ════════════════════════════════════════════════════════════
    # Part E: Summary statistics — prime vs composite
    # ════════════════════════════════════════════════════════════
    print()
    print("Part E: Summary — prime vs composite")
    print("-" * 72)
    print()

    primes = [all_data[q] for q in q_values if all_data[q]['prime']]
    comps = [all_data[q] for q in q_values if not all_data[q]['prime']]

    if primes:
        avg_n = sum(d['n_modes'] for d in primes) / len(primes)
        avg_gap = sum(d['mean_gap'] for d in primes) / len(primes)
        avg_min = sum(d['min_gap'] for d in primes) / len(primes)
        print(f"  Primes ({len(primes)}):")
        print(f"    Mean mode count:   {avg_n:.1f}")
        print(f"    Mean gap:          {avg_gap:.6f}")
        print(f"    Mean min gap:      {avg_min:.6f}")

    if comps:
        avg_n = sum(d['n_modes'] for d in comps) / len(comps)
        avg_gap = sum(d['mean_gap'] for d in comps) / len(comps)
        avg_min = sum(d['min_gap'] for d in comps) / len(comps)
        print(f"  Composites ({len(comps)}):")
        print(f"    Mean mode count:   {avg_n:.1f}")
        print(f"    Mean gap:          {avg_gap:.6f}")
        print(f"    Mean min gap:      {avg_min:.6f}")

    print()
    t_total = time.time() - t_start
    print(f"Total runtime: {t_total:.1f}s")


if __name__ == '__main__':
    main()
