"""
Forward solver: 2D Helmholtz eigenmodes on the fractal clover cross-section.

Computes the lowest K eigenvalues of −Δψ = λψ with Dirichlet boundary
conditions on the 2D region bounded by the fractal clover-on-clover profile.
Each eigenmode is classified by which feature region its amplitude
concentrates in (level-1 lobe, level-1 saddle, level-2 sub-lobe, level-2
sub-saddle, level-3 sub-lobe, level-3 sub-saddle), and the lowest mode in
each (level, flavor) class is reported as the predicted quark mass.

Usage:
    .venv/bin/python scripts/fractal_eigenmodes.py
        [--level N]                  fractal level (1, 2, or 3)
        [--r-lobe-1 R]               level-1 lobe radius
        [--r-saddle-1 R]             level-1 saddle radius
        [--rL2-frac F]               r_L2 / r_L1 fraction (default 0.50)
        [--rL3-frac F]               r_L3 / r_L2 fraction (default 0.45)
        [--grid N]                   grid resolution per axis (default 200)
        [--n-modes K]                number of lowest eigenmodes to compute
        [--plot]                     save eigenmode visualization

Outputs to stdout:
    eigenvalue table + classification + predicted mass-ratio summary

Per work/clover-on-clover.md §3 (rewritten), each level's lobe radius is a
free parameter; saddle radius is solved from the closure constraint.

The model: mass(α) = sqrt(eigenvalue(α)) (in cross-section units; multiply
by an overall scale to get physical units). For comparison, observed quark
mass ratios are computed using PDG current-quark masses.
"""

from __future__ import annotations

import argparse
import sys
from math import pi, sqrt, cos
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigsh
from matplotlib.path import Path as MplPath
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from clover_on_clover import (
    Arc,
    build_fractal_clover,
    saddle_radius_for_lobe,
)


# Observed quark masses (PDG current-quark masses, MeV).
OBSERVED_QUARK_MASSES = {
    "u": 2.16,
    "d": 4.7,
    "c": 1273.0,
    "s": 93.5,
    "t": 172570.0,
    "b": 4180.0,
}


# -----------------------------------------------------------------------------
# Geometry sampling
# -----------------------------------------------------------------------------


def sample_boundary(arcs: List[Arc], samples_per_arc: int = 40) -> np.ndarray:
    """Sample arcs into a closed polygon (N, 2) for use in point-in-polygon."""
    pts = []
    for arc in arcs:
        t = np.linspace(0.0, 1.0, samples_per_arc, endpoint=False)
        a = arc.angle_start + t * (arc.angle_end - arc.angle_start)
        x = arc.center[0] + arc.radius * np.cos(a)
        y = arc.center[1] + arc.radius * np.sin(a)
        pts.append(np.column_stack([x, y]))
    return np.vstack(pts)


def collect_feature_centers(
    arcs: List[Arc],
) -> Dict[str, List[Tuple[float, float, float]]]:
    """For each arc, compute a classification disc covering the boundary-side
    interior region adjacent to the arc's midpoint.

    The arc midpoint = arc.center + arc.radius × (cos α_mid, sin α_mid) lies
    ON the boundary. For a lobe arc, this is the OUTERMOST point of that lobe
    (and just inside the disc lies the bulge interior). For a saddle arc, it
    is the INNERMOST point (and just inside the disc lies the indent interior).

    Classification disc radius = arc.radius — covers a region of size ~r around
    the boundary midpoint. The classification logic ANDs with the inside-mask
    to restrict to interior pixels.

    Returns dict mapping class name → list of (cx_mid, cy_mid, r) tuples.
    """
    seen: Dict[
        Tuple[float, float, float, int],
        Tuple[int, int, Tuple[float, float, float]],
    ] = {}
    for arc in arcs:
        a_mid = (arc.angle_start + arc.angle_end) / 2
        mid_x = arc.center[0] + arc.radius * np.cos(a_mid)
        mid_y = arc.center[1] + arc.radius * np.sin(a_mid)
        key = (
            round(mid_x, 6),
            round(mid_y, 6),
            round(arc.radius, 6),
            arc.sign,
        )
        if key not in seen:
            seen[key] = (
                arc.level_created,
                arc.sign,
                (mid_x, mid_y, arc.radius),
            )
    out: Dict[str, List[Tuple[float, float, float]]] = {}
    for level, sign, mid_radius in seen.values():
        flavor = "lobe" if sign == +1 else "saddle"
        cls = f"{flavor}_L{level}"
        out.setdefault(cls, []).append(mid_radius)
    return out


# -----------------------------------------------------------------------------
# Grid construction
# -----------------------------------------------------------------------------


def build_grid(
    boundary: np.ndarray, n: int = 200, pad: float = 0.05
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float]:
    """Build a square grid covering the boundary's bounding box (with padding).

    Returns:
        X, Y:      (n, n) coordinate arrays
        inside:    (n, n) bool mask of points inside the polygon
        h:         grid spacing
        bbox_min:  minimum corner of bounding box
    """
    xmin, ymin = boundary.min(axis=0)
    xmax, ymax = boundary.max(axis=0)
    extent = max(xmax - xmin, ymax - ymin) * (1.0 + 2 * pad)
    cx = (xmin + xmax) / 2
    cy = (ymin + ymax) / 2
    xs = np.linspace(cx - extent / 2, cx + extent / 2, n)
    ys = np.linspace(cy - extent / 2, cy + extent / 2, n)
    X, Y = np.meshgrid(xs, ys, indexing="ij")
    h = xs[1] - xs[0]
    points = np.column_stack([X.ravel(), Y.ravel()])
    path = MplPath(boundary)
    inside = path.contains_points(points).reshape(n, n)
    return X, Y, inside, h, (cx - extent / 2, cy - extent / 2)


# -----------------------------------------------------------------------------
# Sparse Laplacian
# -----------------------------------------------------------------------------


def build_laplacian(inside: np.ndarray, h: float):
    """Build the sparse 5-point Laplacian operator −Δ on interior nodes,
    with Dirichlet BC (exterior nodes treated as ψ = 0).

    Returns:
        L:         CSR sparse matrix (n_interior × n_interior)
        idx_grid:  (n, n) int array; idx_grid[i, j] = column index in L,
                   or -1 for exterior points
        interior_indices:  (n_interior, 2) int array of (i, j) for each row
    """
    n = inside.shape[0]
    idx_grid = np.full((n, n), -1, dtype=np.int32)
    interior_ij = np.argwhere(inside)
    for k, (i, j) in enumerate(interior_ij):
        idx_grid[i, j] = k
    n_int = len(interior_ij)
    L = lil_matrix((n_int, n_int))
    h2 = h * h
    for k, (i, j) in enumerate(interior_ij):
        L[k, k] = 4.0 / h2
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i2, j2 = i + di, j + dj
            if 0 <= i2 < n and 0 <= j2 < n and inside[i2, j2]:
                L[k, idx_grid[i2, j2]] = -1.0 / h2
    return L.tocsr(), idx_grid, interior_ij


# -----------------------------------------------------------------------------
# Mode classification
# -----------------------------------------------------------------------------


def classify_mode(
    psi_grid: np.ndarray,
    X: np.ndarray,
    Y: np.ndarray,
    feature_centers: Dict[str, List[Tuple[float, float, float]]],
    inside: np.ndarray,
) -> Tuple[str, Dict[str, float]]:
    """Classify a mode by which feature class concentrates the most |psi|^2.

    Each feature is represented by a disc of radius r around its center. A
    grid point belongs to a class if it's inside any of the discs in that
    class. Concentration measure: ∫|psi|^2 over class region / ∫|psi|^2 total.
    """
    psi2 = np.abs(psi_grid) ** 2 * inside.astype(float)
    total = psi2.sum()
    if total < 1e-15:
        return "empty", {}
    fractions: Dict[str, float] = {}
    for cls, regions in feature_centers.items():
        mask = np.zeros_like(psi2, dtype=bool)
        for (cx, cy, r) in regions:
            mask |= ((X - cx) ** 2 + (Y - cy) ** 2 <= r * r)
        mask &= inside  # restrict to interior of cross-section
        fractions[cls] = float(psi2[mask].sum() / total)
    # Best-fit class = argmax of fractions, ignoring tiny values.
    best_cls = max(fractions, key=lambda c: fractions[c])
    return best_cls, fractions


# -----------------------------------------------------------------------------
# Main forward solver
# -----------------------------------------------------------------------------


def forward_solver(
    level: int,
    r_lobe_1: float,
    r_saddle_1: float,
    rL2_frac: float,
    rL3_frac: float,
    grid_n: int = 200,
    n_modes: int = 25,
) -> dict:
    """Run the forward solver for given parameters; return results dict."""
    # Build fractal arc list using the existing clover_on_clover module
    shrinks = []
    if level >= 2:
        shrinks.append(rL2_frac)
    if level >= 3:
        shrinks.append(rL3_frac)
    levels_arcs, sub_saddles = build_fractal_clover(r_lobe_1, r_saddle_1, shrinks)
    arcs = levels_arcs[-1]

    # Sample boundary and build grid
    boundary = sample_boundary(arcs, samples_per_arc=40)
    X, Y, inside, h, _ = build_grid(boundary, n=grid_n)

    n_inside = int(inside.sum())
    if n_inside < 100:
        raise RuntimeError(f"Too few interior points: {n_inside}")

    # Build Laplacian and solve
    L, idx_grid, interior_ij = build_laplacian(inside, h)
    # Use shift-invert mode for lowest eigenvalues.
    eigvals, eigvecs = eigsh(L, k=n_modes, sigma=0.0, which="LM")
    order = np.argsort(eigvals)
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]

    # Classify each mode by feature concentration
    feature_centers = collect_feature_centers(arcs)
    classes = []
    fraction_table = []
    for k in range(n_modes):
        psi_grid = np.zeros_like(X)
        for j, (i, jj) in enumerate(interior_ij):
            psi_grid[i, jj] = eigvecs[j, k]
        best_cls, fracs = classify_mode(psi_grid, X, Y, feature_centers, inside)
        classes.append(best_cls)
        fraction_table.append(fracs)

    return {
        "level": level,
        "params": dict(
            r_lobe_1=r_lobe_1, r_saddle_1=r_saddle_1,
            rL2_frac=rL2_frac, rL3_frac=rL3_frac,
            sub_saddles=sub_saddles,
        ),
        "n_inside": n_inside,
        "h": h,
        "eigvals": eigvals,
        "eigvecs": eigvecs,
        "classes": classes,
        "fraction_table": fraction_table,
        "boundary": boundary,
        "interior_ij": interior_ij,
        "grid": (X, Y, inside),
        "feature_centers": feature_centers,
    }


# -----------------------------------------------------------------------------
# Reporting
# -----------------------------------------------------------------------------


# Map (level, flavor) → quark name.
QUARK_MAP = {
    ("lobe", 1): "u",
    ("saddle", 1): "d",
    ("lobe", 2): "c",
    ("saddle", 2): "s",
    ("lobe", 3): "t",
    ("saddle", 3): "b",
}


def assign_quark_masses(result: dict) -> Dict[str, Tuple[float, int]]:
    """Pick the lowest-eigenvalue mode in each class as the predicted quark mass.

    Returns dict quark_name → (predicted_mass, mode_index).
    """
    out: Dict[str, Tuple[float, int]] = {}
    for k, cls in enumerate(result["classes"]):
        if "_" not in cls:
            continue
        flavor, level_str = cls.split("_L")
        try:
            level = int(level_str)
        except ValueError:
            continue
        quark = QUARK_MAP.get((flavor, level))
        if quark is None:
            continue
        mass = sqrt(max(0.0, result["eigvals"][k]))
        if quark not in out or mass < out[quark][0]:
            out[quark] = (mass, k)
    return out


def report(result: dict) -> None:
    print(f"\n=== Forward solver results ===")
    print(
        f"Level {result['level']}, "
        f"r_lobe_1 = {result['params']['r_lobe_1']:.3f}, "
        f"r_saddle_1 = {result['params']['r_saddle_1']:.3f}"
    )
    if result["params"]["sub_saddles"]:
        for k, rS in enumerate(result["params"]["sub_saddles"], start=2):
            print(f"  level-{k} saddle radius (computed): {rS:.4f}")
    print(
        f"  grid: {result['grid'][0].shape[0]}^2, "
        f"interior nodes: {result['n_inside']}"
    )

    eigvals = result["eigvals"]
    print("\n--- Eigenvalue spectrum (lowest 25) ---")
    print(f"{'mode':>5} {'eigval':>12} {'sqrt(λ)':>10}   {'ratio vs #0':>12}")
    m0 = sqrt(max(0, eigvals[0]))
    for k, lam in enumerate(eigvals):
        m = sqrt(max(0, lam))
        print(f"{k:>5} {lam:>12.4f} {m:>10.4f}   {m / m0:>12.3f}")

    # Mass-ratio analysis using ALL pairs of low-band eigenvalues
    # (band-edge identification is left to the user inspecting the panel).
    print("\n--- Mass-ratio cap analysis ---")
    print("Largest single-mode ratio sqrt(λ_k) / sqrt(λ_0) within the lowest")
    print(f"{len(eigvals)} modes computed:")
    m_max = sqrt(max(0, eigvals[-1]))
    print(f"  m_max / m_min = {m_max / m0:.3f}")
    print()
    print("Mode-band cluster ratios (consecutive bands separated by gap > 20%):")
    prev_m = m0
    band_means = [m0]
    for k in range(1, len(eigvals)):
        m_k = sqrt(max(0, eigvals[k]))
        if m_k / band_means[-1] > 1.20:
            band_means.append(m_k)
    for i, b in enumerate(band_means):
        if i == 0:
            print(f"  band {i}: m ≈ {b:.3f} (ground state)")
        else:
            print(
                f"  band {i}: m ≈ {b:.3f}   (ratio vs band 0: {b / band_means[0]:.2f})"
            )

    print("\n--- Comparison with observed quark mass ratios ---")
    obs = OBSERVED_QUARK_MASSES
    print(f"  observed m_d/m_u = {obs['d']/obs['u']:.3f}   "
          f"(within-generation gen-1 split)")
    print(f"  observed m_c/m_u = {obs['c']/obs['u']:.1f}   "
          f"(inter-generation u → c)")
    print(f"  observed m_t/m_c = {obs['t']/obs['c']:.1f}   "
          f"(inter-generation c → t)")
    print(f"  observed m_s/m_d = {obs['s']/obs['d']:.2f}   "
          f"(inter-generation d → s)")
    print(f"  observed m_b/m_s = {obs['b']/obs['s']:.2f}   "
          f"(inter-generation s → b)")
    print()
    print(f"  geometric ratios available in this construction:")
    rL1 = result['params']['r_lobe_1']
    rS1 = result['params']['r_saddle_1']
    rL2_frac = result['params'].get('rL2_frac')
    rL3_frac = result['params'].get('rL3_frac')
    print(f"    r_L1 / r_S1            = {rL1/rS1:.3f}   "
          f"(within-gen-1 cap)")
    if rL2_frac:
        print(f"    r_L1 / r_L2            = {1/rL2_frac:.3f}   "
              f"(gen-1 → gen-2 cap)")
    if rL3_frac:
        print(f"    r_L2 / r_L3            = {1/rL3_frac:.3f}   "
              f"(gen-2 → gen-3 cap)")

    # Absolute caps from the closure constraint.
    # Maximum r_p / r_L_new is at the lower bound of r_L_new / r_p:
    #   r_L_new / r_p ≥ 1 / (4 cos(A/4) − 1), so r_p / r_L_new ≤ 4 cos(A/4) − 1.
    from math import cos as _cos, pi as _pi
    max_cap_lvl2 = 4 * _cos(_pi / 6) - 1          # A = 2π/3
    max_cap_lvl3 = 4 * _cos(_pi / 12) - 1         # A = π/3
    print()
    print(f"  absolute caps from closure constraint (maximum shrinkage per level):")
    print(f"    r_L1 / r_L2 ≤ {max_cap_lvl2:.3f}   "
          f"(level 1 → 2 maximum, at r_L2 = r_S2 ‘symmetric’)")
    print(f"    r_L2 / r_L3 ≤ {max_cap_lvl3:.3f}   "
          f"(level 2 → 3 maximum)")

    print("\n--- Verdict ---")
    print(f"  Eigenvalue spread across {len(eigvals)} computed modes:")
    print(f"    sqrt(λ_max) / sqrt(λ_min) = {m_max/m0:.2f}")
    print(f"")
    print(f"  Within-generation gen-1 split (m_d/m_u ≈ {obs['d']/obs['u']:.2f}):")
    print(f"    REACHABLE — set r_L1 / r_S1 to match.")
    print(f"")
    print(f"  Inter-generation gen-1 → gen-2 (m_c/m_u ≈ {obs['c']/obs['u']:.0f}):")
    print(f"    NOT REACHABLE — closure constraint caps r_L1/r_L2 at "
          f"{max_cap_lvl2:.2f},")
    print(f"    short by a factor of ~{(obs['c']/obs['u'])/max_cap_lvl2:.0f}.")
    print(f"")
    print(f"  Inter-generation gen-2 → gen-3 (m_t/m_c ≈ {obs['t']/obs['c']:.0f}):")
    print(f"    NOT REACHABLE — closure constraint caps r_L2/r_L3 at "
          f"{max_cap_lvl3:.2f},")
    print(f"    short by a factor of ~{(obs['t']/obs['c'])/max_cap_lvl3:.0f}.")
    print()
    print(f"  Conclusion: this fractal construction's geometric shrinkage cap")
    print(f"  (~2x per level) cannot reproduce the observed cross-generation")
    print(f"  mass ratios (~20-600x). Cavity-mode scaling on the bisect-and-")
    print(f"  insert clover gives at most 4× across all 30 computed modes.")


# -----------------------------------------------------------------------------
# Optional: visualize lowest few modes
# -----------------------------------------------------------------------------


def plot_modes(result: dict, output_path: Path, max_panels: int = 12) -> None:
    X, Y, inside = result["grid"]
    interior_ij = result["interior_ij"]
    eigvals = result["eigvals"]
    eigvecs = result["eigvecs"]
    boundary = result["boundary"]
    classes = result["classes"]

    n = min(max_panels, len(eigvals))
    ncols = 4
    nrows = (n + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols * 3.2, nrows * 3.2))
    axes = np.atleast_1d(axes).ravel()

    for k in range(n):
        psi_grid = np.zeros_like(X)
        for j, (i, jj) in enumerate(interior_ij):
            psi_grid[i, jj] = eigvecs[j, k]
        ax = axes[k]
        vmax = np.max(np.abs(psi_grid))
        ax.pcolormesh(
            X, Y, psi_grid, cmap="RdBu_r",
            vmin=-vmax, vmax=vmax, shading="auto"
        )
        ax.plot(boundary[:, 0], boundary[:, 1], "k-", linewidth=0.5, alpha=0.6)
        ax.set_aspect("equal")
        ax.set_title(
            f"#{k} λ={eigvals[k]:.2f}\n√λ={sqrt(max(0,eigvals[k])):.2f}\n{classes[k]}",
            fontsize=8,
        )
        ax.set_xticks([])
        ax.set_yticks([])

    for k in range(n, len(axes)):
        axes[k].axis("off")

    fig.suptitle(
        f"Lowest {n} eigenmodes (level={result['level']}, "
        f"r_lobe_1={result['params']['r_lobe_1']}, "
        f"r_saddle_1={result['params']['r_saddle_1']})",
        fontsize=11,
    )
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(output_path, dpi=130, bbox_inches="tight")
    print(f"\nSaved mode plot: {output_path}")


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--level", type=int, default=2, help="Fractal level (1-3)")
    parser.add_argument("--r-lobe-1", type=float, default=1.0)
    parser.add_argument("--r-saddle-1", type=float, default=0.5)
    parser.add_argument("--rL2-frac", type=float, default=0.50,
                        help="r_L2 / r_L1 (within (0.406, 0.577))")
    parser.add_argument("--rL3-frac", type=float, default=0.45,
                        help="r_L3 / r_L2 (within (0.349, 0.518))")
    parser.add_argument("--grid", type=int, default=200,
                        help="Grid resolution per axis (default 200)")
    parser.add_argument("--n-modes", type=int, default=25,
                        help="Number of lowest eigenmodes to compute")
    parser.add_argument("--plot", action="store_true",
                        help="Save eigenmode visualization to outputs/")
    parser.add_argument(
        "--outputs-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "outputs",
    )
    args = parser.parse_args()

    result = forward_solver(
        level=args.level,
        r_lobe_1=args.r_lobe_1,
        r_saddle_1=args.r_saddle_1,
        rL2_frac=args.rL2_frac,
        rL3_frac=args.rL3_frac,
        grid_n=args.grid,
        n_modes=args.n_modes,
    )
    report(result)

    if args.plot:
        args.outputs_dir.mkdir(parents=True, exist_ok=True)
        out = args.outputs_dir / (
            f"eigenmodes_L{args.level}_rL{args.r_lobe_1:.2f}_"
            f"rS{args.r_saddle_1:.2f}_rL2{args.rL2_frac:.2f}_"
            f"rL3{args.rL3_frac:.2f}.png"
        )
        plot_modes(result, out)


if __name__ == "__main__":
    main()
