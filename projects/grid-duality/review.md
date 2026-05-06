# Review — projects/grid-duality

Categorized as:

- **Serious** — hard errors of logic, fact, or inference; stand to invalidate a result or a verdict.
- **Moderate** — gaps in reasoning, missing tests, ambiguous interpretations; affect confidence in the conclusion.
- **Light** — wording, presentation, scope-of-claim. Does not affect the verdict.

The review pays particular attention to whether the **RelCos-both** model was given a fair hearing (it was eliminated despite passing several tests), whether the user's intuition that **Scattering's two-direction state is "cheating"** is justified, and whether the **tests applied** are appropriate measures for the project's stated goal of "modeling light propagation à la Maxwell."

Bottom line up front: the project's verdict (Scattering wins) is largely defensible on the tests as run, but the framing has real issues. RelCos-both's failure is *real* but is partly a test-bench artifact and partly a deeper modeling problem that the chapter doesn't separate cleanly. The "Scattering ≈ sim-maxwell" win is partly a pre-commitment that wasn't tested against the user's stated concern about double-state-per-edge being unphysical.

---

## Chapter 1 — Foundation

### Serious
- None. The substrate (nodes, edges, polarity, common-direction orientation, master clock) is cleanly stated and model-neutral as advertised.

### Moderate
- **Bipartite orientation imposes structural asymmetry that the chapter doesn't flag.** The 2D hex torus uses A → B for *all* edges (engine.py:170–172), so every A-node has all-outgoing edges (s = −1 for all incident edges in the v-i node-update sum) and every B-node has all-incoming (s = +1). For Telegrapher and relcos-both, this means ∂_t v has uniform sign at A vs B nodes for any uniform i: A nodes drift one way, B nodes drift the other. This is a real lattice-convention choice, not a bug, but it has dynamical consequences (the two sublattices play asymmetric roles) that aren't called out. Worth a sentence in §3 ("Edge polarity and orientation"), since it affects every v-i model on the lattice.

### Light
- The framing "two primitive types only" is fine, but couplet.md's lessons (notably "no global 1:1 pairing") could be referenced earlier — they explain *why* the substrate stops at this level rather than committing to (node, edge) pairs.

---

## Chapter 2 — Candidate models

### Serious
- **The dual interpretation of v in RelCos-both is asserted to be "mathematically the same — one number — but conceptually different" (models/relcos-both.md:63), but the dynamics actually depends on which interpretation is in force.** The IC translation in §3 of the test bench treats v as a *phase amplitude* (v = A·env·cos(k·x)), but the cos-weighting in the update treats v as a *compass direction*. These two interpretations agree only when v stays small (linearized regime). When v grows — at a junction during scattering, or under Dirichlet pinning — the dial-direction interpretation kicks in nonlinearly and the model's behavior departs from the phase-amplitude reading. This is the structural reason RelCos-both fails Y-junction and Dirichlet tests, but the chapter presents the failures as separate symptoms rather than tracing them to this single root cause.

### Moderate
- **The "cos sum-to-zero gives implicit Kirchhoff conservation" argument generalizes only at *uniform* v.** §6 says "Σ_k cos(θ_k − v) = 0 for any v, when {θ_k} are at 2πk/N spacing" — true. But this is the sum of *cos weights*, not the sum of (i_k · cos weights). Conservation of Σ s_e · i_e · cos(θ_e − v) requires either uniform i or uniform cos weighting. At a Y-junction during a wave-arriving event neither is true, and the conservation property breaks. The chapter does flag this in models/relcos-both.md ("static-source / Dirichlet problems are a different story") but the reader can come away thinking the cos sum-to-zero is doing more work than it actually is.

### Light
- §3's comparative table is helpful. One row missing: **gauge invariance under global v-shift**. v-i Telegrapher/Normalized are invariant under v → v + c (a constant rotation of all dials), because their dynamics depend on differences of v and on i alone. RelCos-both is *not* invariant: cos(θ_e − v_node − c) ≠ cos(θ_e − v_node) in general, and φ(v + c) ≠ φ(v) + c (the principal-branch wrapping kicks in). Scattering trivially is (no v at all). Worth flagging in the table, since it matters for whether "the dial direction" is physically meaningful in absolute terms.

---

## Chapter 3 — Test bench

### Serious
- **The IC translation for RelCos-both is not faithful to the model's compass-dial interpretation, and the chapter doesn't flag this.** §3 specifies *"v(x) = A · env · cos(k·x)"* with i(x) matched as i = ±v. This treats v as wave amplitude. But under RelCos-both's compass-dial picture, the natural IC for an inbound right-moving wave is plausibly v = constant (a fixed dial direction representing the propagation direction), with i carrying the wave envelope. The test bench inherits the v-i convention without testing whether RelCos-both is being asked to represent a configuration that's natural to it. Without a *dial-aware* IC as a control, we can't distinguish between "RelCos-both can't carry this wave" and "the test wasn't set up for RelCos-both." This is the most direct way the user's "was the test fair?" concern lands as a real issue.

### Moderate
- **The energy metrics are not consistent across paradigms.** For v-i models: 0.5·(Σ v_obs² + Σ i²) where v_obs is the principal-branch reading in (−π, π]. For Scattering: 0.5·Σ (a_fwd² + a_bwd²). For a wavepacket of amplitude A and i = ±v, the v-i energy is A² (Σ env² · cos²) per node and edge, while the equivalent Scattering state has a_fwd = (v+i)/2 = ±v (one channel only), giving energy 0.5 · Σ v² per edge. The numerical comparison "energy ratio after 100 steps" lumps these. They're commensurate to leading order but the conventions differ in the constant factor. The chapter could explicitly normalize so the comparisons are apples-to-apples.

- **Test L2's "matched-impedance theory" framing presumes linearity at the junction.** The R = −1/3, T = +2/3 prediction (and the energy fractions 1/9, 4/9, 4/9) is the unique linear, unitary, equal-impedance scattering matrix. Failing this test diagnoses *either* nonlinearity *or* impedance mismatch *or* non-unitarity. RelCos-both fails because of nonlinearity (cos weighting depends on v_centre, which evolves). The chapter reports this as "wrong reflection coefficient" but the root cause is that the model isn't linear-time-invariant at the junction — there's no fixed scattering matrix to compare to in the first place. The diagnosis is correct but the framing conflates "model has wrong scattering coefficients" with "model is nonlinear." The user's elegance hope for RelCos-both was that cos sum-to-zero would produce automatic linear conservation; the test reveals that this only works for uniform fields, not for coherent wavepackets.

- **Test G2 (gravity dynamics-convergence) is described as "informative, not gating," but the verdict treats RelCos-both's failure here as a strike.** §7 says "this test is informative, not gating. Gravity emergence comes from G1; G2 tells us about the model's relaxation behavior." But §4 then uses RelCos-both's energy divergence under pinning as part of the elimination argument. The two framings should align — either G2 disqualifies models that diverge under pinning, or it doesn't. Pick one. (The energy divergence is *also* a legitimate stability concern independent of the gravity story, so the disqualification can stand on its own — but presented as such, not as a gravity-test failure.)

- **Pinning a *v*-on-nodes value means different things in different paradigms, and the chapter doesn't distinguish.** For Telegrapher/Normalized, "Dirichlet pinning v at value V" is the natural across-variable boundary condition: like grounding a node in a circuit. For RelCos-both, the same pinning *also* fixes the compass-dial direction at that node, which is a stronger/different constraint. For Scattering, pinning a node has no direct meaning (no node state); the test bench uses a_fwd = a_bwd = V/2 on incident edges, which is one of several possible interpretations. The chapter could acknowledge that "Dirichlet pinning" is not a paradigm-neutral test the way it is presented.

### Light
- Test S1 (2D Gaussian pulse) and Test S2 (2D wavefront) overlap substantially. S1 catches gross stability failures (Telegrapher's 45,000× divergence); S2 adds a directional-fidelity check. Fine to keep both but state the discrimination explicitly.

- **The 1D dispersion test (L1) is run only on coord-2 lattices, where Scattering reduces to a permutation matrix and v_g = 1 trivially.** This is correctly noted in §3 of chapter 4, but the reader might expect a 2D dispersion test to confirm that Scattering's non-dispersive behavior survives at coord 3. There isn't one. The wavefront test (S2) gives partial information but doesn't sweep k.

---

## Chapter 4 — Model comparison and verdict

### Serious
- **The verdict for RelCos-both ("removed from active set") rests heavily on Y-junction and Dirichlet tests whose framings are partly bench-dependent.** As laid out above, both tests have model-paradigm-dependent IC choices that weren't tested under alternatives. A more honest framing of the RelCos-both verdict would be: "Under the v-i-style IC and Dirichlet conventions used here, RelCos-both fails. Whether a dial-aware IC and a different boundary-condition treatment would change this is not tested." That doesn't change the verdict for the comparison-as-run, but it does change what the verdict *closes*. The chapter currently treats the verdict as definitive ("the model is incompatible with the matched-impedance light-carrier requirement"); a fairer reading is "the model's nonlinearity makes it incompatible with linear-acoustic scattering at hex Y-junctions, *given the IC translation we used*."

### Moderate
- **Normalized's +11.6% energy drift in the Y-junction test is attributed to "the way the 1/N factor interacts with non-uniform coordination" without diagnostic confirmation.** This is plausible but not tested — for instance, by repeating with longer arms (to separate per-step drift from boundary effects), or by computing the linear-stability eigenvalues of the discrete update on the Y-tree directly. The chapter could either run the diagnostic or downgrade to "consistent with non-strict-unitarity at coord-3 junctions, root cause not isolated."

- **RelCos-both's L3 (linearity / superposition) result of R² = 0.005 conflates two failure modes**: (i) the model's free-wave dynamics is nonlinear at finite amplitude (a real issue), and (ii) Dirichlet pinning destabilizes it (a separate issue). The L3 test as run inherits the Dirichlet pinning from the gravity-style setup, so the divergence dominates. A cleaner linearity test would use *free-wave* superposition (two wavepackets crossing each other), which is what sim-maxwell's superposition test does. RelCos-both might pass that even while failing the pinned-source version. The chapter currently reports R² = 0.005 as a strike against "linearity" generally, when the structural issue is specifically about pinned-source dynamics.

- **Scattering's G2 result (force exponent p = −0.628 instead of −1) is dismissed as "a category error in the test."** This dismissal is partly fair (Scattering has no node state to relax to a Dirichlet-pinned static configuration) and partly not (the test bench's chosen interpretation of "pinning" for Scattering — a_fwd = a_bwd = V/2 on incident edges — *is* a natural interpretation that the bench had to commit to). The result that the dynamic field stays localized near the pin is actually *informative* about how Scattering handles imposed boundary conditions; calling it a category error closes off a useful question. A cleaner statement would be: "Scattering's update is unitary; under fixed-source pinning, it doesn't relax — it carries energy away. This is consistent with a wave equation, not a relaxation equation. Gravity is recovered via the substrate Laplacian (G1), not via Scattering's dynamics."

### Light
- The summary presentation in §3 is clear. One quibble: "Scattering passes everything cleanly" is stated, then immediately walked back to "its static limit is not the graph Laplacian." Worth foregrounding the qualification — Scattering passes the *light-propagation* tests cleanly but does not relax to the substrate Laplacian under pinning. That's a feature (it's a wave equation), but readers may otherwise take "passes everything" at face value.

---

## Specific RelCos-both implementation issues

### Serious
- **The edge update is gauge-non-invariant under global v shifts**, even in the linearized regime. From models.py:168–170:

  ```
  amp_tail = phase_distance(v_tail) · cos(θ − v_tail)
  amp_head = phase_distance(v_head) · cos(θ − v_head)
  i_new = i + (amp_tail − amp_head)
  ```

  Under v → v + c (a global rotation of every dial by a constant c):
  - phase_distance(v + c) is *not* phase_distance(v) + c (the principal-branch wrap is non-linear in c).
  - cos(θ − v − c) is not cos(θ − v) (depends on c).

  So the edge update transforms non-trivially under what should be an unobservable phase choice. This means *the model has a preferred zero of v* — the rotation symmetry of the lattice doesn't carry through to the dynamics. For a model whose interpretive content includes "v is a compass direction," this is the wrong symmetry structure. The compass-dial picture would naturally be invariant under "rotate every dial by the same amount"; the actual dynamics are not.

  This isn't called out in the model spec (relcos-both.md). It's the reason the L3 linearity test fails so badly even in the linearized regime: the model's response depends on the absolute value of v, not just on differences.

### Moderate
- **The edge update is *not* the principal-branch difference of cos-weighted node values.** The chapter (02-candidate-models.md §6) describes the rule informally as "principal-branch difference of cos-weighted node values." The actual implementation computes *separate* weighted contributions from each end, then differences them: `(φ(v_t)·cos(θ−v_t)) − (φ(v_h)·cos(θ−v_h))`. These coincide for small v but disagree for general v (because the cos factor is different at the two ends). The verbal description and the actual rule should be reconciled.

- **The variants RelCos-node-only and RelCos-edge-only are referenced as "tried during development and confirmed unstable" but not in the codebase.** The active models.py has only RelativeCosBoth; the partial variants are gone (line 148–151 notes this). Without their behavior in the comparison the structural argument "cos must apply to both phases" can't be reproduced from the code. If the partial variants were unstable, keeping them in models.py with a deprecation note would let the reader confirm.

### Light
- The RelCos-both `init_state` inherits from Telegrapher (since it inherits from Telegrapher class), so v starts at zeros. Under the compass-dial interpretation, "v = 0 everywhere" means "all dials pointing east." That is, the lattice has a built-in preferred direction even in vacuum. Worth a comment.

---

## Cross-cutting issues

### Serious
- **"Bridge to grid" is implicitly settled by Scattering being one of the candidates, but the verdict's reasoning "Scattering wins ⇒ bridge is trivial" is somewhat circular.** The README states: "sim-maxwell's model is one of the candidates, so the historical bridge-to-grid question becomes implicit in the model selection." If Scattering were a poor model on its own merits, this framing would still produce "Scattering wins because Scattering = sim-maxwell." The selection criteria need to be independent of the bridge-to-grid identity. As it happens, Scattering's test results *are* genuinely the best on the metrics chosen — but the framing should make clear that the metric-passing comes first and the bridge-to-grid is a downstream consequence, not the other way around.

### Moderate
- **The project repeatedly elides the difference between "Scattering passes the tests" and "Scattering is the right physical model."** Test passes establish viability; they don't establish uniqueness or physical naturalness. The good news is that the *naturalness* question has a positive answer that the project simply doesn't articulate — Scattering, read as a transmission-line network (each edge a 1D wave-carrier with values at its two ends, each vertex a junction enforcing voltage continuity and current conservation), is physically well-motivated. But the chapter doesn't say this. As written, the verdict has the slight smell of "we picked the candidate that is sim-maxwell's model because the tests we chose are tests sim-maxwell's model passes." The fix is documentation: present Scattering as a network of transmission lines, with the (a_fwd, a_bwd) labels as a notational convenience rather than the primary description.

- **The static-limit-is-Laplacian property is treated as both a strength (Normalized) and not-a-loss (Scattering), with the framing depending on which model is being discussed.** For Normalized, "static limit is the graph Laplacian" is praised as natural and pedagogically clean. For Scattering, "no static limit" is described as not a flaw because gravity comes from the substrate solve. The two framings are individually defensible but together make the comparison structurally unfair: Normalized is asked to do *more* work (carry both light dynamics and gravity-via-relaxation); Scattering is asked to do *less* (just light dynamics; gravity via substrate solve). If both are allowed to use the substrate solve for gravity, Normalized's static-limit advantage becomes redundant — which the chapter notes — but the comparison still uses G2 against models, which credits the redundant property. Pick one rule and apply it uniformly.

### Light
- **Test labeling is tight and useful overall**, but "matched-impedance" without disambiguation can be read as either an acoustic-style impedance match or a transmission-line analog. Both are intended; a one-sentence definition early would help readers from outside the bond-graph tradition.

- **"Scattering is the substrate's natural dynamics" (chapter 4 §1) is a strong claim** that the test bench supports but doesn't fully establish. The substrate is paradigm-neutral; what's "natural" depends on the metrics. A more conservative phrasing ("Scattering is the lattice dynamics that best satisfies the test-bench criteria") would match what was actually shown.

---

## What I'd recommend doing

If the goal is to give RelCos-both (and the user's elegance intuition) a fair hearing before closing the project's verdict:

1. **Add a "dial-aware IC" track to the test bench.** For each test, run RelCos-both with two ICs: the v-i-style IC currently used, and a dial-aware IC where v encodes the direction of intended motion (constant) and i carries the wave envelope. Compare. This isolates whether the failures are intrinsic to the model or specific to the IC translation.

2. **Add a free-wave superposition test** (two wavepackets crossing each other in a 2D-hex bulk region, not pinned). Compare to L3 (which uses Dirichlet pins). RelCos-both may pass the free-wave version while failing the pinned version, which would clarify what about the model is broken.

3. **Add a 2D dispersion sweep for Scattering.** Confirm v_g(k) ≈ 1 at coord 3, not just at coord 2. (The 1D test is uninformative because Scattering trivially reduces to a swap matrix at coord 2.)

4. **Make the gauge-invariance property of v explicit in the model table.** v-i Telegrapher/Normalized: invariant under v → v + c. RelCos-both: not. Scattering: trivially (no v). This is structurally relevant to whether "v is a compass direction" is even a self-consistent interpretation.

5. **Reframe Scattering's documentation as a transmission-line network**, not as forward/backward channels. The "two values per edge" objection dissolves once each value is identified with one *end* of the edge; the edge is a 1D wave-carrier with two ends, the two values are its instantaneous state at those ends, and one clock tick is one transit time. Vertices are junctions enforcing voltage continuity and current conservation; the scattering matrix S = (2/N)·J − I is the unique solution to those constraints. Concrete description in the new "Final suggestions" section below.

If those changes leave the verdict unchanged, the verdict is more solidly grounded. If they change it, the project's open questions get re-opened, which is also fine.

---

## Summary

| Test | Status | Fair? | Comments |
|------|--------|-------|----------|
| S1 stability | clean | ✓ | Telegrapher's 45,000× divergence is real |
| S2 wavefront | clean | partial | RelCos-both's 2.05× growth flagged "borderline" without further diagnosis |
| L1 1D dispersion | clean | ✓ | Scattering trivially passes at coord 2; would benefit from 2D analog |
| L2 Y-junction | result correct, framing conflated | ⚠ | Tests linear-impedance match; RelCos-both fails because nonlinear, not because impedance-mismatched |
| L3 linearity | result correct under tested IC | ⚠ | RelCos-both's failure is dominated by Dirichlet instability, not free-wave nonlinearity |
| G1 substrate Laplacian | clean | ✓ | Substrate property; applies to all models equally |
| G2 dynamics convergence | informative | ⚠ | Treated inconsistently in the verdict — declared "not gating" but used in elimination |

**Verdict on the verdict**: Scattering does win on the tests-as-run, and the win is real. The project's framing leaves three open issues: (a) is RelCos-both's failure intrinsic or test-bench-specific, (b) is the two-channel structure of Scattering physically natural or just a representational artifact, (c) is "static limit = graph Laplacian" actually a desirable property given the project independently uses the substrate solve for gravity. (a) and (c) are about test fairness and verdict consistency. (b) has a clean answer that the project hasn't articulated: Scattering, properly described, is a transmission-line network model — physically well-motivated, with edges as 1D wave-carriers and vertices as junction-points. The "two-channel" feel comes from the (a_fwd, a_bwd) labeling, not from any physical doubling. See the next section for what the right description looks like.

---

## Final suggestions

The most consequential change suggested by the review is not adding more tests — it is **reframing how Scattering is described**. The model itself is the right one. But the "(a_fwd, a_bwd) per edge" framing makes it feel like the model is tracking two parallel computation channels, and that framing is the reason RelCos-both was attempted in the first place and the reason the verdict feels like an aesthetic concession rather than a physical match. A reframing solves the latter without changing the math.

### What sim-maxwell would say if described physically

Each edge in the lattice is a one-dimensional extended object — physically, a short length of lossless transmission line. It has two ends. Each end carries a real-valued amplitude. The clock tick is the transit time across the edge: in one tick, the value at one end propagates along the edge to the other end. Synchronously across the lattice, the value at the other end propagates back. After the tick, what was at end A is now at end B, and vice versa.

Vertices are junctions where multiple edge-ends meet. Vertices hold no state of their own. When values arrive at a vertex from each incident edge-end, the vertex enforces two physical constraints: all incident lines see the same potential at the junction, and current is conserved (Kirchhoff). These constraints uniquely determine how the arriving values are scattered into outgoing values along the same edges. The matrix S = (2/N)·J − I that the model uses is the unique solution; it is not an arbitrary update rule.

Under this description:

- Each **edge** is a physical 1D wave-carrier with values at its two ends.
- Each **vertex** is a junction enforcing voltage continuity and current conservation.
- The **two values per edge** are not parallel channels — they are the natural state of any 1D wave, which always requires two real degrees of freedom per spatial location (analogous to position and velocity in mechanics, or to the d'Alembert characteristics on a string).
- **Node observables** (voltage at the vertex, current into the vertex, etc.) are *derived* from incident edge-end values: V_v = (2/N)·Σ a_incoming, etc. There is no node primitive state because the junction enforces a constraint, not a value.

This is the picture from microwave-network analysis, transmission-line junction theory, and acoustic networks. It is well-established physics, not a contrivance.

### How this satisfies the design goal that originally motivated the project

The grid-couplet → grid-duality arc was looking for a model where nodes have a role, edges have a role, and the two roles map onto the two components needed to carry a wave with fidelity. Under the transmission-line reframing of Scattering:

- **Edges carry the wave content.** Two values per edge — one at each end — is what 1D waves require. The values propagate end-to-end during a clock tick.
- **Nodes enforce constraints.** Voltage continuity and current conservation. The vertex is where the values from incident edges meet and exchange.
- **The two roles are distinct and physical.** Edges are wave-carriers; vertices are junctions. Both are essential.
- **Both roles map naturally onto the two structural primitives** of the substrate (chapter 1's "node and edge"), which is the form-shaped-by-physics outcome the project hoped for.

The "feels like cheating" objection comes from reading "(a_fwd, a_bwd) per edge" as two abstract computation channels. Once each "channel" is identified with one of the edge's two physical ends, the objection dissolves. The model is not tracking parallel computations; it is tracking a wave's instantaneous state on a 1D extended object.

### Concrete documentation changes

These don't change the code. They change the description so the model reads as physical rather than as a representational choice.

1. **models/scattering.md** — rewrite the "State" and "Update rules" sections in the transmission-line language: *value at each end of each edge; one clock tick = one edge transit; vertex applies voltage continuity + Kirchhoff to determine outgoing values from incoming ones.* The (a_fwd, a_bwd) labels can stay as a notational alias but should not be the primary description. Cite microwave-network analysis as the physical reference.

2. **chapter 2 §7** — same reframing in the candidate-tour description.

3. **chapter 4 §4 (Synthesis) and §5 (Verdict)** — explain that Scattering wins because it is the natural transmission-line network model on the substrate, with physical roles for both edges (wave-carriers) and vertices (junctions). The directional decomposition is one way to read the edge state; the more natural reading is "value at each end of a 1D edge."

4. **chapter 4 §6 (What this verdict closes)** — close the two-channel concern explicitly. *The state structure of Scattering is two values per edge because every 1D wave-carrier has two real degrees of freedom; this is a property of 1D wave physics, not an artifact of the discretization.*

### On RelCos-both

The reframing does not rescue RelCos-both. Its structural problems (gauge non-invariance under global v-shift, dial-direction conflation with phase-amplitude, asymmetric scattering at junctions when v evolves) are real and not a function of how Scattering is described. The honest verdict on RelCos-both stands: an interesting attempt to compress amplitude and direction into one bounded variable, which fails because those are genuinely different roles and conflating them produces nonlinearities that vacuum Maxwell does not have.

What the reframing *does* show is that the user's underlying intuition was right — there is a model where nodes have a role, edges have a role, and the two roles carry the wave's two components. That model is Scattering, described physically. RelCos-both was an attempt to find that model in the bounded-phase / one-value-per-node corner of the design space; the search was reasonable but the corner is empty. The right model lives in the transmission-line corner, with state on edges and constraints at vertices.

### On bounded phase

A note worth recording, separate from the rest: **bounded phase (mod 2π on v) is not required for gravity emergence.** The substrate Laplacian solve (G1) and the entropic gravity story in grid-primitive Ch 4 / sim-gravity-2 both work on unbounded fields. The motivation for bounded phase comes from charge emergence (U(1) gauge structure, winding numbers around closed loops, charge quantization), which is a chapter-7 question, not a chapter-4 question. If the project ever wanted to revisit the v-i candidates as a "lumped-element" alternative to Scattering's "transmission-line" model, dropping the mod from Normalized would give a model with consistent units (both v and i real-valued), exact linearity, and global gauge invariance — at the cost of dispersion and energy drift that Scattering does not have. Not a winner against Scattering on the tests, but a cleaner statement of what a node-and-edge v-i theory actually is. Compactness can be reintroduced specifically at the level of charge in chapter 7, where it does meaningful work.

### What the project should look like after these changes

- Scattering's documentation reads as physically natural (transmission-line network), not as a representational choice.
- The "two-channel cheating" concern is closed in the verdict, not just left implicit.
- The RelCos-both verdict is honest about both the structural problems (real) and the IC translation question (not tested).
- The connection between the project's two structural primitives (node, edge) and the two physical roles (junction, wave-carrier) is made explicit, satisfying the original design intent.

The chapter 4 verdict (Scattering wins) does not change. What changes is the *story* of why it wins — from "passes the tests we chose" to "is the lattice analog of a transmission-line network, which is the right physical model for wave propagation on a graph." The latter is what the project was looking for from the start.
