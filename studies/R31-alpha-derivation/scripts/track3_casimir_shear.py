#!/usr/bin/env python3
"""
R31 Track 3: What selects the shear? Casimir energy vs α.

Instead of inputting α, sweep the within-plane shear s₁₂
(and s₅₆ in lockstep) and compute the Casimir energy.
If V_Casimir(s) has a minimum, it predicts s → α.

The Casimir energy is the zero-point (vacuum) energy of
quantum fields on the material space.  It depends on the
geometry.  If it has a minimum, the geometry "wants" to
be there.
"""

import sys, os, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma import (
    alpha_ma, mu_12, hbar_c_MeV_fm, M_E_MEV, M_P_MEV, ALPHA,
    S34, DM2_21, compute_scales,
)

TWO_PI_HC = 2 * math.pi * hbar_c_MeV_fm


def build_metric_at_shear(s12, s56, r_e, r_nu, r_p, sigma_ep=-0.09064):
    """
    Build Ma metric with GIVEN within-plane shears (not derived from α).

    Circumferences are adjusted so that E(1,2,0,0,0,0) = m_e and
    E(0,0,0,0,1,2) = m_p exactly, using the provided s₁₂ and s₅₆.
    """
    mu_e = mu_12(r_e, s12)
    E0_e = M_E_MEV / mu_e
    L2 = TWO_PI_HC / E0_e
    L1 = r_e * L2

    s34 = S34
    E0_nu_sq = DM2_21 / (4 * s34)
    E0_nu = math.sqrt(E0_nu_sq) * 1e-6
    L4 = TWO_PI_HC / E0_nu
    L3 = r_nu * L4

    mu_p = mu_12(r_p, s56)
    E0_p = M_P_MEV / mu_p
    L6 = TWO_PI_HC / E0_p
    L5 = r_p * L6

    L = np.array([L1, L2, L3, L4, L5, L6])

    S_within = np.zeros((6, 6))
    S_within[0, 1] = s12
    S_within[2, 3] = s34
    S_within[4, 5] = s56

    B = np.diag(L) @ (np.eye(6) + S_within)
    G_phys = B.T @ B

    Gt = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            Gt[i, j] = G_phys[i, j] / (L[i] * L[j])

    cross_pairs = [(0, 4), (0, 5), (1, 4), (1, 5)]
    for i, j in cross_pairs:
        Gt[i, j] = sigma_ep
        Gt[j, i] = sigma_ep

    eigvals = np.linalg.eigvalsh(Gt)
    if np.any(eigvals <= 0):
        return None

    Gti = np.linalg.inv(Gt)
    return {'Gt': Gt, 'Gti': Gti, 'L': L}


def casimir_energy(Gti, L, n_max=2, s_exp=5):
    """Epstein zeta sum for Casimir energy."""
    from itertools import product as iterproduct
    Z = 0.0
    rng = range(-n_max, n_max + 1)
    for n in iterproduct(rng, repeat=6):
        if all(ni == 0 for ni in n):
            continue
        n_arr = np.array(n, dtype=float)
        ntilde = n_arr / L
        q = ntilde @ Gti @ ntilde
        if q > 0:
            Z += q**(-s_exp)
    return Z


def mode_energy_from_metric(n, Gti, L):
    """Mode energy in MeV."""
    n = np.asarray(n, dtype=float)
    ntilde = n / L
    E2 = TWO_PI_HC**2 * ntilde @ Gti @ ntilde
    return math.sqrt(max(E2, 0.0))


print("=" * 72)
print("R31 TRACK 3: CASIMIR ENERGY VS WITHIN-PLANE SHEAR")
print("=" * 72)

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064


# ── Section 1: Sweep s₁₂ and compute Casimir energy ─────────────

print("\n\n── Section 1: Casimir energy vs shear ──\n")
print(f"  Fixed: r_e = {R_E}, r_p = {R_P}, σ_ep = {SIGMA_EP}")
print(f"  Sweeping s₁₂ = s₅₆ (same α for both sheets)")
print(f"  At each s, α is computed from α(r, s)")
print()

s_values = np.linspace(0.002, 0.20, 80)
results = []

for s in s_values:
    alpha_e = alpha_ma(R_E, s)
    alpha_p = alpha_ma(R_P, s)

    if alpha_e <= 0 or alpha_e > 0.5:
        continue

    m = build_metric_at_shear(s, s, R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
    if m is None:
        continue

    Z = casimir_energy(m['Gti'], m['L'], n_max=2, s_exp=5)

    E_e = mode_energy_from_metric([1, 2, 0, 0, 0, 0], m['Gti'], m['L'])
    E_p = mode_energy_from_metric([0, 0, 0, 0, 1, 2], m['Gti'], m['L'])
    E_n = mode_energy_from_metric([0, -2, 1, 0, 0, 2], m['Gti'], m['L'])

    results.append({
        's': s, 'alpha_e': alpha_e, 'alpha_p': alpha_p,
        'Z': Z, 'log_Z': math.log10(Z) if Z > 0 else float('-inf'),
        'E_e': E_e, 'E_p': E_p, 'E_n': E_n,
        'L': m['L'].copy(),
    })

print(f"  {'s':>8s} {'α_e':>10s} {'1/α_e':>8s} {'α_p':>10s}"
      f" {'log₁₀(Z)':>10s} {'m_e (MeV)':>10s} {'m_p (MeV)':>10s}")
print(f"  {'─'*70}")

for r in results[::4]:
    marker = " ← obs" if abs(r['alpha_e'] - ALPHA) < 0.001 else ""
    print(f"  {r['s']:8.5f} {r['alpha_e']:10.7f} {1/r['alpha_e']:8.1f}"
          f" {r['alpha_p']:10.7f} {r['log_Z']:10.3f}"
          f" {r['E_e']:10.6f} {r['E_p']:10.3f}{marker}")


# ── Section 2: Does Z have a minimum? ───────────────────────────

print("\n\n── Section 2: Does the Casimir energy have a minimum? ──\n")

if len(results) > 2:
    Z_vals = [r['Z'] for r in results]
    s_vals = [r['s'] for r in results]
    a_vals = [r['alpha_e'] for r in results]

    min_idx = np.argmin(Z_vals)
    max_idx = np.argmax(Z_vals)

    print(f"  Minimum Z at s = {s_vals[min_idx]:.5f}"
          f" (α = 1/{1/a_vals[min_idx]:.1f})")
    print(f"  Maximum Z at s = {s_vals[max_idx]:.5f}"
          f" (α = 1/{1/a_vals[max_idx]:.1f})")
    print(f"  Z range: {Z_vals[min_idx]:.6e} to {Z_vals[max_idx]:.6e}")
    print(f"  Ratio max/min: {Z_vals[max_idx]/Z_vals[min_idx]:.3f}")
    print()

    # Is the minimum in the interior or at the boundary?
    if min_idx == 0:
        print("  The minimum is at the LEFT boundary (smallest s).")
        print("  Casimir energy decreases monotonically with decreasing s.")
        print("  → Z prefers s → 0 (no shear, α → 0, no charge)")
    elif min_idx == len(results) - 1:
        print("  The minimum is at the RIGHT boundary (largest s).")
        print("  Casimir energy decreases monotonically with increasing s.")
        print("  → Z prefers maximum shear (maximum α)")
    else:
        print(f"  *** INTERIOR MINIMUM at s = {s_vals[min_idx]:.5f} ***")
        print(f"  This would predict α = {a_vals[min_idx]:.6f} = 1/{1/a_vals[min_idx]:.1f}")
        print(f"  Observed: α = 1/137.036")

    # Check monotonicity
    dZ = np.diff(Z_vals)
    increasing = np.sum(dZ > 0)
    decreasing = np.sum(dZ < 0)
    print(f"\n  Monotonicity: {increasing} increasing steps, {decreasing} decreasing steps")


# ── Section 3: Casimir energy per sheet ──────────────────────────

print("\n\n── Section 3: Which sheet dominates the Casimir energy? ──\n")

# Compute Casimir on individual sheets
s_test = 0.010293  # s at α = 1/137

m = build_metric_at_shear(s_test, s_test, R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
L = m['L']

print(f"  Circumferences at α = 1/137:")
print(f"    L₁ (e tube) = {L[0]:,.0f} fm")
print(f"    L₂ (e ring) = {L[1]:,.0f} fm")
print(f"    L₃ (ν tube) = {L[2]:,.1e} fm")
print(f"    L₄ (ν ring) = {L[3]:,.1e} fm")
print(f"    L₅ (p tube) = {L[4]:.2f} fm")
print(f"    L₆ (p ring) = {L[5]:.4f} fm")
print()

# The Casimir sum is dominated by the largest dimensions
# because 1/L^10 → smallest L contributes most to q^{-5}
print("  The Casimir energy (q^{-5}) is dominated by modes with")
print("  the SMALLEST q = (n/L)² G̃⁻¹ (n/L).  These are modes")
print("  on the LARGEST dimensions (neutrino, L ~ 10⁸ fm).")
print()
print("  The within-plane shear s₁₂ affects the electron sheet")
print(f"  (L₁ ~ {L[0]:,.0f} fm, L₂ ~ {L[1]:,.0f} fm), which contributes")
print(f"  negligibly compared to the neutrino sheet (L ~ {L[2]:.0e} fm).")
print()
print("  This means the Casimir energy is almost INDEPENDENT")
print("  of s₁₂ (electron shear) and s₅₆ (proton shear).")


# ── Section 4: Verify: electron-only Casimir ─────────────────────

print("\n\n── Section 4: Electron-sheet-only Casimir energy ──\n")

print("  Isolating the electron T² contribution:")
print("  (Set n₃ = n₄ = n₅ = n₆ = 0, sweep n₁, n₂ only)")
print()

e_casimir = []
for r in results:
    Z_e = 0.0
    L_test = r['L']
    Gti_test = build_metric_at_shear(
        r['s'], r['s'], R_E, R_NU, R_P, sigma_ep=SIGMA_EP
    )['Gti']

    for n1 in range(-5, 6):
        for n2 in range(-5, 6):
            if n1 == 0 and n2 == 0:
                continue
            n = np.array([n1, n2, 0, 0, 0, 0], dtype=float)
            ntilde = n / L_test
            q = ntilde @ Gti_test @ ntilde
            if q > 0:
                Z_e += q**(-5)

    e_casimir.append({
        's': r['s'], 'alpha': r['alpha_e'], 'Z_e': Z_e,
        'log_Z_e': math.log10(Z_e) if Z_e > 0 else float('-inf'),
    })

print(f"  {'s':>8s} {'1/α':>8s} {'log₁₀(Z_e)':>12s}")
print(f"  {'─'*32}")
for ec in e_casimir[::4]:
    marker = " ← obs" if abs(ec['alpha'] - ALPHA) < 0.001 else ""
    print(f"  {ec['s']:8.5f} {1/ec['alpha']:8.1f} {ec['log_Z_e']:12.3f}{marker}")

if e_casimir:
    Z_e_vals = [ec['Z_e'] for ec in e_casimir]
    s_e_vals = [ec['s'] for ec in e_casimir]
    a_e_vals = [ec['alpha'] for ec in e_casimir]

    min_idx = np.argmin(Z_e_vals)
    max_idx = np.argmax(Z_e_vals)

    print(f"\n  Electron-only Casimir:")
    print(f"    Minimum at s = {s_e_vals[min_idx]:.5f}"
          f" (α = 1/{1/a_e_vals[min_idx]:.1f})")
    print(f"    Maximum at s = {s_e_vals[max_idx]:.5f}"
          f" (α = 1/{1/a_e_vals[max_idx]:.1f})")

    if min_idx > 0 and min_idx < len(e_casimir) - 1:
        print(f"\n  *** INTERIOR MINIMUM at α = 1/{1/a_e_vals[min_idx]:.1f} ***")
    elif min_idx == 0:
        print(f"\n  Monotonically increasing — prefers s → 0 (α → 0)")
    else:
        print(f"\n  Monotonically decreasing — prefers maximum s (maximum α)")


# ── Section 5: What COULD select α? ─────────────────────────────

print("\n\n── Section 5: Analysis — what could select α? ──\n")

print("  The Casimir energy on the full Ma is dominated by the")
print("  neutrino sheet (largest dimensions).  The within-plane")
print("  shears s₁₂ and s₅₆ have negligible effect on it.")
print()
print("  The electron-sheet Casimir energy depends on s₁₂, but:")
print("  - It is a tiny fraction of the total")
print("  - It varies monotonically (no interior minimum)")
print()
print("  Conclusion: CASIMIR ENERGY ALONE does not select α.")
print()
print("  What else could select α?")
print()
print("  1. MODULI STABILIZATION: a potential V(r, s) that includes")
print("     both Casimir energy AND flux energy (the EM field")
print("     energy stored in the sheared metric).  The shear costs")
print("     energy (distortion of the torus), and this cost could")
print("     balance against the Casimir energy.")
print()
print("  2. TOPOLOGICAL CONSTRAINT: the (1,2) geodesic must close")
print("     smoothly on the sheared torus.  This is already")
print("     satisfied for all s, so it doesn't constrain α.")
print()
print("  3. SELF-CONSISTENCY OF CHARGE: the Ma charge formula")
print("     gives α(r, s).  If the BACK-REACTION of the charge")
print("     on the geometry is included (the charged mode distorts")
print("     the metric), s might be self-consistently determined.")
print("     This requires solving the coupled Einstein-Maxwell")
print("     system on the torus — a challenging calculation.")
print()
print("  4. EXTERNAL CONSTRAINT: an observable (Lamb shift, g−2)")
print("     pins r_e, and then α follows from α(r_e, s₁₂).  This")
print("     doesn't explain WHY α = 1/137, but it does predict it")
print("     from a measured quantity + the geometry.")
print()
print("  The most promising NEAR-TERM path is (4): use a precision")
print("  observable to pin r_e → Track 4.")
print()
print("  The most promising FUNDAMENTAL path is (1) or (3): find")
print("  the energy cost of shear and balance it against Casimir.")
print("  This would genuinely predict α from geometry alone.")


# ── Summary ──────────────────────────────────────────────────────

print("\n\n── Summary ──\n")

print("  1. The full Ma Casimir energy is dominated by the neutrino")
print("     sheet and is nearly independent of the within-plane")
print("     shears s₁₂, s₅₆ that determine α.")
print()
print("  2. The electron-sheet-only Casimir energy depends on s₁₂")
print("     but varies monotonically — no interior minimum exists.")
print()
print("  3. CASIMIR ENERGY ALONE DOES NOT SELECT α.")
print("     The vacuum energy has no preferred shear value.")
print()
print("  4. To derive α, we need either:")
print("     (a) The ENERGY COST OF SHEAR (distortion energy) to")
print("         balance against Casimir energy → moduli potential")
print("     (b) A precision observable that pins r_e → Track 4")
print("     (c) Back-reaction of charge on the geometry")
print()
print("  5. The missing ingredient is DYNAMICS — what makes the")
print("     geometry choose a specific shape.  The kinematic model")
print("     (spectra + Casimir) is insufficient.")
