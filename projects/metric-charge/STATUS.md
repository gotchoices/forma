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
