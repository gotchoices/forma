#!/usr/bin/env python3
"""
R14 Track 1: Charge of linked photons on T³.

BACKGROUND
==========
R19 derived the single-photon charge formula on sheared T³:

    Q ∝ cos(π(s₁₂+s₁₃)) × sin(πs₁₂) × sin(πs₁₃)
        / ((n₂ - s₁₂)(n₃ - s₁₃))

Key results from R19:
- s₁₂ ≈ 0.165 (sets α for the electron)
- s₁₃ = 0 (protects electron planarity, F31)
- s₂₃ free (irrelevant for charge)
- n₁ = 1 required for charge (F30)
- At s₁₃ = 0: only n₃ = 0 modes carry charge (F31)

QUESTION
========
R14 proposes the proton as three photons, topologically linked
on T³, one in each of the three linking planes (F2):

| Plane   | Winding       |
|---------|---------------|
| (1,2)   | (p, q, 0)     |
| (2,3)   | (0, p, q)     |
| (1,3)   | (p, 0, q)     |

What is the total charge of this three-photon state?
How does it compare to the proton charge (+e)?
What are the individual charges?

THIS SCRIPT
===========
1. Compute individual photon charges using R19's formula
2. Sum to get total charge for candidate proton configurations
3. Analyze the (1, n₂, 0) charge spectrum — are there lighter
   charged modes that would contradict observation?
4. Analyze spin quantum numbers for each mode
5. Examine mass constraints and DIS implications
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C


def charge_integral_3d(n1, n2, n3, s12, s13):
    """
    Charge integral for (n₁, n₂, n₃) mode on sheared T³.

    For n₁ ≠ 1: returns 0 (selection rule F30).

    For n₁ = 1:
        I = 4 cos(π(s₁₂+s₁₃)) sin(πs₁₂) sin(πs₁₃)
            / ((n₂ - s₁₂)(n₃ - s₁₃))

    At s₁₃ = 0: sin(πs₁₃)/(n₃-s₁₃) → 0 for n₃≠0, → -π for n₃=0.
    """
    if n1 != 1:
        return 0.0

    q2 = n2 - s12
    q3 = n3 - s13

    if abs(s13) < 1e-12:
        if n3 == 0:
            factor3 = -math.pi
        else:
            return 0.0
    else:
        if abs(q3) < 1e-12:
            return float('inf')
        factor3 = math.sin(math.pi * s13) / q3

    if abs(q2) < 1e-12:
        return float('inf')

    common = 4 * math.cos(math.pi * (s12 + s13))
    factor2 = math.sin(math.pi * s12) / q2

    return common * factor2 * factor3


def geodesic_length(n1, n2, n3, L1, L2, L3, s12, s13, s23):
    """Geodesic length for winding (n₁,n₂,n₃) on sheared T³."""
    d1 = L1 * (n1 + n2 * s12 + n3 * s13)
    d2 = L2 * (n2 + n3 * s23)
    d3 = L3 * n3
    return math.sqrt(d1**2 + d2**2 + d3**2)


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
    fs = [f(s) for s in ss]
    for i in range(len(fs) - 1):
        if fs[i] * fs[i + 1] < 0:
            return brentq(f, ss[i], ss[i + 1], xtol=1e-14)
    return None


def main():
    E_mc2 = m_e * c**2

    print("=" * 72)
    print("R14 Track 1: Charge of Linked Photons on T³")
    print("=" * 72)

    # ------------------------------------------------------------------
    # Setup: electron geometry from R19
    # ------------------------------------------------------------------
    r = 1.0
    s12 = solve_electron_s(r)
    s13 = 0.0
    s23 = 0.0
    print(f"\nGeometry: r = {r}, s₁₂ = {s12:.6f}, s₁₃ = {s13}, s₂₃ = {s23}")

    L2 = lambda_C / (2 * math.pi * math.sqrt(r**2 * (1 + 2 * s12)**2 + 4))
    L1 = r * L2
    print(f"L₁ = {L1:.4e} m,  L₂ = {L2:.4e} m")

    L_e = geodesic_length(1, 2, 0, L1, L2, 1, s12, s13, s23)
    print(f"Electron geodesic: L_e = {L_e:.4e} m,  λ_C = {lambda_C:.4e} m")
    print(f"L_e/λ_C = {L_e/lambda_C:.6f}")

    I_e = charge_integral_3d(1, 2, 0, s12, s13)
    print(f"Electron charge integral: I_e = {I_e:.6f}")

    # ==================================================================
    print("\n" + "=" * 72)
    print("SECTION 1: Candidate proton configurations")
    print("=" * 72)
    # ==================================================================

    print("""
R14 F2 identifies three linking planes on T³:
  (1,2) plane: winding (p, q, 0)
  (2,3) plane: winding (0, p, q)
  (1,3) plane: winding (p, 0, q)

For a Borromean link, one photon in each plane.

Proton candidate A (simplest):
  Photon 1: (1, 2, 0) — electron-type, in (1,2) plane
  Photon 2: (0, 1, 2) — in (2,3) plane
  Photon 3: (1, 0, 2) — in (1,3) plane
""")

    configs = {
        "Proton A": [
            ("(1,2,0)", 1, 2, 0),
            ("(0,1,2)", 0, 1, 2),
            ("(1,0,2)", 1, 0, 2),
        ],
        "Proton B": [
            ("(1,2,0)", 1, 2, 0),
            ("(0,2,1)", 0, 2, 1),
            ("(1,0,1)", 1, 0, 1),
        ],
    }

    for name, photons in configs.items():
        print(f"--- {name} ---")
        total_I = 0.0
        for label, n1, n2, n3 in photons:
            I = charge_integral_3d(n1, n2, n3, s12, s13)
            ratio = I / I_e if abs(I_e) > 1e-12 else 0.0
            total_I += I
            reason = ""
            if n1 != 1:
                reason = " [n₁ ≠ 1 → Q = 0]"
            elif n3 != 0 and abs(s13) < 1e-6:
                reason = " [n₃ ≠ 0, s₁₃ = 0 → Q = 0]"
            print(f"  {label}: I = {I:+.4f}, Q/Q_e = {ratio:+.4f}{reason}")
        total_ratio = total_I / I_e if abs(I_e) > 1e-12 else 0.0
        print(f"  Total: I = {total_I:+.4f}, Q_total/Q_e = {total_ratio:+.4f}")
        print()

    print("""RESULT: With s₁₃ = 0, the charge of a three-photon linked state
is determined entirely by the (1,2)-plane photon.

  - Photon in (2,3) plane has n₁ = 0 → zero charge (n₁ selection rule).
  - Photon in (1,3) plane has n₃ ≠ 0 with s₁₃ = 0 → zero charge (F31).
  - Only the (1,2)-plane photon carries charge, contributing Q = e.

Total charge = e, matching the proton.  This holds for ANY winding
numbers (p,q) in the other two planes, as long as:
  - (2,3) photon has n₁ = 0 (guaranteed by definition)
  - (1,3) photon has n₃ ≠ 0 (guaranteed for non-trivial winding)
""")

    # ==================================================================
    print("=" * 72)
    print("SECTION 2: Neutron candidates")
    print("=" * 72)
    # ==================================================================

    print("""
For total charge = 0, the (1,2)-plane photon must ALSO have zero charge.
Since (2,3) and (1,3) photons always have zero charge at s₁₃ = 0,
the only way to get a neutron is for the (1,2) photon to be uncharged.

With s₁₃ = 0, a (1,2)-plane mode (n₁, n₂, 0) is uncharged when n₁ ≠ 1.

Candidates:""")

    neutron_configs = [
        ("(2, 1, 0)", 2, 1, 0),
        ("(2, 4, 0)", 2, 4, 0),
        ("(3, 2, 0)", 3, 2, 0),
        ("(0, 1, 0)", 0, 1, 0),
    ]

    for label, n1, n2, n3 in neutron_configs:
        I = charge_integral_3d(n1, n2, n3, s12, s13)
        L_mode = geodesic_length(n1, n2, n3, L1, L2, 1.0, s12, s13, s23)
        E_ratio = L_e / L_mode if L_mode > 0 else 0
        spin_str = f"{n1}/{n2}" if n2 != 0 else "∞"
        print(f"  {label}: I = {I:+.6f}, E/m_e = {E_ratio:.3f}, "
              f"winding ratio = {spin_str}")

    print("""
The neutron's (1,2)-plane photon must have n₁ ≠ 1.  The (2,1,0)
mode is the simplest.  Its winding ratio is 2/1 → spin 2 (boson).
The (2,4,0) mode has ratio 2/4 = 1/2 → spin 1/2 (fermion).

A neutron with (2,4,0) in the (1,2) plane preserves spin 1/2 and
has n₁ = 2 → zero charge.  Its geodesic is 2× the electron's,
so the photon energy is m_e/2 (much lighter than a proton quark).
This is an issue for mass — see Section 5.
""")

    # ==================================================================
    print("=" * 72)
    print("SECTION 3: Charge spectrum of (1, n₂, 0) modes")
    print("=" * 72)
    # ==================================================================

    print("""
At s₁₃ = 0, ALL modes (1, n₂, 0) carry charge (since n₁ = 1 and
n₃ = 0).  R19 F31 only protects against n₃ ≠ 0 modes.

Are there lighter charged modes besides the electron (1,2,0)?
""")

    print(f"{'n₂':>4}  {'I(mode)':>10}  {'Q/Q_e':>8}  {'E/m_e':>8}  "
          f"{'spin':>6}  {'status':>20}")
    print("-" * 72)

    for n2 in range(1, 10):
        I = charge_integral_3d(1, n2, 0, s12, s13)
        ratio = I / I_e if abs(I_e) > 1e-12 else 0.0

        L_mode = geodesic_length(1, n2, 0, L1, L2, 1.0, s12, s13, s23)
        E_ratio = L_e / L_mode if L_mode > 0 else 0

        # E₀ normalization correction: Q ∝ √E × I
        Q_ratio = ratio * math.sqrt(E_ratio) if E_ratio > 0 else 0

        spin_val = 1.0 / n2
        spin_str = f"1/{n2}"
        if n2 == 1:
            spin_str = "1"
        elif n2 == 2:
            spin_str = "1/2"

        valid_spin = (n2 == 1 or n2 == 2)
        if n2 == 2:
            status = "ELECTRON"
        elif not valid_spin:
            status = f"spin {spin_str} forbidden?"
        elif E_ratio < 1:
            status = "lighter + charged!"
        else:
            status = "heavier"

        print(f"{n2:4d}  {I:+10.4f}  {Q_ratio:+8.4f}  {E_ratio:8.4f}  "
              f"{spin_str:>6}  {status:>20}")

    print("""
KEY OBSERVATION: (1, n₂, 0) modes with n₂ > 2 are LIGHTER than the
electron and carry charge.  However, their winding ratio is 1/n₂,
which gives spin 1/n₂ — not a valid quantum number for n₂ > 2.

In 3+1D spacetime, angular momentum is quantized as J = nℏ/2.
The phase picked up under one φ-revolution for a (1, q) knot is
exp(i2π/q).  This gives:
  q = 1: exp(i2π) = +1  → boson (spin 1)
  q = 2: exp(iπ)  = −1  → fermion (spin 1/2)
  q = 3: exp(i2π/3)     → anyonic (forbidden in 3+1D)
  q > 2: exotic phase   → not a boson or fermion

If modes with q > 2 are topologically forbidden in 3+1D, then:
  - Only (1,1,0) [spin 1, charged boson] and (1,2,0) [spin 1/2, electron]
    exist as physical charged states.
  - (1,1,0) is HEAVIER than the electron → no lighter charged particle.
  - The electron is protected as the lightest charged fermion.
""")

    # ==================================================================
    print("=" * 72)
    print("SECTION 4: Spin analysis — which modes are physical?")
    print("=" * 72)
    # ==================================================================

    print("""
The key topological constraint: on a torus, a (p, q) geodesic
returns to its starting point after q full revolutions in the
φ direction.  The wavefunction picks up phase exp(i2πp/q) per
φ-revolution.

Quantum mechanics in 3+1D requires integer or half-integer spin,
restricting q to:
  q = 1 (one revolution to close) → bosonic
  q = 2 (two revolutions to close) → fermionic

For the (1, n₂, 0) family on T³ (direction 2 plays role of φ):
  n₂ = 1: closes after 1 period → boson (spin 1)     → W±?
  n₂ = 2: closes after 2 periods → fermion (spin 1/2) → electron
  n₂ ≥ 3: closes after n₂ periods → spin 1/n₂        → FORBIDDEN

If this argument holds:
  - ALL (1, n₂, 0) modes with n₂ ≥ 3 are unphysical.
  - The charged particle spectrum in the (1,2) plane is:
    (1,1,0): charged spin-1 boson, E ≈ 1.58 m_e ≈ 0.81 MeV
    (1,2,0): charged spin-1/2 fermion = electron, E = m_e = 0.511 MeV
  - No lighter charged particle exists.
""")

    print("Extended mode table with spin constraint applied:\n")
    print(f"{'mode':>10}  {'Q/Q_e':>8}  {'E/m_e':>8}  {'spin':>8}  {'physical?':>12}")
    print("-" * 60)

    for n2 in [1, 2, 3, 4, 6]:
        I = charge_integral_3d(1, n2, 0, s12, s13)
        ratio = I / I_e if abs(I_e) > 1e-12 else 0.0
        L_mode = geodesic_length(1, n2, 0, L1, L2, 1.0, s12, s13, s23)
        E_ratio = L_e / L_mode if L_mode > 0 else 0
        Q_ratio = ratio * math.sqrt(E_ratio) if E_ratio > 0 else 0
        spin_str = f"1/{n2}" if n2 > 2 else ("1/2" if n2 == 2 else "1")
        phys = "YES" if n2 <= 2 else "no (spin)"
        label = f"(1,{n2},0)"
        if n2 == 2:
            label += " e⁻"
        print(f"{label:>10}  {Q_ratio:+8.4f}  {E_ratio:8.4f}  {spin_str:>8}  {phys:>12}")

    # ==================================================================
    print("\n" + "=" * 72)
    print("SECTION 5: Mass analysis for proton photons")
    print("=" * 72)
    # ==================================================================

    print("""
The proton's three photons must sum to m_p = 1836 m_e.
R14 F3 noted 1836 = 3 × 612, suggesting each photon at the
612th harmonic.

But the n₁ = 1 selection rule (F30) means:
  The nth harmonic of (1,2,0) is the mode (n, 2n, 0) with n₁ = n.
  For n > 1, this has n₁ ≠ 1 → ZERO CHARGE.

So high harmonics of the electron geodesic are UNCHARGED.
The proton cannot be built from high harmonics of (1,2,0).

ALTERNATIVE: the proton's mass comes from photons in the other
two planes, which carry no charge regardless of energy:
""")

    L3_candidates = [lambda_C / 612, lambda_C / 306, 0.66e-15, 0.84e-15]
    L3_labels = ["λ_C/612", "λ_C/306", "0.66 fm", "0.84 fm"]

    print(f"{'L₃':>12}  {'E(0,0,1)/m_e':>14}  {'E(0,1,2)/m_e':>14}  "
          f"{'3×E(0,0,1)/m_e':>16}  {'proton?':>10}")
    print("-" * 72)

    for L3, label in zip(L3_candidates, L3_labels):
        E_001 = (h * c / L3) / E_mc2
        L_012 = geodesic_length(0, 1, 2, L1, L2, L3, s12, s13, s23)
        E_012 = (h * c / L_012) / E_mc2 if L_012 > 0 else 0
        total_3 = 3 * E_001
        close = "≈1836" if abs(total_3 - 1836) / 1836 < 0.01 else ""
        print(f"{label:>12}  {E_001:14.1f}  {E_012:14.1f}  "
              f"{total_3:16.1f}  {close:>10}")

    print(f"""
If L₃ = λ_C/612 = {lambda_C/612:.3e} m ≈ {lambda_C/612*1e15:.2f} fm:
  Three (0,0,1) photons each have E = 612 m_e → total = 1836 m_e ✓
  But these have n₁ = 0 → ZERO CHARGE.

So the proton model becomes:
  (1,2,0):   charge = e, energy = m_e    (the "valence charge carrier")
  (0,0,1) ×2: charge = 0, energy = 612 m_e each  (the "mass carriers")
  Total: charge = e, mass ≈ 1225 m_e (not 1836 m_e)

Or with three (0,0,1) photons + one (1,2,0):
  Total mass = 3×612 + 1 = 1837 m_e ≈ m_p ✓
  Total charge = e ✓
  But this is FOUR photons, not three.
""")

    # ==================================================================
    print("=" * 72)
    print("SECTION 6: The charge-mass tension")
    print("=" * 72)
    # ==================================================================

    print("""
There is a fundamental tension between charge and mass:

CHARGE requires n₁ = 1 (F30).  On the electron's T³, modes with
n₁ = 1 have energy ~ m_e (Compton scale).  Getting proton-scale
energy (612 m_e) from an n₁ = 1 mode would require the geodesic
length L ~ λ_C/612, which means very high winding numbers.

The only n₁ = 1 modes with E >> m_e are (1, n₂, 0) with very SMALL
n₂ (negative or zero), which have SHORT geodesics:
""")

    print(f"{'mode':>12}  {'L/L_e':>8}  {'E/m_e':>8}  {'charged?':>10}  {'spin':>8}")
    print("-" * 60)

    test_modes = [
        (1, -4, 0), (1, -2, 0), (1, -1, 0), (1, 0, 0),
        (1, 1, 0), (1, 2, 0), (1, 4, 0),
    ]
    for n1, n2, n3 in test_modes:
        L_mode = geodesic_length(n1, n2, n3, L1, L2, 1.0, s12, s13, s23)
        E_ratio = L_e / L_mode if L_mode > 0 else 0
        I = charge_integral_3d(n1, n2, n3, s12, s13)
        charged = "yes" if abs(I) > 1e-6 else "no"
        if n2 == 0:
            spin_str = "∞"
        else:
            from math import gcd
            g = gcd(abs(n1), abs(n2))
            p, q = abs(n1) // g, abs(n2) // g
            spin_str = f"{p}/{q}" if q > 1 else str(p)

        print(f"  ({n1},{n2:+d},{n3}){'':<4}  {L_mode/L_e:8.4f}  "
              f"{E_ratio:8.2f}  {charged:>10}  {spin_str:>8}")

    print("""
Modes with large |n₂| (negative) can have short geodesics and high
energy, but they have non-physical spin (1/|n₂|) unless |n₂| ≤ 2.

The charged, physical modes accessible at proton energies:
  (1, -2, 0): spin 1/2, E ≈ ? m_e — COULD be a heavy charged fermion
  (1, -1, 0): spin 1,   E ≈ ? m_e — charged boson
""")

    print("\nEnergies of (1, n₂, 0) modes including negative n₂:")
    print(f"{'n₂':>5}  {'E/m_e':>10}  {'spin':>6}  {'physical?':>12}  {'Q/Q_e':>8}")
    print("-" * 56)
    for n2 in range(-6, 7):
        L_mode = geodesic_length(1, n2, 0, L1, L2, 1.0, s12, s13, s23)
        E_ratio = L_e / L_mode if L_mode > 0 else 0
        I = charge_integral_3d(1, n2, 0, s12, s13)
        Q_ratio = (I / I_e) * math.sqrt(E_ratio) if abs(I_e) > 1e-12 and E_ratio > 0 else 0

        if n2 == 0:
            spin_str = "∞"
            phys = "no"
        else:
            g = math.gcd(1, abs(n2))
            q_spin = abs(n2) // g
            spin_str = f"1/{q_spin}" if q_spin > 2 else ("1/2" if q_spin == 2 else "1")
            phys = "YES" if q_spin <= 2 else "no"

        print(f"{n2:5d}  {E_ratio:10.4f}  {spin_str:>6}  {phys:>12}  {Q_ratio:+8.4f}")

    # ==================================================================
    print("\n" + "=" * 72)
    print("SECTION 7: Deep inelastic scattering constraint")
    print("=" * 72)
    # ==================================================================

    print("""
DIS experiments observe three scattering centers in the proton,
each coupling to the EM field with strength proportional to e_i²:

  Standard model: e_u = 2/3, e_d = 1/3
    Σ e_i² = (2/3)² + (2/3)² + (1/3)² = 1

Our model (naive, unlinked charges):
  Photon 1 (1,2,0): charge = e     → e₁² = 1
  Photon 2 (0,1,2): charge = 0     → e₂² = 0
  Photon 3 (1,0,2): charge = 0     → e₃² = 0
    Σ e_i² = 1

The sum Σ e_i² = 1 in both cases — but the distribution is
completely different:
  SM:    three scattering centers with e² = 4/9, 4/9, 1/9
  Model: ONE scattering center with e² = 1, two dark

DIS clearly resolves three separate scattering centers.  If our
model has only one charged parton, it contradicts this observation.

POSSIBLE RESOLUTIONS:
1. Linking modifies the individual photon charges, redistributing
   charge from the (1,2) photon into the other two.
2. The "scattering centers" in DIS correspond to something other
   than individual photon charges — perhaps the linking points
   themselves scatter.
3. The model is wrong about individual photon charges.
""")

    # ==================================================================
    print("=" * 72)
    print("SECTION 8: What linking would need to accomplish")
    print("=" * 72)
    # ==================================================================

    print("""
For the model to match observations, linking must:

1. CHARGE: redistribute charge from (e, 0, 0) to (2e/3, 2e/3, -e/3)
   or some other partition summing to +e.

2. MASS: provide proton-scale energy.  Since charged n₁ = 1 modes
   have E ~ m_e, the proton's mass must come primarily from uncharged
   photons in the third dimension.  Linking might bind these together.

3. DIS: create three distinct scattering centers, each with EM coupling.

4. CONFINEMENT: prevent individual photons from separating (Borromean
   linking provides this topologically).

The R19 charge formula was derived for a SINGLE delocalized mode on
T³.  For a multi-photon linked state:
  - The fields are superposed (linear EM theory).
  - If delocalized: charges add linearly → (e, 0, 0).
  - If localized (wavepackets): linking imposes boundary conditions
    at crossing points, potentially modifying each photon's
    effective mode structure and hence its charge.

The localization picture is crucial: linked curves are inherently
LOCALIZED — a delocalized mode filling all of T³ uniformly cannot
be "linked" or "unlinked" with another mode.  The proton's photons
must be wavepackets, not plane waves.

For a wavepacket on a sheared T³, the charge depends on the
localization parameter σ (how spread out the wavepacket is):
  σ → ∞ (delocalized): Q → R19 formula (the electron limit)
  σ ~ finite (localized): Q depends on σ, s, and the boundary
  conditions imposed by the linking topology.

The key calculation for Track 1 Step 2 would be:
  compute Q(σ, s₁₂, linking_topology) for a single photon
  in a linked state, and determine whether the linking constraint
  produces fractional charges.
""")

    # ==================================================================
    print("=" * 72)
    print("SECTION 9: Assessment")
    print("=" * 72)
    # ==================================================================

    print("""
FINDINGS:

F8.  Naive proton charge works: three photons, one per linking plane,
     give total charge = +e at s₁₃ = 0.  This is robust — it holds
     for any winding numbers in the (2,3) and (1,3) planes.  The
     charge comes entirely from the (1,2)-plane photon.

F9.  Neutron charge works trivially: if the (1,2)-plane photon has
     n₁ ≠ 1, total charge = 0.  The simplest neutron candidate uses
     (2,4,0) in the (1,2) plane (preserving spin 1/2).

F10. The (1, n₂, 0) charge spectrum and the spin constraint:
     At s₁₃ = 0, all (1, n₂, 0) modes carry charge.  Modes with
     n₂ > 2 are lighter than the electron — but their winding
     ratio 1/n₂ gives spin 1/n₂, which is forbidden in 3+1D
     (only integer and half-integer spins exist).

     If the spin argument holds, the only physical charged modes
     in the (1,2) plane are (1,1,0) [spin 1] and (1,2,0) [spin 1/2].
     The (1,1,0) mode is heavier than the electron.  So the electron
     is the lightest charged fermion — PROTECTED by spin quantization,
     not just by the s₁₃ = 0 selection rule.

F11. The charge-mass tension persists.  The n₁ = 1 rule forces all
     charged modes to have energies ~ m_e on the electron's T³.
     Proton-scale energy (612 m_e) requires either uncharged modes
     (n₁ ≠ 1) or modes in direction 3 (which is charge-invisible
     at s₁₃ = 0).  The proton must be a mixed state: one low-energy
     charged photon + two (or more) high-energy uncharged photons.

F12. DIS is the critical test.  The naive model has one charged
     scattering center, not three.  This contradicts DIS observations.
     Resolving this requires showing that linking modifies the
     individual photon charges — which in turn requires treating
     the photons as localized wavepackets, not delocalized modes.

STRATEGIC ASSESSMENT:

The naive (delocalized mode) calculation gives a clean proton charge
(+e) and neutron charge (0), but the internal structure doesn't match
the Standard Model.  The model predicts one charged parton and two
dark partons, versus the observed three charged partons with
fractional charges.

Two paths forward:
(A) Localized photon charge: compute Q(σ) for a wavepacket on
    sheared T³, then determine whether linking-imposed localization
    redistributes charge.  This is a hard but well-defined calculation.
(B) Multi-component EM: if the three compact directions each contribute
    a U(1) gauge field, and the physical EM is a linear combination
    of all three, then photons in all three planes could carry EM
    charge.  This changes the charge formula.
""")


if __name__ == "__main__":
    main()
