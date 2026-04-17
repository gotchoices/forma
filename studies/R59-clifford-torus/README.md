# R59: Clifford torus — EM as geometry in 4D

**Status:** Framed
**Background:** [background.md](background.md)
**Type:** theoretical + compute + visualization
**Depends on:** R55 (ℵ-mediated coupling, 10×10 metric),
  R54 (particle inventory), R53 (generations),
  sim-impedance Tracks 8–12 (charge from bending),
  GRID (lattice substrate, charge-emergence.md)
**Motivates:** model-F (if successful), unified EM-gravity
  geometric picture

---

## Premise

The MaSt compact dimensions have been embedded in 3D
throughout studies R1–R58.  This causes problems:
- Self-intersection (proton sheet, a > R)
- Metric saturation (e-sheet, s = 2.004 nearly singular)
- Asymmetric distortion (inner/outer equator)
- No mechanism for opposite-sign curvature (attraction/repulsion)

A 2-torus does not require 3D.  Its natural home is 4D,
where it can be embedded as a **Clifford torus** — the
product of two circles in orthogonal planes.  The Clifford
torus is flat (no inner/outer asymmetry), non-self-intersecting
(any aspect ratio valid), and lives naturally in S³ (the
3-sphere).

This study asks: **if the Ma sheets are Clifford tori in 4D
(or 4+1D with time), does the geometry provide:**

1. **Signed curvature** for EM attraction/repulsion
   (opposite windings → opposite curvature → geodesic
   convergence/divergence)

2. **Universal α** without the 3.6% gap from R55
   (the metric saturation problem disappears in 4D)

3. **A single geometric origin for α** via the ℵ-time
   off-diagonal metric entry in the Lorentzian version

4. **Magnetic moments and radiation** from the time
   component (the 10×10 spatial metric handles static
   coupling but not dynamics)

---

## What changes from the 3D picture

| Feature | 3D torus | Clifford torus (4D) |
|---------|----------|-------------------|
| Extrinsic curvature | Nonzero (inner/outer) | **Zero** (flat embedding) |
| Self-intersection | a > R fails | **Any aspect ratio valid** |
| Tube-ring mixing | cos(θ₁) factor | **Zero** (orthogonal planes) |
| Metric saturation | e-sheet at PD limit | **No saturation** |
| Signed curvature | Not available in 3D | **Available in 4D** (S³ curvature) |
| Visualization | Direct | **Requires projection or dim reduction** |
| Time integration | Separate | **Natural** (4th dim can be Lorentzian) |

---

## Tracks

### Track 1: The Clifford torus metric

Derive the induced metric, extrinsic curvature, and geodesics
for a Clifford torus T² = S¹(r₁) × S¹(r₂) in R⁴ and in S³.

Deliverables:
- The 2D induced metric (should be diagonal: ds² = r₁²dθ₁² + r₂²dθ₂²)
- Extrinsic curvature tensor (should be zero in R⁴, nonzero in S³)
- Geodesic equations on the Clifford torus
- Comparison to the 3D torus metric (the cos θ₁ factor should vanish)
- Show that the flat-torus model-E metric IS the Clifford metric

**Visualization:** project the Clifford torus into 3D via
stereographic projection.  Show how the "distortion" in 3D is
a projection artifact, not real curvature.

### Track 2: Signed curvature from winding modes

A standing-wave mode on the Clifford torus with winding numbers
(n₁, n₂) carries energy distributed on the surface.  This
energy curves the ambient space (4D or S³).

Questions:
- What is the curvature tensor produced by a (1, 2) mode?
- How does the sign of n₁ (tube winding = charge sign) affect
  the curvature?
- Place two modes (opposite signs) at a spatial separation.
  Do geodesics between them converge (attraction)?
- Place two modes (same sign) at a separation.  Do geodesics
  diverge (repulsion)?

This is the key test: does the Clifford torus geometry
reproduce the Coulomb force law from geodesic effects?

**Visualization:** reduce S from 3D to 2D.  Show the geodesic
curvature surface (like viz/geodesic-curvature) with the
compact dimension as height.  Animate geodesic convergence
(attraction) and divergence (repulsion).

### Track 3: The 4+1D Lorentzian metric

Extend the spatial Clifford torus to Lorentzian signature.
The full metric becomes 11-dimensional:
- 6 compact Ma dimensions (three Clifford tori)
- 1 ℵ dimension (Planck scale)
- 3 spatial S dimensions
- 1 time dimension

Or equivalently, embed the Clifford torus in a 4+1D spacetime
where the 4 spatial dimensions are the Clifford R⁴ and the
5th is time.

Questions:
- Does the time component provide the magnetic field
  (the time-space component of the EM field tensor in KK)?
- Is the ℵ-time off-diagonal entry the seat of α?
- Does the Lorentzian metric give propagating EM waves
  (photons) naturally?

**Mathematical emphasis:** This track is primarily analytical.
Derive the KK reduction of the Clifford metric with time,
show the emergence of the EM potential A_μ, and identify
where α appears.

### Track 4: Particle spectrum on the Clifford torus

Recompute the model-E particle inventory using the Clifford
metric instead of the 3D-embedded metric.

Questions:
- Does the Clifford metric reproduce the model-E particle
  spectrum exactly?  (It should — the flat-torus metric IS
  the Clifford metric by construction.)
- Does the ℵ coupling work better on the Clifford torus?
  (The metric saturation problem should vanish.)
- Does the 3.6% α universality gap close?
- Do the cross-sheet shears (neutron, baryons) need
  re-derivation?

### Track 5: Coulomb's law from geodesics

The quantitative test: derive the 1/r² Coulomb force law
from geodesic deviation in the Clifford-torus-curved spacetime.

Given:
- Two particles (Clifford tori) with opposite tube windings
  (charges +e, −e)
- Separated by distance r in the spatial dimensions

Compute:
- The metric perturbation produced by each particle's
  energy-momentum tensor (linearized gravity in 4+1D)
- The geodesic deviation equation for a test particle
- The effective force as a function of r

Expected result:
- F ∝ e²/r² (Coulomb law)
- The coefficient gives α from the geometry
- The sign (attractive for opposite, repulsive for like)
  comes from the signed curvature in compact dimensions

This is the most ambitious track and may require techniques
from linearized KK gravity.

---

## Visualization strategy

Since 4D geometry cannot be directly visualized, every track
will include dimension-reduced visualizations:

**Method A: Dimensional compression.**  Replace 3D space with
2D (a plane or surface), making the compact/time dimensions
visible.  This is how viz/geodesic-curvature works for
gravity.  The "missing" spatial dimension is acceptably lost
because the physics is spherically symmetric.

**Method B: Stereographic projection.**  Project S³ → R³ via
stereographic projection.  The Clifford torus projects to the
familiar 3D torus — but now understood as a projection artifact.
Curvature and geodesics in the projected picture correspond to
(distorted) curvature and geodesics in the true 4D picture.

**Method C: Slice visualization.**  Show 2D slices of the 4D
geometry at fixed values of one coordinate.  Animate over the
sliced coordinate to give a sense of the full structure.

All key results will be derived mathematically FIRST, then
illustrated visually.  The mathematics is primary; the
visualizations are aids to intuition, not substitutes for rigor.

---

## Mathematical prerequisites

The study requires:
- Riemannian geometry in dimensions > 3 (metrics, curvature
  tensors, geodesics on product manifolds)
- Kaluza-Klein reduction (deriving gauge fields from
  higher-dimensional metrics)
- Linearized gravity (metric perturbations from stress-energy,
  geodesic deviation)
- Lorentzian signature (timelike/spacelike distinction,
  causal structure)

Where these concepts are used, they will be derived from
first principles with enough detail for a reader with
college-level engineering mathematics.  The aim is to be
rigorous but not opaque.

---

## Relationship to prior work

| Study | What it provides | What R59 adds |
|-------|-----------------|--------------|
| R54/model-E | Particle inventory on flat T⁶ | Clifford embedding; unchanged spectrum |
| R55 | ℵ-mediated coupling (10×10) | 11×11 with time; no metric saturation |
| sim-impedance | Charge from bending | Bending in 4D (S³ curvature, not 3D inner/outer) |
| charge-emergence | Mechanism of charge | Signed curvature → attraction/repulsion |
| GRID | Lattice substrate, α as input | α from ℵ-time geometry (if Track 3 succeeds) |

---

## Files

| File | Purpose |
|------|---------|
| [background.md](background.md) | Detailed motivation and context |
| README.md | This framing document |
| scripts/ | Computation scripts (per track) |
| findings.md | Results (after computation) |
