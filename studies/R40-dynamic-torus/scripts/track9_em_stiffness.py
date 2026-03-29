#!/usr/bin/env python3
"""
R40 Track 9+10: Required stiffness & EM impedance comparison.

QUESTION
========
What restoring pressure must the torus wall supply to confine the photon?
Is this pressure recognizable as an EM quantity involving μ₀ and/or ε₀?

METHOD
======
1. Recompute Track 1's radiation pressure in physical units (Pa, MeV/fm³).
2. At equilibrium, P_in(θ₁) = P_rad(θ₁).  Report the mean and harmonics.
3. Express as effective tension, modulus, energy density.
4. Compare to EM impedance: decompose into magnetic (B²/2μ₀) and
   electric (ε₀E²/2) contributions.  Check whether the required
   stiffness matches a combination of μ₀, ε₀, or Z₀.
"""

import sys
import os
import math

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model import solve_shear_for_alpha, mu_12, M_P_MEV

HBAR_C_FM = 197.3269804       # MeV·fm
C_SI      = 2.99792458e8      # m/s
MEV_TO_J  = 1.602176634e-13   # J per MeV
FM_TO_M   = 1.0e-15           # m per fm
MU_0      = 1.25663706212e-6  # H/m  (permeability)
EPS_0     = 8.8541878128e-12  # F/m  (permittivity)
Z_0       = math.sqrt(MU_0 / EPS_0)  # ≈ 376.73 Ω
G_N       = 6.67430e-11       # m³/(kg·s²)
E_CHARGE  = 1.602176634e-19   # C
ALPHA_EM  = 1.0 / 137.036

MEV_PER_FM3_TO_PA = MEV_TO_J / FM_TO_M**3   # 1 MeV/fm³ in Pa


# ══════════════════════════════════════════════════════════════════════
#  Proton sheet geometry (same as Track 1)
# ══════════════════════════════════════════════════════════════════════

R_P = 8.906
s56 = solve_shear_for_alpha(R_P)
mu_p = mu_12(R_P, s56)
E0_p = M_P_MEV / mu_p
L_ring = 2 * math.pi * HBAR_C_FM / E0_p
L_tube = R_P * L_ring

R = L_ring / (2 * math.pi)      # ring radius (fm)
a = L_tube / (2 * math.pi)      # tube radius (fm)

n1, n2 = 1, 2
E_photon_MeV = M_P_MEV
E_photon_J   = E_photon_MeV * MEV_TO_J

A_torus = 4 * math.pi**2 * a * R                # surface area (fm²)
V_torus = 2 * math.pi**2 * R * a**2             # enclosed volume (fm³)

a_SI = a * FM_TO_M
R_SI = R * FM_TO_M
A_torus_SI = A_torus * FM_TO_M**2
V_torus_SI = V_torus * FM_TO_M**3

print("=" * 70)
print("R40 Track 9+10: Required stiffness & EM impedance comparison")
print("=" * 70)
print()
print(f"Torus geometry (r_p = {R_P}):")
print(f"  a = {a:.4f} fm = {a_SI:.4e} m  (tube radius)")
print(f"  R = {R:.4f} fm = {R_SI:.4e} m  (ring radius)")
print(f"  a/R = {a/R:.3f}")
print(f"  A = 4π²aR = {A_torus:.2f} fm² = {A_torus_SI:.3e} m²")
print(f"  V = 2π²Ra² = {V_torus:.2f} fm³ = {V_torus_SI:.3e} m³")
print(f"  E_photon = {E_photon_MeV:.3f} MeV = {E_photon_J:.4e} J")
print()


# ══════════════════════════════════════════════════════════════════════
#  Section 1: Radiation pressure profile in physical units
# ══════════════════════════════════════════════════════════════════════

print("-" * 70)
print("Section 1: Radiation pressure in physical units")
print("-" * 70)
print()

# Recompute Track 1's 3D geodesic and curvature decomposition
N = 4000
t = np.linspace(0, 2 * math.pi, N, endpoint=False)
dt = t[1] - t[0]
theta1 = n1 * t
theta2 = n2 * t

rho = R + a * np.cos(theta1)
x = rho * np.cos(theta2)
y = rho * np.sin(theta2)
z = a * np.sin(theta1)

dx = -n1 * a * np.sin(theta1) * np.cos(theta2) - n2 * rho * np.sin(theta2)
dy = -n1 * a * np.sin(theta1) * np.sin(theta2) + n2 * rho * np.cos(theta2)
dz = n1 * a * np.cos(theta1)
speed = np.sqrt(dx**2 + dy**2 + dz**2)
T_hat = np.stack([dx, dy, dz], axis=-1) / speed[:, None]

dT = np.zeros_like(T_hat)
for j in range(3):
    dT[:, j] = np.gradient(T_hat[:, j], dt)
kappa_vec = dT / speed[:, None]

e_r = np.stack([
    np.cos(theta1) * np.cos(theta2),
    np.cos(theta1) * np.sin(theta2),
    np.sin(theta1),
], axis=-1)

kappa_radial_raw = np.sum(kappa_vec * e_r, axis=1)

# The curvature vector κ = dT/ds points toward the center of curvature.
# For a photon spiraling inside the tube, κ points inward → κ·e_r < 0.
# The centrifugal REACTION force (outward against the wall) is -κ·e_r.
kappa_outward = -kappa_radial_raw

# Bin by θ₁ to get pressure profile
N_BINS = 256
theta1_bins = np.linspace(0, 2 * math.pi, N_BINS, endpoint=False)
P_binned = np.zeros(N_BINS)
counts = np.zeros(N_BINS)

theta1_mod = theta1 % (2 * math.pi)
for i in range(N):
    bin_idx = int(theta1_mod[i] / (2 * math.pi) * N_BINS) % N_BINS
    P_binned[bin_idx] += kappa_outward[i]
    counts[bin_idx] += 1
mask = counts > 0
P_binned[mask] /= counts[mask]

# P_binned[i] ≈ κ_outward(θ₁_i)  in fm⁻¹  (positive = pushes outward)
# Physical radiation pressure at θ₁:
#   P_rad(θ₁) = u_surface × κ_outward(θ₁)
# where u_surface = E / A_torus is the 2D energy density.
# Dimensions: [MeV/fm²] × [fm⁻¹] = [MeV/fm³] = pressure.

u_surface = E_photon_MeV / A_torus   # MeV/fm²
P_physical = u_surface * P_binned     # MeV/fm³

P_mean = np.mean(P_physical[mask])
P_max  = np.max(P_physical[mask])
P_min  = np.min(P_physical[mask])

P_mean_Pa = P_mean * MEV_PER_FM3_TO_PA
P_max_Pa  = P_max  * MEV_PER_FM3_TO_PA
P_min_Pa  = P_min  * MEV_PER_FM3_TO_PA

print(f"  2D energy density u = E/A = {u_surface:.4f} MeV/fm²")
print(f"  Mean κ_radial = {np.mean(P_binned[mask]):.6f} fm⁻¹")
print()
print(f"  Radiation pressure P_rad(θ₁) = u × κ_radial(θ₁):")
print(f"    Mean:  {P_mean:.4f} MeV/fm³  =  {P_mean_Pa:.3e} Pa")
print(f"    Max:   {P_max:.4f} MeV/fm³  =  {P_max_Pa:.3e} Pa")
print(f"    Min:   {P_min:.4f} MeV/fm³  =  {P_min_Pa:.3e} Pa")
print(f"    Non-uniformity (RMS/mean): "
      f"{np.std(P_physical[mask])/abs(P_mean):.1%}")
print()

# Fourier decomposition in physical units
n_harmonics = 8
A_k = np.zeros(n_harmonics + 1)
theta_m = theta1_bins[mask]
P_m = P_physical[mask]
A_k[0] = np.mean(P_m)
for k in range(1, n_harmonics + 1):
    A_k[k] = 2 * np.mean(P_m * np.cos(k * theta_m))

print(f"  Fourier harmonics of P_rad (MeV/fm³):")
print(f"  {'k':>4}  {'A_k':>14}  {'|A_k|/A_0':>12}")
print(f"  {'─'*4}  {'─'*14}  {'─'*12}")
for k in range(n_harmonics + 1):
    rel = abs(A_k[k]) / abs(A_k[0]) if A_k[0] != 0 else 0
    print(f"  {k:4d}  {A_k[k]:14.6e}  {rel:12.4f}")


# ══════════════════════════════════════════════════════════════════════
#  Section 2: Required stiffness in various forms
# ══════════════════════════════════════════════════════════════════════

print()
print("-" * 70)
print("Section 2: Required restoring force in various forms")
print("-" * 70)
print()

print(f"  At equilibrium, P_in(θ₁) = P_rad(θ₁) everywhere.")
print(f"  The MEAN restoring pressure is the uniform confinement force.")
print(f"  The HARMONICS describe how the restoring force must vary.")
print()

P0 = A_k[0]  # mean pressure in MeV/fm³
P0_Pa = P0 * MEV_PER_FM3_TO_PA
P0_J_m3 = P0_Pa  # Pa = J/m³

sigma_tension = P0 * a                        # MeV/fm² (2D tension = pressure × radius)
sigma_tension_N_m = P0_Pa * a_SI              # N/m

print(f"  Mean confining pressure:")
print(f"    P₀ = {P0:.4f} MeV/fm³ = {P0_Pa:.3e} Pa")
print()
print(f"  As effective 2D surface tension (σ = P₀ × a):")
print(f"    σ = {sigma_tension:.4f} MeV/fm² = {sigma_tension_N_m:.3e} N/m")
print()
print(f"  As energy density:")
print(f"    u = {P0:.4f} MeV/fm³ = {P0_J_m3:.3e} J/m³")
print()

# For the k=2 harmonic specifically
P2 = abs(A_k[2])
P2_Pa = P2 * MEV_PER_FM3_TO_PA
print(f"  k=2 (elliptical) restoring pressure:")
print(f"    P₂ = {P2:.4f} MeV/fm³ = {P2_Pa:.3e} Pa")
print(f"    P₂/P₀ = {P2/P0:.2%}")
print()


# ══════════════════════════════════════════════════════════════════════
#  Section 3: Comparison with gravitational stiffness (reference)
# ══════════════════════════════════════════════════════════════════════

print("-" * 70)
print("Section 3: GR stiffness comparison (reference, from F24)")
print("-" * 70)
print()

einstein_stiffness = C_SI**4 / (8 * math.pi * G_N)   # N
K_gauss = 1.0 / (a_SI * R_SI)                         # m⁻²
P_GR = K_gauss * einstein_stiffness                    # Pa (force/area)

print(f"  Einstein stiffness c⁴/(8πG) = {einstein_stiffness:.3e} N")
print(f"  Gaussian curvature K = 1/(aR) = {K_gauss:.3e} m⁻²")
print(f"  GR restoring pressure ≈ K × c⁴/(8πG) = {P_GR:.3e} Pa")
print(f"  Ratio P_photon / P_GR = {P0_Pa / P_GR:.2e}")
print()


# ══════════════════════════════════════════════════════════════════════
#  Section 4: EM impedance comparison
# ══════════════════════════════════════════════════════════════════════

print("-" * 70)
print("Section 4: EM impedance comparison")
print("-" * 70)
print()

# 4a. What B field produces P₀ as magnetic pressure?
# P = B²/(2μ₀) → B = √(2μ₀P)
B_required = math.sqrt(2 * MU_0 * P0_Pa)
print(f"  4a. Magnetic pressure B²/(2μ₀) = P₀")
print(f"      B = √(2μ₀P₀) = {B_required:.4e} T")
print()

# 4b. What E field produces P₀ as electric pressure?
# P = ε₀E²/2 → E = √(2P/ε₀)
E_required = math.sqrt(2 * P0_Pa / EPS_0)
print(f"  4b. Electric pressure ε₀E²/2 = P₀")
print(f"      E = √(2P₀/ε₀) = {E_required:.4e} V/m")
print()

# Check consistency: E/c should equal B for a wave in vacuum
print(f"  4c. Consistency check: E/c = {E_required/C_SI:.4e} T")
print(f"      B from 4a = {B_required:.4e} T")
print(f"      Ratio E/(cB) = {E_required / (C_SI * B_required):.6f}"
      f"  (should be 1.0 for a plane wave)")
print()

# 4d. Schwinger critical field comparison
E_schwinger = 1.3e18   # V/m
B_schwinger = E_schwinger / C_SI
print(f"  4d. Schwinger critical field: E_S = {E_schwinger:.1e} V/m, "
      f"B_S = {B_schwinger:.2e} T")
print(f"      E_required / E_S = {E_required / E_schwinger:.1e}")
print(f"      B_required / B_S = {B_required / B_schwinger:.1e}")
print()

# 4e. EM energy density at this pressure
# For EM: u = ε₀E²/2 + B²/(2μ₀) = P (for one polarization at the wall)
# Total EM energy in the torus volume at this energy density:
E_em_in_volume = P0_Pa * V_torus_SI   # J
print(f"  4e. EM energy at pressure P₀ in torus volume V:")
print(f"      E_em = P₀ × V = {P0_Pa:.3e} × {V_torus_SI:.3e}")
print(f"          = {E_em_in_volume:.4e} J = {E_em_in_volume/MEV_TO_J:.2f} MeV")
print(f"      Photon energy = {E_photon_J:.4e} J = {E_photon_MeV:.2f} MeV")
print(f"      Ratio E_em/E_photon = {E_em_in_volume/E_photon_J:.4f}")
print()


# ══════════════════════════════════════════════════════════════════════
#  Section 5: Dimensional analysis — what combinations of μ₀, ε₀
#             give the right pressure at the torus scale?
# ══════════════════════════════════════════════════════════════════════

print("-" * 70)
print("Section 5: Dimensional analysis — EM constants at the torus scale")
print("-" * 70)
print()

# Try various combinations
combos = [
    ("E_photon / V_torus",
     E_photon_J / V_torus_SI,
     "energy density of photon in tube volume"),
    ("E_photon / (A_torus × a)",
     E_photon_J / (A_torus_SI * a_SI),
     "energy density: surface energy / tube radius"),
    ("ε₀ × (E_photon/(e×a))² / 2",
     EPS_0 * (E_photon_J / (E_CHARGE * a_SI))**2 / 2,
     "electric pressure if potential = E/e across tube"),
    ("1/(μ₀ × a²)",
     1.0 / (MU_0 * a_SI**2),
     "inverse (μ₀ × a²)"),
    ("ε₀ × c² / a²",
     EPS_0 * C_SI**2 / a_SI**2,
     "= 1/(μ₀ a²) since ε₀μ₀c² = 1"),
    ("ℏc / a⁴",
     HBAR_C_FM / a**4 * MEV_PER_FM3_TO_PA,
     "quantum pressure scale"),
    ("α × ℏc / a⁴",
     ALPHA_EM * HBAR_C_FM / a**4 * MEV_PER_FM3_TO_PA,
     "α-scaled quantum pressure"),
    ("c⁴/(8πG)",
     einstein_stiffness,
     "Einstein stiffness (not a pressure — for reference)"),
    ("Z₀ / a²",
     Z_0 / a_SI**2,
     "impedance per area"),
    ("Z₀ × c / a³",
     Z_0 * C_SI / a_SI**3,
     "impedance × velocity / volume"),
]

print(f"  Required pressure P₀ = {P0_Pa:.4e} Pa")
print()
print(f"  {'Combination':<30}  {'Value (Pa)':>14}  {'Ratio to P₀':>12}  Note")
print(f"  {'─'*30}  {'─'*14}  {'─'*12}  {'─'*40}")

for name, val, note in combos:
    ratio = val / P0_Pa if P0_Pa != 0 else float('inf')
    marker = " ◄◄◄" if 0.5 < ratio < 2.0 else ""
    print(f"  {name:<30}  {val:14.4e}  {ratio:12.4e}  {note}{marker}")

print()


# ══════════════════════════════════════════════════════════════════════
#  Section 6: The cavity radiation pressure interpretation
# ══════════════════════════════════════════════════════════════════════

print("-" * 70)
print("Section 6: Cavity radiation pressure interpretation")
print("-" * 70)
print()

# The photon's energy stored in the torus tube is E.
# If we model the tube as a cylindrical cavity of radius a and
# length 2πR (the ring circumference), the radiation pressure
# on the cylindrical wall is:
#   P = E / V_cavity  (for a 1D standing wave in the cavity)
#
# V_cavity = π a² × 2πR
V_cav = math.pi * a**2 * 2 * math.pi * R
P_cav = E_photon_MeV / V_cav   # MeV/fm³
P_cav_Pa = P_cav * MEV_PER_FM3_TO_PA

print(f"  Cylindrical cavity model:")
print(f"    Cavity: cylinder radius a, length 2πR")
print(f"    V_cav = πa² × 2πR = {V_cav:.2f} fm³")
print(f"    P_cav = E/V = {P_cav:.4f} MeV/fm³ = {P_cav_Pa:.3e} Pa")
print(f"    Ratio P_cav / P_rad = {P_cav / P_mean:.4f}")
print()

# What if the effective "height" of the cavity is a (one tube radius)?
V_eff_a = A_torus * a
P_eff_a = E_photon_MeV / V_eff_a
P_eff_a_Pa = P_eff_a * MEV_PER_FM3_TO_PA
print(f"  Surface × a model:")
print(f"    V_eff = A × a = {V_eff_a:.2f} fm³")
print(f"    P = E/V_eff = {P_eff_a:.4f} MeV/fm³ = {P_eff_a_Pa:.3e} Pa")
print(f"    Ratio P / P_rad = {P_eff_a / P_mean:.4f}")
print()


# ══════════════════════════════════════════════════════════════════════
#  Section 7: Direct μ₀, ε₀ pressure interpretation
# ══════════════════════════════════════════════════════════════════════

print("-" * 70)
print("Section 7: μ₀ and ε₀ as pressure scales")
print("-" * 70)
print()

# The user's hypothesis: μ₀ and ε₀ themselves encode the
# vacuum's resistance to EM deformation.
#
# μ₀ has dimensions [kg·m·s⁻²·A⁻²].  To make a pressure [kg·m⁻¹·s⁻²]:
#   need to multiply by [m⁻²·A²].
#   μ₀ × (current)² / (length)² = pressure (like magnetic pressure)
#
# ε₀ has dimensions [A²·s⁴·kg⁻¹·m⁻³].  To make a pressure:
#   need to multiply by [kg²·m²·s⁻⁶·A⁻²] = [voltage]² / [length]²
#   ε₀ × E_field² = pressure (like electric pressure)
#
# For a photon with energy E in tube radius a:
#   Characteristic current: I = E / (e × c × a) ... photon "current"
#   Characteristic voltage: V = E / e
#   Characteristic E-field: E_f = V / a = E / (e × a)
#   Characteristic B-field: B = μ₀ I / (2πa)  (Ampere's law)

# The photon's energy defines a characteristic EM scale:
V_char = E_photon_J / E_CHARGE            # characteristic voltage (V)
E_field_char = V_char / a_SI              # characteristic E-field (V/m)
I_char = E_CHARGE * C_SI / (2 * math.pi * a_SI)  # current loop at speed c
B_char_ampere = MU_0 * I_char / (2 * math.pi * a_SI)  # B from Ampere's law

P_electric_char = EPS_0 * E_field_char**2 / 2
P_magnetic_char = B_char_ampere**2 / (2 * MU_0)

print(f"  Characteristic scales from photon energy and tube radius:")
print(f"    V = E/e = {V_char:.3e} V")
print(f"    E_field = V/a = {E_field_char:.3e} V/m")
print(f"    I = ec/(2πa) = {I_char:.3e} A")
print(f"    B (Ampère) = μ₀I/(2πa) = {B_char_ampere:.3e} T")
print()
print(f"  Pressures from these scales:")
print(f"    P_E = ε₀E²/2 = {P_electric_char:.3e} Pa   "
      f"(ratio to P_rad: {P_electric_char/P0_Pa:.2e})")
print(f"    P_B = B²/(2μ₀) = {P_magnetic_char:.3e} Pa   "
      f"(ratio to P_rad: {P_magnetic_char/P0_Pa:.2e})")
print()

# What about using α (fine-structure constant)?
# α = e²/(4πε₀ℏc)
# ε₀ = e²/(4παℏc)
# So ε₀E² ~ (e²/(4παℏc)) × (E_photon/(e×a))²
#        = E_photon² / (4πα × ℏc × a²)
P_alpha_electric = E_photon_J**2 / (4 * math.pi * ALPHA_EM
                                     * HBAR_C_FM * FM_TO_M * MEV_TO_J
                                     * a_SI**2)
print(f"  α-based electric pressure:")
print(f"    P = E²/(4παℏc × a²) = {P_alpha_electric:.3e} Pa   "
      f"(ratio to P_rad: {P_alpha_electric/P0_Pa:.2e})")
print()


# ══════════════════════════════════════════════════════════════════════
#  Section 8: The Maxwell stress tensor decomposition
# ══════════════════════════════════════════════════════════════════════

print("-" * 70)
print("Section 8: Maxwell stress tensor at the torus wall")
print("-" * 70)
print()

# In a waveguide/cavity, the radiation pressure on the wall is:
#   P = B_tangential²/(2μ₀)  +  ε₀ E_normal² / 2
#
# For the photon mode on the torus:
# - The mode propagates helically along the surface
# - At the tube wall, the fields have both tangential and normal components
# - The E/B ratio depends on mode polarization
#
# For a TE-like mode: E_normal = 0, all pressure from B
#   P = B²/(2μ₀)
#   B = √(2μ₀P₀) = √(2 × 1.257e-6 × P₀)
#
# For a TM-like mode: B_normal at wall, E has normal component
#   P = ε₀E²/2
#   E = √(2P₀/ε₀)

print(f"  The radiation pressure P₀ = {P0_Pa:.3e} Pa can come from:")
print()
print(f"  TE-like (magnetic): B² = 2μ₀P₀")
print(f"    B = {B_required:.4e} T")
print(f"    Energy in B field in V_torus: B²/(2μ₀) × V = P₀ × V")
print(f"    = {P0_Pa * V_torus_SI / MEV_TO_J:.2f} MeV")
print()
print(f"  TM-like (electric): ε₀E² = 2P₀")
print(f"    E = {E_required:.4e} V/m")
print(f"    Energy in E field in V_torus: ε₀E²/2 × V = P₀ × V")
print(f"    = {P0_Pa * V_torus_SI / MEV_TO_J:.2f} MeV")
print()
print(f"  Both give the same energy (as they must for a single mode).")
print(f"  The photon energy is {E_photon_MeV:.2f} MeV.")
print(f"  The ratio E_em_in_V / E_photon = "
      f"{P0_Pa * V_torus_SI / E_photon_J:.4f}")
print()

# The INTERESTING case: what if E and B contribute DIFFERENTLY?
# In a cavity, the ratio of electric to magnetic energy depends on
# the mode.  For the fundamental (1,2) torus mode:
#
# The pitch angle of the helix determines the E/B decomposition
# relative to the tube normal.
pitch_angle = math.atan2(n1 * a, n2 * R)  # thin-torus approximation
print(f"  Geodesic pitch angle: α = arctan(n₁a / n₂R) = "
      f"{math.degrees(pitch_angle):.1f}°")
print(f"  (α = 0° → pure ring mode, α = 90° → pure tube mode)")
print()

# For a helical mode at pitch angle α:
# The tube-radial curvature ~ cos²α (from the ring winding component)
# The ring component of B is related to μ₀
# The tube component of E is related to ε₀
# If we decompose the pressure by pitch:
P_ring_fraction = (n2 * R)**2 / ((n1 * a)**2 + (n2 * R)**2)
P_tube_fraction = (n1 * a)**2 / ((n1 * a)**2 + (n2 * R)**2)

print(f"  Mode energy partition (flat-torus):")
print(f"    Ring fraction (n₂²R²/L²): {P_ring_fraction:.4%}")
print(f"    Tube fraction (n₁²a²/L²): {P_tube_fraction:.4%}")
print()
print(f"  If ring ↔ magnetic and tube ↔ electric:")
print(f"    P_B = {P_ring_fraction:.4f} × P₀ = "
      f"{P_ring_fraction * P0_Pa:.3e} Pa")
print(f"    P_E = {P_tube_fraction:.4f} × P₀ = "
      f"{P_tube_fraction * P0_Pa:.3e} Pa")
print(f"    B (ring) = {math.sqrt(2*MU_0*P_ring_fraction*P0_Pa):.4e} T")
print(f"    E (tube) = {math.sqrt(2*P_tube_fraction*P0_Pa/EPS_0):.4e} V/m")
print()


# ══════════════════════════════════════════════════════════════════════
#  Section 9: Summary
# ══════════════════════════════════════════════════════════════════════

print("=" * 70)
print("Summary")
print("=" * 70)
print()

print(f"1. REQUIRED RESTORING PRESSURE")
print(f"   P₀ = {P0:.4f} MeV/fm³ = {P0_Pa:.3e} Pa")
print(f"   This is the mean confining pressure the torus wall must supply")
print(f"   to hold the (1,2) photon in place.")
print()

print(f"2. CAVITY ENERGY DENSITY INTERPRETATION")
print(f"   P₀ = E_photon / V_torus  within a factor of "
      f"{P_cav/P_mean:.2f}.")
print(f"   The radiation pressure is simply the photon's energy density")
print(f"   in the tube volume, scaled by the local curvature κ_radial.")
print()

print(f"3. EM FIELD STRENGTHS")
print(f"   B = {B_required:.2e} T  ({B_required/B_schwinger:.0e} × Schwinger)")
print(f"   E = {E_required:.2e} V/m  ({E_required/E_schwinger:.0e} × Schwinger)")
print(f"   These are the fields a photon of energy {E_photon_MeV:.0f} MeV")
print(f"   would have if confined in a volume of {V_torus:.0f} fm³.")
print()

print(f"4. μ₀ AND ε₀ COMPARISON")
print(f"   μ₀ and ε₀ are not pressures by themselves.  They become")
print(f"   pressures when multiplied by field-strength-squared:")
print(f"     B²/(2μ₀) = ε₀E²/2 = P₀ = {P0_Pa:.2e} Pa")
print(f"   The fields required are {E_required/E_schwinger:.0e}× above "
      f"Schwinger — deep in the")
print(f"   non-perturbative QED regime.  At this scale, μ₀ and ε₀ may")
print(f"   not retain their vacuum values.")
print()

print(f"5. RATIO TO GR STIFFNESS")
print(f"   P₀ / P_GR = {P0_Pa/P_GR:.2e}")
print(f"   The radiation pressure is {abs(math.log10(P0_Pa/P_GR)):.0f} "
      f"orders of magnitude below bulk GR stiffness.")
print(f"   It is {math.log10(P0_Pa):.0f} orders of magnitude in absolute terms.")
print()

print(f"6. KEY RESULT")
E_em_ratio = P0_Pa * V_torus_SI / E_photon_J
print(f"   E_stored = P₀ × V = {E_em_ratio:.4f} × E_photon")
if abs(E_em_ratio - 1.0) < 0.5:
    print(f"   The radiation pressure accounts for the photon's full energy")
    print(f"   stored in the tube volume.  This is self-consistent:")
    print(f"   the photon's energy density IS the radiation pressure.")
    print(f"   No separate 'stiffness' is needed beyond the cavity boundary")
    print(f"   condition that confines the mode.")
else:
    print(f"   The stored energy differs from E_photon by a factor of "
          f"{E_em_ratio:.2f}.")
    print(f"   The discrepancy reflects the curvature weighting —")
    print(f"   κ_radial is not uniform, so P_rad ≠ E/V exactly.")
