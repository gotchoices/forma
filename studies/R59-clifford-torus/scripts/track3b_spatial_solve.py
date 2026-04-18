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
I_ALEPH = 10  # only used when use_aleph=True


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
#   Build ℵ-mediated architecture (Ma → ℵ → t chain, 11D)
# ═══════════════════════════════════════════════════════════════════

def build_aleph_mediated_metric(
    sigma_Ma_aleph_e=+1.0/(2*math.pi),
    sigma_Ma_aleph_p=-1.0/(2*math.pi),
    sigma_aleph_t=ALPHA,
    g_aleph_aleph=1.0,
    use_tubes=False,
):
    """
    Build 11D metric with Ma → ℵ → t chain.

    The effective Ma-t coupling after integrating out ℵ is:
        σ_eff = g(Ma,ℵ) × g(ℵ,t) / g(ℵ,ℵ)

    With small g(ℵ,ℵ), this amplifies: a tiny ℵ dimension can
    magnify small individual entries into an effectively large
    Ma-t coupling, while keeping each entry small enough for
    the metric to remain positive-definite.

    Parameters test different ℵ scales to explore the amplification.

    If use_tubes=True, the Ma↔ℵ shears go on the TUBE dimensions
    (indices 0, 4) rather than the ring dimensions (1, 5).  The
    MaSt theory is that charge comes from tube winding — so
    tube→ℵ→t is the physically-motivated routing.  Tube↔t direct
    coupling broke signature (Track 3 Arch 5/6) because it put a
    large entry next to the Lorentzian t diagonal; tube↔ℵ is
    Euclidean-Euclidean and may not have the same issue.
    """
    m = Metric.model_E()
    assert m.valid

    G = np.zeros((11, 11))
    G[:6, :6] = m.Gt
    G[6, 6] = G[7, 7] = G[8, 8] = 1.0      # S
    G[9, 9] = -1.0                          # t
    G[I_ALEPH, I_ALEPH] = g_aleph_aleph     # ℵ diagonal

    # Ma ↔ ℵ shears — on tubes or rings depending on use_tubes
    i_e, i_p = (I_E_TUBE, I_P_TUBE) if use_tubes else (I_E_RING, I_P_RING)
    G[i_e, I_ALEPH] = sigma_Ma_aleph_e
    G[I_ALEPH, i_e] = sigma_Ma_aleph_e
    G[i_p, I_ALEPH] = sigma_Ma_aleph_p
    G[I_ALEPH, i_p] = sigma_Ma_aleph_p

    # ℵ ↔ t shear
    G[I_ALEPH, I_T] = sigma_aleph_t
    G[I_T, I_ALEPH] = sigma_aleph_t

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

    For ℵ-mediated architectures (11D), we extract via the INVERSE
    metric, which naturally includes the Schur amplification
    σ_eff = g(Ma,ℵ) × g(ℵ,t) / g(ℵ,ℵ).
    """
    n_tilde = np.asarray(n6, dtype=float) / L_Ma
    if G.shape[0] == 10:
        # Direct reading: upper-indexed Ma-t coupling is just g(Ma,t)
        # at leading order (since no ℵ path exists).
        g_Mat = G[:6, I_T]
        Q_direct = float(n_tilde @ g_Mat)
    else:
        # 11D: include ℵ path via inverse metric, which captures Schur
        # amplification automatically.
        try:
            G_inv = np.linalg.inv(G)
        except np.linalg.LinAlgError:
            return float('nan')
        # Upper-indexed g^{Ma,t} includes the ℵ chain contribution
        g_Mat_upper = G_inv[:6, I_T]
        # Normalize back to "effective off-diagonal" form.  The inverse
        # metric's Ma-t block, at leading order in the perturbation, is:
        #   g^{Ma,t} ≈ -[g(Ma,t) + g(Ma,ℵ) g(ℵ,t) / g(ℵ,ℵ)] / (g_tt · g_Ma)
        # For a nearly diagonal Ma and g_tt = -1, this simplifies to
        # +σ_eff / g_Ma(diag) approximately.  We multiply through by
        # the Ma-diagonal scale to get back the "effective σ."
        # Simplest clean extraction: use the inverse-metric value
        # directly as the dimensionless source strength.
        # Dimensional factor: g_tt = -1 and the Ma diagonals in model-E
        # are O(1) for rings (except e-ring due to shear); we leave the
        # extraction as g^{Ma,t} itself.  For symmetry with 10D, also
        # multiply by -g_tt = +1 (no change).
        Q_direct = float(n_tilde @ g_Mat_upper) * (-G_inv[I_T, I_T])
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


def check_signature_and_spectrum(G, L_Ma):
    """Quick signature check and spectrum preservation test."""
    eigs = np.linalg.eigvalsh(G)
    n_neg = int(np.sum(eigs < 0))
    sig_ok = (n_neg == 1)
    if not sig_ok:
        return sig_ok, None, None, None, None
    # Compute particle-root masses to check spectrum
    G_inv = np.linalg.inv(G)
    n_tilde_e = np.zeros(G.shape[0])
    n_tilde_e[:6] = np.asarray(MODE_E, dtype=float) / L_Ma
    n_tilde_p = np.zeros(G.shape[0])
    n_tilde_p[:6] = np.asarray(MODE_P, dtype=float) / L_Ma
    # Solve mass-shell for each
    def solve(nt):
        a = G_inv[I_T, I_T]
        b = 2.0 * (G_inv[:6, I_T] @ nt[:6])
        c = nt[:6] @ G_inv[:6, :6] @ nt[:6]
        if G.shape[0] == 11:
            # Add ℵ-axis diagonal contribution to dispersion from nt[10]=0
            # (no additional term since nt_aleph = 0 at rest).
            pass
        disc = b * b - 4.0 * a * c
        if disc < 0:
            return float('nan')
        return max(
            TWO_PI_HC * abs((b - math.sqrt(disc)) / (2.0 * a)),
            TWO_PI_HC * abs((b + math.sqrt(disc)) / (2.0 * a)),
        )
    E_e = solve(n_tilde_e)
    E_p = solve(n_tilde_p)
    return sig_ok, n_neg, E_e, E_p, eigs


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

    # ── Part 4: ℵ-mediated architecture scan ──
    print()
    print('─' * 80)
    print('  Part 4: ℵ-mediated architecture — does Schur amplification help?')
    print('─' * 80)
    print()
    print('  Effective Ma-t coupling after integrating out ℵ:')
    print('    σ_eff ≈ g(Ma,ℵ) × g(ℵ,t) / g(ℵ,ℵ)')
    print()
    print('  If g(ℵ,ℵ) is small, σ_eff is amplified.  This could let')
    print('  small individual entries produce a large effective Ma-t')
    print('  coupling — potentially hitting the σ_eff ≈ 1.8 we need.')
    print()

    # Scan g(ℵ,ℵ) from 1 down through sub-Planck scales
    print(f'  {"g(ℵ,ℵ)":>10s}  {"Ma↔ℵ":>8s}  {"ℵ↔t":>10s}  '
          f'{"sig":>4s}  {"E_e (MeV)":>10s}  {"E_p (MeV)":>10s}  '
          f'{"Q_e":>11s}  {"α_e / α":>10s}  {"α_e/α_p":>8s}')
    print(f'  {"-"*10}  {"-"*8}  {"-"*10}  {"-"*4}  '
          f'{"-"*10}  {"-"*10}  {"-"*11}  {"-"*10}  {"-"*8}')

    for g_aa in [1.0, 1e-1, 1e-2, 1e-3, 1e-5, 1e-10, 1e-20, 1e-40]:
        # Use R55's Ma-ℵ value (1/(2π)) and ℵ-t = α as starting point
        G_aleph, _ = build_aleph_mediated_metric(
            sigma_Ma_aleph_e=+1.0/(2*math.pi),
            sigma_Ma_aleph_p=-1.0/(2*math.pi),
            sigma_aleph_t=ALPHA,
            g_aleph_aleph=g_aa,
        )
        sig_ok, n_neg, E_e, E_p, eigs = check_signature_and_spectrum(G_aleph, L_Ma)
        if not sig_ok:
            print(f'  {g_aa:10.2e}  {1/(2*math.pi):8.4f}  {ALPHA:10.4e}  '
                  f'{"no":>4s}  {"—":>10s}  {"—":>10s}  '
                  f'{"—":>11s}  {"—":>10s}  {"—":>8s}')
            continue

        # Extract source charges using inverse metric (picks up ℵ chain)
        Q_e = source_charge_Q_from_metric(G_aleph, L_Ma, MODE_E)
        Q_p = source_charge_Q_from_metric(G_aleph, L_Ma, MODE_P)

        alpha_e = (Q_e ** 2) / (4 * math.pi)
        alpha_p = (Q_p ** 2) / (4 * math.pi) if Q_p != 0 else float('nan')

        ratio_e = alpha_e / ALPHA
        ratio_ep = alpha_e / alpha_p if alpha_p != 0 else float('nan')

        e_e_str = f'{E_e:10.4f}' if E_e is not None and not math.isnan(E_e) else f'{"—":>10s}'
        e_p_str = f'{E_p:10.2f}' if E_p is not None and not math.isnan(E_p) else f'{"—":>10s}'

        print(f'  {g_aa:10.2e}  {1/(2*math.pi):8.4f}  {ALPHA:10.4e}  '
              f'{"YES":>4s}  {e_e_str}  {e_p_str}  '
              f'{Q_e:+11.4e}  {ratio_e:10.4e}  '
              f'{ratio_ep:8.4g}')

    print()
    print('  Now sweep with Ma↔ℵ = 1/(2π), solving for ℵ↔t such that α_Coulomb = α')
    print('  (asks: what ℵ↔t entry would we NEED?)')
    print()

    # For the electron-ring mode with n_1 = 2, L_1 = 11.88 fm:
    # At leading order in perturbation theory, Q_e ≈ (n/L)_e × σ_eff
    # where σ_eff = g(Ma,ℵ) × g(ℵ,t) / g(ℵ,ℵ) for the 11D case.
    # For α_Coulomb = Q² / (4π) = α, need Q = √(4πα) ≈ 0.303
    # So (n/L)_e × σ_eff = 0.303 → σ_eff = 0.303 × 11.88 / 2 = 1.80
    target_sigma_eff = math.sqrt(4 * math.pi * ALPHA) * L_Ma[I_E_RING] / MODE_E[I_E_RING]
    print(f'  Target σ_eff (for electron to give α_Coulomb = α): {target_sigma_eff:.4f}')
    print()
    print(f'  {"g(ℵ,ℵ)":>10s}  {"required ℵ↔t":>14s}  {"sig with it":>12s}')
    print(f'  {"-"*10}  {"-"*14}  {"-"*12}')
    for g_aa in [1.0, 1e-1, 1e-2, 1e-3, 1e-5]:
        # σ_eff = (1/(2π)) × σ_aleph_t / g_aa
        # → σ_aleph_t = σ_eff × g_aa × 2π
        required_sigma_at = target_sigma_eff * g_aa * (2 * math.pi)
        # Test if this breaks signature
        G_test, _ = build_aleph_mediated_metric(
            sigma_Ma_aleph_e=+1.0/(2*math.pi),
            sigma_Ma_aleph_p=-1.0/(2*math.pi),
            sigma_aleph_t=required_sigma_at,
            g_aleph_aleph=g_aa,
        )
        sig_ok, n_neg, _, _, _ = check_signature_and_spectrum(G_test, L_Ma)
        print(f'  {g_aa:10.2e}  {required_sigma_at:14.4e}  '
              f'{"YES" if sig_ok else f"no ({n_neg} neg eigs)":>12s}')

    # ── Part 5: Verification — do the "required" ℵ↔t values produce α? ──
    print()
    print('─' * 80)
    print('  Part 5: Verify that "required ℵ↔t" architectures give α_Coulomb = α')
    print('─' * 80)
    print()
    print('  For each config that passed signature, compute α_Coulomb explicitly')
    print('  and check spectrum preservation.')
    print()
    print(f'  {"g(ℵ,ℵ)":>10s}  {"ℵ↔t":>12s}  '
          f'{"E_e (MeV)":>10s}  {"E_e dev":>9s}  {"E_p (MeV)":>10s}  {"E_p dev":>9s}  '
          f'{"α_e/α":>10s}  {"α_p/α":>10s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*10}  {"-"*12}  '
          f'{"-"*10}  {"-"*9}  {"-"*10}  {"-"*9}  '
          f'{"-"*10}  {"-"*10}  {"-"*10}')

    # Need bare masses for deviation check
    G_bare, _ = build_arch7_metric()
    # Remove Arch 7 shears to get truly bare
    G_bare[I_E_RING, I_T] = 0
    G_bare[I_T, I_E_RING] = 0
    G_bare[I_P_RING, I_T] = 0
    G_bare[I_T, I_P_RING] = 0
    _, _, E_e_bare, E_p_bare, _ = check_signature_and_spectrum(G_bare, L_Ma)

    for g_aa in [1.0, 1e-1, 1e-2, 1e-3, 1e-5]:
        required_sigma_at = target_sigma_eff * g_aa * (2 * math.pi)
        G_test, _ = build_aleph_mediated_metric(
            sigma_Ma_aleph_e=+1.0/(2*math.pi),
            sigma_Ma_aleph_p=-1.0/(2*math.pi),
            sigma_aleph_t=required_sigma_at,
            g_aleph_aleph=g_aa,
        )
        sig_ok, n_neg, E_e, E_p, _ = check_signature_and_spectrum(G_test, L_Ma)
        if not sig_ok:
            print(f'  {g_aa:10.2e}  {required_sigma_at:12.4e}  '
                  f'{"—":>10s}  {"—":>9s}  {"—":>10s}  {"—":>9s}  '
                  f'{"—":>10s}  {"—":>10s}  {"—":>10s}')
            continue

        Q_e = source_charge_Q_from_metric(G_test, L_Ma, MODE_E)
        Q_p = source_charge_Q_from_metric(G_test, L_Ma, MODE_P)
        alpha_e = (Q_e ** 2) / (4 * math.pi)
        alpha_p = (Q_p ** 2) / (4 * math.pi) if Q_p != 0 else float('nan')
        ratio_e = alpha_e / ALPHA
        ratio_p = alpha_p / ALPHA if not math.isnan(alpha_p) else float('nan')
        ratio_ep = alpha_e / alpha_p if alpha_p != 0 else float('nan')

        dev_e = abs(E_e - E_e_bare) / E_e_bare * 100
        dev_p = abs(E_p - E_p_bare) / E_p_bare * 100

        print(f'  {g_aa:10.2e}  {required_sigma_at:12.4e}  '
              f'{E_e:10.4f}  {dev_e:8.2f}%  {E_p:10.2f}  {dev_p:8.2f}%  '
              f'{ratio_e:10.4e}  {ratio_p:10.4e}  {ratio_ep:10.4g}')

    # ── Part 6: Tube-based ℵ mediation (tube → ℵ → t) ──
    print()
    print('─' * 80)
    print('  Part 6: Tube-based ℵ mediation (charge comes from tube winding)')
    print('─' * 80)
    print()
    print('  MaSt theory: charge is tube winding.  The physically-motivated')
    print('  routing puts the Ma↔ℵ shear on the TUBE, not the ring.')
    print()
    print('  For the electron (1,2,0,0,0,0), tube winding n_0 = 1.')
    print('  For the proton (0,0,-2,2,1,3), tube winding n_4 = 1.')
    print('  Both have |n_tube| = 1 — which matches observed |charge| = 1.')
    print()
    print('  This is a DIFFERENT scaling from the ring case:')
    print('    ring: n_e=2, n_p=3 → bare charge ratio would be 3/2')
    print('    tube: n_e=1, n_p=1 → bare charge ratio is 1:1 (universal)')
    print()

    # Scan over ℵ parameters with TUBE coupling
    print(f'  Scan: Ma↔ℵ on TUBES, various ℵ↔t and g(ℵ,ℵ)')
    print()
    print(f'  {"Ma↔ℵ":>8s}  {"ℵ↔t":>10s}  {"g(ℵ,ℵ)":>10s}  '
          f'{"sig":>4s}  {"E_e dev":>9s}  {"E_p dev":>9s}  '
          f'{"α_e/α":>12s}  {"α_p/α":>12s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*8}  {"-"*10}  {"-"*10}  {"-"*4}  '
          f'{"-"*9}  {"-"*9}  {"-"*12}  {"-"*12}  {"-"*10}')

    # Test configurations
    test_configs = [
        # (Ma-ℵ, ℵ-t, g(ℵ,ℵ))
        (1.0/(2*math.pi), ALPHA, 1.0),      # R55-like values on tubes
        (1.0/(2*math.pi), ALPHA, 0.1),      # smaller ℵ
        (1.0/(2*math.pi), SQRT_ALPHA, 1.0), # ℵ-t at √α
        (1.0/(2*math.pi), 1.0, 1.0),        # ℵ-t = 1
        (SQRT_ALPHA, SQRT_ALPHA, 1.0),      # both at √α (KK-like)
        (SQRT_ALPHA, 1.0, 1.0),             # Ma-ℵ small, ℵ-t large
        (1.0, ALPHA, 1.0),                  # Ma-ℵ large, ℵ-t small
        (1.0, SQRT_ALPHA, 1.0),             # Ma-ℵ = 1, ℵ-t = √α
        (1.0, 1.0, 1.0),                    # Both entries = 1 (pure KK)
        (0.01, 0.01, 1.0),                  # small symmetric
    ]

    G_bare_aleph, _ = build_aleph_mediated_metric(
        sigma_Ma_aleph_e=0, sigma_Ma_aleph_p=0, sigma_aleph_t=0,
        g_aleph_aleph=1.0, use_tubes=True)
    _, _, E_e_bare_11, E_p_bare_11, _ = check_signature_and_spectrum(
        G_bare_aleph, L_Ma)

    for sigma_Ma_aleph, sigma_aleph_t, g_aa in test_configs:
        G_test, _ = build_aleph_mediated_metric(
            sigma_Ma_aleph_e=+sigma_Ma_aleph,
            sigma_Ma_aleph_p=-sigma_Ma_aleph,  # opposite sign for charge
            sigma_aleph_t=sigma_aleph_t,
            g_aleph_aleph=g_aa,
            use_tubes=True,
        )
        sig_ok, n_neg, E_e, E_p, _ = check_signature_and_spectrum(G_test, L_Ma)
        if not sig_ok:
            print(f'  {sigma_Ma_aleph:8.4f}  {sigma_aleph_t:10.4e}  {g_aa:10.2e}  '
                  f'{"no":>4s}  {"—":>9s}  {"—":>9s}  '
                  f'{"—":>12s}  {"—":>12s}  {"—":>10s}')
            continue

        Q_e = source_charge_Q_from_metric(G_test, L_Ma, MODE_E)
        Q_p = source_charge_Q_from_metric(G_test, L_Ma, MODE_P)
        alpha_e = (Q_e ** 2) / (4 * math.pi)
        alpha_p = (Q_p ** 2) / (4 * math.pi) if Q_p != 0 else float('nan')
        ratio_e = alpha_e / ALPHA
        ratio_p = alpha_p / ALPHA if not math.isnan(alpha_p) else float('nan')
        ratio_ep = alpha_e / alpha_p if alpha_p != 0 else float('nan')

        dev_e = abs(E_e - E_e_bare_11) / E_e_bare_11 * 100
        dev_p = abs(E_p - E_p_bare_11) / E_p_bare_11 * 100

        print(f'  {sigma_Ma_aleph:8.4f}  {sigma_aleph_t:10.4e}  {g_aa:10.2e}  '
              f'{"YES":>4s}  {dev_e:8.2f}%  {dev_p:8.2f}%  '
              f'{ratio_e:12.4e}  {ratio_p:12.4e}  {ratio_ep:10.4g}')

    # ── Part 7: Abandon model-E shears — does tube↔ℵ↔t work on a clean metric? ──
    print()
    print('─' * 80)
    print('  Part 7: No model-E shears — tube↔ℵ↔t on a clean Ma metric')
    print('─' * 80)
    print()
    print('  Part 6 showed tube-based ℵ mediation always breaks signature on')
    print('  model-E.  The cause: s_e = 2.004 makes e-tube near-singular via')
    print('  the internal shear.  Any additional tube coupling pushes the')
    print('  smallest eigenvalue negative.')
    print()
    print('  Test: zero the internal shears (s_e = s_ν = s_p = 0).  Does the')
    print('  tube↔ℵ↔t architecture then work, giving α_Coulomb ≈ α?')
    print()
    print('  Caveat: without model-E shears, the particle spectrum is DIFFERENT.')
    print('  We are asking whether α emerges from the coupling architecture')
    print('  — not whether model-E as a whole still works.  This is the')
    print('  "abandon model-E, solve for α first, derive particles second"')
    print('  scenario.')
    print()

    def build_shearless_aleph_tube_metric(
        sigma_Ma_aleph_e, sigma_Ma_aleph_p, sigma_aleph_t, g_aleph_aleph=1.0,
    ):
        """Build an 11D metric with:
        - Ma block: DIAGONAL (no internal shears, no cross-shears).
          Diagonals set to 1 everywhere (so the shape is set, not the scale).
        - Plus tube↔ℵ, ℵ↔t entries as specified.
        """
        G = np.zeros((11, 11))
        # Ma: pure identity (no shears of any kind)
        for i in range(6):
            G[i, i] = 1.0
        G[6, 6] = G[7, 7] = G[8, 8] = 1.0   # S
        G[9, 9] = -1.0                       # t
        G[I_ALEPH, I_ALEPH] = g_aleph_aleph  # ℵ
        # Tube couplings
        G[I_E_TUBE, I_ALEPH] = sigma_Ma_aleph_e
        G[I_ALEPH, I_E_TUBE] = sigma_Ma_aleph_e
        G[I_P_TUBE, I_ALEPH] = sigma_Ma_aleph_p
        G[I_ALEPH, I_P_TUBE] = sigma_Ma_aleph_p
        G[I_ALEPH, I_T] = sigma_aleph_t
        G[I_T, I_ALEPH] = sigma_aleph_t
        # Use a unit L vector so n/L has simple interpretation
        L = np.ones(6)
        return G, L

    print(f'  Clean Ma metric (identity), unit L vector so "charge" = n_tube directly')
    print()
    print(f'  {"Ma↔ℵ":>8s}  {"ℵ↔t":>10s}  {"g(ℵ,ℵ)":>10s}  '
          f'{"sig":>4s}  {"Q_e":>12s}  {"Q_p":>12s}  '
          f'{"α_e/α":>10s}  {"α_p/α":>10s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*8}  {"-"*10}  {"-"*10}  {"-"*4}  '
          f'{"-"*12}  {"-"*12}  {"-"*10}  {"-"*10}  {"-"*10}')

    clean_test_configs = [
        (SQRT_ALPHA, SQRT_ALPHA, 1.0),     # symmetric √α
        (SQRT_ALPHA, 1.0, 1.0),            # Ma-ℵ √α, ℵ-t = 1
        (1.0, SQRT_ALPHA, 1.0),            # Ma-ℵ = 1, ℵ-t = √α
        (1.0, 1.0, 1.0),                   # both = 1 (pure KK)
        (0.5, 0.5, 1.0),                   # symmetric 0.5
        (0.1, 0.1, 1.0),
        (1.0/(2*math.pi), ALPHA, 1.0),     # R55-like
        (SQRT_ALPHA, SQRT_ALPHA, 0.1),     # smaller g_ℵℵ
        (SQRT_ALPHA, SQRT_ALPHA, 0.01),
    ]

    for sigma_Ma_aleph, sigma_aleph_t, g_aa in clean_test_configs:
        G_clean, L_clean = build_shearless_aleph_tube_metric(
            sigma_Ma_aleph_e=+sigma_Ma_aleph,
            sigma_Ma_aleph_p=-sigma_Ma_aleph,
            sigma_aleph_t=sigma_aleph_t,
            g_aleph_aleph=g_aa,
        )
        sig_ok, n_neg, E_e, E_p, _ = check_signature_and_spectrum(G_clean, L_clean)
        if not sig_ok:
            print(f'  {sigma_Ma_aleph:8.4f}  {sigma_aleph_t:10.4e}  {g_aa:10.2e}  '
                  f'{"no":>4s}  {"—":>12s}  {"—":>12s}  '
                  f'{"—":>10s}  {"—":>10s}  {"—":>10s}')
            continue

        Q_e = source_charge_Q_from_metric(G_clean, L_clean, MODE_E)
        Q_p = source_charge_Q_from_metric(G_clean, L_clean, MODE_P)
        alpha_e = (Q_e ** 2) / (4 * math.pi)
        alpha_p = (Q_p ** 2) / (4 * math.pi) if Q_p != 0 else float('nan')
        ratio_e = alpha_e / ALPHA
        ratio_p = alpha_p / ALPHA if not math.isnan(alpha_p) else float('nan')
        ratio_ep = alpha_e / alpha_p if alpha_p != 0 else float('nan')

        print(f'  {sigma_Ma_aleph:8.4f}  {sigma_aleph_t:10.4e}  {g_aa:10.2e}  '
              f'{"YES":>4s}  {Q_e:+12.4e}  {Q_p:+12.4e}  '
              f'{ratio_e:10.4e}  {ratio_p:10.4e}  {ratio_ep:10.4g}')

    print()
    print('  Observations:')
    print('  - On the clean (shearless) Ma metric, tube↔ℵ↔t CAN pass signature')
    print('  - Electron and proton have identical tube windings (|n_0|=|n_4|=1)')
    print('    → universality is STRUCTURAL (independent of L_Ma sizing)')
    print('  - Whether α comes out to observed α depends on whether a simple')
    print('    (σ_Ma-ℵ, σ_ℵ-t) pair gives α_Coulomb = α')

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
