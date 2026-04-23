"""
R63 Track 2 — Pure p-sheet viable-region map.

Track 1 tested two (ε_p, s_p) points and showed baseline is clean,
Track 21's extreme fails.  Track 2 maps the full viable region:
sweep a 2D grid; at each point, (a) build the metric and calibrate
L_ring_p to the (3, 6) proton, (b) run Track 1's pure-p-sheet
audit, (c) check which of baseline's 7 observed-particle matches
are preserved.

Output: per-point CSV grid, viability tables, shortlist of
candidate points.
"""

import sys, os
import math
import csv
import time
from fractions import Fraction

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    derive_L_ring, L_vector_from_params, signature_ok, M_P_MEV,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF, modelF_baseline

from track1_proton_ghost_audit import (
    enumerate_pure_p_modes, classify_z3_free_mode, match_observed,
    OBSERVED,
)


# Baseline's matched-particle set (from Track 1 F2)
BASELINE_MATCHES = {"p", "π⁰", "η′", "Δ⁺", "Ξ⁻", "Ξ⁰", "Ω⁻"}


# Grid definition
# Include baseline (0.55, 0.162) exactly plus surrounding coverage.
EPS_P_GRID = [0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65,
              0.70, 0.80, 0.90, 1.00, 1.20, 1.50, 2.00]
S_P_GRID = [0.00, 0.05, 0.10, 0.14, 0.162, 0.18, 0.20, 0.25, 0.30,
            0.35, 0.40, 0.45, 0.50]


def evaluate_point(eps_p, s_p):
    """Audit a single (ε_p, s_p) point.  Returns result dict or None
    if signature fails."""
    try:
        L_ring_p = derive_L_ring(M_P_MEV, 3, 6, eps_p, s_p, K_MODELF)
    except Exception:
        return None
    if L_ring_p <= 0 or L_ring_p != L_ring_p:  # NaN guard
        return None

    params = modelF_baseline(eps_p=eps_p, s_p=s_p, L_ring_p=L_ring_p)
    G = build_aug_metric(params)
    if not signature_ok(G):
        return None
    L = L_vector_from_params(params)

    modes = enumerate_pure_p_modes(G, L)
    z3_free = [m for m in modes if m['z3_free']]

    ghosts = []
    matched_particles = set()
    for m in z3_free:
        cls, _ = classify_z3_free_mode(m['E'], m['Q_eff'])
        if cls == 'ghost-sub-observed':
            ghosts.append(m)
        elif cls == 'observed':
            mm = match_observed(m['E'], m['Q_eff'])
            if mm:
                matched_particles.add(mm[0].name)

    mu_36 = math.sqrt((3/eps_p)**2 + (6 - 3*s_p)**2)
    lightest_ghost_E = min((g['E'] for g in ghosts), default=None)

    preserved = matched_particles & BASELINE_MATCHES
    lost = BASELINE_MATCHES - matched_particles
    gained = matched_particles - BASELINE_MATCHES

    return {
        'eps_p': eps_p,
        's_p': s_p,
        'L_ring_p': L_ring_p,
        'mu_36': mu_36,
        'n_ghosts': len(ghosts),
        'lightest_ghost_E': lightest_ghost_E,
        'n_matched': len(matched_particles),
        'n_baseline_preserved': len(preserved),
        'n_baseline_lost': len(lost),
        'n_gained': len(gained),
        'matched': matched_particles,
        'lost': lost,
        'gained': gained,
        'ghosts': ghosts,
    }


def main():
    print("=" * 100)
    print("R63 Track 2 — Pure p-sheet viable-region map")
    print("=" * 100)
    print()
    print(f"  Grid: ε_p ∈ {EPS_P_GRID[0]}..{EPS_P_GRID[-1]}  ({len(EPS_P_GRID)} values)")
    print(f"        s_p ∈ {S_P_GRID[0]}..{S_P_GRID[-1]}  ({len(S_P_GRID)} values)")
    print(f"  Total points: {len(EPS_P_GRID) * len(S_P_GRID)}")
    print(f"  Baseline matches (7 particles): {sorted(BASELINE_MATCHES)}")
    print()

    results = {}
    t0 = time.time()
    for i, eps_p in enumerate(EPS_P_GRID):
        for j, s_p in enumerate(S_P_GRID):
            r = evaluate_point(eps_p, s_p)
            results[(eps_p, s_p)] = r
        elapsed = time.time() - t0
        done = (i + 1) * len(S_P_GRID)
        total = len(EPS_P_GRID) * len(S_P_GRID)
        print(f"  ε_p = {eps_p:.2f} done   ({done}/{total}, {elapsed:.0f}s elapsed)")
    print()

    # ─── Ghost grid ──────────────────────────────────────────────
    print("─" * 100)
    print("  Sub-observed ghost count at each (ε_p, s_p):")
    print("─" * 100)
    header = "   ε_p\\s_p  "
    for s in S_P_GRID:
        header += f"  {s:>5.2f}"
    print(header)
    for eps_p in EPS_P_GRID:
        row = f"   {eps_p:>7.2f}  "
        for s_p in S_P_GRID:
            r = results.get((eps_p, s_p))
            if r is None:
                row += f"  {'  -- ':>5s}"
            else:
                n = r['n_ghosts']
                row += f"  {n:>5d}" if n > 0 else f"  {'·':>5s}"
        print(row)
    print()
    print("  (· = 0 ghosts, clean;  number = ghost count;  -- = signature fail)")
    print()

    # ─── Baseline-match preservation grid ────────────────────────
    print("─" * 100)
    print("  Baseline-match count out of 7 at each (ε_p, s_p):")
    print("─" * 100)
    print(header)
    for eps_p in EPS_P_GRID:
        row = f"   {eps_p:>7.2f}  "
        for s_p in S_P_GRID:
            r = results.get((eps_p, s_p))
            if r is None:
                row += f"  {'  -- ':>5s}"
            else:
                n = r['n_baseline_preserved']
                row += f"  {n:>5d}"
        print(row)
    print()

    # ─── μ(3, 6) grid ────────────────────────────────────────────
    print("─" * 100)
    print("  μ(3, 6) at each (ε_p, s_p)  (sub-π⁰-ghost bound: μ(3,6) ≤ 8.09):")
    print("─" * 100)
    print(header)
    for eps_p in EPS_P_GRID:
        row = f"   {eps_p:>7.2f}  "
        for s_p in S_P_GRID:
            r = results.get((eps_p, s_p))
            if r is None:
                row += f"  {'  -- ':>5s}"
            else:
                row += f"  {r['mu_36']:>5.2f}"
        print(row)
    print()

    # ─── Shortlist: clean + most baseline matches preserved ─────
    strict = [r for r in results.values()
              if r is not None and r['n_ghosts'] == 0 and r['n_baseline_preserved'] == 7]
    relaxed6 = [r for r in results.values()
                if r is not None and r['n_ghosts'] == 0 and r['n_baseline_preserved'] >= 6]
    relaxed5 = [r for r in results.values()
                if r is not None and r['n_ghosts'] == 0 and r['n_baseline_preserved'] >= 5]

    def show_shortlist(tag, rows):
        print("─" * 100)
        print(f"  SHORTLIST ({tag}):  {len(rows)} points")
        print("─" * 100)
        rows = sorted(rows, key=lambda r: (-r['n_baseline_preserved'],
                                             -r['n_matched'], r['eps_p'], r['s_p']))
        print(f"  {'ε_p':>6s}  {'s_p':>6s}  {'L_ring_p':>10s}  {'μ(3,6)':>7s}  "
              f"{'matched':>8s}  {'baseline':>8s}  {'lost':>20s}  "
              f"{'gained':>20s}")
        print("  " + "─" * 96)
        for r in rows[:40]:
            lost_str = ",".join(sorted(r['lost'])) if r['lost'] else "—"
            gained_str = ",".join(sorted(r['gained'])) if r['gained'] else ""
            print(f"  {r['eps_p']:>6.2f}  {r['s_p']:>6.3f}  {r['L_ring_p']:>10.2f}  "
                  f"{r['mu_36']:>7.3f}  {r['n_matched']:>8d}  "
                  f"{r['n_baseline_preserved']:>8d}  "
                  f"{lost_str:<20s}  {gained_str:<20s}")
        if len(rows) > 40:
            print(f"  ... and {len(rows) - 40} more")
        print()

    show_shortlist("clean + all 7 baseline matches", strict)
    show_shortlist("clean + ≥ 6 baseline matches", relaxed6)
    show_shortlist("clean + ≥ 5 baseline matches (broadest)", relaxed5)


    # ─── CSV output ──────────────────────────────────────────────
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'outputs',
                             'track2_grid.csv')
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['eps_p', 's_p', 'L_ring_p', 'mu_36', 'signature_ok',
                    'n_ghosts', 'lightest_ghost_E',
                    'n_matched', 'n_baseline_preserved', 'matched',
                    'lost_vs_baseline', 'gained_vs_baseline'])
        for eps_p in EPS_P_GRID:
            for s_p in S_P_GRID:
                r = results.get((eps_p, s_p))
                if r is None:
                    w.writerow([eps_p, s_p, '', '', 'FALSE',
                                '', '', '', '', '', '', ''])
                else:
                    w.writerow([
                        r['eps_p'], r['s_p'],
                        f"{r['L_ring_p']:.4f}", f"{r['mu_36']:.4f}",
                        'TRUE', r['n_ghosts'],
                        f"{r['lightest_ghost_E']:.2f}" if r['lightest_ghost_E'] else '',
                        r['n_matched'], r['n_baseline_preserved'],
                        '|'.join(sorted(r['matched'])),
                        '|'.join(sorted(r['lost'])),
                        '|'.join(sorted(r['gained'])),
                    ])
    print(f"  Grid CSV written to: {csv_path}")
    print()

    # ─── Summary ─────────────────────────────────────────────────
    print("=" * 100)
    print("R63 Track 2 — viable-region map summary")
    print("=" * 100)
    print()
    total = len(results)
    sig_ok = sum(1 for r in results.values() if r is not None)
    zero_ghosts = sum(1 for r in results.values() if r is not None and r['n_ghosts'] == 0)
    all_matches = len(strict)
    at_least_6 = len(relaxed6)
    at_least_5 = len(relaxed5)
    print(f"  Total grid points:               {total}")
    print(f"  Signature-OK:                    {sig_ok}  ({100*sig_ok/total:.0f}%)")
    print(f"  Zero sub-observed ghosts:        {zero_ghosts}  ({100*zero_ghosts/total:.0f}%)")
    print(f"  Clean + 7 baseline matches:      {all_matches}  ({100*all_matches/total:.0f}%)")
    print(f"  Clean + ≥ 6 baseline matches:    {at_least_6}  ({100*at_least_6/total:.0f}%)")
    print(f"  Clean + ≥ 5 baseline matches:    {at_least_5}  ({100*at_least_5/total:.0f}%)")
    print()


if __name__ == "__main__":
    main()
