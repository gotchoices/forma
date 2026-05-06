# grid-duality — Post-review status

This file tracks follow-ups arising from the independent review in [review.md](review.md). It is a working file, not a chapter; it gets pruned as items are resolved.

The action items are grouped by user priority. The verdict (Scattering wins) is not in question; what changes is the story behind the verdict, the fairness of the elimination of RelCos-both, and the degree to which the substrate-level claims survive scrutiny.

---

## A. User-flagged priorities

### A1. Reframe Scattering as a transmission-line network

The biggest single change. Scattering currently reads as "two parallel computation channels per edge (a_fwd, a_bwd)" — which makes it feel like a representational choice rather than a physical model. The right description is:

- Each **edge** is a one-dimensional extended object — a short length of lossless transmission line with two ends.
- Each end carries a real-valued amplitude.
- One **clock tick** = the time for a value at one end to propagate to the other end (the **propagation delay**, which sets the speed of light c).
- After the tick, what was at end A is now at end B and vice versa — a synchronous full swap.
- **Vertices** carry no state. They are *junctions* / a "marketplace" where incident edge-ends exchange values, enforcing voltage continuity and Kirchhoff current conservation. The matrix S = (2/N)·J − I is the unique solution to those two constraints; it is not an arbitrary update rule.
- The "two values per edge" is not parallel computation — it is what every 1D wave needs (two real degrees of freedom per spatial location, the same as position+velocity in mechanics or d'Alembert characteristics on a string).

**To do**:
- [ ] Rewrite [models/scattering.md](models/scattering.md) "State" and "Update rules" sections in transmission-line language. Keep (a_fwd, a_bwd) as a notational alias only.
- [ ] Rewrite chapter 2 §7 to match.
- [ ] Add a paragraph to chapter 4 §4 (Synthesis) and §5 (Verdict) explaining *why* Scattering wins — not "passes the tests we chose" but "is the lattice analog of a transmission-line network, the natural physical model for wave propagation on a graph."
- [ ] Close the two-channel concern explicitly in chapter 4 §6.
- [ ] Update the foundation chapter's treatment of edge polarity: under the transmission-line picture, edge polarity is not load-bearing for Scattering's dynamics. Note this and demote polarity to "convention" rather than "substrate primitive" — or scope it to the v-i paradigm only.

### A2. Add unbounded-phase variants

The user's theory: discarding winding accumulation via mod 2π is what makes v-i models capable of cooling/relaxation. Test by removing the wrap and seeing whether the failure modes get worse (theory confirmed) or stay the same (wrap is representational only).

**To do**:
- [ ] Add a `wrap_node: bool = True` flag to Telegrapher (inherits to Normalized and RelCos-both). Replace `(v + delta) % TWO_PI` with `... if self.wrap_node else (v + delta)`.
- [ ] Build [scripts/test_unbounded_phase.py](scripts/test_unbounded_phase.py) — a focused side-test that runs S1 (stability) and G2 (Dirichlet-pinning relaxation) for each affected model in both `wrap_node=True` and `wrap_node=False` modes. Compare divergence rates and steady-state behavior.
- [ ] Document the result in [models/telegrapher.md](models/telegrapher.md) and [models/relcos-both.md](models/relcos-both.md) under a new "Bounded vs unbounded phase" subsection. Don't re-open chapter 4.

### A3. Re-test RelCos-both fairly

The reviewer flagged that the current test bench's IC convention (v as wave amplitude) is inherited from v-i Telegrapher and may not be faithful to RelCos-both's compass-dial interpretation. Two specific fixes:

**To do**:
- [ ] **Dial-aware IC track.** For RelCos-both only, add an IC variant where v encodes a constant "intended direction of motion" (e.g., v = direction angle) and i carries the wave envelope. Run S2 wavefront and L2 Y-junction in both ICs. Compare. This tests whether the failures are intrinsic to the model or specific to the v-i-style IC translation.
- [ ] **Free-wave superposition test.** L3 currently uses Dirichlet pins, which destabilize RelCos-both for unrelated reasons (G2's instability, which dominates the L3 result). Add a new test where two Gaussian wavepackets cross each other in the bulk — no pins. Compare to an additive baseline. RelCos-both may pass this version while failing the pinned version, which would clarify what about the model is broken.
- [ ] If those tests change RelCos-both's verdict, revise chapter 4 accordingly. If they don't, note the negative result explicitly so the verdict is clearly "fails *both* free-wave and pinned-source tests, not just pinned-source."

---

## B. RelCos-both implementation issues (review §5)

These are real flaws in the current implementation that don't depend on test-bench fairness.

### B1. Gauge non-invariance under global v-shift

The edge update uses `phase_distance(v) · cos(θ − v)` at each end. Under v → v + c (a global rotation of all dials by a constant), neither factor transforms covariantly: phase_distance is non-linear in c (principal-branch wrap), and cos depends on the absolute angle. So the dynamics depends on the absolute zero of v, not just on differences. The compass-dial interpretation would naturally be invariant under this shift; the actual model is not.

**To do**:
- [ ] Document this in [models/relcos-both.md](models/relcos-both.md) §"Notes" or a new §"Symmetries". Note that the model has a *preferred zero* of v, even though the compass-dial picture would suggest otherwise.
- [ ] Add a "Gauge invariance under v → v + c" row to the comparative table in chapter 2 §3. v-i Telegrapher/Normalized: yes. RelCos-both: no. Scattering: trivially (no v).

### B2. Edge update verbal description doesn't match the code

[02-candidate-models.md](02-candidate-models.md) §6 describes the rule as "principal-branch difference of cos-weighted node values." The code computes *separate* weighted contributions from each end and differences them: `(φ(v_t)·cos(θ−v_t)) − (φ(v_h)·cos(θ−v_h))`. These coincide for small v but disagree for general v (the cos factor differs at the two ends).

**To do**:
- [ ] Reconcile chapter 2 §6 and [models/relcos-both.md](models/relcos-both.md) §"Update rules" with the actual code in [scripts/models.py:166-170](scripts/models.py#L166-L170). Use the precise expression; don't paraphrase as a single principal-branch difference.

### B3. v = 0 init implies preferred direction

Under the compass-dial interpretation, "v = 0 everywhere" means "all dials pointing east." The lattice has a built-in preferred direction even in vacuum — which is structurally suspicious for a model that aims to describe isotropic wave propagation.

**To do**:
- [ ] Add a one-paragraph note in [models/relcos-both.md](models/relcos-both.md) §"Notes". Suggest a randomized-v init as a possible alternative; note that we did not test it.

---

## C. Test-bench fairness and consistency

### C1. G2 framing inconsistency

Chapter 3 §7 says G2 is "informative, not gating." Chapter 4 §4 then uses RelCos-both's energy divergence under G2 as part of the elimination argument. Pick one rule and apply it uniformly.

**To do**:
- [ ] Decide: either G2 is gating (in which case Scattering's partial result is also a strike, not just "category error"), or it isn't (in which case RelCos-both's divergence has to be invoked separately as a free-standing stability concern). Recommend the latter — RelCos-both's instability under pinning is a real stability issue regardless of the gravity story, so the disqualification can stand on its own.
- [ ] Update chapter 3 §7 and chapter 4 §3/§4 to match.

### C2. Pinning is paradigm-dependent

"Dirichlet pin v at value V" means different things across paradigms (a constraint on across-variable in v-i models; a strict dial-direction freeze in RelCos-both; an arbitrary `a_fwd = a_bwd = V/2` in Scattering). The chapter currently presents pinning as a paradigm-neutral test.

**To do**:
- [ ] Add a paragraph to chapter 3 §7 acknowledging that "Dirichlet pinning" has different physical content in each paradigm. Note that this affects how G2's results are read — particularly for Scattering, where the bench had to pick one of several possible interpretations.

### C3. Add 2D dispersion test

The 1D dispersion test is uninformative for Scattering at coord 2 (where S reduces to a swap matrix and v_g = 1 trivially). Confirm at coord 3.

**To do**:
- [ ] Build [scripts/test_2d_dispersion.py](scripts/test_2d_dispersion.py): launch a directional Gaussian wavepacket at a chosen carrier wavevector k on a 2D hex torus, track the centroid in 2D over time, extract v_g(k). Sweep over k. Run for Normalized, RelCos-both, Scattering. Confirm Scattering remains non-dispersive at coord 3, or report the deviation if not.
- [ ] Add as test L1b in chapter 3.

### C4. Energy metric consistency across paradigms

The numerical "energy ratio" is not strictly comparable across v-i and Scattering paradigms because of constant factors in the definitions and the v_obs principal-branch reading. Calibrate so cross-model comparisons are apples-to-apples.

**To do**:
- [ ] Audit `total_energy` in each model class. For a wavepacket of equal amplitude/envelope translated naturally between paradigms, the initial total energies should match within a small constant factor. If not, choose normalizations that make them match.

### C5. Bipartite orientation asymmetry

The 2D hex torus uses A → B for *all* edges, so A nodes always have outgoing-only and B nodes always have incoming-only. For v-i models this gives the two sublattices structurally asymmetric roles in any node-update sum.

**To do**:
- [ ] Add a sentence to chapter 1 §3 ("Edge polarity and orientation") flagging this. Note that the two sublattices are dynamically distinguishable under v-i rules and that this is a property of the bipartite orientation, not the lattice geometry.

---

## D. Verdict-presentation issues

### D1. Bridge-to-grid circularity

The current verdict reads partly as "Scattering wins because Scattering = sim-maxwell and sim-maxwell handles Maxwell." This is partly circular. The correct order: Scattering passes the metrics on its own merits *first*, and the bridge to grid is a downstream consequence, not the basis of the win.

**To do**:
- [ ] Rewrite chapter 4 §5 (verdict) to lead with the metric performance, not the bridge identity. The bridge becomes a footnote: "as a bonus, this is also sim-maxwell's model, so the 'bridge to grid' question is closed by construction."

### D2. "Scattering passes everything cleanly" needs qualification

The current chapter 4 §3 closing line reads "Scattering passes everything cleanly," which is then walked back. Foreground the qualification: passes the *light-propagation* tests cleanly; does not relax to the substrate Laplacian under Dirichlet pinning. Both readings are correct individually; together they need explicit framing.

**To do**:
- [ ] Adjust chapter 4 §3 wording to make the "no static limit, by design" qualification visible alongside the test-pass claim.

### D3. Naturalness articulation

The reviewer's deepest critique: the project shows that Scattering passes the tests but doesn't articulate why it is the *natural* model. The transmission-line reframing (item A1) closes this gap; once that's in place, the verdict's structure is "Scattering wins on tests" and "Scattering is naturally motivated as a transmission-line network on the substrate" — the second statement was implicit before, explicit after.

**To do**: covered by A1.

### D4. Bounded-phase scope clarification

Bounded phase (mod 2π on v) is not required for gravity emergence — both the substrate Laplacian solve and the entropic gravity story work on unbounded fields. Bounded phase is motivated by charge emergence (U(1), winding numbers, charge quantization), which is a chapter-7 question.

**To do**:
- [ ] Add a sentence in chapter 4 §6 ("Left open") noting that bounded-phase v is a chapter-7 design choice (about charge emergence), not a chapter-4 design choice (about light + gravity). Light + gravity work fine on unbounded fields.

---

## E. Light items (no priority but cheap to clean up)

- [ ] Move couplet.md's "no global 1:1 pairing" lesson to chapter 1 §2 as a cited rationale for the substrate stopping at "two primitive types" without pairing.
- [ ] Add a one-sentence "matched-impedance" definition (transmission-line-analog vs acoustic) to chapter 3 §5/L2 for readers from outside the bond-graph tradition.
- [ ] Soften "Scattering is the substrate's natural dynamics" (chapter 4 §1) to "Scattering is the lattice dynamics that best satisfies the test-bench criteria" *until* item A1 lands — at which point "naturally motivated as a transmission-line network" recovers the strong claim on physical grounds.

---

## Suggested order

1. **A1** (Scattering reframing) — biggest narrative shift, all-documentation, high impact.
2. **A2** (unbounded variants) — cheap, addresses a real theoretical question.
3. **A3** (RelCos-both fair-shake tests) — addresses biggest fairness concern in the elimination.
4. **B1, B2, B3** (RelCos-both implementation notes) — once we know whether the model survives A3, document the implementation issues either way.
5. **C1, C2** (G2 and pinning framing) — wording fixes that don't require new computation.
6. **C3** (2D dispersion) — fills a real test-bench gap.
7. **C4, C5** (energy metrics, bipartite asymmetry) — accuracy fixes.
8. **D1, D2, D4** (verdict presentation) — wording fixes; D3 is closed by A1.
9. **E** (light items) — only if the rest is in good shape.

Items not in the action list are review points where I either disagreed or judged the cost-benefit not worth it. None of the review's individual points were rejected outright; the items above represent items where action is justified by the user's stated interests and the depth of the issue.
