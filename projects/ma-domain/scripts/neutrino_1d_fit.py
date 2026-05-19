"""
neutrino_1d_fit.py — fit the 1D shaped neutrino substrate.

Solves the intrinsic Laplace-Beltrami eigenvalue problem on a closed 1D curve

    r(φ) = R · [1 + a1·cos(Nφ) + a2·cos(2Nφ) + δ·cos(φ + φ0)]

per neutrino-1D.md §2 and §4.  Identifies the three lowest mass eigenstates
as the lowest band's three states: a singlet (q=0) plus a doublet (q=±1) in
the unbroken C_N limit, with the doublet split by the 1-fold breaker δ.

Per neutrino-1D.md §4.1, this is the correct interpretation: the three ν
masses are NOT three different |n| harmonics but rather the three lowest
eigenvalues of the operator, including the doublet pair as two separate
states.

The script fits (R, a1, a2, δ, φ₀) for N = 3 to the project's working ν
masses (30, 33, 60) meV.

Outputs to outputs/neutrino_1d_fit.txt
"""

from __future__ import annotations

import numpy as np
import scipy.linalg as la
from scipy.optimize import least_squares
from math import pi
from pathlib import Path


HBARC_MEV_FM = 197.3269804

# Project working values from candidate_fits.py (R49 / model-F Family A)
NEUTRINO_MASSES_MEV = np.array([3.0e-8, 3.3e-8, 6.0e-8])  # 30, 33, 60 meV


def arc_speed(phi: np.ndarray, R: float, a1: float, a2: float,
              N: int, delta: float = 0.0, phi0: float = 0.0) -> np.ndarray:
    """Arc speed g(φ) = sqrt(r² + (dr/dφ)²) for the polar curve with shape
       r(φ) = R · [1 + a1·cos(Nφ) + a2·cos(2Nφ) + δ·cos(φ + φ0)]."""
    r = R * (1.0 + a1 * np.cos(N * phi) + a2 * np.cos(2 * N * phi)
             + delta * np.cos(phi + phi0))
    drdphi = R * (-N * a1 * np.sin(N * phi)
                  - 2 * N * a2 * np.sin(2 * N * phi)
                  - delta * np.sin(phi + phi0))
    return np.sqrt(r * r + drdphi * drdphi)


def eigenvalues(R: float, a1: float, a2: float, N: int,
                delta: float = 0.0, phi0: float = 0.0,
                K: int = 128, n_lowest: int = 8) -> np.ndarray:
    """Sorted lowest n_lowest eigenvalues of the intrinsic Laplace-Beltrami."""
    phi = np.linspace(0, 2 * pi, K, endpoint=False)
    dphi = 2 * pi / K
    g = arc_speed(phi, R, a1, a2, N, delta, phi0)
    g_half = 0.5 * (g + np.roll(g, -1))  # g at half-grid points (i + 1/2)

    A = np.zeros((K, K))
    for i in range(K):
        ip = (i + 1) % K
        im = (i - 1) % K
        w_plus = 1.0 / g_half[i]
        w_minus = 1.0 / g_half[im]
        A[i, i] = (w_plus + w_minus) / dphi
        A[i, ip] = -w_plus / dphi
        A[i, im] = -w_minus / dphi

    B_diag = g * dphi
    eigvals = la.eigh(A, np.diag(B_diag), eigvals_only=True)
    return eigvals[:n_lowest]


def lowest_three_masses(R: float, a1: float, a2: float, N: int,
                        delta: float = 0.0, phi0: float = 0.0,
                        K: int = 128) -> np.ndarray:
    """
    Return the lowest three NON-ZERO eigenvalues as masses (in MeV).
    NO grouping of degenerate pairs — the doublet halves are kept separate
    and serve as m_1, m_2; the singlet is m_3.
    """
    evals = eigenvalues(R, a1, a2, N, delta, phi0, K=K, n_lowest=6)
    # Skip the trivial ground state (eigenvalue ≈ 0)
    nonzero = evals[evals > evals[1] * 1e-4]
    masses = HBARC_MEV_FM * np.sqrt(nonzero[:3])
    return masses


def fit(N: int = 3, K: int = 96, n_seeds: int = 60) -> dict:
    """Fit (R, a1, a2, δ, φ₀) for chosen N to the three observed ν masses."""
    target = NEUTRINO_MASSES_MEV
    phi_check = np.linspace(0, 2 * pi, 512, endpoint=False)

    def residuals(x):
        log_R, a1, a2, delta, phi0 = x
        # Validity check: r > 0 everywhere (require r >= 0.05 R for safety)
        r_test = (1.0 + a1 * np.cos(N * phi_check)
                  + a2 * np.cos(2 * N * phi_check)
                  + delta * np.cos(phi_check + phi0))
        if np.min(r_test) < 0.05:
            # Curve is invalid (r goes negative or near zero); penalize
            return np.array([10.0, 10.0, 10.0])
        try:
            m = lowest_three_masses(10 ** log_R, a1, a2, N, delta, phi0, K)
            if len(m) < 3:
                return np.array([1e3, 1e3, 1e3])
            m_sorted = np.sort(m)
            return np.log10(m_sorted / target)
        except Exception:
            return np.array([1e3, 1e3, 1e3])

    best = None
    # Build a list of starting points: random + targeted "pure ellipse" + targeted "near-circle"
    starts = []
    for seed in range(n_seeds):
        rng = np.random.default_rng(seed)
        starts.append([
            rng.uniform(8.5, 11.5),   # log10 R in fm  (cm-scale)
            rng.uniform(-0.5, 0.5),   # a1 (N-fold shape)
            rng.uniform(-0.3, 0.3),   # a2 (2N-fold shape)
            rng.uniform(-0.4, 0.4),   # δ (1-fold C_N-breaker)
            rng.uniform(0, 2 * pi),   # phi0
        ])
    # Targeted: pure-ellipse (a1=a2=0, only δ) at various δ — natural for doublet splitting
    for d in [0.05, 0.1, 0.15, 0.2, 0.3]:
        starts.append([9.82, 0.0, 0.0, d, 0.0])   # log10 R ~ 6.6e9 fm gives m_1=30 meV
        starts.append([9.82, 0.0, 0.0, -d, 0.0])
    # Targeted: N-shape + small breaker, both signs of a1
    for a1 in [0.2, -0.2, 0.4, -0.4]:
        for d in [0.05, 0.1, 0.2]:
            starts.append([9.6, a1, 0.0, d, 0.0])

    for x0 in starts:
        try:
            res = least_squares(
                residuals, x0,
                bounds=([6, -0.85, -0.85, -0.85, -pi], [14, 0.85, 0.85, 0.85, 3 * pi]),
                method="trf", max_nfev=300,
            )
            m = lowest_three_masses(10 ** res.x[0], res.x[1], res.x[2], N,
                                    res.x[3], res.x[4], K)
            if len(m) < 3:
                continue
            m_sorted = np.sort(m)
            max_err = max(abs(100 * (m_p - m_o) / m_o)
                          for m_p, m_o in zip(m_sorted, target))
            if best is None or max_err < best["max_err"]:
                best = dict(
                    max_err=max_err,
                    R=10 ** res.x[0],
                    a1=res.x[1],
                    a2=res.x[2],
                    delta=res.x[3],
                    phi0=res.x[4] % (2 * pi),
                    N=N,
                    masses=m_sorted,
                )
        except Exception:
            continue
    return best


def main():
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "neutrino_1d_fit.txt"

    lines = []
    lines.append("=" * 80)
    lines.append("1D shaped neutrino substrate fit  (lowest-3-modes reading)")
    lines.append("Substrate: r(φ) = R·[1 + a1·cos(Nφ) + a2·cos(2Nφ) + δ·cos(φ + φ0)]")
    lines.append("Operator:  intrinsic Laplace-Beltrami on the closed curve")
    lines.append("Targets:   m_ν₁ = 30 meV,  m_ν₂ = 33 meV,  m_ν₃ = 60 meV")
    lines.append("Per neutrino-1D.md §4.1: the three masses are the lowest band's")
    lines.append("doublet (m_1, m_2, q=±1) plus singlet (m_3, q=0). NO grouping.")
    lines.append("=" * 80)
    lines.append("")

    # Baseline: featureless circle (no shape) — shows the lowest-3-modes structure
    lines.append("--- Baseline: featureless circle (a1=a2=δ=0) ---")
    R_test = HBARC_MEV_FM / NEUTRINO_MASSES_MEV[0]
    m_circle = lowest_three_masses(R_test, 0.0, 0.0, 3, K=128)
    lines.append(f"  R = {R_test:.4g} fm  ≈  {R_test * 1e-10:.3g} cm  "
                 f"(set so n=1 mode = 30 meV)")
    lines.append(f"  Lowest 3 eigenvalue masses (with doublet kept as two states):")
    for i, m in enumerate(m_circle):
        ratio = m / m_circle[0]
        lines.append(f"    m_{i+1} = {m * 1e9:.4g} meV  "
                     f"(ratio to m_1: {ratio:.3f})")
    lines.append("")
    lines.append("  Circle gives 1 : 1 : 2 — the doublet n=±1 is exactly degenerate,")
    lines.append("  n=+2 (one half of next doublet) sits at 2× the mass.")
    lines.append("  Observed 1 : 1.10 : 2.00 needs a small C-symmetry breaker to")
    lines.append("  lift m_1 ≠ m_2 by ~10%, while keeping m_3 ≈ 2·m_1.")
    lines.append("")

    # Fit for N = 3 (the natural choice given 3 mass eigenstates)
    lines.append("--- N = 3 fit (3 lobes; q=±1 doublet + q=0 singlet) ---")
    r = fit(N=3, K=96, n_seeds=60)
    if r is not None and r['max_err'] < 1000:
        R = r['R']
        lines.append(f"  Best max |Δ%| = {r['max_err']:.4f}%")
        lines.append(f"  R  = {R:.4g} fm  ≈  {R * 1e-10:.3g} cm")
        lines.append(f"  a1 = {r['a1']:+.4f}  (cos(3φ) amplitude)")
        lines.append(f"  a2 = {r['a2']:+.4f}  (cos(6φ) amplitude)")
        lines.append(f"  δ  = {r['delta']:+.4f}  (1-fold C_3 breaker)")
        lines.append(f"  φ₀ = {r['phi0']:.4f}  rad")
        for i, (m, t) in enumerate(zip(r['masses'], NEUTRINO_MASSES_MEV)):
            err = 100 * (m - t) / t
            lines.append(f"  ν_{i+1}: pred = {m * 1e9:>8.4f} meV  "
                         f"obs = {t * 1e9:>5.1f} meV  Δ% = {err:+8.4f}")
    else:
        lines.append("  No fit converged.")
    lines.append("")

    # Also try N = 2 and N = 4 for comparison
    for N in [2, 4]:
        lines.append(f"--- N = {N} fit (for comparison) ---")
        r = fit(N=N, K=96, n_seeds=40)
        if r is not None and r['max_err'] < 1000:
            lines.append(f"  Best max |Δ%| = {r['max_err']:.4f}%")
            lines.append(f"  R = {r['R']:.4g} fm  a1 = {r['a1']:+.4f}  "
                         f"a2 = {r['a2']:+.4f}  δ = {r['delta']:+.4f}")
            for i, (m, t) in enumerate(zip(r['masses'], NEUTRINO_MASSES_MEV)):
                err = 100 * (m - t) / t
                lines.append(f"  ν_{i+1}: pred = {m * 1e9:>8.4f} meV  "
                             f"obs = {t * 1e9:>5.1f} meV  Δ% = {err:+8.4f}")
        else:
            lines.append("  No fit converged.")
        lines.append("")

    text = "\n".join(lines)
    print(text)
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
