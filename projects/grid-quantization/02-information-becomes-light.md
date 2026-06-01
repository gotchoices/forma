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
sign flipped. Consider a static *transverse* disturbance — a fixed
pattern of phase differences in which the three edges of a junction do
*not* all hold the same value. The next tick's sign-flipped reflection
sends back the negative of what is there, so the pattern cannot persist;
it is driven toward its own inversion. (One mode is the exception: the
fully symmetric, all-edges-equal "breathing" pattern is preserved by the
rule unchanged. It reappears in §2.4 as a per-junction eigenmode and in
§3.3 as the ω = 0 flat band. The argument here is for the
non-symmetric, dynamical disturbances.)

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
merely wobble in place — it travels, at a speed bounded above by
Chapter 1's one-edge-per-tick causal ceiling (and measured below at
≈ 0.41 of that ceiling). The [sim-maxwell](../../grid/sim-maxwell/) study confirms this
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
Linear means **non-dispersive**: with ω = v · k, the group velocity
dω/dk equals the phase velocity ω/k, so the carrier and the envelope
travel at exactly the same speed and a wave packet holds its shape as
it moves — the signature of a genuine wave equation, and of light.
(The 0.41 is the phase velocity along one lattice axis, in units of one
edge per tick — well below the §1.3 causal ceiling, and a
lattice-specific figure, not a fundamental constant; other directions
or measures give other values.)

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
- two **transverse (helical)** basis modes, (1, e^{2πi/3}, e^{4πi/3})
  and (1, e^{4πi/3}, e^{2πi/3}): the phase advances steadily *around*
  the junction, one way in each. As *per-junction* eigenmodes these
  carry eigenvalue −1 under the scatter rule — the sign-flip that
  drives oscillation. They are not themselves the propagating photon
  (which is a lattice-wide Bloch mode in a dispersive band — §3.2);
  they supply the **two-dimensional polarisation basis** that a
  transverse propagating mode carries at each junction.

(So the oscillation of §2.1 is the oscillation of the *transverse
sector*: locally, the helical basis carries the eigenvalue −1 sign-flip;
globally, that sector becomes the dispersive Bloch bands of §3.2 — the
modes that actually carry energy across the lattice. The symmetric mode
is left unchanged by the rule and reappears as the ω = 0 flat band of
§3.3.)

The bridge from the per-edge phases to this junction basis is a
discrete Fourier transform: the three edges' phasor representations
e^{iθ₁}, e^{iθ₂}, e^{iθ₃} are projected onto the cube-root weights
(1, e^{2πi/3}, e^{4πi/3}) to read off the symmetric and the two helical
components. The per-edge compact phase of A3 *enters* the junction
description through that projection.

The two transverse basis modes are the two **circular polarisations**,
the combinations E + iB and E − iB. Here is the point to hold onto. A
definite circulation sense — a definite **handedness** — exists only
when the edges carry *relative phase*, i.e. only for complex (phasor)
amplitudes. Real amplitudes give linear polarisation: the wave
propagates, but with no definite handedness. So the wave's
**handedness — its spin — is set by the phase** (the clock face of
Chapter 1), while its **propagation** is the work of the restoring
sign-flip. Two features of the same transverse wave, from two different
sources: the spring makes it oscillate and move; the phase decides
which way it circulates.

(Two notes on the *layer* this story lives in. **Classical, not
quantum:** the phase at work here is the classical field phase —
circular polarisation is ordinary classical electromagnetism. It is
not the quantum amplitude, a separate ingredient taken up later in the
arc. **Not exhibited by the cited sim:** the simulated `scripts/lib.py`
carries real (a_fwd, a_bwd) amplitudes per edge and so does *not*
directly show the helical / spin structure — that requires the
complex / phasor extension flagged in
[tier2-design.md](work/tier2-design.md) §4.)

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
