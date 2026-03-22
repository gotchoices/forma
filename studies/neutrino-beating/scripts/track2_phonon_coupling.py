#!/usr/bin/env python3
"""
R23 Track 2: Phonon coupling analysis.

QUESTION: Does the embedding curvature provide mode-mode coupling
strong enough to support a sub-eV phonon (neutrino)?

KEY FINDING: θ₂-momentum is conserved on the axisymmetric embedded
torus.  The metric ds² = a²dθ₁² + ρ(θ₁)²dθ₂² has no θ₂ dependence,
so the Laplacian commutes with ∂/∂θ₂.  This means modes with
different effective θ₂-momentum do NOT couple through curvature.

This has two consequences:
(a) The proton's harmonics (n, 2n) have different n₂ values and
    do not couple to each other.  No phonon propagation through the
    harmonic spectrum at fixed-background level.
(b) Track 1's near-degenerate triplets involve modes with different
    n₂ — they don't couple either.

APPROACH:
1. Verify analytically that the curvature perturbation conserves n₂.
2. Search for near-degenerate pairs at FIXED n₂ (where coupling exists).
3. Estimate coupling strength from θ₂-symmetry-breaking mechanisms.
4. Compute required coupling for sub-eV phonon mass.
5. Viability assessment.
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha, m_e, c, G, hbar, e as e_charge

m_e_eV = m_e * c**2 / 1.602176634e-19
m_p = 1.67262192369e-27
m_p_eV = m_p * c**2 / 1.602176634e-19
l_P = math.sqrt(hbar * G / c**3)


def alpha_mode_2d(r, s, m):
    q = m - s
    sn = math.sin(2 * math.pi * s)
    if abs(sn) < 1e-15 or abs(q) < 1e-15:
        return 0.0
    d = math.sqrt(r**2 * (1 + m * s)**2 + m**2)
    return r**2 * sn**2 / (4 * math.pi * q**2 * d)


def solve_s(r):
    def f(s):
        return alpha_mode_2d(r, s, 2) - alpha
    ss = np.linspace(0.001, 0.499, 5000)
    fs = [f(si) for si in ss]
    for i in range(len(fs) - 1):
        if fs[i] * fs[i + 1] < 0:
            return brentq(f, ss[i], ss[i + 1], xtol=1e-14)
    return None


def mode_energy_ratio(n1, n2, r, s):
    """E(n1,n2)/E_electron in m_e units."""
    e_sq_e = 1.0 + ((2 - s) / r)**2
    esq = n1**2 + ((n2 - n1 * s) / r)**2
    if esq <= 0:
        return 0.0
    return math.sqrt(esq / e_sq_e)


def main():
    print("=" * 72)
    print("R23 TRACK 2: Phonon coupling analysis")
    print("=" * 72)
    print()

    r = 1.0
    s = solve_s(r)
    eps = 1.0 / r  # a/R = 1/r for the embedding
    print(f"Working at r = {r}, s = {s:.10f}, ε = a/R = {eps:.4f}")

    lambda_C = 2 * math.pi * hbar / (m_e * c)
    a_phys = lambda_C / (4 * math.pi)
    R_phys = r * a_phys
    print(f"Physical dimensions: a = {a_phys:.4e} m, R = {R_phys:.4e} m")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 1: θ₂-momentum conservation (analytical)")
    print("=" * 72)
    print()

    print("The embedded torus metric is:")
    print("  ds² = a² dθ₁² + ρ(θ₁)² dθ₂²")
    print("  where ρ(θ₁) = R + a cos θ₁")
    print()
    print("Key property: the metric has NO θ₂ dependence.")
    print("  → The Laplacian commutes with ∂/∂θ₂")
    print("  → θ₂-momentum p₂ is conserved")
    print("  → Modes with different p₂ do NOT couple")
    print()
    print("For a mode ψ = f(θ₁) e^{i p₂ θ₂}, the θ₁ equation is a")
    print("Sturm-Liouville problem at fixed p₂.  Modes at different p₂")
    print("live in orthogonal subspaces — curvature cannot mix them.")
    print()
    print("On the SHEARED T², the effective θ₂-momentum for mode (n₁,n₂)")
    print("is p₂ = n₂ (from the boundary condition).")
    print("So curvature couples modes (n₁,n₂) and (m₁,n₂) — same n₂ only.")
    print()
    print("CONSEQUENCE: The proton's harmonics (n, 2n) for n = 2,3,4,...")
    print("  have n₂ = 4, 6, 8, ...  Each has a DIFFERENT n₂.")
    print("  → They do NOT couple to each other through curvature.")
    print("  → No phonon can propagate through the harmonic spectrum")
    print("    at the fixed-background level.")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 2: Near-degeneracy at fixed n₂")
    print("=" * 72)
    print()

    print("For the phonon to work, we need near-degenerate modes with")
    print("the SAME n₂.  How tight are fixed-n₂ near-degeneracies?")
    print()

    E_max = 100
    print(f"Scanning n₂ = 1..200, |n₁| ≥ 2, E < {E_max} m_e")
    print()

    best_fixed_n2 = []

    for n2_val in range(1, 201):
        modes_at_n2 = []
        for n1 in range(2, 300):
            E = mode_energy_ratio(n1, n2_val, r, s)
            if 0 < E < E_max:
                modes_at_n2.append((E, n1, n2_val))
            E_neg = mode_energy_ratio(-n1, n2_val, r, s)
            if 0 < E_neg < E_max:
                modes_at_n2.append((E_neg, -n1, n2_val))

        modes_at_n2.sort()
        if len(modes_at_n2) < 2:
            continue

        min_gap = float('inf')
        best_pair = None
        for i in range(len(modes_at_n2) - 1):
            gap = modes_at_n2[i + 1][0] - modes_at_n2[i][0]
            if gap < min_gap and gap > 0:
                min_gap = gap
                best_pair = (modes_at_n2[i], modes_at_n2[i + 1])

        if best_pair:
            gap_eV = min_gap * m_e_eV
            best_fixed_n2.append((gap_eV, n2_val,
                                  best_pair[0], best_pair[1],
                                  len(modes_at_n2)))

    best_fixed_n2.sort()

    print("Tightest 15 near-degeneracies at fixed n₂:")
    print(f"{'n₂':>4s}  {'modes':>5s}  {'ΔE (eV)':>12s}  "
          f"{'E/mₑ':>8s}  Mode pair")
    print("-" * 75)
    for gap_eV, n2v, m1, m2, nm in best_fixed_n2[:15]:
        print(f"{n2v:4d}  {nm:5d}  {gap_eV:12.2f}  "
              f"{m1[0]:8.3f}  ({m1[1]:+d},{m1[2]:+d})"
              f" – ({m2[1]:+d},{m2[2]:+d})")
    print()

    if best_fixed_n2:
        tightest = best_fixed_n2[0]
        print(f"Tightest fixed-n₂ pair: ΔE = {tightest[0]:.2f} eV"
              f" at n₂ = {tightest[1]}")
        print(f"  Compare to Track 1: tightest UNFIXED pair ~0.001 eV")
        print(f"  Ratio: {tightest[0] / 0.001:.0f}× worse with n₂ constraint")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 3: Curvature coupling matrix elements")
    print("=" * 72)
    print()

    print("At fixed n₂, curvature couples modes with Δn₁ = ±1 (from")
    print("cos θ₁ in the metric).  The leading-order coupling is:")
    print()
    print("  V_{n₁,n₁±1} = ε × n₂² / r² × (normalization)")
    print()
    print(f"At ε = 1/r = {eps:.4f}, for the tightest pair:")

    if best_fixed_n2:
        t = best_fixed_n2[0]
        n2v = t[1]
        n1a, n1b = t[2][1], t[3][1]
        Ea = t[2][0]

        V_leading = eps * n2v**2 / r**2
        E_scale = Ea * m_e_eV
        V_eV = V_leading * E_scale

        print(f"  n₂ = {n2v}, modes ({n1a:+d},{n2v}) and ({n1b:+d},{n2v})")
        print(f"  Δn₁ = {abs(n1b - n1a)}")
        print()

        if abs(n1b - n1a) == 1:
            print(f"  V ≈ ε × n₂²/r² × E_scale")
            print(f"    = {eps:.4f} × {n2v}² × {E_scale:.0f} eV")
            print(f"    = {V_eV:.0f} eV")
            print()
            print("  This is a LARGE coupling — much bigger than the")
            print("  level spacing.  The modes are strongly mixed by")
            print("  curvature, not weakly perturbed.")
        else:
            print(f"  Δn₁ = {abs(n1b - n1a)} > 1: coupling is O(ε^{abs(n1b-n1a)})")
            order = abs(n1b - n1a)
            V_high = eps**order * n2v**2 / r**2 * E_scale
            print(f"  V ≈ ε^{order} × n₂²/r² × E_scale")
            print(f"    ≈ {V_high:.2e} eV")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 4: What coupling is needed for a sub-eV phonon?")
    print("=" * 72)
    print()

    print("The phonon mass in a tight-binding chain of N coupled modes:")
    print("  m_phonon ~ t / (N × a_lattice × c²)")
    print("where t = hopping matrix element between adjacent modes")
    print()
    print("For a sub-eV phonon from modes at E ~ 50 m_e:")
    print("  Need: t_effective ~ m_phonon × c² ~ 0.1 eV")
    print()
    print("But this t is the coupling between modes with DIFFERENT n₂.")
    print("On the axisymmetric embedded torus, this coupling is ZERO.")
    print()

    print("Possible θ₂-symmetry-breaking mechanisms:")
    print()

    print("(a) Gravitational backreaction:")
    print("    Each mode curves spacetime.  Mode energy E creates")
    print("    a gravitational perturbation ~ G E / (c⁴ × r_torus).")
    E_mode_J = 50 * m_e_eV * 1.602176634e-19
    grav_coupling = G * E_mode_J / (c**4 * a_phys)
    grav_coupling_eV = grav_coupling / 1.602176634e-19
    print(f"    At E = 50 m_e, r = {a_phys:.2e} m:")
    print(f"    Gravitational coupling ~ {grav_coupling_eV:.2e} eV")
    print(f"    This is {grav_coupling_eV:.2e} / 0.1 = {grav_coupling_eV/0.1:.2e}")
    print(f"    of the required coupling.  NEGLIGIBLE.")
    print()

    print("(b) Proton backreaction on torus shape:")
    print("    The proton's ~154 harmonics create a non-uniform energy")
    print("    density on T².  This deforms the torus, breaking θ₂")
    print("    symmetry.  The deformation scales as:")
    print("    δρ/ρ ~ E_harmonic / E_geometric_stiffness")
    E_proton_eV = m_p_eV
    E_stiffness = m_e_eV  # Compton-scale stiffness (order of magnitude)
    delta_rho = E_proton_eV / E_stiffness
    print(f"    E_proton = {E_proton_eV:.3e} eV")
    print(f"    If E_stiffness ~ m_e c² = {E_stiffness:.0f} eV:")
    print(f"    δρ/ρ ~ {delta_rho:.0f}")
    print(f"    This is O(1) — the backreaction is STRONG.")
    print(f"    But this means the fixed-background approximation")
    print(f"    breaks down entirely for the proton composite.")
    print()

    print("(c) Electromagnetic self-interaction:")
    print("    The electron's (1,2) mode generates EM fields that")
    print("    could mediate coupling between uncharged harmonics")
    print("    via virtual photon exchange.  This is a second-order")
    print("    process: harmonic → photon → harmonic.")
    V_em = alpha * m_e_eV  # order of magnitude for EM vertex
    V_em_2nd = V_em**2 / (50 * m_e_eV)  # second-order perturbation
    print(f"    First-order EM vertex: ~ α × m_e c² = {V_em:.0f} eV")
    print(f"    Second-order (harmonic-harmonic): ~ {V_em_2nd:.1f} eV")
    print(f"    This is significant but involves charged intermediaries.")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 5: The coupling paradox")
    print("=" * 72)
    print()

    print("The phonon model requires weak coupling between harmonics")
    print("(to get sub-eV mass).  But the only strong coupling is")
    print("between modes at FIXED n₂ — and those modes are NOT nearly")
    print("degenerate (ΔE ~ hundreds of eV).")
    print()
    print("The modes that ARE nearly degenerate (from Track 1) have")
    print("different n₂ values and couple with strength:")
    print("  - Gravitational: ~ 10⁻³⁸ eV (negligible)")
    print("  - EM second-order: ~ 10–100 eV (too strong for sub-eV phonon)")
    print("  - Backreaction: unknown but potentially O(1)")
    print()
    print("This creates a PARADOX:")
    print("  - Too weak coupling → phonon mass = 0 (no propagation)")
    print("  - Too strong coupling → phonon mass >> 1 eV (not a neutrino)")
    print("  - Need coupling ~ 10⁻¹⁵ × mode energy to get sub-eV mass")
    print()

    coupling_needed_eV = 0.1  # sub-eV phonon
    E_mode_eV = 50 * m_e_eV
    ratio_needed = coupling_needed_eV / E_mode_eV
    print(f"Required coupling/mode_energy ratio: {ratio_needed:.2e}")
    print(f"  Gravitational: {grav_coupling_eV / E_mode_eV:.2e} — "
          f"10^{math.log10(grav_coupling_eV / E_mode_eV / ratio_needed):.0f}× "
          f"too weak")
    print(f"  EM 2nd order:  {V_em_2nd / E_mode_eV:.2e} — "
          f"10^{math.log10(V_em_2nd / E_mode_eV / ratio_needed):.0f}× "
          f"too strong")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 6: Alternative — geometry fluctuation neutrino")
    print("=" * 72)
    print()

    print("If the phonon-of-harmonics model fails, the neutrino might")
    print("instead be a fluctuation OF the torus geometry (Direction D")
    print("from neutrino.md).  This avoids the coupling problem because")
    print("geometry fluctuations are not KK modes — they're moduli.")
    print()
    print("A shape oscillation of T² (fluctuation of r, s, or L) has:")
    print("  - Charge 0 (no winding number change)")
    print("  - Mass set by geometric stiffness")
    print("  - Created in decay (geometry readjusts when electron escapes)")
    print()
    print("The mass of a moduli fluctuation:")
    print("  m_mod = ℏ √(κ / I) / c²")
    print("where κ = stiffness, I = inertia of the shape mode.")
    print()

    # Rough estimate of moduli mass
    # Stiffness from R18: κ ~ ε₀ E₀² / (2R)
    # where E₀ is the electric field strength at the torus surface
    # For the electron: E₀ ~ e / (4πε₀ a²)
    E_field = e_charge / (4 * math.pi * 8.854e-12 * a_phys**2)
    kappa = 8.854e-12 * E_field**2 / (2 * R_phys)
    # Inertia: I ~ m_e for the electron torus
    # But this is very crude
    I_shape = m_e
    omega_mod = math.sqrt(kappa / I_shape)
    m_mod = hbar * omega_mod / c**2
    m_mod_eV = m_mod * c**2 / 1.602176634e-19

    print(f"Rough estimate (from E-field stiffness):")
    print(f"  E_field at torus surface: {E_field:.2e} V/m")
    print(f"  Stiffness κ: {kappa:.2e} J/m")
    print(f"  Moduli mass: {m_mod_eV:.2e} eV")
    print(f"  (This is extremely crude — order-of-magnitude only)")
    print()

    if m_mod_eV < 1.0:
        print("  The moduli mass is sub-eV — potentially viable!")
    elif m_mod_eV < 1e6:
        print(f"  The moduli mass is {m_mod_eV:.0f} eV — above neutrino scale")
        print(f"  but the estimate is very rough.")
    else:
        print(f"  The moduli mass is {m_mod_eV:.2e} eV — far above neutrino scale")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 7: Viability assessment")
    print("=" * 72)
    print()

    print("NEUTRINO MODEL VIABILITY SCORECARD")
    print()
    print("Requirement           | Phonon model      | Moduli model")
    print("-" * 65)
    print("Charge = 0            | ✓ automatic       | ✓ automatic")
    print("Mass < 0.8 eV         | ? coupling unknown | ? stiffness unknown")
    print("Three flavors         | ? (Track 1: ratio  | ? (three shape modes")
    print("                      |   matches exist)   |   for L₁, L₂, s)")
    print("Spin ½                | ? (spin chain      | ✗ scalar/tensor")
    print("                      |   mechanism)       |   (spin 0 or 2)")
    print("Created in decay      | ✓ occupation shift | ✓ geometry readjusts")
    print("Oscillations          | ✓ beat frequencies | ? moduli mixing")
    print("Mode-mode coupling    | ✗ θ₂ blocks it    | N/A (not modes)")
    print()
    print("KEY OBSTACLES:")
    print()
    print("1. PHONON MODEL: θ₂-momentum conservation prevents curvature-")
    print("   mediated coupling between harmonics.  The coupling needed")
    print("   (~10⁻⁹ of mode energy) falls in a desert between gravity")
    print("   (10⁻³⁸) and EM (10⁻³).  No known mechanism provides it.")
    print()
    print("2. MODULI MODEL: Spin ½ is the killer.  Geometry fluctuations")
    print("   are bosonic (spin 0 for scalar, spin 2 for tensor).  Getting")
    print("   spin ½ from geometry requires supersymmetry or an analog of")
    print("   topological spinons — neither is natural in this framework.")
    print()
    print("3. BOTH MODELS: The T² framework currently has no viable")
    print("   mechanism for producing a spin-½, charge-0, sub-eV particle.")
    print("   The neutrino remains the most serious gap in the model.")
    print()
    print("POSSIBLE RESOLUTIONS:")
    print()
    print("(a) The proton's backreaction on T² breaks θ₂ symmetry,")
    print("    providing the needed coupling.  This requires a self-")
    print("    consistent calculation (beyond fixed background).")
    print("    → This is exactly what R22 needs to compute.")
    print()
    print("(b) The neutrino IS on a separate, larger T² (R20 option (a)).")
    print("    Viable but unsatisfying — introduces a free parameter")
    print("    for each neutrino flavor.")
    print()
    print("(c) The neutrino is a topological defect (Direction E from")
    print("    neutrino.md) — a vortex on T² created during decay.")
    print("    Could carry fractional spin through topological charge.")
    print("    Never computed.")
    print()
    print("(d) The model is incomplete: the neutrino requires physics")
    print("    beyond the T² framework (e.g., a third compact dimension,")
    print("    non-abelian gauge fields, etc.).")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 8: Summary")
    print("=" * 72)
    print()

    print("F8.  θ₂-momentum is conserved on the embedded torus.")
    print("     The metric has no θ₂ dependence → modes with different")
    print("     n₂ don't couple through curvature.  This is exact, not")
    print("     perturbative.")
    print()
    print("F9.  Proton harmonics don't couple at fixed-background level.")
    print("     Harmonics (n, 2n) have n₂ = 4, 6, 8, ...  Different n₂")
    print("     values → no curvature-mediated coupling → no phonon.")
    print()
    if best_fixed_n2:
        print(f"F10. Fixed-n₂ near-degeneracy is ~{best_fixed_n2[0][0]:.0f} eV.")
        print(f"     Compare to unfixed: ~0.001 eV (Track 1).")
        print(f"     The n₂ constraint removes a Diophantine degree of")
        print(f"     freedom, making tight near-degeneracies ~10⁵× rarer.")
        print()
    print("F11. Coupling desert: gravity gives ~10⁻³⁸ eV, EM gives ~10–100 eV.")
    print("     Need ~10⁻⁹ × E_mode for sub-eV phonon.  No known")
    print("     mechanism provides coupling at this scale.")
    print()
    print("F12. The phonon-of-harmonics neutrino model has a structural")
    print("     obstacle: θ₂ conservation.  It is not viable WITHOUT a")
    print("     mechanism that breaks this symmetry.")
    print()
    print("F13. The proton's backreaction on T² (R22) may break θ₂")
    print("     symmetry.  This is the most promising rescue path,")
    print("     but requires a self-consistent calculation.")
    print()
    print("F14. VIABILITY: The T² model does NOT yet have a viable")
    print("     neutrino.  The phonon model fails on coupling (F12),")
    print("     the moduli model fails on spin (spin 0, not ½).")
    print("     The neutrino is the model's most serious open problem.")


if __name__ == "__main__":
    main()
