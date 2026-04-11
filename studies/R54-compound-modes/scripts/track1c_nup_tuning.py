"""
R54 Track 1c: ν-p cross entries to independently tune the neutron

The proton (0,0,0,0,1,3) has no ν content → ν-p cross entries
(σ₃₅, σ₃₆, σ₄₅, σ₄₆) don't affect it.  The neutron
(-1,-2,ν,ν,-1,-3) DOES have ν content → ν-p entries shift it.

Strategy:
1. Keep σ₂₅, σ₂₆ = 0 (so proton stays at 938.272 exactly)
2. Sweep σ₃₅, σ₃₆, σ₄₅, σ₄₆ to push the neutron to ~939.5
3. Report the full landscape and best point
4. Then check: what do pions, kaons, and other hadrons look like
   at this geometry?
"""

import sys
import os
import math
import numpy as np
from itertools import product as iproduct

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model_d import (
    M_E_MEV, M_P_MEV, DM2_21,
    _TWO_PI_HC, solve_shear_for_alpha,
)


def build_metric(L, s_e, s_nu, s_p, sigma=None):
    if sigma is None:
        sigma = {}
    S = np.zeros((6, 6))
    S[0, 1] = s_e; S[2, 3] = s_nu; S[4, 5] = s_p
    B = np.diag(L) @ (np.eye(6) + S)
    Gt = B.T @ B
    for i in range(6):
        for j in range(6):
            Gt[i, j] /= (L[i] * L[j])
    for (i, j), val in sigma.items():
        Gt[i, j] += val; Gt[j, i] += val
    eigs = np.linalg.eigvalsh(Gt)
    if np.any(eigs <= 0):
        return None, None
    return Gt, np.linalg.inv(Gt)


def mode_energy(n, L, Gti):
    n_arr = np.asarray(n, dtype=float)
    nt = n_arr / L
    E2 = _TWO_PI_HC ** 2 * nt @ Gti @ nt
    return math.sqrt(max(E2, 0))


def charge(n): return int(-n[0] + n[4])
def spin_half_count(n): return sum(1 for i in (0, 2, 4) if abs(n[i]) % 2 == 1)


# Setup
EPS_E, S_E = 397.074, 2.004200
EPS_P = 0.55
S_P = solve_shear_for_alpha(EPS_P, n_tube=1, n_ring=3)
EPS_NU, S_NU = 5.0, 0.022

mu_e = math.sqrt((1 / EPS_E) ** 2 + (2 - S_E) ** 2)
L_ring_e = _TWO_PI_HC * mu_e / M_E_MEV
mu_p = math.sqrt((1 / EPS_P) ** 2 + (3 - S_P) ** 2)
L_ring_p = _TWO_PI_HC * mu_p / M_P_MEV
E0_nu = math.sqrt(DM2_21 / (4 * S_NU)) * 1e-6
L_ring_nu = _TWO_PI_HC / E0_nu

L = np.array([EPS_E * L_ring_e, L_ring_e,
              EPS_NU * L_ring_nu, L_ring_nu,
              EPS_P * L_ring_p, L_ring_p])

M_N = 939.565
M_P = 938.272

# Neutron candidate
N_NEUTRON = (-1, -2, -1, 0, -1, -3)  # primary; will test ν variants

# Search ranges for compound modes
n_ranges = [(-3, 3), (-8, 8), (-2, 2), (-2, 2), (-3, 3), (-10, 10)]

# Particle inventory for hadron check
PARTICLES = [
    ('proton', 938.272, +1, 0.5),
    ('neutron', 939.565, 0, 0.5),
    ('pi+', 139.570, +1, None),  # spin 0 or any
    ('pi0', 134.977, 0, 0.0),
    ('pi-', 139.570, -1, None),
    ('K+', 493.677, +1, None),
    ('K0', 497.611, 0, 0.0),
    ('eta', 547.862, 0, 0.0),
    ('Lambda', 1115.683, 0, 0.5),
    ('Sigma+', 1189.37, +1, 0.5),
    ('Sigma-', 1197.449, -1, 0.5),
    ('Xi0', 1314.86, 0, 0.5),
    ('Xi-', 1321.71, -1, 0.5),
    ('Omega-', 1672.45, -1, None),
    ('Delta+', 1232.0, +1, None),
    ('rho', 775.26, +1, None),
    ('phi', 1019.5, 0, None),
    ('eta_prime', 957.78, 0, 0.0),
    ('muon', 105.658, -1, 0.5),
    ('tau', 1776.86, -1, 0.5),
]


def find_best_mode(Gti, target_mass, target_Q, target_spin=None, tolerance=100):
    """Find the mode closest to target mass with given Q and spin."""
    best = None
    for n in iproduct(*[range(lo, hi + 1) for lo, hi in n_ranges]):
        if all(ni == 0 for ni in n):
            continue
        if charge(n) != target_Q:
            continue
        sh = spin_half_count(n)
        if target_spin is not None:
            if target_spin == 0.5 and sh not in (1, 3):
                continue
            if target_spin == 0.0 and sh not in (0, 2):
                continue
        E = mode_energy(n, L, Gti)
        dE = abs(E - target_mass)
        if dE > tolerance:
            continue
        if best is None or dE < best[0]:
            best = (dE, n, E, sh)
    return best


def main():
    print("=" * 78)
    print("R54 Track 1c: ν-p tuning for independent neutron control")
    print("=" * 78)
    print()

    # ── Phase 1: Sweep each ν-p entry individually ─────────────
    print("Phase 1: Individual ν-p entries (σ₂₅ = σ₂₆ = 0, proton untouched)")
    print()

    nup_entries = [(2, 4), (2, 5), (3, 4), (3, 5)]
    nup_labels = ['ν-tube↔p-tube', 'ν-tube↔p-ring',
                  'ν-ring↔p-tube', 'ν-ring↔p-ring']

    # Test with a specific neutron candidate
    neutron_variants = [
        (-1, -2, -1, 0, -1, -3),
        (-1, -2, 1, 0, -1, -3),
        (-1, -2, -1, -1, -1, -3),
        (-1, -2, -1, 1, -1, -3),
        (-1, -2, 0, -1, -1, -3),
        (-1, -2, 0, 1, -1, -3),
    ]

    for (i, j), label in zip(nup_entries, nup_labels):
        print(f"  σ_{i+1}{j+1} ({label}):")
        print(f"    {'σ':>7s}  {'E_proton':>10s}  {'E_neutron':>10s}  "
              f"{'ΔE_p':>8s}  {'ΔE_n':>8s}  {'n-p':>6s}")
        print(f"    {'─'*7}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'*8}  {'─'*6}")

        for sv in np.linspace(-0.3, 0.3, 31):
            sigma = {(i, j): float(sv)}
            Gt, Gti = build_metric(L, S_E, S_NU, S_P, sigma)
            if Gt is None:
                continue

            E_p = mode_energy((0, 0, 0, 0, 1, 3), L, Gti)

            # Best neutron across ν variants
            best_E_n = None
            for nv in neutron_variants:
                E_n = mode_energy(nv, L, Gti)
                if best_E_n is None or abs(E_n - M_N) < abs(best_E_n - M_N):
                    best_E_n = E_n

            dE_p = E_p - M_P
            dE_n = best_E_n - M_N
            print(f"    {sv:>+7.3f}  {E_p:>10.3f}  {best_E_n:>10.3f}  "
                  f"{dE_p:>+8.3f}  {dE_n:>+8.3f}  {best_E_n-E_p:>+6.3f}")
        print()

    # ── Phase 2: 2D sweep of the two most promising ν-p entries
    print("=" * 78)
    print("Phase 2: 2D sweep of most promising ν-p pair")
    print("=" * 78)
    print()

    # First, identify which entry moves the neutron most
    # (from Phase 1 output — but let's just try σ₄₅ and σ₄₆
    # since ν-ring couples more strongly than ν-tube at ε_ν=5)

    grid = np.linspace(-0.3, 0.3, 31)
    best_overall = None

    for s45 in grid[::2]:
        for s46 in grid[::2]:
            sigma = {(3, 4): float(s45), (3, 5): float(s46)}
            Gt, Gti = build_metric(L, S_E, S_NU, S_P, sigma)
            if Gt is None:
                continue

            E_p = mode_energy((0, 0, 0, 0, 1, 3), L, Gti)
            dE_p = abs(E_p - M_P)

            # Best neutron
            best_n = None
            for nv in neutron_variants:
                E_n = mode_energy(nv, L, Gti)
                dE_n = abs(E_n - M_N)
                if best_n is None or dE_n < best_n[0]:
                    best_n = (dE_n, nv, E_n)

            score = dE_p + best_n[0]  # want both small
            if best_overall is None or score < best_overall['score']:
                best_overall = {
                    's45': float(s45), 's46': float(s46),
                    'E_p': E_p, 'E_n': best_n[2], 'n_mode': best_n[1],
                    'score': score, 'dE_p': E_p - M_P,
                    'dE_n': best_n[2] - M_N,
                }

    if best_overall:
        b = best_overall
        print(f"  Best (σ₄₅, σ₄₆): ({b['s45']:+.3f}, {b['s46']:+.3f})")
        print(f"    Proton: {b['E_p']:.3f} MeV (Δ = {b['dE_p']:+.3f})")
        print(f"    Neutron: {b['E_n']:.3f} MeV (Δ = {b['dE_n']:+.3f})")
        print(f"    n-p: {b['E_n']-b['E_p']:+.3f} MeV (obs: +1.293)")
        print(f"    Neutron mode: {b['n_mode']}")
        print()

    # ── Phase 3: Full particle inventory at best geometry ──────
    print("=" * 78)
    print("Phase 3: Full particle inventory at best geometry")
    print("=" * 78)
    print()

    if best_overall:
        sigma_best = {(3, 4): best_overall['s45'],
                      (3, 5): best_overall['s46']}
    else:
        sigma_best = {}

    Gt, Gti = build_metric(L, S_E, S_NU, S_P, sigma_best)

    print(f"  Geometry: σ₄₅={best_overall['s45'] if best_overall else 0:+.3f}, "
          f"σ₄₆={best_overall['s46'] if best_overall else 0:+.3f}")
    print()
    print(f"  {'Particle':>12s}  {'Obs (MeV)':>10s}  {'Pred (MeV)':>10s}  "
          f"{'Δm/m':>8s}  {'mode':>30s}  {'sheets':>8s}")
    print(f"  {'─'*12}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'*30}  {'─'*8}")

    for name, mass, Q, spin in PARTICLES:
        result = find_best_mode(Gti, mass, Q, spin)
        if result is None:
            print(f"  {name:>12s}  {mass:>10.3f}  {'—':>10s}  {'—':>8s}  "
                  f"{'(none in range)':>30s}")
            continue
        dE, n, E, sh = result
        rel = dE / mass * 100
        sh_list = []
        if any(n[i] != 0 for i in (0, 1)): sh_list.append('e')
        if any(n[i] != 0 for i in (2, 3)): sh_list.append('ν')
        if any(n[i] != 0 for i in (4, 5)): sh_list.append('p')
        print(f"  {name:>12s}  {mass:>10.3f}  {E:>10.3f}  "
              f"{rel:>7.2f}%  {str(n):>30s}  {'+'.join(sh_list):>8s}")

    # ── Check specifically: is there ANYTHING near the pion? ───
    print()
    print("=" * 78)
    print("Pion focus: all modes within 20 MeV of 135-140 MeV")
    print("=" * 78)
    print()

    pion_modes = []
    for n in iproduct(*[range(lo, hi + 1) for lo, hi in n_ranges]):
        if all(ni == 0 for ni in n):
            continue
        E = mode_energy(n, L, Gti)
        if 115 < E < 160:
            Q = charge(n)
            sh = spin_half_count(n)
            pion_modes.append((E, n, Q, sh))

    pion_modes.sort()
    print(f"  Modes in 115–160 MeV range: {len(pion_modes)}")
    print(f"  {'E (MeV)':>10s}  {'mode':>30s}  {'Q':>3s}  {'sh':>3s}  {'sheets':>8s}")
    print(f"  {'─'*10}  {'─'*30}  {'─'*3}  {'─'*3}  {'─'*8}")
    for E, n, Q, sh in pion_modes[:30]:
        sh_list = []
        if any(n[i] != 0 for i in (0, 1)): sh_list.append('e')
        if any(n[i] != 0 for i in (2, 3)): sh_list.append('ν')
        if any(n[i] != 0 for i in (4, 5)): sh_list.append('p')
        print(f"  {E:>10.3f}  {str(n):>30s}  {Q:>+3d}  {sh:>3d}  "
              f"{'+'.join(sh_list):>8s}")

    print()
    print("Track 1c complete.")


if __name__ == '__main__':
    main()
