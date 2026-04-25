"""
R64 Track 7 Phase 7g — Re-run α-coupling test at R64 Point B with R64 inventory.

Phase 7e tested whether adding σ_pS_tube to R60 model-F's metric
preserves α-universality across the model-F inventory (proton at
(0,0,0,0,1,3), etc).  That's the right test for "model-F regression."

R64's frame is different:
  - Point B params: ε_p = 0.2052, s_p = 0.025
  - Proton on p-sheet at (3, +2)  (uud composite of (1, ±2) primitives)
  - Neutron on p-sheet at (3, −2) (udd composite)
  - Deuteron on p-sheet at (6, 0)
  - Mesons: still on e/ν sheets (R64 doesn't change those)

Phase 7g tests α-universality at R64's actual frame.

### Method

1. Build R60 metric with R64 Point B's (ε_p, s_p), preserving model-F's
   α-architecture (σ_ta, σ_at, σ_ra prescription).
2. Use R64's u/d compound tuples for baryons (proton, neutron, deuteron
   etc.) plus the same mesons as 7e.
3. Sweep σ_pS_tube; check signature, α/α₀ for each mode.
4. Compare with 7e's pattern: same coupling structure?  Different
   universality band?

### Caveats

- R64's bare α-sum at proton (3, +2) gives α/α₀ = 9, not 1.  This is
  expected — R64 needs a different α-attribution rule (pool item g).
  Phase 7g doesn't fix this; it tests the *coupling structure* at
  R64's tuples regardless of what the baseline α value is.
- For universality test: we compare α(σ) / α(0) ratios — that doesn't
  require α(0) = 1/137 exactly; only that the *relative* shifts are
  consistent across modes.

Outputs:
  outputs/track7_phase7g_R64_alpha_universality.csv
  outputs/track7_phase7g_R64_alpha_curves.png
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
    Params, build_metric_11, signature_ok, alpha_coulomb,
    mode_6_to_11, derive_L_ring,
    ALPHA, SQRT_ALPHA, FOUR_PI, M_E_MEV, M_P_MEV,
    I_ALEPH, I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING,
    I_NU_TUBE, I_NU_RING, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import (   # noqa: E402
    mode_alpha_sum, track9_params,
)


def build_metric_with_pS(p, sigma_pS_tube, sigma_pS_ring=0.0):
    G = build_aug_metric(p).copy()
    for s_idx in (I_SX, I_SY, I_SZ):
        G[I_P_TUBE, s_idx] += sigma_pS_tube
        G[s_idx, I_P_TUBE] += sigma_pS_tube
        if sigma_pS_ring != 0.0:
            G[I_P_RING, s_idx] += sigma_pS_ring
            G[s_idx, I_P_RING] += sigma_pS_ring
    return G


# ─── R64 Point B test modes ─────────────────────────────────────────

# R64's u/d picture: proton uud → (3, +2), neutron udd → (3, −2)
# Compounds (deuteron, NN pairs) follow additive composition.
# Mesons: keep R60 model-F tuples (e/ν sheets unchanged in R64).
R64_TEST_MODES = [
    # (label, 6-tuple)  notes
    ("electron",   (1, 2, 0, 0, 0, 0)),
    ("muon",       (1, 1, -2, -2, 0, 0)),
    ("R64 proton", (0, 0, 0, 0, 3, +2)),
    ("R64 neutron",(0, 0, 0, 0, 3, -2)),
    ("R64 deuteron",(0, 0, 0, 0, 6, 0)),
    ("R64 pp",     (0, 0, 0, 0, 6, +4)),
    ("R64 nn",     (0, 0, 0, 0, 6, -4)),
    ("π⁰",         (0, -1, -2, -2, 0, 0)),
    ("π±",         (-1, -1, -3, -3, 0, 0)),
    ("K±",         (-1, -6, -2, 2, 0, 1)),
    ("ρ",          (-1, 5, -2, 2, 0, 1)),
]


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 7 Phase 7g — α-coupling universality at R64 Point B")
    print("=" * 110)
    print()

    # ─── Set up R64 Point B in R60's metric framework ───────────────
    p_t9 = track9_params()  # Get model-F α-architecture defaults

    # Override with R64 Point B (ε_p, s_p); derive new L_ring_p so
    # the proton mode sits at m_p = 938.272 at R64's tuple (3, +2)
    EPS_P_R64 = 0.2052
    S_P_R64 = 0.0250
    L_ring_p_R64 = derive_L_ring(M_P_MEV, 3, 2, EPS_P_R64, S_P_R64, p_t9.k_p)

    p_r64 = p_t9.copy_with(
        eps_p=EPS_P_R64, s_p=S_P_R64,
        L_ring_p=L_ring_p_R64,
    )

    print(f"R64 Point B baseline (in R60 11D framework):")
    print(f"  ε_p = {p_r64.eps_p}, s_p = {p_r64.s_p}")
    print(f"  L_ring_p = {p_r64.L_ring_p:.4f} fm  (derived for m_p at (3,+2))")
    print(f"  k_p = {p_r64.k_p:.6f}  (model-F)")
    print(f"  σ_ta = √α = {p_r64.sigma_ta:.6f}")
    print(f"  σ_at = 4πα = {p_r64.sigma_at:.6f}")
    print()

    # ─── Sanity: baseline α at σ_pS = 0 ─────────────────────────────
    G_base = build_metric_with_pS(p_r64, 0.0, 0.0)
    sig_base = signature_ok(G_base)
    print(f"Baseline signature OK: {sig_base}")
    print()
    print(f"  {'mode':<14s}  {'tuple':<28s}  {'α_sum':>5s}  "
          f"{'expect α/α₀':>11s}  {'observed α/α₀':>14s}")
    print("─" * 90)
    for label, tup in R64_TEST_MODES:
        n11 = mode_6_to_11(tup)
        alpha = alpha_coulomb(G_base, n11)
        alpha_sum = mode_alpha_sum(tup)
        expect = alpha_sum * alpha_sum
        observed_ratio = alpha / ALPHA
        tup_str = str(tup).replace(" ", "")
        print(f"  {label:<14s}  {tup_str:<28s}  {alpha_sum:>+5d}  "
              f"{expect:>11d}  {observed_ratio:>14.6f}")
    print()

    # Note on R64 proton baseline:
    print("  (Note: R64's bare proton (3,+2) gives α/α₀ = 9 under the simple")
    print("   α-sum rule.  This is expected — R64 needs a different")
    print("   α-attribution rule [pool item g].  Phase 7g tests α/α(0)")
    print("   ratios — coupling structure independent of baseline value.)")
    print()

    # ─── Sweep σ_pS_tube ────────────────────────────────────────────
    print("=" * 70)
    print("Sweep σ_pS_tube (S-isotropic)")
    print("=" * 70)

    sigma_values = np.linspace(-0.5, 0.5, 401)
    sweep_data = []

    sig_band_low = None
    sig_band_high = None
    for sigma in sigma_values:
        G = build_metric_with_pS(p_r64, sigma, 0.0)
        sig = signature_ok(G)
        if sig and sig_band_low is None:
            sig_band_low = sigma
        if sig:
            sig_band_high = sigma
        ratios = {}
        for label, tup in R64_TEST_MODES:
            n11 = mode_6_to_11(tup)
            try:
                a = alpha_coulomb(G, n11)
                ratios[label] = a / ALPHA
            except Exception:
                ratios[label] = float('nan')
        sweep_data.append((sigma, sig, ratios))

    print(f"  Signature-OK σ_pS_tube range (R64 Point B): "
          f"[{sig_band_low:.4f}, {sig_band_high:.4f}]")
    print()

    # ─── Sample table at small σ ────────────────────────────────────
    sample_sigmas = [-0.05, -0.01, -0.005, -0.001, 0.0, 0.001, 0.005, 0.01, 0.05]
    sample_sigmas = [s for s in sample_sigmas
                     if sig_band_low is not None and
                     sig_band_low <= s <= sig_band_high]
    print(f"  α/α(σ=0) ratios across modes:")
    print()
    hdr_label = f"  {'mode':<14s}  "
    hdr_label += "  ".join(f"σ={s:+.3f}".ljust(10) for s in sample_sigmas)
    print(hdr_label)

    baseline_ratios = sweep_data[int(np.argmin(np.abs(sigma_values)))][2]

    for label, _ in R64_TEST_MODES:
        row = f"  {label:<14s}  "
        for s in sample_sigmas:
            idx = int(np.argmin(np.abs(sigma_values - s)))
            cur = sweep_data[idx][2].get(label, float('nan'))
            base = baseline_ratios.get(label, 1.0)
            ratio_to_base = cur / base if base != 0 and np.isfinite(base) else float('nan')
            row += f"{ratio_to_base:>10.6f}  "
        print(row)
    print()

    # ─── Universality metric ────────────────────────────────────────
    print("=" * 70)
    print("Max relative deviation across modes |α(σ)/α(0) − 1|")
    print("=" * 70)

    sigma_kept = []
    max_dev = []
    for sigma, sig, ratios in sweep_data:
        if not sig:
            continue
        devs = []
        for label, _ in R64_TEST_MODES:
            base = baseline_ratios[label]
            cur = ratios[label]
            if base != 0 and np.isfinite(base) and np.isfinite(cur):
                devs.append(abs(cur / base - 1.0))
        if devs:
            sigma_kept.append(sigma)
            max_dev.append(max(devs))

    sigma_kept = np.array(sigma_kept)
    max_dev = np.array(max_dev)

    for threshold in [1e-6, 1e-4, 1e-2]:
        mask = max_dev < threshold
        if np.any(mask):
            kept = sigma_kept[mask]
            print(f"  |Δα/α| < {threshold:.0e}: σ_pS_tube ∈ "
                  f"[{kept.min():+.5f}, {kept.max():+.5f}]")
        else:
            print(f"  |Δα/α| < {threshold:.0e}: empty")
    print()

    # ─── Compare with Phase 7e (model-F frame) bands ────────────────
    print("─" * 70)
    print("Phase 7e (model-F frame) bands for reference:")
    print("  signature OK:        [-0.0750, +0.0750]")
    print("  universality < 1%:   [-0.00250, +0.00250]")
    print("─" * 70)
    print()

    # ─── Verdict ────────────────────────────────────────────────────
    print("=" * 70)
    print("VERDICT — Phase 7g")
    print("=" * 70)

    # Compare ratios to 7e's pattern
    # Quantitative: at σ = ±0.05 in 7e, electron α/α₀ went to 1.166.
    # In 7g, find equivalent.
    idx_neg05 = int(np.argmin(np.abs(sigma_values - (-0.05))))
    idx_pos05 = int(np.argmin(np.abs(sigma_values - 0.05)))
    if (sweep_data[idx_neg05][1] and sweep_data[idx_pos05][1]):
        e_at_neg05 = sweep_data[idx_neg05][2].get('electron', float('nan'))
        e_base = baseline_ratios['electron']
        e_ratio = e_at_neg05 / e_base if e_base else float('nan')
        print(f"  Electron α/α(0) at σ=−0.05: {e_ratio:.4f}  "
              f"(7e: 1.166)")

        p_at_neg05 = sweep_data[idx_neg05][2].get('R64 proton', float('nan'))
        p_base = baseline_ratios['R64 proton']
        p_ratio = p_at_neg05 / p_base if p_base else float('nan')
        print(f"  R64 proton α/α(0) at σ=−0.05: {p_ratio:.4f}  "
              f"(7e proton (1,3): 0.565)")

    # Same pattern as 7e?
    if max_dev[np.argmin(np.abs(sigma_kept - 0))] < 1e-10:
        # baseline is universal
        same_pattern = True
        # check that σ ≠ 0 has deviation
        idx_test = int(np.argmin(np.abs(sigma_kept - 0.05)))
        if idx_test < len(max_dev) and max_dev[idx_test] > 0.01:
            print(f"\n  Same coupling pattern as Phase 7e (model-F frame):")
            print(f"  α-sectors are coupled at R64's frame too.")
            print(f"  σ_pS_tube must be tightly constrained at any baseline.")
        else:
            print(f"\n  Surprisingly small perturbation at σ=0.05 — different from 7e")
    else:
        print(f"\n  Different pattern from 7e — investigate further")

    # ─── Plot ───────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    ax = axes[0, 0]
    for label, _ in R64_TEST_MODES:
        sigmas_p = []
        ratios_p = []
        for sigma, sig, ratios in sweep_data:
            if sig and np.isfinite(ratios.get(label, np.nan)):
                base = baseline_ratios.get(label, 1.0)
                if base != 0:
                    sigmas_p.append(sigma)
                    ratios_p.append(ratios[label] / base)
        if sigmas_p:
            ax.plot(sigmas_p, ratios_p, label=label, linewidth=1.2)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.axhline(1, color='black', linewidth=0.5, linestyle=':')
    ax.set_xlabel('σ_pS_tube')
    ax.set_ylabel('α(mode) / α(σ=0)')
    ax.set_title('R64 Point B: α(mode) vs σ_pS_tube (relative to baseline)')
    ax.set_xlim(sig_band_low * 1.05 if sig_band_low else -0.5,
                sig_band_high * 1.05 if sig_band_high else 0.5)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=7, ncol=2)

    ax = axes[0, 1]
    if len(sigma_kept) > 0:
        ax.semilogy(sigma_kept, np.maximum(max_dev, 1e-16),
                    color='blue', linewidth=1.5, label='R64 Point B')
        ax.axhline(1e-6, color='green', linestyle='--', alpha=0.5)
        ax.axhline(1e-4, color='orange', linestyle='--', alpha=0.5)
        ax.axhline(1e-2, color='red', linestyle='--', alpha=0.5,
                   label='1% universality threshold')
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlabel('σ_pS_tube')
    ax.set_ylabel('max |α(σ)/α(0) − 1|')
    ax.set_title('Universality deviation (R64 frame)')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    ax = axes[1, 0]
    sig_array = np.array([1.0 if s[1] else 0.0 for s in sweep_data])
    ax.fill_between(sigma_values, 0, sig_array, alpha=0.4, color='green')
    ax.axvline(0, color='black', linewidth=0.5)
    if sig_band_low is not None:
        ax.axvline(sig_band_low, color='red', linestyle=':')
        ax.axvline(sig_band_high, color='red', linestyle=':')
    ax.set_xlabel('σ_pS_tube')
    ax.set_ylabel('signature OK')
    ax.set_title(f'Signature band (R64 Point B): '
                 f'[{sig_band_low:.4f}, {sig_band_high:.4f}]')
    ax.set_ylim(-0.1, 1.1)
    ax.grid(alpha=0.3)

    ax = axes[1, 1]
    ax.axis('off')
    summary = [
        ['Test', 'Phase 7g (R64 PB)', 'Phase 7e (model-F)'],
        ['Baseline frame', 'R64 (3,±2) tuples', 'model-F (1,3) tuple'],
        ['Signature band',
         f'[{sig_band_low:+.4f}, {sig_band_high:+.4f}]'
         if sig_band_low is not None else 'EMPTY',
         '[-0.0750, +0.0750]'],
    ]
    # Find universality bands
    for thr_label, thr in [('univ <10⁻⁶', 1e-6), ('univ <1%', 1e-2)]:
        mask = max_dev < thr
        if np.any(mask):
            kept = sigma_kept[mask]
            r64_rng = f'[{kept.min():+.4f}, {kept.max():+.4f}]'
        else:
            r64_rng = 'empty'
        modelf_rng = '[0, 0]' if thr_label == 'univ <10⁻⁶' else '[-0.0025, +0.0025]'
        summary.append([thr_label, r64_rng, modelf_rng])
    table = ax.table(cellText=summary, loc='center',
                     colWidths=[0.25, 0.40, 0.40])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.6)
    ax.set_title('Phase 7g vs Phase 7e summary')

    plt.tight_layout()
    fig_path = out_dir / "track7_phase7g_R64_alpha_curves.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print()
    print(f"  Plot: {fig_path}")

    # ─── CSV ────────────────────────────────────────────────────────
    csv_path = out_dir / "track7_phase7g_R64_alpha_universality.csv"
    fieldnames = ['sigma_pS_tube', 'signature_ok'] + \
                 [f'alpha_ratio_{label}' for label, _ in R64_TEST_MODES]
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for sigma, sig, ratios in sweep_data:
            row = {'sigma_pS_tube': sigma, 'signature_ok': int(sig)}
            for label, _ in R64_TEST_MODES:
                row[f'alpha_ratio_{label}'] = ratios.get(label, float('nan'))
            w.writerow(row)
    print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
