# Theory of the Universe

## About this project

The author is an electrical engineer, not a trained physicist.  This started
as a hobby — a "what if" exploration of a 1997 paper that
proposed the electron is a confined photon.  It has since
produced results I did not expect: parameter-free
predictions of particle masses at percent-level accuracy,
an emergent neutron from pure geometry, nuclei that
appear as standing-wave modes rather than bound collections
of particles, and a neutrino mass-squared ratio that
matches experiment from integer mode numbers alone.

Because I am not expert in theoretical physics, I have
worked more as an architect and project manager than as a
traditional researcher.  The computational modeling,
mathematical derivations, and literature comparisons have
been performed collaboratively with AI (Claude).  Every
numerical result is produced by scripts in this repository
that can be inspected and re-run.

I do not claim that this model is correct.  It may turn out
to be a mathematical coincidence, an elaborate numerology,
or a useful approximation to something deeper.  What I do
claim is that it is *interesting*: a model that starts from
three axioms and derives percent-level particle masses with
no free parameters is, at minimum, worth understanding why
it works as well as it does — and worth understanding
precisely where and why it fails.

The project is conducted in the open.  The studies, scripts,
findings, and failures are all here.  Readers with relevant
expertise are welcome to examine, challenge, or extend the
work.


## The MaSt framework

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
equations).  Everything else — the particle zoo, their
properties, their interactions — should follow.

See [`qa/Q27-foundational-axioms.md`](qa/Q27-foundational-axioms.md) and
[`qa/Q32-energy-geometry-fundamentals.md`](qa/Q32-energy-geometry-fundamentals.md)
for discussion.


## Key results

### Electron (R2, R19, R26)
The (1,2) mode on Ma_e reproduces spin ½ (exact, topological),
mass m_e (resonance condition), charge e (shear mechanism),
g-factor ≈ 2 (energy partition), and magnetic moment (axial B
projection) — with zero free continuous parameters once
topology + e + m_e are given.

### Particle spectrum (R27, R28)
With r_p = 8.906 and σ_ep = −0.091 pinned by the neutron and
muon, the model has **zero free parameters** at the MeV scale.
Parameter-free predictions:

| Particle | Ma mode | Error |
|----------|---------|-------|
| Kaon (K±) | (1,2,0,0,3,4) | 1.2% |
| Eta (η) | (0,0,0,0,3,4) | 0.6% |
| Eta prime (η') | (0,0,0,0,3,6) | 0.3% |
| Phi (φ) | (0,0,0,0,3,8) | 0.8% |
| Lambda (Λ) | (1,2,0,0,3,6) | 0.9% |
| Sigma+ (Σ⁺) | (1,2,0,0,5,8) | 0.3% |

Lifetime-gap correlation r = −0.84 (p = 0.009) for weak
decays supports the off-resonance hypothesis: unstable
particles sit between eigenmodes, and the gap to the nearest
mode predicts the lifetime.

### Neutrino masses (R26)
The neutrino mass-squared ratio Δm²₃₁/Δm²₂₁ = 33.6 is
reproduced **exactly** from integer mode numbers on Ma_ν with
a single shear parameter s_ν = 0.022.  The result is
independent of the aspect ratio r_ν.

### Emergent neutron (R26)
The neutron appears as a cross-plane mode spanning Ma_e × Ma_p
with mode numbers (1,2,0,0,1,2).  Charge = −1+1 = 0 (exact),
mass reproduced at |σ_ep| ≈ 0.091.  It was not put in — it
was found by the Ma solver as a mode nobody looked for.

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

### What remains open
- **The α problem:** what determines the shear s ≈ 0.01
  of the electron sheet?  Multiple studies (R15, R19, R31,
  R32, R34) have constrained but not solved this.
- **Ghost modes:** ~900 modes at physical charges below
  2 GeV vs ~40 known particles.  ~10⁵ coupling suppression
  needed.  Selection rules kill most (R33) but 4 per charged
  sheet survive.
- **The hierarchy:** why is gravity 10⁴⁰× weaker than
  electromagnetism?  The membrane mechanics study (R37)
  proposes both arise from the same elastic interface.
- **Deriving G and α from geometry** (R37).


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

- `reference/` — Source material by others and recorded conversations.
- `primers/` — Self-contained tutorials on topics needed to follow
  the studies.  See [`primers/README.md`](primers/README.md).
- `papers/` — Authored documents presenting theories, results, and
  proofs.  See [`papers/README.md`](papers/README.md).
- `qa/` — Physics questions answered by logic and existing theory
  (no computation).  See [`qa/README.md`](qa/README.md).
- `studies/` — Questions that require a computational model to answer.
  See [`studies/STATUS.md`](studies/STATUS.md) for the registry.
- `labs/` — Proposed physical experiments to test predictions of the
  model.  See [`labs/README.md`](labs/README.md).
- `viz/` — Interactive browser-based visualizations.
  See [`viz/index.html`](viz/index.html).
- `lib/` — Shared Python code (Ma solver, mode search, metrics).


## Navigation

| File | Purpose |
|------|---------|
| [`STATUS.md`](STATUS.md) | Where we are: objectives, results, active front, open problems |
| [`studies/Taxonomy.md`](studies/Taxonomy.md) | **MaSt framework reference:** dimensions, geometry, particle catalog, mechanisms, open problems |
| [`studies/STATUS.md`](studies/STATUS.md) | Study-by-study registry: active, backlog, done |
| [`qa/Q84-mast-terminology.md`](qa/Q84-mast-terminology.md) | MaSt naming conventions and migration guide |
| [`qa/README.md`](qa/README.md) | Index of answered and open physics questions |
| [`qa/INBOX.md`](qa/INBOX.md) | Capture queue for new questions |
| [`papers/README.md`](papers/README.md) | Papers: matter-from-light, sub-quantum memory, atoms-from-geometry, universe-as-mode |
| [`primers/README.md`](primers/README.md) | Tutorials: matrix notation, Maxwell, KK theory, charge-from-energy |
| [`labs/README.md`](labs/README.md) | Proposed physical experiments to test model predictions |
| [`reference/WvM-summary.md`](reference/WvM-summary.md) | Living summary of the foundational WvM paper |
| [`viz/index.html`](viz/index.html) | Browser launcher for all interactive visualizations |
