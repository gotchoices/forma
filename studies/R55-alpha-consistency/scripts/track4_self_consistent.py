"""
R55 Track 4: Self-consistent sheet parameters with ℵ coupling.

Instead of:  internal shears → particle spectrum → bolt on Ma-S
Do:          ℵ coupling fixed → find internal shears → check spectrum

For each sheet:
  1. Fix Ma-ℵ = ±1/(2π) on ring dim, σℵS = 0.290
  2. Search for (ε, s) that gives the reference mass on the
     effective 9×9 metric (after integrating out ℵ)
  3. Compare to model-E parameters

Then:
  4. With new sheet params, re-derive cross-sheet shears
  5. Run full particle inventory
  6. Compare to model-E results

Goal: a self-consistent 10×10 metric where the ℵ coupling
is built in from the start, not bolted on afterward.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from lib.ma_model_d import (
    M_E_MEV, M_P_MEV, DM2_21, ALPHA as ALPHA_CONST,
    _TWO_PI_HC, solve_shear_for_alpha,
)

ALPHA = 1.0 / 137.036
SQRT_ALPHA = np.sqrt(ALPHA)
TWO_PI = 2 * np.pi
INV_2PI = 1.0 / TWO_PI
TWO_PI_HC = _TWO_PI_HC

# ℵ parameters (fixed)
SIGMA_ALEPH_S = 0.29019  # from Track 3b


def mu_mode(nt, nr, eps, s):
    """Dimensionless single-sheet mode energy."""
    return math.sqrt((nt / eps)**2 + (nr - nt * s)**2)


def build_sheet_metric(eps, s):
    """Build the 2×2 dimensionless metric for one sheet."""
    # From the metric construction: B = diag(L) @ (I + S)
    # G̃ = Bᵀ B / (L_i × L_j)
    # For a single sheet with tube dim 0, ring dim 1:
    #   L_tube = eps * L_ring
    #   S[0,1] = s (shear from tube to ring)
    # B = [[L_tube, 0], [s*L_tube, L_ring]]
    #   = [[eps*L, 0], [s*eps*L, L]]
    # Bᵀ B = [[eps²L², s*eps²*L²], [s*eps²*L², (1+s²*eps²... wait
    # Let me just compute directly.
    # G̃[0,0] = (B[0,0]² + B[1,0]²) / (L_tube²)
    #         = (eps²L² + s²*eps²*L²) / (eps²L²)
    #         = 1 + s²  ... no that's wrong
    # Actually the metric code does:
    # S = [[0, s], [0, 0]]  (upper triangular shear)
    # B = diag(L) @ (I + S) = [[L_tube, s*L_tube], [0, L_ring]]
    # Wait no: S[0,1] = s means tube→ring shear
    # B = diag([L_tube, L_ring]) @ ([[1,s],[0,1]])
    #   = [[L_tube, s*L_tube], [0, L_ring]]
    # G̃_raw = Bᵀ @ B = [[L_tube², s*L_tube²], [s*L_tube², s²*L_tube² + L_ring²]]
    # G̃[i,j] = G̃_raw[i,j] / (L[i] * L[j])
    # G̃[0,0] = L_tube² / (L_tube * L_tube) = 1
    # G̃[0,1] = s*L_tube² / (L_tube * L_ring) = s * L_tube/L_ring = s * eps
    # G̃[1,1] = (s²*L_tube² + L_ring²) / (L_ring * L_ring) = s²*eps² + 1
    # Wait, s*eps is the off-diagonal? Let me check with actual values.
    # For e-sheet: s=2.004, eps=397. G̃[0,1] should be 795.8
    # s * eps = 2.004 * 397 = 795.6 ≈ 795.8 ✓
    # G̃[1,1] = s²*eps² + 1 = 2.004² * 397² + 1 = 633,395 ...
    # actual is 633,324. Close but not exact due to how shear enters.

    # Actually let me just use the actual formula from the code:
    # The build uses S[0,1] = s, then B = diag(L) @ (I + S)
    # So B[0,0] = L[0], B[0,1] = s * L[0], B[1,0] = 0, B[1,1] = L[1]
    # G̃ = Bᵀ B / (Li Lj) + sigma_corrections
    # G̃[0,0] = (B[0,0]² + B[1,0]²) / L[0]² = L[0]²/L[0]² = 1
    # G̃[0,1] = (B[0,0]*B[0,1] + B[1,0]*B[1,1]) / (L[0]*L[1])
    #         = (L[0] * s*L[0]) / (L[0]*L[1]) = s * L[0]/L[1] = s * eps
    # G̃[1,1] = (B[0,1]² + B[1,1]²) / L[1]²
    #         = (s²*L[0]² + L[1]²) / L[1]² = s²*eps² + 1

    A = np.array([
        [1.0,           s * eps],
        [s * eps,       1.0 + s**2 * eps**2]
    ])
    return A


def build_10x10_from_sheets(eps_e, s_e, eps_nu, s_nu, eps_p, s_p,
                              cross_shears=None):
    """
    Build the full 10×10 metric from sheet parameters and ℵ coupling.

    Returns (G10, L_6) where L_6 is the circumference vector.
    """
    # Derive L_ring for each sheet from reference masses
    # Electron: mode (1,2), mass = M_E_MEV
    mu_e = mu_mode(1, 2, eps_e, s_e)
    L_ring_e = TWO_PI_HC * mu_e / M_E_MEV

    # Proton: mode (1,3), mass = M_P_MEV
    mu_p = mu_mode(1, 3, eps_p, s_p)
    L_ring_p = TWO_PI_HC * mu_p / M_P_MEV

    # Neutrino: mode (1,1), from Δm²₂₁
    E0_nu = math.sqrt(DM2_21 / (4 * s_nu)) * 1e-6
    L_ring_nu = TWO_PI_HC / E0_nu

    L_6 = np.array([
        eps_e * L_ring_e, L_ring_e,
        eps_nu * L_ring_nu, L_ring_nu,
        eps_p * L_ring_p, L_ring_p,
    ])

    # Build 6×6 Ma metric
    A_e = build_sheet_metric(eps_e, s_e)
    A_nu = build_sheet_metric(eps_nu, s_nu)
    A_p = build_sheet_metric(eps_p, s_p)

    A_6 = np.zeros((6, 6))
    A_6[0:2, 0:2] = A_e
    A_6[2:4, 2:4] = A_nu
    A_6[4:6, 4:6] = A_p

    # Cross-sheet shears
    if cross_shears:
        for (i, j), val in cross_shears.items():
            A_6[i, j] += val
            A_6[j, i] += val

    # Build 10×10
    G10 = np.zeros((10, 10))
    G10[:6, :6] = A_6
    G10[6, 6] = 1.0  # ℵ
    G10[7, 7] = 1.0  # S_x
    G10[8, 8] = 1.0  # S_y
    G10[9, 9] = 1.0  # S_z

    # Ma-ℵ: ring dimensions at ±1/(2π)
    G10[1, 6] = -INV_2PI  # e-ring
    G10[6, 1] = -INV_2PI
    G10[3, 6] = +INV_2PI  # ν-ring
    G10[6, 3] = +INV_2PI
    G10[5, 6] = +INV_2PI  # p-ring
    G10[6, 5] = +INV_2PI

    # ℵ-S
    for j in [7, 8, 9]:
        G10[6, j] = SIGMA_ALEPH_S
        G10[j, 6] = SIGMA_ALEPH_S

    return G10, L_6


def integrate_out_aleph(G10):
    keep = [0, 1, 2, 3, 4, 5, 7, 8, 9]
    M = G10[np.ix_(keep, keep)]
    b = G10[keep, 6]
    g = G10[6, 6]
    return M - np.outer(b, b) / g


def mode_energy_eff(G9, L_6, n6):
    """Mode energy on the effective 9×9 metric."""
    L_9 = np.concatenate([L_6, [1.0, 1.0, 1.0]])
    n9 = np.concatenate([np.array(n6, dtype=float) / L_9[:6], [0, 0, 0]])
    try:
        G9i = np.linalg.inv(G9)
        E2 = TWO_PI_HC**2 * n9 @ G9i @ n9
    except:
        return np.nan
    return math.sqrt(max(E2, 0))


def alpha_eff_mode(G9, L_6, n6):
    """Effective α for a mode."""
    L_9 = np.concatenate([L_6, [1.0, 1.0, 1.0]])
    n_ma = np.array(n6, dtype=float) / L_9[:6]
    A_bare = G9[:6, :6]
    try:
        E2_bare = TWO_PI_HC**2 * n_ma @ np.linalg.inv(A_bare) @ n_ma
        n9 = np.concatenate([n_ma, [0, 0, 0]])
        E2_coupled = TWO_PI_HC**2 * n9 @ np.linalg.inv(G9) @ n9
    except:
        return np.nan
    if E2_coupled <= 0:
        return np.nan
    return (E2_coupled - E2_bare) / E2_coupled


def main():
    print("=" * 75)
    print("R55 Track 4: Self-consistent parameters with ℵ coupling")
    print("=" * 75)
    print()
    print(f"  ℵ structure: Ma-ℵ = ±1/(2π) on rings, σℵS = {SIGMA_ALEPH_S:.5f}")
    print(f"  Strategy: fix ℵ coupling, then find (ε, s) for each sheet")
    print()

    # ── Step 1: How much do we need to adjust? ─────────────
    print("─" * 75)
    print("Step 1: Model-E parameters on the ℵ-corrected metric")
    print("─" * 75)
    print()

    # Model-E values
    eps_e_0, s_e_0 = 397.074, 2.004200
    eps_nu_0, s_nu_0 = 5.0, 0.022
    eps_p_0, s_p_0 = 0.55, solve_shear_for_alpha(0.55, n_tube=1, n_ring=3)

    cross_0 = {(3, 4): -0.18, (3, 5): 0.10}

    G10_0, L6_0 = build_10x10_from_sheets(
        eps_e_0, s_e_0, eps_nu_0, s_nu_0, eps_p_0, s_p_0, cross_0)

    eigs = np.linalg.eigvalsh(G10_0)
    print(f"  Model-E params on 10×10: PD = {np.all(eigs > 0)} (min eig = {min(eigs):.4e})")

    if not np.all(eigs > 0):
        print("  NOT positive-definite. Need to adjust parameters.")
        print()
        # The e-sheet shear saturates the e-tube. Let's check if
        # a small reduction in s_e fixes it.
        print("  Searching for max s_e that keeps PD...")
        for s_test in np.arange(s_e_0, 0, -0.001):
            G10_t, _ = build_10x10_from_sheets(
                eps_e_0, s_test, eps_nu_0, s_nu_0, eps_p_0, s_p_0, cross_0)
            eigs_t = np.linalg.eigvalsh(G10_t)
            if np.all(eigs_t > 0):
                print(f"  PD at s_e = {s_test:.6f} (reduced from {s_e_0:.6f})")
                print(f"  Δs_e = {s_test - s_e_0:.6f}")
                s_e_adj = s_test
                break
        else:
            print("  No PD solution found by reducing s_e.")
            s_e_adj = s_e_0 - 0.01  # fallback

        print()
    else:
        s_e_adj = s_e_0

    # ── Step 2: Adjust s_e to maintain PD ──────────────────
    print("─" * 75)
    print("Step 2: Find self-consistent e-sheet parameters")
    print("─" * 75)
    print()

    # The electron mass is set by: E = TWO_PI_HC * μ(1,2,ε,s) / L_ring
    # On the bare metric, μ(1,2,397,2.004) gives m_e = 0.511 MeV.
    # On the ℵ-corrected metric, the effective 6×6 Ma block shifts,
    # so we need a slightly different (ε,s) to get the same mass.

    # Strategy: fix ε_e = 397.074 (aspect ratio determines generation
    # structure), adjust s_e to:
    #   a) Keep PD
    #   b) Give correct electron mass on the effective metric
    #   c) Preserve m_μ/m_e and m_τ/m_e ratios

    # First, what mass does model-E give on the ℵ-corrected metric?
    if np.all(np.linalg.eigvalsh(G10_0) > 0):
        G9_0 = integrate_out_aleph(G10_0)
        E_e_0 = mode_energy_eff(G9_0, L6_0, (1, 2, 0, 0, 0, 0))
        E_p_0 = mode_energy_eff(G9_0, L6_0, (0, 0, -2, 2, 1, 3))
        print(f"  Model-E on ℵ metric: m_e = {E_e_0:.4f} MeV (target: {M_E_MEV:.4f})")
        print(f"  Model-E on ℵ metric: m_p = {E_p_0:.2f} MeV (target: {M_P_MEV:.2f})")
    else:
        print(f"  Model-E params are NOT PD on 10×10. Using adjusted s_e = {s_e_adj:.6f}")
        G10_adj, L6_adj = build_10x10_from_sheets(
            eps_e_0, s_e_adj, eps_nu_0, s_nu_0, eps_p_0, s_p_0, cross_0)
        G9_adj = integrate_out_aleph(G10_adj)
        E_e_adj = mode_energy_eff(G9_adj, L6_adj, (1, 2, 0, 0, 0, 0))
        E_p_adj = mode_energy_eff(G9_adj, L6_adj, (0, 0, -2, 2, 1, 3))
        print(f"  Adjusted on ℵ metric: m_e = {E_e_adj:.4f} MeV (target: {M_E_MEV:.4f})")
        print(f"  Adjusted on ℵ metric: m_p = {E_p_adj:.2f} MeV (target: {M_P_MEV:.2f})")
        print(f"  Electron shift: {(E_e_adj - M_E_MEV)/M_E_MEV*100:+.2f}%")
        print(f"  Proton shift: {(E_p_adj - M_P_MEV)/M_P_MEV*100:+.2f}%")

    print()

    # ── Step 3: Scan s_e to find the value that gives exact m_e ─
    print("─" * 75)
    print("Step 3: Find s_e that gives exact m_e on the ℵ-corrected metric")
    print("─" * 75)
    print()

    # Binary search over s_e
    eps_e = eps_e_0
    s_lo, s_hi = 1.5, s_e_0

    print(f"  Scanning s_e in [{s_lo:.3f}, {s_hi:.6f}], eps_e = {eps_e:.3f}")
    print()

    best_s_e = None
    best_err = 1e10

    for s_test in np.linspace(s_lo, s_hi, 200):
        G10_t, L6_t = build_10x10_from_sheets(
            eps_e, s_test, eps_nu_0, s_nu_0, eps_p_0, s_p_0, cross_0)
        eigs_t = np.linalg.eigvalsh(G10_t)
        if not np.all(eigs_t > 0):
            continue
        G9_t = integrate_out_aleph(G10_t)
        E_e_t = mode_energy_eff(G9_t, L6_t, (1, 2, 0, 0, 0, 0))
        err = abs(E_e_t - M_E_MEV) / M_E_MEV
        if err < best_err:
            best_err = err
            best_s_e = s_test

    if best_s_e is not None:
        print(f"  Best s_e = {best_s_e:.6f} (model-E: {s_e_0:.6f})")
        print(f"  Δs_e = {best_s_e - s_e_0:.6f} ({(best_s_e - s_e_0)/s_e_0*100:+.3f}%)")
        print(f"  Mass error: {best_err*100:.4f}%")

        # Now check the generation ratios at this s_e
        G10_best, L6_best = build_10x10_from_sheets(
            eps_e, best_s_e, eps_nu_0, s_nu_0, eps_p_0, s_p_0, cross_0)
        G9_best = integrate_out_aleph(G10_best)

        E_e = mode_energy_eff(G9_best, L6_best, (1, 2, 0, 0, 0, 0))
        # Check muon candidate modes
        print()
        print(f"  Generation check at s_e = {best_s_e:.6f}:")
        for n1, n2 in [(1,1), (1,2), (1,3), (3,5), (3,8), (2,4)]:
            E = mode_energy_eff(G9_best, L6_best, (n1, n2, 0, 0, 0, 0))
            ratio = E / E_e if E_e > 0 else 0
            label = ''
            if (n1, n2) == (1, 2): label = ' ← electron'
            if abs(ratio - 206.77) < 20: label = ' ← muon candidate'
            if abs(ratio - 3477) < 500: label = ' ← tau candidate'
            print(f"    ({n1},{n2}): E = {E:.4f} MeV, ratio = {ratio:.2f}{label}")

    else:
        print("  No PD solution found for any s_e. The ℵ coupling")
        print("  may require a different eps_e.")

    print()

    # ── Step 4: Similarly adjust p-sheet ───────────────────
    print("─" * 75)
    print("Step 4: Find s_p that gives exact m_p on the ℵ-corrected metric")
    print("─" * 75)
    print()

    if best_s_e is None:
        print("  Skipped (e-sheet not resolved)")
        print()
    else:
        s_e_new = best_s_e
        eps_p = eps_p_0
        best_s_p = None
        best_p_err = 1e10

        for s_test in np.linspace(0.01, 0.5, 200):
            G10_t, L6_t = build_10x10_from_sheets(
                eps_e, s_e_new, eps_nu_0, s_nu_0, eps_p, s_test, cross_0)
            eigs_t = np.linalg.eigvalsh(G10_t)
            if not np.all(eigs_t > 0):
                continue
            G9_t = integrate_out_aleph(G10_t)
            E_p_t = mode_energy_eff(G9_t, L6_t, (0, 0, -2, 2, 1, 3))
            err = abs(E_p_t - M_P_MEV) / M_P_MEV
            if err < best_p_err:
                best_p_err = err
                best_s_p = s_test

        if best_s_p is not None:
            print(f"  Best s_p = {best_s_p:.6f} (model-E: {s_p_0:.6f})")
            print(f"  Δs_p = {best_s_p - s_p_0:.6f}")
            print(f"  Mass error: {best_p_err*100:.4f}%")
        else:
            print("  No PD solution found for s_p")

    print()

    # ── Step 5: Full inventory with new parameters ─────────
    print("─" * 75)
    print("Step 5: Full particle inventory with self-consistent parameters")
    print("─" * 75)
    print()

    if best_s_e is not None and best_s_p is not None:
        s_e_new = best_s_e
        s_p_new = best_s_p

        G10_new, L6_new = build_10x10_from_sheets(
            eps_e, s_e_new, eps_nu_0, s_nu_0, eps_p, s_p_new, cross_0)
        G9_new = integrate_out_aleph(G10_new)

        particles = [
            ('electron',  (1, 2, 0, 0, 0, 0),      0.511,   -1),
            ('proton',    (0, 0, -2, 2, 1, 3),    938.272,   +1),
            ('neutron',   (0, -4, -1, 2, 0, -3),  939.565,    0),
            ('ν₁',       (0, 0, 1, 1, 0, 0),       0.0000292, 0),
            ('ν₂',       (0, 0, -1, 1, 0, 0),      0.0000305, 0),
            ('deuteron',  (0, 0, 0, 0, 2, 6),    1875.61,    +2),
            ('⁴He',      (0, 0, 0, 0, 4, 12),   3727.38,    +2),
            ('Λ',        (-1, 2, -1, 2, -1, 3),  1115.68,     0),
            ('Σ⁻',       (-1, 2, -2, 2, -2, -2), 1197.45,   -1),
        ]

        print(f"  New parameters: ε_e={eps_e:.3f}, s_e={s_e_new:.6f}, "
              f"ε_p={eps_p:.2f}, s_p={s_p_new:.6f}")
        print(f"  σℵS = {SIGMA_ALEPH_S:.5f}")
        print()

        print(f"  {'Particle':>10s}  {'Obs':>10s}  {'E_new':>10s}  {'Δ%':>7s}  "
              f"{'Q':>3s}  {'α_eff':>12s}  {'α/α₀':>8s}")
        print(f"  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*7}  "
              f"{'─'*3}  {'─'*12}  {'─'*8}")

        for name, n6, m_obs, Q in particles:
            E = mode_energy_eff(G9_new, L6_new, n6)
            ae = alpha_eff_mode(G9_new, L6_new, n6)

            if m_obs > 0:
                dpct = (E - m_obs) / m_obs * 100
            else:
                dpct = 0

            ae_str = f'{ae:.4e}' if not np.isnan(ae) else 'NaN'
            ar_str = f'{ae/ALPHA:.4f}' if not np.isnan(ae) else ''

            print(f"  {name:>10s}  {m_obs:10.3f}  {E:10.3f}  {dpct:+7.2f}  "
                  f"{Q:+3d}  {ae_str:>12s}  {ar_str:>8s}")

        print()

        # α universality summary
        ae_e = alpha_eff_mode(G9_new, L6_new, particles[0][1])
        ae_p = alpha_eff_mode(G9_new, L6_new, particles[1][1])
        ae_nu = alpha_eff_mode(G9_new, L6_new, particles[3][1])

        print(f"  α_eff(electron) = {ae_e:.6e} ({ae_e/ALPHA:.4f}α)")
        print(f"  α_eff(proton)   = {ae_p:.6e} ({ae_p/ALPHA:.4f}α)")
        print(f"  α_eff(ν₁)       = {ae_nu:.6e} ({ae_nu/ALPHA:.4f}α)")
        print(f"  e-p gap: {abs(ae_e-ae_p)/ALPHA:.4f}α ({abs(ae_e-ae_p)/ae_e*100:.2f}%)")

    else:
        print("  Skipped (parameters not resolved)")

    print()
    print("=" * 75)
    print("Track 4 complete.")
    print("=" * 75)


if __name__ == '__main__':
    main()
