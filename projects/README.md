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
  field.** *Update:* the scope now permits substrate extensions (itemized per
  mechanism). **Mechanism 3** ([note](grid-gravity/work/sync-carrier-mechanism.md))
  — lossless stores on nodes and space-links, set by a stored deflection — has
  been taken through a five-step validation plan: it slows every mode alike,
  makes bodies fall as 1/r² and bends light by the full amount (on one stated
  premise), sources its field from an action in proportion to energy, carries it
  at light speed, and reproduces weak-field general relativity to second order;
  in its cheapest form gravity is the steady part of the one field that carries
  light and matter. **Status: objective met for the *static* sector, conditionally on a listed
  ledger of posits; the *dynamic* sector (tensor gravitational waves,
  frame-dragging) is open — the mechanism's single scalar deflection does not yet
  reach it; the statistical (Jacobson) account is taken as the same phenomenon at
  a coarser level, judged by consistency rather than re-derivation; chapter arc
  drafted**
  ([tracker and objectives audit](grid-gravity/work/STATUS.md)). The statistical
  side is kept in [entropic-route](grid-gravity/work/entropic-route.md); an EM
  slot is held open in [em-slot](grid-gravity/work/em-slot.md).
- [grid-matter/](grid-matter/) — Whether GRID produces **matter and quantum
  mechanics**, beyond EM and gravity. (Formerly `grid-saturation`: the entry
  hypothesis — that the *saturation bound* makes particles — was **refuted**
  (the bound is defocusing); the real answer is the **compact phase**.)
  **Act 1 (matter) — largely done:** particles are compact-phase solitons
  (**breather = mass, kink = charge**); relativistic matter waves + de Broglie +
  the **KK mass tower** are measured; stability = a protected winding; the
  light→mass→charge **promotion ladder** ([grid-duality](grid-duality/) ch.7) is
  confirmed dynamically. **Act 2 (quantum mechanics) — frontier:** two-slit
  interference and **single-particle Born** (energy density + whole-quantum) on a
  GRID lab, **collapse dissolved**; the one open core is **entangled Born / Bell**.
  **Status: active; work-file-driven; a chapter arc is drafted in its README.**
- [grid-scattering/](grid-scattering/) — **What sets the rate at which energy
  crosses between GRID's compact sectors, and into space?** Tests saturation and
  overflow as the mechanism: above a ceiling, overflow carries energy across in
  bulk between a node's space group and its sheet group. The ceiling is not free
  — ordinary light must pass below it, which makes the Schwinger limit a
  prediction rather than an input. Fills the gap [ma-domain](ma-domain/) names in
  `work/leakage-rate.md`. *Not a revival of `grid-saturation`: that concerned
  binding, this concerns transfer.*
  **Status: parked — one result, one refutation.** The channel is exactly
  energy-conserving, is gated by the ceiling, and needs a symmetry-breaking seed
  it provably cannot supply itself (a symmetric state under a symmetric rule
  stays symmetric: a million overflow events give zero winding with the
  background off). **Refuted:** the frequency selection the project was built
  around — the structure tracks the simulation box, not the ring, so the ~5×,
  12–58% and 50–100× figures and the per-sheet threshold inference are all
  withdrawn. **Motion is not this project's result:** the ordinary pooled scatter
  supplies Kaluza–Klein dispersion exactly (even in k_x, zero group velocity at
  rest, massless light) while being local and reciprocal, three bespoke
  couplings built before it was tried all failed, and the project's own channel
  *pins* a moving packet above a threshold. Revival is cheapest at a reciprocal
  overflow rule.
