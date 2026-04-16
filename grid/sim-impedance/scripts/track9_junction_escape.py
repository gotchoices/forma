#!/usr/bin/env python3
"""
Track 9 — Junction escape fraction: geometric energy leakage
at a single curved Y-junction on a torus.

On a flat hexagonal sheet, the three edges at a Y-junction
are coplanar.  An incoming unit vector along one edge can be
fully decomposed into the plane of the two outgoing edges.

On a curved torus, the three edges are NOT coplanar.  The
incoming vector has a component perpendicular to the plane of
the outgoing edges — the "escape component."

    f_esc = (ê_in · n̂_outgoing_plane)²

This script computes f_esc at every node on the torus for
two lattice mapping methods:

  Method A — Equal edge lengths: hexagons distort (squish)
             to keep all edges = L.

  Method B — Conformal: edge lengths vary with the metric
             factor p = 1 + ε cos θ₁.

We sweep over lattice resolution (N) and aspect ratio (ε)
and compare f_esc to α ≈ 1/137.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "output"
OUT.mkdir(exist_ok=True)

ALPHA = 1 / 137.036
TAU = 2 * np.pi


# ── Torus geometry ───────────────────────────────────────

def torus_pos(th1, th2, R, a):
    """3D position on a torus with major radius R, minor radius a."""
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    rr = R + a * ct1
    return np.array([rr * cp, a * st1, rr * sp])


def torus_surface_normal(th1, th2):
    """Outward unit normal to the torus surface at (θ₁, θ₂)."""
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    return np.array([ct1 * cp, st1, ct1 * sp])


# ── Honeycomb lattice on a torus ─────────────────────────

def build_honeycomb_torus(N1, N2, R, a, method="conformal"):
    """
    Build a honeycomb lattice on a torus.

    N1 = cells around the tube (θ₁ direction)
    N2 = cells around the ring (θ₂ direction)
    method = "conformal" (B) or "equal_edge" (A)

    Returns:
        positions: (M, 3) array of 3D node positions
        angles:    (M, 2) array of (θ₁, θ₂) per node
        neighbors: list of lists — neighbors[i] = [j1, j2, j3]
    """
    positions = []
    angles = []
    node_map = {}

    for i1 in range(N1):
        for i2 in range(N2):
            for sub in range(2):
                if method == "conformal":
                    th1 = TAU * (i1 + 0.25 * sub) / N1
                    th2 = TAU * (i2 + 0.5 * sub) / N2
                elif method == "equal_edge":
                    th1 = TAU * (i1 + 0.25 * sub) / N1
                    th2 = TAU * (i2 + 0.5 * sub) / N2
                else:
                    raise ValueError(f"Unknown method: {method}")

                idx = len(positions)
                node_map[(i1, i2, sub)] = idx
                pos = torus_pos(th1, th2, R, a)
                positions.append(pos)
                angles.append([th1, th2])

    M = len(positions)
    neighbors = [[] for _ in range(M)]

    for i1 in range(N1):
        for i2 in range(N2):
            A_idx = node_map[(i1, i2, 0)]
            B_idx = node_map[(i1, i2, 1)]

            # A-sublattice (sub=0) connects to:
            #   B in same cell, B in cell (i1, i2-1), B in cell (i1-1, i2)
            neighbors[A_idx].append(B_idx)
            neighbors[A_idx].append(node_map[(i1, (i2 - 1) % N2, 1)])
            neighbors[A_idx].append(node_map[((i1 - 1) % N1, i2, 1)])

            # B-sublattice (sub=1) connects to:
            #   A in same cell, A in cell (i1, i2+1), A in cell (i1+1, i2)
            neighbors[B_idx].append(A_idx)
            neighbors[B_idx].append(node_map[(i1, (i2 + 1) % N2, 0)])
            neighbors[B_idx].append(node_map[((i1 + 1) % N1, i2, 0)])

    return np.array(positions), np.array(angles), neighbors


# ── Escape fraction computation ──────────────────────────

def compute_escape_fractions(positions, angles, neighbors):
    """
    For each node, for each choice of incoming edge, compute
    the escape fraction f_esc = (ê_in · n̂_out_plane)².

    Also computes how much of the escape aligns with the
    torus surface normal.

    Returns dict with arrays indexed by node.
    """
    M = len(positions)
    # Per-node quantities (averaged over 3 incoming edge choices)
    f_esc_avg = np.zeros(M)
    f_esc_normal = np.zeros(M)      # escape projected onto surface normal
    f_esc_all = np.zeros((M, 3))    # per incoming edge

    for i in range(M):
        pos_i = positions[i]
        nbrs = neighbors[i]
        assert len(nbrs) == 3, f"Node {i} has {len(nbrs)} neighbors"

        # Unit edge directions pointing FROM node i TO each neighbor
        e_hat = np.zeros((3, 3))
        for k in range(3):
            diff = positions[nbrs[k]] - pos_i
            e_hat[k] = diff / np.linalg.norm(diff)

        th1, th2 = angles[i]
        n_surf = torus_surface_normal(th1, th2)

        for inc in range(3):
            # Incoming direction (points INTO the node)
            e_in = -e_hat[inc]

            # Two outgoing directions
            out_indices = [k for k in range(3) if k != inc]
            e_out1 = e_hat[out_indices[0]]
            e_out2 = e_hat[out_indices[1]]

            # Normal to the outgoing plane
            cross = np.cross(e_out1, e_out2)
            cross_norm = np.linalg.norm(cross)
            if cross_norm < 1e-12:
                # Degenerate: outgoing edges are parallel
                f_esc_all[i, inc] = 0.0
                continue
            n_out = cross / cross_norm

            # Escape fraction
            dot = np.dot(e_in, n_out)
            f_esc_all[i, inc] = dot**2

            # How much of the escape aligns with the surface normal
            e_escape = dot * n_out
            f_esc_normal[i] += np.dot(e_escape, n_surf)**2

        f_esc_avg[i] = np.mean(f_esc_all[i])
        f_esc_normal[i] /= 3.0

    return {
        "f_esc_avg": f_esc_avg,
        "f_esc_normal": f_esc_normal,
        "f_esc_all": f_esc_all,
    }


# ── Main sweeps ──────────────────────────────────────────

def run_sweep(method_name, method_key):
    """Run the escape fraction computation across N and ε."""
    print(f"\n{'='*60}")
    print(f"  Method {method_name}")
    print(f"{'='*60}")

    eps_values = [0.1, 0.3, 0.5, 0.7, 1.0]
    N_values = [4, 6, 8, 10, 20, 40]

    results_table = []

    for eps in eps_values:
        R = 1.0
        a = eps * R  # ε = a/R

        for N in N_values:
            positions, angs, neighbors = build_honeycomb_torus(
                N, N, R, a, method=method_key
            )
            M = len(positions)

            esc = compute_escape_fractions(positions, angs, neighbors)
            f_avg = esc["f_esc_avg"]
            f_norm = esc["f_esc_normal"]

            mean_f = np.mean(f_avg)
            std_f = np.std(f_avg)
            min_f = np.min(f_avg)
            max_f = np.max(f_avg)
            mean_fn = np.mean(f_norm)

            ratio = mean_f / ALPHA if mean_f > 0 else 0

            results_table.append({
                "eps": eps, "N": N, "M": M,
                "mean_f": mean_f, "std_f": std_f,
                "min_f": min_f, "max_f": max_f,
                "mean_fn": mean_fn,
                "ratio": ratio,
            })

            print(f"  ε={eps:.1f}  N={N:3d}  nodes={M:5d}  "
                  f"f_esc={mean_f:.6e} ± {std_f:.6e}  "
                  f"f_esc/α={ratio:.4f}  "
                  f"range=[{min_f:.6e}, {max_f:.6e}]")

    return results_table


def plot_results(results_A, results_B):
    """Plot escape fraction vs N for various ε, both methods."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    for ax, results, title in [
        (axes[0], results_A, "Method A: Conformal mapping"),
        (axes[1], results_B, "Method B: Equal edge lengths"),
    ]:
        eps_values = sorted(set(r["eps"] for r in results))
        for eps in eps_values:
            subset = [r for r in results if r["eps"] == eps]
            Ns = [r["N"] for r in subset]
            fs = [r["mean_f"] for r in subset]
            ax.plot(Ns, fs, "o-", label=f"ε = {eps:.1f}")

        ax.axhline(ALPHA, color="red", ls="--", alpha=0.7,
                    label=f"α = {ALPHA:.6f}")
        ax.set_xlabel("N (cells per direction)")
        ax.set_ylabel("Mean escape fraction f_esc")
        ax.set_title(title)
        ax.set_yscale("log")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT / "track9_escape_vs_N.png", dpi=150)
    print(f"\n  Saved: {OUT / 'track9_escape_vs_N.png'}")


def plot_spatial_variation(method_key, method_name, eps, N):
    """Plot f_esc as a function of θ₁ position for one (ε, N) case."""
    R = 1.0
    a = eps * R
    positions, angs, neighbors = build_honeycomb_torus(
        N, N, R, a, method=method_key
    )
    esc = compute_escape_fractions(positions, angs, neighbors)
    f_avg = esc["f_esc_avg"]

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    sc = ax.scatter(angs[:, 1], angs[:, 0], c=f_avg, cmap="viridis",
                    s=10, edgecolors="none")
    plt.colorbar(sc, ax=ax, label="f_esc")
    ax.set_xlabel("θ₂ (ring angle)")
    ax.set_ylabel("θ₁ (tube angle)")
    ax.set_title(f"{method_name}: f_esc spatial map  (ε={eps}, N={N})")
    plt.tight_layout()
    fname = f"track9_spatial_{method_key}_eps{eps}_N{N}.png"
    plt.savefig(OUT / fname, dpi=150)
    print(f"  Saved: {OUT / fname}")


def analyze_scaling(results):
    """Check if f_esc scales as ε² / N²."""
    print("\n  Scaling analysis: f_esc vs ε² / N²")
    print(f"  {'ε':>5s}  {'N':>4s}  {'f_esc':>12s}  {'ε²/N²':>12s}  {'ratio':>10s}")
    for r in results:
        eps2_over_N2 = r["eps"]**2 / r["N"]**2
        if eps2_over_N2 > 0:
            rat = r["mean_f"] / eps2_over_N2
        else:
            rat = 0
        print(f"  {r['eps']:5.1f}  {r['N']:4d}  {r['mean_f']:12.6e}  "
              f"{eps2_over_N2:12.6e}  {rat:10.4f}")


def edge_direction_analysis(method_key, method_name, eps, N):
    """Check if f_esc depends on which edge is 'incoming'."""
    R = 1.0
    a = eps * R
    positions, angs, neighbors = build_honeycomb_torus(
        N, N, R, a, method=method_key
    )
    esc = compute_escape_fractions(positions, angs, neighbors)
    f_all = esc["f_esc_all"]  # (M, 3)

    print(f"\n  Edge-direction analysis ({method_name}, ε={eps}, N={N}):")
    print(f"    Edge 0: mean={np.mean(f_all[:,0]):.6e}  std={np.std(f_all[:,0]):.6e}")
    print(f"    Edge 1: mean={np.mean(f_all[:,1]):.6e}  std={np.std(f_all[:,1]):.6e}")
    print(f"    Edge 2: mean={np.mean(f_all[:,2]):.6e}  std={np.std(f_all[:,2]):.6e}")

    var_across_edges = np.std(f_all, axis=1)
    print(f"    Mean std across edges per node: {np.mean(var_across_edges):.6e}")
    print(f"    Max  std across edges per node: {np.max(var_across_edges):.6e}")


# ── Entry point ──────────────────────────────────────────

if __name__ == "__main__":
    print("Track 9: Junction escape fraction")
    print(f"α = {ALPHA:.6e}")

    results_A = run_sweep("A: Conformal mapping", "conformal")
    results_B = run_sweep("B: Equal edge lengths", "equal_edge")

    analyze_scaling(results_A)
    analyze_scaling(results_B)

    plot_results(results_A, results_B)

    for eps in [0.3, 0.7]:
        plot_spatial_variation("conformal", "Conformal", eps, 10)
        plot_spatial_variation("equal_edge", "Equal edge", eps, 10)

    for eps in [0.3, 0.7]:
        edge_direction_analysis("conformal", "Conformal", eps, 10)
        edge_direction_analysis("equal_edge", "Equal edge", eps, 10)

    print("\nDone.")
