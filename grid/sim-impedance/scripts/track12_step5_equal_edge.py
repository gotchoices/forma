#!/usr/bin/env python3
"""
Track 12 Step 5: Row characterization on equal-edge lattice.

Steps 1-4 used the conformal lattice where all hexagons are
identical in angular coordinates.  This produces stretch = 1.0
everywhere and zero charge — the wrong lattice for this analysis.

This step uses the spring-relaxed equal-edge lattice where:
  - 3D edge lengths are equalized
  - Inner equator hexagons are genuinely tall/skinny
  - Outer equator hexagons are genuinely short/wide
  - The shape distortion varies with latitude

Key questions:
  1. How does hexagon shape vary with θ₁ on the equal-edge lattice?
  2. Does the distortion profile have a convergent d₁ harmonic?
  3. Does the leakage correlate with the shape distortion?
  4. Does the charge (E·ρ̂) have a nonzero d₁ on this lattice?
"""

import numpy as np
from pathlib import Path

TAU = 2 * np.pi
ALPHA = 1 / 137.036
E_CHARGE = np.sqrt(4 * np.pi * ALPHA)


# ── Torus geometry ────────────────────────────────────────

def torus_pos(th1, th2, R, a):
    rr = R + a * np.cos(th1)
    return np.array([rr * np.cos(th2), a * np.sin(th1), rr * np.sin(th2)])

def torus_pos_vec(th1, th2, R, a):
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    rr = R + a * ct1
    return np.column_stack([rr * cp, a * st1, rr * sp])

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


# ── Honeycomb with equal-edge relaxation ──────────────────

def build_lattice(N1, N2):
    node_map = {}
    idx = 0
    init_th1 = []
    init_th2 = []
    for i1 in range(N1):
        for i2 in range(N2):
            for sub in range(2):
                node_map[(i1, i2, sub)] = idx
                init_th1.append(TAU * (i1 + 0.25 * sub) / N1)
                init_th2.append(TAU * (i2 + 0.5 * sub) / N2)
                idx += 1
    M = idx
    neighbors = [[] for _ in range(M)]
    for i1 in range(N1):
        for i2 in range(N2):
            A = node_map[(i1, i2, 0)]
            B = node_map[(i1, i2, 1)]
            neighbors[A].extend([B,
                                 node_map[(i1, (i2 - 1) % N2, 1)],
                                 node_map[((i1 - 1) % N1, i2, 1)]])
            neighbors[B].extend([A,
                                 node_map[(i1, (i2 + 1) % N2, 0)],
                                 node_map[((i1 + 1) % N1, i2, 0)]])
    edge_set = set()
    for i in range(M):
        for j in neighbors[i]:
            edge_set.add((min(i, j), max(i, j)))
    edge_arr = np.array(sorted(edge_set), dtype=int)
    angles = np.column_stack([init_th1, init_th2])
    return angles, neighbors, edge_arr, M


def relax_equal_edges(angles, edge_arr, R, a,
                      max_iter=5000, tol=0.003, lr=0.003):
    M = len(angles)
    ei = edge_arr[:, 0]
    ej = edge_arr[:, 1]

    for iteration in range(max_iter):
        pos = torus_pos_vec(angles[:, 0], angles[:, 1], R, a)
        diff = pos[ej] - pos[ei]
        lengths = np.linalg.norm(diff, axis=1)
        L_target = np.mean(lengths)
        rel_dev = np.std(lengths) / L_target

        if rel_dev < tol:
            break

        force_mag = 2.0 * (lengths - L_target)
        direction = diff / lengths[:, None]

        ct1, st1 = np.cos(angles[:, 0]), np.sin(angles[:, 0])
        cp, sp = np.cos(angles[:, 1]), np.sin(angles[:, 1])
        rr = R + a * ct1
        dp_dth1 = np.column_stack([-a * st1 * cp, a * ct1, -a * st1 * sp])
        dp_dth2 = np.column_stack([-rr * sp, np.zeros(M), rr * cp])

        dL_dth1_i = -np.sum(direction * dp_dth1[ei], axis=1)
        dL_dth2_i = -np.sum(direction * dp_dth2[ei], axis=1)
        dL_dth1_j = np.sum(direction * dp_dth1[ej], axis=1)
        dL_dth2_j = np.sum(direction * dp_dth2[ej], axis=1)

        grad = np.zeros((M, 2))
        np.add.at(grad[:, 0], ei, force_mag * dL_dth1_i)
        np.add.at(grad[:, 1], ei, force_mag * dL_dth2_i)
        np.add.at(grad[:, 0], ej, force_mag * dL_dth1_j)
        np.add.at(grad[:, 1], ej, force_mag * dL_dth2_j)

        angles -= lr * grad

    return angles, rel_dev, iteration


def build_equal_edge_torus(N1, N2, R, a):
    """Build honeycomb lattice with relaxed equal-edge lengths."""
    angles, neighbors, edge_arr, M = build_lattice(N1, N2)
    angles, dev, iters = relax_equal_edges(angles, edge_arr, R, a)

    pos = torus_pos_vec(angles[:, 0], angles[:, 1], R, a)
    nodes = np.column_stack([angles[:, 0], angles[:, 1], pos])

    adj = [[] for _ in range(M)]
    for (i, j) in edge_arr:
        vec = pos[j] - pos[i]
        adj[i].append((j, vec))
        adj[j].append((i, -vec))

    # Edge length statistics
    lengths = [np.linalg.norm(pos[j] - pos[i]) for i, j in edge_arr]

    return nodes, adj, neighbors, edge_arr, np.mean(lengths), np.std(lengths) / np.mean(lengths)


# ── Analysis functions ────────────────────────────────────

def wye_shape(node_idx, nodes, adj, R, a):
    """Characterize the Y-junction shape on the equal-edge lattice."""
    th1 = nodes[node_idx, 0]
    th2 = nodes[node_idx, 1]
    t1_hat, t2_hat = torus_tangents(th1, th2, R, a)
    n_hat = torus_normal(th1, th2)

    edge_vecs = [ev for (_, ev) in adj[node_idx]]
    lengths = [np.linalg.norm(ev) for ev in edge_vecs]
    e_hats = [ev / (L + 1e-30) for ev, L in zip(edge_vecs, lengths)]

    # Pairwise angles in 3D
    angles_3d = []
    for i in range(len(e_hats)):
        for j in range(i+1, len(e_hats)):
            cos_a = np.clip(np.dot(e_hats[i], e_hats[j]), -1, 1)
            angles_3d.append(np.degrees(np.arccos(cos_a)))

    # Decompose each edge into tube/ring/normal components
    tube_comps = [np.dot(eh, t1_hat) for eh in e_hats]
    ring_comps = [np.dot(eh, t2_hat) for eh in e_hats]
    normal_comps = [np.dot(eh, n_hat) for eh in e_hats]

    # Ring stretch: how spread are the ring components vs tube
    ring_span = max(abs(rc) for rc in ring_comps)
    tube_span = max(abs(tc) for tc in tube_comps)
    stretch = ring_span / (tube_span + 1e-30)

    # Edge length ratio
    L_ratio = max(lengths) / (min(lengths) + 1e-30)

    # Triple product (non-coplanarity)
    trip = abs(np.dot(e_hats[0], np.cross(e_hats[1], e_hats[2]))) if len(e_hats) >= 3 else 0

    return {
        'th1': th1, 'th2': th2,
        'angles': angles_3d,
        'mean_angle': np.mean(angles_3d),
        'angle_spread': max(angles_3d) - min(angles_3d),
        'stretch': stretch,
        'L_ratio': L_ratio,
        'lengths': lengths,
        'trip': trip,
        'tube_comps': tube_comps,
        'ring_comps': ring_comps,
        'normal_comps': normal_comps,
        'mean_abs_normal': np.mean([abs(nc) for nc in normal_comps]),
    }


def node_leakage_eq(node_idx, nodes, adj, R, a, n1=1, n2=2, n_phase=16):
    """Pure geometry leakage on equal-edge lattice."""
    th1 = nodes[node_idx, 0]
    th2 = nodes[node_idx, 1]
    t1, t2 = torus_tangents(th1, th2, R, a)
    edge_vecs = [ev for (_, ev) in adj[node_idx]]

    e_hats = []
    for ev in edge_vecs:
        n = np.linalg.norm(ev)
        e_hats.append(ev / n if n > 1e-15 else np.zeros(3))

    phases = np.linspace(0, TAU, n_phase, endpoint=False)
    leak_sum = 0.0

    for phase in phases:
        phi = n1 * th1 + n2 * th2 + phase
        E_vec = np.cos(phi) * t1 - np.sin(phi) * t2
        E2_in = np.dot(E_vec, E_vec)
        if E2_in < 1e-30:
            continue

        E_hat = E_vec / np.sqrt(E2_in)
        dots = [np.dot(E_hat, eh) for eh in e_hats]
        in_idx = np.argmin(dots)
        out_idx = [i for i in range(len(e_hats)) if i != in_idx]
        if len(out_idx) < 2:
            continue

        pn = np.cross(e_hats[out_idx[0]], e_hats[out_idx[1]])
        pn_mag = np.linalg.norm(pn)
        if pn_mag < 1e-15:
            continue
        pn = pn / pn_mag

        E_perp = np.dot(E_vec, pn)
        leak_sum += E_perp**2 / E2_in

    return leak_sum / n_phase


# ── Main ─────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("Track 12 Step 5: Equal-edge lattice row characterization")
    print("=" * 70)
    print()

    R = 1.0
    eps = 0.3
    a = eps * R

    # ── Section 1: Build and verify equal-edge lattice ─────
    print("─" * 70)
    print("Section 1: Equal-edge lattice construction")
    print("─" * 70)
    print()

    for N in [6, 10, 14, 20]:
        nodes, adj, nbrs, earr, L_mean, L_dev = build_equal_edge_torus(N, N, R, a)
        M = len(nodes)
        print(f"  N={N:3d}: {M} nodes, L_mean={L_mean:.4f}, "
              f"L_std/L_mean={L_dev:.4f} "
              f"({'GOOD' if L_dev < 0.05 else 'moderate'})")

    print()

    # ── Section 2: Row-by-row shape on equal-edge lattice ──
    print("─" * 70)
    print("Section 2: Y-junction shape at each latitude (equal-edge, N=20)")
    print("─" * 70)
    print()

    N = 20
    nodes, adj, _, _, L_mean, L_dev = build_equal_edge_torus(N, N, R, a)
    M = len(nodes)
    th1_vals = nodes[:, 0]

    # Bin into latitude bands (θ₁ bins of width π/10)
    n_bins = 20
    bin_edges = np.linspace(0, TAU, n_bins + 1)

    print(f"  {'bin':>4s}  {'θ₁_mid':>7s}  {'nodes':>6s}  {'stretch':>8s}  "
          f"{'L_ratio':>8s}  {'trip':>8s}  {'mn∠':>7s}  "
          f"{'∠spread':>8s}  {'mn|norm|':>9s}  {'leak':>12s}")
    print(f"  {'─'*4}  {'─'*7}  {'─'*6}  {'─'*8}  "
          f"{'─'*8}  {'─'*8}  {'─'*7}  "
          f"{'─'*8}  {'─'*9}  {'─'*12}")

    bin_data = []
    for b in range(n_bins):
        lo, hi = bin_edges[b], bin_edges[b+1]
        mid = (lo + hi) / 2
        in_bin = np.where((th1_vals >= lo) & (th1_vals < hi))[0]
        if len(in_bin) == 0:
            continue

        shapes = [wye_shape(ni, nodes, adj, R, a) for ni in in_bin]
        leaks = [node_leakage_eq(ni, nodes, adj, R, a, n_phase=16) for ni in in_bin]

        mean_stretch = np.mean([s['stretch'] for s in shapes])
        mean_Lratio = np.mean([s['L_ratio'] for s in shapes])
        mean_trip = np.mean([s['trip'] for s in shapes])
        mean_angle = np.mean([s['mean_angle'] for s in shapes])
        mean_spread = np.mean([s['angle_spread'] for s in shapes])
        mean_norm = np.mean([s['mean_abs_normal'] for s in shapes])
        mean_leak = np.mean(leaks)

        bin_data.append({
            'th1': mid, 'n_nodes': len(in_bin),
            'stretch': mean_stretch, 'L_ratio': mean_Lratio,
            'trip': mean_trip, 'mean_angle': mean_angle,
            'angle_spread': mean_spread, 'mean_norm': mean_norm,
            'leak': mean_leak,
        })

        print(f"  {b:4d}  {mid:7.3f}  {len(in_bin):6d}  "
              f"{mean_stretch:8.3f}  {mean_Lratio:8.3f}  "
              f"{mean_trip:8.5f}  {mean_angle:7.1f}  "
              f"{mean_spread:8.1f}  {mean_norm:9.5f}  {mean_leak:12.6e}")

    print()

    # ── Section 3: Fourier decomposition on equal-edge ─────
    print("─" * 70)
    print("Section 3: Fourier harmonics of distortion (equal-edge)")
    print("─" * 70)
    print()

    th1_arr = np.array([bd['th1'] for bd in bin_data])
    for measure_name in ['stretch', 'L_ratio', 'trip', 'leak', 'mean_norm']:
        vals = np.array([bd[measure_name] for bd in bin_data])
        d0 = np.mean(vals)
        harmonics = []
        for n in range(1, 6):
            cn = 2 * np.mean(vals * np.cos(n * th1_arr))
            sn = 2 * np.mean(vals * np.sin(n * th1_arr))
            harmonics.append(np.sqrt(cn**2 + sn**2))

        print(f"  {measure_name:>12s}: d₀={d0:10.5f}  "
              f"d₁={harmonics[0]:10.5f}  d₂={harmonics[1]:10.5f}  "
              f"d₃={harmonics[2]:10.5f}  "
              f"d₁/d₀={harmonics[0]/(d0+1e-30):8.4f}")

    print()

    # ── Section 4: Convergence of d₁ with N ────────────────
    print("─" * 70)
    print("Section 4: Does d₁ converge with N? (equal-edge lattice)")
    print("─" * 70)
    print()

    print(f"  {'N':>4s}  {'stretch_d₁':>12s}  {'Lratio_d₁':>12s}  "
          f"{'trip_d₁':>12s}  {'leak_d₁':>12s}  {'norm_d₁':>12s}")
    print(f"  {'─'*4}  {'─'*12}  {'─'*12}  "
          f"{'─'*12}  {'─'*12}  {'─'*12}")

    for Nv in [6, 8, 10, 14, 20]:
        nds, adj_v, _, _, _, _ = build_equal_edge_torus(Nv, Nv, R, a)
        Mv = len(nds)
        th1_v = nds[:, 0]

        # Bin
        n_bins_v = min(2 * Nv, 40)
        bin_edges_v = np.linspace(0, TAU, n_bins_v + 1)

        bin_th1 = []
        bin_stretch = []
        bin_Lratio = []
        bin_trip = []
        bin_leak = []
        bin_norm = []

        for b in range(n_bins_v):
            lo, hi = bin_edges_v[b], bin_edges_v[b+1]
            mid = (lo + hi) / 2
            in_bin = np.where((th1_v >= lo) & (th1_v < hi))[0]
            if len(in_bin) == 0:
                continue

            shapes = [wye_shape(ni, nds, adj_v, R, a) for ni in in_bin]
            leaks = [node_leakage_eq(ni, nds, adj_v, R, a, n_phase=16) for ni in in_bin]

            bin_th1.append(mid)
            bin_stretch.append(np.mean([s['stretch'] for s in shapes]))
            bin_Lratio.append(np.mean([s['L_ratio'] for s in shapes]))
            bin_trip.append(np.mean([s['trip'] for s in shapes]))
            bin_leak.append(np.mean(leaks))
            bin_norm.append(np.mean([s['mean_abs_normal'] for s in shapes]))

        bt = np.array(bin_th1)

        def d1(theta, values):
            cn = 2 * np.mean(np.array(values) * np.cos(theta))
            sn = 2 * np.mean(np.array(values) * np.sin(theta))
            return np.sqrt(cn**2 + sn**2)

        print(f"  {Nv:4d}  {d1(bt, bin_stretch):12.6f}  "
              f"{d1(bt, bin_Lratio):12.6f}  "
              f"{d1(bt, bin_trip):12.6f}  "
              f"{d1(bt, bin_leak):12.6f}  "
              f"{d1(bt, bin_norm):12.6f}")

    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("  The equal-edge lattice produces genuinely different hexagon")
    print("  shapes at different latitudes.  Key observations:")
    print()
    print("  1. Does stretch vary with θ₁? (tall/skinny vs short/wide)")
    print("  2. Does d₁ of any measure converge with N?")
    print("  3. Does leakage correlate with shape distortion?")
    print()
    print(f"  α = {ALPHA:.6e}")
    print()
    print("Track 12 Step 5 complete.")


if __name__ == "__main__":
    main()
