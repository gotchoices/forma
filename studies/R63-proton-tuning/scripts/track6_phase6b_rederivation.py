"""
R63 Track 6 Phase 6b: Constrained tuple re-derivation for the 5 particles
that failed Phase 6a under Q132 v2.

For each failing particle, search the 6-tuple integer lattice for tuples
that simultaneously:
  1. Match the particle's observed mass to within 2% (width-weighted
     threshold for the narrow hadrons; same tolerance R60 T19 used).
  2. Produce the correct compound charge under the v2 per-sheet rule.
  3. Satisfy Z₃ on the p-sheet (|n_pt| ∈ {0, ±3, ±6} for free modes).

The search envelope is |n_i| ≤ 6 (same as R60 T19).  Mass is computed
with the model-F baseline metric (ε_p = 0.55, s_p = 0.162, L_ring_p
calibrated to the (3, 6) proton), so that passing candidates are
drop-in replacements for the R60 T19 tuples under v2.

Failing particles from Phase 6a:
  tau       (1776.86 MeV, |Q|=1)
  Lambda    (1115.68 MeV, |Q|=0)
  Sigma_-   (1197.45 MeV, |Q|=1)
  Xi_-      (1321.71 MeV, |Q|=1)
  Xi_0      (1314.86 MeV, |Q|=0)

Output: top candidates per particle in CSV + printed table.
"""

import sys, os
import csv
import math
from pathlib import Path
from itertools import product

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


# ─── Targets ──────────────────────────────────────────────────────

# (name, observed_mass_MeV, |Q_observed|)
TARGETS = [
    ("tau",      1776.86, 1),
    ("Lambda",   1115.68, 0),
    ("Sigma_-",  1197.45, 1),
    ("Xi_-",     1321.71, 1),
    ("Xi_0",     1314.86, 0),
]

MASS_THRESHOLD = 0.02   # 2% tolerance for the match, matching R60 T19
TOP_K = 5               # top candidates per particle

# Z₃ constraint on free p-sheet modes
Z3_N_PT = {-6, -3, 0, 3, 6}


# ─── v2 predicted charge for a 6-tuple ───────────────────────────

def v2_predicted_Q(tup):
    """Return predicted compound charge under Q132 v2.  Returns None
    if any sheet is in a structurally incoherent state (e.g., gcd=1
    primitive with |p_t|>1 on a sheet that is supposed to be binding —
    though here we simply let the phase-cancellation rule zero that
    sheet's contribution)."""
    n_et, n_er, n_nut, n_nur, n_pt, n_pr = tup
    c_e  = classify_sheet_v2(n_et, n_er)
    c_nu = classify_sheet_v2(n_nut, n_nur)
    c_p  = classify_sheet_v2(n_pt, n_pr)
    Q = (sheet_charge_v2("e",  c_e[0],  c_e[2]) +
         sheet_charge_v2("nu", c_nu[0], c_nu[2]) +
         sheet_charge_v2("p",  c_p[0],  c_p[2]))
    return Q, c_e, c_nu, c_p


# ─── Search ───────────────────────────────────────────────────────

def search_for_target(G, L, target_mass, absQ, n_max=6):
    """Brute-force integer search subject to v2 charge + Z₃ constraints."""
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
                            if E <= 0:
                                continue
                            rel = abs(E - target_mass) / target_mass
                            if rel > MASS_THRESHOLD:
                                continue
                            results.append({
                                'tuple': tup, 'E_pred': E, 'rel': rel,
                                'Q_pred': Q_pred,
                                'e_cat': c_e[0], 'nu_cat': c_nu[0], 'p_cat': c_p[0],
                                'e_k': c_e[1], 'nu_k': c_nu[1], 'p_k': c_p[1],
                            })
    results.sort(key=lambda r: r['rel'])

    # Deduplicate by (n_et, n_er, n_pt, n_pr): ν-sheet windings have
    # negligible mass contribution at R61 geometry, so ν-only variants
    # are physically equivalent.  Keep the best representative per
    # equivalence class.
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


# ─── Main ─────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    # Baseline metric (same as R60 T19)
    L_ring_p_36 = derive_L_ring(M_P_MEV, 3, 6, 0.55, 0.162037, K_MODELF)
    p = modelF_baseline(L_ring_p=L_ring_p_36)
    G = build_aug_metric(p)
    L = L_vector_from_params(p)

    print("=" * 108)
    print("R63 Track 6 Phase 6b — Q132 v2 constrained tuple re-derivation")
    print("=" * 108)
    print(f"  Baseline: model-F (3, 6) calibration; ε_p=0.55, s_p=0.162")
    print(f"  Search: |n_i| ≤ 6, n_pt ∈ Z₃, v2 Q matches observed, mass match ≤ 2%")
    print()

    all_rows = []
    summary = {}
    for name, target_mass, absQ in TARGETS:
        print(f"── {name}   target = {target_mass:.3f} MeV   |Q| = {absQ}")
        cands = search_for_target(G, L, target_mass, absQ)
        if not cands:
            print(f"    NO CANDIDATES within ±{MASS_THRESHOLD*100:.1f}% — widen envelope or re-examine")
            summary[name] = 0
            print()
            continue

        print(f"    {len(cands)} candidate tuples (showing top {min(TOP_K, len(cands))}):")
        print(f"    {'tuple':<30s}  {'E_pred':>10s}  {'Δm/m':>8s}  "
              f"{'Q':>3s}  {'e-cat':<14s}  {'nu-cat':<14s}  {'p-cat':<14s}")
        for r in cands[:TOP_K]:
            tup_str = str(r['tuple']).replace(' ', '')
            print(f"    {tup_str:<30s}  {r['E_pred']:>10.3f}  "
                  f"{r['rel']*100:>+7.3f}%  {r['Q_pred']:>+3d}  "
                  f"{r['e_cat']:<14s}  {r['nu_cat']:<14s}  {r['p_cat']:<14s}")
        print()

        summary[name] = len(cands)
        for rank, r in enumerate(cands[:TOP_K], 1):
            all_rows.append({
                'particle': name,
                'rank': rank,
                'target_mass': target_mass,
                'absQ_observed': absQ,
                'tuple': str(r['tuple']).replace(' ', ''),
                'E_pred': f"{r['E_pred']:.4f}",
                'rel_error': f"{r['rel']:.6f}",
                'Q_predicted': r['Q_pred'],
                'e_category': r['e_cat'],
                'e_k': r['e_k'],
                'nu_category': r['nu_cat'],
                'nu_k': r['nu_k'],
                'p_category': r['p_cat'],
                'p_k': r['p_k'],
            })

    print("=" * 108)
    print("  Phase 6b summary:")
    for name in [t[0] for t in TARGETS]:
        n = summary.get(name, 0)
        status = "✓ candidates found" if n > 0 else "✗ NO candidates — needs wider search or framework extension"
        print(f"    {name:<10s}  {n:>4d} candidates    {status}")
    print()

    # CSV
    if all_rows:
        csv_path = out_dir / "track6_phase6b_rederivation.csv"
        fieldnames = list(all_rows[0].keys())
        with open(csv_path, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            for row in all_rows:
                w.writerow(row)
        print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
