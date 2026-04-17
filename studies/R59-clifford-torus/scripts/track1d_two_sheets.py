"""
R59 Track 1d: Two sheets (electron + proton) — universality test.

Add the proton sheet to the Track 1c minimal system.
Test both coupling approaches on the 2-sheet system:
  D1: direct ring-t (one σ per sheet)
  D2: ℵ-mediated (ring-ℵ per sheet, shared ℵ-t)

The universality question: does a SINGLE coupling parameter
give α for BOTH electron and proton?

Metric structure:
  D1: 4 Ma + 3 S + 1 t = 8D
    Indices: 0 e-tube, 1 e-ring, 2 p-tube, 3 p-ring, 4-6 S, 7 t
  D2: 4 Ma + 1 ℵ + 3 S + 1 t = 9D
    Indices: 0 e-tube, 1 e-ring, 2 p-tube, 3 p-ring, 4 ℵ, 5-7 S, 8 t
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from lib.ma_model_d import M_E_MEV, M_P_MEV, _TWO_PI_HC, solve_shear_for_alpha

ALPHA = 1.0 / 137.036
TWO_PI_HC = _TWO_PI_HC
INV_2PI = 1.0 / (2 * math.pi)


def sheet_metric(eps, s):
    return np.array([
        [1.0,       s * eps],
        [s * eps,   1.0 + s**2 * eps**2]
    ])


def sheet_L(eps, s, n_tube, n_ring, mass_MeV):
    mu = math.sqrt((n_tube/eps)**2 + (n_ring - n_tube*s)**2)
    L_ring = TWO_PI_HC * mu / mass_MeV
    L_tube = eps * L_ring
    return L_tube, L_ring


def build_D1(A_e, A_p, L_e, L_p, sigma_e_t, sigma_p_t):
    """
    D1: 8D = 2 Ma_e + 2 Ma_p + 3 S + 1 t (no ℵ)
    Indices: 0 e-tube, 1 e-ring, 2 p-tube, 3 p-ring, 4-6 S, 7 t
    """
    G = np.zeros((8, 8))

    # Ma blocks
    G[0:2, 0:2] = A_e
    G[2:4, 2:4] = A_p

    # S
    G[4, 4] = 1.0; G[5, 5] = 1.0; G[6, 6] = 1.0

    # t (Lorentzian)
    G[7, 7] = -1.0

    # Ma-t (ring only — tube entries stay zero)
    G[1, 7] = sigma_e_t;  G[7, 1] = sigma_e_t   # e-ring-t
    G[3, 7] = sigma_p_t;  G[7, 3] = sigma_p_t   # p-ring-t

    return G


def build_D2(A_e, A_p, L_e, L_p, sigma_e_aleph, sigma_p_aleph, sigma_aleph_t):
    """
    D2: 9D = 2 Ma_e + 2 Ma_p + 1 ℵ + 3 S + 1 t
    Indices: 0 e-tube, 1 e-ring, 2 p-tube, 3 p-ring, 4 ℵ, 5-7 S, 8 t
    """
    G = np.zeros((9, 9))

    # Ma blocks
    G[0:2, 0:2] = A_e
    G[2:4, 2:4] = A_p

    # ℵ
    G[4, 4] = 1.0

    # S
    G[5, 5] = 1.0; G[6, 6] = 1.0; G[7, 7] = 1.0

    # t
    G[8, 8] = -1.0

    # Ma-ℵ (ring only)
    G[1, 4] = sigma_e_aleph;  G[4, 1] = sigma_e_aleph   # e-ring-ℵ
    G[3, 4] = sigma_p_aleph;  G[4, 3] = sigma_p_aleph   # p-ring-ℵ

    # ℵ-t
    G[4, 8] = sigma_aleph_t;  G[8, 4] = sigma_aleph_t

    return G


def mass_shell(G, idx_t, L_all, n_all):
    """
    Solve mass-shell on the full metric.
    n_all has nonzero entries only for Ma dimensions.
    Returns (E_low, E_high).
    """
    try:
        Gi = np.linalg.inv(G)
    except:
        return np.nan, np.nan

    N = len(G)
    nt = np.zeros(N)
    for i, (n, L) in enumerate(zip(n_all, L_all)):
        if L > 0:
            nt[i] = n / L

    a = Gi[idx_t, idx_t]
    b = 2.0 * np.dot(Gi[:, idx_t], nt)
    c = nt @ Gi @ nt

    disc = b**2 - 4*a*c
    if disc < 0:
        return np.nan, np.nan

    w1 = (-b + math.sqrt(disc)) / (2*a)
    w2 = (-b - math.sqrt(disc)) / (2*a)
    E1 = TWO_PI_HC * abs(w1)
    E2 = TWO_PI_HC * abs(w2)

    return min(E1, E2), max(E1, E2)


def main():
    print("=" * 75)
    print("R59 Track 1d: Two sheets (e + p) — universality test")
    print("=" * 75)
    print()

    # ── Sheet parameters ───────────────────────────────────
    eps_e = 397.074;  s_e = 2.004200
    eps_p = 0.55;     s_p = solve_shear_for_alpha(0.55, n_tube=1, n_ring=3)

    A_e = sheet_metric(eps_e, s_e)
    A_p = sheet_metric(eps_p, s_p)

    Le_tube, Le_ring = sheet_L(eps_e, s_e, 1, 2, M_E_MEV)
    Lp_tube, Lp_ring = sheet_L(eps_p, s_p, 1, 3, M_P_MEV)

    print(f"  Electron: ε={eps_e}, s={s_e:.6f}")
    print(f"    L_tube={Le_tube:.2f} fm, L_ring={Le_ring:.4f} fm")
    print(f"  Proton: ε={eps_p}, s={s_p:.6f}")
    print(f"    L_tube={Lp_tube:.4f} fm, L_ring={Lp_ring:.4f} fm")
    print()

    # L vectors for the two approaches
    # D1: [e-tube, e-ring, p-tube, p-ring, Sx, Sy, Sz, t]
    L_D1 = np.array([Le_tube, Le_ring, Lp_tube, Lp_ring, 1, 1, 1, 1])
    # D2: [e-tube, e-ring, p-tube, p-ring, ℵ, Sx, Sy, Sz, t]
    L_D2 = np.array([Le_tube, Le_ring, Lp_tube, Lp_ring, 1, 1, 1, 1, 1])

    electron = [1, 2, 0, 0]  # n for e-tube, e-ring, p-tube, p-ring
    proton   = [0, 0, 1, 3]

    # Bare energies
    def bare_E(n_Ma, L_Ma, A_sheet):
        nt = np.array(n_Ma, dtype=float) / np.array(L_Ma)
        E2 = TWO_PI_HC**2 * nt @ np.linalg.inv(A_sheet) @ nt
        return math.sqrt(max(E2, 0))

    E_e0 = bare_E([1, 2], [Le_tube, Le_ring], A_e)
    E_p0 = bare_E([1, 3], [Lp_tube, Lp_ring], A_p)
    print(f"  Bare electron: {E_e0:.4f} MeV")
    print(f"  Bare proton:   {E_p0:.2f} MeV")
    print()

    # ── D1: Direct ring-t (one σ for both sheets) ─────────
    print("─" * 75)
    print("D1: Direct ring-t coupling (no ℵ)")
    print("  Same σ for e-ring-t and p-ring-t (opposite signs)")
    print("─" * 75)
    print()

    print(f"  {'σ':>8s}  {'E_e':>8s}  {'E_p':>8s}  {'αe':>10s}  {'αp':>10s}  "
          f"{'αe/α':>8s}  {'αp/α':>8s}  {'gap%':>6s}  {'dir_e':>5s}  {'dir_p':>5s}")
    print(f"  {'─'*8}  {'─'*8}  {'─'*8}  {'─'*10}  {'─'*10}  "
          f"{'─'*8}  {'─'*8}  {'─'*6}  {'─'*5}  {'─'*5}")

    for sigma in [0.001, 0.005, 0.008, 0.009, 0.01, 0.02, 0.05]:
        G = build_D1(A_e, A_p, L_D1[:2], L_D1[2:4],
                     sigma_e_t=-sigma, sigma_p_t=+sigma)

        eigs = np.linalg.eigvalsh(G)
        if np.sum(eigs < 0) != 1:
            print(f"  {sigma:8.4f}  invalid sig ({np.sum(eigs<0)} neg)")
            continue

        # Electron: n = [1,2,0,0, 0,0,0, ω]
        n_e_full = [1, 2, 0, 0, 0, 0, 0, 0]  # 8D, last is ω placeholder
        n_p_full = [0, 0, 1, 3, 0, 0, 0, 0]

        Ee_lo, Ee_hi = mass_shell(G, 7, L_D1, n_e_full[:4] + [0]*4)
        Ep_lo, Ep_hi = mass_shell(G, 7, L_D1, n_p_full[:4] + [0]*4)

        ae = abs(Ee_lo - E_e0) / E_e0
        ap = abs(Ep_lo - E_p0) / E_p0
        gap = abs(ae - ap) / max(ae, 1e-30) * 100

        de = "UP" if Ee_lo > E_e0 else "DOWN"
        dp = "UP" if Ep_lo > E_p0 else "DOWN"

        print(f"  {sigma:8.4f}  {Ee_lo:8.4f}  {Ep_lo:8.2f}  {ae:10.6f}  {ap:10.6f}  "
              f"{ae/ALPHA:8.4f}  {ap/ALPHA:8.4f}  {gap:6.2f}  {de:>5s}  {dp:>5s}")

    print()

    # Fine-tune D1 for electron
    lo, hi = 0.001, 0.05
    for _ in range(200):
        mid = (lo+hi)/2
        G = build_D1(A_e, A_p, L_D1[:2], L_D1[2:4], -mid, +mid)
        eigs = np.linalg.eigvalsh(G)
        if np.sum(eigs<0) != 1: hi=mid; continue
        Ee, _ = mass_shell(G, 7, L_D1, [1,2,0,0,0,0,0,0])
        if np.isnan(Ee): hi=mid; continue
        if abs(Ee-E_e0)/E_e0 < ALPHA: lo=mid
        else: hi=mid

    opt_D1 = (lo+hi)/2
    G_D1 = build_D1(A_e, A_p, L_D1[:2], L_D1[2:4], -opt_D1, +opt_D1)
    Ee, _ = mass_shell(G_D1, 7, L_D1, [1,2,0,0,0,0,0,0])
    Ep, _ = mass_shell(G_D1, 7, L_D1, [0,0,1,3,0,0,0,0])
    ae_D1 = abs(Ee-E_e0)/E_e0
    ap_D1 = abs(Ep-E_p0)/E_p0
    gap_D1 = abs(ae_D1-ap_D1)/ae_D1*100

    print(f"  D1 fine-tuned: σ = {opt_D1:.8f}")
    print(f"    α_eff(e) = {ae_D1:.8e} ({ae_D1/ALPHA:.4f}α)")
    print(f"    α_eff(p) = {ap_D1:.8e} ({ap_D1/ALPHA:.4f}α)")
    print(f"    Gap: {gap_D1:.2f}%")
    print(f"    Direction: e={'UP' if Ee>E_e0 else 'DOWN'}, p={'UP' if Ep>E_p0 else 'DOWN'}")
    print()

    # ── D2: ℵ-mediated (shared ℵ-t, per-sheet ring-ℵ) ────
    print("─" * 75)
    print("D2: ℵ-mediated (ring-ℵ per sheet, shared ℵ-t)")
    print(f"  e-ring-ℵ = {-INV_2PI:+.6f}, p-ring-ℵ = {+INV_2PI:+.6f}")
    print("─" * 75)
    print()

    print(f"  {'σ_ℵt':>8s}  {'E_e':>8s}  {'E_p':>8s}  {'αe':>10s}  {'αp':>10s}  "
          f"{'αe/α':>8s}  {'αp/α':>8s}  {'gap%':>6s}  {'dir_e':>5s}  {'dir_p':>5s}")
    print(f"  {'─'*8}  {'─'*8}  {'─'*8}  {'─'*10}  {'─'*10}  "
          f"{'─'*8}  {'─'*8}  {'─'*6}  {'─'*5}  {'─'*5}")

    for sat in [0.01, 0.05, 0.1, 0.2, 0.26, 0.3, 0.5, 1.0]:
        G = build_D2(A_e, A_p, L_D2[:2], L_D2[2:4],
                     -INV_2PI, +INV_2PI, sat)

        eigs = np.linalg.eigvalsh(G)
        if np.sum(eigs < 0) != 1:
            print(f"  {sat:8.4f}  invalid sig ({np.sum(eigs<0)} neg)")
            continue

        Ee_lo, _ = mass_shell(G, 8, L_D2, [1,2,0,0,0,0,0,0,0])
        Ep_lo, _ = mass_shell(G, 8, L_D2, [0,0,1,3,0,0,0,0,0])

        if np.isnan(Ee_lo) or np.isnan(Ep_lo):
            print(f"  {sat:8.4f}  NaN")
            continue

        ae = abs(Ee_lo - E_e0) / E_e0
        ap = abs(Ep_lo - E_p0) / E_p0
        gap = abs(ae - ap) / max(ae, 1e-30) * 100

        de = "UP" if Ee_lo > E_e0 else "DOWN"
        dp = "UP" if Ep_lo > E_p0 else "DOWN"

        print(f"  {sat:8.4f}  {Ee_lo:8.4f}  {Ep_lo:8.2f}  {ae:10.6f}  {ap:10.6f}  "
              f"{ae/ALPHA:8.4f}  {ap/ALPHA:8.4f}  {gap:6.2f}  {de:>5s}  {dp:>5s}")

    print()

    # Fine-tune D2 for electron
    lo, hi = 0.01, 2.0
    for _ in range(200):
        mid = (lo+hi)/2
        G = build_D2(A_e, A_p, L_D2[:2], L_D2[2:4],
                     -INV_2PI, +INV_2PI, mid)
        eigs = np.linalg.eigvalsh(G)
        if np.sum(eigs<0) != 1: hi=mid; continue
        Ee, _ = mass_shell(G, 8, L_D2, [1,2,0,0,0,0,0,0,0])
        if np.isnan(Ee): hi=mid; continue
        if abs(Ee-E_e0)/E_e0 < ALPHA: lo=mid
        else: hi=mid

    opt_D2 = (lo+hi)/2
    G_D2 = build_D2(A_e, A_p, L_D2[:2], L_D2[2:4],
                     -INV_2PI, +INV_2PI, opt_D2)
    Ee, _ = mass_shell(G_D2, 8, L_D2, [1,2,0,0,0,0,0,0,0])
    Ep, _ = mass_shell(G_D2, 8, L_D2, [0,0,1,3,0,0,0,0,0])
    ae_D2 = abs(Ee-E_e0)/E_e0
    ap_D2 = abs(Ep-E_p0)/E_p0
    gap_D2 = abs(ae_D2-ap_D2)/ae_D2*100

    print(f"  D2 fine-tuned: σ_ℵt = {opt_D2:.8f}")
    print(f"    α_eff(e) = {ae_D2:.8e} ({ae_D2/ALPHA:.4f}α)")
    print(f"    α_eff(p) = {ap_D2:.8e} ({ap_D2/ALPHA:.4f}α)")
    print(f"    Gap: {gap_D2:.2f}%")
    print(f"    Direction: e={'UP' if Ee>E_e0 else 'DOWN'}, p={'UP' if Ep>E_p0 else 'DOWN'}")
    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 75)
    print("SUMMARY: Two-sheet universality test")
    print("=" * 75)
    print()
    print(f"  {'Approach':>15s}  {'σ':>10s}  {'αe/α':>8s}  {'αp/α':>8s}  "
          f"{'gap':>6s}  {'mass dir':>10s}")
    print(f"  {'─'*15}  {'─'*10}  {'─'*8}  {'─'*8}  {'─'*6}  {'─'*10}")
    print(f"  {'D1 (direct)':>15s}  {opt_D1:10.6f}  {ae_D1/ALPHA:8.4f}  {ap_D1/ALPHA:8.4f}  "
          f"{gap_D1:5.2f}%  {'DOWN/DOWN' if Ee<E_e0 else 'UP/UP'}")
    print(f"  {'D2 (ℵ-med)':>15s}  {opt_D2:10.6f}  {ae_D2/ALPHA:8.4f}  {ap_D2/ALPHA:8.4f}  "
          f"{gap_D2:5.2f}%  {'UP/UP'}")
    print()
    print(f"  R55 (spatial ℵ): gap was 3.6%")
    print(f"  Track 1 (full model-E): gap was 1.83% (direct) / 5.24% (ℵ)")
    print()
    print(f"  α = {ALPHA:.6e}")
    print()
    print("Track 1d complete.")


if __name__ == '__main__':
    main()
