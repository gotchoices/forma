#!/usr/bin/env python3
"""sim-defect-gravity — first fail-fast test for theory 7.

Question
--------
Does the cylinder primitive's 2D stress vector field on a 2D lattice
produce a 1/r force law (2D gravity), or does it produce 1/r²
(the elastic spring-lattice failure mode of grid/sim-gravity/)?

Method (static, T = 0)
----------------------
- N × N square lattice. Each site carries a 2-component stress vector
  ψ = (ψ_R, ψ_I) in the cross-sectional plane (chapter 1's (e, φ) in
  Cartesian form).
- Nearest-neighbor harmonic coupling. Bond energy:
      E_bond = (1/2) (ψ_j − ψ_i)ᵀ M (ψ_j − ψ_i)
  with the 2×2 stiffness matrix M from chapter 1:
      M = [[K_ee, K_eφ], [K_eφ, K_φφ]]
- Pin a small circular inclusion at the lattice center to ψ = (1, 0).
- Pin the lattice boundary to ψ = (0, 0).
- Solve for the equilibrium configuration on the unpinned interior.
- Measure the angular-averaged |ψ(r)| as a function of distance r from
  the inclusion. Fit both a logarithmic decay (|ψ| ≈ A + B log r) and a
  power-law decay (|ψ| ≈ C r^p). Report which fits better.

Why static is informative
-------------------------
The minimum-energy configuration of a quadratic energy with positive-
definite stiffness M satisfies, at every interior site,
      ψ_i = (1/n_i) Σ_j ψ_j
which is the discrete Laplace equation, applied independently to each
component of ψ (the matrix M factors out because it is invertible).
The 2D Laplacian Green's function decays as log(r) from a localized
source, so the prediction is:

    |ψ(r)| ∝ log(L / r)        (logarithmic decay)
    |∇ψ(r)| ∝ 1 / r            (1/r force law — 2D gravity scaling)

For comparison, grid/sim-gravity/ on a 2D triangular spring lattice
measured edge strain ε ∝ 1/r² — the elastic Navier-equation result for
vector displacement fields. That is the *failure* mode for entropic
gravity; we want to confirm we are *not* in that regime.

What this test settles
----------------------
- Logarithmic decay → cylinder primitive is in the right kinematic
  regime for 2D gravity. Theory 7 passes the static check; thermal-MC
  follow-up is needed to confirm the entropic mechanism in full.
- Power-law decay r^p with p ≠ 0 → falsification at the kinematic
  level. Theory 7 fails; project triggers ground-rule-8 fallback.

Note on χ̃
----------
Mathematically, M factors out of the static equation, so the result is
*independent* of the off-diagonal coupling K_eφ. We use χ̃ = 1/√2
(equipartition value from chapter 2) for concreteness, but a sweep over
χ̃ would give identical static fields. The chirality matters for
dynamics and finite-T entropy, not for the static Green's function —
which is itself a finding worth marking explicitly.

Usage
-----
    cd projects/grid-primitive/scripts
    python sim-defect-gravity.py

Output
------
    output/field-and-decay.png   — field visualization and radial decay
    output/result.txt            — fit parameters and verdict
"""

import os
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ── Parameters ─────────────────────────────────────────────

N = 121                    # Lattice size (odd, gives a clean center site)
INCLUSION_RADIUS = 4       # Radius of the pinned circular inclusion
INCLUSION_VALUE = np.array([1.0, 0.0])  # Pinned ψ in the inclusion
CHI_TILDE = 1.0 / np.sqrt(2)  # Equipartition (chapter 2 §7); does not affect static


# ── Solver ─────────────────────────────────────────────────

def solve_static(N, inclusion_mask, inclusion_value):
    """Solve the discrete Laplace equation on an N×N lattice with the
    given inclusion mask pinned to inclusion_value and boundary pinned
    to zero. Returns ψ of shape (N, N, 2).

    The two components decouple at static (M factors out of the
    minimization equation), so we solve component-by-component with the
    same sparse Laplacian matrix.
    """
    # Identify pinned vs free sites
    pinned_mask = np.zeros((N, N), dtype=bool)
    pinned_mask[0, :] = pinned_mask[-1, :] = True
    pinned_mask[:, 0] = pinned_mask[:, -1] = True
    pinned_mask |= inclusion_mask

    pinned_values = np.zeros((N, N, 2))
    pinned_values[inclusion_mask] = inclusion_value
    # Boundary is left at zero, which is what zeros() initializes to.

    free_indices = np.argwhere(~pinned_mask)
    n_free = len(free_indices)

    # Build map (i, j) → free-site index
    free_idx = -np.ones((N, N), dtype=int)
    for k, (i, j) in enumerate(free_indices):
        free_idx[i, j] = k

    # Assemble the discrete Laplacian for free sites:
    #   For free site k at (i, j): 4 ψ_k − Σ_neighbors ψ_neighbor = source from pinned neighbors.
    rows, cols, data = [], [], []
    for k, (i, j) in enumerate(free_indices):
        rows.append(k)
        cols.append(k)
        data.append(4.0)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not pinned_mask[ni, nj]:
                rows.append(k)
                cols.append(free_idx[ni, nj])
                data.append(-1.0)

    A = csr_matrix((data, (rows, cols)), shape=(n_free, n_free))

    # Solve per component
    psi = pinned_values.copy()
    for component in range(2):
        b = np.zeros(n_free)
        for k, (i, j) in enumerate(free_indices):
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and pinned_mask[ni, nj]:
                    b[k] += pinned_values[ni, nj, component]
        x = spsolve(A, b)
        for k, (i, j) in enumerate(free_indices):
            psi[i, j, component] = x[k]

    return psi


# ── Diagnostics ────────────────────────────────────────────

def measure_radial_decay(psi, center, inclusion_radius, n_bins=40):
    """Angular-averaged |ψ(r)| versus r."""
    N = psi.shape[0]
    i_grid, j_grid = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    dist = np.sqrt((i_grid - center) ** 2 + (j_grid - center) ** 2)
    mag = np.sqrt(psi[..., 0] ** 2 + psi[..., 1] ** 2)

    r_min = inclusion_radius + 1.5
    r_max = N // 2 - 5
    edges = np.linspace(r_min, r_max, n_bins + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])

    avg = np.zeros(n_bins)
    counts = np.zeros(n_bins, dtype=int)
    for k in range(n_bins):
        m = (dist >= edges[k]) & (dist < edges[k + 1])
        if m.any():
            avg[k] = mag[m].mean()
            counts[k] = m.sum()

    valid = counts > 0
    return centers[valid], avg[valid]


def fit_log_and_power(rs, mags):
    """Fit |ψ| = A + B log r and |ψ| = C r^p; return both with R²."""
    log_rs = np.log(rs)
    log_mags = np.log(np.abs(mags))

    # Logarithmic fit
    B, A = np.polyfit(log_rs, mags, 1)
    res_log = mags - (A + B * log_rs)
    ss_tot = ((mags - mags.mean()) ** 2).sum()
    R2_log = 1 - (res_log ** 2).sum() / ss_tot

    # Power-law fit
    p, log_C = np.polyfit(log_rs, log_mags, 1)
    res_pow = log_mags - (log_C + p * log_rs)
    ss_tot_pow = ((log_mags - log_mags.mean()) ** 2).sum()
    R2_pow = 1 - (res_pow ** 2).sum() / ss_tot_pow

    return {
        "log": {"A": A, "B": B, "R2": R2_log},
        "power": {"C": np.exp(log_C), "p": p, "R2": R2_pow},
    }


def verdict(fits):
    """Compare log vs power fits and return a one-line verdict.

    Logic: a logarithmic curve forced into a power-law fit on a finite
    range will produce some p (typically between −1 and −2) with a
    moderate R². The dispositive comparison is the difference in R²:
    if the log fit is significantly better, the decay is logarithmic.
    """
    R2_log = fits["log"]["R2"]
    R2_pow = fits["power"]["R2"]
    p = fits["power"]["p"]
    margin = 0.02

    if R2_log > 0.99 and R2_log > R2_pow + margin:
        return ("PASS — logarithmic decay (gravity-compatible kinematics, 2D)",
                "The stress vector field has the Laplace Green's function "
                "structure needed for a 1/r force law in 2D. Theory 7 passes "
                "the static check.")
    if R2_pow > 0.99 and R2_pow > R2_log + margin and abs(p + 2.0) < 0.2:
        return ("FAIL — 1/r² decay (elastic spring-lattice regime)",
                "Same failure mode as grid/sim-gravity. Theory 7 falsified at "
                "the kinematic level. Trigger ground-rule-8 fallback.")
    if R2_pow > R2_log + margin:
        return (f"FAIL — power-law decay r^{p:.3f} (not logarithmic)",
                "The decay does not match the 2D Laplacian Green's function. "
                "Theory 7 falsified at the kinematic level.")
    return (f"AMBIGUOUS — both fits comparable (R²_log = {R2_log:.4f}, "
            f"R²_pow = {R2_pow:.4f})",
            "Re-examine the lattice setup; possible boundary or finite-size "
            "artifact. Increase N and re-run before drawing conclusions.")


# ── Main ───────────────────────────────────────────────────

def main():
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)

    print("=" * 64)
    print("  sim-defect-gravity — static fail-fast test for theory 7")
    print("=" * 64)
    print(f"  Lattice:           {N} × {N}")
    print(f"  Inclusion radius:  {INCLUSION_RADIUS}")
    print(f"  Inclusion value:   ψ = {INCLUSION_VALUE}")
    print(f"  χ̃:                {CHI_TILDE:.4f} (does not affect static)")
    print()

    # Build inclusion mask
    center = N // 2
    i_grid, j_grid = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    inclusion_mask = (
        (i_grid - center) ** 2 + (j_grid - center) ** 2
        <= INCLUSION_RADIUS ** 2
    )

    # Solve
    print("Solving Laplace equation on the lattice...")
    psi = solve_static(N, inclusion_mask, INCLUSION_VALUE)
    print("Done.")
    print()

    # Measure
    rs, mags = measure_radial_decay(psi, center, INCLUSION_RADIUS)

    # Fit
    fits = fit_log_and_power(rs, mags)
    one_line, explanation = verdict(fits)

    print("Fit results")
    print("-" * 64)
    print(f"  Logarithmic   |ψ(r)| ≈ {fits['log']['A']:.4f} "
          f"+ {fits['log']['B']:.4f} · log(r)   R² = {fits['log']['R2']:.5f}")
    print(f"  Power-law     |ψ(r)| ≈ {fits['power']['C']:.4f} "
          f"· r^{fits['power']['p']:.4f}   R² = {fits['power']['R2']:.5f}")
    print()
    print("Verdict")
    print("-" * 64)
    print(f"  {one_line}")
    print(f"  {explanation}")
    print()

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Field magnitude
    psi_mag = np.sqrt(psi[..., 0] ** 2 + psi[..., 1] ** 2)
    im = axes[0].imshow(psi_mag, origin="lower", cmap="viridis")
    axes[0].set_title("|ψ(x, y)| around inclusion")
    axes[0].set_xlabel("x (lattice units)")
    axes[0].set_ylabel("y (lattice units)")
    plt.colorbar(im, ax=axes[0], shrink=0.85)

    # Decay vs distance with both fits
    r_fit = np.linspace(rs[0], rs[-1], 200)
    axes[1].plot(rs, mags, "o", label="Simulation", alpha=0.7, color="C0")
    axes[1].plot(
        r_fit,
        fits["log"]["A"] + fits["log"]["B"] * np.log(r_fit),
        "--",
        color="C3",
        label=f"Log:   A + B log(r), B = {fits['log']['B']:.3f}, "
              f"R² = {fits['log']['R2']:.4f}",
    )
    axes[1].plot(
        r_fit,
        fits["power"]["C"] * r_fit ** fits["power"]["p"],
        ":",
        color="C2",
        label=f"Power: C · r^p, p = {fits['power']['p']:.3f}, "
              f"R² = {fits['power']['R2']:.4f}",
    )
    axes[1].set_xscale("log")
    axes[1].set_xlabel("r (lattice units, log scale)")
    axes[1].set_ylabel("|ψ(r)|  (angular-averaged)")
    axes[1].set_title("Radial decay of |ψ|")
    axes[1].legend(fontsize=9, loc="upper right")
    axes[1].grid(True, which="both", alpha=0.3)

    fig.suptitle(
        f"Cylinder primitive on a 2D lattice — static response to a pinned inclusion\n"
        f"{one_line}",
        fontsize=11,
    )
    plt.tight_layout()
    out_path = os.path.join(output_dir, "field-and-decay.png")
    plt.savefig(out_path, dpi=120)
    print(f"Saved {out_path}")

    # Save text result
    txt_path = os.path.join(output_dir, "result.txt")
    with open(txt_path, "w") as f:
        f.write("sim-defect-gravity — static fail-fast test for theory 7\n")
        f.write("=" * 64 + "\n\n")
        f.write(f"Lattice:           {N} x {N}\n")
        f.write(f"Inclusion radius:  {INCLUSION_RADIUS}\n")
        f.write(f"Inclusion value:   psi = {INCLUSION_VALUE}\n")
        f.write(f"chi-tilde:         {CHI_TILDE:.4f} (does not affect static)\n\n")
        f.write("Fit results\n")
        f.write("-" * 64 + "\n")
        f.write(
            f"Log:   |psi| = A + B log(r)\n"
            f"       A = {fits['log']['A']:.6f}, "
            f"B = {fits['log']['B']:.6f}, "
            f"R^2 = {fits['log']['R2']:.6f}\n\n"
        )
        f.write(
            f"Power: |psi| = C * r^p\n"
            f"       C = {fits['power']['C']:.6f}, "
            f"p = {fits['power']['p']:.6f}, "
            f"R^2 = {fits['power']['R2']:.6f}\n\n"
        )
        f.write("Verdict\n")
        f.write("-" * 64 + "\n")
        f.write(f"{one_line}\n")
        f.write(f"{explanation}\n")
    print(f"Saved {txt_path}")
    print()
    print("Done.")


if __name__ == "__main__":
    main()
