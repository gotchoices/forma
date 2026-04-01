#!/usr/bin/env python3
"""sim-gravity-2: scalar baseline.

Two-part test on a vertex-based Gaussian scalar field:

Part 1 — MEAN FIELD (direct solve, no MC):
  Solve ∇²φ = 0 with φ pinned at defect.
  Expected: φ(r) ∝ log(r) → dφ/dr ∝ 1/r.
  This is the 2D gravitational potential/force.

Part 2 — ENTROPY SHADOW (Monte Carlo):
  Sample φ at finite temperature T with pinned defect.
  Measure local variance (entropy proxy) vs distance.
  Expected: var(φ) reduced near defect, deficit ∝ log(r).

Usage:
    source .venv/bin/activate
    python grid/sim-gravity-2/run_scalar.py
"""

import os
import sys
import time
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                "..", "sim-gravity"))
from lattice import make_lattice, boundary_vertices


def find_defect(pos, edges, centre=None):
    """Return frozenset of hexagonal defect vertex indices."""
    if centre is None:
        centre = pos.mean(axis=0)
    c = int(np.argmin(np.sum((pos - centre) ** 2, axis=1)))
    nbrs = set()
    for a, b in edges:
        if a == c:
            nbrs.add(b)
        elif b == c:
            nbrs.add(a)
    return frozenset([c] + sorted(nbrs))


def build_laplacian(n_verts, edges):
    """Build the graph Laplacian as a sparse matrix."""
    row, col, data = [], [], []
    degree = np.zeros(n_verts)
    for a, b in edges:
        row.extend([a, b, a, b])
        col.extend([b, a, a, b])
        data.extend([-1, -1, 1, 1])
        degree[a] += 1
        degree[b] += 1
    L = sparse.csr_matrix((data, (row, col)), shape=(n_verts, n_verts))
    return L


# ── Part 1: Mean field (direct Laplacian solve) ──────────────

def solve_mean_field(nx, ny, label):
    """Solve ∇²φ = 0 with φ=1 at defect, φ=0 at boundary."""
    print(f"\n{'='*60}")
    print(f"  Part 1: Mean field — {label}")
    print(f"{'='*60}")

    pos, edges, _ = make_lattice(nx, ny, periodic=False)
    n = len(pos)
    defect = find_defect(pos, edges)
    bnd = boundary_vertices(nx, ny)
    fixed = defect | bnd
    free = sorted(set(range(n)) - fixed)
    print(f"  Vertices: {n}, Free: {len(free)}, "
          f"Defect: {len(defect)}, Boundary: {len(bnd)}")

    L = build_laplacian(n, edges)

    free_idx = np.array(free)
    fixed_idx = np.array(sorted(fixed))

    phi_fixed = np.zeros(n)
    for v in defect:
        phi_fixed[v] = 1.0

    # Solve L_ff · φ_free = -L_fc · φ_fixed
    L_ff = L[np.ix_(free_idx, free_idx)]
    L_fc = L[np.ix_(free_idx, fixed_idx)]
    rhs = -L_fc.dot(phi_fixed[fixed_idx])

    t0 = time.time()
    phi_free = spsolve(L_ff, rhs)
    dt = time.time() - t0
    print(f"  Solved in {dt:.3f}s")

    phi = phi_fixed.copy()
    phi[free_idx] = phi_free

    # Measure radial profile
    centre = pos[sorted(defect)].mean(axis=0)
    r = np.sqrt(np.sum((pos - centre) ** 2, axis=1))

    # Exclude fixed vertices from analysis
    analysis = sorted(set(range(n)) - fixed)
    r_a = r[analysis]
    phi_a = phi[analysis]

    # Bin
    r_mid, phi_mean = _bin(r_a, phi_a, n_bins=60)

    # Fit log
    half_box = min(nx, ny * np.sqrt(3) / 2) / 2
    fit_rmin, fit_rmax = 3.0, half_box * 0.45
    A, B, phi_fit, r2 = _fit_log(r_mid, phi_mean, fit_rmin, fit_rmax)
    print(f"  φ(r) = {A:.4e}·log(r) + {B:.4e},  R² = {r2:.4f}")

    # Strain
    r_s, strain, p, r2_s, strain_fit = _strain_fit(
        r_mid, phi_mean, fit_rmin, fit_rmax)
    print(f"  dφ/dr ∝ r^(−{p:.3f}),  R² = {r2_s:.4f}")
    print(f"  *** Expect: φ ∝ log(r), dφ/dr ∝ 1/r (p≈1) ***")

    return {
        "label": label + " (mean field)",
        "r_mid": r_mid, "y_mean": phi_mean, "y_fit": phi_fit,
        "A": A, "r2": r2,
        "r_s": r_s, "strain": strain, "strain_fit": strain_fit,
        "p": p, "r2_s": r2_s,
        "fit_rmin": fit_rmin, "fit_rmax": fit_rmax,
    }


# ── Part 2: Entropy shadow (vectorised MC) ───────────────────

def run_mc_entropy(nx, ny, T, n_therm, n_measure, label):
    """MC on vertex scalars; measure variance profile."""
    print(f"\n{'='*60}")
    print(f"  Part 2: MC entropy — {label}, T={T}")
    print(f"{'='*60}")

    pos, edges, _ = make_lattice(nx, ny, periodic=False)
    n = len(pos)
    defect = find_defect(pos, edges)
    bnd = boundary_vertices(nx, ny)
    fixed = defect | bnd
    free_idx = np.array(sorted(set(range(n)) - fixed))
    n_free = len(free_idx)
    print(f"  Vertices: {n}, Free: {n_free}")

    # Build neighbor list for free vertices (for vectorised local energy)
    nbr_list = [[] for _ in range(n)]
    for a, b in edges:
        nbr_list[a].append(b)
        nbr_list[b].append(a)

    phi = np.zeros(n)
    for v in defect:
        phi[v] = 1.0

    # Precompute: sum of neighbor values for local energy delta
    def local_energy_change(idx, new_vals):
        """Vectorised ΔE for changing phi[free_idx] to new_vals."""
        dE = np.zeros(len(idx))
        for k, vi in enumerate(idx):
            old_v = phi[vi]
            new_v = new_vals[k]
            de = 0.0
            for nj in nbr_list[vi]:
                de += (new_v - phi[nj]) ** 2 - (old_v - phi[nj]) ** 2
            dE[k] = 0.5 * de
        return dE

    step = np.sqrt(T) * 0.5
    accept = 0
    total = 0

    t0 = time.time()

    # Thermalise
    for sweep in range(n_therm):
        proposals = phi[free_idx] + step * np.random.randn(n_free)
        dE = local_energy_change(free_idx, proposals)
        accept_mask = (dE < 0) | (np.random.random(n_free) < np.exp(-dE / T))
        phi[free_idx[accept_mask]] = proposals[accept_mask]
        accept += accept_mask.sum()
        total += n_free
        if (sweep + 1) % 200 == 0:
            print(f"    Therm {sweep+1}/{n_therm}, "
                  f"acc={accept/total:.3f}")

    print(f"  Thermalised ({time.time()-t0:.1f}s)")
    accept = 0
    total = 0

    phi_sum = np.zeros(n)
    phi_sq_sum = np.zeros(n)
    n_samples = 0

    for sweep in range(n_measure):
        proposals = phi[free_idx] + step * np.random.randn(n_free)
        dE = local_energy_change(free_idx, proposals)
        accept_mask = (dE < 0) | (np.random.random(n_free) < np.exp(-dE / T))
        phi[free_idx[accept_mask]] = proposals[accept_mask]
        accept += accept_mask.sum()
        total += n_free

        if (sweep + 1) % 3 == 0:
            phi_sum += phi
            phi_sq_sum += phi ** 2
            n_samples += 1

        if (sweep + 1) % 500 == 0:
            print(f"    Meas {sweep+1}/{n_measure}, "
                  f"acc={accept/total:.3f}")

    dt = time.time() - t0
    print(f"  Done ({dt:.1f}s), {n_samples} samples, "
          f"acc={accept/total:.3f}")

    phi_mean = phi_sum / n_samples
    phi_var = phi_sq_sum / n_samples - phi_mean ** 2

    centre = pos[sorted(defect)].mean(axis=0)
    r = np.sqrt(np.sum((pos - centre) ** 2, axis=1))

    analysis = sorted(set(range(n)) - fixed)
    r_a = r[analysis]
    var_a = phi_var[analysis]
    mean_a = np.abs(phi_mean[analysis])

    # Bin variance
    r_mid_v, var_mean = _bin(r_a, var_a, n_bins=50)
    # Bin mean
    r_mid_m, mean_mean = _bin(r_a, mean_a, n_bins=50)

    half_box = min(nx, ny * np.sqrt(3) / 2) / 2
    fit_rmin, fit_rmax = 3.0, half_box * 0.45

    # Fit mean field log
    A_m, B_m, mean_fit, r2_m = _fit_log(r_mid_m, mean_mean,
                                         fit_rmin, fit_rmax)
    print(f"  ⟨|φ|⟩: A·log(r)+B, A={A_m:.4e}, R²={r2_m:.4f}")

    # Fit variance log (entropy shadow)
    A_v, B_v, var_fit, r2_v = _fit_log(r_mid_v, var_mean,
                                        fit_rmin, fit_rmax)
    print(f"  var(φ): A·log(r)+B, A={A_v:.4e}, R²={r2_v:.4f}")

    # Strain on mean field
    r_s, strain, p, r2_s, strain_fit = _strain_fit(
        r_mid_m, mean_mean, fit_rmin, fit_rmax)
    print(f"  d⟨|φ|⟩/dr ∝ r^(−{p:.3f}), R²={r2_s:.4f}")
    print(f"  *** Expect: mean ∝ log(r), var ∝ log(r), "
          f"strain ∝ 1/r ***")

    return {
        "label": label + f" MC T={T}",
        "r_mid": r_mid_m, "y_mean": mean_mean, "y_fit": mean_fit,
        "A": A_m, "r2": r2_m,
        "r_s": r_s, "strain": strain, "strain_fit": strain_fit,
        "p": p, "r2_s": r2_s,
        "fit_rmin": fit_rmin, "fit_rmax": fit_rmax,
        "r_mid_v": r_mid_v, "var_mean": var_mean,
        "var_fit": var_fit, "A_v": A_v, "r2_v": r2_v,
    }


# ── Utilities ─────────────────────────────────────────────────

def _bin(r, y, n_bins=60):
    r_max = r.max()
    edges = np.linspace(0, r_max, n_bins + 1)
    rm, ym = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        mask = (r >= lo) & (r < hi)
        if mask.sum() < 3:
            continue
        rm.append(0.5 * (lo + hi))
        ym.append(y[mask].mean())
    return np.array(rm), np.array(ym)


def _fit_log(r_mid, y, rmin, rmax):
    mask = (r_mid >= rmin) & (r_mid <= rmax) & (y > 0)
    if mask.sum() < 3:
        return np.nan, np.nan, np.full_like(r_mid, np.nan), 0.0
    lr = np.log(r_mid[mask])
    A_mat = np.column_stack([lr, np.ones_like(lr)])
    c, *_ = np.linalg.lstsq(A_mat, y[mask], rcond=None)
    A, B = c
    pred = A * lr + B
    ss_r = np.sum((y[mask] - pred) ** 2)
    ss_t = np.sum((y[mask] - y[mask].mean()) ** 2)
    r2 = 1.0 - ss_r / ss_t if ss_t > 0 else 0.0
    return A, B, A * np.log(r_mid) + B, r2


def _strain_fit(r_mid, y, rmin, rmax):
    dr = np.diff(r_mid)
    dy = np.diff(y)
    strain = np.abs(dy / dr)
    rs = 0.5 * (r_mid[:-1] + r_mid[1:])
    mask = (rs >= rmin) & (rs <= rmax) & (strain > 0)
    if mask.sum() < 3:
        return rs, strain, np.nan, 0.0, np.full_like(rs, np.nan)
    lr = np.log(rs[mask])
    ls = np.log(strain[mask])
    c = np.polyfit(lr, ls, 1)
    p = -c[0]
    A = np.exp(c[1])
    pred = c[0] * lr + c[1]
    ss_r = np.sum((ls - pred) ** 2)
    ss_t = np.sum((ls - ls.mean()) ** 2)
    r2 = 1.0 - ss_r / ss_t if ss_t > 0 else 0.0
    return rs, strain, p, r2, A * rs ** (-p)


# ── Plotting ──────────────────────────────────────────────────

def plot_all(results, out_dir):
    n = len(results)
    fig, axes = plt.subplots(n, 2, figsize=(13, 4.2 * n))
    if n == 1:
        axes = axes[np.newaxis, :]

    for i, d in enumerate(results):
        # Left: potential
        ax = axes[i, 0]
        ax.plot(d["r_mid"], d["y_mean"], "bo", ms=3, alpha=0.7)
        v = np.isfinite(d["y_fit"])
        if v.any():
            ax.plot(d["r_mid"][v], d["y_fit"][v], "r-", lw=2,
                    label=f"A·log(r)+B, R²={d['r2']:.3f}")
        ax.axvline(d["fit_rmin"], color="gray", ls=":", alpha=0.4)
        ax.axvline(d["fit_rmax"], color="gray", ls=":", alpha=0.4)
        ax.set_xlabel("r")
        ax.set_ylabel("⟨|φ|⟩" if "MC" in d["label"] else "φ(r)")
        ax.set_title(d["label"] + " — potential")
        ax.legend(fontsize=7)
        ax.grid(True, alpha=0.3)

        # Right: force
        ax2 = axes[i, 1]
        if len(d["strain"]) > 0:
            pos = d["strain"] > 0
            ax2.plot(d["r_s"][pos], d["strain"][pos], "bo", ms=3,
                     alpha=0.7)
            v2 = np.isfinite(d["strain_fit"]) & (d["strain_fit"] > 0)
            if v2.any():
                ax2.plot(d["r_s"][v2], d["strain_fit"][v2], "r-", lw=2,
                         label=f"r$^{{-{d['p']:.2f}}}$,"
                               f" R²={d['r2_s']:.3f}")
        ax2.axvline(d["fit_rmin"], color="gray", ls=":", alpha=0.4)
        ax2.axvline(d["fit_rmax"], color="gray", ls=":", alpha=0.4)
        ax2.set_xscale("log")
        ax2.set_yscale("log")
        ax2.set_xlabel("r")
        ax2.set_ylabel("|dφ/dr|")
        ax2.set_title(d["label"] + " — force")
        ax2.legend(fontsize=7)
        ax2.grid(True, alpha=0.3)

    fig.suptitle("sim-gravity-2: scalar field — potential and force",
                 fontsize=14, y=1.0)
    fig.tight_layout()
    p1 = os.path.join(out_dir, "scalar_baseline.png")
    fig.savefig(p1, dpi=150, bbox_inches="tight")
    print(f"\n  Saved: {p1}")
    plt.close("all")


# ── Main ──────────────────────────────────────────────────────

def main():
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(out_dir, exist_ok=True)

    results = []

    # Part 1: direct solve (instant)
    results.append(solve_mean_field(100, 100, "100²"))
    results.append(solve_mean_field(200, 200, "200²"))

    # Part 2: MC entropy (small lattice for speed)
    results.append(run_mc_entropy(40, 40, T=1.0,
                                  n_therm=500, n_measure=3000,
                                  label="40²"))

    print(f"\n{'='*60}")
    print("  SUMMARY")
    print(f"{'='*60}")
    print(f"  {'Trial':<30s}  {'A':>9s}  {'R²':>6s}"
          f"  {'p':>6s}  {'R²_s':>6s}")
    print(f"  {'-'*30}  {'-'*9}  {'-'*6}  {'-'*6}  {'-'*6}")
    for d in results:
        print(f"  {d['label']:<30s}  {d['A']:9.4e}  {d['r2']:6.3f}"
              f"  {d['p']:6.3f}  {d['r2_s']:6.3f}")
    print()
    print("  2D gravity: potential ∝ log(r), force ∝ 1/r → p ≈ 1.0")

    plot_all(results, out_dir)


if __name__ == "__main__":
    main()
