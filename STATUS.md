# Project Status

**Mission:** Build a geometric model of fundamental particles from pure EM
energy — no fundamental charges, no point particles. See [`README.md`](README.md).

**Studies roadmap:** [`studies/STATUS.md`](studies/STATUS.md)
**GRID (substrate layer):** [`grid/STATUS.md`](grid/STATUS.md) — derives Maxwell + G from a discrete lattice
**Open questions:** [`qa/INBOX.md`](qa/INBOX.md) — [`qa/README.md`](qa/README.md) for index

---

## What has been established

### The framework (R2, R14, R26)

- **Material Space (Ma)** is a 6D compact manifold composed of three
  flat periodic sheets: Ma_e (electron), Ma_ν (neutrino), Ma_p (proton).
  Full arena: Ma × S × t (6+3+1 = 10 dimensions).
- Particles are standing electromagnetic waves — photons confined to
  closed geodesics on Ma.  Mass = confined energy, spin = winding
  topology, charge = shear-induced symmetry breaking.
- Three sheets are required: a single sheet cannot support both
  uncharged fermions (neutrinos) and charged particles (R14, R25).
- The material space is intrinsically flat; particles see Cartesian
  geometry internally.  The 3D embedding adds curvature that matters
  for charge projection but not for mass or spin (R12).

### Electron properties (R2, R19)

| Property | Status |
|----------|--------|
| Spin ½ | Exact — topological, from (1,2) winding number |
| Mass m_e | Input — Compton path-length condition fixes scale |
| Charge e | Emergent — shear mechanism produces Coulomb field; α still requires one input |
| g-factor ≈ 2.0023 | Derived — WvM energy-partition argument |
| Magnetic moment | Derived — axial projection of B on Ma_e |
| Free parameters | Zero continuous — topology + e + m_e fully determines geometry |

### Particle spectrum (R27, R28)

A computational Ma solver searches for modes matching known particles.
The neutron and muon jointly pin the two geometry parameters r_p = 8.906
and σ_ep = −0.091 (R27 F18), after which the MeV-scale predictions
are insensitive to the remaining free parameters.

| Particle | Error | Source |
|----------|------:|--------|
| Kaon (K⁺) | 1.2% | R27 F31 |
| Eta (η) | 0.6% | R27 F31 |
| Eta prime (η′) | 0.3% | R27 F31 |
| Phi (φ) | 0.8% | R27 F31 |
| Lambda (Λ) | 0.9% | R28 F10 |
| Sigma⁺ (Σ⁺) | 0.3% | R28 F14 |

Lifetime-gap correlation r = −0.84 (p = 0.009) for weak decays:
unstable particles sit between eigenmodes, and the gap predicts
the lifetime.

### Neutrino masses (R24, R26)

Δm²₃₁/Δm²₂₁ = 33.6 reproduced from integer mode numbers on Ma_ν
with a single shear parameter s_ν = 0.022.  The ratio is exact
and independent of r_ν.

### Emergent neutron (R26, R27)

The neutron was not put in — it was found by the solver as a
three-sheet mode (0,−2,+1,0,0,+2) spanning Ma_e × Ma_ν × Ma_p.
Charge Q = 0 (exact, topological).  Spin ½ from neutrino winding.
Mass reproduced at σ_ep = −0.091.

### Nuclear scaling law (R29)

Nuclei are Ma_p modes, not multi-particle bound states.  The law
n_φp = A, n_θp = 2A (A = mass number) matches all nuclei from
deuteron to ⁵⁶Fe at < 1%.  Nuclear spins predicted correctly for
9/11 tested nuclei.  Free neutron ≠ nuclear neutron (explains
nuclear stability).

### Charge mechanism (R15, R19)

Shear of the material sheet lattice breaks azimuthal symmetry,
producing a net Coulomb monopole from a delocalized wave.  The
formula α(r, s) gives a one-parameter family of solutions — every
aspect ratio r > ~2 has a self-consistent shear s.  The electron
is the lightest charged particle (R19 F31).

### Dynamic torus model (R40, R41)

The α-impedance model: the torus wall is the (1−α) energy contour,
with 136/137 of the photon energy confined and 1/137 leaking as the
external field.  The 3D embedding produces a 0.067% elliptical
perturbation with an elastic 1/k² wall response that acts as a
low-pass filter in tube winding number (40× suppression per step).
Dynamic corrections are O(α²) ≈ 5×10⁻⁵ — the static flat-torus
model is the correct zeroth-order approximation.  All three lepton
generations (e, μ, τ) are confirmed as distinct geometric modes
with filter-factor ordering FF(e) > FF(τ) > FF(μ).

### Predictive horizon (R28)

Above ~2 GeV, the Ma mode spectrum becomes too dense (band spacing
< 5 MeV) for mass-matching to be discriminating.  Below ~2 GeV,
the model is predictive.  W/Z/Higgs match trivially — not a test.

### Parameter accounting (R26, R28)

| What | Count |
|------|------:|
| Ma metric components (total) | 21 |
| Set by experimental inputs | 6 |
| Pinned by particle fits (neutron + muon) | 2 |
| Cross-shears (all zero, shown irrelevant) | 11 |
| **Effective free** | **2** |

The two free parameters are r_e (unconstrained) and r_ν (≥ 3.2).
The MeV-scale hadron predictions are insensitive to both.

### Computational infrastructure

- `lib/ma_model.py` — 1,900-line Ma model engine with four-level
  dynamic hierarchy (flat, elliptical, shortcut, full iterative).
  125 unit tests.
- `lib/ma_solver.py` — mode discovery engine for particle search.
- 41 completed studies (S1–S3, R1–R41), ~500 findings recorded.
- White paper draft (`papers/white-paper.md`).

---

## What remains open

### The α problem (Q18, Q34)

What determines the shear s ≈ 0.01 of the electron sheet?
Equivalently, what fixes α?  The formula α(r, s) produces a
continuous family of solutions.  Multiple studies have
constrained but not solved this (R15, R19, R31, R32, R34, R36).
The shear is currently reverse-engineered from α, not
independently determined.  This is the single most important
open problem.

### Ghost modes → dark matter (R42, Q94)

The Ma spectrum below 2 GeV contains ~900 modes at physical
charges versus ~40 observed particles.  Selection rules
(|n₁| = 1, spin-statistics) kill most, but ~4 per charged sheet
survive — most critically the (1,1) boson at half the electron
mass.

R42 established that ghost modes are plausible dark matter
candidates: exact charge symmetry ensures bulk neutrality,
the Compton window hypothesis (Q94) explains why they don't
couple to light, and the mass ratio brackets the observed
5.4 (range 2.4–12.4, realistic filters give 4.4–4.8).

What remains: the Compton window quality factor Q has not been
computed from first principles.  Three candidate mechanisms
are identified (impedance mismatch, multipole suppression,
evanescent cutoff) but the projection integral is unevaluated.

### What selects r_e? (Q34)

The electron sheet aspect ratio r_e is unconstrained by any
observable.  Constrained energy minimisation along the α curve
gives r ≈ 0.5 (R37 F7) — far from the phenomenological range
(r ≈ 4–9).  Resolving this requires the moduli potential (the
vacuum energy of Ma as a function of shape), which is not yet
computable.

### Nuclear binding / strong force (R29, R39, Q95)

Q95 proposes a plausible mechanism: the strong force is the full
internal EM interaction between Ma tori when they overlap at
r ~ λ_C, unattenuated by the Compton window.  This gives
coupling ~ 1 (vs α ≈ 1/137 externally), short range (~fm),
attraction for aligned dipoles, spin dependence, and a hard
core — all qualitative features of the nuclear force.  The
mechanism is identified but the quantitative nuclear potential
has not been derived from first principles.

### Neutrino spin (R25)

Charge-spin linkage (charge requires n₁ = ±1; spin ½ requires
odd n₁) means "uncharged fermion" is impossible in WvM.  The
three-sheet architecture (R26) accommodates neutrino mass but
the spin mechanism for neutrino-sheet modes with n₁ = 0 is
unresolved.

### Deriving G from geometry (R37 → GRID)

Gravity should emerge from the same Ma × S framework.  R37
showed self-gravity is negligible at Compton scale and the
membrane-mechanics derivation was tautological (GR restated).
A genuine derivation of G from Ma geometry has not been achieved.

**New approach:** the [GRID sub-project](grid/README.md) attacks this
from below — deriving G from the information resolution ζ = 1/4 of
a discrete lattice, via Jacobson's thermodynamic argument.  GRID also
derives Maxwell's equations from the same lattice, unifying the
electromagnetic and gravitational foundations.

---

## Possible future investigations

| Area | Key question | Status | Reference |
|------|-------------|--------|-----------|
| Geometric phase / holonomy | Does parallel transport on the embedded torus forbid ghost modes? | Open | Q93 Path 1 |
| Dark matter from ghost modes | Charge cancellation + Compton window → mass ratio 5.4? | **Plausible** — ratio brackets 5.4, mechanism identified | R42, Q94 |
| Compton window Q factor | Compute the projection integral for the first ~20 modes | Open — needed to close R42 | Q94 |
| Strong force from internal EM | Is α_s ≈ 1 the full internal field, with α the Compton-window projection? | **Plausible** — qualitative features match | Q95 |
| Matter–antimatter asymmetry | Does shear chirality provide the CP violation for baryogenesis? | **Plausible** — all Sakharov conditions met geometrically | Q97, Q32 |
| Force carriers in MaSt | Are W/Z/gluon fundamental or collective Ma excitations? | Open — hypothesis framed | Q96 |
| Fusion as mode transition | Is fusion a geometry change on Ma rather than a particle collision? | **Plausible** — interactive model built; re-derives solar T | Q89, Q95, viz/fusion |
| Coupling to S | Do ghost modes project weakly into 3D space? (quantifies Q94) | Open | Q93 Path 2 |
| One-loop self-energy | Do KK mass corrections improve the 1–6% structural errors? | Open | Q93 Path 3 |
| 10D polarization | Does the 8→2+6 polarization split provide new selection rules? | Open | Q93 Path 5 |
| Moduli potential | What vacuum energy functional selects the Ma shape (r_e, r_ν)? | Open | Q34, R37 |
| Biological coupling | Can the neutrino sheet serve as an information substrate? | Open | Q78–Q83 |
| α from first principles | Can dispersive or geometric arguments derive s ≈ 0.01? | Open | Q18, R34 |
