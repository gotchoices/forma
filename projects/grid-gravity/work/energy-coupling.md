# The detour coupling: is δn ∝ energy? — a derivation

**Status:** Derivation. Applies the micro-to-macro method
([micro-to-macro.md](micro-to-macro.md)) to the detour rule
([detour-refractive.md](detour-refractive.md)) to settle the two open
validity questions: (a) is the refractive perturbation δn ∝ mass-**energy**
(→ universal gravity), and (b) is it non-dispersive with a mode spectrum?

Outcome: the detour mechanism **is** a Lorentz-oscillator dielectric with the
mass as the resonant oscillator. Both questions resolve favourably in the
relevant direction; one scaling detail (across masses) is entangled with the
sheet geometry and is deferred.

Grades: **[derived]**, **[plausible]** (well-motivated reading), **[open]**.

---

## 1. The coupling, explicitly

At the shared node n₀, two fields meet:
- the **passing wave** ψ (a spatial wave, frequency ω, small amplitude a — the
  "sub-quantum" probe);
- the **compact standing wave** φ (the mass — a resonant oscillator at
  ω₀ = ω_Compton, amplitude A).

**Parametric coupling [plausible].** By resonance-gating (D1) there is *no*
coupling without the standing wave; the standing wave *enables* sub-quantum
coupling, so the coupling strength is proportional to its amplitude:

<!-- G ∝ A -->
$$
G \;\propto\; A .
$$

(If the coupling were independent of A, an infinitesimal standing wave would
couple fully — contradicting the gated, sub-quantum picture. G ∝ A is the
natural reading.)

## 2. The coupled-oscillator response → a Lorentz dielectric [derived]

The compact oscillator is driven by the passing wave at the shared node:

<!-- phi'' + omega_0^2 phi = G psi -->
$$
\ddot\varphi + \omega_0^2\,\varphi = G\,\psi
\quad\Rightarrow\quad
\varphi(\omega) = \frac{G\,\psi}{\omega_0^2 - \omega^2}.
$$

The oscillator's response feeds **back** onto the passing wave at n₀ (the
detour: in, then out). This back-reaction is **second order in the coupling**
— one factor of G to go in, one to come back:

<!-- Sigma(omega) = G^2 / (omega_0^2 - omega^2) -->
$$
\Sigma(\omega) \;=\; \frac{G^2}{\omega_0^2 - \omega^2}.
$$

With a density ρ of such oscillators (standing waves), the passing wave's
effective index is

<!-- n^2(omega) = 1 + rho G^2 / (omega_0^2 - omega^2) -->
$$
\boxed{\,n^2(\omega) \;=\; 1 + \frac{\rho\,G^2}{\omega_0^2 - \omega^2}\,}
$$

This is **exactly the Lorentz-oscillator model of a dielectric** — the
standard microscopic theory of a refractive medium, with the mass playing the
role of the resonant oscillator. The detour picture is not an analogy to
optical-metric gravity; it *is* the Lorentz dielectric that underlies it.

## 3. Result (a): δn ∝ energy → universal gravity [derived, in the amplitude direction]

Read off the refractive perturbation (ω ≪ ω₀):

<!-- delta n ~ rho G^2 / (2 omega_0^2) ∝ rho A^2 / omega_0^2 -->
$$
\delta n \;\approx\; \frac{\rho\,G^2}{2\,\omega_0^2}
\;\propto\; \frac{\rho\,A^2}{\omega_0^2}.
$$

Because the back-reaction is second order, **δn ∝ G² ∝ A²** — and A² is the
**energy** of the standing wave. So, at fixed particle type (fixed ω₀):

> **δn ∝ ρ·A² = the standing-wave energy density.**

This is the energy-coupling gravity needs: piling up more of the same energy
(more amplitude, more quanta, coherently or incoherently) raises δn
*linearly* in energy. Feeding into the loop-unification result
([loops-and-range.md](loops-and-range.md)) — a scalar source spread by the
massless lattice operator — gives

<!-- grad^2 q = -kappa rho_E  ->  q ∝ M/r -->
$$
\nabla^2 q = -\,\kappa\,\rho_E \quad\Rightarrow\quad q \propto M/r,
$$

Newtonian, **universal** (couples to energy, not charge or species), from the
detour rule. The parametric coupling (G ∝ A) and the round-trip (second
order) are *why* it lands on energy rather than amplitude — the linear-vs-
quadratic question that could have sunk the mechanism comes out quadratic,
i.e. energy.

## 4. Result (b): non-dispersive for ω ≪ ω₀ — but NOT for the clock sector [derived, with a load-bearing caveat]

**Caveat first (review §1, §6).** A Lorentz oscillator is the paradigm
*dispersive* medium; the flatness below is only asymptotic (ω ≪ ω₀), with
corrections O((ω/ω₀)²). This is fine for *passing light* → bending. But the
object whose rate defines proper time is, by this project's own thesis,
**confined light at ω = ω_Compton** — it sits *at* the resonance, where the
ω ≪ ω₀ expansion and the Kapitza time-average both break down. So "it is time
dilation, not an optical medium" holds only for clocks with ω_clock ≪ ω₀
(practical clocks — atomic ~eV ≪ Compton ~MeV — so the deviation is tiny),
**not as exact universality for every clock**. The equivalence-principle claim
is therefore approximate here, not exact — a crux to confront, not a
coefficient detail.

With that caveat, from the Lorentz form, for ω ≪ ω₀:

<!-- n^2 -> 1 + rho G^2/omega_0^2 = const -->
$$
n^2(\omega) \;\to\; 1 + \frac{\rho\,G^2}{\omega_0^2} = \text{const}.
$$

The index is **frequency-independent** far below resonance — the textbook
low-frequency limit of a dielectric. **Non-dispersive.** A 2D sheet with a
mode spectrum {ω_j} contributes a *sum* of Lorentz terms,

<!-- n^2 = 1 + sum_j rho_j G_j^2 / (omega_j^2 - omega^2) -->
$$
n^2(\omega) = 1 + \sum_j \frac{\rho_j\,G_j^2}{\omega_j^2 - \omega^2},
$$

each of which is flat for ω below its mode. So the total is non-dispersive
for ω below the **lowest** sheet mode — resolving the "non-dispersivity with
a spectrum" question the single-resonance argument left open
([simplified-model-and-mast.md](simplified-model-and-mast.md) §5). Dispersion
appears only as ω approaches a sheet resonance (the pair-production / internal
-excitation regime).

## 5. Honest limit: the mass-direction scaling [open, non-gating]

δn ∝ ρ A²/ω₀² carries an explicit ω₀ (mass) dependence. At **fixed** ω₀ the
coupling is to energy (§3) — the equivalence-principle-relevant direction.
But **across** particle species (heavier = higher ω₀ = smaller, more
localized compact geometry), the net scaling of δn with mass mixes this 1/ω₀²
with the localization (ρ grows as the compact geometry shrinks) and the
oscillator strength. Whether these combine to δn ∝ ρ_E *uniformly across
species* — full universality — cannot be settled in the 1D toy; it needs the
MaSt sheet geometry (the compact size R ∝ 1/ω₀, the sheet mode structure).
This is part of the deferred **coefficient / full-sheet** work, and the
coefficient is an *optional bonus, not a gate* (§ README). It is flagged, not
assumed.

## 6. Assessment

Applying the micro-to-macro method to the detour rule gives a result stronger
than expected: the mechanism **is** a Lorentz-oscillator dielectric, so it
inherits standard, textbook refractive physics —

- **δn ∝ energy** (the round-trip makes it second order in the parametric
  coupling ∝ A²), so the coupling is to energy → universal gravity, in the
  direction that matters for the equivalence principle; and
- **non-dispersive** for ω below the lowest mode, generalizing cleanly to the
  sheet spectrum.

Both open validity questions of gate condition (2) and (3) resolve
**favourably from the rule**. What remains is the cross-species mass-scaling
(§5), which is entangled with the sheet geometry and belongs to the
optional coefficient — not a validity gate.

So in the simplified model, mechanism 2 now has all four gate conditions met
*in structure* — (0) vacuum field, (1) 1/r isotropic, (2) non-dispersive
(with spectrum), (3) coupling ∝ energy (constant of the right form) — with
the mass-scaling coefficient and full-sheet rigor as the remaining,
non-gating work. This is the point at which a scaffolding chapter on the
mechanism becomes defensible.
