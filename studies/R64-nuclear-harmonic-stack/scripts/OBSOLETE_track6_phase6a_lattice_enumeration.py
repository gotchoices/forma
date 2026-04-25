"""
R64 Track 6 Phase 6a — P-sheet primitive lattice enumeration and shell structure.

Goal: enumerate all (n_t, n_r) primitives on the p-sheet at Point B,
sort by mass, and look for natural clusters/gaps that could correspond
to nuclear shell closures.

The hypothesis: each (n_t, n_r) primitive holds 6 strands (3 colors ×
2 spins, R63 T10 Pauli capacity).  Each PRIMITIVE PAIR with positive
and negative ring directions (n_r and −n_r) holds 12 strands = 4
baryons = 2 protons + 2 neutrons.

If the lattice naturally clusters by mass into groups whose pair-counts
match observed nuclear magic-number gap capacities, then nuclear shell
structure emerges from R64's harmonic stack.

Observed nuclear magic numbers (per isospin): 2, 8, 20, 28, 50, 82, 126.
Corresponding total-baryon thresholds (both isospins): 4, 16, 40, 56,
100, 164, 252.
Per-shell baryon capacities: 4, 12, 24, 16, 44, 64, 88.
Per-shell primitive-pair capacities (4 baryons per pair): 1, 3, 6, 4,
11, 16, 22.

Phase 6a tests whether the MaSt lattice naturally has these
cardinalities in successive mass-ordered groups.

Output:
  outputs/track6_phase6a_lattice.csv
  outputs/track6_phase6a_mass_spectrum.png
"""

import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# ─── Point B parameters ────────────────────────────────────────────────

EPS_P = 0.2052
S_P   = 0.0250
K_P   = 63.629    # MeV/μ-unit (anchored to proton at (3, +2))


# ─── Mass formula ──────────────────────────────────────────────────────

def mu2(n_t, n_r, eps=EPS_P, s=S_P):
    return (n_t / eps)**2 + (n_r - s * n_t)**2


def mass(n_t, n_r):
    return K_P * math.sqrt(mu2(n_t, n_r))


# ─── Lattice enumeration ──────────────────────────────────────────────

def gcd(a, b):
    """Standard gcd."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def enumerate_lattice(n_t_max=6, n_r_max=20, mass_max=2500.0,
                      exclusion='none'):
    """Enumerate primitives.  exclusion modes:
      'none'         — full lattice (pure mass ordering, no rules)
      'gcd_only'     — keep only gcd(n_t, |n_r|)=1 primitives (Q132 v2)
      'q132_plus'    — gcd=1 plus exclude (1, 0), (1, ±1) per user hint
    """
    primitives = []
    for n_t in range(1, n_t_max + 1):
        for n_r in range(-n_r_max, n_r_max + 1):
            # Apply exclusion rules
            if exclusion == 'gcd_only':
                # Skip n_r = 0 (treat gcd(n, 0) = n as not primitive)
                if n_r == 0:
                    continue
                if gcd(n_t, n_r) != 1:
                    continue
            elif exclusion == 'q132_plus':
                if n_r == 0:
                    continue
                if gcd(n_t, n_r) != 1:
                    continue
                # User's hint: shear rules out (1, ±1)
                if n_t == 1 and abs(n_r) == 1:
                    continue

            m = mass(n_t, n_r)
            if m < mass_max:
                primitives.append({
                    'n_t': n_t,
                    'n_r': n_r,
                    'mass': m,
                    'pair_label': (n_t, abs(n_r)),
                    'is_zero_n_r': (n_r == 0),
                })
    return primitives


def group_into_pairs(primitives):
    """Group (n_t, ±n_r) primitives into pairs.  Returns list of pairs:
    each pair is {'n_t', 'abs_n_r', 'mass_avg', 'mass_min', 'mass_max', 'count'}.
    """
    pair_dict = {}
    for p in primitives:
        key = p['pair_label']
        if key not in pair_dict:
            pair_dict[key] = {
                'n_t': p['n_t'],
                'abs_n_r': abs(p['n_r']),
                'masses': [],
                'count': 0,
            }
        pair_dict[key]['masses'].append(p['mass'])
        pair_dict[key]['count'] += 1

    pairs = []
    for key, d in pair_dict.items():
        masses = sorted(d['masses'])
        pairs.append({
            'n_t': d['n_t'],
            'abs_n_r': d['abs_n_r'],
            'mass_min': masses[0],
            'mass_max': masses[-1],
            'mass_avg': (masses[0] + masses[-1]) / 2,
            'count_in_pair': d['count'],   # 1 if n_r=0, 2 if n_r ≠ 0
        })
    pairs.sort(key=lambda x: x['mass_avg'])
    return pairs


def cumulative_baryon_capacity(pairs):
    """Cumulative baryons as we fill pairs in mass order.

    A pair with n_r ≠ 0 holds 12 strands = 4 baryons.
    A "pair" with n_r = 0 holds 6 strands = 2 baryons (single primitive).
    """
    cum = 0
    cum_list = []
    for p in pairs:
        # 6 strands per primitive; 2 primitives per pair (if n_r ≠ 0)
        n_strands = 6 * p['count_in_pair']
        # 3 strands per baryon (uud, udd composition)
        n_baryons = n_strands // 3 if n_strands % 3 == 0 else n_strands / 3
        cum += n_baryons
        cum_list.append({
            **p,
            'n_strands': n_strands,
            'n_baryons': n_baryons,
            'cum_baryons': cum,
        })
    return cum_list


# ─── Magic number references ──────────────────────────────────────────

OBSERVED_MAGIC_PER_ISOSPIN = [2, 8, 20, 28, 50, 82, 126]
OBSERVED_DOUBLY_MAGIC_A = [4, 16, 40, 56, 100, 164, 252]


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 6 Phase 6a — P-sheet lattice enumeration at Point B")
    print("=" * 110)
    print()
    print(f"  Point B: ε_p = {EPS_P}, s_p = {S_P:+}, K_p = {K_P:.3f}")
    print()
    print("  Pauli capacity per primitive: 6 strands (3 color × 2 spin) [R63 T10]")
    print("  Primitive pair (±n_r): 12 strands = 4 baryons = 2p + 2n")
    print("  Single (n_r=0) primitive: 6 strands = 2 baryons")
    print()
    print(f"  Observed magic-doubly A: {OBSERVED_DOUBLY_MAGIC_A}")
    print(f"  Per-shell baryon capacity (gaps): "
          f"{[OBSERVED_DOUBLY_MAGIC_A[0]] + [OBSERVED_DOUBLY_MAGIC_A[i+1] - OBSERVED_DOUBLY_MAGIC_A[i] for i in range(len(OBSERVED_DOUBLY_MAGIC_A)-1)]}")
    print(f"  Per-shell primitive-pair capacity (÷4): "
          f"{[1, 3, 6, 4, 11, 16, 22]}")
    print()

    # ─── Enumerate lattice — three variations ─────────────────────
    print()
    print("=" * 110)
    print("VARIATION A: Pure mass-ordered enumeration (no exclusions)")
    print("=" * 110)
    primitives_A = enumerate_lattice(n_t_max=6, n_r_max=20, mass_max=3000.0,
                                     exclusion='none')
    pairs_A = cumulative_baryon_capacity(group_into_pairs(primitives_A))
    print(f"  Lattice has {len(primitives_A)} primitives in {len(pairs_A)} pairs")
    print(f"  Magic-A alignment check (cum baryons after first 7 'shells'):")
    target_pair_counts = [1, 4, 10, 14, 25, 41, 63]
    for i, target_A in enumerate(OBSERVED_DOUBLY_MAGIC_A):
        target_pairs = target_pair_counts[i]
        if target_pairs - 1 < len(pairs_A):
            cum = pairs_A[target_pairs - 1]['cum_baryons']
            match = "✓" if cum == target_A else "✗"
            print(f"    A={target_A:>3d}: cum after {target_pairs} pairs = "
                  f"{cum:.0f} {match}")
    print()

    print("=" * 110)
    print("VARIATION B: gcd(n_t, |n_r|) = 1 only (Q132 v2 primitive selection)")
    print("=" * 110)
    primitives_B = enumerate_lattice(n_t_max=6, n_r_max=20, mass_max=3000.0,
                                     exclusion='gcd_only')
    pairs_B = cumulative_baryon_capacity(group_into_pairs(primitives_B))
    print(f"  Lattice has {len(primitives_B)} primitives in {len(pairs_B)} pairs")
    for i, target_A in enumerate(OBSERVED_DOUBLY_MAGIC_A):
        target_pairs = target_pair_counts[i]
        if target_pairs - 1 < len(pairs_B):
            cum = pairs_B[target_pairs - 1]['cum_baryons']
            match = "✓" if cum == target_A else "✗"
            print(f"    A={target_A:>3d}: cum after {target_pairs} pairs = "
                  f"{cum:.0f} {match}")
    print()

    print("=" * 110)
    print("VARIATION C: gcd=1 + exclude (1, ±1) per user hint")
    print("=" * 110)
    primitives_C = enumerate_lattice(n_t_max=6, n_r_max=20, mass_max=3000.0,
                                     exclusion='q132_plus')
    pairs_C = cumulative_baryon_capacity(group_into_pairs(primitives_C))
    print(f"  Lattice has {len(primitives_C)} primitives in {len(pairs_C)} pairs")
    for i, target_A in enumerate(OBSERVED_DOUBLY_MAGIC_A):
        target_pairs = target_pair_counts[i]
        if target_pairs - 1 < len(pairs_C):
            cum = pairs_C[target_pairs - 1]['cum_baryons']
            match = "✓" if cum == target_A else "✗"
            print(f"    A={target_A:>3d}: cum after {target_pairs} pairs = "
                  f"{cum:.0f} {match}")
    print()

    # Use Variation C for detailed analysis
    pairs_with_cum = pairs_C
    primitives = primitives_C
    pairs = group_into_pairs(primitives)

    print(f"  Lattice has {len(primitives)} primitives in {len(pairs)} pairs")
    print(f"  Mass range: {min(p['mass'] for p in primitives):.1f} — "
          f"{max(p['mass'] for p in primitives):.1f} MeV")
    print()

    # ─── Display lattice in mass order ────────────────────────────
    print("Pairs in mass order (lowest 60):")
    print("-" * 100)
    print(f"  {'idx':>4s}  {'(n_t, |n_r|)':>14s}  {'mass_avg':>10s}  "
          f"{'count':>7s}  {'baryons':>8s}  {'cum_baryons':>12s}  "
          f"{'matches magic?':>18s}")
    for i, p in enumerate(pairs_with_cum[:60]):
        cum = p['cum_baryons']
        # Check if this cumulative count matches a doubly-magic A
        magic_match = ""
        if cum in OBSERVED_DOUBLY_MAGIC_A:
            magic_match = f"★ A={cum} doubly-magic"
        print(f"  {i:>4d}  ({p['n_t']:>3d},{p['abs_n_r']:>4d})    "
              f"{p['mass_avg']:>10.2f}  {p['count_in_pair']:>7d}  "
              f"{p['n_baryons']:>8.0f}  {p['cum_baryons']:>12.0f}  "
              f"{magic_match:>18s}")
    print()

    # ─── Look for shell-closure pattern ──────────────────────────
    print("Searching for shell-closure structure:")
    print("-" * 100)

    # Strategy 1: see at which cumulative-pair counts the observed magic numbers fall
    target_cum_baryons = OBSERVED_DOUBLY_MAGIC_A
    print("  Where do the observed magic A values sit in the lattice ordering?")
    print(f"  {'magic A':>10s}  {'pairs needed':>14s}  "
          f"{'pair index in lattice':>24s}  {'mass at that pair':>20s}")
    for target in target_cum_baryons:
        # Find first pair where cum_baryons >= target
        for i, p in enumerate(pairs_with_cum):
            if p['cum_baryons'] >= target:
                pair_label = f"({p['n_t']}, ±{p['abs_n_r']})"
                print(f"  {target:>10d}  {p['cum_baryons']:>14.0f}  "
                      f"  {i:>4d}: {pair_label:>14s}  "
                      f"{p['mass_avg']:>15.2f} MeV")
                break
        else:
            print(f"  {target:>10d}  not reached within lattice")
    print()

    # Strategy 2: look at gaps in the mass spectrum
    print("Mass-gap analysis (looking for natural clusters):")
    print("-" * 100)
    masses = [p['mass_avg'] for p in pairs_with_cum]
    gaps = [(masses[i+1] - masses[i], i) for i in range(len(masses)-1)]
    gaps_sorted = sorted(gaps, reverse=True)[:15]
    print(f"  Top 15 mass gaps in the lattice:")
    print(f"  {'rank':>4s}  {'gap (MeV)':>10s}  {'after pair idx':>15s}  "
          f"{'cum baryons':>12s}  {'next mass':>10s}")
    for rank, (gap, idx) in enumerate(gaps_sorted):
        cum = pairs_with_cum[idx]['cum_baryons']
        next_mass = pairs_with_cum[idx+1]['mass_avg']
        magic = "★" if cum in OBSERVED_DOUBLY_MAGIC_A else ""
        print(f"  {rank+1:>4d}  {gap:>10.2f}  {idx:>15d}  "
              f"{cum:>12.0f}  {next_mass:>10.2f}  {magic}")
    print()

    # ─── Save CSV ─────────────────────────────────────────────────
    csv_path = out_dir / "track6_phase6a_lattice.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(pairs_with_cum[0].keys()))
        w.writeheader()
        w.writerows(pairs_with_cum)

    # ─── Plot ─────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 1, figsize=(14, 10))

    # Top: mass spectrum with magic-A markers
    ax = axes[0]
    cum_arr = np.array([p['cum_baryons'] for p in pairs_with_cum])
    mass_arr = np.array([p['mass_avg'] for p in pairs_with_cum])
    n_t_arr = np.array([p['n_t'] for p in pairs_with_cum])

    # Color by n_t
    colors = plt.cm.tab10(n_t_arr / 6.0)
    ax.scatter(cum_arr, mass_arr, c=colors, s=30,
               edgecolor='black', linewidth=0.3)

    # Mark observed magic-A
    for magic_A in OBSERVED_DOUBLY_MAGIC_A:
        if magic_A <= max(cum_arr):
            ax.axvline(magic_A, color='red', linestyle='--',
                       alpha=0.5, linewidth=1.5)
            ax.text(magic_A, max(mass_arr) * 0.95, f'A={magic_A}',
                    rotation=90, fontsize=8, color='red',
                    verticalalignment='top')

    ax.set_xlabel('Cumulative baryons (filled in mass order)')
    ax.set_ylabel('Pair-average mass (MeV)')
    ax.set_title('P-sheet lattice mass spectrum at Point B '
                 '(red dashes = observed doubly-magic A)')
    ax.grid(alpha=0.3)
    ax.set_xlim(0, min(300, max(cum_arr) + 10))

    # Bottom: histogram-like view of pair masses
    ax = axes[1]
    pair_idx = np.arange(len(pairs_with_cum))
    n_t_for_pair = [p['n_t'] for p in pairs_with_cum]
    masses_for_pair = [p['mass_avg'] for p in pairs_with_cum]
    bars = ax.bar(pair_idx, masses_for_pair,
                   color=[plt.cm.tab10(nt/6.0) for nt in n_t_for_pair],
                   alpha=0.7, edgecolor='black', linewidth=0.3)

    # Mark pair indices that complete a magic A
    cum = np.cumsum([p['n_baryons'] for p in pairs_with_cum])
    for i, c in enumerate(cum):
        if c in OBSERVED_DOUBLY_MAGIC_A:
            ax.axvline(i + 0.5, color='red', linestyle='--', alpha=0.5)

    ax.set_xlabel('Pair index (sorted by mass)')
    ax.set_ylabel('Pair-average mass (MeV)')
    ax.set_title('Mass-ordered pairs (color = n_t)')
    ax.grid(alpha=0.3, axis='y')
    ax.set_xlim(-0.5, min(70, len(pair_idx)) - 0.5)

    plt.tight_layout()
    plt.savefig(out_dir / "track6_phase6a_mass_spectrum.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    # ─── Verdict ──────────────────────────────────────────────────
    print("=" * 110)
    print("VERDICT — Phase 6a")
    print("=" * 110)
    print()

    # Check if magic numbers fall at "natural" boundaries
    target_pair_counts = [1, 4, 10, 14, 25, 41, 63]  # cumulative pairs to magic A
    print(f"  For each observed doubly-magic A, the lattice would need:")
    for i, target_A in enumerate(OBSERVED_DOUBLY_MAGIC_A):
        target_pairs = target_pair_counts[i]
        # Find what cumulative-baryon count we get at that pair index
        if target_pairs - 1 < len(pairs_with_cum):
            cum_at_target = pairs_with_cum[target_pairs - 1]['cum_baryons']
            mass_at = pairs_with_cum[target_pairs - 1]['mass_avg']
            match = "✓" if cum_at_target == target_A else "✗"
            print(f"    A = {target_A:>3d}: target pair-count {target_pairs:>2d}, "
                  f"actual cum_baryons = {cum_at_target:.0f} at "
                  f"mass {mass_at:.1f} {match}")
    print()

    print(f"  CSV: {csv_path}")
    print(f"  Plot: {out_dir / 'track6_phase6a_mass_spectrum.png'}")


if __name__ == "__main__":
    main()
