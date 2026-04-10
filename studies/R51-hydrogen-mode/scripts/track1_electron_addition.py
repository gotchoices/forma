"""
R51 Track 1: Energy cost of adding an electron to a proton

Computes two quantities as functions of σ_ep for both proton
hypotheses ((1,3) and (3,6)):

  ΔE_add(σ) = E(1,2,0,0,n₅,n₆; σ) − E(0,0,0,0,n₅,n₆; σ)
    "How much heavier does the proton become when we add an
    electron quantum to the compound mode?"

  I.E.(σ) = E_e(σ) + E_p(σ) − E_H(σ)
    "How much energy is released when free e⁻ + free p combine
    into the compound mode?"

At σ = 0 (no coupling):
  ΔE_add = m_e²/(2m_p) ≈ 139 eV  (quadrature baseline)
  I.E.   = m_e − m_e²/(2m_p) ≈ 511 keV  (kinematic "binding")

Target: 13.6 eV (hydrogen ionization energy).
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np

from lib.ma_model_d import (
    MaD, M_E_MEV, M_P_MEV, DM2_21,
    _TWO_PI_HC, _build_circumferences, _build_metric,
    solve_shear_for_alpha,
)

EPS_E, EPS_NU, EPS_P = 0.65, 5.0, 0.55
S_NU_DEFAULT = 0.022

PROTON_MODES = [(1, 3), (3, 6)]

MEV_TO_EV = 1e6


def build_model(n_p, sigma_ep=0.0):
    """Build MaD with L_ring derived self-consistently."""
    s_e = solve_shear_for_alpha(EPS_E)
    # NOTE (Q114 §11.5): pass proton mode through; previous version
    # silently used the (1,2) shear for the proton.
    s_p = solve_shear_for_alpha(EPS_P, n_tube=n_p[0], n_ring=n_p[1])
    s_nu = S_NU_DEFAULT

    if s_e is None or s_p is None:
        return None

    L_dummy = _build_circumferences(
        EPS_E, s_e, 1.0, EPS_NU, s_nu, 1.0, EPS_P, s_p, 1.0)
    Gt, Gti = _build_metric(
        L_dummy, s_e, s_nu, s_p, sigma_ep=sigma_ep)
    if Gt is None:
        return None

    n_e_d = np.array([1.0 / EPS_E, 2.0, 0, 0, 0, 0])
    mu_eff_e = math.sqrt(float(n_e_d @ Gti @ n_e_d))
    L_ring_e = _TWO_PI_HC * mu_eff_e / M_E_MEV

    n_p_d = np.array([0, 0, 0, 0, float(n_p[0]) / EPS_P, float(n_p[1])])
    mu_eff_p = math.sqrt(float(n_p_d @ Gti @ n_p_d))
    L_ring_p = _TWO_PI_HC * mu_eff_p / M_P_MEV

    E0_nu_MeV = math.sqrt(DM2_21 / (4 * s_nu)) * 1e-6
    L_ring_nu = _TWO_PI_HC / E0_nu_MeV

    try:
        model = MaD(
            eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
            s_e=s_e, s_nu=s_nu, s_p=s_p,
            L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
            sigma_ep=sigma_ep)
        model._n_p = n_p
    except ValueError:
        return None

    return model


def compute_energies(model, n_p):
    """Compute E_proton, E_electron, E_compound for hydrogen."""
    mode_proton   = (0, 0, 0, 0, n_p[0], n_p[1])
    mode_electron = (1, 2, 0, 0, 0, 0)
    mode_hydrogen = (1, 2, 0, 0, n_p[0], n_p[1])

    E_p = model.energy(mode_proton)
    E_e = model.energy(mode_electron)
    E_H = model.energy(mode_hydrogen)

    return E_p, E_e, E_H


def run_sweep(n_p, sigma_values):
    """Sweep σ_ep and compute ΔE_add and I.E. at each point."""
    label = f"({n_p[0]},{n_p[1]})"
    print(f"\n{'='*72}")
    print(f"  Proton hypothesis: {label}")
    print(f"{'='*72}")

    # Theoretical baseline at σ=0
    dE_theory = (M_E_MEV**2 / (2 * M_P_MEV)) * MEV_TO_EV
    IE_theory = (M_E_MEV - M_E_MEV**2 / (2 * M_P_MEV)) * MEV_TO_EV
    print(f"\n  Theoretical σ=0 baseline:")
    print(f"    ΔE_add = m_e²/(2m_p) = {dE_theory:.3f} eV")
    print(f"    I.E.   = m_e − m_e²/(2m_p) = {IE_theory:.1f} eV")

    results = []

    for sigma in sigma_values:
        model = build_model(n_p, sigma_ep=sigma)
        if model is None:
            results.append(None)
            continue

        E_p, E_e, E_H = compute_energies(model, n_p)

        dE_add_eV = (E_H - E_p) * MEV_TO_EV
        IE_eV = (E_e + E_p - E_H) * MEV_TO_EV

        results.append({
            'sigma': sigma,
            'E_p': E_p,
            'E_e': E_e,
            'E_H': E_H,
            'dE_add_eV': dE_add_eV,
            'IE_eV': IE_eV,
        })

    # Print full table
    valid = [r for r in results if r is not None]
    print(f"\n  σ_ep sweep ({len(valid)} valid points):\n")
    print(f"  {'σ_ep':>8s}  {'E_p (MeV)':>14s}  {'E_e (MeV)':>14s}  "
          f"{'E_H (MeV)':>14s}  {'ΔE_add (eV)':>13s}  {'I.E. (eV)':>13s}")
    print(f"  {'─'*8}  {'─'*14}  {'─'*14}  {'─'*14}  {'─'*13}  {'─'*13}")

    for r in valid:
        print(f"  {r['sigma']:+8.4f}  {r['E_p']:14.9f}  {r['E_e']:14.9f}  "
              f"{r['E_H']:14.9f}  {r['dE_add_eV']:13.4f}  {r['IE_eV']:13.4f}")

    # Find closest approach to 13.6 eV for each metric
    target = 13.6

    # ΔE_add closest to 13.6
    by_dE = sorted(valid, key=lambda r: abs(r['dE_add_eV'] - target))
    if by_dE:
        best = by_dE[0]
        print(f"\n  ΔE_add closest to {target} eV:")
        print(f"    σ_ep = {best['sigma']:+.4f},  ΔE_add = {best['dE_add_eV']:.4f} eV  "
              f"(off by {best['dE_add_eV'] - target:+.4f} eV)")

    # I.E. closest to 13.6
    by_IE = sorted(valid, key=lambda r: abs(r['IE_eV'] - target))
    if by_IE:
        best = by_IE[0]
        print(f"\n  I.E. closest to {target} eV:")
        print(f"    σ_ep = {best['sigma']:+.4f},  I.E. = {best['IE_eV']:.4f} eV  "
              f"(off by {best['IE_eV'] - target:+.4f} eV)")

    # Behavior at key σ values
    print(f"\n  Key σ_ep values:")
    for sig_target in [0.0, -0.13, -0.27, -0.28]:
        matches = [r for r in valid if abs(r['sigma'] - sig_target) < 0.001]
        if matches:
            r = matches[0]
            print(f"    σ_ep = {r['sigma']:+.4f}:  "
                  f"ΔE_add = {r['dE_add_eV']:.4f} eV,  "
                  f"I.E. = {r['IE_eV']:.4f} eV")

    return valid


def decompose_at_sigma(n_p, sigma):
    """Detailed energy decomposition at a specific σ_ep."""
    model = build_model(n_p, sigma_ep=sigma)
    if model is None:
        return

    label = f"({n_p[0]},{n_p[1]})"

    mode_proton   = (0, 0, 0, 0, n_p[0], n_p[1])
    mode_electron = (1, 2, 0, 0, 0, 0)
    mode_hydrogen = (1, 2, 0, 0, n_p[0], n_p[1])

    print(f"\n  Energy decomposition at σ_ep = {sigma:+.4f} [{label}]:")

    for name, mode in [("Proton", mode_proton),
                       ("Electron", mode_electron),
                       ("Hydrogen", mode_hydrogen)]:
        E = model.energy(mode)
        decomp = model.energy_decomp(mode)
        print(f"\n    {name} {mode}:")
        print(f"      E = {E:.12f} MeV  ({E * MEV_TO_EV:.3f} eV)")
        print(f"      E² contributions (MeV²):")
        for key in ['e', 'nu', 'p']:
            val = decomp[key]
            if abs(val) > 1e-30:
                print(f"        {key:>3s}: {val:+.12e}")
        for key in ['ep', 'enu', 'nup']:
            val = decomp[key]
            if abs(val) > 1e-30:
                print(f"        {key:>3s}: {val:+.12e}  (cross-sheet)")


def main():
    print("=" * 72)
    print("R51 Track 1: Energy cost of adding an electron to a proton")
    print("=" * 72)
    print()
    print("Premise: atoms are compound tori modes, not spatial structures.")
    print("Hydrogen = mode (1,2,0,0,n₅,n₆) on the coupled 6-torus.")
    print()
    print(f"Reference values:")
    print(f"  m_e = {M_E_MEV:.6f} MeV = {M_E_MEV * MEV_TO_EV:.1f} eV")
    print(f"  m_p = {M_P_MEV:.6f} MeV = {M_P_MEV * MEV_TO_EV:.1f} eV")
    print(f"  m_e²/(2m_p) = {M_E_MEV**2 / (2 * M_P_MEV) * MEV_TO_EV:.3f} eV")
    print(f"  Target: H ionization energy = 13.600 eV")

    # Fine sweep of σ_ep
    sigma_values = np.concatenate([
        np.linspace(0.0, -0.30, 151),
        np.linspace(0.001, 0.30, 150),
    ])
    sigma_values = np.sort(np.unique(np.round(sigma_values, 6)))

    all_results = {}
    for n_p in PROTON_MODES:
        results = run_sweep(n_p, sigma_values)
        all_results[n_p] = results

    # Decompositions at key σ values
    print(f"\n\n{'='*72}")
    print("DETAILED DECOMPOSITION")
    print(f"{'='*72}")

    for n_p in PROTON_MODES:
        for sigma in [0.0, -0.28]:
            decompose_at_sigma(n_p, sigma)

    # Comparison
    print(f"\n\n{'='*72}")
    print("COMPARISON: ΔE_add at σ_ep = 0 and σ_ep = −0.28")
    print(f"{'='*72}\n")

    print(f"  {'Hypothesis':>12s}  {'σ_ep':>8s}  {'ΔE_add (eV)':>13s}  "
          f"{'I.E. (eV)':>13s}  {'Target':>8s}  {'Ratio':>8s}")
    print(f"  {'─'*12}  {'─'*8}  {'─'*13}  {'─'*13}  {'─'*8}  {'─'*8}")

    for n_p in PROTON_MODES:
        label = f"({n_p[0]},{n_p[1]})"
        for sig_target in [0.0, -0.28]:
            results = all_results[n_p]
            matches = [r for r in results if abs(r['sigma'] - sig_target) < 0.001]
            if matches:
                r = matches[0]
                ratio = r['dE_add_eV'] / 13.6
                print(f"  {label:>12s}  {r['sigma']:+8.4f}  "
                      f"{r['dE_add_eV']:13.4f}  {r['IE_eV']:13.4f}  "
                      f"{'13.6':>8s}  {ratio:8.2f}×")

    # Check: does ΔE_add or I.E. ever reach 13.6 eV?
    print(f"\n\n{'='*72}")
    print("ASSESSMENT")
    print(f"{'='*72}\n")

    for n_p in PROTON_MODES:
        label = f"({n_p[0]},{n_p[1]})"
        results = all_results[n_p]

        dE_range = [r['dE_add_eV'] for r in results]
        IE_range = [r['IE_eV'] for r in results]

        print(f"  {label}:")
        print(f"    ΔE_add range: [{min(dE_range):.3f}, {max(dE_range):.3f}] eV")
        print(f"    I.E. range:   [{min(IE_range):.1f}, {max(IE_range):.1f}] eV")

        if min(dE_range) <= 13.6 <= max(dE_range):
            print(f"    ΔE_add CROSSES 13.6 eV!")
        elif min(dE_range) > 13.6:
            print(f"    ΔE_add minimum ({min(dE_range):.3f} eV) is "
                  f"{min(dE_range)/13.6:.1f}× above target")
        else:
            print(f"    ΔE_add maximum ({max(dE_range):.3f} eV) is "
                  f"below target")

        if min(IE_range) <= 13.6 <= max(IE_range):
            print(f"    I.E. CROSSES 13.6 eV!")
        else:
            closest = min(IE_range, key=lambda x: abs(x - 13.6))
            print(f"    I.E. closest to 13.6: {closest:.1f} eV "
                  f"({closest/13.6:.1f}× target)")
        print()

    print("=" * 72)
    print("Track 1 complete.")
    print("=" * 72)


if __name__ == '__main__':
    main()
