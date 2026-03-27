# R37. Membrane mechanics — gravity and stability from the T²/R³ interface

**Status:** Draft
**Questions:** Q2 (curved appearance), Q76 (metric signature)
**Type:** theoretical + compute
**Depends on:** R19 (shear-charge), R26 (T⁶), R17 (radiation pressure),
R18 (torus stiffness), R31 (origin of α), R35 (elastic torus hypothesis),
R36 (geometric tilt — interactions require spatially varying metric)
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

α remains an input (R31 conclusion), not derived here.  But
α determines the membrane's shear modulus μ_m (via the
R19 charge formula), while the gravitational response
determines the normal stiffness K_n.  The ratio K_n/μ_m
then quantifies the gravitational hierarchy — why gravity
is ~10⁴⁰× weaker than electromagnetism — in mechanical terms.

If gravity follows from the same membrane that produces
charge, then the Einstein field equation is not a postulate
but a consequence of photon confinement on a compact surface.


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
α remains an input.  **This study accepts R31's conclusion:
α is an input, not derived.**  But α determines the
membrane's shear modulus μ_m, which combined with the
independently determined K_n (from gravity) gives a
mechanical characterization of the hierarchy.

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


### The shear connection — α as input, μ_m as output

The (1,2) winding creates an anisotropic stress pattern on
the T² surface.  This stress has a shear component ΔP that
deforms the lattice tangentially.  The equilibrium shear is:

    s_eq = ΔP / μ_m

where μ_m is the membrane's shear modulus.  The R19 charge
formula relates shear to α:

    α = r² μ sin²(2πs) / (4π(2−s)²)

**α is an observed input, not derived here** (per R31).
The known value α = 1/137 fixes the required shear s_eq.
Track 1 computes the anisotropic stress ΔP.  Together they
**determine μ_m**:

    μ_m = ΔP / s_eq(α)

This is the key inversion: α tells us how compliant the
membrane is to tangential deformation.  The normal stiffness
K_n is independently determined by requiring the correct
gravitational field (Track 3).  The ratio K_n/μ_m then
characterizes the hierarchy between gravity and
electromagnetism in purely mechanical terms.

The two elastic responses arise from the same membrane but
involve deformation in different directions: tangential (on
T²) for charge, normal (into R³) for gravity.  These probe
different sectors of the total geometry, so K_n/μ_m need not
be O(1) — the hierarchy K_n ≫ μ_m would mean the T²/R³
boundary is extremely rigid against normal displacement
(making gravity weak) but compliant to tangential shear
(allowing appreciable charge).


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

### Fiber vs. bubble — what the "membrane" is

The T² is not a soap bubble floating in R³.  It is a compact
fiber over each point of R³: at every spatial location, there
exist 2 compact coordinates (θ, φ) in addition to the 3
non-compact coordinates (x, y, z).  The "T²/R³ interface" is
the boundary in the total 5D space between the compact and
non-compact sectors — a codimension boundary, not a spatial
surface.

The Israel junction conditions handle exactly this situation:
a hypersurface in a higher-dimensional spacetime separating
two regions with potentially different geometries.  The
formalism is rigorous even though the "membrane" is not a
surface you could point to in R³.  What makes it physical
is that the photon's field configuration on T² creates
stress-energy AT the boundary, and this stress-energy
affects the geometry on both sides.


### Parameter counting

The membrane has 3 independent elastic parameters:

| Parameter | Controls | Determined by |
|-----------|----------|---------------|
| σ_m (surface energy) | Equilibrium torus size (R, a) | Track 2: force balance → R_eq ~ λ̄_C |
| K_n (normal stiffness) | Gravitational coupling G | Track 3: Israel conditions → K_n = c⁴/(8πG) |
| μ_m (shear modulus) | Charge coupling α | Track 4: α (input) + ΔP (Track 1) → μ_m = ΔP/s_eq |

3 unknowns, 3 observables (R_eq, G, α).  The system is
exactly determined — no free parameters once the inputs
(α, G, λ̄_C) are specified.  The bending rigidity κ_b is
derived from σ_m and the membrane thickness (or topology)
via thin-shell theory.

The non-trivial output is NOT the values of (σ_m, K_n, μ_m)
— those are fixed by the inputs.  The non-trivial outputs
are:
1. Does a stable equilibrium EXIST? (Track 2)
2. Does the normal deformation reproduce the Schwarzschild
   metric, not just the right G? (Track 3)
3. What is K_n/μ_m, and does it match the hierarchy? (Track 5)


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


### Track 4. Shear modulus from α (input) and anisotropic stress

**Goal:** Given α = 1/137 as input, extract the membrane's
shear modulus μ_m from the anisotropic stress computed in
Track 1.  Compare μ_m to K_n (from Track 3) to quantify the
gravitational hierarchy in mechanical terms.

**Method:**
1. From Track 1, extract the anisotropic stress ΔP(θ,φ)
   on the T² surface.
2. From the R19 charge formula, the known α fixes the
   required shear: s_eq ≈ 0.0116 (at r = 6.6).
3. Extract the shear modulus:

       μ_m = ΔP / s_eq

4. From Track 3: K_n = c⁴/(8πG) determines G.
5. Compute the hierarchy ratio:

       K_n / μ_m = ?

   If this ratio reproduces the known gravitational
   hierarchy (~10¹⁴ or similar large number), the hierarchy
   problem has a mechanical interpretation: the T²/R³
   boundary is extremely rigid against normal deformation
   (weak gravity) but compliant to tangential shear
   (appreciable charge).

**Key point:** K_n and μ_m involve deformation in different
directions (normal into R³ vs. tangential on T²).  These
probe different sectors of the total geometry, so the ratio
is NOT constrained by 2D isotropic elasticity (no Poisson
ratio applies).  A large ratio would be a feature, not a bug.

**Output:**
- μ_m in natural units
- K_n/μ_m ratio
- Whether the ratio matches the known hierarchy
- Physical interpretation: what property of the T²/R³
  interface makes it rigid normally but soft tangentially?

**Script:** `scripts/track4_shear_from_stress.py`


### Track 5. The hierarchy in mechanical terms

**Goal:** Synthesize Tracks 2–4 into a coherent mechanical
picture of the gravitational hierarchy.

**Method:**
1. From Track 3: K_n = c⁴/(8πG) ≈ 4.8 × 10⁴² N.
2. From Track 4: μ_m = ΔP/s_eq (computable once Track 1
   gives ΔP).
3. Compute the hierarchy ratio K_n/μ_m.  If it matches the
   known gravitational hierarchy Gm_e²/(ℏc) ≈ 10⁻⁴⁵, then
   the hierarchy is the statement:

       "The T²/R³ boundary is 10¹⁴× more rigid against normal
       deformation than against tangential shear."

4. Ask WHY the normal and tangential responses are so
   different.  Candidate explanations:
   - Normal deformation requires deforming ALL of R³
     (long-range, integrated over infinite volume →
     enormous effective stiffness).  Tangential shear
     is LOCAL to the T² surface (finite area → moderate
     stiffness).
   - The topology of T² may protect tangential modes
     (soft directions in the moduli space) while normal
     modes are fully constrained by the Einstein equations
     in 10D.

5. Check whether the R35 Goldilocks compliance K ∈
   [0.043, 0.080] eV⁻¹ is consistent with the membrane
   parameters.  K from R35 describes the neutrino sheet's
   geometric compliance; it should be derivable from the
   same membrane physics applied to T²_ν.

**Output:**
- K_n/μ_m ratio and whether it matches the hierarchy
- Physical interpretation of the ratio
- Connection to R35's Goldilocks K for the neutrino sheet
- Whether the membrane picture gives a mechanical
  explanation for why gravity is weak


## What success looks like

- **Strong result:** The confined photon's radiation
  pressure on the T²/R³ boundary, balanced against
  spacetime stiffness, produces the weak-field
  Schwarzschild metric — deriving the Einstein field
  equation from confinement mechanics.  α remains an
  input, but G emerges from the same membrane.  The
  hierarchy K_n/μ_m has a clear mechanical interpretation.

- **Moderate result:** The force balance gives a stable
  equilibrium — particle size is determined — but the
  gravitational field has the wrong prefactor (G off by
  orders of magnitude).  This would suggest the membrane
  picture is qualitatively correct but the elastic model
  needs refinement (non-linear effects, quantum
  corrections, or contributions from the other T² sheets).

- **Null result:** No stable equilibrium exists, or the
  normal deformation does not propagate into R³ as
  curvature.  This would rule out the mechanical membrane
  picture for gravity.

- **Bonus:** The K_n/μ_m ratio, computed from first
  principles (Track 1 stress + Israel conditions),
  reproduces the observed gravitational hierarchy
  ~10⁻⁴⁵ without additional input.  The hierarchy
  problem becomes: "the membrane is rigid normally
  because normal deformation costs R³ curvature energy
  integrated over all space, but soft tangentially
  because shear is a local T² deformation."


## Connection to R35 elastic torus

R35 Track 4 introduced the metric compliance K as the master
Goldilocks parameter for neutrino-sheet I/O, with the viable
window K ∈ [0.043, 0.080] eV⁻¹.  F28 noted that computing K
from first principles requires the moduli potential of the T⁶
geometry.

The membrane mechanics studied here IS the physics behind K.
If this study succeeds in computing σ_m, K_n, and μ_m for the
electron sheet, the same formalism applied to the neutrino
sheet should yield the neutrino-sheet compliance.  Checking
consistency with R35's Goldilocks window is a concrete
falsifiability test (Track 5).

The key difference between sheets: the electron sheet carries
a charged photon mode (high radiation pressure, large ΔP),
while the neutrino sheet carries uncharged modes (no EM
radiation pressure — the confinement mechanism and stress
pattern may be different).  This asymmetry may explain why
the neutrino sheet is more compliant (larger K, easier I/O).


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
