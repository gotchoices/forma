"""
R63 Track 3b — Pure p-sheet fitness heat map, width-weighted.

Phase B of Track 3: replace the flat 2%/14% thresholds with
physically-principled thresholds based on natural line width
(Γ = ℏ/τ).  A stable particle demands an exact match; a narrow
resonance demands near-exact; a broad resonance tolerates misses
up to ~2 natural widths.

Threshold definition per target particle:
    threshold = max(floor, k * Γ/m)
with floor = 0.02 (2% model precision) and k = 2 (allow 2 natural
line widths).

Only Δ⁺ has a natural width large enough to push its threshold
above the 2% floor (9.5% → 19% threshold).  Everything else has
its threshold set by the floor.  π⁰'s 14%-threshold concession
from Track 3 is dropped — its natural width is tiny.

Outputs (written to ../outputs/):
  - track3b_fitness_width.png       — width-weighted heat map
  - track3b_comparison.png          — side-by-side with original
  - track3b_difference.png          — fitness_width − fitness_flat
  - track3b_grid.csv                — raw data
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
    derive_L_ring, L_vector_from_params, signature_ok, M_P_MEV,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF, modelF_baseline
from track1_proton_ghost_audit import enumerate_pure_p_modes, classify_z3_free_mode


# ─── Target particles with natural line widths ─────────────────────

# ℏ in MeV·s (for τ → Γ conversion)
HBAR_MeV_s = 6.582119569e-22

# (name, mass_MeV, |Q|, lifetime_s_or_None)
# lifetime=None → stable
PARTICLE_DATA = {
    "p":   (938.272,   1, None),              # stable
    "π⁰":  (134.977,   0, 8.43e-17),          # EM decay
    "η′":  (957.780,   0, 3.36e-21),          # strong decay
    "Δ⁺":  (1232.0,    1, 5.63e-24),          # strong decay — very broad
    "Ξ⁻":  (1321.71,   1, 1.639e-10),         # weak decay
    "Ξ⁰":  (1314.86,   0, 2.9e-10),           # weak decay
    "Ω⁻":  (1672.45,   1, 8.21e-11),          # weak decay
}

FLOOR_THRESHOLD = 0.02   # 2% model-level precision
K_WIDTHS        = 2.0    # allow 2 natural widths


def width_threshold(name):
    mass, _q, tau = PARTICLE_DATA[name]
    if tau is None:
        return FLOOR_THRESHOLD
    gamma = HBAR_MeV_s / tau
    gamma_over_m = gamma / mass
    return max(FLOOR_THRESHOLD, K_WIDTHS * gamma_over_m)


TARGETS = [
    (name, *PARTICLE_DATA[name][:2], width_threshold(name))
    for name in PARTICLE_DATA
]
# TARGETS is now: (name, mass, abs_Q, threshold)

MAX_FITNESS = float(len(TARGETS))


# ─── Grid matches Track 3 ───────────────────────────────────────────

EPS_P_GRID = np.linspace(0.40, 1.20, 81)
S_P_GRID   = np.linspace(0.00, 0.50, 51)


# ─── Fitness computation with width-weighted thresholds ────────────

def compute_point(eps_p, s_p):
    """(fitness, ghost_count, mu36) under width-weighted thresholds."""
    mu36 = math.sqrt((3/eps_p)**2 + (6 - 3*s_p)**2)

    try:
        L_ring_p = derive_L_ring(M_P_MEV, 3, 6, eps_p, s_p, K_MODELF)
    except Exception:
        return (float('nan'), float('nan'), mu36)
    if L_ring_p <= 0 or L_ring_p != L_ring_p:
        return (float('nan'), float('nan'), mu36)

    params = modelF_baseline(eps_p=eps_p, s_p=s_p, L_ring_p=L_ring_p)
    G = build_aug_metric(params)
    if not signature_ok(G):
        return (float('nan'), float('nan'), mu36)
    L = L_vector_from_params(params)

    modes = enumerate_pure_p_modes(G, L)
    z3_free = [m for m in modes if m['z3_free']]

    # Ghost count
    ghost_count = 0
    for m in z3_free:
        cls, _ = classify_z3_free_mode(m['E'], m['Q_eff'])
        if cls == 'ghost-sub-observed':
            ghost_count += 1

    # Fitness with width-weighted thresholds
    fitness = 0.0
    for (name, mass, abs_Q, thr) in TARGETS:
        best_rel = None
        for m in z3_free:
            if abs(m['Q_eff']) != abs_Q:
                continue
            rel = abs(m['E'] - mass) / mass
            if best_rel is None or rel < best_rel:
                best_rel = rel
        if best_rel is None:
            closeness = 0.0
        else:
            closeness = max(0.0, 1.0 - best_rel / thr)
        fitness += closeness

    return (fitness, ghost_count, mu36)


def sweep():
    n_s = len(S_P_GRID)
    n_e = len(EPS_P_GRID)
    fitness = np.zeros((n_s, n_e))
    ghosts  = np.zeros((n_s, n_e), dtype=int)
    mu36    = np.zeros((n_s, n_e))

    t0 = time.time()
    for i, s_p in enumerate(S_P_GRID):
        for j, eps_p in enumerate(EPS_P_GRID):
            f, g, m = compute_point(eps_p, s_p)
            fitness[i, j] = f if not (isinstance(f, float) and math.isnan(f)) else 0.0
            ghosts[i, j]  = int(g) if not (isinstance(g, float) and math.isnan(g)) else -1
            mu36[i, j]    = m
        elapsed = time.time() - t0
        print(f"  s_p = {s_p:.2f}  done  ({(i+1)*n_e:>5d} / {n_s*n_e}, "
              f"{elapsed:.1f}s elapsed)")
    return fitness, ghosts, mu36


# ─── Analytical ghost boundary ─────────────────────────────────────

def ghost_boundary_curve():
    s = np.linspace(0.0, 0.50, 500)
    g = 65.4 - (6.0 - 3.0*s)**2
    ok = g > 0
    eps = np.where(ok, 3.0 / np.sqrt(np.maximum(g, 1e-9)), np.nan)
    return eps, s


# ─── Plotting helpers ──────────────────────────────────────────────

def draw_heatmap(ax, Z, ghosts, title, vmin=0, vmax=None,
                 mark_points=None, top_k=5):
    E_grid, S_grid = np.meshgrid(EPS_P_GRID, S_P_GRID)
    Z_masked = np.where(ghosts > 0, np.nan, Z)

    vmax_use = vmax if vmax is not None else MAX_FITNESS
    pcm = ax.pcolormesh(E_grid, S_grid, Z_masked,
                        cmap='viridis', vmin=vmin, vmax=vmax_use,
                        shading='auto')

    ghost_mask = (ghosts > 0).astype(float)
    if ghost_mask.any():
        ax.contourf(E_grid, S_grid, ghost_mask, levels=[0.5, 1.5],
                    colors='none', hatches=['////'])
        ax.contourf(E_grid, S_grid, ghost_mask, levels=[0.5, 1.5],
                    colors=['#888888'], alpha=0.25)

    levels = [1, 2, 3, 4, 5, 6]
    valid_levels = [lv for lv in levels if lv <= vmax_use]
    if valid_levels:
        cs = ax.contour(E_grid, S_grid, Z_masked, levels=valid_levels,
                        colors='white', linewidths=0.8, alpha=0.7)
        ax.clabel(cs, inline=True, fontsize=7, fmt='%.0f')

    eps_b, s_b = ghost_boundary_curve()
    ax.plot(eps_b, s_b, 'r--', linewidth=1.2,
            label='ghost bound μ(3,6)=8.09')

    ax.plot(0.55, 0.162, '*', color='orange', markersize=16,
            markeredgecolor='black', markeredgewidth=0.8,
            label='baseline')

    Z_search = np.where(ghosts == 0, Z, -np.inf)
    flat_idx = np.argsort(Z_search.ravel())[::-1][:top_k]
    for k, idx in enumerate(flat_idx):
        i, j = np.unravel_index(idx, Z_search.shape)
        ax.plot(EPS_P_GRID[j], S_P_GRID[i], 'o',
                color='white', markerfacecolor='red',
                markersize=8 if k == 0 else 6, markeredgewidth=1)
    # Annotate only the top
    idx = flat_idx[0]
    i, j = np.unravel_index(idx, Z_search.shape)
    ax.annotate(
        f"max: ({EPS_P_GRID[j]:.2f}, {S_P_GRID[i]:.2f})\nfit = {Z[i, j]:.2f}",
        xy=(EPS_P_GRID[j], S_P_GRID[i]),
        xytext=(EPS_P_GRID[j] + 0.1, S_P_GRID[i] + 0.06),
        fontsize=9,
        arrowprops=dict(arrowstyle='->', color='red'))

    ax.set_xlabel('ε_p')
    ax.set_ylabel('s_p')
    ax.set_title(title)
    ax.set_xlim(EPS_P_GRID[0], EPS_P_GRID[-1])
    ax.set_ylim(S_P_GRID[0], S_P_GRID[-1])
    ax.grid(alpha=0.2)
    return pcm


def save_heatmap(Z, ghosts, out_path, title):
    fig, ax = plt.subplots(figsize=(11, 7))
    pcm = draw_heatmap(ax, Z, ghosts, title)
    cbar = plt.colorbar(pcm, ax=ax,
                        label='width-weighted fitness (max 7)')
    legend_patches = [
        Patch(facecolor='none', edgecolor='black', hatch='////',
              label='sub-π⁰ ghost region'),
    ]
    ax.legend(handles=legend_patches + ax.get_legend_handles_labels()[0],
              loc='upper right', framealpha=0.9)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def save_comparison(fitness_flat, fitness_width, ghosts, out_path):
    """Side-by-side heat maps: Track 3 (flat thresholds) vs Track 3b (width)."""
    fig, axes = plt.subplots(1, 2, figsize=(20, 7))

    pcm1 = draw_heatmap(axes[0], fitness_flat, ghosts,
                        "Track 3 — flat thresholds (2% / 14% pion)")
    plt.colorbar(pcm1, ax=axes[0], label='fitness')

    pcm2 = draw_heatmap(axes[1], fitness_width, ghosts,
                        "Track 3b — width-weighted thresholds\n"
                        "(2% floor, 2×Γ/m for broad resonances)")
    plt.colorbar(pcm2, ax=axes[1], label='fitness')

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def save_difference(fitness_flat, fitness_width, ghosts, out_path):
    """Difference: width-weighted minus flat — where does re-scoring change the ranking?"""
    diff = fitness_width - fitness_flat
    diff_masked = np.where(ghosts > 0, np.nan, diff)

    fig, ax = plt.subplots(figsize=(11, 7))
    E_grid, S_grid = np.meshgrid(EPS_P_GRID, S_P_GRID)

    vmax = max(abs(np.nanmin(diff_masked)), abs(np.nanmax(diff_masked)))
    pcm = ax.pcolormesh(E_grid, S_grid, diff_masked,
                        cmap='RdBu_r', vmin=-vmax, vmax=vmax,
                        shading='auto')

    ghost_mask = (ghosts > 0).astype(float)
    if ghost_mask.any():
        ax.contourf(E_grid, S_grid, ghost_mask, levels=[0.5, 1.5],
                    colors='none', hatches=['////'])
        ax.contourf(E_grid, S_grid, ghost_mask, levels=[0.5, 1.5],
                    colors=['#888888'], alpha=0.25)

    eps_b, s_b = ghost_boundary_curve()
    ax.plot(eps_b, s_b, 'k--', linewidth=1.2)
    ax.plot(0.55, 0.162, '*', color='orange', markersize=14,
            markeredgecolor='black', label='baseline')

    ax.set_xlabel('ε_p')
    ax.set_ylabel('s_p')
    ax.set_title("R63 Track 3b — Δ(fitness) = width-weighted − flat\n"
                 "positive (red) = width-weighting rewards this geometry\n"
                 "negative (blue) = flat thresholds were more generous")
    plt.colorbar(pcm, ax=ax, label='Δ fitness')
    ax.legend(loc='upper right')
    ax.grid(alpha=0.2)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def save_csv(fitness, ghosts, mu36, out_path):
    with open(out_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['eps_p', 's_p', 'fitness_width', 'ghost_count', 'mu36'])
        for i, s_p in enumerate(S_P_GRID):
            for j, eps_p in enumerate(EPS_P_GRID):
                w.writerow([f"{eps_p:.3f}", f"{s_p:.3f}",
                            f"{fitness[i, j]:.4f}",
                            int(ghosts[i, j]),
                            f"{mu36[i, j]:.4f}"])


def load_track3_fitness(grid_csv_path):
    """Load Track 3's flat-threshold fitness grid from CSV."""
    fitness_flat = np.zeros_like(np.meshgrid(EPS_P_GRID, S_P_GRID)[0])
    with open(grid_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            eps_p = float(row['eps_p'])
            s_p = float(row['s_p'])
            fit = float(row['fitness'])
            # find grid indices
            j = np.argmin(np.abs(EPS_P_GRID - eps_p))
            i = np.argmin(np.abs(S_P_GRID - s_p))
            fitness_flat[i, j] = fit
    return fitness_flat


# ─── Main ───────────────────────────────────────────────────────────

def main():
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(out_dir, exist_ok=True)

    print("=" * 80)
    print("R63 Track 3b — Width-weighted fitness heat map")
    print("=" * 80)
    print()
    print("  Target thresholds (floor 2%, else 2 × Γ/m):")
    for (name, mass, q, thr) in TARGETS:
        m_, _, tau = PARTICLE_DATA[name]
        tau_str = "stable" if tau is None else f"{tau:.2e} s"
        gamma_over_m = (HBAR_MeV_s / tau / m_) if tau else 0.0
        print(f"    {name:>4s}: m = {mass:>7.2f} MeV, "
              f"τ = {tau_str:>12s}, "
              f"Γ/m = {gamma_over_m:.2e}, "
              f"threshold = {thr*100:.2f}%")
    print()
    print(f"  Grid: {len(EPS_P_GRID)} × {len(S_P_GRID)} "
          f"= {len(EPS_P_GRID)*len(S_P_GRID)} points")
    print()

    fitness_width, ghosts, mu36 = sweep()
    print()

    # Summary
    n_ghost_free = int(np.sum(ghosts == 0))
    n_total = fitness_width.size
    Z_search = np.where(ghosts == 0, fitness_width, -np.inf)
    idx = np.unravel_index(np.argmax(Z_search), Z_search.shape)
    i_max, j_max = idx

    print(f"  Sweep complete.  Ghost-free points: {n_ghost_free} / {n_total}")
    print(f"  Peak width-weighted fitness: {fitness_width[i_max, j_max]:.3f} / "
          f"{MAX_FITNESS:.1f}")
    print(f"    at (ε_p = {EPS_P_GRID[j_max]:.3f}, "
          f"s_p = {S_P_GRID[i_max]:.3f}), μ(3,6) = {mu36[i_max, j_max]:.3f}")
    print()
    print("  Top 10 points (width-weighted, ghost-free only):")
    flat_idx = np.argsort(Z_search.ravel())[::-1][:10]
    print(f"    {'ε_p':>6}  {'s_p':>6}  {'fitness':>8}  {'μ(3,6)':>7}")
    for idx_flat in flat_idx:
        i, j = np.unravel_index(idx_flat, Z_search.shape)
        print(f"    {EPS_P_GRID[j]:>6.3f}  {S_P_GRID[i]:>6.3f}  "
              f"{fitness_width[i, j]:>8.3f}  {mu36[i, j]:>7.3f}")
    print()

    # Outputs
    print("  Writing outputs:")
    out_heatmap = os.path.join(out_dir, 'track3b_fitness_width.png')
    out_compare = os.path.join(out_dir, 'track3b_comparison.png')
    out_diff    = os.path.join(out_dir, 'track3b_difference.png')
    out_csv     = os.path.join(out_dir, 'track3b_grid.csv')

    save_heatmap(fitness_width, ghosts, out_heatmap,
                 "R63 Track 3b — Width-weighted fitness landscape\n"
                 "thresholds scale with each particle's natural line width Γ/m")
    print(f"    ✓ {out_heatmap}")

    track3_csv = os.path.join(out_dir, 'track3_grid.csv')
    if os.path.exists(track3_csv):
        fitness_flat = load_track3_fitness(track3_csv)
        save_comparison(fitness_flat, fitness_width, ghosts, out_compare)
        print(f"    ✓ {out_compare}")
        save_difference(fitness_flat, fitness_width, ghosts, out_diff)
        print(f"    ✓ {out_diff}")
    else:
        print(f"    ! skipping comparison (no {track3_csv} found)")

    save_csv(fitness_width, ghosts, mu36, out_csv)
    print(f"    ✓ {out_csv}")
    print()


if __name__ == "__main__":
    main()
