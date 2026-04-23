"""
R60 Track 21 — Pion search: windings AND free geometric parameters.

Motivation: Track 20 Phase D's |n| ≤ 6 brute-force search leaves
π⁰ at 10.4% and π± at 13.3% — the worst accuracy in the model-F
inventory.  Two avenues to try closing the gap:

  (1) Higher winding.  Pions are produced in high-energy
      collisions, so their mode assignments may involve |n| > 6.
  (2) Free geometric parameters.  The electron sheet (ε_e, s_e)
      is pinned tightly (R53 generations + R60 T17 exemption +
      ghost ordering), but the proton sheet (ε_p, s_p) inherits
      its value from model-E's R19 formula — a constraint that
      no longer applies in model-F.  Shifting (ε_p, s_p) changes
      L_ring_p (via m_p calibration on (3, 6)), which changes
      the p-ring mode spacing and hence the pion mass gap.

Structure:

  Phase 1 — Baseline winding sweep at model-F's (ε_p=0.55,
            s_p=0.162).  Replicates the original Track 21
            result: higher n_max does not improve pions.

  Phase 2 — (ε_p, s_p) grid sweep at n_max=6.  For each
            point, rebuild metric (σ_ra auto-updates), derive
            L_ring_p from m_p on (3, 6), run 2-sheet pion
            search, report best.

  Phase 3 — Take the best (ε_p, s_p) from Phase 2; re-run the
            winding sweep there to confirm that higher n_max
            still does not help (or does, if parameter space
            opened up new regimes).

Under per-sheet Dirac–Kähler + SU(2) composition (R62 D7d / R60
T20), pions are 2-sheet mesons.  Search restricts to exactly two
active sheets (third has both windings = 0) across the pairs
{e+p, e+ν, ν+p}.  Filters: Z₃ on p-sheet, Q-match, composite α.

Sandboxed.  No changes to prior tracks.
"""

import sys, os
import time

sys.path.insert(0, os.path.dirname(__file__))

from track1_solver import (
    derive_L_ring, L_vector_from_params, mode_energy, mode_6_to_11,
    signature_ok, M_P_MEV,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF, modelF_baseline
from track15_phase2_alpha import alpha_sum_composite


# Pion targets: label, mass (MeV), charge
TARGETS = [
    ("π⁰", 134.977, 0),
    ("π±", 139.570, -1),   # π-; π+ symmetric under n→−n
]

N_MAX_SWEEP = [6, 10, 15, 20]
TOP_K = 5

# Phase D (model-F baseline) for comparison
PHASE_D_BASELINE = {
    "π⁰": (0.1040, "(0,0,-1,-6,0,-1)"),
    "π±": (0.1330, "(1,2,0,0,0,-1)"),
}

# Phase 2 parameter grid
EPSILON_P_GRID = [0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.55, 0.70,
                  0.85, 1.00, 1.25, 1.50, 2.00]
S_P_GRID = [0.00, 0.05, 0.10, 0.15, 0.162, 0.20, 0.25, 0.30, 0.40, 0.50]


# ─── Filters ────────────────────────────────────────────────────────

def charge_ok(n6, target_Q):
    return -n6[0] + n6[4] == target_Q


def alpha_ok(n6, target_Q):
    a = alpha_sum_composite(n6)
    if target_Q == 0:
        return abs(a) <= 1
    return a * a == 1


# ─── Result accumulator ─────────────────────────────────────────────

class SearchResult:
    """Accumulator: top-k best, nearest-below, nearest-above."""
    def __init__(self, target, top_k):
        self.target = target
        self.top_k = top_k
        self.best = []
        self.below = None
        self.above = None
        self.total_evaluated = 0

    def add(self, n6, E, pair):
        rel = abs(E - self.target) / self.target
        entry = (rel, n6, E, pair)
        self.total_evaluated += 1
        if len(self.best) < self.top_k or rel < self.best[-1][0]:
            self.best.append(entry)
            self.best.sort(key=lambda x: x[0])
            if len(self.best) > self.top_k:
                self.best.pop()
        if E < self.target:
            if self.below is None or E > self.below[2]:
                self.below = entry
        if E > self.target:
            if self.above is None or E < self.above[2]:
                self.above = entry

    def merge(self, other):
        for e in other.best:
            if len(self.best) < self.top_k or e[0] < self.best[-1][0]:
                self.best.append(e)
                self.best.sort(key=lambda x: x[0])
                if len(self.best) > self.top_k:
                    self.best.pop()
        if other.below is not None:
            if self.below is None or other.below[2] > self.below[2]:
                self.below = other.below
        if other.above is not None:
            if self.above is None or other.above[2] < self.above[2]:
                self.above = other.above
        self.total_evaluated += other.total_evaluated


# ─── Per-pair search primitives ─────────────────────────────────────

def search_ep(G, L, target_mass, target_Q, n_max, top_k):
    rng = range(-n_max, n_max + 1)
    z3_rng = [n for n in rng if n % 3 == 0]
    result = SearchResult(target_mass, top_k)
    for n_et in rng:
        for n_er in rng:
            if n_et == 0 and n_er == 0:
                continue
            for n_pt in z3_rng:
                for n_pr in rng:
                    if n_pt == 0 and n_pr == 0:
                        continue
                    n6 = (n_et, n_er, 0, 0, n_pt, n_pr)
                    if not charge_ok(n6, target_Q):
                        continue
                    if not alpha_ok(n6, target_Q):
                        continue
                    n11 = mode_6_to_11(n6)
                    E = mode_energy(G, L, n11)
                    result.add(n6, E, "e+p")
    return result


def search_en(G, L, target_mass, target_Q, n_max, top_k):
    rng = range(-n_max, n_max + 1)
    result = SearchResult(target_mass, top_k)
    for n_et in rng:
        for n_er in rng:
            if n_et == 0 and n_er == 0:
                continue
            for n_nut in rng:
                for n_nur in rng:
                    if n_nut == 0 and n_nur == 0:
                        continue
                    n6 = (n_et, n_er, n_nut, n_nur, 0, 0)
                    if not charge_ok(n6, target_Q):
                        continue
                    if not alpha_ok(n6, target_Q):
                        continue
                    n11 = mode_6_to_11(n6)
                    E = mode_energy(G, L, n11)
                    result.add(n6, E, "e+ν")
    return result


def search_np(G, L, target_mass, target_Q, n_max, top_k):
    rng = range(-n_max, n_max + 1)
    z3_rng = [n for n in rng if n % 3 == 0]
    result = SearchResult(target_mass, top_k)
    for n_nut in rng:
        for n_nur in rng:
            if n_nut == 0 and n_nur == 0:
                continue
            for n_pt in z3_rng:
                for n_pr in rng:
                    if n_pt == 0 and n_pr == 0:
                        continue
                    n6 = (0, 0, n_nut, n_nur, n_pt, n_pr)
                    if not charge_ok(n6, target_Q):
                        continue
                    if not alpha_ok(n6, target_Q):
                        continue
                    n11 = mode_6_to_11(n6)
                    E = mode_energy(G, L, n11)
                    result.add(n6, E, "ν+p")
    return result


def run_full_search(G, L, target_mass, target_Q, n_max, top_k):
    """Merge all three 2-sheet pair searches."""
    merged = SearchResult(target_mass, top_k)
    merged.merge(search_ep(G, L, target_mass, target_Q, n_max, top_k))
    merged.merge(search_en(G, L, target_mass, target_Q, n_max, top_k))
    merged.merge(search_np(G, L, target_mass, target_Q, n_max, top_k))
    return merged


# ─── Output helpers ─────────────────────────────────────────────────

def fmt_entry(entry):
    if entry is None:
        return "(none)"
    rel, n6, E, pair = entry
    return f"{pair:>5s} {str(n6).replace(' ', ''):<26s}  E={E:>9.3f}  Δm/m={rel*100:+7.3f}%"


def print_target_at_params(G, L, label, target, Q, baseline_rel):
    """Detailed report for one (target, metric) combination at varying n_max."""
    for n_max in N_MAX_SWEEP:
        t0 = time.time()
        merged = run_full_search(G, L, target, Q, n_max, TOP_K)
        elapsed = time.time() - t0

        print(f"  n_max = {n_max:>2d}   ({elapsed:.1f}s, "
              f"{merged.total_evaluated:,} past filter)")
        print(f"    Top-{TOP_K}:")
        for i, (rel, n6, E, pair) in enumerate(merged.best):
            marker = " ★" if rel < baseline_rel else ""
            print(f"      {i+1:>2d}. {pair:>5s}  "
                  f"{str(n6).replace(' ', ''):<28s}  "
                  f"E={E:>9.3f} MeV  Δm/m={rel*100:+7.3f}%{marker}")
        print(f"    Nearest below:  {fmt_entry(merged.below)}")
        print(f"    Nearest above:  {fmt_entry(merged.above)}")
        if merged.below is not None and merged.above is not None:
            gap = merged.above[2] - merged.below[2]
            print(f"    Gap straddling target: {gap:.2f} MeV")
        print()


def build_metric_at(eps_p, s_p):
    """Build params + metric at given (ε_p, s_p).  Returns (ok, params, G, L, L_ring_p)."""
    try:
        L_ring_p = derive_L_ring(M_P_MEV, 3, 6, eps_p, s_p, K_MODELF)
    except Exception:
        return False, None, None, None, None
    if L_ring_p <= 0 or L_ring_p > 10000 or L_ring_p != L_ring_p:  # NaN check
        return False, None, None, None, L_ring_p
    params = modelF_baseline(eps_p=eps_p, s_p=s_p, L_ring_p=L_ring_p)
    G = build_aug_metric(params)
    if not signature_ok(G):
        return False, params, G, None, L_ring_p
    L = L_vector_from_params(params)
    return True, params, G, L, L_ring_p


# ─── Phases ─────────────────────────────────────────────────────────

def phase1_baseline_winding_sweep():
    """Phase 1: winding sweep at model-F baseline (ε_p=0.55, s_p=0.162)."""
    print("=" * 100)
    print("PHASE 1 — Winding sweep at model-F baseline (ε_p=0.55, s_p=0.162)")
    print("=" * 100)
    print()

    ok, params, G, L, L_ring_p = build_metric_at(0.55, 0.162037)
    assert ok, "Model-F baseline should always be signature-OK"
    print(f"  L_ring_p (derived from m_p on (3,6)): {L_ring_p:.4f} fm")
    print()

    for label, target, Q in TARGETS:
        baseline_rel, baseline_tup = PHASE_D_BASELINE[label]
        print(f"─── {label}   Q={Q:+d}   target={target:.4f} MeV ───")
        print(f"     Phase D baseline: {baseline_rel*100:.2f}% at {baseline_tup}")
        print()
        print_target_at_params(G, L, label, target, Q, baseline_rel)
        print()


def phase2_parameter_sweep():
    """Phase 2: sweep (ε_p, s_p) at n_max=6.  Return best points per target."""
    print("=" * 100)
    print("PHASE 2 — Parameter sweep: (ε_p, s_p) at n_max=6")
    print("=" * 100)
    print()
    print(f"  ε_p grid:  {EPSILON_P_GRID}")
    print(f"  s_p grid:  {S_P_GRID}")
    print(f"  Total:     {len(EPSILON_P_GRID) * len(S_P_GRID)} points")
    print()
    print(f"  For each point:  derive L_ring_p from m_p on (3,6),")
    print(f"                    rebuild metric (σ_ra auto-updates),")
    print(f"                    run 2-sheet pion search at n_max=6.")
    print()

    # Per-target best tracking: {label: (rel, eps_p, s_p, n6, E, pair, L_ring_p)}
    per_target_best = {label: None for label, _, _ in TARGETS}

    # Grid output (for each target, Δm/m at each grid point)
    grid_results = {label: {} for label, _, _ in TARGETS}

    t_start = time.time()
    n_ok = 0
    n_bad = 0
    for eps_p in EPSILON_P_GRID:
        for s_p in S_P_GRID:
            ok, params, G, L, L_ring_p = build_metric_at(eps_p, s_p)
            if not ok:
                n_bad += 1
                for label, _, _ in TARGETS:
                    grid_results[label][(eps_p, s_p)] = None
                continue
            n_ok += 1
            for label, target, Q in TARGETS:
                r = run_full_search(G, L, target, Q, 6, 1)
                if r.best:
                    rel, n6, E, pair = r.best[0]
                    grid_results[label][(eps_p, s_p)] = rel
                    cur = per_target_best[label]
                    if cur is None or rel < cur[0]:
                        per_target_best[label] = (rel, eps_p, s_p, n6, E, pair, L_ring_p)
                else:
                    grid_results[label][(eps_p, s_p)] = None

    elapsed = time.time() - t_start
    print(f"  Swept {n_ok} signature-OK points, {n_bad} skipped (bad signature/L_p).")
    print(f"  Total time: {elapsed:.1f}s")
    print()

    # Print grid table per target
    for label, target, Q in TARGETS:
        print(f"─── {label}   target = {target:.4f} MeV ───")
        baseline_rel, _ = PHASE_D_BASELINE[label]
        print(f"     (Phase D baseline: {baseline_rel*100:.2f}%; "
              f"★ = better than baseline)")
        print()
        # Header
        header = f"    ε_p\\s_p"
        for s_p in S_P_GRID:
            header += f"  {s_p:>6.3f}"
        print(header)
        for eps_p in EPSILON_P_GRID:
            row = f"    {eps_p:>7.2f}"
            for s_p in S_P_GRID:
                rel = grid_results[label].get((eps_p, s_p))
                if rel is None:
                    row += f"  {'---':>6s}"
                else:
                    marker = "★" if rel < baseline_rel else " "
                    row += f"  {rel*100:>5.2f}{marker}"
            print(row)
        print()
        # Best point
        best = per_target_best[label]
        if best:
            rel, eps_p, s_p, n6, E, pair, L_p = best
            delta = (baseline_rel - rel) * 100
            print(f"    Best:  ε_p={eps_p:.3f}  s_p={s_p:.3f}  "
                  f"L_ring_p={L_p:.2f} fm")
            print(f"           mode = {pair:>5s}  "
                  f"{str(n6).replace(' ', ''):<26s}  E={E:.3f}  "
                  f"Δm/m={rel*100:+.3f}%  "
                  f"(Δ vs baseline: {delta:+.2f} pp)")
        print()
    print()
    return per_target_best


def phase3_winding_at_best(per_target_best):
    """Phase 3: re-run winding sweep at best (ε_p, s_p) found in Phase 2."""
    print("=" * 100)
    print("PHASE 3 — Winding sweep at best Phase 2 (ε_p, s_p) points")
    print("=" * 100)
    print()

    # Try each target's best point (may be the same, may differ)
    seen = set()
    for label, target, Q in TARGETS:
        best = per_target_best[label]
        if not best:
            continue
        rel, eps_p, s_p, _, _, _, L_ring_p = best
        key = (round(eps_p, 3), round(s_p, 3))
        if key in seen:
            continue
        seen.add(key)

        print(f"─── (ε_p={eps_p:.3f}, s_p={s_p:.3f})   "
              f"L_ring_p={L_ring_p:.2f} fm   (best for {label}) ───")
        print()
        ok, _, G, L, _ = build_metric_at(eps_p, s_p)
        if not ok:
            print("    Bad signature / L_p — skipping.")
            continue
        for lab, tgt, q in TARGETS:
            baseline_rel, baseline_tup = PHASE_D_BASELINE[lab]
            print(f"  {lab}   Q={q:+d}   target={tgt:.4f} MeV   "
                  f"(baseline {baseline_rel*100:.2f}%)")
            print()
            print_target_at_params(G, L, lab, tgt, q, baseline_rel)
        print()


# ─── Main ───────────────────────────────────────────────────────────

def main():
    print("=" * 100)
    print("R60 Track 21 — Pion search over windings AND free geometric parameters")
    print("=" * 100)
    print()
    print("  Free variables considered:")
    print("    • n_max (per-axis winding limit; searched ∈ {6, 10, 15, 20})")
    print("    • (ε_p, s_p) proton-sheet shape (model-F inherits 0.55, 0.162")
    print("      from model-E; Tracks 5 and 8b show wide viable region under σ_ra).")
    print("  Fixed (structural or pinned):")
    print("    • (ε_e, s_e): pinned by R53 generations + R60 T17 exemption")
    print("    • s_ν = 0.022: fixed by Δm² ratio 33.6")
    print("    • ε_ν = 2.0 (R61 #1): negligible pion sensitivity")
    print("    • k = 1.1803/(8π): single-k structural fixed point (R60 T14)")
    print("    • σ_ta = √α, σ_at = 4πα, g_aa = 1: R59 F59 natural form")
    print("    • σ_ra = (sε)·σ_ta: auto-derived per sheet (R60 T7)")
    print()

    phase1_baseline_winding_sweep()
    per_target_best = phase2_parameter_sweep()
    phase3_winding_at_best(per_target_best)

    print("Track 21 complete.")


if __name__ == "__main__":
    main()
