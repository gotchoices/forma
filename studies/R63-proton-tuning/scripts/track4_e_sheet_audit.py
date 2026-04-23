"""
R63 Track 4 — E-sheet parallel audit.

Applies the Tracks 1–3b methodology to the electron sheet.

Scope: strictly e-sheet.  Only (ε_e, s_e) is moved; cross-sheet
σ, ν-sheet, and p-sheet values are held at model-F baseline.

Phase A: ghost audit at R53 Solution D (ε_e=397.074, s_e=2.004200).
Phase B: (ε_e, s_e) fine grid sweep with continuous width-weighted
         fitness; heat map outputs.
Phase C: synthesis in the findings file.

Baseline L_ring_e is derived from m_e at the electron's (1, 2) mode
at each grid point.
"""

import sys, os
import math
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from dataclasses import dataclass
from fractions import Fraction

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    Params, derive_L_ring, L_vector_from_params, mode_energy, mode_6_to_11,
    signature_ok, M_E_MEV, M_P_MEV,
    SQRT_ALPHA, FOUR_PI, ALPHA, PI,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF, modelF_baseline

from track1_proton_ghost_audit import (
    OBSERVED, match_observed, classify_z3_free_mode,
    SPLIT_MIN, LIGHTEST_OBS,
)


# ─── Lepton target particles with natural line widths ──────────────

HBAR_MeV_s = 6.582119569e-22

# (name, mass_MeV, |Q|, lifetime_s | None=stable)
LEPTON_DATA = {
    "e":  (0.510999,   1, None),            # stable
    "μ":  (105.6584,   1, 2.1970e-6),       # weak decay
    "τ":  (1776.86,    1, 2.903e-13),       # weak decay
}

FLOOR_THRESHOLD = 0.02   # 2% model-level floor
K_WIDTHS        = 2.0


def width_threshold(name):
    mass, _q, tau = LEPTON_DATA[name]
    if tau is None:
        return FLOOR_THRESHOLD
    gamma = HBAR_MeV_s / tau
    return max(FLOOR_THRESHOLD, K_WIDTHS * gamma / mass)


TARGETS = [
    (name, *LEPTON_DATA[name][:2], width_threshold(name))
    for name in LEPTON_DATA
]
MAX_FITNESS = float(len(TARGETS))  # 3.0 if every lepton exact


# ─── Metric construction for e-sheet sweeps ────────────────────────

# L_ring_e model-F baseline for reference only — we recalibrate per point.
DEFAULT_L_RING_E = 54.829  # fm (model-F baseline)


def build_params_e(eps_e, s_e, L_ring_e):
    """Construct a Params with overridden e-sheet values and model-F
    defaults for the rest."""
    return Params(
        eps_e=eps_e, s_e=s_e,
        eps_p=0.55, s_p=0.162037,
        eps_nu=2.0, s_nu=0.022,
        k_e=K_MODELF, k_p=K_MODELF, k_nu=K_MODELF,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI * ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=L_ring_e,
        L_ring_p=47.29,       # doesn't affect pure e-sheet modes
        L_ring_nu=1.9577e+11,
    )


# ─── Pure e-sheet enumeration ─────────────────────────────────────

ENERGY_CAP_MEV = 2500.0  # just above τ (1777 MeV)


def enumerate_pure_e_modes(G, L, n_et_max=4, n_er_max=30):
    """Enumerate pure e-sheet modes (n_et, n_er, 0, 0, 0, 0)."""
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
            # Effective charge for pure e-sheet, pure: gcd(0, 0) = 1,
            # so α_sum = n_et; Q_eff = -α_sum = -n_et
            # (composite rule unchanged for n_pt = 0)
            Q_eff = -n_et
            results.append({
                'n_et': n_et, 'n_er': n_er,
                'E': E, 'Q_eff': Q_eff,
            })
    # Deduplicate antiparticle pairs: (n_et, n_er) and (-n_et, -n_er)
    # are C-conjugates at the same energy.  Keep n_et ≥ 0 side.
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


def calibrate_L_ring_e(eps_e, s_e):
    """Derive L_ring_e such that the pure e-sheet (1, 2) mode has
    mass = m_e, using the diagonal single-sheet formula.  The actual
    11D-metric energy will be very close to m_e with small
    off-diagonal corrections."""
    try:
        return derive_L_ring(M_E_MEV, 1, 2, eps_e, s_e, K_MODELF)
    except Exception:
        return None


# ─── Fitness ───────────────────────────────────────────────────────

def compute_point(eps_e, s_e):
    """(fitness, ghost_count, sub_electron_ghost_count) for one point.

    - fitness: sum of lepton closenesses, 0..3.
    - ghost_count: number of sub-observed ghosts in the pure e-sheet
      spectrum (matter-only threshold; below lightest observed matter
      of matching Q).
    - sub_electron_ghost_count: count of charged modes below m_e, a
      specific structural concern (R53 Solution D supposedly guarantees
      electron is the lightest charged mode).
    """
    L_e = calibrate_L_ring_e(eps_e, s_e)
    if L_e is None or L_e <= 0 or L_e != L_e:
        return (float('nan'), float('nan'), float('nan'))

    params = build_params_e(eps_e, s_e, L_e)
    G = build_aug_metric(params)
    if not signature_ok(G):
        return (float('nan'), float('nan'), float('nan'))
    L = L_vector_from_params(params)

    modes = enumerate_pure_e_modes(G, L)

    # Ghost counts
    ghost_count = 0
    sub_e_count = 0
    for m in modes:
        cls, _ = classify_z3_free_mode(m['E'], m['Q_eff'])
        if cls.startswith('ghost'):
            ghost_count += 1
        if abs(m['Q_eff']) == 1 and m['E'] < M_E_MEV:
            sub_e_count += 1

    # Lepton fitness
    fitness = 0.0
    for (name, mass, absQ, thr) in TARGETS:
        best_rel = None
        for m in modes:
            if abs(m['Q_eff']) != absQ:
                continue
            rel = abs(m['E'] - mass) / mass
            if best_rel is None or rel < best_rel:
                best_rel = rel
        if best_rel is None:
            closeness = 0.0
        else:
            closeness = max(0.0, 1.0 - best_rel / thr)
        fitness += closeness

    return (fitness, ghost_count, sub_e_count)


# ─── Phase A: audit at R53 Solution D ──────────────────────────────

BASELINE_EPS_E = 397.074
BASELINE_S_E   = 2.004200


def phase_a_audit():
    print("=" * 100)
    print("R63 Track 4 — PHASE A: Pure e-sheet ghost audit at R53 Solution D")
    print("=" * 100)
    print()

    eps_e, s_e = BASELINE_EPS_E, BASELINE_S_E
    L_e = calibrate_L_ring_e(eps_e, s_e)
    params = build_params_e(eps_e, s_e, L_e)
    G = build_aug_metric(params)
    L = L_vector_from_params(params)

    print(f"  Baseline:       ε_e = {eps_e}, s_e = {s_e}, L_ring_e = {L_e:.4f} fm")
    print(f"  Signature OK:   {signature_ok(G)}")
    print(f"  Energy cap:     {ENERGY_CAP_MEV:.0f} MeV")
    print()

    modes = enumerate_pure_e_modes(G, L)
    print(f"  Enumerated {len(modes)} distinct pure e-sheet modes below "
          f"{ENERGY_CAP_MEV:.0f} MeV.")
    print()

    # Full table (top 40 modes by energy)
    print("  Pure e-sheet modes, sorted by mass (top 40):")
    print(f"    {'E (MeV)':>10s}  {'(n_et,n_er)':>12s}  {'|Q|':>3s}  "
          f"{'classification':<22s}  detail")
    print("    " + "─" * 108)
    ghost_list = []
    sub_e_list = []
    observed_matches = {}
    for m in modes[:40]:
        cls, detail = classify_z3_free_mode(m['E'], m['Q_eff'])
        tup = f"({m['n_et']:+d},{m['n_er']:+d})"
        marker = ""
        if cls.startswith('ghost'):
            marker = " ⚠️"
            ghost_list.append(m)
        elif cls == 'observed':
            marker = " ✓"
            # Extract particle name
            mm = match_observed(m['E'], m['Q_eff'])
            if mm:
                observed_matches.setdefault(mm[0].name, []).append(m)
        if abs(m['Q_eff']) == 1 and m['E'] < M_E_MEV:
            sub_e_list.append(m)
            marker += " [sub-e]"
        print(f"    {m['E']:>10.4f}  {tup:>12s}  {abs(m['Q_eff']):>3d}  "
              f"{cls:<22s}  {detail}{marker}")
    if len(modes) > 40:
        print(f"    ... and {len(modes) - 40} more above 2.5 GeV cap")
    print()

    # Observed-match summary
    print("  Observed-particle matches found in pure e-sheet spectrum:")
    for name, matches in sorted(observed_matches.items(), key=lambda x: -len(x[1])):
        for m in matches[:3]:
            tup = f"({m['n_et']:+d},{m['n_er']:+d})"
            print(f"    {name:>5s}: {tup:>12s}  E = {m['E']:>9.3f} MeV")
        if len(matches) > 3:
            print(f"    {name:>5s}: ... and {len(matches)-3} more")
    print()

    # Lepton-specific check
    print("  Lepton-specific analysis (targets: e, μ, τ):")
    for (name, mass, absQ, thr) in TARGETS:
        best = None
        for m in modes:
            if abs(m['Q_eff']) != absQ:
                continue
            rel = abs(m['E'] - mass) / mass
            if best is None or rel < best[0]:
                best = (rel, m)
        if best is None:
            print(f"    {name:>3s} (target {mass:>8.3f} MeV, thr {thr*100:.1f}%): "
                  f"NO MATCH in |n_er| ≤ 30 range")
        else:
            rel, m = best
            tup = f"({m['n_et']:+d},{m['n_er']:+d})"
            close = max(0.0, 1.0 - rel / thr)
            flag = '✓' if close > 0 else '✗'
            print(f"    {name:>3s} (target {mass:>8.3f} MeV, thr {thr*100:.1f}%): "
                  f"best = {tup:>12s} at {m['E']:>9.3f} MeV  "
                  f"Δm/m = {rel*100:>+6.3f}%  close = {close:.3f}  {flag}")
    print()

    # Ghost summary
    print(f"  Sub-observed ghosts found: {len(ghost_list)}")
    if ghost_list:
        print(f"  Ghost list (below lightest observed matter of matching |Q|):")
        print(f"    {'E (MeV)':>10s}  {'(n_et,n_er)':>12s}  {'|Q|':>3s}  detail")
        print("    " + "─" * 90)
        for m in ghost_list:
            cls, detail = classify_z3_free_mode(m['E'], m['Q_eff'])
            tup = f"({m['n_et']:+d},{m['n_er']:+d})"
            print(f"    {m['E']:>10.4f}  {tup:>12s}  {abs(m['Q_eff']):>3d}  {detail}")
        print()

    print(f"  Charged modes BELOW m_e ({M_E_MEV} MeV): {len(sub_e_list)}")
    if sub_e_list:
        print("  Sub-electron list (would be lighter than observed electron):")
        for m in sub_e_list:
            tup = f"({m['n_et']:+d},{m['n_er']:+d})"
            print(f"    {m['E']:>10.4f}  {tup:>12s}  |Q| = {abs(m['Q_eff'])}")
        print()

    print()
    return ghost_list, sub_e_list


# ─── Phase B: grid sweep ──────────────────────────────────────────

# ε_e: log-spaced ±35% around baseline 397
# s_e: fine linear around baseline 2.004, near the shear-resonance line
EPS_E_GRID = np.logspace(np.log10(250), np.log10(650), 41)   # 41 log points
S_E_GRID   = np.linspace(1.95, 2.06, 56)                      # 56 lin points


def phase_b_sweep():
    print("=" * 100)
    print("R63 Track 4 — PHASE B: (ε_e, s_e) grid sweep")
    print("=" * 100)
    print()
    print(f"  ε_e grid: {len(EPS_E_GRID)} log points from "
          f"{EPS_E_GRID[0]:.1f} to {EPS_E_GRID[-1]:.1f}")
    print(f"  s_e grid: {len(S_E_GRID)} linear points from "
          f"{S_E_GRID[0]:.3f} to {S_E_GRID[-1]:.3f}")
    print(f"  Total: {len(EPS_E_GRID) * len(S_E_GRID)} points")
    print()

    n_s = len(S_E_GRID)
    n_e = len(EPS_E_GRID)
    fitness = np.zeros((n_s, n_e))
    ghosts  = np.zeros((n_s, n_e), dtype=int)
    sub_e   = np.zeros((n_s, n_e), dtype=int)

    t0 = time.time()
    for i, s_e in enumerate(S_E_GRID):
        for j, eps_e in enumerate(EPS_E_GRID):
            f, g, se = compute_point(eps_e, s_e)
            fitness[i, j] = f if not (isinstance(f, float) and math.isnan(f)) else 0.0
            ghosts[i, j]  = int(g) if not (isinstance(g, float) and math.isnan(g)) else -1
            sub_e[i, j]   = int(se) if not (isinstance(se, float) and math.isnan(se)) else -1
        elapsed = time.time() - t0
        print(f"  s_e = {s_e:.4f}  done  ({(i+1)*n_e:>5d} / {n_s*n_e}, "
              f"{elapsed:.1f}s elapsed)")
    print()

    # Summary
    n_total = fitness.size
    n_clean = int(np.sum((ghosts == 0) & (sub_e == 0)))
    n_ghost_free = int(np.sum(ghosts == 0))
    print(f"  Points without sub-observed ghosts:  {n_ghost_free} / {n_total}  "
          f"({100*n_ghost_free/n_total:.0f}%)")
    print(f"  Points without sub-electron ghosts:  "
          f"{int(np.sum(sub_e == 0))} / {n_total}")
    print(f"  Clean on both:                        {n_clean} / {n_total}")

    Z_search = np.where((ghosts == 0) & (sub_e == 0), fitness, -np.inf)
    idx = np.unravel_index(np.argmax(Z_search), Z_search.shape)
    i_max, j_max = idx
    print(f"\n  Peak fitness (clean points only):  "
          f"{fitness[i_max, j_max]:.3f} / {MAX_FITNESS:.1f}")
    print(f"    at (ε_e = {EPS_E_GRID[j_max]:.3f}, s_e = {S_E_GRID[i_max]:.4f})")
    print()

    print("  Top 10 clean points:")
    flat_idx = np.argsort(Z_search.ravel())[::-1][:10]
    print(f"    {'ε_e':>8}  {'s_e':>8}  {'fitness':>8}")
    for idx_flat in flat_idx:
        i, j = np.unravel_index(idx_flat, Z_search.shape)
        print(f"    {EPS_E_GRID[j]:>8.3f}  {S_E_GRID[i]:>8.4f}  "
              f"{fitness[i, j]:>8.3f}")
    print()

    return fitness, ghosts, sub_e


# ─── Plotting ─────────────────────────────────────────────────────

def save_heatmap(Z, ghosts, sub_e, out_path, title):
    fig, ax = plt.subplots(figsize=(12, 8))
    E_grid, S_grid = np.meshgrid(EPS_E_GRID, S_E_GRID)

    # Mask both ghost types
    bad = (ghosts > 0) | (sub_e > 0)
    Z_masked = np.where(bad, np.nan, Z)

    pcm = ax.pcolormesh(E_grid, S_grid, Z_masked, cmap='viridis',
                        vmin=0, vmax=MAX_FITNESS, shading='auto')

    if bad.any():
        bad_float = bad.astype(float)
        ax.contourf(E_grid, S_grid, bad_float, levels=[0.5, 1.5],
                    colors='none', hatches=['////'])
        ax.contourf(E_grid, S_grid, bad_float, levels=[0.5, 1.5],
                    colors=['#888888'], alpha=0.25)

    # Contour lines at integer fitness levels
    levels = [0.5, 1.0, 1.5, 2.0, 2.5]
    valid_levels = [lv for lv in levels if lv <= MAX_FITNESS]
    if valid_levels:
        cs = ax.contour(E_grid, S_grid, Z_masked, levels=valid_levels,
                        colors='white', linewidths=0.8, alpha=0.7)
        ax.clabel(cs, inline=True, fontsize=8, fmt='%.1f')

    # Baseline marker
    ax.plot(BASELINE_EPS_E, BASELINE_S_E, '*', color='orange', markersize=18,
            markeredgecolor='black', markeredgewidth=0.8,
            label=f'R53 Solution D ({BASELINE_EPS_E}, {BASELINE_S_E})')

    # Shear resonance line s_e = 2.0 (where (1, 2) detuning = 0)
    ax.axhline(y=2.0, color='red', linestyle=':', linewidth=1.2,
               label='shear resonance s_e = 2 (for (1,2))')

    # Top peak markers
    Z_search = np.where(~bad, Z, -np.inf)
    top_k = 3
    flat_idx = np.argsort(Z_search.ravel())[::-1][:top_k]
    for k, idx in enumerate(flat_idx):
        i, j = np.unravel_index(idx, Z_search.shape)
        ax.plot(EPS_E_GRID[j], S_E_GRID[i], 'o',
                color='white', markerfacecolor='red',
                markersize=9 if k == 0 else 6, markeredgewidth=1)
    idx = flat_idx[0]
    i, j = np.unravel_index(idx, Z_search.shape)
    ax.annotate(
        f"peak: ({EPS_E_GRID[j]:.1f}, {S_E_GRID[i]:.4f})\nfit = {Z[i, j]:.2f}",
        xy=(EPS_E_GRID[j], S_E_GRID[i]),
        xytext=(EPS_E_GRID[j] * 1.15, S_E_GRID[i] + 0.02),
        fontsize=9,
        arrowprops=dict(arrowstyle='->', color='red'))

    ax.set_xscale('log')
    ax.set_xlabel('ε_e  (e-sheet aspect ratio, log scale)')
    ax.set_ylabel('s_e  (e-sheet shear)')
    ax.set_title(title)

    cbar = plt.colorbar(pcm, ax=ax,
                        label=f'fitness (max {MAX_FITNESS:.0f}: e + μ + τ all exact)')

    legend_patches = [
        Patch(facecolor='none', edgecolor='black', hatch='////',
              label='ghost region (sub-observed or sub-electron)'),
    ]
    ax.legend(handles=legend_patches + ax.get_legend_handles_labels()[0],
              loc='lower right', framealpha=0.9, fontsize=9)

    ax.set_xlim(EPS_E_GRID[0], EPS_E_GRID[-1])
    ax.set_ylim(S_E_GRID[0], S_E_GRID[-1])
    ax.grid(alpha=0.2, which='both')

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def save_ghost_breakdown(ghosts, sub_e, out_path):
    """Two-panel: sub-observed ghost count, sub-electron ghost count."""
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))
    E_grid, S_grid = np.meshgrid(EPS_E_GRID, S_E_GRID)

    for ax, Z, title, cmap in [
        (axes[0], ghosts, "Sub-observed ghost count", "Reds"),
        (axes[1], sub_e, "Sub-electron charged-mode count", "Oranges"),
    ]:
        pcm = ax.pcolormesh(E_grid, S_grid, Z, cmap=cmap,
                            vmin=0, vmax=max(1, Z.max()), shading='auto')
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


# ─── Main ──────────────────────────────────────────────────────────

def main():
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(out_dir, exist_ok=True)

    print()
    print("Lepton targets (width-weighted thresholds):")
    for (name, mass, q, thr) in TARGETS:
        _, _, tau = LEPTON_DATA[name]
        tau_str = "stable" if tau is None else f"{tau:.2e} s"
        print(f"  {name:>2s}: m = {mass:>9.3f} MeV, τ = {tau_str:>12s}, "
              f"thr = {thr*100:.2f}%")
    print()

    # Phase A: baseline audit
    ghosts_list, sub_e_list = phase_a_audit()

    # Phase B: sweep + heat maps
    fitness, ghosts, sub_e = phase_b_sweep()

    print("  Writing outputs:")
    out_fitness = os.path.join(out_dir, 'track4_fitness.png')
    out_ghost_breakdown = os.path.join(out_dir, 'track4_ghost_breakdown.png')
    out_csv = os.path.join(out_dir, 'track4_grid.csv')

    save_heatmap(fitness, ghosts, sub_e, out_fitness,
                 "R63 Track 4 — E-sheet fitness landscape\n"
                 "width-weighted fitness against electron, muon, tau")
    print(f"    ✓ {out_fitness}")

    save_ghost_breakdown(ghosts, sub_e, out_ghost_breakdown)
    print(f"    ✓ {out_ghost_breakdown}")

    # CSV
    with open(out_csv, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['eps_e', 's_e', 'fitness', 'n_ghosts', 'n_sub_electron'])
        for i, s_e in enumerate(S_E_GRID):
            for j, eps_e in enumerate(EPS_E_GRID):
                w.writerow([f"{eps_e:.4f}", f"{s_e:.4f}",
                            f"{fitness[i, j]:.4f}",
                            int(ghosts[i, j]), int(sub_e[i, j])])
    print(f"    ✓ {out_csv}")
    print()


if __name__ == "__main__":
    main()
