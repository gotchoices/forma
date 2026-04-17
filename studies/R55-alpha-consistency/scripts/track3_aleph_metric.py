"""
R55 Track 3: The ℵ-mediated coupling (10×10 metric)

Build the 10×10 metric with the ℵ dimension mediating Ma-S coupling.
The coupling path is Ma → ℵ → S, not Ma → S directly.

Dimensions:
  0: e-tube    (Ma₁)
  1: e-ring    (Ma₂)
  2: ν-tube    (Ma₃)
  3: ν-ring    (Ma₄)
  4: p-tube    (Ma₅)
  5: p-ring    (Ma₆)
  6: ℵ (aleph) — Planck-scale internal edge dimension
  7: S_x
  8: S_y
  9: S_z

Structure:
  - Ma block (0-5): model-E 6×6 metric (unchanged)
  - ℵ diagonal (6,6): 1 (Planck scale = unity)
  - Ma-ℵ (column 6): ±1 for tube dims (charge sign), 0 for ring
  - ℵ-S (row 6, cols 7-9): √α (isotropic)
  - Ma-S (0-5 × 7-9): ZERO — coupling goes through ℵ
  - S block (7-9): identity (flat space)

Test:
  1. Verify particle spectrum unchanged (ℵ at Planck scale
     is invisible to Ma modes)
  2. Integrate out ℵ → effective 9×9 metric
  3. Check: does effective Ma-S coupling = ±√α?
  4. Check: is α universal across all charged modes?
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from lib.metric import Metric

ALPHA = 1.0 / 137.036
SQRT_ALPHA = np.sqrt(ALPHA)
E_CHARGE = np.sqrt(4 * np.pi * ALPHA)

# Reference model-E metric
m = Metric.model_E()
A_6x6 = m.Gt       # 6×6 dimensionless Ma metric
L_6 = m.L           # circumferences (fm)

# Model-E modes
MODES = {
    'electron':    (1, 2, 0, 0, 0, 0),
    'proton':      (0, 0, -2, 2, 1, 3),
    'neutron':     (0, 0, -4, -1, 2, 0),
    'muon_R53':    (3, 8, 0, 0, 0, 0),
    'ν₁':          (0, 0, 1, 1, 0, 0),
    'ν₂':          (0, 0, -1, 1, 0, 0),
    'Λ':           (-1, 2, -1, 2, -1, 3),
    'deuteron':    (0, 0, 0, 0, 2, 6),
}


def build_10x10(A_6x6, sigma_aleph_ma, sigma_aleph_s):
    """
    Build the 10×10 metric with ℵ dimension.

    Parameters
    ----------
    A_6x6 : ndarray (6,6) — Ma metric (dimensionless)
    sigma_aleph_ma : ndarray (6,) — Ma-ℵ coupling for each Ma dim
    sigma_aleph_s : float — ℵ-S coupling (isotropic)

    Returns
    -------
    G10 : ndarray (10,10)
    """
    G10 = np.zeros((10, 10))

    # Ma block (0-5)
    G10[:6, :6] = A_6x6

    # ℵ diagonal (6,6) = 1 (Planck scale)
    G10[6, 6] = 1.0

    # S block (7-9) = identity
    G10[7, 7] = 1.0
    G10[8, 8] = 1.0
    G10[9, 9] = 1.0

    # Ma-ℵ coupling (column 6, rows 0-5)
    for i in range(6):
        G10[i, 6] = sigma_aleph_ma[i]
        G10[6, i] = sigma_aleph_ma[i]

    # ℵ-S coupling (row 6, cols 7-9) — isotropic
    for j in range(7, 10):
        G10[6, j] = sigma_aleph_s
        G10[j, 6] = sigma_aleph_s

    # Ma-S block (0-5 × 7-9) = ZERO
    # (coupling goes through ℵ, not directly)

    # S-S off-diagonal = 0 (flat space)

    return G10


def integrate_out_aleph(G10):
    """
    Integrate out the ℵ dimension (index 6) using the Schur complement.

    G10 = | M   b |   M = 9×9 (Ma+S without ℵ), b = 9×1 (coupling to ℵ)
          | bᵀ  g |   g = scalar (ℵ diagonal)

    Effective 9×9 = M - b bᵀ / g

    But we need to be careful about the ordering. ℵ is at index 6,
    between Ma (0-5) and S (7-9). We need to extract:
      - The 9×9 block excluding row/col 6
      - The coupling vector (row/col 6, excluding diagonal)
      - The ℵ diagonal
    """
    # Indices of non-ℵ dimensions
    keep = [0, 1, 2, 3, 4, 5, 7, 8, 9]

    M_9x9 = G10[np.ix_(keep, keep)]
    b = G10[keep, 6]  # 9-vector: coupling of each non-ℵ dim to ℵ
    g = G10[6, 6]     # ℵ diagonal

    # Schur complement: effective = M - b bᵀ / g
    G9_eff = M_9x9 - np.outer(b, b) / g

    return G9_eff


def mode_energy_10d(G10, L_10, n_10):
    """
    Compute mode energy on the 10×10 metric.

    L_10: circumferences for all 10 dimensions
    n_10: winding numbers for all 10 dimensions
    """
    n_tilde = np.array(n_10, dtype=float) / L_10
    TWO_PI_HC = 197.3269804 * 2 * np.pi

    try:
        G10_inv = np.linalg.inv(G10)
    except np.linalg.LinAlgError:
        return np.nan

    E2 = TWO_PI_HC**2 * n_tilde @ G10_inv @ n_tilde
    return np.sqrt(max(E2, 0))


def mode_energy_9d(G9, L_9, n_9):
    """Compute mode energy on a 9×9 metric."""
    n_tilde = np.array(n_9, dtype=float) / L_9
    TWO_PI_HC = 197.3269804 * 2 * np.pi

    try:
        G9_inv = np.linalg.inv(G9)
    except np.linalg.LinAlgError:
        return np.nan

    E2 = TWO_PI_HC**2 * n_tilde @ G9_inv @ n_tilde
    return np.sqrt(max(E2, 0))


def compute_alpha_eff(G9_eff, L_9, n_9):
    """
    Compute effective α for a mode on the 9×9 effective metric.

    Compare the mode energy with and without the Ma-S coupling
    (which comes from integrating out ℵ).

    α_eff = (E²_coupled - E²_bare) / E²_coupled
    """
    n_tilde = np.array(n_9, dtype=float) / L_9
    TWO_PI_HC = 197.3269804 * 2 * np.pi

    # Bare: Ma-only (6×6 block, no S coupling)
    A_bare = G9_eff[:6, :6]
    try:
        A_inv = np.linalg.inv(A_bare)
    except np.linalg.LinAlgError:
        return np.nan

    n_ma = n_tilde[:6]
    E2_bare = TWO_PI_HC**2 * n_ma @ A_inv @ n_ma

    # Coupled: full 9×9 effective metric
    try:
        G9_inv = np.linalg.inv(G9_eff)
    except np.linalg.LinAlgError:
        return np.nan

    # Mode at rest in S: n_S = (0, 0, 0)
    n_full = np.concatenate([n_tilde[:6], [0, 0, 0]])
    E2_coupled = TWO_PI_HC**2 * n_full @ G9_inv @ n_full

    if E2_coupled <= 0:
        return np.nan

    return (E2_coupled - E2_bare) / E2_coupled


def main():
    print("=" * 70)
    print("R55 Track 3: ℵ-mediated Ma-S coupling")
    print("=" * 70)
    print()
    print(f"  α = {ALPHA:.6e},  √α = {SQRT_ALPHA:.6f}")
    print(f"  e = √(4πα) = {E_CHARGE:.6f}")
    print()

    # ── Section 1: Build the 10×10 metric ──────────────────
    print("─" * 70)
    print("Section 1: The 10×10 metric — three hypotheses for Ma-ℵ")
    print("─" * 70)
    print()

    # Circumferences: 6 Ma + ℵ (=1) + 3 S (=1 each)
    L_10 = np.concatenate([L_6, [1.0, 1.0, 1.0, 1.0]])
    L_9 = np.concatenate([L_6, [1.0, 1.0, 1.0]])

    hypotheses = {
        'A (all ±1)': np.array([-1, -1, +1, +1, +1, +1], dtype=float),
        'B (1/Lᵢ)': 1.0 / L_6,
        'C (tube-only)': np.array([-1, 0, 0, 0, +1, 0], dtype=float),
        'C+ (tube+ν)': np.array([-1, 0, +1, 0, +1, 0], dtype=float),
    }

    for hyp_name, sigma_ma_aleph in hypotheses.items():
        print(f"  Hypothesis {hyp_name}:")
        print(f"    Ma-ℵ = [{', '.join(f'{x:+.4g}' for x in sigma_ma_aleph)}]")
        print(f"    ℵ-S  = {SQRT_ALPHA:.6f} (= √α)")
        print()

        G10 = build_10x10(A_6x6, sigma_ma_aleph, SQRT_ALPHA)

        # Check positive-definiteness
        eigs = np.linalg.eigvalsh(G10)
        pd = np.all(eigs > 0)
        print(f"    Positive-definite: {pd}")
        if not pd:
            print(f"    Min eigenvalue: {min(eigs):.6e}")
            print(f"    → INVALID metric. Skipping.")
            print()
            continue

        # Integrate out ℵ
        G9_eff = integrate_out_aleph(G10)

        # Check the effective Ma-S block
        MaS_block = G9_eff[:6, 6:]
        print(f"    Effective Ma-S block (from integrating out ℵ):")
        for i in range(6):
            dim_name = ['e-tube', 'e-ring', 'ν-tube', 'ν-ring', 'p-tube', 'p-ring'][i]
            vals = MaS_block[i, :]
            if np.all(np.abs(vals) < 1e-15):
                print(f"      {dim_name:>8s} → S: [0, 0, 0]")
            else:
                ratio = vals[0] / SQRT_ALPHA if abs(SQRT_ALPHA) > 1e-30 else 0
                print(f"      {dim_name:>8s} → S: [{vals[0]:+.6f}, {vals[1]:+.6f}, {vals[2]:+.6f}]  "
                      f"(ratio to √α: {ratio:+.4f})")

        print()

        # ── Particle spectrum check ─────────────────────────
        print(f"    Particle spectrum (10D vs 6D):")
        print(f"      {'Mode':>12s}  {'E_6D (MeV)':>12s}  {'E_10D (MeV)':>12s}  {'Δ/E':>10s}")
        print(f"      {'─'*12}  {'─'*12}  {'─'*12}  {'─'*10}")

        for name, n6 in MODES.items():
            E_6d = m.mode_energy(n6)
            # For 10D: winding on ℵ = 0, winding on S = 0 (at rest)
            n10 = list(n6) + [0, 0, 0, 0]
            E_10d = mode_energy_10d(G10, L_10, n10)

            if E_6d > 0 and not np.isnan(E_10d):
                delta = abs(E_10d - E_6d) / E_6d
                marker = " ✓" if delta < 0.001 else f" ← {delta*100:.1f}% SHIFT"
            else:
                delta = np.nan
                marker = " ?"

            print(f"      {name:>12s}  {E_6d:12.4f}  {E_10d:12.4f}  {delta:10.2e}{marker}")

        print()

        # ── α universality check ────────────────────────────
        print(f"    α universality (effective 9×9 metric):")
        print(f"      {'Mode':>12s}  {'Q':>4s}  {'α_eff':>12s}  {'ratio/α':>10s}")
        print(f"      {'─'*12}  {'─'*4}  {'─'*12}  {'─'*10}")

        for name, n6 in MODES.items():
            Q = -n6[0] + n6[4]
            n9 = list(n6) + [0, 0, 0]
            a_eff = compute_alpha_eff(G9_eff, L_9, n9)

            if np.isnan(a_eff):
                print(f"      {name:>12s}  {Q:>+4d}  {'NaN':>12s}")
            else:
                ratio = a_eff / ALPHA if ALPHA > 0 else 0
                marker = " ✓" if abs(ratio - 1.0) < 0.05 else ""
                if Q == 0 and abs(a_eff) < 1e-10:
                    marker = " ✓ (neutral)"
                print(f"      {name:>12s}  {Q:>+4d}  {a_eff:12.6e}  {ratio:10.4f}{marker}")

        print()
        print()

    # ── Section 2: What does the effective Ma-S look like? ──
    print("─" * 70)
    print("Section 2: Detailed effective Ma-S for Hypothesis C (tube-only)")
    print("─" * 70)
    print()

    sigma_C = np.array([-1, 0, 0, 0, +1, 0], dtype=float)
    G10_C = build_10x10(A_6x6, sigma_C, SQRT_ALPHA)
    G9_C = integrate_out_aleph(G10_C)

    print("  Effective 9×9 metric (Ma-S block only):")
    print()
    MaS = G9_C[:6, 6:]
    dim_names = ['e-tube', 'e-ring', 'ν-tube', 'ν-ring', 'p-tube', 'p-ring']
    s_names = ['S_x', 'S_y', 'S_z']

    print(f"  {'':>10s}", end="")
    for sn in s_names:
        print(f"  {sn:>12s}", end="")
    print()
    for i in range(6):
        print(f"  {dim_names[i]:>10s}", end="")
        for j in range(3):
            v = MaS[i, j]
            if abs(v) < 1e-15:
                print(f"  {'0':>12s}", end="")
            else:
                print(f"  {v:>+12.6f}", end="")
        print()

    print()
    print(f"  √α = {SQRT_ALPHA:+.6f}")
    print(f"  The effective Ma-S entries should be ±√α for tube dims, 0 for ring dims.")
    print()

    # Check: is the effective Ma-S block exactly ±√α × (Ma-ℵ) × (ℵ-S)?
    expected = np.outer(sigma_C, [SQRT_ALPHA, SQRT_ALPHA, SQRT_ALPHA])
    diff = MaS - expected
    max_diff = np.max(np.abs(diff))
    print(f"  Max deviation from predicted (σ_Ma-ℵ × σ_ℵ-S): {max_diff:.2e}")
    if max_diff < 1e-10:
        print(f"  → EXACT match (to machine precision)")
    else:
        print(f"  → Deviation exists (Schur complement mixes with Ma block)")

    print()

    # ── Section 3: Sweep σℵS to check sensitivity ──────────
    print("─" * 70)
    print("Section 3: Sweep σℵS — does α_eff = σℵS² ?")
    print("─" * 70)
    print()

    sigma_C = np.array([-1, 0, 0, 0, +1, 0], dtype=float)

    print(f"  {'σℵS':>10s}  {'σℵS²':>12s}  {'α_eff(e)':>12s}  {'α_eff(p)':>12s}  "
          f"{'α_eff(ν₁)':>12s}  {'ratio_e':>10s}")
    print(f"  {'─'*10}  {'─'*12}  {'─'*12}  {'─'*12}  "
          f"{'─'*12}  {'─'*10}")

    for sigma_as in [0.01, 0.03, 0.05, SQRT_ALPHA, 0.1, 0.15, 0.2, 0.3]:
        G10_t = build_10x10(A_6x6, sigma_C, sigma_as)
        eigs = np.linalg.eigvalsh(G10_t)
        if not np.all(eigs > 0):
            print(f"  {sigma_as:10.6f}  {'invalid':>12s}")
            continue

        G9_t = integrate_out_aleph(G10_t)

        a_e = compute_alpha_eff(G9_t, L_9, list(MODES['electron']) + [0,0,0])
        a_p = compute_alpha_eff(G9_t, L_9, list(MODES['proton']) + [0,0,0])
        a_nu = compute_alpha_eff(G9_t, L_9, list(MODES['ν₁']) + [0,0,0])

        predicted = sigma_as**2
        ratio_e = a_e / predicted if predicted > 0 and not np.isnan(a_e) else np.nan

        print(f"  {sigma_as:10.6f}  {predicted:12.6e}  {a_e:12.6e}  {a_p:12.6e}  "
              f"{a_nu:12.6e}  {ratio_e:10.4f}")

    print()
    print(f"  If α_eff = σℵS², then setting σℵS = √α gives α_eff = α. ✓")
    print(f"  The ratio column should be ≈ 1.0 at all σℵS values.")

    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("  The 10×10 metric with ℵ mediating Ma-S coupling:")
    print()
    print("  1. Does the particle spectrum change?")
    print("  2. Is the effective Ma-S coupling = ±√α × (Ma-ℵ)?")
    print("  3. Is α universal across all charged modes?")
    print("  4. Does α_eff = σℵS² hold (so α is set by one number)?")
    print()
    print(f"  α = {ALPHA:.6e}")
    print(f"  √α = {SQRT_ALPHA:.6f}")
    print()
    print("Track 3 complete.")


if __name__ == '__main__':
    main()
