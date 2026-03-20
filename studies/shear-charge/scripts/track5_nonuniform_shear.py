#!/usr/bin/env python3
"""
R19 Track 5: Non-uniform shear on T³.

Track 4 showed uniform shear fails by factor of 2.
Track 5 allows independent shear per plane (s₁₂, s₁₃, s₂₃).

Strategy: for each r₁₂, the electron fixes s₁₂.  Then scan
r₂₃ and solve the quark shears analytically/numerically.
Check mass constraint (proton = 2u + d ≈ 1836 m_e).
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C


def alpha_mode(r, s, m):
    """α for (1,m) mode on a plane with aspect ratio r and shear s."""
    q = m - s
    if abs(q) < 1e-15:
        return float('inf')
    sn = math.sin(2 * math.pi * s)
    if abs(sn) < 1e-15:
        return 0.0
    d = math.sqrt(r**2 * (1 + m*s)**2 + m**2)
    return r**2 * sn**2 / (4 * math.pi * q**2 * d)


def solve_s(r, m, target_alpha):
    """Solve alpha_mode(r, s, m) = target_alpha for s ∈ (0,1)."""
    def f(s):
        return alpha_mode(r, s, m) - target_alpha

    # Fast scan
    N = 2000
    ss = np.linspace(0.002, 0.998, N)
    prev = f(ss[0])
    results = []
    for i in range(1, N):
        cur = f(ss[i])
        if prev * cur < 0:
            try:
                sol = brentq(f, ss[i-1], ss[i], xtol=1e-13)
                results.append(sol)
            except ValueError:
                pass
        prev = cur
    return results


def main():
    alpha_e = alpha
    alpha_u = alpha * 4 / 9
    alpha_d = alpha / 9
    m_e_mode = 2    # electron (1,2)
    m_q = -6        # quark (1,-6)

    print("=" * 72)
    print("R19 Track 5: Non-uniform Shear on T³")
    print("=" * 72)
    print()
    print("Electron (1,2) in (1,2) plane: r₁₂, s₁₂ → α")
    print("Up quark (1,−6) in (1,3) plane: r₁₃, s₁₃ → 4α/9")
    print("Down quark (1,−6) in (2,3) plane: r₂₃, s₂₃ → α/9")
    print("Consistency: r₁₃ = r₁₂ × r₂₃")
    print()

    # ── Section 1: Solve for a range of r₁₂ ──────────────────
    print("SECTION 1: Charge solutions across (r₁₂, r₂₃)")
    print("-" * 72)
    print()

    r12_list = [0.75, 1.0, 1.5, 2.0, 3.0]

    all_results = []

    for r12 in r12_list:
        sols12 = solve_s(r12, m_e_mode, alpha_e)
        if not sols12:
            print(f"r₁₂ = {r12:.2f}: no electron solution")
            continue
        s12 = sols12[0]

        L2 = lambda_C / math.sqrt(r12**2 * (1 + 2*s12)**2 + 4)
        L1 = r12 * L2

        print(f"r₁₂ = {r12:.2f}, s₁₂ = {s12:.6f}")
        print(f"  L₁ = {L1:.4e} m, L₂ = {L2:.4e} m")
        print()

        # Scan r₂₃ in selected values
        r23_candidates = np.concatenate([
            np.linspace(0.3, 5, 100),
            np.linspace(5, 50, 50)
        ])

        found = []
        for r23 in r23_candidates:
            # Down quark: solve s₂₃
            sols23 = solve_s(r23, m_q, alpha_d)
            if not sols23:
                continue
            s23 = sols23[0]

            # Up quark: r₁₃ = r₁₂ × r₂₃, solve s₁₃
            r13 = r12 * r23
            sols13 = solve_s(r13, m_q, alpha_u)
            if not sols13:
                continue
            s13 = sols13[0]

            L3 = L2 / r23

            # Quark geodesics
            L_d = math.sqrt(L2**2 * (1 + m_q*s23)**2 + m_q**2 * L3**2)
            L_u = math.sqrt(L1**2 * (1 + m_q*s13)**2 + m_q**2 * L3**2)

            E_d = h * c / L_d / (m_e * c**2)
            E_u = h * c / L_u / (m_e * c**2)
            E_p = 2 * E_u + E_d

            found.append((r23, s23, r13, s13, L3, E_u, E_d, E_p))
            all_results.append((r12, s12, r23, s23, r13, s13,
                                L1, L2, L3, E_u, E_d, E_p))

        if found:
            # Print a selection
            print(f"  {'r₂₃':>8s} | {'s₂₃':>8s} | {'r₁₃':>8s} | "
                  f"{'s₁₃':>8s} | {'L₃(fm)':>7s} | {'E_u':>7s} | "
                  f"{'E_d':>7s} | {'E_p':>8s} | {'E_p/1836':>8s}")
            print(f"  {'-'*82}")

            # Show subset: every 10th plus any near proton mass
            indices = list(range(0, len(found), max(1, len(found)//8)))
            near_proton = [i for i, f in enumerate(found)
                           if abs(f[7] - 1836.15) / 1836.15 < 0.1]
            indices = sorted(set(indices + near_proton))

            for i in indices:
                r23, s23, r13, s13, L3, E_u, E_d, E_p = found[i]
                marker = " ←" if abs(E_p - 1836.15)/1836.15 < 0.05 else ""
                print(f"  {r23:8.3f} | {s23:8.5f} | {r13:8.3f} | "
                      f"{s13:8.5f} | {L3*1e15:7.3f} | {E_u:7.1f} | "
                      f"{E_d:7.1f} | {E_p:8.1f} | {E_p/1836.15:8.4f}{marker}")
        print()

    # ── Section 2: Focus on proton-mass matches ───────────────
    print()
    print("SECTION 2: Proton mass matches")
    print("-" * 72)
    print()

    proton_matches = [(r[0], r[1], r[2], r[3], r[4], r[5],
                       r[6], r[7], r[8], r[9], r[10], r[11])
                      for r in all_results
                      if abs(r[11] - 1836.15) / 1836.15 < 0.10]

    if proton_matches:
        proton_matches.sort(key=lambda x: abs(x[11] - 1836.15))
        print(f"Solutions within 10% of proton mass (1836.15 m_e):")
        print()
        for pm in proton_matches[:10]:
            r12, s12, r23, s23, r13, s13, L1, L2, L3, E_u, E_d, E_p = pm
            err = (E_p - 1836.15) / 1836.15 * 100
            print(f"  r₁₂={r12:.3f}  s₁₂={s12:.5f}")
            print(f"  r₂₃={r23:.3f}  s₂₃={s23:.5f}  (down quark)")
            print(f"  r₁₃={r13:.3f}  s₁₃={s13:.5f}  (up quark)")
            print(f"  L₁={L1:.3e}  L₂={L2:.3e}  L₃={L3:.3e} m  "
                  f"({L3*1e15:.3f} fm)")
            print(f"  E_u={E_u:.1f}  E_d={E_d:.1f}  "
                  f"E_p=2E_u+E_d={E_p:.1f} m_e  (err={err:+.2f}%)")
            print(f"  Shear pattern: s₁₂/s₂₃={s12/s23:.4f}  "
                  f"s₁₂/s₁₃={s12/s13:.4f}  s₂₃/s₁₃={s23/s13:.4f}")
            print()
    else:
        print("No proton-mass matches found within 10%.")
        print()
        # Show the range of E_p we get
        if all_results:
            E_ps = [r[11] for r in all_results]
            print(f"E_p range: {min(E_ps):.1f} to {max(E_ps):.1f} m_e")
            print(f"(Target: 1836.15 m_e)")
            print()

            # Closest
            closest = min(all_results, key=lambda x: abs(x[11] - 1836.15))
            r12, s12, r23, s23, r13, s13, L1, L2, L3, E_u, E_d, E_p = closest
            err = (E_p - 1836.15) / 1836.15 * 100
            print(f"Closest match:")
            print(f"  r₁₂={r12:.3f}  s₁₂={s12:.5f}")
            print(f"  r₂₃={r23:.3f}  s₂₃={s23:.5f}")
            print(f"  r₁₃={r13:.3f}  s₁₃={s13:.5f}")
            print(f"  E_u={E_u:.1f}  E_d={E_d:.1f}  "
                  f"E_p={E_p:.1f} (err={err:+.1f}%)")

    # ── Section 3: Assessment ─────────────────────────────────
    print()
    print("SECTION 3: Assessment")
    print("=" * 72)
    print()
    print("With non-uniform shear (s₁₂ ≠ s₁₃ ≠ s₂₃), the three")
    print("charge equations + T³ consistency can always be satisfied.")
    print("The system has 5 parameters and 4 constraints, leaving")
    print("1 degree of freedom.")
    print()
    print("The mass constraint (proton = 2u + d) provides the 5th")
    print("equation, which could fully determine the geometry — or")
    print("reveal that no consistent solution exists.")
    print()

    if proton_matches:
        pm = proton_matches[0]
        r12, s12, r23, s23, r13, s13 = pm[:6]
        print("The system IS solvable.  The best solution has:")
        print(f"  Three distinct shear values: {s12:.5f}, {s13:.5f}, {s23:.5f}")
        if abs(s12 - s13) / s12 < 0.1 and abs(s12 - s23) / s12 < 0.1:
            print("  → Shears are approximately equal (near Track 4's assumption)")
        else:
            print("  → Shears are NOT equal (Track 4's assumption was wrong)")
    else:
        print("The (1,−6) quark model with non-uniform shear does NOT")
        print("produce the proton mass.  This suggests either:")
        print("  (a) The quark winding is not (1,−6)")
        print("  (b) The three quarks don't have equal energies")
        print("  (c) The charge formula needs modification (Track 6)")


if __name__ == "__main__":
    main()
