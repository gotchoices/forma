#!/usr/bin/env python3
"""
Track 6, Step 0: Euclidean 4D node coincidence.

Test whether the dimensional effect alone (going from 3D to 4D)
changes the coincidence rate between a 2D hexagonal lattice and
the ambient lattice enough to approach 1/137.

The 4D lattice is the D4 diamond analog:
  - Sublattice A: all integer points (x1,x2,x3,x4) with x1+x2+x3+x4 even
  - Sublattice B: A shifted by (1/2, 1/2, 1/2, 1/2)
  - Each A node has 8 nearest B neighbors at distance sqrt(4*(1/2)^2) = 1
    (the 8 vectors (±1/2, ±1/2, ±1/2, ±1/2) with even number of minus signs...
     actually for D4, the nearest neighbors from an A-node to B-nodes are the
     8 half-integer shifts that are nearest)

Wait — let me reconsider the D4 diamond construction.

D4 root lattice: all integer vectors in R^4 with even coordinate sum.
Nearest neighbors in D4 are at distance sqrt(2), being the 24 vectors
of the form (±1, ±1, 0, 0) (all permutations, any signs) with even sum.

The "diamond" analog (bipartite) uses D4 and its coset D4 + (1/2,1/2,1/2,1/2).
A node at the origin (in D4) connects to the 8 nearest coset nodes at
(±1/2, ±1/2, ±1/2, ±1/2) with an even number of minus signs — distance 1.
But we want 5 edges per node (4-simplex coordination), not 8.

Actually the 4D analog of the diamond lattice should have simplex
coordination (5 neighbors).  The D4 lattice with ALL nearest neighbors
has 24 (the kissing number in 4D).  The bipartite D4+coset gives 8.
Neither is 5.

For GRID's purposes, we need a lattice where each node connects to
exactly 5 neighbors in directions forming a regular 4-simplex.  This
is different from D4.

The 5 simplex directions in 4D (regular 4-simplex centered at origin):
We use these as the neighbor offsets from each A-node to its B-neighbors.
Then from each B-node, the 5 edges point back (negated directions) to
A-nodes.  This creates a bipartite lattice.

The regular 4-simplex vertex coordinates (centered, unit edge length):
Using the standard construction — see computation below.

APPROACH:
Rather than worry about the full infinite lattice algebra, we:
1. Fix the 5 simplex edge directions (unit vectors in R^4)
2. Build the lattice by BFS: start at origin, walk along simplex edges
   alternating A/B sublattices, up to some depth
3. Embed the 2D hexagonal lattice on various 2-planes in R^4
4. Count how many hex nodes land on lattice nodes (within tolerance)

This is exactly the Track 1 approach generalized to 4D.
"""

import numpy as np
from scipy.spatial import cKDTree
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent.parent / "output"
OUT.mkdir(exist_ok=True)

# ── Regular 4-simplex: 5 vertices in R^4 ───────────────────────
# Standard construction: place vertices of regular 4-simplex
# centered at origin with unit edge length.
#
# The 5 vertices of a regular 4-simplex in R^4:
# v_k for k=0..3: e_k * sqrt(2/5) - (1/4) * sum(e_j) * correction
# Simpler: use the known coordinates.
#
# Regular 4-simplex with vertices at unit distance from origin:
# v_i = (e_i - (1/5) sum(e_j)) * scale, plus one vertex at
# (a, a, a, a) pointing "up" in all dimensions.

def make_simplex_directions():
    """Return 5 unit vectors in R^4 forming a regular 4-simplex.

    All pairwise angles = arccos(-1/4) ≈ 104.48°.
    All vectors have unit length.
    Sum of all 5 vectors = 0 (centered at origin).
    """
    # Start with 5 vertices of regular 4-simplex.
    # Construction: embed the 4-simplex in R^4.
    # One clean construction:
    #   v_k = sqrt(2/5) * e_k  for k = 0,1,2,3
    #   v_4 = (-1/sqrt(10), -1/sqrt(10), -1/sqrt(10), -1/sqrt(10))
    # then normalize so all have the same length.
    #
    # Actually, let me just compute directly.
    # For a regular n-simplex in R^n, vertices can be:
    # v_i for i=1..n: the i-th standard basis vector
    # v_0: (c, c, ..., c) where c is chosen so |v_0 - v_i| = |v_i - v_j| = sqrt(2)
    # c satisfies: (1-c)^2 + (n-1)*c^2 = 2
    # => 1 - 2c + c^2 + (n-1)c^2 = 2
    # => nc^2 - 2c - 1 = 0
    # => c = (2 ± sqrt(4 + 4n)) / (2n) = (1 ± sqrt(1+n)) / n
    # Take c = (1 + sqrt(1+n)) / n  (the one that puts v_0 on the same side)

    n = 4  # dimension
    c = (1 + np.sqrt(1 + n)) / n
    # Vertices of the simplex (edge length sqrt(2))
    verts = np.eye(n)  # v_1 through v_4
    v0 = np.full(n, c)
    verts = np.vstack([v0, verts])  # shape (5, 4)

    # Center at origin
    center = verts.mean(axis=0)
    verts -= center

    # Normalize to unit length
    norms = np.linalg.norm(verts, axis=1, keepdims=True)
    verts = verts / norms

    # Verify: all pairwise dot products should be -1/4
    for i in range(5):
        for j in range(i+1, 5):
            dot = np.dot(verts[i], verts[j])
            angle = np.degrees(np.arccos(np.clip(dot, -1, 1)))
            assert abs(dot - (-0.25)) < 1e-10, \
                f"Bad dot product {dot} between v{i} and v{j} (angle={angle:.2f}°)"

    return verts


SIMPLEX_DIRS = make_simplex_directions()


# ── Build the bipartite simplex lattice ─────────────────────────

def build_lattice(depth=6):
    """Build a bipartite simplex lattice in 4D by BFS.

    Sublattice A has nodes connected to B by +simplex_dirs (scaled).
    Sublattice B has nodes connected to A by -simplex_dirs (scaled).

    The edge length is chosen so nearest-neighbor distance = 1.
    Since simplex_dirs are unit vectors, the edge displacement IS
    the direction vector (length 1).

    Returns:
        nodes_a: (N_a, 4) array of A-sublattice positions
        nodes_b: (N_b, 4) array of B-sublattice positions
        all_nodes: (N, 4) array of all positions
    """
    # Edge vectors from A → B
    edge_vectors = SIMPLEX_DIRS.copy()  # 5 directions, unit length

    # BFS: track visited nodes by rounding to grid
    # Use a dict keyed by rounded coordinates
    tolerance = 0.01  # for identifying revisited nodes

    def key(pt):
        """Round to grid for deduplication."""
        return tuple(np.round(pt / tolerance).astype(int))

    nodes_a = {key(np.zeros(4)): np.zeros(4)}
    nodes_b = {}

    frontier_a = [np.zeros(4)]  # current frontier to expand
    is_a_frontier = True

    for step in range(depth):
        new_frontier = []
        if is_a_frontier:
            # Expand A nodes → create B nodes
            for node in frontier_a:
                for ev in edge_vectors:
                    new_pt = node + ev
                    k = key(new_pt)
                    if k not in nodes_b:
                        nodes_b[k] = new_pt
                        new_frontier.append(new_pt)
        else:
            # Expand B nodes → create A nodes
            for node in frontier_a:
                for ev in edge_vectors:
                    new_pt = node - ev  # B → A is -direction
                    k = key(new_pt)
                    if k not in nodes_a:
                        nodes_a[k] = new_pt
                        new_frontier.append(new_pt)

        frontier_a = new_frontier
        is_a_frontier = not is_a_frontier
        print(f"  BFS step {step+1}: frontier={len(frontier_a)}, "
              f"A={len(nodes_a)}, B={len(nodes_b)}")

    a = np.array(list(nodes_a.values()))
    b = np.array(list(nodes_b.values()))
    all_nodes = np.vstack([a, b])

    print(f"  Total: {len(all_nodes)} nodes ({len(a)} A + {len(b)} B)")
    return a, b, all_nodes


# ── 2D hexagonal lattice in a plane ─────────────────────────────

def hex_lattice_2d(n_rings=10):
    """Generate a 2D hexagonal lattice with edge length 1.

    Returns (N, 2) array of node positions in 2D.
    The lattice is centered at origin.
    """
    # Hexagonal lattice basis vectors (edge length 1)
    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3)/2])

    pts = []
    for i in range(-n_rings, n_rings+1):
        for j in range(-n_rings, n_rings+1):
            pt = i * a1 + j * a2
            if np.linalg.norm(pt) <= n_rings + 0.5:
                pts.append(pt)

    return np.array(pts)


def embed_hex_in_4d(hex_2d, e1, e2, origin=None):
    """Embed 2D hex lattice points into 4D using basis vectors e1, e2.

    hex_2d: (N, 2) array of 2D coordinates
    e1, e2: orthonormal 4D vectors spanning the plane
    origin: 4D offset (default: zero)

    Returns (N, 4) array.
    """
    if origin is None:
        origin = np.zeros(4)
    # pts_4d[i] = origin + hex_2d[i,0] * e1 + hex_2d[i,1] * e2
    return origin + hex_2d[:, 0:1] * e1 + hex_2d[:, 1:2] * e2


# ── Random orientations on Gr(2,4) ─────────────────────────────

def random_2plane():
    """Sample a random oriented 2-plane in R^4 (uniform on Grassmannian).

    Returns two orthonormal vectors e1, e2 in R^4.
    """
    # Sample a random 4x2 matrix, then QR decompose
    M = np.random.randn(4, 2)
    Q, _ = np.linalg.qr(M)
    return Q[:, 0], Q[:, 1]


def parametric_2plane(angles):
    """Parametric 2-plane from 4 angles (covers Gr(2,4)).

    Uses the exponential map approach: start from a reference plane
    (e1 = (1,0,0,0), e2 = (0,1,0,0)) and apply rotations.

    angles: (a1, a2, a3, a4) — four angles parameterizing Gr(2,4).
    """
    a1, a2, a3, a4 = angles

    # Start with reference plane: xy-plane in 4D
    e1 = np.array([1.0, 0, 0, 0])
    e2 = np.array([0, 1.0, 0, 0])

    # Apply rotations in the 6 coordinate planes
    # Gr(2,4) has dim 4, so 4 rotations suffice

    # Rotation in (1,3) plane by a1
    def rot(v, i, j, angle):
        w = v.copy()
        c, s = np.cos(angle), np.sin(angle)
        w[i] = c * v[i] - s * v[j]
        w[j] = s * v[i] + c * v[j]
        return w

    # Apply 4 independent rotations that mix the plane with the normal space
    e1 = rot(e1, 0, 2, a1)
    e2 = rot(e2, 0, 2, a1)
    e1 = rot(e1, 1, 3, a2)
    e2 = rot(e2, 1, 3, a2)
    e1 = rot(e1, 0, 3, a3)
    e2 = rot(e2, 0, 3, a3)
    e1 = rot(e1, 1, 2, a4)
    e2 = rot(e2, 1, 2, a4)

    # Re-orthonormalize (Gram-Schmidt)
    e1 = e1 / np.linalg.norm(e1)
    e2 = e2 - np.dot(e2, e1) * e1
    e2 = e2 / np.linalg.norm(e2)

    return e1, e2


# ── Coincidence counting ────────────────────────────────────────

def count_coincidences(hex_4d, lattice_tree, tol):
    """Count how many hex nodes are within `tol` of any lattice node.

    Returns:
        n_hits: number of hex nodes near a lattice node
        fraction: n_hits / total hex nodes
    """
    # Query: for each hex node, is there a lattice node within tol?
    dists, _ = lattice_tree.query(hex_4d)
    n_hits = np.count_nonzero(dists < tol)
    return n_hits, n_hits / len(hex_4d)


# ── Main computation ────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  Track 6, Step 0: Euclidean 4D node coincidence")
    print("=" * 60)

    # ── Verify simplex directions ──
    print("\n── Simplex directions (5 edges in 4D) ──")
    for i, d in enumerate(SIMPLEX_DIRS):
        print(f"  d{i+1} = ({d[0]:+.4f}, {d[1]:+.4f}, {d[2]:+.4f}, {d[3]:+.4f})")

    # Pairwise angles
    print("\n  Pairwise angles:")
    for i in range(5):
        for j in range(i+1, 5):
            dot = np.dot(SIMPLEX_DIRS[i], SIMPLEX_DIRS[j])
            angle = np.degrees(np.arccos(np.clip(dot, -1, 1)))
            print(f"    d{i+1}·d{j+1} = {dot:+.4f}  angle = {angle:.2f}°")

    # ── Build lattice ──
    print("\n── Building 4D simplex lattice (BFS) ──")
    nodes_a, nodes_b, all_nodes = build_lattice(depth=16)

    # Verify nearest-neighbor distances
    tree = cKDTree(all_nodes)
    sample = all_nodes[:min(100, len(all_nodes))]
    dists, _ = tree.query(sample, k=2)  # k=2: self + nearest
    nn_dists = dists[:, 1]  # nearest neighbor (not self)
    print(f"\n  Nearest-neighbor distances (sample of {len(sample)}):")
    print(f"    min = {nn_dists.min():.4f}")
    print(f"    max = {nn_dists.max():.4f}")
    print(f"    mean = {nn_dists.mean():.4f}")
    print(f"    Expected: 1.0000")

    # Check coordination number
    dists_6, _ = tree.query(sample, k=7)
    nn_count = np.sum(dists_6[:, 1:] < 1.01, axis=1)
    print(f"  Coordination number (sample): mean={nn_count.mean():.1f}, "
          f"min={nn_count.min()}, max={nn_count.max()}")
    print(f"  Expected: 5 (interior nodes)")

    # Lattice extent
    extents = all_nodes.max(axis=0) - all_nodes.min(axis=0)
    print(f"  Lattice extent: {extents}")

    # ── Generate 2D hex lattice ──
    print("\n── 2D hexagonal lattice ──")
    n_rings = 15
    hex_2d = hex_lattice_2d(n_rings=n_rings)
    print(f"  {len(hex_2d)} nodes (n_rings={n_rings})")

    # Trim lattice to avoid boundary effects:
    # Only use the central region of the 4D lattice
    center = all_nodes.mean(axis=0)
    radii = np.linalg.norm(all_nodes - center, axis=1)
    R_cut = np.percentile(radii, 60)  # use inner 60%
    mask = radii < R_cut
    lattice_core = all_nodes[mask]
    print(f"  Lattice core: {len(lattice_core)} nodes (R < {R_cut:.2f})")

    core_tree = cKDTree(lattice_core)

    # ── Part 1: Random orientation sweep ──
    print("\n── Part 1: Random orientation sweep ──")
    n_orient = 500
    tolerances = [0.05, 0.10, 0.15, 0.20, 0.30]

    results = {tol: [] for tol in tolerances}

    for trial in range(n_orient):
        e1, e2 = random_2plane()
        hex_4d = embed_hex_in_4d(hex_2d, e1, e2, origin=center)

        # Only count hex nodes that fall inside the lattice core region
        hex_radii = np.linalg.norm(hex_4d - center, axis=1)
        hex_mask = hex_radii < R_cut * 0.8  # tighter cut for hex
        if hex_mask.sum() < 10:
            continue
        hex_core = hex_4d[hex_mask]

        for tol in tolerances:
            n_hits, frac = count_coincidences(hex_core, core_tree, tol)
            results[tol].append(frac)

        if (trial + 1) % 100 == 0:
            print(f"  {trial+1}/{n_orient} orientations done")

    print(f"\n  Results ({n_orient} random orientations):")
    print(f"  {'tol':>6s}  {'mean frac':>10s}  {'std':>10s}  "
          f"{'min':>10s}  {'max':>10s}  {'1/frac':>10s}  {'1/137':>10s}")
    print("  " + "─" * 75)
    for tol in tolerances:
        fracs = np.array(results[tol])
        if len(fracs) == 0:
            continue
        mean_f = fracs.mean()
        std_f = fracs.std()
        inv = 1.0 / mean_f if mean_f > 0 else float('inf')
        print(f"  {tol:6.2f}  {mean_f:10.6f}  {std_f:10.6f}  "
              f"{fracs.min():10.6f}  {fracs.max():10.6f}  "
              f"{inv:10.1f}  {137.036:10.1f}")

    # ── Part 2: Tolerance scaling (finer) ──
    print("\n── Part 2: Tolerance scaling ──")
    fine_tols = np.array([0.01, 0.02, 0.03, 0.05, 0.07, 0.10,
                          0.15, 0.20, 0.25, 0.30, 0.40, 0.50])
    n_orient2 = 200

    tol_means = []
    for tol in fine_tols:
        fracs = []
        for _ in range(n_orient2):
            e1, e2 = random_2plane()
            hex_4d = embed_hex_in_4d(hex_2d, e1, e2, origin=center)
            hex_radii = np.linalg.norm(hex_4d - center, axis=1)
            hex_mask = hex_radii < R_cut * 0.8
            if hex_mask.sum() < 10:
                continue
            hex_core = hex_4d[hex_mask]
            n_hits, frac = count_coincidences(hex_core, core_tree, tol)
            fracs.append(frac)
        mean_f = np.mean(fracs) if fracs else 0
        tol_means.append(mean_f)
        inv = 1.0 / mean_f if mean_f > 0 else float('inf')
        print(f"  tol={tol:.3f}  mean_frac={mean_f:.6f}  1/frac={inv:.1f}")

    # ── Part 3: Find tolerance where 1/frac ≈ 137 ──
    print("\n── Part 3: Searching for tol where 1/frac ≈ 137 ──")
    tol_means = np.array(tol_means)
    inv_fracs = 1.0 / np.where(tol_means > 0, tol_means, 1e-30)

    # Interpolate
    for i in range(len(fine_tols) - 1):
        if (inv_fracs[i] - 137) * (inv_fracs[i+1] - 137) < 0:
            # Linear interpolation
            t1, t2 = fine_tols[i], fine_tols[i+1]
            f1, f2 = inv_fracs[i], inv_fracs[i+1]
            t_137 = t1 + (137 - f1) * (t2 - t1) / (f2 - f1)
            print(f"  1/frac crosses 137 between tol={t1:.3f} and {t2:.3f}")
            print(f"  Interpolated: tol ≈ {t_137:.4f}")
            break
    else:
        print(f"  1/frac range: {inv_fracs.min():.1f} to {inv_fracs.max():.1f}")
        if inv_fracs.min() > 137:
            print(f"  All above 137 — need larger tolerance")
        elif inv_fracs.max() < 137:
            print(f"  All below 137 — need smaller tolerance")

    # ── Part 4: Compare 3D vs 4D ──
    # Build a 3D diamond lattice for comparison
    print("\n── Part 4: 3D diamond comparison ──")
    jack_dirs = np.array([
        [+1, +1, +1],
        [+1, -1, -1],
        [-1, +1, -1],
        [-1, -1, +1],
    ], dtype=float) / np.sqrt(3)

    # Build 3D diamond lattice by BFS
    def build_3d_diamond(depth=8):
        tolerance_3d = 0.01
        def key3(pt):
            return tuple(np.round(pt / tolerance_3d).astype(int))

        nodes_a_3d = {key3(np.zeros(3)): np.zeros(3)}
        nodes_b_3d = {}
        frontier = [np.zeros(3)]
        is_a = True

        for step in range(depth):
            new_frontier = []
            if is_a:
                for node in frontier:
                    for ev in jack_dirs:
                        new_pt = node + ev
                        k = key3(new_pt)
                        if k not in nodes_b_3d:
                            nodes_b_3d[k] = new_pt
                            new_frontier.append(new_pt)
            else:
                for node in frontier:
                    for ev in jack_dirs:
                        new_pt = node - ev
                        k = key3(new_pt)
                        if k not in nodes_a_3d:
                            nodes_a_3d[k] = new_pt
                            new_frontier.append(new_pt)
            frontier = new_frontier
            is_a = not is_a

        a3 = np.array(list(nodes_a_3d.values()))
        b3 = np.array(list(nodes_b_3d.values()))
        return np.vstack([a3, b3])

    nodes_3d = build_3d_diamond(depth=14)
    print(f"  3D diamond: {len(nodes_3d)} nodes")

    center_3d = nodes_3d.mean(axis=0)
    radii_3d = np.linalg.norm(nodes_3d - center_3d, axis=1)
    R_cut_3d = np.percentile(radii_3d, 60)
    core_3d = nodes_3d[radii_3d < R_cut_3d]
    tree_3d = cKDTree(core_3d)

    # 2D hex embedded in 3D at random orientations
    hex_2d_small = hex_lattice_2d(n_rings=n_rings)
    n_orient3 = 200

    print(f"\n  Comparing 3D vs 4D at matched tolerances:")
    print(f"  {'tol':>6s}  {'3D 1/frac':>10s}  {'4D 1/frac':>10s}  {'ratio':>8s}")
    print("  " + "─" * 40)

    for tol in [0.05, 0.10, 0.15, 0.20, 0.30]:
        # 3D
        fracs_3d = []
        for _ in range(n_orient3):
            # Random 2-plane in 3D (random normal direction)
            n_vec = np.random.randn(3)
            n_vec /= np.linalg.norm(n_vec)
            # Build orthonormal basis in the plane
            if abs(n_vec[0]) < 0.9:
                u = np.cross(n_vec, [1, 0, 0])
            else:
                u = np.cross(n_vec, [0, 1, 0])
            u /= np.linalg.norm(u)
            v = np.cross(n_vec, u)

            hex_3d = center_3d + hex_2d_small[:, 0:1] * u + hex_2d_small[:, 1:2] * v
            hex_r = np.linalg.norm(hex_3d - center_3d, axis=1)
            hex_m = hex_r < R_cut_3d * 0.8
            if hex_m.sum() < 10:
                continue
            n_h, f = count_coincidences(hex_3d[hex_m], tree_3d, tol)
            fracs_3d.append(f)

        # 4D (reuse existing results if available, else compute)
        fracs_4d = []
        for _ in range(n_orient3):
            e1, e2 = random_2plane()
            hex_4d = embed_hex_in_4d(hex_2d, e1, e2, origin=center)
            hex_radii = np.linalg.norm(hex_4d - center, axis=1)
            hex_mask = hex_radii < R_cut * 0.8
            if hex_mask.sum() < 10:
                continue
            hex_core = hex_4d[hex_mask]
            n_h, f = count_coincidences(hex_core, core_tree, tol)
            fracs_4d.append(f)

        m3 = np.mean(fracs_3d) if fracs_3d else 0
        m4 = np.mean(fracs_4d) if fracs_4d else 0
        inv3 = 1/m3 if m3 > 0 else float('inf')
        inv4 = 1/m4 if m4 > 0 else float('inf')
        ratio = inv4 / inv3 if inv3 > 0 and inv3 != float('inf') else 0
        print(f"  {tol:6.2f}  {inv3:10.1f}  {inv4:10.1f}  {ratio:8.2f}x")

    # ── Part 5: Orientation dependence ──
    print("\n── Part 5: Orientation dependence (is coupling constant?) ──")
    tol_test = 0.15
    fracs_all = []
    for _ in range(1000):
        e1, e2 = random_2plane()
        hex_4d = embed_hex_in_4d(hex_2d, e1, e2, origin=center)
        hex_radii = np.linalg.norm(hex_4d - center, axis=1)
        hex_mask = hex_radii < R_cut * 0.8
        if hex_mask.sum() < 10:
            continue
        hex_core = hex_4d[hex_mask]
        n_h, f = count_coincidences(hex_core, core_tree, tol_test)
        fracs_all.append(f)

    fracs_all = np.array(fracs_all)
    print(f"  tol={tol_test}, {len(fracs_all)} orientations:")
    print(f"    mean = {fracs_all.mean():.6f}")
    print(f"    std  = {fracs_all.std():.6f}")
    print(f"    CV   = {fracs_all.std()/fracs_all.mean():.4f}" if fracs_all.mean() > 0 else "")
    print(f"    min  = {fracs_all.min():.6f}")
    print(f"    max  = {fracs_all.max():.6f}")
    print(f"    1/mean = {1/fracs_all.mean():.1f}" if fracs_all.mean() > 0 else "")

    # ── Plot ──
    print("\n── Generating plots ──")

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Plot 1: Tolerance scaling
    ax = axes[0]
    ax.plot(fine_tols, 1.0/np.where(tol_means > 0, tol_means, 1e-30),
            'bo-', markersize=5)
    ax.axhline(137.036, color='red', linestyle='--', linewidth=1,
               label='1/α = 137.036')
    ax.set_xlabel('Tolerance δ')
    ax.set_ylabel('1 / coincidence fraction')
    ax.set_title('4D: Coincidence fraction vs tolerance')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_yscale('log')

    # Plot 2: Histogram of fractions at fixed tolerance
    ax = axes[1]
    if len(fracs_all) > 0:
        ax.hist(fracs_all, bins=30, edgecolor='black', alpha=0.7)
        ax.axvline(1/137.036, color='red', linestyle='--', linewidth=1,
                   label=f'1/137 = {1/137.036:.5f}')
        ax.set_xlabel('Coincidence fraction')
        ax.set_ylabel('Count')
        ax.set_title(f'4D: Fraction distribution (tol={tol_test})')
        ax.legend()

    # Plot 3: Fraction vs tolerance (linear)
    ax = axes[2]
    ax.plot(fine_tols, tol_means, 'go-', markersize=5)
    ax.axhline(1/137.036, color='red', linestyle='--', linewidth=1,
               label='α = 1/137')
    ax.set_xlabel('Tolerance δ')
    ax.set_ylabel('Mean coincidence fraction')
    ax.set_title('4D: Mean fraction vs tolerance')
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.suptitle('Track 6 Step 0: Euclidean 4D node coincidence', fontsize=14)
    fig.tight_layout()
    fig.savefig(OUT / "track6_step0_4d_coincidence.png", dpi=150)
    plt.close(fig)
    print(f"  Saved: {OUT / 'track6_step0_4d_coincidence.png'}")

    # ── Summary ──
    print("\n" + "=" * 60)
    print("  SUMMARY: Track 6 Step 0")
    print("=" * 60)
    print(f"\n  4D simplex lattice: {len(all_nodes)} nodes")
    print(f"  2D hex lattice: {len(hex_2d)} nodes")
    print(f"  Simplex angle: 104.48° (arccos(-1/4))")
    print(f"  Reference: 1/α = 137.036")
    print(f"\n  Tolerance scaling (mean 1/fraction):")
    for i, tol in enumerate(fine_tols):
        inv = 1/tol_means[i] if tol_means[i] > 0 else float('inf')
        marker = " ◄ near 137" if abs(inv - 137) < 30 else ""
        print(f"    δ={tol:.3f}  →  1/f = {inv:.1f}{marker}")
    print(f"\n  Orientation dependence at δ={tol_test}:")
    print(f"    CV = {fracs_all.std()/fracs_all.mean():.4f}" if fracs_all.mean() > 0 else "    No data")
    print(f"    (CV ≈ 0 means coupling is constant across orientations)")

    # Save data
    with open(OUT / "track6_step0_results.txt", "w") as f:
        f.write("Track 6 Step 0: Euclidean 4D node coincidence\n\n")
        f.write(f"4D lattice: {len(all_nodes)} nodes\n")
        f.write(f"2D hex: {len(hex_2d)} nodes, n_rings={n_rings}\n\n")
        f.write("Tolerance scaling:\n")
        f.write(f"{'tol':>8s}  {'mean_frac':>12s}  {'1/frac':>10s}\n")
        for i, tol in enumerate(fine_tols):
            inv = 1/tol_means[i] if tol_means[i] > 0 else float('inf')
            f.write(f"{tol:8.3f}  {tol_means[i]:12.6f}  {inv:10.1f}\n")
        f.write(f"\nOrientation distribution at tol={tol_test}:\n")
        f.write(f"  mean={fracs_all.mean():.6f}\n")
        f.write(f"  std={fracs_all.std():.6f}\n")
        f.write(f"  CV={fracs_all.std()/fracs_all.mean():.4f}\n" if fracs_all.mean() > 0 else "")

    print(f"\n  Results saved to {OUT / 'track6_step0_results.txt'}")


if __name__ == "__main__":
    main()
