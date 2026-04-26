"""
R64 Track 9 Phase 9c — V(r) at the prescribed σ_pS_tube + σ_aS pair.

Phase 9a/9b found that σ_aS = -1.819 · σ_pS_tube preserves α universality
to machine precision (H2 hypothesis succeeded; H5 also succeeded with a
3-sheet symmetric form).

Phase 9c uses the H2 prescription, sweeps σ_pS_tube within its
signature-OK range, and computes V(r) for the pn channel at R64 Point B
(matching Phase 7c's calibration) using the corrected two-body kinematic
prefactor 4·(ℏc)² (Phase 8c convention).

Question: does the prescribed (σ_pS_tube, σ_aS) pair deliver a strong-
force trough at intermediate r?  If yes (depth ~50 MeV at r ~1 fm at
some σ_pS_tube within the signature band), Outcome A — strong force
emerges from the metric via this prescription.  If only at unphysical
magnitudes, Outcome B.  If signature breaks before reaching strong-
force depth, Outcome A is partially blocked.

Outputs:
  outputs/track9_phase9c_potential_curves.csv
  outputs/track9_phase9c_potential_curves.png
"""

import os
import sys
import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


R60_SCRIPTS = Path(__file__).resolve().parent.parent.parent / "R60-metric-11" / "scripts"
sys.path.insert(0, str(R60_SCRIPTS))

from track1_solver import (    # noqa: E402
    Params, num_negative_eigs,
    ALPHA, SQRT_ALPHA, FOUR_PI, HBAR_C_MEV_FM,
    I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING,
    I_NU_TUBE, I_NU_RING,
    I_ALEPH, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import track9_params    # noqa: E402


# ─── H2 prescription coefficient from Phase 9b ─────────────────────

H2_COEFF_SIGMA_AS = -1.818920    # σ_aS = COEFF · σ_pS_tube preserves α


# ─── R64 Point B p-sheet calibration (Phase 7c) ────────────────────

EPS_P_R64_B = 0.2052
S_P_R64_B = 0.0250
K_P_R64_B = 63.629


# ─── Constants ─────────────────────────────────────────────────────

A_KINETIC = 4.0 * HBAR_C_MEV_FM ** 2     # two-body relative motion

M_P = 938.272
M_N = 939.565

CONFIGS_R64 = {
    "pp (R64)": dict(n_pt=6, n_pr=4, m_constituents_sum=2 * M_P),
    "pn (R64)": dict(n_pt=6, n_pr=0, m_constituents_sum=M_P + M_N),
    "nn (R64)": dict(n_pt=6, n_pr=-4, m_constituents_sum=2 * M_N),
}


# ─── Augmented metric with H2 prescription ─────────────────────────

def build_metric_at_prescription(p, sigma_pS_tube):
    """Augmented metric: σ_pS_tube direct + σ_aS = H2_COEFF · σ_pS_tube."""
    sigma_aS = H2_COEFF_SIGMA_AS * sigma_pS_tube
    G = build_aug_metric(p).copy()
    for s_idx in (I_SX, I_SY, I_SZ):
        # Direct p-tube ↔ S spatial
        G[I_P_TUBE, s_idx] += sigma_pS_tube
        G[s_idx, I_P_TUBE] += sigma_pS_tube
        # Aleph ↔ S spatial (the universality-preserving companion)
        G[I_ALEPH, s_idx] += sigma_aS
        G[s_idx, I_ALEPH] += sigma_aS
    return G


def schur_effective_sigma_pS(G):
    """Extract the effective (p_t, S_x) coupling from inverse metric.

    σ_eff = -G⁻¹[p_t, S_x] · G[p_t, p_t] · G[S_x, S_x]
    matches Phase 7c's σ_t convention.
    """
    G_inv = np.linalg.inv(G)
    g_pp = G[I_P_TUBE, I_P_TUBE]
    g_SS = G[I_SX, I_SX]
    return -G_inv[I_P_TUBE, I_SX] * g_pp * g_SS


# ─── 7c-style V(r) with corrected two-body kinematics ──────────────

def mu2_Ma_p_sheet(n_pt, n_pr, eps, s):
    return (n_pt / eps) ** 2 + (n_pr - s * n_pt) ** 2


def m_Ma(n_pt, n_pr, eps, s, K_p):
    return K_p * math.sqrt(mu2_Ma_p_sheet(n_pt, n_pr, eps, s))


def m_compound(r, n_pt, n_pr, sigma_eff, eps, s, K_p):
    """7c formula: m²(k_S) = m_Ma² + 4·(ℏc)²·k_S² + 2·k_S·σ_eff·n_pt·ℏc."""
    if r < 1e-6:
        return float('inf')
    k_S = 1.0 / r
    m_ma = m_Ma(n_pt, n_pr, eps, s, K_p)
    m2 = (m_ma ** 2 + A_KINETIC * k_S ** 2
          + 2 * k_S * sigma_eff * n_pt * HBAR_C_MEV_FM)
    if m2 <= 0:
        return float('nan')
    return math.sqrt(m2)


def compute_V_of_r(p, sigma_pS_tube, n_pt, n_pr, m_constituents_sum,
                   r_values):
    """V(r) at the H2 prescription, using R64 Point B p-sheet."""
    G = build_metric_at_prescription(p, sigma_pS_tube)
    if num_negative_eigs(G) != 1:
        return None, None
    sigma_eff = schur_effective_sigma_pS(G)
    Vs = []
    for r in r_values:
        m = m_compound(r, n_pt, n_pr, sigma_eff,
                       EPS_P_R64_B, S_P_R64_B, K_P_R64_B)
        Vs.append(m - m_constituents_sum)
    return np.array(Vs), sigma_eff


# ─── Signature band exploration ────────────────────────────────────

def find_signature_band(p, sigma_max=2.0, n_steps=200):
    """Find the σ_pS_tube range over which signature stays Lorentzian."""
    sigmas = np.linspace(-sigma_max, sigma_max, n_steps)
    band = []
    for s in sigmas:
        G = build_metric_at_prescription(p, s)
        if num_negative_eigs(G) == 1:
            band.append(s)
    if not band:
        return None, None
    return min(band), max(band)


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 9 Phase 9c — V(r) at H2 prescription")
    print("=" * 100)
    print()
    print(f"  H2 prescription: σ_aS = {H2_COEFF_SIGMA_AS} · σ_pS_tube")
    print(f"  R64 Point B: ε_p = {EPS_P_R64_B}, s_p = {S_P_R64_B}, "
          f"K_p = {K_P_R64_B}")
    print(f"  Two-body kinematic prefactor: 4·(ℏc)² (Phase 7c convention)")
    print()

    p = track9_params()

    # ─── Find signature band ───
    print("=" * 80)
    print("Part 1 — Signature band under H2 prescription")
    print("=" * 80)
    print()
    sig_min, sig_max = find_signature_band(p)
    print(f"  Signature-OK range for σ_pS_tube: "
          f"[{sig_min:+.4f}, {sig_max:+.4f}]")
    if sig_min is None:
        print("  Signature broken everywhere; H2 prescription cannot be used.")
        return
    print(f"  Compare to Phase 7e's σ_pS_tube-alone band: [-0.075, +0.075]")
    if abs(sig_max) > 0.075:
        print(f"  → Hub-and-spoke companion EXTENDS the signature-OK range")
        print(f"    by factor {abs(sig_max)/0.075:.2f}× over σ_pS_tube alone.")
    print()

    # ─── Schur σ_eff and V(r) at signature band points ───
    test_sigmas = []
    if sig_min < -0.001:
        test_sigmas.extend([sig_min * 0.95, sig_min * 0.5, sig_min * 0.1])
    test_sigmas.append(0.0)
    if sig_max > 0.001:
        test_sigmas.extend([sig_max * 0.1, sig_max * 0.5, sig_max * 0.95])

    print("=" * 80)
    print("Part 2 — Schur-effective σ_eff and V(r) trough on the prescription")
    print("=" * 80)
    print()
    print(f"  {'σ_pS':>8s}  {'σ_aS':>8s}  {'σ_eff':>10s}  "
          f"{'pn V_min':>10s}  {'r_min':>8s}  {'pp V_min':>10s}  "
          f"{'nn V_min':>10s}")
    print("  " + "─" * 84)

    r_values = np.logspace(-1, 2, 400)  # 0.1 to 100 fm

    csv_rows = []
    for sigma in test_sigmas:
        sigma_aS = H2_COEFF_SIGMA_AS * sigma
        G = build_metric_at_prescription(p, sigma)
        if num_negative_eigs(G) != 1:
            print(f"  {sigma:>+8.4f}  signature broken")
            continue
        sigma_eff = schur_effective_sigma_pS(G)

        results = {}
        for label, cfg in CONFIGS_R64.items():
            V, _ = compute_V_of_r(
                p, sigma,
                cfg['n_pt'], cfg['n_pr'],
                cfg['m_constituents_sum'],
                r_values,
            )
            if V is None:
                results[label] = (float('nan'), float('nan'))
                continue
            mask = (r_values >= 0.3) & (r_values <= 50)
            V_phys = V[mask]
            r_phys = r_values[mask]
            if np.any(np.isfinite(V_phys)):
                idx = np.nanargmin(V_phys)
                results[label] = (V_phys[idx], r_phys[idx])
            else:
                results[label] = (float('nan'), float('nan'))

            for r_i, V_i in zip(r_values, V):
                csv_rows.append({
                    'sigma_pS_tube': sigma,
                    'sigma_aS': sigma_aS,
                    'sigma_eff': sigma_eff,
                    'config': label,
                    'r_fm': r_i,
                    'V_MeV': V_i,
                })

        pn_V, pn_r = results.get("pn (R64)", (float('nan'), float('nan')))
        pp_V, pp_r = results.get("pp (R64)", (float('nan'), float('nan')))
        nn_V, nn_r = results.get("nn (R64)", (float('nan'), float('nan')))
        print(f"  {sigma:>+8.4f}  {sigma_aS:>+8.4f}  {sigma_eff:>+10.4f}  "
              f"{pn_V:>+10.3f}  {pn_r:>+8.3f}  {pp_V:>+10.3f}  {nn_V:>+10.3f}")

    print()

    # ─── Compare to Phase 7c reference ───
    print("=" * 80)
    print("Part 3 — Comparison to Phase 7c (direct σ_pS_tube without companion)")
    print("=" * 80)
    print()
    print(f"  Phase 7c (no α-preservation, broke universality):")
    print(f"    σ_t = -116.1 (7-tensor units), pn trough at r=1.135 fm, "
          f"depth -50.2 MeV.")
    print()

    # Find σ_pS_tube on prescription that matches 7c trough
    sigma_eff_target = -116.1  # In the dimensionless 7-tensor convention
    print(f"  At what σ_pS_tube (under H2 prescription) does σ_eff reach "
          f"Phase 7c's −116?")
    for s_test in np.linspace(sig_min * 0.95, sig_max * 0.95, 25):
        G = build_metric_at_prescription(p, s_test)
        if num_negative_eigs(G) != 1:
            continue
        s_eff = schur_effective_sigma_pS(G)
        if abs(s_eff) > 50:  # close to 7c magnitude
            cfg = CONFIGS_R64["pn (R64)"]
            V, _ = compute_V_of_r(
                p, s_test,
                cfg['n_pt'], cfg['n_pr'],
                cfg['m_constituents_sum'],
                r_values,
            )
            mask = (r_values >= 0.3) & (r_values <= 5)
            V_phys = V[mask]
            r_phys = r_values[mask]
            idx = np.nanargmin(V_phys)
            print(f"    σ_pS = {s_test:+.4f}  →  σ_eff = {s_eff:+.2f}  "
                  f"pn V_min = {V_phys[idx]:+.2f} MeV at r = "
                  f"{r_phys[idx]:.3f} fm")

    print()

    # ─── Plot ───
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    plot_sigmas = test_sigmas
    for sigma in plot_sigmas:
        if abs(sigma) < 1e-6:
            continue
        cfg = CONFIGS_R64["pn (R64)"]
        V, _ = compute_V_of_r(
            p, sigma,
            cfg['n_pt'], cfg['n_pr'],
            cfg['m_constituents_sum'],
            r_values,
        )
        if V is not None:
            ax.plot(r_values, V, label=f'σ_pS = {sigma:+.3f}', linewidth=1.0)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('V_pn(r) (MeV)')
    ax.set_title('V_pn(r) along H2 prescription (R64 Point B)')
    ax.set_xscale('log')
    ax.set_xlim(0.3, 100)
    ax.set_ylim(-100, 200)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc='upper right')

    # Trough depth vs σ_pS_tube
    ax = axes[1]
    sigma_sweep = np.linspace(sig_min * 0.95, sig_max * 0.95, 50)
    sigma_effs = []
    pn_depths = []
    pn_positions = []
    for sigma in sigma_sweep:
        G = build_metric_at_prescription(p, sigma)
        if num_negative_eigs(G) != 1:
            sigma_effs.append(np.nan)
            pn_depths.append(np.nan)
            pn_positions.append(np.nan)
            continue
        s_eff = schur_effective_sigma_pS(G)
        sigma_effs.append(s_eff)
        cfg = CONFIGS_R64["pn (R64)"]
        V, _ = compute_V_of_r(
            p, sigma,
            cfg['n_pt'], cfg['n_pr'],
            cfg['m_constituents_sum'],
            r_values,
        )
        if V is None:
            pn_depths.append(np.nan)
            pn_positions.append(np.nan)
            continue
        mask = (r_values >= 0.3) & (r_values <= 50)
        V_phys = V[mask]
        r_phys = r_values[mask]
        if np.any(np.isfinite(V_phys)):
            idx = np.nanargmin(V_phys)
            pn_depths.append(V_phys[idx])
            pn_positions.append(r_phys[idx])
        else:
            pn_depths.append(np.nan)
            pn_positions.append(np.nan)

    ax2 = ax.twinx()
    line1 = ax.plot(sigma_sweep, pn_depths, 'b-',
                    linewidth=1.5, label='V_min (MeV)')
    line2 = ax2.plot(sigma_sweep, pn_positions, 'r--',
                     linewidth=1.5, label='r_min (fm)')
    ax.set_xlabel('σ_pS_tube')
    ax.set_ylabel('V_min (MeV)', color='blue')
    ax2.set_ylabel('r_min (fm)', color='red')
    ax.set_title('Trough depth/position along H2 prescription (pn)')
    ax.grid(alpha=0.3)
    ax.axhline(-50, color='blue', linestyle=':', alpha=0.5)
    ax2.axhline(1.0, color='red', linestyle=':', alpha=0.5)
    lines = line1 + line2
    labs = [l.get_label() for l in lines]
    ax.legend(lines, labs, fontsize=9, loc='upper right')

    plt.tight_layout()
    fig_path = out_dir / "track9_phase9c_potential_curves.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {fig_path}")

    csv_path = out_dir / "track9_phase9c_potential_curves.csv"
    if csv_rows:
        with open(csv_path, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
            w.writeheader()
            for r in csv_rows:
                w.writerow(r)
        print(f"  CSV: {csv_path}")

    # ─── Verdict ───
    print()
    print("=" * 100)
    print("VERDICT — Phase 9c at H2 prescription")
    print("=" * 100)
    print()
    finite_depths = [d for d in pn_depths if np.isfinite(d)]
    finite_positions = [r for r, d in zip(pn_positions, pn_depths)
                        if np.isfinite(d) and np.isfinite(r)]
    if finite_depths:
        deepest = min(finite_depths)
        idx = pn_depths.index(deepest)
        deepest_r = pn_positions[idx]
        deepest_sigma = sigma_sweep[idx]
        deepest_eff = sigma_effs[idx]

        print(f"  Deepest pn trough on prescription:")
        print(f"    σ_pS_tube = {deepest_sigma:+.4f}")
        print(f"    σ_eff (Schur) = {deepest_eff:+.4f}")
        print(f"    depth = {deepest:+.3f} MeV at r = {deepest_r:.3f} fm")
        print(f"  Phase 7c reference: depth -50.2 MeV at r = 1.135 fm")
        print()
        if abs(deepest) > 30 and 0.5 < deepest_r < 2.0:
            print(f"  → Outcome A: STRONG-FORCE TROUGH EMERGES from the metric")
            print(f"    via H2 prescription.  Direct sheet-S coupling, with")
            print(f"    σ_aS = {H2_COEFF_SIGMA_AS} · σ_pS_tube companion, ")
            print(f"    delivers Phase 7c-magnitude depth at physical r.")
            print(f"    The strong force lives in the metric.")
        elif abs(deepest) > 5:
            print(f"  → Outcome B: prescription works, but trough magnitude")
            print(f"    is below Phase 7c's strong-force scale.  Maximum")
            print(f"    achievable is {deepest:.1f} MeV vs needed −50 MeV.")
            print(f"    Either signature breaks before reaching strong scale,")
            print(f"    or the Schur-effective σ_eff plateaus.")
        else:
            print(f"  → Outcome B/C: prescription preserves α but the trough")
            print(f"    is too shallow.  Within physically permitted σ_pS_tube,")
            print(f"    the trough doesn't reach Phase 7c's strong-force depth.")
            print(f"    Strong force may need additional structure beyond")
            print(f"    H2 prescription.")


if __name__ == "__main__":
    main()
