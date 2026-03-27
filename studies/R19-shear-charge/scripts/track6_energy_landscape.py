#!/usr/bin/env python3
"""
R19 Track 6, Step 0: T³ mode energy landscape.

Before deriving the 3D charge integral, map out the geodesic
lengths (masses) of various winding configurations on a sheared
T³ that hosts the electron as (1,2,0).

Key question (Q63): Why is the electron confined to a 2D plane?
Is (1,2,0) the lowest-energy spin-½ state, or must we invoke
a charge selection rule?

Results feed into Track 6 Steps 1-5.
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C


def geodesic_length_T3(n1, n2, n3, L1, L2, L3, s12, s13, s23):
    """
    Geodesic length for winding (n1, n2, n3) on a sheared T³.

    Lattice vectors (lower-triangular convention):
        v1 = (L1, 0, 0)
        v2 = (s12*L1, L2, 0)
        v3 = (s13*L1, s23*L2, L3)

    Displacement d = n1*v1 + n2*v2 + n3*v3:
        d1 = L1*(n1 + n2*s12 + n3*s13)
        d2 = L2*(n2 + n3*s23)
        d3 = L3*n3
    """
    d1 = L1 * (n1 + n2 * s12 + n3 * s13)
    d2 = L2 * (n2 + n3 * s23)
    d3 = L3 * n3
    return math.sqrt(d1**2 + d2**2 + d3**2)


def alpha_mode_2d(r, s, m):
    """α for (1,m) mode on a 2D plane (from Tracks 1-3)."""
    q = m - s
    sn = math.sin(2 * math.pi * s)
    if abs(sn) < 1e-15 or abs(q) < 1e-15:
        return 0.0
    d = math.sqrt(r**2 * (1 + m * s)**2 + m**2)
    return r**2 * sn**2 / (4 * math.pi * q**2 * d)


def solve_electron_s(r):
    """Solve for electron shear s at aspect ratio r."""
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
    print("R19 Track 6, Step 0: T³ Mode Energy Landscape")
    print("=" * 72)
    print()

    # ── Set up electron geometry ──────────────────────────────
    r12 = 1.0
    s12 = solve_electron_s(r12)

    L2 = lambda_C / math.sqrt(r12**2 * (1 + 2 * s12)**2 + 4)
    L1 = r12 * L2
    L_e = geodesic_length_T3(1, 2, 0, L1, L2, 1, s12, 0, 0)

    print("Electron reference: (1,2,0) in (1,2) plane")
    print(f"  r₁₂ = {r12:.2f}, s₁₂ = {s12:.8f}")
    print(f"  L₁ = {L1:.6e} m, L₂ = {L2:.6e} m")
    print(f"  L_e = {L_e:.6e} m  (λ_C = {lambda_C:.6e} m)")
    print(f"  E_e = m_e c² = {E_mc2:.6e} J = 0.511 MeV")
    print()

    # ── Section 1: Unsheared T³ ───────────────────────────────
    print("SECTION 1: (1,2,k) modes on UNSHEARED T³ (s₁₃ = s₂₃ = 0)")
    print("-" * 72)
    print()
    print("On an unsheared T³:")
    print("  L(1,2,k)² = L_e² + k²L₃²")
    print()
    print("Every k ≠ 0 mode has LONGER geodesic → LOWER energy")
    print("→ LIGHTER particle.  (E = hc/L)")
    print()

    L3_candidates = [0.1 * L1, 0.5 * L1, L1, 2 * L1]
    labels = ["0.1 L₁", "0.5 L₁", "L₁", "2 L₁"]

    header = f"{'k':>4s}"
    for lab in labels:
        header += f" | {'L₃=' + lab:>14s}"
    print(header)
    print("-" * (5 + 17 * len(labels)))

    for k in range(-4, 5):
        row = f"{k:4d}"
        for L3 in L3_candidates:
            L = geodesic_length_T3(1, 2, k, L1, L2, L3, s12, 0, 0)
            E = h * c / L
            mass_ratio = E / E_mc2
            row += f" | {mass_ratio:14.6f}"
        row += f"  {'← electron' if k == 0 else ''}"
        print(row)

    print()
    print("Values: E(1,2,k) / m_e c²  (mass in electron units).")
    print("All k ≠ 0 entries are < 1.000: LIGHTER than the electron.")
    print()
    print("PROBLEM: If these modes carry charge and have spin ½,")
    print("there should be charged fermions lighter than the electron.")
    print("None are observed.")
    print()
    print("RESOLUTION candidates:")
    print("  (a) 3D charge integral vanishes for k ≠ 0 → selection rule")
    print("  (b) Spin ½ requires n₃ = 0 (3D winding changes spin)")
    print("  (c) Shear in the 1-3 / 2-3 planes modifies energy ordering")
    print()

    # ── Section 2: Sheared T³ ─────────────────────────────────
    print()
    print("SECTION 2: Sheared T³ — can (1,2,k) become HEAVIER?")
    print("-" * 72)
    print()
    print("Geodesic with shear:")
    print("  L² = L₁²(1 + 2s₁₂ + ks₁₃)² + L₂²(2 + ks₂₃)² + k²L₃²")
    print()
    A = 1 + 2 * s12
    print(f"L₁ term cancels when: ks₁₃ = -{A:.4f}")
    print(f"L₂ term cancels when: ks₂₃ = -2")
    print(f"Both cancel → L ≈ |k|L₃  (can be MUCH shorter = heavier)")
    print()

    L3 = 0.5 * L1

    print(f"Scanning with L₃ = 0.5 L₁ = {L3:.4e} m")
    print()
    print(f"{'s₁₃':>8s} {'s₂₃':>8s} | {'k*':>4s} {'E*/m_e':>10s} | "\
          f"{'k_cancel':>10s}")
    print("-" * 55)

    for s13 in [0, 0.1, 0.165, 0.22, 0.33, 0.44, 0.5, 0.67]:
        for s23 in [0, 0.33, 0.5, 0.67]:
            best_k = 0
            best_E = 1.0
            for k in range(-20, 21):
                if k == 0:
                    continue
                L = geodesic_length_T3(1, 2, k, L1, L2, L3, s12, s13, s23)
                E = h * c / L / E_mc2
                if E > best_E:
                    best_E = E
                    best_k = k

            k_cancel = -A / s13 if abs(s13) > 1e-10 else float('inf')
            kc_str = f"{k_cancel:10.2f}" if abs(k_cancel) < 100 else \
                     f"{'∞':>10s}"

            if best_E > 1.05:
                print(f"{s13:8.3f} {s23:8.3f} | {best_k:4d} {best_E:10.4f} | "
                      f"{kc_str}")

    print()
    print("(Showing only rows where a mode heavier than 1.05 m_e exists)")
    print()

    # ── Section 3: Energy spectrum on uniform-shear T³ ────────
    print()
    print("SECTION 3: Full mode spectrum — uniform shear T³")
    print("-" * 72)
    print()

    s13 = s12
    s23 = s12
    L3 = L1

    print(f"T³ parameters: s₁₂ = s₁₃ = s₂₃ = {s12:.6f}")
    print(f"  L₁ = L₃ = {L1:.4e} m, L₂ = {L2:.4e} m")
    print()

    N = 6
    modes = []
    for n1 in range(-N, N + 1):
        for n2 in range(-N, N + 1):
            for n3 in range(-N, N + 1):
                if n1 == 0 and n2 == 0 and n3 == 0:
                    continue
                L = geodesic_length_T3(n1, n2, n3, L1, L2, L3,
                                       s12, s13, s23)
                E = h * c / L / E_mc2
                modes.append((n1, n2, n3, L, E))

    modes.sort(key=lambda x: -x[4])

    electron_E = None
    for n1, n2, n3, L, E in modes:
        if (n1, n2, n3) == (1, 2, 0):
            electron_E = E
            break

    print(f"Electron (1,2,0): E = {electron_E:.6f} m_e c²")
    print()

    print("30 heaviest modes:")
    print(f"  {'(n₁,n₂,n₃)':>14s} | {'E/m_e':>10s} | {'note':>25s}")
    print(f"  {'-' * 58}")

    for i, (n1, n2, n3, L, E) in enumerate(modes[:30]):
        note = ""
        if (n1, n2, n3) == (1, 2, 0):
            note = "← ELECTRON"
        elif (n1, n2, n3) == (-1, -2, 0):
            note = "← anti-electron"
        elif n1 == 1 and n2 == 2 and n3 != 0:
            note = f"← (1,2,{n3})"
        print(f"  ({n1:2d},{n2:2d},{n3:2d}) | {E:10.4f} | {note}")

    # (1,2,k) modes specifically
    print()
    print("(1,2,k) family:")
    print(f"  {'k':>4s} | {'E/m_e':>10s} | {'L/λ_C':>10s} | {'vs electron':>12s}")
    print(f"  {'-' * 45}")
    for k in range(-6, 7):
        L = geodesic_length_T3(1, 2, k, L1, L2, L3, s12, s13, s23)
        E = h * c / L / E_mc2
        rel = "SAME" if k == 0 else \
              f"{E / electron_E:.6f}×" if E < electron_E else \
              f"{E / electron_E:.4f}× HEAVIER"
        print(f"  {k:4d} | {E:10.6f} | {L / lambda_C:10.6f} | {rel}")

    print()

    lighter_12k = [(n1, n2, n3, L, E)
                   for n1, n2, n3, L, E in modes
                   if n1 == 1 and n2 == 2 and n3 != 0 and E < electron_E]
    heavier_12k = [(n1, n2, n3, L, E)
                   for n1, n2, n3, L, E in modes
                   if n1 == 1 and n2 == 2 and n3 != 0 and E > electron_E]

    print(f"(1,2,k≠0) lighter than electron: {len(lighter_12k)}")
    print(f"(1,2,k≠0) heavier than electron: {len(heavier_12k)}")
    print()

    # ── Section 4: Cancellation candidates for quarks ─────────
    print()
    print("SECTION 4: Shear-cancellation candidates for quarks")
    print("-" * 72)
    print()
    print("For (1,2,k) to be quark-mass (~612 m_e), need L ≈ λ_C/612.")
    print("This requires cancellation in L₁ and L₂ terms via shear.")
    print()
    print("L₁ cancels: 1 + 2s₁₂ + ks₁₃ = 0  →  s₁₃ = -{:.4f}/k".format(A))
    print("L₂ cancels: 2 + ks₂₃ = 0          →  s₂₃ = -2/k")
    print()
    print(f"{'k':>4s} | {'s₁₃ needed':>12s} | {'s₂₃ needed':>12s} | "
          f"{'|s| < 1?':>8s} | {'|k|L₃ (fm)':>12s}")
    print("-" * 60)

    for k in [-8, -6, -4, -3, -2, -1, 1, 2, 3, 4, 6, 8]:
        s13_need = -A / k
        s23_need = -2.0 / k
        feasible = abs(s13_need) < 1 and abs(s23_need) < 1
        L3_for_quark = lambda_C / 612 / abs(k)
        print(f"{k:4d} | {s13_need:12.6f} | {s23_need:12.6f} | "
              f"{'✓' if feasible else '✗':>8s} | "
              f"{L3_for_quark * 1e15:12.4f}")

    print()
    print("Feasible cancellation (both |s| < 1):")
    print("  k = -3: s₁₃ = +0.44, s₂₃ = +0.67  (L₃ ≈ 0.13 fm)")
    print("  k = -4: s₁₃ = +0.33, s₂₃ = +0.50  (L₃ ≈ 0.10 fm)")
    print("  k = -6: s₁₃ = +0.22, s₂₃ = +0.33  (L₃ ≈ 0.07 fm)")
    print("  k = -8: s₁₃ = +0.17, s₂₃ = +0.25  (L₃ ≈ 0.05 fm)")
    print()
    print("Note: k = -8 gives s₁₃ ≈ 0.17 ≈ s₁₂ (near-uniform shear).")
    print("      k = -6 gives s₂₃ = 1/3, s₁₃ ≈ 0.22.")
    print()

    # ── Section 5: Do (1,2,k) modes remain lighter for these shears? ─
    print()
    print("SECTION 5: Lighter-mode problem with cancellation shear")
    print("-" * 72)
    print()
    print("If s₁₃ and s₂₃ are tuned to make (1,2,k*) very heavy,")
    print("what happens to the OTHER (1,2,k) modes?")
    print()

    test_cases = [
        (-3, -A / (-3), -2.0 / (-3)),
        (-4, -A / (-4), -2.0 / (-4)),
        (-6, -A / (-6), -2.0 / (-6)),
    ]

    for k_star, s13_v, s23_v in test_cases:
        L3_v = lambda_C / 612 / abs(k_star)
        print(f"Case k* = {k_star}: s₁₃ = {s13_v:.4f}, s₂₃ = {s23_v:.4f}, "
              f"L₃ = {L3_v * 1e15:.3f} fm")

        L_e_check = geodesic_length_T3(1, 2, 0, L1, L2, L3_v,
                                        s12, s13_v, s23_v)
        E_e_check = h * c / L_e_check / E_mc2

        print(f"  Electron (1,2,0): L = {L_e_check:.4e} m, "
              f"E = {E_e_check:.6f} m_e")
        print(f"    (vs unsheared-T³ electron: {electron_E:.6f} m_e "
              f"— {'≈ same' if abs(E_e_check - 1) < 0.01 else 'SHIFTED'})")

        print(f"  {'k':>6s} | {'E/m_e':>10s} | {'vs electron':>14s}")
        print(f"  {'-' * 38}")
        for k in range(-8, 9):
            L = geodesic_length_T3(1, 2, k, L1, L2, L3_v,
                                    s12, s13_v, s23_v)
            E = h * c / L / E_mc2
            status = "← ELECTRON" if k == 0 else \
                     "← QUARK CANDIDATE" if k == k_star else \
                     "LIGHTER" if E < E_e_check else \
                     f"heavier ({E:.1f}×)"
            print(f"  {k:6d} | {E:10.4f} | {status}")
        print()

    # ── Section 6: Assessment ─────────────────────────────────
    print()
    print("SECTION 6: Assessment")
    print("=" * 72)
    print()
    print("F25. LIGHTER MODES ALWAYS EXIST.  On any T³ with s₁₃ = s₂₃ = 0,")
    print("     (1,2,k≠0) modes are lighter than the electron.  Even with")
    print("     nonzero s₁₃ and s₂₃ tuned for quark cancellation, some")
    print("     (1,2,k) modes remain lighter than the electron.")
    print()
    print("     This is a ROBUST result: a continuous tower of (1,2,k)")
    print("     modes exists below the electron mass.  Their non-observation")
    print("     requires explanation.")
    print()
    print("F26. ELECTRON PLANARITY IS NOT ENERGETIC.  The electron (1,2,0)")
    print("     is NOT the lowest-energy member of the (1,2,k) family.")
    print("     It is the HIGHEST-energy (heaviest) member when s₁₃=s₂₃=0.")
    print("     The electron must be 'confined to a plane' by a different")
    print("     mechanism — most likely a CHARGE SELECTION RULE:")
    print("     the 3D charge integral vanishes for k ≠ 0.")
    print()
    print("F27. SHEAR CANCELLATION CAN MAKE SPECIFIC k VERY HEAVY.")
    print("     For k = −3 to −8, feasible shear values (|s| < 1) exist")
    print("     that cancel the L₁ and L₂ terms, leaving L ≈ |k|L₃.")
    print("     This is the same mechanism as Track 4's (1,−6) model,")
    print("     now unified in the (1,2,k) framework on a shared T³.")
    print()
    print("F28. CRITICAL NEXT STEP: The 3D charge integral must be")
    print("     computed (Track 6, Step 1).  It must answer:")
    print("     • Does charge vanish for k ≠ 0?  (explains planarity)")
    print("     • If yes: quarks need a DIFFERENT winding pattern, not")
    print("       just the electron + extra k.")
    print("     • If no: the charge VALUES for each k determine whether")
    print("       fractional charges (1/3, 2/3) emerge naturally.")
    print()
    print("SPIN QUESTION (unresolved):")
    print("  On T², spin ½ comes from the 1:2 winding ratio (field")
    print("  returns after two spatial rotations).  For (1,2,k), the")
    print("  extra winding in direction 3 may change the spin.  If so,")
    print("  (1,2,k≠0) modes may be BOSONS, not fermions — which would")
    print("  independently explain why no lighter charged fermions exist.")
    print("  This needs a group-theoretic analysis on T³.")


if __name__ == "__main__":
    main()
