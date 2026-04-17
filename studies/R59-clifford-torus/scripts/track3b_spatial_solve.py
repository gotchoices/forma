"""
R59 Track 3b: Spatial field solve — the Coulomb test.

Track 3's test bed narrowed the candidate mechanism to Arch 7
(Ma_ring ↔ t = α, signs ± for e/p).  It also revealed that three
α_eff measures from the metric disagree:

  (a) mass-shell shift       ~ σ
  (b) inverse-metric gauge   ~ σ²
  (c) spatial coefficient    — not yet computed

This track computes (c): the actual spatial profile of the
metric perturbation δg_{Ma,t}(r) in 3D space S, sourced by a
localized mode at the origin.  Then it:

1. Verifies the 1/r Coulomb profile at r >> L_Ma.
2. Extracts the coefficient C from δg_{Ma,t}(r) = C / (4πr).
3. Converts C to an effective Coulomb coupling α_Coulomb.
4. Compares α_Coulomb to measures (a) and (b) to identify
   which one (if either) is the Coulomb coupling.

The computation:

Background metric: Arch 7 from Track 3 — model-E's 6×6 Ma block,
flat S, Lorentzian t (g_tt = −1), with Ma_ring ↔ t entries:
  G[1, 9] = G[9, 1] = +α   (e-ring ↔ t)
  G[5, 9] = G[9, 5] = −α   (p-ring ↔ t)

Source: a standing-wave mode at origin in S with winding n.  In
mean-field/linearized language, the source produces a stress-
energy with a Ma-t component

  T_{Ma,t}(r) = (winding current) × (mode density)

The effective charge that sources the gauge field A_μ = g^{Ma,μ}
is:

  Q_eff = ∫ T_{Ma,t}(r) d³r  restricted to one Ma direction

For a mode on a single Ma-ring dimension with winding n_r, ring
circumference L_r, and rest energy E_0 = m c²:

  Q_eff ≈ σ × (n_r / L_r) × E_0 / (mc²) × (charge normalization)

The spatial field at r (outside the source):

  δg_{Ma,t}(r) = (1/4π r) × (4 G Q_eff)  [linearized gravity]
           or = Q_eff / (4π r)            [fixed-background Maxwell]

We do both readings and report them.  The "fixed-background"
reading treats the metric off-diagonal as a classical gauge
potential (no gravitational backreaction, consistent with KK's
effective 4D gauge field extraction).  The "linearized gravity"
reading sources the off-diagonal through the stress-energy (and
picks up a factor of G that makes α ~ 10⁻⁴², the known
hierarchy problem).

The fixed-background reading is the physically relevant one for
MaSt at Compton-scale compact dimensions.

Numerical procedure:

1. Define a smeared point source at origin: ρ(r) = Q_eff × f(r)
   where f(r) is a Gaussian of width w ≈ L_ring (Compton-scale).
2. Solve Poisson's equation ∇²φ = −ρ/ε₀ on a spherical grid
   (analytically — 3D Laplacian Green's function is 1/(4π|r−r'|)).
3. Fit φ(r) ~ C/r at large r.
4. Extract C.  Compute α_Coulomb = C × (normalization to observed α).

Three outcomes possible:
- α_Coulomb ≈ α  →  Ma-t mechanism IS Coulomb, σ = α is correct.
- α_Coulomb ≈ α but requires σ ≈ √α  →  mass-shell tuning was
  off by a √α factor, but the mechanism still works.
- α_Coulomb ≠ α by orders of magnitude  →  Ma-t coupling does
  not produce Coulomb's law; R59 falsified.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np

from lib.metric import Metric
from lib.ma_model_d import ALPHA, M_E_MEV, M_P_MEV, _TWO_PI_HC

ALPHA = 1.0 / 137.036
SQRT_ALPHA = math.sqrt(ALPHA)
TWO_PI_HC = _TWO_PI_HC
HBARC_MEV_FM = 197.327  # ℏc in MeV·fm

# Mode definitions
MODE_E = (1, 2, 0, 0, 0, 0)
MODE_P = (0, 0, -2, 2, 1, 3)

# Metric indices
I_E_TUBE, I_E_RING = 0, 1
I_P_TUBE, I_P_RING = 4, 5
I_T = 9


# ═══════════════════════════════════════════════════════════════════
#   Build Arch 7 metric (the single architecture that survives Track 3)
# ═══════════════════════════════════════════════════════════════════

def build_arch7_metric():
    """
    Build the 10D metric for Arch 7: model-E Ma + flat S + Lorentzian t,
    with Ma_ring ↔ t = ±α on e- and p-ring rows/columns.
    """
    m = Metric.model_E()
    assert m.valid

    G = np.zeros((10, 10))
    G[:6, :6] = m.Gt
    G[6, 6] = G[7, 7] = G[8, 8] = 1.0   # S
    G[9, 9] = -1.0                       # t

    # Arch 7 shears
    G[I_E_RING, I_T] = +ALPHA
    G[I_T, I_E_RING] = +ALPHA
    G[I_P_RING, I_T] = -ALPHA
    G[I_T, I_P_RING] = -ALPHA

    return G, m.L


# ═══════════════════════════════════════════════════════════════════
#   Source charge extraction from the metric
# ═══════════════════════════════════════════════════════════════════

def source_charge_Q_from_metric(G, L_Ma, n6):
    """
    Extract the effective source charge for a mode with winding n6.

    Reading 1 — direct gauge (Kaluza): the off-diagonal g_{Ma,t} acts
    as a classical gauge potential A_t.  A mode with winding n_ring
    around the ring circumference L_ring has momentum p = n_ring/L_ring
    in that compact direction, coupling to A_t as p × A_t.  The source
    "charge" that appears in Poisson's equation at large r is:

      Q_Kaluza = (n · g_{Ma,t}) / (dimensionful normalization)

    We compute the dimensionless Q_eff = n_tilde · g_{Ma,t}(row) where
    n_tilde = n/L.  The spatial potential at r (in natural units) is
    then A_t(r) = Q_eff / (4π r).
    """
    n_tilde = np.asarray(n6, dtype=float) / L_Ma
    g_Mat = G[:6, I_T]
    Q_direct = float(n_tilde @ g_Mat)
    return Q_direct


def source_charge_Q_from_inverse(G, L_Ma, n6):
    """
    Reading 2 — inverse-metric extraction (measure b).

    In classical KK, the gauge field A_μ is extracted from the inverse
    metric block: A_μ ∝ g^{Ma,μ}.  The mode's charge is then
    q_n = n · A_μ.
    """
    try:
        G_inv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return float('nan')
    n_tilde = np.asarray(n6, dtype=float) / L_Ma
    g_Mat_inv = G_inv[:6, I_T]
    Q_inv = float(n_tilde @ g_Mat_inv)
    return Q_inv


# ═══════════════════════════════════════════════════════════════════
#   Spatial field solve (numerical)
# ═══════════════════════════════════════════════════════════════════

def solve_spatial_field(Q_source, source_width_fm, r_grid_fm):
    """
    Solve ∇²φ(r) = −ρ(r) on 3D flat space with a Gaussian source
    ρ(r) = Q_source × (1/(2π w²)^{3/2}) × exp(−r²/(2w²))
    at the origin.  Returns φ(r) at the grid points.

    For a Gaussian source, the analytical solution is:
        φ(r) = Q_source/(4π r) × erf(r / (w × √2))
    At r >> w, φ(r) → Q_source/(4π r).
    At r → 0, φ(r) → Q_source × (1/(w × √(2π³)))  [finite].

    Parameters
    ----------
    Q_source : float — integrated source charge (dimensionless).
    source_width_fm : float — Gaussian width (fm).
    r_grid_fm : ndarray — radial distances (fm) to evaluate.

    Returns
    -------
    phi : ndarray — potential values at the grid points.
    """
    phi = np.zeros_like(r_grid_fm, dtype=float)
    for i, r in enumerate(r_grid_fm):
        if r <= 0:
            phi[i] = Q_source / (source_width_fm * math.sqrt(2 * math.pi**3))
        else:
            erf_arg = r / (source_width_fm * math.sqrt(2))
            phi[i] = Q_source * math.erf(erf_arg) / (4 * math.pi * r)
    return phi


def fit_asymptotic_coefficient(r, phi, r_fit_min_fm):
    """
    Fit φ(r) = C / (4π r) at large r (r > r_fit_min_fm).
    Returns the fitted C, and the maximum residual.
    """
    mask = r > r_fit_min_fm
    if np.sum(mask) < 3:
        return float('nan'), float('nan')
    r_fit = r[mask]
    phi_fit = phi[mask]
    # C = φ × 4π × r  at large r (should be constant)
    C_values = phi_fit * 4 * math.pi * r_fit
    C = float(np.mean(C_values))
    residual = float(np.max(np.abs(C_values - C)) / abs(C)) if C != 0 else float('nan')
    return C, residual


# ═══════════════════════════════════════════════════════════════════
#   Main computation: spatial Coulomb test on Arch 7
# ═══════════════════════════════════════════════════════════════════

def coulomb_test_for_mode(G, L_Ma, mode_name, n6, source_width_fm):
    """
    Run the full spatial field solve for one mode and report α_Coulomb.
    """
    print(f'\n─── {mode_name} — mode {n6} ───')

    # Source charge from the metric (two readings)
    Q_direct = source_charge_Q_from_metric(G, L_Ma, n6)
    Q_inv = source_charge_Q_from_inverse(G, L_Ma, n6)
    print(f'  Source strength from metric:')
    print(f'    Q_direct  (n · g_Mat)          = {Q_direct:+.6e}')
    print(f'    Q_inv     (n · g^Mat)          = {Q_inv:+.6e}')

    # Radial grid
    r_max = 1000 * source_width_fm  # out to 1000× source size
    r_grid = np.logspace(
        math.log10(source_width_fm * 0.1),
        math.log10(r_max),
        80,
    )

    # Solve with the DIRECT source strength (Kaluza reading)
    phi_direct = solve_spatial_field(Q_direct, source_width_fm, r_grid)
    C_direct, res_direct = fit_asymptotic_coefficient(
        r_grid, phi_direct, r_fit_min_fm=100 * source_width_fm)

    # Solve with the INVERSE-METRIC source strength (KK reading)
    phi_inv = solve_spatial_field(Q_inv, source_width_fm, r_grid)
    C_inv, res_inv = fit_asymptotic_coefficient(
        r_grid, phi_inv, r_fit_min_fm=100 * source_width_fm)

    print(f'  Solving Poisson for source Gaussian of width {source_width_fm:.2f} fm')
    print(f'  Fitting φ(r) = C/(4π r) at r > {100 * source_width_fm:.0f} fm')
    print(f'  Asymptotic coefficients:')
    print(f'    C_direct = {C_direct:+.6e}   (residual {res_direct:.2e})')
    print(f'    C_inv    = {C_inv:+.6e}   (residual {res_inv:.2e})')

    # Sample points along the radial profile
    print(f'  Sample profile (direct reading):')
    sample_indices = [0, len(r_grid) // 5, len(r_grid) // 2,
                      4 * len(r_grid) // 5, len(r_grid) - 1]
    print(f'    {"r (fm)":>12s}  {"r/w":>8s}  {"φ(r)":>14s}  {"C/(4πr)":>14s}  {"ratio":>8s}')
    for k in sample_indices:
        r = r_grid[k]
        phi = phi_direct[k]
        target = C_direct / (4 * math.pi * r) if r > 0 else float('inf')
        ratio = phi / target if target != 0 else float('nan')
        print(f'    {r:12.3f}  {r/source_width_fm:8.2f}  {phi:14.4e}  '
              f'{target:14.4e}  {ratio:8.4f}')

    # Compare to α
    # The observed electromagnetic coupling: two charges q_1, q_2 at distance r
    # feel potential V = α × q_1 q_2 / r (Gaussian natural units with e² = 4πα).
    # For the electron's field, its SOURCE CHARGE is q_e = ±√(4πα).
    # So the coefficient C in φ(r) = C/(4πr) should equal √(4πα) for a
    # unit electron.  Then α_Coulomb = C² / (4π).

    alpha_from_C_direct = (C_direct ** 2) / (4 * math.pi)
    alpha_from_C_inv = (C_inv ** 2) / (4 * math.pi)

    print(f'  α_Coulomb extraction (α_eff = C² / 4π):')
    print(f'    from C_direct: {alpha_from_C_direct:.6e}   '
          f'ratio to α: {alpha_from_C_direct/ALPHA:.4e}')
    print(f'    from C_inv:    {alpha_from_C_inv:.6e}   '
          f'ratio to α: {alpha_from_C_inv/ALPHA:.4e}')

    return {
        'mode': mode_name,
        'n6': n6,
        'Q_direct': Q_direct,
        'Q_inv': Q_inv,
        'C_direct': C_direct,
        'C_inv': C_inv,
        'alpha_from_C_direct': alpha_from_C_direct,
        'alpha_from_C_inv': alpha_from_C_inv,
    }


# ═══════════════════════════════════════════════════════════════════
#   Cross-check via force between two modes
# ═══════════════════════════════════════════════════════════════════

def force_between_modes(
    G, L_Ma, n6_src, n6_test, source_width_fm, r_obs_fm,
):
    """
    Compute the force between a source mode at origin and a test mode
    at distance r_obs, via:

      F = q_test × ∂φ/∂r

    where q_test is the test mode's charge from the metric, and φ is
    the field from the source mode.  Compare to Coulomb
    F_Coulomb = α × q_src_obs × q_test_obs / r².

    Returns the ratio F/F_Coulomb.
    """
    Q_src = source_charge_Q_from_metric(G, L_Ma, n6_src)
    Q_test = source_charge_Q_from_metric(G, L_Ma, n6_test)

    # At r >> source_width: φ(r) = Q_src/(4π r)
    # So ∂φ/∂r = −Q_src/(4π r²)
    # Force on test charge with "charge" Q_test:
    # F = −Q_test × ∂φ/∂r = Q_test × Q_src / (4π r²)

    # But we need to convert to a ratio.  The expected Coulomb force
    # for two UNIT charges (e = ±√(4πα)) at distance r:
    # F_Coulomb = e² / (4π r²) × (± sign from charge signs) = α × (±1) / r²

    # Our computed force:
    F_numerical = Q_src * Q_test / (4 * math.pi * r_obs_fm ** 2)

    # Coulomb force with unit charges (sign depends on model-E charges):
    charge_src = Metric.charge(n6_src)
    charge_test = Metric.charge(n6_test)
    F_Coulomb_expected = (
        ALPHA * charge_src * charge_test / (r_obs_fm ** 2)
    )

    return {
        'F_numerical': F_numerical,
        'F_Coulomb_expected': F_Coulomb_expected,
        'ratio': (F_numerical / F_Coulomb_expected
                  if F_Coulomb_expected != 0 else float('nan')),
        'charge_src': charge_src,
        'charge_test': charge_test,
    }


# ═══════════════════════════════════════════════════════════════════
#   Main
# ═══════════════════════════════════════════════════════════════════

def main():
    print('=' * 80)
    print('R59 Track 3b — Spatial field solve (Coulomb test)')
    print('=' * 80)
    print()
    print(f'  α = {ALPHA:.8f}')
    print(f'  √α = {SQRT_ALPHA:.8f}')
    print()

    # Build Arch 7 metric
    G, L_Ma = build_arch7_metric()
    print(f'  Architecture: Arch 7 (from Track 3)')
    print(f'    Ma_e-ring ↔ t = +α   (G[1,9])')
    print(f'    Ma_p-ring ↔ t = −α   (G[5,9])')
    print()
    print(f'  Ma circumferences (fm): {L_Ma}')
    print()

    # ── Spatial solve for electron ──
    print('─' * 80)
    print('  Part 1: Spatial field from electron source')
    print('─' * 80)
    # Source width: set by the mode's physical extent.  For the
    # electron, use the e-ring circumference (Compton-like scale).
    L_e_ring = L_Ma[I_E_RING]
    w_e = L_e_ring / (2 * math.pi)
    result_e = coulomb_test_for_mode(
        G, L_Ma, 'electron', MODE_E, source_width_fm=w_e)

    # ── Spatial solve for proton ──
    print()
    print('─' * 80)
    print('  Part 2: Spatial field from proton source')
    print('─' * 80)
    L_p_ring = L_Ma[I_P_RING]
    w_p = L_p_ring / (2 * math.pi)
    result_p = coulomb_test_for_mode(
        G, L_Ma, 'proton', MODE_P, source_width_fm=w_p)

    # ── Force test: electron source, proton at distance r ──
    print()
    print('─' * 80)
    print('  Part 3: Force between electron (origin) and proton (at r)')
    print('─' * 80)
    print()
    print(f'  Comparing computed force to Coulomb expectation F = α × q_e q_p / r²')
    print(f'  at several distances r (in units of the electron source width w_e = '
          f'{w_e:.4f} fm)')
    print()
    print(f'  {"r (fm)":>14s}  {"F_computed":>14s}  {"F_Coulomb":>14s}  {"ratio":>10s}')
    for r_mult in [10, 100, 1000, 10000]:
        r_obs = r_mult * w_e
        res = force_between_modes(
            G, L_Ma, MODE_E, MODE_P, source_width_fm=w_e, r_obs_fm=r_obs)
        print(f'  {r_obs:14.3f}  {res["F_numerical"]:14.4e}  '
              f'{res["F_Coulomb_expected"]:14.4e}  {res["ratio"]:10.4f}')

    # ── Summary and interpretation ──
    print()
    print('=' * 80)
    print('  SUMMARY')
    print('=' * 80)
    print()
    print(f'  Electron source:')
    print(f'    Q_direct = {result_e["Q_direct"]:+.4e}   '
          f'α from C²/4π = {result_e["alpha_from_C_direct"]:.4e}   '
          f'(ratio to α: {result_e["alpha_from_C_direct"]/ALPHA:.4e})')
    print(f'    Q_inv    = {result_e["Q_inv"]:+.4e}   '
          f'α from C²/4π = {result_e["alpha_from_C_inv"]:.4e}   '
          f'(ratio to α: {result_e["alpha_from_C_inv"]/ALPHA:.4e})')
    print()
    print(f'  Proton source:')
    print(f'    Q_direct = {result_p["Q_direct"]:+.4e}   '
          f'α from C²/4π = {result_p["alpha_from_C_direct"]:.4e}   '
          f'(ratio to α: {result_p["alpha_from_C_direct"]/ALPHA:.4e})')
    print(f'    Q_inv    = {result_p["Q_inv"]:+.4e}   '
          f'α from C²/4π = {result_p["alpha_from_C_inv"]:.4e}   '
          f'(ratio to α: {result_p["alpha_from_C_inv"]/ALPHA:.4e})')
    print()
    print(f'  Universality check (electron vs proton, direct reading):')
    if result_p["alpha_from_C_direct"] != 0:
        ratio = result_e['alpha_from_C_direct'] / result_p['alpha_from_C_direct']
        print(f'    α_e / α_p = {ratio:.4f}')
    else:
        print(f'    α_p = 0 (proton has no direct Ma-t coupling with this architecture)')
    print()
    print('=' * 80)
    print('Track 3b complete.')


if __name__ == '__main__':
    main()
