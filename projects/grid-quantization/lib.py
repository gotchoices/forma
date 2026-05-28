"""Honeycomb (N=3) lattice substrate for the grid-quantization project.

Self-contained copy of the minimal lattice machinery this project
needs: honeycomb construction on a torus, the equal-impedance
junction scattering rule, synchronous evolution, a wavefront
initializer, and the edge-energy measure.

Adapted from grid/sim-maxwell/run_hex.py (the completed substrate
study).  Kept here so this speculative project is independent of
that study and can diverge freely — in particular, Tier 2 will need
complex/phasor amplitudes and a modified scatter rule that should
NOT touch the grid/ folder.

The junction rule for N equal-impedance strings (energy
conservation + equal impedance, no Maxwell input):

    outgoing_i = (2/N) * total_incoming - incoming_i

For the honeycomb (N=3): reflection -1/3, transmission 2/3 each.
"""

import numpy as np


# ── Honeycomb lattice on a torus ──────────────────────────────

def make_honeycomb(nx, ny):
    """Honeycomb lattice on a torus (periodic BCs).

    Two vertices per unit cell (A and B sublattices); each vertex
    has exactly 3 edges (N=3).  Total vertices 2*nx*ny, edges
    3*nx*ny, hexagonal faces nx*ny (Euler: V-E+F = 0 on the torus).

    Returns (pos, edges, vert_ei, vert_end, edge_dirs, mid,
             box_rect, wrap).
    """
    V = 2 * nx * ny
    pos = np.zeros((V, 2))

    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3) / 2])
    d_AB = (a1 + a2) / 3.0  # A→B offset within a cell

    for j in range(ny):
        for i in range(nx):
            cell = j * nx + i
            origin = i * a1 + j * a2
            pos[2 * cell] = origin            # A sublattice
            pos[2 * cell + 1] = origin + d_AB  # B sublattice

    box_a = nx * a1
    box_b = ny * a2
    box_matrix = np.column_stack([box_a, box_b])
    box_inv = np.linalg.inv(box_matrix)

    def wrap(delta):
        frac = box_inv @ delta
        frac -= np.round(frac)
        return box_matrix @ frac

    edge_set = set()
    edge_list = []
    for j in range(ny):
        for i in range(nx):
            cell = j * nx + i
            A = 2 * cell
            B_same = A + 1
            i_left = (i - 1) % nx
            B_left = 2 * (j * nx + i_left) + 1
            j_below = (j - 1) % ny
            B_below = 2 * (j_below * nx + i) + 1
            for B in [B_same, B_left, B_below]:
                e = (min(A, B), max(A, B))
                if e not in edge_set:
                    edge_set.add(e)
                    edge_list.append(e)

    edges = np.array(edge_list)
    E = len(edges)

    edge_dirs = np.zeros((E, 2))
    for ei, (u, v) in enumerate(edges):
        edge_dirs[ei] = wrap(pos[v] - pos[u])

    mid = pos[edges[:, 0]] + edge_dirs / 2

    all_corners = np.array([[0, 0], box_a, box_b, box_a + box_b])
    box_rect = np.array([all_corners[:, 0].max(),
                         all_corners[:, 1].max()])

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


# ── Scattering and evolution ─────────────────────────────────

def scatter_step(a_fwd, a_bwd, vert_ei, vert_end, N=3):
    """One synchronous tick of junction scattering at all vertices."""
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
    """Evolve and collect (tick, a_fwd, a_bwd) snapshots."""
    snaps = [(0, a_fwd.copy(), a_bwd.copy())]
    for t in range(1, n_steps + 1):
        a_fwd, a_bwd = scatter_step(a_fwd, a_bwd,
                                     vert_ei, vert_end, N)
        if source_fn is not None:
            a_fwd, a_bwd = source_fn(a_fwd, a_bwd, t)
        if t % snapshot_interval == 0:
            snaps.append((t, a_fwd.copy(), a_bwd.copy()))
    return snaps


# ── Initial conditions and measurement ───────────────────────

def init_wavefront(edge_dirs, mid, box, n_edges, wrap_fn,
                   direction=(1.0, 0.0), center=None, width=3.0):
    """Gaussian band of traveling energy along `direction`."""
    d = np.array(direction, float)
    d /= np.linalg.norm(d)
    if center is None:
        center = box / 2
    center = np.array(center, float)

    dist = np.zeros(n_edges)
    for ei in range(n_edges):
        dist[ei] = wrap_fn(mid[ei] - center) @ d

    envelope = np.exp(-dist ** 2 / (2 * width ** 2))
    proj = edge_dirs @ d
    a_fwd = np.zeros(n_edges)
    a_bwd = np.zeros(n_edges)
    a_fwd[proj > 0] = np.abs(proj[proj > 0]) * envelope[proj > 0]
    a_bwd[proj < 0] = np.abs(proj[proj < 0]) * envelope[proj < 0]
    return a_fwd, a_bwd


def edge_energy(a_fwd, a_bwd):
    return a_fwd ** 2 + a_bwd ** 2
