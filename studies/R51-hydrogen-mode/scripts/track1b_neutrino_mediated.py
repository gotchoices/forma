"""
R51 Track 1b: Neutrino-mediated binding

Tests whether the electron-neutrino cross-sheet coupling (σ_eν)
can produce ~13.6 eV binding for hydrogen compound modes.

The hypothesis: the electron couples to the proton not directly
(ep gives ~260 keV, far too large) but THROUGH the neutrino
sheet, whose enormous circumference (L_ring_ν ~ 4.2×10¹⁰ fm)
makes n_ν/L_ν tiny enough for eV-scale cross-terms.

Five analyses:
1. Scale verification — is the eν cross-term actually eV-scale?
2. Diagonal vs cross-term trade-off
3. Large-n₄ sweep — find where cross-term reaches 13.6 eV
4. Pure eν test (σ_ep = 0)
5. Quantum number mapping (n₃,n₄) → atomic (n,ℓ)?
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np

from lib.ma_model_d import (
    MaD, M_E_MEV, M_P_MEV, DM2_21, ALPHA,
    _TWO_PI_HC, _build_circumferences, _build_metric,
    solve_shear_for_alpha,
)

EPS_E, EPS_NU, EPS_P = 0.65, 5.0, 0.55
S_NU_DEFAULT = 0.022
MEV_TO_EV = 1e6


def build_model(n_p, sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0):
    """Build MaD with self-consistent L_ring."""
    s_e = solve_shear_for_alpha(EPS_E)
    # NOTE (Q114 §11.5): pass proton mode through.
    s_p = solve_shear_for_alpha(EPS_P, n_tube=n_p[0], n_ring=n_p[1])
    s_nu = S_NU_DEFAULT
    if s_e is None or s_p is None:
        return None

    L_dummy = _build_circumferences(
        EPS_E, s_e, 1.0, EPS_NU, s_nu, 1.0, EPS_P, s_p, 1.0)
    Gt, Gti = _build_metric(
        L_dummy, s_e, s_nu, s_p,
        sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)
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
            sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)
        model._n_p = n_p
        return model
    except ValueError:
        return None


def step1_scale_verification(n_p):
    """Verify the eν cross-term scale for small neutrino quantum numbers."""
    print(f"\n{'='*72}")
    print(f"STEP 1: eν cross-term scale verification [{n_p}]")
    print(f"{'='*72}")

    # Build model with σ_ep=-0.28, σ_eν=-0.28 for comparison
    model = build_model(n_p, sigma_ep=-0.28, sigma_enu=-0.28)
    if model is None:
        print("  Model failed.")
        return

    L = model.L
    print(f"\n  Sheet circumferences:")
    print(f"    L_tube_e = {L[0]:.2f} fm,   L_ring_e = {L[1]:.2f} fm")
    print(f"    L_tube_ν = {L[2]:.2e} fm,   L_ring_ν = {L[3]:.2e} fm")
    print(f"    L_tube_p = {L[4]:.4f} fm,   L_ring_p = {L[5]:.4f} fm")

    Gti = model.metric_inv

    # Off-diagonal blocks
    print(f"\n  Off-diagonal blocks of G̃⁻¹:")
    print(f"    ep block (σ_ep = -0.28):")
    for i in range(2):
        for j in range(4, 6):
            print(f"      G̃⁻¹[{i},{j}] = {Gti[i,j]:+.6e}")
    print(f"    eν block (σ_eν = -0.28):")
    for i in range(2):
        for j in range(2, 4):
            print(f"      G̃⁻¹[{i},{j}] = {Gti[i,j]:+.6e}")
    print(f"    νp block:")
    for i in range(2, 4):
        for j in range(4, 6):
            print(f"      G̃⁻¹[{i},{j}] = {Gti[i,j]:+.6e}")

    # Compute eν cross-terms for various (n₃, n₄)
    print(f"\n  eν cross-term for hydrogen mode (1,2,n₃,n₄,{n_p[0]},{n_p[1]}):")
    print(f"  σ_ep = -0.28, σ_eν = -0.28\n")
    print(f"  {'(n₃,n₄)':>8s}  {'E²_eν (MeV²)':>14s}  {'E_eν (eV)':>12s}  "
          f"{'E²_ν diag':>14s}  {'E_ν diag(eV)':>12s}  {'E²_ep':>14s}")
    print(f"  {'─'*8}  {'─'*14}  {'─'*12}  {'─'*14}  {'─'*12}  {'─'*14}")

    for n3 in range(0, 4):
        for n4 in range(0, 4):
            if n3 == 0 and n4 == 0:
                continue
            mode = (1, 2, n3, n4, n_p[0], n_p[1])
            decomp = model.energy_decomp(mode)
            E_total = decomp['total_MeV']
            E2_enu = decomp['enu']
            E2_nu = decomp['nu']
            E2_ep = decomp['ep']

            E_enu_eV = (E2_enu / (2 * E_total)) * MEV_TO_EV if E_total > 0 else 0
            E_nu_eV = (E2_nu / (2 * E_total)) * MEV_TO_EV if E_total > 0 else 0

            print(f"  ({n3},{n4}){' '*(5-len(f'({n3},{n4})'))}  "
                  f"{E2_enu:14.4e}  {E_enu_eV:12.6f}  "
                  f"{E2_nu:14.4e}  {E_nu_eV:12.6f}  "
                  f"{E2_ep:14.4e}")


def step2_diagonal_vs_cross(n_p):
    """Diagonal E_ν vs eν cross-term trade-off."""
    print(f"\n{'='*72}")
    print(f"STEP 2: Diagonal vs cross-term trade-off [{n_p}]")
    print(f"{'='*72}")

    sigma_enu_values = [-0.05, -0.10, -0.20, -0.28]

    mode_p = (0, 0, 0, 0, n_p[0], n_p[1])

    print(f"\n  ΔE_add = E(compound) − E(proton) for various σ_eν and (n₃,n₄)")
    print(f"  σ_ep = -0.28 throughout\n")

    for sigma_enu in sigma_enu_values:
        model = build_model(n_p, sigma_ep=-0.28, sigma_enu=sigma_enu)
        if model is None:
            continue

        E_p = model.energy(mode_p)

        print(f"  σ_eν = {sigma_enu:+.2f}:")
        print(f"  {'(n₃,n₄)':>8s}  {'E_compound':>14s}  {'ΔE_add (eV)':>13s}  "
              f"{'vs σ_eν=0':>10s}")
        print(f"  {'─'*8}  {'─'*14}  {'─'*13}  {'─'*10}")

        # Reference: (n₃,n₄) = (0,0)
        mode_00 = (1, 2, 0, 0, n_p[0], n_p[1])
        E_00 = model.energy(mode_00)
        dE_00 = (E_00 - E_p) * MEV_TO_EV

        # Build reference model with σ_eν=0 for comparison
        model_ref = build_model(n_p, sigma_ep=-0.28, sigma_enu=0.0)
        E_p_ref = model_ref.energy(mode_p)

        print(f"  (0,0)     {E_00:14.9f}  {dE_00:13.3f}  {'(ref)':>10s}")

        for n3 in range(0, 4):
            for n4 in range(0, 4):
                if n3 == 0 and n4 == 0:
                    continue
                mode = (1, 2, n3, n4, n_p[0], n_p[1])
                E_c = model.energy(mode)
                dE = (E_c - E_p) * MEV_TO_EV

                # Compare to same mode at σ_eν=0
                E_c_ref = model_ref.energy(mode)
                dE_ref = (E_c_ref - E_p_ref) * MEV_TO_EV
                delta = dE - dE_ref

                print(f"  ({n3},{n4}){' '*(5-len(f'({n3},{n4})'))}  "
                      f"{E_c:14.9f}  {dE:13.3f}  {delta:+10.3f}")
        print()


def step3_large_n4(n_p):
    """Find neutrino quantum numbers where cross-term reaches 13.6 eV."""
    print(f"\n{'='*72}")
    print(f"STEP 3: Large n₄ sweep [{n_p}]")
    print(f"{'='*72}")

    model = build_model(n_p, sigma_ep=-0.28, sigma_enu=-0.28)
    if model is None:
        print("  Model failed.")
        return

    mode_p = (0, 0, 0, 0, n_p[0], n_p[1])
    E_p = model.energy(mode_p)

    # Reference ΔE_add at (n₃,n₄)=(0,0)
    mode_00 = (1, 2, 0, 0, n_p[0], n_p[1])
    dE_00 = (model.energy(mode_00) - E_p) * MEV_TO_EV

    print(f"\n  Reference ΔE_add (n₃=0,n₄=0): {dE_00:.1f} eV")
    print(f"  σ_ep = -0.28, σ_eν = -0.28")
    print(f"\n  Sweeping n₄ (n₃=0) to find where eν cross-term ≈ 13.6 eV:\n")

    print(f"  {'n₄':>8s}  {'E_compound':>16s}  {'ΔE_add (eV)':>13s}  "
          f"{'E²_eν (MeV²)':>14s}  {'E_eν (eV)':>12s}  "
          f"{'E²_ν (MeV²)':>14s}  {'E_ν (eV)':>12s}")
    print(f"  {'─'*8}  {'─'*16}  {'─'*13}  {'─'*14}  {'─'*12}  {'─'*14}  {'─'*12}")

    n4_values = [0, 1, 10, 100, 1000, 10000, 100000, 1000000]

    for n4 in n4_values:
        mode = (1, 2, 0, n4, n_p[0], n_p[1])
        try:
            E_c = model.energy(mode)
        except ValueError:
            print(f"  {n4:>8d}  — negative E² —")
            continue
        dE = (E_c - E_p) * MEV_TO_EV
        decomp = model.energy_decomp(mode)
        E2_enu = decomp['enu']
        E2_nu = decomp['nu']
        E_total = decomp['total_MeV']
        E_enu_eV = (E2_enu / (2 * E_total)) * MEV_TO_EV if E_total > 0 else 0
        E_nu_eV = (E2_nu / (2 * E_total)) * MEV_TO_EV if E_total > 0 else 0

        print(f"  {n4:>8d}  {E_c:16.9f}  {dE:13.3f}  "
              f"{E2_enu:14.4e}  {E_enu_eV:12.4f}  "
              f"{E2_nu:14.4e}  {E_nu_eV:12.4f}")

    # Also sweep n₃ (tube winding)
    print(f"\n  Sweeping n₃ (n₄=0):\n")
    print(f"  {'n₃':>8s}  {'ΔE_add (eV)':>13s}  "
          f"{'E_eν (eV)':>12s}  {'E_ν (eV)':>12s}")
    print(f"  {'─'*8}  {'─'*13}  {'─'*12}  {'─'*12}")

    for n3 in [0, 1, 10, 100, 1000, 10000, 100000]:
        mode = (1, 2, n3, 0, n_p[0], n_p[1])
        try:
            E_c = model.energy(mode)
        except ValueError:
            print(f"  {n3:>8d}  — negative E² —")
            continue
        dE = (E_c - E_p) * MEV_TO_EV
        decomp = model.energy_decomp(mode)
        E_total = decomp['total_MeV']
        E_enu_eV = (decomp['enu'] / (2 * E_total)) * MEV_TO_EV if E_total > 0 else 0
        E_nu_eV = (decomp['nu'] / (2 * E_total)) * MEV_TO_EV if E_total > 0 else 0
        print(f"  {n3:>8d}  {dE:13.3f}  {E_enu_eV:12.4f}  {E_nu_eV:12.4f}")


def step4_pure_enu(n_p):
    """σ_ep = 0, only σ_eν active."""
    print(f"\n{'='*72}")
    print(f"STEP 4: Pure eν test (σ_ep = 0) [{n_p}]")
    print(f"{'='*72}")

    mode_p = (0, 0, 0, 0, n_p[0], n_p[1])

    sigma_enu_values = np.linspace(0, -0.30, 16)

    print(f"\n  σ_ep = 0, σ_νp = 0, sweeping σ_eν")
    print(f"  Compound mode: (1,2,0,1,{n_p[0]},{n_p[1]}) — one ring neutrino quantum\n")

    print(f"  {'σ_eν':>8s}  {'ΔE_add(0,0)':>13s}  {'ΔE_add(0,1)':>13s}  "
          f"{'Δ(eν effect)':>13s}  {'E²_eν':>14s}  {'E²_ν':>14s}")
    print(f"  {'─'*8}  {'─'*13}  {'─'*13}  {'─'*13}  {'─'*14}  {'─'*14}")

    for sigma_enu in sigma_enu_values:
        model = build_model(n_p, sigma_ep=0.0, sigma_enu=sigma_enu)
        if model is None:
            continue

        E_p = model.energy(mode_p)
        mode_00 = (1, 2, 0, 0, n_p[0], n_p[1])
        mode_01 = (1, 2, 0, 1, n_p[0], n_p[1])

        E_00 = model.energy(mode_00)
        E_01 = model.energy(mode_01)

        dE_00 = (E_00 - E_p) * MEV_TO_EV
        dE_01 = (E_01 - E_p) * MEV_TO_EV
        delta = dE_01 - dE_00

        decomp = model.energy_decomp(mode_01)
        E2_enu = decomp['enu']
        E2_nu = decomp['nu']

        print(f"  {sigma_enu:+8.4f}  {dE_00:13.4f}  {dE_01:13.4f}  "
              f"{delta:+13.6f}  {E2_enu:14.4e}  {E2_nu:14.4e}")

    # Try with larger n₄
    print(f"\n  Same but with n₄ = 1000:")
    print(f"  {'σ_eν':>8s}  {'ΔE_add(0,0)':>13s}  {'ΔE_add(0,1k)':>13s}  "
          f"{'Δ(eν effect)':>13s}")
    print(f"  {'─'*8}  {'─'*13}  {'─'*13}  {'─'*13}")

    for sigma_enu in [-0.05, -0.10, -0.20, -0.28]:
        model = build_model(n_p, sigma_ep=0.0, sigma_enu=sigma_enu)
        if model is None:
            continue

        E_p = model.energy(mode_p)
        mode_00 = (1, 2, 0, 0, n_p[0], n_p[1])
        mode_1k = (1, 2, 0, 1000, n_p[0], n_p[1])

        dE_00 = (model.energy(mode_00) - E_p) * MEV_TO_EV
        dE_1k = (model.energy(mode_1k) - E_p) * MEV_TO_EV

        print(f"  {sigma_enu:+8.4f}  {dE_00:13.4f}  {dE_1k:13.4f}  "
              f"{dE_1k - dE_00:+13.4f}")


def step5_energy_levels(n_p):
    """Check if different (n₃,n₄) reproduce hydrogen energy levels."""
    print(f"\n{'='*72}")
    print(f"STEP 5: Neutrino quantum numbers as energy levels [{n_p}]")
    print(f"{'='*72}")

    model = build_model(n_p, sigma_ep=-0.28, sigma_enu=-0.28)
    if model is None:
        print("  Model failed.")
        return

    mode_p = (0, 0, 0, 0, n_p[0], n_p[1])
    E_p = model.energy(mode_p)

    print(f"\n  ΔE_add for (1,2,n₃,n₄,{n_p[0]},{n_p[1]}) − E_proton:")
    print(f"  σ_ep = -0.28, σ_eν = -0.28\n")

    # Target: hydrogen levels at -13.6/n² eV relative to ionization
    # E₁ = 13.6 eV, E₂ = 3.4 eV, E₃ = 1.51 eV, E₄ = 0.85 eV
    print(f"  {'(n₃,n₄)':>8s}  {'ΔE_add (eV)':>13s}  "
          f"{'ΔE-ΔE(0,0)':>12s}  {'n₃²+n₄²':>8s}")
    print(f"  {'─'*8}  {'─'*13}  {'─'*12}  {'─'*8}")

    ref_mode = (1, 2, 0, 0, n_p[0], n_p[1])
    dE_ref = (model.energy(ref_mode) - E_p) * MEV_TO_EV

    for n3 in range(0, 6):
        for n4 in range(0, 6):
            mode = (1, 2, n3, n4, n_p[0], n_p[1])
            E_c = model.energy(mode)
            dE = (E_c - E_p) * MEV_TO_EV
            delta = dE - dE_ref
            n2 = n3**2 + n4**2
            if n2 <= 25:
                print(f"  ({n3},{n4}){' '*(5-len(f'({n3},{n4})'))}  "
                      f"{dE:13.4f}  {delta:+12.6f}  {n2:>8d}")


def main():
    print("=" * 72)
    print("R51 Track 1b: Neutrino-mediated binding")
    print("=" * 72)
    print()
    print("Hypothesis: atomic binding comes from σ_eν (electron-neutrino")
    print("coupling), not σ_ep (electron-proton coupling).")
    print(f"Target: hydrogen ionization energy = 13.6 eV = ½α²m_e")

    n_p = (1, 3)

    step1_scale_verification(n_p)
    step2_diagonal_vs_cross(n_p)
    step3_large_n4(n_p)
    step4_pure_enu(n_p)
    step5_energy_levels(n_p)

    print(f"\n\n{'='*72}")
    print("Track 1b complete.")
    print(f"{'='*72}")


if __name__ == '__main__':
    main()
