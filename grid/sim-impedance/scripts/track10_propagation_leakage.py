#!/usr/bin/env python3
"""
Track 10 — Propagation leakage: inject a signal at one edge
of a hexagonal torus lattice, propagate it junction-by-junction,
and track how much energy leaks into the surface-normal direction
at each step.

Three methods:
  A — Raw geometric decomposition (solve 3×3 system)
  B — Energy-normalized decomposition (rescale to conserve energy)
  C — S-matrix amplitudes with direction tracking
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


# ── Torus geometry ───────────────────────────────────────

def torus_pos(th1, th2, R, a):
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    rr = R + a * ct1
    return np.array([rr * cp, a * st1, rr * sp])


def torus_surface_normal(th1, th2):
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    return np.array([ct1 * cp, st1, ct1 * sp])


# ── Honeycomb lattice ────────────────────────────────────

def build_honeycomb_torus(N1, N2, R, a):
    """
    Build honeycomb lattice on torus.
    Returns positions (M,3), angles (M,2), neighbors list.
    Each node has exactly 3 neighbors.
    """
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


def edge_direction(positions, i, j):
    """Unit vector from node i to node j."""
    d = positions[j] - positions[i]
    return d / np.linalg.norm(d)


# ── Method A: Raw geometric decomposition ────────────────

def propagate_method_A(positions, angles, neighbors, start_edge, K_max):
    """
    At each junction, solve [ê_a | ê_b | n̂] · [a,b,n] = A × ê_in.
    Propagate a, b to next junctions.  Track normal leakage.
    """
    M = len(positions)

    # Active signals: dict mapping directed edge (src, dst) → amplitude
    active = {start_edge: 1.0}

    step_data = []

    for step in range(K_max):
        new_active = {}
        normal_leakage_step = 0.0
        normal_energy_step = 0.0
        total_inplane_energy = 0.0
        n_processed = 0

        for (src, dst), amp in active.items():
            if abs(amp) < 1e-15:
                continue

            e_in = edge_direction(positions, src, dst)
            v_in = amp * e_in

            # Two outgoing edges (not back to src)
            out_nbrs = [n for n in neighbors[dst] if n != src]
            if len(out_nbrs) < 2:
                continue

            e_a = edge_direction(positions, dst, out_nbrs[0])
            e_b = edge_direction(positions, dst, out_nbrs[1])
            th1, th2 = angles[dst]
            n_hat = torus_surface_normal(th1, th2)

            # Solve [ê_a | ê_b | n̂] · [a,b,n] = v_in
            M3 = np.column_stack([e_a, e_b, n_hat])
            try:
                coeffs = np.linalg.solve(M3, v_in)
            except np.linalg.LinAlgError:
                continue

            a_out, b_out, n_out = coeffs

            normal_leakage_step += n_out
            normal_energy_step += n_out**2
            total_inplane_energy += a_out**2 + b_out**2

            key_a = (dst, out_nbrs[0])
            key_b = (dst, out_nbrs[1])
            new_active[key_a] = new_active.get(key_a, 0.0) + a_out
            new_active[key_b] = new_active.get(key_b, 0.0) + b_out
            n_processed += 1

        total_active_energy = sum(a**2 for a in new_active.values())

        step_data.append({
            "step": step,
            "n_active": len(active),
            "n_processed": n_processed,
            "normal_amp": normal_leakage_step,
            "normal_energy": normal_energy_step,
            "inplane_energy": total_inplane_energy,
            "active_energy": total_active_energy,
        })

        active = new_active

    return step_data


# ── Method B: Energy-normalized decomposition ────────────

def propagate_method_B(positions, angles, neighbors, start_edge, K_max):
    """
    Same as A, but rescale (a, b, n) so a² + b² + n² = A²
    at each junction.
    """
    active = {start_edge: 1.0}
    step_data = []

    for step in range(K_max):
        new_active = {}
        normal_energy_step = 0.0
        n_processed = 0

        for (src, dst), amp in active.items():
            if abs(amp) < 1e-15:
                continue

            e_in = edge_direction(positions, src, dst)
            v_in = amp * e_in

            out_nbrs = [n for n in neighbors[dst] if n != src]
            if len(out_nbrs) < 2:
                continue

            e_a = edge_direction(positions, dst, out_nbrs[0])
            e_b = edge_direction(positions, dst, out_nbrs[1])
            th1, th2 = angles[dst]
            n_hat = torus_surface_normal(th1, th2)

            M3 = np.column_stack([e_a, e_b, n_hat])
            try:
                coeffs = np.linalg.solve(M3, v_in)
            except np.linalg.LinAlgError:
                continue

            a_out, b_out, n_out = coeffs

            # Rescale to conserve energy: a² + b² + n² = amp²
            raw_energy = a_out**2 + b_out**2 + n_out**2
            if raw_energy > 1e-30:
                scale = abs(amp) / np.sqrt(raw_energy)
                a_out *= scale
                b_out *= scale
                n_out *= scale

            normal_energy_step += n_out**2

            key_a = (dst, out_nbrs[0])
            key_b = (dst, out_nbrs[1])
            new_active[key_a] = new_active.get(key_a, 0.0) + a_out
            new_active[key_b] = new_active.get(key_b, 0.0) + b_out
            n_processed += 1

        total_active_energy = sum(a**2 for a in new_active.values())

        step_data.append({
            "step": step,
            "n_active": len(active),
            "normal_energy": normal_energy_step,
            "active_energy": total_active_energy,
        })

        active = new_active

    return step_data


# ── Method C: S-matrix with direction tracking ───────────

def propagate_method_C(positions, angles, neighbors, start_edge, K_max):
    """
    Use the Y-junction S-matrix (2/3 transmitted, -1/3 reflected)
    for scalar amplitudes.  Track the 3D signal direction and
    compute its surface-normal component as leakage.
    """
    # Active signals: (src, dst) → scalar amplitude
    active = {start_edge: 1.0}
    step_data = []

    for step in range(K_max):
        new_active = {}
        normal_energy_step = 0.0
        n_processed = 0

        for (src, dst), amp in active.items():
            if abs(amp) < 1e-15:
                continue

            out_nbrs = [n for n in neighbors[dst] if n != src]
            if len(out_nbrs) < 2:
                continue

            # S-matrix: 2/3 transmitted to each outgoing edge
            t_amp = (2.0 / 3.0) * amp

            # Direction tracking: the incoming signal direction
            e_in = edge_direction(positions, src, dst)
            th1, th2 = angles[dst]
            n_hat = torus_surface_normal(th1, th2)

            # Normal component of the incoming direction
            normal_proj = np.dot(e_in, n_hat)
            normal_energy_step += (amp * normal_proj)**2

            key_a = (dst, out_nbrs[0])
            key_b = (dst, out_nbrs[1])
            new_active[key_a] = new_active.get(key_a, 0.0) + t_amp
            new_active[key_b] = new_active.get(key_b, 0.0) + t_amp
            n_processed += 1

        total_active_energy = sum(a**2 for a in new_active.values())

        step_data.append({
            "step": step,
            "n_active": len(active),
            "normal_energy": normal_energy_step,
            "active_energy": total_active_energy,
        })

        active = new_active

    return step_data


# ── Main ─────────────────────────────────────────────────

def run_case(N, eps, K_max=None):
    """Run all three methods for one (N, ε) case."""
    R = 1.0
    a = eps * R
    if K_max is None:
        K_max = 3 * N

    positions, angs, neighbors = build_honeycomb_torus(N, N, R, a)
    M = len(positions)

    # Start edge: first node → its first neighbor
    start_edge = (0, neighbors[0][0])

    print(f"\n  N={N}, ε={eps:.1f}, nodes={M}, K_max={K_max}")
    print(f"  Start edge: {start_edge}")
    print(f"  Edge length: {np.linalg.norm(positions[start_edge[1]] - positions[start_edge[0]]):.4f}")

    data_A = propagate_method_A(positions, angs, neighbors, start_edge, K_max)
    data_B = propagate_method_B(positions, angs, neighbors, start_edge, K_max)
    data_C = propagate_method_C(positions, angs, neighbors, start_edge, K_max)

    return data_A, data_B, data_C


def print_method_summary(name, data, K_max):
    """Print summary for one method."""
    cum_normal = sum(d["normal_energy"] for d in data)
    print(f"    {name}:")
    print(f"      Cumulative normal energy: {cum_normal:.6e}")
    print(f"      Final active energy: {data[-1]['active_energy']:.6e}")
    if data[-1]['active_energy'] > 0:
        ratio = cum_normal / (cum_normal + data[-1]['active_energy'])
        print(f"      Normal fraction of total: {ratio:.6e}")
        print(f"      Normal fraction / α: {ratio / ALPHA:.4f}")

    # Per-step diagnostics for first few and last few steps
    print(f"      Step-by-step (first 5):")
    for d in data[:5]:
        print(f"        step={d['step']:3d}  "
              f"active_edges={d['n_active']:5d}  "
              f"normal_E={d['normal_energy']:.4e}  "
              f"active_E={d['active_energy']:.4e}")
    if len(data) > 10:
        print(f"      ... (skipping {len(data)-10} steps) ...")
    for d in data[-5:]:
        print(f"        step={d['step']:3d}  "
              f"active_edges={d['n_active']:5d}  "
              f"normal_E={d['normal_energy']:.4e}  "
              f"active_E={d['active_energy']:.4e}")


def main():
    print("Track 10: Propagation leakage")
    print(f"α = {ALPHA:.6e}")

    # ── Small test case first ────────────────────────────
    print("\n" + "="*60)
    print("  Small test: N=4, ε=0.5")
    print("="*60)

    data_A, data_B, data_C = run_case(4, 0.5, K_max=20)
    print_method_summary("Method A (raw decomposition)", data_A, 20)
    print_method_summary("Method B (energy-normalized)", data_B, 20)
    print_method_summary("Method C (S-matrix + direction)", data_C, 20)

    # ── Sweep over N and ε ───────────────────────────────
    print("\n" + "="*60)
    print("  Sweep: cumulative normal fraction after full circuit")
    print("="*60)

    eps_values = [0.3, 0.5, 0.7]
    N_values = [4, 6, 8, 10, 14]

    results = {method: [] for method in ["A", "B", "C"]}

    for eps in eps_values:
        for N in N_values:
            K_max = 3 * N
            dA, dB, dC = run_case(N, eps, K_max)

            for label, data in [("A", dA), ("B", dB), ("C", dC)]:
                cum_normal = sum(d["normal_energy"] for d in data)
                final_active = data[-1]["active_energy"]
                total = cum_normal + final_active
                frac = cum_normal / total if total > 0 else 0

                results[label].append({
                    "eps": eps, "N": N,
                    "cum_normal": cum_normal,
                    "final_active": final_active,
                    "frac": frac,
                })

    # Print summary table
    for label in ["A", "B", "C"]:
        method_names = {"A": "Raw decomposition",
                        "B": "Energy-normalized",
                        "C": "S-matrix + direction"}
        print(f"\n  Method {label}: {method_names[label]}")
        print(f"  {'ε':>4s}  {'N':>4s}  {'Σ n_E':>12s}  "
              f"{'active_E':>12s}  {'frac':>12s}  {'frac/α':>10s}")
        for r in results[label]:
            rat = r["frac"] / ALPHA if r["frac"] > 0 else 0
            print(f"  {r['eps']:4.1f}  {r['N']:4d}  "
                  f"{r['cum_normal']:12.4e}  "
                  f"{r['final_active']:12.4e}  "
                  f"{r['frac']:12.6e}  "
                  f"{rat:10.4f}")

    # ── Plot ─────────────────────────────────────────────
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    for ax, label in zip(axes, ["A", "B", "C"]):
        method_names = {"A": "Raw decomposition",
                        "B": "Energy-normalized",
                        "C": "S-matrix + direction"}
        for eps in eps_values:
            subset = [r for r in results[label] if r["eps"] == eps]
            Ns = [r["N"] for r in subset]
            fracs = [r["frac"] for r in subset]
            ax.plot(Ns, fracs, "o-", label=f"ε = {eps}")

        ax.axhline(ALPHA, color="red", ls="--", alpha=0.7,
                    label=f"α = {ALPHA:.4f}")
        ax.set_xlabel("N")
        ax.set_ylabel("Normal fraction")
        ax.set_title(f"Method {label}: {method_names[label]}")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_yscale("log")

    plt.tight_layout()
    plt.savefig(OUT / "track10_propagation_leakage.png", dpi=150)
    print(f"\n  Saved: {OUT / 'track10_propagation_leakage.png'}")

    # ── Step-by-step evolution for one case ──────────────
    print("\n" + "="*60)
    print("  Step-by-step: N=6, ε=0.5, Method B")
    print("="*60)

    dA, dB, dC = run_case(6, 0.5, K_max=30)

    fig2, axes2 = plt.subplots(1, 3, figsize=(16, 5))

    for ax, data, label in [(axes2[0], dA, "A"),
                             (axes2[1], dB, "B"),
                             (axes2[2], dC, "C")]:
        steps = [d["step"] for d in data]
        norm_e = [d["normal_energy"] for d in data]
        act_e = [d["active_energy"] for d in data]
        cum_norm = np.cumsum(norm_e)

        ax.semilogy(steps, norm_e, "b.-", label="Normal energy (step)", alpha=0.7)
        ax.semilogy(steps, act_e, "g.-", label="Active energy", alpha=0.7)
        ax.semilogy(steps, cum_norm, "r.-", label="Cumulative normal", alpha=0.7)
        ax.set_xlabel("Step")
        ax.set_ylabel("Energy")
        ax.set_title(f"Method {label}")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT / "track10_step_evolution.png", dpi=150)
    print(f"  Saved: {OUT / 'track10_step_evolution.png'}")

    print("\nDone.")


if __name__ == "__main__":
    main()
