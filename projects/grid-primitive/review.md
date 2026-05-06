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
- ~~**Section numbering bug.** Two adjacent sections are both labeled §9: "9. Relationship to the earlier viz model" and "9. What is taken as input from GRID". The latter should be §10 per the concepts table. §11 and §12 then have the right numerical labels but inconsistent counts.~~ **[ADDRESSED]** §9/§10 renumbered.
- ~~**Concept-table mismatch for §4.** Table lists §4 as "Boundedness — why φ is compact and e is not", but the actual §4 heading is "The shape of the field, and what makes entropy possible". The §4 content covers polar/Cartesian framing and winding numbers, not boundedness specifically.~~ **[ADDRESSED]** Concept table updated to match §4's actual content.
- **Polar-vs-Cartesian framing of (e, φ) is ambiguous.** §3 declares *e* a signed magnitude (+ tension, − compression) while φ is an angle mod 2π, then §4 writes ψ_R = *e* cos φ, ψ_I = *e* sin φ — the standard polar→Cartesian map, which assumes *e* ≥ 0 (otherwise (e, φ) and (−e, φ + π) double-cover the same vector). The chapter does not commit to whether (e, φ) are genuine polar coordinates or two independent real fields. (Partially addressed downstream by Ch4's new linearization-around-background paragraph, which clarifies that the chapters work with *fluctuations* around a non-zero ψ₀ — but Ch1's own §3 wording could still be tightened.)
- ~~**A6 listed as input contradicts chapter 8's stated deliverable.** The §10 (numbered "9") "Inputs from GRID" table includes "Coupling α ≈ 1/137 — Axiom A6". README and chapter 8 frame α as a project deliverable (its *form* derived). Treating A6 as input here muddies the input/output boundary.~~ **[ADDRESSED]** Inputs table now distinguishes value (input from A6) from form (chapter 8 — inconclusive).
- **The "matched chirality is the simplest physically motivated choice" justification (§8) overstates.** Even for actual helical-fiber media, PE and KE chirality coefficients need not be identically coupled. The honest framing — which the chapter elsewhere supports — is that matched chirality is a *modeling choice* that prevents the slow-mode tension. The "simplest physically motivated" wording goes beyond that.

### Light
- The "rubber cylinder reinforced with helical fibers" mechanical analog is reused several times (§2, §3, §5, §7) with overlapping detail. Could be tightened.
- §3 has two adjacent paragraphs of mechanical picture (one before the polar-singularity discussion, one after) that are partly redundant.
- §8 calls the entries of *D* "ρ" without restating it is a per-unit-length quantity (it was named in Notation but reintroduction here is brief).

---

## Chapter 2 — Wave on a Single Primitive

### Serious
- ~~**The headline result (M = c² D → ω = c |k|) requires both matched chirality *and* the bare-speed condition K_ee/ρ = K_φφ/I_φ = c², but the chapter presents the result as flowing from matched chirality alone.**~~ **[ADDRESSED]** §4 reorganized so bare-speed equality is foregrounded as a co-postulate alongside matched chirality. §6 and §10 updated accordingly.

### Moderate
- ~~**"Geometric mean" terminology in §7 is incorrect.** The chapter says "the geometric mean of 0 and 1 — equivalently, the point halfway between them on a logarithmic scale — corresponds to *K_eφ*² being half the way to its stability ceiling."~~ **[ADDRESSED]** §7 reframed as the *arithmetic-midpoint* of K_eφ², with a historical note explaining the prior mislabelings.
- ~~**README inconsistency on χ̃ = 1 boundary.** README still claims "The upper limit χ̃ = 1 is degenerate (wave speed → 0)."~~ **[ADDRESSED]** README theory 3 updated to reflect that under matched chirality + bare-speed equality, both modes propagate at *c* throughout the stable range including the boundary.
- ~~**Concept-table mismatch for §5.** Table lists "The two natural modes: how strain and direction combine"; actual heading is "Polarizations: how strain and direction combine in the propagating wave."~~ **[ADDRESSED]** Concept table updated.

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
- ~~**Coordinate switch from (e, φ) to (ψ_R, ψ_I) is unmotivated and changes the math.**~~ **[ADDRESSED]** §4 now opens with "A note on coordinates: linearization around a non-zero background" that establishes (i) the chapter linearizes around ψ₀ ≠ 0, (ii) (δe, δφ) ↔ (δψ_R, δψ_I) is a tangent-space basis change, (iii) the static-Laplacian argument is basis-independent because M is invertible in either basis.
- ~~**The simulations test the Cartesian Laplace equation, not the (e, φ) wave equation.**~~ **[ADDRESSED]** The same §4 paragraph notes that pinning ψ = (1, 0) at an inclusion is exactly the kind of non-zero background the linearization needs, so the simulations are testing the right linearized regime.

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
- ~~**Wye-junction continuity rule is ambiguous in 2D.** §1 says nodes have 3 incident edges and that meeting endpoints have matching (e, φ). But the cylinder's azimuthal direction φ is defined relative to a reference around the cross-section; three cylinders meeting at 120° have three different physical reference frames.~~ **[ADDRESSED]** §1 now contains a "Continuity at a wye junction" paragraph specifying that continuity is on the underlying ψ vector in a shared lab frame, with each cylinder's local-frame (e, φ) determined by the standard rotation between local frame and lab frame.
- **Inherited assumptions not foregrounded.** §3 reuses chapter 2's M = c² D result for the 2D lattice. Acceptable as inheritance, but the chapter could state more explicitly which postulates (matched chirality, bare-speed equality) are inherited and that no new ones are introduced.

### Light
- The "no surprises arise" closing aside in §4 is hand-wavey; could be stated more concretely (or backed by a brief calculation).

---

## Chapter 6 — Bridge to Maxwell

### Serious
- ~~**The "longitudinal/Coulomb component propagates at c" claim in §6 is loose at minimum, and inconsistent with Maxwell at face value.**~~ **[ADDRESSED]** §6 rewritten. The cylinder's two propagating modes are now read as the analogs of the *two transverse polarizations* of a 3+1D photon (not "transverse + Coulomb in 2+1D"). The Coulomb sector is acknowledged as missing from the 2D restriction and deferred to the 3D extension. Summary in §8 updated to match.

### Moderate
- ~~**Notation collision on "*e*".**~~ **[ADDRESSED]** §5 now uses *q* for the elementary charge in the gauge formula, eliminating the collision with the cylinder's *e* field.
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
- ~~**The (Δθ)² leading-order formula may not capture the *form* of α at N = 6.**~~ **[ADDRESSED]** Chapter rewritten for honesty: §4 now contains a "Warning 1 — the small-Δθ expansion is not controlled at N = 6" subsection that lays out the higher-order series and shows the natural expansion parameter is order unity. §6, §7, §10, and the chapter intro mark all leading-order expressions as conditional and explicitly walk back the "1 free variable" headline.
- ~~**K(χ̃) is treated as a function of χ̃ alone, but this is asserted, not shown.**~~ **[ADDRESSED]** Listed as an explicit limitation in the new §10 (formerly §9 "Risks"), and the §6/§7 discussion no longer treats the "K depends only on χ̃" assumption as established.

### Moderate
- ~~**N = 6 is chosen by hexagonal symmetry but is not pinned by physics.**~~ Listed as an explicit limitation in §10.
- ~~**χ̃ = 1/√2 is treated as pinned, but chapter 2 only identified it as a "natural" midpoint.**~~ Listed as an explicit limitation in §10; chapter now uses "tentatively at the natural midpoint" language and references Ch2 §7's arithmetic-midpoint argument.
- ~~**§8.5 "Fractal recursion" adds qualitative observations but no mathematical content.**~~ Section renumbered to §9, kept (it's brief and helpful), and tightened.

### Light
- ~~**Section numbering interruption: §8.5.**~~ **[ADDRESSED]** Renumbered to §9, with §9 "Limitations" → §10 and §10 "Summary" → §11.
- ~~**The 10-significant-figure precision claim for K(1/√2) is misleading.**~~ **[ADDRESSED]** Removed entirely; chapter no longer back-outs a numerical K(1/√2) from α.

---

## Chapter 9 — Closing Summary

### Serious
- None directly; the issues here are inherited from earlier chapters.

### Moderate
- **§2 inherits the Ch7 §4 wording.** "Combined with the hexagonal-lattice geometric factor, this gives a per-node entropy of 1/3 — matching ζ_2D structural-form." Under the consistency-check framing this is fine, but the summary should match the softer language of Ch7 §1/§5: "consistent with ζ_2D = 1/3" rather than "matching."
- **§3 "Linear-Gaussian theory carries the entropy account" inherits the Ch4 coordinate-switch issue.** Partially addressed by Ch4's new linearization-around-background paragraph; the Ch9 §3 summary could be tightened to reference that paragraph explicitly.

### Light
- §6 "Closing thought" has a promotional tone that could be tightened. Already partly walked back when Ch9 was updated for the Ch8 reframing; further tightening is possible.

---

## Cross-cutting issues

A few concerns span multiple chapters and are easier to fix at the project level than within any one chapter:

- ~~**The (e, φ) ↔ (ψ_R, ψ_I) coordinate question.**~~ **[ADDRESSED]** Closed by Ch4 §4's new linearization-around-background paragraph: linearization around ψ₀ ≠ 0 is the regime, the (δe, δφ) ↔ (δψ_R, δψ_I) map is a tangent-space basis change, M is invertible in either basis, the static Laplacian factors out either way.
- **Postulates vs. derivations.** Matched chirality (Ch1 §8), bare-speed equality (Ch2 §4 / Ch3 §2), N = 6 (Ch8 §5), χ̃ = 1/√2 (Ch2 §7 / Ch8) are all postulated or "naturally chosen" rather than derived from deeper requirements. README theory 6 now lists matched chirality + bare-speed equality together as the foundation-level commitments; a fully consolidated table is no longer urgent but would still tighten the project.
- ~~**README drift.**~~ **[ADDRESSED]** README theories 3, 4, 6, 10 reconciled with current chapter contents (no more "wave speed → 0", no more "equipartition / geometric mean" labeling, bare-speed equality named alongside matched chirality, chapter 8 framing corrected to "inconclusive").
