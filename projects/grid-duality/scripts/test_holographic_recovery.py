"""Holographic-recovery test for substrate quantization.

Tests the central hypothesis of grid-quantizing.md / chapter 5: at low
per-cell precision, can high macroscopic resolution be recovered by
*zooming out* — averaging the cell field over a large window? The answer
turns out to depend critically on the rounding scheme:

- **Deterministic rounding** (chapter 5 experiments A–D) produces
  *correlated* noise across neighboring cells, so spatial averaging does
  not cancel it. M ∝ 1/(N·ε)² scaling fails.
- **Stochastic rounding** produces *independent* noise across cells (each
  cell rounds randomly with probabilities tuned so that E[R(v)] = v).
  Averaging M cells gives standard error ~ amp_max / ((N−1)·√M),
  recovering the predicted M ∝ 1/(N−1)²/ε² scaling.

The minimum non-degenerate alphabet is **N = 2** (a single signed bit,
levels {−amp_max, +amp_max}). N = 1 carries no information. So the floor
is 1 bit per cell; with that, the holographic-window size for target
precision ε is M = (amp_max/ε)² cells.

This script tests the predictions on the existing 2D hex substrate.

Run:
    cd projects/grid-duality/scripts
    python test_holographic_recovery.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from engine import make_2d_hex_torus
from models import (
    Scattering, QuantizedScattering, StochasticQuantizedScattering,
)


OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)


# ---------- Smooth field setup ----------------------------------------------

def smooth_gaussian_field(lattice, amplitude=0.5, width_fraction=0.2):
    """Generate a smooth Gaussian field on the lattice. Returns the
    per-edge `a_fwd` values (with `a_bwd = 0`, so v_per_edge = a_fwd)."""
    centre = lattice.positions.mean(axis=0)
    # Use the diagonal of the bounding box as the natural length scale
    diag = np.linalg.norm(lattice.positions.max(axis=0) - lattice.positions.min(axis=0))
    width = width_fraction * diag

    edge_pos = np.empty((lattice.n_edges, 2))
    for ei in range(lattice.n_edges):
        tail_pos = lattice.positions[lattice.tails[ei]]
        disp = lattice.edge_displacements[ei]
        edge_pos[ei] = tail_pos + 0.5 * disp
    r2 = np.sum((edge_pos - centre) ** 2, axis=1)
    return amplitude * np.exp(-r2 / (2 * width ** 2))


# ---------- Windowed-average analysis ---------------------------------------

def windowed_error(true_field, quantized_field, edge_positions, centre,
                   window_radii):
    """For each window radius r, compute |⟨q⟩_window − ⟨t⟩_window| where
    the window is centered at `centre` with radius r. Returns arrays of
    M (cells in window) and abs error."""
    Ms = []
    errs = []
    for r in window_radii:
        d = np.linalg.norm(edge_positions - centre, axis=1)
        mask = d <= r
        M = mask.sum()
        if M < 1:
            continue
        true_avg = true_field[mask].mean()
        quant_avg = quantized_field[mask].mean()
        Ms.append(M)
        errs.append(abs(quant_avg - true_avg))
    return np.array(Ms), np.array(errs)


def windowed_error_many_centres(true_field, quantized_field, edge_positions,
                                window_radii, n_centres=12, rng=None):
    """Average windowed error over multiple window centres scattered
    across the lattice. Lattice is treated as periodic — the torus's
    natural metric is the wrapped (shortest-image) distance — but a
    simpler approximation is to choose centres well inside the
    bounding box and use Euclidean distance. Edges near the boundary
    that don't get the full window are simply excluded."""
    if rng is None:
        rng = np.random.default_rng(0)
    pos_min = edge_positions.min(axis=0)
    pos_max = edge_positions.max(axis=0)
    # Use centres clustered near the middle so all window radii fit.
    max_r = window_radii.max()
    margin = max_r + 1
    span = (pos_max - pos_min) - 2 * margin
    if np.any(span <= 0):
        # Fall back to single centroid
        centres = (pos_min + pos_max).reshape(1, 2) / 2
    else:
        centres = pos_min + margin + rng.random((n_centres, 2)) * span

    # For each radius, accumulate errors across all centres
    err_per_radius = [[] for _ in window_radii]
    M_per_radius = [[] for _ in window_radii]
    for c in centres:
        for ri, r in enumerate(window_radii):
            d = np.linalg.norm(edge_positions - c, axis=1)
            mask = d <= r
            M = mask.sum()
            if M < 1:
                continue
            true_avg = true_field[mask].mean()
            quant_avg = quantized_field[mask].mean()
            err_per_radius[ri].append(abs(quant_avg - true_avg))
            M_per_radius[ri].append(M)

    Ms = np.array([np.mean(M_per_radius[ri]) if M_per_radius[ri] else np.nan
                   for ri in range(len(window_radii))])
    err_mean = np.array([np.mean(err_per_radius[ri]) if err_per_radius[ri] else np.nan
                         for ri in range(len(window_radii))])
    err_std = np.array([np.std(err_per_radius[ri]) if err_per_radius[ri] else np.nan
                        for ri in range(len(window_radii))])
    valid = np.isfinite(Ms)
    return Ms[valid], err_mean[valid], err_std[valid]


# ---------- Experiments -----------------------------------------------------

def edge_positions_of(lattice):
    pos = np.empty((lattice.n_edges, 2))
    for ei in range(lattice.n_edges):
        tail_pos = lattice.positions[lattice.tails[ei]]
        disp = lattice.edge_displacements[ei]
        pos[ei] = tail_pos + 0.5 * disp
    return pos


def experiment_static(amplitude=0.3, amp_max=0.5, rng_seed=42):
    """STATIC test: take a CONSTANT field of value `amplitude`, quantize
    each edge with deterministic vs stochastic, sweep N. For each, plot
    windowed-average error vs window cell count M. A constant field
    isolates quantization noise from any field-variation bias, so a
    pure 1/√M scaling for stochastic is the predicted result.
    """
    print("=== Static holographic-recovery test (constant field) ===")
    nx, ny = 50, 50
    lattice = make_2d_hex_torus(nx, ny)
    edge_pos = edge_positions_of(lattice)
    diag = np.linalg.norm(lattice.positions.max(axis=0) - lattice.positions.min(axis=0))
    print(f"Lattice: {nx}×{ny} hex torus, {lattice.n_edges} edges, diag={diag:.1f}")
    print(f"Field: constant value {amplitude} on every edge (zero spatial bias)")

    true_field = np.full(lattice.n_edges, amplitude)

    # Window radii — sweep over a wide M range. With a constant field,
    # there's no upper bound on usable window size.
    window_radii = np.geomspace(0.5, diag * 0.4, 14)

    Ns = [None, 257, 17, 5, 3, 2]
    rng = np.random.default_rng(rng_seed)

    results = {}
    for N in Ns:
        # Deterministic
        if N is None:
            quant_det = true_field.copy()
            quant_sto = true_field.copy()
        else:
            det = QuantizedScattering(n_levels=N, amp_max=amp_max)
            quant_det = det._quantize(true_field)
            sto = StochasticQuantizedScattering(n_levels=N, amp_max=amp_max, rng=rng)
            quant_sto = sto._quantize(true_field)

        Ms_det, mean_det, std_det = windowed_error_many_centres(
            true_field, quant_det, edge_pos, window_radii, n_centres=20, rng=np.random.default_rng(rng_seed),
        )
        Ms_sto, mean_sto, std_sto = windowed_error_many_centres(
            true_field, quant_sto, edge_pos, window_radii, n_centres=20, rng=np.random.default_rng(rng_seed),
        )

        results[N] = {
            "det": {"M": Ms_det, "err_mean": mean_det, "err_std": std_det},
            "sto": {"M": Ms_sto, "err_mean": mean_sto, "err_std": std_sto},
        }
        label = f"N={N}" if N is not None else "N=∞"
        print(f"  {label:7s}: det max err = {mean_det.max():.4g}, sto max err = {mean_sto.max():.4g}")
    print()
    return results


def fit_powerlaw(M, err, mask=None):
    """Fit log(err) = a + b·log(M); return slope b."""
    if mask is None:
        mask = (err > 0) & (M > 0)
    if mask.sum() < 3:
        return None, None
    log_M = np.log(M[mask])
    log_e = np.log(err[mask])
    coef = np.polyfit(log_M, log_e, 1)
    return coef[0], np.exp(coef[1])  # slope, intercept


def experiment_dynamic(amp_max=0.5, n_steps=40, rng_seed=42):
    """DYNAMIC test: launch a smooth Gaussian pulse, run continuous and
    stochastic-quantized side by side. Compare the windowed-average field
    after several steps to confirm holographic recovery survives dynamics.
    """
    print("=== Dynamic holographic-recovery test ===")
    nx, ny = 50, 50
    lattice = make_2d_hex_torus(nx, ny)
    edge_pos = edge_positions_of(lattice)
    centre = lattice.positions.mean(axis=0)
    diag = np.linalg.norm(lattice.positions.max(axis=0) - lattice.positions.min(axis=0))

    # Initial state: smooth Gaussian on a_fwd, zero on a_bwd
    init_field = smooth_gaussian_field(lattice, amplitude=0.5, width_fraction=0.15)

    # Continuous run
    cont = Scattering()
    state_c = cont.init_state(lattice)
    state_c = {"a_fwd": init_field.copy(), "a_bwd": np.zeros(lattice.n_edges)}
    for _ in range(n_steps):
        state_c = cont.update(state_c, lattice)

    # Stochastic-quantized runs at several N
    Ns = [257, 17, 5, 3, 2]
    rng = np.random.default_rng(rng_seed)
    sto_results = {}
    for N in Ns:
        sto = StochasticQuantizedScattering(n_levels=N, amp_max=amp_max, rng=rng)
        state_q = sto.init_state(lattice)
        # Quantize the initial state
        state_q = {
            "a_fwd": sto._quantize(init_field.copy()),
            "a_bwd": sto._quantize(np.zeros(lattice.n_edges)),
        }
        for _ in range(n_steps):
            state_q = sto.update(state_q, lattice)
        sto_results[N] = state_q

    # Compare via windowed averaging — focus on a_fwd field
    window_radii = np.geomspace(0.5, diag * 0.4, 14)
    final_results = {}
    for N, sto_state in sto_results.items():
        Ms, mean_e, std_e = windowed_error_many_centres(
            state_c["a_fwd"], sto_state["a_fwd"], edge_pos, window_radii, n_centres=20,
            rng=np.random.default_rng(rng_seed),
        )
        final_results[N] = {"M": Ms, "err_mean": mean_e, "err_std": std_e}
        slope, _ = fit_powerlaw(Ms, mean_e)
        slope_str = f"{slope:.2f}" if slope is not None else "—"
        print(f"  N={N:3d}: max err = {mean_e.max():.4g}, fit slope log(err) ~ log(M)·{slope_str} (target -0.5 for 1/√M)")
    print()
    return final_results


# ---------- Plotting --------------------------------------------------------

def plot_results(static_results, dynamic_results):
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # Top-left: static, deterministic, error vs M for each N
    ax = axes[0, 0]
    for N, data in static_results.items():
        if N is None:
            continue
        m, e = data["det"]["M"], data["det"]["err_mean"]
        if len(m) > 0:
            ax.loglog(m, e + 1e-12, "o-", label=f"N={N}", linewidth=1.4, markersize=4)
    # Reference: 1/sqrt(M)
    M_ref = np.geomspace(1, 1e4, 50)
    ax.loglog(M_ref, 0.3 / np.sqrt(M_ref), "k--", linewidth=1, alpha=0.5, label="1/√M (ref)")
    ax.set_xlabel("M (cells per window)")
    ax.set_ylabel("|⟨quantized⟩ − ⟨true⟩|  (windowed mean err)")
    ax.set_title("Static, DETERMINISTIC rounding\n(noise correlated → averaging fails)")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3, which="both")

    # Top-right: static, stochastic, error vs M for each N
    ax = axes[0, 1]
    for N, data in static_results.items():
        if N is None:
            continue
        m, e = data["sto"]["M"], data["sto"]["err_mean"]
        if len(m) > 0:
            ax.loglog(m, e + 1e-12, "s-", label=f"N={N}", linewidth=1.4, markersize=4)
    ax.loglog(M_ref, 0.3 / np.sqrt(M_ref), "k--", linewidth=1, alpha=0.5, label="1/√M (ref)")
    ax.set_xlabel("M (cells per window)")
    ax.set_ylabel("|⟨quantized⟩ − ⟨true⟩|  (windowed mean err)")
    ax.set_title("Static, STOCHASTIC rounding\n(noise independent → averaging works)")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3, which="both")

    # Bottom-left: dynamic, stochastic, error vs M for each N
    ax = axes[1, 0]
    for N, data in dynamic_results.items():
        m, e = data["M"], data["err_mean"]
        if len(m) > 0:
            ax.loglog(m, e + 1e-12, "s-", label=f"N={N}", linewidth=1.4, markersize=4)
    ax.loglog(M_ref, 0.3 / np.sqrt(M_ref), "k--", linewidth=1, alpha=0.5, label="1/√M (ref)")
    ax.set_xlabel("M (cells per window)")
    ax.set_ylabel("|⟨quantized⟩ − ⟨continuum⟩|  (after T steps)")
    ax.set_title("Dynamic (after 40 steps), STOCHASTIC rounding\n(noise grows but holographic averaging holds)")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3, which="both")

    # Bottom-right: minimum N analysis
    ax = axes[1, 1]
    Ns = [N for N in static_results.keys() if N is not None]
    # Take the largest M data point for each N as representative
    Ms_eff = []
    err_det_at_M = []
    err_sto_at_M = []
    for N in Ns:
        d = static_results[N]
        if len(d["det"]["M"]) > 0:
            err_det_at_M.append(d["det"]["err_mean"][-1])
            err_sto_at_M.append(d["sto"]["err_mean"][-1])
            Ms_eff.append(d["det"]["M"][-1])
    ax.semilogx(Ns, err_det_at_M, "o-", color="C3", linewidth=1.4,
                markersize=6, label="deterministic")
    ax.semilogx(Ns, err_sto_at_M, "s-", color="C2", linewidth=1.4,
                markersize=6, label="stochastic")
    ax.set_xlabel("N (levels per cell)")
    ax.set_ylabel(f"err at largest window M ≈ {Ms_eff[0] if Ms_eff else '?':.0f}")
    ax.set_title("Error at largest window vs N\n(stochastic recovers as N drops; deterministic doesn't)")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3, which="both")

    fig.suptitle(
        "Holographic recovery: stochastic rounding gives 1/√M scaling at any N ≥ 2",
        fontsize=12,
    )
    plt.tight_layout()
    out = os.path.join(OUTDIR, "holographic-recovery.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")


def main():
    static = experiment_static()
    dynamic = experiment_dynamic()
    plot_results(static, dynamic)

    # Summary
    print("\n=== Slope summary (static, stochastic) ===")
    print(f"  {'N':>4s}  {'fit slope':>10s}  (target = −0.5 for 1/√M)")
    for N, data in static.items():
        if N is None:
            continue
        slope_sto, _ = fit_powerlaw(data["sto"]["M"], data["sto"]["err_mean"])
        slope_det, _ = fit_powerlaw(data["det"]["M"], data["det"]["err_mean"])
        sto_str = f"{slope_sto:.3f}" if slope_sto is not None else "—"
        det_str = f"{slope_det:.3f}" if slope_det is not None else "—"
        print(f"  {N!s:>4s}  sto: {sto_str:>10s}   det: {det_str:>10s}")


if __name__ == "__main__":
    main()
