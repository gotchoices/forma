"""2D directional wavefront test on a hex torus.

A Gaussian-enveloped sinusoidal wavepacket launched in a chosen direction.
Tests whether each model preserves directional wave propagation, or
disperses / breaks symmetry.

Run:
    cd projects/grid-duality/scripts
    python test_2d_wavefront.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from engine import make_2d_hex_torus
from models import (
    Telegrapher,
    NormalizedTelegrapher,
    RelativeCosBoth,
    Scattering,
)


OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)


def run_simulation_with_initial_state(model, lattice, initial_state, n_steps):
    state = initial_state
    n_obs = [model.node_observable(state).copy()]
    energies = [model.total_energy(state)]
    for _ in range(n_steps):
        state = model.update(state, lattice)
        n_obs.append(model.node_observable(state).copy())
        energies.append(model.total_energy(state))
    return {
        "node_values": np.array(n_obs),
        "energy": np.array(energies),
    }


def init_directional_wavefront(model, lattice, amplitude=0.3, k=0.6,
                               direction_deg=0.0, envelope_width=3.0):
    """Initialize a Gaussian-enveloped sinusoidal wavefront moving in
    `direction_deg`. Dispatches to per-model native state representation:

    - Telegrapher / Normalized / RelCos*: matched v on nodes and i on edges
      (i = A · env · cos(k · along) · projection).
    - Scattering: matched (a_fwd, a_bwd) per edge such that
      a_fwd + a_bwd = v_per_edge and a_fwd − a_bwd = i_per_edge.
    """
    direction = np.deg2rad(direction_deg)
    k_hat = np.array([np.cos(direction), np.sin(direction)])
    state = model.init_state(lattice)
    center = lattice.positions.mean(axis=0)

    # Per-edge envelope and amplitude
    edge_along = np.empty(lattice.n_edges)
    for ei in range(lattice.n_edges):
        tail_pos = lattice.positions[lattice.tails[ei]]
        disp_edge = lattice.edge_displacements[ei]
        edge_pos = tail_pos + 0.5 * disp_edge
        edge_along[ei] = float(np.dot(edge_pos - center, k_hat))
    edge_env = np.exp(-edge_along ** 2 / (2.0 * envelope_width ** 2))
    edge_v = amplitude * edge_env * np.cos(k * edge_along)
    edge_proj = np.cos(lattice.theta - direction)
    edge_i = edge_v * edge_proj

    if isinstance(model, Scattering):
        # a_fwd = (v + i) / 2;  a_bwd = (v − i) / 2  per edge.
        return {
            "a_fwd": (edge_v + edge_i) / 2.0,
            "a_bwd": (edge_v - edge_i) / 2.0,
        }

    # v-i paradigm: set v on nodes, i on edges directly.
    for ni in range(lattice.n_nodes):
        disp = lattice.positions[ni] - center
        along = float(np.dot(disp, k_hat))
        env = np.exp(-along ** 2 / (2.0 * envelope_width ** 2))
        value = amplitude * env * np.cos(k * along)
        state = model.perturb_node(state, ni, value)
    for ei in range(lattice.n_edges):
        state = model.perturb_edge(state, ei, edge_i[ei])
    return state


def plot_2d_results(history, lattice, title, filename, snapshot_indices=None):
    nv = history["node_values"]
    energies = history["energy"]
    n_steps = nv.shape[0] - 1

    if snapshot_indices is None:
        snapshot_indices = np.linspace(0, n_steps, 6).astype(int)

    n_snaps = len(snapshot_indices)
    fig = plt.figure(figsize=(4 * 3, 4 * ((n_snaps + 2) // 3 + 1)))

    early_max = np.abs(nv[: max(2, n_steps // 4)]).max()
    vmax = max(early_max, 0.05)

    for k, idx in enumerate(snapshot_indices):
        ax = plt.subplot(((n_snaps + 2) // 3) + 1, 3, k + 1)
        sc = ax.scatter(
            lattice.positions[:, 0], lattice.positions[:, 1],
            c=nv[idx], cmap="RdBu_r",
            vmin=-vmax, vmax=vmax, s=80,
            edgecolor="black", linewidth=0.4,
        )
        ax.set_title(f"t = {idx} (max |v| = {np.abs(nv[idx]).max():.3f})")
        ax.set_aspect("equal")
        ax.set_xticks([]); ax.set_yticks([])
        plt.colorbar(sc, ax=ax, fraction=0.046)

    ax = plt.subplot(((n_snaps + 2) // 3) + 1, 3, n_snaps + 1)
    ax.plot(energies, "b-", linewidth=1.4)
    ax.set_xlabel("clock step")
    ax.set_ylabel("total energy")
    ax.set_title(f"Energy: {energies[0]:.3f} → {energies[-1]:.3f}")
    ax.grid(alpha=0.3)
    if energies[-1] > 10 * max(energies[0], 1e-12):
        ax.set_yscale("log")

    fig.suptitle(title, fontsize=12)
    plt.tight_layout()
    out_path = os.path.join(OUTDIR, filename)
    plt.savefig(out_path, dpi=110, bbox_inches="tight")
    plt.close()
    print(f"  wrote {out_path}")


def main():
    nx, ny = 20, 12
    n_steps = 80
    direction_deg = 0.0  # wave moves along +x axis

    lattice = make_2d_hex_torus(nx, ny)
    print(f"Lattice: 2D hex torus, {nx}×{ny} cells "
          f"({lattice.n_nodes} nodes, {lattice.n_edges} edges)")
    print(f"Steps: {n_steps}, wave direction: {direction_deg}°")
    print()

    energy_traces = {}
    for ModelCls in [
        Telegrapher,
        NormalizedTelegrapher,
        RelativeCosBoth,
        Scattering,
    ]:
        model = ModelCls()
        print(f"--- Model: {model.name} ---")
        initial_state = init_directional_wavefront(
            model, lattice,
            amplitude=0.3, k=0.6, direction_deg=direction_deg, envelope_width=3.0,
        )
        history = run_simulation_with_initial_state(model, lattice, initial_state, n_steps)
        e0, eF = history["energy"][0], history["energy"][-1]
        print(f"  energy: {e0:.4f} → {eF:.4f}  (ratio {eF / max(e0, 1e-12):.2f}×)")
        plot_2d_results(
            history, lattice,
            f"{model.name} on 2D hex torus ({nx}×{ny}): wavefront at {direction_deg}°",
            f"{model.name}-2d-wavefront.png",
        )
        energy_traces[model.name] = history["energy"]
        print()

    fig, ax = plt.subplots(figsize=(10, 5))
    for name, e in energy_traces.items():
        ax.semilogy(e, label=name, linewidth=1.4)
    ax.set_xlabel("clock step")
    ax.set_ylabel("total energy (log scale)")
    ax.set_title(f"Energy vs time, all candidates, 2D wavefront ({nx}×{ny})")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    out = os.path.join(OUTDIR, "energy-comparison-wavefront.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
