"""
R64 Track 10 Phase 10a — σ_pS_ring as primary direct coupling.

Premise: Tracks 7–9 used σ_pS_tube (charge-channel) and found the metric
cannot deliver Phase 7c-class strong force at signature-permitted
magnitudes.  The user's structural argument: the strong force is
phenomenologically gravity-like (always attractive, charge-symmetric),
so its metric origin should be the *ring* (mass-channel), not the *tube*
(charge-channel).

This phase tests σ_pS_ring as the primary direct sheet-S coupling.
Methodology parallels Phase 7e + Phase 9b: sweep σ_pS_ring alone, check
α universality, search for companion prescriptions if it breaks, then
compute V(r) at any preserved-universality prescription.

Outputs:
  outputs/track10_phase10a_universality_sweep.csv
  outputs/track10_phase10a_potential_curves.csv
  outputs/track10_phase10a_potential_curves.png
"""

import os
import sys
import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
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


# R64 Point B (Phase 7c calibration)
EPS_P_R64_B = 0.2052
S_P_R64_B = 0.0250
K_P_R64_B = 63.629

A_KINETIC = 4.0 * HBAR_C_MEV_FM ** 2

M_P = 938.272
M_N = 939.565

CONFIGS_R64 = {
    "pp (R64)": dict(n_pt=6, n_pr=4, m_constituents_sum=2 * M_P),
    "pn (R64)": dict(n_pt=6, n_pr=0, m_constituents_sum=M_P + M_N),
    "nn (R64)": dict(n_pt=6, n_pr=-4, m_constituents_sum=2 * M_N),
}


def expected_alpha_sum_squared(tup):
    n_et, _, n_νt, _, n_pt, _ = tup
    return (n_et - n_pt + n_νt) ** 2


def build_aug_with_block(p, **entries):
    """Augment metric with sheet-S, aleph-S, σ_at offsets."""
    sigma_at_offset = entries.pop('sigma_at_offset', 0.0)
    p_modified = p.copy_with(sigma_at=p.sigma_at + sigma_at_offset)
    G = build_aug_metric(p_modified).copy()

    def add(idx_a, idx_b, value):
        if value:
            G[idx_a, idx_b] += value
            G[idx_b, idx_a] += value

    for s_idx in (I_SX, I_SY, I_SZ):
        add(I_P_TUBE, s_idx, entries.get('sigma_pS_tube', 0.0))
        add(I_P_RING, s_idx, entries.get('sigma_pS_ring', 0.0))
        add(I_E_TUBE, s_idx, entries.get('sigma_eS_tube', 0.0))
        add(I_E_RING, s_idx, entries.get('sigma_eS_ring', 0.0))
        add(I_NU_TUBE, s_idx, entries.get('sigma_νS_tube', 0.0))
        add(I_NU_RING, s_idx, entries.get('sigma_νS_ring', 0.0))
        add(I_ALEPH, s_idx, entries.get('sigma_aS', 0.0))
    return G


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


def schur_effective_sigma_pS_ring(G):
    """Effective (p_r, S_x) coupling from inverse metric."""
    G_inv = np.linalg.inv(G)
    g_pr = G[I_P_RING, I_P_RING]
    g_SS = G[I_SX, I_SX]
    return -G_inv[I_P_RING, I_SX] * g_pr * g_SS


def schur_effective_sigma_pS_tube(G):
    """Effective (p_t, S_x) coupling from inverse metric."""
    G_inv = np.linalg.inv(G)
    g_pp = G[I_P_TUBE, I_P_TUBE]
    g_SS = G[I_SX, I_SX]
    return -G_inv[I_P_TUBE, I_SX] * g_pp * g_SS


# ─── V(r) computation including BOTH n_pt and n_pr cross-couplings ─

def m_Ma(n_pt, n_pr, eps, s, K_p):
    return K_p * math.sqrt((n_pt / eps) ** 2 + (n_pr - s * n_pt) ** 2)


def m_compound_with_full_cross(r, n_pt, n_pr, sigma_eff_tube, sigma_eff_ring,
                                eps, s, K_p):
    """Mass with cross-couplings via both n_pt and n_pr."""
    if r < 1e-6:
        return float('inf')
    k_S = 1.0 / r
    m_ma = m_Ma(n_pt, n_pr, eps, s, K_p)
    cross = (2 * k_S * sigma_eff_tube * n_pt * HBAR_C_MEV_FM
             + 2 * k_S * sigma_eff_ring * n_pr * HBAR_C_MEV_FM)
    m2 = m_ma ** 2 + A_KINETIC * k_S ** 2 + cross
    if m2 <= 0:
        return float('nan')
    return math.sqrt(m2)


def compute_V_with_both_effective(p, sigma_eff_tube, sigma_eff_ring,
                                   n_pt, n_pr, m_constituents_sum,
                                   r_values):
    Vs = []
    for r in r_values:
        m = m_compound_with_full_cross(
            r, n_pt, n_pr, sigma_eff_tube, sigma_eff_ring,
            EPS_P_R64_B, S_P_R64_B, K_P_R64_B,
        )
        Vs.append(m - m_constituents_sum)
    return np.array(Vs)


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 10 Phase 10a — σ_pS_ring as primary direct coupling")
    print("=" * 100)
    print()

    p = track9_params()

    # ─── Part 1: σ_pS_ring alone — does it preserve α universality? ───
    print("=" * 80)
    print("Part 1 — σ_pS_ring alone (no companion)")
    print("=" * 80)
    print(f"  {'σ_pS_ring':>12s}  {'sig OK':>8s}  {'α-spread':>14s}")
    rows_p1 = []
    for sigma in [0.001, 0.005, 0.01, 0.025, 0.05, 0.10, 0.20]:
        G = build_aug_with_block(p, sigma_pS_ring=sigma)
        sig_ok = num_negative_eigs(G) == 1
        spread = alpha_spread(G) if sig_ok else float('nan')
        marker = "✓" if sig_ok else "✗"
        spread_str = f"{spread:.4e}" if not math.isnan(spread) else "(broken)"
        print(f"  {sigma:>+12.4f}  {marker:>8s}  {spread_str:>14s}")
        rows_p1.append({
            'sigma_pS_ring': sigma,
            'signature_ok': sig_ok,
            'alpha_spread': spread,
        })
    print()

    # ─── Part 2: search for compensation prescriptions ───
    print("=" * 80)
    print("Part 2 — Search for prescription that preserves α universality")
    print("=" * 80)
    print()
    print("  Hypotheses:")
    print("    R1: σ_aS = a · σ_pS_ring (aleph mediator)")
    print("    R2: σ_pS_tube = b · σ_pS_ring (cross-coupling on same sheet)")
    print("    R3: σ_aS = a · σ_pS_ring AND σ_pS_tube = b · σ_pS_ring")
    print()

    test_sigmas = [0.001, 0.005, 0.01, 0.025, 0.05]

    def cost_R1(coeffs, sigma_pS_ring, p):
        a, = coeffs
        G = build_aug_with_block(
            p, sigma_pS_ring=sigma_pS_ring,
            sigma_aS=a * sigma_pS_ring,
        )
        if num_negative_eigs(G) != 1:
            return 1.0
        return alpha_spread(G)

    def cost_R2(coeffs, sigma_pS_ring, p):
        b, = coeffs
        G = build_aug_with_block(
            p, sigma_pS_ring=sigma_pS_ring,
            sigma_pS_tube=b * sigma_pS_ring,
        )
        if num_negative_eigs(G) != 1:
            return 1.0
        return alpha_spread(G)

    def cost_R3(coeffs, sigma_pS_ring, p):
        a, b = coeffs
        G = build_aug_with_block(
            p, sigma_pS_ring=sigma_pS_ring,
            sigma_aS=a * sigma_pS_ring,
            sigma_pS_tube=b * sigma_pS_ring,
        )
        if num_negative_eigs(G) != 1:
            return 1.0
        return alpha_spread(G)

    HYPS = {
        "R1": (cost_R1, ['a'], np.array([0.0])),
        "R2": (cost_R2, ['b'], np.array([0.0])),
        "R3": (cost_R3, ['a', 'b'], np.array([0.0, 0.0])),
    }

    best_prescription = None
    best_spread = float('inf')

    for hyp_name, (cost_fn, params, x0) in HYPS.items():
        print(f"  --- {hyp_name}: " + " + ".join(params) + " ---")
        param_header = "  ".join(f"{n:>10s}" for n in params)
        print(f"    {'σ_pS_ring':>10s}  {param_header}  "
              f"{'α-spread':>12s}  verdict")
        coeffs_seen = []
        for sigma in test_sigmas:
            result = minimize(
                cost_fn, x0,
                args=(sigma, p),
                method='Nelder-Mead',
                options={'xatol': 1e-10, 'fatol': 1e-13, 'maxiter': 10000},
            )
            params_str = "  ".join(f"{v:+10.6f}" for v in result.x)
            verdict = ("exact" if result.fun < 1e-7 else
                       "good" if result.fun < 1e-3 else "fail")
            print(f"    {sigma:>+10.4f}  {params_str}  "
                  f"{result.fun:>12.4e}  {verdict}")
            coeffs_seen.append((sigma, result.x.copy(), result.fun))
            if result.fun < best_spread:
                best_spread = result.fun
                best_prescription = (hyp_name, params, result.x.copy(), sigma)
        # Report consistency
        if len(coeffs_seen) >= 3:
            for i, name in enumerate(params):
                vals = [c[1][i] for c in coeffs_seen]
                m = np.mean(vals)
                if abs(m) > 1e-6:
                    rel_var = (max(vals) - min(vals)) / abs(m)
                    cons = "consistent" if rel_var < 0.05 else "varies"
                    print(f"      {name}: mean = {m:+.6f}, rel-var = "
                          f"{rel_var:.2e}  [{cons}]")
        print()

    if best_prescription is None or best_spread > 1e-6:
        print("  → No tested hypothesis preserves α universality with σ_pS_ring.")
        print("  → Outcome D for Track 10: ring-channel direct coupling")
        print("    structurally cannot preserve α at any tested compensation.")
    else:
        hyp_name, params, coeffs, sigma = best_prescription
        print(f"  → Best prescription: {hyp_name} with coeffs " +
              ", ".join(f"{n}={v:+.4f}" for n, v in zip(params, coeffs)))
        print(f"    α-spread at σ_pS_ring={sigma}: {best_spread:.4e}")
    print()

    # ─── Part 3: V(r) at best prescription, three channels ───
    print("=" * 80)
    print("Part 3 — V(r) at best prescription (pp, pn, nn channels)")
    print("=" * 80)
    print()

    # Choose a representative sigma_pS_ring magnitude near band edge
    # Find signature band first, optimizing prescription at each step
    print("  Finding signature-OK band under best prescription...")
    sig_min = sig_max = 0.0
    if best_prescription is not None:
        hyp_name, params, ref_coeffs, _ = best_prescription
        cost_fn = HYPS[hyp_name][0]
        x0 = ref_coeffs.copy()
        # Sweep up
        for sigma in np.linspace(0.001, 2.0, 200):
            result = minimize(
                cost_fn, x0, args=(sigma, p),
                method='Nelder-Mead',
                options={'xatol': 1e-10, 'fatol': 1e-13, 'maxiter': 5000},
            )
            if result.fun < 1e-7:
                if hyp_name == "R1":
                    G = build_aug_with_block(p, sigma_pS_ring=sigma,
                                              sigma_aS=result.x[0] * sigma)
                elif hyp_name == "R2":
                    G = build_aug_with_block(p, sigma_pS_ring=sigma,
                                              sigma_pS_tube=result.x[0] * sigma)
                elif hyp_name == "R3":
                    G = build_aug_with_block(p, sigma_pS_ring=sigma,
                                              sigma_aS=result.x[0] * sigma,
                                              sigma_pS_tube=result.x[1] * sigma)
                if num_negative_eigs(G) == 1:
                    sig_max = sigma
                    x0 = result.x.copy()
                    continue
            break
        # Sweep down
        x0 = ref_coeffs.copy()
        for sigma in np.linspace(-0.001, -2.0, 200):
            result = minimize(
                cost_fn, x0, args=(sigma, p),
                method='Nelder-Mead',
                options={'xatol': 1e-10, 'fatol': 1e-13, 'maxiter': 5000},
            )
            if result.fun < 1e-7:
                if hyp_name == "R1":
                    G = build_aug_with_block(p, sigma_pS_ring=sigma,
                                              sigma_aS=result.x[0] * sigma)
                elif hyp_name == "R2":
                    G = build_aug_with_block(p, sigma_pS_ring=sigma,
                                              sigma_pS_tube=result.x[0] * sigma)
                elif hyp_name == "R3":
                    G = build_aug_with_block(p, sigma_pS_ring=sigma,
                                              sigma_aS=result.x[0] * sigma,
                                              sigma_pS_tube=result.x[1] * sigma)
                if num_negative_eigs(G) == 1:
                    sig_min = sigma
                    x0 = result.x.copy()
                    continue
            break

    print(f"  Signature-OK σ_pS_ring band under best prescription: "
          f"[{sig_min:+.4f}, {sig_max:+.4f}]")
    print()

    # Compute V(r) at boundaries and zero
    r_values = np.logspace(-1, 2, 400)
    csv_rows = []
    plot_data = []

    if best_prescription is not None and abs(sig_min) > 0.001 and sig_max > 0.001:
        hyp_name, params, ref_coeffs, _ = best_prescription
        cost_fn = HYPS[hyp_name][0]

        for sigma_ring in [sig_min * 0.9, 0.0, sig_max * 0.9]:
            if abs(sigma_ring) > 1e-6:
                result = minimize(
                    cost_fn, ref_coeffs.copy(),
                    args=(sigma_ring, p),
                    method='Nelder-Mead',
                    options={'xatol': 1e-10, 'fatol': 1e-13, 'maxiter': 10000},
                )
                if hyp_name == "R1":
                    sigma_aS = result.x[0] * sigma_ring
                    sigma_tube = 0.0
                    G = build_aug_with_block(p, sigma_pS_ring=sigma_ring,
                                              sigma_aS=sigma_aS)
                elif hyp_name == "R2":
                    sigma_aS = 0.0
                    sigma_tube = result.x[0] * sigma_ring
                    G = build_aug_with_block(p, sigma_pS_ring=sigma_ring,
                                              sigma_pS_tube=sigma_tube)
                elif hyp_name == "R3":
                    sigma_aS = result.x[0] * sigma_ring
                    sigma_tube = result.x[1] * sigma_ring
                    G = build_aug_with_block(p, sigma_pS_ring=sigma_ring,
                                              sigma_aS=sigma_aS,
                                              sigma_pS_tube=sigma_tube)
            else:
                G = build_aug_with_block(p)
                sigma_aS = 0.0
                sigma_tube = 0.0

            if num_negative_eigs(G) != 1:
                continue
            sigma_eff_tube = schur_effective_sigma_pS_tube(G)
            sigma_eff_ring = schur_effective_sigma_pS_ring(G)

            print(f"  σ_pS_ring = {sigma_ring:+.4f}, σ_aS = {sigma_aS:+.4f}, "
                  f"σ_pS_tube = {sigma_tube:+.4f}")
            print(f"    σ_eff_tube (Schur) = {sigma_eff_tube:+.4f}")
            print(f"    σ_eff_ring (Schur) = {sigma_eff_ring:+.4f}")
            print(f"    {'channel':<10s}  {'V_min (MeV)':>12s}  "
                  f"{'r_min (fm)':>10s}  {'V(∞) ≈ Ma offset':>16s}")
            for label, cfg in CONFIGS_R64.items():
                V = compute_V_with_both_effective(
                    p, sigma_eff_tube, sigma_eff_ring,
                    cfg['n_pt'], cfg['n_pr'],
                    cfg['m_constituents_sum'],
                    r_values,
                )
                mask = (r_values >= 0.3) & (r_values <= 50)
                V_phys = V[mask]
                r_phys = r_values[mask]
                idx = np.nanargmin(V_phys)
                V_min = V_phys[idx]
                r_min = r_phys[idx]
                Ma_offset = V[-1]   # at largest r
                print(f"    {label:<10s}  {V_min:>+12.3f}  "
                      f"{r_min:>+10.3f}  {Ma_offset:>+16.3f}")
                for r_i, V_i in zip(r_values, V):
                    csv_rows.append({
                        'sigma_pS_ring': sigma_ring,
                        'sigma_aS': sigma_aS,
                        'sigma_pS_tube': sigma_tube,
                        'sigma_eff_tube': sigma_eff_tube,
                        'sigma_eff_ring': sigma_eff_ring,
                        'config': label,
                        'r_fm': r_i,
                        'V_MeV': V_i,
                    })
                plot_data.append((sigma_ring, label, V))
            print()

    # ─── Plot ───
    fig, ax = plt.subplots(figsize=(10, 6))
    seen_sigmas = sorted(set(d[0] for d in plot_data))
    colors = {'pp (R64)': 'C0', 'pn (R64)': 'C1', 'nn (R64)': 'C2'}
    linestyles = {seen_sigmas[i]: ['-', '--', ':'][i] for i in range(min(3, len(seen_sigmas)))}
    for sigma, label, V in plot_data:
        color = colors.get(label, 'gray')
        ls = linestyles.get(sigma, '-')
        if abs(sigma) > 1e-6:
            ax.plot(r_values, V, color=color, linestyle=ls, linewidth=1.0,
                    label=f'{label}, σ={sigma:+.3f}')
        else:
            ax.plot(r_values, V, color=color, linestyle=ls, linewidth=1.0,
                    alpha=0.5,
                    label=f'{label}, σ=0')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xscale('log')
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('V(r) (MeV)')
    ax.set_title('Track 10a: V(r) under σ_pS_ring primary coupling')
    ax.set_xlim(0.3, 50)
    ax.set_ylim(-100, 100)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=7, loc='upper right')
    plt.tight_layout()
    fig_path = out_dir / "track10_phase10a_potential_curves.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {fig_path}")

    # CSVs
    csv_p1 = out_dir / "track10_phase10a_universality_sweep.csv"
    if rows_p1:
        with open(csv_p1, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(rows_p1[0].keys()))
            w.writeheader()
            for r in rows_p1:
                w.writerow(r)
        print(f"  CSV: {csv_p1}")
    csv_p3 = out_dir / "track10_phase10a_potential_curves.csv"
    if csv_rows:
        with open(csv_p3, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
            w.writeheader()
            for r in csv_rows:
                w.writerow(r)
        print(f"  CSV: {csv_p3}")

    # ─── Verdict ───
    print()
    print("=" * 100)
    print("VERDICT — Phase 10a: σ_pS_ring as primary direct coupling")
    print("=" * 100)
    print()

    # Check whether pp/pn/nn channels are charge-symmetric in V(r)
    if csv_rows:
        # Get V_min for each channel at the band boundary
        sigmas_seen = sorted(set(r['sigma_pS_ring'] for r in csv_rows))
        boundary_sigma = sigmas_seen[-1] if sigmas_seen else 0
        if abs(boundary_sigma) > 1e-6:
            channel_mins = {}
            for label in CONFIGS_R64:
                V_at_boundary = [r['V_MeV'] for r in csv_rows
                                  if r['sigma_pS_ring'] == boundary_sigma
                                  and r['config'] == label]
                r_at_boundary = [r['r_fm'] for r in csv_rows
                                  if r['sigma_pS_ring'] == boundary_sigma
                                  and r['config'] == label]
                if V_at_boundary:
                    physical_idx = [(i, v) for i, v in enumerate(V_at_boundary)
                                     if 0.3 < r_at_boundary[i] < 50
                                     and not math.isnan(v)]
                    if physical_idx:
                        idx, vmin = min(physical_idx, key=lambda x: x[1])
                        channel_mins[label] = (vmin, r_at_boundary[idx])

            if "pp (R64)" in channel_mins and "pn (R64)" in channel_mins \
                    and "nn (R64)" in channel_mins:
                vmin_pp, _ = channel_mins["pp (R64)"]
                vmin_pn, _ = channel_mins["pn (R64)"]
                vmin_nn, _ = channel_mins["nn (R64)"]
                print(f"  At σ_pS_ring = {boundary_sigma:+.4f} (band boundary):")
                print(f"    V_min(pp) = {vmin_pp:+.3f} MeV")
                print(f"    V_min(pn) = {vmin_pn:+.3f} MeV")
                print(f"    V_min(nn) = {vmin_nn:+.3f} MeV")
                print()
                # Charge symmetry: pp ≈ nn?
                if abs(vmin_pp - vmin_nn) < 5:
                    print("  Charge symmetry (pp ≈ nn): ✓")
                else:
                    print(f"  Charge symmetry (pp vs nn): ✗ "
                          f"(differ by {abs(vmin_pp - vmin_nn):.2f} MeV)")
                # Always-attractive across channels?
                all_attract = all(v < 0 for v in [vmin_pp, vmin_pn, vmin_nn])
                if all_attract:
                    print("  All-channels-attractive: ✓")
                else:
                    print(f"  All-channels-attractive: ✗ "
                          f"(some channels not attractive)")
                # pn binding present?
                if vmin_pn < -1:
                    print(f"  pn channel attractive: ✓ ({vmin_pn:+.2f} MeV)")
                else:
                    print(f"  pn channel attractive: ✗ ({vmin_pn:+.2f} MeV)")
                print()
                # Strong-force depth threshold
                deep_enough = all(abs(v) > 30 for v in [vmin_pp, vmin_pn, vmin_nn])
                if deep_enough:
                    print(f"  → Outcome A: ring-S coupling delivers strong force")
                    print(f"    in the metric at signature-OK magnitudes!")
                elif min(vmin_pp, vmin_pn, vmin_nn) < -5:
                    print(f"  → Outcome C: ring-S delivers attractive V(r) but")
                    print(f"    not at strong-force depth.  Metric channel")
                    print(f"    cannot reach Phase 7c-class binding.")
                else:
                    print(f"  → Outcome B: ring-S preserves α universality but")
                    print(f"    delivers only Ma-side offset, no strong-force")
                    print(f"    contribution from cross-coupling.")


if __name__ == "__main__":
    main()
