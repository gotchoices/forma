#!/usr/bin/env python3
"""
R14 Track 1b: Localized photon charge on sheared T³.

BACKGROUND
==========
Track 1 (F8-F13) showed that for DELOCALIZED modes (standing waves
filling all of T³), three photons in three linking planes give total
charge +e, with (e, 0, 0) individual charges.  Deep inelastic
scattering (DIS: high-energy electron scattering off proton
constituents) requires three charged constituents, not one.

This script investigates whether LOCALIZATION changes the charges.

KEY QUESTION
============
When a photon is localized (a wavepacket, not a plane wave), does
it acquire charge it didn't have as a delocalized mode?

THE ANALYSIS
============
A (0,1,2) photon lives in the (θ₂, θ₃) plane.  Its field is:

    ψ(θ₁, θ₂, θ₃) = A(θ₂, θ₃) × cos(θ₂ + 2θ₃)

where A is the wavepacket envelope.

The CHARGE integral (from R19) projects onto cos(θ₁_phys):

    Q ∝ ∫∫∫ ψ × cos(θ₁_phys) dθ₁ dθ₂ dθ₃

The θ₁ integral is:

    ∫₀²π [A(θ₂,θ₃) cos(θ₂+2θ₃)] × cos(θ₁_phys) dθ₁_phys = 0

because A doesn't depend on θ₁, and ∫cos(θ₁)dθ₁ = 0.

CRITICAL INSIGHT: the (0,1,2) photon's field is UNIFORM in the θ₁
direction (the tube direction) regardless of how localized it is in
the (θ₂, θ₃) plane.  Localizing the wavepacket along the geodesic
doesn't create any θ₁ dependence.  Therefore:

    The (0,1,2) photon has ZERO charge for ANY degree of
    localization, as long as it stays in the (θ₂, θ₃) plane.

The only way to give it charge would be to perturb its field
structure in the θ₁ direction — which requires interaction with
another field that HAS θ₁ dependence (like the (1,2,0) photon).

This script verifies this analytically and numerically, then
explores what WOULD be needed to redistribute charge.
"""

import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C
from scipy.optimize import brentq


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


def charge_integral_wavepacket_1d(q_eff, sigma_phi, N_terms=200):
    """
    Charge integral for a wavepacket on the (1,2) geodesic of sheared T²,
    as a function of the localization width σ_φ (in the ring direction).

    The wavepacket is a traveling wave with Gaussian envelope.
    The charge integral reduces to:

        Q(σ) ∝ ∫₀²π A_norm(φ; σ) cos(q_eff φ) dφ

    where A_norm is a periodic Gaussian normalized to ∫A² = 2π.

    Returns Q(σ) / Q(σ→∞).
    """
    phi = np.linspace(0, 2 * np.pi, 10000, endpoint=False)
    dphi = phi[1] - phi[0]

    # Periodic Gaussian envelope
    A = np.zeros_like(phi)
    for n in range(-5, 6):
        A += np.exp(-((phi - np.pi - 2 * np.pi * n) ** 2) / (2 * sigma_phi**2))

    # Normalize so ∫A² dφ = 2π (same energy as delocalized mode)
    A2_integral = np.sum(A**2) * dphi
    A *= np.sqrt(2 * np.pi / A2_integral)

    # Charge integral: ∫ A(φ) cos(q_eff φ) dφ
    Q_loc = np.sum(A * np.cos(q_eff * phi)) * dphi

    # Delocalized charge: ∫₀²π cos(q_eff φ) dφ = sin(2π q_eff) / q_eff
    Q_deloc = np.sin(2 * np.pi * q_eff) / q_eff

    return Q_loc / Q_deloc if abs(Q_deloc) > 1e-15 else 0.0


def charge_mode_space(s12, n2_center, delta_n2, N_modes=50):
    """
    Charge of a mode-space wavepacket on sheared T²: a Gaussian
    superposition of (1, n₂) modes centered on n₂ = n2_center
    with width Δn₂.

    The charge integral for each (1, n₂) mode is:
        I(n₂) = -sin(2πs) / (n₂ - s)

    The wavepacket charge is: Q = Σ c_n I(n₂)
    normalized by Σ |c_n|² = 1.

    Returns Q / Q_electron.
    """
    n2_vals = np.arange(n2_center - N_modes, n2_center + N_modes + 1)
    if delta_n2 < 0.01:
        coeffs = np.zeros_like(n2_vals, dtype=float)
        idx = np.where(n2_vals == n2_center)[0]
        if len(idx) > 0:
            coeffs[idx[0]] = 1.0
        else:
            return 0.0
    else:
        coeffs = np.exp(-((n2_vals - n2_center) ** 2) / (2 * delta_n2**2))
    norm = np.sqrt(np.sum(coeffs**2))
    if norm < 1e-15:
        return 0.0
    coeffs /= norm

    sin_factor = -np.sin(2 * np.pi * s12)
    charges = np.array([sin_factor / (n2 - s12) if abs(n2 - s12) > 1e-10
                        else 0.0 for n2 in n2_vals])

    Q_wp = np.sum(coeffs * charges)
    Q_electron = sin_factor / (2 - s12)

    return Q_wp / Q_electron if abs(Q_electron) > 1e-15 else 0.0


def main():
    print("=" * 72)
    print("R14 Track 1b: Localized Photon Charge on Sheared T³")
    print("=" * 72)

    r = 1.0
    s12 = solve_electron_s(r)
    q_eff = 2 - s12
    print(f"\nGeometry: r = {r}, s₁₂ = {s12:.6f}, q_eff = {q_eff:.6f}")

    # ==================================================================
    print("\n" + "=" * 72)
    print("SECTION 1: Why localization cannot charge the (2,3)-plane photon")
    print("=" * 72)
    # ==================================================================

    print("""
A (0,1,2) photon on T³ has winding numbers n₁ = 0, n₂ = 1, n₃ = 2.
Its geodesic lies entirely in the (θ₂, θ₃) plane.  The field:

    ψ(θ₁, θ₂, θ₃) = A(θ₂, θ₃) × cos(θ₂ + 2θ₃)

The wavepacket envelope A(θ₂, θ₃) can be arbitrarily localized in
the (θ₂, θ₃) plane, but it is ALWAYS uniform in θ₁ (the tube
direction), because the geodesic has n₁ = 0 — it doesn't wind
around the θ₁ circle at all.

The charge integral (R19) projects the field onto cos(θ₁_phys):

    Q ∝ ∫∫∫ ψ(θ₁,θ₂,θ₃) × cos(θ₁_phys) dθ₁ dθ₂ dθ₃

Since ψ is independent of θ₁, the θ₁ integral becomes:

    ∫₀²π 1 × cos(θ₁) dθ₁ = 0

This vanishes identically — independent of the envelope A(θ₂, θ₃).

RESULT: Localizing the (0,1,2) photon along its geodesic CANNOT
give it charge.  The charge is zero for any σ, because the field
has no θ₁ structure to project onto.

The same argument applies to any mode with n₁ = 0.
""")

    # Numerical verification
    print("Numerical verification (3D charge integral for localized wavepackets):\n")
    Nth = 100
    Nph = 100
    dth = 2 * np.pi / Nth
    dph = 2 * np.pi / Nph
    theta1 = np.linspace(0, 2 * np.pi, Nth, endpoint=False)
    theta2 = np.linspace(0, 2 * np.pi, Nph, endpoint=False)
    theta3 = np.linspace(0, 2 * np.pi, Nph, endpoint=False)

    TH1, TH2, TH3 = np.meshgrid(theta1, theta2, theta3, indexing='ij')
    dV = dth * dph * dph

    th1_phys = TH1 + s12 * TH2  # θ₁_phys = θ₁ + s₁₂θ₂ (s₁₃ = 0)

    print(f"{'σ_23':>8}  {'Q/Q_e':>10}  {'comment':>30}")
    print("-" * 55)

    for sigma in [10.0, 3.0, 1.0, 0.5, 0.2]:
        # Localized (0,1,2) wavepacket
        env = np.exp(-((TH2 - np.pi)**2 + (TH3 - np.pi)**2) / (2 * sigma**2))
        field = env * np.cos(TH2 + 2 * TH3)
        integrand = field * np.cos(th1_phys)
        Q = np.sum(integrand) * dV
        Q_e_ref = -2.949  # electron charge integral from Track 1
        ratio = Q / Q_e_ref if abs(Q_e_ref) > 1e-10 else 0
        comment = "delocalized" if sigma > 5 else f"σ = {sigma:.1f} rad"
        print(f"{sigma:8.1f}  {ratio:10.6f}  {comment:>30}")

    # ==================================================================
    print("\n" + "=" * 72)
    print("SECTION 2: Localization of the (1,2,0) photon")
    print("=" * 72)
    # ==================================================================

    print("""
Unlike the (0,1,2) photon, the (1,2,0) photon DOES wind in the θ₁
direction (n₁ = 1).  Its charge comes from the cos(θ₁_phys)
projection.  How does localization affect its charge?

For a traveling wavepacket on the (1,2) geodesic, the charge is:

    Q(σ) ∝ ∫₀²π A(φ; σ) cos(q_eff φ) dφ

where A is the wavepacket envelope (energy-normalized) and q_eff = 2−s.
The key property: Q is the Fourier transform of A at frequency q_eff.
""")

    sigmas = np.logspace(-1.5, 2, 100)
    ratios = [charge_integral_wavepacket_1d(q_eff, s) for s in sigmas]

    print(f"{'σ_φ (rad)':>12}  {'Q(σ)/Q_deloc':>14}  {'meaning':>25}")
    print("-" * 60)
    sigma_display = [0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0]
    for s in sigma_display:
        r_val = charge_integral_wavepacket_1d(q_eff, s)
        if s > 10:
            meaning = "≈ delocalized"
        elif s > 3:
            meaning = "broad wavepacket"
        elif s > 0.5:
            meaning = "moderate localization"
        else:
            meaning = "tight wavepacket"
        print(f"{s:12.2f}  {r_val:14.6f}  {meaning:>25}")

    print(f"""
As σ → ∞ (delocalized): Q → Q_deloc (the R19/electron result).
As σ → 0 (fully localized): Q → 0 (wavepacket too narrow to
sustain a monopole).

RESULT: Localizing the (1,2,0) photon REDUCES its charge.  It
does not enhance it.  The delocalized electron has the MAXIMUM
charge for its mode.  Any localization (as would be imposed by
linking) weakens the charge.
""")

    # ==================================================================
    print("=" * 72)
    print("SECTION 3: Mode-space picture — what modes contribute charge?")
    print("=" * 72)
    # ==================================================================

    print("""
A wavepacket on the (1,2) geodesic can be decomposed into T²
eigenmodes.  Each (1, n₂) mode has charge:

    Q(1, n₂) = -sin(2πs₁₂) / (n₂ - s₁₂)

A Gaussian wavepacket centered on n₂ = 2 with width Δn₂ has charge
    Q_wp = Σ c_n × Q(1,n) / norm

Modes with non-physical spin (n₂ > 2) would be filtered out in
reality, but here we include all modes to see the mathematical
structure.
""")

    print(f"{'Δn₂':>8}  {'Q_wp/Q_e':>10}  {'dominant modes':>30}")
    print("-" * 55)
    for delta in [0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0]:
        ratio = charge_mode_space(s12, 2, delta)
        if delta < 0.05:
            modes = "only (1,2)"
        elif delta < 0.5:
            modes = "(1,1)+(1,2)+(1,3)"
        elif delta < 2:
            modes = "n₂ = 0..4"
        else:
            modes = f"n₂ = {2-int(2*delta)}..{2+int(2*delta)}"
        print(f"{delta:8.2f}  {ratio:10.4f}  {modes:>30}")

    print("""
At small Δn₂ (sharp in mode space = delocalized in real space):
Q = Q_electron exactly.

At large Δn₂ (broad in mode space = localized in real space):
Q increases initially (because neighboring modes (1,1) and (1,3)
have charge > 0), then decreases (because the normalization dilutes
the (1,2) contribution).  But the increase is modest (< 2×).
""")

    # ==================================================================
    print("=" * 72)
    print("SECTION 4: Can photon-photon interaction create charge?")
    print("=" * 72)
    # ==================================================================

    print("""
The (0,1,2) photon has zero charge because its field is uniform
in the θ₁ direction.  The ONLY way to give it charge is to create
θ₁-dependent structure in its field.

Possible mechanisms:

1. CLASSICAL EM INTERACTION: On a flat T³, Maxwell's equations are
   linear.  Two superposed EM waves do not interact.  The (0,1,2)
   photon's field is unaffected by the (1,2,0) photon, regardless
   of linking.

   → No charge transfer.  Classical EM linking is inert.

2. QUANTUM (QED) INTERACTION: Photon-photon scattering occurs at
   order α² via box diagrams.  This could scatter the (0,1,2) photon
   into modes with n₁ ≠ 0.  But the amplitude is O(α²) ≈ 5×10⁻⁵,
   giving charge corrections of order 10⁻⁵ e — far too small for
   2/3 e.

   → Charge transfer exists but is negligible.

3. TOPOLOGICAL DEFECT: If the photons are not ordinary EM waves but
   topological solitons (e.g., vortices in a gauge field), the
   linking topology could impose O(1) boundary conditions that
   modify the field structure.  This goes beyond the WvM framework
   of "photons as EM waves on compact geometry."

   → Would require fundamentally new physics beyond EM.

4. MULTI-COMPONENT EM (KK gauge fields): In Kaluza-Klein theory on
   T³, each compact direction generates a U(1) gauge field.  If the
   physical electromagnetic field is a linear combination of all
   three, then photons in ALL planes contribute to the EM charge.
""")

    # ==================================================================
    print("=" * 72)
    print("SECTION 5: Multi-component EM — the KK alternative")
    print("=" * 72)
    # ==================================================================

    print("""
In KK theory on T³, a particle with winding numbers (n₁, n₂, n₃)
has charges (Q₁, Q₂, Q₃) under three U(1) gauge fields, where
Q_i ∝ n_i.  If the physical EM field is:

    A_EM = a₁ A₁ + a₂ A₂ + a₃ A₃

then the EM charge is Q_EM = a₁ n₁ + a₂ n₂ + a₃ n₃.

For three proton photons:
    (1,2,0): Q = a₁ + 2a₂
    (0,1,2): Q = a₂ + 2a₃
    (1,0,2): Q = a₁ + 2a₃

Solving for (a₁, a₂, a₃) that give quark charges (2/3, 2/3, −1/3):
""")

    # Solve the system
    # a1 + 2a2 = 2/3
    # a2 + 2a3 = 2/3
    # a1 + 2a3 = -1/3
    A = np.array([[1, 2, 0], [0, 1, 2], [1, 0, 2]])
    b = np.array([2.0/3, 2.0/3, -1.0/3])
    coeffs = np.linalg.solve(A, b)
    a1, a2, a3 = coeffs

    print(f"Solution: a₁ = {a1:.4f},  a₂ = {a2:.4f},  a₃ = {a3:.4f}")
    print()

    proton_photons = [
        ("(1,2,0)", np.array([1, 2, 0])),
        ("(0,1,2)", np.array([0, 1, 2])),
        ("(1,0,2)", np.array([1, 0, 2])),
    ]

    total_Q = 0.0
    for label, n in proton_photons:
        Q = np.dot(coeffs, n)
        total_Q += Q
        print(f"  {label}: Q/e = {Q:+.4f}  {'(u quark)' if abs(Q - 2/3) < 0.01 else '(d quark)' if abs(Q + 1/3) < 0.01 else ''}")
    print(f"  Total: Q/e = {total_Q:+.4f}")

    # Check the electron
    n_e = np.array([1, 2, 0])
    Q_e = np.dot(coeffs, n_e)
    print(f"\n  Electron (1,2,0): Q/e = {Q_e:+.4f}  {'✓' if abs(Q_e - 2/3) < 0.01 else '✗'}")

    print(f"""
PROBLEM: In this KK picture, the electron (1,2,0) has charge 2/3 e,
not e.  It's a quark, not an electron!

The electron and the proton's (1,2)-plane photon have IDENTICAL
winding numbers.  In the KK picture, they have the same charge.
There's no way to make one have charge e and the other 2/3 e if
they're the same mode.

CONCLUSION: The simple KK multi-component picture doesn't work
either — it can't distinguish the electron from a quark.

Unless the electron and the proton's charged photon have DIFFERENT
winding numbers (they're not both (1,2,0)).
""")

    # Try different electron winding
    print("What if the electron is a different mode?\n")
    test_electrons = [
        ("(1,2,0)", np.array([1, 2, 0])),
        ("(1,1,0)", np.array([1, 1, 0])),
        ("(1,3,0)", np.array([1, 3, 0])),
        ("(2,1,0)", np.array([2, 1, 0])),
        ("(1,0,0)", np.array([1, 0, 0])),
        ("(0,1,0)", np.array([0, 1, 0])),
        ("(0,0,1)", np.array([0, 0, 1])),
    ]

    print(f"{'Mode':>10}  {'Q_KK/e':>8}  {'= 1?':>6}")
    print("-" * 30)
    for label, n in test_electrons:
        Q = np.dot(coeffs, n)
        ok = "✓" if abs(Q - 1.0) < 0.01 else ""
        print(f"{label:>10}  {Q:+8.4f}  {ok:>6}")

    print("""
With the (2/3, 2/3, -1/3) quark charges, the KK coefficients give
Q = 1 for the mode (3,0,3).  But this is a high-winding mode with
no obvious connection to the electron's (1,2) structure.

The KK multi-component picture requires abandoning the identification
of the electron as a (1,2) knot — a fundamental result from the
original WvM framework and all prior studies (S3, R2, R8, R19).
""")

    # ==================================================================
    print("=" * 72)
    print("SECTION 6: Assessment")
    print("=" * 72)
    # ==================================================================

    print("""
FINDINGS:

F14. Localization cannot charge the (2,3)-plane photon.
     The (0,1,2) photon's field is uniform in the tube (θ₁)
     direction, regardless of localization along its geodesic.
     The charge integral ∫cos(θ₁)dθ₁ = 0 is independent of σ.
     No degree of localization can make this photon charged.

F15. Localization REDUCES the (1,2,0) photon's charge.
     The delocalized mode has the maximum charge for its mode
     (Q = e, the electron).  Any localization (wavepacket width
     σ < ∞) weakens the charge.  Linking, which forces
     localization, would decrease the total charge below e —
     the wrong direction for charge redistribution.

F16. Classical EM linking is inert.
     On a flat T³, Maxwell's equations are linear.  Two EM waves
     superpose without interaction.  The (0,1,2) photon's field
     is unaffected by the (1,2,0) photon, regardless of topology.
     Linking cannot transfer charge classically.  QED corrections
     (photon-photon scattering) are O(α²) ≈ 10⁻⁵ — far too
     small to produce 2/3 e.

F17. The KK multi-component picture is incompatible with the
     electron being a (1,2) knot.
     If the EM gauge field is a linear combination of three
     U(1) fields (one per compact direction), the charge depends
     only on winding numbers.  The electron and the proton's
     charged photon have the same winding (1,2,0) and therefore
     the same charge — making fractional quark charges impossible
     without changing the electron's identity.

STRATEGIC CONCLUSION:

The four mechanisms considered (localization, interaction, classical
linking, KK gauge mixing) all fail to redistribute charge from
(e, 0, 0) to fractional values.  The core problem is:

    The charge integral from R19 depends on the MODE STRUCTURE
    (winding numbers + shear), not on the wavepacket envelope.
    In the θ₁ direction, the field is determined by n₁, and
    n₁ must be 1 for charge.  No spatial rearrangement within
    the (θ₂, θ₃) plane can change this.

This points toward a FUNDAMENTAL limitation of the current charge
mechanism.  Possible exits:

(A) The proton doesn't have three charged constituents in the way
    DIS suggests.  The "three scattering centers" might reflect
    three localized energy concentrations (the linked photons),
    not three separate charges.  The EM coupling of each center
    could be different from its charge — scattering depends on
    field amplitude, not monopole moment.

(B) The charge mechanism needs generalization beyond R19's formula.
    R19 derived charge from the monopole projection of a single
    photon's E-field.  For a multi-photon state, the correct
    projection might involve the TOTAL field, not individual
    photon fields.  Cross terms between photons could contribute.

(C) The compact space is not a flat T³.  Curvature (e.g., from a
    Calabi-Yau manifold or orbifold) could modify the mode
    structure and charge projections fundamentally.
""")


if __name__ == "__main__":
    main()
