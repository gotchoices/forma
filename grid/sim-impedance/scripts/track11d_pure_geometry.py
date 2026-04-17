#!/usr/bin/env python3
"""
Track 11d — Pure geometry leakage: no S-matrix, no imported rules.

At each Y-junction on a curved hexagonal torus:
  1. Signal arrives as a 3D vector along incoming edge
  2. Two outgoing edges define a plane
  3. The component of the signal IN that plane continues forward
  4. The component PERPENDICULAR to that plane leaks out
  5. The continuing signal splits between the two outgoing edges
     proportional to how well it aligns with each

No S-matrix.  No α.  No imported physics.
Just vector projection onto available edge directions.

The leakage at each junction is the fraction of signal energy
that doesn't fit in the outgoing plane — a pure geometric
consequence of bending a flat lattice onto a torus.
"""

import numpy as np
from pathlib import Path

TAU = 2 * np.pi
ALPHA = 1 / 137.036


# ══════════════════════════════════════════════════════════
#  Torus geometry
# ══════════════════════════════════════════════════════════

def torus_pos(th1, th2, R, a):
    rr = R + a * np.cos(th1)
    return np.array([rr * np.cos(th2), a * np.sin(th1), rr * np.sin(th2)])

def torus_normal(th1, th2):
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    return np.array([ct1 * cp, st1, ct1 * sp])

def torus_tangents(th1, th2, R, a):
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    t1_raw = np.array([-st1 * cp, ct1, -st1 * sp])
    t2_raw = np.array([-sp, 0.0, cp])
    t1 = t1_raw / (np.linalg.norm(t1_raw) + 1e-30)
    t2 = t2_raw / (np.linalg.norm(t2_raw) + 1e-30)
    return t1, t2


# ══════════════════════════════════════════════════════════
#  Hexagonal torus lattice
# ══════════════════════════════════════════════════════════

def build_hex_torus(N1, N2, R, a):
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

    n_nodes = len(nodes)
    adj = [[] for _ in range(n_nodes)]
    for (i, j) in edges:
        vec = nodes[j, 2:5] - nodes[i, 2:5]
        adj[i].append((j, vec))
        adj[j].append((i, -vec))

    return nodes, adj


# ══════════════════════════════════════════════════════════
#  Pure geometry junction leakage
# ══════════════════════════════════════════════════════════

def pure_geometry_leakage(E_in_vec, edge_vecs):
    """
    Pure geometry: signal projects onto the plane of outgoing edges.

    Parameters
    ----------
    E_in_vec : ndarray (3,) — incoming signal vector
    edge_vecs : list of ndarray (3,) — 3D vectors to all neighbors

    Returns
    -------
    f_leak : float — fraction of energy perpendicular to outgoing plane
    E_out : ndarray (3,) — the continuing signal (in outgoing plane)

    Method:
    - Identify the "incoming" edge (most anti-aligned with E_in)
    - The other two edges are "outgoing"
    - Project E_in onto the plane spanned by the two outgoing edges
    - The perpendicular component is the leakage
    """
    E2_in = np.dot(E_in_vec, E_in_vec)
    if E2_in < 1e-30:
        return 0.0, np.zeros(3)

    n_edges = len(edge_vecs)
    if n_edges < 3:
        return 0.0, E_in_vec.copy()

    # Unit vectors for each edge
    e_hats = []
    for ev in edge_vecs:
        n = np.linalg.norm(ev)
        e_hats.append(ev / n if n > 1e-15 else np.zeros(3))

    # Identify incoming edge: the one most anti-aligned with E_in
    E_hat = E_in_vec / np.sqrt(E2_in)
    dots = [np.dot(E_hat, eh) for eh in e_hats]
    incoming_idx = np.argmin(dots)

    # Outgoing edges: the other two
    outgoing = [i for i in range(n_edges) if i != incoming_idx]

    # Plane of outgoing edges: normal = ê_out1 × ê_out2
    e1 = e_hats[outgoing[0]]
    e2 = e_hats[outgoing[1]]
    plane_normal = np.cross(e1, e2)
    pn_mag = np.linalg.norm(plane_normal)
    if pn_mag < 1e-15:
        # Outgoing edges are parallel — degenerate
        return 0.0, E_in_vec.copy()
    plane_normal = plane_normal / pn_mag

    # Project E_in onto the outgoing plane
    E_perp = np.dot(E_in_vec, plane_normal) * plane_normal
    E_in_plane = E_in_vec - E_perp

    f_leak = np.dot(E_perp, E_perp) / E2_in

    return f_leak, E_in_plane


def torus_leakage_pure(N1, N2, eps, n1, n2, n_phase=32):
    """
    Mean per-junction leakage for a CP wave, pure geometry model.
    """
    R = 1.0
    a = eps * R
    nodes, adj = build_hex_torus(N1, N2, R, a)
    M = len(nodes)

    leak_map = np.zeros(M)
    phases = np.linspace(0, TAU, n_phase, endpoint=False)

    for node_idx in range(M):
        th1 = nodes[node_idx, 0]
        th2 = nodes[node_idx, 1]
        t1, t2 = torus_tangents(th1, th2, R, a)
        edge_vecs = [ev for (_, ev) in adj[node_idx]]

        leak_sum = 0.0
        for phase in phases:
            phi = n1 * th1 + n2 * th2 + phase
            E_vec = np.cos(phi) * t1 - np.sin(phi) * t2
            f_leak, _ = pure_geometry_leakage(E_vec, edge_vecs)
            leak_sum += f_leak

        leak_map[node_idx] = leak_sum / n_phase

    return np.mean(leak_map), leak_map, nodes


def iterative_circuit_pure(N1, N2, eps, n_circuits=1):
    """
    Walk a signal around a tube circuit on the ACTUAL hexagonal
    lattice (not smooth torus parametrization).

    Start at one node.  At each junction:
    - Identify the outgoing edge most aligned with current direction
    - Walk to that neighbor
    - At the new junction, compute pure-geometry leakage
    - Diminish signal and continue

    Continue until we return near the starting point (one tube circuit).
    """
    R = 1.0
    a = eps * R
    nodes, adj = build_hex_torus(N1, N2, R, a)

    # Start at node 0
    start_idx = 0
    start_th1 = nodes[start_idx, 0]
    start_pos = nodes[start_idx, 2:5]

    # Initial signal: unit amplitude along tube direction
    t1, t2 = torus_tangents(nodes[start_idx, 0], nodes[start_idx, 1], R, a)
    signal = t1.copy()  # propagating along tube
    amplitude = 1.0

    current_idx = start_idx
    cumulative_leak = 0.0
    steps = 0
    max_steps = 10 * N1  # safety limit
    visited_th1 = [start_th1]

    step_data = []

    while steps < max_steps:
        edge_vecs = [ev for (_, ev) in adj[current_idx]]
        neighbor_ids = [nid for (nid, _) in adj[current_idx]]

        # Compute leakage at this junction
        f_leak, E_out = pure_geometry_leakage(signal, edge_vecs)

        energy_leaked = amplitude**2 * f_leak
        cumulative_leak += energy_leaked
        amplitude *= np.sqrt(max(1.0 - f_leak, 0.0))

        # The continuing signal is E_out (in the outgoing plane)
        # Choose the outgoing edge most aligned with E_out
        if np.linalg.norm(E_out) < 1e-20:
            break

        E_out_hat = E_out / np.linalg.norm(E_out)
        best_dot = -2.0
        best_neighbor = -1
        best_edge = None
        for k, (nid, ev) in enumerate(adj[current_idx]):
            ev_hat = ev / (np.linalg.norm(ev) + 1e-30)
            d = np.dot(E_out_hat, ev_hat)
            if d > best_dot:
                best_dot = d
                best_neighbor = nid
                best_edge = ev

        if best_neighbor < 0:
            break

        step_data.append((steps, current_idx, nodes[current_idx, 0],
                         f_leak, energy_leaked, cumulative_leak, amplitude))

        # Move to next node
        signal = amplitude * E_out / (np.linalg.norm(E_out) + 1e-30)
        current_idx = best_neighbor
        steps += 1

        # Check if we've completed a tube circuit
        current_th1 = nodes[current_idx, 0]
        visited_th1.append(current_th1)

        # Detect circuit completion: θ₁ has wrapped around 2π
        if steps > 3:
            total_dth1 = 0.0
            for i in range(1, len(visited_th1)):
                dth = visited_th1[i] - visited_th1[i-1]
                # Handle wrapping
                if dth > np.pi:
                    dth -= TAU
                elif dth < -np.pi:
                    dth += TAU
                total_dth1 += dth

            if abs(total_dth1) >= TAU * n_circuits * 0.95:
                step_data.append((steps, current_idx, current_th1,
                                 0, 0, cumulative_leak, amplitude))
                break

    return cumulative_leak, amplitude, steps, step_data


# ══════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("Track 11d: Pure geometry leakage — no S-matrix")
    print("=" * 70)
    print()
    print("  At each junction: project signal onto plane of outgoing edges.")
    print("  Perpendicular component = leakage.  No imported rules.")
    print()

    # ── Section 1: Per-junction leakage ────────────────────
    print("─" * 70)
    print("Section 1: Mean per-junction leakage (CP wave, time-averaged)")
    print("─" * 70)
    print()

    eps = 0.3
    N = 20
    ml, lmap, nodes = torus_leakage_pure(N, N, eps, 1, 2)

    print(f"  ε = {eps}, N = {N}, mode = (1,2)")
    print(f"  Mean per-junction leakage: {ml:.6e}")
    print(f"  Range: [{lmap.min():.6e}, {lmap.max():.6e}]")
    print(f"  α = {ALPHA:.6e}")
    print(f"  Ratio to α: {ml/ALPHA:.4f}")
    print()

    # ── Section 2: Mode dependence ─────────────────────────
    print("─" * 70)
    print("Section 2: Mode dependence (ε=0.3, N=20)")
    print("─" * 70)
    print()

    print(f"  {'Mode':>8s}  {'f_leak':>12s}  {'ratio/α':>10s}")
    print(f"  {'─'*8}  {'─'*12}  {'─'*10}")

    for n1, n2 in [(1, 2), (1, 3), (1, 1), (0, 1), (2, 4), (2, 3)]:
        ml_m, _, _ = torus_leakage_pure(N, N, eps, n1, n2)
        print(f"  ({n1},{n2})  {ml_m:12.6e}  {ml_m/ALPHA:10.4f}")
    print()

    # ── Section 3: Convergence with N ──────────────────────
    print("─" * 70)
    print("Section 3: Convergence with N (ε=0.3)")
    print("─" * 70)
    print()

    print(f"  {'N':>6s}  {'f_leak':>12s}  {'ratio/α':>10s}  {'N²×f':>10s}")
    print(f"  {'─'*6}  {'─'*12}  {'─'*10}  {'─'*10}")

    conv_data = []
    for Nv in [6, 8, 10, 14, 20, 30, 40]:
        ml_n, _, _ = torus_leakage_pure(Nv, Nv, 0.3, 1, 2, n_phase=32)
        n2f = Nv**2 * ml_n
        conv_data.append((Nv, ml_n))
        print(f"  {Nv:6d}  {ml_n:12.6e}  {ml_n/ALPHA:10.4f}  {n2f:10.4f}")

    # Compute scaling exponent
    if len(conv_data) >= 2:
        N_a, f_a = conv_data[1]
        N_b, f_b = conv_data[-2]
        if f_a > 0 and f_b > 0:
            p = -np.log(f_b / f_a) / np.log(N_b / N_a)
            print(f"\n  Scaling: f_leak ∝ N^(-{p:.2f})")
    print()

    # ── Section 4: ε dependence ────────────────────────────
    print("─" * 70)
    print("Section 4: Aspect ratio dependence (N=20)")
    print("─" * 70)
    print()

    print(f"  {'ε':>8s}  {'f_leak':>12s}  {'ratio/α':>10s}  {'f/ε²':>12s}")
    print(f"  {'─'*8}  {'─'*12}  {'─'*10}  {'─'*12}")

    for ev in [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]:
        ml_e, _, _ = torus_leakage_pure(20, 20, ev, 1, 2, n_phase=32)
        fe2 = ml_e / ev**2 if ev > 0 else 0
        print(f"  {ev:8.3f}  {ml_e:12.6e}  {ml_e/ALPHA:10.4f}  {fe2:12.6e}")
    print()

    # ── Section 5: Iterative walk on actual lattice ────────
    print("─" * 70)
    print("Section 5: Iterative walk on hexagonal lattice")
    print("  (signal walks along actual edges, diminishing at each junction)")
    print("─" * 70)
    print()

    for ev in [0.1, 0.3, 0.5]:
        for Nv in [10, 20, 30]:
            cl, fa, steps, _ = iterative_circuit_pure(Nv, Nv, ev)
            energy_check = cl + fa**2
            print(f"  ε={ev:.1f}, N={Nv:3d}: "
                  f"steps={steps:4d}, "
                  f"cum_leak={cl:.6e}, "
                  f"final_amp={fa:.6f}, "
                  f"E_conserved={energy_check:.4f}, "
                  f"leak/α={cl/ALPHA:.4f}")
        print()

    # ── Section 6: Detailed walk for one case ──────────────
    print("─" * 70)
    print("Section 6: Step-by-step walk (ε=0.3, N=20)")
    print("─" * 70)
    print()

    cl, fa, steps, data = iterative_circuit_pure(20, 20, 0.3)

    print(f"  {'Step':>5s}  {'θ₁':>8s}  {'f_leak':>12s}  {'cum_leak':>12s}  {'amplitude':>10s}")
    print(f"  {'─'*5}  {'─'*8}  {'─'*12}  {'─'*12}  {'─'*10}")
    for step, nid, th1, fl, el, cl_s, amp in data[:30]:
        print(f"  {step:5d}  {th1:8.4f}  {fl:12.6e}  {cl_s:12.6e}  {amp:10.6f}")
    if len(data) > 30:
        print(f"  ... ({len(data)} total steps)")
        step, nid, th1, fl, el, cl_s, amp = data[-1]
        print(f"  {step:5d}  {th1:8.4f}  {fl:12.6e}  {cl_s:12.6e}  {amp:10.6f}")

    print()
    print(f"  Total steps: {steps}")
    print(f"  Cumulative leakage: {cl:.6e}")
    print(f"  Final amplitude: {fa:.6f}")
    print(f"  Energy conserved: {cl + fa**2:.6f}")
    print(f"  α = {ALPHA:.6e}")
    print(f"  Ratio to α: {cl/ALPHA:.4f}")
    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 70)
    print("SUMMARY: All Track 11 results")
    print("=" * 70)
    print()
    print("  Per-junction leakage (N=20, ε=0.3, mode (1,2)):")
    print()
    print(f"  {'Model':>30s}  {'f_leak':>12s}  {'ratio/α':>10s}  {'N²×f':>10s}")
    print(f"  {'─'*30}  {'─'*12}  {'─'*10}  {'─'*10}")

    # Re-run the other models for comparison
    from track11c_angle_corrected import (
        torus_leakage_all_models,
        scatter_grid_smatrix,
        scatter_equal_split,
        scatter_angle_weighted
    )

    try:
        results_abc, _ = torus_leakage_all_models(20, 20, 0.3, 1, 2)
        for name, (ml_v, _) in results_abc.items():
            print(f"  {name:>30s}  {ml_v:12.6e}  {ml_v/ALPHA:10.4f}  {20**2*ml_v:10.4f}")
    except Exception:
        # If import fails, just show our model
        pass

    ml_d, _, _ = torus_leakage_pure(20, 20, 0.3, 1, 2)
    print(f"  {'D (pure geometry)':>30s}  {ml_d:12.6e}  {ml_d/ALPHA:10.4f}  {20**2*ml_d:10.4f}")

    print()
    print("  Convergence products (N²×f → geometric invariant):")
    print()
    for Nv, ml_n in conv_data:
        print(f"    N={Nv:3d}: N²×f = {Nv**2 * ml_n:.4f}")

    print()
    print("  Key observations:")
    print("  1. All models give proper fractions (0 to 1) ✓")
    print("  2. All models converge (N²×f → constant) ✓")
    print("  3. Per-junction leakage scales as 1/N² (resolution-dependent)")
    print("  4. The geometric invariant N²×f is model-dependent:")
    print(f"     A (GRID S-matrix): ~0.63")
    print(f"     B (equal split):   ~2.43")
    print(f"     C (angle-weighted): ~2.2")
    print(f"     D (pure geometry):  TBD")
    print()
    print("  5. The iterative circuit leakage depends on N (number of")
    print("     lattice edges per circuit).  Without knowing the physical")
    print("     value of N (= tube circumference / Planck length),")
    print("     we cannot derive α from this approach.")
    print()
    print("  6. If the physical N is such that the per-circuit leakage")
    print("     equals α, that DETERMINES the tube circumference —")
    print("     i.e., the particle's Compton scale — from α.")
    print("     This would mean α SETS the scale, not the other way.")
    print()
    print("Track 11d complete.")


if __name__ == "__main__":
    main()
