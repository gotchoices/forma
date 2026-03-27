#!/usr/bin/env python3
"""
R27 Track 4: Asymmetric cross-shears and the tau.

The tau mass (1776.9 MeV) falls between rungs of the proton-scale
energy ladder when symmetric cross-shears are used.  This script
investigates whether the 12 independent σ_ij entries (instead of
3 collective values) can close the 5.6% gap while keeping the
neutron and muon masses exact.

Sections:
    1. Validate asymmetric solver
    2. Scan e-p block asymmetries for tau
    3. Include e-ν and ν-p blocks
    4. Multi-target optimization (neutron + muon + tau)
    5. Summary
"""

import sys
import os
import numpy as np
from scipy.optimize import minimize, differential_evolution, brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6_solver import (
    self_consistent_metric, self_consistent_metric_asym,
    find_modes, CROSS_INDICES,
)
from lib.t6 import (
    mode_energy, mode_charge, mode_spin_label,
    M_P_MEV, M_E_MEV, M_N_MEV,
)

R_E, R_NU, R_P = 6.6, 5.0, 8.906
TARGET_DELTA = M_N_MEV - M_P_MEV  # 1.293 MeV
MUON_MASS = 105.658
TAU_MASS  = 1776.86

N_NEUTRON = np.array([0, -2, -5, -5, 0, 2], dtype=float)
N_MUON    = np.array([-1, 5, 0, 0, -2, 0], dtype=float)

# Tau candidates to test
TAU_CANDIDATES = [
    np.array([-1, 5, 0, 0, -2, -4], dtype=float),   # original (1876 MeV)
    np.array([-1, 3, 0, 0, -2, -4], dtype=float),
    np.array([-1, 0, 0, 0, -2, -4], dtype=float),
    np.array([-1, 5, -1, 0, -2, -4], dtype=float),   # with neutrino winding
    np.array([1, 5, 0, 0, 0, -4], dtype=float),       # different charge path
    np.array([-1, 5, 0, 0, -2, -3], dtype=float),     # n6=-3
    np.array([-1, 5, 0, 0, -4, -2], dtype=float),     # swapped proton windings
    np.array([-1, 5, 0, 0, 0, -4], dtype=float),      # no proton ring
    np.array([-3, 5, 0, 0, -4, -2], dtype=float),     # higher electron ring
]


def section(n, title):
    print(f"\n{'='*70}")
    print(f"  SECTION {n}: {title}")
    print(f"{'='*70}\n")


def check_three_masses(cross_shears, n_tau):
    """Compute neutron, muon, tau masses at given cross-shears."""
    sc = self_consistent_metric_asym(R_E, R_NU, R_P, cross_shears)
    if not sc['converged']:
        return None
    Gti = sc['Gtilde_inv']
    L = sc['L']
    E_n = mode_energy(N_NEUTRON, Gti, L)
    E_mu = mode_energy(N_MUON, Gti, L)
    E_tau = mode_energy(n_tau, Gti, L)
    return {
        'E_n': E_n, 'E_mu': E_mu, 'E_tau': E_tau,
        'delta_n': E_n - M_P_MEV,
        'err_mu': E_mu - MUON_MASS,
        'err_tau': (E_tau - TAU_MASS) / TAU_MASS * 100,
        'L': L,
    }


def main():
    # ── Section 1: Validate asymmetric solver ─────────────────────────
    section(1, "Validate asymmetric solver")

    # Symmetric case should reproduce known results
    sym_shears = {(0, 4): -0.09064, (0, 5): -0.09064,
                  (1, 4): -0.09064, (1, 5): -0.09064}
    sc_asym = self_consistent_metric_asym(R_E, R_NU, R_P, sym_shears)
    sc_sym = self_consistent_metric(R_E, R_NU, R_P, sigma_ep=-0.09064)

    E_n_asym = mode_energy(N_NEUTRON, sc_asym['Gtilde_inv'], sc_asym['L'])
    E_n_sym = mode_energy(N_NEUTRON, sc_sym['Gtilde_inv'], sc_sym['L'])

    print(f"  Symmetric σ_ep = -0.09064:")
    print(f"    Symmetric solver: E_n = {E_n_sym:.6f} MeV")
    print(f"    Asymmetric solver: E_n = {E_n_asym:.6f} MeV")
    print(f"    Match: {'✓' if abs(E_n_asym - E_n_sym) < 1e-6 else '✗'}")

    # ── Section 2: Scan e-p block asymmetries ─────────────────────────
    section(2, "E-P block asymmetry scan for tau")

    n_tau = TAU_CANDIDATES[0]  # (-1, 5, 0, 0, -2, -4)
    print(f"  Tau candidate: {tuple(int(x) for x in n_tau)}")
    print(f"  Symmetric prediction: 1876.4 MeV (target: {TAU_MASS})")
    print()

    # Scan: vary σ₁₅ and σ₂₆ independently while keeping σ₁₆=σ₂₅ at base
    base = -0.09064
    print(f"  {'σ₁₅':>8s} {'σ₁₆':>8s} {'σ₂₅':>8s} {'σ₂₆':>8s}  "
          f"{'E_tau':>10s} {'τ err%':>8s}  {'m_n-m_p':>10s} {'E_mu':>10s}")
    print(f"  {'-'*85}")

    best_tau_err = 100.0
    best_shears = None

    for d15 in np.arange(-0.15, 0.16, 0.05):
        for d26 in np.arange(-0.15, 0.16, 0.05):
            s15 = base + d15
            s16 = base
            s25 = base
            s26 = base + d26
            cs = {(0, 4): s15, (0, 5): s16, (1, 4): s25, (1, 5): s26}
            r = check_three_masses(cs, n_tau)
            if r is None:
                continue
            tau_err = abs(r['err_tau'])
            if tau_err < best_tau_err:
                best_tau_err = tau_err
                best_shears = cs.copy()
            if tau_err < 6.0:
                print(f"  {s15:+8.3f} {s16:+8.3f} {s25:+8.3f} {s26:+8.3f}  "
                      f"{r['E_tau']:10.1f} {r['err_tau']:+7.2f}%  "
                      f"{r['delta_n']:+10.4f} {r['E_mu']:10.3f}")

    print(f"\n  Best tau error from σ₁₅/σ₂₆ scan: {best_tau_err:.2f}%")

    # Now try all 4 e-p entries independently
    print(f"\n  Full 4-parameter scan (coarser grid):")
    print(f"  {'σ₁₅':>8s} {'σ₁₆':>8s} {'σ₂₅':>8s} {'σ₂₆':>8s}  "
          f"{'E_tau':>10s} {'τ err%':>8s}  {'m_n-m_p':>10s}")
    print(f"  {'-'*75}")

    best_tau_err = 100.0
    best_full = None
    offsets = np.arange(-0.20, 0.21, 0.10)
    for d15 in offsets:
        for d16 in offsets:
            for d25 in offsets:
                for d26 in offsets:
                    cs = {(0, 4): base + d15, (0, 5): base + d16,
                          (1, 4): base + d25, (1, 5): base + d26}
                    r = check_three_masses(cs, n_tau)
                    if r is None:
                        continue
                    tau_err = abs(r['err_tau'])
                    if tau_err < best_tau_err:
                        best_tau_err = tau_err
                        best_full = (cs.copy(), r)

    if best_full:
        cs, r = best_full
        print(f"  {cs[(0,4)]:+8.3f} {cs[(0,5)]:+8.3f} "
              f"{cs[(1,4)]:+8.3f} {cs[(1,5)]:+8.3f}  "
              f"{r['E_tau']:10.1f} {r['err_tau']:+7.2f}%  "
              f"{r['delta_n']:+10.4f}")
        print(f"\n  Best tau error from full e-p scan: {best_tau_err:.2f}%")

    # ── Section 3: Include other cross-blocks ─────────────────────────
    section(3, "Include e-ν and ν-p cross-shears")

    print("  Searching with all 12 cross-shear entries...")
    print("  Using differential_evolution on combined objective.\n")

    n_tau_test = TAU_CANDIDATES[0]

    def objective(params):
        """
        Minimize: (m_n - m_p - 1.293)² + (E_mu - 105.658)² + (E_tau/1776.9 - 1)²×1e6
        Params: 12 cross-shear entries.
        """
        cs = {}
        idx = 0
        for block_name in ['ep', 'enu', 'nup']:
            for (i, j) in CROSS_INDICES[block_name]:
                cs[(i, j)] = params[idx]
                idx += 1

        sc = self_consistent_metric_asym(R_E, R_NU, R_P, cs)
        if not sc['converged']:
            return 1e10

        Gti = sc['Gtilde_inv']
        L = sc['L']
        E_n = mode_energy(N_NEUTRON, Gti, L)
        E_mu = mode_energy(N_MUON, Gti, L)
        E_tau = mode_energy(n_tau_test, Gti, L)

        cost_n = ((E_n - M_P_MEV - TARGET_DELTA) / TARGET_DELTA) ** 2
        cost_mu = ((E_mu - MUON_MASS) / MUON_MASS) ** 2
        cost_tau = ((E_tau - TAU_MASS) / TAU_MASS) ** 2

        return cost_n * 1e6 + cost_mu * 1e6 + cost_tau * 1e6

    bounds = [(-0.3, 0.3)] * 12
    result = differential_evolution(
        objective, bounds, seed=42,
        maxiter=200, tol=1e-10, polish=True,
        workers=1,
    )

    cs_opt = {}
    idx = 0
    for block_name in ['ep', 'enu', 'nup']:
        for (i, j) in CROSS_INDICES[block_name]:
            cs_opt[(i, j)] = result.x[idx]
            idx += 1

    r = check_three_masses(cs_opt, n_tau_test)
    if r:
        print(f"  Optimization result (cost = {result.fun:.4e}):")
        print(f"    m_n - m_p = {r['delta_n']:+.4f} MeV  (target: {TARGET_DELTA:.3f})")
        print(f"    E_muon    = {r['E_mu']:.4f} MeV  (target: {MUON_MASS})")
        print(f"    E_tau     = {r['E_tau']:.1f} MeV  (target: {TAU_MASS})")
        print(f"    τ error   = {r['err_tau']:+.2f}%")
        print()
        print(f"  Cross-shear values:")
        for block_name in ['ep', 'enu', 'nup']:
            vals = [cs_opt[(i, j)] for (i, j) in CROSS_INDICES[block_name]]
            labels = [f"σ_{i+1}{j+1}" for (i, j) in CROSS_INDICES[block_name]]
            for lbl, val in zip(labels, vals):
                print(f"    {lbl} = {val:+.6f}")

    # ── Section 4: Try different tau modes with optimizer ─────────────
    section(4, "Test alternative tau modes with optimizer")

    print(f"  {'Mode':>35s}  {'E_tau':>10s}  {'τ err%':>8s}  "
          f"{'m_n-m_p':>10s}  {'E_mu':>10s}")
    print(f"  {'-'*80}")

    for n_tau_cand in TAU_CANDIDATES:
        Q = mode_charge(n_tau_cand)
        spin = mode_spin_label(n_tau_cand)
        if Q != -1:
            continue

        def obj_cand(params, n_t=n_tau_cand):
            cs = {}
            idx = 0
            for bn in ['ep', 'enu', 'nup']:
                for (i, j) in CROSS_INDICES[bn]:
                    cs[(i, j)] = params[idx]
                    idx += 1
            sc = self_consistent_metric_asym(R_E, R_NU, R_P, cs)
            if not sc['converged']:
                return 1e10
            Gti, L = sc['Gtilde_inv'], sc['L']
            E_n = mode_energy(N_NEUTRON, Gti, L)
            E_mu = mode_energy(N_MUON, Gti, L)
            E_tau = mode_energy(n_t, Gti, L)
            cost_n = ((E_n - M_P_MEV - TARGET_DELTA) / TARGET_DELTA) ** 2
            cost_mu = ((E_mu - MUON_MASS) / MUON_MASS) ** 2
            cost_tau = ((E_tau - TAU_MASS) / TAU_MASS) ** 2
            return cost_n * 1e6 + cost_mu * 1e6 + cost_tau * 1e6

        res = differential_evolution(
            obj_cand, bounds, seed=42,
            maxiter=100, tol=1e-10, polish=True, workers=1,
        )

        cs2 = {}
        idx = 0
        for bn in ['ep', 'enu', 'nup']:
            for (i, j) in CROSS_INDICES[bn]:
                cs2[(i, j)] = res.x[idx]
                idx += 1

        r2 = check_three_masses(cs2, n_tau_cand)
        if r2:
            ns = f"({int(n_tau_cand[0]):+d},{int(n_tau_cand[1]):+d}," \
                 f"{int(n_tau_cand[2]):+d},{int(n_tau_cand[3]):+d}," \
                 f"{int(n_tau_cand[4]):+d},{int(n_tau_cand[5]):+d})"
            print(f"  {ns:>35s}  {r2['E_tau']:10.1f}  {r2['err_tau']:+7.2f}%  "
                  f"{r2['delta_n']:+10.4f}  {r2['E_mu']:10.3f}")

    # ── Section 5: Summary ────────────────────────────────────────────
    section(5, "Summary")

    print("  Can asymmetric cross-shears close the tau gap?")
    print()
    if r and abs(r['err_tau']) < 1.0:
        print("  YES — the tau mass can be matched with asymmetric shears.")
        print(f"  Best tau error: {r['err_tau']:+.2f}%")
    else:
        print("  The tau gap may require higher quantum numbers (n_max > 5)")
        print("  or mechanisms beyond single-mode KK physics.")
        if r:
            print(f"  Best tau error achieved: {r['err_tau']:+.2f}%")


if __name__ == '__main__':
    main()
