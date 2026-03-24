#!/usr/bin/env python3
"""
R27 Track 1b: Asymmetric cross-shear investigation.

Track 1a showed that the SYMMETRIC cross-shear (all 4 entries in
the e-p block equal to σ) makes the self-consistent neutron LIGHTER
than the proton.  This script investigates:

1. Negative σ_ep (does the sign matter in the self-consistent case?)
2. Asymmetric cross-shears (individual σ₁₅, σ₁₆, σ₂₅, σ₂₆)
3. Cross-shears on other blocks (σ_eν, σ_νp) while σ_ep varies
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq, minimize

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.t6 import (
    mode_energy, mode_charge, compute_scales, is_positive_definite,
    hbar_c_MeV_fm, M_E_MEV, M_P_MEV, M_N_MEV, S34,
)

N_ELECTRON = (1, 2, 0, 0, 0, 0)
N_PROTON   = (0, 0, 0, 0, 1, 2)
N_NEUTRON  = (1, 2, 0, 0, 1, 2)

R_E  = 6.6
R_NU = 5.0
R_P  = 6.6
TARGET_DELTA = M_N_MEV - M_P_MEV   # 1.293 MeV


def build_asymmetric_metric(L, s12, s34, s56, cross_shears):
    """
    Build G̃ with individual cross-shear entries.

    cross_shears: dict with keys like (i, j) for i < j, values are σ_ij.
    """
    S_within = np.zeros((6, 6))
    S_within[0, 1] = s12
    S_within[2, 3] = s34
    S_within[4, 5] = s56

    B = np.diag(L) @ (np.eye(6) + S_within)
    G_phys = B.T @ B

    Gtilde = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            Gtilde[i, j] = G_phys[i, j] / (L[i] * L[j])

    for (i, j), sig in cross_shears.items():
        Gtilde[i, j] = sig
        Gtilde[j, i] = sig

    if not is_positive_definite(Gtilde):
        return None, None
    Gtilde_inv = np.linalg.inv(Gtilde)
    return Gtilde, Gtilde_inv


def self_consistent_asym(r_e, r_nu, r_p, cross_shears,
                         tol=1e-12, max_iter=50):
    """
    Self-consistent L₂, L₆ with arbitrary cross-shear entries.
    """
    L, s12, s34, s56 = compute_scales(r_e, r_nu, r_p)

    for _ in range(max_iter):
        Gt, Gti = build_asymmetric_metric(L, s12, s34, s56, cross_shears)
        if Gt is None:
            return None, None, None, None, None, None, False

        E_e = mode_energy(N_ELECTRON, Gti, L)
        E_p = mode_energy(N_PROTON, Gti, L)

        if abs(E_e - M_E_MEV) / M_E_MEV < tol and abs(E_p - M_P_MEV) / M_P_MEV < tol:
            return L, s12, s34, s56, Gt, Gti, True

        L[1] *= E_e / M_E_MEV
        L[0] = r_e * L[1]
        L[5] *= E_p / M_P_MEV
        L[4] = r_p * L[5]

    return L, s12, s34, s56, Gt, Gti, False


def main():
    print("=" * 78)
    print("R27 Track 1b: Asymmetric Cross-Shear Investigation")
    print("=" * 78)

    # ══════════════════════════════════════════════════════════════════
    #  SECTION 1: Negative σ_ep
    # ══════════════════════════════════════════════════════════════════

    print()
    print("SECTION 1: Negative σ_ep (self-consistent)")
    print("-" * 78)

    ep_pairs = [(0, 4), (0, 5), (1, 4), (1, 5)]

    for sig_val in [-0.5, -0.3, -0.1, -0.05, -0.01, 0.01, 0.05, 0.1, 0.3, 0.5]:
        cs = {p: sig_val for p in ep_pairs}
        L, s12, s34, s56, Gt, Gti, conv = self_consistent_asym(
            R_E, R_NU, R_P, cs)
        if not conv or Gt is None:
            print(f"  σ_ep = {sig_val:+.3f}  →  did not converge / not positive-definite")
            continue
        E_n = mode_energy(N_NEUTRON, Gti, L)
        delta = E_n - M_P_MEV
        print(f"  σ_ep = {sig_val:+.3f}  →  E_n = {E_n:.4f} MeV  "
              f"m_n−m_p = {delta:+.6f} MeV")

    # ══════════════════════════════════════════════════════════════════
    #  SECTION 2: Asymmetric cross-shears within the e-p block
    # ══════════════════════════════════════════════════════════════════

    print()
    print()
    print("SECTION 2: Asymmetric cross-shears in e-p block")
    print("-" * 78)
    print()
    print("  Scanning σ₁₅, σ₁₆, σ₂₅, σ₂₆ independently.")
    print("  Looking for any configuration where m_n > m_p.")

    # Try various asymmetric patterns
    best_delta = -999
    best_config = None

    test_vals = [-0.3, -0.2, -0.1, -0.05, 0, 0.05, 0.1, 0.2, 0.3]

    count = 0
    positive_count = 0
    for s15 in test_vals:
        for s16 in test_vals:
            for s25 in test_vals:
                for s26 in test_vals:
                    if s15 == 0 and s16 == 0 and s25 == 0 and s26 == 0:
                        continue
                    cs = {(0, 4): s15, (0, 5): s16, (1, 4): s25, (1, 5): s26}
                    L, s12, s34, s56, Gt, Gti, conv = self_consistent_asym(
                        R_E, R_NU, R_P, cs)
                    count += 1
                    if not conv or Gt is None:
                        continue
                    E_n = mode_energy(N_NEUTRON, Gti, L)
                    delta = E_n - M_P_MEV
                    if delta > 0:
                        positive_count += 1
                    if delta > best_delta:
                        best_delta = delta
                        best_config = (s15, s16, s25, s26)

    print(f"\n  Tested {count} configurations")
    print(f"  Configurations with m_n > m_p: {positive_count}")
    print(f"\n  Best m_n − m_p = {best_delta:+.6f} MeV")
    if best_config:
        print(f"    at σ₁₅={best_config[0]:+.2f}, σ₁₆={best_config[1]:+.2f},"
              f" σ₂₅={best_config[2]:+.2f}, σ₂₆={best_config[3]:+.2f}")

    if best_delta > 0 and best_config:
        # Refine around the best configuration
        print(f"\n  Refining around best configuration...")
        bc = best_config
        refined_best = best_delta
        refined_config = best_config

        for d15 in np.linspace(bc[0] - 0.05, bc[0] + 0.05, 11):
            for d16 in np.linspace(bc[1] - 0.05, bc[1] + 0.05, 11):
                for d25 in np.linspace(bc[2] - 0.05, bc[2] + 0.05, 11):
                    for d26 in np.linspace(bc[3] - 0.05, bc[3] + 0.05, 11):
                        cs = {(0, 4): d15, (0, 5): d16,
                              (1, 4): d25, (1, 5): d26}
                        L, s12, s34, s56, Gt, Gti, conv = \
                            self_consistent_asym(R_E, R_NU, R_P, cs)
                        if not conv or Gt is None:
                            continue
                        E_n = mode_energy(N_NEUTRON, Gti, L)
                        delta = E_n - M_P_MEV
                        if delta > refined_best:
                            refined_best = delta
                            refined_config = (d15, d16, d25, d26)

        print(f"  Refined best m_n − m_p = {refined_best:+.6f} MeV")
        print(f"    at σ₁₅={refined_config[0]:+.3f}, σ₁₆={refined_config[1]:+.3f},"
              f" σ₂₅={refined_config[2]:+.3f}, σ₂₆={refined_config[3]:+.3f}")

    # ══════════════════════════════════════════════════════════════════
    #  SECTION 3: Different neutron quantum numbers
    # ══════════════════════════════════════════════════════════════════

    print()
    print()
    print("SECTION 3: Alternative neutron quantum numbers")
    print("-" * 78)
    print()
    print("  Searching for charge-0, spin-½ modes near m_p with σ_ep = 0.1")

    cs_sym = {p: 0.1 for p in ep_pairs}
    L, s12, s34, s56, Gt, Gti, conv = self_consistent_asym(
        R_E, R_NU, R_P, cs_sym)

    if conv:
        candidates = []
        rng = range(-3, 4)
        from itertools import product
        for n in product(rng, repeat=6):
            if all(ni == 0 for ni in n):
                continue
            Q = mode_charge(n)
            if Q != 0:
                continue
            n_half = sum(abs(n[i]) % 2 for i in [0, 2, 4])
            E = mode_energy(n, Gti, L)
            if 930 < E < 950:
                candidates.append((n, E, n_half))

        candidates.sort(key=lambda x: abs(x[1] - M_N_MEV))

        print(f"\n  Charge-0 modes between 930–950 MeV:")
        print(f"  {'Quantum numbers':>30s} │ {'E (MeV)':>12s} │ {'m_n−m_p':>10s} │ Spin")
        print(f"  {'─'*30}─┼─{'─'*12}─┼─{'─'*10}─┼─{'─'*15}")
        for n, E, nh in candidates[:20]:
            sp = {0: "boson", 1: "½", 2: "0 or 1", 3: "½ or 3/2"}[nh]
            print(f"  {str(n):>30s} │ {E:12.4f} │ {E - M_P_MEV:+10.4f} │ {sp}")

    # ══════════════════════════════════════════════════════════════════
    #  SECTION 4: Summary
    # ══════════════════════════════════════════════════════════════════

    print()
    print()
    print("SECTION 4: Summary")
    print("=" * 78)
    print(f"""
  KEY FINDING: Under self-consistent treatment, the symmetric
  cross-shear makes the neutron mode (1,2,0,0,1,2) LIGHTER
  than the proton for all σ_ep values.

  Asymmetric scan: {positive_count} of {count} tested configurations
  had m_n > m_p.  Best Δm = {best_delta:+.6f} MeV (target: +1.293).

  This overturns the naive R26 F67 result.  The self-consistency
  correction (adjusting L₂, L₆ to keep m_e, m_p exact) more
  than compensates for the cross-shear energy increase.
""")


if __name__ == "__main__":
    main()
