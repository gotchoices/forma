# R59: Clifford torus — EM as spacetime geometry

**Status:** Framed
**Background:** [background.md](background.md)
**Type:** theoretical + compute + visualization
**Depends on:** R55 (ℵ-mediated coupling), R54 (particle inventory),
  R53 (generations), sim-impedance (charge from bending),
  GRID (lattice substrate)

---

## Core question

Einstein showed: gravity is not a force — it's curvature of
spacetime (St).  Mass bends the spatial-time (S-t) plane,
causing geodesic convergence (objects "fall" toward each other).

**Could electromagnetism work the same way?**  If charges bend
the compact-time (Ma-t) plane — with a sign that depends on
the winding direction — then:
- Opposite charges → curvatures cancel between them →
  geodesics converge → **attraction**
- Like charges → curvatures reinforce between them →
  geodesics diverge → **repulsion**

The Coulomb force would be geodesic deviation in the Ma-t
plane, just as gravitational "force" is geodesic deviation
in the S-t plane.

---

## Why the Clifford torus

The Ma sheets have been embedded in 3D space (S) throughout
R1–R58.  This causes problems:
- Self-intersection (proton sheet)
- Metric saturation (e-sheet nearly singular, R55 F8)
- Inner/outer asymmetry (complicates charge analysis)
- No mechanism for signed curvature

A 2-torus needs at least 4 dimensions for a flat embedding.
The **Clifford torus** embeds in 4D as two circles in
orthogonal planes: no bending, no self-intersection, any
aspect ratio valid.  The model-E flat-torus metric has been
implicitly assuming a Clifford embedding all along.

The physical question: which 4 dimensions?
- 4 spatial (pure math, no forces) — incomplete
- 3 spatial + time (spacetime) — the KK picture, gives forces
- 2 compact + 1 spatial + 1 time — a hybrid

The study investigates all options, with emphasis on the
spacetime embedding where the Ma-t coupling provides the
electromagnetic force.

---

## What changes from 3D

| Feature | 3D torus | Clifford torus |
|---------|----------|---------------|
| Extrinsic curvature | Nonzero (inner/outer) | Zero (flat) |
| Self-intersection | Fails when a > R | Any aspect ratio valid |
| Tube-ring mixing | cos(θ₁) factor | Zero (orthogonal) |
| Metric saturation | e-sheet at PD limit | No saturation |
| EM as geometry | No signed curvature | Signed curvature from Ma-t |
| Time integration | Separate (bolt-on) | Natural (part of the 4D) |

---

## Open questions (not asserted)

1. **Does the Clifford embedding need ℵ?**  R55 Track 3 used
   ℵ to mediate Ma-S coupling (3.6% universality gap).  If
   the time dimension provides the coupling via KK reduction,
   ℵ may be redundant — or it may be the microscopic
   mechanism that the time-based coupling implements at the
   lattice scale.  To be determined.

2. **Which circle couples to time?**  If the torus embeds in
   spacetime, one circle is spatial and one involves time.
   Is it the tube (charge direction) or the ring (mass/frequency
   direction)?  The KK picture suggests the tube couples to t
   (producing the electric potential g₅₀).  But the ring might
   also couple (producing the magnetic potential).

3. **Where does α appear?**  In KK theory, α comes from the
   ratio of the compact dimension's size to the Planck length.
   In the Clifford-spacetime picture, it might come from the
   Ma-t off-diagonal metric entry directly.  A single entry
   setting α (as the user proposed) would be the cleanest
   result.

---

## Tracks

### Track 1: The Clifford torus metric

Derive the induced metric, extrinsic curvature, and geodesics
for the Clifford torus T² = S¹(r₁) × S¹(r₂).

- In R⁴ (4 spatial dimensions)
- In S³ (the 3-sphere)
- Comparison to the 3D torus metric
- Prove: the model-E flat-torus metric IS the Clifford metric

**Viz:** Stereographic projection S³ → R³ showing the
Clifford torus as the familiar 3D torus (a projection,
not the true geometry).

### Track 2: Signed curvature from windings

Compute the curvature produced by a mode with winding (n₁, n₂)
on the Clifford torus.

- Does the sign of n₁ produce opposite curvature?
- Place two opposite-sign modes at separation r in S.
  Do geodesics converge (attraction)?
- Place two same-sign modes.  Do geodesics diverge (repulsion)?

**Viz:** 2D spatial surface (S compressed to 2D) with compact
dimension as height.  Show geodesic convergence for opposite
charges, divergence for like charges.

### Track 3: Spacetime metric with compact dimensions

Build the metric for a Clifford torus embedded in spacetime
(R^{3,1}) or in an extended spacetime with compact dimensions.

Full metric dimensions:
- 6 compact (Ma) — three Clifford tori
- 3 spatial (S)
- 1 time (t)
- 1 ℵ (open — include if needed, omit if not)

Derive the KK reduction:
- Which off-diagonal entries produce A_μ (EM potential)?
- Does the electric potential (φ = g₅₀) give the Coulomb force?
- Does the magnetic potential (A = g₅ᵢ) give magnetic effects?
- Where does α appear?  Is it a single metric entry?

**Mathematical emphasis:** derivation-heavy, following the
standard KK procedure but for our specific geometry.  Show
each step.

### Track 4: Particle spectrum

Verify the model-E particle inventory on the Clifford metric.

- The flat-torus spectrum should be identical (by construction)
- Add the Ma-t coupling and check for spectrum shifts
- If ℵ is included: compare to R55 Track 3 results
- Does the metric saturation problem (R55 F8) disappear?
- Does the 3.6% α universality gap close?

### Track 5: Coulomb's law from geodesics

Derive F ∝ e²/r² from geodesic deviation.

Given two charged Clifford tori at separation r:
- Compute the metric perturbation (linearized gravity + KK)
- Solve the geodesic deviation equation
- Extract the effective force vs r
- Verify: 1/r² law, correct sign, coefficient gives α

This is the most ambitious track.  It tests whether the
Clifford-spacetime picture reproduces the quantitative
Coulomb law, not just the qualitative attraction/repulsion.

---

## Visualization strategy

**The problem:** 4+ dimensional geometry cannot be directly
seen.  The study must rely on mathematical rigor first, then
illustration.

**Method A: Dimensional compression.**  Compress S from 3D to
2D, freeing one visual axis for the compact or time dimension.
Based on the approach in viz/geodesic-curvature.  Show:
- Spatial surface with compact dimension visible (height/color)
- Time as animation
- Geodesic paths showing convergence/divergence

**Method B: Stereographic projection.**  S³ → R³.  The
Clifford torus projects to the familiar 3D torus — distorted
but topologically correct.  Mark the distortions as projection
artifacts.

**Method C: 2D slices.**  Fix one coordinate, show the
remaining 2D cross-section.  Animate over the fixed coordinate.

**Rule:** Derive everything analytically first.  Only then
visualize.  If the math says convergence, show convergence.
Don't rely on the picture to discover physics — use it to
confirm and communicate.

---

## Mathematical approach

The study requires Riemannian/Lorentzian geometry beyond what
prior studies used.  Each new concept will be derived from
scratch with enough detail for a reader with college-level
engineering math:

- **Product manifolds:** how the metric of T² = S¹ × S¹ comes
  from the metrics of the two circles
- **Extrinsic curvature:** how a surface curves in its
  ambient space (second fundamental form)
- **KK reduction:** how a (D+1)-dimensional metric with one
  compact dimension produces D-dimensional gravity + gauge field
- **Linearized gravity:** how small metric perturbations from
  a source produce geodesic deviation (the "force")
- **Lorentzian signature:** how time differs from space in the
  metric (−dt² vs +dx²) and what this means for geodesics

---

## Files

| File | Purpose |
|------|---------|
| [background.md](background.md) | Detailed motivation and context |
| README.md | This framing document |
| scripts/ | Computation scripts (per track) |
| findings.md | Results (after computation) |
