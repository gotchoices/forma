"""
R64 Track 17 — Pool item ac: σ_pS_tube residual sweep at moderate magnitudes.

Track 11 sat at σ_pS_tube ≈ −0.125 (singular metric edge) demanding the
metric provide ALL of nuclear binding.  Track 13b showed this fails QM
(3 bound pn states, bound nn/pp).  Track 15 showed the architecture
should be Ma compound (Track 14: ~1 MeV/n base) PLUS SEMF-style
residual.

This track tests: at MODERATE σ_pS_tube (well inside signature band, no
edge issues), can the σ_pS_tube + H2 cross-term contribution give:

  (a) ~0 additional binding for pn at the 2-body level (deuteron is
      already explained by Ma compound; σ_pS_tube must NOT over-bind).
  (b) Sufficient volume contribution in mean-field for heavy nuclei
      (volume term a_v ~ 14 MeV/n).
  (c) Pass the 2-body QM gate (1 bound pn state at ~2.22 MeV,
      unbound nn/pp, scattering lengths in the right ballpark).

Plus: scan σ_pS_ring alongside σ_pS_tube to test whether the ring
channel adds binding without breaking α-Coulomb (Phase 10a:  ring is
α-inert).
"""

import math
import csv
from pathlib import Path

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

R60_SCRIPTS = Path(__file__).resolve().parent.parent.parent / "R60-metric-11" / "scripts"
sys.path.insert(0, str(R60_SCRIPTS))

from track1_solver import (    # noqa: E402
    signature_ok, ALPHA, FOUR_PI, HBAR_C_MEV_FM,
    I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING, I_NU_TUBE, I_NU_RING,
    I_ALEPH, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import track9_params    # noqa: E402


H2_P = -1.818920
M_P = 938.272
M_N = 939.565
HBAR_C = HBAR_C_MEV_FM
A_KINETIC = 4.0 * HBAR_C ** 2

MU_RED_PN = (M_P * M_N) / (M_P + M_N)
HBAR2_2MU_PN = HBAR_C ** 2 / (2 * MU_RED_PN)
HBAR2_2MU_PP = HBAR_C ** 2 / (2 * (M_P / 2.0))
HBAR2_2MU_NN = HBAR_C ** 2 / (2 * (M_N / 2.0))

# Point A
EPS_P = 0.07309
S_P = 0.19387
K_P = 22.847

# Nuclear-matter saturation density (for mean-field volume estimate)
RHO_SAT = 0.16   # fm⁻³
A_V_TARGET = 13.6   # MeV/nucleon (from Track 15 fit; literature is 15.85)


def build_metric(p, sigma_pS_tube=0.0, sigma_pS_ring=0.0, h2=True):
    G = build_aug_metric(p).copy()
    sigma_aS = (H2_P * sigma_pS_tube) if h2 else 0.0
    for s_idx in (I_SX, I_SY, I_SZ):
        if sigma_pS_tube:
            G[I_P_TUBE, s_idx] += sigma_pS_tube
            G[s_idx, I_P_TUBE] += sigma_pS_tube
        if sigma_pS_ring:
            G[I_P_RING, s_idx] += sigma_pS_ring
            G[s_idx, I_P_RING] += sigma_pS_ring
        if sigma_aS:
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


def m_Ma(n_pt, n_pr):
    return K_P * math.sqrt((n_pt / EPS_P) ** 2 + (n_pr - S_P * n_pt) ** 2)


def V_compound(r, n_pt, n_pr, se_tube, se_ring):
    if r < 1e-9:
        return float('inf')
    m_ma = m_Ma(n_pt, n_pr)
    k = 1.0 / r
    cross = 2 * k * se_tube * n_pt * HBAR_C + 2 * k * se_ring * n_pr * HBAR_C
    m2 = m_ma ** 2 + A_KINETIC * k ** 2 + cross
    if m2 <= 0:
        return float('inf')
    return math.sqrt(m2)


def V_eff(r, n_pt, n_pr, se_tube, se_ring,
          with_coulomb=False, charges=(0, 0)):
    nuclear = V_compound(r, n_pt, n_pr, se_tube, se_ring) - m_Ma(n_pt, n_pr)
    if with_coulomb and charges[0] != 0 and charges[1] != 0:
        if r < 1e-6:
            return float('inf')
        coulomb = ALPHA * HBAR_C * charges[0] * charges[1] / r
        return nuclear + coulomb
    return nuclear


def find_V_min(V_func, r_lo=0.3, r_hi=20.0, n=2000):
    rs = np.linspace(r_lo, r_hi, n)
    Vs = np.array([V_func(r) for r in rs])
    valid = np.isfinite(Vs)
    if not valid.any():
        return None, None
    rs_v = rs[valid]
    Vs_v = Vs[valid]
    i = int(np.argmin(Vs_v))
    return rs_v[i], Vs_v[i]


def mean_field_volume(V_func, r_max=10.0, n=2000):
    """Mean-field per-nucleon volume contribution: U = ρ_sat · ∫V(r) d³r.
    Truncated at r_max to handle 1/r tail.
    """
    rs = np.linspace(0.4, r_max, n)
    Vs = np.array([V_func(r) for r in rs])
    valid = np.isfinite(Vs)
    if not valid.any():
        return float('nan')
    rs_v = rs[valid]
    Vs_v = Vs[valid]
    integrand = 4 * math.pi * rs_v ** 2 * Vs_v
    integral = np.trapezoid(integrand, rs_v)   # MeV·fm³
    return RHO_SAT * integral / 2.0   # /2 to avoid pair double-counting


def shoot(E, V_func, hbar2_2mu, r_min=0.05, r_max=20.0):
    def rhs(r, y):
        u, du = y
        if r < 1e-9:
            return [du, 0.0]
        v = V_func(r)
        if not np.isfinite(v):
            v = 1e10
        d2u = (v - E) * u / hbar2_2mu
        return [du, d2u]
    sol = solve_ivp(rhs, [r_min, r_max], [0.0, 1.0],
                    dense_output=True, max_step=0.02,
                    rtol=1e-9, atol=1e-12, method='RK45')
    return sol.y[0, -1], sol


def find_bound_states(V_func, hbar2_2mu, E_lo=-30.0, E_hi=-0.001, n=300, r_max=20.0):
    Es = np.linspace(E_lo, E_hi, n)
    us = []
    for E in Es:
        try:
            u, _ = shoot(E, V_func, hbar2_2mu, r_max=r_max)
            us.append(u)
        except Exception:
            us.append(np.nan)
    us = np.array(us)
    bound = []
    for i in range(1, len(us)):
        if not (np.isfinite(us[i-1]) and np.isfinite(us[i])):
            continue
        if us[i-1] * us[i] < 0:
            try:
                E_b = brentq(
                    lambda E: shoot(E, V_func, hbar2_2mu, r_max=r_max)[0],
                    Es[i-1], Es[i], xtol=1e-6
                )
                bound.append(E_b)
            except Exception:
                pass
    return bound


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 17 — σ_pS_tube residual sweep at moderate magnitudes")
    print("=" * 100)
    print()
    print(f"  Working at Point A (ε={EPS_P}, s={S_P}, K={K_P})")
    print(f"  Target: a_v ≈ {A_V_TARGET} MeV/n (Track 15 fitted residual)")
    print(f"  ρ_saturation = {RHO_SAT} fm⁻³")
    print(f"  Phase 7c V_min (singular edge): −50 MeV at 1.135 fm")
    print()

    p = track9_params().copy_with(eps_p=EPS_P, s_p=S_P)

    # ── Sweep σ_pS_tube at moderate values ──────────────────────────
    print("=" * 100)
    print("Step 1: σ_pS_tube sweep — V_min, mean-field volume, QM bound states")
    print("=" * 100)
    print()
    print(f"  {'σ_pS':>8s} {'σ_eff_t':>9s} {'V_min(pn)':>10s} {'r_min':>7s} "
          f"{'<V>_mf':>10s} {'#bnd':>5s} {'B_pn':>8s} {'B(²H)':>8s}")
    print("  " + "─" * 78)

    rows_t = []
    for s_pS in [0.001, 0.005, 0.01, 0.02, 0.03, 0.05, 0.075, 0.10, 0.115]:
        s = -s_pS  # negative for attractive
        G = build_metric(p, sigma_pS_tube=s, sigma_pS_ring=0.0, h2=True)
        if not signature_ok(G):
            continue
        se_t = schur_eff_tube(G)
        se_r = schur_eff_ring(G)

        V_pn = lambda r: V_eff(r, 6, 0, se_t, se_r)
        r_m, V_m = find_V_min(V_pn)
        mf_vol = mean_field_volume(V_pn)
        bs = find_bound_states(V_pn, HBAR2_2MU_PN, E_lo=-30.0, E_hi=-0.001, n=200)
        if bs:
            E0 = bs[0]
            delta_ma = m_Ma(6, 0) - (M_P + M_N)
            B = -E0 + (-delta_ma)
        else:
            E0 = None
            B = None

        n_bs = len(bs)
        B_str = f"{B:>+7.2f}" if B is not None else "   ─   "
        E0_str = f"{E0:>+7.2f}" if E0 is not None else "   ─   "
        print(f"  {s_pS:>8.4f} {se_t:>+9.4f} {V_m:>+10.3f} {r_m:>7.3f} "
              f"{mf_vol:>+10.3f} {n_bs:>5d} {E0_str:>8s} {B_str:>8s}")
        rows_t.append({
            "sigma_pS_tube": s_pS,
            "sigma_eff_tube": se_t,
            "V_min_pn": V_m, "r_min_pn": r_m,
            "mean_field_per_n": mf_vol,
            "n_bound_pn": n_bs,
            "E0_pn": E0,
            "B_pn_total": B,
        })
    print()

    # ── σ_pS_ring sweep for comparison ──────────────────────────────
    print("=" * 100)
    print("Step 2: σ_pS_ring sweep (no tube; α-inert per Phase 10a)")
    print("=" * 100)
    print()
    print(f"  {'σ_pS_r':>8s} {'σ_eff_r':>9s} {'V_min(pn)':>10s} {'r_min':>7s} "
          f"{'<V>_mf':>10s} {'#bnd':>5s} {'B_pn':>8s}")
    print("  " + "─" * 70)
    rows_r = []
    for s_pS in [0.001, 0.005, 0.01, 0.025, 0.05, 0.075, 0.10, 0.122]:
        s = -s_pS
        G = build_metric(p, sigma_pS_tube=0.0, sigma_pS_ring=s, h2=False)
        if not signature_ok(G):
            continue
        se_t = schur_eff_tube(G)
        se_r = schur_eff_ring(G)

        # For pn (n_pr=0), σ_pS_ring contributes nothing!
        # Test pp instead (n_pr = +4) to see ring effect.
        V_pn = lambda r: V_eff(r, 6, 0, se_t, se_r)
        r_m, V_m = find_V_min(V_pn)
        mf_vol = mean_field_volume(V_pn)
        bs = find_bound_states(V_pn, HBAR2_2MU_PN, E_lo=-30.0, E_hi=-0.001, n=200)
        if bs:
            E0 = bs[0]
            delta_ma = m_Ma(6, 0) - (M_P + M_N)
            B = -E0 + (-delta_ma)
            B_str = f"{B:>+7.2f}"
        else:
            B_str = "   ─   "
        n_bs = len(bs)
        print(f"  {s_pS:>8.4f} {se_r:>+9.4f} {V_m:>+10.3f} {r_m:>7.3f} "
              f"{mf_vol:>+10.3f} {n_bs:>5d} {B_str:>8s}")
        rows_r.append({
            "sigma_pS_ring": s_pS, "sigma_eff_ring": se_r,
            "V_min_pn": V_m, "r_min_pn": r_m,
            "mean_field_per_n": mf_vol, "n_bound_pn": n_bs,
        })
    print()

    print("  Note: σ_pS_ring · n_pr = 0 for pn (rings cancel).")
    print("  σ_pS_ring contributes to pp/nn but not deuteron.")
    print()

    # ── Find σ_pS_tube giving correct deuteron + reasonable volume ──
    print("=" * 100)
    print("Step 3: Identify σ_pS_tube where deuteron = 2.22 MeV AND volume reasonable")
    print("=" * 100)
    print()
    print(f"  Target B(²H) = 2.22 MeV (1 bound state from Ma compound + small σ contrib)")
    print(f"  Target a_v ≈ {A_V_TARGET} MeV/n for SEMF residual")
    print()
    print("  Reading from Step 1 rows:")
    print()
    for r in rows_t:
        if r["B_pn_total"] is not None:
            B_match = abs(r["B_pn_total"] - 2.22)
            mf_match = abs(r["mean_field_per_n"] + A_V_TARGET) / A_V_TARGET
            note = ""
            if B_match < 1.0 and r["n_bound_pn"] == 1:
                note = "   ← deuteron OK"
            if abs(r["mean_field_per_n"]) > 1.0:
                note += f"   <V>_mf={r['mean_field_per_n']:+.2f}"
            if note:
                print(f"    σ_pS_tube = {r['sigma_pS_tube']:.4f}: "
                      f"B(²H)={r['B_pn_total']:+.2f}, n_bs={r['n_bound_pn']},"
                      f" <V>_mf={r['mean_field_per_n']:+.2f}{note}")
    print()

    # CSV
    csv_path = out_dir / "track17_pool_ac_residual_sweep.csv"
    with open(csv_path, "w", newline="") as f:
        if rows_t:
            writer = csv.DictWriter(f, fieldnames=list(rows_t[0].keys()))
            writer.writeheader()
            writer.writerows(rows_t)
    print(f"  CSV: {csv_path}")
    print()

    # ── Verdict ─────────────────────────────────────────────────────
    print("=" * 100)
    print("VERDICT — Track 17")
    print("=" * 100)
    print()
    # Sweet spot: σ_pS_tube where (a) deuteron ≈ 2.22 (1 bound state),
    # (b) <V>_mf > some threshold for volume contribution
    sweet_t = [r for r in rows_t
               if r["B_pn_total"] is not None
               and abs(r["B_pn_total"] - 2.22) < 1.5
               and r["n_bound_pn"] == 1]
    if sweet_t:
        print(f"  Found σ_pS_tube candidates with reasonable deuteron AND single bound state:")
        for r in sweet_t:
            print(f"    σ_pS_tube = {r['sigma_pS_tube']:.4f}  "
                  f"(σ_eff = {r['sigma_eff_tube']:+.4f})  "
                  f"B(²H) = {r['B_pn_total']:+.2f} MeV  "
                  f"<V>_mf = {r['mean_field_per_n']:+.3f} MeV")
    else:
        print(f"  No σ_pS_tube candidate gives both correct deuteron AND single bound state.")
    print()


if __name__ == "__main__":
    main()
