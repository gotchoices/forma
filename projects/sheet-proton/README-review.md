# README review — sheet-proton

Critical comments on the project README. Grouped by severity. Each item cites the lines / sections involved and proposes a specific fix where one is clear.

---

## A. Errors and contradictions

### A1. Project-status contradiction (critical)

The README's status line (line 6) reads:

> **Status:** Active. Work files have converged on the **modulated-clover construction** …

But [work/STATUS.md](work/STATUS.md) line 5 reads:

> **Project state:** **On hold** as of 2026-05-16. The dim-sharing reframe explored in 3-torus.md and ma-share.md (both since moved to [ma-domain](../ma-domain/)) suggested that the three-sheet architecture should be reconceived as a single multi-dim Ma domain with sparse cross-terms.

These are flatly incompatible. A reader reaching the README first will assume the project is in active development; reaching STATUS.md they will assume the opposite. One of the two needs to be updated. If sheet-proton has resumed (the README has been substantially rewritten around the modulated-clover construction since the hold), STATUS.md needs an explicit "resumed on YYYY-MM-DD" annotation. If the project is still on hold but the README documents the pre-hold settled state, the README status line needs to say so.

### A2. Twist value: README's τ = 1/2 vs STATUS's "settled τ = 1/3"

The README repeatedly commits to the half-twist τ = 1/2 modulated-clover as the operative geometry (lines 83, 87, 110, 116, 202–208, 334, 339). STATUS.md, however, contains:

> **Is τ = 1/3 tunable or forced?** … τ = 1/3 is therefore "forced" once we commit to the 3-lobe / 3-saddle profile structure. **Settled.** (line 168)

If the modulated-clover construction supersedes the τ = 1/3 forcing argument, the README should explicitly say *why* τ = 1/2 supersedes τ = 1/3 — i.e., what changed between the two pictures (probably: that the half-twist allows the (1/2, 1) tracks to close in one ring revolution under a different surface identification than the full-twist construction assumed). As written, the reader sees two "settled" answers to the same question.

### A3. "Q = +1, Q = 0 exactly" overstates what is derived

Several passages claim the integer baryon charges are recovered *exactly* (lines 6, 121, 264, 276–278, 336). Reading the substrate work file:

> [modulated-clover.md] The **integer baryon charges** are recovered as a 2-condition tuning of the modulation (sin- and cos-harmonics → Q_p − Q_n = 1 and Q_p + Q_n = 1), not as a forced consequence of the static cross-section.

So the integer charges come from a 2-parameter *fit* to the targets +1 and 0, not from a derivation of those targets. The README should distinguish "matched exactly by tuning two modulation amplitudes" from "derived exactly from the geometry." As written, the wording suggests the latter when only the former is the case.

### A4. "Mass ratio matched exactly at R_major ≈ 36.17" obscures that R_major is fit, not predicted

Lines 6, 140–141, and 169 use "matched exactly" / "matches m_n/m_p exactly" framing for the mass ratio. [modulated-clover.md] is more candid:

> The path-length mechanism … gets the mass-difference sign for free … But the ratio's *magnitude* is a one-parameter fit (the charge-neutral ring aspect ratio), not a prediction.

The README should adopt the work file's clearer framing: *the sign of m_n − m_p is forced; the magnitude requires R_major as a fit parameter.* The current phrasing "matched exactly at R_major ≈ 36.17" reads as a prediction.

### A5. "Color = which Z₃ phase track" conflates structural analog with the gauge group

Lines 117, 136, 290–296, 338 identify "color" with the substrate's discrete Z₃ symmetry orbits. QCD color is the gauge group SU(3), continuous and 8-generator, not the discrete Z₃ ⊂ SU(3). This distinction has been raised explicitly elsewhere in the framework (metric-charge Ch 11 review item 2: "structural analog of color confinement" vs "color SU(3)"). The README should either:

- Adopt the same hedged language used in metric-charge Ch 11 ("structural analog of color confinement," "Z₃ structural analog of color"), or
- State explicitly that the framework reads color as the Z₃ orbit, with the relationship to full SU(3) gauge structure deferred / open.

As written, the identification reads as if SU(3) gauge theory has been recovered from a Z₃ orbit, which it has not.

---

## B. Substantive omissions

### B1. C1–C6 + G1 hypotheses are cited but never enumerated

The status line and lines 78–80 commit the construction to "C1–C6 + G1." A reader needs to chase to [work/derived-clover.md §C1–C6](work/derived-clover.md) to find what those are. For a README that is meant to be the project's entry point, a one-line summary of each hypothesis would let a reader understand the construction's commitments without leaving the page.

Suggested: a short table after §"Why this project exists" listing C1 (substrate topology = T²), C2 (cross-section 3-fold symmetry from color), C3 (half-twist from spin → half-integer t-winding), C4 (ring-axis Z₃), C5 (per-arc curvature = charge density under G1), C6 (proton/neutron = two (1/2, 1) tracks).

### B2. The "(1/2, 1) winding outside standard closure" foundational gap is not mentioned

The construction's central object is the (1/2, 1) torus knot. [modulated-clover.md] explicitly flags:

> The half-integer tube winding of the (1/2, 1) tracks sits outside the standard closure-mode derivation — a real foundational gap (open question 1 in §6).

This is the single most important caveat about the construction — the tracks the framework identifies with the proton and neutron are *not* closure-satisfying modes in the sense metric-charge Ch 4 established. The README's "Open questions inside the construction's scope" section (lines 148–162) lists two questions but omits this one entirely. It should be the first item, not absent.

### B3. "Coordinates and notation" advertises (ε, σ_uw) that the project does not actually use

Lines 33–47 introduce the coordinate table (t, S₁, S₂, u, w, ε, σ_uw, (m, n)) inherited from metric-charge, then immediately (lines 43–51) clarify that "the modulated-clover construction this project develops works in a different parameterisation (cross-section harmonic content + R_major + modulation amplitudes)." The actual operative parameters — a₁(θ), b₁(θ), R_major, the modulation harmonics — never appear in any table.

This is backwards. The inherited (ε, σ_uw) parameterisation is a historical precedent the project no longer uses; the modulated-clover parameters are what matter for everything from Chapter 2 onward. The Coordinates table should lead with the modulated-clover parameters and demote (ε, σ_uw) to a footnote about the predecessor framework.

### B4. Mass formula m = 2πℏc/L_track is asserted without derivation or citation

Line 140 introduces the mass mechanism as "Path-length: m = 2πℏc/L_track" with no explanation of why path length gives mass via this specific relation. For a project where mass is one of two main empirical anchors (the other being charge), and for the project's stated college-engineering audience (per [../CLAUDE.md](../CLAUDE.md)), this needs at minimum a one-line gloss ("treating the closed track as a standing wave with wavelength = L_track, the de Broglie / Compton relation gives m = 2πℏc/L_track") and a cross-reference to where the relation is derived (metric-mass? metric-charge? a work file?).

### B5. Wave-on-substrate vs particle-on-track reconciliation is asserted but not derived

Lines 250–254 and the LB section (lines 304–329) acknowledge a real tension: the LB computation shows the wave-quantum's amplitude is *not* track-localised, yet the per-arc charge integral is taken *along* a track. The README resolves this by asserting that the per-arc integral is "Berry-phase-like" — "determined by how the cross-section tangent winds, not by where the wave's amplitude sits."

This is a strong structural claim and the README should either:

- Cite the work file where the Berry-phase-style identification is set up and verified (lb-mode-localization.md is mentioned for the negative LB result, but not for the Berry-phase reframe), or
- Flag this as an open structural question rather than asserting it as settled.

As written, a reader is asked to accept that "wave-quantum with global amplitude carries along-the-track charge content" without machinery to support that claim. The metric-charge Ch 11 framework provides G1 as the per-arc integration *hypothesis*; the Berry-phase reading is an additional claim on top of G1, not a consequence of it.

### B6. The R_major ≈ 36.17 fit's absolute scale is not connected to physical units

Line 141: "R_major remains the one free parameter the framework does not yet derive." Line 168: "Absolute baryon mass scale. R_major is a free parameter; the construction matches m_n/m_p but not m_p itself."

But R_major ≈ 36.17 *what*? In what units is this dimensionless number? The project clearly intends ring radius in tube-radius units (or some such), but the README never says. A reader cannot evaluate the claim "R_major ≈ 36.17 fits the mass ratio" without knowing what's being measured against what. A short note on the dimensionalisation would help.

---

## C. Framing concerns

### C1. "Theories that have converged" is presented as a goal

Section structure under "Goals" (lines 67–208):

1. Overriding goal — forward-looking ✓
2. Generation-agnostic form, generation-specific parameters — descriptive
3. **Theories that have converged** — these are *results*, not goals
4. Open questions inside the construction's scope — descriptive
5. What we don't predict — descriptive limitations
6. Handoff to ma-domain — descriptive

Only items 1 and 2 are properly goals. Items 3–6 are project state. The "Goals" header is misleading. Suggested restructure: split into "Goals" (1, 2) and "Status of the construction" (3–6).

### C2. "Theories that have converged" claim is weakly supported in places

Item 4 of "Theories that have converged" (lines 123–132) states quark substructure has converged. But [work/STATUS.md] line 134 describes the Wannier work as "**exploratory record** (demoted 2026-05-26)" and notes that the Wannier construction "agreed with the simpler '3 arc-pieces in series' picture *without adding new predictive content*." If the more sophisticated machinery (Wannier) did not add predictive content, the simpler picture remains untested at the level of distinguishing predictions from alternatives. "Converged" overstates this.

Item 6 (mass mechanism, lines 139–141) claims "The mass ratio m_n/m_p is matched exactly at R_major ≈ 36.17." This is a one-parameter fit (see A4 above). Calling a fit "converged" is fine in the sense that the fit value has stabilised, but a reader will read "converged" as "predictive validation."

### C3. The "smeared per-arc charge" framed as structural prediction is questionable

Lines 128–132, 283–287, and 336 frame the smooth-substrate per-arc charges (~+0.59, ~−0.26) as a "structural prediction" of the framework. There are two concerns:

- The standard-model values (+2/3, −1/3) are very well established empirically (deep inelastic scattering, R-ratio, parton distributions, etc.). Framing the smooth-substrate values as a *prediction* of the framework, which by implication competes with the standard-model values, is a strong claim that needs more support than "the smooth substrate gives these numbers."

- The phrase "structural prediction rather than a fit failure" reads as if the framework is *defending* the smooth values against a perceived empirical mismatch. A more honest framing: "the framework's per-arc reading on the smooth substrate does not equal the standard-model fractional charges; the relationship between the smooth-substrate values and the empirical ±2/3, ∓1/3 values is open."

This is the kind of "parameterisation artifact reported as structural finding" caveat that has come up in other project reviews; the README should adopt the same care here.

### C4. The framework's inheritance graph is broader than the rules state

Ground rule 1 (line 55) names metric-charge and metric-binding as the inheritance sources. But the README also cites:

- grid-duality (line 213, 217) — for substrate framework, α-coupling
- metric-mass (line 215) — for single-compact-dimension precursor
- ma-domain (line 218) — for downstream multi-generation framework

The ground rules should either expand to acknowledge the full inheritance chain or the README body should not cite the additional projects as if they were already in the inheritance set.

---

## D. Minor issues

### D1. Internal section ordering

The "Why this project exists" section (lines 8–27) ends with an empirical anchor list. The "Background reading" section (lines 210–228) gives the foundational-project list. These two sections are doing similar work (setting context) and would read better adjacent, with empirical anchors clearly separated from architectural lineage.

### D2. Several work files referenced but not described

Lines 230–232 say "See work/ for active explorations. work/STATUS.md tracks the current state of each file." But work/ contains 16 files (per the listing), and the README cites about 8 of them in passing. A reader has no map of which work files are foundational, which are deprecated, and which are exploratory. Even a short index in the README — "modulated-clover.md is the current operative construction; clover-quarks.md is the predecessor superseded by it; lb-mode-localization.md is a negative result; quark-wannier-decomposition.md is demoted to exploratory" — would orient a new reader substantially.

### D3. "Possible appendix (if useful)" leaves the chapter arc unsettled

Lines 341–343 end with a hedged "Possible appendix (if useful): A. Closed-form analytical machinery." Either it's part of the arc (commit) or it isn't (drop). The current phrasing makes the arc feel unfinished.

### D4. The "Framing — one wave-quantum per baryon" section sits inside "Chapter arc"

Lines 243–329 are extensive framing prose nominally introducing the chapter arc table at line 331. This material is doing substantive setup work and would read better as a top-level section ("§ Framing") before "Chapter arc," with the table itself being the chapter arc's only content.

---

## Summary

The README is doing a lot of work — orienting a reader to a complex construction across multiple sibling projects, naming hypotheses, declaring scope, and previewing seven chapters. The most important fixes are:

1. **Reconcile the README's "Active" status with STATUS.md's "On hold."** (A1)
2. **Stop using "exactly" for results that are tuned fits.** (A3, A4)
3. **List the C1–C6 hypotheses inline.** (B1)
4. **Flag the (1/2, 1)-winding foundational gap.** (B2)
5. **Adopt the same hedged language for color as for the metric-charge Ch 11 SU(N) discussion.** (A5, C3)
6. **Restructure "Goals" so results don't sit under a forward-looking header.** (C1)

The smaller items (B3–B6, C2, D1–D4) can wait but accumulate to a noticeably more navigable document if addressed.

The project's core construction (modulated-clover, per-arc charges, path-length masses, Z₂ × Z₃ symmetry) is substantive and worth presenting carefully. The README's current framing tends to over-claim ("exactly," "converged," "structural prediction") in ways that the underlying work files themselves do not. Aligning the README's tone with the work files' more candid framing would strengthen the project's standing rather than weaken it.
