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

Every tick, each cell:

1. **Reads** its own phase θ and the link states on all its
   edges (the gauge connections U_j shared with neighbors)
2. **Computes** its new phase θ_new
3. **Contributes** to updating the link variable on each of its
   edges (collaboratively with the neighbor on the other end)

The result becomes visible to neighbors on the **next** tick.
The speed of light is the maximum propagation speed because a
cell can only reach its immediate neighbors in one cycle.

### What a cell knows and what it computes

In lattice gauge theory, two kinds of state live on the lattice:

- **Cell state (site variable):** the phase θ ∈ [0, 2π) — this
  is the matter field.
- **Link state (edge variable):** the gauge connection
  U_j ∈ U(1) — one per edge, shared between the two endpoint
  cells.  This is the electromagnetic field (the lattice version
  of A_μ from [maxwell.md](maxwell.md)).

The link variables are **independent degrees of freedom**, not
determined by the endpoint phases.  They have their own dynamics
(the Wilson plaquette action).  The electric and magnetic fields
(E and B) are encoded in products of link variables around
closed loops (plaquettes), not in the cell phases.

So each tick, a cell in a pentachoron lattice computes:

| Output | Count | What it represents |
|--------|-------|--------------------|
| New phase θ_new | 1 | Matter field update |
| Contributions to link updates | 5 | Electromagnetic field update (one per neighbor) |
| **Total** | **6** | **Degrees of freedom processed per cell per tick** |

A propagating disturbance in the cell phases is **charged
matter**.  A propagating disturbance in the link states is a
**photon**.

### What a cell communicates

A cell does not "send messages."  Its state (phase + link
contributions) is simply **visible** to its neighbors through
the shared links.  The link IS the communication channel:

- The neighbor reads the link variable to learn about the
  coupling
- The neighbor reads (indirectly, via the link update rule) the
  effect of this cell's phase

So each cell communicates **more than its phase**.  It
communicates its phase AND its half of 5 link updates — totaling
6 pieces of information per tick.

---

## Leading candidate: 4D simplicial lattice (ζ = 1/6)

The simplex is the minimal polytope in any dimension — the cell
with the fewest faces.  In 4D, it is the **pentachoron**
(5-cell): a "4D pyramid."

Properties of the pentachoron:

- 5 vertices, 10 edges, 10 triangular faces, 5 tetrahedral facets
- Each cell shares a tetrahedral facet with **5 neighbors**
- It is the simplest possible 4D cell (fewest facets)

### The resolution argument

Each tick, the cell processes 6 degrees of freedom: its own
phase plus 5 link contributions.  The bit of physical
information at that cell is a collective property of the full
local patch — **self + neighbors**:

- 1 cell + 5 neighbors = **6 contributors per bit**
- Each cell contributes 1/6 of a bit → **ζ = 1/6**
- G = 1/(4ζ) = 3/2 in natural units

This counting is reinforced by the computational picture: 6
outputs per cell per tick maps naturally to 1/6 bit per cell.

### Why 4D simplicial?

The simplex is the "simplest possible" cell in D dimensions,
paralleling A3's choice of the "simplest possible" internal
variable (the phase circle).  This minimality principle — always
choose the simplest structure — runs through the GRID axioms.

### Tiling

Regular pentachorons do not tile flat 4D space.
Irregular simplicial complexes do (any manifold can be
triangulated — this is the basis of finite element methods,
Regge calculus, and causal dynamical triangulations).  The
continuum limit smooths out irregularity.

---

## Alternative: (1,3)-split simplicial

Instead of a full 4D simplicial lattice, tile the 3D spatial
dimensions with tetrahedra and handle time separately as a
causal step.

The tetrahedron (3D simplex) has **4 faces → 4 spatial
neighbors**.  With the self + neighbors count: ζ = 1/5.

| Geometry | Neighbors (z) | ζ = 1/(z+1) | G = 1/(4ζ) |
|----------|--------------|-------------|-----------|
| 4D simplicial (leading) | 5 | **1/6** | 3/2 |
| 3D simplicial (spatial) | 4 | 1/5 | 5/4 |

**Note on Bekenstein-Hawking:** the traditional BH entropy
formula S = A/(4G) uses ζ = 1/4.  The (1,3)-split simplicial
lattice with "neighbors only" counting (ζ = 1/z = 1/4)
reproduces this.  Under the self + neighbors scheme, no simple
geometry gives exactly 1/4.  This is a tension worth noting —
but not necessarily fatal, since BH entropy has never been
experimentally measured and the "1/4" could reflect a different
counting convention.

---

## Comparison of candidate geometries

All using the self + neighbors counting: ζ = 1/(z+1).

| Lattice type | Dimension | Neighbors (z) | ζ | G = 1/(4ζ) |
|-------------|-----------|--------------|---|-----------|
| **4D simplicial** | **4** | **5** | **1/6** | **3/2** |
| 3D simplicial (spatial) | 3 | 4 | 1/5 | 5/4 |
| 4D hypercubic | 4 | 8 | 1/9 | 9/4 |
| 3D cubic (spatial) | 3 | 6 | 1/7 | 7/4 |

The simplicial lattice gives the smallest coordination numbers,
consistent with the minimality principle.

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

## Why self + neighbors

The cell itself must be included in the tally.  The bit of
physical information at a cell is not just what the neighbors
dictate — it is the collective state of the whole local patch:
the cell's own phase, plus the link states connecting it to
all neighbors.

**The computational argument:** each tick, the cell processes
6 degrees of freedom (1 phase + 5 link contributions).  These
6 pieces of information define one bit.  The cell is both a
participant and a contributor — not a passive recipient.

**The gauge theory argument:** in lattice gauge theory, the
physical (gauge-invariant) state at a point depends on both
the site variable (phase) and the link variables (connections)
around it.  You cannot define F_μν at a cell without knowing
the cell's links, and you cannot define the links without
knowing both endpoints.  The full local patch is the minimal
gauge-invariant unit.

---

## What needs to be shown

1. **Does the coordination number determine ζ?**
   The argument "z+1 local degrees of freedom → ζ = 1/(z+1)"
   is physically motivated but unproven.  A rigorous
   information-theoretic derivation (Shannon entropy on a
   graph, gauge-invariant degree-of-freedom count) would
   promote this from conjecture to theorem.

2. **Why simplicial (if simplicial)?**  The simplex is the
   minimal polytope.  Is there a uniqueness or optimality
   argument beyond minimality?  Could a consistency condition
   (e.g. requiring the lattice to support causal dynamics)
   single out the simplex?

3. **Full 4D or (1,3)-split?**  Does time participate in the
   packing on equal footing with space, or is the causal
   dimension handled separately?  The (1,3) signature (A2)
   suggests time IS different, which favors the split
   approach — but this is not settled.

4. **Reconciliation with Bekenstein-Hawking.**  The standard
   BH factor is 1/4.  If the correct value is 1/6, this is
   a prediction that differs from the theoretical consensus.
   Either: (a) the counting convention differs, (b) the BH
   derivation has a convention-dependent factor, or (c) ζ = 1/6
   is wrong.  This needs investigation.

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
