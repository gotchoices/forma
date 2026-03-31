# Lattice Geometry — Open Investigation

**Status:** Exploratory — not yet part of the axiomatic chain.
Captured here so it doesn't block the Maxwell and G derivations.

---

## The question

Axiom A5 currently sets ζ (the resolution — bits per Planck cell)
as a free parameter with value 1/4.  Two open directions:

1. **Can ζ be derived from the packing geometry?**  If the cell
   shape determines the coordination number, and the coordination
   number determines ζ, then the resolution is not a free
   parameter — it's a geometric consequence.

2. **Does the choice of packing matter for the derivations?**
   Maxwell does not use ζ at all — it works on any lattice.
   The G derivation uses ζ but the *mechanism* (entropy →
   thermodynamics → Einstein equations) works for any value.
   The specific G you get depends on ζ, but the fact that
   gravity emerges does not.

This means GRID is open to multiple packing geometries.  The
packing determines ζ, which determines G.  If nature picks a
specific packing, that's why G has the value it does.  If
multiple packings are consistent, then the packing (or
equivalently ζ) is a design parameter — and we measure G to
determine which geometry nature chose.

## How ζ enters the derivations

| Derivation | Uses ζ? | Geometry-dependent? |
|------------|---------|---------------------|
| Maxwell (maxwell.md) | No | No — works on any lattice |
| G (gravity.md) | Yes: G = 1/(4ζ) | The mechanism is universal; the value of G depends on ζ |
| Stiffness c⁴/(8πG) | Yes: = 2ζ/π | Same — mechanism universal, value depends on ζ |

So the question "which packing?" is really the question "what
is ζ?", which is really the question "what is G?".

---

## Candidate geometries

### Hypercubic (the default assumption)

Cells are 4D hypercubes.  Each cell has 2D = 8 neighbors in
4D, or 2×3 = 6 spatial neighbors in the (1,3) split.

- Simple, regular, tiles flat space exactly
- Standard in lattice gauge theory
- Coordination number 6 (spatial) or 8 (full 4D)
- Would give ζ = 1/6 or 1/8 if the coordination argument holds

### Simplicial (tetrahedral spatial cells)

Cells are simplices — the minimal polytope in each dimension.
In 3D, the simplex is a tetrahedron (4 faces, 4 neighbors).

| D | Simplex | Neighbors per cell |
|---|---------|-------------------|
| 2 | Triangle | 3 |
| 3 | Tetrahedron | **4** |
| 4 | Pentachoron | 5 |

For (1,3) spacetime, if the spatial lattice is simplicial, each
cell has **4 spatial neighbors**.  If ζ = 1/(spatial coordination
number), this gives ζ = 1/4 — matching Bekenstein-Hawking.

- The simplex is the "simplest possible" cell (fewest faces),
  paralleling A3's choice of "simplest possible" internal
  variable (the phase circle)
- Used in Regge calculus, spin foams, causal dynamical
  triangulations
- Irregular tilings are standard (finite element methods)
- Does not tile flat space regularly, but the continuum limit
  smooths out irregularity

### Other packings

Not explored yet.  Any packing that gives a well-defined
coordination number z produces a candidate ζ = 1/z.

---

## The coordination number argument (sketch)

Each cell holds a phase θ.  The physical information is in the
phase differences with neighbors (A3, A4).  A cell with z
neighbors contributes its one phase value to z relationships.
To extract one independent bit requires the full neighborhood —
all z links must be consulted.

Therefore: each cell contributes 1/z of a bit, giving ζ = 1/z.

**This is a hand-wave.**  A rigorous version needs one of:

- Shannon entropy of phase differences on a graph with
  coordination z
- Holographic entropy counting on simplicial vs hypercubic
  boundaries
- The number of independent gauge-invariant degrees of freedom
  per cell as a function of lattice topology

If the argument holds, then the packing **determines** ζ, and
the problem reduces to: what packing does nature use?

If it fails (ζ is independent of the coordination number), then
ζ remains a free parameter regardless of the packing.

---

## The A_μ connection protocol

On any lattice, each cell interacts with its neighbors through
shared faces (or links, depending on the lattice).  The
connection A_μ (the link phase) lives on each face — it encodes
how two cells sharing that face compare their phases.

- The **cell** stores a phase θ
- Each **face** stores a link phase φ = eA_μ (the dynamic
  interaction state)
- A_μ is the protocol by which neighboring cells interact — it
  is dynamic (oscillates, carries energy as photons) but lives
  on the lattice's connections, not above it

The number of faces per cell depends on the packing.  This may
or may not affect the physics in the continuum limit (where the
cell shape is washed out).

---

## What needs to be shown

1. **Does the coordination number rigorously determine ζ?**
   The hand-wave needs a precise information-theoretic proof.

2. **Does the packing affect the continuum limit?**  Lattice
   gauge theory and Regge calculus both claim the continuum
   limit is universal (independent of cell shape).  If so, the
   packing determines ζ but nothing else — all other physics
   is the same.

3. **If the continuum limit is universal, why does ζ depend on
   the packing?**  This is the sharpest version of the question.
   If ζ = 1/z and z depends on the packing, but everything else
   is packing-independent, then G is the one observable that
   remembers the discrete structure.  That would be a strong
   statement: G is the fingerprint of the lattice geometry.

4. **Why simplicial (if simplicial)?**  The simplex is the
   minimal polytope — fewest faces, most economical.  Is there
   an optimality or uniqueness argument?

---

## Precedent

- **Regge calculus** (1961): discretizes GR on simplicial
  lattices.  Curvature lives on (D−2)-dimensional hinges.
- **Spin foam models** (Ponzano-Regge, Barrett-Crane, EPRL):
  quantum gravity on simplicial complexes.  Active research.
- **Causal dynamical triangulations** (CDT, Ambjørn-Loll):
  sum over simplicial spacetimes with causal structure.
  Recovers 4D semiclassical geometry in the continuum limit.
- **Lattice gauge theory on simplicial complexes**: less common
  than hypercubic but studied.  The continuum limit of U(1)
  gauge theory on simplicial lattices gives Maxwell.

## Relation to the derivations

The Maxwell derivation ([maxwell.md](maxwell.md)) and the G
derivation ([gravity.md](gravity.md)) do **not** depend on the
lattice being simplicial or any particular packing.  Maxwell
works on any lattice with the right axioms.  The G derivation
works for any ζ — the packing only affects the specific value
of G, not the mechanism by which gravity emerges.

This investigation runs in parallel with the derivations, not
in series.  It is about whether A5 (ζ = 1/4) can be promoted
from a free parameter to a geometric consequence — and if so,
which geometry nature selects.
