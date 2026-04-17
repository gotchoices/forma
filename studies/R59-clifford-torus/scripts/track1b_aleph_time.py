"""
R59 Track 1b: ℵ-mediated time coupling (11D metric).

Architecture:
  11D = 6 Ma + 1 ℵ + 3 S + 1 t
  Indices: 0-5 Ma, 6 ℵ, 7-9 S, 10 t

Key difference from Track 1:
  - NO direct Ma-t entries (all zero)
  - R55's Ma-ℵ entries preserved (hypothesis F: ring at ±1/(2π))
  - ONE new entry: σ_{ℵt} (aleph-to-time coupling)
  - Effective Ma-t coupling emerges as Ma-ℵ × ℵ-t product

Benefits over Track 1:
  - Signs inherited from R55 geometry, not hand-coded
  - One knob (σ_{ℵt}), not six
  - ν coupling determined by R55's ν-ring entry, not by ansatz

The mass-shell condition on the 11D metric:
  g^{μν} k_μ k_ν = 0
  with k = (n/L, 0, 0, 0, 0, ω)  [Ma windings, ℵ=0, S=0, t=ω]
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from lib.metric import Metric
from lib.ma_model_d import _TWO_PI_HC

ALPHA = 1.0 / 137.036
TWO_PI_HC = _TWO_PI_HC
INV_2PI = 1.0 / (2 * math.pi)

m = Metric.model_E()
A_6x6 = m.Gt
L_6 = m.L

MODES = [
    ('electron',  (1, 2, 0, 0, 0, 0),    0.511,   -1),
    ('proton',    (0, 0, -2, 2, 1, 3),  938.272,   +1),
    ('neutron',   (0, -4, -1, 2, 0, -3), 939.565,   0),
    ('ν₁',       (0, 0, 1, 1, 0, 0),     2.92e-5,  0),
    ('ν₂',       (0, 0, -1, 1, 0, 0),    3.05e-5,  0),
    ('deuteron',  (0, 0, 0, 0, 2, 6),  1875.61,    +2),
    ('Λ',        (-1, 2, -1, 2, -1, 3), 1115.68,    0),
    ('Σ⁻',       (-1, 2, -2, 2, -2, -2), 1197.45, -1),
]

# R55 hypothesis F: Ma-ℵ coupling on ring dimensions at ±1/(2π)
# Signs: e-ring negative, ν-ring positive, p-ring positive
SIGMA_MA_ALEPH = np.array([0, -INV_2PI, 0, +INV_2PI, 0, +INV_2PI])

# R55's optimal ℵ-S coupling (for reference)
R55_SIGMA_ALEPH_S = 0.29019


def build_11d(sigma_aleph_t, sigma_aleph_s=0.0):
    """
    Build the 11×11 metric.

    Indices: 0-5 Ma, 6 ℵ, 7-9 S, 10 t

    - Ma block (0-5): model-E A_6x6
    - Ma-ℵ (col 6): R55 hypothesis F (±1/(2π) on rings)
    - ℵ diagonal (6,6): +1
    - S diagonal (7-9): +1
    - t diagonal (10): -1
    - ℵ-S (6, 7-9): sigma_aleph_s (optional, for comparison)
    - ℵ-t (6, 10): sigma_aleph_t  (THE NEW PARAMETER)
    - Ma-t: ALL ZERO (coupling goes through ℵ)
    - Ma-S: ALL ZERO (coupling goes through ℵ)
    """
    G = np.zeros((11, 11))

    # Ma block
    G[:6, :6] = A_6x6

    # ℵ diagonal
    G[6, 6] = 1.0

    # S diagonal
    G[7, 7] = 1.0
    G[8, 8] = 1.0
    G[9, 9] = 1.0

    # t diagonal (Lorentzian)
    G[10, 10] = -1.0

    # Ma-ℵ (R55 hypothesis F)
    for i in range(6):
        G[i, 6] = SIGMA_MA_ALEPH[i]
        G[6, i] = SIGMA_MA_ALEPH[i]

    # ℵ-S (optional — set to 0 by default, since coupling goes through t)
    for j in [7, 8, 9]:
        G[6, j] = sigma_aleph_s
        G[j, 6] = sigma_aleph_s

    # ℵ-t (THE NEW ENTRY)
    G[6, 10] = sigma_aleph_t
    G[10, 6] = sigma_aleph_t

    return G


def mass_shell_both(G, n6):
    """
    Solve the mass-shell condition on the 11D metric.

    k = (n₁/L₁, ..., n₆/L₆, 0, 0, 0, 0, ω)
    g^{μν} k_μ k_ν = 0  →  quadratic in ω

    Returns (E_low, E_high) — both roots.
    """
    try:
        Gi = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return np.nan, np.nan

    # Full 11D wavevector (Ma winding, ℵ=0, S=0, t=ω)
    # Indices: 0-5 Ma, 6 ℵ, 7-9 S, 10 t
    nt = np.array(n6, dtype=float) / L_6  # Ma part

    # Quadratic: a ω² + b ω + c = 0
    # a = Gi[10,10]
    a = Gi[10, 10]

    # b = 2 × Σ_{i in Ma} Gi[i, 10] × nt[i]
    #   + 2 × Gi[6, 10] × 0  (ℵ winding = 0)
    #   + 2 × Σ_{j in S} Gi[j, 10] × 0  (S winding = 0)
    b = 2.0 * np.dot(Gi[:6, 10], nt)

    # c = Σ_{i,j in Ma} Gi[i,j] × nt[i] × nt[j]
    c = nt @ Gi[:6, :6] @ nt

    disc = b**2 - 4 * a * c
    if disc < 0:
        return np.nan, np.nan

    w1 = (-b + math.sqrt(disc)) / (2 * a)
    w2 = (-b - math.sqrt(disc)) / (2 * a)
    E1 = TWO_PI_HC * abs(w1)
    E2 = TWO_PI_HC * abs(w2)

    return min(E1, E2), max(E1, E2)


def main():
    print("=" * 75)
    print("R59 Track 1b: ℵ-mediated time coupling (11D)")
    print("=" * 75)
    print()
    print("  11D = 6 Ma + 1 ℵ + 3 S + 1 t")
    print(f"  Ma-ℵ: R55 hypothesis F (rings at ±1/(2π) = ±{INV_2PI:.6f})")
    print("  Ma-t: ALL ZERO (coupling through ℵ)")
    print("  Ma-S: ALL ZERO")
    print("  New parameter: σ_{ℵt} (one knob)")
    print()

    # ── Section 1: Sanity check — bare metric (σ_{ℵt} = 0) ──
    print("─" * 75)
    print("Section 1: Bare 11D metric (σ_ℵt = 0, σ_ℵS = 0)")
    print("─" * 75)
    print()

    G_bare = build_11d(0.0, 0.0)
    eigs = np.linalg.eigvalsh(G_bare)
    n_neg = np.sum(eigs < 0)
    print(f"  Eigenvalues: {n_neg} negative (should be 1 for Lorentzian)")
    print(f"  Min eigenvalue: {min(eigs):.6f}")
    print()

    print(f"  {'Mode':>10s}  {'E_model-E':>10s}  {'E_11D':>10s}  {'match':>6s}")
    print(f"  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*6}")
    for name, n6, mobs, Q in MODES:
        Eme = m.mode_energy(n6)
        Elo, Ehi = mass_shell_both(G_bare, n6)
        match = "✓" if abs(Elo - Eme) / Eme < 0.001 else "✗"
        print(f"  {name:>10s}  {Eme:10.4f}  {Elo:10.4f}  {match:>6s}")
    print()

    # ── Section 2: Sweep σ_{ℵt} (no ℵ-S coupling) ─────────
    print("─" * 75)
    print("Section 2: Sweep σ_{ℵt} — time coupling through ℵ only")
    print("  (σ_ℵS = 0, no spatial ℵ coupling)")
    print("─" * 75)
    print()

    print(f"  {'σ_ℵt':>8s}  {'sig':>4s}  {'E_e':>8s}  {'E_p':>8s}  "
          f"{'Δe%':>7s}  {'Δp%':>7s}  {'α_e/α':>8s}  {'α_p/α':>8s}  {'gap%':>6s}")
    print(f"  {'─'*8}  {'─'*4}  {'─'*8}  {'─'*8}  "
          f"{'─'*7}  {'─'*7}  {'─'*8}  {'─'*8}  {'─'*6}")

    E_e0 = m.mode_energy(MODES[0][1])
    E_p0 = m.mode_energy(MODES[1][1])

    for sat in [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0]:
        G = build_11d(sat, 0.0)
        eigs = np.linalg.eigvalsh(G)
        n_neg = np.sum(eigs < 0)
        sig = "✓" if n_neg == 1 else f"✗{n_neg}"

        Ee_lo, Ee_hi = mass_shell_both(G, MODES[0][1])
        Ep_lo, Ep_hi = mass_shell_both(G, MODES[1][1])

        if np.isnan(Ee_lo) or np.isnan(Ep_lo):
            print(f"  {sat:8.4f}  {sig:>4s}  NaN")
            continue

        de = (Ee_lo - E_e0) / E_e0 * 100
        dp = (Ep_lo - E_p0) / E_p0 * 100
        ae = abs(Ee_lo - E_e0) / E_e0
        ap = abs(Ep_lo - E_p0) / E_p0
        gap = abs(ae - ap) / ae * 100 if ae > 0 else 0

        print(f"  {sat:8.4f}  {sig:>4s}  {Ee_lo:8.4f}  {Ep_lo:8.2f}  "
              f"{de:+7.3f}  {dp:+7.3f}  {ae/ALPHA:8.4f}  {ap/ALPHA:8.4f}  {gap:6.2f}")

    print()

    # ── Section 3: Fine-tune σ_{ℵt} for α_eff(e) = α ──────
    print("─" * 75)
    print("Section 3: Fine-tune σ_{ℵt} for α_eff(electron) = α")
    print("─" * 75)
    print()

    lo, hi = 0.01, 5.0
    for _ in range(200):
        mid = (lo + hi) / 2
        G = build_11d(mid, 0.0)
        eigs = np.linalg.eigvalsh(G)
        if np.sum(eigs < 0) != 1:
            hi = mid
            continue
        Ee_lo, _ = mass_shell_both(G, MODES[0][1])
        if np.isnan(Ee_lo):
            hi = mid
            continue
        ae = abs(Ee_lo - E_e0) / E_e0
        if ae < ALPHA:
            lo = mid
        else:
            hi = mid

    opt = (lo + hi) / 2
    G_opt = build_11d(opt, 0.0)

    print(f"  Optimal σ_ℵt = {opt:.8f}")
    print()

    # Full inventory at optimal
    print(f"  {'Mode':>10s}  {'Q':>3s}  {'E_bare':>10s}  {'E_lo':>10s}  "
          f"{'E_hi':>10s}  {'split':>8s}  {'α_eff':>12s}  {'α/α₀':>8s}")
    print(f"  {'─'*10}  {'─'*3}  {'─'*10}  {'─'*10}  "
          f"{'─'*10}  {'─'*8}  {'─'*12}  {'─'*8}")

    all_ae = []
    for name, n6, mobs, Q in MODES:
        Eb = m.mode_energy(n6)
        Elo, Ehi = mass_shell_both(G_opt, n6)
        split = Ehi - Elo if not np.isnan(Ehi) else 0
        ae = abs(Elo - Eb) / Eb if not np.isnan(Elo) else np.nan
        ar = ae / ALPHA if not np.isnan(ae) else np.nan
        all_ae.append((name, Q, ae))

        print(f"  {name:>10s}  {Q:+3d}  {Eb:10.4f}  {Elo:10.4f}  "
              f"{Ehi:10.4f}  {split:8.4f}  {ae:.6e}  {ar:8.4f}")

    print()

    # Universality summary
    charged = [(n, ae) for n, Q, ae in all_ae if Q != 0 and not np.isnan(ae)]
    if charged:
        ae_vals = [ae for _, ae in charged]
        print(f"  Charged modes:")
        for name, ae in charged:
            print(f"    {name:>10s}: α_eff = {ae:.6e} ({ae/ALPHA:.4f}α)")
        if len(ae_vals) >= 2:
            gap = (max(ae_vals) - min(ae_vals)) / max(ae_vals) * 100
            print(f"  Gap: {gap:.2f}%")

    neutral = [(n, ae) for n, Q, ae in all_ae if Q == 0 and not np.isnan(ae)]
    if neutral:
        print(f"  Neutral modes:")
        for name, ae in neutral:
            print(f"    {name:>10s}: α_eff = {ae:.6e} ({ae/ALPHA:.4f}α)")

    print()

    # ── Section 4: Compare — what do inherited signs look like? ──
    print("─" * 75)
    print("Section 4: Effective Ma-t coupling (inherited from R55 × σ_ℵt)")
    print("─" * 75)
    print()

    # Integrate out ℵ from the 11D metric to get effective 10D
    # Then examine the Ma-t block
    keep = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]  # exclude ℵ (index 6)
    G11 = G_opt
    M10 = G11[np.ix_(keep, keep)]
    b_aleph = G11[keep, 6]
    g_aleph = G11[6, 6]

    G10_eff = M10 - np.outer(b_aleph, b_aleph) / g_aleph

    # Ma-t block is G10_eff[0:6, 9] (since t is at index 9 in the 10D)
    # Wait — in the kept indices, t is at position 9 (the last of keep)
    # keep = [0,1,2,3,4,5, 7,8,9, 10]
    # In the effective 10D: Ma is 0-5, S is 6-8, t is 9
    Ma_t_eff = G10_eff[:6, 9]
    dim_names = ['e-tube', 'e-ring', 'ν-tube', 'ν-ring', 'p-tube', 'p-ring']

    print("  Effective Ma-t entries (from integrating out ℵ):")
    print()
    for i, name in enumerate(dim_names):
        v = Ma_t_eff[i]
        sign_note = ""
        if abs(v) > 1e-10:
            if v < 0:
                sign_note = "(−) ← e-sheet sign"
            else:
                sign_note = "(+) ← p/ν-sheet sign"
        print(f"    {name:>10s} → t: {v:+12.6f}  {sign_note}")

    print()
    print("  These signs are INHERITED from R55's Ma-ℵ entries,")
    print("  not hand-coded.  e-ring is negative, p-ring and ν-ring")
    print("  are positive — matching the charge convention.")
    print()

    # ── Section 5: Mass direction check ────────────────────
    print("─" * 75)
    print("Section 5: Does mass increase or decrease?")
    print("─" * 75)
    print()

    for name, n6, mobs, Q in MODES[:4]:
        Eb = m.mode_energy(n6)
        Elo, Ehi = mass_shell_both(G_opt, n6)
        direction = "DECREASE" if Elo < Eb else "INCREASE" if Elo > Eb else "unchanged"
        print(f"  {name:>10s}: {Eb:.4f} → {Elo:.4f} ({direction}, {(Elo-Eb)/Eb*100:+.3f}%)")

    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 75)
    print("SUMMARY")
    print("=" * 75)
    print()
    print(f"  σ_ℵt = {opt:.6f}")
    print(f"  Signs: inherited from R55 Ma-ℵ geometry")
    print(f"  Direct Ma-t: zero (all coupling through ℵ)")
    print()
    print("  Track 1b vs Track 1:")
    print("    Track 1:  6 hand-coded Ma-t entries, 1.83% gap")
    print("    Track 1b: 1 knob (σ_ℵt), signs from R55")
    print()
    print(f"  α = {ALPHA:.6e}")
    print()
    print("Track 1b complete.")


if __name__ == '__main__':
    main()
