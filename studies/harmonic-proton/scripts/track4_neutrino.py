#!/usr/bin/env python3
"""
R20 Track 4: Can the neutrino live on T²?

QUESTION
========
The neutrino has spin 1/2, charge 0, and mass < 0.8 eV (≈ 1.6e-6 m_e).
Can it be modeled as a mode on the electron's T², or does it require
a separate compact space?

APPROACH
========
1. Catalog all uncharged spin-1/2 modes on the electron's T²
   and confirm the lightest is (2,4) at 2 m_e — far too heavy.
2. Compute the T² size needed for a neutrino-mass fundamental
   mode and compare with experimental bounds on extra dimensions.
3. Assess composite/perturbative mechanisms (beat frequencies,
   mass splitting) that might produce ultra-light excitations.
4. Check consistency with beta decay kinematics.
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C

m_p = 1.67262192369e-27
m_n = 1.67492749804e-27
mass_ratio_pe = m_p / m_e
mass_ratio_ne = m_n / m_e

m_nu_upper_eV = 0.8
m_nu_cosmo_eV = 0.09 / 3  # per flavor, cosmological
eV_to_kg = 1.602176634e-19 / c**2
m_nu_upper_kg = m_nu_upper_eV * eV_to_kg
m_nu_cosmo_kg = m_nu_cosmo_eV * eV_to_kg


def alpha_mode_2d(r, s, m):
    q = m - s
    sn = math.sin(2 * math.pi * s)
    if abs(sn) < 1e-15 or abs(q) < 1e-15:
        return 0.0
    d = math.sqrt(r**2 * (1 + m * s)**2 + m**2)
    return r**2 * sn**2 / (4 * math.pi * q**2 * d)


def solve_electron_s(r):
    def f(s):
        return alpha_mode_2d(r, s, 2) - alpha
    ss = np.linspace(0.001, 0.499, 5000)
    fs = [f(s) for s in ss]
    for i in range(len(fs) - 1):
        if fs[i] * fs[i + 1] < 0:
            return brentq(f, ss[i], ss[i + 1], xtol=1e-14)
    return None


def energy_ratio_momentum(n1, n2, r, s):
    """E(n1,n2)/E(1,2) in momentum picture."""
    def k_sq(a, b):
        return (a / 1.0)**2 + ((b - a * s) / r)**2
    k_e = k_sq(1, 2)
    k_m = k_sq(n1, n2)
    if k_e == 0:
        return float('inf')
    return math.sqrt(k_m / k_e)


def spin_of_mode(n1, n2):
    """Spin = |n1/n2| if n2 != 0, else undefined."""
    if n2 == 0:
        return None
    return abs(n1 / n2)


def main():
    r = 1.0
    s = solve_electron_s(r)
    print(f"Electron geometry: r = {r}, s₁₂ = {s:.10f}")
    print(f"Electron mode: (1, 2), mass = {m_e:.6e} kg = 0.511 MeV")
    print()

    m_e_eV = m_e * c**2 / 1.602176634e-19
    m_e_MeV = m_e_eV / 1e6
    print(f"Neutrino mass upper bound (KATRIN): {m_nu_upper_eV} eV "
          f"= {m_nu_upper_eV / m_e_eV:.2e} m_e")
    print(f"Neutrino mass per flavor (cosmo):  {m_nu_cosmo_eV:.4f} eV "
          f"= {m_nu_cosmo_eV / m_e_eV:.2e} m_e")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 1: Uncharged spin-1/2 modes on the electron's T²")
    print("=" * 72)
    print()
    print("Spin-1/2 requires n₂ = 2n₁ (i.e., |n₁/n₂| = 1/2).")
    print("Charge 0 requires |n₁| ≠ 1.")
    print()

    candidates = []
    for n1 in range(-20, 21):
        for n2 in range(-40, 41):
            if n1 == 0 and n2 == 0:
                continue
            sp = spin_of_mode(n1, n2)
            if sp is None:
                continue
            if abs(sp - 0.5) > 1e-10:
                continue
            if abs(n1) == 1:
                continue
            E_ratio = energy_ratio_momentum(n1, n2, r, s)
            candidates.append((n1, n2, E_ratio))

    candidates.sort(key=lambda x: x[2])
    print(f"{'Mode':>12s}  {'E/m_e':>10s}  {'E (MeV)':>10s}  {'|n₁|':>5s}")
    print("-" * 45)
    seen = set()
    for n1, n2, E in candidates[:20]:
        key = (abs(n1), abs(n2))
        if key in seen:
            continue
        seen.add(key)
        print(f"({n1:+3d},{n2:+3d})  {E:10.4f}  {E * m_e_MeV:10.4f}  {abs(n1):5d}")

    print()
    lightest = candidates[0]
    print(f"Lightest uncharged spin-1/2 mode: ({lightest[0]},{lightest[1]})")
    print(f"  E = {lightest[2]:.4f} m_e = {lightest[2] * m_e_MeV:.4f} MeV")
    print(f"  This is {lightest[2] / (m_nu_upper_eV / m_e_eV):.0e} × "
          f"the neutrino mass upper bound.")
    print()
    print("CONCLUSION: No mode on the electron's T² can be the neutrino.")
    print("  The gap is ~6 orders of magnitude.")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 2: What T² size would produce a neutrino-mass mode?")
    print("=" * 72)
    print()

    print("The fundamental (1,2) mode on a T² has E = ℏc|k(1,2)|.")
    print("For the electron's T²: E(1,2) = m_e c² → L determines m_e.")
    print()
    print(f"Electron Compton wavelength: λ_C = {lambda_C:.6e} m")
    print()

    for label, m_nu_eV in [("KATRIN upper bound", m_nu_upper_eV),
                            ("Cosmological (per flavor)", m_nu_cosmo_eV)]:
        ratio = m_e_eV / m_nu_eV
        L_nu = lambda_C * ratio
        print(f"--- {label}: m_ν = {m_nu_eV:.4f} eV ---")
        print(f"  Mass ratio m_e/m_ν = {ratio:.2e}")
        print(f"  Required T² scale: L_ν = λ_C × (m_e/m_ν)")
        print(f"                    = {lambda_C:.3e} m × {ratio:.2e}")
        print(f"                    = {L_nu:.3e} m")
        print(f"                    = {L_nu * 1e6:.1f} μm")
        print()

    print("Experimental bounds on extra compact dimensions:")
    print("  Sub-mm gravity (Adelberger et al. 2024): R < ~30 μm")
    print("  Neutron scattering: R < ~10 nm (for some scenarios)")
    print()

    L_katrin = lambda_C * (m_e_eV / m_nu_upper_eV)
    L_cosmo = lambda_C * (m_e_eV / m_nu_cosmo_eV)
    print(f"  Neutrino T² at KATRIN bound: {L_katrin * 1e6:.1f} μm")
    print(f"  Neutrino T² at cosmo bound:  {L_cosmo * 1e6:.0f} μm")
    print()

    print("Assessment:")
    if L_katrin < 30e-6:
        print(f"  KATRIN-scale T² ({L_katrin*1e6:.1f} μm) is BELOW the "
              f"sub-mm gravity bound (~30 μm).")
        print("  This is experimentally ALLOWED but would be detectable")
        print("  in next-generation gravity experiments.")
    else:
        print(f"  KATRIN-scale T² ({L_katrin*1e6:.1f} μm) EXCEEDS the "
              f"sub-mm gravity bound (~30 μm).")
        print("  This is likely RULED OUT by current experiments if the")
        print("  extra dimensions couple to gravity.")

    if L_cosmo < 30e-6:
        print(f"  Cosmo-scale T² ({L_cosmo*1e6:.0f} μm) is also below "
              f"the gravity bound.")
    else:
        print(f"  Cosmo-scale T² ({L_cosmo*1e6:.0f} μm) EXCEEDS the "
              f"gravity bound.")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 3: Could the neutrino be a composite/perturbative effect?")
    print("=" * 72)
    print()

    print("3a. Beat frequency between nearly degenerate modes")
    print("-" * 50)
    print()
    print("If two modes with energies E₁ and E₂ are nearly degenerate,")
    print("their 'beat' has effective energy |E₁ - E₂|. Could this be")
    print("neutrino-scale?")
    print()

    near_pairs = []
    modes = []
    for n1 in range(-10, 11):
        for n2 in range(-20, 21):
            if n1 == 0 and n2 == 0:
                continue
            E = energy_ratio_momentum(n1, n2, r, s)
            if E < 20:
                modes.append((n1, n2, E))

    modes.sort(key=lambda x: x[2])
    min_diff = float('inf')
    min_pair = None
    for i in range(len(modes) - 1):
        diff = modes[i + 1][2] - modes[i][2]
        if diff > 1e-10 and diff < min_diff:
            min_diff = diff
            min_pair = (modes[i], modes[i + 1])

    if min_pair:
        m1, m2 = min_pair
        print(f"  Closest pair: ({m1[0]:+d},{m1[1]:+d}) at {m1[2]:.6f} m_e")
        print(f"                ({m2[0]:+d},{m2[1]:+d}) at {m2[2]:.6f} m_e")
        print(f"  ΔE = {min_diff:.6f} m_e = {min_diff * m_e_MeV * 1e6:.1f} eV")
        print(f"  Neutrino mass = {m_nu_upper_eV:.1f} eV")
        print(f"  Ratio ΔE/m_ν = {min_diff * m_e_eV / m_nu_upper_eV:.1f}")
        print()
        if min_diff * m_e_eV > m_nu_upper_eV * 100:
            print("  CONCLUSION: Even the closest pair splitting is far too")
            print("  large.  Beat frequencies don't reach neutrino scale.")
        else:
            print("  This splitting is in the right ballpark!")

    print()
    print("  Note: For s₁₂ ≈ 0.165, the shear is an irrational number,")
    print("  so no exact degeneracies occur.  All mode energies are distinct.")
    print()

    print("  Five closest mode pairs (E < 20 m_e):")
    diffs = []
    for i in range(len(modes) - 1):
        d = modes[i + 1][2] - modes[i][2]
        if d > 1e-10:
            diffs.append((d, modes[i], modes[i + 1]))
    diffs.sort()
    for d, m1, m2 in diffs[:5]:
        print(f"    ({m1[0]:+d},{m1[1]:+d}) – ({m2[0]:+d},{m2[1]:+d}): "
              f"ΔE = {d:.6f} m_e = {d * m_e_eV:.1f} eV")
    print()

    print("  Extending to higher modes (E < 100 m_e) for closer pairs...")
    modes_hi = []
    for n1 in range(-60, 61):
        for n2 in range(-120, 121):
            if n1 == 0 and n2 == 0:
                continue
            E = energy_ratio_momentum(n1, n2, r, s)
            if E < 100:
                modes_hi.append((n1, n2, E))
    modes_hi.sort(key=lambda x: x[2])
    diffs_hi = []
    for i in range(len(modes_hi) - 1):
        d = modes_hi[i + 1][2] - modes_hi[i][2]
        if d > 1e-14:
            diffs_hi.append((d, modes_hi[i], modes_hi[i + 1]))
    diffs_hi.sort()
    print(f"  Total modes below 100 m_e: {len(modes_hi)}")
    print(f"  Five closest pairs:")
    for d, m1, m2 in diffs_hi[:5]:
        print(f"    ({m1[0]:+d},{m1[1]:+d}) – ({m2[0]:+d},{m2[1]:+d}): "
              f"ΔE = {d:.10f} m_e = {d * m_e_eV:.4f} eV")
    if diffs_hi:
        d0 = diffs_hi[0][0]
        print(f"  Closest splitting: {d0 * m_e_eV:.4f} eV "
              f"(ratio to m_ν: {d0 * m_e_eV / m_nu_upper_eV:.2f})")
    print()

    print("3b. Perturbative mass correction")
    print("-" * 50)
    print()
    print("Could curvature/embedding corrections to the flat-T² eigenvalue")
    print("produce a nearly-massless mode?")
    print()
    print("On flat T², every mode has E = ℏc|k| > 0 (for non-zero k).")
    print("The lightest uncharged spin-1/2 mode (2,4) has E = 2 m_e.")
    print("A perturbative correction would need to reduce this by 99.99998%")
    print(f"to reach {m_nu_upper_eV} eV. This is not perturbative — it")
    print("would require fine-tuned cancellation.")
    print()
    print("More plausible: the neutrino is NOT a Kaluza-Klein mode at all,")
    print("but a different type of excitation entirely (see Section 5).")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 4: Consistency with beta decay")
    print("=" * 72)
    print()

    m_n_eV = m_n * c**2 / 1.602176634e-19
    m_p_eV = m_p * c**2 / 1.602176634e-19
    Q_value_eV = (m_n_eV - m_p_eV - m_e_eV)
    Q_value_MeV = Q_value_eV / 1e6

    print("Beta decay: n → p + e⁻ + ν̄_e")
    print(f"  Q value (available KE): {Q_value_MeV:.4f} MeV = {Q_value_eV:.1f} eV")
    print(f"  Neutrino rest mass:     < {m_nu_upper_eV} eV")
    print(f"  Ratio Q/m_ν:            > {Q_value_eV / m_nu_upper_eV:.0f}")
    print()
    print("The antineutrino is ultra-relativistic in all observed decays.")
    print("Its rest mass is negligible compared to the decay energy.")
    print()
    print("In the harmonic model (Track 3), the 0.782 MeV released")
    print("comes from the neutron's excess harmonic energy. The question")
    print("is: what IS the antineutrino in this model?")
    print()
    print("Options:")
    print("  A. A wave packet of harmonic energy escaping the composite.")
    print("     Problem: harmonic energies are quantized in units of m_e.")
    print("     A wave packet carrying 0.782 MeV kinetic energy would")
    print("     correspond to ~1.5 harmonic quanta. The rest mass of such")
    print("     a packet would be ≥ 2 m_e (the lightest uncharged spin-1/2")
    print("     mode), not < 0.8 eV.")
    print()
    print("  B. A mode on a separate, much larger T² (Section 2).")
    print("     The neutrino would be a (1,2) fundamental on its own torus")
    print("     with L_ν ~ 1.6 μm. It couples to the electron/proton system")
    print("     during weak interactions but lives on a different geometry.")
    print()
    print("  C. Not a torus mode at all — possibly a gravitational or")
    print("     topological excitation of the compact space itself")
    print("     (geometry fluctuation rather than field fluctuation).")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 5: The neutrino as a different scale")
    print("=" * 72)
    print()

    print("If each lepton generation has its own T² scale:")
    print()
    print(f"  Electron:  L_e  = {lambda_C:.3e} m  (m = {m_e_MeV:.4f} MeV)")
    print()

    m_mu_eV = 1.883531627e-28 * c**2 / 1.602176634e-19
    m_tau_eV = 3.16754e-27 * c**2 / 1.602176634e-19
    L_mu = lambda_C * m_e_eV / m_mu_eV
    L_tau = lambda_C * m_e_eV / m_tau_eV

    print(f"  Muon:      L_μ  = {L_mu:.3e} m   (m = {m_mu_eV/1e6:.2f} MeV)")
    print(f"  Tau:       L_τ  = {L_tau:.3e} m   (m = {m_tau_eV/1e6:.1f} MeV)")
    print()

    print("Neutrino scales (if neutrino is a (1,2) mode on a separate T²):")
    for label, m_eV in [("KATRIN bound (0.8 eV)", 0.8),
                        ("Cosmo (~0.03 eV)", 0.03),
                        ("Atmospheric Δm² (~0.05 eV)", 0.05)]:
        L = lambda_C * m_e_eV / m_eV
        print(f"  ν ({label}): L = {L:.3e} m = {L*1e6:.1f} μm")
    print()

    print("Mass hierarchy in terms of T² scale:")
    print()
    print("  particle   mass (eV)     L (m)           L/L_e")
    print("  " + "-" * 55)
    particles = [
        ("tau",      m_tau_eV,  L_tau),
        ("muon",     m_mu_eV,   L_mu),
        ("electron", m_e_eV,    lambda_C),
        ("ν (0.05eV)", 0.05,    lambda_C * m_e_eV / 0.05),
    ]
    for name, mass_eV, L in particles:
        print(f"  {name:12s} {mass_eV:12.2f}    {L:12.3e}    {L/lambda_C:12.2e}")
    print()

    print("The neutrino's T² would be ~10⁷ × the electron's T².")
    print("This is a SEPARATE compact geometry, not a mode on the same torus.")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 6: Muon and tau as 'hot' electrons")
    print("=" * 72)
    print()

    m_mu_me = 1.883531627e-28 / m_e
    m_tau_me = 3.16754e-27 / m_e
    print("An alternative to multi-scale T²: the muon and tau are the")
    print("SAME (1,2) fundamental on the SAME T² as the electron, but")
    print("with uncharged harmonics (like the proton).")
    print()
    print(f"  Muon:  m_μ = {m_mu_me:.2f} m_e → needs {m_mu_me - 1:.2f} m_e "
          f"of uncharged harmonics")
    print(f"  Tau:   m_τ = {m_tau_me:.1f} m_e → needs {m_tau_me - 1:.1f} m_e "
          f"of uncharged harmonics")
    print(f"  Proton: m_p = {mass_ratio_pe:.2f} m_e → needs {mass_ratio_pe - 1:.2f} m_e "
          f"of uncharged harmonics")
    print()
    print("Comparison of 'excited electron' composites:")
    print()
    print(f"  {'Particle':>10s}  {'Mass/m_e':>10s}  {'Charge':>8s}  {'Spin':>6s}  "
          f"{'Stable?':>8s}  {'Decay':>30s}")
    print("  " + "-" * 80)
    particles_table = [
        ("electron", 1.0, "-e", "1/2", "yes", "—"),
        ("muon", m_mu_me, "-e", "1/2", "no", "e⁻ + ν̄_e + ν_μ (2.2 μs)"),
        ("tau", m_tau_me, "-e", "1/2", "no", "multiple modes (~0.3 ps)"),
        ("proton", mass_ratio_pe, "+e", "1/2", "yes", "—"),
        ("neutron", mass_ratio_ne, "0", "1/2", "no", "p + e⁻ + ν̄_e (879 s)"),
    ]
    for name, mass, charge, spin, stable, decay in particles_table:
        print(f"  {name:>10s}  {mass:10.2f}  {charge:>8s}  {spin:>6s}  "
              f"{stable:>8s}  {decay:>30s}")
    print()

    print("Key pattern:")
    print("  - Muon and tau: same fundamental as electron, charge -e.")
    print("    Harmonics escape → decay to electron + neutrinos.")
    print("  - Proton: OPPOSITE fundamental (-1,-2), charge +e.")
    print("    Cannot shed charge (lightest +e particle). Stable.")
    print("  - Neutron: both fundamentals + harmonics.")
    print("    Can eject electron fundamental. Unstable.")
    print()
    print("This suggests muon/tau decay = harmonic evaporation,")
    print("same mechanism as neutron decay but with only one")
    print("fundamental (no charge annihilation needed).")
    print()
    print("The muon and tau emit neutrinos in decay. If these are")
    print("NOT modes on the electron's T², the question is: where")
    print("do they come from? The neutrino must be created in the")
    print("decay process, not pre-existing in the composite.")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 7: Summary")
    print("=" * 72)
    print()
    print("F14. Neutrino cannot be a mode on the electron's T²")
    print("     Lightest uncharged spin-1/2 mode: (2,4) at 2 m_e = 1.022 MeV")
    print("     Neutrino mass: < 0.8 eV.  Gap: ~6 orders of magnitude.")
    print()
    print("F15. Neutrino T² size and experimental bounds")
    print(f"     A (1,2) fundamental matching m_ν < 0.8 eV needs")
    print(f"     L_ν ≈ {L_katrin*1e6:.1f} μm.  Current sub-mm gravity bound:")
    print(f"     R < ~30 μm.  This is experimentally {'allowed' if L_katrin < 30e-6 else 'excluded'}.")
    print()
    print("F16. Mode splittings reach neutrino mass scale")
    if diffs_hi:
        d0 = diffs_hi[0][0]
        m1_hi, m2_hi = diffs_hi[0][1], diffs_hi[0][2]
        print(f"     At low modes (E < 20 m_e): closest ΔE = {min_diff * m_e_eV:.1f} eV")
        print(f"     At higher modes (E < 100 m_e): closest ΔE = {d0 * m_e_eV:.4f} eV")
        print(f"     Pair: ({m1_hi[0]:+d},{m1_hi[1]:+d}) – ({m2_hi[0]:+d},{m2_hi[1]:+d})")
        print(f"     This is {d0 * m_e_eV / m_nu_upper_eV:.2f}× the KATRIN bound.")
        print(f"     Sub-eV splittings arise naturally from the irrational shear.")
        print(f"     Physical meaning unclear: beat ≠ particle without coupling.")
    print()
    print("F17. Muon/tau as 'hot electrons' (same T², same fundamental)")
    print(f"     Muon = (1,2) + {m_mu_me - 1:.0f} m_e harmonics")
    print(f"     Tau  = (1,2) + {m_tau_me - 1:.0f} m_e harmonics")
    print("     Decay = harmonic evaporation → bare electron + neutrinos")
    print()
    print("F18. Open: neutrino identity")
    print("     Three options remain:")
    print("     A. Mode on a separate, larger T² (L ~ μm)")
    print("     B. Geometry fluctuation (not a field mode)")
    print("     C. Created in decay (not pre-existing)")
    print("     Distinguishing these requires understanding the")
    print("     weak interaction in the torus framework.")


if __name__ == "__main__":
    main()
