"""
R64 Track 10 Phase 10b — Aleph-redundancy audit.

User-proposed simplification: can the 11D metric reduce to 10D by
removing aleph entirely?  The replacement: direct sheet-spacetime
couplings (σ_xt_t, σ_xr_t, etc.) instead of routing through aleph.

Methodology: in the 11D framework, ZERO OUT all aleph row entries
(σ_ta, σ_at, σ_ra, σ_aS) so aleph becomes effectively isolated, then
add direct sheet-time entries as compensation.  Search for values
that preserve α universality across the inventory and produce
α ≈ 1/137 at the right magnitude.

If the search succeeds: aleph is removable and the metric
simplifies to effectively 10D.

If the search fails: aleph is structurally required.

Outputs:
  outputs/track10_phase10b_aleph_audit.csv
"""

import os
import sys
import math
import csv
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

R60_SCRIPTS = Path(__file__).resolve().parent.parent.parent / "R60-metric-11" / "scripts"
sys.path.insert(0, str(R60_SCRIPTS))

from track1_solver import (    # noqa: E402
    Params, alpha_coulomb, mode_6_to_11, num_negative_eigs,
    ALPHA, SQRT_ALPHA, FOUR_PI, HBAR_C_MEV_FM,
    I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING, I_NU_TUBE, I_NU_RING,
    I_ALEPH, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import track9_params    # noqa: E402


TEST_MODES = [
    ("electron", (1, 2, 0, 0, 0, 0)),
    ("muon",     (1, 1, -2, -2, 0, 0)),
    ("proton",   (0, 0, 0, 0, 1, 3)),
    ("neutron",  (0, -4, -1, 2, 0, -3)),
    ("Lambda",   (-1, 2, -1, 2, -1, 3)),
    ("Sigma_-",  (-1, 2, -2, 2, -2, -2)),
    ("pi0",      (0, -1, -2, -2, 0, 0)),
    ("pi_pm",    (-1, -1, -3, -3, 0, 0)),
    ("K_pm",     (-1, -6, -2, 2, 0, 1)),
    ("rho",      (-1, 5, -2, 2, 0, 1)),
]


def expected_alpha_sum_squared(tup):
    n_et, _, n_νt, _, n_pt, _ = tup
    return (n_et - n_pt + n_νt) ** 2


def alpha_spread(G):
    values = []
    for label, tup in TEST_MODES:
        n11 = mode_6_to_11(tup)
        a = alpha_coulomb(G, n11)
        sq = expected_alpha_sum_squared(tup)
        if sq > 0:
            values.append(a / (ALPHA * sq))
    if not values:
        return float('inf')
    return max(values) - min(values)


def alpha_proton(G):
    """α_Coulomb on the proton mode (n_pt=1, n_pr=3 model-F)."""
    n11 = mode_6_to_11((0, 0, 0, 0, 1, 3))
    return alpha_coulomb(G, n11)


def build_metric_no_aleph(p, **direct_entries):
    """Build 11D metric with all aleph couplings zeroed and direct
    sheet-spacetime entries added.  Effectively 10D — aleph is
    isolated (only its diagonal entry remains).

    direct_entries: σ_xt_t, σ_xr_t for x ∈ {e, p, ν}; optional
    σ_xt_S, σ_xr_S as well.
    """
    # Start from R60 augmented metric
    G = build_aug_metric(p).copy()

    # Zero out aleph row and column (except diagonal)
    for idx in (I_E_TUBE, I_E_RING, I_NU_TUBE, I_NU_RING,
                I_P_TUBE, I_P_RING, I_T, I_SX, I_SY, I_SZ):
        G[I_ALEPH, idx] = 0.0
        G[idx, I_ALEPH] = 0.0

    # Add direct sheet-time entries
    sheet_indices = {
        'et': I_E_TUBE, 'er': I_E_RING,
        'pt': I_P_TUBE, 'pr': I_P_RING,
        'νt': I_NU_TUBE, 'νr': I_NU_RING,
    }

    for sheet_key, idx in sheet_indices.items():
        # Direct sheet-time
        key_t = f"sigma_{sheet_key}_t"
        if key_t in direct_entries and direct_entries[key_t] != 0:
            G[idx, I_T] += direct_entries[key_t]
            G[I_T, idx] += direct_entries[key_t]
        # Direct sheet-spatial (S-isotropic)
        key_S = f"sigma_{sheet_key}_S"
        if key_S in direct_entries and direct_entries[key_S] != 0:
            for s_idx in (I_SX, I_SY, I_SZ):
                G[idx, s_idx] += direct_entries[key_S]
                G[s_idx, idx] += direct_entries[key_S]

    return G


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 10 Phase 10b — Aleph-redundancy audit (10D direct-coupling)")
    print("=" * 100)
    print()

    p = track9_params()

    # ─── Part 1: All aleph entries zeroed, no replacement ───
    print("=" * 80)
    print("Part 1 — Baseline: zero all aleph couplings, no replacement")
    print("=" * 80)
    print()
    G_no_aleph = build_metric_no_aleph(p)
    sig_ok = num_negative_eigs(G_no_aleph) == 1
    spread = alpha_spread(G_no_aleph)
    a_p = alpha_proton(G_no_aleph)
    print(f"  Signature OK: {sig_ok}")
    print(f"  α universality spread: {spread:.4e}")
    print(f"  α(proton): {a_p:.6e}  (target: {ALPHA:.6e} = 1/137)")
    print()
    if sig_ok and spread < 1e-9 and abs(a_p - ALPHA) / ALPHA < 0.01:
        print("  → Aleph is fully redundant; removing it preserves everything.")
        return
    elif sig_ok:
        print("  → Aleph removal preserves signature but breaks α magnitude or universality.")
    else:
        print("  → Aleph removal breaks signature.  Search direct entries.")
    print()

    # ─── Part 2: Search direct sheet-time entries ───
    print("=" * 80)
    print("Part 2 — Search direct sheet-time coupling prescriptions")
    print("=" * 80)
    print()
    print("  Hypotheses:")
    print("    H_T1: only σ_pt_t  (1 parameter)")
    print("    H_T2: σ_xt_t for x ∈ {e, p, ν}  (3 parameters)")
    print("    H_T3: σ_xt_t and σ_xr_t for x ∈ {e, p, ν}  (6 parameters)")
    print()

    # Cost includes BOTH α universality AND α magnitude constraint
    # to prevent degenerate "all α = 0" solutions
    def cost_with_magnitude(G):
        if num_negative_eigs(G) != 1:
            return 1.0
        spread = alpha_spread(G)
        a_p = alpha_proton(G)
        # Penalty for α(proton) deviating from 1/137
        magnitude_error = abs(a_p / ALPHA - 1) if ALPHA > 0 else 0
        return spread + 0.1 * magnitude_error

    def cost_HT1(coeffs, p):
        sigma_pt_t, = coeffs
        G = build_metric_no_aleph(p, sigma_pt_t=sigma_pt_t)
        return cost_with_magnitude(G)

    def cost_HT2(coeffs, p):
        e, q, n = coeffs
        G = build_metric_no_aleph(
            p, sigma_et_t=e, sigma_pt_t=q, sigma_νt_t=n,
        )
        return cost_with_magnitude(G)

    def cost_HT3(coeffs, p):
        et, er, pt, pr, nt, nr = coeffs
        G = build_metric_no_aleph(
            p,
            sigma_et_t=et, sigma_er_t=er,
            sigma_pt_t=pt, sigma_pr_t=pr,
            sigma_νt_t=nt, sigma_νr_t=nr,
        )
        return cost_with_magnitude(G)

    HYPS = {
        "H_T1: σ_pt_t only":
            (cost_HT1, ['sigma_pt_t'], np.array([0.01])),
        "H_T2: σ_xt_t for all 3 sheets":
            (cost_HT2, ['σ_et_t', 'σ_pt_t', 'σ_νt_t'],
             np.array([0.01, 0.01, 0.01])),
        "H_T3: σ_xt_t and σ_xr_t for all 3 sheets":
            (cost_HT3,
             ['σ_et_t', 'σ_er_t', 'σ_pt_t', 'σ_pr_t', 'σ_νt_t', 'σ_νr_t'],
             np.array([0.01, 0.01, 0.01, 0.01, 0.01, 0.01])),
    }

    best_global = None
    rows = []

    for hyp_name, (cost_fn, params, x0) in HYPS.items():
        print(f"  --- {hyp_name} ---")
        # Multi-start optimization
        best_for_hyp = None
        best_x = None
        for trial in range(10):
            x0_trial = x0 + np.random.randn(len(x0)) * 0.05
            try:
                result = minimize(
                    cost_fn, x0_trial,
                    args=(p,),
                    method='Nelder-Mead',
                    options={'xatol': 1e-12, 'fatol': 1e-14,
                              'maxiter': 30000},
                )
            except Exception as ex:
                continue
            if best_for_hyp is None or result.fun < best_for_hyp:
                best_for_hyp = result.fun
                best_x = result.x.copy()

        if best_x is None:
            print(f"    (no valid optimization completed)")
            print()
            continue

        params_str = "  ".join(f"{p_name}={v:+.6f}"
                                for p_name, v in zip(params, best_x))
        verdict = ("exact" if best_for_hyp < 1e-9 else
                   "good" if best_for_hyp < 1e-3 else
                   "fail")
        print(f"    {params_str}")
        print(f"    α-spread: {best_for_hyp:.4e}  [{verdict}]")

        # Check signature and α magnitude at solution
        if hyp_name.startswith("H_T1"):
            G_test = build_metric_no_aleph(p, sigma_pt_t=best_x[0])
        elif hyp_name.startswith("H_T2"):
            e, q, n = best_x
            G_test = build_metric_no_aleph(
                p, sigma_et_t=e, sigma_pt_t=q, sigma_νt_t=n,
            )
        else:
            et, er, pt, pr, nt, nr = best_x
            G_test = build_metric_no_aleph(
                p,
                sigma_et_t=et, sigma_er_t=er,
                sigma_pt_t=pt, sigma_pr_t=pr,
                sigma_νt_t=nt, sigma_νr_t=nr,
            )

        sig_ok = num_negative_eigs(G_test) == 1
        a_p_at = alpha_proton(G_test)
        print(f"    Signature OK: {sig_ok}")
        print(f"    α(proton): {a_p_at:.6e}  "
              f"(target {ALPHA:.6e}; ratio {a_p_at/ALPHA:.4f})")

        rows.append({
            'hypothesis': hyp_name,
            'n_params': len(params),
            'alpha_spread': best_for_hyp,
            'signature_ok': sig_ok,
            'alpha_proton': a_p_at,
            'alpha_ratio_to_target': a_p_at / ALPHA if ALPHA > 0 else float('nan'),
            **{p_name: float(v) for p_name, v in zip(params, best_x)},
        })

        if best_global is None or best_for_hyp < best_global['alpha_spread']:
            best_global = rows[-1]
        print()

    # ─── Save CSV ───
    if rows:
        csv_path = out_dir / "track10_phase10b_aleph_audit.csv"
        all_keys = sorted(set().union(*(r.keys() for r in rows)))
        with open(csv_path, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=all_keys)
            w.writeheader()
            for r in rows:
                w.writerow(r)
        print(f"  CSV: {csv_path}")
        print()

    # ─── Verdict ───
    print("=" * 100)
    print("VERDICT — Phase 10b: aleph-redundancy audit")
    print("=" * 100)
    print()
    if best_global is None:
        print("  No hypothesis returned a valid optimization.")
        print("  Aleph removal cannot be replaced by direct entries (catastrophic).")
        return
    print(f"  Best result: {best_global['hypothesis']}")
    print(f"    α-spread: {best_global['alpha_spread']:.4e}")
    print(f"    Signature OK: {best_global['signature_ok']}")
    print(f"    α(proton)/α_target: {best_global['alpha_ratio_to_target']:.4f}")
    print()
    if (best_global['alpha_spread'] < 1e-9 and
            best_global['signature_ok'] and
            abs(best_global['alpha_ratio_to_target'] - 1) < 0.01):
        print("  → ALEPH IS REDUNDANT.  Direct sheet-time couplings can fully")
        print("    replace the aleph row.  MaSt's metric simplifies to 10D.")
    elif best_global['alpha_spread'] < 1e-9 and best_global['signature_ok']:
        print("  → Direct couplings preserve universality and signature, but")
        print(f"    α magnitude is off by ratio {best_global['alpha_ratio_to_target']:.4f}.")
        print("    Could potentially be tuned; structurally aleph may be replaceable.")
    elif best_global['signature_ok']:
        print(f"  → Direct couplings preserve signature, but α universality")
        print(f"    spread is {best_global['alpha_spread']:.2e} (not exact).")
        print("    Aleph appears to provide universality structurally.")
    else:
        print("  → No tested direct-coupling structure preserves both signature")
        print("    and α universality.  Aleph is structurally required.")


if __name__ == "__main__":
    main()
