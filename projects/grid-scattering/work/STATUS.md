# STATUS — grid-scattering checklist

Living document. Tracks what is settled, what is running, and what is queued.
Project framing: [../README.md](../README.md). Supporting detail: [../Appendix.md](../Appendix.md).

**PARKED (2026-10-07) on a stated obstruction.** The mechanism works for what it was built for — energy crosses on overflow, the crossing is resonant at the predicted circumference, the reverse channel runs unprompted, and the rule conserves energy exactly. **But a particle made here cannot move through space**, and that is measured rather than feared ([measurements.md](measurements.md) §M4). Three attempts to supply motion have failed, each for the same underlying reason, and the reason is the project's own posit: motion of a compact mode needs space and the compact direction joined in one wave operator, which strict separation removes.

Parked rather than closed. The missing piece is specific: **a binding nonlinearity on the field value**, which [grid-matter](../../grid-matter/work/focusing-from-phase.md) already has and which already produces a mobile particle on this lattice. Revival conditions are in [../README.md](../README.md) §6.

## Settled

- [x] **Arena is a cylinder** (product lattice, rings joined along x).
- [x] **Overflow conserves exactly** — rotation between register groups, audited drift ~10⁻¹⁶.
- [x] **Nothing crosses below the ceiling, with no drive, or with no background** (the last is the equivariance check: the state breaks the symmetry, never the rule).
- [x] **Crossing is resonant at ~5×** at the predicted circumference, with 3× seed scatter. [measurements.md](measurements.md) §M3.
- [x] **The reverse channel runs unprompted**, and is what lets a ring shed energy.
- [x] **Local rule adopted.** The earlier non-local `--one-point` argmax both departed from GRID locality and suppressed the resonance.

## The obstruction

- [x] **A particle cannot move.** At rest it radiates symmetrically and decays in place (x-centroid 0.0000 at every amplitude); launched with x-momentum it shears apart (x content travels 41 nodes, compact content stays at 0). [measurements.md](measurements.md) §M4.

## Retracted

- [x] ~~Resonance at 50–100×, and 12–58× over detuning~~ → **~5×**, conserving rule, proper energy metric.
- [x] ~~A moving particle is a soliton bound by saturation~~ → contradicts the project's own ceiling calibration.
- [x] ~~Weak always-on coupling restores KK motion~~ → a rotation is a mass term, not a derivative coupling; at θ = 0.1 light gains a gap ω = 0.1 at k = 0.
- [x] ~~Four discrete junction rules~~ → artifact of imposing per-node momentum conservation with the wrong measure.
- [x] ~~"The fatal items were all added during review rounds"~~ → not accurate. The amplitude-moving rule was in the project's own framing from the start; the error was publishing ratios from it.

## Queued — experiments

Ordered so each can fail cheaply and early. Pre-register the expected answer before running.

- [ ] **E1 — Does energy stay in the ring?** Inject, stop driving, watch the ring. With the reverse channel on there should be a **lifetime**; measure it, and see whether it depends on how much is stored and on which mode. This is the first thing that could become a decay *rate*, which objective 2 needs.
- [ ] **E0 — Seed-average the resonance.** The surviving ~1.5× sits on a background that wanders 0.25–0.31. Average over seeds and give it an error bar before it is called a result at all.
- [ ] **E2a — Implement momentum-carrying overflow.** The excess should carry its x-momentum across; it currently does not. Prerequisite for E2–E4.
- [ ] **E2 — The angled shot: a standing wave in c with motion in x.** Inject into both groups at the same instant and node, with a controlled ratio — most of the shot going straight, a component making the turn. Does the result translate as **one object**, keeping its winding?
  *Pre-register:* with saturation on, it should hold together; with it off, the x-part should run ahead at the lattice speed and the c-part stay put, shearing apart within a few ticks. If it holds together with saturation **off**, §4 of junction-geometry.md is wrong and should be rewritten.
- [ ] **E3 — Does it have inertia?** If E2 gives a bound helix, sweep its x-momentum and winding number and fit the total energy. *Target:* ω² = c²k² + ω₀², the relation that makes compact momentum behave as mass. [grid-matter ch. 4](../../grid-matter/04-matter-waves-and-de-broglie.md) has it to <2% for the pooled scatter, so the comparison is direct.
- [ ] **E4 — Does mass grow with velocity?** With E3 in hand, push the helix harder and check E² = (pc)² + (mc²)² — relativistic dispersion, with the rest mass set by the winding. **This is special relativity, not general**; gravity stays with [grid-gravity](../../grid-gravity/). A pass here would be the project's strongest result.
- [ ] **E5 — Re-run the scatter discriminator on the current arena.** The clean per-sheet-vs-pooled A/B was measured on the superseded product grid. Needs repeating with a pooled junction as the control arm.
- [x] **E6 — Sweep ω at fixed nc.** Done. The resonance is at ω = 2π·m/nc exactly, confirmed at nc = 12, 18, 24, 36 with 12–58× retention over an 8% detuning. The threshold frequency is set by the **ring**, not by the ceiling — which is what lets one amplitude ceiling coexist with a different threshold per sheet.
- [ ] **E8 — Resonance width.** A resonance gives a peak; Breit–Wheeler is peaked but broad, and the arena's is sharp. Measure the width against the reverse-channel strength and see whether it can be broadened to match.
- [ ] **E7 — Report energy drift.** Now measurable (background jitter defaults off) but not printed. Amplitude is moved, energy goes as amplitude squared, so the books will not balance; the size and sign of the gap is data.

## Queued — writing

- [ ] Fold junction-geometry.md's result into README §2: grouping is no longer the mechanism, junction geometry plus nonlinearity is.
- [ ] Retire [Appendix §H](../Appendix.md) (the per-sheet node's provenance), superseded by junction-geometry.md.
- [ ] Update the index entry in [../../README.md](../../README.md) once §2 changes.

## Open questions

- **How small is "essentially nothing"?** The ideal node never crosses below the ceiling. A real one might leak — from sub-threshold structure, or from rare background-driven saturation. Whether that residue is required, and whether it is what α measures, is unsettled.
- **Does the ring empty in quanta or continuously?** E1 should show which.
- **Is the arena below the minimum?** thoughts.md defines a group as a *sheet*, meaning a plane. The 1D × 1D reduction makes each group a single line. Deliberate, and fine for the crossing question, but a 2D compact sheet will be needed before anything about sheet-internal structure can be said.
