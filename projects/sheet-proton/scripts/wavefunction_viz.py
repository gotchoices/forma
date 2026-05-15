"""
Wavefunction visualization and localization classification on the corrugated
clover cross-section.

Computes Hill-equation eigenfunctions via `laplacian_spectrum.hill_eigenvalues`
(with `return_eigvecs=True`), evaluates ψ(u) on a u-grid, and computes:

  1. Spatial probability density |ψ(u)|² weighted by the metric √|g(u)|.
  2. Lobe vs saddle overlap fractions
       L = ∫_lobe |ψ|² √|g| du / total
       S = ∫_saddle |ψ|² √|g| du / total
     (the lobe region is the union of three 240° lobe arcs at u-coordinates
     [k·2π/3, k·2π/3 + φ_L) for k = 0, 1, 2; saddle region is the complement.)
  3. Localization classification:
       whole-circumference  if max bin probability < 1/3 + tol
       lobe-localized       if L > L_thresh
       saddle-localized     if S > S_thresh
  4. Antinode-position fingerprint: a separate diagnostic for Mechanism D.
     For an eigenstate at cross-section quantum number m (its dominant
     Fourier-mode |p|), the antinode pattern should either align with lobe
     centers (u = 0, 2π/3, 4π/3 modulo Z₃ shifts) or saddle centers
     (u = π/3, π, 5π/3).

Per work/3-gen.md §9.2 and §9.3 — this script implements the Mechanism-D
discriminator and the localization-pattern classification.

Scope note: this tool operates on the 1D Hill equation from the 2D-surface
picture (see work/clover-modes-analytical.md for why that picture rules out
the hoped-for lobe/saddle mass hierarchy structurally). The natural follow-on
for the 3D wave-guide picture (work/tube-waveguide.md) is a separate 2D
Helmholtz solver for the clover-shaped cross-section domain, not yet
implemented. The localization-classifier ideas here may transfer to that
solver's eigenfunctions in 2D.

Usage (single mode):
    python scripts/wavefunction_viz.py --epsilon E --chi C --k-v KV --mode M

Usage (Mechanism-D doublet test across m = 1, 2, 3):
    python scripts/wavefunction_viz.py --doublet-test --epsilon E --chi C

Outputs:
    outputs/wavefn_loc_eps<E>_chi<C>_kv<KV>_mode<M>.png
    outputs/doublet_test_eps<E>_chi<C>.csv
    outputs/doublet_test_eps<E>_chi<C>.png
"""

from __future__ import annotations

import argparse
import sys
from math import pi
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from laplacian_spectrum import hill_eigenvalues
from lib.geometry import ProfileParams, profile


def evaluate_psi(p_values: np.ndarray, fourier_coefs: np.ndarray,
                 u_grid: np.ndarray) -> np.ndarray:
    """ψ(u) = Σ_p c_p e^{ipu}. Returns complex amplitudes on u_grid."""
    # Outer product: e^{ip_k u_j} as a matrix, then dot with coefs.
    phase = np.exp(1j * np.outer(u_grid, p_values))  # (N_u, N_p)
    return phase @ fourier_coefs  # (N_u,)


def lobe_mask_and_metric(eps: float, chi: float, u_grid: np.ndarray):
    """Return (lobe_mask, sqrt_g) at each u in u_grid.

    A "lobe region" is the union of the three lobe arcs.  Per
    [lib/geometry.py:_profile_point], within a fundamental domain
    φ ∈ [0, 2π/3), the lobe arc occupies arc-length s ∈ [0, arc_lobe), i.e.
    φ ∈ [0, φ_L) where φ_L = (2π/3) · (2 r_lobe) / (2 r_lobe + r_saddle).
    Saddles fill the complement in each fundamental domain.

    √|g| on the u-axis at P_x = 0 baseline is just ε (the constant arc-length
    speed); the metric correction is √(1 + P_x)² ≈ 1 + P_x, so √|g(u)| = ε ·
    (1 + P_x(u)) in R = 1 units. We compute P_x directly from `profile`.
    """
    r_lobe = eps / (2.0 + chi)
    r_saddle = chi * r_lobe
    params = ProfileParams(r_lobe=r_lobe, r_saddle=r_saddle)
    P_x_u, _ = profile(u_grid % (2.0 * pi), params)
    fund_period = 2.0 * pi / 3.0
    # Lobe fraction within a fundamental domain:
    phi_L = fund_period * (2.0 * r_lobe) / (2.0 * r_lobe + r_saddle)
    fund_phi = u_grid % fund_period
    lobe_mask = fund_phi < phi_L
    sqrt_g = eps * (1.0 + P_x_u)  # R = 1 units; √|g| = ε(R + P_x) = ε(1+P_x)
    return lobe_mask, sqrt_g, P_x_u


def localization_fractions(psi_abs2: np.ndarray, sqrt_g: np.ndarray,
                            lobe_mask: np.ndarray) -> tuple:
    """Compute (L, S) = (lobe overlap, saddle overlap) of the probability density.

    Integrates |ψ|² √|g| du over lobe-region and saddle-region; returns
    fractions of total. L + S = 1.
    """
    integrand = psi_abs2 * sqrt_g
    total = np.trapezoid(integrand)
    if total <= 0:
        return float("nan"), float("nan")
    L = np.trapezoid(np.where(lobe_mask, integrand, 0.0)) / total
    S = 1.0 - L
    return float(L), float(S)


def lobe_baseline_fraction(eps: float, chi: float) -> float:
    """Geometric baseline L for a uniform-amplitude wave.

    The lobe region occupies fraction L_baseline = 2 r_lobe / (2 r_lobe + r_saddle)
    = 2 / (2 + χ) of the cross-section arc length. Any L significantly
    above (below) this baseline indicates lobe (saddle) localization.
    """
    return 2.0 / (2.0 + chi)


def classify(L: float, baseline: float) -> str:
    """Classify by excess lobe overlap Δ = L − baseline.

      Δ > +0.15 → strongly lobe-localized
      Δ > +0.05 → mildly lobe-focused
      Δ < −0.15 → strongly saddle-localized
      Δ < −0.05 → mildly saddle-focused
      |Δ| ≤ 0.05 → whole-circumference (≈ uniform baseline)
    """
    delta = L - baseline
    if delta > 0.15:
        return "lobe-localized"
    if delta > 0.05:
        return "mildly lobe-focused"
    if delta < -0.15:
        return "saddle-localized"
    if delta < -0.05:
        return "mildly saddle-focused"
    return "whole-circumference"


def antinode_alignment(u_grid: np.ndarray, psi_abs2: np.ndarray) -> float:
    """Return the signed Z₃ Fourier moment alignment of |ψ|².

    Specifically: compute the q = ±3 Fourier mode of |ψ|², which is the
    Z₃-symmetric component. Phase tells us whether the antinodes align with
    lobe centers (u = 0, 2π/3, 4π/3 — phase = 0) or saddle centers
    (u = π/3, π, 5π/3 — phase = π).

    Returns a real value in [-1, 1]:
       +1 → fully lobe-aligned antinodes
       −1 → fully saddle-aligned antinodes
        0 → no Z₃-symmetric component (whole-circumference)
    """
    # |ψ|² should be 2π-periodic. Compute c_3 = (1/2π) ∫ |ψ|² e^{-3iu} du
    N = len(u_grid)
    integrand = psi_abs2 * np.exp(-3j * u_grid)
    c_3 = np.trapezoid(integrand) / N * len(u_grid)  # actually 2π avg
    # Better: explicit
    c_3 = np.mean(psi_abs2 * np.exp(-3j * u_grid))
    c_0 = np.mean(psi_abs2)
    if c_0 == 0:
        return 0.0
    # Real part of c_3/c_0: phase 0 ⇒ +1, phase π ⇒ −1
    return float(np.real(c_3 / c_0))


def normalise_psi(psi: np.ndarray, sqrt_g: np.ndarray) -> np.ndarray:
    """Normalise ψ on the metric: ∫ |ψ|² √|g| du = 1."""
    integrand = np.abs(psi) ** 2 * sqrt_g
    norm = np.trapezoid(integrand) * (2.0 * pi / len(integrand))
    if norm <= 0:
        return psi
    return psi / np.sqrt(norm)


def find_mode_at_quantum_number(p_values: np.ndarray, vecs: np.ndarray,
                                  target_p: int) -> int:
    """Return the index of the eigenvector whose dominant Fourier component
    is closest to target_p. Used to select 'the m = N mode' for Mechanism-D
    testing."""
    target_idx = int(np.argmin(np.abs(p_values - target_p)))
    overlaps = np.abs(vecs[target_idx, :])
    return int(np.argmax(overlaps))


def run_single(args) -> None:
    """Compute and plot ψ(u) and |ψ(u)|² for one mode at given k_v."""
    eps = args.epsilon
    chi = args.chi
    k_v = args.k_v
    mode = args.mode

    eigs, vecs, p_values = hill_eigenvalues(
        k_v, eps, chi, args.n_grid, args.n_eigenvalues,
        sigma=args.sigma, tau=args.tau, return_eigvecs=True,
    )

    n_modes = len(eigs)
    if mode >= n_modes:
        raise SystemExit(f"--mode {mode} ≥ available eigenstates {n_modes}")

    # u-grid for visualisation
    N_u = 600
    u_grid = np.linspace(0.0, 2.0 * pi, N_u, endpoint=False)

    psi = evaluate_psi(p_values, vecs[:, mode], u_grid)
    lobe_mask, sqrt_g, P_x_u = lobe_mask_and_metric(eps, chi, u_grid)
    psi = normalise_psi(psi, sqrt_g)
    psi_abs2 = np.abs(psi) ** 2

    L, S = localization_fractions(psi_abs2, sqrt_g, lobe_mask)
    baseline = lobe_baseline_fraction(eps, chi)
    cls = classify(L, baseline)
    align = antinode_alignment(u_grid, psi_abs2)
    dominant_p = int(p_values[np.argmax(np.abs(vecs[:, mode]))])

    print(f"Wavefunction at (ε, χ, k_v) = ({eps}, {chi}, {k_v}); mode index {mode}")
    print(f"  μ² = {eigs[mode]:.6f}")
    print(f"  dominant p (cross-section wavenumber) = {dominant_p}")
    print(f"  lobe overlap L = {L:.4f},  saddle overlap S = {S:.4f}")
    print(f"  geometric baseline (uniform-wave L) = {baseline:.4f}")
    print(f"  excess Δ = L − baseline = {L - baseline:+.4f}")
    print(f"  Z₃-alignment (real c_3/c_0) = {align:+.4f}")
    print(f"  classification: {cls}")

    args.outputs_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True,
                              gridspec_kw={"height_ratios": [2, 1]})
    # Top: |ψ|² with lobe regions shaded
    ax = axes[0]
    ax.plot(u_grid, psi_abs2, color="C0", linewidth=1.8,
            label=r"$|\psi(u)|^2$")
    # Shade lobe regions
    for k in range(3):
        fund_start = k * 2.0 * pi / 3.0
        # Get the lobe-extent inside this fundamental domain
        # phi_L (in fund-domain units) = (2π/3) · 2r_lobe / (2r_lobe + r_saddle)
        r_lobe = eps / (2.0 + chi)
        r_saddle = chi * r_lobe
        phi_L = (2.0 * pi / 3.0) * (2.0 * r_lobe) / (2.0 * r_lobe + r_saddle)
        ax.axvspan(fund_start, fund_start + phi_L, color="C2", alpha=0.10)
        ax.axvspan(fund_start + phi_L, fund_start + 2.0 * pi / 3.0,
                   color="C3", alpha=0.10)
    ax.set_ylabel(r"$|\psi(u)|^2$")
    ax.set_title(
        f"Mode {mode}: ε={eps}, χ={chi}, k_v={k_v:.4f}, dominant p={dominant_p},  "
        f"μ²={eigs[mode]:.4g}\n"
        f"L={L:.3f}  S={S:.3f}  Z₃-align={align:+.3f}  →  {cls}  "
        f"(green = lobe, red = saddle)",
        fontsize=10,
    )
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3)

    # Bottom: P_x (the cross-section profile structure for reference)
    ax = axes[1]
    ax.plot(u_grid, P_x_u, color="black", linewidth=1.2,
            label=r"$P_x(u)$ (cross-section profile radial component)")
    ax.set_xlabel("u (helical cross-section coordinate)")
    ax.set_ylabel(r"$P_x(u)$")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right")

    out_path = (args.outputs_dir
                / f"wavefn_loc_eps{eps:.2f}_chi{chi:.2f}"
                  f"_kv{k_v:.4f}_mode{mode}.png")
    fig.tight_layout()
    fig.savefig(out_path, dpi=120, bbox_inches="tight")
    print(f"  Saved: {out_path}")


def run_doublet_test(args) -> None:
    """Mechanism-D doublet test: for each m ∈ {1, 2, 3}, find the two lowest
    eigenstates with dominant cross-section wavenumber close to m, then
    classify each as lobe-focused or saddle-focused.

    Output: CSV table of m, mass, classification, L, S, Z₃-alignment;
    PNG showing all six wavefunctions side-by-side.
    """
    eps = args.epsilon
    chi = args.chi
    sigma = args.sigma
    tau = args.tau

    # We need to cover several Bloch sectors to find m ∈ {1, 2, 3}.
    # m = |p|; the dominant-p convention: m_t = p in our Hill setup.
    # For m_t = 1: k_v sector = m_r − 2τ m_t = m_r − 2/3, integer m_r gives k_v ∈ {..., −2/3, 1/3, 4/3, ...}. Use k_v = 1/3 (m_r = 1).
    # For m_t = 2: k_v = m_r − 4/3 → use k_v = 2/3 (m_r = 2).
    # For m_t = 3: k_v = m_r − 2 → use k_v = 0 (m_r = 2 wraps).
    test_cases = [
        # (m_target, k_v, p_target, m_r_for_label)
        (1, 1.0 / 3.0, 1, 1),
        (2, 2.0 / 3.0, 2, 2),
        (3, 0.0, 3, 2),
    ]

    N_u = 600
    u_grid = np.linspace(0.0, 2.0 * pi, N_u, endpoint=False)
    lobe_mask, sqrt_g, P_x_u = lobe_mask_and_metric(eps, chi, u_grid)

    rows = []
    fig, axes = plt.subplots(3, 2, figsize=(12, 10), sharex=True)
    baseline = lobe_baseline_fraction(eps, chi)

    for row_idx, (m_target, k_v, p_target, m_r_label) in enumerate(test_cases):
        eigs, vecs, p_values = hill_eigenvalues(
            k_v, eps, chi, args.n_grid, args.n_eigenvalues,
            sigma=sigma, tau=tau, return_eigvecs=True,
        )

        # Find candidate eigenstates whose dominant Fourier component is
        # ±p_target (the m-wave structure).
        candidates = []
        for j in range(len(eigs)):
            v = vecs[:, j]
            dominant = int(p_values[np.argmax(np.abs(v))])
            if abs(dominant) == p_target:
                psi = evaluate_psi(p_values, v, u_grid)
                psi = normalise_psi(psi, sqrt_g)
                psi_abs2 = np.abs(psi) ** 2
                L, _ = localization_fractions(psi_abs2, sqrt_g, lobe_mask)
                align = antinode_alignment(u_grid, psi_abs2)
                candidates.append({
                    "j": j, "mu2": float(eigs[j]), "dominant": dominant,
                    "L": L, "S": 1.0 - L, "align": align,
                    "psi_abs2": psi_abs2,
                })

        # Sort by mass, take the two lowest
        candidates.sort(key=lambda c: c["mu2"])
        if len(candidates) < 2:
            print(f"  m = {m_target}: WARNING only {len(candidates)} "
                  f"candidate(s) with |p| = {p_target} found; "
                  "increase --n-eigenvalues")
            sel = candidates[:1]
        else:
            sel = candidates[:2]

        # Identify which is lobe-focused vs saddle-focused
        # (by signed Z₃-alignment, +ve = lobe, −ve = saddle).
        sel.sort(key=lambda c: -c["align"])  # lobe-focused first
        labels = (
            ["lobe-focused", "saddle-focused"] if len(sel) == 2
            else ["solo (no doublet)"]
        )

        for col_idx, (cand, label) in enumerate(zip(sel, labels)):
            cls = classify(cand["L"], baseline)
            rows.append((m_target, k_v, m_r_label, label, cand["dominant"],
                         cand["mu2"], cand["L"], cand["S"], cand["align"], cls))

            ax = axes[row_idx, col_idx]
            ax.plot(u_grid, cand["psi_abs2"], color="C0", linewidth=1.5)
            # Shade lobe/saddle regions
            r_lobe = eps / (2.0 + chi)
            r_saddle = chi * r_lobe
            phi_L = (2.0 * pi / 3.0) * (2.0 * r_lobe) / (2.0 * r_lobe + r_saddle)
            for k in range(3):
                fund_start = k * 2.0 * pi / 3.0
                ax.axvspan(fund_start, fund_start + phi_L,
                           color="C2", alpha=0.12)
                ax.axvspan(fund_start + phi_L, fund_start + 2.0 * pi / 3.0,
                           color="C3", alpha=0.12)
            ax.set_title(
                f"m = {m_target}  ({label})\n"
                f"μ² = {cand['mu2']:.4g}, dominant p = {cand['dominant']:+d}, "
                f"L = {cand['L']:.3f}, Z₃ = {cand['align']:+.3f}  →  {cls}",
                fontsize=9,
            )
            ax.set_ylabel(r"$|\psi(u)|^2$")
            ax.grid(True, alpha=0.3)
            if row_idx == 2:
                ax.set_xlabel("u")

        # Pad the row if we only found one candidate
        if len(sel) < 2:
            axes[row_idx, 1].axis("off")

    fig.suptitle(
        f"Mechanism-D doublet test: ε={eps}, χ={chi}, σ={sigma}, τ={tau:.4f}\n"
        f"(green shading = lobe regions, red = saddle regions)",
        fontsize=11,
    )
    fig.tight_layout()

    args.outputs_dir.mkdir(parents=True, exist_ok=True)
    plot_path = (args.outputs_dir
                 / f"doublet_test_eps{eps:.2f}_chi{chi:.2f}"
                   f"_sigma{sigma:.3f}.png")
    fig.savefig(plot_path, dpi=120, bbox_inches="tight")

    csv_path = (args.outputs_dir
                / f"doublet_test_eps{eps:.2f}_chi{chi:.2f}"
                  f"_sigma{sigma:.3f}.csv")
    with open(csv_path, "w") as f:
        f.write("m,k_v,m_r,label,dominant_p,mu2,L,S,Z3_align,classification\n")
        for m, kv, mr, lbl, dom, mu2, L, S, al, cls in rows:
            f.write(f"{m},{kv:.6f},{mr},{lbl},{dom},{mu2:.6f},"
                    f"{L:.6f},{S:.6f},{al:.6f},{cls}\n")

    print()
    print(f"Geometric baseline (uniform-wave L) = {baseline:.4f} at χ = {chi}")
    print()
    print(f"{'m':>3}  {'label':>15}  {'dominant_p':>10}  {'μ²':>10}  "
          f"{'L':>6}  {'Δ=L−base':>8}  {'Z₃':>7}  {'class':>22}")
    print("-" * 102)
    for m, kv, mr, lbl, dom, mu2, L, S, al, cls in rows:
        print(f"{m:3d}  {lbl:>15}  {dom:+10d}  {mu2:10.4g}  "
              f"{L:6.3f}  {L - baseline:+8.3f}  {al:+7.3f}  {cls:>22}")
    print()
    print(f"Wrote: {plot_path.name}")
    print(f"Wrote: {csv_path.name}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epsilon", type=float, default=0.5)
    parser.add_argument("--chi", type=float, default=1.0)
    parser.add_argument("--sigma", type=float, default=0.0)
    parser.add_argument("--tau", type=float, default=1.0 / 3.0)
    parser.add_argument("--n-grid", type=int, default=512)
    parser.add_argument("--n-eigenvalues", type=int, default=12)
    parser.add_argument("--k-v", type=float, default=1.0 / 3.0)
    parser.add_argument("--mode", type=int, default=0,
                        help="Eigenstate index to visualise (single-mode mode).")
    parser.add_argument("--doublet-test", action="store_true",
                        help="Run the Mechanism-D doublet test across m ∈ {1,2,3} "
                        "instead of a single-mode visualisation.")
    parser.add_argument("--outputs-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "outputs")
    args = parser.parse_args()

    if args.doublet_test:
        run_doublet_test(args)
    else:
        run_single(args)


if __name__ == "__main__":
    main()
