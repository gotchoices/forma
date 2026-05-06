"""Fair-shake IC test for RelCos-both.

The reviewer noted that the test bench's standard IC (v = A·env·cos(k·x),
i matched) treats v as a wave amplitude — natural for v-i Telegrapher,
but possibly inconsistent with RelCos-both's compass-dial interpretation,
where v should encode a *heading*. The reviewer's suggested alternative:
v constant (= the direction of intended motion), i alone carrying the
wave envelope.

This script reruns the two RelCos-both light-carrier tests under both
ICs to check whether the model's failures are intrinsic or specific to
the v-amplitude IC translation:

  Probe A — 2D directional wavefront on a 20×12 hex torus, 80 steps.
            Propagation direction +x (= 0°).
              IC-standard:  v = A·env·cos(k·x_along), i = matched
              IC-dial:      v = 0 (compass pointing +x), i = wavepacket only

  Probe B — Y-junction (3 arms × 60 nodes, coord-3 centre), 90 steps.
            Wavepacket inbound on arm 0 (toward centre).
              IC-standard:  v = wavepacket, i = −v (left-mover)
              IC-dial:      v = π everywhere (compass pointing −x toward
                            the centre on arm 0; constant elsewhere as a
                            uniform background), i = wavepacket only on
                            arm 0 edges

For each probe, report energy conservation, propagation pattern, and
matched-impedance fractions where applicable. If the dial-aware IC
shows substantially better behavior, RelCos-both's verdict in chapter 4
needs revision; if it shows comparable failure, the verdict stands and
the failures are intrinsic to the model.

Run:
    cd projects/grid-duality/scripts
    python test_relcos_dial_ic.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from engine import make_2d_hex_torus, make_y_tree
from models import RelativeCosBoth

from test_2d_wavefront import init_directional_wavefront, run_simulation_with_initial_state
from test_y_junction import (
    init_inbound_packet, per_arm_energy,
    arm_node_indices, arm_edge_indices,
)


OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)


# ---------- Probe A: 2D directional wavefront ----------

def init_dial_aware_wavefront(model, lattice, amplitude=0.3, k=0.6,
                              direction_deg=0.0, envelope_width=3.0):
    """Dial-aware IC: v = 0 everywhere (compass pointing +x for
    direction_deg=0); i carries the wavepacket. Mirrors the geometry of
    test_2d_wavefront.init_directional_wavefront's edge_i but does not
    set v on nodes."""
    direction = np.deg2rad(direction_deg)
    k_hat = np.array([np.cos(direction), np.sin(direction)])
    state = model.init_state(lattice)
    centre = lattice.positions.mean(axis=0)

    # Per-edge envelope and amplitude — wave travels along k_hat.
    edge_along = np.empty(lattice.n_edges)
    for ei in range(lattice.n_edges):
        tail_pos = lattice.positions[lattice.tails[ei]]
        disp_edge = lattice.edge_displacements[ei]
        edge_pos = tail_pos + 0.5 * disp_edge
        edge_along[ei] = float(np.dot(edge_pos - centre, k_hat))
    edge_env = np.exp(-edge_along ** 2 / (2.0 * envelope_width ** 2))
    edge_amp = amplitude * edge_env * np.cos(k * edge_along)
    edge_proj = np.cos(lattice.theta - direction)
    edge_i = edge_amp * edge_proj

    # Set v = 0 (already zeros from init_state). Set i on edges.
    for ei in range(lattice.n_edges):
        state = model.perturb_edge(state, ei, edge_i[ei])
    return state


def run_wavefront_probe():
    nx, ny = 20, 12
    n_steps = 80
    lattice = make_2d_hex_torus(nx, ny)
    print(f"== Probe A: 2D directional wavefront ({nx}×{ny} hex torus, {n_steps} steps) ==\n")

    results = {}
    for label, init_fn in [
        ("standard-IC", init_directional_wavefront),
        ("dial-aware-IC", init_dial_aware_wavefront),
    ]:
        model = RelativeCosBoth()
        initial_state = init_fn(model, lattice, amplitude=0.3, k=0.6,
                                direction_deg=0.0, envelope_width=3.0)
        history = run_simulation_with_initial_state(
            model, lattice, initial_state, n_steps,
        )
        e0, eF = history["energy"][0], history["energy"][-1]
        ratio = eF / max(e0, 1e-12)
        e_max = history["energy"].max()
        # Wavefront propagation: max |v| at last step (probe of activity).
        nv = history["node_values"]
        late_amp = np.abs(nv[-1]).max()
        early_amp = np.abs(nv[0]).max()
        results[label] = {
            "ratio": ratio, "e_max": e_max,
            "early_amp": early_amp, "late_amp": late_amp,
            "history": history,
        }
        print(f"  {label}:")
        print(f"    energy: {e0:.4f} → {eF:.4f} (ratio {ratio:.3g}; peak {e_max:.4f})")
        print(f"    node max |v|: t=0 → {early_amp:.4f}, t={n_steps} → {late_amp:.4f}")
        print()

    # Side-by-side snapshots at end-of-run
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, (label, res) in zip(axes, results.items()):
        nv_late = res["history"]["node_values"][-1]
        sc = ax.scatter(
            lattice.positions[:, 0], lattice.positions[:, 1],
            c=nv_late, cmap="RdBu_r", s=24, edgecolor="none",
        )
        vmax = max(np.abs(nv_late).max(), 1e-9)
        sc.set_clim(-vmax, vmax)
        ax.set_title(f"RelCos-both, {label}\nstep {n_steps}, energy ratio {res['ratio']:.2g}")
        ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
        plt.colorbar(sc, ax=ax, fraction=0.046)
    fig.suptitle("Wavefront probe: standard IC vs dial-aware IC", fontsize=12)
    plt.tight_layout()
    out = os.path.join(OUTDIR, "relcos-dial-ic-wavefront.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"  wrote {out}\n")
    return results


# ---------- Probe B: Y-junction with dial-aware IC ----------

def init_dial_aware_y_packet(model, lattice, arm_length, x0=35.0, k=0.4,
                             sigma=5.0, amplitude=0.3, dial_direction=np.pi):
    """Dial-aware Y-junction IC: v = `dial_direction` everywhere
    (e.g., π = pointing −x = into the centre along arm 0), and i carries
    the wavepacket on arm 0 edges only."""
    state = model.init_state(lattice)
    arm_edges = arm_edge_indices(arm_length)

    # Set v = dial_direction on every node.
    for ni in range(lattice.n_nodes):
        # perturb_node accumulates; init_state has v=0, so this sets v.
        state = model.perturb_node(state, ni, dial_direction)

    # Set i on arm 0 edges, encoding a wavepacket inbound toward the centre.
    for ei_local, ei in enumerate(arm_edges[0]):
        r = ei_local + 0.5
        env = np.exp(-((r - x0) ** 2) / (2 * sigma ** 2))
        # i sign: for v-i wave inbound toward centre (decreasing arm-index),
        # i = +v_envelope (since arm 0 edges point outward, "toward centre"
        # means a wave whose i is sign-aligned with the +x edge direction
        # but envelope on the far end of the arm).
        state = model.perturb_edge(state, ei, amplitude * env * np.cos(k * r))
    return state


def run_y_junction_probe():
    arm_length = 60
    n_steps = 90
    lattice = make_y_tree(arm_length)
    arm_edges = arm_edge_indices(arm_length)
    arm_nodes = arm_node_indices(arm_length)
    print(f"== Probe B: Y-junction (3 arms × {arm_length}, {n_steps} steps) ==")
    print(f"  Theory: 0.1111 / 0.4444 / 0.4444 (R²=1/9, T²=4/9 each)\n")

    # Use the same wavepacket parameters as test_y_junction.main() for an
    # apples-to-apples comparison with the chapter 4 result.
    packet_params = dict(x0=35.0, k=0.4, sigma=5.0, amplitude=0.3)
    results = {}
    for label, init_fn, extra_kwargs in [
        ("standard-IC", init_inbound_packet, {}),
        ("dial-aware-IC", init_dial_aware_y_packet,
         {"dial_direction": np.pi}),
    ]:
        model = RelativeCosBoth()
        state = init_fn(model, lattice, arm_length, **packet_params, **extra_kwargs)
        e_total_initial = float(model.total_energy(state))
        e_arm0_initial = sum(per_arm_energy(model, state, arm_edges, arm_nodes))
        history = [per_arm_energy(model, state, arm_edges, arm_nodes)]
        total_history = [e_total_initial]
        for _ in range(n_steps):
            state = model.update(state, lattice)
            history.append(per_arm_energy(model, state, arm_edges, arm_nodes))
            total_history.append(float(model.total_energy(state)))
        history = np.array(history)
        total_history = np.array(total_history)

        e_final = history[-1]
        total_final = e_final.sum()
        frac = e_final / max(total_final, 1e-12)
        energy_drift = (total_history[-1] - total_history[0]) / max(total_history[0], 1e-12)
        results[label] = {
            "fractions": frac, "energy_drift": energy_drift,
            "history": history, "total_history": total_history,
        }
        print(f"  {label}:")
        print(f"    arm 0 (reflected):    {frac[0]:.4f}  (theory 0.1111)")
        print(f"    arm 1 (transmitted):  {frac[1]:.4f}  (theory 0.4444)")
        print(f"    arm 2 (transmitted):  {frac[2]:.4f}  (theory 0.4444)")
        print(f"    total system energy drift: {energy_drift:+.4f}")
        print()

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    for ax, (label, res) in zip(axes, results.items()):
        for arm_i, arm_label in enumerate(
            ["arm 0 (reflected)", "arm 1 (transmitted)", "arm 2 (transmitted)"]
        ):
            ax.plot(res["history"][:, arm_i], linewidth=1.4, label=arm_label)
        ax.axhline(res["history"][0].sum() * (1/9), color="C0", linestyle=":",
                   alpha=0.5, label="theory R²")
        ax.axhline(res["history"][0].sum() * (4/9), color="C1", linestyle=":",
                   alpha=0.5, label="theory T² per arm")
        ax.set_xlabel("clock step"); ax.set_ylabel("arm energy")
        ax.set_title(f"RelCos-both, {label}\nenergy drift {res['energy_drift']:+.3f}")
        ax.legend(loc="best", fontsize=8)
        ax.grid(alpha=0.3)
    fig.suptitle("Y-junction probe: standard IC vs dial-aware IC", fontsize=12)
    plt.tight_layout()
    out = os.path.join(OUTDIR, "relcos-dial-ic-y-junction.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"  wrote {out}\n")
    return results


def main():
    wf = run_wavefront_probe()
    yj = run_y_junction_probe()

    print("=== Summary ===")
    print(f"  {'IC variant':16s}  {'wavefront ratio':>18s}  {'Y arm 0 (R)':>14s}  {'Y arm 1 (T)':>14s}  {'Y arm 2 (T)':>14s}  {'Y energy drift':>16s}")
    print(f"  {'-'*16}  {'-'*18}  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*16}")
    for label in ["standard-IC", "dial-aware-IC"]:
        r1 = wf[label]["ratio"]
        f = yj[label]["fractions"]
        d = yj[label]["energy_drift"]
        print(f"  {label:16s}  {r1:>18.3g}  {f[0]:>14.4f}  {f[1]:>14.4f}  {f[2]:>14.4f}  {d:>+16.4f}")

    print("\n  Theory at coord-3 Y-junction: 0.1111 / 0.4444 / 0.4444; energy drift 0")


if __name__ == "__main__":
    main()
