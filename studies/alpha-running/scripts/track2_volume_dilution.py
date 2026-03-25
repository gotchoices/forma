#!/usr/bin/env python3
"""
R32 Track 2: Volume dilution and the high-energy coupling.

In Kaluza-Klein theory, the 4D gauge coupling is related to
the higher-dimensional coupling by the volume of the compact
space:

    α₄ = α_D / V_compact   (in appropriate units)

More precisely, for a (4+d)-dimensional theory compactified
on a d-dimensional torus, the 4D coupling is:

    g₄² = g_{4+d}² / V_d

where V_d is the volume of the compact space in units of
the fundamental length scale.

This script computes:
1. The physical volume of each T² sheet and of T⁶
2. The "bare" higher-dimensional coupling α_D = α × V / V_ref
3. Whether α_D is a recognizable geometric constant
4. Dimensionless volume ratios between sheets
"""

import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6_solver import self_consistent_metric
from lib.t6 import (
    M_P_MEV, M_E_MEV, M_N_MEV, hbar_c_MeV_fm, ALPHA,
)

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064

print("=" * 70)
print("R32 Track 2: Volume dilution and the high-energy coupling")
print("=" * 70)

result = self_consistent_metric(
    R_E, R_NU, R_P, sigma_ep=SIGMA_EP
)
L = result['L']

labels = ["L₁(e tube)", "L₂(e ring)", "L₃(ν tube)",
          "L₄(ν ring)", "L₅(p tube)", "L₆(p ring)"]

print(f"\nCircumferences:")
for i, lab in enumerate(labels):
    print(f"  {lab:15s} = {L[i]:18.2f} fm")

# ── Sheet areas ──────────────────────────────────────────────────────

A_e = L[0] * L[1]
A_nu = L[2] * L[3]
A_p = L[4] * L[5]
V_t6 = A_e * A_nu * A_p

print(f"\nSheet areas:")
print(f"  Electron T²:  A_e  = L₁ × L₂ = {A_e:.4e} fm²")
print(f"  Neutrino T²:  A_ν  = L₃ × L₄ = {A_nu:.4e} fm²")
print(f"  Proton T²:    A_p  = L₅ × L₆ = {A_p:.4e} fm²")
print(f"\n  Full T⁶ volume: V = {V_t6:.4e} fm⁶")

# ── Compton wavelengths for reference ────────────────────────────────

lambda_e = hbar_c_MeV_fm / M_E_MEV
lambda_p = hbar_c_MeV_fm / M_P_MEV

print(f"\nCompton wavelengths (ℏ/mc):")
print(f"  Electron: λ_e = {lambda_e:.2f} fm")
print(f"  Proton:   λ_p = {lambda_p:.4f} fm")

# ── Dimensionless volumes ────────────────────────────────────────────
# Express volumes in natural units: V / λ^d where λ is the
# relevant Compton wavelength

print(f"\n{'='*70}")
print("DIMENSIONLESS VOLUME RATIOS")
print("="*70)

A_e_dimless = A_e / lambda_e**2
A_p_dimless = A_p / lambda_p**2
A_nu_dimless_e = A_nu / lambda_e**2

print(f"\n  A_e / λ_e²  = {A_e_dimless:.4f}")
print(f"  A_p / λ_p²  = {A_p_dimless:.4f}")
print(f"  A_ν / λ_e²  = {A_nu_dimless_e:.4e}")

print(f"\n  Ratio A_e/A_p = {A_e/A_p:.4e}")
print(f"  Ratio A_ν/A_e = {A_nu/A_e:.4e}")
print(f"  Ratio A_ν/A_p = {A_nu/A_p:.4e}")

# ── KK volume dilution ───────────────────────────────────────────────
#
# In KK theory for a single extra dimension of radius R:
#   α₄ = α₅ / (2πR)
# where α₅ has dimensions of [length].
#
# For 2 extra dimensions (one T²):
#   α₄ = α₆ / A
# where α₆ has dimensions of [length²].
#
# The dimensionless "bare" coupling is obtained by measuring
# the volume in natural units.  For a T² with circumferences
# L₁, L₂, the natural unit of area is (2πλ_C)² where λ_C
# is the Compton wavelength of the particle defining the scale.
#
# α_bare = α₄ × (A / A_natural)

print(f"\n{'='*70}")
print("VOLUME DILUTION: α_bare = α × V / V_natural")
print("="*70)

# For each sheet, compute α_bare using its own Compton wavelength
# as the natural scale

# Electron sheet: natural area = (2π ℏ/m_e c)²
A_nat_e = (2 * math.pi * lambda_e)**2
alpha_bare_e = ALPHA * A_e / A_nat_e
print(f"\nElectron sheet:")
print(f"  Natural area (2πλ_e)² = {A_nat_e:.2f} fm²")
print(f"  A_e / A_nat_e = {A_e/A_nat_e:.6f}")
print(f"  α_bare_e = α × A_e/A_nat_e = {alpha_bare_e:.6f}")
print(f"  1/α_bare_e = {1/alpha_bare_e:.2f}")

# Proton sheet
A_nat_p = (2 * math.pi * lambda_p)**2
alpha_bare_p = ALPHA * A_p / A_nat_p
print(f"\nProton sheet:")
print(f"  Natural area (2πλ_p)² = {A_nat_p:.6f} fm²")
print(f"  A_p / A_nat_p = {A_p/A_nat_p:.6f}")
print(f"  α_bare_p = α × A_p/A_nat_p = {alpha_bare_p:.6f}")
print(f"  1/α_bare_p = {1/alpha_bare_p:.2f}")

# ── Alternative: use circumference ratios ────────────────────────────
# The mode energy is E = (2πℏc/L) × μ, so the natural length
# for the electron is L₂/μ₁₂.  Since E = m_e, we have
# L₂ = 2πℏc × μ₁₂ / m_e = 2πλ_e × μ₁₂.

mu_e = L[1] / (2 * math.pi * lambda_e)
mu_p = L[5] / (2 * math.pi * lambda_p)

print(f"\n{'='*70}")
print("MODE ENERGY FACTORS")
print("="*70)
print(f"  μ₁₂(electron) = L₂/(2πλ_e) = {mu_e:.6f}")
print(f"  μ₁₂(proton)   = L₆/(2πλ_p) = {mu_p:.6f}")
print(f"  These encode the shear: L = 2πλ_C × μ₁₂")

# ── Effective 4+2 coupling (electron sheet only) ─────────────────────
# If we treat the electron sheet as a 2D compact space and
# the proton/neutrino sheets as decoupled, the KK relation is:
#   α₄ = g₆² / A_e
# So g₆² = α₄ × A_e = α × L₁ × L₂

print(f"\n{'='*70}")
print("EFFECTIVE HIGHER-DIMENSIONAL COUPLINGS")
print("="*70)

g6_e_sq = ALPHA * A_e
print(f"\nElectron sheet (4+2 → 4 reduction):")
print(f"  g₆² = α × A_e = {g6_e_sq:.4f} fm²")
print(f"  g₆² / (4π) = {g6_e_sq/(4*math.pi):.4f} fm²")
print(f"  g₆  = {math.sqrt(g6_e_sq):.4f} fm")
print(f"  g₆ / λ_e = {math.sqrt(g6_e_sq)/lambda_e:.6f}")
print(f"  g₆² / λ_e² = {g6_e_sq/lambda_e**2:.6f}")

g6_p_sq = ALPHA * A_p
print(f"\nProton sheet (4+2 → 4 reduction):")
print(f"  g₆² = α × A_p = {g6_p_sq:.6f} fm²")
print(f"  g₆ / λ_p = {math.sqrt(g6_p_sq)/lambda_p:.6f}")
print(f"  g₆² / λ_p² = {g6_p_sq/lambda_p**2:.6f}")

# ── Effective 4+4 coupling (electron + proton) ───────────────────────

V_ep = A_e * A_p
g8_sq = ALPHA * V_ep
print(f"\nElectron + proton sheets (4+4 → 4 reduction):")
print(f"  V_ep = A_e × A_p = {V_ep:.4e} fm⁴")
print(f"  g₈² = α × V_ep = {g8_sq:.4e} fm⁴")

# ── Search for recognizable constants ────────────────────────────────

print(f"\n{'='*70}")
print("SEARCH FOR RECOGNIZABLE GEOMETRIC CONSTANTS")
print("="*70)

# The key dimensionless ratios
ratios = {
    "A_e / A_nat_e": A_e / A_nat_e,
    "A_p / A_nat_p": A_p / A_nat_p,
    "A_e / (4π λ_e²)": A_e / (4 * math.pi * lambda_e**2),
    "A_p / (4π λ_p²)": A_p / (4 * math.pi * lambda_p**2),
    "√(A_e/A_p)": math.sqrt(A_e / A_p),
    "A_e/A_p / (m_p/m_e)²": (A_e/A_p) / (M_P_MEV/M_E_MEV)**2,
    "L₁/L₅ (tube ratio)": L[0] / L[4],
    "L₂/L₆ (ring ratio)": L[1] / L[5],
    "r_e × r_p": R_E * R_P,
    "r_e / r_p": R_E / R_P,
    "(r_e × r_p) / (4π)": R_E * R_P / (4 * math.pi),
}

known_constants = {
    "1": 1.0,
    "2": 2.0,
    "4": 4.0,
    "π": math.pi,
    "2π": 2 * math.pi,
    "4π": 4 * math.pi,
    "4π²": 4 * math.pi**2,
    "1/α": 1/ALPHA,
    "24": 24.0,
    "1/24": 1/24.0,
    "α": ALPHA,
    "m_p/m_e": M_P_MEV / M_E_MEV,
    "(m_p/m_e)²": (M_P_MEV / M_E_MEV)**2,
}

print(f"\nDimensionless ratios and nearby constants:")
for name, val in ratios.items():
    print(f"\n  {name} = {val:.6f}")
    for cname, cval in known_constants.items():
        if cval > 0 and abs(val/cval - 1) < 0.05:
            print(f"    ≈ {cname} ({cval:.6f}, off by {(val/cval-1)*100:+.2f}%)")

# ── The specific question: what is the "bare" alpha? ─────────────────

print(f"\n{'='*70}")
print("THE BARE COUPLING QUESTION")
print("="*70)

print(f"""
The KK volume dilution says:
    α₄ = α_D / V_dimensionless

If α₄ = 1/137 and V_dimensionless = A/(2πλ)²:

  Electron sheet:
    V_dimless = {A_e/A_nat_e:.6f}
    α_D = α × V = {alpha_bare_e:.6f}
    1/α_D = {1/alpha_bare_e:.2f}

  Proton sheet:
    V_dimless = {A_p/A_nat_p:.6f}
    α_D = α × V = {alpha_bare_p:.6f}
    1/α_D = {1/alpha_bare_p:.2f}
""")

# ── Check: does α_D relate to 1/24? ─────────────────────────────────

print(f"Comparison to 1/24 = {1/24:.6f}:")
print(f"  α_bare_e = {alpha_bare_e:.6f}  →  ratio to 1/24: {alpha_bare_e * 24:.4f}")
print(f"  α_bare_p = {alpha_bare_p:.6f}  →  ratio to 1/24: {alpha_bare_p * 24:.4f}")

# ── Neutrino sheet and scale hierarchy ───────────────────────────────

print(f"\n{'='*70}")
print("NEUTRINO SHEET AND SCALE HIERARCHY")
print("="*70)

A_nat_nu_e = (2 * math.pi * lambda_e)**2
print(f"\nNeutrino sheet volume (in electron natural units):")
print(f"  A_ν / (2πλ_e)² = {A_nu/A_nat_nu_e:.4e}")
print(f"  This enormous ratio ({A_nu/A_nat_nu_e:.1e}) explains why")
print(f"  neutrino interactions are weak: the coupling is diluted")
print(f"  by the huge neutrino sheet area.")

alpha_weak_est = ALPHA * A_e / A_nu
print(f"\n  Estimated 'weak coupling' from volume ratio:")
print(f"  α_weak ~ α × A_e/A_ν = {alpha_weak_est:.4e}")
print(f"  Fermi constant G_F ~ {alpha_weak_est:.4e}")
print(f"  Measured G_F ~ 1.166e-5 GeV⁻²")

# Express G_F in dimensionless terms for comparison
# G_F in natural units: G_F × m_p² ≈ 1.02e-5
GF_dimless = 1.166e-5 * (M_P_MEV * 1e-3)**2
print(f"  G_F × m_p² = {GF_dimless:.4e} (dimensionless)")
print(f"  α × A_e/A_ν = {alpha_weak_est:.4e}")
print(f"  Ratio: {alpha_weak_est/GF_dimless:.2f}")

# ── Summary ──────────────────────────────────────────────────────────

print(f"\n{'='*70}")
print("SUMMARY")
print("="*70)

print(f"""
1. Volume dilution on the electron sheet:
   α_bare = α × A_e/(2πλ_e)² = {alpha_bare_e:.6f}  (1/α_bare = {1/alpha_bare_e:.1f})
   This is NOT 1/24.  It is {alpha_bare_e*24:.3f} × (1/24).

2. Volume dilution on the proton sheet:
   α_bare = α × A_p/(2πλ_p)² = {alpha_bare_p:.6f}  (1/α_bare = {1/alpha_bare_p:.1f})
   This is also not a recognizable constant.

3. The electron/proton area ratio:
   A_e/A_p = {A_e/A_p:.4e}  ≈ (m_p/m_e)² × (r_e/r_p)²
   This is by construction: L ~ 2πλ_C × μ, and λ_C ~ 1/m.

4. The neutrino sheet is {A_nu/A_e:.1e}× larger than the
   electron sheet.  This volume ratio provides a natural
   explanation for why weak interactions are weak: the
   coupling is geometrically diluted by the enormous
   neutrino compact space.

5. The naive volume dilution does not produce 1/24 or any
   other immediately recognizable geometric constant.  The
   "bare" coupling depends on which sheet is used and which
   natural length scale defines the dimensionless volume.
""")
