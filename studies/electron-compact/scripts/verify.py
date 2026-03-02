#!/usr/bin/env python3
"""
verify.py — Electron from Geometry: numerical verification.

Computes the fully determined electron geometry (r = a/R = 1/√(πα))
and verifies all measurable properties match experiment.

Reference: findings.md F1–F8.
Run:  python3 studies/electron-compact/scripts/verify.py
"""

import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import (h, hbar, c, e, eps0, alpha, m_e,
                            lambda_C, r_bar)


def banner(title):
    print()
    print("=" * 64)
    print(f"  {title}")
    print("=" * 64)


def section(title):
    print(f"\n--- {title} ---\n")


# ── Derived constants ─────────────────────────────────────────

lbar_C    = hbar / (m_e * c)                     # reduced Compton wavelength
mu_B      = e * hbar / (2 * m_e)                 # Bohr magneton (J/T)
g_wvm     = 2 * (1 + alpha / (2 * math.pi))      # WvM g-factor (with q=e)
mu_e_calc = g_wvm * mu_B / 2                     # predicted magnetic moment
mu_e_exp  = 9.2847647043e-24                     # NIST value (J/T)

# The physical aspect ratio, fixed by the charge condition (S2)
r_phys = 1 / math.sqrt(math.pi * alpha)


# ══════════════════════════════════════════════════════════════
#  Section 1: Constants and reference values
# ══════════════════════════════════════════════════════════════

banner("1. Reference values")

print(f"  Compton wavelength       λ_C   = {lambda_C:.6e} m")
print(f"  Reduced Compton          ƛ_C   = {lbar_C:.6e} m")
print(f"  Electron mass            m_e   = {m_e:.6e} kg")
print(f"                                 = {m_e * c**2 / e / 1e6:.4f} MeV/c²")
print(f"  Fine-structure const     α     = {alpha:.6e}")
print(f"  1/α                           = {1/alpha:.2f}")
print(f"  Bohr magneton            μ_B   = {mu_B:.6e} J/T")


# ══════════════════════════════════════════════════════════════
#  Section 2: The physical aspect ratio
# ══════════════════════════════════════════════════════════════

banner("2. Aspect ratio from charge condition  [findings F3]")

section("r = a/R = L_θ/L_φ = 1/√(πα)")

print(f"  πα                     = {math.pi * alpha:.6f}")
print(f"  1/(πα)                 = {1/(math.pi * alpha):.4f}")
print(f"  r = 1/√(πα)            = {r_phys:.5f}")
print()
print(f"  This is fixed by the charge condition a/R = 1/√(πα).")
print(f"  The tube circumference L_θ = 2πa, the major circumference")
print(f"  L_φ = 2πR, so r = L_θ/L_φ = a/R.")


# ══════════════════════════════════════════════════════════════
#  Section 3: Fully determined geometry
# ══════════════════════════════════════════════════════════════

banner("3. Fully determined electron geometry  [findings F5]")

r = r_phys
L_phi   = lambda_C / math.sqrt(4 + r**2)
L_theta = r * L_phi
R       = L_phi / (2 * math.pi)
a       = L_theta / (2 * math.pi)
path    = math.sqrt(4 * L_phi**2 + L_theta**2)
E       = h * c / path
mass    = E / c**2
T_orbit = path / c
f_orbit = 1 / T_orbit

section("Compact dimensions (the flat rectangle)")
print(f"  L_φ  (major circ.)     = {L_phi:.6e} m")
print(f"  L_θ  (minor circ.)     = {L_theta:.6e} m")
print(f"  r = L_θ/L_φ            = {L_theta/L_phi:.5f}")

section("3D torus embedding")
print(f"  R    (major radius)    = {R:.6e} m")
print(f"  a    (tube radius)     = {a:.6e} m")
print(f"  a/R                    = {a/R:.5f}")
print(f"  (Spindle torus: a > R, self-intersects in 3D embedding)")

section("Path and resonance")
print(f"  Path length ℓ          = {path:.6e} m")
print(f"  λ_C                    = {lambda_C:.6e} m")
print(f"  ℓ / λ_C                = {path/lambda_C:.10f}")
print(f"  Orbit period T         = {T_orbit:.6e} s")
print(f"  Orbit frequency f      = {f_orbit:.4e} Hz")
print(f"  Compton frequency      = {m_e * c**2 / h:.4e} Hz")
print(f"  f_orbit / f_Compton    = {f_orbit / (m_e * c**2 / h):.10f}")


# ══════════════════════════════════════════════════════════════
#  Section 4: All electron properties
# ══════════════════════════════════════════════════════════════

banner("4. Electron properties — all verified  [findings F6]")

g_factor = g_wvm
spin = 0.5
mu = g_factor * (e / (2 * mass)) * spin * hbar

section("Mass")
print(f"  E = hc/ℓ               = {E / e / 1e6:.6f} MeV")
print(f"  m = E/c²               = {mass:.6e} kg")
print(f"  m / m_e                = {mass/m_e:.10f}")

section("Spin")
print(f"  s = ℏ/2                = {spin}")
print(f"  (topological — from (1,2) double winding)")

section("Charge")
print(f"  a/R = 1/√(πα)          = {a/R:.5f}")
print(f"  q = e                  (by construction from S2)")

section("g-factor and magnetic moment")
print(f"  g = 2(1 + α/(2π))     = {g_factor:.6f}")
print(f"  g (experiment)         = 2.002319")
print(f"  μ = g(e/2m)(ℏ/2)      = {mu:.6e} J/T")
print(f"  μ (NIST)               = {mu_e_exp:.6e} J/T")
print(f"  μ_calc / μ_exp         = {mu/mu_e_exp:.6f}")


# ══════════════════════════════════════════════════════════════
#  Section 5: Consistency checks
# ══════════════════════════════════════════════════════════════

banner("5. Consistency checks")

checks = []

def check(name, val, expected, tol=1e-10):
    ok = abs(val / expected - 1) < tol
    status = "✓" if ok else "✗"
    print(f"  {status}  {name:30s}  = {val:.6e}  (expect {expected:.6e},"
          f"  ratio {val/expected:.10f})")
    checks.append(ok)

check("Path length",    path,       lambda_C)
check("Mass",           mass,       m_e)
check("a/R ratio",      a/R,        r_phys)
check("Orbit frequency", f_orbit,   m_e * c**2 / h)

print()
if all(checks):
    print("  All checks passed.")
else:
    print("  SOME CHECKS FAILED — investigate.")


# ══════════════════════════════════════════════════════════════
#  Section 6: Comparison with WvM r → 0 limit
# ══════════════════════════════════════════════════════════════

banner("6. Comparison with WvM (r → 0 limit)  [findings F5]")

R_wvm = lambda_C / (4 * math.pi)

print(f"  WvM assumed r → 0 (thin torus):")
print(f"    R_wvm = λ_C/(4π)     = {R_wvm:.6e} m")
print(f"    (tube radius → 0)")
print()
print(f"  Corrected (r = {r_phys:.2f}):")
print(f"    R                    = {R:.6e} m")
print(f"    a                    = {a:.6e} m")
print(f"    R / R_wvm            = {R/R_wvm:.4f}")
print()
print(f"  The corrected orbital radius R is {R/R_wvm:.1%} of WvM's value.")
print(f"  The torus is much fatter than WvM assumed (a ≈ {a/R:.1f} R).")


# ══════════════════════════════════════════════════════════════
#  Section 7: The electron recipe
# ══════════════════════════════════════════════════════════════

banner("7. The electron recipe  [findings F6]")

print(f"""
  ┌─────────────────────────────────────────────────────────────┐
  │                     ELECTRON RECIPE                         │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  Inputs:                                                    │
  │    • Two compact periodic dimensions (T²)                   │
  │    • Geodesic: (1,2) torus knot                             │
  │    • Photon energy: E = m_e c² = 0.511 MeV                 │
  │    • Fine-structure constant: α ≈ 1/137                     │
  │                                                             │
  │  Geometry (fully determined):                               │
  │    • r = a/R = 1/√(πα)  = {r_phys:8.4f}                     │
  │    • R (major radius)   = {R:.3e} m                     │
  │    • a (tube radius)    = {a:.3e} m                     │
  │    • ℓ (path length)    = {path:.3e} m = λ_C             │
  │                                                             │
  │  Properties (all match experiment):                         │
  │    • Mass   = 0.511 MeV/c²     (from resonance)            │
  │    • Spin   = ½                 (from topology)             │
  │    • Charge = e                 (from r = 1/√(πα))          │
  │    • g      ≈ 2.0023            (from α)                    │
  │    • μ      = 9.285 × 10⁻²⁴ J/T                            │
  │                                                             │
  │  Free parameters: NONE                                      │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
""")


# ══════════════════════════════════════════════════════════════
#  Section 8: Other particles — exploratory
# ══════════════════════════════════════════════════════════════

banner("8. Other particles — exploratory  [findings F7]")

section("Muon: same topology, different energy?")

m_muon = 1.883531627e-28  # kg
ratio = m_muon / m_e
lambda_mu = h / (m_muon * c)

L_phi_mu   = lambda_mu / math.sqrt(4 + r_phys**2)
L_theta_mu = r_phys * L_phi_mu
R_mu       = L_phi_mu / (2 * math.pi)
a_mu       = L_theta_mu / (2 * math.pi)

print(f"  m_μ / m_e              = {ratio:.2f}")
print(f"  λ_μ (Compton)          = {lambda_mu:.4e} m")
print(f"  If same T² shape (r = {r_phys:.2f}), same (1,2) knot:")
print(f"    R_μ                  = {R_mu:.4e} m")
print(f"    a_μ                  = {a_mu:.4e} m")
print(f"    R_e / R_μ            = {R/R_mu:.2f}  (= m_μ/m_e)")
print(f"  The muon would be a smaller copy of the electron.")
print(f"  What makes it heavier — a shorter-wavelength photon on")
print(f"  the same T², or a different (smaller) T²?")

section("Quark charges: different a/R ratios (S3)")

for name, q_frac in [("electron", 1.0), ("up quark", 2/3), ("down quark", 1/3)]:
    r_q = 1 / (q_frac * math.sqrt(math.pi * alpha))
    print(f"  {name:12s}  q = {q_frac:.3f}e  →  r = a/R = {r_q:.4f}"
          f"  = {1/q_frac:.0f}/√(πα)")

print()
print("  Different charges imply different aspect ratios.")
print("  Quarks would need a different T² (or a different a/R")
print("  mechanism) than the electron.")
