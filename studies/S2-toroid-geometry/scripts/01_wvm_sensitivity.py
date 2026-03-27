#!/usr/bin/env python3
"""
01_wvm_sensitivity.py — Sensitivity of the WvM charge estimate to geometry.

The WvM charge derivation makes two geometric choices:
  1. Cavity volume V  (determines average field ⟨E⟩ from photon energy)
  2. Charge radius r_c (where ⟨E⟩ is equated to the Coulomb field)

Their specific choices — spherical cavity of diameter λ and charge
radius r̄ = λ/(4π) — yield q ≈ 0.91e.  But how sensitive is this?

General derivation:
  Energy density:  u = hc / (λ V)
  RMS E-field:     ⟨E⟩ = √(u / ε₀)  = √(hc / (ε₀ λ V))
  Coulomb match:   q / (4π ε₀ r_c²)  = ⟨E⟩
  ∴  q(V, r_c) = 4π ε₀ r_c² · √(hc / (ε₀ λ V))

This script sweeps:
  A. Cavity shape (sphere → torus with varying aspect ratio)
  B. Charge radius r_c
  C. Combined — for each shape, what r_c gives q = e exactly?
  D. E-B energy partition factor

Reference: theory.md §5.1, findings.md F6
"""

import math
import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib import constants as C
from lib.wvm import wvm_charge, q_over_e

lam = C.lambda_C
R_torus = lam / (2 * math.pi)     # major radius (photon orbit radius)
r_bar = C.r_bar                    # λ/(4π) — WvM's charge radius


def q_general(V, r_c):
    """
    Generalized WvM charge estimate.

    V    : cavity volume (m³)
    r_c  : radius at which Coulomb field is matched (m)

    Derivation (following WvM §3):
      Total energy U = hc/λ, split equally into E and B (E = cB for
      propagating wave): U_E = U/2.
      Electric energy density: W_E = U_E/V = hc/(2λV).
      Also W_E = ε₀E²/2, so E² = hc/(ε₀λV) = u_total/ε₀.
      Equate to Coulomb field at r_c: q/(4πε₀r_c²) = E.
    """
    u = C.h * C.c / (lam * V)
    E_rms = math.sqrt(u / C.eps0)
    return 4 * math.pi * C.eps0 * r_c**2 * E_rms


def V_sphere(radius):
    return (4 / 3) * math.pi * radius**3


def V_torus(R, a):
    """Volume of a torus with major radius R and tube radius a."""
    return 2 * math.pi**2 * R * a**2


def main():
    V_wvm = V_sphere(lam / 2)
    q_wvm = q_general(V_wvm, r_bar)

    print("=" * 72)
    print("WvM Charge Sensitivity Analysis")
    print("=" * 72)
    print()
    print("WvM baseline (sphere of diameter λ, charge at r̄ = λ/4π):")
    print(f"  λ_C   = {lam:.6e} m")
    print(f"  V_sph = {V_wvm:.6e} m³")
    print(f"  r̄     = {r_bar:.6e} m")
    print(f"  q     = {q_wvm:.6e} C")
    print(f"  q/e   = {q_wvm / C.e:.6f}")
    print(f"  (lib) = {q_over_e:.6f}")
    print()

    # ══════════════════════════════════════════════════════════════════════════
    # A. Vary cavity shape: sphere → torus with varying minor radius a
    # ══════════════════════════════════════════════════════════════════════════
    print("─" * 72)
    print("A. CAVITY SHAPE: Torus (major radius R = λ/2π) with varying tube")
    print(f"   radius a.  Charge radius fixed at r̄ = λ/(4π) = {r_bar:.3e} m.")
    print("─" * 72)
    print()
    print(f"  {'a/R':>8s}  {'a (m)':>12s}  {'V_torus':>12s}  {'V/V_sph':>8s}"
          f"  {'q/e':>8s}  {'Deficit':>8s}")

    a_over_R = np.linspace(0.05, 1.0, 20)
    for ratio in a_over_R:
        a = ratio * R_torus
        V = V_torus(R_torus, a)
        q = q_general(V, r_bar)
        qe = q / C.e
        deficit = (1 - qe) * 100
        marker = ""
        if abs(qe - 1.0) < 0.005:
            marker = " ← q ≈ e"
        elif abs(qe - q_over_e) < 0.005:
            marker = " ← WvM"
        print(f"  {ratio:>8.4f}  {a:>12.3e}  {V:>12.3e}  {V / V_wvm:>8.4f}"
              f"  {qe:>8.5f}  {deficit:>+7.2f}%{marker}")

    # What a/R gives q = e exactly?
    # q = e  ⟹  V = (4πε₀r̄²)² · hc/(ε₀λe²)
    # Easier: q ∝ 1/√V, so V_exact = V_wvm · (q_wvm/e)²
    V_exact = V_wvm * (q_wvm / C.e)**2
    a_exact = math.sqrt(V_exact / (2 * math.pi**2 * R_torus))
    print()
    print(f"  For q = e exactly with toroidal cavity:")
    print(f"    a/R = {a_exact / R_torus:.6f}")
    print(f"    a   = {a_exact:.6e} m")
    print(f"    V   = {V_exact:.6e} m³  ({V_exact / V_wvm:.4f} × V_sphere)")
    print()

    # ══════════════════════════════════════════════════════════════════════════
    # B. Vary charge radius r_c (keeping spherical cavity)
    # ══════════════════════════════════════════════════════════════════════════
    print("─" * 72)
    print("B. CHARGE RADIUS: Vary r_c from 0.5 r̄ to 2 r̄.")
    print(f"   Cavity fixed at WvM sphere (V = {V_wvm:.3e} m³).")
    print("─" * 72)
    print()
    print(f"  {'r_c / r̄':>8s}  {'r_c (m)':>12s}  {'q/e':>8s}  {'Deficit':>8s}")

    for frac in np.linspace(0.5, 2.0, 16):
        rc = frac * r_bar
        q = q_general(V_wvm, rc)
        qe = q / C.e
        deficit = (1 - qe) * 100
        marker = ""
        if abs(qe - 1.0) < 0.005:
            marker = " ← q ≈ e"
        elif abs(frac - 1.0) < 0.05:
            marker = " ← WvM"
        print(f"  {frac:>8.4f}  {rc:>12.3e}  {qe:>8.5f}  {deficit:>+7.2f}%{marker}")

    # What r_c gives q = e exactly?
    # q ∝ r_c², so r_c_exact = r_bar · √(e/q_wvm)
    rc_exact = r_bar * math.sqrt(C.e / q_wvm)
    print()
    print(f"  For q = e exactly with spherical cavity:")
    print(f"    r_c / r̄ = {rc_exact / r_bar:.6f}")
    print(f"    r_c     = {rc_exact:.6e} m")
    print(f"    r_c / R_torus = {rc_exact / R_torus:.6f}")
    print(f"    (WvM r̄ / R = {r_bar / R_torus:.6f} = 1/2 by construction)")
    print()

    # ══════════════════════════════════════════════════════════════════════════
    # C. Combined: for each cavity shape, what r_c gives q = e?
    # ══════════════════════════════════════════════════════════════════════════
    print("─" * 72)
    print("C. COMBINED: For each cavity, the r_c that gives q = e exactly.")
    print("─" * 72)
    print()
    print(f"  {'Cavity':>14s}  {'V (m³)':>12s}  {'r_c for q=e':>12s}"
          f"  {'r_c / r̄':>8s}  {'r_c / R':>8s}")

    cavities = [
        ("WvM sphere",     V_sphere(lam / 2)),
        ("Torus a/R=0.25", V_torus(R_torus, 0.25 * R_torus)),
        ("Torus a/R=0.50", V_torus(R_torus, 0.50 * R_torus)),
        ("Torus a/R=0.75", V_torus(R_torus, 0.75 * R_torus)),
        ("Torus a/R=1.00", V_torus(R_torus, 1.00 * R_torus)),
        ("Torus a=exact",  V_exact),
    ]

    for name, V in cavities:
        # q = 4πε₀ r_c² √(hc/(ε₀λV)) = e
        # r_c² = e / (4πε₀ √(hc/(ε₀λV)))
        u = C.h * C.c / (lam * V)
        E_rms = math.sqrt(u / C.eps0)
        rc_needed = math.sqrt(C.e / (4 * math.pi * C.eps0 * E_rms))
        print(f"  {name:>14s}  {V:>12.3e}  {rc_needed:>12.3e}"
              f"  {rc_needed / r_bar:>8.4f}  {rc_needed / R_torus:>8.4f}")

    print()

    # ══════════════════════════════════════════════════════════════════════════
    # D. Note on E-B energy partition
    # ══════════════════════════════════════════════════════════════════════════
    print("─" * 72)
    print("D. NOTE ON E-B ENERGY PARTITION")
    print("─" * 72)
    print()
    print("  WvM correctly handle E-B equipartition (§3 of paper):")
    print("    U_E = U_B = U/2    (E = cB for propagating wave)")
    print("    W_E = ε₀E²/2 = U_E/V = U/(2V)")
    print("    ∴ E² = U/(Vε₀) = u_total/ε₀")
    print()
    print("  The factors of 2 cancel: half the energy is electric, but the")
    print("  energy-density formula W_E = ε₀E²/2 also has a factor of ½.")
    print("  So the E-field is fully determined by the total energy and volume.")
    print("  There is no free parameter here to adjust.")
    print()

    # ══════════════════════════════════════════════════════════════════════════
    # Summary
    # ══════════════════════════════════════════════════════════════════════════
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print()
    print("q/e depends on two geometric choices: cavity volume V and charge")
    print("radius r_c.  (The E-B split is fixed by wave physics.)")
    print()
    print("The 9% deficit can be closed by:")
    print()
    print(f"  1. Shrinking V to {V_exact/V_wvm:.4f}× WvM sphere  (torus a/R = "
          f"{a_exact/R_torus:.4f}, degenerate)")
    print(f"  2. Increasing r_c to {rc_exact/r_bar:.4f}× r̄  (≈5% shift)")
    print(f"  3. Any combination of the above.")
    print()
    print("Key insight: a toroidal cavity makes q LARGER (stronger field),")
    print("not smaller.  The spherical approximation is the generous end.")
    print("The most sensitive parameter is r_c (q ∝ r_c²).  A ~5% shift")
    print("in where you evaluate the Coulomb field closes the entire deficit.")
    print()
    print("WvM acknowledged these approximations explicitly (§3 of paper):")
    print('  "It depends on the detailed distribution of the internal fields')
    print('   and also on the precise value we choose for the effective charge')
    print('   radius."')
    print()
    print("The 0.91e result is an order-of-magnitude success, not a precise")
    print("prediction.  Whether the deficit is 'real' (requiring sub-structure)")
    print("or an artifact of the geometric approximation remains open.")
    print()


if __name__ == "__main__":
    main()
