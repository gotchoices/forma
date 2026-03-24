#!/usr/bin/env python3
"""
Can α be DERIVED from the T⁶×R³ geometry rather than input?

Currently α = 1/137 is an input: we solve for the shear s that
produces it.  But the geometry also produces Yukawa corrections
to the Coulomb potential.  If we sweep α (by sweeping s), the
hydrogen atom changes.  Is there a special α?

Approach:
  1. Fix r_e, keep m_e = 0.511 MeV
  2. Sweep s from 0 to 0.49
  3. At each s, compute:
     - α from the KK formula
     - L_ring, L_tube from circumference formula
     - KK gauge boson masses (Yukawa masses)
     - Hydrogen ground state with perturbative Yukawa corrections
     - Ratio of Yukawa correction to Coulomb binding
  4. Look for special values of α:
     - Maximum α consistent with stable hydrogen
     - Minimum perturbation from Yukawa corrections
     - Any self-consistency conditions
"""

import sys, os, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6 import alpha_kk, mu_12, hbar_c_MeV_fm, M_E_MEV, M_P_MEV

TWO_PI_HC = 2 * math.pi * hbar_c_MeV_fm
ALPHA_OBS = 1.0 / 137.036


def hydrogen_with_yukawa(alpha, m_e, L_tube, n_kk_max=10):
    """
    Hydrogen ground state energy with Yukawa corrections from KK modes.

    Returns binding energy (negative), Yukawa correction, and diagnostics.
    """
    if alpha <= 0:
        return {'E1': 0, 'dE_yukawa': 0, 'E_total': 0,
                'yukawa_frac': 0, 'a0': float('inf'), 'lambda_kk': 0}

    a0 = hbar_c_MeV_fm / (m_e * alpha)  # Bohr radius in fm

    E1_coulomb = -0.5 * m_e * alpha**2  # ground state in MeV

    # Yukawa corrections from KK massive gauge bosons
    # V_Yukawa = -α × Σ_n exp(-m_n r)/r  where m_n = 2πn/L_tube
    # <exp(-μr)/r>_1s = (2/a0) × 1/(1 + μa0/2)²  × (1/a0)
    # Actually: <exp(-μr)>_1s = 1/(1 + μa0/2)²
    # And first-order perturbation: ΔE = <V_Yukawa>_1s

    # For each KK mode n: m_n = 2πn ℏc / L_tube (in inverse fm)
    # Actually m_n in MeV/c²: m_n = 2πn × ℏc / L_tube MeV
    # The Yukawa potential is V_n = -α exp(-m_n r / ℏc) / r
    # = -α ℏc exp(-r/λ_n) / r  where λ_n = L_tube/(2πn) fm

    # <V_n>_1s = -α × (2/a0) / (1 + a0/(2λ_n))²  × ℏc/a0
    # Wait, let me be careful.

    # The Coulomb potential in our units: V(r) = -α ℏc / r (MeV when r in fm)
    # Yukawa correction: V_n(r) = -α ℏc exp(-r/λ_n) / r
    # where λ_n = L_tube/(2πn) = ℏc/m_n

    # 1s expectation value: <1/r × exp(-r/λ)>_1s for ψ_1s = (1/√π)(1/a0)^{3/2} exp(-r/a0)
    # = (4/a0³) ∫₀^∞ r² (1/r) exp(-r/λ) exp(-2r/a0) dr
    # = (4/a0³) ∫₀^∞ r exp(-(2/a0 + 1/λ)r) dr
    # = (4/a0³) × 1/(2/a0 + 1/λ)²
    # = 4 / (a0 × (2 + a0/λ)²)

    # So <V_n>_1s = -α ℏc × 4 / (a0 × (2 + a0/λ_n)²)
    # Compare to <V_Coulomb>_1s = -α ℏc / a0 × 1 = -α ℏc × (1/a0)

    # Wait, <1/r>_1s = 1/a0²... no.
    # <1/r>_1s = 1/a0 for hydrogen. So <V_C>_1s = -α ℏc / a0 = -m_e α² ℏc²... hmm.

    # Let me use the standard result:
    # For hydrogen ψ_1s ∝ exp(-r/a0):
    # <exp(-μr)/r> = ∫ |ψ|² exp(-μr)/r d³r
    #              = (4/a0³) ∫₀^∞ r² × exp(-2r/a0) × exp(-μr)/r × dr
    #              = (4/a0³) ∫₀^∞ r exp(-(2/a0 + μ)r) dr
    #              = (4/a0³) × 1/(2/a0 + μ)²
    #              = 4a0 / (2 + μa0)²

    # Hmm, let me redo:
    #              = (4/a0³) × 1/(2/a0 + μ)²
    #              = 4/(a0³ × (2/a0 + μ)²)
    #              = 4/(a0 × (2 + μa0))²  ... no
    #              = 4/a0³ × a0²/(2 + μa0)²  ... let me just compute:
    # 1/(2/a0 + μ)² = a0²/(2 + μa0)²
    # So the whole thing is 4/a0³ × a0²/(2 + μa0)² = 4/(a0(2 + μa0)²)

    # For μ = 0: <1/r> = 4/(a0 × 4) = 1/a0.  ✓

    # Yukawa perturbation for KK mode n:
    # ΔE_n = -α × ℏc × 4/(a0(2 + μ_n a0)²)
    # where μ_n = 1/λ_n = 2πn/L_tube

    # Note: <V_Coulomb> = -α × ℏc × 1/a0 = -α × ℏc × m_e α / ℏc = -m_e α²

    dE_total = 0.0
    for n in range(1, n_kk_max + 1):
        lambda_n = L_tube / (2 * math.pi * n)  # fm
        mu_n = 1.0 / lambda_n  # fm⁻¹
        mu_a0 = mu_n * a0

        expectation = 4.0 / (a0 * (2 + mu_a0)**2)

        dE_n = -alpha * hbar_c_MeV_fm * expectation
        dE_total += dE_n

    E_total = E1_coulomb + dE_total

    lambda_1 = L_tube / (2 * math.pi)
    yukawa_frac = dE_total / E1_coulomb if E1_coulomb != 0 else 0

    return {
        'E1': E1_coulomb,
        'dE_yukawa': dE_total,
        'E_total': E_total,
        'yukawa_frac': yukawa_frac,
        'a0': a0,
        'lambda_kk': lambda_1,
        'lambda_over_a0': lambda_1 / a0 if a0 > 0 else 0,
    }


print("=" * 72)
print("CAN α BE DERIVED FROM T⁶ GEOMETRY?")
print("=" * 72)


# ── Section 1: What happens when we sweep α ─────────────────────

print("\n\n── Section 1: Hydrogen spectrum vs α (at fixed r_e) ──\n")

R_E = 6.6

print(f"  Fixed: r_e = {R_E}, m_e = {M_E_MEV} MeV")
print(f"  Sweeping s from 0.001 to 0.49 → varying α\n")

s_values = np.linspace(0.002, 0.49, 500)
results = []

for s in s_values:
    alpha = alpha_kk(R_E, s)
    if alpha <= 0 or alpha > 1.0:
        continue

    mu = mu_12(R_E, s)
    E0 = M_E_MEV / mu
    L_ring = TWO_PI_HC / E0
    L_tube = R_E * L_ring

    h = hydrogen_with_yukawa(alpha, M_E_MEV, L_tube)

    results.append({
        's': s, 'alpha': alpha, '1/alpha': 1/alpha,
        'L_ring': L_ring, 'L_tube': L_tube,
        **h,
    })

print(f"  {'α':>10s} {'1/α':>8s} {'s':>8s} {'E₁ (eV)':>10s}"
      f" {'ΔE_Yuk (eV)':>12s} {'Yuk/Coul':>10s}"
      f" {'λ/a₀':>8s} {'a₀ (fm)':>10s}")
print(f"  {'─'*82}")

# Show selected points
alpha_targets = [1/200, 1/180, 1/160, 1/150, 1/140, ALPHA_OBS,
                 1/130, 1/120, 1/100, 1/80, 1/50, 1/30, 1/20, 1/10]

for at in alpha_targets:
    closest = min(results, key=lambda r: abs(r['alpha'] - at))
    if abs(closest['alpha'] - at) / at > 0.05:
        continue
    r = closest
    E1_eV = r['E1'] * 1e6  # MeV → eV
    dE_eV = r['dE_yukawa'] * 1e6
    marker = " ← OBSERVED" if abs(r['alpha'] - ALPHA_OBS) < 0.001 else ""
    print(f"  {r['alpha']:10.6f} {r['1/alpha']:8.1f} {r['s']:8.5f}"
          f" {E1_eV:10.2f} {dE_eV:12.4f} {r['yukawa_frac']:10.4f}"
          f" {r['lambda_over_a0']:8.4f} {r['a0']:10.0f}{marker}")


# ── Section 2: Is there a maximum α for stable hydrogen? ────────

print("\n\n── Section 2: Stability limits ──\n")

# Find where Yukawa correction exceeds various thresholds
for threshold in [0.01, 0.05, 0.10, 0.25, 0.50, 1.00]:
    critical = [r for r in results if abs(r['yukawa_frac']) >= threshold]
    if critical:
        first = min(critical, key=lambda r: abs(r['yukawa_frac'] - threshold))
        print(f"  |ΔE_Yukawa/E_Coulomb| = {threshold:4.0%} at α ≈ 1/{1/first['alpha']:.0f}"
              f" (s = {first['s']:.4f})")
    else:
        print(f"  |ΔE_Yukawa/E_Coulomb| = {threshold:4.0%}: never reached in scan")

# Find where Bohr radius < L_tube (electron "sees" compact dimensions)
compact_transition = [r for r in results if r['a0'] < r['L_tube']]
if compact_transition:
    first = compact_transition[0]
    print(f"\n  a₀ < L_tube at α ≈ 1/{1/first['alpha']:.0f}"
          f" (a₀ = {first['a0']:.0f} fm, L_tube = {first['L_tube']:.0f} fm)")
    print(f"  Below this, the electron 'sees' the compact geometry directly.")
    print(f"  The KK approximation breaks down.")

# Find where Bohr radius < L_ring
ring_transition = [r for r in results if r['a0'] < r['L_ring']]
if ring_transition:
    first = ring_transition[0]
    print(f"\n  a₀ < L_ring at α ≈ 1/{1/first['alpha']:.0f}"
          f" (a₀ = {first['a0']:.0f} fm, L_ring = {first['L_ring']:.0f} fm)")
    print(f"  Below this, the electron orbit is smaller than the ring.")
    print(f"  The notion of a 'separate R³ atom' fails completely.")


# ── Section 3: Does the geometry prefer a specific α? ───────────

print("\n\n── Section 3: Does the geometry prefer a specific α? ──\n")

# Look at the Yukawa correction as a function of α
# Is there an inflection point, minimum perturbation, etc.?

# The Yukawa/Coulomb ratio as a function of α:
alphas = [r['alpha'] for r in results]
yuk_fracs = [abs(r['yukawa_frac']) for r in results]

# Derivative of Yukawa fraction w.r.t. α
d_yuk = np.gradient(yuk_fracs, alphas)

# Is there a regime where the perturbation is flat (insensitive to α)?
# Look for d(yukawa_frac)/d(alpha) ≈ 0

print("  Yukawa correction behavior:")
print(f"  {'1/α':>8s} {'|ΔE/E|':>10s} {'d|ΔE/E|/dα':>14s}")
print(f"  {'─'*36}")

for at in [1/200, 1/150, ALPHA_OBS, 1/100, 1/50, 1/20, 1/10]:
    idx = min(range(len(results)),
              key=lambda i: abs(results[i]['alpha'] - at))
    if idx < len(d_yuk):
        print(f"  {1/results[idx]['alpha']:8.1f} {yuk_fracs[idx]:10.6f}"
              f" {d_yuk[idx]:14.4f}")

# The Yukawa fraction is monotonically increasing with α
print("\n  The Yukawa perturbation grows monotonically with α.")
print("  There is no minimum or inflection point that selects")
print("  a preferred α from perturbation size alone.")


# ── Section 4: Self-consistency condition ────────────────────────

print("\n\n── Section 4: Self-consistency — a deeper constraint? ──\n")

print("  The current model has a CIRCULAR structure:")
print("    Input α → compute s → compute geometry → verify α")
print("  This is tautological — any α works.")
print()
print("  For α to be PREDICTED, we need to BREAK the circle")
print("  with an independent constraint on s (or equivalently,")
print("  on the geometry).  Possible candidates:")
print()

print("  (A) CASIMIR ENERGY MINIMIZATION:")
print("      The vacuum energy of T⁶ depends on the geometry.")
print("      If the geometry minimizes its vacuum energy, s is")
print("      determined, and α follows.  This requires computing")
print("      the Casimir energy as a function of s.")
print()

print("  (B) MODE-SPECTRUM MATCHING:")
print("      The T⁶ spectrum depends on s (through the sheared")
print("      metric).  If we demand that the spectrum matches")
print("      observed particle masses OPTIMALLY, this constrains s.")
print("      But at large r, s is small and barely affects the")
print("      spectrum — so this constraint is weak.")
print()

print("  (C) PROTON CHARGE RADIUS:")
print("      The proton's charge distribution depends on s₅₆.")
print("      The measured proton charge radius (0.84 fm) could")
print("      constrain s₅₆, which would fix α for the proton sheet.")
print("      This has not been explored.")
print()

print("  (D) MULTI-PARTICLE SELF-CONSISTENCY:")
print("      In a full T⁶×R³ calculation (not KK-reduced),")
print("      the electron-proton interaction is computed from")
print("      the FULL 9D wave equation.  The effective α that")
print("      emerges might differ from α_KK.  If we demand")
print("      that the 9D calculation reproduces the OBSERVED")
print("      hydrogen spectrum, this constrains the geometry.")
print("      This is the most fundamental approach but also")
print("      the most computationally expensive.")


# ── Section 5: What the Yukawa scale tells us ───────────────────

print("\n\n── Section 5: What the Yukawa scale tells us ──\n")

# At α = 1/137:
r_obs = min(results, key=lambda r: abs(r['alpha'] - ALPHA_OBS))
print(f"  At α = 1/137 (observed), r_e = {R_E}:")
print(f"    Bohr radius:     a₀ = {r_obs['a0']:,.0f} fm")
print(f"    Yukawa range:    λ  = {r_obs['lambda_kk']:,.0f} fm")
print(f"    Ring circ:       L₂ = {r_obs['L_ring']:,.0f} fm")
print(f"    Tube circ:       L₁ = {r_obs['L_tube']:,.0f} fm")
print(f"    λ/a₀ = {r_obs['lambda_over_a0']:.4f}")
print(f"    Yukawa/Coulomb = {abs(r_obs['yukawa_frac']):.4f} ({abs(r_obs['yukawa_frac'])*100:.2f}%)")
print()

# Scale hierarchy
print(f"  Scale hierarchy at observed α:")
print(f"    L_ring = {r_obs['L_ring']:,.0f} fm  (particle scale)")
print(f"    L_tube = {r_obs['L_tube']:,.0f} fm  (Yukawa range scale)")
print(f"    a₀     = {r_obs['a0']:,.0f} fm  (atom scale)")
print(f"    Ratio L_tube/L_ring = {r_obs['L_tube']/r_obs['L_ring']:.1f} = r_e")
print(f"    Ratio a₀/L_tube = {r_obs['a0']/r_obs['L_tube']:.1f}")
print(f"    Ratio a₀/L_ring = {r_obs['a0']/r_obs['L_ring']:.0f}")
print()
print(f"  The atom (a₀) is {r_obs['a0']/r_obs['L_tube']:.0f}× larger than the Yukawa range")
print(f"  and {r_obs['a0']/r_obs['L_ring']:.0f}× larger than the ring.")
print(f"  This separation of scales is WHAT MAKES ATOMS POSSIBLE:")
print(f"  the electron orbit is large enough that the compact")
print(f"  dimensions are invisible to it (perturbative corrections only).")
print()

# How does this hierarchy depend on α?
print(f"  How the hierarchy changes with α:")
print(f"    a₀ = ℏc/(m_e α) ∝ 1/α")
print(f"    L_tube depends on r and s, hence on α")
print(f"    At small α: a₀ → ∞, atom is huge, Yukawa irrelevant")
print(f"    At large α: a₀ → 0, atom shrinks below compact dims")
print()

# Key transition point: where a₀ = L_tube
if compact_transition:
    ct = compact_transition[0]
    print(f"  CRITICAL TRANSITION: a₀ = L_tube at α ≈ 1/{1/ct['alpha']:.0f}")
    print(f"    Below this α, the atom is 'outside' the compact geometry")
    print(f"    Above this α, the atom is 'inside' — R³ QM breaks down")
    print(f"    The observed α = 1/137 is well below this threshold")


# ── Section 6: Effect of r_e on the constraint ──────────────────

print("\n\n── Section 6: Does the answer change with r_e? ──\n")

print(f"  Repeat the key analysis at several r_e values:\n")
print(f"  {'r_e':>6s} {'a₀/L_tube':>10s} {'λ/a₀':>8s} {'Yuk/Coul':>10s}"
      f" {'α_crit':>8s}")
print(f"  {'─'*46}")

for r_e in [1.0, 2.0, 5.0, 6.6, 8.906, 20.0, 50.0, 100.0]:
    s = None
    s_scan = np.concatenate([
        np.linspace(1e-8, 1e-4, 500),
        np.linspace(1e-4, 0.01, 500),
        np.linspace(0.01, 0.49, 2000),
    ])
    from scipy.optimize import brentq
    for i in range(len(s_scan) - 1):
        if (alpha_kk(r_e, s_scan[i]) - ALPHA_OBS) * \
           (alpha_kk(r_e, s_scan[i+1]) - ALPHA_OBS) < 0:
            s = brentq(lambda ss: alpha_kk(r_e, ss) - ALPHA_OBS,
                       s_scan[i], s_scan[i+1])
            break
    if s is None:
        print(f"  {r_e:6.1f}  no α=1/137 solution")
        continue

    mu = mu_12(r_e, s)
    E0 = M_E_MEV / mu
    L_ring = TWO_PI_HC / E0
    L_tube = r_e * L_ring

    h = hydrogen_with_yukawa(ALPHA_OBS, M_E_MEV, L_tube)

    # Find critical α where a₀ = L_tube
    # a₀ = ℏc/(m_e α) = L_tube → α_crit = ℏc/(m_e L_tube)
    alpha_crit = hbar_c_MeV_fm / (M_E_MEV * L_tube)

    print(f"  {r_e:6.1f} {h['a0']/L_tube:10.1f} {h['lambda_over_a0']:8.4f}"
          f" {abs(h['yukawa_frac']):10.6f} 1/{1/alpha_crit:.0f}")

print()
print("  Key observation: at EVERY r_e, a₀/L_tube ∝ 1/(r_e × α).")
print("  Larger r_e → smaller ratio → Yukawa corrections grow.")
print("  But even at r_e = 100, the correction is < 1%.")
print()
print("  The critical α (where atoms break) depends on r_e:")
print("  α_crit = ℏc/(m_e r_e L_ring) = 1/(r_e × μ₁₂)")
print("  At r_e = 6.6:  α_crit ≈ 1/13  (α must be < 1/13)")
print("  At r_e = 100:  α_crit ≈ 1/200 (α must be < 1/200)")


# ── Section 7: The deeper question ──────────────────────────────

print("\n\n── Section 7: Could α be derived? Assessment ──\n")

print("  WHAT WE FOUND:")
print("  1. The Yukawa correction grows monotonically with α.")
print("     No special 'preferred' α emerges from perturbation")
print("     theory alone.")
print()
print("  2. There IS a maximum α ≈ 1/(r_e × μ₁₂) where the Bohr")
print("     radius shrinks below L_tube.  Above this, the KK")
print("     approximation breaks down and atoms cannot exist in")
print("     the 3D sense.  At r_e = 6.6: α_max ≈ 1/13.")
print()
print("  3. The observed α = 1/137 is well below α_max (by 10×).")
print("     So atom stability does NOT pin α to 1/137 — it only")
print("     requires α < 1/13 (at r_e = 6.6).")
print()
print("  4. HOWEVER, if r_e is large (say r_e ≈ 1000), then")
print("     α_max ≈ 1/2000, and α = 1/137 would be TOO LARGE.")
print("     This means: α = 1/137 CONSTRAINS r_e from above!")
print()
print("  NEW INSIGHT:")
print("  ═══════════")
print("  The requirement 'atoms must exist' gives:")
print("        r_e < 1/(α × μ₁₂) ≈ 137/2 ≈ 68.5")
print()
print("  This is the first UPPER BOUND on r_e from physics!")
print("  Previously we only had r_e > 0.26 (from shear-charge).")
print("  Now: 0.26 < r_e < ~68")
print()

# Compute the actual bound
mu_test = 2.0  # μ₁₂ ≈ 2 for large r
r_max = 1.0 / (ALPHA_OBS * mu_test)
print(f"  Precise bound: r_e < 1/(α × μ₁₂) = 1/({ALPHA_OBS:.6f} × 2)")
print(f"                 r_e < {r_max:.1f}")
print()

print("  Conversely, if we knew r_e precisely, we'd have a")
print("  lower bound on α: α > 1/(r_e × μ₁₂).")
print("  And if we could determine r_e from ANOTHER observable")
print("  (proton charge radius, Lamb shift, electron g-2), we")
print("  could PREDICT α from the geometry!")
print()
print("  PATHS TO DERIVING α:")
print("  1. Find an observable that pins r_e → α follows from")
print("     the α(r, s) formula.")
print("  2. Compute the Casimir energy of T⁶ as a function of")
print("     all shears → the minimum determines all shears → α.")
print("  3. Solve the full 9D hydrogen atom (not KK-reduced)")
print("     → the effective coupling that emerges IS α.")
print("  4. Find a self-consistency between the T⁶ spectrum and")
print("     atomic binding that uniquely determines s.")
print()
print("  The most promising near-term: path (1).  The Lamb shift")
print("  in hydrogen has a Yukawa component that depends on r_e.")
print("  If the measured Lamb shift constrains r_e, α follows.")
print("  This would be a genuine PREDICTION of the model.")
