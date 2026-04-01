# Lattice Geometry — Open Investigation

**Status:** Exploratory — not yet part of the axiomatic chain.
Captured here so it doesn't block the Maxwell and G derivations.

---

## The core idea

The lattice resolution ζ (bits per cell) may not be a free
parameter.  If the cell geometry determines how many neighbors
each cell has, and one bit requires the full local neighborhood
to compute, then ζ follows from the packing.

---

## The cell as a computer

Each cell is a tiny processor that runs one computation per
**Planck time** (one tick).  This is already implicit in axiom
A1: disturbances propagate at one cell per tick (c = 1).  The
Planck time is the clock cycle of the lattice.

### Model A (original): node + edges

In the original picture, each cell has its own phase register
(site variable θ) plus link variables on its edges.  Every
tick, the cell reads its phase and edge states, computes new
values, and propagates.

### Model B (current): cell = its edges

In Model B, the cell has **no separate state register**.  The
cell IS its boundary — D + 1 edges (for a D-simplex), each a
vibrating string carrying standing-wave modes:

- **Lowest mode** on each edge: the gauge connection A_μ
  (the link variable from lattice gauge theory)
- **Higher modes:** sub-state structure contributing to
  entropy but not directly visible at the lattice scale
- **Phase θ:** a collective property of the cell's edge
  modes, not a separate variable

The **vertices** where edges meet are coupling junctions —
they apply the update rule (covariant derivative), but store
no state.

Every tick, each edge:

1. **Vibrates** — its standing-wave modes advance
2. **Exchanges energy** with connected edges at vertex
   junctions
3. The junction applies the coupling rule: superposition of
   incoming modes determines outgoing modes

The result becomes visible to neighbors on the **next** tick.
The speed of light is the maximum propagation speed because a
cell can only reach its face-sharing neighbors in one cycle.

### What a cell knows

All state lives on edges.  In a 3D tetrahedral cell:

| Element | Count | What it stores |
|---------|-------|---------------|
| Edges (strings) | 6 | Standing-wave modes; lowest = A_μ |
| Faces (shared with neighbors) | 4 | Each face's edges define the coupling |
| Vertices (junctions) | 4 | Coupling rule only — no state |

The edge variables are the fundamental degrees of freedom.
Products of edge modes around closed loops (plaquettes) give
the field tensor F_μν.  A propagating disturbance in the
edge modes is a **photon**.

---

## Two counting models

The value of ζ depends on whether the cell has internal
state beyond its edges.

### Model A: self + neighbors (original)

The cell has its own state register (phase θ) separate from
the link variables on its edges.  One bit of information is
a collective property of the cell and its face-sharing
neighbors:

- D-simplex has D + 1 faces → D + 1 neighbors
- Self + (D + 1) neighbors = D + 2 contributors per bit
- **ζ = 1/(D + 2)**

### Model B: cell = its edges (current leading model)

The cell has **no separate internal state**.  It IS its
boundary — a collection of strings (edges) that carry all
the state.  The "node" at each vertex is just a coupling
junction where strings meet and exchange energy, not a
state holder.

In this picture, each edge of the simplex is a vibrating
string that stores standing-wave modes.  The lowest mode
carries the gauge connection A_μ; higher modes are sub-state
(internal degrees of freedom contributing to entropy).  The
phase θ is a collective property of the cell's edge modes,
not a separate variable.

The bit is computed from the cell's edges alone — no
additional "self" contribution:

- D-simplex has D + 1 faces → D + 1 neighbors
- No separate self → D + 1 contributors per bit
- **ζ = 1/(D + 1)**

### Comparison

| Dim | Simplex | Faces | Model A: 1/(D+2) | Model B: 1/(D+1) |
|-----|---------|-------|-------------------|-------------------|
| 2D | Triangle | 3 | 1/4 | **1/3** |
| 3D | Tetrahedron | 4 | 1/5 | **1/4** |
| 4D | Pentachoron | 5 | 1/6 | **1/5** |

### Bekenstein-Hawking and Model B

The BH entropy formula is S = A/4 → ζ = 1/4.  Under
Model B, this value comes from the **3D tetrahedron**, not
the 2D triangle.

This is physically appropriate: a black hole horizon is a 2D
surface embedded in **3D space**.  The cells that "vote" on
the entropy of the horizon are the 3D tetrahedral cells
adjacent to it.  Each tetrahedron has 4 face-sharing
neighbors → ζ = 1/4.

Under Model A, ζ = 1/4 required either the 2D triangle
(which felt like choosing the answer) or a different counting
convention.  Under Model B, ζ = 1/4 falls out naturally
from the 3D simplex — the right dimensionality for the
cells surrounding a horizon.

### Why Model B is preferred

1. **No extra objects.**  Model A requires a separate phase
   register at each cell centre.  Model B uses only the
   lattice edges — the cell is its geometry, not a point
   with attachments.

2. **Entropy from strings.**  Model B's edges carry
   standing-wave modes, giving each cell a rich state space
   and therefore entropy.  This is essential for the
   thermodynamic (Jacobson) route to gravity.  Model A's
   single phase variable has no internal microstates.
   (See [sim-gravity-2/](sim-gravity-2/).)

3. **Vertices are junctions, not state holders.**  The vertex
   where edges meet applies the coupling rule (the covariant
   derivative D_μθ = ∂_μθ − eA_μ) but does not store state.
   This is simpler and avoids double-counting.

4. **BH from the right dimension.**  ζ = 1/4 from the 3D
   tetrahedron (the cell type adjacent to horizons) rather
   than an ad hoc 2D argument.

---

## Leading candidate: 3D simplicial, Model B (ζ = 1/4)

The spatial lattice is tiled by tetrahedra.  Each tetrahedron
has 4 triangular faces, each shared with one neighbor.  Under
Model B counting (no self), ζ = 1/4.

This matches the Bekenstein-Hawking factor and gives:
- G = 1/(4ζ) = 1 in natural units
- Spacetime stiffness c⁴/(8πG) = 1/(8π)

The full 4D lattice uses a (1,3) split: tetrahedra tile 3D
space, and time advances as a causal step (one tick = one
Planck time).  This is consistent with axiom A2's (1,3)
signature and with causal dynamical triangulations.

### 4D simplicial alternative

If the lattice is fully 4D simplicial (pentachorons), Model B
gives ζ = 1/5.  This doesn't match BH but could be relevant
for bulk entropy (as opposed to horizon entropy).

| Geometry | Model B: ζ = 1/(D+1) | G = 1/(4ζ) | BH match? |
|----------|---------------------|-----------|-----------|
| **3D tetrahedron** | **1/4** | **1** | **Yes** |
| 4D pentachoron | 1/5 | 5/4 | No |

### Tiling

Regular tetrahedra do not tile flat 3D space, but irregular
simplicial complexes do (any 3-manifold can be triangulated).
The continuum limit smooths out irregularity.  This is the
basis of Regge calculus, causal dynamical triangulations,
and finite element methods.

---

## How ζ enters the derivations

| Derivation | Uses ζ? | Affected by packing choice? |
|------------|---------|----------------------------|
| Maxwell ([maxwell.md](maxwell.md)) | No | No — works on any lattice |
| G ([gravity.md](gravity.md)) | Yes: G = 1/(4ζ) | Mechanism is universal; value of G depends on ζ |
| Stiffness c⁴/(8πG) | Yes: = ζ/(2π) | Same — mechanism universal, value depends on ζ |

Both proofs are geometry-independent.  The packing determines ζ,
which determines G.  If nature picks a specific packing, that's
why G has the value it does.

---

## Why Model B (neighbors only, no self)

In Model B, the cell IS its edges.  There is no separate
"self" state to count.  The bit of physical information at
a cell is the collective state of its boundary strings —
the edges shared with neighbors.

**The string argument:** a triangular cell (2D) is three
vibrating strings forming its boundary.  Each string is
shared with one neighbor.  The cell's information content
is fully determined by its 3 edges.  There is no additional
internal register; the vertex junctions store no state.

**The computational argument:** each tick, the cell's edges
vibrate, exchange energy at vertices, and advance their
modes.  The vertex applies the coupling rule (covariant
derivative), but the state lives on the edges.  In a 3D
tetrahedron: 4 face-sharing edges, no separate self → 4
contributors per bit → ζ = 1/4.

**The gauge theory argument:** in lattice gauge theory, the
physically relevant variables are the **link variables**
(gauge connections on edges), not site variables.  The
gauge-invariant content (F_μν) is built from products of
link variables around plaquettes.  The site variable (phase)
is gauge-dependent and can be gauged away at any single site.
The physical information IS on the links — consistent with
Model B.

**Historical note:** Model A ("self + neighbors") was the
original counting scheme.  Model B is preferred because it
eliminates the ad hoc "self" contribution, produces ζ = 1/4
from the 3D tetrahedron (the right dimension for horizons),
and is compatible with the string-register picture needed
for entropic gravity.

---

## What needs to be shown

1. **Does the face count determine ζ?**
   The argument "D + 1 faces → ζ = 1/(D + 1)" under Model B
   is physically motivated but unproven.  A rigorous
   information-theoretic derivation (Shannon entropy on a
   simplicial complex, gauge-invariant degree-of-freedom
   count) would promote this from conjecture to theorem.

2. **Why simplicial (if simplicial)?**  The simplex is the
   minimal polytope.  Is there a uniqueness or optimality
   argument beyond minimality?  Could a consistency condition
   (e.g. requiring the lattice to support causal dynamics)
   single out the simplex?

3. **Is ζ dimension-dependent?**  Under Model B, ζ depends
   on the dimensionality of the relevant cells.  For
   horizons (2D surfaces in 3D space), the adjacent cells
   are 3D → ζ = 1/4.  For bulk 4D cells, ζ = 1/5.  Can
   different ζ values coexist in the same lattice?  Or is
   only the horizon value physically relevant (via A5)?

4. **String-register validation.**  Model B requires edges
   to carry multi-mode state (standing waves).  The
   sim-gravity-2 simulation will test whether this produces
   the correct entropic force (1/r in 2D).  A positive
   result would strongly support Model B over Model A.

---

## Precedent

- **Regge calculus** (1961): discretizes GR on simplicial
  lattices.  Well-established.
- **Causal dynamical triangulations** (CDT, Ambjørn-Loll):
  sum over simplicial spacetimes with causal structure.
  CDT treats time differently from space (the "causal"
  part), favoring the (1,3)-split approach.
- **Spin foam models** (Ponzano-Regge, Barrett-Crane, EPRL):
  quantum gravity on simplicial complexes.
- **Lattice gauge theory on simplicial complexes**: the
  continuum limit of U(1) gauge theory gives Maxwell,
  regardless of whether the lattice is simplicial or
  hypercubic.
- **Cellular automaton interpretations** ('t Hooft 2014,
  Wolfram 2002): physics as computation on a discrete
  lattice with a fixed clock cycle.  The GRID picture —
  cells computing new states from local inputs each Planck
  tick — is in this tradition.

---

## Relation to the derivations

Both derivations work for **any** packing and **any** ζ.
This investigation runs in parallel, not in series.  It asks:
can A5 be promoted from free parameter to geometric
consequence?
