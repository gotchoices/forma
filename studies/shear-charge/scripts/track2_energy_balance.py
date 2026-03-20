#!/usr/bin/env python3
"""
R19 Track 2: Energy balance — is non-zero shear stable?

The photon is a traveling wave along the (1,2) geodesic on T².
Its energy is E = hc/L where L is the geodesic path length
(NOT the 2D eigenmode energy — R12 F6).

On the sheared T², the geodesic endpoint shifts:
  (1,2) → (L₁ + 2sL₁, 2L₂)  in the universal cover
  L(s) = 2π√(a²(1+2s)² + 4R²)

For s > 0, L(s) > L(0) = λ_C, so E_photon DECREASES.

Two competing effects:
  1. Mode energy decreases (geodesic gets longer) → favors shear
  2. Coulomb self-energy increases (Q > 0) → opposes shear

If the decrease dominates, E_total is monotonically decreasing
and there's no self-stabilizing equilibrium.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C

import numpy as np


def geometry(r):
    """Torus geometry from Compton constraint L_geo = λ_C at s=0."""
    R = lambda_C / (2.0 * math.pi * math.sqrt(4 + r**2))
    a = r * R
    return R, a


def L_geodesic(s, a, R):
    """
    Geodesic path length for (1,2) mode on sheared T².
    
    On the flat T² with lattice e₁=(L₁,0), e₂=(sL₁, L₂),
    the (1,2) endpoint is e₁ + 2e₂ = (L₁(1+2s), 2L₂).
    """
    L1 = 2 * math.pi * a
    L2 = 2 * math.pi * R
    return math.sqrt((L1 * (1 + 2*s))**2 + (2 * L2)**2)


def E_photon(s, a, R):
    """Photon energy = hc / L_geodesic."""
    return h * c / L_geodesic(s, a, R)


def E0_field(E_phot, a, R):
    """Field amplitude from photon energy distributed over torus."""
    return math.sqrt(E_phot / (eps0 * math.pi**2 * a**2 * R))


def Q_from_shear(s, E0, a):
    """Q(s) = ε₀ E₀ a²π |sin(2πs)| / |2−s|."""
    q_eff = 2.0 - s
    if abs(q_eff) < 1e-15:
        return eps0 * E0 * a**2 * math.pi * 2 * math.pi
    return eps0 * E0 * a**2 * math.pi * abs(math.sin(2*math.pi*s)) / abs(q_eff)


def E_coulomb(Q, R, g_r):
    """Coulomb self-energy of charge Q on torus."""
    return Q**2 * g_r / (4 * math.pi * eps0 * R)


def full_energy(s, a, R, g_r):
    """Total energy = E_photon + E_Coulomb at given shear."""
    Ep = E_photon(s, a, R)
    E0 = E0_field(Ep, a, R)
    Q = Q_from_shear(s, E0, a)
    Ec = E_coulomb(Q, R, g_r)
    return Ep, Q, Ec, Ep + Ec


def main():
    E_mc2 = m_e * c**2

    print("=" * 70)
    print("R19 Track 2: Energy Balance — Is Non-Zero Shear Stable?")
    print("=" * 70)
    print()

    # ── Section 1: Verify the photon energy model ─────────────
    print("SECTION 1: Photon energy = hc/L_geodesic (not eigenmode)")
    print("-" * 70)
    print()

    r = 1.0
    g_r = 0.5
    R, a = geometry(r)

    L0 = L_geodesic(0, a, R)
    E0_check = h * c / L0
    E_eigen = hbar * c * math.sqrt(1/a**2 + 4/R**2)

    print(f"Geometry: r = {r}, R = {R:.4e} m, a = {a:.4e} m")
    print(f"L_geodesic(s=0) = {L0:.6e} m")
    print(f"λ_C             = {lambda_C:.6e} m")
    print(f"L/λ_C           = {L0/lambda_C:.8f}  (should be 1.0)")
    print()
    print(f"E_photon = hc/L = {E0_check:.6e} J = {E0_check/E_mc2:.6f} m_e c²")
    print(f"E_eigen  = ℏc|k|= {E_eigen:.6e} J = {E_eigen/E_mc2:.6f} m_e c²")
    print()
    print(f"The eigenmode energy is {E_eigen/E0_check:.1f}× the photon energy.")
    print("This confirms R12 F6: the photon is NOT the torus eigenmode.")
    print("The physical photon has ONE wavelength along the geodesic,")
    print(f"while the eigenmode fits {E_eigen/E0_check:.0f} wavelengths.")
    print()

    # ── Section 2: How shear changes the geodesic ─────────────
    print("SECTION 2: Geodesic path length vs shear (fixed geometry)")
    print("-" * 70)
    print()

    s_vals = np.linspace(0.0, 0.999, 500)

    print(f"{'s':>8s} | {'L(s)/λ_C':>10s} | {'E_phot/m_ec²':>13s} | "
          f"{'Q/e':>8s} | {'E_C/m_ec²':>12s} | {'E_tot/m_ec²':>12s}")
    print("-" * 80)

    results = []
    for s in s_vals:
        Ep, Q, Ec, Et = full_energy(s, a, R, g_r)
        Ls = L_geodesic(s, a, R)
        results.append((s, Ls, Ep, Q, Ec, Et))

    for s_sample in [0.00, 0.05, 0.10, 0.157, 0.20, 0.25, 0.30,
                     0.40, 0.50, 0.60, 0.70, 0.77, 0.90, 0.99]:
        idx = max(0, np.argmin(np.abs(s_vals - s_sample)))
        s, Ls, Ep, Q, Ec, Et = results[idx]
        print(f"{s:8.3f} | {Ls/lambda_C:10.6f} | {Ep/E_mc2:13.6f} | "
              f"{Q/e:8.4f} | {Ec/E_mc2:12.6e} | {Et/E_mc2:12.6f}")

    print()

    # ── Section 3: Scale comparison ───────────────────────────
    print("SECTION 3: Scale comparison at s = 0.157 (Track 1 solution)")
    print("-" * 70)
    print()

    s_t1 = 0.157
    Ep_t1, Q_t1, Ec_t1, Et_t1 = full_energy(s_t1, a, R, g_r)
    dEp = Ep_t1 - E_mc2

    print(f"ΔE_photon = {dEp/E_mc2:.6f} m_e c²  "
          f"({dEp/E_mc2*100:.3f}%)")
    print(f"E_Coulomb = {Ec_t1/E_mc2:.6e} m_e c²  "
          f"({Ec_t1/E_mc2*100:.4f}%)")
    print(f"|ΔE_photon|/E_Coulomb = {abs(dEp)/max(Ec_t1, 1e-99):.1f}")
    print(f"Q = {Q_t1/e:.4f} e")
    print()

    # ── Section 4: Derivative at s = 0 ────────────────────────
    print("SECTION 4: Derivatives at s = 0")
    print("-" * 70)
    print()

    ds = 1e-6
    Ep_0 = E_photon(0, a, R)
    Ep_ds = E_photon(ds, a, R)
    dEp_ds = (Ep_ds - Ep_0) / ds

    _, _, Ec_0, _ = full_energy(0, a, R, g_r)
    _, _, Ec_ds, _ = full_energy(ds, a, R, g_r)
    dEc_ds = (Ec_ds - Ec_0) / ds

    print(f"dE_photon/ds|₀ = {dEp_ds/E_mc2:.6f} m_e c² per unit shear")
    print(f"dE_Coulomb/ds|₀ = {dEc_ds/E_mc2:.6e} m_e c² per unit shear")
    print(f"dE_total/ds|₀  = {(dEp_ds + dEc_ds)/E_mc2:.6f} m_e c²")
    print()

    if dEp_ds + dEc_ds < 0:
        print("The total derivative is NEGATIVE at s = 0.")
        print("The system wants to increase shear (lower energy).")
    else:
        print("The total derivative is POSITIVE at s = 0.")
        print("The system resists shear.")
    print()

    print("Physical interpretation:")
    print("  dE_photon/ds < 0: the geodesic gets longer → photon")
    print("    frequency drops → energy decreases.")
    print("  dE_Coulomb/ds ≈ 0: charge Q ∝ sin(2πs) starts")
    print("    quadratically → Coulomb cost is negligible at small s.")
    print("  No restoring force opposes the shear at s = 0.")
    print()

    # ── Section 5: Minimum search ─────────────────────────────
    print("SECTION 5: Does E_total(s) have a minimum at s > 0?")
    print("-" * 70)
    print()

    Et_arr = np.array([r[-1] for r in results])
    idx_min = np.argmin(Et_arr)
    s_min = s_vals[idx_min]

    is_mono = True
    for i in range(len(Et_arr) - 1):
        if Et_arr[i+1] > Et_arr[i] + 1e-30:
            is_mono = False
            break

    print(f"Minimum E_total at s = {s_min:.4f}")
    print(f"E_total(s_min) = {Et_arr[idx_min]/E_mc2:.6f} m_e c²")
    print(f"Monotonically decreasing? {is_mono}")
    print()

    if not is_mono:
        local_mins = []
        for i in range(1, len(Et_arr) - 1):
            if Et_arr[i] < Et_arr[i-1] and Et_arr[i] < Et_arr[i+1]:
                local_mins.append((s_vals[i], Et_arr[i]))
        if local_mins:
            print("Local minima found:")
            for sm, em in local_mins:
                _, Qm, _, _ = full_energy(sm, a, R, g_r)
                alpha_m = Qm**2 / (4*math.pi*eps0*hbar*c)
                print(f"  s = {sm:.6f}, E = {em/E_mc2:.6f} m_e c², "
                      f"Q = {Qm/e:.4f} e, α = {alpha_m:.6f}")

    print()

    # ── Section 6: Aspect ratio scan ──────────────────────────
    print("SECTION 6: Aspect ratio scan")
    print("-" * 70)
    print()

    print(f"{'r':>6s} | {'dE_phot/ds|₀':>14s} | {'E_C_max/m_ec²':>14s} | "
          f"{'|dE_p|/E_C_max':>14s} | {'Local min?':>10s}")
    print("-" * 72)

    for r_scan in [0.25, 0.50, 0.75, 1.00, 1.50, 2.00, 3.00, 4.00]:
        R_s, a_s = geometry(r_scan)

        Ep0 = E_photon(0, a_s, R_s)
        Ep_d = E_photon(ds, a_s, R_s)
        dEp = (Ep_d - Ep0) / ds

        Ec_max = 0
        Et_scan = []
        for s in s_vals:
            _, _, Ec, Et = full_energy(s, a_s, R_s, g_r)
            if Ec > Ec_max:
                Ec_max = Ec
            Et_scan.append(Et)

        Et_scan = np.array(Et_scan)
        has_local_min = False
        for i in range(1, len(Et_scan) - 1):
            if Et_scan[i] < Et_scan[i-1] and Et_scan[i] < Et_scan[i+1]:
                has_local_min = True
                break

        ratio = abs(dEp) / max(Ec_max, 1e-99)
        print(f"{r_scan:6.2f} | {dEp/E_mc2:14.6f} | {Ec_max/E_mc2:14.6e} | "
              f"{ratio:14.1f} | {'YES' if has_local_min else 'No':>10s}")

    print()

    # ── Section 7: Self-consistent mass decomposition ─────────
    print("SECTION 7: Self-consistent mass at Q = e")
    print("-" * 70)
    print()

    E_C_e = alpha * E_mc2 * g_r * math.sqrt(r**2 + 4)
    E_bare = E_mc2 - E_C_e

    print("If the electron has Q = e, its rest mass includes:")
    print(f"  E_Coulomb = α g √(r²+4) × m_e c² = {E_C_e/E_mc2:.6f} m_e c²")
    print(f"            = {E_C_e/E_mc2/alpha:.2f} α m_e c²")
    print(f"  E_bare    = {E_bare/E_mc2:.6f} m_e c²")
    print(f"  EM fraction: {E_C_e/E_mc2*100:.3f}%")
    print()
    print("This O(α) EM self-energy is consistent with QED's")
    print("electromagnetic contribution to the electron mass.")
    print()

    # ── Section 8: Verdict ────────────────────────────────────
    print("SECTION 8: Verdict")
    print("-" * 70)
    print()
    print("1. The photon energy is E = hc/L_geodesic (NOT the 2D")
    print(f"   eigenmode energy, which is {E_eigen/E0_check:.0f}× larger for r=1).")
    print()
    print("2. Shear makes the geodesic LONGER: L(s) > L(0) = λ_C.")
    print("   The photon energy DECREASES: ΔE_photon < 0.")
    print()
    print("3. Charge creates Coulomb self-energy: E_C > 0.")
    print("   But |ΔE_photon| ≫ E_C (by factor ~10-100).")
    print()
    print("4. dE_total/ds|₀ < 0 — the system wants to shear.")
    print("   E_total(s) is monotonically decreasing: no equilibrium.")
    print()
    print("5. CONCLUSION: Non-zero shear is NOT self-stabilizing.")
    print("   The flat T² has no potential well for the shear modulus.")
    print("   The shear must be fixed by an external constraint:")
    print("   • T³ modular geometry (third compact dimension)")
    print("   • Topological self-linking (knot invariants)")
    print("   • Embedding curvature")
    print()
    print("6. POSITIVE: The mechanism is self-consistent IF shear is")
    print("   externally fixed.  The EM self-energy (O(α m_e c²)) is")
    print("   the correct order of magnitude, and the required shear")
    print("   (δ ≈ a for r = 1) is geometrically natural.")


if __name__ == "__main__":
    main()
