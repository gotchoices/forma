#!/usr/bin/env python3
"""
R11 Track 7: Wave superposition / sub-harmonic test.

For each q, the photon makes q orbits around the major axis.
Each orbit deposits a wave contribution at different minor-circle
positions (θ_k = 2πpk/q).  We superimpose these contributions
and analyze the Fourier spectrum for sub-harmonic content.

The hypothesis (Q30): for prime q, all energy stays in the
fundamental Compton frequency.  For composite q, divisors create
sub-harmonic frequencies where partial constructive interference
leaks energy from the fundamental.

Three analyses:
  A. Orbit-indexed signal at an observation point (DFT over orbits)
  B. Torus surface field (2D Fourier decomposition)
  C. Varying kernel width to test robustness
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha


def factorize_divisors(q):
    """Return sorted list of non-trivial divisors of q (exclude 1 and q)."""
    divs = []
    for d in range(2, q):
        if q % d == 0:
            divs.append(d)
    return divs


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


def dft_power(signal_re, signal_im):
    """Compute |DFT|² for a complex signal given as separate re/im arrays."""
    N = len(signal_re)
    power = []
    two_pi = 2.0 * math.pi
    for n in range(N):
        Re = 0.0
        Im = 0.0
        for k in range(N):
            angle = -two_pi * n * k / N
            ca = math.cos(angle)
            sa = math.sin(angle)
            Re += signal_re[k] * ca - signal_im[k] * sa
            Im += signal_re[k] * sa + signal_im[k] * ca
        power.append(Re * Re + Im * Im)
    return power


def analysis_A(q, r, sigma=0.5):
    """
    Orbit-indexed signal at an observation point.

    An observer sits at θ_obs = 0 on the major circle.
    Orbit k passes at θ_k = 2πpk/q on the minor circle.
    The field contribution from orbit k has:
      - Compton phase: exp(2πi k/q)
      - Geometric weight: K(θ_k) from proximity kernel
      - Amplitude modulation: 1/(1 + r cos θ_k) from flux conservation

    Signal: a_k = K(θ_k) / (1 + r cos θ_k) × exp(2πi k/q)
    """
    p = (q - 1) // 2
    two_pi = 2.0 * math.pi

    sig_re = []
    sig_im = []

    for k in range(q):
        theta_k = (two_pi * p * k / q) % two_pi
        dt = theta_k
        if dt > math.pi:
            dt -= two_pi

        # Gaussian proximity kernel
        K = math.exp(-dt * dt / (2.0 * sigma * sigma))
        # Flux conservation amplitude
        amp = K / (1.0 + r * math.cos(theta_k))
        # Compton phase
        phase = two_pi * k / q
        sig_re.append(amp * math.cos(phase))
        sig_im.append(amp * math.sin(phase))

    return dft_power(sig_re, sig_im)


def analysis_B(q, r, N_phi=512):
    """
    Torus surface field projected onto the major circle.

    Sample the geodesic path densely.  At each point, the scalar
    wave ψ(t) = cos(2πt) is modulated by the local metric factor
    (1 + r cos θ)⁻¹.  Project onto φ bins by accumulating the
    field at each major-angle position.

    This captures intra-orbit θ variation, not just orbit-averaged θ.
    """
    p = (q - 1) // 2
    two_pi = 2.0 * math.pi
    pts_per_orbit = 64
    N_total = q * pts_per_orbit

    # Accumulate into φ bins (mod 2π)
    bins_re = [0.0] * N_phi
    bins_im = [0.0] * N_phi

    for i in range(N_total):
        t = (i + 0.5) / N_total  # t ∈ [0, 1]
        theta = two_pi * p * t
        phi = two_pi * q * t
        phi_mod = phi % two_pi
        bin_idx = int(phi_mod / two_pi * N_phi) % N_phi

        # Scalar wave amplitude
        wave_re = math.cos(two_pi * t)
        wave_im = math.sin(two_pi * t)
        # Metric modulation
        metric = 1.0 / (1.0 + r * math.cos(theta))

        bins_re[bin_idx] += wave_re * metric
        bins_im[bin_idx] += wave_im * metric

    return dft_power(bins_re, bins_im)


def analyze_spectrum(power, q, ref_freqs=None, label=""):
    """Extract key metrics from the power spectrum.

    ref_freqs: set of frequency indices to measure 'sub-harmonic' power.
    If None, uses q's own divisor-derived frequencies.
    """
    total = sum(power)
    if total == 0:
        return {'fund_frac': 0, 'sub_harm_frac': 0, 'max_non_fund': 0,
                'leakage_ratio': 0, 'n_divisors': 0}

    fund = power[1]  # n=1 is the fundamental Compton frequency
    divs = factorize_divisors(q)

    # Sub-harmonic power at divisor frequencies (own divisors)
    own_div_freqs = set()
    for d in divs:
        own_div_freqs.add(q // d)
        own_div_freqs.add(d)
    own_div_freqs.discard(1)
    own_div_freqs.discard(0)
    own_sub = sum(power[n] for n in own_div_freqs if 0 < n < len(power))

    # Power at reference frequencies (for fair cross-q comparison)
    ref_sub = 0.0
    if ref_freqs:
        ref_sub = sum(power[n] for n in ref_freqs if 0 < n < len(power))

    # Total non-fundamental power (all n ≠ 0 and ≠ 1)
    non_fund = total - fund - power[0]

    # Maximum single non-fundamental peak
    max_nf = 0
    max_nf_n = 0
    for n in range(2, len(power)):
        if power[n] > max_nf:
            max_nf = power[n]
            max_nf_n = n

    return {
        'fund_frac': fund / total,
        'non_fund_frac': non_fund / total,
        'own_sub_frac': own_sub / total,
        'ref_sub_frac': ref_sub / total,
        'max_nf': max_nf / total,
        'max_nf_n': max_nf_n,
        'n_divisors': len(divs),
        'total': total,
    }


def main():
    print("R11 Track 7: Wave Superposition / Sub-Harmonic Test")
    print("=" * 72)
    print()

    # q values: dense around 137, mix of primes and composites
    q_values = sorted(set([
        # Composites near 137
        105, 121, 125, 129, 133, 135, 141, 143, 145, 147, 153,
        # Primes near 137
        113, 127, 131, 137, 139, 149, 151,
        # Additional composites with many divisors
        165, 195,
        # Additional primes for comparison
        101, 103, 107, 109, 157, 163,
    ]))

    def r_approx(q):
        return 0.0025 * (q - 100) + 0.10

    # Reference divisor frequencies from q=135 (for fair comparison)
    # 135 = 3³×5, divisors = {3, 5, 9, 15, 27, 45}
    # Corresponding frequencies: {45, 27, 15, 9, 5, 3} and {3, 5, 9, 15, 27, 45}
    ref_divs_135 = {3, 5, 9, 15, 27, 45}

    # ════════════════════════════════════════════════════════════
    # Analysis A: Orbit-indexed signal
    # ════════════════════════════════════════════════════════════
    print("Analysis A: Orbit-indexed signal at observation point")
    print("  (Gaussian kernel σ = 0.5 rad, flux-conservation amplitude)")
    print()
    print(f"  {'q':>5s}  {'P?':>3s}  {'div':>4s}  "
          f"{'fund%':>8s}  {'non-fund%':>10s}  "
          f"{'own-div%':>10s}  {'ref-135%':>10s}")
    print(f"  {'─'*5}  {'─'*3}  {'─'*4}  "
          f"{'─'*8}  {'─'*10}  "
          f"{'─'*10}  {'─'*10}")

    results_A = []
    for q in q_values:
        r = r_approx(q)
        power = analysis_A(q, r, sigma=0.5)
        m = analyze_spectrum(power, q, ref_freqs=ref_divs_135)
        p = is_prime(q)
        results_A.append({'q': q, 'prime': p, 'power': power, **m})

        print(f"  {q:5d}  {'★' if p else ' ':>3s}  "
              f"{m['n_divisors']:4d}  "
              f"{m['fund_frac']*100:8.3f}  "
              f"{m['non_fund_frac']*100:10.4f}  "
              f"{m['own_sub_frac']*100:10.6f}  "
              f"{m['ref_sub_frac']*100:10.6f}")

    print()

    # Summary statistics
    primes_A = [r for r in results_A if r['prime']]
    comps_A = [r for r in results_A if not r['prime']]

    if primes_A:
        avg_fund = sum(r['fund_frac'] for r in primes_A) / len(primes_A)
        avg_ref = sum(r['ref_sub_frac'] for r in primes_A) / len(primes_A)
        print(f"  Primes ({len(primes_A)}):")
        print(f"    Mean fundamental:      {avg_fund*100:.3f}%")
        print(f"    Mean ref-135 power:    {avg_ref*100:.6f}%")

    if comps_A:
        avg_fund = sum(r['fund_frac'] for r in comps_A) / len(comps_A)
        avg_own = sum(r['own_sub_frac'] for r in comps_A) / len(comps_A)
        avg_ref = sum(r['ref_sub_frac'] for r in comps_A) / len(comps_A)
        print(f"  Composites ({len(comps_A)}):")
        print(f"    Mean fundamental:      {avg_fund*100:.3f}%")
        print(f"    Mean own-divisor power: {avg_own*100:.6f}%")
        print(f"    Mean ref-135 power:    {avg_ref*100:.6f}%")

    print()

    # ════════════════════════════════════════════════════════════
    # Analysis A': Fair comparison — same frequencies across q
    # ════════════════════════════════════════════════════════════
    print("Analysis A': Fair comparison — power at specific frequencies")
    print("  Power at n = 3, 5, 9, 15, 27, 45 for each q")
    print("  (These are 135's divisor frequencies)")
    print()
    test_ns = [3, 5, 9, 15, 27, 45]
    hdr = f"  {'q':>5s}  {'P?':>3s}"
    for n in test_ns:
        hdr += f"  {'n='+str(n):>10s}"
    hdr += f"  {'sum':>10s}"
    print(hdr)
    print(f"  {'─'*5}  {'─'*3}" + f"  {'─'*10}" * (len(test_ns) + 1))

    for res in results_A:
        q = res['q']
        power = res['power']
        total = res['total']
        line = f"  {q:5d}  {'★' if res['prime'] else ' ':>3s}"
        row_sum = 0
        for n in test_ns:
            if n < len(power):
                frac = power[n] / total * 100
                row_sum += frac
                is_own_div = q % n == 0 and n != 1 and n != q
                marker = "÷" if is_own_div else " "
                line += f"  {frac:9.5f}{marker}"
            else:
                line += f"  {'N/A':>10s}"
        line += f"  {row_sum:10.5f}"
        print(line)

    print()

    # ════════════════════════════════════════════════════════════
    # Analysis A'': Kernel width sweep
    # ════════════════════════════════════════════════════════════
    print("Analysis A'': Kernel width sweep (q=135 vs q=137)")
    print("  Power at 135's divisor frequencies {3,5,9,15,27,45}")
    print()
    sigmas = [0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.14]
    print(f"  {'σ':>6s}  {'q':>5s}  {'P?':>3s}  "
          f"{'fund%':>8s}  {'own-div%':>10s}  {'ref-135%':>10s}")
    print(f"  {'─'*6}  {'─'*5}  {'─'*3}  "
          f"{'─'*8}  {'─'*10}  {'─'*10}")

    for sigma in sigmas:
        for q in [135, 137]:
            r = r_approx(q)
            power = analysis_A(q, r, sigma=sigma)
            m = analyze_spectrum(power, q, ref_freqs=ref_divs_135)
            p = is_prime(q)
            print(f"  {sigma:6.2f}  {q:5d}  {'★' if p else ' ':>3s}  "
                  f"{m['fund_frac']*100:8.3f}  "
                  f"{m['own_sub_frac']*100:10.6f}  "
                  f"{m['ref_sub_frac']*100:10.6f}")
        print()

    # ════════════════════════════════════════════════════════════
    # Deep dive: power spectrum comparison
    # ════════════════════════════════════════════════════════════
    print()
    print("Deep dive: Power spectrum for q=135 vs q=137")
    print()

    for q in [135, 137]:
        r = r_approx(q)
        power = analysis_A(q, r, sigma=0.5)
        total = sum(power)
        p = (q - 1) // 2
        divs = factorize_divisors(q)
        div_set = set(divs) | set(q // d for d in divs) if divs else set()

        print(f"  q = {q} ({'prime' if is_prime(q) else 'composite'}), "
              f"p = {p}, divisors = {divs}")

        # Show top 15 peaks (excluding n=0)
        indexed = [(n, power[n] / total) for n in range(1, q)]
        indexed.sort(key=lambda x: -x[1])
        print(f"  Top 15 peaks:")
        for n, frac in indexed[:15]:
            tags = []
            if n == 1:
                tags.append("FUND")
            if n in div_set:
                tags.append("DIV")
            if n in ref_divs_135:
                tags.append("ref135")
            tag = " ".join(tags) if tags else ""
            print(f"    n = {n:4d}  {frac*100:10.6f}%  {tag}")
        print()

    # ════════════════════════════════════════════════════════════
    # Analysis C: Average power at divisor vs non-divisor freqs
    # ════════════════════════════════════════════════════════════
    print()
    print("Analysis C: Divisor frequency enhancement ratio")
    print("  For composites: (mean power at own divisor freqs)")
    print("                / (mean power at non-divisor freqs)")
    print()
    print(f"  {'q':>5s}  {'divisors':>20s}  "
          f"{'mean@div':>12s}  {'mean@other':>12s}  {'ratio':>8s}")
    print(f"  {'─'*5}  {'─'*20}  {'─'*12}  {'─'*12}  {'─'*8}")

    for res in results_A:
        q = res['q']
        if res['prime']:
            continue
        power = res['power']
        total = res['total']
        divs = factorize_divisors(q)
        div_freqs = set(divs) | set(q // d for d in divs)
        div_freqs.discard(0)
        div_freqs.discard(1)
        div_freqs.discard(q)

        non_div_freqs = set(range(2, q)) - div_freqs
        if not div_freqs or not non_div_freqs:
            continue

        mean_div = sum(power[n] for n in div_freqs) / len(div_freqs)
        mean_other = sum(power[n] for n in non_div_freqs) / len(non_div_freqs)
        ratio = mean_div / mean_other if mean_other > 0 else float('inf')

        divs_str = "×".join(str(d) for d in sorted(divs)[:4])
        if len(divs) > 4:
            divs_str += "..."
        print(f"  {q:5d}  {divs_str:>20s}  "
              f"{mean_div/total*100:12.6f}  "
              f"{mean_other/total*100:12.6f}  "
              f"{ratio:8.3f}")

    print()
    print("Done.")


if __name__ == '__main__':
    main()
