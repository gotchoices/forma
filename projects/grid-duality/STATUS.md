# grid-duality — Post-review status

This file tracks follow-ups arising from the independent review in [review.md](review.md). It is a working file, not a chapter; it gets pruned as items are resolved.

The action items are organized first by *priority* (within each block A–E) and then collected into *chunks* of work at the end of the file. Chunks are the unit of execution; an item may serve more than one chunk.

The verdict (Scattering wins) is not in question. What changes is the story behind the verdict, the fairness of the elimination of RelCos-both, and the degree to which the substrate-level claims survive scrutiny.

---

## A. User-flagged priorities

### A1. Reframe Scattering as register / transmission-line network

The biggest single change. Scattering currently reads as "two parallel computation channels per edge (a_fwd, a_bwd)" — which makes it feel like a representational choice rather than a physical model. The right description, agreed during review:

- Each **node** is an N-register processor (one register per incident edge).
- Each **edge** is a two-ended transmission line capable of carrying information in both directions.
- A **register** is *not* owned by either side — it is the structural element formed where one end of an edge docks into a node. Each edge contributes two registers (one at each end). Each node hosts one register per incident edge. So a register sits at the boundary between an edge and a node and is "owned" jointly.
- One **clock cycle** has two phases:
  - **Inhale.** Each node samples its registers, applies the scattering matrix S = (2/N)·J − I, and overwrites the register values with the result.
  - **Exhale.** Each edge transmits its two ends' values along itself, which has the effect of swapping the values in its two registers (one at each end node). One exhale = one edge transit; this is what sets the speed of light c.
- Vertices enforce two physical constraints during inhale: voltage continuity (all incident lines see the same potential at the junction) and Kirchhoff current conservation. S = (2/N)·J − I is the *unique* solution to those constraints — not an arbitrary update rule.
- The "two values per edge" is not parallel computation — it is what every 1D wave-carrier needs (two real degrees of freedom per spatial location, the same as position+velocity in mechanics or d'Alembert characteristics on a string). Under the register reading, the two values are simply the values at the edge's two ends.

This framing closes the "two-channel cheating" objection (the values are at *physical ends*, not in parallel channels), makes the speed of light explicit (= one exhale), demotes edge polarity from substrate primitive to v-i-paradigm convenience (registers don't care which end is "head"), and makes energy conservation structurally obvious (inhale is a local unitary, exhale is a pure relabeling).

**To do**:
- [ ] Rewrite [models/scattering.md](models/scattering.md) "State" and "Update rules" sections in register / inhale-exhale language. Keep (a_fwd, a_bwd) only as a footnote alias for sim-maxwell readers.
- [ ] Rewrite chapter 2 §7 to match.
- [ ] Update chapter 1 §2 ("Nodes and edges") to introduce the *register* as the structural meeting point of an edge end with a node — applicable when the model uses Scattering, and reducing to a v-i node-edge interaction otherwise.
- [ ] Update chapter 1 §3 ("Edge polarity") to demote polarity to a v-i-paradigm convenience, not a substrate primitive, since Scattering is the winning model and its registers are unordered.
- [ ] Add a paragraph to chapter 4 §4 (Synthesis) and §5 (Verdict) explaining *why* Scattering wins — not just "passes the tests we chose" but "is the natural register / transmission-line network on the substrate, with nodes as active processors and edges as wave-carriers; speed of light = exhale; energy conservation = unitary inhale + relabeling exhale."
- [ ] Close the two-channel concern explicitly in chapter 4 §6.
- [ ] Optional follow-up: refactor [scripts/models.py](scripts/models.py) Scattering implementation to store state as `r[node, slot]` instead of `(a_fwd, a_bwd)[edge]`, so the code mirrors the description. Pure refactor, no functional change. Lower priority than the documentation rewrite.

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

## Chunks

The items group naturally into five chunks.

### Chunk 1 — Scattering narrative reframe (pure documentation) ✓ DONE
Items: **A1**, **D1**, **D2**, **D3** (closed by A1), **D4**, light wording from **E** that touches the same files.
Files affected: [models/scattering.md](models/scattering.md), [01-foundation.md](01-foundation.md), [02-candidate-models.md](02-candidate-models.md), [04-model-comparison.md](04-model-comparison.md), [README.md](README.md).
No new tests. No code changes (the optional implementation refactor in A1 is deferred — see B5 of A1, marked optional). Independent of every other chunk.

Result: Scattering's documentation now leads with "N-register processor + transmission-line edges + inhale/exhale clock" framing. Polarity is demoted to a paradigm-specific labeling convention. Chapter 4's verdict leads with metric performance and naturalness; bridge-to-grid is a downstream consequence rather than the basis. Bounded-phase scope clarified as a charge-emergence question.

### Chunk 2 — Unbounded phase variants ✓ DONE
Items: **A2**.
One flag added to [scripts/models.py](scripts/models.py); one new script [scripts/test_unbounded_phase.py](scripts/test_unbounded_phase.py); brief notes added to [models/telegrapher.md](models/telegrapher.md), [models/relcos-both.md](models/relcos-both.md), and [models/normalized.md](models/normalized.md).

Result: the mod 2π wrap is *not* a thermodynamic-cooling mechanism — it is a symptom-suppressor. In stable regimes (Normalized, RelCos-both free-wave) the wrap is bit-identically inert, "armed but never firing." In failing regimes (Telegrapher CFL divergence, RelCos-both Dirichlet-pinning divergence) the wrap caps the magnitude of failure (10⁵× instead of 10¹⁰⁵×) but does not fix the underlying instability. Cooling, where it appears (Normalized's relaxation to the substrate Laplacian under damping), comes from the damping term and the static-limit-equals-Laplacian property, not from phase wrapping.

Chapter 4 verdict is unchanged. Documentation updates landed in the per-model spec files; chapter 4 was not reopened.

### Chunk 3 — RelCos-both fair-shake ✓ DONE
Items: **A3**, **B1**, **B2**, **B3**, **C1**.
New scripts: [scripts/test_relcos_dial_ic.py](scripts/test_relcos_dial_ic.py), [scripts/test_2d_freewave_superposition.py](scripts/test_2d_freewave_superposition.py). Documentation updates in [models/relcos-both.md](models/relcos-both.md), [02-candidate-models.md](02-candidate-models.md), [03-test-bench.md](03-test-bench.md), [04-model-comparison.md](04-model-comparison.md).

Result: RelCos-both's elimination is *strengthened*, not revised. Three independent failure modes confirmed:
1. **Junction nonlinearity**: standard L2 result of 0.27/0.41/0.33 with arm-1/arm-2 asymmetry stands. Dial-aware IC gives 0.56/0.10/0.34 — *worse*, not better.
2. **Dirichlet-pinning instability**: standard G2 result of 60,000× divergence stands. Reframed as a free-standing stability concern, not a gravity-test failure (C1 gating clarification).
3. **Free-wave nonlinearity** (new): R² = 0.88 on free-wave superposition (vs Normalized and Scattering at machine ε). Previously the L3 R² = 0.005 conflated this with the Dirichlet failure; now we have clean separation. RelCos-both is intrinsically nonlinear in vacuum.

Implementation issues documented (B1 gauge non-invariance under v → v + c, B2 verbal vs actual edge update, B3 v = 0 default IC imposing a preferred direction). Chapter 4 §3 (linearity), §4 (synthesis), and the results table updated to reflect the L3a/L3b split and the L4 dial-aware fair-shake. Chapter 3 has new test descriptions for L3b, L4, and a clarified G2 gating note.

### Chunk 4 — Test-bench fairness fixes ✓ DONE
Items: **C2**, **C3**, **C4**, **C5** (C5 was actually delivered as part of Chunk 1's chapter-1 §3 update).
One new script: [scripts/test_2d_dispersion.py](scripts/test_2d_dispersion.py). Wording updates in [03-test-bench.md](03-test-bench.md), [04-model-comparison.md](04-model-comparison.md), and [01-foundation.md](01-foundation.md) §3. Energy-metric audit confirmed cross-paradigm absolute values differ by a constant factor (≈ 0.65 for typical wavepackets); ratios and fractions are paradigm-comparable.

Result of C3 (the substantive new test): Scattering at coord 3 is *mildly* dispersive (v_g = 0.35 ± 0.06 across k ∈ [0.2, 2.6], spread ≈ 17%) — not the perfect non-dispersion seen in 1D, which was an artifact of the coord-2 swap matrix. Normalized at coord 3 has v_g = 0.19 ± 0.10 (relative spread > 50%). RelCos-both's centroid does not translate coherently. Chapter 4's L1 row split into L1a (1D coord 2) and L1b (2D coord 3); the verdict is unchanged but more accurately stated.

### Chunk 5 — Light items ✓ DONE
Items: remaining **E** (couplet.md cross-reference, matched-impedance definition).
Brief additions to [01-foundation.md](01-foundation.md) §2 (couplet rationale for keeping primitives independent) and [03-test-bench.md](03-test-bench.md) §5/L2 (one-paragraph definition of "matched impedance" in transmission-line terms).

---

## Suggested execution order

1. **Chunk 1** first. Highest narrative impact, lowest risk, independent of every test outcome. Resets the framing so all subsequent work slots into the right story.
2. **Chunk 2** second. Cheap, focused, addresses a user-stated theory.
3. **Chunk 3** third. The expensive one — should land before the project is considered closed.
4. **Chunk 4** fourth. Fills test-bench gaps; mostly mechanical.
5. **Chunk 5** last (or rolled into Chunks 1/4 opportunistically).

Chunks 1, 2, and 4 are mutually independent and can be done in any order or parallelised. Chunk 3 may force minor revisions to documents Chunk 1 produced; that revision cost is small (a few paragraphs of chapter 4 §3/§4) and worth paying, since Chunk 1 is the larger work and benefits from being "right" earlier.

Items not in the action list are review points where I either disagreed or judged the cost-benefit not worth acting on. None were rejected outright.
