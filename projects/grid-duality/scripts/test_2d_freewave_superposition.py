"""Free-wave superposition test: linearity without Dirichlet pinning.

The reviewer noted that the L3 superposition test (test_2d_superposition.py)
inherits Dirichlet pinning from the gravity-style setup, which means
RelCos-both's failure there is dominated by its Dirichlet-pinning
instability rather than by an intrinsic free-wave nonlinearity. To
distinguish those two failure modes, this test launches *free* wavepackets
in a 2D hex bulk region and compares:

  v_AB(t) — single run with both wavepackets present from t=0
  v_A(t) + v_B(t) — sum of two single-wavepacket runs

A linear model satisfies v_AB = v_A + v_B for all t. The per-step deviation
diagnoses nonlinearity. RelCos-both is expected to be nonlinear in
free-wave dynamics too (the cos(θ − v) factor depends on v at each node),
but the nonlinearity may be small at the amplitudes used in chapter 4 and
swamped by the Dirichlet-pinning divergence in the original L3 test.

Setup: 2D hex torus (20×20). Two Gaussian-modulated cosine wavepackets
launched in opposite directions so they cross. Run for 60 steps with no
pins, no damping. Compare v_AB to v_A + v_B at each step.

Run:
    cd projects/grid-duality/scripts
    python test_2d_freewave_superposition.py
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


def superpose_initial_states(model, lattice, state_a, state_b):
    """Build a single initial state whose v and i (or scattering registers)
    are the additive sum of state_a's and state_b's.

    For v-i models (Telegrapher / Normalized / RelCos-both): adding v at
    nodes and i at edges. v is added before any wrap (mod 2π is applied
    once if wrap_node is True).
    For Scattering: a_fwd_AB = a_fwd_A + a_fwd_B; same for a_bwd."""
    if isinstance(model, Scattering):
        return {
            "a_fwd": state_a["a_fwd"] + state_b["a_fwd"],
            "a_bwd": state_a["a_bwd"] + state_b["a_bwd"],
        }
    raw_v = state_a["v"] + state_b["v"]
    if getattr(model, "wrap_node", True):
        v_combined = raw_v % (2 * np.pi)
    else:
        v_combined = raw_v
    return {
        "v": v_combined,
        "i": state_a["i"] + state_b["i"],
    }


def main():
    nx, ny = 20, 20
    n_steps = 60
    amplitude = 0.15
    k = 0.6
    envelope_width = 3.0

    lattice = make_2d_hex_torus(nx, ny)
    print(f"Free-wave superposition: 2D hex torus {nx}×{ny} ({lattice.n_nodes} nodes)")
    print(f"  Two wavepackets, A in +x direction, B in −x (so they cross)")
    print(f"  Amplitude {amplitude}, k={k}, σ={envelope_width}; {n_steps} steps; no pins")
    print()

    fig, axes = plt.subplots(3, 2, figsize=(12, 12))
    summary = {}

    for row, ModelCls in enumerate([NormalizedTelegrapher, RelativeCosBoth, Scattering]):
        model = ModelCls()
        # Three independent runs: A only, B only, A+B together.
        state_a = init_directional_wavefront(
            model, lattice, amplitude=amplitude, k=k,
            direction_deg=0.0, envelope_width=envelope_width,
        )
        state_b = init_directional_wavefront(
            model, lattice, amplitude=amplitude, k=k,
            direction_deg=180.0, envelope_width=envelope_width,
        )
        state_ab = superpose_initial_states(model, lattice, state_a, state_b)

        hist_a = run_simulation_with_initial_state(model, lattice, state_a, n_steps)
        hist_b = run_simulation_with_initial_state(model, lattice, state_b, n_steps)
        hist_ab = run_simulation_with_initial_state(model, lattice, state_ab, n_steps)

        nv_a = hist_a["node_values"]
        nv_b = hist_b["node_values"]
        nv_ab = hist_ab["node_values"]
        sum_AB = nv_a + nv_b

        # Per-step linearity error: ||v_AB − (v_A + v_B)|| / ||v_AB||.
        rel_err_per_step = np.zeros(nv_ab.shape[0])
        for t in range(nv_ab.shape[0]):
            num = np.linalg.norm(nv_ab[t] - sum_AB[t])
            den = max(np.linalg.norm(nv_ab[t]), 1e-12)
            rel_err_per_step[t] = num / den

        # End-of-run R²: how well does v_AB linearly fit (v_A + v_B)?
        from test_2d_static_field import rescaled_match
        match_final = rescaled_match(sum_AB[-1], nv_ab[-1], np.ones(lattice.n_nodes, dtype=bool))
        # Direct (unrescaled) ratio at the final step
        denom = sum_AB[-1]
        valid = np.abs(denom) > 1e-6
        if valid.any():
            ratio = nv_ab[-1][valid] / denom[valid]
            ratio_mean = float(ratio.mean())
            ratio_std = float(ratio.std())
        else:
            ratio_mean = ratio_std = float("nan")

        summary[model.name] = {
            "rel_err_max": rel_err_per_step.max(),
            "rel_err_mean": rel_err_per_step.mean(),
            "rel_err_per_step": rel_err_per_step,
            "match_R2": match_final["r2"] if match_final else None,
            "ratio_mean": ratio_mean,
            "ratio_std": ratio_std,
        }
        print(f"--- {model.name} ---")
        print(f"  per-step rel error ‖v_AB − (v_A + v_B)‖ / ‖v_AB‖:")
        print(f"    mean: {rel_err_per_step.mean():.4g}")
        print(f"    max:  {rel_err_per_step.max():.4g}")
        if match_final:
            print(f"  end-step rescaled match (v_A+v_B vs v_AB): R²={match_final['r2']:.4f}")
            print(f"  end-step direct ratio v_AB / (v_A+v_B): mean={ratio_mean:+.4f}, std={ratio_std:.4f}")
        print()

        # Plot per-step error
        ax = axes[row, 0]
        ax.semilogy(rel_err_per_step, linewidth=1.4)
        ax.set_xlabel("clock step")
        ax.set_ylabel("‖v_AB − (v_A+v_B)‖ / ‖v_AB‖  (log)")
        ax.set_title(f"{model.name}: per-step linearity error")
        ax.grid(alpha=0.3)

        # Scatter plot of per-node v_AB vs (v_A + v_B) at end of run
        ax = axes[row, 1]
        ax.scatter(sum_AB[-1], nv_ab[-1], s=4, alpha=0.4)
        # Identity reference line
        lo = min(sum_AB[-1].min(), nv_ab[-1].min())
        hi = max(sum_AB[-1].max(), nv_ab[-1].max())
        ax.plot([lo, hi], [lo, hi], "r--", linewidth=0.8, alpha=0.5,
                label="identity (linear)")
        ax.set_xlabel("v_A + v_B  (sum of single runs)")
        ax.set_ylabel("v_AB  (joint run)")
        ax.set_title(f"{model.name}: per-node, t={n_steps}")
        ax.legend(loc="best", fontsize=8)
        ax.grid(alpha=0.3)
        ax.set_aspect("equal", adjustable="datalim")

    fig.suptitle("Free-wave superposition test (no Dirichlet pinning, no damping)",
                 fontsize=12)
    plt.tight_layout()
    out = os.path.join(OUTDIR, "freewave-superposition.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}\n")

    # ── Summary ──
    print("=== Summary ===")
    print(f"  {'model':18s}  {'rel err mean':>14s}  {'rel err max':>14s}  {'match R²':>10s}  {'ratio mean':>12s}  {'ratio std':>12s}")
    print(f"  {'-'*18}  {'-'*14}  {'-'*14}  {'-'*10}  {'-'*12}  {'-'*12}")
    for name, res in summary.items():
        em = f"{res['rel_err_mean']:.3g}"
        ex = f"{res['rel_err_max']:.3g}"
        r2 = f"{res['match_R2']:.4f}" if res['match_R2'] is not None else "—"
        rm = f"{res['ratio_mean']:+.4f}"
        rs = f"{res['ratio_std']:.4f}"
        print(f"  {name:18s}  {em:>14s}  {ex:>14s}  {r2:>10s}  {rm:>12s}  {rs:>12s}")


if __name__ == "__main__":
    main()
