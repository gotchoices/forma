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

For background on who built this, how AI was used, and how to
judge what you're reading, see [DISCLAIMERS](DISCLAIMERS.md).

Please clone this repo and encourage your friends to do the same.
If you have the scientific background to review some
of the studies contained here, please help out!


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

See [`qa/Q84-mast-terminology.md`](qa/Q84-mast-terminology.md)
for the full terminology specification.

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

See [`qa/Q27-foundational-axioms.md`](qa/Q27-foundational-axioms.md) and
[`qa/Q32-energy-geometry-fundamentals.md`](qa/Q32-energy-geometry-fundamentals.md)
for discussion.


## Key results

### Parameter accounting

The Ma geometry has 21 independent metric components (R26 F57).
Eight constraints from experimental data and particle fits leave
13 formally free — but 11 of these are cross-shear components
that are all zero and shown irrelevant to every observable tested
(R28 F1/F4).  The **effective free parameters are 2: r_e and r_ν**.

| What | Count | Details |
|------|------:|---------|
| Ma metric components | 21 | Flat 6×6 symmetric metric |
| Set by experimental inputs | 6 | 3 ring scales (m_e, m_p, Δm²₂₁); 3 within-plane shears (α → s_e given r_e, α → s_p given r_p, Δm² ratio → s_ν) |
| Pinned by particle fits | 2 | r_p = 8.906 and σ_ep = −0.091 (jointly by neutron + muon, R27 F18) |
| Cross-shears (irrelevant) | 11 | All set to 0; shown insensitive to MeV-scale spectrum (R28) |
| **Effective free** | **2** | **r_e** (unconstrained), **r_ν** (≥ 3.2) |

The MeV-scale hadron predictions (below) are insensitive to both
remaining free parameters — they depend almost entirely on r_p
and σ_ep.  In this sense the predictions are parameter-free.
The model as a whole has 2 undetermined shape parameters: r_e
has no known observable to pin it, and r_ν is only lower-bounded
(r_ν ≥ 3.2 from the cosmological Σm_ν bound).

See R26 F57–F63 and [`studies/Taxonomy.md`](studies/Taxonomy.md) §3
for the full census.

### Electron (R2, R19, R26)
The (1,2) mode on Ma_e reproduces spin ½ (exact, topological),
mass m_e (input), charge e (shear mechanism, requires α as
input given free r_e), g-factor ≈ 2 (energy partition), and
magnetic moment (axial B projection).

### Particle spectrum (R27, R28)
With r_p and σ_ep pinned by the neutron and muon (R27 F18),
the MeV-scale predictions are insensitive to both remaining
free parameters (r_e, r_ν).  Predictions:

| Particle | Ma mode | Error | Source |
|----------|---------|------:|--------|
| Kaon (K⁺) | (−4,−8,+1,0,−3,−1) | 1.2% | R27 F31 |
| Eta (η) | (−5,−8, 0,0,−5,+1) | 0.6% | R27 F31 |
| Eta prime (η′) | (−3,−8, 0,0,−3,+2) | 0.3% | R27 F31 |
| Phi (φ) | (−7,−8, 0,0,−7,+2) | 0.8% | R27 F31 |
| Lambda (Λ) | (−12,−15,+1,0,−12,−2) | 0.9% | R28 F10 |
| Sigma+ (Σ⁺) | (−14,−15, 0,0,−13,+2) | 0.3% | R28 F14 |

Lifetime-gap correlation r = −0.84 (p = 0.009) for weak
decays supports the off-resonance hypothesis: unstable
particles sit between eigenmodes, and the gap to the nearest
mode predicts the lifetime.

### Neutrino masses (R26)
The neutrino mass-squared ratio Δm²₃₁/Δm²₂₁ = 33.6 is
reproduced from integer mode numbers on Ma_ν with a single
shear parameter s_ν = 0.022.  The ratio is independent of r_ν,
which remains free (lower-bounded by cosmological Σm_ν).
Individual neutrino masses depend weakly on r_ν.

### Emergent neutron (R26, R27)
The neutron appears as a three-sheet mode (0,−2,+1,0,0,+2)
spanning Ma_e × Ma_ν × Ma_p (R27 F15).  Charge Q = −n₁ + n₅ = 0
(exact, both zero).  Spin ½ from neutrino ring winding (n₃ = 1).
Mass reproduced at σ_ep = −0.091 (R27 F18).  It was not put
in — it was found by the Ma solver as a mode nobody looked for.

### Nuclear scaling law (R29)
Nuclei are Ma_p modes, not multi-particle bound states.
The scaling law n_φp = A, n_θp = 2A (where A = mass number)
matches all nuclei from deuteron to ⁵⁶Fe at < 1% error.
Nuclear spins predicted correctly for 9 of 11 tested nuclei.

### Predictive horizon (R28)
Above ~2 GeV, the Ma mode spectrum becomes so dense (band
spacing < 5 MeV) that matching particles to modes ceases
to be discriminating.  Below ~2 GeV, the model is predictive.
W/Z/Higgs match trivially at high energy — not a test.

### Plausible explanations (not yet derived, but geometrically motivated)

Several phenomena that the Standard Model treats as separate
problems appear to have unified geometric explanations in MaSt.
These are plausible — the mechanisms are identified and the
arguments are self-consistent — but the quantitative derivations
are incomplete.

| Phenomenon | SM status | MaSt explanation | Reference |
|------------|-----------|-----------------|-----------|
| Dark matter | Unknown particle(s); no detection after decades of search | Ghost modes on Ma: exact charge symmetry, Compton window suppresses EM coupling, mass ratio brackets 5.4 | R42, Q94 |
| Strong force | Separate force with fitted coupling α_s | Internal EM between overlapping Ma tori at r ~ λ_C, unattenuated by Compton window; range, strength, and attraction emerge | Q95 |
| Matter–antimatter asymmetry | Requires CP violation beyond SM (CKM phase too small by ~10¹⁰) | Shear chirality of Ma breaks C and CP geometrically; all three Sakharov conditions met from geometry | Q97, Q32 |
| Nuclear binding | QCD confinement (non-perturbative, lattice-computed) | Nuclei are Ma_p modes, not multi-particle bound states; binding = mode transition on Ma | R29, Q89, Q95 |
| Force carriers (W, Z, gluon) | Fundamental gauge bosons | Possibly collective Ma excitations rather than fundamental fields; under investigation | Q96 |
| Three generations | Unexplained; SM accommodates but does not predict | Successive harmonics on Ma_e; dynamic filter orders them (FF(e) > FF(τ) > FF(μ)) but does not predict exactly three | R41, Q86 |

### What remains open
- **The α problem:** what determines the shear s ≈ 0.01
  of the electron sheet?  Multiple studies (R15, R19, R31,
  R32, R34) have constrained but not solved this.  α is
  the single most important unsolved parameter.
- **Ghost mode suppression:** the Compton window hypothesis
  (Q94) and dark matter reinterpretation (R42) are promising,
  but the window quality factor Q has not been computed from
  first principles.
- **The hierarchy:** why is gravity ~10⁴⁰× weaker than EM?
  GRID explains the mechanism — EM is local phase dynamics,
  gravity is collective thermodynamics — but the precise ratio
  depends on ζ and α, whose relationship (if any) is unknown.
- **Weak force mechanism:** are W/Z collective Ma excitations
  or something else? (Q96)


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

**Williamson and van der Mark (1997)** ([PDF][wvm]) proposed
the specific mechanism: an electron is a single photon
confined to a (1,2) torus knot.  The model reproduces spin ½
(exact, topological) and charge ≈ 0.91e (approximate,
geometric).  This project extends WvM into the MaSt
framework: the photon lives on a flat material sheet
(a periodic 2-dimensional surface), and the electron's
properties emerge from the geometry of that surface.  The
neutrino crisis — uncharged spin-½ particles are impossible
on a single sheet (R25) — forced the architecture from one
sheet to three (3Ma = Ma_e × Ma_ν × Ma_p), yielding Ma (R26).

[wvm]: https://fondationlouisdebroglie.org/AFLB-222/MARK.TEX2.pdf


## Structure

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
| [`STATUS.md`](STATUS.md) | Where we are: objectives, results, active front, open problems |
| [`studies/Taxonomy.md`](studies/Taxonomy.md) | **MaSt framework reference:** dimensions, geometry, particle catalog, mechanisms, open problems |
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
