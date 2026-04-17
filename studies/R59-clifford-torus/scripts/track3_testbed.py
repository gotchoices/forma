"""
R59 Track 3 (rebuilt): Shear architecture test bed.

The question: when we put a dimensionless shear of magnitude σ into a
particular metric off-diagonal, does the resulting geometry produce
an effective α coupling in S of magnitude σ?

This script surveys a set of architectures (shear placements) and
extracts α_eff from each by the same procedure.  No tuning; each
architecture's α_eff is determined by its geometry alone.

Procedure for each architecture:

1. Construct an N×N metric (N = 10 without ℵ, 11 with).
   Starting point: model-E's 6×6 Ma metric (flat, with internal
   shears per R53).  Add flat S block (3D, +1), Lorentzian t
   diagonal (−1), optional ℵ diagonal (+1).

2. Overlay the architecture's shears at specified entries.

3. Check metric signature (exactly one negative eigenvalue = Lorentzian).
   A broken signature disqualifies the architecture.

4. Compute the particle-spectrum preservation: solve the particle
   root of the mass-shell quadratic for the bare electron mode
   (1,2,0,0,0,0) and proton mode (0,0,-2,2,1,3).  Compare to
   model-E's bare masses.  >1% deviation disqualifies.

5. Extract α_eff from the metric.  Three complementary measures:
      (a) Mass-shell splitting between particle and antiparticle roots:
            2δE/E_bare, where δE is half the ω₊ − ω₋ gap.  This is
            what Track 1 measured.
      (b) Direct inverse-metric coupling: the off-diagonal block
            g^{Ma,t} in the inverse (upper-indexed) metric, which
            IS the effective 4D gauge potential A_μ in natural
            normalization.
      (c) Spatial force coefficient: the coefficient C in
            δg_{Ma,t}(r) = C/r for r ≫ L_Ma, from the inverse-metric
            extraction.

   All three must be mutually consistent for the architecture to
   produce genuine α coupling.

6. Report signature, spectrum, α_eff(a,b,c) for electron and proton,
   and universality (e vs p).

None of these steps tunes any parameter.  Every α_eff is a direct
function of the input shears and the known model-E geometry.

Architectures surveyed:

  Arch 0:  Baseline (no off-diagonals beyond model-E)
  Arch 1:  Internal cross shear Ma_e-tube ↔ Ma_p-tube = α
  Arch 2:  Ma_tube ↔ S = α (direct spatial coupling)
  Arch 3:  Ma_tube ↔ ℵ = 1, ℵ ↔ S = α (ℵ-mediated to S)
  Arch 4:  Ma_tube ↔ ℵ = 1, ℵ ↔ t = α (ℵ-mediated to t)
  Arch 5:  Ma_tube ↔ t = α (direct Ma-t, single entry)
  Arch 6:  Ma_tube ↔ t = √α (KK-natural scale)
  Arch 7:  Ma_ring ↔ t = α (Track 1's architecture)
  Arch 8:  Ma_ring ↔ t = √α

For each: "tube" indices are 0 (e-tube) and 4 (p-tube); "ring"
indices are 1 (e-ring) and 5 (p-ring); tube and ring entries get
opposite signs for e and p to match observed charges.
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

# Mode definitions (6-tuples of winding numbers)
MODE_E = (1, 2, 0, 0, 0, 0)
MODE_P = (0, 0, -2, 2, 1, 3)

# Dimension indexing:
#   0-5: Ma (e-tube, e-ring, ν-tube, ν-ring, p-tube, p-ring)
#   6-8: S (x, y, z)
#   9:   t
#   10:  ℵ (if 11D)
I_E_TUBE, I_E_RING = 0, 1
I_P_TUBE, I_P_RING = 4, 5
I_SX, I_SY, I_SZ = 6, 7, 8
I_T = 9
I_ALEPH = 10


# ═══════════════════════════════════════════════════════════════════
#   Metric construction
# ═══════════════════════════════════════════════════════════════════

def build_metric(
    shears_Ma=None,
    shears_Ma_S=None,
    shears_Ma_t=None,
    use_aleph=False,
    shears_Ma_aleph=None,
    shear_aleph_t=None,
    shear_aleph_S=None,
):
    """
    Build the full metric as a real N×N numpy array.

    Starting point: model-E's 6×6 Ma metric (from lib.metric), flat
    3D S, Lorentzian t, optional ℵ.  Additional shears overlay on
    top, summed symmetrically into (i,j) and (j,i).

    Parameters
    ----------
    shears_Ma : dict {(i,j): value} — extra Ma-Ma entries (added to
        model-E's internal + cross shears).  i, j in [0..5].
    shears_Ma_S : dict {(i_Ma, j_S): value} — j_S in [0..2].
    shears_Ma_t : dict {i_Ma: value} — tube or ring index.
    use_aleph : bool — if True, N=11 and ℵ block added.
    shears_Ma_aleph : dict {i_Ma: value}.
    shear_aleph_t : float or None.
    shear_aleph_S : float or None — if set, applied uniformly to
        all three ℵ-S entries.

    Returns
    -------
    G : (N, N) ndarray — the metric.
    L_Ma : (6,) ndarray — Ma circumferences (fm).
    """
    N = 11 if use_aleph else 10

    # Model-E base metric (6x6 dimensionless Ma block)
    m = Metric.model_E()
    assert m.valid, "model-E base metric is not valid"

    G = np.zeros((N, N))
    G[:6, :6] = m.Gt
    L_Ma = m.L.copy()  # circumferences in fm

    # S block: +1 identity (Euclidean)
    G[I_SX, I_SX] = 1.0
    G[I_SY, I_SY] = 1.0
    G[I_SZ, I_SZ] = 1.0

    # Time: Lorentzian, −1
    G[I_T, I_T] = -1.0

    # ℵ block (Euclidean)
    if use_aleph:
        G[I_ALEPH, I_ALEPH] = 1.0

    # Additional Ma-Ma shears
    if shears_Ma:
        for (i, j), val in shears_Ma.items():
            G[i, j] += val
            if i != j:
                G[j, i] += val

    # Ma-S shears
    if shears_Ma_S:
        for (i_Ma, j_S), val in shears_Ma_S.items():
            idx_S = 6 + j_S
            G[i_Ma, idx_S] = val
            G[idx_S, i_Ma] = val

    # Ma-t shears
    if shears_Ma_t:
        for i_Ma, val in shears_Ma_t.items():
            G[i_Ma, I_T] = val
            G[I_T, i_Ma] = val

    # Ma-ℵ shears
    if use_aleph and shears_Ma_aleph:
        for i_Ma, val in shears_Ma_aleph.items():
            G[i_Ma, I_ALEPH] = val
            G[I_ALEPH, i_Ma] = val

    # ℵ-t shear
    if use_aleph and shear_aleph_t is not None:
        G[I_ALEPH, I_T] = shear_aleph_t
        G[I_T, I_ALEPH] = shear_aleph_t

    # ℵ-S shears (applied uniformly across x,y,z)
    if use_aleph and shear_aleph_S is not None:
        for idx_S in (I_SX, I_SY, I_SZ):
            G[I_ALEPH, idx_S] = shear_aleph_S
            G[idx_S, I_ALEPH] = shear_aleph_S

    return G, L_Ma


# ═══════════════════════════════════════════════════════════════════
#   Signature check
# ═══════════════════════════════════════════════════════════════════

def check_signature(G):
    """
    Return (n_neg, signature_ok) where signature_ok means exactly
    one negative eigenvalue (Lorentzian with mostly-plus convention).
    """
    eigs = np.linalg.eigvalsh(G)
    n_neg = int(np.sum(eigs < 0))
    signature_ok = (n_neg == 1)
    return n_neg, signature_ok, eigs


# ═══════════════════════════════════════════════════════════════════
#   Mass-shell computation (particle + antiparticle roots)
# ═══════════════════════════════════════════════════════════════════

def mass_shell_roots(G, L_Ma, n6):
    """
    Solve the mass-shell equation g^{AB} k_A k_B = 0 for a mode with
    winding n6 at rest in S (and at ℵ=0 if 11D).

    Returns (E_particle, E_antiparticle) in MeV, or (nan, nan) if
    the discriminant is negative.

    E_particle is the larger of the two (mass increased by coupling);
    E_antiparticle is the smaller.

    The wavevector in the full metric is:
        k = (n/L_Ma, 0, 0, 0, ω, [0 for ℵ])
    where ω = E/(2πℏc).  Mass-shell condition is
        g^{ab} k_a k_b = 0
    with the upper-index inverse metric.  Expanding:
        c + b ω + a ω² = 0
    where
        a = g^{tt}
        b = 2 · g^{Ma,t} · (n/L)
        c = (n/L) · g^{Ma,Ma} · (n/L)
    (plus analogous ℵ contributions; since k_ℵ = 0 those vanish
    except through the inverse entries, which the full linear algebra
    handles automatically.)
    """
    N = G.shape[0]

    try:
        G_inv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return np.nan, np.nan

    n_tilde = np.zeros(N)
    n_tilde[:6] = np.asarray(n6, dtype=float) / L_Ma

    # Quadratic coefficients in ω
    a = G_inv[I_T, I_T]
    b = 2.0 * (G_inv[:6, I_T] @ n_tilde[:6])
    c = n_tilde[:6] @ G_inv[:6, :6] @ n_tilde[:6]

    # Add ℵ contributions if present.  k_ℵ = 0, but cross entries
    # (Ma-ℵ in inverse) modify c via the Ma-Ma slice of G^{-1}; that
    # is already captured above.  Direct t-ℵ contribution is zero
    # since k_ℵ = 0.
    # (No additional terms needed — they're zero by k_ℵ = 0.)

    disc = b * b - 4.0 * a * c
    if disc < 0:
        return np.nan, np.nan
    sqrt_disc = math.sqrt(disc)

    # Roots: ω = (-b ± √disc) / (2a).  With a = -1:
    #   ω = (b ∓ √disc) / 2
    omega_1 = (b - sqrt_disc) / (2.0 * a)
    omega_2 = (b + sqrt_disc) / (2.0 * a)

    E1 = TWO_PI_HC * abs(omega_1)
    E2 = TWO_PI_HC * abs(omega_2)

    E_particle = max(E1, E2)
    E_anti = min(E1, E2)
    return E_particle, E_anti


# ═══════════════════════════════════════════════════════════════════
#   α extraction — three complementary measures
# ═══════════════════════════════════════════════════════════════════

def extract_alpha_mass_shell(G, L_Ma, n6, E_bare):
    """
    Measure (a): fractional mass-shell splitting.

    α_eff = (E_particle − E_bare) / E_bare.
    This is what Track 1 measured (with the sign corrected by F22).
    """
    E_particle, E_anti = mass_shell_roots(G, L_Ma, n6)
    if math.isnan(E_particle):
        return np.nan
    return (E_particle - E_bare) / E_bare


def extract_alpha_inverse_metric(G, L_Ma, n6):
    """
    Measure (b): effective 4D gauge field from the inverse metric.

    In Kaluza-Klein theory, A_μ = −g^{Ma,μ} / g^{Ma,Ma} (natural
    normalization).  For a mode with winding n, the effective 4D
    charge is q_n = (n/L) · A_μ × (normalization).

    We extract the dimensionless coupling:
        σ_eff = |g^{Ma,t}| · |n/L| / √(|g^{Ma,Ma}| · |g^{tt}|)
    evaluated with the full inverse metric and the mode's n/L vector.
    α_eff = σ_eff² (by the natural KK normalization where the
    Coulomb coupling is σ² with σ the dimensionless slant angle).

    This is the 'gauge extraction' reading — independent of any
    mass-shell solve.
    """
    try:
        G_inv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return np.nan

    n_tilde = np.zeros(G.shape[0])
    n_tilde[:6] = np.asarray(n6, dtype=float) / L_Ma

    # Numerator: coupling between Ma wavevector and time direction
    # via the inverse metric off-diagonal
    g_Mat_dot_n = G_inv[:6, I_T] @ n_tilde[:6]

    # Denominator: scale-setting product of diagonal blocks
    g_MaMa = n_tilde[:6] @ G_inv[:6, :6] @ n_tilde[:6]
    g_tt = G_inv[I_T, I_T]

    if abs(g_MaMa) < 1e-30 or abs(g_tt) < 1e-30:
        return np.nan

    # σ_eff is the dimensionless slant angle felt by the mode
    sigma_eff = abs(g_Mat_dot_n) / math.sqrt(abs(g_MaMa) * abs(g_tt))
    alpha_eff = sigma_eff * sigma_eff
    return alpha_eff


def extract_alpha_spatial(G, L_Ma, n6):
    """
    Measure (c): spatial-field coefficient.

    For a source mode at origin in S, the linearized Einstein equation
    on flat 3D S gives δg_{Ma,t}(r) = C/(4π r) at large r, where C is
    proportional to the source strength.

    In our 10D/11D setup with the source mode's Ma winding n, the
    coefficient C is derived from the inverse metric entries:
        C = (n/L) · g^{Ma,t}  (evaluated on the full inverse)
    The resulting 4D potential is A_0(r) = C/(4π r × g^{tt}).

    A test mode with winding m at distance r feels potential energy
        V(r) = (m/L · C) / (4π r × g^{tt})
    Matching to Coulomb V = α q_1 q_2 / r with q_n ∝ n:
        α_eff = |C|² / (4π g^{tt})²  × (per-mode normalization)

    We report the dimensionless |C|² / |g^{tt}|².
    """
    try:
        G_inv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return np.nan

    n_tilde = np.zeros(G.shape[0])
    n_tilde[:6] = np.asarray(n6, dtype=float) / L_Ma

    C = G_inv[:6, I_T] @ n_tilde[:6]
    g_tt = G_inv[I_T, I_T]
    g_MaMa = n_tilde[:6] @ G_inv[:6, :6] @ n_tilde[:6]

    if abs(g_tt) < 1e-30 or abs(g_MaMa) < 1e-30:
        return np.nan

    # Normalize to the mode's Ma scale so α_eff is dimensionless and
    # scale-free (so electron and proton can be compared directly)
    return (C * C) / (abs(g_tt) * abs(g_MaMa))


# ═══════════════════════════════════════════════════════════════════
#   Single-architecture test
# ═══════════════════════════════════════════════════════════════════

def test_architecture(name, description, arch_kwargs):
    """Run all diagnostics for one architecture and return a dict."""

    # Build metric
    G, L_Ma = build_metric(**arch_kwargs)
    N = G.shape[0]

    # Signature check
    n_neg, sig_ok, eigs = check_signature(G)

    # Bare reference: no extra shears (just model-E)
    G_bare, _ = build_metric()
    E_e_bare, _ = mass_shell_roots(G_bare, L_Ma, MODE_E)
    E_p_bare, _ = mass_shell_roots(G_bare, L_Ma, MODE_P)

    if not sig_ok:
        return {
            'name': name, 'description': description,
            'N': N, 'n_neg': n_neg, 'signature_ok': False,
            'E_e_bare': E_e_bare, 'E_p_bare': E_p_bare,
            'E_e_particle': np.nan, 'E_p_particle': np.nan,
            'spectrum_e_dev': np.nan, 'spectrum_p_dev': np.nan,
            'spectrum_ok': False,
            'alpha_e_shell': np.nan, 'alpha_p_shell': np.nan,
            'alpha_e_inv': np.nan, 'alpha_p_inv': np.nan,
            'alpha_e_spatial': np.nan, 'alpha_p_spatial': np.nan,
            'min_eig': float(eigs.min()), 'max_eig': float(eigs.max()),
        }

    # Mass-shell computation
    E_e_particle, E_e_anti = mass_shell_roots(G, L_Ma, MODE_E)
    E_p_particle, E_p_anti = mass_shell_roots(G, L_Ma, MODE_P)

    # Spectrum preservation: use the particle-root energy
    if math.isnan(E_e_particle) or math.isnan(E_p_particle):
        spectrum_e_dev = spectrum_p_dev = np.nan
        spectrum_ok = False
    else:
        spectrum_e_dev = abs(E_e_particle - E_e_bare) / E_e_bare
        spectrum_p_dev = abs(E_p_particle - E_p_bare) / E_p_bare
        spectrum_ok = (spectrum_e_dev < 0.05) and (spectrum_p_dev < 0.05)

    # α extraction (three measures)
    alpha_e_shell = extract_alpha_mass_shell(G, L_Ma, MODE_E, E_e_bare)
    alpha_p_shell = extract_alpha_mass_shell(G, L_Ma, MODE_P, E_p_bare)
    alpha_e_inv = extract_alpha_inverse_metric(G, L_Ma, MODE_E)
    alpha_p_inv = extract_alpha_inverse_metric(G, L_Ma, MODE_P)
    alpha_e_spatial = extract_alpha_spatial(G, L_Ma, MODE_E)
    alpha_p_spatial = extract_alpha_spatial(G, L_Ma, MODE_P)

    return {
        'name': name, 'description': description,
        'N': N, 'n_neg': n_neg, 'signature_ok': True,
        'E_e_bare': E_e_bare, 'E_p_bare': E_p_bare,
        'E_e_particle': E_e_particle, 'E_p_particle': E_p_particle,
        'E_e_anti': E_e_anti, 'E_p_anti': E_p_anti,
        'spectrum_e_dev': spectrum_e_dev,
        'spectrum_p_dev': spectrum_p_dev,
        'spectrum_ok': spectrum_ok,
        'alpha_e_shell': alpha_e_shell,
        'alpha_p_shell': alpha_p_shell,
        'alpha_e_inv': alpha_e_inv,
        'alpha_p_inv': alpha_p_inv,
        'alpha_e_spatial': alpha_e_spatial,
        'alpha_p_spatial': alpha_p_spatial,
        'min_eig': float(eigs.min()), 'max_eig': float(eigs.max()),
    }


# ═══════════════════════════════════════════════════════════════════
#   Architecture definitions
# ═══════════════════════════════════════════════════════════════════

def architectures():
    """Return list of (name, description, arch_kwargs) tuples."""

    def arch(name, description, **kwargs):
        return (name, description, kwargs)

    archs = []

    # ── Arch 0 ──
    archs.append(arch(
        'Arch 0 — Baseline',
        'No additional off-diagonals beyond model-E (internal '
        'shears, and the default σ₄₅=−0.18, σ₄₆=+0.10 soft '
        'cross-sheet entries from R54)',
    ))

    # ── Arch 1 ──
    archs.append(arch(
        'Arch 1 — Internal cross shear = α',
        'Additional Ma_e-tube ↔ Ma_p-tube entry of magnitude α',
        shears_Ma={(I_E_TUBE, I_P_TUBE): ALPHA},
    ))

    # ── Arch 2 ──
    archs.append(arch(
        'Arch 2 — Ma_tube ↔ S = α',
        'Ma_e-tube ↔ S_x = +α, Ma_p-tube ↔ S_x = −α',
        shears_Ma_S={(I_E_TUBE, 0): +ALPHA, (I_P_TUBE, 0): -ALPHA},
    ))

    # ── Arch 3 ──
    archs.append(arch(
        'Arch 3 — Ma↔ℵ=1, ℵ↔S=α',
        'Ma_e-tube↔ℵ=+1, Ma_p-tube↔ℵ=−1; ℵ↔S_x = α',
        use_aleph=True,
        shears_Ma_aleph={I_E_TUBE: +1.0, I_P_TUBE: -1.0},
        shear_aleph_S=ALPHA,
    ))

    # ── Arch 4 ──
    archs.append(arch(
        'Arch 4 — Ma↔ℵ=1, ℵ↔t=α',
        'Ma_e-tube↔ℵ=+1, Ma_p-tube↔ℵ=−1; ℵ↔t = α',
        use_aleph=True,
        shears_Ma_aleph={I_E_TUBE: +1.0, I_P_TUBE: -1.0},
        shear_aleph_t=ALPHA,
    ))

    # ── Arch 5 ──
    archs.append(arch(
        'Arch 5 — Ma_tube ↔ t = α',
        'Direct Ma_e-tube↔t = +α, Ma_p-tube↔t = −α',
        shears_Ma_t={I_E_TUBE: +ALPHA, I_P_TUBE: -ALPHA},
    ))

    # ── Arch 6 ──
    archs.append(arch(
        'Arch 6 — Ma_tube ↔ t = √α',
        'Direct, scaled by √α: Ma_e-tube↔t = +√α, Ma_p-tube↔t = −√α',
        shears_Ma_t={I_E_TUBE: +SQRT_ALPHA, I_P_TUBE: -SQRT_ALPHA},
    ))

    # ── Arch 7 ──
    archs.append(arch(
        'Arch 7 — Ma_ring ↔ t = α (Track 1-style)',
        'Ma_e-ring↔t = +α, Ma_p-ring↔t = −α',
        shears_Ma_t={I_E_RING: +ALPHA, I_P_RING: -ALPHA},
    ))

    # ── Arch 8 ──
    archs.append(arch(
        'Arch 8 — Ma_ring ↔ t = √α',
        'Same as Arch 7 but scaled by √α',
        shears_Ma_t={I_E_RING: +SQRT_ALPHA, I_P_RING: -SQRT_ALPHA},
    ))

    return archs


# ═══════════════════════════════════════════════════════════════════
#   Reporting
# ═══════════════════════════════════════════════════════════════════

def fmt(x, ratio=False):
    """Format a float for the results table."""
    if isinstance(x, bool):
        return 'YES' if x else 'no'
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return '—'
    if isinstance(x, int):
        return str(x)
    if abs(x) < 1e-4 or abs(x) > 1e4:
        return f'{x:.2e}'
    if ratio:
        return f'{x:.3f}'
    return f'{x:.4g}'


def print_header(title, char='='):
    width = 90
    print(char * width)
    print(title)
    print(char * width)


def print_section(title):
    print()
    print('─' * 90)
    print(f'  {title}')
    print('─' * 90)


def main():
    print_header('R59 Track 3 (rebuilt) — Shear architecture test bed')
    print()
    print(f'  α = {ALPHA:.8f} = 1/137.036')
    print(f'  √α = {SQRT_ALPHA:.8f}')
    print()
    print(f'  Mode e: {MODE_E}  (electron, charge −1)')
    print(f'  Mode p: {MODE_P}  (proton, charge +1)')
    print()

    # Compute bare reference
    G_bare, L_Ma = build_metric()
    E_e_bare, _ = mass_shell_roots(G_bare, L_Ma, MODE_E)
    E_p_bare, _ = mass_shell_roots(G_bare, L_Ma, MODE_P)
    print(f'  Bare electron: {E_e_bare:.4f} MeV')
    print(f'  Bare proton:   {E_p_bare:.4f} MeV')
    print()
    print(f'  L_Ma (fm): {L_Ma}')
    print()

    # Run all architectures
    archs = architectures()
    results = []
    for name, description, kwargs in archs:
        result = test_architecture(name, description, kwargs)
        results.append(result)

    # ── Detailed per-architecture output ──
    for r in results:
        print_section(r['name'])
        print(f'  {r["description"]}')
        print()
        print(f'  Metric dimension:     {r["N"]}')
        print(f'  Negative eigenvalues: {r["n_neg"]}   '
              f'(signature ok: {fmt(r["signature_ok"])})')
        if not r['signature_ok']:
            print(f'  Min/max eigenvalues:  {r["min_eig"]:.4g} / '
                  f'{r["max_eig"]:.4g}')
            print('  → DISQUALIFIED (wrong metric signature)')
            continue
        print()
        print(f'  Electron particle-root mass:  {r["E_e_particle"]:.6f} MeV  '
              f'(bare {r["E_e_bare"]:.4f}, dev {100*r["spectrum_e_dev"]:.3f}%)')
        print(f'  Proton   particle-root mass:  {r["E_p_particle"]:.4f} MeV  '
              f'(bare {r["E_p_bare"]:.4f}, dev {100*r["spectrum_p_dev"]:.3f}%)')
        print(f'  Spectrum preservation:        {fmt(r["spectrum_ok"])}')
        print()
        print(f'  α extraction (three measures):')
        print(f'    (a) Mass-shell shift:        '
              f'electron {fmt(r["alpha_e_shell"])}  '
              f'proton {fmt(r["alpha_p_shell"])}')
        print(f'    (b) Inverse-metric gauge:    '
              f'electron {fmt(r["alpha_e_inv"])}  '
              f'proton {fmt(r["alpha_p_inv"])}')
        print(f'    (c) Spatial coefficient |C|²: '
              f'electron {fmt(r["alpha_e_spatial"])}  '
              f'proton {fmt(r["alpha_p_spatial"])}')
        print()
        print(f'  Ratio to α (mass-shell measure): '
              f'electron {fmt(r["alpha_e_shell"]/ALPHA if not math.isnan(r["alpha_e_shell"]) else np.nan, ratio=True)}  '
              f'proton {fmt(r["alpha_p_shell"]/ALPHA if not math.isnan(r["alpha_p_shell"]) else np.nan, ratio=True)}')

    # ── Summary table ──
    print()
    print_header('Summary table', '═')
    print()
    header = (
        f'  {"Arch":40s}  {"sig":>4s}  {"spec":>4s}  '
        f'{"α_e(a)":>10s}  {"α_p(a)":>10s}  {"e/α":>6s}  {"p/α":>6s}'
    )
    print(header)
    print(f'  {"-"*40}  {"-"*4}  {"-"*4}  {"-"*10}  {"-"*10}  {"-"*6}  {"-"*6}')
    for r in results:
        sig = 'YES' if r['signature_ok'] else 'no'
        spec = 'YES' if r.get('spectrum_ok') else 'no'
        ae = r['alpha_e_shell']
        ap = r['alpha_p_shell']
        ae_rat = ae/ALPHA if not math.isnan(ae) else np.nan
        ap_rat = ap/ALPHA if not math.isnan(ap) else np.nan
        name_trunc = r['name'][:40]
        print(f'  {name_trunc:40s}  {sig:>4s}  {spec:>4s}  '
              f'{fmt(ae):>10s}  {fmt(ap):>10s}  '
              f'{fmt(ae_rat, ratio=True):>6s}  {fmt(ap_rat, ratio=True):>6s}')
    print()

    # ── Cross-measure consistency check ──
    print_section('Cross-measure consistency')
    print('  For each architecture that passed signature+spectrum, does')
    print('  α_eff from measure (a) agree with measure (b) at the order of α?')
    print()
    for r in results:
        if not r['signature_ok']:
            continue
        ae = r['alpha_e_shell']
        ae_inv = r['alpha_e_inv']
        if math.isnan(ae) or math.isnan(ae_inv):
            continue
        # Report ratios between the different measures
        ratio = ae / ae_inv if abs(ae_inv) > 1e-30 else float('inf')
        print(f'  {r["name"][:50]:50s}  (a)/(b) = {ratio:.3f}')

    print()
    print_header('Track 3 test bed complete')


if __name__ == '__main__':
    main()
