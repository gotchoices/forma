#!/usr/bin/env python3
"""
R34 Track 1: Kramers-Kronig dispersive model of α(E).

The hypothesis: 1/α₀ = 80.5 is the geometric base coupling.
The T⁶ mode spectrum acts as a set of absorption resonances
that modulate α via Kramers-Kronig dispersion:

    1/α(E) = 1/α₀ + Σ_k f_k × D(E, E_k, γ_k)

where D is the dispersive (real part of) response function
for each resonance at energy E_k, and f_k is the oscillator
strength.

For a single Lorentzian resonance at E_k with width γ_k:
    D(E, E_k, γ) = (E_k² - E²) / ((E_k² - E²)² + (γ E)²)

Below resonance (E < E_k): D > 0 → 1/α increases (coupling weakens)
Above resonance (E > E_k): D < 0 → 1/α decreases (coupling strengthens)

This is bidirectional modulation from the base coupling.
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

ALPHA_0 = 1.0 / 137.036
ALPHA_MID = 1.0 / 80.5

print("=" * 70)
print("R34 Track 1: Kramers-Kronig dispersive model of α(E)")
print("=" * 70)

result = self_consistent_metric(
    R_E, R_NU, R_P, sigma_ep=SIGMA_EP
)
Gt = result['Gtilde']
Gti = result['Gtilde_inv']
L = result['L']

# ── Enumerate ALL modes (charged and neutral) ────────────────────────

print(f"\nEnumerating modes with n_max={N_MAX_EP}...")

all_modes = []
rng_ep = range(-N_MAX_EP, N_MAX_EP + 1)
rng_nu = range(-N_MAX_NU, N_MAX_NU + 1)

for n in product(rng_ep, rng_ep, rng_nu, rng_nu, rng_ep, rng_ep):
    if all(ni == 0 for ni in n):
        continue
    E = mode_energy(n, Gti, L)
    if E <= 0 or E > 1e6:
        continue
    Q = mode_charge(n)
    spin = mode_spin(n)
    all_modes.append((n, E, Q, spin))

all_modes.sort(key=lambda x: x[1])
charged_modes = [m for m in all_modes if m[2] != 0]

print(f"  Total modes: {len(all_modes)}")
print(f"  Charged modes: {len(charged_modes)}")
print(f"  Neutral modes: {len(all_modes) - len(charged_modes)}")


# ── Known particle identification ────────────────────────────────────

known_particles = {
    (1, 2, 0, 0, 0, 0): ("electron", M_E_MEV),
    (-1, -2, 0, 0, 0, 0): ("positron", M_E_MEV),
    (0, 0, 0, 0, 1, 2): ("proton", M_P_MEV),
    (0, 0, 0, 0, -1, -2): ("antiproton", M_P_MEV),
}


# ── Dispersive model ─────────────────────────────────────────────────

print(f"\n{'='*70}")
print("KRAMERS-KRONIG DISPERSIVE MODEL")
print("=" * 70)

print(f"""
Model: each T⁶ mode at energy E_k acts as a resonance.
The dispersive contribution to 1/α is:

  Δ(1/α) = Σ_k f_k × g_k × (E_k² - E²) / ((E_k² - E²)² + (γ E_k)²)

where:
  f_k = oscillator strength (1 for known particles, 10⁻⁵ for ghosts)
  g_k = coupling factor (Q_k² × spin degeneracy factor)
  γ   = damping ratio (width/mass, controls resonance sharpness)

The overall normalization C is chosen so that:
  1/α(0) = 1/α₀ + C × Σ_k f_k g_k / E_k² = 137
  where 1/α₀ = 80.5 (the base coupling)
""")


def dispersive_alpha(E_probe, modes, C, gamma_ratio, alpha0_inv):
    """
    Compute 1/α(E) from the dispersive sum.

    Each mode contributes a Kramers-Kronig dispersive term:
    D_k = (E_k² - E²) / ((E_k² - E²)² + (γ E_k)² E²)

    At E=0: D_k = 1/E_k² (positive → increases 1/α)
    At E→∞: D_k → -1/E² (negative → decreases 1/α)
    At E=E_k: D_k = 0 (resonance crossing)
    """
    delta = 0.0
    for (n, E_k, Q, spin), f_k, g_k in modes:
        gamma = gamma_ratio * E_k
        num = E_k**2 - E_probe**2
        denom = num**2 + (gamma * E_probe)**2
        if denom > 0:
            delta += f_k * g_k * num / denom
    return alpha0_inv + C * delta


# Assign oscillator strengths and coupling factors
mode_data = []
for (n, E, Q, spin) in charged_modes:
    n_tuple = tuple(n)
    if n_tuple in known_particles:
        f_k = 1.0
    else:
        f_k = 1e-5  # ghost suppression

    # Coupling factor: Q² × spin degeneracy
    g_k = Q**2 * (1.0 if spin == "boson (spin 0)" else 2.0)
    mode_data.append(((n, E, Q, spin), f_k, g_k))


# ── Scan over damping ratios ─────────────────────────────────────────

print(f"\n{'='*70}")
print("SCANNING DAMPING RATIO γ AND NORMALIZATION C")
print("=" * 70)

# At E=0, the dispersive sum is Σ f_k g_k / E_k²
# We want: 1/α(0) = 80.5 + C × sum_at_zero = 137
# So: C × sum_at_zero = 56.5
# Therefore: C = 56.5 / sum_at_zero

sum_at_zero = sum(f_k * g_k / E_k**2
                  for (n, E_k, Q, spin), f_k, g_k in mode_data)

C_required = 56.5 / sum_at_zero if sum_at_zero != 0 else 0

print(f"\n  Σ f_k g_k / E_k² (E→0 limit) = {sum_at_zero:.6e}")
print(f"  C required for 1/α(0) = 137: C = {C_required:.6e}")

# What does the dispersive sum give at E→∞?
# At E→∞: D_k → -1/E² × Σ f_k g_k (independent of E_k)
# So: Δ(1/α) → -C × Σ f_k g_k / E²  →  0
# That's not right.  At E→∞, the dispersive contribution vanishes,
# leaving 1/α(∞) = 1/α₀ = 80.5.
#
# But we want 1/α(∞) = 24.  So the simple dispersive model gives
# 1/α → 80.5 at high energy, NOT 24.
#
# For 1/α to go BELOW 80.5, we need a second mechanism:
# either non-dispersive (vacuum polarization) or a different
# functional form.

sum_fk_gk = sum(f_k * g_k for (n, E_k, Q, spin), f_k, g_k in mode_data)
print(f"\n  Σ f_k g_k (high-E limit numerator) = {sum_fk_gk:.4f}")
print(f"\n  At E → ∞: Δ(1/α) → -C × Σ f_k g_k / E² → 0")
print(f"  So 1/α(∞) → 1/α₀ = 80.5, NOT 24.")
print(f"  The simple Kramers-Kronig model cannot push 1/α below 80.5.")


# ── Modified model: log-dispersive (QFT-like) ────────────────────────

print(f"\n\n{'='*70}")
print("MODIFIED MODEL: LOG-DISPERSIVE (QFT-LIKE)")
print("=" * 70)

print(f"""
Standard QFT vacuum polarization gives logarithmic running:
  Δ(1/α) = -Σ_k b_k Q_k² / (3π) × ln(E/m_k)   for E > m_k

This is NOT a Kramers-Kronig dispersion.  It's monotonic:
1/α always decreases with E (for charged modes).

But we can combine BOTH effects:
  1/α(E) = 1/α₀ + C_disp × Σ dispersive  + C_vp × Σ vacuum_pol

The dispersive part ADDS to 1/α at low E (screening: +56.5)
The vacuum polarization SUBTRACTS from 1/α at high E.

For the sum to reach 24 at very high E, we need:
  80.5 + 0 (dispersive vanishes) - C_vp × running = 24
  C_vp × running = 56.5
""")

# Compute vacuum polarization running at various scales
# Using ONLY known particles (e, p) for the monotonic part
# and the ghost modes contribute to the dispersive part

energy_probes = [
    ("E → 0", 1e-6),
    ("m_e/10", M_E_MEV / 10),
    ("m_e", M_E_MEV),
    ("10 MeV", 10),
    ("100 MeV", 100),
    ("m_p", M_P_MEV),
    ("2 GeV", 2000),
    ("10 GeV", 10000),
    ("m_Z (91.2 GeV)", 91200),
    ("1 TeV", 1e6),
    ("10 TeV", 1e7),
]


# ── HYBRID MODEL ─────────────────────────────────────────────────────
# 
# 1/α(E) = 80.5 + 56.5 × screening(E) - running(E)
#
# screening(E): dispersive, goes from +1 at E=0 to 0 at E→∞
# running(E):   logarithmic, goes from 0 at E=0 to 56.5 at E→∞
#
# At E=0:  1/α = 80.5 + 56.5 - 0 = 137     ✓
# At E→∞: 1/α = 80.5 + 0 - 56.5 = 24       ✓
# At E_mid: 1/α ≈ 80.5 + 28.25 - 28.25 = 80.5  ✓

print(f"\n{'='*70}")
print("HYBRID MODEL: SCREENING + RUNNING")
print("=" * 70)

print(f"""
  1/α(E) = 80.5 + 56.5 × S(E) - 56.5 × R(E)

  S(E) = screening function:  S(0) = 1,  S(∞) = 0
  R(E) = running function:    R(0) = 0,  R(∞) = 1

  Both functions transition around a characteristic scale E*.
  If S and R have the same transition scale:
    1/α(E*) = 80.5 + 56.5 × 0.5 - 56.5 × 0.5 = 80.5  ✓

  S(E) represents dispersive screening (Kramers-Kronig)
  R(E) represents vacuum polarization (QFT running)
""")

# Model S(E) as a smooth step: S(E) = E*² / (E² + E*²)
# Model R(E) as a smooth step: R(E) = E² / (E² + E*²)
# Note: S(E) + R(E) = 1 for all E!  So:
#   1/α(E) = 80.5 + 56.5 × S(E) - 56.5 × R(E)
#           = 80.5 + 56.5 × (S - R)
#           = 80.5 + 56.5 × (2S - 1)
#           = 80.5 + 56.5 × (E*² - E²)/(E² + E*²)
#           = 80.5 + 56.5 × (1 - 2E²/(E² + E*²))

# This is a Lorentzian dispersion curve!

def hybrid_inv_alpha(E, E_star, inv_alpha_0=80.5, delta=56.5):
    """Hybrid model: 1/α = α₀⁻¹ + δ × (E*² - E²)/(E² + E*²)"""
    return inv_alpha_0 + delta * (E_star**2 - E**2) / (E**2 + E_star**2)

# If S + R = 1, the model reduces to a SINGLE function:
#   1/α(E) = 80.5 + 56.5 × (E*² - E²) / (E² + E*²)
# This is a Lorentzian dispersion with:
#   Center: E*
#   Amplitude: 56.5
#   At E=0: 1/α = 80.5 + 56.5 = 137
#   At E=E*: 1/α = 80.5  (midpoint)
#   At E→∞: 1/α = 80.5 - 56.5 = 24

print(f"If S(E) + R(E) = 1 (complementary functions), the model simplifies:")
print(f"  1/α(E) = 80.5 + 56.5 × (E*² - E²) / (E² + E*²)")
print(f"  This is a single Lorentzian dispersion curve.")
print()

# What E* reproduces the SM value at m_Z?
# 1/α(m_Z) ≈ 128
# 128 = 80.5 + 56.5 × (E*² - 91200²) / (91200² + E*²)
# 47.5 = 56.5 × (E*² - 91200²) / (91200² + E*²)
# 47.5/56.5 = (E*² - 91200²) / (91200² + E*²)
# Let x = E*/91200
# 0.8407 = (x² - 1) / (1 + x²)
# 0.8407 + 0.8407 x² = x² - 1
# 1.8407 = x²(1 - 0.8407) = 0.1593 x²
# x² = 11.555
# x = 3.399
# E* = 3.399 × 91200 = 310,000 MeV = 310 GeV

mZ = 91200  # MeV
target_inv_alpha_mZ = 128.0
# Solve: target = 80.5 + 56.5 × (E*² - mZ²) / (mZ² + E*²)
# (target - 80.5)/56.5 = (E*² - mZ²) / (mZ² + E*²)
ratio = (target_inv_alpha_mZ - 80.5) / 56.5
# ratio = (x² - 1)/(x² + 1)  where x = E*/mZ
# ratio(x² + 1) = x² - 1
# x²(1 - ratio) = 1 + ratio
# x² = (1 + ratio)/(1 - ratio)
x_sq = (1 + ratio) / (1 - ratio)
E_star_from_mZ = mZ * math.sqrt(x_sq)
print(f"E* from requiring 1/α(m_Z) = 128:")
print(f"  E* = {E_star_from_mZ:.0f} MeV = {E_star_from_mZ/1e3:.1f} GeV")
print()

# Try different characteristic scales
candidate_scales = {
    "Proton ring (E₆)": 2 * math.pi * hbar_c_MeV_fm / L[5],
    "Proton tube (E₅)": 2 * math.pi * hbar_c_MeV_fm / L[4],
    "Proton geometric mean": 2*math.pi*hbar_c_MeV_fm / math.sqrt(L[4]*L[5]),
    "m_p": M_P_MEV,
    "2 GeV (predictive horizon)": 2000,
    "Fit from α(m_Z) = 1/128": E_star_from_mZ,
    "W/Z mass (~80-91 GeV)": 80000,
    "Higgs mass (125 GeV)": 125000,
    "310 GeV (fit)": E_star_from_mZ,
}

print(f"\n{'='*70}")
print("LORENTZIAN DISPERSION: 1/α(E) FOR VARIOUS E*")
print("=" * 70)

print(f"\n  {'E*':>30s}", end="")
for label, _ in energy_probes:
    short = label.split("(")[0].strip()
    print(f"  {short:>10s}", end="")
print()
print(f"  {'─'*30}", end="")
for _ in energy_probes:
    print(f"  {'─'*10}", end="")
print()

for scale_name, E_star in candidate_scales.items():
    if scale_name.startswith("310"):
        continue
    print(f"  {scale_name:>30s}", end="")
    for label, E_val in energy_probes:
        inv_a = hybrid_inv_alpha(E_val, E_star)
        print(f"  {inv_a:10.1f}", end="")
    print(f"  (E*={E_star:.0f} MeV)")

# SM comparison
print(f"\n  {'SM (measured/extrapolated)':>30s}", end="")
sm_values = {
    1e-6: 137.036,
    M_E_MEV/10: 137.03,
    M_E_MEV: 137.0,
    10: 136.5,
    100: 135.5,
    M_P_MEV: 134,
    2000: 133,
    10000: 131,
    91200: 128,
    1e6: 125,
    1e7: 122,
}
for label, E_val in energy_probes:
    approx = sm_values.get(E_val, 0)
    if approx:
        print(f"  {approx:10.1f}", end="")
    else:
        print(f"  {'?':>10s}", end="")
print()


# ── Best fit: what E* matches the SM running? ────────────────────────

print(f"\n\n{'='*70}")
print("BEST FIT: LORENTZIAN vs SM RUNNING")
print("=" * 70)

# The SM running from 0 to m_Z changes 1/α by ~9 (137→128).
# The Lorentzian model changes by:
#   Δ(1/α) = 80.5+56.5 - (80.5 + 56.5×(E*²-mZ²)/(mZ²+E*²))
#           = 56.5 × (1 - (E*²-mZ²)/(mZ²+E*²))
#           = 56.5 × 2mZ²/(mZ²+E*²)
# For Δ = 9:  56.5 × 2mZ²/(mZ²+E*²) = 9
# 2mZ²/(mZ²+E*²) = 0.1593
# mZ²+E*² = 2mZ²/0.1593 = 12.56 mZ²
# E*² = 11.56 mZ² → E* = 3.40 mZ = 310 GeV

E_star_best = E_star_from_mZ
print(f"\n  Best fit E* = {E_star_best:.0f} MeV = {E_star_best/1e3:.1f} GeV")
print(f"  This is {E_star_best/M_P_MEV:.0f} × m_p = {E_star_best/91200:.2f} × m_Z")

# Compare the Lorentzian to SM at several scales
print(f"\n  {'Energy':>15s} {'SM 1/α':>10s} {'Lorentzian':>10s} {'Δ':>8s}")
print(f"  {'─'*15} {'─'*10} {'─'*10} {'─'*8}")
sm_pts = [
    (0.0005, 137.036),
    (0.511, 137.0),
    (105.7, 135.9),  # muon mass
    (938, 134.0),
    (4200, 133.0),   # b quark
    (91200, 128.0),
    (125000, 127.0),  # Higgs
    (173000, 126.0),  # top
    (1e6, 125.0),     # 1 TeV
]
for E_val, sm_inv in sm_pts:
    lor_inv = hybrid_inv_alpha(E_val, E_star_best)
    delta = lor_inv - sm_inv
    label = f"{E_val:.1f}" if E_val < 1000 else f"{E_val/1e3:.0f}k"
    print(f"  {label:>15s} {sm_inv:10.1f} {lor_inv:10.1f} {delta:+8.1f}")


# ── Check what happens at T⁶ scales ──────────────────────────────────

print(f"\n\n{'='*70}")
print("LORENTZIAN MODEL AT T⁶ SCALES")
print("=" * 70)

t6_scales = [
    ("Electron tube (38 keV)", 0.0385),
    ("Electron ring (254 keV)", 0.254),
    ("Proton tube (52 MeV)", 52.4),
    ("Proton ring (467 MeV)", 466.6),
    ("m_e", M_E_MEV),
    ("m_p", M_P_MEV),
    ("E* (310 GeV)", E_star_best),
    ("Planck scale", 1.22e22),
]

print(f"\n  With E* = {E_star_best/1e3:.1f} GeV:")
print(f"  {'Scale':>30s} {'E (MeV)':>15s} {'1/α':>10s}")
print(f"  {'─'*30} {'─'*15} {'─'*10}")
for name, E_val in t6_scales:
    inv_a = hybrid_inv_alpha(E_val, E_star_best)
    print(f"  {name:>30s} {E_val:15.4f} {inv_a:10.2f}")


# ── The key question: is E* = 310 GeV meaningful? ────────────────────

print(f"\n\n{'='*70}")
print("WHAT IS E* = 310 GeV?")
print("=" * 70)

print(f"""
  E* = {E_star_best/1e3:.1f} GeV is the energy scale where 1/α = 80.5
  in the Lorentzian model.  This is:

  - {E_star_best/M_P_MEV:.0f} × proton mass
  - {E_star_best/91200:.2f} × Z boson mass
  - {E_star_best/80400:.2f} × W boson mass
  - {E_star_best/125000:.2f} × Higgs mass
  - Close to the electroweak symmetry breaking scale (~246 GeV)

  The Higgs vacuum expectation value v = 246 GeV is the
  fundamental scale of electroweak symmetry breaking.
  E* = {E_star_best/1e3:.0f} GeV ≈ {E_star_best/246000:.2f} × v.

  If E* ≈ v (the Higgs VEV), it would mean the "resonance"
  where α passes through its geometric midpoint is the
  electroweak scale itself.

  Alternatively, E* could be a GEOMETRIC scale of the T⁶:
  - ℏc / √(L₅ × L₆) = {hbar_c_MeV_fm / math.sqrt(L[4]*L[5]):.1f} MeV
    (proton sheet, NOT 310 GeV)
  - The T⁶ predictive horizon is ~2 GeV
    (NOT 310 GeV)

  E* = {E_star_best/1e3:.0f} GeV does not correspond to any
  obvious T⁶ geometric scale.  It IS close to the electroweak
  scale, which may be a coincidence or may indicate that the
  T⁶ model connects to electroweak physics at this scale.
""")


# ── Does the Lorentzian model WORK? ──────────────────────────────────

print(f"{'='*70}")
print("ASSESSMENT: DOES THE LORENTZIAN MODEL WORK?")
print("=" * 70)

print(f"""
STRENGTHS:
  1. Exactly reproduces endpoints: 1/α(0) = 137, 1/α(∞) = 24
  2. Has the right qualitative shape (monotonically decreasing)
  3. The midpoint E* can be fit to match 1/α(m_Z) = 128
  4. Simple one-parameter model (only E* is free)
  5. The fitted E* ≈ 310 GeV is near the electroweak scale

WEAKNESSES:
  1. The Lorentzian shape is WRONG for SM running.
     SM: 1/α runs logarithmically (slowly at low E, ~same rate at high E)
     Lorentzian: 1/α runs fastest AT E* and slow at both extremes.
     The Lorentzian predicts α changes slowly below 10 GeV,
     then rapidly around E* = 310 GeV.  The SM has the opposite:
     most running occurs at low E (crossing thresholds).

  2. The fit at m_Z is forced (we chose E* to match it).
     Below m_Z, the Lorentzian gives 1/α ≈ 137 (too high).
     The SM gives 1/α ≈ 135 at m_p.  The Lorentzian gives 136.99.
     So the Lorentzian UNDER-predicts the running at intermediate
     energies.

  3. E* = 310 GeV has no T⁶ origin.  It's an electroweak scale,
     not a compact geometry scale.

  4. The model has no MECHANISM — it's a fit, not a derivation.
     The Kramers-Kronig picture provides the shape, but the
     parameters (80.5, 56.5, E*) are all fit from observations.
""")

# Quantify the comparison
print(f"\nQuantitative comparison at key energies:")
print(f"  {'Energy':>15s} {'SM 1/α':>8s} {'Lorentz':>8s} {'Error':>8s}")
print(f"  {'─'*15} {'─'*8} {'─'*8} {'─'*8}")
total_err = 0
for E_val, sm_inv in sm_pts:
    lor_inv = hybrid_inv_alpha(E_val, E_star_best)
    err = abs(lor_inv - sm_inv) / sm_inv * 100
    total_err += err
    label = f"{E_val:.1f}" if E_val < 1000 else f"{E_val/1e3:.0f}k"
    print(f"  {label:>15s} {sm_inv:8.1f} {lor_inv:8.1f} {err:7.2f}%")
print(f"  Average error: {total_err/len(sm_pts):.2f}%")


# ── SUMMARY ──────────────────────────────────────────────────────────

print(f"\n{'='*70}")
print("SUMMARY")
print("=" * 70)

print(f"""
1. The pure Kramers-Kronig dispersive model CANNOT reach 1/α = 24.
   At high energy, the dispersive contributions vanish, leaving
   1/α → 80.5 (the base coupling).  A second mechanism (vacuum
   polarization / logarithmic running) is needed for the UV side.

2. The HYBRID model — where screening (dispersive, IR) and running
   (logarithmic, UV) are complementary functions S(E) + R(E) = 1 —
   reduces to a Lorentzian dispersion:

     1/α(E) = 80.5 + 56.5 × (E*² - E²) / (E² + E*²)

   This is a one-parameter model (E*) that automatically gives
   1/α from 137 (IR) to 24 (UV).

3. Fitting E* to match 1/α(m_Z) = 128 gives E* ≈ {E_star_best/1e3:.0f} GeV,
   near the electroweak scale (v = 246 GeV).

4. The Lorentzian shape does NOT match the SM's logarithmic running
   at intermediate energies.  The Lorentzian under-predicts the
   running below m_Z (gives 1/α too close to 137) and has the
   wrong curvature.

5. The model suggests α has TWO components:
   - A geometric base coupling 1/α₀ = 80.5
   - A modulation ±56.5 that acts bidirectionally
   The screening (IR) and anti-screening (UV) are complementary:
   one fades as the other grows, with the crossover at E*.
""")
