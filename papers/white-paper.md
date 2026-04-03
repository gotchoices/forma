# Particle Spectrum from Flat Extra Dimensions

**Status:** draft

---

## Abstract

The masses of elementary particles are among the least understood
constants in physics.  The Standard Model accommodates them as
inputs but offers no mechanism that determines their values.  This
paper presents a model in which particles are standing
electromagnetic waves on a compact six-dimensional manifold — three
flat tori, one each for the electron, neutrino, and proton families.
The Lagrangian is free electromagnetism in ten dimensions; no
additional fields, sources, or gravity coupling are introduced.

A particle's mass is the eigenfrequency of its mode on the compact
space.  Its electric charge and spin are determined by the winding
topology.  Four measured quantities fix the geometry (the electron
mass, the proton mass, the solar neutrino mass splitting, and the
fine-structure constant).  Two further calibration points (the
neutron and muon masses) pin the remaining shape parameters.  After
this, seven hadron masses — from the kaon to the sigma baryon —
emerge within 1.2% of their observed values with no further
adjustment.  The model also reproduces nuclear masses to < 1% via a
simple scaling law, predicts the neutrino mass hierarchy (normal
ordering, Σm_ν ≈ 118 meV), and recovers the electron's anomalous
magnetic moment g = 2(1 + α/2π) from geometry.

The model has significant open problems: roughly 900 predicted
modes below 2 GeV versus ~40 observed particles (the ghost mode
problem), a 5.6% structural error on the tau mass, and two free
parameters (the electron and neutrino aspect ratios) that remain
undetermined.  These are discussed alongside the results.

---

### Model card

| | |
|---|---|
| **Framework** | Maxwell's equations on a flat 10D manifold Ma × S × t |
| **Topology** | Ma = three flat tori (Ma_e × Ma_ν × Ma_p), S = ℝ³, t = ℝ |
| **Inputs** | m_e, m_p, Δm²₂₁, α (three masses fix torus scales; α fixes within-plane shears given aspect ratios) |
| **Pinned by observation** | r_p = 8.906 and σ_ep = −0.091 (neutron + muon, R27 F18; muon fit approximate — see §6), s₃₄ = 0.022 (ν oscillations) |
| **Effective free parameters** | 2 (r_e, r_ν); MeV predictions insensitive to both |
| **Outputs** | 6 particle masses to < 1.2% with no adjustment (7 within ~1.2%); three lepton masses accommodated; nuclear masses to < 1% (R29) |
| **Failures** | π⁺ (14%), Ω⁻ (structurally forbidden), ghost modes (~14k charge −1 spin ½ levels vs 3 observed leptons); τ gap (5.6%) is consistent with its short lifetime under the off-resonance hypothesis |
| **Testable** | Σm_ν = 116–120 meV (depends on r_ν), normal ordering, Ma_ν ring L₄ ≈ 42 μm (within reach of short-range gravity experiments if gravity propagates in Ma_ν) |

---

## Notation

| Symbol | Meaning |
|--------|---------|
| Ma | Material space — the compact 6D manifold (three 2-tori) |
| Ma_e, Ma_ν, Ma_p | Electron, neutrino, and proton sheets (each a flat 2-torus) |
| S | Ordinary 3D space (ℝ³) |
| n = (n₁,…,n₆) | Mode quantum numbers (integer winding numbers on Ma) |
| n₁, n₃, n₅ | Tube windings on Ma_e, Ma_ν, Ma_p |
| n₂, n₄, n₆ | Ring windings on Ma_e, Ma_ν, Ma_p |
| L₁,…,L₆ | Circumferences of the six compact dimensions (fm) |
| r_e, r_ν, r_p | Aspect ratios: r = L_tube / L_ring for each sheet |
| s₁₂, s₃₄, s₅₆ | Within-plane shear: skew angle of each torus lattice |
| σ_ep | Cross-plane shear: off-diagonal metric coupling between Ma_e and Ma_p |
| G̃ | Dimensionless 6×6 metric on Ma (G̃_ij = G^phys_ij / (L_i L_j)) |
| ñ | Scaled winding vector: ñ_i = n_i / L_i |
| μ₁₂(r,s) | Dimensionless energy of the (1,2) mode: √(1/r² + (2−s)²) |
| Q | Electric charge in units of e |
| α | Fine-structure constant (≈ 1/137) |


## 1. Model and results

The model is free electromagnetism on a ten-dimensional manifold.
Six dimensions form a compact flat space Ma (material space);
three are ordinary space S = ℝ³; one is time.  The Lagrangian is

    L = −¼ F_MN F^MN,   M,N = 0,…,9

with no sources, no gravity coupling, and no additional fields.
Particles are standing electromagnetic waves on Ma.  Each mode is
labeled by six integers (n₁,…,n₆) — the winding numbers around
the compact directions.  The mode's rest energy is its mass; its
quantum numbers determine charge and spin.

The spectrum table, with no parameters adjusted beyond those
pinned by the four inputs (m_e, m_p, Δm²₂₁, α) and two
calibration points (neutron mass, muon mass):

| Particle | Obs (MeV) | Mode | Pred (MeV) | Error |
|----------|----------:|------|----------:|------:|
| e⁻ | 0.511 | (+1,+2, 0, 0, 0, 0) | 0.511 | input |
| p | 938.3 | ( 0, 0, 0, 0,+1,+2) | 938.3 | input |
| n | 939.6 | ( 0,−2,+1, 0, 0,+2) | 939.6 | pins σ_ep |
| μ⁻ | 105.7 | (−1,+5, 0, 0,−2, 0) | 105.7 | pins r_p |
| K⁺ | 493.7 | (−4,−8,+1, 0,−3,−1) | 488.0 | 1.2% |
| K⁰ | 497.6 | (−3,−8, 0, 0,−3,+1) | 503.7 | 1.2% |
| η | 547.9 | (−5,−8, 0, 0,−5,+1) | 551.2 | 0.6% |
| η′ | 957.8 | (−3,−8, 0, 0,−3,+2) | 961.1 | 0.3% |
| φ | 1019.5 | (−7,−8, 0, 0,−7,+2) | 1028.0 | 0.8% |
| Λ | 1115.7 | (−12,−15,+1, 0,−12,−2) | 1105.9 | 0.9% |
| Σ⁺ | 1189.4 | (−14,−15, 0, 0,−13,+2) | 1193.4 | 0.3% |
| τ⁻ | 1776.9 | (−1,+8, 0, 0,−2,−4) | 1876.4 | 5.6% |
| π⁺ | 139.6 | (+2,−8,+1, 0,+3, 0) | 158.5 | 14% |
| Ω⁻ | 1672.5 | — | — | forbidden |

Seven masses (K⁺ through Σ⁺) land within ~1.2% of observation
with zero free parameters adjusted.  Failures are discussed in §7.
Source: R27 F31, R28 F10/F14.


## 2. Geometry and mode spectrum

Ma is the product of three flat 2-tori:

    Ma = Ma_e × Ma_ν × Ma_p

Each torus has two circumferences — a tube and a ring — giving
six compact dimensions total with circumferences L₁,…,L₆:

| Sheet | Tube (φ) | Ring (θ) | Scale |
|-------|----------|----------|-------|
| Ma_e (electron) | L₁ = r_e L₂ | L₂ | ~5,000 fm |
| Ma_ν (neutrino) | L₃ = r_ν L₄ | L₄ | ~42 μm |
| Ma_p (proton) | L₅ = r_p L₆ | L₆ | ~2.6 fm |

The ring circumferences are set by the input masses:

    L₂ = 2πℏc / (m_e c² × μ₁₂),   L₆ = 2πℏc / (m_p c² × μ₅₆)

where μ₁₂ and μ₅₆ are dimensionless mode energies of the (1,2)
winding pattern at the given aspect ratio and shear.  L₄ is set
by Δm²₂₁ analogously.  The tube circumferences follow from the
aspect ratios: L₁ = r_e L₂, etc.

The metric on Ma is a flat 6×6 symmetric matrix G̃ with three
types of off-diagonal structure:

- **Within-plane shears** s₁₂, s₃₄, s₅₆: each skews a rectangle
  into a parallelogram.  The fine-structure constant α determines
  sₑ and s_p given the aspect ratios (§3).  The neutrino shear
  s₃₄ is fixed by the mass-squared ratio (§5).
- **Cross-plane shears** σ_ep, σ_eν, σ_νp: couple different
  sheets.  Only σ_ep matters; the others are zero and irrelevant
  (R28 F1/F4).

Mode energies follow from the inverse metric:

    E(n) = 2πℏc √( ñᵀ G̃⁻¹ ñ ),   ñᵢ = nᵢ / Lᵢ

**Parameter accounting.** The metric has 21 independent components.
Eight are constrained: three ring scales (m_e, m_p, Δm²₂₁), three
within-plane shears (α, Δm² ratio), and two from the neutron +
muon fit (r_p, σ_ep).  Of the 13 formally free, 11 are cross-shear
components that are all zero and shown irrelevant.  The effective
free parameters are **2: r_e and r_ν**.


## 3. Spin, charge, and mass

**Spin** is topological.  A photon circulating on a torus carries
angular momentum set by its winding numbers.  The tube dimensions
(n₁, n₃, n₅) determine spin: each odd tube winding contributes
spin ½.  The electron mode (1, 2) has one odd tube winding
(n₁ = 1), giving spin ½.  The proton mode (0, 0, 0, 0, 1, 2)
likewise has n₅ = 1 (odd), giving spin ½.  Modes with zero or
two odd tube windings are bosons.

**Charge** arises from compact momentum in the Kaluza–Klein sense.
The electromagnetic U(1) is identified with the difference of
tube momenta between the electron and proton sheets:

    Q / e = −n₁ + n₅

This gives Q = −1 for the electron (n₁ = 1, n₅ = 0), Q = +1 for
the proton (n₁ = 0, n₅ = 1), and Q = 0 for the neutron
(n₁ = 0, n₅ = 0).  The formula produces correct integer charges
for all matched particles (R27 F31).

**The fine-structure constant** connects charge strength to
geometry.  The shear-induced charge integral on an embedded
torus gives (R19 F35):

    α(r, s) = r² μ₁₂(r,s) sin²(2πs) / [4π (2−s)²]

where μ₁₂ = √(1/r² + (2−s)²).  At a given aspect ratio r,
there is a unique shear s that reproduces α = 1/137.  This
determines s_e(r_e) and s_p(r_p).  Since r_p = 8.906 is known,
s_p is fully determined.  Since r_e is free, s_e varies with it —
but the product s_e(r_e) always gives α = 1/137.

**Mass** is the mode eigenfrequency.  No additional mechanism is
needed: the photon's rest energy on Ma is the particle's mass.

**g-factor.**  The electron's magnetic moment arises from the
circulating photon's angular momentum projected along its spin
axis.  A fraction α/(2π) of the photon's energy resides in
the external Coulomb field (non-rotating), shifting the ratio
of magnetic moment to angular momentum:

    g = 2(1 + α/(2π)) ≈ 2.00232

This reproduces the leading QED correction from geometry alone
(R2 Property 4).


## 4. The neutron

The neutron is a three-sheet mode spanning Ma_e × Ma_ν × Ma_p
with quantum numbers (0, −2, +1, 0, 0, +2).

- **Charge:** Q = −n₁ + n₅ = −0 + 0 = 0 (exact).
- **Spin:** n₁ = 0 (even), n₃ = 1 (odd) → spin ½ from the
  neutrino tube winding.
- **Mass:** determined by the cross-sheet coupling σ_ep.
  The mode spans all three sheets; its energy exceeds the proton's
  because cross-sheet modes always cost more than single-sheet
  modes.  m_n − m_p = 1.293 MeV is reproduced self-consistently
  at σ_ep = −0.091 (R27 F11–F16).

The neutron mode "lives" on the tube dimensions of the electron
and proton sheets (n₂ = −2, n₆ = +2) and the tube of the
neutrino sheet (n₃ = +1).  Its spin comes entirely from the
neutrino sector — suggestive, given that beta decay is a weak
(neutrino-mediated) process.

When the cross-sheet coupling weakens, the mode decomposes into
its three resident single-sheet modes: proton, electron, and
neutrino — exactly the products of beta decay.  The decay
energetics are self-consistent: ΔE = +0.78 MeV at the mode
level, matching observation (R27 F34).

The neutron and muon masses jointly pin the two parameters r_p
and σ_ep (R27 F18).  After this, all remaining MeV-scale
predictions require no further adjustment.

**Note:** The muon is unstable (τ = 2.2 μs).  The off-resonance
hypothesis (§6) predicts it should have a small gap (~0.3%), not
an exact eigenmode match.  Using it as an exact fit target
introduces a small systematic; r_p and σ_ep should eventually
be re-derived from stable anchors only.


## 5. Neutrino mass splittings

Neutrino mass eigenstates are modes on Ma_ν.  The three lightest
modes with odd tube winding (|n₃| = 1, giving spin ½) are
(1,1), (−1,1), and (1,2) at the Assignment A shear s₃₄ = 0.02199
(R26 F33).

The mass-squared ratio depends on a single parameter:

    Δm²₃₁ / Δm²₂₁ = (3 − 2s₃₄) / (4 s₃₄)

At s₃₄ = 0.02199 this gives 33.6, matching the experimental
value 33.6 ± 0.9 (R26 F1).  The ratio is independent of r_ν —
a notable feature, since it means the neutrino mass hierarchy
is determined by a single geometric parameter with no dependence
on the unknown aspect ratio.

The total neutrino mass Σm_ν depends weakly on r_ν:

| r_ν | Σm_ν (meV) |
|-----|-----------|
| 3.2 (lower bound) | 120 |
| 5.0 (reference) | 118 |
| ∞ (asymptote) | 116 |

All values are below the cosmological bound (~120 meV).  The
model predicts **normal mass ordering** (m₁ < m₂ < m₃) for all
allowed r_ν (R26 F33).  Inverted ordering is geometrically
excluded.


## 6. Three generations

Three charge −1, spin ½ modes match the observed charged leptons:

| Gen | Particle | Mode | Mass (MeV) | Mechanism |
|-----|----------|------|--------:|-----------|
| 1st | e⁻ | (+1,+2, 0, 0, 0, 0) | 0.511 | Single-sheet (Ma_e) |
| 2nd | μ⁻ | (−1,+5, 0, 0,−2, 0) | 105.7 | Cross-sheet (Ma_e × Ma_p) |
| 3rd | τ⁻ | (−1,+8, 0, 0,−2,−4) | 1876.4 | Cross-sheet (Ma_e × Ma_p) |

The electron lives on Ma_e alone.  The muon adds proton-ring
windings; the tau adds proton-tube windings on top of that.  Each
generation accesses shorter length scales and higher energies.
All three share the same charge (Q = −n₁ + n₅ = −1) and spin
(one odd tube winding), so they are electromagnetically identical
except for mass — as observed.

Three neutrino modes on Ma_ν match the Δm² splittings (§5).

**Why three and not more?**  The model does not predict exactly
three.  The charge −1, spin ½ spectrum contains ~14,000 distinct
energy levels below 10 GeV (R38 F1).  Ma_ν has ~1,000 weakly-
charged neutrino species (R38 F3), creating a 140σ tension with
the Z-width measurement N_ν = 2.996 ± 0.007.

The generation count reduces to the ghost mode problem (§8).  One
partial resolution: the resonance capture hypothesis (R38 Track 5).
If Ma acts as a resonant cavity with quality factor Q ≈ 30, the
tau sits at the edge of capture (5.6% off-resonance) and the 4th
generation mode at ~2346 MeV is excluded.  This gates charged
leptons at three but does not address the neutrino overcounting.


## 7. Predictions and failures

### Untuned predictions

Seven particle masses land within ~1.2% of observation with no
parameters adjusted beyond those pinned by the neutron and muon.
The full spectrum table appears in §1.

Five of these (K⁺, η, η′, φ, and K⁰) were found in R27's
systematic catalog at n_max = 8.  The Λ and Σ⁺ matches improved
from 5.8% and 11.6% to 0.9% and 0.3% when the search was
extended to n_max = 15 (R28 F10–F14).

The lifetime-gap correlation provides an independent test.  Among
15 unstable particles, the Pearson correlation between log|gap|
and log(lifetime) is r = −0.61; for weak charged-current decays
alone (8 particles), r = −0.84 (p = 0.009) with a power law
τ ∝ |gap|^(−2.7) (R27 F33/F39).  Particles farther from a Ma
eigenmode decay faster — exactly as the off-resonance hypothesis
predicts.

### Failures

- **Tau (5.6%):** The nearest mode is locked at ~2m_p ≈ 1876 MeV
  by the self-consistency constraint.  No mode exists within
  100 MeV of the observed 1776.9 MeV (R27 F20–F22).

- **Pion (14%):** The lightest meson; its mass may be sensitive to
  nonlinear corrections or within-plane shear details not yet
  modeled.

- **Omega baryon (Ω⁻):** Structurally forbidden.  Spin 3/2
  requires three odd tube windings, forcing charge Q = −n₁ + n₅
  to be even.  Charge −1, spin 3/2 cannot exist as a single Ma
  mode (R27 F35).

- **Vector mesons (ρ⁰, ω):** 20% off; short-lived (10⁻²³ s).
  These sit far from any eigenmode and are consistent with the
  off-resonance interpretation.

### Nuclear scaling law

Nuclei appear as proton-sheet modes, not multi-particle bound
states.  The scaling law n_φp = A, n_θp = 2A (A = mass number)
matches all nuclei from deuteron to ⁵⁶Fe at < 1% (R29).  Nuclear
spins are predicted correctly for 9 of 11 tested nuclei.

### Predictive horizon

Above ~2 GeV, the proton-sheet energy bands are spaced by
< 5 MeV (R28 F5).  Any particle mass can be matched to within
a few MeV, so predictions above this scale are not discriminating.
W, Z, and Higgs all have nearby modes, but trivially so — this
is not a test of the model.


## 8. Open problems

**The α problem.**  The fine-structure constant enters as an input
that fixes the within-plane shears.  A self-selecting mechanism
would eliminate one free parameter (r_e) by determining it from
α alone.  Membrane energy minimisation prefers r_e ≈ 0.50 (R37 F7)
but the minimum is broad.  No moduli potential has been derived.

**Ghost modes.**  The model predicts ~900 modes with physical
charges below 2 GeV; nature has ~40 particles in this range
(R28 F5–F6).  Selection rules from the R19 charge integral reduce
ghosts to ~4 per charged sheet (R33 F1), but this integral (WvM)
applies to embedded tori, while the current metric is a flat
quotient space where charge arises from KK momentum.  Reconciling
the two — or finding an alternative suppression mechanism — is the
central open problem.

**Three generations.**  The charged lepton count could be gated by
resonance capture (R38 Track 5): at cavity Q ≈ 30 the tau is
barely captured and the 4th generation is excluded.  But the
neutrino overcounting (~1,000 species vs 3 observed) and the
broader ghost problem (14,000 charged lepton modes vs 3) require
a different or more general mechanism.

**No QFT formulation.**  Decay rates, running couplings, and
scattering amplitudes require a quantized field theory on
Ma × S × t.  The classical wave equation gives the mass spectrum;
the quantum theory is needed for everything else.

**Gravity.**  Ma_ν has circumference L₄ ≈ 42 μm.  If gravity
propagates in this dimension, short-range gravity experiments
would detect deviations from 1/r² at this scale.  Current bounds
reach ~50 μm with no deviation seen — barely compatible.  If
gravity does not propagate in Ma_ν (e.g., only Ma_p at fm scale
is gravitationally active), the constraint is satisfied but the
mechanism must be explained.
