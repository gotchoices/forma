"""
R53 Track 1: Solve for (ε, s) that produce three lepton generations

ANALYTIC approach:  For modes A=(p,q), B=(r,t), C=(u,v) on one sheet:

    μ² = (n_t/ε)² + (n_r − n_t·s)²

Let x = 1/ε².  The two ratio equations μ_B/μ_A = R1, μ_C/μ_A = R2
are linear in x and s (after squaring), giving a 2×2 system that
can be solved exactly for each triple.  No grid search needed.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from lib.ma_model_d import alpha_from_geometry


M_E = 0.51099895
M_MU = 105.65837
M_TAU = 1776.86

R_MU = M_MU / M_E    # 206.768
R_TAU = M_TAU / M_E   # 3477.23


def mu2(nt, nr, eps, s):
    return (nt / eps) ** 2 + (nr - nt * s) ** 2


def solve_triple(e_mode, mu_mode, tau_mode):
    """
    Solve for (ε, s) such that:
        μ(mu_mode)  / μ(e_mode) = R_MU
        μ(tau_mode) / μ(e_mode) = R_TAU

    Returns list of (ε, s) solutions (may be 0, 1, or 2).
    """
    p, q = e_mode    # electron (n_t, n_r)
    r, t = mu_mode   # muon
    u, v = tau_mode   # tau

    # μ² = n_t²·x + (n_r - n_t·s)²  where x = 1/ε²
    # Let's expand:
    # μ_A² = p²x + (q - p·s)² = p²x + q² - 2pqs + p²s²
    # μ_B² = r²x + (t - r·s)² = r²x + t² - 2rts + r²s²
    # μ_C² = u²x + (v - u·s)² = u²x + v² - 2uvs + u²s²
    #
    # Condition: μ_B² = R1² · μ_A²  and  μ_C² = R2² · μ_A²
    #
    # μ_B² - R1²·μ_A² = 0:
    # (r² - R1²p²)x + (t² - R1²q²) - 2s(rt - R1²pq) + s²(r² - R1²p²) = 0
    #
    # Let: a1 = r² - R1²p²,  b1 = t² - R1²q²,  c1 = rt - R1²pq
    # Then: a1·x + b1 - 2c1·s + a1·s² = 0
    # → a1(x + s²) - 2c1·s + b1 = 0  ... (I)
    #
    # Similarly for tau:
    # a2(x + s²) - 2c2·s + b2 = 0     ... (II)
    # where a2 = u² - R2²p², b2 = v² - R2²q², c2 = uv - R2²pq

    R1sq = R_MU ** 2
    R2sq = R_TAU ** 2

    a1 = r**2 - R1sq * p**2
    b1 = t**2 - R1sq * q**2
    c1 = r * t - R1sq * p * q

    a2 = u**2 - R2sq * p**2
    b2 = v**2 - R2sq * q**2
    c2 = u * v - R2sq * p * q

    # From (I): a1·w - 2c1·s + b1 = 0  where w = x + s²
    # From (II): a2·w - 2c2·s + b2 = 0
    #
    # This is a linear system in (w, s):
    # | a1  -2c1 | | w |   | -b1 |
    # | a2  -2c2 | | s | = | -b2 |

    det = a1 * (-2 * c2) - a2 * (-2 * c1)
    det = -2 * (a1 * c2 - a2 * c1)

    if abs(det) < 1e-20:
        return []

    w = (-b1 * (-2 * c2) - (-b2) * (-2 * c1)) / det
    w = (2 * b1 * c2 - 2 * b2 * c1) / det

    s_val = (a1 * (-b2) - a2 * (-b1)) / det
    s_val = (-a1 * b2 + a2 * b1) / det

    # w = x + s², so x = w - s²
    x = w - s_val ** 2

    if x < 0:
        return []  # ε² = 1/x would be negative

    eps = 1.0 / math.sqrt(x) if x > 1e-30 else 1e15  # huge ε if x≈0

    # Verify
    me = math.sqrt(mu2(*e_mode, eps, s_val))
    mm = math.sqrt(mu2(*mu_mode, eps, s_val))
    mt = math.sqrt(mu2(*tau_mode, eps, s_val))

    if me < 1e-15:
        return []

    r_mu_check = mm / me
    r_tau_check = mt / me

    err_mu = abs(r_mu_check / R_MU - 1)
    err_tau = abs(r_tau_check / R_TAU - 1)

    if err_mu < 0.01 and err_tau < 0.01:
        return [(eps, s_val, err_mu, err_tau)]
    return []


def main():
    print("=" * 78)
    print("R53 Track 1: Three lepton generations from in-sheet shear")
    print("=" * 78)
    print()
    print(f"  Target: m_μ/m_e = {R_MU:.3f},  m_τ/m_e = {R_TAU:.2f}")
    print(f"  Target: m_τ/m_μ = {M_TAU/M_MU:.4f}")
    print()

    # Generate ALL spin-½ modes with |n_t| ≤ 7 (odd), |n_r| ≤ 50
    modes = []
    for nt in range(-7, 8):
        if nt == 0 or abs(nt) % 2 == 0:
            continue
        for nr in range(-50, 51):
            modes.append((nt, nr))

    print(f"  Candidate modes: {len(modes)} (|n_t| ≤ 7 odd, |n_r| ≤ 50)")
    print()

    # Test all ordered triples (e, μ, τ) from this pool
    solutions = []
    n_tested = 0

    for i, e_mode in enumerate(modes):
        for j, mu_mode in enumerate(modes):
            if j == i:
                continue
            for k, tau_mode in enumerate(modes):
                if k == i or k == j:
                    continue

                sols = solve_triple(e_mode, mu_mode, tau_mode)
                for (eps, s, err_mu, err_tau) in sols:
                    if eps <= 0 or eps > 1e8:
                        continue

                    # Compute α
                    try:
                        a = alpha_from_geometry(eps, s,
                                                n_tube=e_mode[0],
                                                n_ring=e_mode[1])
                    except Exception:
                        a = float('nan')

                    # Fundamentalness: prefer small total quantum numbers
                    max_nr = max(abs(e_mode[1]), abs(mu_mode[1]),
                                 abs(tau_mode[1]))
                    max_nt = max(abs(e_mode[0]), abs(mu_mode[0]),
                                 abs(tau_mode[0]))
                    total = sum(abs(n) for m in (e_mode, mu_mode, tau_mode)
                                for n in m)

                    solutions.append({
                        'e': e_mode, 'mu': mu_mode, 'tau': tau_mode,
                        'eps': eps, 's': s,
                        'err_mu': err_mu, 'err_tau': err_tau,
                        'alpha': a,
                        'max_nr': max_nr, 'max_nt': max_nt,
                        'total': total,
                    })

                n_tested += 1

        if (i + 1) % 20 == 0:
            print(f"  Progress: e-mode {i+1}/{len(modes)}, "
                  f"{len(solutions)} solutions so far...")

    print(f"\n  Total triples tested: ~{n_tested:,}")
    print(f"  Solutions found: {len(solutions)}")
    print()

    if not solutions:
        print("  NO SOLUTIONS FOUND.")
        print("  The three-generation hypothesis does not work for any")
        print("  triple with |n_t| ≤ 7 and |n_r| ≤ 50.")
        print()
        print("Track 1 complete.")
        return

    # ── Sort by fundamentalness (smallest max ring winding) ─────────
    solutions.sort(key=lambda x: (x['max_nr'], x['max_nt'], x['total']))

    # Deduplicate (same triple at same ε, s)
    unique = []
    for sol in solutions:
        is_dup = False
        for u in unique:
            if (sol['e'] == u['e'] and sol['mu'] == u['mu']
                    and sol['tau'] == u['tau']):
                is_dup = True
                break
        if not is_dup:
            unique.append(sol)

    print(f"  Unique solutions: {len(unique)}")
    print()

    # ── Report top solutions ────────────────────────────────────────
    print("=" * 78)
    print("Top 40 solutions (sorted by max |n_r| — most fundamental first)")
    print("=" * 78)
    print()
    print(f"  {'electron':>10s}  {'muon':>10s}  {'tau':>10s}  "
          f"{'ε':>10s}  {'s':>10s}  "
          f"{'1/α':>8s}  {'max_nr':>6s}  {'total':>5s}")
    print(f"  {'─'*10}  {'─'*10}  {'─'*10}  "
          f"{'─'*10}  {'─'*10}  "
          f"{'─'*8}  {'─'*6}  {'─'*5}")

    for sol in unique[:40]:
        a = sol['alpha']
        inv_a = 1.0 / a if (a > 0 and not math.isnan(a)) else float('nan')
        print(f"  {str(sol['e']):>10s}  {str(sol['mu']):>10s}  "
              f"{str(sol['tau']):>10s}  "
              f"{sol['eps']:>10.3f}  {sol['s']:>10.6f}  "
              f"{inv_a:>8.2f}  "
              f"{sol['max_nr']:>6d}  {sol['total']:>5d}")
    print()

    # ── Highlight the most fundamental ──────────────────────────────
    print("=" * 78)
    print("Most fundamental solution (smallest max |n_r|)")
    print("=" * 78)
    best = unique[0]
    a = best['alpha']
    inv_a = 1.0 / a if (a > 0 and not math.isnan(a)) else float('nan')
    print(f"  Electron: {best['e']}")
    print(f"  Muon:     {best['mu']}")
    print(f"  Tau:      {best['tau']}")
    print(f"  ε = {best['eps']:.6f}")
    print(f"  s = {best['s']:.6f}")
    print()

    # Predicted masses
    eps, s = best['eps'], best['s']
    me = math.sqrt(mu2(*best['e'], eps, s))
    mm = math.sqrt(mu2(*best['mu'], eps, s))
    mt = math.sqrt(mu2(*best['tau'], eps, s))
    scale = M_E / me
    print(f"  Predicted masses (scaled so electron = {M_E:.4f} MeV):")
    print(f"    electron: {scale*me:.4f} MeV  (input)")
    print(f"    muon:     {scale*mm:.4f} MeV  (obs: {M_MU:.4f})")
    print(f"    tau:      {scale*mt:.4f} MeV  (obs: {M_TAU:.4f})")
    print()
    print(f"  α at this geometry: {a:.6f}  (1/α = {inv_a:.2f})")
    print(f"  Target: 1/α = 137.036")
    print()

    # ── Analysis: what ε and s ranges appear? ───────────────────────
    print("=" * 78)
    print("Parameter ranges across all solutions")
    print("=" * 78)
    eps_vals = [s['eps'] for s in unique if s['eps'] < 1e6]
    s_vals = [s['s'] for s in unique]
    if eps_vals:
        print(f"  ε range: [{min(eps_vals):.3f}, {max(eps_vals):.3f}]")
        print(f"  s range: [{min(s_vals):.4f}, {max(s_vals):.4f}]")
    print()

    # ── Special interest: solutions with ε < 10 ────────────────────
    compact = [s for s in unique if s['eps'] < 10]
    print(f"  Solutions with ε < 10: {len(compact)}")
    for sol in compact[:20]:
        a = sol['alpha']
        inv_a = 1.0 / a if (a > 0 and not math.isnan(a)) else float('nan')
        print(f"    {str(sol['e']):>10s} {str(sol['mu']):>10s} "
              f"{str(sol['tau']):>10s}  "
              f"ε={sol['eps']:>8.3f}  s={sol['s']:>10.5f}  "
              f"1/α={inv_a:>8.2f}")
    print()

    print("Track 1 complete.")


if __name__ == '__main__':
    main()
