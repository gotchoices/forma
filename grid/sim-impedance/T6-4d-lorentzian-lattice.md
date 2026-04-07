# Track 6: Node coincidence in a 4D Lorentzian lattice

**Status:** Framing

---

## Premise

Tracks 3-5 investigated the coupling between a 2D
hexagonal lattice and a 3D diamond lattice.  Results:

- Track 3: edge alignment exists at discrete angles;
  fraction = 1/137 at tolerance ~2.2° (free parameter)
- Track 4: total cos² projection is constant (4/3 per
  edge) — tetrahedral 2-design identity
- Track 5: coherent wavefront transfer is constant
  (T = 2, η = 1) — 2-design kills ALL quadratic coupling

The 2-design symmetry of the Euclidean tetrahedron
prevents any orientation-dependent coupling at a single
junction.

**But GRID is not 3D Euclidean.  GRID is 4D Lorentzian.**

Axiom A1: four-dimensional lattice.  Axiom A2: one
dimension is timelike with a minus sign.  The lattice
has Minkowski signature (−,+,+,+), not Euclidean
(+,+,+,+).

A Lorentzian simplex is NOT a spherical 2-design.  The
timelike direction breaks the isotropy.  Coupling between
a 2D sheet and the 4D Lorentzian lattice SHOULD depend
on orientation — specifically, on how much of the sheet's
normal points in the timelike direction.

Track 6 computes the node coincidence rate between a 2D
hexagonal lattice and the 4D Lorentzian simplex lattice.

---

## The simplex progression

The natural lattice in each dimension uses the regular
simplex as the coordination geometry:

| Dim | Edges/node | Simplex | Angle between edges | Lattice type |
|-----|-----------|---------|--------------------:|-------------|
| 2D | 3 | Triangle | 120.00° = arccos(−1/2) | Honeycomb |
| 3D | 4 | Tetrahedron | 109.47° = arccos(−1/3) | Diamond |
| 4D | 5 | 4-simplex | 104.48° = arccos(−1/4) | D4 diamond analog |

Each lattice is bipartite (two sublattices, edges only
between sublattices — like the honeycomb in 2D and
diamond in 3D).  Each node connects to n+1 neighbors
in directions pointing toward the vertices of the regular
n-simplex.  All edges have the same length L.

The angular mismatch between the 2D lattice (120°) and
the nD lattice grows with dimension:

| Coupling | Mismatch from 120° |
|----------|-------------------:|
| 2D → 2D | 0.00° |
| 2D → 3D | 10.53° |
| 2D → 4D | 15.52° |

---

## The Lorentzian 4-simplex

In Euclidean 4D, the 5 simplex directions are all
equivalent — the angle between any pair is arccos(−1/4)
= 104.48°.

In Lorentzian 4D, one direction is timelike.  The 5
edges from a node split into:

- **4 spacelike edges:** spatial directions, metric
  interval ds² = +L²
- **1 timelike edge:** temporal direction, metric interval
  ds² = −L²

In natural units, L = 1 and τ = 1 (one Planck length,
one Planck time, c = L/τ = 1).  Both edge types have
coordinate length 1 in their respective dimensions.
But the metric treats them differently:

> ds²(spacelike) = +1
> ds²(timelike) = −1

### Angles in Lorentzian geometry

The "angle" between two edges uses the Minkowski inner
product:

> cos θ_M = (a · b)_η / (|a|_η × |b|_η)

where (a · b)_η = η_μν a^μ b^ν with η = diag(−1,+1,+1,+1).

For two spacelike edges: the Minkowski angle is close
to the Euclidean angle but modified by the timelike
components.

For a spacelike edge and the timelike edge: the Minkowski
"angle" involves a hyperbolic rotation (boost) rather
than a circular rotation.  This is fundamentally different
from the spatial angles.

**The Lorentzian simplex is NOT a spherical 2-design.**
The isotropy is broken by the timelike direction.
Quadratic coupling measures (cos², dot products) are
NOT constant over all orientations — they depend on the
angle between the 2D plane and the timelike axis.

This is why Track 6 might succeed where Tracks 4-5 failed.

### Constructing the 5 edge directions

The 4 spacelike edges should reduce to the familiar
tetrahedral jack when projected onto the 3 spatial
dimensions.  The 5th (timelike) edge points purely in
the time direction.

A candidate set of 5 edge directions in (t, x, y, z):

**Option A — Euclidean 4-simplex:**

The 5 vertices of the regular 4-simplex in 4D (centered
at origin, edge length √2 for convenience):

```
d₁ = (+1, +1, +1, −1/√5) / norm
d₂ = (+1, −1, −1, −1/√5) / norm
d₃ = (−1, +1, −1, −1/√5) / norm
d₄ = (−1, −1, +1, −1/√5) / norm
d₅ = (0,   0,  0, +4/√5) / norm
```

(with the 4th component as the "time" direction)
All pairwise Euclidean angles = arccos(−1/4) = 104.48°.

**Option B — Lorentzian split (physical):**

The 3 spatial dimensions carry the tetrahedral jack
(4 edges at 109.47°).  The time dimension adds a 5th
edge.  The 5th edge should make equal Minkowski "angles"
with each spatial edge.

```
d₁ = (0,  +1, +1, +1) / √3    (spatial, tetrahedral)
d₂ = (0,  +1, −1, −1) / √3    (spatial)
d₃ = (0,  −1, +1, −1) / √3    (spatial)
d₄ = (0,  −1, −1, +1) / √3    (spatial)
d₅ = (1,   0,  0,  0)           (purely timelike)
```

In this construction:
- Spatial edges are tetrahedral (109.47° pairwise)
- The timelike edge is orthogonal to ALL spatial edges
  in the Euclidean sense, but has Minkowski interval
  ds² = −1
- The Minkowski inner product of any spatial edge with
  the timelike edge is: η(d_spatial, d₅) = −0 + 0 = 0
  (orthogonal in both Euclidean and Minkowski sense)

This might be too simple — the timelike edge is
completely decoupled from the spatial ones.  A more
physical construction might tilt the timelike edge
relative to the spatial ones (as a Euclidean 4-simplex
would).

**Option C — True 4-simplex with Lorentzian interpretation:**

Use the Euclidean 4-simplex directions but interpret
the 4th coordinate as time with metric (−,+,+,+).
The 5 directions then have both spatial and temporal
components.  The Minkowski inner products are different
from the Euclidean inner products, breaking the 2-design
symmetry.

**Track 6 should test all three options** and determine
which is physically appropriate for GRID.

---

## The lattice in 4D

### The bipartite simplex lattice

Generalizing from 2D and 3D:

| Dimension | Sublattice A | Sublattice B | Connection |
|-----------|-------------|-------------|-----------|
| 2D | Triangular lattice | Offset triangular | Each A connects to 3 B's (and vice versa) |
| 3D | FCC lattice | Offset FCC (by ¼,¼,¼) | Each A connects to 4 B's = diamond |
| 4D | D4 lattice | Offset D4 | Each A connects to 5 B's |

The D4 lattice in 4D is the root lattice of the D4 Lie
algebra.  It consists of all integer-coordinate points
(x₁, x₂, x₃, x₄) where x₁ + x₂ + x₃ + x₄ is even.
The offset sublattice shifts by (½, ½, ½, ½).

**D4 is the densest lattice packing in 4D** — the analog
of FCC in 3D.  The diamond analog (two interpenetrating
D4 lattices) would be the natural 4D GRID lattice.

### Edge properties

In the D4 diamond lattice:
- Each node has 5 nearest neighbors (the 5 simplex
  directions from the offset sublattice)
- All nearest-neighbor distances are equal
- The lattice fills 4D space with no gaps

With Lorentzian signature, one of the 4 coordinates
is timelike.  The lattice still fills 4D but the metric
is (−,+,+,+) instead of (+,+,+,+).

---

## What to compute

### Step 0: Euclidean 4D first (isolate the dimensional effect)

Before introducing Lorentzian complications, test the
pure dimensional effect: does going from 3D to 4D (with
the tighter 104.48° angles and 5 edges per node) change
the node coincidence rate enough to approach 1/137?

**Rationale:** there are two potentially independent
effects:

1. **The dimensional effect:** more edges to scatter into
   (5 vs 4), tighter angles (104.48° vs 109.47°), and
   one more dimension to "miss" when a 2D plane slices
   through the lattice.  These are purely geometric and
   don't require Lorentzian signature.

2. **The Lorentzian effect:** the timelike direction
   breaks the simplex symmetry, making the coupling
   orientation-dependent (where the Euclidean 2-design
   symmetry made it constant in 3D).

Step 0 tests effect #1 in isolation.  If the Euclidean
4D result is already ~1/137, the Lorentzian signature is
a refinement, not the primary mechanism.  If it gives
something else (say ~1/100), the Lorentzian correction
is what adjusts it.  If it gives ~1/20 (same as 3D),
the dimensional effect is negligible and only the
Lorentzian effect matters.

**Method:**

1. Build the Euclidean D4 diamond lattice (5 edges per
   node, all equal length, all pairwise angles 104.48°)
   in a region of Euclidean 4D (~10⁴ nodes).

2. Embed a 2D hexagonal lattice on a plane at various
   orientations.  In Euclidean 4D, a 2D plane is
   parameterized by 4 angles (Grassmannian Gr(2,4)).

3. Count node coincidences as in Track 1: how many 2D
   hexagonal nodes sit on 4D lattice nodes within
   tolerance δ?

4. Sweep orientations.  Report the coincidence rate.
   Compare to Track 1's 3D result (~1/20) and to 1/137.

5. Vary the tolerance δ and check scaling (as in Track 3
   Step 1).  If the coincidence fraction = 1/137 at some
   natural δ, the dimensional effect alone produces α.

**Decision point:**
- If ~1/137: Euclidean 4D is sufficient.  Steps 1-5
  (Lorentzian) may still be interesting for understanding
  the symmetry breaking but are not needed for α.
- If ~1/100: close — Lorentzian correction may bridge
  the gap.  Proceed to Steps 1-5.
- If ~1/20: no dimensional effect.  The extra dimension
  doesn't help.  Lorentzian signature is the only hope.
- If ~1/1000: the 4D lattice is TOO sparse for 2D
  coincidence.  Track 6 is unlikely to produce α.

**Scattering analysis (complement to coincidence):**

Even if node coincidence doesn't give 1/137 directly,
the SCATTERING at a 4D junction may.  At a shared node
where 3 wye edges meet 5 jack edges (total 8), the
scattering rule distributes energy across 8 channels.
The fraction going from wye to jack edges is 5/8 of the
scattered energy (vs 4/7 in 3D).  The FORWARD fraction
(energy continuing as a coherent wave) depends on the
104.48° angles.

Compute the forward scattering fraction analytically
(same approach as Track 5 but with 5 jack edges at
104.48° instead of 4 at 109.47°).  Check whether the
Euclidean 4-simplex is ALSO a 2-design (which would
make the coupling constant again) or whether 5 directions
in 4D break the symmetry.

Note: the regular 4-simplex (5 vertices in 4D) IS a
spherical 2-design in 4D.  This means Track 5's deadlock
(constant coupling at all orientations) would recur in
Euclidean 4D.  **If so, the per-junction coupling is
constant in ALL Euclidean dimensions** — only the
Lorentzian signature can break it.  This would make
Step 0's scattering analysis a quick negative, but the
node coincidence counting might still vary with
orientation (it's a lattice property, not a single-
junction property).


### Step 1: Construct the 4D lattice

Generate nodes of the D4 diamond lattice in a region
of 4D space (~10⁴ nodes).  Both sublattices.

If Lorentzian: the 4th coordinate is time.  Nodes at
t = 0, t = ±1, t = ±2, ... (the lattice extends in
time as well as space).  A 2D sheet at a fixed time
(or at a time-tilted orientation) intersects different
numbers of nodes depending on the tilt.

### Step 2: Embed the 2D hexagonal lattice

A 2D hexagonal lattice on a plane in 4D is specified by:
- A point (the origin, placed at a lattice node)
- Two basis vectors defining the plane (or equivalently,
  a normal 2-plane: 2 orthogonal directions perpendicular
  to the sheet)

In 4D, a 2D plane has a 2D normal space (not a 1D normal
like in 3D).  The orientation of the plane is described
by a point on the Grassmannian Gr(2,4) — the space of
2-planes in 4D.  This has dimension 4 (not 2 or 3 as in
the 3D case).

For a Lorentzian lattice, the plane can be:
- **Purely spatial:** both basis vectors are spacelike.
  The normal 2-plane includes the timelike direction.
  This is a "spatial slice" — the sheet lives in space
  at a fixed time.
- **Partially timelike:** one basis vector has a timelike
  component.  The sheet extends partly in the time
  direction.  This is a "worldsheet."
- The angle between the sheet and the timelike axis is
  the physically meaningful parameter.

### Step 3: Count node coincidences

At each orientation of the 2D plane in 4D, count how
many 2D hexagonal nodes sit on 4D lattice nodes.

Report:
- Coincidence rate as a function of the 4 orientation
  parameters
- The rate for purely spatial planes (conventional 3D
  embedding — should reproduce Track 1-like results)
- The rate for tilted planes (partially timelike — the
  NEW content)
- Whether the Lorentzian signature produces orientation
  dependence that the Euclidean 3D case lacked

### Step 4: The torus in 4D

A torus in 4D spacetime has a worldsheet — it extends
in both space and time.  The standing wave on the torus
oscillates in time (that's what "standing wave" means).
The torus surface sweeps through BOTH spatial AND
temporal orientations as you go around the tube and ring.

The coupling integral:

> α_torus = (1/A) ∮ C(orientation(s)) dA

now includes the timelike tilt.  If C depends on the
timelike component of the surface normal (which it should,
because the Lorentzian signature breaks the 2-design
symmetry), the torus integral gives a DIFFERENT result
from the purely spatial case.

### Step 5: Compare to α

At various torus geometries (ε, embedding orientation
in 4D), compute α_torus.  Look for α_torus = 1/137.

---

## Why the Lorentzian signature might break the deadlock

Tracks 4-5 showed that the Euclidean tetrahedron's
2-design symmetry makes all quadratic coupling measures
constant.  The coupling is the same at every orientation.

A Lorentzian simplex (4 spacelike + 1 timelike edges)
breaks this symmetry because:

1. **The inner product changes sign.**  The Minkowski
   inner product η(a,b) = −a₀b₀ + a₁b₁ + a₂b₂ + a₃b₃
   is different from the Euclidean a·b = a₀b₀ + ... The
   cos² projection of a 2D edge onto a timelike 4D edge
   has a MINUS sign contribution that doesn't cancel.

2. **The timelike edge is distinguishable.**  In the
   Euclidean 4-simplex, all 5 edges are equivalent
   (permutation symmetry).  In the Lorentzian case,
   the timelike edge is physically distinct from the 4
   spacelike edges (it has ds² < 0 instead of ds² > 0).
   This reduces the symmetry from S₅ (symmetric group
   on 5 elements) to S₄ × Z₂ (permutation of 4 spatial
   + flip of time).

3. **The 2-design property fails.**  A set of 5 vectors
   in 4D with Lorentzian inner product does NOT
   necessarily form a spherical 2-design on the
   Lorentzian "sphere" (the hyperboloid).  The identity
   Σ (ê·d_j)² = constant may not hold when one of the
   d_j has Minkowski norm −1 instead of +1.

If the 2-design property fails, the coupling between a
2D sheet and the 4D lattice DEPENDS on orientation — and
specifically on the timelike tilt of the sheet.  A sheet
purely in space (zero timelike tilt) would have one
coupling.  A sheet with a timelike component would have
a different coupling.  The torus, which oscillates in
time, samples both.

---

## Dimensional analysis: could 2D → 4D give 1/137?

Track 1 (2D → 2D, same lattice): coincidence rate ~1/20.

The number 20 comes from geometric probability at the
specific tolerance used.  But the underlying structure
is: 2D → 3D coincidence is reduced by one dimension of
"missing."  2D → 4D would be reduced by TWO dimensions.

Rough scaling:
- 2D → 3D: ~1/20 (one extra dimension to miss)
- 2D → 4D: ~1/20 × correction_factor

If the correction factor from the Lorentzian time
dimension is ~20/137 ≈ 1/7, the total is 1/137.

Whether the factor is 1/7 depends on the lattice
geometry — specifically on how the timelike periodicity
(one tick per Planck time) relates to the spatial
periodicity (one edge per Planck length).  In natural
units these are both 1, but the metric sign difference
could produce a non-unity ratio.

This is what the computation will determine.

---

## What would kill this hypothesis

- **The 4D Lorentzian lattice is still a 2-design** for
  the Minkowski inner product → coupling is constant →
  same deadlock as Tracks 4-5.  (This seems unlikely
  because the timelike direction breaks the symmetry,
  but it needs to be checked.)

- **The coincidence rate depends on orientation but is
  nowhere near 1/137** — it might be 1/10 or 1/10000.

- **The D4 diamond analog with Lorentzian signature
  doesn't exist** — the lattice might not be consistent
  with equal-length edges in Minkowski space.  (It
  should be — D4 is defined by integer conditions, not
  by a specific metric — but the edge lengths in the
  Lorentzian metric might not all be equal.)

---

## Connection to GRID

This track computes the coupling between GRID's two
structural levels:

- **Ma sheets (2D hexagonal):** the material surfaces
  where particles live as standing waves
- **The 4D spacetime lattice:** the GRID substrate on
  which Ma sheets are embedded

The coupling fraction is what we've been calling α —
the impedance mismatch between the 2D sheet and the
ambient lattice.  If Track 6 shows this is 1/137 for
the physical 4D Lorentzian lattice at the correct torus
geometry, α is derived from pure lattice geometry.

**This would close the one remaining free parameter of
the GRID + MaSt framework.**

---

**Script:** `scripts/track6_4d_lattice.py` (planned)
