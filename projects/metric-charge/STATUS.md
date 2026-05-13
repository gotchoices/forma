# STATUS — metric-charge open issues

This file tracks items that remain open after the work1 refactor pass (which restructured Chapter 5 around the wrap-order-asymmetric standing-wave construction, established the chirality-criterion closure rule with T(1, n') primitives, and propagated the labeling and framing changes through chapters 1–8 plus README). The items below are remaining open work *after* that refactor.

---

## Open todos — items I agree with

### TODO-M2 — Four-property gauge-potential test asserted, not derived

**Status:** ✅ **Resolved** by the unified wrap-order-enforcement framing developed in [work-m2.md](work-m2.md) (Sept 2026) and integrated into [Ch 5 §4.6](05-metric-self-consistency.md). The four-property test now runs cleanly at both σ = 0 and σ ≠ 0 under one framing.

**What was established (Ch 5 §§4.6.1–4.6.5):**
- The wrap-order convention of [Ch 1 §10](01-foundation.md) selects h_μw as the gauge candidate. The four-property test is *confirmation* that the convention's selection satisfies standard-physics gauge-potential requirements, not a *selection mechanism* between competing candidates.
- Property 1 (index structure), Property 2 (gauge transformation), Property 3 (field strength antisymmetry and gauge invariance): all derived from coordinate-transformation rules and partial-derivative commutativity. Bookkeeping done explicitly.
- Property 4 (Lorentz-force coupling): explicit Christoffel calculation Γ^μ_νw = −(1/2)F^B^μ_ν, slow-motion limit giving m d²x^μ/dτ² = F^B^μ_ν v^ν p^w — the standard Lorentz-force structure with p^w as charge. Converts the σ = 0 claim from asserted to derived.
- **σ ≠ 0 extension (Ch 5 §4.6.5):** under [Ch 8 §2.2](08-shear-and-fractional-charge.md)'s single-Bloch-mode interpretation, h_μu and h_uw are sourced in addition to h_μw. The wrap-order convention selects h_μw as the gauge potential at σ ≠ 0 identically to σ = 0; h_μu is characterized as the **mass-direction metric perturbation** (frame-dragging-like gravitational contribution), not a second gauge potential. The R_u-symmetrization mechanism of the σ = 0 case is preserved as one realization of the wrap-order convention; the convention is the more fundamental principle and propagates cleanly to σ ≠ 0.

**Why the wrap-order-enforcement framing rather than the symmetric four-property reading:** Applying the four-property test symmetrically to both h_μu and h_μw would lead to a U(1) × U(1) prediction at σ ≠ 0, which conflicts with the framework's "single gauge potential per closure-satisfying particle" claim and the σ = 0 framework's single-U(1) correspondence with standard EM. The symmetric reading imports the symmetry implicit in standard KK (one compact direction, no asymmetry) into this framework (which has explicit wrap-order asymmetry per [Ch 1 §10](01-foundation.md)). Under wrap-order enforcement at the gauge-identification level, the U(1) × U(1) puzzle dissolves: h_μw is the gauge potential by convention at both regimes; h_μu's nonzero contribution at σ ≠ 0 is a metric-distortion effect, not a gauge force.

**Work product retained:** [work-m2.md](work-m2.md) is preserved as the scoping document that surfaced and resolved the σ ≠ 0 framing question. The "symmetric reading → U(1) × U(1)" thread is recorded there as a superseded framing, useful for future readers wondering why σ ≠ 0 doesn't predict two gauge potentials.

---

### TODO-M8(a) — Chapter 8 optimization computation

**Status:** ✅ **Resolved** by the [Ch 8 refactor](08-shear-and-fractional-charge.md) (Sept 2026). The optimization computation is settled within metric-charge's declared scope (linear theory; see [Ch 1 §11](01-foundation.md)'s "nonlinear backreaction deferred" non-assumption). The original framing's "k_opt from energy minimization" was found to be **degenerate at the linearized level** — all k give identical total energy under Configuration Y. This is the framework's honest answer.

**What was established (Ch 8 §§2–6):**
- The σε product is the structural lever for the closure-satisfying primitive spectrum: n_opt = round(σε) selects the lightest T(1, n) primitive, with mass exactly M at integer σε (Ch 8 §2.3).
- σ_uw breaks both R_u and R_w chirality reflections by 4σmn/ε in μ², preserving only R_J (Ch 8 §3).
- The natural particle under shear is the single Bloch mode (Ch 8 §2.2); the σ = 0 R_u-symmetrization breaks down at σ ≠ 0.
- Multi-link interpretation: Configuration Y (k phased copies, k gauge-potential cross-terms) is the framework's commitment (Ch 8 §5).
- Linear scalar-field theory does not select k (Ch 8 §6.1); phase-coherence around closed curves is automatically integer regardless of σ, so it does not produce σ-dependent k-selection (Ch 8 §6.2).

**Where k-selection lives:** Outside metric-charge's linear scope. Candidate mechanisms identified in Ch 8 §6.3–6.4 are forwarded:
- **Nonlinear self-interaction (φ⁴ inter-component coupling):** Forwarded to [metric-binding](../metric-binding/) along with other multi-knot energetics. The φ⁴ term is exactly the kind of nonlinear inter-component coupling metric-binding's scope addresses.
- **Substrate Z_k input:** Forwarded to [grid-duality §8](../grid-duality/08-where-alpha-appears.md).
- **Confinement-like binding:** Forwarded to [metric-binding](../metric-binding/).

metric-charge sets up the inventory (which (m, n) configurations are closure-satisfying, what structural consequences flow under Configuration Y, what fractional-charge organization a k-component multi-link produces); the k-selection question itself is downstream.

---

### TODO-L5 — Fractional-charge sign assignments not worked out

**Status:** Open. Acknowledged in Ch 8 §6.3 and in open-questions, but flagged as a substantive missing piece.

**What review.md says:** The framework's "1/k fractional charge per component" prediction (e.g., 3-component multi-link gives 1/3 per component) doesn't address sign or value structure. Down-type quarks have charge −1/3; up-type have +2/3. The framework currently:
- (i) doesn't say why fractional charge would be specifically −1/3 vs +1/3
- (ii) doesn't explain where +2/3 (up-type) comes from
- (iii) doesn't relate the three quark families' relative signs and magnitudes

**Why I agree:** A reader could mistake the multi-link entry's "1/k" for a derived prediction of fractional-charge magnitude when the calculation hasn't been done. The "candidate quark" identification is preliminary in a way that should be explicit.

**Scope of fix:**
- Trace how the framework's (m, n) signs determine charge sign of each component (under the natural-particle R_u-symmetrized construction, this is the sign of the tube-direction wavenumber m).
- Examine whether different multi-link configurations might naturally give the −1/3 vs +2/3 pattern.
- Note explicitly where +2/3 charges would come from in the framework (different multi-link configurations, or not predicted?).

**Estimate:** Half-day as a careful sign/magnitude audit. The audit can proceed independently of k_opt: trace how (m, n) signs determine charge sign under the single-Bloch-mode interpretation of Ch 8 §2.2, working in a generic-k framing.

**Suggested order:** Independent of remaining TODOs. The empirical identification "which multi-link is the up-type vs down-type quark" is downstream (depends on k-selection, which is forwarded per TODO-M8(a)); but the *structural* sign analysis lives in metric-charge and can be tightened in Ch 6 / Ch 8 §7 directly.

---

### TODO-N2 — Infinite tower of mass-only states needs engagement

**Status:** ✅ **Resolved** (May 2026). Added a short paragraph to [Ch 4 §4.2](04-the-closure-condition.md) after the "substantive framework prediction" claim about the genuine-torus-knot tower, listing the four candidate selection mechanisms (mass cost, aspect-ratio dependence, multi-knot decay, predictive-content distinction). The framework's stance is now explicit: the tower is part of the *predicted* structural inventory; specific *population* selection is downstream work, with multi-knot decay forwarded to [metric-binding](../metric-binding/).

**Original issue:** The framework predicts a much larger tower of closure-failing mass-only states than standard physics observes; without engagement with selection mechanisms, the predictive content read ambiguously as either "framework predicts many neutral massive species" or "framework allows many but doesn't predict their populations."

---

## Open todos — post-refactor review findings

The three items below come from the post-refactor pass of [review.md](review.md) (recorded under "New issues / Light"). Each is a small targeted edit; none affects substantive conclusions. I agree with all three.

### TODO-P1 — Write `09-closing-summary.md`

**Status:** Open. The file is referenced from [README §Chapters](README.md) line 158 and from [Chapter 8 §9](08-shear-and-fractional-charge.md) line 206 but does not exist.

**What review.md says:** With the refactor making the chapter 1–8 substrate solid, the missing summary chapter is more visible. Cross-references should either be removed/conditionalized, or the file should be added so the project's table of contents is self-consistent.

**Why I agree:** Two live cross-references point at a non-existent file. Of the two fixes (remove pointers vs. write the chapter), writing the chapter is the right one — chapters 1–8 now have a coherent single-derivation arc that benefits from a consolidating summary, and the project needs a clean hand-off point to metric-binding.

**Scope of fix:** Write a brief `09-closing-summary.md` that:
- consolidates what chapters 1–8 establish (chirality criterion → wrap-order-asymmetric standing wave → single gauge field per closure-satisfying particle → mass-only fallback for closure-failing modes → fractional-charge picture);
- points at STATUS for what remains open;
- hands off to [metric-binding](../metric-binding/) for binding/decay/multi-link energetics not in scope here.

**Estimate:** Half-day to a day.

**Suggested order:** Best done after TODO-M8(a) and TODO-L5 settle, so the summary can report the optimization outcome and quark-charge structure honestly. If those slip, write a placeholder summary that flags them as pending.

---

### TODO-P2 — Replace stale closure-condition quote in Ch 8 §4

**Status:** ✅ **Resolved** by the [Ch 8 refactor](08-shear-and-fractional-charge.md) (Sept 2026). The stale "2π winding on w + standing wave on both u and w" quotation has been replaced with current chirality-criterion phrasing referencing the operational synchronization condition m | n. Ch 8 §4 now reads consistently with Ch 1 §10.

**Original issue:** [Chapter 8 §4](08-shear-and-fractional-charge.md)'s opening quoted a pre-chirality-criterion phrasing that no longer appeared in Ch 1 §10 — a stale cross-reference making the chapter's framing inconsistent with the rest of the project.

---

### TODO-Disc1 — Multi-sheet metric composition (forwarded to metric-binding)

**Status:** Open. Forwarded.

**What's at stake.** When metric-binding considers two or more closure-satisfying species sharing extended spacetime, each species has its own (ε, σ_uw) pair. Three architectural questions arise: (i) substrate sharing — one 2D compact bundle hosting multiple sheets, or separate compact bundles per species? (ii) diagonal normalization across species — g_uu = g_ww = 1 for each species under the current convention, but species-specific normalization may be required for consistency in multi-species settings; (iii) shear composition — how do per-species σ_uw values compose when sheets share extended spacetime?

**Why this is metric-binding's, not metric-charge's.** metric-charge's scope is charge generation in the general case for one sheet at a time. The multi-species composition rules are downstream architectural commitments. Ch 1 §11 now flags this explicitly as a non-assumption.

**Scope of resolution:** metric-binding's architectural framing should commit to (i)–(iii). No work required within metric-charge.

---

### TODO-Disc2 — Diagonal normalization choice for multi-species (forwarded to metric-binding)

**Status:** Open. Forwarded.

**What's at stake.** Current metric-charge convention writes g_uu = g_ww = 1 in periodicity-form coordinates (with ε in the periodicities). An equivalent parametrization moves ε into the (u, u) diagonal (g_uu = ε², g_ww = 1) with unit periodicities. The two forms describe the same sheet — same ε in two homes (Ch 1 §3). The choice doesn't affect single-particle predictions but may matter when multiple species share a metric.

**Why this is metric-binding's, not metric-charge's.** Same as TODO-Disc1: it's a multi-species architectural choice. Ch 1 §11 now flags it explicitly as a non-assumption.

**Scope of resolution:** metric-binding's architectural framing should commit to one diagonal-normalization convention or accommodate both with a clear rule for which is used when. No work required within metric-charge.

---

### TODO-Ch8a — Propagate Configuration Y commitment to Ch 4 §4.3 and Ch 5 §4 — **DONE**

**Status:** Done (May 2026).

**What was done:**
- [Ch 4 §4.3a](04-the-closure-condition.md): added explicit Configuration Y commitment with cross-reference to Ch 8 §5 and a note on the k-cross-terms-per-link structure with grid-duality consistency.
- [Ch 5 §4.6](05-metric-self-consistency.md): added scope-note blocks for (i) σ = 0 caveat with forward pointer to Ch 8 §2.2 (extending TODO-M2 to the σ ≠ 0 case); (ii) Configuration Y commitment with the k-cross-terms-per-link statement.
- [Ch 6 §6.4](06-handedness-and-pairs.md) (new subsection): added the R_u-conjugate vs R_w-conjugate distinct-roles framing from Ch 8 §3, with subsequent §§6.5–6.7 renumbered. The new subsection clarifies that R_u-conjugate split is about "natural-particle definition shifting under shear" while R_w-conjugate split is the framework's chirality-bias variable.
- [Ch 8 §inheritance](08-shear-and-fractional-charge.md): cross-reference to Ch 6 updated from §6.4 to §6.5 to track the renumbering.

---

### TODO-Ch9 — Write Chapter 9: Ratio and shear together

**Status:** ✅ **Resolved** (May 2026). Chapter 9 written and integrated as [09-ratio-and-shear.md](09-ratio-and-shear.md) (~490 lines, finished form). The chapter brings ratio ε and shear σ_uw together into a unified treatment of the (σ_uw, ε) parameter space, identifies the three structural regimes, characterizes the three sheet types qualitatively, develops the σ → 1 principal-axis suppression mechanism, addresses the single-axis dominance puzzle, treats the σ ↔ s translation for empirical correspondence, and sets up the "metric from observables" inversion substrate.

**Predecessor scoping document:** [work-ch9.md](work-ch9.md) — preserved as the scoping document that surfaced the chapter's structural content and the parametrization decisions.

**Remaining follow-on bookkeeping** (tracked under TODO-P1 below): update [README.md](README.md) chapter list to include Ch 9 and shift the closing summary to `10-closing-summary.md`; update Ch 7 §8 and Ch 8 §9 "What's next" pointers to direct to Ch 9 before the closing summary.

---

### TODO-P3 — Split Ch 6 §4.1's off-diagonal formula into two cases

**Status:** ✅ **Resolved** (May 2026). [Ch 6 §4.1](06-handedness-and-pairs.md) now splits the off-diagonal entries into two categories with explicit derivations of how each transforms under joint reversal (m, n) ↔ (−m, −n):
- **Spacetime↔compact (T_tu, T_tw)** ∝ |α|² − |β|² — linear in each wavenumber individually, flips sign under joint reversal, cancels under equal amplitudes (the gauge-potential channel).
- **Compact↔compact (T_uw)** ∝ |α|² + |β|² — bilinear in (k_u, k_w), invariant under joint reversal, doubles under equal amplitudes (the chirality-field channel).

The split removes the tension between §4.1's previous single-formula presentation and §4.2's claim that R_J-symmetrization "cancels the spacetime↔compact gauge potential and leaves only diagonal mass plus the chirality-encoded compact-compact cross-term T_uw."

**Original issue:** [Chapter 6 §4.1](06-handedness-and-pairs.md) previously presented the off-diagonal stress-energy with a single formula T_off-diag ∝ |α|² − |β|², treating all off-diagonals as cancelling under equal amplitudes. This was wrong for T_uw (which transforms differently under joint reversal) and in tension with §4.2's R_J-symmetrization claim and Chapter 5's explicit T_uw ≠ 0 calculation under R_J.

---

## Open todos — items I disagree with or am ambivalent about

### L1 — "Discovery mode" rhetorical framing inconsistent with content

**Reviewer's claim:** The README claims the project is "in discovery mode" without "explicitly hunting" for any specific particle. But MaSt model-F's identifications (electron at T(1, 2), proton at ε ≈ 1, etc.) shape the chapters' framing.

**My disagreement:** Using known targets as comparison points is appropriate and standard for a framework that claims relevance to physics. The README's rule 4 explicitly states "MaSt identifications are reference targets, not inputs," and the chapters consistently treat them as such — flagging "candidate identification (MaSt model-F reference target)" rather than "this *is* the electron." The rhetoric of "discovery mode while looking sideways at MaSt" is not a fault; it is the right balance for an exploratory framework that has to be relatable to physics for the work to mean anything.

**My recommendation:** Decline to rebalance. The current framing is appropriate.

---

### L3 — "Knot" vs "(m,n) mode" terminology drifts

**Reviewer's claim:** Ch 3 carefully distinguishes (m, n) (primary physical label) from topological knot type (derived). Subsequent chapters drift between "knot" and "(m, n) mode" loosely.

**My disagreement:** Ch 3 §3.1 already explicitly addresses this: it says "weak knot" is a label for closure-satisfying modes regardless of whether they are topologically genuine knots, and the (m, n) integer pair is the primary physical label. Subsequent chapters' usage of "knot" follows this established convention. The drift the reviewer flags is real but minor; tightening it consistently would be invasive (replace "knot" with "(m, n) mode" throughout) for unclear payoff.

**My recommendation:** Decline to tighten. Possibly add one sentence at top of Ch 4 cross-referencing Ch 3's terminology convention if it helps; even that is borderline.

---

## Cross-cutting observations

- After the Ch 8 refactor, the Ch 9 chapter write-up, the TODO-M2 integration, the N2 tower-selection paragraph, and the P3 formula split (Sept 2026–May 2026), the framework is **structurally complete** for the single-sheet model. There is no remaining load-bearing computation at metric-charge's linear scope.
- Two items remain open within metric-charge:
  - **TODO-L5** — Fractional-charge sign audit. Half-day structural sign analysis tracing how (m, n) signs determine charge sign under the single-Bloch-mode interpretation.
  - **TODO-P1** — Closing summary chapter. Half-day-to-day write-up consolidating Chapters 1–9, plus the bookkeeping rename (`09-` → `10-closing-summary.md`), README chapter-list update, and Ch 7/Ch 8/Ch 9 "What's next" pointer updates. Best done last so it can incorporate L5's finding.
- **What's forwarded out of metric-charge:**
  - k-selection mechanism (the φ⁴ inter-component calculation, substrate Z_k, confinement) → grid-duality / metric-binding.
  - Multi-sheet composition rules (Disc1, Disc2) → metric-binding.
  - Matter/antimatter bias mechanism → substrate-level (grid-primitive) work.
  - The "metric from observables" inversion exercise for specific empirical sheets → downstream sheet-specific follow-on work.
- The matter/antimatter origin question — opened by Ch 6 §6's chirality finding and confirmed by the Ch 8 refactor — is the one place where the framework has *no* derived mechanism for a structural property the user expects to be physically meaningful. σ_uw biases chirality *within particles*, not matter/antimatter populations.
- The framework is now structurally complete for the single-sheet model. The Ch 9 chapter consolidates *what ratio and shear do together*, including how the (σ_uw, ε) parameter space supports the framework's three sheet types and how a sheet's metric can be derived from its observed properties — the substrate for sheet-specific downstream work in metric-binding and beyond.
