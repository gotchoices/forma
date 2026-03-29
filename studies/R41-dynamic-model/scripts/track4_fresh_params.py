#!/usr/bin/env python3
"""
R41 Track 4 — Fresh parameter determination

Re-derives geometry parameters from observed masses using both the
static and dynamic models.  No assumptions from previous studies —
the solver starts from a generic initial guess and converges.

The R27 baseline:
  - Targets: neutron (939.565 MeV) + muon (105.658 MeV)
  - Free params: r_p, σ_ep
  - Fixed: r_e = 0.5, r_nu = 5.0  (free but unconstrained)
  - Result: r_p ≈ 8.906, σ_ep ≈ -0.0906

We repeat this with dynamic='full' and dynamic='shortcut' to see
if the dynamic model shifts the optimal parameters.

We also attempt a broader fit with more targets and free params
to see if the dynamic model breaks degeneracies the static model
can't.

Usage:
    cd studies && python3 R41-dynamic-model/scripts/track4_fresh_params.py
"""

import sys, os, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../..')

from lib.ma_model import Ma, Target, M_E_MEV, M_P_MEV, M_N_MEV


# PDG 2022 masses (MeV)
M_MUON = 105.6584
M_NEUTRON = M_N_MEV    # 939.565

# Mode assignments
ELECTRON = (1, 2, 0, 0, 0, 0)
PROTON   = (0, 0, 0, 0, 1, 2)
NEUTRON  = (0, -2, 1, 0, 0, 2)
MUON     = (-1, 5, 0, 0, -2, 0)


def section(title):
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def print_fit_result(label, result, elapsed):
    print(f"--- {label} ---")
    if not result.converged:
        print(f"  *** DID NOT CONVERGE after {result.iterations} iterations ***")
        if result.ma is None:
            print("  No valid Ma produced.")
            return
    else:
        print(f"  Converged in {result.iterations} iterations ({elapsed*1000:.0f} ms)")

    p = result.params
    print(f"  r_e   = {p.get('r_e', '?')}")
    print(f"  r_nu  = {p.get('r_nu', '?')}")
    print(f"  r_p   = {p.get('r_p', '?'):.8f}" if isinstance(p.get('r_p'), float) else f"  r_p   = {p.get('r_p', '?')}")
    print(f"  σ_ep  = {p.get('sigma_ep', '?'):.8f}" if isinstance(p.get('sigma_ep'), float) else f"  σ_ep  = {p.get('sigma_ep', '?')}")

    m = result.ma
    print(f"\n  Residuals (MeV):")
    for i, r in enumerate(result.residuals):
        print(f"    target {i}: {r:+.6e} MeV")

    print(f"\n  Energies:")
    print(f"    E(electron) = {m.energy(ELECTRON):.6f} MeV  (target: {M_E_MEV:.6f})")
    print(f"    E(proton)   = {m.energy(PROTON):.3f} MeV  (target: {M_P_MEV:.3f})")
    print(f"    E(neutron)  = {m.energy(NEUTRON):.3f} MeV  (target: {M_NEUTRON:.3f})")
    print(f"    E(muon)     = {m.energy(MUON):.3f} MeV  (target: {M_MUON:.3f})")

    if m.dynamic:
        print(f"\n  Dynamic corrections:")
        for name, mode in [('electron', ELECTRON), ('proton', PROTON),
                           ('neutron', NEUTRON), ('muon', MUON)]:
            corr = m.dynamic_correction(mode)
            print(f"    δE/E({name:>8}) = {corr.delta_E_over_E:+.6e}")

    print()


def main():
    # ══════════════════════════════════════════════════════════════════
    section("1. REPRODUCE R27 BASELINE (static model)")
    # ══════════════════════════════════════════════════════════════════

    targets_R27 = [
        Target(n=NEUTRON, mass_MeV=M_NEUTRON),
        Target(n=MUON,    mass_MeV=M_MUON),
    ]

    t0 = time.perf_counter()
    result_static = Ma.fit(
        targets=targets_R27,
        free_params=['r_p', 'sigma_ep'],
        fixed_params={'r_e': 0.5, 'r_nu': 5.0},
        dynamic=False,
    )
    t_static = time.perf_counter() - t0
    print_fit_result("Static fit (R27 reproduction)", result_static, t_static)

    # ══════════════════════════════════════════════════════════════════
    section("2. SAME FIT WITH dynamic='shortcut'")
    # ══════════════════════════════════════════════════════════════════

    t0 = time.perf_counter()
    result_shortcut = Ma.fit(
        targets=targets_R27,
        free_params=['r_p', 'sigma_ep'],
        fixed_params={'r_e': 0.5, 'r_nu': 5.0},
        dynamic='shortcut',
    )
    t_shortcut = time.perf_counter() - t0
    print_fit_result("Dynamic fit (shortcut)", result_shortcut, t_shortcut)

    # ══════════════════════════════════════════════════════════════════
    section("3. SAME FIT WITH dynamic='full'")
    # ══════════════════════════════════════════════════════════════════

    t0 = time.perf_counter()
    result_full = Ma.fit(
        targets=targets_R27,
        free_params=['r_p', 'sigma_ep'],
        fixed_params={'r_e': 0.5, 'r_nu': 5.0},
        dynamic='full',
    )
    t_full = time.perf_counter() - t0
    print_fit_result("Dynamic fit (full)", result_full, t_full)

    # ══════════════════════════════════════════════════════════════════
    section("4. PARAMETER COMPARISON")
    # ══════════════════════════════════════════════════════════════════

    results = {
        'static': result_static,
        'shortcut': result_shortcut,
        'full': result_full,
    }

    print(f"{'Method':>10}  {'r_p':>14}  {'σ_ep':>14}  {'Converged':>10}  {'Iters':>6}")
    print(f"{'─'*10}  {'─'*14}  {'─'*14}  {'─'*10}  {'─'*6}")
    for label, res in results.items():
        if res.ma is None:
            print(f"{label:>10}  {'FAILED':>14}  {'':>14}  {'No':>10}")
            continue
        p = res.params
        print(f"{label:>10}  {p['r_p']:14.8f}  {p['sigma_ep']:14.8f}  "
              f"{'Yes' if res.converged else 'No':>10}  {res.iterations:6d}")

    # Parameter shifts
    if result_static.converged and result_full.converged:
        ps = result_static.params
        pf = result_full.params
        print(f"\n  Δr_p   (full − static) = {pf['r_p'] - ps['r_p']:+.6e}")
        print(f"  Δσ_ep  (full − static) = {pf['sigma_ep'] - ps['sigma_ep']:+.6e}")

    # ══════════════════════════════════════════════════════════════════
    section("5. ENERGY TABLE AT EACH SOLUTION")
    # ══════════════════════════════════════════════════════════════════

    particles = [
        ('electron', ELECTRON, M_E_MEV),
        ('proton',   PROTON,   M_P_MEV),
        ('neutron',  NEUTRON,  M_NEUTRON),
        ('muon',     MUON,     M_MUON),
    ]

    print(f"{'Particle':>10}  {'Target':>12}  ", end='')
    for label in results:
        print(f"{'E_'+label:>14}  ", end='')
    print()
    print(f"{'─'*10}  {'─'*12}  " + "  ".join(['─'*14]*len(results)))

    for name, mode, m_target in particles:
        print(f"{name:>10}  {m_target:12.3f}  ", end='')
        for label, res in results.items():
            if res.ma is None:
                print(f"{'—':>14}  ", end='')
            else:
                E = res.ma.energy(mode)
                print(f"{E:14.6f}  ", end='')
        print()

    # ══════════════════════════════════════════════════════════════════
    section("6. BROADER FIT: 3 TARGETS, 3 FREE PARAMS")
    # ══════════════════════════════════════════════════════════════════

    print("Adding electron as a target, freeing r_e.\n")

    targets_3 = [
        Target(n=ELECTRON, mass_MeV=M_E_MEV),
        Target(n=NEUTRON,  mass_MeV=M_NEUTRON),
        Target(n=MUON,     mass_MeV=M_MUON),
    ]

    for method, label in [(False, 'static'), ('full', 'full')]:
        t0 = time.perf_counter()
        res = Ma.fit(
            targets=targets_3,
            free_params=['r_e', 'r_p', 'sigma_ep'],
            fixed_params={'r_nu': 5.0},
            dynamic=method,
        )
        elapsed = time.perf_counter() - t0
        print_fit_result(f"3-target fit ({label})", res, elapsed)

    # ══════════════════════════════════════════════════════════════════
    section("7. STRESS TEST: r_p FROM DIFFERENT STARTING POINT")
    # ══════════════════════════════════════════════════════════════════

    print("Starting from r_p=5.0, σ_ep=0.0 (far from solution).\n")

    for method, label in [(False, 'static'), ('full', 'full')]:
        t0 = time.perf_counter()
        res = Ma.fit(
            targets=targets_R27,
            free_params=['r_p', 'sigma_ep'],
            fixed_params={'r_e': 0.5, 'r_nu': 5.0,
                          'r_p': 5.0, 'sigma_ep': 0.0},
            dynamic=method,
        )
        elapsed = time.perf_counter() - t0
        print_fit_result(f"Far start ({label})", res, elapsed)

    # ══════════════════════════════════════════════════════════════════
    section("SUMMARY")
    # ══════════════════════════════════════════════════════════════════

    print("Key questions for Track 4:")
    print("  1. Does the dynamic model shift r_p and σ_ep?")
    print("  2. If so, by how much relative to the static solution?")
    print("  3. Does the dynamic model break any degeneracies?")
    print("  4. Are the residuals smaller with the dynamic model?")
    print("  5. Is r_p still ~8.906 or has the dynamic correction moved it?")


if __name__ == '__main__':
    main()
