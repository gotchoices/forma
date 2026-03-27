#!/usr/bin/env python3
"""
verify.py — Numerical verification for the KK charge comparison.

Evaluates every charge formula from findings.md with physical
constants, computes implied scales, and explores the T² parameter
space for a (1,2) geodesic.

Reference: findings.md F1–F12.
"""

import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
from constants import (h, hbar, c, e, eps0, G, alpha, m_e,
                        lambda_C, l_P)

# ── Additional derived quantities ─────────────────────────────

q_P   = math.sqrt(4 * math.pi * eps0 * hbar * c)  # Planck charge (C)
lbar_C = hbar / (m_e * c)                      # reduced Compton wavelength (m)


def banner(title):
    print()
    print("=" * 62)
    print(f"  {title}")
    print("=" * 62)


def section(title):
    print(f"\n--- {title} ---\n")


# ══════════════════════════════════════════════════════════════
#  Section 1: Fundamental scales
# ══════════════════════════════════════════════════════════════

banner("1. Fundamental scales")

print(f"  Planck length          l_P    = {l_P:.4e} m")
print(f"  Planck charge          q_P    = {q_P:.4e} C")
print(f"  Fine-structure const   α      = {alpha:.6e}")
print(f"  √α                           = {math.sqrt(alpha):.6f}")
print(f"  Compton wavelength     λ_C    = {lambda_C:.4e} m")
print(f"  Reduced Compton        ƛ_C    = {lbar_C:.4e} m")
print(f"  WvM orbit radius  ƛ_C/2      = {lbar_C/2:.4e} m")
print(f"  Elementary charge      e      = {e:.4e} C")
print(f"  e / q_P  = √α               = {e/q_P:.6f}")

assert abs(e/q_P - math.sqrt(alpha)) / math.sqrt(alpha) < 1e-6, \
    "e/q_P should equal √α"


# ══════════════════════════════════════════════════════════════
#  Section 2: KK charge formula (gravitational, 5D)
# ══════════════════════════════════════════════════════════════

banner("2. KK gravitational charge (5D)")

section("The coupling constant κ  [findings F5]")

kappa = math.sqrt(4 * math.pi * eps0 * G) / c
print(f"  κ = √(4πε₀G) / c  = {kappa:.4e}")

section("Compact radius for q = e (n=1)")

R_KK = l_P / math.sqrt(alpha)
R_KK_alt = math.sqrt(4 * math.pi * eps0 * G) * hbar / (e * c)
print(f"  R_KK = l_P / √α           = {R_KK:.4e} m")
print(f"  R_KK (direct formula)      = {R_KK_alt:.4e} m")
print(f"  R_KK / l_P                 = {R_KK/l_P:.2f}  (Planck lengths)")
print(f"  R_KK / ƛ_C                 = {R_KK/lbar_C:.2e}")

assert abs(R_KK - R_KK_alt) / R_KK < 1e-4, \
    "Two R_KK formulas should agree"

section("Verification: KK charge at R = R_KK")

q_KK_check = q_P * l_P / R_KK
print(f"  q_KK  = q_P × l_P / R_KK  = {q_KK_check:.4e} C")
print(f"  q_KK / e                   = {q_KK_check/e:.6f}")

assert abs(q_KK_check/e - 1.0) < 0.01, \
    "KK charge at R_KK should give e"

section("Scale comparison")

ratio = (lbar_C / 2) / R_KK
print(f"  WvM orbit radius           = {lbar_C/2:.4e} m")
print(f"  KK compact radius          = {R_KK:.4e} m")
print(f"  Ratio (WvM / KK)           = {ratio:.2e}")
print(f"  ≈ 10^{math.log10(ratio):.1f}")


# ══════════════════════════════════════════════════════════════
#  Section 3: WvM charge formula
# ══════════════════════════════════════════════════════════════

banner("3. WvM charge formula  [findings F7]")

q_WvM = (1 / (2 * math.pi)) * math.sqrt(3 * eps0 * hbar * c)

print(f"  q_WvM = (1/2π) √(3ε₀ℏc)   = {q_WvM:.4e} C")
print(f"  e                           = {e:.4e} C")
print(f"  q_WvM / e                   = {q_WvM/e:.4f}")
print(f"  Deficit                     = {(1 - q_WvM/e)*100:.1f}%")

section("In Planck units")

q_WvM_over_qP = q_WvM / q_P
geometric_factor = math.sqrt(3 / (16 * math.pi**3))

print(f"  q_WvM / q_P                = {q_WvM_over_qP:.6f}")
print(f"  √(3/(16π³))                = {geometric_factor:.6f}")
print(f"  √α                         = {math.sqrt(alpha):.6f}")
print(f"  (q_WvM / e)²               = {(q_WvM/e)**2:.4f}")
print(f"  i.e.  3/(16π³) / α         = {geometric_factor**2 / alpha:.4f}")

section("What q_WvM = q_KK would require")

R_match = l_P * q_P / q_WvM
print(f"  If q_KK = q_WvM:")
print(f"    R = l_P × q_P / q_WvM   = {R_match:.4e} m")
print(f"    R / l_P                  = {R_match/l_P:.2f}  Planck lengths")
print(f"  Compare: R_KK (for q=e)    = {R_KK/l_P:.2f}  Planck lengths")


# ══════════════════════════════════════════════════════════════
#  Section 4: Structural comparison
# ══════════════════════════════════════════════════════════════

banner("4. Structural comparison  [findings F8]")

print("  Formula                    Value (C)     / e       / q_P")
print("  ─────────────────────────  ──────────    ──────    ──────")
print(f"  e (observed)               {e:.4e}    1.0000    {e/q_P:.6f}")
print(f"  q_WvM                      {q_WvM:.4e}    {q_WvM/e:.4f}    {q_WvM/q_P:.6f}")
print(f"  q_KK (R = R_KK)            {q_KK_check:.4e}    {q_KK_check/e:.4f}    {q_KK_check/q_P:.6f}")
print()
print("  Key: q_WvM involves (ε₀, ℏ, c, geometry)")
print("       q_KK  involves (G, ε₀, ℏ, c, compact radius R)")
print("       WvM has no G.  KK requires G.")


# ══════════════════════════════════════════════════════════════
#  Section 5: T² parameter space for (1,2) geodesic
# ══════════════════════════════════════════════════════════════

banner("5. T² parameter space — (1,2) geodesic  [findings F10]")

section("Constraint: √(4L₁² + L₂²) = λ_C")

n1, n2 = 2, 1

sample_ratios = [0.5, 1.0, 2.0, 4.0, 8.0]
print(f"  r = L₂/L₁    L₁ (m)       L₂ (m)       "
      f"R₁ (m)       R₂ (m)")
print(f"  ────────      ──────       ──────       "
      f"──────       ──────")

for r in sample_ratios:
    L1 = lambda_C / math.sqrt(n1**2 + (n2 * r)**2)
    L2 = r * L1
    R1 = L1 / (2 * math.pi)
    R2 = L2 / (2 * math.pi)
    print(f"  {r:5.1f}      {L1:.4e}   {L2:.4e}   "
          f"{R1:.4e}   {R2:.4e}")

section("KK gravitational charges at Compton scale  [findings F10]")

print("  For any r, the compact radii are ~ λ_C/(2π) ~ 10⁻¹³ m.")
print("  KK charge goes as q_P × l_P / R.\n")

r_example = 2.0
L1 = lambda_C / math.sqrt(n1**2 + (n2 * r_example)**2)
L2 = r_example * L1
R1 = L1 / (2 * math.pi)
R2 = L2 / (2 * math.pi)

q1_KK = n1 * q_P * l_P / R1
q2_KK = n2 * q_P * l_P / R2
q_eff = math.sqrt(q1_KK**2 + q2_KK**2)

print(f"  Example: r = {r_example}")
print(f"    L₁ = {L1:.4e} m     L₂ = {L2:.4e} m")
print(f"    R₁ = {R1:.4e} m     R₂ = {R2:.4e} m")
print()
print(f"    q₁ (KK, n₁=2) = {q1_KK:.4e} C  =  {q1_KK/e:.2e} × e")
print(f"    q₂ (KK, n₂=1) = {q2_KK:.4e} C  =  {q2_KK/e:.2e} × e")
print(f"    |q| (Pythag.)  = {q_eff:.4e} C  =  {q_eff/e:.2e} × e")
print()
print(f"  These are ~ 10^{math.log10(q1_KK/e):.0f} times too small.")
print(f"  The KK gravitational mechanism does not work at Compton scale.")

section("WvM charge (independent of geometry)")

print(f"  q_WvM = {q_WvM:.4e} C = {q_WvM/e:.4f} × e")
print(f"  (Same regardless of L₁, L₂ — depends only on field topology)")


# ══════════════════════════════════════════════════════════════
#  Section 6: Ratio sweep
# ══════════════════════════════════════════════════════════════

banner("6. Ratio sweep: L₂/L₁ from 0.1 to 10  [findings F10]")

print("  r = L₂/L₁   q₁/e          q₂/e          |q|/e")
print("  ─────────    ──────        ──────         ──────")

for i in range(11):
    r = 0.1 + i * 0.99
    L1 = lambda_C / math.sqrt(n1**2 + (n2 * r)**2)
    L2 = r * L1
    R1 = L1 / (2 * math.pi)
    R2 = L2 / (2 * math.pi)
    q1 = n1 * q_P * l_P / R1
    q2 = n2 * q_P * l_P / R2
    qe = math.sqrt(q1**2 + q2**2)
    print(f"  {r:7.2f}      {q1/e:.4e}    {q2/e:.4e}     {qe/e:.4e}")

print()
print("  All KK charges are ~ 10⁻²² × e, regardless of ratio.")
print("  The gravitational coupling is too weak at this scale.")


# ══════════════════════════════════════════════════════════════
#  Section 7: Summary
# ══════════════════════════════════════════════════════════════

banner("7. Summary")

print("""
  ┌─────────────────────────────────────────────────────────┐
  │  Charge formula        Value       Involves G?  Scale   │
  ├─────────────────────────────────────────────────────────┤
  │  e (observed)          1.000 e     —            —       │
  │  q_WvM (cavity E)      0.912 e     No           Compton │
  │  q_KK  (gravitational) 1.000 e*    Yes          Planck  │
  │                                                         │
  │  * requires R = l_P/√α ≈ 1.89 × 10⁻³⁴ m               │
  │    At Compton-scale R: q_KK ~ 10⁻²² e                  │
  └─────────────────────────────────────────────────────────┘

  Conclusion: WvM and KK charge are different mechanisms.
  KK provides topology (confinement, spin, mass quantization).
  WvM provides the charge (electromagnetic field profile).
""")
