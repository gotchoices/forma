#!/usr/bin/env python3
"""
Track 11 — Vector energy deficit at curved Y-junctions.

At each Y-junction on a curved hexagonal torus:
1. The CP field E arrives as a 3D vector along one edge
2. The S-matrix distributes scalar amplitude: 2/3 to each
   forward edge, -1/3 reflected
3. The outgoing amplitudes ride on 3D edge vectors that are
   non-coplanar due to curvature
4. The reconstructed outgoing vector differs from the input
5. The deficit (normal component of the reconstruction) is
   the energy that "doesn't fit" on the curved surface

Key: the S-matrix weights (2/3, -1/3) involve NO α.
The edge directions are pure geometry.  The deficit is
α-free and parameter-free.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "output"
OUT.mkdir(exist_ok=True)

TAU = 2 * np.pi
ALPHA = 1 / 137.036


# ══════════════════════════════════════════════════════════
#  Torus geometry
# ══════════════════════════════════════════════════════════

def torus_pos(th1, th2, R, a):
    """3D position on a torus."""
    rr = R + a * np.cos(th1)
    return np.array([rr * np.cos(th2), a * np.sin(th1), rr * np.sin(th2)])


def torus_tangents(th1, th2, R, a):
    """Unit tangent vectors t1 (tube), t2 (ring), surface normal, and rho-hat."""
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    # Unnormalized tangents
    t1_raw = np.array([-st1 * cp, ct1, -st1 * sp])  # d/dθ₁, length a
    t2_raw = np.array([-sp, 0.0, cp])                # d/dθ₂, length R+a cos θ₁
    n_hat = np.array([ct1 * cp, st1, ct1 * sp])      # outward surface normal
    rho_hat = np.array([cp, 0.0, sp])                 # cylindrical radial
    # Normalize tangents
    t1 = t1_raw / (np.linalg.norm(t1_raw) + 1e-30)
    t2 = t2_raw / (np.linalg.norm(t2_raw) + 1e-30)
    return t1, t2, n_hat, rho_hat


# ══════════════════════════════════════════════════════════
#  Hexagonal torus lattice
# ══════════════════════════════════════════════════════════

def build_hex_torus(N1, N2, R, a):
    """
    Honeycomb lattice on a torus.
    Returns (nodes, adjacency).
    nodes: (M, 5) array — [θ₁, θ₂, x, y, z]
    adj: list of lists — adj[i] = [(neighbor_idx, edge_vec), ...]
    """
    nodes = []
    node_map = {}
    for i1 in range(N1):
        for i2 in range(N2):
            for sub in range(2):
                th1 = TAU * (i1 + 0.25 * sub) / N1
                th2 = TAU * (i2 + 0.5 * sub) / N2
                idx = len(nodes)
                node_map[(i1, i2, sub)] = idx
                pos = torus_pos(th1, th2, R, a)
                nodes.append([th1, th2, pos[0], pos[1], pos[2]])
    nodes = np.array(nodes)

    # Build edge list
    edges = []
    for i1 in range(N1):
        for i2 in range(N2):
            a_idx = node_map[(i1, i2, 0)]
            b_idx = node_map[(i1, i2, 1)]
            edges.append((a_idx, b_idx))
            i1_next = (i1 + 1) % N1
            i2_next = (i2 + 1) % N2
            edges.append((b_idx, node_map[(i1_next, i2, 0)]))
            edges.append((b_idx, node_map[(i1, i2_next, 0)]))

    # Build adjacency with edge vectors
    n_nodes = len(nodes)
    adj = [[] for _ in range(n_nodes)]
    for (i, j) in edges:
        vec_ij = nodes[j, 2:5] - nodes[i, 2:5]
        vec_ji = -vec_ij
        adj[i].append((j, vec_ij))
        adj[j].append((i, vec_ji))

    return nodes, adj


# ══════════════════════════════════════════════════════════
#  Core computation: vector energy deficit at each junction
# ══════════════════════════════════════════════════════════

def vector_deficit_at_node(E_vec, edge_vecs):
    """
    Compute the vector energy deficit at one Y-junction.

    Parameters
    ----------
    E_vec : ndarray (3,) — incoming CP field vector (3D)
    edge_vecs : list of ndarray (3,) — 3D vectors to neighbors

    Returns
    -------
    deficit_n : float — normal component of reconstruction error
    deficit_rho : float — ρ̂ component of reconstruction error
    E2_in : float — incoming energy
    E2_out : float — reconstructed outgoing energy
    """
    n_edges = len(edge_vecs)
    if n_edges < 2:
        return 0.0, 0.0, 0.0, 0.0

    # Normalize edge vectors
    e_hats = []
    for ev in edge_vecs:
        norm = np.linalg.norm(ev)
        if norm < 1e-15:
            e_hats.append(np.zeros(3))
        else:
            e_hats.append(ev / norm)

    # Project incoming field onto each edge
    projections = [np.dot(E_vec, eh) for eh in e_hats]

    # S-matrix scattering: for N edges,
    #   S_ii = 2/N - 1,  S_ij = 2/N
    # For N=3: reflect = -1/3, transmit = 2/3
    N = n_edges
    S_diag = 2.0 / N - 1.0   # -1/3 for N=3
    S_off = 2.0 / N           # 2/3 for N=3

    # Outgoing amplitude on each edge:
    #   b_i = S_ii * a_i + S_off * Σ_{j≠i} a_j
    #       = S_diag * a_i + S_off * (Σ_all a_j - a_i)
    #       = S_diag * a_i + S_off * (total - a_i)
    #       = (S_diag - S_off) * a_i + S_off * total
    total_proj = sum(projections)
    outgoing = []
    for i in range(N):
        b_i = (S_diag - S_off) * projections[i] + S_off * total_proj
        outgoing.append(b_i)

    # Reconstruct the outgoing 3D vector
    V_recon = sum(b * eh for b, eh in zip(outgoing, e_hats))

    # Energy comparison
    E2_in = np.dot(E_vec, E_vec)
    E2_out = np.dot(V_recon, V_recon)

    # Deficit vector = V_recon - E_vec (the error)
    deficit_vec = V_recon - E_vec

    return np.dot(deficit_vec, deficit_vec), E2_in, E2_out, deficit_vec


def compute_deficit_map(N1, N2, eps, n1, n2, n_phase=64):
    """
    Compute the time-averaged vector energy deficit at each
    junction for a CP wave (n1, n2) on a torus with ε = a/R.

    Time-averaging: sample n_phase values of the wave phase
    (equivalent to different instants) and average the deficit.

    Returns
    -------
    deficit_per_node : ndarray (M,) — time-averaged |deficit|²
    nodes : ndarray (M, 5)
    total_deficit : float — sum over all nodes (area-weighted)
    total_energy : float — sum of incoming energy (area-weighted)
    """
    R = 1.0
    a = eps * R
    nodes, adj = build_hex_torus(N1, N2, R, a)
    M = len(nodes)

    deficit_per_node = np.zeros(M)

    # Phase samples for time-averaging
    phases = np.linspace(0, TAU, n_phase, endpoint=False)

    for node_idx in range(M):
        th1 = nodes[node_idx, 0]
        th2 = nodes[node_idx, 1]

        t1, t2, n_hat, rho_hat = torus_tangents(th1, th2, R, a)
        edge_vecs = [ev for (_, ev) in adj[node_idx]]

        # Time-average over wave phase
        deficit_sum = 0.0
        energy_sum = 0.0

        for phase_offset in phases:
            phi = n1 * th1 + n2 * th2 + phase_offset
            E_vec = np.cos(phi) * t1 - np.sin(phi) * t2

            d2, E2_in, E2_out, dvec = vector_deficit_at_node(E_vec, edge_vecs)
            deficit_sum += d2
            energy_sum += E2_in

        deficit_per_node[node_idx] = deficit_sum / n_phase

    # Area weighting
    th1_all = nodes[:, 0]
    p = 1.0 + eps * np.cos(th1_all)
    dA = p / M * (TAU * a) * (TAU * R)

    total_deficit = np.sum(deficit_per_node * dA)
    total_energy = np.sum(dA)  # normalized wave has unit energy density

    return deficit_per_node, nodes, total_deficit, total_energy


# ══════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("Track 11: Vector energy deficit at curved Y-junctions")
    print("=" * 70)
    print()
    print("  The S-matrix weights (2/3, -1/3) contain NO α.")
    print("  The edge directions are pure torus geometry.")
    print("  The deficit is α-free and parameter-free.")
    print()

    # ── Section 1: Basic computation at fixed ε, N ─────────
    print("─" * 70)
    print("Section 1: Deficit for mode (1,2) at ε=0.3")
    print("─" * 70)
    print()

    eps = 0.3
    N = 20
    d_per_node, nodes, d_total, e_total = compute_deficit_map(N, N, eps, 1, 2)

    coupling = d_total / e_total
    print(f"  ε = {eps}, N = {N}, mode = (1,2)")
    print(f"  Total deficit (area-weighted): {d_total:.6f}")
    print(f"  Total energy (area-weighted):  {e_total:.6f}")
    print(f"  Coupling ratio (deficit/energy): {coupling:.6e}")
    print(f"  α = {ALPHA:.6e}")
    print(f"  Ratio to α: {coupling / ALPHA:.4f}")
    print()

    # ── Section 2: Mode dependence ─────────────────────────
    print("─" * 70)
    print("Section 2: Mode dependence (ε=0.3, N=20)")
    print("─" * 70)
    print()

    N = 20
    eps = 0.3
    print(f"  {'Mode':>8s}  {'deficit':>12s}  {'energy':>12s}  {'coupling':>12s}  {'ratio/α':>10s}")
    print(f"  {'─'*8}  {'─'*12}  {'─'*12}  {'─'*12}  {'─'*10}")

    for n1, n2 in [(1, 2), (1, 3), (1, 1), (0, 1), (2, 4), (1, 5), (2, 3)]:
        _, _, dt, et = compute_deficit_map(N, N, eps, n1, n2, n_phase=32)
        c = dt / et if et > 0 else 0
        r = c / ALPHA if ALPHA > 0 else 0
        print(f"  ({n1},{n2})  {dt:12.6f}  {et:12.6f}  {c:12.6e}  {r:10.4f}")

    print()

    # ── Section 3: Convergence with N ──────────────────────
    print("─" * 70)
    print("Section 3: Convergence with lattice resolution N")
    print("─" * 70)
    print()

    eps = 0.3
    print(f"  Mode (1,2), ε = {eps}")
    print(f"  {'N':>6s}  {'deficit':>12s}  {'energy':>12s}  {'coupling':>12s}  {'ratio/α':>10s}  {'N²×coupling':>12s}")
    print(f"  {'─'*6}  {'─'*12}  {'─'*12}  {'─'*12}  {'─'*10}  {'─'*12}")

    convergence_data = []
    for N in [6, 10, 14, 20, 30, 40]:
        _, _, dt, et = compute_deficit_map(N, N, eps, 1, 2, n_phase=32)
        c = dt / et if et > 0 else 0
        r = c / ALPHA
        n2c = N**2 * c
        convergence_data.append((N, c, r))
        print(f"  {N:6d}  {dt:12.6f}  {et:12.6f}  {c:12.6e}  {r:10.4f}  {n2c:12.4f}")

    print()

    # Check scaling: does coupling ~ 1/N^p for some p?
    if len(convergence_data) >= 2:
        N1_c, c1, _ = convergence_data[1]
        N2_c, c2, _ = convergence_data[-2]
        if c1 > 0 and c2 > 0:
            p = -np.log(c2 / c1) / np.log(N2_c / N1_c)
            print(f"  Scaling: coupling ∝ N^(-{p:.2f})")
            if abs(p) < 0.5:
                print(f"  → APPROXIMATELY CONVERGENT (weak N dependence)")
            elif p > 1.5:
                print(f"  → DECREASING toward zero (resolution-dependent)")
            else:
                print(f"  → MODERATE N dependence")
    print()

    # ── Section 4: ε dependence ───────���────────────────────
    print("─" * 70)
    print("Section 4: Aspect ratio dependence (N=20, mode (1,2))")
    print("─" * 70)
    print()

    N = 20
    print(f"  {'ε':>8s}  {'coupling':>12s}  {'ratio/α':>10s}  {'coupling/ε²':>12s}")
    print(f"  {'─'*8}  {'─'*12}  {'─'*10}  {'─'*12}")

    for eps in [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]:
        _, _, dt, et = compute_deficit_map(N, N, eps, 1, 2, n_phase=32)
        c = dt / et if et > 0 else 0
        r = c / ALPHA
        ce2 = c / eps**2 if eps > 0 else 0
        print(f"  {eps:8.3f}  {c:12.6e}  {r:10.4f}  {ce2:12.6e}")

    print()

    # ── Section 5: Standing vs traveling wave ──────────────
    print("─" * 70)
    print("Section 5: Standing wave check (should give ~zero deficit)")
    print("─" * 70)
    print()

    N = 20
    eps = 0.3

    # Standing wave: use cos(φ) instead of time-averaging a traveling wave
    # A standing wave has E = cos(n1 θ1) cos(n2 θ2) t1 - sin(n1 θ1) sin(n2 θ2) t2
    # The time-average of a traveling wave gives a definite deficit.
    # A standing wave should give a DIFFERENT deficit (possibly zero).
    # We test by using a single phase (no time averaging).

    _, _, dt_trav, et_trav = compute_deficit_map(N, N, eps, 1, 2, n_phase=32)
    _, _, dt_inst, et_inst = compute_deficit_map(N, N, eps, 1, 2, n_phase=1)

    c_trav = dt_trav / et_trav
    c_inst = dt_inst / et_inst

    print(f"  Traveling (time-averaged, 32 phases): coupling = {c_trav:.6e}")
    print(f"  Instantaneous (1 phase):              coupling = {c_inst:.6e}")
    print(f"  Ratio (traveling/instantaneous): {c_trav / c_inst:.4f}" if c_inst > 0 else "  (instantaneous = 0)")
    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 70)
    print("Track 11 Summary")
    print("=" * 70)
    print()

    # Get the key number
    N_ref = 20
    eps_ref = 0.3
    _, _, dt_ref, et_ref = compute_deficit_map(N_ref, N_ref, eps_ref, 1, 2, n_phase=32)
    c_ref = dt_ref / et_ref
    r_ref = c_ref / ALPHA

    print(f"  At ε={eps_ref}, N={N_ref}, mode (1,2):")
    print(f"    Vector energy deficit coupling = {c_ref:.6e}")
    print(f"    α = {ALPHA:.6e}")
    print(f"    Ratio = {r_ref:.4f}")
    print()

    if abs(r_ref - 1.0) < 0.1:
        print(f"  *** CLOSE TO α ***")
    elif r_ref > 0.01 and r_ref < 100:
        print(f"  Same order of magnitude as α but not exact.")
    else:
        print(f"  Not close to α.")

    # Check convergence conclusion
    if len(convergence_data) >= 2:
        _, c_small, _ = convergence_data[0]
        _, c_large, _ = convergence_data[-1]
        if c_small > 0 and c_large > 0:
            ratio = c_large / c_small
            if ratio > 0.5 and ratio < 2.0:
                print(f"  Coupling is approximately N-independent (converged).")
            elif c_large < c_small:
                print(f"  Coupling DECREASES with N — resolution-dependent.")
            else:
                print(f"  Coupling INCREASES with N — unexpected.")

    print()
    print("Track 11 complete.")


if __name__ == "__main__":
    main()
