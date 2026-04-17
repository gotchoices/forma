#!/usr/bin/env python3
"""
Track 11b — Proper leakage fraction at curved Y-junctions.

Corrects Track 11a's errors:
1. Computes a proper FRACTION (0 to 1), not a norm
2. At each junction: unit signal arrives on one edge, scatters
   via S-matrix (2/3 forward, -1/3 reflect), outgoing rides
   on actual 3D edge vectors.  The fraction of outgoing energy
   that projects onto the surface NORMAL is the leakage.
3. Iterative: the signal arriving at the next junction is
   diminished by the scattering at the previous one.
4. Uses actual 3D edge directions (not 120° — curvature
   distorts the angles).

Physical picture:
  - A pulse enters one edge of the hexagonal torus
  - At junction 1: splits into 2 forward + 1 reflected
  - Each outgoing branch has amplitude riding on a 3D edge vector
  - The edge vector has a tangential part (stays in surface)
    and a normal part (leaks out)
  - The normal fraction at this junction = leakage
  - The tangential part continues to the next junction
  - At junction 2: the diminished signal scatters again
  - After a full circuit around the tube, total leakage
    accumulated is the coupling fraction
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
    rr = R + a * np.cos(th1)
    return np.array([rr * np.cos(th2), a * np.sin(th1), rr * np.sin(th2)])


def torus_normal(th1, th2):
    """Outward surface normal (unit vector)."""
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    return np.array([ct1 * cp, st1, ct1 * sp])


# ══════════════════════════════════════════════════════════
#  Hexagonal torus lattice
# ══════════════════════════════════════════════════════════

def build_hex_torus(N1, N2, R, a):
    """
    Honeycomb lattice on a torus.
    Returns (nodes, adj).
    nodes: (M, 5) array — [θ₁, θ₂, x, y, z]
    adj: list of lists — adj[i] = [(neighbor_idx, edge_vec_3d), ...]
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
        vec_ij = nodes[j, 2:5] - nodes[i, 2:5]
        vec_ji = -vec_ij
        adj[i].append((j, vec_ij))
        adj[j].append((i, vec_ji))

    return nodes, adj


# ══════════════════════════════════════════════════════════
#  Single junction leakage fraction
# ══════════════════════════════════════════════════════════

def junction_leakage(E_in_vec, edge_vecs, n_hat):
    """
    Compute leakage at one Y-junction for a vector signal.

    Parameters
    ----------
    E_in_vec : ndarray (3,) — incoming signal as 3D vector
    edge_vecs : list of ndarray (3,) — vectors to neighbors (raw, not unit)
    n_hat : ndarray (3,) — local surface normal (unit)

    Returns
    -------
    f_leak : float — fraction of incoming energy that goes to normal
    E_tang_out : float — tangential outgoing energy (what continues)
    E_total_in : float — incoming energy
    """
    E2_in = np.dot(E_in_vec, E_in_vec)
    if E2_in < 1e-30:
        return 0.0, 0.0, 0.0

    n_edges = len(edge_vecs)
    if n_edges < 2:
        return 0.0, 0.0, E2_in

    # Unit edge vectors
    e_hats = []
    for ev in edge_vecs:
        norm = np.linalg.norm(ev)
        if norm < 1e-15:
            e_hats.append(np.zeros(3))
        else:
            e_hats.append(ev / norm)

    # Project incoming signal onto each edge
    # (how much of the input aligns with each edge direction)
    a_in = [np.dot(E_in_vec, eh) for eh in e_hats]

    # S-matrix: for N=3 edges, S_ii = -1/3, S_ij = 2/3
    # Outgoing amplitude on edge i:
    #   b_i = -1/3 * a_i + 2/3 * (a_j + a_k)  for the other two edges
    N = n_edges
    S_refl = 2.0 / N - 1.0   # -1/3
    S_trans = 2.0 / N         # 2/3

    total_a = sum(a_in)
    b_out = []
    for i in range(N):
        b_i = S_refl * a_in[i] + S_trans * (total_a - a_in[i])
        b_out.append(b_i)

    # Reconstruct outgoing 3D vector
    V_out = np.zeros(3)
    for i in range(N):
        V_out += b_out[i] * e_hats[i]

    # Decompose outgoing into tangential and normal
    V_normal = np.dot(V_out, n_hat) * n_hat
    V_tangential = V_out - V_normal

    E2_normal = np.dot(V_normal, V_normal)
    E2_tangential = np.dot(V_tangential, V_tangential)
    E2_out_total = np.dot(V_out, V_out)

    # Leakage fraction = normal energy / input energy
    f_leak = E2_normal / E2_in

    return f_leak, E2_tangential, E2_in


# ══════════════════════════════════════════════════════════
#  Full torus computation: CP wave, time-averaged
# ══════════════════════════════════════════════════════════

def torus_leakage(N1, N2, eps, n1, n2, n_phase=32):
    """
    Compute the total leakage fraction for a CP wave on a torus.

    At each junction:
    - The CP field provides the local E vector
    - The junction scatters it via S-matrix onto the 3 edges
    - The normal component of the reconstructed output is leakage
    - Time-average over wave phases

    This is the PER-JUNCTION average leakage, which we then
    report as a fraction.

    Returns
    -------
    mean_leak : float — mean leakage fraction per junction
    total_leak : float — area-weighted total leakage
    total_energy : float — area-weighted total energy
    leak_map : ndarray — per-node leakage
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

        # Surface normal
        n_hat = torus_normal(th1, th2)

        # Tangent vectors (unnormalized)
        ct1, st1 = np.cos(th1), np.sin(th1)
        cp, sp = np.cos(th2), np.sin(th2)
        t1_raw = np.array([-st1 * cp, ct1, -st1 * sp])
        t2_raw = np.array([-sp, 0.0, cp])
        t1 = t1_raw / (np.linalg.norm(t1_raw) + 1e-30)
        t2 = t2_raw / (np.linalg.norm(t2_raw) + 1e-30)

        edge_vecs = [ev for (_, ev) in adj[node_idx]]

        # Time-average leakage
        leak_sum = 0.0
        for phase in phases:
            phi = n1 * th1 + n2 * th2 + phase
            E_vec = np.cos(phi) * t1 - np.sin(phi) * t2

            f_leak, _, _ = junction_leakage(E_vec, edge_vecs, n_hat)
            leak_sum += f_leak

        leak_map[node_idx] = leak_sum / n_phase

    # Area weighting
    th1_all = nodes[:, 0]
    p = 1.0 + eps * np.cos(th1_all)
    dA = p / M * (TAU * a) * (TAU * R)

    total_leak = np.sum(leak_map * dA)
    total_energy = np.sum(dA)
    mean_leak = np.mean(leak_map)

    return mean_leak, total_leak, total_energy, leak_map, nodes


# ══════════════════════════════════════════════════════════
#  Iterative propagation: diminished signal at each step
# ══════════════════════════════════════════════════════════

def iterative_tube_circuit(N1, eps, n_steps=None):
    """
    Propagate a signal around one tube circuit (θ₁ direction).

    At each junction along the tube:
    - Input signal amplitude (starts at 1.0)
    - Scatter via S-matrix: 2/3 forward, -1/3 back
    - Normal component leaks out
    - Tangential component continues (diminished)
    - Next junction receives the diminished signal

    Track cumulative leakage after a full circuit.

    This is a 1D chain of junctions around the tube, at fixed θ₂.
    """
    R = 1.0
    a = eps * R
    if n_steps is None:
        n_steps = N1  # one full tube circuit

    # Junctions equally spaced around the tube
    theta1_vals = np.linspace(0, TAU, n_steps, endpoint=False)
    th2 = 0.0  # fixed azimuthal position

    amplitude = 1.0  # signal energy (starts at unity)
    cumulative_leak = 0.0
    step_data = []

    for i, th1 in enumerate(theta1_vals):
        # Surface normal at this point
        n_hat = torus_normal(th1, th2)

        # Tangent vectors
        ct1, st1 = np.cos(th1), np.sin(th1)
        cp, sp = np.cos(th2), np.sin(th2)
        t1_raw = np.array([-st1 * cp, ct1, -st1 * sp])
        t1 = t1_raw / (np.linalg.norm(t1_raw) + 1e-30)

        # The signal propagates along the tube direction (t1)
        E_in = amplitude * t1

        # Next junction: edges point in slightly different directions
        # due to curvature.  The angular deviation is Δθ₁ = 2π/N1
        dth = TAU / n_steps
        th1_next = th1 + dth

        # Edge to next node (approximate: follows the tube)
        pos_here = torus_pos(th1, th2, R, a)
        pos_next = torus_pos(th1_next, th2, R, a)
        edge_fwd = pos_next - pos_here
        edge_fwd_hat = edge_fwd / (np.linalg.norm(edge_fwd) + 1e-30)

        # Edge backward
        th1_prev = th1 - dth
        pos_prev = torus_pos(th1_prev, th2, R, a)
        edge_back = pos_prev - pos_here
        edge_back_hat = edge_back / (np.linalg.norm(edge_back) + 1e-30)

        # Third edge: ring direction (perpendicular to tube on surface)
        t2_raw = np.array([-sp, 0.0, cp])
        t2 = t2_raw / (np.linalg.norm(t2_raw) + 1e-30)
        # Approximate ring-direction edge
        dth2 = TAU / n_steps
        pos_ring = torus_pos(th1, th2 + dth2, R, a)
        edge_ring = pos_ring - pos_here
        edge_ring_hat = edge_ring / (np.linalg.norm(edge_ring) + 1e-30)

        edges = [edge_back, edge_fwd, edge_ring]

        # Compute leakage at this junction
        f_leak, E2_tang, E2_in = junction_leakage(E_in, edges, n_hat)

        # The leaked fraction comes out of the signal
        energy_leaked = amplitude**2 * f_leak
        cumulative_leak += energy_leaked

        # Remaining amplitude (tangential) continues
        # amplitude² × (1 - f_leak) = remaining energy
        amplitude = amplitude * np.sqrt(max(1.0 - f_leak, 0.0))

        step_data.append((i, th1, f_leak, energy_leaked, cumulative_leak, amplitude))

    return cumulative_leak, amplitude, step_data


# ══════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("Track 11b: Proper leakage fraction at curved Y-junctions")
    print("=" * 70)
    print()
    print("  Leakage = normal component of reconstructed outgoing vector")
    print("  as a FRACTION of incoming energy (must be 0 to 1).")
    print()

    # ── Section 1: Per-junction leakage, CP wave ───────────
    print("─" * 70)
    print("Section 1: Mean per-junction leakage fraction")
    print("─" * 70)
    print()

    eps = 0.3
    N = 20
    mean_leak, t_leak, t_energy, lmap, nodes = torus_leakage(N, N, eps, 1, 2)

    print(f"  ε = {eps}, N = {N}, mode = (1,2)")
    print(f"  Mean per-junction leakage fraction: {mean_leak:.6e}")
    print(f"  Min per-junction: {lmap.min():.6e}")
    print(f"  Max per-junction: {lmap.max():.6e}")
    print(f"  α = {ALPHA:.6e}")
    print(f"  Ratio to α: {mean_leak / ALPHA:.4f}")
    print()

    # ── Section 2: Mode dependence ─────────────────────────
    print("─" * 70)
    print("Section 2: Mode dependence (ε=0.3, N=20)")
    print("─" * 70)
    print()

    print(f"  {'Mode':>8s}  {'mean f_leak':>12s}  {'ratio/α':>10s}")
    print(f"  {'─'*8}  {'─'*12}  {'─'*10}")

    for n1, n2 in [(1, 2), (1, 3), (1, 1), (0, 1), (2, 4), (2, 3)]:
        ml, _, _, _, _ = torus_leakage(N, N, eps, n1, n2, n_phase=32)
        print(f"  ({n1},{n2})  {ml:12.6e}  {ml/ALPHA:10.4f}")

    print()

    # ── Section 3: Convergence with N ──────────────────────
    print("─" * 70)
    print("Section 3: Convergence with N (ε=0.3, mode (1,2))")
    print("─" * 70)
    print()

    print(f"  {'N':>6s}  {'mean f_leak':>12s}  {'ratio/α':>10s}  {'N²×f':>12s}")
    print(f"  {'─'*6}  {'─'*12}  {'─'*10}  {'─'*12}")

    for N in [6, 10, 14, 20, 30, 40]:
        ml, _, _, _, _ = torus_leakage(N, N, eps, 1, 2, n_phase=32)
        print(f"  {N:6d}  {ml:12.6e}  {ml/ALPHA:10.4f}  {N**2 * ml:12.4f}")

    print()

    # ── Section 4: ε dependence ────────────────────────────
    print("─" * 70)
    print("Section 4: Aspect ratio dependence (N=20)")
    print("─" * 70)
    print()

    print(f"  {'ε':>8s}  {'mean f_leak':>12s}  {'ratio/α':>10s}  {'f/ε²':>12s}")
    print(f"  {'─'*8}  {'─'*12}  {'─'*10}  {'─'*12}")

    for eps_val in [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]:
        ml, _, _, _, _ = torus_leakage(20, 20, eps_val, 1, 2, n_phase=32)
        fe2 = ml / eps_val**2 if eps_val > 0 else 0
        print(f"  {eps_val:8.3f}  {ml:12.6e}  {ml/ALPHA:10.4f}  {fe2:12.6e}")

    print()

    # ── Section 5: Iterative tube circuit ──────────────────
    print("─" * 70)
    print("Section 5: Iterative propagation around tube circuit")
    print("  (signal diminishes at each junction)")
    print("─" * 70)
    print()

    for eps_val in [0.1, 0.3, 0.5, 0.7]:
        for N_steps in [10, 20, 40, 80]:
            cum_leak, final_amp, data = iterative_tube_circuit(N_steps, eps_val)
            print(f"  ε={eps_val:.1f}, N={N_steps:3d}: "
                  f"cumulative leak = {cum_leak:.6e}, "
                  f"final amplitude = {final_amp:.6f}, "
                  f"ratio/α = {cum_leak/ALPHA:.4f}")
        print()

    # ── Section 6: Detailed step-by-step for one circuit ───
    print("─" * 70)
    print("Section 6: Step-by-step for ε=0.3, N=20")
    print("─" * 70)
    print()

    cum_leak, final_amp, data = iterative_tube_circuit(20, 0.3)

    print(f"  {'Step':>5s}  {'θ₁':>8s}  {'f_leak':>12s}  {'E_leaked':>12s}  "
          f"{'cum_leak':>12s}  {'amplitude':>10s}")
    print(f"  {'─'*5}  {'─'*8}  {'─'*12}  {'─'*12}  {'─'*12}  {'─'*10}")

    for i, th1, fl, el, cl, amp in data:
        print(f"  {i:5d}  {th1:8.4f}  {fl:12.6e}  {el:12.6e}  "
              f"{cl:12.6e}  {amp:10.6f}")

    print()
    print(f"  After full circuit:")
    print(f"    Cumulative leakage: {cum_leak:.6e}")
    print(f"    Final amplitude: {final_amp:.6f}")
    print(f"    Energy conserved: {cum_leak + final_amp**2:.6f} (should be 1.0)")
    print(f"    α = {ALPHA:.6e}")
    print(f"    Ratio to α: {cum_leak / ALPHA:.4f}")
    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 70)
    print("Track 11b Summary")
    print("=" * 70)
    print()
    print("  Track 11b computes two quantities:")
    print("  1. Per-junction leakage fraction (CP wave, time-averaged)")
    print("  2. Cumulative leakage over one tube circuit (iterative,")
    print("     with signal diminishing at each step)")
    print()
    print("  Both are proper fractions (0 to 1) with no free parameters.")
    print()

    print("Track 11b complete.")


if __name__ == "__main__":
    main()
