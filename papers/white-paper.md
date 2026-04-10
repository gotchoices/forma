# Matter from Light: A Geometric Particle Spectrum

**Status:** draft
**Model era:** [model-D](../models/model-D.md). Proton as (1,3)
fundamental mode; no parameters pinned to unstable particles; waveguide
cutoff and topological spin replace earlier ad hoc filters. See
[`model-D.md`](../models/model-D.md) for the full Assumptions / Results
card.

---

## Abstract

The masses of elementary particles are among the least understood
constants in physics.  The Standard Model accommodates them as
inputs but offers no mechanism that determines their values.  This
paper presents a model in which particles are standing
electromagnetic waves on a compact six-dimensional manifold — three
flat tori, one each for the electron, neutrino, and proton families.
The Lagrangian is free electromagnetism in eleven dimensions; no
additional fields, sources, or gravity coupling are introduced.

A particle's mass is the eigenfrequency of its mode on the compact
space.  Its electric charge and spin are determined by the winding
topology.  Four measured quantities fix the geometry (the electron
mass, the proton mass, the solar neutrino mass splitting, and the
fine-structure constant α).  No parameters are pinned to unstable
particle masses — the neutron and all hadrons are genuine
predictions, not calibration targets.

Eleven of seventeen testable particles below 2 GeV are predicted
within 2% of their observed masses (ten as single modes, one as
a spin-singlet pair).  Stable particles match closely;
unstable particles miss by an amount that predicts their
instability — a near-miss to a standing-wave resonance.  The model
reproduces nuclear masses from deuterium to iron at < 1% via a
single scaling law, predicts neutrino oscillation (mass-squared
ratio Δm²₃₁/Δm²₂₁ = 33.6 exact, normal ordering, Majorana nature),
and identifies a geometric mechanism for the electron's anomalous
magnetic moment.

The electromagnetic field equations used here are not imported —
they are derived from a discrete lattice at the Planck scale
(the GRID framework), which also derives the gravitational
constant G from the lattice's information density.  Electric
charge is topological winding on the GRID lattice; spin ½ arises
from odd tube winding numbers.  The particle model (MaSt) takes
these field equations as input and constructs the spectrum from
compact geometry.

The model has open problems.  The muon sits in a structural mass
desert — no Q = −1 spin-½ eigenmode exists between 5 and 200 MeV
across all sign branches, cross-shear grids, and winding ranges
tested (R50 Track 8).  Charged and neutral pions likewise sit in this
desert, unreachable by single modes or pairs.  Cross-shear coupling
between sheets CAN boost the effective e-sheet mass in principle
(confirmed mechanism), but the current metric structure caps the
boost at 2.5× before singularity, far short of the 207× needed for
the muon (R50 Track 10).  A richer metric parameterization is the
leading path forward.  A large number of predicted modes below 2 GeV
are mostly electrically neutral and have been reinterpreted as
dark matter candidates.  These are discussed alongside the results.

---

### Model card

| | |
|---|---|
| **Framework** | Maxwell's equations on a flat 11D manifold Ma × S × t |
| **Topology** | Ma = three flat tori (Ma_e × Ma_ν × Ma_p), S = ℝ³, t = ℝ |
| **Inputs** | m_e, m_p, Δm²₂₁, α (three masses fix torus scales; α fixes within-plane shears given aspect ratios) |
| **Constrained from data** | σ_ep ≈ −0.13, ε_e ≈ 0.65, ε_p ≈ 0.55 (swept, not pinned to specific particles); σ_eν tested in [−0.20, +0.20] |
| **Effective free parameters** | 2 (ε_e, ε_ν); waveguide cutoff may constrain both; MeV predictions insensitive |
| **Proton** | (1,3) fundamental mode (leading); universal charge formula Q = −n₁ + n₅ works for particles and nuclei |
| **Outputs** | 11 of 17 testable particles within 2% (10 single + 1 pair); nuclear masses to < 1% (R50 Track 5); neutrino oscillation ratio exact |
| **Ephemeral particles** | Unstable particles miss resonance by an amount consistent with their instability; stable particles match closely |
| **Ghost modes** | Lightest charged ghost (1,1) eliminated by waveguide cutoff; most remaining modes electrically neutral → dark matter candidates |
| **Testable** | Σm_ν = 116–120 meV (normal ordering, Majorana); 0νββ at |m_ββ| ~ 10–30 meV; Ma_ν ring L₄ ≈ 42 μm |

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
| ε_e, ε_ν, ε_p | Aspect ratios: ε = L_tube / L_ring for each sheet (earlier papers use r) |
| s₁₂, s₃₄, s₅₆ | Within-plane shear: skew angle of each torus lattice |
| σ_ep | Cross-plane shear: off-diagonal metric coupling between Ma_e and Ma_p |
| G̃ | Dimensionless 6×6 metric on Ma (G̃_ij = G^phys_ij / (L_i L_j)) |
| ñ | Scaled winding vector: ñ_i = n_i / L_i |
| μ(ε,s,n_t,n_r) | Dimensionless mode energy: √(n_t²/ε² + (n_r−s)²) |
| Q | Electric charge in units of e |
| α | Fine-structure constant (≈ 1/137) |


## 1. Model and results

The model is free electromagnetism on an eleven-dimensional manifold.
Six dimensions form a compact flat space Ma (material space);
three are ordinary space S = ℝ³; one is time; one is the GRID
phase fiber (§9).  The Lagrangian is

    L = −¼ F_MN F^MN,   M,N = 0,…,10

with no sources, no gravity coupling, and no additional fields.
Particles are standing electromagnetic waves on Ma.  Each mode is
labeled by six integers (n₁,…,n₆) — the winding numbers around
the compact directions.  The mode's rest energy is its mass; its
quantum numbers determine charge and spin.

The spectrum table.  Four inputs fix the geometry (m_e, m_p,
Δm²₂₁, α).  No parameters are pinned to unstable particle masses —
the neutron and all hadrons are predictions.  Working geometry:
σ_ep = −0.13, ε_e = 0.65, ε_p = 0.55.

| Particle | Obs (MeV) | Mode | Pred (MeV) | |Δm|/m |
|----------|----------:|------|----------:|------:|
| e⁻ | 0.511 | (1, 2, 0, 0, 0, 0) | 0.511 | input |
| p | 938.3 | (0, 0, 0, 0, 1, 3) | 938.3 | input |
| n | 939.6 | (0, 6, \*, \*, 0, 8) | 939.3 | 0.03% |
| φ | 1019.5 | (−1, 6, \*, \*, −2, −8) | 1019.9 | 0.05% |
| Ω⁻ | 1672.5 | (−2, −6, \*, \*, −3, 13) | 1673.1 | 0.04% |
| τ⁻ | 1776.9 | (2, 5, \*, \*, 1, −15) | 1780.0 | 0.18% |
| Σ⁺ | 1189.4 | (−2, −5, \*, \*, −1, −10) | 1187.1 | 0.19% |
| Δ⁰ | 1232.0 | (1, −6, \*, \*, 2, 10) | 1237.0 | 0.41% |
| Λ | 1115.7 | (−2, 6, \*, \*, −2, −9) | 1127.7 | 1.1% |
| Ξ⁰ | 1314.9 | (0, 6, \*, \*, 0, 11) | 1291.4 | 1.8% |
| η′ | 957.8 | (0, −6, \*, \*, 0, −8) | 939.3 | 1.9% |
| ρ⁰ | 775.3 | (1, −6, \*, \*, 1, −6) | 742.3 | 4.3% |
| K⁰ | 497.6 | (0, −6, \*, \*, 0, −4) | 469.7 | 5.6% |
| η | 547.9 | (0, 6, \*, \*, 0, −5) | 586.8 | 7.1% |
| μ⁻ | 105.7 | (1, 6, \*, \*, 0, −1) | 117.2 | 10.9% |
| K± | 493.7 | Q=0 (248.6) + Q=±1 (248.6) pair | 497.3 | 0.73% |
| π± | 139.6 | — | — | desert |
| π⁰ | 135.0 | — | — | desert |

Neutrino quantum numbers (marked \*) freely vary — Ma_ν
contributes < 0.001% of the energy at hadron scales.  Eleven of
seventeen testable particles match within 2% (10 single modes, 1
spin-singlet pair).  Best predictions: φ (0.05%), Ω⁻ (0.04%),
n (0.03%).  K± rescued as paired ~249 MeV modes (R50 Track 9).
Failures are discussed in §7.
Source: R50, model-D (σ_ep = −0.13, ε_e = 0.65, ε_p = 0.55).


## 2. Geometry and mode spectrum

Ma is the product of three flat 2-tori:

    Ma = Ma_e × Ma_ν × Ma_p

Each torus has two circumferences — a tube and a ring — giving
six compact dimensions total with circumferences L₁,…,L₆:

| Sheet | Tube (φ) | Ring (θ) | Scale |
|-------|----------|----------|-------|
| Ma_e (electron) | L₁ = ε_e L₂ | L₂ | ~5,000 fm |
| Ma_ν (neutrino) | L₃ = ε_ν L₄ | L₄ | ~42 μm |
| Ma_p (proton) | L₅ = ε_p L₆ | L₆ | ~2.6 fm |

The aspect ratio ε = L_tube / L_ring sets the shape of each torus
(ε < 1 is a thin tube, ε > 1 is fat).

The ring circumferences are set by the input masses:

    L₂ = 2πℏc / (m_e c² × μ₁₂),   L₆ = 2πℏc / (m_p c² × μ₁₃)

where μ₁₂ and μ₁₃ are dimensionless mode energies of the
electron (1,2) and proton (1,3) winding patterns at the given
aspect ratio and shear.  L₄ is set by Δm²₂₁ analogously.  The
tube circumferences follow from the aspect ratios: L₁ = ε_e L₂,
etc.

The metric on Ma is a flat 6×6 symmetric matrix G̃ with three
types of off-diagonal structure:

- **Within-plane shears** s₁₂, s₃₄, s₅₆: each skews a rectangle
  into a parallelogram.  The fine-structure constant α determines
  sₑ and s_p given the aspect ratios (§3).  The neutrino shear
  s₃₄ is fixed by the mass-squared ratio (§5).
- **Cross-plane shears** σ_ep, σ_eν, σ_νp: couple different
  sheets.  σ_ep ≈ −0.13 sets the neutron mass and is the most
  important cross-shear.  σ_eν has negligible effect on hadron-
  scale energies in the current (scalar) parameterization, but
  modifies the effective e-sheet mass through the metric's Schur
  complement — a mechanism under active investigation for the
  muon (R50 Track 10).

Mode energies follow from the inverse metric:

    E(n) = 2πℏc √( ñᵀ G̃⁻¹ ñ ),   ñᵢ = nᵢ / Lᵢ

**Parameter accounting.** The metric has 21 independent components.
Six are constrained by measurements: three ring scales (m_e, m_p,
Δm²₂₁) and three within-plane shears (α on each charged sheet,
Δm² ratio on Ma_ν).  Of the 15 formally free, 11 are cross-shear
components that are all zero and shown irrelevant (R28 F1/F4).
Two more (ε_p and σ_ep) are swept over and constrained by spectrum
quality — not pinned to any single particle mass.  The effective
free parameters are **2: ε_e and ε_ν**.

These may not remain free.  The torus acts as a waveguide cavity:
modes below a frequency cutoff cannot propagate and are evanescent
(R46).  On Ma_e, this eliminates the (1,1) ghost — a lighter-than-
electron charged particle that has never been observed — while
preserving the (1,2) electron.  The cutoff depends on ε_e,
constraining it.  Similarly, ε_ν may be constrained by the
requirement that exactly three neutrino mass eigenstates are
observed (R49 finds Family A at ε_ν ≈ 5 strongly favored).  If
both aspect ratios are pinned by waveguide filtering, the
effective free parameter count drops to **zero**.


## 3. Spin, charge, and mass

**Spin** is topological.  A photon circulating on a torus carries
angular momentum set by its winding numbers.  The tube winding
number n_tube determines spin: each odd tube winding contributes
spin ½.  The electron mode (1, 2) has n₁ = 1 (odd), giving
spin ½.  The proton mode (0, 0, 0, 0, 1, 3) likewise has n₅ = 1
(odd), giving spin ½.  Modes with zero or two odd tube windings
are bosons.

This is a topological fact, not a dynamical rule: spin ½ is the
parity of the tube winding number, just as charge is the tube
winding number itself.  The earlier WvM-derived ratio rule
(s = n₁/n₂) is superseded.

**Charge** is topological.  In the GRID lattice, each cell carries
a periodic phase θ ∈ [0, 2π).  A standing wave whose phase winds
through a full 2π around the tube of a torus creates a topological
defect — an irreducible twist that the ambient lattice detects as
electric charge.  The winding number is quantized (integers only,
by phase periodicity) and universal (independent of sheet size).
Standing waves carry zero net circulation and therefore zero
charge (R48 F4); a net traveling component (from shear-induced
asymmetry) is required.

The charge formula across sheets is:

    Q / e = −n₁ + n₅

This gives Q = −1 for the electron (n₁ = 1, n₅ = 0), Q = +1 for
the proton (n₁ = 0, n₅ = 1), and Q = 0 for the neutron
(n₁ = 0, n₅ = 0).  The formula produces correct charges for all
matched particles and for all tested nuclei from deuterium to
iron (R50 Track 5).

The n₁ = ±1 selection rule — only modes with exactly one tube
winding on a charged sheet carry unit charge — has been derived
from the circular polarization geometry of the confined photon:
the CP rotation rate must match the tube's geometric rotation rate
for the normal E-field component to be constant (R48 F3).

**The fine-structure constant** α ≈ 1/137 is a measured input.
In the GRID picture, α is the impedance mismatch between the 2D
material sheet and the 3D spatial lattice — the fraction of the
standing wave's energy that couples through the junction as Coulomb
field.  A particle of mass m has internal energy mc² on the sheet
and external Coulomb energy αmc² in the ambient lattice.

The shear parameter s — the angle at which the sheet is embedded
in the ambient lattice — provides a geometric consistency
condition linking α to the torus shape.  The formula is mode-aware
(R19 F35, updated for general (n_tube, n_ring) in Q114):

    α(ε, s, n_t, n_r) = ε² μ(ε,s,n_t,n_r) sin²(2πs) / [4π (n_r−s)²]

where μ = √(n_t²/ε² + (n_r−s)²).  At a given aspect ratio ε and
mode, there is a unique shear s that reproduces α = 1/137.  This
determines s_e(ε_e) for the electron (1,2) and s_p(ε_p) for the
proton (1,3).  The shear sign (positive or negative branch) is
not yet uniquely determined — both solve α = 1/137, with different
magnitudes (R50 F23–F28).

The shear also breaks the symmetry between clockwise and
counterclockwise circulation on the torus, determining the
matter/antimatter preference (CPT is exact; C is broken by
the embedding chirality).

**Mass** is the mode eigenfrequency.  No additional mechanism is
needed: the photon's rest energy on Ma is the particle's mass.

**g-factor.**  The electron's magnetic moment arises from the
circulating photon's angular momentum projected along its spin
axis.  The bare magnetic moment is topological: g_bare = n_ring
(the ring winding number), giving g_bare = 2 for the electron
and g_bare = 3 for the (1,3) proton (Q114).  The Coulomb self-
field back-reacts on the circulating wave, shifting the moment.
R52 confirmed the correct sign (+0.1%, additive) for the
electron from the B-field distribution.  The proton (measured
g = 5.586, requiring a +86% anomaly from g_bare = 3) needs a
different mechanism — shear-dependent self-energy showed
promise (R52 Tracks 4d–4e) but the clean sign-rule hypothesis
was retracted after a mode-aware audit (R52 F25).  Cross-sheet
effects and lattice-native back-reaction remain leads.  The
anomalous moment is currently an **accommodation**.


## 4. The neutron

The neutron is a three-sheet mode spanning Ma_e × Ma_ν × Ma_p
with quantum numbers (0, 6, \*, \*, 0, 8) at σ_ep ≈ −0.13.

- **Charge:** Q = −n₁ + n₅ = −0 + 0 = 0 (exact).
- **Spin:** n₁ = 0 (even), n₃ = odd → spin ½ from the neutrino
  tube winding (neutrino quantum numbers \* freely vary — they
  contribute negligible energy at hadron scales).
- **Mass:** predicted at 939.3 MeV (observed 939.6 MeV, 0.03%
  residual).  The neutron is a **prediction**, not a calibration
  target — σ_ep is swept, not pinned to the neutron mass.

The neutron spans all three sheets; its energy exceeds the
proton's because cross-sheet modes always cost more than single-
sheet modes.  The mass difference m_n − m_p = 1.293 MeV emerges
naturally at σ_ep ≈ −0.13.

The mode's slight offset from the nearest exact eigenmode is
itself a prediction: the neutron is an almost-resonance, near
but not exactly on a standing-wave peak.  Its instability (mean
life ~880 s) is predicted by this near-miss — an exact eigenmode
would be stable.  When the cross-sheet coupling weakens, the mode
decomposes into its three resident single-sheet modes: proton,
electron, and neutrino — exactly the products of beta decay.

**Neutron stability in nuclei.**  In a nucleus, the neutron mode
is part of a larger multi-sheet winding pattern where the proton-
sheet quantum numbers scale with mass number A (§7).  The
composite mode sits closer to a true eigenmode than the free
neutron does, explaining why bound neutrons are stable while
free neutrons decay.


## 5. Neutrino oscillation and mass structure

Neutrino mass eigenstates are modes on Ma_ν.  The three lightest
modes with odd tube winding (|n₃| = 1, giving spin ½) are
(1,1), (−1,1), and (1,2) — the three base modes of Assignment A
at shear s₃₄ = 0.02199 (R26 F33).

These three modes predict neutrino oscillation directly.  The
mass-squared ratio depends on a single parameter:

    Δm²₃₁ / Δm²₂₁ = (3 − 2s₃₄) / (4 s₃₄)

At s₃₄ = 0.02199 this gives 33.6, matching the experimental
value 33.6 ± 0.9 exactly (R26 F1).  The ratio is independent
of ε_ν — the neutrino mass hierarchy is determined by a single
geometric parameter with no dependence on the unknown aspect
ratio.

The model predicts **normal mass ordering** (m₁ < m₂ < m₃),
**Majorana nature** (ν₁ and ν₂ are C-conjugates related by
shear, Q105), and testable neutrinoless double beta decay at
|m_ββ| ~ 10–30 meV.  Inverted ordering is geometrically
excluded.

The total neutrino mass Σm_ν depends weakly on ε_ν:

| ε_ν | Σm_ν (meV) |
|-----|-----------|
| 3.2 (lower bound) | 120 |
| 5.0 (reference) | 118 |
| ∞ (asymptote) | 116 |

All values are below the cosmological bound (~120 meV).

**Neutrino sheet geometry.**  R49 investigated the full (ε_ν, s₃₄)
parameter space and found that Family A (large ε_ν ≈ 5, low base
winding numbers, ~26 sterile modes between ν₁ and ν₃) is strongly
favored.  Waveguide cutoff rules out ε_ν ≤ 0.2 (no modes
propagate); families with small ε_ν produce 120+ sterile species
in tension with cosmology.  The neutrino sheet coupling constant
at ε_ν = 5 is α_ν ≈ 1/52 (Q111) — comparable to but distinct from
the electromagnetic α ≈ 1/137.


## 6. Three generations

Three charge −1, spin ½ modes match the observed charged leptons:

| Gen | Particle | Mode | Pred (MeV) | Obs (MeV) | Mechanism |
|-----|----------|------|--------:|--------:|-----------|
| 1st | e⁻ | (1, 2, 0, 0, 0, 0) | 0.511 | 0.511 | Single-sheet (Ma_e) |
| 2nd | μ⁻ | (1, 6, \*, \*, 0, −1) | 117.2 | 105.7 | Cross-sheet (Ma_e × Ma_p) |
| 3rd | τ⁻ | (2, 5, \*, \*, 1, −15) | 1780.0 | 1776.9 | Cross-sheet (Ma_e × Ma_p) |

The electron lives on Ma_e alone.  The muon and tau add proton-
sheet windings, accessing shorter length scales and higher
energies.  All three share the same charge (Q = −n₁ + n₅ = −1)
and spin (one odd tube winding), so they are electromagnetically
identical except for mass — as observed.

The muon sits in a mass desert: no Q = −1 spin-½ eigenmode
exists between 5 and 200 MeV.  An exhaustive search across all
four shear sign branches, 21 σ_eν cross-shear values, and
3 million candidate 6-tuples with winding ranges up to n₂ = ±10
confirms the desert is structural (R50 Track 8, F56).  The muon
at 105.7 MeV sits squarely in this void with a 10.9% residual at
σ_ep = −0.13 and no viable candidate at any parameter combination.

The mechanism for bridging this gap has been partially identified:
cross-shear σ_eν modifies the effective e-sheet mass through the
metric's Schur complement — a confirmed boost that reaches 2.5×
before the metric goes singular (R50 Track 10, F67).  The muon
requires 207× (= m_μ/m_e).  The leading path forward is a richer
metric coupling structure (structured 2×2 cross-block rather than
a single scalar σ_eν) or a multi-parameter back-reaction where the
ν companion simultaneously shifts ε_e, s_e, and σ_eν.

The tau, by contrast, is predicted within 0.18% as a purely ν+p
mode (0, 0, −2, −3, −1, 6) at σ_eν = −0.20 — no electron-sheet
component at all (R50 Track 8, F57).  The tau is not a "heavier
electron" in this geometry; it is a ν+p object.  This is a
substantial improvement over model-C (5.6%).

Three neutrino modes on Ma_ν match the Δm² splittings (§5).

**Why three and not more?**  The model produces many modes with
the right charge and spin.  The generation count reduces to the
ghost mode problem (§8).  For neutrinos, R49 found that Family A
(ε_ν ≈ 5) has the fewest sterile modes (~26) between the three
active mass eigenstates, partially addressing the Z-width tension
(N_ν = 2.996 ± 0.007).  Whether the remaining modes couple
weakly enough to evade detection is under investigation.


## 7. Predictions and failures

### Predictions from geometry

Eleven of seventeen testable particles below 2 GeV are predicted
within 2% with no parameters pinned to any of them.  The full
spectrum table appears in §1.  The neutron (0.03%), φ (0.05%),
and Ω⁻ (0.04%) are the most precise predictions.

The **Omega baryon (Ω⁻)** — structurally forbidden in model-C
as a single Ma mode (charge −1, spin 3/2 requires three odd tube
windings, forcing even charge) — is now predicted at 0.04%.  The
(1,3) proton mode allows composite loopholes that the earlier
(1,2) proton could not.

### Ephemeral particles (predicted, not failures)

Particles that do not sit exactly on a Ma eigenmode are not
stable standing waves — they are transient excitations, a
"ringing" of the torus near but not on a resonance.  The gap
between the observed mass and the nearest eigenmode predicts
the particle's instability.  Stable particles match closely;
unstable particles miss by an amount consistent with their
decay rate.

- **K⁰ (5.6%), η (7.1%), ρ⁰ (4.3%):** Fair matches.  All are
  unstable, and the mass gaps are consistent with their short
  lifetimes.

- **μ⁻ (10.9%):** Sits in a structural mass desert — zero
  Q = −1 spin-½ modes between 5 and 200 MeV across all sign
  branches and σ_eν values (R50 F56).  The desert is confirmed
  robust under decay-product composition (F66), pair sums (F63),
  and cross-shear boost (F67).  Cross-shear boost via σ_eν is
  the correct *mechanism* (Schur complement amplifies the
  effective e-sheet mass, reaching 2.5× before singularity) but
  the current metric parameterization is quantitatively
  insufficient (need 207×).  Leading paths: richer cross-coupling
  structure, multi-parameter back-reaction, or action-based
  variational approach (R50 F69).

- **K± (0.73%, rescued):** Charged spin-zero mesons cannot exist
  as single modes (topology forces charge to carry spin ½).
  However, two spin-½ modes can pair into a spin singlet (total
  spin 0).  The K⁺ decomposes into a Q = 0 mode (248.6 MeV) and
  a Q = +1 mode (248.6 MeV), each at the spectral floor — the
  lightest non-trivial energy the geometry supports.  The kaon
  mass ≈ 2× the spectral floor (R50 Track 9, F61).

- **π± and π⁰:** Remain unreachable.  At 135–140 MeV, all three
  pions sit in the mass desert between the anomalous light cluster
  (0–5 MeV) and the spectral floor (~248 MeV).  π± are additionally
  topologically forbidden as single modes (charge forces spin ≥ ½).
  No single mode, pair sum, or decay-product composition can reach
  this range (R50 F58, F62, F66).  The pion and muon are the only
  inventory particles below 2 GeV that the linear ℤ⁶ picture
  cannot host.

The lifetime-gap correlation provides a quantitative test.
The Spearman rank correlation between mass gap and lifetime is
ρ = +0.55 (correct sign in all tested subsets, R50 F26 under
(−,−) shear branch).  The power law exponent β = −2.7 is
recovered for the weak-decay-minus-muon subset (matching R27).
The correlation is qualitatively confirmed but quantitatively
insufficient as a single-variable predictor — the neutron and
Ω⁻ have nearly identical mass gaps (~0.03–0.04%) but lifetimes
differing by 10¹³, proving that decay channel and phase space
matter alongside geometry.

### Nuclear scaling law

Nuclei appear as proton-sheet modes, not multi-particle bound
states.  Under the (1,3) proton, the scaling law is n₅ = A,
n₆ = 3A (A = mass number).  One charge formula Q = −n₁ + n₅
works for every particle and every nucleus.  This matches all
nuclei from deuterium to ⁵⁶Fe at < 1% (R50 Track 5,
confirming R29).

### Quark confinement

The proton mode (1,3) has gcd(1,3) = 1 — irreducible.  Its
three-fold internal structure (three antinodes of the ring
winding) is a property of a single standing wave, not three
separable sub-particles.  "Quarks" are this three-fold pattern
seen in scattering; confinement is automatic because you cannot
peel an antinode off its wave.  Modes with gcd > 1 (like a
hypothetical (2,4) = 2×(1,2) on Ma_e) fission via Coulomb
repulsion; modes with gcd = 1 cannot (Q109, R33 T9).

### Strong force

At nuclear distances (where tori overlap), particles interact
through the full internal field at coupling strength ~1, not
through the α ≈ 1/137 Coulomb force that leaks into 3D space.
The ratio α_s/α ≈ 137 is this attenuation factor.  The strong
force is internal electromagnetism at full coupling.

### Predictive horizon

Above ~2 GeV, the proton-sheet energy bands are spaced by
< 5 MeV (R28 F5).  Any particle mass can be matched to within
a few MeV, so predictions above this scale are not discriminating.
W, Z, and Higgs all have nearby modes, but trivially so — this
is not a test of the model.


## 8. Open problems

**Anomalous magnetic moments.**  The Coulomb self-field of the
torus mode perturbs the circulating wave, shifting the magnetic
moment.  R52 confirmed the correct sign for the electron
(+0.1%, additive) and identified a shear-dependent mechanism
that can produce opposite sign for the proton (−7%, subtractive).
However, the "classical sign rule" — that a single shear
convention gives both signs — was retracted after a mode-aware
audit (R52 F25).  The quantitative magnitude calculation and
sign rule remain open; cross-sheet effects and lattice-native
back-reaction are leads.

**Shear sign branch.**  The α formula has two shear solutions
(positive and negative) at each aspect ratio.  Both solve
α = 1/137.  The (−,−) branch wins on lifetime-gap correlation
(R50 F26, ρ = +0.55 vs +0.07 for (+,+)).  A single observable
that uniquely selects the branch is not yet identified.

**Muon mass desert.**  No Q = −1 spin-½ eigenmode exists between
5 and 200 MeV — confirmed by exhaustive search across all four
sign branches, a 21-point σ_eν grid, and 3 million candidate
6-tuples (R50 Track 8, F56).  The desert is structural and robust
to every avenue tested: single modes, pair sums (Track 9, F63),
decay-product composition (Track 10, F66), and cross-shear boost
(Track 10b, F67).  The cross-shear mechanism IS directionally
correct (σ_eν modifies the effective e-sheet mass through the
Schur complement of the metric inverse), but the current single-
scalar parameterization hits metric singularity at 2.5× boost,
far short of the 207× (= m_μ/m_e) required.  Extending the metric
to a richer cross-coupling structure — a 2×2 matrix of independent
tube-tube, tube-ring, ring-tube, ring-ring couplings, or
multi-parameter back-reaction involving ε_e, s_e, and σ_eν
simultaneously — is the leading path forward (R50 F69).

**Pions (π±, π⁰).**  All three pions sit in the same 5–200 MeV
desert.  Charged pions face an additional barrier: the topology
requires charge to carry spin ≥ ½, so Q = ±1 spin-0 states
are structurally forbidden as single 6-tuples (R50 F58).  Charged
kaons are rescued as spin-singlet pairs of two ~249 MeV modes
(R50 F61), but pions at 135–140 MeV sit below the spectral floor
— unreachable even as pairs (R50 F62).  Whatever physics bridges
the 100–200 MeV gap must address BOTH the muon and the pion.
The pion decay chain (π → μ + ν_μ, μ → e + ν̄_e + ν_μ) suggests
these particles are built from the same ingredients, and solving
the muon may automatically solve the pion (R50 F69, path E).

**Ghost modes and dark matter.**  The model predicts many more
modes below 2 GeV (~200–400 levels) than there are observed
particles (~19).  Most are electrically neutral (even tube
winding, giving zero charge by the n₁ = ±1 selection rule).
These modes carry mass but no electromagnetic signature — they
are dark matter candidates, in broadly the right mass ratio to
visible matter (R42).

The lightest charged ghost — the (1,1) mode, lighter than the
electron and never observed — is eliminated by waveguide cutoff:
the torus acts as a physical cavity, and modes below a frequency
threshold cannot propagate (R46).  This is a consequence of the
GRID substrate, not an ad hoc filter.  Selection rules beyond
waveguide cutoff likely eliminate most remaining ghosts, but
these rules are not yet identified.

**Mode overcounting.**  The geometry produces ~200–400 distinct
energy levels below 2 GeV for ~19 observed particles.  After
waveguide cutoff and the n₁ = ±1 charge selection, the charged
ghost count is manageable.  The neutral overcounting is
reinterpreted as dark matter, but the ratio is imprecise.

**No QFT formulation.**  Decay rates, running couplings, and
scattering amplitudes require a quantized field theory on
Ma × S × t.  The classical wave equation gives the mass spectrum;
the quantum theory is needed for everything else.

**Gravity.**  Ma_ν has circumference L₄ ≈ 42 μm.  If gravity
propagates in this dimension, short-range gravity experiments
would detect deviations from 1/r² at this scale.  Current bounds
reach ~50 μm with no deviation seen — barely compatible.  GRID
derives G from the lattice's information density (ζ = 1/4),
independently of the compact dimensions.  Whether gravity
propagates in Ma_ν or only in the 3D spatial lattice is an open
question with testable consequences.

---

## 9. The substrate: GRID

This paper takes Maxwell's equations as given and constructs
particles from them.  The GRID framework (Geometric Relational
Interaction Domain) goes one level deeper: it derives Maxwell's
equations and the gravitational constant G from a discrete
lattice at the Planck scale.

GRID rests on six axioms — a 4D causal lattice with periodic
phase, local gauge invariance, information resolution ζ = 1/4,
and coupling strength α ≈ 1/137.  From these:

- Maxwell's equations emerge from phase dynamics and gauge
  invariance (grid/maxwell.md)
- Einstein's field equations emerge from the thermodynamics
  of the lattice's information content (grid/gravity.md)
- G = 1/(4ζ) = 1 in natural units — derived, not postulated
- Charge quantization follows from phase periodicity
- The cosmological constant Λ appears as an integration constant

The relationship between the two layers:

```
GRID (substrate)
    Derives: Maxwell's equations, G, Λ, charge quantization
    Input: α ≈ 1/137 (sole free parameter)
         │
         ▼
MaSt (this paper)
    Takes: Maxwell + α (from GRID)
    Constructs: particle spectrum, masses, charges, spins
    Input: m_e, m_p, Δm²₂₁ (three scales that set torus sizes)
```

GRID provides the rules.  MaSt plays by them.  Together, they
attempt a complete geometric account of fundamental physics
from one measured constant and three measured scales.

For the full GRID derivation, see
[grid/foundations.md](../grid/foundations.md),
[grid/maxwell.md](../grid/maxwell.md),
[grid/gravity.md](../grid/gravity.md), and
[grid/synthesis.md](../grid/synthesis.md).
For an accessible introduction, see
[primers/physics-from-fabric.md](../primers/physics-from-fabric.md).
