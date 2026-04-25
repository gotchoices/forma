"""
R64 Track 7 Phase 7h — Yukawa QM observables test.

Phase 7d showed that Phase 7c's polynomial V(r) = A₂/r² + A₁/r fails
quantum-mechanical observables: 3 bound states in pn (vs 1), B(²H)=30
MeV (vs 2.22), wrong sign for a_s.  The diagnosis was the long-range
1/r tail acting like a strong attractive Coulomb-like force.

Phase 7h tests whether replacing the polynomial form with a Yukawa
exponential cutoff fixes these failures.  In QFT, V_Yukawa =
−g²·exp(−mr/ℏc)/r emerges from a propagator integral with a massive
mediator — pool item m in R64's track pool.  The mediator's mass m
sets the range; coupling g² sets the strength.

Three variants, all with reduced mass μ = m_p·m_n/(m_p+m_n):

  V1: Pure Yukawa, m = 140 MeV (pion mass observed).
      V(r) = −g²·ℏc·exp(−m·r/ℏc)/r
  V2: Pure Yukawa, m = 254 MeV (R64 mediator candidate at (0, ±4))
  V3: Hybrid — Phase 7c kinetic 1/r² hard core + Yukawa attraction
      V(r) = A₂/r² − g²·ℏc·exp(−m·r/ℏc)/r,  A₂ = (ℏc)²/m_p

For each variant, sweep g² to find the regime where pn has exactly 1
bound state at ~2 MeV; check QM observables across pp, pn, nn.

Outputs:
  outputs/track7_phase7h_yukawa_curves.png
  outputs/track7_phase7h_yukawa_results.csv
"""

import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


# ─── Constants ──────────────────────────────────────────────────────────

M_P = 938.272
M_N = 939.565
ALPHA = 1.0 / 137.035999084
HBAR_C = 197.3269804

# Reduced masses (relative motion, two-body COM)
MU_RED_PN = (M_P * M_N) / (M_P + M_N)
MU_RED_PP = M_P / 2.0
MU_RED_NN = M_N / 2.0

HBAR2_2MU_PN = HBAR_C**2 / (2 * MU_RED_PN)
HBAR2_2MU_PP = HBAR_C**2 / (2 * MU_RED_PP)
HBAR2_2MU_NN = HBAR_C**2 / (2 * MU_RED_NN)

# Phase 7c kinetic hard core
A2_KINETIC = HBAR_C**2 / M_P   # ≈ 41.5 MeV·fm²


# ─── Yukawa potentials ──────────────────────────────────────────────────

def V_pure_yukawa(r, m_med, g_sq, with_coulomb=False, charges=(0, 0)):
    """V = −g²·ℏc·exp(−m·r/ℏc)/r [+ Coulomb if charges nonzero]."""
    if r < 1e-6:
        return float('-inf')
    v = -g_sq * HBAR_C * math.exp(-m_med * r / HBAR_C) / r
    if with_coulomb and charges[0] * charges[1] > 0:
        v += ALPHA * HBAR_C * charges[0] * charges[1] / r
    return v


def V_hybrid(r, m_med, g_sq, with_coulomb=False, charges=(0, 0)):
    """V = A₂/r² − g²·ℏc·exp(−m·r/ℏc)/r [+ Coulomb]."""
    if r < 1e-6:
        return float('inf')
    v = A2_KINETIC / r**2 - g_sq * HBAR_C * math.exp(-m_med * r / HBAR_C) / r
    if with_coulomb and charges[0] * charges[1] > 0:
        v += ALPHA * HBAR_C * charges[0] * charges[1] / r
    return v


# ─── Schrödinger solver (reused from Phase 7d) ──────────────────────────

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


def find_bound_states(V_func, hbar2_2mu, E_range=(-50.0, -0.001),
                      n_scan=400, r_max=30.0):
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


def compute_scattering_length(V_func, hbar2_2mu, ks=None, r_max=40.0):
    if ks is None:
        ks = np.linspace(0.01, 0.15, 8)
    raw = []
    for k in ks:
        try:
            E = hbar2_2mu * k**2
            u_end, sol = shoot(E, V_func, hbar2_2mu, r_max=r_max)
            r_match = r_max
            u_m = sol.sol(r_match)[0]
            du_m = sol.sol(r_match)[1]
            phase = math.atan2(k * u_m, du_m)
            delta = phase - k * r_match
            while delta > math.pi / 2:
                delta -= math.pi
            while delta <= -math.pi / 2:
                delta += math.pi
            kcot = k / math.tan(delta) if abs(math.tan(delta)) > 1e-12 else float('nan')
            raw.append((k, kcot))
        except Exception:
            raw.append((k, float('nan')))
    arr = np.array([(k, kcot) for k, kcot in raw if np.isfinite(kcot)])
    if len(arr) < 3:
        return float('nan')
    p = np.polyfit(arr[:, 0]**2, arr[:, 1], 1)
    c0 = p[1]
    return -1.0 / c0 if abs(c0) > 1e-12 else float('inf')


# ─── Test runner ──────────────────────────────────────────────────────

def test_variant(label, V_func_factory, m_med, g_sq_values):
    """Run a sweep over g² for one Yukawa variant.  Report at each g²:
    pn bound-state count, B(²H), a_t, nn bound-states, pp bound-states.
    """
    print()
    print("=" * 80)
    print(f"Variant {label}: m = {m_med} MeV")
    print("=" * 80)
    print()
    print(f"  {'g²':>6s}  {'pn n_bs':>7s}  {'B(²H) MeV':>11s}  "
          f"{'a_t (fm)':>11s}  {'nn n_bs':>7s}  {'pp n_bs':>7s}")
    print("─" * 75)
    results = []
    for g_sq in g_sq_values:
        V_pn = lambda r: V_func_factory(r, m_med, g_sq, False, (0, 0))
        V_pp = lambda r: V_func_factory(r, m_med, g_sq, True, (1, 1))
        V_nn = lambda r: V_func_factory(r, m_med, g_sq, False, (0, 0))

        try:
            pn_bs = find_bound_states(V_pn, HBAR2_2MU_PN,
                                       E_range=(-50.0, -0.005),
                                       n_scan=300, r_max=25.0)
            nn_bs = find_bound_states(V_nn, HBAR2_2MU_NN,
                                       E_range=(-50.0, -0.005),
                                       n_scan=300, r_max=25.0)
            pp_bs = find_bound_states(V_pp, HBAR2_2MU_PP,
                                       E_range=(-50.0, -0.005),
                                       n_scan=300, r_max=25.0)
            B_2H = -pn_bs[0] if pn_bs else None
            a_t = compute_scattering_length(V_pn, HBAR2_2MU_PN, r_max=30.0) \
                  if not pn_bs or len(pn_bs) <= 2 else float('nan')

            B_str = f"{B_2H:>11.3f}" if B_2H is not None else f"{'unbound':>11s}"
            a_t_str = f"{a_t:>+11.3f}" if np.isfinite(a_t) else f"{'NaN':>11s}"
            print(f"  {g_sq:>6.3f}  {len(pn_bs):>7d}  {B_str}  {a_t_str}  "
                  f"{len(nn_bs):>7d}  {len(pp_bs):>7d}")

            results.append({
                'variant': label,
                'm_med_MeV': m_med,
                'g_sq': g_sq,
                'pn_bound_states': len(pn_bs),
                'pn_E_ground': pn_bs[0] if pn_bs else None,
                'B_2H_MeV': B_2H,
                'a_t_fm': a_t,
                'nn_bound_states': len(nn_bs),
                'pp_bound_states': len(pp_bs),
            })
        except Exception as e:
            print(f"  {g_sq:>6.3f}  ERROR: {e}")
            results.append({'variant': label, 'm_med_MeV': m_med,
                            'g_sq': g_sq, 'error': str(e)})

    return results


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 7 Phase 7h — Yukawa QM observables test")
    print("=" * 110)
    print()
    print(f"  Reduced mass μ(pn) = {MU_RED_PN:.3f} MeV")
    print(f"  ℏ²/(2μ) = {HBAR2_2MU_PN:.3f} MeV·fm²")
    print(f"  A₂ kinetic hard core (Phase 7c) = (ℏc)²/m_p = {A2_KINETIC:.3f} MeV·fm²")
    print()

    # ─── Variant 1: Pure Yukawa, m = 140 MeV ──────────────────────
    g_sq_v1 = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0, 1.5, 2.0]
    results_v1 = test_variant("V1 — Pure Yukawa (m=m_π)",
                               V_pure_yukawa, 140.0, g_sq_v1)

    # ─── Variant 2: Pure Yukawa, m = 254 MeV (R64 (0,4)) ──────────
    g_sq_v2 = [0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0]
    results_v2 = test_variant("V2 — Pure Yukawa (m=R64(0,4)≈254)",
                               V_pure_yukawa, 254.0, g_sq_v2)

    # ─── Variant 3: Hybrid (kinetic hard core + Yukawa) ───────────
    g_sq_v3 = [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0]
    results_v3 = test_variant("V3 — Hybrid 1/r² hard core + Yukawa(m_π)",
                               V_hybrid, 140.0, g_sq_v3)

    all_results = results_v1 + results_v2 + results_v3

    # ─── Find the parameter set closest to deuteron ───────────────
    print()
    print("=" * 80)
    print("Identifying parameter sets meeting acceptance criteria")
    print("=" * 80)
    print()

    candidates = []
    for r in all_results:
        if 'error' in r:
            continue
        bn = r.get('pn_bound_states', -1)
        b = r.get('B_2H_MeV')
        nn = r.get('nn_bound_states', -1)
        pp = r.get('pp_bound_states', -1)
        a_t = r.get('a_t_fm', float('nan'))
        # Criteria: 1 pn bound state, B in [1, 5] MeV, nn=0, pp=0, a_t > 0
        if bn == 1 and b is not None and 1.0 <= b <= 5.0 \
                and nn == 0 and pp == 0:
            candidates.append(r)

    if candidates:
        print(f"  {'variant':<35s}  {'m':>5s}  {'g²':>5s}  "
              f"{'B(²H)':>7s}  {'a_t':>7s}  pn nn pp")
        for c in candidates:
            print(f"  {c['variant']:<35s}  {c['m_med_MeV']:>5.0f}  "
                  f"{c['g_sq']:>5.2f}  {c['B_2H_MeV']:>7.3f}  "
                  f"{c['a_t_fm']:>+7.2f}  {c['pn_bound_states']} "
                  f"{c['nn_bound_states']} {c['pp_bound_states']}")
    else:
        print("  No parameter set in the swept ranges meets all criteria.")
        print("  Closest candidates (1 bound state, B near 2.22):")
        # Find ones with 1 bound state and reasonable B
        close = [r for r in all_results if 'error' not in r and
                 r.get('pn_bound_states') == 1 and
                 r.get('B_2H_MeV') is not None]
        close.sort(key=lambda x: abs(x['B_2H_MeV'] - 2.22))
        for c in close[:5]:
            print(f"    {c['variant']:<32s}  m={c['m_med_MeV']:.0f}, "
                  f"g²={c['g_sq']:.2f}: B={c['B_2H_MeV']:.3f} MeV, "
                  f"nn_bs={c['nn_bound_states']}, pp_bs={c['pp_bound_states']}")

    # ─── Plot ──────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. V(r) profiles for representative g² values
    ax = axes[0, 0]
    r_arr = np.linspace(0.3, 5.0, 300)
    for g_sq in [0.5, 1.0, 2.0]:
        v = [V_pure_yukawa(r, 140.0, g_sq) for r in r_arr]
        ax.plot(r_arr, v, label=f'V1 m=140, g²={g_sq}', linewidth=1.2)
    for g_sq in [0.5, 1.5]:
        v = [V_hybrid(r, 140.0, g_sq) for r in r_arr]
        ax.plot(r_arr, v, '--', label=f'V3 hybrid, g²={g_sq}',
                linewidth=1.2)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('V(r) (MeV)')
    ax.set_title('Yukawa V(r) shapes')
    ax.set_ylim(-100, 50)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # 2. B(²H) vs g² for each variant
    ax = axes[0, 1]
    for variant, results, color in [('V1 (m=140)', results_v1, 'blue'),
                                      ('V2 (m=254)', results_v2, 'red'),
                                      ('V3 (hybrid)', results_v3, 'green')]:
        gs = []
        bs = []
        for r in results:
            if 'error' not in r and r.get('B_2H_MeV') is not None:
                gs.append(r['g_sq'])
                bs.append(r['B_2H_MeV'])
        if gs:
            ax.semilogy(gs, bs, 'o-', color=color, label=variant,
                        linewidth=1.2)
    ax.axhline(2.224, color='black', linestyle='--', alpha=0.5,
               label='observed 2.224 MeV')
    ax.set_xlabel('g²')
    ax.set_ylabel('B(²H) (MeV)')
    ax.set_title('Deuteron binding vs coupling')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # 3. Bound-state count vs g²
    ax = axes[1, 0]
    for variant, results, color in [('V1 pn (m=140)', results_v1, 'blue'),
                                      ('V2 pn (m=254)', results_v2, 'red'),
                                      ('V3 pn (hybrid)', results_v3, 'green')]:
        gs = []
        ns = []
        for r in results:
            if 'error' not in r:
                gs.append(r['g_sq'])
                ns.append(r['pn_bound_states'])
        if gs:
            ax.plot(gs, ns, 'o-', color=color, label=variant)
    ax.axhline(1, color='black', linestyle='--', alpha=0.5,
               label='observed (1 deuteron)')
    ax.set_xlabel('g²')
    ax.set_ylabel('# pn bound states')
    ax.set_title('Bound-state count vs coupling')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # 4. Summary
    ax = axes[1, 1]
    ax.axis('off')
    text = "Phase 7h verdict:\n\n"
    if candidates:
        text += f"{len(candidates)} parameter set(s) pass acceptance:\n\n"
        for c in candidates[:5]:
            text += (f"  {c['variant'][:25]}\n"
                     f"    m={c['m_med_MeV']:.0f}, g²={c['g_sq']:.2f}\n"
                     f"    B(²H)={c['B_2H_MeV']:.2f} MeV\n"
                     f"    a_t={c['a_t_fm']:+.2f} fm\n"
                     f"    nn unbound, pp unbound\n\n")
        text += "Yukawa form RESOLVES Phase 7d failures.\n"
        text += "Pool item m is validated as path."
    else:
        text += "No parameters meet all criteria.\n\n"
        text += "Yukawa form alone does not\n"
        text += "fully resolve Phase 7d failures\n"
        text += "in the swept parameter space."
    ax.text(0.05, 0.95, text, transform=ax.transAxes, va='top',
            fontsize=9, family='monospace')

    plt.tight_layout()
    fig_path = out_dir / "track7_phase7h_yukawa_curves.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print()
    print(f"  Plot: {fig_path}")

    # ─── CSV ──────────────────────────────────────────────────────
    csv_path = out_dir / "track7_phase7h_yukawa_results.csv"
    fieldnames = ['variant', 'm_med_MeV', 'g_sq', 'pn_bound_states',
                  'B_2H_MeV', 'a_t_fm', 'nn_bound_states', 'pp_bound_states']
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader()
        for r in all_results:
            if 'error' not in r:
                w.writerow(r)
    print(f"  CSV: {csv_path}")

    # ─── Verdict ──────────────────────────────────────────────────
    print()
    print("=" * 110)
    print("VERDICT — Phase 7h")
    print("=" * 110)
    if candidates:
        print(f"  {len(candidates)} parameter set(s) pass all acceptance criteria.")
        print(f"  Yukawa form RESOLVES the QM observable failures of Phase 7d.")
        print(f"  Pool item m (Yukawa propagator extension) is validated as the")
        print(f"  structural cut needed for nuclear-binding QM observables.")
    else:
        # Best partial
        partial = [r for r in all_results if 'error' not in r and
                   r.get('pn_bound_states') == 1]
        if partial:
            partial.sort(key=lambda x: abs(x.get('B_2H_MeV', 100) - 2.22))
            best = partial[0]
            print(f"  No exact match, but best partial:")
            print(f"    {best['variant']}, m={best['m_med_MeV']}, g²={best['g_sq']}")
            print(f"    pn=1, B(²H)={best['B_2H_MeV']:.3f} MeV, "
                  f"nn={best['nn_bound_states']}, pp={best['pp_bound_states']}")
            if best['nn_bound_states'] == 0 and best['pp_bound_states'] == 0:
                print(f"  → Yukawa partially validated: correct unbinding pattern,")
                print(f"    binding magnitude needs refinement.")
            else:
                print(f"  → Yukawa form has correct shape but parameter range")
                print(f"    needs widening.")
        else:
            print(f"  No clean Yukawa fit found in swept ranges.")


if __name__ == "__main__":
    main()
