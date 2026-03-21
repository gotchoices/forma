#!/usr/bin/env python3
"""
R20 Track 1: Harmonic spectrum and charge on sheared T².

QUESTION
========
The proton is modeled as the electron's (1,2) fundamental mode plus
higher harmonics — additional modes that add mass but not charge.

1. What are the energies of the (n, 2n) harmonics?
2. Do they carry zero charge (as predicted by F30)?
3. What harmonic sums reproduce the proton mass (1836 m_e)?
4. Are there convergent infinite series that reach the target?

SETUP
=====
On sheared T² with aspect ratio r = L₂/L₁ and shear s₁₂:

- Lattice vectors: a₁ = L₁ ê_x,  a₂ = s₁₂ L₁ ê_x + L₂ ê_y
- Reciprocal vectors: b₁ = (2π/L₁, -2πs/L₂),  b₂ = (0, 2π/L₂)
- Mode (n₁, n₂) wavevector: k = n₁ b₁ + n₂ b₂
- Energy: E = ℏc|k| = hc √((n₁/L₁)² + ((n₂ - n₁s)/L₂)²)

The (n, 2n) mode has wavevector k = n × k(1,2), so E(n,2n) = n × m_e.

Charge formula (R19): only modes with n₁ = ±1 carry charge.
For n₁ = 1:  Q ∝ sin(2πs₁₂) / (n₂ - s₁₂)
For n₁ = -1: Q ∝ -sin(2πs₁₂) / (n₂ + s₁₂)
For |n₁| ≥ 2: Q = 0 (the θ₁ integral kills them)
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C

m_p = 1.67262192369e-27  # proton mass (kg)
m_n = 1.67492749804e-27  # neutron mass (kg)
mass_ratio_pe = m_p / m_e  # 1836.15267...
mass_ratio_ne = m_n / m_e  # 1838.68366...


def alpha_mode_2d(r, s, m):
    """Self-consistent α for (1,m) on T² (from R19 Track 3)."""
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


def charge_integral_2d(n1, n2, s12):
    """
    Charge integral for mode (n₁, n₂) on sheared T².

    Returns I ∝ Q/Q_e (unnormalized).
    Zero for |n₁| ≠ 1.  For n₁ = ±1, the effective winding
    q₂ = n₂ - n₁ s₁₂ determines the charge.
    """
    if abs(n1) != 1:
        return 0.0
    q2 = n2 - n1 * s12
    if abs(q2) < 1e-12:
        return float('inf')
    sign = 1 if n1 == 1 else -1
    return sign * math.sin(2 * math.pi * s12) / q2


def energy_ratio_momentum(n1, n2, r, s):
    """
    E(n₁,n₂) / E(1,2) in the momentum picture.

    E = ℏc|k| where k = n₁b₁ + n₂b₂.
    """
    num = math.sqrt(n1**2 + ((n2 - n1 * s) / r)**2)
    den = math.sqrt(1 + ((2 - s) / r)**2)
    return num / den


def energy_ratio_winding(n1, n2, r, s):
    """
    E(n₁,n₂) / E(1,2) in the winding picture.

    E = hc/L_geodesic, L = √((L₁(n₁+n₂s))² + (n₂L₂)²).
    """
    L_e = math.sqrt((1 + 2 * s)**2 + (2 * r)**2)
    L_mode = math.sqrt((n1 + n2 * s)**2 + (n2 * r)**2)
    if L_mode < 1e-30:
        return float('inf')
    return L_e / L_mode


def main():
    print("=" * 72)
    print("R20 Track 1: Harmonic Spectrum and Charge on Sheared T²")
    print("=" * 72)
    print()

    r = 1.0
    s = solve_electron_s(r)
    print(f"Electron geometry: r = {r}, s₁₂ = {s:.8f}")
    print(f"  q_eff = 2 - s = {2 - s:.8f}")
    print(f"  α(model) = {alpha_mode_2d(r, s, 2):.10e}")
    print(f"  α(CODATA) = {alpha:.10e}")
    print(f"  m_p/m_e = {mass_ratio_pe:.5f}")
    print(f"  m_n/m_e = {mass_ratio_ne:.5f}")
    print()

    I_e = charge_integral_2d(1, 2, s)
    print(f"Electron charge integral: I_e = {I_e:.8f}")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 1: Energy and charge of (n, 2n) harmonics")
    print("=" * 72)
    print()
    print("The (n, 2n) mode is the nth multiple of the electron's wavevector.")
    print("In the momentum picture, E(n,2n) = n × m_e.")
    print("In the winding picture, E(n,2n) = m_e / n.")
    print()

    print(f"{'n':>4}  {'mode':>10}  {'E/m_e(mom)':>12}  {'E/m_e(wind)':>12}  "
          f"{'Q/Q_e':>8}  {'n₁':>4}")
    print("-" * 72)

    for n in range(1, 21):
        n1, n2 = n, 2 * n
        E_mom = energy_ratio_momentum(n1, n2, r, s)
        E_wind = energy_ratio_winding(n1, n2, r, s)
        I = charge_integral_2d(n1, n2, s)
        Q_ratio = I / I_e if abs(I_e) > 1e-12 else 0.0
        print(f"{n:4d}  ({n1:3d},{n2:3d})  {E_mom:12.6f}  {E_wind:12.6f}  "
              f"{Q_ratio:8.4f}  {n1:4d}")

    print()
    print("KEY RESULT: For n ≥ 2, Q/Q_e = 0 exactly (n₁ = n ≠ ±1).")
    print("The momentum-picture energy is exactly n × m_e.")
    print("The winding-picture energy is m_e / n (gets lighter, not heavier).")
    print()
    print("For building a heavier proton, we need the MOMENTUM picture")
    print("(harmonics get heavier).  This is the standard QFT result for")
    print("a massless field on a flat torus: E = ℏc|k|.")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 2: Charged modes — the full (n₁=±1) spectrum")
    print("=" * 72)
    print()
    print("Only modes with n₁ = ±1 carry charge.")
    print("Positive n₁ = +1 modes carry the same sign as the electron.")
    print("Negative n₁ = -1 modes carry the opposite sign (anti-particles).")
    print()

    print(f"{'mode':>10}  {'E/m_e':>10}  {'Q/Q_e':>8}  {'type':>12}")
    print("-" * 60)

    charged_modes = []
    for n2 in range(-6, 7):
        for n1_sign in [1, -1]:
            n1 = n1_sign
            E = energy_ratio_momentum(n1, n2, r, s)
            I = charge_integral_2d(n1, n2, s)
            Q = I / I_e if abs(I_e) > 1e-12 else 0.0
            if n1 == 1 and n2 == 2:
                label = "← electron"
            elif n1 == -1 and n2 == -2:
                label = "← positron"
            elif abs(Q) > 0.99 and abs(Q) < 1.01:
                label = "Q ≈ ±e"
            else:
                label = ""
            charged_modes.append((n1, n2, E, Q))
            print(f"({n1:+2d},{n2:+2d})    {E:10.4f}  {Q:+8.4f}  {label:>12}")

    print()
    print("NOTE: The (-1,-2) mode has Q/Q_e = -1.000 exactly.")
    print("This is the CPT conjugate of the electron (positron).")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 3: General uncharged mode catalog")
    print("=" * 72)
    print()
    print("Any mode with |n₁| ≠ 1 is uncharged.  These are candidates")
    print("for adding mass to the proton without affecting charge.")
    print()

    print(f"{'mode':>10}  {'E/m_e(mom)':>12}  {'notes':>30}")
    print("-" * 60)

    uncharged = []
    for n1 in range(-5, 6):
        for n2 in range(-5, 6):
            if abs(n1) == 1 or (n1 == 0 and n2 == 0):
                continue
            E = energy_ratio_momentum(n1, n2, r, s)
            if E < 10:
                uncharged.append((n1, n2, E))

    uncharged.sort(key=lambda x: x[2])
    for n1, n2, E in uncharged[:30]:
        note = ""
        if n2 != 0 and n1 != 0 and n2 / n1 == 2:
            note = f"← harmonic #{n1}"
        elif n1 == 0:
            note = "← pure θ₂ mode"
        print(f"({n1:+2d},{n2:+2d})    {E:12.4f}  {note:>30}")

    print()
    print(f"Total uncharged modes with E < 10 m_e: {len(uncharged)}")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 4: Proton mass from harmonic sums")
    print("=" * 72)
    print()

    target = mass_ratio_pe
    print(f"Target: m_p/m_e = {target:.5f}")
    print()

    # --- 4a: Complete harmonic series (momentum picture) ---
    print("4a. Complete series: Σ_{n=1}^{N} n = N(N+1)/2")
    print("-" * 40)
    best_N = None
    best_err = float('inf')
    for N in range(1, 200):
        total = N * (N + 1) / 2
        err = abs(total - target)
        if err < best_err:
            best_err = err
            best_N = N
        if N <= 65 and N >= 55:
            print(f"  N = {N:3d}:  Σ = {total:8.0f}  "
                  f"(Δ = {total - target:+8.2f} m_e)")
    print(f"  Best: N = {best_N}, Σ = {best_N*(best_N+1)/2:.0f}, "
          f"Δ = {best_N*(best_N+1)/2 - target:+.2f} m_e")
    print()

    uncharged_target = target - 1  # harmonics (n ≥ 2) must provide this

    # --- 4b: Harmonic sum excluding fundamental ---
    print("4b. Harmonics only (n ≥ 2): Σ_{n=2}^{N} n = N(N+1)/2 - 1")
    print("    (fundamental already contributes 1 m_e of the proton mass)")
    print("-" * 40)
    for N in range(55, 66):
        total = N * (N + 1) / 2 - 1
        print(f"  N = {N:3d}:  Σ = {total:8.0f}  "
              f"(Δ = {total - uncharged_target:+8.2f} m_e)")
    print()

    # --- 4c: Thermal / Bose-Einstein distribution ---
    print("4c. Thermal (Bose-Einstein) distribution")
    print("    f(n) = 1/(exp(n/T) - 1),  Σ n × f(n) = total mass")
    print("-" * 40)

    def thermal_mass(T):
        total = 0.0
        for n in range(1, 10000):
            x = n / T
            if x > 500:
                break
            total += n / (math.exp(x) - 1)
        return total

    def thermal_charge(T, s12, I_e):
        """Charge contribution from thermal distribution of (n, 2n) modes."""
        total_I = 0.0
        for n in range(1, 10000):
            x = n / T
            if x > 500:
                break
            f_n = 1.0 / (math.exp(x) - 1)
            I_n = charge_integral_2d(n, 2 * n, s12)
            total_I += f_n * I_n
        return total_I / I_e if abs(I_e) > 1e-12 else 0.0

    T_values = np.linspace(5, 60, 200)
    masses = [thermal_mass(T) for T in T_values]

    T_proton = None
    for i in range(len(masses) - 1):
        if (masses[i] - target) * (masses[i + 1] - target) < 0:
            T_proton = brentq(lambda T: thermal_mass(T) - target,
                              T_values[i], T_values[i + 1])
            break

    if T_proton:
        m_thermal = thermal_mass(T_proton)
        q_thermal = thermal_charge(T_proton, s, I_e)
        f1 = 1.0 / (math.exp(1.0 / T_proton) - 1)
        print(f"  Temperature for m_p: T = {T_proton:.4f} m_e "
              f"({T_proton * m_e * c**2 / 1.602e-13:.2f} MeV)")
        print(f"  Thermal mass sum: {m_thermal:.4f} m_e")
        print(f"  Thermal charge sum (Q/Q_e): {q_thermal:.6f}")
        print(f"  Occupation of fundamental: f(1) = {f1:.2f}")
        print()
        print("  *** PROBLEM: f(1) ≈ {:.0f} means ~{:.0f} copies of the".format(
            f1, f1))
        print("  charged fundamental.  Total charge ≈ {:.0f}e, not e.".format(f1))
        print("  A pure thermal distribution DOES NOT preserve Q = e.")
        print()

        print("  Occupation numbers f(n) for key harmonics:")
        for n in [1, 2, 3, 5, 10, 20, 50, 100]:
            x = n / T_proton
            f_n = 1 / (math.exp(x) - 1) if x < 500 else 0
            E_contrib = n * f_n
            print(f"    n = {n:3d}: f(n) = {f_n:.4f}, "
                  f"energy contribution = {E_contrib:.2f} m_e")
        print()

        n_eff = sum(1 / (math.exp(n / T_proton) - 1)
                    for n in range(1, 10000)
                    if n / T_proton < 500)
        print(f"  Effective number of excited modes: {n_eff:.1f}")
        print(f"  Highest significantly occupied harmonic: ", end="")
        for n in range(10000, 0, -1):
            if n / T_proton < 500 and 1 / (math.exp(n / T_proton) - 1) > 0.01:
                print(f"n ≈ {n}")
                break
    else:
        print("  Could not find thermal T for proton mass.")
    print()

    # --- 4c-bis: Corrected thermal — f(1) = 1 exactly ---
    print("4c′. Corrected thermal: f(1) = 1, f(n≥2) = 1/(e^{n/T'}-1)")
    print("     Total mass = 1 + Σ_{n≥2} n/(e^{n/T'}-1)")
    print("-" * 40)

    def thermal_mass_n2plus(T):
        total = 0.0
        for n in range(2, 10000):
            x = n / T
            if x > 500:
                break
            total += n / (math.exp(x) - 1)
        return total

    target_n2 = target - 1  # uncharged harmonics must provide 1835.15 m_e
    T_values2 = np.linspace(5, 60, 500)
    masses2 = [thermal_mass_n2plus(T) for T in T_values2]

    T_corrected = None
    for i in range(len(masses2) - 1):
        if (masses2[i] - target_n2) * (masses2[i + 1] - target_n2) < 0:
            T_corrected = brentq(lambda T: thermal_mass_n2plus(T) - target_n2,
                                 T_values2[i], T_values2[i + 1])
            break

    if T_corrected:
        m_corr = thermal_mass_n2plus(T_corrected) + 1
        print(f"  T' for m_p: {T_corrected:.4f} m_e "
              f"({T_corrected * m_e * c**2 / 1.602e-13:.2f} MeV)")
        print(f"  Total mass: 1 + {thermal_mass_n2plus(T_corrected):.4f} "
              f"= {m_corr:.4f} m_e")
        print(f"  Total charge: exactly e (by construction)")
        print()
        print("  Occupation of uncharged harmonics:")
        for n in [2, 3, 5, 10, 20, 50, 100]:
            x = n / T_corrected
            f_n = 1 / (math.exp(x) - 1) if x < 500 else 0
            E_contrib = n * f_n
            print(f"    n = {n:3d}: f(n) = {f_n:.4f}, "
                  f"energy = {E_contrib:.2f} m_e")
    else:
        print("  Could not find T' for corrected thermal distribution.")
    print()

    # --- 4d: Power-law cutoff series ---
    print("4d. Power-law cutoff: f(n) = 1 for n ≤ N, else 0")
    print("    What partial sum matches best?")
    print("-" * 40)

    # Find combinations of harmonics summing to target
    # N(N+1)/2 ≈ 1836.15 → N ≈ 60.2 (not integer)
    N_low = 60
    sum_low = N_low * (N_low + 1) / 2  # 1830
    deficit = target - sum_low
    print(f"  Σ(1..60) = {sum_low:.0f}, deficit = {deficit:.2f} m_e")
    print(f"  Σ(1..61) = {N_low * (N_low + 2) / 2 + 30.5:.0f}, "
          f"excess = {61*62/2 - target:.2f} m_e")
    print()
    print(f"  The deficit {deficit:.2f} m_e could come from:")
    print(f"    - A partial occupation of the n=61 harmonic")
    print(f"    - A few uncharged modes from the general catalog")
    print(f"    - Shear corrections to the exact harmonic energies")
    print()

    # --- 4e: Geometric series ---
    print("4e. Geometric series: f(n) = x^(n-1), Σ_{n≥2} n x^(n-1)")
    print("    (uncharged harmonics only, f(1) = 1 for fundamental)")
    print("-" * 40)

    def geometric_mass_n2plus(x):
        if abs(x) >= 1:
            return float('inf')
        # Σ_{n=2}^∞ n x^(n-1) = d/dx[Σ x^n from n=2] = d/dx[x²/(1-x)]
        # = (2x(1-x) + x²)/(1-x)² = x(2-x)/(1-x)²
        return x * (2 - x) / (1 - x)**2

    x_proton = brentq(lambda x: geometric_mass_n2plus(x) - uncharged_target,
                       0.5, 0.9999)
    m_geom = geometric_mass_n2plus(x_proton)
    print(f"  x for uncharged mass = {uncharged_target:.2f}: x = {x_proton:.8f}")
    print(f"  Uncharged mass: {m_geom:.4f} m_e")
    print(f"  Total mass (1 + uncharged): {1 + m_geom:.4f} m_e")
    print(f"  Total charge: exactly e")
    print(f"  Convergence: |x| < 1, series converges ✓")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 5: Energy formula — momentum vs winding")
    print("=" * 72)
    print()
    print("Two energy formulas give opposite predictions for harmonics:")
    print()
    print("  Momentum (QFT): E(n,2n) = n × m_e  → harmonics are HEAVIER")
    print("  Winding (R13):  E(n,2n) = m_e / n  → harmonics are LIGHTER")
    print()

    E_mom_1 = energy_ratio_momentum(1, 2, r, s)
    E_wind_1 = energy_ratio_winding(1, 2, r, s)
    print(f"For the electron (1,2):")
    print(f"  E_momentum / m_e = {E_mom_1:.6f}  (should be 1.0 by definition)")
    print(f"  E_winding / m_e  = {E_wind_1:.6f}  (also 1.0 — both normalized)")
    print()
    print("The two agree for the electron because we set L_geo = λ_C or")
    print("|k| = m_e c/ℏ, respectively.  But they DIFFER for other modes")
    print("when the mode direction doesn't coincide with the geodesic.")
    print()
    print("For (n, 2n) harmonics, the wavevector direction IS the same")
    print("as (1,2), so k(n,2n) = n × k(1,2) and E_mom = n × m_e.")
    print("But L_geo(n,2n) = n × L_geo(1,2), so E_wind = m_e / n.")
    print()
    print("The momentum picture (E = ℏc|k|) is standard for quantum fields.")
    print("The winding picture (E = hc/L) applies to strings, not fields.")
    print("For a photon (field), the momentum picture should be correct.")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 6: Oscillation structure along the geodesic")
    print("=" * 72)
    print()
    print("How many wavelengths does each mode have per geodesic traversal?")
    print("For mode (n₁, n₂), the projected wavevector along the (1,2)")
    print("geodesic gives k_‖ = 2π(n₁ + 2n₂) / L_geo.")
    print("Number of wavelengths per traversal = n₁ + 2n₂.")
    print()

    print(f"{'mode':>10}  {'n₁+2n₂':>8}  {'E/m_e':>10}  {'Q/Q_e':>8}")
    print("-" * 50)
    for n in range(1, 11):
        n1, n2 = n, 2 * n
        osc = n1 + 2 * n2
        E = energy_ratio_momentum(n1, n2, r, s)
        I = charge_integral_2d(n1, n2, s)
        Q = I / I_e if abs(I_e) > 1e-12 else 0.0
        print(f"({n1:2d},{n2:2d})    {osc:8d}  {E:10.4f}  {Q:+8.4f}")

    print()
    print("The electron (1,2) oscillates 5 times per traversal.")
    print("The (n,2n) mode oscillates 5n times.  These are the 5th, 10th,")
    print("15th, ... harmonics of the geodesic, not the 1st, 2nd, 3rd.")
    print()
    print("The TRUE fundamental of the (1,2) geodesic (1 wavelength per")
    print("traversal) requires n₁ + 2n₂ = 1, e.g., mode (1,0) or (-1,1).")
    print("But these are different T² eigenmodes, not (n,2n) harmonics.")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 7: Summary and assessment")
    print("=" * 72)
    print()
    print("ESTABLISHED RESULTS:")
    print()
    print("F1. The (n, 2n) harmonics have E = n × m_e (momentum picture)")
    print("    and Q = 0 for n ≥ 2 (exact, by the n₁ selection rule).")
    print("    Adding harmonics adds mass without charge.")
    print()
    print("F2. The charge of the (-1,-2) mode (CPT conjugate) is exactly")
    print("    −Q_electron.  Opposite-charge modes exist on the torus.")
    print()
    print("F3. A pure thermal distribution of (n, 2n) modes CANNOT model")
    print("    the proton: f(1) ≈ 33 means ~33 copies of the charged")
    print("    fundamental, giving Q ≈ 33e.  The charge constraint")
    print("    requires f(1) = 1 exactly (one charged quantum).")
    print()
    print("F4. With f(1) = 1 fixed, multiple uncharged spectra (n ≥ 2)")
    print("    can reproduce the remaining 1835 m_e:")
    if T_corrected:
        print(f"    - Corrected thermal at T' ≈ {T_corrected:.1f} m_e (convergent)")
    print(f"    - Complete series n=1..60 gives 1830 m_e (deficit {deficit:.1f})")
    print(f"    - Geometric series with x ≈ {x_proton:.4f} (convergent)")
    print("    The specific distribution is underdetermined without a")
    print("    selection mechanism.")
    print()
    print("F5. The momentum and winding energy formulas give opposite")
    print("    predictions: harmonics are HEAVIER (momentum) vs LIGHTER")
    print("    (winding).  The momentum picture (standard QFT) is needed")
    print("    for building a heavy proton from harmonics.")
    print()
    print("OPEN QUESTIONS:")
    print()
    print("- What physical mechanism selects the harmonic spectrum?")
    print("- Is the momentum picture correct for a photon on a torus?")
    print("  (R13/R19 used the winding picture for the electron.)")
    print("- What stabilizes the harmonic composite against decay?")
    print("- How does the harmonic proton scatter in DIS?")
    print()


if __name__ == "__main__":
    main()
