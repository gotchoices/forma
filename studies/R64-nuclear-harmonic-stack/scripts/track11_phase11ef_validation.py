"""
R64 Track 11 Phases 11e + 11f — Validation gates before model-G assembly.

Phase 11e: Joint refit stability — verify (ε_p, s_p, K_p) Point B
remains stable when σ_pS_tube + H2 is active at the signature edge.
Sweeps (ε_p, s_p) around Point B and reports V_min(pn) stability.

Phase 11f: Full R64 hadron inventory under σ_pS_tube + H2 active.
For each hadron tuple, compute α/α₀ (R0 and A1) and mode_energy.
Verify universality holds and masses don't break under the new
strong-force architecture.

Outputs:
  outputs/track11_phase11e_point_b_stability.csv
  outputs/track11_phase11f_inventory_validation.csv
"""

import sys
import math
import csv
from pathlib import Path

import numpy as np

R60_SCRIPTS = Path(__file__).resolve().parent.parent.parent / "R60-metric-11" / "scripts"
sys.path.insert(0, str(R60_SCRIPTS))

from track1_solver import (    # noqa: E402
    alpha_coulomb, mode_6_to_11, mode_energy, signature_ok,
    L_vector_from_params, ALPHA, FOUR_PI, HBAR_C_MEV_FM, MA_SLICE,
    I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING, I_NU_TUBE, I_NU_RING,
    I_ALEPH, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import (   # noqa: E402
    track9_params, MODEL_E_INVENTORY,
)


H2_COEFFICIENT = -1.818920
EPS_P_R64_B = 0.2052
S_P_R64_B = 0.0250
K_P_R64_B = 63.629
A_KIN = 4.0 * HBAR_C_MEV_FM ** 2
M_P, M_N = 938.272, 939.565


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
    ma_t_col = G_inv[MA_SLICE, I_T]
    Q = float((n_ma @ ma_t_col) * (-G_inv[I_T, I_T]))
    return Q * Q / FOUR_PI


def build_metric_with_H2(p, sigma_pS_tube):
    G = build_aug_metric(p).copy()
    sigma_aS = H2_COEFFICIENT * sigma_pS_tube
    for s_idx in (I_SX, I_SY, I_SZ):
        G[I_P_TUBE, s_idx] += sigma_pS_tube
        G[s_idx, I_P_TUBE] += sigma_pS_tube
        G[I_ALEPH, s_idx] += sigma_aS
        G[s_idx, I_ALEPH] += sigma_aS
    return G


def schur_eff_tube(G):
    G_inv = np.linalg.inv(G)
    g_pp = G[I_P_TUBE, I_P_TUBE]
    g_SS = G[I_SX, I_SX]
    return float(-G_inv[I_P_TUBE, I_SX] * g_pp * g_SS)


def schur_eff_ring(G):
    G_inv = np.linalg.inv(G)
    g_pr = G[I_P_RING, I_P_RING]
    g_SS = G[I_SX, I_SX]
    return float(-G_inv[I_P_RING, I_SX] * g_pr * g_SS)


def find_sigma_for_eff_tube(p, target=-116.0):
    """Find σ_pS_tube giving σ_eff_tube = target (preserves sign)."""
    # Negative σ_pS_tube gives negative σ_eff_tube.
    sign = -1.0 if target < 0 else +1.0
    sigmas = np.linspace(0.0, 0.20, 20001)
    last_ok = 0.0
    for s in sigmas:
        G = build_metric_with_H2(p, sign * s)
        if signature_ok(G):
            last_ok = s
        else:
            break
    band_edge = last_ok
    if band_edge == 0:
        return None, None

    lo, hi = 0.0, band_edge
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        G = build_metric_with_H2(p, sign * mid)
        if not signature_ok(G):
            hi = mid
            continue
        se = schur_eff_tube(G)
        if abs(se) < abs(target):
            lo = mid
        else:
            hi = mid
    return sign * mid, sign * band_edge


def m_Ma(n_pt, n_pr, eps, s, K):
    return K * math.sqrt((n_pt / eps) ** 2 + (n_pr - s * n_pt) ** 2)


def m_compound(r, n_pt, n_pr, se_tube, se_ring, eps, s, K):
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


def vmin_for(n_pt, n_pr, m_sum, se_tube, se_ring, eps, s, K):
    rs = np.linspace(0.4, 5.0, 1500)
    Es = np.array([m_compound(r, n_pt, n_pr, se_tube, se_ring,
                              eps, s, K) - m_sum for r in rs])
    valid = ~np.isnan(Es)
    if not valid.any():
        return None, None
    return rs[valid][int(np.argmin(Es[valid]))], Es[valid].min()


# ──────────────────────────────────────────────────────────────────
# Phase 11e: Point B stability under σ_pS_tube + H2
# ──────────────────────────────────────────────────────────────────

def phase_11e(out_dir):
    print("=" * 95)
    print("Phase 11e — Point B stability under σ_pS_tube + H2 active")
    print("=" * 95)
    print()

    # Sweep around Point B
    eps_grid = [0.18, 0.19, 0.2052, 0.21, 0.22, 0.23, 0.25]
    s_grid = [0.020, 0.025, 0.030, 0.040, 0.050]

    print(f"  Target: σ_eff_tube = -116 (Phase 7c).")
    print(f"  Reporting V_min(pn) and r_min(pn) at each (ε_p, s_p):")
    print()
    print(f"  {'ε_p':>7s}  {'s_p':>7s}  {'σ_pS_tube':>11s}  "
          f"{'σ_eff_tube':>11s}  {'r_min(pn)':>10s}  {'V_min(pn)':>11s}  "
          f"{'r_min(pp)':>10s}  {'V_min(pp)':>11s}")
    print("  " + "─" * 100)

    rows = []
    for eps_p in eps_grid:
        for s_p in s_grid:
            p = track9_params().copy_with(eps_p=eps_p, s_p=s_p)
            sigma, edge = find_sigma_for_eff_tube(p, target=-116.0)
            if sigma is None:
                print(f"  {eps_p:>7.4f}  {s_p:>7.4f}  ─")
                continue
            G = build_metric_with_H2(p, sigma)
            se_t = schur_eff_tube(G)
            se_r = schur_eff_ring(G)
            r_pn, V_pn = vmin_for(6, 0, M_P + M_N, se_t, se_r,
                                   eps_p, s_p, K_P_R64_B)
            r_pp, V_pp = vmin_for(6, +4, 2 * M_P, se_t, se_r,
                                   eps_p, s_p, K_P_R64_B)
            print(f"  {eps_p:>7.4f}  {s_p:>7.4f}  {sigma:>+11.6f}  "
                  f"{se_t:>+11.4f}  {r_pn:>10.3f}  {V_pn:>+11.3f}  "
                  f"{r_pp:>10.3f}  {V_pp:>+11.3f}")
            rows.append({
                "eps_p": eps_p, "s_p": s_p, "sigma_pS_tube": sigma,
                "band_edge": edge, "sigma_eff_tube": se_t,
                "sigma_eff_ring": se_r,
                "r_min_pn": r_pn, "V_min_pn": V_pn,
                "r_min_pp": r_pp, "V_min_pp": V_pp,
            })
    print()

    # Stability check
    point_b_row = next(r for r in rows
                       if abs(r["eps_p"] - EPS_P_R64_B) < 1e-3
                       and abs(r["s_p"] - S_P_R64_B) < 1e-3)
    print(f"  At Point B (ε_p = {EPS_P_R64_B}, s_p = {S_P_R64_B}):")
    print(f"    V_min(pn) = {point_b_row['V_min_pn']:+.3f} MeV at "
          f"r = {point_b_row['r_min_pn']:.3f} fm")
    print(f"    Phase 7c reference: V_min ≈ -50 MeV at r ≈ 1.135 fm")
    print()

    # Compute spread of V_min(pn) across the grid
    vpn_values = [r["V_min_pn"] for r in rows if r["V_min_pn"] is not None]
    if vpn_values:
        print(f"  V_min(pn) range across grid: "
              f"[{min(vpn_values):+.2f}, {max(vpn_values):+.2f}] MeV")
        print(f"  → Strong-force depth is {'stable' if (max(vpn_values) - min(vpn_values)) < 5 else 'sensitive'} "
              f"to (ε_p, s_p) around Point B.")
    print()

    # CSV
    csv_path = out_dir / "track11_phase11e_point_b_stability.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"  CSV: {csv_path}")
    print()


# ──────────────────────────────────────────────────────────────────
# Phase 11f: Full R64 hadron inventory under σ_pS_tube + H2 active
# ──────────────────────────────────────────────────────────────────

# R64 quark-decomposed hadron inventory.  Map R60 model-F tuples to
# R64 equivalents where the proton structure changed.  For mesons
# the R60 tuples are kept (e/ν sheets unchanged).
R64_INVENTORY_FOR_VALIDATION = [
    # (label, target_mass_MeV, expected_charge_e, R64_tuple)
    ("electron",   0.51100,  -1.0,   (1, 2, 0, 0, 0, 0)),
    ("muon",       105.658,  -1.0,   (1, 1, -2, -2, 0, 0)),
    ("π⁰",         134.977,   0.0,   (0, -1, -2, -2, 0, 0)),
    ("π±",         139.570,  -1.0,   (-1, -1, -3, -3, 0, 0)),
    ("K±",         493.677,  -1.0,   (-1, -6, -2, 2, 0, 1)),
    ("K⁰",         497.611,   0.0,   (0, -4, -2, 2, 0, 1)),
    ("η",          547.862,   0.0,   (-1, -4, -2, 2, -1, 0)),
    ("ρ",          775.260,   0.0,   (-1, 5, -2, 2, 0, 1)),
    ("φ",          1019.461,  0.0,   (-1, 4, 2, -2, -1, 2)),
    ("R64 proton", 938.272,  +1.0,   (0, 0, 0, 0, 3, +2)),
    ("R64 neutron",939.565,   0.0,   (0, 0, 0, 0, 3, -2)),
]


def phase_11f(out_dir):
    print("=" * 95)
    print("Phase 11f — Full R64 hadron inventory under σ_pS_tube + H2 active")
    print("=" * 95)
    print()

    # Use R60 model-F structural k_p (NOT K_P_R64_B which is the kinematic
    # prefactor for the m_Ma formula; the structural g_pp diagonal is the
    # universal tube coupling 0.04696442 from track9_params).
    p = track9_params().copy_with(eps_p=EPS_P_R64_B, s_p=S_P_R64_B)
    sigma, edge = find_sigma_for_eff_tube(p, target=-116.0)
    G = build_metric_with_H2(p, sigma)
    L = L_vector_from_params(p)
    se_t = schur_eff_tube(G)

    print(f"  At R64 Point B with σ_pS_tube = {sigma:+.6f} (σ_eff_tube = {se_t:+.2f}):")
    print()
    print(f"  {'particle':<13s}  {'tuple':<22s}  {'q_exp':>6s}  "
          f"{'α/α₀ (R0)':>10s}  {'α/α₀ (A1)':>10s}  "
          f"{'expected':>9s}  {'A1 ratio':>9s}  "
          f"{'predicted m':>11s}  {'target m':>9s}")
    print("  " + "─" * 110)

    rows = []
    devs_A1 = []
    for label, m_target, q_exp, n6 in R64_INVENTORY_FOR_VALIDATION:
        n11 = mode_6_to_11(n6)
        a_R0 = alpha_coulomb(G, n11)
        a_A1 = alpha_A1(G, n6)
        expected_alpha = (q_exp ** 2) * ALPHA
        ratio_A1 = a_A1 / expected_alpha if expected_alpha > 0 else float('nan')
        if abs(q_exp) > 1e-10:
            devs_A1.append(abs(ratio_A1 - 1.0))
        m_pred = mode_energy(G, L, n11)
        n6_str = str(n6).replace(" ", "")
        ratio_str = f"{ratio_A1:.4f}" if not math.isnan(ratio_A1) else "—"
        print(f"  {label:<13s}  {n6_str:<22s}  {q_exp:>+6.2f}  "
              f"{a_R0/ALPHA:>10.4f}  {a_A1/ALPHA:>10.4f}  "
              f"{q_exp**2:>9.4f}  {ratio_str:>9}  "
              f"{m_pred:>11.3f}  {m_target:>9.3f}")
        rows.append({
            "particle": label, "tuple": n6_str, "q_expected": q_exp,
            "alpha_R0": a_R0, "alpha_A1": a_A1,
            "expected_alpha_over_alpha0": q_exp ** 2,
            "A1_ratio": ratio_A1,
            "predicted_mass_MeV": m_pred, "target_mass_MeV": m_target,
        })

    print()
    if devs_A1:
        print(f"  A1 universality spread (max |α/α_expected - 1|): {max(devs_A1):.4e}")
    print()

    # CSV
    csv_path = out_dir / "track11_phase11f_inventory_validation.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"  CSV: {csv_path}")
    print()


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)
    print()
    phase_11e(out_dir)
    phase_11f(out_dir)
    print("=" * 95)
    print("Combined verdict")
    print("=" * 95)
    print()
    print("  Phases 11e and 11f assess whether the σ_pS_tube + H2 architecture")
    print("  remains coherent across the working-point neighborhood (11e) and")
    print("  the full hadron inventory (11f).")


if __name__ == "__main__":
    main()
