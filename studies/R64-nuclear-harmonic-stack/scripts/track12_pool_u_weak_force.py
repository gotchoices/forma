"""
R64 pool item u — Weak force from e-sheet → S coupling.

Tests whether activating σ_eS_tube + e-sheet H2 prescription (analogous
to Track 11's strong-force discovery on the p-sheet) delivers a
weak-force-like potential.

The H2 coefficient generalizes by sheet substitution:
    b_e = -G⁻¹[E_TUBE, t] / G⁻¹[ALEPH, t]

At R60 model-F baseline the inverse-metric column [*, t] was:
    G⁻¹[ALEPH, t]   = +0.16911
    G⁻¹[P_TUBE, t]  = +0.30759   →  b_p = -1.81892
    G⁻¹[E_TUBE, t]  = -0.30759   →  b_e = +1.81892
    G⁻¹[NU_TUBE, t] = -0.30759   →  b_ν = +1.81892

So |b_e| = |b_p| = √α/k = 1.819, but signs differ due to sheet-sign
conventions (sign_e=+1, sign_p=-1, sign_ν=+1).

Outputs:
  outputs/track12_pool_u_weak_e_sheet.csv
  outputs/track12_pool_u_weak_potential.png
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
    alpha_coulomb, mode_6_to_11, signature_ok,
    ALPHA, FOUR_PI, HBAR_C_MEV_FM, MA_SLICE,
    I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING, I_NU_TUBE, I_NU_RING,
    I_ALEPH, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import track9_params    # noqa: E402


# H2 coefficient for e-sheet (derived; opposite sign from p-sheet)
H2_E = +1.818920

# R64 Point B (proton sheet calibration; we keep this for cross-tests)
EPS_P_R64_B = 0.2052
S_P_R64_B = 0.0250
K_P_R64_B = 63.629

# e-sheet parameters from R60 model-F
EPS_E = 397.074
S_E = 2.004200
# K for e-sheet: kinematic prefactor that calibrates m_e at (1, 2).
# m_e = K_e · sqrt((1/eps_e)² + (2 - s_e)²) = 0.511 MeV at calibration.
def derive_K_e():
    bare = math.sqrt((1.0/EPS_E)**2 + (2.0 - S_E*1.0)**2)
    return 0.510999 / bare
K_E = derive_K_e()

A_KIN = 4.0 * HBAR_C_MEV_FM ** 2

M_E = 0.510999
M_MU = 105.658

# Universality test inventory (R64 inventory)
TEST_MODES = [
    ("electron",     (1, 2, 0, 0, 0, 0)),
    ("muon",         (1, 1, -2, -2, 0, 0)),
    ("R64 proton",   (0, 0, 0, 0, 3, +2)),
    ("R64 neutron",  (0, 0, 0, 0, 3, -2)),
    ("u quark",      (0, 0, 0, 0, 1, +2)),
    ("d quark",      (0, 0, 0, 0, 1, -2)),
]

EXPECTED_CHARGES = {
    "electron":      -1.0,
    "muon":          -1.0,
    "R64 proton":    +1.0,
    "R64 neutron":    0.0,
    "u quark":       +2/3,
    "d quark":       -1/3,
}


def f_charge(n_pt, n_pr):
    return n_pt / 6.0 + n_pr / 4.0


def alpha_A1(G, n6):
    G_inv = np.linalg.inv(G)
    n_et, n_er, n_νt, n_νr, n_pt, n_pr = n6
    n_eff_p = f_charge(n_pt, n_pr)
    n_ma = np.zeros(6)
    n_ma[I_E_TUBE  - 1] = n_et
    n_ma[I_E_RING  - 1] = n_er
    n_ma[I_NU_TUBE - 1] = n_νt
    n_ma[I_NU_RING - 1] = n_νr
    n_ma[I_P_TUBE  - 1] = n_eff_p
    n_ma[I_P_RING  - 1] = 0.0
    Q = float((n_ma @ G_inv[MA_SLICE, I_T]) * (-G_inv[I_T, I_T]))
    return Q * Q / FOUR_PI


def build_metric_with_e_H2(p, sigma_eS_tube):
    """R64 metric with σ_eS_tube + e-sheet H2 (σ_aS = +1.819·σ_eS_tube)."""
    G = build_aug_metric(p).copy()
    sigma_aS = H2_E * sigma_eS_tube
    for s_idx in (I_SX, I_SY, I_SZ):
        G[I_E_TUBE, s_idx] += sigma_eS_tube
        G[s_idx, I_E_TUBE] += sigma_eS_tube
        G[I_ALEPH, s_idx] += sigma_aS
        G[s_idx, I_ALEPH] += sigma_aS
    return G


def schur_eff_eS_tube(G):
    """Schur σ_eff_eS_tube = -G⁻¹[E_TUBE, S_x] · g_ee · g_SS."""
    G_inv = np.linalg.inv(G)
    g_ee = G[I_E_TUBE, I_E_TUBE]
    g_SS = G[I_SX, I_SX]
    return float(-G_inv[I_E_TUBE, I_SX] * g_ee * g_SS)


def universality_spread(G):
    devs = []
    for label, n6 in TEST_MODES:
        q_exp = EXPECTED_CHARGES[label]
        if abs(q_exp) < 1e-10:
            continue
        a = alpha_A1(G, n6)
        ratio = a / ALPHA
        expected = q_exp ** 2
        devs.append(abs(ratio / expected - 1.0))
    return max(devs) if devs else 0.0


def find_signature_edge(p, sigma_max=0.5, n_steps=50001):
    sigmas = np.linspace(0.0, sigma_max, n_steps)
    last_ok = 0.0
    for s in sigmas:
        G = build_metric_with_e_H2(p, s)
        if signature_ok(G):
            last_ok = s
        else:
            break
    return last_ok


# ── e-sheet two-body mass formula ────────────────────────────────────

def m_Ma_e(n_et, n_er, eps=EPS_E, s=S_E, K=K_E):
    return K * math.sqrt((n_et / eps) ** 2 + (n_er - s * n_et) ** 2)


def m_compound_e(r, n_et, n_er, se_eS_tube, eps=EPS_E, s=S_E, K=K_E):
    if r < 1e-12:
        return float('inf')
    k_S = 1.0 / r
    m_ma = m_Ma_e(n_et, n_er, eps, s, K)
    cross = 2 * k_S * se_eS_tube * n_et * HBAR_C_MEV_FM
    m2 = m_ma ** 2 + A_KIN * k_S ** 2 + cross
    if m2 <= 0:
        return float('nan')
    return math.sqrt(m2)


def compute_V(n_et, n_er, m_sum, se_eS_tube,
              r_lo=0.001, r_hi=10.0, n_pts=3000, log=True):
    if log:
        rs = np.logspace(math.log10(r_lo), math.log10(r_hi), n_pts)
    else:
        rs = np.linspace(r_lo, r_hi, n_pts)
    Es = np.array([
        m_compound_e(r, n_et, n_er, se_eS_tube) - m_sum for r in rs
    ])
    valid = ~np.isnan(Es)
    if not valid.any():
        return None, None, None, None, None
    rs_v = rs[valid]
    Es_v = Es[valid]
    i_min = int(np.argmin(Es_v))
    return rs_v[i_min], Es_v[i_min], Es_v[-1], rs_v, Es_v


def fit_yukawa(rs, Vs):
    """Fit V(r) ≈ -A·exp(-m·r)/r via log-linearization on attractive segment."""
    valid = (Vs < 0) & (rs > 0)
    if valid.sum() < 5:
        return None, None
    rs_v = rs[valid]
    Vs_v = Vs[valid]
    # ln(-V·r) = ln(A) - m·r
    y = np.log(-Vs_v * rs_v)
    finite = np.isfinite(y)
    if finite.sum() < 5:
        return None, None
    p = np.polyfit(rs_v[finite], y[finite], 1)
    m_fit = -p[0]   # in fm⁻¹
    A_fit = math.exp(p[1])
    # Convert m_fit (fm⁻¹) to mass via m_MeV = m_fit · ℏc ≈ m_fit · 197.3
    m_MeV = m_fit * HBAR_C_MEV_FM
    return A_fit, m_MeV


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    p = track9_params().copy_with(eps_p=EPS_P_R64_B, s_p=S_P_R64_B)

    print("=" * 95)
    print("R64 pool item u — Weak force from e-sheet → S coupling")
    print("=" * 95)
    print()
    print(f"  Working point: R64 Point B (p-sheet) + R60 model-F (e-sheet)")
    print(f"  e-sheet H2 coefficient: b_e = +{H2_E:.6f}")
    print(f"    (derived: b_e = -√α/k = -G⁻¹[E_TUBE,t]/G⁻¹[ALEPH,t])")
    print(f"    (positive sign because sign_e = +1; b_p = -{H2_E:.6f})")
    print(f"  K_e (kinematic prefactor for e-sheet, derived): {K_E:.4f} MeV")
    print(f"  e-sheet (ε_e, s_e) = ({EPS_E}, {S_E}) — R60 model-F values")
    print()

    # ── Step 1: Find signature edge under e-sheet H2 ─────────────────
    print("=" * 95)
    print("Step 1: Find e-sheet signature edge")
    print("=" * 95)
    edge = find_signature_edge(p)
    print(f"  Signature edge: σ_eS_tube = {edge:.6f}")
    print()

    # ── Step 2: σ_eff_eS_tube vs σ_eS_tube ──────────────────────────
    print("=" * 95)
    print("Step 2: σ_eff_eS_tube and A1 universality across the band")
    print("=" * 95)
    print(f"  {'σ_eS_tube':>12s}  {'sig OK':>7s}  {'σ_eff_eS_tube':>14s}  "
          f"{'A1 spread':>11s}")
    print("  " + "─" * 60)

    rows = []
    test_sigmas = [0.0, edge*0.25, edge*0.50, edge*0.75, edge*0.90,
                   edge*0.95, edge*0.99, edge]
    for s in test_sigmas:
        G = build_metric_with_e_H2(p, s)
        ok = signature_ok(G)
        if not ok:
            continue
        se = schur_eff_eS_tube(G)
        spread = universality_spread(G)
        print(f"  {s:>12.6f}  {'YES':>7s}  {se:>+14.4f}  {spread:>11.3e}")
        rows.append({
            "sigma_eS_tube": s,
            "signature_ok": ok,
            "sigma_eff_eS_tube": se,
            "A1_spread": spread,
        })
    print()

    # ── Step 3: V(r) at multiple σ_eff_eS_tube magnitudes ───────────
    print("=" * 95)
    print("Step 3: V(r) for ee, eμ, μμ at multiple σ_eff_eS_tube magnitudes")
    print("=" * 95)
    print()
    # Target σ_eff magnitudes to scan
    target_se_values = []
    # Include both signs and a range
    for s_pS in [-edge*0.95, -edge*0.5, -edge*0.1,
                 +edge*0.1, +edge*0.5, +edge*0.95]:
        G = build_metric_with_e_H2(p, s_pS)
        if signature_ok(G):
            se = schur_eff_eS_tube(G)
            target_se_values.append((s_pS, se))

    # Also try the σ_eS_tube giving large σ_eff (analog to strong)
    for label, n_et, n_er, m_sum in [
        ("ee",  2,  4, 2 * M_E),
        ("eμ",  2,  3, M_E + M_MU),
        ("μμ",  2,  2, 2 * M_MU),
    ]:
        print(f"  Channel {label}: n_et={n_et}, n_er={n_er}, m_sum={m_sum:.3f} MeV")
        print(f"    {'σ_eS_tube':>12s}  {'σ_eff_eS':>10s}  "
              f"{'r_min (fm)':>11s}  {'V_min (MeV)':>11s}  {'V(10 fm)':>10s}")
        for s_input, se in target_se_values:
            r_m, V_m, V_inf, _, _ = compute_V(n_et, n_er, m_sum, se,
                                                r_lo=0.001, r_hi=10.0)
            if r_m is None:
                continue
            print(f"    {s_input:>+12.6f}  {se:>+10.4f}  "
                  f"{r_m:>11.4f}  {V_m:>+11.4f}  {V_inf:>+10.4f}")
        print()

    # ── Step 4: Yukawa fit on the most-attractive case ──────────────
    print("=" * 95)
    print("Step 4: Yukawa profile fit V(r) ≈ -A·exp(-m·r)/r")
    print("=" * 95)
    # Pick the largest |σ_eff| with attractive (negative) cross term.
    # Cross term sign: 2·k_S·σ_eff·n_et·ℏc.  n_et = 2 for ee; need σ_eff < 0.
    s_negative = -edge * 0.99
    G_neg = build_metric_with_e_H2(p, s_negative)
    se_neg = schur_eff_eS_tube(G_neg)
    print(f"  Operating point: σ_eS_tube = {s_negative:+.6f}")
    print(f"  σ_eff_eS_tube = {se_neg:+.4f}")
    print()

    for label, n_et, n_er, m_sum in [
        ("ee", 2, 4, 2 * M_E),
        ("μμ", 2, 2, 2 * M_MU),
    ]:
        r_m, V_m, V_inf, rs, Vs = compute_V(n_et, n_er, m_sum, se_neg,
                                             r_lo=0.0001, r_hi=10.0,
                                             n_pts=5000)
        if r_m is None:
            print(f"  {label}: V(r) all NaN — m² goes negative")
            continue
        print(f"  {label}: r_min = {r_m:.4f} fm, V_min = {V_m:+.4f} MeV, "
              f"V(10 fm) = {V_inf:+.4f} MeV")
        # Fit Yukawa on attractive portion at r > r_min
        A_fit, m_MeV = fit_yukawa(rs[rs > r_m], Vs[rs > r_m])
        if A_fit is not None:
            print(f"    Yukawa fit: V(r) ≈ -{A_fit:.4f}·exp(-r·{m_MeV/HBAR_C_MEV_FM:.4f}/ℏc) / r")
            print(f"    Implied mediator mass: {m_MeV:.2f} MeV")
            print(f"    SM W± mass:            80,400 MeV")
            print(f"    Ratio (predicted/W):   {m_MeV/80400:.6f}")
        else:
            print(f"    Yukawa fit: insufficient attractive segment")
        print()

    # ── Step 5: Plot V(r) curves ────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    for ax, log in zip(axes, [False, True]):
        for label, n_et, n_er, m_sum in [
            ("ee", 2, 4, 2 * M_E),
            ("μμ", 2, 2, 2 * M_MU),
        ]:
            _, _, _, rs, Vs = compute_V(n_et, n_er, m_sum, se_neg,
                                          r_lo=0.0001, r_hi=5.0, n_pts=2000)
            if rs is not None:
                ax.plot(rs, Vs, label=label)
        ax.axhline(0, color='black', linestyle='--', alpha=0.4)
        ax.set_xlabel("r (fm)")
        ax.set_ylabel("V(r) (MeV)")
        ax.legend()
        ax.set_title(f"V(r) under σ_eS_tube + e-H2 active "
                     f"(σ_eff_eS_tube = {se_neg:+.2f})")
        if log:
            ax.set_xscale("log")
        ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "track12_pool_u_weak_potential.png", dpi=120)
    plt.close()
    print(f"  PNG: {out_dir / 'track12_pool_u_weak_potential.png'}")

    # ── CSV ─────────────────────────────────────────────────────────
    csv_path = out_dir / "track12_pool_u_weak_e_sheet.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"  CSV: {csv_path}")
    print()

    # ── Verdict ─────────────────────────────────────────────────────
    print("=" * 95)
    print("VERDICT — pool item u")
    print("=" * 95)
    print()
    G_edge = build_metric_with_e_H2(p, edge * 0.99)
    se_edge = schur_eff_eS_tube(G_edge)
    spread_edge = universality_spread(G_edge)
    print(f"  Signature edge:                      σ_eS_tube = {edge:.6f}")
    print(f"  σ_eff_eS_tube near edge:             {se_edge:+.4f}")
    print(f"  A1 universality at edge:             {spread_edge:.3e}")
    print()


if __name__ == "__main__":
    main()
