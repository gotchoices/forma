#!/usr/bin/env python3
"""
Track 8 — Aperture coupling: E-field leakage from bending
a hexagonal lattice into a torus.

Two computations:

Part A — CP vector field with ρ̂ projection:
  The CP field on the torus is tangential, so E · n̂_surface = 0
  exactly.  But E · ρ̂ (cylindrical radial) is NON-ZERO because
  the tangent plane tilts relative to the radial direction.
  The t̂₁ tangent vector has a ρ̂ component of -sin θ₁.
  This gives the charge selection rule: only n₁ = 1 produces
  net charge (CP synchronization with tube geometry).

Part B — Junction scattering on curved lattice:
  At each Y-junction, a wave arrives on one edge and scatters
  to the other two.  On a curved surface, the three edges are
  not coplanar.  The SCATTERING RESIDUAL — the difference
  between the flat-surface and curved-surface scattered fields —
  has a component in the ρ̂ direction.  This is the physical
  mechanism of "aperture coupling."
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


# ── Torus geometry helpers ───────────────────────────────

def torus_pos(th1, th2, R, a):
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    rr = R + a * ct1
    return np.array([rr * cp, a * st1, rr * sp])


def torus_tangents(th1, th2, R, a):
    """Unit tangent vectors and outward normal at (θ₁, θ₂)."""
    ct1, st1 = np.cos(th1), np.sin(th1)
    cp, sp = np.cos(th2), np.sin(th2)
    t1 = np.array([-st1 * cp, ct1, -st1 * sp])  # ∂/∂θ₁, length a
    t2 = np.array([-sp, 0.0, cp])                # ∂/∂θ₂, length R+a cos θ₁
    n_hat = np.array([ct1 * cp, st1, ct1 * sp])
    rho_hat = np.array([cp, 0.0, sp])             # cylindrical radial
    return t1, t2, n_hat, rho_hat


# ── Part A: Continuum CP field on discrete lattice ───────

def build_hex_torus(N1, N2, R, a):
    """
    Honeycomb lattice on a torus.
    Returns nodes (M,5), edges (E,2), and per-node geometric data.
    """
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
    edges = np.array(edges, dtype=int)
    return nodes, edges, node_map


def cp_field_rho_projection(N1, N2, eps, n1, n2, wave_type="traveling"):
    """
    Compute the CP field E · ρ̂ on a discrete hexagonal torus.

    The CP field at each node is:
      E_CP = cos(φ) × t̂₁ − sin(φ) × t̂₂
    where φ = n₁θ₁ + n₂θ₂.

    E_CP · ρ̂ = cos(φ) × (t̂₁ · ρ̂) = cos(φ) × (−sin θ₁)
    since t̂₂ · ρ̂ = 0.

    For traveling waves, we use the magnitude (time-averaged):
      |E_CP · ρ̂| = |cos((n₁−1)θ₁)| (the tube factor)
    """
    R = 1.0
    a = eps * R
    nodes, edges, _ = build_hex_torus(N1, N2, R, a)

    th1 = nodes[:, 0]
    th2 = nodes[:, 1]
    phi = n1 * th1 + n2 * th2

    if wave_type == "traveling":
        E_rho = np.cos((n1 - 1) * th1)
    else:
        E_rho = -np.sin(th1) * np.cos(phi)

    p = 1.0 + eps * np.cos(th1)
    dA = p / len(nodes) * (TAU * a) * (TAU * R)

    Q = np.sum(E_rho * dA)
    E_abs = np.sum(np.abs(E_rho) * dA)
    return Q, E_abs, E_rho, nodes


# ── Part B: Junction scattering residual ─────────────────

def junction_scattering_leakage(N1, N2, eps, n1, n2):
    """
    At each Y-junction on the curved torus, compute the scattering
    residual: the ρ̂ component of the vector difference between
    the curved-surface and flat-surface scattered fields.

    Physical picture:
    - Wave arrives at each junction from the "propagation direction"
    - Scatters to 3 edges with amplitudes from the junction rule
    - On a flat sheet: scattered E is in-plane
    - On a curved sheet: edge directions deviate → ρ̂ component

    For a CP mode, the propagation direction rotates around the tube,
    producing a θ₁-dependent ρ̂ leakage that integrates non-trivially.
    """
    R = 1.0
    a = eps * R
    nodes, edges, _ = build_hex_torus(N1, N2, R, a)
    n_nodes = len(nodes)

    # Build adjacency: for each node, list its connected edges and neighbors
    adj = [[] for _ in range(n_nodes)]
    for k, (i, j) in enumerate(edges):
        adj[i].append((k, j))
        adj[j].append((k, i))

    # At each node, compute:
    #   1. The CP field direction (in 3D)
    #   2. The edge directions (in 3D)
    #   3. Project CP field onto each edge → amplitude
    #   4. Weight each edge's ρ̂ component by its amplitude
    #   5. Sum → E_rho at this junction

    E_rho_junction = np.zeros(n_nodes)

    for node_idx in range(n_nodes):
        th1 = nodes[node_idx, 0]
        th2 = nodes[node_idx, 1]
        pos = nodes[node_idx, 2:5]

        t1_hat, t2_hat, n_hat, rho_hat = torus_tangents(th1, th2, R, a)

        phi = n1 * th1 + n2 * th2

        # CP field at this node (tangential vector in 3D)
        E_cp = np.cos(phi) * t1_hat - np.sin(phi) * t2_hat

        # For each connected edge, compute:
        #   - 3D edge direction
        #   - Amplitude = E_CP · ê_edge
        #   - ρ̂ contribution = amplitude × (ê_edge · ρ̂)
        E_rho_local = 0.0
        for edge_idx, neighbor_idx in adj[node_idx]:
            neighbor_pos = nodes[neighbor_idx, 2:5]
            edge_vec = neighbor_pos - pos
            edge_len = np.linalg.norm(edge_vec)
            if edge_len < 1e-15:
                continue
            e_hat = edge_vec / edge_len

            amplitude = np.dot(E_cp, e_hat)
            rho_component = np.dot(e_hat, rho_hat)
            E_rho_local += amplitude * rho_component

        E_rho_junction[node_idx] = E_rho_local

    # Integrate with area weighting
    th1_all = nodes[:, 0]
    p = 1.0 + eps * np.cos(th1_all)
    dA = p / n_nodes * (TAU * a) * (TAU * R)

    Q = np.sum(E_rho_junction * dA)
    Q_abs = np.sum(np.abs(E_rho_junction) * dA)

    return Q, Q_abs, E_rho_junction, nodes


# ── Main ─────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("Track 8: Aperture coupling — E-field leakage from bending")
    print("=" * 70)

    # ── Part A: CP field ρ̂ projection (reproduces R48) ───
    print("\n══ Part A: CP field E·ρ̂ on discrete lattice ══")
    print("  (Should reproduce R48: only n₁=1 gives net charge)")
    print()
    print(f"{'Mode':>8s}  {'Wave':>10s}  {'Q':>12s}  {'|Q|/Σ|E|dA':>12s}")
    print("-" * 50)

    eps = 0.3
    N = 40
    for n1, n2 in [(1, 2), (1, 3), (0, 1), (2, 4), (1, 1), (1, 5)]:
        for wt in ["traveling", "standing"]:
            Q, Ea, _, _ = cp_field_rho_projection(N, N, eps, n1, n2, wt)
            ratio = abs(Q) / Ea if Ea > 1e-30 else 0.0
            print(f"({n1},{n2})  {wt:>10s}  {Q:12.4f}  {ratio:12.6f}")

    # ── Part A2: n₁ selection rule ────────────────────────
    print("\n── Part A2: n₁ selection rule (traveling waves, ε=0.3) ──")
    print(f"{'Mode':>8s}  {'Q':>12s}  {'Expected':>12s}")
    print("-" * 40)
    for n1 in range(5):
        for n2 in [2, 3]:
            Q, _, _, _ = cp_field_rho_projection(N, N, eps, n1, n2, "traveling")
            expected = "nonzero" if n1 == 1 else "~zero"
            print(f"({n1},{n2})  {Q:12.4f}  {expected:>12s}")

    # ── Part B: Junction scattering leakage ───────────────
    print("\n══ Part B: Junction scattering E·ρ̂ leakage ══")
    print("  (CP field projected onto edges, then edges projected onto ρ̂)")
    print()
    print(f"{'Mode':>8s}  {'Q_junc':>12s}  {'Q_abs':>12s}  {'Q/Q_abs':>12s}")
    print("-" * 55)

    for n1, n2 in [(1, 2), (1, 3), (0, 1), (2, 4), (1, 1)]:
        Q, Qa, _, _ = junction_scattering_leakage(N, N, eps, n1, n2)
        ratio = Q / Qa if abs(Qa) > 1e-30 else 0.0
        print(f"({n1},{n2})  {Q:12.6f}  {Qa:12.4f}  {ratio:12.6e}")

    # ── Part B2: Convergence ──────────────────────────────
    print("\n── Part B2: Junction leakage convergence with N ──")
    print(f"{'N':>6s}  {'Q_junc':>12s}  {'Q_abs':>12s}  {'Q/Q_abs':>12s}")
    print("-" * 45)

    eps = 0.3
    for N in [10, 20, 30, 40, 60]:
        Q, Qa, _, _ = junction_scattering_leakage(N, N, eps, 1, 2)
        ratio = Q / Qa if abs(Qa) > 1e-30 else 0.0
        print(f"{N:6d}  {Q:12.6f}  {Qa:12.4f}  {ratio:12.6e}")

    # ── Part B3: ε sweep ──────────────────────────────────
    print("\n── Part B3: Junction leakage vs ε ──")
    print(f"{'ε':>8s}  {'Q_junc':>12s}  {'Q_abs':>12s}  {'Q/Q_abs':>12s}")
    print("-" * 50)

    N = 40
    eps_vals, ratios_eps = [], []
    for eps in [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]:
        Q, Qa, _, _ = junction_scattering_leakage(N, N, eps, 1, 2)
        ratio = Q / Qa if abs(Qa) > 1e-30 else 0.0
        eps_vals.append(eps)
        ratios_eps.append(ratio)
        print(f"{eps:8.3f}  {Q:12.6f}  {Qa:12.4f}  {ratio:12.6e}")

    # ── Part C: Comparison with α ─────────────────────────
    print("\n══ Part C: Comparison with α ══")
    eps = 0.3
    N = 40
    Q_cp, _, _, _ = cp_field_rho_projection(N, N, eps, 1, 2, "traveling")
    Q_junc, Qa_junc, _, _ = junction_scattering_leakage(N, N, eps, 1, 2)

    print(f"  α = {ALPHA:.6e}")
    print(f"  e = √(4πα) = {np.sqrt(4*np.pi*ALPHA):.6f}")
    print(f"  1/α = {1/ALPHA:.2f}")
    print()
    print(f"  CP field Q (Part A):       {Q_cp:.6f}")
    print(f"  Junction Q (Part B):       {Q_junc:.6f}")
    print(f"  Junction Q_abs:            {Qa_junc:.4f}")
    jratio = Q_junc / Qa_junc if abs(Qa_junc) > 1e-30 else 0.0
    print(f"  Junction Q/Q_abs:          {jratio:.6e}")
    print(f"  Junction Q/Q_abs / α:      {jratio/ALPHA:.4f}")

    # ── Visualization ─────────────────────────────────────
    print("\n── Visualizations ──")

    eps = 0.3
    N = 40

    fig, axes = plt.subplots(2, 3, figsize=(15, 9))

    # Row 1: CP field E·ρ̂
    for idx, (n1, n2) in enumerate([(1, 2), (1, 3), (2, 4)]):
        _, _, E_rho, nds = cp_field_rho_projection(N, N, eps, n1, n2, "traveling")
        ax = axes[0, idx]
        vmax = max(np.abs(E_rho).max(), 0.01)
        sc = ax.scatter(nds[:, 1], nds[:, 0], c=E_rho, cmap="RdBu_r",
                        s=2, vmin=-vmax, vmax=vmax)
        ax.set_title(f"CP E·ρ̂  ({n1},{n2})")
        ax.set_xlabel("θ₂")
        ax.set_ylabel("θ₁")
        fig.colorbar(sc, ax=ax)

    # Row 2: Junction scattering E·ρ̂
    for idx, (n1, n2) in enumerate([(1, 2), (1, 3), (2, 4)]):
        _, _, E_rho_j, nds = junction_scattering_leakage(N, N, eps, n1, n2)
        ax = axes[1, idx]
        vmax = max(np.abs(E_rho_j).max(), 0.01)
        sc = ax.scatter(nds[:, 1], nds[:, 0], c=E_rho_j, cmap="RdBu_r",
                        s=2, vmin=-vmax, vmax=vmax)
        ax.set_title(f"Junc E·ρ̂  ({n1},{n2})")
        ax.set_xlabel("θ₂")
        ax.set_ylabel("θ₁")
        fig.colorbar(sc, ax=ax)

    fig.suptitle(f"E·ρ̂ distribution (ε={eps}, N={N})", fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT / "track8_Erho_distribution.png", dpi=150)
    print(f"  Saved: {OUT / 'track8_Erho_distribution.png'}")

    # Convergence plot
    fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(eps_vals, ratios_eps, "o-", color="steelblue")
    ax1.axhline(ALPHA, color="red", ls="--", alpha=0.5, label=f"α = {ALPHA:.4e}")
    ax1.set_xlabel("ε = a/R")
    ax1.set_ylabel("Q / Q_abs")
    ax1.set_title("Junction leakage ratio vs ε")
    ax1.legend()

    Ns_conv = [10, 20, 30, 40, 60]
    Qs_conv = []
    for Ni in Ns_conv:
        Q, _, _, _ = junction_scattering_leakage(Ni, Ni, 0.3, 1, 2)
        Qs_conv.append(Q)
    ax2.plot(Ns_conv, Qs_conv, "s-", color="darkgreen")
    ax2.set_xlabel("N (lattice cells per direction)")
    ax2.set_ylabel("Q (junction leakage)")
    ax2.set_title("Convergence: mode (1,2), ε=0.3")

    fig2.tight_layout()
    fig2.savefig(OUT / "track8_convergence.png", dpi=150)
    print(f"  Saved: {OUT / 'track8_convergence.png'}")

    print("\n" + "=" * 70)
    print("Track 8 complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
