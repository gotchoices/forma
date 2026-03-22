#!/usr/bin/env python3
"""
R24 Track 1: T³ mode structure and neutrino flavors.

QUESTION
========
Can the three neutrino mass eigenstates arise from modes on the third
compact dimension of T³?

The electron uses two of three compact dimensions: mode (1,2,0) on
the T² subplane (θ₁, θ₂).  Modes with n₁ = 0 are automatically
uncharged (R19: charge requires n₁ = ±1).  If the third dimension
has circumference L₃ >> L₁, L₂, the lightest uncharged modes are
pure θ₃ modes (0, 0, n₃) with mass ∝ n₃/L₃.

KEY INSIGHT: The mass-squared ratio Δm²₃₁/Δm²₂₁ for modes (0,0,n_a),
(0,0,n_b), (0,0,n_c) is exactly (n_c² − n_a²)/(n_b² − n_a²).
This depends ONLY on integers — it's parameter-free.

SETUP
=====
Flat T³ lattice:
  a₁ = L₁ ê_x
  a₂ = s₁₂ L₁ ê_x + L₂ ê_y
  a₃ = s₁₃ L₁ ê_x + s₂₃ L₂ ê_y + L₃ ê_z

Reciprocal lattice → wavevector of mode (n₁, n₂, n₃):
  k_x = 2πn₁/L₁
  k_y = 2π(n₂ − n₁ s₁₂)/L₂
  k_z = 2π(n₃ − n₂ s₂₃ − n₁(s₁₃ − s₁₂ s₂₃))/L₃

E(n) = hc|k| = hc√(q₁² /L₁² + q₂² /L₂² + q₃² /L₃²)
where q₁=n₁, q₂=n₂−n₁s₁₂, q₃=n₃−n₂s₂₃−n₁(s₁₃−s₁₂s₂₃).
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, alpha, m_e, e as e_charge

m_e_eV = m_e * c**2 / 1.602176634e-19
eV_to_J = 1.602176634e-19
hc_eVm = h * c / eV_to_J  # hc in eV·m

# Experimental neutrino parameters (PDG 2024, normal ordering)
DM2_21 = 7.53e-5    # eV²  (solar)
DM2_32 = 2.455e-3   # eV²  (atmospheric)
DM2_31 = DM2_32 + DM2_21  # ≈ 2.530e-3 eV²
TARGET_RATIO = DM2_31 / DM2_21


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
    fs = [f(si) for si in ss]
    for i in range(len(fs) - 1):
        if fs[i] * fs[i + 1] < 0:
            return brentq(f, ss[i], ss[i + 1], xtol=1e-14)
    return None


def energy_ratio_t3(n1, n2, n3, r, r3, s12, s13=0.0, s23=0.0):
    """
    E(n₁,n₂,n₃) / E_electron on flat T³.

    Returns the ratio; multiply by m_e c² for absolute energy.
    """
    q1 = n1
    q2 = n2 - n1 * s12
    q3 = n3 - n2 * s23 - n1 * (s13 - s12 * s23)

    q1e = 1
    q2e = 2 - s12
    q3e = -2 * s23 - (s13 - s12 * s23)

    esq = q1**2 + (q2 / r)**2 + (q3 / r3)**2
    esq_e = q1e**2 + (q2e / r)**2 + (q3e / r3)**2

    if esq <= 0 or esq_e <= 0:
        return 0.0
    return math.sqrt(esq / esq_e)


def main():
    print("=" * 76)
    print("R24 Track 1: T³ Mode Structure and Neutrino Flavors")
    print("=" * 76)

    # ================================================================
    # SECTION 1: Setup
    # ================================================================
    print()
    print("SECTION 1: T³ geometry")
    print("-" * 76)
    print()

    r_values = [3.0, 5.0, 10.0]
    s12_map = {}
    for r in r_values:
        s12 = solve_electron_s(r)
        s12_map[r] = s12
        denom = math.sqrt(1 + ((2 - s12) / r)**2)
        print(f"  r = {r:5.1f}:  s₁₂ = {s12:.8f},  "
              f"√(1+((2−s)/r)²) = {denom:.6f}")

    r = 5.0
    s12 = s12_map[r]
    denom_e = math.sqrt(1 + ((2 - s12) / r)**2)
    print()
    print(f"Reference geometry: r = {r}, s₁₂ = {s12:.8f}")
    print(f"Initially s₁₃ = s₂₃ = 0 (decoupled third dimension).")
    print()

    # Verify electron energy
    r3_test = 1e8
    E_check = energy_ratio_t3(1, 2, 0, r, r3_test, s12)
    print(f"Electron (1,2,0) energy check: E/E_e = {E_check:.10f}")
    print()

    # ================================================================
    # SECTION 2: Uncharged mode catalog
    # ================================================================
    print("=" * 76)
    print("SECTION 2: Uncharged modes on T³  (n₁ = 0)")
    print("=" * 76)
    print()
    print("Modes with n₁ = 0 carry zero charge (R19: charge requires n₁ = ±1).")
    print("With s₁₃ = s₂₃ = 0, the energy simplifies to:")
    print("  E(0, n₂, n₃)/E_e = √((n₂/r)² + (n₃/r₃)²) / √(1 + ((2−s)/r)²)")
    print()
    print("Since r₃ >> r, modes with n₂ ≠ 0 have E ~ m_e/r ≫ neutrino scale.")
    print("The lightest uncharged modes are pure θ₃ modes: (0, 0, n₃).")
    print()

    print(f"  {'mode':>12}  {'E/E_e':>14}  {'E (eV)':>12}  {'type':>20}")
    print("  " + "-" * 64)

    for n3 in range(1, 6):
        E_ratio = energy_ratio_t3(0, 0, n3, r, r3_test, s12)
        E_eV = E_ratio * m_e_eV
        print(f"  (0, 0,{n3:+2d})   {E_ratio:14.6e}  {E_eV:12.4e}  "
              f"pure θ₃")

    print("  " + "." * 64)
    for n2 in [1, -1]:
        for n3 in [0, 1]:
            if n2 == 0 and n3 == 0:
                continue
            E_ratio = energy_ratio_t3(0, n2, n3, r, r3_test, s12)
            E_eV = E_ratio * m_e_eV
            label = "pure θ₂" if n3 == 0 else "mixed"
            print(f"  (0,{n2:+2d},{n3:+2d})   {E_ratio:14.6e}  {E_eV:12.4e}  "
                  f"{label}")

    print()
    print("  The pure θ₃ modes are lighter than θ₂ modes by factor")
    print(f"  r/r₃ = {r}/{r3_test:.0e} = {r/r3_test:.1e}.")
    print()

    # ================================================================
    # SECTION 3: Mass-squared ratio — integer search
    # ================================================================
    print("=" * 76)
    print("SECTION 3: Mass-squared ratio from integer triplets")
    print("=" * 76)
    print()
    print("For modes (0,0,n_a), (0,0,n_b), (0,0,n_c) with n_a < n_b < n_c:")
    print("  m(n₃) ∝ n₃   →   Δm²₃₁/Δm²₂₁ = (n_c² − n_a²)/(n_b² − n_a²)")
    print()
    print("This ratio depends ONLY on integers — parameter-free prediction.")
    print()
    print(f"Target: Δm²₃₁/Δm²₂₁ = {TARGET_RATIO:.2f}")
    print(f"Uncertainty: ≈ ±0.9 (propagated from PDG 2024)")
    print()

    sigma_ratio = 0.9

    print(f"  {'(n_a,n_b,n_c)':>16}  {'ratio':>8}  {'Δratio':>8}  "
          f"{'|Δ|/σ':>6}  {'Σm/m₁':>6}")
    print("  " + "-" * 56)

    solutions = []
    for na in range(1, 12):
        for nb in range(na + 1, 30):
            denom = nb**2 - na**2
            nc_sq = TARGET_RATIO * denom + na**2
            nc_exact = math.sqrt(nc_sq)
            for nc in [int(nc_exact), int(nc_exact) + 1]:
                if nc <= nb or nc > 50:
                    continue
                ratio = (nc**2 - na**2) / denom
                delta = ratio - TARGET_RATIO
                nsigma = abs(delta) / sigma_ratio
                sum_m = (na + nb + nc) / na
                if nsigma < 2.0:
                    solutions.append((na, nb, nc, ratio, delta, nsigma, sum_m))

    solutions.sort(key=lambda x: (x[5], x[0]))
    shown = set()
    count = 0
    for na, nb, nc, ratio, delta, nsigma, sum_m in solutions:
        key = (na, nb, nc)
        if key in shown:
            continue
        shown.add(key)
        marker = ""
        if na == 1 and nb == 2 and nc == 10:
            marker = " ← minimal"
        print(f"  ({na:2d},{nb:2d},{nc:2d})        {ratio:8.2f}  "
              f"{delta:+8.2f}   {nsigma:5.2f}  {sum_m:6.1f}{marker}")
        count += 1
        if count >= 15:
            break

    print()
    print(f"  Total triplets within 2σ (n_c ≤ 50): {len(shown)}")
    print()

    # Check if consecutive modes ever work
    print("  Consecutive modes (n, n+1, n+2):")
    print("    ratio = (4n+4)/(2n+1),  max at n=1: 8/3 = 2.67")
    print("    IMPOSSIBLE to reach 33.6 → gap between ν₂ and ν₃ is required.")
    print()

    # ================================================================
    # SECTION 4: Required third dimension size
    # ================================================================
    print("=" * 76)
    print("SECTION 4: Physical size of third compact dimension")
    print("=" * 76)
    print()

    # L₃ = hc × √((n_b²−n_a²)/Δm²₂₁), independent of r!
    # Because r₃ and L₁ both depend on denom_e, which cancels.

    print("Derivation:")
    print("  m(0,0,n₃) = (hc/L₁) × n₃/r₃ × 1/denom_e  [wrong — see below]")
    print()
    print("Actually: E(0,0,n₃) = hc × n₃/L₃  (direct from wavevector)")
    print("and E_e = hc × denom_e/L₁ = m_e c².")
    print("Since L₃ = r₃ × L₁:")
    print("  E(0,0,n₃) = hc × n₃/(r₃ L₁) = m_e c² × n₃/(r₃ × denom_e)")
    print()
    print("  Δm²₂₁ = m_b² − m_a² = (hc)²(n_b² − n_a²)/L₃²")
    print("  → L₃ = hc × √((n_b² − n_a²)/Δm²₂₁)")
    print()
    print("NOTE: L₃ is INDEPENDENT of r, s₁₂, and all T² parameters!")
    print()

    best_solutions = [(1, 2, 10), (2, 3, 13), (4, 5, 18), (5, 6, 20)]

    print(f"  {'(n_a,n_b,n_c)':>16}  {'ratio':>8}  {'L₃ (μm)':>10}  "
          f"{'m₁ (meV)':>10}  {'m₂ (meV)':>10}  {'m₃ (meV)':>10}  "
          f"{'Σm (meV)':>10}")
    print("  " + "-" * 90)

    for na, nb, nc in best_solutions:
        ratio = (nc**2 - na**2) / (nb**2 - na**2)
        L3 = hc_eVm * math.sqrt((nb**2 - na**2) / DM2_21)
        L3_um = L3 * 1e6

        m1 = hc_eVm * na / L3
        m2 = hc_eVm * nb / L3
        m3 = hc_eVm * nc / L3
        sum_m = m1 + m2 + m3

        print(f"  ({na:2d},{nb:2d},{nc:2d})        {ratio:8.1f}  "
              f"{L3_um:10.1f}  "
              f"{m1*1e3:10.2f}  {m2*1e3:10.2f}  {m3*1e3:10.2f}  "
              f"{sum_m*1e3:10.1f}")

    print()
    print("  Cosmological bound: Σm < 120 meV  (Planck 2018)")
    print()

    # Focus on minimal (1,2,10)
    na, nb, nc = 1, 2, 10
    L3 = hc_eVm * math.sqrt(3 / DM2_21)
    L3_um = L3 * 1e6
    m1 = hc_eVm / L3
    m2 = 2 * m1
    m3 = 10 * m1

    print(f"  --- Focus: (1, 2, 10) ---")
    print(f"  L₃ = {L3_um:.1f} μm  (circumference of third dimension)")
    print(f"  Radius = L₃/(2π) = {L3_um/(2*math.pi):.1f} μm")
    print()
    print(f"  m₁ = {m1*1e3:.3f} meV = {m1:.5f} eV")
    print(f"  m₂ = {m2*1e3:.3f} meV = {m2:.5f} eV")
    print(f"  m₃ = {m3*1e3:.3f} meV = {m3:.5f} eV")
    print(f"  m₂/m₁ = {m2/m1:.1f}  (prediction)")
    print(f"  m₃/m₁ = {m3/m1:.1f}  (prediction)")
    print(f"  Σm = {(m1+m2+m3)*1e3:.1f} meV = {m1+m2+m3:.4f} eV")
    print()
    print(f"  Δm²₂₁ = {(m2**2 - m1**2):.4e} eV²  "
          f"(exp: {DM2_21:.4e})")
    print(f"  Δm²₃₁ = {(m3**2 - m1**2):.4e} eV²  "
          f"(exp: {DM2_31:.4e})")
    print(f"  Ratio = {(m3**2 - m1**2)/(m2**2 - m1**2):.2f}  "
          f"(exp: {TARGET_RATIO:.2f})")
    print()

    # ================================================================
    # SECTION 5: Gravity constraint
    # ================================================================
    print("=" * 76)
    print("SECTION 5: Testability — gravity and extra dimensions")
    print("=" * 76)
    print()

    gravity_limit = 50  # μm (Eöt-Wash, Kapner et al. 2007)

    print(f"  Current short-range gravity test: Newton's law verified")
    print(f"  down to ~{gravity_limit} μm (Eöt-Wash experiment).")
    print()
    print(f"  For (1,2,10): L₃ = {L3_um:.0f} μm  (circumference)")
    print(f"                L₃/(2π) = {L3_um/(2*math.pi):.0f} μm  (radius)")
    print()

    if L3_um > gravity_limit:
        print(f"  ⚠ L₃ > {gravity_limit} μm.  IF gravity propagates in")
        print(f"  the third dimension, this is ALREADY CONSTRAINED.")
    else:
        print(f"  L₃ < {gravity_limit} μm — below current limit.")

    print()
    print("  However, in this model the compact dimensions are where the")
    print("  photon lives.  Whether gravity propagates there depends on")
    print("  model details (not yet specified).  If gravity is confined")
    print("  to 3+1D, the constraint does not apply.")
    print()

    # ================================================================
    # SECTION 6: Modes between ν₂ and ν₃
    # ================================================================
    print("=" * 76)
    print("SECTION 6: Intermediate modes — sterile neutrinos?")
    print("=" * 76)
    print()
    print(f"For (1,2,10): modes n₃ = 3,4,...,9 exist between ν₂ and ν₃.")
    print(f"If these thermalize in the early universe, N_eff would include")
    print(f"all 10 light species instead of 3.")
    print()
    print(f"  CMB constraint: N_eff = 2.99 ± 0.17 (Planck 2018)")
    print(f"  10 thermalized species: N_eff ≈ 10 × (4/11)^(4/3) ≈ 6.1")
    print(f"  → EXCLUDED at >18σ")
    print()
    print("Possible resolutions:")
    print("  1. The 7 intermediate modes don't thermalize (suppressed coupling)")
    print("  2. The modes that couple to W/Z are SELECTED by a quantum number")
    print("     (analogous to how only n₁=±1 carries charge)")
    print("  3. The assignment (1,2,10) is wrong — different mechanism for ν₃")
    print()

    # ================================================================
    # SECTION 7: Effect of T³ shear
    # ================================================================
    print("=" * 76)
    print("SECTION 7: Effect of T³ shear on spectrum")
    print("=" * 76)
    print()
    print("With s₁₃ = s₂₃ = 0, pure θ₃ modes (0,0,n₃) are unaffected by shear.")
    print("Only modes with n₁ ≠ 0 or n₂ ≠ 0 are shifted.")
    print()
    print("Testing: do s₁₃, s₂₃ modify the pure θ₃ spectrum?")
    print()

    for s23_test in [0, 0.1, 0.3]:
        for s13_test in [0, 0.1]:
            if s13_test == 0 and s23_test == 0:
                continue
            energies = []
            for n3 in [1, 2, 10]:
                E = energy_ratio_t3(0, 0, n3, r, r3_test, s12, s13_test, s23_test)
                energies.append(E)

            dm21 = energies[1]**2 - energies[0]**2
            dm31 = energies[2]**2 - energies[0]**2
            ratio_test = dm31 / dm21 if dm21 > 0 else float('inf')

            print(f"  s₁₃={s13_test:.1f}, s₂₃={s23_test:.1f}:  "
                  f"E₁={energies[0]:.6e}  E₂={energies[1]:.6e}  "
                  f"E₁₀={energies[2]:.6e}  "
                  f"ratio={ratio_test:.2f}")

    print()
    print("Pure θ₃ modes (n₁=n₂=0) are IMMUNE to shear.")
    print("Shear only enters via q₃ = n₃ − n₂s₂₃ − n₁(s₁₃ − s₁₂s₂₃),")
    print("and for n₁=n₂=0: q₃ = n₃ exactly.")
    print()

    # But shear DOES affect the electron and mixed modes:
    print("Shear DOES affect the electron (1,2,0) and mixed modes:")
    for s23_test in [0, 0.01, 0.1]:
        E_e_shifted = energy_ratio_t3(1, 2, 0, r, r3_test, s12, 0, s23_test)
        print(f"  s₂₃={s23_test:.2f}:  E_e(1,2,0)/E_e(ref) = {E_e_shifted:.10f}")
    print()
    print("At s₂₃ = 0.1, the electron energy shifts by ~10⁻¹⁸ (negligible")
    print("because r₃ = 10⁸ and the s₂₃ correction goes as 1/r₃²).")
    print()

    # ================================================================
    # SECTION 8: Spin question
    # ================================================================
    print("=" * 76)
    print("SECTION 8: Spin of (0,0,n₃) modes — open question")
    print("=" * 76)
    print()
    print("Neutrinos are spin-½ fermions.  In the WvM model, spin-½ arises")
    print("from the (1,2) winding topology: the photon's polarization vector")
    print("rotates by π (not 2π) per symmetry-axis revolution → spinor.")
    print()
    print("Mode (0,0,n₃) has NO winding in θ₁ or θ₂.  It is a standing")
    print("wave purely in the third dimension.  Whether it carries spin-½")
    print("depends on the T³ embedding topology:")
    print()
    print("  • If T³ = T² × S¹ (product): θ₃ is a flat circle → spin 0")
    print("  • If T³ has non-trivial fibration: θ₃ could inherit spinor")
    print("    structure from the T² base → spin ½ possible")
    print()
    print("This requires analytical work (beyond this numerical study).")
    print("CRITICAL: if (0,0,n₃) modes are spin-0, they CANNOT be neutrinos.")
    print()

    # ================================================================
    # SECTION 9: Parameter counting
    # ================================================================
    print("=" * 76)
    print("SECTION 9: Parameter counting")
    print("=" * 76)
    print()

    print("T³ parameters (total):")
    print("  L₁ (overall scale)            — fixed by m_e")
    print("  r = L₂/L₁ (aspect ratio)      — FREE")
    print("  s₁₂ (T² shear)                — fixed by α(r)")
    print("  r₃ = L₃/L₁ (third dim ratio)  — fixed by Δm²₂₁ + mode assignment")
    print("  s₁₃ (θ₁-θ₃ shear)             — FREE (but decoupled at leading order)")
    print("  s₂₃ (θ₂-θ₃ shear)             — FREE (but decoupled at leading order)")
    print()
    print("  Free continuous parameters: 3 (r, s₁₃, s₂₃)")
    print("  [L₁, s₁₂, r₃ are fixed by m_e, α, Δm²₂₁]")
    print()
    print("  Discrete choice: mode assignment (n_a, n_b, n_c)")
    print("  — constrained by Δm²₃₁/Δm²₂₁ = 33.6 → (1,2,10) etc.")
    print()

    print("Observable targets:")
    print("  α = 1/137.036                  — fixes s₁₂(r)           [used]")
    print("  m_e = 0.511 MeV                — fixes L₁               [used]")
    print("  Δm²₂₁ = 7.53×10⁻⁵ eV²         — fixes L₃               [used]")
    print("  Δm²₃₁/Δm²₂₁ ≈ 33.6            — integer constraint     [used]")
    print("  θ₁₂ = 33.4° (solar mixing)     — constrains s₁₃, s₂₃   [available]")
    print("  θ₂₃ = 49.0° (atmospheric)      — constrains s₁₃, s₂₃   [available]")
    print("  θ₁₃ = 8.6° (reactor)           — constrains s₁₃, s₂₃   [available]")
    print("  δ_CP ≈ 195° (CP phase)         — additional constraint  [available]")
    print()
    print("  Remaining free params: r, s₁₃, s₂₃  (3 parameters)")
    print("  Remaining constraints: θ₁₂, θ₂₃, θ₁₃, δ_CP  (4 observables)")
    print()
    print("  → OVER-DETERMINED: 4 constraints on 3 parameters")
    print("  → r is PREDICTED (not free)")
    print("  → Model is FALSIFIABLE")
    print()
    print("  NOTE: This assumes the PMNS mixing matrix arises from T³ shear.")
    print("  The mapping mixing angles → (r, s₁₃, s₂₃) needs explicit derivation.")
    print()

    # ================================================================
    # SECTION 10: Predictions summary
    # ================================================================
    print("=" * 76)
    print("SECTION 10: Summary and predictions")
    print("=" * 76)
    print()

    print("FINDINGS:")
    print()
    print("F1. Modes with n₁ = 0 on T³ are automatically uncharged.")
    print("    Natural neutrino candidates on the same geometry as the electron.")
    print()
    print("F2. The lightest uncharged modes are pure θ₃: (0,0,n₃) with m ∝ n₃/L₃.")
    print("    Mixed modes (0,n₂≠0,n₃) have m ~ m_e/r — far too heavy.")
    print()
    print("F3. Mass-squared ratio is determined by integers alone:")
    ratio_pred = (10**2 - 1) / (4 - 1)
    print(f"    (n_c² − n_a²)/(n_b² − n_a²) for (1,2,10) = {ratio_pred:.1f}")
    print(f"    Experiment: {TARGET_RATIO:.1f} ± 0.9")
    print(f"    Agreement: {abs(ratio_pred - TARGET_RATIO)/sigma_ratio:.1f}σ")
    print()
    print(f"F4. L₃ is fixed by Δm²₂₁ alone: L₃ = {L3_um:.0f} μm.")
    print(f"    Independent of r, s₁₂, or any T² parameter.")
    print()
    print(f"F5. Predicted masses (1,2,10 assignment):")
    print(f"    m₁ = {m1*1e3:.2f} meV,  m₂ = {m2*1e3:.2f} meV,  "
          f"m₃ = {m3*1e3:.2f} meV")
    print(f"    m₂/m₁ = 2 exactly,  m₃/m₁ = 10 exactly")
    print(f"    Σm = {(m1+m2+m3)*1e3:.1f} meV  (< 120 meV cosmological bound ✓)")
    print()
    print("F6. T³ shear does NOT modify the pure θ₃ spectrum (proven above).")
    print("    The mass-squared ratio is a robust integer prediction.")
    print()
    print("F7. Parameter counting: 3 free continuous (r, s₁₃, s₂₃) vs")
    print("    4 mixing observables → over-determined → r predicted + falsifiable.")
    print()
    print("OPEN QUESTIONS:")
    print()
    print("  Q1. Do (0,0,n₃) modes carry spin-½?  If not, they cannot be")
    print("      neutrinos.  Requires analysis of T³ fibration topology.")
    print()
    print("  Q2. What suppresses modes n₃ = 3–9?  The N_eff constraint")
    print("      excludes thermalized sterile species.  Need a coupling")
    print("      selection rule or non-thermalization argument.")
    print()
    print("  Q3. Does the PMNS matrix arise from (s₁₃, s₂₃)?  Explicit")
    print("      derivation needed.  If successful, r is predicted.")
    print()
    print(f"  Q4. Is L₃ ~ {L3_um:.0f} μm compatible with gravity tests?")
    print("      Depends on whether gravity propagates in compact dims.")
    print()


if __name__ == "__main__":
    main()
