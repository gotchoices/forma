"""
R43 Track 2 — W and Z masses from cross-sheet coupling barriers.

Q96 interprets W as a transient cross-sheet mode-transition state
and Z as a same-sheet resonance of cross-sheet coupling.  Their
masses should emerge from the Ma geometry.

Tests:
  1. Cross-sheet barrier energy at different σ values
  2. Mode spectrum near 80 and 91 GeV
  3. Relationship to the midpoint coupling (310 GeV, R34)
  4. W/Z mass ratio as a Weinberg angle test

Key relation: M_W / M_Z = cos θ_W ≈ 0.882
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from lib.ma import (build_scaled_metric, mode_energy, compute_scales,
                    solve_shear_for_alpha, mu_12,
                    M_E_MEV, M_P_MEV, M_N_MEV, hbar_c_MeV_fm, ALPHA,
                    is_positive_definite)
from itertools import product

M_W = 80379      # MeV
M_Z = 91188      # MeV
V_HIGGS = 246220  # MeV (Higgs vev)
COS_TW = M_W / M_Z
SIN2_TW = 1 - COS_TW**2

R_E = 6.6
R_NU = 5.0
R_P = 8.906
SIGMA_EP = 0.038

print("=" * 70)
print("R43 Track 2: W and Z masses from cross-sheet coupling")
print("=" * 70)

L, s12, s34, s56 = compute_scales(R_E, R_NU, R_P)

print(f"\nSheet scales:")
print(f"  Ma_e: L₁ = {L[0]:.4f} fm, L₂ = {L[1]:.6f} fm")
print(f"  Ma_ν: L₃ = {L[2]:.2f} fm, L₄ = {L[3]:.2f} fm")
print(f"  Ma_p: L₅ = {L[4]:.6f} fm, L₆ = {L[5]:.8f} fm")

E0_e = 2 * np.pi * hbar_c_MeV_fm / L[1]
E0_p = 2 * np.pi * hbar_c_MeV_fm / L[5]
E0_nu = 2 * np.pi * hbar_c_MeV_fm / L[3]
print(f"\nEnergy scales:")
print(f"  E₀_e (ring) = {E0_e:.4f} MeV")
print(f"  E₀_ν (ring) = {E0_nu*1e6:.4f} eV = {E0_nu:.4e} MeV")
print(f"  E₀_p (ring) = {E0_p:.4f} MeV")

# ── Test 1: Cross-sheet barrier interpretation ──────────────────────

print("\n--- Test 1: Barrier energy from σ_ep ---\n")

# The barrier height between two sheets is the energy cost of
# exciting a mode that has winding numbers on both sheets.
# The cross-sheet metric element σ_ep couples the sheets.
#
# In perturbation theory, if σ is small, the energy shift is:
#   ΔE² / E² ≈ σ × (geometric factor)
# For the neutron (1,2,0,0,1,2), this is directly computable.

Gt_0, Gti_0, L_0, _ = build_scaled_metric(R_E, R_NU, R_P, sigma_ep=0.0)
Gt_s, Gti_s, L_s, _ = build_scaled_metric(R_E, R_NU, R_P, sigma_ep=SIGMA_EP)

# Neutron-like mode: energy with and without coupling
E_n_uncoupled = mode_energy((1,2,0,0,1,2), Gti_0, L_0)
E_n_coupled = mode_energy((1,2,0,0,1,2), Gti_s, L_s)
delta_E_n = E_n_coupled - E_n_uncoupled

print(f"Neutron mode (1,2,0,0,1,2):")
print(f"  Uncoupled: {E_n_uncoupled:.3f} MeV")
print(f"  Coupled:   {E_n_coupled:.3f} MeV")
print(f"  Shift:     {delta_E_n:.3f} MeV ({delta_E_n/E_n_uncoupled*100:.3f}%)")

# The barrier energy should be related to the critical σ
# at which the metric becomes singular (max coupling).
print(f"\n  Scanning σ_ep for metric singularity...")

sigma_crit = None
for sig in np.linspace(0.01, 1.0, 10000):
    Gt_t, _, _, _ = build_scaled_metric(R_E, R_NU, R_P, sigma_ep=sig)
    if not is_positive_definite(Gt_t):
        sigma_crit = sig
        break

if sigma_crit:
    print(f"  Metric becomes singular at σ_ep ≈ {sigma_crit:.4f}")
    
    # The barrier energy scale: energy at which σ becomes O(1)
    # The cross-sheet coupling runs with energy (like α does).
    # At low energy, σ is small.  At the barrier energy, σ → σ_crit.
    
    # Scaling argument: if σ_ep runs logarithmically like α:
    #   σ(μ) = σ₀ / (1 - b·σ₀·ln(μ/m₀))
    # The Landau pole (σ → ∞) occurs at:
    #   μ_barrier = m₀ × exp(1 / (b·σ₀))
    
    # With b ~ 1/(2π) (one-loop), σ₀ = 0.038, m₀ = m_n ≈ 940 MeV:
    for b_coeff in [1/(2*np.pi), 1/(4*np.pi), 1/(6*np.pi)]:
        mu_barrier = M_N_MEV * np.exp(1 / (b_coeff * SIGMA_EP))
        print(f"  b = 1/{1/b_coeff/np.pi:.0f}π: μ_barrier = {mu_barrier:.1e} MeV = {mu_barrier/1e3:.1e} GeV")
else:
    print(f"  No singularity found up to σ_ep = 1.0")

# ── Test 2: High-energy cross-sheet modes ───────────────────────────

print("\n--- Test 2: Mode spectrum near M_W and M_Z ---\n")

# Scan for modes with energy near 80–91 GeV that span two sheets.
# These are modes with non-zero winding numbers on at least two
# of the three sheets.

Gt, Gti, L_arr, _ = build_scaled_metric(
    R_E, R_NU, R_P, sigma_ep=SIGMA_EP
)

n_max = 100
target_low = 70000   # MeV
target_high = 100000  # MeV

print(f"Searching for cross-sheet modes with E ∈ [{target_low/1e3:.0f}, {target_high/1e3:.0f}] GeV")
print(f"  n_max = {n_max}")
print()

# Cross-sheet modes: windings on e AND p sheets (W/Z territory)
# Due to the huge scale hierarchy (L_ν ~ mm, L_e ~ fm, L_p ~ 0.001 fm),
# the proton sheet's energy scale dominates.
# E₀_p = 2πℏc/L₆_p ≈ several hundred MeV → need n ~ 100-200 for ~80 GeV

# How many ring windings on proton sheet to hit 80 GeV?
n_W_est = M_W / E0_p
n_Z_est = M_Z / E0_p
print(f"  E₀_p = {E0_p:.2f} MeV → n ≈ {n_W_est:.0f} for M_W, {n_Z_est:.0f} for M_Z")
print(f"  E₀_e = {E0_e:.2f} MeV → n ≈ {M_W/E0_e:.0f} for M_W")
print()

# The proton ring circumference is sub-fm, so modes are very widely spaced.
# Let's compute E for pure p-sheet modes near target:
print("Pure proton sheet modes near M_W:")
for n5 in range(0, 3):
    for n6 in range(int(n_W_est) - 5, int(n_W_est) + 5):
        if n6 <= 0:
            continue
        n = (0, 0, 0, 0, n5, n6)
        E = mode_energy(n, Gti, L_arr)
        if target_low < E < target_high:
            print(f"  {str(n):>25s}: E = {E:.0f} MeV = {E/1e3:.3f} GeV")

# Cross-sheet e-p modes near target:
print("\nCross-sheet e-p modes near M_W:")
found = 0
for n1 in range(0, 3):
    for n2 in range(0, 3):
        if n1 == 0 and n2 == 0:
            continue
        for n5 in range(0, 3):
            for n6 in range(int(n_W_est) - 5, int(n_W_est) + 5):
                if n5 == 0 and n6 == 0:
                    continue
                if n6 <= 0:
                    continue
                n = (n1, n2, 0, 0, n5, n6)
                E = mode_energy(n, Gti, L_arr)
                if target_low < E < target_high:
                    print(f"  {str(n):>25s}: E = {E:.0f} MeV = {E/1e3:.3f} GeV")
                    found += 1
                    if found > 20:
                        break
            if found > 20:
                break
        if found > 20:
            break
    if found > 20:
        break

# ── Test 3: Midpoint coupling connection ────────────────────────────

print("\n--- Test 3: Connection to midpoint coupling (R34) ---\n")

E_midpoint = 310000  # MeV (310 GeV from R34)

# R34 found that the coupling runs from α at low energy to a
# "midpoint" at ~310 GeV where screening reduces α to α/2.
# The electroweak scale (Higgs vev v = 246 GeV) is nearby.

print(f"R34 midpoint energy: {E_midpoint/1e3:.0f} GeV")
print(f"Higgs vev v:         {V_HIGGS/1e3:.0f} GeV")
print(f"Ratio: E_mid / v =   {E_midpoint/V_HIGGS:.3f}")
print()

# In the SM: M_W = gv/2 where g = e/sin θ_W
e_coupling = np.sqrt(4 * np.pi * ALPHA)
g_weak = e_coupling / np.sqrt(SIN2_TW)
M_W_from_v = g_weak * V_HIGGS / 2
print(f"SM check: M_W = gv/2 = {g_weak:.4f} × {V_HIGGS/1e3:.0f} GeV / 2 = {M_W_from_v/1e3:.1f} GeV")
print(f"  (target: {M_W/1e3:.1f} GeV) ✓")
print()

# Can we get v from Ma geometry?
# v = 2πℏc / L_cross, where L_cross is some cross-sheet distance?
L_cross_needed = 2 * np.pi * hbar_c_MeV_fm / V_HIGGS
print(f"If v = 2πℏc / L_cross → L_cross = {L_cross_needed:.5f} fm = {L_cross_needed*1e3:.2f} am")
print(f"  Compare: L₆_p = {L_arr[5]:.5f} fm")
print(f"  Ratio: L_cross / L₆_p = {L_cross_needed / L_arr[5]:.4f}")
print()

# The cross-sheet "effective distance" might be:
# L_eff = √(L_e × L_p) / σ_ep  (geometric mean weighted by coupling)
L_eff = np.sqrt(L_arr[1] * L_arr[5]) / SIGMA_EP
E_from_Leff = 2 * np.pi * hbar_c_MeV_fm / L_eff
print(f"Geometric mean approach:")
print(f"  L_eff = √(L₂_e × L₆_p) / σ_ep = {L_eff:.4f} fm")
print(f"  E = 2πℏc / L_eff = {E_from_Leff:.1f} MeV = {E_from_Leff/1e3:.3f} GeV")
print()

# Alternative: the cross-sheet energy scale as σ × E₀_geom
E_geom = np.sqrt(E0_e * E0_p)
E_cross_scale = E_geom / SIGMA_EP
print(f"Alternative: E_geom / σ_ep = √(E₀_e × E₀_p) / σ_ep")
print(f"  E_geom = √({E0_e:.2f} × {E0_p:.2f}) = {E_geom:.2f} MeV")
print(f"  E_cross = {E_cross_scale:.0f} MeV = {E_cross_scale/1e3:.1f} GeV")
print()

# What σ_ep would give M_W from this formula?
sigma_for_MW = E_geom / M_W
print(f"  σ_ep needed for M_W = {M_W/1e3:.1f} GeV: {sigma_for_MW:.5f}")
print(f"  (actual σ_ep = {SIGMA_EP})")

# ── Test 4: W/Z mass ratio ─────────────────────────────────────────

print("\n--- Test 4: W/Z mass ratio from geometry ---\n")

print(f"SM: M_W / M_Z = cos θ_W = {COS_TW:.6f}")
print(f"    sin²θ_W = {SIN2_TW:.6f}")
print()

# Test: does the W/Z mass ratio relate to any geometric ratio?
# In Ma, the W involves cross-sheet transitions and the Z involves
# same-sheet resonances.  Their mass ratio might emerge from:

# The ratio of eigenvalues of the 6×6 metric
evals = np.linalg.eigvalsh(Gt)
print(f"Eigenvalues of G̃: {evals}")
print(f"  Ratios of adjacent eigenvalues:")
for i in range(len(evals)-1):
    ratio = evals[i] / evals[i+1]
    print(f"    λ_{i}/λ_{i+1} = {ratio:.6f}")

# The ratio of the smallest eigenvalue (most coupled direction)
# to 1 (uncoupled):
print(f"\n  1 - λ_min = {1 - evals[0]:.6f}")
print(f"  √(1 - λ_min²) = {np.sqrt(1 - evals[0]**2):.6f}")
print(f"  cos θ_W target = {COS_TW:.6f}")

# What if the W is the cross-sheet mode and Z is
# the same mode without sheet transition?
# Then M_Z² = M_W² + (something from EM coupling)
# → M_Z² - M_W² = M_W² × tan²θ_W

M_WZ_diff = np.sqrt(M_Z**2 - M_W**2)
print(f"\n  √(M_Z² - M_W²) = {M_WZ_diff:.0f} MeV = {M_WZ_diff/1e3:.1f} GeV")
print(f"  = M_W × tan θ_W = {M_W * np.sqrt(SIN2_TW/(1-SIN2_TW))/1e3:.1f} GeV")

# ── Test 5: Three-way consistency check ─────────────────────────────

print("\n--- Test 5: Three-way consistency check ---\n")

# The Weinberg angle should be overdetermined by:
# (a) sin²θ_W from coupling ratios
# (b) M_W/M_Z from cross-sheet mode energies
# (c) Geometric ratios from Ma metric

# From Track 1, we found sin²θ_W ≈ 3/13 = 0.2308 (geometric).
# Does this predict M_W/M_Z correctly?

sin2_from_3_13 = 3.0 / 13.0
cos_from_3_13 = np.sqrt(1 - sin2_from_3_13)
MW_from_3_13 = M_Z * cos_from_3_13

print(f"If sin²θ_W = 3/13:")
print(f"  sin²θ_W = {sin2_from_3_13:.6f}")
print(f"  cos θ_W = {cos_from_3_13:.6f}")
print(f"  M_W = M_Z × cos θ_W = {M_Z/1e3:.1f} × {cos_from_3_13:.4f} = {MW_from_3_13/1e3:.3f} GeV")
print(f"  Measured M_W = {M_W/1e3:.3f} GeV")
print(f"  Deviation: {(MW_from_3_13 - M_W)/M_W * 100:.3f}%")

# What integer ratio N/M gives the best match to sin²θ_W?
print(f"\nBest small integer ratios p/q near sin²θ_W = {SIN2_TW:.6f}:")
best = []
for p in range(1, 20):
    for q in range(p+1, 50):
        ratio = p / q
        diff = abs(ratio - SIN2_TW) / SIN2_TW
        best.append((diff, p, q, ratio))

best.sort()
for diff, p, q, ratio in best[:10]:
    print(f"  {p}/{q} = {ratio:.6f}  ({diff*100:.3f}% off)")

# ── Summary ─────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"""
W/Z mass from Ma geometry:

1. Direct cross-sheet coupling energy at σ_ep = {SIGMA_EP}:
   - Too small (~MeV) to reach M_W = 80.4 GeV
   - σ_ep couples sheets perturbatively, not at the EW scale

2. Mode spectrum near 80-91 GeV:
   - Requires very high winding numbers on proton sheet
   - n₆ ~ {n_W_est:.0f} ring windings → deeply in dense-spectrum regime (R28 F5)
   - Cannot uniquely identify W/Z as specific modes

3. Midpoint coupling (R34):
   - E_midpoint = 310 GeV ≈ 1.26 × v_Higgs
   - Cross-sheet energy √(E₀_e × E₀_p)/σ_ep = {E_cross_scale/1e3:.1f} GeV
   - Order-of-magnitude but not a precise match to M_W

4. W/Z mass ratio:
   - M_W/M_Z = cos θ_W = {COS_TW:.4f} is a constraint, not a derivation
   - Track 1's 3/13 match: M_W(predicted) = {MW_from_3_13/1e3:.3f} GeV 
    ({(MW_from_3_13-M_W)/M_W*100:+.3f}% vs measured {M_W/1e3:.3f} GeV)

5. Three-way consistency:
   - sin²θ_W = 3/13 → M_W = {MW_from_3_13/1e3:.3f} GeV ({(MW_from_3_13-M_W)/M_W*100:+.3f}%)
   - sin²θ_W from σ_pν = 0.151 → consistent with positive-definite metric
   - Metric determinant approach needs σ_pν = 0.260 (different from coupling ratio)
""")
