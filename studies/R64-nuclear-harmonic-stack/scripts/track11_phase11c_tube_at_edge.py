"""
R64 Track 11 Phase 11c — σ_pS_tube + H2 prescription at signature edge.

Tests whether the tube channel (charge-symmetric: n_pt = 6 for all
two-nucleon systems) delivers Phase 7c-class strong force when the
σ_eff_tube is measured at the precise signature edge (Phase 11a
methodology), not at "safe distance" as Phase 9c did.

H2 prescription: σ_aS = -1.819 · σ_pS_tube (preserves α universality;
derived in Phase 9b).

Outputs:
  outputs/track11_phase11c_tube_edge.csv
  outputs/track11_phase11c_potential_curves.png
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


# H2 prescription from Phase 9b
H2_COEFFICIENT = -1.818920

# R64 Point B
EPS_P_R64_B = 0.2052
S_P_R64_B = 0.0250
K_P_R64_B = 63.629

A_KIN = 4.0 * HBAR_C_MEV_FM ** 2
M_P, M_N = 938.272, 939.565

# Universality test inventory (R64-only, since A1 attribution is
# defined for R64 quark composition; R60 model-F's (1, 3) proton
# tuple is not a valid R64 quark composite under f(n_pt, n_pr)).
TEST_MODES = [
    ("electron",     (1, 2, 0, 0, 0, 0)),
    ("muon",         (1, 1, -2, -2, 0, 0)),
    ("R64 proton",   (0, 0, 0, 0, 3, +2)),
    ("R64 neutron",  (0, 0, 0, 0, 3, -2)),
    ("R64 deuteron", (0, 0, 0, 0, 6, 0)),
    ("R64 pp",       (0, 0, 0, 0, 6, +4)),
    ("R64 nn",       (0, 0, 0, 0, 6, -4)),
    ("u quark",      (0, 0, 0, 0, 1, +2)),
    ("d quark",      (0, 0, 0, 0, 1, -2)),
]

# Expected charge in units of e (for A1 attribution rule)
EXPECTED_CHARGES = {
    "electron":      -1.0,
    "muon":          -1.0,
    "R64 proton":    +1.0,
    "R64 neutron":    0.0,
    "R64 deuteron":  +1.0,
    "R64 pp":        +2.0,
    "R64 nn":         0.0,
    "u quark":       +2/3,
    "d quark":       -1/3,
}


def f_charge(n_pt: int, n_pr: int) -> float:
    """A1 charge function: n_pt/6 + n_pr/4 (signed quark electric charge)."""
    return n_pt / 6.0 + n_pr / 4.0


def alpha_A1(G: np.ndarray, n6: tuple) -> float:
    """A1 attribution: project p-sheet through f(n_pt, n_pr) onto tube row."""
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
    ma_t_col = G_inv[MA_SLICE, I_T]
    Q = float((n_ma @ ma_t_col) * (-G_inv[I_T, I_T]))
    return Q * Q / FOUR_PI


def build_metric_with_H2(p, sigma_pS_tube: float):
    """R64 metric with σ_pS_tube and H2 companion σ_aS = -1.819·σ_pS_tube."""
    G = build_aug_metric(p).copy()
    sigma_aS = H2_COEFFICIENT * sigma_pS_tube
    for s_idx in (I_SX, I_SY, I_SZ):
        G[I_P_TUBE, s_idx] += sigma_pS_tube
        G[s_idx, I_P_TUBE] += sigma_pS_tube
        G[I_ALEPH, s_idx] += sigma_aS
        G[s_idx, I_ALEPH] += sigma_aS
    return G


def schur_eff_tube(G: np.ndarray) -> float:
    """Schur σ_eff_tube = -G⁻¹[p_t, S_x] · g_pp · g_SS."""
    G_inv = np.linalg.inv(G)
    g_pp = G[I_P_TUBE, I_P_TUBE]
    g_SS = G[I_SX, I_SX]
    return float(-G_inv[I_P_TUBE, I_SX] * g_pp * g_SS)


def schur_eff_ring(G: np.ndarray) -> float:
    """Schur σ_eff_ring = -G⁻¹[p_r, S_x] · g_pr · g_SS."""
    G_inv = np.linalg.inv(G)
    g_pr = G[I_P_RING, I_P_RING]
    g_SS = G[I_SX, I_SX]
    return float(-G_inv[I_P_RING, I_SX] * g_pr * g_SS)


def universality_spread(G: np.ndarray, attribution: str = "A1") -> float:
    """Max |α(mode)/α_expected − 1| over charged modes."""
    devs = []
    for label, n6 in TEST_MODES:
        q_exp = EXPECTED_CHARGES[label]
        if abs(q_exp) < 1e-10:
            continue
        if attribution == "A1":
            a = alpha_A1(G, n6)
        else:
            a = alpha_coulomb(G, mode_6_to_11(n6))
        ratio = a / ALPHA
        expected = q_exp ** 2
        devs.append(abs(ratio / expected - 1.0))
    return max(devs) if devs else 0.0


def find_sigma_for_target_eff(p, target_eff: float, sigma_max: float = 0.5):
    """Bisection: find σ_pS_tube where σ_eff_tube = target_eff (positive sign)."""
    # First find signature boundary
    sigmas = np.linspace(0.0, sigma_max, 50001)
    last_ok = 0.0
    for s in sigmas:
        G = build_metric_with_H2(p, s)
        if signature_ok(G):
            last_ok = s
        else:
            break
    band_edge = last_ok

    # Now bisect for target_eff in [0, band_edge]
    lo, hi = 0.0, band_edge
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        G = build_metric_with_H2(p, mid)
        if not signature_ok(G):
            hi = mid
            continue
        se = schur_eff_tube(G)
        if abs(se) < target_eff:
            lo = mid
        else:
            hi = mid
    return mid, band_edge


def m_Ma(n_pt, n_pr, eps, s, K):
    return K * math.sqrt((n_pt / eps) ** 2 + (n_pr - s * n_pt) ** 2)


def m_compound(r, n_pt, n_pr, se_tube, se_ring,
               eps=EPS_P_R64_B, s=S_P_R64_B, K=K_P_R64_B):
    if r < 1e-6:
        return float('inf')
    k_S = 1.0 / r
    m_ma = m_Ma(n_pt, n_pr, eps, s, K)
    cross = (2 * k_S * se_tube * n_pt * HBAR_C_MEV_FM
             + 2 * k_S * se_ring * n_pr * HBAR_C_MEV_FM)
    m2 = m_ma ** 2 + A_KIN * k_S ** 2 + cross
    if m2 <= 0:
        return float('nan')
    return math.sqrt(m2)


def compute_V(n_pt, n_pr, m_sum, se_tube, se_ring,
              r_lo=0.3, r_hi=5.0, n_pts=2000):
    rs = np.linspace(r_lo, r_hi, n_pts)
    Es = np.array([m_compound(r, n_pt, n_pr, se_tube, se_ring) - m_sum for r in rs])
    valid = ~np.isnan(Es)
    if not valid.any():
        return None, None, None, None, None
    rs_v = rs[valid]
    Es_v = Es[valid]
    i_min = int(np.argmin(Es_v))
    return rs_v[i_min], Es_v[i_min], Es_v[-1], rs_v, Es_v


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    p = track9_params().copy_with(eps_p=EPS_P_R64_B, s_p=S_P_R64_B)

    print("=" * 95)
    print("R64 Track 11 Phase 11c — σ_pS_tube + H2 at signature edge")
    print("=" * 95)
    print()
    print(f"  R64 Point B: ε_p = {p.eps_p}, s_p = {p.s_p}")
    print(f"  H2 prescription: σ_aS = {H2_COEFFICIENT:.6f} · σ_pS_tube")
    print()

    # ── Step 1: scan σ_pS_tube under H2, find boundary and σ_eff curve ──
    print("=" * 95)
    print("Step 1: σ_eff_tube vs σ_pS_tube (with H2 companion)")
    print("=" * 95)
    print()

    sample_sigmas = [0.0, 0.01, 0.025, 0.040, 0.050, 0.060, 0.064,
                     0.066, 0.068, 0.069, 0.070, 0.0703, 0.0704]
    print(f"  {'σ_pS_tube':>10s}  {'sig OK':>7s}  {'σ_eff_tube':>11s}  "
          f"{'σ_eff_ring':>11s}  {'A1 spread':>11s}  {'R0 spread':>11s}")
    print("  " + "─" * 80)

    rows = []
    for s in sample_sigmas:
        G = build_metric_with_H2(p, s)
        ok = signature_ok(G)
        if not ok:
            print(f"  {s:>10.5f}  {'NO':>7s}  ─")
            continue
        se_t = schur_eff_tube(G)
        se_r = schur_eff_ring(G)
        spread_A1 = universality_spread(G, "A1")
        spread_R0 = universality_spread(G, "R0")
        print(f"  {s:>10.5f}  {'YES':>7s}  {se_t:>+11.4f}  {se_r:>+11.4f}  "
              f"{spread_A1:>11.3e}  {spread_R0:>11.3e}")
        rows.append({
            "sigma_pS_tube": s,
            "signature_ok": ok,
            "sigma_eff_tube": se_t,
            "sigma_eff_ring": se_r,
            "A1_spread": spread_A1,
            "R0_spread": spread_R0,
        })
    print()

    # ── Step 2: find precise band edge and target σ_eff_tube = 116 ──
    print("=" * 95)
    print("Step 2: find σ_pS_tube giving σ_eff_tube = 116 (Phase 7c target)")
    print("=" * 95)
    print()
    s_at_target, band_edge = find_sigma_for_target_eff(p, target_eff=116.0)
    G_target = build_metric_with_H2(p, s_at_target)
    se_t_target = schur_eff_tube(G_target)
    se_r_target = schur_eff_ring(G_target)
    spread_A1_target = universality_spread(G_target, "A1")
    spread_R0_target = universality_spread(G_target, "R0")
    print(f"  Band edge:                σ_pS_tube = {band_edge:.6f}")
    print(f"  Target σ_eff_tube = 116:  σ_pS_tube = {s_at_target:.6f}")
    print(f"  At target:")
    print(f"    σ_eff_tube  = {se_t_target:+.4f}")
    print(f"    σ_eff_ring  = {se_r_target:+.4f}")
    print(f"    A1 spread   = {spread_A1_target:.3e}")
    print(f"    R0 spread   = {spread_R0_target:.3e}")
    print(f"    Signature OK: {signature_ok(G_target)}")
    print()

    # ── Step 3: also probe σ_eff_tube = -116 (Phase 7c was negative) ──
    # The cross term in Phase 7c had σ_t = -116 (attractive).  Here we
    # can vary the sign by σ_pS_tube > 0 vs σ_pS_tube < 0.
    print("=" * 95)
    print("Step 3: V(r) for pp, pn, nn at σ_eff_tube = ±116")
    print("=" * 95)
    print()

    # Determine σ_eff_tube sign at positive σ_pS_tube
    sign_tube_pos = +1.0 if se_t_target > 0 else -1.0
    print(f"  σ_pS_tube > 0 gives σ_eff_tube sign: {'+' if sign_tube_pos > 0 else '-'}")
    print(f"  Phase 7c had σ_t = -116 (attractive cross term).")
    print()

    # Test both signs
    for tag, target_sign in [("+116", +1.0), ("-116", -1.0)]:
        # If natural σ_eff sign is opposite to target_sign, flip σ_pS_tube
        s_use = s_at_target if sign_tube_pos == target_sign else -s_at_target
        G_v = build_metric_with_H2(p, s_use)
        ok = signature_ok(G_v)
        if not ok:
            print(f"  σ_eff_tube = {tag}: signature broken (σ_pS_tube = {s_use:+.6f})")
            continue
        se_t = schur_eff_tube(G_v)
        se_r = schur_eff_ring(G_v)
        print(f"  σ_eff_tube = {tag} (σ_pS_tube = {s_use:+.6f}):")
        print(f"    Schur σ_eff_tube = {se_t:+.4f}, σ_eff_ring = {se_r:+.4f}")
        print(f"    {'channel':<12s}  {'n_pt':>5s}  {'n_pr':>5s}  "
              f"{'r_min':>7s}  {'V_min':>10s}  {'V(5fm)':>10s}")
        print("    " + "─" * 60)
        for label, n_pt, n_pr, m_sum in [
            ("pp", 6, +4, 2 * M_P),
            ("pn", 6,  0, M_P + M_N),
            ("nn", 6, -4, 2 * M_N),
        ]:
            r_m, V_m, V_inf, _, _ = compute_V(n_pt, n_pr, m_sum, se_t, se_r)
            print(f"    {label:<12s}  {n_pt:>5d}  {n_pr:>+5d}  "
                  f"{r_m:>7.3f}  {V_m:>+10.3f}  {V_inf:>+10.3f}")
        print()

    # ── Step 4: V(r) plot at -116 ──────────────────────────────────
    s_attractive = -s_at_target if sign_tube_pos > 0 else s_at_target
    G_attr = build_metric_with_H2(p, s_attractive)
    if signature_ok(G_attr):
        se_t = schur_eff_tube(G_attr)
        se_r = schur_eff_ring(G_attr)

        fig, ax = plt.subplots(figsize=(10, 6))
        for label, n_pt, n_pr, m_sum, color in [
            ("pp", 6, +4, 2 * M_P, "tab:blue"),
            ("pn", 6,  0, M_P + M_N, "tab:orange"),
            ("nn", 6, -4, 2 * M_N, "tab:green"),
        ]:
            _, _, _, rs, Es = compute_V(n_pt, n_pr, m_sum, se_t, se_r,
                                         r_lo=0.4, r_hi=5.0, n_pts=2000)
            ax.plot(rs, Es, label=f"{label}  n_pr={n_pr:+d}", color=color)
        ax.axhline(0, color="black", linestyle="--", alpha=0.4)
        ax.axhline(-50, color="red", linestyle=":", alpha=0.6, label="Phase 7c reference (-50 MeV)")
        ax.set_xlabel("r (fm)")
        ax.set_ylabel("V(r) (MeV)")
        ax.set_title(f"Phase 11c: V(r) at σ_eff_tube = {se_t:+.1f}, σ_eff_ring = {se_r:+.2f}")
        ax.legend()
        ax.set_ylim(-100, 50)
        plt.tight_layout()
        plt.savefig(out_dir / "track11_phase11c_potential_curves.png", dpi=120)
        plt.close()
        print(f"  PNG: {out_dir / 'track11_phase11c_potential_curves.png'}")

    # ── CSV ─────────────────────────────────────────────────────────
    csv_path = out_dir / "track11_phase11c_tube_edge.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "sigma_pS_tube", "signature_ok",
            "sigma_eff_tube", "sigma_eff_ring",
            "A1_spread", "R0_spread",
        ])
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print(f"  CSV: {csv_path}")
    print()

    # ── Verdict ─────────────────────────────────────────────────────
    print("=" * 95)
    print("VERDICT — Phase 11c")
    print("=" * 95)
    print()
    pass_universality = spread_A1_target < 1e-6
    print(f"  σ_eff_tube reaches ±116 within signature band:  {'YES' if abs(se_t_target) >= 100 else 'PARTIAL' if abs(se_t_target) >= 10 else 'NO'}")
    print(f"  A1 universality at edge (spread):                {spread_A1_target:.3e}  ({'PASS' if pass_universality else 'FAIL'})")
    print(f"  Band edge σ_pS_tube:                             {band_edge:.6f}")
    print()


if __name__ == "__main__":
    main()
