# standing-wave-vs-mediator.md — particle/mediator distinction

**Status:** Exploratory work file. Develops the structural distinction between *particles* (directionless standing waves, localized) and *mediators* (propagating waves, directional, ranged) within the MaSt framework. Foundational for [strong.md](../../sheet-proton/work/strong.md) and the wave-only reading of force mediation.

**Tone:** Conceptual / foundational. Less computation-heavy than the other work files; more about getting the framework's vocabulary right.

---

## 1. The question

The MaSt framework's emerging wave-only reading distinguishes between two kinds of mode:

- **Particles** are *standing waves* — directionless, localized, with definite (m, n) winding. The construction in [metric-mass chapter 5](../../metric-mass/05-metric-self-consistency.md) argues this is *structural*: a particle on a compact internal coordinate shouldn't have a built-in direction of propagation around the loop.

- **Mediators** are *propagating waves* — directional, ranged, carrying interactions between particles. The pion in [strong.md](../../sheet-proton/work/strong.md)'s Yukawa picture is a mediator; it has a Compton wavelength λ that sets the range of the force it mediates.

These two kinds of mode are *different* — they satisfy different boundary conditions and have different roles in the framework. But they live on the same substrate (the sheet) and obey the same underlying wave equation.

**The question:** what's the mathematical distinction between them, and how do they couple to each other?

---

## 2. The structural setup

Both particles and mediators are solutions of the wave equation on the sheet. The wave equation is:

<!-- (∂²/∂t² − c²∇²)φ = 0 (free), with appropriate boundary conditions on the sheet -->
$$
\bigl(\partial_t^2 - c^2\, \nabla^2\bigr)\varphi \;=\; 0
$$

(or its generalization with the sheet's metric). The same equation admits different *kinds* of solution depending on boundary conditions and spatial extent:

| Property | Particle (standing wave) | Mediator (propagating wave) |
|---|---|---|
| Direction of propagation around loop | Both ways equally (±n superposition) | Single direction (or freely radiating) |
| Spatial extent | Localized (envelope falls off) | Extended (propagates outward) |
| Energy | E = mc² + KE (finite, fixed) | Carried in flight; transient |
| Boundary condition | Standing-wave (closes on the compact direction) | Outgoing or incoming |
| Lifetime | Persistent | Travels from source to sink |

These are different *modes* of the same field. A particle is a mode that doesn't propagate (in the compact-direction sense); a mediator is a mode that does.

---

## 3. The mathematical distinction

In standard QFT, the distinction between "real particles" and "virtual particles" (which are what mediates forces in Feynman-diagram language) is:
- Real particle: on-shell (E² = (pc)² + (mc²)²)
- Virtual particle: off-shell, mathematically convenient

In MaSt's wave reading, "virtual particle" isn't quite the right concept because there's no need to quantize the field — particles and mediators are both classical wave modes. The distinction is more like:
- Particle: localized, persistent, energy-momentum conserved within its envelope
- Mediator: propagating, source-and-sink-coupled, carries energy from source to sink

The boundary conditions differ:
- Particle: bound by its own self-binding (it doesn't fly apart)
- Mediator: bound only by its source-and-sink (it would propagate freely without them)

---

## 4. The coupling between them

When a particle emits or absorbs a mediator, what's actually happening?

In the wave reading: a particle's standing-wave envelope perturbs the surrounding field. The perturbation propagates as a mediator wave. A second particle's standing-wave envelope absorbs the perturbation.

Mathematically:
1. The first particle's source term (the standing wave's amplitude) couples to the free wave equation
2. A small perturbation propagates outward
3. The second particle's location is reached by the perturbation
4. The second particle's standing wave is modified

This is essentially classical Green's-function propagation: a source at one point produces a field at another point, with the propagator determining the range and shape of the effect.

For a Yukawa propagator: the source-field response has the form

<!-- G(r) = exp(-r/λ) / (4π r) -->
$$
G(r) \;=\; \frac{e^{-r/\lambda}}{4\pi r}
$$

The range λ comes from the mediator's mass (Compton wavelength). The 1/r is from 3D spatial dispersion. The exponential decay is from the mediator's mass causing it to oscillate at frequency ω = mc²/ℏ over distances of λ.

So the coupling between particles and mediators is just classical wave propagation with appropriate source terms.

---

## 5. Key questions

1. **Why are particles directionless but mediators directional?** Boundary conditions. A particle's wave is bound to a compact internal coordinate; the standing-wave construction is structural (per chapter 5). A mediator's wave propagates in extended spatial direction; it has a definite (E, p) and a definite direction. Both follow from the boundary conditions, not from any intrinsic difference.

2. **Can the same mode be both a particle and a mediator?** Possibly. A pion in QCD is observed as a "real particle" (deuteron decay produces real pions) and as a "virtual mediator" (Yukawa exchange). In MaSt: a pion is a 2-component qq̄ standing wave when seen on its own (particle); the same mode propagates between nucleons when sourced (mediator). The dual role isn't paradoxical; it's just two boundary-condition contexts for the same wave mode.

3. **How does the mediator coupling depend on the particle's standing-wave structure?** The mediator's emission rate depends on the source's *coupling* to the mediator field. For a charged particle and a photon, the coupling is α. For a nucleon and a pion, the coupling is g (the pion-nucleon coupling, ~13 in QCD). What determines g in MaSt? Presumably the overlap of the mediator's mode with the source's standing-wave structure. **TODO:** formalize this.

4. **Does the mediator wave have a "ground state"?** In QFT, the vacuum is the ground state of all fields. In MaSt, with no Quantization-of-fields machinery, what's the equivalent? Probably: zero amplitude of all modes; the field is "off" with no sources or excitations.

5. **What's the relationship to the dispersion relation?** Both particles and mediators must satisfy the wave equation, so both must lie on the dispersion ω² = c²(k_S² + (n/R_u)²). For a particle: k_S = 0 (rest frame), so ω = c|n|/R_u = m_n c²/ℏ. For a mediator: k_S ≠ 0, and ω relates to k_S via the dispersion. So mediators have non-zero spatial momentum, in contrast to particles which (at rest) have only compact-direction momentum.

---

## 6. Connection to QFT particle/field duality

In QFT, the field-mode framework treats every excitation of the field as a "particle" — both bound states and propagating quanta. The distinction between "real particle" and "virtual particle" is operational (a real particle satisfies dispersion exactly; a virtual one doesn't have to).

MaSt's particle/mediator distinction is similar but more structural:
- "Real particle" in QFT = standing-wave mode in MaSt (bound, on-shell, real-valued)
- "Virtual particle" in QFT = mediator-wave-mode in MaSt (propagating, on-shell, carrying interaction)

The structural difference: MaSt explicitly distinguishes the two kinds at the wave-equation level. QFT treats them as different boundary conditions of the same field.

This is honest about the wave-only reading: there are no "virtual particles" in MaSt; there are mediator waves with source-and-sink boundary conditions. The framework can describe interaction physics in classical-wave language without invoking QFT machinery.

---

## 7. Computational implications

Once the particle/mediator distinction is formalized, several things become computable:

1. **Mediator-emission rate from a particle.** Given a particle's standing-wave amplitude and the mediator's coupling, compute the rate of mediator emission. This determines force strength.

2. **Force law from mediator exchange.** Given the mediator's Compton wavelength and coupling strength, derive the static Yukawa potential V(r). This is what [strong.md](../../sheet-proton/work/strong.md) needs.

3. **Mediator absorption by a target particle.** Given the source-mediated field at the target's location, compute the target's response (energy shift, momentum kick).

4. **Scattering amplitudes.** Particle-particle scattering via mediator exchange follows from the source-propagator-sink structure.

These are all standard Green's-function calculations. The MaSt-specific input is the mediator's mass (determined by its standing-wave structure on the sheet) and the source coupling (determined by overlap with the particle's standing wave).

---

## 8. Cross-references

- [metric-mass chapter 5](../../metric-mass/05-metric-self-consistency.md) — standing-wave particle commitment; the directionless construction
- [strong.md](../../sheet-proton/work/strong.md) — Yukawa mediator picture, depends on the particle/mediator distinction
- [meson-spectrum.md](../../sheet-proton/work/meson-spectrum.md) — mesons can be either particles (observed) or mediators (exchange); the dual role
- [primers/maxwell-primer.md](../../../primers/maxwell-primer.md) — Maxwell's equations and photon propagation; classical wave reading of EM mediation
- [primers/kaluza-klein.md](../../../primers/kaluza-klein.md) — KK photon as compact-dimension excitation

## 9. Next actions

1. Formalize the boundary-condition distinction between particle and mediator solutions of the wave equation on the sheet.
2. Compute the coupling between a particle's standing wave and a mediator's propagating wave (overlap integral).
3. Use this to derive the source-mediated force-law form (Yukawa V(r)) from first principles.
4. Feed result into [strong.md](../../sheet-proton/work/strong.md) for the Yukawa-mediator path.

## 10. Promotion candidate

If this work file matures, the particle/mediator distinction probably warrants promotion to a *primer* rather than living in metric-binding's work files. It's foundational across the whole framework (relevant to metric-charge, metric-binding, and beyond). The work file is the development scratchpad; the primer is the eventual settled vocabulary.
