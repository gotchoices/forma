"""
R50 Track 10: Decay-product composition

The muon decays as: μ⁻ → e⁻ + ν̄_e + ν_μ
The pion decays as: π⁺ → μ⁺ + ν_μ

The user's insight: if a particle IS its decay products bound
together, then the particle's 6-tuple is the SUM of the
components' quantum numbers, and its mass is computed from the
metric at that combined 6-tuple.

This is NOT a pair-sum (Track 9).  There, mass_pair = E(A) + E(B).
Here, mass_compound = E(n_A + n_B) — the metric's quadratic form
is evaluated at the sum of the integer quantum numbers.  Since
E² is quadratic, E(A+B) ≠ E(A) + E(B) in general; the cross-terms
can dramatically alter the mass.

This script:
  1. Builds the muon as electron + ν-dressings: n_μ = (1, 2, n₃, n₄, 0, 0)
  2. Shows E for all choices of ν-dressing up to large n₃, n₄
  3. Tests pion = muon_mode + ν for hypothetical muon modes
  4. Explains why the ν sheet does (or doesn't) contribute enough
     energy to escape the desert
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np

from lib.ma_model_d import (
    MaD, M_E_MEV, M_P_MEV, DM2_21,
    _TWO_PI_HC, _build_circumferences, _build_metric,
    solve_shear_for_alpha_signed, solve_shear_for_alpha,
)

EPS_E = 0.65
EPS_NU = 5.0
EPS_P = 0.55
S_NU_DEFAULT = 0.022
N_E_REF = (1, 2)
N_P_REF = (1, 3)


def build_model(s_e_sign=+1, s_p_sign=+1, sigma_enu=0.0, sigma_ep=0.0):
    """Build calibrated model on given branch."""
    s_e = solve_shear_for_alpha_signed(EPS_E, sign=s_e_sign,
                                        n_tube=N_E_REF[0], n_ring=N_E_REF[1])
    s_p = solve_shear_for_alpha_signed(EPS_P, sign=s_p_sign,
                                        n_tube=N_P_REF[0], n_ring=N_P_REF[1])
    s_nu = S_NU_DEFAULT
    if s_e is None or s_p is None:
        return None

    L_dummy = _build_circumferences(
        EPS_E, s_e, 1.0, EPS_NU, s_nu, 1.0, EPS_P, s_p, 1.0)
    Gt, Gti = _build_metric(
        L_dummy, s_e, s_nu, s_p,
        sigma_ep=sigma_ep, sigma_enu=sigma_enu)
    if Gt is None:
        return None

    n_e_d = np.array([N_E_REF[0] / EPS_E, N_E_REF[1], 0, 0, 0, 0])
    mu_eff_e = math.sqrt(float(n_e_d @ Gti @ n_e_d))
    L_ring_e = _TWO_PI_HC * mu_eff_e / M_E_MEV

    n_p_d = np.array([0, 0, 0, 0, N_P_REF[0] / EPS_P, N_P_REF[1]])
    mu_eff_p = math.sqrt(float(n_p_d @ Gti @ n_p_d))
    L_ring_p = _TWO_PI_HC * mu_eff_p / M_P_MEV

    E0_nu_MeV = math.sqrt(DM2_21 / (4 * s_nu)) * 1e-6
    L_ring_nu = _TWO_PI_HC / E0_nu_MeV

    try:
        model = MaD(
            eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
            s_e=s_e, s_nu=s_nu, s_p=s_p,
            L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
            sigma_ep=sigma_ep, sigma_enu=sigma_enu)
        return model
    except ValueError:
        return None


def main():
    print("=" * 78)
    print("R50 Track 10: Decay-product composition")
    print("=" * 78)
    print()
    print("Decay products → compound quantum numbers → mass from metric.")
    print()
    print("Key distinction from Track 9 (pair sums):")
    print("  Track 9:  M_pair  = E(n_A) + E(n_B)     [sum of individual masses]")
    print("  Track 10: M_comp  = E(n_A + n_B)         [metric at summed quantum #s]")
    print("  These are very different because E² is quadratic, not linear.")
    print()

    # ── Section 1: The scale problem ────────────────────────────────
    print("=" * 78)
    print("Section 1: Why does ν dressing barely change the energy?")
    print("=" * 78)
    print()

    m = build_model(+1, +1)
    L = m.L
    print(f"  Circumferences (fm):")
    print(f"    L_tube_e  = {L[0]:.4f}    L_ring_e  = {L[1]:.4f}")
    print(f"    L_tube_ν  = {L[2]:.4f}  L_ring_ν  = {L[3]:.4f}")
    print(f"    L_tube_p  = {L[4]:.4f}    L_ring_p  = {L[5]:.4f}")
    print()
    print(f"  Scale comparison:")
    print(f"    L_ring_ν / L_ring_e = {L[3] / L[1]:.1f}×")
    print(f"    Energy per ν winding ∝ 1/L_ring_ν ∝ {_TWO_PI_HC / L[3]:.6f} MeV")
    print(f"    Energy per e winding ∝ 1/L_ring_e ∝ {_TWO_PI_HC / L[1]:.3f} MeV")
    ratio = (L[3] / L[1])
    print(f"    ν winding contributes {1/ratio:.1e}× as much as e winding")
    print()
    print("  This is why ν dressings can't bridge the 5–200 MeV gap:")
    print("  the ν sheet is ~10⁸× larger than the e sheet, so each ν")
    print("  winding adds ~10⁻⁶ MeV, not ~100 MeV.")
    print()

    # ── Section 2: Muon = electron + ν dressing ─────────────────────
    print("=" * 78)
    print("Section 2: Muon as electron + ν dressing")
    print("=" * 78)
    print()
    print("  μ⁻ → e⁻ + ν̄_e + ν_μ")
    print("  ⇒ n_μ = n_e + n_ν̄e + n_νμ = (1, 2, ?, ?, 0, 0)")
    print("  where ? = sum of ν decay-product quantum numbers")
    print()
    print("  Since the number of ν components doesn't matter (only the")
    print("  total ν winding does), muon = (1, 2, n₃, n₄, 0, 0) for")
    print("  some integers n₃, n₄.  Let's compute E for all of them.")
    print()

    # Scan over a wide range of ν windings
    max_nu = 20
    print(f"  n₃ ∈ [{-max_nu}, {max_nu}], n₄ ∈ [{-max_nu}, {max_nu}]")
    print()

    # Collect results across branches and σ_eν
    branches = [
        ('++', +1, +1),
        ('+-', +1, -1),
        ('-+', -1, +1),
        ('--', -1, -1),
    ]
    sigma_grid = [0.0, -0.10, -0.20, +0.10, +0.20]

    best_muon = None

    for branch_label, s_e_sign, s_p_sign in branches:
        for sigma in sigma_grid:
            model = build_model(s_e_sign, s_p_sign, sigma_enu=sigma)
            if model is None:
                continue
            for n3 in range(-max_nu, max_nu + 1):
                for n4 in range(-max_nu, max_nu + 1):
                    n = (1, 2, n3, n4, 0, 0)
                    try:
                        E = model.energy(n)
                    except ValueError:
                        continue
                    delta = abs(E - 105.658)
                    if best_muon is None or delta < best_muon['delta']:
                        best_muon = {
                            'n': n, 'E': E, 'delta': delta,
                            'branch': branch_label,
                            'sigma': sigma,
                            'rel': delta / 105.658,
                        }

    # Also show the map for ++ branch, σ=0
    print("  Energy map E(1, 2, n₃, n₄, 0, 0) on ++ branch, σ_eν = 0:")
    print()
    m0 = build_model(+1, +1, sigma_enu=0.0)
    # Show a grid of n₃ ∈ [-5, 5], n₄ ∈ [-5, 5]
    print(f"  {'n₃\\n₄':>6s}", end='')
    for n4 in range(-5, 6):
        print(f"  {n4:>8d}", end='')
    print()
    for n3 in range(-5, 6):
        print(f"  {n3:>6d}", end='')
        for n4 in range(-5, 6):
            n = (1, 2, n3, n4, 0, 0)
            try:
                E = m0.energy(n)
                if E > 9999:
                    print(f"  {'>9999':>8s}", end='')
                else:
                    print(f"  {E:>8.3f}", end='')
            except ValueError:
                print(f"  {'ERR':>8s}", end='')
        print()
    print()

    # Also show extreme n₃, n₄
    print("  Extreme ν windings (++ branch, σ=0):")
    for n3, n4 in [(0, 0), (0, 1), (0, 10), (0, 100), (0, 1000),
                    (1, 0), (10, 0), (100, 0),
                    (5, 5), (10, 10), (20, 20)]:
        n = (1, 2, n3, n4, 0, 0)
        E = m0.energy(n)
        print(f"    (1, 2, {n3:>4d}, {n4:>4d}, 0, 0)  E = {E:>12.6f} MeV")
    print()

    target = 105.658
    print(f"  Best muon candidate across all branches/σ:")
    print(f"    mode = {best_muon['n']}")
    print(f"    E = {best_muon['E']:.6f} MeV  (target: {target:.3f})")
    print(f"    Δm/m = {best_muon['rel']*100:.3f}%")
    print(f"    branch = {best_muon['branch']}, σ_eν = {best_muon['sigma']}")
    print()

    # ── Section 3: What about p-sheet dressing? ─────────────────────
    print("=" * 78)
    print("Section 3: Muon with proton-sheet dressing")
    print("=" * 78)
    print()
    print("  What if the muon is (1, 2, n₃, n₄, n₅, n₆) with p-sheet?")
    print("  The p-sheet has L_ring_p comparable to L_ring_e, so p windings")
    print("  contribute MeV-scale energy.  But Q = -n₁ + n₅ = -1 + n₅,")
    print("  so for Q = -1 we need n₅ = 0 (no p-tube winding).")
    print("  However n₆ (p-ring) is free and doesn't affect charge.")
    print()
    print("  Scanning (1, 2, n₃, n₄, 0, n₆):")
    print()

    best_pring = None
    for branch_label, s_e_sign, s_p_sign in branches:
        for sigma in sigma_grid:
            model = build_model(s_e_sign, s_p_sign, sigma_enu=sigma)
            if model is None:
                continue
            for n3 in range(-5, 6):
                for n4 in range(-5, 6):
                    for n6 in range(-10, 11):
                        if n6 == 0 and n3 == 0 and n4 == 0:
                            continue  # that's just the electron
                        n = (1, 2, n3, n4, 0, n6)
                        if MaD.charge(n) != -1:
                            continue
                        try:
                            E = model.energy(n)
                        except ValueError:
                            continue
                        delta = abs(E - target)
                        if best_pring is None or delta < best_pring['delta']:
                            best_pring = {
                                'n': n, 'E': E, 'delta': delta,
                                'branch': branch_label,
                                'sigma': sigma,
                                'rel': delta / target,
                            }

    print(f"  Best muon candidate with p-ring dressing:")
    print(f"    mode = {best_pring['n']}")
    print(f"    E = {best_pring['E']:.3f} MeV  (target: {target:.3f})")
    print(f"    Δm/m = {best_pring['rel']*100:.3f}%")
    print(f"    branch = {best_pring['branch']}, σ_eν = {best_pring['sigma']}")
    print()

    # ── Section 4: Full compound with both ν and p dressing ─────────
    print("=" * 78)
    print("Section 4: Full compound — (1, 2, n₃, n₄, n₅, n₆) with Q = -1")
    print("=" * 78)
    print()
    print("  Allow n₅ ≠ 0 as long as Q = -n₁ + n₅ = -1 + n₅ = -1 ⇒ n₅ = 0.")
    print("  Wait — that forces n₅ = 0.  To have p-tube winding AND Q = -1,")
    print("  we'd need n₁ = 1 + n₅.  Let's allow this.")
    print()
    print("  Scanning (n₁, 2, n₃, n₄, n₅, n₆) with -n₁ + n₅ = -1, spin ½:")
    print()

    best_full = None
    for branch_label, s_e_sign, s_p_sign in branches:
        for sigma in sigma_grid:
            model = build_model(s_e_sign, s_p_sign, sigma_enu=sigma)
            if model is None:
                continue
            for n5 in range(-3, 4):
                n1 = n5 + 1  # Q = -n1 + n5 = -1
                if abs(n1) > 3:
                    continue
                for n6 in range(-10, 11):
                    for n3 in range(-5, 6):
                        for n4 in range(-5, 6):
                            n = (n1, 2, n3, n4, n5, n6)
                            if MaD.charge(n) != -1:
                                continue
                            if MaD.spin_total(n) != 0.5:
                                continue
                            try:
                                E = model.energy(n)
                            except ValueError:
                                continue
                            delta = abs(E - target)
                            if best_full is None or delta < best_full['delta']:
                                best_full = {
                                    'n': n, 'E': E, 'delta': delta,
                                    'branch': branch_label,
                                    'sigma': sigma,
                                    'rel': delta / target,
                                }

    print(f"  Best muon candidate (full compound, Q=-1, spin-½):")
    print(f"    mode = {best_full['n']}")
    print(f"    E = {best_full['E']:.3f} MeV  (target: {target:.3f})")
    print(f"    Δm/m = {best_full['rel']*100:.3f}%")
    print(f"    branch = {best_full['branch']}, σ_eν = {best_full['sigma']}")
    print()

    # ── Section 5: The ν scale problem ──────────────────────────────
    print("=" * 78)
    print("Section 5: Why does this fail? The ν scale problem.")
    print("=" * 78)
    print()
    print("  The energy formula is E² = (2πℏc)² nᵀ G̃⁻¹ n / L²")
    print("  Each sheet contributes ∝ 1/L²_sheet.  The scale ratios:")
    print(f"    L_ring_e  = {m0.L_ring[0]:.4f} fm")
    print(f"    L_ring_ν  = {m0.L_ring[1]:.4f} fm")
    print(f"    L_ring_p  = {m0.L_ring[2]:.4f} fm")
    print()
    print(f"    L_ν / L_e = {m0.L_ring[1] / m0.L_ring[0]:.1f}")
    print(f"    L_p / L_e = {m0.L_ring[2] / m0.L_ring[0]:.3f}")
    print()
    print("  The ν sheet is ~10⁸× larger than the e sheet.")
    print("  ν windings contribute ~10⁻⁶ MeV per winding.")
    print("  Even n₃ = 1000 adds only ~0.001 MeV to the electron.")
    print()
    print("  The p sheet is ~3× larger — its windings add ~hundreds of MeV")
    print("  per unit, WAY too coarse to land at 106 MeV from a base of")
    print("  0.511 MeV.")
    print()
    print("  The fundamental problem: the three sheets span vastly different")
    print("  mass scales (meV, MeV, hundreds of MeV), and no integer")
    print("  combination can bridge the 0.511 → 105.66 MeV gap.")
    print()
    print("  To reach 105.66 MeV from the electron base, we would need")
    print("  a mechanism that changes the e-sheet SCALE (L_ring_e), not")
    print("  just adds more windings.  That is back-reaction: the ν")
    print("  companion's presence modifies the fabric geometry that")
    print("  determines L_ring_e.")
    print()

    # ── Section 6: What back-reaction WOULD need to do ──────────────
    print("=" * 78)
    print("Section 6: What back-reaction would need to do")
    print("=" * 78)
    print()
    print("  If the muon IS (1, 2, n₃, n₄, 0, 0) with modified geometry,")
    print("  what L_ring_e would be needed?")
    print()
    # For the bare electron: E = (2πℏc) × μ_e / L_ring_e = 0.511 MeV
    # → L_ring_e = (2πℏc) × μ_e / 0.511
    # For the muon: E = 105.658 → L_ring_e' = (2πℏc) × μ_muon / 105.658
    # If μ_muon ≈ μ_e (just the (1,2) winding), then
    # L_ring_e' = L_ring_e × 0.511 / 105.658
    L_e = m0.L_ring[0]
    L_e_muon = L_e * 0.511 / 105.658
    ratio = L_e / L_e_muon
    print(f"  Current L_ring_e = {L_e:.4f} fm (calibrated to electron)")
    print(f"  Needed  L_ring_e = {L_e_muon:.6f} fm (to give (1,2) mode → 106 MeV)")
    print(f"  Shrinkage factor = {ratio:.1f}×")
    print()
    print("  The ν companion would need to shrink the e-sheet ring by a")
    print(f"  factor of ~{ratio:.0f}×.  This is a DRAMATIC geometric change.")
    print("  It means the ν winding constricts the e-sheet fabric,")
    print("  squeezing its circumference from ~400 fm to ~2 fm.")
    print()
    print("  In a back-reaction model, this shrinkage would come from")
    print("  the tension that the ν winding exerts on the shared fabric.")
    print("  The ν mode's presence modifies the metric in the e-sheet")
    print("  region, changing L_ring_e from its 'free' value to the")
    print("  'loaded' value.  The muon's mass is then the (1,2) energy")
    print("  on this compressed e-sheet.")
    print()
    print("  Self-consistency requirement: the SAME geometry that gives")
    print("  the muon at 105.66 MeV must give the bare electron at 0.511")
    print("  MeV when the ν companion is ABSENT.  This means the geometry")
    print("  is mode-dependent — it's not a universal metric, it's a")
    print("  metric PARAMETERIZED by the mode content.")
    print()
    print("Track 10 complete.")


if __name__ == '__main__':
    main()
