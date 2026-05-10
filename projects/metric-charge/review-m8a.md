# Review — work-m8a.md

This file reviews [work-m8a.md](work-m8a.md), the proposed addressing of [TODO-M8(a)](STATUS.md) — the open question of what the chapter-8 optimization computation actually yields when carried out honestly.

The review is structured as: overall assessment, what the work gets right, where it falls short, and what to do next. I treat shear-ratio.md as informal input (per the instruction not to reference it in the project) — its empirical values inform what mathematical content the framework needs to be able to explain, but the project's derivations stand on their own.

---

## Overall assessment

The exploration is **honest and largely correct**, and it goes well beyond TODO-M8(a)'s narrow brief to engage the broader "shear and ratio together" question — which is what the project actually needs.

Two findings are the cleanest payoff:

- **m_opt = σε** for the lightest closure-satisfying T(m, 1) primitive (§4.1). This is a genuine linear-theory derivation, not asserted: completing the square in m on μ²(m, 1; σ, ε) gives a parabola minimum at m_opt = σε, and the global (1 − σ²)⁻¹ factor cancels the parabola's (1 − σ²) bottom value to leave physical mass exactly M at integer σε. Clean, novel, and structurally important.

- **k_opt is not derivable in pure linear theory** (§6.2). The mass of a k × T(m', 1) multi-link is k²·μ²(m', 1), so the physical mass is k·m(m', 1) — exactly equal to k separate primitives. Linear theory simply does not distinguish them. This is the *correct* answer to TODO-M8(a)'s framing, and the honest answer is more valuable than the "k = 3 emerges" framing it replaces.

The §§3, 4, 5 derivations of symmetry structure, m_opt, and single-axis vs closure-satisfying competition are sound. The §§7, 8 regime map and three-sheet correspondence is reasonable as qualitative structural commentary.

However, the work has several substantive gaps that need to be closed before this can be the basis of a Chapter 8 rewrite, and one of them is critical for connecting to the project's broader empirical scaffolding.

---

## Strengths

### S1. The honest k_opt finding

The right answer to "minimize E(k) over k" in linear theory is "the minimum is degenerate; nothing selects k." work-m8a.md derives this clearly, identifies the candidate ingredients that *could* select k (substrate Z_k, nonlinearity, exclusion, confinement, commensurability), and forwards the k-selection question to grid-duality or metric-binding as appropriate. This is exactly what the project's "discovery-not-proof" stance calls for.

### S2. The m_opt derivation

§4.1 is the cleanest derivable result in the file. The cancellation of (1 − σ²) factors at the integer-σε minimum is striking and deserves prominent placement. The level-crossing analysis (§4.3) and the no-three-fold-degeneracy result (§4.4) are correct consequences.

### S3. Surfacing the architectural question

§5.3 — single-axis modes dominate the low-energy spectrum at extreme ε, but the framework wants charged sheets at extreme ε — is a real architectural question that Chapter 7 only partially flagged. work-m8a.md sharpens it and offers three candidate resolutions (a/b/c). Even without committing, raising the question clearly is valuable.

### S4. Engaging all three sheet types

The qualitative mapping of three sheet types onto regions of the (σ, ε) landscape (§8) is the right shape of analysis. The neutrino-like "mass-eigenstate vs chirality-eigenstate oscillation" prediction (§8.3) is a structurally falsifiable claim worth pursuing.

---

## Concerns and gaps

### G1. The natural particle under shear is not actually defined

This is the most subtle issue. Per [Ch 5 §4](05-metric-self-consistency.md), the natural particle is the **R_u-symmetrized** combination (++) + (−+) = (m, n) + (−m, n). work-m8a.md §3.1 correctly notes that **R_u is broken by shear** — (m, n) and (−m, n) have different μ² under σ ≠ 0:

- μ²(m, n) = m²/ε² − 2σmn/ε + n²
- μ²(−m, n) = m²/ε² + 2σmn/ε + n²

These differ by 4σmn/ε. So (m, n) + (−m, n) at equal amplitude is **not a stationary state** of the sheared wave equation. The "natural particle" of Ch 5 §4 doesn't strictly survive into the σ ≠ 0 regime.

§3.2 attempts to address this but conflates R_u and R_w. The chirality-pair "split" it discusses (between (m, n) and (m, −n)) is the R_w-conjugate pair, not R_u. The R_u-conjugate split — between (m, n) and (−m, n), which is what the natural-particle construction actually combines — is just as broken under shear, and is not discussed.

Practical implication: work-m8a.md uses μ²(m, n; σ, ε) as "the natural particle's mass" throughout §§4–8. Under shear, this is really the mass of the single Bloch mode (m, n), not the symmetrized combination. The structural conclusions (m_opt = σε, level crossings, regime map) are still correct as statements about single-Bloch-mode masses under shear. But the work needs to commit to whether the natural particle under shear is:

(a) The single Bloch mode at (m, n) — wrap-order picks one chirality sector, no symmetrization. The mass is μ²(m, n; σ, ε).

(b) The R_u-symmetrized combination — not a stationary state under shear; only meaningful at σ = 0 or as a small-σ perturbative concept.

(c) Some redefinition specific to the sheared regime — the lowest-energy eigenstate that has the appropriate wrap-order-aligned properties under shear.

The choice matters because it affects how the single gauge field B_μ from h_μw is computed under shear. Chapter 5 §4.6 asserts the four-property gauge structure for the R_u-symmetrized natural particle; under shear, that derivation doesn't strictly transfer. The chapter rewrite needs to address this.

### G2. The parametrization issue is flagged but not developed

§9.3 mentions "lattice-shear vs metric-shear" non-equivalence but doesn't develop it. The framework's σ_uw is metric-shear, bounded by |σ_uw| < 1 (positive-definiteness of the (u, w) sub-block). Production studies (R60, R63, R64) use a different parametrization where the dispersion takes the form

<!-- μ² = (n_t/ε)² + (n_r − s·n_t)² -->
$$
\mu^2 \;=\; (n_t/\varepsilon)^2 + (n_r - s\,n_t)^2
$$

with shear coefficient s that is *not bounded*. Expanding,

$$
\mu^2 \;=\; n_t^2/\varepsilon^2 + n_r^2 - 2s\,n_t n_r + s^2\,n_t^2
$$

Compare to metric-charge's μ² = m²/ε² − 2σmn/ε + n² (with the global (1 − σ²)⁻¹ factor). Matching the linear-in-shear cross-term gives σ = s·ε. The quadratic-in-shear terms differ:

- Lattice-shear: + s²·n_t² = + (σ/ε)²·m²
- Metric-shear (expanded): the (1 − σ²)⁻¹ overall factor contributes + σ²·(m²/ε² + n²) at order σ²

These don't match. The two parametrizations agree at first order in shear but **diverge at second order**, and metric-shear has the hard wall |σ| < 1 that lattice-shear doesn't.

This is consequential. The production studies' shear values for the lepton-like sheet (s on order unity, multiplied by ε on order hundreds) place the empirical sheet far outside metric-charge's σ_uw range. Without resolving the parametrization — or accepting that metric-charge's σ_uw is structurally a different beast from the studies' s — the project cannot quantitatively predict the empirical sheet values from its own machinery.

The chapter 8 rewrite should either (i) develop the lattice-shear form as the framework's primary parametrization, (ii) explicitly accept that σ_uw is bounded and that the empirical sheet values therefore use a different parametrization, or (iii) work out the coordinate change that relates the two and identify where the |σ| = 1 boundary maps to in the lattice-shear form. work-m8a.md §9.3 flags the problem; it doesn't solve it.

### G3. The phase-coherence mechanism (§6.3c) is the most promising open avenue and is unexplored

§6.3 enumerates five candidate ingredients that *could* select k. Of these, only (c) — "phase-coherence under sheared metric" with a possible Z_k commensurability — is a *linear-theory* mechanism. The others (nonlinearity, substrate Z_k, exclusion, confinement) all require structure outside linear scalar-field theory.

If commensurability does select specific k at specific (σ, ε), it would be a clean linear-theory derivation of k_opt — and would substantially improve TODO-M8(a)'s answer. work-m8a.md flags it as "worth a careful analysis but speculative without it" and moves on. This is the analysis most worth doing before declaring the linear-theory result fully exhausted.

The specific calculation: a closed traversal of the k × T(m', 1) link in the sheared metric picks up holonomy phases that depend on (σ, ε, m', k). For the link to close on itself consistently (the wave function returns to its starting value after one full traversal), these holonomies must satisfy specific integer constraints. The constraints depend on k. Whether they pick out specific k (e.g., k = 3 at certain (σ, ε)) is computable; whether they do is open.

### G4. The σ → 1 principal-axis suppression argument (§7.3) needs verification

The claim that "at σ → 1, only the principal-axis closure-satisfying primitive remains at moderate mass; everything else has mass scaled up by (1 − σ²)⁻¹" depends on the principal-axis eigenvector aligning with an integer (m, n) lattice direction. work-m8a.md notes this is automatic only when σε is integer (so m_opt = σε is integer). For generic σε, the principal axis is off-lattice, and integer modes don't lie exactly on the principal axis — the residual (m̂/ε − σ)² controls how much they deviate.

The "suppression of single-axis modes at σ → 1" argument therefore needs careful accounting of how the residual affects the closure-satisfying primitive's mass vs how the (1 − σ²)⁻¹ factor affects single-axis modes. If both scale similarly near σ → 1, no suppression. The argument is plausible but not rigorous as stated.

### G5. The three-sheet engagement is qualitative only

§8 maps the three sheet types onto regions of the (σ, ε) plane qualitatively. The structural patterns it identifies (lepton ↔ principal-axis-aligned charge; neutrino ↔ near-degenerate chirality pairs; hadron ↔ small ε / substrate-driven 3-component) are reasonable, but they don't predict specific (σ, ε) values that would match the empirical estimates.

The user's question — "we should be able to figure out why mathematically [each sheet ends up at its specific (ε, σ)]" — is the right intuition, but answering it requires:

1. Resolving the parametrization issue (G2) so that "specific (σ, ε)" is meaningful across framework and empirical numbers.
2. Identifying what *additional* structure each sheet brings beyond bare (σ, ε) — the substrate inputs, k-selection mechanism, single-axis suppression argument, etc. — that determine why this particular (σ, ε) value is favored for this sheet.
3. Showing that an optimization (energy minimization plus whatever constraint mechanism the framework commits to) actually picks out the empirical values.

work-m8a.md does (1)-flag but not (1)-solve, doesn't do (2), and doesn't do (3). This is the work that's actually needed to answer the user's question.

### G6. Multi-link mass under shear has a subtlety not addressed

§6.1 computes m(km', k) = k · m(m', 1) by treating the multi-link as a single Bloch mode at (km', k). This is mathematically correct as the bare-dispersion mass of *that specific Bloch mode*. But the physical interpretation — "the link's mass equals k times the primitive's mass" — assumes the multi-link configuration is realized as a single (m, n) = (km', k) excitation rather than as a superposition of k primitives at distinct phase positions.

These are different physical configurations:

- **Configuration X**: a single Bloch mode at (km', k). Wavefunction has km'-fold structure in u, k-fold in w. Mass m(km', k) = k·m(m', 1).
- **Configuration Y**: k independent T(m', 1) primitives, each at a phase-offset position around w (the k-component link structure of Ch 4 §4.3). Each component is at (m', 1); total mass is k·m(m', 1) by additivity.

Linear theory says these have the same total mass. But they are *different field configurations*, and the framework's choice between them is what determines whether the multi-link is really "k separate primitives stuck together" or "a single mode with km'-fold u-structure." This distinction matters for §7's discussion of how the link's gauge structure works (k surviving h_μw cross-terms per Ch 5 §4 — but the §4 derivation was for a single closure-satisfying mode, not for a configuration with km'-fold structure).

work-m8a.md doesn't engage with this. The chapter rewrite should either resolve it or explicitly acknowledge that "k × T(m', 1) multi-link" is the Y interpretation, not the X interpretation.

---

## On the user's deeper question

The user asks: "we should be able to figure out why mathematically [the three sheets have such different optimal (ε, σ)]?" Yes — but not from work-m8a.md as it stands. The gaps that block this are:

- The parametrization issue (G2). Until the empirical s and metric-charge's σ_uw are reconciled, "why does the electron sheet land at ε ≈ 400 and s ≈ 2" can't be asked of metric-charge's machinery directly.
- The k-selection mechanism (G3). The hadronic sheet's 3-component structure requires *something* to pick k = 3, and that something isn't in linear theory. Phase coherence might be derivable in linear theory; substrate Z_3 needs to be inherited from grid-duality.
- The single-axis suppression mechanism (G4 and §5.3's architectural question). Without it, the framework can't put any charged sheet at extreme ε — the empirical lepton-like sheet's location is blocked.

Resolving these three would let the project propose specific structural reasons for each sheet's optimal parameter values. work-m8a.md identifies all three as needing resolution; none is resolved.

The user's intuition that ratio and shear should be understood individually first, then together, is correct, and §§4–8 of work-m8a.md is precisely the right kind of analysis to develop. But the analysis stops at "here's the qualitative landscape." The quantitative engagement — predicting why the three sheets sit where they do — is downstream of the gaps above.

A productive next step might be:

1. Settle the parametrization (lattice-shear or metric-shear, with clear conventions).
2. Pursue §6.3(c) — work out the phase-coherence constraints under shear and check whether they select specific k.
3. Develop the σ → 1 suppression argument rigorously (or rule it out).
4. With the above in hand, return to the three sheet types and try to predict each sheet's preferred (σ, ε) from structural mechanisms.

---

## Recommendations

### For the Chapter 8 rewrite (when the gaps are filled)

work-m8a.md §10's recommendations are largely sound:

- §10.1 (reframe central derivation away from k_opt-from-optimization) — yes, do this.
- §10.2 (add the m_opt analysis prominently) — yes.
- §10.3 (engage the architectural question) — yes; commit to a resolution or explicitly leave open.
- §10.4 (consider merging Ch 7 and Ch 8, or adding a combined chapter) — Option B (separate ratio-only and shear-only setups, with a combined "ratio + shear together" chapter) seems right. The combined chapter is where the three-regime / three-sheet structural analysis lives.
- §10.5 (forwardings) — yes, including specifically forwarding the k-selection question to grid-duality.
- §10.6 (honest scope statement) — yes.

### Before rewriting the chapter

Address G1 (natural particle under shear), G2 (parametrization), and ideally G3 (phase-coherence) first. The chapter rewrite without these will need to repeatedly acknowledge open questions where the math should give an answer; with them resolved, the chapter can make stronger claims.

### Status of TODO-M8(a)

work-m8a.md substantively addresses the four sub-items of TODO-M8(a) and reports the honest finding (k_opt is undefined in linear theory). The todo can be considered **partially addressed**: the optimization question's answer is now clear, but the chapter still needs to be rewritten with the new framing, and the deeper sheet-character analysis the work surfaces is unfinished. STATUS.md's todo should be updated to reflect the partial answer and to add the follow-on items: phase-coherence calculation, parametrization choice, natural-particle-under-shear clarification.

The work is the right kind of work — open-minded, mathematically careful, honest about what linear theory does and doesn't predict. The gaps identified here are extensions of that same approach, not corrections to it.
