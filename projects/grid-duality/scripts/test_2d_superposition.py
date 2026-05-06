"""2D superposition / linearity test.

Static-field tests with one source vs two: does the combined field equal
the sum of individual responses? In gravity (and electromagnetism), the
potential is linear — a key property used to add up many bodies. Lattice
models that pass the gravity static-field test should also obey
superposition.

Setup: same 2D hex torus and Dirichlet pinning as test_2d_static_field.
Run three configurations per model:

  1. Source A pinned at +0.3, sink ring at 0
  2. Source B pinned at +0.3 (different node), sink ring at 0
  3. Both A and B pinned at +0.3, sink ring at 0

Measure linearity by computing the per-node correlation between
(v_A + v_B) and v_AB after a linear best-fit rescaling.

Run:
    cd projects/grid-duality/scripts
    python test_2d_superposition.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from engine import make_2d_hex_torus
from models import NormalizedTelegrapher, Scattering

from test_2d_static_field import (
    torus_distances, pin_state, run_with_pins, rescaled_match,
)


OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)


def settled_field(model, lattice, pinned_idxs, pinned_vals, n_steps, damping):
    history, _ = run_with_pins(
        model, lattice, pinned_idxs, pinned_vals, n_steps, damping=damping
    )
    return history[3 * n_steps // 4:].mean(axis=0)


def build_pin_arrays(distances_a, distances_b, source_a, source_b,
                     source_value, sink_dist_min, mode):
    """Return (idxs, vals) for one of three modes: 'A', 'B', 'AB'.

    The sink ring is the union of nodes at distance ≥ sink_dist_min from
    EITHER source — this guarantees consistent boundary geometry across
    runs (so v_A + v_B and v_AB share the same Dirichlet BC structure)."""
    sink_mask = (distances_a >= sink_dist_min) & (distances_b >= sink_dist_min)
    sink_mask[source_a] = False
    sink_mask[source_b] = False
    sink_idxs = np.where(sink_mask)[0]

    if mode == "A":
        src_idxs = [source_a]
        src_vals = [source_value]
    elif mode == "B":
        src_idxs = [source_b]
        src_vals = [source_value]
    else:  # 'AB'
        src_idxs = [source_a, source_b]
        src_vals = [source_value, source_value]
    pinned_idxs = np.concatenate([src_idxs, sink_idxs]).astype(int)
    pinned_vals = np.concatenate([src_vals, np.zeros(len(sink_idxs))])
    return pinned_idxs, pinned_vals


def main():
    nx, ny = 25, 25
    n_steps = 800
    damping = 0.02
    source_value = 0.3
    sink_dist_min = 9.0

    lattice = make_2d_hex_torus(nx, ny)
    centre = lattice.positions.mean(axis=0)
    # Source A: closest to centre−offset; source B: closest to centre+offset
    offset = np.array([3.0, 0.0])
    source_a = int(np.argmin(np.linalg.norm(
        lattice.positions - (centre - offset), axis=1)))
    source_b = int(np.argmin(np.linalg.norm(
        lattice.positions - (centre + offset), axis=1)))
    distances_a = torus_distances(lattice, nx, ny, source_a)
    distances_b = torus_distances(lattice, nx, ny, source_b)

    print(f"Lattice: 2D hex torus, {nx}×{ny} cells ({lattice.n_nodes} nodes)")
    print(f"Source A: node {source_a}; Source B: node {source_b}")
    print(f"Separation: {np.linalg.norm(lattice.positions[source_a] - lattice.positions[source_b]):.2f}")
    print(f"Sink ring: distance ≥ {sink_dist_min} from BOTH sources")
    print()

    # Region of interest: nodes inside both sink rings (the unpinned interior).
    interior_mask = (distances_a < sink_dist_min) & (distances_b < sink_dist_min)
    interior_mask[source_a] = False  # exclude pinned points themselves
    interior_mask[source_b] = False

    fig, axes = plt.subplots(2, 4, figsize=(20, 9))

    summary = {}
    for row, ModelCls in enumerate([NormalizedTelegrapher, Scattering]):
        model = ModelCls()
        print(f"--- Model: {model.name} ---")

        # Run three configurations
        fields = {}
        for mode in ["A", "B", "AB"]:
            pinned_idxs, pinned_vals = build_pin_arrays(
                distances_a, distances_b, source_a, source_b,
                source_value, sink_dist_min, mode,
            )
            fields[mode] = settled_field(
                model, lattice, pinned_idxs, pinned_vals, n_steps, damping,
            )

        sum_AB = fields["A"] + fields["B"]
        joint_AB = fields["AB"]

        match = rescaled_match(sum_AB, joint_AB, interior_mask)
        if match:
            print(f"  rescaled match (v_A+v_B vs v_AB): a={match['a']:+.4f}, b={match['b']:+.4f}, R²={match['r2']:.4f}")
            # Direct (un-rescaled) per-node ratio
            denom = sum_AB[interior_mask]
            num = joint_AB[interior_mask]
            valid = np.abs(denom) > 1e-6
            if valid.any():
                ratio = num[valid] / denom[valid]
                print(f"  direct ratio v_AB / (v_A+v_B): mean={ratio.mean():+.4f}, "
                      f"std={ratio.std():.4f}  (target: mean=1, std=0)")

        summary[model.name] = match

        # Visualize
        cmap_range = max(np.abs(joint_AB).max() * 1.05, 1e-6)
        for col, (label, field) in enumerate(
            [("v_A", fields["A"]), ("v_B", fields["B"]),
             ("v_A + v_B", sum_AB), ("v_AB (joint)", joint_AB)]
        ):
            ax = axes[row, col]
            sc = ax.scatter(
                lattice.positions[:, 0], lattice.positions[:, 1],
                c=field, cmap="RdBu_r",
                vmin=-cmap_range, vmax=cmap_range, s=14, edgecolor="none",
            )
            ax.set_title(f"{model.name}: {label}", fontsize=10)
            ax.set_aspect("equal")
            ax.set_xticks([]); ax.set_yticks([])
            plt.colorbar(sc, ax=ax, fraction=0.046)
        print()

    fig.suptitle("Superposition test: does v_A + v_B = v_AB? "
                 "(linearity of static field)", fontsize=12)
    plt.tight_layout()
    out = os.path.join(OUTDIR, "superposition-2d.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")

    print("\n=== Summary ===")
    print(f"  {'model':18s}  {'fit a':>10s}  {'fit b':>10s}  {'R²':>10s}")
    print(f"  {'-'*18}  {'-'*10}  {'-'*10}  {'-'*10}")
    for name, match in summary.items():
        if match:
            a = f"{match['a']:+.4f}"
            b = f"{match['b']:+.4f}"
            r2 = f"{match['r2']:.4f}"
            print(f"  {name:18s}  {a:>10s}  {b:>10s}  {r2:>10s}")
        else:
            print(f"  {name:18s}  {'—':>10s}  {'—':>10s}  {'—':>10s}")


if __name__ == "__main__":
    main()
