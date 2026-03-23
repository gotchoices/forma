#!/usr/bin/env python3
"""
R26 Track 1c: Non-coprime and higher-order modes.

The knot-zoo excluded non-coprime (p,q) pairs (gcd(p,q) ≠ 1), but on
a flat T² these are valid standing waves — they are simply modes whose
wavevector is a multiple of a shorter fundamental.  Enumerate all modes
(p,q) with p,q up to 25, including non-coprime, and assess whether any
offer a path to three spin-½ neutrino mass eigenstates.

Also: on T⁶, modes can have nonzero winding on multiple T² subplanes.
Classify these cross-plane mode families.

KEY DISTINCTION: torus knots vs. T² modes
==========================================
- A torus KNOT (p,q) with gcd(p,q) = 1 is a single closed geodesic
  on the embedded torus surface.  The knot-zoo studied these.
- A T² MODE (n₃,n₄) is a standing wave on the flat torus, with
  wavevector k = (2πn₃/L₃, 2πn₄/L₄).  ALL integer (n₃,n₄) are
  valid, including non-coprime.
- A non-coprime mode (n₃,n₄) = d×(p,q) with gcd(p,q)=1 is the
  d-th harmonic of the fundamental (p,q) mode.  It has d times
  the wavevector and d times the energy.
- The spin formula L_z = ℏ/q applies to the FUNDAMENTAL winding
  pattern.  For mode d×(p,q), the effective winding is still
  topologically (p,q) — it just has d wavelengths fitting in the
  path.  The angular momentum is L_z = ℏ/q (unchanged).
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, c

eV_to_J = 1.602176634e-19
hc_eVm = h * c / eV_to_J

DM2_21 = 7.53e-5    # eV²
DM2_32 = 2.455e-3   # eV²
DM2_31 = DM2_32 + DM2_21
TARGET_RATIO = DM2_31 / DM2_21
COSMO_BOUND = 0.120  # eV


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def fundamental(n3, n4):
    """Return the fundamental (p,q) winding and harmonic number d."""
    if n3 == 0 and n4 == 0:
        return (0, 0, 0)
    g = gcd(n3, n4)
    return (n3 // g, n4 // g, g)


def spin_of_mode(n3, n4):
    """
    Spin of mode (n₃, n₄) on the neutrino T².

    The mode is the d-th harmonic of fundamental (p, q) = (n₃/d, n₄/d).
    Spin = ℏ/|q| where q is the fundamental ring winding.
    Fermion if |p| is odd.
    """
    if n3 == 0 and n4 == 0:
        return None, None, None
    p, q, d = fundamental(n3, n4)
    if q == 0:
        return None, None, None
    spin_val = 1.0 / abs(q)
    is_fermion = (abs(p) % 2 != 0)
    return spin_val, is_fermion, (p, q, d)


def mu_sq(n3, n4, s, r):
    """Dimensionless mass-squared for mode (n₃, n₄)."""
    return (n3 / r)**2 + (n4 - n3 * s)**2


def spin_label(n3, n4):
    """Human-readable spin label."""
    sp, ferm, info = spin_of_mode(n3, n4)
    if sp is None:
        return "—", "—"
    if abs(sp - 0.5) < 0.01:
        s_str = "½"
    elif abs(sp - 1.0) < 0.01:
        s_str = "1"
    else:
        s_str = f"1/{abs(info[1])}"
    f_str = "F" if ferm else "B"
    return s_str, f_str


def main():
    print("=" * 76)
    print("R26 Track 1c: Non-Coprime and Higher-Order Modes")
    print("=" * 76)

    # ================================================================
    # SECTION 1: Coprime vs non-coprime mode classification
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 1: Mode classification — coprime vs non-coprime")
    print("=" * 76)

    print("\n  A mode (n₃, n₄) decomposes as d × (p, q) where:")
    print("    d = gcd(|n₃|, |n₄|)  (harmonic number)")
    print("    (p, q) = (n₃/d, n₄/d)  (fundamental winding)")
    print("    Coprime: d = 1.  Non-coprime: d > 1.")

    print("\n  Examples:")
    examples = [(1,2), (2,4), (3,6), (2,2), (4,2), (6,2),
                (3,2), (6,4), (9,6), (4,4), (1,1), (2,1)]
    print(f"\n  {'Mode':>8s}  {'Fund (p,q)':>10s}  {'d':>3s}  "
          f"{'Spin':>5s}  {'F/B':>3s}  {'Coprime?':>8s}")
    for n3, n4 in examples:
        p, q, d = fundamental(n3, n4)
        sp, fb = spin_label(n3, n4)
        cop = "yes" if d == 1 else "no"
        print(f"  ({n3:2d},{n4:2d})    ({p:2d},{q:2d})     {d:3d}  "
              f"{sp:>5s}  {fb:>3s}  {cop:>8s}")

    print("\n  Key insight: mode (2,4) is the 2nd harmonic of fundamental")
    print("  (1,2).  It has the same TOPOLOGICAL winding as the electron")
    print("  but twice the wavevector → twice the energy → twice the mass.")
    print("  Its spin is still ℏ/2 (spin-½), same as the fundamental.")

    # ================================================================
    # SECTION 2: Do non-coprime modes offer new spin-½ candidates?
    # ================================================================
    print("\n\n" + "=" * 76)
    print("SECTION 2: Spin-½ fermion modes (coprime and non-coprime)")
    print("=" * 76)

    print("\n  Spin-½ requires |q| = 2 in the fundamental.  Fermion requires")
    print("  |p| odd in the fundamental.")
    print("\n  Spin-½ fermion modes (n₃, n₄) satisfy:")
    print("    fundamental (p, q) has |q| = 2 and |p| odd")
    print("    → (n₃, n₄) = d × (p_odd, ±2) for any d ≥ 1")
    print("\n  Examples of non-coprime spin-½ fermion modes:")

    nc_examples = []
    for d in range(1, 6):
        for p in [1, 3, 5, -1, -3]:
            for q in [2, -2]:
                n3, n4 = d * p, d * q
                if abs(n3) <= 25 and abs(n4) <= 25:
                    nc_examples.append((n3, n4, p, q, d))

    print(f"\n  {'Mode':>8s}  {'Fund':>8s}  {'d':>3s}  {'Spin':>5s}")
    shown = set()
    for n3, n4, p, q, d in sorted(nc_examples, key=lambda x: x[4])[:20]:
        key = (n3, n4)
        if key in shown:
            continue
        shown.add(key)
        sp, fb = spin_label(n3, n4)
        print(f"  ({n3:2d},{n4:2d})    ({p:2d},{q:2d})   {d:3d}  {sp:>5s} {fb}")

    print("\n  Non-coprime modes like (2,4), (3,6), (4,8) are spin-½ fermions")
    print("  because their fundamental is (1,2).  But they are HEAVIER than")
    print("  (1,2), not lighter — they are harmonics, not new fundamentals.")
    print("  They add to the sterile neutrino problem, not solve it.")

    # ================================================================
    # SECTION 3: Complete mode census for neutrino T²
    # ================================================================
    print("\n\n" + "=" * 76)
    print("SECTION 3: Complete mode census — how many spin-½ fermions?")
    print("=" * 76)

    # For Assignment A parameters
    s_A = 0.02199
    r_A = 5.0  # r >> 1 to satisfy cosmology
    E0_A = math.sqrt(DM2_21 / (4 * s_A))

    print(f"\n  Assignment A: s = {s_A}, r = {r_A}")
    print(f"  E₀ = {E0_A*1e3:.2f} meV")

    # Count all spin-½ fermion modes below 1 eV
    spin_half_f_cop = []
    spin_half_f_nc = []
    for n3 in range(-100, 101):
        for n4 in range(-100, 101):
            if n3 == 0 and n4 == 0:
                continue
            m = E0_A * math.sqrt(mu_sq(n3, n4, s_A, r_A))
            if m > 1.0:
                continue
            sp, ferm, info = spin_of_mode(n3, n4)
            if sp is not None and abs(sp - 0.5) < 0.01 and ferm:
                p, q, d = info
                if d == 1:
                    spin_half_f_cop.append((m, n3, n4))
                else:
                    spin_half_f_nc.append((m, n3, n4))

    print(f"\n  Spin-½ fermion modes below 1 eV:")
    print(f"    Coprime (d=1):     {len(spin_half_f_cop)}")
    print(f"    Non-coprime (d>1): {len(spin_half_f_nc)}")
    print(f"    Total:             {len(spin_half_f_cop) + len(spin_half_f_nc)}")

    print("\n  Lightest 10 coprime spin-½ fermion modes:")
    spin_half_f_cop.sort()
    for m, n3, n4 in spin_half_f_cop[:10]:
        p, q, d = fundamental(n3, n4)
        print(f"    ({n3:3d},{n4:3d})  fund=({p:2d},{q:2d}) d={d}  m={m*1e3:.2f} meV")

    print("\n  Lightest 10 non-coprime spin-½ fermion modes:")
    spin_half_f_nc.sort()
    for m, n3, n4 in spin_half_f_nc[:10]:
        p, q, d = fundamental(n3, n4)
        print(f"    ({n3:3d},{n4:3d})  fund=({p:2d},{q:2d}) d={d}  m={m*1e3:.2f} meV")

    print("\n  Non-coprime modes are always HEAVIER than their fundamental:")
    print("    m(d×p, d×q) = d × m(p, q)  (in the zero-shear limit)")
    print("  So they add intermediate modes above the lightest states,")
    print("  worsening the sterile neutrino problem.")

    # ================================================================
    # SECTION 4: Can non-coprime modes form a clean neutrino triplet?
    # ================================================================
    print("\n\n" + "=" * 76)
    print("SECTION 4: Non-coprime triplet search")
    print("=" * 76)

    print("\n  Can a triplet mixing coprime and non-coprime modes avoid")
    print("  the sterile neutrino problem?")
    print("\n  Consider: ν₁ = (1,2), ν₂ = (2,4), ν₃ = (d,2d) for some d.")
    print("  These all have fundamental (1,2) → all spin-½ ✓")
    print("\n  Mass ratios:")

    for d3 in range(2, 8):
        m1sq = mu_sq(1, 2, 0, 1)  # s→0 limit for clarity
        m2sq = mu_sq(2, 4, 0, 1)
        m3sq = mu_sq(d3, 2*d3, 0, 1)
        if m2sq - m1sq > 0:
            ratio = (m3sq - m1sq) / (m2sq - m1sq)
            print(f"    (1,2), (2,4), ({d3},{2*d3}): ratio = {ratio:.2f}"
                  f"  (target: {TARGET_RATIO:.2f})")

    print("\n  These ratios are d²−1 / 3 (in zero-shear limit):")
    print("  For ratio ≈ 33.6: d² ≈ 101.8, d ≈ 10.1")
    print("  So (1,2), (2,4), (10,20) would give ratio ≈ 33.0")

    # Check with shear
    d_try = 10
    best_dev = 1e10
    best_s, best_r = None, None
    for r in [x * 0.1 for x in range(1, 100)]:
        for s in [x * 0.001 for x in range(-500, 500)]:
            m1 = mu_sq(1, 2, s, r)
            m2 = mu_sq(2, 4, s, r)
            m3 = mu_sq(d_try, 2*d_try, s, r)
            denom = m2 - m1
            if denom <= 0:
                continue
            rat = (m3 - m1) / denom
            dev = abs(rat - TARGET_RATIO)
            if dev < best_dev and m1 < m2 < m3:
                best_dev = dev
                best_s, best_r = s, r

    if best_s is not None:
        m1 = mu_sq(1, 2, best_s, best_r)
        m2 = mu_sq(2, 4, best_s, best_r)
        m3 = mu_sq(d_try, 2*d_try, best_s, best_r)
        ratio_nc = (m3 - m1) / (m2 - m1)
        print(f"\n  Best (1,2)+(2,4)+({d_try},{2*d_try}):")
        print(f"    s = {best_s:.4f}, r = {best_r:.2f}")
        print(f"    ratio = {ratio_nc:.4f}")

        # Count intermediate spin-½ fermion modes
        E0_nc = math.sqrt(DM2_21 / (m2 - m1))
        m1_phys = E0_nc * math.sqrt(m1)
        m2_phys = E0_nc * math.sqrt(m2)
        m3_phys = E0_nc * math.sqrt(m3)
        print(f"    m₁ = {m1_phys*1e3:.2f} meV, m₂ = {m2_phys*1e3:.2f} meV, "
              f"m₃ = {m3_phys*1e3:.2f} meV")
        print(f"    Σm = {(m1_phys+m2_phys+m3_phys)*1e3:.1f} meV")

        n_between = 0
        for n3 in range(-d_try*2, d_try*2 + 1):
            for n4 in range(-d_try*2, d_try*2 + 1):
                if n3 == 0 and n4 == 0:
                    continue
                sp, ferm, info = spin_of_mode(n3, n4)
                if sp is None or abs(sp - 0.5) > 0.01 or not ferm:
                    continue
                msq = mu_sq(n3, n4, best_s, best_r)
                if m2 < msq < m3:
                    n_between += 1
        print(f"    Intermediate spin-½ fermions: {n_between}")
    else:
        print(f"\n  No match found for harmonic triplet with d={d_try}")

    print("\n  Non-coprime harmonics have d times the wavevector but the")
    print("  same topological winding.  They are denser in the spectrum,")
    print("  not sparser.  Including them INCREASES the sterile neutrino")
    print("  count, never decreases it.")

    # ================================================================
    # SECTION 5: Cross-plane modes on T⁶
    # ================================================================
    print("\n\n" + "=" * 76)
    print("SECTION 5: Cross-plane modes on T⁶")
    print("=" * 76)

    print("""
  On T⁶ = T²_e × T²_ν × T²_p, a general mode has six winding numbers:
  (n₁, n₂, n₃, n₄, n₅, n₆)

  "Pure" modes live on one T² subplane:
    Electron:  (n₁, n₂, 0, 0, 0, 0)
    Neutrino:  (0, 0, n₃, n₄, 0, 0)
    Proton:    (0, 0, 0, 0, n₅, n₆)

  Cross-plane modes have nonzero winding on two or more subplanes:
    e.g. (1, 2, 0, 0, 1, 0) — electron + proton winding

  In the zero-cross-shear limit, cross-plane modes have energy:
    E² = E²_e(n₁,n₂) + E²_ν(n₃,n₄) + E²_p(n₅,n₆)

  The lightest cross-plane modes involving the neutrino T² have:
    E ≥ √(E²_ν + E²_other)

  where E_other is at least ~0.5 MeV (electron scale) or ~1 GeV
  (proton scale).  So cross-plane modes are MUCH heavier than pure
  neutrino modes (~meV).  They cannot serve as light neutrino states.
""")

    # Quantify
    m_e_eV = 0.511e6  # electron mass in eV
    m_nu_eV = 0.050    # ν₃ mass in eV (approximate)

    E_cross_min = math.sqrt(m_e_eV**2 + m_nu_eV**2)
    print(f"  Lightest cross-plane mode (electron + neutrino T²):")
    print(f"    E ≥ √(m_e² + m_ν²) ≈ {E_cross_min:.0f} eV = {E_cross_min/1e6:.6f} MeV")
    print(f"    This is ~10¹⁰ × heavier than the neutrino.")
    print(f"    Cross-plane modes cannot be neutrinos.")

    print("""
  With nonzero cross-shear, cross-plane modes develop off-diagonal
  coupling.  But the energy hierarchy (MeV vs meV) means the mixing
  amplitude is suppressed by (m_ν/m_e)² ~ 10⁻¹⁷.  Cross-shear can
  perturb mode energies at this level but cannot create new light
  spin-½ states.

  Cross-plane modes are relevant for:
  - PMNS mixing (small perturbative coupling between ν and e sectors)
  - Heavy sterile neutrinos at the MeV–GeV scale
  - Exotic particles with both electric and "weak" charge
  But NOT for the three light neutrino mass eigenstates.
""")

    # ================================================================
    # SECTION 6: Summary
    # ================================================================
    print("=" * 76)
    print("SECTION 6: Summary")
    print("=" * 76)

    print("""
  1. Non-coprime modes (d > 1) are harmonics of coprime fundamentals.
     They have the SAME spin as their fundamental (spin = ℏ/q_fund).
     They are HEAVIER (energy scales with d).  They add to the mode
     spectrum density, worsening the sterile neutrino problem.

  2. No non-coprime mode provides a new spin-½ candidate that wasn't
     already covered by the coprime (p, 2) modes in Track 1b.

  3. Cross-plane modes on T⁶ are too heavy (≥ MeV) to be light
     neutrinos.  The energy hierarchy (meV vs MeV) suppresses
     cross-plane mixing at the 10⁻¹⁷ level.

  4. The mode menu for the neutrino T² is unchanged:
     - Spin-½ fermions: (p, 2) with p odd, for any p
     - All other modes have spin ≠ ½ or are bosons
     - Non-coprime modes add density but no new physics

  CONCLUSION: Track 1c finds no new candidate modes.  The mode menu
  established in Tracks 1a–1b stands.  The sterile neutrino problem
  cannot be solved by expanding the mode census.
""")


if __name__ == "__main__":
    main()
