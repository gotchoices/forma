"""
R63 Track 5 — E-sheet fitness landscape under Q132.

Re-renders Track 4's grid sweep using the Q132 promotion-chain
principle: |n_tube| = ±1 per particle-creation event; a mode with
tube-but-no-ring (or ring-but-no-tube) is a valid neutral particle
with self-generated mass, not a ghost.  Under Q132 the ghost mask
that dominated Track 4 largely disappears — the lepton-fit
topography that was hidden becomes visible.

Under Q132 rules:
  - enumeration is restricted to |n_et| ∈ {−1, 0, +1} (multi-event
    modes are forbidden, not ghosts — they don't exist as particles);
  - effective charge: Q = −n_et only when BOTH n_et and n_er are
    nonzero (full promotion chain); otherwise Q = 0 (neutral);
  - (0, n_r≠0) → valid neutral (ring-trapped photon);
  - (±1, 0) → valid neutral (tube-only self-mass);
  - (±1, n_r≠0) → valid charged particle (full chain).

Outputs (in ../outputs/):
  - track5_fitness_q132.png         — primary heat map
  - track5_counts_q132.png          — diagnostic (dark-count, charged-gap)
  - track5_grid_q132.csv            — raw grid data
  - track5_dark_catalog.csv         — predicted neutral modes at each grid
                                        point inside the ghost-free region
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


# ─── Q132 charge + enumeration ─────────────────────────────────────

def q132_charge(n_et, n_er):
    """Q132 effective charge.

    Full promotion chain requires BOTH a ring trap (mass) AND a
    tube 2π closure (charge).  If either is missing, the mode is
    neutral.
    """
    if n_et == 0 or n_er == 0:
        return 0
    return -n_et


def enumerate_e_modes_q132(G, L, n_er_max=30):
    """Q132-compliant pure e-sheet enumeration: |n_et| ≤ 1."""
    results = []
    for n_et in (-1, 0, 1):
        for n_er in range(-n_er_max, n_er_max + 1):
            if n_et == 0 and n_er == 0:
                continue
            n6 = (n_et, n_er, 0, 0, 0, 0)
            n11 = mode_6_to_11(n6)
            E = mode_energy(G, L, n11)
            if E > ENERGY_CAP_MEV:
                continue
            Q_eff = q132_charge(n_et, n_er)
            results.append({
                'n_et': n_et, 'n_er': n_er, 'E': E, 'Q_eff': Q_eff,
            })
    # Deduplicate antiparticle pairs: (n_et, n_er) and (−n_et, −n_er)
    # are C-conjugates at the same energy.
    seen = set()
    deduped = []
    for r in sorted(results, key=lambda x: (x['E'], abs(x['n_et']), abs(x['n_er']))):
        key = (round(r['E'], 4), abs(r['Q_eff']))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)
    deduped.sort(key=lambda x: x['E'])
    return deduped


# ─── Q132 classification ──────────────────────────────────────────

def classify_q132(E, n_et, n_er, Q_eff):
    """Classify under Q132.  Returns (category, detail)."""
    m = match_observed(E, Q_eff)
    if m:
        p, rel, thr = m
        return 'observed', f"{p.name} (Δm/m = {rel*100:+.2f}%)"

    if n_et == 0 and n_er != 0:
        return 'dark-ring-only', f"neutral, mass = {E:.2f} MeV"
    if n_et != 0 and n_er == 0:
        return 'dark-tube-only', f"neutral, mass = {E:.2f} MeV"

    if abs(n_et) == 1 and n_er != 0:
        lightest = LIGHTEST_OBS.get(abs(Q_eff))
        if lightest is not None and E < lightest:
            return 'ghost-sub-observed', \
                   f"predicted charged at {E:.3f}; lightest observed |Q|=1 is {lightest:.3f} MeV"
        return 'charged-gap', f"charged, unmatched, {E:.2f} MeV"

    return 'unknown', ''


# ─── Per-point computation ─────────────────────────────────────────

def compute_point_q132(eps_e, s_e, return_modes=False):
    L_e = calibrate_L_ring_e(eps_e, s_e)
    if L_e is None or L_e <= 0 or L_e != L_e:
        return (float('nan'),) * 4 + (None,)
    params = build_params_e(eps_e, s_e, L_e)
    G = build_aug_metric(params)
    if not signature_ok(G):
        return (float('nan'),) * 4 + (None,)
    L = L_vector_from_params(params)

    modes = enumerate_e_modes_q132(G, L)

    ghost_count = 0
    dark_count = 0
    charged_gap = 0
    for m in modes:
        cls, _ = classify_q132(m['E'], m['n_et'], m['n_er'], m['Q_eff'])
        if cls == 'ghost-sub-observed':
            ghost_count += 1
        elif cls.startswith('dark'):
            dark_count += 1
        elif cls == 'charged-gap':
            charged_gap += 1

    # Fitness: match e, μ, τ among charged modes only
    fitness = 0.0
    for (name, mass, absQ, thr) in TARGETS:
        best_rel = None
        for m in modes:
            if abs(m['Q_eff']) != absQ:
                continue
            rel = abs(m['E'] - mass) / mass
            if best_rel is None or rel < best_rel:
                best_rel = rel
        if best_rel is not None:
            fitness += max(0.0, 1.0 - best_rel / thr)

    if return_modes:
        return (fitness, ghost_count, dark_count, charged_gap, modes)
    return (fitness, ghost_count, dark_count, charged_gap, None)


# ─── Phase A: audit at R53 Solution D under Q132 ──────────────────

def phase_a_audit():
    print("=" * 100)
    print("R63 Track 5 — PHASE A: E-sheet audit at R53 Solution D under Q132")
    print("=" * 100)
    print()

    eps_e, s_e = BASELINE_EPS_E, BASELINE_S_E
    fitness, ghosts, darks, charged_gap, modes = compute_point_q132(
        eps_e, s_e, return_modes=True)

    print(f"  Baseline: ε_e = {eps_e}, s_e = {s_e}")
    print(f"  Fitness (3-lepton, width-weighted): {fitness:.3f} / {MAX_FITNESS:.1f}")
    print(f"  Mode classification:")
    print(f"    ghost-sub-observed:  {ghosts}")
    print(f"    dark (valid predicted neutral): {darks}")
    print(f"    charged-gap (unmatched):        {charged_gap}")
    print()

    print("  Top 30 modes at R53 Solution D under Q132:")
    print(f"    {'E (MeV)':>10s}  {'(n_et,n_er)':>12s}  {'Q132':>4s}  "
          f"{'category':<22s}  detail")
    print("    " + "─" * 108)
    for m in modes[:30]:
        cls, detail = classify_q132(m['E'], m['n_et'], m['n_er'], m['Q_eff'])
        tup = f"({m['n_et']:+d},{m['n_er']:+d})"
        marker = {'observed': '✓',
                  'ghost-sub-observed': '⚠',
                  'dark-ring-only': '◦',
                  'dark-tube-only': '◦',
                  'charged-gap': '·'}.get(cls, '?')
        print(f"    {m['E']:>10.4f}  {tup:>12s}  {m['Q_eff']:>+4d}  "
              f"{cls:<22s}  {detail}  {marker}")
    if len(modes) > 30:
        print(f"    ... and {len(modes) - 30} more below {ENERGY_CAP_MEV:.0f} MeV")
    print()

    print("  Predicted DARK modes at baseline (neutral candidates):")
    dark_modes = [m for m in modes if classify_q132(
        m['E'], m['n_et'], m['n_er'], m['Q_eff'])[0].startswith('dark')]
    for m in dark_modes[:15]:
        tup = f"({m['n_et']:+d},{m['n_er']:+d})"
        dark_type = 'ring-only' if m['n_et'] == 0 else 'tube-only'
        print(f"    {m['E']:>10.4f}  {tup:>12s}  {dark_type}")
    if len(dark_modes) > 15:
        print(f"    ... and {len(dark_modes) - 15} more dark modes")
    print()

    print("  Lepton-specific fits (Q132-filtered):")
    for (name, mass, absQ, thr) in TARGETS:
        best = None
        for m in modes:
            if abs(m['Q_eff']) != absQ:
                continue
            rel = abs(m['E'] - mass) / mass
            if best is None or rel < best[0]:
                best = (rel, m)
        if best is None:
            print(f"    {name:>3s}: NO CHARGED MATCH")
        else:
            rel, m = best
            tup = f"({m['n_et']:+d},{m['n_er']:+d})"
            close = max(0.0, 1.0 - rel / thr)
            flag = '✓' if close > 0 else '✗'
            print(f"    {name:>3s} (target {mass:>8.3f}, thr {thr*100:.1f}%): "
                  f"best = {tup:>12s} at {m['E']:>9.3f}  "
                  f"Δm/m = {rel*100:>+6.3f}%  close = {close:.3f}  {flag}")
    print()
    return fitness


# ─── Phase B: grid sweep under Q132 ────────────────────────────────

def phase_b_sweep():
    print("=" * 100)
    print("R63 Track 5 — PHASE B: (ε_e, s_e) grid sweep under Q132")
    print("=" * 100)
    print()
    print(f"  Grid: {len(EPS_E_GRID)} × {len(S_E_GRID)} "
          f"= {len(EPS_E_GRID)*len(S_E_GRID)} points "
          f"(same as Track 4; Q132 classifier)")
    print()

    n_s = len(S_E_GRID)
    n_e = len(EPS_E_GRID)
    fitness = np.zeros((n_s, n_e))
    ghosts  = np.zeros((n_s, n_e), dtype=int)
    darks   = np.zeros((n_s, n_e), dtype=int)
    gaps    = np.zeros((n_s, n_e), dtype=int)

    t0 = time.time()
    for i, s_e in enumerate(S_E_GRID):
        for j, eps_e in enumerate(EPS_E_GRID):
            f, g, d, c, _ = compute_point_q132(eps_e, s_e)
            fitness[i, j] = f if not (isinstance(f, float) and math.isnan(f)) else 0.0
            ghosts[i, j]  = g if not (isinstance(g, float) and math.isnan(g)) else -1
            darks[i, j]   = d if not (isinstance(d, float) and math.isnan(d)) else -1
            gaps[i, j]    = c if not (isinstance(c, float) and math.isnan(c)) else -1
        elapsed = time.time() - t0
        if (i + 1) % 10 == 0 or i == n_s - 1:
            print(f"  s_e = {s_e:.4f}  done  "
                  f"({(i+1)*n_e:>5d} / {n_s*n_e}, {elapsed:.1f}s elapsed)")
    print()

    # Summary
    n_total = fitness.size
    n_ghost_free = int(np.sum(ghosts == 0))
    print(f"  Ghost-free points (no sub-observed charged ghosts):  "
          f"{n_ghost_free} / {n_total}  ({100*n_ghost_free/n_total:.0f}%)")

    Z_search = np.where(ghosts == 0, fitness, -np.inf)
    idx = np.unravel_index(np.argmax(Z_search), Z_search.shape)
    i_max, j_max = idx
    print(f"  Peak fitness (ghost-free):  {fitness[i_max, j_max]:.3f} / "
          f"{MAX_FITNESS:.1f}")
    print(f"    at (ε_e = {EPS_E_GRID[j_max]:.3f}, s_e = {S_E_GRID[i_max]:.4f})")

    # Baseline fitness (at R53 Solution D)
    # find closest grid point
    ii = np.argmin(np.abs(S_E_GRID - BASELINE_S_E))
    jj = np.argmin(np.abs(EPS_E_GRID - BASELINE_EPS_E))
    print(f"  Baseline grid point: fitness = {fitness[ii, jj]:.3f} "
          f"(at grid closest to {BASELINE_EPS_E}, {BASELINE_S_E})")
    print()

    print("  Top 10 ghost-free points:")
    flat_idx = np.argsort(Z_search.ravel())[::-1][:10]
    print(f"    {'ε_e':>8}  {'s_e':>8}  {'fitness':>8}  {'darks':>6}  {'gaps':>6}")
    for idx_flat in flat_idx:
        i, j = np.unravel_index(idx_flat, Z_search.shape)
        print(f"    {EPS_E_GRID[j]:>8.3f}  {S_E_GRID[i]:>8.4f}  "
              f"{fitness[i, j]:>8.3f}  {darks[i, j]:>6d}  {gaps[i, j]:>6d}")
    print()

    return fitness, ghosts, darks, gaps


# ─── Plotting ──────────────────────────────────────────────────────

def save_fitness_heatmap(fitness, ghosts, out_path):
    fig, ax = plt.subplots(figsize=(12, 8))
    E_grid, S_grid = np.meshgrid(EPS_E_GRID, S_E_GRID)

    # Ghost mask (sub-observed charged only — should be nearly empty)
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

    # Contour lines
    levels = [0.5, 1.0, 1.5, 2.0, 2.5]
    cs = ax.contour(E_grid, S_grid, fit_masked, levels=levels,
                    colors='white', linewidths=0.8, alpha=0.7)
    ax.clabel(cs, inline=True, fontsize=8, fmt='%.1f')

    # Baseline
    ax.plot(BASELINE_EPS_E, BASELINE_S_E, '*', color='orange', markersize=18,
            markeredgecolor='black', markeredgewidth=0.8,
            label=f'R53 Solution D ({BASELINE_EPS_E}, {BASELINE_S_E:.4f})')

    # Shear resonance line
    ax.axhline(y=2.0, color='red', linestyle=':', linewidth=1.2,
               label='shear resonance s_e = 2 (for (1,2))')

    # Peak marker
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
        fontsize=10,
        arrowprops=dict(arrowstyle='->', color='red'))

    ax.set_xscale('log')
    ax.set_xlabel('ε_e  (e-sheet aspect ratio, log scale)')
    ax.set_ylabel('s_e  (e-sheet shear)')
    ax.set_title(
        "R63 Track 5 — E-sheet fitness landscape under Q132\n"
        "promotion-chain classification: (0, n_r) and (1, 0) are valid "
        "neutral predictions, not ghosts")

    cbar = plt.colorbar(pcm, ax=ax, label='fitness (max 3: e + μ + τ all exact)')

    legend_patches = [
        Patch(facecolor='none', edgecolor='black', hatch='////',
              label='sub-observed charged ghost (under Q132: rare)'),
    ]
    ax.legend(handles=legend_patches + ax.get_legend_handles_labels()[0],
              loc='lower right', framealpha=0.9, fontsize=9)

    ax.set_xlim(EPS_E_GRID[0], EPS_E_GRID[-1])
    ax.set_ylim(S_E_GRID[0], S_E_GRID[-1])
    ax.grid(alpha=0.2, which='both')

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def save_counts_plot(darks, gaps, ghosts, out_path):
    """Diagnostic: dark count, charged-gap count, ghost count."""
    fig, axes = plt.subplots(1, 3, figsize=(24, 7))
    E_grid, S_grid = np.meshgrid(EPS_E_GRID, S_E_GRID)

    for ax, Z, title, cmap in [
        (axes[0], darks, "Dark-mode predictions (valid neutral)", "Blues"),
        (axes[1], gaps, "Unmatched charged-gap modes", "Oranges"),
        (axes[2], ghosts, "Sub-observed charged ghosts (Q132)", "Reds"),
    ]:
        vmax = max(1, Z.max()) if Z.max() > 0 else 1
        pcm = ax.pcolormesh(E_grid, S_grid, Z, cmap=cmap,
                            vmin=0, vmax=vmax, shading='auto')
        ax.plot(BASELINE_EPS_E, BASELINE_S_E, '*', color='blue', markersize=14,
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


def save_csv(fitness, ghosts, darks, gaps, out_path):
    with open(out_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['eps_e', 's_e', 'fitness_q132', 'n_ghosts', 'n_dark', 'n_gap'])
        for i, s_e in enumerate(S_E_GRID):
            for j, eps_e in enumerate(EPS_E_GRID):
                w.writerow([f"{eps_e:.4f}", f"{s_e:.4f}",
                            f"{fitness[i, j]:.4f}",
                            int(ghosts[i, j]),
                            int(darks[i, j]),
                            int(gaps[i, j])])


def save_dark_catalog_at_peak(fitness, ghosts, out_path):
    """Catalog of dark-mode predictions at the peak and a few shortlist points."""
    Z_search = np.where(ghosts == 0, fitness, -np.inf)
    flat_idx = np.argsort(Z_search.ravel())[::-1][:5]

    with open(out_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['rank', 'eps_e', 's_e', 'fitness', 'mode_tup',
                    'mass_MeV', 'dark_type', 'Q132_Q'])
        for rank, idx_flat in enumerate(flat_idx, 1):
            i, j = np.unravel_index(idx_flat, Z_search.shape)
            eps_e = EPS_E_GRID[j]
            s_e = S_E_GRID[i]
            fit = fitness[i, j]
            _, _, _, _, modes = compute_point_q132(eps_e, s_e, return_modes=True)
            for m in modes:
                cls, _ = classify_q132(m['E'], m['n_et'], m['n_er'], m['Q_eff'])
                if cls.startswith('dark'):
                    dark_type = 'ring-only' if m['n_et'] == 0 else 'tube-only'
                    tup = f"({m['n_et']:+d},{m['n_er']:+d})"
                    w.writerow([rank, f"{eps_e:.4f}", f"{s_e:.4f}",
                                f"{fit:.3f}", tup, f"{m['E']:.3f}",
                                dark_type, m['Q_eff']])


# ─── Main ──────────────────────────────────────────────────────────

def main():
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(out_dir, exist_ok=True)

    # Phase A
    phase_a_audit()

    # Phase B
    fitness, ghosts, darks, gaps = phase_b_sweep()

    # Plots
    print("  Writing outputs:")
    out_fitness = os.path.join(out_dir, 'track5_fitness_q132.png')
    out_counts  = os.path.join(out_dir, 'track5_counts_q132.png')
    out_csv     = os.path.join(out_dir, 'track5_grid_q132.csv')
    out_darks   = os.path.join(out_dir, 'track5_dark_catalog.csv')

    save_fitness_heatmap(fitness, ghosts, out_fitness)
    print(f"    ✓ {out_fitness}")
    save_counts_plot(darks, gaps, ghosts, out_counts)
    print(f"    ✓ {out_counts}")
    save_csv(fitness, ghosts, darks, gaps, out_csv)
    print(f"    ✓ {out_csv}")
    save_dark_catalog_at_peak(fitness, ghosts, out_darks)
    print(f"    ✓ {out_darks}")
    print()


if __name__ == "__main__":
    main()
