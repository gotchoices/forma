# The conservative rule, and gravity as the steady part of one field

**Status:** Derivation + simulation. **Steps 5c′ and 5d of the mechanism 3
validation plan ([STATUS.md](STATUS.md)).** (a) The lattice rule for stores whose
weights change in time is *derived* from the action; it says what must be carried
through a change of weight, and the back-reaction appears without being added.
(b) With that rule the cheapest branch works: **one** real field, **no** coupling
constant — two lumps of wave rectify a steady deflection thirty times larger
than their own amplitude and fall into it, on the ray law, with the third law
holding. (c) One hazard of this branch is found and characterized (resonant
second-harmonic generation); (d) the breathing-source flag of step 3 is
corrected — it assumed a point source.

Script: [`../scripts/same_channel.py`](../scripts/same_channel.py).
Figure: [`../outputs/same_channel.png`](../outputs/same_channel.png).

Grades: **[rigorous]**, **[simulated]**, **[argument]**, **[inconclusive]**,
**[open]**.

---

## 1. The rule: what is carried through a change of weight [rigorous]

The closed-loop run of step 5c
([closed-loop-result.md](closed-loop-result.md)) held each store's *energy*
fixed when its weight changed. That keeps the waves' norm exact, but it means
the deflection's energy comes from nowhere; it was adequate only because the
fields were weak. The derived rule follows from writing the lattice in
Hamiltonian form. Per node: a deflection q and a **momentum** P. Per link: an
**extension** e, the difference of q across it. With the linear-delay rule
(requirement R9),

<!-- M(q) = (1+q/2)²  node inertia;  C(q̄) = (1+q̄/2)²  compliance of a space link;  compact links unloaded -->
$$
M(q) = \bigl(1+\tfrac q2\bigr)^2 ,\qquad
C(\bar q) = \bigl(1+\tfrac{\bar q}2\bigr)^2 ,\qquad
H = \sum_{\text{nodes}} \frac{P^2}{2M(q)} + \sum_{\text{space links}} \frac{e^2}{2C(\bar q)} + \sum_{\text{compact links}} \frac{e^2}{2} ,
$$

with q̄ the mean of q at a link's two ends. Hamilton's equations give the
deflection rate v = P/M, the tension T = e/C, and

<!-- dP/dt = (net tension) + ½ M′(q) v² + ¼ Σ_adjacent C′(q̄) T² -->
$$
\dot P \;=\; (\text{net tension}) \;+\; \tfrac12 M'(q)\,v^2 \;+\; \tfrac14\!\!\sum_{\text{adjacent links}}\!\! C'(\bar q)\,T^2 .
$$

- **What is carried through a change of M or C is P and e** — the canonical
  variables — not the stored energies. In circuit terms: when a capacitance
  changes, the charge on it is what stays, and its voltage and energy jump; the
  energy difference is the work done on whatever changed the capacitance.
- **The last two terms are not added.** They are forced by the q-dependence of
  M and C, and they are the lattice form of the source found in step 3. Both are
  squares: an oscillating wave pushes q *upward*, always, in proportion to its
  energy.
- **Total energy is conserved** by construction. In the simulation H drifts by
  7×10⁻⁴ over the run at time-step 0.5 and by half that at 0.25 — the
  integrator's error, not the model's.

## 2. One field, no coupling constant [simulated]

If q in §1 is the *same* field whose oscillation is the wave, nothing else is
needed: the wave's own squares drive its own zero-frequency part. This is the
same-channel branch of
[requirements-and-dof.md](requirements-and-dof.md) §6. There is no stiffness to
choose; the strength of gravity in lattice units is whatever the rule gives.

Two lumps — compact n = 1 modes circulating around a ring of 16 nodes, at rest
in x, energies in the ratio 3, amplitudes 2.0×10⁻³ and 3.5×10⁻³, 1200 nodes
apart — are released and nothing else is done.

| | |
|---|---|
| steady deflection rectified by the lumps | q = 0.112, against a wave amplitude of 0.0035 |
| lighter lump moved | +22.85 nodes; ray law +22.90; ratio **0.998** |
| heavier lump moved | −7.28 nodes; ray law −7.28; ratio **0.999** |
| acceleration ratio | 3.13 (energy ratio 3.00) |
| momenta at the end | equal and opposite to **0.2%** |

The zero-frequency part of the field grows into the same tent-shaped deflection
as in step 5c (one extended dimension again, so a constant pull), and each lump
falls toward the other exactly as the ray law requires in that deflection. The
separate-channel and same-channel branches agree; the second simply has fewer
parts.

## 3. A hazard of the same-channel branch: the second harmonic [simulated + argument]

The same nonlinearity that rectifies also drives the compact **n = 2** mode at
twice the lump's frequency. In the run above it reaches 4% of the fundamental's
amplitude (under 1% of its energy) — far more than an off-resonance estimate
gives. The reason is structural: the Kaluza–Klein tower is harmonic (the n = 2
rest frequency is twice the n = 1), so the drive is **resonant and
phase-matched**, and the n = 2 amplitude grows steadily rather than saturating.

Physically this is two n = 1 quanta merging into one n = 2 quantum — allowed by
both energy and compact momentum, at threshold. It is a gravitational-strength
process and needs two quanta in the same place, so it does not touch a single
particle; what it implies for dense matter has not been estimated. **[open]**
It is absent from the separate-channel branch only to the extent that branch's
source was approximated by its steady part.

## 4. The breathing-source flag, corrected [argument]

Step 3 found that a purely *standing* wave is a pulsing source, and estimated
that a proton-mass standing wave would radiate itself away in about 2 million
years ([action-and-gamma.md](action-and-gamma.md) §6). **That estimate assumed a
point source, and it is wrong for any real particle.** The source is the energy
density of the wave, spread over the particle's wave packet. An extended source
radiates only through its Fourier component at the radiated wavenumber; here the
radiated wavelength is half the particle's Compton wavelength, so for a packet of
width σ the radiated amplitude carries a factor

<!-- exp(−(k σ)² / 4),  k = 2ω₀/c  (k σ = 2σ / Compton length) -->
$$
\exp\!\bigl[-(k\sigma)^2/4\bigr], \qquad k = 2\omega_0/c .
$$

A proton confined to a nucleus (σ ≈ 1 fm, Compton length 0.21 fm) has
kσ ≈ 9.5: the power is suppressed by about 10⁻²⁰, lengthening the lifetime from
millions of years to ~10²⁶ years. Any less confined particle is suppressed further.
Only a body localized *within* its own Compton wavelength radiates freely — and
such a state is relativistic, not a particle at rest. So requirement R10 is
softened: a standing neutral particle is not excluded; the constraint bites only
below the Compton scale. (A circulating mode still has an exactly steady source,
confirmed to machine precision.)

**A numerical check of this was attempted and is inconclusive.** Lumps narrow
enough to radiate measurably (a few Compton lengths) also spread at a good
fraction of light speed, so their own tails reach any probe and pulse there
locally, swamping the radiation: the measured signal stayed flat where the
prediction falls by four orders of magnitude. The form-factor statement rests on
the linearity of the zero-frequency sector's response to a given source — a
standard antenna argument — not on a simulation. The test mode was removed from
the script rather than left as a misleading tool. **[inconclusive]**

## 5. What this establishes, and what it does not

**Established.** The conservative rule; that gravity can be the steady part of
the same field that carries light and matter, with no added wave degrees of
freedom and no coupling constant — only the node memory; mutual attraction, the
ray law, the third law and energy conservation in that setting.

**Not established.**
- Three dimensions for the closed loop (as in step 5c).
- The size of the second-harmonic / merging process in real matter.
- Light-on-light scattering at gravitational strength (the other half of item
  5d) — not yet examined.
- That the strength the rule gives corresponds to Newton's constant: in lattice
  units it is of order one, which is what a Planck-scale grain means; consistent,
  not a prediction.

## Grades summary

- **[rigorous]** The Hamiltonian lattice, what is carried through a change of
  weight, the forced back-reaction terms, energy conservation.
- **[simulated]** One-field attraction: ray law 0.998 / 0.999, acceleration
  ratio 3.13, momentum balance 0.2%, rectified deflection 30× the wave
  amplitude; energy error scaling with the time-step; the resonant second
  harmonic; steady source of a circulating mode.
- **[argument]** Why the second harmonic is resonant; the form-factor
  suppression of breathing radiation and the correction to step 3's estimate.
- **[inconclusive]** The numerical breathing test.
- **[open]** Second-harmonic/merging rate in matter; light-on-light; three
  dimensions.
