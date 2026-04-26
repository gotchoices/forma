"""
R64 Track 11 Phase 11d — closed-form derivation of the H2 coefficient.

Phase 9b found empirically that σ_aS = b · σ_pS_tube with b ≈ −1.819
preserves α universality.  Phase 11c showed this prescription, when
activated at the signature edge with A1 attribution, delivers the
strong force at full magnitude.

Phase 11d derives b in closed form.

Setup.  Adding σ_pS_tube to (P_TUBE, S_i) and σ_aS = b·σ_pS_tube to
(ALEPH, S_i) for i ∈ {x, y, z} perturbs G.  At first order:

    ΔG⁻¹[Ma_α, t] = −Σ_{i,j} G⁻¹[Ma_α, i] · ΔG[i, j] · G⁻¹[j, t]

ΔG is non-zero only at the (P_TUBE, S_i), (S_i, P_TUBE), (ALEPH, S_i),
(S_i, ALEPH) pairs.  At baseline G⁻¹[S_i, t] = 0 (S is diagonal-
Euclidean and doesn't couple to t).  So:

    ΔG⁻¹[Ma_α, t] = −σ_pS_tube · S_sum_α · (G⁻¹[P_TUBE, t]
                                            + b · G⁻¹[ALEPH, t])

where S_sum_α = Σ_i G⁻¹[Ma_α, S_i].  For universality (ΔG⁻¹ = 0 for
all α), the bracket must vanish:

    b = − G⁻¹[P_TUBE, t] / G⁻¹[ALEPH, t]

Phase 11d verifies this analytical formula matches the empirical
−1.819 from Phase 9b, and explores whether the ratio simplifies in
closed form in terms of (ε_p, s_p, σ_ta, σ_at, σ_ra).
"""

import sys
import math
from pathlib import Path

import numpy as np

R60_SCRIPTS = Path(__file__).resolve().parent.parent.parent / "R60-metric-11" / "scripts"
sys.path.insert(0, str(R60_SCRIPTS))

from track1_solver import (    # noqa: E402
    ALPHA, SQRT_ALPHA, FOUR_PI,
    I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING, I_NU_TUBE, I_NU_RING,
    I_ALEPH, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import track9_params    # noqa: E402


def main():
    print("=" * 90)
    print("R64 Track 11 Phase 11d — closed-form H2 coefficient")
    print("=" * 90)
    print()

    # ── Step 1: numerical verification at R64 Point B ───────────────
    p = track9_params().copy_with(eps_p=0.2052, s_p=0.0250)
    G = build_aug_metric(p)
    G_inv = np.linalg.inv(G)

    G_pt_t = G_inv[I_P_TUBE, I_T]
    G_a_t = G_inv[I_ALEPH, I_T]
    b_predicted = -G_pt_t / G_a_t

    print(f"  At R64 Point B (ε_p = {p.eps_p}, s_p = {p.s_p}):")
    print(f"    G⁻¹[P_TUBE, t]  = {G_pt_t:+.10f}")
    print(f"    G⁻¹[ALEPH, t]   = {G_a_t:+.10f}")
    print(f"    b = −G⁻¹[P_TUBE, t] / G⁻¹[ALEPH, t] = {b_predicted:+.10f}")
    print(f"    Phase 9b empirical:                    −1.818920 (≈)")
    print()
    print(f"    Match: {abs(b_predicted - (-1.818920)) < 1e-3}")
    print()

    # ── Step 2: derivation form check ───────────────────────────────
    # Try to express the ratio in terms of metric parameters.
    # In R60 model-F:
    #   σ_at = 4πα,  σ_ta = √α,  σ_ra = (s·ε)·σ_ta
    #   sign_p = −1 for the p-sheet
    #
    # Let's look at the columns G⁻¹[*, t] explicitly to find the
    # algebraic structure.
    print("  Inspect inverse metric column G⁻¹[*, t]:")
    labels = ["ALEPH", "P_TUBE", "P_RING", "E_TUBE", "E_RING",
              "NU_TUBE", "NU_RING", "SX", "SY", "SZ", "T"]
    for i, lbl in enumerate(labels):
        print(f"    G⁻¹[{lbl:<7s}, t] = {G_inv[i, I_T]:+.10f}")
    print()

    # ── Step 3: parameter sweep to confirm formula ──────────────────
    print("  Verify b formula across multiple (ε_p, s_p) points:")
    print(f"    {'ε_p':>8s}  {'s_p':>8s}  "
          f"{'G⁻¹[pt,t]':>14s}  {'G⁻¹[a,t]':>14s}  "
          f"{'b_predicted':>14s}")
    for eps_p, s_p in [(0.2052, 0.025), (0.4, 3.0), (0.55, 0.16),
                       (0.073, 0.194), (0.20, 0.10), (0.30, 0.05)]:
        p_test = track9_params().copy_with(eps_p=eps_p, s_p=s_p)
        G_test = build_aug_metric(p_test)
        try:
            G_inv_test = np.linalg.inv(G_test)
            G_pt = G_inv_test[I_P_TUBE, I_T]
            G_a = G_inv_test[I_ALEPH, I_T]
            b_pred = -G_pt / G_a
        except np.linalg.LinAlgError:
            G_pt = G_a = b_pred = float('nan')
        print(f"    {eps_p:>8.4f}  {s_p:>8.4f}  "
              f"{G_pt:>+14.6e}  {G_a:>+14.6e}  {b_pred:>+14.6f}")
    print()

    # ── Step 4: simplified formula attempt ──────────────────────────
    # G⁻¹[ALEPH, t] in R60 is dominated by the σ_at entry on the
    # aleph row.  In a simplified 2-block model (ALEPH ↔ T only,
    # ignoring sheets):
    #   G⁻¹[ALEPH, T] ≈ σ_at / det
    # with appropriate sign convention.  In the full metric, sheet
    # mixing modifies this.
    #
    # Rather than struggle with full Schur algebra, let's test
    # whether b is approximately a simple ratio of metric entries.
    print("  Heuristic ratios:")
    print(f"    G[T, ALEPH]                      = {G[I_T, I_ALEPH]:+.6f}")
    print(f"    G[ALEPH, T]                      = {G[I_ALEPH, I_T]:+.6f}")
    print(f"    G[T, P_TUBE]                     = {G[I_T, I_P_TUBE]:+.6f}")
    print(f"    G[P_TUBE, T]                     = {G[I_P_TUBE, I_T]:+.6f}")
    print(f"    σ_at = 4πα                       = {FOUR_PI * ALPHA:+.6f}")
    print(f"    σ_ta = √α                        = {SQRT_ALPHA:+.6f}")
    print(f"    σ_ra_p = (s_p·ε_p)·σ_ta          = "
          f"{p.s_p * p.eps_p * SQRT_ALPHA:+.6f}")
    print()

    # ── Step 5: b as function of (ε_p, s_p) — try clean form ──────
    print("  Try clean closed forms:")
    sa = SQRT_ALPHA
    fa = FOUR_PI * ALPHA
    eps_p, s_p = p.eps_p, p.s_p

    # Hypothesis: b = -1/(s_p · ε_p · σ_ta · scale)
    candidates = [
        ("1/(s·ε)", 1.0 / (s_p * eps_p)),
        ("1/(s·ε·√α)", 1.0 / (s_p * eps_p * sa)),
        ("σ_ta/(σ_at)", sa / fa),
        ("1/(4π·α·s·ε)", 1.0 / (fa * s_p * eps_p)),
        ("ε_p/(s_p)", eps_p / s_p),
        ("(s·ε + 1)", s_p * eps_p + 1),
        ("−1/(σ_ra/σ_ta)", -1.0 / (s_p * eps_p)),
        ("−ε_p/(α·s_p)", -eps_p / (ALPHA * s_p)),
    ]
    print(f"    {'expression':<25s}  {'value':>14s}  "
          f"{'matches b?':>10s}")
    for label, value in candidates:
        match = abs(value - b_predicted) < 0.05
        print(f"    {label:<25s}  {value:>+14.6f}  "
              f"{'YES' if match else 'no':>10s}")
    print()

    # Inverse-metric look at the dominant Schur path (ALEPH-T):
    # G⁻¹[ALEPH, T] = (cofactor) / det
    #
    # For the relationship b = -G⁻¹[P_TUBE, T] / G⁻¹[ALEPH, T], let
    # me try expanding via the adjugate.  The dominant contribution
    # to G⁻¹[P_TUBE, T] comes from sheet mixing through ALEPH:
    #   G⁻¹[P_TUBE, T] ≈ σ_ta_p · G⁻¹[ALEPH, T] + ...
    # which would give b = -σ_ta_p / 1.  But σ_ta_p = sign_p·√α
    # = -√α ≈ -0.0854; b would be ≈ +0.0854, not −1.819.  So
    # higher-order Schur effects dominate.
    #
    # Try: ratio of Cramer's-rule numerators.  Both numerators are
    # (n−1)×(n−1) cofactors.  Their ratio cancels the determinant.
    print("  Cramer/cofactor ratio check:")
    n = G.shape[0]
    minor_pt = np.delete(np.delete(G, I_P_TUBE, axis=0), I_T, axis=1)
    minor_a = np.delete(np.delete(G, I_ALEPH, axis=0), I_T, axis=1)
    sign_pt = (-1) ** (I_P_TUBE + I_T)
    sign_a = (-1) ** (I_ALEPH + I_T)
    cof_pt = sign_pt * np.linalg.det(minor_pt)
    cof_a = sign_a * np.linalg.det(minor_a)
    # G⁻¹[i, j] = cofactor(j, i) / det(G);
    # G⁻¹[P_TUBE, T] uses cofactor(T, P_TUBE).
    minor_T_pt = np.delete(np.delete(G, I_T, axis=0), I_P_TUBE, axis=1)
    minor_T_a = np.delete(np.delete(G, I_T, axis=0), I_ALEPH, axis=1)
    cof_T_pt = ((-1) ** (I_T + I_P_TUBE)) * np.linalg.det(minor_T_pt)
    cof_T_a = ((-1) ** (I_T + I_ALEPH)) * np.linalg.det(minor_T_a)
    detG = np.linalg.det(G)
    print(f"    cofactor(T, P_TUBE)             = {cof_T_pt:+.6e}")
    print(f"    cofactor(T, ALEPH)              = {cof_T_a:+.6e}")
    print(f"    det(G)                          = {detG:+.6e}")
    print(f"    G⁻¹[P_TUBE, T] (via cofactor)   = {cof_T_pt / detG:+.6e}")
    print(f"    G⁻¹[ALEPH, T] (via cofactor)    = {cof_T_a / detG:+.6e}")
    print(f"    b (cofactor ratio)              = {-cof_T_pt / cof_T_a:+.6f}")
    print()

    # ── Step 6: empirical b vs ε_p curve to find structural form ───
    print("  b(ε_p) curve at fixed s_p = 0.025:")
    print(f"    {'ε_p':>8s}  {'b_predicted':>14s}  "
          f"{'1/ε_p':>10s}  {'b·ε_p':>10s}")
    for eps_p in [0.05, 0.1, 0.15, 0.2052, 0.3, 0.5, 1.0, 2.0]:
        p_test = track9_params().copy_with(eps_p=eps_p, s_p=0.025)
        G_test = build_aug_metric(p_test)
        try:
            G_inv_test = np.linalg.inv(G_test)
            b_pred = -G_inv_test[I_P_TUBE, I_T] / G_inv_test[I_ALEPH, I_T]
        except np.linalg.LinAlgError:
            b_pred = float('nan')
        b_eps = b_pred * eps_p if not math.isnan(b_pred) else float('nan')
        print(f"    {eps_p:>8.4f}  {b_pred:>+14.6f}  "
              f"{1/eps_p:>10.4f}  {b_eps:>+10.4f}")
    print()

    print("  b(s_p) curve at fixed ε_p = 0.2052:")
    print(f"    {'s_p':>8s}  {'b_predicted':>14s}  "
          f"{'b·s_p':>12s}  {'b/s_p':>12s}")
    for s_p in [0.01, 0.025, 0.05, 0.10, 0.20, 0.50, 1.0]:
        p_test = track9_params().copy_with(eps_p=0.2052, s_p=s_p)
        G_test = build_aug_metric(p_test)
        try:
            G_inv_test = np.linalg.inv(G_test)
            b_pred = -G_inv_test[I_P_TUBE, I_T] / G_inv_test[I_ALEPH, I_T]
        except np.linalg.LinAlgError:
            b_pred = float('nan')
        b_s = b_pred * s_p if not math.isnan(b_pred) else float('nan')
        b_div_s = b_pred / s_p if not math.isnan(b_pred) else float('nan')
        print(f"    {s_p:>8.4f}  {b_pred:>+14.6f}  "
              f"{b_s:>+12.6f}  {b_div_s:>+12.6f}")
    print()

    # ── Verdict ─────────────────────────────────────────────────────
    print("=" * 90)
    print("VERDICT — Phase 11d")
    print("=" * 90)
    print()
    print("  Closed-form prescription:")
    print()
    print("      b = − G⁻¹[P_TUBE, t] / G⁻¹[ALEPH, t]")
    print()
    print(f"  At R64 Point B: b = {b_predicted:+.6f}  (Phase 9b: −1.819)")
    print()
    print("  Derivation: from first-order perturbation theory on G⁻¹.")
    print("  Adding σ_pS_tube at (P_TUBE, S_i) and σ_aS at (ALEPH, S_i)")
    print("  shifts G⁻¹[Ma_α, t] proportional to (G⁻¹[P_TUBE, t] +")
    print("  b·G⁻¹[ALEPH, t]).  Universality requires this bracket = 0.")
    print()


if __name__ == "__main__":
    main()
