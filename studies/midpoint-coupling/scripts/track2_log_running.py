#!/usr/bin/env python3
"""
R34 Track 2: Logarithmic running from 1/α₀ = 80.

Hypothesis: 1/α₀ = 80 is the bare geometric coupling
(from the weighted gauge partition, R32 F23).  Standard
QFT vacuum polarization screens the charge at low energy,
pushing 1/α from 80 up to 137.

Use the full T⁶ charged-mode spectrum (from R32 Track 1)
with a uniform ghost suppression factor f, and:

1. Fit f so that 1/α(E→0) = 137
2. With this f, compute 1/α(m_Z) — does it match 128?
3. Report f and compare to the R31/R32 constraint (~10⁻⁵)
"""

import sys
import os
import math
import numpy as np
from itertools import product

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6_solver import self_consistent_metric
from lib.t6 import (
    mode_energy, mode_charge, mode_spin,
    M_P_MEV, M_E_MEV, M_N_MEV, hbar_c_MeV_fm,
)

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064
N_MAX_EP = 8
N_MAX_NU = 0

ALPHA_OBS = 1.0 / 137.036
INV_ALPHA_OBS = 137.036
INV_ALPHA_MZ = 128.0
INV_ALPHA_BASE = 80.0
M_Z = 91187.6  # MeV

print("=" * 70)
print("R34 Track 2: Logarithmic running from 1/α₀ = 80")
print("=" * 70)

result = self_consistent_metric(
    R_E, R_NU, R_P, sigma_ep=SIGMA_EP
)
Gti = result['Gtilde_inv']
L = result['L']


# ── Enumerate charged modes ──────────────────────────────────────────

print(f"\nEnumerating charged modes...")
charged_modes = []
rng_ep = range(-N_MAX_EP, N_MAX_EP + 1)
rng_nu = range(-N_MAX_NU, N_MAX_NU + 1)

known_particle_modes = {
    (1, 2, 0, 0, 0, 0),
    (-1, -2, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 2),
    (0, 0, 0, 0, -1, -2),
}

for n in product(rng_ep, rng_ep, rng_nu, rng_nu, rng_ep, rng_ep):
    if all(ni == 0 for ni in n):
        continue
    Q = mode_charge(n)
    if Q == 0:
        continue
    E = mode_energy(n, Gti, L)
    if E <= 0 or E > 1e6:
        continue
    spin = mode_spin(n)
    is_known = tuple(n) in known_particle_modes
    charged_modes.append((n, E, Q, spin, is_known))

charged_modes.sort(key=lambda x: x[1])
print(f"  Total charged modes: {len(charged_modes)}")
print(f"  Known particles: {sum(1 for m in charged_modes if m[4])}")
print(f"  Ghost modes: {sum(1 for m in charged_modes if not m[4])}")


# ── Running calculation ──────────────────────────────────────────────

def compute_inv_alpha(E_probe, modes, f_ghost, inv_alpha_bare, cutoff):
    """
    Compute 1/α(E_probe) using one-loop QFT running.

    The bare coupling is defined at the cutoff scale Λ.
    Running DOWN from Λ to E_probe:

      1/α(E) = 1/α(Λ) + Σ_k (b_k Q_k²)/(3π) × ln(Λ/max(E, m_k))

    Each mode with mass m_k and E < Λ contributes screening
    (increases 1/α) at energies below its mass.

    b_k = 1 for Dirac fermions (spin ½)
    b_k = 1/4 for scalars (spin 0)
    b_k = 1/3 for "two halves → 0 or 1" (average)
    """
    delta = 0.0
    for (n, m_k, Q, spin, is_known) in modes:
        if m_k >= cutoff:
            continue

        f_k = 1.0 if is_known else f_ghost

        if spin == "fermion (spin ½)":
            b_k = 1.0
        elif spin == "boson (spin 0)":
            b_k = 1.0 / 4.0
        else:
            b_k = 1.0 / 3.0

        E_eff = max(E_probe, m_k)
        if E_eff < cutoff:
            delta += f_k * b_k * Q**2 / (3 * math.pi) * math.log(cutoff / E_eff)

    return inv_alpha_bare + delta


# ── Fit the ghost suppression factor ─────────────────────────────────

print(f"\n{'='*70}")
print("FITTING GHOST SUPPRESSION FACTOR")
print("=" * 70)

# We need: 1/α(E→0) = 137.036
# Try a range of cutoff scales and find f for each

cutoff_scales = [
    ("1 TeV", 1e6),
    ("10 TeV", 1e7),
    ("100 TeV", 1e8),
    ("1 PeV", 1e9),
]

from scipy.optimize import brentq

print(f"\n  Base coupling: 1/α₀ = {INV_ALPHA_BASE}")
print(f"  Target: 1/α(0) = {INV_ALPHA_OBS}")
print(f"  Need: Δ(1/α) = {INV_ALPHA_OBS - INV_ALPHA_BASE:.3f}")

results_by_cutoff = {}

for cutoff_name, cutoff in cutoff_scales:
    # Find f such that 1/α(m_e/100) ≈ 137.036
    E_low = M_E_MEV / 100  # effectively E → 0

    def residual(log_f):
        f = 10**log_f
        inv_a = compute_inv_alpha(E_low, charged_modes, f, INV_ALPHA_BASE, cutoff)
        return inv_a - INV_ALPHA_OBS

    # Check bounds
    inv_a_f0 = compute_inv_alpha(E_low, charged_modes, 0, INV_ALPHA_BASE, cutoff)
    inv_a_f1 = compute_inv_alpha(E_low, charged_modes, 1e-3, INV_ALPHA_BASE, cutoff)

    print(f"\n  Cutoff = {cutoff_name}:")
    print(f"    f=0 (SM only): 1/α(0) = {inv_a_f0:.2f}")
    print(f"    f=10⁻³:        1/α(0) = {inv_a_f1:.2f}")

    if inv_a_f0 > INV_ALPHA_OBS:
        print(f"    SM alone overshoots! No ghost modes needed at this cutoff.")
        continue

    if inv_a_f1 < INV_ALPHA_OBS:
        # Try larger f
        inv_a_f2 = compute_inv_alpha(E_low, charged_modes, 1e-1, INV_ALPHA_BASE, cutoff)
        print(f"    f=10⁻¹:        1/α(0) = {inv_a_f2:.2f}")

    try:
        log_f_fit = brentq(residual, -8, -1, xtol=1e-10)
        f_fit = 10**log_f_fit

        # Now compute 1/α at m_Z with this f
        inv_a_mZ = compute_inv_alpha(M_Z, charged_modes, f_fit, INV_ALPHA_BASE, cutoff)

        print(f"    Fitted f = {f_fit:.6e}  (= 10^{log_f_fit:.3f})")
        print(f"    1/α(m_Z) with this f: {inv_a_mZ:.2f}")
        print(f"    Target 1/α(m_Z): {INV_ALPHA_MZ:.1f}")
        print(f"    Discrepancy: {inv_a_mZ - INV_ALPHA_MZ:+.2f}")

        results_by_cutoff[cutoff_name] = (f_fit, inv_a_mZ, cutoff)

    except Exception as e:
        print(f"    Fit failed: {e}")


# ── Detailed running with best fit ───────────────────────────────────

print(f"\n\n{'='*70}")
print("DETAILED RUNNING CURVE")
print("=" * 70)

# Use 1 TeV cutoff (most conservative)
best_cutoff_name = list(results_by_cutoff.keys())[0] if results_by_cutoff else None

if best_cutoff_name:
    f_best, inv_a_mZ_best, cutoff_best = results_by_cutoff[best_cutoff_name]

    print(f"\n  Using cutoff = {best_cutoff_name}, f = {f_best:.4e}")

    energy_points = [
        ("0 (m_e/100)", M_E_MEV / 100),
        ("m_e (0.511 MeV)", M_E_MEV),
        ("1 MeV", 1.0),
        ("m_μ (105.7 MeV)", 105.658),
        ("m_π (135 MeV)", 134.977),
        ("m_τ (1.777 GeV)", 1776.86),
        ("m_c (1.27 GeV)", 1270),
        ("m_b (4.18 GeV)", 4180),
        ("m_p (938 MeV)", M_P_MEV),
        ("10 GeV", 10000),
        ("m_Z (91.2 GeV)", M_Z),
        ("m_H (125 GeV)", 125000),
        ("m_t (173 GeV)", 173000),
        ("500 GeV", 500000),
        ("1 TeV", 1e6),
    ]

    # SM comparison values (approximate)
    sm_values = {
        M_E_MEV / 100: 137.036,
        M_E_MEV: 137.0,
        1.0: 136.9,
        105.658: 135.9,
        134.977: 135.8,
        1776.86: 133.5,
        1270: 133.8,
        4180: 133.0,
        M_P_MEV: 134.0,
        10000: 131.0,
        M_Z: 128.0,
        125000: 127.0,
        173000: 126.0,
        500000: 124.5,
        1e6: 123.5,
    }

    print(f"\n  {'Energy':>25s} {'T⁶ 1/α':>10s} {'SM 1/α':>10s} {'Δ':>8s}")
    print(f"  {'─'*25} {'─'*10} {'─'*10} {'─'*8}")

    for name, E_val in energy_points:
        inv_a = compute_inv_alpha(E_val, charged_modes, f_best, INV_ALPHA_BASE, cutoff_best)
        sm_inv = sm_values.get(E_val, None)
        if sm_inv:
            delta = inv_a - sm_inv
            print(f"  {name:>25s} {inv_a:10.2f} {sm_inv:10.1f} {delta:+8.2f}")
        else:
            print(f"  {name:>25s} {inv_a:10.2f}")


# ── Compare all cutoffs ──────────────────────────────────────────────

print(f"\n\n{'='*70}")
print("COMPARISON ACROSS CUTOFF SCALES")
print("=" * 70)

if results_by_cutoff:
    print(f"\n  {'Cutoff':>15s} {'f':>12s} {'1/α(m_Z)':>10s} {'Δ from 128':>12s} {'f/10⁻⁵':>10s}")
    print(f"  {'─'*15} {'─'*12} {'─'*10} {'─'*12} {'─'*10}")

    for name, (f_val, inv_mZ, cutoff) in results_by_cutoff.items():
        print(f"  {name:>15s} {f_val:12.4e} {inv_mZ:10.2f} {inv_mZ-128:+12.2f} {f_val/1e-5:10.2f}")


# ── Decompose the running ────────────────────────────────────────────

print(f"\n\n{'='*70}")
print("DECOMPOSITION: SM vs GHOST CONTRIBUTIONS")
print("=" * 70)

if best_cutoff_name:
    f_best, _, cutoff_best = results_by_cutoff[best_cutoff_name]
    E_low = M_E_MEV / 100

    # SM-only running (f=0)
    inv_a_sm_only = compute_inv_alpha(E_low, charged_modes, 0, INV_ALPHA_BASE, cutoff_best)
    sm_contribution = inv_a_sm_only - INV_ALPHA_BASE

    # Full running
    inv_a_full = compute_inv_alpha(E_low, charged_modes, f_best, INV_ALPHA_BASE, cutoff_best)
    total_screening = inv_a_full - INV_ALPHA_BASE
    ghost_contribution = total_screening - sm_contribution

    print(f"\n  Running from 1/α₀ = {INV_ALPHA_BASE} to 1/α(0):")
    print(f"    SM fermions alone:    +{sm_contribution:.2f}")
    print(f"    Ghost modes (f={f_best:.2e}): +{ghost_contribution:.2f}")
    print(f"    Total screening:      +{total_screening:.2f}")
    print(f"    Final 1/α(0):         {inv_a_full:.3f}")

    print(f"\n    SM fraction: {sm_contribution/total_screening*100:.1f}%")
    print(f"    Ghost fraction: {ghost_contribution/total_screening*100:.1f}%")

    # At m_Z
    inv_a_sm_mZ = compute_inv_alpha(M_Z, charged_modes, 0, INV_ALPHA_BASE, cutoff_best)
    inv_a_full_mZ = compute_inv_alpha(M_Z, charged_modes, f_best, INV_ALPHA_BASE, cutoff_best)
    sm_at_mZ = inv_a_sm_mZ - INV_ALPHA_BASE
    ghost_at_mZ = (inv_a_full_mZ - INV_ALPHA_BASE) - sm_at_mZ

    print(f"\n  At m_Z = 91.2 GeV:")
    print(f"    SM screening:    +{sm_at_mZ:.2f}")
    print(f"    Ghost screening: +{ghost_at_mZ:.2f}")
    print(f"    Total:           +{sm_at_mZ + ghost_at_mZ:.2f}")
    print(f"    1/α(m_Z):        {inv_a_full_mZ:.2f}  (target: 128)")


# ── SUMMARY ──────────────────────────────────────────────────────────

print(f"\n\n{'='*70}")
print("SUMMARY")
print("=" * 70)

if results_by_cutoff:
    f_best, inv_mZ_best, _ = list(results_by_cutoff.values())[0]
    print(f"""
Starting from the geometric base coupling 1/α₀ = 80:

1. GHOST SUPPRESSION FACTOR:
   f = {f_best:.4e} (= {f_best/1e-5:.2f} × 10⁻⁵)
   This is the suppression needed for ghost modes to produce
   the observed screening from 1/80 to 1/137.
   R31/R32 constraint: f ~ 10⁻⁵ (same order of magnitude)

2. 1/α AT m_Z:
   Model: {inv_mZ_best:.2f}
   Measured: 128.0
   Discrepancy: {inv_mZ_best - 128:+.2f}

3. INTERPRETATION:
""")
    if abs(inv_mZ_best - 128) < 2:
        print(f"   STRONG RESULT: The model matches 1/α(m_Z) within"
              f" {abs(inv_mZ_best - 128):.1f} units.")
        print(f"   The ghost suppression factor f = {f_best:.2e} is")
        print(f"   independently derived from the running (not from Lamb shift).")
        print(f"   If this matches the Lamb shift constraint, it provides")
        print(f"   an independent cross-check on the T⁶ model.")
    elif abs(inv_mZ_best - 128) < 10:
        print(f"   MODERATE RESULT: The model is within {abs(inv_mZ_best-128):.0f} units")
        print(f"   of the measured value.  The qualitative picture works")
        print(f"   but the mode spectrum may need refinement.")
    else:
        print(f"   NULL RESULT: The model misses by {abs(inv_mZ_best-128):.0f} units.")
        print(f"   The logarithmic running from 1/80 does not reproduce")
        print(f"   the SM running at m_Z.  The weighted gauge partition")
        print(f"   giving 1/80 may be a coincidence.")
else:
    print(f"\n  No successful fit found.")
