# R37. Membrane mechanics — gravity, stability, and α from the T²/R³ interface

**Status:** Draft — awaiting review
**Questions:** Q2 (curved appearance), Q18 (deriving α), Q76 (metric
signature)
**Type:** theoretical + compute
**Depends on:** R19 (shear-charge), R26 (T⁶), R17 (radiation pressure),
R18 (torus stiffness), R31 (origin of α), R35 (elastic torus hypothesis)
**Supports:** Paper 4 candidate (universe-as-mode)

---

## Motivation

General relativity states that mass-energy curves spacetime.
Einstein's field equation

    G_μν = (8πG / c⁴) T_μν

relates curvature (G_μν) to stress-energy (T_μν) and has been
verified to extraordinary precision.  But the equation is
**postulated, not derived**.  It says THAT energy produces
curvature and by HOW MUCH, but never says WHY.  The mechanism
by which a lump of energy deforms the surrounding geometry is
not provided — it is taken as axiomatic.

In the T⁶ framework, matter IS geometry: the electron is a
standing electromagnetic wave (photon) confined on a compact
T² surface.  The mass m_e c² is the photon's field energy.
The T² surface sits at the boundary between compact dimensions
and non-compact R³ — a physical **interface** through which the
photon's fields partially extend.  The E field projects
perpendicular to this surface into R³ (producing charge), while
the B field remains tangent (producing the magnetic dipole).

This study asks: does the photon's confinement on T² exert a
measurable force on the T²/R³ interface?  If so, does the
interface's elastic response:

1. **Stabilize the particle** — radiation pressure balanced
   against membrane tension sets the torus dimensions?
2. **Produce gravity** — the membrane deformation propagates
   into R³ as spacetime curvature?
3. **Determine α** — the shear of the lattice is the
   membrane's tangential deformation under load?

If all three follow from the same membrane mechanics, then
mass, charge, and gravitational coupling are not independent
facts — they are three aspects of a single force balance at
the compact/non-compact interface.


## Background

### Prior results on related mechanisms

**R17 (radiation pressure):** Computed the centrifugal force
from the photon's curved 3D path.  Found that the force is
perpendicular to velocity (no clumping), width-breathing is
conservative, and φ-symmetry is preserved.  Centrifugal
force is a consequence of confinement, not a mechanism for
charge.  **R17 looked at forces ALONG the torus surface.**
This study looks at forces NORMAL to the surface — pressure
on the T²/R³ boundary itself.

**R18 (torus stiffness):** Tested whether the photon's EM
field could deform the torus shape and break the φ-symmetry
that protects zero charge.  Found that axisymmetric
deformation preserves φ-symmetry → charge remains zero, and
the Coulomb energy cost exceeds the photon energy saving by
96×.  The symmetric torus is stable against shape
deformation.  **R18 asked whether the photon deforms the
torus.** This study asks whether the photon deforms R³
through the torus boundary — a different target.

**R31 (origin of α):** Systematically tested mechanisms for
deriving α.  Hydrogen is NOT a T⁶ mode.  Casimir energy has
no minimum.  KK Yukawa corrections are 10³–10⁶× too large.
α remains an input; deriving it requires dynamics or a moduli
potential.  **The membrane stiffness proposed here IS a
candidate moduli potential.**

**R35 (elastic torus, Hypothesis I):** Track 3 found that a
flat T⁶ blocks both reading and writing to the neutrino
sheet — the shielding is symmetric.  The resolution was
Hypothesis I: the torus geometry is NOT rigid but deformable.
Geometric modulation (metric fluctuations) bypasses the
three-layer protection, enabling I/O.  The Goldilocks
parameter shifted from cross-shear σ_eν to **metric
stiffness K** (F18).  **This study provides the physics
behind K.**

**R36 (geometric tilt):** Found that KK gauge fields EMERGE
from solving the wave equation on compact × non-compact
space (F8).  They are not an external assumption.  A constant
tilt (Wilson line) has zero field strength (F4).  Interactions
require SPATIALLY VARYING metric cross-terms.  **The membrane
deformation proposed here would produce spatially varying
metric components — exactly what R36 showed is needed for
interactions to exist.**


### The standard physics picture

In GR, the relationship between matter and geometry is:

    Matter (T_μν)  →  [field equation]  →  Geometry (G_μν)

Matter and geometry are ontologically separate.  You specify
the matter content, then solve for the curvature.  The
constant κ = c⁴/(8πG) ≈ 4.8 × 10⁴² N is the "stiffness of
spacetime" — the conversion factor between stress-energy
density and curvature.  It is enormous, meaning spacetime is
extremely rigid.  GR provides no explanation for this value.

In the T⁶ picture, matter IS geometry (compact-dimension
modes).  The field equation should become a self-consistency
condition: the compact geometry (which constitutes the
particle) must be consistent with the non-compact geometry
(which constitutes gravity).  There is no external "matter"
to insert — everything is geometry, and gravity is the
requirement that the total geometry be globally self-consistent.


### The membrane picture

A circularly polarized photon confined on T² is a photon
bouncing inside a resonant cavity.  The cavity walls are the
T²/R³ interface — the boundary between compact and non-compact
dimensions.

**Radiation pressure.** A confined photon exerts radiation
pressure on the cavity walls.  For the electron:

    P_rad = U / V_torus ≈ m_e c² / (2πR)²a
          ≈ 8.2 × 10⁻¹⁴ J / (10⁻¹³ m)³
          ≈ 10²⁵ Pa

This is ~10¹⁰ atmospheres — an enormous internal pressure,
applied at every point on the compact surface, directed
perpendicular to the surface (into R³).

**Spacetime resistance.** If R³ has a finite resistance to
deformation, it pushes back.  The gravitational stiffness is:

    κ = c⁴ / (8πG) ≈ 4.8 × 10⁴² N

The resulting deformation of R³ around the particle:

    δg/g ~ P_rad / κ
         ~ (m_e c² / V) / (c⁴/(8πG))
         ~ G m_e / (r² c²)

This IS the Newtonian gravitational potential Φ/c² = Gm/(rc²).
The photon's radiation pressure on the compact/non-compact
boundary, balanced against spacetime stiffness, produces the
weak-field Schwarzschild metric.  The chain is:

    confined photon → radiation pressure → membrane deformation
    → R³ metric perturbation → gravitational field

No postulate is needed.  Gravity FOLLOWS from the photon's
confinement on a compact surface in a geometry that resists
deformation.


### Stability from force balance

In GR, a point particle is a singularity — there is no
internal structure, no stability mechanism.  The electron's
size is a free parameter (or zero, in the point-particle
idealization).

In the membrane picture, the particle's size is set by a
**force balance**:

| Force | Direction | Source |
|-------|-----------|--------|
| Radiation pressure | Outward (expanding T²) | Confined photon energy density |
| Membrane tension | Inward (contracting T²) | T²/R³ boundary surface energy |
| R³ curvature cost | Inward | Energy penalty for deforming R³ |

- **Too small:** Radiation pressure dominates (energy density
  ∝ 1/V → diverges as V → 0).  The photon pushes the membrane
  outward.
- **Too large:** Membrane tension and curvature cost dominate,
  pulling the surface inward (like surface tension on a soap
  bubble).
- **Equilibrium:** A specific size where forces balance.  This
  determines the torus dimensions (R, a) and therefore the
  particle mass.

If this equilibrium exists, the Compton wavelength is not a
free parameter — it is the size at which radiation pressure
balances membrane resistance.


### The shear connection — charge and α

A perfectly elastic membrane under uniform pressure deforms
symmetrically.  But the T² lattice has two independent
directions (poloidal and toroidal), and the pressure is not
isotropic — the (1,2) winding creates an anisotropic stress
pattern.  Under anisotropic stress, an elastic membrane
responds with **shear** — a tangential displacement of the
lattice.

If the equilibrium shear is determined by the pressure
balance:

    s_eq ~ P_anisotropic / K_shear

where K_shear is the membrane's shear modulus, then the
charge formula (R19)

    α = r² μ sin²(2πs) / (4π(2−s)²)

gives α as a derived quantity — determined by the ratio of
anisotropic radiation pressure to membrane shear stiffness.
Both are geometric quantities.  No free parameters.

The chain would be:

    (1,2) winding → anisotropic stress → membrane shear
    → lattice tilt s → charge Q → α

And α and G would arise from the SAME membrane mechanics:
α from the tangential (shear) response, G from the normal
(bulge) response.  They would be related through the
membrane's elastic properties (Lamé parameters or equivalent).


### Axial vs radial coupling asymmetry

The magnetic dipole and electric charge couple to R³ with
strikingly different efficiencies:

- **B (axial):** The torus symmetry axis is a fixed direction
  in R³.  The B field's axial component adds coherently around
  the torus.  No symmetry breaking needed.  The g-factor g ≈ 2
  is topological (O(1) coupling).

- **E (radial):** The outward direction ROTATES as you go
  around the torus.  E components cancel unless shear breaks
  the symmetry.  The coupling is O(s) where s ~ √α.

The fraction of E-field energy that appears as long-range
Coulomb field is O(α) ≈ 0.73%.  The rest is near-field
multipole structure confined to within a few torus radii.

In the membrane picture, this asymmetry has a mechanical
origin: the axial direction is invariant under the torus
rotational symmetry → B projects without cancellation.  The
radial direction rotates → E cancels unless the lattice is
sheared.  The shear magnitude (set by anisotropic membrane
stress) determines HOW MUCH of the E field escapes as
monopole → α.

**α is the geometric penalty for converting rotational
(tangential) field energy into radial (monopole) field
energy through membrane shear.**


## Theory

### The T²/R³ interface as an elastic membrane

Model the T²/R³ boundary as a 2D elastic membrane with:

- **Surface energy density σ_m** (energy per unit area of
  the interface — analogous to surface tension)
- **Bending rigidity κ_b** (resistance to curvature of the
  membrane — penalizes small radii)
- **Shear modulus μ_m** (resistance to tangential
  deformation of the lattice)
- **Normal stiffness K_n** (resistance to displacement of
  the membrane into R³ — related to spacetime stiffness κ)

The confined photon provides:

- **Isotropic radiation pressure P_iso = U/(2V)** — equal in
  all directions, pushes the membrane outward
- **Anisotropic stress ΔP** — the (1,2) winding pattern
  creates a stress that differs in the poloidal (θ) and
  toroidal (φ) directions

The equilibrium geometry is the solution to:

    P_iso + ΔP(θ,φ) = σ_m H + κ_b ΔH + μ_m s + K_n δn

where H is the mean curvature, ΔH is the curvature
variation, s is the shear strain, and δn is the normal
displacement.


### Connection to known physics

**The Israel junction conditions** (1966) provide the exact
GR treatment of a hypersurface separating two spacetime
regions.  The stress-energy on the surface is related to the
discontinuity in the extrinsic curvature K_ab:

    S_ab = −(1/8πG) ([K_ab] − [K] h_ab)

where [K_ab] is the jump in extrinsic curvature across the
membrane, [K] is its trace, and h_ab is the induced metric.

In the T⁶ framework, the T² surface is precisely such a
hypersurface: it separates the compact interior from the
non-compact exterior.  The Israel conditions applied to this
surface would give the membrane stress-energy tensor in terms
of the metric jump.

**The Randall-Sundrum model** (1999) is a brane-world scenario
where our universe is a 3-brane (membrane) in a
5-dimensional bulk.  The brane tension relates to the
cosmological constant.  The T² membrane is an analogous
structure at particle scale — a 2-brane separating compact
and non-compact dimensions.

**The Nambu-Goto action** describes a membrane (string, brane)
whose dynamics minimizes surface area.  Applied to the T²
surface:

    S_membrane = −σ_m ∫ √|det h_ab| d²ξ

where h_ab is the induced metric on the T² surface.  This
gives the surface tension contribution to the force balance.


### What the membrane stiffness IS

The key unknown is K_n — the normal stiffness of the T²/R³
interface.  Several candidates:

1. **Planck stiffness.** K_n = c⁴/(8πG) per unit area.
   This identifies the membrane stiffness with GR's spacetime
   stiffness, giving a direct connection to the gravitational
   constant.

2. **KK moduli potential.** In KK theory, the compact
   dimensions have "moduli" — continuous parameters (like R, a,
   s) not fixed by the equations of motion on a flat torus.
   A moduli potential V(R, a, s) would provide forces
   stabilizing these parameters.  The membrane stiffness
   IS the second derivative of this potential:
   K_n = ∂²V/∂(δn)².

3. **Casimir energy.** The quantum vacuum energy of the
   confined photon field on T² depends on the torus geometry.
   Casimir forces between the compact walls could provide a
   restoring force.  R31 found no minimum in the Casimir
   energy as a function of geometry — but that calculation
   used a flat T² without the normal displacement degree of
   freedom.  Including the T²/R³ interface as a dynamical
   surface may change this.

4. **Higher-dimensional Einstein equations.** If the full
   10D geometry (T⁶ × R³ × R¹) satisfies the 10D Einstein
   equations, the compactification itself provides forces on
   the T² surfaces.  The requirement of self-consistency
   (10D Ricci flatness, or a specific cosmological constant)
   could determine K_n.


## Approach

### Track 1. Radiation pressure on the T² surface

**Goal:** Compute the stress tensor of the confined (1,2)
photon mode on the T² surface.  Decompose it into isotropic
pressure, anisotropic shear stress, and the normal force on
the T²/R³ boundary.

**Method:**
1. Write the (1,2) mode's E and B fields on the T² surface
   using the known mode functions from R19/R26.
2. Compute the Maxwell stress tensor T_ij at the surface.
3. Decompose into:
   - P_iso: isotropic pressure (drives expansion/contraction)
   - ΔP(θ,φ): anisotropic part (drives shear)
   - T_nn: normal-normal component (drives R³ deformation)
4. Evaluate numerically for the electron (m_e c², r = 1–9,
   KK Compton constraint).

**Output:**
- P_iso, ΔP, T_nn as functions of position on the T² surface
  and aspect ratio r
- The force per unit area on the T²/R³ boundary
- Whether the stress is predominantly normal (bulge) or
  tangential (shear)

**Script:** `scripts/track1_radiation_stress.py`


### Track 2. Force balance and particle stability

**Goal:** Determine whether a stable equilibrium exists where
photon radiation pressure balances membrane tension and R³
stiffness.

**Method:**
1. Model the total energy as a function of torus dimensions
   (R, a) and normal displacement δn:

       E_total(R, a, δn) = E_photon(R, a)
                         + E_surface(R, a)
                         + E_curvature(R, a, δn)

   where:
   - E_photon = hc/L_geodesic (decreases with larger torus)
   - E_surface = σ_m × A_torus (increases with larger torus)
   - E_curvature = ½ K_n δn² × A_torus (penalty for R³
     deformation)

2. Find extrema: ∂E/∂R = ∂E/∂a = ∂E/∂(δn) = 0.
3. Check stability: the Hessian matrix of second derivatives
   must be positive definite (all eigenvalues > 0).
4. If a stable equilibrium exists, read off the predicted
   torus dimensions (R_eq, a_eq) and compare to the known
   Compton-scale values.

**Success criterion:** An equilibrium exists at R ~ λ̄_C with
physical values of σ_m and K_n.

**Script:** `scripts/track2_force_balance.py`


### Track 3. Gravity from normal deformation

**Goal:** Compute the R³ metric perturbation produced by the
membrane's normal displacement.  Check whether it reproduces
the weak-field Schwarzschild metric.

**Method:**
1. Treat the T² surface as a thin shell with stress-energy
   S_ab determined by Track 1.
2. Apply the Israel junction conditions to compute the
   extrinsic curvature jump [K_ab] across the surface.
3. Match to the exterior Schwarzschild metric at large r:

       g_00 ≈ −(1 − 2Gm/(rc²))
       g_rr ≈ 1 + 2Gm/(rc²)

4. Check: does the total stress-energy on the T² surface
   give the correct ADM mass m = m_e?

**Output:**
- The gravitational field of the electron, derived from
  membrane mechanics (not postulated).
- Whether the Newtonian potential Gm/r emerges naturally.
- The relationship between membrane stiffness K_n and G:
  is K_n = c⁴/(8πG)?

**Script:** `scripts/track3_gravity_from_membrane.py`


### Track 4. Shear from anisotropic stress → α

**Goal:** Determine whether the anisotropic stress from the
(1,2) winding pattern produces an equilibrium shear that
matches the value needed for α = 1/137.

**Method:**
1. From Track 1, extract the anisotropic stress ΔP(θ,φ)
   on the T² surface.
2. Model the T² lattice as an elastic sheet with shear
   modulus μ_m.  Under the anisotropic stress, the lattice
   deforms:

       s_eq = ΔP / μ_m

3. Substitute s_eq into the KK α formula (R19 F35):

       α = r² √(1/r² + (2−s)²) sin²(2πs) / (4π(2−s)²)

4. Solve for the shear modulus μ_m that gives α = 1/137.
5. Check: is this μ_m related to K_n (from Track 2/3) by
   a known elasticity relationship (e.g., μ = K/(2(1+ν))
   for Poisson ratio ν)?

**Success criterion:** A single membrane with two elastic
constants (K_n, μ_m) related by a Poisson ratio simultaneously
produces:
- Correct particle size (Compton wavelength)
- Correct gravitational field (G)
- Correct electric charge (α = 1/137)

If the Poisson ratio is determined by the T² topology (e.g.,
ν = 1/3 for a 2D membrane in 3D), then G and α are related
through a single elastic constant with no free parameters.

**Script:** `scripts/track4_shear_from_stress.py`


### Track 5. Relationship between α and G

**Goal:** If Tracks 2–4 succeed, extract the predicted
relationship between α and G.

**Method:**
1. From Track 3: K_n determines G via K_n = c⁴/(8πG).
2. From Track 4: μ_m determines α via the shear mechanism.
3. The ratio K_n/μ_m is related to the membrane's Poisson
   ratio ν:

       K_n / μ_m = 2(1 + ν)   (for 2D isotropic elasticity)

4. Substituting:

       G / α = f(ν, r, topology)

   where f is a computable function.

5. Compare to the known ratio:

       G m_e² / (ℏc) ≈ 1.75 × 10⁻⁴⁵

   which is the gravitational coupling constant.  In this
   picture, this ratio is not a coincidence — it is set by the
   membrane's elastic properties.

**Output:**
- The predicted α/G ratio as a function of Poisson ratio ν
  and aspect ratio r
- Whether any physically reasonable (ν, r) reproduces the
  observed ratio
- If so: a derivation of the hierarchy problem (why gravity
  is 10⁴⁰× weaker than electromagnetism) from membrane
  elasticity


## What success looks like

- **Strong result:** A single elastic membrane with
  computable constants simultaneously gives particle
  stability, gravity, and α.  The hierarchy problem
  (G ≪ α) reduces to the membrane's Poisson ratio.

- **Moderate result:** The force balance works
  qualitatively — stable equilibrium exists — but the
  predicted α or G are orders of magnitude off.  This
  would suggest the membrane picture is correct but the
  elastic model is too simple (need non-linear elasticity,
  quantum corrections, or additional membrane physics).

- **Null result:** No stable equilibrium exists, or the
  membrane deformation produces no coupling to R³.  This
  would rule out the mechanical membrane picture and
  push toward the "designer's-choice" hypothesis for α
  (R36 conclusion).

- **Breakthrough:** The relationship between α and G is
  derived with no free parameters.  The gravitational
  hierarchy is explained.  The measured G and α are the
  unique self-consistent solution of the membrane
  mechanics.


## Relationship to the universe-as-mode hypothesis

The universe-as-mode thought piece
([`papers/universe-as-mode.md`](../../papers/universe-as-mode.md))
proposes that each particle's T⁶ fiber acts as a local
"frame-of-reference computer" managing energy propagation.
The membrane mechanics studied here provides the PHYSICS
behind that picture: the fiber computes by applying the
membrane's elastic response to incoming field configurations.
Gravity is the fiber's normal response.  Charge is the
fiber's shear response.  The "computation" is the physical
process of membrane equilibration.

If the membrane's elastic constants are ultimately set by
a self-consistency condition (the T⁶ × R³ × R¹ geometry
satisfying the 10D Einstein equations), this connects to
the self-referential closure in section 7 of the thought
piece: the constants are what they are because no other
values make the membrane mechanics self-consistent.
