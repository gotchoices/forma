# Track 3: Discrete edge alignment — 2D wye meets 3D jack

**Status:** Framing

---

## Premise

At the Planck scale, everything is discrete.  Every edge
is exactly L.  There is no tolerance — either two nodes
are one Planck length apart or they aren't connected.

The 2D GRID lattice is a hexagonal mesh.  Each node is a
**wye** (Y): three edges at 120° in a plane.

The 3D GRID lattice is a diamond-type structure.  Each
node is a **jack**: four edges at tetrahedral angles
(109.47° between any pair).

The question: when a 2D hexagonal lattice (all edges L)
is embedded as a plane in a 3D diamond lattice (all edges
L), at what orientations do edges from one lattice align
exactly with edges from the other?

"Align" means: the edge direction from one lattice is
exactly parallel to an edge direction in the other, AND
both endpoints land on lattice nodes at distance exactly L.
An aligned edge can transmit phase information between
the two lattices — it is a coupling channel.

---

## The two primitives

**The wye (2D node):**
- 3 edges in a plane
- 120° between any pair
- All edges length L

**The jack (3D node):**
- 4 edges in 3D
- 109.47° between any pair (tetrahedral)
- All edges length L

At "magic angle 0" — the plane coincides with a face of
the tetrahedron — three of the four jack edges project
into the plane at exactly 120° separation.  These three
projections match the three wye directions.  All three
edges can carry phase.  This is perfect coupling.

At a generic angle — zero wye edges match jack edges.
Zero coupling.

At specific intermediate angles — one or two edges may
align.  These are partial coupling orientations.

The set of allowed orientations is DISCRETE because both
lattices are discrete.  An edge either lands on a node or
it doesn't.  There is no "almost."

---

## Parameters

A plane in 3D is described by two angles:

- **θ (tilt):** angle between the plane normal and a
  reference axis (e.g., [001] of the diamond lattice)
- **φ (azimuth):** rotation of the normal around the
  reference axis

Once the plane is oriented, the hexagonal lattice on it
has one additional degree of freedom:

- **ψ (twist):** rotation of the hexagonal lattice within
  its own plane

On a torus, ψ is not free — it varies continuously as
you go around the torus (determined by the geodesic
direction).  For the flat-plane analysis, ψ is a third
parameter.

The full search space is (θ, φ, ψ).  But the discrete
constraint (edges must land on lattice nodes) means only
specific (θ, φ, ψ) triples produce any alignment at all.
The goal is to enumerate these triples and count the
coupling level at each.

---

## The coupling staircase

At each valid orientation, some number of edges align
(from 0 to the maximum for the patch size).  The levels:

| Level | Shared edges | What it means |
|-------|-------------|---------------|
| 0 | None | Decoupled — no phase can transfer |
| 1 | 1 edge (2 nodes) | Minimal coupling — one phase channel |
| 2 | 2 edges | Two channels |
| 3 | 3 edges (one complete wye) | One full node coupled |
| N | N edges | N phase channels |
| max | All edges in patch | Perfect coupling (magic angle) |

The number of orientations at each level, and the
distribution of levels, is the coupling spectrum.  If
low-coupling levels (1-2 edges) vastly outnumber high-
coupling levels, the average coupling fraction may be
small — possibly 1/137.

---

## Steps

### Step 1: Single-node analysis (analytical)

Place one diamond jack and one hexagonal wye at the same
origin.  The jack has 4 edge directions (the tetrahedral
vertices).  The wye has 3 edge directions in the (θ, φ, ψ)
plane.

For a wye edge to align with a jack edge, the unit vectors
must be parallel:

> ê_wye(θ, φ, ψ, k) = ê_jack(j)

where k ∈ {1,2,3} labels the wye edges and j ∈ {1,2,3,4}
labels the jack edges.

The four jack directions (tetrahedral vertices,
normalized):

```
d₁ = (+1, +1, +1) / √3
d₂ = (+1, −1, −1) / √3
d₃ = (−1, +1, −1) / √3
d₄ = (−1, −1, +1) / √3
```

The three wye directions in a plane with normal
n̂(θ, φ), rotated by twist ψ, are computed from the
120°-separated unit vectors in the plane.

**The computation:** for each pair (k, j), solve for
(θ, φ, ψ) where ê_wye = ê_jack.  This gives exact
equations (no numerical search needed for single-edge
alignment).

**Deliverables:**
- The complete set of (θ, φ, ψ) where at least one
  wye-jack edge alignment occurs
- How many edges align at each orientation (1, 2, or 3)
- The angular spacing between successive alignment
  orientations
- Whether the alignment set is finite, countably infinite,
  or dense

**This step is fast (analytical) and determines whether
Steps 2-3 are worth doing.**  If no alignments exist
except at the trivial magic angles (plane on a tetrahedral
face), the discrete coupling hypothesis fails at the most
basic level.

### Step 2: Extended lattice (computational)

Build a patch of diamond lattice (~10³ nodes, edge
length L = 1).  Build a hexagonal lattice on a plane at
each magic orientation from Step 1.  For each:

- Count how many hexagonal-lattice edges have BOTH
  endpoints coinciding with diamond-lattice nodes
  (exact match — integer coordinates or equivalent)
- Record the spatial pattern of shared edges: are they
  periodic?  Random?  Clustered?
- Determine the repeat distance (if periodic): how far
  apart are successive shared edges?  This is the
  "superlattice" of coupling points.

**What this reveals:** Step 1 tells you that a single
edge CAN align.  Step 2 tells you how MANY edges align
in an extended patch — whether the single-node alignment
extends to a repeating pattern across the lattice.

If the shared edges form a periodic superlattice, the
coupling density (shared edges per unit area) is a
well-defined geometric constant.

### Step 3: Coupling ratio and α

Count:
- **N_coupled:** total number of (θ, φ, ψ) orientations
  (from Steps 1-2) where at least 1 edge aligns
- **N_total:** total number of discrete orientations
  sampled (the full discrete orientation space)
- **Coupling fraction:** N_coupled / N_total

Also compute the WEIGHTED coupling: instead of counting
orientations (binary: coupled or not), weight each
orientation by the number of shared edges per unit area.
The weighted coupling fraction accounts for partial
coupling at intermediate angles.

**Compare to 1/137.**

If the coupling fraction (or its weighted version) equals
1/137 at the diamond lattice's natural parameters (no
adjustable inputs), α has a discrete geometric origin.

---

## Connection to the torus

The flat-plane analysis gives C(θ, φ, ψ) — the coupling
at each orientation.  A torus traces a specific closed
path through (θ, φ, ψ) space as you go around it.  The
path is determined by the torus geometry (aspect ratio ε
and embedding orientation).

The torus coupling is:

> α_torus = (1/circumference) ∮ C(θ(s), φ(s), ψ(s)) ds

where s is the arc length parameter along the torus.

If C is discrete (zero-or-nonzero at specific angles),
then α_torus counts how many times the torus path passes
through a coupling orientation, weighted by dwell time.

This connects Track 3 (discrete) to Track 2 (continuum):
Track 3 provides the exact C(θ, φ, ψ).  Track 2's torus
integral evaluates it along a specific path.

---

## What would kill this hypothesis

- **Step 1 finds no alignments** except the trivial magic
  angles (plane on tetrahedral face).  This means the
  angular mismatch (120° vs 109.47°) prevents ANY
  partial coupling.  The only coupling is perfect or
  nothing.  Track 3 reduces to Track 2 with just 4 magic
  directions.

- **Step 2 shows aligned edges don't extend** beyond the
  origin.  A single-node alignment that doesn't repeat
  in the extended lattice means the coupling is
  infinitesimal (one edge out of infinitely many).

- **Step 3 gives a ratio far from 1/137.**  The ratio
  might be 1/10 or 1/10000 — either way, it's not α.

Any of these would close Track 3.  But each failure is
informative: it narrows the space of possible geometric
origins for α.

---

## Notes

- We deliberately ignore the truncated octahedron as a
  cell shape.  The 3D lattice is defined by its EDGES
  (the diamond graph), not by an enclosing polyhedron.
  GRID lives on edges and nodes, not on cells.

- The diamond lattice has "chair" hexagons (6-cycles
  with 3 vertices lifted out of plane, angles warped
  from 120° to 109.47°).  These are NOT regular hexagons.
  We do NOT search for regular hexagons in the diamond
  lattice — we search for individual EDGE alignments
  between the flat 2D wye and the 3D jack.

- The 120° vs 109.47° angular mismatch (~10.5°) is the
  fundamental tension.  Every coupling event requires
  this mismatch to be accommodated at the shared node.
  How the lattice accommodates it (which edges bend,
  which break, which find alternative paths) determines
  the coupling strength.

**Script:** `scripts/track3_discrete_embedding.py` (planned)
