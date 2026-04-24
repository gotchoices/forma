"""
R63 Track 5 — E-sheet fitness landscape under Q132 v2.

Re-renders the e-sheet (ε_e, s_e) sweep using the refined Q132
(v2) classifier.  Key differences from the v1 implementation:

  - Enumeration is no longer restricted to |n_et| ≤ 1.  Higher
    |n_et| modes are classified per v2 rules rather than forbidden
    at enumeration.
  - gcd-based classification: reduce (n_et, n_er) to its primitive
    (p_t, p_r) with gcd = 1.
      * primitive (0, p_r≠0)   → ring-only neutral (k copies)
      * primitive (p_t≠0, 0)   → tube-only neutral (k copies)
      * primitive (±1, p_r≠0)  → bright charged (k copies =
                                   k independent particles on the
                                   e-sheet, since e has no binding)
      * primitive (|p_t|>1, gcd=1) → DARK massive (phase-locked
                                      2π traversal fails; ω-sum = 0)
  - Ghost criterion under v2: a *bright primitive* charged mode
    whose mass is below the lightest observed same-|Q| particle.
    Given L_ring_e is calibrated to the electron at (1, 2), no
    bright primitive on the e-sheet can be below m_e, so the
    e-sheet is expected to be ghost-free at every grid point.
  - Discipline rule for charged predictions: every observed
    charged lepton should be predicted; no bright-primitive mode
    below the decay-into-observed threshold should be orphaned.
    Bright primitives *above* the decay threshold are routing-
    suppressed (R56/R57) and acceptable.

Outputs (../outputs/):
  - track5_fitness_q132v2.png        — fitness heat map
  - track5_counts_q132v2.png         — diagnostics: bright-gap,
                                        dark, multiples, ghost
  - track5_grid_q132v2.csv           — raw grid data
  - track5_dark_catalog_v2.csv       — dark-mode predictions at
                                        top shortlist grid points
"""

import sys, os
import math
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    L_vector_from_params, mode_energy, mode_6_to_11,
    signature_ok, M_E_MEV,
)
from track7b_resolve import build_aug_metric
from track1_proton_ghost_audit import match_observed, LIGHTEST_OBS
from track4_e_sheet_audit import (
    LEPTON_DATA, TARGETS, MAX_FITNESS,
    build_params_e, calibrate_L_ring_e,
    EPS_E_GRID, S_E_GRID, ENERGY_CAP_MEV,
    BASELINE_EPS_E, BASELINE_S_E,
)


# ─── Q132 v2 classifier ────────────────────────────────────────────

def gcd_primitive(n_t, n_r):
    """Return (k, p_t, p_r) with original = k × primitive, gcd(p_t, p_r) = 1.

    Sign convention: the primitive carries the sign of the original.
    Edge cases: (0, 0) returns (0, 0, 0).
    """
    if n_t == 0 and n_r == 0:
        return (0, 0, 0)
    g = math.gcd(abs(n_t), abs(n_r))
    return (g, n_t // g, n_r // g)


def classify_q132_v2(n_t, n_r):
    """Classify (n_t, n_r) under Q132 v2.

    Returns dict with keys:
      category:  'null' | 'ring-only' | 'tube-only'
                 | 'bright-charged' | 'dark-massive'
      k:         multiplicity (gcd-reduction count)
      p_t, p_r:  primitive winding numbers
      Q_per:     charge per bright copy (0 for non-bright)
      Q_total:   Q_per × k for bright, 0 otherwise
    """
    if n_t == 0 and n_r == 0:
        return dict(category='null', k=0, p_t=0, p_r=0, Q_per=0, Q_total=0)
    k, p_t, p_r = gcd_primitive(n_t, n_r)
    if p_t == 0:
        return dict(category='ring-only', k=k, p_t=0, p_r=p_r, Q_per=0, Q_total=0)
    if p_r == 0:
        return dict(category='tube-only', k=k, p_t=p_t, p_r=0, Q_per=0, Q_total=0)
    if abs(p_t) == 1:
        # Bright primitive: one tube event with ring at integer phase.
        # Q convention on the e-sheet: electron (1, 2) has Q = -1, so
        # Q_per = -p_t for the e-sheet.  (For other sheets the sign is
        # adjusted per sheet convention when used in compounds.)
        Q_per = -p_t
        return dict(category='bright-charged', k=k, p_t=p_t, p_r=p_r,
                    Q_per=Q_per, Q_total=Q_per * k)
    # |p_t| > 1, gcd = 1 → ω-sum cancels
    return dict(category='dark-massive', k=k, p_t=p_t, p_r=p_r, Q_per=0, Q_total=0)


# ─── Enumeration (no |n_et| restriction under v2) ──────────────────

def enumerate_e_modes_v2(G, L, n_et_max=4, n_er_max=30):
    """Enumerate pure e-sheet modes and classify each under v2.

    |n_et| ≤ n_et_max (default 4 covers the (n, 2n) tower through
    (4, 8) and the gcd=1 examples like (2, 3), (3, 2), (3, 5), (5, 2)
    that become dark under v2).  Anti-particle dedup: keep one of
    each (n_et, n_er) ↔ (-n_et, -n_er) pair.
    """
    results = []
    for n_et in range(-n_et_max, n_et_max + 1):
        for n_er in range(-n_er_max, n_er_max + 1):
            if n_et == 0 and n_er == 0:
                continue
            n6 = (n_et, n_er, 0, 0, 0, 0)
            n11 = mode_6_to_11(n6)
            E = mode_energy(G, L, n11)
            if E > ENERGY_CAP_MEV:
                continue
            cls = classify_q132_v2(n_et, n_er)
            results.append({
                'n_et': n_et, 'n_er': n_er, 'E': E, **cls,
            })
    # Anti-particle dedup by (E rounded, |Q_total|)
    seen = set()
    deduped = []
    for r in sorted(results, key=lambda x: (x['E'], abs(x['n_et']), abs(x['n_er']))):
        key = (round(r['E'], 4), abs(r['Q_total']), r['category'], r['k'])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)
    deduped.sort(key=lambda x: x['E'])
    return deduped


# ─── Per-mode sub-classification against observed inventory ────────

def subclassify_mode(m):
    """Return ('matched'|'bright-gap'|'bright-ghost'|'dark'|'multiple'|'neutral-mass', detail).

    - 'matched':     bright primitive (k=1) matches an observed
                     charged particle within its threshold.
    - 'bright-gap':  bright primitive (k=1), unmatched, above
                     lightest observed same-|Q| (routing-split-
                     dominated per R56/R57 — acceptable).
    - 'bright-ghost': bright primitive (k=1), unmatched, below
                     lightest observed same-|Q| — a real ghost
                     (should not appear under v2 with proper
                     calibration).
    - 'multiple':    bright with k > 1; interpreted as k free
                     primitive copies on the unbinding e-sheet.
                     Not a new particle; carries the primitive's
                     sub-classification.
    - 'dark':        dark-massive (gcd=1, |p_t|>1) — mass-only.
    - 'neutral-mass': ring-only or tube-only neutral.
    """
    cat = m['category']
    if cat in ('ring-only', 'tube-only'):
        return 'neutral-mass', f"{cat}, mass = {m['E']:.3f} MeV"
    if cat == 'dark-massive':
        return 'dark', f"primitive ({m['p_t']:+d},{m['p_r']:+d}), mass = {m['E']:.3f} MeV"
    if cat == 'bright-charged':
        # Match against observed
        mm = match_observed(m['E'], m['Q_per'])
        if m['k'] == 1:
            if mm:
                p, rel, thr = mm
                return 'matched', f"{p.name} (Δm/m = {rel*100:+.2f}%)"
            lightest = LIGHTEST_OBS.get(abs(m['Q_per']))
            if lightest is not None and m['E'] < lightest:
                return 'bright-ghost', \
                       f"primitive charged at {m['E']:.3f}; lightest observed |Q|=1 is {lightest:.3f} MeV"
            return 'bright-gap', f"primitive charged, {m['E']:.3f} MeV"
        # k > 1
        # Per v2 on the no-binding e-sheet, this is k independent
        # primitives.  Inherit the primitive's match result.
        return 'multiple', \
               f"{m['k']} × primitive ({m['p_t']:+d},{m['p_r']:+d}) (each at {m['E']/m['k']:.3f} MeV)"
    return 'unknown', ''


# ─── Per-point computation ─────────────────────────────────────────

def compute_point(eps_e, s_e, return_modes=False):
    L_e = calibrate_L_ring_e(eps_e, s_e)
    if L_e is None or L_e <= 0 or L_e != L_e:
        return (float('nan'),) * 5 + (None,)
    params = build_params_e(eps_e, s_e, L_e)
    G = build_aug_metric(params)
    if not signature_ok(G):
        return (float('nan'),) * 5 + (None,)
    L = L_vector_from_params(params)

    modes = enumerate_e_modes_v2(G, L)

    counts = dict(ghost=0, gap=0, dark=0, neutral=0, matched=0, multiple=0)
    for m in modes:
        sub, _ = subclassify_mode(m)
        if sub == 'bright-ghost':
            counts['ghost'] += 1
        elif sub == 'bright-gap':
            counts['gap'] += 1
        elif sub == 'dark':
            counts['dark'] += 1
        elif sub == 'neutral-mass':
            counts['neutral'] += 1
        elif sub == 'matched':
            counts['matched'] += 1
        elif sub == 'multiple':
            counts['multiple'] += 1

    # Fitness against the three charged leptons.  Only primitive
    # bright matches count; multiples and darks do not contribute.
    fitness = 0.0
    for (name, mass, absQ, thr) in TARGETS:
        best_rel = None
        for m in modes:
            if m['category'] != 'bright-charged' or m['k'] != 1:
                continue
            if abs(m['Q_per']) != absQ:
                continue
            rel = abs(m['E'] - mass) / mass
            if best_rel is None or rel < best_rel:
                best_rel = rel
        if best_rel is not None:
            fitness += max(0.0, 1.0 - best_rel / thr)

    if return_modes:
        return (fitness, counts['ghost'], counts['gap'],
                counts['dark'], counts['multiple'], modes)
    return (fitness, counts['ghost'], counts['gap'],
            counts['dark'], counts['multiple'], None)


# ─── Phase A: audit at R53 Solution D under v2 ────────────────────

def phase_a_audit():
    print("=" * 100)
    print("R63 Track 5 — PHASE A: E-sheet audit at R53 Solution D under Q132 v2")
    print("=" * 100)
    print()

    eps_e, s_e = BASELINE_EPS_E, BASELINE_S_E
    fitness, gh, gap, dk, mult, modes = compute_point(eps_e, s_e, return_modes=True)

    print(f"  Baseline: ε_e = {eps_e}, s_e = {s_e}")
    print(f"  Fitness (3-lepton, width-weighted): {fitness:.3f} / {MAX_FITNESS:.1f}")
    print(f"  Classification counts at baseline:")
    print(f"    bright-ghost (primitive < lightest observed):  {gh}")
    print(f"    bright-gap (primitive unmatched, split-suppressed):  {gap}")
    print(f"    dark (primitive |p_t|>1, gcd=1):  {dk}")
    print(f"    multiple (k > 1 copies of primitive):  {mult}")
    print()

    print("  Mode listing at R53 Solution D (top 40 by mass):")
    print(f"    {'E (MeV)':>10s}  {'(n_t,n_r)':>10s}  {'k':>3s}  "
          f"{'prim':>10s}  {'Q':>3s}  {'category':<18s}  detail")
    print("    " + "─" * 120)
    for m in modes[:40]:
        sub, detail = subclassify_mode(m)
        tup = f"({m['n_et']:+d},{m['n_er']:+d})"
        prim = f"({m['p_t']:+d},{m['p_r']:+d})" if m['category'] != 'null' else '—'
        marker = {'matched': '✓', 'bright-gap': '·', 'bright-ghost': '⚠',
                  'multiple': '×', 'dark': '◌', 'neutral-mass': '◦'}.get(sub, '?')
        print(f"    {m['E']:>10.4f}  {tup:>10s}  {m['k']:>3d}  "
              f"{prim:>10s}  {m['Q_per']:>+3d}  {sub:<18s}  {detail}  {marker}")
    if len(modes) > 40:
        print(f"    ... {len(modes) - 40} more modes below {ENERGY_CAP_MEV:.0f} MeV")
    print()

    print("  Lepton fits (bright primitives only):")
    for (name, mass, absQ, thr) in TARGETS:
        best = None
        for m in modes:
            if m['category'] != 'bright-charged' or m['k'] != 1:
                continue
            if abs(m['Q_per']) != absQ:
                continue
            rel = abs(m['E'] - mass) / mass
            if best is None or rel < best[0]:
                best = (rel, m)
        if best is None:
            print(f"    {name:>3s}: NO PRIMITIVE CHARGED MATCH")
        else:
            rel, m = best
            tup = f"({m['n_et']:+d},{m['n_er']:+d})"
            close = max(0.0, 1.0 - rel / thr)
            flag = '✓' if close > 0 else '✗'
            print(f"    {name:>3s} (target {mass:>8.3f}, thr {thr*100:.1f}%): "
                  f"{tup:>10s} at {m['E']:>9.3f}  "
                  f"Δm/m = {rel*100:>+6.3f}%  close = {close:.3f}  {flag}")
    print()

    # Ghost list (if any)
    ghosts = [m for m in modes if subclassify_mode(m)[0] == 'bright-ghost']
    if ghosts:
        print(f"  ⚠  BRIGHT GHOSTS at baseline ({len(ghosts)}):")
        for m in ghosts:
            _, d = subclassify_mode(m)
            tup = f"({m['n_et']:+d},{m['n_er']:+d})"
            print(f"    {tup:>10s}  {d}")
    else:
        print("  ✓  No bright-primitive ghosts at baseline.")
    print()

    # Bright-gap inventory (charged predictions with no observed match)
    gaps = [m for m in modes if subclassify_mode(m)[0] == 'bright-gap']
    print(f"  Bright-gap modes (charged, unmatched, routing-suppressed): {len(gaps)}")
    for m in gaps[:10]:
        tup = f"({m['n_et']:+d},{m['n_er']:+d})"
        print(f"    {tup:>10s}  {m['E']:>9.3f} MeV  Q = {m['Q_per']:+d}")
    if len(gaps) > 10:
        print(f"    ... {len(gaps) - 10} more")
    print()

    return fitness


# ─── Phase B: grid sweep under v2 ──────────────────────────────────

def phase_b_sweep():
    print("=" * 100)
    print("R63 Track 5 — PHASE B: (ε_e, s_e) grid sweep under Q132 v2")
    print("=" * 100)
    print()
    print(f"  Grid: {len(EPS_E_GRID)} × {len(S_E_GRID)} "
          f"= {len(EPS_E_GRID)*len(S_E_GRID)} points")
    print()

    n_s, n_e = len(S_E_GRID), len(EPS_E_GRID)
    fitness = np.zeros((n_s, n_e))
    ghosts  = np.zeros((n_s, n_e), dtype=int)
    gaps    = np.zeros((n_s, n_e), dtype=int)
    darks   = np.zeros((n_s, n_e), dtype=int)
    mults   = np.zeros((n_s, n_e), dtype=int)

    t0 = time.time()
    for i, s_e in enumerate(S_E_GRID):
        for j, eps_e in enumerate(EPS_E_GRID):
            f, g, ga, d, mu, _ = compute_point(eps_e, s_e)
            def _safe(x): return x if not (isinstance(x, float) and math.isnan(x)) else 0
            fitness[i, j] = _safe(f)
            ghosts[i, j]  = _safe(g)
            gaps[i, j]    = _safe(ga)
            darks[i, j]   = _safe(d)
            mults[i, j]   = _safe(mu)
        if (i + 1) % 10 == 0 or i == n_s - 1:
            elapsed = time.time() - t0
            print(f"  s_e = {s_e:.4f}  done  "
                  f"({(i+1)*n_e:>5d} / {n_s*n_e}, {elapsed:.1f}s elapsed)")
    print()

    n_total = fitness.size
    n_ghost_free = int(np.sum(ghosts == 0))
    print(f"  Ghost-free points:  {n_ghost_free} / {n_total}  "
          f"({100*n_ghost_free/n_total:.0f}%)")

    Z_search = np.where(ghosts == 0, fitness, -np.inf)
    idx = np.unravel_index(np.argmax(Z_search), Z_search.shape)
    i_max, j_max = idx
    print(f"  Peak fitness (ghost-free):  {fitness[i_max, j_max]:.3f} / "
          f"{MAX_FITNESS:.1f}")
    print(f"    at (ε_e = {EPS_E_GRID[j_max]:.3f}, s_e = {S_E_GRID[i_max]:.4f})")

    ii = np.argmin(np.abs(S_E_GRID - BASELINE_S_E))
    jj = np.argmin(np.abs(EPS_E_GRID - BASELINE_EPS_E))
    print(f"  Baseline grid neighbor: fitness = {fitness[ii, jj]:.3f} "
          f"(closest to ε={BASELINE_EPS_E}, s={BASELINE_S_E})")
    print()

    print("  Top 10 ghost-free points:")
    flat_idx = np.argsort(Z_search.ravel())[::-1][:10]
    print(f"    {'ε_e':>8}  {'s_e':>8}  {'fitness':>8}  "
          f"{'gaps':>5}  {'dark':>5}  {'mult':>5}")
    for idx_flat in flat_idx:
        i, j = np.unravel_index(idx_flat, Z_search.shape)
        print(f"    {EPS_E_GRID[j]:>8.3f}  {S_E_GRID[i]:>8.4f}  "
              f"{fitness[i, j]:>8.3f}  "
              f"{gaps[i, j]:>5d}  {darks[i, j]:>5d}  {mults[i, j]:>5d}")
    print()

    return fitness, ghosts, gaps, darks, mults


# ─── Plots ─────────────────────────────────────────────────────────

def save_fitness_heatmap(fitness, ghosts, out_path):
    fig, ax = plt.subplots(figsize=(12, 8))
    E_grid, S_grid = np.meshgrid(EPS_E_GRID, S_E_GRID)

    mask = (ghosts > 0)
    fit_masked = np.where(mask, np.nan, fitness)

    pcm = ax.pcolormesh(E_grid, S_grid, fit_masked, cmap='viridis',
                        vmin=0, vmax=MAX_FITNESS, shading='auto')
    if mask.any():
        m = mask.astype(float)
        ax.contourf(E_grid, S_grid, m, levels=[0.5, 1.5],
                    colors='none', hatches=['////'])
        ax.contourf(E_grid, S_grid, m, levels=[0.5, 1.5],
                    colors=['#888888'], alpha=0.25)

    levels = [0.5, 1.0, 1.5, 2.0, 2.5]
    cs = ax.contour(E_grid, S_grid, fit_masked, levels=levels,
                    colors='white', linewidths=0.8, alpha=0.7)
    ax.clabel(cs, inline=True, fontsize=8, fmt='%.1f')

    ax.plot(BASELINE_EPS_E, BASELINE_S_E, '*', color='orange', markersize=18,
            markeredgecolor='black', markeredgewidth=0.8,
            label=f'R53 Solution D ({BASELINE_EPS_E}, {BASELINE_S_E:.4f})')
    ax.axhline(y=2.0, color='red', linestyle=':', linewidth=1.2,
               label='shear resonance s_e = 2')

    Z_search = np.where(ghosts == 0, fitness, -np.inf)
    idx = np.unravel_index(np.argmax(Z_search), Z_search.shape)
    i_max, j_max = idx
    ax.plot(EPS_E_GRID[j_max], S_E_GRID[i_max], 'o',
            color='white', markerfacecolor='red', markersize=10,
            markeredgewidth=1.5)
    ax.annotate(
        f"peak: ({EPS_E_GRID[j_max]:.1f}, {S_E_GRID[i_max]:.4f})\n"
        f"fit = {fitness[i_max, j_max]:.2f} / {MAX_FITNESS:.0f}",
        xy=(EPS_E_GRID[j_max], S_E_GRID[i_max]),
        xytext=(EPS_E_GRID[j_max] * 1.2, S_E_GRID[i_max] + 0.02),
        fontsize=10, arrowprops=dict(arrowstyle='->', color='red'))

    ax.set_xscale('log')
    ax.set_xlabel('ε_e  (log scale)')
    ax.set_ylabel('s_e')
    ax.set_title(
        "R63 Track 5 — E-sheet fitness landscape under Q132 v2\n"
        "gcd decomposition; primitive bright charges matched against observed leptons")

    plt.colorbar(pcm, ax=ax, label='fitness (max 3: e + μ + τ)')
    legend_patches = [
        Patch(facecolor='none', edgecolor='black', hatch='////',
              label='bright-primitive ghost (below lightest observed)'),
    ]
    ax.legend(handles=legend_patches + ax.get_legend_handles_labels()[0],
              loc='lower right', framealpha=0.9, fontsize=9)
    ax.set_xlim(EPS_E_GRID[0], EPS_E_GRID[-1])
    ax.set_ylim(S_E_GRID[0], S_E_GRID[-1])
    ax.grid(alpha=0.2, which='both')
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def save_counts_plot(gaps, darks, mults, ghosts, out_path):
    fig, axes = plt.subplots(2, 2, figsize=(18, 12))
    E_grid, S_grid = np.meshgrid(EPS_E_GRID, S_E_GRID)

    panels = [
        (axes[0, 0], gaps,   "Bright-gap primitives (routing-suppressed)", "Oranges"),
        (axes[0, 1], darks,  "Dark-massive (phase-cancelled)",             "Purples"),
        (axes[1, 0], mults,  "Multiple-copy bright modes (k > 1)",         "Blues"),
        (axes[1, 1], ghosts, "Bright-primitive ghosts (discipline check)", "Reds"),
    ]
    for ax, Z, title, cmap in panels:
        vmax = max(1, int(Z.max()))
        pcm = ax.pcolormesh(E_grid, S_grid, Z, cmap=cmap,
                            vmin=0, vmax=vmax, shading='auto')
        ax.plot(BASELINE_EPS_E, BASELINE_S_E, '*', color='lime', markersize=14,
                markeredgecolor='black', label='R53 Solution D')
        ax.axhline(y=2.0, color='red', linestyle=':', linewidth=1.0)
        ax.set_xscale('log')
        ax.set_xlabel('ε_e (log)')
        ax.set_ylabel('s_e')
        ax.set_title(title)
        plt.colorbar(pcm, ax=ax, label='count')
        ax.legend(loc='lower right')
        ax.grid(alpha=0.2)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def save_csv(fitness, ghosts, gaps, darks, mults, out_path):
    with open(out_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['eps_e', 's_e', 'fitness', 'ghosts', 'gaps', 'darks', 'multiples'])
        for i, s_e in enumerate(S_E_GRID):
            for j, eps_e in enumerate(EPS_E_GRID):
                w.writerow([f"{eps_e:.4f}", f"{s_e:.4f}",
                            f"{fitness[i, j]:.4f}",
                            int(ghosts[i, j]), int(gaps[i, j]),
                            int(darks[i, j]), int(mults[i, j])])


def save_dark_catalog(fitness, ghosts, out_path):
    Z_search = np.where(ghosts == 0, fitness, -np.inf)
    flat_idx = np.argsort(Z_search.ravel())[::-1][:5]
    with open(out_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['rank', 'eps_e', 's_e', 'fitness', 'mode',
                    'primitive', 'k', 'mass_MeV', 'category'])
        for rank, idx_flat in enumerate(flat_idx, 1):
            i, j = np.unravel_index(idx_flat, Z_search.shape)
            eps_e = EPS_E_GRID[j]
            s_e = S_E_GRID[i]
            fit = fitness[i, j]
            _, _, _, _, _, modes = compute_point(eps_e, s_e, return_modes=True)
            for m in modes:
                sub, _ = subclassify_mode(m)
                if sub in ('dark', 'neutral-mass'):
                    tup = f"({m['n_et']:+d},{m['n_er']:+d})"
                    prim = f"({m['p_t']:+d},{m['p_r']:+d})"
                    w.writerow([rank, f"{eps_e:.4f}", f"{s_e:.4f}",
                                f"{fit:.3f}", tup, prim, m['k'],
                                f"{m['E']:.3f}", m['category']])


# ─── Main ──────────────────────────────────────────────────────────

def main():
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(out_dir, exist_ok=True)

    phase_a_audit()
    fitness, ghosts, gaps, darks, mults = phase_b_sweep()

    print("  Writing outputs:")
    out_fit   = os.path.join(out_dir, 'track5_fitness_q132v2.png')
    out_cnt   = os.path.join(out_dir, 'track5_counts_q132v2.png')
    out_csv   = os.path.join(out_dir, 'track5_grid_q132v2.csv')
    out_dark  = os.path.join(out_dir, 'track5_dark_catalog_v2.csv')

    save_fitness_heatmap(fitness, ghosts, out_fit)
    print(f"    ✓ {out_fit}")
    save_counts_plot(gaps, darks, mults, ghosts, out_cnt)
    print(f"    ✓ {out_cnt}")
    save_csv(fitness, ghosts, gaps, darks, mults, out_csv)
    print(f"    ✓ {out_csv}")
    save_dark_catalog(fitness, ghosts, out_dark)
    print(f"    ✓ {out_dark}")
    print()


if __name__ == "__main__":
    main()
