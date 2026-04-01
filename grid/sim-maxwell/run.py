#!/usr/bin/env python3
"""sim-maxwell: wave propagation on a triangular lattice.

Tests whether the string junction scattering rule (energy
conservation, no Maxwell input) produces directional wave
propagation.

The scattering matrix at each vertex (N=6 edges) is:
    outgoing_i = (2/N) * total_incoming - incoming_i
               = (1/3) * total - incoming_i

This is the unique solution satisfying:
1. Energy conservation
2. Equal impedance (all edges identical)
3. Linearity

No free parameters.  No Maxwell.  No gauge invariance.

Usage:
    source .venv/bin/activate
    python grid/sim-maxwell/run.py
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ── Lattice (triangular, periodic BCs = torus) ───────────────

def make_lattice(nx, ny):
    V = nx * ny
    pos = np.zeros((V, 2))
    for j in range(ny):
        for i in range(nx):
            pos[j * nx + i] = [i + 0.5 * (j % 2),
                               j * np.sqrt(3) / 2]

    box = np.array([float(nx), ny * np.sqrt(3) / 2])

    edge_set = set()
    edge_list = []
    for j in range(ny):
        for i in range(nx):
            v = j * nx + i
            jup = (j + 1) % ny
            if j % 2 == 0:
                nbrs = [j * nx + (i + 1) % nx,
                         jup * nx + i,
                         jup * nx + (i - 1) % nx]
            else:
                nbrs = [j * nx + (i + 1) % nx,
                         jup * nx + (i + 1) % nx,
                         jup * nx + i]
            for w in nbrs:
                e = (min(v, w), max(v, w))
                if e not in edge_set:
                    edge_set.add(e)
                    edge_list.append(e)

    edges = np.array(edge_list)
    E = len(edges)

    # Edge displacement vectors (shortest on torus)
    edge_dirs = pos[edges[:, 1]] - pos[edges[:, 0]]
    edge_dirs[:, 0] -= box[0] * np.round(edge_dirs[:, 0] / box[0])
    edge_dirs[:, 1] -= box[1] * np.round(edge_dirs[:, 1] / box[1])

    # Edge midpoints
    mid = pos[edges[:, 0]] + edge_dirs / 2

    # Vertex-edge connectivity (all vertices have exactly 6 edges)
    vert_ei = np.zeros((V, 6), dtype=int)
    vert_end = np.zeros((V, 6), dtype=int)
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

    assert np.all(vert_count == 6), \
        f"Coordination error: {vert_count.min()}–{vert_count.max()}"

    return pos, edges, vert_ei, vert_end, edge_dirs, mid, box


# ── Scattering step (vectorised) ─────────────────────────────

def scatter_step(a_fwd, a_bwd, vert_ei, vert_end):
    """One tick: junction scattering at all vertices.

    For N=6 equal-impedance strings:
        outgoing_i = (1/3) * total_incoming - incoming_i
    """
    incoming = np.where(vert_end == 0,
                        a_bwd[vert_ei],
                        a_fwd[vert_ei])

    total = incoming.sum(axis=1, keepdims=True)
    outgoing = (1.0 / 3.0) * total - incoming

    new_fwd = np.zeros_like(a_fwd)
    new_bwd = np.zeros_like(a_bwd)

    mask0 = vert_end == 0
    mask1 = vert_end == 1
    np.add.at(new_fwd, vert_ei[mask0], outgoing[mask0])
    np.add.at(new_bwd, vert_ei[mask1], outgoing[mask1])

    return new_fwd, new_bwd


def evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
           source_fn=None, snapshot_interval=1):
    """Evolve and collect snapshots."""
    snaps = []
    if 0 % snapshot_interval == 0:
        snaps.append((0, a_fwd.copy(), a_bwd.copy()))

    for t in range(1, n_steps + 1):
        a_fwd, a_bwd = scatter_step(a_fwd, a_bwd, vert_ei, vert_end)
        if source_fn is not None:
            a_fwd, a_bwd = source_fn(a_fwd, a_bwd, t)
        if t % snapshot_interval == 0:
            snaps.append((t, a_fwd.copy(), a_bwd.copy()))

    return snaps


# ── Initial conditions ───────────────────────────────────────

def init_wavefront(edge_dirs, mid, box, n_edges,
                   direction=(1.0, 0.0), center=None, width=3.0):
    """Gaussian band of rightward-traveling energy."""
    d = np.array(direction, float)
    d /= np.linalg.norm(d)

    if center is None:
        center = box / 2
    center = np.array(center, float)

    dx = mid - center
    dx[:, 0] -= box[0] * np.round(dx[:, 0] / box[0])
    dx[:, 1] -= box[1] * np.round(dx[:, 1] / box[1])
    dist = dx @ d
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
                      amplitude=0.05):
    """Oscillating source at one vertex."""
    def source_fn(a_fwd, a_bwd, t):
        amp = amplitude * np.sin(omega * t)
        for k in range(6):
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


def energy_centroid(energy, mid, box):
    total = energy.sum()
    if total < 1e-30:
        return box / 2
    cx = np.average(np.cos(2 * np.pi * mid[:, 0] / box[0]),
                    weights=energy)
    sx = np.average(np.sin(2 * np.pi * mid[:, 0] / box[0]),
                    weights=energy)
    cy = np.average(np.cos(2 * np.pi * mid[:, 1] / box[1]),
                    weights=energy)
    sy = np.average(np.sin(2 * np.pi * mid[:, 1] / box[1]),
                    weights=energy)
    x = np.arctan2(sx, cx) * box[0] / (2 * np.pi) % box[0]
    y = np.arctan2(sy, cy) * box[1] / (2 * np.pi) % box[1]
    return np.array([x, y])


def energy_rms_spread(energy, mid, centroid, box):
    """RMS distance of energy from centroid (periodic)."""
    dx = mid - centroid
    dx[:, 0] -= box[0] * np.round(dx[:, 0] / box[0])
    dx[:, 1] -= box[1] * np.round(dx[:, 1] / box[1])
    r2 = (dx ** 2).sum(axis=1)
    total = energy.sum()
    if total < 1e-30:
        return 0.0
    return np.sqrt(np.average(r2, weights=energy))


def directionality_ratio(energy, mid, centroid, direction, box,
                         half_angle=np.pi / 3):
    """Fraction of energy within ±half_angle of direction."""
    d = np.array(direction, float)
    d /= np.linalg.norm(d)

    dx = mid - centroid
    dx[:, 0] -= box[0] * np.round(dx[:, 0] / box[0])
    dx[:, 1] -= box[1] * np.round(dx[:, 1] / box[1])
    r = np.sqrt((dx ** 2).sum(axis=1))
    r = np.maximum(r, 1e-10)
    cos_angle = (dx @ d) / r

    fwd = cos_angle > np.cos(half_angle)
    total = energy.sum()
    if total < 1e-30:
        return 1.0 / 3.0
    return energy[fwd].sum() / total


def angular_distribution(energy, mid, centroid, box, n_bins=36):
    dx = mid - centroid
    dx[:, 0] -= box[0] * np.round(dx[:, 0] / box[0])
    dx[:, 1] -= box[1] * np.round(dx[:, 1] / box[1])
    angles = np.arctan2(dx[:, 1], dx[:, 0])
    bin_edges = np.linspace(-np.pi, np.pi, n_bins + 1)
    hist = np.zeros(n_bins)
    for i in range(n_bins):
        mask = (angles >= bin_edges[i]) & (angles < bin_edges[i + 1])
        hist[i] = energy[mask].sum()
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    return bin_centers, hist


# ── Tests ────────────────────────────────────────────────────

def test_wavefront(nx, ny, n_steps, width, out_dir):
    """Test 1: does a directed wavefront propagate?"""
    print(f"\n{'='*60}")
    print(f"  Test 1: Wavefront propagation ({nx}×{ny}, "
          f"{n_steps} steps, width={width})")
    print(f"{'='*60}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box = \
        make_lattice(nx, ny)
    E = len(edges)
    direction = np.array([1.0, 0.0])

    a_fwd, a_bwd = init_wavefront(
        edge_dirs, mid, box, E,
        direction=direction, width=width)

    E0 = edge_energy(a_fwd, a_bwd).sum()
    c0 = energy_centroid(edge_energy(a_fwd, a_bwd), mid, box)
    print(f"  Initial energy: {E0:.4f}")
    print(f"  Initial centroid: ({c0[0]:.1f}, {c0[1]:.1f})")

    snap_interval = max(1, n_steps // 50)
    snaps = evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
                   snapshot_interval=snap_interval)

    times, spreads, dirs, energies = [], [], [], []
    cum_dx = []
    prev_centroid = c0.copy()
    total_dx = 0.0

    for t, af, ab in snaps:
        en = edge_energy(af, ab)
        c = energy_centroid(en, mid, box)
        s = energy_rms_spread(en, mid, c, box)
        dr = directionality_ratio(en, mid, c0, direction, box)

        # Track cumulative displacement frame-by-frame
        # to avoid torus-wrapping confusion
        step_dx = c[0] - prev_centroid[0]
        step_dx -= box[0] * np.round(step_dx / box[0])
        total_dx += step_dx
        prev_centroid = c.copy()

        times.append(t)
        cum_dx.append(total_dx)
        spreads.append(s)
        dirs.append(dr)
        energies.append(en.sum())

    print(f"\n  Cumulative centroid displacement (x): "
          f"{cum_dx[-1]:.3f} lattice units")
    print(f"  Speed: {cum_dx[-1]/n_steps:.4f} "
          f"lattice units / tick")
    print(f"  Final RMS spread: {spreads[-1]:.2f}")
    print(f"  Initial RMS spread: {spreads[0]:.2f}")
    print(f"  Directionality (fwd 60° cone): "
          f"{dirs[0]:.3f} → {dirs[-1]:.3f}")
    print(f"  Energy conservation: "
          f"{energies[0]:.6f} → {energies[-1]:.6f} "
          f"(ratio {energies[-1]/energies[0]:.8f})")

    # Energy snapshots
    snap_times = [0, n_steps // 4, n_steps // 2,
                  3 * n_steps // 4, n_steps]
    snap_data = {}
    for t, af, ab in snaps:
        if t in snap_times:
            snap_data[t] = edge_energy(af, ab)

    # Plot
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    # Row 0: energy snapshots
    for i, t in enumerate(snap_times[:3]):
        if t in snap_data:
            ax = axes[0, i]
            en = snap_data[t]
            sc = ax.scatter(mid[:, 0], mid[:, 1], c=en, s=0.3,
                            cmap="hot", vmin=0,
                            vmax=max(en.max(), 1e-10))
            ax.set_aspect("equal")
            ax.set_title(f"t = {t}")
            ax.set_xlim(0, box[0])
            ax.set_ylim(0, box[1])

    # Row 1 left: centroid trajectory (cumulative, unwrapped)
    axes[1, 0].plot(times, cum_dx, "b-", lw=2)
    axes[1, 0].set_xlabel("t (ticks)")
    axes[1, 0].set_ylabel("cumulative Δx")
    axes[1, 0].set_title("Centroid displacement (unwrapped)")
    axes[1, 0].grid(True, alpha=0.3)

    # Row 1 middle: spread
    axes[1, 1].plot(times, spreads, "r-", lw=2)
    axes[1, 1].set_xlabel("t (ticks)")
    axes[1, 1].set_ylabel("RMS spread")
    axes[1, 1].set_title("Energy spread")
    axes[1, 1].grid(True, alpha=0.3)

    # Row 1 right: directionality
    axes[1, 2].plot(times, dirs, "g-", lw=2)
    axes[1, 2].axhline(1.0 / 3.0, color="gray", ls="--",
                        label="isotropic (1/3)")
    axes[1, 2].set_xlabel("t (ticks)")
    axes[1, 2].set_ylabel("forward fraction")
    axes[1, 2].set_title("Directionality ratio (±60°)")
    axes[1, 2].legend()
    axes[1, 2].grid(True, alpha=0.3)
    axes[1, 2].set_ylim(0, 1)

    fig.suptitle("sim-maxwell: wavefront propagation", fontsize=14)
    fig.tight_layout()
    path = os.path.join(out_dir, "wavefront.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.close(fig)

    return {
        "speed": cum_dx[-1] / n_steps,
        "spread_ratio": spreads[-1] / max(spreads[0], 0.1),
        "dir_initial": dirs[0],
        "dir_final": dirs[-1],
        "energy_ratio": energies[-1] / energies[0],
    }


def test_single_edge(nx, ny, n_steps, out_dir):
    """Test 2: single edge pulse — expect isotropic diffusion."""
    print(f"\n{'='*60}")
    print(f"  Test 2: Single edge pulse ({nx}×{ny}, {n_steps} steps)")
    print(f"{'='*60}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box = \
        make_lattice(nx, ny)
    E = len(edges)

    # Pick a horizontal edge near the center
    center = box / 2
    dists = np.sqrt(((mid - center) ** 2).sum(axis=1))
    horiz = np.abs(edge_dirs[:, 1]) < 0.1
    candidates = np.where(horiz)[0]
    edge_idx = candidates[np.argmin(dists[candidates])]

    a_fwd, a_bwd = init_single_edge(E, edge_idx)
    direction = edge_dirs[edge_idx].copy()
    direction /= np.linalg.norm(direction)

    c0 = mid[edge_idx].copy()
    E0 = 1.0

    snap_interval = max(1, n_steps // 50)
    snaps = evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
                   snapshot_interval=snap_interval)

    times, spreads, dirs, energies = [], [], [], []
    for t, af, ab in snaps:
        en = edge_energy(af, ab)
        s = energy_rms_spread(en, mid, c0, box)
        dr = directionality_ratio(en, mid, c0, direction, box)
        times.append(t)
        spreads.append(s)
        dirs.append(dr)
        energies.append(en.sum())

    print(f"  Final RMS spread: {spreads[-1]:.2f}")
    print(f"  Directionality: {dirs[0]:.3f} → {dirs[-1]:.3f}")
    print(f"  Isotropic would be: {1.0/3.0:.3f}")
    print(f"  Energy conservation: {energies[-1]/energies[0]:.8f}")

    # Angular distribution at final time
    _, af_final, ab_final = snaps[-1]
    en_final = edge_energy(af_final, ab_final)
    ang, hist = angular_distribution(en_final, mid, c0, box)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Energy snapshot
    snap_t = n_steps // 2
    for t, af, ab in snaps:
        if t == snap_t or (t > snap_t and len(snaps) > 2):
            en = edge_energy(af, ab)
            r = np.sqrt(((mid - c0) ** 2).sum(axis=1))
            view = r < box[0] / 3
            axes[0].scatter(mid[view, 0], mid[view, 1],
                            c=en[view], s=1, cmap="hot")
            axes[0].set_aspect("equal")
            axes[0].set_title(f"Energy at t={t}")
            break

    axes[1].plot(times, spreads, "r-", lw=2)
    axes[1].set_xlabel("t")
    axes[1].set_ylabel("RMS spread")
    axes[1].set_title("Single edge: spread (expect √t diffusion)")
    axes[1].grid(True, alpha=0.3)

    axes[2].bar(np.degrees(ang), hist, width=360 / len(ang),
                alpha=0.7)
    axes[2].set_xlabel("angle (deg)")
    axes[2].set_ylabel("energy")
    axes[2].set_title(f"Angular distribution at t={n_steps}")
    axes[2].grid(True, alpha=0.3)

    fig.suptitle("sim-maxwell: single edge pulse", fontsize=14)
    fig.tight_layout()
    path = os.path.join(out_dir, "single_edge.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.close(fig)

    return {
        "spread_final": spreads[-1],
        "dir_final": dirs[-1],
    }


def test_point_source(nx, ny, n_steps, omega, out_dir):
    """Test 3: oscillating point source — expect circular waves."""
    print(f"\n{'='*60}")
    print(f"  Test 3: Point source ({nx}×{ny}, {n_steps} steps, "
          f"ω={omega:.2f})")
    print(f"{'='*60}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box = \
        make_lattice(nx, ny)
    E = len(edges)

    center_vert = (ny // 2) * nx + nx // 2
    source_fn = make_point_source(vert_ei, vert_end, center_vert,
                                  omega)
    a_fwd = np.zeros(E)
    a_bwd = np.zeros(E)

    center_pos = pos[center_vert]

    snap_interval = max(1, n_steps // 50)
    snaps = evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
                   source_fn=source_fn,
                   snapshot_interval=snap_interval)

    # Radial amplitude profile at final time
    _, af_final, ab_final = snaps[-1]
    en_final = edge_energy(af_final, ab_final)
    amp_final = np.sqrt(en_final)

    dx = mid - center_pos
    dx[:, 0] -= box[0] * np.round(dx[:, 0] / box[0])
    dx[:, 1] -= box[1] * np.round(dx[:, 1] / box[1])
    r = np.sqrt((dx ** 2).sum(axis=1))

    # Bin by distance
    r_max = min(box) / 3
    bins = np.linspace(0.5, r_max, 40)
    r_mid, amp_mean = [], []
    for lo, hi in zip(bins[:-1], bins[1:]):
        mask = (r >= lo) & (r < hi)
        if mask.sum() < 5:
            continue
        r_mid.append(0.5 * (lo + hi))
        amp_mean.append(amp_final[mask].mean())
    r_mid = np.array(r_mid)
    amp_mean = np.array(amp_mean)

    # Fit 1/√r (2D cylindrical wave)
    if len(r_mid) > 5:
        mask = (r_mid > 3) & (r_mid < r_max * 0.8) & (amp_mean > 0)
        if mask.sum() > 3:
            lr = np.log(r_mid[mask])
            la = np.log(amp_mean[mask])
            c = np.polyfit(lr, la, 1)
            p = -c[0]
            pred = np.exp(c[1]) * r_mid[mask] ** (-p)
            ss_r = np.sum((la - (c[0] * lr + c[1])) ** 2)
            ss_t = np.sum((la - la.mean()) ** 2)
            r2 = 1.0 - ss_r / ss_t if ss_t > 0 else 0.0
            print(f"  Amplitude ∝ r^(−{p:.3f}), R² = {r2:.4f}")
            print(f"  2D cylindrical wave: expect p ≈ 0.5")
        else:
            p, r2, pred = np.nan, 0, None
    else:
        p, r2, pred = np.nan, 0, None

    # Angular isotropy check
    ang, hist = angular_distribution(en_final, mid, center_pos, box)
    isotropy = hist.std() / hist.mean() if hist.mean() > 0 else 0
    print(f"  Angular isotropy (CoV): {isotropy:.3f} "
          f"(0 = perfect)")

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Snapshot
    _, af_mid, ab_mid = snaps[len(snaps) // 2]
    en_mid = edge_energy(af_mid, ab_mid)
    view = r < r_max
    axes[0].scatter(mid[view, 0], mid[view, 1],
                    c=en_mid[view], s=1, cmap="hot")
    axes[0].set_aspect("equal")
    axes[0].set_title(f"Energy at t={snaps[len(snaps)//2][0]}")

    # Radial profile
    if len(r_mid) > 0:
        axes[1].plot(r_mid, amp_mean, "bo", ms=3)
        if pred is not None:
            axes[1].plot(r_mid[mask], pred, "r-", lw=2,
                         label=f"r$^{{-{p:.2f}}}$, R²={r2:.3f}")
        axes[1].set_xscale("log")
        axes[1].set_yscale("log")
        axes[1].set_xlabel("r")
        axes[1].set_ylabel("amplitude")
        axes[1].set_title("Radial amplitude")
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)

    # Angular
    axes[2].bar(np.degrees(ang), hist, width=360 / len(ang),
                alpha=0.7)
    axes[2].set_xlabel("angle (deg)")
    axes[2].set_ylabel("energy")
    axes[2].set_title("Angular distribution")
    axes[2].grid(True, alpha=0.3)

    fig.suptitle("sim-maxwell: point source", fontsize=14)
    fig.tight_layout()
    path = os.path.join(out_dir, "point_source.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.close(fig)

    return {"p": p, "r2": r2, "isotropy_cov": isotropy}


def test_wavelength(nx, ny, n_steps, out_dir):
    """Test 4: directionality vs wavefront width (proxy for λ)."""
    print(f"\n{'='*60}")
    print(f"  Test 4: Wavelength dependence ({nx}×{ny})")
    print(f"{'='*60}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box = \
        make_lattice(nx, ny)
    E = len(edges)
    direction = np.array([1.0, 0.0])

    widths = [1, 2, 3, 5, 8, 12, 20]
    results_w = []

    for w in widths:
        a_fwd, a_bwd = init_wavefront(
            edge_dirs, mid, box, E,
            direction=direction, width=float(w))
        snaps = evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
                       snapshot_interval=n_steps)
        _, af, ab = snaps[-1]
        en = edge_energy(af, ab)
        c0 = energy_centroid(edge_energy(a_fwd, a_bwd), mid, box)
        dr = directionality_ratio(en, mid, c0, direction, box)

        c_final = energy_centroid(en, mid, box)
        dx_c = c_final[0] - c0[0]
        dx_c -= box[0] * np.round(dx_c / box[0])
        speed = dx_c / n_steps

        results_w.append({"width": w, "dir": dr, "speed": speed})
        print(f"  width={w:3d}: dir={dr:.3f}, speed={speed:.4f}")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    ws = [r["width"] for r in results_w]
    ds = [r["dir"] for r in results_w]
    ss = [r["speed"] for r in results_w]

    axes[0].plot(ws, ds, "bo-", lw=2)
    axes[0].axhline(1.0 / 3.0, color="gray", ls="--",
                    label="isotropic")
    axes[0].set_xlabel("wavefront width (lattice units)")
    axes[0].set_ylabel("directionality ratio")
    axes[0].set_title("Directionality vs wavefront width")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(ws, ss, "ro-", lw=2)
    axes[1].set_xlabel("wavefront width (lattice units)")
    axes[1].set_ylabel("propagation speed (units/tick)")
    axes[1].set_title("Speed vs wavefront width")
    axes[1].grid(True, alpha=0.3)

    fig.suptitle("sim-maxwell: wavelength dependence", fontsize=14)
    fig.tight_layout()
    path = os.path.join(out_dir, "wavelength.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.close(fig)

    return results_w


# ── Main ─────────────────────────────────────────────────────

def main():
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(out_dir, exist_ok=True)

    print("sim-maxwell: wave propagation on a triangular lattice")
    print("Scattering rule: outgoing_i = (1/3)*total - incoming_i")
    print("(energy conservation, equal impedance, no Maxwell input)")

    # Test 1: wavefront
    r1 = test_wavefront(100, 100, n_steps=80, width=5.0,
                        out_dir=out_dir)

    # Test 2: single edge pulse
    r2 = test_single_edge(60, 60, n_steps=40, out_dir=out_dir)

    # Test 3: point source
    r3 = test_point_source(80, 80, n_steps=60, omega=1.0,
                           out_dir=out_dir)

    # Test 4: wavelength dependence
    r4 = test_wavelength(80, 80, n_steps=50, out_dir=out_dir)

    # Summary
    print(f"\n{'='*72}")
    print("  SUMMARY — sim-maxwell")
    print(f"{'='*72}")
    print(f"\n  Scattering rule: outgoing = (1/3)*total − incoming")
    print(f"  (N=6 equal-impedance strings, no free parameters)")
    print()
    print(f"  Test 1 — Wavefront propagation:")
    print(f"    Speed:          {r1['speed']:.4f} lattice units/tick")
    print(f"    Spread ratio:   {r1['spread_ratio']:.2f}×")
    print(f"    Directionality: {r1['dir_initial']:.3f} → "
          f"{r1['dir_final']:.3f}")
    print(f"    Energy conserved: "
          f"{r1['energy_ratio']:.8f}")
    print()
    print(f"  Test 2 — Single edge pulse:")
    print(f"    Final spread:   {r2['spread_final']:.2f}")
    print(f"    Directionality: {r2['dir_final']:.3f} "
          f"(isotropic = {1/3:.3f})")
    print()
    print(f"  Test 3 — Point source:")
    print(f"    Amplitude ∝ r^(−{r3['p']:.3f}), R²={r3['r2']:.4f}")
    print(f"    Angular CoV:    {r3['isotropy_cov']:.3f}")
    print(f"    (2D cylindrical wave: p = 0.5, CoV → 0)")
    print()
    print(f"  Test 4 — Width dependence:")
    for r in r4:
        print(f"    width={r['width']:3d}: "
              f"dir={r['dir']:.3f}, speed={r['speed']:.4f}")

    print()
    speed = r1['speed']
    t4_best = max(r["dir"] for r in r4)
    if abs(speed) > 0.1 and t4_best > 0.5:
        print("  ★ DIRECTIONAL PROPAGATION OBSERVED")
        print(f"    Speed ≈ {abs(speed):.2f} lattice units/tick")
        print(f"    Best directionality: {t4_best:.1%}")
        print("    Coherent wavefronts propagate; single pulses scatter.")
        print("    This is Huygens' principle on the discrete lattice.")
    elif t4_best > 0.4:
        print("  ~ WEAK DIRECTIONALITY")
        print("    Some forward bias but not strongly directional.")
    else:
        print("  ✗ ISOTROPIC DIFFUSION")
        print("    Energy spreads uniformly. The junction scattering")
        print("    rule alone does not produce directional waves.")
        print("    Fallback: try Level 1–3 approaches (README.md).")


if __name__ == "__main__":
    main()
