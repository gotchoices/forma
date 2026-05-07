# Chapter 9: Node decomposition — working outline

> **Status: working outline.** The chapter below is the section-by-section sketch produced during chapter-9 planning. The substantive claim has shifted from the original outline: the node is not a primitive, but it is *not* eliminated by impedance tricks or Y-Δ network reductions either. The cleanest reading is that the substrate has two structural ingredients of very different kinds — *bare edges* (the only dynamic primitive) and *connectivity* (static structural information) — and what we have been calling a "node" is the **compound** that emerges when N bare edges meet at a junction whose local connectivity says they meet there. The S-matrix is implicit in the compound's structure, not a rule that any primitive runs.

---

## §0. Working questions

These are the questions the chapter has identified. Most have provisional answers from the planning discussion; the chapter would develop them concretely.

### W1. What is a node, structurally?

The original [grid-couplet](../grid-couplet/) brainstorm asked whether nodes and edges are symmetric "couplet halves" of a single underlying primitive. The chapter's substantive answer: no — they are not symmetric, but neither is a node a primitive in the same sense as an edge. A node is a **compound**: what one gets when N bare edges meet at a junction, with the local connectivity making them coherent. The dynamic primitive is the bare edge; the structural primitive is the connectivity; the node is the compound of edges-meeting-under-connectivity.

### W2. Can the substrate be described with edges as the only primitive?

Provisional answer: yes, with one important qualifier. Bare edges are the only *dynamic* primitive. But the substrate also has a *structural* ingredient — the connectivity, which says how edges meet — and that ingredient is not made of edges. So "edges only" is true in the sense that nothing else evolves under the clock, false in the sense that connectivity is a separate kind of structural information.

### W3. Where does the S-matrix live?

Not in the bare edge (which only swaps its end-registers). Not in a separate node-as-primitive (which we have eliminated). It lives *implicitly* in the compound's structure — in the way N bare edges relate to each other through the junction's connectivity. The S-matrix is what the compound *is*, not what any primitive *does*.

### W4. Does the reverse direction work — can an edge be built from nodes?

Provisional answer: no, asymmetrically. Edges have spatial extent (transit time, end-to-end direction, propagation); nodes do not. A construction "build an edge from nodes" terminates at smaller edges, not at pure nodes. So edges are the more fundamental of the two structural ingredients.

---

## §1. The chapter's job

Identify the substrate's irreducible primitives. The original grid-couplet question was "are nodes and edges two halves of one underlying primitive?" The chapter's answer:

- Edges are the only *dynamic* primitive — the only thing whose state changes under the clock.
- Connectivity is a separate *structural* ingredient — fixed, not evolving — encoding which edges meet at which junctions.
- Nodes are not primitives. A node is the **compound** that emerges when N bare edges meet at a junction, plus the connectivity making them coherent. The compound's S-matrix behavior is implicit in its structure.

This is a cleaner answer than "build a node out of edges via Y-Δ" (which the original outline overstated) or "edges are richer because they carry impedance" (which conflated this substrate with EM transmission lines). The substrate is pure information; impedance and EM are higher-level emergent concepts. At the substrate level, the only dynamic primitive is the bare edge, and the only structural ingredient added is connectivity.

The chapter develops this substantively in §3–§5, then handles the asymmetry (§6) and the connection to chapter 4's transmission-line reframing (§7).

## §2. The bare edge

The minimal edge primitive:

- *State.* Two registers, one at each end. Each register holds a single value (real-valued in the chapter-4 model; bit-valued in the chapter-5 substrate-quantization reading).
- *Operation.* During the exhale phase of the clock, swap the two end-registers. That is the only thing the edge does.
- *No internal state beyond the two registers.* No parameters, no impedance, no transit-time variation, no awareness of other edges.

The bare edge is fully described by these properties. Anything richer is *not the edge*; it is some other structural element that the substrate also has.

## §3. Connectivity as a structural ingredient

The substrate has a second kind of ingredient — connectivity — that is structurally distinct from the edge. Specifically:

- Connectivity says *which edges meet at which junctions*. This is the lattice's wiring diagram.
- Connectivity is *static*: it is fixed when the lattice is constructed and does not change under the clock.
- Connectivity carries *no register state*: it is structural information, not dynamic information.

Connectivity is what distinguishes a 1D ring from a 2D hex from a 3D diamond, even though the bare-edge primitive is the same in all three. Two lattices with different connectivities have different dynamics, even if their edges are identical.

This is not a controversial claim — every chapter so far has implicitly used connectivity. What chapter 9 makes explicit is that connectivity is a *separate ingredient* from the bare edge, not a property of the edge itself. An edge does not "know" what it is connected to; the connectivity is information that lives outside the edge primitive.

## §4. The compound: what we have been calling a node

When N bare edges meet at a junction whose connectivity says they meet there, the result is a compound. The compound has:

- *N bare edges* contributing N pairs of end-registers — N of those registers are at the junction, N are at the far ends.
- *Connectivity* saying which N edges meet here, and how (e.g., in what local order).

The compound's behavior is derived from these two structural ingredients together. Specifically: when one inspects the compound's response to inputs at the N outer terminals, the behavior is exactly the S-matrix S = (2/N)·J − I from chapter 4. The S-matrix is not a rule that any primitive runs; it is *what the compound is*, structurally.

This is parallel to the situation in classical transmission-line theory: a Y-junction of three lines does not "compute" anything; the scattering at the junction is what voltage continuity + Kirchhoff's law require, given the geometry. The geometry is the analog of our substrate's connectivity. Our substrate's connectivity is, similarly, what makes the compound's behavior be what it is.

### §4.1 Why this is not "rich edges"

A previous draft of this chapter framed the reduction as "edges with impedance" (an EM-flavored move) or "edges with context-aware update rules" (a per-edge richness). Both are incorrect framings of what the substrate actually is.

In the correct framing, edges remain bare. The "richness" — the S-matrix's complexity, the multi-input averaging, the subtract-your-own subtraction — is a property of the *compound*, not of any bare edge. The compound is a structural pattern (N bare edges plus the connectivity that makes them meet); the pattern has the S-matrix behavior; no individual edge does.

### §4.2 Why this is not "computation at the node"

A different previous framing said "nodes compute the S-matrix via an active update rule." This is also not quite the right reading. The S-matrix at a coord-N compound is the *unique algebraic consequence* of the compound's structure (the two physical constraints — potential continuity and Kirchhoff's current law — admit exactly one solution at the compound's terminals). That solution is the S-matrix. Calling this "computation" overstates the agency of the compound; it is doing what its structure forces, not running a rule.

A discrete-clock implementation must *enforce* this structural fact tick by tick (continuous physics enforces it automatically), so in our simulation engine there is an explicit per-tick operation that applies S. But the operation is *deriving the structural consequence*, not *implementing an arbitrary rule*. The rule is what the compound's structure forces.

## §5. Where the S-matrix lives

To consolidate: the S-matrix is implicit in the structure formed by bare edges + connectivity. It does not live:

- *In any bare edge.* Bare edges only swap their two end-registers; pure swaps are permutations and cannot produce the S-matrix's non-permutation entries.
- *In any per-edge parameter.* No edge carries impedance, angle, delay, or other parameter that would let it execute a fragment of S on its own.
- *In a separate "node" primitive.* There is no node-as-primitive in this chapter's framing.

Where the S-matrix lives:

- *In the compound's structure.* When N bare edges meet under the connectivity that says they meet at a coord-N junction, the resulting compound's terminal behavior is exactly S. The matrix is what the structural pattern *is*.

This is the chapter's substantive structural claim. Eliminating "node as primitive" does not displace the S-matrix into edges or registers; it relocates it from "primitive's update rule" to "compound's structural identity."

## §6. The asymmetry: edges cannot be built from nodes

A short section establishing that the reduction is one-way.

### §6.1 Edges have spatial extent; nodes do not

The bare edge has two end-registers separated by an exhale's worth of "transit." That transit is what propagates information across the lattice. A node — under any reading — does not have this property; it is a meeting point, not a path between meeting points.

A construction "build an edge from nodes" must somehow produce spatial extent from non-extended primitives. The natural attempt — chain many nodes with internal edges — *uses edges* in the construction, terminating at smaller edges rather than at pure nodes. The reduction does not work in this direction.

### §6.2 The conclusion

Edges are the more fundamental of the two ingredients. Connectivity is the second structural ingredient. Nodes are derived compounds, not primitives. The original grid-couplet "node and edge are symmetric halves of one primitive" framing is not correct: they are not symmetric, and the asymmetry favours the edge.

## §7. Connection to the chapter-4 transmission-line reframing

The chapter's claim that the substrate has bare edges + connectivity, with nodes being derived compounds, is consistent with — and in some sense *required by* — the chapter-4 reframing of Scattering as a transmission-line network. A real transmission-line network does not have "node primitives" either; it has lines and the geometric points at which they meet. The S-matrix at any junction is what the line physics + the meeting geometry produce.

Our substrate inherits the same structure: bare edges in place of lines, connectivity in place of meeting geometry, compounds in place of physical junctions. The chapter-4 verdict — *Scattering is what a transmission-line network looks like on a graph* — is exactly what one would expect if the substrate's primitives are bare edges + connectivity, with the S-matrix being structural rather than algorithmic.

## §8. The information-content reading (chapter-5 connection)

Chapter 5 established that the substrate's information capacity scales with cell count. Under the bare-edges-plus-connectivity framing, the information content is precisely what bare edges' end-registers hold — that is, 2 × |edges| values total, with each register being one slot in the per-cell information budget.

Connectivity contributes *no per-tick information* to this count: it is structural, fixed, and does not evolve. The chapter-5 holographic-window argument (M ≥ (amp_max/((N−1)·ε))² cells per macroscopic resolution) implicitly counted edge-register state and not connectivity, because connectivity is not a state-bearing primitive.

This is consistent and worth stating: the substrate's bit-counting all happens in bare edges. Connectivity wires the edges together; it does not contribute to the substrate's information capacity.

## §9. Closing pointer

The substrate has two structural ingredients of different kinds: the bare edge (dynamic, with two end-registers and a swap operation) and the connectivity (static, encoding how edges meet). The node is not a primitive; it is the compound that emerges when N bare edges meet at a junction with the connectivity that says they meet there. The S-matrix is implicit in the compound's structural identity, not a rule that any primitive runs.

Edges are the more fundamental of the two ingredients (edges-from-nodes does not work the way nodes-from-edges does). The original grid-couplet "node and edge are symmetric primitives" question is settled: they are not symmetric; edges are primary; nodes are derived.

This closes the substrate-structure portion of the project. Chapter 10 (closing summary) consolidates the project's results.

The chapter sequence is summarized in the project [README](README.md).

---

## Appendix A: Notes for full chapter writing

- §3 (connectivity as a structural ingredient) is the chapter's key conceptual move. Develop carefully: connectivity is *not* a property of edges and *not* a per-vertex computational state; it is wiring information that lives at the lattice level. Some readers may want to call connectivity "the graph"; this is fine and worth saying explicitly.
- §4 (the compound) is the load-bearing structural claim. Make sharp the distinction between "the compound *runs* the S-matrix" (incorrect — implies agency) and "the compound *is* the S-matrix" (correct — structural identity). The §4.1 and §4.2 subsections defending against the "rich edges" and "computation at the node" misreadings are necessary.
- §5 (where the S-matrix lives) is a one-sentence punchline, but worth its own subsection so the reader can land on the answer cleanly.
- §6 (asymmetry) is short; the structural fact is that edges have transit and nodes don't. Belabouring it would dilute the punchline.
- §7 (transmission-line reframing) closes the loop with chapter 4. The substrate's structural framing is consistent with — and in fact necessitated by — calling Scattering a transmission-line-network model.
- §8 (information content) closes the loop with chapter 5. Edges hold all the dynamic information; connectivity is fixed wiring with no information-budget contribution.
- The chapter does *not* attempt to reimplement [scripts/models.py](scripts/models.py) in any "edges-only" form. The structural claim does not depend on the implementation; in fact, the standard implementation already locates the S-matrix at the node primitive, but that is a *coding* convenience, not a structural claim about the substrate.

## Appendix B: What was discarded from the prior outline

The prior outline (committed earlier) leaned on Y-Δ network reduction and impedance as edge structure. Both were over-stated:

- *Y-Δ doesn't actually eliminate coord-3 vertices in a periodic lattice.* It reorganises topology locally but increases coord at neighbouring vertices. The "all nodes vanish" reading I sketched does not survive contact with how Y-Δ actually works on a connected lattice. The current outline drops Y-Δ as the central reduction; the substantive reduction is "node is a compound," not "node is a Y-Δ-equivalent triangle."
- *Impedance was an EM flavour applied to a substrate that is pre-Maxwell.* At the substrate level there are no voltages, currents, or impedances; there are only register values and connectivity. The original outline conflated the chapter-4 transmission-line *analogy* with literal EM physics; this draft removes that confusion. (The chapter-4 reframing of Scattering as "transmission-line network" remains, but it is a structural analogy, not a claim that the substrate carries voltage and current at the per-edge level. See chapter 6 §2.5's "potential" framing.)
- The "edges with rich update rules" framing tried to put the S-matrix's computation at the edge level. That framing made edges richer than they need to be. The current outline keeps edges bare and locates the S-matrix in the compound's structural identity instead.

These changes simplify the chapter substantially. The substantive claim is now: *bare edges + connectivity = substrate; nodes are compounds, not primitives; the S-matrix is structural, not algorithmic.* Everything else is supporting development.
