"""
R63 Track 6 Phase 6c — Marginal ratio scans per sheet under Q132 v2.

For each of the three sheets (e, ν, p), sweep its (ε, s) over a 2D grid
while holding the other two sheets at model-F baseline.  At each grid
point, re-derive that sheet's L_ring from the sheet-anchor tuple,
rebuild the 11D metric, compute the predicted mass of every particle
in the v2-certified inventory, and score against observed masses
using width-weighted thresholds (natural line width Γ = ℏ/τ).

Scoring philosophy:
  - The goal is NOT to minimize Δm/m arbitrarily.  A particle's miss
    should be consistent with its observed natural width.
  - Threshold per particle = max(floor, K × Γ/m) with floor = 0.02.
  - Closeness = max(0, 1 − |Δm/m| / threshold).
  - Broad resonances (ρ at Γ/m ≈ 0.19) have wide thresholds; narrow
    states (leptons, most hadrons) bottom out at the 2% floor.

v2-certified inventory:
  - 14 tuples from R60 Track 19 that pass Phase 6a compatibility
  - 5 tuples from Phase 6b re-derivation (τ, Λ, Σ⁻, Ξ⁻, Ξ⁰)

Output (../outputs/):
  - track6_phase6c_p_sheet.png   — p-sheet fitness heat map
  - track6_phase6c_e_sheet.png   — e-sheet fitness heat map
  - track6_phase6c_nu_sheet.png  — ν-sheet fitness heat map
  - track6_phase6c_grids.csv     — raw grid data (all three scans)
  - track6_phase6c_peaks.csv     — per-scan peaks + per-particle breakdown
"""

import sys, os
import math
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    Params, derive_L_ring, L_vector_from_params, mode_energy, mode_6_to_11,
    signature_ok, M_E_MEV, M_P_MEV,
    SQRT_ALPHA, FOUR_PI, ALPHA,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF


# ─── v2-certified inventory ────────────────────────────────────────
# (name, 6-tuple, mass_MeV, |Q|, lifetime_s | None=stable)
# Lifetimes from PDG; strong-decay particles use Γ-derived τ.

HBAR_MeV_s = 6.582119569e-22

INVENTORY = [
    # ── Inputs (pinned to mass by calibration) ──
    ("electron",  ( 1,  2,  0,  0,  0,  0),  0.510999,   1, None),
    ("proton",    ( 0,  0,  0,  0,  3,  6),  938.272,    1, None),
    ("nu_1",      ( 0,  0,  1,  1,  0,  0),  3.21e-8,    0, None),  # anchor
    # ── R60 T19 tuples passing Phase 6a ──
    ("muon",      ( 1,  1, -2, -6,  0,  0),  105.6584,   1, 2.1970e-6),
    ("neutron",   (-3, -6,  1, -6, -3, -6),  939.565,    0, 879.4),
    ("eta_prime", ( 0, -6, -1, -6,  0, -6),  957.780,    0, 3.36e-21),
    ("Sigma_+",   ( 2, -3, -2, -6,  3,  6),  1189.37,    1, 8.018e-11),
    ("phi",       (-3, -6,  1, -6, -3,  6),  1019.461,   0, 1.548e-22),
    ("rho",       (-3, -6,  1, -6, -3,  3),  775.26,     0, 4.411e-24),
    ("K0",        ( 0, -1, -1, -6,  0, -4),  497.611,    0, 8.954e-11),
    ("K_pm",      ( 1,  3, -2, -6,  0, -4),  493.677,    1, 1.238e-8),
    ("eta",       ( 0, -4, -1, -6,  0, -3),  547.862,    0, 5.02e-19),
    ("pi0",       ( 0,  0, -1, -6,  0, -1),  134.977,    0, 8.43e-17),
    ("pi_pm",     ( 1,  2, -2, -6,  0, -1),  139.570,    1, 2.603e-8),
    # ── Phase 6b v2 replacements ──
    ("tau",       (-6, -4, -6, -6, -6,  6),  1776.86,    1, 2.903e-13),
    ("Lambda",    (-2,  5, -6, -6,  0, -5),  1115.683,   0, 2.632e-10),
    ("Sigma_-",   (-2,  4, -6, -6, -3, -5),  1197.449,   1, 1.479e-10),
    ("Xi_-",      (-3,  2, -6, -6, -3,  6),  1321.71,    1, 1.639e-10),
    ("Xi_0",      ( 0,  0, -6, -6, -6, -1),  1314.86,    0, 2.90e-10),
]

FLOOR_THRESHOLD = 0.02   # 2% model-level precision floor
K_WIDTHS        = 2.0    # allow up to 2 natural widths


def width_threshold(mass, tau):
    """Width-weighted threshold: max(floor, K × Γ/m)."""
    if tau is None:
        return FLOOR_THRESHOLD
    gamma = HBAR_MeV_s / tau
    return max(FLOOR_THRESHOLD, K_WIDTHS * gamma / mass)


INVENTORY_WITH_THR = [
    (name, tup, mass, absQ, tau, width_threshold(mass, tau))
    for (name, tup, mass, absQ, tau) in INVENTORY
]

MAX_FITNESS = float(len(INVENTORY_WITH_THR))


# ─── Model-F baseline ──────────────────────────────────────────────

BASELINE = dict(
    eps_e=397.074, s_e=2.004200,
    eps_p=0.55,    s_p=0.162037,
    eps_nu=2.0,    s_nu=0.022,
    k_e=K_MODELF,  k_p=K_MODELF,  k_nu=K_MODELF,
    g_aa=1.0,
    sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI * ALPHA,
    sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
)


def build_params(eps_e, s_e, eps_p, s_p, eps_nu, s_nu):
    """Build Params, auto-calibrating each sheet's L_ring from its anchor."""
    # p-sheet anchored on (3, 6) proton
    try:
        L_p = derive_L_ring(M_P_MEV, 3, 6, eps_p, s_p, K_MODELF)
    except Exception:
        return None
    if L_p is None or L_p <= 0 or L_p != L_p:
        return None
    # e-sheet anchored on (1, 2) electron
    try:
        L_e = derive_L_ring(M_E_MEV, 1, 2, eps_e, s_e, K_MODELF)
    except Exception:
        return None
    if L_e is None or L_e <= 0 or L_e != L_e:
        return None
    # ν-sheet anchored on (1, 1) ν₁ at its tiny mass
    M_NU_MEV = 3.21e-8
    try:
        L_nu = derive_L_ring(M_NU_MEV, 1, 1, eps_nu, s_nu, K_MODELF)
    except Exception:
        return None
    if L_nu is None or L_nu <= 0 or L_nu != L_nu:
        return None

    return Params(
        eps_e=eps_e, s_e=s_e,
        eps_p=eps_p, s_p=s_p,
        eps_nu=eps_nu, s_nu=s_nu,
        k_e=BASELINE['k_e'], k_p=BASELINE['k_p'], k_nu=BASELINE['k_nu'],
        g_aa=BASELINE['g_aa'],
        sigma_ta=BASELINE['sigma_ta'], sigma_at=BASELINE['sigma_at'],
        sign_e=BASELINE['sign_e'], sign_p=BASELINE['sign_p'], sign_nu=BASELINE['sign_nu'],
        L_ring_e=L_e, L_ring_p=L_p, L_ring_nu=L_nu,
    )


# ─── Fitness ────────────────────────────────────────────────────────

def score_point(params):
    """Given Params, compute full-inventory width-weighted fitness.

    Returns (fitness, per_particle_misses) or (nan, None) if the metric
    or any critical quantity is invalid.
    """
    G = build_aug_metric(params)
    if not signature_ok(G):
        return float('nan'), None
    L = L_vector_from_params(params)

    fitness = 0.0
    details = []
    for (name, tup, mass, absQ, tau, thr) in INVENTORY_WITH_THR:
        n11 = mode_6_to_11(tup)
        try:
            E = mode_energy(G, L, n11)
        except Exception:
            details.append((name, None, None, 0.0, thr, tau))
            continue
        if E is None or E <= 0 or E != E:
            details.append((name, None, None, 0.0, thr, tau))
            continue
        rel = abs(E - mass) / mass
        closeness = max(0.0, 1.0 - rel / thr)
        fitness += closeness
        details.append((name, E, rel, closeness, thr, tau))
    return fitness, details


# ─── Grids per sheet ────────────────────────────────────────────────

# Grids chosen so model-F baseline + known candidate peaks are sampled.
#   p-sheet baseline (0.550, 0.162); Track 3b peaks (0.73, 0.34), (0.89, 0.01),
#   (0.80, 0.05).
#   e-sheet baseline (397.074, 2.0042).
#   ν-sheet baseline (2.0, 0.022).

def _grid_with_points(arange_args, extras):
    base = np.arange(*arange_args)
    combined = sorted(set(list(base) + list(extras)))
    return np.array(combined)


P_EPS_GRID = _grid_with_points((0.40, 1.21, 0.02), [0.55, 0.73, 0.80, 0.89])
P_S_GRID   = _grid_with_points((0.00, 0.51, 0.02),
                                [0.01, 0.05, 0.162, 0.34])

E_EPS_GRID = np.logspace(np.log10(250), np.log10(650), 21)
E_S_GRID   = _grid_with_points((1.98, 2.031, 0.002), [2.0042])

NU_EPS_GRID = _grid_with_points((1.0, 10.5, 1.0), [2.0, 5.0])
NU_S_GRID   = _grid_with_points((0.005, 0.105, 0.01), [0.022])

# Specific candidate points to evaluate explicitly (outside grid scans)
NAMED_POINTS = [
    ("baseline",           397.074, 2.0042, 0.55, 0.162,  2.0, 0.022),
    ("Track 3b peak",      397.074, 2.0042, 0.80, 0.05,   2.0, 0.022),
    ("Track 3b alt peak 1", 397.074, 2.0042, 0.73, 0.34,  2.0, 0.022),
    ("Track 3b alt peak 2", 397.074, 2.0042, 0.89, 0.01,  2.0, 0.022),
]


# ─── Scan runners ───────────────────────────────────────────────────

def scan_sheet(sheet_name, eps_grid, s_grid):
    """Run a 2D scan varying one sheet's (ε, s); others held at baseline."""
    n_e, n_s = len(eps_grid), len(s_grid)
    fitness = np.zeros((n_s, n_e))
    fitness.fill(np.nan)
    peak_details = None
    peak_fitness = -np.inf

    t0 = time.time()
    for i, s in enumerate(s_grid):
        for j, eps in enumerate(eps_grid):
            if sheet_name == "p":
                p = build_params(BASELINE['eps_e'], BASELINE['s_e'],
                                 eps, s,
                                 BASELINE['eps_nu'], BASELINE['s_nu'])
            elif sheet_name == "e":
                p = build_params(eps, s,
                                 BASELINE['eps_p'], BASELINE['s_p'],
                                 BASELINE['eps_nu'], BASELINE['s_nu'])
            elif sheet_name == "nu":
                p = build_params(BASELINE['eps_e'], BASELINE['s_e'],
                                 BASELINE['eps_p'], BASELINE['s_p'],
                                 eps, s)
            else:
                raise ValueError(sheet_name)
            if p is None:
                continue
            f, details = score_point(p)
            if isinstance(f, float) and not math.isnan(f):
                fitness[i, j] = f
                if f > peak_fitness:
                    peak_fitness = f
                    peak_details = (eps, s, details)
        elapsed = time.time() - t0
        if (i + 1) % 5 == 0 or i == n_s - 1:
            print(f"    {sheet_name}-sheet  s={s:.4f}  "
                  f"({(i+1)*n_e}/{n_s*n_e}, {elapsed:.1f}s)")
    return fitness, peak_fitness, peak_details


def print_peak(sheet_name, peak_fitness, peak_details, log_file=None):
    def emit(line):
        print(line)
        if log_file is not None:
            log_file.write(line + "\n")

    if peak_details is None:
        emit(f"\n  {sheet_name}-sheet: no valid grid point.\n")
        return

    eps, s, details = peak_details
    emit(f"\n  === {sheet_name}-sheet peak ===")
    emit(f"  (ε, s) = ({eps:.3f}, {s:.4f})   fitness = {peak_fitness:.3f} "
         f"/ {MAX_FITNESS:.0f}")
    emit(f"  {'particle':<10s}  {'E_pred':>10s}  {'Δm/m':>8s}  "
         f"{'Γ/m (width)':>12s}  {'threshold':>10s}  {'closeness':>10s}")
    emit("  " + "-" * 78)
    for (name, E, rel, closeness, thr, tau) in details:
        gamma_over_m = (HBAR_MeV_s / tau) / next(
            m for (n, t, m, q, t2, th) in INVENTORY_WITH_THR if n == name) if tau else 0
        e_str = f"{E:>10.4f}" if E is not None else f"{'nan':>10s}"
        r_str = f"{rel*100:>+7.4f}%" if rel is not None else f"{'':>8s}"
        w_str = f"{gamma_over_m:>10.2e}" if tau else "stable"
        emit(f"  {name:<10s}  {e_str}  {r_str}  {w_str:>12s}  "
             f"{thr*100:>9.4f}%  {closeness:>10.4f}")


# ─── Main ──────────────────────────────────────────────────────────

def evaluate_named_points(log_file):
    print("\n── Named-point evaluations (no grid) ──")
    log_file.write("\n── Named-point evaluations ──\n")
    for (name, ee, se, ep, sp, enu, snu) in NAMED_POINTS:
        p = build_params(ee, se, ep, sp, enu, snu)
        if p is None:
            line = f"  {name}: invalid params"
            print(line); log_file.write(line + "\n")
            continue
        f, details = score_point(p)
        line = (f"  {name:<24s} (εₑ,sₑ,εₚ,sₚ,ε_ν,s_ν) = "
                f"({ee:.3f}, {se:.4f}, {ep:.2f}, {sp:.3f}, {enu:.1f}, {snu:.3f})  "
                f"fitness = {f:.3f} / {MAX_FITNESS:.0f}")
        print(line); log_file.write(line + "\n")
        print_peak(name, f, (ep, sp, details), log_file=log_file)


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)
    log_path = out_dir / "track6_phase6c_peaks.txt"
    log_file = open(log_path, "w")

    print("=" * 100)
    print("R63 Track 6 Phase 6c — Marginal ratio scans (v2 inventory, width-weighted)")
    print("=" * 100)

    # Named-point evaluations first
    evaluate_named_points(log_file)

    # Three marginal scans
    print("\n── p-sheet marginal scan ──")
    p_fit, p_peak_f, p_peak = scan_sheet("p", P_EPS_GRID, P_S_GRID)
    print_peak("p", p_peak_f, p_peak, log_file=log_file)

    print("\n── e-sheet marginal scan ──")
    e_fit, e_peak_f, e_peak = scan_sheet("e", E_EPS_GRID, E_S_GRID)
    print_peak("e", e_peak_f, e_peak, log_file=log_file)

    print("\n── ν-sheet marginal scan ──")
    nu_fit, nu_peak_f, nu_peak = scan_sheet("nu", NU_EPS_GRID, NU_S_GRID)
    print_peak("nu", nu_peak_f, nu_peak, log_file=log_file)

    # Plots
    print("\n── Writing outputs ──")
    plot_heatmap(p_fit, P_EPS_GRID, P_S_GRID, "p-sheet",
                 r"$\varepsilon_p$", r"$s_p$",
                 (BASELINE['eps_p'], BASELINE['s_p']),
                 out_dir / "track6_phase6c_p_sheet.png")
    print(f"  ✓ {out_dir / 'track6_phase6c_p_sheet.png'}")

    plot_heatmap(e_fit, E_EPS_GRID, E_S_GRID, "e-sheet",
                 r"$\varepsilon_e$ (log)", r"$s_e$",
                 (BASELINE['eps_e'], BASELINE['s_e']),
                 out_dir / "track6_phase6c_e_sheet.png",
                 xscale="log")
    print(f"  ✓ {out_dir / 'track6_phase6c_e_sheet.png'}")

    plot_heatmap(nu_fit, NU_EPS_GRID, NU_S_GRID, "ν-sheet",
                 r"$\varepsilon_\nu$", r"$s_\nu$",
                 (BASELINE['eps_nu'], BASELINE['s_nu']),
                 out_dir / "track6_phase6c_nu_sheet.png")
    print(f"  ✓ {out_dir / 'track6_phase6c_nu_sheet.png'}")

    save_grids_csv(p_fit, P_EPS_GRID, P_S_GRID, "p",
                   e_fit, E_EPS_GRID, E_S_GRID, "e",
                   nu_fit, NU_EPS_GRID, NU_S_GRID, "nu",
                   out_dir / "track6_phase6c_grids.csv")
    print(f"  ✓ {out_dir / 'track6_phase6c_grids.csv'}")

    log_file.close()
    print(f"  ✓ {log_path}")


def plot_heatmap(fit, eps_grid, s_grid, title, xlabel, ylabel,
                 baseline_pt, out_path, xscale="linear"):
    fig, ax = plt.subplots(figsize=(12, 8))
    E_grid, S_grid = np.meshgrid(eps_grid, s_grid)

    vmax = float(np.nanmax(fit)) if not np.all(np.isnan(fit)) else MAX_FITNESS
    pcm = ax.pcolormesh(E_grid, S_grid, fit, cmap='viridis',
                        vmin=0, vmax=vmax, shading='auto')

    # Peak
    if not np.all(np.isnan(fit)):
        i_max, j_max = np.unravel_index(np.nanargmax(fit), fit.shape)
        ax.plot(eps_grid[j_max], s_grid[i_max], 'o',
                color='white', markerfacecolor='red', markersize=12,
                markeredgewidth=1.5,
                label=f'peak: ({eps_grid[j_max]:.3f}, {s_grid[i_max]:.4f}) '
                      f'f={fit[i_max, j_max]:.2f}')
    ax.plot(*baseline_pt, '*', color='orange', markersize=16,
            markeredgecolor='black', label=f'baseline {baseline_pt}')

    ax.set_xscale(xscale)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(f"R63 Phase 6c — {title} marginal fitness scan\n"
                 f"19-particle inventory, width-weighted, max = {MAX_FITNESS:.0f}")
    plt.colorbar(pcm, ax=ax, label='fitness')
    ax.legend(loc='lower right', framealpha=0.9)
    ax.grid(alpha=0.2, which='both')
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()


def save_grids_csv(pf, peg, psg, pn, ef, eeg, esg, en,
                   nf, neg, nsg, nn, out_path):
    with open(out_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['sheet', 'eps', 's', 'fitness'])
        for (grid, eps, sg, name) in [(pf, peg, psg, pn),
                                        (ef, eeg, esg, en),
                                        (nf, neg, nsg, nn)]:
            for i, s in enumerate(sg):
                for j, e in enumerate(eps):
                    val = grid[i, j]
                    val_str = f"{val:.4f}" if not math.isnan(val) else ""
                    w.writerow([name, f"{e:.6f}", f"{s:.6f}", val_str])


if __name__ == "__main__":
    main()
