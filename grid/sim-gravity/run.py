#!/usr/bin/env python3
"""sim-gravity: end-to-end pipeline.

Generate lattice → embed rigid body → dilate → relax → measure → plot.

Tests whether the deformation field from an embedded rigid body
reproduces 2D gravity:
  - Edge strain ε(r) ∝ 1/r   [gravitational force — primary test]
  - Displacement u(r) ∝ log(r) [gravitational potential — secondary]

Usage (from repo root):
    source .venv/bin/activate
    python grid/sim-gravity/run.py
"""

import os
import sys
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))

from lattice import make_lattice, boundary_vertices
from embed import embed_hexagon, embed_triangle, apply_dilation
from relax import relax
from measure import (displacement_field, edge_strain_field,
                     bin_radial, fit_log, fit_power_law)


def run_trial(nx, ny, shape, scale, label):
    """Run one trial: free BCs with clamped boundary for convergence."""
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"  Lattice: {nx}×{ny} = {nx*ny} vertices")
    print(f"  Rigid body: {shape}, dilation = {scale}")
    print(f"{'='*60}")

    pos_eq, edges, rest = make_lattice(nx, ny, periodic=False)
    print(f"  Edges: {len(edges)}")

    if shape == "hexagon":
        defect = embed_hexagon(pos_eq, edges)
    else:
        defect = embed_triangle(pos_eq, edges)

    bnd = boundary_vertices(nx, ny)
    frozen = defect | bnd
    print(f"  Frozen: {len(defect)} defect + {len(bnd)} boundary")

    pos_init = apply_dilation(pos_eq, defect, scale=scale)

    t0 = time.time()
    pos_relaxed, energy = relax(pos_init, edges, rest, frozen)
    dt = time.time() - t0
    print(f"  Relaxation: {dt:.2f}s, energy = {energy:.4e}")

    centre = pos_eq[sorted(defect)].mean(axis=0)
    half_box = min(nx, ny * np.sqrt(3) / 2) / 2
    fit_rmin = 3.0
    fit_rmax = half_box * 0.45

    # --- Primary: edge strain (local, no boundary artifact) ---
    r_eps, eps = edge_strain_field(
        pos_eq, pos_relaxed, edges, rest, centre,
        exclude_verts=defect | bnd)
    r_eps_mid, eps_mean, eps_std, eps_cnt = bin_radial(r_eps, eps, n_bins=60)
    p_eps, A_eps, eps_fit, r2_eps = fit_power_law(
        r_eps_mid, eps_mean, r_min=fit_rmin, r_max=fit_rmax)
    print(f"  Edge strain: ε ∝ r^(−{p_eps:.3f})   R² = {r2_eps:.4f}")
    print(f"    fit range [{fit_rmin:.0f}, {fit_rmax:.0f}]")

    # --- Secondary: displacement ---
    r_u, u = displacement_field(
        pos_eq, pos_relaxed, defect | bnd, centre)
    r_u_mid, u_mean, u_std, _ = bin_radial(r_u, u, n_bins=60)
    A_log, B_log, u_fit, r2_log = fit_log(
        r_u_mid, u_mean, r_min=fit_rmin, r_max=fit_rmax)
    print(f"  Displacement: u = {A_log:.3e}·log(r)+{B_log:.3e}"
          f"   R² = {r2_log:.4f}")

    print(f"  *** Expect: ε ∝ 1/r (p≈1), u ∝ log(r) ***")

    return {
        "label": label,
        "r_eps_mid": r_eps_mid, "eps_mean": eps_mean,
        "eps_std": eps_std, "eps_fit": eps_fit,
        "p_eps": p_eps, "A_eps": A_eps, "r2_eps": r2_eps,
        "r_u_mid": r_u_mid, "u_mean": u_mean, "u_std": u_std,
        "u_fit": u_fit, "A_log": A_log, "B_log": B_log,
        "r2_log": r2_log,
        "fit_rmin": fit_rmin, "fit_rmax": fit_rmax,
        "pos_eq": pos_eq, "pos_relaxed": pos_relaxed,
        "defect": defect, "edges": edges,
    }


def plot_strain(ax, d):
    """Log-log: edge strain vs distance with power-law fit."""
    ax.errorbar(d["r_eps_mid"], d["eps_mean"], yerr=d["eps_std"],
                fmt="o", ms=2, alpha=0.6, label="ε(r) data")
    valid = np.isfinite(d["eps_fit"]) & (d["eps_fit"] > 0)
    if valid.any():
        ax.plot(d["r_eps_mid"][valid], d["eps_fit"][valid], "r-", lw=2,
                label=f"ε ∝ r$^{{-{d['p_eps']:.2f}}}$,"
                      f" R²={d['r2_eps']:.3f}")
    ax.axvline(d["fit_rmin"], color="gray", ls=":", alpha=0.4)
    ax.axvline(d["fit_rmax"], color="gray", ls=":", alpha=0.4)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("r (lattice units)")
    ax.set_ylabel("edge strain ε = |Δl|/l₀")
    ax.set_title(d["label"] + " — strain (force analog)")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)


def plot_potential(ax, d):
    """Linear-log: displacement vs distance with log fit."""
    ax.errorbar(d["r_u_mid"], d["u_mean"], yerr=d["u_std"],
                fmt="o", ms=2, alpha=0.6, label="u(r) data")
    valid = np.isfinite(d["u_fit"])
    if valid.any():
        ax.plot(d["r_u_mid"][valid], d["u_fit"][valid], "r-", lw=2,
                label=f"A·log(r)+B, R²={d['r2_log']:.3f}")
    ax.axvline(d["fit_rmin"], color="gray", ls=":", alpha=0.4)
    ax.axvline(d["fit_rmax"], color="gray", ls=":", alpha=0.4)
    ax.set_xlabel("r (lattice units)")
    ax.set_ylabel("displacement u(r)")
    ax.set_title(d["label"] + " — displacement (potential analog)")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)


def plot_lattice(ax, d):
    """Deformed lattice near defect, coloured by strain."""
    pos = d["pos_relaxed"]
    defect = d["defect"]
    edges = d["edges"]
    flist = sorted(defect)
    ctr = d["pos_eq"][flist].mean(axis=0)
    radius = 18.0
    near = np.sqrt(np.sum((pos - ctr) ** 2, axis=1)) < radius

    for a, b in edges:
        if near[a] or near[b]:
            l = np.sqrt(np.sum((pos[a] - pos[b]) ** 2))
            strain = abs(l - 1.0)
            c = plt.cm.hot(min(strain * 20, 1.0))
            ax.plot([pos[a, 0], pos[b, 0]], [pos[a, 1], pos[b, 1]],
                    "-", color=c, lw=0.5, alpha=0.7)

    ax.plot(pos[flist, 0], pos[flist, 1], "gs", ms=5, label="defect")
    ax.set_aspect("equal")
    ax.set_xlim(ctr[0] - radius, ctr[0] + radius)
    ax.set_ylim(ctr[1] - radius, ctr[1] + radius)
    ax.set_title("Lattice near defect (colour = strain)")
    ax.legend(fontsize=8)


def main():
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(out_dir, exist_ok=True)

    trials = [
        (100, 100, "hexagon",  1.3, "100² hex s=1.3"),
        (150, 150, "hexagon",  1.3, "150² hex s=1.3"),
        (200, 200, "hexagon",  1.3, "200² hex s=1.3"),
        (200, 200, "hexagon",  1.5, "200² hex s=1.5"),
        (200, 200, "triangle", 1.3, "200² tri s=1.3"),
    ]

    results = []
    for nx, ny, shape, scale, label in trials:
        results.append(run_trial(nx, ny, shape, scale, label))

    # --- Summary ---
    print(f"\n{'='*72}")
    print("  SUMMARY")
    print(f"{'='*72}")
    hdr = (f"  {'Trial':<22s}  {'p_strain':>8s}  {'R²_ε':>6s}"
           f"  {'A_log':>9s}  {'R²_log':>6s}")
    print(hdr)
    print(f"  {'-'*22}  {'-'*8}  {'-'*6}  {'-'*9}  {'-'*6}")
    for d in results:
        print(f"  {d['label']:<22s}  {d['p_eps']:8.3f}  {d['r2_eps']:6.3f}"
              f"  {d['A_log']:9.3e}  {d['r2_log']:6.3f}")
    print()
    print("  2D gravity prediction:")
    print("    Edge strain ε(r) ∝ 1/r   → p_strain ≈ 1.0, high R²")
    print("    Displacement u(r) ∝ log(r) → high R²_log")

    # --- Plots ---
    n = len(results)
    fig, axes = plt.subplots(n, 2, figsize=(13, 4.2 * n))
    if n == 1:
        axes = axes[np.newaxis, :]
    for i, d in enumerate(results):
        plot_strain(axes[i, 0], d)
        plot_potential(axes[i, 1], d)

    fig.suptitle(
        "sim-gravity: edge strain (force) & displacement (potential)",
        fontsize=14, y=1.0)
    fig.tight_layout()
    path1 = os.path.join(out_dir, "gravity_fits.png")
    fig.savefig(path1, dpi=150, bbox_inches="tight")
    print(f"\n  Saved: {path1}")

    fig2, ax2 = plt.subplots(1, 1, figsize=(9, 9))
    plot_lattice(ax2, results[2])
    path2 = os.path.join(out_dir, "lattice_detail.png")
    fig2.savefig(path2, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path2}")

    plt.close("all")


if __name__ == "__main__":
    main()
