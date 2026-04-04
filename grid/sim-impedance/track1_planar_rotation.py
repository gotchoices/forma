#!/usr/bin/env python3
"""
Track 1: Coincidence rate between two rotated triangular lattices.

Two 2D triangular lattices, both edge-length L=1, occupy the same
plane.  Lattice B is rotated by angle θ relative to lattice A.

For each angle θ we count cross-lattice node pairs separated by
distance 1 ± ε and report the coincidence rate per node, normalised
to the intact-lattice coordination number (6 for triangular).

We also look at the spatial distribution of coincidences to detect
superlattice periodicity.
"""

import numpy as np
from scipy.spatial import cKDTree
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)


# ── Lattice generation ──────────────────────────────────────────

def triangular_lattice(n_rows, n_cols):
    """Generate a triangular lattice centred near the origin.

    Returns an (N, 2) array of node positions with edge length 1.
    """
    pts = []
    for row in range(n_rows):
        for col in range(n_cols):
            x = col + 0.5 * (row % 2)
            y = row * np.sqrt(3) / 2
            pts.append((x, y))
    pts = np.array(pts)
    pts -= pts.mean(axis=0)          # centre on origin
    return pts


def rotate(pts, theta_deg):
    """Rotate (N,2) point array by theta_deg about the origin."""
    t = np.radians(theta_deg)
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])
    return pts @ R.T


# ── Coincidence counting ────────────────────────────────────────

def count_coincidences(pts_a, pts_b, L=1.0, eps=0.02):
    """Count pairs (one from A, one from B) with |r_a - r_b| in [L-eps, L+eps].

    Returns:
        n_hits   – total number of coincidence pairs
        per_node – hits per node of lattice A
        ratio    – per_node / 6  (fraction of intact coordination)
    """
    tree_b = cKDTree(pts_b)
    # Query each point in A for neighbours in B within L + eps
    outer = tree_b.query_ball_point(pts_a, L + eps)
    n_hits = 0
    for i, neighbours in enumerate(outer):
        if not neighbours:
            continue
        dists = np.linalg.norm(pts_b[neighbours] - pts_a[i], axis=1)
        n_hits += np.count_nonzero(dists >= L - eps)
    per_node = n_hits / len(pts_a)
    ratio = per_node / 6.0
    return n_hits, per_node, ratio


def coincidence_positions(pts_a, pts_b, L=1.0, eps=0.02):
    """Return midpoints of all coincidence pairs (for spatial analysis)."""
    tree_b = cKDTree(pts_b)
    outer = tree_b.query_ball_point(pts_a, L + eps)
    midpoints = []
    for i, neighbours in enumerate(outer):
        if not neighbours:
            continue
        dists = np.linalg.norm(pts_b[neighbours] - pts_a[i], axis=1)
        mask = dists >= L - eps
        for j_idx in np.where(mask)[0]:
            j = neighbours[j_idx]
            midpoints.append(0.5 * (pts_a[i] + pts_b[j]))
    return np.array(midpoints) if midpoints else np.empty((0, 2))


# ── Analysis 1: Sweep angle ────────────────────────────────────

def sweep_angle(n_rows=80, n_cols=80, eps=0.02):
    """Sweep rotation angle from 0.5° to 30° and measure coincidence rate."""
    pts_a = triangular_lattice(n_rows, n_cols)
    # Trim to a central disk to avoid edge effects
    R_cut = min(n_rows, n_cols) * 0.35
    mask_a = np.linalg.norm(pts_a, axis=1) < R_cut
    pts_a_cut = pts_a[mask_a]

    angles = np.concatenate([
        np.arange(0.5, 5.0, 0.25),
        np.arange(5.0, 30.01, 0.5),
    ])
    results = []

    print(f"Lattice: {n_rows}×{n_cols} = {len(pts_a)} nodes, "
          f"trimmed to {len(pts_a_cut)} in disk R<{R_cut:.1f}")
    print(f"Tolerance ε = {eps}")
    print(f"Sweeping {len(angles)} angles from {angles[0]:.2f}° to {angles[-1]:.2f}°")
    print()
    print(f"  {'θ (°)':>8s}  {'hits':>7s}  {'per node':>9s}  {'rate/6':>9s}")
    print("  " + "─" * 38)

    for theta in angles:
        pts_b = rotate(pts_a, theta)
        pts_b_cut = pts_b[mask_a]
        n_hits, per_node, ratio = count_coincidences(
            pts_a_cut, pts_b_cut, L=1.0, eps=eps)
        results.append((theta, n_hits, per_node, ratio))
        print(f"  {theta:8.2f}  {n_hits:7d}  {per_node:9.4f}  {ratio:9.6f}")

    return results


# ── Analysis 2: Fine sweep around peaks ─────────────────────────

def fine_sweep(peak_angles, n_rows=80, n_cols=80, eps=0.02, halfwidth=2.0):
    """Fine-grain sweep around candidate peak angles."""
    pts_a = triangular_lattice(n_rows, n_cols)
    R_cut = min(n_rows, n_cols) * 0.35
    mask_a = np.linalg.norm(pts_a, axis=1) < R_cut
    pts_a_cut = pts_a[mask_a]

    all_results = []
    for centre in peak_angles:
        angles = np.arange(centre - halfwidth, centre + halfwidth + 0.01, 0.05)
        angles = angles[(angles > 0) & (angles <= 30)]
        results = []
        for theta in angles:
            pts_b = rotate(pts_a, theta)
            pts_b_cut = pts_b[mask_a]
            n_hits, per_node, ratio = count_coincidences(
                pts_a_cut, pts_b_cut, L=1.0, eps=eps)
            results.append((theta, n_hits, per_node, ratio))
        all_results.append((centre, results))
    return all_results


# ── Analysis 3: Spatial pattern at a given angle ────────────────

def spatial_analysis(theta, n_rows=80, n_cols=80, eps=0.02):
    """Visualise the spatial distribution of coincidences at one angle."""
    pts_a = triangular_lattice(n_rows, n_cols)
    R_cut = min(n_rows, n_cols) * 0.35
    mask_a = np.linalg.norm(pts_a, axis=1) < R_cut
    pts_a_cut = pts_a[mask_a]

    pts_b = rotate(pts_a, theta)
    pts_b_cut = pts_b[mask_a]

    mids = coincidence_positions(pts_a_cut, pts_b_cut, L=1.0, eps=eps)
    return mids


# ── Analysis 4: Tolerance scaling ───────────────────────────────

def tolerance_scaling(theta, n_rows=80, n_cols=80):
    """Check how coincidence rate scales with tolerance ε.

    If rate ∝ ε, the geometric content is in the proportionality
    constant (the rate density).  If rate has a plateau or step,
    there may be exact coincidences.
    """
    pts_a = triangular_lattice(n_rows, n_cols)
    R_cut = min(n_rows, n_cols) * 0.35
    mask_a = np.linalg.norm(pts_a, axis=1) < R_cut
    pts_a_cut = pts_a[mask_a]
    pts_b = rotate(pts_a, theta)
    pts_b_cut = pts_b[mask_a]

    epsilons = np.array([0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2])
    results = []
    for eps in epsilons:
        n_hits, per_node, ratio = count_coincidences(
            pts_a_cut, pts_b_cut, L=1.0, eps=eps)
        # Rate density = per_node / (2*eps) — coincidences per node per unit tolerance
        density = per_node / (2 * eps) if eps > 0 else 0
        results.append((eps, n_hits, per_node, ratio, density))
    return results


# ── Plotting ────────────────────────────────────────────────────

def plot_sweep(results):
    angles = [r[0] for r in results]
    rates = [r[3] for r in results]      # ratio = per_node / 6

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(angles, rates, 'b.-', markersize=4, linewidth=0.8)
    ax.axhline(1/137.036, color='red', linestyle='--', linewidth=0.8,
               label=f'α = 1/137 = {1/137.036:.6f}')
    ax.set_xlabel('Rotation angle θ (degrees)')
    ax.set_ylabel('Coincidence rate / 6  (fraction of intact coordination)')
    ax.set_title('Track 1: Cross-lattice coincidence rate vs rotation angle')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "sweep_angle.png", dpi=150)
    plt.close(fig)
    print(f"\n  Saved: {OUT / 'sweep_angle.png'}")


def plot_spatial(mids, theta):
    if len(mids) == 0:
        print(f"  No coincidences at θ = {theta}° — skipping spatial plot")
        return
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(mids[:, 0], mids[:, 1], s=1, alpha=0.5, color='blue')
    ax.set_aspect('equal')
    ax.set_title(f'Coincidence midpoints at θ = {theta:.2f}°  '
                 f'({len(mids)} pairs)')
    ax.set_xlabel('x / L')
    ax.set_ylabel('y / L')
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    fname = OUT / f"spatial_{theta:.1f}deg.png"
    fig.savefig(fname, dpi=150)
    plt.close(fig)
    print(f"  Saved: {fname}")


def plot_tolerance(tol_results, theta):
    epsilons = [r[0] for r in tol_results]
    per_node = [r[2] for r in tol_results]
    densities = [r[4] for r in tol_results]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(epsilons, per_node, 'bo-', markersize=5)
    ax1.set_xlabel('Tolerance ε / L')
    ax1.set_ylabel('Coincidences per node')
    ax1.set_title(f'Rate vs tolerance (θ = {theta:.1f}°)')
    ax1.grid(True, alpha=0.3)

    ax2.plot(epsilons, densities, 'ro-', markersize=5)
    ax2.set_xlabel('Tolerance ε / L')
    ax2.set_ylabel('Rate density (per node per unit ε)')
    ax2.set_title(f'Rate density vs tolerance (θ = {theta:.1f}°)')
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT / f"tolerance_{theta:.1f}deg.png", dpi=150)
    plt.close(fig)
    print(f"  Saved: {OUT / f'tolerance_{theta:.1f}deg.png'}")


# ── Main ────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  TRACK 1: Two rotated triangular lattices")
    print("=" * 60)
    print()

    # ── Part 1: Coarse angle sweep ──
    print("── Part 1: Coarse angle sweep ──")
    print()
    results = sweep_angle(n_rows=80, n_cols=80, eps=0.02)
    plot_sweep(results)

    # ── Part 2: Tolerance scaling at a few angles ──
    print()
    print("── Part 2: Tolerance scaling ──")
    print()
    test_angles = [7.5, 13.2, 21.8]
    for theta in test_angles:
        print(f"  θ = {theta}°:")
        tol_results = tolerance_scaling(theta)
        print(f"    {'ε':>8s}  {'hits':>7s}  {'per node':>9s}  {'rate/6':>9s}  {'density':>9s}")
        for eps, n_hits, pn, ratio, dens in tol_results:
            print(f"    {eps:8.3f}  {n_hits:7d}  {pn:9.4f}  {ratio:9.6f}  {dens:9.2f}")
        plot_tolerance(tol_results, theta)
        print()

    # ── Part 3: Spatial pattern at selected angles ──
    print("── Part 3: Spatial pattern of coincidences ──")
    print()

    # Pick angles where coincidence rate is interesting
    # (peaks from sweep, plus a generic angle)
    rates = [(r[0], r[3]) for r in results]
    rates.sort(key=lambda x: -x[1])
    top_angles = [rates[0][0], rates[1][0], rates[2][0]]
    # Also add a generic irrational-ish angle
    top_angles.append(13.17)
    top_angles = sorted(set(top_angles))

    for theta in top_angles:
        mids = spatial_analysis(theta)
        print(f"  θ = {theta:.2f}°: {len(mids)} coincidence pairs")
        plot_spatial(mids, theta)

    # ── Part 4: Fine sweep around most promising angles ──
    print()
    print("── Part 4: Fine sweep around peaks ──")
    print()
    peak_angles = [r[0] for r in sorted(rates, key=lambda x: -x[1])[:3]]
    fine_results = fine_sweep(peak_angles, n_rows=80, n_cols=80, eps=0.02)
    for centre, fres in fine_results:
        print(f"  Peak near θ = {centre:.2f}°:")
        print(f"    {'θ':>8s}  {'per node':>9s}  {'rate/6':>9s}")
        best = max(fres, key=lambda r: r[3])
        for theta, n_hits, pn, ratio in fres:
            marker = " ◄" if theta == best[0] else ""
            print(f"    {theta:8.2f}  {pn:9.4f}  {ratio:9.6f}{marker}")
        print(f"    Peak: θ = {best[0]:.2f}°, rate/6 = {best[3]:.6f}")
        print()

    # ── Summary ──
    print("=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    print()
    print(f"  Reference: α = 1/137.036 = {1/137.036:.6f}")
    print(f"  Intact lattice coordination: 6 neighbors")
    print()
    rates_sorted = sorted(rates, key=lambda x: x[0])
    print(f"  {'θ (°)':>8s}  {'rate/6':>9s}  {'1/rate':>9s}  {'note':>20s}")
    print("  " + "─" * 50)
    for theta, ratio in rates_sorted:
        inv = 1.0 / ratio if ratio > 0 else float('inf')
        note = ""
        if abs(inv - 137.036) / 137.036 < 0.1:
            note = "★ near 1/α"
        elif abs(inv - 137.036) / 137.036 < 0.3:
            note = "~ order of α"
        print(f"  {theta:8.2f}  {ratio:9.6f}  {inv:9.1f}  {note:>20s}")

    # Save raw data
    with open(OUT / "sweep_data.txt", "w") as f:
        f.write("# theta_deg  n_hits  per_node  ratio_over_6\n")
        for theta, n_hits, pn, ratio in results:
            f.write(f"{theta:.2f}  {n_hits}  {pn:.6f}  {ratio:.8f}\n")
    print(f"\n  Raw data: {OUT / 'sweep_data.txt'}")


if __name__ == "__main__":
    main()
