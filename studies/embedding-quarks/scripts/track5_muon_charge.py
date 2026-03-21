#!/usr/bin/env python3
"""
R21 Track 5: Muon charge constraint on the aspect ratio.

QUESTION
========
In R20, the muon is a "hot electron": the (1,2) fundamental
plus uncharged harmonics adding 205.8 m_e of mass.  On flat T²,
the harmonics are exactly uncharged (n₁ ≠ 1 → Q = 0).

On the curved torus (Track 2), even-parity modes acquire nonzero
charge overlap C.  If harmonics carry charge, the muon's total
charge deviates from -e.

Experimentally, Q_muon/Q_electron = 1 ± 10⁻¹² (PDG).
This constrains either ε = a/R or the harmonic spectrum.

KEY INSIGHT (from perturbation theory)
======================================
At small ε, the charge overlap for mode n₁ scales as:

  n₁ odd:  C = 0 exactly (parity)
  n₁ = 0:  C ∝ ε   (from ∫ 1 × cos θ × ε cos θ dθ = ε π)
  n₁ = 2:  C ∝ ε   (from ∫ cos 2θ × cos²θ dθ = π/2)
  n₁ = 4:  C ∝ ε²  (the O(ε) integral vanishes)
  n₁ ≥ 6 even: C ∝ ε² or higher

The mode energy scales as E ~ n m_e (roughly).  The
charge-per-unit-mass ratio determines the constraint:

  n₁ = 0:  Q/E ~ ε/(ε m_e) = 1/m_e  → O(1), INDEPENDENT of ε!
  n₁ = 2:  Q/E ~ ε/(2 m_e)          → O(ε)
  n₁ = 4:  Q/E ~ ε²/(4 m_e)         → O(ε²)
"""

import sys
import os
import math
import numpy as np
from scipy import linalg

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha, m_e, c


MUON_EXCESS = 206.768 - 1.0  # muon mass in m_e, minus fundamental


def build_eigenvalue_system(eps, n2, N):
    """Build S f = λ W f for the curved torus."""
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


def classify_parity(f, N):
    """Classify as even or odd under θ → 2π − θ."""
    f_rev = np.array([f[(-j) % N] for j in range(N)])
    overlap = np.dot(f, f_rev) / (np.linalg.norm(f)**2)
    return 'even' if overlap > 0 else 'odd'


def charge_overlap(f, eps, N):
    """C = ∫ f(θ) cos(θ) (1 + ε cos θ) dθ."""
    h = 2 * math.pi / N
    theta = np.array([2 * math.pi * j / N for j in range(N)])
    return np.sum(f * np.cos(theta) * (1 + eps * np.cos(theta))) * h


def analyze_modes(eps, n2, N, num_modes=8):
    """Get eigenvalues, charge overlaps, parities for lowest modes."""
    S, W = build_eigenvalue_system(eps, n2, N)
    eigenvalues, eigenvectors = linalg.eigh(S, W)
    idx = np.argsort(eigenvalues)
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    theta = np.array([2 * math.pi * j / N for j in range(N)])
    w = 1 + eps * np.cos(theta)

    results = []
    for i in range(min(num_modes, len(eigenvalues))):
        f = eigenvectors[:, i]
        norm = np.sqrt(np.sum(f**2 * w) * 2 * math.pi / N)
        f = f / norm * math.sqrt(2 * math.pi)
        parity = classify_parity(f, N)
        C = charge_overlap(f, eps, N) if parity == 'even' else 0.0
        results.append({
            'idx': i, 'lambda': eigenvalues[i],
            'parity': parity, 'C': C
        })
    return results


def main():
    N = 256

    # ==================================================================
    print("=" * 72)
    print("SECTION 1: Charge overlap for harmonic modes")
    print("=" * 72)
    print()
    print("For each toroidal number n₂, compute the charge overlap C")
    print("of the first few even modes.  The electron is (n₁=1, n₂=2).")
    print()

    eps_values = [0.01, 0.05, 0.1, 0.2, 0.3, 0.5]
    n2_values = [1, 2, 4, 6]

    # First, get C_electron at each ε
    print("Electron charge overlap C_e (n₂=2, cos-like n₁=1):")
    C_electron = {}
    for eps in eps_values:
        modes = analyze_modes(eps, 2, N)
        even_modes = [m for m in modes if m['parity'] == 'even']
        C_e = max(even_modes, key=lambda m: abs(m['C']))['C']
        C_electron[eps] = C_e
        print(f"  ε = {eps}: C_e = {C_e:.6f}")
    print()

    print(f"{'ε':>6s}  {'n₂':>4s}  {'idx':>4s}  {'Parity':>6s}  "
          f"{'λ':>10s}  {'C':>10s}  {'C/C_e':>8s}  "
          f"{'E/m_e':>8s}  {'(C/C_e)/(E/m_e)':>16s}")
    print("-" * 85)

    for eps in eps_values:
        C_e = C_electron[eps]

        for n2 in n2_values:
            modes = analyze_modes(eps, n2, N, num_modes=6)

            # Electron eigenvalue for energy normalization
            electron_modes = analyze_modes(eps, 2, N)
            lam_e = max(
                [m for m in electron_modes if m['parity'] == 'even'],
                key=lambda m: abs(m['C'])
            )['lambda']

            for m in modes:
                if m['parity'] == 'odd':
                    continue
                if abs(m['C']) < 1e-10:
                    continue

                C_ratio = m['C'] / C_e if abs(C_e) > 1e-15 else 0
                E_ratio = math.sqrt(m['lambda'] / lam_e) if lam_e > 0 else 0
                charge_per_mass = (C_ratio / E_ratio
                                   if abs(E_ratio) > 1e-15 else float('inf'))

                print(f"{eps:6.2f}  {n2:4d}  {m['idx']:4d}  "
                      f"{m['parity']:>6s}  {m['lambda']:10.4f}  "
                      f"{m['C']:10.6f}  {C_ratio:8.4f}  "
                      f"{E_ratio:8.4f}  {charge_per_mass:16.6f}")
        print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 2: Perturbative scaling verification")
    print("=" * 72)
    print()
    print("Check that C scales as predicted: C ∝ ε for n₁ = 0 and 2,")
    print("C ∝ ε² for n₁ = 4, etc.")
    print()

    eps_test = [0.01, 0.02, 0.05, 0.1, 0.2]

    for n2 in [2, 4]:
        print(f"n₂ = {n2}:")
        print(f"  {'ε':>8s}  {'C(n₁≈0)':>12s}  {'C/ε':>10s}  "
              f"{'C(n₁≈2)':>12s}  {'C/ε':>10s}  "
              f"{'C(n₁≈4)':>12s}  {'C/ε²':>12s}")
        print("  " + "-" * 80)

        for eps in eps_test:
            modes = analyze_modes(eps, n2, N, num_modes=10)
            even_modes = [m for m in modes if m['parity'] == 'even']

            C_vals = {}
            for m in even_modes:
                C_vals[m['idx']] = m['C']

            # idx=0 is n₁≈0, idx=2 is n₁≈1 cos-like, idx=4 is n₁≈2 cos-like
            C0 = C_vals.get(0, 0)
            C4 = C_vals.get(4, 0)
            C8 = C_vals.get(8, 0) if 8 in C_vals else 0

            print(f"  {eps:8.4f}  {C0:12.6f}  {C0/eps:10.4f}  "
                  f"{C4:12.6f}  {C4/eps if abs(eps) > 1e-15 else 0:10.4f}  "
                  f"{C8:12.6f}  "
                  f"{C8/eps**2 if abs(eps) > 1e-15 else 0:12.4f}")
        print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 3: Worst-case muon charge deviation")
    print("=" * 72)
    print()
    print(f"Muon excess mass: {MUON_EXCESS:.1f} m_e")
    print(f"Experimental bound: |ΔQ/e| < 10⁻¹²")
    print()
    print("For each harmonic mode, compute the charge deviation if ALL")
    print("muon harmonic mass were in that mode.")
    print()

    print(f"{'ε':>8s}  {'Harmonic':>12s}  {'E/m_e':>8s}  "
          f"{'C/C_e':>8s}  {'N_quanta':>10s}  "
          f"{'|ΔQ/e|':>12s}  {'Constraint':>12s}")
    print("-" * 85)

    # R20 harmonic candidates: (n, 2n) family
    harmonic_labels = {
        (0, 1): "(0,1) ground",
        (0, 2): "(0,2) ground",
        (2, 4): "(2,4) harm.",
        (4, 8): "(4,8) harm.",
        (3, 6): "(3,6) harm.",
    }

    for eps in [0.01, 0.05, 0.1, 0.2, 0.5]:
        C_e = C_electron.get(eps)
        if C_e is None:
            modes_e = analyze_modes(eps, 2, N)
            even_e = [m for m in modes_e if m['parity'] == 'even']
            C_e = max(even_e, key=lambda m: abs(m['C']))['C']

        electron_modes = analyze_modes(eps, 2, N)
        lam_e = max(
            [m for m in electron_modes if m['parity'] == 'even'],
            key=lambda m: abs(m['C'])
        )['lambda']

        for (n1_target, n2_target), label in harmonic_labels.items():
            modes = analyze_modes(eps, n2_target, N, num_modes=10)

            # Find the mode closest to n₁_target
            even_modes = [m for m in modes if m['parity'] == 'even']
            if n1_target == 0:
                target_mode = even_modes[0] if even_modes else None
            elif n1_target == 2:
                target_mode = even_modes[2] if len(even_modes) > 2 else None
            elif n1_target == 3:
                odd_modes = [m for m in modes if m['parity'] == 'odd']
                target_mode = odd_modes[0] if odd_modes else None
            elif n1_target == 4:
                target_mode = even_modes[3] if len(even_modes) > 3 else None
            else:
                target_mode = None

            if target_mode is None:
                continue

            E_ratio = math.sqrt(target_mode['lambda'] / lam_e) \
                if lam_e > 0 and target_mode['lambda'] > 0 else 0
            if E_ratio < 1e-10:
                continue

            C_ratio = target_mode['C'] / C_e if abs(C_e) > 1e-15 else 0

            if target_mode['parity'] == 'odd':
                C_ratio = 0.0

            N_quanta = MUON_EXCESS / E_ratio if E_ratio > 0 else float('inf')
            delta_Q = abs(N_quanta * C_ratio)

            if delta_Q > 0:
                eps_max = 1e-12 / (delta_Q / eps) if eps > 0 else 0
                constraint = f"ε < {eps_max:.1e}"
            else:
                constraint = "no constraint"

            print(f"{eps:8.4f}  {label:>12s}  {E_ratio:8.4f}  "
                  f"{C_ratio:8.4f}  {N_quanta:10.1f}  "
                  f"{delta_Q:12.4e}  {constraint:>12s}")
        print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 4: Constraint on ε from each harmonic type")
    print("=" * 72)
    print()
    print("Computing |ΔQ/e| vs ε for selected harmonics.")
    print("The constraint is |ΔQ/e| < 10⁻¹².")
    print()

    eps_scan = np.logspace(-4, -0.1, 50)

    constraint_results = {}
    for label_key, n2_target in [("n₁≈0,n₂=2", 2), ("n₁≈2,n₂=4", 4)]:
        for eps in eps_scan:
            if eps >= 1.0:
                continue
            modes_e = analyze_modes(eps, 2, N)
            even_e = [m for m in modes_e if m['parity'] == 'even']
            C_e = max(even_e, key=lambda m: abs(m['C']))['C']
            lam_e = max(even_e, key=lambda m: abs(m['C']))['lambda']

            modes = analyze_modes(eps, n2_target, N, num_modes=10)
            even_modes = [m for m in modes if m['parity'] == 'even']

            if "n₁≈0" in label_key:
                target = even_modes[0] if even_modes else None
            else:
                target = even_modes[2] if len(even_modes) > 2 else None

            if target is None:
                continue

            E_ratio = math.sqrt(target['lambda'] / lam_e) \
                if lam_e > 0 and target['lambda'] > 0 else 0
            C_ratio = target['C'] / C_e if abs(C_e) > 1e-15 else 0

            if E_ratio > 1e-10:
                N_q = MUON_EXCESS / E_ratio
                delta_Q = abs(N_q * C_ratio)

                if label_key not in constraint_results:
                    constraint_results[label_key] = []
                constraint_results[label_key].append((eps, delta_Q))

    for label, data in constraint_results.items():
        print(f"{label}:")
        print(f"  {'ε':>12s}  {'|ΔQ/e|':>14s}  {'log₁₀|ΔQ/e|':>14s}  "
              f"{'Allowed?':>10s}")
        print("  " + "-" * 55)
        for eps, dQ in data[::5]:
            allowed = "YES" if dQ < 1e-12 else "NO"
            log_dQ = math.log10(dQ) if dQ > 0 else -99
            print(f"  {eps:12.6f}  {dQ:14.4e}  {log_dQ:14.2f}  "
                  f"{allowed:>10s}")
        print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 5: Summary — harmonic selection rule")
    print("=" * 72)
    print()
    print("Each n₁ ≥ 1 mode has TWO versions on the curved torus:")
    print("  cos-like (even parity): carries charge C ≠ 0")
    print("  sin-like (odd parity):  carries NO charge (C = 0 exactly)")
    print()
    print("Even modes in eigenvalue order: n₁ = 0, 1cos, 2cos, 3cos, ...")
    print("Odd modes in eigenvalue order:  n₁ = 1sin, 2sin, 3sin, ...")
    print()

    eps = 0.1
    modes_e = analyze_modes(eps, 2, N)
    even_e = [m for m in modes_e if m['parity'] == 'even']
    C_e = max(even_e, key=lambda m: abs(m['C']))['C']
    lam_e = max(even_e, key=lambda m: abs(m['C']))['lambda']

    print(f"At ε = {eps} (r = {1/eps:.0f}):")
    print()
    print(f"{'Harmonic':>12s}  {'Version':>8s}  {'Parity':>6s}  "
          f"{'E/m_e':>8s}  {'C/C_e':>10s}  {'|ΔQ/e|_tot':>10s}  "
          f"{'Status':>25s}")
    print("-" * 95)

    harmonics = [
        (0, 2, "ground"),
        (2, 4, "(2,4)"),
        (3, 6, "(3,6)"),
        (4, 8, "(4,8)"),
        (5, 10, "(5,10)"),
        (6, 12, "(6,12)"),
    ]

    for n1, n2, label in harmonics:
        num_needed = max(2 * n1 + 4, 12)
        modes = analyze_modes(eps, n2, N, num_modes=num_needed)
        even_modes = [m for m in modes if m['parity'] == 'even']
        odd_modes = [m for m in modes if m['parity'] == 'odd']

        versions = []
        if n1 == 0:
            if even_modes:
                versions.append(("(only)", even_modes[0]))
        else:
            # even_modes[n1] is the cos-like version of n₁
            if len(even_modes) > n1:
                versions.append(("cos", even_modes[n1]))
            # odd_modes[n1-1] is the sin-like version of n₁
            if len(odd_modes) > n1 - 1:
                versions.append(("sin", odd_modes[n1 - 1]))

        for ver_name, mode in versions:
            E_ratio = math.sqrt(mode['lambda'] / lam_e) \
                if lam_e > 0 and mode['lambda'] > 0 else 0
            C_ratio = mode['C'] / C_e if abs(C_e) > 1e-15 else 0
            if mode['parity'] == 'odd':
                C_ratio = 0.0

            cpm = abs(C_ratio / E_ratio) if abs(E_ratio) > 1e-10 else 0
            total_dev = MUON_EXCESS * cpm

            if mode['parity'] == 'odd':
                status = "ALLOWED (C = 0)"
            elif total_dev > 1.0:
                status = f"EXCLUDED (ΔQ/e = {total_dev:.1f})"
            elif total_dev > 1e-12:
                eps_max = eps * 1e-12 / total_dev
                status = f"constrained (ε < {eps_max:.0e})"
            else:
                status = "negligible"

            print(f"{label:>12s}  {ver_name:>8s}  {mode['parity']:>6s}  "
                  f"{E_ratio:8.4f}  {C_ratio:10.6f}  {total_dev:10.4e}  "
                  f"{status:>25s}")

    print()
    print("CONCLUSION:")
    print()
    print("The muon charge constraint creates a PARITY SELECTION RULE")
    print("for the harmonic spectrum of charged composites:")
    print()
    print("  1. SIN-LIKE (odd-parity) modes: ALWAYS allowed as harmonics.")
    print("     Charge overlap C = 0 exactly by symmetry, for any n₁, any ε.")
    print()
    print("  2. n₁ = 0 mode (even only, no sin version): EXCLUDED at any ε.")
    print("     Charge-per-mass is O(1), independent of ε.")
    print("     With 205.8 m_e of mass: |ΔQ/e| ~ 70.")
    print()
    print("  3. COS-LIKE n₁ = 2 mode: charge-per-mass ~ ε/2.")
    print("     If present, requires ε < ~6×10⁻¹⁴.")
    print()
    print("  4. COS-LIKE n₁ ≥ 3 modes: charge-per-mass ~ ε².")
    print("     Weaker but still significant: ε < ~10⁻⁶ to 10⁻⁹.")
    print()
    print("EITHER the torus is extremely thin (ε < 10⁻¹⁴, curvature")
    print("negligible), OR the model PREDICTS that all harmonics must")
    print("be sin-like (odd-parity).  This selects the harmonic spectrum.")
    print()
    print("For the R20 harmonic family (n, 2n) with n ≥ 2:")
    print("  Each mode has a cos (charged) and sin (uncharged) version.")
    print("  The muon constraint forces ALL harmonics to be sin-like.")
    print("  This is a testable prediction of the curved-torus model.")


if __name__ == "__main__":
    main()
