#!/usr/bin/env python3
"""sim-maxwell: superposition test.

Launch two wavefronts at 90° on a triangular lattice.
Let them cross.  Measure whether they emerge intact.

If the scattering rule is truly linear, two waves should
pass through each other without distortion.  This is the
second pillar of classical wave physics (after directional
propagation, which Test 1 confirmed).

The test:
  1. Run wavefront A alone → record energy profile at t_final
  2. Run wavefront B alone → record energy profile at t_final
  3. Run A+B together → record energy profile at t_final
  4. Compare (A+B)_together vs A_alone + B_alone

If superposition holds: the combined run equals the sum of
individual runs (at every edge).  Residual should be zero.

Also run on the hexagonal lattice for comparison.

Usage:
    source .venv/bin/activate
    python grid/sim-maxwell/run_superposition.py
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
from run import (make_lattice, scatter_step, evolve,
                 init_wavefront, edge_energy, energy_centroid,
                 directionality_ratio)
from run_hex import (make_honeycomb,
                     scatter_step as hex_scatter_step,
                     evolve as hex_evolve,
                     init_wavefront as hex_init_wavefront,
                     edge_energy as hex_edge_energy,
                     energy_centroid as hex_energy_centroid)


def wrap_periodic(dx, box):
    dx[:, 0] -= box[0] * np.round(dx[:, 0] / box[0])
    dx[:, 1] -= box[1] * np.round(dx[:, 1] / box[1])
    return dx


# ── Triangular lattice superposition ────────────────────────

def test_superposition_tri(nx, ny, n_steps, width, out_dir):
    print(f"\n{'='*60}")
    print(f"  Superposition: TRIANGULAR ({nx}×{ny}, "
          f"{n_steps} steps, w={width})")
    print(f"{'='*60}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box = \
        make_lattice(nx, ny)
    E = len(edges)

    dir_A = np.array([1.0, 0.0])   # rightward
    dir_B = np.array([0.0, 1.0])   # upward

    center_A = np.array([box[0] * 0.25, box[1] * 0.5])
    center_B = np.array([box[0] * 0.5, box[1] * 0.25])

    # Wave A alone
    a_fwd_A, a_bwd_A = init_wavefront(
        edge_dirs, mid, box, E,
        direction=dir_A, center=center_A, width=width)
    E_A0 = edge_energy(a_fwd_A, a_bwd_A).sum()

    snaps_A = evolve(a_fwd_A, a_bwd_A, vert_ei, vert_end,
                     n_steps, snapshot_interval=n_steps)
    _, af_A, ab_A = snaps_A[-1]
    en_A = edge_energy(af_A, ab_A)

    # Wave B alone
    a_fwd_B, a_bwd_B = init_wavefront(
        edge_dirs, mid, box, E,
        direction=dir_B, center=center_B, width=width)
    E_B0 = edge_energy(a_fwd_B, a_bwd_B).sum()

    snaps_B = evolve(a_fwd_B, a_bwd_B, vert_ei, vert_end,
                     n_steps, snapshot_interval=n_steps)
    _, af_B, ab_B = snaps_B[-1]
    en_B = edge_energy(af_B, ab_B)

    # A+B together (linear superposition of initial conditions)
    a_fwd_AB = a_fwd_A.copy() + a_fwd_B.copy()
    a_bwd_AB = a_bwd_A.copy() + a_bwd_B.copy()

    # Re-init A and B for fresh copies
    a_fwd_A0, a_bwd_A0 = init_wavefront(
        edge_dirs, mid, box, E,
        direction=dir_A, center=center_A, width=width)
    a_fwd_B0, a_bwd_B0 = init_wavefront(
        edge_dirs, mid, box, E,
        direction=dir_B, center=center_B, width=width)
    a_fwd_AB = a_fwd_A0 + a_fwd_B0
    a_bwd_AB = a_bwd_A0 + a_bwd_B0
    E_AB0 = edge_energy(a_fwd_AB, a_bwd_AB).sum()

    snaps_AB = evolve(a_fwd_AB, a_bwd_AB, vert_ei, vert_end,
                      n_steps, snapshot_interval=n_steps)
    _, af_AB, ab_AB = snaps_AB[-1]
    en_AB = edge_energy(af_AB, ab_AB)

    # Compare: combined final state vs sum of individual
    # Amplitude-level comparison (the strong test):
    # If linear: af_AB = af_A + af_B and ab_AB = ab_A + ab_B
    residual_fwd = af_AB - (af_A + af_B)
    residual_bwd = ab_AB - (ab_A + ab_B)
    residual_amp = np.sqrt(residual_fwd**2 + residual_bwd**2)
    max_residual = residual_amp.max()
    rms_residual = np.sqrt(np.mean(residual_amp**2))
    total_amp = np.sqrt(np.mean(af_AB**2 + ab_AB**2))

    # Energy-level comparison:
    en_sum = en_A + en_B
    # Note: energy is quadratic, so en_AB ≠ en_A + en_B in general.
    # But the AMPLITUDES should add if the system is linear.
    # The energy comparison is: how does the energy distribution differ?
    cross_term = en_AB - en_sum
    cross_fraction = np.abs(cross_term).sum() / en_AB.sum()

    print(f"\n  Initial energies:")
    print(f"    Wave A: {E_A0:.4f}")
    print(f"    Wave B: {E_B0:.4f}")
    print(f"    A+B:    {E_AB0:.4f}")
    print(f"    Sum:    {E_A0 + E_B0:.4f}")
    print(f"    (A+B has cross terms → E_AB ≠ E_A + E_B)")

    print(f"\n  Amplitude superposition (the linear test):")
    print(f"    max |a_AB − (a_A + a_B)|: {max_residual:.2e}")
    print(f"    RMS residual:             {rms_residual:.2e}")
    print(f"    RMS combined amplitude:   {total_amp:.2e}")
    print(f"    Relative residual:        {rms_residual/total_amp:.2e}")

    if max_residual < 1e-10:
        print(f"\n  ★ PERFECT SUPERPOSITION (residual < 1e-10)")
        print(f"    Waves pass through each other with zero distortion.")
        print(f"    The scattering rule is exactly linear.")
    elif rms_residual / total_amp < 0.01:
        print(f"\n  ~ APPROXIMATE SUPERPOSITION (residual < 1%)")
    else:
        print(f"\n  ✗ SUPERPOSITION FAILS (residual = "
              f"{rms_residual/total_amp:.1%})")

    # Directionality: does each wave keep its direction?
    c_A = energy_centroid(en_A, mid, box)
    c_B = energy_centroid(en_B, mid, box)
    dir_A_final = directionality_ratio(en_A, mid, center_A,
                                        dir_A, box)
    dir_B_final = directionality_ratio(en_B, mid, center_B,
                                        dir_B, box)

    # For the combined run, isolate contributions by
    # looking at energy in each wave's forward cone
    dir_AB_A = directionality_ratio(en_AB, mid, center_A,
                                     dir_A, box)
    dir_AB_B = directionality_ratio(en_AB, mid, center_B,
                                     dir_B, box)

    print(f"\n  Directionality (±60° cone):")
    print(f"    Wave A alone:    {dir_A_final:.3f}")
    print(f"    Wave B alone:    {dir_B_final:.3f}")
    print(f"    A in combined:   {dir_AB_A:.3f}")
    print(f"    B in combined:   {dir_AB_B:.3f}")

    print(f"\n  Energy conservation:")
    print(f"    A alone:    {en_A.sum():.8f} / {E_A0:.4f}")
    print(f"    B alone:    {en_B.sum():.8f} / {E_B0:.4f}")
    print(f"    Combined:   {en_AB.sum():.8f} / {E_AB0:.4f}")

    # Plot
    fig, axes = plt.subplots(2, 3, figsize=(18, 11))

    # Row 1: energy snapshots at t_final
    for ax, (en, title) in zip(axes[0],
            [(en_A, "Wave A alone (→)"),
             (en_B, "Wave B alone (↑)"),
             (en_AB, "A + B combined")]):
        sc = ax.scatter(mid[:, 0], mid[:, 1], c=en, s=0.3,
                        cmap="hot", vmin=0,
                        vmax=max(en_A.max(), en_B.max(),
                                 en_AB.max()) * 0.5)
        ax.set_aspect("equal")
        ax.set_title(title)
        ax.set_xlim(0, box[0])
        ax.set_ylim(0, box[1])

    # Row 2: analysis
    # Residual map
    ax = axes[1][0]
    sc = ax.scatter(mid[:, 0], mid[:, 1], c=residual_amp,
                    s=0.3, cmap="hot")
    ax.set_aspect("equal")
    ax.set_title(f"Amplitude residual\n"
                 f"(max={max_residual:.1e})")
    ax.set_xlim(0, box[0])
    ax.set_ylim(0, box[1])
    plt.colorbar(sc, ax=ax, shrink=0.7)

    # Energy difference
    ax = axes[1][1]
    vmax = np.abs(cross_term).max()
    sc = ax.scatter(mid[:, 0], mid[:, 1], c=cross_term,
                    s=0.3, cmap="RdBu_r", vmin=-vmax, vmax=vmax)
    ax.set_aspect("equal")
    ax.set_title(f"Energy: combined − sum\n"
                 f"(cross-term fraction = {cross_fraction:.3f})")
    ax.set_xlim(0, box[0])
    ax.set_ylim(0, box[1])
    plt.colorbar(sc, ax=ax, shrink=0.7)

    # Summary text
    ax = axes[1][2]
    ax.axis("off")
    summary = (
        f"SUPERPOSITION TEST — TRIANGULAR (N=6)\n\n"
        f"Lattice: {nx}×{ny}, {n_steps} steps\n"
        f"Wave A: rightward (→), width={width}\n"
        f"Wave B: upward (↑), width={width}\n\n"
        f"Amplitude residual:\n"
        f"  max = {max_residual:.2e}\n"
        f"  RMS = {rms_residual:.2e}\n"
        f"  relative = {rms_residual/total_amp:.2e}\n\n"
        f"Energy cross-term fraction: {cross_fraction:.4f}\n\n"
    )
    if max_residual < 1e-10:
        summary += "★ PERFECT LINEAR SUPERPOSITION\n"
        summary += "Waves pass through each other unchanged."
    ax.text(0.05, 0.95, summary, transform=ax.transAxes,
            fontsize=10, verticalalignment="top",
            fontfamily="monospace",
            bbox=dict(boxstyle="round", facecolor="wheat",
                      alpha=0.5))

    fig.suptitle("Superposition test — Triangular lattice (N=6)",
                 fontsize=14, fontweight="bold")
    fig.tight_layout()
    path = os.path.join(out_dir, "superposition_tri.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"\n  Saved: {path}")
    plt.close(fig)

    return {
        "max_residual": max_residual,
        "rms_residual": rms_residual,
        "relative_residual": rms_residual / total_amp,
        "cross_fraction": cross_fraction,
        "lattice": "triangular",
    }


# ── Hexagonal lattice superposition ─────────────────────────

def test_superposition_hex(nx, ny, n_steps, width, out_dir):
    print(f"\n{'='*60}")
    print(f"  Superposition: HEXAGONAL ({nx}×{ny}, "
          f"{n_steps} steps, w={width})")
    print(f"{'='*60}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box, wrap = \
        make_honeycomb(nx, ny)
    E = len(edges)

    dir_A = np.array([1.0, 0.0])
    dir_B = np.array([0.0, 1.0])

    center_A = np.array([box[0] * 0.25, box[1] * 0.5])
    center_B = np.array([box[0] * 0.5, box[1] * 0.25])

    # Wave A alone
    a_fwd_A, a_bwd_A = hex_init_wavefront(
        edge_dirs, mid, box, E, wrap,
        direction=dir_A, center=center_A, width=width)
    E_A0 = hex_edge_energy(a_fwd_A, a_bwd_A).sum()

    snaps_A = hex_evolve(a_fwd_A, a_bwd_A, vert_ei, vert_end,
                         n_steps, snapshot_interval=n_steps, N=3)
    _, af_A, ab_A = snaps_A[-1]
    en_A = hex_edge_energy(af_A, ab_A)

    # Wave B alone
    a_fwd_B, a_bwd_B = hex_init_wavefront(
        edge_dirs, mid, box, E, wrap,
        direction=dir_B, center=center_B, width=width)
    E_B0 = hex_edge_energy(a_fwd_B, a_bwd_B).sum()

    snaps_B = hex_evolve(a_fwd_B, a_bwd_B, vert_ei, vert_end,
                         n_steps, snapshot_interval=n_steps, N=3)
    _, af_B, ab_B = snaps_B[-1]
    en_B = hex_edge_energy(af_B, ab_B)

    # A+B together
    a_fwd_A0, a_bwd_A0 = hex_init_wavefront(
        edge_dirs, mid, box, E, wrap,
        direction=dir_A, center=center_A, width=width)
    a_fwd_B0, a_bwd_B0 = hex_init_wavefront(
        edge_dirs, mid, box, E, wrap,
        direction=dir_B, center=center_B, width=width)
    a_fwd_AB = a_fwd_A0 + a_fwd_B0
    a_bwd_AB = a_bwd_A0 + a_bwd_B0
    E_AB0 = hex_edge_energy(a_fwd_AB, a_bwd_AB).sum()

    snaps_AB = hex_evolve(a_fwd_AB, a_bwd_AB, vert_ei, vert_end,
                          n_steps, snapshot_interval=n_steps, N=3)
    _, af_AB, ab_AB = snaps_AB[-1]
    en_AB = hex_edge_energy(af_AB, ab_AB)

    # Compare amplitudes
    residual_fwd = af_AB - (af_A + af_B)
    residual_bwd = ab_AB - (ab_A + ab_B)
    residual_amp = np.sqrt(residual_fwd**2 + residual_bwd**2)
    max_residual = residual_amp.max()
    rms_residual = np.sqrt(np.mean(residual_amp**2))
    total_amp = np.sqrt(np.mean(af_AB**2 + ab_AB**2))

    cross_term = en_AB - (en_A + en_B)
    cross_fraction = np.abs(cross_term).sum() / en_AB.sum()

    print(f"\n  Initial energies:")
    print(f"    Wave A: {E_A0:.4f}")
    print(f"    Wave B: {E_B0:.4f}")
    print(f"    A+B:    {E_AB0:.4f}")

    print(f"\n  Amplitude superposition:")
    print(f"    max |a_AB − (a_A + a_B)|: {max_residual:.2e}")
    print(f"    RMS residual:             {rms_residual:.2e}")
    print(f"    Relative residual:        {rms_residual/total_amp:.2e}")

    if max_residual < 1e-10:
        print(f"\n  ★ PERFECT SUPERPOSITION (residual < 1e-10)")
    elif rms_residual / total_amp < 0.01:
        print(f"\n  ~ APPROXIMATE SUPERPOSITION (residual < 1%)")
    else:
        print(f"\n  ✗ SUPERPOSITION FAILS")

    print(f"\n  Energy conservation:")
    print(f"    A alone:    {en_A.sum():.8f} / {E_A0:.4f}")
    print(f"    B alone:    {en_B.sum():.8f} / {E_B0:.4f}")
    print(f"    Combined:   {en_AB.sum():.8f} / {E_AB0:.4f}")

    # Plot
    fig, axes = plt.subplots(2, 3, figsize=(18, 11))

    for ax, (en, title) in zip(axes[0],
            [(en_A, "Wave A alone (→)"),
             (en_B, "Wave B alone (↑)"),
             (en_AB, "A + B combined")]):
        sc = ax.scatter(mid[:, 0], mid[:, 1], c=en, s=0.3,
                        cmap="hot", vmin=0,
                        vmax=max(en_A.max(), en_B.max(),
                                 en_AB.max()) * 0.5)
        ax.set_aspect("equal")
        ax.set_title(title)
        ax.set_xlim(0, box[0])
        ax.set_ylim(0, box[1])

    ax = axes[1][0]
    sc = ax.scatter(mid[:, 0], mid[:, 1], c=residual_amp,
                    s=0.3, cmap="hot")
    ax.set_aspect("equal")
    ax.set_title(f"Amplitude residual\n(max={max_residual:.1e})")
    ax.set_xlim(0, box[0])
    ax.set_ylim(0, box[1])
    plt.colorbar(sc, ax=ax, shrink=0.7)

    ax = axes[1][1]
    vmax = max(np.abs(cross_term).max(), 1e-15)
    sc = ax.scatter(mid[:, 0], mid[:, 1], c=cross_term,
                    s=0.3, cmap="RdBu_r", vmin=-vmax, vmax=vmax)
    ax.set_aspect("equal")
    ax.set_title(f"Energy cross-term\n(fraction = {cross_fraction:.3f})")
    ax.set_xlim(0, box[0])
    ax.set_ylim(0, box[1])
    plt.colorbar(sc, ax=ax, shrink=0.7)

    ax = axes[1][2]
    ax.axis("off")
    summary = (
        f"SUPERPOSITION TEST — HEXAGONAL (N=3)\n\n"
        f"Lattice: {nx}×{ny}, {n_steps} steps\n"
        f"Wave A: rightward (→), width={width}\n"
        f"Wave B: upward (↑), width={width}\n\n"
        f"Amplitude residual:\n"
        f"  max = {max_residual:.2e}\n"
        f"  RMS = {rms_residual:.2e}\n"
        f"  relative = {rms_residual/total_amp:.2e}\n\n"
        f"Energy cross-term fraction: {cross_fraction:.4f}\n\n"
    )
    if max_residual < 1e-10:
        summary += "★ PERFECT LINEAR SUPERPOSITION\n"
        summary += "Waves pass through each other unchanged."
    ax.text(0.05, 0.95, summary, transform=ax.transAxes,
            fontsize=10, verticalalignment="top",
            fontfamily="monospace",
            bbox=dict(boxstyle="round", facecolor="lightblue",
                      alpha=0.5))

    fig.suptitle("Superposition test — Hexagonal lattice (N=3)",
                 fontsize=14, fontweight="bold")
    fig.tight_layout()
    path = os.path.join(out_dir, "superposition_hex.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"\n  Saved: {path}")
    plt.close(fig)

    return {
        "max_residual": max_residual,
        "rms_residual": rms_residual,
        "relative_residual": rms_residual / total_amp,
        "cross_fraction": cross_fraction,
        "lattice": "hexagonal",
    }


# ── Main ─────────────────────────────────────────────────────

def main():
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(out_dir, exist_ok=True)

    print("sim-maxwell: SUPERPOSITION TEST")
    print("Two wavefronts at 90°, check if they pass through")
    print("each other unchanged (amplitude-level comparison).")
    print()

    r_tri = test_superposition_tri(
        nx=100, ny=100, n_steps=60, width=3.0, out_dir=out_dir)

    r_hex = test_superposition_hex(
        nx=60, ny=60, n_steps=50, width=3.0, out_dir=out_dir)

    print(f"\n{'='*72}")
    print("  SUMMARY — SUPERPOSITION")
    print(f"{'='*72}")
    print()
    print(f"  {'':>12s}  {'Max residual':>14s}  "
          f"{'Relative':>12s}  {'Verdict':>20s}")
    print(f"  {'-'*12}  {'-'*14}  {'-'*12}  {'-'*20}")
    for r in [r_tri, r_hex]:
        name = r["lattice"].capitalize()
        verdict = ("★ PERFECT" if r["max_residual"] < 1e-10
                   else "~ approximate"
                   if r["relative_residual"] < 0.01
                   else "✗ fails")
        print(f"  {name:>12s}  {r['max_residual']:14.2e}  "
              f"{r['relative_residual']:12.2e}  {verdict:>20s}")

    print()
    if r_tri["max_residual"] < 1e-10 and r_hex["max_residual"] < 1e-10:
        print("  ★ SUPERPOSITION IS EXACT ON BOTH LATTICES")
        print("    The scattering rule is linear by construction.")
        print("    Two crossing wavefronts pass through each other")
        print("    with zero distortion at the amplitude level.")
        print()
        print("    This confirms the second pillar of classical wave")
        print("    physics (after directional propagation):")
        print("      1. Directional propagation ✅ (Test 1)")
        print("      2. Linear superposition ✅ (this test)")
        print()
        print("    The energy cross-terms are non-zero because")
        print("    energy is quadratic in amplitude (E = a²).")
        print("    But the amplitudes — the physical fields —")
        print("    superpose exactly.")


if __name__ == "__main__":
    main()
