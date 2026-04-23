"""
R63 Track 3 — Pure p-sheet fitness heat map.

Replaces Track 2's brittle "integer match count" criterion with a
continuous closeness-based fitness score.  Sweeps (ε_p, s_p) on a
fine grid and writes PNG heat maps to outputs/.

Fitness (Option 2 from the advice document): for each target
particle, find the pure p-sheet Z₃-free mode with matching |Q|
closest in mass.  Closeness = max(0, 1 − |Δm/m| / threshold),
clipped to [0, 1].  Total fitness = sum over targets (max = N
where N = |targets|).  Ghost-region points (any sub-observed
ghost) are masked out.

Grid: ε_p ∈ [0.40, 1.20], s_p ∈ [0.00, 0.50].  Fine enough for
smooth contours (~4000 points).

Outputs (written to ../outputs/):
  - track3_fitness.png       — primary heat map with contours
  - track3_ghost_count.png   — ghost count map (diagnostic)
  - track3_mu36.png          — μ(3, 6) contour map (reference)
  - track3_grid.csv          — raw data
"""

import sys, os
import math
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import Patch

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    derive_L_ring, L_vector_from_params, signature_ok, M_P_MEV,
    mode_6_to_11, mode_energy,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF, modelF_baseline

from track1_proton_ghost_audit import (
    enumerate_pure_p_modes, classify_z3_free_mode,
)


# ─── Target particles (baseline-matched set from Track 1 F2) ────────

# (name, mass_MeV, |Q|, match_threshold)
TARGETS = [
    ("p",    938.272,   1, 0.02),
    ("π⁰",   134.977,   0, 0.14),   # pion gets relaxed threshold
    ("η′",   957.780,   0, 0.02),
    ("Δ⁺",   1232.0,    1, 0.02),
    ("Ξ⁻",   1321.71,   1, 0.02),
    ("Ξ⁰",   1314.86,   0, 0.02),
    ("Ω⁻",   1672.45,   1, 0.02),
]
MAX_FITNESS = len(TARGETS)  # 7.0 when every particle is exactly matched


# ─── Grid ───────────────────────────────────────────────────────────

EPS_P_GRID = np.linspace(0.40, 1.20, 81)   # 81 values; 0.40–1.20 in steps of 0.01
S_P_GRID   = np.linspace(0.00, 0.50, 51)   # 51 values; 0.00–0.50 in steps of 0.01


# ─── Fitness computation ────────────────────────────────────────────

def compute_point(eps_p, s_p):
    """Return (fitness_score, ghost_count, mu36) for (ε_p, s_p).

    fitness_score: sum of closeness over TARGETS.
    ghost_count:   number of sub-observed ghosts (Track 1 criterion).
    mu36:          the μ(3, 6) dimensionless eigenvalue for reference.
    Returns (nan, nan, mu36) if signature fails.
    """
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

    # Fitness: sum of closeness across target particles
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


# ─── Analytic ghost-free boundary ───────────────────────────────────

def ghost_boundary_curve():
    """Plotting coords for the curve μ(3,6) = 8.09 in (ε, s) space.

    (3/ε)² + (6 − 3 s)² = 65.4
     ⇒  ε = 3 / √(65.4 − (6 − 3s)²)   where  (6 − 3s)² ≤ 65.4
    """
    s = np.linspace(0.0, 0.50, 500)
    g = 65.4 - (6.0 - 3.0*s)**2
    ok = g > 0
    eps = np.where(ok, 3.0 / np.sqrt(np.maximum(g, 1e-9)), np.nan)
    return eps, s


# ─── Plotting ───────────────────────────────────────────────────────

def save_heatmap(Z, ghosts, mu36, out_path):
    """Primary fitness heat map with ghost mask + ghost boundary."""
    fig, ax = plt.subplots(figsize=(11, 7))
    E_grid, S_grid = np.meshgrid(EPS_P_GRID, S_P_GRID)

    # Masked fitness: set to NaN where ghost count > 0
    Z_masked = np.where(ghosts > 0, np.nan, Z)

    # Fitness heat map
    pcm = ax.pcolormesh(E_grid, S_grid, Z_masked,
                        cmap='viridis', vmin=0, vmax=MAX_FITNESS,
                        shading='auto')

    # Ghost region — shade with grey hatch
    ghost_mask = (ghosts > 0).astype(float)
    # contourf with hatch for ghost region
    if ghost_mask.any():
        ax.contourf(E_grid, S_grid, ghost_mask, levels=[0.5, 1.5],
                    colors='none', hatches=['////'])
        # Also darker semi-transparent overlay
        ax.contourf(E_grid, S_grid, ghost_mask, levels=[0.5, 1.5],
                    colors=['#888888'], alpha=0.25)

    # Contour lines at integer fitness levels
    levels = [1, 2, 3, 4, 5, 6, 6.5, 7]
    cs = ax.contour(E_grid, S_grid, Z_masked, levels=levels,
                    colors='white', linewidths=0.8, alpha=0.7)
    ax.clabel(cs, inline=True, fontsize=8, fmt='%.1f')

    # Analytic ghost-free boundary
    eps_b, s_b = ghost_boundary_curve()
    ax.plot(eps_b, s_b, 'r--', linewidth=1.2,
            label='ghost boundary:  μ(3,6) = 8.09')

    # Baseline marker
    ax.plot(0.55, 0.162, '*', color='orange', markersize=18,
            markeredgecolor='black', markeredgewidth=0.8,
            label='baseline (0.55, 0.162)')

    # Track 21 point (outside grid but for reference)
    # ax.plot(0.15, 0.05, 'x', color='red', markersize=10, ...)

    # Local maxima — find top few
    # Mask ghost region for maximum search
    Z_search = np.where(ghosts == 0, Z, -np.inf)
    top_n = 5
    # Simple approach: find top-n unmasked values
    flat_idx = np.argsort(Z_search.ravel())[::-1][:top_n]
    for k, idx in enumerate(flat_idx):
        i, j = np.unravel_index(idx, Z_search.shape)
        ax.plot(EPS_P_GRID[j], S_P_GRID[i], 'o',
                color='white', markerfacecolor='red',
                markersize=8, markeredgewidth=1)
        if k == 0:
            ax.annotate(f"max: ({EPS_P_GRID[j]:.2f}, {S_P_GRID[i]:.2f})"
                        f"\nfit = {Z[i, j]:.2f}",
                        xy=(EPS_P_GRID[j], S_P_GRID[i]),
                        xytext=(EPS_P_GRID[j]+0.1, S_P_GRID[i]+0.05),
                        fontsize=9,
                        arrowprops=dict(arrowstyle='->', color='red'))

    ax.set_xlabel('ε_p  (proton-sheet aspect ratio)')
    ax.set_ylabel('s_p  (proton-sheet shear)')
    ax.set_title("R63 Track 3 — Pure p-sheet fitness landscape\n"
                 f"fitness = Σ (closeness to {len(TARGETS)} baseline target particles), max = {MAX_FITNESS}")

    cbar = plt.colorbar(pcm, ax=ax, label='fitness score (0 = no matches; 7 = all exact)')

    # Legend for hatch
    legend_patches = [
        Patch(facecolor='none', edgecolor='black', hatch='////',
              label='sub-π⁰ ghost region (unphysical)'),
    ]
    ax.legend(handles=legend_patches + ax.get_legend_handles_labels()[0],
              loc='upper right', framealpha=0.9)

    ax.set_xlim(EPS_P_GRID[0], EPS_P_GRID[-1])
    ax.set_ylim(S_P_GRID[0], S_P_GRID[-1])
    ax.grid(alpha=0.2)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def save_ghost_map(ghosts, out_path):
    """Diagnostic map of sub-observed ghost count."""
    fig, ax = plt.subplots(figsize=(11, 7))
    E_grid, S_grid = np.meshgrid(EPS_P_GRID, S_P_GRID)

    pcm = ax.pcolormesh(E_grid, S_grid, ghosts,
                        cmap='Reds', vmin=0, vmax=max(1, ghosts.max()),
                        shading='auto')
    eps_b, s_b = ghost_boundary_curve()
    ax.plot(eps_b, s_b, 'k--', linewidth=1.2,
            label='analytic boundary μ(3,6) = 8.09')
    ax.plot(0.55, 0.162, '*', color='orange', markersize=15,
            markeredgecolor='black', label='baseline')

    ax.set_xlabel('ε_p')
    ax.set_ylabel('s_p')
    ax.set_title("R63 Track 3 — Sub-observed ghost count")
    plt.colorbar(pcm, ax=ax, label='ghost count')
    ax.legend(loc='upper right')
    ax.grid(alpha=0.2)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def save_mu36_map(mu36, out_path):
    """Reference map of μ(3, 6) with ghost bound overlaid."""
    fig, ax = plt.subplots(figsize=(11, 7))
    E_grid, S_grid = np.meshgrid(EPS_P_GRID, S_P_GRID)

    pcm = ax.pcolormesh(E_grid, S_grid, mu36, cmap='viridis',
                        shading='auto')
    levels = [5, 6, 7, 8, 8.09, 9, 10, 12, 15]
    cs = ax.contour(E_grid, S_grid, mu36, levels=levels,
                    colors='white', linewidths=0.8)
    ax.clabel(cs, inline=True, fontsize=8, fmt='%.2f')

    # Highlight the 8.09 contour
    cs_bound = ax.contour(E_grid, S_grid, mu36, levels=[8.09],
                          colors='red', linewidths=2.0)
    ax.clabel(cs_bound, inline=True, fontsize=10, fmt='%.2f')

    ax.plot(0.55, 0.162, '*', color='orange', markersize=15,
            markeredgecolor='black', label='baseline')

    ax.set_xlabel('ε_p')
    ax.set_ylabel('s_p')
    ax.set_title("R63 Track 3 — μ(3, 6) reference map\n"
                 "red contour: ghost-free boundary at μ(3, 6) = 8.09")
    plt.colorbar(pcm, ax=ax, label='μ(3, 6)')
    ax.legend(loc='upper right')
    ax.grid(alpha=0.2)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def save_csv(fitness, ghosts, mu36, out_path):
    with open(out_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['eps_p', 's_p', 'fitness', 'ghost_count', 'mu36'])
        for i, s_p in enumerate(S_P_GRID):
            for j, eps_p in enumerate(EPS_P_GRID):
                w.writerow([f"{eps_p:.3f}", f"{s_p:.3f}",
                            f"{fitness[i, j]:.4f}",
                            int(ghosts[i, j]),
                            f"{mu36[i, j]:.4f}"])


# ─── Main ───────────────────────────────────────────────────────────

def main():
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(out_dir, exist_ok=True)

    print("=" * 80)
    print("R63 Track 3 — Pure p-sheet fitness heat map")
    print("=" * 80)
    print()
    print(f"  Grid: {len(EPS_P_GRID)} × {len(S_P_GRID)} "
          f"= {len(EPS_P_GRID)*len(S_P_GRID)} points")
    print(f"  ε_p ∈ [{EPS_P_GRID[0]:.2f}, {EPS_P_GRID[-1]:.2f}]")
    print(f"  s_p ∈ [{S_P_GRID[0]:.2f}, {S_P_GRID[-1]:.2f}]")
    print(f"  Target particles ({len(TARGETS)}): "
          f"{', '.join(t[0] for t in TARGETS)}")
    print(f"  Max fitness: {MAX_FITNESS:.1f}")
    print()

    fitness, ghosts, mu36 = sweep()
    print()

    # ─── Summary ────────────────────────────────────────────
    n_ghost_free = int(np.sum(ghosts == 0))
    n_total = fitness.size
    print(f"  Sweep complete.  Ghost-free points: {n_ghost_free} / {n_total}")

    Z_search = np.where(ghosts == 0, fitness, -np.inf)
    idx = np.unravel_index(np.argmax(Z_search), Z_search.shape)
    i_max, j_max = idx
    print(f"  Peak fitness: {fitness[i_max, j_max]:.3f} / {MAX_FITNESS:.1f}")
    print(f"    at (ε_p = {EPS_P_GRID[j_max]:.3f}, "
          f"s_p = {S_P_GRID[i_max]:.3f}),  "
          f"μ(3,6) = {mu36[i_max, j_max]:.3f}")
    # top 10 local
    print()
    print("  Top 10 points (highest fitness, ghost-free only):")
    flat_idx = np.argsort(Z_search.ravel())[::-1][:10]
    print(f"    {'ε_p':>6}  {'s_p':>6}  {'fitness':>8}  {'μ(3,6)':>7}")
    for idx_flat in flat_idx:
        i, j = np.unravel_index(idx_flat, Z_search.shape)
        print(f"    {EPS_P_GRID[j]:>6.3f}  {S_P_GRID[i]:>6.3f}  "
              f"{fitness[i, j]:>8.3f}  {mu36[i, j]:>7.3f}")
    print()

    # ─── Outputs ────────────────────────────────────────────
    print("  Writing outputs:")
    out_fitness = os.path.join(out_dir, 'track3_fitness.png')
    out_ghost   = os.path.join(out_dir, 'track3_ghost_count.png')
    out_mu36    = os.path.join(out_dir, 'track3_mu36.png')
    out_csv     = os.path.join(out_dir, 'track3_grid.csv')

    save_heatmap(fitness, ghosts, mu36, out_fitness)
    print(f"    ✓ {out_fitness}")
    save_ghost_map(ghosts, out_ghost)
    print(f"    ✓ {out_ghost}")
    save_mu36_map(mu36, out_mu36)
    print(f"    ✓ {out_mu36}")
    save_csv(fitness, ghosts, mu36, out_csv)
    print(f"    ✓ {out_csv}")
    print()


if __name__ == "__main__":
    main()
