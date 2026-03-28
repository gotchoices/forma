#!/usr/bin/env python3
"""
R40 Track 1: Radiation pressure on the tube wall from a confined photon.

PHYSICAL PICTURE
================
A photon circulates inside the tube of a torus, following the (1,2)
geodesic.  At each point the photon has momentum p = E/c directed
along the path tangent.  The path curves — the tube bends it.  The
photon presses outward against the tube wall, like a ball rolling
inside a curved pipe.

The centrifugal force per unit path length is:
    F = p × v / ρ = E κ
where κ is the path curvature and E is the photon energy.

This force has components:
  - Radial in the tube cross-section (pushing against the tube wall)
  - Along the torus surface normal (pushing the torus outward/inward
    relative to the ring axis)

We decompose the curvature into these components to find the pressure
distribution on the tube wall.

The tube wall is a circle of radius a centered on the tube axis.
At each θ₁ (tube angle), the outward radial force on the wall per
unit path length is the component of the centrifugal force pointing
radially away from the tube center.

The proton sheet geometry is fully determined by r_p = 8.906 (R27 F18).
"""

import sys
import os
import math

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model import solve_shear_for_alpha, mu_12, M_P_MEV

HBAR_C_FM = 197.3269804  # MeV·fm


# ══════════════════════════════════════════════════════════════════════
#  Proton sheet geometry
# ══════════════════════════════════════════════════════════════════════

R_P = 8.906
s56 = solve_shear_for_alpha(R_P)
mu_p = mu_12(R_P, s56)
E0_p = M_P_MEV / mu_p
L_ring = 2 * math.pi * HBAR_C_FM / E0_p
L_tube = R_P * L_ring

R = L_ring / (2 * math.pi)     # major radius (fm)
a = L_tube / (2 * math.pi)     # minor radius (fm)
eps = a / R                      # = r_p

E_photon = M_P_MEV  # photon energy = proton mass (MeV)

print("=" * 70)
print("R40 Track 1: Radiation pressure on the tube wall")
print("=" * 70)
print()
print(f"Proton sheet (r_p = {R_P}, pinned by R27 F18):")
print(f"  L_tube = {L_tube:.4f} fm,  L_ring = {L_ring:.4f} fm")
print(f"  a = {a:.4f} fm (tube radius),  R = {R:.4f} fm (ring radius)")
print(f"  a/R = {eps:.3f}")
print(f"  Photon energy = {E_photon:.3f} MeV")
print()


# ══════════════════════════════════════════════════════════════════════
#  Section 1: The (1,2) geodesic on the FLAT torus
# ══════════════════════════════════════════════════════════════════════

print("-" * 70)
print("Section 1: The (1,2) geodesic on the flat torus")
print("-" * 70)
print()

# On the flat torus, the geodesic is a straight line on the universal
# cover: θ₁ = n₁ t, θ₂ = n₂ t.  The path length is:
#   ℓ = √((n₁ L_tube)² + (n₂ L_ring)²) = √(L_tube² + 4 L_ring²)
# This equals the Compton wavelength λ_C = h/(mc).

n1, n2 = 1, 2
path_flat = math.sqrt((n1 * L_tube)**2 + (n2 * L_ring)**2)
lambda_C = 2 * math.pi * HBAR_C_FM / E_photon

print(f"  Flat-torus path length: {path_flat:.6f} fm")
print(f"  Compton wavelength:     {lambda_C:.6f} fm")
print(f"  Ratio: {path_flat / lambda_C:.6f}")
print()

# The photon momentum magnitude is p = E/c = h/λ_C.
# On the flat torus, the photon moves in a straight line — no curvature,
# no centrifugal force.  ALL the curvature comes from the EMBEDDING
# of the flat torus into 3D.
#
# When we embed the flat torus as a torus of revolution, the straight
# line becomes a helix in 3D.  The helix curves, and the curvature
# creates a centrifugal force pushing the photon against the tube wall.

# The pitch angle of the geodesic:
# tan(α) = n₁ a / (n₂ R) for a torus of revolution (thin limit)
# But for a >> R, we need to be more careful.

# On the flat torus (rectangle L_tube × L_ring), the geodesic has
# slope: rise/run = L_tube / (2 L_ring) in the (θ₂, θ₁) plane.
# The tube velocity per unit t: dθ₁/dt = 1 (n₁=1)
# The ring velocity per unit t: dθ₂/dt = 2 (n₂=2)

print(f"  Geodesic pitch: the photon advances {n1} tube cycle per")
print(f"  {n2} ring cycles.  On the flat torus this is a straight line.")
print(f"  On the embedded torus it becomes a helix that curves in 3D.")
print()


# ══════════════════════════════════════════════════════════════════════
#  Section 2: 3D path and centrifugal force decomposition
# ══════════════════════════════════════════════════════════════════════

print("-" * 70)
print("Section 2: 3D curvature and centrifugal force decomposition")
print("-" * 70)
print()

N = 4000
t = np.linspace(0, 2 * math.pi, N, endpoint=False)
dt = t[1] - t[0]
theta1 = n1 * t
theta2 = n2 * t

# 3D embedding
rho = R + a * np.cos(theta1)
x = rho * np.cos(theta2)
y = rho * np.sin(theta2)
z = a * np.sin(theta1)

# Tangent dr/dt
dx = -n1 * a * np.sin(theta1) * np.cos(theta2) - n2 * rho * np.sin(theta2)
dy = -n1 * a * np.sin(theta1) * np.sin(theta2) + n2 * rho * np.cos(theta2)
dz = n1 * a * np.cos(theta1)
tangent = np.stack([dx, dy, dz], axis=-1)
speed = np.sqrt(np.sum(tangent**2, axis=1))
T_hat = tangent / speed[:, None]

# Curvature vector κ = dT/ds via central differences
dT = np.zeros_like(T_hat)
for j in range(3):
    dT[:, j] = np.gradient(T_hat[:, j], dt)
kappa_vec = dT / speed[:, None]  # dT/ds = (dT/dt)/(ds/dt)
kappa_mag = np.sqrt(np.sum(kappa_vec**2, axis=1))

# Now decompose the curvature into components relative to the tube
# cross-section.  At each point on the torus surface, define:
#
# e_r = radial unit vector in tube cross-section (points away from
#       the tube axis, i.e., away from the ring centerline)
#     = (cos θ₁ cos θ₂, cos θ₁ sin θ₂, sin θ₁)
#       (this is the outward surface normal of the torus)
#
# The centrifugal force on the tube wall is the component of
# the curvature vector along e_r:
#   κ_radial = κ · e_r
#
# Positive κ_radial = force pushing OUTWARD against the tube wall
# Negative κ_radial = force pulling inward (toward tube center)

e_r = np.stack([
    np.cos(theta1) * np.cos(theta2),
    np.cos(theta1) * np.sin(theta2),
    np.sin(theta1),
], axis=-1)

kappa_radial = np.sum(kappa_vec * e_r, axis=1)

# The centrifugal force per unit path length:
#   F_radial = E × κ_radial  (in units of MeV/fm per fm = MeV/fm²)
# For the pressure profile we care about the shape, not the absolute
# value.  Report κ_radial × ds/dt (force per unit parameter dt).

F_radial_per_dt = kappa_radial * speed

print(f"  3D speed range: [{speed.min():.4f}, {speed.max():.4f}] fm/rad")
print(f"  |κ| range: [{kappa_mag.min():.4f}, {kappa_mag.max():.4f}] fm⁻¹")
print(f"  κ_radial range: [{kappa_radial.min():.4f}, {kappa_radial.max():.4f}] fm⁻¹")
print()

print(f"  {'t/π':>6}  {'θ₁/π':>6}  {'κ_radial':>10}  {'F_rad':>10}  location")
print(f"  {'─'*6}  {'─'*6}  {'─'*10}  {'─'*10}  {'─'*15}")

sample_indices = np.linspace(0, N-1, 16, dtype=int)
for idx in sample_indices:
    th1 = theta1[idx] % (2 * math.pi)
    if th1 < 0.1 * math.pi:
        loc = "outer eq."
    elif abs(th1 - math.pi/2) < 0.2:
        loc = "top"
    elif abs(th1 - math.pi) < 0.1 * math.pi:
        loc = "inner eq."
    elif abs(th1 - 3*math.pi/2) < 0.2:
        loc = "bottom"
    else:
        loc = ""
    print(f"  {t[idx]/math.pi:6.3f}  {theta1[idx]/math.pi:6.3f}  "
          f"{kappa_radial[idx]:+10.4f}  {F_radial_per_dt[idx]:+10.4f}  {loc}")


# ══════════════════════════════════════════════════════════════════════
#  Section 3: Pressure profile on the tube wall
# ══════════════════════════════════════════════════════════════════════

print()
print("-" * 70)
print("Section 3: Pressure profile on the tube wall P(θ₁)")
print("-" * 70)
print()

# The geodesic visits each tube angle θ₁ twice per period (once on
# each ring half-circuit).  Average the radial force over visits
# to get the net pressure at each tube angle.

N_BINS = 256
theta1_bins = np.linspace(0, 2 * math.pi, N_BINS, endpoint=False)
P_binned = np.zeros(N_BINS)
counts = np.zeros(N_BINS)

theta1_mod = theta1 % (2 * math.pi)
for i in range(N):
    bin_idx = int(theta1_mod[i] / (2 * math.pi) * N_BINS) % N_BINS
    P_binned[bin_idx] += F_radial_per_dt[i]
    counts[bin_idx] += 1

mask = counts > 0
P_binned[mask] /= counts[mask]

P_mean = np.mean(P_binned[mask])
P_max = np.max(P_binned[mask])
P_min = np.min(P_binned[mask])

print(f"  Pressure (outward radial force per unit dt, averaged by θ₁):")
print()
print(f"  {'θ₁/π':>8}  {'P/⟨P⟩':>10}  {'P_raw':>12}  direction")
print(f"  {'─'*8}  {'─'*10}  {'─'*12}  {'─'*15}")

for i in range(0, N_BINS, N_BINS // 16):
    val = P_binned[i]
    ratio = val / P_mean if P_mean != 0 else 0
    direction = "← outward" if val > 0 else "→ inward"
    print(f"  {theta1_bins[i]/math.pi:8.4f}  {ratio:10.4f}  {val:12.6e}  {direction}")

print()
print(f"  Mean pressure:  {P_mean:.6e}")
print(f"  Min pressure:   {P_min:.6e}")
print(f"  Max pressure:   {P_max:.6e}")
print(f"  Max/Mean ratio: {P_max/P_mean:.4f}" if P_mean != 0 else "")
print(f"  Min/Mean ratio: {P_min/P_mean:.4f}" if P_mean != 0 else "")

n_outward = np.sum(P_binned[mask] > 0)
n_inward = np.sum(P_binned[mask] < 0)
n_total = np.sum(mask)
print()
print(f"  Outward (against tube wall): {n_outward}/{n_total} bins")
print(f"  Inward (toward tube axis):   {n_inward}/{n_total} bins")


# ══════════════════════════════════════════════════════════════════════
#  Section 4: Fourier decomposition
# ══════════════════════════════════════════════════════════════════════

print()
print("-" * 70)
print("Section 4: Fourier decomposition of P(θ₁)")
print("-" * 70)
print()

n_harmonics = 8
A_k = np.zeros(n_harmonics + 1)
B_k = np.zeros(n_harmonics + 1)

theta_masked = theta1_bins[mask]
P_masked = P_binned[mask]

A_k[0] = np.mean(P_masked)
for k in range(1, n_harmonics + 1):
    A_k[k] = 2 * np.mean(P_masked * np.cos(k * theta_masked))
    B_k[k] = 2 * np.mean(P_masked * np.sin(k * theta_masked))

print(f"  P(θ₁) = A₀ + Σ Aₖ cos(kθ₁) + Bₖ sin(kθ₁)")
print()
print(f"  {'k':>4}  {'Aₖ':>14}  {'Bₖ':>14}  {'amplitude':>14}  {'|amp|/|A₀|':>12}")
print(f"  {'─'*4}  {'─'*14}  {'─'*14}  {'─'*14}  {'─'*12}")

for k in range(n_harmonics + 1):
    amp = math.sqrt(A_k[k]**2 + B_k[k]**2)
    rel = amp / abs(A_k[0]) if A_k[0] != 0 else 0
    print(f"  {k:4d}  {A_k[k]:14.6e}  {B_k[k]:14.6e}  {amp:14.6e}  {rel:12.4f}")

print()
# Physical interpretation of each harmonic:
print("  Physical meaning of each harmonic:")
print("    k=0: uniform pressure (the mean)")
print("    k=1: cos θ₁ = shift of tube center (dipole)")
print("    k=2: cos 2θ₁ = elliptical deformation of cross-section")
print("    k=3: cos 3θ₁ = triangular deformation")
print("    k=4: cos 4θ₁ = square deformation")


# ══════════════════════════════════════════════════════════════════════
#  Section 5: Force balance assessment
# ══════════════════════════════════════════════════════════════════════

print()
print("-" * 70)
print("Section 5: Force balance assessment")
print("-" * 70)
print()

residual = P_masked - P_mean
residual_max = np.max(np.abs(residual))
residual_rms = math.sqrt(np.mean(residual**2))

print(f"  Non-uniformity of the pressure:")
print(f"    Max |P - ⟨P⟩| / |⟨P⟩|: {residual_max / abs(P_mean):.2%}")
print(f"    RMS |P - ⟨P⟩| / |⟨P⟩|: {residual_rms / abs(P_mean):.2%}")
print()

# What deformation does this drive?
# The k=1 component (cos θ₁) pushes the tube cross-section off-center.
# The k=2 component (cos 2θ₁) squeezes the circle into an ellipse.
# The actual deformation depends on the restoring force, but the
# PRESSURE PATTERN tells us which deformations are being driven.

k1_amp = math.sqrt(A_k[1]**2 + B_k[1]**2)
k2_amp = math.sqrt(A_k[2]**2 + B_k[2]**2)
k3_amp = math.sqrt(A_k[3]**2 + B_k[3]**2)

print(f"  Deformation drivers (pressure harmonics / mean):")
print(f"    k=1 (off-center shift): {k1_amp/abs(A_k[0]):.2%}")
print(f"    k=2 (elliptical):       {k2_amp/abs(A_k[0]):.2%}")
print(f"    k=3 (triangular):       {k3_amp/abs(A_k[0]):.2%}")
print()

dominant = max(range(1, n_harmonics + 1),
               key=lambda k: math.sqrt(A_k[k]**2 + B_k[k]**2))
print(f"  Dominant deformation mode: k = {dominant}")


# ══════════════════════════════════════════════════════════════════════
#  Summary
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("Track 1 Summary")
print("=" * 70)
print()
print(f"Geometry: a = {a:.2f} fm, R = {R:.4f} fm, a/R = {eps:.1f}")
print()

if n_outward == n_total:
    print(f"The photon pushes OUTWARD everywhere on the tube wall.")
    print(f"The confining medium must push inward to hold the shape.")
elif n_inward == n_total:
    print(f"The photon pushes INWARD everywhere.")
else:
    print(f"Mixed: outward in {n_outward} bins, inward in {n_inward} bins.")

print()
print(f"Pressure non-uniformity: {residual_rms / abs(P_mean):.1%} (RMS/mean)")
print(f"Dominant harmonic: k = {dominant} "
      f"({'elliptical' if dominant == 2 else 'dipole' if dominant == 1 else f'k={dominant}'})")
print()

if residual_rms / abs(P_mean) > 0.1:
    print(f"The tube wall pressure varies by {residual_rms / abs(P_mean):.0%}.")
    print(f"A perfectly circular cross-section is NOT in equilibrium.")
    print(f"Either the surface deforms, or the confining medium supplies")
    print(f"a non-uniform restoring force that matches P(θ₁).")
    print()
    print(f"The dominant deformation driver is k={dominant}.")
    if dominant == 1:
        print(f"This shifts the tube center — the cross-section moves")
        print(f"but doesn't change shape.")
    elif dominant == 2:
        print(f"This squeezes the circular cross-section into an ellipse.")
        print(f"The tube becomes elongated in one direction.")
else:
    print(f"The pressure is nearly uniform ({residual_rms / abs(P_mean):.1%}).")
    print(f"The circular cross-section is a good approximation.")
