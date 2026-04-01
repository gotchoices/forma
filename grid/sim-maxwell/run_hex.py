#!/usr/bin/env python3
"""sim-maxwell on a HEXAGONAL (honeycomb) lattice.

Same junction scattering rule, but N=3 edges per vertex
instead of N=6 (triangular).

Scattering for N=3:
    outgoing_i = (2/3) * total - incoming_i
    Reflection: -1/3  (vs -2/3 for triangular)
    Transmission: 2/3  (vs 1/3 for triangular)

Expect: cleaner directional propagation (11% energy reflected
vs 44%).

Usage:
    source .venv/bin/activate
    python grid/sim-maxwell/run_hex.py
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ── Hexagonal (honeycomb) lattice on a torus ──────────────────

def make_honeycomb(nx, ny):
    """Honeycomb lattice on a torus (periodic BCs).

    The honeycomb has 2 vertices per unit cell (A and B sublattices).
    Each vertex has exactly 3 edges (N=3).

    nx, ny: number of unit cells in each direction.
    Total vertices: 2 * nx * ny.
    Total edges: 3 * nx * ny (each vertex has 3 edges, shared).
    """
    V = 2 * nx * ny
    pos = np.zeros((V, 2))

    # Unit cell vectors for honeycomb
    a1 = np.array([1.0, 0.0])              # horizontal
    a2 = np.array([0.5, np.sqrt(3) / 2])   # 60° up-right

    # Two atoms per unit cell
    # A at origin, B at (1/3)(a1 + a2) offset
    d_AB = (a1 + a2) / 3.0  # offset from A to B within cell

    for j in range(ny):
        for i in range(nx):
            cell = j * nx + i
            origin = i * a1 + j * a2
            pos[2 * cell] = origin            # A sublattice
            pos[2 * cell + 1] = origin + d_AB  # B sublattice

    # Box vectors for periodic wrapping
    box_a = nx * a1
    box_b = ny * a2
    box_matrix = np.column_stack([box_a, box_b])  # columns are box vectors
    box_inv = np.linalg.inv(box_matrix)

    def wrap(delta):
        """Wrap displacement to shortest image using box matrix."""
        frac = box_inv @ delta
        frac -= np.round(frac)
        return box_matrix @ frac

    # Build edges: each A vertex connects to 3 B vertices
    edge_set = set()
    edge_list = []

    for j in range(ny):
        for i in range(nx):
            cell = j * nx + i
            A = 2 * cell

            # B in same cell
            B_same = A + 1

            # B in cell to the left: (i-1, j)
            i_left = (i - 1) % nx
            B_left = 2 * (j * nx + i_left) + 1

            # B in cell below: (i, j-1)
            j_below = (j - 1) % ny
            B_below = 2 * (j_below * nx + i) + 1

            for B in [B_same, B_left, B_below]:
                e = (min(A, B), max(A, B))
                if e not in edge_set:
                    edge_set.add(e)
                    edge_list.append(e)

    edges = np.array(edge_list)
    E = len(edges)

    # Edge displacement vectors (shortest image)
    edge_dirs = np.zeros((E, 2))
    for ei, (u, v) in enumerate(edges):
        d = pos[v] - pos[u]
        edge_dirs[ei] = wrap(d)

    # Edge midpoints
    mid = pos[edges[:, 0]] + edge_dirs / 2

    # Effective box for plotting (rectangular bounding box)
    all_corners = np.array([
        [0, 0],
        box_a,
        box_b,
        box_a + box_b
    ])
    box_rect = np.array([all_corners[:, 0].max(),
                         all_corners[:, 1].max()])

    # Vertex-edge connectivity (all vertices have exactly 3 edges)
    max_N = 3
    vert_ei = np.zeros((V, max_N), dtype=int)
    vert_end = np.zeros((V, max_N), dtype=int)
    vert_count = np.zeros(V, dtype=int)

    for ei in range(E):
        u, v = edges[ei]
        k = vert_count[u]
        vert_ei[u, k] = ei
        vert_end[u, k] = 0
        vert_count[u] += 1

        k = vert_count[v]
        vert_ei[v, k] = ei
        vert_end[v, k] = 1
        vert_count[v] += 1

    if not np.all(vert_count == 3):
        bad = np.where(vert_count != 3)[0]
        print(f"  WARNING: {len(bad)} vertices with count != 3 "
              f"(range {vert_count.min()}-{vert_count.max()})")

    return (pos, edges, vert_ei, vert_end, edge_dirs, mid,
            box_rect, wrap)


# ── Scattering step (N=3) ────────────────────────────────────

def scatter_step(a_fwd, a_bwd, vert_ei, vert_end, N=3):
    incoming = np.where(vert_end == 0,
                        a_bwd[vert_ei],
                        a_fwd[vert_ei])

    total = incoming.sum(axis=1, keepdims=True)
    outgoing = (2.0 / N) * total - incoming

    new_fwd = np.zeros_like(a_fwd)
    new_bwd = np.zeros_like(a_bwd)

    mask0 = vert_end == 0
    mask1 = vert_end == 1
    np.add.at(new_fwd, vert_ei[mask0], outgoing[mask0])
    np.add.at(new_bwd, vert_ei[mask1], outgoing[mask1])

    return new_fwd, new_bwd


def evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
           source_fn=None, snapshot_interval=1, N=3):
    snaps = [(0, a_fwd.copy(), a_bwd.copy())]
    for t in range(1, n_steps + 1):
        a_fwd, a_bwd = scatter_step(a_fwd, a_bwd,
                                     vert_ei, vert_end, N)
        if source_fn is not None:
            a_fwd, a_bwd = source_fn(a_fwd, a_bwd, t)
        if t % snapshot_interval == 0:
            snaps.append((t, a_fwd.copy(), a_bwd.copy()))
    return snaps


# ── Initial conditions ───────────────────────────────────────

def init_wavefront(edge_dirs, mid, box, n_edges, wrap_fn,
                   direction=(1.0, 0.0), center=None, width=3.0):
    d = np.array(direction, float)
    d /= np.linalg.norm(d)

    if center is None:
        center = box / 2
    center = np.array(center, float)

    dist = np.zeros(n_edges)
    for ei in range(n_edges):
        dx = wrap_fn(mid[ei] - center)
        dist[ei] = dx @ d

    envelope = np.exp(-dist ** 2 / (2 * width ** 2))
    proj = edge_dirs @ d

    a_fwd = np.zeros(n_edges)
    a_bwd = np.zeros(n_edges)
    a_fwd[proj > 0] = np.abs(proj[proj > 0]) * envelope[proj > 0]
    a_bwd[proj < 0] = np.abs(proj[proj < 0]) * envelope[proj < 0]

    return a_fwd, a_bwd


def init_single_edge(n_edges, edge_idx=0):
    a_fwd = np.zeros(n_edges)
    a_bwd = np.zeros(n_edges)
    a_fwd[edge_idx] = 1.0
    return a_fwd, a_bwd


def make_point_source(vert_ei, vert_end, source_vert, omega,
                      amplitude=0.05, N=3):
    def source_fn(a_fwd, a_bwd, t):
        amp = amplitude * np.sin(omega * t)
        for k in range(N):
            ei = vert_ei[source_vert, k]
            end = vert_end[source_vert, k]
            if end == 0:
                a_fwd[ei] += amp
            else:
                a_bwd[ei] += amp
        return a_fwd, a_bwd
    return source_fn


# ── Measurement ──────────────────────────────────────────────

def edge_energy(a_fwd, a_bwd):
    return a_fwd ** 2 + a_bwd ** 2


def energy_centroid(energy, mid, box, wrap_fn):
    total = energy.sum()
    if total < 1e-30:
        return box / 2
    ref = mid[np.argmax(energy)]
    dx_all = np.array([wrap_fn(m - ref) for m in mid])
    cx = ref[0] + np.average(dx_all[:, 0], weights=energy)
    cy = ref[1] + np.average(dx_all[:, 1], weights=energy)
    return np.array([cx, cy])


def directionality_ratio(energy, mid, centroid, direction,
                         wrap_fn, half_angle=np.pi / 3):
    d = np.array(direction, float)
    d /= np.linalg.norm(d)

    dx = np.array([wrap_fn(m - centroid) for m in mid])
    r = np.sqrt((dx ** 2).sum(axis=1))
    r = np.maximum(r, 1e-10)
    cos_angle = (dx @ d) / r

    fwd = cos_angle > np.cos(half_angle)
    total = energy.sum()
    if total < 1e-30:
        return 1.0 / 3.0
    return energy[fwd].sum() / total


# ── Tests ────────────────────────────────────────────────────

def test_wavefront(nx, ny, n_steps, width, out_dir):
    print(f"\n{'='*60}")
    print(f"  Hex wavefront ({nx}×{ny}, {n_steps} steps, w={width})")
    print(f"{'='*60}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box, wrap = \
        make_honeycomb(nx, ny)
    E = len(edges)
    V = len(pos)
    direction = np.array([1.0, 0.0])
    print(f"  Vertices: {V}, Edges: {E}")

    a_fwd, a_bwd = init_wavefront(
        edge_dirs, mid, box, E, wrap,
        direction=direction, width=width)

    E0 = edge_energy(a_fwd, a_bwd).sum()
    c0 = energy_centroid(edge_energy(a_fwd, a_bwd), mid, box, wrap)
    print(f"  Initial energy: {E0:.4f}")

    snap_interval = max(1, n_steps // 50)
    snaps = evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
                   snapshot_interval=snap_interval, N=3)

    times, dirs, energies = [], [], []
    cum_dx = []
    prev_c = c0.copy()
    total_dx = 0.0

    for t, af, ab in snaps:
        en = edge_energy(af, ab)
        c = energy_centroid(en, mid, box, wrap)
        dr = directionality_ratio(en, mid, c0, direction, wrap)
        step_dx = wrap(c - prev_c)[0]
        total_dx += step_dx
        prev_c = c.copy()
        times.append(t)
        cum_dx.append(total_dx)
        dirs.append(dr)
        energies.append(en.sum())

    speed = cum_dx[-1] / n_steps if n_steps > 0 else 0

    print(f"  Speed: {speed:.4f} lattice units / tick")
    print(f"  Directionality: {dirs[0]:.3f} → {dirs[-1]:.3f}")
    print(f"  Energy: {energies[0]:.6f} → {energies[-1]:.6f} "
          f"(ratio {energies[-1]/energies[0]:.8f})")

    # Plot
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    axes[0].plot(times, cum_dx, "b-", lw=2)
    axes[0].set_xlabel("t (ticks)")
    axes[0].set_ylabel("cumulative Δx")
    axes[0].set_title("Centroid displacement")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(times, dirs, "g-", lw=2)
    axes[1].axhline(1.0 / 3.0, color="gray", ls="--",
                    label="isotropic (1/3)")
    axes[1].set_xlabel("t (ticks)")
    axes[1].set_ylabel("forward fraction")
    axes[1].set_title("Directionality (±60°)")
    axes[1].legend()
    axes[1].set_ylim(0, 1)
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(times, energies, "r-", lw=2)
    axes[2].set_xlabel("t (ticks)")
    axes[2].set_ylabel("total energy")
    axes[2].set_title("Energy conservation")
    axes[2].grid(True, alpha=0.3)

    fig.suptitle("Hexagonal lattice (N=3): wavefront", fontsize=14)
    fig.tight_layout()
    path = os.path.join(out_dir, "hex_wavefront.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.close(fig)

    return {"speed": speed, "dir_initial": dirs[0],
            "dir_final": dirs[-1],
            "energy_ratio": energies[-1] / energies[0]}


def test_single_edge(nx, ny, n_steps, out_dir):
    print(f"\n{'='*60}")
    print(f"  Hex single edge ({nx}×{ny}, {n_steps} steps)")
    print(f"{'='*60}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box, wrap = \
        make_honeycomb(nx, ny)
    E = len(edges)

    center = box / 2
    dists = np.array([np.linalg.norm(wrap(m - center))
                      for m in mid])
    edge_idx = np.argmin(dists)
    direction = edge_dirs[edge_idx].copy()
    direction /= np.linalg.norm(direction)

    a_fwd, a_bwd = init_single_edge(E, edge_idx)
    c0 = mid[edge_idx].copy()

    snaps = evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
                   snapshot_interval=max(1, n_steps // 50), N=3)

    _, af_f, ab_f = snaps[-1]
    en_f = edge_energy(af_f, ab_f)
    dr = directionality_ratio(en_f, mid, c0, direction, wrap)

    print(f"  Directionality: {dr:.3f} (isotropic = 0.333)")
    print(f"  Energy: {en_f.sum():.8f}")

    fig, ax = plt.subplots(figsize=(6, 5))
    from matplotlib.collections import LineCollection
    r = np.array([np.linalg.norm(wrap(m - c0)) for m in mid])
    view = r < box.min() / 3
    ax.scatter(mid[view, 0], mid[view, 1], c=en_f[view], s=2,
               cmap="hot")
    ax.set_aspect("equal")
    ax.set_title(f"Single edge at t={n_steps}")
    path = os.path.join(out_dir, "hex_single_edge.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.close(fig)

    return {"dir_final": dr}


def test_wavelength(nx, ny, n_steps, out_dir):
    print(f"\n{'='*60}")
    print(f"  Hex wavelength dependence ({nx}×{ny})")
    print(f"{'='*60}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box, wrap = \
        make_honeycomb(nx, ny)
    E = len(edges)
    direction = np.array([1.0, 0.0])

    widths = [1, 2, 3, 5, 8, 12, 20]
    results_w = []

    for w in widths:
        a_fwd, a_bwd = init_wavefront(
            edge_dirs, mid, box, E, wrap,
            direction=direction, width=float(w))
        c0 = energy_centroid(edge_energy(a_fwd, a_bwd),
                             mid, box, wrap)

        snaps = evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
                       snapshot_interval=n_steps, N=3)
        _, af, ab = snaps[-1]
        en = edge_energy(af, ab)
        dr = directionality_ratio(en, mid, c0, direction, wrap)

        c_final = energy_centroid(en, mid, box, wrap)
        dx = wrap(c_final - c0)[0]
        speed = dx / n_steps

        results_w.append({"width": w, "dir": dr, "speed": speed})
        print(f"  width={w:3d}: dir={dr:.3f}, speed={speed:.4f}")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    ws = [r["width"] for r in results_w]
    ds = [r["dir"] for r in results_w]
    ss = [r["speed"] for r in results_w]

    axes[0].plot(ws, ds, "bo-", lw=2, label="Hexagonal (N=3)")
    axes[0].axhline(1.0 / 3.0, color="gray", ls="--",
                    label="isotropic")
    axes[0].set_xlabel("wavefront width")
    axes[0].set_ylabel("directionality ratio")
    axes[0].set_title("Directionality vs width")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(ws, ss, "ro-", lw=2)
    axes[1].set_xlabel("wavefront width")
    axes[1].set_ylabel("speed (units/tick)")
    axes[1].set_title("Speed vs width")
    axes[1].grid(True, alpha=0.3)

    fig.suptitle("Hexagonal lattice (N=3): wavelength dependence",
                 fontsize=14)
    fig.tight_layout()
    path = os.path.join(out_dir, "hex_wavelength.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.close(fig)

    return results_w


# ── Main ─────────────────────────────────────────────────────

def main():
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(out_dir, exist_ok=True)

    print("sim-maxwell: HEXAGONAL lattice (N=3)")
    print("Scattering: outgoing_i = (2/3)*total - incoming_i")
    print("Reflection: -1/3 (vs -2/3 for triangular)")
    print("Transmission: 2/3 each (vs 1/3 for triangular)")

    r1 = test_wavefront(80, 80, n_steps=60, width=5.0,
                        out_dir=out_dir)

    r2 = test_single_edge(50, 50, n_steps=30, out_dir=out_dir)

    r4 = test_wavelength(60, 60, n_steps=40, out_dir=out_dir)

    print(f"\n{'='*72}")
    print("  SUMMARY — HEXAGONAL (N=3) vs TRIANGULAR (N=6)")
    print(f"{'='*72}")
    print()
    print(f"  Wavefront (width=5):")
    print(f"    Hexagonal:  speed={r1['speed']:.4f}, "
          f"dir={r1['dir_final']:.3f}")
    print(f"    Triangular: speed=0.7115, dir=0.031")
    print(f"    (Tri dir is low because wide wavefront on "
          f"large lattice)")
    print()
    print(f"  Single edge:")
    print(f"    Hexagonal:  dir={r2['dir_final']:.3f}")
    print(f"    Triangular: dir=0.235")
    print(f"    Isotropic:  dir=0.333")
    print()
    print(f"  Width dependence:")
    print(f"  {'width':>6s}  {'hex dir':>8s}  {'hex speed':>9s}"
          f"  {'tri dir':>8s}  {'tri speed':>9s}")
    print(f"  {'-'*6}  {'-'*8}  {'-'*9}  {'-'*8}  {'-'*9}")
    tri_data = {1: (0.936, 0.688), 2: (0.942, 0.698),
                3: (0.929, 0.700), 5: (0.853, 0.701),
                8: (0.750, 0.701), 12: (0.667, 0.702),
                20: (0.561, 0.702)}
    for r in r4:
        w = r["width"]
        td, ts = tri_data.get(w, (0, 0))
        print(f"  {w:6d}  {r['dir']:8.3f}  {r['speed']:9.4f}"
              f"  {td:8.3f}  {ts:9.4f}")

    print()
    h_best = max(r["dir"] for r in r4)
    t_best = 0.942
    if h_best > t_best:
        print(f"  ★ HEXAGONAL IS MORE DIRECTIONAL")
        print(f"    Best hex: {h_best:.3f} vs best tri: {t_best:.3f}")
    elif h_best > 0.5:
        print(f"  ~ BOTH PROPAGATE, comparable performance")
        print(f"    Best hex: {h_best:.3f} vs best tri: {t_best:.3f}")
    else:
        print(f"  ✗ HEXAGONAL DOES NOT PROPAGATE WELL")


if __name__ == "__main__":
    main()
