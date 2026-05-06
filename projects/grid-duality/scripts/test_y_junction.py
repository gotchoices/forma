"""Y-junction reflection/transmission test.

The canonical sim-maxwell test: a Gaussian wavepacket launched along one
arm of a coord-3 Y-tree, measured for how much energy reflects back into
the trunk versus transmits into each branch. Theory (matched-impedance
scattering): R = −1/3, T = +2/3 per branch, so the energy fractions are

    reflected:    R² = 1/9 ≈ 0.111
    transmitted:  2 · T² = 8/9 ≈ 0.889  (4/9 per branch)

These coefficients are what makes the lattice a viable *light* carrier:
energy is conserved at every junction, with no spurious absorption or
amplification. A model that matches these coefficients on a Y-junction
matches them everywhere on a hex lattice (where every node is coord 3).

Setup: a Y-tree with three 60-node arms. A wavepacket is launched on
arm 0 at distance ~30 from the centre, moving inward. After ~30 steps
the wave reaches the junction; after another ~30 it has cleared into
the side arms. Energy is measured per-arm.

Run:
    cd projects/grid-duality/scripts
    python test_y_junction.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from engine import make_y_tree
from models import NormalizedTelegrapher, RelativeCosBoth, Scattering


OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)


def arm_node_indices(arm_length):
    """Return per-arm node-index ranges (excluding central node 0)."""
    return [
        np.arange(1, arm_length + 1),
        np.arange(arm_length + 1, 2 * arm_length + 1),
        np.arange(2 * arm_length + 1, 3 * arm_length + 1),
    ]


def arm_edge_indices(arm_length):
    """Return per-arm edge-index ranges. Each arm has `arm_length`
    edges: 1 spoke + (arm_length-1) chain edges. They are appended
    consecutively in make_y_tree, so arm i's edges are
    [i*arm_length .. (i+1)*arm_length−1]."""
    return [
        np.arange(arm_length * i, arm_length * (i + 1))
        for i in range(3)
    ]


def init_inbound_packet(model, lattice, arm_length, x0=30.0, k=0.6,
                        sigma=4.0, amplitude=0.3):
    """Place a Gaussian-modulated cosine on arm 0, moving toward the
    centre. Other two arms start at zero.

    For Scattering: a_bwd on arm-0 edges = wave moving toward centre
    (since edges point outward, "toward centre" is the bwd direction).
    a_fwd = 0 everywhere.

    For v-i models (Normalized): v on arm-0 nodes is the wavepacket;
    i on arm-0 edges is set so the wave moves toward centre. With edges
    pointing outward, a wave moving toward decreasing position has
    i = −v (sign chosen for leftward-moving solution).
    """
    state = model.init_state(lattice)
    arm_nodes = arm_node_indices(arm_length)
    arm_edges = arm_edge_indices(arm_length)

    if isinstance(model, Scattering):
        a_bwd = state["a_bwd"].copy()
        # Arm 0 edges in the order they were added: spoke first, then
        # chain edges. Edge i within arm 0 has its midpoint at distance
        # ~ (i + 0.5) from the centre.
        for ei_local, ei in enumerate(arm_edges[0]):
            r = ei_local + 0.5
            env = np.exp(-((r - x0) ** 2) / (2 * sigma ** 2))
            a_bwd[ei] = amplitude * env * np.cos(k * r)
        return {"a_fwd": state["a_fwd"], "a_bwd": a_bwd}

    # v-i paradigm
    for ni_local, ni in enumerate(arm_nodes[0]):
        r = ni_local + 1.0  # node at index 1 is at distance 1 from centre
        env = np.exp(-((r - x0) ** 2) / (2 * sigma ** 2))
        v = amplitude * env * np.cos(k * r)
        state = model.perturb_node(state, ni, v)
    for ei_local, ei in enumerate(arm_edges[0]):
        r = ei_local + 0.5
        env = np.exp(-((r - x0) ** 2) / (2 * sigma ** 2))
        v = amplitude * env * np.cos(k * r)
        # left-moving wave: i = −v
        state = model.perturb_edge(state, ei, -v)
    return state


def per_arm_energy(model, state, arm_edges, arm_nodes):
    """Energy localized on each arm.

    For Scattering: arm energy = 0.5 · sum (a_fwd² + a_bwd²) on arm edges.
    For v-i models:  arm energy = 0.5 · sum(v² on arm nodes) +
                                  0.5 · sum(i² on arm edges).
    The central node 0 is excluded from all arms (it sits at the junction
    and carries a small fraction of the energy that doesn't belong to any
    single arm). Both definitions sum to (model.total_energy − E_central)
    so per-arm fractions are directly comparable to R² / T² theory."""
    if isinstance(model, Scattering):
        return [
            0.5 * float(
                np.sum(state["a_fwd"][ee] ** 2) + np.sum(state["a_bwd"][ee] ** 2)
            )
            for ee in arm_edges
        ]
    # v-i: include both node-v energy and edge-i energy on each arm.
    out = []
    for ee, nn in zip(arm_edges, arm_nodes):
        e_edge = 0.5 * float(np.sum(state["i"][ee] ** 2))
        v_obs = state["v"]
        # phase-distance reading for v in (-π, π]
        v_signed = ((v_obs[nn] + np.pi) % (2 * np.pi)) - np.pi
        e_node = 0.5 * float(np.sum(v_signed ** 2))
        out.append(e_edge + e_node)
    return out


def main():
    arm_length = 60
    n_steps = 90
    x0 = 35.0          # initial wavepacket centre on arm 0
    k = 0.4            # carrier wavevector
    sigma = 5.0
    amplitude = 0.3

    lattice = make_y_tree(arm_length)
    arm_edges = arm_edge_indices(arm_length)
    arm_nodes = arm_node_indices(arm_length)
    print(f"Y-tree: 3 arms of length {arm_length} ({lattice.n_nodes} nodes, {lattice.n_edges} edges)")
    print(f"Wavepacket: x0={x0}, k={k}, σ={sigma}, A={amplitude}")
    print(f"Steps: {n_steps}")
    print()
    print(f"Theory (matched-impedance, coord-3 junction):")
    print(f"  reflected fraction:    R²    = 1/9 ≈ {1/9:.4f}")
    print(f"  transmitted total:    2·T²  = 8/9 ≈ {8/9:.4f}")
    print(f"  transmitted per arm:    T²  = 4/9 ≈ {4/9:.4f}")
    print()

    model_classes = [NormalizedTelegrapher, RelativeCosBoth, Scattering]
    fig, axes = plt.subplots(1, len(model_classes), figsize=(7 * len(model_classes), 5))
    summary = {}

    for col, ModelCls in enumerate(model_classes):
        model = ModelCls()
        print(f"--- Model: {model.name} ---")
        state = init_inbound_packet(
            model, lattice, arm_length,
            x0=x0, k=k, sigma=sigma, amplitude=amplitude,
        )

        e0_arm = per_arm_energy(model, state, arm_edges, arm_nodes)
        e_initial = sum(e0_arm)
        e_total_initial = float(model.total_energy(state))
        print(f"  initial energy (arm 0): {e0_arm[0]:.4f}; "
              f"arm 1: {e0_arm[1]:.4f}; arm 2: {e0_arm[2]:.4f}")
        print(f"  total system energy at t=0: {e_total_initial:.4f}")
        # Run dynamics
        history = [e0_arm]
        total_history = [e_total_initial]
        for _ in range(n_steps):
            state = model.update(state, lattice)
            history.append(per_arm_energy(model, state, arm_edges, arm_nodes))
            total_history.append(float(model.total_energy(state)))
        history = np.array(history)
        total_history = np.array(total_history)

        # Reflection / transmission: at the final step, the inbound
        # wavepacket has scattered once and the resulting waves are
        # travelling outward. Compare arm energies (relative to total
        # remaining energy).
        e_final = history[-1]
        total_final = e_final.sum()
        if total_final > 0:
            frac = e_final / total_final
            print(f"  final (step {n_steps}) energy fractions per arm:")
            print(f"    arm 0 (reflected):    {frac[0]:.4f}  (theory 1/9 = 0.1111)")
            print(f"    arm 1 (transmitted):  {frac[1]:.4f}  (theory 4/9 = 0.4444)")
            print(f"    arm 2 (transmitted):  {frac[2]:.4f}  (theory 4/9 = 0.4444)")
            print(f"  total transmitted: {frac[1] + frac[2]:.4f}  (theory 8/9 = 0.8889)")
            true_energy_drift = (total_history[-1] - total_history[0]) / max(total_history[0], 1e-12)
            print(f"  total system energy drift (model.total_energy): {true_energy_drift:+.6f}")

        summary[model.name] = {
            "fractions": e_final / max(total_final, 1e-12),
            "history": history,
        }

        ax = axes[col]
        for arm_i, label in enumerate(
            ["arm 0 (reflected)", "arm 1 (transmitted)", "arm 2 (transmitted)"]
        ):
            ax.plot(history[:, arm_i], linewidth=1.4, label=label)
        ax.axhline(history[0].sum() * (1/9), color="C0", linestyle=":",
                   alpha=0.5, label="theory R²")
        ax.axhline(history[0].sum() * (4/9), color="C1", linestyle=":",
                   alpha=0.5, label="theory T² per arm")
        ax.set_xlabel("clock step")
        ax.set_ylabel("arm energy")
        ax.set_title(f"{model.name}: per-arm energy vs time")
        ax.legend(loc="best", fontsize=9)
        ax.grid(alpha=0.3)
        print()

    fig.suptitle(
        "Y-junction matched-impedance test (coord-3): "
        "R = −1/3, T = +2/3 per branch", fontsize=12,
    )
    plt.tight_layout()
    out = os.path.join(OUTDIR, "y-junction.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")

    print("\n=== Summary (final-step energy fractions) ===")
    print(f"  {'model':18s}  {'arm0 (R)':>10s}  {'arm1 (T)':>10s}  {'arm2 (T)':>10s}  {'sum T':>10s}")
    print(f"  {'-'*18}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")
    print(f"  {'theory':18s}  {1/9:>10.4f}  {4/9:>10.4f}  {4/9:>10.4f}  {8/9:>10.4f}")
    for name, data in summary.items():
        f = data["fractions"]
        print(f"  {name:18s}  {f[0]:>10.4f}  {f[1]:>10.4f}  {f[2]:>10.4f}  {f[1]+f[2]:>10.4f}")


if __name__ == "__main__":
    main()
