"""
R63 Track 9 Phase 9b — Non-additive tuple search for the deuteron.

Phase 9a falsified linear cross-shear dressing of the additive
composition tuple as a binding mechanism.  The falsification was
conditional on the additive composition being the correct compound
tuple for bound nuclei.  Phase 9b tests whether it actually is — by
searching for v2-compatible Ma tuples at (A=2, Z=1) that have lower
mass than the 1876.54 MeV additive prediction.

If a lighter tuple exists at or below the observed 1875.61 MeV, the
deuteron bound state is that tuple rather than the additive sum,
and nuclear binding is in Ma via non-additive tuple selection.

If no such tuple exists within the search envelope, Path A is
falsified for the deuteron and Track 9 proceeds to Phase 9c (mass-
formula validity at high n_pt).

Search setup:
  - Target mass: 1875.61 MeV (observed deuteron)
  - Reference mass: 1876.54 MeV (additive prediction, needs beating)
  - Search envelope: ±Δ around additive tuple (1, 2, -1, -1, 6, 12)
  - Filters: Z₃ on p-sheet (n_pt multiple of 3); positive g-candidate
    v2 per-sheet charge (consistency with deuteron being a charged
    composite is handled by ingredient-sum, but we report per-sheet
    values for inspection).

Outputs:
  - printed table of top candidates
  - outputs/track9_phase9b_deuteron_candidates.csv
"""

import sys, os
import csv
from pathlib import Path
from itertools import product

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    derive_L_ring, L_vector_from_params, mode_energy, mode_6_to_11,
    signature_ok, M_E_MEV, M_P_MEV,
    SQRT_ALPHA, FOUR_PI, ALPHA,
    Params,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF

from track6_phase6a_compatibility import classify_sheet_v2, sheet_charge_v2


# ─── g-candidate working parameters ────────────────────────────────

def build_working_params():
    return Params(
        eps_e=397.074, s_e=2.0042,
        eps_p=0.55, s_p=0.162037,
        eps_nu=2.0, s_nu=0.022,
        k_e=K_MODELF, k_p=K_MODELF, k_nu=K_MODELF,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI * ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=derive_L_ring(M_E_MEV, 1, 2, 397.074, 2.0042, K_MODELF),
        L_ring_p=derive_L_ring(M_P_MEV, 3, 6, 0.55, 0.162037, K_MODELF),
        L_ring_nu=derive_L_ring(3.21e-8, 1, 1, 2.0, 0.022, K_MODELF),
    )


# ─── Targets ────────────────────────────────────────────────────────

DEUTERON_MASS_OBS = 1875.61  # MeV
ADDITIVE_TUPLE = (1, 2, -1, -1, 6, 12)
ADDITIVE_MASS = 1876.544  # computed in Phase 8a

DEUTERON_OBSERVED_Q = +1  # ingredient-sum charge


# ─── Search ─────────────────────────────────────────────────────────

def compound_v2_charge(tup):
    """v2 per-sheet charge of the compound tuple (for reference only;
    composite charge should come from ingredient sum in the bound-
    state interpretation)."""
    n_et, n_er, n_nut, n_nur, n_pt, n_pr = tup
    c_e  = classify_sheet_v2(n_et,  n_er)
    c_nu = classify_sheet_v2(n_nut, n_nur)
    c_p  = classify_sheet_v2(n_pt,  n_pr)
    return (sheet_charge_v2("e",  c_e[0],  c_e[2])
            + sheet_charge_v2("nu", c_nu[0], c_nu[2])
            + sheet_charge_v2("p",  c_p[0],  c_p[2]))


def search(delta_e=3, delta_nu=3, delta_p_tube=3, delta_p_ring=6,
           max_hits=200):
    """Scan tuples within ±Δ of the additive deuteron tuple.

    Envelope is asymmetric: the p-sheet dominates mass so we scan
    it more carefully (Δ_p_tube=3 in steps of 3 to preserve Z₃,
    Δ_p_ring=6 with step 1).  ν-sheet has negligible effect so we
    keep a small scan there for completeness.
    """
    params = build_working_params()
    G = build_aug_metric(params)
    assert signature_ok(G), "signature broken at working params"
    L = L_vector_from_params(params)

    # Center on additive tuple
    ce, cr, cnu_t, cnu_r, cpt, cpr = ADDITIVE_TUPLE

    # Ranges
    e_tube_range  = range(ce - delta_e,  ce + delta_e + 1)
    e_ring_range  = range(cr - delta_e,  cr + delta_e + 1)
    nu_t_range    = range(cnu_t - delta_nu, cnu_t + delta_nu + 1)
    nu_r_range    = range(cnu_r - delta_nu, cnu_r + delta_nu + 1)
    # Z₃: n_pt must be multiple of 3; step through multiples near 6
    pt_values     = [v for v in range(cpt - delta_p_tube, cpt + delta_p_tube + 1)
                     if v % 3 == 0]
    pr_range      = range(cpr - delta_p_ring, cpr + delta_p_ring + 1)

    results = []
    total = 0
    for n_et in e_tube_range:
        for n_er in e_ring_range:
            for n_nut in nu_t_range:
                for n_nur in nu_r_range:
                    for n_pt in pt_values:
                        for n_pr in pr_range:
                            tup = (n_et, n_er, n_nut, n_nur, n_pt, n_pr)
                            if tup == (0, 0, 0, 0, 0, 0):
                                continue
                            total += 1
                            try:
                                E = mode_energy(G, L, mode_6_to_11(tup))
                            except Exception:
                                continue
                            if E <= 0 or E != E:
                                continue
                            # Only keep candidates with mass within ±2% of observed
                            rel = (E - DEUTERON_MASS_OBS) / DEUTERON_MASS_OBS
                            if abs(rel) > 0.02:
                                continue
                            Q_v2 = compound_v2_charge(tup)
                            results.append({
                                'tuple': tup, 'E': E, 'rel': rel,
                                'Q_v2': Q_v2,
                            })

    print(f"  Scanned {total:,} tuples; {len(results)} within ±2% of observed")
    results.sort(key=lambda r: r['E'])
    return results


# ─── Main ───────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 112)
    print("R63 Track 9 Phase 9b — Non-additive tuple search for the deuteron")
    print("=" * 112)
    print(f"  Observed deuteron mass: {DEUTERON_MASS_OBS} MeV")
    print(f"  Additive tuple:  {ADDITIVE_TUPLE}  → mass {ADDITIVE_MASS:.3f} MeV")
    print(f"  Binding target:  ~2.2 MeV (observed − additive)")
    print(f"  Search envelope: Δ=3 on e and ν, Δ=3 on n_pt (Z₃-filtered),")
    print(f"                   Δ=6 on n_pr")
    print()

    results = search()

    # Print top candidates below additive
    below_additive = [r for r in results if r['E'] < ADDITIVE_MASS]
    above_or_equal = [r for r in results if r['E'] >= ADDITIVE_MASS]

    print(f"  Candidates BELOW additive ({ADDITIVE_MASS:.3f} MeV): {len(below_additive)}")
    print(f"  Candidates at or above additive: {len(above_or_equal)}")
    print()

    if below_additive:
        print("  Top 20 tuples lighter than additive (ranked by mass closeness to observed):")
        # Sort these by closeness to observed
        below_ranked = sorted(below_additive,
                              key=lambda r: abs(r['E'] - DEUTERON_MASS_OBS))
        print(f"    {'tuple':<30s}  {'E_pred (MeV)':>14s}  "
              f"{'Δm/m':>10s}  {'Q_v2':>5s}  {'below-additive':>14s}")
        for r in below_ranked[:20]:
            tup_str = str(r['tuple']).replace(' ', '')
            below_add = ADDITIVE_MASS - r['E']
            print(f"    {tup_str:<30s}  {r['E']:>14.5f}  "
                  f"{r['rel']*100:>+9.4f}%  {r['Q_v2']:>+5d}  "
                  f"{below_add:>+14.4f}")
        print()

        # Save all lighter-than-additive to CSV
        csv_path = out_dir / "track9_phase9b_deuteron_candidates.csv"
        with open(csv_path, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['rank', 'tuple', 'E_pred', 'rel_error', 'Q_v2',
                        'below_additive_MeV'])
            for rank, r in enumerate(below_ranked, 1):
                tup_str = str(r['tuple']).replace(' ', '')
                w.writerow([rank, tup_str, f"{r['E']:.6f}",
                            f"{r['rel']:.8f}", r['Q_v2'],
                            f"{ADDITIVE_MASS - r['E']:.4f}"])
        print(f"  CSV: {csv_path}  ({len(below_ranked)} entries)")
    else:
        print("  No tuple within envelope has mass below the additive "
              f"{ADDITIVE_MASS:.3f} MeV.")
        print("  Additive is the envelope-minimum for the deuteron.")
        print()

    # Specific check: is there any tuple within 0.5 MeV of observed?
    close_to_observed = [r for r in results
                          if abs(r['E'] - DEUTERON_MASS_OBS) < 0.5]
    print(f"  Tuples within 0.5 MeV of observed 1875.61 MeV: {len(close_to_observed)}")
    if close_to_observed:
        print(f"    {'tuple':<30s}  {'E_pred (MeV)':>14s}  "
              f"{'Δm':>10s}  {'Q_v2':>5s}")
        for r in close_to_observed[:10]:
            tup_str = str(r['tuple']).replace(' ', '')
            dm = r['E'] - DEUTERON_MASS_OBS
            print(f"    {tup_str:<30s}  {r['E']:>14.5f}  "
                  f"{dm:>+10.4f}  {r['Q_v2']:>+5d}")
    print()

    # Verdict
    print("─" * 112)
    if below_additive:
        best = sorted(below_additive, key=lambda r: r['E'])[0]
        best_mass = best['E']
        gap_closed = ADDITIVE_MASS - best_mass
        remaining = best_mass - DEUTERON_MASS_OBS
        print(f"  Lightest tuple found:  {best['tuple']}  at {best_mass:.4f} MeV")
        print(f"  Closes gap by:   {gap_closed:.4f} MeV (observed gap = 2.2 MeV)")
        print(f"  Remaining to observed: {remaining:.4f} MeV")
        if remaining <= 0.5:
            print(f"  ✓ PASSES deuteron target — non-additive tuple "
                  f"reproduces observed mass")
        elif gap_closed >= 1.0:
            print(f"  ⚠ PARTIAL — tuple below additive but not at observed")
        else:
            print(f"  ✗ Gap closure < 1 MeV — not a plausible binding mechanism")
    else:
        print(f"  FALSIFIED: no tuple in the ±3/±6 envelope is lighter than")
        print(f"  the additive prediction.  Additive is locally optimal for")
        print(f"  the deuteron.  Proceed to Phase 9c (mass-formula validity).")
    print()


if __name__ == "__main__":
    main()
