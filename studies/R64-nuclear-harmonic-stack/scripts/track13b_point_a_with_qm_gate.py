"""
R64 Track 13b — Point A unified-working-point validation, with QM gate.

Addresses review.md Concern 1 (Phase 7d's QM gate was never re-applied
to Phase 11c's V(r)) by:

  (a) Re-applying the QM gate to Point B's V(r) — same calc as Phase 7d
      but using metric-derived σ_eff_tube at signature edge (Phase 11c
      reproduction).  This validates that Phase 11c's V(r) inherits
      Phase 7c's QM failures.

  (b) Computing V(r) at Point A's parameters under the metric
      (σ_pS_tube + H2 at signature edge for Point A); applying the
      QM gate.

  (c) Reporting whether Point A's V(r) passes the QM gate that
      Point B's failed.

Ground-truth observables:
  B(²H)        = 2.224 MeV  (1 bound state in pn ³S₁)
  pp           = unbound (pp ¹S₀)
  nn           = unbound (nn ¹S₀)
  a_s (singlet)= -23.7 fm
  a_t (triplet)= +5.42 fm
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


# ─── Constants ───────────────────────────────────────────────────────
M_P = 938.272
M_N = 939.565
HBAR_C = HBAR_C_MEV_FM
A_KINETIC = 4.0 * HBAR_C ** 2

# Reduced masses
MU_RED_PN = (M_P * M_N) / (M_P + M_N)
MU_RED_PP = M_P / 2.0
MU_RED_NN = M_N / 2.0

HBAR2_2MU_PN = HBAR_C ** 2 / (2 * MU_RED_PN)
HBAR2_2MU_PP = HBAR_C ** 2 / (2 * MU_RED_PP)
HBAR2_2MU_NN = HBAR_C ** 2 / (2 * MU_RED_NN)

# H2 prescription: σ_aS = b_p · σ_pS_tube
H2_P = -1.818920


# ─── Working points ──────────────────────────────────────────────────
POINT_A = dict(eps_p=0.07309, s_p=0.19387, K_p=22.847, label="Point A")
POINT_B = dict(eps_p=0.2052,  s_p=0.0250,  K_p=63.629, label="Point B")


# ─── Metric construction ────────────────────────────────────────────
def build_metric_with_pS_tube_H2(p, sigma_pS_tube):
    """11D metric with σ_pS_tube on (p_t, S_i) and σ_aS=H2_P·σ on (ℵ, S_i)."""
    G = build_aug_metric(p).copy()
    sigma_aS = H2_P * sigma_pS_tube
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


def find_signature_edge(p, sigma_max=0.5, n_steps=200001):
    """Find the largest |σ_pS_tube| keeping signature Lorentzian."""
    sigmas = np.linspace(0.0, sigma_max, n_steps)
    last_ok = 0.0
    for s in sigmas:
        # negative side gives attractive σ_eff_tube
        G = build_metric_with_pS_tube_H2(p, -s)
        if signature_ok(G):
            last_ok = s
        else:
            break
    return last_ok


def find_sigma_for_target_eff(p, target_eff_magnitude=116.0):
    """Bisect on σ_pS_tube < 0 until σ_eff_tube ≈ -target_eff_magnitude."""
    edge = find_signature_edge(p)
    if edge < 1e-12:
        return None, None
    lo, hi = 0.0, edge
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        G = build_metric_with_pS_tube_H2(p, -mid)
        if not signature_ok(G):
            hi = mid
            continue
        se = -schur_eff_tube(G)  # σ_eff_tube < 0 since σ_pS_tube < 0
        # we want |se| = target → se = -target (negative)
        if abs(se) < target_eff_magnitude:
            lo = mid
        else:
            hi = mid
    return -mid, edge


# ─── V(r) construction (using metric-derived σ_eff_tube) ────────────
def m_Ma(n_pt, n_pr, eps, s, K):
    return K * math.sqrt((n_pt / eps) ** 2 + (n_pr - s * n_pt) ** 2)


def V_compound(r, n_pt, n_pr, sigma_eff_tube, eps, s, K):
    """m(r) at relative-coordinate spatial separation r."""
    if r < 1e-9:
        return float('inf')
    m_ma = m_Ma(n_pt, n_pr, eps, s, K)
    k = 1.0 / r
    m2 = m_ma ** 2 + A_KINETIC * k ** 2 + 2 * k * sigma_eff_tube * n_pt * HBAR_C
    if m2 <= 0:
        return float('inf')
    return math.sqrt(m2)


def V_eff(r, n_pt, n_pr, sigma_eff_tube, eps, s, K,
          with_coulomb=False, charges=(0, 0)):
    nuclear = V_compound(r, n_pt, n_pr, sigma_eff_tube, eps, s, K) - m_Ma(n_pt, n_pr, eps, s, K)
    if with_coulomb and charges[0] != 0 and charges[1] != 0:
        if r < 1e-6:
            return float('inf')
        coulomb = ALPHA * HBAR_C * charges[0] * charges[1] / r
        return nuclear + coulomb
    return nuclear


# ─── Schrödinger machinery (lifted from Phase 7d) ───────────────────
def shoot(E, V_func, hbar2_2mu, r_min=0.01, r_max=30.0):
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


def find_bound_states(V_func, hbar2_2mu, E_range=(-40.0, -0.01),
                      n_scan=600, r_max=30.0):
    Es = np.linspace(E_range[0], E_range[1], n_scan)
    us = []
    for E in Es:
        try:
            u_end, _ = shoot(E, V_func, hbar2_2mu, r_max=r_max)
            us.append(u_end)
        except Exception:
            us.append(np.nan)
    us = np.array(us)
    bound_states = []
    for i in range(1, len(us)):
        if not (np.isfinite(us[i-1]) and np.isfinite(us[i])):
            continue
        if us[i-1] * us[i] < 0:
            try:
                E_bound = brentq(
                    lambda E: shoot(E, V_func, hbar2_2mu, r_max=r_max)[0],
                    Es[i-1], Es[i], xtol=1e-6
                )
                bound_states.append(E_bound)
            except Exception:
                pass
    return bound_states


def phase_shift_at_k(k, V_func, hbar2_2mu, r_max=40.0, r_min=0.01):
    E = hbar2_2mu * k ** 2
    u_end, sol = shoot(E, V_func, hbar2_2mu, r_min=r_min, r_max=r_max)
    u_m = sol.sol(r_max)[0]
    du_m = sol.sol(r_max)[1]
    phase = math.atan2(k * u_m, du_m)
    delta = phase - k * r_max
    while delta > math.pi / 2:
        delta -= math.pi
    while delta <= -math.pi / 2:
        delta += math.pi
    return delta


def compute_scattering_length(V_func, hbar2_2mu, ks=None, r_max=40.0):
    if ks is None:
        ks = np.linspace(0.01, 0.15, 10)
    raw = []
    for k in ks:
        try:
            d = phase_shift_at_k(k, V_func, hbar2_2mu, r_max=r_max)
            kcot = k / math.tan(d) if abs(math.tan(d)) > 1e-12 else float('nan')
            raw.append((k, d, kcot))
        except Exception:
            raw.append((k, float('nan'), float('nan')))
    arr = np.array([(k, kcot) for k, _, kcot in raw if np.isfinite(kcot)])
    if len(arr) < 3:
        return float('nan'), float('nan'), raw
    ks_v = arr[:, 0]
    kc_v = arr[:, 1]
    p = np.polyfit(ks_v ** 2, kc_v, 1)
    a = -1.0 / p[1] if abs(p[1]) > 1e-12 else float('inf')
    r_eff = 2 * p[0]
    return a, r_eff, raw


# ─── Driver ──────────────────────────────────────────────────────────
def analyze_point(point, target_eff=116.0, label_extra=""):
    p = track9_params().copy_with(eps_p=point['eps_p'], s_p=point['s_p'])
    print()
    print("=" * 90)
    print(f"  Working point: {point['label']}{label_extra}")
    print(f"  (ε_p, s_p, K_p) = ({point['eps_p']}, {point['s_p']}, {point['K_p']})")
    print("=" * 90)

    sigma, edge = find_sigma_for_target_eff(p, target_eff)
    if sigma is None:
        print("  No signature-OK band — abort")
        return None

    G = build_metric_with_pS_tube_H2(p, sigma)
    se_tube = schur_eff_tube(G)
    print(f"  Signature edge: σ_pS_tube = ±{edge:.6f}")
    print(f"  Operating σ_pS_tube = {sigma:+.6f}")
    print(f"  → σ_eff_tube = {se_tube:+.4f}")
    print(f"  → m_Ma asymptotes:")
    eps, s, K = point['eps_p'], point['s_p'], point['K_p']
    print(f"      m_Ma(pn) = m_Ma(6, 0)  = {m_Ma(6, 0, eps, s, K):.3f} MeV  "
          f"(2·M_p+M_n)/2 = {(2*M_P + 2*M_N)/2:.3f}")
    print(f"      m_Ma(pp) = m_Ma(6, +4) = {m_Ma(6, +4, eps, s, K):.3f} MeV")
    print(f"      m_Ma(nn) = m_Ma(6, -4) = {m_Ma(6, -4, eps, s, K):.3f} MeV")

    # Build V_eff functions for this point
    def V_pn(r):
        return V_eff(r, 6, 0, se_tube, eps, s, K)

    def V_pp(r):
        return V_eff(r, 6, +4, se_tube, eps, s, K,
                     with_coulomb=True, charges=(1, 1))

    def V_nn(r):
        return V_eff(r, 6, -4, se_tube, eps, s, K)

    # Static V profile
    print()
    print(f"  V_eff(r) profile [pn channel, MeV]:")
    for r in [0.4, 0.7, 1.0, 1.135, 1.5, 2.0, 5.0]:
        print(f"    r = {r:5.2f} fm → V_pn = {V_pn(r):+9.3f}")

    delta_ma_pn = m_Ma(6, 0, eps, s, K) - (M_P + M_N)
    delta_ma_pp = m_Ma(6, +4, eps, s, K) - 2 * M_P
    delta_ma_nn = m_Ma(6, -4, eps, s, K) - 2 * M_N
    print()
    print(f"  Ma-side offsets:")
    print(f"    Δ_Ma(pn) = {delta_ma_pn:+.3f} MeV")
    print(f"    Δ_Ma(pp) = {delta_ma_pp:+.3f} MeV")
    print(f"    Δ_Ma(nn) = {delta_ma_nn:+.3f} MeV")

    # ── QM gate ────────────────────────────────────────────────
    print()
    print(f"  ── QM GATE (Phase 7d Schrödinger) ──")
    print()

    print(f"  pn bound states (deuteron candidate):")
    pn_bs = find_bound_states(V_pn, HBAR2_2MU_PN,
                               E_range=(-35.0, -0.01), n_scan=400, r_max=30.0)
    if pn_bs:
        E0_pn = pn_bs[0]
        print(f"    {len(pn_bs)} bound state(s) found")
        for i, E in enumerate(pn_bs):
            print(f"      State {i}: E = {E:+.4f} MeV")
        binding_total_pn = -E0_pn + (-delta_ma_pn)
        print(f"    Ground state E₀ = {E0_pn:.3f} MeV")
        print(f"    Binding above V(∞):           {-E0_pn:.3f} MeV")
        print(f"    Binding from free-N threshold: {binding_total_pn:.3f} MeV")
        print(f"    Observed B(²H) = 2.224 MeV    (1 bound state)")
        n_bs_pn = len(pn_bs)
    else:
        print(f"    No bound states found (would mean no deuteron — wrong)")
        E0_pn = None
        n_bs_pn = 0

    print()
    print(f"  nn bound states (singlet check):")
    nn_bs = find_bound_states(V_nn, HBAR2_2MU_NN,
                               E_range=(-35.0, -0.01), n_scan=400, r_max=30.0)
    if nn_bs:
        for i, E in enumerate(nn_bs):
            print(f"    State {i}: E = {E:+.4f} MeV  (nature: nn unbound)")
        n_bs_nn = len(nn_bs)
    else:
        print(f"    No bound states (✓ matches observation)")
        n_bs_nn = 0

    print()
    print(f"  pp bound states (singlet w/ Coulomb):")
    pp_bs = find_bound_states(V_pp, HBAR2_2MU_PP,
                               E_range=(-35.0, -0.01), n_scan=400, r_max=30.0)
    if pp_bs:
        for i, E in enumerate(pp_bs):
            print(f"    State {i}: E = {E:+.4f} MeV  (nature: pp unbound)")
        n_bs_pp = len(pp_bs)
    else:
        print(f"    No bound states (✓ matches observation)")
        n_bs_pp = 0

    print()
    print(f"  Scattering lengths:")
    a_t, _, _ = compute_scattering_length(
        V_pn, HBAR2_2MU_PN, ks=np.linspace(0.01, 0.15, 8), r_max=40.0)
    a_s_nn, _, _ = compute_scattering_length(
        V_nn, HBAR2_2MU_NN, ks=np.linspace(0.01, 0.15, 8), r_max=40.0)
    print(f"    a_t (pn triplet)       = {a_t:+.3f} fm   (observed: +5.42)")
    print(f"    a_s (nn singlet analog)= {a_s_nn:+.3f} fm   (observed: −23.7)")

    return {
        'point': point,
        'sigma_pS_tube': sigma,
        'sigma_eff_tube': se_tube,
        'edge': edge,
        'pn_bound_states': pn_bs,
        'nn_bound_states': nn_bs,
        'pp_bound_states': pp_bs,
        'binding_pn_above_threshold': binding_total_pn if pn_bs else None,
        'a_t': a_t,
        'a_s_nn': a_s_nn,
        'V_pn': V_pn, 'V_pp': V_pp, 'V_nn': V_nn,
    }


def main():
    print("=" * 90)
    print("R64 Track 13b — Point A unified-working-point validation, with QM gate")
    print("=" * 90)
    print()
    print("  Premise (per review.md Concern 1): Phase 7d's QM gate was never")
    print("  re-applied to Phase 11c's V(r).  Track 13b applies it to:")
    print("    (a) Phase 11c reproduction at Point B  (control)")
    print("    (b) New computation at Point A         (test)")
    print()
    print("  Observed targets:")
    print("    B(²H) = 2.224 MeV    (1 bound state in pn)")
    print("    nn, pp = unbound")
    print("    a_t   = +5.42 fm")
    print("    a_s   = −23.7 fm")

    result_B = analyze_point(POINT_B, target_eff=116.0,
                              label_extra=" — Phase 11c reproduction (control)")
    result_A = analyze_point(POINT_A, target_eff=116.0,
                              label_extra=" — Track 13b test")

    # ── Verdict ────────────────────────────────────────────────────
    print()
    print("=" * 90)
    print("VERDICT — Track 13b")
    print("=" * 90)
    print()

    def n_bs(r, key):
        return len(r[key]) if r and r[key] else 0

    print(f"  {'':<18s}  {'Point B':>20s}  {'Point A':>20s}  {'Observed':>12s}")
    print("  " + "─" * 80)
    if result_B:
        print(f"  {'pn bound states':<18s}  {n_bs(result_B,'pn_bound_states'):>20d}  "
              f"{n_bs(result_A,'pn_bound_states'):>20d}  "
              f"{1:>12d}")
    if result_B and result_B['binding_pn_above_threshold'] is not None:
        b_B = f"{result_B['binding_pn_above_threshold']:+.2f}"
    else:
        b_B = "—"
    if result_A and result_A['binding_pn_above_threshold'] is not None:
        b_A = f"{result_A['binding_pn_above_threshold']:+.2f}"
    else:
        b_A = "—"
    print(f"  {'B(²H) [MeV]':<18s}  {b_B:>20s}  {b_A:>20s}  {'+2.22':>12s}")
    print(f"  {'nn bound states':<18s}  {n_bs(result_B,'nn_bound_states'):>20d}  "
          f"{n_bs(result_A,'nn_bound_states'):>20d}  {0:>12d}")
    print(f"  {'pp bound states':<18s}  {n_bs(result_B,'pp_bound_states'):>20d}  "
          f"{n_bs(result_A,'pp_bound_states'):>20d}  {0:>12d}")
    print(f"  {'a_t [fm]':<18s}  {result_B['a_t']:>20.2f}  "
          f"{result_A['a_t']:>20.2f}  {'+5.42':>12s}")
    print(f"  {'a_s [fm]':<18s}  {result_B['a_s_nn']:>20.2f}  "
          f"{result_A['a_s_nn']:>20.2f}  {'-23.70':>12s}")

    print()
    pass_A = (n_bs(result_A,'pn_bound_states') == 1
              and n_bs(result_A,'nn_bound_states') == 0
              and n_bs(result_A,'pp_bound_states') == 0)
    pass_B = (n_bs(result_B,'pn_bound_states') == 1
              and n_bs(result_B,'nn_bound_states') == 0
              and n_bs(result_B,'pp_bound_states') == 0)
    print(f"  Point B QM gate (count-of-bound-states test): "
          f"{'PASS' if pass_B else 'FAIL'}")
    print(f"  Point A QM gate (count-of-bound-states test): "
          f"{'PASS' if pass_A else 'FAIL'}")
    print()

    # Plot V(r) for both points
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    r_plot = np.linspace(0.3, 8.0, 400)
    for ax, r_pt, label in zip(axes,
                                 [result_B, result_A],
                                 ["Point B", "Point A"]):
        if r_pt is None:
            continue
        V_pn_plot = [r_pt['V_pn'](r) for r in r_plot]
        V_pp_plot = [r_pt['V_pp'](r) for r in r_plot]
        V_nn_plot = [r_pt['V_nn'](r) for r in r_plot]
        ax.plot(r_plot, V_pn_plot, label='pn', linewidth=1.8)
        ax.plot(r_plot, V_pp_plot, label='pp', linewidth=1.5, linestyle='--')
        ax.plot(r_plot, V_nn_plot, label='nn', linewidth=1.5, linestyle=':')
        ax.axhline(0, color='black', linewidth=0.5)
        if r_pt['pn_bound_states']:
            for E in r_pt['pn_bound_states']:
                ax.axhline(E, color='red', linewidth=0.6, alpha=0.5)
        ax.set_xlabel('r (fm)')
        ax.set_ylabel('V_eff(r) (MeV)')
        ax.set_title(f"{label}: σ_eff_tube = {r_pt['sigma_eff_tube']:.1f}")
        ax.legend()
        ax.set_ylim(-100, 50)
        ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_dir / "track13b_point_a_qm_gate.png", dpi=120)
    plt.close()
    print(f"  PNG: {out_dir / 'track13b_point_a_qm_gate.png'}")


if __name__ == "__main__":
    main()
