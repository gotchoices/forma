"""
R55 Track 3b: Fine-tune σℵS for exact α, re-scan particle inventory.

Hypothesis F established:
  - Ma-ℵ coupling: ring dimensions at ±1/(2π), tubes = 0
  - ℵ-S coupling: σℵS (single parameter)
  - Effective Ma-S: ring→S at ±(1/2π)×σℵS, tube→S = 0
  - Universal α across e and p sheets to ~4%

This script:
  1. Binary search for σℵS that gives exact α for the electron
  2. Check universality: does the same σℵS give α for the proton?
  3. Re-scan the full model-E particle inventory on the 10D metric
  4. Assess spectrum shifts and whether re-tuning is needed
  5. Build the 10×10 metric reference table
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from lib.metric import Metric

ALPHA = 1.0 / 137.036
SQRT_ALPHA = np.sqrt(ALPHA)
TWO_PI = 2 * np.pi
INV_2PI = 1.0 / TWO_PI
TWO_PI_HC = 197.3269804 * TWO_PI

m = Metric.model_E()
A_6x6 = m.Gt
L_6 = m.L
L_9 = np.concatenate([L_6, [1.0, 1.0, 1.0]])

# Hypothesis F: ring-only coupling
SIGMA_MA_ALEPH_F = np.array([0, -INV_2PI, 0, +INV_2PI, 0, +INV_2PI])

# Full model-E particle inventory
PARTICLES = [
    ('electron',   (1, 2, 0, 0, 0, 0),      0.511,    -1, True),
    ('proton',     (0, 0, -2, 2, 1, 3),    938.272,    +1, True),
    ('neutron',    (0, -4, -1, 2, 0, -3),  939.565,     0, False),
    ('muon',       (3, 8, 0, 0, 0, 0),     105.658,    -3, False),
    ('ν₁',        (0, 0, 1, 1, 0, 0),        2.92e-5,  0, True),
    ('ν₂',        (0, 0, -1, 1, 0, 0),       3.05e-5,  0, True),
    ('ν₃',        (0, 0, 1, 2, 0, 0),        5.82e-5,  0, True),
    ('tau_cand',   (3, -6, 2, -2, 2, 3),  1776.86,     -1, False),
    ('Λ',         (-1, 2, -1, 2, -1, 3),  1115.68,      0, False),
    ("η'",        (-1, -7, 2, -2, -1, 2),  957.78,      0, False),
    ('Σ⁻',        (-1, 2, -2, 2, -2, -2), 1197.45,     -1, False),
    ('Σ⁺',        (-2, 3, 2, -2, -1, -3), 1189.37,     +1, False),
    ('Ξ⁻',        (-1, 5, -2, 2, -2, 1),  1321.71,     -1, False),
    ('φ',         (-1, 4, 2, -2, -1, 2),  1019.46,      0, False),
    ('Ξ⁰',       (-1, 8, -3, 3, -1, 2),  1314.86,      0, False),
    ('ρ',         (-1, 5, -2, 2, 0, 1),    775.26,      0, False),
    ('K⁰',        (0, -4, -2, 2, 0, 1),    497.61,      0, False),
    ('K±',        (-1, -6, -2, 2, 0, 1),   493.68,     -1, False),
    ('η',         (-1, -4, -2, 2, -1, 0),  547.86,      0, False),
    ('π⁰',        (0, -1, -2, -2, 0, 0),   135.0,       0, False),
    ('π±',        (-1, -1, -3, -3, 0, 0),  139.6,      -1, False),
    ('deuteron',   (0, 0, 0, 0, 2, 6),    1875.61,     +2, False),
    ('⁴He',       (0, 0, 0, 0, 4, 12),    3727.38,     +2, False),
    ('¹²C',       (0, 0, 0, 0, 12, 36),  11174.86,     +6, False),
    ('⁵⁶Fe',      (0, 0, 0, 0, 56, 168), 52089.8,     +26, False),
]


def build_10x10(sigma_ma_aleph, sigma_aleph_s):
    G10 = np.zeros((10, 10))
    G10[:6, :6] = A_6x6
    G10[6, 6] = 1.0
    for j in range(7, 10):
        G10[j, j] = 1.0
    for i in range(6):
        G10[i, 6] = sigma_ma_aleph[i]
        G10[6, i] = sigma_ma_aleph[i]
    for j in range(7, 10):
        G10[6, j] = sigma_aleph_s
        G10[j, 6] = sigma_aleph_s
    return G10


def integrate_out_aleph(G10):
    keep = [0, 1, 2, 3, 4, 5, 7, 8, 9]
    M = G10[np.ix_(keep, keep)]
    b = G10[keep, 6]
    g = G10[6, 6]
    return M - np.outer(b, b) / g


def mode_energy_6d(n6):
    return m.mode_energy(n6)


def mode_energy_9d(G9, n6):
    n9 = np.concatenate([np.array(n6, dtype=float) / L_9[:6], [0, 0, 0]])
    try:
        G9i = np.linalg.inv(G9)
        E2 = TWO_PI_HC**2 * n9 @ G9i @ n9
    except:
        return np.nan
    return np.sqrt(max(E2, 0))


def alpha_eff(G9, n6):
    n_ma = np.array(n6, dtype=float) / L_9[:6]
    A_bare = G9[:6, :6]
    try:
        E2_bare = TWO_PI_HC**2 * n_ma @ np.linalg.inv(A_bare) @ n_ma
        n9 = np.concatenate([n_ma, [0, 0, 0]])
        E2_coupled = TWO_PI_HC**2 * n9 @ np.linalg.inv(G9) @ n9
    except:
        return np.nan
    if E2_coupled <= 0:
        return np.nan
    return (E2_coupled - E2_bare) / E2_coupled


def main():
    print("=" * 75)
    print("R55 Track 3b: Fine-tune σℵS and re-scan particle inventory")
    print("=" * 75)
    print()
    print(f"  Hypothesis F: ring-only Ma-ℵ coupling at ±1/(2π)")
    print(f"  Ma-ℵ = [0, {-INV_2PI:+.6f}, 0, {+INV_2PI:+.6f}, 0, {+INV_2PI:+.6f}]")
    print(f"  ℵ-S = σℵS (to be determined)")
    print(f"  Target: α_eff(electron) = α = {ALPHA:.6e}")
    print()

    # ── Step 1: Binary search for σℵS ──────────────────────
    print("─" * 75)
    print("Step 1: Fine-tune σℵS for exact α(electron)")
    print("─" * 75)
    print()

    lo, hi = 0.1, 0.5
    for _ in range(100):
        mid = (lo + hi) / 2
        G10 = build_10x10(SIGMA_MA_ALEPH_F, mid)
        eigs = np.linalg.eigvalsh(G10)
        if not np.all(eigs > 0):
            hi = mid
            continue
        G9 = integrate_out_aleph(G10)
        ae = alpha_eff(G9, PARTICLES[0][1])  # electron
        if np.isnan(ae):
            hi = mid
        elif ae < ALPHA:
            lo = mid
        else:
            hi = mid

    sigma_opt = (lo + hi) / 2
    G10_opt = build_10x10(SIGMA_MA_ALEPH_F, sigma_opt)
    G9_opt = integrate_out_aleph(G10_opt)

    ae = alpha_eff(G9_opt, PARTICLES[0][1])
    ap = alpha_eff(G9_opt, PARTICLES[1][1])
    anu = alpha_eff(G9_opt, PARTICLES[4][1])

    print(f"  Optimal σℵS = {sigma_opt:.8f}")
    print(f"  Effective ℵ-S product: 1/(2π) × σℵS = {INV_2PI * sigma_opt:.8f}")
    print(f"  (√α = {SQRT_ALPHA:.8f})")
    print()
    print(f"  α_eff(electron) = {ae:.8e}  (target = {ALPHA:.8e}, ratio = {ae/ALPHA:.6f})")
    print(f"  α_eff(proton)   = {ap:.8e}  (ratio = {ap/ALPHA:.6f})")
    print(f"  α_eff(ν₁)       = {anu:.8e}  (ratio = {anu/ALPHA:.6f})")
    print(f"  Universality: |α_e - α_p| / α = {abs(ae - ap)/ALPHA:.4f}")
    print()

    # ── Step 2: Full particle inventory ────────────────────
    print("─" * 75)
    print("Step 2: Particle inventory — 6D vs effective 9D")
    print("─" * 75)
    print()

    print(f"  {'Particle':>10s}  {'Obs (MeV)':>10s}  {'E_6D':>10s}  {'E_9D':>10s}  "
          f"{'Δ6D%':>7s}  {'Δ9D%':>7s}  {'shift%':>7s}  {'Q':>3s}  {'α_eff':>12s}  {'α_eff/α':>8s}")
    print(f"  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*10}  "
          f"{'─'*7}  {'─'*7}  {'─'*7}  {'─'*3}  {'─'*12}  {'─'*8}")

    for name, n6, m_obs, Q, is_stable in PARTICLES:
        E_6d = mode_energy_6d(n6)
        E_9d = mode_energy_9d(G9_opt, n6)
        a_eff = alpha_eff(G9_opt, n6)

        if m_obs > 0:
            d6 = (E_6d - m_obs) / m_obs * 100
            d9 = (E_9d - m_obs) / m_obs * 100
        else:
            d6 = 0
            d9 = 0

        shift = (E_9d - E_6d) / E_6d * 100 if E_6d > 0 else 0

        a_str = f'{a_eff:.4e}' if not np.isnan(a_eff) else 'NaN'
        r_str = f'{a_eff/ALPHA:.4f}' if not np.isnan(a_eff) else ''

        print(f"  {name:>10s}  {m_obs:10.3f}  {E_6d:10.3f}  {E_9d:10.3f}  "
              f"{d6:+7.2f}  {d9:+7.2f}  {shift:+7.3f}  {Q:+3d}  {a_str:>12s}  {r_str:>8s}")

    print()

    # ── Step 3: Effective 9×9 metric — Ma-S block ──────────
    print("─" * 75)
    print("Step 3: Effective Ma-S coupling block")
    print("─" * 75)
    print()

    MaS = G9_opt[:6, 6:]
    dim_names = ['e-tube', 'e-ring', 'ν-tube', 'ν-ring', 'p-tube', 'p-ring']
    s_names = ['S_x', 'S_y', 'S_z']

    print(f"  {'':>10s}", end="")
    for sn in s_names:
        print(f"  {sn:>12s}", end="")
    print(f"  {'ratio/√α':>10s}")

    for i in range(6):
        print(f"  {dim_names[i]:>10s}", end="")
        for j in range(3):
            v = MaS[i, j]
            print(f"  {v:>+12.6f}", end="")
        ratio = MaS[i, 0] / SQRT_ALPHA if abs(SQRT_ALPHA) > 1e-30 else 0
        print(f"  {ratio:>+10.4f}")

    print()
    print(f"  √α = {SQRT_ALPHA:.6f}")
    print(f"  Effective ring→S entries should be ≈ ±√α for exact α coupling")
    print()

    # ── Step 4: The 10×10 metric reference ─────────────────
    print("─" * 75)
    print("Step 4: Full 10×10 metric (for metric-terms.md)")
    print("─" * 75)
    print()

    dim_names_10 = dim_names + ['ℵ'] + s_names

    print("  10×10 metric G̃ (nonzero entries only):")
    print()

    for i in range(10):
        for j in range(i, 10):
            v = G10_opt[i, j]
            if abs(v) > 1e-15:
                print(f"    G̃[{dim_names_10[i]:>8s}, {dim_names_10[j]:>8s}] = {v:>+14.6f}"
                      f"{'  (diagonal)' if i == j else ''}")

    print()

    # ── Step 5: Universality across all charged modes ──────
    print("─" * 75)
    print("Step 5: α universality — all charged particles")
    print("─" * 75)
    print()

    charged = [(n, n6, Q) for n, n6, _, Q, _ in PARTICLES if Q != 0]

    alphas = []
    print(f"  {'Particle':>10s}  {'Q':>3s}  {'α_eff':>12s}  {'α_eff/α':>10s}")
    print(f"  {'─'*10}  {'─'*3}  {'─'*12}  {'─'*10}")

    for name, n6, Q in charged:
        ae = alpha_eff(G9_opt, n6)
        ratio = ae / ALPHA if not np.isnan(ae) else 0
        alphas.append(ae)
        marker = " ✓" if abs(ratio - 1.0) < 0.1 else ""
        print(f"  {name:>10s}  {Q:+3d}  {ae:12.6e}  {ratio:10.4f}{marker}")

    valid_alphas = [a for a in alphas if not np.isnan(a)]
    if valid_alphas:
        mean_a = np.mean(valid_alphas)
        spread = (max(valid_alphas) - min(valid_alphas)) / mean_a * 100
        print()
        print(f"  Mean α_eff: {mean_a:.6e}")
        print(f"  Spread: {spread:.1f}%")
        print(f"  Target: {ALPHA:.6e}")

    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 75)
    print("SUMMARY")
    print("=" * 75)
    print()
    print(f"  σℵS = {sigma_opt:.8f}")
    print(f"  Effective product: (1/2π) × σℵS = {INV_2PI * sigma_opt:.8f}")
    print(f"  √α = {SQRT_ALPHA:.8f}")
    print(f"  Ratio: product / √α = {INV_2PI * sigma_opt / SQRT_ALPHA:.4f}")
    print()
    print(f"  α universality: electron = {ae/ALPHA:.4f}α, proton = {ap/ALPHA:.4f}α")
    print(f"  ν coupling: {anu/ALPHA:.4f}α (nonzero)")
    print()
    print("Track 3b complete.")


if __name__ == '__main__':
    main()
