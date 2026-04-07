# Track 5 Findings: Wavefront transfer efficiency

Script: `scripts/track5_wavefront_transfer.py`

---

## F1. ALL quantities are constant — no orientation dependence

The transfer efficiency T, the pattern match η, and the
energy fraction are ALL exactly constant at every
orientation tested (121,500 orientations in the full sweep,
plus magic angles, random angles, and torus integrals at
9 different ε values and 2 torus axes):

| Quantity | Value | Varies? |
|----------|-------|---------|
| T (transfer efficiency) | 2.000000 | No — CV = 0.0000 |
| η (pattern match) | 1.000000 | No — exactly 1 everywhere |
| Energy fraction | 2.000000 | No — constant |
| Tr(MᵀM) | 4.000000 | No — as expected from T4 |

**η = 1 everywhere** means: the projected wye amplitudes
ALWAYS perfectly match the desired jack amplitudes for
forward propagation.  There is no directional mismatch.
The pattern match is perfect at every orientation.

**T = 2 everywhere** means: the energy that exits the
shared node on jack edges in the forward direction is
TWICE the incoming wye energy.  This seems unphysical
(energy gain?) but reflects the normalization: the
projection M × a distributes the wye energy across 4
jack edges, and the forward-propagating component
captures more than the original because the jack has
4 edges collecting from 3 wye edges.

The bottom line: **the tetrahedral symmetry is even
stronger than Track 4 suggested.**  Not only is the
total cos² projection constant (T4's identity), but
the COHERENT wavefront transfer — the product of energy
fraction and pattern match — is also constant.  There
is zero orientation dependence.  The torus integral is
trivially the same constant at all ε.


## F2. The singular values are constant: σ = (√2, √2, 0)

The SVD of the 4×3 projection matrix M gives exactly:

> σ₁ = √2, σ₂ = √2, σ₃ = 0

at ALL orientations (verified across 16,200 orientations
optimized over ψ).

This means M always has **rank 2** — the 3D projection
of the 2D wave lives in a 2D subspace of the 4D jack
space.  One dimension is always lost (σ₃ = 0).  The two
surviving dimensions each couple with strength √2.

**Why σ₃ = 0:** the three wye edges lie in a plane.
Their projections onto 4 jack edges span at most a 2D
subspace (because the wye vectors span a 2D plane).  The
jack has 4 edges but the wye can only excite 2 independent
directions in jack-space.

**Why σ₁ = σ₂ = √2:** the two surviving coupling
directions have EQUAL strength.  This is because the wye
has 3-fold rotational symmetry in its plane, and the
projection of a 3-fold symmetric pattern onto a tetrahedron
always produces two equal singular values (the symmetry
prevents one direction from being preferred over the other
within the surviving 2D subspace).


## F3. Why the symmetry kills everything

The tetrahedron has a deep mathematical property: it is a
**spherical 2-design** (and 3-design).  This means that
for ANY polynomial of degree ≤ 2 (including cos² and
dot products), the average over the 4 tetrahedral
directions equals the average over the full sphere.

The wye has 3-fold symmetry.  Combined with the
tetrahedron's 2-design property, every quadratic quantity
(energy, projection, transfer efficiency) averages to the
same value regardless of the relative orientation of the
two structures.

**This is not a coincidence or a bug in the computation —
it is a theorem.**  No quadratic coupling measure between
a 3-fold symmetric planar structure and a tetrahedral
structure can depend on their relative orientation.

To get orientation-dependent coupling, you would need:
- A coupling that goes as a HIGHER power than cos²
  (cubic or quartic dependence on angle)
- OR: a lattice structure that is NOT a spherical 2-design
  (the tetrahedron is special in this regard)
- OR: a computation that involves the LATTICE (many nodes,
  periodic structure) rather than a SINGLE junction (one
  wye meeting one jack)


## F4. What this means for deriving α

**The single-junction approach is dead.** The coupling
between one wye node and one jack node is a constant
(T = 2, η = 1) that does not depend on orientation,
does not depend on ε, and does not equal 1/137.

**What might still work:**

1. **Extended lattice effects.**  A single junction has
   perfect symmetry.  But a LATTICE of junctions — where
   the 2D hexagonal lattice meets the 3D diamond lattice
   across many nodes simultaneously — may break this
   symmetry.  Constructive/destructive interference between
   many junctions could produce an orientation-dependent
   net coupling.  This requires Step 2 of Track 3 (extended
   lattice), which has not been done.

2. **Higher-order coupling.**  The cos² (quadratic)
   coupling is killed by the 2-design symmetry.  But the
   LATTICE has higher-order structure — cubic, quartic
   terms from multi-node paths.  A wave that travels from
   the 2D lattice through one junction, propagates on the
   3D lattice, and then returns through another junction
   picks up phase information from the LATTICE GEOMETRY
   (not just the single junction).  This round-trip
   coupling is inherently higher than quadratic and might
   break the symmetry.

3. **The 19.47° gap.**  Track 3 F4 showed that the
   fundamental angular mismatch between 120° and 109.47°
   is 19.47°.  This angle appears in the geometry but not
   in the quadratic coupling (which is constant).  It might
   appear in a PHASE coupling — where the mismatch between
   the wye direction and the jack direction produces a
   phase shift (not an amplitude reduction) at each
   junction.  The accumulated phase shift across many
   junctions could produce interference effects that
   depend on the lattice geometry and the propagation
   direction.


## F5. Summary

| Track | Question | Result |
|-------|---------|--------|
| 3 | Do edges align? (binary) | Yes, at discrete angles; fraction = 1/137 at ~2.2° tolerance |
| 4 | Does cos² projection vary? | No — Σ cos² = 4/3 constant (tetrahedral identity) |
| 5 | Does coherent transfer vary? | No — T = 2, η = 1 constant (spherical 2-design symmetry) |

All single-junction approaches give orientation-
independent coupling.  The tetrahedral symmetry is too
perfect.  To break it, you need either multi-junction
(lattice) effects or higher-order (non-quadratic) coupling.

The fact that the tetrahedron is a 2-design is the
fundamental reason.  A different 3D lattice node (not
tetrahedral) would not have this property — but the
diamond/tetrahedral lattice is the natural candidate for
GRID's 3D structure because it has equal edge lengths and
4-connectivity.
