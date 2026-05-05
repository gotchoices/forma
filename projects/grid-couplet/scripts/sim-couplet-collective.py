#!/usr/bin/env python3
"""
sim-couplet-collective — exploratory dynamics for chapter 2.

Question
--------
What does v2 dynamics produce on a closed loop of N couplets, and on
an open chain of M couplets?

The chapter examines whether closed loops behave dynamically as
emergent nodes and whether open chains behave as emergent edges.
This script implements the v2 update rules from chapter 1 §6 and
runs both topologies under representative initial conditions and
external drives, reporting collective behavior.

Status
------
Exploratory. Results inform chapter 2 prose; they are not the
derivation. Plots and printouts are for the agent's reference.

Conventions (per chapter 1)
---------------------------
- Each node i has its partner edge attached at phi_attach = 0 (its
  intrinsic zero); in a 1D array, the partner is the edge entering
  the node from its left (per viz/grid-lab geometry).
- The other connection (the next couplet's edge, leaving to the right)
  attaches at phi_attach = pi.
- v2 update (per clock cycle = inhale then exhale):
    Inhale (nodes):  phi_i += (1/k) * sum_j e_j * cos(phi_attach,j)
    Exhale (edges):  e_i  += k * (phi_tail - phi_head)
- For a 1D periodic array (mod N): node_i sees e_{i-1} at phi=0 and
  e_i at phi=pi, giving phi_i += (1/k) * (e_{i-1} - e_i).
  Edge_i has tail node_i, head node_{i+1}: e_i += k*(phi_i - phi_{i+1}).
- For an open chain of M couplets, the trailing edge (edge_{M-1}) is
  a stub per grid-lab; node_0 has only e_0 (at phi=pi); node_{M-1}
  has only e_{M-2} (at phi=0).

Run
---
    cd projects/grid-couplet/scripts
    python sim-couplet-collective.py

Output
------
    output/<test>.png  — time-evolution plots
    output/notes.txt   — collected numerical findings
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)

K = 1.0  # translation factor (default per chapter 1 §6)
NOTES = []


def note(msg):
    print(msg)
    NOTES.append(msg)


# ---------- v2 update rules ----------

def v2_step_periodic(phi, e):
    """One clock cycle (inhale + exhale) for a periodic loop of N couplets."""
    e_prev = np.roll(e, 1)                       # e_{i-1}
    phi_new = phi + (1.0 / K) * (e_prev - e)     # node update
    phi_next = np.roll(phi_new, -1)              # phi_{i+1}
    e_new = e + K * (phi_new - phi_next)         # edge update
    return phi_new, e_new


def v2_step_open(phi, e):
    """One clock cycle for an open chain of M couplets (edge[M-1] is a stub)."""
    M = len(phi)
    phi_new = np.copy(phi)
    # node 0: only e[0] at phi_attach = pi
    phi_new[0] = phi[0] + (1.0 / K) * (-e[0])
    # interior nodes: e[i-1] at phi=0 plus e[i] at phi=pi
    for i in range(1, M - 1):
        phi_new[i] = phi[i] + (1.0 / K) * (e[i - 1] - e[i])
    # node M-1: only e[M-2] at phi=0
    phi_new[M - 1] = phi[M - 1] + (1.0 / K) * (e[M - 2])
    # edges 0..M-2 update; edge M-1 stays inert (stub)
    e_new = np.copy(e)
    for i in range(M - 1):
        e_new[i] = e[i] + K * (phi_new[i] - phi_new[i + 1])
    return phi_new, e_new


# ---------- Run helpers ----------

def run_periodic(N, phi0, e0, T):
    phi, e = phi0.copy(), e0.copy()
    h_phi, h_e = [phi.copy()], [e.copy()]
    for _ in range(T):
        phi, e = v2_step_periodic(phi, e)
        h_phi.append(phi.copy())
        h_e.append(e.copy())
    return np.array(h_phi), np.array(h_e)


def run_open(M, phi0, e0, T):
    phi, e = phi0.copy(), e0.copy()
    h_phi, h_e = [phi.copy()], [e.copy()]
    for _ in range(T):
        phi, e = v2_step_open(phi, e)
        h_phi.append(phi.copy())
        h_e.append(e.copy())
    return np.array(h_phi), np.array(h_e)


def plot_dynamics(h_phi, h_e, fname, title):
    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    for i in range(h_phi.shape[1]):
        axes[0].plot(h_phi[:, i], label=f"node {i}", linewidth=0.8)
    for i in range(h_e.shape[1]):
        axes[1].plot(h_e[:, i], label=f"edge {i}", linewidth=0.8)
    axes[0].set_ylabel("Phases φ")
    axes[1].set_ylabel("Edges e")
    axes[1].set_xlabel("Step (full clock cycles)")
    axes[0].legend(loc="upper right", ncol=3, fontsize=7)
    axes[0].set_title(title)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, fname), dpi=100)
    plt.close()


# ---------- Tests ----------

def test_closed_loop_random():
    """A: closed loop, small random initial perturbation. What stabilizes?"""
    note("\n=== A: closed loop, random init ===")
    rng = np.random.default_rng(42)
    for N in [2, 3, 4, 6, 12]:
        phi0 = rng.normal(0, 0.1, N)
        e0 = rng.normal(0, 0.1, N)
        h_phi, h_e = run_periodic(N, phi0, e0, T=400)
        edge_sum = h_e.sum(axis=1)
        phi_mean = h_phi.mean(axis=1)
        note(f"N={N:2d}  edge_sum range=[{edge_sum.min():+.4g}, {edge_sum.max():+.4g}]"
             f"  phi_mean range=[{phi_mean.min():+.4g}, {phi_mean.max():+.4g}]"
             f"  final phi.std={h_phi[-1].std():.4g}")
        if N == 6:
            plot_dynamics(h_phi, h_e, "A-closed-N6-random.png",
                          f"Closed loop N={N}, random init")


def test_closed_loop_delta():
    """B: closed loop, single delta on phi_0. Propagation pattern?"""
    note("\n=== B: closed loop, delta init at node 0 ===")
    for N in [4, 6, 12]:
        phi0 = np.zeros(N); phi0[0] = 0.5
        e0 = np.zeros(N)
        h_phi, h_e = run_periodic(N, phi0, e0, T=300)
        # Phase winding: sum of phase differences around the loop / (2*pi)
        diffs = np.diff(np.concatenate([h_phi, h_phi[:, :1]], axis=1), axis=1)
        winding = diffs.sum(axis=1) / (2 * np.pi)
        edge_sum = h_e.sum(axis=1)
        note(f"N={N:2d}  edge_sum max|.|={np.abs(edge_sum).max():.4g}"
             f"  winding range=[{winding.min():+.4g}, {winding.max():+.4g}]"
             f"  final phi.mean={h_phi[-1].mean():+.4g}")
        if N == 6:
            plot_dynamics(h_phi, h_e, "B-closed-N6-delta.png",
                          f"Closed loop N={N}, delta init at node 0")


def test_open_chain_random():
    """C: open chain, random init. What stabilizes?"""
    note("\n=== C: open chain, random init ===")
    rng = np.random.default_rng(43)
    for M in [3, 4, 6, 12]:
        phi0 = rng.normal(0, 0.1, M)
        e0 = rng.normal(0, 0.1, M)
        e0[-1] = 0.0  # stub
        h_phi, h_e = run_open(M, phi0, e0, T=400)
        active_edge_sum = h_e[:, :-1].sum(axis=1)
        phi_mean = h_phi.mean(axis=1)
        endpoint_diff = h_phi[:, -1] - h_phi[:, 0]
        note(f"M={M:2d}  active edge_sum range=[{active_edge_sum.min():+.4g}, {active_edge_sum.max():+.4g}]"
             f"  endpoint phi diff range=[{endpoint_diff.min():+.4g}, {endpoint_diff.max():+.4g}]"
             f"  final phi.mean={h_phi[-1].mean():+.4g}")
        if M == 6:
            plot_dynamics(h_phi, h_e, "C-open-M6-random.png",
                          f"Open chain M={M}, random init")


def test_open_chain_pinned():
    """D: open chain with endpoints driven (pinned to fixed phases).

    This is the key reverse-construction test: external nodes pin both
    endpoints, and we ask whether the chain transmits the phase
    difference as if it were a single edge.
    """
    note("\n=== D: open chain, endpoints pinned ===")
    for M in [3, 4, 6, 12]:
        phi = np.zeros(M)
        e = np.zeros(M)
        pinned_left, pinned_right = 0.0, 1.0
        T = 1500
        h_phi, h_e = [phi.copy()], [e.copy()]
        for _ in range(T):
            phi, e = v2_step_open(phi, e)
            phi[0] = pinned_left            # external nodes pin endpoints
            phi[M - 1] = pinned_right
            h_phi.append(phi.copy())
            h_e.append(e.copy())
        h_phi = np.array(h_phi)
        h_e = np.array(h_e)
        # Steady-state diagnostics
        final_phi = h_phi[-1]
        final_e = h_e[-1]
        active_edge_sum = final_e[:-1].sum()
        # Expected if the chain behaves as a single edge under v2:
        # A single edge driven by two nodes phi_L, phi_R holds
        # value e_eff = k*(phi_L - phi_R) at steady state... but v2 is
        # additive without dissipation, so steady state requires
        # phi_tail = phi_head — no; instead examine the static
        # (Laplace) solution: phi linear from pinned_left to pinned_right.
        expected_dphi = (pinned_right - pinned_left) / (M - 1)
        note(f"M={M:2d}  final phi: {np.array2string(final_phi, precision=3)}")
        note(f"        expected uniform dphi (Laplace): {expected_dphi:+.4g}")
        note(f"        actual avg dphi: {np.diff(final_phi).mean():+.4g}")
        note(f"        final active edges: {np.array2string(final_e[:-1], precision=3)}")
        note(f"        sum of active edges: {active_edge_sum:+.4g}")
        if M == 6:
            plot_dynamics(h_phi, h_e, "D-open-M6-pinned.png",
                          f"Open chain M={M}, endpoints pinned 0 → 1")


def test_closed_loop_driven():
    """E: closed loop driven by an external edge attached to one node.

    Compare loop's mean-phase response to a single node driven by the
    same external edge. If the loop is operationally equivalent to a
    single node, the responses match.
    """
    note("\n=== E: closed loop driven by external edge vs single node ===")
    N = 6
    phi_attach = np.pi / 3   # away from 0 and pi to be a clean third coupling
    drive_freq = 0.02
    T = 800
    phi = np.zeros(N)
    e = np.zeros(N)
    phi_single = 0.0
    h_loop_mean = [phi.mean()]
    h_single = [phi_single]
    for t in range(T):
        e_ext = np.cos(2 * np.pi * drive_freq * t)
        # Loop step with extra contribution at node 0
        e_prev = np.roll(e, 1)
        phi_new = phi + (1.0 / K) * (e_prev - e)
        phi_new[0] += (1.0 / K) * e_ext * np.cos(phi_attach)
        phi_next = np.roll(phi_new, -1)
        e_new = e + K * (phi_new - phi_next)
        phi, e = phi_new, e_new
        h_loop_mean.append(phi.mean())
        # Single-node baseline (no other connections)
        phi_single = phi_single + (1.0 / K) * e_ext * np.cos(phi_attach)
        h_single.append(phi_single)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(h_loop_mean, label="Closed loop, mean phase")
    ax.plot(h_single, label="Single node (same drive)", linestyle="--")
    ax.set_xlabel("Step")
    ax.set_ylabel("Phase")
    ax.set_title(f"Closed loop (N={N}) vs single node, sinusoidal drive")
    ax.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "E-closed-vs-node-driven.png"), dpi=100)
    plt.close()
    note(f"  N={N} drive_freq={drive_freq}")
    note(f"  loop mean range=[{min(h_loop_mean):+.4g}, {max(h_loop_mean):+.4g}]")
    note(f"  single-node range=[{min(h_single):+.4g}, {max(h_single):+.4g}]")


def main():
    test_closed_loop_random()
    test_closed_loop_delta()
    test_open_chain_random()
    test_open_chain_pinned()
    test_closed_loop_driven()
    with open(os.path.join(OUTDIR, "notes.txt"), "w") as f:
        f.write("\n".join(NOTES) + "\n")
    print(f"\nNotes saved to {OUTDIR}/notes.txt")
    print(f"Plots saved to {OUTDIR}/")


if __name__ == "__main__":
    main()
