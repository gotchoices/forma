# Physics from Fabric

**Status:** Outline
**Audience:** General engineering background — no assumed knowledge of
thermodynamics, information theory, quantum physics, or advanced
mathematics.  Concepts explained as introduced.

**Purpose:** How a discrete lattice at the smallest possible scale
produces both electromagnetism and gravity from first principles.
No equations of physics are imported — Maxwell's equations and
Einstein's gravitational constant are derived as outputs.

---

## Abstract

Empty space has structure.  GRID (Geometric Relational Interaction
Domain) models the vacuum as a lattice of identical cells at the
Planck scale (~10⁻³⁵ m), connected by edges that carry energy.
Energy scatters at junctions according to a single parameter-free
rule determined by conservation — and in the continuum limit, the
resulting wave propagation obeys Maxwell's equations.  Separately,
counting the lattice's possible configurations produces an entropy
proportional to surface area, from which the gravitational field
equation and Newton's constant G emerge.  Electromagnetism is
mechanical (what the edges carry); gravity is statistical (how many
ways the edges can be arranged).  Both forces arise from the same
lattice, governed by two constants: α ≈ 1/137 (coupling strength,
measured) and ζ = 1/4 (information resolution, likely geometric).
Computational simulations verify directional wave propagation,
linear superposition, and the correct gravitational power law —
all without importing any equation of physics.

---

## Contents

1. [The question](#1-the-question)
2. [The fabric](#2-the-fabric)
3. [How energy propagates](#3-how-energy-propagates)
4. [What the lattice can't do mechanically](#4-what-the-lattice-cant-do-mechanically)
5. [Counting states](#5-counting-states)
6. [What is a quarter-bit?](#6-what-is-a-quarter-bit)
7. [How edges build up to patterns](#7-how-edges-build-up-to-patterns)
8. [How counting states produces gravity](#8-how-counting-states-produces-gravity)
9. [Why hexagons?](#9-why-hexagons)
10. [Two knobs](#10-two-knobs)
11. [The two faces of the fabric](#11-the-two-faces-of-the-fabric)
12. [Connecting to the particle model](#12-connecting-to-the-particle-model)
13. [What remains open](#13-what-remains-open)

---

## 1. The question

What is empty space made of?

We know how to *describe* electromagnetism (Maxwell's equations)
and gravity (Newton's G, Einstein's curvature).  But no one has
explained *why* the vacuum has the properties it does — why
light travels at c, why gravity is so weak, why electric and
magnetic fields are coupled in exactly the way they are.

This primer describes a model — GRID (Geometric Relational
Interaction Domain) — that derives both forces from a single
structure: a lattice of identical cells at the smallest possible
scale, connected by edges that carry energy.  The electromagnetic
equations emerge from how energy propagates through this lattice.
The gravitational constant emerges from counting the lattice's
possible configurations.  Nothing is imported — both are outputs
of the lattice's rules.


## 2. The fabric

What the lattice is, how big the cells are, and what each
cell can do.

- Cells at the Planck scale (~10⁻³⁵ m).  How small is that?
  (Scale analogies.)
- Each cell is connected to its neighbors by edges.  Each edge
  carries energy.
- Energy hops from cell to cell, one step per tick.  This
  hopping speed IS the speed of light: c = one cell per tick.
- Cells interact only with their immediate neighbors.  There is
  no action at a distance.
- The full rule set (six axioms, stated in plain language):
  1. Four-dimensional grid of identical cells
  2. One dimension is time (causal ordering); three are space
  3. Each edge carries energy
  4. Energy is conserved at every junction
  5. Each cell contributes a fixed fraction of one bit of
     information (the resolution ζ — explained in §6)
  6. The coupling strength between edges is set by a single
     constant α


## 3. How energy propagates

From edges to electromagnetic waves.

- Each edge carries energy.  When energy arrives at a junction,
  it scatters into the outgoing edges according to a simple
  rule: outgoing_i = (2/N) × total − incoming_i, where N is
  the number of edges meeting at the junction
- This rule has no free parameters — it is uniquely determined
  by energy conservation at equal-impedance junctions.  It is
  the same principle as a pipe junction or a beam splitter.
- A single pulse hitting one junction mostly reflects backward.
  But a coherent wavefront — many edges excited in phase —
  propagates forward, because the scattered wavelets from
  neighboring junctions constructively interfere in the forward
  direction and cancel sideways.  This is how wavelets at each
  junction combine to maintain a directed wave.
- Simulations confirm this.  A broad wavefront propagates at
  ~0.7 lattice units per tick, barely spreading.  A point
  source radiates in all directions, like a pebble in a pond.
  Both behaviors emerge from the same parameter-free rule.
- Two wavefronts crossing each other pass through and
  recombine unchanged — superposition, verified to ~10⁻¹⁵
  residual error.
- In the continuum limit (many cells, long wavelengths),
  this propagation obeys Maxwell's equations.  No Maxwell was
  put in — the equations fell out of the scattering rule.
- Charge quantization also emerges: if the energy on edges
  has a periodic (cyclic) character, the winding number
  around a loop is an integer.  Charge comes in integer
  multiples for free.


## 4. What the lattice can't do mechanically

The same scattering rule that propagates light does NOT
produce gravity.

- A lattice with energy on edges naturally produces wave
  equations (that's how we got electromagnetism above)
- But what about gravity?  Try biasing the edges — increase
  the energy in a region to simulate a massive object
- Result: the disturbance field falls off as 1/r² (in 2D).
  This is elastic behavior — like stretching a rubber sheet.
- Gravity's force falls off as 1/r (in 2D) — a different
  power law.
- Simulation proof: a lattice of springs matches elasticity
  exactly (R² ≈ 0.9999) but does NOT match gravity at any
  parameter setting.
- However, a scalar field on the same lattice — where each
  cell holds a single value rather than a position — DOES
  produce the 1/r force (R² ≈ 0.999).  The difference:
  elasticity is about how edges move in space (a vector
  field); gravity is about how edges are *configured* (a
  scalar field).  Same lattice, different physics.
- The conclusion: gravity comes from counting configurations,
  not from mechanical distortion.  This leads us to counting
  states.


## 5. Counting states

Why the number of possible arrangements matters.

- Each edge in the lattice can hold many different values.
  The total number of distinct arrangements in a region is
  called the entropy of that region.
- Example: a shuffled deck of cards has high entropy (many
  arrangements look "random"); a sorted deck has low entropy
  (only one arrangement).  Nothing about heat — just counting.
- Systems drift toward arrangements with more possibilities,
  not because of a force, but because there are simply more
  ways to be in a high-entropy state than a low-entropy one
- Temperature is the exchange rate between energy and entropy:
  how much energy must you pay to rearrange one bit's worth
  of the lattice
- On the GRID lattice: the energy values on edges in a region
  define its entropy.  A region with more edges in excited
  states has higher entropy.  This counting is what produces
  gravity.


## 6. What is a quarter-bit?

The information content of a single cell.

- A "bit" is one yes/no answer — the smallest unit of
  information (0 or 1)
- How much information does one cell of the lattice carry?
  Information theory sets a lower bound: the information
  content of any region of space is proportional to its
  surface area, not its volume, and the density works out to
  about 1 bit per 4 Planck-area cells.  Each cell contributes
  roughly ¼ of a bit.
- A quarter-bit is a "fractional bit" — one cell alone
  cannot encode a full yes/no answer, but four cells together
  can.  Analogy: one pixel alone can't make a recognizable
  image, but a 2×2 block can encode one meaningful symbol.
- We take ζ = 1/4 as a working hypothesis and ask: how do you
  actually construct a quarter-bit?  A cell needs four
  connections — four edges leading into it — so that each
  edge carries 1/4 of the cell's information to one neighbor.
  In 3D space, this means cells with four faces (tetrahedra).
  On a 2D sheet, adapt to three connections per cell — which
  leads directly to hexagons (§9).
- This number ζ = 1/4 is one of GRID's two constants.  It
  determines the strength of gravity.  Unlike α, it may
  follow from the lattice geometry itself rather than being
  a free parameter (see §10).


## 7. How edges build up to patterns

From fractional bits to the rich structure of physics.

- Each cell holds ¼ bit, but describing the full state of
  the lattice at a point (direction, magnitude, and rate of
  change of energy) requires ~1000 bits
- A sliding window of ~4000 cells is needed to encode one
  complete local description — like reading a sentence from
  a stream of individual letters
- The information is holographic: it lives on surfaces (2D
  boundaries), not in volumes (3D bulk).  The bulk is
  redundant — you can reconstruct the interior from the
  boundary.
- Patterns of edge values across many cells ARE the physical
  fields.  A smooth wave across many cells is a light wave.
  A systematic gradient in entropy is a gravitational field.


## 8. How counting states produces gravity

From information density to the gravitational constant.

- Start with the lattice and its resolution: each cell
  contributes ζ = 1/4 bit.  The total information in a
  region is proportional to its surface area (not volume).
- When energy flows through a region, it changes the values
  on the edges it crosses — it changes the entropy.
- The amount of entropy change is: δS = ζ × δA (change in
  information = resolution × change in area)
- Energy and entropy are linked by temperature:
  δQ = T × δS (energy deposited = temperature × entropy
  change)
- The lattice has a causal structure — a time direction.
  Any observer accelerating through the lattice encounters
  a causal horizon (a boundary beyond which information
  cannot reach them).  That horizon has a temperature
  proportional to the acceleration: T = a/(2π) in natural
  units.
- Combining these: energy flow through a region changes
  area, mediated by temperature and resolution.  The
  relationship between energy content and geometric change
  IS the gravitational field equation.
- The gravitational constant falls out directly:
  G = 1/(4ζ) = 1/(4 × ¼) = 1 in natural units.
  Converting to SI units recovers the measured value
  G = 6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻².
- Simulation verification: on the same lattice where
  mechanical springs gave the wrong power law (§4), a
  scalar field with entropy-driven dynamics gives the
  right one (1/r in 2D, R² ≈ 0.999).


## 9. Why hexagons?

The shape of the fabric and why it matters.

- The quarter-bit (§6) tells us a 2D cell needs three
  connections.  A lattice where every junction has three
  edges is a hexagonal mesh.
- But there are two more independent reasons hexagons win.
- **Wave propagation.**  On a triangular lattice, each
  junction has 6 edges.  When a wave hits a 6-way junction,
  ~44% of its energy bounces back.  On a hexagonal lattice,
  each junction has only 3 edges — reflection drops to ~11%.
  Simulations confirm cleaner propagation: on the hexagonal
  lattice, even a single pulse propagates forward (53%
  directionality vs 33% isotropic).  On the triangular
  lattice, single pulses scatter backward.
- **Flexibility.**  Triangles with fixed-length edges are
  rigid — they cannot deform.  Hexagons with fixed-length
  edges can flex, bend, and curve without breaking.  A
  soccer ball uses pentagons to bend an otherwise flat hex
  mesh into a sphere.
- Pentagon = curvature defect.  A region with extra pentagons
  is curved inward.  The density of pentagon defects maps
  directly to gravitational curvature around a massive object.
- A wave propagating on the hexagonal lattice cannot detect
  bending.  The scattering rule depends only on N (the number
  of edges) and their amplitudes — not on angles or
  curvature.  Locally, every junction looks the same.  Only
  topological defects (a junction with 2 edges instead of 3)
  are detectable.  This is the equivalence principle at the
  lattice level: gravity is invisible locally.
- 2D hex mesh: works for the flat material sheets where
  particles live as standing waves
- 3D extension: the spatial dimensions use an analogous
  structure.  How the hex dual generalizes to 3D is an
  active area of work.


## 10. Two knobs

The entire model has two constants.

- **α ≈ 1/137** — the coupling strength.  Sets how strongly
  edges interact at junctions.  Determines the strength of
  electromagnetism.  This is the one number GRID takes from
  experiment.
- **ζ = 1/4** — the resolution.  Sets how much information
  each cell contributes.  Determines the strength of gravity
  through G = 1/(4ζ).  Unlike α, ζ may be derived from the
  lattice geometry: in 3D, a simplicial cell (tetrahedron)
  has four face-neighbors, giving ζ = 1/4 as a geometric
  consequence rather than a free parameter.
- If ζ follows from geometry, α is the sole measured input.
- Everything else — the speed of light, Planck's constant,
  the vacuum permittivity and permeability, Boltzmann's
  constant — turns out to be unit conversion, not physics.
  They are artifacts of measuring length in meters, time in
  seconds, and energy in joules.
- Why is gravity so much weaker than electromagnetism?
  Because α and ζ are very different numbers.  Whether they
  are fundamentally related is an open question — answering
  it would reduce the model to zero free parameters.


## 11. The two faces of the fabric

How one lattice produces two different forces.

- **Electromagnetism** is mechanical.  Energy scatters at
  junctions → waves propagate → Maxwell's equations emerge
  in the continuum limit.  Direct, dynamic, deterministic.
  No state-counting required.
- **Gravity** is statistical.  Counting edge arrangements →
  entropy proportional to area → geometry adjusts to
  accommodate energy flow → the gravitational field equation
  emerges.  Collective and emergent.
- Same lattice, different physics.  Electromagnetism is what
  the edges *carry*.  Gravity is what the edges *are* (how
  many ways they can be arranged).
- This explains the hierarchy: scattering at a single
  junction is local and strong.  Statistical effects require
  collective behavior of enormous numbers of cells and are
  correspondingly gentle.  Gravity is weak because it is a
  crowd effect, not a local interaction.


## 12. Connecting to the particle model

How GRID feeds into MaSt.

- MaSt (Material–Space–time) is the particle model built
  on top of GRID.  It takes the electromagnetic wave
  equation and the coupling constant α — both derived by
  GRID — and constructs particles as standing waves on
  compact (periodic) geometry.
- The material sheets (Ma) are 2D regions of the lattice
  where the mesh is flat and periodic — standing waves
  on these sheets are the particles of nature
- Rolling a hexagonal sheet into a torus costs nothing.
  A wave propagating on the torus cannot detect the bending
  — the scattering rule is the same whether the sheet is
  flat or rolled.  Curvature appears only in the surrounding
  3D lattice, which must rearrange (introducing pentagonal
  defects) to accommodate the torus.  The rearrangement IS
  the particle's gravitational field.
- The spatial dimensions (S) are the 3D bulk lattice where
  the mesh can curve — curvature is gravity
- Particles are energy patterns on flat lattice.  Gravity is
  the statistical behavior of curved lattice.  Both arise
  from the same cells and edges.


## 13. What remains open

- Can α be derived from ζ (or vice versa)?  This would
  reduce the model to zero free parameters.
- The gravity derivation currently bridges from the discrete
  lattice to a smooth continuum.  Making this bridge
  rigorous — proving that discrete cell-counting produces
  smooth curvature — is unfinished.
- Does the hexagonal lattice generalize cleanly to 3D?
  The 2D hex mesh and its pentagon defects work beautifully;
  the 3D analog is under development.
- Can the lattice's junction rules reproduce quantum
  mechanics, or does something additional need to be added?
  MaSt offers a geometric account of several quantum
  phenomena (quantized energy levels, uncertainty, spin)
  that emerge from wave mechanics on compact geometry
  rather than being postulated.
- Every observer is built from lattice excitations.
  Because all forces come from the same lattice, all
  measuring instruments transform the same way under
  motion — which may explain why no observer can detect
  the lattice itself.
- What is the specific energy pattern on the lattice that
  becomes a confined standing wave — a particle?  Finding
  this initial condition (the "alpha chord") would connect
  GRID directly to the particle spectrum.


## References

- GRID technical documents: `grid/foundations.md`,
  `grid/maxwell.md`, `grid/gravity.md`, `grid/synthesis.md`
- Primer: `across-through.md` — the conjugate pattern
  underlying wave propagation on the lattice
- Primer: `charge-from-energy.md` — how geometry produces
  particles (the MaSt layer above GRID)

Historical context (these works arrived at compatible results
from different starting points; GRID does not import them):
- Jacobson (1995): derived gravity from thermodynamics on
  horizons
- Bekenstein (1973), Hawking (1975): discovered the 1/4
  information density from black hole physics
