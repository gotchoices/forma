# Chapter 2: Closure and Bounding — the Entropic Origin of the Dial

*Outline. Each section is a placeholder for prose to be written.*

---

## §1. The chapter's job

- Derive the entropic-bounding mechanism by which closing a couplet chain into a 2π loop produces a dial.
- Show that the closure operation has a calculable, structural effect: a continuous unbounded cumulative magnitude becomes a discrete winding-number label plus a bounded phase pattern.
- Establish that the asymmetry is one-directional: open chains close into dials, but dials cannot open back into chains. The entropy of bounding is the structural reason.
- This chapter resolves the edge-vs-dial primacy question from the model itself, not from trial-and-error construction.

## §2. The two configurations

- Set up the **open 1D couplet chain** of N couplets: N points φ_0, φ_1, …, φ_{N−1} in ℝ; N edges, with the trailing edge an inert stub per chapter 1 §5.
- Set up the **closed 1D couplet loop** of N couplets: N points with periodic identification φ_N ≡ φ_0; N active edges connecting consecutive points around the loop.
- In both configurations, points hold values per chapter 1 §2 (real-valued, with bounded-phase interpretation deferred to closure) and edges store the integrated history of their endpoint difference per chapter 1 §3.
- The bounded-phase character of a dial — what makes it a dial rather than a chain — is what falls *out* of the closure analysis. Establishing it as a derived structural fact rather than a primitive-level posit is the central job of this chapter.

## §3. The cumulative magnitude — open chain

- Define the chain's cumulative endpoint value Δ_chain ≡ φ_{N−1} − φ_0 = Σᵢ₌₀^{N−2} (φ_{i+1} − φ_i).
- Under v2 dynamics with external partners pinning the two endpoints (φ_left, φ_right), Δ_chain takes the value φ_right − φ_left in steady state.
- Δ_chain is a continuous real, unbounded — limited only by the partners' chosen values.
- The chain's externally-visible state is one continuous unbounded variable (Δ_chain) plus N − 1 internal degrees of freedom (the intermediate point phases) that are slaved to the dynamics.
- This is the **emergent edge** that an open chain produces: a continuous unbounded magnitude carrier, structurally analogous to a single primitive edge.

## §4. The closure constraint — closed loop

- Define the loop's cumulative phase change Δ_loop ≡ Σᵢ₌₀^{N−1} (φ_{i+1} − φ_i) summed once around the loop, with the periodic identification φ_N ≡ φ_0.
- Each individual difference (φ_{i+1} − φ_i) read in the principal branch (−π, π] is bounded by [−π, π].
- The *sum* of differences, summed once around the loop, must equal 2π · k for some integer k — the **winding number**.
- Crucially, Δ_loop is a discrete integer label (times 2π), not a continuous unbounded variable. The closure operation has *quantized* what was continuous in the open chain.
- The N point phases mod 2π form the loop's residual configurational state — a bounded torus T^N (or T^{N−1} after gauge fixing of an overall phase reference).

## §5. Coarse-graining — the externally visible dial

- An external edge connecting to one of the loop's points sees that point's phase, modulo 2π. This phase is bounded.
- The winding number k is a separate topological label that an external observer detects through global coherence properties (e.g., by tracing the full loop or by observing how the loop responds to external winding-changing perturbations).
- The loop's externally-visible state has two parts:
  - A bounded phase at the connecting point.
  - A discrete integer winding sector.
- This is the **emergent dial**: a bounded-phase external object with a discrete sector-label invariant.

## §6. The information-capacity asymmetry

- Open chain capacity (treating point phases as ℝ-valued and edge histories as ℝ-valued integrals): N continuous unbounded reals, plus integrated histories that grow with time. Per Shannon, capacity ~ N · ∞.
- Closed loop capacity: N point phases, each bounded in [0, 2π) after closure → finite per-phase capacity log₂(2π/Δφ) for some discretization scale Δφ; plus 1 integer winding label with bounded range (set by physically reasonable bounds on k).
- The "loss" in closure: the cumulative continuous unbounded variable Δ_chain becomes a discrete bounded integer Δ_loop / 2π. This is finite information loss in the precise Shannon sense — a real-valued unbounded variable has unbounded information capacity, an integer with bounded range has finite capacity.
- The bounding is **entropic** in the precise sense: the closure operation discards continuous degrees of freedom into a discrete invariant. The brainstorm's hunch that "bounding has entropy" is now a derived structural fact, with the closure operation and the discrete winding number as its concrete realization.

## §7. Why the inverse fails

- Constructing an open couplet chain (continuous unbounded magnitude) from a closed dial loop (discrete winding label + bounded phases) would require *recovering* a continuous variable from a discrete one. Information cannot increase under coarse-graining; the recovery is impossible without injecting external information.
- A network of closed dials connected by primitive edges can carry continuous magnitudes — but the connecting edges are *primitive*, not emergent from the dials. An emergent edge from a network of dials alone fails by the information argument.
- This establishes the structural asymmetry: **open couplet chains close into dials; dials do not open into chains.**
- The asymmetry the brainstorm hypothesized — that bounding loses information that decompactification cannot recover — is now a derived, calculable feature of the model rather than an unproven hunch.

## §8. What this means for the project

- **Edge/dial primacy is resolved by the asymmetry.** The point is the 0D primitive; the edge is the 1D relational object between points; the dial is emergent. Neither the edge nor the dial is more fundamental — they are different structural roles, distinguished by topology (open vs. closed). The earlier "edge/node primacy as discovery target" framing is now settled by direct structural derivation.
- The macro convention of chapter 1 §9 — "node defaults to dial at the lattice scale" — is justified: the dial is the externally-visible object at lattice vertices, and its internal point/edge construction is the topic only when the closure mechanism itself is being analyzed.
- Downstream chapters can treat dials as the lattice's nodes by default, with the construction made explicit only where needed.

## §9. Closing

- Brief pointer to the project [README](README.md) for the chapter sequence.
