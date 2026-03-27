#!/usr/bin/env python3
"""
R28 Track 4: High-energy modes — W, Z, Higgs search.

At 80–130 GeV, proton-sheet quantum numbers are large (|n| ~ 100–200).
We search for nearest modes, measure band density, and assess whether
matches at these energies are physically meaningful or trivially easy.

Key diagnostic: compare the gap for W/Z/Higgs to the gap for an
arbitrary "fake particle" at the same energy scale.  If both match
equally well, the T⁶ spectrum is too dense to be predictive there.
"""

import sys, os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6_solver import self_consistent_metric
from lib.t6 import mode_energy, mode_charge, mode_spin, M_P_MEV

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064

sc = self_consistent_metric(R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
Gti = sc['Gtilde_inv']
L = sc['L']

TARGETS = [
    ("W±",    80_379.0,  +1,  2, "gauge boson, spin 1"),
    ("Z⁰",   91_188.0,   0,  2, "gauge boson, spin 1"),
    ("H⁰",  125_250.0,   0,  0, "scalar, spin 0"),
]

# "Fake" particles at similar energies for the trivial-match test
FAKES = [
    ("Fake-A",  83_000.0,   0,  2, "arbitrary Q=0, spin 1"),
    ("Fake-B",  97_500.0,  +1,  0, "arbitrary Q=+1, spin 0"),
    ("Fake-C", 110_000.0,   0,  0, "arbitrary Q=0, spin 0"),
    ("Fake-D",  75_000.0,  +1,  2, "arbitrary Q=+1, spin 1"),
    ("Fake-E", 140_000.0,   0,  2, "arbitrary Q=0, spin 1"),
]

N_MAX_P = 250


def find_nearest_high_energy(target_mass, target_charge, target_spin,
                              Gti, L, n_max_p=N_MAX_P):
    """
    Search for nearest mode at high energy.

    At high energy, n2 is irrelevant (set to 0).  n1 is determined
    by n5 and the charge constraint: n1 = n5 - Q.  So the search
    is a 2D sweep over (n5, n6).
    """
    best = None
    best_err = float('inf')

    for n5 in range(-n_max_p, n_max_p + 1):
        n1 = n5 - target_charge

        n1_odd = abs(n1) % 2
        n5_odd = abs(n5) % 2
        base_odd = n1_odd + n5_odd

        n3_ok = None
        for n3_try in [0, 1]:
            total = base_odd + n3_try
            if total == target_spin:
                n3_ok = n3_try
                break
            if target_spin == 0 and total == 2:
                n3_ok = n3_try
                break
            if target_spin == 2 and total == 2:
                n3_ok = n3_try
                break
        if n3_ok is None:
            continue

        for n6 in range(-n_max_p, n_max_p + 1):
            n = np.array([n1, 0, n3_ok, 0, n5, n6], dtype=float)
            E = mode_energy(n, Gti, L)
            err = abs(E - target_mass)
            if err < best_err:
                best_err = err
                best = {
                    'n': tuple(int(x) for x in n),
                    'E': E,
                    'gap_MeV': target_mass - E,
                    'gap_pct': (target_mass - E) / target_mass * 100,
                }

    return best


def measure_band_density(E_center, Q, spin, Gti, L, window=500.0,
                          n_max_p=N_MAX_P):
    """
    Count distinct mode energies within [E_center - window, E_center + window].
    Returns average spacing in MeV.
    """
    energies = set()

    for n5 in range(-n_max_p, n_max_p + 1):
        n1 = n5 - Q
        n1_odd = abs(n1) % 2
        n5_odd = abs(n5) % 2
        base_odd = n1_odd + n5_odd

        n3_ok = None
        for n3_try in [0, 1]:
            total = base_odd + n3_try
            if total == spin or (spin == 0 and total == 2) or (spin == 2 and total == 2):
                n3_ok = n3_try
                break
        if n3_ok is None:
            continue

        for n6 in range(-n_max_p, n_max_p + 1):
            n = np.array([n1, 0, n3_ok, 0, n5, n6], dtype=float)
            E = mode_energy(n, Gti, L)
            if abs(E - E_center) <= window:
                energies.add(round(E, 2))

    sorted_E = sorted(energies)
    if len(sorted_E) < 2:
        return len(sorted_E), float('inf'), sorted_E

    spacings = [sorted_E[i+1] - sorted_E[i] for i in range(len(sorted_E) - 1)]
    avg_spacing = np.mean(spacings)
    return len(sorted_E), avg_spacing, sorted_E


print("=" * 72)
print("R28 TRACK 4: HIGH-ENERGY MODES (W, Z, HIGGS)")
print("=" * 72)


# ── Section 1: Search for W, Z, Higgs ───────────────────────────

print("\n\n── Section 1: Nearest modes for W, Z, Higgs ──\n")
print(f"  Search range: n_max = {N_MAX_P} on proton sheet")
print(f"  n₂ = 0 (electron ring; < 0.04 MeV per step)")
print()

results = {}
for name, mass, Q, spin, desc in TARGETS:
    m = find_nearest_high_energy(mass, Q, spin, Gti, L)
    results[name] = m
    print(f"  {name:6s}  ({desc})")
    print(f"    Observed: {mass:,.0f} MeV")
    print(f"    Mode:     {m['E']:,.1f} MeV  n = {m['n']}")
    print(f"    Gap:      {m['gap_MeV']:+,.1f} MeV ({m['gap_pct']:+.4f}%)")
    print()

# W/Z ratio
E_W = results['W±']['E']
E_Z = results['Z⁰']['E']
ratio_obs = 91_188.0 / 80_379.0
ratio_mode = E_Z / E_W
print(f"  W/Z mass ratio:")
print(f"    Observed:  {ratio_obs:.6f}")
print(f"    Mode:      {ratio_mode:.6f}")
print(f"    Mismatch:  {abs(ratio_mode - ratio_obs) / ratio_obs * 100:.4f}%")


# ── Section 2: Trivial-match test ────────────────────────────────

print("\n\n── Section 2: Trivial-match test (fake particles) ──\n")
print("  If fake particles match equally well, the spectrum is too")
print("  dense to distinguish real physics from noise.\n")

all_gaps = []
for name, mass, Q, spin, desc in TARGETS:
    all_gaps.append((name, mass, abs(results[name]['gap_pct'])))

for name, mass, Q, spin, desc in FAKES:
    m = find_nearest_high_energy(mass, Q, spin, Gti, L)
    all_gaps.append((name, mass, abs(m['gap_pct'])))

print(f"  {'Particle':10s} {'Mass (MeV)':>12s} {'|Gap|':>10s} {'Real?':>6s}")
print(f"  {'─'*42}")
for name, mass, gap_pct in sorted(all_gaps, key=lambda x: x[2]):
    real = "YES" if name in ('W±', 'Z⁰', 'H⁰') else "no"
    print(f"  {name:10s} {mass:12,.0f} {gap_pct:9.4f}% {real:>6s}")


# ── Section 3: Band density at W, Z, Higgs energies ─────────────

print("\n\n── Section 3: Band density at high energies ──\n")

# Compare density at 1 GeV vs 80 GeV
for E_test, label in [(1000, "1 GeV"), (80_000, "80 GeV"), (125_000, "125 GeV")]:
    n_modes, avg_sp, _ = measure_band_density(E_test, 0, 2, Gti, L,
                                               window=500.0)
    print(f"  At {label}: {n_modes} modes in ±500 MeV window, "
          f"avg spacing = {avg_sp:.1f} MeV")

print()
print("  For comparison:")
print("    W mass uncertainty:     ±12 MeV")
print("    Z mass uncertainty:     ±2 MeV")
print("    Higgs mass uncertainty: ±110 MeV")


# ── Section 4: Is the W/Z ratio special? ────────────────────────

print("\n\n── Section 4: Is the W/Z ratio geometrically special? ──\n")

# Check if the ratio m_Z/m_W = 1.1344 emerges naturally
# Compare: take ALL modes near 80 and 91 GeV and compute pairwise ratios
n_W_modes, _, W_energies = measure_band_density(80_379, +1, 2, Gti, L, window=200.0)
n_Z_modes, _, Z_energies = measure_band_density(91_188, 0, 2, Gti, L, window=200.0)

# Find all ratios near the observed W/Z ratio
close_ratios = []
for e_z in Z_energies:
    for e_w in W_energies:
        r = e_z / e_w
        if abs(r - ratio_obs) / ratio_obs < 0.001:
            close_ratios.append((e_w, e_z, r))

print(f"  Modes near W (±200 MeV): {n_W_modes}")
print(f"  Modes near Z (±200 MeV): {n_Z_modes}")
print(f"  Mode pairs with ratio within 0.1% of m_Z/m_W: {len(close_ratios)}")
if close_ratios:
    print(f"\n  First 5 matching pairs:")
    for ew, ez, r in sorted(close_ratios, key=lambda x: abs(x[2] - ratio_obs))[:5]:
        print(f"    W = {ew:,.1f},  Z = {ez:,.1f},  ratio = {r:.6f}")


# ── Section 5: Band density scaling ─────────────────────────────

print("\n\n── Section 5: How band density scales with energy ──\n")
print(f"  {'Energy':>10s} {'Modes in ±500 MeV':>20s} {'Avg spacing':>14s} {'Max gap to nearest':>20s}")
print(f"  {'─'*68}")

for E_test in [500, 1000, 2000, 5000, 10_000, 20_000, 50_000, 80_000, 125_000]:
    n_modes, avg_sp, energies = measure_band_density(E_test, 0, 2, Gti, L, window=500.0)
    if n_modes > 0:
        max_gap = max(abs(E_test - e) for e in energies) if energies else 0
        min_gap = min(abs(E_test - e) for e in energies) if energies else 0
        label = f"{E_test/1000:.0f} GeV" if E_test >= 1000 else f"{E_test} MeV"
        print(f"  {label:>10s} {n_modes:>20d} {avg_sp:>13.1f} MeV {min_gap:>13.1f} MeV")


# ── Summary ──────────────────────────────────────────────────────

print("\n\n── Summary ──\n")

W_gap = abs(results['W±']['gap_pct'])
Z_gap = abs(results['Z⁰']['gap_pct'])
H_gap = abs(results['H⁰']['gap_pct'])
avg_fake = np.mean([g for _, _, g in all_gaps if _ not in ('W±', 'Z⁰', 'H⁰')])

print(f"  W± gap:  {W_gap:.4f}%")
print(f"  Z⁰ gap:  {Z_gap:.4f}%")
print(f"  H⁰ gap:  {H_gap:.4f}%")
print(f"  Avg fake gap: {avg_fake:.4f}%")
print()

if max(W_gap, Z_gap, H_gap) < 0.01 and avg_fake < 0.01:
    print("  CONCLUSION: The T⁶ spectrum is too dense at these energies.")
    print("  Both real and fake particles match to < 0.01%.")
    print("  The model is NOT predictive above a few GeV.")
elif max(W_gap, Z_gap, H_gap) < avg_fake * 0.1:
    print("  CONCLUSION: Real particles match significantly better than fakes.")
    print("  The T⁶ geometry may encode something about electroweak masses.")
else:
    print("  CONCLUSION: Real and fake particles match comparably.")
    print("  The T⁶ spectrum's high-energy density makes individual")
    print("  mass matches non-diagnostic.")
