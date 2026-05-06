# Chapter 1: Foundation

## §1. The chapter's job

This project sits parallel to [grid-primitive](../grid-primitive/), which collapsed the GRID lattice's internal structure into a single distributed object — a *cylinder primitive* carrying both magnitude (longitudinal stress) and phase (azimuthal direction) on one continuous body. That model is *analog-first*: continuous, mechanical, with state varying along a 1D extent and propagation by direct elasticity.

grid-couplet takes the opposite stance — *digital-first*. The lattice is built from two structural primitives — the **edge** (a 1D relational object) and the **node** (a junction where edges meet) — assembled into **couplets** (one edge plus one node) as the lattice-building unit. There are two species of node: the **point** (a 0D node, the bootstrap species we have to start with) and the **dial** (an emergent n-D node that arises when a couplet chain closes into a 2π loop).

The model in this stance is not new. [viz/grid-lab](../../viz/grid-lab.md) implements its dynamics. This chapter does not redefine that model. It states the model in the project's notation, separates which features are *posits* (taken as given) from which are *discovery targets* (questions the project examines), introduces the couplet as the lattice-building unit, and defines the wrap-promotion ladder that organizes the project's chapters.

grid-lab serves throughout as a working reference, not an authority. As long as the analyses here remain consistent with grid-lab's specification, the two stay aligned; where the project's chapters produce a result that suggests a different choice — a different sign convention, a different update-rule version, a different geometric default — the result takes precedence and the visualizer is updated to match.

## §2. The point

The simplest node — and the only node we have at the start, before any closure has produced a dial — is the **point**: a 0D node holding one piece of state, a real-valued φ ∈ ℝ. It has no spatial extent.

The genus name **node** covers any object that acts as a junction for edges. In this chapter, where the species matters the prose says "point" or "dial" explicitly; where only the genus matters it says "node." The point is the *bootstrap species* — what the model has before any structure has been built.

A deliberate choice: the point's value is not posited as bounded. The bounded-phase interpretation a dial exhibits is something that emerges later, from the closure operation that wraps a couplet chain into a dial (taken up in the project's closure derivation). At the primitive level, the point is just a value-holder; whether the value behaves like an unbounded magnitude or a bounded phase depends on what closes around it.

A point may have any number of edges connecting at it. The point's **connection rule** forces all edges meeting there to share their endpoint value with the point's value. The point itself stores nothing else — it is, structurally, the location at which a shared value is held and updated.

Geometrically, a point is rendered as a single location with no extent. Edges meeting at a point all converge to the same location.

A point gathers its new value on the inhale phase of the master clock (§6). Its update rule is given in §7.

## §3. The edge

The **edge** is a 1D relational object connecting two nodes. It has two structural ends — a **tail** and a **head** — that fix once it is placed in a lattice. Together these define its **polarity**: the direction from tail to head.

An edge's value is its **integrated history** of the differential between its endpoint values, accumulated over time as the clock advances. Concretely, on each exhale phase the edge's stored value increments by k · (φ_tail − φ_head), where φ_tail and φ_head are the values at the edge's two endpoints (set by the nodes there) and k is a translation factor introduced in §7.

The edge's value is therefore unbounded — it accumulates without periodic identification. Polarity is structural and fixed; the value is dynamic and can grow large.

The distinction between polarity and value matters. Polarity is direction-bearing: the edge always points from tail to head. The value is a real number, the running integral of the endpoint difference, sign-respecting. A negative value does not flip the edge's polarity; it indicates the integral has accumulated more from negative-difference epochs than from positive ones.

**Edge length is logical, not topological.** An edge's identity is its connectivity (which two nodes it joins) and its stored value. It is not a metric object; it has no length in the sense of a distance to be traversed. When the lattice is drawn, edges are rendered as line segments for visualization, but those drawn lengths are a layout convention rather than a structural property. Propagation speed is set by the clock cadence (§6), not by edge length.

Geometrically, a default edge sits along an axis with its tail at −x and its head at +x.

## §4. The couplet

A **couplet** is one (edge, node) pair — the project's lattice-building unit. At the foundational level the node in a couplet is a point; once dials emerge, a couplet at the lattice scale is (edge, dial). In both readings the structure is the same: an edge joined to a node it pairs with.

Picture an edge with one of its two endpoints distinguished as the couplet's *partner node*. The couplet packages a single propagation step: a magnitude carrier (the edge) joined to a value carrier (the node), with the connecting interface (the junction, §8) coupling them under the clock.

The couplet is **posited** as the candidate functional building block at the lattice scale: larger structures are assembled from couplets, with each new couplet contributing exactly one edge and one new node to the lattice. Whether this assembly tiles 2D sheets exactly, with no orphan edges or nodes, is examined later in the project.

By convention, when a couplet is added to a growing lattice, the new edge connects to a previously-existing node, and the new node becomes the partner of the new edge. The angular position at which the new edge connects to the existing node is part of the lattice's geometry — addressed next.

## §5. Connection geometry

A node can have multiple edges connecting to it — at distinct angular positions if the node has spatial extent (a dial — §9), or all at the same location if the node is a point. For lattice construction at the working scale, the angular positions are part of the lattice's geometry.

Two cases concern this project:

- **1D linear array.** Each new couplet connects at φ_attach = π — 180° from the previously-existing partner edge — producing a chain that alternates node and edge along a single axis, joined head-to-tail. This is the canonical 1D arrangement in [viz/grid-lab](../../viz/grid-lab.md).

- **2D hex sheet.** Each new couplet connects at φ_attach = +2π/3 or −2π/3 — 120° or 240° from the partner edge. The result is a hexagonal sheet built by recursive splits, with each lattice vertex hosting up to three connections at the three vertices of an equilateral triangle.

The 2D split rule is the construction principle examined for couplet tiling in the project's later analyses. It is named here so that §9's introduction of the dial can be stated against a concrete connection geometry.

A 1D array may be **periodic** (the trailing edge's head connects back to node 0, closing the chain into a loop) or **open** (the trailing edge has no head and is treated as an inert stub for unit-cell symmetry). The two cases give different behavior under the update rule and are kept distinct throughout the project.

## §6. The master clock

The model evolves under a **master clock** that alternates between two discrete phases, 0 and 1. The transitions between phases carry the dynamics:

- **Inhale** (the 1 → 0 transition): the *gather* phase. Nodes update — each gathers its new value from connected edges.
- **Exhale** (the 0 → 1 transition): the *assert* phase. Edges update — each integrates the new endpoint difference into its stored history.

The pairing of names — yin/yang, reflective/assertive, inhalative/exhalative — is suggestive rather than load-bearing. It marks the asymmetry: nodes gather, edges assert. The names are convention; the structural fact is that nodes and edges never update on the same transition.

This staggered scheme is the digital analog of a Yee-style finite-difference scheme, in which electric and magnetic fields are evaluated on alternating half-time-steps. The project does not derive that analogy here; it adopts the staggered structure and examines its consequences.

**Propagation speed is set by the clock, not by edge length.** One full clock cycle (an inhale followed by an exhale) advances a perturbation by one couplet — one edge plus one node — through the lattice. Coarsely, this is the lattice's signal speed *c*. Edge length is logical, not topological (§3); the clock cadence is what sets the metric. This is a direct contrast with [grid-primitive](../grid-primitive/), where the analog cylinder primitive's physical length L sets c via transit time τ = L/c.

The clock can be operated as a manual half-step (a single inhale or exhale at a time, useful for tracing dynamics by hand) or as a continuous run (alternating phases at a settable speed, useful for observing wave propagation).

## §7. The update rule

For each clock phase, every primitive of the active type evaluates a local update rule. The rule looks only at the primitive's own current value and the values of its directly connected neighbors.

The project uses a single update rule, the Yee-style additive rule from [viz/grid-lab](../../viz/grid-lab.md). It is memory-bearing — both halves of the rule add to the primitive's current value rather than replacing it — and it supports stable, linear, propagating waves: two perturbations launched from opposite ends of a chain pass through each other without disrupting each other.

The chapter uses **natural units** throughout: one unit of edge magnitude corresponds to one radian of node phase, with no scaling factor between them. This is a deliberate departure from grid-lab's translation factor k and per-edge coupling stub — both can be reintroduced if a downstream analysis requires them, but they would only obscure the structural arguments at this stage.

### Node on inhale

A node adds to its current value the weighted sum of its connected edges:

> φ_node ← φ_node + Σᵢ eᵢ · cos(φ_attach,ᵢ)

where eᵢ is the value of the *i*-th connected edge and φ_attach,ᵢ is the angular location at which that edge connects — measured from the node's intrinsic angular zero, set by its partner edge (§4). For a stand-alone point (a node with no dial structure around it), all attached edges connect at φ_attach = 0, and the rule reduces to a sum of edge values.

### Edge on exhale

An edge adds to its current value the tail-minus-head value difference:

> e_edge ← e_edge + (φ_tail − φ_head)

The tail-minus-head sign convention follows from stability: the edge stores a flux pointing from high-value tail to low-value head, so a positive tail-minus-head difference increases the edge's value.

## §8. The junction

A **junction** is the interface where one edge meets one node at one specific φ_attach. Every edge has two junctions — one at its tail and one at its head. Every node has as many junctions as edges connected to it.

Information flow at a junction is **rectified by the clock**. On inhale the junction transmits the edge's value (with the cos(φ_attach) weighting and 1/k scaling) into the node's update. On exhale it transmits the endpoint values (with the k scaling and sign convention) into the edge's update. The two directions never operate simultaneously; the clock phase selects which way information flows.

This rectification is the sense in which the junction behaves like a *bidirectional diode* — a coupling element that conducts in one direction during one half of a cycle and in the other direction during the other half. The analogy is named here; it is not pursued further in this chapter.

The junction is a structural object, not just bookkeeping. The model contains three candidate "primary" objects — the node, the edge, and the junction — and the project does not commit in advance to whether the junction is itself more fundamental than its constituents.

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

**No fractal recursion is required.** A dial's constituent points and edges are at the same structural level as every other point and edge in the lattice — there is no "smaller" scale inside a dial. The compact rendering of a dial (drawn as a small ring at a lattice vertex while connecting edges are drawn long) is a visualization convenience, not a structural fact. Edge length is logical (§3), so the contrast between "small dial-internal edge" and "long lattice-spanning edge" exists only in the drawing, not in the model. Nothing the project derives requires a sub-scale below points and edges.

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

- **Two primitives plus one emergent species.** Points (0D nodes — single value) and edges (1D — integrated history of node-difference) are the structural primitives. Dials are emergent (closed couplet loops), with the closure derivation establishing them as the lattice's working node.
- **No required sub-scale.** Points are 0D, edges are 1D — that is the structural floor. Edge length is logical, not topological; nothing inside points or edges is required by the model.
- **The clock.** Two phases alternate; nodes update on inhale, edges on exhale. Propagation speed *c* is set by the clock cadence (one couplet per cycle), not by edge length.
- **The update rule.** The Yee-style additive rule of §7 is taken as given from [viz/grid-lab](../../viz/grid-lab.md).
- **The couplet as candidate unit.** §4's posit — that larger structures are assembled from (edge, node) couplets, where the node is a point at the foundational level and a dial at the lattice level — is taken forward into the rest of the project.

### Discovery targets

- **Junction primacy.** Whether the junction (rather than the node or the edge) is itself a more fundamental object than its constituents remains open. The bidirectional-diode framing of §8 may extend into a literal characterization or remain only suggestive.
- **Thickness, conditionally.** The model itself does not require sub-structure. But whether the project's primitives have *effective* thickness in some derivations — for example, an emergent thickness from the L2 wrap that becomes the dimension across which the L3 wrap folds — is a separate modeling question, addressed when the α discussion arrives.
- **Couplet tiling.** Whether the couplet always admits exact tiling of a 2D hex sheet — every edge in exactly one couplet's edge slot, every node in exactly one couplet's node slot — is open.
- **α and the ladder.** Where in L0–L3 α-type phenomena appear: the second-order-wrap framing (α emerges when a wrap folds across a dimension that already has extent) is examined alongside the thickness question.

## §12. Bridge to viz/grid-lab

The chapter has named points, edges, nodes, dials, the master clock, the inhale/exhale phases, the update rule, the junction, and the couplet. Each is one-to-one with the corresponding object in [viz/grid-lab](../../viz/grid-lab.md), with two adjustments. First, grid-lab specifies two update-rule versions (a v1 phase-replacement and a v2 Yee-style additive); this project uses the additive rule only — the replacement variant has no memory and is structurally inconsistent with edges-as-integrated-difference. Second, this project uses natural units throughout, dropping grid-lab's translation factor k and per-edge coupling stub; if either becomes algebraically necessary it can be reintroduced at that point.

The model is *adopted*, not redefined. grid-lab is a working reference, not authoritative. As long as the analyses here remain consistent with grid-lab's specification, the two stay aligned; where the project produces a result that suggests a different choice, the result takes precedence and the visualizer is updated to match.

## §13. Closing

The model and its discovery targets are now stated. The chapter sequence is summarized in the project [README](README.md).
