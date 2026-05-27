# STATUS — sheet-proton work file tracker

Living document. Tracks the work files' states and what each one
contributes to the chapter arc. Update as work progresses.

**Project state:** **Active** (resumed 2026-05-26). The earlier
on-hold annotation (2026-05-16) reflected an exploratory pause
while the dim-sharing reframe was moved to [ma-domain](../../ma-domain/).
The two projects now run in parallel: ma-domain is the
multi-generation reframe; sheet-proton is the single-generation
worked example. The arc has settled on the half-twist τ = 1/2
modulated-clover (work/modulated-clover.md, work/derived-clover.md),
which supersedes the older τ = 1/3 clover-quarks mechanism for
the purposes of the chapter arc. The chapter arc is in
[../README.md §Chapter arc](../README.md#chapter-arc); chapter
prose is currently being drafted starting with
[../01-foundation.md](../01-foundation.md).

---

## Work files by role

### Foundational — the construction the chapter arc rests on

- **[modulated-clover.md](modulated-clover.md)** — the operative
  substrate construction. Step-by-step derivation: cross-section
  budget (Step 1), modulation/track solver (Step 3), mass spectrum
  (Step 4), aspect-ratio sweep (Step 5), parameter sweep (Step 6),
  path-length mass mechanism (Step 7). The symmetric Step-7 result
  is the construction the arc commits to.
- **[derived-clover.md](derived-clover.md)** — formal derivation
  framework: hypothesis chain C1–C6, per-arc charge integral,
  inverse-spectral-problem framing, the Z₂ × Z₃-symmetric finding,
  discrete-symmetry structure, quark-substructure framing.

### Computational findings folded into the arc

- **[lb-mode-localization.md](lb-mode-localization.md)** —
  numerical test of whether any LB eigenmode (or low-energy
  superposition) on the modulated-clover is track-localised.
  **Negative result.** Folded into the chapter-arc framing as the
  reason the wave-quantum's amplitude is *not* track-localised
  while its charge content is along-the-track.
- **[quark-decomposition.md](quark-decomposition.md)** — first
  attempt at the 3-quarks-in-series test. Equal-θ-segment
  integration of the (1/2, 1) track charge gives uniform per-segment
  values (+1/3, 0) — the Z₃ symmetry forces equality. Established
  that the per-arc fractional charges live in the *cross-section*
  integral, not the track integral.
- **[quark-wannier-decomposition.md](quark-wannier-decomposition.md)** —
  *exploratory record (demoted 2026-05-26).* Wannier-function
  formalisation of "3 superimposed wave packets per track" agreed
  with the simpler 3-arc-pieces-in-series picture without adding
  predictive content. The durable finding — piecewise-circular vs
  smooth-Fourier per-arc winding — is folded into the arc; the
  Wannier machinery itself is kept available for future chapters
  that may need quark-quark interference.

### Frontier / out-of-scope-for-current-arc

The following work files explore territory beyond the seven-chapter
arc's scope. Listed for orientation; not load-bearing for the arc.

- **[clover-quarks.md](clover-quarks.md)** — *predecessor
  construction (superseded).* Used τ = 1/3 with piecewise-circular
  arcs. Conceptually instructive but superseded by the
  modulated-clover; not load-bearing.
- **[clover-mass.md](clover-mass.md)** — analytical mass spectrum
  on the corrugated torus. Used in the older τ = 1/3 line.
- **[clover-modes-analytical.md](clover-modes-analytical.md)** —
  structural analysis of why 2-D Hill modes can't host multi-generation
  mass hierarchies on the 2-D surface. Negative-result analysis.
- **[3-gen.md](3-gen.md)** — three-generation-mechanism survey;
  negative verdict for the 2-D-surface case, 3-D wave-guide
  candidate remains.
- **[tube-waveguide.md](tube-waveguide.md)** — 3-D wave-guide
  extension; potential route to multi-generation mass hierarchy.
- **[clover-on-clover.md](clover-on-clover.md)** — fractal /
  nested extension explored as a multi-generation candidate.
- **[clover-inverse.md](clover-inverse.md)** — inverse-spectral
  formulation; reframed in derived-clover.md.
- **[quark-flavor.md](quark-flavor.md)** — quark structure as
  canceling primitives. Cross-references metric-charge.
- **[meson-spectrum.md](meson-spectrum.md)** — light-meson
  framing; not yet derived.
- **[strong.md](strong.md)** — strong-force / mediator framing;
  not yet derived.

---

## Open work items

These are the named gaps the arc *can in principle* close with
further work. See [../README.md §Open questions inside the
construction's scope](../README.md#open-questions-inside-the-constructions-scope)
for the README-level statement.

- **Closed-form charge integral.** Push M(t₀) = Q(t₀) − ½ to an
  analytical expression in the modulation parameters via
  Weierstrass substitution. Currently first-order expansion +
  numerical verification.
- **(1/2, 1) winding outside standard closure.** The half-integer
  tube winding sits outside metric-charge Ch 4's closure-mode
  derivation. The construction works around this by building the
  half-twist into the substrate; whether the (1/2, 1) modes are
  closure-satisfying *in the substrate-extended sense* is open.
  Flagged in [modulated-clover.md §6](modulated-clover.md).
- **R_major as a free parameter.** The absolute mass scale of the
  baryon doublet depends on R_major, which the construction does
  not yet derive from a deeper principle. Identifying an
  independent input that pins R_major would convert m_p from
  calibration to prediction.

---

## Open architectural questions

- **R64 Point A vs Point B reconciliation.** The earlier R64
  proton-sheet (ε, σ) parameter fits operate in a different
  parameterisation than the modulated-clover. Relationship is open
  but not load-bearing for the chapter arc.
- **Multi-sheet hadrons** (Λ, Σ, Ξ, Ω). Require a coupling
  mechanism between sheets of different generations; the mechanism
  lives in [metric-binding](../../metric-binding/) and/or
  [ma-domain](../../ma-domain/), not on this sheet.
- **Spinor upgrade.** Required for: spin-½ structure, magnetic
  moments, Δ baryons (spin-3/2), and the γ⁵-chirality vs
  intrinsic-parity distinction. Forward-looking; not part of the
  current arc.

---

## Cross-reference: sibling projects

- [metric-charge](../../metric-charge/) — generic 2-D-sheet framework
  this project specialises (Ch 1, Ch 4, Ch 6, Ch 11 are inherited).
- [metric-mass](../../metric-mass/), [metric-binding](../../metric-binding/) —
  generic frameworks this project draws from; see README §Background
  reading.
- [ma-domain](../../ma-domain/) — downstream multi-generation
  reframe; sheet-proton's settled half-twist construction is the
  worked example ma-domain inherits.

---

## Notes on workflow

1. Work files are exploratory. They evolve. Retiring or merging
   files is encouraged when hypotheses settle.
2. When a work file's main hypothesis converges, its content
   graduates to chapter prose in this project's chapter arc.
3. Computational scripts live in [`../scripts/`](../scripts/); use
   Python with numpy, scipy, and matplotlib.
4. Cross-reference liberally between work files; the dependency
   structure is real.
