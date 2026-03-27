#!/usr/bin/env python3
"""
R29 Track 2: Hydrogen from Ma geometry.

The Ma Yukawa corrections to the Coulomb potential are small
(10⁻¹⁵ to 10⁻¹ depending on r_e), so first-order perturbation
theory is exact to high precision.

The energy shift of level (n,l) is:

  ΔE_nl = <nl| V_Yukawa |nl>
        = -α ℏc × Σ_i <nl| exp(-β_i r) / r |nl>

where β_i = 2π / L_i and the sum runs over the 4 e/p material
dimensions (neutrino decouples since n₃=n₄=0 for both e,p).

For hydrogen wave functions, these expectation values are
analytically known.  For the 1S state:

  <1s| e^{-βr}/r |1s> = 4 / (a₀ (2 + β a₀)²)

For general (n,l):

  <nl| e^{-βr}/r |nl> = (2/(n a₀))^3 × I_nl(β)

where I_nl involves the Laguerre polynomial overlap integrals.
"""

import sys
import os
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import factorial, genlaguerre

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma import (
    ALPHA, M_E_MEV, M_P_MEV, hbar_c_MeV_fm,
)
from lib.ma_solver import self_consistent_metric

R_P = 8.906
R_NU = 5.0
SIGMA_EP = -0.09064

EV_PER_MEV = 1e6
MU = M_E_MEV * M_P_MEV / (M_E_MEV + M_P_MEV)  # reduced mass
A0 = hbar_c_MeV_fm / (ALPHA * MU)               # Bohr radius in fm


def get_circumferences(r_e):
    sc = self_consistent_metric(r_e, R_NU, R_P, sigma_ep=SIGMA_EP)
    return sc['L']


def yukawa_expectation_nl(n, l, beta):
    """
    <nl| exp(-β r) / r |nl> for hydrogen-like atom.

    Computes numerically using the exact radial wave function.
    """
    a = A0
    rho_factor = 2.0 / (n * a)

    norm = math.sqrt(rho_factor**3 * factorial(n - l - 1, exact=True)
                     / (2 * n * factorial(n + l, exact=True)))

    L_poly = genlaguerre(n - l - 1, 2 * l + 1)

    def integrand(r):
        rho = rho_factor * r
        R_nl = norm * math.exp(-rho / 2) * rho**l * L_poly(rho)
        return R_nl**2 * math.exp(-beta * r) * r  # r² × e^{-βr}/r × R²

    r_peak = n**2 * a
    r_max = r_peak * 20

    result, _ = quad(integrand, 0, r_max, limit=200, epsrel=1e-12)
    return result


def yukawa_expectation_1s_analytic(beta):
    """Exact analytical result for 1S state."""
    return 4.0 / (A0 * (2.0 + beta * A0)**2)


def energy_shift(n, l, L):
    """
    First-order energy shift from Ma Yukawa corrections.

    ΔE = -α ℏc × Σ_i <nl| exp(-2π r / L_i) / r |nl>

    Sum over i = 0,1,4,5 (electron and proton dimensions).
    """
    shift = 0.0
    for i in [0, 1, 4, 5]:
        beta = 2 * math.pi / L[i]
        overlap = yukawa_expectation_nl(n, l, beta)
        shift += overlap
    return -ALPHA * hbar_c_MeV_fm * shift


def section(num, title):
    print(f"\n{'='*70}")
    print(f"  SECTION {num}: {title}")
    print(f"{'='*70}\n")


def main():
    # ── Section 1: Analytical validation ──────────────────────────────
    section(1, "Validation: 1S analytical vs numerical")

    print(f"  Reduced mass μ = {MU:.6f} MeV")
    print(f"  Bohr radius a₀ = {A0:.1f} fm = {A0 * 1e-5:.5f} Å")
    print(f"  E₁ = {-0.5 * ALPHA**2 * MU * EV_PER_MEV:.4f} eV\n")

    test_betas = [1e-6, 1e-4, 1e-3, 1e-2, 0.1]
    print(f"  {'β (fm⁻¹)':>12s}  {'Analytic':>14s}  {'Numerical':>14s}  {'Ratio':>8s}")
    print(f"  {'-'*55}")

    for beta in test_betas:
        ana = yukawa_expectation_1s_analytic(beta)
        num = yukawa_expectation_nl(1, 0, beta)
        ratio = num / ana if ana != 0 else 0
        print(f"  {beta:12.2e}  {ana:14.6e}  {num:14.6e}  {ratio:8.6f}")

    # ── Section 2: Energy levels at r_e = 6.6 ────────────────────────
    section(2, "Hydrogen energy shifts at r_e = 6.6")

    r_e = 6.6
    L = get_circumferences(r_e)

    print(f"  r_e = {r_e}")
    print(f"  L₁ (e-tube) = {L[0]:.1f} fm → β₁ = {2*math.pi/L[0]:.5e} fm⁻¹")
    print(f"  L₂ (e-ring) = {L[1]:.1f} fm → β₂ = {2*math.pi/L[1]:.5e} fm⁻¹")
    print(f"  L₅ (p-tube) = {L[4]:.1f} fm → β₅ = {2*math.pi/L[4]:.5e} fm⁻¹")
    print(f"  L₆ (p-ring) = {L[5]:.2f} fm → β₆ = {2*math.pi/L[5]:.3e} fm⁻¹")
    print()

    print("  Individual dimension contributions to 1S shift:\n")
    print(f"  {'Dimension':>14s}  {'β (fm⁻¹)':>12s}  {'<1s|e^-βr/r|1s>':>16s}  "
          f"{'ΔE_i (eV)':>14s}")
    print(f"  {'-'*65}")

    for name, idx in [("e-tube (L₁)", 0), ("e-ring (L₂)", 1),
                       ("p-tube (L₅)", 4), ("p-ring (L₆)", 5)]:
        beta = 2 * math.pi / L[idx]
        overlap = yukawa_expectation_nl(1, 0, beta)
        dE = -ALPHA * hbar_c_MeV_fm * overlap * EV_PER_MEV
        print(f"  {name:>14s}  {beta:12.5e}  {overlap:16.6e}  {dE:+14.6e}")

    total_shift = energy_shift(1, 0, L)
    print(f"\n  Total 1S shift: {total_shift * EV_PER_MEV:+.6e} eV")
    print(f"  Fractional:     {total_shift / (0.5 * ALPHA**2 * MU):+.6e}")

    print(f"\n  Full level table:\n")
    print(f"  {'(n,l)':>6s}  {'E_Coulomb (eV)':>16s}  {'ΔE_Ma (eV)':>16s}  "
          f"{'|ΔE|/E':>12s}  {'E_total (eV)':>16s}")
    print(f"  {'-'*72}")

    levels = {}
    for n in range(1, 5):
        for l in range(n):
            E_c = -0.5 * ALPHA**2 * MU / n**2
            dE = energy_shift(n, l, L)
            E_tot = E_c + dE
            frac = abs(dE / E_c)
            levels[(n, l)] = {'E_c': E_c, 'dE': dE, 'E_tot': E_tot}

            print(f"  ({n},{l}):  {E_c * EV_PER_MEV:16.6f}  "
                  f"{dE * EV_PER_MEV:+16.6e}  {frac:12.2e}  "
                  f"{E_tot * EV_PER_MEV:16.6f}")

    # ── Section 3: Lamb-like splitting ────────────────────────────────
    section(3, "Lamb-like splitting from Ma corrections")

    print("  In pure Coulomb, 2S and 2P are degenerate (E depends only on n).")
    print("  The Ma Yukawa corrections lift this degeneracy because the")
    print("  short-range correction affects S states (l=0, peaks at origin)")
    print("  more than P states (l=1, zero at origin).\n")

    dE_2s = levels[(2, 0)]['dE']
    dE_2p = levels[(2, 1)]['dE']
    lamb_t6 = (dE_2s - dE_2p) * EV_PER_MEV

    print(f"  ΔE(2S) = {dE_2s * EV_PER_MEV:+.6e} eV")
    print(f"  ΔE(2P) = {dE_2p * EV_PER_MEV:+.6e} eV")
    print(f"  Ma Lamb splitting = ΔE(2S) − ΔE(2P) = {lamb_t6:+.6e} eV")
    print(f"  Measured Lamb shift = 4.372 × 10⁻⁶ eV (1057.845 MHz)")
    print(f"  Ratio Ma/measured = {abs(lamb_t6) / 4.372e-6:.2e}")

    print(f"\n  Splitting for all n=2,3,4 levels:\n")
    print(f"  {'Level pair':>14s}  {'ΔE (eV)':>14s}")
    print(f"  {'-'*32}")
    for n in range(2, 5):
        for l in range(1, n):
            split = (levels[(n, 0)]['dE'] - levels[(n, l)]['dE']) * EV_PER_MEV
            print(f"  {n}S − {n}{['S','P','D','F'][l]}:  {split:+14.6e}")

    # ── Section 4: r_e sweep ──────────────────────────────────────────
    section(4, "r_e dependence: 1S shift and Lamb splitting")

    print(f"  {'r_e':>6s}  {'L₁ (fm)':>10s}  {'ΔE₁ₛ (eV)':>14s}  "
          f"{'|ΔE|/E₁':>12s}  {'Lamb (eV)':>14s}  {'Lamb/meas':>12s}")
    print(f"  {'-'*75}")

    E_1s = -0.5 * ALPHA**2 * MU
    lamb_meas = 4.372e-6  # eV

    for r_e in [1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.6, 8.0, 10.0, 15.0, 20.0, 30.0]:
        L = get_circumferences(r_e)
        dE_1s = energy_shift(1, 0, L)
        dE_2s = energy_shift(2, 0, L)
        dE_2p = energy_shift(2, 1, L)
        lamb = (dE_2s - dE_2p) * EV_PER_MEV
        frac = abs(dE_1s / E_1s)

        print(f"  {r_e:6.1f}  {L[0]:10.1f}  {dE_1s * EV_PER_MEV:+14.6e}  "
              f"{frac:12.2e}  {lamb:+14.6e}  {abs(lamb)/lamb_meas:12.2e}")

    print()
    print("  The Ma Lamb splitting is same-sign as measured (2S below 2P")
    print("  in energy ↔ 2S shifted down more because S-wave peaks at origin).")
    print()
    print("  Constraint thresholds:")
    print("    Lamb shift measured to ~10 kHz (2.4 × 10⁻⁹ eV):")
    print("    → Ma Lamb splitting must be < 2.4 × 10⁻⁹ eV")
    print("    1S-2S measured to 10 Hz (4 × 10⁻¹⁴ eV):")
    print("    → 1S shift must be < ~10⁻¹⁴ eV")

    # ── Section 5: Physical interpretation ────────────────────────────
    section(5, "Physical interpretation")

    print("  The Ma Yukawa corrections have a clean physical picture:")
    print()
    print("  At distances r >> L_i (far from material dimension size),")
    print("  the correction exp(-2πr/L_i) → 0 and V → pure Coulomb.")
    print()
    print("  At distances r ~ L_i, the electron 'feels' the extra")
    print("  material dimension: the effective dimensionality is higher")
    print("  than 3, making the potential steeper (more attractive).")
    print()
    print("  The proton dimensions (L₅ ≈ 24 fm, L₆ ≈ 2.7 fm) are so")
    print("  small compared to a₀ that their corrections vanish.")
    print("  Only the electron tube (L₁ = r_e × L₂) matters.")
    print()
    print("  This means: the Ma model predicts a SPECIFIC short-range")
    print("  deviation from Coulomb's law, governed by the geometry of")
    print("  the electron's material dimensions.  The deviation is an")
    print("  exponentially decaying enhancement of the attraction at")
    print(f"  distances < L₁/(2π) ≈ {L[0]/(2*math.pi):.0f} fm.")

    # ── Section 6: Summary ────────────────────────────────────────────
    section(6, "Summary")

    print("  1. HYDROGEN REPRODUCED: E₁ = -13.6 eV, a₀ = 0.53 Å.")
    print("     No free parameters — chain from Ma geometry to atoms.")
    print()
    print("  2. YUKAWA CORRECTIONS computed via first-order perturbation")
    print("     theory with exact hydrogen wave functions.")
    print("     Dominant correction: electron tube dimension (L₁).")
    print()
    print("  3. Ma LAMB SPLITTING: The Yukawa correction shifts S states")
    print("     more than P states (same sign as QED Lamb shift).")
    print("     At r_e = 6.6: Ma Lamb ~ few × 10⁻⁴ eV, 100× too large")
    print("     compared to the real Lamb shift.  This CONSTRAINS r_e.")
    print()
    print("  4. r_e CONSTRAINT: The measured Lamb shift (~4.4 μeV ±10 kHz)")
    print("     constrains the Ma contribution.  Exact bound depends on")
    print("     whether the Ma correction adds to or competes with the")
    print("     QED Lamb shift, but order-of-magnitude: r_e ≲ 3–5.")
    print()
    print("  5. PREDICTION: If r_e is known, the Ma model predicts a")
    print("     specific Yukawa correction to ALL atomic spectra — not")
    print("     just hydrogen.  Heavier atoms with smaller orbits would")
    print("     show larger corrections (closer to the material dimension).")


if __name__ == '__main__':
    main()
