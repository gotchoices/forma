# Chapter 1: Foundation

## §1. The chapter's job

This project sits parallel to [grid-primitive](../grid-primitive/), which collapsed the GRID lattice's internal structure into a single distributed object — a *cylinder primitive* carrying both magnitude (longitudinal stress) and phase (azimuthal direction) on one continuous body. That model is *analog-first*: continuous, mechanical, with state varying along a 1D extent and propagation by direct elasticity.

grid-couplet takes the opposite stance — *digital-first*. The lattice is built from explicit structural types: a **point** (0D primitive), an **edge** (1D relational object connecting two points), and a **dial** (an emergent n-D node, built from a closed loop of points and edges). The genus name **node** covers both points and dials.

The model in this stance is not new. [viz/grid-lab](../../viz/grid-lab.md) implements its dynamics. This chapter does not redefine that model. It states the model in the project's notation, separates which features are *posits* (taken as given) from which are *discovery targets* (questions the project examines), introduces the couplet as the lattice-building unit, and defines the wrap-promotion ladder that organizes the project's chapters.

grid-lab serves throughout as a working reference, not an authority. As long as the analyses here remain consistent with grid-lab's specification, the two stay aligned; where the project's chapters produce a result that suggests a different choice — a different sign convention, a different update-rule version, a different geometric default — the result takes precedence and the visualizer is updated to match.

## §2. The point

The foundational primitive is the **point** — a 0D node. It has no spatial extent and one piece of state: a single real-valued φ ∈ ℝ.

A deliberate choice: the point's value is not posited as bounded. The bounded-phase interpretation a dial exhibits is something that emerges later, from the closure operation that wraps a couplet chain into a dial (chapter 2's derivation). At the primitive level, the point is just a value-holder; whether the value behaves like an unbounded magnitude or a bounded phase depends on what closes around it.

A point may have any number of edges connecting at it. The point's **connection rule** forces all edges meeting there to share their endpoint value with the point's value. The point itself stores nothing else — it is, structurally, the location at which a shared value is held and updated.

Geometrically, a point is rendered as a single location with no extent. Edges meeting at a point all converge to the same location.

A point gathers its new value on the inhale phase of the master clock (§6). Its update rule is given in §7.

## §3. The edge

The **edge** is a 1D relational object connecting two points. It has two structural ends — a **tail** and a **head** — that fix once it is placed in a lattice. Together these define its **polarity**: the direction from tail to head.

An edge's value is its **integrated history** of the differential between its endpoint values, accumulated over time as the clock advances. Concretely, on each exhale phase the edge's stored value increments by k · (φ_tail − φ_head), where φ_tail and φ_head are the phases at the edge's two endpoints (set by the points there) and k is a translation factor introduced in §7.

The edge's value is therefore unbounded — it accumulates without periodic identification. Polarity is structural and fixed; the value is dynamic and can grow large.

The distinction between polarity and value matters. Polarity is direction-bearing: the edge always points from tail to head. The value is a real number, the running integral of the endpoint difference, sign-respecting. A negative value does not flip the edge's polarity; it indicates the integral has accumulated more from negative-difference epochs than from positive ones.

Geometrically, a default edge sits along an axis with its tail at −x and its head at +x.

## §4. The couplet

A **couplet** is one (edge, point) pair — the project's lattice-building unit. Picture an edge with one of its two endpoints distinguished as the couplet's *partner point*. The couplet packages a single propagation step: a magnitude carrier (the edge) joined to a phase carrier (the point), with the connecting interface (the junction, §8) coupling them under the clock.

The couplet is **posited** as the candidate functional building block at the lattice scale: larger structures are assembled from couplets, with each new couplet contributing exactly one edge and one new point to the lattice. Whether this assembly tiles 2D sheets exactly, with no orphan edges or points, is examined later in the project.

By convention, when a couplet is added to a growing lattice, the new edge connects to a previously-existing point, and the new point becomes the partner of the new edge. The angular position at which the new edge connects to the existing point is part of the lattice's geometry — addressed next.

## §5. Connection geometry

A point can have multiple edges connecting to it — at distinct angular positions if the point is part of a dial (§9), or all at the same location if the point stands alone. For lattice construction at the working scale, the angular positions are part of the lattice's geometry.

Two cases concern this project:

- **1D linear array.** Each new couplet connects at φ_attach = π — 180° from the previously-existing partner edge — producing a chain that alternates point and edge along a single axis, joined head-to-tail. This is the canonical 1D arrangement in [viz/grid-lab](../../viz/grid-lab.md).

- **2D hex sheet.** Each new couplet connects at φ_attach = +2π/3 or −2π/3 — 120° or 240° from the partner edge. The result is a hexagonal sheet built by recursive splits, with each lattice vertex hosting up to three connections at the three vertices of an equilateral triangle.

The 2D split rule is the construction principle examined for couplet tiling in the project's later analyses. It is named here so that §9's introduction of the dial can be stated against a concrete connection geometry.

A 1D array may be **periodic** (the trailing edge's head connects back to point 0, closing the chain into a loop) or **open** (the trailing edge has no head and is treated as an inert stub for unit-cell symmetry). The two cases give different behavior under the update rule and are kept distinct throughout the project.

## §6. The master clock

The model evolves under a **master clock** that alternates between two discrete phases, 0 and 1. The transitions between phases carry the dynamics:

- **Inhale** (the 1 → 0 transition): the *gather* phase. Points update — each gathers its new value from connected edges.
- **Exhale** (the 0 → 1 transition): the *assert* phase. Edges update — each integrates the new endpoint difference into its stored history.

The pairing of names — yin/yang, reflective/assertive, inhalative/exhalative — is suggestive rather than load-bearing. It marks the asymmetry: points gather, edges assert. The names are convention; the structural fact is that points and edges never update on the same transition.

This staggered scheme is the digital analog of a Yee-style finite-difference scheme, in which electric and magnetic fields are evaluated on alternating half-time-steps. The project does not derive that analogy here; it adopts the staggered structure and examines its consequences.

The clock can be operated as a manual half-step (a single inhale or exhale at a time, useful for tracing dynamics by hand) or as a continuous run (alternating phases at a settable speed, useful for observing wave propagation).

## §7. The update rule

For each clock phase, every primitive of the active type evaluates a local update rule. The rule looks only at the primitive's own current value, the values of its directly connected neighbors, and a settable per-edge coupling that is not yet activated in this project.

The project uses a single update rule, the Yee-style additive rule from [viz/grid-lab](../../viz/grid-lab.md). It is memory-bearing — both halves of the rule add to the primitive's current value rather than replacing it — and it supports stable, linear, propagating waves: two perturbations launched from opposite ends of a chain pass through each other without disrupting each other.

### Point on inhale

A point adds to its current phase the weighted sum of its connected edges:

> φ_point ← φ_point + (1/k) · Σᵢ eᵢ · cos(φ_attach,ᵢ)

where eᵢ is the value of the *i*-th connected edge and φ_attach,ᵢ is the angular location at which that edge connects — measured from the point's intrinsic angular zero, set by its partner edge (§4). For a stand-alone point with no dial structure, all attached edges connect at φ_attach = 0, and the rule reduces to a sum of edge values.

### Edge on exhale

An edge adds to its current value k times the tail-minus-head phase difference:

> e_edge ← e_edge + k · (φ_tail − φ_head)

The tail-minus-head sign convention follows from stability: the edge stores a flux pointing from high-phase tail to low-phase head, so a positive tail-minus-head difference increases the edge's value.

### Translation factor k

The factor k translates between the two value units — magnitudes (edges) and phases (points). It is the same in both halves of the rule. Its default value is 1; the analyses that follow treat it symbolically and pin it numerically only where the algebra forces a choice.

### Per-edge coupling

A second per-edge coupling factor is present in the state of every edge. In the present rule it is stubbed at 1 and not used. Later work in the project may activate it as a function of the bending angle between primitives at a junction; the present chapter notes its existence and leaves it inert.

## §8. The junction

A **junction** is the interface where one edge meets one point at one specific φ_attach. Every edge has two junctions — one at its tail and one at its head. Every point has as many junctions as edges connected to it.

Information flow at a junction is **rectified by the clock**. On inhale the junction transmits the edge's value (with the cos(φ_attach) weighting and 1/k scaling) into the point's update. On exhale it transmits the endpoint phases (with the k scaling and sign convention) into the edge's update. The two directions never operate simultaneously; the clock phase selects which way information flows.

This rectification is the sense in which the junction behaves like a *bidirectional diode* — a coupling element that conducts in one direction during one half of a cycle and in the other direction during the other half. The analogy is named here; it is not pursued further in this chapter.

The junction is a structural object, not just bookkeeping. The model contains three candidate "primary" objects — the point, the edge, and the junction — and the project does not commit in advance to whether the junction is itself more fundamental than its constituents.

## §9. The dial

A **dial** is an emergent compound node: a closed periodic loop of N (point, edge) couplets in a 2π wrap. The dial inherits spatial extent from the layout of its constituent points, and external edges connect to it at one of its constituent points — each at a distinct angular position on the dial's perimeter.

By project convention:

- A **1D dial** has N = 2 constituent points, with two external connection locations at angles 0 and π. Used at lattice vertices in 1D linear arrays.
- A **2D dial** has N = 3 constituent points (the hex-tiling default), with three external connection locations at angles 0, +2π/3, and −2π/3. Used at lattice vertices in 2D hexagonal sheets.
- A **3D dial** is out of project scope — higher coordination, with two angular degrees of freedom per connection (e.g., 4 connections in a tetrahedral / diamond lattice).

The dial's external behavior — what an outside observer sees through one of its constituent points — is a bounded phase plus a discrete winding-number label. This section names the dial and states this external behavior; the closure derivation that establishes the entropic-bounding mechanism (by which an open couplet chain's continuous unbounded cumulative magnitude is mapped, on closure, to a discrete winding sector and a bounded phase pattern) is taken up later in the project.

### Macro convention: node defaults to dial

At the lattice scale, every vertex where edges meet is a dial — a 1D dial in a 1D linear array, a 2D dial in a 2D hex sheet. The genus name **node** covers both points and dials, but at the macro lattice scale "node" without further qualification refers to a dial. Points surface explicitly only where the dial's internal construction is the topic.

A dial may be rendered visibly (with its constituent points explicit) or implicitly (treated as a single object); both are valid descriptions at different levels of detail. The dial's existence and its angular connection structure are real either way: edges connect to dials in a *spatially-aware* manner — the angle of connection on the dial's rim is part of the lattice's geometry.

## §10. The promotion ladder

The project organizes its chapters against a **wrap-promotion ladder** — a hierarchy of structures, each level obtained from the previous by a wrap (closure) operation, and each expected to support a recognizable physical phenomenon.

| Level | Structure | Wrap | Expected phenomenon |
|---|---|---|---|
| **L0** | Single point or single edge | none | Raw information |
| **L1** | Open 1D couplet chain | none (linear, unbounded) | Coherent traveling perturbation — "light"-analog |
| **L2** | Closed 1D couplet loop → 1D or 2D dial | 1D wrap | Bounded phase + winding number — KK-style mass-analog |
| **L3** | 2D dial sheet wrapped into a torus | 2D wrap | Charge — established in [grid/charge-emergence.md](../../grid/charge-emergence.md) |

L1 introduces extent and direction without closure. L2 closes a 1D couplet chain into a periodic loop — this is the entropic-bounding step that produces a dial. L3 closes a 2D sheet of dials into a torus, producing charge per the existing GRID derivation.

Each level may admit a **leakage** analog — a fraction of the wrapped structure that escapes the closure. Leakage at L3 is well-characterized: it is the mechanism by which a curved 2D dial sheet produces a Coulomb field visible in 3D ambient space. Whether L1 and L2 admit leakage analogs is an open question, conditional on whether the project's primitives have extent — see §11.

The ladder is not a result. It is the **expectation** the project works against. Whether each level cleanly delivers its expected phenomenon, and whether anything new appears between or beyond the listed levels, is determined by the analyses that follow.

## §11. Posits and discovery targets

The chapter is explicit about what is taken as given and what remains open.

### Posited

- **Three structural types.** Points (0D, single phase), edges (1D, integrated point-difference history), and dials (emergent closed-loop nodes) as defined in §2, §3, §9.
- **The clock.** Two phases alternate; points update on inhale, edges on exhale.
- **The update rule.** The Yee-style additive rule of §7 is taken as given from [viz/grid-lab](../../viz/grid-lab.md).
- **The couplet as candidate unit.** §4's posit — that larger structures are assembled from (edge, point) couplets — is taken forward into the rest of the project.
- **Point as 0D primitive.** The point is the foundational primitive at the working scale; edges are 1D relational objects between points; dials emerge from closed couplet loops. This stance replaces an earlier "edge/node primacy" framing — the point's role as primitive is now structural, not a discovery question.

### Discovery targets

- **Junction primacy.** Whether the junction (rather than the point or the edge) is itself a more fundamental object than its constituents remains open. The bidirectional-diode framing of §8 may extend into a literal characterization or remain only suggestive.
- **Thickness.** Whether the model commits to primitives having extent from sub-structure, and whether that commitment is consequential at the working scale, is unresolved. Two outcomes are live: primitives are *truly* 0D / 1D and infinitely thin, or primitives have thickness inherited from a fractal substructure that the working scale does not open but does feel.
- **Couplet tiling.** Whether the couplet always admits exact tiling of a 2D hex sheet — every edge in exactly one couplet's edge slot, every point in exactly one couplet's point slot — is open.
- **α and leakage in the ladder.** Where in L0–L3 leakage analogs appear, and whether α-type phenomena live at L2 or only at L3, is conditional on the thickness question and is examined alongside it.

## §12. Bridge to viz/grid-lab

The chapter has named points, edges, dials, the master clock, the inhale/exhale phases, the update rule, the translation factor k, the per-edge coupling stub, the junction, and the couplet. Each is one-to-one with the corresponding object in [viz/grid-lab](../../viz/grid-lab.md), with one exception: grid-lab specifies two update-rule versions (a v1 phase-replacement and a v2 Yee-style additive). This project uses the additive rule only; the replacement variant has no memory and is structurally inconsistent with the present chapter's edges-as-integrated-difference framing.

The model is *adopted*, not redefined. grid-lab is a working reference, not authoritative. As long as the analyses here remain consistent with grid-lab's specification, the two stay aligned; where the project produces a result that suggests a different choice, the result takes precedence and the visualizer is updated to match.

## §13. Closing

The model and its discovery targets are now stated. The chapter sequence is summarized in the project [README](README.md).
