"""
Numerical Laplacian eigenvalue spectrum on the corrugated torus.

Computes the spectrum by direct finite-difference discretization of the
Hill equation (the 1D problem that arises from the helical reduction;
see work/clover-mass.md §2). For each ring-direction wavenumber k_v,
solve:

    L ψ = ω² ψ
    L = -(1/(c²(R+P_x))) d/du[(R+P_x) dψ/du] + k_v²/(R+P_x)² ψ

with periodic BC ψ(u+2π) = ψ(u) on u ∈ [0, 2π).

This script intentionally does NOT use the analytical mass formula
μ² = (n - 2m/3)² + (m/ε)² or the second-order PT formula. It just
discretizes the metric and solves the eigenvalue problem. The output
eigenvalues are then compared (in a separate report) against the
analytical predictions, providing an INDEPENDENT validation.

Usage:
    python scripts/laplacian_spectrum.py [--epsilon E] [--chi CHI]
                                          [--k-v K1,K2,...]
                                          [--n-grid N] [--n-eigenvalues NE]
                                          [--compare]

Outputs:
    outputs/spectrum_eps<E>_chi<C>.csv
    outputs/spectrum_eps<E>_chi<C>.png (if --compare)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.linalg as sla
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.geometry import ProfileParams, profile


def hill_eigenvalues(k_v: float, eps: float, chi: float, N: int, n_eigs: int,
                     sigma: float = 0.0, tau: float = 1.0 / 3.0) -> np.ndarray:
    """Lowest n_eigs eigenvalues μ² of the Hill operator at k_v, with
    correct Bloch sector restriction.

    Implemented in Fourier basis. The plane-wave modes e^{ipu} are restricted
    to p ≡ q (mod 3) where q = 3·k_v (must be integer), which is the Bloch-
    sector requirement on the corrugated torus.

    Generalised to nonzero rolled-leaf shear sigma (see work/clover-quarks.md
    §1.3, §10.3, work/clover-mass.md §§1-4). At sigma = 0 the operator
    reduces to the original tau-only Hill form.

    Derivation (R_major = 1 units, c = ε). The metric in helical coords
    (v = θ, u = φ + τθ) is:
        g_vv = w² − 2 σ τ ε²
        g_vu = σ ε²
        g_uu = ε²
    with w(u) = 1 + P_x(u) and determinant |g| = ε² · W̃ where
        W̃ ≡ w² − σ (σ + 2τ) ε².
    The Hill operator H acting on χ in ψ = e^{ik_v v} χ(u) has matrix
    elements ⟨p'|H|p⟩ (with self-adjoint weight √|g|):
        ⟨p'|H|p⟩ = p p' · P_κ + (p + p') · k_v · R_κ + k_v² · Q_κ
        ⟨p'|M|p⟩ = (√|g|)_κ
    where κ = p' − p, and the operator pieces (per work/clover-mass.md §2):
        P(u) = √|g| · g^uu = (w² − 2στε²) / (ε √W̃)
        Q(u) = √|g| · g^vv = ε / √W̃
        R(u) = √|g| · g^vu = −σ ε / √W̃ = −σ Q
    Subscript κ denotes the κ-th Fourier coefficient.

    For numerical normalisation (matching the original σ = 0 form), divide
    K and M by ε, giving:
        P/ε = (w² − 2στε²) / (ε² √W̃)
        Q/ε = 1 / √W̃
        R/ε = −σ / √W̃
        M/ε = √W̃
    At σ = 0 these reduce to (w/ε², 1/w, 0, w) — the original code's
    coefficients (where P_x = w − 1 and the existing a_κ accounting recovers
    p p' (w/ε²)_κ = (p²/ε²) δ_κ + (p p'/ε²) a_κ).

    N here is the FFT resolution (not a u-grid for finite differences).
    The Fourier-mode cutoff is P_max = N // 4 by default for safety.
    """
    # k_v must be a third-integer
    q_int = 3 * k_v
    if abs(q_int - round(q_int)) > 1e-9:
        raise ValueError(f"k_v = {k_v} not of form q/3 for integer q")
    q_int = int(round(q_int))

    P_max = max(10, n_eigs + 5)
    p_values = [p for p in range(-P_max, P_max + 1)
                if (p - q_int) % 3 == 0]
    n_modes = len(p_values)

    # Build profile and sample u-grid functions
    r_lobe = eps / (2.0 + chi)
    r_saddle = chi * r_lobe
    params = ProfileParams(r_lobe=r_lobe, r_saddle=r_saddle)
    u = np.linspace(0, 2 * np.pi, N, endpoint=False)
    P_x, _ = profile(u, params)
    w = 1.0 + P_x

    # σ-modified determinant factor W̃ = w² − σ(σ + 2τ) ε²
    sigma_sq_eps_sq = sigma * (sigma + 2.0 * tau) * eps**2
    W_tilde = w**2 - sigma_sq_eps_sq
    if np.any(W_tilde <= 0):
        raise ValueError(
            f"W̃ = w² − σ(σ+2τ)ε² became non-positive (σ={sigma}, ε={eps}); "
            "metric is degenerate. Use smaller σ or smaller ε."
        )
    sqrt_W_tilde = np.sqrt(W_tilde)

    # Operator pieces (normalised by ε, matching existing convention)
    P_func = (w**2 - 2.0 * sigma * tau * eps**2) / (eps**2 * sqrt_W_tilde)
    Q_func = 1.0 / sqrt_W_tilde
    R_func = -sigma / sqrt_W_tilde
    M_func = sqrt_W_tilde

    # Fourier coefficients
    P_coefs = np.fft.fft(P_func) / N
    Q_coefs = np.fft.fft(Q_func) / N
    R_coefs = np.fft.fft(R_func) / N
    M_coefs = np.fft.fft(M_func) / N

    def coef(arr, kappa: int) -> complex:
        return arr[kappa % N]

    # Build dense matrices K and M
    K = np.zeros((n_modes, n_modes), dtype=complex)
    M = np.zeros((n_modes, n_modes), dtype=complex)
    for i, p_i in enumerate(p_values):
        for j, p_j in enumerate(p_values):
            kappa = p_i - p_j  # ⟨ψ_{p_i}|·|ψ_{p_j}⟩ → Fourier index p_i - p_j
            K[i, j] = (p_i * p_j) * coef(P_coefs, kappa) \
                    + (p_i + p_j) * k_v * coef(R_coefs, kappa) \
                    + (k_v**2) * coef(Q_coefs, kappa)
            M[i, j] = coef(M_coefs, kappa)

    # Solve generalized eigenvalue (Hermitian)
    eigs = sla.eigh(K, M, eigvals_only=True)
    return np.sort(eigs.real)[:n_eigs]


def predicted_zeroth_order(k_v: float, eps: float, n_eigs: int,
                            sigma: float = 0.0) -> np.ndarray:
    """Analytical flat-limit prediction in helical-frame form.

    μ² = (k_v − σ p)² + (p/ε)² for integer p in the Bloch sector
    p ≡ q (mod 3) with q = 3·k_v. At σ = 0 this reduces to the original
    μ² = k_v² + (p/ε)². At σ ≠ 0, completing the square in (m_t, m_r) labels
    yields σ_eff = σ + 2τ for the cross-term (see work/clover-mass.md §4).

    This is the prediction we want to validate against, NOT used in computing
    the numerical eigenvalues above.
    """
    q_int = int(round(3 * k_v))
    p_range = [p for p in range(-(2 * n_eigs + 30), 2 * n_eigs + 31)
               if (p - q_int) % 3 == 0]
    predicted = sorted([(k_v - sigma * p) ** 2 + (p / eps) ** 2 for p in p_range])
    return np.array(predicted[:n_eigs])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epsilon", type=float, default=0.5,
                        help="Aspect ratio L_total/(2π R_major). Default 0.5.")
    parser.add_argument("--chi", type=float, default=1.0,
                        help="Corrugation ratio r_saddle/r_lobe. Default 1.0.")
    parser.add_argument("--sigma", type=float, default=0.0,
                        help="Rolled-leaf intrinsic shear (default 0.0). "
                        "Same units as tau. See work/clover-quarks.md §1.3, §10.3.")
    parser.add_argument("--tau", type=float, default=1.0 / 3.0,
                        help="Topological twist (default 1/3). Forced to k/3 by "
                        "the profile's Z_3 symmetry.")
    parser.add_argument("--k-v", type=str, default="0,0.3333,0.6667,1.0",
                        help="Comma-separated k_v values to sweep. Default "
                        "covers the third-integer Bloch sectors 0, 1/3, 2/3, 1.")
    parser.add_argument("--n-grid", type=int, default=512,
                        help="Number of u-grid points. Default 512.")
    parser.add_argument("--n-eigenvalues", type=int, default=6,
                        help="Lowest N eigenvalues to compute per k_v. Default 6.")
    parser.add_argument("--compare", action="store_true",
                        help="Generate comparison plot vs zeroth-order analytical formula.")
    parser.add_argument("--outputs-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "outputs")
    args = parser.parse_args()

    eps = args.epsilon
    chi = args.chi
    sigma = args.sigma
    tau = args.tau
    k_v_values = [float(x) for x in args.k_v.split(",")]
    eta = eps / (2.0 + chi)

    print(f"Hill spectrum: ε={eps}, χ={chi}, σ={sigma}, τ={tau}, "
          f"N={args.n_grid}, n_eigs={args.n_eigenvalues}")
    print(f"  η = ε/(2+χ) = {eta:.4f}  (PT valid when η ≪ 1)")
    print()

    # Build results table
    print(f"  {'k_v':>10} | " + " ".join(f"μ²_{i}".rjust(11) for i in range(args.n_eigenvalues)))
    print("  " + "-" * (12 + 12 * args.n_eigenvalues))
    rows = []
    for k_v in k_v_values:
        eigs = hill_eigenvalues(k_v, eps, chi, args.n_grid, args.n_eigenvalues,
                                sigma=sigma, tau=tau)
        rows.append((k_v, eigs))
        print(f"  {k_v:10.4f} | " + " ".join(f"{e:+11.5f}" for e in eigs))

    # If --compare, also print zeroth-order predictions side-by-side
    if args.compare:
        print()
        print(f"Comparison to zeroth-order analytical prediction μ² = (k_v − σ p)² + (p/ε)² (σ={sigma}):")
        print(f"  {'k_v':>10} | {'Numerical':>40} | {'Zeroth-order':>40} | {'Δ':>10}")
        for k_v, eigs in rows:
            pred = predicted_zeroth_order(k_v, eps, args.n_eigenvalues, sigma=sigma)
            num_str = " ".join(f"{e:+8.4f}" for e in eigs[:4])
            pred_str = " ".join(f"{e:+8.4f}" for e in pred[:4])
            delta = np.max(np.abs(eigs - pred))
            print(f"  {k_v:10.4f} | {num_str:>40} | {pred_str:>40} | {delta:10.5f}")

    # Save CSV
    args.outputs_dir.mkdir(parents=True, exist_ok=True)
    csv_path = args.outputs_dir / f"spectrum_eps{eps:.2f}_chi{chi:.2f}.csv"
    with open(csv_path, "w") as f:
        header = ["k_v"] + [f"mu2_{i}" for i in range(args.n_eigenvalues)]
        f.write(",".join(header) + "\n")
        for k_v, eigs in rows:
            f.write(f"{k_v:.6f}," + ",".join(f"{e:.8f}" for e in eigs) + "\n")
    print(f"\nSaved: {csv_path}")

    # Comparison plot
    if args.compare:
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))
        all_eigs_num = []
        all_eigs_pred = []
        for k_v, eigs in rows:
            pred = predicted_zeroth_order(k_v, eps, args.n_eigenvalues)
            ax.scatter([k_v] * len(eigs), eigs, color="C0", marker="o", s=40,
                       label="Numerical (Hill)" if k_v == k_v_values[0] else "")
            ax.scatter([k_v] * len(pred), pred, color="C1", marker="x", s=60,
                       label="Predicted (flat-limit)" if k_v == k_v_values[0] else "")
            all_eigs_num.extend(eigs)
            all_eigs_pred.extend(pred)
        ax.set_xlabel("k_v")
        ax.set_ylabel("μ² (mass squared, dimensionless)")
        ax.set_title(f"Hill-equation spectrum vs flat-limit formula\n"
                     f"ε={eps}, χ={chi}, η={eta:.3f}, N_grid={args.n_grid}")
        ax.grid(True, alpha=0.3)
        ax.legend()
        plot_path = args.outputs_dir / f"spectrum_eps{eps:.2f}_chi{chi:.2f}.png"
        fig.savefig(plot_path, dpi=120, bbox_inches="tight")
        print(f"Saved: {plot_path}")


if __name__ == "__main__":
    main()
