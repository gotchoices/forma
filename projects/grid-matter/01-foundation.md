# Chapter 1 — Foundation and testbed

## §1 The question

Earlier GRID work established two things the substrate produces on its own.
**Electromagnetism** is the linear wave dynamics of the equal-impedance scatter —
Maxwell's equations emerge from the lattice ([grid/sim-maxwell](../../grid/sim-maxwell/)).
**Gravity** follows a Jacobson-style thermodynamic route, the metric as an
equation of state ([grid/gravity.md](../../grid/gravity.md)). Both, in different
senses, are *classical*: the field theory of light and the geometry of spacetime.

This chapter opens a different question: does the same substrate also produce
**matter** — stable, localized particles carrying mass and charge — and **quantum
mechanics** — interference, discrete detection, the Born rule, entanglement? The
framing is deliberately interrogative. The work is pursued in two acts, *matter*
(Chapters 2–6) and *quantum mechanics* (Chapters 7–10), with every result graded
for what is **derived**, what is **posited**, and what remains **open**.

## §2 The GRID substrate

GRID is a causal lattice whose only variables are directed edge amplitudes,
updated each tick by the equal-impedance scatter S = (2/N)J − I followed by
propagation to neighbours. The scatter is orthogonal, so the dynamics is unitary
(energy-conserving), and — being *linear* — it obeys exact superposition. The
construction and its Maxwell limit are developed in
[grid-primitive](../grid-primitive/) and [grid-duality](../grid-duality/) and are
taken as given here. Linearity is exactly why the bare substrate gives Maxwell and
nothing more: superposition forbids the mode-mixing that bound states and quanta
require. The missing ingredient is a nonlinearity — the subject of Chapters 2–3.

## §3 The testbed: the (x, compact-c) cylinder

Throughout we use the minimal setting that can separate light from matter: one
**extended** dimension x and one **compact** dimension c, wrapped into a cylinder.
A photon is the c-uniform **n=0** mode propagating in x; anything in the compact
**n≥1** sector is a candidate for matter. This is the same simplified geometry
[metric-mass](../metric-mass/) uses for its continuum mass derivation, which
Chapter 4 corroborates dynamically. One extended plus one compact dimension is the
smallest arena in which the two sectors are distinct.

## §4 Two different compact structures

A recurring source of confusion — and the distinction the whole matter half turns
on — is that "compact" names two different things:

- a **compact coordinate** (the c-ring, or a 2D Ma sheet): a periodic *position*
  dimension. A field on it carries a **Kaluza–Klein mass** (a quadratic term),
  developed in Chapter 4;
- a **compact field *value*** (the field's value lives on a circle — the ℵ-line,
  or a sheet's U(1) phase): its on-site potential is **periodic** (a cosine),
  developed in Chapter 3.

These are not the same object, and conflating them was the early error that this
arc corrects. Chapter 3 needs the field-value phase; Chapter 4 needs only the
coordinate.

## §5 Method and honesty conventions

The project is computational-first: build the minimal simulation, observe, then
return to derivation. Claims carry status flags — **[D]** derived, **[P]** posited
(a stated premise), **[O]** open — and where a chapter corroborates standard
physics or another forma project it cites the result in a few lines rather than
re-deriving it. The supporting record is indexed in [work/README.md](work/README.md).
