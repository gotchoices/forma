# Theory of the Universe

A project of [GotChoices.org](https://gotchoices.org)

## About this project

What started as a hobby — an engineer's "what if" exploration
of a 1997 paper proposing the electron is a confined photon —
has yielded some remarkable results: percent-level particle
mass predictions from geometry alone, an emergent neutron that
nobody put in by hand, and a neutrino mass ratio that falls
out of integer winding numbers.

I don't claim the model is correct.  It may be coincidence,
numerology, or something deeper.  But it is *interesting* — and
it may offer fresh angles on some of physics' unsolved problems,
from the origin of mass to the nature of dark matter.

**This project does not compete with the Standard Model.**
The Standard Model works — its predictions are confirmed to
extraordinary precision.  But it requires ~25 free parameters
(particle masses, coupling constants, mixing angles) that are
measured, not explained.  MaSt/GRID attempt to derive those
parameters from a simpler starting point: the geometry of a
compact six-dimensional space.

Model-E uses **7 measured inputs** to derive the rest:

| Input | What it sets |
|-------|-------------|
| α = 1/137 | Ma-S coupling strength |
| m_e | electron ring scale |
| m_p | proton ring scale |
| Δm²₂₁ | neutrino ring scale |
| m_μ / m_e | e-sheet aspect ratio and shear |
| m_τ / m_e | (same — two ratios fix two parameters) |
| Δm²₃₁ / Δm²₂₁ | neutrino shear |

Of these, 3 are dimensional scales (every theory needs units)
and **4 are dimensionless** (α, m_μ/m_e, m_τ/m_e, Δm² ratio).
The Standard Model has ~19 dimensionless parameters.  Model-E
reduces this to 4 — and if GRID derives α from the lattice,
potentially **3**.

From these inputs, model-E derives: 20 particle masses, nuclear
masses from deuterium to iron, three lepton generations, charge
quantization, neutrino oscillation, and ghost-mode elimination.

For background on who built this, how AI was used, and how to
judge what you're reading, see [DISCLAIMERS](DISCLAIMERS.md).

Please clone this repo and encourage your friends to do the same.
If you have the scientific background to review some
of the studies contained here, please help out!

**New here?** The [`papers/`](papers/README.md) folder offers three
entry paths — scientific, intuitive, and reflective — depending on
how you like to learn.  Start with
[What If?](papers/whatif.md) for the core idea in plain language, or
[Matter from Light](papers/matter-from-light.md) for the full
technical story.


## The big picture

This project attempts a unified geometric account of
fundamental physics — including gravity — from two free
parameters and a discrete lattice.

The work is organized in two layers:

**[GRID](grid/README.md)** (Geometric Relational Interaction
Domain) is the substrate: a minimal 4D causal lattice whose
phase dynamics produce Maxwell's equations and whose
information density produces Einstein's field equations and
the gravitational constant G.  GRID derives both long-range
forces from six axioms without importing either one.  Beyond
the theoretical derivations, GRID provides a functional
mechanical model of the spacetime fabric: a hexagonal lattice
where edges carry standing-wave modes, junctions scatter
energy by impedance matching, and curvature arises from
pentagonal defects.  Simulations confirm that this lattice
propagates directional waves (no Maxwell input), superposes
them exactly, and accommodates Schwarzschild geometry — the
event horizon is not a lattice failure, but the physical
singularity is.  See [`grid/synthesis.md`](grid/synthesis.md)
for what has been established.

**MaSt** (Material – Space – time) is the architecture built
on that substrate: six compact dimensions where particles are
standing electromagnetic waves.  MaSt takes Maxwell's equations
(now derived by GRID) and the coupling constant α as inputs,
then produces the particle spectrum, masses, charges, nuclear
structure, and plausible mechanisms for the strong force (Q95)
and matter–antimatter asymmetry (Q97).  Quantum behavior in
MaSt is not postulated — it emerges from wave mechanics on
compact geometry: quantized energy levels are standing-wave
modes, uncertainty is the Fourier bandwidth limit, and spin
is winding topology.

Together, GRID + MaSt attempt to unify general relativity with
quantum field theory through a common geometric substrate.

## The MaSt Continuum

**MaSt** = **Ma**terial – **S**pace – **t**ime.

The framework proposes that spacetime has six additional
compact ("material") dimensions — three pairs forming
material sheets — where particles are standing waves of
confined electromagnetic energy.  The full arena is
**Ma × S × t** (6 + 3 + 1 = 10 dimensions).

See [`studies/Taxonomy.md`](studies/Taxonomy.md)
for the full framework reference.

| Symbol | Name | Dimensions | What it is |
|--------|------|:----------:|------------|
| Ma | Material space | 6 | The compact dimensions; three periodic sheets |
| Ma_e | Electron sheet | 2 | Modes: electron, muon, tau |
| Ma_ν | Neutrino sheet | 2 | Modes: neutrino mass eigenstates |
| Ma_p | Proton sheet | 2 | Modes: proton, hadrons, nuclei |
| S | Space | 3 | The three large spatial dimensions |
| t | Time | 1 | Time |

The three sheets (3Ma) have vastly different scales:

| Sheet | Size | Mode energy | Particle family |
|-------|------|-------------|-----------------|
| Ma_p | ~fm | ~GeV | Proton, hadrons |
| Ma_e | ~pm | ~MeV | Electron, muon, tau |
| Ma_ν | ~μm–mm | ~meV (THz) | Neutrinos |


## Guiding principle

**Energy and geometry are the only fundamentals.**

Mass, charge, spin, and magnetic moment are all emergent:

| Property  | Emerges from                          |
|-----------|---------------------------------------|
| Mass      | Energy confined in periodic geometry  |
| Charge    | Shear of the material sheet lattice   |
| Spin      | Winding ratio of geodesic (p:q)       |
| Mag. mom. | Axial projection of compact B field   |

Conservation laws are emergent too — but exact.  Mass
conservation is energy conservation.  Charge conservation
is topological winding-number conservation (you can't
smoothly unwrap a path on a material sheet).  Spin
conservation is geodesic topology.  These are exact because
topology is exact.

The only true inputs are: (1) the existence of energy
(photons), (2) the existence and shape of material
dimensions (Ma), and (3) the rules of propagation (Maxwell's
equations — now derived by [GRID](grid/README.md) from a
discrete lattice).  Everything else — the particle zoo, their
properties, their interactions — should follow.

GRID's six axioms ([`grid/foundations.md`](grid/foundations.md))
now derive both Maxwell's equations and gravity from this
principle.  See [`studies/Taxonomy.md`](studies/Taxonomy.md) §6
for the full mechanism catalog.


## Models

The MaSt model has evolved through five generations.  The
**current model is model-E** — a full T⁶ metric with generation
structure and compound modes on 20 of 20 surveyed particles.

| Model | Era | Key idea | Status |
|-------|-----|----------|--------|
| [model-A](models/model-A.md) | S1–R25 | WvM / single-sheet electron | Superseded |
| [model-B](models/model-B.md) | R26–R38 | Three tori / `ma.py` — first particle predictions | Superseded |
| [model-C](models/model-C.md) | R39–R44 | Generalized model / `ma_model.py` — dynamic torus, dark matter, electroweak | Superseded |
| [model-D](models/model-D.md) | R45–R52 | Filtered model / `ma_model_d.py` — waveguide cutoff, (1,3) proton, GRID integration | Superseded |
| [model-E](models/model-E.md) | R53–R55 | Full T⁶ with generation structure — 20/20 particles, shear resonance, 9×9 metric | **Active** |

**Headline results** (model-E; see [`models/model-E.md`](models/model-E.md)):

- **20 of 20 surveyed particles have credible modes** — stable
  particles (proton, electron) are exact eigenmodes; all unstable
  particles are near-misses with gaps consistent with their
  instability
- Three charged lepton generations from in-sheet shear resonance —
  mass ratios algebraically exact from geometry
- Nuclear masses from deuterium to iron at ≤ 1.1%
- Neutrino mass-squared ratio Δm²₃₁/Δm²₂₁ = 33.6 from integer
  winding numbers (exact, parameter-free).
- Emergent neutron — a three-sheet mode nobody put in, found by
  the solver.
- Nuclear scaling law: nuclei as Ma_p modes match d → ⁵⁶Fe at < 1%.
- Plausible geometric mechanisms for dark matter, the strong force,
  and matter–antimatter asymmetry.

**What model-E changes** (see [`models/model-E.md`](models/model-E.md)):
model-E treats the six compact dimensions as one T⁶ (not three
independent sheets), with a 9×9 metric whose off-diagonal entries
serve four distinct roles: in-sheet shears for generation structure,
cross-sheet entries for compound modes, Ma-S entries for α coupling,
and flat space.  Three lepton generations emerge from shear resonance.
The (1,1) ghost is eliminated by shear ordering, not waveguide cutoff.
Charged pion spin barrier broken via multi-sheet tube windings.
Charge sign originates from opposite Ma-S coupling: e-sheet → S is
negative, p-sheet → S is positive.


## Foundation

This project builds on a line of thought running through a
century of physics:

**de Broglie (1924)** proposed that particles *are* waves,
with wavelength λ = h/p.  This was the first suggestion that
matter and waves are the same thing, not merely analogous.
MaSt takes this literally: particles are standing
electromagnetic waves on material geometry.

**Schrödinger (1926)** originally conceived his wave equation
as describing a real physical wave — not a probability
amplitude.  He was deeply uncomfortable with Born's
statistical interpretation and spent decades defending the
reality of the wave.  His discovery of *zitterbewegung*
(trembling motion at the Compton scale in the Dirac equation)
hinted at real circular motion underlying particle structure.
MaSt vindicates Schrödinger's intuition: the wavefunction on
Ma is a real electromagnetic standing wave, and the
zitterbewegung is the photon circulating on the (1,2)
geodesic.

**Kaluza (1921) and Klein (1926)** showed that a single
compact extra dimension, appended to Einstein's four-dimensional
spacetime, produces electromagnetism from pure geometry —
the electromagnetic potential is the off-diagonal component
of the 5D metric.  MaSt extends KK from one compact
dimension to six (Ma = 3 × material sheets), producing not
just electromagnetism but the full particle spectrum: masses,
charges, spins, and decay patterns.  R36 showed that the KK
gauge field is not an assumption imposed on the model — it
*emerges* from solving the wave equation on compact × non-compact
space.

**Williamson and van der Mark (1997)** ([PDF][wvm],
[video overview][wvm-video]) proposed the specific mechanism:
an electron is a single photon confined to a (1,2) torus knot.  The model reproduces spin ½
(exact, topological) and charge ≈ 0.91e (approximate,
geometric).  This project extends WvM into the MaSt
framework: the photon lives on a flat material sheet
(a periodic 2-dimensional surface), and the electron's
properties emerge from the geometry of that surface.  The
neutrino crisis — uncharged spin-½ particles are impossible
on a single sheet (R25) — forced the architecture from one
sheet to three (3Ma = Ma_e × Ma_ν × Ma_p), yielding Ma (R26).

[wvm]: https://fondationlouisdebroglie.org/AFLB-222/MARK.TEX2.pdf
[wvm-video]: https://www.youtube.com/watch?v=hYyrgDEJLOA&t=1690s


## Structure

- `models/` — **Model documentation**: versioned writeups of each
  MaSt model generation (A through D).
  See [`models/README.md`](models/README.md).
- `grid/` — **GRID** (Geometric Relational Interaction Domain):
  the substrate layer.  Derives Maxwell + Einstein from a discrete
  lattice.  See [`grid/README.md`](grid/README.md).
- `studies/` — Questions that require a computational model to answer.
  See [`studies/STATUS.md`](studies/STATUS.md) for the registry.
- `qa/` — Physics questions answered by logic and existing theory
  (no computation).  See [`qa/README.md`](qa/README.md).
- `papers/` — Authored documents presenting theories, results, and
  proofs.  See [`papers/README.md`](papers/README.md).
- `primers/` — Self-contained tutorials on topics needed to follow
  the studies.  See [`primers/README.md`](primers/README.md).
- `labs/` — Proposed physical experiments to test predictions of the
  model.  See [`labs/README.md`](labs/README.md).
- `viz/` — Interactive browser-based visualizations.
  See [`viz/index.html`](viz/index.html).
- `reference/` — Source material by others and recorded conversations.
- `lib/` — Shared Python code (Ma solver, mode search, metrics).


## Navigation

| File | Purpose |
|------|---------|
| [`models/model-E.md`](models/model-E.md) | **Current model** (active) — full T⁶ with generation structure, 20/20 particles, 9×9 metric |
| [`models/model-D.md`](models/model-D.md) | Previous model — filtered model with waveguide cutoff and (1,3) proton |
| [`models/model-C.md`](models/model-C.md) | **Latest quantitative predictions** — particle tables, parameter census, full results |
| [`models/README.md`](models/README.md) | Model index: all four generations (A–D) |
| [`STATUS.md`](STATUS.md) | Project-level status: mission, active front, open problems |
| [`studies/Taxonomy.md`](studies/Taxonomy.md) | **MaSt framework reference:** dimensions, geometry, particle catalog, mechanisms |
| [`grid/README.md`](grid/README.md) | **GRID** — substrate layer: derives Maxwell + G from a discrete lattice |
| [`studies/STATUS.md`](studies/STATUS.md) | Study-by-study registry: active, backlog, done |
| [`qa/Q84-mast-terminology.md`](qa/Q84-mast-terminology.md) | MaSt naming conventions and migration guide |
| [`qa/README.md`](qa/README.md) | Index of answered and open physics questions |
| [`qa/INBOX.md`](qa/INBOX.md) | Capture queue for new questions |
| [`papers/README.md`](papers/README.md) | Papers: matter-from-light, sub-quantum memory, atoms-from-geometry, universe-as-mode |
| [`primers/README.md`](primers/README.md) | Tutorials: matrix notation, Maxwell, KK theory, charge-from-energy |
| [`labs/README.md`](labs/README.md) | Proposed physical experiments to test model predictions |
| [`reference/WvM-summary.md`](reference/WvM-summary.md) | Living summary of the foundational WvM paper |
| [`viz/index.html`](viz/index.html) | Browser launcher for all interactive visualizations |


## License

This work is licensed under
[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
You are free to share and adapt this material for any purpose, including
commercial, provided you give appropriate credit to
[GotChoices.org](https://gotchoices.org) and distribute any derivative
works under the same license.  See [LICENSE](LICENSE) for details.
