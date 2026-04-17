# R59 Background: From 3D Embedding to Spacetime Geometry

## Terminology

Throughout this document and study:

| Symbol | Meaning |
|--------|---------|
| **S** | The three spatial dimensions (x, y, z) |
| **t** | The time dimension |
| **St** | Spacetime: S + t (3+1 dimensions, Lorentzian signature) |
| **Ma** | The six compact material dimensions (three 2-tori) |
| **ℵ** | The sub-Planck internal edge dimension (GRID) — an open hypothesis, not asserted |
| **R⁴** | Four-dimensional Euclidean space (four spatial dims, NO time) |
| **R^{3,1}** | Minkowski spacetime (3 spatial + 1 time, Lorentzian) |
| **S³** | The 3-sphere — a 3D surface embedded in R⁴ (spatial, no time) |

"4D" is ambiguous.  This study distinguishes carefully:
- 4 spatial dimensions (R⁴) — used for the mathematical Clifford torus
- 3+1 spacetime (R^{3,1}) — the physical arena
- Whether the Clifford torus embeds in pure space or in spacetime is an open question


## The lesson physics learned from gravity — and didn't apply to EM

Einstein transformed our understanding of gravity.  Before
general relativity, gravity was a force: masses exert an
attractive pull on each other through space.  After Einstein,
gravity became an effect: mass warps spacetime, and other
masses follow the straightest possible paths (geodesics) through
the warped geometry.  Spacetime tells mass how to fall.

The key insight: gravity is strongest in the TIME direction.
In the spatial dimensions (S), mass bends geodesics gently —
producing slow orbital curvature.  In the time dimension (t),
mass bends geodesics steeply — producing the acceleration we
call "falling."  When you stand on Earth, you're not being
pulled down by a force.  Your geodesic through spacetime is
curved in the t direction by Earth's mass, and that curvature
manifests as the sensation of weight.

Physics fully accepted this for gravity.  But for electro-
magnetism, the pre-Einstein picture persists: charged particles
exert forces on each other through fields.  The electromagnetic
field is a physical entity (the photon field), and forces are
mediated by virtual photon exchange.

This isn't because no one tried to geometrize EM.  Einstein
himself spent thirty years (1925–1955) on unified field theory.
Kaluza (1921) showed that adding a fifth dimension to spacetime
(a compact spatial dimension beyond S) causes the off-diagonal
metric components between the 5th dimension and St to behave
exactly like the electromagnetic potential A_μ.  Specifically:

- The compact-**time** off-diagonal (g₅₀) = the electric
  potential φ → Coulomb force
- The compact-**spatial** off-diagonals (g₅ᵢ) = the vector
  potential **A** → magnetic force

In Kaluza-Klein theory, **electromagnetism IS spacetime
curvature** — in a compact dimension coupled to St.  The
electric force, like gravity, is curvature in the time
direction.  The magnetic force is curvature in the spatial
directions.  The only difference from gravity is that the
compact-dimension curvature can have a SIGN (from the winding
direction), while the gravitational curvature from mass is
always positive.

MaSt/GRID sits on the Einstein/Kaluza-Klein side.  The compact
Ma dimensions ARE the extra dimensions of KK theory.  We are
doing what Einstein attempted — geometrizing electromagnetism —
with the advantage of six compact dimensions and a discrete
lattice substrate.


## How gravity bends spacetime — and how EM might do the same

### Gravity: mass bends the S-t plane

A mass M sits at the origin.  In the Schwarzschild solution:

- **Spatial curvature:** geodesics in S curve gently around
  the mass.  An orbiting planet follows a nearly circular
  spatial path.  The spatial curvature is proportional to
  M/r — small at large distances.

- **Time curvature:** geodesics in the S-t plane curve
  steeply.  A dropped object follows a parabolic worldline in
  the S-t plane — accelerating toward the mass.  The time
  curvature (g₀₀ component) is proportional to M/r and is
  the dominant effect of gravity.

The reason gravity feels like a force is that time is
always passing — you're always moving through t.  The
curvature of t near a mass deflects your worldline, causing
acceleration.  You can avoid the spatial curvature (by
staying still), but you can never avoid the time curvature.

### EM: charge bends the Ma-t plane (KK picture)

A charge Q sits at the origin.  In the KK picture, the charge
is a mode with winding number n on the compact dimension.
The winding produces curvature in the compact-t plane:

- **Compact-time curvature (g₅₀):** geodesics in the
  compact-t plane curve proportionally to Q/r.  This is the
  electrostatic potential φ.  Another charged particle (with
  its own compact winding) experiences this curvature as a
  force — attractive if the windings are opposite (curvatures
  cancel between the charges), repulsive if the windings are
  the same (curvatures reinforce).

- **Compact-spatial curvature (g₅ᵢ):** a MOVING charge
  produces curvature in the compact-spatial planes.  This is
  the magnetic vector potential **A**.  The resulting geodesic
  deviation is the magnetic force.

The parallel to gravity is exact:
- Gravity: mass bends the S-t plane → objects accelerate (fall)
- EM: charge bends the Ma-t plane → charges accelerate (attract/repel)

The crucial difference: gravity bends S-t with one sign (always
attractive, because mass is always positive).  EM bends Ma-t
with either sign (attractive or repulsive, because winding can
be clockwise or counterclockwise).


## The problem of signed curvature in 3D

In MaSt studies R1–R58, the compact Ma dimensions have been
embedded in 3D (ordinary space S).  A 2-torus in 3D has an
inner equator and an outer equator.  The curvature changes
sign between them — but this sign change is an artifact of
the 3D embedding, not a property of the charge.

In 3D, both positive and negative charges produce the SAME
bending of the torus surface (same curvature at each point).
The charge sign comes from the winding direction (clockwise
vs counterclockwise), not from the curvature.  There is no
geometric mechanism in 3D for opposite charges to curve
space in opposite directions.

For EM as true spacetime geometry, we need curvature that
depends on the SIGN of the charge.  This requires the compact
dimensions to couple to time — not just to space.


## The 3D torus as a simplification with real problems

Embedding a 2-torus in 3D causes specific problems:

1. **Self-intersection.**  When the tube radius exceeds the
   ring radius (a > R, i.e., ε < 1), the torus intersects
   itself in 3D.  The proton sheet (ε_p = 0.55) has this
   problem.

2. **Metric saturation.**  The e-sheet's internal shear
   (s_e = 2.004) pushes the 2×2 metric to the positive-
   definiteness boundary (off-diagonal ratio = 0.9999).
   No additional coupling can be added without breaking
   the metric (R55 Track 3, F8).

3. **Inner/outer asymmetry.**  The 3D embedding stretches
   the outer equator and compresses the inner equator.
   The junction distortions are nonuniform, complicating the
   leakage analysis (sim-impedance Tracks 11–12).

4. **Tube-ring mixing.**  In 3D, the ring circumference
   varies with tube position: 2π(R + a cos θ₁).  The tube
   and ring directions are not independent.  The flat-torus
   metric (model-E) assumes they are — which is only true
   for the Clifford embedding, not the 3D embedding.


## The Clifford torus

### What it is

The Clifford torus is a 2-torus embedded in R⁴ (four spatial
dimensions) as the product of two circles in orthogonal planes:

<!-- T² = S¹(r₁) × S¹(r₂) ⊂ R⁴ -->
$$
T^2 = S^1(r_1) \times S^1(r_2) \subset \mathbb{R}^4
$$

Parameterized by two angles (θ₁, θ₂):

<!-- x₁ = r₁ cos θ₁, x₂ = r₁ sin θ₁, x₃ = r₂ cos θ₂, x₄ = r₂ sin θ₂ -->
$$
\begin{aligned}
x_1 &= r_1 \cos\theta_1, \quad x_2 = r_1 \sin\theta_1 \\
x_3 &= r_2 \cos\theta_2, \quad x_4 = r_2 \sin\theta_2
\end{aligned}
$$

The tube circle (θ₁) lies in the (x₁, x₂) plane.  The ring
circle (θ₂) lies in the (x₃, x₄) plane.  The two planes are
orthogonal — they share no direction.

### Key properties

**Extrinsically flat.**  The Clifford torus has zero extrinsic
curvature in R⁴.  Every point on the surface has the same
local geometry.  The induced metric is:

<!-- ds² = r₁² dθ₁² + r₂² dθ₂² -->
$$
ds^2 = r_1^2\, d\theta_1^2 + r_2^2\, d\theta_2^2
$$

This is diagonal — no cross terms, no curvature, completely
uniform.  There is no inner/outer equator.

**No self-intersection.**  The two circles live in orthogonal
planes.  They never interfere, regardless of r₁/r₂.  Any
aspect ratio is valid.

**The flat-torus metric IS the Clifford metric.**  The 2×2
diagonal metric ds² = L₁²dθ₁² + L₂²dθ₂² that model-E uses
for each sheet IS the induced metric of the Clifford torus.
The model-E metric has been implicitly assuming a Clifford
embedding all along — it just didn't know it.


## The physical question: which "4D" is physical?

The Clifford torus mathematically requires 4 dimensions.
But which 4?

### Option A: Four spatial dimensions

The torus sits in R⁴ — pure space, no time.  This is
mathematically clean but physically incomplete.  It resolves
self-intersection and metric saturation but doesn't connect
to forces (which require time curvature).

### Option B: Three spatial + time (spacetime, St)

The torus sits in R^{3,1} — Minkowski spacetime.  One circle
is spatial; the other involves the time direction.  This is
the KK picture: the compact dimension couples to time, and
the Coulomb force IS curvature in the compact-time plane.

If the TUBE circle is in a spatial plane and the RING circle
involves time, then:
- The tube winding (charge) is a spatial pattern
- The ring winding (which sets mass via frequency) couples
  to time
- The Ma-t coupling produces the electric field
- The combination gives both charge quantization (from
  spatial topology) and electromagnetic force (from time
  curvature)

### Option C: Ma space + ℵ or time

The tube and ring are both in compact (Ma) dimensions.  The
"4th dimension" that the Clifford torus needs is either ℵ
or time or a combination.  This is the R55 picture extended
to 4D embedding.

The study should investigate all three options.  The
physically correct answer may be that the "4 dimensions"
are 2 compact (Ma) + 1 spatial (S) + 1 time (t), or some
other combination.


## The ℵ hypothesis — open, not asserted

R55 Track 3 introduced the ℵ-line as the mediator of Ma-S
coupling, achieving near-universal α (3.6% gap).  This study
does NOT assume ℵ is the correct mechanism.  Instead, it
asks:

- Does the Clifford torus embedding in spacetime (with time)
  provide the coupling mechanism BY ITSELF?
- If so, is ℵ redundant?
- Or does ℵ still play a role as the microscopic (lattice-scale)
  implementation of the time-based coupling?

The relationship between the ℵ-mediated picture (R55) and the
spacetime-geometry picture (this study) is an open question.


## The visualization challenge

The Clifford torus lives in 4 dimensions (whichever 4 they
are).  We cannot directly visualize 4D geometry.  Two
strategies:

**Dimensional compression.**  Replace 3D space with 2D,
freeing a visual axis for the compact or time dimension.
The existing viz/geodesic-curvature program does this for
gravity — it shows a 2D spatial surface with curvature.
An analogous tool for EM would show:
- A 2D spatial surface (x, z) with the compact dimension
  as height or color
- Time as animation (evolving the curvature)
- Geodesic convergence (attraction) and divergence
  (repulsion) as paths on the surface

**Stereographic projection.**  Project S³ → R³, mapping the
Clifford torus to the familiar 3D torus.  The 3D picture is
now understood as a projection of the true 4D geometry, not
the geometry itself.  Distortions in the 3D picture (inner/
outer asymmetry) are projection artifacts.

All results will be derived mathematically first.  The
visualizations are aids to intuition, not substitutes for
the mathematics.
