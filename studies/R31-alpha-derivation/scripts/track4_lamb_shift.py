#!/usr/bin/env python3
"""
R31 Track 4: Hydrogen Lamb shift as a probe of r_e.

The Ma geometry produces KK massive gauge bosons with masses
M_KK = n × 2πℏc / L_tube.  These generate Yukawa corrections
to the Coulomb potential:

    V(r) = -α/r × [1 + Σ_n exp(-M_n r)]

The Yukawa terms modify the hydrogen 2S-2P splitting (Lamb shift).
Standard QED predicts 1057.833 MHz.  Measured: 1057.845(9) MHz.
The residual ~0.012 MHz (with large uncertainty) could constrain r_e.

We compute the Ma Yukawa contribution to the Lamb shift as a
function of r_e and find the r_e (if any) that matches.
"""

import sys, os, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma import (
    alpha_ma, mu_12, solve_shear_for_alpha,
    hbar_c_MeV_fm, M_E_MEV, M_P_MEV, ALPHA,
)

TWO_PI_HC = 2 * math.pi * hbar_c_MeV_fm

a0_fm = hbar_c_MeV_fm / (M_E_MEV * ALPHA)  # Bohr radius in fm

LAMB_MEASURED = 1057.845  # MHz
LAMB_QED = 1057.833       # MHz (theoretical QED prediction)
LAMB_RESIDUAL = LAMB_MEASURED - LAMB_QED  # ~0.012 MHz

print("=" * 72)
print("R31 TRACK 4: HYDROGEN LAMB SHIFT AS r_e PROBE")
print("=" * 72)


# ── Section 1: The Lamb shift and Ma contribution ───────────────

print("\n\n── Section 1: Lamb shift overview ──\n")

print(f"  Lamb shift (2S₁/₂ − 2P₁/₂ splitting in hydrogen):")
print(f"    Measured:     {LAMB_MEASURED:.3f} ± 0.009 MHz")
print(f"    QED theory:   {LAMB_QED:.3f} MHz")
print(f"    Residual:     {LAMB_RESIDUAL:+.3f} ± 0.009 MHz")
print()
print(f"  The residual is within experimental uncertainty —")
print(f"  could be zero, or could be new physics (Ma Yukawa).")
print()
print(f"  Bohr radius: a₀ = {a0_fm:,.0f} fm")
print(f"  For Ma Yukawa to affect 2S-2P:")
print(f"    Yukawa range must be comparable to a₀")
print(f"    → KK mass M ~ ℏc/a₀ = {hbar_c_MeV_fm/a0_fm*1e6:.1f} eV")
print(f"    Or shorter range if the 2S wavefunction overlaps")
print(f"    the Yukawa well (2S has ψ(0) ≠ 0)")


# ── Section 2: KK boson masses vs r_e ───────────────────────────

print("\n\n── Section 2: KK boson masses as function of r_e ──\n")

print(f"  The electron tube circumference L₁ = r_e × L₂.")
print(f"  First KK mass: M₁ = 2πℏc / L₁")
print()

r_e_values = [0.5, 1.0, 2.0, 3.0, 5.0, 6.6, 10.0, 20.0, 50.0, 68.0]

print(f"  {'r_e':>6s} {'L₂ (fm)':>10s} {'L₁ (fm)':>12s}"
      f" {'M₁ (MeV)':>10s} {'M₁ (eV)':>12s} {'a₀/L₁':>8s}")
print(f"  {'─'*62}")

for r_e in r_e_values:
    s = solve_shear_for_alpha(r_e)
    if s is None:
        continue
    mu = mu_12(r_e, s)
    E0 = M_E_MEV / mu
    L2 = TWO_PI_HC / E0
    L1 = r_e * L2
    M1 = TWO_PI_HC / L1
    print(f"  {r_e:6.1f} {L2:10.0f} {L1:12.0f}"
          f" {M1:10.6f} {M1*1e6:12.0f} {a0_fm/L1:8.1f}")


# ── Section 3: Yukawa correction to Lamb shift ──────────────────

print("\n\n── Section 3: Yukawa correction to 2S-2P splitting ──\n")

print("  The Yukawa correction modifies the Coulomb potential:")
print("    V(r) = −α/r × [1 + Σ_n e^{−n M₁ r}]")
print()
print("  For the Lamb shift (2S₁/₂ − 2P₁/₂):")
print("  The 2S state has |ψ(0)|² ≠ 0 (s-wave touches origin)")
print("  The 2P state has |ψ(0)|² = 0 (p-wave vanishes at origin)")
print()
print("  The Yukawa term is short-range → affects 2S much more than 2P")
print("  → shifts the 2S level relative to 2P → modifies Lamb shift")
print()
print("  First-order perturbation theory:")
print("  ΔE_2S ≈ −α × ∫ |ψ_2S(r)|² × Σ_n e^{−n M₁ r} / r × d³r")
print()
print("  For M₁ r ≫ 1 (Yukawa range ≪ Bohr radius),")
print("  the correction is exponentially suppressed:")
print("    ΔE_Lamb ∝ e^{−M₁ a₀}")
print()
print("  For M₁ a₀ ≫ 1, the Yukawa correction is negligible.")
print("  For M₁ a₀ ~ 1, it could be significant.")

# Compute for each r_e
print()
print(f"  {'r_e':>6s} {'M₁ (MeV)':>10s} {'M₁ a₀':>10s}"
      f" {'e^(−M₁a₀)':>12s} {'Regime':>20s}")
print(f"  {'─'*62}")

promising_re = []

for r_e in [0.3, 0.5, 1.0, 2.0, 3.0, 5.0, 6.6, 10.0, 20.0, 50.0, 68.0]:
    s = solve_shear_for_alpha(r_e)
    if s is None:
        continue
    mu = mu_12(r_e, s)
    E0 = M_E_MEV / mu
    L2 = TWO_PI_HC / E0
    L1 = r_e * L2
    M1 = TWO_PI_HC / L1

    M1_a0 = M1 * a0_fm / hbar_c_MeV_fm  # dimensionless
    exp_factor = math.exp(-M1_a0) if M1_a0 < 700 else 0.0

    if M1_a0 > 50:
        regime = "negligible"
    elif M1_a0 > 10:
        regime = "extremely small"
    elif M1_a0 > 1:
        regime = "suppressed"
    else:
        regime = "SIGNIFICANT"

    print(f"  {r_e:6.1f} {M1:10.6f} {M1_a0:10.1f}"
          f" {exp_factor:12.4e} {regime:>20s}")

    if M1_a0 < 100:
        promising_re.append({
            'r_e': r_e, 'M1': M1, 'M1_a0': M1_a0,
            'exp_factor': exp_factor,
        })


# ── Section 4: Quantitative Lamb shift correction ───────────────

print("\n\n── Section 4: Quantitative Yukawa Lamb shift ──\n")

print("  For hydrogen 2S state:")
print("    ψ_2S(r) = (1/4√(2π)) × (1/a₀)^{3/2} × (2 − r/a₀) × e^{−r/(2a₀)}")
print("    |ψ_2S(0)|² = 1/(8π a₀³)")
print()
print("  Contact approximation (Yukawa range ≪ a₀):")
print("    ΔE_contact = −4π α ℏc × |ψ_2S(0)|² × Σ_n 1/(n² M₁²)")
print("               = −α ℏc / (2 a₀³) × Σ_n 1/(n² M₁²)")
print()

# More careful: integrate with 2S wavefunction
def yukawa_lamb_correction(r_e, n_kk_max=10):
    """
    Compute ΔE_Lamb from Ma Yukawa corrections.

    Uses exact integration of 2S wavefunction with Yukawa potential.

    Returns ΔE in eV and in MHz.
    """
    s = solve_shear_for_alpha(r_e)
    if s is None:
        return None

    mu = mu_12(r_e, s)
    E0 = M_E_MEV / mu
    L2 = TWO_PI_HC / E0
    L1 = r_e * L2
    M1_MeV = TWO_PI_HC / L1

    # Convert to natural units where a₀ = 1
    # M₁ in units of 1/a₀: M1_nat = M1_MeV × a₀ / ℏc
    M1_nat = M1_MeV * a0_fm / hbar_c_MeV_fm

    # ΔE_2S from Yukawa: exact integral for each KK mode
    # V_Yuk(r) = −α/r × e^{−M_n r}
    # ΔE_2S = <2S|V_Yuk|2S> = −α × ∫₀^∞ |R_2S(r)|² × e^{−M_n r} / r × r² dr
    #       = −α × ∫₀^∞ R_2S² × e^{−M_n r} × r dr

    # R_2S(r) = (1/(2√2)) × (1/a₀)^{3/2} × (2 − r/a₀) × e^{−r/(2a₀)}
    # In a₀ = 1 units: R_2S(r) = (2−r)/(2√2) × e^{−r/2}

    # I(M) = ∫₀^∞ [(2−r)²/8] × e^{−r} × e^{−Mr} × r dr
    #       = (1/8) ∫₀^∞ (4r − 4r² + r³) × e^{−(1+M)r} dr

    # Using ∫₀^∞ r^n e^{−βr} dr = n!/β^{n+1}:
    # I(M) = (1/8) × [4/(1+M)² − 8/(1+M)³ + 6/(1+M)⁴]

    total_2S = 0.0
    total_2P = 0.0

    for n_kk in range(1, n_kk_max + 1):
        M = n_kk * M1_nat
        beta = 1 + M

        # 2S integral
        I_2S = (1.0/8) * (4.0/beta**2 - 8.0/beta**3 + 6.0/beta**4)
        total_2S += I_2S

        # 2P integral: R_2P(r) = r/(2√6 a₀) × e^{−r/(2a₀)}
        # In a₀ = 1: R_2P(r) = r/(2√6) × e^{−r/2}
        # I_2P(M) = ∫₀^∞ [r²/24] × e^{−r} × e^{−Mr} × r dr
        #         = (1/24) × 6/β⁴ = 1/(4β⁴)
        I_2P = 1.0 / (4 * beta**4)
        total_2P += I_2P

    # Energy in atomic units (Hartree = 2 × 13.6 eV)
    # ΔE = −α × (total_2S − total_2P) × E_H
    # where E_H = α² m_e c² / 2 = 13.6 eV (Hartree/2)

    # Actually: ΔE = −α × ℏc/a₀ × (total_2S − total_2P)
    #              = −α × (α m_e c²) × (total_2S − total_2P)
    #              = −α² m_e c² × (total_2S − total_2P)

    dE_eV = -ALPHA**2 * M_E_MEV * 1e6 * (total_2S - total_2P)
    dE_MHz = dE_eV * 241.799e6  # eV to Hz, then /1e6 to MHz... 
    # Actually: 1 eV = 241.799 THz = 241,799 GHz = 241,799,000 MHz
    dE_MHz = dE_eV * 241.799e6 / 1e6  # eV × (Hz/eV) / (MHz/Hz) ... no
    # Let me just convert properly
    # 1 eV = 1.602e-19 J, E = hf → f = E/h = 1.602e-19 / 6.626e-34 Hz
    # f = 2.4180e14 Hz = 241,800 GHz = 241.8 THz
    h_eV_s = 4.13567e-15  # eV·s (Planck constant)
    dE_Hz = dE_eV / h_eV_s
    dE_MHz_val = dE_Hz / 1e6

    return {
        'r_e': r_e, 'M1_MeV': M1_MeV, 'M1_nat': M1_nat,
        'dE_eV': dE_eV, 'dE_MHz': dE_MHz_val,
        'total_2S': total_2S, 'total_2P': total_2P,
    }


print(f"  Yukawa Lamb shift correction ΔE_Lamb(r_e):\n")
print(f"  {'r_e':>6s} {'M₁a₀':>8s} {'ΔE (eV)':>12s} {'ΔE (MHz)':>12s}"
      f" {'Regime':>16s}")
print(f"  {'─'*58}")

r_e_sweep = np.concatenate([
    np.linspace(0.3, 2.0, 18),
    np.linspace(2.5, 10.0, 16),
    np.linspace(12, 68, 15),
])

lamb_results = []

for r_e in r_e_sweep:
    res = yukawa_lamb_correction(r_e)
    if res is None:
        continue
    lamb_results.append(res)

    if res['M1_nat'] > 50:
        regime = "negligible"
    elif abs(res['dE_MHz']) < 0.001:
        regime = "< 0.001 MHz"
    elif abs(res['dE_MHz']) < 0.01:
        regime = "measurable?"
    elif abs(res['dE_MHz']) < 1:
        regime = "SIGNIFICANT"
    else:
        regime = "HUGE"

    if r_e in [0.3, 0.5, 1.0, 2.0, 5.0, 6.6, 10.0, 20.0, 50.0, 68.0] or \
       abs(res['dE_MHz'] - LAMB_RESIDUAL) < 0.01 * abs(LAMB_RESIDUAL):
        print(f"  {r_e:6.1f} {res['M1_nat']:8.1f} {res['dE_eV']:12.4e}"
              f" {res['dE_MHz']:12.6f} {regime:>16s}")

# Find r_e where correction matches residual
print(f"\n  Looking for r_e where |ΔE| = {LAMB_RESIDUAL:.3f} MHz...\n")

if lamb_results:
    dE_arr = np.array([r['dE_MHz'] for r in lamb_results])
    re_arr = np.array([r['r_e'] for r in lamb_results])
    abs_dE = np.abs(dE_arr)

    print(f"  Absolute correction range:")
    print(f"    |ΔE| = {min(abs_dE):,.0f} to {max(abs_dE):,.0f} MHz")
    print(f"    Lamb shift itself: {LAMB_MEASURED:.0f} MHz")
    print(f"    Residual: {LAMB_RESIDUAL:.3f} MHz")
    print()

    min_correction = min(abs_dE)
    max_correction = max(abs_dE)
    print(f"  ⚠ CRITICAL: Even the SMALLEST correction ({min_correction:,.0f} MHz)")
    print(f"    is {min_correction/LAMB_MEASURED:,.0f}× the ENTIRE Lamb shift!")
    print()
    print(f"  The naive KK Yukawa correction is catastrophically large")
    print(f"  at ALL viable r_e values (0.26 < r_e < 68.5).")
    print()
    print(f"  This means either:")
    print(f"    (a) The KK massive modes DON'T couple as assumed")
    print(f"    (b) There are cancellations between different KK towers")
    print(f"    (c) The effective theory breaks down at the tube scale")
    print(f"    (d) The naive Yukawa picture is wrong for Ma")


# ── Section 5: Constraints on r_e from Lamb shift ───────────────

print("\n\n── Section 5: Constraints on r_e ──\n")

print("  The Lamb shift measurement has uncertainty ±0.009 MHz.")
print("  The Ma Yukawa correction must satisfy:")
print(f"    |ΔE_Ma| < {LAMB_RESIDUAL + 0.009:.3f} MHz (upper bound)")
print()

print("  The Lamb shift constraint is moot — the naive Yukawa")
print("  correction is too large by factors of 10³ to 10⁶ to be")
print("  compatible with observation at ANY r_e.")
print()
print("  Full constraint landscape:")
print(f"    r_e < 0.26:      No α = 1/137 solution exists (R19)")
print(f"    r_e > 68.5:      Bohr radius < tube size (R30 F23)")
print(f"    Viable range:    0.26 < r_e < 68.5")
print(f"    Lamb shift:      ALL r_e ruled out by naive KK Yukawa")
print()
print("  This does NOT necessarily rule out the Ma model —")
print("  it rules out the NAIVE ASSUMPTION that each KK massive")
print("  mode couples with the same strength as the massless mode.")


# ── Section 6: Energy scale analysis ────────────────────────────

print("\n\n── Section 6: Why the Yukawa correction matters ──\n")

print("  The Lamb shift is a ~1000 MHz splitting.")
print("  QED accounts for it to 6 significant figures.")
print(f"  The residual ({LAMB_RESIDUAL:.3f} MHz) is at the 7th digit.")
print()
print("  The Ma Yukawa correction at r_e = 6.6:")
res_66 = yukawa_lamb_correction(6.6)
if res_66:
    print(f"    ΔE = {res_66['dE_MHz']:.4f} MHz")
    print(f"    This is {abs(res_66['dE_MHz'])/LAMB_MEASURED * 100:.4f}% of the Lamb shift")
    print(f"    Contact approximation: M₁a₀ = {res_66['M1_nat']:.1f}")
    if res_66['M1_nat'] < 2:
        print(f"    ⚠ M₁a₀ < 2 — not in the contact regime!")
        print(f"    The Yukawa range is comparable to the atom size.")
        print(f"    Contact approximation is unreliable here.")
    elif res_66['M1_nat'] > 10:
        print(f"    M₁a₀ > 10 — deep in the exponential suppression regime")
        print(f"    The correction is exponentially small and reliable.")

# At r_e = 1.0
res_1 = yukawa_lamb_correction(1.0)
if res_1:
    print(f"\n  At r_e = 1.0:")
    print(f"    ΔE = {res_1['dE_MHz']:.4f} MHz, M₁a₀ = {res_1['M1_nat']:.1f}")

# At r_e = 50
res_50 = yukawa_lamb_correction(50.0)
if res_50:
    print(f"\n  At r_e = 50:")
    print(f"    ΔE = {res_50['dE_MHz']:.6f} MHz, M₁a₀ = {res_50['M1_nat']:.1f}")


# ── Summary ──────────────────────────────────────────────────────

print("\n\n── Summary ──\n")

print("  1. The naive KK Yukawa correction to hydrogen is")
print("     CATASTROPHICALLY LARGE at all viable r_e values.")
print("     Even the smallest correction (at r_e ~ 0.3) is")
print("     ~300,000× the entire Lamb shift.")
print()
print("  2. At r_e = 6.6 (our working value), the correction")
print("     is ~35 MILLION MHz — 34,000× the Lamb shift.")
print("     This would completely destroy atomic spectroscopy.")
print()
print("  3. The correction falls as a POWER LAW in M₁a₀,")
print("     not exponentially.  This is because the 2S")
print("     wavefunction has |ψ(0)|² ≠ 0 and samples the")
print("     Yukawa potential near the origin, where it behaves")
print("     like pure Coulomb (before the exponential kills it).")
print()
print("  4. CONCLUSION: The naive KK Yukawa coupling is ruled")
print("     out.  The KK massive modes CANNOT couple to electrons")
print("     with the same strength (α) as the massless mode.")
print()
print("  5. This is actually a PREDICTION: Ma predicts that the")
print("     effective coupling of KK massive modes must be")
print("     suppressed relative to α.  The Lamb shift requires")
print("     suppression by a factor of at least ~10⁵.")
print()
print("  6. Possible suppression mechanisms:")
print("     (a) Wavefunction overlap — KK modes may not")
print("         overlap with point-like particle wavefunctions")
print("     (b) Renormalization — running coupling from the")
print("         KK mass scale down to atomic scales")
print("     (c) The gauge field is NOT simply off-diagonal")
print("         metric — it may have a different origin in Ma")
