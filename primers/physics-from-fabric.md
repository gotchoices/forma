# Physics from Fabric

How a discrete lattice at the Planck scale produces both
electromagnetism and gravity — from one structure, one measured
constant, and nothing imported.

**Audience:** General engineering background.  No assumed
knowledge of thermodynamics, information theory, quantum
physics, or advanced mathematics.  Concepts explained as
introduced.

---

## Contents

1. [The question](#1-the-question)
2. [The fabric](#2-the-fabric)
3. [Clock hands and connections](#3-clock-hands-and-connections)
4. [From connections to Maxwell](#4-from-connections-to-maxwell)
5. [What waves can't explain](#5-what-waves-cant-explain)
6. [Counting arrangements](#6-counting-arrangements)
7. [The quarter-bit](#7-the-quarter-bit)
8. [From counting to gravity](#8-from-counting-to-gravity)
9. [One lattice, two forces](#9-one-lattice-two-forces)
10. [The defect cost](#10-the-defect-cost)
11. [Connecting to particles](#11-connecting-to-particles)
12. [One free parameter](#12-one-free-parameter)

---

## 1. The question

What is empty space made of?

We know how to *describe* electromagnetism (Maxwell's
equations) and gravity (Newton's G, Einstein's curvature).
But no one has explained *why* the vacuum has the properties
it does — why light travels at c, why gravity is so weak, why
electric and magnetic fields are coupled in exactly the way
they are.

This primer describes a model — GRID (Geometric Relational
Interaction Domain) — that derives both forces from a single
structure: a lattice of identical cells at the smallest
possible scale, connected by edges.  The electromagnetic
equations emerge from the phase dynamics of this lattice.
The gravitational constant emerges from counting the lattice's
possible configurations.  Nothing is imported — both forces
are outputs of the lattice's rules.


## 2. The fabric

Imagine an enormous grid of identical cells filling all of
space.  Each cell is unimaginably small — about 10⁻³⁵ meters
across, a length called the **Planck length**.  To put that
in perspective: a Planck length is to an atom as an atom is
to the observable universe.

Each cell is connected to its neighbors by edges.  Nothing
else exists — no background, no container.  The lattice IS
space.

GRID rests on six axioms — minimal assumptions about this
lattice:

1. **Four-dimensional grid of identical cells.**  Three
   dimensions of space, one of time.  Disturbances hop from
   cell to cell, one step per tick.  This hopping speed IS
   the speed of light.

2. **One dimension is time.**  Time flows forward only.
   Information moves from past to future, never the reverse.
   This is what makes one dimension special — it carries a
   causal ordering that the spatial dimensions do not.

3. **Each cell carries a phase.**  Think of a tiny clock hand
   glued to each cell, pointing in some direction on a circle.
   The clock hand can swing freely — forward or backward on
   each tick — but the physical content is not where any one
   clock hand points.  Only the *differences* between
   neighboring clock hands matter.

4. **Relabeling doesn't change the physics.**  You can reset
   every cell's clock hand by a different amount, and the
   physics stays the same — provided you adjust the
   connections between cells to compensate.  This principle,
   called gauge invariance, turns out to force the lattice to
   carry additional information on its edges.  That additional
   information is the electromagnetic field.

5. **Each cell contributes a quarter-bit of information.**
   One cell alone cannot encode a full yes/no answer.  It
   takes four cells working together to register one bit of
   physical information.  This resolution, ζ = 1/4, sets the
   information density of the lattice.

6. **The coupling strength is α ≈ 1/137.**  A single
   dimensionless number — the fine-structure constant — sets
   how strongly the phase field couples to the connection
   field.  This is the one number GRID takes from experiment.

That's it.  Six rules.  Everything else — Maxwell's equations,
the gravitational constant, charge quantization, the speed of
light — is derived.


## 3. Clock hands and connections

Axioms 3 and 4 are the engine of electromagnetism.  Here is
how they work.

Each cell has a phase — a clock hand pointing somewhere on a
circle.  The phase at cell A might read "45°" and at
neighboring cell B "50°."  The difference (5°) is the
physically meaningful quantity.  The absolute angles are
arbitrary — if someone secretly added 30° to every clock in
the universe, nothing would change.

Now here is the key step.  Axiom 4 says you can add *different*
amounts to different cells and the physics still doesn't change.
Add 10° to cell A and 25° to cell B.  The old difference was
5°.  The new phases are 55° and 75°, with a difference of 20°.
That's different — so something must compensate.

The compensating quantity lives on the **edge** between A
and B.  Call it the **connection**.  It adjusts whenever you
relabel, so that the combination "phase difference minus
connection" is always the same regardless of how you relabel.
This combination is the gauge-invariant, physically real
quantity.

The connection is not something we added to the lattice by
hand.  It is *forced to exist* by the relabeling rule.  If
you demand that arbitrary local relabeling doesn't change the
physics, you must have a connection on every edge.  There is
no choice.

The lattice now holds two kinds of state:

| Where | What | What it becomes |
|-------|------|-----------------|
| On cells (nodes) | Phase (clock hand) | Matter field |
| On edges (links) | Connection | Electromagnetic field |

Both are part of the lattice's memory.  Both update on every
tick.  A propagating ripple in the connection states IS a
photon — a traveling disturbance in the electromagnetic
field.  The clock-hand phases are the matter; the connections
are the light.


## 4. From connections to Maxwell

Now zoom out.  Instead of individual cells, look at the
lattice from a great distance — many cells across, many ticks
long.  The discrete phases and connections blur into smooth
fields.  This is the **continuum limit**, like zooming out
from individual pixels until you see a photograph.

In this limit, the connection field becomes the electromagnetic
potential A_μ — the standard object from which E and B fields
are computed.  The physically real quantity — the part that
doesn't change under relabeling — is the **curl** of A around
a closed loop.  This curl is the electromagnetic field tensor
F_μν, which packages all six components of E and B into one
object.

To get equations of motion, we need a rule for how the lattice
evolves.  The rule is the **principle of least action**: among
all possible evolutions, the lattice follows the one that
extremizes a single number (the action).  The form of the
action is uniquely fixed by three requirements that come
directly from the axioms:

- Gauge-invariant (only depends on the curl, not on the
  relabeling-dependent potential)
- Lorentz-invariant (same for all observers)
- Local (depends on fields at a point, not at a distance)

There is exactly one action that satisfies all three.  Varying
it produces **all four of Maxwell's equations**:

| Equation | Name | What it says |
|----------|------|-------------|
| ∇ · **E** = ρ | Gauss's law | Charge creates diverging electric field |
| ∇ × **B** − ∂**E**/∂t = **J** | Ampère's law | Current and changing E create curling B |
| ∇ × **E** + ∂**B**/∂t = 0 | Faraday's law | Changing B creates curling E |
| ∇ · **B** = 0 | No monopoles | Magnetic field lines have no endpoints |

The first two come from varying the action.  The last two
are automatic — they are geometric identities that hold for
any field defined as a curl.  No Maxwell was imported.  The
equations fell out of the lattice structure.

**Charge quantization** also emerges for free.  The phase is
periodic — it wraps around every 2π.  A closed loop of cells
where the phase winds through a full 2π cycle is a
**topological vortex**.  You cannot have half a vortex.  The
winding number must be an integer: 0, ±1, ±2, ...  Each
integer is a unit of charge.  Charge comes in discrete
packets because the clock hand is a circle, not a line.

Simulations verify the key predictions: directional wave
propagation emerges from the lattice geometry alone, and two
crossing wavefronts pass through each other unchanged
(superposition verified to ~10⁻¹⁵ residual error).


## 5. What waves can't explain

The same lattice that produces electromagnetic waves does
NOT produce gravity — at least not mechanically.

Try it: put energy into a region of the lattice and let the
wave equation propagate the disturbance outward.  The
resulting field falls off as 1/r² (in 2D simulations).  This
is elastic behavior — like poking a rubber sheet.  The
displacement spreads according to elasticity theory, which
predicts 1/r².

But gravity's force falls off as 1/r (in 2D) — a
fundamentally different power law.

Simulations confirm this cleanly.  A lattice of springs
matches elasticity theory to R² ≈ 0.9999 but does NOT match
gravity at any parameter setting.  The mechanical approach
gives the wrong answer.

However, a **scalar field** on the same lattice — where each
cell holds a single number representing its configuration
count, rather than a displacement vector — DOES produce the
1/r force (R² ≈ 0.999).  The difference: elasticity is about
how edges move in space (a vector field); gravity is about
how edges are *configured* (a scalar counting field).

The conclusion: gravity comes from counting configurations,
not from mechanical distortion.  This leads us to entropy.


## 6. Counting arrangements

**Entropy** is a count of possibilities.

Each edge in the lattice can hold many different values.  The
total number of distinct arrangements in a region is the
entropy of that region.  Nothing about heat — just counting.

A shuffled deck of cards has high entropy: many arrangements
look "random."  A sorted deck has low entropy: only one
arrangement qualifies.  Nobody pushes the deck toward
disorder — there are simply more disordered arrangements than
ordered ones.  Systems drift toward higher entropy because
there are more ways to be there.

**Temperature** is the exchange rate between energy and
entropy: how much energy must you pay to rearrange one bit of
the lattice.  High temperature means rearrangements are cheap.
Low temperature means they are expensive.

On the GRID lattice: the values on edges in a region define
its entropy.  A region with more excited edges has more
possible configurations, hence higher entropy.  This counting
is what produces gravity.


## 7. The quarter-bit

A **bit** is one yes/no answer — the smallest unit of
information (0 or 1).

How much information does one cell of the lattice carry?
There is a deep result from information theory: the
information content of any region of space is proportional
to its **surface area**, not its volume.  This is called the
**holographic principle** — the interior of a region is
redundant; all the information lives on the boundary.

The density works out to about 1 bit per 4 Planck-area
cells.  Each cell contributes roughly **¼ of a bit**.

A quarter-bit is a fractional bit — one cell alone cannot
encode a full yes/no answer, but four cells together can.
Think of it as an anti-aliasing constraint: no excitation
can have spatial frequency higher than 1/(4L), where L is
the cell size.

Where does 1/4 come from?  In 3D space, the simplest cell
shape is a tetrahedron — a triangular pyramid with four
faces.  Each face borders one neighbor.  Under the counting
scheme where the cell has no separate internal state — its
information is entirely encoded in its boundary relationships
— each cell contributes one share to four neighbors, giving
ζ = 1/4.  The value follows from the packing geometry of the
lattice, not from an external measurement.

This number ζ = 1/4 is one of GRID's two constants.  It
determines the strength of gravity.


## 8. From counting to gravity

Here is how counting arrangements produces the gravitational
field equation.

Start with the lattice and its resolution: each cell
contributes ζ = 1/4 bit.  The total information on any
surface of area A is:

> S = ζ × A = A/4

When energy flows through a region, it changes the values on
the edges it crosses — it changes the entropy.  Energy and
entropy are linked by temperature through the **Clausius
relation**:

> δQ = T × δS

(energy deposited = temperature × entropy change).  This is
basic thermodynamics, not a gravitational assumption.

Now the lattice's causal structure (axiom 2) enters.  Any
observer accelerating through the lattice encounters a
**causal horizon** — a boundary beyond which information
cannot reach them.  This horizon has a temperature
proportional to the acceleration:

> T = a / (2π)

This is the **Unruh effect** — a result from quantum field
theory on flat spacetime.  It connects acceleration (geometry)
to temperature (thermodynamics).

Combining these: energy flowing through a horizon changes the
horizon's area.  The rate of area change is related to the
curvature of spacetime through a kinematic identity (the
Raychaudhuri equation — no gravitational assumption, just
geometry).  Plugging everything together:

> Energy content at a point determines the curvature at
> that point.

This IS the gravitational field equation.  The gravitational
constant falls out directly:

> G = 1/(4ζ) = 1  (in natural units)

Converting to SI units recovers the measured value:
G = 6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻².

The cosmological constant Λ also appears, for free, as an
integration constant — it is not put in by hand.

**Why does spacetime bend around mass?**  Because energy
flowing through causal horizons changes their entropy, and
entropy is proportional to area.  The geometry must adjust
to accommodate the entropy change.  Spacetime bends because
information flow forces geometric change.

Simulation verification: on the same lattice where mechanical
springs gave the wrong power law (§5), an entropy-driven
scalar field gives the right one (1/r in 2D, R² ≈ 0.999).


## 9. One lattice, two forces

The lattice produces two forces through two completely
different mechanisms:

| | Electromagnetism | Gravity |
|--|------------------|---------|
| **Mechanism** | Dynamics — phase oscillations propagate as waves | Thermodynamics — entropy of configurations determines geometry |
| **What it uses** | Phases on cells, connections on edges, gauge symmetry | Information density, causal horizons, entropy-area law |
| **Free parameter** | α ≈ 1/137 (coupling strength) | ζ = 1/4 (information resolution) |
| **Nature** | Local, mechanical, deterministic | Collective, statistical, emergent |

Electromagnetism is what the edges *carry*.  Gravity is how
the edges *are arranged*.

This explains the **hierarchy** — why gravity is so vastly
weaker than electromagnetism.  Phase interactions happen at
every junction, every tick.  They are local and immediate.
Entropy effects require the collective behavior of enormous
numbers of cells.  You need ~10⁶⁰ cells' worth of area
before the statistical effect becomes significant.  Gravity
is weak because it is a crowd effect, not a local interaction.


## 10. The defect cost

We now have electromagnetism (from phase dynamics) and gravity
(from entropy).  But what is a charged particle in this
picture?  And where does α show up physically?

In the companion framework MaSt (Material Space), a particle
is a **photon confined to a 2D sheet** that is wrapped into a
torus and embedded in the 3D spatial lattice.  The standing
wave circulates on the torus, and its phase winds through a
full 2π cycle going once through the tube.

From the ambient 3D lattice's perspective, this 2π winding
is a **topological defect** — an irreducible twist in the
phase field that cannot be smoothed away.  Gauss's law
detects it as electric charge.

The standing wave on the sheet carries the particle's full
rest energy mc² — this is the particle's mass.  But the
ambient 3D lattice must also store energy to accommodate
the topological twist.  This accommodation energy is the
**Coulomb field** — the static electric field radiating
outward from the charge.

The energy partition is exact:

| Where | Energy | What it is |
|-------|--------|------------|
| On the 2D sheet | mc² | The standing wave — mass |
| In the 3D ambient lattice | αmc² | The Coulomb field — the cost of the twist |

The fraction of total energy that leaks into the ambient
lattice is:

> E_Coulomb / E_wave = α ≈ 1/137

Only 1/137 of the wave's energy appears externally as
Coulomb field.  The remaining 136/137 stays on the sheet,
circulating as the standing wave that constitutes the
particle's mass.

This is what α *is* in the GRID picture: the **energy tax**
that the ambient lattice levies on a topological defect.  It
is an impedance mismatch — the 2D sheet and the 3D lattice
are two different fabrics, and energy crosses between them
at a rate set by their structural coupling.

Alpha is not a mysterious constant attached to the particle.
It is a property of the **junction** between two grid fabrics
of different dimensionality.  The particle inherits it from
the substrate — it doesn't generate it.


## 11. Connecting to particles

GRID provides the substrate.  MaSt (Material–Space–time)
builds particles on top of it.

MaSt takes the electromagnetic wave equation and the coupling
constant α — both provided by GRID — and constructs particles
as standing waves on compact (periodic) 2D sheets.

The material sheets (Ma) are regions of the lattice where the
mesh is flat and periodic.  A 2D triangular lattice (like a
sheet of graphene) wrapped into a torus creates a closed
surface with no boundary.  Standing waves on this torus are
the particles of nature.

The torus topology produces quantum numbers for free:

- **Charge:** the winding number through the tube (how many
  times the phase wraps through 2π).  Integer-valued by
  topology.
- **Magnetic moment:** winding around the ring (2 turns for
  the electron).
- **Spin:** the ratio of tube windings to ring windings
  (1/2 for the electron).

The sheet itself stays flat — all triangles remain
equilateral, all edges remain one Planck length.  It is the
*ambient 3D lattice* that must rearrange to accommodate the
torus.  This rearrangement IS the particle's gravitational
field.  The flat sheet carries mass.  The warped ambient
lattice carries gravity.  Both arise from the same cells and
edges.


## 12. One free parameter

The entire framework has two constants:

**ζ = 1/4** — the information resolution.  Likely derived
from the lattice geometry (tetrahedral cells in 3D have four
face-neighbors, giving ζ = 1/4 as a geometric consequence).
Determines the strength of gravity through G = 1/(4ζ).

**α ≈ 1/137** — the coupling strength.  Measured from
experiment.  Determines the strength of electromagnetism —
the energy cost of a topological defect, the impedance
mismatch at the junction between 2D sheets and 3D space.

If ζ follows from geometry, **α is the sole free parameter**.

Everything else that appears in physics textbooks as a
"fundamental constant" turns out to be either derived or
definitional:

| Constant | What it really is |
|----------|-------------------|
| c (speed of light) | One cell per tick — defines the ratio of length to time units |
| ℏ (Planck's constant) | One phase cycle per Planck energy — defines energy units |
| k_B (Boltzmann's constant) | One bit per Planck temperature — defines temperature units |
| ε₀, μ₀ (vacuum permittivity/permeability) | Both equal 1 in natural units — they encode α in SI disguise |
| G (gravitational constant) | 1/(4ζ) — derived from information resolution |

The SI values of these constants (c = 3 × 10⁸ m/s, etc.) are
not deep — they just reflect the ratio between human-scale
units and Planck-scale units.

**What remains open:**

- **The continuum limit.**  The gravity derivation bridges
  from a discrete lattice to smooth differential geometry.
  Making this bridge rigorous is unfinished — it is an open
  problem shared with all of quantum gravity.

- **3D lattice structure.**  The 2D sheet geometry is well
  understood (triangular lattice, torus wrapping).  How the
  3D spatial lattice generalizes — its cell shapes, its
  defect structure — is under development.

- **Quantum mechanics.**  GRID does not derive QM from
  scratch.  MaSt offers geometric origins for several quantum
  phenomena (quantized energy as standing-wave modes,
  uncertainty as Fourier bandwidth, spin as winding topology),
  but a full derivation of quantum mechanics from the lattice
  is not claimed.

- **Why α ≈ 1/137.**  The value of α is a free parameter.
  The lattice permits a wide range of coupling strengths
  (verified computationally).  What selects the observed
  value is unknown.  GRID explains what α *means* — the
  impedance mismatch at a dimensional junction — but not
  why it has the value it does.

---

## References

GRID technical documents:
- [`grid/foundations.md`](../grid/foundations.md) — the six axioms
- [`grid/maxwell.md`](../grid/maxwell.md) — full Maxwell derivation
- [`grid/gravity.md`](../grid/gravity.md) — full gravity derivation
- [`grid/synthesis.md`](../grid/synthesis.md) — what GRID proves and doesn't

Related primers:
- [`alpha-in-grid.md`](alpha-in-grid.md) — deep dive on the role of α
- [`across-through.md`](across-through.md) — the conjugate pattern underlying wave propagation
- [`charge-from-energy.md`](charge-from-energy.md) — how geometry produces particles (the MaSt layer)

Historical context (these works arrived at compatible results
from different starting points; GRID does not import them):
- Jacobson (1995): derived gravity from thermodynamics on horizons
- Bekenstein (1973), Hawking (1975): discovered the 1/4 information density from black hole physics
- Wilson (1974): lattice gauge theory — gauge fields on discrete lattices
