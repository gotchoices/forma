"""
R54 Track 2: Nuclear analysis at the R54 geometry

Tests whether stable nuclei (deuteron through ⁵⁶Fe) are matched
at the R53 e-sheet + model-D p-sheet + R54 cross-shears.

Nuclear scaling law (from R29, confirmed in R50 Track 5):
  n₁ = −N (neutron count, negative for Q convention)
  n₅ = A (mass number)
  n₆ = 3A (ring ratio from (1,3) proton)
  Q = −n₁ + n₅ = N + A... wait, Q = -(-N) + A = N + A?

Actually: Q = -n₁ + n₅.  For a nucleus with Z protons, N neutrons:
  n₁ = N (neutron count — e-sheet tube windings from N neutrons)
  n₅ = A (mass number — p-sheet tube windings)
  Q = -N + A = Z  ✓

But at R54 geometry, L_ring_e = 11.88 fm (not 5939 fm).  Each
e-ring winding contributes ~104 MeV.  Nuclear modes have e-ring
windings (n₂) that add substantial energy.  Need to find optimal
n₂ at the new geometry.
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
    if sigma is None: sigma = {}
    S = np.zeros((6, 6)); S[0, 1] = s_e; S[2, 3] = s_nu; S[4, 5] = s_p
    B = np.diag(L) @ (np.eye(6) + S)
    Gt = B.T @ B
    for i in range(6):
        for j in range(6): Gt[i, j] /= (L[i] * L[j])
    for (i, j), val in sigma.items():
        Gt[i, j] += val; Gt[j, i] += val
    eigs = np.linalg.eigvalsh(Gt)
    if np.any(eigs <= 0): return None, None
    return Gt, np.linalg.inv(Gt)


def mode_energy(n, L, Gti):
    na = np.asarray(n, dtype=float); nt = na / L
    E2 = _TWO_PI_HC ** 2 * nt @ Gti @ nt
    return math.sqrt(max(E2, 0))


def charge(n): return int(-n[0] + n[4])


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

# R54 cross-shears
sigma_base = {(3, 4): -0.18, (3, 5): 0.10}

# R29 nuclear benchmarks
NUCLEI = [
    ("d",     2,   1,   1875.613),
    ("³He",   3,   2,   2808.391),
    ("t",     3,   1,   2808.921),
    ("⁴He",   4,   2,   3727.379),
    ("⁶Li",   6,   3,   5601.518),
    ("⁷Li",   7,   3,   6533.833),
    ("⁹Be",   9,   4,   8392.750),
    ("¹²C",  12,   6,  11174.862),
    ("¹⁴N",  14,   7,  13040.203),
    ("¹⁶O",  16,   8,  14895.079),
    ("⁵⁶Fe", 56,  26,  52089.808),
]


def main():
    print("=" * 78)
    print("R54 Track 2: Nuclear analysis")
    print("=" * 78)
    print()
    print(f"  E-sheet: ε={EPS_E:.1f}, s={S_E:.6f}, L_ring={L_ring_e:.4f} fm")
    print(f"  P-sheet: ε={EPS_P:.2f}, s={S_P:.6f}, L_ring={L_ring_p:.4f} fm")
    print(f"  E per e-ring: {_TWO_PI_HC/L_ring_e:.1f} MeV")
    print(f"  E per p-ring: {_TWO_PI_HC/L_ring_p:.1f} MeV")
    print()

    Gt, Gti = build_metric(L, S_E, S_NU, S_P, sigma_base)

    # ── Method 1: R29 scaling law (n₁=N, n₅=A, n₆=3A) ────────
    print("=" * 78)
    print("Method 1: R29 scaling law (n₅=A, n₆=3A, optimize n₂, n₃, n₄)")
    print("=" * 78)
    print()

    print(f"  {'Nucleus':>6s}  {'A':>3s}  {'Z':>3s}  {'Obs (MeV)':>10s}  "
          f"{'Pred (MeV)':>10s}  {'Δm/m':>8s}  {'mode':>35s}  {'Q_check':>8s}")
    print(f"  {'─'*6}  {'─'*3}  {'─'*3}  {'─'*10}  {'─'*10}  {'─'*8}  "
          f"{'─'*35}  {'─'*8}")

    for sym, A, Z, mass in NUCLEI:
        N = A - Z
        n1 = N   # e-tube (neutron count)
        n5 = A   # p-tube (mass number)
        n6 = 3 * A  # p-ring (scaling law)

        # Optimize n₂ (e-ring) and ν quantum numbers
        best = None
        for n2 in range(-30, 31):
            for n3 in range(-2, 3):
                for n4 in range(-2, 3):
                    n = (n1, n2, n3, n4, n5, n6)
                    E = mode_energy(n, L, Gti)
                    dE = abs(E - mass)
                    if best is None or dE < best[0]:
                        best = (dE, n, E)

        dE, n_best, E_best = best
        rel = dE / mass * 100
        Q = charge(n_best)
        Q_ok = '✓' if Q == Z else f'✗ (Q={Q})'
        print(f"  {sym:>6s}  {A:>3d}  {Z:>3d}  {mass:>10.1f}  "
              f"{E_best:>10.1f}  {rel:>7.2f}%  {str(n_best):>35s}  {Q_ok:>8s}")

    print()

    # ── Method 2: Free search (no scaling law assumed) ─────────
    print("=" * 78)
    print("Method 2: Free search — best 6-tuple for each nucleus")
    print("  (no scaling law assumed; search Q=Z modes near target mass)")
    print("=" * 78)
    print()

    # For nuclei up to ⁴He only (search space manageable)
    small_nuclei = [n for n in NUCLEI if n[1] <= 4]

    for sym, A, Z, mass in small_nuclei:
        best = None
        # Wider search for small nuclei
        ranges = [(-5, 5), (-15, 15), (-3, 3), (-3, 3), (-1, max(A+1, 5)), (-3, max(3*A+3, 15))]
        for n in iproduct(*[range(lo, hi + 1) for lo, hi in ranges]):
            if all(ni == 0 for ni in n): continue
            if charge(n) != Z: continue
            E = mode_energy(n, L, Gti)
            dE = abs(E - mass)
            if dE > mass * 0.05: continue  # within 5%
            if best is None or dE < best[0]:
                best = (dE, n, E)

        if best:
            dE, n_best, E_best = best
            rel = dE / mass * 100
            print(f"  {sym}: best = {n_best}  E = {E_best:.1f} MeV  "
                  f"Δm/m = {rel:.3f}%  Q = {charge(n_best)}")
        else:
            print(f"  {sym}: no mode within 5% found")

    print()

    # ── Comparison with model-D ────────────────────────────────
    print("=" * 78)
    print("For reference: model-D nuclear results (R50 Track 5)")
    print("=" * 78)
    print()
    print("  Model-D at σ_ep=−0.13: d 0.05%, ⁴He 0.69%, ¹²C 0.76%, ⁵⁶Fe 0.87%")
    print()

    print("Track 2 complete.")


if __name__ == '__main__':
    main()
