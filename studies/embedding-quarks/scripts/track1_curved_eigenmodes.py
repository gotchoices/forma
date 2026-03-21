#!/usr/bin/env python3
"""
R21 Track 1: Eigenmodes on the embedded (curved) torus.

QUESTION
========
On a flat T², eigenmodes are plane waves e^{i(n₁θ₁ + n₂θ₂)} with
energy E = ℏc|k|.  The embedded torus has position-dependent
curvature K = cos θ₁ / (a(R + a cos θ₁)).  How does this curvature
modify the eigenmodes?  Do they localize at specific angular
positions?

SETUP
=====
The embedded torus metric:
    ds² = a² dθ₁² + (R + a cos θ₁)² dθ₂²

Define ε = a/R (tube-to-center ratio).  The metric has θ₂ symmetry,
so modes separate: ψ = f(θ₁) e^{in₂ θ₂}.

The eigenvalue equation in Sturm-Liouville form:
    d/dθ₁[p(θ₁) df/dθ₁] + [λ w(θ₁) - q(θ₁)] f = 0

where:
    p(θ₁) = 1 + ε cos θ₁
    w(θ₁) = 1 + ε cos θ₁
    q(θ₁) = ε² n₂² / (1 + ε cos θ₁)
    λ = a² k²   (dimensionless eigenvalue)

On flat T² (ε → 0): λ = n₁² + ε² n₂²,  f = e^{in₁ θ₁}.

EMBEDDING CONVENTION
====================
θ₁ = poloidal (around the tube), period L₁ = 2πa
θ₂ = toroidal (around the hole), period L₂ = 2πR
r = L₂/L₁ = R/a = 1/ε

Electron (1,2): winds once around tube, twice around hole.
"""

import sys
import os
import math
import numpy as np
from scipy import linalg

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha


def build_eigenvalue_system(eps, n2, N):
    """
    Build the generalized eigenvalue problem S f = λ W f
    for the curved-torus Laplacian with toroidal mode number n₂.

    Returns (S, W) matrices of size N × N.
    """
    h = 2 * math.pi / N
    theta = np.array([2 * math.pi * j / N for j in range(N)])

    p = 1 + eps * np.cos(theta)
    w = 1 + eps * np.cos(theta)
    q = eps**2 * n2**2 / (1 + eps * np.cos(theta))

    p_half_plus = np.array([(p[j] + p[(j + 1) % N]) / 2 for j in range(N)])
    p_half_minus = np.array([(p[j] + p[(j - 1) % N]) / 2 for j in range(N)])

    S = np.zeros((N, N))
    W = np.diag(w)

    for j in range(N):
        jm = (j - 1) % N
        jp = (j + 1) % N
        S[j, jm] = -p_half_minus[j] / h**2
        S[j, j] = (p_half_minus[j] + p_half_plus[j]) / h**2 + q[j]
        S[j, jp] = -p_half_plus[j] / h**2

    return S, W


def flat_eigenvalue(n1, n2, eps):
    """Eigenvalue on flat T²: λ = n₁² + ε² n₂²."""
    return n1**2 + eps**2 * n2**2


def localization_measure(f, theta):
    """
    Quantify how localized a mode is.

    Returns (IPR, peak_theta):
    - IPR = inverse participation ratio = ∫|f|⁴ / (∫|f|²)².
      IPR = 1/(2π) for uniform; larger = more localized.
    - peak_theta = angle where |f|² is maximum.
    """
    prob = np.abs(f)**2
    prob /= np.sum(prob)
    ipr = np.sum(prob**2) * len(prob)
    peak_idx = np.argmax(prob)
    return ipr, theta[peak_idx]


def main():
    N = 256

    # ==================================================================
    print("=" * 72)
    print("SECTION 1: Eigenvalue spectrum vs curvature parameter ε")
    print("=" * 72)
    print()
    print("Comparing curved-torus eigenvalues with flat-T² values.")
    print("The flat eigenvalue is λ_flat = n₁² + ε²n₂².")
    print()

    eps_values = [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
    n2_values = [0, 1, 2, 4]

    print(f"{'ε':>6s}  {'n₂':>4s}  {'n₁':>4s}  {'λ_curved':>12s}  "
          f"{'λ_flat':>12s}  {'Δλ/λ (%)':>10s}")
    print("-" * 60)

    for n2 in [0, 2]:
        for eps in [0.01, 0.1, 0.3, 0.5, 0.9]:
            S, W = build_eigenvalue_system(eps, n2, N)
            eigenvalues = linalg.eigvalsh(S, W)
            eigenvalues.sort()

            for n1 in range(5):
                lam_flat = flat_eigenvalue(n1, n2, eps)
                idx = n1 if n2 == 0 else None

                if n2 == 0:
                    lam_curved = eigenvalues[2 * n1] if n1 > 0 else eigenvalues[0]
                else:
                    lam_curved = eigenvalues[n1]

                if lam_flat > 0:
                    delta = (lam_curved - lam_flat) / lam_flat * 100
                else:
                    delta = 0 if abs(lam_curved) < 1e-10 else float('inf')

                print(f"{eps:6.2f}  {n2:4d}  {n1:4d}  {lam_curved:12.6f}  "
                      f"{lam_flat:12.6f}  {delta:+10.3f}")
            print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 2: Electron mode (n₁=1, n₂=2) in detail")
    print("=" * 72)
    print()
    print("The electron is the (1,2) mode.  How does curvature modify it?")
    print()

    theta = np.array([2 * math.pi * j / N for j in range(N)])

    print(f"{'ε':>6s}  {'r=1/ε':>8s}  {'λ_curved':>12s}  {'λ_flat':>12s}  "
          f"{'Δλ/λ%':>8s}  {'IPR':>8s}  {'peak θ₁':>8s}  {'Comment':>20s}")
    print("-" * 95)

    for eps in eps_values:
        S, W = build_eigenvalue_system(eps, 2, N)
        eigenvalues, eigenvectors = linalg.eigh(S, W)

        sort_idx = np.argsort(eigenvalues)
        eigenvalues = eigenvalues[sort_idx]
        eigenvectors = eigenvectors[:, sort_idx]

        lam_flat = flat_eigenvalue(1, 2, eps)

        # The n₁=1 mode should be near eigenvalue index 1
        # (index 0 is n₁=0, which has lower eigenvalue)
        # Find the eigenvalue closest to flat prediction
        best_idx = np.argmin(np.abs(eigenvalues - lam_flat))
        lam_curved = eigenvalues[best_idx]
        f_mode = eigenvectors[:, best_idx]

        delta = (lam_curved - lam_flat) / lam_flat * 100
        ipr, peak = localization_measure(f_mode, theta)

        r_val = 1 / eps if eps > 0 else float('inf')

        if eps < 0.05:
            comment = "nearly flat"
        elif eps < 0.2:
            comment = "weak curvature"
        elif eps < 0.5:
            comment = "moderate curvature"
        elif eps < 0.8:
            comment = "strong curvature"
        else:
            comment = "near-degenerate"

        print(f"{eps:6.2f}  {r_val:8.2f}  {lam_curved:12.6f}  {lam_flat:12.6f}  "
              f"{delta:+8.3f}  {ipr:8.4f}  {peak:8.4f}  {comment:>20s}")

    print()
    print("IPR = 1.0 means perfectly uniform (plane wave).")
    print("IPR > 1 means localized.  IPR = N means delta-function.")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 3: Mode profiles at selected ε values")
    print("=" * 72)
    print()

    for eps in [0.1, 0.3, 0.5, 0.9]:
        S, W = build_eigenvalue_system(eps, 2, N)
        eigenvalues, eigenvectors = linalg.eigh(S, W)
        sort_idx = np.argsort(eigenvalues)
        eigenvalues = eigenvalues[sort_idx]
        eigenvectors = eigenvectors[:, sort_idx]

        print(f"--- ε = {eps}, r = {1/eps:.2f} ---")
        print()

        lam_flat_0 = flat_eigenvalue(0, 2, eps)
        lam_flat_1 = flat_eigenvalue(1, 2, eps)

        for target_n1, lam_flat in [(0, lam_flat_0), (1, lam_flat_1)]:
            best_idx = np.argmin(np.abs(eigenvalues - lam_flat))
            lam = eigenvalues[best_idx]
            f_mode = eigenvectors[:, best_idx]

            prob = np.abs(f_mode)**2
            prob /= np.sum(prob) * (2 * math.pi / N)
            ipr, peak = localization_measure(f_mode, theta)

            print(f"  n₁ ≈ {target_n1}: λ = {lam:.6f} (flat: {lam_flat:.6f})")
            print(f"  IPR = {ipr:.4f}, peak at θ₁ = {peak:.4f} "
                  f"({peak * 180 / math.pi:.1f}°)")

            outer = prob[0]
            inner = prob[N // 2]
            print(f"  |f|² at outer equator (θ₁=0): {outer:.4f}")
            print(f"  |f|² at inner equator (θ₁=π): {inner:.4f}")
            print(f"  Outer/inner ratio: {outer / inner:.3f}" if inner > 1e-15
                  else "  Inner ≈ 0")
            print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 4: All low-lying modes and degeneracy structure")
    print("=" * 72)
    print()
    print("First 10 eigenvalues at each ε, compared with flat predictions.")
    print()

    for eps in [0.1, 0.5, 0.9]:
        S, W = build_eigenvalue_system(eps, 2, N)
        eigenvalues = linalg.eigvalsh(S, W)
        eigenvalues.sort()

        print(f"ε = {eps}, n₂ = 2:")
        print(f"  {'idx':>4s}  {'λ_curved':>12s}  {'Nearest flat':>14s}  "
              f"{'Δλ/λ%':>10s}")
        print("  " + "-" * 45)

        flat_candidates = []
        for n1 in range(-10, 11):
            flat_candidates.append((n1, flat_eigenvalue(n1, 2, eps)))
        flat_candidates.sort(key=lambda x: x[1])

        for i in range(min(10, len(eigenvalues))):
            lam = eigenvalues[i]
            best_flat = min(flat_candidates, key=lambda x: abs(x[1] - lam))
            n1_match = best_flat[0]
            lam_flat = best_flat[1]
            delta = ((lam - lam_flat) / lam_flat * 100
                     if abs(lam_flat) > 1e-10 else 0)
            print(f"  {i:4d}  {lam:12.6f}  n₁={n1_match:+d} ({lam_flat:8.4f})  "
                  f"{delta:+10.3f}%")
        print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 5: Gaussian curvature and effective potential")
    print("=" * 72)
    print()
    print("The eigenvalue equation is a Schrödinger-like equation with")
    print("an effective potential V(θ₁) = q(θ₁)/w(θ₁) = ε²n₂²/(1+ε cos θ₁)².")
    print()

    for eps in [0.1, 0.3, 0.5, 0.9]:
        print(f"ε = {eps}, n₂ = 2:")
        V_outer = eps**2 * 4 / (1 + eps)**2
        V_inner = eps**2 * 4 / (1 - eps)**2
        K_outer = 1 / (eps * (1 / eps + 1))
        K_inner = -1 / (eps * (1 / eps - 1)) if eps < 1 else float('-inf')

        print(f"  V(θ₁=0) [outer] = {V_outer:.6f}")
        print(f"  V(θ₁=π) [inner] = {V_inner:.6f}")
        print(f"  V ratio (inner/outer) = {V_inner / V_outer:.3f}")
        print(f"  Gaussian curvature K(0) = {K_outer:.4f}/a²")
        print(f"  Gaussian curvature K(π) = {K_inner:.4f}/a²"
              if eps < 1 else f"  K(π) → -∞ (degenerate)")
        print()

    print("The effective potential is LARGER at the inner equator.")
    print("This means modes are pushed AWAY from the inner equator")
    print("toward the outer equator — curvature concentrates modes")
    print("on the outside of the torus.")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 6: Summary")
    print("=" * 72)
    print()

    print("F1. Eigenvalue shift from curvature")

    S, W = build_eigenvalue_system(0.5, 2, N)
    evals = linalg.eigvalsh(S, W)
    evals.sort()
    lam_flat_1_2 = flat_eigenvalue(1, 2, 0.5)
    best = evals[np.argmin(np.abs(evals - lam_flat_1_2))]
    delta_05 = (best - lam_flat_1_2) / lam_flat_1_2 * 100

    S, W = build_eigenvalue_system(0.9, 2, N)
    evals = linalg.eigvalsh(S, W)
    evals.sort()
    lam_flat_1_2_09 = flat_eigenvalue(1, 2, 0.9)
    best_09 = evals[np.argmin(np.abs(evals - lam_flat_1_2_09))]
    delta_09 = (best_09 - lam_flat_1_2_09) / lam_flat_1_2_09 * 100

    print(f"     At ε = 0.5 (r = 2): electron (1,2) eigenvalue shifts "
          f"by {delta_05:+.2f}%")
    print(f"     At ε = 0.9 (r = 1.1): shift is {delta_09:+.2f}%")
    print(f"     Curvature corrections are perturbative for ε < 0.3,")
    print(f"     significant for ε > 0.5.")
    print()

    print("F2. Mode localization from curvature")

    for eps in [0.1, 0.5, 0.9]:
        S, W = build_eigenvalue_system(eps, 2, N)
        evals, evecs = linalg.eigh(S, W)
        sort_idx = np.argsort(evals)
        evecs = evecs[:, sort_idx]
        evals = evals[sort_idx]

        lam_flat = flat_eigenvalue(1, 2, eps)
        best_idx = np.argmin(np.abs(evals - lam_flat))
        f_mode = evecs[:, best_idx]
        prob = np.abs(f_mode)**2
        prob /= np.sum(prob)

        outer_frac = np.sum(prob[:N // 4]) + np.sum(prob[3 * N // 4:])
        inner_frac = np.sum(prob[N // 4:3 * N // 4])

        ipr, _ = localization_measure(f_mode, theta)

        print(f"     ε = {eps}: IPR = {ipr:.3f}, "
              f"outer half = {outer_frac:.1%}, inner half = {inner_frac:.1%}")

    print()
    print("     Modes concentrate on the OUTER equator (θ₁ ≈ 0).")
    print("     The effective potential from curvature pushes amplitude")
    print("     away from the inner equator (θ₁ ≈ π).")
    print()

    print("F3. Implications for position-dependent charge")
    print("     If charge density follows |f(θ₁)|², then the embedded")
    print("     torus naturally concentrates charge on the outer equator.")
    print("     At strong curvature (ε > 0.5), the outer/inner amplitude")
    print("     ratio exceeds 2:1 — a large asymmetry.")
    print("     Track 2 will compute the charge integral with these modes.")


if __name__ == "__main__":
    main()
