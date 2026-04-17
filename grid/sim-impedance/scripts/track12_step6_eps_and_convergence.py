#!/usr/bin/env python3
"""
Track 12 Step 6: ε dependence and tighter convergence.

Step 5 found leak_d₁ ≈ 0.053 at ε=0.3, N=20, with d₁/d₀ ≈ 0.99.
This step:
  A. Tightens the equal-edge relaxation for cleaner convergence
  B. Sweeps ε to find the functional form of leak_d₁(ε)
  C. Checks whether leak_d₁/ε or leak_d₁/ε² is constant
  D. Tests convergence with N at tighter tolerance
  E. Compares leak_d₁ to α, e, and simple functions
"""

import numpy as np
from pathlib import Path

TAU = 2 * np.pi
ALPHA = 1 / 137.036
E_CHARGE = np.sqrt(4 * np.pi * ALPHA)


def torus_pos_vec(th1, th2, R, a):
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    rr = R + a * ct1
    return np.column_stack([rr * cp, a * st1, rr * sp])

def torus_normal_scalar(th1, th2):
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    return np.array([ct1 * cp, st1, ct1 * sp])

def torus_tangents_scalar(th1, th2, R, a):
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    t1 = np.array([-st1 * cp, ct1, -st1 * sp])
    t2 = np.array([-sp, 0.0, cp])
    return t1 / (np.linalg.norm(t1) + 1e-30), t2 / (np.linalg.norm(t2) + 1e-30)


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
                      max_iter=8000, tol=0.002, lr=0.002):
    """Tighter tolerance than Step 5."""
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

    return angles, rel_dev


def build_ee_torus(N, R, a):
    """Build equal-edge torus, return nodes/adj/stats."""
    angles, nbrs, earr, M = build_lattice(N, N)
    angles, dev = relax_equal_edges(angles, earr, R, a)
    pos = torus_pos_vec(angles[:, 0], angles[:, 1], R, a)
    nodes = np.column_stack([angles[:, 0], angles[:, 1], pos])

    adj = [[] for _ in range(M)]
    for (i, j) in earr:
        vec = pos[j] - pos[i]
        adj[i].append((j, vec))
        adj[j].append((i, -vec))

    return nodes, adj, dev


def node_leakage(node_idx, nodes, adj, R, a, n1=1, n2=2, n_phase=16):
    th1 = nodes[node_idx, 0]
    th2 = nodes[node_idx, 1]
    t1, t2 = torus_tangents_scalar(th1, th2, R, a)
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


def compute_leak_d1(nodes, adj, R, a, n_bins=20, n_phase=16):
    """Compute the d₁ Fourier harmonic of the leakage profile."""
    M = len(nodes)
    th1_vals = nodes[:, 0]
    bin_edges = np.linspace(0, TAU, n_bins + 1)

    bin_th1 = []
    bin_leak = []

    for b in range(n_bins):
        lo, hi = bin_edges[b], bin_edges[b+1]
        mid = (lo + hi) / 2
        in_bin = np.where((th1_vals >= lo) & (th1_vals < hi))[0]
        if len(in_bin) == 0:
            continue
        leaks = [node_leakage(ni, nodes, adj, R, a, n_phase=n_phase)
                 for ni in in_bin]
        bin_th1.append(mid)
        bin_leak.append(np.mean(leaks))

    bt = np.array(bin_th1)
    bl = np.array(bin_leak)

    d0 = np.mean(bl)
    cn = 2 * np.mean(bl * np.cos(bt))
    sn = 2 * np.mean(bl * np.sin(bt))
    d1 = np.sqrt(cn**2 + sn**2)
    phase = np.degrees(np.arctan2(sn, cn))

    # Also d₂
    cn2 = 2 * np.mean(bl * np.cos(2 * bt))
    sn2 = 2 * np.mean(bl * np.sin(2 * bt))
    d2 = np.sqrt(cn2**2 + sn2**2)

    return d0, d1, d2, phase


def main():
    print("=" * 70)
    print("Track 12 Step 6: ε dependence and convergence")
    print("=" * 70)
    print()
    R = 1.0

    # ── Section A: ε sweep at fixed N=14 ──────────────────
    print("─" * 70)
    print("Section A: leak_d₁ vs ε (N=14, equal-edge)")
    print("─" * 70)
    print()

    N = 14
    print(f"  {'ε':>6s}  {'d₀':>10s}  {'d₁':>10s}  {'d₂':>10s}  "
          f"{'d₁/d₀':>8s}  {'d₁/ε':>10s}  {'d₁/ε²':>10s}  "
          f"{'d₁/α':>8s}  {'dev':>8s}")
    print(f"  {'─'*6}  {'─'*10}  {'─'*10}  {'─'*10}  "
          f"{'─'*8}  {'─'*10}  {'─'*10}  "
          f"{'─'*8}  {'─'*8}")

    eps_data = []
    for eps in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        a = eps * R
        nodes, adj, dev = build_ee_torus(N, R, a)
        d0, d1, d2, ph = compute_leak_d1(nodes, adj, R, a, n_bins=14)
        d1_eps = d1 / eps if eps > 0 else 0
        d1_eps2 = d1 / eps**2 if eps > 0 else 0

        eps_data.append((eps, d0, d1, d2, dev))
        print(f"  {eps:6.3f}  {d0:10.6f}  {d1:10.6f}  {d2:10.6f}  "
              f"{d1/(d0+1e-30):8.4f}  {d1_eps:10.4f}  {d1_eps2:10.2f}  "
              f"{d1/ALPHA:8.2f}  {dev:8.4f}")

    print()

    # Check if d₁/ε or d₁/ε² is constant
    d1_vals = [d[2] for d in eps_data]
    eps_vals = [d[0] for d in eps_data]
    d1_over_eps = [d1/e for d1, e in zip(d1_vals, eps_vals)]
    d1_over_eps2 = [d1/e**2 for d1, e in zip(d1_vals, eps_vals)]

    print(f"  d₁/ε  range: [{min(d1_over_eps):.4f}, {max(d1_over_eps):.4f}], "
          f"std/mean = {np.std(d1_over_eps)/np.mean(d1_over_eps):.3f}")
    print(f"  d₁/ε² range: [{min(d1_over_eps2):.2f}, {max(d1_over_eps2):.2f}], "
          f"std/mean = {np.std(d1_over_eps2)/np.mean(d1_over_eps2):.3f}")
    print()

    # ── Section B: Convergence with N at ε=0.3 ────────────
    print("─" * 70)
    print("Section B: Convergence with N (ε=0.3, equal-edge)")
    print("─" * 70)
    print()

    eps = 0.3
    a = eps * R

    print(f"  {'N':>4s}  {'d₀':>10s}  {'d₁':>10s}  {'d₂':>10s}  "
          f"{'d₁/d₀':>8s}  {'d₁/α':>8s}  {'dev':>8s}")
    print(f"  {'─'*4}  {'─'*10}  {'─'*10}  {'─'*10}  "
          f"{'─'*8}  {'─'*8}  {'─'*8}")

    conv_data = []
    for Nv in [6, 8, 10, 12, 14, 16, 20]:
        nodes, adj, dev = build_ee_torus(Nv, R, a)
        n_bins = max(8, 2 * Nv)
        d0, d1, d2, ph = compute_leak_d1(nodes, adj, R, a, n_bins=n_bins)
        conv_data.append((Nv, d0, d1, d2, dev))

        print(f"  {Nv:4d}  {d0:10.6f}  {d1:10.6f}  {d2:10.6f}  "
              f"{d1/(d0+1e-30):8.4f}  {d1/ALPHA:8.2f}  {dev:8.4f}")

    print()

    # ── Section C: Convergence at ε=0.5 ────────────────────
    print("─" * 70)
    print("Section C: Convergence with N (ε=0.5)")
    print("─" * 70)
    print()

    eps = 0.5
    a = eps * R

    print(f"  {'N':>4s}  {'d₀':>10s}  {'d₁':>10s}  {'d₁/d₀':>8s}  {'d₁/α':>8s}")
    print(f"  {'─'*4}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'*8}")

    for Nv in [6, 8, 10, 12, 14, 16, 20]:
        nodes, adj, dev = build_ee_torus(Nv, R, a)
        d0, d1, d2, ph = compute_leak_d1(nodes, adj, R, a, n_bins=max(8, 2*Nv))
        print(f"  {Nv:4d}  {d0:10.6f}  {d1:10.6f}  "
              f"{d1/(d0+1e-30):8.4f}  {d1/ALPHA:8.2f}")

    print()

    # ── Section D: Compare d₁ to known constants ──────────
    print("─" * 70)
    print("Section D: Compare converged d₁ to known constants")
    print("─" * 70)
    print()

    # Use the best N=14 values at several ε
    print("  At N=14:")
    for eps_v, d0_v, d1_v, d2_v, dev_v in eps_data:
        candidates = [
            ('α', ALPHA),
            ('ε/2π', eps_v / TAU),
            ('ε²/2', eps_v**2 / 2),
            ('ε/(4π)', eps_v / (4 * np.pi)),
            ('ε²/(4π)', eps_v**2 / (4 * np.pi)),
            ('α·ε', ALPHA * eps_v),
            ('ε/137', eps_v / 137),
            ('sin(ε)/2', np.sin(eps_v) / 2),
            ('ε²·π', eps_v**2 * np.pi),
        ]

        best = min(candidates, key=lambda c: abs(d1_v - c[1]) / (d1_v + 1e-30))
        err = (d1_v - best[1]) / (d1_v + 1e-30) * 100

        print(f"    ε={eps_v:.2f}: d₁ = {d1_v:.6f}, "
              f"closest = {best[0]} = {best[1]:.6f} ({err:+.1f}%)")

    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("  Key results:")
    print()

    # d₁ vs ε pattern
    print("  1. ε dependence of leak_d₁:")
    for eps_v, d0_v, d1_v, d2_v, dev_v in eps_data:
        print(f"     ε={eps_v:.2f}: d₁={d1_v:.6f}, d₁/ε={d1_v/eps_v:.4f}, "
              f"d₁/ε²={d1_v/eps_v**2:.2f}")

    print()
    print("  2. Convergence:")
    for Nv, d0_v, d1_v, d2_v, dev_v in conv_data:
        print(f"     N={Nv:3d}: d₁={d1_v:.6f}, d₁/α={d1_v/ALPHA:.2f}")

    print()
    print(f"  α = {ALPHA:.6e}")
    print(f"  e = √(4πα) = {E_CHARGE:.6f}")
    print()
    print("Track 12 Step 6 complete.")


if __name__ == "__main__":
    main()
