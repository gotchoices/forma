#!/usr/bin/env python3
"""
R21 Track 2: Position-dependent charge on the curved torus.

QUESTION
========
On flat T², the R19 charge integral gives α for the (1,2) mode.
The integral factorizes:

  Q ∝ [∫ cos(Θ+X)(R + a cos Θ)dΘ] × [∫ cos(q_eff Φ) dΦ]
    = aπ cos(X) × sin(2πq_eff)/q_eff

The θ₁ integral picks out the n₁ = 1 component through
the area element's cos θ₁ factor:

  ∫ cos(Θ+X) cos(Θ) dΘ = π cos(X)   ← only nonzero for n₁ = ±1

On the curved torus, the eigenmode f(θ₁) replaces cos θ₁.
The "charge overlap integral" becomes:

  C(mode) = ∫₀²π f(θ₁) × cos θ₁ × (1 + ε cos θ₁) dθ₁

Different modes have different C values → different charges
from the same shear.

KEY SYMMETRY: The Sturm-Liouville equation is invariant under
θ₁ → 2π − θ₁ (parity).  Eigenmodes are either EVEN (cos-like,
f(2π−θ) = f(θ)) or ODD (sin-like, f(2π−θ) = −f(θ)).

Since cos θ₁ and (1 + ε cos θ₁) are both even:
  - EVEN modes: C ≠ 0 in general (even × even × even = even)
  - ODD modes:  C = 0 exactly  (odd × even × even = odd)

Only even modes carry charge.
"""

import sys
import os
import math
import numpy as np
from scipy import linalg

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha


def build_eigenvalue_system(eps, n2, N):
    """Build S f = λ W f for the curved torus (from Track 1)."""
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


def get_sorted_modes(eps, n2, N):
    """Solve the eigenvalue problem and return sorted eigenvalues/vectors."""
    S, W = build_eigenvalue_system(eps, n2, N)
    eigenvalues, eigenvectors = linalg.eigh(S, W)
    idx = np.argsort(eigenvalues)
    return eigenvalues[idx], eigenvectors[:, idx]


def classify_parity(f, N):
    """
    Classify an eigenfunction as even or odd under θ → 2π − θ.
    Returns ('even', score) or ('odd', score) where score ∈ [0, 1].
    """
    f_rev = np.array([f[(-j) % N] for j in range(N)])
    overlap = np.dot(f, f_rev) / (np.linalg.norm(f)**2)
    if overlap > 0:
        return 'even', abs(overlap)
    else:
        return 'odd', abs(overlap)


def charge_overlap(f, eps, N):
    """
    Compute the charge overlap integral:
      C = ∫₀²π f(θ₁) cos(θ₁) (1 + ε cos θ₁) dθ₁

    Uses trapezoidal rule on the N-point grid.
    """
    h = 2 * math.pi / N
    theta = np.array([2 * math.pi * j / N for j in range(N)])
    integrand = f * np.cos(theta) * (1 + eps * np.cos(theta))
    return np.sum(integrand) * h


def alpha_curved(C, r, s, n2=2):
    """
    Effective α for a curved-torus mode with charge overlap C.

    On flat T² (n₁=1, cos-like): C_flat = π, and
      α_flat = r² sin²(2πs) / (4π (n₂-s)² √(r²(1+n₂s)²+n₂²))

    The charge Q ∝ C × sin(2πs)/q_eff, so α ∝ C².
    We normalize: α_curved = (C/π)² × α_flat.
    """
    q_eff = n2 - s
    sn = math.sin(2 * math.pi * s)
    if abs(sn) < 1e-15 or abs(q_eff) < 1e-15:
        return 0.0
    d = math.sqrt(r**2 * (1 + n2 * s)**2 + n2**2)
    alpha_flat = r**2 * sn**2 / (4 * math.pi * q_eff**2 * d)
    return (C / math.pi)**2 * alpha_flat


def solve_electron_s(r):
    """Solve for electron shear s such that α_flat = 1/137."""
    def alpha_flat(s):
        q = 2 - s
        sn = math.sin(2 * math.pi * s)
        if abs(sn) < 1e-15 or abs(q) < 1e-15:
            return 0.0
        d = math.sqrt(r**2 * (1 + 2 * s)**2 + 4)
        return r**2 * sn**2 / (4 * math.pi * q**2 * d)

    from scipy.optimize import brentq
    ss = np.linspace(0.001, 0.499, 5000)
    fs = [alpha_flat(s) - alpha for s in ss]
    solutions = []
    for i in range(len(fs) - 1):
        if fs[i] * fs[i + 1] < 0:
            s_root = brentq(lambda s: alpha_flat(s) - alpha, ss[i], ss[i + 1])
            solutions.append(s_root)
    return solutions[0] if solutions else None


def main():
    N = 256
    n2 = 2

    # ==================================================================
    print("=" * 72)
    print("SECTION 1: Charge overlap integral C(mode) vs curvature ε")
    print("=" * 72)
    print()
    print("C = ∫ f(θ₁) cos(θ₁) (1 + ε cos θ₁) dθ₁")
    print("On flat T²: C(cos-like n₁=1) = π, C(sin-like) = 0, C(n₁=0) = 0.")
    print("On curved T²: even modes have C ≠ 0; odd modes always C = 0.")
    print()

    theta = np.array([2 * math.pi * j / N for j in range(N)])

    eps_values = [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]

    print(f"{'ε':>6s}  {'Mode':>12s}  {'Parity':>6s}  {'λ':>10s}  "
          f"{'C':>10s}  {'C/π':>8s}  {'(C/π)²':>8s}")
    print("-" * 72)

    for eps in eps_values:
        eigenvalues, eigenvectors = get_sorted_modes(eps, n2, N)

        for idx in range(min(6, len(eigenvalues))):
            f = eigenvectors[:, idx]

            # Normalize so that ∫|f|² w dθ = 2π
            w = 1 + eps * np.cos(theta)
            norm = np.sqrt(np.sum(f**2 * w) * 2 * math.pi / N)
            f = f / norm * math.sqrt(2 * math.pi)

            parity, score = classify_parity(f, N)
            C = charge_overlap(f, eps, N)
            C_over_pi = C / math.pi

            label = f"idx={idx}"
            print(f"{eps:6.2f}  {label:>12s}  {parity:>6s}  "
                  f"{eigenvalues[idx]:10.4f}  {C:10.6f}  "
                  f"{C_over_pi:8.4f}  {C_over_pi**2:8.4f}")

        print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 2: Charge ratios between modes")
    print("=" * 72)
    print()
    print("Target for quarks: ratios of 2/3 and 1/3 relative to electron.")
    print("The electron is the lowest even mode with C ≈ π (the cos-like")
    print("n₁ = 1 mode on flat T²).")
    print()

    print("The electron is identified as the even mode with LARGEST |C|")
    print("(the mode with the most cos θ₁ content = the n₁≈1 cos-like mode).")
    print()

    print(f"{'ε':>6s}  {'e⁻ idx':>6s}  {'C_electron':>12s}  "
          f"{'C(ground)':>12s}  {'ratio₀':>8s}  "
          f"{'C(next even)':>12s}  {'ratio':>8s}")
    print("-" * 80)

    for eps in eps_values:
        eigenvalues, eigenvectors = get_sorted_modes(eps, n2, N)
        w = 1 + eps * np.cos(theta)

        C_all = []
        parities = []
        for idx in range(min(10, len(eigenvalues))):
            f = eigenvectors[:, idx]
            norm = np.sqrt(np.sum(f**2 * w) * 2 * math.pi / N)
            f = f / norm * math.sqrt(2 * math.pi)
            C_all.append(charge_overlap(f, eps, N))
            p, _ = classify_parity(f, N)
            parities.append(p)

        # Find the electron mode: even mode with LARGEST |C|
        electron_idx = max(
            (i for i, p in enumerate(parities) if p == 'even'),
            key=lambda i: abs(C_all[i]),
            default=None
        )

        if electron_idx is None:
            print(f"{eps:6.2f}  (no electron mode found)")
            continue

        C_e = C_all[electron_idx]

        # Ground state (idx=0, always even)
        C_0 = C_all[0]
        ratio_0 = C_0 / C_e if abs(C_e) > 1e-15 else 0

        # Find other even modes with nonzero C
        other_even = [
            (i, C_all[i]) for i in range(len(C_all))
            if parities[i] == 'even' and i != electron_idx and abs(C_all[i]) > 1e-6
        ]
        if other_even:
            next_idx, C_next = max(other_even, key=lambda x: abs(x[1]))
            ratio_next = C_next / C_e
        else:
            C_next = 0
            ratio_next = 0

        print(f"{eps:6.2f}  {electron_idx:6d}  {C_e:12.6f}  {C_0:12.6f}  "
              f"{ratio_0:8.4f}  {C_next:12.6f}  {ratio_next:8.4f}")

    # ==================================================================
    print()
    print("=" * 72)
    print("SECTION 3: Effective α for each mode")
    print("=" * 72)
    print()
    print("Using R19 shear formula with curved-torus overlap integral.")
    print("α_eff = (C/π)² × α_flat(r, s)")
    print()

    for r in [2.0, 3.0, 5.0, 10.0]:
        s = solve_electron_s(r)
        if s is None:
            continue

        eps = 1.0 / r
        if eps >= 1.0:
            continue

        print(f"--- r = {r:.1f}, ε = {eps:.3f}, s = {s:.6f} "
              f"(α_flat = 1/137) ---")
        print()

        eigenvalues, eigenvectors = get_sorted_modes(eps, n2, N)
        w = 1 + eps * np.cos(theta)

        print(f"  {'idx':>4s}  {'Parity':>6s}  {'λ':>10s}  "
              f"{'C':>10s}  {'C/π':>8s}  {'α_eff':>12s}  "
              f"{'Q/e':>8s}  {'Label':>12s}")
        print("  " + "-" * 80)

        electron_alpha = None
        for idx in range(min(8, len(eigenvalues))):
            f = eigenvectors[:, idx]
            norm = np.sqrt(np.sum(f**2 * w) * 2 * math.pi / N)
            f = f / norm * math.sqrt(2 * math.pi)

            parity, _ = classify_parity(f, N)
            C = charge_overlap(f, eps, N)
            alpha_eff = alpha_curved(C, r, s, n2) if parity == 'even' else 0.0
            Q_over_e = math.sqrt(alpha_eff / alpha) if alpha_eff > 0 else 0.0

            if parity == 'odd':
                label = "(uncharged)"
            elif abs(C) < 0.01:
                label = "(~zero)"
            else:
                label = ""

            print(f"  {idx:4d}  {parity:>6s}  {eigenvalues[idx]:10.4f}  "
                  f"{C:10.6f}  {C / math.pi:8.4f}  {alpha_eff:12.8f}  "
                  f"{Q_over_e:8.4f}  {label:>12s}")
        print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 4: Scanning for quark charge ratios")
    print("=" * 72)
    print()
    print("For each ε, compute charge ratios of even modes relative")
    print("to the electron (cos-like n₁≈1).  Look for 2/3 or 1/3.")
    print()

    target_ratios = [1/3, 2/3]
    best_matches = []

    eps_scan = np.linspace(0.01, 0.95, 200)
    for eps in eps_scan:
        eigenvalues, eigenvectors = get_sorted_modes(eps, n2, N)
        w = 1 + eps * np.cos(theta)

        C_list = []
        for idx in range(min(8, len(eigenvalues))):
            f = eigenvectors[:, idx]
            norm = np.sqrt(np.sum(f**2 * w) * 2 * math.pi / N)
            f = f / norm * math.sqrt(2 * math.pi)
            p, _ = classify_parity(f, N)
            C = charge_overlap(f, eps, N) if p == 'even' else 0.0
            C_list.append((C, p, idx))

        # Find electron: even mode with largest |C|
        even_modes = [(C, idx) for C, p, idx in C_list if p == 'even']
        if not even_modes:
            continue
        C_e = max(even_modes, key=lambda x: abs(x[0]))[0]
        if abs(C_e) < 1e-10:
            continue

        # Check all other even modes for ratio matches
        for C, p, idx in C_list:
            if p != 'even' or abs(C) < 1e-6:
                continue
            ratio = abs(C / C_e)
            if ratio > 0.99:
                continue
            for target in target_ratios:
                if abs(ratio - target) < 0.02:
                    best_matches.append((eps, idx, ratio, target, C, C_e))

    if best_matches:
        print("Found matches (within ±0.02 of target):")
        print(f"{'ε':>8s}  {'idx':>4s}  {'C/C_e':>8s}  {'Target':>8s}  "
              f"{'C':>10s}  {'C_e':>10s}")
        print("-" * 55)
        for eps, idx, ratio, target, C, C_e in best_matches:
            print(f"{eps:8.4f}  {idx:4d}  {ratio:8.4f}  {target:8.4f}  "
                  f"{C:10.6f}  {C_e:10.6f}")
    else:
        print("No charge ratios matching 1/3 or 2/3 found in this scan.")

    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 5: Full ratio landscape")
    print("=" * 72)
    print()
    print("All charge ratios C(mode)/C(electron) for even modes,")
    print("at selected ε values.")
    print()

    for eps in [0.1, 0.2, 0.3, 0.5, 0.7, 0.9]:
        eigenvalues, eigenvectors = get_sorted_modes(eps, n2, N)
        w = 1 + eps * np.cos(theta)

        print(f"ε = {eps}, r = {1/eps:.2f}:")

        results = []
        for idx in range(min(10, len(eigenvalues))):
            f = eigenvectors[:, idx]
            norm = np.sqrt(np.sum(f**2 * w) * 2 * math.pi / N)
            f = f / norm * math.sqrt(2 * math.pi)
            p, _ = classify_parity(f, N)
            C = charge_overlap(f, eps, N) if p == 'even' else 0.0
            results.append((idx, p, eigenvalues[idx], C))

        even_C = [C for idx, p, lam, C in results if p == 'even']
        C_e = max(even_C, key=abs) if even_C else None

        if C_e is None:
            print("  (no electron mode found)")
            continue

        print(f"  {'idx':>4s}  {'Parity':>6s}  {'λ':>10s}  "
              f"{'C':>10s}  {'C/C_e':>8s}  {'(C/C_e)²':>10s}")
        print("  " + "-" * 60)
        for idx, p, lam, C in results:
            ratio = C / C_e if abs(C_e) > 1e-15 else 0
            print(f"  {idx:4d}  {p:>6s}  {lam:10.4f}  "
                  f"{C:10.6f}  {ratio:8.4f}  {ratio**2:10.4f}")
        print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 6: Summary and implications")
    print("=" * 72)
    print()

    # Compute key numbers for the summary
    for eps in [0.3, 0.5]:
        eigenvalues, eigenvectors = get_sorted_modes(eps, n2, N)
        w = 1 + eps * np.cos(theta)

        C_vals = []
        parities = []
        for idx in range(min(6, len(eigenvalues))):
            f = eigenvectors[:, idx]
            norm = np.sqrt(np.sum(f**2 * w) * 2 * math.pi / N)
            f = f / norm * math.sqrt(2 * math.pi)
            p, _ = classify_parity(f, N)
            C = charge_overlap(f, eps, N) if p == 'even' else 0.0
            C_vals.append(C)
            parities.append(p)

        even_C = [C for C, p in zip(C_vals, parities) if p == 'even']
        C_e = max(even_C, key=abs) if even_C else None

        if C_e is None:
            continue

        print(f"At ε = {eps} (r = {1/eps:.1f}):")
        for i, (C, p) in enumerate(zip(C_vals, parities)):
            ratio = C / C_e if abs(C_e) > 1e-15 else 0
            print(f"  Mode {i}: parity={p}, C = {C:.6f}, "
                  f"C/C_e = {ratio:.4f}, "
                  f"Q/Q_e = {ratio:.4f}")
        print()


if __name__ == "__main__":
    main()
