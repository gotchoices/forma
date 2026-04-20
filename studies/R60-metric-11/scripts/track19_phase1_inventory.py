"""
R60 Track 19 — Phase 1: Inventory re-sweep on (3, 6) baseline.

Run the full model-E / R60 inventory against the Track 15
Option A calibration (L_ring_p = 47.29 fm for (3, 6) proton),
keeping all other parameters from model-F's Track 12 baseline.

For each of the 18 inventory tuples, compute:
  - mass with the bare tuple
  - α_Coulomb with bare and composite rules
  - deviation from observed mass
  - compare to the original Track 10 / Track 12 reported values

For tuples where the bare p-sheet winding has gcd > 1, also
test the "tripled" reading: (n_et, n_er, n_νt, n_νr, 3·n_pt, 3·n_pr).

Sandboxed — no changes to prior scripts.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    build_metric_11, signature_ok, alpha_coulomb, mode_6_to_11,
    derive_L_ring, L_vector_from_params, mode_energy,
    ALPHA, M_P_MEV,
)
from track7b_resolve import build_aug_metric
from track10_hadron_inventory import MODEL_E_INVENTORY, mode_charge, mode_alpha_sum
from track15_phase1_mass import K_MODELF, modelF_baseline
from track15_phase2_alpha import alpha_sum_composite


def main():
    print("=" * 90)
    print("R60 Track 19 — Phase 1: inventory re-sweep on (3, 6) baseline")
    print("=" * 90)
    print()

    # ── Baseline: Track 12 parameters with L_ring_p = 47.29 fm (Track 15 Option A) ──
    L_ring_p_36 = derive_L_ring(M_P_MEV, 3, 6, 0.55, 0.162037, K_MODELF)
    p = modelF_baseline(L_ring_p=L_ring_p_36)
    G = build_aug_metric(p)
    L = L_vector_from_params(p)

    print(f"  Baseline: Track 12 + Track 15 Option A")
    print(f"    (ε_e, s_e, L_ring_e) = ({p.eps_e}, {p.s_e}, {p.L_ring_e:.4f} fm)")
    print(f"    (ε_p, s_p, L_ring_p) = ({p.eps_p}, {p.s_p}, {L_ring_p_36:.4f} fm)")
    print(f"    (ε_ν, s_ν, L_ring_ν) = ({p.eps_nu}, {p.s_nu}, {p.L_ring_nu:.4e} fm)")
    print(f"    k = {K_MODELF:.4e}")
    print(f"    signature ok: {signature_ok(G)}")
    print()

    # ── Verify anchors ──
    print("─" * 90)
    print("  Anchor check (e, p, ν₁):")
    print("─" * 90)
    anchors = [
        ("electron (1, 2)",       (1, 2, 0, 0, 0, 0),    0.511),
        ("proton (3, 6)",         (0, 0, 0, 0, 3, 6),    938.272),
        ("ν₁ R61 #1 (+1, +1)",    (0, 0, 1, 1, 0, 0),    5.0e-8),
    ]
    for label, n6, target in anchors:
        n11 = mode_6_to_11(n6)
        E = mode_energy(G, L, n11)
        a = alpha_coulomb(G, n11) / ALPHA
        rel = (E - target) / target
        print(f"    {label:<24s}  E = {E:>12.6e}  (target {target:>12.4e})  "
              f"Δ = {rel:>+.4%}  α/α = {a:.4f}")
    print()

    # ── Inventory re-sweep ──
    print("─" * 90)
    print("  Full inventory re-sweep (18 particles, bare model-E tuples):")
    print("─" * 90)
    print()
    print(f"  {'particle':<10s}  {'tuple':<28s}  {'Q':>3s}  "
          f"{'α_sum_bare':>11s}  {'α_sum_comp':>11s}  "
          f"{'E_pred (MeV)':>13s}  {'target':>11s}  {'Δ':>9s}  {'M-E Δ'}")
    print("  " + "-" * 110)

    summary = []
    for label, target, Q, tup, me_delta in MODEL_E_INVENTORY:
        n11 = mode_6_to_11(tup)
        E_pred = mode_energy(G, L, n11)
        rel = (E_pred - target) / target
        a_bare = mode_alpha_sum(tup)
        a_comp = alpha_sum_composite(tup)
        a_ratio = alpha_coulomb(G, n11) / ALPHA

        tuple_str = str(tup).replace(" ", "")
        Q_check = mode_charge(tup)
        print(f"  {label:<10s}  {tuple_str:<28s}  {Q_check:>+3d}  "
              f"{a_bare:>+11d}  {a_comp:>+11d}  "
              f"{E_pred:>13.4f}  {target:>11.4f}  {rel:>+9.4%}  {me_delta}")
        summary.append((label, target, tup, E_pred, rel, a_bare, a_comp, a_ratio))
    print()

    # ── Statistics ──
    print("─" * 90)
    print("  Accuracy summary:")
    print("─" * 90)
    print()
    ranges = [
        ("≤ 0.5%",  lambda r: abs(r) <= 0.005),
        ("≤ 1%",    lambda r: 0.005 < abs(r) <= 0.01),
        ("≤ 2%",    lambda r: 0.01 < abs(r) <= 0.02),
        ("≤ 5%",    lambda r: 0.02 < abs(r) <= 0.05),
        ("≤ 10%",   lambda r: 0.05 < abs(r) <= 0.10),
        ("> 10%",   lambda r: abs(r) > 0.10),
    ]
    for label, pred in ranges:
        matches = [s[0] for s in summary if pred(s[4])]
        print(f"    {label:<10s}  {len(matches):>3d}  {matches}")
    print()

    # ── Tuples that need composite reinterpretation ──
    print("─" * 90)
    print("  Composite-α reinterpretation check:")
    print("─" * 90)
    print()
    print("  For tuples where α_sum_bare² ≠ 1, check whether composite")
    print("  α_sum_comp gives α_sum² = 1 (α = α after reinterpretation).")
    print()

    needs_comp = [s for s in summary
                  if s[5] * s[5] != 1 and not (s[2][4] == 0 and s[2][5] == 0)]
    print(f"  {'particle':<10s}  {'tuple':<28s}  {'bare α':>10s}  "
          f"{'comp α':>10s}  {'comp gives α?':>15s}")
    for label, target, tup, E, rel, a_bare, a_comp, a_ratio in needs_comp:
        a_bare_sq = a_bare * a_bare
        a_comp_sq = a_comp * a_comp
        helps = "YES" if a_comp_sq == 1 else ("SAME" if a_comp_sq == a_bare_sq else "DIFF")
        print(f"  {label:<10s}  {str(tup).replace(' ', ''):<28s}  "
              f"{a_bare_sq:>10d}  {a_comp_sq:>10d}  {helps:>15s}")
    print()

    # ── Comparison to Track 12 baseline (L_ring_p = 20.55 fm, bare (1, 3) proton) ──
    print("─" * 90)
    print("  Comparison: (3, 6) baseline (this track) vs bare Track 12 baseline:")
    print("─" * 90)
    print()
    print("  The only difference between the two baselines is L_ring_p:")
    print(f"    (1, 3) interpretation: L_ring_p = 20.55 fm (proton at μ(1, 3) = 2.78)")
    print(f"    (3, 6) interpretation: L_ring_p = {L_ring_p_36:.2f} fm (proton at μ(3, 6) = 7.75)")
    print(f"    Ratio: {L_ring_p_36 / 20.55:.4f}")
    print()
    # Build Track 12 baseline for comparison
    p_13 = modelF_baseline(L_ring_p=20.551)
    G_13 = build_aug_metric(p_13)
    L_13 = L_vector_from_params(p_13)
    print(f"  {'particle':<10s}  {'tuple':<28s}  "
          f"{'E (1,3)-base':>13s}  {'E (3,6)-base':>13s}  {'Δ ratio':>10s}")
    print("  " + "-" * 90)
    for label, target, tup, E, rel, a_bare, a_comp, a_ratio in summary:
        n11 = mode_6_to_11(tup)
        E_13 = mode_energy(G_13, L_13, n11)
        E_36 = E
        ratio = E_36 / E_13 if E_13 > 0 else float("inf")
        print(f"  {label:<10s}  {str(tup).replace(' ', ''):<28s}  "
              f"{E_13:>13.4f}  {E_36:>13.4f}  {ratio:>10.4f}")
    print()
    print("  Observation: masses on (3, 6) baseline differ from (1, 3)")
    print("  baseline for any tuple with nonzero p-sheet content.  This is")
    print("  because L_ring_p changed by 2.3×.  The question is whether the")
    print("  composite reading (tripling the p-sheet winding) recovers the")
    print("  original masses.")
    print()

    # ── Test: tripled p-sheet reading ──
    print("─" * 90)
    print("  Tripled p-sheet test: replace (n_pt, n_pr) with (3·n_pt, 3·n_pr):")
    print("─" * 90)
    print()
    print(f"  {'particle':<10s}  {'bare tuple':<24s}  {'tripled tuple':<24s}  "
          f"{'bare E':>12s}  {'tripled E':>12s}  {'E_13 (ref)':>12s}")
    print("  " + "-" * 102)
    for label, target, tup, E, rel, a_bare, a_comp, a_ratio in summary:
        if tup[4] == 0 and tup[5] == 0:
            continue  # no p-sheet content
        tripled = (tup[0], tup[1], tup[2], tup[3], 3 * tup[4], 3 * tup[5])
        n11_tripled = mode_6_to_11(tripled)
        E_tripled = mode_energy(G, L, n11_tripled)
        # Also compute on (1, 3) baseline for reference
        n11_bare = mode_6_to_11(tup)
        E_13 = mode_energy(G_13, L_13, n11_bare)
        print(f"  {label:<10s}  {str(tup).replace(' ', ''):<24s}  "
              f"{str(tripled).replace(' ', ''):<24s}  "
              f"{E:>12.4f}  {E_tripled:>12.4f}  {E_13:>12.4f}")
    print()
    print("  Observations:")
    print("    If the (3, 6) baseline with TRIPLED p-sheet windings gives")
    print("    similar masses to the (1, 3) baseline with BARE windings, the")
    print("    two readings are equivalent.  Check whether tripled E matches")
    print("    E_13 (the original model-F prediction).")
    print()

    print("Phase 1 complete.")


if __name__ == "__main__":
    main()
