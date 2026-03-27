#!/usr/bin/env python3
"""
R30 Track 4: The r → ∞ limit — T² degenerating to T¹.

As the aspect ratio r = L_tube/L_ring → ∞, the tube gets infinitely
long and its modes drop to zero energy.  Does the charge mechanism
survive?  Is there a phase transition?  Where does r_p = 8.906 sit
in the landscape?

Also examines r → r_crit (lower bound): does charge vanish
discontinuously?
"""

import sys, os, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6 import (
    alpha_kk, solve_shear_for_alpha, mu_12,
    hbar_c_MeV_fm, M_E_MEV, M_P_MEV, ALPHA,
)

TWO_PI_HC = 2 * math.pi * hbar_c_MeV_fm


def solve_shear_extended(r, alpha_target=ALPHA):
    """Extended shear solver that works at large r (small s)."""
    from scipy.optimize import brentq
    s_scan = np.concatenate([
        np.linspace(1e-8, 1e-4, 500),
        np.linspace(1e-4, 0.01, 500),
        np.linspace(0.01, 0.49, 2000),
    ])
    a_scan = [alpha_kk(r, s) for s in s_scan]
    for i in range(len(s_scan) - 1):
        if (a_scan[i] - alpha_target) * (a_scan[i + 1] - alpha_target) < 0:
            return brentq(lambda s: alpha_kk(r, s) - alpha_target,
                          s_scan[i], s_scan[i + 1])
    return None


def t2_properties(r, mass, label=""):
    """Compute T² properties at given r for a particle of given mass."""
    s = solve_shear_extended(r)
    if s is None:
        return None

    mu = mu_12(r, s)
    E0 = mass / mu
    L_ring = TWO_PI_HC / E0
    L_tube = r * L_ring

    # Energy contributions from tube vs ring
    E_tube = TWO_PI_HC / L_tube  # = E0/r = mass/(mu*r)
    E_ring = TWO_PI_HC * (2 - s) / L_ring  # = E0*(2-s)

    # Fraction of energy from tube
    E_tube_sq = (1.0 / r)**2
    E_ring_sq = (2 - s)**2
    tube_frac = E_tube_sq / (E_tube_sq + E_ring_sq)

    # α at this (r, s) — should be 1/137
    a = alpha_kk(r, s)

    return {
        'r': r, 's': s, 'mu': mu, 'E0': E0,
        'L_ring': L_ring, 'L_tube': L_tube,
        'E_tube': E_tube, 'E_ring': E_ring,
        'tube_frac': tube_frac,
        'alpha': a,
    }


print("=" * 72)
print("R30 TRACK 4: THE r → ∞ LIMIT")
print("=" * 72)


# ── Section 1: Sweep r for electron ─────────────────────────────

print("\n\n── Section 1: Electron T² properties vs r ──\n")
print(f"  {'r':>8s} {'s':>10s} {'μ₁₂':>8s} {'L_tube (fm)':>14s}"
      f" {'L_ring (fm)':>14s} {'tube E%':>8s} {'α':>10s}")
print(f"  {'─'*76}")

r_values = [0.3, 0.5, 1.0, 2.0, 3.0, 5.0, 6.6, 8.906, 10, 20, 50,
            100, 500, 1000]

for r in r_values:
    p = t2_properties(r, M_E_MEV)
    if p is None:
        print(f"  {r:8.1f}  NO SOLUTION (r < r_crit)")
        continue
    marker = " ← r_e default" if abs(r - 6.6) < 0.01 else ""
    marker = " ← r_p pinned" if abs(r - 8.906) < 0.01 else marker
    print(f"  {r:8.3f} {p['s']:10.6f} {p['mu']:8.4f} {p['L_tube']:14.1f}"
          f" {p['L_ring']:14.1f} {p['tube_frac']*100:7.3f}%"
          f" {p['alpha']:10.7f}{marker}")


# ── Section 2: Find r_crit ──────────────────────────────────────

print("\n\n── Section 2: Critical r (lower bound) ──\n")

r_crit = None
for r_test in np.arange(0.01, 1.0, 0.001):
    s = solve_shear_for_alpha(r_test)
    if s is not None:
        r_crit = r_test
        break

print(f"  r_crit ≈ {r_crit:.3f} (smallest r with α = 1/137 solution)")
print()

# Properties near r_crit
for r in [r_crit, r_crit + 0.01, r_crit + 0.1, 0.5, 1.0]:
    p = t2_properties(r, M_E_MEV)
    if p:
        print(f"  r = {r:.3f}: s = {p['s']:.6f}, "
              f"tube fraction = {p['tube_frac']*100:.1f}%, "
              f"L_tube = {p['L_tube']:.0f} fm")


# ── Section 3: Asymptotic behavior ──────────────────────────────

print("\n\n── Section 3: Large-r asymptotics ──\n")

print("  As r → ∞:")
print("    s → 0 (shear vanishes)")
print("    But r²s² → const (product stays finite)")
print("    μ₁₂ → 2 (ring-dominated)")
print("    E₀ → m/2")
print("    L_ring → 2 × Compton wavelength")
print("    L_tube → ∞")
print("    Tube energy fraction → 0")
print()
print("  Verify numerically:")
print(f"  {'r':>8s} {'r²s²':>12s} {'s×r':>10s} {'μ₁₂':>8s} {'E₀/m':>8s}")
print(f"  {'─'*50}")

for r in [1, 5, 10, 50, 100, 500, 1000]:
    p = t2_properties(r, M_E_MEV)
    if p:
        print(f"  {r:8d} {r**2 * p['s']**2:12.6f} {p['s']*r:10.6f}"
              f" {p['mu']:8.5f} {p['E0']/M_E_MEV:8.5f}")


# ── Section 4: Does charge survive at large r? ──────────────────

print("\n\n── Section 4: Charge mechanism at extreme r ──\n")

print("  The α formula: α = r² μ sin²(2πs) / [4π(2−s)²]")
print("  We CONSTRAIN α = 1/137 at every r.")
print("  So charge is always e — by construction.")
print()
print("  But the MECHANISM differs:")
print("  - Small r: large shear s, strong geometric twist")
print("  - Large r: tiny shear s ∝ 1/r, compensated by r²")
print()
print("  The charge is topological (integer-valued): it's either")
print("  e or 0.  There is no smooth transition.  As long as the")
print("  (1,2) geodesic exists and the metric has nonzero shear,")
print("  the charge is exactly e.")
print()
print("  This explains why r is free: the charge mechanism depends")
print("  on the TOPOLOGY (tube wraps once, ring wraps twice) and the")
print("  EXISTENCE of shear, not on its magnitude.  Any r > r_crit")
print("  produces a valid solution.")


# ── Section 5: Mode spectrum vs r ────────────────────────────────

print("\n\n── Section 5: Mode spectrum evolution with r ──\n")
print("  First 10 modes on electron T² at selected r values:")
print()

for r in [1.0, 6.6, 50.0, 500.0]:
    p = t2_properties(r, M_E_MEV)
    if p is None:
        continue

    s = p['s']
    E0 = p['E0']
    L_ring = p['L_ring']
    L_tube = p['L_tube']

    modes = []
    for n1 in range(-5, 6):
        for n2 in range(-5, 6):
            if n1 == 0 and n2 == 0:
                continue
            E = E0 * math.sqrt((n1 / r)**2 + (n2 - n1 * s)**2)
            Q = -n1
            spin = abs(n1) % 2
            modes.append((E, n1, n2, Q, spin))

    modes.sort()

    print(f"  r = {r:.1f} (s = {s:.6f}):")
    print(f"    {'Mode':>8s} {'E (MeV)':>10s} {'E/m_e':>8s} {'Q':>3s} {'spin':>5s}")
    for E, n1, n2, Q, spin in modes[:10]:
        print(f"    ({n1:+d},{n2:+d}) {E:10.4f} {E/M_E_MEV:8.3f} {Q:+2d}"
              f" {'½' if spin==1 else '0':>5s}")
    print()


# ── Section 6: Where does r_p = 8.906 sit? ──────────────────────

print("\n── Section 6: Is r_p = 8.906 special? ──\n")

# Check various properties at r_p
p = t2_properties(8.906, M_P_MEV, "proton")
print(f"  Proton at r_p = 8.906:")
print(f"    s = {p['s']:.6f}")
print(f"    Tube energy fraction: {p['tube_frac']*100:.2f}%")
print(f"    L_tube = {p['L_tube']:.2f} fm")
print(f"    L_ring = {p['L_ring']:.4f} fm")
print(f"    L_tube / L_ring = {p['L_tube']/p['L_ring']:.3f} (= r)")
print()

# Check if tube fraction has any special value
print("  Tube energy fraction vs r (proton sheet):")
print(f"    {'r':>6s} {'tube %':>8s} {'1/r²':>10s}")
print(f"    {'─'*28}")
for r in [1.0, 2.0, 4.0, 6.0, 8.906, 10, 20, 50]:
    pp = t2_properties(r, M_P_MEV)
    if pp:
        print(f"    {r:6.2f} {pp['tube_frac']*100:7.3f}% {1/r**2:10.6f}")

print()
print("  The tube fraction is approximately 1/(4r²) for large r.")
print(f"  At r_p = 8.906: tube contributes {p['tube_frac']*100:.2f}% of E².")
print(f"  The proton is 99.7% ring-dominated — but the tube is still")
print(f"  essential for charge and spin.")
print()

# Is r_p pinned by physics or arbitrary?
print("  r_p = 8.906 was pinned by the neutron mass (R27 Track 2).")
print("  It is NOT at any geometric threshold (r_crit, golden ratio, etc).")
print("  Its value comes from the cross-shear σ_ep needed to shift the")
print("  neutron mode to 939.565 MeV.  This is a physical constraint,")
print("  not a geometric one.")


# ── Section 7: The tube as a topological necessity ───────────────

print("\n\n── Section 7: The tube as topological necessity ──\n")

print("  At r = 1000 (extreme case):")
pp = t2_properties(1000, M_E_MEV)
print(f"    s = {pp['s']:.8f} (almost zero)")
print(f"    Tube energy fraction: {pp['tube_frac']*100:.5f}%")
print(f"    L_tube = {pp['L_tube']/1e6:.1f} million fm = {pp['L_tube']/1e13:.1f} mm")
print(f"    The tube is macroscopic!")
print()
print("  Yet the electron still has:")
print(f"    Charge = −e (exact, from topology)")
print(f"    Spin = ½ (from n₁ = 1, odd)")
print(f"    Mass = {M_E_MEV} MeV (exact, by construction)")
print()
print("  The tube at r = 1000 contributes < 0.00003% of the energy.")
print("  It is energetically irrelevant but topologically essential.")
print("  Removing it (going to T¹) would kill charge and spin.")
print()
print("  This is the resolution of the 'too many dimensions' question:")
print("  the tube dimension CAN be arbitrarily large (even macroscopic),")
print("  contributing negligible energy, but it MUST EXIST for charge")
print("  and spin to work.  It is a topological degree of freedom,")
print("  not an energetic one.")


# ── Summary ──────────────────────────────────────────────────────

print("\n\n── Summary ──\n")
print("  1. No phase transition: charge works for ALL r > r_crit ≈ 0.26.")
print("     The (1,2) geodesic exists at every r and carries charge e.")
print()
print("  2. At large r, s → 0 as 1/r, tube fraction → 0 as 1/r².")
print("     The tube becomes energetically irrelevant but topologically")
print("     essential (provides charge and spin).")
print()
print("  3. r is free because the charge mechanism is topological:")
print("     it depends on the EXISTENCE of shear (nonzero s), not its")
print("     magnitude.  The α formula r²s² ≈ const ensures charge = e")
print("     at every r.")
print()
print("  4. r_p = 8.906 is pinned by the neutron mass, not by geometry.")
print("     The proton tube contributes 0.3% of E² — it is 99.7%")
print("     ring-dominated but still structurally necessary.")
print()
print("  5. The tube dimension is a topological necessity, not an")
print("     energetic one.  This is why it can be 'invisible' in")
print("     scattering experiments (< 0.01% energy contribution at")
print("     large r) yet essential for the model's predictions.")
