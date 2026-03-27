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

### Track 4. Analytical estimate  *(COMPLETE — negative result)*

**Script:** [`scripts/track4_analytical.py`](scripts/track4_analytical.py)

Computed the 3D curvature, centrifugal force, and Fourier
decomposition along the (1,2) helix for r = 0.25, 0.5, 1.0.
Tested four variants of the charge integral: perfect torus,
deformed tube, velocity-modulated field, nonlinear metric
coupling.

**Result: ALL charge integrals give exactly zero.**

The tube deformation (from centrifugal pressure) is
φ-independent on a symmetric torus.  It breaks the tube's
circular symmetry (in θ) but preserves the ring's rotational
symmetry (in φ).  The charge integral factorizes as
[θ-stuff] × ∫cos(2φ)dφ = 0 regardless of the deformation.

The root cause is the **two-pass cancellation**: the (1,2)
winding visits each ring position at θ and θ+π.  Any
θ-dependent quantity cancels between the two passes because
cos(θ) + cos(θ+π) = 0.

**This rules out Tracks 1–3** (tube deformation → mode
coupling → charge) as originally conceived.  On a symmetric
torus, no amount of tube deformation can produce a monopole.

**Positive findings preserved:**
- Curvature harmonic series quantified (F1, F2)
- Force magnitudes and components catalogued
- The φ-symmetry protection clearly identified (F3–F5)
- Opens Track 5 (dynamic wavepacket compression)

See [`findings.md`](findings.md) F1–F5 for details.


### Track 5. Dynamic wavepacket compression  *(COMPLETE — negative result)*

**Script:** [`scripts/track5_wavepacket.py`](scripts/track5_wavepacket.py)

Track 4 showed that the centrifugal force can't produce
charge from a delocalized wave.  Track 5 asked: can it
determine σ (the localization width) for a localized
wavepacket?

Two sub-effects were investigated:

**A. Width clumping (compression/stretching).**
Could the centrifugal force gradient across the wavepacket
compress it at the inner equator and stretch it at the outer,
with a net residual from the nonlinearity?

**Result: No.**  Two independent reasons:

1. **F ⊥ v exactly.**  The centrifugal force has zero
   component along the path direction (it is always
   perpendicular to the velocity).  This is a geometric
   identity, not an approximation.  There is no direct
   force that can push energy volumes together or apart
   along the path.

2. **σ_φ = const in the flat metric.**  The angular width
   of the wavepacket in the flat T² coordinates is a
   constant of the motion.  The 3D width σ_3D oscillates
   ("breathes") because the 3D arc length per unit φ
   varies, but the net magnification per circuit is
   exactly 1.  The packet returns to its original 3D
   extent after every circuit.

**B. Path deflection.**
Could the surface-perpendicular centrifugal force deflect
the path from the flat-T² geodesic, modifying the charge
integral?

**Result: The force is not an external perturbation.**
The centrifugal force and the confinement force are
Newton's third-law pair — they are the same force viewed
from inside (flat T²) and outside (3D).  The photon
follows the flat-T² geodesic, and the 3D curvature is
what this straight-line motion looks like from outside.

A hypothetical deflection calculation (treating the force
as external) gives enormous displacements (Δθ ~ 8–16 rad,
multiple full tube rotations), confirming the force
magnitude but also confirming that it is already fully
balanced by the confinement.

See [`findings.md`](findings.md) F7–F10 for details.


## Status

**Tracks 4 & 5: both negative.  R17 is complete.**

**Track 4** showed that tube deformation from centrifugal
pressure preserves the ring's rotational symmetry, so the
monopole integral vanishes.  Tracks 1–3 are ruled out.

**Track 5** showed that the centrifugal force cannot
determine σ either:
- F ⊥ v exactly → no direct clumping (F7)
- Width breathing is exactly conservative → σ_φ = const (F8)
- The centrifugal force is a consequence of confinement,
  not an external perturbation → cannot deflect the path (F10)

**Key positive insight:** the centrifugal force decomposition
reveals that ~70% of the force is normal to the surface
(pushes field into 3D) and ~70% is perpendicular to the
path on the surface (would deflect if external).  These are
enormous (~0.5 N) and fully balanced by the confinement.
This confirms the model's self-consistency: the centrifugal
force IS the inertia of the confined photon.


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
  [`R15-forward-charge/findings.md`](../R15-forward-charge/findings.md)
- R13 Track 3: monopole integral, azimuthal symmetry kills
  charge.
  [`R13-kk-charge-t3/findings.md`](../R13-kk-charge-t3/findings.md)
- R16 README: Fourier decomposition framework.
  [`R16-harmonic-charge/README.md`](../R16-harmonic-charge/README.md)
- R8 Track 3: g = 2 from topology, anomalous moment open.
  [`R8-multi-winding/findings.md`](../R8-multi-winding/findings.md)
