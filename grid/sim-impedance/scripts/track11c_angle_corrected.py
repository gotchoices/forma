#!/usr/bin/env python3
"""
Track 11c — Angle-corrected leakage with multiple scattering models.

Three scattering models tested:
  A. GRID S-matrix: amplitude 2/3 to each outgoing, -1/3 reflected
     Energy: 4/9 per outgoing, 1/9 reflected
  B. Equal split (no reflection): 1/2 energy to each outgoing
     (amplitude 1/√2 ≈ 0.707 per outgoing, 0 reflected)
  C. Angle-weighted: coupling proportional to how well the incoming
     edge aligns with each outgoing edge. Uses cos(θ) projection.
     Normalized to conserve energy.

For each model, at each curved Y-junction:
  1. Compute actual 3D edge directions (distorted from 120°)
  2. Apply the scattering model to get outgoing vector
  3. Decompose into tangential + normal
  4. Normal fraction = leakage at this junction
  5. Iterate around tube circuit with diminishing signal
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
#  Junction angle analysis
# ══════════════════════════════════════════════════════════

def junction_angles(edge_vecs):
    """Compute pairwise angles (degrees) between edge vectors at a junction."""
    e_hats = []
    for ev in edge_vecs:
        n = np.linalg.norm(ev)
        if n < 1e-15:
            e_hats.append(np.zeros(3))
        else:
            e_hats.append(ev / n)

    angles = []
    for i in range(len(e_hats)):
        for j in range(i+1, len(e_hats)):
            cos_a = np.clip(np.dot(e_hats[i], e_hats[j]), -1, 1)
            angles.append(np.degrees(np.arccos(cos_a)))
    return angles


# ══════════════════════════════════════════════════════════
#  Scattering models
# ══════════════════════════════════════════════════════════

def scatter_grid_smatrix(E_in, edge_vecs):
    """
    Model A: GRID S-matrix (2/3 transmit amplitude, -1/3 reflect).
    Amplitude-based, angle-independent.

    Returns the outgoing 3D vector (sum of scattered amplitudes × edge dirs).
    """
    N = len(edge_vecs)
    e_hats = []
    for ev in edge_vecs:
        n = np.linalg.norm(ev)
        e_hats.append(ev / n if n > 1e-15 else np.zeros(3))

    # Project input onto each edge
    a_in = [np.dot(E_in, eh) for eh in e_hats]

    S_refl = 2.0 / N - 1.0   # -1/3
    S_trans = 2.0 / N         # 2/3

    total_a = sum(a_in)
    V_out = np.zeros(3)
    for i in range(N):
        b_i = S_refl * a_in[i] + S_trans * (total_a - a_in[i])
        V_out += b_i * e_hats[i]

    return V_out


def scatter_equal_split(E_in, edge_vecs):
    """
    Model B: Equal energy split (no reflection).
    Each outgoing edge gets 1/2 of the incoming energy.
    Amplitude = sqrt(1/2) per outgoing edge.

    For 3 edges: identify the "incoming" edge as the one most
    anti-aligned with E_in, and the other two as outgoing.
    """
    N = len(edge_vecs)
    e_hats = []
    for ev in edge_vecs:
        n = np.linalg.norm(ev)
        e_hats.append(ev / n if n > 1e-15 else np.zeros(3))

    # The incoming direction is the edge most anti-aligned with E_in
    projections = [np.dot(E_in, eh) for eh in e_hats]

    # For a CP wave, E_in is tangential. The "incoming edge" is the
    # one the wave arrived on (most aligned with -E direction, i.e.
    # most negative projection). The outgoing edges are the other two.
    # Actually, for a general CP field at a node, there's no single
    # "incoming" edge. Let's use a different approach:
    #
    # Project E_in onto each edge. The outgoing vector is the sum
    # of projections onto the two most-forward edges, each weighted
    # by 1/sqrt(2) to conserve energy.
    #
    # Simpler: decompose E_in into the edge basis, then redistribute
    # evenly among the two forward edges.

    # Sort by projection (most positive = most aligned = outgoing)
    order = sorted(range(N), key=lambda i: projections[i], reverse=True)

    # Top 2 are outgoing, bottom 1 is the "incoming" (most anti-aligned)
    # Each outgoing gets amplitude = √(1/2) × |E_in projected forward|
    E_in_mag = np.linalg.norm(E_in)
    if E_in_mag < 1e-30:
        return np.zeros(3)

    amp = E_in_mag / np.sqrt(2)
    V_out = amp * (e_hats[order[0]] + e_hats[order[1]]) / np.sqrt(2)
    # Normalize to conserve energy: |V_out|² should equal |E_in|² (no reflection)
    # Actually, just project E_in onto the two forward edges equally
    a_fwd = [max(projections[order[0]], 0), max(projections[order[1]], 0)]
    total_fwd = sum(a_fwd) + 1e-30
    # Split input energy equally between two outgoing edges
    V_out = np.zeros(3)
    for k in range(2):
        idx = order[k]
        V_out += (E_in_mag / np.sqrt(2)) * e_hats[idx]

    return V_out


def scatter_angle_weighted(E_in, edge_vecs):
    """
    Model C: Angle-weighted scattering.
    The coupling from incoming to each outgoing edge is proportional
    to the cosine of the angle between them (dot product of unit vecs).
    Negative projections (backward edges) get zero.
    Normalized to conserve energy.

    This is the physical model: a signal propagates better along
    edges aligned with its direction.
    """
    N = len(edge_vecs)
    e_hats = []
    for ev in edge_vecs:
        n = np.linalg.norm(ev)
        e_hats.append(ev / n if n > 1e-15 else np.zeros(3))

    E_in_mag = np.linalg.norm(E_in)
    if E_in_mag < 1e-30:
        return np.zeros(3)
    E_in_hat = E_in / E_in_mag

    # Weight each edge by how well it aligns with E_in direction
    weights = []
    for eh in e_hats:
        w = np.dot(E_in_hat, eh)
        weights.append(max(w, 0.0))  # only forward-going edges

    total_w = sum(weights)
    if total_w < 1e-30:
        return np.zeros(3)

    # Normalize weights so total outgoing energy = input energy
    # V_out = Σ (w_i / norm) * E_in_mag * ê_i
    # We need |V_out|² = |E_in|²
    # With weights normalized: w_i' = w_i / total_w
    # V_out = E_in_mag * Σ w_i' * ê_i
    # |V_out|² = E_in_mag² * |Σ w_i' * ê_i|²

    norm_weights = [w / total_w for w in weights]
    V_out_unit = sum(nw * eh for nw, eh in zip(norm_weights, e_hats))
    V_out_mag = np.linalg.norm(V_out_unit)
    if V_out_mag < 1e-30:
        return np.zeros(3)

    # Scale to conserve energy
    V_out = E_in_mag * V_out_unit / V_out_mag

    return V_out


# ══════════════════════════════════════════════════════════
#  Leakage computation
# ══════════════════════════════════════════════════════════

def junction_leakage(E_in_vec, edge_vecs, n_hat, scatter_fn):
    """
    Compute leakage fraction at one junction using a given scatter model.

    Returns (f_leak, f_tangential) — fractions of input energy.
    """
    E2_in = np.dot(E_in_vec, E_in_vec)
    if E2_in < 1e-30:
        return 0.0, 0.0

    V_out = scatter_fn(E_in_vec, edge_vecs)

    # Decompose into normal and tangential
    V_n = np.dot(V_out, n_hat) * n_hat
    V_t = V_out - V_n

    f_leak = np.dot(V_n, V_n) / E2_in
    f_tang = np.dot(V_t, V_t) / E2_in

    return f_leak, f_tang


def torus_leakage_all_models(N1, N2, eps, n1, n2, n_phase=32):
    """
    Compute mean per-junction leakage for all three models.
    """
    R = 1.0
    a = eps * R
    nodes, adj = build_hex_torus(N1, N2, R, a)
    M = len(nodes)

    models = {
        'A (GRID S-matrix)': scatter_grid_smatrix,
        'B (equal split)': scatter_equal_split,
        'C (angle-weighted)': scatter_angle_weighted,
    }

    results = {}
    phases = np.linspace(0, TAU, n_phase, endpoint=False)

    for model_name, scatter_fn in models.items():
        leak_map = np.zeros(M)

        for node_idx in range(M):
            th1 = nodes[node_idx, 0]
            th2 = nodes[node_idx, 1]
            n_hat = torus_normal(th1, th2)
            t1, t2 = torus_tangents(th1, th2, R, a)
            edge_vecs = [ev for (_, ev) in adj[node_idx]]

            leak_sum = 0.0
            for phase in phases:
                phi = n1 * th1 + n2 * th2 + phase
                E_vec = np.cos(phi) * t1 - np.sin(phi) * t2

                f_leak, _ = junction_leakage(E_vec, edge_vecs, n_hat, scatter_fn)
                leak_sum += f_leak

            leak_map[node_idx] = leak_sum / n_phase

        mean_leak = np.mean(leak_map)
        results[model_name] = (mean_leak, leak_map)

    return results, nodes


def iterative_circuit(N_steps, eps, scatter_fn):
    """
    Propagate a signal around one tube circuit (θ₁ direction)
    using a given scattering model.
    """
    R = 1.0
    a = eps * R
    theta1_vals = np.linspace(0, TAU, N_steps, endpoint=False)
    th2 = 0.0
    dth = TAU / N_steps

    amplitude = 1.0
    cumulative_leak = 0.0

    for th1 in theta1_vals:
        n_hat = torus_normal(th1, th2)
        t1, t2 = torus_tangents(th1, th2, R, a)

        E_in = amplitude * t1  # propagating along tube

        # Build local edge directions from neighbors
        pos_here = torus_pos(th1, th2, R, a)
        pos_fwd = torus_pos(th1 + dth, th2, R, a)
        pos_back = torus_pos(th1 - dth, th2, R, a)
        pos_ring = torus_pos(th1, th2 + dth, R, a)

        edge_vecs = [pos_back - pos_here, pos_fwd - pos_here, pos_ring - pos_here]

        f_leak, f_tang = junction_leakage(E_in, edge_vecs, n_hat, scatter_fn)

        cumulative_leak += amplitude**2 * f_leak
        amplitude *= np.sqrt(max(1.0 - f_leak, 0.0))

    return cumulative_leak, amplitude


# ══════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("Track 11c: Angle-corrected leakage — three scattering models")
    print("=" * 70)
    print()
    print("  Model A: GRID S-matrix (ampl 2/3 fwd, -1/3 reflect)")
    print("           Energy: 4/9 per outgoing, 1/9 reflected")
    print("  Model B: Equal split (1/2 energy per outgoing, no reflect)")
    print("  Model C: Angle-weighted (coupling ∝ cos θ, forward only)")
    print()

    # ── Section 1: Junction angles on the torus ────────────
    print("─" * 70)
    print("Section 1: Actual junction angles on curved torus (ε=0.3, N=20)")
    print("─" * 70)
    print()

    R = 1.0
    eps = 0.3
    a = eps * R
    N = 20
    nodes, adj = build_hex_torus(N, N, R, a)

    all_angles = []
    for node_idx in range(len(nodes)):
        evecs = [ev for (_, ev) in adj[node_idx]]
        if len(evecs) >= 3:
            angs = junction_angles(evecs)
            all_angles.extend(angs)

    print(f"  Mean angle: {np.mean(all_angles):.2f}° (flat = 120°)")
    print(f"  Std: {np.std(all_angles):.2f}°")
    print(f"  Range: [{np.min(all_angles):.1f}°, {np.max(all_angles):.1f}°]")
    print(f"  Deviation from 120°: {120 - np.mean(all_angles):+.2f}°")
    print()

    # ── Section 2: All three models compared ───────────────
    print("─" * 70)
    print("Section 2: Mean per-junction leakage — all models (ε=0.3, N=20)")
    print("─" * 70)
    print()

    results, _ = torus_leakage_all_models(N, N, eps, 1, 2, n_phase=32)

    print(f"  {'Model':>25s}  {'mean f_leak':>12s}  {'ratio/α':>10s}")
    print(f"  {'─'*25}  {'─'*12}  {'─'*10}")
    for name, (ml, _) in results.items():
        print(f"  {name:>25s}  {ml:12.6e}  {ml/ALPHA:10.4f}")
    print()

    # ── Section 3: Convergence with N — all models ─────────
    print("─" * 70)
    print("Section 3: Convergence with N (ε=0.3, mode (1,2))")
    print("─" * 70)
    print()

    for model_name, scatter_fn in [('A (GRID)', scatter_grid_smatrix),
                                     ('B (equal)', scatter_equal_split),
                                     ('C (angle)', scatter_angle_weighted)]:
        print(f"  Model {model_name}:")
        print(f"    {'N':>6s}  {'mean f_leak':>12s}  {'ratio/α':>10s}  {'N²×f':>10s}")
        print(f"    {'─'*6}  {'─'*12}  {'─'*10}  {'─'*10}")

        for Nv in [6, 10, 14, 20, 30, 40]:
            R_v = 1.0
            a_v = eps * R_v
            nds, adj_v = build_hex_torus(Nv, Nv, R_v, a_v)
            M = len(nds)
            phases = np.linspace(0, TAU, 32, endpoint=False)

            leak_sum = 0.0
            for ni in range(M):
                th1 = nds[ni, 0]
                th2 = nds[ni, 1]
                n_hat = torus_normal(th1, th2)
                t1, t2 = torus_tangents(th1, th2, R_v, a_v)
                evecs = [ev for (_, ev) in adj_v[ni]]

                node_leak = 0.0
                for phase in phases:
                    phi = th1 + 2 * th2 + phase
                    E_vec = np.cos(phi) * t1 - np.sin(phi) * t2
                    fl, _ = junction_leakage(E_vec, evecs, n_hat, scatter_fn)
                    node_leak += fl
                leak_sum += node_leak / len(phases)

            ml = leak_sum / M
            print(f"    {Nv:6d}  {ml:12.6e}  {ml/ALPHA:10.4f}  {Nv**2 * ml:10.4f}")
        print()

    # ── Section 4: Iterative circuit — all models ──────────
    print("─" * 70)
    print("Section 4: Cumulative leakage per tube circuit (iterative)")
    print("─" * 70)
    print()

    for model_name, scatter_fn in [('A (GRID)', scatter_grid_smatrix),
                                     ('B (equal)', scatter_equal_split),
                                     ('C (angle)', scatter_angle_weighted)]:
        print(f"  Model {model_name}:")
        print(f"    {'N':>6s}  {'ε=0.1':>12s}  {'ε=0.3':>12s}  {'ε=0.5':>12s}  {'ε=0.7':>12s}")
        print(f"    {'─'*6}  {'─'*12}  {'─'*12}  {'─'*12}  {'─'*12}")

        for Nv in [10, 20, 40, 80]:
            row = f"    {Nv:6d}"
            for ev in [0.1, 0.3, 0.5, 0.7]:
                cl, _ = iterative_circuit(Nv, ev, scatter_fn)
                row += f"  {cl:12.6e}"
            print(row)

        # Show ratio to α for the key case
        print()
        print(f"    Ratio to α (ε=0.3):")
        for Nv in [10, 20, 40, 80]:
            cl, fa = iterative_circuit(Nv, 0.3, scatter_fn)
            print(f"      N={Nv:3d}: leak/α = {cl/ALPHA:.4f}, "
                  f"energy conserved = {cl + fa**2:.6f}")
        print()

    # ── Section 5: ε dependence at fixed N ─────────────────
    print("─" * 70)
    print("Section 5: ε dependence of iterative circuit (N=20)")
    print("─" * 70)
    print()

    N_fix = 20
    print(f"  {'ε':>8s}", end="")
    for mn in ['A (GRID)', 'B (equal)', 'C (angle)']:
        print(f"  {mn:>14s}", end="")
    print()
    print(f"  {'─'*8}", end="")
    for _ in range(3):
        print(f"  {'─'*14}", end="")
    print()

    for ev in [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]:
        row = f"  {ev:8.3f}"
        for scatter_fn in [scatter_grid_smatrix, scatter_equal_split, scatter_angle_weighted]:
            cl, _ = iterative_circuit(N_fix, ev, scatter_fn)
            row += f"  {cl/ALPHA:14.4f}"
        print(row + "  (× α)")

    print()
    print("=" * 70)
    print("Track 11c complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
