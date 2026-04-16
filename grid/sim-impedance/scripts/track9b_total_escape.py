#!/usr/bin/env python3
"""
Track 9b — Follow-up analysis: total escape and normal component.

Questions addressed:
1. Does the SUM of f_esc over all M nodes converge as N → ∞?
2. What fraction of the escape is in the surface-normal direction
   vs tangential to the surface?
3. If total escape converges, is it near α?
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "output"
OUT.mkdir(exist_ok=True)

ALPHA = 1 / 137.036
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


def compute_detailed_escape(positions, angles, neighbors):
    """
    For each node and each incoming edge, compute:
    - f_esc: total escape fraction = (ê_in · n̂_out_plane)²
    - f_normal: fraction of escape in surface-normal direction
    - f_tangential: fraction of escape tangential to surface
    - escape vector components
    """
    M = len(positions)

    per_node_f_esc = np.zeros(M)        # mean over 3 edges
    per_node_f_normal = np.zeros(M)     # normal component of escape
    per_node_f_tangential = np.zeros(M) # tangential component

    for i in range(M):
        pos_i = positions[i]
        nbrs = neighbors[i]
        e_hat = np.zeros((3, 3))
        for k in range(3):
            diff = positions[nbrs[k]] - pos_i
            e_hat[k] = diff / np.linalg.norm(diff)

        th1, th2 = angles[i]
        n_surf = torus_surface_normal(th1, th2)

        for inc in range(3):
            e_in = -e_hat[inc]
            out_idx = [k for k in range(3) if k != inc]
            e_out1 = e_hat[out_idx[0]]
            e_out2 = e_hat[out_idx[1]]

            cross = np.cross(e_out1, e_out2)
            cross_norm = np.linalg.norm(cross)
            if cross_norm < 1e-12:
                continue
            n_out = cross / cross_norm

            dot = np.dot(e_in, n_out)
            e_escape = dot * n_out  # escape vector

            f_esc = dot**2
            f_norm = np.dot(e_escape, n_surf)**2
            f_tang = f_esc - f_norm

            per_node_f_esc[i] += f_esc / 3
            per_node_f_normal[i] += f_norm / 3
            per_node_f_tangential[i] += max(f_tang, 0) / 3

    return per_node_f_esc, per_node_f_normal, per_node_f_tangential


def main():
    print("Track 9b: Total escape and normal component analysis")
    print(f"α = {ALPHA:.6e}")
    print()

    eps_values = [0.1, 0.2, 0.3, 0.5, 0.7, 1.0]
    N_values = [4, 6, 8, 10, 14, 20, 30, 40, 60]

    # ── Part 1: Does total escape converge? ──────────────

    print("="*75)
    print("  Part 1: Total escape  Σ f_esc  over all M nodes")
    print("="*75)
    print(f"  {'ε':>4s}  {'N':>4s}  {'M':>5s}  {'mean f_esc':>12s}  "
          f"{'Σ f_esc':>12s}  {'Σ f_norm':>12s}  {'norm/total':>10s}")
    print("-"*75)

    convergence_data = {}

    for eps in eps_values:
        R = 1.0
        a = eps * R
        convergence_data[eps] = {"N": [], "total": [], "total_norm": [],
                                  "mean": [], "M": []}

        for N in N_values:
            positions, angs, neighbors = build_honeycomb_torus(N, N, R, a)
            M = len(positions)
            f_esc, f_norm, f_tang = compute_detailed_escape(
                positions, angs, neighbors)

            total_esc = np.sum(f_esc)
            total_norm = np.sum(f_norm)
            mean_esc = np.mean(f_esc)
            norm_frac = total_norm / total_esc if total_esc > 0 else 0

            convergence_data[eps]["N"].append(N)
            convergence_data[eps]["total"].append(total_esc)
            convergence_data[eps]["total_norm"].append(total_norm)
            convergence_data[eps]["mean"].append(mean_esc)
            convergence_data[eps]["M"].append(M)

            print(f"  {eps:4.1f}  {N:4d}  {M:5d}  {mean_esc:12.6e}  "
                  f"{total_esc:12.4f}  {total_norm:12.4f}  {norm_frac:10.4f}")

        print()

    # ── Part 2: Convergence plot ─────────────────────────

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Total escape vs N
    ax = axes[0, 0]
    for eps in eps_values:
        d = convergence_data[eps]
        ax.plot(d["N"], d["total"], "o-", label=f"ε = {eps}")
    ax.axhline(1/ALPHA, color="red", ls="--", alpha=0.5, label="1/α = 137")
    ax.axhline(1.0, color="gray", ls=":", alpha=0.5)
    ax.set_xlabel("N")
    ax.set_ylabel("Σ f_esc (total over all nodes)")
    ax.set_title("Total escape vs lattice resolution")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Total normal escape vs N
    ax = axes[0, 1]
    for eps in eps_values:
        d = convergence_data[eps]
        ax.plot(d["N"], d["total_norm"], "o-", label=f"ε = {eps}")
    ax.axhline(ALPHA, color="red", ls="--", alpha=0.5, label=f"α = {ALPHA:.4f}")
    ax.set_xlabel("N")
    ax.set_ylabel("Σ f_normal (normal component)")
    ax.set_title("Total surface-normal escape vs N")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Mean escape vs N (log-log)
    ax = axes[1, 0]
    for eps in eps_values:
        d = convergence_data[eps]
        ax.plot(d["N"], d["mean"], "o-", label=f"ε = {eps}")
    ax.axhline(ALPHA, color="red", ls="--", alpha=0.5, label=f"α")
    ax.set_xlabel("N")
    ax.set_ylabel("Mean f_esc per node")
    ax.set_title("Mean per-node escape (log scale)")
    ax.set_yscale("log")
    ax.set_xscale("log")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Norm fraction vs N
    ax = axes[1, 1]
    for eps in eps_values:
        d = convergence_data[eps]
        norm_frac = [n/t if t > 0 else 0
                     for n, t in zip(d["total_norm"], d["total"])]
        ax.plot(d["N"], norm_frac, "o-", label=f"ε = {eps}")
    ax.set_xlabel("N")
    ax.set_ylabel("Normal fraction of total escape")
    ax.set_title("What fraction of escape is surface-normal?")
    ax.set_ylim(0, 1.1)
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT / "track9b_total_escape.png", dpi=150)
    print(f"Saved: {OUT / 'track9b_total_escape.png'}")

    # ── Part 3: Scaling analysis ─────────────────────────

    print()
    print("="*75)
    print("  Part 3: Scaling — does Σ f_esc converge?")
    print("="*75)
    for eps in eps_values:
        d = convergence_data[eps]
        totals = d["total"]
        Ns = d["N"]
        if len(totals) >= 2:
            last = totals[-1]
            second_last = totals[-2]
            change = abs(last - second_last) / abs(last) if last != 0 else 0
            print(f"  ε={eps:.1f}: Σ f_esc at N={Ns[-2]} → {second_last:.4f}, "
                  f"N={Ns[-1]} → {last:.4f}  "
                  f"(Δ = {change*100:.1f}%)")

    # ── Part 4: Power-law fit ────────────────────────────

    print()
    print("="*75)
    print("  Part 4: Power-law fit  f_esc_mean ~ N^(-p)")
    print("="*75)
    for eps in eps_values:
        d = convergence_data[eps]
        Ns = np.array(d["N"][2:], dtype=float)  # skip small N
        means = np.array(d["mean"][2:])
        if len(Ns) >= 3 and all(means > 0):
            coeffs = np.polyfit(np.log(Ns), np.log(means), 1)
            p = -coeffs[0]
            C = np.exp(coeffs[1])
            print(f"  ε={eps:.1f}: f_esc ~ {C:.4f} × N^(-{p:.3f})")
            if abs(p - 2) < 0.3:
                total_limit = C * TAU**2 / 2  # integral of C/N² × 2N²
                print(f"         → Σ f_esc converges to ~ {2*C:.4f}")
        else:
            print(f"  ε={eps:.1f}: insufficient data for fit")

    print("\nDone.")


if __name__ == "__main__":
    main()
