# STATUS — metric-charge open issues

This file tracks items that remain open after the work1 refactor pass (which restructured Chapter 5 around the wrap-order-asymmetric standing-wave construction, swapped the closure-rule convention to n | m with T(m, 1) primitives, and propagated the labeling and framing changes through chapters 1–8 plus README). The items below are remaining open work *after* that refactor.

---

## Open todos — items I agree with

### TODO-M2 — Four-property gauge-potential test asserted, not derived

**Status:** Open. The work1 refactor simplified the test to one gauge potential (Ch 5 §4.6) but did not actually carry out the geodesic-equation calculation.

**What review.md says:** Ch 5's gauge-potential property test currently asserts each of four properties without explicit calculation. Properties 1–3 are bookkeeping (transformation under coordinate change, antisymmetric field strength, gauge invariance). **Property 4 is the substantive one** — the geodesic equation for a particle on the perturbed metric, in the slow-motion limit, picks up a Lorentz-force-like term proportional to compact-direction momentum. This is asserted; the calculation is not in the chapter.

**Why I agree:** The chapter's distinctive methodological commitment is to *test* the standard-physics correspondence rather than assume it. The four-property test as written reduces this to citation. A genuine test would compute the geodesic equation expansion explicitly.

**Scope of fix:**
- Properties 1–3: short tightening; cite metric-mass Ch 5 (which does Property 2 explicitly for 1D-compact) and extend to the 2D-compact tube direction in 1–2 paragraphs.
- Property 4: real calculation. Expand the geodesic equation for a charged particle on the surviving gauge potential h_μw, take the slow-motion limit, isolate the force term, show it has the structure of the Lorentz force.

**Estimate:** Half-day, mostly Property 4.

**Suggested approach:** Write Property 4 as a new sub-subsection in Ch 5 §4.6 with the explicit calculation. This converts the chapter's gauge-potential claim from "asserted" to "derived for a single charged-test-particle on a closure-satisfying mode's metric perturbation."

---

### TODO-M8(a) — Chapter 8 optimization computation pending

**Status:** Open. Substantive work.

**What review.md says:** Ch 8's framing is honest (§6 an open optimization rather than a presupposed-answer derivation; §7 addresses integer-quantization consistency), but the actual energy-minimization computation across (σ, ε) space — the calculation that determines k_opt(σ, ε) — has not been done. The chapter remains effectively an outline.

**Why I agree:** The framework's three-phase / quark-like prediction is contingent on Ch 8's optimization yielding k_opt = 3 across the natural (σ, ε) range. Until done, the prediction is pending rather than established. The framework's claim to predict fractional charge in a quark-like pattern depends on this.

**Scope of fix:**
- Compute E(k; σ, ε, m') for k × T(m', 1) multi-link configurations under σ_uw shear.
- Minimize over k for the lightest m' (m' = 1 at most ε, possibly m' = 2 elsewhere).
- Plot or tabulate k_opt(σ, ε) across the natural parameter range.
- Report the result honestly — k_opt = 3 if it falls out, some other k otherwise.

**Estimate:** Multi-day; involves real algebra and possibly numerical exploration. Structurally the largest single open todo.

**Suggested order:** Couples to TODO-L5 (which depends on knowing k_opt to identify "the quark configuration").

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

**Estimate:** Half-day if approached as a careful sign/magnitude audit; more if it requires the Ch 8 optimization to be done first (since k_opt is needed to identify which multi-link is "the quark").

**Suggested order:** Couples to TODO-M8(a). Probably best done after the Ch 8 optimization, so the configuration in question is settled.

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

**Status:** Open. Trivial fix; flagged by post-refactor pass as a stale quote left over from the pre-chirality-criterion framing.

**What review.md says:** [Chapter 8 §4](08-shear-and-fractional-charge.md) line 99 reads:

> The phase-pattern view of [Chapter 1 §10](01-foundation.md): "2π winding on w + standing wave on both u and w." This is stated in the bare-metric basis.

The quoted phrasing predates both the synchronization-rule reformulation and the work1 chirality criterion. Current Ch 1 §10 frames closure as a chirality criterion with synchronization (n | m) as the operational test. The chapter's downstream reasoning is sound; only the quoted formulation is stale.

**Why I agree:** The quote no longer matches what Ch 1 §10 says. Anyone clicking the cross-reference would find a different formulation. The fix is a one-line replacement.

**Scope of fix:** Replace line 99's quoted phrasing with a current one — e.g., "The chirality criterion of [Chapter 1 §10](01-foundation.md), with the operational synchronization condition n | m on (m, n) integer labels, is stated in the bare-metric basis."

**Estimate:** Trivial. Single line edit.

**Suggested order:** Independent. Can be done immediately.

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

- The remaining substantive items (M2, M8(a), L5, N2) are all about *carrying through* what the framework already structurally predicts. None of them require new framework ingredients; they require honest computation against the existing structure. This is the right kind of remaining work for a project that is framing-complete after the work1 refactor.
- The matter/antimatter origin question — opened by Ch 6 §6's chirality finding — is the one place where the framework currently has *no* derived mechanism for a structural property the user expects to be physically meaningful. The framework now sharply commits: σ_uw biases chirality *within particles*, not matter/antimatter populations. Where matter/antimatter bias does come from is forwarded to substrate-level (grid-primitive) work; the user has indicated they have ideas to discuss separately.
