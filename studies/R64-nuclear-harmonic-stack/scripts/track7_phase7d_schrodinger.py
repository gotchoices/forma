"""
R64 Track 7 Phase 7d — Schrödinger validation of Phase 7c V(r).

Solve the radial Schrödinger equation with the Phase 7c two-body
potential and compute:

  - Deuteron binding energy B(²H)        [pn ³S₁ channel]
  - Triplet scattering length a_t        [pn ³S₁, low-energy limit]
  - Singlet scattering length a_s        [NN ¹S₀, low-energy limit]

Compare to observed:
  B(²H) = 2.224 MeV,  a_t = +5.42 fm,  a_s = -23.7 fm

V(r) construction (relativistic 7-tensor with Phase 7c kinematics):

    m²(k_S) = m²_Ma(n_pt, n_pr) + 4·(ℏc)²·k_S² + 2·k_S·σ_t·n_pt·ℏc
    V_eff(r) = m(r) - m_Ma  (subtract V(r→∞) so V_eff(∞) = 0)

For pn:    (n_pt, n_pr) = (6, 0)    — no σ_r term, no Coulomb
For pp:    (n_pt, n_pr) = (6, +4)   — adds α·ℏc/r Coulomb
For nn:    (n_pt, n_pr) = (6, -4)   — no Coulomb

Note on Ma-side offset:
  m_Ma(6, 0) = 1860.52 MeV;  (m_p + m_n) = 1877.84 MeV;
  Δ_Ma = -17.32 MeV  (R64 Ma already binds the (6, 0) compound by 17 MeV
  even at r → ∞, before σ_t coupling is added).
  Phase 7d's Schrödinger eigenvalue is the binding *above V(r=∞)*.
  Total binding from free-nucleon threshold = -E_eigen + |Δ_Ma|.

Polynomial 1/r tail caveat:
  V_eff(r) ~ A₁/r at large r (no exponential cutoff).  The scattering
  length is technically Coulomb-modified, not standard short-range.
  We compute effective-range parameters at finite k and report
  honestly — the limit k → 0 may not be cleanly defined.

Outputs:
  outputs/track7_phase7d_potential_and_wavefunctions.png
  outputs/track7_phase7d_results.csv
"""

import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


# ─── Constants ──────────────────────────────────────────────────────────

EPS_P = 0.2052
S_P = 0.0250
K_P = 63.629    # MeV/μ-unit

M_P = 938.272   # MeV
M_N = 939.565   # MeV
ALPHA = 1.0 / 137.035999084
HBAR_C = 197.3269804   # MeV·fm

A_KINETIC = 4.0 * HBAR_C**2   # Phase 7c two-body kinematic coefficient
SIGMA_T = -116.1              # Phase 7c best fit

# Reduced masses (relevant for COM Schrödinger)
MU_RED_PN = (M_P * M_N) / (M_P + M_N)
MU_RED_PP = M_P / 2.0
MU_RED_NN = M_N / 2.0

HBAR2_2MU_PN = HBAR_C**2 / (2 * MU_RED_PN)
HBAR2_2MU_PP = HBAR_C**2 / (2 * MU_RED_PP)
HBAR2_2MU_NN = HBAR_C**2 / (2 * MU_RED_NN)


# ─── Mass & potential ──────────────────────────────────────────────────

def m_Ma(n_pt, n_pr):
    mu2 = (n_pt / EPS_P)**2 + (n_pr - S_P * n_pt)**2
    return K_P * math.sqrt(mu2)


def V_compound(r, n_pt, n_pr):
    """Joint compound mass at S-separation r."""
    if r < 1e-6:
        return float('inf')
    m_ma = m_Ma(n_pt, n_pr)
    k = 1.0 / r
    m2 = m_ma**2 + A_KINETIC * k**2 + 2 * k * SIGMA_T * n_pt * HBAR_C
    if m2 <= 0:
        return float('inf')
    return math.sqrt(m2)


def V_eff(r, n_pt, n_pr, with_coulomb=False, charges=(0, 0)):
    """Effective Schrödinger potential: V(r) - V(infinity)."""
    nuclear = V_compound(r, n_pt, n_pr) - m_Ma(n_pt, n_pr)
    if with_coulomb and charges[0] != 0 and charges[1] != 0:
        coulomb = ALPHA * HBAR_C * charges[0] * charges[1] / r if r > 1e-6 else float('inf')
        return nuclear + coulomb
    return nuclear


def V_pn(r):
    return V_eff(r, 6, 0)


def V_pp(r):
    return V_eff(r, 6, +4, with_coulomb=True, charges=(1, 1))


def V_nn(r):
    return V_eff(r, 6, -4)


# ─── Radial Schrödinger solver ──────────────────────────────────────────

def shoot(E, V_func, hbar2_2mu, r_min=0.01, r_max=30.0):
    """Integrate radial SE from r_min outward with u(r_min)=0, u'(r_min)=1.
    Returns (u(r_max), full solution)."""

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
                      n_scan=400, r_max=30.0):
    """Find all bound states by scanning E and detecting sign changes
    in u(r_max)."""
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
    """Compute s-wave phase shift δ(k) by matching u(r) at large r
    to A·sin(k·r + δ)."""
    E = hbar2_2mu * k**2
    u_end, sol = shoot(E, V_func, hbar2_2mu, r_min=r_min, r_max=r_max)
    # Match at r_max: u = A sin(kr + δ), du = A k cos(kr + δ)
    # → tan(k·r + δ) = k·u/du
    # → δ = atan2(k·u, du) - k·r   (mod π)
    r_match = r_max
    u_m = sol.sol(r_match)[0]
    du_m = sol.sol(r_match)[1]
    phase = math.atan2(k * u_m, du_m)
    delta = phase - k * r_match
    # Normalize to (-π/2, π/2]
    while delta > math.pi / 2:
        delta -= math.pi
    while delta <= -math.pi / 2:
        delta += math.pi
    return delta


def compute_scattering_length(V_func, hbar2_2mu, ks=None, r_max=40.0):
    """Effective-range expansion: k·cot(δ) = -1/a + (r_e/2)·k² + O(k⁴).
    Returns (a, r_eff, raw_data)."""
    if ks is None:
        ks = np.linspace(0.005, 0.2, 12)  # fm⁻¹
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
    # Linear fit kcot = c0 + c1·k² → -1/a = c0, r_e/2 = c1
    p = np.polyfit(ks_v**2, kc_v, 1)
    c1, c0 = p[0], p[1]
    a = -1.0 / c0 if abs(c0) > 1e-12 else float('inf')
    r_eff = 2 * c1
    return a, r_eff, raw


# ─── Main ─────────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 7 Phase 7d — Schrödinger validation of Phase 7c V(r)")
    print("=" * 110)
    print()
    print(f"  Phase 7c parameters: σ_t = {SIGMA_T}, A = 4·(ℏc)² = {A_KINETIC:.0f} MeV²·fm²")
    print(f"  μ_red(pn) = {MU_RED_PN:.3f} MeV,  ℏ²/(2μ) = {HBAR2_2MU_PN:.3f} MeV·fm²")
    print()

    # ─── V_eff profile ────────────────────────────────────────────
    print("V_eff(r) profile [pn channel, MeV]:")
    print("-" * 60)
    rs = [0.4, 0.5, 0.7, 1.0, 1.135, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0]
    for r in rs:
        print(f"  r = {r:5.2f} fm: V_eff = {V_pn(r):+8.3f}")

    delta_ma_pn = m_Ma(6, 0) - (M_P + M_N)
    delta_ma_pp = m_Ma(6, +4) - 2 * M_P
    delta_ma_nn = m_Ma(6, -4) - 2 * M_N
    print()
    print(f"  Ma-side offsets (m_Ma - constituents, before S-coupling):")
    print(f"    Δ_Ma(pn) = {delta_ma_pn:+.3f} MeV")
    print(f"    Δ_Ma(pp) = {delta_ma_pp:+.3f} MeV")
    print(f"    Δ_Ma(nn) = {delta_ma_nn:+.3f} MeV")

    # ─── pn bound state (deuteron) ────────────────────────────────
    print()
    print("=" * 70)
    print("pn bound states (deuteron candidate)")
    print("=" * 70)
    pn_bs = find_bound_states(V_pn, HBAR2_2MU_PN,
                              E_range=(-35.0, -0.01), n_scan=600,
                              r_max=30.0)
    if pn_bs:
        E0 = pn_bs[0]
        print(f"  Bound states found: {len(pn_bs)}")
        for i, E in enumerate(pn_bs):
            print(f"    State {i}: E = {E:+.4f} MeV  (binding above V(∞) = {-E:.4f} MeV)")
        binding_total_pn = -E0 + (-delta_ma_pn)
        print()
        print(f"  Ground state E₀ = {E0:+.3f} MeV")
        print(f"  Binding above V(r=∞) threshold:           {-E0:.3f} MeV")
        print(f"  Total binding from free-nucleon threshold: {binding_total_pn:.3f} MeV")
        print(f"  Observed B(²H):                            2.224 MeV")
    else:
        print("  No bound states found in [-35, -0.01] MeV")
        E0 = None

    # ─── nn bound state ───────────────────────────────────────────
    print()
    print("nn bound states (singlet check):")
    nn_bs = find_bound_states(V_nn, HBAR2_2MU_NN,
                              E_range=(-35.0, -0.01), n_scan=400,
                              r_max=30.0)
    if nn_bs:
        for i, E in enumerate(nn_bs):
            print(f"    State {i}: E = {E:+.4f} MeV")
    else:
        print("  No nn bound states (consistent with observation: nn is unbound)")

    # ─── pp bound state ───────────────────────────────────────────
    print()
    print("pp bound states (singlet w/ Coulomb):")
    pp_bs = find_bound_states(V_pp, HBAR2_2MU_PP,
                              E_range=(-35.0, -0.01), n_scan=400,
                              r_max=30.0)
    if pp_bs:
        for i, E in enumerate(pp_bs):
            print(f"    State {i}: E = {E:+.4f} MeV")
    else:
        print("  No pp bound states (consistent with observation: pp is unbound)")

    # ─── Scattering lengths ───────────────────────────────────────
    print()
    print("=" * 70)
    print("Scattering length analysis (effective-range expansion)")
    print("=" * 70)
    print("Note: V(r) has 1/r polynomial tail; scattering length is")
    print("Coulomb-modified, not standard short-range — interpret with care.")
    print()

    # pn scattering (triplet, ³S₁): use V_pn (no Coulomb) at low k
    a_t, re_t, raw_t = compute_scattering_length(V_pn, HBAR2_2MU_PN,
                                                  ks=np.linspace(0.01, 0.15, 10),
                                                  r_max=40.0)
    print(f"  pn channel (triplet ³S₁):")
    print(f"    a_t (effective-range fit) = {a_t:+.3f} fm")
    print(f"    r_eff                     = {re_t:+.3f} fm")
    print(f"    Observed a_t              = +5.42 fm")
    print()

    # nn scattering (singlet, ¹S₀): use V_nn at low k
    a_s_nn, re_s_nn, raw_s_nn = compute_scattering_length(V_nn, HBAR2_2MU_NN,
                                                           ks=np.linspace(0.01, 0.15, 10),
                                                           r_max=40.0)
    print(f"  nn channel (singlet ¹S₀ analog, no Coulomb):")
    print(f"    a_s (effective-range fit) = {a_s_nn:+.3f} fm")
    print(f"    r_eff                     = {re_s_nn:+.3f} fm")
    print(f"    Observed a_s (np singlet) = -23.7 fm")
    print()

    # ─── Plot V(r) and wavefunction ───────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # V_eff(r) for all three channels
    ax = axes[0, 0]
    r_plot = np.linspace(0.3, 8.0, 400)
    V_pn_plot = [V_pn(r) for r in r_plot]
    V_pp_plot = [V_pp(r) for r in r_plot]
    V_nn_plot = [V_nn(r) for r in r_plot]
    ax.plot(r_plot, V_pn_plot, label='pn', linewidth=1.8)
    ax.plot(r_plot, V_pp_plot, label='pp (+ Coulomb)', linewidth=1.5,
            linestyle='--')
    ax.plot(r_plot, V_nn_plot, label='nn', linewidth=1.5, linestyle=':')
    ax.axhline(0, color='black', linewidth=0.5)
    if E0 is not None:
        ax.axhline(E0, color='red', linewidth=0.8, linestyle='-',
                   label=f'pn ground state E = {E0:.2f} MeV')
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('V_eff(r) (MeV)')
    ax.set_title('Phase 7c V(r) potential, all channels')
    ax.set_ylim(-50, 50)
    ax.set_xlim(0.3, 8)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

    # pn ground state wavefunction (if bound)
    ax = axes[0, 1]
    if E0 is not None:
        u_end, sol = shoot(E0, V_pn, HBAR2_2MU_PN, r_max=30.0)
        r_wf = np.linspace(0.01, 25, 400)
        u_wf = sol.sol(r_wf)[0]
        # Normalize
        norm = math.sqrt(np.trapezoid(u_wf**2, r_wf))
        u_wf = u_wf / norm
        ax.plot(r_wf, u_wf, color='blue', linewidth=1.8,
                label=f'pn ground state, E = {E0:.3f} MeV')
        ax.fill_between(r_wf, 0, u_wf, alpha=0.2, color='blue')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.set_xlabel('r (fm)')
        ax.set_ylabel('u(r) (normalized)')
        ax.set_title('pn ground-state wavefunction')
        ax.grid(alpha=0.3)
        ax.legend(fontsize=9)
    else:
        ax.text(0.5, 0.5, 'No pn bound state found',
                transform=ax.transAxes, ha='center', fontsize=11)
        ax.set_title('pn ground-state wavefunction')

    # k·cot(δ) vs k² for triplet
    ax = axes[1, 0]
    ks_arr = np.array([x[0] for x in raw_t if np.isfinite(x[2])])
    kc_arr = np.array([x[2] for x in raw_t if np.isfinite(x[2])])
    if len(ks_arr) > 2:
        ax.plot(ks_arr**2, kc_arr, 'o-', color='blue',
                label='pn triplet (Phase 7c V(r))')
        # Show fit
        p = np.polyfit(ks_arr**2, kc_arr, 1)
        ks_fine = np.linspace(0, ks_arr.max()**2, 100)
        ax.plot(ks_fine, p[1] + p[0] * ks_fine, '--', color='red',
                label=f'fit: -1/a = {p[1]:.3f} → a = {-1/p[1] if abs(p[1])>1e-9 else float("inf"):+.2f} fm')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('k² (fm⁻²)')
    ax.set_ylabel('k·cot(δ) (fm⁻¹)')
    ax.set_title('pn triplet effective-range expansion')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

    # Summary table
    ax = axes[1, 1]
    ax.axis('off')
    summary = [
        ['Quantity', 'Phase 7d', 'Observed', 'Comment'],
        ['B(²H) above V(∞)', f'{-E0:.2f} MeV' if E0 else 'no bound', '—', 'Schrödinger eigenvalue'],
        ['B(²H) total (incl. Δ_Ma)',
         f'{-E0 + abs(delta_ma_pn):.2f} MeV' if E0 else 'no bound',
         '2.22 MeV', 'Free-nucleon threshold'],
        ['a_t (triplet)', f'{a_t:+.2f} fm', '+5.42 fm', 'Coulomb-modified (1/r tail)'],
        ['a_s (nn singlet)', f'{a_s_nn:+.2f} fm', '-23.7 fm', 'Coulomb-modified'],
        ['nn bound states', f'{len(nn_bs)}', '0 (unbound)', 'should be 0'],
        ['pp bound states', f'{len(pp_bs)}', '0 (unbound)', 'should be 0'],
    ]
    cell_text = [row for row in summary]
    table = ax.table(cellText=cell_text, loc='center',
                     colWidths=[0.32, 0.20, 0.18, 0.30])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.5)
    ax.set_title('Phase 7d summary')

    plt.tight_layout()
    fig_path = out_dir / "track7_phase7d_potential_and_wavefunctions.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {fig_path}")

    # ─── CSV ──────────────────────────────────────────────────────
    csv_rows = [
        {'metric': 'sigma_t', 'value': SIGMA_T, 'unit': '(dimensionless)'},
        {'metric': 'A_kinetic', 'value': A_KINETIC, 'unit': 'MeV^2·fm^2'},
        {'metric': 'mu_red_pn', 'value': MU_RED_PN, 'unit': 'MeV'},
        {'metric': 'Delta_Ma_pn', 'value': delta_ma_pn, 'unit': 'MeV'},
        {'metric': 'E_ground_pn', 'value': E0 if E0 else None, 'unit': 'MeV'},
        {'metric': 'B_2H_above_threshold', 'value': -E0 if E0 else None, 'unit': 'MeV'},
        {'metric': 'B_2H_total', 'value': (-E0 + abs(delta_ma_pn)) if E0 else None, 'unit': 'MeV'},
        {'metric': 'B_2H_observed', 'value': 2.224, 'unit': 'MeV'},
        {'metric': 'a_triplet_phase7d', 'value': a_t, 'unit': 'fm'},
        {'metric': 'a_triplet_observed', 'value': 5.42, 'unit': 'fm'},
        {'metric': 'a_singlet_nn_phase7d', 'value': a_s_nn, 'unit': 'fm'},
        {'metric': 'a_singlet_observed', 'value': -23.7, 'unit': 'fm'},
        {'metric': 'nn_bound_states', 'value': len(nn_bs), 'unit': 'count'},
        {'metric': 'pp_bound_states', 'value': len(pp_bs), 'unit': 'count'},
    ]
    csv_path = out_dir / "track7_phase7d_results.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['metric', 'value', 'unit'])
        w.writeheader()
        w.writerows(csv_rows)
    print(f"  CSV: {csv_path}")

    # ─── Verdict ──────────────────────────────────────────────────
    print()
    print("=" * 110)
    print("VERDICT — Phase 7d")
    print("=" * 110)
    if E0 is not None:
        binding = -E0 + abs(delta_ma_pn)
        ratio = binding / 2.224
        print(f"  B(²H) [total, from free-nucleon threshold]: {binding:.2f} MeV")
        print(f"  Observed B(²H):                               2.22 MeV")
        print(f"  Ratio Phase 7d / observed:                    {ratio:.2f}×")
        if 0.8 <= ratio <= 1.2:
            print(f"  → PASS: B(²H) within ±20% of observed")
        elif 0.5 <= ratio <= 2.0:
            print(f"  → PARTIAL: B(²H) within factor 2")
        else:
            print(f"  → FAIL: B(²H) off by factor {ratio:.1f} — polynomial 1/r tail")
            print(f"    likely dominates; pool item m (Yukawa propagator) is the natural")
            print(f"    follow-on")
    else:
        print(f"  No pn bound state found — V(r) is too weak or the search range")
        print(f"  needs widening")
    print()
    print(f"  pn channel produces bound state(s): {len(pn_bs)} "
          f"(observed: 1 deuteron)")
    print(f"  nn channel produces bound state(s): {len(nn_bs)} "
          f"(observed: 0)")
    print(f"  pp channel produces bound state(s): {len(pp_bs)} "
          f"(observed: 0)")


if __name__ == "__main__":
    main()
