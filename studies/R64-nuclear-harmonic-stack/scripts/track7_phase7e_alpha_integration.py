"""
R64 Track 7 Phase 7e — α-coupling integration test.

Phase 7c introduced a new metric off-diagonal at (p_t, S_x), (p_t, S_y),
(p_t, S_z) — call it σ_pS_tube — to deliver the strong-force trough.
R60's α-architecture lives in the ℵ row (σ_ta tube↔ℵ, σ_at ℵ↔t,
σ_ra ring↔ℵ derived).  These are different metric entries.  But when
the 11×11 is solved/diagonalized, eigenmodes mix.  Question: does
adding σ_pS_tube disturb R60's α-extraction?

Method:
  - Augment R60's model-F baseline metric with σ_pS_tube at the new
    (p_t, S) entries (S-isotropic: same value at G[1,7], G[1,8], G[1,9]).
  - Optional: also test σ_pS_ring at (p_r, S_*).  Phase 7c forces
    σ_pS_ring = 0 by charge-independence, but we sweep it for
    completeness.
  - Sweep σ_pS_tube over a wide range; detect signature-OK band.
  - Within the band, compute α_Coulomb(mode) for several model-F
    inventory modes (electron, muon, proton, π⁰, etc.).
  - Universality check: does α/α_baseline stay equal to 1 across all
    modes for any σ_pS_tube ≠ 0?

Acceptance criteria:
  (1) Signature stays Lorentzian for σ_pS_tube ≠ 0       (required)
  (2) α stays at baseline value for σ_pS_tube ≠ 0        (PASS = decoupled)
  (3) α-universality across modes survives               (no model-F regression)

If (1)/(2)/(3) all pass: greenlight model-G integration with σ_pS_tube
as a free knob.  If they fail: derive constraint σ_pS_tube = f(...) that
preserves universality.

Outputs:
  outputs/track7_phase7e_alpha_universality.csv
  outputs/track7_phase7e_alpha_curves.png
"""

import os
import sys
import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# Wire in R60's Track 1 + Track 7b infrastructure
R60_SCRIPTS = Path(__file__).resolve().parent.parent.parent / "R60-metric-11" / "scripts"
sys.path.insert(0, str(R60_SCRIPTS))

from track1_solver import (    # noqa: E402
    Params, build_metric_11, signature_ok, num_negative_eigs,
    alpha_coulomb, mode_6_to_11, L_vector_from_params, mode_energy,
    ALPHA, SQRT_ALPHA, FOUR_PI, M_E_MEV, M_P_MEV,
    I_ALEPH, I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING,
    I_NU_TUBE, I_NU_RING, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import (   # noqa: E402
    MODEL_E_INVENTORY, mode_alpha_sum, track9_params,
)


# ─── Augment R60 model-F metric with σ_pS_tube ──────────────────────────

def build_metric_with_pS(p: Params, sigma_pS_tube: float,
                          sigma_pS_ring: float = 0.0) -> np.ndarray:
    """R60 model-F baseline metric (with ring↔ℵ via σ_ra) plus the new
    (p_t, S) and optionally (p_r, S) off-diagonals."""
    G = build_aug_metric(p).copy()
    for s_idx in (I_SX, I_SY, I_SZ):
        G[I_P_TUBE, s_idx] += sigma_pS_tube
        G[s_idx, I_P_TUBE] += sigma_pS_tube
        if sigma_pS_ring != 0.0:
            G[I_P_RING, s_idx] += sigma_pS_ring
            G[s_idx, I_P_RING] += sigma_pS_ring
    return G


# ─── Test modes — sample of model-F inventory ───────────────────────────

# Use modes spanning Q = ±1, 0 and the active-sheet taxonomy.  All
# computed via the bare rule's α/α = (n_et − n_pt + n_νt)².
TEST_MODES = [
    # (label, model-F 6-tuple)
    ("electron", (1, 2, 0, 0, 0, 0)),
    ("muon",     (1, 1, -2, -2, 0, 0)),
    ("proton",   (0, 0, 0, 0, 1, 3)),     # bare model-F (1,3)
    ("neutron",  (0, -4, -1, 2, 0, -3)),
    ("Λ",        (-1, 2, -1, 2, -1, 3)),
    ("Σ⁻",       (-1, 2, -2, 2, -2, -2)),
    ("π⁰",       (0, -1, -2, -2, 0, 0)),
    ("π±",       (-1, -1, -3, -3, 0, 0)),
    ("K±",       (-1, -6, -2, 2, 0, 1)),
    ("ρ",        (-1, 5, -2, 2, 0, 1)),
]


# ─── Main ─────────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 7 Phase 7e — α-coupling integration test")
    print("=" * 110)
    print()
    print("Goal: does the (p_t, S) coupling required by Phase 7c disturb")
    print("R60's α-architecture in the 11D metric?")
    print()

    # ─── Baseline ──────────────────────────────────────────────────
    p = track9_params()
    print("Baseline params (R60 Track 9 model-F-style):")
    print(f"  ε_e = {p.eps_e},  s_e = {p.s_e}")
    print(f"  ε_p = {p.eps_p},  s_p = {p.s_p}")
    print(f"  ε_ν = {p.eps_nu}, s_ν = {p.s_nu}")
    print(f"  k_e = k_p = k_ν = {p.k_e:.6f}")
    print(f"  σ_ta = √α = {p.sigma_ta:.6f}")
    print(f"  σ_at = 4πα = {p.sigma_at:.6f}")
    print()

    # Sanity: baseline α at σ_pS = 0
    G_base = build_metric_with_pS(p, 0.0, 0.0)
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

    # ─── Sweep σ_pS_tube ──────────────────────────────────────────────
    print("=" * 70)
    print("Sweep σ_pS_tube (S-isotropic; σ_pS_ring = 0)")
    print("=" * 70)

    sigma_values = np.linspace(-0.5, 0.5, 401)  # dimensionless entries
    sweep_data = []   # rows: (sigma, signature_ok, dict of α/α per mode)

    sig_band_low = None
    sig_band_high = None
    for sigma in sigma_values:
        G = build_metric_with_pS(p, sigma, 0.0)
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

    print(f"  Signature-OK σ_pS_tube range: [{sig_band_low:.4f}, {sig_band_high:.4f}]")
    print()

    # ─── Universality analysis within signature band ──────────────
    print("Sample α/α values across modes (σ_pS_tube ∈ signature band):")
    print()
    sample_sigmas = [-0.1, -0.05, -0.01, 0.0, 0.01, 0.05, 0.1]
    sample_sigmas = [s for s in sample_sigmas
                     if sig_band_low is not None and
                     sig_band_low <= s <= sig_band_high]

    print(f"  {'mode':<10s}  " +
          "  ".join(f"σ={s:+.3f}".ljust(10) for s in sample_sigmas))
    for label, tup in TEST_MODES:
        row = f"  {label:<10s}  "
        for s in sample_sigmas:
            # Find closest sweep entry
            idx = int(np.argmin(np.abs(sigma_values - s)))
            r = sweep_data[idx][2].get(label, float('nan'))
            row += f"{r:>10.6f}  "
        print(row)
    print()

    # ─── Universality metric: max relative deviation from baseline ───
    print("=" * 70)
    print("Universality metric: max |α(σ)/α(0) − 1| across test modes")
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

    # Find regions where deviation is below thresholds
    for threshold in [1e-6, 1e-4, 1e-2]:
        mask = max_dev < threshold
        if np.any(mask):
            kept = sigma_kept[mask]
            print(f"  |Δα/α| < {threshold:.0e}: σ_pS_tube ∈ "
                  f"[{kept.min():+.5f}, {kept.max():+.5f}]")
        else:
            print(f"  |Δα/α| < {threshold:.0e}: empty (no σ_pS_tube ≠ 0 satisfies)")
    print()

    # ─── Verdict ──────────────────────────────────────────────────
    print("=" * 70)
    print("VERDICT — Phase 7e")
    print("=" * 70)

    # Pure decoupling test: at small σ_pS_tube, does α stay at baseline?
    small_sigmas = [s for s in sample_sigmas if abs(s) > 0]
    decoupled = True
    for s in small_sigmas:
        idx = int(np.argmin(np.abs(sigma_values - s)))
        for label, _ in TEST_MODES:
            base = baseline_ratios[label]
            cur = sweep_data[idx][2][label]
            if base != 0 and np.isfinite(base):
                if abs(cur / base - 1.0) > 1e-10:
                    decoupled = False
                    break
        if not decoupled:
            break

    if decoupled:
        print("  → α-COUPLING SECTORS ARE DECOUPLED")
        print("    α(mode) is independent of σ_pS_tube to numerical noise.")
        print("    σ_pS_tube can be added to model-G without disturbing")
        print("    R60's α-architecture.")
    else:
        # Find first σ where deviation exceeds 1e-10
        for sigma, sig, ratios in sweep_data:
            if not sig or sigma == 0:
                continue
            for label, _ in TEST_MODES:
                base = baseline_ratios[label]
                cur = ratios[label]
                if base != 0 and np.isfinite(base):
                    if abs(cur / base - 1.0) > 1e-10:
                        print(f"  → α-COUPLING SECTORS ARE COUPLED")
                        print(f"    α({label}) deviates at σ_pS_tube = {sigma:+.5f}")
                        print(f"    {label} baseline α/α = {base:.6f}, "
                              f"σ_pS={sigma:+.4f} α/α = {cur:.6f}")
                        break
            break
        print()
        print("    σ_pS_tube needs structural prescription (analogous to σ_ra).")

    # ─── Plot ─────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. α/α vs σ_pS_tube for each mode
    ax = axes[0, 0]
    for label, _ in TEST_MODES:
        sigmas_p = []
        ratios_p = []
        for sigma, sig, ratios in sweep_data:
            if sig and np.isfinite(ratios.get(label, np.nan)):
                sigmas_p.append(sigma)
                ratios_p.append(ratios[label])
        ax.plot(sigmas_p, ratios_p, label=label, linewidth=1.2)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('σ_pS_tube')
    ax.set_ylabel('α(mode) / α₀')
    ax.set_title('α(mode) vs σ_pS_tube')
    ax.set_xlim(sig_band_low * 1.05 if sig_band_low else -0.5,
                sig_band_high * 1.05 if sig_band_high else 0.5)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=7, loc='best', ncol=2)

    # 2. Max deviation across modes
    ax = axes[0, 1]
    if len(sigma_kept) > 0:
        ax.semilogy(sigma_kept, np.maximum(max_dev, 1e-16),
                    color='blue', linewidth=1.5)
        ax.axhline(1e-6, color='green', linestyle='--', alpha=0.5,
                   label='ε = 10⁻⁶')
        ax.axhline(1e-4, color='orange', linestyle='--', alpha=0.5,
                   label='ε = 10⁻⁴')
        ax.axhline(1e-2, color='red', linestyle='--', alpha=0.5,
                   label='ε = 10⁻²')
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlabel('σ_pS_tube')
    ax.set_ylabel('max |α(σ)/α(0) − 1|')
    ax.set_title('Universality deviation across modes')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # 3. Signature-OK band
    ax = axes[1, 0]
    sig_array = np.array([1.0 if s[1] else 0.0 for s in sweep_data])
    ax.fill_between(sigma_values, 0, sig_array, alpha=0.4, color='green',
                    label='signature OK (1 negative eig)')
    ax.axvline(0, color='black', linewidth=0.5)
    if sig_band_low is not None:
        ax.axvline(sig_band_low, color='red', linestyle=':',
                   label=f'low edge: {sig_band_low:.3f}')
        ax.axvline(sig_band_high, color='red', linestyle=':',
                   label=f'high edge: {sig_band_high:.3f}')
    ax.set_xlabel('σ_pS_tube')
    ax.set_ylabel('signature OK (1 = yes)')
    ax.set_title('Signature preservation')
    ax.set_ylim(-0.1, 1.1)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # 4. Summary table
    ax = axes[1, 1]
    ax.axis('off')
    summary = [
        ['Test', 'Result'],
        ['Signature-OK band', f'[{sig_band_low:.3f}, {sig_band_high:.3f}]'
         if sig_band_low is not None else 'EMPTY'],
        ['α decoupled at σ ≠ 0', 'YES' if decoupled else 'NO'],
    ]
    if not decoupled:
        # find ε=1e-6 universality range
        mask = max_dev < 1e-6
        if np.any(mask):
            summary.append(['σ where |Δα|<10⁻⁶',
                            f'[{sigma_kept[mask].min():+.5f}, '
                            f'{sigma_kept[mask].max():+.5f}]'])
        else:
            summary.append(['σ where |Δα|<10⁻⁶', 'only σ=0'])
    table = ax.table(cellText=summary, loc='center',
                     colWidths=[0.50, 0.40])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.6)
    ax.set_title('Phase 7e summary')

    plt.tight_layout()
    fig_path = out_dir / "track7_phase7e_alpha_curves.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print()
    print(f"  Plot: {fig_path}")

    # ─── CSV ──────────────────────────────────────────────────────
    csv_path = out_dir / "track7_phase7e_alpha_universality.csv"
    fieldnames = ['sigma_pS_tube', 'signature_ok'] + \
                 [f'alpha_ratio_{label}' for label, _ in TEST_MODES]
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for sigma, sig, ratios in sweep_data:
            row = {'sigma_pS_tube': sigma, 'signature_ok': int(sig)}
            for label, _ in TEST_MODES:
                row[f'alpha_ratio_{label}'] = ratios.get(label, float('nan'))
            w.writerow(row)
    print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
