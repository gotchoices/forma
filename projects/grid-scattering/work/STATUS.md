# STATUS — grid-scattering checklist

Living document. Project framing: [../README.md](../README.md). All numbers with
provenance: [measurements.md](measurements.md). Supporting detail:
[../Appendix.md](../Appendix.md).

**PARKED (2026-10-07), with one result and one refutation.** The nonlinear
channel has a ceiling and carries energy across it, and needs a
symmetry-breaking seed it cannot supply itself. The **frequency selection the
project was built around is refuted** — the structure belongs to the simulation
box, not the ring. **Motion is not this project's result**: the ordinary pooled
scatter gives it exactly, and the project's own channel destroys it above a
threshold.

**The lesson worth keeping.** Three coupling rules were built to keep the
compact sectors from mixing and to supply motion. No rule was needed for the
first — a Bloch label does it — and the ordinary pooled scatter does the second
better than any of the three, while also being local and reciprocal. The whole
line was solving a problem the project created for itself. The second lesson is
about error bars: a ~5× effect was called "settled" from three overlapping
seeds, and eight seeds at a single frequency span a factor of 4.4.

## Settled

- [x] **Arena is a cylinder** (product lattice, rings joined along x).
- [x] **Overflow conserves exactly** — orthogonal rotation between register
      groups, audited drift 1.2 × 10⁻¹⁶. [§M1](measurements.md)
- [x] **The linear sector moves nothing across, at any amplitude** — exactly
      zero, and forced rather than posited. [§M2](measurements.md)
- [x] **The ceiling gates the channel** — nothing fires below it, winding leaves
      the background floor just above it. [§M4](measurements.md)
- [x] **The crossing needs a seed the rule cannot supply** — over a million
      overflow events give precisely zero winding with the background off.
      Exact, by equivariance. [§M4](measurements.md)
- [x] **The reverse channel runs unprompted.**
- [x] **Local rule adopted.** The earlier non-local `--one-point` argmax both
      departed from GRID locality and suppressed the effect it was credited with.
- [x] **The pooled scatter is the linear sector.** KK dispersion to 0.1% exact /
      2.6% for a packet, even in k_x exactly, group velocity exactly zero at
      rest, massless light, mass tower 1 : 1.99 : 2.96 — node-local and
      reciprocal. Not a result of this project. [§M3](measurements.md)

## Open

- [ ] **A reciprocal overflow rule.** The rotation pairs `+x` with `+c` and `−x`
      with `−c` — the same non-reciprocal pairing that broke the gradient
      coupling. Harmless in the window (even in k_x to 5 × 10⁻⁵) but it leaks
      asymmetry in the pinned regime. Coupling each compact register to *both* x
      registers is a one-line change. **Cheapest open experiment.**
- [ ] **Why the overflow pins a moving packet.** Above drive amplitude ≈ 0.9 the
      speed collapses to zero with energy still exactly conserved. Likely a
      strong amplitude-dependent local scatterer, i.e. self-localisation, but
      that has not been shown. [§M6](measurements.md)
- [ ] **Does the ring empty in quanta or continuously?** E1 below.
- [ ] **How small is "essentially nothing"?** An ideal node never crosses below
      the ceiling; a real one might leak, from sub-threshold structure or rare
      background-driven saturation. Whether that residue is required, and
      whether it is what α measures, is unsettled.

## Retracted

- [x] ~~Resonance at 50–100×~~, ~~12–58% over detuning~~, ~~~5× at the predicted
      circumference~~ → **refuted entirely.** The frequency structure tracks the
      x-box, not the ring: changing nc 24→36 moves the tower by a third and
      leaves the sweep unchanged within error bars. [§M5](measurements.md)
- [x] ~~Each sheet carries its own threshold, set by its circumference, landing
      at the particle's own mass scale~~ → built on the above.
- [x] ~~An intense optical laser makes no pairs because it misses the electron
      ring's resonance~~ → same.
- [x] ~~The linear half of the posit (sectors kept apart below the ceiling is a
      distinguishing choice)~~ → not a choice; forced by Bloch for *any* linear
      rule. [§M2](measurements.md)
- [x] ~~Wound modes have mass and move (gradient coupling)~~ → the band is not
      even in k_x and a mode at rest drifts at +0.107. The reported 0.0–0.7%
      agreement came from sampling only k_x ∈ [0, 0.10]. [§M7](measurements.md)
- [x] ~~Weak always-on coupling restores KK motion~~ → a constant rotation is a
      mass term; at θ = 0.1 light gains a gap ω = 0.1 at k = 0.
- [x] ~~A moving particle is a soliton bound by saturation~~ → contradicts the
      project's own ceiling calibration.
- [x] ~~Four discrete junction rules~~ → artifact of imposing per-node momentum
      conservation, with the wrong measure, when it is not required at all.
- [x] ~~"The fatal items were all added during review rounds"~~ → not accurate.
      The amplitude-moving rule was in the project's own framing from the start.

## Queued — experiments

Ordered so each can fail cheaply. Pre-register the expected answer before
running.

- [ ] **E1 — Reciprocal overflow.** Replace the `+x↔+c` / `−x↔−c` pairing with
      each compact register coupling to both x registers, same ceiling and gain.
      *Pre-register:* the §M6 pinning should weaken or vanish, and
      |v(−k) + v(+k)| should stay at the 10⁻⁵ level into the previously pinned
      regime. If the pinning survives a reciprocal rule, it is self-localisation
      and the mechanism genuinely obstructs motion.
- [ ] **E2 — Does energy stay in the ring?** Inject, stop driving, watch the
      ring. With the reverse channel on there should be a **lifetime**; measure
      it, and whether it depends on how much is stored and on which mode. This
      is the first thing that could become a decay *rate*, which objective 1
      needs to be more than "creation works".
- [ ] **E3 — The accumulation rate (objective 3).** Does repeated overflow build
      up, and how does that depend on drive strength and ring size? Needs E2
      first, since a build-up rate is meaningless without the loss rate.
- [ ] **E4 — Equipartition control.** The hard-driven runs thermalise to roughly
      half the energy wound, which is what a classical nonlinear lattice does
      and what §5 of the README says cannot yet be interpreted. Measure the
      approach to it so that any future selection claim can be stated as a
      departure from equipartition rather than as a raw fraction.
- [ ] **E5 — Pooled against grouped, on the current arena.** The discriminator
      that would show whether grouping buys anything observable at all. It was
      last measured on the superseded arena, and §M2 has since removed its
      original motivation, so it is now a check on whether the project has any
      linear-sector content left.
- [ ] **E6 — Resonance width, if E-anything revives frequency selection.** A
      resonance gives a peak, not a step; Breit–Wheeler is peaked but broad.
      Blocked on a geometry whose box modes are out of range of its ring modes
      (README §7.2).

## Queued — writing

- [ ] Update the index entry in [../../README.md](../../README.md) to match the
      parked verdict. *(Done 2026-10-07; re-check if the verdict moves.)*
- [ ] Retire [Appendix §H](../Appendix.md) (the per-sheet node's provenance) —
      superseded by [junction-geometry.md](junction-geometry.md), which has
      itself now been cut back to what survives.
- [ ] [first-run.md](first-run.md) is a withdrawn round kept for the audit
      trail. Leave it, but it should not be cited for any number.
