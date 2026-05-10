# Review — projects/metric-charge

Categorized as:

- **Serious** — hard errors of logic, fact, or inference; stand to invalidate a result or a verdict.
- **Moderate** — gaps in reasoning, asserted-not-derived claims, hand-waving, ambiguous formulations, framing tensions; affect confidence in the conclusions.
- **Light** — wording, presentation, scope-of-claim issues. Do not affect substantive conclusions.

This review is the post-refactor pass. The previous review's substantive items have either been resolved by the work1 refactor (S1, S2, S3, M1, M3, M4, M5, M6, M7, L2, L4, L6, L7, N1) or moved to [STATUS.md](STATUS.md) as remaining open todos (TODO-M2, TODO-M8(a), TODO-L5, TODO-N2; plus the author's documented disagreements with prior items L1 and L3). This file records new issues found in the post-refactor pass — items not already tracked in STATUS.

---

## Verdict on the work1 refactor

The refactor is **well-executed**. The chirality criterion is consistently applied across Chapters 1, 4, and 5; the wrap-order convention (u = ring, w = tube) is explicit and propagated through closure rule, multi-link inventory, and gauge-potential identification; the topological-vs-particle-symmetry distinction (Chapter 5 §4.3) addresses the prior-review concern that the principle was over-strong; the σ_uw analysis is sharpened in Chapter 6 §6 to commit explicitly that σ_uw biases chirality within particles, not matter/antimatter populations; and the wrap-order's three-faces consolidation (Chapter 5 §6.4) folds the prior standalone §6.5 demonstration into the central derivation cleanly.

I spot-checked the central math: the three candidate symmetrizations in Chapter 5 §4.2 (R_J → 2A·cos(k_u u + k_w w)·cos(ωt); R_u → 2A·cos(k_u u)·cos(k_w w − ωt); R_w → 2A·cos(k_w w)·cos(k_u u − ωt)) reduce correctly from the (++) ± (sign-pair) sums via cos-sum identities, and the resulting T_μν entries in §4.4 (T_tu = 0, T_tw = −A²·ω·k_w, T_uw = 0) are consistent with the spatial averages of the derivative products. The σ_uw symmetry analysis in Chapter 6 §6.2 is correct (cross-term k_u·k_w invariant under joint sign flip; flips under each chirality reflection), and the resulting commitment that σ_uw biases chirality within particles but not matter/antimatter populations follows from the math directly.

The remaining substantive open items (TODO-M2, M8(a), L5, N2 in STATUS) are unaffected by the refactor.

---

## New issues

### Light

#### 1. Chapter 9 (closing summary) is referenced but does not exist

[README §Chapters](README.md) line 158 lists `09-closing-summary.md` as the consolidation chapter, and [Chapter 8 §9](08-shear-and-fractional-charge.md) line 206 has a "What's next" pointer to the same file. The file does not exist in the project directory.

This was a less-visible problem when chapter 8 itself was in outline form (prior status: "chapters 1-7 in full prose, chapter 8 in outline"). With the refactor making the chapter 1-8 substrate solid, the missing summary chapter is more visible.

The project is functional without a closing summary, and the README's chapter-list signals the planned-but-unwritten status. But the cross-references should either be removed/conditionalized, or the file should be added (even as a brief outline) so the project's table of contents is self-consistent.

Suggested fix: write a brief `09-closing-summary.md` that consolidates what chapters 1-8 establish, what remains open (point at STATUS), and the hand-off to metric-binding. Half-day to a day's work.

#### 2. Chapter 8 §4 quotes a stale form of the closure condition

[Chapter 8 §4](08-shear-and-fractional-charge.md) line 99 reads:

> The phase-pattern view of [Chapter 1 §10](01-foundation.md): "2π winding on w + standing wave on both u and w." This is stated in the bare-metric basis.

The quoted phrasing — "2π winding on w + standing wave on both u and w" — does not appear in current Chapter 1 §10. It is the formulation that the previous review's S1 finding flagged as imprecise; that finding was resolved first by the synchronization rule reformulation, then by the chirality criterion in the work1 refactor. Current Chapter 1 §10 frames closure as a chirality criterion with synchronization (n | m) as the operational test.

The chapter's downstream reasoning in §4 (about how shear entangles u and w windings, and the conservative interpretation that closure operates on (m, n) labels in the bare basis) is sound. Only the quoted formulation is stale.

Suggested fix: replace line 99's quoted phrasing with a current one — e.g., "The chirality criterion of [Chapter 1 §10](01-foundation.md), with the operational synchronization condition n | m on (m, n) integer labels, is stated in the bare-metric basis."

#### 3. Chapter 6 §4.1's off-diagonal cancellation formula is imprecise

[Chapter 6 §4.1](06-handedness-and-pairs.md) lines 158-176 summarizes the stress-energy of a sign-conjugate pair configuration with two formulas:

> $$T_{\mu\mu} \propto |\alpha|^2 + |\beta|^2$$
> $$T_{\mu\nu}^{\text{off-diag}} \propto |\alpha|^2 - |\beta|^2$$

The second formula treats "T_off-diagonal" as a single category that cancels under equal amplitudes. This is correct for the spacetime↔compact off-diagonals (T_tu, T_tw — both odd under (m, n) ↔ (−m, −n) since p_u and p_w both flip sign under joint reversal), but **incorrect for the compact↔compact entry T_uw**, which is bilinear in (k_u, k_w) and *invariant* under joint reversal (both factors flip, the product is unchanged). Under equal amplitudes, T_uw doubles rather than cancels.

The §4.1 imprecision is in tension with §4.2 line 185 — which correctly notes that R_J-symmetrization "cancels the spacetime↔compact gauge potential and leaves only diagonal mass plus the chirality-encoded compact-compact cross-term T_uw" — and with [Chapter 5 §4.2 / §5.2](05-metric-self-consistency.md), which explicitly computes T_uw ≠ 0 under R_J for both closure-satisfying and closure-failing modes.

A reader following the §4.1 math could conclude that *all* off-diagonals (including T_uw) cancel, contradicting §4.2's lead-paragraph claim and Chapter 5's explicit calculation.

Suggested fix: replace §4.1's single off-diagonal formula with two — one for spacetime↔compact (∝ |α|² − |β|², cancels under equal amplitudes) and one for compact↔compact (∝ |α|² + |β|², doubles under equal amplitudes, recording the chirality field T_uw). The spacetime↔compact and compact↔compact entries transform differently under R_J and should be tabulated separately.

---

## Cross-cutting observations

The work1 refactor has produced a cohesive single-derivation arc: chirality criterion → wrap-order-asymmetric standing-wave construction → single gauge field per closure-satisfying particle → closure-failing modes mass-only via R_J fallback. The four equivalent views of the closure condition (chirality, synchronization, topological, metric-side) are explicitly equated in Chapter 5 §6, and each chapter from 1 through 8 references the others through the chirality framing — no visible layering between the older synchronization-only framing and the new chirality framing.

The three findings above are pre-publication-pass issues — one missing chapter, one stale cross-reference, one imprecise formula — that require small edits in three specific places. None affects the framework's substantive conclusions. After these fixes plus the STATUS-tracked todos (M2, M8(a), L5, N2), the project would be in a publication-ready state for its declared scope.

The matter/antimatter-origin question, surfaced sharply by Chapter 6 §6's commitment that σ_uw cannot bias matter/antimatter populations, remains the project's most consequential structural open question and is forwarded to project-direction work outside this review's scope (per the cross-cutting note in STATUS).
