# Chapter 2 — Why simple binding fails

This chapter is a negative result, and it earns its place: mapping what does *not*
bind a particle is the argument for the mechanism that does (Chapter 3). It is
deliberately brief.

## §1 What binding requires

A particle is a mode that is **localized**, **mobile**, and **stable** — it stays
together, it can move, and it does not disperse. On the bare linear substrate a
localized massive mode fails the last test at once: it is a superposition of
wavevectors with different velocities, so it spreads (the Kaluza–Klein dispersion
of Chapter 4). Binding therefore requires a nonlinearity that holds the mode
together against dispersion.

## §2 The value-bound is defocusing

The obvious candidate — and the project's original entry hypothesis — is the
discrete-maximum **bound** on an edge amplitude: cap |φ| at some value. But a cap
on a *linear amplitude* confines the field to an interval [−b, b], which acts as a
**wall**. A wall makes an oscillator *harden*: its frequency *rises* with
amplitude (a particle in a box hits the walls sooner when it carries more energy).
A hardening nonlinearity is **defocusing** — the wrong sign to bind. So the
saturation hypothesis cannot, by itself, make a particle. This is stated, not
belaboured; the sign is made precise in Chapter 3, where the *opposite*
topology — a circle rather than an interval — flips it.

## §3 The mechanisms that did not bind

Across the work files a series of local field responses were tried on the (x,c)
substrate; none produced a stable, mobile, localized mode. Grouped by distinct
mechanism type:

| Mechanism | Idea | Why it did not bind |
|---|---|---|
| clip (value-bound) | hard amplitude cap | defocusing wall (§2) |
| spillover | route excess to other edges | no persistent transfer; no pump |
| crude discreteness | round edges to ±1 | non-conserving; froze the whole lattice |
| Kerr index (knob A) | load-dependent phase delay | slowed the wave but did not confine |
| strain / metric (knob B) | load-dependent contraction | captured but did not confine (a real gravity-carrier candidate, kept separate) |
| topological winding | a U(1) phase winding | protected and localized but **immobile** (flat band) |

Detail is in [work/results-m1-m2.md](work/results-m1-m2.md),
[work/phase-winding-results.md](work/phase-winding-results.md), and
[work/responsive-medium.md](work/responsive-medium.md).

A caution on reading this table. A mechanism failing *these* tests does not prove
it has no merit — it may have been the wrong mechanism, or the right one tested in
the wrong regime. Each entry is a **"not yet" with a named obstruction**, not a
closed verdict; several (knob B's strain field especially) remain live for other
purposes. What the table establishes is narrower and sound: *no local
amplitude-response tried here binds a particle*, which is enough to motivate
looking elsewhere.

## §4 No prior containment in forma

A survey of the wider framework found the same: no earlier forma study had
demonstrated dynamical containment. Localized modes disperse on the 1D cylinder,
on a 2D torus, and on a 2D sheet alike; where particles appear in metric-mass and
metric-charge they are *asserted* analytically, with localization deferred. So the
gap is not peculiar to this project.

## §5 The lesson, and the fork

These negatives **motivate** — they do not deductively prove — that the missing
ingredient is a **focusing** nonlinearity; independently, focusing paired with
saturation is the standard recipe for a soliton. The live question for Chapter 3
is then sharp and topological: is the bounded field an **interval** (a clipped
amplitude, defocusing) or a **circle** (a compact phase, focusing)? The substrate
does not decide it; that choice is the hinge of the matter half.
