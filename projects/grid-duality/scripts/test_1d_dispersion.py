"""1D dispersion / group-velocity test.

Send a Gaussian-modulated sinusoidal wavepacket of carrier wavevector k on
a 1D periodic ring. Track the envelope centroid over time. Linear fit of
position vs step gives the group velocity v_g(k).

A non-dispersive medium (continuum wave equation) would give v_g(k) = c
constant. Lattice models always show some dispersion at large k (close to
the lattice cutoff at k = π). The shape of v_g(k) is a model fingerprint:

- Normalized telegrapher: standard wave equation discretization →
  v_g(k) ∝ cos(k/2) (or similar), monotone-decreasing in |k|.
- Scattering (sim-maxwell):  unitary scattering matrix at each vertex →
  potentially different v_g(k); depends on the model's exact dispersion.

In 1D with coord 2, both should propagate cleanly without amplification,
so this test should run stably.

Run:
    cd projects/grid-duality/scripts
    python test_1d_dispersion.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from engine import make_1d_periodic
from models import NormalizedTelegrapher, RelativeCosBoth, Scattering


OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)


def envelope_centroid(field, n):
    """Circular centroid of |field|² on a ring of `n` nodes — returns
    a float position in [0, n). Uses the complex-exponential trick to
    avoid wrap-around discontinuities."""
    pwr = np.abs(field) ** 2
    if pwr.sum() < 1e-30:
        return None
    angles = 2 * np.pi * np.arange(n) / n
    z = (pwr * np.exp(1j * angles)).sum()
    return (n / (2 * np.pi)) * (np.angle(z) % (2 * np.pi))


def unwrap_position(positions, n):
    """Unwrap a sequence of circular positions ∈ [0, n) into a continuous
    real-valued path, assuming step-to-step motion is smaller than n/2."""
    out = [positions[0]]
    for p in positions[1:]:
        d = p - out[-1]
        d = ((d + n / 2) % n) - n / 2
        out.append(out[-1] + d)
    return np.array(out)


def init_packet_1d(model, lattice, k, x0, sigma, amplitude):
    """Initialize a Gaussian-modulated sinusoidal wavepacket on a 1D ring.

    For v-i (Normalized): v on nodes is the wavepacket; i on edges is set
    so the wave moves to the right (the canonical right-moving solution
    of the discrete wave equation).

    For Scattering: a_fwd = wavepacket on each edge, a_bwd = 0 (wave only
    on the forward channel = right-moving).
    """
    n = lattice.n_nodes
    x = np.arange(n)
    env = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2))
    v_node = amplitude * env * np.cos(k * x)
    # right-moving wave: i_e = v_tail (in the discrete telegrapher,
    # right-moving => i_+ ≈ v on the same edge).
    i_edge = amplitude * env * np.cos(k * x)  # along edge tail position

    state = model.init_state(lattice)
    if isinstance(model, Scattering):
        return {"a_fwd": i_edge.copy(), "a_bwd": np.zeros(lattice.n_edges)}
    for ni in range(n):
        state = model.perturb_node(state, ni, v_node[ni])
    for ei in range(lattice.n_edges):
        state = model.perturb_edge(state, ei, i_edge[ei])
    return state


def measure_group_velocity(model, lattice, k, n_steps,
                           sigma=8.0, amplitude=0.05):
    """Run the model with an initial wavepacket of carrier k. Return
    (v_g, positions_unwrapped)."""
    n = lattice.n_nodes
    x0 = n // 4  # start a quarter of the way around
    state = init_packet_1d(model, lattice, k, x0, sigma, amplitude)

    positions = []
    for step in range(n_steps + 1):
        field = model.node_observable(state)
        c = envelope_centroid(field, n)
        if c is None:
            return None, None
        positions.append(c)
        if step < n_steps:
            state = model.update(state, lattice)

    pos_unwrapped = unwrap_position(np.array(positions), n)
    # Linear fit position vs step over a stable window (skip first 4 to
    # avoid transient).
    t = np.arange(len(pos_unwrapped))
    if len(pos_unwrapped) < 10:
        return None, pos_unwrapped
    skip = 4
    coef = np.polyfit(t[skip:], pos_unwrapped[skip:], 1)
    v_g = coef[0]
    return v_g, pos_unwrapped


def main():
    n_ring = 256
    n_steps = 80
    ks = np.linspace(0.1, np.pi - 0.1, 30)
    sigma = 12.0
    amplitude = 0.05

    lattice = make_1d_periodic(n_ring)
    print(f"1D periodic ring: {n_ring} nodes")
    print(f"Steps per run: {n_steps}; wavepacket σ={sigma}, A={amplitude}")
    print(f"Sweep over k ∈ [{ks[0]:.2f}, {ks[-1]:.2f}] ({len(ks)} values)")
    print()

    vg_results = {}
    paths_at_kmid = {}
    k_mid_idx = len(ks) // 2

    for ModelCls in [NormalizedTelegrapher, RelativeCosBoth, Scattering]:
        model = ModelCls()
        print(f"--- Model: {model.name} ---")
        v_gs = []
        for i, k in enumerate(ks):
            v_g, path = measure_group_velocity(
                model, lattice, k, n_steps,
                sigma=sigma, amplitude=amplitude,
            )
            v_gs.append(v_g if v_g is not None else np.nan)
            if i == k_mid_idx:
                paths_at_kmid[model.name] = path
        v_gs = np.array(v_gs)
        finite = np.isfinite(v_gs)
        if finite.any():
            print(f"  v_g range: [{np.nanmin(v_gs):+.3f}, {np.nanmax(v_gs):+.3f}]")
            print(f"  v_g at k≈π/2: {v_gs[k_mid_idx]:+.4f}")
            print(f"  mean |v_g|: {np.nanmean(np.abs(v_gs)):.4f}")
        vg_results[model.name] = v_gs
        print()

    # ── Plot ─────────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Panel 1: v_g vs k
    ax = axes[0]
    for name, v_gs in vg_results.items():
        ax.plot(ks, v_gs, "o-", label=name, markersize=4, linewidth=1.4)
    # Continuum reference: cos(k/2) is the dispersion of the simplest
    # leapfrog discretization on a unit lattice with c = 1.
    ax.plot(ks, np.cos(ks / 2), "k--", linewidth=1.0,
            label="cos(k/2) (leapfrog continuum ref)")
    ax.axhline(1.0, color="grey", linestyle=":", alpha=0.5,
               label="v=1 (max for nondispersive c=1)")
    ax.set_xlabel("wavevector k (rad/site)")
    ax.set_ylabel("group velocity v_g")
    ax.set_title("Dispersion: v_g(k) per model")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 2: example path at mid-k
    ax = axes[1]
    for name, path in paths_at_kmid.items():
        if path is not None:
            ax.plot(path, label=name, linewidth=1.4)
    ax.set_xlabel("clock step")
    ax.set_ylabel("envelope position (unwrapped)")
    ax.set_title(f"Wavepacket trajectory at k ≈ {ks[k_mid_idx]:.2f}")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3)

    fig.suptitle(f"1D dispersion test ({n_ring}-node ring)")
    plt.tight_layout()
    out = os.path.join(OUTDIR, "dispersion-1d.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")

    # ── Summary ─────────────────────────────────────────────────
    print("\n=== Summary ===")
    print(f"  {'model':18s}  {'v_g(π/4)':>10s}  {'v_g(π/2)':>10s}  {'v_g(3π/4)':>10s}  {'mean|v_g|':>10s}")
    print(f"  {'-'*18}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")
    k_indices = {
        "π/4": int(np.argmin(np.abs(ks - np.pi / 4))),
        "π/2": int(np.argmin(np.abs(ks - np.pi / 2))),
        "3π/4": int(np.argmin(np.abs(ks - 3 * np.pi / 4))),
    }
    for name, v_gs in vg_results.items():
        c1 = f"{v_gs[k_indices['π/4']]:+.3f}"
        c2 = f"{v_gs[k_indices['π/2']]:+.3f}"
        c3 = f"{v_gs[k_indices['3π/4']]:+.3f}"
        c4 = f"{np.nanmean(np.abs(v_gs)):.3f}"
        print(f"  {name:18s}  {c1:>10s}  {c2:>10s}  {c3:>10s}  {c4:>10s}")


if __name__ == "__main__":
    main()
