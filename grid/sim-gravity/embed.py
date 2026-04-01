"""Insert a rigid body into the lattice.

The rigid body is a small cluster of vertices whose positions are
frozen during relaxation.  This models a flat compact sub-structure
(the Ma torus cross-section) embedded in the ambient lattice (S).

Three built-in shapes:
  "triangle"  — 1 triangle  (3 vertices)
  "hexagon"   — 6 triangles (7 vertices: centre + ring)
  "patch"     — all vertices within a given radius of centre
"""

import numpy as np


def find_nearest(pos: np.ndarray, target: np.ndarray) -> int:
    """Index of the vertex closest to *target*."""
    return int(np.argmin(np.sum((pos - target) ** 2, axis=1)))


def embed_triangle(pos: np.ndarray, edges: np.ndarray,
                   centre: np.ndarray | None = None):
    """Freeze one triangle near *centre* (default: lattice midpoint).

    Returns the set of frozen vertex indices.
    """
    if centre is None:
        centre = pos.mean(axis=0)
    c = find_nearest(pos, centre)
    nbrs = set()
    for a, b in edges:
        if a == c:
            nbrs.add(b)
        elif b == c:
            nbrs.add(a)
    nbrs = sorted(nbrs)
    return frozenset([c, nbrs[0], nbrs[1]])


def embed_hexagon(pos: np.ndarray, edges: np.ndarray,
                  centre: np.ndarray | None = None):
    """Freeze a hexagonal ring (centre + 6 neighbours)."""
    if centre is None:
        centre = pos.mean(axis=0)
    c = find_nearest(pos, centre)
    nbrs = set()
    for a, b in edges:
        if a == c:
            nbrs.add(b)
        elif b == c:
            nbrs.add(a)
    return frozenset([c] + sorted(nbrs))


def embed_patch(pos: np.ndarray, radius: float,
                centre: np.ndarray | None = None):
    """Freeze all vertices within *radius* of *centre*."""
    if centre is None:
        centre = pos.mean(axis=0)
    dists = np.sqrt(np.sum((pos - centre) ** 2, axis=1))
    return frozenset(int(i) for i in np.where(dists <= radius)[0])


def apply_dilation(pos: np.ndarray, frozen: frozenset,
                   scale: float = 1.2) -> np.ndarray:
    """Expand the rigid body by *scale* to create a defect.

    Returns a copy of *pos* with the frozen vertices moved outward
    from their centroid.  The surrounding lattice keeps its original
    equilibrium positions, creating stress that must be relaxed.
    """
    pos = pos.copy()
    flist = sorted(frozen)
    centroid = pos[flist].mean(axis=0)
    for v in flist:
        pos[v] = centroid + scale * (pos[v] - centroid)
    return pos
