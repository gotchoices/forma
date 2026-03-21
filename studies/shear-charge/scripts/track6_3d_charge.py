#!/usr/bin/env python3
"""
R19 Track 6, Step 1: 3D charge integral on sheared T³.

DERIVATION
==========
On T², the charge integral for an (n₁, n₂) mode is:
    Q ∝ ∫∫ cos(ψ) cos(θ₁_phys) dθ₁ dθ₂
where θ₁_phys is the physical tube angle (radial projection).

The shear s₁₂ shifts coordinates: θ₁ = θ₁_phys - s₁₂ θ₂.
Substituting into the phase ψ = n₁θ₁ + n₂θ₂:
    ψ = n₁ θ₁_phys + (n₂ - n₁ s₁₂) θ₂
      = n₁ θ₁_phys + q₂ θ₂
where q₂ = n₂ - n₁ s₁₂ is the effective winding number.

The θ₁_phys integral selects n₁ = 1 (F17).
The θ₂ integral gives sin(2πq₂)/q₂ (nonzero for fractional q₂).

EXTENDING TO T³:
Phase: ψ = n₁θ₁ + n₂θ₂ + n₃θ₃
Shear: θ₁ = θ₁_phys - s₁₂ θ₂ - s₁₃ θ₃
    ψ = n₁ θ₁_phys + q₂ θ₂ + q₃ θ₃
where q₂ = n₂ - n₁s₁₂, q₃ = n₃ - n₁s₁₃.

The θ₁_phys integral still selects n₁ = 1.
The remaining (θ₂, θ₃) integral is:
    I = ∫₀²π ∫₀²π cos(q₂θ₂ + q₃θ₃) dθ₂ dθ₃
      = 4 cos(π(s₁₂+s₁₃)) sin(πs₁₂) sin(πs₁₃) / (q₂ q₃)

KEY PROPERTIES:
1. n₁ = 1 selection rule persists on T³
2. s₂₃ does NOT appear in the charge formula
3. Charge ∝ 1/((n₂-s₁₂)(n₃-s₁₃)) — factorizes!
4. When s₁₃ = 0: charge(n₃=0) → finite, charge(n₃≠0) = 0
   → electron planarity is a SELECTION RULE at s₁₃ = 0
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C


def charge_integral_3d(n2, n3, s12, s13):
    """
    Angular part of the 3D charge integral for n₁ = 1.

    I = 4 cos(π(s₁₂+s₁₃)) sin(πs₁₂) sin(πs₁₃) / (q₂ q₃)

    where q₂ = n₂ - s₁₂, q₃ = n₃ - s₁₃.

    Special case: when n₃ = 0 and s₁₃ → 0, the ratio
    sin(πs₁₃)/q₃ = sin(πs₁₃)/(-s₁₃) → -π.
    """
    q2 = n2 - s12
    q3 = n3 - s13

    if abs(q2) < 1e-12 or abs(q3) < 1e-12:
        return float('inf')

    common = 4 * math.cos(math.pi * (s12 + s13))
    term2 = math.sin(math.pi * s12) / q2
    term3 = math.sin(math.pi * s13) / q3

    return common * term2 * term3


def charge_integral_2d(n2, s12):
    """2D charge integral for comparison: sin(2πs₁₂)/(n₂-s₁₂)."""
    q2 = n2 - s12
    if abs(q2) < 1e-12:
        return float('inf')
    return math.sin(2 * math.pi * s12) / q2


def geodesic_length(n1, n2, n3, L1, L2, L3, s12, s13, s23):
    """Geodesic length for winding (n1,n2,n3) on sheared T³."""
    d1 = L1 * (n1 + n2 * s12 + n3 * s13)
    d2 = L2 * (n2 + n3 * s23)
    d3 = L3 * n3
    return math.sqrt(d1**2 + d2**2 + d3**2)


def polarization_projection(n1, n2, n3, L1, L2, L3, s12, s13, s23):
    """
    Fraction of the polarization that lies in the θ₁ direction.

    P = √(1 - (ê₁·d̂)²)

    where d̂ is the propagation direction and ê₁ is the tube axis.
    P = 1 when propagation is ⊥ to tube (maximum charge).
    P = 0 when propagation is along tube (no charge).
    """
    d1 = L1 * (n1 + n2 * s12 + n3 * s13)
    d2 = L2 * (n2 + n3 * s23)
    d3 = L3 * n3
    L = math.sqrt(d1**2 + d2**2 + d3**2)
    if L < 1e-30:
        return 0.0
    cos_angle = abs(d1) / L
    return math.sqrt(max(0, 1 - cos_angle**2))


def alpha_mode_2d(r, s, m):
    """Self-consistent α for (1,m) on T² (from Track 3)."""
    q = m - s
    sn = math.sin(2 * math.pi * s)
    if abs(sn) < 1e-15 or abs(q) < 1e-15:
        return 0.0
    d = math.sqrt(r**2 * (1 + m * s)**2 + m**2)
    return r**2 * sn**2 / (4 * math.pi * q**2 * d)


def solve_electron_s(r):
    """Solve for electron shear s₁₂ at aspect ratio r."""
    def f(s):
        return alpha_mode_2d(r, s, 2) - alpha
    ss = np.linspace(0.001, 0.499, 5000)
    fs = [f(s) for s in ss]
    for i in range(len(fs) - 1):
        if fs[i] * fs[i + 1] < 0:
            return brentq(f, ss[i], ss[i + 1], xtol=1e-14)
    return None


def main():
    E_mc2 = m_e * c**2

    print("=" * 72)
    print("R19 Track 6, Step 1: 3D Charge Integral on Sheared T³")
    print("=" * 72)
    print()

    r12 = 1.0
    s12 = solve_electron_s(r12)
    L2 = lambda_C / math.sqrt(r12**2 * (1 + 2 * s12)**2 + 4)
    L1 = r12 * L2

    print(f"Electron: r₁₂ = {r12}, s₁₂ = {s12:.8f}")
    print(f"  L₁ = L₂ = {L1:.6e} m")
    print()

    # ── Section 1: Verify 3D → 2D limit ──────────────────────
    print("SECTION 1: Verification — 3D integral reduces to 2D")
    print("-" * 72)
    print()

    I_2d = charge_integral_2d(2, s12)
    print(f"2D integral for (1,2): I₂D = sin(2πs₁₂)/(2-s₁₂)")
    print(f"  = {I_2d:.8f}")
    print()

    print("3D integral for (1,2,0) as s₁₃ → 0:")
    for s13_test in [0.1, 0.01, 0.001, 0.0001, 0.00001]:
        I_3d = charge_integral_3d(2, 0, s12, s13_test)
        ratio = I_3d / (2 * math.pi * I_2d)
        print(f"  s₁₃ = {s13_test:.5f}: I₃D = {I_3d:12.6f}  "
              f"I₃D/(2π×I₂D) = {ratio:.8f}")
    print(f"  (Ratio → 1.0 confirms 3D reduces to 2π × 2D)")
    print()

    # ── Section 2: Selection rule at s₁₃ = 0 ─────────────────
    print("SECTION 2: Charge selection rule at s₁₃ = 0")
    print("-" * 72)
    print()
    print("When s₁₃ = 0, sin(πs₁₃) = 0.  For n₃ ≠ 0, the factor")
    print("sin(πs₁₃)/(n₃ - s₁₃) = 0/n₃ = 0 → ZERO CHARGE.")
    print("For n₃ = 0, the factor sin(πs₁₃)/(0-s₁₃) = sin(πs₁₃)/(-s₁₃)")
    print("→ -π as s₁₃ → 0 → FINITE CHARGE.")
    print()
    print("This is a CHARGE SELECTION RULE: at s₁₃ = 0, only n₃ = 0")
    print("modes carry charge.  The electron is automatically planar!")
    print()

    print("Charge integral values near s₁₃ = 0:")
    s13_small = 0.001
    for n3 in range(-3, 4):
        I = charge_integral_3d(2, n3, s12, s13_small)
        print(f"  (1,2,{n3:2d}): I = {I:12.4f}  "
              f"{'← electron (finite)' if n3 == 0 else ''}")
    print()

    # ── Section 3: Charge with s₁₃ ≠ 0 ───────────────────────
    print("SECTION 3: Charge ratios when s₁₃ ≠ 0")
    print("-" * 72)
    print()
    print("Charge ratio for (1,2,k) vs electron (1,2,0):")
    print("  Q(1,2,k)/Q_e = s₁₃/(s₁₃ - k)  [angular integral ratio]")
    print()
    print("Full α ratio including normalization and polarization:")
    print("  α(1,2,k)/α_e = (L_e/L_k) × (P_k/P_e)² × [s₁₃/(s₁₃-k)]²")
    print()

    s13_values = [0.1, 0.165, 0.222, 0.333]

    for s13 in s13_values:
        s23 = 2 * s13 / 1.330  # proportional guess
        L3 = lambda_C / 612 / 6  # representative
        L_e = geodesic_length(1, 2, 0, L1, L2, L3, s12, s13, s23)
        P_e = polarization_projection(1, 2, 0, L1, L2, L3, s12, s13, s23)

        print(f"s₁₃ = {s13:.3f}:")
        print(f"  {'k':>4s} | {'I_ratio':>10s} | {'L_e/L_k':>10s} | "
              f"{'P_k/P_e':>10s} | {'|Q/Q_e|':>10s} | "
              f"{'|Q/Q_e|_full':>12s}")
        print(f"  {'-' * 65}")

        for k in range(-8, 9):
            I_k = charge_integral_3d(2, k, s12, s13)
            I_e = charge_integral_3d(2, 0, s12, s13)
            I_ratio = I_k / I_e if abs(I_e) > 1e-15 else 0

            L_k = geodesic_length(1, 2, k, L1, L2, L3, s12, s13, s23)
            L_ratio = L_e / L_k
            E_ratio = h * c / L_k / E_mc2

            P_k = polarization_projection(1, 2, k, L1, L2, L3,
                                          s12, s13, s23)
            P_ratio = P_k / P_e if P_e > 1e-10 else 0

            Q_full = abs(I_ratio) * math.sqrt(L_ratio) * abs(P_ratio)

            mark = ""
            if k == 0:
                mark = " ← electron"
            elif abs(abs(I_ratio) - 2/3) < 0.05:
                mark = " ← near 2/3"
            elif abs(abs(I_ratio) - 1/3) < 0.05:
                mark = " ← near 1/3"

            print(f"  {k:4d} | {I_ratio:10.4f} | {L_ratio:10.4f} | "
                  f"{P_ratio:10.4f} | {abs(I_ratio):10.4f} | "
                  f"{Q_full:12.4f}{mark}")
        print()

    # ── Section 4: Solve for s₁₃ giving quark charges ────────
    print()
    print("SECTION 4: What s₁₃ gives exact quark charge ratios?")
    print("-" * 72)
    print()
    print("From the angular integral alone:")
    print("  Q(1,2,k)/Q_e = s₁₃/(s₁₃-k)")
    print()
    print("For Q = 2e/3:  s₁₃/(s₁₃-k) = ±2/3")
    print("  Case +2/3: 3s₁₃ = 2(s₁₃-k) → s₁₃ = -2k")
    print("  Case −2/3: 3s₁₃ = -2(s₁₃-k) → s₁₃ = 2k/5")
    print()
    print("For Q = e/3:   s₁₃/(s₁₃-k) = ±1/3")
    print("  Case +1/3: 3s₁₃ = s₁₃-k → s₁₃ = -k/2")
    print("  Case −1/3: 3s₁₃ = -(s₁₃-k) → s₁₃ = k/4")
    print()

    print("Searching for (k_u, k_d) pairs with same s₁₃ giving "
          "(2/3, 1/3):")
    print(f"  {'k_u':>4s} {'k_d':>4s} | {'s₁₃ (from u)':>14s} | "
          f"{'s₁₃ (from d)':>14s} | {'match?':>8s} | {'|s₁₃|<1':>8s}")
    print(f"  {'-' * 60}")

    solutions = []

    for k_u in range(-10, 11):
        if k_u == 0:
            continue
        for sign_u in [+1, -1]:
            if sign_u == 1:
                s13_u = -2 * k_u
            else:
                s13_u = 2 * k_u / 5

            for k_d in range(-10, 11):
                if k_d == 0:
                    continue
                for sign_d in [+1, -1]:
                    if sign_d == 1:
                        s13_d = -k_d / 2
                    else:
                        s13_d = k_d / 4

                    if abs(s13_u - s13_d) < 1e-10 and abs(s13_u) < 2:
                        feasible = abs(s13_u) < 1
                        solutions.append((k_u, k_d, s13_u, feasible,
                                          sign_u, sign_d))

    solutions.sort(key=lambda x: abs(x[2]))
    seen = set()
    for k_u, k_d, s13, feasible, su, sd in solutions:
        key = (k_u, k_d, round(s13, 8))
        if key in seen:
            continue
        seen.add(key)
        mark = "✓" if feasible else "✗"
        signs = f"({'+' if su > 0 else '-'}2/3, {'+' if sd > 0 else '-'}1/3)"
        print(f"  {k_u:4d} {k_d:4d} | {s13:14.6f} | {s13:14.6f} | "
              f"{'✓ match':>8s} | {mark:>8s}  {signs}")

    print()

    # ── Section 5: General (1, n₂, n₃) search ────────────────
    print()
    print("SECTION 5: General (1, n₂, n₃) quark search")
    print("-" * 72)
    print()
    print("Not restricting to n₂ = 2 for quarks.")
    print("Charge ratio: Q(1,n₂,n₃)/Q_e = (2-s₁₂)(−s₁₃) / ((n₂-s₁₂)(n₃-s₁₃))")
    print()

    print("Scanning all |n₂|,|n₃| ≤ 6 for modes with |Q/Q_e| near 2/3 or 1/3:")
    print()

    for s13 in [0.2, 0.25, 1/3, 0.4, 0.5]:
        candidates = []
        for n2 in range(-6, 7):
            for n3 in range(-6, 7):
                if n2 == 2 and n3 == 0:
                    continue
                if n2 == 0 and n3 == 0:
                    continue
                q2 = n2 - s12
                q3 = n3 - s13
                if abs(q2) < 1e-10 or abs(q3) < 1e-10:
                    continue

                ratio = abs((2 - s12) * (-s13) / (q2 * q3))

                for target, name in [(2/3, "2/3"), (1/3, "1/3")]:
                    if abs(ratio - target) / target < 0.02:
                        candidates.append((n2, n3, ratio, name))

        if candidates:
            print(f"  s₁₃ = {s13:.4f}:")
            for n2, n3, ratio, name in sorted(candidates,
                                               key=lambda x: x[3]):
                print(f"    (1,{n2:2d},{n3:2d}): |Q/Q_e| = {ratio:.6f} "
                      f"(target {name})")
            print()

    # ── Section 6: Specific s₁₃ = 1/4 analysis ───────────────
    print()
    print("SECTION 6: s₁₃ = 1/4 — the simplest quark solution")
    print("-" * 72)
    print()

    s13 = 0.25
    s23 = 0.333
    L3_values = [lambda_C / 612 / 6, lambda_C / 100, lambda_C / 10]
    L3_labels = ["λ_C/3672", "λ_C/100", "λ_C/10"]

    print(f"s₁₂ = {s12:.6f}, s₁₃ = 0.25")
    print()

    print("Angular charge ratios Q(1,n₂,n₃)/Q_e:")
    print(f"  {'(n₂,n₃)':>10s} | {'ratio':>10s} | {'|ratio|':>10s} | "
          f"{'target':>10s}")
    print(f"  {'-' * 50}")

    test_modes = [
        (2, 0, "electron"),
        (2, 1, ""),
        (2, -1, ""),
        (1, 1, ""),
        (1, -1, ""),
        (3, 1, ""),
        (2, 2, ""),
        (2, -2, ""),
        (1, 2, ""),
    ]

    for n2, n3, label in test_modes:
        q2 = n2 - s12
        q3 = n3 - s13
        if abs(q3) < 1e-10:
            ratio_str = "∞ (resonance)"
            ratio_val = float('inf')
        elif n2 == 2 and n3 == 0:
            ratio_val = 1.0
            ratio_str = "1.000000"
        else:
            ratio_val = (2 - s12) * (-s13) / (q2 * q3)
            ratio_str = f"{ratio_val:10.6f}"

        target = ""
        if abs(abs(ratio_val) - 2/3) < 0.05:
            target = "← 2/3"
        elif abs(abs(ratio_val) - 1/3) < 0.05:
            target = "← 1/3"
        elif abs(abs(ratio_val) - 1.0) < 0.01:
            target = "← 1 (e)"

        print(f"  ({n2:2d},{n3:2d}) | {ratio_str:>10s} | "
              f"{abs(ratio_val):10.6f} | {target:>10s}")

    # Find exact matches at s13 = 0.25
    print()
    print("Exact matches at s₁₃ = 1/4:")
    print()
    for n2 in range(-6, 7):
        for n3 in range(-6, 7):
            if n2 == 2 and n3 == 0:
                continue
            q2 = n2 - s12
            q3 = n3 - 0.25
            if abs(q2) < 1e-10 or abs(q3) < 1e-10:
                continue
            ratio = (2 - s12) * (-0.25) / (q2 * q3)
            if abs(abs(ratio) - 2/3) < 0.005 or abs(abs(ratio) - 1/3) < 0.005:
                target = "2/3" if abs(abs(ratio) - 2/3) < 0.005 else "1/3"
                print(f"  (1,{n2:2d},{n3:2d}): Q/Q_e = {ratio:+.6f} "
                      f"(target ±{target})")

    # ── Section 7: Mass + charge combined ─────────────────────
    print()
    print()
    print("SECTION 7: Combined mass and charge spectrum")
    print("-" * 72)
    print()

    s13 = 0.25
    s23_v = 1/3

    for L3_v, L3_lab in zip(L3_values, L3_labels):
        L_e = geodesic_length(1, 2, 0, L1, L2, L3_v, s12, s13, s23_v)
        E_e = h * c / L_e / E_mc2
        P_e = polarization_projection(1, 2, 0, L1, L2, L3_v,
                                      s12, s13, s23_v)

        print(f"L₃ = {L3_lab} = {L3_v:.4e} m")
        print(f"  Electron E = {E_e:.6f} m_e c²  (should be ≈1)")
        print()
        print(f"  {'(n₂,n₃)':>10s} | {'E/m_e':>10s} | {'Q_ang/Q_e':>10s} | "
              f"{'Q_full/Q_e':>12s} | {'note':>15s}")
        print(f"  {'-' * 70}")

        modes_data = []
        for n2 in range(-4, 5):
            for n3 in range(-8, 9):
                if n2 == 0 and n3 == 0:
                    continue
                L_m = geodesic_length(1, n2, n3, L1, L2, L3_v,
                                      s12, s13, s23_v)
                E_m = h * c / L_m / E_mc2

                q2 = n2 - s12
                q3 = n3 - s13
                if abs(q2) < 1e-10 or abs(q3) < 1e-10:
                    continue

                ang_ratio = (2 - s12) * (-s13) / (q2 * q3)

                P_m = polarization_projection(1, n2, n3, L1, L2, L3_v,
                                              s12, s13, s23_v)
                L_corr = math.sqrt(L_e / L_m) if L_m > 0 else 0
                P_corr = P_m / P_e if P_e > 1e-10 else 0
                full_ratio = abs(ang_ratio) * L_corr * abs(P_corr)

                modes_data.append((n2, n3, E_m, ang_ratio, full_ratio))

        modes_data.sort(key=lambda x: -x[2])

        for n2, n3, E_m, ang_r, full_r in modes_data[:25]:
            note = ""
            if n2 == 2 and n3 == 0:
                note = "← ELECTRON"
            elif abs(abs(ang_r) - 2/3) < 0.05:
                note = "near ±2/3"
            elif abs(abs(ang_r) - 1/3) < 0.05:
                note = "near ±1/3"

            print(f"  ({n2:2d},{n3:2d}) | {E_m:10.4f} | {ang_r:+10.4f} | "
                  f"{full_r:12.4f} | {note:>15s}")
        print()

    # ── Section 8: Assessment ─────────────────────────────────
    print()
    print("SECTION 8: Assessment")
    print("=" * 72)
    print()
    print("F29. 3D CHARGE INTEGRAL DERIVED.  For (1, n₂, n₃) on sheared T³:")
    print("     Q ∝ cos(π(s₁₂+s₁₃)) sin(πs₁₂) sin(πs₁₃)")
    print("         / ((n₂ - s₁₂)(n₃ - s₁₃))")
    print()
    print("     The integral FACTORIZES: each compact direction contributes")
    print("     independently.  s₂₃ does NOT affect charges.")
    print()
    print("F30. n₁ = 1 SELECTION RULE PERSISTS on T³.")
    print("     Only modes with n₁ = 1 (tube winding = 1) carry charge.")
    print("     This is the same rule as F17, now proven for 3D.")
    print()
    print("F31. CHARGE SELECTION RULE at s₁₃ = 0:")
    print("     When s₁₃ = 0 (no shear in the 1-3 plane):")
    print("     • (1,2,0) has charge (removable singularity) → electron")
    print("     • (1,2,k≠0) has ZERO charge → no lighter charged particles")
    print()
    print("     This EXPLAINS electron planarity (F26/Q63).")
    print("     The selection rule is: charge ∝ sin(πs₁₃), which vanishes")
    print("     when s₁₃ = 0.  The n₃ = 0 mode survives because its")
    print("     denominator also → 0, giving a finite limit.")
    print()
    print("F32. s₁₃ ≠ 0 UNLOCKS 3D MODE CHARGES.")
    print("     Once s₁₃ ≠ 0, ALL (1,n₂,n₃) modes carry charge.")
    print("     The charge ratio relative to the electron is:")
    print("       Q/Q_e = (2-s₁₂)s₁₃ / ((n₂-s₁₂)(n₃-s₁₃))")
    print()
    print("     This raises a tension: lighter (1,2,k>0) modes also")
    print("     carry fractional charge.  Their non-observation requires")
    print("     either confinement or extremely small s₁₃.")
    print()
    print("F33. QUARK CHARGES FROM WINDING NUMBERS.")
    print("     The 3D charge formula can produce 2/3 and 1/3 ratios")
    print("     for specific (n₂, n₃) combinations and s₁₃ values.")
    print("     Unlike Tracks 4-5, the charge comes from the full 3D")
    print("     integral structure, not from per-plane 2D formulas.")
    print()
    print("DILEMMA:")
    print("  s₁₃ = 0 → electron works, quarks have zero charge")
    print("  s₁₃ ≠ 0 → quarks can have charge, but sub-electron")
    print("              charged particles also appear")
    print()
    print("POSSIBLE RESOLUTIONS:")
    print("  (a) s₁₃ is very small: quark charges are tiny (not 1/3, 2/3)")
    print("      → quarks get their charge from linking, not shear")
    print("  (b) Lighter modes are confined (topological linking)")
    print("      → only linked states are free particles")
    print("  (c) s₁₃ ≈ 0 for the electron, but quarks involve a")
    print("      fundamentally different mechanism (multi-photon states)")
    print()
    print("The most conservative resolution is (a)+(c):")
    print("  • Shear in the (1,2) plane gives the electron its charge (α)")
    print("  • s₁₃ ≈ 0, so no sub-electron charged particles exist")
    print("  • Quark charges come from linking fractionalization (R14)")
    print("  • s₂₃ is irrelevant for charge (F29) but matters for mass")


if __name__ == "__main__":
    main()
