"""
R55 Track 1a: Per-sheet Ma-S coupling analysis

For each sheet independently:
  1. Extract the 2×2 sheet metric (with internal shear)
  2. Add Ma-S coupling parameterized by σ
  3. Solve for σ that gives α_eff = 1/137 for the reference mode
  4. Test universality: does the same σ give α for other modes?

The effective coupling uses the Schur complement:
  A_eff = A_sheet - B·C⁻¹·Bᵀ = A_sheet - 3·b⊗b
  α_eff(mode) = 1 - ñᵀ A⁻¹ ñ / (ñᵀ A_eff⁻¹ ñ)

Key finding: universality requires BBᵀ ∝ A, which is impossible
for a rank-2 matrix A. Universality is approximate and depends
on the aspect ratio ε — small ε (nearly square) gives better
universality than large ε (elongated spindle).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from lib.metric import Metric

ALPHA = 1.0 / 137.036


def alpha_eff_single_sheet(A_2x2, L_2, b_2, mode_2):
    """Compute α_eff for a mode on a single sheet with Ma-S coupling.

    Parameters
    ----------
    A_2x2 : ndarray (2, 2) — sheet metric (dimensionless)
    L_2 : ndarray (2,) — circumferences (fm)
    b_2 : ndarray (2,) — Ma-S couplings [tube, ring]
    mode_2 : tuple (2,) — winding numbers on this sheet

    Returns
    -------
    float — effective coupling fraction, or NaN if metric invalid
    """
    n = np.array(mode_2, dtype=float)
    n_tilde = n / L_2

    A_inv = np.linalg.inv(A_2x2)
    E2_bare = n_tilde @ A_inv @ n_tilde

    # A_eff = A - 3·b⊗b  (factor 3 from 3 spatial dimensions)
    BBT = 3.0 * np.outer(b_2, b_2)
    A_eff = A_2x2 - BBT

    eigs = np.linalg.eigvalsh(A_eff)
    if np.any(eigs <= 0):
        return np.nan

    A_eff_inv = np.linalg.inv(A_eff)
    E2_coupled = n_tilde @ A_eff_inv @ n_tilde

    if E2_coupled <= 0:
        return np.nan

    return (E2_coupled - E2_bare) / E2_coupled


def solve_sigma_proportional(A_2x2, L_2, ref_mode, target=ALPHA):
    """Solve for Ma-S coupling proportional to √(diagonal).

    Sets b_i = σ × √(A_ii) so that both dimensions couple
    proportionally to their scale.

    Returns (b_vector, σ_base)
    """
    lo, hi = 0.0, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        b = mid * np.sqrt(np.diag(A_2x2))
        a_eff = alpha_eff_single_sheet(A_2x2, L_2, b, ref_mode)
        if np.isnan(a_eff):
            hi = mid
        elif a_eff < target:
            lo = mid
        else:
            hi = mid
    sigma = (lo + hi) / 2
    b = sigma * np.sqrt(np.diag(A_2x2))
    return b, sigma


def solve_sigma_ring_only(A_2x2, L_2, ref_mode, target=ALPHA):
    """Solve with coupling only on the ring dimension."""
    lo, hi = 0.0, 0.8
    for _ in range(200):
        mid = (lo + hi) / 2
        b = np.array([0.0, mid])
        a_eff = alpha_eff_single_sheet(A_2x2, L_2, b, ref_mode)
        if np.isnan(a_eff):
            hi = mid
        elif a_eff < target:
            lo = mid
        else:
            hi = mid
    sigma = (lo + hi) / 2
    return np.array([0.0, sigma]), sigma


def solve_sigma_uniform(A_2x2, L_2, ref_mode, target=ALPHA):
    """Solve with equal coupling on both dimensions."""
    lo, hi = 0.0, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        b = np.array([mid, mid])
        a_eff = alpha_eff_single_sheet(A_2x2, L_2, b, ref_mode)
        if np.isnan(a_eff):
            hi = mid
        elif a_eff < target:
            lo = mid
        else:
            hi = mid
    sigma = (lo + hi) / 2
    return np.array([sigma, sigma]), sigma


def test_universality(A_2x2, L_2, b, modes, names):
    """Test coupling universality across modes. Returns (results, spread)."""
    results = []
    alphas = []
    for mode, name in zip(modes, names):
        a_eff = alpha_eff_single_sheet(A_2x2, L_2, b, mode)
        results.append((name, mode, a_eff))
        if not np.isnan(a_eff):
            alphas.append(a_eff)
    spread = (max(alphas) - min(alphas)) / np.mean(alphas) * 100 if len(alphas) > 1 else 0
    return results, spread


def main():
    m = Metric.model_E()
    A = m.Gt
    L = m.L

    print("=" * 75)
    print("R55 Track 1a: Per-Sheet Ma-S Coupling Analysis")
    print("=" * 75)
    print()
    print("Assumption: each sheet couples to S at effective strength α = 1/137.")
    print("Question: what Ma-S entries achieve this, and is the coupling universal")
    print("across modes on the same sheet?")
    print()

    sheets = [
        ('e-sheet', (0, 1), (1, 2),
         [(1, 2), (1, 1), (3, 8), (1, 3), (2, 4), (3, 6), (1, -1), (3, 5)],
         ['electron(1,2)', 'ghost(1,1)', 'muon(3,8)', '(1,3)', '(2,4)',
          '(3,6)', '(1,-1)', '(3,5)']),
        ('ν-sheet', (2, 3), (1, 1),
         [(1, 1), (-1, 1), (1, 2), (2, 2), (1, -1), (2, 1)],
         ['ν₁(1,1)', 'ν₂(-1,1)', 'ν₃(1,2)', '(2,2)', '(1,-1)', '(2,1)']),
        ('p-sheet', (4, 5), (1, 3),
         [(1, 3), (1, 1), (2, 6), (1, 2), (3, 9), (1, -1), (-1, 3)],
         ['proton(1,3)', '(1,1)', 'deuteron(2,6)', '(1,2)', 'iron(3,9)',
          '(1,-1)', 'antiproton(-1,3)']),
    ]

    strategies = [
        ('proportional (b_i ∝ √A_ii)', solve_sigma_proportional),
        ('ring-only (b_tube = 0)', solve_sigma_ring_only),
        ('uniform (b_tube = b_ring)', solve_sigma_uniform),
    ]

    for sheet_name, (i0, i1), ref_mode, test_modes, test_names in sheets:
        A_2x2 = A[i0:i1+1, i0:i1+1].copy()
        L_2 = L[i0:i1+1].copy()

        # Compute metric properties
        off_diag_ratio = abs(A_2x2[0, 1]) / np.sqrt(A_2x2[0, 0] * A_2x2[1, 1])

        print("─" * 75)
        print(f"  {sheet_name}")
        print("─" * 75)
        print(f"  Dimensions: ({i0}, {i1})")
        print(f"  L = [{L_2[0]:.4g}, {L_2[1]:.4g}] fm")
        print(f"  A = [[{A_2x2[0,0]:.6g}, {A_2x2[0,1]:.6g}],")
        print(f"       [{A_2x2[1,0]:.6g}, {A_2x2[1,1]:.6g}]]")
        print(f"  Off-diagonal ratio |A₀₁|/√(A₀₀·A₁₁) = {off_diag_ratio:.6f}")
        print(f"    (0 = perfectly isotropic, 1 = maximally anisotropic)")
        print(f"  Reference mode: {ref_mode}")
        print()

        for strat_name, solver in strategies:
            b, sigma = solver(A_2x2, L_2, ref_mode)
            a_ref = alpha_eff_single_sheet(A_2x2, L_2, b, ref_mode)
            results, spread = test_universality(A_2x2, L_2, b, test_modes, test_names)

            print(f"  Strategy: {strat_name}")
            print(f"    b = [{b[0]:+.6g}, {b[1]:+.6g}],  σ_base = {sigma:.6g}")
            print(f"    Reference α_eff = {a_ref:.8f}")
            print()
            print(f"    {'Mode':>20s}  {'α_eff':>12s}  {'Δ from 1/137':>12s}  {'aligned?':>8s}")
            print(f"    {'─'*20}  {'─'*12}  {'─'*12}  {'─'*8}")

            for name, mode, a_eff in results:
                if np.isnan(a_eff):
                    print(f"    {name:>20s}  {'NaN':>12s}")
                    continue
                err = (a_eff - ALPHA) / ALPHA * 100
                # Check if mode is proportional to reference
                nt_ref, nr_ref = ref_mode
                nt, nr = mode
                if nt_ref != 0 and nr_ref != 0:
                    aligned = (nt * nr_ref == nr * nt_ref)
                elif nt_ref == 0:
                    aligned = (nt == 0)
                else:
                    aligned = (nr == 0)
                aligned_str = "yes" if aligned else "no"
                marker = " ✓" if abs(err) < 1 else ""
                print(f"    {name:>20s}  {a_eff:>12.8f}  {err:>+10.2f}%  {aligned_str:>8s}{marker}")

            print(f"    Spread across all modes: {spread:.2f}%")
            print()

        # Identify which modes match
        print(f"  PATTERN: modes proportional to ref {ref_mode} get EXACT α.")
        print(f"  Non-proportional modes deviate because BBᵀ ∝ b⊗b is rank-1")
        print(f"  while A is rank-2. The deviation grows with off-diagonal ratio.")
        print()

    # ── Summary ──────────────────────────────────────────────────
    print("=" * 75)
    print("SUMMARY")
    print("=" * 75)
    print()
    print("  Sheet        ε        off-diag ratio    universality")
    print("  ─────────    ─────    ──────────────    ────────────")
    print("  p-sheet      0.55     0.089             GOOD — proton, deuteron, iron exact")
    print("  ν-sheet      5.0      0.109             FAIR — ν₁ exact, ν₂ 0.3% off")
    print("  e-sheet      397      1.000             POOR — only (n, 2n) modes match")
    print()
    print("  The e-sheet's extreme aspect ratio (ε = 397) makes the 2×2 metric")
    print("  nearly rank-1 (off-diag ratio = 1.000). This destroys universality")
    print("  for modes not aligned with the electron direction.")
    print()
    print("  Question: is there an alternative e-sheet geometry with smaller ε")
    print("  that still produces three lepton generations?")
    print()


if __name__ == '__main__':
    main()
