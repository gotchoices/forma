#!/usr/bin/env python3
"""
Diagnostic: what are the actual 3D angles at Y-junctions
on the torus?  And what decomposition coefficients (a, b, n)
result from the 3×3 solve?

Also: what angle would we get with equal edge lengths?
"""

import numpy as np

TAU = 2 * np.pi


def torus_pos(th1, th2, R, a):
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    rr = R + a * ct1
    return np.array([rr * cp, a * st1, rr * sp])


def torus_surface_normal(th1, th2):
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    return np.array([ct1 * cp, st1, ct1 * sp])


def build_honeycomb_torus(N1, N2, R, a):
    positions = []
    angles = []
    node_map = {}
    for i1 in range(N1):
        for i2 in range(N2):
            for sub in range(2):
                th1 = TAU * (i1 + 0.25 * sub) / N1
                th2 = TAU * (i2 + 0.5 * sub) / N2
                idx = len(positions)
                node_map[(i1, i2, sub)] = idx
                positions.append(torus_pos(th1, th2, R, a))
                angles.append([th1, th2])
    M = len(positions)
    neighbors = [[] for _ in range(M)]
    for i1 in range(N1):
        for i2 in range(N2):
            A = node_map[(i1, i2, 0)]
            B = node_map[(i1, i2, 1)]
            neighbors[A].append(B)
            neighbors[A].append(node_map[(i1, (i2 - 1) % N2, 1)])
            neighbors[A].append(node_map[((i1 - 1) % N1, i2, 1)])
            neighbors[B].append(A)
            neighbors[B].append(node_map[(i1, (i2 + 1) % N2, 0)])
            neighbors[B].append(node_map[((i1 + 1) % N1, i2, 0)])
    return np.array(positions), np.array(angles), neighbors


def analyze_junction(positions, angles, neighbors, node_idx):
    """Analyze a single junction: angles, edge lengths, decomposition."""
    pos = positions[node_idx]
    nbrs = neighbors[node_idx]
    th1, th2 = angles[node_idx]
    n_hat = torus_surface_normal(th1, th2)

    edges = []
    edge_lengths = []
    for k in range(3):
        diff = positions[nbrs[k]] - pos
        length = np.linalg.norm(diff)
        e_hat = diff / length
        edges.append(e_hat)
        edge_lengths.append(length)

    # 3D angles between edges (chord angles)
    angle_01 = np.degrees(np.arccos(np.clip(np.dot(edges[0], edges[1]), -1, 1)))
    angle_02 = np.degrees(np.arccos(np.clip(np.dot(edges[0], edges[2]), -1, 1)))
    angle_12 = np.degrees(np.arccos(np.clip(np.dot(edges[1], edges[2]), -1, 1)))

    # How much each edge is out of the tangent plane
    normal_proj = [np.dot(e, n_hat) for e in edges]

    # Decomposition: for each incoming edge, solve [e_a | e_b | n̂] [a,b,n] = -e_in
    decomp_results = []
    for inc in range(3):
        e_in = -edges[inc]  # incoming direction (pointing into node)
        out_idx = [k for k in range(3) if k != inc]
        e_a = edges[out_idx[0]]
        e_b = edges[out_idx[1]]
        M3 = np.column_stack([e_a, e_b, n_hat])
        try:
            coeffs = np.linalg.solve(M3, e_in)
        except np.linalg.LinAlgError:
            coeffs = [np.nan, np.nan, np.nan]
        a, b, n = coeffs
        energy_sum = a**2 + b**2 + n**2
        decomp_results.append((a, b, n, energy_sum))

    return {
        "th1": th1, "th2": th2,
        "edge_lengths": edge_lengths,
        "angles_3d": [angle_01, angle_02, angle_12],
        "normal_proj": normal_proj,
        "decomp": decomp_results,
    }


def main():
    print("Junction angle and decomposition diagnostic")
    print("="*70)

    for N in [4, 6, 10]:
        for eps in [0.3, 0.5, 0.7]:
            R = 1.0
            a = eps * R
            positions, angs, neighbors = build_honeycomb_torus(N, N, R, a)
            M = len(positions)

            print(f"\nN={N}, ε={eps}, nodes={M}")
            print("-"*70)

            # Analyze a few representative nodes
            # Outer equator (θ₁ ≈ 0), inner equator (θ₁ ≈ π), and mid
            sample_nodes = []
            for i in range(M):
                th1 = angs[i][0]
                # Outer equator: θ₁ near 0
                if abs(th1) < TAU / (4 * N):
                    sample_nodes.append(("outer", i))
                # Inner equator: θ₁ near π
                elif abs(th1 - np.pi) < TAU / (4 * N):
                    sample_nodes.append(("inner", i))
                # Mid: θ₁ near π/2
                elif abs(th1 - np.pi/2) < TAU / (4 * N):
                    sample_nodes.append(("mid", i))

            # Take first of each type
            seen = set()
            for label, idx in sample_nodes:
                if label in seen:
                    continue
                seen.add(label)

                info = analyze_junction(positions, angs, neighbors, idx)
                print(f"  {label} equator (θ₁={info['th1']:.3f}):")
                print(f"    Edge lengths: {info['edge_lengths'][0]:.4f}, "
                      f"{info['edge_lengths'][1]:.4f}, "
                      f"{info['edge_lengths'][2]:.4f}")
                print(f"    3D angles: {info['angles_3d'][0]:.2f}°, "
                      f"{info['angles_3d'][1]:.2f}°, "
                      f"{info['angles_3d'][2]:.2f}°  "
                      f"(sum={sum(info['angles_3d']):.2f}°)")
                print(f"    Edge normal projections: "
                      f"{info['normal_proj'][0]:.4f}, "
                      f"{info['normal_proj'][1]:.4f}, "
                      f"{info['normal_proj'][2]:.4f}")
                print(f"    Decomposition (a, b, n, a²+b²+n²):")
                for inc, (a, b, n, e2) in enumerate(info['decomp']):
                    print(f"      edge {inc} incoming: a={a:+.4f} b={b:+.4f} "
                          f"n={n:+.4f}  Σ²={e2:.4f}")

            # Statistics over ALL nodes
            all_angles = []
            all_a = []
            all_b = []
            all_n = []
            all_e2 = []
            all_lengths = []
            for i in range(M):
                info = analyze_junction(positions, angs, neighbors, i)
                all_angles.extend(info["angles_3d"])
                all_lengths.extend(info["edge_lengths"])
                for a, b, n, e2 in info["decomp"]:
                    all_a.append(a)
                    all_b.append(b)
                    all_n.append(n)
                    all_e2.append(e2)

            all_angles = np.array(all_angles)
            all_lengths = np.array(all_lengths)
            all_a = np.array(all_a)
            all_b = np.array(all_b)
            all_n = np.array(all_n)
            all_e2 = np.array(all_e2)

            print(f"  Statistics over all {M} nodes:")
            print(f"    Angles: min={np.min(all_angles):.2f}° "
                  f"max={np.max(all_angles):.2f}° "
                  f"mean={np.mean(all_angles):.2f}° "
                  f"std={np.std(all_angles):.2f}°")
            print(f"    Edge lengths: min={np.min(all_lengths):.4f} "
                  f"max={np.max(all_lengths):.4f} "
                  f"ratio={np.max(all_lengths)/np.min(all_lengths):.3f}")
            print(f"    |a|: min={np.min(np.abs(all_a)):.4f} "
                  f"max={np.max(np.abs(all_a)):.4f} "
                  f"mean={np.mean(np.abs(all_a)):.4f}")
            print(f"    |b|: min={np.min(np.abs(all_b)):.4f} "
                  f"max={np.max(np.abs(all_b)):.4f} "
                  f"mean={np.mean(np.abs(all_b)):.4f}")
            print(f"    |n|: min={np.min(np.abs(all_n)):.4f} "
                  f"max={np.max(np.abs(all_n)):.4f} "
                  f"mean={np.mean(np.abs(all_n)):.4f}")
            print(f"    a²+b²+n²: min={np.min(all_e2):.4f} "
                  f"max={np.max(all_e2):.4f} "
                  f"mean={np.mean(all_e2):.4f}")

    print("\n\nFlat sheet reference (no curvature, ε=0):")
    print("  120° Y-junction decomposition:")
    e1 = np.array([1, 0, 0], dtype=float)
    e2 = np.array([-0.5, np.sqrt(3)/2, 0])
    e3 = np.array([-0.5, -np.sqrt(3)/2, 0])
    n_hat = np.array([0, 0, 1], dtype=float)
    e_in = -e1
    M3 = np.column_stack([e2, e3, n_hat])
    coeffs = np.linalg.solve(M3, e_in)
    print(f"  ê_in = -ê₁: a={coeffs[0]:.4f} b={coeffs[1]:.4f} n={coeffs[2]:.4f}")
    print(f"  a²+b²+n² = {sum(c**2 for c in coeffs):.4f}")
    print(f"  Angle between ê₂ and ê₃: {np.degrees(np.arccos(np.dot(e2, e3))):.2f}°")

    print("\nDone.")


if __name__ == "__main__":
    main()
