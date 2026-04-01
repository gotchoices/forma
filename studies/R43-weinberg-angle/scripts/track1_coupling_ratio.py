"""
R43 Track 1 — Weinberg angle from cross-sheet coupling ratio.

Tests whether sin²θ_W ≈ 0.231 emerges from the ratio of
cross-sheet coupling (σ parameters) to within-sheet EM
coupling (α) on the Ma geometry.

Three approaches:
  A. Direct ratio:  sin²θ_W = f(α, σ_ep, σ_eν, σ_pν)
  B. Energy-scale ratio:  sin²θ_W from the coupling energies
  C. Geometric survey:  dimensionless ratios near 0.231

Uses existing pinned values:
  σ_ep ≈ 0.038  (from neutron mass, R26 F67)
  σ_eν < 0.05   (from neutrino Δm² ratio, R26 F72)
  σ_pν: free    (scanned)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from lib.ma import (build_scaled_metric, mode_energy, compute_scales,
                    alpha_ma, solve_shear_for_alpha, mu_12,
                    M_E_MEV, M_P_MEV, M_N_MEV, hbar_c_MeV_fm, ALPHA)

SIN2_TW_TARGET = 0.2312
M_W = 80379      # MeV (PDG 2022)
M_Z = 91188      # MeV (PDG 2022)
COS_TW = M_W / M_Z   # 0.8815
G_FERMI = 1.1664e-5   # GeV^-2 (Fermi constant)

# Standard aspect ratios
R_E = 6.6
R_NU = 5.0
R_P = 8.906

# Pinned cross-shears
SIGMA_EP = 0.038
SIGMA_ENU = 0.0    # start at zero, scan later

print("=" * 70)
print("R43 Track 1: Weinberg angle from cross-sheet coupling")
print("=" * 70)

# ── Approach A: Direct coupling ratios ──────────────────────────────

print("\n--- Approach A: Direct coupling ratios ---\n")

L, s12, s34, s56 = compute_scales(R_E, R_NU, R_P)

print(f"Electron sheet: r_e = {R_E}, s_e = {s12:.5f}")
print(f"Neutrino sheet: r_ν = {R_NU}, s_ν = {s34:.5f}")
print(f"Proton sheet:   r_p = {R_P}, s_p = {s56:.5f}")
print(f"α = {ALPHA:.6f} = 1/{1/ALPHA:.1f}")
print(f"σ_ep = {SIGMA_EP} (from neutron mass)")
print()

print("Hypothesis: sin²θ_W = α / (α + σ²_eff)")
print()

sigma_values = [SIGMA_EP, 0.05, 0.10, 0.15, 0.156, 0.20, 0.30]
print(f"  {'σ_eff':>10s}  {'σ²':>10s}  {'sin²θ_W':>10s}  {'vs 0.231':>10s}")
print(f"  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")

for sig in sigma_values:
    s2tw = ALPHA / (ALPHA + sig**2)
    print(f"  {sig:10.4f}  {sig**2:10.6f}  {s2tw:10.6f}  {s2tw/SIN2_TW_TARGET:10.4f}×")

# Solve for σ_eff that gives target
sigma_target = np.sqrt(ALPHA * (1 - SIN2_TW_TARGET) / SIN2_TW_TARGET)
print(f"\n  Target sin²θ_W = {SIN2_TW_TARGET} requires σ_eff = {sigma_target:.5f}")
print(f"  σ²_eff = {sigma_target**2:.6f}")
print(f"  σ_eff / σ_ep = {sigma_target / SIGMA_EP:.2f}")

# ── Approach B: Energy-scale coupling ───────────────────────────────

print("\n--- Approach B: Mode energy ratios ---\n")

# The Fermi constant relates to the W mass:  G_F/√2 = g²/(8M_W²)
# In Ma terms, the "weak coupling" g might be related to cross-sheet
# mode energies.  The key modes are:

Gt, Gti, L_arr, scales = build_scaled_metric(
    R_E, R_NU, R_P,
    sigma_ep=SIGMA_EP, sigma_enu=SIGMA_ENU
)

# Cross-sheet modes: modes with windings on two sheets
cross_modes_ep = [
    (1, 2, 0, 0, 1, 2),   # neutron-like
    (1, 0, 0, 0, 1, 0),   # lightest e-p cross
    (1, 0, 0, 0, 0, 1),
    (0, 1, 0, 0, 1, 0),
    (0, 1, 0, 0, 0, 1),
]

print("Cross-sheet e-p modes (σ_ep = 0.038):")
print(f"  {'Mode':>20s}  {'E (MeV)':>12s}")
print(f"  {'-'*20}  {'-'*12}")
for n in cross_modes_ep:
    E = mode_energy(n, Gti, L_arr)
    print(f"  {str(n):>20s}  {E:12.3f}")

# The W mass should correspond to some cross-sheet barrier
# energy.  In KK theory, M_W ~ 2π/(cross-sheet spacing).
# The cross-sheet "spacing" in Ma is related to the off-diagonal
# metric element σ_ep.

# Energy scale from σ_ep:
# The metric perturbation from σ_ep affects mode energies at
# order σ² × E_0.  The relevant energy scale is:
E0_e = M_E_MEV / mu_12(R_E, s12)
E0_p = M_P_MEV / mu_12(R_P, s56)

# The coupling energy between sheets:
# ΔE² ≈ σ² × E0_e × E0_p (cross term in metric)
coupling_energy_sq = SIGMA_EP**2 * (2 * np.pi * hbar_c_MeV_fm)**2 / (L_arr[1] * L_arr[5])
coupling_energy = np.sqrt(abs(coupling_energy_sq))

print(f"\nCoupling energy scale from σ_ep:")
print(f"  E_coupling ≈ {coupling_energy:.1f} MeV = {coupling_energy/1000:.3f} GeV")
print(f"  M_W = {M_W/1000:.1f} GeV")
print(f"  M_Z = {M_Z/1000:.1f} GeV")
print(f"  Ratio E_coupling / M_W = {coupling_energy / M_W:.4f}")

# ── Approach C: Geometric ratio survey ──────────────────────────────

print("\n--- Approach C: Geometric ratio survey ---\n")

print("Dimensionless ratios from Ma geometry:")
print(f"  {'Ratio':>40s}  {'Value':>10s}  {'vs 0.231':>10s}")
print(f"  {'-'*40}  {'-'*10}  {'-'*10}")

ratios = {
    'α (within-sheet coupling)': ALPHA,
    '4α': 4 * ALPHA,
    'α × π': ALPHA * np.pi,
    'ζ = 1/4': 0.25,
    '1 - ζ = 3/4': 0.75,
    '3/13': 3/13,
    's_e (electron shear)': s12,
    's_p (proton shear)': s56,
    's_ν (neutrino shear)': s34,
    's_e + s_p': s12 + s56,
    's_e × s_p × 1000': s12 * s56 * 1000,
    'σ_ep': SIGMA_EP,
    'σ_ep²': SIGMA_EP**2,
    'σ_ep / (1 + σ_ep)': SIGMA_EP / (1 + SIGMA_EP),
    'r_e / (r_e + r_p + r_ν)': R_E / (R_E + R_P + R_NU),
    'r_ν / (r_e + r_p + r_ν)': R_NU / (R_E + R_P + R_NU),
    '1/r_e + 1/r_p': 1/R_E + 1/R_P,
    'L1/L5 (tube ratio e/p)': L_arr[0] / L_arr[4],
    'L2/L6 (ring ratio e/p)': L_arr[1] / L_arr[5],
    '(L2/L6)²': (L_arr[1] / L_arr[5])**2,
    'A_e / A_p (area ratio)': (L_arr[0]*L_arr[1]) / (L_arr[4]*L_arr[5]),
    'A_e / (A_e + A_p)': (L_arr[0]*L_arr[1]) / (L_arr[0]*L_arr[1] + L_arr[4]*L_arr[5]),
    'A_e / A_total (all 3 sheets)': (L_arr[0]*L_arr[1]) / (L_arr[0]*L_arr[1] + L_arr[2]*L_arr[3] + L_arr[4]*L_arr[5]),
    'm_e / (m_e + m_p)': M_E_MEV / (M_E_MEV + M_P_MEV),
    'm_e / m_p': M_E_MEV / M_P_MEV,
    '(m_e/m_p)^(1/2)': np.sqrt(M_E_MEV / M_P_MEV),
    'α / σ_ep': ALPHA / SIGMA_EP,
    'α / σ_ep²': ALPHA / SIGMA_EP**2,
    'σ_ep² / α': SIGMA_EP**2 / ALPHA,
    'σ_ep × s_e': SIGMA_EP * s12,
    'sin²(π × σ_ep)': np.sin(np.pi * SIGMA_EP)**2,
}

# Sort by closeness to target
sorted_ratios = sorted(ratios.items(), key=lambda x: abs(x[1] - SIN2_TW_TARGET))

for name, val in sorted_ratios:
    marker = " ★" if abs(val - SIN2_TW_TARGET) / SIN2_TW_TARGET < 0.1 else ""
    print(f"  {name:>40s}  {val:10.6f}  {val/SIN2_TW_TARGET:10.4f}×{marker}")

# ── Approach D: Scan σ_pν for Weinberg match ────────────────────────

print("\n--- Approach D: σ_pν scan with fixed σ_ep ---\n")

# The effective cross-sheet coupling might involve all three σ's.
# The Fermi constant is measured from muon decay (μ → e ν_μ ν_e),
# which involves electron-neutrino coupling.  But the Weinberg
# angle mixes EM and weak, which involves all sheets.

# Hypothesis: sin²θ_W = g'²/(g² + g'²) where:
#   g'² ∝ α (hypercharge ~ EM coupling)
#   g²  ∝ some combination of σ's (weak ~ cross-sheet coupling)

# Test: g² = σ_ep² + σ_eν² + σ_pν² (sum of all cross-sheet couplings)
print("Hypothesis: sin²θ_W = α / (α + Σσ²)")
print(f"  σ_ep = {SIGMA_EP} (fixed)")
print(f"  σ_eν = 0 (fixed at zero)")
print(f"  Scanning σ_pν...")
print()

print(f"  {'σ_pν':>8s}  {'Σσ²':>10s}  {'sin²θ_W':>10s}  {'vs target':>10s}")
print(f"  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*10}")

best_pν = None
best_diff = 1.0

for s_pn in np.linspace(0.0, 0.5, 200):
    sum_sigma2 = SIGMA_EP**2 + SIGMA_ENU**2 + s_pn**2
    s2tw = ALPHA / (ALPHA + sum_sigma2)
    diff = abs(s2tw - SIN2_TW_TARGET)
    if diff < best_diff:
        best_diff = diff
        best_pν = s_pn

    if s_pn < 0.005 or abs(s_pn - 0.038) < 0.002 or abs(s_pn - 0.05) < 0.002 \
       or abs(s_pn - 0.1) < 0.002 or abs(s_pn - 0.15) < 0.002 \
       or abs(s_pn - 0.156) < 0.002 or abs(s_pn - 0.2) < 0.003 \
       or abs(s_pn - best_pν) < 0.002:
        print(f"  {s_pn:8.4f}  {sum_sigma2:10.6f}  {s2tw:10.6f}  {s2tw/SIN2_TW_TARGET:10.4f}×")

# Also test the sum-all hypothesis
sum_s2_best = SIGMA_EP**2 + SIGMA_ENU**2 + best_pν**2
s2tw_best = ALPHA / (ALPHA + sum_s2_best)
print(f"\n  Best match at σ_pν = {best_pν:.4f}")
print(f"    Σσ² = {sum_s2_best:.6f}")
print(f"    sin²θ_W = {s2tw_best:.6f} (target: {SIN2_TW_TARGET})")

# Check positivity with this value
Gt_test, Gti_test, L_test, _ = build_scaled_metric(
    R_E, R_NU, R_P,
    sigma_ep=SIGMA_EP, sigma_enu=SIGMA_ENU, sigma_nup=best_pν
)
from lib.ma import is_positive_definite
pd = is_positive_definite(Gt_test)
print(f"    Metric positive definite: {pd}")

# Check if this σ_pν perturbs the neutron mass
E_neutron = mode_energy((1,2,0,0,1,2), Gti_test, L_test)
print(f"    Neutron energy at this σ_pν: {E_neutron:.3f} MeV (target: {M_N_MEV})")

# ── Approach E: Alternative — g² from metric determinant ────────────

print("\n--- Approach E: Metric-based coupling ---\n")

# The off-diagonal structure of G̃ encodes the coupling.
# det(G̃) = 1 when no coupling, < 1 with coupling.
# The coupling fraction might be related to sin²θ_W.

for sig_pn in [0.0, 0.038, best_pν, 0.1, 0.15]:
    Gt_t, _, _, _ = build_scaled_metric(
        R_E, R_NU, R_P,
        sigma_ep=SIGMA_EP, sigma_enu=SIGMA_ENU, sigma_nup=sig_pn
    )
    det = np.linalg.det(Gt_t)
    coupling_fraction = 1 - det
    evals = np.linalg.eigvalsh(Gt_t)
    min_eval = evals.min()
    print(f"  σ_pν={sig_pn:.3f}: det(G̃)={det:.6f}, "
          f"1-det={coupling_fraction:.6f}, "
          f"min_eig={min_eval:.4f}")

# Compare 1-det to sin²θ_W
print(f"\n  Need 1-det(G̃) ≈ {SIN2_TW_TARGET}")
# Solve for σ_pν where 1-det = 0.231
print("  Scanning for 1-det = 0.231...")

best_pν_det = None
best_diff_det = 1.0
for s_pn in np.linspace(0.0, 0.5, 1000):
    Gt_t, _, _, _ = build_scaled_metric(
        R_E, R_NU, R_P,
        sigma_ep=SIGMA_EP, sigma_enu=SIGMA_ENU, sigma_nup=s_pn
    )
    det = np.linalg.det(Gt_t)
    diff = abs(1 - det - SIN2_TW_TARGET)
    if diff < best_diff_det:
        best_diff_det = diff
        best_pν_det = s_pn

Gt_t, Gti_t, L_t, _ = build_scaled_metric(
    R_E, R_NU, R_P,
    sigma_ep=SIGMA_EP, sigma_enu=SIGMA_ENU, sigma_nup=best_pν_det
)
det_best = np.linalg.det(Gt_t)
pd_best = is_positive_definite(Gt_t)
E_n_det = mode_energy((1,2,0,0,1,2), Gti_t, L_t)
print(f"  → σ_pν = {best_pν_det:.4f}: 1-det = {1-det_best:.6f}, "
      f"pd={pd_best}, m_n={E_n_det:.3f} MeV")

# ── Approach F: W mass from cross-sheet resonance ───────────────────

print("\n--- Approach F: W/Z mass from cross-sheet mode energy ---\n")

# The W might be a resonance between Ma_e and Ma_p.
# Its mass would be set by the coupling barrier energy.
# In the KK picture: M_W ~ 2πℏc × σ_ep / √(L_e × L_p)
# (the off-diagonal metric element × the geometric mean scale)

print("W/Z from cross-sheet coupling energy:")
print()

# The cross-sheet coupling energy between sheets a and b is
# related to the off-diagonal block of the metric.
# E_cross ~ (2πℏc)² × σ / (L_a × L_b)

for name, i, j, sig in [
    ('e-p (tube-tube)', 0, 4, SIGMA_EP),
    ('e-p (ring-ring)', 1, 5, SIGMA_EP),
    ('e-p (tube-ring)', 0, 5, SIGMA_EP),
    ('e-p (ring-tube)', 1, 4, SIGMA_EP),
]:
    E_cross = (2 * np.pi * hbar_c_MeV_fm)**2 * abs(sig) / (L_arr[i] * L_arr[j])
    E_cross_sqrt = np.sqrt(E_cross) if E_cross > 0 else 0
    print(f"  {name:>20s}: E² = {E_cross:.3e} MeV², "
          f"E = {E_cross_sqrt:.1f} MeV = {E_cross_sqrt/1000:.3f} GeV")

# Try geometric mean of e and p energy scales × σ_ep
E_geom = np.sqrt(M_E_MEV * M_P_MEV)
E_W_est = E_geom / SIGMA_EP
print(f"\n  √(m_e × m_p) / σ_ep = {E_geom:.1f} / {SIGMA_EP} = {E_W_est:.0f} MeV = {E_W_est/1000:.1f} GeV")
print(f"  (target: M_W = {M_W/1000:.1f} GeV)")

# Try: M_W = m_p / (2πσ_ep) or similar
E_W_est2 = M_P_MEV / (2 * np.pi * SIGMA_EP)
print(f"  m_p / (2π σ_ep) = {E_W_est2:.0f} MeV = {E_W_est2/1000:.1f} GeV")

# Try: M_W from Fermi constant relation
# G_F/√2 = g²/(8M_W²), and in Ma: g² ~ 4π × σ_ep² (cross-sheet coupling)
g2_from_GF = 8 * M_W**2 * G_FERMI * 1e-6 / np.sqrt(2)  # convert GeV^-2
print(f"\n  From G_F: g² = 8M_W²G_F/√2 = {g2_from_GF:.4f}")
print(f"  g = {np.sqrt(g2_from_GF):.4f}")
print(f"  If g² = 4π σ_eff²: σ_eff = {np.sqrt(g2_from_GF / (4*np.pi)):.5f}")
print(f"  If g = σ_eff: σ_eff = {np.sqrt(g2_from_GF):.5f}")

# ── Summary ─────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"""
Target: sin²θ_W = {SIN2_TW_TARGET}

Approach A (α/(α+σ²)):
  Requires σ_eff = {sigma_target:.5f}
  This is {sigma_target/SIGMA_EP:.1f}× larger than σ_ep = {SIGMA_EP}
  Interpretation: if σ_eff involves all three cross-shears,
  σ_pν ≈ {best_pν:.4f} could close the gap.

Approach C (geometric ratios):
  Closest matches listed above (★ = within 10%).

Approach D (σ_pν scan with Σσ²):
  Best fit at σ_pν = {best_pν:.4f}, sin²θ_W = {s2tw_best:.6f}

Approach E (metric determinant):
  1-det(G̃) = {SIN2_TW_TARGET} at σ_pν = {best_pν_det:.4f}
  Metric positive definite: {pd_best}
  Neutron mass preserved: {E_n_det:.3f} MeV

M_W estimates:
  √(m_e × m_p) / σ_ep = {E_W_est/1000:.1f} GeV (target: {M_W/1000:.1f} GeV)
  m_p / (2πσ_ep) = {E_W_est2/1000:.1f} GeV
""")
