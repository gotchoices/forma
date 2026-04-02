"""
Local torus EM model for R46 — vector field with circular polarization.

A circularly polarized photon on the (n₁, n₂) geodesic has its
E-field rotating in the plane perpendicular to propagation.  On a
torus, one axis of that plane is the surface normal, the other is
tangent to the surface (perpendicular to the geodesic).

For n₁ = 1, the E-field rotation rate matches the surface-normal
rotation rate (one turn per tube circuit).  The result: E_normal
is constant around the tube, depending only on ring position θ₂.

    E_n(θ₁, θ₂) = E₀ cos(q_eff θ₂)
    E_t(θ₁, θ₂) = E₀ sin(q_eff θ₂)

where q_eff = n₂ − s.  The θ₁ from the mode phase cancels against
the θ₁ from the surface-normal rotation — this IS the n₁ = 1
selection rule (R19 F17) seen from the vector perspective.

For circular polarization, |E|² = E₀² everywhere (cos² + sin² = 1),
so the field energy is uniformly distributed over the surface.

Conventions:
  θ₁: tube angle (0 = outer equator, π = inner equator)
  θ₂: ring angle (0 .. 2π)
  r = a/R: aspect ratio (tube radius / ring radius, R19 convention)
  s: fractional shear (dimensionless)
  q_eff = n₂ − s: effective ring winding number
"""

import math
import numpy as np

# ── Physical constants (CODATA 2018) ─────────────────────────────
H       = 6.62607015e-34      # Planck constant, J·s
HBAR    = H / (2 * math.pi)
C       = 299792458.0          # speed of light, m/s
EPS0    = 8.8541878128e-12     # vacuum permittivity, F/m
E_CHARGE = 1.602176634e-19    # elementary charge, C
ALPHA   = 7.2973525693e-3     # fine structure constant
M_E     = 9.1093837015e-31    # electron mass, kg
LAMBDA_C = H / (M_E * C)     # Compton wavelength, m
LAMBDABAR_C = HBAR / (M_E * C)  # reduced Compton wavelength, m


def make_grid(N1=256, N2=512):
    """Uniform (θ₁, θ₂) grid on [0, 2π) × [0, 2π)."""
    t1 = np.linspace(0, 2 * np.pi, N1, endpoint=False)
    t2 = np.linspace(0, 2 * np.pi, N2, endpoint=False)
    T1, T2 = np.meshgrid(t1, t2, indexing='ij')
    return T1, T2, t1, t2


# ── Torus geometry ───────────────────────────────────────────────

def rho_factor(T1, r):
    """ρ/R = 1 + r cos θ₁, where r = a/R."""
    return 1.0 + r * np.cos(T1)


def torus_area(r):
    """Total surface area A = 4π²aR = 4π²r R².  Returns A/R²."""
    return 4.0 * math.pi**2 * r


def geometry_kk(r, s):
    """Torus dimensions under KK Compton constraint.
    E_mode = (ℏc/R)·μ = m_e c²  →  R = λ̄_C · μ,  a = rR.
    μ(1, n₂) = √(1/r² + (n₂−s)²), with n₂ = 2 for the electron."""
    q = 2.0 - s
    mu = math.sqrt(1.0 / r**2 + q**2)
    R = LAMBDABAR_C * mu
    a = r * R
    return R, a


# ── Vector field: circular polarization on torus ─────────────────
#
# Physical picture (unipolar model):
#
#   The confined photon's E field always pushes outward from the
#   2D sheet into 3D.  The radiation pressure at each point is
#   proportional to E₀(1 + cos(q_eff θ₂)) — always ≥ 0.
#
#   The DC component (the "1") is the equilibrium pressure that
#   maintains the cavity against the membrane's confining force
#   (R37 force balance).  It does not produce external field.
#
#   The AC component (cos(q_eff θ₂)) is the standing-wave
#   modulation: where cos > 0 the pressure exceeds the mean and
#   more field leaks through the Compton window; where cos < 0
#   the pressure is below the mean and less leaks.  Only this
#   modulation produces external charge.
#
#   The opposite knot chirality (positron) has the modulation
#   reversed in sign, giving charge +e.

def e_normal_unipolar(T2, q_eff):
    """Outward radiation pressure on the sheet, always ≥ 0.

    P_out ∝ E₀(1 + cos(q_eff θ₂))

    Returns dimensionless (1 + cos(q θ₂)), range [0, 2].
    This is the physical field — no energy passes backward
    through the sheet.
    """
    return 1.0 + np.cos(q_eff * T2)


def e_normal_ac(T2, q_eff):
    """Charge-producing modulation of E_normal.

    The deviation from mean radiation pressure: cos(q_eff θ₂).
    This is what leaks through the Compton window as external
    field and integrates to give charge Q = −e.
    Returns dimensionless cos(q θ₂), range [−1, +1].
    """
    return np.cos(q_eff * T2)


def e_tangential(T2, q_eff):
    """Tangential component of E (⊥ to geodesic, in surface).
    E_t = E₀ sin(q_eff θ₂).  Returns E_t/E₀."""
    return np.sin(q_eff * T2)


def b_tangential(T2, q_eff):
    """B field is tangential, 90° from E_t, magnitude E₀/c.
    For a CP wave, B_t = (E₀/c) sin(q_eff θ₂).
    Returns c·B_t/E₀ (dimensionless, same pattern as E_t)."""
    return np.sin(q_eff * T2)


def field_amplitude_cp(r, R):
    """E₀ from total mode energy = m_e c² for circular polarization.

    For CP, |E|² = E₀² uniformly (cos² + sin² = 1).  The EM energy
    density is ε₀ E₀² (E and B contribute equally).  The mode
    extends through the torus wall with characteristic depth a
    (same convention as R19/R44), giving effective volume
    V = a × 4π²aR = 4π²a²R:

        U = ε₀ E₀² × 4π²a²R

    Setting U = m_e c²:  E₀ = √(m_e c² / (4π²a²R ε₀))

    The thickness factor a cancels in the α formula, but is needed
    to get the correct absolute E₀ and hence the correct charge.
    """
    a = r * R
    return math.sqrt(M_E * C**2 / (4.0 * math.pi**2 * a**2 * R * EPS0))


# ── Charge integral ──────────────────────────────────────────────

def charge_integral_analytic(E0, r, R, s, n2=2):
    """Analytical total charge for a CP (n₁=1, n₂) mode.

    Q = ε₀ E₀ ∫∫ cos(q_eff θ₂) × a(R + a cos θ₁) dθ₁ dθ₂

    θ₁ integral: ∫₀²π a(R + a cos θ₁) dθ₁ = 2πaR
    θ₂ integral: ∫₀²π cos(q θ₂) dθ₂ = sin(2πq)/q = −sin(2πs)/(n₂−s)

    Q = −ε₀ E₀ × 2πaR × sin(2πs) / (n₂ − s)
    """
    q_eff = n2 - s
    a = r * R
    return -EPS0 * E0 * 2 * math.pi * a * R * math.sin(2 * math.pi * s) / q_eff


def charge_numerical(E0, T1, T2, r, R, q_eff, N1, N2):
    """Numerical charge integral for validation."""
    a = r * R
    rho = R + a * np.cos(T1)
    En = E0 * np.cos(q_eff * T2)
    sigma = EPS0 * En
    dA = a * rho
    dth1 = 2 * math.pi / N1
    dth2 = 2 * math.pi / N2
    return np.sum(sigma * dA) * dth1 * dth2


# ── Alpha formula (vector/CP model) ─────────────────────────────

def alpha_cp_kk(r, s, n2=2):
    """Fine structure constant from the CP vector model under KK.

    Derived by setting Q = e in charge_integral_analytic with
    E₀ from field_amplitude_cp (volume-normalized) and R from
    geometry_kk:

        Q² = ε₀ m_e c² R sin²(2πs) / q²

        α = Q²/(4πε₀ℏc) = μ sin²(2πs) / (4π q²)

    where μ = √(1/r² + q²) and q = n₂ − s.

    Relation to scalar: α_CP = α_scalar / r².
    At r = 1, both formulas agree.  At larger r, CP requires
    more shear to produce the same α.
    """
    q = n2 - s
    if abs(q) < 1e-15:
        return 0.0
    sn = math.sin(2 * math.pi * s)
    if abs(sn) < 1e-15:
        return 0.0
    mu = math.sqrt(1.0 / r**2 + q**2)
    return mu * sn**2 / (4 * math.pi * q**2)


def alpha_scalar_kk(r, s, n2=2):
    """R19 scalar α formula (KK convention) for comparison.
    α = r² √(1/r² + (n₂−s)²) sin²(2πs) / (4π(n₂−s)²)"""
    q = n2 - s
    if abs(q) < 1e-15:
        return 0.0
    sn = math.sin(2 * math.pi * s)
    if abs(sn) < 1e-15:
        return 0.0
    mu = math.sqrt(1.0 / r**2 + q**2)
    return r**2 * mu * sn**2 / (4 * math.pi * q**2)


def solve_shear(r, alpha_func, target=None):
    """Bisection solver for α(r,s) = target."""
    if target is None:
        target = ALPHA
    ss = np.linspace(0.001, 0.499, 40000)
    vals = np.array([alpha_func(r, si) - target for si in ss])
    for i in range(len(vals) - 1):
        if vals[i] * vals[i+1] < 0:
            lo, hi = float(ss[i]), float(ss[i+1])
            for _ in range(80):
                mid = (lo + hi) / 2.0
                if (alpha_func(r, mid) - target) * (alpha_func(r, lo) - target) < 0:
                    hi = mid
                else:
                    lo = mid
            return (lo + hi) / 2.0
    return None


# ── Ghost mode ───────────────────────────────────────────────────

def ghost_mass_ratio_kk(r, s):
    """m_ghost / m_electron under KK for (1,1) vs (1,2)."""
    mu_e = math.sqrt(1.0 / r**2 + (2.0 - s)**2)
    mu_g = math.sqrt(1.0 / r**2 + (1.0 - s)**2)
    return mu_g / mu_e
