"""
R49 Track 1b: First-above-cutoff triplet

If the waveguide cutoff is the neutrino's mode selection
mechanism, then the first 3 propagating modes above cutoff
should form the observed triplet.

Waveguide cutoff: mode (n₃, n₄) propagates if n₄ > |n₃|/ε.

Mass formula: μ²(n₃, n₄) = (n₃/ε)² + (n₄ − n₃·s)²

Strategy:
  1. Fine sweep of ε from 0.1 to 20
  2. At each ε, list all propagating modes, sort by mass
  3. Take the first 3 → candidate triplet
  4. Compute Δm² ratio
  5. Scan s to find best match to 33.6
"""

import math
import numpy as np

PI = math.pi
TAU = 2 * PI

DM2_21 = 7.53e-5
DM2_31 = 2.530e-3
TARGET_RATIO = DM2_31 / DM2_21  # 33.60
COSMO_BOUND = 0.120

HBAR = 1.054571817e-34
C = 299792458.0
EV_TO_J = 1.602176634e-19
HC_EVM = HBAR * C / EV_TO_J


def mu_sq(n3, n4, s, eps):
    return (n3 / eps)**2 + (n4 - n3 * s)**2


def propagates(n3, n4, eps):
    """Waveguide cutoff: mode propagates if n₄ > |n₃|/ε."""
    return n4 > abs(n3) / eps


def propagating_modes(eps, s, n3_max=20, n4_max=10):
    """All propagating modes, sorted by mass."""
    modes = []
    for n3 in range(-n3_max, n3_max + 1):
        for n4 in range(1, n4_max + 1):
            if not propagates(n3, n4, eps):
                continue
            ms = mu_sq(n3, n4, s, eps)
            if ms > 0:
                modes.append((n3, n4, ms))
    modes.sort(key=lambda m: m[2])
    return modes


def compute_I(p, q, eps):
    t = np.linspace(0, TAU, 2048, endpoint=False)
    dt = TAU / 2048
    rho = 1.0 + eps * np.cos(p * t)
    return float(np.sum(np.sqrt(p**2 * eps**2 + q**2 * rho**2)) * dt)


_spin_cache = {}

def Lz_over_hbar(p, q, eps):
    key = (abs(p), abs(q), round(eps, 4))
    if key not in _spin_cache:
        I = compute_I(abs(p), abs(q), eps)
        S = 2 * PI**2 * q**2 * (2 + eps**2) / I**2
        _spin_cache[key] = S / abs(q)
    return _spin_cache[key]


def triplet_ratio(modes, i, j, k, s, eps):
    dm21 = modes[j][2] - modes[i][2]
    dm31 = modes[k][2] - modes[i][2]
    if dm21 <= 0:
        return None
    return dm31 / dm21


def triplet_masses(modes, i, j, k):
    dm21 = modes[j][2] - modes[i][2]
    if dm21 <= 0:
        return None
    E0_sq = DM2_21 / dm21
    E0 = math.sqrt(E0_sq)
    m1 = E0 * math.sqrt(modes[i][2])
    m2 = E0 * math.sqrt(modes[j][2])
    m3 = E0 * math.sqrt(modes[k][2])
    L4 = HC_EVM / E0
    return m1, m2, m3, E0, L4


def print_section(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def main():
    print("R49 Track 1b: First-Above-Cutoff Triplet")
    print("=" * 70)

    # ── 1. Sweep ε, find first 3 modes above cutoff ─────────────

    print_section("1. FIRST-3-ABOVE-CUTOFF vs ε (at s = 0)")

    print("  At s = 0 (no shear), the mode spectrum is symmetric.")
    print("  Show first 5 propagating modes at each ε.\n")

    print(f"  {'ε':>6} {'#1':>10} {'#2':>10} {'#3':>10}"
          f" {'#4':>10} {'#5':>10}")
    print(f"  {'-'*6} {'-'*10} {'-'*10} {'-'*10}"
          f" {'-'*10} {'-'*10}")

    for eps in [0.3, 0.5, 0.7, 1.0, 1.2, 1.5, 2.0, 2.5,
                3.0, 4.0, 5.0, 7.0, 10.0]:
        modes = propagating_modes(eps, s=0)
        row = f"  {eps:6.1f}"
        for i in range(min(5, len(modes))):
            n3, n4, ms = modes[i]
            row += f" ({n3:2d},{n4:d})"
        print(row)

    # ── 2. At each ε, sweep s to match ratio ────────────────────

    print_section("2. SWEEP (ε, s): FIRST-3 TRIPLET RATIO")

    eps_fine = np.concatenate([
        np.arange(0.3, 1.0, 0.05),
        np.arange(1.0, 3.0, 0.1),
        np.arange(3.0, 10.0, 0.5),
        np.arange(10.0, 20.1, 2.0),
    ])

    s_fine = np.concatenate([
        np.arange(0.0, 0.05, 0.001),
        np.arange(0.05, 0.2, 0.005),
        np.arange(0.2, 0.5, 0.01),
    ])

    best_hits = []

    for eps in eps_fine:
        best_for_eps = None
        for s in s_fine:
            modes = propagating_modes(eps, s)
            if len(modes) < 3:
                continue
            ratio = triplet_ratio(modes, 0, 1, 2, s, eps)
            if ratio is None:
                continue
            err = abs(ratio - TARGET_RATIO)
            if err < 1.0:
                info = triplet_masses(modes, 0, 1, 2)
                if info is None:
                    continue
                m1, m2, m3, E0, L4 = info
                sm = m1 + m2 + m3
                if sm >= COSMO_BOUND:
                    continue
                rec = {
                    'eps': float(eps), 's': float(s),
                    'n1': (modes[0][0], modes[0][1]),
                    'n2': (modes[1][0], modes[1][1]),
                    'n3': (modes[2][0], modes[2][1]),
                    'ratio': ratio, 'err': err,
                    'm1': m1*1000, 'm2': m2*1000, 'm3': m3*1000,
                    'sm': sm*1000, 'E0': E0*1000,
                    'L4_um': L4*1e6,
                    'L3_um': eps*L4*1e6,
                    'n_prop': len(modes),
                }
                if best_for_eps is None or err < best_for_eps['err']:
                    best_for_eps = rec

        if best_for_eps is not None:
            best_hits.append(best_for_eps)

    print(f"  Found {len(best_hits)} ε values with a matching"
          f" first-3 triplet.\n")

    if best_hits:
        print(f"  {'ε':>6} {'s':>7} {'ν₁':>8} {'ν₂':>8} {'ν₃':>8}"
              f" {'m₁':>6} {'m₂':>6} {'m₃':>6} {'Σm':>6}"
              f" {'ratio':>6} {'err':>5}"
              f" {'L₃':>7} {'L₄':>7}")
        print(f"  {'-'*6} {'-'*7} {'-'*8} {'-'*8} {'-'*8}"
              f" {'-'*6} {'-'*6} {'-'*6} {'-'*6}"
              f" {'-'*6} {'-'*5} {'-'*7} {'-'*7}")
        for r in best_hits:
            print(f"  {r['eps']:6.2f} {r['s']:7.4f}"
                  f" {str(r['n1']):>8} {str(r['n2']):>8}"
                  f" {str(r['n3']):>8}"
                  f" {r['m1']:6.1f} {r['m2']:6.1f}"
                  f" {r['m3']:6.1f} {r['sm']:6.1f}"
                  f" {r['ratio']:6.2f} {r['err']:5.2f}"
                  f" {r['L3_um']:7.1f} {r['L4_um']:7.1f}")

    # ── 3. Best matches: detail ──────────────────────────────────

    print_section("3. BEST MATCHES (ratio within 0.5 of target)")

    close = [r for r in best_hits if r['err'] < 0.5]
    close.sort(key=lambda r: r['err'])

    if close:
        for r in close[:10]:
            print(f"  ε = {r['eps']:.2f}, s = {r['s']:.4f}")
            print(f"    Triplet: {r['n1']}, {r['n2']}, {r['n3']}")
            print(f"    Masses: {r['m1']:.2f}, {r['m2']:.2f},"
                  f" {r['m3']:.2f} meV  (Σ = {r['sm']:.1f})")
            print(f"    Ratio: {r['ratio']:.3f}"
                  f"  (target {TARGET_RATIO:.2f},"
                  f" err = {r['err']:.3f})")
            print(f"    Sheet: L₃ = {r['L3_um']:.1f} μm,"
                  f" L₄ = {r['L4_um']:.1f} μm")

            spins = []
            for nm in [r['n1'], r['n2'], r['n3']]:
                p, q = abs(nm[0]), nm[1]
                lz = Lz_over_hbar(p, q, r['eps'])
                spins.append(lz)
            print(f"    Spins: [{', '.join(f'{v:.3f}' for v in spins)}]")

            modes = propagating_modes(r['eps'], r['s'])
            print(f"    Total propagating modes"
                  f" (|n₃|≤20, n₄≤10): {len(modes)}")
            print(f"    First 6: {[(m[0],m[1]) for m in modes[:6]]}")
            print()
    else:
        print("  None found within 0.5 of target.")

    # ── 4. What if first-3 doesn't work? Try first-N ────────────

    print_section("4. WHAT IF TRIPLET IS NOT THE FIRST 3?")

    print("  Try all triplets from the first 6 propagating modes.\n")

    alt_hits = []
    for eps in eps_fine:
        for s in s_fine:
            modes = propagating_modes(eps, s)
            if len(modes) < 3:
                continue
            n_check = min(6, len(modes))
            for i in range(n_check):
                for j in range(i+1, n_check):
                    for k in range(j+1, n_check):
                        ratio = triplet_ratio(modes, i, j, k, s, eps)
                        if ratio is None:
                            continue
                        err = abs(ratio - TARGET_RATIO)
                        if err < 0.3:
                            info = triplet_masses(modes, i, j, k)
                            if info is None:
                                continue
                            m1, m2, m3, E0, L4 = info
                            sm = m1 + m2 + m3
                            if sm >= COSMO_BOUND:
                                continue
                            gap = i  # modes below lightest
                            alt_hits.append({
                                'eps': float(eps), 's': float(s),
                                'n1': (modes[i][0], modes[i][1]),
                                'n2': (modes[j][0], modes[j][1]),
                                'n3': (modes[k][0], modes[k][1]),
                                'idx': (i, j, k),
                                'ratio': ratio, 'err': err,
                                'sm': sm * 1000,
                                'gap': gap,
                            })

    alt_hits.sort(key=lambda r: r['err'])

    first3 = [r for r in alt_hits if r['idx'] == (0, 1, 2)]
    skipped = [r for r in alt_hits if r['idx'] != (0, 1, 2)]

    print(f"  First-3 matches (0,1,2): {len(first3)}")
    print(f"  Skipping modes (gap > 0): {len(skipped)}")

    if skipped:
        print(f"\n  Best non-first-3 solutions:")
        seen = set()
        count = 0
        for r in skipped[:20]:
            key = (round(r['eps'],2), r['idx'], r['n1'], r['n2'], r['n3'])
            if key in seen:
                continue
            seen.add(key)
            print(f"    ε={r['eps']:5.2f} s={r['s']:.3f}"
                  f"  idx={r['idx']}"
                  f"  {r['n1']},{r['n2']},{r['n3']}"
                  f"  ratio={r['ratio']:.2f}"
                  f"  Σm={r['sm']:.0f}meV"
                  f"  gap={r['gap']}")
            count += 1
            if count >= 10:
                break

    # ── 5. Summary ───────────────────────────────────────────────

    print_section("5. SUMMARY")

    if close:
        best = close[0]
        print(f"  Best first-above-cutoff triplet:")
        print(f"    ε = {best['eps']:.2f}, s = {best['s']:.4f}")
        print(f"    Modes: {best['n1']}, {best['n2']}, {best['n3']}")
        print(f"    Ratio error: {best['err']:.3f}")
        print(f"    Σm = {best['sm']:.1f} meV")
    else:
        print("  No exact first-above-cutoff match found.")

    print(f"\n  Total first-3 matches (err < 0.3): {len(first3)}")
    print(f"  Total with-gap matches (err < 0.3): {len(skipped)}")


if __name__ == '__main__':
    main()
