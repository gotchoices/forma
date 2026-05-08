# STATUS — metric-charge open issues

This file is a working todo for the project. It records unresolved issues from [review.md](review.md) plus issues discovered during recent editing passes. Work is to be picked off this file in user-prioritized order.

---

## Open todos — items I agree with

### TODO-M2 — Four-property gauge-potential test asserted, not derived

**Status:** Open. The most substantive of the remaining Moderate items.

**What review.md says:** Ch 5 §4.2 walks through four standard-physics properties of a gauge potential and asserts each is reproduced. Properties 1–3 are bookkeeping (transformation under coordinate change, antisymmetric field strength, gauge invariance). **Property 4 is the substantive one** — the geodesic equation for a particle on the perturbed metric h_μu, in the slow-motion limit, picks up a Lorentz-force-like term proportional to p^u. This is asserted; the calculation is not in the chapter.

**Why I agree:** The chapter's distinctive methodological commitment is to *test* the standard-physics correspondence rather than assume it. The four-property test as written reduces this to citation. A genuine test would compute the geodesic equation expansion explicitly.

**Scope of fix:**
- Properties 1–3: short tightening; cite metric-mass Ch 5 (which does Property 2 explicitly for 1D-compact) and extend to 2D-compact in 1–2 paragraphs.
- Property 4: real calculation. Expand the geodesic equation for a charged particle on the perturbed h_μu metric, take the slow-motion limit, isolate the force term, show it has the structure of the Lorentz force. ~1–2 pages of algebra.

**Estimate:** Half-day to a day, mostly Property 4.

**Suggested approach:** Write Property 4 as a new sub-subsection in [Ch 5 §4.2](05-metric-self-consistency.md) with the explicit calculation. This converts the chapter's gauge-potential claim from "asserted" to "derived for a single charged-test-particle on a closure-satisfying mode's metric perturbation."

---

### TODO-M3 — Two U(1)s: what is the second gauge field, physically?

**Status:** Qualifier added in Ch 5 §8 (this session). The interpretive question still open and load-bearing.

**Why the user asked for clarification:** The framework predicts *two* gauge potentials (A_μ from h_μu, B_μ from h_μw) at L3. Standard physics has *one* observed EM gauge potential. The framework's reproduction-of-standard-EM claim is conditional on resolving this.

Full analysis in [§M3 — what are the two fields?](#m3--understanding-the-two-fields) below.

**Decision needed:** Which physical interpretation does the project adopt for B_μ? Several candidates exist (Hodge-dual magnetic, mixed gauge boson à la Standard Model electroweak, ungauged dummy direction, new physics) and each has different downstream consequences. This is genuine open work; resolving it likely requires interaction with grid alpha-derivation downstream.

**Suggested order:** Treat as a *thinking-through* todo first — clarify what the framework would predict under each candidate interpretation, decide which is most consistent with the framework's other commitments. Then fix Ch 5 §8 to reflect the chosen interpretation (or to explicitly tabulate the candidates with the framework's framework-internal preference).

---

### TODO-M8(a) — Chapter 8 optimization computation pending

**Status:** Open. Substantive work.

**What review.md says:** Ch 8's framing has been substantially improved (§6 now an honest open optimization rather than a presupposed-answer derivation; §7 addresses integer-quantization consistency), but the actual energy-minimization computation across (σ, ε) space — the calculation that determines k_opt(σ, ε) — has not been done. The chapter remains effectively an outline.

**Why I agree:** The framework's three-phase / quark-like prediction is contingent on Ch 8's optimization yielding k_opt = 3 across the natural (σ, ε) range. Until done, the prediction is pending rather than established. The framework's claim to predict fractional charge in a quark-like pattern depends on this.

**Scope of fix:**
- Compute E(k; σ, ε, q) for k × T(1, q) multi-link configurations under σ_uw shear.
- Minimize over k for the lightest q (q = 1 at small ε, possibly q = 2 elsewhere).
- Plot or tabulate k_opt(σ, ε) across the natural parameter range.
- Report the result honestly — k_opt = 3 if it falls out, some other k otherwise.

**Estimate:** Multi-day; involves real algebra and possibly numerical exploration. Structurally the largest single open todo.

**Suggested order:** Lower priority than the M3 / σ-shear interpretive questions, but if the user wants the framework's predictions to land before downstream MaSt-correspondence work, this is the calculation that needs doing.

---

### TODO-L5 — Fractional-charge sign assignments not worked out

**Status:** Open. Noted as Light because acknowledged in Ch 8 §6.3 and in open-questions, but flagged as a substantive missing piece.

**What review.md says:** The framework's "1/k fractional charge per component" prediction (e.g., (3, 6) = 3 × T(1, 2) gives 1/3 per component) doesn't address sign or value structure. Down-type quarks have charge −1/3; up-type have +2/3. The framework currently:
- (i) doesn't say why fractional charge would be specifically −1/3 vs +1/3
- (ii) doesn't explain where +2/3 (up-type) comes from
- (iii) doesn't relate the three quark families' relative signs and magnitudes

**Why I agree:** A reader could mistake the (3, 6) entry's "1/3" for a derived prediction of fractional-charge magnitude when the calculation hasn't been done. The "candidate quark" identification is preliminary in a way that should be explicit.

**Scope of fix:**
- Trace how the framework's (m, n) signs determine charge sign of each component.
- Examine whether different multi-link configurations (k × T(1, 2) vs k × T(1, 3) etc.) might naturally give the −1/3 vs +2/3 pattern.
- Note explicitly where +2/3 charges would come from in the framework (different (m, n) with different sign patterns? a different k × T configuration? not predicted?).

**Estimate:** Half-day if approached as a careful sign/magnitude audit; more if it requires the Ch 8 optimization to be done first (since k_opt is needed to identify which multi-link is "the quark").

**Suggested order:** Couples to M8(a). Probably best done after the optimization, so the configuration in question is settled.

---

### TODO-N2 — Infinite tower of mass-only states needs engagement

**Status:** Open. Identified as Light/Moderate by reviewer.

**What review.md says:** The synchronization rule predicts the entire genuine-torus-knot tower (T(2, 3), T(2, 5), T(3, 4), T(3, 5), T(2, 7), …) as mass-only states. Standard physics has only a small number of stable neutral massive species. The framework currently lists the prediction without engaging with the tension.

**Why I agree:** This is a substantive consequence of the synchronization rule. The framework's predictive content for non-charged massive states is significantly larger than standard physics observes. Brief engagement with selection mechanisms (mass cost, decay channels, aspect-ratio cuts) would clarify what the framework actually predicts vs what it merely allows.

**Scope of fix (modest):** Add a short subsection or paragraph to [Ch 4 §4.2](04-the-closure-condition.md) acknowledging the tower and listing candidate selection mechanisms using the framework's existing machinery:
- *Mass cost* — heavier modes (larger √(m² + n²)) are energetically more costly to populate.
- *Aspect-ratio dependence* (Ch 7) — at extreme ε, only specific (m, n) values are stable; the tower is not uniformly populated.
- *Multi-knot decay* — forwarded to [metric-binding](../metric-binding/) — heavier members of the tower may decay into multi-link configurations of T(1, q) primitives via energetics not captured at this project's linear-theory level.
- *Predictive content distinction* — what the framework predicts is *what's possible*; what's *populated* depends on energetics not in scope here.

**Estimate:** Single editing pass; one paragraph or short subsection.

**Suggested order:** Easy. Can be done independently of other todos. Useful clarification for any reader.

---

## Open todos — items I disagree with or am ambivalent about

### L1 — "Discovery mode" rhetorical framing inconsistent with content

**Reviewer's claim:** The README claims the project is "in discovery mode" without "explicitly hunting" for any specific particle. But MaSt model-F's identifications (electron at T(1, 2), proton at ε ≈ 1, etc.) shape the chapters' framing.

**My disagreement:** Using known targets as comparison points is appropriate and standard for a framework that claims relevance to physics. The README's rule 4 explicitly states "MaSt identifications are reference targets, not inputs," and the chapters consistently treat them as such — flagging "candidate identification (MaSt model-F reference target)" rather than "this *is* the electron." The rhetoric of "discovery mode while looking sideways at MaSt" is not a fault; it is the right balance for an exploratory framework that has to be relatable to physics for the work to mean anything.

**My recommendation:** Decline to rebalance. The current framing is appropriate.

---

### L3 — "Knot" vs "(m,n) mode" terminology drifts

**Reviewer's claim:** Ch 3 carefully distinguishes (m, n) (primary physical label) from topological knot type (derived). Subsequent chapters drift between "knot" and "(m, n) mode" loosely — e.g., Ch 4 §4 calls T(1, q) "weak-knot diagonal" modes despite their being topologically unknots.

**My disagreement:** Ch 3 §3.1 already explicitly addresses this: it says "weak knot" is a label for T(1, q) modes regardless of whether they are topologically genuine knots, and the (m, n) integer pair is the primary physical label. Subsequent chapters' usage of "knot" follows this established convention. The drift the reviewer flags is real but minor; tightening it consistently would be invasive (replace "knot" with "(m, n) mode" throughout) for unclear payoff. Readers who follow Ch 3 carefully understand the convention.

**My recommendation:** Decline to tighten. Possibly add one sentence at top of Ch 4 cross-referencing Ch 3's terminology convention if it helps; even that is borderline.

---

## M3 — understanding the two fields

This is the explanation requested for what the framework's "two U(1)s" actually means physically, and why the discrepancy with standard EM is load-bearing.

### What the framework predicts

Closure-satisfying modes (at the full L3 substrate) have *both* compact-direction momenta nonzero: p_u ≠ 0 and p_w ≠ 0. By the linearized Einstein analysis of [Ch 5 §3–§4](05-metric-self-consistency.md), each compact direction's momentum sources its own off-diagonal metric perturbation set:

- **A_μ ≡ h_μu** (with μ ∈ {t, S₁, S₂}) — sourced by p_u — passes the four-property gauge-potential test
- **B_μ ≡ h_μw** — sourced by p_w — passes the same test

Each is *independently* a valid U(1) gauge potential under the standard-physics definitions. The framework therefore predicts a **U(1) × U(1) gauge structure** at L3.

### What standard physics has

Standard physics' EM is a **single** U(1) gauge theory (U(1)_em). The Standard Model has additional gauge structure (SU(2) × U(1)_Y for electroweak, SU(3) for color), but for plain EM there is one A_μ — the photon.

So the framework's two U(1)s vs standard physics' one U(1)_em is a real structural mismatch.

### The four candidate resolutions

**Resolution 1: Hodge-dual magnetic-charge analog.** A_μ describes electric charge; B_μ describes magnetic charge. Under Hodge duality in 4D, F_μν has a dual ⋆F_μν that satisfies the *dual* Maxwell equations; magnetic monopoles couple to a dual gauge potential B_μ. Standard physics treats magnetic charge as formal (monopoles aren't observed directly) but the framework would predict it structurally. *If true, the framework predicts magnetic monopoles as a structural twin of electric charges.* This is a falsifiable prediction.

**Resolution 2: B_μ is a new force.** A_μ is the standard photon; B_μ is a new long-range gauge field that couples to compact-w-direction momentum. *If true, the framework predicts an additional Standard-Model-extending force.* Also falsifiable: matter with charge under B should exhibit a long-range B-mediated interaction. Strong constraint from existing observations: most matter shows no such interaction.

**Resolution 3: B_μ is gauged away (redundancy).** Some structural condition (yet to be derived) makes B_μ pure gauge / unobservable on physical states. The two U(1)s would be redundant labels for the same underlying physics; only one is observed. *If true, the framework's prediction reduces to standard EM.* Requires identifying the gauge-fixing condition that does this.

**Resolution 4: A_μ and B_μ mix into observed photon plus a different boson.** Like the Standard Model's electroweak mixing (Weinberg angle): U(1)_Y and SU(2)_3 mix to give the photon (a particular linear combination) and the Z⁰ (the orthogonal combination). The framework's A_μ and B_μ might similarly mix, with one combination being the observed photon and the other being a different field that may or may not be observed. *If true, the framework predicts a partner gauge boson to the photon — possibly already identified with something in the SM, possibly new.*

### What the framework currently says

[Ch 5 §8](05-metric-self-consistency.md) lists Resolutions 1, 2, and 3 (without Resolution 4) and selects none. The Ch 5 §8 qualifier added in this session ("modulo the two-U(1)s issue") makes the conditional nature of the EM-reproduction claim explicit, but the underlying choice is still open.

### Why this matters for the framework's predictions

Each resolution implies different downstream physics:

| Resolution | What B_μ is | Implication for framework predictions |
|---|---|---|
| 1 (Hodge-dual magnetic) | Magnetic photon | Framework predicts magnetic monopoles as a structural twin of electric charge — falsifiable |
| 2 (new force) | A new long-range gauge field | Framework predicts SM-extending physics — falsifiable, strongly constrained |
| 3 (gauged away) | Redundant | Framework reduces to standard EM; need to identify the gauge-fixing condition |
| 4 (mixed) | Mixed with A into photon + partner | Framework predicts the partner; could be Z⁰, could be new |

Choosing among these is downstream work that depends on what the framework's other commitments (closure rule, integer-quantization, etc.) consistently allow. **Without a resolution, the framework's claim to "reproduce standard EM at the linearized level" is structurally incomplete** — what it produces is a U(1)×U(1) gauge structure that *might or might not* reduce to standard U(1)_em.

### What the user might want from this todo

Three possible levels of engagement:

- **Low:** Add Resolution 4 (mixed) to Ch 5 §8's list of candidates, and move on. Easy.
- **Medium:** Examine which of the four resolutions is most consistent with the framework's other commitments (e.g., grid-duality's Z₃ at L3, the wrap-order convention, the synchronization rule). Pick the candidate most likely to be derivable downstream and flag it as the framework's leading hypothesis. Substantive but not exhaustive.
- **High:** Actually carry through one of the candidate resolutions to derived physics (e.g., compute what magnetic-charge phenomenology the framework predicts under Resolution 1; or work out what mixing angle Resolution 4 would give). Real new work.

My recommendation: Start with **Medium**. The framework's commitments (closure rule, KK reduction, wrap-order convention) probably do prefer one resolution over the others; identifying which strengthens the framework's predictive content without committing to a full derivation. The High path can come later if the chosen candidate looks promising.

---

## Cross-cutting observations

- M3 (two U(1)s) is about the framework's predicted structure being *richer than standard physics*. The framework consistently predicts more than the SM has. Whether this means the framework is overpredicting (and needs constraints to reduce to SM) or underpredicting-as-recognized (the extra structure is real and observable in principle) is a recurring open question.
- The remaining substantive Moderate items (M2, M3, M8(a)) are all about *carrying through* what the framework already structurally predicts. None of them require new framework ingredients; they require honest computation against the existing structure. This is the right kind of remaining work for a project that is mostly framing-complete.
- The matter/antimatter bias question — opened by Ch 6 §6's chirality finding — is the one place where the framework currently has *no* derived mechanism for a structural property the user expects to be physically meaningful. Resolution candidates (different shear in metric, substrate-level chirality) are forwarded to project-direction work; the user has indicated they have ideas to discuss separately.
