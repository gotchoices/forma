"""Side-test: bounded vs unbounded phase in v-i models.

The default v-i candidates (Telegrapher, Normalized, RelCos-both) carry
the node variable v on the compact U(1) circle [0, 2π) — every step
applies (v + delta) % 2π, discarding any winding accumulation. The
question for this test: is that wrap doing thermodynamic work (enabling
relaxation by discarding winding entropy), or is it purely a
representational choice with no dynamical role?

Each affected model now has a `wrap_node` class attribute (default
True). Setting it to False on an instance turns v into an unbounded ℝ
variable: no mod 2π, no principal-branch reduction in the edge update.
This script runs two probes against each (model, wrap) combination:

  Probe 1 — 2D stability (S1 analog).
    Localised Gaussian on a 14×14 hex torus, 100 steps. Energy ratio
    final / initial. Tests whether removing the wrap changes the
    stability signature.

  Probe 2 — Dirichlet relaxation (G2 analog).
    Pinned source at centre, pinned sink ring, 800 steps with damping
    0.02, time-averaged field over the last quarter. Compares to the
    analytical graph-Laplacian solve. Tests whether removing the wrap
    changes the model's ability to relax to the static solution.

Models in scope: Telegrapher, RelCos-both. Normalized is also affected
by the flag and is included as a control (its bounded version is the
"good" relaxer; we expect the unbounded version to behave similarly
since v stays small in stable regimes).

Run:
    cd projects/grid-duality/scripts
    python test_unbounded_phase.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from engine import make_2d_hex_torus
from models import Telegrapher, NormalizedTelegrapher, RelativeCosBoth

from test_2d_pulse import gaussian_at_center, run_simulation
from test_2d_static_field import (
    laplacian_solve, pin_indices_value_pairs, run_with_pins,
    torus_distances, fit_log, fit_power, rescaled_match,
)


OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)


def make_variant(ModelCls, wrap_node):
    """Instantiate `ModelCls` with the chosen wrap_node flag. Returns the
    model and a label suitable for plots."""
    model = ModelCls()
    model.wrap_node = wrap_node
    label_suffix = "" if wrap_node else "-unbounded"
    label = f"{model.name}{label_suffix}"
    return model, label


def probe_stability(model, lattice, n_steps=100, amplitude=0.5, width=1.5):
    """2D Gaussian-pulse stability test. Returns final/initial energy
    ratio and the energy trace."""
    perturb_fn = gaussian_at_center(amplitude=amplitude, width=width)(lattice)
    history = run_simulation(model, lattice, perturb_fn, n_steps)
    energies = history["energy"]
    return {
        "ratio": energies[-1] / max(energies[0], 1e-12),
        "energies": energies,
    }


def probe_relaxation(model, lattice, distances, pinned_idxs, pinned_vals,
                     v_ref, fit_r_min, fit_r_max, interior_mask,
                     n_steps=800, damping=0.02):
    """Dirichlet-pinning relaxation test. Returns log fit, force-law
    fit, and per-node match-to-Laplacian R²."""
    history, energies = run_with_pins(
        model, lattice, pinned_idxs, pinned_vals, n_steps, damping=damping,
    )
    avg_field = history[3 * n_steps // 4:].mean(axis=0)
    log_fit = fit_log(distances, np.abs(avg_field), fit_r_min, fit_r_max)
    pwr_fit = fit_power(distances, np.abs(avg_field), fit_r_min, fit_r_max)
    match = rescaled_match(avg_field, v_ref, interior_mask)
    return {
        "energy_ratio": energies[-1] / max(energies[0], 1e-12),
        "energy_max": float(energies.max()),
        "log_fit": log_fit,
        "pwr_fit": pwr_fit,
        "match": match,
    }


def main():
    # ── Stability probe ──────────────────────────────────────────────
    nx_s, ny_s = 14, 14
    lattice_stab = make_2d_hex_torus(nx_s, ny_s)
    print(f"Stability probe: 2D hex torus {nx_s}x{ny_s} ({lattice_stab.n_nodes} nodes), 100 steps")
    print(f"  Default wrap_node=True is the existing model. wrap_node=False removes mod 2π.")
    print()

    stability_results = {}
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

    for col, ModelCls in enumerate([Telegrapher, NormalizedTelegrapher, RelativeCosBoth]):
        ax = axes[col]
        for wrap_node, color, dash in [(True, "C0", "-"), (False, "C3", "--")]:
            model, label = make_variant(ModelCls, wrap_node)
            res = probe_stability(model, lattice_stab)
            stability_results[label] = res
            ax.semilogy(res["energies"], color=color, linestyle=dash,
                        label=f"wrap={wrap_node} (ratio {res['ratio']:.2g})")
        ax.set_title(f"{ModelCls.__name__}: 2D pulse, 100 steps")
        ax.set_xlabel("step"); ax.set_ylabel("total energy (log)")
        ax.legend(loc="best", fontsize=9)
        ax.grid(alpha=0.3)

    fig.suptitle("Stability probe: bounded (solid) vs unbounded (dashed) phase", fontsize=12)
    plt.tight_layout()
    out_s = os.path.join(OUTDIR, "unbounded-stability.png")
    plt.savefig(out_s, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"  wrote {out_s}\n")

    # ── Relaxation probe ─────────────────────────────────────────────
    nx_r, ny_r = 25, 25
    lattice_rel = make_2d_hex_torus(nx_r, ny_r)
    centre = lattice_rel.positions.mean(axis=0)
    source_idx = int(np.argmin(np.linalg.norm(lattice_rel.positions - centre, axis=1)))
    distances = torus_distances(lattice_rel, nx_r, ny_r, source_idx)
    sink_dist_min = 9.0
    fit_r_min = 1.5
    fit_r_max = sink_dist_min - 0.5
    pinned_idxs, pinned_vals = pin_indices_value_pairs(
        distances, source_idx, 0.3, sink_dist_min,
    )
    interior_mask = (distances >= fit_r_min) & (distances <= fit_r_max)
    v_ref = laplacian_solve(lattice_rel, pinned_idxs, pinned_vals)

    print(f"Relaxation probe: 2D hex torus {nx_r}x{ny_r} ({lattice_rel.n_nodes} nodes)")
    print(f"  Source pinned at {source_idx}, sink ring at distance ≥ {sink_dist_min}")
    print(f"  800 steps, damping=0.02; comparing to analytical graph Laplacian solve.\n")

    relax_results = {}
    for ModelCls in [Telegrapher, NormalizedTelegrapher, RelativeCosBoth]:
        for wrap_node in [True, False]:
            model, label = make_variant(ModelCls, wrap_node)
            print(f"--- {label} ---")
            try:
                res = probe_relaxation(
                    model, lattice_rel, distances,
                    pinned_idxs, pinned_vals,
                    v_ref, fit_r_min, fit_r_max, interior_mask,
                )
                relax_results[label] = res
                e_max = res["energy_max"]
                e_ratio = res["energy_ratio"]
                print(f"  energy: peak {e_max:.2f}, final/initial {e_ratio:.3g}")
                if res["log_fit"]:
                    print(f"  log fit:   slope {res['log_fit']['B']:+.4f}, R²={res['log_fit']['r2']:.4f}")
                if res["pwr_fit"]:
                    print(f"  force fit: p {res['pwr_fit']['p']:+.4f}, R²={res['pwr_fit']['r2']:.4f}")
                if res["match"]:
                    print(f"  match to Laplacian: a={res['match']['a']:+.4f}, R²={res['match']['r2']:.4f}")
            except Exception as e:
                print(f"  exception: {e}")
                relax_results[label] = None
            print()

    # ── Summary ──────────────────────────────────────────────────────
    print("=== Stability summary ===")
    print(f"  {'model':28s}  {'energy ratio (100 steps)':>26s}")
    print(f"  {'-'*28}  {'-'*26}")
    for label, res in stability_results.items():
        print(f"  {label:28s}  {res['ratio']:>26.4g}")

    print("\n=== Relaxation summary ===")
    print(f"  {'model':28s}  {'log slope':>12s}  {'force p':>10s}  {'match R²':>10s}  {'peak energy':>12s}")
    print(f"  {'-'*28}  {'-'*12}  {'-'*10}  {'-'*10}  {'-'*12}")
    for label, res in relax_results.items():
        if res is None:
            print(f"  {label:28s}  {'(crash)':>12s}  {'—':>10s}  {'—':>10s}  {'—':>12s}")
            continue
        # Clamp ridiculous overflow values so the table stays readable.
        def _fmt(val, fmt):
            if val is None or not np.isfinite(val):
                return "overflow"
            if abs(val) > 1e6:
                return f"{val:.1e}"
            return f"{val:{fmt}}"
        b = _fmt(res["log_fit"]["B"], "+.4f") if res["log_fit"] else "—"
        p = _fmt(res["pwr_fit"]["p"], "+.4f") if res["pwr_fit"] else "—"
        mr2 = _fmt(res["match"]["r2"], ".4f") if res["match"] else "—"
        em = _fmt(res["energy_max"], ".2g")
        print(f"  {label:28s}  {b:>12s}  {p:>10s}  {mr2:>10s}  {em:>12s}")


if __name__ == "__main__":
    main()
