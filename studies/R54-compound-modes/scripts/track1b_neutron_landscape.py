"""
R54 Track 1b: Neutron landscape — all candidates, all cross entries

Don't pick one neutron candidate prematurely.  Map the full
landscape:
  1. At σ = 0, find ALL Q=0 spin-½ modes within 50 MeV of 939.565
  2. For each of the active cross entries (σ₂₅, σ₂₆), sweep and
     track how EVERY candidate's energy moves
  3. For 2D combinations of (σ₂₅, σ₂₆), find all modes near the
     neutron mass and report which ones converge
  4. Report: how many distinct neutron candidates exist at the
     best-fit cross-shear?
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
def sheets(n):
    s = []
    if any(n[i] != 0 for i in (0, 1)): s.append('e')
    if any(n[i] != 0 for i in (2, 3)): s.append('ν')
    if any(n[i] != 0 for i in (4, 5)): s.append('p')
    return '+'.join(s)


# Setup
EPS_E, S_E = 397.074, 2.004200
EPS_P, S_P = 0.55, solve_shear_for_alpha(0.55, n_tube=1, n_ring=3)
EPS_NU, S_NU = 5.0, 0.022

mu_e = math.sqrt((1/EPS_E)**2 + (2 - S_E)**2)
L_ring_e = _TWO_PI_HC * mu_e / M_E_MEV
mu_p = math.sqrt((1/EPS_P)**2 + (3 - S_P)**2)
L_ring_p = _TWO_PI_HC * mu_p / M_P_MEV
E0_nu = math.sqrt(DM2_21 / (4 * S_NU)) * 1e-6
L_ring_nu = _TWO_PI_HC / E0_nu

L = np.array([EPS_E * L_ring_e, L_ring_e,
              EPS_NU * L_ring_nu, L_ring_nu,
              EPS_P * L_ring_p, L_ring_p])

M_N = 939.565
M_P = 938.272

n_ranges = [(-3, 3), (-8, 8), (-2, 2), (-2, 2), (-3, 3), (-10, 10)]


def find_neutron_candidates(Gti, tolerance=50.0):
    """Find ALL Q=0 spin-½ modes within tolerance of neutron mass."""
    cands = []
    for n in iproduct(*[range(lo, hi+1) for lo, hi in n_ranges]):
        if all(ni == 0 for ni in n): continue
        if charge(n) != 0: continue
        if spin_half_count(n) not in (1, 3): continue
        E = mode_energy(n, L, Gti)
        if abs(E - M_N) < tolerance:
            cands.append(n)
    return cands


def deduplicate_by_nu(cands, Gti):
    """Group candidates that differ only in ν quantum numbers."""
    groups = {}
    for n in cands:
        key = (n[0], n[1], n[4], n[5])  # e and p parts
        E = mode_energy(n, L, Gti)
        if key not in groups:
            groups[key] = {'modes': [], 'E': E,
                          'Q': charge(n), 'sh': spin_half_count(n)}
        groups[key]['modes'].append(n)
    return groups


def main():
    print("=" * 78)
    print("R54 Track 1b: Neutron landscape")
    print("=" * 78)
    print()

    # ── Phase 1: All neutron candidates at σ = 0 ───────────────
    print("Phase 1: All Q=0 spin-½ candidates within 50 MeV of neutron at σ=0")
    print()

    Gt0, Gti0 = build_metric(L, S_E, S_NU, S_P)
    cands_0 = find_neutron_candidates(Gti0, tolerance=50)
    groups_0 = deduplicate_by_nu(cands_0, Gti0)

    print(f"  Raw candidates: {len(cands_0)}")
    print(f"  Distinct (ignoring ν quantum numbers): {len(groups_0)}")
    print()

    print(f"  {'(n1,n2,n5,n6)':>20s}  {'E (MeV)':>10s}  {'ΔE':>8s}  "
          f"{'sh':>3s}  {'sheets':>8s}  {'#ν variants':>11s}")
    print(f"  {'─'*20}  {'─'*10}  {'─'*8}  {'─'*3}  {'─'*8}  {'─'*11}")

    for key in sorted(groups_0.keys(), key=lambda k: abs(groups_0[k]['E'] - M_N)):
        g = groups_0[key]
        n_sample = g['modes'][0]
        sh_label = sheets(n_sample)
        print(f"  {str(key):>20s}  {g['E']:>10.3f}  {g['E']-M_N:>+8.3f}  "
              f"{g['sh']:>3d}  {sh_label:>8s}  {len(g['modes']):>11d}")
    print()

    # ── Phase 2: Track candidates across σ₂₅ sweep ────────────
    print("=" * 78)
    print("Phase 2: How each candidate moves with σ₂₅ (e-ring ↔ p-tube)")
    print("=" * 78)
    print()

    # Get the distinct e+p keys
    keys = sorted(groups_0.keys(), key=lambda k: abs(groups_0[k]['E'] - M_N))[:15]

    sigma_vals = np.linspace(-0.15, 0.15, 31)
    print(f"  {'σ₂₅':>7s}", end='')
    for key in keys[:10]:
        print(f"  {str(key):>14s}", end='')
    print()

    for sv in sigma_vals:
        sigma = {(1, 4): sv}
        Gt, Gti = build_metric(L, S_E, S_NU, S_P, sigma)
        if Gt is None:
            print(f"  {sv:>+7.3f}  {'singular':>14s}")
            continue
        print(f"  {sv:>+7.3f}", end='')
        for key in keys[:10]:
            n1, n2, n5, n6 = key
            n = (n1, n2, 0, 0, n5, n6)
            E = mode_energy(n, L, Gti)
            print(f"  {E:>14.3f}", end='')
        print()
    print()

    # ── Phase 3: Track candidates across σ₂₆ sweep ────────────
    print("=" * 78)
    print("Phase 3: How each candidate moves with σ₂₆ (e-ring ↔ p-ring)")
    print("=" * 78)
    print()

    print(f"  {'σ₂₆':>7s}", end='')
    for key in keys[:10]:
        print(f"  {str(key):>14s}", end='')
    print()

    for sv in sigma_vals:
        sigma = {(1, 5): sv}
        Gt, Gti = build_metric(L, S_E, S_NU, S_P, sigma)
        if Gt is None:
            print(f"  {sv:>+7.3f}  {'singular':>14s}")
            continue
        print(f"  {sv:>+7.3f}", end='')
        for key in keys[:10]:
            n1, n2, n5, n6 = key
            n = (n1, n2, 0, 0, n5, n6)
            E = mode_energy(n, L, Gti)
            print(f"  {E:>14.3f}", end='')
        print()
    print()

    # ── Phase 4: 2D scan (σ₂₅, σ₂₆) — find best neutron ──────
    print("=" * 78)
    print("Phase 4: 2D landscape (σ₂₅, σ₂₆) — best neutron at each point")
    print("=" * 78)
    print()

    grid = np.linspace(-0.15, 0.15, 31)
    best_overall = None

    print(f"  {'σ₂₅':>7s}  {'σ₂₆':>7s}  {'E_proton':>10s}  "
          f"{'E_neutron':>10s}  {'ΔE_n':>8s}  {'ΔE_p':>8s}  "
          f"{'neutron (n1,n2,n5,n6)':>25s}")
    print(f"  {'─'*7}  {'─'*7}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'*8}  {'─'*25}")

    for s25 in grid[::3]:  # coarse first
        for s26 in grid[::3]:
            sigma = {(1, 4): float(s25), (1, 5): float(s26)}
            Gt, Gti = build_metric(L, S_E, S_NU, S_P, sigma)
            if Gt is None:
                continue

            E_p = mode_energy((0, 0, 0, 0, 1, 3), L, Gti)

            # Find best neutron
            best_n = None
            for n in iproduct(*[range(lo, hi+1) for lo, hi in n_ranges]):
                if all(ni == 0 for ni in n): continue
                if charge(n) != 0: continue
                if spin_half_count(n) not in (1, 3): continue
                E = mode_energy(n, L, Gti)
                dE = abs(E - M_N)
                if best_n is None or dE < best_n[0]:
                    best_n = (dE, n, E)

            if best_n:
                n = best_n[1]
                key = (n[0], n[1], n[4], n[5])
                dE_n = best_n[2] - M_N
                dE_p = E_p - M_P
                print(f"  {s25:>+7.3f}  {s26:>+7.3f}  {E_p:>10.3f}  "
                      f"{best_n[2]:>10.3f}  {dE_n:>+8.3f}  {dE_p:>+8.3f}  "
                      f"{str(key):>25s}")

                if best_overall is None or best_n[0] < best_overall['dE']:
                    best_overall = {
                        's25': float(s25), 's26': float(s26),
                        'dE': best_n[0], 'E_n': best_n[2],
                        'n': best_n[1], 'E_p': E_p,
                    }

    print()

    if best_overall:
        print("=" * 78)
        print("Best neutron candidate across all (σ₂₅, σ₂₆)")
        print("=" * 78)
        b = best_overall
        print(f"  σ₂₅ = {b['s25']:+.3f}, σ₂₆ = {b['s26']:+.3f}")
        print(f"  Neutron: {b['n']}  E = {b['E_n']:.3f} MeV  "
              f"(target {M_N}, Δ = {b['E_n']-M_N:+.3f})")
        print(f"  Proton:  (0,0,0,0,1,3)  E = {b['E_p']:.3f} MeV  "
              f"(target {M_P}, Δ = {b['E_p']-M_P:+.3f})")
        print(f"  n-p mass difference: {b['E_n']-b['E_p']:.3f} MeV  "
              f"(observed: {M_N-M_P:.3f})")
        print()

        # At the best point, list ALL candidates within 5 MeV
        sigma = {(1, 4): b['s25'], (1, 5): b['s26']}
        Gt, Gti = build_metric(L, S_E, S_NU, S_P, sigma)
        near = []
        for n in iproduct(*[range(lo, hi+1) for lo, hi in n_ranges]):
            if all(ni == 0 for ni in n): continue
            if charge(n) != 0: continue
            if spin_half_count(n) not in (1, 3): continue
            E = mode_energy(n, L, Gti)
            if abs(E - M_N) < 5:
                near.append((abs(E - M_N), n, E))
        near.sort()

        groups = deduplicate_by_nu(
            [n for _, n, _ in near],
            Gti)

        print(f"  All distinct neutrons within 5 MeV at best (σ₂₅, σ₂₆):")
        print(f"  {'(n1,n2,n5,n6)':>20s}  {'E (MeV)':>10s}  {'ΔE':>8s}  "
              f"{'sheets':>8s}  {'#ν':>4s}")
        print(f"  {'─'*20}  {'─'*10}  {'─'*8}  {'─'*8}  {'─'*4}")
        for key in sorted(groups.keys(), key=lambda k: abs(groups[k]['E'] - M_N)):
            g = groups[key]
            n_sample = g['modes'][0]
            print(f"  {str(key):>20s}  {g['E']:>10.3f}  {g['E']-M_N:>+8.3f}  "
                  f"{sheets(n_sample):>8s}  {len(g['modes']):>4d}")

    print()
    print("Track 1b complete.")


if __name__ == '__main__':
    main()
