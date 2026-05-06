"""2D dispersion / group-velocity sweep on a hex torus (coord 3).

The 1D dispersion test (test_1d_dispersion.py) is uninformative for
Scattering: at coord 2 the scattering matrix S = (2/2)·J − I reduces to
a swap, so amplitudes propagate one site per step at every wavevector,
giving v_g = 1 trivially. This test confirms Scattering's
non-dispersive property at the more interesting coord 3.

Setup: 2D hex torus, large enough that a directional wavepacket has
room to travel without wrap-around effects within the run. For each
carrier wavevector k, launch a Gaussian-modulated cosine wavepacket
moving in +x. Project each node's contribution along +x, take a
weighted centroid of |v|², and linear-fit centroid-vs-time to extract
v_g(k).

A non-dispersive lattice gives v_g(k) = constant. Dispersion shows up
as v_g(k) varying with k.

Run:
    cd projects/grid-duality/scripts
    python test_2d_dispersion.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from engine import make_2d_hex_torus
from models import NormalizedTelegrapher, RelativeCosBoth, Scattering

from test_2d_wavefront import (
    init_directional_wavefront, run_simulation_with_initial_state,
)


OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)


def envelope_centroid_along_axis(field, positions, axis_unit, ref_position):
    """Weighted centroid of |field|² along `axis_unit`, relative to
    `ref_position`. Returns a scalar = projected position of the
    centroid along the axis."""
    pwr = np.abs(field) ** 2
    if pwr.sum() < 1e-30:
        return None
    along = (positions - ref_position) @ axis_unit
    return float((pwr * along).sum() / pwr.sum())


def measure_2d_group_velocity(model, lattice, k, direction_deg=0.0,
                              n_steps=20, sigma=4.0, amplitude=0.15,
                              fit_window=(3, 15)):
    """Initialize a directional wavepacket, track its centroid along the
    propagation axis over time, return v_g and the centroid trajectory.

    `fit_window` is a (start, end) slice over which the linear fit is
    taken. Default skips the first 3 steps (transient) and fits up to
    step 15, well before any torus wraparound effect."""
    direction = np.deg2rad(direction_deg)
    axis = np.array([np.cos(direction), np.sin(direction)])
    centre = lattice.positions.mean(axis=0)

    initial_state = init_directional_wavefront(
        model, lattice, amplitude=amplitude, k=k,
        direction_deg=direction_deg, envelope_width=sigma,
    )
    history = run_simulation_with_initial_state(
        model, lattice, initial_state, n_steps,
    )
    nv = history["node_values"]

    centroids = []
    for t in range(nv.shape[0]):
        c = envelope_centroid_along_axis(nv[t], lattice.positions, axis, centre)
        if c is None:
            return None, None
        centroids.append(c)
    centroids = np.array(centroids)

    fs, fe = fit_window
    fe = min(fe, len(centroids))
    if fe - fs < 4:
        return None, centroids
    t_arr = np.arange(len(centroids))
    coef = np.polyfit(t_arr[fs:fe], centroids[fs:fe], 1)
    v_g = float(coef[0])
    return v_g, centroids


def main():
    nx, ny = 40, 40
    n_steps = 18
    sigma = 4.0
    amplitude = 0.15
    ks = np.linspace(0.2, 2.6, 12)

    lattice = make_2d_hex_torus(nx, ny)
    print(f"2D hex torus: {nx}×{ny} cells ({lattice.n_nodes} nodes, {lattice.n_edges} edges)")
    print(f"Coord at every node: {int(lattice.coord.max())}")
    print(f"Wavepacket: A={amplitude}, σ={sigma}, direction +x; {n_steps} steps")
    print(f"k sweep: {len(ks)} values from {ks[0]:.2f} to {ks[-1]:.2f}")
    print()

    vg_results = {}
    paths_at_kmid = {}
    k_mid_idx = len(ks) // 2

    for ModelCls in [NormalizedTelegrapher, RelativeCosBoth, Scattering]:
        model = ModelCls()
        print(f"--- {model.name} ---")
        v_gs = []
        for i, k in enumerate(ks):
            v_g, path = measure_2d_group_velocity(
                model, lattice, k, n_steps=n_steps,
                sigma=sigma, amplitude=amplitude,
            )
            v_gs.append(v_g if v_g is not None else np.nan)
            if i == k_mid_idx:
                paths_at_kmid[model.name] = path
        v_gs = np.array(v_gs)
        finite_vals = v_gs[np.isfinite(v_gs)]
        if len(finite_vals) > 0:
            print(f"  v_g range: [{finite_vals.min():+.3f}, {finite_vals.max():+.3f}]")
            print(f"  v_g spread (max−min): {finite_vals.max() - finite_vals.min():.4f}")
            print(f"  v_g at k≈{ks[k_mid_idx]:.2f}: {v_gs[k_mid_idx]:+.4f}")
        vg_results[model.name] = v_gs
        print()

    # ── Plot ────────────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    for name, v_gs in vg_results.items():
        ax.plot(ks, v_gs, "o-", label=name, markersize=4, linewidth=1.4)
    ax.set_xlabel("wavevector k (rad/edge-length)")
    ax.set_ylabel("group velocity v_g")
    ax.set_title(f"2D hex (coord 3): v_g(k)")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3)

    ax = axes[1]
    for name, path in paths_at_kmid.items():
        if path is not None:
            ax.plot(path, label=name, linewidth=1.4)
    ax.set_xlabel("clock step")
    ax.set_ylabel("centroid position along +x")
    ax.set_title(f"Wavepacket trajectory at k ≈ {ks[k_mid_idx]:.2f}")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3)

    fig.suptitle(f"2D dispersion test (coord 3, hex torus {nx}×{ny})", fontsize=12)
    plt.tight_layout()
    out = os.path.join(OUTDIR, "dispersion-2d.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")

    # ── Summary ─────────────────────────────────────────────────────
    print("\n=== Summary (coord 3) ===")
    print(f"  {'model':18s}  {'v_g min':>10s}  {'v_g max':>10s}  {'spread':>10s}  {'mean v_g':>10s}")
    print(f"  {'-'*18}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")
    for name, v_gs in vg_results.items():
        finite_vals = v_gs[np.isfinite(v_gs)]
        if len(finite_vals) > 0:
            vmin = f"{finite_vals.min():+.4f}"
            vmax = f"{finite_vals.max():+.4f}"
            spread = f"{finite_vals.max() - finite_vals.min():.4f}"
            mean = f"{finite_vals.mean():+.4f}"
        else:
            vmin = vmax = spread = mean = "—"
        print(f"  {name:18s}  {vmin:>10s}  {vmax:>10s}  {spread:>10s}  {mean:>10s}")


if __name__ == "__main__":
    main()
