# Track 4: Projection coupling — how much signal transfers from 2D to 3D?

**Status:** Framing (conceptual)

---

## The question

A signal (phase, energy, information) propagates on a 2D
hexagonal lattice.  The lattice is embedded in a 3D
diamond-type lattice.  At any node where the two lattices
meet, signal on a 2D edge must couple onto a 3D edge to
enter the ambient space.

**How much of the signal transfers?**

This is not a coincidence question (Track 3: do edges
align? binary yes/no).  It is a projection question:
what fraction of the energy on a 2D edge projects onto
a 3D edge?  The answer is continuous, not binary —
determined by the angle between the edges, like a
polarizer.

---

## The physics: Malus's law on a lattice

When a wave traveling along edge A encounters edge B at
angle θ, the fraction of energy that couples onto B is:

> coupling = cos²(θ)

This is Malus's law — the same physics as light passing
through a polarizer.  cos²(0°) = 1 (perfect alignment,
full transfer).  cos²(90°) = 0 (perpendicular, no
transfer).  cos²(45°) = 0.5 (half transfers).

The specific phase value (the information content at any
instant) doesn't matter.  What matters is the GEOMETRIC
EFFICIENCY — what fraction of whatever signal exists on
edge A gets projected onto edge B.  The signal is the
information.  The projection is the coupling.

---

## The setup

**The 2D wye:** 3 edges in a plane at 120° separation.
Each edge carries signal — phase propagating along the
hexagonal lattice.

**The 3D jack:** 4 edges at tetrahedral angles (109.47°).
Each edge carries signal — phase propagating along the
diamond lattice.

**At a shared node:** a signal arriving on a wye edge
encounters the 4 jack edges.  For each jack edge, the
coupling is cos²(angle between the wye edge and the jack
edge).  The total coupling FROM one wye edge INTO the
jack is the sum over all 4 jack edges:

> C_k = Σ_j cos²(θ_kj)

where θ_kj is the angle between wye edge k and jack
edge j.

**The total coupling from the entire wye into the jack**
is the average over the 3 wye edges:

> C_total = (1/3) Σ_k Σ_j cos²(θ_kj)

This is a single number — the average fraction of wye
signal that projects onto the jack, for a given relative
orientation of the wye plane in the jack.

---

## What to compute

### Step 1: Fixed orientation

At a specific (θ, φ, ψ), compute C_total.  This is a
3×4 matrix of cos² values, summed and averaged.  Pure
dot products of known unit vectors — no numerical search,
no tolerance, exact.

### Step 2: Sweep over orientations

Compute C_total(θ, φ, ψ) over the full orientation
sphere.  This gives the coupling as a function of how the
2D sheet is oriented in 3D.

Key questions:
- What is C_total at the ⟨111⟩ magic angles?
- What is C_total at generic angles?
- What is the AVERAGE C_total over all orientations?
- What is the MINIMUM C_total (worst coupling)?
- What is the DISTRIBUTION of C_total values?

### Step 3: The torus integral

A torus embedded in the 3D lattice has its surface normal
sweeping through orientations as you go around.  The
coupling at each surface patch is C_total(θ(s), φ(s),
ψ(s)).  The average coupling over the torus surface is:

> α_torus = (1/A) ∮ C_total(θ, φ, ψ) dA

This depends on the torus geometry (ε, embedding
orientation).

**The hypothesis:** α_torus = 1/137 at a specific ε.

### Step 4: Normalization

The raw C_total is the fraction of wye energy that
projects onto jack edges.  But this needs normalization:

**Option A:** C_total / C_max, where C_max is the maximum
possible coupling (at the magic angle).  This gives a
ratio between 0 and 1.

**Option B:** C_total as an absolute fraction.  A single
vector projected onto 4 tetrahedral directions has
Σ cos²(θ_j) = 4/3 (by the identity for tetrahedral
vectors: Σ_j (ê · d_j)² = 4/3 for any unit ê, when
d_j are the 4 tetrahedral directions).  For 3 wye
edges: the sum is 3 × 4/3 = 4.  Divided by the number
of pairs (12): C_avg = 4/12 = 1/3.

So the AVERAGE projection fraction over random
orientations is 1/3 — not 1/137.  This is too large.

**Option C:** not the average projection, but the
DIFFERENCE between the magic-angle coupling and the
average coupling.  Or: the variance of C_total across
orientations.  Or: the fraction of the torus surface
where C_total exceeds some threshold.

The right normalization determines what quantity we're
comparing to 1/137.

---

## Why this might work (and why it might not)

### Why it might work

- The projection ratio is a pure geometric quantity —
  no free parameters, no tolerance
- It depends on the specific angles (120° vs 109.47°)
  in a non-trivial way
- The torus integral introduces ε dependence, allowing
  the ratio to vary with geometry
- Track 3 Step 1 showed that the 19.47° barrier is the
  fundamental mismatch; the cos²(19.47°) = 0.889 — the
  fraction of energy that couples at the magic angle
  (11.1% is lost to the angular mismatch)

### Why it might not work

- The average projection (1/3) is a consequence of the
  tetrahedral symmetry identity Σ (ê·d_j)² = 4/3.
  This might overwhelm any angle-specific structure.
- The coupling might be the same at all orientations
  (if the tetrahedral symmetry makes C_total constant
  over the sphere — which it does for the sum Σ_j
  cos²(θ_j) for a SINGLE vector, but might not for 3
  wye vectors simultaneously).
- 1/137 is a very specific number.  Generic geometric
  ratios tend to give simple fractions.

### The critical check

Does C_total VARY with (θ, φ, ψ), or is it constant?

If constant (same at all orientations): the coupling
fraction is a universal number, independent of how the
sheet is oriented.  If that number is 1/137, we're done.
If not, this approach can't produce α.

If variable: the torus integral becomes meaningful, and
α could emerge from the torus geometry.

**This is computable in one line of algebra** for the
sum Σ_k Σ_j cos²(θ_kj) — it may simplify to a constant
or it may depend on orientation.  Check this BEFORE
running any numerical sweep.

---

## The analytical test

The sum Σ_j (ê·d_j)² = 4/3 for ANY unit vector ê when
d_j are the 4 tetrahedral directions.  This is a
well-known identity.

For 3 wye vectors ê_1, ê_2, ê_3 at 120° in a plane:

> Σ_k Σ_j (ê_k · d_j)² = Σ_k [4/3] = 3 × 4/3 = 4

**This is constant — independent of orientation.**

So C_total = 4/12 = 1/3 at ALL orientations.  The
tetrahedral symmetry makes the total projection fraction
exactly 1/3 regardless of how the wye plane is tilted.

**This kills the simplest version of Track 4.** The
cos²-weighted coupling is 1/3 everywhere, not 1/137.
There is no orientation dependence and no torus integral
to evaluate.

### But...

The identity Σ (ê·d_j)² = 4/3 holds because the four
tetrahedral directions form a spherical 2-design — they
perfectly sample the sphere for quadratic functions.  The
sum of squared projections is the same for any input
direction.

However, this identity applies to cos² (intensity/energy
coupling).  The amplitude coupling is |cos(θ)|, not
cos²(θ).  The sum Σ |ê·d_j| is NOT constant — it depends
on orientation.  If the physical coupling goes as
AMPLITUDE (not intensity), the projection ratio varies
with orientation and the torus integral becomes
meaningful.

Similarly, if the coupling is directional (signed: cos θ
rather than cos² θ or |cos θ|), the sum Σ (ê·d_j)
depends on orientation (it's related to the dipole
moment of the tetrahedron, which is zero by symmetry for
the FULL sum but nonzero for partial sums).

**The question of whether coupling goes as cos², |cos|,
or cos determines whether Track 4 has any content.**
This is a physics question, not a geometry question:
does the lattice gauge coupling transfer amplitude
(first power) or intensity (second power)?

In lattice gauge theory, the coupling at a junction goes
as the REAL PART of the link variable product — which is
cos(phase difference), a signed first-power quantity.
This means the relevant sum is Σ cos(θ), not Σ cos²(θ).
And Σ_j (ê · d_j) = 0 for the full tetrahedron (by
symmetry: the four directions sum to zero).

**So:** for amplitude coupling (cos θ), the sum over all
4 jack edges is zero.  For energy coupling (cos² θ), the
sum is 4/3 (constant).  Neither gives 1/137.

This requires a rethink of what "coupling" means at the
junction.  The signal doesn't couple to ALL jack edges
simultaneously — it couples to the NEAREST jack edge (the
one closest in angle).  The coupling to the nearest edge
is cos²(θ_min), and θ_min varies with orientation.  THIS
quantity is NOT constant and could give a non-trivial
torus integral.

---

## Revised approach: nearest-edge coupling

Instead of projecting onto all 4 jack edges (which gives
a constant), project onto the NEAREST jack edge only.

At each orientation (θ, φ, ψ), for each wye edge k, find
the jack edge j that is closest in angle.  The coupling
for that wye edge is cos²(θ_kj_min).  The average over
the 3 wye edges is:

> C_nearest(θ, φ, ψ) = (1/3) Σ_k cos²(θ_k,nearest)

This DOES vary with orientation — at the magic angle,
θ_nearest = 19.47° → cos²(19.47°) = 0.889.  At generic
angles, θ_nearest is larger → coupling is weaker.

**This is the physically motivated quantity:** at a
lattice junction, signal arriving on one edge doesn't
spray into all outgoing edges equally.  It preferentially
couples to the most closely aligned outgoing edge.

### What to compute (revised)

1. C_nearest(θ, φ, ψ) over the orientation sphere
2. The average, minimum, maximum, and distribution
3. The torus integral at various ε
4. Compare to 1/137

**Script:** `scripts/track4_projection_coupling.py` (planned)
