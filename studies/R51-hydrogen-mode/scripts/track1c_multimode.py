"""
R51 Track 1c: Multi-mode atom — neutrino-mediated coupling

Tests a fundamentally different picture from Tracks 1–1b:
the atom is NOT a single compound eigenvalue but MULTIPLE
coexisting modes coupled through the neutrino sheet.

- The nucleus is a mode (primarily Ma_p, with neutrino numbers)
- Each electron shell is a separate mode (primarily Ma_e,
  with its own neutrino numbers)
- Both share the neutrino sheet, which mediates 3D binding

Three analyses:
1. Neutrino mode census — do degeneracies match shell capacities?
2. Two-mode energy splitting — are neutrino-assignment-dependent
   energy differences at the eV scale?
3. Shared neutrino coupling — do correlated neutrino numbers
   lower total energy vs uncorrelated?
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from collections import defaultdict

from lib.ma_model_d import (
    MaD, M_E_MEV, M_P_MEV, DM2_21, ALPHA,
    _TWO_PI_HC, _build_circumferences, _build_metric,
    solve_shear_for_alpha, mu_mode,
)

EPS_E, EPS_NU, EPS_P = 0.65, 5.0, 0.55
S_NU_DEFAULT = 0.022
MEV_TO_EV = 1e6


def build_model(n_p, sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0):
    """Build MaD with self-consistent L_ring."""
    s_e = solve_shear_for_alpha(EPS_E)
    s_p = solve_shear_for_alpha(EPS_P)
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


# ── Step 1: Neutrino mode census ──────────────────────────────────

def step1_neutrino_census():
    """Count neutrino modes on the (n₃,n₄) lattice by energy level."""
    print(f"\n{'='*72}")
    print("STEP 1: Neutrino mode census on the ε_ν = 5.0 torus")
    print(f"{'='*72}")

    s_nu = S_NU_DEFAULT
    eps_nu = EPS_NU

    # Neutrino energy for a mode (n₃, n₄) on an isolated sheet:
    # μ²(n₃,n₄) = (n₃/ε)² + (n₄ − n₃·s)²
    # Energy ∝ μ, so group by μ² value
    #
    # On the torus, ε_ν = 5.0 means tube is 5× ring.
    # The tube direction (n₃) contributes n₃/ε = n₃/5.
    # The ring direction (n₄) contributes n₄ − n₃·s_ν ≈ n₄ (s_ν = 0.022 is tiny).

    print(f"\n  ε_ν = {eps_nu},  s_ν = {s_nu}")
    print(f"  μ²(n₃,n₄) = (n₃/{eps_nu})² + (n₄ − {s_nu}·n₃)²")
    print(f"  For ε_ν = 5: tube winding carries 1/25 the weight of ring winding")

    n_max = 10
    mu2_modes = defaultdict(list)

    for n3 in range(-n_max, n_max + 1):
        for n4 in range(-n_max, n_max + 1):
            if n3 == 0 and n4 == 0:
                continue
            mu2 = mu_mode(n3, n4, eps_nu, s_nu)
            mu2_rounded = round(mu2, 8)
            mu2_modes[mu2_rounded].append((n3, n4))

    sorted_levels = sorted(mu2_modes.keys())

    print(f"\n  Energy levels (sorted by μ²), up to n₃,n₄ ∈ [{-n_max},{n_max}]:")
    print(f"\n  {'Level':>5s}  {'μ²':>12s}  {'Degeneracy':>10s}  {'Modes (n₃,n₄)':s}")
    print(f"  {'─'*5}  {'─'*12}  {'─'*10}  {'─'*40}")

    # Electron shell capacities for reference
    shell_capacities = [2, 6, 2, 10, 6, 2, 14, 10, 6, 2]
    cumulative = []
    c = 0
    for sc in shell_capacities:
        c += sc
        cumulative.append(c)

    for i, mu2 in enumerate(sorted_levels[:30]):
        modes = mu2_modes[mu2]
        deg = len(modes)
        modes_str = str(modes[:8])
        if len(modes) > 8:
            modes_str += f" ... ({len(modes)} total)"
        print(f"  {i+1:5d}  {mu2:12.6f}  {deg:10d}  {modes_str}")

    # Cumulative count
    print(f"\n  Cumulative mode count vs electron shell structure:")
    print(f"\n  {'Level':>5s}  {'μ²':>12s}  {'Deg':>5s}  {'Cumul':>6s}  "
          f"{'Shell target':>12s}")
    print(f"  {'─'*5}  {'─'*12}  {'─'*5}  {'─'*6}  {'─'*12}")

    cum = 0
    shell_idx = 0
    for i, mu2 in enumerate(sorted_levels[:20]):
        modes = mu2_modes[mu2]
        deg = len(modes)
        cum += deg
        target = ""
        if shell_idx < len(cumulative) and cum >= cumulative[shell_idx]:
            target = f"← {cumulative[shell_idx]} ({['s','p','s','d','p','s','f','d','p','s'][shell_idx]})"
            while shell_idx < len(cumulative) and cum >= cumulative[shell_idx]:
                shell_idx += 1
        print(f"  {i+1:5d}  {mu2:12.6f}  {deg:5d}  {cum:6d}  {target:>12s}")

    # Also show the pattern: what does the degeneracy sequence look like?
    print(f"\n  Degeneracy sequence (first 20 levels):")
    degs = [len(mu2_modes[mu2]) for mu2 in sorted_levels[:20]]
    print(f"  {degs}")
    print(f"\n  For comparison, atomic subshell capacities: [2, 6, 10, 14, ...]")
    print(f"  (from 2(2ℓ+1) for ℓ = 0, 1, 2, 3)")


# ── Step 2: Two-mode energy splitting ─────────────────────────────

def step2_two_mode_splitting(n_p):
    """Compute nuclear + electron mode energies with varying ν numbers."""
    print(f"\n{'='*72}")
    print(f"STEP 2: Two-mode energy splitting [{n_p}]")
    print(f"{'='*72}")

    # Build models at different cross-shear values
    for sigma_ep in [0.0, -0.28]:
        model = build_model(n_p, sigma_ep=sigma_ep)
        if model is None:
            continue

        print(f"\n  σ_ep = {sigma_ep}, σ_eν = 0, σ_νp = 0")

        # Nuclear mode: (0, 0, n₃_nuc, n₄_nuc, n₅, n₆)
        # Electron mode: (1, 2, n₃_e, n₄_e, 0, 0)
        # "Free proton" (no neutrino): (0, 0, 0, 0, n₅, n₆)
        # "Free electron" (no neutrino): (1, 2, 0, 0, 0, 0)

        E_free_p = model.energy((0, 0, 0, 0, n_p[0], n_p[1]))
        E_free_e = model.energy((1, 2, 0, 0, 0, 0))
        E_free_sum = E_free_p + E_free_e

        print(f"\n  Free proton:   E = {E_free_p:.9f} MeV")
        print(f"  Free electron: E = {E_free_e:.9f} MeV")
        print(f"  Sum (unbound): E = {E_free_sum:.9f} MeV")
        print(f"                   = {E_free_sum * MEV_TO_EV:.3f} eV")

        # Now: give both modes neutrino quantum numbers
        print(f"\n  Two-mode sum: E_nuc(0,0,n₃,n₄,{n_p[0]},{n_p[1]}) "
              f"+ E_e(1,2,n₃',n₄',0,0)")
        print(f"\n  Case A: Same neutrino numbers (correlated — bound?)")
        print(f"  {'(n₃,n₄)':>8s}  {'E_nuc':>14s}  {'E_e':>14s}  {'Sum':>14s}  "
              f"{'ΔE (eV)':>12s}")
        print(f"  {'─'*8}  {'─'*14}  {'─'*14}  {'─'*14}  {'─'*12}")

        for n3, n4 in [(0,0), (0,1), (0,2), (1,0), (1,1), (0,3), (2,0)]:
            E_nuc = model.energy((0, 0, n3, n4, n_p[0], n_p[1]))
            E_e = model.energy((1, 2, n3, n4, 0, 0))
            E_sum = E_nuc + E_e
            dE = (E_sum - E_free_sum) * MEV_TO_EV
            print(f"  ({n3},{n4}){' '*(5-len(f'({n3},{n4})'))}  "
                  f"{E_nuc:14.9f}  {E_e:14.9f}  {E_sum:14.9f}  {dE:+12.4f}")

        print(f"\n  Case B: Different neutrino numbers (uncorrelated)")
        print(f"  {'nuc(n₃,n₄)':>10s}  {'e(n₃,n₄)':>10s}  {'E_nuc':>14s}  "
              f"{'E_e':>14s}  {'Sum':>14s}  {'ΔE (eV)':>12s}")
        print(f"  {'─'*10}  {'─'*10}  {'─'*14}  {'─'*14}  {'─'*14}  {'─'*12}")

        pairs = [
            ((0,1), (0,0)), ((0,0), (0,1)),
            ((0,1), (0,2)), ((0,2), (0,1)),
            ((1,0), (0,1)), ((0,1), (1,0)),
            ((0,1), (0,1)), ((1,1), (1,1)),
        ]
        for (n3a, n4a), (n3b, n4b) in pairs:
            E_nuc = model.energy((0, 0, n3a, n4a, n_p[0], n_p[1]))
            E_e = model.energy((1, 2, n3b, n4b, 0, 0))
            E_sum = E_nuc + E_e
            dE = (E_sum - E_free_sum) * MEV_TO_EV
            print(f"  ({n3a},{n4a}){' '*(7-len(f'({n3a},{n4a})'))}  "
                  f"({n3b},{n4b}){' '*(7-len(f'({n3b},{n4b})'))}  "
                  f"{E_nuc:14.9f}  {E_e:14.9f}  {E_sum:14.9f}  {dE:+12.4f}")


# ── Step 3: Shared neutrino coupling ──────────────────────────────

def step3_shared_neutrino(n_p):
    """Test whether shared neutrino numbers lower total energy."""
    print(f"\n{'='*72}")
    print(f"STEP 3: Shared neutrino coupling [{n_p}]")
    print(f"{'='*72}")

    # With all three cross-shears active, the neutrino sheet
    # couples to both electron and proton sheets.  Does this
    # create a preference for correlated neutrino numbers?

    for sigma_enu in [0.0, -0.10, -0.28]:
        for sigma_nup in [0.0, -0.10, -0.28]:
            if sigma_enu == 0.0 and sigma_nup == 0.0:
                continue

            model = build_model(n_p, sigma_ep=-0.28,
                                sigma_enu=sigma_enu, sigma_nup=sigma_nup)
            if model is None:
                print(f"\n  σ_eν={sigma_enu}, σ_νp={sigma_nup}: "
                      f"metric not positive-definite, skipping")
                continue

            print(f"\n  σ_ep = -0.28, σ_eν = {sigma_enu}, σ_νp = {sigma_nup}")

            E_free_p = model.energy((0, 0, 0, 0, n_p[0], n_p[1]))
            E_free_e = model.energy((1, 2, 0, 0, 0, 0))
            E_free_sum = E_free_p + E_free_e

            # Compare: nuclear mode with (0,1) + electron mode with (0,1) [correlated]
            #      vs: nuclear mode with (0,1) + electron mode with (0,0) [uncorrelated]
            #      vs: nuclear mode with (0,0) + electron mode with (0,1) [uncorrelated]

            print(f"\n  {'Config':>25s}  {'E_nuc':>14s}  {'E_e':>14s}  "
                  f"{'Sum':>14s}  {'ΔE (eV)':>12s}")
            print(f"  {'─'*25}  {'─'*14}  {'─'*14}  {'─'*14}  {'─'*12}")

            configs = [
                ("free (0,0)+(0,0)", (0,0), (0,0)),
                ("nuc only (0,1)+(0,0)", (0,1), (0,0)),
                ("e only (0,0)+(0,1)", (0,0), (0,1)),
                ("correl (0,1)+(0,1)", (0,1), (0,1)),
                ("anti (0,1)+(0,-1)", (0,1), (0,-1)),
                ("correl (1,0)+(1,0)", (1,0), (1,0)),
                ("anti (1,0)+(-1,0)", (1,0), (-1,0)),
                ("correl (1,1)+(1,1)", (1,1), (1,1)),
                ("anti (1,1)+(-1,-1)", (1,1), (-1,-1)),
            ]

            for label, (n3a,n4a), (n3b,n4b) in configs:
                E_nuc = model.energy((0, 0, n3a, n4a, n_p[0], n_p[1]))
                E_e = model.energy((1, 2, n3b, n4b, 0, 0))
                E_sum = E_nuc + E_e
                dE = (E_sum - E_free_sum) * MEV_TO_EV
                print(f"  {label:>25s}  {E_nuc:14.9f}  {E_e:14.9f}  "
                      f"{E_sum:14.9f}  {dE:+12.4f}")

    # Also test: does the compound mode (single eigenvalue) differ
    # from the two-mode sum?
    print(f"\n  ── Compound vs two-mode comparison ──")
    model = build_model(n_p, sigma_ep=-0.28, sigma_enu=-0.28, sigma_nup=-0.28)
    if model is None:
        print("  Model failed at full coupling.")
        return

    E_free_p = model.energy((0, 0, 0, 0, n_p[0], n_p[1]))
    E_free_e = model.energy((1, 2, 0, 0, 0, 0))

    print(f"\n  σ_ep = σ_eν = σ_νp = -0.28")
    print(f"\n  {'Description':>30s}  {'Energy (MeV)':>16s}  {'vs free sum (eV)':>16s}")
    print(f"  {'─'*30}  {'─'*16}  {'─'*16}")

    E_free_sum = E_free_p + E_free_e
    print(f"  {'Free sum (p + e)':>30s}  {E_free_sum:16.9f}  {'(ref)':>16s}")

    for (n3, n4) in [(0,0), (0,1), (1,0), (1,1)]:
        # Two-mode sum
        E_nuc = model.energy((0, 0, n3, n4, n_p[0], n_p[1]))
        E_e = model.energy((1, 2, n3, n4, 0, 0))
        E_2mode = E_nuc + E_e
        dE_2mode = (E_2mode - E_free_sum) * MEV_TO_EV

        # Single compound eigenvalue
        E_compound = model.energy((1, 2, n3, n4, n_p[0], n_p[1]))
        dE_compound = (E_compound - E_free_sum) * MEV_TO_EV

        label_2m = f"2-mode ({n3},{n4})+({n3},{n4})"
        label_1m = f"compound (1,2,{n3},{n4},{n_p[0]},{n_p[1]})"

        print(f"  {label_2m:>30s}  {E_2mode:16.9f}  {dE_2mode:+16.4f}")
        print(f"  {label_1m:>30s}  {E_compound:16.9f}  {dE_compound:+16.4f}")


def main():
    print("=" * 72)
    print("R51 Track 1c: Multi-mode atom — neutrino-mediated coupling")
    print("=" * 72)
    print()
    print("Tests whether atoms are multi-mode states (nuclear mode +")
    print("electron mode) coupled through shared neutrino quantum numbers.")
    print(f"Target: hydrogen ionization energy = 13.6 eV")

    n_p = (1, 3)

    step1_neutrino_census()
    step2_two_mode_splitting(n_p)
    step3_shared_neutrino(n_p)

    print(f"\n\n{'='*72}")
    print("Track 1c complete.")
    print(f"{'='*72}")


if __name__ == '__main__':
    main()
