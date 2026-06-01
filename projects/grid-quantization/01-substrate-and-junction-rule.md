# Ch. 1 — The substrate and the junction rule

**Status:** Draft (prose, first pass). Part of the [presentation arc](README.md#presentation-arc).
**Grade:** [derived] — inherited substrate, cited rather than re-derived.
**Role:** establish the discrete medium and its local update rule — the stage on which the rest is built.

GRID models space not as a continuum but as a discrete network: a graph
of **nodes** joined by **edges**, advancing under a clock. Everything in
the chapters that follow happens on this network. This chapter fixes
three things — the network's shape, the single quantity each piece of it
carries, and the local rule by which that quantity updates. None of it
is new; the substrate is the one established in
[foundations.md](../../grid/foundations.md),
[hexagonal.md](../../grid/hexagonal.md), and the
[sim-maxwell](../../grid/sim-maxwell/) study, and is set out here only to
fix notation and keep the arc self-contained.

## 1.1 The honeycomb lattice

The network is a **honeycomb** (hexagonal) lattice — a tiling of
hexagons. Its defining feature is its **coordination number**, the
number of edges meeting at each node, which is **three**. A node where
three edges meet is a **Y-junction**, and it is where the action is: a
signal arriving along one edge is redistributed onto the others.

The physical degrees of freedom live on the **edges**, not the nodes. In
GRID's "cell = its edges" reading, an edge is the elementary cell and a
node is a junction — a place where cells meet and interact
([hexagonal.md](../../grid/hexagonal.md)). Three is the smallest
coordination that lets a signal both continue onward and branch, and it
is the choice that gives the medium its particular scattering behaviour
(§1.4). The honeycomb used here is the two-dimensional sheet; the full
GRID lattice has **three spatial dimensions** (plus the timelike axis
A2 supplies), but the account of light can be developed on the sheet.

## 1.2 The cell's state: a bounded, periodic phase

Each edge carries one degree of freedom: a **phase** θ — an angle, a
position on a circle, with θ and θ + 2π denoting the *same* state. It is
like a clock face: the cell's state is where a hand points, and **only
the angle matters — the cell has no separate amplitude or magnitude,
only the phase**. This is **axiom A3**.

Two properties of this choice are used repeatedly and are worth naming
before they are needed:

- **The phase is compact (periodic).** It lives on a closed circle of
  circumference 2π; advancing by a full turn returns to the start. This
  per-edge circle is what GRID calls the **ℵ-line**
  ([foundations.md](../../grid/foundations.md)) — the smallest compact
  dimension in the framework.
- **Only differences are physical.** The absolute value of θ on a single
  cell is not observable; only the *difference* in phase between
  neighbouring cells carries content. A uniform shift of every cell's
  phase changes nothing — the lattice's gauge freedom (axiom A4).

A propagating disturbance, then, is not a value sitting on one cell but a
*pattern of differences* moving across cells. The junction rule (§1.4)
governs how that pattern moves.

## 1.3 The clock

Time on the lattice is **discrete**: the network advances in synchronous
steps called **ticks**. The discreteness comes from **axiom A1** (the
four-dimensional causal lattice supplies discrete time and the length
scale L); **axiom A2** then fixes the Lorentzian signature (1,3) that
distinguishes timelike from spacelike, and so the causal ordering. At
each tick, every junction reads its current inputs and produces its
outputs, and nothing propagates faster than **one edge per tick** —
the lattice's *causal* ceiling, the analog of the speed of light's
limiting role in the continuum. (Actual wave packets move slower than
this ceiling: the photon's measured phase velocity is ≈ 0.41 of one edge
per tick — §2.3. The ceiling and the measured wave speed are different
numbers on the lattice; the continuum *c* is both at once.)

So the substrate is a clocked network: edges hold phases, the clock
ticks, and at each tick the junctions act. What remains is to say what
the junctions do.

## 1.4 The junction rule

At a Y-junction the signals arriving on the three edges are scattered
into the signals leaving on them. The rule is not chosen freely; it is
fixed by two requirements:

- **energy conservation** — the junction neither creates nor destroys
  signal energy, and
- **equal impedance** — the three edges are physically equivalent, so
  the junction treats them symmetrically.

For a junction of N equal edges, the impedance-matched rule meeting both
— unique under the standard convention of real, time-symmetric scattering
— is

> outgoing_i = (2/N) · (total incoming) − incoming_i.

For the honeycomb, N = 3:

> outgoing = (2/3) · (sum of all incoming) − incoming.

This carries two coefficients. A signal arriving on one edge is
**transmitted** onto each of the other two with coefficient **2/3**, and
**reflected** back along its own edge with coefficient **−1/3**. The
reflection is *negative* — sign-flipped relative to the incoming signal.
That sign is not incidental: it is the single feature that makes the
medium dynamical rather than inert. It is recorded here and used later.
The coefficients and their derivation from impedance matching are in
[hexagonal.md](../../grid/hexagonal.md); the rule is the one simulated in
[sim-maxwell](../../grid/sim-maxwell/) and reimplemented in this
project's `scripts/lib.py`.

Two things this form glosses, both worth flagging up front. **What the
rule operates on:** in the simulated form each edge carries not a single
number but a *pair* of real directed amplitudes (a_fwd, a_bwd) — the
right-moving and left-moving components of the signal — and the rule is
applied to those amplitudes at the junctions (`scripts/lib.py:scatter_step`).
**Which layer that is:** this real-amplitude form is the *wave*
description, a linearisation around A3's compact phase rather than a
direct rule on the phase itself (the arithmetic *(2/3)·total − incoming*
is not defined on a circle). The relation between A3's underlying compact
phase and these linearised amplitudes is itself an open item — the
bit-conserving rule of [work/energy-and-coherence.md](work/energy-and-coherence.md)
§5–§6 — not addressed in this chapter.

## 1.5 Nothing electromagnetic was put in

The junction rule was built from geometry, energy conservation, and
equal impedance alone. No electric field, magnetic field, or Maxwell
equation enters its construction. That those *follow* — that a
disturbance on this network is light, obeying Maxwell's equations — is a
result derived from the rule, not an input to it
([maxwell.md](../../grid/maxwell.md), sim-maxwell). At bottom the
substrate is a clocked scattering network of phase-carrying edges;
electromagnetism is something it does.

---

The stage is set: a honeycomb of phase-carrying edges (each a small
compact circle, the ℵ-line), a discrete clock, and a single
impedance-matched scattering rule whose reflection is sign-flipped. The
remaining chapters (see the [arc](README.md#presentation-arc)) develop
what lives on this stage.

## Sources

- [foundations.md](../../grid/foundations.md) — A1 (4D discrete lattice; length scale L), A2 ((1,3) Lorentzian signature → causal ordering), A3 (compact phase / ℵ-line), A4 (gauge)
- [hexagonal.md](../../grid/hexagonal.md) — N = 3 scattering; the 2/3 transmission, −1/3 reflection
- [sim-maxwell](../../grid/sim-maxwell/) — the substrate simulation; Maxwell from the rule
- `scripts/lib.py` — this project's lattice / scatter / evolve implementation

## Claim discipline

[derived] / inherited. Everything here is established GRID substrate,
cited rather than re-derived. No quantum content, and no claim beyond
"this is the medium and its rule." The sign-flipped reflection is
recorded but not yet exploited; the ℵ-line is named but its role is not
yet drawn on; the gap between A3's compact phase and the simulated
real-amplitude wave form is flagged as an open item, not resolved here.
