#!/usr/bin/env python3
"""
R45 Track 1: Proton magnetic moment from geodesic tilting.

Computes the g-factor of the proton by:
1. Building the 6D Ma metric with cross-shear σ_ep
2. Computing the geodesic velocity of the (0,0,0,0,1,2) mode
3. Decomposing velocity into Ma_e and Ma_p ring components
4. Computing the magnetic moment from the current loop on each sheet
5. Extracting g_p = 2μ/μ_N

The magnetic dipole moment comes from charge circulating around
RING directions (indices 1, 3, 5 — Ma_e ring, Ma_ν ring, Ma_p ring).
Tube circulation creates toroidal fields with zero net dipole moment.

Convention:
  μ_N = eℏ/(2m_p)        — nuclear magneton
  g_p = 2μ/μ_N           — proton g-factor
  Measured: g_p = 5.5857, μ_p = 2.7928 μ_N
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from lib.ma import (build_scaled_metric, mode_energy,
                    hbar_c_MeV_fm, M_P_MEV, M_E_MEV)


# ── Parameters (all pinned by R27 F18, except r_e and r_nu) ────

R_P = 8.906
SIGMA_EP = -0.09064
R_E_DEFAULT = 6.6
R_NU = 5.0

PROTON = np.array([0, 0, 0, 0, 1, 2], dtype=float)
NEUTRON = np.array([0, -2, 1, 0, 0, 2], dtype=float)

G_P_MEAS = 5.5857
MU_P_MEAS = 2.7928


# ── Core computation ────────────────────────────────────────────

def geodesic_velocity(n, Gti, L):
    """v_i = Σ_j G̃⁻¹_ij (n_j / L_j)"""
    return Gti @ (n / L)


def compute_moment(n, Gti, L):
    """
    Magnetic moment in units of μ_N from the current-loop formula.

    μ = (e/2) × c × Σ_rings (f_ring_i × R_ring_i)
    μ/μ_N = (m_p c/ℏ) × Σ_rings (f_ring_i × R_ring_i)
          = (M_P / hbar_c) × Σ (f_ring_i × L_ring_i / (2π))

    Ring directions: index 1 (Ma_e), 3 (Ma_ν), 5 (Ma_p).
    f_ring_i = u_i / |u| where u_i = v_i × L_i (physical velocity).
    """
    v = geodesic_velocity(n, Gti, L)
    u = v * L
    u_mag = np.sqrt(np.sum(u**2))

    ring_idx = [1, 3, 5]
    ring_names = ['Ma_e', 'Ma_ν', 'Ma_p']

    f_ring = np.array([u[i] / u_mag for i in ring_idx])
    R_ring = np.array([L[i] / (2 * np.pi) for i in ring_idx])

    mu_contributions = (M_P_MEV / hbar_c_MeV_fm) * f_ring * R_ring
    mu_total = np.sum(mu_contributions)
    g = 2 * mu_total

    sheet_frac = {}
    for sheet, (i0, i1) in [('Ma_e', (0, 1)), ('Ma_ν', (2, 3)), ('Ma_p', (4, 5))]:
        sheet_frac[sheet] = (u[i0]**2 + u[i1]**2) / u_mag**2

    return {
        'g': g,
        'mu_over_muN': mu_total,
        'f_ring': dict(zip(ring_names, f_ring)),
        'mu_ring': dict(zip(ring_names, mu_contributions)),
        'R_ring_fm': dict(zip(ring_names, R_ring)),
        'sheet_velocity_frac': sheet_frac,
        'u': u,
        'u_mag': u_mag,
    }


# ── Main ────────────────────────────────────────────────────────

def main():
    sep = '=' * 62

    # Build metrics
    Gt, Gti, L, sc = build_scaled_metric(
        R_E_DEFAULT, R_NU, R_P, sigma_ep=SIGMA_EP)
    Gt0, Gti0, L0, sc0 = build_scaled_metric(
        R_E_DEFAULT, R_NU, R_P, sigma_ep=0.0)

    print(sep)
    print("R45 TRACK 1: PROTON MOMENT FROM GEODESIC TILTING")
    print(sep)

    print(f"\nParameters:")
    print(f"  r_p = {R_P}  (pinned, R27 F18)")
    print(f"  σ_ep = {SIGMA_EP}  (pinned, R27 F18)")
    print(f"  r_e = {R_E_DEFAULT}  (free)")
    print(f"  r_ν = {R_NU}  (free)")
    print(f"  s₁₂ = {sc['s12']:.6f}")
    print(f"  s₅₆ = {sc['s56']:.6f}")

    print(f"\nCircumferences and radii:")
    names = ['L₁ e-tube', 'L₂ e-ring', 'L₃ ν-tube', 'L₄ ν-ring',
             'L₅ p-tube', 'L₆ p-ring']
    for i, nm in enumerate(names):
        R = L[i] / (2 * np.pi)
        print(f"  {nm}: L = {L[i]:.4e} fm,  R = {R:.4e} fm")

    # Verify mode energies
    E_p = mode_energy(PROTON, Gti, L)
    E_p0 = mode_energy(PROTON, Gti0, L0)
    print(f"\nProton energy:  {E_p:.4f} MeV (σ_ep={SIGMA_EP})")
    print(f"                {E_p0:.4f} MeV (σ_ep=0)")

    # ── Baseline (no cross-shear) ──────────────────────────────

    print(f"\n{sep}")
    print("BASELINE: σ_ep = 0  (no cross-sheet coupling)")
    print(sep)

    res0 = compute_moment(PROTON, Gti0, L0)
    print(f"\n  Ring velocity fractions:")
    for sheet, f in res0['f_ring'].items():
        print(f"    {sheet}: {f:+.8e}")
    print(f"\n  Ring moment contributions (μ/μ_N):")
    for sheet, m in res0['mu_ring'].items():
        print(f"    {sheet}: {m:+.8f}")
    print(f"\n  Total μ/μ_N = {res0['mu_over_muN']:.8f}")
    print(f"  g_p = {res0['g']:.8f}")
    print(f"\n  (Expected: g ≈ 4 from the (1,2) current loop on Ma_p)")

    # ── With cross-shear ───────────────────────────────────────

    print(f"\n{sep}")
    print(f"WITH CROSS-SHEAR: σ_ep = {SIGMA_EP}")
    print(sep)

    res = compute_moment(PROTON, Gti, L)

    print(f"\n  Velocity² fractions by sheet:")
    for sheet, f in res['sheet_velocity_frac'].items():
        print(f"    {sheet}: {f:.8e}  ({f*100:.6f}%)")

    print(f"\n  Ring velocity fractions (signed):")
    for sheet, f in res['f_ring'].items():
        print(f"    {sheet}: {f:+.8e}")

    print(f"\n  Ring radii:")
    for sheet, r in res['R_ring_fm'].items():
        print(f"    {sheet}: {r:.4e} fm")

    print(f"\n  Moment contributions (μ/μ_N):")
    for sheet, m in res['mu_ring'].items():
        print(f"    {sheet}: {m:+.8f}")

    print(f"\n  ────────────────────────────────────")
    print(f"  Total μ/μ_N = {res['mu_over_muN']:.8f}")
    print(f"  g_p         = {res['g']:.8f}")
    print(f"  ────────────────────────────────────")
    print(f"  Measured μ/μ_N = {MU_P_MEAS}")
    print(f"  Measured g_p   = {G_P_MEAS}")
    print(f"  ────────────────────────────────────")

    delta_g = res['g'] - res0['g']
    print(f"\n  Cross-shear effect:")
    print(f"    Δg = {delta_g:+.8f}")
    print(f"    Δg/g_baseline = {delta_g/res0['g']:+.6e}")

    # ── Sensitivity to r_e ─────────────────────────────────────

    print(f"\n{sep}")
    print("SENSITIVITY TO r_e (free parameter)")
    print(sep)
    print(f"\n  {'r_e':>6s}  {'g_p':>12s}  {'f_ring(Ma_e)':>14s}  "
          f"{'R_e ring (fm)':>14s}  {'μ_e/μ_N':>12s}")
    print(f"  {'─'*6}  {'─'*12}  {'─'*14}  {'─'*14}  {'─'*12}")

    for r_e_test in [0.5, 1.0, 2.0, 3.0, 5.0, 6.6, 8.0, 10.0, 15.0, 50.0]:
        try:
            Gt_t, Gti_t, L_t, _ = build_scaled_metric(
                r_e=r_e_test, r_nu=R_NU, r_p=R_P, sigma_ep=SIGMA_EP)
            res_t = compute_moment(PROTON, Gti_t, L_t)
            print(f"  {r_e_test:6.1f}  {res_t['g']:12.6f}  "
                  f"{res_t['f_ring']['Ma_e']:+14.8e}  "
                  f"{res_t['R_ring_fm']['Ma_e']:14.4e}  "
                  f"{res_t['mu_ring']['Ma_e']:+12.8f}")
        except Exception as e:
            print(f"  {r_e_test:6.1f}  FAILED: {e}")

    # ── Geodesic velocity decomposition ────────────────────────

    print(f"\n{sep}")
    print("FULL VELOCITY DECOMPOSITION (r_e = {})".format(R_E_DEFAULT))
    print(sep)

    v = geodesic_velocity(PROTON, Gti, L)
    u = v * L
    u_mag = np.sqrt(np.sum(u**2))

    dim_names = ['θ₁ e-tube', 'θ₂ e-ring',
                 'θ₃ ν-tube', 'θ₄ ν-ring',
                 'θ₅ p-tube', 'θ₆ p-ring']
    print(f"\n  {'Direction':>12s}  {'v (scaled)':>14s}  "
          f"{'u = v×L':>14s}  {'u/|u|':>14s}")
    print(f"  {'─'*12}  {'─'*14}  {'─'*14}  {'─'*14}")
    for i, nm in enumerate(dim_names):
        print(f"  {nm:>12s}  {v[i]:+14.6e}  "
              f"{u[i]:+14.6e}  {u[i]/u_mag:+14.8e}")

    # ── Inverse metric structure ───────────────────────────────

    print(f"\n{sep}")
    print("INVERSE METRIC G̃⁻¹ (showing Ma_e–Ma_p coupling)")
    print(sep)

    print("\n  Full G̃⁻¹:")
    for i in range(6):
        row = '  '.join(f'{Gti[i,j]:+8.5f}' for j in range(6))
        print(f"  [{row}]")

    print("\n  Ma_e–Ma_p off-diagonal block (rows 0-1, cols 4-5):")
    for i in range(2):
        for j in range(4, 6):
            print(f"    G̃⁻¹[{i},{j}] = {Gti[i,j]:+.6e}")

    # ── Neutron preview ────────────────────────────────────────

    print(f"\n{sep}")
    print("NEUTRON MOMENT (preview — Track 2)")
    print(sep)

    E_n = mode_energy(NEUTRON, Gti, L)
    print(f"\n  Mode: {tuple(NEUTRON.astype(int))}")
    print(f"  Energy: {E_n:.4f} MeV")
    print(f"  Charge: Q = -n₁ + n₅ = 0 + 0 = 0")

    res_n = compute_moment(NEUTRON, Gti, L)
    print(f"\n  Velocity² fractions:")
    for sheet, f in res_n['sheet_velocity_frac'].items():
        print(f"    {sheet}: {f:.6e}")

    print(f"\n  Ring velocity fractions:")
    for sheet, f in res_n['f_ring'].items():
        print(f"    {sheet}: {f:+.8e}")

    print(f"\n  Naive moment (treating as charge +1):")
    print(f"    μ/μ_N = {res_n['mu_over_muN']:.6f}")
    print(f"    g = {res_n['g']:.6f}")
    print(f"\n  *** WARNING: The neutron is charge-neutral. The naive ***")
    print(f"  *** current-loop formula assumes charge +e everywhere. ***")
    print(f"  *** The actual neutron moment requires decomposing the ***")
    print(f"  *** currents by sheet charge: Ma_e carries q=-n₁ and  ***")
    print(f"  *** Ma_p carries q=+n₅.  Full Track 2 needed.         ***")

    # ── Summary ────────────────────────────────────────────────

    print(f"\n{sep}")
    print("SUMMARY")
    print(sep)
    print(f"\n  Baseline g_p (σ_ep=0, torus current loop): {res0['g']:.4f}")
    print(f"  g_p with σ_ep = {SIGMA_EP}:                  {res['g']:.4f}")
    print(f"  Measured g_p:                               {G_P_MEAS}")
    print(f"  Discrepancy from measured:                  "
          f"{(res['g'] - G_P_MEAS)/G_P_MEAS*100:+.2f}%")
    print(f"\n  Cross-shear effect on g:")
    print(f"    Δg = {delta_g:+.6f}")
    print(f"    Direction: {'increase' if delta_g > 0 else 'decrease'}")
    frac_e = res['sheet_velocity_frac']['Ma_e']
    print(f"\n  Velocity fraction leaked to Ma_e: {frac_e:.6e} ({frac_e*100:.4f}%)")
    print(f"  Radius amplification R_e/R_p: "
          f"{res['R_ring_fm']['Ma_e'] / res['R_ring_fm']['Ma_p']:.1f}×")


if __name__ == '__main__':
    main()
