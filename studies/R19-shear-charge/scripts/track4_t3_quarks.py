#!/usr/bin/env python3
"""
R19 Track 4: T³ quark charges from winding numbers.

Most constrained hypothesis: a single T³ with uniform shear
(s₁₂ = s₂₃ = s₁₃ = s) supports three particles as different
winding configurations, producing charges e, 2e/3, e/3.

The T³ has circumferences L₁, L₂, L₃ and a single shear s.
After fixing the electron mass (sets one scale), there are
3 free parameters: two aspect ratios (r₁₂ = L₁/L₂,
r₂₃ = L₂/L₃) and the shear s.  Three charge equations
(Q_e = e, Q_u = 2e/3, Q_d = e/3) make the system exactly
determined.

Generalized charge formula for an (n,m) mode on a 2D plane
with circumferences Lₐ, L_b and shear s:

    q_eff(n,m) = m − n·s

    Q(n,m) ∝ sin(2πns) / (m − ns) × normalization

The normalization depends on the photon energy (geodesic length)
and the 2D geometry (aspect ratio of the plane).

For the electron on the (1,2) plane (T² results carry over):
    α_e = r₁₂² sin²(2πs) / (4π(2−s)² √(r₁₂²(1+2s)²+4))
    Q_e² = 4πε₀ℏc × α_e  →  Q_e = e
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq, fsolve

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C


# ── Core formulas ──────────────────────────────────────────────

def alpha_from_plane(r, s, n, m):
    """
    Charge² / (4πε₀ℏc) for an (n,m) mode on a 2D plane with
    aspect ratio r = L_tube/L_ring and shear s.

    Generalizes the electron formula:
      α = r² sin²(2πns) / (4π (m−ns)² √(r²(1+2ns/m... wait)

    Need to be careful: the self-consistent Compton constraint
    and normalization both depend on (n,m).
    """
    q_eff = m - n * s

    # Geodesic path length for (n,m) on sheared lattice:
    # In the universal cover, the (n,m) endpoint is at:
    #   x = n·L₁ + m·s·L₁ = L₁(n + ms)
    #   y = m·L₂
    # where L₁ = 2π·a (tube circ), L₂ = 2π·R (ring circ)
    # Path length² = x² + y² = L₁²(n+ms)² + L₂²m²
    #              = (2πa)²(n+ms)² + (2πR)²m²
    #              = 4π²(a²(n+ms)² + R²m²)
    # L = 2π√(a²(n+ms)² + m²R²)
    #
    # With r = a/R:
    # L = 2πR√(r²(n+ms)² + m²)
    #
    # Compton constraint: L = λ = hc/E_photon
    # So R = λ/(2π√(r²(n+ms)² + m²))

    denom_sq = r**2 * (n + m*s)**2 + m**2
    denom = math.sqrt(denom_sq)

    # The charge formula, normalized so that total photon
    # energy = E_photon on the 2D subtorus:
    #
    # α_mode = r² sin²(2πns) / (4π q_eff² √(r²(n+ms)² + m²))
    #
    # This follows the same derivation as Track 1/3:
    # Q = ε₀ E₀ a²π sin(2πns)/q_eff
    # E₀ = √(E_photon / (ε₀ π² a² R))
    # Q² = ε₀ a² E_photon sin²(2πns) / (R q_eff²)
    # α_mode = Q²/(4πε₀ℏc) = a² E_photon sin²(2πns) / (4πℏc R q_eff²)
    #        = r² R E_photon sin²(2πns) / (4πℏc q_eff²)
    # With E_photon = hc/L and R = L/(2π denom):
    #   = r² [L/(2π denom)] × [hc/L] × sin²(2πns) / (4πℏc q_eff²)
    #   = r² h / (8π² denom) × sin²(2πns) / (4πℏ q_eff²)
    #   = r² × (h/(4πℏ)) / (8π² denom) × sin²(2πns) / q_eff²
    # Note h/(4πℏ) = h/(4π × h/(2π)) = 1/2. So:
    #   = r² sin²(2πns) / (16π² denom q_eff²)
    # Hmm, let me redo this more carefully.

    # Q² = ε₀ E₀² a⁴ π² sin²(2πns) / q_eff²
    # Wait, let me go back to the derivation from Track 1/3.
    #
    # Q = ε₀ E₀ a² π |sin(2πs)| / |2-s|  [for (1,2)]
    # Generalized to (n,m):
    # Q = ε₀ E₀ a² π |sin(2πns)| / |q_eff|   ... but need to check

    # Actually the integral is:
    # Q = ε₀ E₀ ∫ cos(q_eff Φ) × a × dΦ × a_surface_element
    # On the torus surface, the area element in the φ-direction is
    # just a dΘ dΦ (for flat T²).  The charge integral is:
    # Q = ε₀ E₀ ∫₀²π ∫₀²π cos(nΘ + q_eff Φ) a dΘ R dΦ  ... no.
    #
    # Let me think about this more carefully.  The Gauss's law
    # integral picks up the φ-average of the radial E-field.
    # The radial field at angle Φ is proportional to cos(q_eff Φ).
    # Wait, for (1,2) mode, the field on the surface goes as
    # cos(Θ + q_eff Φ).  The Θ-integration over [0, 2π] gives
    # zero for the n=1 component UNLESS we're looking at the
    # monopole moment.
    #
    # Actually, I think the charge formula is more subtle for
    # general (n,m).  For the (1,2) electron, the WvM charge
    # mechanism relies on the p=1 tube winding: the E-field
    # rotates once around the tube cross-section per tube
    # circumference, which means the radial component has a
    # nonzero average when projected outward.
    #
    # For a general (n,m) mode, the tube winding is n.
    # The WvM mechanism requires n=1 for the monopole moment
    # to be nonzero (higher n gives zero Θ-average).
    #
    # Let me re-examine: for an (n,m) mode, the field goes as
    # cos(n Θ + q_eff Φ).  The radial component of E at angle
    # Θ on the tube is E_r ∝ cos(Θ) × cos(nΘ + q_eff Φ).
    # Integrating over Θ ∈ [0, 2π]:
    # ∫₀²π cos(Θ) cos(nΘ + q_eff Φ) dΘ = π cos(q_eff Φ) [n=1]
    #                                     = 0            [n≠1]
    #
    # So n must equal 1 for charge to be nonzero!
    # This is the same constraint S3 found, just now on a
    # sheared lattice.

    if n != 1:
        return 0.0

    # For n = 1:  q_eff = m - s
    q_eff = m - s
    sin_term = math.sin(2 * math.pi * s)

    if abs(sin_term) < 1e-15:
        return 0.0
    if abs(q_eff) < 1e-15:
        return float('inf')

    # Self-consistent formula (n=1):
    # L = 2π√(a²(1+ms)² + m²R²)
    # With r = a/R:
    # denom = √(r²(1+ms)² + m²)
    denom = math.sqrt(r**2 * (1 + m*s)**2 + m**2)

    alpha_val = r**2 * sin_term**2 / (4 * math.pi * q_eff**2 * denom)
    return alpha_val


def charge_ratio_pure(s, m1, m2):
    """
    Charge ratio Q(1,m2)/Q(1,m1) from the sin/q_eff factors alone,
    ignoring normalization differences.

    Q ∝ sin(2πs) / (m - s)  [for n=1]

    The sin(2πs) factor is the SAME for all n=1 modes, so:
    Q(1,m2)/Q(1,m1) = (m1 - s) / (m2 - s)

    This is purely geometric — the charge ratio is determined
    by the shear s and the winding numbers alone (for uniform
    shear with the same normalization conventions).
    """
    return abs((m1 - s) / (m2 - s))


def main():
    print("=" * 72)
    print("R19 Track 4: T³ Quark Charges from Winding Numbers")
    print("=" * 72)
    print()

    # ── Section 1: n=1 constraint ─────────────────────────────
    print("SECTION 1: The n=1 constraint persists on sheared T²")
    print("-" * 72)
    print()
    print("The WvM charge mechanism requires the E-field to rotate")
    print("ONCE around the tube cross-section per period (n=1).")
    print("For n ≠ 1, the Θ-integral of cos(Θ)cos(nΘ+q_eff Φ)")
    print("vanishes — no monopole moment.")
    print()
    print("This means ALL charged particles must have n = 1 tube")
    print("winding.  Different charges come from different φ-winding")
    print("numbers m, not from different n values.")
    print()
    print("For n = 1 modes on a sheared lattice:")
    print("  q_eff(1,m) = m − s")
    print("  Q ∝ sin(2πs) / (m − s)")
    print()
    print("Since sin(2πs) is the same for all m, the charge RATIO")
    print("between two modes (1,m₁) and (1,m₂) is simply:")
    print()
    print("  Q(1,m₂) / Q(1,m₁) = (m₁ − s) / (m₂ − s)")
    print()
    print("This is purely geometric — independent of aspect ratios")
    print("and normalization (assuming the same plane and E₀).")
    print()

    # ── Section 2: Can uniform shear give the right ratios? ───
    print("SECTION 2: Charge ratios from different m values")
    print("-" * 72)
    print()
    print("Electron: (1,2) mode, Q_e = e")
    print("Up quark: (1,m_u) mode, Q_u = 2e/3")
    print("Down quark: (1,m_d) mode, Q_d = e/3")
    print()
    print("Required ratios (relative to electron):")
    print("  Q_u/Q_e = 2/3 = (2−s)/(m_u−s)")
    print("  Q_d/Q_e = 1/3 = (2−s)/(m_d−s)")
    print()
    print("Solving for m_u and m_d:")
    print("  m_u − s = (3/2)(2−s) = 3 − 3s/2  →  m_u = 3 − s/2")
    print("  m_d − s = 3(2−s) = 6 − 3s         →  m_d = 6 − 2s")
    print()

    print("For m_u and m_d to be INTEGERS (required for periodic")
    print("boundary conditions on T³):")
    print()
    print("  m_u = 3 − s/2 ∈ ℤ  →  s = 2(3 − m_u)")
    print("  m_d = 6 − 2s ∈ ℤ   →  s = (6 − m_d)/2")
    print()
    print("Both must give the same s.  Let's check:")
    print()

    print("| m_u | s (from m_u) | m_d (from s) | m_d integer? | s range ok? |")
    print("|-----|-------------|-------------|-------------|-------------|")
    for m_u in range(1, 8):
        s_from_mu = 2 * (3 - m_u)
        m_d_from_s = 6 - 2 * s_from_mu
        md_is_int = (m_d_from_s == int(m_d_from_s))
        s_ok = 0 < s_from_mu < 1
        print(f"|  {m_u}  | {s_from_mu:11.4f} | {m_d_from_s:11.4f} | "
              f"{'✓' if md_is_int else '✗':^11s} | "
              f"{'✓' if s_ok else '✗ (s=' + str(s_from_mu) + ')':^11s} |")
    print()

    print("RESULT: No integer m_u gives s ∈ (0,1).")
    print()
    print("The constraint m_u = 3 − s/2 requires s = 2(3 − m_u).")
    print("For m_u = 2: s = 2.  For m_u = 3: s = 0.  Neither is")
    print("in the physical range 0 < s < 1.")
    print()

    # ── Section 3: Same-plane analysis ────────────────────────
    print("SECTION 3: What if quarks are in DIFFERENT planes?")
    print("-" * 72)
    print()
    print("The above assumed all three particles share the same")
    print("2D plane (same r and E₀).  On T³, the quarks may be")
    print("in different planes with different aspect ratios.")
    print()
    print("In different planes, the normalization differs because")
    print("the photon energy (geodesic length) and geometry (a, R)")
    print("are different.  The charge formula becomes:")
    print()
    print("  α_mode = r² sin²(2πs) / (4π (m−s)² √(r²(1+ms)²+m²))")
    print()
    print("where r is the aspect ratio of the specific plane.")
    print()

    # For each candidate m, find the aspect ratio r that gives
    # the target charge
    print("For each m, solve for the aspect ratio r that gives")
    print("the target charge, with the SAME shear s as the electron.")
    print()

    # Use the electron's self-consistent s at r=1 as reference
    def alpha_n1(r, s, m):
        q = m - s
        if abs(q) < 1e-15:
            return float('inf')
        sin_term = math.sin(2 * math.pi * s)**2
        denom = math.sqrt(r**2 * (1 + m*s)**2 + m**2)
        return r**2 * sin_term / (4 * math.pi * q**2 * denom)

    def solve_for_r(s, m, target_alpha):
        """Find r such that alpha_n1(r, s, m) = target_alpha."""
        def f(r):
            return alpha_n1(r, s, m) - target_alpha
        # Scan for root
        r_vals = np.linspace(0.01, 50, 10000)
        f_vals = [f(r) for r in r_vals]
        solutions = []
        for i in range(len(f_vals) - 1):
            if f_vals[i] * f_vals[i+1] < 0:
                r_sol = brentq(f, r_vals[i], r_vals[i+1], xtol=1e-12)
                solutions.append(r_sol)
        return solutions

    # Reference: electron at r_e = 1, find s
    def solve_electron_s(r_e):
        def f(s):
            return alpha_n1(r_e, s, 2) - alpha
        s_scan = np.linspace(0.001, 0.999, 5000)
        f_scan = [f(s) for s in s_scan]
        for i in range(len(f_scan) - 1):
            if f_scan[i] * f_scan[i+1] < 0 and s_scan[i] < 0.5:
                return brentq(f, s_scan[i], s_scan[i+1], xtol=1e-14)
        return None

    r_e_values = [1.0, 1.5, 2.0]

    alpha_u = alpha * (2/3)**2  # Q_u = 2e/3
    alpha_d = alpha * (1/3)**2  # Q_d = e/3

    print("Target α values:")
    print(f"  α_e = {alpha:.10f}  (Q = e)")
    print(f"  α_u = {alpha_u:.10f}  (Q = 2e/3)")
    print(f"  α_d = {alpha_d:.10f}  (Q = e/3)")
    print()

    for r_e in r_e_values:
        s_e = solve_electron_s(r_e)
        if s_e is None:
            print(f"r_e = {r_e}: no electron solution found")
            continue

        print(f"Electron: r_e = {r_e:.2f}, s = {s_e:.8f}")
        print(f"  α_e = {alpha_n1(r_e, s_e, 2):.10f} (target: {alpha:.10f})")
        print()

        # For each candidate quark winding m, find r in their plane
        m_candidates = [1, 2, 3, 4, 5, 6]

        print(f"  Up quark (Q = 2e/3, α_u = {alpha_u:.6e}):")
        print(f"  {'m':>4s} | {'r required':>12s} | {'α achieved':>14s} | {'feasible':>10s}")
        print(f"  {'-'*50}")
        for m in m_candidates:
            sols = solve_for_r(s_e, m, alpha_u)
            if sols:
                for r_sol in sols[:2]:
                    a_check = alpha_n1(r_sol, s_e, m)
                    print(f"  {m:4d} | {r_sol:12.6f} | {a_check:14.10f} | {'✓':>10s}")
            else:
                alpha_max = max(alpha_n1(r, s_e, m)
                               for r in np.linspace(0.01, 50, 5000))
                print(f"  {m:4d} | {'---':>12s} | α_max={alpha_max:.2e} | "
                      f"{'✗ too small' if alpha_max < alpha_u else '✗':>10s}")
        print()

        print(f"  Down quark (Q = e/3, α_d = {alpha_d:.6e}):")
        print(f"  {'m':>4s} | {'r required':>12s} | {'α achieved':>14s} | {'feasible':>10s}")
        print(f"  {'-'*50}")
        for m in m_candidates:
            sols = solve_for_r(s_e, m, alpha_d)
            if sols:
                for r_sol in sols[:2]:
                    a_check = alpha_n1(r_sol, s_e, m)
                    print(f"  {m:4d} | {r_sol:12.6f} | {a_check:14.10f} | {'✓':>10s}")
            else:
                alpha_max = max(alpha_n1(r, s_e, m)
                               for r in np.linspace(0.01, 50, 5000))
                print(f"  {m:4d} | {'---':>12s} | α_max={alpha_max:.2e} | "
                      f"{'✗ too small' if alpha_max < alpha_d else '✗':>10s}")
        print()

    # ── Section 4: Mass consistency ───────────────────────────
    print()
    print("SECTION 4: Mass consistency check")
    print("-" * 72)
    print()
    print("If the quarks are (1,m) modes in different planes of T³,")
    print("each quark photon has energy E = hc/L_geodesic.")
    print()
    print("The geodesic length for a (1,m) mode on a plane with")
    print("aspect ratio r and shear s:")
    print("  L = 2πR √(r²(1+ms)² + m²)")
    print("  E = hc/L")
    print()
    print("The electron has E_e = m_e c².  A quark with (1,m) in")
    print("a plane with aspect ratio r_q has:")
    print("  E_q/E_e = L_e/L_q")
    print()

    # Compute mass ratios for the solutions found above
    r_e = 1.0
    s_e = solve_electron_s(r_e)
    L_e_factor = math.sqrt(r_e**2 * (1 + 2*s_e)**2 + 4)

    print(f"Reference electron: r = {r_e}, s = {s_e:.8f}")
    print(f"  L_e ∝ √(r²(1+2s)² + 4) = {L_e_factor:.6f}")
    print()

    m_vals = [1, 2, 3, 4, 5, 6]
    alpha_targets = {'u': alpha_u, 'd': alpha_d}

    for quark_name, alpha_target in alpha_targets.items():
        print(f"Quark {quark_name} (α = {alpha_target:.6e}):")
        for m in m_vals:
            sols = solve_for_r(s_e, m, alpha_target)
            if sols:
                r_q = sols[0]
                L_q_factor = math.sqrt(r_q**2 * (1 + m*s_e)**2 + m**2)

                # R_q from Compton-like constraint
                # (if the quark photon has its own energy, L_q sets
                # a different R_q, but they share the same T³, so
                # the circumferences are shared.)
                #
                # Actually, on a shared T³, the circumferences are
                # L₁, L₂, L₃.  The electron in the (1,2) plane sees
                # L₁ and L₂.  A quark in the (1,3) plane sees L₁ and
                # L₃.  The aspect ratios are:
                #   r_e = L₁/(2πR_e) ... this needs rethinking.
                #
                # The "aspect ratio" of a plane is r_ij = Lᵢ/Lⱼ
                # (ratio of the two circumferences in that plane).
                # For the (1,2) plane: r₁₂ = L₁/L₂
                # For the (1,3) plane: r₁₃ = L₁/L₃
                # For the (2,3) plane: r₂₃ = L₂/L₃
                #
                # These are related: r₁₃ = r₁₂ × r₂₃

                # The quark mass relative to electron:
                # E_q/E_e = L_e/L_q = (R_e × L_e_factor) / (R_q × L_q_factor)
                #
                # But R_e and R_q refer to different circumferences
                # of the T³.  If the electron uses (L₁, L₂) and the
                # quark uses (Lᵢ, Lⱼ), these may share some L's.

                # For simplicity, report the geodesic length factor
                print(f"  m={m}, r_q = {r_q:.4f}: "
                      f"L_q_factor = {L_q_factor:.4f}, "
                      f"L_e/L_q = {L_e_factor/L_q_factor:.4f} "
                      f"(if same R)")
        print()

    # ── Section 5: Shared T³ with mass constraint ──────────────
    print()
    print("SECTION 5: The mass constraint on a shared T³")
    print("=" * 72)
    print()
    print("On a shared T³, the circumferences L₁, L₂, L₃ are fixed.")
    print("The electron (1,2) in the (1,2) plane sets L₁ and L₂")
    print("at the Compton scale (~10⁻¹² m).")
    print()
    print("A quark has energy E_q ≈ 612 m_e c² (from m_p = 3×612×m_e).")
    print("Its geodesic must be 612× shorter than the electron's:")
    print("  L_q = λ_C / 612 ≈ 3.96 × 10⁻¹⁵ m")
    print()
    print("But the quark's plane SHARES a circumference with the")
    print("electron.  E.g., quarks in (2,3) plane share L₂ with")
    print("the electron, where L₂ ~ 10⁻¹² m.")
    print()
    print("For a (1,m) mode in the (2,3) plane on a sheared lattice:")
    print("  L_q = √(L₂²(1+ms)² + m²L₃²)")
    print()
    print("Since L₂ ~ 10⁻¹² ≫ L_q ~ 10⁻¹⁵, the L₂ term")
    print("dominates UNLESS (1+ms) ≈ 0, i.e., m ≈ −1/s.")
    print()

    r_e = 1.0
    s_e = solve_electron_s(r_e)
    L2 = lambda_C / math.sqrt(r_e**2 * (1+2*s_e)**2 + 4)
    L1 = r_e * L2
    L_e = math.sqrt(L1**2 * (1+2*s_e)**2 + 4*L2**2)

    print(f"Electron (r=1): s = {s_e:.8f}, 1/s = {1/s_e:.4f}")
    print(f"  L₁ = {L1:.6e} m, L₂ = {L2:.6e} m")
    print(f"  L_e = {L_e:.6e} m = λ_C = {lambda_C:.6e} m")
    print()

    E_quark = 612 * m_e * c**2
    L_q_target = h * c / E_quark

    print(f"Target quark geodesic: L_q = {L_q_target:.4e} m")
    print(f"  (= λ_C/612 = {lambda_C/612:.4e} m)")
    print()

    print("Critical near-miss: s ≈ 0.165, and 1/6 = 0.1667.")
    print(f"  s / (1/6) = {s_e * 6:.6f}")
    print(f"  If s = 1/6 exactly, then m = −6 gives (1+ms) = 0 exactly.")
    print()

    print("Scanning m values for the quark in the (2,3) plane:")
    print(f"{'m':>5s} | {'1+ms':>10s} | {'L_q(L₃=0)':>12s} | "
          f"{'L₃ needed':>12s} | {'L₃ (fm)':>10s} | {'E_q/m_e':>10s}")
    print("-" * 75)

    for m in [-8, -7, -6, -5, -4, -3, 3, 4, 5, 6]:
        factor_1ms = 1 + m * s_e

        # L_q if L₃ = 0 (only the L₂ term)
        L_q_L3_zero = abs(factor_1ms) * L2
        E_from_L2_only = h * c / L_q_L3_zero if L_q_L3_zero > 0 else float('inf')

        # L₃ needed to achieve L_q = λ_C/612, assuming the L₂ term
        # is what it is
        L_q_sq_target = L_q_target**2
        L2_contribution = L2**2 * factor_1ms**2
        if L_q_sq_target > L2_contribution:
            L3_needed = math.sqrt((L_q_sq_target - L2_contribution) / m**2)
            L_q_check = math.sqrt(L2_contribution + m**2 * L3_needed**2)
            E_q_check = h * c / L_q_check / (m_e * c**2)
        else:
            L3_needed = None

        if L3_needed is not None:
            print(f"{m:5d} | {factor_1ms:10.6f} | {L_q_L3_zero:12.4e} | "
                  f"{L3_needed:12.4e} | {L3_needed*1e15:10.4f} | "
                  f"{E_q_check:10.2f}")
        else:
            E_from_L2 = h * c / L_q_L3_zero / (m_e * c**2) if L_q_L3_zero > 1e-30 else 0
            print(f"{m:5d} | {factor_1ms:10.6f} | {L_q_L3_zero:12.4e} | "
                  f"{'L₂ alone > L_q':>12s} | {'---':>10s} | "
                  f"{E_from_L2:10.2f}")

    print()

    # Focus on m = -6 case
    m_q = -6
    factor_1ms = 1 + m_q * s_e
    print(f"FOCUS: m = {m_q}")
    print(f"  (1 + ms) = 1 + ({m_q})(0.16513) = {factor_1ms:.6f}")
    print(f"  This is {abs(factor_1ms):.4f}, not zero.")
    print(f"  L₂ contribution: |1+ms| × L₂ = {abs(factor_1ms)*L2:.4e} m")
    print(f"  This alone gives E = {h*c/(abs(factor_1ms)*L2)/(m_e*c**2):.1f} m_e c²")
    print()

    # What if s = 1/6 exactly?
    s_exact = 1.0/6.0
    factor_exact = 1 + m_q * s_exact
    print(f"If s were exactly 1/6:")
    print(f"  (1 + ms) = 1 + ({m_q})(1/6) = {factor_exact:.10f}")
    print(f"  L₂ contribution vanishes exactly!")
    print(f"  L_q = |m| × L₃ = 6 L₃")
    print(f"  For E_q = 612 m_e: L₃ = λ_C/3672 = {lambda_C/3672:.4e} m")
    print(f"                       = {lambda_C/3672*1e15:.3f} fm")
    print()

    proton_radius = 0.8751e-15  # m, charge radius
    print(f"Compare: proton charge radius = {proton_radius*1e15:.4f} fm")
    print(f"         L₃ = {lambda_C/3672*1e15:.3f} fm")
    print(f"         L₃/(2π) = {lambda_C/3672/2/math.pi*1e15:.4f} fm")
    print()

    # Check: does s = 1/6 give the electron's α?
    alpha_at_s16 = alpha_n1(r_e, s_exact, 2)
    print(f"But does s = 1/6 work for the ELECTRON?")
    print(f"  α(r=1, s=1/6, m=2) = {alpha_at_s16:.10f}")
    print(f"  α (actual)          = {alpha:.10f}")
    print(f"  Ratio:               {alpha_at_s16/alpha:.6f}")
    print()

    # What r gives α with s=1/6?
    def f_r_at_s16(r):
        return alpha_n1(r, s_exact, 2) - alpha

    r_scan = np.linspace(0.5, 10, 10000)
    for i in range(len(r_scan)-1):
        if f_r_at_s16(r_scan[i]) * f_r_at_s16(r_scan[i+1]) < 0:
            r_at_s16 = brentq(f_r_at_s16, r_scan[i], r_scan[i+1])
            print(f"  If s = 1/6, α = 1/137 requires r = {r_at_s16:.6f}")
            break

    print()

    # ── Section 6: Charge of the m=-6 quark ───────────────────
    print()
    print("SECTION 6: Charge of the m = −6 quark mode")
    print("-" * 72)
    print()
    print("For a (1, −6) mode in the (2,3) plane with shear s:")
    print("  q_eff = −6 − s")
    print("  Q ∝ sin(2πs) / (−6 − s)")
    print()
    print("The charge RATIO relative to the electron (1,2):")
    print("  Q_q/Q_e = |(2−s)/(−6−s)| × [normalization ratio]")
    print()
    print("The 'pure' ratio (ignoring normalization):")

    for s_test in [s_e, s_exact]:
        ratio_pure = abs((2 - s_test) / (-6 - s_test))
        print(f"  s = {s_test:.6f}: |Q_q/Q_e|_pure = {ratio_pure:.6f} "
              f"({ratio_pure:.4f} vs 1/3 = 0.3333, vs 2/3 = 0.6667)")
    print()

    print("The pure ratio gives ~0.30, which is close to 1/3 = 0.333")
    print("but ~10% off.  The normalization correction (different")
    print("plane geometry, different photon energy) could bridge")
    print("this gap — or the quark may be in a different mode.")
    print()

    # Check all m values for pure ratio closest to 1/3 and 2/3
    print("Pure charge ratios |(2−s)/(m−s)| for all m (s = {:.6f}):".format(s_e))
    print(f"{'m':>5s} | {'ratio':>10s} | {'closest to':>12s} | {'error':>10s}")
    print("-" * 45)
    for m in range(-10, 11):
        if m == 2:  # skip electron
            continue
        denom = m - s_e
        if abs(denom) < 1e-10:
            continue
        ratio = abs((2 - s_e) / denom)
        closest = min([(abs(ratio - 1/3), '1/3'), (abs(ratio - 2/3), '2/3')],
                      key=lambda x: x[0])
        if closest[0] < 0.15:
            print(f"{m:5d} | {ratio:10.6f} | {closest[1]:>12s} | "
                  f"{closest[0]:10.6f}")

    print()

    # ── Section 7: Assessment ─────────────────────────────────
    print()
    print("SECTION 7: Overall Assessment")
    print("=" * 72)
    print()
    print("1. n=1 CONSTRAINT: Only n=1 modes produce charge.")
    print("   Different charges must come from different m values.")
    print()
    print("2. SAME PLANE: RULED OUT. Integer m constraint cannot")
    print("   produce 1/3 and 2/3 ratios with physical s.")
    print()
    print("3. DIFFERENT PLANES: Charge formula is flexible enough")
    print("   for any target charge (different r per plane).")
    print()
    print("4. MASS CONSTRAINT IS SEVERE: Quarks sharing a")
    print("   circumference with the electron need (1+ms) ≈ 0")
    print("   to get the right geodesic length.  This requires")
    print("   m ≈ −1/s.  With s ≈ 0.165, m ≈ −6.")
    print()
    print("5. NEAR-MISS: s ≈ 1/6 (vs actual s_e = 0.165) would")
    print("   make (1+ms) = 0 exactly for m = −6.  The electron's")
    print("   self-consistent s at r=1 is 1% away from 1/6.")
    print()
    print("6. CHARGE RATIO: The pure charge ratio for m = −6 is")
    print("   ~0.30, close to 1/3 but 10% off.  Normalization")
    print("   corrections (different plane geometry) could help.")
    print()
    # ── Section 8: T³ consistency check ─────────────────────────
    print()
    print("SECTION 8: T³ circumference consistency")
    print("-" * 72)
    print()
    print("If both quarks are (1,−6) modes in different planes of T³")
    print("with s = 1/6 (so (1+ms) = 0 exactly), then:")
    print()
    print("  α_q = r_q² × sin²(π/3) / (4π × (37/6)² × 6)")
    print("      = r_q² / 3817")
    print()

    C_q = 0.75 / (4 * math.pi * (37/6)**2 * 6)
    print(f"  C_q = {C_q:.6e}  (so α_q = C_q × r_q²)")
    print()

    print("Up quark in (1,3) plane:  α_u = 4α/9 = {:.6e}".format(4*alpha/9))
    r13_sq = 4*alpha/9 / C_q
    r13 = math.sqrt(r13_sq)
    print(f"  r₁₃² = {r13_sq:.4f},  r₁₃ = L₁/L₃ = {r13:.4f}")
    print()

    print("Down quark in (2,3) plane: α_d = α/9 = {:.6e}".format(alpha/9))
    r23_sq = alpha/9 / C_q
    r23 = math.sqrt(r23_sq)
    print(f"  r₂₃² = {r23_sq:.4f},  r₂₃ = L₂/L₃ = {r23:.4f}")
    print()

    r12_from_quarks = r13 / r23
    print(f"Consistency: r₁₂ = r₁₃/r₂₃ = {r13:.4f}/{r23:.4f} = {r12_from_quarks:.4f}")
    print()

    # What r₁₂ does the electron need?
    print(f"But the electron requires:")
    print(f"  r₁₂ = 0.993 (for α = 1/137 at s = 1/6)")
    print()

    print(f"CONTRADICTION: quarks require r₁₂ = {r12_from_quarks:.1f},")
    print(f"               electron requires r₁₂ ≈ 1.0.")
    print()
    print(f"The factor-of-2 discrepancy is EXACT: it comes from")
    print(f"  α_u/α_d = (Q_u/Q_d)² = 4")
    print(f"  α_u/α_d = r₁₃²/r₂₃² = (L₁/L₂)² = r₁₂²")
    print(f"  So r₁₂ = 2 exactly.")
    print()
    print(f"This is a clean negative result for the uniform-shear")
    print(f"hypothesis with (1,−6) quarks in different planes.")
    print()
    print(f"NOTE: r₁₂ = 2 = the electron's poloidal winding number.")
    print(f"This coincidence may hint at a deeper connection, but")
    print(f"with the current charge formula, it conflicts with the")
    print(f"electron's r₁₂ ≈ 1 requirement.")
    print()

    print()
    print("SECTION 9: Overall Assessment")
    print("=" * 72)
    print()
    print("RESULTS:")
    print("  1. n=1 constraint: only n=1 modes produce charge.")
    print("  2. Same plane: RULED OUT (integer m impossible).")
    print("  3. Mass constraint: quarks need m ≈ −1/s ≈ −6.")
    print("  4. s ≈ 1/6 near-miss: electron's s is 1% from 1/6,")
    print("     which would make m = −6 exact. L₃ ≈ 0.66 fm.")
    print("  5. Charge pure ratio at m = −6: ~0.30 (vs 1/3 target).")
    print("  6. T³ consistency: uniform shear requires r₁₂ = 2 from")
    print("     quarks but r₁₂ ≈ 1 from electron. RULED OUT.")
    print()
    print("INTERPRETATION:")
    print("  The uniform-shear Track 4 hypothesis fails, but it")
    print("  produces several tantalizing near-misses:")
    print("    • s ≈ 1/6 (1% off)")
    print("    • charge ratio ≈ 0.30 (10% from 1/3)")
    print("    • L₃ ≈ 0.66 fm (order of proton radius)")
    print("    • r₁₂ = 2 (the electron's own winding number)")
    print()
    print("  These suggest the correct mechanism is CLOSE to this")
    print("  picture but requires a modification:")
    print("    → Track 5: non-uniform shear (different s per plane)")
    print("    → Track 6: linking modifies the charge formula")
    print("    → Alternative winding assignments")


if __name__ == "__main__":
    main()
