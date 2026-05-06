# Chapter 2: Closure and Bounding — the Entropic Origin of the Dial

## §1. The chapter's job

Chapter 1 introduced the dial as the macroscopic node at the lattice scale: a closed periodic loop of N (point, edge) couplets in a 2π wrap. The introduction stated the dial's external behavior — bounded phase plus a discrete winding number — without deriving where that behavior comes from. This chapter carries out the derivation.
<!--EC I don't want "v2" terminology imported from grid-lab.  This project should just have its "update rules" period.  In general I don't want to import anything in particular from grid-lab.  This project should stand on its own.  -->
The argument is structural. Starting from the v2 update rule (chapter 1 §7) applied to two configurations of N couplets — an open 1D chain and a closed 1D loop — show how each presents itself to an external observer, and identify the asymmetry that distinguishes them. The result is the **entropic-bounding** mechanism: closing a couplet chain into a 2π loop maps the chain's continuous unbounded cumulative magnitude into a discrete integer winding number, leaving a bounded phase pattern as the externally-visible state. The continuous information channel narrows to a discrete topological label, and the point pattern (mod 2π) becomes the dominant continuous-information channel.

The chapter resolves what was originally framed as a discovery target — whether edges or dials are the more fundamental object — by deriving, rather than positing, that the asymmetry is *topological* (open vs. closed) rather than *primitive* (one type vs. the other). Points and edges are the structural primitives; dials are emergent under closure. The brainstorm's hunch that "bounding has entropy, unbounding does not" is made precise here.

## §2. The two configurations
<!--EC Can we make some figures for this section? -->
Both configurations consist of N couplets — N nodes (points) and N edges — connected sequentially. They differ only in topology.

**Open 1D couplet chain.** N points with values φ_0, φ_1, …, φ_{N−1} in ℝ; N edges, with the trailing edge (e_{N−1}) an inert stub per chapter 1 §5. The chain's two endpoints (point 0 and point N−1) are exposed: external partners may attach at either end.

**Closed 1D couplet loop.** N points with periodic identification φ_N ≡ φ_0; N edges, all active. The trailing edge (e_{N−1}) connects point N−1 back to point 0, closing the loop.

Both configurations evolve under the v2 update rule of chapter 1 §7. In both, the natural choice of initial conditions for a freshly-built structure is e_i(0) = 0 — the edges have no prior history to remember.

In both configurations, internal edges meet at points. The point's connection rule (chapter 1 §2) forces all edges meeting at a point to share their endpoint value with the point's value: there is *no* phase difference at the joining locations. The phase difference between an edge's tail and its head is *along the edge's length*, between two distinct points; not at the points themselves.

## §3. Edges as integrated histories of point differences

The v2 rule for an edge (chapter 1 §7) gives:

> e_edge(t+1) = e_edge(t) + (φ_tail(t+1) − φ_head(t+1))

Iterating from time 0 to t:

> e_i(t) = e_i(0) + Σ_{s=1}^{t} (φ_tail,i(s) − φ_head,i(s))

For a freshly-built structure with e_i(0) = 0:

> e_i(t) = Σ_{s=1}^{t} (φ_tail,i(s) − φ_head,i(s))

Each edge's value at time t is *fully determined by the history of its endpoint nodes*. Edges are not independent state variables in the usual sense — they are integrated records of what the points have been doing.

This is true in both topologies. The difference between open and closed configurations does not lie in *whether* edges record point histories — they always do — but in what *macroscopic* information that record encodes.

## §4. The open chain — emergent edge

An open 1D chain of N couplets, viewed externally through its two endpoints, presents one macroscopic observable: the **cumulative endpoint difference**

> Δ_chain(t) ≡ φ_{N−1}(t) − φ_0(t) = Σ_{i=0}^{N−2} (φ_{i+1}(t) − φ_i(t))

External partners pinning the two endpoints set Δ_chain to whatever value they impose. The intermediate point phases are slaved to the dynamics; the only externally-controllable observable is the end-to-end difference.

Δ_chain is a continuous real number, unbounded. It can take any value the partners' choice imposes, with no closure constraint forcing it into a particular range. Over time, if the endpoint values change, Δ_chain tracks them — the chain's emergent variable evolves continuously.

The chain therefore *carries* a continuous unbounded magnitude. Externally, it behaves like a single primitive edge: an object that holds a real-valued integrated difference between its two attachment points. This is the **emergent edge** — a coarse-grained edge constructed from a chain of finer (edge, point) couplets.
<!--EC Do we _need_ an emergent edge?  Or is it just a novelty (functionally equivalent to a native edge)?  Thoughts? -->

## §5. The closed loop — closure and the winding number

A closed 1D loop of N couplets has no exposed endpoints; the loop's topology identifies point N with point 0. The cumulative-around-the-loop expression is:

> Δ_loop(t) ≡ Σ_{i=0}^{N−1} (φ_{i+1}(t) − φ_i(t))

with the periodic identification φ_N(t) ≡ φ_0(t).

Read literally — point values as unrestricted reals, summed without modular arithmetic — the sum telescopes and Δ_loop is identically zero. That reading throws away the structure the closed-loop topology provides.

The natural reading instead interprets phases as living on the circle S¹ — i.e., mod 2π — once the topology is closed. Each individual difference (φ_{i+1} − φ_i) is then read in the principal branch (−π, π], giving each term a bounded value in [−π, π]. The sum, summed once around the loop, must equal an integer multiple of 2π:

> Δ_loop = 2π · k for some integer k

This integer k is the **winding number**: the number of complete 2π revolutions the phase makes as one traverses the loop once. Different values of k label topologically distinct configurations.

The bounded-phase interpretation a dial exhibits emerges from this reading. The point's value, originally an unbounded real (chapter 1 §2), becomes a bounded phase mod 2π *because* the closure imposes a topological context in which the mod 2π reading is the natural one. This is the sense in which the bounded-phase character is derived from closure rather than posited at the primitive level.

The crucial structural feature: Δ_loop is *discrete* — an integer multiple of 2π. The closure operation has *quantized* what was continuous in the open chain. There is no continuous unbounded macroscopic observable on a closed loop.

The winding number is conserved under v2 dynamics for sufficiently small perturbations — those that do not push any individual difference (φ_{i+1} − φ_i) across the principal-branch boundary at ±π. Topology-changing perturbations large enough to cross the boundary can shift k by ±1; this corresponds to an actual phase slip, distinguishable from continuous evolution.

## §6. The dial's external view

The closed loop's residual configurational state — after the closure interpretation is applied — consists of N point phases mod 2π (a torus T^N, or T^{N−1} after gauge-fixing an overall phase reference) plus the integer winding label k.

An external edge connecting to one of the loop's points — say point 0 — sees that point's phase, modulo 2π. The phase is bounded. The winding number is a separate topological label that an external observer detects through global coherence properties: by tracing the full loop, or by observing how the loop responds to external perturbations that attempt to change its winding.

The loop's externally-visible state has two parts:

- A **bounded phase** at the connecting point.
- A **discrete winding sector** k.

This is the **emergent dial**: a bounded-phase external object with a discrete topological invariant. The bounded phase is the "what the dial is currently doing" observable; the winding number is "what topological sector the dial is in." Larger N values give finer discretizations of the dial's perimeter (more constituent points, hence more attach locations available for external edges); the bounded-phase character does not depend on N.
<!--EC Is it true then, that any winding information, if it were present, is invisible from the outside (where we can only connect at poits)? 

Will phase evolve around the loop as the clock ticks?  Or do we expect the circuit to find a steady state?  Do we answer this question in the narrative.  Seems like a good answer would be: That at a resonance, we will see a steady state, but in every other case, phase may have a velocity around the loop.  Presumably this will come into play in other models if/when we analyze alpha leakage is residual eddy currents.
-->
## §7. The information-capacity asymmetry

A side-by-side comparison of capacities makes the closure's effect explicit.

**Open chain.** N point values, each unbounded ℝ. Macroscopic observable Δ_chain — continuous unbounded ℝ. Edge values are determined by point histories (§3) and carry no independent capacity beyond the points' history. Total continuous-information capacity: unbounded — limited only by what the external partners can impose.

**Closed loop.** N point phases, each bounded in [0, 2π) once the closure interpretation is in place. Per-phase capacity log₂(2π/Δφ) for some fine-grained discretization Δφ; total ~ N · log₂(2π/Δφ). Macroscopic observable Δ_loop — discrete integer winding number with practically bounded range (set by the model's regime).

The "loss" in closure: the cumulative continuous unbounded variable Δ_chain becomes a discrete bounded integer Δ_loop / 2π = k. In the precise Shannon sense, a real-valued unbounded variable has unbounded information capacity; an integer with bounded range has finite capacity. The continuous information channel collapses to a discrete one.

This is the **entropy of bounding** made precise: the closure operation discards continuous degrees of freedom into a discrete topological invariant. The brainstorm's hunch that "bounding loses information that decompactification cannot recover" is this collapse, expressed structurally.

## §8. Edges become bookkeeping in the closed loop

Closure also has a specific consequence for the relationship between edges and points within a closed loop.

In an open chain, the edges' macroscopic sum Σ e_i is *unbounded* — it grows linearly with time when the endpoint partners impose a non-zero Δ_chain. The edges carry the magnitude that the chain's emergent edge presents.

In a closed loop, the edges' macroscopic sum is constrained by the closure:

> Σ_i e_i(t) = Σ_i Σ_s (φ_i(s) − φ_{i+1}(s)) = Σ_s [Σ_i (φ_i(s) − φ_{i+1}(s))] = Σ_s [2π · k(s)]

If the winding number is constant in time (a topologically protected sector), Σ_i e_i grows linearly as 2π · k · t, but the *information* in this growth is just the integer k — already a discrete quantity. The cumulative magnitude stored across all edges is just a multiple of 2π · k; nothing continuous accumulates.

The continuous information that an *open* chain stored in its edges (the unbounded cumulative magnitude) is absent in a closed loop. What remains is:

- The point phase pattern (mod 2π) — continuous, bounded.
- The winding number — discrete.

Both are *recoverable from the points alone*. The point phases give the phase pattern directly, and the winding number is a topological property of the point-phase sequence around the loop. The edges' internal values, while not strictly redundant during transients (they store the integrated history that drives the dynamics), do not carry any externally-visible macroscopic information beyond what the points already encode.

In a closed loop, the focus shifts from edges to points. Edges remain as bookkeeping channels that record the integrated history and thereby drive the dynamics, but they cease to be a continuous-information channel for external observers. The macroscopic dial is fully characterized by its point phases (mod 2π) and its winding number.

## §9. Why the inverse fails

Constructing an open couplet chain (continuous unbounded magnitude) from a closed dial loop (discrete winding + bounded phases) would require *recovering* a continuous variable from a discrete one. Information cannot increase under coarse-graining; the recovery is impossible without injecting external information.

A network of closed dials connected by primitive edges *can* carry continuous magnitudes — but the connecting edges are *primitive*, not emergent from the dials. An emergent edge from a network of dials alone fails by the information argument: dials present discrete winding labels and bounded phases, neither of which suffices to encode a continuous unbounded variable.

This establishes the structural asymmetry: **open couplet chains close into dials; dials do not open into chains.** The entropy of bounding is one-directional. The brainstorm's hunch — that bounding loses information that decompactification cannot recover — is now derived from the v2 dynamics plus the closure topology.

## §10. What this means for the project

The chapter's outcome resolves what was originally framed as the project's edge-vs-dial primacy question:

- **Edge/dial primacy is settled by topology.** The point is the 0D primitive; the edge is the 1D relational object between points; the dial is emergent under closure. Neither edge nor dial is "more fundamental" — they are different structural roles distinguished by *topology* (open vs. closed). The asymmetry the brainstorm hypothesized survives, but as a topological feature rather than a primitive-level one.

- **The macro convention "node = dial at the lattice scale" is justified.** Chapter 1 §9's convention — that at the lattice level "node" without further qualification refers to a dial — is now grounded: dials are what closure produces, and the dial is the externally-visible object at lattice vertices. Points surface only inside dials, where the closure construction matters.

- **Edges are bookkeeping inside a dial.** They store the integrated history that drives the dial's dynamics, but they no longer carry the continuous-information channel that they did in the open chain. The dial's externally-visible state lives in its point phases (mod 2π) and its winding number.

- **The bounded-phase character of nodes is derived, not posited.** Chapter 1 §2 left the point's value as an unbounded real, deferring the bounded interpretation. The closure derivation here supplies the missing piece: bounded phase emerges as the natural reading once the topology is closed, and the winding number is the topological invariant that distinguishes inequivalent closures.

The brainstorm's hunch is now a derived structural fact. The project's downstream chapters can take "the dial is the lattice node; its external state is bounded phase + winding" as established, rather than as a discovery target.

## §11. Closing

The closure derivation is complete. The chapter sequence is summarized in the project [README](README.md).
