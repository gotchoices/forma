"""2D static-field test: gravity emergence from the substrate.

In grid/sim-gravity-2, gravity is computed by solving the graph Laplacian
on the lattice directly (no time evolution): L·v = 0 with v pinned at a
defect. The Green's function on a 2D hex graph decays as log(r), giving a
1/r force law — the 2D analog of Newton. This emergence is a property of
the *lattice substrate*, not of any particular dynamic update rule. It is
the same Laplacian regardless of which model lives on the lattice.

This test has two parts:

  PART A — substrate test (paradigm-neutral). Solve the graph Laplacian
  directly with Dirichlet pins. Verify log(r) potential and 1/r force.
  This is the reference for what "gravity from the lattice" looks like.
  Mirrors grid/sim-gravity-2/run_scalar.py's approach.

  PART B — dynamics-convergence check (model-dependent). Does each
  candidate model's dynamic update, with pins applied every step and a
  small damping factor, *relax* toward the substrate's static solution?
  Models whose static limit is the graph Laplacian (e.g., Normalized) do.
  Models that are unitary wave equations (e.g., Scattering) need not —
  their dynamics propagate but do not relax. This is informative but not
  required for gravity emergence; gravity emerges via Part A.

Plot |v|(r) and fit log + power-law decay. Compare each model's dynamic
result to the analytical Laplacian result.

Run:
    cd projects/grid-duality/scripts
    python test_2d_static_field.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from engine import make_2d_hex_torus
from models import NormalizedTelegrapher, RelativeCosBoth, Scattering


OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)


# ---------- Helpers ----------------------------------------------------------

def torus_distances(lattice, nx, ny, ref_idx):
    """Shortest-image periodic distance from ref_idx to every node."""
    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3) / 2])
    box = np.column_stack([nx * a1, ny * a2])
    box_inv = np.linalg.inv(box)
    ref = lattice.positions[ref_idx]
    dists = np.zeros(lattice.n_nodes)
    for ni in range(lattice.n_nodes):
        disp = lattice.positions[ni] - ref
        frac = box_inv @ disp
        frac -= np.round(frac)
        dists[ni] = np.linalg.norm(box @ frac)
    return dists


def pin_indices_value_pairs(distances, source_idx, source_value, sink_dist_min):
    """Return arrays of (pinned indices, pinned values).
    Source at `source_idx` is pinned to `source_value`. All nodes at
    distance ≥ sink_dist_min are pinned to 0."""
    sink_idxs = np.where(distances >= sink_dist_min)[0]
    sink_idxs = sink_idxs[sink_idxs != source_idx]
    pinned_idxs = np.concatenate([[source_idx], sink_idxs]).astype(int)
    pinned_vals = np.concatenate([[source_value], np.zeros(len(sink_idxs))])
    return pinned_idxs, pinned_vals


def laplacian_solve(lattice, pinned_idxs, pinned_vals):
    """Solve graph Laplacian L·v = 0 with Dirichlet pins."""
    L = lattice.M @ lattice.M.T  # graph Laplacian (degree on diag, −1 off-diag for connected)
    n = lattice.n_nodes
    fixed = np.zeros(n, dtype=bool)
    fixed[pinned_idxs] = True
    free = ~fixed
    L_ff = L[np.ix_(free, free)]
    L_fc = L[np.ix_(free, fixed)]
    v = np.zeros(n)
    v[pinned_idxs] = pinned_vals  # assign by index, not mask order
    rhs = -L_fc @ v[fixed]
    v[free] = np.linalg.solve(L_ff, rhs)
    return v


def pin_state(model, state, lattice, pinned_idxs, pinned_vals):
    """Apply pins to the model's native state."""
    if isinstance(model, Scattering):
        a_fwd = state["a_fwd"].copy()
        a_bwd = state["a_bwd"].copy()
        for idx, val in zip(pinned_idxs, pinned_vals):
            incident_mask = np.abs(lattice.M[idx]) > 0
            a_fwd[incident_mask] = val / 2.0
            a_bwd[incident_mask] = val / 2.0
        return {"a_fwd": a_fwd, "a_bwd": a_bwd}
    new_state = dict(state)
    new_state["v"] = state["v"].copy()
    new_state["v"][pinned_idxs] = pinned_vals
    return new_state


def damp_state(model, state, alpha):
    """Apply a fractional damping (1-alpha) to the 'through' variable, which
    is what removes energy from the wave system. For v-i models that means
    edge currents i; for Scattering it means both forward and backward
    amplitudes (decreasing wave energy uniformly)."""
    if isinstance(model, Scattering):
        return {
            "a_fwd": state["a_fwd"] * (1.0 - alpha),
            "a_bwd": state["a_bwd"] * (1.0 - alpha),
        }
    new_state = dict(state)
    new_state["i"] = state["i"] * (1.0 - alpha)
    return new_state


def run_with_pins(model, lattice, pinned_idxs, pinned_vals, n_steps, damping=0.0):
    state = model.init_state(lattice)
    state = pin_state(model, state, lattice, pinned_idxs, pinned_vals)
    history = [model.node_observable(state).copy()]
    energies = [model.total_energy(state)]
    for _ in range(n_steps):
        state = model.update(state, lattice)
        if damping > 0.0:
            state = damp_state(model, state, damping)
        state = pin_state(model, state, lattice, pinned_idxs, pinned_vals)
        history.append(model.node_observable(state).copy())
        energies.append(model.total_energy(state))
    return np.array(history), np.array(energies)


def fit_log(distances, field, r_min, r_max):
    mask = (distances >= r_min) & (distances <= r_max) & np.isfinite(field) & (field > 0)
    if mask.sum() < 4:
        return None
    r = distances[mask]
    f = field[mask]
    coef = np.polyfit(np.log(r), f, 1)
    B, A = coef
    f_fit = A + B * np.log(r)
    ss_res = np.sum((f - f_fit) ** 2)
    ss_tot = np.sum((f - f.mean()) ** 2)
    r2 = 1.0 - ss_res / max(ss_tot, 1e-30)
    return {"A": A, "B": B, "r2": r2, "n": int(mask.sum())}


def fit_power(distances, field, r_min, r_max):
    mask = (distances >= r_min) & (distances <= r_max) & np.isfinite(field) & (field > 0)
    if mask.sum() < 4:
        return None
    r = distances[mask]
    f = field[mask]
    coef = np.polyfit(np.log(r), np.log(f), 1)
    p, log_C = coef
    f_fit = np.exp(log_C) * r ** p
    ss_res = np.sum((np.log(f) - np.log(f_fit)) ** 2)
    ss_tot = np.sum((np.log(f) - np.log(f).mean()) ** 2)
    r2 = 1.0 - ss_res / max(ss_tot, 1e-30)
    return {"C": np.exp(log_C), "p": p, "r2": r2, "n": int(mask.sum())}


def field_gradient_magnitude(field, lattice):
    """Per-node estimator of |∇v|: RMS of |Δv across each incident edge|.

    For each node, average over incident edges of |v_tail − v_head| (an
    unsigned 'edge field-difference'). This is a discrete proxy for the
    field gradient magnitude at that node — analogous to the magnitude
    of the electric or gravitational force per unit charge.
    """
    edge_diff = np.abs(field[lattice.tails] - field[lattice.heads])
    # |M[n,e]| selects edges incident to node n; coord normalises.
    return (np.abs(lattice.M) @ edge_diff) / np.maximum(lattice.coord, 1.0)


def rescaled_match(field, ref_field, mask):
    """Rescale `field` to best-fit `ref_field` over `mask`, return R²."""
    f = field[mask]
    r = ref_field[mask]
    # Linear regression with intercept: r = a·f + b
    if np.std(f) < 1e-12:
        return None
    coef = np.polyfit(f, r, 1)
    a, b = coef
    r_fit = a * f + b
    ss_res = np.sum((r - r_fit) ** 2)
    ss_tot = np.sum((r - r.mean()) ** 2)
    r2 = 1.0 - ss_res / max(ss_tot, 1e-30)
    return {"a": a, "b": b, "r2": r2, "n": int(mask.sum())}


def plot_field_panel(ax, lattice, field, title, cmap_range=None):
    if cmap_range is None:
        cmap_range = max(np.abs(field).max(), 1e-9)
    sc = ax.scatter(
        lattice.positions[:, 0], lattice.positions[:, 1],
        c=field, cmap="RdBu_r",
        vmin=-cmap_range, vmax=cmap_range, s=14,
        edgecolor="none",
    )
    ax.set_title(title, fontsize=10)
    ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    plt.colorbar(sc, ax=ax, fraction=0.046)


# ---------- Main test --------------------------------------------------------

def main():
    nx, ny = 25, 25
    n_steps = 800
    damping = 0.02   # fractional decay of through-variable per step
    source_value = 0.3
    sink_dist_min = 9.0   # nodes at distance ≥ this are pinned to zero
    fit_r_min = 1.5
    fit_r_max = sink_dist_min - 0.5  # avoid the boundary ring

    lattice = make_2d_hex_torus(nx, ny)
    centre = lattice.positions.mean(axis=0)
    source_idx = int(np.argmin(np.linalg.norm(lattice.positions - centre, axis=1)))
    distances = torus_distances(lattice, nx, ny, source_idx)
    pinned_idxs, pinned_vals = pin_indices_value_pairs(
        distances, source_idx, source_value, sink_dist_min
    )

    print(f"Lattice: 2D hex torus, {nx}×{ny} cells "
          f"({lattice.n_nodes} nodes)")
    print(f"Source pinned at node {source_idx}, value {source_value}")
    print(f"Sink ring: {len(pinned_idxs) - 1} nodes at distance ≥ {sink_dist_min} pinned to 0")
    print(f"Fit window: r ∈ [{fit_r_min:.1f}, {fit_r_max:.1f}]")
    print(f"Steps: {n_steps}; damping={damping}; settled state from last 1/4")
    print()

    # Mask of "interior" nodes — used for per-node match comparison.
    interior_mask = (distances >= fit_r_min) & (distances <= fit_r_max)

    # ── PART A — Substrate test (paradigm-neutral graph Laplacian) ──
    print("=== PART A: substrate test (graph Laplacian solve) ===")
    print("This is the gravity-emergence reference — depends only on the")
    print("lattice graph, not on any dynamic update rule. Mirrors")
    print("grid/sim-gravity-2/run_scalar.py's static solve.")
    print()
    v_ref = laplacian_solve(lattice, pinned_idxs, pinned_vals)
    log_ref = fit_log(distances, np.abs(v_ref), fit_r_min, fit_r_max)
    pwr_ref = fit_power(distances, np.abs(v_ref), fit_r_min, fit_r_max)
    grad_ref = field_gradient_magnitude(v_ref, lattice)
    grad_pwr_ref = fit_power(distances, grad_ref, fit_r_min, fit_r_max)
    if log_ref:
        print(f"  log fit:    |v|(r) = {log_ref['A']:+.4f} {log_ref['B']:+.4f}·log(r), R²={log_ref['r2']:.4f}")
    if pwr_ref:
        print(f"  power fit:  |v|(r) = {pwr_ref['C']:.4f}·r^{pwr_ref['p']:+.4f}, R²={pwr_ref['r2']:.4f}")
    if grad_pwr_ref:
        print(f"  force fit:  |∇v|(r) = {grad_pwr_ref['C']:.4f}·r^{grad_pwr_ref['p']:+.4f}, R²={grad_pwr_ref['r2']:.4f}  (target p ≈ −1)")
    print()

    # ── PART B — Dynamics-convergence check (per-model) ─────────────
    print("=== PART B: dynamics-convergence check ===")
    print("Does each model's update rule, with pins applied every step")
    print("and small damping, relax toward Part A's static solution? This")
    print("is *not* a requirement for gravity emergence — gravity comes")
    print("from Part A on any model's substrate — but it tells us which")
    print("models have the graph Laplacian as their dynamic static limit.")
    print()

    model_results = {"laplacian-ref": (v_ref, log_ref, pwr_ref, grad_pwr_ref, None)}
    for ModelCls in [NormalizedTelegrapher, RelativeCosBoth, Scattering]:
        model = ModelCls()
        print(f"--- Model: {model.name} ---")
        history, energies = run_with_pins(
            model, lattice, pinned_idxs, pinned_vals, n_steps, damping=damping
        )
        # With damping the system settles to a static field; take the
        # time-average over the last quarter (well past transient decay).
        avg_field = history[3 * n_steps // 4:].mean(axis=0)
        print(f"  energy: {energies[0]:.3f} → {energies[-1]:.3f}  (range {energies.min():.3f}–{energies.max():.3f})")
        log_fit = fit_log(distances, np.abs(avg_field), fit_r_min, fit_r_max)
        pwr_fit = fit_power(distances, np.abs(avg_field), fit_r_min, fit_r_max)
        grad = field_gradient_magnitude(avg_field, lattice)
        grad_pwr_fit = fit_power(distances, grad, fit_r_min, fit_r_max)
        match = rescaled_match(avg_field, v_ref, interior_mask)
        if log_fit:
            print(f"  log fit:    |v|(r) = {log_fit['A']:+.4f} {log_fit['B']:+.4f}·log(r), R²={log_fit['r2']:.4f}")
        if pwr_fit:
            print(f"  power fit:  |v|(r) = {pwr_fit['C']:.4f}·r^{pwr_fit['p']:+.4f}, R²={pwr_fit['r2']:.4f}")
        if grad_pwr_fit:
            print(f"  force fit:  |∇v|(r) = {grad_pwr_fit['C']:.4f}·r^{grad_pwr_fit['p']:+.4f}, R²={grad_pwr_fit['r2']:.4f}  (target p ≈ −1)")
        if match:
            print(f"  per-node match to Laplacian: a={match['a']:+.4f}, b={match['b']:+.4f}, R²={match['r2']:.4f}")
        model_results[model.name] = (avg_field, log_fit, pwr_fit, grad_pwr_fit, match)
        print()

    # ── Combined plot ───────────────────────────────────────────────
    n_panels = len(model_results)
    fig = plt.figure(figsize=(5 * n_panels, 5 + 5))

    # Top row: field heatmaps, common scale
    cmap_range = max(np.abs(v_ref).max() * 1.05, 1e-9)
    for i, (name, item) in enumerate(model_results.items()):
        field = item[0]
        ax = plt.subplot(2, n_panels, i + 1)
        # Use per-panel range for non-reference (different magnitudes due to damping).
        panel_range = cmap_range if name == "laplacian-ref" else max(np.abs(field).max() * 1.05, 1e-9)
        plot_field_panel(ax, lattice, field,
                         f"{name}\n(time-avg field)", panel_range)

    # Bottom row: combined |v|(r) plot — *normalised* to compare shapes
    ax = plt.subplot(2, 1, 2)
    colors = ["k", "C0", "C1", "C2"]
    rs = np.linspace(fit_r_min, fit_r_max, 100)
    for (name, item), color in zip(model_results.items(), colors):
        field = item[0]
        log_fit = item[1]
        # Normalise each curve to its own max in the fit window for shape comparison
        in_window = interior_mask & (np.abs(field) > 0)
        if in_window.sum() < 4:
            continue
        norm = np.abs(field[in_window]).max()
        ax.scatter(distances[in_window], np.abs(field[in_window]) / norm,
                   s=8, alpha=0.4, color=color, label=f"{name} data")
        if log_fit:
            curve = (log_fit["A"] + log_fit["B"] * np.log(rs)) / norm
            ax.plot(rs, curve, color=color, linestyle="-", linewidth=1.4,
                    label=f"{name} log: slope/max={log_fit['B'] / norm:+.3f}, R²={log_fit['r2']:.3f}")

    ax.axvspan(fit_r_min, fit_r_max, alpha=0.08, color="grey", label=f"fit window [{fit_r_min:.1f}, {fit_r_max:.1f}]")
    ax.set_xlabel("distance r from source")
    ax.set_ylabel("|v(r)| / max  (normalised)")
    ax.set_title("Static field decay shape: log fit per model (normalised to compare shapes)")
    ax.legend(loc="upper right", fontsize=7)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    out = os.path.join(OUTDIR, "static-field-comparison.png")
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")

    # ── Summary table ───────────────────────────────────────────────
    print("\n=== Summary ===")
    print(f"  {'model':18s}  {'log R²':>8s}  {'force p':>10s}  {'force R²':>10s}  {'match R²':>10s}")
    print(f"  {'-'*18}  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*10}")
    for name, item in model_results.items():
        field, log_fit, pwr_fit, grad_pwr_fit, match = item
        lr2 = f"{log_fit['r2']:.3f}" if log_fit else "—"
        gp = f"{grad_pwr_fit['p']:+.3f}" if grad_pwr_fit else "—"
        gpr2 = f"{grad_pwr_fit['r2']:.3f}" if grad_pwr_fit else "—"
        mr2 = f"{match['r2']:.3f}" if match else "—"
        print(f"  {name:18s}  {lr2:>8s}  {gp:>10s}  {gpr2:>10s}  {mr2:>10s}")


if __name__ == "__main__":
    main()
