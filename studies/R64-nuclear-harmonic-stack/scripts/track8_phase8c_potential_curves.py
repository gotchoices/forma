"""
R64 Track 8 Phase 8c — V(r) along the (σ_aS, σ_at) universality locus.

Phase 8b established a 1D locus in (σ_aS, σ_at) space where
α = 1/137.036 exactly, extending to σ_aS = ±0.31.  Phase 8c
computes the two-nucleon potential V(r) at representative points
on the locus and asks: does V(r) have a strong-force trough at
intermediate r when σ_aS is at "strong-force magnitude"?

═══════════════════════════════════════════════════════════════════════
KINEMATIC NORMALIZATION (corrected from earlier 8c run):

Earlier 8c used R60's `mode_energy()` machinery, which carries a
`(2π·ℏc)²` prefactor appropriate for compact-direction standing-
wave momentum.  When applied to the S-direction (which is NOT
compactified) with `k_S = 1/r`, this implicitly assumed
single-particle relativistic momentum p = 2π·ℏ/r — a wavelength-r
de Broglie convention with NO two-body kinematic factor.

For two-body relative motion in COM frame, the correct invariant-
mass-squared kinematic addition is:

    M_inv²(p_rel) = M_total² + 4·p_rel²

with p_rel = ℏ·k_S = ℏ/r (just the Heisenberg uncertainty scale).
This gives kinetic prefactor 4·(ℏc)², not (2π·ℏc)².

The earlier 8c result inflated the S-direction kinetic term by
(2π)²/4 = π² ≈ 9.87 — large enough that any attractive cross
coupling couldn't produce a visible trough.  This phase recomputes
using Phase 7c's convention (4·(ℏc)² for two-body), with the
cross-coupling extracted from the full augmented 11D Schur
structure.
═══════════════════════════════════════════════════════════════════════

Method (corrected):

1. Build augmented 11D metric with σ_aS at G[ℵ, S_x/y/z] and σ_at
   on the universality locus from Phase 8b.
2. Invert numerically to get G⁻¹.
3. Extract effective (p_t, S) coupling: σ_eff = G⁻¹[p_t, S_x] /
   |G⁻¹[p_t,p_t]·G⁻¹[S_x,S_x]| — converting from inverse-metric
   off-diagonal to the equivalent of Phase 7c's σ_t entry.
4. Plug σ_eff into Phase 7c's mass formula:

       m²(k_S) = m²_Ma + 4·(ℏc)²·k_S² + 2·k_S·σ_eff·n_pt·ℏc

5. V(r) = m(r) − M_constituents.

This gives a Phase 7c-equivalent calculation with the aleph-
mediated coupling.  Direct comparison: at what σ_aS does the
Schur-effective σ_eff equal Phase 7c's σ_t = -116?  Is that
σ_aS inside the universality locus?

Outputs:
  outputs/track8_phase8c_potential_curves.csv
  outputs/track8_phase8c_potential_curves.png
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
    Params, signature_ok,
    ALPHA, SQRT_ALPHA, FOUR_PI, HBAR_C_MEV_FM,
    I_ALEPH, I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING,
    I_NU_TUBE, I_NU_RING, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import track9_params    # noqa: E402


# ─── Two-body kinematic constants (Phase 7c convention) ─────────────

A_KINETIC = 4.0 * HBAR_C_MEV_FM ** 2     # = 4·(ℏc)²    [MeV²·fm²]


# ─── Augmented metric construction ──────────────────────────────────

def build_metric_with_aS_at(p, sigma_aS, sigma_at):
    """R60 model-F augmented metric with σ_aS at G[ℵ, S] and overridden σ_at."""
    p_modified = p.copy_with(sigma_at=sigma_at)
    G = build_aug_metric(p_modified).copy()
    for s_idx in (I_SX, I_SY, I_SZ):
        G[I_ALEPH, s_idx] += sigma_aS
        G[s_idx, I_ALEPH] += sigma_aS
    return G


def schur_effective_sigma_pS(p, sigma_aS, sigma_at):
    """Extract the Phase 7c-equivalent σ_t from the augmented 11D metric.

    The aleph-mediated path p_t ─[σ_ta]→ ℵ ─[σ_aS]→ S induces an
    effective off-diagonal G⁻¹[p_t, S_x] in the inverse metric.
    Convert to the equivalent direct entry that would appear in
    Phase 7c's σ_pS_tube via:

        σ_eff = -G⁻¹[p_t, S_x] · √(G[p_t,p_t] · G[S_x,S_x])

    To leading order this equals σ_ta · σ_aS · (geometric factor),
    but using the full inverse captures higher-order Schur effects.
    """
    G = build_metric_with_aS_at(p, sigma_aS, sigma_at)
    G_inv = np.linalg.inv(G)
    # Sign convention: σ_eff appears in 7c as +σ_t entry at G[p_t, S];
    # the inverse-metric off-diagonal flips sign at leading order.
    # We extract the magnitude with a normalization that recovers σ_t
    # at the leading-order level.
    g_pp = G[I_P_TUBE, I_P_TUBE]
    g_SS = G[I_SX, I_SX]
    sigma_eff = -G_inv[I_P_TUBE, I_SX] * g_pp * g_SS
    return sigma_eff


def schur_leading_order_sigma_pS(sigma_aS, sigma_ta):
    """Analytical leading-order: σ_eff ≈ σ_ta · σ_aS / g_aa = σ_ta · σ_aS."""
    return sigma_ta * sigma_aS


# ─── 7c-style mass formula with corrected kinematics ────────────────

def mu2_Ma_p_sheet(n_pt, n_pr, eps_p, s_p):
    """Dimensionless p-sheet mass-squared eigenvalue."""
    return (n_pt / eps_p) ** 2 + (n_pr - s_p * n_pt) ** 2


def m_Ma(n_pt, n_pr, eps_p, s_p, K_p):
    """Compound p-sheet mass in MeV (Ma side, no S coupling)."""
    return K_p * math.sqrt(mu2_Ma_p_sheet(n_pt, n_pr, eps_p, s_p))


def m_squared_7c_style(n_pt, n_pr, k_S, sigma_eff,
                       eps_p, s_p, K_p):
    """7c's mass formula with corrected kinematics, σ_eff replacing σ_t.

    m²(k_S) = m_Ma² + 4·(ℏc)²·k_S² + 2·k_S·σ_eff·n_pt·ℏc
    """
    m_ma = m_Ma(n_pt, n_pr, eps_p, s_p, K_p)
    m_S2_kin = A_KINETIC * k_S ** 2
    cross = 2 * k_S * sigma_eff * n_pt * HBAR_C_MEV_FM
    return m_ma ** 2 + m_S2_kin + cross


def m_at_separation(r, n_pt, n_pr, sigma_eff, eps_p, s_p, K_p):
    if r < 1e-6:
        return float('inf')
    k_S = 1.0 / r
    m2 = m_squared_7c_style(n_pt, n_pr, k_S, sigma_eff, eps_p, s_p, K_p)
    if m2 <= 0:
        return float('nan')
    return math.sqrt(m2)


def compute_V_of_r(p, sigma_aS, sigma_at, n_pt, n_pr,
                   r_values, m_constituents_sum,
                   use_full_schur=True):
    """V(r) = m(r) - m_constituents_sum.

    use_full_schur: if True, extract σ_eff from the full inverse metric
                    (captures higher-order corrections).  If False, use
                    leading-order σ_eff = σ_ta · σ_aS.
    """
    if use_full_schur:
        sigma_eff = schur_effective_sigma_pS(p, sigma_aS, sigma_at)
    else:
        sigma_eff = schur_leading_order_sigma_pS(sigma_aS, p.sigma_ta)

    Vs = []
    for r in r_values:
        m = m_at_separation(r, n_pt, n_pr, sigma_eff,
                            p.eps_p, p.s_p, p.K_p if hasattr(p, 'K_p') else None)
        Vs.append(m - m_constituents_sum)
    return np.array(Vs), sigma_eff


# ─── Locus compensation formula from Phase 8b ───────────────────────

def sigma_at_on_locus(sigma_aS, sigma_at_baseline=None, c=18.3):
    """σ_at(σ_aS) = 4πα · (1 + c·σ_aS²)^(-1/2)  per F8b.3."""
    if sigma_at_baseline is None:
        sigma_at_baseline = FOUR_PI * ALPHA
    return sigma_at_baseline / math.sqrt(1 + c * sigma_aS ** 2)


# ─── Configurations ─────────────────────────────────────────────────

# R64 Point B p-sheet (the calibration used for Phase 7c's σ_t = -116)
EPS_P_R64_B = 0.2052
S_P_R64_B = 0.0250
K_P_R64_B = 63.629

M_P = 938.272
M_N = 939.565

# Two-body compound winding for nucleon pairs (R64 picture):
# proton = (3, +2), neutron = (3, -2); joint compound n_pt = 6.
# For R60 model-F picture (proton at (1, 3)): joint compound n_pt = 2.
# We test BOTH so we can compare to Phase 7c (R64 picture) AND R60
# Track 9 baseline.

CONFIGS_R64 = {
    "pp (R64)": dict(n_pt=6, n_pr=4, m_constituents_sum=2 * M_P,
                     coulomb=(1, 1)),
    "pn (R64)": dict(n_pt=6, n_pr=0, m_constituents_sum=M_P + M_N,
                     coulomb=(1, 0)),
    "nn (R64)": dict(n_pt=6, n_pr=-4, m_constituents_sum=2 * M_N,
                     coulomb=(0, 0)),
}


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 8 Phase 8c (CORRECTED) — V(r) along universality locus")
    print("=" * 110)
    print()
    print("Kinematic correction: A_kinetic = 4·(ℏc)² for two-body relative")
    print("motion, replacing earlier (2π·ℏc)² which inflated the kinetic")
    print(f"term by (2π)²/4 = π² ≈ {math.pi**2:.3f}.")
    print()

    p = track9_params()
    sigma_at_baseline = p.sigma_at
    sigma_ta_baseline = p.sigma_ta

    # Override p-sheet params to R64 Point B (the parameters Phase 7c used)
    p_R64 = p.copy_with(eps_p=EPS_P_R64_B, s_p=S_P_R64_B)
    p_R64.K_p = K_P_R64_B  # attach K_p for our formula

    print(f"Baseline params:")
    print(f"  R60 model-F: σ_ta = √α = {sigma_ta_baseline:.6f}")
    print(f"  R60 model-F: σ_at = 4πα = {sigma_at_baseline:.6f}")
    print(f"  R64 Point B: ε_p = {EPS_P_R64_B}, s_p = {S_P_R64_B}, "
          f"K_p = {K_P_R64_B}")
    print()
    print(f"Phase 7c reference (direct σ_pS_tube approach):")
    print(f"  σ_t = -116.1 (in 7-tensor units, dimensionless)")
    print(f"  Trough: depth -50.2 MeV at r = 1.135 fm")
    print()

    # ─── Part 1: Schur-effective σ along the locus ───
    print("=" * 80)
    print("Part 1 — Schur-effective σ_pS_tube along the universality locus")
    print("=" * 80)
    print()
    print(f"  {'σ_aS':>8s}  {'σ_at':>10s}  "
          f"{'σ_eff (full)':>14s}  {'σ_eff (LO)':>12s}  "
          f"{'σ_eff/σ_t,7c':>14s}")
    print("  " + "─" * 78)

    sigma_aS_test_values = [-0.30, -0.20, -0.10, -0.05, -0.025, -0.01, 0.0,
                            0.01, 0.025, 0.05, 0.10, 0.20, 0.30]

    schur_table = []
    for s_aS in sigma_aS_test_values:
        s_at = sigma_at_on_locus(s_aS, sigma_at_baseline)
        sigma_eff_full = schur_effective_sigma_pS(p_R64, s_aS, s_at)
        sigma_eff_LO = schur_leading_order_sigma_pS(s_aS, sigma_ta_baseline)
        ratio_to_7c = sigma_eff_full / (-116.1)
        print(f"  {s_aS:>+8.3f}  {s_at:>10.6f}  "
              f"{sigma_eff_full:>+14.6f}  {sigma_eff_LO:>+12.6f}  "
              f"{ratio_to_7c:>+14.5f}")
        schur_table.append({
            'sigma_aS': s_aS,
            'sigma_at': s_at,
            'sigma_eff_full_schur': sigma_eff_full,
            'sigma_eff_leading_order': sigma_eff_LO,
            'ratio_to_phase7c_sigma_t': ratio_to_7c,
        })
    print()
    print("  Phase 7c reference: σ_t = -116.1.  Phase 8c σ_eff at locus")
    print("  boundary (σ_aS = ±0.30) is several orders of magnitude smaller.")
    print()

    # ─── Part 2: V(r) at representative locus points ───
    print("=" * 80)
    print("Part 2 — V(r) at representative locus points (corrected kinematics)")
    print("=" * 80)
    print()

    r_values = np.logspace(-1, 1.0, 200)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: pn V(r) along locus, full range
    ax = axes[0, 0]
    locus_to_plot = [-0.30, -0.20, -0.10, -0.05, 0.0, +0.05, +0.10, +0.20, +0.30]
    for s_aS in locus_to_plot:
        s_at = sigma_at_on_locus(s_aS, sigma_at_baseline)
        cfg = CONFIGS_R64["pn (R64)"]
        V, sigma_eff = compute_V_of_r(
            p_R64, s_aS, s_at,
            cfg['n_pt'], cfg['n_pr'],
            r_values, cfg['m_constituents_sum'],
            use_full_schur=True,
        )
        ax.plot(r_values, V, label=f'σ_aS = {s_aS:+.2f}', linewidth=1.0)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('V(r) (MeV)')
    ax.set_title('pn V(r) along locus — corrected kinematics')
    ax.set_xlim(0.3, 5)
    ax.set_ylim(-200, 200)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc='upper right')

    # Panel 2: V(r) at σ_aS = -0.30 (locus boundary, max attractive)
    ax = axes[0, 1]
    s_aS_max = -0.30
    s_at_max = sigma_at_on_locus(s_aS_max, sigma_at_baseline)
    print(f"At σ_aS = {s_aS_max} (locus boundary, max negative):")
    print(f"  σ_at on locus = {s_at_max:.6f}")
    print()
    print(f"  {'config':<12s}  {'σ_eff':>12s}  {'V_min (MeV)':>12s}  "
          f"{'r_min (fm)':>10s}")
    for label, cfg in CONFIGS_R64.items():
        V, sigma_eff = compute_V_of_r(
            p_R64, s_aS_max, s_at_max,
            cfg['n_pt'], cfg['n_pr'],
            r_values, cfg['m_constituents_sum'],
            use_full_schur=True,
        )
        # Find minimum in physical range
        mask = (r_values >= 0.3) & (r_values <= 10)
        V_phys = V[mask]
        r_phys = r_values[mask]
        idx = np.nanargmin(V_phys)
        ax.plot(r_values, V, label=f'{label}', linewidth=1.5)
        print(f"  {label:<12s}  {sigma_eff:>+12.6f}  {V_phys[idx]:>+12.3f}  "
              f"{r_phys[idx]:>+10.3f}")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('V(r) (MeV)')
    ax.set_title(f'V(r) at σ_aS = {s_aS_max} (locus boundary)')
    ax.set_xlim(0.3, 5)
    ax.set_ylim(-100, 200)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)
    print()

    # Panel 3: V(r) at σ_aS = -0.05 (small magnitude on locus)
    ax = axes[1, 0]
    s_aS_small = -0.05
    s_at_small = sigma_at_on_locus(s_aS_small, sigma_at_baseline)
    print(f"At σ_aS = {s_aS_small} (small magnitude, ~α-scale):")
    print(f"  σ_at on locus = {s_at_small:.6f}")
    print()
    print(f"  {'config':<12s}  {'σ_eff':>12s}  {'V_min (MeV)':>12s}  "
          f"{'r_min (fm)':>10s}")
    for label, cfg in CONFIGS_R64.items():
        V, sigma_eff = compute_V_of_r(
            p_R64, s_aS_small, s_at_small,
            cfg['n_pt'], cfg['n_pr'],
            r_values, cfg['m_constituents_sum'],
            use_full_schur=True,
        )
        mask = (r_values >= 0.3) & (r_values <= 10)
        V_phys = V[mask]
        r_phys = r_values[mask]
        idx = np.nanargmin(V_phys)
        ax.plot(r_values, V, label=f'{label}', linewidth=1.5)
        print(f"  {label:<12s}  {sigma_eff:>+12.6f}  {V_phys[idx]:>+12.3f}  "
              f"{r_phys[idx]:>+10.3f}")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('V(r) (MeV)')
    ax.set_title(f'V(r) at σ_aS = {s_aS_small} (small)')
    ax.set_xlim(0.3, 5)
    ax.set_ylim(-50, 200)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)
    print()

    # Panel 4: depth and position vs σ_aS (negative, attractive side)
    ax = axes[1, 1]
    cfg = CONFIGS_R64["pn (R64)"]
    sigma_sweep = np.linspace(-0.30, -0.001, 60)
    depths = []
    positions = []
    for s_aS in sigma_sweep:
        s_at = sigma_at_on_locus(s_aS, sigma_at_baseline)
        V, sigma_eff = compute_V_of_r(
            p_R64, s_aS, s_at,
            cfg['n_pt'], cfg['n_pr'],
            r_values, cfg['m_constituents_sum'],
            use_full_schur=True,
        )
        mask = (r_values >= 0.3) & (r_values <= 10)
        V_phys = V[mask]
        r_phys = r_values[mask]
        if np.any(np.isfinite(V_phys)):
            idx = np.nanargmin(V_phys)
            depths.append(V_phys[idx])
            positions.append(r_phys[idx])
        else:
            depths.append(np.nan)
            positions.append(np.nan)

    ax2 = ax.twinx()
    line1 = ax.plot(sigma_sweep, depths, 'b-', linewidth=1.5,
                    label='trough depth (V_min)')
    line2 = ax2.plot(sigma_sweep, positions, 'r--', linewidth=1.5,
                     label='trough position (r_min)')
    ax.set_xlabel('σ_aS')
    ax.set_ylabel('V_min (MeV)', color='blue')
    ax2.set_ylabel('r_min (fm)', color='red')
    ax.set_title('Trough depth & position along negative-σ locus (pn)')
    ax.grid(alpha=0.3)
    ax.axhline(-50, color='blue', linestyle=':', alpha=0.5,
               label='7c reference: -50 MeV')
    ax2.axhline(1.0, color='red', linestyle=':', alpha=0.5)
    lines = line1 + line2
    labs = [l.get_label() for l in lines]
    ax.legend(lines, labs, fontsize=9, loc='lower right')

    plt.tight_layout()
    fig_path = out_dir / "track8_phase8c_potential_curves.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {fig_path}")
    print()

    # ─── Part 3: What σ_aS would be needed to match 7c? ───
    print("=" * 80)
    print("Part 3 — What σ_aS would match Phase 7c's σ_t = -116?")
    print("=" * 80)
    print()
    sigma_t_target = -116.1
    # σ_eff_LO = σ_ta · σ_aS  →  σ_aS = σ_eff / σ_ta
    sigma_aS_required = sigma_t_target / sigma_ta_baseline
    print(f"  Phase 7c σ_t target: {sigma_t_target}")
    print(f"  σ_ta (R60 baseline): {sigma_ta_baseline:.6f}")
    print(f"  Required σ_aS = σ_t / σ_ta = "
          f"{sigma_aS_required:+.2f}")
    print(f"  Phase 8a/8b signature band: ±0.425 (σ_aS), locus boundary ±0.31")
    print()
    print(f"  Required σ_aS is **{abs(sigma_aS_required) / 0.31:.0f}× larger**")
    print(f"  than the locus boundary; the metric signature breaks long")
    print(f"  before reaching this magnitude.")
    print()
    print(f"  This is the structural barrier: aleph-mediation suppresses the")
    print(f"  effective coupling by σ_ta = √α ≈ 0.085, so any locus-permitted")
    print(f"  σ_aS produces σ_eff at most ~0.085·0.31 ≈ 0.026 — over 4000×")
    print(f"  smaller than 7c's σ_t.")
    print()

    # ─── CSV ──────────────────────────────────────────────────────
    csv_path = out_dir / "track8_phase8c_potential_curves.csv"
    csv_rows = []
    for s_aS in sigma_aS_test_values:
        s_at = sigma_at_on_locus(s_aS, sigma_at_baseline)
        for label, cfg in CONFIGS_R64.items():
            V, sigma_eff = compute_V_of_r(
                p_R64, s_aS, s_at,
                cfg['n_pt'], cfg['n_pr'],
                r_values, cfg['m_constituents_sum'],
                use_full_schur=True,
            )
            for i, r in enumerate(r_values):
                csv_rows.append({
                    'config': label,
                    'sigma_aS': s_aS,
                    'sigma_at': s_at,
                    'sigma_eff': sigma_eff,
                    'r_fm': r,
                    'V_MeV': V[i],
                })
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
        w.writeheader()
        w.writerows(csv_rows)
    print(f"  CSV: {csv_path}")

    # Schur table CSV
    schur_csv = out_dir / "track8_phase8c_schur_coupling.csv"
    with open(schur_csv, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(schur_table[0].keys()))
        w.writeheader()
        w.writerows(schur_table)
    print(f"  CSV: {schur_csv}")

    # ─── Verdict ──────────────────────────────────────────────────
    print()
    print("=" * 110)
    print("VERDICT — Phase 8c (corrected)")
    print("=" * 110)
    print()
    cfg = CONFIGS_R64["pn (R64)"]
    s_at_max = sigma_at_on_locus(-0.30, sigma_at_baseline)
    sigma_eff_max = schur_effective_sigma_pS(p_R64, -0.30, s_at_max)

    # Ma-side offset at r → ∞
    m_Ma_pn = m_Ma(cfg['n_pt'], cfg['n_pr'],
                    EPS_P_R64_B, S_P_R64_B, K_P_R64_B)
    Ma_offset = m_Ma_pn - cfg['m_constituents_sum']

    # Analytical trough from V(r) = A/(2M·r²) + B/(2M·r) (linearized)
    # r_min = 2A/|B|;   depth = B²/(8·A·M_total) (relative to V(∞))
    M_total = cfg['m_constituents_sum']
    A = A_KINETIC
    B = 2 * sigma_eff_max * cfg['n_pt'] * HBAR_C_MEV_FM
    if B < 0:
        r_min_analytical = 2 * A / abs(B)
        depth_analytical = -(B ** 2) / (8 * A * M_total)
    else:
        r_min_analytical = float('inf')
        depth_analytical = 0.0

    print(f"  σ_aS at locus boundary (-0.30) gives σ_eff = {sigma_eff_max:.4f}")
    print(f"    (Phase 7c had σ_t = {sigma_t_target}; ratio = "
          f"{sigma_eff_max/sigma_t_target:.5f})")
    print()
    print(f"  Two distinct contributions to V(r) for the pn channel:")
    print()
    print(f"  (a) Ma-side asymptotic offset (independent of σ_aS):")
    print(f"      m_Ma(pn at R64 Point B) − (m_p + m_n) = "
          f"{Ma_offset:+.2f} MeV")
    print(f"      This is the F7a.2 finding — R64 Point B's compound (6, 0)")
    print(f"      sits 17 MeV below the additive sum at infinite separation.")
    print(f"      It's a Ma-side feature, not a strong-force coupling effect.")
    print()
    print(f"  (b) Aleph-mediated cross-coupling contribution to V(r):")
    print(f"      Analytical trough position r_min = 2A/|B| = "
          f"{r_min_analytical:.1f} fm")
    print(f"      Analytical trough depth ΔV_min = "
          f"{depth_analytical * 1e6:.3f} μeV")
    print(f"      Phase 7c reference: r_min = 1.135 fm, depth = −50.2 MeV.")
    print()
    print(f"  The aleph-mediated trough sits at "
          f"{r_min_analytical/1.135:.0f}× the position")
    print(f"  of Phase 7c's, with depth "
          f"{abs(depth_analytical)/50.2 * 1e6:.2f} ppb of Phase 7c's.")
    print(f"  At physical r ≤ 10 fm, V(r) is essentially the Ma-side offset")
    print(f"  ({Ma_offset:+.2f} MeV) plus a negligible cross-coupling correction.")
    print()
    print(f"  STRUCTURAL CONCLUSION: aleph-mediation cannot deliver strong-")
    print(f"  force coupling at locus-permitted σ_aS magnitudes.")
    print(f"  The Schur suppression factor σ_ta = √α ≈ 0.085 means")
    print(f"  σ_eff_max ≈ {sigma_eff_max:.3f} on the locus, vs Phase 7c's σ_t = "
          f"{sigma_t_target}.")
    print(f"  To match Phase 7c, σ_aS would need {abs(sigma_aS_required):.0f}, ")
    print(f"  ~4400× outside the signature band [−0.425, +0.425].")
    print()
    print(f"  This confirms Q135's third reading:")
    print(f"  - Aleph mediates EM at α-magnitude (Coulomb via σ_at, magnetic")
    print(f"    via σ_aS at α-magnitude — completes EM, MaSt's missing piece).")
    print(f"  - Strong force is structurally NOT a metric off-diagonal.")
    print(f"    Pivots to propagator-based formalism (R64 pool m, Route B):")
    print(f"    massive mediator (meson-analog), 1/(k² + m²) propagator,")
    print(f"    Yukawa form falls out structurally.")
    print(f"  - Cross-sheet σ entries and direct sheet-S entries stay zero")
    print(f"    by structure (Q135's hub-and-spoke principle).")


if __name__ == "__main__":
    main()
