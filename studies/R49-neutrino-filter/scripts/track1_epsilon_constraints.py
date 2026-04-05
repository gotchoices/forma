"""
R49 Track 1: Constraints on ε_ν

Sweeps the (ε_ν, s₃₄) parameter space to find all mode triplets
on Ma_ν that match experimental neutrino oscillation data.

Strategy (for performance):
  Phase 1: Find all triplets matching Δm² ratio (fast, mass only)
  Phase 2: Check Σm and ordering (fast)
  Phase 3: Compute spin ONLY for surviving candidates (slow)

Mass formula:
  μ²(n₃, n₄) = (n₃/ε)² + (n₄ − n₃·s)²

Spin formula (finite ε):
  L_z/ℏ = S(ε)/q, where S(ε) = 2π²q²(2 + ε²) / I²(ε)
  I(ε) = ∫₀²π √(p²ε² + q²(1+ε cos(pt))²) dt
"""

import math
import numpy as np

PI = math.pi
TAU = 2 * PI

DM2_21 = 7.53e-5     # eV²
DM2_31 = 2.530e-3    # eV²
TARGET_RATIO = DM2_31 / DM2_21  # 33.60
RATIO_SIGMA = 0.9
COSMO_BOUND = 0.120   # eV

HBAR = 1.054571817e-34
C = 299792458.0
EV_TO_J = 1.602176634e-19
HC_EVM = HBAR * C / EV_TO_J


def mu_sq(n3, n4, s, eps):
    return (n3 / eps)**2 + (n4 - n3 * s)**2


def compute_I(p, q, eps):
    t = np.linspace(0, TAU, 2048, endpoint=False)
    dt = TAU / 2048
    rho = 1.0 + eps * np.cos(p * t)
    return float(np.sum(np.sqrt(p**2 * eps**2 + q**2 * rho**2)) * dt)


_spin_cache = {}

def Lz_over_hbar(p, q, eps):
    key = (abs(p), abs(q), round(eps, 5))
    if key not in _spin_cache:
        I = compute_I(abs(p), abs(q), eps)
        S = 2 * PI**2 * q**2 * (2 + eps**2) / I**2
        _spin_cache[key] = S / abs(q)
    return _spin_cache[key]


def build_modes(eps, s, n3_max=10, n4_max=6):
    modes = []
    for n3 in range(-n3_max, n3_max + 1):
        for n4 in range(0, n4_max + 1):
            if n3 == 0 and n4 == 0:
                continue
            ms = mu_sq(n3, n4, s, eps)
            if ms <= 0:
                continue
            modes.append((n3, n4, ms))
    modes.sort(key=lambda m: m[2])
    return modes


def find_triplets_fast(modes):
    """Find triplets matching Δm² ratio. Returns indices + ratio."""
    n = len(modes)
    results = []
    for i in range(n):
        for j in range(i + 1, n):
            dm21 = modes[j][2] - modes[i][2]
            if dm21 <= 1e-30:
                continue
            target_ms3 = modes[i][2] + dm21 * TARGET_RATIO
            for k in range(j + 1, n):
                if modes[k][2] < target_ms3 - dm21 * RATIO_SIGMA:
                    continue
                if modes[k][2] > target_ms3 + dm21 * RATIO_SIGMA:
                    break
                dm31 = modes[k][2] - modes[i][2]
                ratio = dm31 / dm21
                results.append((i, j, k, ratio))
    return results


def check_masses(modes, i, j, k):
    dm21 = modes[j][2] - modes[i][2]
    if dm21 <= 0:
        return None
    E0_sq = DM2_21 / dm21
    E0 = math.sqrt(E0_sq)
    m1 = E0 * math.sqrt(modes[i][2])
    m2 = E0 * math.sqrt(modes[j][2])
    m3 = E0 * math.sqrt(modes[k][2])
    sm = m1 + m2 + m3
    if sm >= COSMO_BOUND:
        return None
    if not (m1 < m2 < m3):
        return None
    L4 = HC_EVM / E0
    return m1, m2, m3, sm, E0, L4


def count_between(modes, ms_lo, ms_hi):
    return sum(1 for _, _, ms in modes if ms_lo < ms < ms_hi)


def print_section(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def main():
    print("R49 Track 1: Constraints on ε_ν")
    print("=" * 70)

    eps_values = [0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0,
                  3.0, 5.0, 7.0, 10.0, 20.0, 50.0, 100.0]
    s_values = [0.001, 0.005, 0.01, 0.015, 0.02, 0.022,
                0.025, 0.03, 0.04, 0.05, 0.07, 0.1,
                0.15, 0.2, 0.3, 0.4]

    print(f"\n  Sweeping {len(eps_values)} ε × {len(s_values)} s"
          f" = {len(eps_values)*len(s_values)} points")
    print(f"  Target Δm² ratio: {TARGET_RATIO:.2f} ± {RATIO_SIGMA}")
    print(f"  Cosmological bound: Σm < {COSMO_BOUND*1000:.0f} meV")

    # ── Phase 1 & 2: mass-based search ───────────────────────────

    print_section("PHASE 1-2: MASS-BASED TRIPLET SEARCH")

    candidates = []  # (eps, s, modes_i, modes_j, modes_k, ratio, masses)
    eps_stats = {}

    for eps in eps_values:
        for s in s_values:
            modes = build_modes(eps, s)
            triplets = find_triplets_fast(modes)
            for i, j, k, ratio in triplets:
                mass_info = check_masses(modes, i, j, k)
                if mass_info is None:
                    continue
                m1, m2, m3, sm, E0, L4 = mass_info
                n_st = count_between(modes, modes[i][2], modes[k][2]) - 1
                candidates.append({
                    'eps': eps, 's': s,
                    'n1': (modes[i][0], modes[i][1]),
                    'n2': (modes[j][0], modes[j][1]),
                    'n3': (modes[k][0], modes[k][1]),
                    'ratio': ratio,
                    'm1': m1*1000, 'm2': m2*1000, 'm3': m3*1000,
                    'sm': sm*1000,
                    'E0': E0*1000,
                    'L3_um': eps * L4 * 1e6,
                    'L4_um': L4 * 1e6,
                    'n_sterile': n_st,
                })

                if eps not in eps_stats:
                    eps_stats[eps] = 0
                eps_stats[eps] += 1

    print(f"  Candidates passing mass + Σm + ordering: {len(candidates)}")
    print()
    print(f"  {'ε':>6} {'N_cand':>8}")
    print(f"  {'-'*6} {'-'*8}")
    for e in sorted(eps_stats.keys()):
        print(f"  {e:6.1f} {eps_stats[e]:8d}")

    # ── Phase 3: spin check on candidates ────────────────────────

    print_section("PHASE 3: SPIN CHECK")

    viable = []
    marginal = []

    unique_mode_eps = set()
    for c in candidates:
        for nm in [c['n1'], c['n2'], c['n3']]:
            unique_mode_eps.add((abs(nm[0]), nm[1], c['eps']))

    print(f"  Computing spin for {len(unique_mode_eps)} unique"
          f" (|n₃|, n₄, ε) combinations...")

    for p, q, eps in unique_mode_eps:
        if q > 0:
            Lz_over_hbar(p, q, eps)

    print(f"  Done. Cache size: {len(_spin_cache)}\n")

    for c in candidates:
        spins = []
        all_ok = True
        for nm in [c['n1'], c['n2'], c['n3']]:
            p, q = abs(nm[0]), nm[1]
            if q == 0:
                spins.append(None)
                all_ok = False
                continue
            lz = Lz_over_hbar(p, q, c['eps'])
            spins.append(lz)
            if abs(lz - 0.5) >= 0.15:
                all_ok = False
        c['spins'] = spins
        c['spin_ok'] = all_ok
        if all_ok:
            viable.append(c)
        elif all(v is not None and abs(v - 0.5) < 0.25
                 for v in spins):
            marginal.append(c)

    # ── Results ──────────────────────────────────────────────────

    print_section("VIABLE SOLUTIONS (all criteria)")

    if viable:
        print(f"  {'ε':>6} {'s':>7} {'ν₁':>8} {'ν₂':>8} {'ν₃':>8}"
              f" {'m₁':>6} {'m₂':>6} {'m₃':>6} {'Σm':>6}"
              f" {'ratio':>6} {'L₃':>7} {'L₄':>7} {'N_st':>4}"
              f" {'spins':>18}")
        print(f"  {'-'*6} {'-'*7} {'-'*8} {'-'*8} {'-'*8}"
              f" {'-'*6} {'-'*6} {'-'*6} {'-'*6}"
              f" {'-'*6} {'-'*7} {'-'*7} {'-'*4} {'-'*18}")
        for r in sorted(viable, key=lambda x: (x['eps'], x['s'])):
            sp = ",".join(f"{v:.2f}" if v else "?" for v in r['spins'])
            print(f"  {r['eps']:6.2f} {r['s']:7.4f}"
                  f" {str(r['n1']):>8} {str(r['n2']):>8}"
                  f" {str(r['n3']):>8}"
                  f" {r['m1']:6.1f} {r['m2']:6.1f}"
                  f" {r['m3']:6.1f} {r['sm']:6.1f}"
                  f" {r['ratio']:6.2f}"
                  f" {r['L3_um']:7.1f} {r['L4_um']:7.1f}"
                  f" {r['n_sterile']:4d} [{sp}]")
    else:
        print("  None found.")

    print_section("NEAR-MISS SOLUTIONS (spin within 0.25 of ½)")

    if marginal:
        shown = 0
        for r in sorted(marginal, key=lambda x: (x['eps'], x['s'])):
            if shown >= 25:
                break
            sp = ",".join(f"{v:.3f}" if v else "?" for v in r['spins'])
            print(f"  ε={r['eps']:5.1f} s={r['s']:.4f}"
                  f"  {str(r['n1']):>8} {str(r['n2']):>8}"
                  f" {str(r['n3']):>8}"
                  f"  Σm={r['sm']:6.1f}"
                  f"  spins=[{sp}]"
                  f"  ratio={r['ratio']:.2f}"
                  f"  N_st={r['n_sterile']}")
            shown += 1
        if len(marginal) > 25:
            print(f"  ... and {len(marginal) - 25} more")
        print(f"\n  Total near-misses: {len(marginal)}")
    else:
        print("  None found.")

    # ── Waveguide cutoff ─────────────────────────────────────────

    print_section("WAVEGUIDE CUTOFF LANDSCAPE")

    print("  Open boundary: propagates if n₄ > |n₃|/ε\n")

    test_modes = [(1,1), (-1,1), (1,2), (1,3), (3,2), (3,6), (2,4)]
    print(f"  {'ε':>6}", end="")
    for m in test_modes:
        print(f" {str(m):>6}", end="")
    print()
    print(f"  {'-'*6}", end="")
    for _ in test_modes:
        print(f" {'-'*6}", end="")
    print()
    for eps in [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0]:
        print(f"  {eps:6.1f}", end="")
        for n3, n4 in test_modes:
            prop = "✓" if n4 > abs(n3) / eps else "✗"
            print(f" {prop:>6}", end="")
        print()

    # ── Mode density ─────────────────────────────────────────────

    print_section("MODE DENSITY vs ε")

    s_demo = 0.022
    print(f"  At s = {s_demo}, modes with |n₃| ≤ 50, n₄ ≤ 10\n")
    print(f"  {'ε':>6} {'N_modes':>8} {'below 1eV':>10}")
    print(f"  {'-'*6} {'-'*8} {'-'*10}")

    for eps in [0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0]:
        modes = build_modes(eps, s_demo, n3_max=50, n4_max=10)
        ms_1eV = (1.0)**2  # rough: 1 eV in mu² units depends on E0
        # Use E0 from (1,1) + (1,2) mass splitting
        dm = abs(mu_sq(1, 2, s_demo, eps) - mu_sq(1, 1, s_demo, eps))
        if dm > 0:
            E0 = math.sqrt(DM2_21 / dm)
        else:
            E0 = 0.03
        cutoff_musq = (1.0 / E0)**2 if E0 > 0 else 1e10
        n_below = sum(1 for _, _, ms in modes if ms < cutoff_musq)
        print(f"  {eps:6.1f} {len(modes):8d} {n_below:10d}")

    # ── Summary ──────────────────────────────────────────────────

    print_section("SUMMARY")

    print(f"  Parameter points: {len(eps_values) * len(s_values)}")
    print(f"  Mass-viable triplets: {len(candidates)}")
    print(f"  Fully viable (+ spin): {len(viable)}")
    print(f"  Near-miss (spin marginal): {len(marginal)}")

    if viable:
        eps_range = sorted(set(r['eps'] for r in viable))
        s_range = sorted(set(r['s'] for r in viable))
        print(f"\n  Viable ε range: {min(eps_range)} — {max(eps_range)}")
        print(f"  Viable s range: {min(s_range):.4f} — {max(s_range):.4f}")
        unique = set((r['n1'], r['n2'], r['n3']) for r in viable)
        print(f"  Unique triplets: {len(unique)}")
        for t in sorted(unique):
            print(f"    {t[0]}, {t[1]}, {t[2]}")
    elif marginal:
        print("\n  No fully viable solutions, but near-misses exist.")
        print("  Spin criterion may need refinement or ε_ν may need")
        print("  finer sampling in the near-miss region.")


if __name__ == '__main__':
    main()
