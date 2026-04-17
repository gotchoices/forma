#!/usr/bin/env python3
"""
Track 12 Step 2: Per-row and per-node charge/leakage analysis.

A hexagonal torus has N₁ rows of nodes around the tube.
Each row sits at a specific θ₁ and handles a specific slice
of the 2π tube rotation.  The bending between adjacent rows
is the turning angle Δθ₁.

Key computation:
  For each row, compute the mean distortion (deviation from
  flat 120° junctions).  Then compute the leakage (Track 11d
  pure geometry) at each node.  Plot leakage vs distortion.

If leakage = f(distortion) is a universal function (same at
all lattice resolutions N), then f encodes α.

Specifically: Σ f(distortion_k) over all nodes should equal
some quantity related to α, independent of N.
"""

import numpy as np
from pathlib import Path

TAU = 2 * np.pi
ALPHA = 1 / 137.036
E_CHARGE = np.sqrt(4 * np.pi * ALPHA)

OUT = Path(__file__).resolve().parent.parent / "output"
OUT.mkdir(exist_ok=True)


# ── Torus geometry ────────────────────────────────────────

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


# ── Hexagonal torus lattice ──────────────────────────────

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


# ── Per-node distortion and leakage ──────────────────────

def node_distortion(node_idx, nodes, adj):
    """
    Compute the distortion at one node.

    Returns:
      mean_angle_deviation: mean |angle - 120°| in degrees
      max_angle_deviation: max |angle - 120°| in degrees
      non_coplanarity: solid angle of the 3 edge directions (rad)
      turning_to_neighbors: mean turning angle to neighbors (deg)
    """
    edge_vecs = [ev for (_, ev) in adj[node_idx]]
    n_edges = len(edge_vecs)

    e_hats = []
    for ev in edge_vecs:
        n = np.linalg.norm(ev)
        e_hats.append(ev / n if n > 1e-15 else np.zeros(3))

    # Pairwise angles
    deviations = []
    for i in range(n_edges):
        for j in range(i+1, n_edges):
            cos_a = np.clip(np.dot(e_hats[i], e_hats[j]), -1, 1)
            ang = np.degrees(np.arccos(cos_a))
            deviations.append(abs(ang - 120.0))

    # Non-coplanarity: |ê₁ · (ê₂ × ê₃)| — the scalar triple product
    if n_edges >= 3:
        trip = abs(np.dot(e_hats[0], np.cross(e_hats[1], e_hats[2])))
    else:
        trip = 0.0

    # Turning angle to neighbors
    n_hat = torus_normal(nodes[node_idx, 0], nodes[node_idx, 1])
    turning = []
    for nid, _ in adj[node_idx]:
        n_hat_nb = torus_normal(nodes[nid, 0], nodes[nid, 1])
        cos_t = np.clip(np.dot(n_hat, n_hat_nb), -1, 1)
        turning.append(np.degrees(np.arccos(cos_t)))

    return {
        'mean_dev': np.mean(deviations) if deviations else 0,
        'max_dev': max(deviations) if deviations else 0,
        'triple_product': trip,
        'mean_turning': np.mean(turning) if turning else 0,
    }


def node_leakage(node_idx, nodes, adj, n_phase=32):
    """
    Pure geometry leakage at one node, time-averaged over CP wave phases.
    (Track 11d method)
    """
    th1 = nodes[node_idx, 0]
    th2 = nodes[node_idx, 1]
    R = 1.0
    eps = 0.3  # will be parameterized
    a = eps * R
    t1, t2 = torus_tangents(th1, th2, R, a)
    edge_vecs = [ev for (_, ev) in adj[node_idx]]

    e_hats = []
    for ev in edge_vecs:
        n = np.linalg.norm(ev)
        e_hats.append(ev / n if n > 1e-15 else np.zeros(3))

    phases = np.linspace(0, TAU, n_phase, endpoint=False)
    leak_sum = 0.0

    for phase in phases:
        phi = 1 * th1 + 2 * th2 + phase  # mode (1,2)
        E_vec = np.cos(phi) * t1 - np.sin(phi) * t2
        E2_in = np.dot(E_vec, E_vec)
        if E2_in < 1e-30:
            continue

        # Identify incoming edge (most anti-aligned)
        E_hat = E_vec / np.sqrt(E2_in)
        dots = [np.dot(E_hat, eh) for eh in e_hats]
        in_idx = np.argmin(dots)
        out_idx = [i for i in range(len(e_hats)) if i != in_idx]

        if len(out_idx) < 2:
            continue

        # Outgoing plane normal
        pn = np.cross(e_hats[out_idx[0]], e_hats[out_idx[1]])
        pn_mag = np.linalg.norm(pn)
        if pn_mag < 1e-15:
            continue
        pn = pn / pn_mag

        # Leakage = component perpendicular to outgoing plane
        E_perp = np.dot(E_vec, pn)
        leak_sum += E_perp**2 / E2_in

    return leak_sum / n_phase


# ── Main ─────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("Track 12 Step 2: Per-row and per-node analysis")
    print("=" * 70)
    print()

    R = 1.0
    eps = 0.3
    a = eps * R

    # ── Section 1: Row structure ───────────────────────────
    print("─" * 70)
    print("Section 1: Row structure of the hexagonal torus")
    print("─" * 70)
    print()
    print("  Each unit cell contributes 2 nodes at θ₁ positions:")
    print("  sub=0 at θ₁ = 2π·i₁/N₁, sub=1 at θ₁ = 2π·(i₁+0.25)/N₁")
    print("  So there are 2N₁ 'sub-rows' of N₂ nodes each.")
    print()

    for N in [4, 6, 10, 20]:
        nodes, adj = build_hex_torus(N, N, R, a)
        M = len(nodes)

        # Group nodes by θ₁ (into rows)
        th1_vals = nodes[:, 0]
        unique_th1 = np.sort(np.unique(np.round(th1_vals, 8)))
        n_rows = len(unique_th1)
        nodes_per_row = M // n_rows

        print(f"  N={N:3d}: {M} nodes, {n_rows} rows, {nodes_per_row} nodes/row")

        # Compute per-row distortion and leakage
        row_data = []
        for th1_target in unique_th1:
            row_indices = np.where(np.abs(th1_vals - th1_target) < 1e-6)[0]
            if len(row_indices) == 0:
                continue

            # Mean distortion for this row
            devs = []
            trips = []
            leaks = []
            for ni in row_indices:
                d = node_distortion(ni, nodes, adj)
                devs.append(d['mean_dev'])
                trips.append(d['triple_product'])
                l = node_leakage(ni, nodes, adj, n_phase=16)
                leaks.append(l)

            row_data.append({
                'th1': th1_target,
                'n_nodes': len(row_indices),
                'mean_dev': np.mean(devs),
                'mean_trip': np.mean(trips),
                'mean_leak': np.mean(leaks),
            })

        print(f"\n  {'row':>4s}  {'θ₁':>7s}  {'nodes':>6s}  {'mean|Δ∠|':>10s}  "
              f"{'triple':>10s}  {'leak':>12s}  {'leak/α':>10s}")
        print(f"  {'─'*4}  {'─'*7}  {'─'*6}  {'─'*10}  "
              f"{'─'*10}  {'─'*12}  {'─'*10}")

        for i, rd in enumerate(row_data):
            print(f"  {i:4d}  {rd['th1']:7.3f}  {rd['n_nodes']:6d}  "
                  f"{rd['mean_dev']:10.2f}  {rd['mean_trip']:10.6f}  "
                  f"{rd['mean_leak']:12.6e}  {rd['mean_leak']/ALPHA:10.4f}")

        # Total leakage
        total_leak = sum(rd['mean_leak'] * rd['n_nodes'] for rd in row_data)
        total_dev = sum(rd['mean_dev'] * rd['n_nodes'] for rd in row_data)
        print(f"\n  Total leakage (Σ per-node × count): {total_leak:.4f}")
        print(f"  Total leakage / α: {total_leak/ALPHA:.4f}")
        print(f"  Total leakage / (M × α): {total_leak/(M*ALPHA):.4f}")
        print()

    # ── Section 2: Leakage vs distortion — universal curve? ─
    print("─" * 70)
    print("Section 2: Leakage vs distortion — is f(distortion) universal?")
    print("─" * 70)
    print()
    print("  For each node, compute (distortion, leakage).")
    print("  Plot across multiple N values.")
    print("  If the points collapse onto one curve, f is universal.")
    print()

    all_points = {}  # N -> list of (distortion, leakage)

    for N in [4, 6, 10, 14, 20]:
        nodes, adj = build_hex_torus(N, N, R, a)
        M = len(nodes)

        points = []
        for ni in range(M):
            d = node_distortion(ni, nodes, adj)
            l = node_leakage(ni, nodes, adj, n_phase=16)
            points.append((d['mean_dev'], d['triple_product'], l))

        all_points[N] = points

        # Summary statistics
        devs = [p[0] for p in points]
        trips = [p[1] for p in points]
        leaks = [p[2] for p in points]

        print(f"  N={N:3d} ({M} nodes):")
        print(f"    Distortion range: [{min(devs):.1f}°, {max(devs):.1f}°]")
        print(f"    Triple product range: [{min(trips):.6f}, {max(trips):.6f}]")
        print(f"    Leakage range: [{min(leaks):.6e}, {max(leaks):.6e}]")
        print(f"    Σ leakage: {sum(leaks):.4f}, Σ/α = {sum(leaks)/ALPHA:.2f}")
        print()

    # ── Section 3: Ratio test — does Σ(leak)/M converge? ──
    print("─" * 70)
    print("Section 3: Does Σ(leakage) / M converge?  Or Σ(leakage) / N²?")
    print("─" * 70)
    print()

    print(f"  {'N':>4s}  {'M':>6s}  {'Σleak':>10s}  {'Σleak/M':>12s}  "
          f"{'Σleak/N²':>12s}  {'M×mean_leak':>12s}  "
          f"{'Σleak/α':>10s}")
    print(f"  {'─'*4}  {'─'*6}  {'─'*10}  {'─'*12}  "
          f"{'─'*12}  {'─'*12}  "
          f"{'─'*10}")

    for N in sorted(all_points.keys()):
        pts = all_points[N]
        M = len(pts)
        total = sum(p[2] for p in pts)
        mean = total / M
        print(f"  {N:4d}  {M:6d}  {total:10.4f}  {total/M:12.6e}  "
              f"{total/N**2:12.6e}  {M*mean:12.4f}  "
              f"{total/ALPHA:10.2f}")

    print()

    # ── Section 4: Leakage vs triple product (scatter) ─────
    print("─" * 70)
    print("Section 4: Leakage vs triple product — binned")
    print("  (Do different N values collapse onto one curve?)")
    print("─" * 70)
    print()

    # Bin by triple product and compute mean leakage per bin
    for N in sorted(all_points.keys()):
        pts = all_points[N]
        trips = np.array([p[1] for p in pts])
        leaks = np.array([p[2] for p in pts])

        # Sort by triple product
        order = np.argsort(trips)
        trips_s = trips[order]
        leaks_s = leaks[order]

        # Bin into quartiles
        n_bins = 4
        bin_size = len(pts) // n_bins
        print(f"  N={N:3d}:")
        for b in range(n_bins):
            lo = b * bin_size
            hi = (b + 1) * bin_size if b < n_bins - 1 else len(pts)
            mean_t = np.mean(trips_s[lo:hi])
            mean_l = np.mean(leaks_s[lo:hi])
            print(f"    bin {b}: trip=[{trips_s[lo]:.4f}..{trips_s[hi-1]:.4f}], "
                  f"mean_trip={mean_t:.4f}, mean_leak={mean_l:.6e}, "
                  f"leak/trip={mean_l/(mean_t+1e-30):.4f}")
        print()

    # ── Section 5: The brute force question ────────────────
    print("─" * 70)
    print("Section 5: Brute force — leakage per node at each θ₁")
    print("  Normalized by the node's share of 2π")
    print("─" * 70)
    print()
    print("  Each node's share of the 2π tube rotation = 2π / M_total")
    print("  The leakage at that node, divided by its angular share,")
    print("  gives 'leakage per radian of bending at this curvature'")
    print()

    for N in [6, 10, 20]:
        nodes, adj = build_hex_torus(N, N, R, a)
        M = len(nodes)
        share = TAU / M  # each node's share of the full 2π

        th1_vals = nodes[:, 0]

        # Group by θ₁ row and compute leakage per radian
        unique_th1 = np.sort(np.unique(np.round(th1_vals, 8)))

        print(f"  N={N:3d} ({M} nodes, share = {np.degrees(share):.2f}°/node):")
        print(f"    {'θ₁':>7s}  {'leak/node':>12s}  {'leak/share':>12s}  "
              f"{'curvature':>10s}")
        print(f"    {'─'*7}  {'─'*12}  {'─'*12}  {'─'*10}")

        for th1_target in unique_th1:
            row_idx = np.where(np.abs(th1_vals - th1_target) < 1e-6)[0]
            leaks_row = [node_leakage(ni, nodes, adj, n_phase=16) for ni in row_idx]
            mean_l = np.mean(leaks_row)

            # Local curvature of the torus at this θ₁
            # κ = cos(θ₁) / (R + a cos(θ₁))
            kappa = np.cos(th1_target) / (R + a * np.cos(th1_target))

            print(f"    {th1_target:7.3f}  {mean_l:12.6e}  "
                  f"{mean_l/share:12.6e}  {kappa:10.4f}")

        print()

    print("=" * 70)
    print("Track 12 Step 2 complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
