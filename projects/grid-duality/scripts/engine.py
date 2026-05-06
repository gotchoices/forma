"""Lattice engine for grid-duality.

Provides:
- `Lattice` class — graph with nodes and directed edges, plus an
  incidence matrix for vectorised updates.
- Lattice constructors:
    `make_1d_periodic(n)`         — 1D ring of n nodes
    `make_2d_hex_torus(nx, ny)`   — 2D hex on a torus, bipartite orientation

The engine is paradigm-neutral: it supplies the substrate (geometry +
edge polarity) but does not commit to any specific update rule or
state structure. Models in models.py plug into it.
"""

import numpy as np


class Lattice:
    """A graph lattice with nodes and directed edges.

    Edges have polarity (tail → head). The incidence matrix M has
    M[node, edge] = +1 if this node is the edge's head (incoming),
    −1 if this node is the edge's tail (outgoing), 0 otherwise.

    Attributes:
        n_nodes: int
        n_edges: int
        edges: list of (tail_idx, head_idx) tuples
        tails: ndarray shape (n_edges,), node index of each edge's tail
        heads: ndarray shape (n_edges,), node index of each edge's head
        positions: ndarray shape (n_nodes, dim), spatial position per node (for plots)
        M: ndarray shape (n_nodes, n_edges), the signed incidence matrix
    """

    def __init__(self, n_nodes, edges, positions=None, edge_displacements=None):
        self.n_nodes = int(n_nodes)
        self.n_edges = len(edges)
        self.edges = list(edges)
        self.tails = np.array([t for t, _ in edges], dtype=np.int64)
        self.heads = np.array([h for _, h in edges], dtype=np.int64)

        if positions is None:
            positions = np.array([[i] for i in range(n_nodes)], dtype=float)
        self.positions = np.asarray(positions, dtype=float)

        # Incidence matrix
        M = np.zeros((self.n_nodes, self.n_edges), dtype=float)
        for ei, (t, h) in enumerate(edges):
            M[t, ei] = -1.0
            M[h, ei] = +1.0
        self.M = M

        # Coordination per node = number of incident edges (in or out)
        self.coord = np.abs(M).sum(axis=1)

        # Edge geometric direction θ (radians).
        # If displacements are provided (e.g., wrapped for a torus), use them;
        # else compute from raw position differences.
        if edge_displacements is None:
            edge_displacements = self.positions[self.heads] - self.positions[self.tails]
        self.edge_displacements = np.asarray(edge_displacements, dtype=float)
        if self.edge_displacements.shape[-1] >= 2:
            self.theta = np.arctan2(
                self.edge_displacements[:, 1],
                self.edge_displacements[:, 0],
            )
        else:
            self.theta = np.zeros(self.n_edges)


def make_1d_periodic(n):
    """A 1D periodic ring of n nodes connected by n right-pointing edges.

    Edge i: tail at node i, head at node (i+1) mod n.
    Nodes are spaced at integer positions along the x-axis.
    """
    edges = [(i, (i + 1) % n) for i in range(n)]
    positions = np.array([[i, 0.0] for i in range(n)], dtype=float)
    # All edges point in the +x direction (including the wraparound edge).
    edge_displacements = np.tile(np.array([[1.0, 0.0]]), (n, 1))
    return Lattice(n, edges, positions, edge_displacements=edge_displacements)


def make_2d_hex_torus(nx, ny):
    """A 2D hexagonal lattice on a torus, with bipartite (A → B) edge orientation.

    nx × ny unit cells; 2 nodes per cell (A and B sublattices).
    Each A-node connects to 3 B-nodes via outgoing edges (tails at A).
    Periodic in both lattice-vector directions.

    Returns a `Lattice` whose `positions` are the 2D Cartesian coordinates.
    """
    # Hex unit-cell vectors
    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3) / 2])
    d_AB = (a1 + a2) / 3.0  # offset from A to B within a cell

    n_nodes = 2 * nx * ny
    positions = np.zeros((n_nodes, 2))

    def A_idx(i, j):
        return 2 * ((j % ny) * nx + (i % nx))

    def B_idx(i, j):
        return A_idx(i, j) + 1

    for j in range(ny):
        for i in range(nx):
            origin = i * a1 + j * a2
            positions[A_idx(i, j)] = origin
            positions[B_idx(i, j)] = origin + d_AB

    # Edges: each A connects to 3 B's. All edges A → B (bipartite orientation).
    # Displacement vectors per edge are computed from the *unwrapped*
    # neighbor offsets so they reflect the short-image direction even
    # when the edge wraps around the torus.
    edges = []
    edge_displacements = []
    # Local displacements from any A to its three B-neighbors:
    disp_same = d_AB
    disp_left = -a1 + d_AB
    disp_below = -a2 + d_AB

    for j in range(ny):
        for i in range(nx):
            A = A_idx(i, j)
            edges.append((A, B_idx(i, j)));     edge_displacements.append(disp_same)
            edges.append((A, B_idx(i - 1, j))); edge_displacements.append(disp_left)
            edges.append((A, B_idx(i, j - 1))); edge_displacements.append(disp_below)

    edge_displacements = np.array(edge_displacements)
    return Lattice(n_nodes, edges, positions, edge_displacements=edge_displacements)
