#!/usr/bin/env python3
"""
Q52 quick check: what happens at r = a/R = 1/2?

The "equal distance per winding" argument gives r = 1/2.
Check what geometry this produces and whether anything
interesting falls out.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import (h, hbar, c, eps0, e, alpha, m_e, lambda_C, mu0)

r_e = e**2 / (4.0 * math.pi * eps0 * m_e * c**2)
lambda_bar = lambda_C / (2.0 * math.pi)  # reduced Compton wavelength
mu_B = e * hbar / (2.0 * m_e)  # Bohr magneton

print("=" * 66)
print("Q52: Geometry at r = a/R = 1/2")
print("=" * 66)
print()

r = 0.5
R = lambda_C / (2.0 * math.pi * math.sqrt(4 + r**2))
a = r * R

print("PATH CONSTRAINT: ℓ = 2π√(a² + 4R²) = λ_C")
print()
print(f"  r = a/R = {r}")
print(f"  R = λ_C / (2π√(4 + r²)) = λ_C / (2π√{4 + r**2})")
print(f"    = {R:.6e} m")
print(f"  a = R/2 = {a:.6e} m")
print()

path_len = 2.0 * math.pi * math.sqrt((1 * a)**2 + (2 * R)**2)
print(f"  Path length = {path_len:.6e} m")
print(f"  λ_C         = {lambda_C:.6e} m")
print(f"  Ratio       = {path_len/lambda_C:.10f}")
print()

# Comparison scales
print("COMPARISON WITH KNOWN SCALES")
print("-" * 66)
print(f"  R          = {R:.6e} m")
print(f"  a          = {a:.6e} m")
print(f"  λ_C        = {lambda_C:.6e} m  (Compton wavelength)")
print(f"  λ̄_C = ℏ/mc = {lambda_bar:.6e} m  (reduced Compton)")
print(f"  r_e        = {r_e:.6e} m  (classical electron radius)")
print()
print(f"  R / λ̄_C    = {R/lambda_bar:.6f}")
print(f"  R / r_e    = {R/r_e:.6f}")
print(f"  a / r_e    = {a/r_e:.6f}")
print(f"  R / λ_C    = {R/lambda_C:.6f}")
print()

# Clean expressions
print("CLEAN EXPRESSIONS")
print("-" * 66)
sqrt_val = math.sqrt(4 + 0.25)
print(f"  √(4 + 1/4) = √(17/4) = √17/2 = {sqrt_val:.6f}")
print(f"  R = λ_C / (π√17) = {lambda_C / (math.pi * math.sqrt(17)):.6e} m")
print(f"                    = {R:.6e} m  ✓")
print(f"  a = λ_C / (2π√17) = {lambda_C / (2*math.pi*math.sqrt(17)):.6e} m")
print()

# Tube circumference and ring circumference
tube_circ = 2 * math.pi * a
ring_circ = 2 * math.pi * R
print(f"  Tube circumference (2πa) = {tube_circ:.6e} m")
print(f"  Ring circumference (2πR) = {ring_circ:.6e} m")
print(f"  Tube/Ring ratio          = {tube_circ/ring_circ:.6f} = r = 1/2 ✓")
print()

# Distance per winding
dist_per_tube = tube_circ / 1  # p=1
dist_per_ring = ring_circ / 2  # q=2
print(f"  Distance per tube winding (2πa/1) = {dist_per_tube:.6e} m")
print(f"  Distance per ring winding (2πR/2) = {dist_per_ring:.6e} m")
print(f"  Ratio = {dist_per_tube/dist_per_ring:.6f}")
print(f"  (Should be 1.0 if 'equal distance per winding' → ✓)")
print()

# Area of the torus surface
area = 4.0 * math.pi**2 * R * a
print(f"  Torus surface area = 4π²Ra = {area:.6e} m²")
print()

# What does the R15 localization formula give?
print("R15 LOCALIZATION FORMULA")
print("-" * 66)
sigma = math.sqrt(math.log(1.0/alpha) / 4.0)
print(f"  σ = √(ln(1/α)/4) = {sigma:.6f} rad = {math.degrees(sigma):.2f}°")
print(f"  σ/(2π) = {sigma/(2*math.pi):.4f} ({sigma/(2*math.pi)*100:.1f}% of ring)")
print()
print(f"  σ × R = {sigma * R:.6e} m  (arc length of localization)")
print(f"  σ × R / λ_C = {sigma * R / lambda_C:.6f}")
print(f"  σ × R / a = {sigma * R / a:.6f}")
print()

# Coulomb energy at this geometry
U_coulomb = alpha * m_e * c**2
U_total = m_e * c**2
print("ENERGY BUDGET")
print("-" * 66)
print(f"  Total energy = m_e c² = {U_total:.6e} J")
print(f"  Coulomb energy = α × m_e c² = {U_coulomb:.6e} J")
print(f"  Coulomb / Total = α = {alpha:.6e} = 1/{1/alpha:.1f}")
print()

# Coulomb self-energy at this R
U_point = e**2 / (4 * math.pi * eps0 * R)
print(f"  Point charge self-energy at R:")
print(f"    e²/(4πε₀R) = {U_point:.6e} J")
print(f"    Ratio to m_e c² = {U_point/U_total:.6f}")
print(f"    (Should be ~α = {alpha:.6f})")
print()

# Magnetic moment check
print("MAGNETIC MOMENT CHECK")
print("-" * 66)
print(f"  Bohr magneton μ_B = eℏ/(2m_e) = {mu_B:.6e} J/T")
print()
print("  Classical current loop (I × Area):")
I = e * c / path_len  # current = charge × velocity / path length
A_enclosed = 2 * math.pi * R**2  # q=2 loops, each enclosing πR²
mu_classical = I * A_enclosed
print(f"    I = ec/ℓ = {I:.6e} A")
print(f"    Enclosed area (2 loops × πR²) = {A_enclosed:.6e} m²")
print(f"    μ_classical = I × A = {mu_classical:.6e} J/T")
print(f"    μ_classical / μ_B = {mu_classical/mu_B:.6f}")
print()
print("  QM result (g=2, S=ℏ/2):")
mu_qm = 2 * (e / (2 * m_e)) * (hbar / 2)
print(f"    μ = g × (e/2m) × S = {mu_qm:.6e} J/T")
print(f"    μ / μ_B = {mu_qm/mu_B:.6f}")
print()

# Does r=1/2 give any clean α relationship?
print("DOES r = 1/2 CONNECT TO α?")
print("-" * 66)
print()

# From R7: U/U_target ≈ 0.018 at r=0.5 (from the data table)
u_ratio_r7 = 0.018
g_shape = u_ratio_r7 * U_total / (2 * e**2 / (4*math.pi*eps0*R))
print(f"  From R7 data at r=0.5: U/U_target = {u_ratio_r7}")
print(f"  Shape factor g(0.5) ≈ {g_shape:.4f}")
print(f"  α_forward = π/(4 × g × √(4+r²))")
print(f"            = π/(4 × {g_shape:.4f} × {math.sqrt(4+r**2):.4f})")
alpha_fwd = math.pi / (4 * g_shape * math.sqrt(4 + r**2))
print(f"            = {alpha_fwd:.4f}")
print(f"  κ = α/α_forward = {alpha/alpha_fwd:.6f}")
print()

# Other notable r values for comparison
print("COMPARISON: GEOMETRY AT DIFFERENT r VALUES")
print("-" * 66)
print(f"{'r':>6s} | {'R (m)':>11s} | {'a (m)':>11s} | {'R/λ̄_C':>8s} | {'R/r_e':>8s} | {'note':>20s}")
print("-" * 75)
for rv, note in [(0.25, ""), (0.50, "equal dist/winding"),
                  (1.0/math.pi, "1/π"), (0.5, ""),
                  (1.0, "square torus"),
                  (2.0, ""), (math.pi, "π"),
                  (0.308, "R8 q=137 value")]:
    if rv == 0.5 and note == "":
        continue
    Rv = lambda_C / (2.0 * math.pi * math.sqrt(4 + rv**2))
    av = rv * Rv
    print(f"{rv:6.3f} | {Rv:11.4e} | {av:11.4e} | {Rv/lambda_bar:8.4f} | "
          f"{Rv/r_e:8.2f} | {note:>20s}")

print()
print("=" * 66)
print("SUMMARY")
print("=" * 66)
print()
print(f"At r = 1/2:")
print(f"  R = λ_C/(π√17) ≈ {R:.4e} m ≈ {R/lambda_bar:.3f} λ̄_C ≈ {R/r_e:.1f} r_e")
print(f"  a = λ_C/(2π√17) ≈ {a:.4e} m")
print(f"  The geometry is a thin torus at Compton scale.")
print(f"  The (1,2) WvM charge mechanism works (p=1).")
print(f"  Coulomb energy = α × m_e c² (same as all Compton-scale tori).")
print()
print(f"  r = 1/2 is geometrically clean (equal arc per winding)")
print(f"  but does not by itself determine α.  α still requires")
print(f"  knowing σ (localization) or the embedding deformation (Q51).")
