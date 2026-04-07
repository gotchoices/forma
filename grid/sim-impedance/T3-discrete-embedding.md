# Track 3: Discrete embedding — hexagonal rings on a 3D lattice

**Status:** Framing

---

## Premise

Track 2 treats the lattice as a continuum with smooth
angular dependence.  Track 3 goes to the foundation:
everything is discrete at the Planck scale.  Every edge
is exactly L.  There is no tolerance δ — either two nodes
are one Planck length apart or they aren't connected.

The question: at what DISCRETE angles can a 2D hexagonal
structure share nodes with a 3D lattice, when all edges
are constrained to length exactly L?

---

## The angle mismatch

In the 3D lattice (diamond cubic or truncated octahedral
vertex graph), each node has 4 edges at tetrahedral angles
(109.47° between any pair).  In the 2D hexagonal lattice,
each node has 3 edges at 120°.

These angles are DIFFERENT (109.47° vs 120°).  At "magic
angle 0" (a hexagonal face of the truncated octahedron),
the 2D and 3D hexagons align perfectly — all 6 nodes
coincide, all edges match.  An arbitrarily small rotation
away from this angle gives ZERO coupling — not "weak"
coupling, but exactly zero, because at the Planck scale
there is no "almost aligned."

But at some specific FINITE rotation, a new alignment
occurs: at least one edge in lattice A lies exactly on top
of an edge in lattice B.  This is the "first angle" —
the smallest rotation from magic angle 0 where any
coupling occurs.  It won't be a full 6-edge hexagonal
match — it might be just 1 or 2 shared nodes.  But it's
nonzero.

---

## The coupling staircase

A discrete staircase of coupling levels:

| Coupling level | Shared nodes | Description |
|---------------|-------------|-------------|
| 0 | 0 | Generic angle — zero coupling, the sheets are decoupled |
| 1 | 1 edge (2 nodes) | First angle — minimal partial coupling |
| 2 | 2 edges (3 nodes) | Second angle — partial coupling |
| 3 | 3 edges (forming a triangle) | Half-hexagon coupling |
| ... | ... | ... |
| 6 | Full hexagon (6 edges, 6 nodes) | Magic angle — perfect coupling |

The angles at which each level occurs are FIXED by the
lattice geometry.  They are not tunable.  And crucially:
the number of angles at each level and the energy cost
per level may determine α.

**The hypothesis:** α is the ratio of "partially coupled
angles" to "total possible angles" on the discrete lattice.
Or equivalently: α is the probability that a random
discrete orientation has at least one shared edge between
the 2D and 3D lattices.

---

## Sub-tracks

### Track 3a: Single hexagonal ring

Can a hexagonal ring of 6 edges (length L each) embed in
the 3D lattice?  At how many orientations?

**Method:** enumerate all sets of 6 lattice nodes in the 3D
lattice that form a regular hexagon of edge length L.
Count the distinct orientations.  These are the magic
angles.

This is a pure combinatorial search on a small region of
the 3D lattice (~10³ nodes).  Hours of computation at most.

**Deliverables:**
- Number of distinct hexagonal ring orientations in each
  3D lattice type (diamond cubic, truncated-octahedral
  vertex graph)
- The actual angles (in spherical coordinates)
- Whether the two lattice types give the same or different
  results

### Track 3b: Partial matches — the coupling staircase

For each possible relative orientation of the two lattices
(discretized by the 3D lattice geometry), count how many
node-node coincidences exist within a patch of ~100 cells.

**Record at each discrete angle:**
- How many nodes from the 2D hexagonal lattice coincide
  with 3D lattice nodes?
- How many shared edges (pairs of coincident nodes that
  are also L apart)?
- How many complete hexagons (all 6 nodes shared)?

**Map the coupling staircase.  Identify:**
- The first angle (minimum nonzero coupling — 1 shared edge)
- The spacing between successive coupling levels
- How many angles produce 1, 2, 3, 4, 5, 6 shared edges
- Whether the low-coupling angles (1-2 shared edges)
  outnumber the high-coupling angles (5-6 shared edges)
  by a factor related to α
- Whether there is a periodic or quasi-periodic pattern
  in the staircase (repeating at some characteristic
  angular interval)

### Track 3c: Small tori — convergence to α

Build the smallest possible torus from discrete edges
(a hexagonal tube ring + connecting edges) and attempt to
embed it in the 3D lattice at each valid orientation from
Track 3b.

At each torus size (measured in Planck edges), count:
- M(N) = number of valid embedding orientations
- T(N) = total number of discrete orientations attempted

The ratio M(N)/T(N) is a discrete approximation to the
coupling fraction.  As N grows (larger torus, more
possible angles), the discrete set grows denser and
M/T should converge to a limit.

**The prediction:** M(N)/T(N) → α = 1/137 as N → ∞.

If this converges, α is derived from the discrete
geometry of hexagonal structures embedded in the
3D truncated-octahedral (or diamond cubic) lattice.
No free parameters.  No measured inputs.  Pure
combinatorial geometry.

---

## Why this might be the most fundamental computation

Track 1 failed because 2D-in-2D has no preferred angles.
Track 2 (continuum) introduces preferred angles from the
3D lattice but works in the smooth approximation.  Track 3
works at the actual Planck-discrete level where the lattice
lives.

If α emerges from Track 3, it is the MOST fundamental
derivation possible: a pure integer-geometry ratio from
the way hexagons fit into the 3D lattice.  No physics,
no dynamics, no fields — just counting.

---

## The diamond lattice alternative

The truncated octahedron describes the CELLS.  But GRID
is defined by EDGES (links carrying the gauge connection).
The relevant structure may be the edge graph — the diamond
cubic lattice, where each node has 4 edges at tetrahedral
angles (109.47°) with all edges equal length.

The diamond lattice and the truncated-octahedral vertex
graph are closely related (both are 4-connected with all
edges equal).  Track 3a should test BOTH: embed hexagonal
rings in the diamond lattice and in the truncated-
octahedral vertex graph.  If they give different results,
the choice of 3D lattice matters.  If they agree, the
specific cell shape is irrelevant — only the vertex
connectivity counts.

---

**Script:** `track3_discrete_embedding.py` (planned)
