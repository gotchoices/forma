"""
R54 Track 1: Proton search on the full T⁶

Build the 6×6 metric from:
  - E-sheet: R53 Solution D (ε_e=397, s_e=2.004, electron=(1,2))
  - P-sheet: model-D (ε_p=0.55, s_p=0.162, proton=(1,3) for L_ring_p cal)
  - ν-sheet: R49 (ε_ν=5.0, s_ν=0.022)

Then search for compound 6-tuples near the proton mass (938.272 MeV)
with Q = +1, spin ½, and near the neutron mass (939.565 MeV) with
Q = 0, spin ½.

The metric supports all 12 individual cross-dimensional entries.
"""

import sys
import os
import math
import numpy as np
from itertools import product as iproduct

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model_d import (
    MaD, M_E_MEV, M_P_MEV, DM2_21,
    _TWO_PI_HC, solve_shear_for_alpha,
)


# ════════════════════════════════════════════════════════════════
#  Metric builder with individual cross entries
# ════════════════════════════════════════════════════════════════

def build_metric_individual(L, s_e, s_nu, s_p, sigma=None):
    """
    Build the 6×6 dimensionless metric G̃ with all 12 individual
    cross-dimensional entries.

    sigma: dict with keys like (0,2), (0,3), (1,2), (1,3),
           (0,4), (0,5), (1,4), (1,5), (2,4), (2,5), (3,4), (3,5)
           Each is a single float. Missing entries default to 0.
    """
    if sigma is None:
        sigma = {}

    # Build B = diag(L)(I + S)
    S = np.zeros((6, 6))
    S[0, 1] = s_e
    S[2, 3] = s_nu
    S[4, 5] = s_p

    B = np.diag(L) @ (np.eye(6) + S)
    G_phys = B.T @ B

    # Dimensionless metric
    Gt = np.empty((6, 6))
    for i in range(6):
        for j in range(6):
            Gt[i, j] = G_phys[i, j] / (L[i] * L[j])

    # Add individual cross entries
    for (i, j), val in sigma.items():
        if val != 0.0:
            Gt[i, j] += val
            Gt[j, i] += val

    # Check positive-definite
    eigs = np.linalg.eigvalsh(Gt)
    if np.any(eigs <= 0):
        return None, None

    Gti = np.linalg.inv(Gt)
    return Gt, Gti


def mode_energy(n, L, Gti):
    """Energy of a 6-tuple in MeV."""
    n_arr = np.asarray(n, dtype=float)
    n_tilde = n_arr / L
    E2 = _TWO_PI_HC ** 2 * n_tilde @ Gti @ n_tilde
    return math.sqrt(max(E2, 0))


def charge(n):
    return int(-n[0] + n[4])


def spin_half_count(n):
    return sum(1 for i in (0, 2, 4) if abs(n[i]) % 2 == 1)


# ════════════════════════════════════════════════════════════════
#  Setup
# ════════════════════════════════════════════════════════════════

# R53 Solution D: electron = (1, 2) at ε_e = 397.074, s_e = 2.004200
EPS_E = 397.074
S_E = 2.004200

# Model-D proton: (1, 3) at ε_p = 0.55, s_p from α
EPS_P = 0.55
S_P = solve_shear_for_alpha(EPS_P, n_tube=1, n_ring=3)

# R49 neutrino
EPS_NU = 5.0
S_NU = 0.022

M_PROTON = 938.272
M_NEUTRON = 939.565


def build_circumferences():
    """Compute L_ring for each sheet from reference masses."""
    # E-sheet: electron (1, 2) → 0.511 MeV
    mu_e = math.sqrt((1 / EPS_E) ** 2 + (2 - 1 * S_E) ** 2)
    L_ring_e = _TWO_PI_HC * mu_e / M_E_MEV

    # P-sheet: proton (1, 3) → 938.272 MeV
    mu_p = math.sqrt((1 / EPS_P) ** 2 + (3 - 1 * S_P) ** 2)
    L_ring_p = _TWO_PI_HC * mu_p / M_P_MEV

    # ν-sheet: from Δm²₂₁
    E0_nu = math.sqrt(DM2_21 / (4 * S_NU)) * 1e-6
    L_ring_nu = _TWO_PI_HC / E0_nu

    L = np.array([
        EPS_E * L_ring_e, L_ring_e,
        EPS_NU * L_ring_nu, L_ring_nu,
        EPS_P * L_ring_p, L_ring_p,
    ])
    return L, L_ring_e, L_ring_nu, L_ring_p


# ════════════════════════════════════════════════════════════════
#  Main
# ════════════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("R54 Track 1: Proton search on the full T⁶")
    print("=" * 70)
    print()

    L, L_ring_e, L_ring_nu, L_ring_p = build_circumferences()

    print(f"Sheet geometries:")
    print(f"  E-sheet: ε={EPS_E:.1f}, s={S_E:.6f}, L_ring={L_ring_e:.4f} fm")
    print(f"  ν-sheet: ε={EPS_NU:.1f}, s={S_NU:.5f}, L_ring={L_ring_nu:.1f} fm")
    print(f"  P-sheet: ε={EPS_P:.2f}, s={S_P:.6f}, L_ring={L_ring_p:.4f} fm")
    print()
    print(f"  Energy per unit μ:")
    print(f"    E-sheet: {_TWO_PI_HC / L_ring_e:.3f} MeV  (≈ {_TWO_PI_HC / L[1]:.3f} per ring)")
    print(f"    P-sheet: {_TWO_PI_HC / L_ring_p:.3f} MeV  (≈ {_TWO_PI_HC / L[5]:.3f} per ring)")
    print()

    # ── Baseline (σ = 0): pure proton mode check ───────────────
    Gt0, Gti0 = build_metric_individual(L, S_E, S_NU, S_P)
    if Gt0 is None:
        print("  Baseline metric not positive-definite!")
        return

    E_e = mode_energy((1, 2, 0, 0, 0, 0), L, Gti0)
    E_p = mode_energy((0, 0, 0, 0, 1, 3), L, Gti0)
    print(f"  Baseline (σ=0):")
    print(f"    E(1,2,0,0,0,0) = {E_e:.6f} MeV  (target: {M_E_MEV})")
    print(f"    E(0,0,0,0,1,3) = {E_p:.3f} MeV  (target: {M_PROTON})")
    print()

    # ── Scan compound modes near proton mass at σ = 0 ──────────
    print("=" * 70)
    print("Phase 1: Compound modes near proton mass at σ = 0")
    print("=" * 70)
    print()

    # Generate candidates: small windings on each sheet
    n_ranges = [
        (-3, 3),   # n₁ e-tube
        (-8, 8),   # n₂ e-ring
        (-2, 2),   # n₃ ν-tube
        (-2, 2),   # n₄ ν-ring
        (-3, 3),   # n₅ p-tube
        (-10, 10), # n₆ p-ring
    ]

    proton_candidates = []
    neutron_candidates = []

    for n in iproduct(*[range(lo, hi + 1) for lo, hi in n_ranges]):
        if all(ni == 0 for ni in n):
            continue
        Q = charge(n)
        sh = spin_half_count(n)
        E = mode_energy(n, L, Gti0)

        if abs(E - M_PROTON) < 50 and Q == 1 and sh in (1, 3):
            proton_candidates.append((abs(E - M_PROTON), n, E, Q, sh))
        if abs(E - M_NEUTRON) < 50 and Q == 0 and sh in (1, 3):
            neutron_candidates.append((abs(E - M_NEUTRON), n, E, Q, sh))

    proton_candidates.sort()
    neutron_candidates.sort()

    print(f"  Search range: {[f'{lo}..{hi}' for lo, hi in n_ranges]}")
    print(f"  Proton candidates (Q=+1, spin ½, within 50 MeV): "
          f"{len(proton_candidates)}")
    print(f"  Neutron candidates (Q=0, spin ½, within 50 MeV): "
          f"{len(neutron_candidates)}")
    print()

    print(f"  Top 20 proton candidates:")
    print(f"  {'mode':>30s}  {'E (MeV)':>10s}  {'ΔE':>8s}  Q  spin_h")
    print(f"  {'─'*30}  {'─'*10}  {'─'*8}  {'─'}  {'─'*6}")
    for _, n, E, Q, sh in proton_candidates[:20]:
        sheets = []
        if any(n[i] != 0 for i in (0, 1)):
            sheets.append('e')
        if any(n[i] != 0 for i in (2, 3)):
            sheets.append('ν')
        if any(n[i] != 0 for i in (4, 5)):
            sheets.append('p')
        print(f"  {str(n):>30s}  {E:>10.3f}  {E-M_PROTON:>+8.3f}  "
              f"{Q}  {sh}  {'+'.join(sheets)}")
    print()

    print(f"  Top 20 neutron candidates:")
    print(f"  {'mode':>30s}  {'E (MeV)':>10s}  {'ΔE':>8s}  Q  spin_h")
    print(f"  {'─'*30}  {'─'*10}  {'─'*8}  {'─'}  {'─'*6}")
    for _, n, E, Q, sh in neutron_candidates[:20]:
        sheets = []
        if any(n[i] != 0 for i in (0, 1)):
            sheets.append('e')
        if any(n[i] != 0 for i in (2, 3)):
            sheets.append('ν')
        if any(n[i] != 0 for i in (4, 5)):
            sheets.append('p')
        print(f"  {str(n):>30s}  {E:>10.3f}  {E-M_NEUTRON:>+8.3f}  "
              f"{Q}  {sh}  {'+'.join(sheets)}")
    print()

    # ── Phase 2: Sweep σ_ep entries ────────────────────────────
    print("=" * 70)
    print("Phase 2: Effect of individual cross entries on proton/neutron")
    print("=" * 70)
    print()

    # Test each of the 4 e-p entries individually
    ep_entries = [(0, 4), (0, 5), (1, 4), (1, 5)]
    ep_labels = ['e-tube↔p-tube', 'e-tube↔p-ring',
                 'e-ring↔p-tube', 'e-ring↔p-ring']

    for (i, j), label in zip(ep_entries, ep_labels):
        print(f"  Sweeping σ_{i+1}{j+1} ({label}):")
        print(f"    {'σ':>8s}  {'E_proton':>10s}  {'E_neutron_best':>15s}  "
              f"{'Δn':>8s}  {'neutron_mode':>30s}")
        print(f"    {'─'*8}  {'─'*10}  {'─'*15}  {'─'*8}  {'─'*30}")

        for sigma_val in np.linspace(-0.3, 0.3, 13):
            sigma = {(i, j): sigma_val}
            Gt, Gti = build_metric_individual(L, S_E, S_NU, S_P, sigma)
            if Gt is None:
                print(f"    {sigma_val:>+8.3f}  {'singular':>10s}")
                continue

            E_p_now = mode_energy((0, 0, 0, 0, 1, 3), L, Gti)

            # Find best neutron
            best_n = None
            for n in iproduct(*[range(lo, hi + 1) for lo, hi in n_ranges]):
                if all(ni == 0 for ni in n):
                    continue
                if charge(n) != 0:
                    continue
                if spin_half_count(n) not in (1, 3):
                    continue
                E = mode_energy(n, L, Gti)
                dE = abs(E - M_NEUTRON)
                if best_n is None or dE < best_n[0]:
                    best_n = (dE, n, E)

            if best_n:
                dn = best_n[1]
                print(f"    {sigma_val:>+8.3f}  {E_p_now:>10.3f}  "
                      f"{best_n[2]:>15.3f}  "
                      f"{best_n[2]-M_NEUTRON:>+8.3f}  {str(dn):>30s}")
            else:
                print(f"    {sigma_val:>+8.3f}  {E_p_now:>10.3f}  {'none':>15s}")
        print()

    # ── Phase 3: Combined e-p cross entries ────────────────────
    print("=" * 70)
    print("Phase 3: Combined σ_ep sweep (all 4 entries equal)")
    print("=" * 70)
    print()
    print(f"    {'σ_ep':>8s}  {'E(proton)':>10s}  {'best neutron E':>15s}  "
          f"{'Δn':>8s}  {'mode':>30s}")
    print(f"    {'─'*8}  {'─'*10}  {'─'*15}  {'─'*8}  {'─'*30}")

    for sigma_val in np.linspace(-0.3, 0.3, 31):
        sigma = {(0, 4): sigma_val, (0, 5): sigma_val,
                 (1, 4): sigma_val, (1, 5): sigma_val}
        Gt, Gti = build_metric_individual(L, S_E, S_NU, S_P, sigma)
        if Gt is None:
            print(f"    {sigma_val:>+8.3f}  {'singular':>10s}")
            continue

        E_p_now = mode_energy((0, 0, 0, 0, 1, 3), L, Gti)

        best_n = None
        for n in iproduct(*[range(lo, hi + 1) for lo, hi in n_ranges]):
            if all(ni == 0 for ni in n):
                continue
            if charge(n) != 0:
                continue
            if spin_half_count(n) not in (1, 3):
                continue
            E = mode_energy(n, L, Gti)
            dE = abs(E - M_NEUTRON)
            if best_n is None or dE < best_n[0]:
                best_n = (dE, n, E)

        if best_n:
            print(f"    {sigma_val:>+8.3f}  {E_p_now:>10.3f}  "
                  f"{best_n[2]:>15.3f}  "
                  f"{best_n[2]-M_NEUTRON:>+8.3f}  {str(best_n[1]):>30s}")
    print()

    print("Track 1 complete.")


if __name__ == '__main__':
    main()
