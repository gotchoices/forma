#!/usr/bin/env python3
"""
R39 Track 6: Full electromagnetic interaction (electric + magnetic).

The charge circulating on the geodesic at speed c is a current loop.
Two current loops interact magnetically (Neumann formula).  For a
photon (v = c), the magnetic interaction is the SAME ORDER as the
electric — not a small correction.

The total EM interaction between two charge distributions with
tangent vectors dl̂ at each segment is:

    U_EM = Σᵢ Σⱼ dq_i × dq_j × (1 − dl̂_i · dl̂_j) / |r_i − r_j|

where the (1 − dl̂·dl̂) factor arises from:
  - Electric:  +1/r  (Coulomb repulsion for like charges)
  - Magnetic:  −(v/c)² (dl̂·dl̂)/r  (Neumann, attractive for parallel)
  - At v = c:  combined factor is (1 − dl̂·dl̂)

Physical picture (spinning top):
  - Parallel currents (dl̂·dl̂ = +1): electric + magnetic CANCEL → 0
  - Anti-parallel (dl̂·dl̂ = −1): both repulsive → factor = 2
  - Perpendicular (dl̂·dl̂ = 0): pure electric → factor = 1

This means orientation matters enormously.  Two proton-tori
approaching pole-to-pole (aligned current loops) could have
dramatically different interaction than equator-to-equator.

NOTE: Uses v = c (photon speed).  If the correct speed is
different, the magnetic contribution scales as (v/c)².
"""

import sys
import os
import math
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model import solve_shear_for_alpha, mu_12, M_P_MEV
from lib.embedded import EmbeddedSheet

# ── Proton sheet geometry ────────────────────────────────────────

R_P = 8.906
HBAR_C = 197.3269804

s56 = solve_shear_for_alpha(R_P)
mu_p = mu_12(R_P, s56)
E0_p = M_P_MEV / mu_p
L_ring = 2 * math.pi * HBAR_C / E0_p
L_tube = R_P * L_ring

p_sheet = EmbeddedSheet.from_circumferences(L_tube, L_ring)

R = p_sheet.R
a = p_sheet.a

print("=" * 70)
print("R39 Track 6: Full electromagnetic interaction")
print("=" * 70)
print()
print(f"Proton sheet: a = {a:.4f} fm, R = {R:.4f} fm, a/R = {p_sheet.aspect:.3f}")
print()

N1, N2 = 1, 2
N_SEG = 500
Q = 1.0


# ── Geodesic with tangent vectors ────────────────────────────────

def geodesic_with_tangents(sheet, n1, n2, N, phi=0.0):
    """
    Compute geodesic positions AND unit tangent vectors.

    Returns
    -------
    pos : (N, 3) — positions in fm
    dl_hat : (N, 3) — unit tangent vectors at each point
    """
    R_val, a_val = sheet.R, sheet.a
    t = np.linspace(0, 2 * math.pi, N, endpoint=False)
    theta1 = n1 * t + phi
    theta2 = n2 * t

    cos1 = np.cos(theta1)
    sin1 = np.sin(theta1)
    cos2 = np.cos(theta2)
    sin2 = np.sin(theta2)

    rho = R_val + a_val * cos1
    pos = np.stack([rho * cos2, rho * sin2, a_val * sin1], axis=-1)

    # Tangent: dr/dt = n1 ∂r/∂θ₁ + n2 ∂r/∂θ₂
    dx = -n1 * a_val * sin1 * cos2 - n2 * rho * sin2
    dy = -n1 * a_val * sin1 * sin2 + n2 * rho * cos2
    dz = n1 * a_val * cos1

    tangent = np.stack([dx, dy, dz], axis=-1)
    norms = np.linalg.norm(tangent, axis=1, keepdims=True)
    dl_hat = tangent / norms

    return pos, dl_hat


def em_interaction(pos1, dq1, dl1, pos2, dq2, dl2):
    """
    Full electromagnetic interaction energy (electric + magnetic).

    U_EM = Σ dq1_i × dq2_j × (1 − dl̂1_i · dl̂2_j) / |r1_i − r2_j|

    Returns (U_EM, U_elec, U_mag) all in units of e²/(4πε₀ fm).
    """
    dr = pos1[:, None, :] - pos2[None, :, :]         # (N1, N2, 3)
    dist = np.sqrt(np.sum(dr**2, axis=2))             # (N1, N2)

    # Dot product of tangent vectors
    dot = np.sum(dl1[:, None, :] * dl2[None, :, :], axis=2)  # (N1, N2)

    # Charge products
    qq = dq1[:, None] * dq2[None, :]                  # (N1, N2)

    U_elec = float(np.sum(qq / dist))
    U_mag = float(-np.sum(qq * dot / dist))
    U_em = U_elec + U_mag

    return U_em, U_elec, U_mag


def rotate_points(pos, dl_hat, axis, angle):
    """Rotate positions and tangent vectors around an axis."""
    c, s = math.cos(angle), math.sin(angle)
    if axis == 'x':
        R_mat = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    elif axis == 'y':
        R_mat = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    elif axis == 'z':
        R_mat = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    return pos @ R_mat.T, dl_hat @ R_mat.T


# ── Particle 1: fixed at origin ──────────────────────────────────

pos1, dl1 = geodesic_with_tangents(p_sheet, N1, N2, N_SEG, phi=0.0)
dq1 = np.full(N_SEG, Q / N_SEG)

# ── Orientation configurations ───────────────────────────────────

configs = [
    ("aligned-z",   "Aligned, separated along z (pole-to-pole)",
     'z', 0.0, 2),
    ("aligned-x",   "Aligned, separated along x (equator-to-equator)",
     'x', 0.0, 0),
    ("flipped-z",   "Flipped (180° x-rotation), separated along z",
     'z', math.pi, 2),
    ("tilted90-z",  "Tilted 90° (y-rotation), separated along z",
     'z', math.pi/2, 2),
]

d_values = np.geomspace(0.2, 50.0, 40)

print("=" * 70)
print("Sweep: U_EM / U_Coulomb for different orientations")
print("=" * 70)
print()

results = {}

for config_name, description, sep_axis, tilt_angle, sep_idx in configs:
    print(f"─── {description} ───")
    print()

    # Rotate particle 2
    if tilt_angle != 0.0:
        if sep_axis == 'z' and config_name == 'flipped-z':
            pos2_rot, dl2_rot = rotate_points(pos1, dl1, 'x', tilt_angle)
        elif config_name == 'tilted90-z':
            pos2_rot, dl2_rot = rotate_points(pos1, dl1, 'y', tilt_angle)
        else:
            pos2_rot, dl2_rot = pos1.copy(), dl1.copy()
    else:
        pos2_rot, dl2_rot = pos1.copy(), dl1.copy()

    dq2 = np.full(N_SEG, Q / N_SEG)

    print(f"  {'d (fm)':>8}  {'d/a':>6}  {'U_EM/U_C':>10}  "
          f"{'U_elec/U_C':>12}  {'U_mag/U_C':>12}  {'attractive?':>12}")
    print(f"  {'─'*8}  {'─'*6}  {'─'*10}  {'─'*12}  {'─'*12}  {'─'*12}")

    em_ratios = []
    for d in d_values:
        U_C = Q * Q / d
        pos2_shifted = pos2_rot.copy()
        pos2_shifted[:, sep_idx] += d

        U_em, U_el, U_mg = em_interaction(pos1, dq1, dl1,
                                           pos2_shifted, dq2, dl2_rot)

        em_ratio = U_em / U_C
        el_ratio = U_el / U_C
        mg_ratio = U_mg / U_C
        attr = "YES <<<" if U_em < 0 else ""
        em_ratios.append(em_ratio)

        if len(d_values) <= 20 or d < 10 or d > 40 or abs(em_ratio) < 0.1:
            print(f"  {d:8.3f}  {d/a:6.2f}  {em_ratio:10.4f}  "
                  f"{el_ratio:12.4f}  {mg_ratio:12.4f}  {attr:>12}")

    em_ratios = np.array(em_ratios)
    results[config_name] = em_ratios

    # Check for attraction
    if np.any(em_ratios < 0):
        idx_attr = np.where(em_ratios < 0)[0]
        d_attr = d_values[idx_attr[0]]
        print(f"\n  *** ATTRACTION at d = {d_attr:.3f} fm ({d_attr/a:.2f} a) ***")
        print(f"      {len(idx_attr)} of {len(d_values)} distances")
        min_idx = np.argmin(em_ratios)
        print(f"      Minimum U_EM/U_C = {em_ratios[min_idx]:.4f} at d = {d_values[min_idx]:.3f} fm")
    else:
        print(f"\n  No attraction (min U_EM/U_C = {em_ratios.min():.4f})")

    print()

# ── Summary comparison ───────────────────────────────────────────

print("=" * 70)
print("Summary: U_EM / U_Coulomb at selected distances")
print("=" * 70)
print()

print(f"  {'d (fm)':>8}  {'d/a':>6}", end="")
for name, desc, _, _, _ in configs:
    label = name[:12]
    print(f"  {label:>12}", end="")
print(f"  {'elec-only':>12}")
print(f"  {'─'*8}  {'─'*6}", end="")
for _ in configs:
    print(f"  {'─'*12}", end="")
print(f"  {'─'*12}")

sample_d = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0, 15.0, 30.0]
for d_target in sample_d:
    i = int(np.argmin(np.abs(d_values - d_target)))
    d = d_values[i]
    U_C = Q * Q / d
    print(f"  {d:8.3f}  {d/a:6.2f}", end="")
    for name, _, _, _, _ in configs:
        print(f"  {results[name][i]:12.4f}", end="")
    # Pure electric for comparison (aligned-z config)
    pos2_z = pos1.copy()
    pos2_z[:, 2] += d
    U_el = float(np.sum(dq1[:, None] * dq1[None, :] /
                         np.sqrt(np.sum((pos1[:, None, :] - pos2_z[None, :, :])**2, axis=2))))
    print(f"  {U_el/U_C:12.4f}")

# ── Conclusions ──────────────────────────────────────────────────

print()
print("=" * 70)
print("Track 6 Conclusions")
print("=" * 70)
print()
print("For a photon (v = c), the magnetic interaction is the SAME ORDER")
print("as the electric interaction.  The combined factor per segment pair")
print("is (1 − dl̂₁·dl̂₂), where dl̂ is the unit tangent to the geodesic.")
print()
print("Results by configuration:")
for name, desc, _, _, _ in configs:
    em = results[name]
    if np.any(em < 0):
        n_attr = np.sum(em < 0)
        min_val = em.min()
        min_d = d_values[np.argmin(em)]
        print(f"  {name}: ATTRACTIVE at {n_attr} distances, "
              f"min = {min_val:.4f} at d = {min_d:.2f} fm")
    else:
        print(f"  {name}: no attraction, min ratio = {em.min():.4f}")
