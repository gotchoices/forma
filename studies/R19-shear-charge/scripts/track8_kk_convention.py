#!/usr/bin/env python3
"""
R19 Track 8: KK convention reconciliation.

R26 Track 1a showed that the KK eigenmode energy formula is the correct
wave-equation result on a flat T² — only it reproduces the experimental
neutrino mass-squared ratio of 33.6.  Tracks 1–3 used the WvM geodesic
Compton constraint (L_geo = λ_C), giving α_WvM.  This track re-derives
α under the KK constraint (E₀ μ(1,2) = m_e c²).

Key insight: the charge PHYSICS (field integration, Gauss's law) is
identical.  Only the relationship between (r, s) and physical scales
(R, a) changes, because the Compton constraint is different.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C

import numpy as np
from scipy.optimize import brentq


# ── Formulas ──────────────────────────────────────────────────────────

def mu_12(r, s):
    """Dimensionless mode energy μ(1,2) under KK."""
    return math.sqrt(1/r**2 + (2 - s)**2)


def alpha_wvm(r, s):
    """Original R19 Track 3 α formula (WvM Compton constraint)."""
    denom = math.sqrt(r**2 * (1 + 2*s)**2 + 4)
    return r**2 * math.sin(2*math.pi*s)**2 / (4*math.pi * (2-s)**2 * denom)


def alpha_ma(r, s):
    """
    α under Ma Compton constraint.

    Derivation:
      KK constraint:  E₀ μ(1,2) = m_e c²
        where E₀ = ℏc/R,  μ = √(1/r²+(2−s)²)
        → R = λ̄_C √(1/r²+(2−s)²)

      Charge integral (unchanged):
        Q = ε₀ E₀ a² π sin(2πs)/(2−s)
        α = Q²/(4πε₀ℏc) = r²(R/λ̄_C) sin²(2πs) / (4π(2−s)²)

      Substituting R/λ̄_C = √(1/r²+(2−s)²):
        α = r² √(1/r²+(2−s)²) sin²(2πs) / (4π(2−s)²)
    """
    mu = math.sqrt(1/r**2 + (2 - s)**2)
    return r**2 * mu * math.sin(2*math.pi*s)**2 / (4*math.pi * (2-s)**2)


def geometry_wvm(r, s):
    """Physical scales under WvM Compton constraint."""
    lambdabar = hbar / (m_e * c)
    R = lambdabar / math.sqrt(r**2 * (1 + 2*s)**2 + 4)
    a = r * R
    return R, a


def geometry_kk(r, s):
    """Physical scales under KK Compton constraint."""
    lambdabar = hbar / (m_e * c)
    R = lambdabar * math.sqrt(1/r**2 + (2 - s)**2)
    a = r * R
    return R, a


def solve_shear(alpha_func, r, alpha_target=alpha):
    """Solve for s at given r using specified α formula."""
    def f(s):
        return alpha_func(r, s) - alpha_target

    s_scan = np.linspace(0.001, 0.499, 5000)
    f_scan = [f(s) for s in s_scan]

    solutions = []
    for i in range(len(f_scan) - 1):
        if f_scan[i] * f_scan[i+1] < 0:
            s_sol = brentq(f, s_scan[i], s_scan[i+1], xtol=1e-14)
            solutions.append(s_sol)

    return solutions


def main():
    lambdabar = hbar / (m_e * c)
    E_mc2 = m_e * c**2

    print("=" * 76)
    print("R19 Track 8: KK Convention Reconciliation")
    print("=" * 76)

    # ── SECTION 1: Analytical derivation ──────────────────────────────
    print()
    print("SECTION 1: The two α formulas")
    print("-" * 76)
    print("""
  The charge integral Q = ε₀ E₀ a²π sin(2πs)/(2−s) is IDENTICAL
  in both conventions.  What differs is the Compton constraint
  that sets R (and hence a = rR, E₀ = √(2mc²/(ε₀V))):

  WvM:  L_geodesic(1,2) = λ_C
        R_WvM = λ̄_C / √(r²(1+2s)² + 4)

  KK:   E₀ μ(1,2) = m_e c²   where μ = √(1/r²+(2−s)²)
        R_KK = λ̄_C √(1/r²+(2−s)²)

  Since α = r²(R/λ̄_C) sin²(2πs) / (4π(2−s)²):

  WvM:  α = r² sin²(2πs) / (4π(2−s)² √(r²(1+2s)²+4))
  KK:   α = r² √(1/r²+(2−s)²) sin²(2πs) / (4π(2−s)²)

  The ratio:
    α_KK/α_WvM = √((1/r²+(2−s)²)(r²(1+2s)²+4))
""")

    for r in [1.0, 3.0, 6.6]:
        s_wvm_sols = solve_shear(alpha_wvm, r)
        s_wvm = s_wvm_sols[0] if s_wvm_sols else float('nan')
        ratio = math.sqrt((1/r**2 + (2-s_wvm)**2) * (r**2*(1+2*s_wvm)**2 + 4))
        print(f"  r = {r:.1f}: α_KK/α_WvM = {ratio:.3f}  "
              f"(at WvM solution s = {s_wvm:.6f})")

    # ── SECTION 2: s(r) comparison ────────────────────────────────────
    print()
    print("SECTION 2: s(r) curves — WvM vs KK")
    print("-" * 76)
    print()

    r_values = [0.50, 0.75, 1.00, 1.25, 1.50, 2.00, 3.00, 4.00, 5.00, 6.60]

    print(f"{'r':>6s} | {'s_WvM':>10s} | {'s_KK':>10s} | "
          f"{'ratio':>8s} | {'R_WvM(m)':>11s} | {'R_KK(m)':>11s} | "
          f"{'R ratio':>8s}")
    print("-" * 82)

    results = []

    for r in r_values:
        s_wvm_sols = solve_shear(alpha_wvm, r)
        s_kk_sols = solve_shear(alpha_ma, r)

        s_wvm = s_wvm_sols[0] if s_wvm_sols else float('nan')
        s_kk = s_kk_sols[0] if s_kk_sols else float('nan')

        if math.isnan(s_wvm) and math.isnan(s_kk):
            print(f"{r:6.2f} | {'---':>10s} | {'---':>10s} | "
                  f"{'---':>8s} | {'---':>11s} | {'---':>11s} | {'---':>8s}")
            continue

        R_w = geometry_wvm(r, s_wvm)[0] if not math.isnan(s_wvm) else float('nan')
        R_k = geometry_kk(r, s_kk)[0] if not math.isnan(s_kk) else float('nan')

        s_ratio = s_kk / s_wvm if (not math.isnan(s_wvm) and s_wvm > 0) else float('nan')
        R_ratio = R_k / R_w if (not math.isnan(R_w) and R_w > 0) else float('nan')

        results.append((r, s_wvm, s_kk, R_w, R_k))

        s_w_str = f"{s_wvm:.6f}" if not math.isnan(s_wvm) else "---"
        s_k_str = f"{s_kk:.6f}" if not math.isnan(s_kk) else "---"
        sr_str = f"{s_ratio:.4f}" if not math.isnan(s_ratio) else "---"
        Rw_str = f"{R_w:.4e}" if not math.isnan(R_w) else "---"
        Rk_str = f"{R_k:.4e}" if not math.isnan(R_k) else "---"
        Rr_str = f"{R_ratio:.4f}" if not math.isnan(R_ratio) else "---"

        print(f"{r:6.2f} | {s_w_str:>10s} | {s_k_str:>10s} | "
              f"{sr_str:>8s} | {Rw_str:>11s} | {Rk_str:>11s} | {Rr_str:>8s}")

    # ── SECTION 3: Geometric interpretation under KK ──────────────────
    print()
    print("SECTION 3: Full electron geometry under KK")
    print("-" * 76)
    print()

    for r, s_wvm, s_kk, R_w, R_k in results:
        if math.isnan(s_kk):
            continue

        a_k = r * R_k
        V_k = 2 * math.pi**2 * a_k**2 * R_k

        E0_field = math.sqrt(2 * E_mc2 / (eps0 * V_k))
        Q = eps0 * E0_field * a_k**2 * math.pi * abs(math.sin(2*math.pi*s_kk)) / abs(2 - s_kk)
        alpha_check = Q**2 / (4 * math.pi * eps0 * hbar * c)

        E_mode = (hbar * c / R_k) * mu_12(r, s_kk)

        delta_over_a = 2 * math.pi * s_kk
        q_eff = 2 - s_kk

        g_r = 0.5
        E_C = Q**2 * g_r / (4 * math.pi * eps0 * R_k)

        print(f"  r = {r:.2f}")
        print(f"    s_KK      = {s_kk:.8f}   (δ/a = {delta_over_a:.4f} = "
              f"{math.degrees(delta_over_a):.1f}°)")
        print(f"    R         = {R_k:.4e} m   a = {a_k:.4e} m")
        print(f"    E(1,2)    = {E_mode/E_mc2:.8f} m_e c²   "
              f"(α check: {alpha_check:.6e} vs {alpha:.6e})")
        print(f"    q_eff     = {q_eff:.6f}")
        print(f"    E_Coulomb = {E_C/E_mc2:.4e} m_e c² = "
              f"{E_C/E_mc2/alpha:.2f} α m_e c²")
        print()

    # ── SECTION 4: F7 resolution ──────────────────────────────────────
    print()
    print("SECTION 4: Resolution of F7 (eigenmode vs geodesic energy)")
    print("-" * 76)
    print()

    r1_data = [x for x in results if abs(x[0] - 1.0) < 0.01]
    if r1_data:
        r, s_w, s_k, R_w, R_k = r1_data[0]

        E_eigenmode_on_wvm = (hbar * c / R_w) * mu_12(r, s_w)
        L_geo_wvm = math.sqrt((2*math.pi*r*R_w*(1+2*s_w))**2 + (4*math.pi*R_w)**2)
        E_geo_wvm = h * c / L_geo_wvm

        E_eigenmode_on_kk = (hbar * c / R_k) * mu_12(r, s_k)

        print(f"  F7 stated: on the WvM-sized torus (r=1), the eigenmode energy")
        print(f"  is {E_eigenmode_on_wvm/E_mc2:.2f}× m_e c² — inconsistent with m_e.")
        print()
        print(f"  Resolution: the WvM torus is too SMALL.  Smaller cavity →")
        print(f"  higher eigenfrequencies.  The torus must be LARGER so")
        print(f"  E(1,2) = m_e c².")
        print()
        print(f"  WvM torus (r=1):  R = {R_w:.4e} m   E_eigen = {E_eigenmode_on_wvm/E_mc2:.4f} m_e c²")
        print(f"  KK  torus (r=1):  R = {R_k:.4e} m   E_eigen = {E_eigenmode_on_kk/E_mc2:.8f} m_e c²  ✓")
        print()
        print(f"  The KK torus is {R_k/R_w:.1f}× larger (R_KK/R_WvM = {R_k/R_w:.2f}).")
        print(f"  The eigenmode energy is m_e c² by construction.  F7 is")
        print(f"  resolved: the photon IS the eigenmode, on the correctly-")
        print(f"  sized torus.")

    # ── SECTION 5: Critical aspect ratio ──────────────────────────────
    print()
    print()
    print("SECTION 5: Critical aspect ratio under KK")
    print("-" * 76)
    print()

    r_scan = np.linspace(0.01, 2.0, 2000)
    r_crit_kk = None
    for r in r_scan:
        sols = solve_shear(alpha_ma, r)
        if sols:
            r_crit_kk = r
            break

    r_crit_wvm = None
    for r in r_scan:
        sols = solve_shear(alpha_wvm, r)
        if sols:
            r_crit_wvm = r
            break

    print(f"  r_crit (WvM): {r_crit_wvm:.3f}")
    print(f"  r_crit (KK):  {r_crit_kk:.3f}")
    print()

    max_alpha_ma_vals = []
    for r in [0.1, 0.2, 0.3, 0.4, 0.5]:
        s_test = np.linspace(0.001, 0.499, 1000)
        a_vals = [alpha_ma(r, s) for s in s_test]
        max_alpha_ma_vals.append((r, max(a_vals)))
        print(f"  r = {r:.1f}: max(α_KK) = {max(a_vals):.6f}  "
              f"(need {alpha:.6f})")

    # ── SECTION 6: Lattice angle comparison ───────────────────────────
    print()
    print()
    print("SECTION 6: Geometric naturalness — lattice angle")
    print("-" * 76)
    print()

    print(f"{'r':>6s} | {'s_WvM':>10s} | {'angle_WvM':>10s} | "
          f"{'s_KK':>10s} | {'angle_KK':>10s} | {'off-90_WvM':>10s} | "
          f"{'off-90_KK':>10s}")
    print("-" * 82)

    for r, s_w, s_k, _, _ in results:
        if math.isnan(s_w) or math.isnan(s_k):
            continue
        L1_over_L2 = r
        for label, s_val in [("", s_w), ("", s_k)]:
            pass

        angle_w = math.degrees(math.atan2(1, s_w * r)) if s_w > 0 else 90.0
        angle_k = math.degrees(math.atan2(1, s_k * r)) if s_k > 0 else 90.0
        off90_w = 90.0 - angle_w
        off90_k = 90.0 - angle_k

        print(f"{r:6.2f} | {s_w:10.6f} | {angle_w:9.1f}° | "
              f"{s_k:10.6f} | {angle_k:9.1f}° | "
              f"{off90_w:9.1f}° | {off90_k:9.1f}°")

    # ── SECTION 7: Neutrino consistency check ─────────────────────────
    print()
    print()
    print("SECTION 7: Neutrino mass ratio — convention-independence check")
    print("-" * 76)
    print()

    s_nu = 0.02199
    print(f"  Neutrino shear s₃₄ = {s_nu}")
    print()

    for r_nu in [1.0, 3.0, 6.6, 10.0]:
        mu_11 = math.sqrt(1/r_nu**2 + (1 - s_nu)**2)
        mu_m11 = math.sqrt(1/r_nu**2 + (1 + s_nu)**2)
        mu_12_v = math.sqrt(1/r_nu**2 + (2 - s_nu)**2)

        dm2_21 = mu_m11**2 - mu_11**2
        dm2_31 = mu_12_v**2 - mu_11**2

        ratio_kk = dm2_31 / dm2_21

        L_11 = math.sqrt(r_nu**2*(1+s_nu)**2 + 1)
        L_m11 = math.sqrt(r_nu**2*(1-s_nu)**2 + 1)
        L_12 = math.sqrt(r_nu**2*(1+2*s_nu)**2 + 4)

        e_11 = 1 / L_11
        e_m11 = 1 / L_m11
        e_12 = 1 / L_12

        e_sorted = sorted([e_11, e_m11, e_12])
        dm2_21_w = e_sorted[1]**2 - e_sorted[0]**2
        dm2_31_w = e_sorted[2]**2 - e_sorted[0]**2
        ratio_wvm = dm2_31_w / dm2_21_w if dm2_21_w > 0 else float('nan')

        print(f"  r_ν = {r_nu:5.1f}:  KK ratio = {ratio_kk:6.2f}  "
              f"WvM ratio = {ratio_wvm:6.2f}  "
              f"{'✓' if abs(ratio_kk - 33.6) < 0.5 else '✗'} / "
              f"{'✓' if abs(ratio_wvm - 33.6) < 0.5 else '✗'}")

    print()
    print("  KK ratio is r-independent (always 33.60).  ✓")
    print("  WvM ratio is r-dependent and wrong.  ✗")
    print("  → KK is the correct mode energy formula.")

    # ── SECTION 8: Summary ────────────────────────────────────────────
    print()
    print()
    print("SECTION 8: Track 8 Summary")
    print("=" * 76)
    print()

    r1 = [x for x in results if abs(x[0] - 1.0) < 0.01]
    r66 = [x for x in results if abs(x[0] - 6.6) < 0.01]

    if r1:
        _, s_w1, s_k1, R_w1, R_k1 = r1[0]
        print(f"  At r = 1.0:")
        print(f"    WvM: s = {s_w1:.6f}, R = {R_w1:.4e} m")
        print(f"    KK:  s = {s_k1:.6f}, R = {R_k1:.4e} m")
        print(f"    s_KK/s_WvM = {s_k1/s_w1:.4f}")
        print()

    if r66:
        _, s_w66, s_k66, R_w66, R_k66 = r66[0]
        print(f"  At r = 6.6:")
        print(f"    WvM: s = {s_w66:.6f}, R = {R_w66:.4e} m")
        print(f"    KK:  s = {s_k66:.6f}, R = {R_k66:.4e} m")
        print(f"    s_KK/s_WvM = {s_k66/s_w66:.4f}")
        print()

    print("""  CONCLUSIONS:

  1. SAME PHYSICS: The charge mechanism (shear → sin(2πs)/(2−s)
     → net Gauss flux) is identical in both conventions.

  2. DIFFERENT SCALES: KK gives a larger torus (R_KK > R_WvM)
     and a smaller shear (s_KK < s_WvM) for the same α = 1/137.

  3. F7 RESOLVED: The eigenmode energy equals m_e c² on the KK
     torus by construction.  The "5× discrepancy" arose from
     computing eigenmode energy on the (too-large) WvM torus.

  4. NEUTRINO PROOF: The KK formula gives the r-independent
     mass-squared ratio 33.60 (matching experiment).  WvM gives
     r-dependent ratios ~1–2.  This is decisive evidence for KK.

  5. ONE-PARAMETER FAMILY PRESERVED: Under KK, the electron is
     still a one-parameter family in r.  For each r > r_crit,
     there is a unique s giving α = 1/137.

  6. ACTION: All R19 results (F1–F16) carry over with updated
     numerical values.  The α formula changes but the structure
     (one equation, two unknowns r and s, one free parameter)
     is unchanged.  R26's Track 2 can use KK scales directly.
""")


if __name__ == "__main__":
    main()
