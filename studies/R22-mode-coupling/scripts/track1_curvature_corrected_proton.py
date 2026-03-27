#!/usr/bin/env python3
"""
R22 Track 1: Curvature-corrected harmonic energies and proton mass.

On flat T², each harmonic (n, 2n) has energy exactly n × m_e, so the
proton mass M = m_e + Σ n·f(n) is geometry-independent.  The embedded
torus's position-dependent curvature modifies mode energies, breaking
the exact E ∝ n scaling and making M depend on the aspect ratio r.

METHOD
======
Fourier-Galerkin spectral method for the Sturm-Liouville problem:

  d/dθ₁[(1+ε cos θ₁) df/dθ₁] + [λ(1+ε cos θ₁) − ε²n₂²/(1+ε cos θ₁)] f = 0

Self-adjoint form:  S f = λ W f
  S = D₁ᵀ diag(p) D₁ + diag(q)     (symmetric positive definite)
  W = diag(w)                         (diagonal positive definite)

where D₁ is the spectral first-derivative matrix (antisymmetric, exact).
This eliminates the O(h²k²) discretization error of finite differences,
which dominated the high-harmonic eigenvalues in the FD approach.

SECTION 4 proves that backreaction preserves θ₂ symmetry, ruling out
the R23 phonon-neutrino rescue path.
"""

import sys
import os
import math
import numpy as np
from scipy import linalg
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha, m_e

m_p = 1.67262192369e-27
MASS_RATIO = m_p / m_e  # 1836.15267


# ── Physics utilities ─────────────────────────────────────────────────

def alpha_mode_2d(r, s, m):
    q = m - s
    sn = math.sin(2 * math.pi * s)
    if abs(sn) < 1e-15 or abs(q) < 1e-15:
        return 0.0
    d = math.sqrt(r**2 * (1 + m * s)**2 + m**2)
    return r**2 * sn**2 / (4 * math.pi * q**2 * d)


def solve_shear(r):
    def f(s):
        return alpha_mode_2d(r, s, 2) - alpha
    ss = np.linspace(0.001, 0.499, 5000)
    fs = [f(s) for s in ss]
    for i in range(len(fs) - 1):
        if fs[i] * fs[i + 1] < 0:
            return brentq(f, ss[i], ss[i + 1], xtol=1e-14)
    return None


# ── Spectral Sturm-Liouville solver ──────────────────────────────────

def build_spectral_D1(N):
    """
    Spectral first-derivative matrix for periodic grid of N points.
    D₁ is antisymmetric and exact (no discretization error).

    N MUST be odd to avoid spurious Nyquist zero-eigenvalue mode.
    """
    assert N % 2 == 1, "N must be odd to avoid Nyquist artifact"
    k = np.zeros(N)
    for m in range(N):
        k[m] = m if m <= N // 2 else m - N
    ik = 1j * k

    D1 = np.zeros((N, N))
    for j in range(N):
        e_j = np.zeros(N)
        e_j[j] = 1.0
        D1[:, j] = np.fft.ifft(ik * np.fft.fft(e_j)).real
    return D1


def build_kinetic_matrix(eps, D1):
    """
    Kinetic part of the Sturm-Liouville operator:
      K = D₁ᵀ diag(p) D₁
    where p(θ) = 1 + ε cos θ.  Depends only on ε, not on n₂.
    """
    N = D1.shape[0]
    theta = 2 * np.pi * np.arange(N) / N
    p = 1.0 + eps * np.cos(theta)
    return D1.T @ (p[:, None] * D1), p


def solve_eigenvalues(K, p, eps, n2_eff, n_needed):
    """
    Solve the full Sturm-Liouville eigenvalue problem at given n₂_eff.
    Returns the first n_needed sorted eigenvalues.
    """
    N = K.shape[0]
    q = eps**2 * n2_eff**2 / p
    S = K + np.diag(q)
    W = np.diag(p)
    eigs = linalg.eigvalsh(S, W)
    eigs.sort()
    return eigs[:n_needed]


# ── Proton mass ───────────────────────────────────────────────────────

def bose_einstein(E, T):
    x = E / T
    if x > 500:
        return 0.0
    return 1.0 / (math.exp(x) - 1.0)


def proton_mass_flat(T_prime, n_max=300):
    M = 1.0
    for n in range(2, n_max + 1):
        M += float(n) / (math.exp(float(n) / T_prime) - 1.0)
    return M


def find_T_prime_flat(target=MASS_RATIO):
    def f(T):
        return proton_mass_flat(T) - target
    return brentq(f, 10.0, 100.0, xtol=1e-10)


# ═══════════════════════════════════════════════════════════════════════

def main():
    N = 255  # odd to avoid Nyquist artifact
    n_max = 60

    T_prime_flat = find_T_prime_flat()
    M_flat_check = proton_mass_flat(T_prime_flat)

    print("=" * 74)
    print("R22 TRACK 1: Curvature-corrected harmonic energies and proton mass")
    print("=" * 74)
    print()
    print(f"Method: Fourier-Galerkin spectral (N = {N} grid points, odd)")
    print(f"Harmonics: n = 2..{n_max}")
    print(f"Flat-torus T' = {T_prime_flat:.4f} m_e  →  M_flat = {M_flat_check:.2f} m_e")
    print()
    print("Conventions:")
    print("  Electron (1,2): cos-like eigenvalue (index 1) — lower energy")
    print("  Harmonic (n,2n): sin-like eigenvalue (index 2n)")
    print("  n₂_eff = n(2−s) for harmonic (n, 2n)")
    print()

    # Precompute spectral derivative matrix (once for all r)
    D1 = build_spectral_D1(N)

    # ── Verification: flat-torus eigenvalues ──────────────────────────
    print("Verification (ε = 0.001, n₂_eff = 2.0):")
    eps_test = 0.001
    K_test, p_test = build_kinetic_matrix(eps_test, D1)
    eigs_test = solve_eigenvalues(K_test, p_test, eps_test, 2.0, 8)
    print(f"  Eigenvalue indices and values (flat ε→0 expect "
          f"k² + ε²n₂² = k² + {eps_test**2 * 4:.6f}):")
    for i, ev in enumerate(eigs_test):
        k_expected = [0, 1, 1, 2, 2, 3, 3, 4][i]
        lam_expected = k_expected**2 + eps_test**2 * 4
        print(f"    index {i}: λ = {ev:.6f}  "
              f"(expected {lam_expected:.6f} for |k|={k_expected})")
    print()

    r_values = [3.0, 4.29, 6.0, 10.0, 20.0]

    # ── SECTION 1: Eigenvalue corrections ─────────────────────────────
    print("=" * 74)
    print("SECTION 1: Eigenvalue corrections for selected harmonics")
    print("=" * 74)
    print()

    for r in r_values:
        s = solve_shear(r)
        if s is None:
            continue
        eps = 1.0 / r

        K, p = build_kinetic_matrix(eps, D1)

        # Electron eigenvalue (cos-like at |n₁|=1)
        n2e = 2 - s
        eigs_e = solve_eigenvalues(K, p, eps, n2e, 4)
        lam_e = eigs_e[1]
        lam_e_flat = 1.0 + eps**2 * n2e**2

        print(f"r = {r:.2f}  ε = {eps:.4f}  s = {s:.6f}")
        print(f"  Electron: λ_flat = {lam_e_flat:.6f}  "
              f"λ_curved = {lam_e:.6f}  "
              f"Δλ/λ = {(lam_e - lam_e_flat)/lam_e_flat*100:+.6f}%")
        print()
        print(f"  {'n':>4s}  {'n₂_eff':>8s}  {'λ_flat':>12s}  "
              f"{'λ_curved':>12s}  {'Δλ/λ (%)':>10s}  "
              f"{'E/E_e flat':>10s}  {'E/E_e curv':>10s}")
        print(f"  {'-' * 74}")

        for n in [1, 2, 3, 5, 10, 20, 30, 40, 50, 60]:
            if n > n_max:
                break
            n2_eff = n * (2 - s)
            eigs = solve_eigenvalues(K, p, eps, n2_eff, 2 * n + 2)

            if n == 1:
                lam_curved = eigs[1]  # cos-like for electron
            else:
                lam_curved = eigs[2 * n]  # sin-like for harmonics

            lam_flat = n**2 + eps**2 * n2_eff**2
            delta_pct = (lam_curved - lam_flat) / lam_flat * 100

            ratio_flat = float(n)
            ratio_curved = math.sqrt(lam_curved / lam_e)

            print(f"  {n:4d}  {n2_eff:8.3f}  {lam_flat:12.4f}  "
                  f"{lam_curved:12.4f}  {delta_pct:+10.6f}  "
                  f"{ratio_flat:10.4f}  {ratio_curved:10.6f}")

        print(flush=True)

    # ── SECTION 2: Energy ratio deviation from n ──────────────────────
    print("=" * 74)
    print("SECTION 2: Deviation of E_curved(n,2n)/E_curved(1,2) from n")
    print("=" * 74)
    print()
    print("On flat T², E(n,2n)/E(1,2) = n exactly.  δ(n) = E_curved/E_e − n.")
    print()

    for r in [3.0, 4.29, 10.0]:
        s = solve_shear(r)
        eps = 1.0 / r
        K, p = build_kinetic_matrix(eps, D1)
        eigs_e = solve_eigenvalues(K, p, eps, 2 - s, 4)
        lam_e = eigs_e[1]

        print(f"r = {r:.2f}  ε = {eps:.4f}")
        print(f"  {'n':>4s}  {'E/E_e flat':>10s}  {'E/E_e curv':>10s}  "
              f"{'δ':>12s}  {'δ/n (ppm)':>10s}")
        print(f"  {'-' * 56}")

        max_dev = 0.0
        for n in range(2, n_max + 1):
            n2_eff = n * (2 - s)
            eigs = solve_eigenvalues(K, p, eps, n2_eff, 2 * n + 2)
            lam_n = eigs[2 * n]

            ratio_curved = math.sqrt(lam_n / lam_e)
            dev = ratio_curved - float(n)
            dev_ppm = dev / float(n) * 1e6
            max_dev = max(max_dev, abs(dev))

            if n <= 10 or n % 5 == 0:
                print(f"  {n:4d}  {float(n):10.4f}  {ratio_curved:10.6f}  "
                      f"{dev:+12.6f}  {dev_ppm:+10.1f}")

        print(f"  max |δ| over n=2..{n_max}: {max_dev:.6f} m_e")
        print(flush=True)

    # ── SECTION 3: Proton mass ────────────────────────────────────────
    print()
    print("=" * 74)
    print("SECTION 3: Proton mass M(r) with curvature corrections")
    print("=" * 74)
    print()
    print(f"M_flat = {MASS_RATIO:.2f} m_e  at  T' = {T_prime_flat:.4f} m_e")
    print()
    n_tail = 300

    r_scan = np.concatenate([
        np.arange(2.5, 6.0, 0.5),
        np.arange(6.0, 15.0, 1.0),
        np.arange(15.0, 30.0, 5.0),
    ])

    print(f"Exact S-L solve for n = 2..{n_max}; asymptotic correction "
          f"for n = {n_max+1}..{n_tail}.")
    print(f"Asymptotic: E(n)/E_e ≈ n × (1 + δ∞/n), where δ∞/n is the "
          f"converged ratio at n={n_max}.")
    print()
    print(f"  {'r':>6s}  {'ε':>6s}  {'δ∞/n (ppm)':>11s}  "
          f"{'M_curved':>10s}  {'ΔM':>10s}  {'ΔM/M (%)':>10s}")
    print(f"  {'-' * 68}")

    results = []
    for r in r_scan:
        s = solve_shear(r)
        if s is None:
            continue
        eps = 1.0 / r
        K, p = build_kinetic_matrix(eps, D1)

        n2e = 2 - s
        eigs_e = solve_eigenvalues(K, p, eps, n2e, 4)
        lam_e = eigs_e[1]

        # Exact part: n = 2..n_max
        M_curved = 1.0
        for n in range(2, n_max + 1):
            n2_eff = n * (2 - s)
            eigs = solve_eigenvalues(K, p, eps, n2_eff, 2 * n + 2)
            lam_n = eigs[2 * n]
            ratio = math.sqrt(lam_n / lam_e)
            f_n = bose_einstein(ratio, T_prime_flat)
            M_curved += ratio * f_n

        # Asymptotic correction factor from converged δ/n at n=n_max
        n2_eff_last = n_max * (2 - s)
        eigs_last = solve_eigenvalues(K, p, eps, n2_eff_last, 2 * n_max + 2)
        lam_last = eigs_last[2 * n_max]
        ratio_last = math.sqrt(lam_last / lam_e)
        delta_rel = ratio_last / n_max - 1.0  # δ∞/n
        delta_ppm = delta_rel * 1e6

        # Tail: n = n_max+1..n_tail using asymptotic ratio
        for n in range(n_max + 1, n_tail + 1):
            ratio = float(n) * (1.0 + delta_rel)
            f_n = bose_einstein(ratio, T_prime_flat)
            M_curved += ratio * f_n

        delta_M = M_curved - M_flat_check
        delta_pct = delta_M / M_flat_check * 100
        results.append((r, eps, M_curved, delta_M, delta_pct, delta_ppm))

        print(f"  {r:6.2f}  {eps:6.4f}  {delta_ppm:11.1f}  "
              f"{M_curved:10.2f}  {delta_M:+10.2f}  {delta_pct:+10.4f}",
              flush=True)

    print()
    if results:
        signs = set(1 if x[3] > 0 else -1 for x in results)
        if len(signs) > 1:
            for i in range(len(results) - 1):
                if results[i][3] * results[i + 1][3] < 0:
                    r_cross = (results[i][0] + results[i + 1][0]) / 2
                    print(f"  Mass crosses M_flat near r ≈ {r_cross:.1f}")
        closest = min(results, key=lambda x: abs(x[3]))
        print(f"  Closest to experiment: r = {closest[0]:.2f}  "
              f"(M = {closest[2]:.2f} m_e,  ΔM = {closest[3]:+.2f})")

    # ── SECTION 4: θ₂ backreaction ────────────────────────────────────
    print()
    print("=" * 74)
    print("SECTION 4: θ₂ symmetry of energy density (backreaction)")
    print("=" * 74)
    print()
    print("CLAIM: Energy density is θ₂-independent for every mode.")
    print()
    print("PROOF:")
    print("  ψ(θ₁, θ₂) = f(θ₁) · exp(i n₂_eff θ₂)")
    print("  |ψ|² = |f(θ₁)|²  (phase drops out)")
    print()
    print("  This holds for EVERY mode regardless of quantum numbers.")
    print("  For any statistical or coherent mixture:")
    print("    ⟨ρ(θ₁,θ₂)⟩ = Σ_n f_occ(n) · |f_n(θ₁)|²  (no θ₂ dependence)")
    print()
    print("CONSEQUENCE:")
    print("  1. Backreaction does NOT break θ₂ symmetry.")
    print("  2. n₂ remains an exactly conserved quantum number.")
    print("  3. Modes with different n₂ still cannot couple.")
    print("  4. The R23 phonon-neutrino rescue path is ruled out")
    print("     at the mean-field level, even with proton backreaction.")
    print()
    print("REMAINING NEUTRINO PATHS:")
    print("  (a) Separate T² per flavor (R20 Direction A)")
    print("  (b) Quantum fluctuations beyond mean field (suppressed)")
    print("  (c) Multi-torus or T³ topology (unexplored)")
    print("  (d) Moduli oscillation with spin mechanism (R23 F14)")


if __name__ == '__main__':
    main()
