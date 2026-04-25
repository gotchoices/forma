"""
R64 Track 7 Phase 7f — Unit translation: 7-tensor σ_t ↔ 11D σ_pS_tube.

Phase 7c's σ_t = −116.1 lives in the 7-tensor formula

    m²(k_S) = m²_Ma + 4·(ℏc)²·k_S² + 2·k_S·σ_t·n_pt·ℏc

where σ_t implicitly carries (1/L_p) units (the 7-tensor doesn't
distinguish a metric off-diagonal from a coupling coefficient).

R60's 11D σ_pS_tube is a dimensionless metric component — entries
of G are dimensionless, mass extraction goes via
`E² = (2πℏc)² · ñ · G⁻¹ · ñ` with ñ = n/L.

Phase 7e showed α-universality breaks for σ_pS_tube outside
[−0.0025, +0.0025].  Question: where does Phase 7c's σ_t = −116
land in 11D units?

### Method

In R60's 11D metric augmented with σ_pS_tube at G[p_t, S_*]
(S-isotropic), evaluating mass at compound (n_p_t, n_p_r, k_S)
gives a Schur-complement cross term in m² of the form

    Δm²_cross(11D) ≈ (2πℏc)² · 2 · ñ_p_t · k_S · G⁻¹[p_t, S]
                  ≈ −(2πℏc)² · 2 · (n_p_t / L_p_t) · k_S
                       · σ_pS_tube / (G[p_t, p_t] · G[S, S])

with G[p_t, p_t] = k_p · 1 = k_p (single-k) and G[S, S] = 1.

For this to equal the 7-tensor cross term `2 · k_S · σ_t · n_pt · ℏc`:

    σ_pS_tube_equiv = −σ_t · L_p_t · k_p / [(2π)² · ℏc]

with L_p_t = ε_p · L_ring_p the p-sheet *tube* length, k_p the
metric per-sheet scale.

The factor structure:
  • σ_t in 7-tensor units multiplies (n_pt · ℏc) directly
  • σ_pS_tube in 11D is dimensionless inside G
  • Translation requires the L_p_t scale and (2π)² from
    Bohr-Sommerfeld + ℏc to land in MeV²

### What this phase does

1. Set up R60 baseline (Track 9 model-F-style params).
2. Compute σ_pS_tube_equiv via the formula above for σ_t = −116.1.
3. Verify numerically: build the 11D metric with σ_pS_tube_equiv,
   evaluate m at finite k_S, compare with 7-tensor's prediction
   at the same parameters.
4. Locate σ_pS_tube_equiv in Phase 7e's signature and universality
   bands.
5. Report whether 7c's coupling is "safely small" or
   "problematically large" in 11D units.

### Caveats

- Track 9 baseline (ε_p = 0.4, s_p = 3.0) differs from R64
  Point B (ε_p = 0.2052, s_p = 0.025) — the unit translation
  depends on which baseline we use.  Phase 7g re-runs the
  α-test at R64's own frame; here we use Track 9's L_p for
  numerical translation, then re-do with R64 params for
  cross-check.

Outputs:
  outputs/track7_phase7f_unit_translation.csv
  outputs/track7_phase7f_unit_translation.png
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
    mode_6_to_11, L_vector_from_params, mode_energy,
    derive_L_ring,
    ALPHA, SQRT_ALPHA, FOUR_PI, M_E_MEV, M_P_MEV,
    HBAR_C_MEV_FM, TWO_PI_HC,
    I_ALEPH, I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING,
    I_NU_TUBE, I_NU_RING, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import track9_params    # noqa: E402

# Phase 7c value
SIGMA_T_7C = -116.1

# Phase 7e signature and universality bands (dimensionless)
SIG_BAND = (-0.0750, +0.0750)
UNIV_1PCT_BAND = (-0.00250, +0.00250)


def build_metric_with_pS(p, sigma_pS_tube, sigma_pS_ring=0.0):
    """R60 model-F augmented metric plus (p_t/p_r, S_*) cross-shears."""
    G = build_aug_metric(p).copy()
    for s_idx in (I_SX, I_SY, I_SZ):
        G[I_P_TUBE, s_idx] += sigma_pS_tube
        G[s_idx, I_P_TUBE] += sigma_pS_tube
        if sigma_pS_ring != 0.0:
            G[I_P_RING, s_idx] += sigma_pS_ring
            G[s_idx, I_P_RING] += sigma_pS_ring
    return G


def compute_cross_coefficient_11D(p, sigma_pS_tube, n_pt=6, k_S=1.0):
    """Numerically evaluate the cross-coefficient in m²(k_S) for the
    augmented 11D metric.  Returns the coefficient C such that
    m² ≈ m²(k_S=0) + 4·(ℏc)²·k_S² + C·k_S, isolating the σ_pS-induced
    cross term.

    Method:
      m²(σ, k_S=0) = baseline; m²(σ, k_S) - m²(σ, k_S=0) - 4(ℏc)²·k_S²
                    isolates the cross contribution.
      Divide by k_S to get the per-k_S coefficient.

    For comparison with 7c: cross_coef_7c = 2·σ_t·n_pt·ℏc
    """
    G_aug = build_metric_with_pS(p, sigma_pS_tube, 0.0)
    # mode_energy uses MA_SLICE; we need full 11D evaluation including S
    # Build n11 with n_pt and one S momentum (k_S taken as n_S = k_S * L_S
    # with L_S = 1 fm placeholder for "extended S")
    n11 = np.zeros(11)
    n11[I_P_TUBE] = n_pt
    L = L_vector_from_params(p)
    # For S, treat n_S as the dimensionless "winding-equivalent" so that
    # n_S/L_S = k_S (using L_S = 1 fm placeholder)
    # m² = (2πℏc)² · ñ · G⁻¹ · ñ, ñ = n/L, ñ_S = k_S
    n_tilde = n11 / L
    n_tilde[I_SX] = k_S
    G_inv = np.linalg.inv(G_aug)
    m2 = (TWO_PI_HC ** 2) * (n_tilde @ G_inv @ n_tilde)
    return m2


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 7 Phase 7f — Unit translation 7-tensor σ_t ↔ 11D σ_pS_tube")
    print("=" * 110)
    print()

    # ─── Baseline ──────────────────────────────────────────────────
    p = track9_params()
    L_p_t = p.eps_p * p.L_ring_p
    print(f"Baseline (R60 Track 9 model-F-style):")
    print(f"  ε_p = {p.eps_p}, s_p = {p.s_p}")
    print(f"  L_ring_p = {p.L_ring_p:.4f} fm")
    print(f"  L_p_tube = ε·L_r = {L_p_t:.4f} fm")
    print(f"  k_p = {p.k_p:.6f}")
    print(f"  σ_ta = √α = {p.sigma_ta:.6f}")
    print()

    # ─── Analytical translation ─────────────────────────────────────
    print("─" * 70)
    print("Analytical Schur-complement translation")
    print("─" * 70)
    print()
    print("Equating cross terms in m²(k_S):")
    print("  7-tensor:  2 · k_S · σ_t · n_pt · ℏc")
    print("  11D Schur: −(2π·ℏc)² · 2 · (n_pt/L_p) · k_S · σ_pS / (k_p · 1)")
    print()
    print("  → σ_pS = −σ_t · L_p · k_p / [(2π)² · ℏc]")
    print()

    sigma_pS_analytical = -SIGMA_T_7C * L_p_t * p.k_p / ((2 * math.pi) ** 2 * HBAR_C_MEV_FM)
    print(f"  σ_t (7-tensor) = {SIGMA_T_7C}")
    print(f"  σ_pS_analytical = -({SIGMA_T_7C}) · {L_p_t:.4f} · {p.k_p:.6f}"
          f" / [(2π)² · {HBAR_C_MEV_FM}]")
    print(f"                  = {sigma_pS_analytical:+.6e}")
    print()

    # ─── Numerical verification ─────────────────────────────────────
    print("─" * 70)
    print("Numerical verification: build 11D metric, evaluate m²(k_S)")
    print("─" * 70)
    print()

    n_pt_test = 6
    k_S_test = 1.0  # fm⁻¹  (=1/r, r=1 fm)

    # Baseline at σ_pS = 0
    m2_zero = compute_cross_coefficient_11D(p, 0.0, n_pt=n_pt_test, k_S=k_S_test)

    # Perturbed at σ_pS = σ_pS_analytical
    m2_pert = compute_cross_coefficient_11D(p, sigma_pS_analytical,
                                              n_pt=n_pt_test, k_S=k_S_test)

    delta_m2_11D = m2_pert - m2_zero  # MeV²

    # 7-tensor prediction at the same n_pt and k_S, ignoring kinetic A
    # (which is part of m2_zero approximately).  Cross term only:
    delta_m2_7c = 2 * k_S_test * SIGMA_T_7C * n_pt_test * HBAR_C_MEV_FM

    print(f"  Test mode: n_pt = {n_pt_test}, k_S = {k_S_test} fm⁻¹")
    print(f"  m²(σ_pS=0)         = {m2_zero:.6e} MeV²")
    print(f"  m²(σ_pS=σ_eq)      = {m2_pert:.6e} MeV²")
    print(f"  11D Δm² (full)     = {delta_m2_11D:+.6e} MeV²")
    print(f"  7c Δm² (cross only) = {delta_m2_7c:+.6e} MeV²")
    print(f"  Ratio 11D / 7c     = {delta_m2_11D / delta_m2_7c:+.6f}")
    print()
    print(f"  (Ratio close to 1 confirms unit translation; deviations come")
    print(f"   from finite-σ Schur higher-order terms and kinetic A↔1 mismatch.)")
    print()

    # ─── Numerical refinement: solve for σ_pS that reproduces 7c Δm² ──
    print("─" * 70)
    print("Numerical refinement: solve for σ_pS giving 7c's Δm² exactly")
    print("─" * 70)
    print()
    from scipy.optimize import brentq

    target_delta_m2 = delta_m2_7c

    def residual(sigma):
        try:
            m2 = compute_cross_coefficient_11D(p, sigma,
                                                 n_pt=n_pt_test, k_S=k_S_test)
            return (m2 - m2_zero) - target_delta_m2
        except Exception:
            return 1e30

    # Search range around analytical estimate
    s_lo = sigma_pS_analytical * 5
    s_hi = sigma_pS_analytical * 0.1 if sigma_pS_analytical < 0 else 0.0
    if sigma_pS_analytical > 0:
        s_lo, s_hi = sigma_pS_analytical * 0.1, sigma_pS_analytical * 5
    # Make sure bracket has different signs
    if residual(s_lo) * residual(s_hi) > 0:
        # Try a wider range
        s_lo, s_hi = -0.05, 0.05

    try:
        sigma_pS_numerical = brentq(residual, s_lo, s_hi, xtol=1e-9)
        print(f"  σ_pS (numerical, exact match to 7c Δm²): {sigma_pS_numerical:+.6e}")
        print(f"  σ_pS (analytical, leading order):         {sigma_pS_analytical:+.6e}")
        print(f"  Higher-order correction factor: "
              f"{sigma_pS_numerical / sigma_pS_analytical:+.6f}")
    except Exception as e:
        print(f"  Numerical refinement failed: {e}")
        sigma_pS_numerical = sigma_pS_analytical
    print()

    # ─── Locate in Phase 7e bands ───────────────────────────────────
    print("=" * 70)
    print("Locating σ_pS_equiv in Phase 7e signature/universality bands")
    print("=" * 70)
    print()
    abs_sigma = abs(sigma_pS_numerical)
    print(f"  σ_pS_equiv (from 7c σ_t=-116.1):  {sigma_pS_numerical:+.6e}")
    print(f"  |σ_pS_equiv|:                     {abs_sigma:.6e}")
    print()
    print(f"  Phase 7e signature-OK band:       [{SIG_BAND[0]:+.4f}, {SIG_BAND[1]:+.4f}]")
    print(f"  Phase 7e universality (1%) band:  [{UNIV_1PCT_BAND[0]:+.5f}, "
          f"{UNIV_1PCT_BAND[1]:+.5f}]")
    print()

    in_sig_band = SIG_BAND[0] <= sigma_pS_numerical <= SIG_BAND[1]
    in_univ_1pct = UNIV_1PCT_BAND[0] <= sigma_pS_numerical <= UNIV_1PCT_BAND[1]

    if in_sig_band:
        print(f"  ✓ INSIDE signature band")
    else:
        print(f"  ✗ OUTSIDE signature band — metric is unphysical")

    if in_univ_1pct:
        print(f"  ✓ INSIDE universality (1%) band — α perturbation < 1%")
    else:
        print(f"  ✗ OUTSIDE universality (1%) band — α perturbation > 1%")
        if in_sig_band:
            ratio = abs_sigma / UNIV_1PCT_BAND[1]
            print(f"    |σ_pS_equiv| is {ratio:.2f}× the 1% threshold")
            # Estimate magnitude of α perturbation at this σ
            # From 7e: deviation is quadratic, |Δα/α| ~ (σ/0.05)² · 0.16 (electron)
            # at σ=0.05 → Δα/α = 0.166; so coefficient ~ 0.166/0.05² = 66.4
            est_dev = (sigma_pS_numerical / 0.05)**2 * 0.166
            print(f"    Estimated α(electron) shift: ~{est_dev*100:.2f}%")

    # ─── Re-run with R64 Point B params for cross-check ─────────────
    print()
    print("=" * 70)
    print("Cross-check: σ_pS at R64 Point B params")
    print("=" * 70)
    print()

    # R64 Point B params — adjust eps_p, s_p, derive new L_ring_p
    # Keep model-F's k_p
    EPS_P_R64 = 0.2052
    S_P_R64 = 0.0250
    K_P_R64_in_modelF = derive_L_ring(M_P_MEV, 3, 2, EPS_P_R64, S_P_R64, p.k_p)

    # Build R64 params (preserve model-F α-architecture)
    p_r64 = p.copy_with(
        eps_p=EPS_P_R64,
        s_p=S_P_R64,
        L_ring_p=K_P_R64_in_modelF,  # derived to give m_p=938 at R64 (3,2) tuple
    )

    L_p_t_r64 = p_r64.eps_p * p_r64.L_ring_p

    print(f"  R64 Point B (in R60 metric units):")
    print(f"    ε_p = {p_r64.eps_p}, s_p = {p_r64.s_p}")
    print(f"    L_ring_p = {p_r64.L_ring_p:.4f} fm")
    print(f"    L_p_tube = {L_p_t_r64:.4f} fm")
    print()

    sigma_pS_r64_analytical = (-SIGMA_T_7C * L_p_t_r64 * p_r64.k_p
                                / ((2 * math.pi) ** 2 * HBAR_C_MEV_FM))
    print(f"  σ_pS_analytical (R64 Point B params): {sigma_pS_r64_analytical:+.6e}")

    in_sig_r64 = SIG_BAND[0] <= sigma_pS_r64_analytical <= SIG_BAND[1]
    in_univ_r64 = UNIV_1PCT_BAND[0] <= sigma_pS_r64_analytical <= UNIV_1PCT_BAND[1]
    print(f"  → in signature band:    {in_sig_r64}")
    print(f"  → in universality band: {in_univ_r64}")
    print()

    # ─── Plot ───────────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Position relative to bands
    ax = axes[0]
    ax.axvspan(SIG_BAND[0], SIG_BAND[1], alpha=0.2, color='green',
               label='signature OK')
    ax.axvspan(UNIV_1PCT_BAND[0], UNIV_1PCT_BAND[1], alpha=0.4, color='blue',
               label='universality < 1%')
    ax.axvline(sigma_pS_numerical, color='red', linewidth=2,
               label=f'7c σ_t→σ_pS (Track 9): {sigma_pS_numerical:+.4f}')
    ax.axvline(sigma_pS_r64_analytical, color='purple', linewidth=2,
               linestyle='--',
               label=f'7c σ_t→σ_pS (R64 PB): {sigma_pS_r64_analytical:+.4f}')
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlabel('σ_pS_tube (dimensionless 11D)')
    ax.set_yticks([])
    ax.set_xlim(-0.1, 0.1)
    ax.legend(fontsize=8, loc='upper right')
    ax.set_title('Phase 7c σ_t equivalence in 11D bands')

    # Detail near the universality band
    ax = axes[1]
    ax.axvspan(UNIV_1PCT_BAND[0], UNIV_1PCT_BAND[1], alpha=0.4, color='blue',
               label='universality < 1%')
    ax.axvline(sigma_pS_numerical, color='red', linewidth=2,
               label=f'σ_pS (Track 9): {sigma_pS_numerical:+.5f}')
    ax.axvline(sigma_pS_r64_analytical, color='purple', linewidth=2,
               linestyle='--',
               label=f'σ_pS (R64 PB): {sigma_pS_r64_analytical:+.5f}')
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlabel('σ_pS_tube (dimensionless 11D)')
    ax.set_yticks([])
    ax.set_xlim(-0.02, 0.02)
    ax.legend(fontsize=8, loc='upper right')
    ax.set_title('Zoom on universality band')

    plt.tight_layout()
    fig_path = out_dir / "track7_phase7f_unit_translation.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {fig_path}")

    # ─── CSV ────────────────────────────────────────────────────────
    csv_path = out_dir / "track7_phase7f_unit_translation.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['quantity', 'value', 'unit'])
        w.writerow(['sigma_t_7c', SIGMA_T_7C, '7-tensor units'])
        w.writerow(['sigma_pS_analytical_track9', sigma_pS_analytical,
                    'dimensionless 11D'])
        w.writerow(['sigma_pS_numerical_track9', sigma_pS_numerical,
                    'dimensionless 11D'])
        w.writerow(['sigma_pS_analytical_R64PB', sigma_pS_r64_analytical,
                    'dimensionless 11D'])
        w.writerow(['signature_band_low', SIG_BAND[0], '11D'])
        w.writerow(['signature_band_high', SIG_BAND[1], '11D'])
        w.writerow(['univ_1pct_low', UNIV_1PCT_BAND[0], '11D'])
        w.writerow(['univ_1pct_high', UNIV_1PCT_BAND[1], '11D'])
        w.writerow(['in_sig_band_track9', in_sig_band, 'bool'])
        w.writerow(['in_univ_1pct_track9', in_univ_1pct, 'bool'])
        w.writerow(['in_sig_band_R64PB', in_sig_r64, 'bool'])
        w.writerow(['in_univ_1pct_R64PB', in_univ_r64, 'bool'])
    print(f"  CSV: {csv_path}")

    # ─── Verdict ────────────────────────────────────────────────────
    print()
    print("=" * 110)
    print("VERDICT — Phase 7f")
    print("=" * 110)
    print()

    if in_univ_1pct:
        print(f"  Phase 7c's σ_t = {SIGMA_T_7C} translates to a TINY 11D σ_pS_tube ≈ "
              f"{sigma_pS_numerical:+.5f}")
        print(f"  This is INSIDE Phase 7e's 1% universality band.")
        print(f"  → α-perturbation from 7c's coupling is <1% — model-F effectively")
        print(f"    intact.  Pool item m (Yukawa pivot) NOT forced by 7e/7f.")
    elif in_sig_band:
        print(f"  Phase 7c's σ_t = {SIGMA_T_7C} translates to 11D σ_pS_tube ≈ "
              f"{sigma_pS_numerical:+.5f}")
        print(f"  Inside signature band but OUTSIDE 1% universality band.")
        print(f"  → α-perturbation at the few-percent level for some modes.")
        print(f"    Model-G integration requires a structural prescription for")
        print(f"    σ_pS_tube — pool item m Yukawa pivot remains a strong alternative.")
    else:
        print(f"  Phase 7c's σ_t = {SIGMA_T_7C} translates to 11D σ_pS_tube ≈ "
              f"{sigma_pS_numerical:+.5f}")
        print(f"  OUTSIDE the signature-OK band — 7c's coupling magnitude is")
        print(f"  too large to fit in R60's 11D framework directly.")
        print(f"  → Strong evidence that 7c's σ_t is NOT a metric off-diagonal.")
        print(f"    Pool item m (Yukawa propagator) is the natural reframing.")


if __name__ == "__main__":
    main()
