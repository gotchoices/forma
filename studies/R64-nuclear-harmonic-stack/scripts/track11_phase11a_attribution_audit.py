"""
R64 Track 11 Phase 11a — α-attribution audit for R64 quark inventory.

Premise: R64 decomposes the proton into u + u + d quarks, giving
proton tuple (3, +2) with n_pt = 3.  The α-Coulomb formula reads
n_pt linearly into Q, so α/α₀ = (n_pt)² = 9 at the R64 proton (vs
α/α₀ = 1 at R60 model-F proton (1, 3)).  This factor of 9 has been
silently propagated since Phase 7g.

Phase 11a tests:
  1. Quantify α/α₀ across full R64 inventory under current attribution.
  2. Test alternative attribution A1: charge function f(n_pt, n_pr)
     = n_pt/6 + n_pr/4 reproducing u = +2/3, d = −1/3, proton = +1.
  3. Test alternative calibration A2: σ_ta_p_R64 = √α / 3 to absorb
     the factor of 3 in the proton's tube charge.
  4. Compare σ_eff_ring at signature boundary under each rule (the
     Phase 10a quantity that capped at 1.13).

Outputs:
  outputs/track11_phase11a_attribution_audit.csv
  outputs/track11_phase11a_alpha_ratios.png
"""

import sys
import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

R60_SCRIPTS = Path(__file__).resolve().parent.parent.parent / "R60-metric-11" / "scripts"
sys.path.insert(0, str(R60_SCRIPTS))

from track1_solver import (    # noqa: E402
    Params, alpha_coulomb, mode_6_to_11, num_negative_eigs, signature_ok,
    ALPHA, SQRT_ALPHA, FOUR_PI,
    I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING, I_NU_TUBE, I_NU_RING,
    I_ALEPH, I_SX, I_SY, I_SZ, I_T,
    MA_SLICE,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import track9_params    # noqa: E402


# ─── R64 inventory (quark-decomposed) ─────────────────────────────────
# Each entry: (label, 6-tuple, expected_charge_in_e)
R64_INVENTORY = [
    # Single quarks (R64 primitives)
    ("u (R64 prim)",   (0, 0, 0, 0,  1, +2),  +2/3),
    ("d (R64 prim)",   (0, 0, 0, 0,  1, -2),  -1/3),
    # Baryons (R64 composites)
    ("R64 proton",     (0, 0, 0, 0,  3, +2),  +1.0),
    ("R64 neutron",    (0, 0, 0, 0,  3, -2),   0.0),
    # Two-nucleon compounds
    ("R64 deuteron",   (0, 0, 0, 0,  6,  0),  +1.0),
    ("R64 pp",         (0, 0, 0, 0,  6, +4),  +2.0),
    ("R64 nn",         (0, 0, 0, 0,  6, -4),   0.0),
    # Leptons (R60 model-F tuples; R64 keeps these unchanged)
    ("electron",       (1, 2, 0, 0, 0, 0),    -1.0),
    ("muon",           (1, 1, -2, -2, 0, 0),  -1.0),
    ("ν_e",            (0, 0, 1, 1, 0, 0),     0.0),
]


def f_charge(n_pt: int, n_pr: int) -> float:
    """Signed electric charge in units of e from p-sheet (n_pt, n_pr).

    Derived from u = (1, +2) → +2/3, d = (1, -2) → -1/3:
        f(n_pt, n_pr) = n_pt/6 + n_pr/4.

    Reproduces:
        u (1, +2):     1/6 + 1/2 = +2/3 ✓
        d (1, -2):     1/6 - 1/2 = -1/3 ✓
        proton (3,+2): 3/6 + 2/4 = +1   ✓
        neutron (3,-2):3/6 - 2/4 = 0    ✓
        deuteron(6,0): 6/6 + 0   = +1   ✓
    """
    return n_pt / 6.0 + n_pr / 4.0


def alpha_coulomb_A1(G: np.ndarray, n6: tuple) -> float:
    """Attribution rule A1: project p-sheet through f(n_pt, n_pr).

    Replaces the raw n_pt, n_pr contributions in Q with a single
    "charge-projected" contribution n_eff_p = f(n_pt, n_pr) on the
    tube row only (n_pr contribution absorbed into the projection).
    Other sheets (e, ν) are unchanged from R60 model-F.
    """
    G_inv = np.linalg.inv(G)
    n_et, n_er, n_νt, n_νr, n_pt, n_pr = n6
    n_eff_p = f_charge(n_pt, n_pr)
    # Build effective Ma vector: tube-only on p-sheet at n_eff_p.
    n_ma = np.zeros(6)
    n_ma[I_E_TUBE  - 1] = n_et
    n_ma[I_E_RING  - 1] = n_er
    n_ma[I_NU_TUBE - 1] = n_νt
    n_ma[I_NU_RING - 1] = n_νr
    n_ma[I_P_TUBE  - 1] = n_eff_p
    n_ma[I_P_RING  - 1] = 0.0   # absorbed into projection
    ma_t_col = G_inv[MA_SLICE, I_T]
    Q = float((n_ma @ ma_t_col) * (-G_inv[I_T, I_T]))
    return Q * Q / FOUR_PI


def build_p_recalibrated(p: Params, scale: float) -> Params:
    """Rule A2: scale the p-sheet's σ_ta by `scale` (e.g., 1/3)."""
    # In R60 the global σ_ta is sheet-symmetric.  R64 may need a
    # sheet-asymmetric calibration to absorb the n_pt = 3 factor.
    # The cleanest test: scale σ_ta only on the p-sheet.  This
    # requires a per-sheet σ_ta which the R60 solver doesn't
    # expose directly — so we apply the scaling via an offset in
    # the augmented metric.
    return p   # placeholder; actual scaling done in build helper.


def build_metric_A2(p: Params, p_sheet_scale: float):
    """Build metric with p-sheet σ_ta scaled by `p_sheet_scale`."""
    G = build_aug_metric(p).copy()
    # The aleph row entries that depend on σ_ta are at:
    #   G[I_ALEPH, I_P_TUBE] = sign_p · σ_ta  (and the symmetric)
    #   G[I_P_TUBE, I_ALEPH] = sign_p · σ_at  (and the symmetric)
    # Scaling σ_ta_p by `s` means scaling these p-sheet aleph
    # entries by `s`.
    sign_p = -1.0  # from track9_params
    base_ta = sign_p * p.sigma_ta
    base_at = sign_p * p.sigma_at
    new_ta = base_ta * p_sheet_scale
    new_at = base_at * p_sheet_scale
    # Reset to baseline first, then apply scaled values.
    G[I_ALEPH, I_P_TUBE] = new_ta
    G[I_P_TUBE, I_ALEPH] = new_ta
    # σ_at scaling: the σ_at entries are stored at (p_t, ℵ).
    # In R60 model-F, sigma_at maps to G[ℵ, p_t] same as σ_ta.
    # Skip σ_at scaling for now — focus on σ_ta which dominates the
    # α extraction at leading order.
    # Also need to scale σ_ra on p-sheet (which is (s_p · ε_p) · σ_ta).
    # sigma_ra_p was added in build_aug_metric as a derived quantity.
    # Recompute and scale.
    sigma_ra_p_old = (p.s_p * p.eps_p) * base_ta
    sigma_ra_p_new = (p.s_p * p.eps_p) * new_ta
    delta_ra = sigma_ra_p_new - sigma_ra_p_old
    G[I_ALEPH, I_P_RING] += delta_ra
    G[I_P_RING, I_ALEPH] += delta_ra
    return G


def build_aug_with_block(p, **entries):
    """Augment metric with sheet-S, aleph-S offsets (from Phase 10a)."""
    G = build_aug_metric(p).copy()

    def add(idx_a, idx_b, value):
        if value:
            G[idx_a, idx_b] += value
            G[idx_b, idx_a] += value

    for s_idx in (I_SX, I_SY, I_SZ):
        add(I_P_TUBE, s_idx, entries.get('sigma_pS_tube', 0.0))
        add(I_P_RING, s_idx, entries.get('sigma_pS_ring', 0.0))
        add(I_ALEPH,  s_idx, entries.get('sigma_aS', 0.0))
    return G


# ─── Audit machinery ────────────────────────────────────────────────

def audit_inventory(G: np.ndarray, label: str, alpha_func=None) -> list:
    """Compute α/α₀ at each R64 inventory entry."""
    if alpha_func is None:
        alpha_func = lambda G, n6: alpha_coulomb(G, mode_6_to_11(n6))
    results = []
    for inv_label, n6, q_expected in R64_INVENTORY:
        a = alpha_func(G, n6)
        ratio = a / ALPHA if ALPHA > 0 else 0.0
        # Expected ratio for charged modes: |q|² (since α ∝ Q²)
        expected_ratio = q_expected ** 2
        deviation = ratio - expected_ratio
        results.append({
            "rule": label,
            "mode": inv_label,
            "n6": n6,
            "q_expected_e": q_expected,
            "alpha_over_alpha0": ratio,
            "expected_ratio": expected_ratio,
            "deviation": deviation,
        })
    return results


def universality_spread(results: list) -> float:
    """Spread = max |α_actual/α_expected − 1| over charged modes only."""
    deviations = []
    for r in results:
        if r["expected_ratio"] > 1e-10:
            ratio = r["alpha_over_alpha0"] / r["expected_ratio"]
            deviations.append(abs(ratio - 1.0))
    return max(deviations) if deviations else 0.0


# ─── σ_eff_ring at signature boundary (Phase 10a context) ───────────

def signature_band_pS_ring(p: Params, sigma_max: float = 0.5,
                           n_steps: int = 500,
                           metric_builder=None) -> tuple:
    """Find largest σ_pS_ring keeping signature Lorentzian."""
    if metric_builder is None:
        metric_builder = lambda p, sigma: build_aug_with_block(
            p, sigma_pS_ring=sigma)
    sigmas = np.linspace(0.0, sigma_max, n_steps + 1)
    last_ok = 0.0
    for s in sigmas:
        G = metric_builder(p, s)
        if signature_ok(G):
            last_ok = s
        else:
            break
    return last_ok


def schur_sigma_eff_ring(G: np.ndarray) -> float:
    """Phase 10a's Schur-effective σ_eff_ring formula:
        σ_eff_ring = −G⁻¹[p_r, S_x] · g_pr · g_SS
    """
    try:
        G_inv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return float('nan')
    g_pr = G[I_P_RING, I_P_RING]
    g_SS = G[I_SX, I_SX]
    return float(-G_inv[I_P_RING, I_SX] * g_pr * g_SS)


# ─── Main ────────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    p = track9_params()

    # R64 Point B parameters (consistent with Phase 10a)
    p_R64 = p.copy_with(eps_p=0.2052, s_p=0.0250)

    print("=" * 90)
    print("R64 Track 11 Phase 11a — α-attribution audit")
    print("=" * 90)
    print()
    print(f"  R64 Point B: ε_p = {p_R64.eps_p}, s_p = {p_R64.s_p}")
    print(f"  σ_ta = {p_R64.sigma_ta:.6f} = √α")
    print(f"  σ_at = {p_R64.sigma_at:.6f} = 4πα")
    print()

    # ── Rule R0: status quo ─────────────────────────────────────────
    print("=" * 90)
    print("Rule R0: Status quo (current alpha_coulomb formula at R60 model-F + R64 Point B)")
    print("=" * 90)
    print()
    G0 = build_aug_metric(p_R64)
    print(f"  Signature OK: {signature_ok(G0)}")
    print(f"  G_inv[p_t, t]: {np.linalg.inv(G0)[I_P_TUBE, I_T]:+.6e}")
    print(f"  G_inv[p_r, t]: {np.linalg.inv(G0)[I_P_RING, I_T]:+.6e}")
    print()
    print(f"  {'mode':<18s}  {'tuple':<22s}  {'q_expected':>10s}  "
          f"{'α/α₀':>10s}  {'expected':>10s}  {'ratio':>10s}")
    print("  " + "─" * 82)
    R0 = audit_inventory(G0, "R0_status_quo")
    for r in R0:
        n6_str = str(r["n6"]).replace(" ", "")
        ratio = r["alpha_over_alpha0"] / r["expected_ratio"] if r["expected_ratio"] > 1e-10 else float('inf')
        print(f"  {r['mode']:<18s}  {n6_str:<22s}  "
              f"{r['q_expected_e']:>+10.4f}  "
              f"{r['alpha_over_alpha0']:>10.4f}  "
              f"{r['expected_ratio']:>10.4f}  "
              f"{ratio if not math.isinf(ratio) else '—':>10}")
    spread_R0 = universality_spread(R0)
    print(f"\n  Universality spread (R0): {spread_R0:.4e}")
    print()

    # ── Rule A1: charge function attribution ────────────────────────
    print("=" * 90)
    print("Rule A1: charge function f(n_pt, n_pr) = n_pt/6 + n_pr/4")
    print("=" * 90)
    print()
    print("  At each mode, p-sheet contribution to Q is n_eff_p = f(n_pt, n_pr).")
    print("  This is the signed electric charge in units of e.")
    print()
    print(f"  {'mode':<18s}  {'tuple':<22s}  {'q_expected':>10s}  "
          f"{'α/α₀':>10s}  {'expected':>10s}  {'ratio':>10s}")
    print("  " + "─" * 82)
    R_A1 = audit_inventory(G0, "A1_charge_function", alpha_func=alpha_coulomb_A1)
    for r in R_A1:
        n6_str = str(r["n6"]).replace(" ", "")
        ratio = r["alpha_over_alpha0"] / r["expected_ratio"] if r["expected_ratio"] > 1e-10 else float('inf')
        ratio_str = f"{ratio:.4f}" if not math.isinf(ratio) else "—"
        print(f"  {r['mode']:<18s}  {n6_str:<22s}  "
              f"{r['q_expected_e']:>+10.4f}  "
              f"{r['alpha_over_alpha0']:>10.4f}  "
              f"{r['expected_ratio']:>10.4f}  "
              f"{ratio_str:>10}")
    spread_A1 = universality_spread(R_A1)
    print(f"\n  Universality spread (A1): {spread_A1:.4e}")
    print()

    # ── Rule A2: scale σ_ta_p by 1/3 ────────────────────────────────
    print("=" * 90)
    print("Rule A2: σ_ta_p scaled by 1/3 (absorbs the n_pt = 3 factor)")
    print("=" * 90)
    print()
    G_A2 = build_metric_A2(p_R64, p_sheet_scale=1.0/3.0)
    sig_ok_A2 = signature_ok(G_A2)
    print(f"  Signature OK: {sig_ok_A2}")
    if sig_ok_A2:
        print(f"  G_inv[p_t, t]: {np.linalg.inv(G_A2)[I_P_TUBE, I_T]:+.6e}")
    print()
    print(f"  {'mode':<18s}  {'tuple':<22s}  {'q_expected':>10s}  "
          f"{'α/α₀':>10s}  {'expected':>10s}  {'ratio':>10s}")
    print("  " + "─" * 82)
    R_A2 = audit_inventory(G_A2, "A2_sigma_ta_scaled")
    for r in R_A2:
        n6_str = str(r["n6"]).replace(" ", "")
        ratio = r["alpha_over_alpha0"] / r["expected_ratio"] if r["expected_ratio"] > 1e-10 else float('inf')
        ratio_str = f"{ratio:.4f}" if not math.isinf(ratio) else "—"
        print(f"  {r['mode']:<18s}  {n6_str:<22s}  "
              f"{r['q_expected_e']:>+10.4f}  "
              f"{r['alpha_over_alpha0']:>10.4f}  "
              f"{r['expected_ratio']:>10.4f}  "
              f"{ratio_str:>10}")
    spread_A2 = universality_spread(R_A2)
    print(f"\n  Universality spread (A2): {spread_A2:.4e}")
    print()

    # ── σ_eff_ring at signature boundary under each rule ────────────
    print("=" * 90)
    print("σ_eff_ring at signature boundary (Phase 10a comparison)")
    print("=" * 90)
    print()

    # R0 baseline (Phase 10a): metric structure unchanged.
    band_R0 = signature_band_pS_ring(p_R64)
    G_R0_band = build_aug_with_block(p_R64, sigma_pS_ring=band_R0)
    sigma_eff_R0 = schur_sigma_eff_ring(G_R0_band)
    print(f"  R0 (status quo):")
    print(f"    σ_pS_ring band boundary: ±{band_R0:.4f}")
    print(f"    σ_eff_ring (Schur):       {sigma_eff_R0:+.4f}")
    print(f"    Phase 7c target:          ±116")
    print(f"    Gap factor:               {abs(116/sigma_eff_R0) if sigma_eff_R0 != 0 else float('inf'):.1f}×")
    print()

    if sig_ok_A2:
        # A2 metric: scaled σ_ta_p.
        def builder_A2(p_in, sigma):
            G = build_metric_A2(p_in, p_sheet_scale=1.0/3.0)
            for s_idx in (I_SX, I_SY, I_SZ):
                G[I_P_RING, s_idx] += sigma
                G[s_idx, I_P_RING] += sigma
            return G

        band_A2 = signature_band_pS_ring(p_R64, metric_builder=builder_A2)
        G_A2_band = builder_A2(p_R64, band_A2)
        sigma_eff_A2 = schur_sigma_eff_ring(G_A2_band)
        print(f"  A2 (σ_ta_p scaled by 1/3):")
        print(f"    σ_pS_ring band boundary: ±{band_A2:.4f}")
        print(f"    σ_eff_ring (Schur):       {sigma_eff_A2:+.4f}")
        print(f"    Gap factor:               {abs(116/sigma_eff_A2) if sigma_eff_A2 != 0 else float('inf'):.1f}×")
        print(f"    Ratio vs R0:              {sigma_eff_A2/sigma_eff_R0:.4f}×" if sigma_eff_R0 != 0 else "")
    else:
        print(f"  A2 (σ_ta_p scaled by 1/3): Signature broke — band undefined")
    print()

    # ── Verdict ─────────────────────────────────────────────────────
    print("=" * 90)
    print("VERDICT — Phase 11a")
    print("=" * 90)
    print()
    proton_R0 = next(r for r in R0 if r["mode"] == "R64 proton")
    proton_A1 = next(r for r in R_A1 if r["mode"] == "R64 proton")
    proton_A2 = next(r for r in R_A2 if r["mode"] == "R64 proton")
    print(f"  R64 proton α/α₀ under each rule:")
    print(f"    R0 (status quo):                {proton_R0['alpha_over_alpha0']:.4f}  (expected 1.0)")
    print(f"    A1 (charge-function projection): {proton_A1['alpha_over_alpha0']:.4f}  (expected 1.0)")
    print(f"    A2 (σ_ta_p scaled by 1/3):       {proton_A2['alpha_over_alpha0']:.4f}  (expected 1.0)")
    print()
    print(f"  Universality spread (charged-mode max |α_actual/α_expected − 1|):")
    print(f"    R0: {spread_R0:.4e}")
    print(f"    A1: {spread_A1:.4e}")
    print(f"    A2: {spread_A2:.4e}")
    print()

    # Determine outcome
    rules_passing = []
    for label, spread, p_ratio in [
        ("R0", spread_R0, proton_R0['alpha_over_alpha0']),
        ("A1", spread_A1, proton_A1['alpha_over_alpha0']),
        ("A2", spread_A2, proton_A2['alpha_over_alpha0']),
    ]:
        if abs(p_ratio - 1.0) < 1e-3 and spread < 1e-3:
            rules_passing.append(label)

    if rules_passing:
        print(f"  → Rules giving correct R64 proton α AND universality: {', '.join(rules_passing)}")
        print(f"  → Outcome A or B candidate (depending on σ_eff impact).")
    else:
        print(f"  → No simple rule recovers α universality at R64 inventory tuples.")
        print(f"  → Outcome C: R64's primitive composition is incompatible with current α formula.")
    print()

    # Write CSV
    csv_path = out_dir / "track11_phase11a_attribution_audit.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "rule", "mode", "n6", "q_expected_e",
            "alpha_over_alpha0", "expected_ratio", "deviation",
        ])
        writer.writeheader()
        for r in R0 + R_A1 + R_A2:
            r2 = dict(r)
            r2["n6"] = str(r2["n6"]).replace(" ", "")
            writer.writerow(r2)
    print(f"  CSV: {csv_path}")

    # Plot
    fig, ax = plt.subplots(figsize=(11, 6))
    rules = ["R0", "A1", "A2"]
    rule_data = {"R0": R0, "A1": R_A1, "A2": R_A2}
    width = 0.25
    labels = [r["mode"] for r in R0]
    x = np.arange(len(labels))
    for i, rule in enumerate(rules):
        ratios = []
        for r in rule_data[rule]:
            if r["expected_ratio"] > 1e-10:
                ratios.append(r["alpha_over_alpha0"] / r["expected_ratio"])
            else:
                ratios.append(np.nan)
        ax.bar(x + (i - 1) * width, ratios, width, label=rule)
    ax.axhline(1.0, color="black", linestyle="--", alpha=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_ylabel("α(mode) / α_expected   (charged modes)")
    ax.set_title("Phase 11a: α-attribution under three rules")
    ax.legend()
    ax.set_yscale("log")
    plt.tight_layout()
    plt.savefig(out_dir / "track11_phase11a_alpha_ratios.png", dpi=120)
    plt.close()
    print(f"  PNG: {out_dir / 'track11_phase11a_alpha_ratios.png'}")
    print()


if __name__ == "__main__":
    main()
