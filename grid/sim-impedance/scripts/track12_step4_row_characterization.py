#!/usr/bin/env python3
"""
Track 12 Step 4: Row-by-row Y-junction characterization.

At each latitude θ₁ on the torus, the Y-junctions experience
a specific type of distortion:

  θ₁ ≈ 0 (outer equator):   ring edges stretched, tube edges normal
                              → hexagons short and wide
                              → Y angles: two wide, one narrow

  θ₁ ≈ π/2 (top/bottom):    minimal distortion (curvature changes sign)
                              → hexagons nearly regular
                              → Y angles: ~120° each

  θ₁ ≈ π (inner equator):   ring edges compressed, tube edges normal
                              → hexagons tall and skinny
                              → Y angles: two narrow, one wide

This step:
1. Characterize each row's Y-junction shape precisely
2. Decompose the distortion into "ring stretch" and "tube bend"
3. Compute the E-field normal component (Track 8 method) per row
4. Determine which rows contribute most to charge
5. Look for a universal function: charge_contribution(distortion_type)
"""

import numpy as np
from pathlib import Path

TAU = 2 * np.pi
ALPHA = 1 / 137.036
E_CHARGE = np.sqrt(4 * np.pi * ALPHA)


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
    return t1 / (np.linalg.norm(t1) + 1e-30), t2 / (np.linalg.norm(t2) + 1e-30)

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


def characterize_wye(node_idx, nodes, adj, R, a):
    """
    Fully characterize one Y-junction on the torus.

    Returns dict with:
      th1, th2: position on torus
      curvature: local Gaussian curvature κ = cos θ₁ / (R + a cos θ₁)
      ring_circumference: local ring circumference 2π(R + a cos θ₁)
      edge_lengths: [L1, L2, L3]
      edge_angles_3d: [α12, α13, α23] — pairwise angles in 3D
      edge_types: classify each edge as 'tube', 'ring', or 'diagonal'
                  based on how much it aligns with t₁ vs t₂
      ring_stretch: ratio of ring-direction edge length to tube-direction
      tube_component: how much each edge points in the tube direction
      ring_component: how much each edge points in the ring direction
      normal_component: how much each edge points out of the surface
      non_coplanarity: scalar triple product
    """
    th1 = nodes[node_idx, 0]
    th2 = nodes[node_idx, 1]
    t1_hat, t2_hat = torus_tangents(th1, th2, R, a)
    n_hat = torus_normal(th1, th2)

    kappa = np.cos(th1) / (R + a * np.cos(th1))
    ring_circ = TAU * (R + a * np.cos(th1))

    edge_vecs = [ev for (_, ev) in adj[node_idx]]
    n_edges = len(edge_vecs)

    lengths = []
    e_hats = []
    tube_comps = []
    ring_comps = []
    normal_comps = []

    for ev in edge_vecs:
        L = np.linalg.norm(ev)
        lengths.append(L)
        eh = ev / (L + 1e-30)
        e_hats.append(eh)
        tube_comps.append(abs(np.dot(eh, t1_hat)))
        ring_comps.append(abs(np.dot(eh, t2_hat)))
        normal_comps.append(abs(np.dot(eh, n_hat)))

    # Classify edges by direction
    edge_types = []
    for tc, rc in zip(tube_comps, ring_comps):
        if tc > 0.7:
            edge_types.append('tube')
        elif rc > 0.7:
            edge_types.append('ring')
        else:
            edge_types.append('diagonal')

    # Pairwise angles
    angles_3d = []
    for i in range(n_edges):
        for j in range(i+1, n_edges):
            cos_a = np.clip(np.dot(e_hats[i], e_hats[j]), -1, 1)
            angles_3d.append(np.degrees(np.arccos(cos_a)))

    # Ring stretch: ratio of ring-edge length to tube-edge length
    ring_lengths = [L for L, t in zip(lengths, edge_types) if t == 'ring']
    tube_lengths = [L for L, t in zip(lengths, edge_types) if t == 'tube']
    diag_lengths = [L for L, t in zip(lengths, edge_types) if t == 'diagonal']

    if tube_lengths and ring_lengths:
        ring_stretch = np.mean(ring_lengths) / np.mean(tube_lengths)
    elif tube_lengths and diag_lengths:
        ring_stretch = np.mean(diag_lengths) / np.mean(tube_lengths)
    else:
        ring_stretch = 1.0

    # Non-coplanarity
    trip = abs(np.dot(e_hats[0], np.cross(e_hats[1], e_hats[2]))) if n_edges >= 3 else 0

    return {
        'th1': th1, 'th2': th2,
        'curvature': kappa,
        'ring_circumference': ring_circ,
        'edge_lengths': lengths,
        'edge_angles_3d': angles_3d,
        'edge_types': edge_types,
        'ring_stretch': ring_stretch,
        'tube_comps': tube_comps,
        'ring_comps': ring_comps,
        'normal_comps': normal_comps,
        'non_coplanarity': trip,
        'mean_normal': np.mean(normal_comps),
    }


def row_cp_charge(row_indices, nodes, adj, R, a, n1=1, n2=2, n_phase=32):
    """
    Compute the time-averaged E·ρ̂ for a row of nodes.
    This is the Track 8 charge measure — the n₁=1 component
    that produces net Gauss flux.

    Returns the mean E·ρ̂ for the row (signed).
    """
    phases = np.linspace(0, TAU, n_phase, endpoint=False)
    row_charge = 0.0

    for ni in row_indices:
        th1 = nodes[ni, 0]
        th2 = nodes[ni, 1]
        t1, t2 = torus_tangents(th1, th2, R, a)
        cp, sp = np.cos(th2), np.sin(th2)
        rho_hat = np.array([cp, 0.0, sp])

        node_charge = 0.0
        for phase in phases:
            phi = n1 * th1 + n2 * th2 + phase
            E_vec = np.cos(phi) * t1 - np.sin(phi) * t2
            node_charge += np.dot(E_vec, rho_hat)

        row_charge += node_charge / n_phase

    return row_charge / len(row_indices)


def main():
    print("=" * 70)
    print("Track 12 Step 4: Row-by-row Y-junction characterization")
    print("=" * 70)
    print()

    R = 1.0
    eps = 0.3
    a = eps * R

    # ── Section 1: Full characterization at N=20 ──────────
    print("─" * 70)
    print("Section 1: Y-junction character at each latitude (N=20, ε=0.3)")
    print("─" * 70)
    print()

    N = 20
    nodes, adj = build_hex_torus(N, N, R, a)
    M = len(nodes)
    th1_vals = nodes[:, 0]
    unique_th1 = np.sort(np.unique(np.round(th1_vals, 8)))

    print(f"  {'row':>4s}  {'θ₁':>7s}  {'region':>8s}  {'κ':>7s}  "
          f"{'stretch':>8s}  {'trip':>8s}  {'mn_norm':>8s}  "
          f"{'∠min':>6s}  {'∠max':>6s}  {'types':>14s}")
    print(f"  {'─'*4}  {'─'*7}  {'─'*8}  {'─'*7}  "
          f"{'─'*8}  {'─'*8}  {'─'*8}  "
          f"{'─'*6}  {'─'*6}  {'─'*14}")

    row_data = []
    for i, th1_t in enumerate(unique_th1):
        row_idx = np.where(np.abs(th1_vals - th1_t) < 1e-6)[0]

        # Classify region
        if th1_t < 0.5 or th1_t > TAU - 0.5:
            region = 'outer'
        elif abs(th1_t - np.pi) < 0.5:
            region = 'inner'
        elif abs(th1_t - np.pi/2) < 0.5 or abs(th1_t - 3*np.pi/2) < 0.5:
            region = 'top/bot'
        else:
            region = 'mid'

        chars = [characterize_wye(ni, nodes, adj, R, a) for ni in row_idx]

        mean_stretch = np.mean([c['ring_stretch'] for c in chars])
        mean_trip = np.mean([c['non_coplanarity'] for c in chars])
        mean_norm = np.mean([c['mean_normal'] for c in chars])
        all_angles = [ang for c in chars for ang in c['edge_angles_3d']]
        min_ang = min(all_angles)
        max_ang = max(all_angles)

        # Most common edge type pattern
        type_counts = {}
        for c in chars:
            key = tuple(sorted(c['edge_types']))
            type_counts[key] = type_counts.get(key, 0) + 1
        most_common = max(type_counts, key=type_counts.get)

        kappa = chars[0]['curvature']

        row_data.append({
            'th1': th1_t, 'row_idx': row_idx, 'region': region,
            'kappa': kappa, 'stretch': mean_stretch, 'trip': mean_trip,
            'mean_norm': mean_norm, 'min_ang': min_ang, 'max_ang': max_ang,
            'types': most_common, 'n_nodes': len(row_idx),
        })

        print(f"  {i:4d}  {th1_t:7.3f}  {region:>8s}  {kappa:+7.3f}  "
              f"{mean_stretch:8.3f}  {mean_trip:8.5f}  {mean_norm:8.5f}  "
              f"{min_ang:6.1f}  {max_ang:6.1f}  {str(most_common):>14s}")

    print()

    # ── Section 2: CP charge per row ───────────────────────
    print("─" * 70)
    print("Section 2: CP field charge (E·ρ̂) per row")
    print("  (Track 8 method — only n₁=1 component gives net charge)")
    print("─" * 70)
    print()

    print(f"  {'row':>4s}  {'θ₁':>7s}  {'region':>8s}  {'κ':>7s}  "
          f"{'stretch':>8s}  {'E·ρ̂':>12s}  {'|E·ρ̂|':>12s}")
    print(f"  {'─'*4}  {'─'*7}  {'─'*8}  {'─'*7}  "
          f"{'─'*8}  {'─'*12}  {'─'*12}")

    cp_by_row = []
    for i, rd in enumerate(row_data):
        q = row_cp_charge(rd['row_idx'], nodes, adj, R, a, n1=1, n2=2)
        q_abs = abs(q)
        cp_by_row.append(q)

        print(f"  {i:4d}  {rd['th1']:7.3f}  {rd['region']:>8s}  "
              f"{rd['kappa']:+7.3f}  {rd['stretch']:8.3f}  "
              f"{q:12.6e}  {q_abs:12.6e}")

    print()
    total_q = sum(cp_by_row)
    total_abs = sum(abs(q) for q in cp_by_row)
    print(f"  Total Q (signed): {total_q:.6e}")
    print(f"  Total |Q|:        {total_abs:.6e}")
    print()

    # ── Section 3: Fourier decompose the charge profile ────
    print("─" * 70)
    print("Section 3: Fourier decomposition of the charge profile")
    print("─" * 70)
    print()

    th1_arr = np.array([rd['th1'] for rd in row_data])
    q_arr = np.array(cp_by_row)

    print(f"  Fourier harmonics of E·ρ̂(θ₁):")
    for n in range(6):
        cn = 2 * np.mean(q_arr * np.cos(n * th1_arr))
        sn = 2 * np.mean(q_arr * np.sin(n * th1_arr))
        amp = np.sqrt(cn**2 + sn**2)
        phase = np.degrees(np.arctan2(sn, cn))
        print(f"    n={n}: amplitude = {amp:.6e}, phase = {phase:+.1f}°"
              f"{'  ← CHARGE (n₁=1)' if n == 1 else ''}")

    print()

    # ── Section 4: Charge vs distortion correlation ────────
    print("─" * 70)
    print("Section 4: Charge contribution vs distortion measures")
    print("─" * 70)
    print()

    stretches = np.array([rd['stretch'] for rd in row_data])
    kappas = np.array([rd['kappa'] for rd in row_data])
    trips = np.array([rd['trip'] for rd in row_data])
    norms = np.array([rd['mean_norm'] for rd in row_data])
    q_abs_arr = np.abs(q_arr)

    print(f"  Correlation of |E·ρ̂| with distortion measures:")
    for name, vals in [('curvature κ', kappas),
                        ('ring_stretch', stretches),
                        ('non_coplanarity', trips),
                        ('mean_normal', norms)]:
        if np.std(vals) > 1e-10 and np.std(q_abs_arr) > 1e-10:
            corr = np.corrcoef(vals, q_abs_arr)[0, 1]
        else:
            corr = 0
        print(f"    {name:>20s}: r = {corr:+.4f}")

    print()

    # ── Section 5: Convergence check — does charge d₁ converge?
    print("─" * 70)
    print("Section 5: Does the charge profile's d₁ converge with N?")
    print("─" * 70)
    print()

    print(f"  {'N':>4s}  {'charge_d₁':>12s}  {'d₁/α':>10s}  "
          f"{'stretch_d₁':>12s}  {'str_d₁/α':>10s}")
    print(f"  {'─'*4}  {'─'*12}  {'─'*10}  "
          f"{'─'*12}  {'─'*10}")

    for Nv in [4, 6, 8, 10, 14, 20, 30, 40]:
        nds, adj_v = build_hex_torus(Nv, Nv, R, a)
        Mv = len(nds)
        th1_v = nds[:, 0]
        unique_th1_v = np.sort(np.unique(np.round(th1_v, 8)))

        row_ths = []
        row_qs = []
        row_strs = []

        for th1_t in unique_th1_v:
            ridx = np.where(np.abs(th1_v - th1_t) < 1e-6)[0]
            q = row_cp_charge(ridx, nds, adj_v, R, a, n1=1, n2=2, n_phase=32)
            chars = [characterize_wye(ni, nds, adj_v, R, a) for ni in ridx]
            s = np.mean([c['ring_stretch'] for c in chars])
            row_ths.append(th1_t)
            row_qs.append(q)
            row_strs.append(s)

        row_ths = np.array(row_ths)
        row_qs = np.array(row_qs)
        row_strs = np.array(row_strs)

        # d₁ of charge profile
        cn_q = 2 * np.mean(row_qs * np.cos(row_ths))
        sn_q = 2 * np.mean(row_qs * np.sin(row_ths))
        d1_q = np.sqrt(cn_q**2 + sn_q**2)

        # d₁ of stretch profile
        cn_s = 2 * np.mean(row_strs * np.cos(row_ths))
        sn_s = 2 * np.mean(row_strs * np.sin(row_ths))
        d1_s = np.sqrt(cn_s**2 + sn_s**2)

        print(f"  {Nv:4d}  {d1_q:12.6e}  {d1_q/ALPHA:10.4f}  "
              f"{d1_s:12.6f}  {d1_s/ALPHA:10.2f}")

    print()

    # ── Section 6: The stretch profile is the shape signal ─
    print("─" * 70)
    print("Section 6: Ring stretch profile — the shape distortion")
    print("  (How much each row's hexagons are stretched vs compressed)")
    print("─" * 70)
    print()

    N = 40  # high resolution for clean profile
    nds, adj_v = build_hex_torus(N, N, R, a)
    th1_v = nds[:, 0]
    unique_th1_v = np.sort(np.unique(np.round(th1_v, 8)))

    print(f"  N={N}, ε={eps}")
    print(f"  {'row':>4s}  {'θ₁':>7s}  {'stretch':>8s}  {'κ':>7s}  "
          f"{'1+ε·cosθ₁':>10s}  {'str/(1+εc)':>10s}")
    print(f"  {'─'*4}  {'─'*7}  {'─'*8}  {'─'*7}  "
          f"{'─'*10}  {'─'*10}")

    str_profile = []
    for i, th1_t in enumerate(unique_th1_v):
        ridx = np.where(np.abs(th1_v - th1_t) < 1e-6)[0]
        chars = [characterize_wye(ni, nds, adj_v, R, a) for ni in ridx]
        s = np.mean([c['ring_stretch'] for c in chars])
        kap = np.cos(th1_t) / (R + a * np.cos(th1_t))
        p = 1 + eps * np.cos(th1_t)  # metric factor

        str_profile.append(s)

        if i % 4 == 0 or i == len(unique_th1_v) - 1:
            print(f"  {i:4d}  {th1_t:7.3f}  {s:8.4f}  {kap:+7.3f}  "
                  f"{p:10.4f}  {s/p:10.4f}")

    print()

    # Is stretch ∝ (1 + ε cos θ₁)?
    str_arr = np.array(str_profile)
    p_arr = 1 + eps * np.cos(unique_th1_v)
    ratio = str_arr / p_arr
    print(f"  Is stretch ∝ (1 + ε cos θ₁)?")
    print(f"    stretch / (1 + ε cos θ₁): mean = {np.mean(ratio):.4f}, "
          f"std = {np.std(ratio):.4f}")
    print(f"    If std ≈ 0, stretch is exactly proportional to the metric factor.")
    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("  The Y-junction distortion pattern around the tube:")
    print("    Outer equator (θ₁=0):  short/wide hexagons, stretch > 1")
    print("    Top/bottom (θ₁=π/2):   nearly regular, stretch ≈ 1")
    print("    Inner equator (θ₁=π):  tall/skinny hexagons, stretch < 1")
    print()
    print("  The ring stretch is proportional to the metric factor")
    print("  p = 1 + ε cos θ₁, which is the local ring circumference")
    print("  relative to the mean.")
    print()
    print("  The CP charge (E·ρ̂) per row varies with θ₁ and should")
    print("  have a dominant d₁ Fourier component if charge comes from")
    print("  the inner-outer asymmetry (the defining feature of the torus).")
    print()
    print(f"  α = {ALPHA:.6e}")
    print(f"  e = √(4πα) = {E_CHARGE:.6f}")
    print()
    print("Track 12 Step 4 complete.")


if __name__ == "__main__":
    main()
