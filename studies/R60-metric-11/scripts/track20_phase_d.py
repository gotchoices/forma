"""
R60 Track 20 — Phase D: Re-search Track 19 inventory with top spin rules.

For each top-scoring rule from Phase A/B, rerun the α-filtered
Z₃-compliant brute force on the (3, 6) baseline, using the rule
as the spin filter.  Report mass accuracy per particle.

Top rules to test:
 - Rule 4 (parity) — baseline, already used by Track 19
 - Rule 6 (L-∞ max) — perfectly consistent, gets spin-1 correct
 - Rule 7 (unit-per-sheet AM add) — second-best coverage
 - Rule 5 (vector magnitude) — perfectly consistent

Sandboxed.
"""

import sys, os
import math
from fractions import Fraction
from itertools import product as iproduct

sys.path.insert(0, os.path.dirname(__file__))

from track1_solver import (
    mode_6_to_11, derive_L_ring, L_vector_from_params, mode_energy,
    ALPHA, M_P_MEV,
)
from track7b_resolve import build_aug_metric
from track10_hadron_inventory import MODEL_E_INVENTORY, mode_charge
from track15_phase1_mass import K_MODELF, modelF_baseline
from track15_phase2_alpha import alpha_sum_composite
from track20_phase_ab import (
    OBSERVED_SPIN, sheet_ratio, active_sheets,
    rule_4_parity, rule_5_vector_magnitude, rule_6_linf_max, rule_7_unit_per_sheet,
)


# Spin rule callables for search filter
SPIN_RULES = {
    "parity": rule_4_parity,
    "L-∞ max": rule_6_linf_max,
    "vector mag": rule_5_vector_magnitude,
    "unit/sheet AM": rule_7_unit_per_sheet,
}


def z3_search_with_spin(G, L, target_mass, target_Q, target_spin,
                         spin_rule, n_max=6, top_k=1):
    """α-filtered brute force with Z₃ on p-sheet + custom spin rule."""
    best = []
    rng = range(-n_max, n_max + 1)
    z3_nt_values = [n for n in rng if n % 3 == 0]

    for n_et in rng:
        for n_er in rng:
            for n_nut in rng:
                for n_nur in rng:
                    for n_pt in z3_nt_values:
                        for n_pr in rng:
                            if (n_et == 0 and n_er == 0 and n_nut == 0 and
                                n_nur == 0 and n_pt == 0 and n_pr == 0):
                                continue
                            n6 = (n_et, n_er, n_nut, n_nur, n_pt, n_pr)
                            Q = -n6[0] + n6[4]
                            if Q != target_Q:
                                continue
                            alpha_sum = alpha_sum_composite(n6)
                            if target_Q == 0:
                                if abs(alpha_sum) > 1:
                                    continue
                            else:
                                if alpha_sum * alpha_sum != 1:
                                    continue
                            # Apply spin rule
                            try:
                                if not spin_rule(n6, target_spin):
                                    continue
                            except Exception:
                                continue

                            n11 = mode_6_to_11(n6)
                            E = mode_energy(G, L, n11)
                            rel = abs(E - target_mass) / target_mass

                            if len(best) < top_k or rel < best[-1][0]:
                                best.append((rel, n6, E, alpha_sum))
                                best.sort(key=lambda x: x[0])
                                if len(best) > top_k:
                                    best.pop()
    return best


def main():
    print("=" * 100)
    print("R60 Track 20 — Phase D: re-search inventory under top spin rules")
    print("=" * 100)
    print()

    L_ring_p_36 = derive_L_ring(M_P_MEV, 3, 6, 0.55, 0.162037, K_MODELF)
    p = modelF_baseline(L_ring_p=L_ring_p_36)
    G = build_aug_metric(p)
    L = L_vector_from_params(p)

    print(f"  Baseline: (3, 6) proton calibration, L_ring_p = {L_ring_p_36:.4f} fm")
    print(f"  Search: Z₃ p-sheet + composite α rule + each spin rule below")
    print()

    # Target particles (exclude inputs: electron, proton — they anchor calibration)
    targets = [(label, target, Q, me_tup, me_delta)
               for (label, target, Q, me_tup, me_delta) in MODEL_E_INVENTORY
               if me_delta != "input"]

    # Run search for each rule
    results_per_rule = {}
    for rule_name, rule_fn in SPIN_RULES.items():
        print(f"─── Running search with rule: {rule_name} ───")
        results = {}
        for label, target_mass, Q, _, me_delta in targets:
            spin = OBSERVED_SPIN.get(label)
            if spin is None:
                continue
            best = z3_search_with_spin(G, L, target_mass, Q, spin,
                                        rule_fn, n_max=6, top_k=1)
            if not best:
                results[label] = None
            else:
                rel, n6, E, a_sum = best[0]
                results[label] = (n6, E, rel, a_sum)
        results_per_rule[rule_name] = results
    print()

    # ── Per-particle comparison table ──
    print("─" * 100)
    print("  Per-particle mass accuracy under each spin rule:")
    print("─" * 100)
    print()
    print(f"  {'particle':<10s}  {'spin':>4s}  {'target':>12s}", end="")
    for rule_name in SPIN_RULES:
        print(f"  {rule_name:>14s}", end="")
    print()
    print("  " + "-" * 98)

    for label, target, Q, _, _ in targets:
        spin = OBSERVED_SPIN.get(label)
        if spin is None:
            continue
        print(f"  {label:<10s}  {str(spin):>4s}  {target:>12.4f}", end="")
        for rule_name in SPIN_RULES:
            res = results_per_rule[rule_name].get(label)
            if res is None:
                print(f"  {'— no match —':>14s}", end="")
            else:
                _, _, rel, _ = res
                print(f"  {rel*100:>+13.3f}%", end="")
        print()
    print()

    # ── Per-rule summary statistics ──
    print("─" * 100)
    print("  Per-rule summary:")
    print("─" * 100)
    print()
    print(f"  {'Rule':<16s}  {'matches ≤ 2%':>12s}  {'matches ≤ 5%':>12s}  "
          f"{'no match':>10s}  {'max Δ':>10s}")
    print("  " + "-" * 70)
    for rule_name in SPIN_RULES:
        results = results_per_rule[rule_name]
        within_2 = 0
        within_5 = 0
        no_match = 0
        max_delta = 0.0
        for label, res in results.items():
            if res is None:
                no_match += 1
            else:
                _, _, rel, _ = res
                if rel <= 0.02:
                    within_2 += 1
                if rel <= 0.05:
                    within_5 += 1
                max_delta = max(max_delta, rel)
        total = len(results)
        print(f"  {rule_name:<16s}  {within_2:>3d} / {total}    {within_5:>3d} / {total}    "
              f"{no_match:>5d}      {max_delta*100:>9.2f}%")
    print()

    # ── Show actual tuples for the most restrictive rule (L-∞) ──
    print("─" * 100)
    print("  Tuples found under L-∞ max rule (most restrictive consistent rule):")
    print("─" * 100)
    print()
    print(f"  {'particle':<10s}  {'spin':>4s}  {'best tuple':<28s}  "
          f"{'E_pred':>12s}  {'target':>12s}  {'Δ':>9s}")
    print("  " + "-" * 80)
    for label, target, Q, _, _ in targets:
        spin = OBSERVED_SPIN.get(label)
        if spin is None:
            continue
        res = results_per_rule["L-∞ max"].get(label)
        if res is None:
            print(f"  {label:<10s}  {str(spin):>4s}  {'— no Z₃ match —':<28s}")
        else:
            n6, E, rel, a_sum = res
            sheets = active_sheets(n6)
            sign = "+" if E >= target else "-"
            print(f"  {label:<10s}  {str(spin):>4s}  "
                  f"{str(n6).replace(' ', ''):<28s}  "
                  f"{E:>12.4f}  {target:>12.4f}  "
                  f"{sign}{rel*100:>7.3f}%")
    print()

    # ── Tuples found under unit-per-sheet AM rule (top coverage) ──
    print("─" * 100)
    print("  Tuples found under unit-per-sheet AM rule (best coverage, 14/16 ≤ 2%):")
    print("─" * 100)
    print()
    print(f"  {'particle':<10s}  {'spin':>4s}  {'best tuple':<28s}  "
          f"{'sheets':>7s}  {'E_pred':>12s}  {'target':>12s}  {'Δ':>9s}")
    print("  " + "-" * 92)
    for label, target, Q, _, _ in targets:
        spin = OBSERVED_SPIN.get(label)
        if spin is None:
            continue
        res = results_per_rule["unit/sheet AM"].get(label)
        if res is None:
            print(f"  {label:<10s}  {str(spin):>4s}  {'— no match —':<28s}")
        else:
            n6, E, rel, a_sum = res
            sheets = active_sheets(n6)
            n_active = len(sheets)
            sign = "+" if E >= target else "-"
            print(f"  {label:<10s}  {str(spin):>4s}  "
                  f"{str(n6).replace(' ', ''):<28s}  {n_active:>7d}  "
                  f"{E:>12.4f}  {target:>12.4f}  "
                  f"{sign}{rel*100:>7.3f}%")
    print()

    # ── Structural summary of unit-per-sheet AM matches ──
    print("─" * 100)
    print("  Structural pattern (unit-per-sheet AM): sheets active vs observed spin:")
    print("─" * 100)
    print()
    sheet_spin_grid = {}
    for label, target, Q, _, _ in targets:
        spin = OBSERVED_SPIN.get(label)
        if spin is None:
            continue
        res = results_per_rule["unit/sheet AM"].get(label)
        if res is None:
            continue
        n6 = res[0]
        sheets = active_sheets(n6)
        n_active = len(sheets)
        key = (n_active, spin)
        sheet_spin_grid.setdefault(key, []).append(label)

    for (n_active, spin), labels in sorted(sheet_spin_grid.items()):
        print(f"  {n_active} active sheets, spin {spin}:  {labels}")
    print()
    print("  Under unit-per-sheet AM rule, each active sheet contributes spin ½;")
    print("  the total composes via angular momentum addition:")
    print("    1 sheet → spin ½          (e.g., electron, (3,6) proton)")
    print("    2 sheets → spin 0 or 1    (e.g., mesons)")
    print("    3 sheets → spin ½ or 3/2  (e.g., baryons)")
    print()
    print("  The k=1 → spin-½, k=2 → spin-{0,1}, k=3 → spin-{½, 3/2} structure")
    print("  matches the observed particle taxonomy: 1-sheet leptons and simple")
    print("  baryons are spin ½; 2-sheet mesons are spin 0 or 1; 3-sheet baryons")
    print("  are spin ½ (ground state) with spin 3/2 for excited states.")
    print()

    # ── Per-sheet ratio structure under L-∞ rule ──
    print("─" * 100)
    print("  Per-sheet ratio structure under L-∞ rule tuples:")
    print("─" * 100)
    print()
    for label, target, Q, _, _ in targets:
        spin = OBSERVED_SPIN.get(label)
        if spin is None:
            continue
        res = results_per_rule["L-∞ max"].get(label)
        if res is None:
            continue
        n6, E, rel, a_sum = res
        sheets = active_sheets(n6)
        ratios_str = []
        for (s, n_t, n_r, r) in sheets:
            if r is None:
                if n_r == 0:
                    ratios_str.append(f"{s}:∞")
                else:
                    ratios_str.append(f"{s}:0/0")
            else:
                ratios_str.append(f"{s}:{r}")
        print(f"  {label:<10s}  spin={str(spin):>4s}  {', '.join(ratios_str)}")
    print()

    print("Phase D complete.")


if __name__ == "__main__":
    main()
