"""
R55 Track 1: Ma-S transfer function

Build the full 9×9 metric (Ma + S), inject mode perturbations into Ma,
and compute what fraction of each mode's energy is diverted into S by
the Ma-S coupling entries.

Sweep Ma-S parameters to find values where the effective coupling
equals α = 1/137 for ALL charged modes simultaneously.

The 9×9 metric in block form:

    G = | A    B  |      A = 6×6 Ma (known)
        | Bᵀ   C  |      C = 3×3 S  (identity)
                          B = 6×3 Ma-S coupling (unknown)

For a mode at rest in S with Ma winding vector ñ:
    E²_bare    = ñᵀ A⁻¹ ñ              (no coupling)
    E²_coupled = ñᵀ (A − B C⁻¹ Bᵀ)⁻¹ ñ  (with coupling)

The ratio (E²_coupled − E²_bare) / E²_coupled ≈ α_eff
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from lib.metric import Metric

# ════════════════════════════════════════════════════════════════
#  Constants
# ═══════════════════════���════════════════════════════════════════

ALPHA_TARGET = 1.0 / 137.036

# Test modes: (winding numbers, name, expected charge)
# Charge formula: Q = -n₁ + n₅
# Neutrinos live on ν-sheet (dims 2,3) with n₁=n₅=0 → Q=0
TEST_MODES = [
    ((1, 2, 0, 0, 0, 0),    'electron',  -1),
    ((0, 0, -2, 2, 1, 3),   'proton',    +1),
    ((1, 1, -2, -2, 0, 0),  'muon',      -1),
    ((0, 0, 1, 1, 0, 0),    'ν₁',         0),
    ((0, 0, -1, 1, 0, 0),   'ν₂',         0),
    ((0, 0, 0, 0, -1, -3),  'antiproton', -1),
]


def build_9x9_metric(A_6x6, L, sigma_eR_S, sigma_pT_S, sigma_pR_S):
    """
    Build the full 9×9 metric from the 6×6 Ma metric and Ma-S parameters.

    Parameters
    ----------
    A_6x6 : ndarray (6, 6)
        The dimensionless Ma metric G̃ (already built by Metric class).
    L : ndarray (6,)
        Circumference vector in fm.
    sigma_eR_S : float
        Ma-S coupling for e-ring → S (negative = negative charge).
        Applied to dimension index 1.
    sigma_pT_S : float
        Ma-S coupling for p-tube → S (positive = positive charge).
        Applied to dimension index 4.
    sigma_pR_S : float
        Ma-S coupling for p-ring → S (positive = positive charge).
        Applied to dimension index 5.

    Returns
    -------
    G9 : ndarray (9, 9)
        Full 9×9 metric.

    Notes
    -----
    - e-tube (dim 0) and ν-tube (dim 2): coupling ≈ 0 (dimensions too large)
    - ν-ring (dim 3): coupling = 0 (neutrinos electrically neutral)
    - Spatial isotropy: each Ma dim couples equally to S_x, S_y, S_z
    """
    G9 = np.zeros((9, 9))

    # Ma block (top-left 6×6)
    G9[:6, :6] = A_6x6

    # S block (bottom-right 3×3) = identity (flat space)
    G9[6, 6] = 1.0
    G9[7, 7] = 1.0
    G9[8, 8] = 1.0

    # Ma-S block (6×3) and its transpose
    # Each Ma dimension couples equally to all 3 S dimensions
    # The coupling values are dimensionless shears in the metric
    ma_s_couplings = np.zeros(6)
    ma_s_couplings[1] = sigma_eR_S    # e-ring → S (negative)
    ma_s_couplings[4] = sigma_pT_S    # p-tube → S (positive)
    ma_s_couplings[5] = sigma_pR_S    # p-ring → S (positive)

    for i in range(6):
        for j in range(3):
            G9[i, 6 + j] = ma_s_couplings[i]
            G9[6 + j, i] = ma_s_couplings[i]

    return G9


def compute_alpha_eff(A_6x6, L, sigma_eR_S, sigma_pT_S, sigma_pR_S, mode):
    """
    Compute the effective coupling fraction for a given mode.

    α_eff = (E²_coupled − E²_bare) / E²_coupled

    This is the fraction of the mode's energy that is diverted
    into S by the Ma-S coupling.

    Parameters
    ----------
    A_6x6 : ndarray (6, 6)
        Dimensionless Ma metric.
    L : ndarray (6,)
        Circumferences in fm.
    sigma_eR_S, sigma_pT_S, sigma_pR_S : float
        Ma-S coupling parameters.
    mode : tuple (6,)
        Winding numbers.

    Returns
    -------
    alpha_eff : float
        Effective coupling fraction.
    E_bare : float
        Bare mode energy (Ma only).
    E_coupled : float
        Coupled mode energy (Ma + S).
    """
    n = np.array(mode, dtype=float)
    n_tilde = n / L  # ñ = n/L

    # Bare energy: E² ∝ ñᵀ A⁻¹ ñ (Ma only)
    A_inv = np.linalg.inv(A_6x6)
    E2_bare = n_tilde @ A_inv @ n_tilde

    # Coupled energy: E² ∝ ñᵀ (A − B C⁻¹ Bᵀ)⁻¹ ñ
    # C = I₃, so C⁻¹ = I₃, and B C⁻¹ Bᵀ = B Bᵀ
    B = np.zeros((6, 3))
    B[1, :] = sigma_eR_S
    B[4, :] = sigma_pT_S
    B[5, :] = sigma_pR_S

    BBT = B @ B.T
    A_eff = A_6x6 - BBT

    # Check positive-definiteness
    eigs = np.linalg.eigvalsh(A_eff)
    if np.any(eigs <= 0):
        return np.nan, np.nan, np.nan

    A_eff_inv = np.linalg.inv(A_eff)
    E2_coupled = n_tilde @ A_eff_inv @ n_tilde

    if E2_coupled <= 0:
        return np.nan, np.nan, np.nan

    alpha_eff = (E2_coupled - E2_bare) / E2_coupled

    return alpha_eff, np.sqrt(max(E2_bare, 0)), np.sqrt(max(E2_coupled, 0))


def universality_score(params, A_6x6, L, charged_modes, neutral_modes):
    """
    Score function for optimization.

    For charged modes: penalize deviation of α_eff from 1/137.
    For neutral modes: penalize nonzero α_eff.

    Returns sum of squared relative errors.
    """
    sigma_eR, sigma_pT, sigma_pR = params

    score = 0.0
    for mode, name, Q in charged_modes:
        a_eff, _, _ = compute_alpha_eff(A_6x6, L, sigma_eR, sigma_pT, sigma_pR, mode)
        if np.isnan(a_eff):
            return 1e10  # penalty for invalid metric
        if Q != 0:
            # Charged: want α_eff = 1/137
            err = (a_eff - ALPHA_TARGET) / ALPHA_TARGET
            score += err ** 2
        else:
            # Neutral: want α_eff = 0
            score += (a_eff / ALPHA_TARGET) ** 2

    return score


def main():
    print("=" * 70)
    print("R55 Track 1: Ma-S Transfer Function")
    print("=" * 70)
    print()

    # ── Build the Ma-only metric from model-E ──────────────────
    m = Metric.model_E()
    A_6x6 = m.Gt    # 6×6 dimensionless metric
    L = m.L          # circumference vector (fm)

    print("Model-E Ma metric (6×6):")
    print(f"  ε = {m.eps}")
    print(f"  s = {m.shears}")
    print(f"  L = [{', '.join(f'{x:.4g}' for x in L)}] fm")
    print()

    # ── Phase 1: Single-parameter exploration ──────────────────
    # First, explore with a single coupling strength σ
    # and equal magnitude on all active dimensions
    # (signs: e-ring negative, p-tube positive, p-ring positive)

    print("─" * 70)
    print("Phase 1: Single-parameter sweep (σ_eR = -σ, σ_pT = +σ, σ_pR = +σ)")
    print("─" * 70)
    print()

    print(f"  {'σ':>10s}", end="")
    for _, name, Q in TEST_MODES:
        print(f"  {name:>12s}", end="")
    print()
    print(f"  {'─'*10}", end="")
    for _ in TEST_MODES:
        print(f"  {'─'*12}", end="")
    print()

    for sigma in np.logspace(-4, -0.3, 30):
        sigma_eR = -sigma   # negative for electron charge
        sigma_pT = +sigma   # positive for proton charge
        sigma_pR = +sigma   # positive for proton charge

        print(f"  {sigma:>10.6f}", end="")
        for mode, name, Q in TEST_MODES:
            a_eff, _, _ = compute_alpha_eff(
                A_6x6, L, sigma_eR, sigma_pT, sigma_pR, mode)
            if np.isnan(a_eff):
                print(f"  {'NaN':>12s}", end="")
            else:
                marker = " ◄" if abs(a_eff - ALPHA_TARGET) / ALPHA_TARGET < 0.1 else ""
                print(f"  {a_eff:>10.6f}{marker}", end="")
        print()

    print()

    # ── Phase 2: Independent parameter sweep ───────────────────
    # Allow e-ring and p-ring/p-tube couplings to differ

    print("─" * 70)
    print("Phase 2: Two-parameter sweep (σ_e, σ_p independent)")
    print("─" * 70)
    print()

    best_score = 1e10
    best_params = None

    for sigma_e in np.logspace(-4, -0.3, 50):
        for sigma_p in np.logspace(-4, -0.3, 50):
            sigma_eR = -sigma_e
            sigma_pT = +sigma_p
            sigma_pR = +sigma_p

            alphas = {}
            valid = True
            for mode, name, Q in TEST_MODES:
                a_eff, _, _ = compute_alpha_eff(
                    A_6x6, L, sigma_eR, sigma_pT, sigma_pR, mode)
                if np.isnan(a_eff):
                    valid = False
                    break
                alphas[name] = (a_eff, Q)

            if not valid:
                continue

            # Score: charged modes should have α_eff = 1/137
            #        neutral modes should have α_eff = 0
            score = 0.0
            for name, (a_eff, Q) in alphas.items():
                if Q != 0:
                    score += ((a_eff - ALPHA_TARGET) / ALPHA_TARGET) ** 2
                else:
                    score += (a_eff / ALPHA_TARGET) ** 2

            if score < best_score:
                best_score = score
                best_params = (sigma_e, sigma_p, alphas)

    if best_params:
        sigma_e, sigma_p, alphas = best_params
        print(f"  Best fit: σ_e = {sigma_e:.6f}, σ_p = {sigma_p:.6f}")
        print(f"  Score: {best_score:.6e}")
        print()
        print(f"  {'Mode':>12s}  {'Q':>4s}  {'α_eff':>12s}  {'target':>12s}  {'error':>10s}")
        print(f"  {'─'*12}  {'─'*4}  {'─'*12}  {'─'*12}  {'─'*10}")
        for name, (a_eff, Q) in alphas.items():
            target = ALPHA_TARGET if Q != 0 else 0.0
            if target > 0:
                err = f"{(a_eff - target)/target*100:+.2f}%"
            else:
                err = f"{a_eff:.2e}"
            print(f"  {name:>12s}  {Q:>+4d}  {a_eff:>12.6f}  {target:>12.6f}  {err:>10s}")
    else:
        print("  No valid solution found in grid search.")

    print()

    # ── Phase 3: Three-parameter optimization ──────────────────
    # Allow σ_pT and σ_pR to differ

    print("─" * 70)
    print("Phase 3: Three-parameter optimization (σ_eR, σ_pT, σ_pR independent)")
    print("─" * 70)
    print()

    all_modes = TEST_MODES

    # Fine grid search: allow σ_pT and σ_pR to differ
    best_score3 = 1e10
    best_params3 = None

    for sigma_e in np.logspace(-4, -0.3, 40):
        for sigma_pT_v in np.logspace(-4, -0.3, 40):
            for sigma_pR_v in [sigma_pT_v * r for r in [0.5, 0.8, 1.0, 1.2, 1.5, 2.0]]:
                s_eR = -sigma_e
                s_pT = +sigma_pT_v
                s_pR = +sigma_pR_v

                score = 0.0
                valid = True
                for mode, name, Q in all_modes:
                    a_eff, _, _ = compute_alpha_eff(A_6x6, L, s_eR, s_pT, s_pR, mode)
                    if np.isnan(a_eff):
                        valid = False
                        break
                    if Q != 0:
                        score += ((a_eff - ALPHA_TARGET) / ALPHA_TARGET) ** 2
                    else:
                        score += (a_eff / ALPHA_TARGET) ** 2

                if valid and score < best_score3:
                    best_score3 = score
                    best_params3 = (s_eR, s_pT, s_pR)

    # Local refinement around best point
    if best_params3:
        eR0, pT0, pR0 = best_params3
        for de in np.linspace(-abs(eR0)*0.3, abs(eR0)*0.3, 20):
            for dpT in np.linspace(-abs(pT0)*0.3, abs(pT0)*0.3, 20):
                for dpR in np.linspace(-abs(pR0)*0.3, abs(pR0)*0.3, 20):
                    s_eR = eR0 + de
                    s_pT = pT0 + dpT
                    s_pR = pR0 + dpR

                    score = 0.0
                    valid = True
                    for mode, name, Q in all_modes:
                        a_eff, _, _ = compute_alpha_eff(A_6x6, L, s_eR, s_pT, s_pR, mode)
                        if np.isnan(a_eff):
                            valid = False
                            break
                        if Q != 0:
                            score += ((a_eff - ALPHA_TARGET) / ALPHA_TARGET) ** 2
                        else:
                            score += (a_eff / ALPHA_TARGET) ** 2

                    if valid and score < best_score3:
                        best_score3 = score
                        best_params3 = (s_eR, s_pT, s_pR)

    if best_params3 and best_score3 < 1e5:
        sigma_eR, sigma_pT, sigma_pR = best_params3
        print(f"  Optimized Ma-S coupling:")
        print(f"    σ(e-ring → S) = {sigma_eR:+.8f}")
        print(f"    σ(p-tube → S) = {sigma_pT:+.8f}")
        print(f"    σ(p-ring → S) = {sigma_pR:+.8f}")
        print(f"  Optimization score: {best_score3:.6e}")
        print()

        print(f"  {'Mode':>12s}  {'Q':>4s}  {'α_eff':>12s}  {'target':>12s}  {'error':>10s}")
        print(f"  {'─'*12}  {'─'*4}  {'─'*12}  {'─'*12}  {'─'*10}")
        for mode, name, Q in TEST_MODES:
            a_eff, E_bare, E_coupled = compute_alpha_eff(
                A_6x6, L, sigma_eR, sigma_pT, sigma_pR, mode)
            target = ALPHA_TARGET if Q != 0 else 0.0
            if target > 0:
                err = f"{(a_eff - target)/target*100:+.2f}%"
            else:
                err = f"{a_eff:.2e}"
            print(f"  {name:>12s}  {Q:>+4d}  {a_eff:>12.8f}  {target:>12.6f}  {err:>10s}")

        print()
        print("  Universality assessment:")
        charged_alphas = []
        for mode, name, Q in TEST_MODES:
            if Q != 0:
                a_eff, _, _ = compute_alpha_eff(
                    A_6x6, L, sigma_eR, sigma_pT, sigma_pR, mode)
                charged_alphas.append(a_eff)

        if charged_alphas:
            spread = (max(charged_alphas) - min(charged_alphas)) / np.mean(charged_alphas)
            print(f"    Charged mode α_eff range: {min(charged_alphas):.8f} – {max(charged_alphas):.8f}")
            print(f"    Spread: {spread*100:.4f}%")
            print(f"    Mean: {np.mean(charged_alphas):.8f}")
            print(f"    Target: {ALPHA_TARGET:.8f}")
            if spread < 0.01:
                print(f"    → UNIVERSAL to < 1% — α is geometrically determined")
            elif spread < 0.1:
                print(f"    → Nearly universal ({spread*100:.1f}% spread)")
            else:
                print(f"    → NOT universal ({spread*100:.1f}% spread) — model has a problem")
    else:
        print("  Optimization failed to converge.")

    print()
    print("Track 1 complete.")


if __name__ == '__main__':
    main()
