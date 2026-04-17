#!/usr/bin/env python3
"""
Track 12: Charge per radian — top-down α from the minimal torus.

GRID tells us: a full 2π defect = one unit of charge e = √(4πα).
A torus IS a 2π defect.  This track asks:

1. What is the smallest hexagonal lattice that forms a valid torus?
2. How much is each Y-junction distorted from 120°?
3. How does the total distortion relate to 2π?
4. If we distribute the known charge (e) across junctions
   proportionally to their distortion, what is the charge
   per radian?
5. Can we compute a distortion ENERGY that equals α × mode energy?
"""

import numpy as np
from pathlib import Path

TAU = 2 * np.pi
ALPHA = 1 / 137.036
E_CHARGE = np.sqrt(4 * np.pi * ALPHA)  # ≈ 0.3028

OUT = Path(__file__).resolve().parent.parent / "output"
OUT.mkdir(exist_ok=True)


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
    t1 = np.array([-st1 * cp, ct1, -st1 * sp])
    t2 = np.array([-sp, 0.0, cp])
    n1 = np.linalg.norm(t1)
    n2 = np.linalg.norm(t2)
    return t1 / (n1 + 1e-30), t2 / (n2 + 1e-30)


# ══════════════════════════════════════════════════════════
#  Hexagonal torus lattice
# ══════════════════════════════════════════════════════════

def build_hex_torus(N1, N2, R, a):
    """Build honeycomb lattice on torus. Returns (nodes, adj)."""
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

    return nodes, adj, edges


# ══════════════════════════════════════════════════════════
#  Junction analysis
# ══════════════════════════════════════════════════════════

def analyze_junction(node_idx, nodes, adj):
    """
    Compute geometric properties of one Y-junction.

    Returns dict with:
      angles_3d: list of 3 pairwise angles between edges (degrees)
      angle_sum: sum of the 3 angles
      angular_deficiency: 360 - angle_sum (Descartes)
      solid_angle: solid angle subtended by the 3 edge directions
      normal_deviation: angle between outgoing-plane normal and surface normal
      turning_angle: angle of surface normal rotation to nearest neighbor
      edge_lengths: list of 3 edge lengths
    """
    th1 = nodes[node_idx, 0]
    th2 = nodes[node_idx, 1]
    n_hat = torus_normal(th1, th2)

    edge_vecs = [ev for (_, ev) in adj[node_idx]]
    n_edges = len(edge_vecs)

    # Unit edge vectors
    e_hats = []
    lengths = []
    for ev in edge_vecs:
        L = np.linalg.norm(ev)
        lengths.append(L)
        e_hats.append(ev / L if L > 1e-15 else np.zeros(3))

    # Pairwise angles
    angles = []
    for i in range(n_edges):
        for j in range(i+1, n_edges):
            cos_a = np.clip(np.dot(e_hats[i], e_hats[j]), -1, 1)
            angles.append(np.degrees(np.arccos(cos_a)))

    angle_sum = sum(angles)
    angular_deficiency = 360.0 - angle_sum

    # Solid angle of the 3 edge directions
    # (for 3 unit vectors, solid angle = area of spherical triangle)
    if n_edges >= 3:
        # Use the formula: tan(Ω/4) = |a·(b×c)| / (1 + a·b + a·c + b·c)
        a, b, c = e_hats[0], e_hats[1], e_hats[2]
        numer = abs(np.dot(a, np.cross(b, c)))
        denom = 1 + np.dot(a, b) + np.dot(a, c) + np.dot(b, c)
        if denom > 1e-15:
            solid_angle = 4 * np.arctan2(numer, denom)
        else:
            solid_angle = 0.0
    else:
        solid_angle = 0.0

    # Outgoing plane normal vs surface normal
    if n_edges >= 3:
        plane_n = np.cross(e_hats[0], e_hats[1])
        pn_mag = np.linalg.norm(plane_n)
        if pn_mag > 1e-15:
            plane_n = plane_n / pn_mag
            cos_dev = abs(np.dot(plane_n, n_hat))
            normal_deviation = np.degrees(np.arccos(np.clip(cos_dev, 0, 1)))
        else:
            normal_deviation = 0.0
    else:
        normal_deviation = 0.0

    # Turning angle: rotation of surface normal to each neighbor
    turning_angles = []
    for nid, ev in adj[node_idx]:
        n_hat_neighbor = torus_normal(nodes[nid, 0], nodes[nid, 1])
        cos_turn = np.clip(np.dot(n_hat, n_hat_neighbor), -1, 1)
        turning_angles.append(np.degrees(np.arccos(cos_turn)))

    return {
        'angles_3d': angles,
        'angle_sum': angle_sum,
        'angular_deficiency': angular_deficiency,
        'solid_angle': solid_angle,
        'solid_angle_deg': np.degrees(solid_angle),
        'normal_deviation': normal_deviation,
        'turning_angles': turning_angles,
        'mean_turning': np.mean(turning_angles),
        'edge_lengths': lengths,
    }


# ══════════════════════════════════════════════════════════
#  CP field charge at each junction (Track 8 method)
# ══════════════════════════════════════════════════════════

def cp_charge_per_junction(nodes, adj, eps, n1, n2, n_phase=64):
    """
    Compute the time-averaged E·ρ̂ at each junction for a CP wave.
    This is the Track 8 charge measure.
    """
    R = 1.0
    a = eps * R
    M = len(nodes)
    phases = np.linspace(0, TAU, n_phase, endpoint=False)

    charge_map = np.zeros(M)

    for node_idx in range(M):
        th1 = nodes[node_idx, 0]
        th2 = nodes[node_idx, 1]
        t1, t2 = torus_tangents(th1, th2, R, a)

        cp, sp = np.cos(th2), np.sin(th2)
        rho_hat = np.array([cp, 0.0, sp])

        charge_sum = 0.0
        for phase in phases:
            phi = n1 * th1 + n2 * th2 + phase
            E_vec = np.cos(phi) * t1 - np.sin(phi) * t2
            charge_sum += np.dot(E_vec, rho_hat)

        charge_map[node_idx] = charge_sum / n_phase

    return charge_map


# ══════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("Track 12: Charge per radian — top-down α from the minimal torus")
    print("=" * 70)
    print()
    print(f"  GRID predicts: e = √(4πα) = {E_CHARGE:.6f}")
    print(f"  α = {ALPHA:.6e},  1/α = {1/ALPHA:.2f}")
    print(f"  A full 2π defect (torus tube) produces charge e.")
    print(f"  Question: how is e distributed across junctions?")
    print()

    # ── Section 1: Minimal tori — lattice statistics ───────
    print("─" * 70)
    print("Section 1: Hexagonal tori at various sizes")
    print("─" * 70)
    print()

    eps = 0.3
    R = 1.0
    a = eps * R

    print(f"  ε = {eps}")
    print()
    print(f"  {'N':>4s}  {'nodes':>6s}  {'edges':>6s}  {'mean∠':>8s}  "
          f"{'Σ|Δ∠|':>8s}  {'Σsolid':>8s}  {'Σturn':>8s}  "
          f"{'edge_min':>9s}  {'edge_max':>9s}")
    print(f"  {'─'*4}  {'─'*6}  {'─'*6}  {'─'*8}  "
          f"{'─'*8}  {'─'*8}  {'─'*8}  "
          f"{'─'*9}  {'─'*9}")

    torus_data = {}
    for N in [2, 3, 4, 5, 6, 8, 10, 14, 20]:
        nodes, adj, edges_list = build_hex_torus(N, N, R, a)
        M = len(nodes)
        n_edges = len(edges_list)

        all_angles = []
        all_deficiency = []
        all_solid = []
        all_turning = []
        all_edge_lengths = []

        for ni in range(M):
            info = analyze_junction(ni, nodes, adj)
            all_angles.extend(info['angles_3d'])
            all_deficiency.append(info['angular_deficiency'])
            all_solid.append(info['solid_angle'])
            all_turning.append(info['mean_turning'])
            all_edge_lengths.extend(info['edge_lengths'])

        sum_abs_def = sum(abs(d) for d in all_deficiency)
        sum_solid = sum(all_solid)
        sum_turning = sum(all_turning)

        torus_data[N] = {
            'nodes': M, 'edges': n_edges,
            'mean_angle': np.mean(all_angles),
            'sum_abs_deficiency': sum_abs_def,
            'sum_solid': sum_solid,
            'sum_turning': sum_turning,
            'edge_min': min(all_edge_lengths),
            'edge_max': max(all_edge_lengths),
        }

        print(f"  {N:4d}  {M:6d}  {n_edges:6d}  "
              f"{np.mean(all_angles):8.2f}  "
              f"{sum_abs_def:8.2f}  "
              f"{np.degrees(sum_solid):8.2f}  "
              f"{sum_turning:8.2f}  "
              f"{min(all_edge_lengths):9.4f}  "
              f"{max(all_edge_lengths):9.4f}")

    print()

    # ── Section 2: Detailed minimal torus (N=2) ───────────
    print("─" * 70)
    print("Section 2: Detailed junction analysis — minimal torus (N=2)")
    print("─" * 70)
    print()

    N = 2
    nodes, adj, edges_list = build_hex_torus(N, N, R, a)
    M = len(nodes)

    print(f"  N = {N}: {M} nodes, {len(edges_list)} edges")
    print()

    print(f"  {'Node':>5s}  {'θ₁':>7s}  {'θ₂':>7s}  "
          f"{'∠₁':>6s}  {'∠₂':>6s}  {'∠₃':>6s}  "
          f"{'Σ∠':>7s}  {'deficit':>8s}  {'solid∠':>7s}  "
          f"{'turn':>7s}")
    print(f"  {'─'*5}  {'─'*7}  {'─'*7}  "
          f"{'─'*6}  {'─'*6}  {'─'*6}  "
          f"{'─'*7}  {'─'*8}  {'─'*7}  "
          f"{'─'*7}")

    junction_data = []
    for ni in range(M):
        info = analyze_junction(ni, nodes, adj)
        th1 = nodes[ni, 0]
        th2 = nodes[ni, 1]
        angs = sorted(info['angles_3d'])
        while len(angs) < 3:
            angs.append(0)

        junction_data.append(info)
        print(f"  {ni:5d}  {th1:7.3f}  {th2:7.3f}  "
              f"{angs[0]:6.1f}  {angs[1]:6.1f}  {angs[2]:6.1f}  "
              f"{info['angle_sum']:7.1f}  {info['angular_deficiency']:+8.1f}  "
              f"{info['solid_angle_deg']:7.2f}  "
              f"{info['mean_turning']:7.2f}")

    print()

    # ── Section 3: Distortion measures and 2π ──────────────
    print("─" * 70)
    print("Section 3: Total distortion measures vs 2π")
    print("─" * 70)
    print()

    for N in [2, 3, 4, 5, 6, 10, 20]:
        nodes_n, adj_n, _ = build_hex_torus(N, N, R, a)
        M_n = len(nodes_n)

        sum_solid = 0
        sum_turning = 0
        sum_def = 0

        for ni in range(M_n):
            info = analyze_junction(ni, nodes_n, adj_n)
            sum_solid += info['solid_angle']
            sum_turning += np.radians(info['mean_turning'])
            sum_def += abs(info['angular_deficiency'])

        print(f"  N={N:3d} ({M_n:4d} nodes):")
        print(f"    Σ solid angle = {sum_solid:.4f} rad = {sum_solid/TAU:.4f} × 2π")
        print(f"    Σ turning     = {sum_turning:.4f} rad = {sum_turning/TAU:.4f} × 2π")
        print(f"    Σ |deficit|   = {sum_def:.2f}°  = {np.radians(sum_def)/TAU:.4f} × 2π")
        print()

    # ── Section 4: Charge distribution — Approach A ────────
    print("─" * 70)
    print("Section 4: Charge distribution — proportional to solid angle")
    print("─" * 70)
    print()
    print(f"  If q_k = (solid_angle_k / Σ_solid) × e:")
    print()

    for N in [2, 3, 5, 10, 20]:
        nodes_n, adj_n, _ = build_hex_torus(N, N, R, a)
        M_n = len(nodes_n)

        solid_angles = []
        for ni in range(M_n):
            info = analyze_junction(ni, nodes_n, adj_n)
            solid_angles.append(info['solid_angle'])

        total_solid = sum(solid_angles)
        if total_solid < 1e-30:
            continue

        charges = [(sa / total_solid) * E_CHARGE for sa in solid_angles]
        charge_per_rad = E_CHARGE / total_solid

        print(f"  N={N:3d}: Σsolid = {total_solid:.4f} rad, "
              f"charge/rad = {charge_per_rad:.6f}, "
              f"max q_k = {max(charges):.6f}, "
              f"min q_k = {min(charges):.6f}")

    print()
    print(f"  For reference: e/(2π) = {E_CHARGE/TAU:.6f}")
    print(f"  √(α/π) = {np.sqrt(ALPHA/np.pi):.6f}")
    print()

    # ── Section 5: Charge distribution — Approach B ────────
    print("─" * 70)
    print("Section 5: Charge from CP field (Track 8 method)")
    print("─" * 70)
    print()

    for N in [2, 3, 5, 10, 20]:
        nodes_n, adj_n, _ = build_hex_torus(N, N, R, a)
        charge_map = cp_charge_per_junction(nodes_n, adj_n, eps, 1, 2)

        Q_total = np.sum(charge_map)
        Q_abs = np.sum(np.abs(charge_map))
        n_positive = np.sum(charge_map > 0)
        n_negative = np.sum(charge_map < 0)

        print(f"  N={N:3d}: Q_total = {Q_total:+.4f}, |Q|_total = {Q_abs:.4f}, "
              f"+nodes = {n_positive}, -nodes = {n_negative}")

    print()

    # ── Section 6: Distortion energy — Approach C ──────────
    print("─" * 70)
    print("Section 6: Distortion energy (elastic cost of bending)")
    print("─" * 70)
    print()
    print("  At each junction, measure the distortion from the flat")
    print("  120° configuration.  The 'distortion energy' is the")
    print("  sum of squared angular deviations (in radians).")
    print()
    print("  If α = Σ(δθ²) / (normalization), what normalization gives α?")
    print()

    for N in [2, 3, 4, 5, 6, 8, 10, 14, 20, 30, 40]:
        nodes_n, adj_n, _ = build_hex_torus(N, N, R, a)
        M_n = len(nodes_n)

        sum_dtheta2 = 0.0  # Σ (angle - 120°)² in radians²
        sum_solid2 = 0.0   # Σ (solid_angle)²
        sum_solid = 0.0

        for ni in range(M_n):
            info = analyze_junction(ni, nodes_n, adj_n)
            for ang in info['angles_3d']:
                dth = np.radians(ang - 120.0)
                sum_dtheta2 += dth**2
            sum_solid2 += info['solid_angle']**2
            sum_solid += info['solid_angle']

        # Various normalizations
        E_dtheta2 = sum_dtheta2
        E_solid2 = sum_solid2

        # What normalization N_x gives α = E / N_x?
        if E_dtheta2 > 0:
            norm_for_alpha_dt2 = E_dtheta2 / ALPHA
        else:
            norm_for_alpha_dt2 = float('inf')

        if E_solid2 > 0:
            norm_for_alpha_s2 = E_solid2 / ALPHA
        else:
            norm_for_alpha_s2 = float('inf')

        print(f"  N={N:3d} ({M_n:4d} nodes): "
              f"Σδθ² = {E_dtheta2:.6f}, "
              f"Σδθ²/α = {E_dtheta2/ALPHA:.2f}, "
              f"Σδθ²/(4π) = {E_dtheta2/(4*np.pi):.6f}, "
              f"Σsolid = {sum_solid:.4f}")

    print()

    # ── Section 7: Does Σδθ² / (4π × N_cells) converge? ───
    print("─" * 70)
    print("Section 7: Convergence of distortion measures")
    print("─" * 70)
    print()

    print(f"  {'N':>4s}  {'Σδθ²':>10s}  {'Σδθ²/N²':>10s}  "
          f"{'Σsolid':>10s}  {'Σsolid/N²':>10s}  "
          f"{'Σδθ²/(4π)':>10s}")
    print(f"  {'─'*4}  {'─'*10}  {'─'*10}  "
          f"{'─'*10}  {'─'*10}  "
          f"{'─'*10}")

    for N in [2, 3, 4, 5, 6, 8, 10, 14, 20, 30, 40]:
        nodes_n, adj_n, _ = build_hex_torus(N, N, R, a)
        M_n = len(nodes_n)

        sum_dtheta2 = 0.0
        sum_solid = 0.0

        for ni in range(M_n):
            info = analyze_junction(ni, nodes_n, adj_n)
            for ang in info['angles_3d']:
                dth = np.radians(ang - 120.0)
                sum_dtheta2 += dth**2
            sum_solid += info['solid_angle']

        print(f"  {N:4d}  {sum_dtheta2:10.6f}  {sum_dtheta2/N**2:10.6f}  "
              f"{sum_solid:10.6f}  {sum_solid/N**2:10.6f}  "
              f"{sum_dtheta2/(4*np.pi):10.6f}")

    print()

    # ── Section 8: ε dependence ────────────────────────────
    print("─" * 70)
    print("Section 8: ε dependence (N=20)")
    print("─" * 70)
    print()

    N = 20
    print(f"  {'ε':>8s}  {'Σδθ²':>10s}  {'Σsolid':>10s}  "
          f"{'Σδθ²/α':>10s}  {'Σδθ²/ε²':>10s}")
    print(f"  {'─'*8}  {'─'*10}  {'─'*10}  "
          f"{'─'*10}  {'─'*10}")

    for eps_v in [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]:
        a_v = eps_v * R
        nodes_n, adj_n, _ = build_hex_torus(N, N, R, a_v)
        M_n = len(nodes_n)

        sum_dtheta2 = 0.0
        sum_solid = 0.0

        for ni in range(M_n):
            info = analyze_junction(ni, nodes_n, adj_n)
            for ang in info['angles_3d']:
                dth = np.radians(ang - 120.0)
                sum_dtheta2 += dth**2
            sum_solid += info['solid_angle']

        fe2 = sum_dtheta2 / eps_v**2 if eps_v > 0 else 0
        print(f"  {eps_v:8.3f}  {sum_dtheta2:10.6f}  {sum_solid:10.6f}  "
              f"{sum_dtheta2/ALPHA:10.2f}  {fe2:10.4f}")

    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"  Known: e = √(4πα) = {E_CHARGE:.6f}")
    print(f"  Known: α = {ALPHA:.6e}")
    print()

    # Key numbers from the minimal torus
    N_min = 2
    nodes_min, adj_min, _ = build_hex_torus(N_min, N_min, R, a)
    M_min = len(nodes_min)
    sum_solid_min = 0
    sum_dtheta2_min = 0
    for ni in range(M_min):
        info = analyze_junction(ni, nodes_min, adj_min)
        sum_solid_min += info['solid_angle']
        for ang in info['angles_3d']:
            sum_dtheta2_min += np.radians(ang - 120.0)**2

    print(f"  Minimal torus (N=2, {M_min} nodes, ε={eps}):")
    print(f"    Σ solid angle  = {sum_solid_min:.4f} rad = {sum_solid_min/TAU:.4f} × 2π")
    print(f"    Σ δθ²          = {sum_dtheta2_min:.4f} rad²")
    print(f"    charge/solid   = e / Σsolid = {E_CHARGE/sum_solid_min:.6f}")
    print(f"    e / 2π         = {E_CHARGE/TAU:.6f}")
    print()

    # Check: does any convergent quantity equal α?
    print("  Convergent invariants (from Section 7, large N limit):")
    nodes_40, adj_40, _ = build_hex_torus(40, 40, R, a)
    sum_dtheta2_40 = 0
    sum_solid_40 = 0
    for ni in range(len(nodes_40)):
        info = analyze_junction(ni, nodes_40, adj_40)
        for ang in info['angles_3d']:
            sum_dtheta2_40 += np.radians(ang - 120.0)**2
        sum_solid_40 += info['solid_angle']

    print(f"    Σδθ²/N²  → {sum_dtheta2_40/40**2:.6f}  (invariant)")
    print(f"    Σsolid/N² → {sum_solid_40/40**2:.6f}  (invariant)")
    print(f"    α         = {ALPHA:.6f}")
    print(f"    Σδθ²/N² / α = {sum_dtheta2_40/40**2/ALPHA:.4f}")
    print(f"    Σsolid/N² / α = {sum_solid_40/40**2/ALPHA:.4f}")
    print()

    print("  Does any measure give α directly?")
    ratio_dt2 = sum_dtheta2_40 / 40**2 / ALPHA
    ratio_sol = sum_solid_40 / 40**2 / ALPHA
    if abs(ratio_dt2 - 1.0) < 0.1:
        print(f"    Σδθ²/N² ≈ α to {abs(ratio_dt2-1)*100:.1f}% — POSSIBLE MATCH")
    elif abs(ratio_sol - 1.0) < 0.1:
        print(f"    Σsolid/N² ≈ α to {abs(ratio_sol-1)*100:.1f}% — POSSIBLE MATCH")
    else:
        print(f"    No direct match. Σδθ²/N² = {ratio_dt2:.2f}×α, "
              f"Σsolid/N² = {ratio_sol:.2f}×α")

    print()
    print("Track 12 complete.")


if __name__ == "__main__":
    main()
