"""
R64 Track 8 Phase 8a — σ_aS sweep at fixed σ_at = 4πα.

Hub-and-spoke premise (Q135): all metric off-diagonals route through
aleph.  Phase 7c's empirical σ_pS_tube (direct p-sheet → S spatial)
bypasses aleph and was shown by Phase 7e to perturb α universality.

Phase 8a tests an aleph-mediated alternative: σ_aS at G[ℵ, S_x],
G[ℵ, S_y], G[ℵ, S_z] (S-isotropic), with σ_at held fixed at its
model-F value 4πα.  Question: can σ_aS take a non-zero value
without disturbing α universality?

Three outcomes possible:
  (A) α stays at baseline for σ_aS ≠ 0 in some range → sectors
      fully decoupled, hub-and-spoke confirmed for EM
  (B) α perturbed at all σ_aS ≠ 0 → proceed to Phase 8b
      (joint σ_aS, σ_at search for compensating constraint)
  (C) α stays at baseline only near σ_aS = 0, breaks at large
      σ_aS → strong-force-via-σ_aS hypothesis fails for simple form

Outputs:
  outputs/track8_phase8a_alpha_universality.csv
  outputs/track8_phase8a_alpha_curves.png
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
    Params, build_metric_11, signature_ok,
    alpha_coulomb, mode_6_to_11,
    ALPHA, SQRT_ALPHA, FOUR_PI, M_E_MEV, M_P_MEV,
    I_ALEPH, I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING,
    I_NU_TUBE, I_NU_RING, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import (   # noqa: E402
    mode_alpha_sum, track9_params,
)


def build_metric_with_aS(p, sigma_aS):
    """R60 model-F augmented metric plus (ℵ, S_*) cross-shears
    (S-isotropic).  σ_at stays at p.sigma_at (model-F value)."""
    G = build_aug_metric(p).copy()
    for s_idx in (I_SX, I_SY, I_SZ):
        G[I_ALEPH, s_idx] += sigma_aS
        G[s_idx, I_ALEPH] += sigma_aS
    return G


# Same 10-mode test inventory as Phase 7e
TEST_MODES = [
    ("electron", (1, 2, 0, 0, 0, 0)),
    ("muon",     (1, 1, -2, -2, 0, 0)),
    ("proton",   (0, 0, 0, 0, 1, 3)),
    ("neutron",  (0, -4, -1, 2, 0, -3)),
    ("Λ",        (-1, 2, -1, 2, -1, 3)),
    ("Σ⁻",       (-1, 2, -2, 2, -2, -2)),
    ("π⁰",       (0, -1, -2, -2, 0, 0)),
    ("π±",       (-1, -1, -3, -3, 0, 0)),
    ("K±",       (-1, -6, -2, 2, 0, 1)),
    ("ρ",        (-1, 5, -2, 2, 0, 1)),
]


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 8 Phase 8a — σ_aS sweep at fixed σ_at = 4πα")
    print("=" * 110)
    print()
    print("Hub-and-spoke test: does aleph-S coupling preserve α universality?")
    print()

    p = track9_params()
    print(f"Baseline params (R60 Track 9 model-F):")
    print(f"  ε_p = {p.eps_p}, s_p = {p.s_p}")
    print(f"  σ_ta = √α = {p.sigma_ta:.6f}")
    print(f"  σ_at = 4πα = {p.sigma_at:.6f}  (HELD FIXED)")
    print()

    # ─── Baseline at σ_aS = 0 ────────────────────────────────────────
    G_base = build_metric_with_aS(p, 0.0)
    sig_base = signature_ok(G_base)
    print(f"Baseline signature OK: {sig_base}")
    print()
    print(f"  {'mode':<10s}  {'tuple':<28s}  {'α_sum':>5s}  "
          f"{'expect α/α':>10s}  {'observed α/α':>13s}")
    for label, tup in TEST_MODES:
        n11 = mode_6_to_11(tup)
        alpha = alpha_coulomb(G_base, n11)
        alpha_sum = mode_alpha_sum(tup)
        expect = alpha_sum * alpha_sum
        observed_ratio = alpha / ALPHA
        tup_str = str(tup).replace(" ", "")
        print(f"  {label:<10s}  {tup_str:<28s}  {alpha_sum:>+5d}  "
              f"{expect:>10d}  {observed_ratio:>13.6f}")
    print()

    # ─── Sweep σ_aS ──────────────────────────────────────────────────
    print("=" * 70)
    print("Sweep σ_aS over wide range (σ_at fixed at 4πα)")
    print("=" * 70)

    sigma_values = np.linspace(-0.5, 0.5, 401)
    sweep_data = []

    sig_band_low = None
    sig_band_high = None
    for sigma in sigma_values:
        G = build_metric_with_aS(p, sigma)
        sig = signature_ok(G)
        if sig and sig_band_low is None:
            sig_band_low = sigma
        if sig:
            sig_band_high = sigma
        ratios = {}
        for label, tup in TEST_MODES:
            n11 = mode_6_to_11(tup)
            try:
                a = alpha_coulomb(G, n11)
                ratios[label] = a / ALPHA
            except Exception:
                ratios[label] = float('nan')
        sweep_data.append((sigma, sig, ratios))

    if sig_band_low is None:
        print("  NO signature-OK σ_aS values found in sweep range")
    else:
        print(f"  Signature-OK σ_aS range: [{sig_band_low:.4f}, {sig_band_high:.4f}]")
    print()

    # ─── Sample table ──────────────────────────────────────────────
    sample_sigmas = [-0.1, -0.05, -0.01, -0.001, 0.0, 0.001, 0.01, 0.05, 0.1]
    sample_sigmas = [s for s in sample_sigmas
                     if sig_band_low is not None and
                     sig_band_low <= s <= sig_band_high]

    print(f"  Sample α/α values across modes (σ_aS in signature band):")
    print()
    hdr = f"  {'mode':<10s}  "
    hdr += "  ".join(f"σ={s:+.3f}".ljust(11) for s in sample_sigmas)
    print(hdr)
    for label, _ in TEST_MODES:
        row = f"  {label:<10s}  "
        for s in sample_sigmas:
            idx = int(np.argmin(np.abs(sigma_values - s)))
            r = sweep_data[idx][2].get(label, float('nan'))
            row += f"{r:>11.6f}  "
        print(row)
    print()

    # ─── Universality metric ────────────────────────────────────────
    print("=" * 70)
    print("Universality deviation from baseline:")
    print("  max|α(σ)/α(0) − 1| across the 10 test modes")
    print("=" * 70)

    baseline_ratios = sweep_data[int(np.argmin(np.abs(sigma_values)))][2]

    sigma_kept = []
    max_dev = []
    for sigma, sig, ratios in sweep_data:
        if not sig:
            continue
        devs = []
        for label, _ in TEST_MODES:
            base = baseline_ratios[label]
            cur = ratios[label]
            if base != 0 and np.isfinite(base) and np.isfinite(cur):
                devs.append(abs(cur / base - 1.0))
        if devs:
            sigma_kept.append(sigma)
            max_dev.append(max(devs))

    sigma_kept = np.array(sigma_kept)
    max_dev = np.array(max_dev)

    for threshold in [1e-10, 1e-6, 1e-4, 1e-2]:
        mask = max_dev < threshold
        if np.any(mask):
            kept = sigma_kept[mask]
            print(f"  |Δα/α| < {threshold:.0e}: σ_aS ∈ "
                  f"[{kept.min():+.5f}, {kept.max():+.5f}]")
        else:
            print(f"  |Δα/α| < {threshold:.0e}: empty")
    print()

    # ─── Verdict ───────────────────────────────────────────────────
    print("=" * 70)
    print("VERDICT — Phase 8a")
    print("=" * 70)
    print()

    # Compare to Phase 7e (σ_pS_tube): 1% band was [-0.0025, +0.0025]
    print("Reference: Phase 7e σ_pS_tube 1% band was [-0.0025, +0.0025]")
    print()

    # Strict decoupling: |Δα| < 1e-10 at any σ_aS ≠ 0?
    decoupled = False
    threshold_test = 1e-10
    for sigma in sigma_kept[(np.abs(sigma_kept) > 0.001) & (np.abs(sigma_kept) < 0.1)]:
        idx = np.argmin(np.abs(sigma_kept - sigma))
        if max_dev[idx] < threshold_test:
            decoupled = True
            break

    if decoupled:
        print(f"  → σ_aS DECOUPLED from α at numerical noise level.")
        print(f"    Hub-and-spoke principle CONFIRMED for EM sector.")
        print(f"    σ_aS can be added to model-G without disturbing α.")
        print()
        print(f"    Skip Phase 8b; proceed directly to Phase 8c (V(r) computation).")
    else:
        # Compare bands to 7e
        mask_1pct = max_dev < 1e-2
        if np.any(mask_1pct):
            kept = sigma_kept[mask_1pct]
            print(f"  → σ_aS COUPLES to α at fixed σ_at.")
            print(f"    1% universality band: [{kept.min():+.5f}, {kept.max():+.5f}]")
            print(f"    Phase 7e reference (σ_pS_tube): [-0.0025, +0.0025]")
            ratio = (kept.max() - kept.min()) / 0.005
            print(f"    8a band is {ratio:.2f}× the 7e band.")
        else:
            print(f"  → σ_aS strongly perturbs α at any non-zero value.")
            print(f"    No 1% universality band found.")
        print()
        print(f"    → Proceed to Phase 8b: joint (σ_aS, σ_at) sweep to find")
        print(f"      compensating constraint.")

    # ─── Plot ──────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. α/α(0) per mode vs σ_aS
    ax = axes[0, 0]
    for label, _ in TEST_MODES:
        sigmas_p = []
        ratios_p = []
        for sigma, sig, ratios in sweep_data:
            if sig and np.isfinite(ratios.get(label, np.nan)):
                base = baseline_ratios.get(label, 1.0)
                if base != 0:
                    sigmas_p.append(sigma)
                    ratios_p.append(ratios[label] / base)
        ax.plot(sigmas_p, ratios_p, label=label, linewidth=1.2)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.axhline(1, color='black', linewidth=0.5, linestyle=':')
    ax.set_xlabel('σ_aS')
    ax.set_ylabel('α(mode) / α(σ=0)')
    ax.set_title('α(mode) vs σ_aS  (σ_at = 4πα fixed)')
    ax.set_xlim(sig_band_low * 1.05 if sig_band_low else -0.5,
                sig_band_high * 1.05 if sig_band_high else 0.5)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=7, ncol=2)

    # 2. Max universality deviation
    ax = axes[0, 1]
    if len(sigma_kept) > 0:
        ax.semilogy(sigma_kept, np.maximum(max_dev, 1e-16),
                    color='blue', linewidth=1.5, label='Phase 8a (σ_aS)')
        ax.axhline(1e-10, color='gray', linestyle='--', alpha=0.5,
                   label='ε = 10⁻¹⁰ (decoupled)')
        ax.axhline(1e-6, color='green', linestyle='--', alpha=0.5,
                   label='ε = 10⁻⁶')
        ax.axhline(1e-4, color='orange', linestyle='--', alpha=0.5,
                   label='ε = 10⁻⁴')
        ax.axhline(1e-2, color='red', linestyle='--', alpha=0.5,
                   label='ε = 10⁻² (1%)')
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlabel('σ_aS')
    ax.set_ylabel('max |α(σ)/α(0) − 1|')
    ax.set_title('Universality deviation')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # 3. Signature band
    ax = axes[1, 0]
    sig_array = np.array([1.0 if s[1] else 0.0 for s in sweep_data])
    ax.fill_between(sigma_values, 0, sig_array, alpha=0.4, color='green',
                    label='signature OK')
    ax.axvline(0, color='black', linewidth=0.5)
    if sig_band_low is not None:
        ax.axvline(sig_band_low, color='red', linestyle=':',
                   label=f'low: {sig_band_low:.3f}')
        ax.axvline(sig_band_high, color='red', linestyle=':',
                   label=f'high: {sig_band_high:.3f}')
    ax.set_xlabel('σ_aS')
    ax.set_ylabel('signature OK')
    ax.set_title('Signature preservation')
    ax.set_ylim(-0.1, 1.1)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # 4. Summary
    ax = axes[1, 1]
    ax.axis('off')
    summary = [
        ['Test', 'Phase 8a (σ_aS)', 'Phase 7e ref (σ_pS_tube)'],
        ['Signature band',
         f'[{sig_band_low:+.4f}, {sig_band_high:+.4f}]'
         if sig_band_low is not None else 'EMPTY',
         '[−0.0750, +0.0750]'],
    ]
    for thr_label, thr in [('univ <10⁻¹⁰', 1e-10),
                            ('univ <10⁻⁶', 1e-6),
                            ('univ <1%', 1e-2)]:
        mask = max_dev < thr
        if np.any(mask):
            kept = sigma_kept[mask]
            cur_rng = f'[{kept.min():+.4f}, {kept.max():+.4f}]'
        else:
            cur_rng = 'empty'
        if thr_label == 'univ <10⁻¹⁰':
            ref_rng = '{0}'
        elif thr_label == 'univ <10⁻⁶':
            ref_rng = '{0}'
        else:
            ref_rng = '[−0.0025, +0.0025]'
        summary.append([thr_label, cur_rng, ref_rng])

    table = ax.table(cellText=summary, loc='center',
                     colWidths=[0.20, 0.40, 0.40])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.6)
    ax.set_title('Phase 8a vs Phase 7e summary')

    plt.tight_layout()
    fig_path = out_dir / "track8_phase8a_alpha_curves.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print()
    print(f"  Plot: {fig_path}")

    # ─── CSV ──────────────────────────────────────────────────────
    csv_path = out_dir / "track8_phase8a_alpha_universality.csv"
    fieldnames = ['sigma_aS', 'signature_ok'] + \
                 [f'alpha_ratio_{label}' for label, _ in TEST_MODES]
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for sigma, sig, ratios in sweep_data:
            row = {'sigma_aS': sigma, 'signature_ok': int(sig)}
            for label, _ in TEST_MODES:
                row[f'alpha_ratio_{label}'] = ratios.get(label, float('nan'))
            w.writerow(row)
    print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
