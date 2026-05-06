"""2D pulse test on a hex torus.

Runs a chosen model on a 2D hexagonal lattice with bipartite (A → B)
edge orientation, perturbs a node at the center with a Gaussian
envelope, and produces snapshots at evenly-spaced time steps plus an
energy-vs-time plot.

This is the load-bearing test for whether Telegrapher (or any
candidate model) gives stable 2D wave propagation.

Run:
    cd projects/grid-duality/scripts
    python test_2d_pulse.py
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


def run_simulation(model, lattice, perturbation_fn, n_steps):
    state = model.init_state(lattice)
    state = perturbation_fn(model, state)
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


def gaussian_at_center(amplitude=0.5, width=1.5):
    """Apply a Gaussian envelope of node-value perturbations centred at the
    lattice's centroid. Uses each node's 2D position; works on any lattice
    with `lattice.positions`."""
    def _fn_factory(lattice):
        center = lattice.positions.mean(axis=0)

        def _fn(model, state):
            for ni in range(lattice.n_nodes):
                r2 = np.sum((lattice.positions[ni] - center) ** 2)
                value = amplitude * np.exp(-r2 / (2 * width ** 2))
                if abs(value) > 1e-9:
                    state = model.perturb_node(state, ni, value)
            return state
        return _fn
    return _fn_factory


def plot_2d_results(history, lattice, title, filename, snapshot_indices=None):
    """Snapshot grid of node values at chosen time steps, plus energy plot."""
    nv = history["node_values"]
    energies = history["energy"]
    n_steps = nv.shape[0] - 1

    if snapshot_indices is None:
        # 6 evenly-spaced snapshots from t=0 to t=n_steps
        snapshot_indices = np.linspace(0, n_steps, 6).astype(int)

    n_snaps = len(snapshot_indices)
    fig = plt.figure(figsize=(4 * 3, 4 * ((n_snaps + 2) // 3 + 1)))

    # Use a fixed color scale across all snapshots, based on the early-time max
    early_max = np.abs(nv[: max(2, n_steps // 4)]).max()
    vmax = max(early_max, 0.05)

    for k, idx in enumerate(snapshot_indices):
        ax = plt.subplot(((n_snaps + 2) // 3) + 1, 3, k + 1)
        sc = ax.scatter(
            lattice.positions[:, 0],
            lattice.positions[:, 1],
            c=nv[idx],
            cmap="RdBu_r",
            vmin=-vmax,
            vmax=vmax,
            s=80,
            edgecolor="black",
            linewidth=0.4,
        )
        ax.set_title(f"t = {idx} (max |v| = {np.abs(nv[idx]).max():.3f})")
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        plt.colorbar(sc, ax=ax, fraction=0.046)

    # Energy plot in the last subplot
    ax = plt.subplot(((n_snaps + 2) // 3) + 1, 3, n_snaps + 1)
    ax.plot(energies, "b-", linewidth=1.4)
    ax.set_xlabel("clock step")
    ax.set_ylabel("total energy")
    ax.set_title(f"Energy: {energies[0]:.3f} → {energies[-1]:.3f}")
    ax.grid(alpha=0.3)
    if energies[-1] > 10 * energies[0]:
        ax.set_yscale("log")

    fig.suptitle(title, fontsize=12)
    plt.tight_layout()
    out_path = os.path.join(OUTDIR, filename)
    plt.savefig(out_path, dpi=110, bbox_inches="tight")
    plt.close()
    print(f"  wrote {out_path}")


def main():
    nx, ny = 14, 14
    n_steps = 100

    lattice = make_2d_hex_torus(nx, ny)
    print(f"Lattice: 2D hex torus, {nx}×{ny} cells "
          f"({lattice.n_nodes} nodes, {lattice.n_edges} edges, "
          f"coord = {int(lattice.coord[0])} per node)")
    print(f"Steps: {n_steps}")
    print()

    perturbation_factory = gaussian_at_center(amplitude=0.5, width=1.5)

    energy_traces = {}
    for ModelCls in [
        Telegrapher,
        NormalizedTelegrapher,
        RelativeCosBoth,
        Scattering,
    ]:
        model = ModelCls()
        print(f"--- Model: {model.name} ---")
        perturbation_fn = perturbation_factory(lattice)
        history = run_simulation(model, lattice, perturbation_fn, n_steps)
        e0, eF = history["energy"][0], history["energy"][-1]
        print(f"  energy: {e0:.4f} → {eF:.4f}  (ratio {eF / max(e0, 1e-12):.2f}×)")
        plot_2d_results(
            history,
            lattice,
            f"{model.name} on 2D hex torus ({nx}×{ny}): Gaussian perturbation",
            f"{model.name}-2d-gaussian.png",
        )
        energy_traces[model.name] = history["energy"]
        print()

    # Summary plot of energy traces (log-y for fair comparison)
    fig, ax = plt.subplots(figsize=(10, 5))
    for name, e in energy_traces.items():
        ax.semilogy(e, label=name, linewidth=1.4)
    ax.set_xlabel("clock step")
    ax.set_ylabel("total energy (log scale)")
    ax.set_title(f"Energy vs time, all candidates, 2D hex torus ({nx}×{ny})")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    out = os.path.join(OUTDIR, "energy-comparison.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
