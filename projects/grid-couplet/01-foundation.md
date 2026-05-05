# Chapter 1: Foundation

## §1. The chapter's job

This project sits parallel to [grid-primitive](../grid-primitive/), which collapsed the GRID lattice's internal structure into a single distributed object — a *cylinder primitive* carrying both magnitude (longitudinal stress) and phase (azimuthal direction) on one continuous body. That model is *analog-first*: continuous, mechanical, with state varying along a 1D extent and propagation by direct elasticity.

grid-couplet takes the opposite stance — *digital-first*. Two distinct primitives, edges and nodes, are kept as separate objects connected at junctions. Their evolution is governed by a master clock that alternates between two phases, with edges and nodes updating on opposite phases.

The model in this stance is not new. [viz/grid-lab](../../viz/grid-lab.md) already specifies it in detail — the geometric layout of edges and nodes, the two-phase clock, and two versions (v1 and v2) of the update rules. This chapter does not redefine that model. It states the model in the project's notation, separates which features are *posits* (taken as given) from which are *discovery targets* (questions the project examines), and introduces the couplet as the candidate functional unit and the promotion ladder as the project's organizing structure.

grid-lab serves throughout as a reference rather than an authority. Where the analyses that follow remain consistent with grid-lab's specification, the two stay aligned; where the chapters produce a result that suggests a different choice, the result takes precedence and grid-lab is updated to match.

## §2. The edge

The first primitive is the **edge**: a linear object that carries a single real-valued state.

An edge has two structural ends: a **tail** and a **head**. Together these define its **polarity** — a direction from tail to head — independent of any state the edge carries. Polarity is fixed once the edge is placed in a lattice; it is not a value that updates.

The edge's **value** is a real number, which may be positive, negative, or zero. It is unbounded — there is no periodic identification.

The distinction between polarity and value matters. Polarity is structural and direction-bearing: the edge always points from tail to head. The value is the magnitude (and sign) carried by the edge at the current clock step. A negative value does not flip the edge's polarity; it means a state of one sign in the tail-to-head direction.

Geometrically, a default edge sits along an axis with its tail at −x and its head at +x, matching the convention in [viz/grid-lab](../../viz/grid-lab.md). The edge is rendered as a segment with tail and head markers.

*Worked example.* Two edges side by side, both oriented tail-at-left / head-at-right. One has value +3, the other −3. The two edges have the **same polarity** (both pointing right) but **opposite values**. They are not mirror images of each other — they are two states of the same structural object.

## §3. The node

The second primitive is the **node**: a periodic object that carries a phase.

A node's value is a phase φ ∈ [0, 2π). The state is strictly periodic: 2π is identified with 0, and values fold back into the half-open interval. The bounded compact mode is the only interpretation used in this project; bounded compact directions are what produce the gravity scaling and the mass-analog already established at lower layers, and there is no need for an unbounded interpretation here.

Geometrically, a node is a circle in the lattice plane. Its phase is identified with a position around the circle's rim.

A node carries an **intrinsic zero** — the angular location at which φ = 0. The zero is fixed by a single designated **partner edge**: the angular location where that partner edge connects to the node's rim *is* the node's zero, by definition. Other edges that connect to the same node connect at non-zero angular offsets relative to the partner-edge connection point.

This is the sense in which a node is more than just a phase variable — it has structure. The zero is not a free choice; it is fixed by the partner-edge pairing. The pairing itself is formalized in §8 as the **couplet**.

## §4. Connecting edges and nodes

An edge connects to a node at a specific angular location on the node's rim. Call that location **φ_attach**: the angle, measured from the node's intrinsic zero, where the edge's tail or head meets the node.

A single node may be connected to one or more edges, each at a distinct φ_attach. The simplest case is a node with only its partner edge, which connects at φ_attach = 0 by definition.

When additional edges connect to the same node, their angular spacing depends on the lattice geometry being assembled:

- **1D linear array.** Each new couplet connects to the previous one at φ_attach = π — 180° around the node from the partner-edge connection. The result is a chain alternating edges and nodes along a single axis, joined head-to-tail. This is the canonical 1D arrangement in [viz/grid-lab](../../viz/grid-lab.md).

- **2D hex sheet.** Each new couplet connects at φ_attach = +2π/3 or −2π/3 (120° or 240° from the partner-edge connection). The result is a hexagonal sheet built by recursive splits — each node hosts up to three connections at the three vertices of an equilateral triangle on its rim.

The 2D split rule is the construction principle examined for couplet tiling later in the project. It is named here so that §8's posit (the couplet as functional unit) can be stated against a concrete connection geometry.

A 1D array may be **periodic** (the trailing edge's head connects back to node 0, closing the chain into a logical loop) or **open** (the trailing edge has no head node and is treated as an inert stub for unit-cell symmetry). The two cases give different behavior under the update rules and are kept distinct throughout the project.

## §5. The master clock

The model evolves under a **master clock** that alternates between two discrete phases, 0 and 1. The transitions between phases carry the dynamics:

- **Inhale** (the 1 → 0 transition): the *gather* phase. Nodes update, drawing information from their connected edges.
- **Exhale** (the 0 → 1 transition): the *assert* phase. Edges update, drawing information from their connected nodes.

The pairing of names — yin/yang, reflective/assertive, inhalative/exhalative — is suggestive rather than load-bearing. It marks the asymmetry: nodes gather, edges assert. The names are convention; the structural fact is that nodes and edges never update on the same transition.

This staggered scheme is the digital analog of a Yee-style finite-difference scheme, in which electric and magnetic fields are evaluated on alternating half-time-steps. The project does not derive that analogy here; it adopts the staggered structure and examines its consequences.

The clock can be operated in two modes:

- **Manual half-step** — a single inhale or exhale at a time, useful for tracing dynamics by hand.
- **Continuous run** — alternating phases at a settable speed, useful for observing wave propagation.

## §6. Update rules

For each clock phase, every primitive of the active type evaluates a local rule. The rule looks only at the primitive's own current value, the values of its directly connected neighbors, and a settable per-edge coupling that is not yet activated in this project.

The project carries two versions of the update rules from [viz/grid-lab](../../viz/grid-lab.md). They differ in whether the rule *replaces* or *adds to* the primitive's current value.

### v1 — phase-replacement

A node's next phase is set directly from its connected edges:

> φ_node ← (1/k) · Σᵢ eᵢ · cos(φ_attach,ᵢ)

where eᵢ is the value of the *i*-th connected edge, φ_attach,ᵢ is the angular location where that edge connects to the node, and k is a translation factor (see below).

An edge's next value is set directly from its two nodes:

> e_edge ← k · (φ_tail + φ_head)

with the sign convention as specified in grid-lab.

This version is dissipative — each update overwrites the previous state, and structure does not propagate cleanly. It is useful as a starting form for first-pass intuition.

### v2 — Yee-style additive

A node *adds* to its current phase the v1-style contribution:

> φ_node ← φ_node + (1/k) · Σᵢ eᵢ · cos(φ_attach,ᵢ)

An edge *adds* k times the tail-minus-head phase difference to its current value:

> e_edge ← e_edge + k · (φ_tail − φ_head)

The tail-minus-head sign convention follows from stability: the edge stores a flux pointing from high-phase tail to low-phase head, so a positive tail-minus-head difference increases the edge's value. (Derivation: grid-lab.)

This version supports stable, linear, propagating waves. Two perturbations launched from opposite ends of a chain pass through each other without disrupting each other.

### Translation factor k

The factor k translates between the two primitives' value units — magnitudes (edges) and phases (nodes). It is the same in both versions of the update rules. Its default value is 1; the analyses that follow treat it symbolically and pin it numerically only where the algebra forces a choice.

### Per-edge coupling

A second per-edge coupling factor is present in the state of every edge. In v1 and v2 it is stubbed at 1 and not used. Later work in the project may activate it as a function of the bending angle between primitives at a junction; the present chapter notes its existence and leaves it inert.

### Choice of version

Both versions are taken as given from grid-lab. Subsequent chapters select between them as the analysis dictates: v1 where conceptual simplicity matters, v2 where stable wave propagation is required.

## §7. The junction

A **junction** is the interface where one edge meets one node at one specific φ_attach. Every edge has two junctions — one at its tail end and one at its head end. Every node has as many junctions as edges connected to it.

Information flow at a junction is **rectified by the clock**. On inhale the junction transmits the edge's value (with the cos(φ_attach) weighting and 1/k scaling) into the node's update. On exhale it transmits the node's phase (with the k scaling and sign convention) into the edge's update. The two directions never operate simultaneously; the clock phase selects which way information flows.

This rectification is the sense in which the junction behaves like a *bidirectional diode* — a coupling element that conducts in one direction during one half of a cycle and in the other direction during the other half. The analogy is named here; it is not pursued further in this chapter.

The junction is a structural object, not just bookkeeping. The model contains three candidate "primary" objects — the edge, the node, and the junction — and the project does not commit in advance to which (if any) is foundational.

## §8. The couplet

A **couplet** is one (edge, node) pair together with the two junctions that connect them.

The couplet packages a complete propagation step. The edge holds a magnitude with directional polarity. The node holds a phase whose zero is fixed by this very edge (§3's partner edge is the couplet's edge). The junction couples them under the clock, with information flowing in alternating directions on alternating phases. One couplet alone is the smallest object that can carry both a magnitude and a phase under the model's dynamics — a single (edge, node) pair, not separate edges or nodes in isolation.

The couplet is **posited** as the candidate functional building block at the lattice scale: larger structures are to be assembled from couplets, with no orphan edges or orphan nodes appearing at any scale of the assembly. The 1D and 2D connection geometries of §4 are stated against this posit.

The posit names the candidate but does not commit to which of the couplet's three structural pieces (edge, node, or junction) is the foundational primitive. Three readings remain open:

- The **edge** is foundational; the node is an emergent structure (perhaps a wrapped chain of sub-edges) and the junction is the coupling between scales.
- The **node** is foundational; the edge is an emergent structure (perhaps a degenerate or unrolled node) and the junction is again a coupling.
- The **junction** is foundational; edge and node are two reductive views of what the junction couples, distinguished only by which side of the clock-rectified flow they sit on.

A fourth reading — that no single piece is foundational and the couplet itself is the irreducible object — remains live as long as none of the first three is settled.

## §9. The promotion ladder

The project organizes its chapters against a **wrap-promotion ladder** — a hierarchy of structures, each level obtained from the previous by a wrap operation, and each expected to support a recognizable physical phenomenon.

| Level | Structure | Wrap operation | Expected phenomenon |
|---|---|---|---|
| **L0** | Single edge or single node | none | Raw information |
| **L1** | Open 1D edge chain | none (linear, unbounded) | Coherent traveling perturbation — "light"-analog |
| **L2** | 1D edge chain closed by 2π wrap into a node | 1D wrap | KK-style mass-analog |
| **L3** | 2D hex sheet wrapped into a torus | 2D wrap | Charge — established in [grid/charge-emergence.md](../../grid/charge-emergence.md) |

Each level's wrap is a topological closure operation. L1 introduces extent and direction without closure. L2 closes a 1D chain into a periodic loop, producing a compact direction along which momentum is quantized — the same mechanism producing rest mass in [metric-mass](../metric-mass/) and substrate inertia in grid-primitive chapter 8. L3 closes a 2D sheet into a torus, producing charge per the existing GRID derivation.

Each level may admit a **leakage** analog — a fraction of the wrapped structure that escapes the closure. Leakage at L3 is well-characterized: it is the mechanism by which a curved 2D sheet produces a Coulomb field visible in 3D ambient space. Whether L1 and L2 admit leakage analogs is an open question, conditional on whether the model commits to primitives having extent — see §10.

The ladder is not a result. It is the **expectation** the project works against. Whether each level cleanly delivers its expected phenomenon, and whether anything new appears between or beyond the listed levels, is determined by the analyses that follow.

## §10. Posits and discovery targets

The chapter is explicit about what is taken as given and what remains open.

### Posited

- **The two primitives.** Edges and nodes exist as distinct digital objects with the values and structures of §2 and §3.
- **The clock.** Two phases alternate, with nodes updating on inhale and edges on exhale, per §5.
- **The update rules.** v1 and v2 from [viz/grid-lab](../../viz/grid-lab.md) are adopted as stated, per §6.
- **The couplet as candidate unit.** §8's posit — that larger structures are assembled from (edge, node) couplets — is taken forward into the rest of the project.

### Discovery targets

The following are *not* posited; each is examined in its own chapter as the project unfolds:

- **Edge/node primacy.** Whether edges and nodes are dual views of one underlying property, or genuinely asymmetric — with one as the foundational primitive and the other as emergent — is examined by attempting both constructions and comparing what fails. The brainstorm's hunch is asymmetry by an entropy argument: bounding loses information that decompactification cannot recover. The hunch is open.
- **Junction primacy.** Whether the junction (rather than the edge or node) is the actual foundational object remains open. The bidirectional-diode framing of §7 may extend into a literal characterization or remain only suggestive.
- **Thickness.** Whether the model commits to primitives having extent from sub-structure, and whether that commitment is consequential at the working scale, is unresolved. Two outcomes are live: primitives are *truly* infinitely thin, or primitives have thickness inherited from a fractal substructure that the working scale does not open but does feel.
- **Couplet tiling.** Whether the couplet always admits exact tiling of a 2D hex sheet — every edge in exactly one couplet's edge slot, every node in exactly one couplet's node slot — is the second blocking question.
- **α and leakage in the ladder.** Where in L0–L3 leakage analogs appear, and whether α-type phenomena live at L2 or only at L3, is conditional on the thickness question and is examined alongside it.

## §11. Bridge to viz/grid-lab

The chapter has named edges, nodes, junctions, the master clock, the inhale/exhale phases, the v1 and v2 update rules, the translation factor k, and the per-edge coupling stub. Each of these is one-to-one with the corresponding object in [viz/grid-lab](../../viz/grid-lab.md). The model is *adopted*, not redefined.

grid-lab is a working reference, not authoritative. As long as the analyses here remain consistent with grid-lab's specification, the two stay aligned. Where the project produces a result that suggests a different choice — a different sign convention, a different geometric default, a different update-rule version, a different treatment of the trailing edge — the result takes precedence and the visualizer is updated to match.

## §12. Closing

The model and its discovery targets are now stated. The chapter sequence is summarized in the project [README](README.md).
