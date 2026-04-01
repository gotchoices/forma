"""Triangular lattice generation with periodic boundary conditions.

Builds an Nx × Ny triangular lattice on a torus (periodic in both
directions).  Returns vertex positions and edge connectivity.

Coordinate convention:
  Row i, column j  →  vertex index  i * Nx + j
  Even rows:  x = j,              y = i * (√3/2)
  Odd rows:   x = j + 0.5,        y = i * (√3/2)

Each interior vertex has 6 neighbours.  Periodicity wraps the
boundaries so every vertex is interior.
"""

import numpy as np


def make_lattice(nx: int, ny: int, periodic: bool = True):
    """Return (positions, edges, rest_lengths).

    Parameters
    ----------
    nx, ny : int
        Number of columns / rows.
    periodic : bool
        If True, wrap edges to form a torus.  If False, leave
        boundaries free (finite sheet).

    Returns
    -------
    pos : ndarray, shape (N, 2)
        Equilibrium vertex positions.
    edges : ndarray, shape (E, 2), dtype int
        Pairs of vertex indices (undirected).
    rest_lengths : ndarray, shape (E,)
        All ones (equilateral triangles with unit edge).
    """
    n = nx * ny
    pos = np.empty((n, 2))

    dy = np.sqrt(3.0) / 2.0

    for i in range(ny):
        for j in range(nx):
            idx = i * nx + j
            x = float(j) + (0.5 if i % 2 else 0.0)
            y = float(i) * dy
            pos[idx] = (x, y)

    edge_set = set()

    def add(a, b):
        if a != b:
            edge_set.add((min(a, b), max(a, b)))

    for i in range(ny):
        for j in range(nx):
            v = i * nx + j

            if periodic:
                add(v, i * nx + (j + 1) % nx)
                i_up = (i + 1) % ny
                if i % 2 == 0:
                    add(v, i_up * nx + j)
                    add(v, i_up * nx + (j - 1) % nx)
                else:
                    add(v, i_up * nx + j)
                    add(v, i_up * nx + (j + 1) % nx)
            else:
                if j + 1 < nx:
                    add(v, i * nx + j + 1)
                if i + 1 < ny:
                    i_up = i + 1
                    add(v, i_up * nx + j)
                    if i % 2 == 0:
                        if j - 1 >= 0:
                            add(v, i_up * nx + j - 1)
                    else:
                        if j + 1 < nx:
                            add(v, i_up * nx + j + 1)

    edges = np.array(sorted(edge_set), dtype=int)
    rest_lengths = np.ones(len(edges))

    return pos, edges, rest_lengths


def boundary_vertices(nx: int, ny: int):
    """Return the set of vertex indices on the boundary of a free lattice."""
    bnd = set()
    for j in range(nx):
        bnd.add(j)
        bnd.add((ny - 1) * nx + j)
    for i in range(ny):
        bnd.add(i * nx)
        bnd.add(i * nx + nx - 1)
    return frozenset(bnd)
