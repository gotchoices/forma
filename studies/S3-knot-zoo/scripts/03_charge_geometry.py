#!/usr/bin/env python3
"""
03_charge_geometry.py — Explore charge from torus geometry.

F3 showed that varying the torus knot winding number does NOT produce
fractional charges: only (1,2) gives nonzero charge. But charge
depends continuously on the torus aspect ratio a/R:

    q = e / (a/R · √(πα))     [from S2-toroid-geometry study F6]

So different geometries (different a/R values) produce different
charges. This script explores whether the electron, up quark, and
down quark can all be (1,2) knots on tori with different a/R.

Two sub-models are tested:
  A. Shared dimension — all particles on one compact dimension (same a)
  B. Two dimensions — leptons and quarks on separate compact dimensions

Bears on theory.md P2 (charge), findings F3, F4.
"""

import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib import constants as C


def ar_for_charge(q_frac):
    """
    Required a/R to produce charge q = q_frac * e.
    From q = e * (1/√(πα)) / (a/R), solving for a/R:
        a/R = 1 / (q_frac * √(πα))
    """
    return 1.0 / (q_frac * math.sqrt(math.pi * C.alpha))


def compton_R(mass_MeV):
    """
    WvM orbital radius R = λ_C / (4π) = ℏ / (2mc).
    Input mass in MeV/c².
    """
    mass_kg = mass_MeV * 1e6 * C.e / C.c**2
    lambda_C = C.h / (mass_kg * C.c)
    return lambda_C / (4 * math.pi)


# Experimental values (MeV/c²)
m_e = 0.51099895
m_u = 2.16      # up quark current mass (PDG 2024 central value)
m_d = 4.67      # down quark current mass (PDG 2024 central value)
m_mu = 105.6584
m_tau = 1776.86
m_c = 1270.0
m_s = 93.4
m_t = 172760.0
m_b = 4180.0


def main():
    ar_e = ar_for_charge(1.0)

    print("=" * 78)
    print("Charge from Torus Geometry")
    print("=" * 78)
    print()
    print("  Formula: q/e = 1/(√(πα) · a/R)   →   a/R = 1/(q_frac · √(πα))")
    print(f"  √(πα) = {math.sqrt(math.pi * C.alpha):.6f}")
    print(f"  1/√(πα) = {1/math.sqrt(math.pi * C.alpha):.4f}")
    print()

    print("─" * 78)
    print("  Required a/R for each charge quantum:")
    print("─" * 78)
    charges = [
        ("Electron",     1.0,   "e"),
        ("Up quark",     2/3,   "2e/3"),
        ("Down quark",   1/3,   "e/3"),
        ("Neutrino",     0.0,   "0"),
    ]

    for name, q_frac, label in charges:
        if q_frac == 0:
            print(f"  {name:15s}  q = {label:5s}  a/R = ∞ (no finite geometry)")
        else:
            ar = ar_for_charge(q_frac)
            print(f"  {name:15s}  q = {label:5s}  a/R = {ar:.4f}"
                  f"  = {1/q_frac:.0f}/√(πα)"
                  f"  ({ar/ar_e:.1f}× electron)")
    print()

    # ──────────────────────────────────────────────────────────────────
    print("=" * 78)
    print("Model A: Shared Compact Dimension (same a for all particles)")
    print("=" * 78)
    print()
    print("  If all particles share one compact dimension with tube radius a,")
    print("  then a/R varies because R varies (R ∝ 1/m). Predictions:")
    print()

    ar_u = ar_for_charge(2/3)
    ar_d = ar_for_charge(1/3)

    R_e = compton_R(m_e)
    a_shared = ar_e * R_e

    pred_R_u = a_shared / ar_u
    pred_R_d = a_shared / ar_d

    pred_m_u = C.hbar / (2 * pred_R_u * (m_e * 1e6 * C.e / C.c**2) / (C.hbar / (2 * R_e * C.c)) * C.c)

    pred_m_u_MeV = m_e * (ar_u / ar_e)
    pred_m_d_MeV = m_e * (ar_d / ar_e)

    print(f"  Electron: a/R = {ar_e:.4f},  R = {R_e:.4e} m,  a = {a_shared:.4e} m")
    print(f"  Up quark: a/R = {ar_u:.4f},  R = {a_shared/ar_u:.4e} m")
    print(f"  Down quark: a/R = {ar_d:.4f},  R = {a_shared/ar_d:.4e} m")
    print()

    print("  Mass predictions (from R = ℏ/(2mc), same a):")
    print()
    print(f"    m_u/m_e = (a/R_u)/(a/R_e) = {ar_u/ar_e:.4f}")
    print(f"    Predicted m_u = {pred_m_u_MeV:.4f} MeV")
    print(f"    Experimental m_u = {m_u} MeV")
    print(f"    Ratio pred/exp = {pred_m_u_MeV/m_u:.3f}")
    print()
    print(f"    m_d/m_e = (a/R_d)/(a/R_e) = {ar_d/ar_e:.4f}")
    print(f"    Predicted m_d = {pred_m_d_MeV:.4f} MeV")
    print(f"    Experimental m_d = {m_d} MeV")
    print(f"    Ratio pred/exp = {pred_m_d_MeV/m_d:.3f}")
    print()
    print(f"    m_d/m_u predicted = {ar_d/ar_u:.4f}")
    print(f"    m_d/m_u experimental = {m_d/m_u:.4f}")
    print()

    print("  Verdict: absolute masses are off by ~3×, but the ratio")
    print("  m_d/m_u = 2.000 vs experimental ≈ {:.1f} is close.".format(m_d/m_u))
    print()

    # ──────────────────────────────────────────────────────────────────
    print("=" * 78)
    print("Model B: Two Compact Dimensions (leptons vs quarks)")
    print("=" * 78)
    print()
    print("  Quarks share a compact dimension with tube radius a_q ≠ a_e.")
    print("  The electron has its own dimension. Only quark mass ratios")
    print("  are predicted (not absolute masses).")
    print()

    print("  Within the quark dimension:")
    print(f"    a/R_u = {ar_u:.4f}  (for charge 2e/3)")
    print(f"    a/R_d = {ar_d:.4f}  (for charge e/3)")
    print(f"    R_u/R_d = (a/R_d)/(a/R_u) = {ar_d/ar_u:.4f}")
    print(f"    → m_d/m_u = R_u/R_d = {ar_d/ar_u:.4f}")
    print(f"    Experimental m_d/m_u = {m_d/m_u:.4f}")
    print(f"    Agreement: {abs(1 - (ar_d/ar_u)/(m_d/m_u))*100:.1f}% off")
    print()

    print("  Cross-generation consistency test:")
    print("  If the same quark dimension governs all generations,")
    print("  the mass ratio within each generation should be the same:")
    print()
    print(f"    Gen 1: m_d/m_u = {m_d/m_u:.3f}  (predicted: 2.000)")
    print(f"    Gen 2: m_s/m_c = {m_s/m_c:.3f}  (predicted: 2.000)")
    print(f"    Gen 3: m_b/m_t = {m_b/m_t:.5f}  (predicted: 2.000)")
    print()

    # ──────────────────────────────────────────────────────────────────
    print("=" * 78)
    print("Extended Table: All Charged Fermions")
    print("=" * 78)
    print()
    print(f"  {'Particle':12s}  {'Charge':>6s}  {'Mass MeV':>10s}  "
          f"{'a/R needed':>10s}  {'R (m)':>12s}")
    print("  " + "─" * 60)

    particles = [
        ("Electron",  1.0,   m_e),
        ("Muon",      1.0,   m_mu),
        ("Tau",       1.0,   m_tau),
        ("Up",        2/3,   m_u),
        ("Down",      1/3,   m_d),
        ("Charm",     2/3,   m_c),
        ("Strange",   1/3,   m_s),
        ("Top",       2/3,   m_t),
        ("Bottom",    1/3,   m_b),
    ]

    for name, q_frac, mass in particles:
        ar = ar_for_charge(q_frac)
        R = compton_R(mass)
        print(f"  {name:12s}  {q_frac:>6.3f}  {mass:>10.2f}  "
              f"{ar:>10.4f}  {R:>12.4e}")

    print()
    print("  Note: All particles with the same charge need the SAME a/R.")
    print("  All electrons, muons, and taus need a/R = {:.4f}.".format(ar_e))
    print("  All +2/3 quarks need a/R = {:.4f}.".format(ar_u))
    print("  All -1/3 quarks need a/R = {:.4f}.".format(ar_d))
    print()
    print("  Under the compact-dimension model, generations are harmonics")
    print("  (different photon energies on the same path), NOT different")
    print("  geometries. So the same a/R for same charge is consistent.")
    print()

    # ──────────────────────────────────────────────────────────────────
    print("=" * 78)
    print("Key Numbers Summary")
    print("=" * 78)
    print()
    print(f"  a/R for q = e  :  1/√(πα)     = {ar_e:.4f}")
    print(f"  a/R for q = 2e/3: (3/2)/√(πα)  = {ar_u:.4f}  (= 1.5 × {ar_e:.2f})")
    print(f"  a/R for q = e/3 : 3/√(πα)      = {ar_d:.4f}  (= 3.0 × {ar_e:.2f})")
    print()
    print(f"  Ratio pattern: a/R scales as 1/q_frac")
    print(f"    electron : up : down  =  1 : 3/2 : 3")
    print()
    print("  Mass ratio prediction (shared quark dimension):")
    print(f"    m_d/m_u = (a/R_d)/(a/R_u) = 3/(3/2) = 2")
    print(f"    Experimental: {m_d/m_u:.2f}")
    print()


if __name__ == "__main__":
    main()
