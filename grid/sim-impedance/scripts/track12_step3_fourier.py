#!/usr/bin/env python3
"""
Track 12 Step 3: Fourier decomposition of the distortion pattern.

Track 8 showed: charge requires CP synchronization — only the
component of leakage that varies at frequency n₁=1 around the
tube contributes to charge.  Higher harmonics cancel.

Step 2 showed: total leakage grows with N (not convergent).
But the total is dominated by the DC component (d₀).

This step asks: does the FIRST HARMONIC (d₁) of the distortion
pattern converge?  The d₁ component captures the inner-vs-outer
asymmetry of the torus — the thing that makes hexagons tall/skinny
on the inside and short/wide on the outside.

If d₁ converges and relates to α, it would mean:
  charge = (first harmonic of distortion pattern) × (geometric factor)
and the lattice-resolution dependence cancels out.
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


# ── Distortion measures at each node ─────────────────────

def node_distortions(node_idx, nodes, adj):
    """
    Compute multiple distortion measures at one node.
    Returns dict with:
      mean_angle_dev: mean |angle - 120°| in degrees
      triple_product: |ê₁ · (ê₂ × ê₃)| — non-coplanarity
      aspect_ratio: ratio of longest to shortest edge
      edge_length_std: std dev of edge lengths / mean
      angle_asymmetry: max_angle - min_angle (spread)
    """
    edge_vecs = [ev for (_, ev) in adj[node_idx]]
    n_edges = len(edge_vecs)

    lengths = [np.linalg.norm(ev) for ev in edge_vecs]
    e_hats = [ev / (L + 1e-30) for ev, L in zip(edge_vecs, lengths)]

    # Pairwise angles
    angles = []
    for i in range(n_edges):
        for j in range(i+1, n_edges):
            cos_a = np.clip(np.dot(e_hats[i], e_hats[j]), -1, 1)
            angles.append(np.degrees(np.arccos(cos_a)))

    # Triple product
    trip = abs(np.dot(e_hats[0], np.cross(e_hats[1], e_hats[2]))) if n_edges >= 3 else 0

    # Edge length variation
    mean_L = np.mean(lengths)
    std_L = np.std(lengths) / (mean_L + 1e-30)
    aspect = max(lengths) / (min(lengths) + 1e-30)

    return {
        'mean_angle_dev': np.mean([abs(a - 120) for a in angles]),
        'triple_product': trip,
        'aspect_ratio': aspect,
        'edge_std': std_L,
        'angle_spread': max(angles) - min(angles) if angles else 0,
        'angles': angles,
        'edge_lengths': lengths,
    }


def node_leakage(node_idx, nodes, adj, R, a, n1=1, n2=2, n_phase=16):
    """Pure geometry leakage at one node, time-averaged."""
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
    print("Track 12 Step 3: Fourier decomposition of distortion pattern")
    print("=" * 70)
    print()
    print("  Question: does the first Fourier harmonic (d₁) of the")
    print("  distortion pattern converge with N?")
    print()

    R = 1.0

    # ── Section 1: Distortion profile d(θ₁) ───────────────
    print("─" * 70)
    print("Section 1: Distortion profiles at multiple N (ε=0.3)")
    print("─" * 70)
    print()

    eps = 0.3
    a = eps * R

    fourier_results = {}

    for N in [4, 6, 8, 10, 14, 20, 30, 40]:
        nodes, adj = build_hex_torus(N, N, R, a)
        M = len(nodes)
        th1_vals = nodes[:, 0]

        # Group by θ₁ row
        unique_th1 = np.sort(np.unique(np.round(th1_vals, 8)))

        # Compute per-row averages of various distortion measures
        row_th1 = []
        row_leak = []
        row_trip = []
        row_angle_dev = []
        row_aspect = []
        row_angle_spread = []

        for th1_target in unique_th1:
            row_idx = np.where(np.abs(th1_vals - th1_target) < 1e-6)[0]
            if len(row_idx) == 0:
                continue

            leaks = []
            trips = []
            adevs = []
            aspects = []
            spreads = []

            for ni in row_idx:
                d = node_distortions(ni, nodes, adj)
                l = node_leakage(ni, nodes, adj, R, a, n_phase=16)
                leaks.append(l)
                trips.append(d['triple_product'])
                adevs.append(d['mean_angle_dev'])
                aspects.append(d['aspect_ratio'])
                spreads.append(d['angle_spread'])

            row_th1.append(th1_target)
            row_leak.append(np.mean(leaks))
            row_trip.append(np.mean(trips))
            row_angle_dev.append(np.mean(adevs))
            row_aspect.append(np.mean(aspects))
            row_angle_spread.append(np.mean(spreads))

        row_th1 = np.array(row_th1)
        row_leak = np.array(row_leak)
        row_trip = np.array(row_trip)
        row_angle_dev = np.array(row_angle_dev)
        row_aspect = np.array(row_aspect)
        row_angle_spread = np.array(row_angle_spread)

        # Fourier decomposition of each measure
        # d(θ₁) = d₀ + Σ dₙ cos(nθ₁) + eₙ sin(nθ₁)
        # For N_rows samples, compute up to harmonic N_rows/2

        def fourier_decompose(theta, values, n_harmonics=5):
            """Compute Fourier coefficients of values(theta)."""
            N_pts = len(theta)
            coeffs = {}
            # DC
            coeffs['d0'] = np.mean(values)
            # Harmonics
            for n in range(1, n_harmonics + 1):
                cn = 2 * np.mean(values * np.cos(n * theta))
                sn = 2 * np.mean(values * np.sin(n * theta))
                amplitude = np.sqrt(cn**2 + sn**2)
                coeffs[f'c{n}'] = cn
                coeffs[f's{n}'] = sn
                coeffs[f'a{n}'] = amplitude
            return coeffs

        measures = {
            'leakage': row_leak,
            'triple': row_trip,
            'angle_dev': row_angle_dev,
            'aspect': row_aspect,
            'angle_spread': row_angle_spread,
        }

        fourier_results[N] = {}
        for name, values in measures.items():
            fc = fourier_decompose(row_th1, values)
            fourier_results[N][name] = fc

    # ── Section 2: Fourier harmonics table ─────────────────
    print("─" * 70)
    print("Section 2: Fourier harmonics of distortion measures (ε=0.3)")
    print("─" * 70)
    print()

    for measure_name in ['leakage', 'triple', 'angle_dev', 'aspect', 'angle_spread']:
        print(f"  Measure: {measure_name}")
        print(f"  {'N':>4s}  {'d₀':>10s}  {'d₁':>10s}  {'d₂':>10s}  "
              f"{'d₃':>10s}  {'d₁/d₀':>10s}  {'d₁/α':>10s}")
        print(f"  {'─'*4}  {'─'*10}  {'─'*10}  {'─'*10}  "
              f"{'─'*10}  {'─'*10}  {'─'*10}")

        for N in sorted(fourier_results.keys()):
            fc = fourier_results[N][measure_name]
            d0 = fc['d0']
            d1 = fc['a1']
            d2 = fc['a2']
            d3 = fc['a3']
            ratio_d1_d0 = d1 / d0 if abs(d0) > 1e-30 else 0
            ratio_d1_alpha = d1 / ALPHA

            print(f"  {N:4d}  {d0:10.6f}  {d1:10.6f}  {d2:10.6f}  "
                  f"{d3:10.6f}  {ratio_d1_d0:10.4f}  {ratio_d1_alpha:10.2f}")

        print()

    # ── Section 3: Convergence of d₁ ───────────────────────
    print("─" * 70)
    print("Section 3: Does d₁ converge with N?")
    print("─" * 70)
    print()

    for measure_name in ['leakage', 'triple', 'angle_dev', 'aspect']:
        d1_values = []
        N_values = []
        for N in sorted(fourier_results.keys()):
            d1 = fourier_results[N][measure_name]['a1']
            d1_values.append(d1)
            N_values.append(N)

        # Check if d1 is converging, growing, or shrinking
        if len(d1_values) >= 3:
            first = d1_values[1]  # skip N=4 (too coarse)
            last = d1_values[-1]
            if first > 0 and last > 0:
                ratio = last / first
                if 0.5 < ratio < 2.0:
                    trend = "APPROXIMATELY CONVERGENT"
                elif ratio < 0.5:
                    trend = "DECREASING toward zero"
                else:
                    trend = "INCREASING (not convergent)"
            else:
                trend = "mixed signs"
        else:
            trend = "insufficient data"

        print(f"  {measure_name:>15s}: d₁ at N=6 = {d1_values[1]:.6f}, "
              f"d₁ at N=40 = {d1_values[-1]:.6f} → {trend}")

    print()

    # ── Section 4: ε dependence of d₁ ─────────────────────
    print("─" * 70)
    print("Section 4: ε dependence of d₁ (N=20)")
    print("─" * 70)
    print()

    N = 20
    print(f"  {'ε':>8s}  {'leak_d₁':>10s}  {'trip_d₁':>10s}  "
          f"{'adev_d₁':>10s}  {'leak_d₁/ε':>10s}  {'leak_d₁/α':>10s}")
    print(f"  {'─'*8}  {'─'*10}  {'─'*10}  "
          f"{'─'*10}  {'─'*10}  {'─'*10}")

    for eps_v in [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]:
        a_v = eps_v * R
        nodes, adj = build_hex_torus(N, N, R, a_v)
        th1_vals = nodes[:, 0]
        unique_th1 = np.sort(np.unique(np.round(th1_vals, 8)))

        row_th1 = []
        row_leak = []
        row_trip = []
        row_adev = []

        for th1_t in unique_th1:
            row_idx = np.where(np.abs(th1_vals - th1_t) < 1e-6)[0]
            if len(row_idx) == 0:
                continue

            leaks = [node_leakage(ni, nodes, adj, R, a_v, n_phase=16) for ni in row_idx]
            trips = []
            adevs = []
            for ni in row_idx:
                d = node_distortions(ni, nodes, adj)
                trips.append(d['triple_product'])
                adevs.append(d['mean_angle_dev'])

            row_th1.append(th1_t)
            row_leak.append(np.mean(leaks))
            row_trip.append(np.mean(trips))
            row_adev.append(np.mean(adevs))

        row_th1 = np.array(row_th1)

        def get_d1(theta, values):
            cn = 2 * np.mean(values * np.cos(theta))
            sn = 2 * np.mean(values * np.sin(theta))
            return np.sqrt(cn**2 + sn**2)

        ld1 = get_d1(row_th1, np.array(row_leak))
        td1 = get_d1(row_th1, np.array(row_trip))
        ad1 = get_d1(row_th1, np.array(row_adev))
        ld1_eps = ld1 / eps_v if eps_v > 0 else 0

        print(f"  {eps_v:8.3f}  {ld1:10.6f}  {td1:10.6f}  "
              f"{ad1:10.6f}  {ld1_eps:10.4f}  {ld1/ALPHA:10.2f}")

    print()

    # ── Section 5: The key test — d₁ × N convergence ──────
    print("─" * 70)
    print("Section 5: Does d₁ × N (or d₁ × N²) converge?")
    print("─" * 70)
    print()
    print("  If d₁ ~ 1/N, then d₁×N → const (geometric invariant)")
    print("  If d₁ ~ 1/N², then d₁×N² → const")
    print()

    eps = 0.3
    a = eps * R

    print(f"  ε = {eps}")
    print(f"  {'N':>4s}  {'leak_d₁':>10s}  {'d₁×N':>10s}  {'d₁×N²':>10s}  "
          f"{'trip_d₁':>10s}  {'td₁×N':>10s}  {'td₁×N²':>10s}")
    print(f"  {'─'*4}  {'─'*10}  {'─'*10}  {'─'*10}  "
          f"{'─'*10}  {'─'*10}  {'─'*10}")

    for N in [4, 6, 8, 10, 14, 20, 30, 40]:
        nodes, adj = build_hex_torus(N, N, R, a)
        th1_vals = nodes[:, 0]
        unique_th1 = np.sort(np.unique(np.round(th1_vals, 8)))

        row_th1 = []
        row_leak = []
        row_trip = []

        for th1_t in unique_th1:
            row_idx = np.where(np.abs(th1_vals - th1_t) < 1e-6)[0]
            if len(row_idx) == 0:
                continue

            leaks = [node_leakage(ni, nodes, adj, R, a, n_phase=16) for ni in row_idx]
            trips = []
            for ni in row_idx:
                d = node_distortions(ni, nodes, adj)
                trips.append(d['triple_product'])

            row_th1.append(th1_t)
            row_leak.append(np.mean(leaks))
            row_trip.append(np.mean(trips))

        row_th1 = np.array(row_th1)

        def get_d1(theta, values):
            cn = 2 * np.mean(values * np.cos(theta))
            sn = 2 * np.mean(values * np.sin(theta))
            return np.sqrt(cn**2 + sn**2)

        ld1 = get_d1(row_th1, np.array(row_leak))
        td1 = get_d1(row_th1, np.array(row_trip))

        print(f"  {N:4d}  {ld1:10.6f}  {ld1*N:10.4f}  {ld1*N**2:10.2f}  "
              f"{td1:10.6f}  {td1*N:10.4f}  {td1*N**2:10.2f}")

    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("  The distortion pattern d(θ₁) has Fourier harmonics:")
    print("    d₀ = average (DC component)")
    print("    d₁ = first harmonic (inner-outer asymmetry)")
    print("    d₂ = second harmonic (top-bottom modulation)")
    print()
    print("  Track 8 showed only the d₁ component contributes to charge")
    print("  (CP synchronization at frequency n₁=1).")
    print()
    print("  If d₁ × N converges: d₁ is a geometric invariant / N")
    print("    → the first harmonic of distortion is a property of")
    print("      the torus geometry, not the lattice resolution")
    print()
    print(f"  α = {ALPHA:.6e}")
    print(f"  e = √(4πα) = {E_CHARGE:.6f}")
    print()

    # Final check
    eps = 0.3
    a = eps * R
    for N in [20, 40]:
        nodes, adj = build_hex_torus(N, N, R, a)
        th1_vals = nodes[:, 0]
        unique_th1 = np.sort(np.unique(np.round(th1_vals, 8)))
        row_th1 = []
        row_leak = []
        for th1_t in unique_th1:
            row_idx = np.where(np.abs(th1_vals - th1_t) < 1e-6)[0]
            if len(row_idx) == 0:
                continue
            leaks = [node_leakage(ni, nodes, adj, R, a, n_phase=16) for ni in row_idx]
            row_th1.append(th1_t)
            row_leak.append(np.mean(leaks))
        row_th1 = np.array(row_th1)
        cn = 2 * np.mean(np.array(row_leak) * np.cos(row_th1))
        sn = 2 * np.mean(np.array(row_leak) * np.sin(row_th1))
        d1 = np.sqrt(cn**2 + sn**2)
        print(f"  N={N}: leakage d₁ = {d1:.6f}, d₁×N = {d1*N:.4f}, "
              f"d₁×N/α = {d1*N/ALPHA:.2f}")

    print()
    print("Track 12 Step 3 complete.")


if __name__ == "__main__":
    main()
