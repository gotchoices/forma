"""
R43 Track 4 — Can 3/13 be derived from a trace on the Ma metric?

In SU(5) GUT, sin²θ_W = 3/8 comes from a trace calculation:
the ratio Tr(Y²)/Tr(T₃²) of the hypercharge and isospin
generators in the fundamental 5-representation.

The MaSt analog: is there a natural decomposition of the
6×6 Ma metric G̃ into "electromagnetic" and "weak" parts
whose trace ratio gives 3/13?

We try every plausible definition to see if 3/13 emerges
from the metric itself, not from ad hoc parameter counting.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from lib.ma import (build_scaled_metric, compute_scales, ALPHA,
                    is_positive_definite, mode_energy)

R_E = 6.6
R_NU = 5.0
R_P = 8.906
SIGMA_EP = 0.038

SIN2_TW = 0.23122   # PDG MS-bar at M_Z

print("=" * 70)
print("R43 Track 4: Trace derivation of 3/13")
print("=" * 70)

L, s12, s34, s56 = compute_scales(R_E, R_NU, R_P)

# Build metrics at different σ configurations
Gt_full, Gti_full, _, _ = build_scaled_metric(
    R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
Gt_0, Gti_0, _, _ = build_scaled_metric(
    R_E, R_NU, R_P, sigma_ep=0.0)

print(f"\nWithin-sheet shears: s₁₂ = {s12:.5f}, s₃₄ = {s34:.5f}, s₅₆ = {s56:.5f}")
print(f"Cross-sheet shear: σ_ep = {SIGMA_EP}")
print()

# ── Define the EM and weak parts of the metric ─────────────────────

# The metric G̃ = I + S_em + S_weak where:
#   S_em = within-sheet off-diagonal part (shears s)
#   S_weak = cross-sheet off-diagonal part (shears σ)

I6 = np.eye(6)

S_em = Gt_full.copy()
S_em[np.diag_indices(6)] = 0   # remove diagonal
# Zero out cross-sheet entries
for i in range(2):
    for j in range(2, 6):
        S_em[i, j] = 0; S_em[j, i] = 0
for i in range(2, 4):
    for j in range(4, 6):
        S_em[i, j] = 0; S_em[j, i] = 0

S_weak = Gt_full - I6 - S_em

print("S_em (within-sheet shears):")
print(np.round(S_em, 5))
print()
print("S_weak (cross-sheet shears):")
print(np.round(S_weak, 5))
print()

# ── Approach 1: Frobenius norm ratio ───────────────────────────────

print("--- Approach 1: Frobenius norm ratio ---\n")

norm_em = np.linalg.norm(S_em, 'fro')
norm_weak = np.linalg.norm(S_weak, 'fro')
norm_total = np.linalg.norm(S_em + S_weak, 'fro')

f1 = norm_em**2 / (norm_em**2 + norm_weak**2)
print(f"  ||S_em||² = {norm_em**2:.6f}")
print(f"  ||S_weak||² = {norm_weak**2:.6f}")
print(f"  ||S_em||² / (||S_em||² + ||S_weak||²) = {f1:.6f}")
print(f"  Target: {SIN2_TW:.6f}")
print(f"  3/13 = {3/13:.6f}")
print()

# Frobenius norm² = Tr(M^T M) = sum of squares of all entries.
# S_em has 2×3 = 6 nonzero entries (3 pairs symmetric)
# S_weak has at most 2×12 = 24 nonzero entries (but only σ_ep set)
# With only σ_ep: 2×4 = 8 nonzero entries

n_em_entries = np.count_nonzero(S_em)
n_weak_entries = np.count_nonzero(S_weak)
print(f"  Nonzero entries: EM = {n_em_entries}, weak = {n_weak_entries}")

# ── Approach 2: Trace of squared coupling ──────────────────────────

print("\n--- Approach 2: Tr(S²) ratio ---\n")

tr_em2 = np.trace(S_em @ S_em)
tr_weak2 = np.trace(S_weak @ S_weak)
tr_total2 = np.trace((S_em + S_weak) @ (S_em + S_weak))

f2 = tr_em2 / (tr_em2 + tr_weak2)
print(f"  Tr(S_em²) = {tr_em2:.6f}")
print(f"  Tr(S_weak²) = {tr_weak2:.6f}")
print(f"  Tr(S_em²) / (Tr(S_em²) + Tr(S_weak²)) = {f2:.6f}")
print(f"  (same as Frobenius: {f1:.6f})")

# ── Approach 3: Eigenvalue decomposition ───────────────────────────

print("\n--- Approach 3: Eigenvalue-based ratios ---\n")

evals_full = np.linalg.eigvalsh(Gt_full)
evals_em = np.linalg.eigvalsh(I6 + S_em)   # metric with only EM coupling
evals_0 = np.ones(6)  # uncoupled = identity

print(f"  Eigenvalues (uncoupled): {evals_0}")
print(f"  Eigenvalues (EM only):   {np.round(np.sort(np.linalg.eigvalsh(I6 + S_em)), 6)}")
print(f"  Eigenvalues (full):      {np.round(evals_full, 6)}")
print()

# Deviation from identity
delta_em = np.sort(np.linalg.eigvalsh(I6 + S_em)) - 1
delta_full = evals_full - 1
print(f"  δ_em = eigenvalues(I+S_em) - 1:  {np.round(delta_em, 6)}")
print(f"  δ_full = eigenvalues(G̃) - 1:     {np.round(delta_full, 6)}")
print()

sum_delta_em2 = np.sum(delta_em**2)
sum_delta_full2 = np.sum(delta_full**2)
f3 = sum_delta_em2 / sum_delta_full2
print(f"  Σ(δ_em²) / Σ(δ_full²) = {sum_delta_em2:.6f} / {sum_delta_full2:.6f} = {f3:.6f}")

# ── Approach 4: Coupling-independent counting ──────────────────────

print("\n--- Approach 4: Pure counting (no coupling values) ---\n")

# The key insight from SU(5): the ratio doesn't depend on the
# actual coupling values, only on the group structure.
# If MaSt has a similar property, 3/13 should emerge from
# the STRUCTURE of the 3-sheet system, not from specific s, σ values.

# Define projectors onto the EM and weak subspaces of the
# space of off-diagonal metric entries.

# A 6×6 symmetric matrix has 15 independent off-diagonal entries.
# Organize them as a 15-vector, with a projector onto the 3 EM
# entries and onto the 12 weak entries.

# P_em projects onto entries: (0,1), (2,3), (4,5)
# P_weak projects onto the remaining 12

# In SU(5), sin²θ_W = Tr(Q_em²) / Tr(Q_total²) where Q is
# computed in the fundamental rep.

# MaSt analog: each off-diagonal entry is a "generator" of
# coupling. The EM generators are the 3 within-sheet shears.
# The weak generators are the 12 cross-sheet entries.
# But the 12 weak entries are NOT independent — they come in
# blocks of 4, each controlled by one σ.

# Effective generator count:
# EM: 3 generators, each with coupling = s_i
# Weak: 3 generators, each with coupling = σ_ij
# But each weak generator "acts on" 4 metric entries, while
# each EM generator acts on 1 entry (actually 2, symmetric).

# SU(5)-style: sum of squared generators weighted by multiplicity
# EM: Σ (multiplicity × coupling²) = 3 × (1² × s²) = 3s² (each s fills 1 pair)
# Weak: Σ (multiplicity × coupling²) = 3 × (4 × σ²) = 12σ²  (each σ fills 4 pairs)

# If all couplings are equal (s = σ):
f4_equal = 3 / (3 + 12)
print(f"  If all couplings equal (s = σ):")
print(f"    3/(3+12) = 3/15 = {f4_equal:.6f}")
print()

# But the couplings are NOT equal. What if we normalize each
# by its "natural" scale?

# EM coupling: s ~ α (the shear IS the electromagnetic coupling)
# Weak coupling: σ ~ σ (the cross-shear IS the weak coupling)
# At some "unification" point where s = σ (or they have a common
# origin), the ratio would be 3/15 = 1/5.

# What if the EM generators have weight 1 (they control 1 pair)
# and the weak generators have weight 4/3 (they control 4 pairs
# but only 3 are independent)?

# Actually: each EM generator fills 1 off-diagonal pair.
# Each weak generator fills 4 off-diagonal pairs (a 2×2 block).
# So the "weight" per generator is:
#   EM: 1 pair per generator → weight = 1
#   Weak: 4 pairs per generator → weight = 4

# In SU(5), generators are normalized by Tr(T_a T_b) = δ_ab/2.
# The U(1) generator Y has Tr(Y²) = 5/6.
# The SU(2) generators T_i have Tr(T_i²) = 1/2 each.
# sin²θ_W = (5/3 × g'²) / (5/3 × g'² + g²) → 3/8 at unification.

# MaSt analog with block weights:
# EM: 3 generators × weight 1 = 3
# Weak: 3 generators × weight 4 = 12
# Ratio: 3/(3+12) = 1/5. Still not 3/13.

# ── Approach 5: What DOES give 3/13 from structure? ────────────────

print("--- Approach 5: What structural ratio equals 3/13? ---\n")

# Let's be systematic. 3/13 = 3/(3 + 10).
# What is 10 in the Ma structure?

# Possibilities for 10:
# - dim(SU(5)) = 24 → no
# - Number of entries in the antisymmetric part? 6×6 antisym = 15 → no
# - C(5,2) = 10? Where does 5 come from? 5 = D-1 = 6-1?
# - 10 = 2×5? Where 5 = number of "other" dimensions (from any
#   given sheet's perspective, 4 cross dims + 1 partner within-sheet)
# - 10 = number of independent METRIC entries beyond identity and 
#   EM shears? Total indep = 21. Minus 6 diagonal = 15. Minus 3 EM = 12.
#   Minus 2 redundant? Hmm.

# Let's try: what if the EM fraction is computed as a ratio of
# coupling CHANNELS, where channels are weighted by the
# dimension of the representation they connect?

# Each within-sheet shear s_ij connects dim_i × dim_j = 1×1 = 1
# mode pair (within a 2D block).
# Each cross-sheet σ connects 2×2 = 4 mode pairs (between two 2D blocks).
# But there are 3 σ blocks.

# What if "effective weight" = √(pairs per generator)?
# EM: 3 × √1 = 3
# Weak: 3 × √4 = 6
# Total: 9. Ratio: 3/9 = 1/3. Not 3/13.

# What if weight = pairs:
# EM: 3 × 1 = 3
# Weak: 3 × 4 = 12
# But then add the diagonal (6 entries, weight 1 each)? 
# No, diagonal doesn't couple.

# What if we count the DIMENSION of the space of metrics
# consistent with the 3-sheet block structure?
# A 6×6 symmetric matrix with fixed diagonal and block structure:
#   3 within-sheet shears
#   3 cross-sheet σ's (each filling a 2×2 block)
#   3 aspect ratios
#   = 9 parameters. Ratio: 3/9 = 1/3. Not 3/13.

# What if we DON'T collapse the σ blocks?
# Independent off-diagonal entries: 15 total.
# EM: 3
# Weak: 12
# Plus the 6 diagonal entries (fixed but still "there"):
# Total structural entries: 6 + 3 + 12 = 21.
# EM fraction: 3/21 = 1/7. Not 3/13.

# What if we use the SCALED entries?
# Diagonal: 6 entries × 1 = 6
# EM off-diag: 3 entries × s = 3s ~ 3α (since s ~ α/10)
# Weak off-diag: 12 entries × σ = 12σ

# Hmm. Let me try a completely different approach.
# Instead of decomposing the metric, decompose the INVERSE metric.

print("Decomposing G̃⁻¹:\n")
print(f"  G̃⁻¹ =")
print(np.round(Gti_full, 5))
print()

# Extract the within-sheet and cross-sheet parts of G̃⁻¹
Gti_diag = np.diag(np.diag(Gti_full))
Gti_em = np.zeros((6,6))
for sheet_start in [0, 2, 4]:
    i, j = sheet_start, sheet_start + 1
    Gti_em[i,j] = Gti_full[i,j]
    Gti_em[j,i] = Gti_full[j,i]

Gti_weak = Gti_full - Gti_diag - Gti_em

tr_Gti = np.trace(Gti_full)
tr_Gti_diag = np.trace(Gti_diag)
tr_Gti_em2 = np.trace(Gti_em @ Gti_em)
tr_Gti_weak2 = np.trace(Gti_weak @ Gti_weak)

print(f"  Tr(G̃⁻¹) = {tr_Gti:.6f}")
print(f"  Tr(G̃⁻¹_diag) = {tr_Gti_diag:.6f}")
print()
print(f"  ||G̃⁻¹_em||² = Tr(G̃⁻¹_em²) = {tr_Gti_em2:.6f}")
print(f"  ||G̃⁻¹_weak||² = Tr(G̃⁻¹_weak²) = {tr_Gti_weak2:.6f}")
f5 = tr_Gti_em2 / (tr_Gti_em2 + tr_Gti_weak2)
print(f"  Ratio: {f5:.6f}")

# ── Approach 6: Coupling-independent structure ─────────────────────

print("\n--- Approach 6: Coupling-independent structural ratios ---\n")

# The SU(5) derivation works at ANY coupling value — it's a
# normalization condition, not a dynamics calculation.
# For 3/13 to be "derived," it should emerge at ANY σ and s value.

# Test: compute Tr(S_em²)/(Tr(S_em²) + Tr(S_weak²)) for
# different σ and s values. If it's always 3/13, it's structural.

print("  Testing universality: does the ratio depend on σ/s?")
print(f"  {'σ_ep':>8s}  {'s₁₂':>8s}  {'f_em':>10s}  {'vs 3/13':>10s}")
print(f"  {'-'*8}  {'-'*8}  {'-'*10}  {'-'*10}")

for sig in [0.001, 0.01, 0.038, 0.1, 0.2, 0.5]:
    # Build metric with this σ on all three cross-blocks
    Gt_t, _, _, _ = build_scaled_metric(
        R_E, R_NU, R_P,
        sigma_ep=sig, sigma_enu=sig, sigma_nup=sig)
    if not is_positive_definite(Gt_t):
        print(f"  {sig:8.3f}  {s12:8.5f}  {'(not PD)':>10s}")
        continue
    
    S_em_t = np.zeros((6,6))
    for sheet_start in [0, 2, 4]:
        i, j = sheet_start, sheet_start + 1
        S_em_t[i,j] = Gt_t[i,j]
        S_em_t[j,i] = Gt_t[j,i]
    
    S_weak_t = Gt_t - np.eye(6) - S_em_t
    
    tr_e2 = np.trace(S_em_t @ S_em_t)
    tr_w2 = np.trace(S_weak_t @ S_weak_t)
    ratio = tr_e2 / (tr_e2 + tr_w2) if (tr_e2 + tr_w2) > 0 else 0
    
    print(f"  {sig:8.3f}  {s12:8.5f}  {ratio:10.6f}  {ratio/(3/13):10.4f}×")

# Also test with different r values (which change s)
print()
print("  Varying r_e (changes s_e but not σ):")
print(f"  {'r_e':>8s}  {'s₁₂':>8s}  {'f_em':>10s}  {'vs 3/13':>10s}")
print(f"  {'-'*8}  {'-'*8}  {'-'*10}  {'-'*10}")

for r_e_test in [1.0, 2.0, 4.0, 6.6, 10.0, 20.0]:
    try:
        Gt_t, _, _, sc = build_scaled_metric(
            r_e_test, R_NU, R_P,
            sigma_ep=SIGMA_EP, sigma_enu=SIGMA_EP, sigma_nup=SIGMA_EP)
        s_test = sc['s12']
        
        S_em_t = np.zeros((6,6))
        for sheet_start in [0, 2, 4]:
            i, j = sheet_start, sheet_start + 1
            S_em_t[i,j] = Gt_t[i,j]
            S_em_t[j,i] = Gt_t[j,i]
        
        S_weak_t = Gt_t - np.eye(6) - S_em_t
        
        tr_e2 = np.trace(S_em_t @ S_em_t)
        tr_w2 = np.trace(S_weak_t @ S_weak_t)
        ratio = tr_e2 / (tr_e2 + tr_w2) if (tr_e2 + tr_w2) > 0 else 0
        
        print(f"  {r_e_test:8.1f}  {s_test:8.5f}  {ratio:10.6f}  {ratio/(3/13):10.4f}×")
    except Exception as e:
        print(f"  {r_e_test:8.1f}  (failed: {e})")

# ── Approach 7: Metric entry counting with σ = s ───────────────────

print("\n--- Approach 7: Universal σ = s (equal coupling) ---\n")

# If EM and weak couplings unify (σ = s), what ratio emerges?
# Build a metric where all off-diagonal entries are equal: s = σ = x

for x in [0.01, 0.05, 0.1]:
    G_unif = np.eye(6)
    for i in range(6):
        for j in range(i+1, 6):
            G_unif[i,j] = x
            G_unif[j,i] = x
    
    S_em_u = np.zeros((6,6))
    for sheet_start in [0, 2, 4]:
        i, j = sheet_start, sheet_start + 1
        S_em_u[i,j] = x
        S_em_u[j,i] = x
    S_weak_u = G_unif - np.eye(6) - S_em_u
    
    tr_e2 = np.trace(S_em_u @ S_em_u)
    tr_w2 = np.trace(S_weak_u @ S_weak_u)
    ratio = tr_e2 / (tr_e2 + tr_w2)
    
    # Also check number-based: EM has 3 pairs × x², weak has 12 pairs × x²
    ratio_counting = 3 / (3 + 12)
    
    print(f"  x = {x}: Tr-ratio = {ratio:.6f}, counting = {ratio_counting:.6f}")
    print(f"    = {int(round(3/ratio))}/... → 3/{3/ratio:.1f}")

# The "unified coupling" ratio is 3/15 = 1/5, not 3/13.
# This means 3/13 CANNOT come from a pure entry-counting argument
# when all couplings are equal.

print("\n  → At unified coupling (σ = s): ratio = 3/15 = 1/5")
print("  → 3/13 requires the EM and weak couplings to differ.")
print("  → This means 3/13 is NOT purely structural (unlike SU(5)'s 3/8)")

# ── Approach 8: What ratio gives 3/13 with s ≠ σ? ─────────────────

print("\n--- Approach 8: Required s/σ ratio for 3/13 ---\n")

# If f = 3s² / (3s² + 12σ²) = 3/13:
# → 13 × 3s² = 3 × (3s² + 12σ²)
# → 39s² = 9s² + 36σ²
# → 30s² = 36σ²
# → s²/σ² = 36/30 = 6/5
# → s/σ = √(6/5) ≈ 1.095

s_over_sigma = np.sqrt(6/5)
print(f"  3s²/(3s² + 12σ²) = 3/13  requires  s/σ = √(6/5) = {s_over_sigma:.6f}")
print()

# Check actual values:
for name, s_val in [("s₁₂ (electron)", s12), ("s₃₄ (neutrino)", s34), ("s₅₆ (proton)", s56)]:
    actual_ratio = s_val / SIGMA_EP
    print(f"  {name}: s/σ_ep = {s_val:.5f}/{SIGMA_EP} = {actual_ratio:.4f}")
    print(f"    Need {s_over_sigma:.4f}, have {actual_ratio:.4f}")

# What if σ_eff involves all three cross-shears at equal value?
# The Frobenius norm of S_weak with all σ's = σ:
# Tr(S_weak²) = 12 × 2 × σ² (12 pairs, each appearing twice in S²)
# Actually: Tr(S_weak²) = 2 × (number of pairs) × σ²
# For 3 blocks of 4 pairs = 12 pairs: Tr = 2 × 12 × σ² = 24σ²
# Tr(S_em²) = 2 × 3 × s² = 6s² (3 within-sheet pairs)
# Wait, let me just compute it.

for sig_all in [0.038, 0.01, 0.1]:
    Gt_a, _, _, sc_a = build_scaled_metric(
        R_E, R_NU, R_P,
        sigma_ep=sig_all, sigma_enu=sig_all, sigma_nup=sig_all)
    
    S_e = np.zeros((6,6))
    for ss in [0, 2, 4]:
        i, j = ss, ss + 1
        S_e[i,j] = Gt_a[i,j]
        S_e[j,i] = Gt_a[j,i]
    S_w = Gt_a - np.eye(6) - S_e
    
    t_e = np.trace(S_e @ S_e)
    t_w = np.trace(S_w @ S_w)
    
    # What s/σ ratio would give 3/13?
    s_avg = np.sqrt(t_e / 6)
    sigma_avg = np.sqrt(t_w / 24)
    
    print(f"\n  All σ = {sig_all}:")
    print(f"    Tr(S_em²) = {t_e:.6f}, effective s_rms = {s_avg:.5f}")
    print(f"    Tr(S_weak²) = {t_w:.6f}, effective σ_rms = {sigma_avg:.5f}")
    print(f"    s_rms/σ_rms = {s_avg/sigma_avg:.4f} (need {s_over_sigma:.4f} for 3/13)")
    print(f"    Actual ratio: {t_e/(t_e+t_w):.6f} (need {3/13:.6f})")

# ── Summary ─────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"""
No trace calculation on the Ma metric produces 3/13 independent
of coupling values.

Key results:
  Approach 1-3: Tr(S_em²) / (Tr(S_em²) + Tr(S_weak²)) depends on
                the actual values of s and σ, not just on structure.

  Approach 6:   The ratio changes with σ and r_e.  It is NOT universal.

  Approach 7:   At unified coupling (s = σ), the ratio is 3/15 = 1/5,
                not 3/13.  This proves 3/13 is not a pure counting result.

  Approach 8:   For the trace ratio to equal 3/13, one needs
                s/σ = √(6/5) ≈ 1.095 when all σ's are equal.
                The actual s₁₂/σ_ep = {s12/SIGMA_EP:.3f} (much less than 1.095).

Conclusion: 3/13 cannot be derived from a simple trace on the
Ma metric.  Unlike SU(5)'s 3/8 (which follows from group theory
and is coupling-independent), 3/13 either:

  (a) arises from a more subtle structural argument we haven't
      found, or
  (b) is a numerical coincidence with suggestive but non-rigorous
      interpretive support, or
  (c) requires a dynamical mechanism (coupling running, threshold
      matching) rather than a static trace calculation.

The parameter counting (3 EM shears out of 13 structural params)
remains the best interpretive handle, but it is not a derivation.
""")
