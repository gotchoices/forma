#!/usr/bin/env python3
"""
R32 Track 1: Running of α from the Ma mode spectrum.

Enumerate all charged (Q ≠ 0) Ma modes and compute their
one-loop contribution to the running of the electromagnetic
coupling α.  Each mode with mass m_i, charge Q_i, and spin
type s_i contributes:

    Δ(1/α)(E) = -b_i Q_i² / (3π) × ln(E/m_i)   for E > m_i

where b_i depends on spin:
    scalar (spin 0):         b = 1/4
    Dirac fermion (spin ½):  b = 1
    vector (spin 1):         b = -7    (non-Abelian; for massive Abelian: +1/4)

For massive Kaluza-Klein modes in a U(1) theory, all modes contribute
with b > 0 (no asymptotic freedom), so 1/α(E) decreases
monotonically with E (α increases).

Output: α(E) from m_e to 100 TeV, compared to SM running.
"""

import sys
import os
import math
import numpy as np
from itertools import product

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_solver import self_consistent_metric
from lib.ma import (
    mode_energy, mode_charge, mode_spin,
    M_P_MEV, M_E_MEV, M_N_MEV, hbar_c_MeV_fm,
)

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064
N_MAX_EP = 8
N_MAX_NU = 0

ALPHA_0 = 1.0 / 137.036

print("=" * 70)
print("R32 Track 1: Running of α from Ma mode spectrum")
print("=" * 70)

result = self_consistent_metric(
    R_E, R_NU, R_P, sigma_ep=SIGMA_EP
)
Gt = result['Gtilde']
Gti = result['Gtilde_inv']
L = result['L']

print(f"\nCircumferences (fm):")
labels = ["L₁(e tube)", "L₂(e ring)", "L₃(ν tube)",
          "L₄(ν ring)", "L₅(p tube)", "L₆(p ring)"]
for i, lab in enumerate(labels):
    print(f"  {lab:15s} = {L[i]:12.2f}")

# ── Enumerate charged modes ──────────────────────────────────────────

print(f"\nEnumerating charged modes with n_max={N_MAX_EP} "
      f"(electron/proton), n_max_nu={N_MAX_NU} (neutrino)...")

charged_modes = []
rng_ep = range(-N_MAX_EP, N_MAX_EP + 1)
rng_nu = range(-N_MAX_NU, N_MAX_NU + 1)

for n in product(rng_ep, rng_ep, rng_nu, rng_nu, rng_ep, rng_ep):
    if all(ni == 0 for ni in n):
        continue

    Q = mode_charge(n)
    if Q == 0:
        continue

    E = mode_energy(n, Gti, L)
    if E <= 0 or E > 1e6:
        continue

    spin_h = mode_spin(n)
    charged_modes.append({
        'n': n,
        'E_MeV': E,
        'Q': Q,
        'spin_halves': spin_h,
    })

charged_modes.sort(key=lambda m: m['E_MeV'])
print(f"Found {len(charged_modes)} charged modes below 1000 TeV")

# ── Classify by spin ─────────────────────────────────────────────────
# In a U(1) Kaluza-Klein theory, the beta function coefficient for each
# charged mode depends on its spin.  For massive modes:
#   spin 0 (scalar):     b = 1/12  (complex scalar: 1/6)
#   spin ½ (fermion):    b = 1/3   (Dirac: 4/3 but we count per mode)
#   spin 1 (vector):     b = 1/12  (massive, Abelian - Proca)

def beta_coeff(spin_halves):
    """One-loop beta coefficient per charged mode."""
    if spin_halves == 0:
        return 1.0 / 3.0
    elif spin_halves == 1:
        return 4.0 / 3.0
    elif spin_halves == 2:
        return 1.0 / 3.0
    else:
        return 4.0 / 3.0

spin_counts = {}
for m in charged_modes:
    sh = m['spin_halves']
    spin_counts[sh] = spin_counts.get(sh, 0) + 1

print(f"\nSpin classification of charged modes:")
spin_labels = {0: "boson (spin 0)", 1: "fermion (spin ½)",
               2: "2×½ → 0 or 1", 3: "3×½ → ½ or 3/2"}
for sh in sorted(spin_counts):
    print(f"  {spin_labels.get(sh, f'spin_h={sh}'):25s}: {spin_counts[sh]:6d} modes")

# ── Mass distribution ────────────────────────────────────────────────

mass_bins = [0, 1, 10, 100, 500, 1000, 2000, 5000, 10000, 100000, 1e6]
print(f"\nCharged mode mass distribution:")
for i in range(len(mass_bins) - 1):
    lo, hi = mass_bins[i], mass_bins[i + 1]
    count = sum(1 for m in charged_modes if lo < m['E_MeV'] <= hi)
    if count > 0:
        print(f"  {lo:>8.0f} – {hi:>8.0f} MeV: {count:6d} modes")

# ── Compute running of 1/α ───────────────────────────────────────────

E_points_MeV = np.logspace(np.log10(0.5), np.log10(1e5), 500)

inv_alpha = np.full_like(E_points_MeV, 1.0 / ALPHA_0)

for mode in charged_modes:
    m_i = mode['E_MeV']
    Q_i = abs(mode['Q'])
    b_i = beta_coeff(mode['spin_halves'])

    mask = E_points_MeV > m_i
    inv_alpha[mask] -= (b_i * Q_i**2) / (3 * math.pi) * np.log(E_points_MeV[mask] / m_i)

alpha_running = 1.0 / inv_alpha

# ── Report key values ────────────────────────────────────────────────

print("\n" + "=" * 70)
print("RUNNING OF α FROM Ma MODE SPECTRUM")
print("=" * 70)

checkpoints = [
    ("m_e (0.511 MeV)", 0.511),
    ("1 MeV", 1.0),
    ("10 MeV", 10.0),
    ("100 MeV", 100.0),
    ("m_p (938 MeV)", 938.0),
    ("2 GeV (Ma predictive horizon)", 2000.0),
    ("10 GeV", 10000.0),
    ("m_Z (91.2 GeV)", 91200.0),
]

print(f"\n{'Energy':>35s}   1/α(E)    α(E)        Δ(1/α)")
print("-" * 70)
for label, E_val in checkpoints:
    idx = np.searchsorted(E_points_MeV, E_val)
    if idx >= len(E_points_MeV):
        idx = len(E_points_MeV) - 1
    ia = inv_alpha[idx]
    a = 1.0 / ia if ia > 0 else float('inf')
    delta = ia - 1.0 / ALPHA_0
    print(f"  {label:>33s}   {ia:7.2f}   1/{1/a:7.2f}     {delta:+7.2f}")

# ── SM comparison ────────────────────────────────────────────────────

print(f"\n{'Comparison to Standard Model':}")
print(f"  SM:  α(0) = 1/137.036,  α(m_Z) = 1/127.9")
print(f"  SM Δ(1/α) from 0 to m_Z: {137.036 - 127.9:+.1f}")
idx_mz = np.searchsorted(E_points_MeV, 91200.0)
if idx_mz < len(E_points_MeV):
    t6_delta = inv_alpha[idx_mz] - 1.0 / ALPHA_0
    print(f"  Ma Δ(1/α) from 0 to m_Z: {t6_delta:+.1f}")
    print(f"  Ma has {abs(t6_delta)/9.1:.1f}× the SM running")

# ── Count thresholds crossed ─────────────────────────────────────────

thresholds_below_2gev = sum(1 for m in charged_modes if m['E_MeV'] < 2000)
thresholds_below_mz = sum(1 for m in charged_modes if m['E_MeV'] < 91200)
print(f"\n  Charged mode thresholds below 2 GeV:  {thresholds_below_2gev}")
print(f"  Charged mode thresholds below m_Z:    {thresholds_below_mz}")

# ── Check: does 1/α reach ~24 anywhere? ──────────────────────────────

print(f"\n{'Search for 1/α ≈ 24':}")
candidates = [(E_points_MeV[i], inv_alpha[i]) for i in range(len(inv_alpha))
              if 20 < inv_alpha[i] < 28]
if candidates:
    E_24, ia_24 = min(candidates, key=lambda x: abs(x[1] - 24))
    print(f"  1/α passes through ~24 at E ≈ {E_24:.0f} MeV ({E_24/1000:.1f} GeV)")
    print(f"  Exact value at that energy: 1/α = {ia_24:.2f}")
else:
    if all(ia > 28 for ia in inv_alpha):
        print(f"  1/α never drops below 28 in scanned range")
        print(f"  Minimum 1/α = {min(inv_alpha):.2f} at E = {E_points_MeV[np.argmin(inv_alpha)]:.0f} MeV")
    elif all(ia < 20 for ia in inv_alpha[inv_alpha > 0]):
        print(f"  1/α drops below 20 — running is very fast")
        idx_cross = np.searchsorted(-inv_alpha, -24)
        if idx_cross < len(E_points_MeV):
            print(f"  1/α crosses 24 at E ≈ {E_points_MeV[idx_cross]:.0f} MeV")

# ── Does 1/α go negative (Landau pole)? ─────────────────────────────

if any(inv_alpha <= 0):
    idx_pole = np.argmax(inv_alpha <= 0)
    print(f"\n  ⚠ LANDAU POLE: 1/α → 0 at E ≈ {E_points_MeV[idx_pole]:.0f} MeV "
          f"({E_points_MeV[idx_pole]/1000:.1f} GeV)")
    print(f"  Perturbation theory breaks down at this scale.")
else:
    print(f"\n  No Landau pole in scanned range (up to {E_points_MeV[-1]/1000:.0f} GeV)")
    print(f"  Minimum 1/α = {min(inv_alpha):.2f}")

# ── Energy of proton ring (material scale) ────────────────────────────

E_compact = hbar_c_MeV_fm * 2 * math.pi / L[5]
print(f"\n  Proton ring energy scale: {E_compact:.1f} MeV")
idx_compact = np.searchsorted(E_points_MeV, E_compact)
if idx_compact < len(inv_alpha):
    print(f"  1/α at proton ring scale: {inv_alpha[idx_compact]:.2f}")

# ── Summary ──────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
n_total = len(charged_modes)
lightest = charged_modes[0] if charged_modes else None
heaviest_below_2gev = [m for m in charged_modes if m['E_MeV'] < 2000]

print(f"\nTotal charged modes enumerated: {n_total}")
if lightest:
    print(f"Lightest charged mode: {lightest['E_MeV']:.3f} MeV "
          f"(Q={lightest['Q']}, n={lightest['n']})")
if heaviest_below_2gev:
    h = heaviest_below_2gev[-1]
    print(f"Heaviest charged mode below 2 GeV: {h['E_MeV']:.1f} MeV")
print(f"Charged modes below 2 GeV: {len(heaviest_below_2gev)}")

print(f"\nα(0) = 1/{1/ALPHA_0:.3f}")
if idx_mz < len(inv_alpha) and inv_alpha[idx_mz] > 0:
    print(f"α(m_Z) from Ma = 1/{inv_alpha[idx_mz]:.2f}  "
          f"(SM: 1/127.9)")
print(f"Minimum 1/α in range = {min(inv_alpha):.2f} "
      f"at E = {E_points_MeV[np.argmin(inv_alpha)]/1000:.1f} GeV")
