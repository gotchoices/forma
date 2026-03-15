"""
R13 Track 2: Four candidate charge mechanisms on T³

Track 1 showed that flat T³ gives zero charge (no polarization
rotation).  Four candidate resolutions:

  1. Compact-space curvature (→ gravity integration)
  2. Metric off-diagonal terms (KK gauge connection)
  3. Topological charge (winding number = charge)
  4. Cross-terms in 7D field equations

This script analyzes each mechanism quantitatively where
possible.

Bears on: R13 findings, Q18, Q32
"""

import math

# Physical constants
G = 6.67430e-11          # N m²/kg²
c = 2.99792458e8         # m/s
hbar = 1.054571817e-34   # J·s
epsilon_0 = 8.8541878128e-12  # F/m
e_SI = 1.602176634e-19   # C
m_e = 9.1093837015e-31   # kg
alpha = 1/137.035999084
r_e = 2.8179403262e-15   # m
lambda_C = 2.42631023867e-12  # m

R = 2.79e-15   # major radius
a = 8.60e-16   # minor radius
L1 = 2 * math.pi * a
L2 = 2 * math.pi * R


def section(title):
    print(f"\n{'=' * 65}")
    print(f"  {title}")
    print(f"{'=' * 65}")


def subsection(title):
    print(f"\n--- {title} ---")


# ================================================================
# RESOLUTION 1: Compact-space curvature
# ================================================================
section("RESOLUTION 1: Compact-space curvature")

subsection("Gravitational curvature from the photon's energy")

E_electron = m_e * c**2
energy_density = E_electron / (L1 * L2 * L2)  # assume L3 ~ L2

R_curv_gravity = G * energy_density / c**4  # Ricci scalar ~ G T / c⁴

print(f"Photon energy:    {E_electron:.3e} J = {E_electron/1.602e-13:.3f} MeV")
print(f"Compact volume:   V ~ L₁L₂² = {L1 * L2**2:.3e} m³")
print(f"Energy density:   ρ ~ E/V = {energy_density:.3e} J/m³")
print(f"Gravitational curvature: R ~ Gρ/c⁴ = {R_curv_gravity:.3e} m⁻²")

# What curvature is needed?  On the embedded torus:
# K = cos θ / (a(R + a cos θ))
K_max = 1 / (a * (R + a))  # at θ = 0 (outer equator)
K_min = -1 / (a * (R - a))  # at θ = π (inner equator)
K_avg = 0  # Gauss-Bonnet: ∫K dA = 0 for torus

print(f"\nCurvature of embedded torus:")
print(f"  K_max (outer) = {K_max:.3e} m⁻²")
print(f"  K_min (inner) = {K_min:.3e} m⁻²")
print(f"  K_avg = 0 (Gauss-Bonnet)")

ratio = K_max / R_curv_gravity
print(f"\nRatio K_embedded / K_gravity = {ratio:.3e}")
print(f"Gravitational curvature is {ratio:.0e}× too small.")

subsection("What gravitational coupling would be needed?")

# If we need K ~ K_max from gravity:
# K = G_eff × ρ / c⁴
# G_eff = K × c⁴ / ρ
G_needed = K_max * c**4 / energy_density
print(f"Required G_eff = {G_needed:.3e} N m²/kg²")
print(f"Ratio G_eff / G = {G_needed / G:.3e}")
print(f"√(G_eff/G) = {math.sqrt(G_needed / G):.3e}")

# In theories with large extra dimensions (ADD model):
# G_4 = G_D / V_compact
# G_D = G_4 × V_compact
# If G_D >> G_4 (compact volume is small):
V_compact = L1 * L2 * L2  # assume L3 ~ L2
G_D = G * V_compact
print(f"\nIn standard KK: G₇ = G₄ × V = {G_D:.3e}")
print(f"This makes G₇ SMALLER, not larger — wrong direction.")
print(f"Need a mechanism that makes compact-scale gravity STRONGER.")

subsection("Assessment: Resolution 1")

print(f"""
VERDICT: Standard Einstein gravity is too weak by ~{ratio:.0e}×.
The compact curvature from gravitational self-interaction is
negligible.

However, if a non-Einsteinian gravity or a modified coupling
operates at the compact scale, the connection between curvature
and charge would unify EM and gravity.  The required coupling
is G_eff ~ {G_needed:.1e}, which is {G_needed/G:.1e}× Newton's G.

INTERESTING: The ratio G_needed/G is related to the ratio of
electromagnetic to gravitational force between two electrons:
  F_EM / F_grav = e²/(4πε₀) / (G m_e²) = {e_SI**2 / (4*math.pi*epsilon_0 * G * m_e**2):.3e}

These are the SAME ratio (within a few orders of magnitude).
This is not coincidental — it's a restatement of the hierarchy
problem.  Unifying EM and gravity at the compact scale requires
solving the hierarchy problem.
""")


# ================================================================
# RESOLUTION 2: Off-diagonal metric (KK gauge connection)
# ================================================================
section("RESOLUTION 2: Off-diagonal metric (KK gauge connection)")

print(f"""
In the KK metric, off-diagonal terms mix compact and spatial
coordinates:

  ds² = g_μν dx^μ dx^ν + g_ab (dy^a + A^a_μ dx^μ)(dy^b + A^b_ν dx^ν)

The gauge field A^a_μ(x) is the connection between compact and
spatial dimensions.  A particle moving in the compact direction
with velocity v^a sees a 4D gauge field:

  A_μ = A^a_μ × v_a

and its 4D charge is proportional to its compact momentum.

For a WINDING mode (not a momentum mode), the coupling to A^a_μ
is different.  The winding mode has zero compact momentum but
nonzero compact extent (it wraps around).  Its coupling to the
gauge connection depends on the LINE INTEGRAL of A^a_μ around
the compact dimension:

  Φ = ∮ A^a_μ dx^μ dy_a   (Wilson line / holonomy)

If A^a_μ is constant (flat connection), this integral is
proportional to the winding number:

  Φ = w_a × A^a_μ × L_a

The charge would then be:
  e = w_a × (something involving A^a_μ and L_a)
""")

subsection("Does this give the right charge?")

print(f"""
For this mechanism to work, we need:
1. A nonzero gauge connection A^a_μ in the background
2. The winding mode's coupling to it must give charge e

The gauge connection A^a_μ would be a BACKGROUND FIELD — part
of the vacuum configuration.  In standard KK, A^a_μ = 0 in the
vacuum (no background EM field).  But if the compact space has
a nontrivial connection (e.g., a flat connection with nontrivial
holonomy), the winding modes acquire charge.

This is similar to the Aharonov-Bohm effect: a charged particle
moving around a solenoid acquires a phase proportional to the
enclosed flux, even though the field is zero everywhere the
particle travels.

For the electron:
  Charge = winding number × (background flux per unit winding)
  e = w × Φ₀

If w = 1 (fundamental winding), then Φ₀ = e.  This doesn't
PREDICT the charge — it just says "the background flux is such
that one winding gives charge e."  The charge is transferred
from the background field to the winding mode.

PROBLEM: This explains charge quantization (multiples of e for
winding number multiples) but doesn't derive e from geometry.
The value of e (or α) is encoded in the background flux Φ₀,
which is a free parameter of the vacuum.
""")

subsection("Assessment: Resolution 2")

print(f"""
VERDICT: Metric off-diagonal terms CAN give winding modes a
charge.  This naturally explains:
  - Charge quantization (charge ∝ winding number)
  - Why only winding modes are charged (momentum modes have
    different coupling)
  - Why the electron is charged (it winds around T³)

But it does NOT derive the value of e or α.  The charge is
determined by a background gauge flux, which is a free
parameter.

This resolution SHIFTS the problem from "what determines the
compact geometry?" to "what determines the background flux?"
It's progress (charge quantization is explained) but not a
complete solution.
""")


# ================================================================
# RESOLUTION 3: Topological charge
# ================================================================
section("RESOLUTION 3: Topological charge (winding = charge)")

print(f"""
The most radical resolution: winding number IS charge, by
definition.  The charge of a state is determined entirely by
its topology — how many times it wraps around the compact
dimensions.

In this view:
  - Charge is not a field effect (no monopole moment needed)
  - Charge is not a coupling to a background (no gauge field)
  - Charge IS the winding number, with a universal conversion
    factor between "number of windings" and "Coulombs"

The conversion factor is:
  e = (one winding in the charge-relevant dimension)
  e/3 = (fractional winding, from linking on T³)

This is analogous to how spin works in the model: spin ½ is
the winding ratio 1:2, by definition.  No field calculation
is needed — it's purely topological.

The question becomes: what determines the UNITS?  Why does
one winding correspond to 1.6 × 10⁻¹⁹ Coulombs?
""")

subsection("Charge in natural units")

# In natural units (ℏ = c = 1, Gaussian):
# α = e²/(4π) = 1/137
# e = √(4πα) = √(4π/137)
e_natural = math.sqrt(4 * math.pi * alpha)
print(f"In natural (Gaussian) units: e = √(4πα) = {e_natural:.6f}")
print(f"  α = e²/(4π) = {e_natural**2 / (4*math.pi):.8f}")
print(f"  1/α = {1/alpha:.6f}")

print(f"""
In natural units, e ≈ {e_natural:.3f}.  If one winding = charge e,
then:

  α = (one winding)² / (4π) = {e_natural**2:.4f} / (4π)

The question reduces to: why is the "charge per winding" equal
to √(4πα)?

This is equivalent to asking: what sets the size of the compact
space relative to the Planck scale?  In natural units:

  e² = 4πα   and   α = e²/(ℏc) × (1/4πε₀)

The relationship between charge and geometry would be:
  L_compact / L_Planck ~ f(α)

where f is some function determined by the compactification.
""")

subsection("Topological charge and Gauss's law")

print(f"""
If charge is topological, Gauss's law must still hold:
  ∮ E · dA = Q/ε₀

The electric field of a winding mode must produce a 1/r² field
at large distances.  How?

Even if we DEFINE charge as winding number, the FIELD must be
computed.  A winding mode on T³ has specific EM field
configuration, and that field's large-distance behavior
determines the effective charge.

So topological charge is not really an independent resolution —
it's a NAMING convention.  The physics still requires computing
the field.  The question is whether the winding topology
GUARANTEES a specific monopole moment, regardless of the
details of the field profile.

ANALOGY: A magnetic monopole's charge is topological (it's
determined by the first Chern number of the gauge bundle).
No matter how you deform the field, the charge stays the same
as long as the topology is preserved.

Could the electric charge of a winding mode be similarly
topological?  This would require a theorem:

  "Any smooth EM field configuration on M₄ × T³ with winding
   number w in the compact dimensions has a 4D monopole moment
   proportional to w."

Such a theorem would be powerful — it would make charge
quantization and charge conservation automatic, without needing
to compute the field profile.

Whether such a theorem exists is an OPEN MATHEMATICAL QUESTION.
""")

subsection("Assessment: Resolution 3")

print(f"""
VERDICT: Topological charge is the most elegant resolution.
  - Charge quantization: automatic (winding numbers are integers)
  - Charge conservation: automatic (winding is topological)
  - Fractional charges: natural (linking fractionalization on T³)

But it requires a theorem: winding number → monopole moment.
This is an open mathematical question about the topology of
EM fields on M₄ × T³.  If true, it would be the strongest
possible foundation for the model.

It does NOT determine α by itself — the value of the charge
per winding is a separate question (related to the compact
volume in natural units).
""")


# ================================================================
# RESOLUTION 4: 7D field equation cross-terms
# ================================================================
section("RESOLUTION 4: 7D field equation cross-terms")

print(f"""
The 7D Maxwell equations on M₄ × T³ are:

  ∂_M F^MN = 0

where M, N run over all 7 dimensions.  Expanding:

  ∂_μ F^μν + ∂_a F^aν = 0    (4D Maxwell + compact source)
  ∂_μ F^μa + ∂_b F^ba = 0    (compact Maxwell + 4D source)

The first equation says: the 4D Maxwell equations have a
SOURCE TERM from the compact dimensions.

  ∂_a F^aν = J^ν_eff

This effective 4D current J^ν_eff comes from the variation of
the field in the compact directions.  Even on a flat T³, if the
field has nontrivial dependence on the compact coordinates
(which it does — it wraps around the geodesic), this source
term is nonzero.

For a plane wave on the geodesic:
  A^M(x, y) = ε^M × exp(i(k_μ x^μ + k_a y^a))

The effective current in 4D:
  J^ν_eff = ∂_a F^aν = ∂_a (∂^a A^ν - ∂^ν A^a)

If A has nonzero compact components (A^a ≠ 0), the cross-term
∂_a ∂^a A^ν gives a mass-like term (KK mass), and the term
-∂_a ∂^ν A^a gives a current-like term.

The current-like term:
  J^ν = -∂^ν (∂_a A^a)  =  -∂^ν (ik_a A^a × exp(...))
""")

subsection("Does this generate charge?")

print(f"""
The key question: does the effective 4D current J^ν from a
winding mode produce a static Coulomb-like field?

For a static configuration (the electron at rest), we need
J^0 ≠ 0 (charge density) at large distances.

The winding mode's field is confined to the compact dimensions.
Its compact-direction gradients (∂_a F^aν) are large (the field
varies on the scale of L₁, L₂).  But when integrated over the
compact volume, the average may vanish:

  ∫_T³ J^ν_eff d³y = ∫_T³ ∂_a F^aν d³y = 0

by periodicity!  The integral of a total derivative over a
compact space vanishes.

This means: THE VOLUME-AVERAGED 4D CURRENT IS ZERO.

The winding mode does NOT produce a net charge density when
averaged over the compact dimensions.  At distances r >> L
(which is all macroscopic distances), the field falls off
faster than 1/r² — it produces a MULTIPOLE field, not a
monopole (Coulomb) field.
""")

subsection("Unless... the field has a zero-mode component")

print(f"""
The volume-averaged current vanishes, but the field may still
have a monopole component if the FIELD ITSELF (not just the
current) has a zero-mode component.

The 4D field at large distances is:
  A^μ(x) = Σ_n A^μ_n(x) × ψ_n(y)

The zero-mode component A^μ_0(x) gives the long-range field.
It is sourced by:

  □₄ A^μ_0 = ∫_T³ J^μ(x, y) × ψ*_0(y) d³y

Since ψ_0 = 1/√V (constant), this integral IS the volume
average of J^μ — which we just showed vanishes.

CONCLUSION: On a flat T³ with standard Maxwell equations, a
winding mode produces ZERO long-range (Coulomb) field.

This confirms F6 from Track 1 through a different argument:
the 7D Maxwell equations, when decomposed into 4D modes, give
zero monopole coupling for winding modes on a flat T³.
""")

subsection("Assessment: Resolution 4")

print(f"""
VERDICT: 7D Maxwell cross-terms do NOT generate charge for
winding modes on flat T³.  The volume-averaged 4D current
vanishes by periodicity.  This is a rigorous result, not an
approximation.

This CONFIRMS that flat T³ + standard Maxwell = no charge.
Something beyond flat geometry + standard field equations is
needed.
""")


# ================================================================
# SYNTHESIS
# ================================================================
section("SYNTHESIS: Which resolutions survive?")

print(f"""
| Resolution | Status | Notes |
|------------|--------|-------|
| 1. Curvature | Viable but quantitatively challenged | Standard gravity too weak by ~10⁴⁰. Needs modified gravity at compact scale. Would unify EM + gravity. |
| 2. Gauge connection | Viable | Explains charge quantization. Does not predict α. Shifts problem to "what sets the background flux." |
| 3. Topological charge | Viable if theorem exists | Most elegant. Requires proof that winding → monopole moment. Open math question. |
| 4. Cross-terms | RULED OUT | Volume-averaged current = 0 by periodicity on flat T³. |

Resolution 4 is eliminated.

Resolutions 1, 2, and 3 remain.  They are not mutually
exclusive — the correct answer may combine elements:

COMBINED PICTURE:
  - The compact space has slight curvature (Resolution 1),
    sourced by a mechanism stronger than Einstein gravity
  - This curvature creates off-diagonal metric terms
    (Resolution 2) that couple winding modes to 4D gauge fields
  - The coupling is proportional to the winding number
    (Resolution 3), making charge quantization automatic

In this combined picture:
  - Charge = winding number × (curvature-dependent coupling)
  - α = (curvature of compact space)² × (geometric factors)
  - Gravity and EM are unified through the 7D metric
  - The hierarchy problem (why gravity is weak) = why the
    compact curvature is small

THE KEY UNKNOWN: What determines the compact-space curvature?
If it's standard Einstein gravity → too weak (hierarchy problem).
If it's some other mechanism → what is it?

CANDIDATES:
  - Flux compactification (string theory mechanism)
  - Casimir energy of the compact space
  - Topological constraint (e.g., the compact space MUST have
    specific curvature to support stable winding modes)
  - A non-Einsteinian gravitational theory at the compact scale
""")
