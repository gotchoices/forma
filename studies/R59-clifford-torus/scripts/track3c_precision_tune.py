"""
R59 Track 3c: Precision tune of the clean-metric tube↔ℵ↔t architecture.

Track 3b F42 found that a shearless Ma metric with tube-based ℵ
mediation produces α_Coulomb ≈ 0.68α at the natural parameter point
(σ_ta, σ_at, g_ℵℵ) = (√α, 1, 1), with exact structural universality
(α_e/α_p = 1.000).

Track 3c asks: what combination gives α_Coulomb = α exactly, and
does that combination take a natural form?

Approach:
1. Fix the architecture (clean Ma + tube↔ℵ + ℵ↔t, symmetric ±
   signs on e/p tubes).
2. Sweep (σ_ta, σ_at, g_ℵℵ) systematically.
3. For each config: extract Q_e (source charge via inverse metric)
   and compute α_Coulomb = Q² / (4π).  Compare to observed α.
4. Report the configurations where α_Coulomb matches α to ≤ 1 %.
5. Check structural universality (α_e / α_p = 1.000) at the match
   points.
6. Analyze whether the matching values take a simple form.

This is a pure numerical sweep — no new physics.  It caps the F42
positive signal precisely and tells us whether the "plug in α, get
α out" intuition survives precision testing.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np

ALPHA = 1.0 / 137.036
SQRT_ALPHA = math.sqrt(ALPHA)

# Mode definitions
MODE_E = (1, 2, 0, 0, 0, 0)
MODE_P = (0, 0, -2, 2, 1, 3)

# Metric indices (11D with ℵ at index 10)
I_E_TUBE = 0
I_P_TUBE = 4
I_T = 9
I_ALEPH = 10


# ═══════════════════════════════════════════════════════════════════
#   Metric builder: clean (shearless) Ma + tube↔ℵ↔t
# ═══════════════════════════════════════════════════════════════════

def build_clean_metric(sigma_ta, sigma_at, g_aa):
    """
    Build the 11D metric:
      - Ma: identity (shearless, no cross-shears)
      - S: identity
      - t: Lorentzian (-1)
      - ℵ: diagonal = g_aa
      - tube↔ℵ: ±sigma_ta (electron +, proton -)
      - ℵ↔t: sigma_at
    """
    G = np.zeros((11, 11))
    for i in range(6):
        G[i, i] = 1.0      # Ma — identity
    G[6, 6] = G[7, 7] = G[8, 8] = 1.0   # S
    G[9, 9] = -1.0                       # t
    G[I_ALEPH, I_ALEPH] = g_aa           # ℵ
    # tube↔ℵ entries
    G[I_E_TUBE, I_ALEPH] = +sigma_ta
    G[I_ALEPH, I_E_TUBE] = +sigma_ta
    G[I_P_TUBE, I_ALEPH] = -sigma_ta
    G[I_ALEPH, I_P_TUBE] = -sigma_ta
    # ℵ↔t
    G[I_ALEPH, I_T] = sigma_at
    G[I_T, I_ALEPH] = sigma_at
    return G


# ═══════════════════════════════════════════════════════════════════
#   α_Coulomb extraction: Q = (n/L) · g^{Ma,t} × (-g^{tt})
# ═══════════════════════════════════════════════════════════════════

def compute_alpha_coulomb(G, n6):
    """
    Extract α_Coulomb for a mode with winding n6.

    On the clean (identity Ma) metric we use L = 1 everywhere, so
    n_tilde = n6 directly.  The source charge Q is extracted from
    the inverse metric's Ma-t block (which includes the ℵ chain
    contribution automatically):
        Q = (n · g^{Ma,t}) × (-g^{tt})
    α_Coulomb = Q² / (4π).

    Returns (Q, α_Coulomb).  Returns (nan, nan) if the metric is
    non-invertible.
    """
    try:
        G_inv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return float('nan'), float('nan')
    n_tilde = np.zeros(G.shape[0])
    n_tilde[:6] = np.asarray(n6, dtype=float)  # L = 1 on clean metric
    Q = float((n_tilde[:6] @ G_inv[:6, I_T]) * (-G_inv[I_T, I_T]))
    alpha = Q * Q / (4 * math.pi)
    return Q, alpha


def check_signature(G):
    """Return True if the metric has exactly one negative eigenvalue."""
    eigs = np.linalg.eigvalsh(G)
    return int(np.sum(eigs < 0)) == 1


# ═══════════════════════════════════════════════════════════════════
#   Sweep utilities
# ═══════════════════════════════════════════════════════════════════

def evaluate_config(sigma_ta, sigma_at, g_aa):
    """Return a dict summarizing one parameter combination."""
    G = build_clean_metric(sigma_ta, sigma_at, g_aa)
    sig_ok = check_signature(G)
    if not sig_ok:
        return {
            'sigma_ta': sigma_ta, 'sigma_at': sigma_at, 'g_aa': g_aa,
            'sig_ok': False,
            'Q_e': float('nan'), 'Q_p': float('nan'),
            'alpha_e': float('nan'), 'alpha_p': float('nan'),
            'ratio_e': float('nan'), 'ratio_p': float('nan'),
            'universal': False,
        }
    Q_e, alpha_e = compute_alpha_coulomb(G, MODE_E)
    Q_p, alpha_p = compute_alpha_coulomb(G, MODE_P)
    ratio_e = alpha_e / ALPHA if not math.isnan(alpha_e) else float('nan')
    ratio_p = alpha_p / ALPHA if not math.isnan(alpha_p) else float('nan')
    # Structural universality: α_e/α_p should be very close to 1.
    universal = (
        not math.isnan(alpha_p) and alpha_p > 0 and
        abs(alpha_e / alpha_p - 1.0) < 1e-6
    )
    return {
        'sigma_ta': sigma_ta, 'sigma_at': sigma_at, 'g_aa': g_aa,
        'sig_ok': True,
        'Q_e': Q_e, 'Q_p': Q_p,
        'alpha_e': alpha_e, 'alpha_p': alpha_p,
        'ratio_e': ratio_e, 'ratio_p': ratio_p,
        'universal': universal,
    }


# ═══════════════════════════════════════════════════════════════════
#   Main
# ═══════════════════════════════════════════════════════════════════

def main():
    print('=' * 82)
    print('R59 Track 3c — Precision tune of clean-metric tube↔ℵ↔t architecture')
    print('=' * 82)
    print()
    print(f'  α = {ALPHA:.10f}')
    print(f'  √α = {SQRT_ALPHA:.10f}')
    print()
    print('  Architecture (fixed): clean Ma (identity), tube↔ℵ with ± signs')
    print('  for e/p, single ℵ↔t entry.  Parameters to tune: σ_ta, σ_at, g_aa.')
    print()
    print('  Baseline from F42:')
    print('    (σ_ta, σ_at, g_aa) = (√α, 1, 1) → α_Coulomb = 0.68α')
    print()

    # ── Section 1: 1D sweep along σ_at with σ_ta=√α, g_aa=1 ──
    print('─' * 82)
    print('  Section 1: Sweep σ_at (with σ_ta = √α, g_aa = 1)')
    print('─' * 82)
    print()
    print('  F42 had σ_at = 1 giving 0.68α.  Scan up (where α grows) and down')
    print('  to find the combinatino where α_Coulomb = α exactly.')
    print()
    print(f'  {"σ_at":>12s}  {"sig":>4s}  {"Q_e":>14s}  '
          f'{"α_e/α":>12s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*12}  {"-"*4}  {"-"*14}  {"-"*12}  {"-"*10}')

    # Fine scan around σ_at = 1–2
    sigma_at_values = np.concatenate([
        np.array([0.5, 0.75, 0.9, 1.0]),
        np.linspace(1.05, 1.5, 10),
        np.array([1.6, 1.8, 2.0, 2.5, 3.0]),
    ])
    best_by_ratio = None
    for s_at in sigma_at_values:
        r = evaluate_config(SQRT_ALPHA, s_at, 1.0)
        marker = ''
        if r['sig_ok']:
            if abs(r['ratio_e'] - 1.0) < 0.01:
                marker = '   ← α match'
                if (best_by_ratio is None or
                    abs(r['ratio_e'] - 1.0) < abs(best_by_ratio['ratio_e'] - 1.0)):
                    best_by_ratio = r
        sig_str = 'YES' if r['sig_ok'] else 'no'
        if r['sig_ok']:
            ae_ratio = f'{r["ratio_e"]:12.4f}'
            eq_ratio = (f'{r["alpha_e"]/r["alpha_p"]:10.6f}'
                        if r['alpha_p'] != 0 else '     —    ')
            q_e = f'{r["Q_e"]:+14.6e}'
        else:
            ae_ratio = '     —    '
            eq_ratio = '     —    '
            q_e = '     —        '
        print(f'  {s_at:12.4f}  {sig_str:>4s}  {q_e}  {ae_ratio}  '
              f'{eq_ratio}{marker}')

    if best_by_ratio:
        print()
        print(f'  Closest match to α at σ_ta=√α, g_aa=1:')
        print(f'    σ_at = {best_by_ratio["sigma_at"]:.6f}')
        print(f'    α_e / α = {best_by_ratio["ratio_e"]:.6f}')
        print(f'    α_e / α_p = {best_by_ratio["alpha_e"]/best_by_ratio["alpha_p"]:.10f}')

    # ── Section 2: 1D sweep along g_aa with σ_ta=√α, σ_at=1 ──
    print()
    print('─' * 82)
    print('  Section 2: Sweep g_aa (with σ_ta = √α, σ_at = 1)')
    print('─' * 82)
    print()
    print('  Alternative axis to find α match: vary g_aa.  Smaller g_aa')
    print('  amplifies via Schur (F42 showed at g_aa=0.1 α grows to ~8α).')
    print()
    print(f'  {"g_aa":>12s}  {"sig":>4s}  {"Q_e":>14s}  '
          f'{"α_e/α":>12s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*12}  {"-"*4}  {"-"*14}  {"-"*12}  {"-"*10}')

    g_aa_values = np.concatenate([
        np.array([5.0, 3.0, 2.0, 1.5]),
        np.linspace(1.0, 0.5, 11),
        np.array([0.4, 0.3, 0.2, 0.15, 0.1]),
    ])
    best_by_g = None
    for g_aa in g_aa_values:
        r = evaluate_config(SQRT_ALPHA, 1.0, g_aa)
        marker = ''
        if r['sig_ok']:
            if abs(r['ratio_e'] - 1.0) < 0.01:
                marker = '   ← α match'
                if (best_by_g is None or
                    abs(r['ratio_e'] - 1.0) < abs(best_by_g['ratio_e'] - 1.0)):
                    best_by_g = r
        sig_str = 'YES' if r['sig_ok'] else 'no'
        if r['sig_ok']:
            ae_ratio = f'{r["ratio_e"]:12.4f}'
            eq_ratio = (f'{r["alpha_e"]/r["alpha_p"]:10.6f}'
                        if r['alpha_p'] != 0 else '     —    ')
            q_e = f'{r["Q_e"]:+14.6e}'
        else:
            ae_ratio = '     —    '
            eq_ratio = '     —    '
            q_e = '     —        '
        print(f'  {g_aa:12.4f}  {sig_str:>4s}  {q_e}  {ae_ratio}  '
              f'{eq_ratio}{marker}')

    if best_by_g:
        print()
        print(f'  Closest match to α at σ_ta=√α, σ_at=1:')
        print(f'    g_aa = {best_by_g["g_aa"]:.6f}')
        print(f'    α_e / α = {best_by_g["ratio_e"]:.6f}')

    # ── Section 3: 1D sweep along σ_ta with σ_at=1, g_aa=1 ──
    print()
    print('─' * 82)
    print('  Section 3: Sweep σ_ta (with σ_at = 1, g_aa = 1)')
    print('─' * 82)
    print()
    print('  If the tube-ℵ entry is not exactly √α, what value hits α?')
    print()
    print(f'  {"σ_ta":>12s}  {"sig":>4s}  {"Q_e":>14s}  '
          f'{"α_e/α":>12s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*12}  {"-"*4}  {"-"*14}  {"-"*12}  {"-"*10}')

    sigma_ta_values = np.concatenate([
        np.array([0.02, 0.05]),
        np.linspace(0.07, 0.15, 17),
        np.array([0.2, 0.3, 0.5]),
        np.linspace(0.55, 0.90, 36),   # fine scan near divergence
        np.array([0.95, 1.0, 1.2, 1.5, 2.0]),
    ])
    best_by_ta = None
    for s_ta in sigma_ta_values:
        r = evaluate_config(s_ta, 1.0, 1.0)
        marker = ''
        if r['sig_ok']:
            if abs(r['ratio_e'] - 1.0) < 0.01:
                marker = '   ← α match'
                if (best_by_ta is None or
                    abs(r['ratio_e'] - 1.0) < abs(best_by_ta['ratio_e'] - 1.0)):
                    best_by_ta = r
        sig_str = 'YES' if r['sig_ok'] else 'no'
        if r['sig_ok']:
            ae_ratio = f'{r["ratio_e"]:12.4f}'
            eq_ratio = (f'{r["alpha_e"]/r["alpha_p"]:10.6f}'
                        if r['alpha_p'] != 0 else '     —    ')
            q_e = f'{r["Q_e"]:+14.6e}'
        else:
            ae_ratio = '     —    '
            eq_ratio = '     —    '
            q_e = '     —        '
        print(f'  {s_ta:12.4f}  {sig_str:>4s}  {q_e}  {ae_ratio}  '
              f'{eq_ratio}{marker}')

    if best_by_ta:
        print()
        print(f'  Closest match to α at σ_at=1, g_aa=1:')
        print(f'    σ_ta = {best_by_ta["sigma_ta"]:.6f}')
        print(f'    σ_ta / √α = {best_by_ta["sigma_ta"] / SQRT_ALPHA:.6f}')
        print(f'    α_e / α = {best_by_ta["ratio_e"]:.6f}')

    # ── Section 4: Narrowed sweep to find exact match ──
    print()
    print('─' * 82)
    print('  Section 4: Combined 2D scan — fixing σ_ta=√α, scanning (σ_at, g_aa)')
    print('─' * 82)
    print()
    print('  Find combinations where α_Coulomb = α to ≤ 0.1%.')
    print()

    exact_matches = []
    for s_at in np.linspace(1.0, 2.0, 21):
        for g_aa in np.linspace(0.3, 1.0, 15):
            r = evaluate_config(SQRT_ALPHA, s_at, g_aa)
            if r['sig_ok'] and abs(r['ratio_e'] - 1.0) < 0.001:
                exact_matches.append(r)

    print(f'  Found {len(exact_matches)} matches to within 0.1% of α.  Sample:')
    print()
    print(f'  {"σ_at":>8s}  {"g_aa":>8s}  {"α_e/α":>10s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*8}  {"-"*8}  {"-"*10}  {"-"*10}')
    for r in sorted(exact_matches,
                    key=lambda d: abs(d['ratio_e'] - 1.0))[:15]:
        print(f'  {r["sigma_at"]:8.4f}  {r["g_aa"]:8.4f}  '
              f'{r["ratio_e"]:10.6f}  {r["alpha_e"]/r["alpha_p"]:10.8f}')

    # ── Section 5: Analyze tuning naturalness ──
    print()
    print('─' * 82)
    print('  Section 5: Does the tuning take a natural form?')
    print('─' * 82)
    print()

    # Best single-parameter tunings
    print('  Natural-looking candidates:')
    print()
    natural_candidates = [
        ('√α, 1, 1 (F42 baseline)', SQRT_ALPHA, 1.0, 1.0),
        ('√α, 1, 2/3', SQRT_ALPHA, 1.0, 2/3),
        ('√α, 1, 1/√2', SQRT_ALPHA, 1.0, 1/math.sqrt(2)),
        ('√α, 1, 1/2', SQRT_ALPHA, 1.0, 0.5),
        ('√α, 4/π, 1', SQRT_ALPHA, 4/math.pi, 1.0),
        ('√α, π/2, 1', SQRT_ALPHA, math.pi/2, 1.0),
        ('√α, √(4π/3), 1', SQRT_ALPHA, math.sqrt(4*math.pi/3), 1.0),
        ('1/(2π), 1, 1', 1/(2*math.pi), 1.0, 1.0),
        ('α, 1, α', ALPHA, 1.0, ALPHA),
    ]
    print(f'  {"Combination":>30s}  {"α_e/α":>10s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*30}  {"-"*10}  {"-"*10}')
    for name, s_ta, s_at, g_aa in natural_candidates:
        r = evaluate_config(s_ta, s_at, g_aa)
        if r['sig_ok']:
            eq = (f'{r["alpha_e"]/r["alpha_p"]:10.6f}'
                  if r['alpha_p'] != 0 else '     —    ')
            print(f'  {name:>30s}  {r["ratio_e"]:10.4f}  {eq}')
        else:
            print(f'  {name:>30s}  {"no sig":>10s}  {"":>10s}')

    # ── Summary ──
    print()
    print('=' * 82)
    print('  SUMMARY')
    print('=' * 82)
    print()

    if best_by_ratio:
        print(f'  Best σ_at alone (σ_ta=√α, g_aa=1): {best_by_ratio["sigma_at"]:.4f}')
        print(f'    → α_e = {best_by_ratio["ratio_e"]:.4f}α')
    if best_by_g:
        print(f'  Best g_aa alone (σ_ta=√α, σ_at=1): {best_by_g["g_aa"]:.4f}')
        print(f'    → α_e = {best_by_g["ratio_e"]:.4f}α')

    if exact_matches:
        simplest = min(exact_matches,
                       key=lambda d: (abs(d['sigma_at'] - 1.0) +
                                      abs(d['g_aa'] - 1.0)))
        print()
        print(f'  Simplest 2D match (σ_at, g_aa closest to (1, 1)):')
        print(f'    σ_ta = √α  (fixed)')
        print(f'    σ_at = {simplest["sigma_at"]:.4f}')
        print(f'    g_aa = {simplest["g_aa"]:.4f}')
        print(f'    α_e / α = {simplest["ratio_e"]:.6f}')
        print(f'    α_e / α_p = {simplest["alpha_e"]/simplest["alpha_p"]:.10f}')

    print()
    print('  Structural universality (α_e / α_p = 1.000) is preserved at')
    print('  every matching point — it is an architectural property, not')
    print('  tuning-dependent.')
    print()
    print('Track 3c complete.')


if __name__ == '__main__':
    main()
