"""
R51 Track 1a: Per-sheet energy decomposition and the α² question

Four analyses:
1. Analytical cross-term: extract the off-diagonal block of G̃⁻¹
   and compute E²_cross explicitly for the hydrogen mode
2. α² check: does the cross-term scale as α² when α is varied?
3. Fixed-L computation: no L_ring recalibration, exposing the
   raw Schur complement correction
4. Mode-winding comparison: hydrogen vs neutron cross-terms
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np

from lib.ma_model_d import (
    MaD, M_E_MEV, M_P_MEV, DM2_21, ALPHA,
    _TWO_PI_HC, _build_circumferences, _build_metric,
    solve_shear_for_alpha, alpha_from_geometry,
)

EPS_E, EPS_NU, EPS_P = 0.65, 5.0, 0.55
S_NU_DEFAULT = 0.022
MEV_TO_EV = 1e6

PROTON_MODES = [(1, 3), (3, 6)]


def build_model(n_p, sigma_ep=0.0):
    """Build MaD with self-consistent L_ring (recalibrated)."""
    s_e = solve_shear_for_alpha(EPS_E)
    # NOTE (Q114 §11.5): pass proton mode through.
    s_p = solve_shear_for_alpha(EPS_P, n_tube=n_p[0], n_ring=n_p[1])
    s_nu = S_NU_DEFAULT
    if s_e is None or s_p is None:
        return None, s_e, s_p

    L_dummy = _build_circumferences(
        EPS_E, s_e, 1.0, EPS_NU, s_nu, 1.0, EPS_P, s_p, 1.0)
    Gt, Gti = _build_metric(
        L_dummy, s_e, s_nu, s_p, sigma_ep=sigma_ep)
    if Gt is None:
        return None, s_e, s_p

    n_e_d = np.array([1.0 / EPS_E, 2.0, 0, 0, 0, 0])
    mu_eff_e = math.sqrt(float(n_e_d @ Gti @ n_e_d))
    L_ring_e = _TWO_PI_HC * mu_eff_e / M_E_MEV

    n_p_d = np.array([0, 0, 0, 0, float(n_p[0]) / EPS_P, float(n_p[1])])
    mu_eff_p = math.sqrt(float(n_p_d @ Gti @ n_p_d))
    L_ring_p = _TWO_PI_HC * mu_eff_p / M_P_MEV

    E0_nu_MeV = math.sqrt(DM2_21 / (4 * s_nu)) * 1e-6
    L_ring_nu = _TWO_PI_HC / E0_nu_MeV

    model = MaD(
        eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
        s_e=s_e, s_nu=s_nu, s_p=s_p,
        L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
        sigma_ep=sigma_ep)
    model._n_p = n_p
    return model, s_e, s_p


def build_model_fixed_L(n_p, sigma_ep, L_ring_e_0, L_ring_nu_0, L_ring_p_0,
                        s_e, s_nu, s_p):
    """Build MaD with FIXED L_ring (no recalibration)."""
    try:
        model = MaD(
            eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
            s_e=s_e, s_nu=s_nu, s_p=s_p,
            L_ring_e=L_ring_e_0, L_ring_nu=L_ring_nu_0,
            L_ring_p=L_ring_p_0,
            sigma_ep=sigma_ep)
        model._n_p = n_p
        return model
    except ValueError:
        return None


def step1_analytical_crossterm(n_p, sigma_ep=-0.28):
    """Extract and analyze the off-diagonal block of G̃⁻¹."""
    label = f"({n_p[0]},{n_p[1]})"
    print(f"\n{'='*72}")
    print(f"STEP 1: Analytical cross-term [{label}, σ_ep = {sigma_ep}]")
    print(f"{'='*72}")

    model, s_e, s_p = build_model(n_p, sigma_ep=sigma_ep)
    if model is None:
        print("  Model construction failed.")
        return

    Gti = model.metric_inv
    L = model.L

    # Off-diagonal block: electron (0,1) × proton (4,5)
    ep_block = Gti[0:2, 4:6]
    print(f"\n  Within-sheet shears: s_e = {s_e:.6f}, s_p = {s_p:.6f}")
    print(f"  α = {ALPHA:.6f} = 1/{1/ALPHA:.2f}")
    print(f"  s_e × s_p = {s_e * s_p:.8f}")
    print(f"  α² = {ALPHA**2:.8f}")
    print(f"  Ratio s_e×s_p / α² = {s_e * s_p / ALPHA**2:.4f}")

    print(f"\n  Off-diagonal block of G̃⁻¹ (electron × proton):")
    print(f"    G̃⁻¹[0,4] = {Gti[0,4]:+.10e}  (tube_e × tube_p)")
    print(f"    G̃⁻¹[0,5] = {Gti[0,5]:+.10e}  (tube_e × ring_p)")
    print(f"    G̃⁻¹[1,4] = {Gti[1,4]:+.10e}  (ring_e × tube_p)")
    print(f"    G̃⁻¹[1,5] = {Gti[1,5]:+.10e}  (ring_e × ring_p)")

    # Hydrogen mode: (1, 2, 0, 0, n₅, n₆)
    n_H = np.array([1, 2, 0, 0, n_p[0], n_p[1]], dtype=float)
    n_tilde = n_H / L

    # Cross-sheet contribution to E²
    e_part = n_tilde[0:2]
    p_part = n_tilde[4:6]
    E2_cross_raw = float(e_part @ ep_block @ p_part)
    E2_cross = 2 * _TWO_PI_HC**2 * E2_cross_raw  # factor 2 for symmetry

    E_total = model.energy(tuple(int(x) for x in n_H))
    E_cross_eV = (E2_cross / (2 * E_total)) * MEV_TO_EV

    print(f"\n  Hydrogen mode: {tuple(int(x) for x in n_H)}")
    print(f"  n_tilde (n/L): [{', '.join(f'{x:.6e}' for x in n_tilde)}]")
    print(f"\n  E²_cross = 2 × (2πℏc)² × (n_e/L_e) · G̃⁻¹_ep · (n_p/L_p)")
    print(f"           = {E2_cross:.6e} MeV²")
    print(f"  E_total  = {E_total:.9f} MeV")
    print(f"  E_cross  ≈ E²_cross / (2E) = {E_cross_eV:.1f} eV")

    # Compare to ½ α² m_e
    half_a2_me = 0.5 * ALPHA**2 * M_E_MEV * MEV_TO_EV
    print(f"\n  Target: ½ α² m_e = {half_a2_me:.4f} eV = 13.6 eV")
    print(f"  Ratio E_cross / (½ α² m_e) = {E_cross_eV / half_a2_me:.1f}")

    # Break down which components of the off-diagonal block contribute
    print(f"\n  Component breakdown of E²_cross:")
    labels = [("tube_e×tube_p", 0, 4), ("tube_e×ring_p", 0, 5),
              ("ring_e×tube_p", 1, 4), ("ring_e×ring_p", 1, 5)]
    for name, i, j in labels:
        contrib = 2 * _TWO_PI_HC**2 * n_tilde[i] * Gti[i,j] * n_tilde[j]
        contrib_eV = (contrib / (2 * E_total)) * MEV_TO_EV
        print(f"    {name}: E²={contrib:.4e} MeV², E≈{contrib_eV:.1f} eV")

    return E2_cross, E_cross_eV, s_e, s_p


def step2_alpha_scaling(n_p, sigma_ep=-0.28):
    """Check if cross-term scales as α² by varying α."""
    label = f"({n_p[0]},{n_p[1]})"
    print(f"\n{'='*72}")
    print(f"STEP 2: α² scaling test [{label}, σ_ep = {sigma_ep}]")
    print(f"{'='*72}")

    alpha_factors = [0.5, 0.7, 1.0, 1.5, 2.0, 3.0]
    print(f"\n  Varying α by factors, keeping ε and σ_ep fixed.")
    print(f"  If E_cross ∝ α², then E_cross/α² should be constant.\n")
    print(f"  {'α/α₀':>6s}  {'α':>10s}  {'s_e':>10s}  {'s_p':>10s}  "
          f"{'E_cross(eV)':>12s}  {'E_cross/α²':>12s}")
    print(f"  {'─'*6}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*12}  {'─'*12}")

    results = []
    for factor in alpha_factors:
        alpha_test = ALPHA * factor
        s_e = solve_shear_for_alpha(EPS_E, alpha_target=alpha_test)
        # NOTE (Q114 §11.5): pass proton mode through.
        s_p = solve_shear_for_alpha(EPS_P, alpha_target=alpha_test,
                                     n_tube=n_p[0], n_ring=n_p[1])
        if s_e is None or s_p is None:
            print(f"  {factor:6.2f}  — no solution —")
            continue

        s_nu = S_NU_DEFAULT

        L_dummy = _build_circumferences(
            EPS_E, s_e, 1.0, EPS_NU, s_nu, 1.0, EPS_P, s_p, 1.0)
        Gt, Gti = _build_metric(L_dummy, s_e, s_nu, s_p, sigma_ep=sigma_ep)
        if Gt is None:
            print(f"  {factor:6.2f}  — metric not positive-definite —")
            continue

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
        except ValueError:
            print(f"  {factor:6.2f}  — model failed —")
            continue

        n_H = (1, 2, 0, 0, n_p[0], n_p[1])
        decomp = model.energy_decomp(n_H)
        E_total = decomp['total_MeV']
        E2_cross = decomp['ep']
        E_cross_eV = (E2_cross / (2 * E_total)) * MEV_TO_EV
        ratio = E_cross_eV / (alpha_test**2)

        print(f"  {factor:6.2f}  {alpha_test:10.6f}  {s_e:10.6f}  {s_p:10.6f}  "
              f"{E_cross_eV:12.1f}  {ratio:12.1f}")
        results.append((factor, alpha_test, E_cross_eV, ratio))

    if len(results) >= 2:
        ratios = [r[3] for r in results]
        spread = (max(ratios) - min(ratios)) / np.mean(ratios)
        print(f"\n  Spread of E_cross/α²: {spread*100:.1f}%")
        if spread < 0.05:
            print(f"  → E_cross scales as α² (< 5% variation)")
        elif spread < 0.20:
            print(f"  → Approximate α² scaling (< 20% variation)")
        else:
            print(f"  → E_cross does NOT scale as α² ({spread*100:.0f}% variation)")

    return results


def step3_fixed_L(n_p, sigma_ep=-0.28):
    """No-recalibration computation to expose Schur complement."""
    label = f"({n_p[0]},{n_p[1]})"
    print(f"\n{'='*72}")
    print(f"STEP 3: Fixed-L computation [{label}]")
    print(f"{'='*72}")

    # Build model at σ=0 to get reference L values
    model_0, s_e, s_p = build_model(n_p, sigma_ep=0.0)
    if model_0 is None:
        print("  Model at σ=0 failed.")
        return

    L_ring_e_0 = model_0._L[1]  # ring circumference
    L_ring_nu_0 = model_0._L[3]
    L_ring_p_0 = model_0._L[5]
    s_nu = S_NU_DEFAULT

    mode_e = (1, 2, 0, 0, 0, 0)
    mode_p = (0, 0, 0, 0, n_p[0], n_p[1])
    mode_H = (1, 2, 0, 0, n_p[0], n_p[1])

    E_e_0 = model_0.energy(mode_e)
    E_p_0 = model_0.energy(mode_p)
    E_H_0 = model_0.energy(mode_H)

    print(f"\n  Reference (σ=0, L fixed from here):")
    print(f"    L_ring_e = {L_ring_e_0:.6f} fm")
    print(f"    L_ring_p = {L_ring_p_0:.6f} fm")
    print(f"    E_e = {E_e_0:.9f} MeV = {E_e_0*MEV_TO_EV:.3f} eV")
    print(f"    E_p = {E_p_0:.9f} MeV = {E_p_0*MEV_TO_EV:.3f} eV")
    print(f"    E_H = {E_H_0:.9f} MeV = {E_H_0*MEV_TO_EV:.3f} eV")

    # Sweep σ with fixed L
    sigma_values = np.linspace(0.0, -0.30, 61)
    print(f"\n  σ_ep sweep with FIXED L (no recalibration):\n")
    print(f"  {'σ_ep':>8s}  {'E_e (eV)':>14s}  {'E_p (eV)':>14s}  "
          f"{'E_H (eV)':>14s}  {'ΔE_e':>10s}  {'ΔE_p':>10s}  "
          f"{'ΔE_add':>10s}  {'I.E.':>10s}")
    print(f"  {'─'*8}  {'─'*14}  {'─'*14}  {'─'*14}  "
          f"{'─'*10}  {'─'*10}  {'─'*10}  {'─'*10}")

    for sigma in sigma_values:
        m = build_model_fixed_L(n_p, sigma,
                                L_ring_e_0, L_ring_nu_0, L_ring_p_0,
                                s_e, s_nu, s_p)
        if m is None:
            continue

        E_e = m.energy(mode_e)
        E_p = m.energy(mode_p)
        E_H = m.energy(mode_H)

        dE_e = (E_e - E_e_0) * MEV_TO_EV
        dE_p = (E_p - E_p_0) * MEV_TO_EV
        dE_add = (E_H - E_p) * MEV_TO_EV
        IE = (E_e + E_p - E_H) * MEV_TO_EV

        print(f"  {sigma:+8.4f}  {E_e*MEV_TO_EV:14.3f}  {E_p*MEV_TO_EV:14.3f}  "
              f"{E_H*MEV_TO_EV:14.3f}  {dE_e:+10.3f}  {dE_p:+10.3f}  "
              f"{dE_add:10.3f}  {IE:10.3f}")

    # Detailed analysis at σ_ep = -0.28
    m_28 = build_model_fixed_L(n_p, -0.28,
                               L_ring_e_0, L_ring_nu_0, L_ring_p_0,
                               s_e, s_nu, s_p)
    if m_28:
        E_e_28 = m_28.energy(mode_e)
        E_p_28 = m_28.energy(mode_p)
        E_H_28 = m_28.energy(mode_H)

        print(f"\n  At σ_ep = −0.28 (fixed L):")
        print(f"    ΔE_e = {(E_e_28 - E_e_0)*MEV_TO_EV:+.3f} eV  "
              f"(Schur complement shift of electron)")
        print(f"    ΔE_p = {(E_p_28 - E_p_0)*MEV_TO_EV:+.3f} eV  "
              f"(Schur complement shift of proton)")
        print(f"    ΔE_H = {(E_H_28 - E_H_0)*MEV_TO_EV:+.3f} eV  "
              f"(total shift of compound mode)")
        print(f"    ΔE_add = {(E_H_28 - E_p_28)*MEV_TO_EV:.3f} eV  "
              f"(cost of adding e⁻ to shifted proton)")
        print(f"    I.E. = {(E_e_28 + E_p_28 - E_H_28)*MEV_TO_EV:.3f} eV  "
              f"(shifted separation energy)")


def step4_winding_comparison(n_p, sigma_ep=-0.28):
    """Compare hydrogen vs neutron cross-terms."""
    label = f"({n_p[0]},{n_p[1]})"
    print(f"\n{'='*72}")
    print(f"STEP 4: Mode-winding comparison [{label}, σ_ep = {sigma_ep}]")
    print(f"{'='*72}")

    model, s_e, s_p = build_model(n_p, sigma_ep=sigma_ep)
    if model is None:
        print("  Model failed.")
        return

    # Hydrogen mode
    mode_H = (1, 2, 0, 0, n_p[0], n_p[1])

    # Neutron candidates from R50
    # For (1,3): best unfiltered neutron was (-2, -4, -2, -1, -2, 0)
    # For (3,6): best was (0, -6, 0, 0, 0, -8) or similar
    if n_p == (1, 3):
        mode_n = (-2, -4, -2, -1, -2, 0)
    else:
        mode_n = (0, -6, 0, 0, 0, -8)

    modes = [
        ("Hydrogen", mode_H),
        ("Neutron", mode_n),
    ]

    print(f"\n  {'Mode':>10s}  {'6-tuple':>25s}  {'E²_ep (MeV²)':>14s}  "
          f"{'E_total':>12s}  {'E_cross(eV)':>12s}  {'Winding prod':>12s}")
    print(f"  {'─'*10}  {'─'*25}  {'─'*14}  {'─'*12}  {'─'*12}  {'─'*12}")

    for name, mode in modes:
        decomp = model.energy_decomp(mode)
        E_total = decomp['total_MeV']
        E2_cross = decomp['ep']
        E_cross_eV = (E2_cross / (2 * E_total)) * MEV_TO_EV if E_total > 0 else 0

        n = np.array(mode, dtype=float)
        winding_prod = abs(n[0]*n[4] + n[0]*n[5] + n[1]*n[4] + n[1]*n[5])

        mode_str = str(mode)
        print(f"  {name:>10s}  {mode_str:>25s}  {E2_cross:14.4e}  "
              f"{E_total:12.6f}  {E_cross_eV:12.1f}  {winding_prod:12.0f}")

    # Detailed: what generates the scale separation?
    print(f"\n  Scale separation analysis:")

    L = model.L
    Gti = model.metric_inv

    for name, mode in modes:
        n = np.array(mode, dtype=float)
        n_tilde = n / L
        ep_block = Gti[0:2, 4:6]

        print(f"\n  {name} {mode}:")
        print(f"    n_e/L_e = [{n_tilde[0]:.4e}, {n_tilde[1]:.4e}]")
        print(f"    n_p/L_p = [{n_tilde[4]:.4e}, {n_tilde[5]:.4e}]")

        contrib_total = 0
        for i, il in [(0, "tube_e"), (1, "ring_e")]:
            for j, jl in [(4, "tube_p"), (5, "ring_p")]:
                c = 2 * _TWO_PI_HC**2 * n_tilde[i] * Gti[i,j] * n_tilde[j]
                contrib_total += c
                E_total = model.energy(mode)
                c_eV = (c / (2 * E_total)) * MEV_TO_EV
                print(f"    {il}×{jl}: n/L = {n_tilde[i]:.4e} × {n_tilde[j]:.4e}, "
                      f"G̃⁻¹={Gti[i,j]:+.6e}, E²_contrib={c:.4e} MeV², "
                      f"E≈{c_eV:.1f} eV")


def main():
    print("=" * 72)
    print("R51 Track 1a: Per-sheet energy decomposition and α² question")
    print("=" * 72)

    for n_p in PROTON_MODES:
        step1_analytical_crossterm(n_p, sigma_ep=-0.28)

    # α² scaling test (run once for (1,3))
    step2_alpha_scaling((1, 3), sigma_ep=-0.28)

    for n_p in PROTON_MODES:
        step3_fixed_L(n_p, sigma_ep=-0.28)

    for n_p in PROTON_MODES:
        step4_winding_comparison(n_p, sigma_ep=-0.28)

    print(f"\n\n{'='*72}")
    print("Track 1a complete.")
    print(f"{'='*72}")


if __name__ == '__main__':
    main()
