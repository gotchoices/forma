# Chapter 9: Node decomposition

## §1. The chapter's job

Earlier chapters treated the node as a primitive: a coord-N vertex that applies the scattering matrix S = (2/N)·J − I to its N registers per inhale phase. This chapter does not propose to remove the node primitive from the substrate. It asks a constructive question instead: *can the node's functional behavior be built from edge primitives plus some additional rules and context that operate only inside the node's compound?*

The answer is yes, and the chapter shows how. Two concrete constructions are developed: a **star** with a single shared register at the junction (the cleanest implementation), and a **triangle** mesh of three inner edges with no shared register (more conceptually pure but mathematically heavier). Both produce the S-matrix at the outer terminals; both use only edge-level operations on the inside, with sub-tick scheduling within the inhale phase. The chapter ends with the structural conclusions about edge-vs-node primacy that follow from the construction.

The chapter does not change the substrate. The standard implementation (one node primitive, one S-matrix application per tick, [scripts/models.py](scripts/models.py)) is unchanged. What this chapter establishes is that *a functional equivalent of the node primitive can be constructed from edges-plus-context*, which settles the original [grid-couplet](../grid-couplet/) question about whether nodes and edges are independent primitives.

## §2. The bare edge

The minimal edge primitive carries the smallest possible state and the simplest possible operation:

- *State.* Two end-registers, each holding a single value.
- *Operation.* During the exhale phase, swap the two end-registers.

This is the entire bare edge. No parameters, no impedance, no transit-time variation, no awareness of other edges or junctions. When operating *outside* a compound, an edge does only this.

Inside a compound, the same edge primitive can be configured with additional rules — a sub-tick schedule and access to context registers — without changing what the bare edge fundamentally is. The richness lives in the compound's configuration, not in the edge itself.

## §3. What we mean by "compound model of a node"

A compound is a configuration of bare edges, possibly together with one or more context elements (shared registers, sub-tick scheduling, local rules), arranged so that *viewed from the outside, the compound's behavior is indistinguishable from a single node primitive applying S = (2/N)·J − I*.

The "view from outside" criterion is precise. Imagine wiring the compound into the rest of the lattice through N outer terminals (one per outer edge that connects to the compound). After one full clock tick — inhale plus exhale — the values at the N outer terminals must match what they would be if a single node primitive at coord N had applied S and then exhaled.

Two structural notes:

- The compound's *internal* state (extra registers, intermediate values during sub-ticks) is invisible from outside. The construction may use as much internal state as needed, as long as it does not leak out.
- The compound must complete its work within one inhale phase. No extra ticks of delay through the compound are allowed; from the outside, the compound's response is per-tick equivalent to a node primitive.

## §4. The star construction

The simplest construction. A central junction register V is added inside the compound, plus three inner connections (we will call them micro-edges) from V to the three outer-edge inner-end registers.

### §4.1 Geometry

```
                   outer terminal A
                          ●
                          │
                          │ outer edge A (bare)
                          │
                          ● s_A  ──┐
                                   │ inner micro-edge A
                                   │
                                  [V]  ← shared hub register (context)
                                   │
                          ┌── s_B ●│
                          │        ●─── s_C ────┐
                          │ inner  │            │
                          │ edge B │ inner edge C
                          │        │            │
                          │        │            │
                          ● s_B    ●            ● s_C
                          │                     │
                          │ outer edge B (bare) │ outer edge C (bare)
                          │                     │
                          ●                     ●
                   outer terminal B      outer terminal C
```

Three bare outer edges (A, B, C), each contributing two registers — an outer-terminal register and an inner-end register (s_A, s_B, s_C). One context register V at the hub. Three inner micro-edges, each connecting one s_i to V.

Total state inside the compound: 3 inner-end registers (s_A, s_B, s_C) + 1 hub register V = 4 registers. From outside, only the three outer-terminal registers are visible.

### §4.2 The inhale algorithm

The inhale phase is decomposed into three sub-ticks:

**Sub-tick 1 — gather.** Each inner micro-edge deposits its s_i value into V additively:

> V ← s_A + s_B + s_C.

After sub-tick 1, V holds the sum of the three inner-end registers. The s_i registers retain their original values.

**Sub-tick 2 — scale.** The hub register V is rescaled to the junction potential:

> V ← (2/N) · V = (2/3) · V.

After sub-tick 2, V holds the junction potential (2/3) · (s_A + s_B + s_C), which is what chapter 6 §2.5 called *V = 2 × the average of the inputs*.

**Sub-tick 3 — broadcast.** Each inner micro-edge writes back V − s_i to its inner-end register:

> s_A ← V − s_A,
> s_B ← V − s_B,
> s_C ← V − s_C.

After sub-tick 3, each inner-end register holds the S-matrix output for that channel.

### §4.3 Verification

By direct computation, after the three sub-ticks:

> s_A_new = V − s_A_old = (2/3)(s_A + s_B + s_C) − s_A = (−1/3)·s_A + (2/3)·s_B + (2/3)·s_C.

This is exactly row 1 of S = (2/3)·J − I applied to (s_A, s_B, s_C). Similarly for s_B and s_C. The compound implements the S-matrix exactly.

After the inhale phase ends, the standard exhale runs on the outer edges (each outer edge swaps its two end-registers as usual). The result at the outer terminals is identical to what a single coord-3 node primitive would have produced.

### §4.4 What primitives are used

Inside the compound:

- *Bare outer edges* — three of them, contributing s_A, s_B, s_C.
- *Inner micro-edges* — three of them, with two specific operations each (deposit additively in sub-tick 1, write-back in sub-tick 3). These are not "rich edges" with parameters; they are bare-edge-like elements running a fixed two-phase rule.
- *Hub register V* — one extra register, structurally a context element.
- *Sub-tick clock* — three sub-ticks within the inhale phase.

The compound is *one shared register V* + *three inner micro-edges with a fixed two-phase rule* + *sub-tick scheduling*. No per-edge parameters, no impedance, no per-edge angles.

## §5. The triangle construction

A more elegant construction in the sense of "edges only" (no shared central register) but mathematically heavier. Three inner micro-edges arranged as a triangle, each connecting two of the three outer-edge inner-end registers.

### §5.1 Geometry

```
                   outer terminal A
                          ●
                          │
                          │ outer edge A (bare)
                          │
                          ●  s_A
                         ╱ ╲
                        ╱   ╲
            inner      ╱     ╲     inner
            edge A-B  ╱       ╲    edge A-C
                     ╱         ╲
                    ╱           ╲
                   ●─────────────●
                  s_B    inner  s_C
                          edge B-C
                  │             │
                  │ outer       │ outer
                  │ edge B      │ edge C
                  │             │
                  ●             ●
            outer term B    outer term C
```

Three bare outer edges contributing s_A, s_B, s_C. Three inner micro-edges forming a triangle: A-B, B-C, A-C. No central register.

Total state inside the compound: 3 inner-end registers from the outer edges + 6 inner-end registers from the triangle micro-edges (each triangle edge has two ends, one at each pair of corners) = 9 registers, although we will see that the triangle micro-edges' end-registers coincide with the outer edges' inner-end registers in a specific way.

### §5.2 The Givens-rotation decomposition

Any orthogonal N×N matrix factors into a product of N(N−1)/2 Givens rotations, each acting on a pair of indices. For S = (2/3)·J − I (orthogonal because S² = I from chapter 6 §2), the decomposition has 3 rotations:

> S = G_{12}(θ_1) · G_{23}(θ_2) · G_{13}(θ_3)

where G_{ij}(θ) is the 2×2 rotation by angle θ acting on indices i and j (and the identity on the remaining index). Specific angles θ_1, θ_2, θ_3 can be solved analytically for the S-matrix.

### §5.3 The inhale algorithm

Each inner triangle micro-edge performs *one Givens rotation* on its pair of inner-end registers during one of three sub-ticks:

**Sub-tick 1.** Inner edge A-B applies G_{12}(θ_1) to (s_A, s_B). Both registers update.

**Sub-tick 2.** Inner edge B-C applies G_{23}(θ_2) to (s_B, s_C). Both registers update.

**Sub-tick 3.** Inner edge A-C applies G_{13}(θ_3) to (s_A, s_C). Both registers update.

### §5.4 Verification

After the three sub-ticks, the composite operation applied to (s_A, s_B, s_C) is G_{12}(θ_1) · G_{23}(θ_2) · G_{13}(θ_3) = S. The outer-terminal behavior matches a coord-3 node primitive.

### §5.5 Comparison with the star

The triangle is "edges only" in the sense that it has no shared register V — the only registers inside the compound are at the corners of the triangle, which are also the inner-end registers of the outer edges. The cost: each inner micro-edge has a *parameterised* operation (a specific Givens-rotation angle), not a single fixed two-phase rule. The triangle's micro-edges carry numerical parameters; the star's micro-edges have a uniform two-phase rule.

The star and triangle are both legitimate constructions. The star is simpler to specify (one fixed rule, one shared register) but uses an extra register. The triangle is more elegant (no extra register, only edge-pair operations) but requires three angle parameters that vary by edge.

The chapter's substantive observation: *which one is "more primitive" depends on what one prefers to count as the cost.* If extra registers are cheap and parameter variety is expensive, the star wins. If parameter variety is cheap and extra registers are expensive, the triangle wins. Both implement the S-matrix; both use only edge-level operations plus sub-tick scheduling.

## §6. Higher coord: tree decomposition

A coord-N node decomposes into a tree of (N − 2) coord-3 sub-junctions linked by internal connections. This is well-known in network theory; the calculation is the cascade of coord-3 reductions, with each internal connection's parameters chosen so the overall N-terminal behavior matches the original coord-N S-matrix.

For coord 4 (the relevant case for 3D diamond), the decomposition is one internal node linking two coord-3 sub-junctions:

```
              outer 1               outer 4
                 ●                     ●
                 │                     │
               s_1                   s_4
                  ╲                  ╱
                   ╲                ╱
                  [Y_a]──── int ──[Y_b]
                   ╱                ╲
                  ╱                  ╲
               s_2                   s_3
                 │                     │
                 ●                     ●
              outer 2               outer 3
```

Y_a and Y_b are coord-3 compounds (each implemented by the star or triangle from §4 or §5). The "int" register is the shared internal connection.

Higher coord-N reduces to N − 2 cascaded coord-3 sub-junctions in this manner. The construction terminates at coord-3 compounds, each of which is implemented by §4 or §5.

The chapter does not work out the parameters for coord ≥ 4 explicitly. The structural result is that any coord-N node has a functional model in terms of edge primitives plus context, with the model's complexity scaling linearly with N − 2.

## §7. The reverse direction: edges from nodes

The constructions of §4 and §5 give a functional model of the *node* in terms of edge primitives + context. The reverse direction — building an edge from nodes — does not work the same way.

The bare edge has *spatial extent*. Information at one end propagates to the other end during one exhale; this transit is what makes the edge a propagation medium. A node is a *meeting point*, not a propagation medium; it has no spatial extent.

A construction "build an edge from nodes" must produce spatial extent from non-extended primitives. The natural attempt — chain many small nodes together with internal edges of unit length — *uses edges in the construction*. The reduction terminates at smaller edges, not at pure nodes. Edges cannot be functionally reduced to nodes the way nodes can be functionally reduced to edges plus context.

This asymmetry is the chapter's substantive structural conclusion: *edges are the more fundamental of the two ingredients*. Nodes are derivable as compounds; edges are not. The original [grid-couplet](../grid-couplet/) question of whether nodes and edges are symmetric halves of one underlying primitive is answered: no, they are not symmetric, and the asymmetry favors the edge.

## §8. Connection to chapter 4 and chapter 5

### §8.1 Consistency with the chapter-4 transmission-line reframing

The constructions of §4 and §5 are consistent with — and in some sense suggested by — the chapter-4 reframing of Scattering as a transmission-line network. A real transmission-line network does not have a "node primitive" either; junctions are emergent meeting points where the line physics produces scattering through the geometry of the meeting. Our constructions inherit this structure: the outer edges carry information across the lattice; the compound at the junction (whether star or triangle) implements what the meeting demands.

The chapter does not claim that the substrate is *literally* a transmission-line network. It claims that the structural pattern is the same — bare propagation primitives connected by a configuration that produces the scattering — and that the chapter-4 reframing's success is consistent with that pattern.

### §8.2 Information content under the construction

Chapter 5 established that the substrate's information capacity is in its register state, with the holographic-window scaling M ≥ (amp_max/((N−1)·ε))² cells per macroscopic resolution. Under the §4 star construction, each compound adds one extra register V relative to the standard node primitive — a small addition to the substrate's total information count. Under the §5 triangle construction, no extra registers are added, but each inner micro-edge carries a parameter (the rotation angle), which is structural information rather than dynamic state.

Either way, the constructions do not change the substrate's *dynamic* information content (the per-tick evolving state) by more than a constant factor per junction. The bit-counting arguments of chapter 5 carry over with at most that constant adjustment.

## §9. Closing pointer

The functional behavior of a coord-N node primitive can be constructed from bare edges plus a small amount of additional context — either a shared junction register (the star construction of §4) or a triangle of parameter-bearing inner micro-edges (the triangle construction of §5). Both produce the S-matrix at the outer terminals; both use only edge-level operations plus sub-tick scheduling. Higher-coord nodes reduce to cascaded coord-3 sub-junctions.

The reverse direction — building an edge from nodes — does not work the same way: edges have spatial extent that nodes lack. Edges remain the more fundamental of the two structural ingredients.

This closes the substrate-structure portion of the project. The original [grid-couplet](../grid-couplet/) question about whether nodes and edges are symmetric primitives is settled: they are not symmetric; nodes have functional models in edge-and-context terms, while edges do not have the analogous reduction. The chapter does not propose to change the substrate's primitive set; it establishes that a functional equivalent of the node primitive exists in edge-and-context terms.

Chapter 10 (closing summary) consolidates the project's results.

The chapter sequence is summarized in the project [README](README.md).
