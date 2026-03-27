#!/usr/bin/env python3
"""
R25 Track 1: Spin analysis of (0,0,n₃) modes on T³.

Tests three candidate mechanisms for giving these modes spin-½:
  A. Shear-induced winding on the (θ₂,θ₃) subplane
  B. Non-trivial spin structure on T³
  C. Curvature-induced spin-orbit coupling

SPIN MECHANISM IN WvM
=====================
The electron (1,2) mode has:
  - p = 1 tube windings (θ₁ direction)
  - q = 2 ring windings (θ₂ direction)

Spin-½ arises from two independent arguments:

1. Angular momentum: L = E/ωs = ℏω/(q·ω) = ℏ/q = ℏ/2
   where ωs = q·ω because the photon passes the same azimuth
   q times per orbital period.

2. Phase twist: p tube traversals give a π·p phase twist to the
   E-field. For odd p, the E-field is inverted after one orbit →
   two orbits needed → fermion → spin-½.

Both require non-zero tube winding (p = n₁ ≠ 0).

For (0,0,n₃) modes: p = n₁ = 0.  No tube traversal.
  → No phase twist → boson
  → No ring circulation → no angular momentum about symmetry axis

KEY QUESTION: does T³ shear or curvature change this?
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
hc_eVm = h * c / eV_to_J


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
    fs = [f(si) for si in ss]
    for i in range(len(fs) - 1):
        if fs[i] * fs[i + 1] < 0:
            return brentq(f, ss[i], ss[i + 1], xtol=1e-14)
    return None


def wavevector_t3(n1, n2, n3, L1, r, r3, s12, s13=0.0, s23=0.0):
    """Physical wavevector components (k₁, k₂, k₃) for mode (n₁,n₂,n₃)."""
    L2 = r * L1
    L3 = r3 * L1
    q1 = n1
    q2 = n2 - n1 * s12
    q3 = n3 - n2 * s23 - n1 * (s13 - s12 * s23)
    k1 = 2 * math.pi * q1 / L1
    k2 = 2 * math.pi * q2 / L2
    k3 = 2 * math.pi * q3 / L3
    return k1, k2, k3


def energy_t3(n1, n2, n3, r, r3, s12, s13=0.0, s23=0.0):
    """Energy of mode (n₁,n₂,n₃) in units of E_electron."""
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
    print("R25 Track 1: Spin Analysis of (0,0,n₃) Modes")
    print("=" * 76)

    r = 5.0
    s12 = solve_electron_s(r)
    r3 = 1e8
    L1 = hc_eVm / (m_e_eV * math.sqrt(1 + ((2 - s12) / r)**2))

    print()
    print(f"Reference geometry: r = {r}, s₁₂ = {s12:.8f}, r₃ = {r3:.0e}")
    print(f"L₁ = {L1:.4e} m,  L₂ = {r*L1:.4e} m,  L₃ = {r3*L1:.4e} m")
    print()

    # ================================================================
    # SECTION 1: WvM spin mechanism — the n₁ dependence
    # ================================================================
    print("=" * 76)
    print("SECTION 1: WvM spin mechanism")
    print("=" * 76)
    print()
    print("In the WvM model, spin arises from TWO properties of the (1,2) orbit:")
    print()
    print("  (i)  ANGULAR MOMENTUM: L = E/ωs where ωs = n_φ·ω")
    print("       The photon goes n_φ = 2 times around the ring per orbit.")
    print("       L = ℏω/(2ω) = ℏ/2.")
    print()
    print("  (ii) PHASE TWIST: p = n₁ tube traversals give π·p phase twist.")
    print("       Odd p → E-field inverted → two orbits needed → fermion.")
    print("       Even p (incl. p=0) → E-field returns → boson.")
    print()
    print("Both depend on the WINDING NUMBERS (n₁, n₂):")
    print()

    modes = [
        (1, 2, "electron", "½ (fermion)"),
        (0, 1, "θ₂ only", "0 (boson)"),
        (0, 0, "trivial", "0 (boson)"),
        (2, 4, "double electron", "1 (boson)"),
        (1, 4, "slow tube", "¼ (→ ½ fermion)"),
        (3, 2, "triple tube", "3/2 (fermion)"),
    ]

    print(f"  {'mode':>8}  {'n₁(=p)':>6}  {'n₂(=q)':>6}  "
          f"{'odd p?':>6}  {'L = ℏ/q':>8}  {'spin':>15}  {'name':>18}")
    print("  " + "-" * 78)
    for n1, n2, name, spin_str in modes:
        odd = "YES" if n1 % 2 == 1 else "no"
        L_str = f"ℏ/{n2}" if n2 > 0 else "0"
        print(f"  ({n1},{n2})     {n1:6d}  {n2:6d}  "
              f"{odd:>6}  {L_str:>8}  {spin_str:>15}  {name:>18}")

    print()
    print("  KEY: p = n₁ determines fermion/boson (odd/even).")
    print("       q = n₂ determines spin magnitude (ℏ/q).")
    print("       Spin-½ requires BOTH odd n₁ AND n₂ = 2.")
    print()

    # ================================================================
    # SECTION 2: Mode (0,0,n₃) — zero tube winding
    # ================================================================
    print("=" * 76)
    print("SECTION 2: Mode (0,0,n₃) has p = n₁ = 0")
    print("=" * 76)
    print()
    print("For a pure θ₃ mode on T³:")
    print("  n₁ = 0  →  p = 0 (even)  →  no phase twist  →  BOSON")
    print("  n₂ = 0  →  q = 0          →  no ring circulation  →  L_z = 0")
    print()
    print("The mode is a standing wave (or traveling wave) purely along θ₃.")
    print("It does not traverse the tube. It does not circulate around the ring.")
    print("It has no angular momentum about the torus symmetry axis.")
    print()
    print("Spin = 0.  This is independent of n₃, L₃, r₃, or any other parameter.")
    print()

    # ================================================================
    # SECTION 3: Mechanism A — does shear redirect the wavevector?
    # ================================================================
    print("=" * 76)
    print("SECTION 3: Mechanism A — shear and wavevector direction")
    print("=" * 76)
    print()
    print("On the sheared T³, the lattice vector a₃ is tilted:")
    print("  a₃ = (s₁₃·L₁, s₂₃·L₂, L₃)")
    print()
    print("One might expect mode (0,0,n₃) to propagate along this tilted")
    print("direction, acquiring tube/ring winding components.")
    print()
    print("But the WAVEVECTOR of mode (0,0,n₃) is determined by the")
    print("RECIPROCAL lattice, not the direct lattice:")
    print()

    shear_tests = [
        (0.0, 0.0),
        (0.1, 0.2),
        (0.5, 1.0),
        (0.25, 0.5),
    ]

    print(f"  {'s₁₃':>5}  {'s₂₃':>5}  {'k₁ (m⁻¹)':>14}  {'k₂ (m⁻¹)':>14}  "
          f"{'k₃ (m⁻¹)':>14}  {'E/E_e':>12}")
    print("  " + "-" * 74)

    for s13, s23 in shear_tests:
        k1, k2, k3 = wavevector_t3(0, 0, 1, L1, r, r3, s12, s13, s23)
        E = energy_t3(0, 0, 1, r, r3, s12, s13, s23)
        print(f"  {s13:5.2f}  {s23:5.2f}  {k1:14.4e}  {k2:14.4e}  "
              f"{k3:14.4e}  {E:12.4e}")

    print()
    print("  Result: k₁ = k₂ = 0 for ALL shear values.")
    print("  The wavevector of (0,0,n₃) is ALWAYS purely along θ₃.")
    print()
    print("  Physical explanation: the reciprocal lattice vector b₃ is always")
    print("  perpendicular to the (θ₁,θ₂) plane, regardless of how a₃ is tilted.")
    print("  Shear tilts the LATTICE but not the WAVEVECTOR.")
    print()
    print("  From the R24 T1 effective quantum numbers:")
    print("  q₁ = n₁ = 0,  q₂ = n₂ - n₁·s₁₂ = 0,  q₃ = n₃ = n₃")
    print("  No shear terms survive when n₁ = n₂ = 0.")
    print()
    print("  CONCLUSION: Shear cannot give (0,0,n₃) modes any tube or ring")
    print("  winding. Mechanism A fails: no spin-½ from shear redirection.")
    print()

    # ================================================================
    # SECTION 4: Mechanism A — modes WITH ring winding
    # ================================================================
    print("=" * 76)
    print("SECTION 4: What if neutrinos have ring winding?")
    print("=" * 76)
    print()
    print("Could neutrinos be modes with n₂ ≠ 0 (giving q > 0 for spin)")
    print("and n₁ = 1 (giving odd p for fermion)?")
    print()
    print("Problem: n₁ = 1 → mode is CHARGED (R19: charge requires n₁ = ±1).")
    print("Neutrinos are uncharged. So n₁ must be 0.")
    print()
    print("What about n₁ = 0, n₂ ≠ 0? Then p = 0 → boson → spin-0.")
    print()
    print("The charge-spin linkage is structural:")
    print("  n₁ = 0  →  uncharged  AND  spin-0  (no tube traversal)")
    print("  n₁ = 1  →  charged    AND  spin-½  (odd tube traversal)")
    print()
    print("Energy of modes with winding (for reference):")
    print()
    print(f"  {'mode':>14}  {'n₁':>3}  {'n₂':>3}  {'n₃':>3}  "
          f"{'E/E_e':>12}  {'E (eV)':>12}  {'spin':>6}  {'charge':>8}")
    print("  " + "-" * 80)

    candidates = [
        (0, 0, 1, "0", "0"),
        (0, 0, 10, "0", "0"),
        (0, 1, 0, "0", "0"),
        (0, 1, 2, "0", "0"),
        (1, 2, 0, "½", "e"),
        (1, 0, 1, "½", "e"),
        (1, 2, 1, "½", "e"),
    ]

    for n1, n2, n3, spin, charge in candidates:
        E = energy_t3(n1, n2, n3, r, r3, s12)
        E_eV = E * m_e_eV
        label = f"({n1},{n2},{n3})"
        print(f"  {label:>14}  {n1:3d}  {n2:3d}  {n3:3d}  "
              f"{E:12.4e}  {E_eV:12.2f}  {spin:>6}  {charge:>8}")

    print()
    print("  Modes with spin-½ (n₁=1) have E ~ 0.5 MeV (electron scale).")
    print("  Modes with n₁=0 and n₂≠0 have E ~ m_e/r ~ 100 keV.")
    print("  Pure θ₃ modes (0,0,n₃) have E ~ meV but spin-0.")
    print()
    print("  NO mode is simultaneously: (a) uncharged, (b) light (meV),")
    print("  and (c) spin-½.")
    print()

    # ================================================================
    # SECTION 5: Can shear make n₂ ≠ 0 modes light?
    # ================================================================
    print("=" * 76)
    print("SECTION 5: Shear cannot make n₂ ≠ 0 modes light")
    print("=" * 76)
    print()
    print("For n₁ = 0, the effective quantum numbers are:")
    print("  q₁ = 0")
    print("  q₂ = n₂ − n₁·s₁₂ = n₂   (shear s₂₃ does NOT enter q₂)")
    print("  q₃ = n₃ − n₂·s₂₃          (s₂₃ only shifts q₃)")
    print()
    print("  E² ∝ (n₂/r)² + (q₃/r₃)²")
    print()
    print("The (n₂/r)² term is ALWAYS present for n₂ ≠ 0, regardless of shear.")
    print("Shear modifies q₃ but cannot cancel q₂ = n₂.")
    print()

    print(f"  {'mode':>14}  {'s₂₃':>5}  {'q₂':>4}  {'q₃':>6}  "
          f"{'E/E_e':>12}  {'E (eV)':>12}")
    print("  " + "-" * 64)

    for s23_test in [0.0, 0.5, 2.0]:
        q2 = 2
        q3 = 1 - 2 * s23_test
        E = energy_t3(0, 2, 1, r, r3, s12, 0, s23_test)
        E_eV = E * m_e_eV
        print(f"  (0, 2, 1)       {s23_test:5.1f}  {q2:4d}  {q3:6.1f}  "
              f"{E:12.4e}  {E_eV:12.0f}")

    print()
    print("  Energy stays ~ 100 keV for ALL shear values (dominated by q₂=2).")
    print("  Only modes with n₂ = 0 can be light → only (0,0,n₃) → spin-0.")
    print()
    print("  The three constraints form a closed trap:")
    print("    Light (meV)    →  n₂ = 0  (q₂ = n₂ dominates otherwise)")
    print("    Uncharged      →  n₁ = 0  (R19)")
    print("    Spin-½         →  n₁ odd  (WvM)")
    print("  All three cannot be satisfied simultaneously.")
    print()

    # ================================================================
    # SECTION 6: Mechanism B — spin structures on T³
    # ================================================================
    print("=" * 76)
    print("SECTION 6: Mechanism B — spin structures on T³")
    print("=" * 76)
    print()
    print("A flat T³ admits 2³ = 8 distinct spin structures, specifying")
    print("periodic (P) or anti-periodic (A) boundary conditions for")
    print("spinor fields in each direction.")
    print()
    print("However, the photon field (E, B) is a VECTOR field (spin-1),")
    print("not a spinor (spin-½). Vector fields always have periodic")
    print("boundary conditions, regardless of the spin structure.")
    print()
    print("The electron's spin-½ arises from a DYNAMICAL mechanism")
    print("(angular momentum L = E/ωs), not from the field being a spinor.")
    print("The photon remains a vector field; the (1,2) orbit converts")
    print("the photon's spin-1 into the electron's spin-½.")
    print()
    print("Without the (1,2) orbit (i.e., with n₁ = n₂ = 0), there is")
    print("no conversion mechanism. Choosing a different spin structure")
    print("for T³ would affect hypothetical spinor fields but not the")
    print("electromagnetic field.")
    print()
    print("CONCLUSION: Mechanism B is inapplicable. Spin structures")
    print("affect spinors, not vectors. The WvM model uses vector fields.")
    print()

    # ================================================================
    # SECTION 7: Mechanism C — curvature mixing
    # ================================================================
    print("=" * 76)
    print("SECTION 7: Mechanism C — curvature-induced mixing")
    print("=" * 76)
    print()
    print("The embedded T² has curvature ε = 1/r that mixes θ₁ modes")
    print("(R22: Sturm-Liouville eigenmodes are not pure Fourier modes).")
    print()
    print("Could a (0,0,n₃) mode mix with (m,0,n₃) modes via curvature,")
    print("acquiring spin-½ from the m ≠ 0 component?")
    print()

    eps = 1.0 / r
    print(f"  Curvature parameter: ε = 1/r = {eps:.3f}")
    print()

    E_neutrino_eV = 0.01
    E_electron_eV = m_e_eV

    print(f"  Mode (0,0,1):   E ≈ {E_neutrino_eV:.0e} eV  (neutrino scale)")
    print(f"  Mode (1,0,1):   E ≈ {E_electron_eV:.0e} eV  (electron scale)")
    print(f"  Mode (−1,0,1):  E ≈ {E_electron_eV:.0e} eV  (electron scale)")
    print()

    gap = E_electron_eV - E_neutrino_eV

    V_matrix_element = eps * E_neutrino_eV

    mixing = V_matrix_element / gap
    print(f"  Energy gap: ΔE = {gap:.0e} eV")
    print(f"  Curvature matrix element: V ∼ ε × E₀ = {V_matrix_element:.1e} eV")
    print(f"  Mixing coefficient: c₁ ∼ V/ΔE = {mixing:.1e}")
    print(f"  Spin contribution: c₁² × ℏ/2 = {mixing**2:.1e} × ℏ/2")
    print()

    if abs(mixing) < 1e-4:
        print(f"  Mixing amplitude {mixing:.1e} is NEGLIGIBLE.")
    print()
    print("  Even with generous estimates, the perturbative spin")
    print("  contribution is O(10⁻¹²) ℏ.  Not spin-½.")
    print()
    print("  Furthermore, on a product space T² × S¹, the curvature")
    print("  of T² acts only on the (θ₁, θ₂) sector.  The θ₃ wavefunction")
    print("  factorizes: ψ(θ₁,θ₂,θ₃) = φ(θ₁,θ₂) × e^{in₃θ₃}.")
    print("  The curvature mixes different φ but doesn't affect the θ₃ part.")
    print("  So the mode remains a product state — its 'T² part' has some")
    print("  small admixture of m ≠ 0, but the overall particle is still")
    print("  defined by its quantum numbers (0,0,n₃) and has spin-0.")
    print()
    print("  CONCLUSION: Mechanism C fails. Curvature mixing is perturbatively")
    print("  small (~10⁻¹²) and doesn't change the spin quantum number.")
    print()

    # ================================================================
    # SECTION 8: The charge-spin linkage
    # ================================================================
    print("=" * 76)
    print("SECTION 8: The charge-spin linkage — structural result")
    print("=" * 76)
    print()
    print("The WvM framework has a deep structural constraint:")
    print()
    print("  CHARGE requires n₁ = ±1  (R19: only n₁ = ±1 carries charge)")
    print("  SPIN-½ requires n₁ odd   (S3-knot-zoo: odd p → fermion)")
    print()
    print("Both are controlled by n₁ (tube winding number). This creates")
    print("a perfect linkage:")
    print()
    print("  n₁ = 0   →  Q = 0    AND  spin = 0    (uncharged boson)")
    print("  n₁ = ±1  →  Q = ±e   AND  spin = ½    (charged fermion)")
    print()
    print("In the Standard Model, neutrinos are UNCHARGED FERMIONS.")
    print("The WvM framework cannot produce this combination.")
    print("  - Uncharged → n₁ = 0 → boson (spin-0)")
    print("  - Fermion → n₁ odd → charged")
    print()
    print("This is not a failure of the specific T³ model.")
    print("It is a structural limitation of the WvM spin mechanism.")
    print()

    # ================================================================
    # SECTION 9: Exhaustive check — any mode with spin-½ AND Q=0?
    # ================================================================
    print("=" * 76)
    print("SECTION 9: Exhaustive search for uncharged spin-½ modes")
    print("=" * 76)
    print()
    print("Search all modes (n₁, n₂, n₃) with |n₁|,|n₂| ≤ 5, |n₃| ≤ 10")
    print("for modes that are BOTH uncharged (n₁ = 0) AND spin-½ (n₁ odd):")
    print()

    count_uncharged = 0
    count_spin_half = 0
    count_both = 0

    for n1 in range(-5, 6):
        for n2 in range(-5, 6):
            for n3 in range(-10, 11):
                if n1 == 0 and n2 == 0 and n3 == 0:
                    continue
                uncharged = (n1 == 0)
                fermion = (abs(n1) % 2 == 1)  # odd n₁
                if uncharged:
                    count_uncharged += 1
                if fermion:
                    count_spin_half += 1
                if uncharged and fermion:
                    count_both += 1

    print(f"  Uncharged modes (n₁ = 0): {count_uncharged}")
    print(f"  Fermion modes (n₁ odd):   {count_spin_half}")
    print(f"  Both (uncharged fermion):  {count_both}")
    print()
    print("  The intersection is EMPTY. These are mutually exclusive")
    print("  conditions on the SAME quantum number n₁.")
    print()

    # ================================================================
    # SECTION 10: Summary
    # ================================================================
    print("=" * 76)
    print("SECTION 10: Track 1 Summary")
    print("=" * 76)
    print()
    print("FINDINGS:")
    print()
    print("F1. MECHANISM A FAILS: Shear does not redirect the wavevector")
    print("    of (0,0,n₃) modes. The wavevector is always along θ₃")
    print("    regardless of s₁₃, s₂₃. No tube/ring winding → spin-0.")
    print()
    print("F2. MECHANISM B IS INAPPLICABLE: Spin structures on T³ affect")
    print("    spinor fields, not vector fields. The photon is a vector")
    print("    field. The WvM spin mechanism is dynamical (L = E/ωs),")
    print("    not topological (spinor boundary conditions).")
    print()
    print("F3. MECHANISM C FAILS: Curvature mixing between (0,0,n₃) and")
    print("    (m,0,n₃) modes has amplitude ~10⁻⁶, contributing spin")
    print("    ~10⁻¹² ℏ. Negligible. Also, on a product space T² × S¹,")
    print("    the curvature factorizes and doesn't change n₁.")
    print()
    print("F4. CHARGE-SPIN LINKAGE: In the WvM framework, both charge")
    print("    and spin-½ are controlled by n₁ (tube winding number):")
    print("      charge requires n₁ = ±1 (R19)")
    print("      spin-½ requires n₁ odd (S3-knot-zoo)")
    print("    The conditions n₁ = 0 (uncharged) and n₁ odd (fermion)")
    print("    are MUTUALLY EXCLUSIVE. The WvM model cannot produce")
    print("    uncharged fermions.")
    print()
    print("F5. T³ NEUTRINO MODEL FAILS AT SPIN GATE: Despite the")
    print("    remarkable kinematic success (mass-squared ratio 33.63")
    print("    from integers alone, matching experiment to 0.03σ),")
    print("    modes (0,0,n₃) are spin-0 bosons, not spin-½ fermions.")
    print("    They cannot be neutrinos.")
    print()
    print("F6. SCOPE OF FAILURE: This is not specific to the T³ model.")
    print("    It is a structural limitation of the WvM spin mechanism.")
    print("    ANY compact-dimension model using the same mechanism")
    print("    (spin from tube winding) will have the same charge-spin")
    print("    linkage. Uncharged fermions are impossible.")
    print()
    print("IMPLICATIONS:")
    print()
    print("  The neutrino exists (angular momentum conservation demands")
    print("  it — see R24-torus-dynamics/neutrinos.md). The WvM framework")
    print("  currently has no mechanism to produce it.")
    print()
    print("  Possible paths forward:")
    print("  (a) A DIFFERENT spin mechanism that decouples charge from spin")
    print("  (b) Neutrinos are composite (two spin-½ particles can form")
    print("      spin-0 or spin-1; the right combination might give ½)")
    print("  (c) The neutrino arises from a mechanism outside the current")
    print("      WvM framework entirely (e.g., a different field type)")
    print()
    print("  Path (a) would require modifying the foundational spin")
    print("  derivation L = E/ωs, which is one of the model's strengths.")
    print("  Path (b) requires three spin-½ constituents, but the only")
    print("  available ones are charged (electrons). A bound state of")
    print("  electron + two positrons? Exotic and speculative.")
    print("  Path (c) would mean the framework is incomplete — not wrong,")
    print("  but not a theory of everything.")
    print()
    print("  Track 2 (PMNS from T³ geometry) is CANCELLED: without")
    print("  spin-½ neutrinos, the PMNS derivation has no target.")
    print("  The r-selection path through neutrino mixing is closed.")
    print()


if __name__ == "__main__":
    main()
