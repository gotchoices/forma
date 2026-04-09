# Q113: Do bound neutrino modes participate in thermal equilibrium?

**Status:** Open — conceptual hypothesis with quantitative implications
**Related:**
  [Q77](Q77-alpha-as-impedance.md) (α as impedance mismatch),
  [Q92](Q92-neutrino-sheet-as-bath.md) (neutrino sheet as dissipative bath),
  [Q111](Q111-neutrino-coupling-constant.md) (neutrino coupling α_ν ≈ 1/52),
  [R49](../studies/R49-neutrino-filter/findings.md) F22–F25 (Compton overlap),
  [`primers/threshold-theory.md`](../primers/threshold-theory.md) (Planck 1911),
  [Q89](Q89-fusion-as-mode-transition.md) (neutrino Compton window)

---

## 1. Black body radiation and MaSt

### What MaSt does not change

Planck's 1911 "second theory" — continuous absorption,
threshold emission — produces the same equilibrium spectrum
as his 1900 quantized theory.  The Planck distribution is
the unique thermal equilibrium regardless of whether the
underlying mechanism is quantized or threshold-based.  MaSt
and threshold theory do not alter the black body spectrum.

### What MaSt does change

MaSt adds structure to the emitting matter.  Every particle
is a standing wave on a material sheet, and the coupling
between each sheet and spacetime S is characterised by a
geometric constant:

| Sheet | Coupling | Interpretation |
|-------|----------|----------------|
| Ma_e (electron) | α = 1/137 | EM impedance mismatch |
| Ma_p (proton) | α = 1/137 | Same EM coupling |
| Ma_ν (neutrino) | α_ν ≈ 1/52 | Non-EM channel (Q111) |

The electron and proton sheets couple to the photon field
at strength α.  This is the mechanism behind thermal
radiation: matter (Ma modes) exchanges energy with the
radiation field (S modes) at a rate set by the impedance
mismatch.

The neutrino sheet also has a geometric coupling to S
(α_ν ≈ 1/52), but through a non-electromagnetic channel.
The question is whether this coupling allows neutrino
sheet modes to participate in thermal physics.

## 2. Bound vs free neutrino modes

The standard picture of thermal neutrinos involves free
neutrinos produced and annihilated through weak processes
(e.g., the cosmic neutrino background at T_ν ≈ 1.95 K).
Free neutrinos interact so weakly that they decouple from
matter at T ~ 10¹⁰ K and stream freely thereafter.

**But most neutrino modes in ordinary matter are not free.**

Every neutron contains a bound neutrino mode as part of
its compound torus structure.  In a block of iron:

- 26 neutrons per atom (⁵⁶Fe)
- ~8.5 × 10²² atoms/cm³
- → ~2.2 × 10²⁴ bound neutrino modes per cm³

These bound modes are **stationary**.  They are locked
into the nuclear structure as standing waves.  They do not
escape.  If they absorb energy from the thermal field,
they re-emit it locally.  They are available to participate
in thermal equilibrium in the same sense that phonon modes
or electron orbital modes participate.

The bound neutrino modes vastly outnumber any free
neutrinos passing through the material.  The cosmic
neutrino background has a number density of ~56 ν/cm³
per flavour, while a cm³ of iron contains ~10²⁴ bound
neutrino modes — a factor of ~10²² more.

## 3. Energy scales

The neutrino mass eigenstates (Assignment A) set the
energy scale of the bound modes:

| Mode | Mass | Pair threshold (2m) | Temperature |
|------|------|---------------------|-------------|
| ν₁ (1,1) | 29.2 meV | 58.4 meV | ~680 K |
| ν₂ (−1,1) | 30.5 meV | 61.0 meV | ~710 K |
| ν₃ (1,2) | 58.2 meV | 116.4 meV | ~1350 K |

| Reference | Energy | Temperature |
|-----------|--------|-------------|
| Room temperature kT | 25.9 meV | 300 K |
| ν₁ Compton energy | 29.2 meV | 339 K |
| ν₁ν̄₁ pair threshold | 58.4 meV | 680 K |
| Iron melting point | — | 1811 K |
| Solar surface | — | 5778 K |

At room temperature, kT ≈ 26 meV — comparable to but
just below the ν₁ mass.  The single-mode excitation
energy is already thermally accessible.  The pair
production threshold (2m_ν₁ ≈ 58 meV, ~680 K) requires
moderate heating — a dull red heat.

## 4. The question: thermalization rate

The existence of bound neutrino modes at the right energy
scale is necessary but not sufficient.  For them to affect
thermal physics, they must **exchange energy with the
lattice** on a timescale shorter than the observation time.

Two limiting cases:

**Fast coupling (thermalized):**  If bound neutrino
modes exchange energy with surrounding atoms efficiently
— perhaps through the collective Compton overlap (R49
F22–F23: each neutrino mode's Compton window encompasses
~10¹³ atoms) — they act as additional thermodynamic
degrees of freedom.  Consequences:

- Excess specific heat at temperatures above ~340 K
  (where neutrino modes become thermally active),
  beyond what lattice phonons and electrons account for
- The excess would be material-dependent (proportional
  to the neutron count per atom, not the atomic mass)
- A frequency-selective thermal absorption band near
  ~7 THz (42 μm, the ν₁ Compton frequency) and ~14 THz
  (21 μm, the ν₃ Compton frequency)

**Slow coupling (frozen out):**  If the coupling between
neutrino modes and the thermal field is too weak (as
expected from standard weak-interaction rates), the
modes exist but don't exchange energy on laboratory
timescales.  They are analogous to nuclear spin
degrees of freedom, which are formally present but
thermally decoupled in most experiments.  In this case,
there would be no observable thermal signature.

The collective Compton overlap (10¹³ atoms sharing a
neutrino Compton window) could enhance the effective
coupling beyond the single-particle weak rate.  Whether
this enhancement is sufficient to reach thermal
equilibrium at laboratory timescales is an open question
(R49 F25).

## 5. Connection to threshold theory

In the threshold model, absorption is continuous and
sub-threshold.  A bound neutrino mode in a neutron could
continuously absorb energy from the ambient thermal IR
field, accumulating sub-threshold energy over time.  This
is exactly the loading mechanism of Q85 and L02.

If this loading is efficient, the neutrino modes are
effectively thermal — they absorb and emit at the
thermal rate, contributing to the specific heat.  The
threshold mechanism provides a pathway for energy
exchange even if the instantaneous coupling is weak:
slow continuous absorption, followed by threshold
emission, at a rate that equilibrates over macroscopic
times.

## 6. Observational handles

If bound neutrino modes participate in thermal
equilibrium, the effects would be:

1. **Specific heat anomaly.**  An additional contribution
   beyond the Debye (phonon) and Sommerfeld (electron)
   terms, scaling with the neutron count per atom.
   Onset ~340 K, saturating when kT >> m_ν.  Size:
   roughly 3 modes × k_B per neutron (if fully active).

2. **Neutron-count scaling.**  The anomaly would
   correlate with the number of neutrons, not protons
   or electrons.  Comparing isotopes (e.g., ⁵⁶Fe vs
   ⁵⁴Fe) could isolate the effect.

3. **Frequency-selective thermal absorption.**  A
   narrow absorption feature near ~7 THz (42 μm) in
   thermal spectra, material-independent, present in
   any neutron-bearing substance.

4. **Modified emissivity.**  At temperatures above
   ~680 K, energy channelled into neutrino modes is
   either re-emitted at neutrino-mode frequencies
   (contributing to thermal IR) or transferred to
   nuclear modes (contributing to anomalous heat).

## 7. What is already known experimentally

High-temperature specific heat measurements of metals
show deviations from the Debye model, but these are
conventionally attributed to anharmonic phonons,
electronic contributions, magnetic ordering, and
vacancy formation.  No one has looked for a
neutron-count-dependent residual.

Far-IR spectroscopy (~7 THz) of simple materials
(metals, noble gases, molecular crystals) could in
principle reveal a material-independent absorption
feature.  Synchrotron-based far-IR facilities have
sufficient resolution and range.

## 8. Summary

MaSt does not change the Planck spectrum (threshold
theory gives the same equilibrium distribution).  But
it identifies a population of bound neutrino modes
inside every neutron — stationary, at the right energy
scale (~30–60 meV), and potentially coupled to the
thermal field through the collective Compton overlap.
Whether these modes are thermally active or frozen out
depends on the effective coupling rate, which is the
central open question.  If active, they would produce
measurable anomalies in specific heat and far-IR
absorption, scaling with neutron number rather than
atomic mass or electron count.

---

*Connects to: Q77 (α as impedance), Q92 (neutrino
bath — ghost suppression angle), Q111 (α_ν ≈ 1/52),
R49 F22–F25 (Compton overlap and collective coupling),
Q85/L02 (threshold loading mechanism),
[`primers/threshold-theory.md`](../primers/threshold-theory.md)
(Planck 1911)*
