# Review — projects/grid-primitive

Chapter-by-chapter review. Issues categorized as:

- **Serious** — hard errors of logic, fact, or inference; stand to invalidate a result.
- **Moderate** — unexplained variables, missing citations, gaps in reasoning, ambiguities; should be tightened to be reasonably understood.
- **Light** — language, style, or clarity. Does not affect accuracy or results.

**Scope note.** This review takes the project at the framing it sets for itself: the project is *not* trying to derive α numerically, and it *assumes* ζ_2D = 1/3 from lattice geometry rather than deriving it. Issues that would be Serious if the project were claiming a numerical derivation of α or ζ are downgraded to Moderate or removed when they are about *consistency* with assumed values rather than *derivation* of those values.

---

## Chapter 1 — Foundation

### Serious
- None.

### Moderate
- **Section numbering bug.** Two adjacent sections are both labeled §9: "9. Relationship to the earlier viz model" and "9. What is taken as input from GRID". The latter should be §10 per the concepts table. §11 and §12 then have the right numerical labels but inconsistent counts.
- **Concept-table mismatch for §4.** Table lists §4 as "Boundedness — why φ is compact and e is not", but the actual §4 heading is "The shape of the field, and what makes entropy possible". The §4 content covers polar/Cartesian framing and winding numbers, not boundedness specifically.
- **Polar-vs-Cartesian framing of (e, φ) is ambiguous.** §3 declares *e* a signed magnitude (+ tension, − compression) while φ is an angle mod 2π, then §4 writes ψ_R = *e* cos φ, ψ_I = *e* sin φ — the standard polar→Cartesian map, which assumes *e* ≥ 0 (otherwise (e, φ) and (−e, φ + π) double-cover the same vector). The chapter does not commit to whether (e, φ) are genuine polar coordinates or two independent real fields. This ambiguity propagates into chapter 4 (see Ch4 Serious #1).
- **A6 listed as input contradicts chapter 8's stated deliverable.** The §10 (numbered "9") "Inputs from GRID" table includes "Coupling α ≈ 1/137 — Axiom A6". README and chapter 8 frame α as a project deliverable (its *form* derived). Treating A6 as input here muddies the input/output boundary.
- **The "matched chirality is the simplest physically motivated choice" justification (§8) overstates.** Even for actual helical-fiber media, PE and KE chirality coefficients need not be identically coupled. The honest framing — which the chapter elsewhere supports — is that matched chirality is a *modeling choice* that prevents the slow-mode tension. The "simplest physically motivated" wording goes beyond that.

### Light
- The "rubber cylinder reinforced with helical fibers" mechanical analog is reused several times (§2, §3, §5, §7) with overlapping detail. Could be tightened.
- §3 has two adjacent paragraphs of mechanical picture (one before the polar-singularity discussion, one after) that are partly redundant.
- §8 calls the entries of *D* "ρ" without restating it is a per-unit-length quantity (it was named in Notation but reintroduction here is brief).

---

## Chapter 2 — Wave on a Single Primitive

### Serious
- **The headline result (M = c² D → ω = c |k|) requires both matched chirality *and* the bare-speed condition K_ee/ρ = K_φφ/I_φ = c², but the chapter presents the result as flowing from matched chirality alone.** §4 says "matched chirality removes any speed difference between polarizations." That is only true when the diagonal bare-speeds already match. Without bare-speed equality, M = c² D fails: the diagonal entries of M and D have different ratios, so M ≠ (constant) · D and the eigenvalue problem retains two distinct propagation speeds. Bare-speed equality is introduced parenthetically and described as something "chapter 3 will identify with the lattice signal speed," but chapter 3 does not derive it — it postulates it. So the chapter's result rests on two postulates, only one of which (matched chirality) is established at the foundation level. The chapter should foreground bare-speed equality as a co-postulate, not slip it in as a definitional aside.

### Moderate
- **"Geometric mean" terminology in §7 is incorrect.** The chapter says "the geometric mean of 0 and 1 — equivalently, the point halfway between them on a logarithmic scale — corresponds to *K_eφ*² being half the way to its stability ceiling." The geometric mean of {0, 1} is √(0 · 1) = 0, not 1/√2. The actual argument is that χ̃² = 1/2 places K_eφ² at the *arithmetic* mean of 0 and the stability ceiling. Since this argument carries the named justification for the natural shear value used in chapter 8, the labeling matters.
- **README inconsistency on χ̃ = 1 boundary.** README still claims "The upper limit χ̃ = 1 is degenerate (wave speed → 0)." Chapter 2 §6 contradicts this: under matched chirality, both modes propagate at *c* throughout the stable range *including the boundary*, because M and D become singular together and their proportionality M = c² D persists. README needs updating.
- **Concept-table mismatch for §5.** Table lists "The two natural modes: how strain and direction combine"; actual heading is "Polarizations: how strain and direction combine in the propagating wave."

### Light
- §1 introduces *T̃* and *Ṽ* as densities by name in body text but the tilde notation isn't called out — a brief sentence would help readers parse it.
- §3's "phasor representation familiar from electrical engineering" aside is fine for an engineering audience but adds little.
- §5's circular-polarization sub-section is informative but unused in subsequent chapters; could be trimmed.

---

## Chapter 3 — Shear and *c*

### Serious
- None.

### Moderate
- **Mixed framing of the bare-speed condition: constraint vs. postulate.** §1 frames it as "the cylinder must propagate waves at speed *c*" — a constraint imposed by the lattice cadence. §2 then describes it as a separate postulated assumption ("we posit it as an assumption of the model, motivated by the same reasoning as matched chirality"). One framing or the other should be picked; the cleanest reading is that we *define* the bare speed as *c* (in the cylinder's microstructure) and then *posit* this equals the lattice signal speed.
- **Open question 1 from README is not directly restated and answered.** The chapter is supposed to settle "Does the lattice signal speed *c* fix χ̃ uniquely?" The answer (no — χ̃ stays free; the constraint pins two stiffness ratios, not χ̃) is implicit in §5's table but never stated as the answer to the open question.

### Light
- §4's simplifying assumption (ρ = I_φ ≡ ρ₀, K_ee = K_φφ ≡ K) is mentioned and tabled, then the general case is waved through with "the same shape with more terms." A brief explicit form for the general case would tighten the chapter.

---

## Chapter 4 — Entropy from Defects

### Serious
- **Coordinate switch from (e, φ) to (ψ_R, ψ_I) is unmotivated and changes the math.** Chapters 1–2 set up the wave equation in (e, φ) coordinates with M coupling K_eφ between polar magnitude and angle gradients. Chapter 4 §4 abruptly says "**u** = (ψ_R, ψ_I)" — Cartesian components — and asserts the same wave equation D ∂_t² **u** = M ∇² **u** carries over. But K_eφ in (e, φ) couples gradient-of-magnitude with gradient-of-angle, which is generally a *nonlinear* expression in (ψ_R, ψ_I). The chapter's static-Laplacian conclusion (that M factors out leaving ∇² ψ = 0 component-wise) requires either (a) a justification that (e, φ) → (ψ_R, ψ_I) preserves the matrix structure — which is not generally true; (b) redefining the field as Cartesian, contradicting chapter 1's polar setup; or (c) a linearization argument around |ψ| ≠ 0 that explains the equivalence. None of these is given. This is a real gap in the chapter's central derivation.
- **The simulations test the Cartesian Laplace equation, not the (e, φ) wave equation.** From `output/result.txt`: inclusions are pinned to "ψ = [1. 0.]", a Cartesian 2-component field. The simulations confirm the Cartesian Laplace equation produces logarithmic decay and 1/r force scaling — clean for what they test. But their relevance to the chapter's claim about the cylinder primitive depends on the unaddressed coordinate-switch question above. As currently written, the simulations show that *if* the cylinder primitive's static problem reduces to a 2D Cartesian Laplace equation, it gives 1/r — but the reduction itself is what's not derived.

### Moderate
- **§5 sign ambiguity.** F(r) = ∓ q₁ q₂ / (2π r) is written with ∓, with sign "depending on the boundary-condition convention." For gravity-analog (always attractive between like sources) the sign should be derivable from the energy expression and pinned, not left to convention.
- **§6 "variance and entropy are monotonically related" is asserted without the explicit relationship.** For a Gaussian, S_local = ½ log(2π e σ²) per mode; the chapter doesn't quote this, leaving the integration step ("integrating the entropy deficit along a curve scales linearly with length") informal.
- **§3 dimensional handwave.** "log *r* is dimensionless if *r* is in some chosen length units, and the constant absorbs the choice of units." More precisely, only log(r/r₀) is dimensionless for any reference scale r₀; the "constant absorbs" framing is loose.

### Light
- §1 uses "1D-area scaling" for what is just "length" (since 2D horizons are curves). Conceptually correct but the phrasing is awkward.
- §8 reports "log 15 ≈ 2.71" without specifying natural log; consistent with the Green's-function derivation (which uses natural log throughout) but a one-word note would prevent confusion.

---

## Chapter 5 — 2D Lattice Assembly

### Serious
- None.

### Moderate
- **§4 Bloch-band claim is asserted, not derived.** "Under matched chirality with M = c² D on every edge, all 6 bands are zone-folded copies of the single dispersion ω = c |**k**|." In general, periodic structures produce band gaps and other features even with uniform local dynamics. The claim that no anomalies arise needs at least a brief structural argument (e.g., that the matched-chirality scalar reduction removes the polarization-mixing terms that would normally drive band gaps). Without this, the conclusion is stipulated.
- **Wye-junction continuity rule is ambiguous in 2D.** §1 says nodes have 3 incident edges and that meeting endpoints have matching (e, φ). But the cylinder's azimuthal direction φ is defined relative to a reference around the cross-section; three cylinders meeting at 120° have three different physical reference frames. Continuity of the underlying ψ vector across the junction is well-defined; continuity of (e, φ) coordinates is frame-dependent. The chapter doesn't specify which is meant.
- **Inherited assumptions not foregrounded.** §3 reuses chapter 2's M = c² D result for the 2D lattice. Acceptable as inheritance, but the chapter could state more explicitly which postulates (matched chirality, bare-speed equality) are inherited and that no new ones are introduced.

### Light
- The "no surprises arise" closing aside in §4 is hand-wavey; could be stated more concretely (or backed by a brief calculation).

---

## Chapter 6 — Bridge to Maxwell

### Serious
- **The "longitudinal/Coulomb component propagates at c" claim in §6 is loose at minimum, and inconsistent with Maxwell at face value.** The chapter says the cylinder primitive's two propagating modes "both propagate at *c* in the unfixed formulation." In standard 2+1D Maxwell, the longitudinal/Coulomb component is *not* a propagating wave even before gauge fixing — it is a constraint-determined non-radiative field. Mapping the cylinder's two equally-propagating modes onto "transverse photon (radiative) + longitudinal/Coulomb (non-radiative)" requires more than the chapter provides; as written, the mapping is asymmetric in a way that contradicts the chapter-5 result that both modes propagate at *c*.

### Moderate
- **Notation collision on "*e*".** §5 writes the gauge-transformation rule as A_μ → A_μ + (1/*e*) ∂_μ χ, where *e* is "the elementary charge from axiom A6, not our *e* field." The chapter flags this ("the notation collision is unfortunate but standard") but uses the formula anyway without disambiguating typographically (e.g., subscripting one or using a distinct symbol). Trips up the reader.
- **§3 identification θ ↔ φ at lattice nodes is by analogy, not derivation.** The chapter asserts the cylinder's azimuthal direction *is* grid/maxwell.md's cell phase θ on the basis of "the right structural properties" (both are angles, both unobservable absolutely). It does not establish that they evolve under the same dynamics or have the same physical interpretation.
- **§4 "A_μ = ∂_μ φ" identification glosses the gauge-connection structure.** A_μ in Maxwell is supposed to come from the *gauge connection* enforcing local invariance under θ → θ + χ; ∂_μ φ is just the spatial gradient of an angle field. Whether ∂_μ φ carries the right transformation law (and the right holonomy structure on closed loops) needs checking, not assertion.

### Light
- The chapter is short; the asserted identifications would benefit from a brief worked example (e.g., a single cylinder with prescribed φ(x, t), showing what θ at each endpoint and A_μ along the edge come out to be).

---

## Chapter 7 — Bridge to Gravity

### Serious
- None.

### Moderate
- **§4's "lattice-geometry factor of 2π/3" is reverse-engineered, but the chapter's own framing softens this.** §1 and §5 explicitly say this chapter is a *consistency check* on an *assumed* ζ_2D = 1/3, not a derivation. Under that framing, §4 is an existence demonstration that *some* lattice-geometry factor of order unity could bridge the continuum coefficient (1/(2π)) to the per-node value (1/3) — i.e., the cylinder primitive does not preclude ζ_2D = 1/3. That is all the chapter actually claims. The remaining issue is just that §4's prose over-promises ("comes out to 2π/3", "matching ζ_2D = 1/3 exactly") in a way the rest of the chapter walks back. The fix is to soften §4's wording to match the consistency-check framing of §1 and §5.
- **The 2D entanglement-entropy log violation.** §8 raises this real concern and defers it to "the natural 3D extension would resolve this" — which is outside the project's scope. This leaves a substantive issue with chapter 4's area-scaling claim un-addressed within the project; worth flagging that it is *deferred*, not resolved.

### Light
- The repeated phrase "structural-form match" is cumbersome; could be tightened.

---

## Chapter 8 — Wrap and α

### Serious
- **The (Δθ)² leading-order formula may not capture the *form* of α at N = 6.** The chapter derives η_kink ≈ K · (Δθ)² as the leading term of a small-Δθ expansion. For N = 6, Δθ = 60° = 1.047 rad — order unity, not small. §9 acknowledges this as a risk but treats it as a precision concern. It is bigger than that: if higher-order terms (Δθ⁴, Δθ⁶, …) are O(1) at this Δθ, the *structural form* η_loop = 4π² K(χ̃) / N is itself missing terms — and the missing terms may not share the 1/N scaling. The chapter's "1 free variable" headline depends on the structural form being right, not just on the value of K. Even under the project's scope (no numerical derivation of α), this concern bears on whether the structural understanding the chapter delivers is reliable.
- **K(χ̃) is treated as a function of χ̃ alone, but this is asserted, not shown.** Step 4 of the §3 calculation outline ("integrate over radiated channels") would in principle determine whether K depends only on χ̃ or also on N (or on the full kink geometry — incoming/outgoing edge directions, lattice orientation, etc.). The chapter assumes K = K(χ̃) so that the clean separation "N from lattice, χ̃ from chapter 2, K from primitive dynamics" holds and α reduces to one free variable. If K turns out to be K(χ̃, N) or carry residual lattice dependence, the "one free variable" claim weakens to "one or more, depending on what K depends on."

### Moderate
- **N = 6 is chosen by hexagonal symmetry but is not pinned by physics.** §9 acknowledges "a MaSt-style charge-bearing torus might have a different *N* set by the particle's specific structure." The "1 free variable" claim depends on N = 6 being correct; if N also varies per particle, α has at least two free parameters (N and K), placing the result in the user's "no insight added" bucket.
- **χ̃ = 1/√2 is treated as pinned, but chapter 2 only identified it as a "natural" midpoint.** Chapter 2 §7 explicitly says "Nothing in chapter 2 alone pins χ̃ to any particular value within (0, 1)." Treating 1/√2 as fixed in chapter 8 is a leap. Combined with the geometric-mean labeling error (Ch2 Moderate), the chapter is using a value whose justification has known issues.
- **§8.5 "Fractal recursion" adds qualitative observations but no mathematical content.** Belongs in an appendix or a chapter footnote rather than mid-chapter.

### Light
- **Section numbering interruption: §8.5.** Either fold §8.5 into §8 or renumber subsequent sections. The "8.5" stop-gap interrupts the section sequence.
- **The 10-significant-figure precision claim for K(1/√2) is misleading.** The CODATA value of α has that precision, but K is derived from a leading-order perturbative expansion at order-unity Δθ; transferring α's precision to K is unjustified.

---

## Chapter 9 — Closing Summary

### Serious
- None directly; the issues here are inherited from earlier chapters.

### Moderate
- **§2 inherits the Ch7 §4 wording.** "Combined with the hexagonal-lattice geometric factor, this gives a per-node entropy of 1/3 — matching ζ_2D structural-form." Under the consistency-check framing this is fine, but the summary should match the softer language of Ch7 §1/§5: "consistent with ζ_2D = 1/3" rather than "matching."
- **§3 "Linear-Gaussian theory carries the entropy account" inherits the Ch4 coordinate-switch issue.** The discovery is real for Cartesian (ψ_R, ψ_I), but the summary doesn't acknowledge that the chapter-2 wave equation was in (e, φ); the equivalence is not established within the project.

### Light
- §6 "Closing thought" has a promotional tone ("That is the project's contribution") that could be tightened.

---

## Cross-cutting issues

A few concerns span multiple chapters and are easier to fix at the project level than within any one chapter:

- **The (e, φ) ↔ (ψ_R, ψ_I) coordinate question.** Threads through chapters 1–6. A single short section establishing exactly when polar and Cartesian formulations are equivalent (linearization regime, role of |ψ| ≠ 0 background, invariance of M and D under change of basis) would close the gap that affects chapter 4 most acutely.
- **Postulates vs. derivations.** Matched chirality (Ch1 §8), bare-speed equality (Ch3 §2), N = 6 (Ch8 §5), χ̃ = 1/√2 (Ch2 §7 / Ch8) are all postulated or "naturally chosen" rather than derived from deeper requirements. The project would benefit from one consolidated table — somewhere in the README or chapter 9 — listing every postulate, its motivation, and what it costs to drop.
- **README drift.** Chapter results have moved past several README claims (slow-mode behavior at χ̃ = 1, the "equipartition" framing reframed as "geometric mean," the entropic mechanism shifted from defects to linear-Gaussian). README should be reconciled with the current chapter contents.
