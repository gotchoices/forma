"""
R50 Track 10b: Can σ_eν boost the muon mass without changing L_ring_e?

The user's idea: the free electron has n₃ = n₄ = 0, so σ_eν
doesn't affect it.  The muon has ν windings, so σ_eν activates
and changes the effective metric.  L_ring_e stays fixed.

Question: does changing σ_eν (at fixed L_ring_e) change the
energy of e-sheet modes?  If yes, mode-dependent σ_eν is a
viable mechanism for the muon mass.

The mechanism would be: σ_eν modifies G̃⁻¹_ee through the
Schur complement (matrix inversion of the block structure).
Even though the ν sheet is huge (L_ν >> L_e), the DIMENSIONLESS
metric G̃ has O(1) entries because L factors cancel in the
normalization.  So σ_eν = O(1) can change G̃⁻¹ substantially.

This script:
1. Builds a baseline model at σ_eν = 0, records L_ring_e
2. Rebuilds with same L_ring_e at increasing σ_eν
3. Computes E(1,2,0,0,0,0) and E(1,2,n₃,n₄,0,0) at each σ_eν
4. Reports whether σ_eν can reach the muon mass (105.658 MeV)
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

EPS_E = 0.65
EPS_NU = 5.0
EPS_P = 0.55
S_NU_DEFAULT = 0.022


def main():
    print("=" * 78)
    print("Track 10b: σ_eν boost — can cross-shear alone create the muon mass?")
    print("=" * 78)
    print()

    # ── Baseline model (σ = 0) ──────────────────────────────────────
    s_e = solve_shear_for_alpha(EPS_E)
    s_p = solve_shear_for_alpha(EPS_P, n_tube=1, n_ring=3)
    s_nu = S_NU_DEFAULT

    m0 = MaD.from_physics(eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
                           n_e=(1, 2), n_p=(1, 3))

    L_ring_e = m0.L_ring[0]
    L_ring_nu = m0.L_ring[1]
    L_ring_p = m0.L_ring[2]

    print(f"Baseline (σ_eν = 0):")
    print(f"  s_e = {s_e:.6f},  s_p = {s_p:.6f},  s_ν = {s_nu}")
    print(f"  L_ring_e = {L_ring_e:.4f} fm")
    print(f"  L_ring_ν = {L_ring_nu:.4f} fm")
    print(f"  L_ring_p = {L_ring_p:.4f} fm")
    print(f"  E(1,2,0,0,0,0) = {m0.energy((1,2,0,0,0,0)):.6f} MeV")
    print()

    # ── Key test: how does G̃⁻¹_ee change with σ_eν? ────────────────
    print("=" * 78)
    print("Test 1: How does E(1,2,0,0,0,0) change with σ_eν at FIXED L_ring_e?")
    print("=" * 78)
    print()
    print("  If σ_eν modifies the Schur complement of the e-block,")
    print("  then even modes with n₃=n₄=0 will feel the change")
    print("  (through G̃⁻¹_ee, which depends on the full metric).")
    print()

    sigma_grid = np.concatenate([
        np.linspace(0, 0.5, 11),
        np.linspace(0.6, 1.0, 5),
        np.linspace(1.5, 5.0, 8),
        np.linspace(6.0, 20.0, 8),
        np.linspace(30, 100, 8),
    ])

    print(f"  {'σ_eν':>8s}  {'E(1,2,0,0,0,0)':>16s}  {'E(1,2,1,1,0,0)':>16s}  "
          f"{'E(1,2,2,3,0,0)':>16s}  {'metric ok?':>10s}")
    print(f"  {'─'*8}  {'─'*16}  {'─'*16}  {'─'*16}  {'─'*10}")

    for sigma in sigma_grid:
        try:
            model = MaD(
                eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
                s_e=s_e, s_nu=s_nu, s_p=s_p,
                L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
                sigma_enu=float(sigma))
            E_bare = model.energy((1, 2, 0, 0, 0, 0))
            E_11 = model.energy((1, 2, 1, 1, 0, 0))
            E_23 = model.energy((1, 2, 2, 3, 0, 0))
            print(f"  {sigma:>8.2f}  {E_bare:>16.6f}  {E_11:>16.6f}  "
                  f"{E_23:>16.6f}  {'✓':>10s}")
        except ValueError as e:
            print(f"  {sigma:>8.2f}  {'—':>16s}  {'—':>16s}  "
                  f"{'—':>16s}  {'✗ (singular)':>16s}")

    print()

    # ── Also try negative σ_eν ──────────────────────────────────────
    print("=" * 78)
    print("Test 2: Negative σ_eν")
    print("=" * 78)
    print()
    print(f"  {'σ_eν':>8s}  {'E(1,2,0,0,0,0)':>16s}  {'E(1,2,1,1,0,0)':>16s}  "
          f"{'E(1,2,2,3,0,0)':>16s}  {'metric ok?':>10s}")
    print(f"  {'─'*8}  {'─'*16}  {'─'*16}  {'─'*16}  {'─'*10}")

    for sigma in -sigma_grid:
        if sigma == 0:
            continue
        try:
            model = MaD(
                eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
                s_e=s_e, s_nu=s_nu, s_p=s_p,
                L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
                sigma_enu=float(sigma))
            E_bare = model.energy((1, 2, 0, 0, 0, 0))
            E_11 = model.energy((1, 2, 1, 1, 0, 0))
            E_23 = model.energy((1, 2, 2, 3, 0, 0))
            print(f"  {sigma:>8.2f}  {E_bare:>16.6f}  {E_11:>16.6f}  "
                  f"{E_23:>16.6f}  {'✓':>10s}")
        except ValueError as e:
            print(f"  {sigma:>8.2f}  {'—':>16s}  {'—':>16s}  "
                  f"{'—':>16s}  {'✗ (singular)':>16s}")

    print()

    # ── Test 3: What if σ_eν is mode-dependent? ────────────────────
    print("=" * 78)
    print("Test 3: Mode-dependent σ_eν — the user's proposal")
    print("=" * 78)
    print()
    print("  Scenario: σ_eν = 0 for the bare electron (no ν windings),")
    print("  σ_eν = σ_large for the muon (ν windings present).")
    print()
    print("  The electron stays at 0.511 MeV because it sees σ_eν = 0.")
    print("  The muon sees σ_eν ≠ 0 and gets a boosted mass.")
    print()
    print("  For this to work, E(1,2,0,0,0,0) at σ_eν = σ_large must")
    print("  be ~105.7 MeV.  (The ν windings contribute ~0 directly;")
    print("  the mass comes from the modified G̃⁻¹_ee Schur complement.)")
    print()

    # Find the σ_eν that gives E(1,2,0,0,0,0) = 105.658 MeV
    target = 105.658

    # Binary search for σ_eν
    best_pos = None
    best_neg = None

    for sigma in np.linspace(0, 500, 5001):
        for sign in [+1, -1]:
            s = sign * sigma
            try:
                model = MaD(
                    eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
                    s_e=s_e, s_nu=s_nu, s_p=s_p,
                    L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
                    sigma_enu=float(s))
                E = model.energy((1, 2, 0, 0, 0, 0))
                delta = abs(E - target)
                if sign > 0:
                    if best_pos is None or delta < best_pos[1]:
                        best_pos = (s, delta, E)
                else:
                    if best_neg is None or delta < best_neg[1]:
                        best_neg = (s, delta, E)
            except ValueError:
                pass

    for label, best in [("Positive σ_eν", best_pos), ("Negative σ_eν", best_neg)]:
        if best is None:
            print(f"  {label}: no valid model found")
        else:
            s, delta, E = best
            rel = delta / target * 100
            print(f"  {label}: best σ_eν = {s:+.2f}  "
                  f"→ E(1,2,0,0,0,0) = {E:.3f} MeV  "
                  f"(Δ = {delta:.3f}, {rel:.2f}%)")
    print()

    # ── Test 4: What does the muon look like? ───────────────────────
    print("=" * 78)
    print("Test 4: If σ_eν gives 105.66 MeV, what are other mode energies?")
    print("=" * 78)
    print()

    for label, best in [("Positive", best_pos), ("Negative", best_neg)]:
        if best is None or best[1] > 50:
            print(f"  {label}: not close enough, skipping")
            continue
        s_target = best[0]
        try:
            model = MaD(
                eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
                s_e=s_e, s_nu=s_nu, s_p=s_p,
                L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
                sigma_enu=float(s_target))
        except ValueError:
            print(f"  {label}: model fails at σ_eν = {s_target}")
            continue

        print(f"  {label} σ_eν = {s_target:+.2f}:")
        print(f"    Muon candidate  (1,2,0,0,0,0):  {model.energy((1,2,0,0,0,0)):.3f} MeV")
        for n3, n4 in [(0,0), (1,0), (0,1), (1,1), (-1,1), (1,2), (2,3),
                        (-2,-3), (1,-1)]:
            n = (1, 2, n3, n4, 0, 0)
            E = model.energy(n)
            print(f"    (1, 2, {n3:>2d}, {n4:>2d}, 0, 0):  {E:>10.3f} MeV  "
                  f"  Q={MaD.charge(n):+d}  spin={MaD.spin_total(n)}")

        # Also: what does the proton look like?
        print(f"    Proton (0,0,0,0,1,3):  "
              f"{model.energy((0,0,0,0,1,3)):.3f} MeV")
        print()

    print("Track 10b complete.")


if __name__ == '__main__':
    main()
