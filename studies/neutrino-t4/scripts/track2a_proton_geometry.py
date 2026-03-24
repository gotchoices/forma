#!/usr/bin/env python3
"""
R26 Track 2a: Proton T² geometry.

The proton is a (1,2) photon on its own T² at fm scale, with charge +e.
R19's self-consistent α formula applies identically:

    α = r² sin²(2πs) / (4π (2−s)² √(r²(1+2s)²+4))

This is the SAME one-parameter family as the electron — same topology,
same charge mechanism, different physical scale.  The proton mass sets
L₄ (ring circumference), and r_p = a/R sets the shape.

This script:
1. Solves the α constraint for s(r_p)
2. Computes physical scales (L₃, L₄, R, a) from the proton mass
3. Catalogs the mode spectrum on the proton T²
4. Compares electron and proton T² geometries
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import (h, hbar, c, eps0, e, alpha as ALPHA,
                            m_e, lambda_C)

M_P_KG = 1.67262192369e-27   # proton mass (kg)
M_N_KG = 1.67492749804e-27   # neutron mass (kg)
M_P_MEV = M_P_KG * c**2 / (1.602176634e-13)  # proton mass in MeV
M_N_MEV = M_N_KG * c**2 / (1.602176634e-13)
M_E_MEV = m_e * c**2 / (1.602176634e-13)
LAMBDA_P = h / (M_P_KG * c)  # proton Compton wavelength (m)


def alpha_from_rs(r, s):
    """Self-consistent α formula from R19 Track 3."""
    q_eff = 2 - s
    sin_term = math.sin(2 * math.pi * s)
    denom = math.sqrt(r**2 * (1 + 2*s)**2 + 4)
    if abs(q_eff) < 1e-15:
        return float('inf')
    return r**2 * sin_term**2 / (4 * math.pi * q_eff**2 * denom)


def solve_shear(r, alpha_target=ALPHA):
    """Solve for s at given r such that α(r,s) = α_target."""
    s_scan = np.linspace(0.001, 0.49, 5000)
    alpha_scan = [alpha_from_rs(r, s) for s in s_scan]
    roots = []
    for i in range(len(s_scan) - 1):
        if (alpha_scan[i] - alpha_target) * (alpha_scan[i+1] - alpha_target) < 0:
            s_root = brentq(lambda s: alpha_from_rs(r, s) - alpha_target,
                            s_scan[i], s_scan[i+1])
            roots.append(s_root)
    return roots


def mode_energy(n3, n4, r, s):
    """Dimensionless energy μ = E/E₀ for mode (n3, n4)."""
    return math.sqrt((n3 / r)**2 + (n4 - n3 * s)**2)


def mu_12(r, s):
    """Dimensionless energy of the (1,2) mode: E(1,2) = E₀ × μ."""
    return math.sqrt(1.0/r**2 + (2 - s)**2)


def physical_scales(r, s, particle_mass_MeV):
    """
    Compute physical dimensions of the T² for given r, s.

    Uses KK mode energy convention (consistent with Track 1a):
      E(1,2) = E₀ × μ(1,2) = particle mass
    → E₀ = m_particle / μ(1,2)
    → L₄ = hc / E₀

    Note: R19's α formula was derived under a different convention
    (WvM geodesic-length Compton constraint).  The two give different
    physical scales.  This is an open question (see Section 5).
    """
    mu = mu_12(r, s)
    E0_MeV = particle_mass_MeV / mu
    hc_MeV_fm = 2 * math.pi * 197.3269804  # hc in MeV·fm
    L4 = hc_MeV_fm / E0_MeV                # fm
    L3 = r * L4
    R = L4 / (2 * math.pi)
    a = L3 / (2 * math.pi)
    return L3, L4, R, a, E0_MeV


def spin_correction(p, q, eps, N=5000):
    """L_z/ℏ for mode (p,q) at aspect ratio ε = a/R (from Track 1d)."""
    theta = np.linspace(0, 2 * np.pi, N, endpoint=False)
    integrand = np.sqrt(p**2 * eps**2 + q**2 * (1 + eps * np.cos(theta))**2)
    ell = np.mean(integrand)
    Lz = q * np.pi * (2 + eps**2) / ell**2
    return Lz / (2 * np.pi)


def main():
    print("=" * 76)
    print("R26 Track 2a: Proton T² Geometry")
    print("=" * 76)

    # ================================================================
    # SECTION 1: The α constraint — same formula, same family
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 1: α(r, s) = 1/137 for the proton T²")
    print("=" * 76)
    print(f"""
  The proton is a (1,2) photon on its own T² with charge +e.
  The R19 self-consistent α formula:

    α = r² sin²(2πs) / (4π (2−s)² √(r²(1+2s)²+4))

  applies identically — same topology, same winding, same charge
  mechanism.  Only the SCALE differs: the proton's Compton wavelength
  λ_p = {LAMBDA_P*1e15:.4f} fm replaces the electron's λ_e = {lambda_C*1e12:.4f} pm.

  Solving for s(r_p) at α = {ALPHA:.10f}:
""")

    r_values = [0.5, 1.0, 2.0, 3.0, 5.0, 6.6, 8.0, 10.0, 15.0, 20.0]

    print(f"  {'r_p':>6s}  {'s₅₆':>10s}  {'r_p matches r_e?':>18s}")
    print(f"  {'─'*6}  {'─'*10}  {'─'*18}")

    solutions = {}
    for r in r_values:
        roots = solve_shear(r)
        if roots:
            s = roots[0]
            solutions[r] = s
            print(f"  {r:6.1f}  {s:10.6f}  yes (same formula)")
        else:
            print(f"  {r:6.1f}  {'—':>10s}  no solution")

    print(f"""
  The solution curve s(r) is IDENTICAL for electron and proton — the
  α formula depends only on (r, s) and the charge +e, not on mass or
  scale.  The proton T² is geometrically SIMILAR to the electron T²
  (same shape family), just 1836× smaller in linear dimensions.
""")

    # ================================================================
    # SECTION 2: Physical scales
    # ================================================================
    print("=" * 76)
    print("SECTION 2: Physical scales of the proton T²")
    print("=" * 76)

    print(f"\n  Proton mass: {M_P_MEV:.3f} MeV")
    print(f"  Proton Compton wavelength: λ_p = {LAMBDA_P*1e15:.4f} fm")
    print(f"  Electron Compton wavelength: λ_e = {lambda_C*1e12:.4f} pm "
          f"= {lambda_C*1e15:.1f} fm")
    print(f"  Ratio: λ_e/λ_p = m_p/m_e = {M_P_MEV/M_E_MEV:.2f}")

    print(f"\n  {'r_p':>5s}  {'s₅₆':>8s}  {'L₄ (fm)':>9s}  {'L₃ (fm)':>9s}  "
          f"{'R (fm)':>8s}  {'a (fm)':>8s}  {'E₀ (MeV)':>10s}")
    print(f"  {'─'*5}  {'─'*8}  {'─'*9}  {'─'*9}  {'─'*8}  {'─'*8}  {'─'*10}")

    for r in [1.0, 2.0, 3.0, 5.0, 6.6, 10.0]:
        if r not in solutions:
            continue
        s = solutions[r]
        L3, L4, R, a, E0 = physical_scales(r, s, M_P_MEV)
        print(f"  {r:5.1f}  {s:8.5f}  {L4:9.4f}  {L3:9.4f}  "
              f"{R:8.4f}  {a:8.4f}  {E0:10.2f}")

    print(f"""
  For comparison, the electron T² at the same r values:""")

    print(f"\n  {'r_e':>5s}  {'s₁₂':>8s}  {'L₄ (fm)':>9s}  {'L₃ (fm)':>9s}  "
          f"{'R (fm)':>8s}  {'a (fm)':>8s}  {'E₀ (MeV)':>10s}")
    print(f"  {'─'*5}  {'─'*8}  {'─'*9}  {'─'*9}  {'─'*8}  {'─'*8}  {'─'*10}")

    for r in [1.0, 2.0, 5.0, 6.6]:
        if r not in solutions:
            continue
        s = solutions[r]
        L3, L4, R, a, E0 = physical_scales(r, s, M_E_MEV)
        print(f"  {r:5.1f}  {s:8.5f}  {L4*1e3:9.4f}  {L3*1e3:9.4f}  "
              f"{R*1e3:8.4f}  {a*1e3:8.4f}  {E0:10.4f}")
    print(f"  (electron values in units of 10⁻³ fm = pm × 10⁻³)")

    # ================================================================
    # SECTION 3: Mode spectrum on the proton T²
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 3: Mode spectrum on the proton T²")
    print("=" * 76)

    for r in [1.0, 5.0, 6.6]:
        if r not in solutions:
            continue
        s = solutions[r]
        _, _, _, _, E0 = physical_scales(r, s, M_P_MEV)

        print(f"\n  r_p = {r}, s = {s:.5f}, E₀ = {E0:.2f} MeV:")
        print(f"  {'(n₅,n₆)':>8s}  {'μ':>8s}  {'Mass(MeV)':>10s}  "
              f"{'p-odd?':>7s}  {'L_z/ℏ':>7s}  {'Charged':>8s}  {'ID':>12s}")
        print(f"  {'─'*8}  {'─'*8}  {'─'*10}  {'─'*7}  {'─'*7}  {'─'*8}  {'─'*12}")

        modes = []
        for n5 in range(-10, 11):
            for n6 in range(-5, 6):
                if n5 == 0 and n6 == 0:
                    continue
                mu = mode_energy(n5, n6, r, s)
                mass = E0 * mu
                if mass <= 2000:  # below 2 GeV
                    is_fermion = abs(n5) % 2 == 1
                    charged = abs(n5) == 1
                    Lz = spin_correction(abs(n5), abs(n6), r) if n6 != 0 else 0
                    modes.append((n5, n6, mu, mass, is_fermion, Lz, charged))

        modes.sort(key=lambda x: x[3])

        # Identify proton
        proton_mass = E0 * mode_energy(1, 2, r, s)

        for n5, n6, mu, mass, ferm, Lz, chg in modes[:30]:
            ferm_s = "F" if ferm else "B"
            chg_s = "yes" if chg else "no"

            ident = ""
            if (n5, n6) == (1, 2):
                ident = "← proton"
            elif (n5, n6) == (-1, -2):
                ident = "← antiproton"
            elif abs(mass - M_N_MEV) < 5:
                ident = f"Δm={mass-M_P_MEV:+.1f}"

            print(f"  ({n5:+d},{n6:+d})  {mu:8.4f}  {mass:10.2f}  "
                  f"{'yes' if ferm else 'no':>7s}  {Lz:7.3f}  {chg_s:>8s}  {ident}")

        if len(modes) > 30:
            print(f"  ... {len(modes) - 30} more modes below 2 GeV")

    # ================================================================
    # SECTION 4: Electron vs proton T² comparison
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 4: Electron vs proton — same shape, different scale")
    print("=" * 76)

    r_ref = 6.6
    if r_ref in solutions:
        s = solutions[r_ref]

        L3_p, L4_p, R_p, a_p, E0_p = physical_scales(r_ref, s, M_P_MEV)
        L3_e, L4_e, R_e, a_e, E0_e = physical_scales(r_ref, s, M_E_MEV)

        print(f"""
  At r = {r_ref} (S2's electron aspect ratio), s = {s:.5f}:

  │ Property       │ Electron T²      │ Proton T²        │ Ratio        │
  │ ──────         │ ──────────       │ ──────────       │ ─────        │
  │ Particle       │ (1,2) mode       │ (1,2) mode       │ same         │
  │ Mass           │ {M_E_MEV:.4f} MeV    │ {M_P_MEV:.3f} MeV   │ {M_P_MEV/M_E_MEV:.2f}     │
  │ Charge         │ −e               │ +e               │ same |Q|     │
  │ Spin           │ ½                │ ½                │ same         │
  │ r = a/R        │ {r_ref}              │ {r_ref}              │ 1            │
  │ s (shear)      │ {s:.5f}          │ {s:.5f}          │ 1            │
  │ L₄ = 2πR      │ {L4_e*1e3:.4f} pm     │ {L4_p:.4f} fm     │ {L4_e/L4_p:.2f}     │
  │ L₃ = 2πa      │ {L3_e*1e3:.3f} pm    │ {L3_p:.3f} fm    │ {L3_e/L3_p:.2f}     │
  │ R (ring)       │ {R_e*1e3:.4f} pm     │ {R_p:.4f} fm     │ {R_e/R_p:.2f}     │
  │ a (tube)       │ {a_e*1e3:.3f} pm    │ {a_p:.3f} fm    │ {a_e/a_p:.2f}     │
  │ E₀             │ {E0_e:.4f} MeV   │ {E0_p:.2f} MeV    │ {E0_p/E0_e:.2f}     │

  If the electron and proton share the same r (aspect ratio), then
  the proton T² is a SCALED COPY of the electron T²:

    L_proton / L_electron = m_e / m_p = 1/{M_P_MEV/M_E_MEV:.2f}

  for every linear dimension.  The shapes are identical; only the
  scale differs.  This is the simplest possibility.
""")

    # ================================================================
    # SECTION 5: What determines m_p/m_e?
    # ================================================================
    print("=" * 76)
    print("SECTION 5: The mass ratio m_p/m_e")
    print("=" * 76)

    print(f"""
  If both T²s have the SAME r and s (same shape), then:

    m_p/m_e = E₀_p/E₀_e × μ_p/μ_e

  where μ = √((1/r)² + (2−s)²) is the dimensionless mode energy.
  Since r and s are the same, μ_p = μ_e, and:

    m_p/m_e = E₀_p/E₀_e = L₄_e/L₄_p

  The mass ratio is just the ratio of the compact dimension sizes.
  The model does NOT predict m_p/m_e — it takes it as input (via
  the ratio of compact dimension scales).

  If the two T²s have DIFFERENT r values (r_e ≠ r_p), then:

    m_p/m_e = (E₀_p/E₀_e) × √[((1/r_p)² + (2−s_p)²) /
                                 ((1/r_e)² + (2−s_e)²)]

  This depends on both r_e and r_p separately.  The mass ratio
  constrains the ratio of L₄ values but does not fix individual r.

  In either case, the proton/electron mass ratio is an INPUT to the
  model, not a prediction.  The ratio of compact dimension scales
  (L₄_proton/L₄_electron) is tuned to produce m_p/m_e = {M_P_MEV/M_E_MEV:.2f}.
""")

    # ================================================================
    # SECTION 6: Convention issue — WvM vs KK mode energies
    # ================================================================
    print("=" * 76)
    print("SECTION 6: Open question — WvM vs KK mode energies")
    print("=" * 76)

    print(f"""
  Two conventions exist for mode energies on the sheared T²:

  KK (Track 1a):  E(n₃,n₄) = E₀ √((n₃/r)² + (n₄ − n₃s)²)
    Wavevector on flat torus with quantized reciprocal lattice.
    Used for neutrino mass ratios → matched experiment.

  WvM (R19):      E(n₃,n₄) = hc / L_geodesic(n₃,n₄)
    Single photon energy = hc / path length.
    Used to derive α formula → matched 1/137.

  These give DIFFERENT mode energies for the same (n₃,n₄).
  The KK formula has E ∝ |k| (larger k → more energy).
  The WvM formula has E ∝ 1/L (longer path → less energy).

  Consequences:
  - KK: (1,2) is heavier than (1,1) [more momentum → more energy]
  - WvM: (1,2) is lighter than (1,1) [longer path → less energy]
  - Mass ordering is REVERSED between conventions.

  For Track 2a, we use KK convention (consistent with Track 1a):
    E₀ = m_proton / μ(1,2) where μ = √(1/r² + (2−s)²)

  The α formula s(r) is the same dimensionless curve regardless
  (it depends on geometry, not on which convention sets the scale).
  But the PHYSICAL SCALES (R, a, L₄) differ between conventions.

  Reconciling these two pictures — one gives correct neutrino
  ratios, the other gives correct α — is an open problem.
  It may require a unified energy formula that reduces to both
  in appropriate limits, or one convention may be wrong.
""")

    # ================================================================
    # SECTION 7: Summary
    # ================================================================
    print("=" * 76)
    print("SECTION 7: Track 2a Summary")
    print("=" * 76)

    print(f"""
  1. The proton T² uses the SAME α formula as the electron T².
     The solution curve s(r) is identical — the geometry is a
     one-parameter family in r, just like the electron.

  2. Physical scales at r = {r_ref} (KK convention):
     R_p = {R_p:.4f} fm,  a_p = {a_p:.3f} fm
     L₄ = {L4_p:.4f} fm,  L₃ = {L3_p:.3f} fm
     E₀ = {E0_p:.2f} MeV

  3. The proton T² is geometrically SIMILAR to the electron T²
     (same shape, scaled by m_e/m_p ≈ 1/1836 in all lengths).
     This is the simplest possibility; r_p ≠ r_e is also allowed
     but adds a free parameter.

  4. The mode spectrum on the proton T² mirrors the electron's:
     (1,2) = proton, (−1,−2) = antiproton, plus higher modes.
     The nearest modes to the proton are (1,1) and (−1,1) at
     different masses (depending on r_p).

  5. The mass ratio m_p/m_e = {M_P_MEV/M_E_MEV:.2f} is an INPUT — it
     sets the ratio L₄_e/L₄_p.  The model does not predict this
     ratio; it emerges from the relative sizes of the two compact
     T²s within T⁶.

  6. For Track 2b (charge radius): the proton's charge distribution
     is the (1,2) geodesic on a torus with R = {R_p:.4f} fm.
     The experimental charge radius (0.841 fm) is {0.841/R_p:.1f}× R.

  7. For Track 2c (neutron): the nearest uncharged fermion mode
     on the proton T² has p = 3, with mass and spin very different
     from the neutron's requirements.

  8. OPEN QUESTION: the WvM and KK mode energy conventions give
     different physical scales and mass orderings.  The neutrino
     study used KK; the α derivation used WvM.  Reconciliation
     needed.
""")


if __name__ == "__main__":
    main()
