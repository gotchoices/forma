"""
R63 Track 6 Phase 6b-pion — Constrained pion tuple re-derivation under v2.

Phase 6c exposed that Phase 6a's Q-only filter let two particles through
with correct charge but catastrophic mass match: π⁰ (+10.37%) and
π± (+13.32%) at model-F baseline.  Phase 6c also showed that no ratio
shift within the v2 landscape closes pions without simultaneously
breaking 12 other hadrons.

This script searches the v2 tuple lattice specifically for pion candidates
at MODEL-F BASELINE ratios — looking for alternative assignments that
close the mass gap while (by construction) preserving the 17 working
particles whose tuples are held fixed.

Search parameters:
  - Target masses: π⁰ 134.977 MeV (|Q|=0), π± 139.570 MeV (|Q|=1)
  - Envelope: |n_i| ≤ 6 initially (extendable); n_pt ∈ {0, ±3, ±6} (Z₃)
  - Filters: v2 predicted charge matches observed; mass within 2% floor
  - Dedup: by (n_et, n_er, n_pt, n_pr) non-ν structure

Output:
  - prints the top matches per target (tight and medium tiers)
  - CSV of all dedup'd candidates

If nothing lands within 2%, widens envelope to |n_i| ≤ 8 and retries.
"""

import sys, os
import csv
import math
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    L_vector_from_params, mode_energy, mode_6_to_11,
    derive_L_ring, M_P_MEV,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF, modelF_baseline

from track6_phase6a_compatibility import (
    classify_sheet_v2, sheet_charge_v2,
)


TARGETS = [
    ("pi0",   134.977, 0),
    ("pi_pm", 139.570, 1),
]

Z3_N_PT = {-6, -3, 0, 3, 6}
MASS_THRESHOLD = 0.02
TIGHT_THRESHOLD = 1e-3  # 0.1% — "near-exact"
TOP_K = 10
# If nothing within MASS_THRESHOLD, fall back to a wider net to characterize
# the real gap.
WIDE_THRESHOLD = 0.30


def v2_predicted_Q(tup):
    n_et, n_er, n_nut, n_nur, n_pt, n_pr = tup
    c_e  = classify_sheet_v2(n_et, n_er)
    c_nu = classify_sheet_v2(n_nut, n_nur)
    c_p  = classify_sheet_v2(n_pt, n_pr)
    Q = (sheet_charge_v2("e",  c_e[0],  c_e[2]) +
         sheet_charge_v2("nu", c_nu[0], c_nu[2]) +
         sheet_charge_v2("p",  c_p[0],  c_p[2]))
    return Q, c_e, c_nu, c_p


def search_target(G, L, target_mass, absQ, n_max=6,
                  mass_threshold=MASS_THRESHOLD):
    rng = range(-n_max, n_max + 1)
    results = []
    for n_et in rng:
        for n_er in rng:
            for n_nut in rng:
                for n_nur in rng:
                    for n_pt in rng:
                        if n_pt not in Z3_N_PT:
                            continue
                        for n_pr in rng:
                            if n_et == n_er == n_nut == n_nur == n_pt == n_pr == 0:
                                continue
                            tup = (n_et, n_er, n_nut, n_nur, n_pt, n_pr)
                            Q_pred, c_e, c_nu, c_p = v2_predicted_Q(tup)
                            if abs(Q_pred) != absQ:
                                continue
                            n11 = mode_6_to_11(tup)
                            E = mode_energy(G, L, n11)
                            if E is None or E <= 0:
                                continue
                            rel = abs(E - target_mass) / target_mass
                            if rel > mass_threshold:
                                continue
                            results.append({
                                'tuple': tup, 'E_pred': E, 'rel': rel,
                                'Q_pred': Q_pred,
                                'e_cat': c_e[0], 'e_k': c_e[1],
                                'e_pt': c_e[2], 'e_pr': c_e[3],
                                'nu_cat': c_nu[0], 'nu_k': c_nu[1],
                                'p_cat': c_p[0], 'p_k': c_p[1],
                                'p_pt': c_p[2], 'p_pr': c_p[3],
                            })
    results.sort(key=lambda r: r['rel'])
    # Dedup by (n_et, n_er, n_pt, n_pr) — ν variants are mass-equivalent
    seen = set()
    deduped = []
    for r in results:
        t = r['tuple']
        key = (t[0], t[1], t[4], t[5])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)
    return deduped


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    # Model-F baseline metric
    L_ring_p = derive_L_ring(M_P_MEV, 3, 6, 0.55, 0.162037, K_MODELF)
    p = modelF_baseline(L_ring_p=L_ring_p)
    G = build_aug_metric(p)
    L = L_vector_from_params(p)

    print("=" * 108)
    print("R63 Track 6 Phase 6b-pion — v2 tuple search for π⁰ and π± at model-F baseline")
    print("=" * 108)
    print(f"  Ratios: ε_p=0.55, s_p=0.162, ε_e=397.074, s_e=2.0042, ε_ν=2.0, s_ν=0.022")
    print(f"  Filters: v2 Q match, Z₃ p-sheet, |Δm/m| ≤ {MASS_THRESHOLD*100:.0f}%")
    print()

    all_rows = []
    for name, target_mass, absQ in TARGETS:
        print(f"── {name}   target = {target_mass:.3f} MeV   |Q| = {absQ}")
        cands = search_target(G, L, target_mass, absQ, n_max=6)
        envelope = 6
        if not cands:
            print(f"    No candidates at |n_i| ≤ 6 within ±{MASS_THRESHOLD*100:.0f}%.")
            print(f"    Widening to |n_i| ≤ 8...")
            cands = search_target(G, L, target_mass, absQ, n_max=8)
            envelope = 8

        if not cands:
            print(f"    No candidates at |n_i| ≤ 8 within ±{MASS_THRESHOLD*100:.0f}%.")
            print(f"    Falling back to wide search (±{WIDE_THRESHOLD*100:.0f}%)"
                  f" to characterize the gap...")
            cands = search_target(G, L, target_mass, absQ, n_max=8,
                                   mass_threshold=WIDE_THRESHOLD)
            if not cands:
                print(f"    Still no v2-compatible tuples within ±{WIDE_THRESHOLD*100:.0f}%.")
                print()
                continue
            print(f"    Found {len(cands)} candidates within "
                  f"±{WIDE_THRESHOLD*100:.0f}% (v2 cannot reach ±2%)")

        tight = [r for r in cands if r['rel'] <= TIGHT_THRESHOLD]
        print(f"    {len(cands)} distinct candidates at |n_i| ≤ {envelope}; "
              f"{len(tight)} tighter than {TIGHT_THRESHOLD*100:.2f}%")
        print(f"    Top {min(TOP_K, len(cands))}:")
        print(f"    {'tuple':<30s}  {'E_pred':>10s}  {'Δm/m':>10s}  "
              f"{'Q':>3s}  {'e-cat':<14s}  {'p-cat':<14s}")
        for r in cands[:TOP_K]:
            tup_str = str(r['tuple']).replace(' ', '')
            print(f"    {tup_str:<30s}  {r['E_pred']:>10.4f}  "
                  f"{r['rel']*100:>+9.5f}%  {r['Q_pred']:>+3d}  "
                  f"{r['e_cat']:<14s}  {r['p_cat']:<14s}")
        print()

        for rank, r in enumerate(cands[:TOP_K], 1):
            all_rows.append({
                'particle': name, 'rank': rank,
                'target_mass': target_mass, 'absQ': absQ,
                'envelope': envelope,
                'tuple': str(r['tuple']).replace(' ', ''),
                'E_pred': f"{r['E_pred']:.5f}",
                'rel_error': f"{r['rel']:.6e}",
                'Q_pred': r['Q_pred'],
                'e_cat': r['e_cat'], 'e_k': r['e_k'],
                'e_pt': r['e_pt'], 'e_pr': r['e_pr'],
                'nu_cat': r['nu_cat'], 'nu_k': r['nu_k'],
                'p_cat': r['p_cat'], 'p_k': r['p_k'],
                'p_pt': r['p_pt'], 'p_pr': r['p_pr'],
            })

    if all_rows:
        csv_path = out_dir / "track6_phase6b_pion_candidates.csv"
        fieldnames = list(all_rows[0].keys())
        with open(csv_path, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            for row in all_rows:
                w.writerow(row)
        print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
