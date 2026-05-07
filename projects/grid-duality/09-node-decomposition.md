# Chapter 9: Node decomposition

## §1. The chapter's job

Earlier chapters treated the node as a primitive: a coord-N vertex that applies the scattering matrix S = (2/N)·J − I to its N registers per inhale phase. This chapter does not propose to remove the node primitive from the substrate. It asks a constructive question: *can the node's functional behavior be built from edge primitives plus some additional rules and context that operate only inside the node's compound, without smuggling in a small computational element disguised as something else?*

The answer is yes, and the chapter shows how. The construction it leads with — a **triangle** mesh of three inner edges with no shared central state — passes a stringent honesty test: nowhere inside the compound is there a register or operation that does not already belong to the edges themselves. The "context" that lets the three edges produce the S-matrix is a self-consistency condition on the edges' parameters, not a central coordinator. A second, simpler construction (the **star** with a shared junction register) is sketched as a less honest alternative; it works mathematically but reintroduces a small node-like computational element inside the compound and is therefore not a genuine "edges-only" reduction.

The chapter does not change the substrate. The standard implementation in [scripts/models.py](scripts/models.py) keeps the node primitive intact for performance reasons. What this chapter establishes is *the structural fact that a functional equivalent of the node primitive exists in edge-and-context terms*, which settles the original grid-couplet question (see [couplet.md](couplet.md)) about whether nodes and edges are independent primitives.

## §2. The bare edge

The minimal edge primitive carries the smallest possible state and the simplest possible operation:

- *State.* Two end-registers, each holding a single value.
- *Operation.* During the exhale phase, swap the two end-registers.

This is the entire bare edge. No parameters, no impedance, no transit-time variation, no awareness of other edges or junctions. When operating *outside* a compound, an edge does only this.

Inside a compound, an edge can be configured with a sub-tick schedule and possibly a parameter (a rotation angle, in §4 below) that determines what it does during the inhale phase. These extras are edge-level; they do not require the existence of any other primitive type.

## §3. What we mean by "compound model of a node"

A compound is a configuration of bare edges, possibly together with sub-tick scheduling and per-edge parameters, arranged so that *viewed from the outside, the compound's behavior is indistinguishable from a single node primitive applying S = (2/N)·J − I*.

The "view from outside" criterion is precise. Imagine wiring the compound into the rest of the lattice through N outer terminals (one per outer edge that connects to the compound). After one full clock tick — inhale plus exhale — the values at the N outer terminals must match what they would be if a single node primitive at coord N had applied S and then exhaled.

Two structural notes:

- The compound's *internal* state (intermediate values during sub-ticks) is invisible from outside. The construction may use sub-tick computation as needed, as long as it does not leak out and as long as it is performed by edges, not by a central element.
- The compound must complete its work within one inhale phase. No extra ticks of delay through the compound are allowed; from outside, the compound's response is per-tick equivalent to a node primitive.

The honesty test for "edges + context" reductions: every register inside the compound must be the end-register of some edge (its own or a neighbouring outer edge), and every operation must act on a single edge's two end-registers. No register exists *only at the junction*; no operation reaches across more than one edge at a time. The §4 triangle construction passes this test; the §5 star construction does not.

## §4. The triangle construction

Three inner micro-edges arranged as a triangle, each connecting two of the three outer-edge inner-end registers. No central register; no central operation. The compound's behavior emerges from the three inner edges running their own rules in a coordinated sub-tick order, with parameters chosen for self-consistency.

### §4.1 Geometry

```
                outer terminal A
                       ●
                       │
                       │ outer edge A (bare)
                       │
                       ●  s_A
                      ╱ ╲
           inner     ╱   ╲    inner
           edge AB  ╱     ╲   edge AC
                  ╱       ╲
                 ╱         ╲
                ●───────────●
              s_B  inner   s_C
                   edge BC
                │           │
                │ outer     │ outer
                │ edge B    │ edge C
                │           │
                ●           ●
        outer terminal B   outer terminal C
```

Three bare outer edges contributing the inner-end registers s_A, s_B, s_C. Three inner micro-edges forming a triangle: edge AB connects s_A and s_B; edge BC connects s_B and s_C; edge AC connects s_A and s_C. *The three triangle edges have no end-registers of their own beyond what is already contributed by the outer edges.* Each inner edge "couples" two existing outer-edge end-registers; it does not add new state.

Total state inside the compound: three registers (s_A, s_B, s_C), all of which are end-registers of the outer bare edges. Zero registers are added by the inner mesh. Zero registers exist *only* at the junction.

### §4.2 The Givens-rotation decomposition

Any orthogonal N × N matrix factors into a product of at most N(N − 1)/2 Givens rotations, each acting on a pair of indices. For the coord-3 scattering matrix S = (2/3)·J − I, which is orthogonal because S² = I (chapter 6 §2.1), the decomposition has 3 rotations:

<!-- S = G_AC(θ_3) · G_BC(θ_2) · G_AB(θ_1) -->
$$
S \;=\; G_{AC}(\theta_3) \cdot G_{BC}(\theta_2) \cdot G_{AB}(\theta_1)
$$

where G_ij(θ) is the 2 × 2 rotation by angle θ acting on the pair of indices (i, j) (and the identity on the remaining index). The angles θ_1, θ_2, θ_3 are determined by the requirement that the composition equals S, and they can be solved analytically. (Standard Euler-angle decomposition: S is a 180° rotation around the all-ones axis (1, 1, 1)/√3 — the eigenvalues are 1, −1, −1 with the +1 eigenvector along (1, 1, 1) — and any 3-D rotation has a Givens / Euler decomposition.)

### §4.3 The inhale algorithm

Each inner triangle edge performs *one* Givens rotation on its pair of end-registers during one of three sub-ticks:

**Sub-tick 1** — inner edge AB applies G_AB(θ_1) to (s_A, s_B). Both registers update; s_C is untouched.

**Sub-tick 2** — inner edge BC applies G_BC(θ_2) to (s_B, s_C). Both registers update; s_A is untouched.

**Sub-tick 3** — inner edge AC applies G_AC(θ_3) to (s_A, s_C). Both registers update; s_B is untouched.

After the three sub-ticks, the composite operation applied to (s_A, s_B, s_C) is G_AC(θ_3) · G_BC(θ_2) · G_AB(θ_1) = S. The compound has implemented the S-matrix on its three inner-end registers. The outer terminals (after the standard exhale on the outer edges) now carry exactly what a coord-3 node primitive would have produced.

### §4.4 The honesty of this construction

What makes this construction faithful to "edges plus context, no smuggled-in nodes":

- *Each operation acts on one inner edge's two end-registers.* No edge reads or writes a third register; no operation involves more than two values at a time.
- *No state exists inside the compound that does not belong to an edge.* Every register the compound uses is the end-register of an outer edge.
- *No central coordinator runs at runtime.* Each inner edge knows only its own rotation angle and runs its rotation when its sub-tick fires. No edge tells the others what to do; no scheduler outside the edges resolves their interactions.

The "context" — what makes the compound coherent — is the *off-line agreement* on the three rotation angles θ_1, θ_2, θ_3. These angles are chosen at compound-construction time so that the composition equals S. At runtime each edge runs its angle independently. There is no central element imposing anything; the angles fit together because they were designed to fit together. *Coordination via consistent parameters, not via a coordinator.* This is closer to how a distributed system without a hub actually works: each component has a fixed rule, the rules were chosen so the global behaviour is what is required, and at runtime nothing centralised happens.

The absence of a central register or central operation is the chapter's structural answer to the user's intuition that "context" should not secretly be a node. In the triangle construction, it isn't.

## §5. The star construction (a less honest alternative)

For completeness, a simpler construction exists with one major caveat. It uses one shared junction register V plus three inner micro-edges arranged as a star with V at the centre. It is mathematically simpler than the triangle but smuggles a small node-like element back in.

### §5.1 Geometry

```
              outer terminal A
                     ●
                     │
                     │ outer edge A (bare)
                     │
                     ●  s_A
                      \
                       \  inner micro-edge A
                        \
                        [V]   ← shared junction register
                       / \
                      /   \
              inner  /     \  inner
              edge B/       \edge C
                   /         \
                  ●           ●
                 s_B          s_C
                  │           │
                  │ outer     │ outer
                  │ edge B    │ edge C
                  │           │
                  ●           ●
         outer terminal B   outer terminal C
```

A central register V is added inside the compound. Three inner micro-edges connect V to the three outer-edge inner-end registers (s_A, s_B, s_C). The compound has *four* registers internally: s_A, s_B, s_C, and V.

### §5.2 The inhale algorithm

The inhale runs in three sub-ticks:

- *Sub-tick 1 (gather).* Each inner micro-edge deposits its s_i value into V additively: V ← s_A + s_B + s_C.
- *Sub-tick 2 (scale).* The hub register V is rescaled to the junction potential: V ← (2/N) · V.
- *Sub-tick 3 (broadcast).* Each inner micro-edge writes V − s_i back to its s_i register.

By direct computation, after the three sub-ticks: s_A_new = (2/3)(s_A + s_B + s_C) − s_A, which is row 1 of S applied to (s_A, s_B, s_C). Similarly for s_B and s_C. The compound implements the S-matrix exactly.

### §5.3 Why this construction is less honest

The shared register V fails the §3 honesty test. It is a register that exists *only inside the compound* and *only at the junction* — it is not the end-register of any edge. It has its own update rule (it is summed into during sub-tick 1, scaled in sub-tick 2, and read in sub-tick 3). It coordinates the three inner micro-edges by being the common point all three of them write into and read from.

This is functionally what a node does: hold a single shared piece of state, mediate the interactions of multiple edges through itself, run its own local computation. The star construction has *replaced one coord-3 node primitive with a coord-3 compound that contains a coord-3 sub-node*, which is not a reduction. It is a renaming: V plays the part the node played, just in smaller letters.

The triangle construction does not have this defect. It has no register that exists only at the junction; it has no operation that reads or writes more than one edge's two end-registers at a time. Each inner edge runs entirely on its own pair. The triangle is a genuine "edges + parameter context" reduction; the star is a "edges + tiny node" arrangement.

### §5.4 When the star might still be worth keeping

For implementation purposes, the star is simpler: one fixed two-phase rule per inner edge (deposit, write-back), one extra register, no parameter to tune. The triangle requires three rotation angles whose values must be solved analytically and stored. If one is implementing the substrate in a programming language and does not care about the structural reduction question, the star is more pragmatic.

But for the chapter's structural question — *can a node's functional behaviour be built without secretly using a node?* — only the triangle gives a positive answer. The star answers a different question: *can the node's functional behaviour be implemented compactly?* (Yes, but only by re-locating it.)

## §6. Higher coord: tree decomposition

A coord-N node decomposes into a tree of (N − 2) coord-3 sub-junctions linked by internal connections. Each coord-3 sub-junction can in turn be implemented by the triangle construction of §4. The cascade of triangles produces a coord-N compound made entirely of inner edges with parameter-bearing Givens rotations and outer edges as terminals.

For coord 4 (the relevant case for 3D diamond), the decomposition is two coord-3 sub-junctions linked by one internal connection:

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

Y_a and Y_b are coord-3 compounds (each implemented by the §4 triangle construction). The "int" is an internal connection: a register that lives between the two triangles, *and is itself the end-register of an inner edge connecting them*. So even in the cascade, no register exists outside an edge.

Higher coord-N reduces to N − 2 cascaded coord-3 sub-junctions in this way. The construction terminates at coord-3 compounds, each implemented by the triangle. The chapter does not work out the parameters for coord ≥ 4 explicitly. The structural result is that any coord-N node has a triangle-based functional model in terms of edge primitives plus parameter context, with the model's complexity scaling linearly in N − 2.

## §7. The reverse direction: edges from nodes

The triangle construction gives a functional model of the *node* in terms of bare edges plus parameter context. The reverse direction — building an edge from nodes — does not work the same way.

The bare edge has *spatial extent*. Information at one end propagates to the other end during one exhale; this transit is what makes the edge a propagation medium. A node is a *meeting point*, not a propagation medium; it has no spatial extent.

A construction "build an edge from nodes" must produce spatial extent from non-extended primitives. The natural attempt — chain many small nodes together with internal connections of unit length — *uses edges in the construction*. The reduction terminates at smaller edges, not at pure nodes. Edges cannot be functionally reduced to nodes the way nodes can be functionally reduced to edges plus parameter context.

This asymmetry is the chapter's substantive structural conclusion: *edges are the more fundamental of the two ingredients*. Nodes are derivable as compounds; edges are not. The original grid-couplet question (see [couplet.md](couplet.md)) of whether nodes and edges are symmetric halves of one underlying primitive is answered: no, they are not symmetric, and the asymmetry favours the edge.

## §8. Connection to chapter 4 and chapter 5

### §8.1 Consistency with the chapter-4 transmission-line reframing

The triangle construction is consistent with the chapter-4 reframing of Scattering as a transmission-line network. A real transmission-line network does not have a "node primitive" either; junctions are emergent meeting points where the line physics produces scattering through the geometry of the meeting. Our triangle construction inherits this structure: the outer edges carry information across the lattice; the three inner edges plus their pre-agreed angles produce what the geometry of meeting demands.

The chapter does not claim that the substrate is *literally* a transmission-line network. It claims that the structural pattern is the same — bare propagation primitives connected by a configuration whose mutual self-consistency produces the scattering — and that the chapter-4 reframing's success is consistent with that pattern.

### §8.2 Information content under the construction

Chapter 5 established that the substrate's information capacity is in its register state, with the holographic-window scaling M ≥ (amp_max/((N − 1)·ε))² cells per macroscopic resolution. Under the §4 triangle construction, *no extra registers are added* per junction (the inner edges share the outer edges' inner-end registers as their endpoints). The substrate's per-tick information count is exactly the same as the standard node-primitive implementation.

What the triangle adds is *parameter information*: each inner edge carries a rotation angle. Parameter information is structural rather than dynamical (it does not evolve under the clock), so it does not contribute to the substrate's per-tick bit count. The bit-counting arguments of chapter 5 carry over without modification.

The §5 star construction *does* add a register V per junction, increasing the substrate's per-tick state by one register per junction. This is another reason to prefer the triangle: it preserves chapter 5's bit-counting exactly, while the star inflates it.

## §9. Closing pointer

The functional behaviour of a coord-N node primitive can be constructed from bare edges plus parameter context — a triangle of inner micro-edges performing Givens rotations whose angles are jointly chosen to compose to S. The construction adds no central register and no central operation; coordination among the inner edges is achieved through self-consistent parameters fixed at compound-construction time, not through a runtime coordinator. This is the genuine "edges + context" reduction.

The simpler star construction, with a shared junction register V, also implements S but does so by reintroducing a small node-like element inside the compound; it is not faithful to the structural question.

The reverse direction — building an edge from nodes — does not work the same way: edges have spatial extent that nodes lack. Edges remain the more fundamental of the two structural ingredients.

This closes the substrate-structure portion of the project. The original grid-couplet question (see [couplet.md](couplet.md)) about whether nodes and edges are symmetric primitives is settled: they are not symmetric; nodes have functional models in edge-and-parameter-context terms, while edges do not have the analogous reduction.

Chapter 10 (closing summary) consolidates the project's results.

The chapter sequence is summarized in the project [README](README.md).
