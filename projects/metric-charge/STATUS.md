# STATUS — metric-charge open issues

This file tracks items that remain open after the work1 refactor pass (which restructured Chapter 5 around the wrap-order-asymmetric standing-wave construction, swapped the closure-rule convention to n | m with T(m, 1) primitives, and propagated the labeling and framing changes through chapters 1–8 plus README). The items below are remaining open work *after* that refactor.

---

## Open todos — items I agree with

### TODO-M2 — Four-property gauge-potential test asserted, not derived

**Status:** Open. The work1 refactor simplified the test to one gauge potential (Ch 5 §4.6) but did not actually carry out the geodesic-equation calculation. The [Ch 8 refactor](08-shear-and-fractional-charge.md) (Sept 2026) extends the scope: under shear, the natural-particle definition shifts to the single-Bloch-mode interpretation (Ch 8 §2.2), and the four-property test must be redone for σ ≠ 0 as well.

**What review.md says:** Ch 5's gauge-potential property test currently asserts each of four properties without explicit calculation. Properties 1–3 are bookkeeping (transformation under coordinate change, antisymmetric field strength, gauge invariance). **Property 4 is the substantive one** — the geodesic equation for a particle on the perturbed metric, in the slow-motion limit, picks up a Lorentz-force-like term proportional to compact-direction momentum. This is asserted; the calculation is not in the chapter.

**Why I agree:** The chapter's distinctive methodological commitment is to *test* the standard-physics correspondence rather than assume it. The four-property test as written reduces this to citation. A genuine test would compute the geodesic equation expansion explicitly.

**Scope of fix:**
- Properties 1–3 at σ = 0: short tightening; cite metric-mass Ch 5 (which does Property 2 explicitly for 1D-compact) and extend to the 2D-compact tube direction in 1–2 paragraphs.
- Property 4 at σ = 0: real calculation. Expand the geodesic equation for a charged particle on the surviving gauge potential h_μw, take the slow-motion limit, isolate the force term, show it has the structure of the Lorentz force.
- **σ ≠ 0 extension (added by Ch 8 refactor):** redo all four properties for the single-Bloch-mode particle under shear. The surviving cross-term pattern (T_tu, T_tw, T_uw) differs from the σ = 0 R_u-symmetrized version; the gauge-potential structure under shear is not derivable from a simple translation of the σ = 0 result.

**Estimate:** Half-day for σ = 0 (mostly Property 4). Additional half-day or more for the σ ≠ 0 extension.

**Suggested approach:** Write Property 4 as a new sub-subsection in Ch 5 §4.6 with the explicit calculation at σ = 0 first, then extend to σ ≠ 0 in a second pass once the single-Bloch-mode framing is propagated through Ch 5.

---

### TODO-M8(a) — Chapter 8 optimization computation

**Status:** ✅ **Resolved** by the [Ch 8 refactor](08-shear-and-fractional-charge.md) (Sept 2026). The optimization computation is settled within metric-charge's declared scope (linear theory; see [Ch 1 §11](01-foundation.md)'s "nonlinear backreaction deferred" non-assumption). The original framing's "k_opt from energy minimization" was found to be **degenerate at the linearized level** — all k give identical total energy under Configuration Y. This is the framework's honest answer.

**What was established (Ch 8 §§2–6):**
- The σε product is the structural lever for the closure-satisfying primitive spectrum: m_opt = round(σε) selects the lightest T(m, 1) primitive, with mass exactly M at integer σε (Ch 8 §2.3).
- σ_uw breaks both R_u and R_w chirality reflections by 4σmn/ε in μ², preserving only R_J (Ch 8 §3).
- The natural particle under shear is the single Bloch mode (Ch 8 §2.2); the σ = 0 R_u-symmetrization breaks down at σ ≠ 0.
- Multi-link interpretation: Configuration Y (k phased copies, k gauge-potential cross-terms) is the framework's commitment (Ch 8 §5).
- Linear scalar-field theory does not select k (Ch 8 §6.1); phase-coherence around closed curves is automatically integer regardless of σ, so it does not produce σ-dependent k-selection (Ch 8 §6.2).

**Where k-selection lives:** Outside metric-charge's linear scope. Candidate mechanisms identified in Ch 8 §6.3–6.4 are forwarded:
- **Nonlinear self-interaction (φ⁴ inter-component coupling):** Forwarded to [metric-binding](../metric-binding/) along with other multi-knot energetics. The φ⁴ term is exactly the kind of nonlinear inter-component coupling metric-binding's scope addresses.
- **Substrate Z_k input:** Forwarded to [grid-duality §8](../grid-duality/08-where-alpha-appears.md).
- **Confinement-like binding:** Forwarded to [metric-binding](../metric-binding/).

metric-charge sets up the inventory (which (m, n) configurations are closure-satisfying, what structural consequences flow under Configuration Y, what fractional-charge organization a k-component multi-link produces); the k-selection question itself is downstream.

**Minor follow-on (non-blocking):** Ch 8 §6.5 currently says the framework "should attempt the φ⁴ calculation before forwarding." This wording overcommits relative to Ch 1 §11's nonlinear-backreaction deferral. A small framing tightening in Ch 8 §6.5 (and parallel mentions in Ch 9 §5.2 / §5.4 / §8) would align the prose with the forwarded-to-metric-binding stance. Single editing pass.

---

### TODO-L5 — Fractional-charge sign assignments not worked out

**Status:** Open. Acknowledged in Ch 8 §6.3 and in open-questions, but flagged as a substantive missing piece.

**What review.md says:** The framework's "1/k fractional charge per component" prediction (e.g., 3-component multi-link gives 1/3 per component) doesn't address sign or value structure. Down-type quarks have charge −1/3; up-type have +2/3. The framework currently:
- (i) doesn't say why fractional charge would be specifically −1/3 vs +1/3
- (ii) doesn't explain where +2/3 (up-type) comes from
- (iii) doesn't relate the three quark families' relative signs and magnitudes

**Why I agree:** A reader could mistake the multi-link entry's "1/k" for a derived prediction of fractional-charge magnitude when the calculation hasn't been done. The "candidate quark" identification is preliminary in a way that should be explicit.

**Scope of fix:**
- Trace how the framework's (m, n) signs determine charge sign of each component (under the natural-particle R_u-symmetrized construction, this is the sign of the tube-direction wavenumber n).
- Examine whether different multi-link configurations might naturally give the −1/3 vs +2/3 pattern.
- Note explicitly where +2/3 charges would come from in the framework (different multi-link configurations, or not predicted?).

**Estimate:** Half-day as a careful sign/magnitude audit. The audit can proceed independently of k_opt: trace how (m, n) signs determine charge sign under the single-Bloch-mode interpretation of Ch 8 §2.2, working in a generic-k framing.

**Suggested order:** Independent of remaining TODOs. The empirical identification "which multi-link is the up-type vs down-type quark" is downstream (depends on k-selection, which is forwarded per TODO-M8(a)); but the *structural* sign analysis lives in metric-charge and can be tightened in Ch 6 / Ch 8 §7 directly.

---

### TODO-N2 — Infinite tower of mass-only states needs engagement

**Status:** Open. Identified as Light/Moderate by reviewer.

**What review.md says:** The closure rule predicts the entire genuine-torus-knot tower (T(2, 3), T(2, 5), T(3, 4), T(3, 5), T(2, 7), …) as closure-failing — mass + chirality field, no observable EM. Standard physics has only a small number of stable neutral massive species. The framework currently lists the prediction without engaging with the tension.

**Why I agree:** This is a substantive consequence of the closure rule. The framework's predictive content for non-charged massive states is significantly larger than standard physics observes. Brief engagement with selection mechanisms (mass cost, decay channels, aspect-ratio cuts) would clarify what the framework actually predicts vs what it merely allows.

**Scope of fix (modest):** Add a short subsection or paragraph to Ch 4 or Ch 9 acknowledging the tower and listing candidate selection mechanisms using the framework's existing machinery:
- *Mass cost* — heavier modes (larger √(m² + n²)) are energetically more costly to populate.
- *Aspect-ratio dependence* (Ch 7) — at extreme ε, only specific (m, n) values are stable; the tower is not uniformly populated.
- *Multi-knot decay* — forwarded to [metric-binding](../metric-binding/) — heavier members of the tower may decay into multi-link configurations of T(m, 1) primitives via energetics not captured at this project's linear-theory level.
- *Predictive content distinction* — what the framework predicts is *what's possible*; what's *populated* depends on energetics not in scope here.

**Estimate:** Single editing pass; one paragraph or short subsection.

**Suggested order:** Easy. Can be done independently of other todos.

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

**Status:** ✅ **Resolved** by the [Ch 8 refactor](08-shear-and-fractional-charge.md) (Sept 2026). The stale "2π winding on w + standing wave on both u and w" quotation has been replaced with current chirality-criterion phrasing referencing the operational synchronization condition n | m. Ch 8 §4 now reads consistently with Ch 1 §10.

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

**Status:** Open. Scoped in [work-ch9.md](work-ch9.md) (Sept 2026).

**What's at stake.** Chapters 7 (ratio alone) and 8 (shear alone) treat the two metric parameters as independent. But the framework's three qualitative sheet types — lepton-like, neutrino-like, hadronic-like — each correspond to a *specific combination* of σ and ε, not to a single parameter alone. The lepton-like sheet's character (single isolable charged primitive at moderate mass, substantial parity violation) needs both large ε and substantial σ. The neutrino-like sheet's character (near-degenerate chirality pairs, oscillation) needs both ε near 1 and σ near zero. The hadronic-like sheet's 3-component structure needs both small ε and moderate σ. Neither Ch 7 nor Ch 8 derives these joint structural patterns.

Ch 9 is also the substrate for the eventual downstream exercise: given a sheet's measured properties (mass, gauge structure, observable charge), derive the metric values (diagonals + cross-term) for that sheet. Metric-charge does not handle specific sheets; Ch 9 provides the general-sheet model from which sheet-specific work can build.

**Scope of fix (per [work-ch9.md](work-ch9.md)):**
- Combined (σ, ε) parameter space (§§1–2 of work-ch9.md)
- Single-axis dominance puzzle and resolution candidates (§3)
- σ → 1 principal-axis suppression mechanism — rigorous treatment with integer-ε / non-integer-ε cases (§4)
- Three structural regimes by combined (σ, ε) (§5)
- Three sheet types — qualitative correspondence (§6)
- Towards "metric from observables" (§8.6)

**Dependencies:**
- TODO-M8(a)'s φ⁴ inter-component calculation feeds Ch 9's hadronic-sheet derivation. Best done before Ch 9's write-up so the chapter can commit to mechanism (a) or forward.
- TODO-Ch8a (Configuration Y propagation) should be done first so Ch 9 inherits the commitment cleanly.

**Estimate:** Multi-day chapter write-up after dependencies settle.

**Suggested order:** After TODO-M8(a)'s φ⁴ calculation. Before TODO-P1 (closing summary), which needs Ch 9's combined-parameter structure to be present.

---

### TODO-P3 — Split Ch 6 §4.1's off-diagonal formula into two cases

**Status:** Open. Targeted formula correction.

**What review.md says:** [Chapter 6 §4.1](06-handedness-and-pairs.md) lines 158–176 summarizes the stress-energy of a sign-conjugate pair with a single off-diagonal formula:

> $$T_{\mu\nu}^{\text{off-diag}} \propto |\alpha|^2 - |\beta|^2$$

This treats "T_off-diagonal" as a single category that cancels under equal amplitudes. Correct for spacetime↔compact entries (T_tu, T_tw — odd under (m, n) ↔ (−m, −n)). **Incorrect for the compact↔compact entry T_uw**, which is bilinear in (k_u, k_w) and *invariant* under joint reversal — under equal amplitudes T_uw doubles rather than cancels.

The §4.1 imprecision is in tension with §4.2's claim that R_J-symmetrization "cancels the spacetime↔compact gauge potential and leaves only diagonal mass plus the chirality-encoded compact-compact cross-term T_uw," and with [Chapter 5 §4.2 / §5.2](05-metric-self-consistency.md), which explicitly computes T_uw ≠ 0 under R_J.

**Why I agree:** The math is wrong as written. A reader following §4.1 alone could conclude all off-diagonals cancel, contradicting the explicit Ch 5 calculation and the §4.2 lead paragraph in the same chapter. T_uw and T_tu/T_tw transform differently under R_J and need separate tabulation.

**Scope of fix:** Replace §4.1's single off-diagonal formula with two:
- spacetime↔compact (T_tu, T_tw): ∝ |α|² − |β|², cancels under equal amplitudes;
- compact↔compact (T_uw): ∝ |α|² + |β|², doubles under equal amplitudes, recording the chirality-field cross-term.

Add one sentence noting the different transformation properties under R_J that explain the asymmetric outcome.

**Estimate:** Small targeted edit; under an hour.

**Suggested order:** Independent. Can be done immediately.

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

- After the Ch 8 refactor (Sept 2026) and the Ch 9 chapter write-up, the remaining substantive items are all editing-pass quality. There is no remaining load-bearing computation at metric-charge's linear scope; the structural framework is complete.
- Remaining items partition into two classes:
  - **Localized computations / cleanups** within metric-charge's linear scope (M2 four-property gauge test at σ = 0 and σ ≠ 0; L5 sign audit; N2 tower selection; P3 Ch 6 §4.1 formula fix; Ch8a Configuration Y propagation): honest tightening against existing structure. Tractable.
  - **Chapter-level bookkeeping** (P1 closing summary — needs renaming to `10-closing-summary.md` since Ch 9 now occupies the `09-` slot; updates to README chapter list and Ch 7/Ch 8 "What's next" pointers).
- **What's forwarded out of metric-charge:**
  - k-selection mechanism (the φ⁴ inter-component calculation, substrate Z_k, confinement) → grid-duality / metric-binding.
  - Multi-sheet composition rules (Disc1, Disc2) → metric-binding.
  - Matter/antimatter bias mechanism → substrate-level (grid-primitive) work.
  - The "metric from observables" inversion exercise for specific empirical sheets → downstream sheet-specific follow-on work.
- The matter/antimatter origin question — opened by Ch 6 §6's chirality finding and confirmed by the Ch 8 refactor — is the one place where the framework has *no* derived mechanism for a structural property the user expects to be physically meaningful. σ_uw biases chirality *within particles*, not matter/antimatter populations.
- The framework is now structurally complete for the single-sheet model. The Ch 9 chapter consolidates *what ratio and shear do together*, including how the (σ_uw, ε) parameter space supports the framework's three sheet types and how a sheet's metric can be derived from its observed properties — the substrate for sheet-specific downstream work in metric-binding and beyond.
