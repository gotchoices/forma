# work-L5.md — TODO-L5: Fractional-charge sign assignments

This file frames [TODO-L5](STATUS.md): the framework's "1/k charge per component" prediction (Configuration Y, [Ch 8 §5](08-shear-and-fractional-charge.md)) gives uniform per-component fractional charge, which does not match the observed quark pattern (proton = u + u + d = +2/3 + 2/3 − 1/3 = +1).

The work falls into two layers:

- **Layer 1 (in scope):** Sign-tracing audit. What charge sign does a single closure-satisfying T(m', 1) primitive carry? What about its R_u-, R_w-, and R_J-conjugates? What about a uniform-phase k × T(m', 1) Configuration Y multi-link? This is tractable as a half-day editing pass.
- **Layer 2 (out of scope for metric-charge):** Baryon composition — the +2/3, +2/3, −1/3 pattern within a bound multi-particle state. The R-track studies (R53 / R54 / R63 / R64) and the structural hypotheses H1–H3 below are the candidate inputs to this question. Resolution is forwarded to [metric-binding](../metric-binding/) and the R-track.

Conventions follow the rest of the project. M ≡ (ℏ/c)·(2π/L_w). σ ≡ σ_uw.

---

## Sections

| § | Topic |
|---|-------|
| 1 | Layer 1 — sign-tracing audit |
| 2 | Context: the R-track's mode-by-mode approach |
| 3 | Three structural hypotheses |
| 4 | Recommendation |

---

## 1. Layer 1 — sign-tracing audit

Under the single-Bloch-mode interpretation of [Ch 8 §2.2](08-shear-and-fractional-charge.md) and the wrap-order convention of [Ch 1 §10](01-foundation.md), the closure-satisfying primitive is T(m', 1). EM charge couples to tube-direction momentum p^w (per [Ch 5 §4.6.4](05-metric-self-consistency.md) Lorentz-force structure m d²x^μ/dτ² = F^B^μ_ν v^ν p^w). For a Bloch mode at (m, n) = (m', ±1):

<!-- p^w = ℏ k_w = ℏ (2π/L_w) n -->
$$
p^w \;=\; \hbar\, k_w \;=\; \hbar\,\frac{2\pi}{L_w}\, n
$$

The framework's natural charge-sign assignment for a single primitive then organizes by the four discrete reflections of [Ch 8 §2.1](08-shear-and-fractional-charge.md):

| Mode | p^w sign | Charge sign | Mass at σ ≠ 0 | Role |
|---|---|---|---|---|
| T(m', +1) | + | +1 | μ²(m', 1; σ, ε) | "particle" (wrap-order picks m' sign for lower mass) |
| T(m', −1) | − | −1 | μ²(m', −1; σ, ε) = μ²(m', 1) + 4σm'/ε | R_w-conjugate — opposite charge, mass-split |
| T(−m', +1) | + | +1 | μ²(−m', 1; σ, ε) = μ²(m', 1) + 4σm'/ε | R_u-conjugate — same charge, mass-split |
| T(−m', −1) | − | −1 | μ²(−m', −1; σ, ε) = μ²(m', 1) | R_J-conjugate — opposite charge, mass-degenerate |

The R_J pair T(m', +1) ↔ T(−m', −1) is the framework's matter/antimatter labeling per [Ch 6 §3](06-handedness-and-pairs.md) — mass-degenerate under shear, opposite charge.

For a uniform-phase Configuration Y k × T(m', 1) multi-link: all k components share the same primitive (m', +1), all carry charge +1/k of the link's integer total charge k, all phases at 2πj/k for j = 0, ..., k−1. **Per-component charge sign is uniform** — no mixed-sign structure from intra-link phasing.

**Audit conclusion:** the framework's existing prediction is uniform-sign per component within a Configuration Y multi-link. Mixed-sign baryon composition (u + u + d) is not within the natural prediction of Configuration Y at uniform phasing. The framework would need either (a) non-uniform Configuration Y with mixed-orientation components, (b) a different multi-link construct entirely, or (c) a compound-mode picture in which the "baryon" is built from independent mode-assignments rather than a single primitive multi-link.

This audit is in scope for metric-charge. The result is a clean statement of what the framework currently predicts — useful regardless of whether downstream work later supplies a different baryon-composition mechanism.

---

## 2. Context: the R-track's mode-by-mode approach

The R-track studies after R60 — specifically [R53-three-generations](../../studies/R53-three-generations/), with refinements in [R54-compound-modes](../../studies/R54-compound-modes/), [R63-proton-tuning](../../studies/R63-proton-tuning/), and [R64-nuclear-harmonic-stack](../../studies/R64-nuclear-harmonic-stack/) — take a structurally different approach to quark identification than metric-charge's Configuration Y picture:

- **Each quark gets its own (m, n) mode on the proton sheet.** R53's assignments are u = (1, 19), c = (1, 18), t = (7, 3) at one ε and s; d = (5, 4), s = (1, 1), b = (5, −5) at a different ε and s.
- **Mass hierarchies emerge quantitatively from shear-resonance numerics** (R53 reports u : c : t = 1 : 588 : 80,000 and d : s : b = 1 : 20 : 889 to high precision).
- **Charge per mode comes from a separate phase-locking rule** (the R-track's "Q132 v2 promotion-chain") tied to gcd structure of the mode's winding numbers — not from intra-link phasing within a multi-link.
- **The proton is a compound of three independent mode-assignments**, not a single 3-component Configuration Y multi-link.

The R-track has its own unresolved issue: two different shear values (≈ 19 for up-types, ≈ 0.8 for down-types) on what should be one physical sheet (R53 finding F16). R54 and R64 are exploring resolutions (cross-sheet σ_ep coupling, ring-flipped u/d primitives at one geometry). Neither is finalized.

The R-track's picture suggests:

> The +2/3, +2/3, −1/3 asymmetric pattern within a baryon is **mode-identity-and-binding**, not intra-link phasing.

If this is the right framing, Configuration Y is not the place metric-charge should look for the up/down sign asymmetry. Configuration Y explains *fractional-charge magnitude per component of a single primitive multi-link* — structurally distinct from the composition of a baryon from multiple distinct primitives.

---

## 3. Three structural hypotheses

Three structural ideas worth recording as concrete hypotheses, with the existing framework's stance on each and what would close it.

### 3.1 H1 — 120° phase separation produces spatial separation

> Phase rotation around the ring (e.g., 120° for k = 3) produces spatial separation between components.

**Framework status:** Already in Configuration Y per [Ch 8 §5](08-shear-and-fractional-charge.md). The k × T(m', 1) multi-link at relative phases 2πj/k for j = 0, ..., k−1 is exactly this construction. The 120° spacing is the k = 3 specialization; each component is a phase-shifted copy of the same primitive at the same wavevector.

**Charge consequence:** Each component carries the same per-component charge magnitude (1/k of the link's integer charge) with uniform sign. The 120° phasing produces spatial separation, not charge-sign asymmetry between components.

**Conclusion:** H1 is the existing Configuration Y picture. Accounts for the magnitude prediction (1/k per component) but not for the sign-mix (u + u + d). Confirms what the framework already has; does not deliver the asymmetry.

### 3.2 H2 — "Upside-down" knot carries opposite charge

> A knot rotated to fill space not occupied by the original (an inverted embedding on the same torus) carries opposite charge from the reference.

**Framework status:** Geometrically, "upside-down" on T² admits several interpretations under the four discrete reflections of [Ch 8 §2.1](08-shear-and-fractional-charge.md):

- **R_w reflection** — (u, w) ↔ (u, −w). Maps T(m, n) → T(m, −n). Flips tube winding → flips p^w → flips charge. Mass differs at σ ≠ 0 (R_w-split).
- **R_J = R_u ∘ R_w** — (u, w) ↔ (−u, −w). Maps T(m, n) → T(−m, −n). Flips both windings → flips p^w → flips charge. Mass unchanged at any σ (R_J preserved).

The natural geometric interpretation of "rotated 180° around a diameter through the torus, filling complementary space" is closest to R_J: simultaneous flip of both ring and tube directions, mass-preserving, charge-flipping. This is the framework's existing matter/antimatter labeling.

**Charge consequence:** T(m', +1) (particle) and T(−m', −1) (antiparticle) form a mass-degenerate, opposite-charge pair under R_J. Confirms the H2 intuition directly.

**Conclusion:** H2 recovers the existing R_J = matter/antimatter symmetry from the visualizer-level "inverted embedding" intuition. Audit-completeness item: state this geometric interpretation explicitly in [Ch 6 §3](06-handedness-and-pairs.md)'s R_J discussion as supporting intuition. The framework already has the structural content.

### 3.3 H3 — Compound knot with 2 regular + 1 inverted components, forced by topology

> A complex knot structure that fails to close as 3 uniform components but closes only as 2 components in regular orientation + 1 inverted. This would naturally give a +q, +q, −q charge ratio across the three components — the +2/3, +2/3, −1/3 pattern of the proton if total integer charge is +1.

**Framework status:** This is the genuinely novel hypothesis. The standard torus-link multi-component object T(km', k) decomposes into k linked components *all in the same orientation*. Configuration Y formalizes this as k uniformly-phased copies. To get a 2 : 1 orientation split, the multi-link would have to be:

- **Not a standard torus link.** A mixed-orientation compound is not naturally of T(km', k) form.
- **A topologically distinct compound.** Candidates: a multi-component link of distinct knot types (Hopf-link-like), a satellite construction, a connected sum, or a multi-link structure on a higher-genus or higher-dimensional compact that does not admit uniform-orientation embedding.
- **Forced by a generalization of the closure rule.** [Ch 1 §10](01-foundation.md)'s chirality criterion applies per-component. A compound-level generalization could conceivably forbid uniform orientation and force a 2 : 1 split.

**What would close H3:** identify a multi-component link structure such that:

1. The structure is topologically realizable as a closed object on T² (or on the framework's natural compact substrate including cross-sheet structure per [R54](../../studies/R54-compound-modes/)).
2. The structure does *not* admit a uniform-orientation embedding — closure as a single object requires mixed orientations.
3. The forced orientation ratio is 2 : 1 across 3 components.
4. The resulting per-component charge ratios are +q, +q, −q with q = 1/3 of the integer total charge.

This is a substantive open question. It is not derivable from the existing closure rule and Configuration Y as stated. Three avenues for investigation:

- **Substrate-level forcing from grid-duality's wrap-promotion ladder.** L0 → L1 → L2 are structurally distinct substrate operations ([Ch 1 §10](01-foundation.md), [grid-duality §7.5](../grid-duality/07-wrap-promotion-modeling.md)). A compound at L2 might require mixed orientations as a consequence of how L0 phasing propagates upward. Forwarded to [grid-duality](../grid-duality/).
- **Compound modes on cross-coupled sheets.** [R54](../../studies/R54-compound-modes/) explores compound-mode structure with cross-sheet couplings (σ_ep, σ_eν, σ_νp). A 3-component proton compound may require mixed orientations once cross-sheet structure is included — exactly the picture R54 is working toward. Forwarded to the R-track / [metric-binding](../metric-binding/).
- **Generalized closure rule under compound multi-sheet structure.** The chirality criterion of [Ch 1 §10](01-foundation.md) operates per-component on T². A compound generalization is conceivable but not currently formulated. Open structural question.

**Conclusion:** H3 is forwarded. It is not investigable within metric-charge's current framework-level commitments — the existing closure rule and Configuration Y do not produce mixed-orientation compounds, and generalizing them is downstream architectural work. If H3 closes, it would explain the +2/3, +2/3, −1/3 pattern from topological necessity — the "home-run" scenario. Recording H3 as a specific structural-topology question gives downstream work (metric-binding, grid-duality, R-track) a sharp target rather than a vague "fractional-charge asymmetry" placeholder.

---

## 4. Recommendation

### 4.1 In scope for metric-charge — half-day editing pass

The sign-tracing audit of §1 should be propagated into the chapters where charge-sign assignments are currently implicit:

- **Ch 6 §3** ([handedness-and-pairs §3](06-handedness-and-pairs.md)): R_J already identified as matter/antimatter. Add an explicit statement that charge sign flips under R_J via p^w → −p^w, and include the four-mode table of §1 above as the framework's natural charge-sign assignment. Add H2's visualizer-level "inverted embedding" interpretation as supporting intuition.
- **Ch 8 §6 or §7** ([shear-and-fractional-charge](08-shear-and-fractional-charge.md)): tighten the fractional-charge claim. State what Configuration Y predicts (uniform per-component sign at 1/k charge magnitude) and what it does *not* predict (the +2/3, +2/3, −1/3 baryon pattern). Replace any language suggesting the asymmetry might emerge from further Configuration Y refinement.
- **Ch 8 forward-pointer:** add an explicit reference to the R-track's mode-by-mode picture (§2 above) and to H3 (§3.3) as the structural-topology candidate that downstream work would need to close. The forward-pointer should be specific about what is being deferred, not a vague placeholder.

Estimate: half-day editing pass. Independent of TODO-N2 / TODO-P3 / Ch8a — can be done at any time.

### 4.2 Forwarded — concrete pointers

- **R-track ([R53](../../studies/R53-three-generations/), [R54](../../studies/R54-compound-modes/), [R63](../../studies/R63-proton-tuning/), [R64](../../studies/R64-nuclear-harmonic-stack/)):** Empirical mode-by-mode quark identification, including the two-shear puzzle and its in-progress resolution attempts.
- **[metric-binding](../metric-binding/):** Multi-knot energetics, baryon composition, mechanism for binding mixed-orientation components.
- **[grid-duality](../grid-duality/):** Substrate-level structure that might force mixed-orientation compounds at the L2 promotion level.

### 4.3 What this work product delivers

- A clean statement of what metric-charge predicts for charge signs under existing commitments.
- An honest delineation of what is in-scope (sign-tracing audit) and what is downstream (baryon composition).
- Three concrete hypotheses (H1, H2, H3) recorded for downstream investigation, with H3 marked as the structural-topology candidate that would deliver the up/down asymmetry from first principles.
- A forward-pointer that accurately reflects the state of downstream work, not a placeholder that suggests metric-charge will eventually solve the problem itself.

The audit's half-day editing pass is the actionable next step. H1 and H2 are recoveries of existing framework content; H3 is the open structural question whose downstream resolution would close baryon composition.

---

## Notes

The R-track's two-shear puzzle (R53 F16) is the active barrier to a clean closed picture in downstream work. metric-charge does not need to resolve it; the forward-pointer should reflect that the downstream picture is still settling.

H3 is recorded as the framework's most promising structural avenue for delivering the +2/3, +2/3, −1/3 pattern from topological necessity. If a downstream investigation closes H3 affirmatively, the result feeds back into metric-charge as a refinement of Configuration Y or a generalization of the closure rule. If H3 closes negatively, the pattern remains an empirical input rather than a derived structure — the framework's predictive content for fractional-charge magnitude (1/k per component) still stands, but the sign-mix becomes a downstream-supplied input.
