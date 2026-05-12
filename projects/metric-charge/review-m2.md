# review-m2.md — Review of work-m2.md

## Verdict on the math

**σ = 0 derivation (§2):** Correct and clean. The Christoffel calculation in §2.4 reproduces standard KK Lorentz-force structure (m d²x^μ/dτ² = F^B^μ_ν v^ν p^w) by direct computation, applied to the framework's h_μw cross-term. Properties 1–3 (§§2.1–2.3) are bookkeeping that follows from the framework's existing symmetries. Property 4 is the substantive one and it goes through. This portion converts Ch 5 §4.6's *asserted* four-property claim into *derived*.

**σ ≠ 0 derivation (§3):** Math is computationally correct. For a single Bloch mode at (m, n) with both windings nonzero, T_tu and T_tw are both nonzero, and the four-property test as written runs identically for h_μu and h_μw — both pass. The Christoffel calculation gives m d²x^μ/dτ² = F^A^μ_ν v^ν p^u + F^B^μ_ν v^ν p^w.

**Where work-m2 goes wrong, however, is not the math — it is the framing.** See next section.

## The framework-level error in work-m2

work-m2 runs the four-property gauge-potential test symmetrically on both compact directions (h_μu and h_μw) and reports that both pass, concluding U(1) × U(1). This imports the symmetry implicit in standard KK (which has only *one* compact direction, so the question of which cross-term is "the" gauge potential never arises) without enforcing this framework's structural asymmetry.

This framework has an explicit wrap-order convention (Ch 1 §10):

- **u = ring** (multi-wrap direction, where mass arises from standing-wave structure)
- **w = tube** (single-wrap direction, where charge arises from KK-style traveling-wave structure)

The two compact directions are **not interchangeable**. They play structurally distinct roles in the framework: u carries the closure-quantized standing-wave content (mass), w carries the KK-style traveling-wave content (charge). The four-property test, as a test of *which* cross-term is the gauge potential, should be applied with the wrap-order convention enforced — not symmetrically on both directions as if they were exchangeable.

Under wrap-order enforcement, the question "is h_μu a second gauge potential?" is not answered by running the four-property test on it. It is answered by the convention: h_μu is the mass-direction metric perturbation, structurally distinct from the gauge potential. The four-property test is the *confirmation* that h_μw (the wrap-order-selected gauge candidate) satisfies the standard-physics gauge-potential requirements. It is not a *selection mechanism* between candidates.

work-m2's U(1) × U(1) conclusion follows only if one treats the four-property test as a selection mechanism applied symmetrically to both directions — which is what standard KK implicitly does when there is no asymmetry to break. This framework has the asymmetry, and using it resolves the apparent puzzle.

## The resolution: wrap-order enforcement at the gauge-identification level

The σ = 0 framework currently enforces single-U(1) at the **particle-construction level**: R_u-symmetrization is applied to the natural particle, ⟨p^u⟩ vanishes, the h_μu cross-term mechanically drops out of the geodesic equation. The framework reads off the surviving h_μw as the gauge potential.

This mechanism works at σ = 0 but breaks at σ ≠ 0 because R_u-symmetrization is no longer a particle symmetry under shear (Ch 8 §2.3 interpretation (a) — the single-Bloch-mode commitment — has definite ⟨p^u⟩ ≠ 0).

The proposed resolution is to enforce single-U(1) at the **gauge-identification level** instead:

- h_μw is the gauge potential **by wrap-order convention**, full stop. The four-property test confirms it satisfies standard-physics gauge-potential requirements.
- h_μu is the mass-direction metric perturbation. It is *structurally not* a gauge potential, regardless of whether it would pass a symmetric four-property test in isolation.

This works uniformly at both σ = 0 and σ ≠ 0 — the same convention selects h_μw in both regimes, with no special mechanism required for either.

**Trade-off:** σ = 0 single-U(1) becomes a consequence of an axiom (wrap-order convention) rather than a derivation (R_u-symmetrization plus four-property test). But wrap-order is *already* axiomatic in this framework (Ch 1 §10). What this resolution does is propagate that existing axiom into Ch 5's gauge-identification step explicitly, rather than relying on a particle-level mechanism that happens to produce the same answer at σ = 0 but fails at σ ≠ 0.

R_u-symmetrization is preserved as one realization of the wrap-order convention at σ = 0 — the convention is consistent with R_u-symmetrization where R_u-symmetrization applies, and extends naturally to σ ≠ 0 where it does not.

## Rework instructions for work-m2

The other agent should rework work-m2.md as follows:

1. **Keep §2 (σ = 0 derivation) with light reframing.** The Christoffel calculation and four-property test for h_μw remain. Add a framing note at the start of §2 stating that h_μw is the gauge candidate by wrap-order convention (Ch 1 §10), and the four-property test confirms it satisfies standard-physics gauge-potential requirements. Position the test as *confirmation*, not *selection*.

2. **Rewrite §3 (σ ≠ 0) under the wrap-order framing.** The single-Bloch-mode commitment of Ch 8 §2.2 makes both T_tu and T_tw nonzero. Under wrap-order convention:
   - h_μw is the gauge potential. Run the four-property test on h_μw — it passes (same structure as §2).
   - h_μu is the mass-direction metric perturbation. It is not a gauge-potential candidate. The geodesic equation includes its contribution as a metric-distortion effect on particle motion, not as a Lorentz force from a second gauge field. (Optional: characterize this contribution briefly to clarify what role h_μu plays.)
   - The Christoffel calculation in §3 should explicitly distinguish the F^B^μ_ν v^ν p^w piece (Lorentz force from the gauge potential) from the h_μu contribution (mass-direction metric effect). Do not present the latter as F^A^μ_ν v^ν p^u as if A were a gauge potential.

3. **Drop §4 (U(1) × U(1) statement) and §5 (interpretation (b) alternative).** Under wrap-order enforcement these become unnecessary — there is no U(1) × U(1) puzzle to resolve, and no need for an interpretation (b) workaround. Their content can be deleted, or compressed into a short subsection noting the alternative framings that were considered and superseded.

4. **Replace §6 (three-options recommendation) with unified integration.** The recommendation becomes: integrate the σ = 0 and σ ≠ 0 derivations together under the wrap-order framing into Ch 5 §4.6 (and a brief reference in Ch 8 §2.2 as noted below). No deferral required.

## Implications for the chapters

- **Ch 1 §10 (wrap-order convention):** Add a short connective note explaining that the convention is the labeling of the asymmetry the closure rule (developed in Ch 8 §2.2) will force. The (m, 1) form of closure-satisfying primitives means one winding is always 1 (the KK-traveling-wave direction) and the other is variable m (the multi-wrap standing-wave direction). The wrap-order convention names the variable-m direction "ring" (mass) and the fixed-1 direction "tube" (charge). This makes the convention structure-aligned rather than free choice. A forward pointer to Ch 8 §2.2 is sufficient — the closure rule is developed there, not here.

- **Ch 5 §4 (current single-U(1) derivation):** Reframe the gauge-identification step to invoke the wrap-order convention as the primary selector of h_μw. R_u-symmetrization is preserved as a property of the σ = 0 natural particle that is *consistent with* the wrap-order selection (it makes h_μu mechanically vanish from the geodesic equation in addition to being structurally non-gauge by convention). The Ch 5 §4.6 four-property claim is converted from asserted to derived by importing work-m2 §2's Christoffel calculation.

- **Ch 8 §2.2 (single-Bloch-mode commitment):** Two additions:
  1. Clarify that under the single-Bloch-mode interpretation, h_μu's nonzero contribution from definite ⟨p^u⟩ ≠ 0 is the mass-direction metric perturbation — not a second gauge potential. This is the wrap-order convention applied at the gauge-identification level.
  2. Add a brief note on the status of (m, n) states with n > 1 (tube winding greater than 1): these are off the primitive lattice under the closure rule and read as non-primitive states — harmonic content, composite states, or spatially separated multi-primitive configurations — rather than as a new fundamental sector. This closes the corresponding gap in the framework's treatment of non-primitive sectors and clarifies why the primitive (m, 1) form is the right thing to develop downstream.

- **Ch 9 §5.1 (lepton-like sheet character):** No longer threatened by U(1) × U(1) at large σ. The lepton-like sheet retains single-U(1) character under the wrap-order convention regardless of σ regime. The σ → 1 principal-axis suppression of Ch 9 §3 continues to operate, and the lepton-like single-isolable-charged-primitive framing survives.

## Recommendation

1. Update work-m2.md per the rework instructions in §"Rework instructions for work-m2" above.
2. Integrate the reworked §2 + §3 (now uniform under wrap-order framing) into Ch 5 §4.6 and Ch 8 §2.2 as noted in §"Implications for the chapters."
3. Update STATUS.md to mark TODO-M2 resolved by wrap-order gauge-identification, replacing the prior "extended by Ch 8 refactor to include σ ≠ 0" framing. No TODO-M2b is needed.
4. The work-m2.md content remains valuable as the document that *surfaced* the framing question, even after rework — the original symmetric reading is the natural reading and was worth working through to see that the asymmetry has to be imported explicitly at the gauge-identification step.

The math in work-m2 is settled. The reframing is what is needed, and it makes σ = 0 and σ ≠ 0 a single derivation rather than two cases with different mechanisms.
