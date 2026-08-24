# Projects

Educational, exploratory work that develops intuition about the MaSt
framework. Projects are free to take long, indirect, or pedagogical
side-paths in the service of learning. They are not required to
produce a result that pushes the production model forward.

This is the deliberate counterpart to [studies/](../studies/), which
hold the project's main computational research thread.

## Projects vs. studies

| | [Studies](../studies/) | Projects |
|---|---|---|
| **Primary purpose** | Push the model forward | Develop intuition |
| **Style** | Computational, hypothesis-driven | Mixed: derivation, viz, toy code |
| **Goal** | Confirm/refute a specific claim | Understand a concept thoroughly |
| **Side-paths** | Avoided — stay focused on the question | Welcome — that's the point |
| **Outputs** | Findings files tied to tracks | Whatever serves the learning goal |
| **Closure** | When the question is answered | When the user feels they understand |
| **Audience** | Future-self verifying past results | Future-self (or others) building intuition |

Studies are about answering questions efficiently. Projects are about
building the mental machinery that makes future questions easier to
ask.

A project may produce derivations, primers, visualizations,
small-scale toy simulations, comparative analyses, or annotated
explorations of literature. A project may also produce pieces that
later get promoted into [primers/](../primers/) or
[studies/](../studies/) — but it doesn't have to.

## Phase structure

Projects can grow into multi-phase work with subdirectories.
Treat them like long-form pedagogical investigations: build
understanding incrementally, take detours when they're
illuminating, and don't force a conclusion on a fixed schedule.

Each project's README should:
- Explain the question or concept being explored
- Sketch the phases (early ones in detail, later ones as a pool)
- Note what success looks like (often: a clear mental model, not a
  number)
- Link to relevant studies, primers, or qa entries

## Active projects

- [metric-mass/](metric-mass/) — Build the metric from the minimum
  number of dimensions needed to see mass generation. Backs up from
  R-track's 11D complexity to develop intuition about what each
  metric component does. **Status: provisionally complete.**
- [metric-charge/](metric-charge/) — Follow-up to metric-mass,
  taking up the analogous question for charge on a 2D compact
  sheet. **Status: framed; awaiting first chapter.**
- [metric-binding/](metric-binding/) — Follow-up to metric-charge,
  taking up multi-knot interactions on a 2D sheet — energy at
  separation, force laws, bound-state regimes. General-framework
  work files in [work/](metric-binding/work/) (cancellation,
  partial knots, Z₃ confinement, particle/mediator vocabulary).
  **Status: work-file-driven; holding pattern while sheet-proton
  advances.**
- [sheet-proton/](sheet-proton/) — Proton-sheet-specific
  exploration: what does the sheet hosting the proton, neutron,
  and nuclear physics uniquely look like? Quark-flavor mappings,
  meson spectrum, Yukawa mediator for strong force, corrugated-
  torus geometry candidate. **Status: active; work-file-driven;
  initial computational results pending.**
- [grid-quantization/](grid-quantization/) — A GRID-only account of
  why light is quantized, and whether h and α can be *derived* (not
  assumed) from lattice recirculation loops. Tests the
  [Q140](../qa/Q140-light-quantization-from-recirculation.md)
  conjecture. **Status: Tier 1 done — single-hexagon energy return
  (2/3)¹² = 1/129.75 sits in α's running range; Tier 2 (h-universality
  / RG fixed point) not started.**
- [grid-gravity/](grid-gravity/) — Mechanical, substrate-level models in
  which mass (a compact standing wave) varies *local time* for nearby
  waves — the microscopic counterpart to
  [grid/gravity.md](../grid/gravity.md)'s statistical (Jacobson)
  derivation. Several candidate mechanisms under one shared gate (vacuum
  field, massless 1/r, non-dispersive, coefficient — all tracing to
  losslessness). **Status: parked — blocked on a foundations gap, not
  refuted.** Two theses explored; mechanism 1 (congestion) fails the
  vacuum-field test. Mechanism 2 (detour/refractive): a gauge-invariant
  derivation shows the local coupling *is* a refractive index (metric/kinetic,
  non-dispersive, energy-sourced) — an earlier "photon mass" read was a gauge
  artifact — so it is **not refuted**, but it is **blocked on range**: a 1/r
  field needs a massless, neutral, propagating carrier, and GRID's spectrum has
  none (photon = massless but charge-coupled; KK = neutral but Planck-massive;
  the ℵ-line size is a per-particle parameter, not a field). The **thesis**
  (mass → local-time gradient → gravity) stays open; forma's Jacobson route
  (metric as equation-of-state, needing no such carrier) is the fallback.
  Revival needs a substrate-level result making the ℵ-line size a massless
  field.**
- [grid-saturation/](grid-saturation/) — Whether the **bounded/saturating**
  GRID substrate (the same discrete-max bound posed for light-quantization)
  reproduces, as *dynamics*, the quantum phenomena the linear grid can't:
  the quantization threshold, **pair production** (energy S ↔ compact),
  single-quantum **instantiation/collapse**, and the **Born rule** (∝ |field|²
  from energy density). Tested on a minimal 1D-space + 1D-compact **(x,c)
  cylinder**. Key insight: the "missing nonlinearity" *is* the saturation.
  **Status: new; substrate dynamics posed but unsimulated. First step is the
  linear cylinder baseline (KK decoupling / pass-through, never tested
  dynamically in forma), then a *conserving* saturation (excess spills S→c)
  to test pair production and the Born rule.**
