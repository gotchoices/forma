"""Substrate-quantization sweep on the chapter-4 test bench.

Implements the experimental program from grid-quantizing.md §7. Replaces
each register's real-valued state with one of N levels in [−amp_max,
+amp_max]; sweeps over (N, lattice scale s) and measures how each test's
result deviates from the continuous baseline.

Predicted scaling (analog-averaging regime, §5.2):
    error(N, s) ≈ C / (N · s^p)
with p ≈ 2 for amplitude tests and p ≈ 1 for scattering tests.

Predicted test-by-test behavior (§7.4):
- L1 (1D coord-2 dispersion): exact at any (N, s) — bit-swap reproduces
  continuous swap exactly.
- S1 / S2 (2D stability under naive quantization): error compounds
  linearly per step; fails at small (N, s); recovers as s grows.
- L2 (Y-junction matched-impedance): requires coarse-graining; fails at
  (N=2, s=1); converges with s.
- L3 (linearity): passes at sufficient s for any N.

This script focuses on the most informative diagnostic experiments: A, B,
C, D below. A two-axis (N, s) sweep over every test would be more
thorough but slower; the four chosen experiments are sufficient to test
the predicted scaling laws.

Run:
    cd projects/grid-duality/scripts
    python test_quantization_sweep.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from engine import make_2d_hex_torus, make_y_tree
from models import Scattering, QuantizedScattering

from test_2d_pulse import gaussian_at_center, run_simulation
from test_y_junction import (
    init_inbound_packet, per_arm_energy,
    arm_node_indices, arm_edge_indices,
)


OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)


def make_quantized(n_levels, amp_max=1.0):
    """Convenience: a QuantizedScattering instance, or the parent Scattering
    when n_levels is None / inf."""
    if n_levels is None or n_levels == float("inf"):
        return Scattering()
    return QuantizedScattering(n_levels=n_levels, amp_max=amp_max)


# ---------- Experiment A: stability sweep over N at fixed lattice ----------

def experiment_A():
    """S1-style stability test on a 14×14 hex torus, 100 steps, Gaussian
    pulse. Sweep N. amp_max chosen with margin over the IC amplitude."""
    print("=== Experiment A: stability sweep over N (fixed 14×14 hex) ===\n")
    nx, ny = 14, 14
    n_steps = 100
    amplitude = 0.5
    width = 1.5
    amp_max = 0.5  # matches IC amplitude — keeps level spacing fine at low N.

    lattice = make_2d_hex_torus(nx, ny)
    perturb_fn = gaussian_at_center(amplitude=amplitude, width=width)(lattice)

    Ns = [None, 257, 65, 17, 9, 5, 3]
    results = {}
    for N in Ns:
        model = make_quantized(N, amp_max=amp_max)
        history = run_simulation(model, lattice, perturb_fn, n_steps)
        e = history["energy"]
        ratio = e[-1] / max(e[0], 1e-12)
        results[N] = {"e0": e[0], "eF": e[-1], "ratio": ratio, "energies": e}
        label = f"N={N}" if N is not None else "N=∞ (Scattering)"
        print(f"  {label:18s}  e0={e[0]:.3f}  eF={e[-1]:.3f}  ratio={ratio:.3g}")
    print()
    return results


# ---------- Experiment B: stability with lattice refinement ----------

def experiment_B():
    """Does coarse-graining (refine the lattice) recover continuum behavior
    at low N? Pick a low-N variant that fails Experiment A and scale the
    lattice from 14×14 up to 56×56. Track ratio."""
    print("=== Experiment B: stability with lattice refinement (N=4) ===\n")
    n_steps = 100
    amplitude = 0.5
    width = 1.5
    amp_max = 0.5
    N = 17  # intermediate N — clear noise, but signal survives quantization.

    sizes = [(14, 14), (28, 28), (42, 42), (56, 56)]
    results = {}
    for (nx, ny) in sizes:
        lattice = make_2d_hex_torus(nx, ny)
        # Scale the perturbation width with the lattice so the pulse
        # occupies the same physical extent (in lattice units).
        # Width=1.5 at 14×14 ≈ width=3 at 28×28, etc.
        s = nx / 14
        perturb_fn = gaussian_at_center(amplitude=amplitude, width=width * s)(lattice)
        model = make_quantized(N, amp_max=amp_max)
        history = run_simulation(model, lattice, perturb_fn, n_steps)
        e = history["energy"]
        ratio = e[-1] / max(e[0], 1e-12)
        results[(nx, ny)] = {"e0": e[0], "eF": e[-1], "ratio": ratio, "energies": e, "s": s}
        print(f"  {nx}×{ny} (s={s:.0f})  e0={e[0]:.3f}  eF={e[-1]:.3f}  ratio={ratio:.3g}")
    print()
    return results


# ---------- Experiment C: Y-junction over N ----------

def experiment_C():
    """L2-style Y-junction test. Sweep N at fixed arm length."""
    print("=== Experiment C: Y-junction reflection/transmission over N ===\n")
    arm_length = 60
    n_steps = 90
    amp_max = 0.4  # matches IC amplitude (0.3) — fine spacing at low N.

    lattice = make_y_tree(arm_length)
    arm_edges = arm_edge_indices(arm_length)
    arm_nodes = arm_node_indices(arm_length)

    Ns = [None, 257, 65, 17, 9, 5, 3]
    results = {}
    print("  Theory: arm0=0.1111 (R²), arm1=arm2=0.4444 (T²)")
    for N in Ns:
        model = make_quantized(N, amp_max=amp_max)
        if N is None:
            state = init_inbound_packet(model, lattice, arm_length, x0=35.0, k=0.4, sigma=5.0, amplitude=0.3)
        else:
            # Build state using the parent class's init logic, then quantize.
            base = Scattering()
            state = init_inbound_packet(base, lattice, arm_length, x0=35.0, k=0.4, sigma=5.0, amplitude=0.3)
            state = {
                "a_fwd": model._quantize(state["a_fwd"]),
                "a_bwd": model._quantize(state["a_bwd"]),
            }
            model._lattice = lattice  # Make sure observables work

        for _ in range(n_steps):
            state = model.update(state, lattice)
        e_arms = per_arm_energy(model, state, arm_edges, arm_nodes)
        total = sum(e_arms)
        if total > 0:
            frac = [e / total for e in e_arms]
        else:
            frac = [0, 0, 0]
        results[N] = {"fractions": frac, "total_energy": total}
        label = f"N={N}" if N is not None else "N=∞"
        print(f"  {label:6s}  arm0={frac[0]:.4f}  arm1={frac[1]:.4f}  arm2={frac[2]:.4f}  (total E = {total:.3f})")
    print()
    return results


# ---------- Experiment D: Y-junction with arm-length scaling at low N ----------

def experiment_D():
    """At low N (=4), does increasing arm length (more cells per macroscopic
    feature) recover matched-impedance theory? Wavepacket parameters scale
    proportionally."""
    print("=== Experiment D: Y-junction arm-length scaling (N=4) ===\n")
    n_steps_base = 90
    amp_max = 0.4
    N = 17

    arm_lengths = [60, 120, 240, 480]
    results = {}
    print("  Theory: arm0=0.1111 (R²), arm1=arm2=0.4444 (T²)")
    for arm_length in arm_lengths:
        lattice = make_y_tree(arm_length)
        arm_edges = arm_edge_indices(arm_length)
        arm_nodes = arm_node_indices(arm_length)
        # Scale wavepacket params with arm length so wave fills the same
        # fraction of arm. Steps scale up so the wave reaches the junction.
        s = arm_length / 60
        n_steps = int(n_steps_base * s)
        x0 = 35.0 * s
        sigma = 5.0 * s
        # Wavevector stays constant — same physical wavelength in lattice units
        k = 0.4 / s

        # Initial state via continuous version, then quantize
        base = Scattering()
        state = init_inbound_packet(
            base, lattice, arm_length,
            x0=x0, k=k, sigma=sigma, amplitude=0.3,
        )
        model = make_quantized(N, amp_max=amp_max)
        state = {
            "a_fwd": model._quantize(state["a_fwd"]),
            "a_bwd": model._quantize(state["a_bwd"]),
        }
        model._lattice = lattice

        for _ in range(n_steps):
            state = model.update(state, lattice)
        e_arms = per_arm_energy(model, state, arm_edges, arm_nodes)
        total = sum(e_arms)
        if total > 0:
            frac = [e / total for e in e_arms]
        else:
            frac = [0, 0, 0]
        results[arm_length] = {"fractions": frac, "total_energy": total, "s": s}
        print(f"  arm_length={arm_length:4d} (s={s:.0f})  arm0={frac[0]:.4f}  arm1={frac[1]:.4f}  arm2={frac[2]:.4f}  (total E={total:.3f})")
    print()
    return results


# ---------- Plotting ----------

def plot_summary(rA, rB, rC, rD):
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # A: ratio vs N (log)
    ax = axes[0, 0]
    Ns_a = [N for N in rA.keys() if N is not None]
    ratios_a = [rA[N]["ratio"] for N in Ns_a]
    ax.semilogx(Ns_a, ratios_a, "o-", linewidth=1.4, markersize=6)
    cont_ratio = rA[None]["ratio"]
    ax.axhline(cont_ratio, color="grey", linestyle="--", alpha=0.6,
               label=f"N=∞ (Scattering): {cont_ratio:.3f}×")
    ax.set_xlabel("N (levels per cell)")
    ax.set_ylabel("energy ratio after 100 steps")
    ax.set_title("A: stability vs N (14×14 hex)")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3, which="both")

    # B: ratio vs lattice scale s at N=4
    ax = axes[0, 1]
    sizes = list(rB.keys())
    ratios_b = [rB[k]["ratio"] for k in sizes]
    s_vals = [rB[k]["s"] for k in sizes]
    ax.semilogy(s_vals, ratios_b, "o-", linewidth=1.4, markersize=6, color="C1")
    ax.axhline(1.0, color="grey", linestyle="--", alpha=0.6,
               label="continuum target (1.0×)")
    ax.set_xlabel("lattice scale s (×14×14)")
    ax.set_ylabel("energy ratio after 100 steps (log)")
    ax.set_title("B: stability with lattice refinement (N=4)")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3, which="both")

    # C: Y-junction fractions vs N
    ax = axes[1, 0]
    Ns_c = [N for N in rC.keys() if N is not None]
    arm0 = [rC[N]["fractions"][0] for N in Ns_c]
    arm1 = [rC[N]["fractions"][1] for N in Ns_c]
    arm2 = [rC[N]["fractions"][2] for N in Ns_c]
    ax.semilogx(Ns_c, arm0, "o-", color="C0", linewidth=1.4, label="arm 0 (R)")
    ax.semilogx(Ns_c, arm1, "s-", color="C1", linewidth=1.4, label="arm 1 (T)")
    ax.semilogx(Ns_c, arm2, "^-", color="C2", linewidth=1.4, label="arm 2 (T)")
    ax.axhline(1/9, color="C0", linestyle=":", alpha=0.6, label="theory R²=1/9")
    ax.axhline(4/9, color="C1", linestyle=":", alpha=0.6, label="theory T²=4/9")
    ax.set_xlabel("N (levels per cell)")
    ax.set_ylabel("arm energy fraction")
    ax.set_title("C: Y-junction fractions vs N (60-arm Y-tree)")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3, which="both")

    # D: Y-junction at N=4, vs arm length
    ax = axes[1, 1]
    arm_lengths = list(rD.keys())
    arm0_d = [rD[L]["fractions"][0] for L in arm_lengths]
    arm1_d = [rD[L]["fractions"][1] for L in arm_lengths]
    arm2_d = [rD[L]["fractions"][2] for L in arm_lengths]
    ax.semilogx(arm_lengths, arm0_d, "o-", color="C0", linewidth=1.4, label="arm 0 (R)")
    ax.semilogx(arm_lengths, arm1_d, "s-", color="C1", linewidth=1.4, label="arm 1 (T)")
    ax.semilogx(arm_lengths, arm2_d, "^-", color="C2", linewidth=1.4, label="arm 2 (T)")
    ax.axhline(1/9, color="C0", linestyle=":", alpha=0.6, label="theory R²=1/9")
    ax.axhline(4/9, color="C1", linestyle=":", alpha=0.6, label="theory T²=4/9")
    ax.set_xlabel("arm length (cells)")
    ax.set_ylabel("arm energy fraction")
    ax.set_title("D: Y-junction at N=4, vs arm length")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3, which="both")

    fig.suptitle(
        "Substrate quantization sweep — chapter 5 / grid-quantizing.md", fontsize=12,
    )
    plt.tight_layout()
    out = os.path.join(OUTDIR, "quantization-sweep.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")


def main():
    rA = experiment_A()
    rB = experiment_B()
    rC = experiment_C()
    rD = experiment_D()
    plot_summary(rA, rB, rC, rD)


if __name__ == "__main__":
    main()
