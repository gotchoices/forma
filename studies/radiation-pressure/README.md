# R17. Radiation Pressure Self-Consistency  *(open)*

A confined photon has momentum.  A photon on a curved path
experiences centrifugal force — this is what "having mass"
means.  The centrifugal effects modify the field distribution
on the torus, creating a non-circular tube cross-section.
That deformation breaks the azimuthal symmetry that kills
the monopole (R15 F3), potentially generating charge and
determining α.

This study computes the self-consistent field configuration
where the photon's own radiation pressure shapes the geometry
and the geometry determines the field.


## Motivation

### The two-frame picture

The model has two domains (R12 F14):

- **Inside T²:** the compact space is flat.  The photon
  propagates along a straight geodesic (no forces, no
  curvature).  Mass and spin emerge from the topology.

- **Outside in 3D:** the same compact space is embedded as a
  torus.  The (1,2) geodesic appears as a tight helix in 3D.
  The photon's electromagnetic field leaks into 3D through
  the embedding.  Charge and Coulomb energy emerge from this
  projection.

These are not two different models — they are two descriptions
of the same field, seen from inside or outside the compact
space.  Effects computed in the 3D frame can feed back into
the compact-space dynamics through the coupling between the
two domains.

### Centrifugal force on a confined photon

A photon has momentum p = E/c = ℏω/c.  Confined to a curved
path, its momentum must continuously change direction.  The
confining geometry provides the centripetal force; the reaction
is centrifugal force (radiation pressure on the "walls" of the
confining geometry).

This is not exotic physics — it is the same effect as:
- Radiation pressure in a curved waveguide (higher on the
  outside of bends)
- Gravitational lensing (photon trajectory bent by gravity)
- The equivalence principle (all energy, including light,
  responds to inertia)

In our model, the photon's confinement gives it mass (inertia).
That inertia, combined with the curved 3D path, creates
centrifugal effects.  Asking "does the confined photon feel
centrifugal force?" is equivalent to asking "does the electron
have mass?" — and the answer is obviously yes.

### Is this relativistic?

Yes.  The photon moves at c, so the centrifugal effects are
inherently relativistic.  For a photon of energy E on a path
with local radius of curvature ρ:

    F_centrifugal = E / (c × ρ) = p / ρ

At the Compton scale (ρ ~ R ~ 10⁻¹³ m), this force is
enormous: F ~ m_e c / R ~ 10⁻⁶ N.  For comparison, the
Coulomb force between two electrons at the Bohr radius is
~ 10⁻⁸ N — the centrifugal force is ~100× stronger.

### The particle-wave interpretation

R15 showed that α = exp(−4σ²), where σ is the angular width
of the photon's wavepacket.  The interpretation (confirmed
by analysis):

| Regime | σ | α | Description |
|--------|---|---|-------------|
| Pure particle | 0 | 1 | Fully localized, maximum charge |
| Actual electron | 1.1 rad | 1/137 | Partially localized |
| Pure wave | ∞ | 0 | Fully delocalized, zero charge |

In WvM's original model (pure particle), the photon is at one
point on the torus, E always points outward, and charge appears.
But this gives α = 1 (too much coupling).  The real photon is
a wave with finite extent — and the question is: what determines
that extent?

The balance-of-forces idea says: σ is set by competing effects.
Something spreads the wavepacket (quantum pressure / dispersion),
and something concentrates it.  The equilibrium determines σ
and hence α.

### Why not just quantum pressure vs. Coulomb?

A naive two-term energy functional:

    E(σ) = C₁/σ²  +  C₂ × exp(−4σ²)

has both terms DECREASING with σ — both favor delocalization.
The kinetic energy (uncertainty principle: narrow packet → high
momentum → high energy) favors spreading.  The Coulomb self-
energy (same-sign charges repelling) ALSO favors spreading.
Minimizing E(σ) gives σ → ∞ (zero charge).

This is an important negative result: the Coulomb self-interaction
is repulsive, so it cannot be the concentrating force.  Something
ELSE must provide the concentration.

### The centrifugal deformation mechanism

On the (1,2) helix, the local radius of curvature varies:

- At the OUTER equator of the torus (farthest from ring center):
  the effective radius is R + a — curvature is gentlest,
  centrifugal push is weakest.
- At the INNER equator (closest to ring center):
  the effective radius is R − a — curvature is tightest,
  centrifugal push is strongest.

The radiation pressure on the tube wall is therefore non-uniform:
higher on the inside, lower on the outside.  This is exactly
the physics of water in a curved pipe — the pressure is higher
on the outer wall of the bend.

The non-uniform pressure deforms the tube cross-section:
the field distribution is denser on the outside of the torus
(away from the ring center) where the confining "wall" is more
gently curved.  The cross-section becomes non-circular.

This deformation breaks the azimuthal symmetry — exactly what
R15 F3 identified as necessary for charge generation.  The
n = 2 mode (from the (1,2) winding) can now couple to n = 0
(the monopole / charge).  The coupling strength depends on the
magnitude of the deformation, which depends on the radiation
pressure, which depends on the photon's energy and the geometry.

### The self-consistency chain

The full chain, from photon momentum to α:

    Photon has momentum p = E/c
    → curves along (1,2) helix in 3D
    → centrifugal radiation pressure on tube wall
    → pressure is non-uniform (stronger at inner equator)
    → tube cross-section deforms (becomes non-circular)
    → azimuthal symmetry is broken
    → n = 2 mode couples to n = 0 (monopole)
    → coupling strength determines apparent charge Q
    → α = Q²/(4πε₀ℏc)

The deformation is self-consistent: the photon's energy
determines the radiation pressure, which determines the
deformation, which determines the mode coupling.  There are
no free parameters — the deformation is fixed by the photon's
own properties.

This is analogous to a star, where the equilibrium radius is
determined by the balance between thermal pressure (outward)
and gravity (inward), with both depending on the star's own
mass.

### Why the embedding already creates harmonics

Even BEFORE the centrifugal deformation, the embedding
itself creates harmonics.  A uniform wave on flat T²
(constant amplitude, constant velocity c) maps to a
non-uniform field in 3D because the metric scale factor
varies over the torus surface.

On flat T², the photon's "little Cartesian squares" are all
identical.  But on the embedded torus, the outer equator
(distance R + a from the ring center) has circumference
2π(R + a), while the inner equator has circumference
2π(R − a).  The same internal distance maps to different
3D arc lengths:

- Outer equator: each internal unit → (1 + r) units of 3D arc
- Inner equator: each internal unit → (1 − r) units of 3D arc

A photon at constant c in the flat metric appears to have
varying 3D speed:

    v_3D(θ) = c × (R + a cos θ) / R = c(1 + r cos θ)

For r = 1/2, the 3D speed oscillates between 1.5c (outer)
and 0.5c (inner).  The "superluminal" outer velocity is not
a relativity violation — it is an artifact of comparing
distances in two different metrics.

The 3D energy density transforms accordingly:

    u_3D = u_flat × R / (R + a cos θ)
         ≈ u_flat × (1 − r cos θ + r² cos²θ − ...)

A single-mode wave in flat T² becomes a multi-harmonic
pattern in 3D.  The nonlinear metric mapping generates
harmonics in the θ direction (tube cross-section) that the
flat-space wave does not have.

### Why these harmonics alone don't produce charge

On a SYMMETRIC torus, the metric distortion depends only on
θ, not on φ.  The θ-harmonics are the same at every ring
position.  The charge integral still factorizes:

    Q = ∫[θ stuff] × ∫cos(2φ) dφ = 0

More subtly: the (1,2) geodesic maps θ to φ via θ = φ/2,
so the photon visits each ring position φ on TWO passes at
complementary tube positions:

- First pass:  θ = φ/2      (e.g., outer equator at φ = 0)
- Second pass: θ = φ/2 + π  (inner equator at φ = 0)

The metric modulation on the two passes involves:
cos(φ/2) + cos(φ/2 + π) = cos(φ/2) − cos(φ/2) = 0

The two passes cancel exactly.  Every ring position gets
visited at both the "fast" and "slow" tube positions, and
the modulation averages to zero.  This is the azimuthal
symmetry reasserting itself.

### What the centrifugal deformation adds

The metric mapping is a KINEMATIC effect — pure coordinate
transformation, no dynamics.  It creates θ-harmonics but
cannot break the φ-symmetry.

The centrifugal deformation is a DYNAMIC effect — forces
reshaping the actual geometry.  It changes the tube
cross-section from circular to non-circular, modifying the
metric mapping in a way that could break the two-pass
cancellation.  On a deformed tube, the "fast" and "slow"
visits to the same ring position are no longer perfectly
complementary, because the tube shape itself has changed.

Both effects contribute to the harmonics in the 3D field:

| Effect | Creates θ-harmonics? | Breaks φ-symmetry? |
|--------|---------------------|-------------------|
| Metric mapping (kinematic) | Yes | No |
| Centrifugal deformation (dynamic) | Yes | Potentially |

The centrifugal deformation is the critical ingredient.
Without it, the monopole is exactly zero.  With it, charge
can appear — and the magnitude is determined by the
deformation, which is self-consistent (fixed by the photon's
own energy and the geometry).

### Connection to Q51 and R15 F8 candidate 6

This study is the quantitative implementation of two
converging leads:

- **Q51 (non-torus embeddings):** identified that breaking
  the tube's circular symmetry allows n = 2 → n = 0 mode
  coupling.  R17 provides the PHYSICAL MECHANISM for the
  deformation (centrifugal radiation pressure).

- **R15 F8 candidate 6 (dipole radiation pattern):** noted
  that a circularly polarized photon radiates non-isotropically,
  power ∝ (1 + cos²θ)/2.  R17 adds another source of
  deformation: even without the dipole pattern, the curvature
  of the 3D path itself creates non-uniform pressure.  Both
  effects (radiation pattern + centrifugal pressure) contribute
  to the tube deformation and may reinforce each other.


## Tracks

### Track 1. Radiation pressure distribution

Compute the radiation pressure on the tube surface for a
(1,2) helical mode at speed c.

**Method:**
1. Parametrize the (1,2) geodesic on the torus in 3D:
   x(t), y(t), z(t) with velocity |v| = c.
2. At each point, compute the local radius of curvature ρ(t).
   For a helix on a torus, ρ depends on the position (θ, φ)
   on the tube.
3. The radiation pressure at each surface point is proportional
   to the energy density times the curvature: P ∝ u / ρ.
   For a photon uniformly distributed along the path,
   u ∝ 1/(cross-section area) and ρ varies with θ.
4. Map P(θ, φ) and decompose into Fourier components.

**Key question:** is the pressure distribution φ-independent
(same everywhere around the ring) or does it vary with φ?

On a perfect torus, symmetry forces φ-independence.  The
pressure varies only with θ (position on the tube cross-section).
This deforms the cross-section uniformly around the ring —
it breaks the TUBE's circular symmetry but preserves the
RING's rotational symmetry.

**Expected output:** P(θ) for a range of aspect ratios r = a/R.

### Track 2. Tube cross-section deformation

Given the radiation pressure distribution P(θ) from Track 1,
compute the equilibrium tube shape.

**Method:**
Two possible approaches:

A. **Energy minimization:** the tube shape adjusts until the
   internal radiation pressure is balanced by the restoring
   force (from the requirement that the compact space remain
   flat — the total Gaussian curvature is zero for a flat T²,
   constraining the allowed deformations).

B. **Self-consistent field:** solve Maxwell's equations on the
   deformed torus, compute the new radiation pressure from the
   resulting field, and iterate until the field is consistent
   with the shape.

**Key constraint:** the deformed tube must still have the same
topology (T²) and the same total path length (λ_C).  The flat-
torus condition constrains the allowed deformations — not all
shapes are compatible with zero intrinsic curvature.

**Expected output:** the equilibrium tube cross-section shape
as a function of r = a/R.

### Track 3. Mode coupling from deformed cross-section

Given the deformed tube shape from Track 2, compute the
coupling between Fourier modes.

**Method:**
1. Write the (1,2) wave on the deformed torus.
2. Compute the charge density σ(θ, φ) × dA on the
   3D-embedded surface.
3. The area element dA is now θ-dependent in a different way
   than for a circular tube — the deformation changes the
   Jacobian.
4. Decompose σ × dA into Fourier modes in both θ and φ.
5. Extract the (0, 0) component — this is the monopole charge.
6. Compute α = Q²/(4πε₀ℏc).

This is the payoff calculation.  If the deformation from
Track 2 produces a nonzero (0, 0) component, we have charge
from self-consistency.  If α ≈ 1/137, we have a derivation.

**Expected difficulty:** medium-high.  The deformation
calculation (Track 2) is the hard part; once the shape is
known, the mode coupling integral is straightforward.

### Track 4. Analytical estimate

Before the full numerical calculation, attempt a perturbative
estimate.

**Method:**
1. Model the tube cross-section as a circle plus a small
   elliptical deformation: ρ(θ) = a(1 + ε cos θ), where
   ε is the deformation parameter.
2. The deformation ε is determined by the ratio of centrifugal
   pressure variation to the restoring stiffness.  For a thin
   torus (a ≪ R), ε ∝ a/R.
3. The mode coupling from (1, 2) to (0, 0) involves the
   product of the deformation (cos θ term) with the wave
   pattern (cos θ from the p = 1 winding), giving a cos²θ
   term that has a nonzero θ-average.
4. The coupling coefficient is proportional to ε.
5. α ∝ ε².

If ε ∝ a/R and α ∝ (a/R)², then fixing a/R = 1/2 (from Q52,
the "equal distance per winding" constraint) would give a
specific numerical value for α.  Check whether it matches
1/137.

**Expected difficulty:** low-medium.  This is a back-of-
envelope calculation that could confirm or rule out the
mechanism before investing in the full numerics.

**Priority:** do this FIRST.  If the perturbative estimate
gives α ~ 10⁻² for reasonable geometry, the mechanism is
viable and the full calculation is worth doing.  If it gives
α ~ 1 or α ~ 10⁻⁶, the mechanism is likely wrong.


## What would success look like?

**Tier 1 (strong):** α = 1/137 falls out of the self-consistent
radiation pressure calculation with no free parameters.  The
deformation is determined by the photon's energy, the torus
topology, and Maxwell's equations.

**Tier 2 (promising):** α comes out as a function of the
aspect ratio r = a/R.  Combined with Q52's constraint (r = 1/2
from equal distance per winding), α is determined.  Two
independent geometric constraints fix two parameters (r and α).

**Tier 3 (informative):** the mechanism produces charge but at
the wrong magnitude (α ≠ 1/137).  This would still identify
radiation pressure as the physical origin of charge and narrow
the search for corrections.

**Tier 4 (negative):** the centrifugal deformation preserves
too much symmetry (e.g., the deformation is φ-independent on
a symmetric torus, so the monopole integral still vanishes).
This would rule out the mechanism and redirect toward other
candidates (F8 candidates 1–4, or the dipole radiation pattern
as an independent effect).


## What is NOT addressed

- The anomalous magnetic moment (Q53).  The leading g = 2 is
  topology-independent (R8 Track 3).  The anomalous correction
  α/(2π) may follow from the field distribution computed here,
  but it is not a primary target.

- Higher-order QED effects (vacuum polarization, etc.).  These
  are α² or smaller and are beyond the scope of a first
  calculation.


## Connections

- **R15** — established α = exp(−4σ²) and the localization
  framework.  R17 provides the physical mechanism for σ.
- **R16** — analytical Fourier decomposition.  R17 provides
  the physical origin of the mode coupling that R16 computes
  abstractly.
- **R13** — proved that p ≠ 1 gives zero charge; established
  the monopole integral formalism.
- **Q51** — non-torus embeddings and mode coupling.  R17 is
  the quantitative calculation for the specific deformation
  caused by radiation pressure.
- **Q52** — aspect ratio r = a/R = 1/2 from "equal distance
  per winding."  If Track 4 gives α ∝ r², this constraint
  determines α.
- **Q53** — anomalous moment.  The field distribution from
  the self-consistent calculation may also predict g − 2.

## References

- R15 findings: localization formula, σ, candidates for what
  determines σ.
  [`forward-charge/findings.md`](../forward-charge/findings.md)
- R13 Track 3: monopole integral, azimuthal symmetry kills
  charge.
  [`kk-charge-t3/findings.md`](../kk-charge-t3/findings.md)
- R16 README: Fourier decomposition framework.
  [`harmonic-charge/README.md`](../harmonic-charge/README.md)
- R8 Track 3: g = 2 from topology, anomalous moment open.
  [`multi-winding/findings.md`](../multi-winding/findings.md)
