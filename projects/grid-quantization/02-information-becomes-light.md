# Ch. 2 — Information becomes light

**Status:** Draft (prose, first pass). Part of the [presentation arc](README.md#presentation-arc).
**Grade:** [derived] — classical wave mechanics + the junction's mode structure; standard/cited.
**Role:** show how an injected disturbance becomes propagating light — and trace its two defining features, propagation and spin, to two *different* sources.

Chapter 1 fixed the medium: a honeycomb of phase-carrying edges, a
discrete clock, and one impedance-matched scattering rule. This chapter
shows that a disturbance on that medium *is* light — a propagating
electromagnetic wave with two polarizations — and, just as importantly,
traces its two distinguishing features to two different places.
Propagation comes from the rule's sign-flipped reflection; the wave's
handedness, its spin, comes from the compact phase, the ℵ-line. Keeping
those apart is the point of the chapter.

## 2.1 Why a static disturbance cannot stay still

Recall the junction rule's reflection coefficient: −1/3. A signal
arriving at a junction is partly sent back along its own edge with its
sign flipped. Consider a static disturbance — a fixed pattern of phase
differences, held in place. At the next tick the sign-flipped reflection
sends back the negative of what is there, so the pattern cannot persist;
it is driven toward its own inversion.

This is a **restoring force** — the same thing that makes a spring
oscillate: displace it, and it pushes back. A medium with a restoring
force does not let a disturbance sit; it makes it oscillate. The negative
sign is essential: a *positive* reflection would let a disturbance spread
and fade away (mere diffusion), with nothing to swing it back. The −1/3
is what turns an inert network into an oscillating one.

## 2.2 Oscillation becomes propagation

Applied across the lattice tick after tick, the junction rule is — in the
continuum limit — the ordinary **wave equation** ∂²a/∂t² = c²∇²a
([Q140](../../qa/Q140-light-quantization-from-recirculation.md) §2): the
restoring force at each junction, coupled to its neighbours, hands the
oscillation from edge to edge. A localized disturbance therefore does not
merely wobble in place — it travels, at the one-edge-per-tick speed of
Chapter 1. The [sim-maxwell](../../grid/sim-maxwell/) study confirms this
directly: directional propagation, energy conserved, and disturbances
adding linearly (exact superposition). An injected pattern of phase
differences — "information" placed on the lattice — propagates away as a
wave. That wave is light.

## 2.3 The dispersion relation

How a medium ties a wave's frequency ω to its wavenumber k is its
**dispersion relation**, ω(k). Driving the lattice across a range of
frequencies and reading off the wavelength that results gives, in the
long-wavelength regime,

> ω ≈ 0.41 · k,

a **linear** relation (`scripts/run_recirculation.py --test disp`).
Linear means **non-dispersive**: every wavelength travels at the same
speed, so a wave packet holds its shape as it moves — the signature of a
genuine wave equation, and of light. (The 0.41 is the phase velocity
along one lattice axis: a lattice-specific figure, not a fundamental
constant; other directions or measures give other values.)

## 2.4 The two polarizations, and where handedness comes from

So far the disturbance has been treated as a scalar. Light is a *vector*
wave with two **polarizations**, and that structure comes from the
three-fold geometry of the junction.

At a Y-junction the three edge amplitudes can be re-expressed in a basis
built from the **cube roots of unity** — the complex numbers 1,
e^{2πi/3}, e^{4πi/3}, spaced equally around the unit circle. This splits
the junction's response into three modes ([fields.md](../../grid/fields.md)):

- a **symmetric** mode (1, 1, 1): all edges in phase — a breathing
  (monopole) excitation that *pools at the node* rather than propagating.
  It is not the photon.
- two **transverse (helical)** modes, (1, e^{2πi/3}, e^{4πi/3}) and
  (1, e^{4πi/3}, e^{2πi/3}): the phase advances steadily *around* the
  junction, one way in each. These are the modes that oscillate and
  propagate — the photon — and they span its two-dimensional polarization
  space.

(The oscillation of §2.1 is really the oscillation of *these* transverse
modes: under the scattering rule they carry the sign-flip — the restoring
effect — while the symmetric mode is left unchanged.)

The two transverse modes are the two **circular polarizations**, the
combinations E + iB and E − iB. Here is the point to hold onto. A definite
circulation sense — a definite **handedness** — exists only when the
edges carry *relative phase*, i.e. only for complex (phasor) amplitudes.
Real amplitudes give linear polarization: the wave propagates, but with
no definite handedness. So the wave's **handedness — its spin — is set by
the phase** (the clock face of Chapter 1), while its **propagation** is
the work of the restoring sign-flip. Two features of the same transverse
wave, from two different sources: the spring makes it oscillate and move;
the phase decides which way it circulates.

(The phase at work here is the **classical** field phase — circular
polarization is ordinary classical electromagnetism. It is not the
quantum amplitude, which is a separate ingredient taken up later in the
arc.)

## 2.4a The handedness lives on the ℵ-line — a unification, not an evasion

The phase the helical modes use is the per-edge compact phase, which
Chapter 1 named the **ℵ-line**. So the spin of light is not produced
*without* a compact dimension — it is produced by *the smallest one*.
This is precisely the Kaluza–Klein mechanism GRID and MaSt use elsewhere
([photon-from-aleph.md](../../grid/photon-from-aleph.md)): the circle
(S¹ = the ℵ-line) privileges a U(1) one-form whose four-dimensional
vector index *is* spin-1 — the **why**; the three-fold junction organizes
the ℵ-line phases into the two helicities — the **how**. The junction
account and the ℵ-line/Kaluza–Klein account are the *same* mechanism at
the per-edge scale, not competitors. (An earlier framing that this
"needs no ℵ-line" was wrong: the phase it relies on *is* the ℵ-line. What
is genuinely avoided is a *separate, additional* compactification
postulate, not the ℵ-line.)

One thing the unification still owes: a demonstration that the
Kaluza–Klein route (a one-form on a single ℵ-line → two transverse
states) and the junction route (three-fold helical eigenmodes → two
helicities) deliver the *same* two states. They are very plausibly the
why and the how of one fact, but their coincidence is asserted here, not
yet shown.

## 2.5 What "light" is, in the model

Putting the pieces together: light is a propagating disturbance of the
lattice's phase-carrying edges, carrying coupled E and B. Its
**propagation** is the work of the sign-flipped restoring term; its
**handedness (spin)** is circulation in the ℵ-line phase, organized by
the three-fold junction into two polarizations. Nothing electromagnetic
and nothing quantum was assumed to reach this — only the substrate of
Chapter 1.

---

The remaining chapters (see the [arc](README.md#presentation-arc)) build
on this.

## Sources

- [Q140](../../qa/Q140-light-quantization-from-recirculation.md) §2 — oscillation / propagation from the junction rule
- [fields.md](../../grid/fields.md) — the cube-root-of-unity decomposition; helical E ± iB modes
- [photon-from-aleph.md](../../grid/photon-from-aleph.md) — the ℵ-line = per-edge S¹; spin-1 via Kaluza–Klein
- [sim-maxwell](../../grid/sim-maxwell/), `scripts/run_recirculation.py --test disp` — propagation, energy conservation, dispersion

## Claim discipline

[derived], classical. Two attributions kept distinct: **propagation** ←
the −1/3 restoring sign-flip; **spin / helicity** ← the compact phase =
the ℵ-line (A3), organized by the junction. Do **not** say "no ℵ-line" —
the phase used *is* the ℵ-line. The phase here is classical (circular
polarization is ordinary EM); no *quantum* content yet. The
KK-route / junction-route equivalence is flagged as owed, not shown.
