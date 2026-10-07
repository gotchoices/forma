# STATUS — grid-scattering checklist

Living document. Tracks what is settled, what is running, and what is queued.
Project framing: [../README.md](../README.md). Supporting detail: [../Appendix.md](../Appendix.md).

**Where things stand (2026-10-07).** The arena is built and the mechanism fires. Energy crosses from the line into a ring on overflow, the crossing is **resonant** (50–100× at nc = mλ, sharp to one node), the resonance selects the predicted mode, and at the strongest resonance the reverse channel opens on its own. The junction-geometry question is settled analytically, and with it the review's F1. Nothing yet shows a particle that *moves*, which is the next thing to find out.

---

## Settled

- [x] **Arena.** One linear array x; a ring at every x coordinate; line and ring joined only during an overflow, at one point. An (nx × nc) product grid is *wrong* — it is nc parallel lines, so a photon saturates every ring at once and injects uniformly, giving winding 0 and no particle. [first-run.md](first-run.md)
- [x] **The mechanism transfers.** Collision above the ceiling, overflow into the ring, ~89% of it circulating with no seed needed — one-point injection is inherently non-uniform. [first-run.md](first-run.md)
- [x] **Transfer is resonant.** 50–100× enhancement at nc = mλ, one node either side kills it; needs a *sustained* drive, since a single pulse injects once and has nothing to interfere with. [first-run.md](first-run.md)
- [x] **Resonance selects the predicted mode.** nc/λ = 1, 2, 3 → n = 1, 2, 3. [first-run.md](first-run.md)
- [x] **Reverse channel exists.** 1181 ring → line events at the strongest resonance, with no extra rule. [first-run.md](first-run.md)
- [x] **Junction geometry.** Uniform is forced at a symmetric Y junction; at an X junction there are exactly four symmetric rules and no continuous knob, so weak coupling must be nonlinear. [junction-geometry.md](junction-geometry.md)
- [x] **F1 answered.** A moving particle is a soliton bound by saturation; the geometry permits both motions, the nonlinearity binds them. [junction-geometry.md](junction-geometry.md)
- [x] **Maxwell not at risk.** The partition is S against a sheet, not dimension against dimension, so the spatial sector is unchanged. [junction-geometry.md](junction-geometry.md)

## Queued — experiments

Ordered so each can fail cheaply and early. Pre-register the expected answer before running.

- [ ] **E1 — Does energy stay in the ring?** Inject, stop driving, watch the ring. With the reverse channel on there should be a **lifetime**; measure it, and see whether it depends on how much is stored and on which mode. This is the first thing that could become a decay *rate*, which objective 2 needs.
- [ ] **E2 — The angled shot: a standing wave in c with motion in x.** Inject into both groups at the same instant and node, with a controlled ratio — most of the shot going straight, a component making the turn. Does the result translate as **one object**, keeping its winding?
  *Pre-register:* with saturation on, it should hold together; with it off, the x-part should run ahead at the lattice speed and the c-part stay put, shearing apart within a few ticks. If it holds together with saturation **off**, §4 of junction-geometry.md is wrong and should be rewritten.
- [ ] **E3 — Does it have inertia?** If E2 gives a bound helix, sweep its x-momentum and winding number and fit the total energy. *Target:* ω² = c²k² + ω₀², the relation that makes compact momentum behave as mass. [grid-matter ch. 4](../../grid-matter/04-matter-waves-and-de-broglie.md) has it to <2% for the pooled scatter, so the comparison is direct.
- [ ] **E4 — Does mass grow with velocity?** With E3 in hand, push the helix harder and check E² = (pc)² + (mc²)² — relativistic dispersion, with the rest mass set by the winding. **This is special relativity, not general**; gravity stays with [grid-gravity](../../grid-gravity/). A pass here would be the project's strongest result.
- [ ] **E5 — Re-run the scatter discriminator on the current arena.** The clean per-sheet-vs-pooled A/B was measured on the superseded product grid. Needs repeating with a pooled junction as the control arm.
- [ ] **E6 — Sweep ω at fixed nc.** Confirms the condition is nc = mλ rather than a coincidence of the sizes chosen.
- [ ] **E7 — Report energy drift.** Now measurable (background jitter defaults off) but not printed. Amplitude is moved, energy goes as amplitude squared, so the books will not balance; the size and sign of the gap is data.

## Queued — writing

- [ ] Fold junction-geometry.md's result into README §2: grouping is no longer the mechanism, junction geometry plus nonlinearity is.
- [ ] Retire [Appendix §H](../Appendix.md) (the per-sheet node's provenance), superseded by junction-geometry.md.
- [ ] Update the index entry in [../../README.md](../../README.md) once §2 changes.

## Open questions

- **How small is "essentially nothing"?** The ideal node never crosses below the ceiling. A real one might leak — from sub-threshold structure, or from rare background-driven saturation. Whether that residue is required, and whether it is what α measures, is unsettled.
- **Does the ring empty in quanta or continuously?** E1 should show which.
- **Is the arena below the minimum?** thoughts.md defines a group as a *sheet*, meaning a plane. The 1D × 1D reduction makes each group a single line. Deliberate, and fine for the crossing question, but a 2D compact sheet will be needed before anything about sheet-internal structure can be said.
