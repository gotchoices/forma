"""
neutrino_1d_fit.py — fit the 1D neutrino substrate with a Wilson-loop flux.

The neutrino is hosted on a closed 1D curve with N-fold-symmetric shape

    r(phi) = R * [1 + a1*cos(N phi) + a2*cos(2N phi)]      (tube-function family)

Modes are eigenstates of the intrinsic Laplace-Beltrami operator on the curve.

THE PROBLEM.  A featureless circle — or any C_N-symmetric shape — gives the
lowest three nonzero modes a fixed 1 : 1 : 2 mass pattern: an n = +-1
degenerate doublet plus the n = -2 mode at twice the mass.  A C_N-symmetric
shape perturbation cannot split the doublet (it is symmetry-protected), so the
observed (30, 33, 60) meV hierarchy is unreachable.  This is the ~6% wall
documented in config-neutrino.md NC.5-NC.6.

THE LEVER.  Per grid-primitive ch.9, a small substrate antisymmetric chirality
chi_anti is equivalent to a built-in background gauge field.  On a compact
wrap it contributes a gauge-invariant Wilson-loop phase (an Aharonov-Bohm
flux).  The closed neutrino loop IS such a wrap, so a nu wave circulating it
picks up a flux Phi.  In the operator this is a covariant derivative
D_s = d/ds + i A_s, which shifts mode n to (n + f) with f = Phi / 2pi:

    eigenvalue(n)  proportional to  (n + f)^2

The n = +-1 doublet then splits LINEARLY in f — the first-order lever a
C_N-symmetric shape lacks.  The lowest nonzero modes become
(1-f) : (1+f) : (2-f), which can match 1 : 1.1 : 2.

This script fits (R, a1, a2, f) for N = 3 to the working nu masses
(30, 33, 60) meV, and sweeps f to exhibit the mechanism.

NOTE on the n = 0 mode.  With f != 0 the constant mode (n = 0) is no longer
massless; it acquires mass proportional to f (~5% of m_1).  The script skips
it as the substrate ground state and fits the three observed neutrinos to
n = -1, +1, -2.  The light n = 0 state is a prediction of this mechanism
(see config-neutrino.md NC for discussion).

Inputs : command-line (see --help); all default sensibly.
Outputs: outputs/neutrino_1d_fit.txt
"""

from __future__ import annotations

import argparse
import numpy as np
import scipy.linalg as la
from scipy.optimize import least_squares
from math import pi
from pathlib import Path


HBARC_MEV_FM = 197.3269804

# Project working values from candidate_fits.py (R49 / model-F Family A)
NEUTRINO_MASSES_MEV = np.array([3.0e-8, 3.3e-8, 6.0e-8])  # 30, 33, 60 meV


def arc_speed(phi: np.ndarray, R: float, a1: float, a2: float,
              N: int) -> np.ndarray:
    """Arc speed g(phi) = sqrt(r^2 + (dr/dphi)^2) for the C_N-symmetric polar
       curve r(phi) = R * [1 + a1*cos(N phi) + a2*cos(2N phi)]."""
    r = R * (1.0 + a1 * np.cos(N * phi) + a2 * np.cos(2 * N * phi))
    drdphi = R * (-N * a1 * np.sin(N * phi) - 2 * N * a2 * np.sin(2 * N * phi))
    return np.sqrt(r * r + drdphi * drdphi)


def eigenvalues(R: float, a1: float, a2: float, N: int,
                flux: float = 0.0, K: int = 128,
                n_lowest: int = 8) -> np.ndarray:
    """Sorted lowest n_lowest eigenvalues of the intrinsic Laplace-Beltrami
       operator on the closed shaped curve, with a Wilson-loop flux fraction
       f = flux threaded through the loop.

       The flux enters as a covariant derivative: each nearest-neighbour
       hopping carries a Peierls phase exp(i * 2pi*flux / K), so the total
       phase around the loop is 2pi*flux.  Mode n then has eigenvalue
       proportional to (n + flux)^2.  flux = 0 recovers the plain operator.
    """
    phi = np.linspace(0, 2 * pi, K, endpoint=False)
    dphi = 2 * pi / K
    g = arc_speed(phi, R, a1, a2, N)
    g_half = 0.5 * (g + np.roll(g, -1))  # g at half-grid points (i + 1/2)

    ph = np.exp(1j * 2 * pi * flux / K)  # per-hop Peierls phase

    A = np.zeros((K, K), dtype=complex)
    for i in range(K):
        ip = (i + 1) % K
        im = (i - 1) % K
        w_plus = 1.0 / g_half[i]
        w_minus = 1.0 / g_half[im]
        A[i, i] = (w_plus + w_minus) / dphi
        A[i, ip] = -w_plus / dphi * ph
        A[i, im] = -w_minus / dphi * np.conj(ph)

    B_diag = g * dphi
    # A is complex-Hermitian, B is real positive-diagonal.
    eigvals = la.eigh(A, np.diag(B_diag), eigvals_only=True)
    return eigvals[:n_lowest]


def lowest_three_masses(R: float, a1: float, a2: float, N: int,
                        flux: float = 0.0, K: int = 128) -> np.ndarray:
    """The three neutrino masses (MeV): the n = -1, +1, -2 modes.

    The single lowest mode (n = 0; massless at flux = 0, mass proportional to
    flux otherwise) is skipped as the substrate ground state.  The remaining
    three lowest eigenvalues are the neutrino mass eigenstates.
    """
    evals = eigenvalues(R, a1, a2, N, flux, K=K, n_lowest=6)
    masses = HBARC_MEV_FM * np.sqrt(np.abs(evals[1:4]))
    return masses


def fit(N: int = 3, K: int = 96, n_seeds: int = 80) -> dict:
    """Fit (R, a1, a2, flux) for chosen N to the three observed nu masses."""
    target = NEUTRINO_MASSES_MEV
    phi_check = np.linspace(0, 2 * pi, 512, endpoint=False)

    def residuals(x):
        log_R, a1, a2, flux = x
        r_test = (1.0 + a1 * np.cos(N * phi_check)
                  + a2 * np.cos(2 * N * phi_check))
        if np.min(r_test) < 0.05:
            return np.array([10.0, 10.0, 10.0])
        try:
            m = lowest_three_masses(10 ** log_R, a1, a2, N, flux, K)
            if len(m) < 3 or not np.all(np.isfinite(m)):
                return np.array([1e3, 1e3, 1e3])
            m_sorted = np.sort(m)
            return np.log10(m_sorted / target)
        except Exception:
            return np.array([1e3, 1e3, 1e3])

    starts = []
    for seed in range(n_seeds):
        rng = np.random.default_rng(seed)
        starts.append([
            rng.uniform(8.0, 10.5),   # log10 R in fm  (cm-scale)
            rng.uniform(-0.5, 0.5),   # a1 (N-fold shape)
            rng.uniform(-0.3, 0.3),   # a2 (2N-fold shape)
            rng.uniform(0.0, 0.35),   # flux fraction f
        ])
    # Targeted: near-circle at the analytically-expected flux f ~ 0.048.
    for f0 in [0.03, 0.048, 0.07, 0.10]:
        starts.append([8.8, 0.0, 0.0, f0])
        starts.append([9.0, 0.2, 0.0, f0])
        starts.append([9.0, -0.2, 0.0, f0])

    best = None
    for x0 in starts:
        try:
            res = least_squares(
                residuals, x0,
                bounds=([6, -0.85, -0.85, 0.0], [12, 0.85, 0.85, 0.5]),
                method="trf", max_nfev=400,
            )
            m = lowest_three_masses(10 ** res.x[0], res.x[1], res.x[2], N,
                                    res.x[3], K)
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
                    flux=res.x[3],
                    N=N,
                    masses=m_sorted,
                )
        except Exception:
            continue
    return best


def fit_fixed_flux(N: int, flux: float, K: int = 96,
                   n_seeds: int = 30) -> tuple | None:
    """Best fit of (R, a1, a2) to the three nu masses at a FIXED flux.
       Used by the flux sweep.  Returns (max_err%, R, a1, a2, masses)."""
    target = NEUTRINO_MASSES_MEV
    phi_check = np.linspace(0, 2 * pi, 512, endpoint=False)

    def residuals(x):
        log_R, a1, a2 = x
        r_test = (1.0 + a1 * np.cos(N * phi_check)
                  + a2 * np.cos(2 * N * phi_check))
        if np.min(r_test) < 0.05:
            return np.array([10.0, 10.0, 10.0])
        try:
            m = np.sort(lowest_three_masses(10 ** log_R, a1, a2, N, flux, K))
            return np.log10(m / target)
        except Exception:
            return np.array([1e3, 1e3, 1e3])

    best = None
    for seed in range(n_seeds):
        rng = np.random.default_rng(seed)
        x0 = [rng.uniform(8.0, 10.5), rng.uniform(-0.5, 0.5),
              rng.uniform(-0.3, 0.3)]
        try:
            res = least_squares(
                residuals, x0,
                bounds=([6, -0.85, -0.85], [12, 0.85, 0.85]),
                method="trf", max_nfev=300,
            )
            m = np.sort(lowest_three_masses(10 ** res.x[0], res.x[1],
                                            res.x[2], N, flux, K))
            max_err = max(abs(100 * (m_p - m_o) / m_o)
                          for m_p, m_o in zip(m, target))
            if best is None or max_err < best[0]:
                best = (max_err, 10 ** res.x[0], res.x[1], res.x[2], m)
        except Exception:
            continue
    return best


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--N", type=int, default=3,
                    help="lobe count for the primary fit (default 3)")
    ap.add_argument("--K", type=int, default=96,
                    help="grid resolution for the fit (default 96)")
    ap.add_argument("--seeds", type=int, default=80,
                    help="random restart count for the fit (default 80)")
    args = ap.parse_args()

    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "neutrino_1d_fit.txt"

    lines = []
    lines.append("=" * 80)
    lines.append("1D neutrino substrate fit  —  Wilson-loop flux mechanism")
    lines.append("Substrate: closed curve r(phi) = R[1 + a1 cos(N phi)"
                 " + a2 cos(2N phi)]")
    lines.append("Operator:  intrinsic Laplace-Beltrami + Wilson-loop flux f")
    lines.append("           (mode n  ->  eigenvalue proportional to (n+f)^2)")
    lines.append("Targets:   m_nu1 = 30 meV,  m_nu2 = 33 meV,  m_nu3 = 60 meV")
    lines.append("Flux origin: substrate antisymmetric chirality chi_anti")
    lines.append("             (grid-primitive ch.9) threaded through the loop.")
    lines.append("=" * 80)
    lines.append("")

    # --- Baseline: featureless circle, no flux ---------------------------
    lines.append("--- Baseline: featureless circle, NO flux (f = 0) ---")
    R_test = HBARC_MEV_FM / NEUTRINO_MASSES_MEV[0]
    m0 = lowest_three_masses(R_test, 0.0, 0.0, 3, flux=0.0, K=128)
    lines.append(f"  R = {R_test:.4g} fm")
    for i, m in enumerate(m0):
        lines.append(f"    m_{i+1} = {m * 1e9:8.4g} meV   "
                     f"(ratio to m_1: {m / m0[0]:.4f})")
    lines.append("  -> 1 : 1 : 2.  The n=+-1 doublet is exactly degenerate;")
    lines.append("     no C_N-symmetric shape can split it (the 6% wall).")
    lines.append("")

    # --- Circle WITH flux: the doublet splits ----------------------------
    lines.append("--- Featureless circle WITH flux: the doublet splits ---")
    lines.append(f"  {'flux f':>8}  {'m_1 (meV)':>11}  {'m_2 (meV)':>11}  "
                 f"{'m_3 (meV)':>11}  {'m_2/m_1':>9}  {'m_3/m_1':>9}")
    for f in [0.0, 0.02, 0.0476, 0.10]:
        m = lowest_three_masses(R_test, 0.0, 0.0, 3, flux=f, K=128)
        lines.append(f"  {f:8.4f}  {m[0]*1e9:11.4f}  {m[1]*1e9:11.4f}  "
                     f"{m[2]*1e9:11.4f}  {m[1]/m[0]:9.4f}  {m[2]/m[0]:9.4f}")
    lines.append("  The flux shifts mode n to (n+f); lowest three nonzero")
    lines.append("  modes go as (1-f) : (1+f) : (2-f).  f ~ 0.048 gives the")
    lines.append("  observed 1 : 1.10 : ~2.05 — doublet split is now first-order.")
    lines.append("")

    # --- Flux sweep: best fit error as a function of flux ----------------
    lines.append("--- Flux sweep: best fit of (R, a1, a2) at each fixed f ---")
    lines.append(f"  {'flux f':>8}  {'best max|delta%|':>16}  {'a1':>8}  "
                 f"{'a2':>8}")
    for f in [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.10]:
        b = fit_fixed_flux(args.N, f, K=args.K, n_seeds=30)
        if b is None:
            lines.append(f"  {f:8.4f}  {'(no fit)':>16}")
            continue
        lines.append(f"  {f:8.4f}  {b[0]:16.4f}  {b[2]:+8.4f}  {b[3]:+8.4f}")
    lines.append("  Error collapses from the ~6% wall (f=0) toward ~0 as f")
    lines.append("  approaches the doublet-splitting value.")
    lines.append("")

    # --- Full fit: (R, a1, a2, flux) all free ----------------------------
    lines.append(f"--- N = {args.N} full fit: (R, a1, a2, flux) free ---")
    r = fit(N=args.N, K=args.K, n_seeds=args.seeds)
    if r is not None and r['max_err'] < 1000:
        R = r['R']
        lines.append(f"  Best max |delta%| = {r['max_err']:.4f}%")
        lines.append(f"  R    = {R:.4g} fm  ~  {R * 1e-10:.4g} cm")
        lines.append(f"  a1   = {r['a1']:+.4f}   (cos({args.N}phi) amplitude)")
        lines.append(f"  a2   = {r['a2']:+.4f}   (cos({2*args.N}phi) amplitude)")
        lines.append(f"  flux = {r['flux']:.5f}   (Wilson-loop fraction"
                     f" f = Phi/2pi)")
        for i, (m, t) in enumerate(zip(r['masses'], NEUTRINO_MASSES_MEV)):
            err = 100 * (m - t) / t
            lines.append(f"  nu_{i+1}: pred = {m * 1e9:8.4f} meV   "
                         f"obs = {t * 1e9:5.1f} meV   delta% = {err:+8.4f}")
        # the skipped n = 0 light state
        ev = eigenvalues(R, r['a1'], r['a2'], args.N, r['flux'],
                         K=128, n_lowest=6)
        m0_light = HBARC_MEV_FM * np.sqrt(abs(ev[0]))
        lines.append(f"  (n=0 ground state, skipped: m_0 = {m0_light*1e9:.4f}"
                     f" meV — a predicted light state)")
    else:
        lines.append("  No fit converged.")
    lines.append("")

    # --- N = 2, 4 comparison ---------------------------------------------
    for N in [2, 4]:
        if N == args.N:
            continue
        lines.append(f"--- N = {N} full fit (for comparison) ---")
        r = fit(N=N, K=args.K, n_seeds=max(40, args.seeds // 2))
        if r is not None and r['max_err'] < 1000:
            lines.append(f"  Best max |delta%| = {r['max_err']:.4f}%   "
                         f"flux = {r['flux']:.5f}")
            lines.append(f"  R = {r['R']:.4g} fm  a1 = {r['a1']:+.4f}  "
                         f"a2 = {r['a2']:+.4f}")
        else:
            lines.append("  No fit converged.")
        lines.append("")

    text = "\n".join(lines)
    print(text)
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
