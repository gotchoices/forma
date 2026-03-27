#!/usr/bin/env python3
"""
R33 Track 8: Wave-optics coupling through the shear aperture.

The shear s creates a physical displacement δ = s × L₂ between
adjacent lattice rows on the T².  This displacement is the "aperture"
through which compact modes radiate into R³.

Track 1 used a geometric (Fourier) charge integral:
    Q ∝ sin(2πs) / (n₂ - s)
which ENHANCES low-n₂ modes.

This track tests whether a wave-optics treatment — where the aperture
δ is sub-wavelength — gives a different scaling.

THREE MODELS ARE COMPARED:

1. Geometric (Track 1): Q² ∝ 1/(n₂ - s)²
   → Low n₂ enhanced, (1,1) at 2× electron

2. Bethe aperture (d/λ)⁴: Q² ∝ (s·n₂)⁴
   → Low n₂ suppressed, (1,1) at 1/16× electron

3. 2D cavity radiation: solve for the radiated power from a
   rectangular cavity with a sub-wavelength slit, mode by mode.
"""

import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.t6 import solve_shear_for_alpha, alpha_kk, ALPHA


def geometric_coupling(n2, s):
    """Track 1 geometric charge integral: Q² ∝ sin²(2πs)/(n₂-s)²."""
    q = n2 - s
    if abs(q) < 1e-12:
        return float('inf')
    return math.sin(2 * math.pi * s)**2 / q**2


def bethe_coupling(n2, s):
    """
    Bethe sub-wavelength aperture: transmission ∝ (d/λ)⁴.

    Aperture: d = s × L₂
    Ring wavelength of mode (1, n₂): λ_ring = L₂/|n₂|

    d/λ = s × |n₂|

    T ∝ (s × |n₂|)⁴
    """
    if n2 == 0:
        return 0.0
    return (s * abs(n2))**4


def cavity_slit_radiation(n2, s, r, n_terms=200):
    """
    2D cavity with sub-wavelength slit radiating into free space.

    Model: a rectangular cavity of dimensions L₁ × L₂ (aspect ratio r)
    with a slit of width δ = s × L₂ along one edge.  A mode (1, n₂)
    oscillates inside.  The field at the slit determines the radiated
    power.

    The slit samples the mode's field over an arc of angular width
    Δθ = 2πs on the ring.  The overlap integral is:

        A(n₂, s) = ∫₀^{2πs} cos(n₂ θ) dθ = sin(2π s n₂) / n₂

    The radiated power is proportional to |A|² times the radiation
    impedance of the slit.  For a sub-wavelength slit of width d
    radiating into 3D, the impedance scales as (kd)² where
    k = 2π/λ_free is the free-space wavevector.

    Combined: P ∝ |A|² × (k_free × d)²

    For the compact mode, λ_free = c/f = (L₂/n₂) × (L₂/L_mode),
    but we're radiating into R³ where the free-space wavelength is
    λ = 2πℏc/E = λ̄_C.  The mode energy sets k_free.

    The key insight: the slit overlap A(n₂, s) already contains the
    sub-wavelength physics.  For small s:

        A(n₂, s) = sin(2πsn₂)/n₂ ≈ 2πs  (for sn₂ << 1)

    This is INDEPENDENT of n₂ when sn₂ << 1 — all sub-wavelength
    modes couple equally through the slit!

    For sn₂ ~ 1 (wavelength comparable to slit), the coupling has
    oscillatory structure.
    """
    if n2 == 0:
        return 0.0

    overlap = math.sin(2 * math.pi * s * abs(n2)) / abs(n2)

    mu = math.sqrt(1.0 / r**2 + (n2 - s)**2)
    k_delta = 2 * math.pi * mu * s

    return overlap**2 * k_delta**2


def dipole_radiation_model(n2, s, r):
    """
    Treat the slit as an oscillating dipole driven by the cavity mode.

    The cavity mode (1, n₂) produces a time-varying field at the slit.
    The dipole moment of the slit is:

        p ∝ δ × E_slit

    where δ = s L₂ is the slit width and E_slit is the field amplitude
    at the slit location.

    For a standing wave with n₂ half-wavelengths around the ring,
    the field at a slit centered at θ = 0 is:

        E_slit = E₀ cos(0) = E₀  (for all n₂, if slit is at antinode)

    But the slit averages the field over width δ:

        <E> = (1/δ) ∫₀^δ E₀ cos(n₂ × 2πx/L₂) dx
            = E₀ × sin(πsn₂) / (πsn₂)    [sinc function]

    The dipole moment: p ∝ δ × <E> = s L₂ × E₀ × sinc(πsn₂)

    Radiated power from an oscillating dipole at frequency ω:
        P ∝ ω⁴ |p|²  (Larmor formula)

    ω ∝ mode energy μ(1, n₂)

    Total: P ∝ μ⁴ × s² × sinc²(πsn₂)
    """
    if n2 == 0:
        return 0.0

    mu = math.sqrt(1.0 / r**2 + (n2 - s)**2)

    x = math.pi * s * abs(n2)
    if abs(x) < 1e-12:
        sinc = 1.0
    else:
        sinc = math.sin(x) / x

    return mu**4 * s**2 * sinc**2


def main():
    r = 6.6
    s = solve_shear_for_alpha(r)

    print("=" * 78)
    print("R33 Track 8: Wave-Optics Coupling Through the Shear Aperture")
    print("=" * 78)
    print()
    print(f"Parameters: r = {r}, s = {s:.8f}")
    print(f"Aperture: δ/L₂ = s = {s:.5f}  (~1% of ring circumference)")
    print()

    print("─" * 78)
    print("SECTION 1: Four coupling models compared")
    print("─" * 78)
    print()

    ref_geo = geometric_coupling(2, s)
    ref_bethe = bethe_coupling(2, s)
    ref_cavity = cavity_slit_radiation(2, s, r)
    ref_dipole = dipole_radiation_model(2, s, r)

    print(f"{'n₂':>4s} | {'Geometric':>12s} | {'Bethe (d/λ)⁴':>12s} | "
          f"{'Cavity-slit':>12s} | {'Dipole+sinc':>12s} | "
          f"{'λ_ring/δ':>10s} | {'WvM Spin':>12s}")
    print(f"     | {'(Track 1)':>12s} | {'':>12s} | "
          f"{'':>12s} | {'':>12s} | {'':>10s} |")
    print(f"  {'─' * 90}")

    for n2 in range(-8, 9):
        if n2 == 0:
            geo = float('inf')
        else:
            geo = geometric_coupling(n2, s)
        bethe = bethe_coupling(n2, s)
        cavity = cavity_slit_radiation(n2, s, r)
        dipole = dipole_radiation_model(n2, s, r)

        geo_r = geo / ref_geo if ref_geo > 0 and geo < 1e30 else float('inf')
        bethe_r = bethe / ref_bethe if ref_bethe > 0 else 0
        cavity_r = cavity / ref_cavity if ref_cavity > 0 else 0
        dipole_r = dipole / ref_dipole if ref_dipole > 0 else 0

        if abs(n2) > 0:
            lambda_ratio = 1.0 / (s * abs(n2))
        else:
            lambda_ratio = float('inf')

        spin_val = abs(1.0 / n2) if n2 != 0 else None
        if spin_val is None:
            spin_str = "undefined"
        elif abs(spin_val - 0.5) < 0.01:
            spin_str = "½ ✓"
        elif abs(spin_val - 1.0) < 0.01:
            spin_str = "1 ✓"
        elif abs(spin_val - round(spin_val)) < 0.01:
            spin_str = f"{int(round(spin_val))} ✓"
        else:
            spin_str = f"1/{abs(n2)} ✗"

        marker = ""
        if n2 == 2:
            marker = " ← ELECTRON"
        elif n2 == -2:
            marker = " ← anti-e"

        if geo_r > 1e10:
            geo_s = "    ∞      "
        else:
            geo_s = f"{geo_r:12.4f}"

        print(f"  {n2:+3d} | {geo_s} | {bethe_r:12.4f} | "
              f"{cavity_r:12.4f} | {dipole_r:12.4f} | "
              f"{lambda_ratio:10.1f} | {spin_str:>12s}{marker}")

    print()
    print("─" * 78)
    print("SECTION 2: Focus on the critical modes")
    print("─" * 78)
    print()

    critical = [
        (1, "(1,1) ghost boson"),
        (-1, "(1,-1) ghost boson"),
        (2, "(1,2) ELECTRON"),
        (-2, "(1,-2) anti-electron"),
        (3, "(1,3) [spin-killed]"),
        (4, "(1,4) [spin-killed]"),
    ]

    for n2, desc in critical:
        geo_r = geometric_coupling(n2, s) / ref_geo
        bethe_r = bethe_coupling(n2, s) / ref_bethe
        cavity_r = cavity_slit_radiation(n2, s, r) / ref_cavity
        dipole_r = dipole_radiation_model(n2, s, r) / ref_dipole
        mu = math.sqrt(1.0 / r**2 + (n2 - s)**2)
        mu_e = math.sqrt(1.0 / r**2 + (2 - s)**2)
        mass_ratio = mu / mu_e

        print(f"  {desc}:")
        print(f"    Mass = {mass_ratio:.3f} m_e")
        print(f"    Geometric (Track 1): {geo_r:.4f}× electron coupling")
        print(f"    Bethe (d/λ)⁴:        {bethe_r:.4f}× electron coupling")
        print(f"    Cavity-slit:         {cavity_r:.4f}× electron coupling")
        print(f"    Dipole+sinc:         {dipole_r:.4f}× electron coupling")
        print()

    print("─" * 78)
    print("SECTION 3: Scaling law analysis")
    print("─" * 78)
    print()
    print("How does coupling scale with n₂ for each model?")
    print("Fit: log(coupling) = β × log(|n₂|) + const")
    print()

    for model_name, model_fn, ref in [
        ("Geometric", geometric_coupling, ref_geo),
        ("Bethe", bethe_coupling, ref_bethe),
        ("Cavity-slit", cavity_slit_radiation, ref_cavity),
        ("Dipole+sinc", dipole_radiation_model, ref_dipole),
    ]:
        n2_vals = [2, 3, 4, 5, 6, 7, 8]
        if model_name == "Cavity-slit":
            ratios = [model_fn(n2, s, r) / ref for n2 in n2_vals]
        elif model_name == "Dipole+sinc":
            ratios = [model_fn(n2, s, r) / ref for n2 in n2_vals]
        else:
            ratios = [model_fn(n2, s) / ref for n2 in n2_vals]

        log_n = np.log(np.array(n2_vals, dtype=float))
        log_r = np.log(np.array(ratios, dtype=float))
        beta, intercept = np.polyfit(log_n, log_r, 1)

        print(f"  {model_name:15s}: β = {beta:+.2f}  "
              f"(coupling ∝ n₂^{beta:.2f})")

    print()
    print("─" * 78)
    print("SECTION 4: The sinc structure — natural cutoff?")
    print("─" * 78)
    print()
    print("The dipole model has a sinc²(πsn₂) factor.  The first zero")
    print("of sinc is at πsn₂ = π, i.e., n₂ = 1/s.")
    print(f"  First sinc zero at n₂ = 1/s = {1/s:.1f}")
    print(f"  This is far above the relevant range (n₂ ≤ 8).")
    print()
    print("For small argument (πsn₂ << 1), sinc ≈ 1 - (πsn₂)²/6:")
    for n2 in [1, 2, 3, 4, 5, 8]:
        x = math.pi * s * n2
        sinc_val = math.sin(x) / x if abs(x) > 1e-12 else 1.0
        correction = 1 - x**2/6
        print(f"  n₂ = {n2}: sinc(πs×{n2}) = {sinc_val:.8f}  "
              f"(1 - correction = {1 - sinc_val:.2e})")

    print()
    print("The sinc correction is negligible (~10⁻⁴) for all relevant")
    print("modes.  The sinc does NOT provide a cutoff in the low-n₂ range.")

    print()
    print("─" * 78)
    print("SECTION 5: What does the ω⁴ factor do?")
    print("─" * 78)
    print()
    print("The dipole model includes P ∝ ω⁴ (Larmor radiation).")
    print("Mode energy μ(1, n₂) = √(1/r² + (n₂-s)²):")
    print()
    mu_e = math.sqrt(1.0 / r**2 + (2 - s)**2)
    for n2 in [-2, -1, 0, 1, 2, 3, 4, 5, 8]:
        mu = math.sqrt(1.0 / r**2 + (n2 - s)**2)
        mu4_ratio = (mu / mu_e)**4
        print(f"  n₂ = {n2:+2d}: μ = {mu:.4f}, "
              f"(μ/μ_e)⁴ = {mu4_ratio:.4f}")
    print()
    print("The ω⁴ factor STRONGLY suppresses low-n₂ modes:")
    print(f"  (1,1): (μ/μ_e)⁴ = {(math.sqrt(1/r**2+(1-s)**2)/mu_e)**4:.4f}")
    print(f"  (1,0): (μ/μ_e)⁴ = {(math.sqrt(1/r**2+s**2)/mu_e)**4:.4f}")
    print()
    print("THIS is the key suppression mechanism in the dipole model.")
    print("Lower-energy modes radiate less efficiently because P ∝ ω⁴.")

    print()
    print("=" * 78)
    print("KEY FINDINGS")
    print("=" * 78)
    print(f"""
F9.  The sinc aperture effect is negligible.  For s ≈ 0.01 and
     n₂ ≤ 8, the argument πsn₂ ≤ 0.26, giving sinc ≈ 0.989.
     The aperture is so much smaller than all mode wavelengths that
     it treats them all equally — no wavelength selectivity.

F10. The ω⁴ Larmor factor provides STRONG low-n₂ suppression.
     In the dipole radiation model, P ∝ μ(n₂)⁴.  Since μ(1,1) ≈ 1.0
     and μ(1,2) ≈ 2.0, the ratio is:

         P(1,1)/P(1,2) ∝ (1.0/2.0)⁴ = 1/16 = 0.063

     The (1,1) ghost radiates 16× less power than the electron,
     purely from the frequency dependence of dipole radiation.

F11. Combining sinc and ω⁴ in the dipole model:

         α_eff(1,1)/α_eff(1,2) ≈ 0.063  (dipole model)

     Compare to Track 1:
         α_eff(1,1)/α_eff(1,2) ≈ 2.03   (geometric integral)

     The two models disagree by a factor of ~32.  The dipole model
     says the (1,1) ghost is 16× WEAKER than the electron, not 2×
     stronger.

F12. The scaling exponents differ dramatically:

         Geometric:    coupling ∝ n₂^{{-2}}  (low n₂ enhanced)
         Bethe:        coupling ∝ n₂^{{+4}}  (low n₂ suppressed)
         Cavity-slit:  coupling ∝ n₂^{{+2}}  (low n₂ suppressed)
         Dipole+sinc:  coupling ∝ n₂^{{+4}}  (low n₂ suppressed)

     Three of four models show LOW-n₂ suppression.  The geometric
     integral is the outlier — it ignores the radiation physics
     (how efficiently the mode EMITS into R³) and only computes
     the charge structure.

F13. The physical picture: the geometric integral answers "how much
     charge does the mode carry?" (answer: more for low n₂).  The
     dipole model answers "how efficiently does the mode radiate?"
     (answer: less for low n₂, because ω⁴).  The OBSERVABLE
     coupling is the product — charge × radiation efficiency.
     The ω⁴ suppression overwhelms the 1/(n₂-s)² enhancement.

F14. For the proton sheet, the same mechanism applies: the (1,1)
     ghost at ~470 MeV has μ ≈ 1.0 vs the proton's μ ≈ 2.0.
     The ω⁴ suppression gives P(1,1)/P(1,2) ≈ 1/16.

F15. CRITICAL CAVEAT: the ω⁴ Larmor scaling applies to classical
     dipole radiation.  In quantum field theory, the coupling of
     a charged particle to the photon field depends on the CHARGE
     (not ω⁴).  Whether the ω⁴ factor is physical or an artifact
     of the classical dipole model requires a QFT-level calculation
     of the vertex coupling between T² modes and R³ photons.

     If ω⁴ is physical: the (1,1) ghost is naturally suppressed.
     If ω⁴ is not physical: Track 1's geometric result stands,
     and the (1,1) tension remains.
""")


if __name__ == "__main__":
    main()
