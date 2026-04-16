#!/usr/bin/env python3
"""
Tracks 9 & 10 — REDONE with equal-edge-length lattice.

Uses vectorized spring relaxation for performance.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import time

OUT = Path(__file__).resolve().parent.parent / "output"
OUT.mkdir(exist_ok=True)

ALPHA = 1 / 137.036
TAU = 2 * np.pi


# ── Torus geometry (vectorized) ──────────────────────────

def torus_pos_vec(th1, th2, R, a):
    """Vectorized: positions for arrays of (θ₁, θ₂)."""
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    rr = R + a * ct1
    return np.column_stack([rr * cp, a * st1, rr * sp])


def torus_normal_vec(th1, th2):
    """Vectorized: surface normals for arrays of (θ₁, θ₂)."""
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    return np.column_stack([ct1 * cp, st1, ct1 * sp])


# ── Honeycomb connectivity ───────────────────────────────

def build_lattice(N1, N2):
    """Build honeycomb connectivity and initial conformal angles."""
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
    edge_arr = np.array(sorted(edge_set), dtype=int)  # (E, 2)

    angles = np.column_stack([init_th1, init_th2])  # (M, 2)
    return angles, neighbors, edge_arr, M


# ── Vectorized spring relaxation ─────────────────────────

def relax_equal_edges(angles, edge_arr, R, a,
                      max_iter=3000, tol=0.003, lr=0.003):
    """Spring relaxation fully vectorized over edges."""
    M = len(angles)
    E = len(edge_arr)
    ei = edge_arr[:, 0]  # (E,)
    ej = edge_arr[:, 1]  # (E,)

    for iteration in range(max_iter):
        pos = torus_pos_vec(angles[:, 0], angles[:, 1], R, a)  # (M, 3)
        diff = pos[ej] - pos[ei]  # (E, 3)
        lengths = np.linalg.norm(diff, axis=1)  # (E,)
        L_target = np.mean(lengths)
        rel_dev = np.std(lengths) / L_target

        if rel_dev < tol:
            if iteration > 0:
                print(f"    Converged at iter {iteration}: "
                      f"std/mean={rel_dev:.6f}")
            break

        force_mag = 2.0 * (lengths - L_target)  # (E,)
        direction = diff / lengths[:, None]  # (E, 3) unit vectors

        # ∂p/∂θ₁ and ∂p/∂θ₂ for all nodes
        ct1, st1 = np.cos(angles[:, 0]), np.sin(angles[:, 0])
        cp, sp = np.cos(angles[:, 1]), np.sin(angles[:, 1])
        rr = R + a * ct1
        # dp/dth1 = (-a sin θ₁ cos θ₂, a cos θ₁, -a sin θ₁ sin θ₂)
        dp_dth1 = np.column_stack([-a * st1 * cp, a * ct1, -a * st1 * sp])
        # dp/dth2 = (-rr sin θ₂, 0, rr cos θ₂)
        dp_dth2 = np.column_stack([-rr * sp, np.zeros(M), rr * cp])

        # dL/dθ for node i: -(direction · dp/dθ_i)
        # dL/dθ for node j: +(direction · dp/dθ_j)
        dL_dth1_i = -np.sum(direction * dp_dth1[ei], axis=1)  # (E,)
        dL_dth2_i = -np.sum(direction * dp_dth2[ei], axis=1)
        dL_dth1_j = np.sum(direction * dp_dth1[ej], axis=1)
        dL_dth2_j = np.sum(direction * dp_dth2[ej], axis=1)

        # Accumulate gradients
        grad = np.zeros((M, 2))
        np.add.at(grad[:, 0], ei, force_mag * dL_dth1_i)
        np.add.at(grad[:, 1], ei, force_mag * dL_dth2_i)
        np.add.at(grad[:, 0], ej, force_mag * dL_dth1_j)
        np.add.at(grad[:, 1], ej, force_mag * dL_dth2_j)

        angles -= lr * grad
        angles[:, 0] %= TAU
        angles[:, 1] %= TAU

        if iteration % 500 == 0:
            print(f"    iter {iteration:4d}: L_std/mean={rel_dev:.6f} "
                  f"range=[{np.min(lengths):.5f}, {np.max(lengths):.5f}]")

    pos = torus_pos_vec(angles[:, 0], angles[:, 1], R, a)
    diff = pos[ej] - pos[ei]
    lengths = np.linalg.norm(diff, axis=1)
    print(f"    FINAL: L_mean={np.mean(lengths):.5f} "
          f"std/mean={np.std(lengths)/np.mean(lengths):.6f} "
          f"ratio={np.max(lengths)/np.min(lengths):.4f}")
    return angles


# ── Track 9: Escape fractions ────────────────────────────

def compute_escape(pos, angles, neighbors):
    """Per-node escape fraction."""
    M = len(pos)
    f_esc_avg = np.zeros(M)
    f_esc_normal = np.zeros(M)

    normals = torus_normal_vec(angles[:, 0], angles[:, 1])

    for i in range(M):
        nbrs = neighbors[i]
        e_hat = np.zeros((3, 3))
        for k in range(3):
            d = pos[nbrs[k]] - pos[i]
            e_hat[k] = d / np.linalg.norm(d)

        n_surf = normals[i]

        for inc in range(3):
            e_in = -e_hat[inc]
            oi = [k for k in range(3) if k != inc]
            cross = np.cross(e_hat[oi[0]], e_hat[oi[1]])
            cn = np.linalg.norm(cross)
            if cn < 1e-12:
                continue
            n_out = cross / cn
            dot = np.dot(e_in, n_out)
            f_esc_avg[i] += dot**2 / 3.0

            e_esc = dot * n_out
            f_esc_normal[i] += np.dot(e_esc, n_surf)**2 / 3.0

    return f_esc_avg, f_esc_normal


# ── Track 10: S-matrix propagation ───────────────────────

def propagate_smatrix(pos, angles, neighbors, start_edge, K_max):
    """S-matrix propagation with reflected wave included."""
    normals = torus_normal_vec(angles[:, 0], angles[:, 1])
    active = {start_edge: 1.0}
    cum_normal = 0.0

    for step in range(K_max):
        new_active = {}
        step_normal = 0.0

        for (src, dst), amp in active.items():
            if abs(amp) < 1e-15:
                continue

            # Direction tracking
            d = pos[dst] - pos[src]
            e_in = d / np.linalg.norm(d)
            normal_proj = np.dot(e_in, normals[dst])
            step_normal += (amp * normal_proj)**2

            out_nbrs = [n for n in neighbors[dst] if n != src]

            # S-matrix: 2/3 transmitted, -1/3 reflected
            t_amp = (2.0 / 3.0) * amp
            r_amp = (-1.0 / 3.0) * amp

            for nbr in out_nbrs:
                key = (dst, nbr)
                new_active[key] = new_active.get(key, 0.0) + t_amp
            key_r = (dst, src)
            new_active[key_r] = new_active.get(key_r, 0.0) + r_amp

        cum_normal += step_normal
        active = new_active

    total_active = sum(a**2 for a in active.values())
    return cum_normal, total_active


# ── Main ─────────────────────────────────────────────────

def main():
    print("Tracks 9 & 10: REDONE with equal-edge-length lattice")
    print(f"α = {ALPHA:.6e}\n")

    eps_values = [0.3, 0.5, 0.7]
    N_values = [4, 6, 8, 10, 14, 20, 30, 40]

    results = []

    for eps in eps_values:
        R = 1.0
        a = eps * R
        for N in N_values:
            t0 = time.time()
            print(f"--- N={N}, ε={eps} ---")
            angs, neighbors, edge_arr, M = build_lattice(N, N)

            angs = relax_equal_edges(angs, edge_arr, R, a,
                                     max_iter=4000, tol=0.003,
                                     lr=0.002)

            pos = torus_pos_vec(angs[:, 0], angs[:, 1], R, a)

            # Junction angle stats
            all_ang = []
            for i in range(M):
                nbrs = neighbors[i]
                es = []
                for k in range(3):
                    d = pos[nbrs[k]] - pos[i]
                    es.append(d / np.linalg.norm(d))
                for p in range(3):
                    for q in range(p+1, 3):
                        all_ang.append(np.degrees(
                            np.arccos(np.clip(np.dot(es[p], es[q]), -1, 1))))
            all_ang = np.array(all_ang)

            # Track 9
            f_esc, f_norm = compute_escape(pos, angs, neighbors)
            mean_f = np.mean(f_esc)
            total_f = np.sum(f_esc)
            total_fn = np.sum(f_norm)

            # Track 10 (skip for N > 20 — too many active edges)
            cum_n, act_e, frac10 = 0, 0, 0
            if N <= 20:
                K_max = 3 * N
                start = (0, neighbors[0][0])
                cum_n, act_e = propagate_smatrix(
                    pos, angs, neighbors, start, K_max)
                total = cum_n + act_e
                frac10 = cum_n / total if total > 0 else 0

            dt = time.time() - t0

            results.append({
                "eps": eps, "N": N, "M": M,
                "mean_f": mean_f, "total_f": total_f,
                "total_fn": total_fn,
                "angle_mean": np.mean(all_ang),
                "angle_std": np.std(all_ang),
                "angle_min": np.min(all_ang),
                "angle_max": np.max(all_ang),
                "cum_n": cum_n, "act_e": act_e, "frac10": frac10,
                "dt": dt,
            })

            print(f"  T9: mean_f={mean_f:.6e}  Σf={total_f:.4f}  "
                  f"f/α={mean_f/ALPHA:.4f}")
            if N <= 20:
                print(f"  T10: frac={frac10:.6e}  frac/α={frac10/ALPHA:.4f}")
            print(f"  angles: {np.mean(all_ang):.1f}±{np.std(all_ang):.1f}°  "
                  f"[{np.min(all_ang):.1f}, {np.max(all_ang):.1f}]")
            print(f"  ({dt:.1f}s)")

    # ── Summary ──────────────────────────────────────────
    print("\n" + "="*75)
    print("  SUMMARY: Track 9 — Per-node escape (equal-edge lattice)")
    print("="*75)
    print(f"  {'ε':>4s}  {'N':>4s}  {'M':>5s}  {'mean f_esc':>12s}  "
          f"{'Σ f_esc':>10s}  {'Σ f_norm':>10s}  {'f/α':>8s}  "
          f"{'angles':>16s}")
    for r in results:
        print(f"  {r['eps']:4.1f}  {r['N']:4d}  {r['M']:5d}  "
              f"{r['mean_f']:12.6e}  "
              f"{r['total_f']:10.4f}  "
              f"{r['total_fn']:10.4f}  "
              f"{r['mean_f']/ALPHA:8.4f}  "
              f"{r['angle_mean']:5.1f}±{r['angle_std']:4.1f}°")

    print("\n" + "="*75)
    print("  SUMMARY: Track 10 — S-matrix propagation (equal-edge)")
    print("="*75)
    print(f"  {'ε':>4s}  {'N':>4s}  {'cum_norm':>12s}  "
          f"{'active_E':>12s}  {'frac':>12s}  {'frac/α':>10s}")
    for r in results:
        if r["N"] <= 20:
            rat = r["frac10"] / ALPHA if r["frac10"] > 0 else 0
            print(f"  {r['eps']:4.1f}  {r['N']:4d}  "
                  f"{r['cum_n']:12.4e}  "
                  f"{r['act_e']:12.4e}  "
                  f"{r['frac10']:12.6e}  "
                  f"{rat:10.4f}")

    # ── Plots ────────────────────────────────────────────
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    ax = axes[0]
    for eps in eps_values:
        s = [r for r in results if r["eps"] == eps]
        ax.plot([r["N"] for r in s], [r["mean_f"] for r in s],
                "o-", label=f"ε={eps}")
    ax.axhline(ALPHA, color="red", ls="--", alpha=0.7, label="α")
    ax.set_xlabel("N")
    ax.set_ylabel("Mean f_esc per node")
    ax.set_title("Track 9: Per-node escape")
    ax.set_yscale("log")
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    for eps in eps_values:
        s = [r for r in results if r["eps"] == eps]
        ax.plot([r["N"] for r in s], [r["total_f"] for r in s],
                "o-", label=f"ε={eps}")
    ax.set_xlabel("N")
    ax.set_ylabel("Σ f_esc")
    ax.set_title("Track 9: Total escape")
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[2]
    for eps in eps_values:
        s = [r for r in results if r["eps"] == eps and r["N"] <= 20]
        ax.plot([r["N"] for r in s], [r["frac10"] for r in s],
                "o-", label=f"ε={eps}")
    ax.axhline(ALPHA, color="red", ls="--", alpha=0.7, label="α")
    ax.set_xlabel("N")
    ax.set_ylabel("Normal fraction")
    ax.set_title("Track 10: S-matrix propagation")
    ax.set_yscale("log")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT / "track9_10_equal_edge.png", dpi=150)
    print(f"\nSaved: {OUT / 'track9_10_equal_edge.png'}")
    print("Done.")


if __name__ == "__main__":
    main()
