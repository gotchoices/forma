# Ch. 7 — The honest ledger

**Status:** Draft (prose, first pass). Part of the [presentation arc](README.md#presentation-arc).
**Grade:** [scope] — accounting, not derivation. This chapter consolidates what the arc has and has not claimed.
**Role:** the full accounting. What is derived, what is imported, what is conjectured, what is out of scope, and what is open for the next step.

Chapters 1 through 6 worked through the arc. This chapter consolidates
the honest picture in one place: a single table of what GRID says each
phenomenon *is*, with status; and a one-page summary of what is
derived, what is imported or conjectured, what is out of scope, and
what is open. Nothing new is claimed here; the chapter is the ledger.

## 7.1 What GRID says each phenomenon is

The table below is the single clearest statement of what the arc
accomplishes. Each row names an observed phenomenon, what it *is* in
the GRID model, and the *status* of that identification.

| Observed phenomenon | What it *is* in GRID | Status |
|---|---|---|
| EM wave / light | a propagating excitation of the edge-wave (junction-scatter) network | derived |
| wave propagation | the −1/3 restoring term → oscillation; linear dispersion ω ≈ 0.41·k | derived |
| spin / polarisation | the two helicities (E ± iB) from the ℵ-line phase (A3 per edge), organised by the three-fold junction — the same Kaluza–Klein mechanism MaSt uses for spin | derived (modulo the why/how complementarity flagged in ch. 2 §2.4a) |
| photon spectrum (which ω) | the dispersive Bloch bands of chapter 3 (lowest acoustic band = the photon, with measured ω ≈ 0.41·k) | derived |
| ℏ (quantum of action) | the substrate phase-space grain dW·τ — a unit, not a prediction | identified |
| **light quantisation** (integer photons) | **single-valuedness of a complex amplitude on the compact phase ⇒ integer occupation** | **candidate** — requires A5 to supply a complex amplitude (the quantum state); not a cheaper stochastic claim |
| localised "bound" mode | a flat-band compact-localised state at ω = 0, π | shown — but zero / band-edge energy, **not** a finite-rest-energy massive particle; mass proper is MaSt |
| charge | a spatial 2π phase winding (classical topological vortex) | derived ([maxwell.md](../../grid/maxwell.md)) |
| gravity | horizon entropy from finite information (A5 → Jacobson) | derived ([gravity.md](../../grid/gravity.md)) |
| α (electromagnetic coupling strength) | a loop-leakage / winding coupling; the *value* is input (A6); the single-loop number (2/3)¹² = 1/129.75 sits inside α's running range but is a property of a forced single pulse, not of a free propagating wave | input; numerical observation is *suggestive*, not predicted |

One substrate; most entries are *identifiable structures in the model*,
not separate postulates. **The two deepest entries — light quantisation
and gravity — share their axiom (A5)**: gravity reads A5 as horizon
entropy density, quantisation reads it as a complex amplitude on the
compact phase. Whether those two readings are the *same* reading of A5
is conjectural (chapter 6 §6.4); whether they are at least *consistent*
readings is granted by the arc as a working assumption.

## 7.2 What is derived

The following are derived from GRID's axioms together with the
computational measurements of chapter 3:

- **Information → light, with two polarisations** (chapters 1–2). The
  −1/3 restoring term turns a static perturbation into a propagating
  oscillation; the helical Y-junction eigenmodes organise the per-edge
  ℵ-line phases into the two transverse polarisations / helicities —
  the same Kaluza–Klein mechanism MaSt uses for spin.
- **The photon spectrum (P1)** (chapter 3). The lowest acoustic
  dispersive band is the free photon, with measured small-k slope
  ω ≈ 0.41·k (`scripts/run_recirculation.py --test disp`). The flat
  bands at ω = 0 and ω = π host bound (zero-mode / band-edge) states.
- **Each mode is an exact classical harmonic oscillator (P2)**
  (chapter 3). Linear dynamics + exact superposition; the quantum
  *ladder* (P3) is separate, taken up later.
- **Scale-invariance of the photon band** (chapter 3 §3.5). Linear
  dispersion as an IR fixed point, with deviation falling as ~k²
  toward long wavelength.
- **ℏ is a unit, not a target** (chapter 4). ℏ = dW·τ as a grain
  product, dimensionally forced. Universality of ℏ across fields
  follows automatically — same grains, same ℏ.
- **Planck scaling, power ∝ ω** (chapter 5 §5.0). Rigorously, from
  bounded discreteness alone: the substrate has no amplitude knob, so
  lower frequency means proportionally fewer transitions per unit
  time. Generalises to any finite base n ≥ 2 (with the phase-dial
  reading as the formal anchor; cost-model dependent prefactors).
- **The integer-ladder mechanism for P3 + P4** (chapter 5 §5.2–§5.3).
  Periodicity of the per-mode oscillation phase ⇒ integer Fourier
  index of the state on it ⇒ integer occupation. *Given* the
  complex-amplitude state, by Fourier-series.

## 7.3 What is imported or conjectured

Chapter 6 names what is *not* derived:

- **The A5 reading: state on the compact phase is a single-valued
  complex amplitude** (§6.1, §6.2). *[interpretive]* — the
  load-bearing piece of the entire arc. Without it P3 is undelivered;
  with it, P3 + P4 follow by standard mathematics. The import bridges
  per-cell *spatial* information (A5's allocation) to per-mode
  *temporal* amplitude (the Fourier-series object); the chapter names
  that bridge as part of what the import has to perform.
- **The shared root with gravity** (§6.4). *[conjecture]* — that
  gravity's reading of A5 (statistical entropy on a spatial horizon)
  and quantisation's reading (complex amplitude on a temporal phase)
  are the *same* reading. Even granting unification, "shared root"
  should be heard as "shared input" — A5 is the ingredient that two
  distinct machineries (Jacobson thermodynamics for gravity; the
  Fourier U(1) ↔ ℤ structure for quantisation) turn into their
  respective results.
- **The bounded occupation ladder** (§6.5). *[predicted, given the
  import]* — a sharp GRID-specific deviation from textbook QED's
  unbounded ladder. Astronomically high cap; unobservable today.
- **The α-scale leakage coupling** (§6.5). *[suggestive, not
  predicted]* — α is an A6 input. The (2/3)¹² = 1/129.75 number sits
  inside α's running range but is a property of a forced single pulse
  around an isolated loop; a clean propagating wave's net induced
  circulation cancels (the zigzag-cancellation finding).
- **The dynamical gate: a bit-conserving discrete-CA substrate rule**
  (§6.6). *[conjecture, unbuilt]* — the candidate is a sigma-delta
  node carrying a bounded accumulator that resolves the 1/3
  obstruction. No GRID simulation has been written that runs it.

## 7.4 What is out of scope

The arc deliberately does *not* address:

- **The Born rule and the measurement problem.** Given the
  quantum-state structure that chapter 6 imports, deriving Born
  probabilities and a measurement mechanism is the foundations-of-QM
  problem proper, which is not GRID-specific. The arc imports the
  complex-amplitude state and stops there.
- **Interference, entanglement, and the rest of QM dynamics.** Same
  scope: these are downstream of the import and require the full QM
  apparatus rather than GRID's substrate alone.
- **The cell-Planck identification at literal scale.** Chapter 4 §4.4
  marks this as the framework's *posit*, not a theorem. The arc does
  not attempt to derive the absolute lattice spacing.
- **Mass proper.** The flat-band CLS of chapter 3 §3.3 is a localised
  zero-energy bound mode, not a finite-rest-energy massive particle.
  Mass-as-rest-energy lives in MaSt, not in the substrate.

## 7.5 Open computational and construction probes

Three fronts remain open, each of which would tighten the arc:

- **The bit-conserving sigma-delta substrate rule** (§6.6). Build a
  simulation that runs the sigma-delta-style accumulator node on the
  honeycomb lattice; verify that its long-time average reproduces the
  continuous (2/3) scatter rule, that no bits leak, and that the
  bounded-substrate story of chapter 5 §5.0 is internally consistent.
  This would discharge the dynamical-gate conjecture from candidate to
  construction.
- **Per-edge ℵ-line → per-mode oscillation phase** (the aggregation
  step flagged in chapters 5 §5.2 and 6 §6.1). The arc currently
  treats this bridge as part of the import. An explicit construction
  showing how many per-edge phases combine into a single per-mode φ
  when a wave forms would shrink what the import has to perform — and
  would settle whether the per-edge ℵ-line of A3 *gives rise to* the
  per-mode φ in a derivable way, or whether the connection has to be
  imported.
- **Loop-closure / emergent-photon sectors.** Quantum-spin-ice and
  related lattice constructions are known to deliver emergent photons
  from bounded discrete substrates. Investigating whether GRID's
  honeycomb falls into such a sector — or constructing a sector where
  it does — would give chapter 6's import an independent
  corroboration.

These are *probes*, not closed predictions; their results would refine
the arc rather than overturn it.

## 7.6 Place in GRID, and the bottom line

This arc sits at one rung of GRID's broader promotion ladder:
**substrate → light → mass → charge**. The substrate of chapters 1
and 4 gives light via the propagation and modes of chapters 2–3 (with
A1–A4 + A5 jointly providing what is required). Mass proper sits one
rung up in MaSt — the bound CLS of chapter 3 §3.3 is *not* it. Charge
sits another rung up, derived in
[maxwell.md](../../grid/maxwell.md) from the spatial 2π winding
mechanism.

**Gravity shares its deepest axiom (A5) with light-quantisation.** If
chapter 6's shared-root conjecture holds, GRID's foundational economy
is striking: one axiom of finite information underwrites both the
spacetime equations and the quantisation of light. If the conjecture
proves weaker — A5 being a *shared input* rather than a *shared root*
— the picture remains an economical one: A5 supplies a single
quantitative ingredient that two distinct machineries turn into their
respective consequences.

The arc's bottom line is unchanged from the README headline. **GRID's
claim is explanatory, not predictive.** It says *what each phenomenon
is* in one substrate (lattice + clock + periodic phase + finite
information), and it reduces the conspicuous missing entry — light
quantisation — to one well-localised import (a complex amplitude over
A3's compact phase) that the arc names and grades honestly. The
accomplishment is the unified account above; the open work is the
construction of the substrate rule and the resolution of the
A5-reading question.

---

## Sources

- README §"What GRID says each phenomenon is" — the table this chapter consolidates
- chapters 1–6 of the arc, in full
- [work/countability-from-information.md](work/countability-from-information.md), [work/energy-and-coherence.md](work/energy-and-coherence.md) — the working notes behind chapters 5–6
- [foundations.md](../../grid/foundations.md), [gravity.md](../../grid/gravity.md), [maxwell.md](../../grid/maxwell.md), [photon-from-aleph.md](../../grid/photon-from-aleph.md) — GRID's foundational documents the arc rests on

## Claim discipline

[scope]. This chapter introduces no new claims; it consolidates the
arc's accounting. The phenomenon table, the derived list, the
imported / conjectured list, the out-of-scope list, and the open
probes are each carried over from chapters 1–6 with their grading
intact. The "shared root" framing is preserved as a graded conjecture
— not as an established result. The chapter is honest about the fact
that GRID does *not* predict h, α, or absolute scales; it predicts
dimensionless structure and identifies the load-bearing import.
