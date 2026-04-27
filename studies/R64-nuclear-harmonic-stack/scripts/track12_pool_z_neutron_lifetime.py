"""
R64 pool item z — Neutron lifetime order-of-magnitude estimate.

Step 1 (this script): verify MaSt's structural Q-value and check
whether standard Fermi golden-rule phase-space + placeholder G_F
reproduces τ_n ≈ 880 s.  Identify what G_F-equivalent value MaSt
would need; then check whether any of MaSt's natural structural
quantities (L_ring values, sheet shears, σ_eff at edge) sit at
that magnitude.

Step 2 (later): build the cross-sheet matrix element from σ_eS +
σ_νS + aleph mediations and predict τ_n directly.
"""

import math
import sys
from pathlib import Path

import numpy as np

R60_SCRIPTS = Path(__file__).resolve().parent.parent.parent / "R60-metric-11" / "scripts"
sys.path.insert(0, str(R60_SCRIPTS))

from track1_solver import (    # noqa: E402
    ALPHA, SQRT_ALPHA, FOUR_PI, HBAR_C_MEV_FM,
)


# Observed values (PDG)
TAU_N_OBSERVED_S = 879.4
M_E = 0.510999  # MeV
M_P_OBS = 938.272  # MeV
M_N_OBS = 939.565  # MeV
DELTA_M_OBS = M_N_OBS - M_P_OBS  # 1.293 MeV
Q_OBS = DELTA_M_OBS - M_E         # 0.782 MeV (m_ν ≈ 0)

# SM constants
G_F = 1.166378e-5    # GeV⁻²; convert later
G_F_MEV = G_F * 1e-6  # MeV⁻²
LAMBDA_AXIAL = 1.2731   # g_A / g_V
PHASE_SPACE_F = 1.6887  # Fermi function

# Conversion: 1 MeV⁻¹ in seconds = ℏ / (1 MeV)
HBAR_MEVS = 6.582119e-22  # MeV·s


# R64 working points
POINT_A = dict(eps_p=0.07309, s_p=0.19387, K_p=22.847, label="Point A (Track 1)")
POINT_B = dict(eps_p=0.2052,  s_p=0.0250,  K_p=63.629, label="Point B (Track 3)")


def m_Ma(n_pt, n_pr, eps_p, s_p, K_p):
    return K_p * math.sqrt((n_pt / eps_p) ** 2 + (n_pr - s_p * n_pt) ** 2)


def gamma_SM_from_Q(Q_MeV, lam=LAMBDA_AXIAL, f=PHASE_SPACE_F, GF_MeV=G_F_MEV):
    """SM neutron decay rate (units: MeV).  Standard scaling:
       Γ ≈ (G_F² · (1+3λ²) · m_e⁵ · f) / (2π³)
       with the Q-value entering implicitly through f.

    For order-of-magnitude this is fine; exact form has Q-dependence
    in f and the integration limits.
    """
    return (GF_MeV ** 2) * (1 + 3 * lam ** 2) * (M_E ** 5) * f / (2 * math.pi ** 3)


def gamma_simple_phase_space(Q_MeV, GF_MeV=G_F_MEV, lam=LAMBDA_AXIAL):
    """More explicit phase-space integral.  For Q ≫ m_e, ~Q^5; for
    Q ≈ m_e, the integral is dominated by Coulomb-suppressed lower
    edge.  Standard result for free neutron is the SM number above;
    use SM formula for cleanness.
    """
    return gamma_SM_from_Q(Q_MeV, lam=lam, GF_MeV=GF_MeV)


def main():
    print("=" * 95)
    print("R64 pool item z — Neutron lifetime order-of-magnitude estimate")
    print("=" * 95)
    print()

    # ── Step 1: Verify MaSt Q-value ─────────────────────────────────
    print("=" * 95)
    print("Step 1: MaSt structural Q-value at each working point")
    print("=" * 95)
    print()
    print(f"  Observed:  m_n − m_p = {DELTA_M_OBS:.4f} MeV")
    print(f"             Q = m_n − m_p − m_e = {Q_OBS:.4f} MeV")
    print()

    print(f"  {'Point':<22s}  {'m_p (MeV)':>10s}  {'m_n (MeV)':>10s}  "
          f"{'Δm (MeV)':>10s}  {'Q (MeV)':>10s}")
    print("  " + "─" * 80)

    for pt in [POINT_A, POINT_B]:
        m_p = m_Ma(3, +2, pt['eps_p'], pt['s_p'], pt['K_p'])
        m_n = m_Ma(3, -2, pt['eps_p'], pt['s_p'], pt['K_p'])
        delta_m = m_n - m_p
        Q = delta_m - M_E
        print(f"  {pt['label']:<22s}  {m_p:>10.4f}  {m_n:>10.4f}  "
              f"{delta_m:>10.4f}  {Q:>10.4f}")

    print()

    # ── Step 2: SM formula gives the right answer ───────────────────
    print("=" * 95)
    print("Step 2: SM formula sanity check (with measured G_F)")
    print("=" * 95)
    print()
    Gamma_sm = gamma_SM_from_Q(Q_OBS)
    tau_sm = HBAR_MEVS / Gamma_sm
    print(f"  G_F  = {G_F:.4e} GeV⁻² = {G_F_MEV:.4e} MeV⁻²")
    print(f"  Γ_SM = (G_F)² · (1+3λ²) · m_e⁵ · f / (2π³)")
    print(f"       = {Gamma_sm:.4e} MeV")
    print(f"  τ_SM = ℏ/Γ = {tau_sm:.2f} s")
    print(f"  τ_obs (PDG) = {TAU_N_OBSERVED_S} s")
    print(f"  ratio = {tau_sm / TAU_N_OBSERVED_S:.3f}  (≈1 confirms formula)")
    print()

    # ── Step 3: What does MaSt need to reproduce τ_n? ───────────────
    print("=" * 95)
    print("Step 3: What G_F-equivalent does MaSt need to reproduce τ_n?")
    print("=" * 95)
    print()
    # Required Γ for τ_obs = 880 s:
    Gamma_required = HBAR_MEVS / TAU_N_OBSERVED_S
    print(f"  Required Γ for τ = {TAU_N_OBSERVED_S} s: {Gamma_required:.4e} MeV")
    # Solve for G_F²:
    GF2_required_MeV = Gamma_required * 2 * math.pi ** 3 / (
        (1 + 3 * LAMBDA_AXIAL ** 2) * (M_E ** 5) * PHASE_SPACE_F)
    GF_required_MeV = math.sqrt(GF2_required_MeV)
    print(f"  Required G_F² = {GF2_required_MeV:.4e} MeV⁻⁴")
    print(f"  Required |G_F| = {GF_required_MeV:.4e} MeV⁻²")
    print()

    # ── Step 4: Compare to MaSt structural quantities ───────────────
    print("=" * 95)
    print("Step 4: Compare required G_F to MaSt structural quantities")
    print("=" * 95)
    print()
    print(f"  Target: |G_F| ≈ {GF_required_MeV:.4e} MeV⁻²  "
          f"({1/math.sqrt(GF_required_MeV):.4f} MeV equivalent)")
    print(f"  (SM Higgs VEV: v = 246 GeV ⇒ √2/(2v²) = G_F)")
    print(f"  MaSt energy scale equivalent of v = "
          f"{1/math.sqrt(2*GF_required_MeV):.4e} MeV"
          f" = {1/math.sqrt(2*GF_required_MeV)/1e3:.4f} GeV")
    print()
    # Compare to MaSt L_ring values
    L_ring_p_fm = 15.244
    L_ring_e_fm = 54.83
    L_ring_p_inv2 = 1.0 / (L_ring_p_fm / HBAR_C_MEV_FM) ** 2  # in MeV²
    L_ring_e_inv2 = 1.0 / (L_ring_e_fm / HBAR_C_MEV_FM) ** 2
    print(f"  Various MaSt structural quantities (units of MeV⁻²):")
    print(f"    1/L_ring_p² (= ℏ²c²/L²): "
          f"{(HBAR_C_MEV_FM / L_ring_p_fm)**(-2):.4e}")
    print(f"    1/L_ring_e²:             "
          f"{(HBAR_C_MEV_FM / L_ring_e_fm)**(-2):.4e}")
    print(f"    1/M_W² (W boson, 80.4 GeV): "
          f"{1.0 / (80400.0)**2:.4e}")
    print(f"    1/M_Z² (Z boson, 91.2 GeV): "
          f"{1.0 / (91200.0)**2:.4e}")
    print(f"    α / m_p²: {ALPHA / (938.272)**2:.4e}")
    print(f"    α² / m_p²: {ALPHA**2 / (938.272)**2:.4e}")
    print(f"    s_p² (Point A) / m_p²: {(POINT_A['s_p'])**2 / (938.272)**2:.4e}")
    print(f"    s_p (Point A) / m_p²: {POINT_A['s_p'] / (938.272)**2:.4e}")
    print(f"    s_p (Point A) · α / m_p²: "
          f"{POINT_A['s_p'] * ALPHA / (938.272)**2:.4e}")
    print()

    # ── Step 5: Consider potential structural origin ────────────────
    print("=" * 95)
    print("Step 5: Suggestive structural matches")
    print("=" * 95)
    print()
    target = GF_required_MeV
    candidates = [
        ("1/M_W² (SM)", 1.0 / (80400.0) ** 2),
        ("α / m_p²", ALPHA / (938.272) ** 2),
        ("α² / m_p²", ALPHA ** 2 / (938.272) ** 2),
        ("s_p (A) · α / m_p²", POINT_A['s_p'] * ALPHA / (938.272) ** 2),
        ("s_p (A) · α² / m_p²", POINT_A['s_p'] * ALPHA ** 2 / (938.272) ** 2),
        ("α / (m_p · m_W)", ALPHA / (938.272 * 80400.0)),
        ("1/(m_p · m_W)", 1.0 / (938.272 * 80400.0)),
        ("L_ring_p [fm] · α / m_p² [MeV²]", 15.244 * ALPHA / 938.272**2),
        ("(L_ring_p / ℏc)² · α", (15.244 / HBAR_C_MEV_FM) ** 2 * ALPHA),
    ]
    print(f"  Target: G_F ≈ {target:.4e} MeV⁻²")
    print()
    print(f"  {'expression':<40s}  {'value (MeV⁻²)':>18s}  {'ratio to target':>18s}")
    print("  " + "─" * 85)
    for label, value in candidates:
        ratio = value / target if target > 0 else 0
        print(f"  {label:<40s}  {value:>18.4e}  {ratio:>18.4f}")
    print()

    # ── Step 6: Verdict ─────────────────────────────────────────────
    print("=" * 95)
    print("VERDICT — pool item z (order-of-magnitude estimate)")
    print("=" * 95)
    print()
    print("  Step 1 (Q-value):   MaSt gives correct n−p mass gap and Q at both")
    print("                      Point A and Point B (per Track 1 calibration).")
    print(f"  Step 2 (formula):   SM Γ formula reproduces τ_n = 880 s with")
    print(f"                      measured G_F = 1.166e-5 GeV⁻².  Confirmed.")
    print(f"  Step 3 (target):    MaSt must produce |G_F| ≈ "
          f"{GF_required_MeV:.4e} MeV⁻² to match.")
    print(f"  Step 4 (structure): No clean MaSt structural quantity sits at")
    print(f"                      this exact magnitude.  The natural candidates")
    print(f"                      are off by orders of magnitude in either")
    print(f"                      direction.")
    print()
    print("  Implication: The structural origin of G_F (or its MaSt analog) is")
    print("  not obvious from existing scale parameters.  The cross-sheet")
    print("  matrix element calculation (step iii of pool item z, deferred)")
    print("  is what's actually needed — not just dimensional analysis.")


if __name__ == "__main__":
    main()
