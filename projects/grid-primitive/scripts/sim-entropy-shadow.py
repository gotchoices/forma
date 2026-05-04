#!/usr/bin/env python3
"""sim-entropy-shadow — finite-T thermal MC test for theory 7.

Question
--------
At finite temperature, does the cylinder primitive's 2D stress vector
field on a 2D lattice exhibit the variance "shadow" pattern around an
embedded inclusion that produces an entropic 1/r force in 2D — the
same signature that grid/sim-gravity-2 verified for its scalar mode
tower?

Method
------
- Same 2D square lattice as sim-defect-gravity.py, with a circular
  inclusion at the center pinned to ψ = (1, 0).
- Heat-bath Monte Carlo at temperature T, sampling the Gaussian field
  conditioned on the pinned values. Checkerboard sweeps for
  vectorisation.
- After thermalisation, accumulate (ψ_sum, ψ_sq_sum) over many sweeps.
- Compute mean field ⟨ψ(r)⟩ and total variance var(ψ_R) + var(ψ_I) at
  each site.
- Angular-average and check the radial decay of both.

What this test settles
----------------------
For a linear Gaussian theory, var(ψ_i) = T · [G(M)]_ii where G(M) is
the Green's function of the discrete Laplacian operator.  Since the
Laplacian Green's function decays as log(r) (verified statically by
sim-defect-gravity.py), the variance also decays as log(r). This is
the *entropic* signature — fluctuations are reduced near a pinned
inclusion in a logarithmic profile, exactly the pattern that
underwrites the 2D-gravity entropic-force argument (Jacobson):

      S(r) ~ −log(r)   ⇒   F = T · dS/dr ~ 1/r

If the variance falls off logarithmically in our simulation, the
cylinder primitive matches the kinematic + entropic structure that
sim-gravity-2 verified for its mode-tower model. This is necessary
(though not sufficient) for theory 7 in its full form.

What this script does NOT test
------------------------------
- Topological vortex defects (BKT physics). Those require nonlinear
  constraints (|ψ| ≈ const) or thermal energies large enough to break
  the linear-Gaussian regime. Deferred to a future BKT-specific
  script.
- Coefficient matching to ζ = 1/4. The static + linear-Gaussian tests
  check *scaling*; matching the coefficient requires care with units
  and lattice geometry not handled here.

Note on χ̃
----------
The cross-coupling K_eφ enters via tr(M⁻¹), which affects the
*amplitude* of fluctuations and the correlation between components,
but not the spatial decay shape. We use χ̃ = 1/√2 for concreteness.

Usage
-----
    cd projects/grid-primitive/scripts
    python sim-entropy-shadow.py

Output
------
    output/entropy-shadow.png         — visualisations and radial fits
    output/entropy-shadow-result.txt  — fit parameters and verdict
"""

import os
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ── Parameters ─────────────────────────────────────────────

N = 121                    # Lattice size; large enough for a clean log regime
INCLUSION_RADIUS = 4
INCLUSION_VALUE = np.array([1.0, 0.0])
CHI_TILDE = 1.0 / np.sqrt(2)

T = 1.0                    # Temperature (sets fluctuation scale)
N_THERMALISE = 2000        # Sweeps to thermalise
N_MEASURE = 8000           # Sweeps over which to average
SAMPLE_EVERY = 5           # Sample every k sweeps to reduce autocorrelation

# Fit range — sim-gravity-2 style: stop well short of the outer boundary,
# where Dirichlet suppression of fluctuations creates a non-monotonic
# variance profile (an artifact of the finite box, not of the physics).
FIT_R_FRAC = 0.45          # Use r up to 0.45 * (lattice half-width)


# ── Setup ──────────────────────────────────────────────────

def build_inclusion_mask(N, center, radius):
    i_grid, j_grid = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    return (i_grid - center) ** 2 + (j_grid - center) ** 2 <= radius ** 2


def build_pinned_mask_and_values(N, inclusion_mask, inclusion_value):
    pinned_mask = np.zeros((N, N), dtype=bool)
    pinned_mask[0, :] = pinned_mask[-1, :] = True
    pinned_mask[:, 0] = pinned_mask[:, -1] = True
    pinned_mask |= inclusion_mask

    pinned_values = np.zeros((N, N, 2))
    pinned_values[inclusion_mask] = inclusion_value
    return pinned_mask, pinned_values


def neighbor_sum(psi):
    """Sum of 4 nearest-neighbor values at each interior site (vectorised)."""
    s = np.zeros_like(psi)
    s[1:-1, 1:-1] = (
        psi[:-2, 1:-1] + psi[2:, 1:-1]
        + psi[1:-1, :-2] + psi[1:-1, 2:]
    )
    return s


# ── Heat-bath MC ───────────────────────────────────────────

def run_mc(N, M, T, pinned_mask, pinned_values,
           n_thermalise, n_measure, sample_every, rng=None):
    """Heat-bath MC on an N × N lattice of 2-component stress vectors.

    Uses checkerboard sweeps. Each free site is updated by sampling
    from its conditional Gaussian distribution given its 4 neighbors.
    For a quadratic-in-differences energy with stiffness M, that
    distribution is N(μ, Σ) with μ = (1/4) Σ_neighbors and
    Σ = (T / 4) · M⁻¹.

    Returns (mean, var_per_component) — angular-averaged later.
    """
    if rng is None:
        rng = np.random.default_rng(seed=12345)

    # Initialise field with pinned values; free sites start at zero.
    psi = pinned_values.copy()

    # Cholesky factor of the per-update covariance Σ = (T/4) M⁻¹
    M_inv = np.linalg.inv(M)
    Sigma = (T / 4.0) * M_inv
    L_chol = np.linalg.cholesky(Sigma)  # L L^T = Σ

    # Checkerboard masks (only free sites participate)
    i_grid, j_grid = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    free_mask = ~pinned_mask
    black_mask = ((i_grid + j_grid) % 2 == 0) & free_mask
    white_mask = ((i_grid + j_grid) % 2 == 1) & free_mask
    n_black = int(black_mask.sum())
    n_white = int(white_mask.sum())

    def sweep():
        # Black update
        s = neighbor_sum(psi)
        mu = s / 4.0
        z = rng.standard_normal(size=(n_black, 2))
        delta = z @ L_chol.T
        psi[black_mask] = mu[black_mask] + delta

        # White update (using freshly-updated black values)
        s = neighbor_sum(psi)
        mu = s / 4.0
        z = rng.standard_normal(size=(n_white, 2))
        delta = z @ L_chol.T
        psi[white_mask] = mu[white_mask] + delta

    # Thermalise
    print(f"  Thermalising for {n_thermalise} sweeps...")
    t0 = time.time()
    for k in range(n_thermalise):
        sweep()
        if (k + 1) % 500 == 0:
            print(f"    Therm {k + 1}/{n_thermalise}, "
                  f"elapsed {time.time() - t0:.1f}s")

    # Measure
    print(f"  Measuring for {n_measure} sweeps "
          f"(sampling every {sample_every})...")
    psi_sum = np.zeros_like(psi)
    psi_sq_sum = np.zeros_like(psi)
    n_samples = 0
    for k in range(n_measure):
        sweep()
        if (k + 1) % sample_every == 0:
            psi_sum += psi
            psi_sq_sum += psi ** 2
            n_samples += 1
        if (k + 1) % 1000 == 0:
            print(f"    Meas {k + 1}/{n_measure}, "
                  f"samples {n_samples}, elapsed {time.time() - t0:.1f}s")

    mean = psi_sum / n_samples
    var = psi_sq_sum / n_samples - mean ** 2  # per-component variance
    return mean, var, n_samples


# ── Diagnostics ────────────────────────────────────────────

def measure_radial_profile(field, center, inclusion_radius, n_bins=40):
    """Angular-averaged radial profile of a scalar field over the full lattice
    (used for visualisation; fitting uses a restricted range)."""
    N = field.shape[0]
    i_grid, j_grid = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    dist = np.sqrt((i_grid - center) ** 2 + (j_grid - center) ** 2)

    r_min = inclusion_radius + 1.5
    r_max = N // 2 - 3
    edges = np.linspace(r_min, r_max, n_bins + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])

    avg = np.zeros(n_bins)
    counts = np.zeros(n_bins, dtype=int)
    for k in range(n_bins):
        m = (dist >= edges[k]) & (dist < edges[k + 1])
        if m.any():
            avg[k] = field[m].mean()
            counts[k] = int(m.sum())
    valid = counts > 0
    return centers[valid], avg[valid]


def fit_window(rs, ys, r_min, r_max):
    """Restrict (rs, ys) to r ∈ [r_min, r_max] for fitting."""
    mask = (rs >= r_min) & (rs <= r_max)
    return rs[mask], ys[mask]


def fit_log_and_power(rs, ys):
    """Fit y = A + B log r and y = C r^p; returns dict with both."""
    log_rs = np.log(rs)
    log_ys = np.log(np.abs(ys))

    B, A = np.polyfit(log_rs, ys, 1)
    res_log = ys - (A + B * log_rs)
    ss_tot = ((ys - ys.mean()) ** 2).sum()
    R2_log = 1 - (res_log ** 2).sum() / ss_tot

    p, log_C = np.polyfit(log_rs, log_ys, 1)
    res_pow = log_ys - (log_C + p * log_rs)
    ss_tot_pow = ((log_ys - log_ys.mean()) ** 2).sum()
    R2_pow = 1 - (res_pow ** 2).sum() / ss_tot_pow

    return {
        "log": {"A": A, "B": B, "R2": R2_log},
        "power": {"C": np.exp(log_C), "p": p, "R2": R2_pow},
    }


def verdict_for(name, fits):
    """Return a one-line verdict for a single radial profile.

    For a finite range, log and power fits can both look reasonable
    because log(r) is approximately r^p for some p over a limited range.
    Use absolute R²_log as the primary criterion and require log to
    not be worse than power.
    """
    R2_log = fits["log"]["R2"]
    R2_pow = fits["power"]["R2"]
    p = fits["power"]["p"]
    # Strong power-law signature (e.g., elastic 1/r²) should be flagged
    if R2_pow > R2_log + 0.05 and abs(p + 2.0) < 0.2:
        return f"{name}: 1/r² decay (elastic, NOT log) (R²_pow = {R2_pow:.4f})"
    if R2_pow > R2_log + 0.05:
        return f"{name}: power-law r^{p:.3f} (R²_pow = {R2_pow:.4f})"
    if R2_log > 0.9:
        return f"{name}: logarithmic decay (R²_log = {R2_log:.4f})"
    return (f"{name}: ambiguous "
            f"(R²_log = {R2_log:.4f}, R²_pow = {R2_pow:.4f})")


# ── Main ───────────────────────────────────────────────────

def main():
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)

    print("=" * 64)
    print("  sim-entropy-shadow — finite-T fail-fast test for theory 7")
    print("=" * 64)
    print(f"  Lattice:           {N} × {N}")
    print(f"  Inclusion radius:  {INCLUSION_RADIUS}")
    print(f"  Inclusion value:   ψ = {INCLUSION_VALUE}")
    print(f"  χ̃:                {CHI_TILDE:.4f}")
    print(f"  Temperature T:     {T}")
    print(f"  Thermalise sweeps: {N_THERMALISE}")
    print(f"  Measure sweeps:    {N_MEASURE} (sample every {SAMPLE_EVERY})")
    print()

    # Stiffness matrix
    K_ee = 1.0
    K_pp = 1.0
    K_ep = CHI_TILDE * np.sqrt(K_ee * K_pp)
    M = np.array([[K_ee, K_ep], [K_ep, K_pp]])

    # Setup
    center = N // 2
    inclusion_mask = build_inclusion_mask(N, center, INCLUSION_RADIUS)
    pinned_mask, pinned_values = build_pinned_mask_and_values(
        N, inclusion_mask, INCLUSION_VALUE
    )

    # MC
    mean, var, n_samples = run_mc(
        N=N, M=M, T=T,
        pinned_mask=pinned_mask, pinned_values=pinned_values,
        n_thermalise=N_THERMALISE, n_measure=N_MEASURE,
        sample_every=SAMPLE_EVERY,
    )
    print(f"  MC complete: {n_samples} samples accumulated")
    print()

    # Compute scalar fields for analysis
    mean_mag = np.sqrt(mean[..., 0] ** 2 + mean[..., 1] ** 2)
    var_total = var[..., 0] + var[..., 1]  # tr of per-site covariance

    # Bulk variance reference (corner of lattice, far from inclusion and boundary)
    bulk_radius = N // 2 - 8
    bulk_mask = (
        ((np.arange(N)[:, None] - center) ** 2
         + (np.arange(N)[None, :] - center) ** 2)
        > bulk_radius ** 2
    )
    bulk_mask &= ~pinned_mask
    if bulk_mask.any():
        bulk_var = var_total[bulk_mask].mean()
        print(f"  Bulk variance (far from inclusion): {bulk_var:.4f}")

    # Radial profiles (full range, for visualisation)
    rs_mean, mean_profile = measure_radial_profile(
        mean_mag, center, INCLUSION_RADIUS
    )
    rs_var, var_profile = measure_radial_profile(
        var_total, center, INCLUSION_RADIUS
    )

    # Fit window: avoid the outer boundary where Dirichlet suppresses
    # fluctuations and creates a non-monotonic profile artifact.
    half_box = N / 2.0
    fit_r_min = INCLUSION_RADIUS + 2.0
    fit_r_max = FIT_R_FRAC * half_box
    print(f"  Fit window: r ∈ [{fit_r_min:.1f}, {fit_r_max:.1f}]")
    print()

    rs_mean_fit, mean_profile_fit = fit_window(
        rs_mean, mean_profile, fit_r_min, fit_r_max
    )
    rs_var_fit, var_profile_fit = fit_window(
        rs_var, var_profile, fit_r_min, fit_r_max
    )

    # Fit
    mean_fits = fit_log_and_power(rs_mean_fit, mean_profile_fit)
    var_fits = fit_log_and_power(rs_var_fit, var_profile_fit)

    print()
    print("Mean field ⟨|ψ(r)|⟩")
    print("-" * 64)
    print(f"  Log:   A = {mean_fits['log']['A']:.4f}, "
          f"B = {mean_fits['log']['B']:.4f}, "
          f"R² = {mean_fits['log']['R2']:.5f}")
    print(f"  Power: C = {mean_fits['power']['C']:.4f}, "
          f"p = {mean_fits['power']['p']:.4f}, "
          f"R² = {mean_fits['power']['R2']:.5f}")
    print()
    print("Variance var(ψ_R) + var(ψ_I)  [the entropy shadow]")
    print("-" * 64)
    print(f"  Log:   A = {var_fits['log']['A']:.4f}, "
          f"B = {var_fits['log']['B']:.4f}, "
          f"R² = {var_fits['log']['R2']:.5f}")
    print(f"  Power: C = {var_fits['power']['C']:.4f}, "
          f"p = {var_fits['power']['p']:.4f}, "
          f"R² = {var_fits['power']['R2']:.5f}")
    print()

    # Verdict
    mean_verdict = verdict_for("Mean field", mean_fits)
    var_verdict = verdict_for("Variance shadow", var_fits)
    print("Verdict")
    print("-" * 64)
    print(f"  {mean_verdict}")
    print(f"  {var_verdict}")

    def is_log(fits):
        R2_log = fits["log"]["R2"]
        R2_pow = fits["power"]["R2"]
        return R2_log > 0.9 and not (R2_pow > R2_log + 0.05)

    if is_log(mean_fits) and is_log(var_fits):
        overall = ("PASS — both mean field and variance show logarithmic "
                   "decay (entropic 1/r force scaling, 2D)")
        explanation = (
            "The cylinder primitive at finite temperature exhibits the "
            "same entropy-shadow pattern that grid/sim-gravity-2 found "
            "for its mode-tower model. Theory 7 passes the linear "
            "thermal test. A BKT / topological-defect follow-up will "
            "test the coefficient match against ζ; for now, the "
            "scaling is correct."
        )
    else:
        overall = "REVIEW — at least one fit is not cleanly logarithmic"
        explanation = (
            "Inspect the fits and the field maps. Possible causes: "
            "insufficient sampling, finite-size artifacts, or genuine "
            "deviation from the linear Gaussian theory."
        )
    print()
    print(f"  → {overall}")
    print(f"  {explanation}")
    print()

    # Plots
    fig, axes = plt.subplots(2, 2, figsize=(13, 11))

    # Mean field map
    im0 = axes[0, 0].imshow(mean_mag, origin="lower", cmap="viridis")
    axes[0, 0].set_title("⟨|ψ(x, y)|⟩  (mean field)")
    axes[0, 0].set_xlabel("x")
    axes[0, 0].set_ylabel("y")
    plt.colorbar(im0, ax=axes[0, 0], shrink=0.85)

    # Variance map
    im1 = axes[0, 1].imshow(var_total, origin="lower", cmap="magma")
    axes[0, 1].set_title("var(ψ_R) + var(ψ_I)  (entropy shadow)")
    axes[0, 1].set_xlabel("x")
    axes[0, 1].set_ylabel("y")
    plt.colorbar(im1, ax=axes[0, 1], shrink=0.85)

    # Mean field decay (full data shown, fit only over the window)
    r_curve = np.linspace(rs_mean_fit[0], rs_mean_fit[-1], 200)
    axes[1, 0].plot(rs_mean, mean_profile, "o", label="MC (full)",
                    alpha=0.4, color="C0")
    axes[1, 0].plot(rs_mean_fit, mean_profile_fit, "o",
                    label="MC (fit window)", color="C0")
    axes[1, 0].plot(
        r_curve,
        mean_fits["log"]["A"] + mean_fits["log"]["B"] * np.log(r_curve),
        "--", color="C3",
        label=f"Log: B = {mean_fits['log']['B']:.3f}, "
              f"R² = {mean_fits['log']['R2']:.4f}",
    )
    axes[1, 0].axvspan(fit_r_min, fit_r_max, alpha=0.07, color="green")
    axes[1, 0].set_xscale("log")
    axes[1, 0].set_xlabel("r (log scale)")
    axes[1, 0].set_ylabel("⟨|ψ(r)|⟩")
    axes[1, 0].set_title("Mean field radial decay")
    axes[1, 0].legend(fontsize=9)
    axes[1, 0].grid(True, which="both", alpha=0.3)

    # Variance decay (full data shown, fit only over the window)
    r_curve_v = np.linspace(rs_var_fit[0], rs_var_fit[-1], 200)
    axes[1, 1].plot(rs_var, var_profile, "o", label="MC (full)",
                    alpha=0.4, color="C1")
    axes[1, 1].plot(rs_var_fit, var_profile_fit, "o",
                    label="MC (fit window)", color="C1")
    axes[1, 1].plot(
        r_curve_v,
        var_fits["log"]["A"] + var_fits["log"]["B"] * np.log(r_curve_v),
        "--", color="C3",
        label=f"Log: B = {var_fits['log']['B']:.3f}, "
              f"R² = {var_fits['log']['R2']:.4f}",
    )
    axes[1, 1].axvspan(fit_r_min, fit_r_max, alpha=0.07, color="green")
    axes[1, 1].set_xscale("log")
    axes[1, 1].set_xlabel("r (log scale)")
    axes[1, 1].set_ylabel("var(ψ_R) + var(ψ_I)")
    axes[1, 1].set_title("Variance shadow radial profile")
    axes[1, 1].legend(fontsize=9)
    axes[1, 1].grid(True, which="both", alpha=0.3)

    fig.suptitle(
        f"Cylinder primitive on 2D lattice, T = {T}, χ̃ = {CHI_TILDE:.3f}\n"
        f"{overall}",
        fontsize=11,
    )
    plt.tight_layout()
    out_path = os.path.join(output_dir, "entropy-shadow.png")
    plt.savefig(out_path, dpi=120)
    print(f"Saved {out_path}")

    # Text result
    txt_path = os.path.join(output_dir, "entropy-shadow-result.txt")
    with open(txt_path, "w") as f:
        f.write("sim-entropy-shadow — finite-T fail-fast test for theory 7\n")
        f.write("=" * 64 + "\n\n")
        f.write(f"Lattice:           {N} x {N}\n")
        f.write(f"Inclusion radius:  {INCLUSION_RADIUS}\n")
        f.write(f"Inclusion value:   psi = {INCLUSION_VALUE}\n")
        f.write(f"chi-tilde:         {CHI_TILDE:.4f}\n")
        f.write(f"Temperature T:     {T}\n")
        f.write(f"Thermalise sweeps: {N_THERMALISE}\n")
        f.write(f"Measure sweeps:    {N_MEASURE} "
                f"(sample every {SAMPLE_EVERY})\n")
        f.write(f"MC samples:        {n_samples}\n\n")
        f.write("Mean field <|psi(r)|>\n")
        f.write("-" * 64 + "\n")
        f.write(
            f"  Log:   |psi| = A + B log(r), "
            f"A = {mean_fits['log']['A']:.6f}, "
            f"B = {mean_fits['log']['B']:.6f}, "
            f"R^2 = {mean_fits['log']['R2']:.6f}\n"
        )
        f.write(
            f"  Power: |psi| = C * r^p, "
            f"C = {mean_fits['power']['C']:.6f}, "
            f"p = {mean_fits['power']['p']:.6f}, "
            f"R^2 = {mean_fits['power']['R2']:.6f}\n\n"
        )
        f.write("Variance var(psi_R) + var(psi_I)  [entropy shadow]\n")
        f.write("-" * 64 + "\n")
        f.write(
            f"  Log:   var = A + B log(r), "
            f"A = {var_fits['log']['A']:.6f}, "
            f"B = {var_fits['log']['B']:.6f}, "
            f"R^2 = {var_fits['log']['R2']:.6f}\n"
        )
        f.write(
            f"  Power: var = C * r^p, "
            f"C = {var_fits['power']['C']:.6f}, "
            f"p = {var_fits['power']['p']:.6f}, "
            f"R^2 = {var_fits['power']['R2']:.6f}\n\n"
        )
        f.write("Verdict\n")
        f.write("-" * 64 + "\n")
        f.write(f"  {mean_verdict}\n")
        f.write(f"  {var_verdict}\n\n")
        f.write(f"  -> {overall}\n")
        f.write(f"  {explanation}\n")
    print(f"Saved {txt_path}")
    print()
    print("Done.")


if __name__ == "__main__":
    main()
