"""First test: pulse propagation in 1D.

Runs a chosen model on a 1D periodic ring, perturbs a single node,
records the time evolution, and produces space-time plots plus an
energy-vs-time plot.

Run:
    cd projects/grid-duality/scripts
    python test_pulse.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from engine import make_1d_periodic
from models import Telegrapher


OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)


def run_simulation(model, lattice, perturbation_fn, n_steps):
    """Run a simulation and return time series of observables."""
    state = model.init_state(lattice)
    state = perturbation_fn(model, state)

    n_obs = [model.node_observable(state).copy()]
    e_obs = [model.edge_observable(state).copy()]
    energies = [model.total_energy(state)]

    for _ in range(n_steps):
        state = model.update(state, lattice)
        n_obs.append(model.node_observable(state).copy())
        e_obs.append(model.edge_observable(state).copy())
        energies.append(model.total_energy(state))

    return {
        "node_values": np.array(n_obs),
        "edge_values": np.array(e_obs),
        "energy": np.array(energies),
    }


def plot_results(history, title, filename):
    """Make space-time plots and an energy plot."""
    nv = history["node_values"]
    ev = history["edge_values"]
    en = history["energy"]

    fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

    # Node values: rows are time steps, columns are node indices
    vmax_n = max(np.abs(nv).max(), 1e-9)
    im0 = axes[0].imshow(
        nv.T, aspect="auto", origin="lower",
        cmap="RdBu_r", vmin=-vmax_n, vmax=vmax_n,
    )
    axes[0].set_xlabel("clock step")
    axes[0].set_ylabel("node index")
    axes[0].set_title(f"Node value v (phase distance from 0; range ±{vmax_n:.2f})")
    plt.colorbar(im0, ax=axes[0])

    vmax_e = max(np.abs(ev).max(), 1e-9)
    im1 = axes[1].imshow(
        ev.T, aspect="auto", origin="lower",
        cmap="RdBu_r", vmin=-vmax_e, vmax=vmax_e,
    )
    axes[1].set_xlabel("clock step")
    axes[1].set_ylabel("edge index")
    axes[1].set_title(f"Edge value i (range ±{vmax_e:.2f})")
    plt.colorbar(im1, ax=axes[1])

    axes[2].plot(en, "b-", linewidth=1.4)
    axes[2].set_xlabel("clock step")
    axes[2].set_ylabel("total energy = ½ (Σ v² + Σ i²)")
    axes[2].set_title(f"Energy: {en[0]:.3f} → {en[-1]:.3f}")
    axes[2].grid(alpha=0.3)

    fig.suptitle(title, fontsize=12)
    plt.tight_layout()
    out_path = os.path.join(OUTDIR, filename)
    plt.savefig(out_path, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"  wrote {out_path}")


# ---------- Perturbations ----------

def perturb_delta(amplitude=0.5):
    """Single-node delta at the center."""
    def _fn(model, state):
        n = state["v"].shape[0]
        return model.perturb_node(state, n // 2, amplitude)
    return _fn


def perturb_gaussian(amplitude=0.5, width=2.5):
    """Smooth Gaussian envelope at the center."""
    def _fn(model, state):
        n = state["v"].shape[0]
        center = n // 2
        for i in range(n):
            offset = i - center
            value = amplitude * np.exp(-(offset ** 2) / (2 * width ** 2))
            state = model.perturb_node(state, i, value)
        return state
    return _fn


def perturb_traveling_wave(amplitude=0.3, k=0.4):
    """A pure forward-moving wavepacket on a 1D ring with right-pointing edges.

    For Telegrapher's continuum limit, a forward wave v(x, t) = A·cos(k·x − ω·t)
    pairs with i(x, t) = −A·cos(k·x − ω·t) (with c = ω/k = 1 in lattice units).
    The edge i_j sits at midpoint x_e = j + 0.5 between nodes j and j+1.
    """
    def _fn(model, state):
        n = state["v"].shape[0]
        center = n // 2
        envelope_width = 5.0
        for i in range(n):
            offset = i - center
            env = np.exp(-(offset ** 2) / (2 * envelope_width ** 2))
            state = model.perturb_node(state, i, amplitude * env * np.cos(k * offset))
        for ei in range(n):
            offset = ei - center + 0.5
            env = np.exp(-(offset ** 2) / (2 * envelope_width ** 2))
            # Forward wave: i has opposite sign to v at the same spatial position.
            state = model.perturb_edge(state, ei, -amplitude * env * np.cos(k * offset))
        return state
    return _fn


# ---------- Main ----------

def main():
    n = 64
    n_steps = 100

    lattice = make_1d_periodic(n)
    model = Telegrapher()

    print(f"Lattice: 1D periodic, n={n}, n_edges={lattice.n_edges}")
    print(f"Model: {model.name}")
    print(f"Steps: {n_steps}")
    print()

    print("Test 1 — single-node delta:")
    history = run_simulation(model, lattice, perturb_delta(0.5), n_steps)
    print(f"  energy: {history['energy'][0]:.4f} → {history['energy'][-1]:.4f}")
    plot_results(
        history,
        f"{model.name} on 1D ring (n={n}): single-node delta perturbation",
        f"{model.name}-1d-delta.png",
    )

    print("\nTest 2 — Gaussian envelope:")
    history = run_simulation(model, lattice, perturb_gaussian(0.5, 2.5), n_steps)
    print(f"  energy: {history['energy'][0]:.4f} → {history['energy'][-1]:.4f}")
    plot_results(
        history,
        f"{model.name} on 1D ring (n={n}): Gaussian envelope perturbation",
        f"{model.name}-1d-gaussian.png",
    )

    print("\nTest 3 — traveling wavepacket (matched v and i):")
    history = run_simulation(model, lattice, perturb_traveling_wave(0.3, 0.4), n_steps)
    print(f"  energy: {history['energy'][0]:.4f} → {history['energy'][-1]:.4f}")
    plot_results(
        history,
        f"{model.name} on 1D ring (n={n}): traveling wavepacket",
        f"{model.name}-1d-traveling.png",
    )


if __name__ == "__main__":
    main()
