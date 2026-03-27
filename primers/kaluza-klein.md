# Kaluza-Klein Theory — A Ground-Up Introduction

A self-contained introduction to Kaluza-Klein (KK) theory,
starting from coordinates and distance and ending with
electromagnetism emerging from geometry. Assumes calculus,
vectors, and matrices. No prior exposure to general relativity
or differential geometry is needed.

---

## 1. Coordinates and distance

Everything starts with measuring distance.

In a plane, the distance between two nearby points is the
Pythagorean theorem:

    ds² = dx² + dy²

This says: if you step dx to the right and dy upward, the total
distance you've traveled (squared) is dx² + dy². In 3D:

    ds² = dx² + dy² + dz²

The "ds²" notation means the square of an infinitesimal distance
— the distance between two points that are infinitely close. Why
infinitesimal? Because in curved space the formula changes from
place to place, so it's only exactly right for tiny steps. For
flat space it works at any scale.

**Spacetime.** Einstein showed that time and space are intertwined.
The spacetime "distance" (called the interval) between two nearby
events is:

    ds² = −c²dt² + dx² + dy² + dz²

The minus sign on the time term is the key difference between
space and time. We won't need the details — just the fact that
spacetime distance is a real, computable thing, and it governs
how particles move.


## 2. The metric: the distance recipe

The formula ds² = dx² + dy² is specific to Cartesian coordinates
in flat space. Switch to polar coordinates (r, θ) and the same
flat plane has a different-looking distance formula:

    ds² = dr² + r² dθ²

The geometry hasn't changed — it's still a flat plane. But the
recipe for computing distance from coordinate differences has
changed. This recipe is called the **metric**.

We can write the metric as a matrix. In 2D Cartesian:

    ds² = dx² + dy²

    g = | 1  0 |
        | 0  1 |

    ds² = [dx, dy] · g · [dx, dy]ᵀ

In polar coordinates:

    ds² = dr² + r² dθ²

    g = | 1   0  |
        | 0   r² |

Same flat plane, different metric matrix. The metric encodes both
the geometry of the space AND the coordinate system.

**Why this matters:** the metric is the fundamental object in
general relativity. If you know the metric, you know everything
about the geometry — distances, angles, curvature, and how
particles move.


## 3. Off-diagonal terms and mixing

So far our metrics have been diagonal — each coordinate contributes
independently to the distance. But metrics can have off-diagonal
terms. Consider a 2D metric:

    g = | 1  A |
        | A  1 |

    ds² = dx² + 2A dx dy + dy²

The cross term 2A dx dy means the coordinates are "mixed" — moving
in x also partly counts as moving in y. You can think of this as
the axes being tilted rather than perpendicular.

When A = 0, the axes are orthogonal. When A ≠ 0, they're tilted.
Motion in one direction drags you in the other.

This will be the key to understanding electromagnetism as geometry.


## 4. Geodesics: the shortest path

A **geodesic** is the path of shortest distance between two points.
In flat space, geodesics are straight lines. On a sphere, they're
great circles. In general, the metric determines what "shortest"
means, so different metrics give different geodesics.

The important physical principle: **free particles follow
geodesics.** In flat space, a free particle moves in a straight
line (Newton's first law). In curved space, a free particle follows
a geodesic — a curved path that is "straight" according to the
local geometry.

When we see a particle following a curved path, we can explain it
two ways:
- **Force:** something pushes the particle off a straight line
- **Geometry:** the particle IS following a straight line, but in
  a curved space

General relativity takes the geometry view for gravity. Kaluza-Klein
takes the geometry view for electromagnetism.


## 5. General relativity in brief

Einstein's insight: gravity is not a force. Mass and energy curve
spacetime — they change the metric. Free particles follow geodesics
in this curved spacetime, and those geodesics look like the
trajectories of particles accelerating under gravity.

The metric near a massive object (like Earth) differs slightly from
the flat spacetime metric. This difference is what makes objects
fall. The "force" of gravity is really just the curvature of the
shortest path.

**Einstein's field equations** relate the curvature of the metric
to the energy and momentum present. We won't need the explicit
equations — just the principle:

    Energy/momentum → determines → metric → determines → geodesics

This chain is the entire content of general relativity. If you
know the metric, you can compute how everything moves.


## 6. What "compact" means

A dimension is **compact** if it has finite size but no boundary.
Travel far enough in one direction, and you return to where you
started.

You already know a compact coordinate: the angle θ in polar
coordinates. θ goes from 0 to 2π and then wraps — θ = 0 is the
same point as θ = 2π. The θ direction is a circle of circumference
2π (in radians) or 2πr (in distance units at radius r).

Now imagine a new coordinate w that wraps after distance L:

    w  and  w + L  are the same point

This is a compact dimension with circumference L. Mathematically,
it's a circle, written S¹.

A compact dimension can be **flat** — zero intrinsic curvature.
Analogy: wrap a flat sheet of paper into a cylinder. The paper is
still flat (you can unroll it without stretching), but the
circumference direction is compact. A straight line drawn on the
flat sheet becomes a helix on the cylinder, but it's still a
geodesic — the shortest path.


## 7. Kaluza's idea: a fifth dimension

In 1921, Theodor Kaluza asked: what if spacetime has one more
dimension than we observe?

In ordinary 4D spacetime, coordinates are (t, x, y, z) and the
metric is a 4×4 matrix. Add a fifth coordinate w. Now the metric
is a 5×5 matrix.

The 5D distance formula could be written as a single expression
— g_AB dx^A dx^B with A,B running over all five coordinates —
but that would bury the physics inside a 25-term sum. Instead,
we split the 5×5 matrix into three groups, each with a distinct
physical meaning:

    ds² = g_μν dx^μ dx^ν + g₅₅ dw² + 2 g_μ5 dx^μ dw
          ───────┬──────   ────┬────   ──────┬──────
          spacetime×space   w×w        spacetime×w
          = gravity         = scalar   = electromagnetism

Here μ and ν each run over {t, x, y, z} — the four spacetime
coordinates. The expression g_μν dx^μ dx^ν uses index notation
(see `matrix-primer.md` §9): it means "sum over all combinations
of μ and ν," which is 4×4 = 16 terms — the spacetime metric.

The factor of 2 on the cross terms has the same origin as in the
matrix primer (§7): the metric matrix is symmetric (g_μ5 = g_5μ),
so the terms with indices (μ,5) and (5,μ) are equal and combine.

For example, in just 2D:

    g_μν dx^μ dx^ν = g₁₁ dx¹ dx¹ + g₁₂ dx¹ dx² + g₂₁ dx² dx¹ + g₂₂ dx² dx²

which is just the matrix product [dx¹, dx²] · g · [dx¹, dx²]ᵀ.

The three groups of terms in the 5D metric:

| Terms | What they are | Physical meaning |
|-------|---------------|------------------|
| g_μν dx^μ dx^ν | 4D spacetime metric | Gravity |
| g₅₅ dw² | Length of the extra dimension | A scalar field (the "dilaton") |
| 2 g_μ5 dx^μ dw | Cross terms mixing w with spacetime | **Electromagnetism** |

The cross terms are the key. They connect to the electromagnetic
potential — the four-number object A_μ from which all electric
and magnetic fields are derived. (For a full review of Maxwell's
equations, potentials, and A_μ, see [`maxwell-primer.md`](maxwell-primer.md).
The short version follows.)

In electromagnetism, the E and B fields (6 components total) can
all be derived from just 4 numbers called the **four-potential**:

    A_μ = (φ/c, A_x, A_y, A_z)

where φ is the scalar potential (voltage) and **A** is the vector
potential. The fields come from derivatives of the potentials:

    E = −∇φ − ∂A/∂t       (E points "downhill" from high voltage)
    B = ∇ × A              (B is the "swirl" of A)

Kaluza's identification: the four cross terms of the 5D metric
ARE the four-potential:

    g_μ5 = A_μ

The metric cross terms (how much the compact dimension tilts
relative to each spacetime direction) and the electromagnetic
potential (the object whose derivatives give E and B) are the
same mathematical object. If you know the 5D metric, you know
the electromagnetic field.

This is why the three-way split matters. The cross terms between
spacetime and the compact dimension aren't just "some off-diagonal
entries" — they are electromagnetism, encoded in the geometry of
the extra dimension.


## 8. What the cross terms do physically

When A_μ = 0 (no electromagnetic field), the 5D metric has no
cross terms. The compact dimension w is perfectly orthogonal to
spacetime. Motion in w doesn't affect motion in spacetime, and
vice versa.

When A_μ ≠ 0, moving through spacetime drags you in the w
direction (and vice versa). The 5D distance formula becomes:

    ds² = g_μν dx^μ dx^ν + (dw + A_μ dx^μ)²

Expanding the squared term:

    (dw + A_μ dx^μ)² = dw² + 2 A_μ dw dx^μ + A_μ A_ν dx^μ dx^ν

The middle term (2 A_μ dw dx^μ) is the cross term that mixes the
dimensions. The last term (A_μ A_ν dx^μ dx^ν) is a small
correction to the spacetime metric from the electromagnetic field
energy.

**Physical picture:** imagine walking on a conveyor belt that runs
at an angle to your path. Your forward motion carries you sideways
(the cross term). How much you drift sideways depends on your
speed and the belt's tilt (A_μ). If you also have momentum in the
sideways direction (momentum in w = charge), the belt accelerates
you forward. This acceleration is the electromagnetic force.


## 9. Klein's contribution: compactification

In 1926, Oskar Klein made Kaluza's idea physical by making the
fifth dimension compact:

    w ~ w + L

The coordinate w wraps with circumference L. This has a profound
consequence.

**Quantization.** A particle has a wavefunction ψ that must be
single-valued — if you go around the compact dimension and return
to the same point, the wavefunction must return to the same value:

    ψ(w + L) = ψ(w)

The solutions are:

    ψ(w) = exp(i n w 2π / L)    for  n = 0, ±1, ±2, ...

where n is an integer. The momentum in the w direction is:

    p_w = n ℏ / R

where R = L / (2π) is the compact radius and ℏ is the reduced
Planck constant.

**The key identification:** this quantized momentum is electric
charge.

    q = p_w / c = n ℏ / (R c)

A particle with n = 0 has no momentum in w — it's neutral. A
particle with n = +1 has one unit of momentum in w — it carries
charge +e. A particle with n = −1 carries charge −e.

The elementary charge is:

    e = ℏ / (R c)

Solving for R:

    R = ℏ / (e c) ≈ 2 × 10⁻³⁴ m

This is extraordinarily small — far below anything we can probe
experimentally, which is why we don't "see" the extra dimension.
(The exact value depends on normalization conventions for how
the metric couples to matter; the order of magnitude is robust.)


## 10. What falls out

From the 5D Einstein field equations (applied to the 5×5 metric),
three sets of equations emerge:

| 5D equations | 4D result |
|--------------|-----------|
| Spacetime-spacetime components | Einstein's equations (gravity) |
| Spacetime-w components | **Maxwell's equations** (electromagnetism) |
| w-w component | Scalar field equation (dilaton) |

From the 5D geodesic equation (the equation of motion for a free
particle in 5D), you get:

    4D geodesic (gravity) + Lorentz force (electromagnetism)

A free particle in 5D, which just follows a straight line, looks
like a charged particle being deflected by electromagnetic fields
in 4D.

These results are **exact** — not approximations, analogies, or
heuristics. They are consequences of the mathematics of the 5×5
metric. Maxwell's equations are literally the Einstein equations
applied to the off-diagonal metric components.

**Summary:**

| Physical concept | KK geometric origin |
|------------------|---------------------|
| EM potential A_μ | Off-diagonal metric g_μ5 |
| Electric charge | Momentum in compact dimension |
| Charge quantization | Periodicity of compact dimension |
| Charge conservation | Translation symmetry in w (Noether's theorem) |
| Lorentz force | Geodesic equation in 5D |
| Maxwell's equations | Einstein equations in 5D |
| Gauge transformation | Coordinate shift in w |


## 11. Charge conservation from symmetry

A powerful result comes from Noether's theorem, which says: every
continuous symmetry of the physics corresponds to a conserved
quantity.

In ordinary 3D space:
- Translation symmetry in x → momentum p_x is conserved
- Translation symmetry in y → momentum p_y is conserved
- Rotation symmetry → angular momentum L is conserved

In KK:
- Translation symmetry in w → momentum p_w is conserved
- But p_w is charge
- Therefore **charge is conserved**

This is not a separate postulate — it follows from the geometry.
If the metric doesn't depend on w (the compact dimension "looks
the same" everywhere along its circumference), then momentum in
w is conserved, which means charge is conserved.

This is the same reason momentum is conserved: space looks the
same at every point (translation symmetry). Charge conservation
and momentum conservation are the same theorem applied to
different dimensions.


## 12. Geodesics in 5D: where the force comes from

Consider a particle with momentum p_w = q c in the compact
direction, moving through a region where A_μ ≠ 0. The 5D
geodesic equation (shortest path in 5D) produces, when projected
to 4D:

    (4D acceleration) = (gravitational terms) + q (E + v × B)

The second term is the **Lorentz force** — the force on a charge
q in electric field E and magnetic field B, where v is the
particle's velocity. This is exact.

The particle isn't being pushed by a force — it's following a
straight line in 5D. But because the compact dimension is tilted
by the EM field (A_μ ≠ 0), a "straight line" in 5D projects to
a curved path in 4D. We interpret that curvature as the effect
of an electromagnetic force, just as we interpret the curvature
of an orbit around Earth as the effect of gravitational force.


## 13. An analogy: the tilted conveyor belt

Imagine a long hallway with a moving floor (like an airport
walkway), but the walkway runs at an angle to the hallway. The
floor's velocity field is A(x) — it varies along the hallway.

- A person standing still (p_w = 0, neutral) is not affected by
  the walkway's angle — they don't move.
- A person walking in the walkway direction (p_w ≠ 0, charged)
  gets carried sideways by the angle — they experience a force.
- The faster they walk in the walkway direction (more charge),
  the stronger the sideways deflection.
- If the walkway angle varies (A changes with position), the
  deflection varies — this is the electromagnetic field.

This analogy captures the essential mechanism: charge is motion
in a hidden direction, and the electromagnetic force is a
geometric consequence of that direction being tilted relative to
the directions we can see.


## 14. What is established vs. what is hypothetical

**Established (proven mathematically, not disputed):**
- The 5D → 4D decomposition is exact
- Maxwell's equations emerge from the 5D Einstein equations
- Charge quantization follows from periodicity
- Geodesics in 5D give the Lorentz force in 4D
- Noether's theorem gives charge conservation

These are mathematical facts — true regardless of whether nature
actually has compact dimensions.

**Hypothetical (not observed, not disproven):**
- Whether nature actually has compact extra dimensions
- The size of any such dimensions
- Whether the dilaton scalar field exists

LHC searches constrain compact dimension sizes to be smaller than
~10⁻¹⁹ m. This doesn't rule them out — KK predicts R ~ 10⁻³⁴ m,
which is far smaller than current experimental reach.

**Known limitations:**
- The compact radius R is a free parameter. KK doesn't predict
  its value, and hence doesn't predict the value of e (or α).
- Simple KK (one compact dimension) only produces U(1) gauge
  symmetry — electromagnetism. The strong force (SU(3)) and weak
  force (SU(2)) require additional compact dimensions with more
  complex topology. This is part of the motivation for string
  theory's 6–7 extra dimensions.
- KK predicts a scalar field (dilaton) from g₅₅. This field has
  not been observed.


## 15. The essential insight

Kaluza-Klein theory says:

> **Electromagnetism is what gravity looks like when there is a
> small, compact extra dimension.**

The electromagnetic field is the shape of the extra dimension. 
Charge is momentum in the extra dimension. The force on a charged
particle is the curvature of the shortest path through the extra
dimension. All of electromagnetism — fields, forces, charge
quantization, charge conservation, Maxwell's equations — is
geometry.

Whether nature actually works this way is unknown. But the
mathematical machinery is exact, and it provides a framework in
which questions about charge, confinement, and particle structure
can be formulated precisely.

---

*See also: `studies/R1-kk-charge/theory.md` for how this framework
extends to two material dimensions and connects to the WvM electron
model.*
