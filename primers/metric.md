# The Metric — A Ground-Up Introduction

A self-contained introduction to the metric tensor, starting from
the simplest question — *how do we measure distance?* — and ending
with light cones and the wave equation. Assumes calculus, vectors,
and matrices. No prior exposure to general relativity is needed.

This primer is a prerequisite for
[kaluza-klein.md](kaluza-klein.md) and is referenced from various
projects and studies that use the metric formalism. It is paced
deliberately gently; if you are fluent with differential geometry,
parts will feel basic. That is intentional.

---

## Concepts introduced in this primer

| § | Concept |
|---|---------|
| 1 | Why we need a metric |
| 2 | Distance in Cartesian coordinates: ds² = dx² + dy² |
| 3 | Distance in polar coordinates: ds² = dr² + r² dθ² |
| 4 | The metric as a matrix |
| 5 | The metric is a *field* of matrices |
| 6 | Off-diagonal terms and what they mean |
| 7 | Spacetime and the minus sign |
| 8 | The light cone and interval classification |
| 9 | The metric near a mass |
| 10 | Geodesics: free particles follow shortest paths |
| 11 | The d'Alembertian and the wave equation |
| 12 | Compact dimensions |

---

## 1. Why we need a metric

Coordinates are labels. They tell you *which point* you are at, but
they do not, on their own, tell you *how far* one point is from
another.

In Cartesian coordinates on a flat plane, the distance from (0, 0)
to (3, 4) is 5 (Pythagoras), but in polar coordinates the distance
from (r=1, θ=0) to (r=1, θ=π) is *not* π — it is 2 (the chord
across a unit-radius circle, or 2 along the arc, depending on
which path you mean). Different coordinate systems describe the
same points but produce different "differences."

The **metric** is the recipe that converts coordinate-differences
into actual distances. It is the bridge between the abstract labels
we use to describe space and the physical lengths we want to
measure.

In one sentence: **coordinates give labels, the metric gives
distances**.

---

## 2. Distance in Cartesian coordinates

In a flat plane with Cartesian coordinates (x, y), the distance
between two nearby points is given by the Pythagorean theorem:

<!-- ds² = dx² + dy² -->
$$
ds^2 = dx^2 + dy^2
$$

Reading the notation:

- **dx, dy** — small *coordinate differences* between the two
  points. If one point is at (x, y) and the other at
  (x + dx, y + dy), then dx and dy are the offsets in each
  direction.
- **ds** — the actual physical distance between the points.
- **ds²** — distance squared. We use the squared form because it
  avoids the square root and makes the algebra cleaner.

Why "infinitesimal" (the small d's)? Because in *curved* spaces the
recipe changes from place to place — it is only exactly right for
infinitesimally small steps. For flat space the formula works at
any scale, but using infinitesimals from the start lets the same
notation handle both flat and curved cases.

Extending to 3D:

<!-- ds² = dx² + dy² + dz² -->
$$
ds^2 = dx^2 + dy^2 + dz^2
$$

And to 4D Euclidean (we'll see Lorentzian spacetime in §7):

<!-- ds² = dx² + dy² + dz² + dw² -->
$$
ds^2 = dx^2 + dy^2 + dz^2 + dw^2
$$

The pattern: in an N-dimensional Cartesian Euclidean space, ds² is
the sum of squares of all coordinate differences.

---

## 3. Distance in polar coordinates

Take the same flat plane and switch to polar coordinates (r, θ),
where r is distance from the origin and θ is angle. Now the
distance recipe looks different:

<!-- ds² = dr² + r² dθ² -->
$$
ds^2 = dr^2 + r^2\,d\theta^2
$$

Why? Because **coordinates are not always distances**.

- **r** is itself a distance (from the origin), so a step dr is
  literally that much distance moved radially. Contributes dr² to
  ds², just like Cartesian.
- **θ** is an *angle* (radians or degrees). A step dθ is just an
  angular change; it is not yet a distance.

To convert dθ to actual distance, we use the arc-length formula:
arc length = radius × angle. So an angular step dθ at radius r
produces a *tangential distance* of r·dθ. The contribution to ds²
is therefore (r·dθ)² = r² dθ².

Sanity checks:

- At the origin (r = 0), changing θ moves you nowhere. The formula
  agrees: r² dθ² = 0.
- At r = 10, a small angular step dθ = 0.01 sweeps an arc of
  length 0.1, *not* 0.01. The r² factor converts angle to distance.
- Units: dr² has units of length². r² dθ² also has length² (length²
  × radian², and radians are dimensionless). ✓

**Same flat plane, different coordinates, different recipe.** The
geometry has not changed. What has changed is how the coordinate
labels relate to actual distances. The metric is the bookkeeping
that makes this conversion explicit.

---

## 4. The metric as a matrix

We can write any of these distance recipes as a matrix sandwich.

For 2D Cartesian:

<!-- g = [[1, 0], [0, 1]];  ds² = [dx, dy] · g · [dx, dy]ᵀ -->
$$
g = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},
\qquad
ds^2 = \begin{pmatrix} dx & dy \end{pmatrix}\,g\,\begin{pmatrix} dx \\ dy \end{pmatrix}
$$

To check the sandwich gives the right answer, do the matrix
multiplication step by step:

```
[dx, dy] · [1  0]  =  [dx, dy]    (multiplied row by matrix)
           [0  1]

[dx, dy] · [dx]  =  dx² + dy²    (multiplied row by column)
           [dy]
```

So the sandwich gives ds² = dx² + dy². Same answer.

For 2D polar:

<!-- g = [[1, 0], [0, r²]] -->
$$
g = \begin{pmatrix} 1 & 0 \\ 0 & r^2 \end{pmatrix}
$$

The sandwich [dr, dθ] · g · [dr, dθ]ᵀ gives dr² + r² dθ². Same
answer as the polar formula.

**General form.** In any number of coordinates, the metric is an
N × N symmetric matrix g_μν, and:

<!-- ds² = sum over μ,ν of g_μν dx^μ dx^ν -->
$$
ds^2 = \sum_{\mu,\nu}\, g_{\mu\nu}\, dx^\mu\, dx^\nu
$$

Reading the indices:

- **μ, ν** are coordinate labels — they each run over all the
  coordinates of the space (e.g., for 3D Cartesian: x, y, z).
- **dx^μ** means "the small step in the μ-th coordinate." If
  μ = x, dx^μ = dx.
- **g_μν** is the matrix entry in row μ, column ν.
- The sum runs over all combinations of μ and ν, so an N-coordinate
  space has N² terms (most of them zero for a diagonal metric).

This is the standard physics notation. Anywhere you see ds² written
this way, you can unpack it as a matrix sandwich.

(For more on matrix index notation, see
[matrix-primer.md](matrix-primer.md).)

---

## 5. The metric is a *field* of matrices

The metric matrix can depend on position. Look at the polar
example:

<!-- g(r, θ) = diag(1, r²) -->
$$
g(r, \theta) = \begin{pmatrix} 1 & 0 \\ 0 & r^2 \end{pmatrix}
$$

The g₂₂ entry is r² — a *function of position*. At r = 1 the entry
is 1; at r = 5 the entry is 25. So the metric matrix is *different
at different points*.

This generalizes. In any space (flat or curved, Cartesian or
exotic), the metric is best understood as a **field of matrices**:
at every point in space, there is a little matrix sitting there,
and that matrix is the local distance recipe.

Concretely, computing distance involves *two* inputs:

1. **Where you are.** This tells you which g matrix to use.
2. **Which way you stepped.** This is the (dx, dy) vector you plug
   into the sandwich.

In 2D Cartesian flat space, the matrix is the same everywhere
(g = identity), so step 1 is trivial — only the step matters. In
polar (still flat space, just curvilinear coordinates), the matrix
depends on r, so step 1 is non-trivial. In *curved* space, the
matrix can vary in even richer ways, and how it varies *is* what
we call curvature.

**In one sentence:** the metric is a function from "where you are"
to "the local distance recipe at this point."

---

## 6. Off-diagonal terms and what they mean

So far our metrics have been diagonal — the matrix has nonzero
entries only on the diagonal. That means each coordinate
contributes independently to distance: a step in x and a step in y
have no "cross talk."

A metric can have *off-diagonal* entries:

<!-- g = [[1, A], [A, 1]];  ds² = dx² + 2A dx dy + dy² -->
$$
g = \begin{pmatrix} 1 & A \\ A & 1 \end{pmatrix},
\qquad
ds^2 = dx^2 + 2A\,dx\,dy + dy^2
$$

The cross term `2A dx dy` is what off-diagonal entries produce.

Why the factor of 2? Because the metric matrix is symmetric
(g_xy = g_yx), so the (x, y) and (y, x) entries both contribute
A dx dy, and they add to give 2A dx dy. (See
[matrix-primer.md §7](matrix-primer.md) for the symmetric matrix
convention.)

**Geometric interpretation: tilted axes.** When A = 0, the
coordinate axes are perpendicular and don't mix. When A ≠ 0, the
axes are tilted relative to each other — moving in x partly counts
as moving in y. You can think of A as measuring how non-orthogonal
the coordinate system is at that point.

**Physical interpretation: fields.** In general relativity and
related theories, off-diagonal metric entries often encode physical
fields. The most famous example: in Kaluza-Klein theory, the
off-diagonal entries g_μ5 (mixing 4D spacetime directions with the
compact 5th dimension) are exactly the electromagnetic potential
A_μ. Seeing an off-diagonal entry "light up" can mean a real field
is present, not just a coordinate quirk.

So off-diagonal entries can come from two sources:

1. **Coordinate choice.** A tilted or oblique coordinate system in
   otherwise flat empty space. These are "fake" off-diagonals you
   can remove by changing coordinates.
2. **Real physics.** Genuine geometric content sourced by some
   field or stress-energy. These cannot be removed by coordinate
   changes — they are intrinsic.

Distinguishing the two is part of the work general relativity does.

---

## 7. Spacetime and the minus sign

Einstein's special relativity introduced spacetime as a
four-dimensional manifold combining time and space. The interval
between two nearby spacetime events is:

<!-- ds² = -c²dt² + dx² + dy² + dz² -->
$$
ds^2 = -c^2\,dt^2 + dx^2 + dy^2 + dz^2
$$

The minus sign on the time term is the signature feature of
spacetime. As a matrix:

<!-- g = diag(-c², 1, 1, 1) -->
$$
g_{\mu\nu} = \begin{pmatrix} -c^2 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}
$$

A metric with one negative eigenvalue (the time direction) and the
rest positive is called **Lorentzian**. (A metric with all positive
eigenvalues is **Euclidean** — ordinary 3D space, 4D Euclidean
space, etc.)

**Why the minus sign?** It is forced on us by experiment — the speed
of light is the same in every inertial frame. The mathematical
consequence of that empirical fact is that c² t² − x² − y² − z² is
the same in every inertial frame (invariant under Lorentz
transformations), while the Euclidean combination t² + x² + y² + z²
is *not* invariant. So if we want a metric that respects how
physics actually works, the time term must enter with the opposite
sign.

The c² factor on dt² is just unit-conversion: time is in seconds,
space in meters, and c² turns one into the other so the units of
ds² come out as length².

---

## 8. The light cone and interval classification

The minus sign creates a fundamentally new feature absent in
Euclidean geometry: ds² can be **positive, negative, or zero**.

| ds² value | Name | What it is |
|-----------|------|-----------|
| ds² < 0 | **time-like** | Path a massive particle can take |
| ds² = 0 | **light-like** (null) | Path of a photon |
| ds² > 0 | **space-like** | Two events too far apart for light to connect |

These three categories don't exist in Euclidean geometry — there,
distance is always non-negative. The minus sign is what creates the
classification.

**Time-like (ds² < 0).** A massive particle sitting still has
dx = dy = dz = 0 but dt > 0, so ds² = −c² dt² < 0. For *any*
massive particle in *any* frame, the spatial part can never grow
large enough to compensate (that would require v > c). So a massive
particle's path always has ds² < 0.

**Light-like (ds² = 0).** Light moves at speed c, so dx² + dy² + dz²
exactly equals c² dt², and ds² = 0. Light's path is the boundary
between time-like and space-like. Any wave equation of the form
□φ = 0 (we will define □ in §11) has solutions whose wavefronts
travel along light-like paths.

**Space-like (ds² > 0).** Two events at the same instant (dt = 0)
but different places (dx ≠ 0) have ds² = +dx² > 0. No physical
particle can be present at both events — that would require
infinite speed.

**The light cone.** At any spacetime event, the set of light-like
paths emanating from it forms a *double cone* — one cone opening
into the future, one cone opening into the past, both with their
apex (point) at "here, now":

```
   t (time)
   ↑
   │  \                            /
   │   \  future light cone       /
   │    \  (time-like interior,  /
   │     \  light-like surface) /
   │      \                    /
   │       \                  /
   │        \                /
   │         \              /
   │          \            /
  ─┼───────────●──────────●────────→  S (space)
   │          /  here ↑    \          space-like
   │         /              \
   │        /  Apex of cones \   "elsewhere"
   │       /                  \  (causally
   │      /                    \  disconnected)
   │     /   past light cone    \
   │    /  (time-like interior,  \
   │   /     light-like surface)  \
   │  /                            \
```

Inside the future cone: events you can travel to (your future).
Inside the past cone: events that could have influenced you
(your past). On either cone surface: paths a light signal can
take. Outside both cones: events too far away in space to be
causally connected to "here, now" — neither past nor future, just
"elsewhere."

**Why this matters.** The entire causal structure of physics —
past, future, "elsewhere," what can influence what — is encoded by
the minus sign and the resulting interval classification. When we
say "this field obeys the wave equation" we are saying "its
disturbances propagate on light-like paths." When we say "this
particle has rest mass" we are saying "its world-line is
time-like."

---

## 9. The metric near a mass

The Minkowski metric of §7 is the metric of empty spacetime — flat,
constant everywhere. Adding mass curves spacetime. Here is the
classic example.

**Schwarzschild (non-rotating spherical mass).** In spherical
coordinates (t, r, θ, φ) outside a mass M, the metric is:

<!-- ds² = -(1 - r_s/r) c² dt² + (1 - r_s/r)^-1 dr² + r²dθ² + r²sin²θ dφ² -->
$$
ds^2 = -\left(1 - \frac{r_s}{r}\right) c^2\,dt^2
     + \left(1 - \frac{r_s}{r}\right)^{-1} dr^2
     + r^2\,d\theta^2
     + r^2\sin^2\theta\,d\phi^2
$$

where r_s = 2GM/c² is the Schwarzschild radius. As a matrix, still
diagonal:

```
g = diag( −(1 − r_s/r),  (1 − r_s/r)^(−1),  r²,  r² sin²θ )
```

Things to notice:

- **Still diagonal.** A static spherical mass does not introduce
  off-diagonals. Only the time and radial diagonal entries get
  modified.
- **Position-dependent.** The g_tt and g_rr entries depend on r
  (and the angular ones depend on θ). So the metric is genuinely
  a field of matrices here.
- **Recovers flat space far away.** As r → ∞, r_s/r → 0, and the
  metric becomes diag(−1, 1, r², r² sin²θ) — just flat Minkowski
  in spherical coordinates. So Schwarzschild is "Minkowski plus
  corrections that fade with distance."

Physical effects encoded in the modified entries:

- g_tt = −(1 − r_s/r) means clocks tick slower deep in the gravity
  well. (Gravitational time dilation.)
- g_rr = (1 − r_s/r)^(−1) means radial rulers get stretched.

These two together are what we call gravity — the modified geodesics
in this metric reproduce orbital mechanics, light bending, and (when
r_s → r) a black hole horizon.

**When do off-diagonals appear?** When the source has rotation or
some other directional structure. The Kerr metric (rotating black
hole) has g_tφ ≠ 0 — the time and azimuthal directions mix. This
is **frame dragging**: spacetime gets dragged around by the spinning
mass. An object in free fall near a spinning black hole is forced
to co-rotate just by virtue of the geometry.

**General principle.** Whatever stress-energy is present
(via Einstein's equations) sources whichever components of the
metric have the matching symmetry. Static spherical mass → only
spherical-static-compatible diagonals. Rotating mass → also some
off-diagonals (rotation breaks static symmetry). Electromagnetic
energy → contributes to all components in principle.

---

## 10. Geodesics: free particles follow shortest paths

A **geodesic** is the path of shortest (or longest, depending on
sign conventions in spacetime) interval between two points.

In flat Euclidean space, geodesics are straight lines. On a sphere,
they are great circles. In curved spacetime, they are the paths
extremized by the metric.

The physical principle: **free particles follow geodesics**.

- In flat space, a free particle moves in a straight line. (Newton's
  first law.)
- In curved spacetime, a free particle follows a curved path that
  is "straight" according to the local metric.

When we see a particle following a curved trajectory, there are two
ways to describe it:

- **Force view.** Something pushes the particle off a straight line.
- **Geometry view.** The particle IS following a straight line, but
  the space is curved.

General relativity takes the geometry view: gravity is not a force,
it is the curvature of spacetime. Kaluza-Klein extends the same
geometry view to electromagnetism.

The geodesic equation is:

<!-- d²x^a/dτ² + Γ^a_bc (dx^b/dτ)(dx^c/dτ) = 0 -->
$$
\frac{d^2 x^a}{d\tau^2}
  + \Gamma^a_{bc}\,\frac{dx^b}{d\tau}\,\frac{dx^c}{d\tau} = 0
$$

The Γ^a_bc are *Christoffel symbols* built from derivatives of the
metric. We will not need their explicit form here — just the fact
that they encode "how the metric varies near this point" and that
the geodesic equation is determined entirely by the metric.

---

## 11. The d'Alembertian and the wave equation

Just as the metric controls how distance is measured, it controls
how *waves propagate*.

The **d'Alembertian** □ is the spacetime version of the Laplacian
∇². For 4D Cartesian Minkowski spacetime:

<!-- □ = -(1/c²)∂²/∂t² + ∂²/∂x² + ∂²/∂y² + ∂²/∂z² -->
$$
\Box = -\frac{1}{c^2}\frac{\partial^2}{\partial t^2} + \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}
$$

For an arbitrary metric, the d'Alembertian is built from the inverse
metric and partial derivatives:

<!-- □φ = sum over μ,ν of g^μν ∂_μ ∂_ν φ -->
$$
\Box\varphi = \sum_{\mu,\nu}\, g^{\mu\nu}\, \partial_\mu \partial_\nu\, \varphi
$$

Three notations to unpack:

- **∂_μ φ** means "the partial derivative of φ with respect to the
  μ-th coordinate." If μ = t, ∂_μ = ∂/∂t. The lower index μ
  labels which coordinate.
- **g^μν** (raised indices) is the **inverse** of the metric matrix
  g_μν (lowered indices). For diagonal metrics, the inverse is the
  matrix of reciprocals: g^tt = 1/g_tt, etc.
- **The sum over μ, ν** runs over all coordinates. For a 4D
  manifold, that's 4 × 4 = 16 terms (most zero if g is diagonal).

(This compact notation is sometimes written with the Σ implicit —
the *Einstein summation convention*: any pair of repeated indices,
one raised and one lowered, is summed automatically. We will write
the Σ explicitly here for clarity but you will see it dropped
elsewhere.)

The **wave equation** for a massless field is:

<!-- □φ = 0 -->
$$
\Box\varphi = 0
$$

This says: the appropriate weighted sum of second derivatives of φ,
across all directions, vanishes. Solutions are waves that propagate
at speed c — i.e., on light-like paths (ds² = 0). So *□φ = 0 is
the equation for a light-like field*: its disturbances live on the
light cones of §8.

Adding a mass to the equation gives the **Klein-Gordon equation**:

<!-- (□ - (mc/ℏ)²) φ = 0 -->
$$
\left(\Box - \left(\frac{mc}{\hbar}\right)^2\right) \varphi = 0
$$

This describes a massive scalar field. The extra term is what makes
the field's quanta have rest mass m. (Without it, the quanta are
massless.)

---

## 12. Compact dimensions

A dimension is **compact** if it has finite size but no boundary —
travel far enough in one direction and you return to where you
started.

You already know one compact coordinate: the angle θ in polar
coordinates. θ goes from 0 to 2π and then wraps — θ = 0 and
θ = 2π are the same point. The θ direction is a circle.

Now imagine a fresh coordinate w (or u, or anything) that wraps
after distance L:

<!-- w and w + L are the same point -->
$$
w \;\sim\; w + L
$$

This is a compact dimension with circumference L. Mathematically,
it is a circle, denoted **S¹** (the "1-sphere," the math name for
an ordinary circle; S² is the surface of a ball, S³ is a higher
sphere, and so on).

A compact dimension can be **flat** — zero intrinsic curvature.
Analogy: take a flat sheet of paper and roll it into a cylinder.
The paper is still flat (you can unroll it without stretching),
but one direction (around the cylinder) has become compact. A
straight line drawn on the flat sheet becomes a helix on the
cylinder, but it is still a geodesic — the shortest path on the
cylinder.

**Why compact dimensions matter for physics.** In Kaluza-Klein
theory, an extra compact spatial dimension produces electromagnetism
as a geometric consequence. In string theory, six or seven extra
compact dimensions are postulated to accommodate the standard
model. In our own MaSt project, compact directions are central to
the mass-generation story.

The key feature: if a field is required to be **single-valued** on
the compact direction (its value at w must equal its value at
w + L), then the field's momentum in the compact direction can only
take certain *quantized* values — integer multiples of 2π/L (in
wavenumber units) or equivalently nℏ/R (in momentum units, where
R = L/2π is the compact radius). This quantization is the
mechanism by which compact dimensions produce discrete, particle-
like properties from a continuous field.

---

## What's next

Equipped with the metric, geodesics, and compact dimensions, you
have the prerequisites for:

- [kaluza-klein.md](kaluza-klein.md) — the standard KK theory:
  electromagnetism as a geometric consequence of one compact
  extra dimension.
- [maxwell-primer.md](maxwell-primer.md) — Maxwell's equations
  and the four-potential A_μ, which becomes identified with
  off-diagonal metric components in KK.
- The [metric-mass project](../projects/metric-mass/) — building
  intuition by deriving mass from a single compact dimension on a
  minimal manifold.
- The R-track studies of metric configurations
  ([R60-metric-11](../studies/R60-metric-11/) and beyond).
