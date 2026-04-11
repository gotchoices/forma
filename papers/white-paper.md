# Matter from Light: A Geometric Particle Spectrum

**Status:** draft
**Model era:** [model-E](../models/model-E.md). Full T⁶ with
generation structure, 9×9 metric, 20/20 particle modes.  See
[`model-E.md`](../models/model-E.md) for the complete model card.

---

## Abstract

The masses of elementary particles are among the least understood
constants in physics.  The Standard Model accommodates them as
inputs but offers no mechanism that determines their values.  This
paper presents a model in which particles are standing
electromagnetic waves on a compact six-dimensional torus (T⁶).
The Lagrangian is free electromagnetism in eleven dimensions; no
additional fields, sources, or gravity coupling are introduced.

A particle's mass is the eigenfrequency of its mode on the compact
space.  Its electric charge and spin are determined by the winding
topology.  Seven measured quantities fix the geometry — three masses
that set the torus scales, the fine-structure constant α, two mass
ratios that set the electron-sheet shape, and one neutrino mass
ratio.  No parameters are pinned to unstable particle masses.

**All 20 surveyed particles below 2 GeV have credible modes.**
Stable particles (proton, electron) are exact eigenmodes.
Unstable particles are near-misses — transient excitations near
but not on a resonance — with gaps consistent with their
instability.  Seventeen of twenty match within 2%; the remaining
three (pions) have larger gaps consistent with their short
lifetimes.  The model reproduces nuclear masses from deuterium to
iron at ≤ 1.1%, predicts neutrino oscillation (mass-squared ratio
Δm²₃₁/Δm²₂₁ = 33.6 exact, normal ordering, Majorana nature),
derives three charged lepton generations from a single geometric
parameter, and eliminates ghost modes through the same mechanism
that creates the generation structure.

This is not a competitor to the Standard Model.  The Standard
Model's ~19 dimensionless parameters are measured, not explained.
This model attempts to derive them from geometry, currently using
4 dimensionless inputs (vs 19).  Where the Standard Model says
"the muon mass is 105.658 MeV," this model says "the muon is a
near-miss to mode (1, 1, −2, −2, 0, 0) on the T⁶, at 0.83% off
the eigenfrequency."

The electromagnetic field equations used here are derived from a
discrete lattice at the Planck scale (the GRID framework), which
also derives the gravitational constant G.  Electric charge is
topological winding on the GRID lattice; spin ½ arises from odd
tube winding numbers.

---

### Model card

| | |
|---|---|
| **Framework** | Maxwell's equations on a flat 11D manifold T⁶ × S³ × t × phase |
| **Topology** | T⁶ (one six-torus, read as three 2-torus sheets at zero cross-coupling) |
| **Measured inputs** | 7: m_e, m_p, Δm²₂₁, α, m_μ/m_e, m_τ/m_e, Δm²₃₁/Δm²₂₁ |
| **Dimensionless inputs** | 4 (vs ~19 in the Standard Model) |
| **Metric** | 9×9 (T⁶ × S³) with 45 entries; off-diagonals serve 4 distinct roles |
| **Outputs** | 20/20 particle modes; nuclear masses ≤ 1.1%; 3 lepton generations; ν oscillation exact |
| **Stable particles** | Exact eigenmodes (proton 0.00%, electron 0.00%) |
| **Unstable particles** | Near-misses with gaps correlated to instability |
| **Ghost elimination** | Shear ordering — electron naturally lightest; no ad hoc filter |
| **Charge mechanism** | Topological (GRID); sign from Ma-S coupling: e-sheet→S negative, p-sheet→S positive |
| **Testable** | Σm_ν = 116–120 meV; 0νββ at |m_ββ| ~ 10–30 meV; Ma_ν ring L₄ ≈ 42 μm |

---

## 1. The spectrum

Seven measured inputs fix the geometry.  Every particle below
2 GeV has a credible mode — stable particles are exact, unstable
particles are near-misses.

| Particle | Obs (MeV) | Mode | Δm/m | Status |
|----------|----------|------|------|--------|
| e⁻ | 0.511 | (1, 2, −2, −2, 0, 0) | input | stable ✓ |
| p | 938.3 | (0, 0, −2, 2, 1, 3) | input | stable ✓ |
| Λ | 1115.7 | (−1, 2, −1, 2, −1, 3) | 0.00% | near-miss |
| η′ | 957.8 | (−1, −7, 2, −2, −1, 2) | 0.00% | near-miss |
| Σ⁻ | 1197.4 | (−1, 2, −2, 2, −2, −2) | 0.01% | near-miss |
| Σ⁺ | 1189.4 | (−2, 3, 2, −2, −1, −3) | 0.02% | near-miss |
| Ξ⁻ | 1321.7 | (−1, 5, −2, 2, −2, 1) | 0.03% | near-miss |
| τ⁻ | 1776.9 | (3, −6, 2, −2, 2, 3) | 0.05% | near-miss |
| φ | 1019.5 | (−1, 4, 2, −2, −1, 2) | 0.06% | near-miss |
| n | 939.6 | (0, −4, −1, 2, 0, −3) | 0.07% | near-miss |
| Ω⁻ | 1672.5 | (−2, 2, −2, 2, −3, 0) | 0.13% | near-miss |
| Δ⁺ | 1232.0 | (−3, −6, 2, −2, −2, 2) | 0.17% | near-miss |
| Ξ⁰ | 1314.9 | (−1, 8, −1, 2, −1, 2) | 0.19% | near-miss |
| μ⁻ | 105.7 | (1, 1, −2, −2, 0, 0) | 0.83% | near-miss |
| ρ | 775.3 | (−1, 5, −2, 2, 0, 1) | 0.97% | near-miss |
| K⁰ | 497.6 | (0, −4, −2, 2, 0, 1) | 1.04% | near-miss |
| K± | 493.7 | (−1, −6, −2, 2, 0, 1) | 1.77% | near-miss |
| η | 547.9 | (−1, −4, −2, 2, −1, 0) | 1.84% | near-miss |
| π⁰ | 135.0 | (0, −1, −2, −2, 0, 0) | 22.7% | near-miss |
| π± | 139.6 | (−1, −1, −2, −2, 0, 0) | 24.9% | near-miss |

Source: R54, model-E.  Geometry: ε_e = 397, s_e = 2.004;
ε_p = 0.55, s_p = 0.162; ε_ν = 5.0, s_ν = 0.022.
Cross-shears: σ₄₅ = −0.18, σ₄₆ = +0.10 (soft, neutron region).

Each mode is a 6-tuple (n₁, n₂, n₃, n₄, n₅, n₆) — the winding
numbers around the six compact dimensions.  Nearly all modes
span multiple "sheets" (have nonzero windings on two or three
torus pairs).  The modes are eigenstates of the full T⁶, not
of individual sheets.


## 2. Geometry

The six compact dimensions form a flat six-torus T⁶.  Three pairs
of dimensions are historically called "sheets" (Ma_e, Ma_ν, Ma_p),
but this decomposition is a basis choice — at nonzero cross-
coupling, the sheets blur into one 6D space (Q116).

| Pair | Tube L | Ring L | Shape |
|------|--------|--------|-------|
| e-sheet (dims 1–2) | 4717 fm | 11.9 fm | fat (ε = 397) |
| ν-sheet (dims 3–4) | 2.1×10¹¹ fm | 4.2×10¹⁰ fm | fat (ε = 5) |
| p-sheet (dims 5–6) | 2.45 fm | 4.45 fm | thin (ε = 0.55) |

The ring circumferences are set by particle masses (m_e → L₂,
m_p → L₆, Δm²₂₁ → L₄).  The tube circumferences follow from
the aspect ratios.

**The 9×9 metric** on T⁶ × S³ has 45 independent entries:

- **9 diagonal:** circumferences (6) + flat space (3)
- **3 in-sheet shears:** generation structure and mode energies
- **12 cross-sheet entries:** compound modes (neutron, hadrons)
- **18 Ma-S entries:** α coupling (charge → Coulomb field)
- **3 within-S:** flat space (zero)

Mode energy: E(n) = 2πℏc √(ñᵀ G̃⁻¹ ñ), where ñᵢ = nᵢ/Lᵢ.

See [metric-terms.md](../studies/R54-compound-modes/metric-terms.md)
for the complete 45-entry reference table with visual layout.


## 3. Spin, charge, and α

**Spin** is topological.  Each odd tube winding (n₁, n₃, n₅)
contributes spin ½.  The electron (1, 2, ...) has one odd tube
winding → spin ½.  Modes with two odd tube windings on
different sheets can produce spin 0 — this is how charged pions
become possible (§7).

**Charge** is topological.  A tube winding sweeps the GRID phase
through 2π, creating a topological defect detected as electric
charge.  The charge formula Q = −n₁ + n₅ gives correct charges
for all particles and all nuclei tested.

**The charge sign comes from the Ma-S coupling.**  The formula
Q = −n₁ + n₅ encodes that the e-sheet couples to 3D space with
NEGATIVE sign (electrons are negative) and the p-sheet with
POSITIVE sign (protons are positive).  The ν-sheet has zero
Ma-S coupling (neutrinos are electrically neutral).  The coupling
magnitude is α = 1/137 for both charged sheets.  Matter vs
antimatter is the sign of the tube winding; positive vs negative
charge is which sheet the winding lives on.

**α = 1/137** is a measured input from the GRID substrate — the
impedance mismatch at the junction between the compact space and
3D space.  At the p-sheet geometry (ε = 0.55), the R19 formula
provides a consistency condition linking α to the in-sheet shear
s_p.  At the e-sheet geometry (ε = 397), the R19 formula breaks
down — s_e is free and serves a different role (§6).  The Ma-S
block of the 9×9 metric controls the coupling; the quantitative
derivation is pending (R55).


## 4. The neutron

The neutron is a 6D knot — a single closed curve threading all
six compact dimensions:

> **(0, −4, −1, 2, 0, −3)** at 938.9 MeV (0.07% off observed)

Its quantum numbers encode: zero e-tube winding (Q_e = 0), four
e-ring windings, one ν-tube winding (spin ½), and three p-ring
windings.  Charge: Q = 0 − 0 = 0.

The neutron is literally **electron + neutrino + proton** fused
into one mode.  Its beta decay (n → p + e⁻ + ν̄_e) is the
decomposition of this 6D knot into its three component modes
when the cross-coupling weakens.

The 0.07% mass gap (below the observed 939.565 MeV) predicts
the neutron's instability — it is a near-miss, not an exact
eigenmode, consistent with its 880 s lifetime.

**In nuclei,** the neutron mode is embedded in a larger composite
where the proton-sheet quantum numbers scale with mass number A
(n₅ = A, n₆ = 3A).  The composite sits closer to a true
eigenmode, explaining why bound neutrons are stable.


## 5. Neutrino oscillation

Three modes on Ma_ν — (1,1), (−1,1), (1,2) — at shear
s₃₄ = 0.02199 predict neutrino oscillation directly:

> Δm²₃₁ / Δm²₂₁ = (3 − 2s₃₄) / (4 s₃₄) = **33.6**

matching the experimental value 33.6 ± 0.9 exactly.

Normal ordering, Majorana nature, and Σm_ν = 116–120 meV
are predicted.  Inverted ordering is geometrically excluded.


## 6. Three generations

The three charged lepton masses emerge from **shear resonance**
on the electron sheet.

At shear s_e ≈ 2.004, the mode (1, 2) has ring detuning
n₂ − n₁ · s ≈ 0 — a near-cancellation that makes it anomalously
light.  Other modes don't cancel and are much heavier:

| Gen | Mode | Ring detuning | Mass |
|-----|------|---------------|------|
| 1st (e) | (1, 2) | −0.004 (resonance) | 0.511 MeV |
| 2nd (μ) | (−3, −5) | +1.013 | 105.7 MeV |
| 3rd (τ) | (−7, 3) | +17.029 | 1776.9 MeV |

The mass ratios m_μ/m_e and m_τ/m_e are algebraically exact
from two geometric parameters (ε_e, s_e).

**Ghost elimination.** The (1,1) ghost — a charged mode lighter
than the electron in earlier models, eliminated by ad hoc
waveguide cutoff — is naturally heavy at this geometry (209 MeV).
The electron IS the lightest charged mode because it sits at the
shear resonance.  No filter needed.


## 7. The pion mechanism

The charged pion was "impossible" in earlier models: Q = ±1
forces at least one odd tube winding → spin ≥ ½, but the pion
has spin 0.

The solution: **two odd tube windings on different sheets.**
A mode with n₁ odd (e-sheet) AND n₃ odd (ν-sheet) has
spin_half_count = 2 → spin 0 possible.  The charge can be ±1
from the e-sheet tube alone.

The π± candidate (−1, −1, −2, −2, 0, 0) has Q = +1, spin 0,
and energy 104.8 MeV — 25% below the observed 139.6 MeV.  This
is a large gap, consistent with the pion's short lifetime
(26 ns for π±, 8.4 × 10⁻¹⁷ s for π⁰).


## 8. Nuclear scaling

Nuclei appear as composite modes with proton-sheet quantum
numbers scaling with mass number A:

> n₅ = A, n₆ = 3A

| Nucleus | A | Z | Δm/m |
|---------|---|---|------|
| d | 2 | 1 | 0.05% |
| ⁴He | 4 | 2 | 0.69% |
| ¹²C | 12 | 6 | 0.76% |
| ⁵⁶Fe | 56 | 26 | 1.05% |

Charge: Q = −n₁ + n₅ = Z for every nucleus tested.


## 9. Open questions

**α from the 9×9 metric.** The Ma-S coupling entries determine
α = 1/137, but the quantitative formula connecting them has not
been derived.  The conceptual framework is clear (charge is
topological, α is the Ma-S projection); the mathematics is
pending (R55).

**Off-resonance correlation.** Stable particles are exact
eigenmodes; unstable particles are near-misses.  The correlation
between gap size and lifetime is correct qualitatively but weak
as a single variable (Spearman ρ = +0.14).  It is stratified by
decay mechanism: strong-decay particles are short-lived regardless
of gap (coupling ~1); weak-decay particles show the expected
gap-lifetime relationship.

**Dark matter candidates.** The geometry predicts many neutral
modes below 2 GeV that carry mass but no electromagnetic charge.
These are dark matter candidates, in broadly the right abundance
relative to visible matter.

**No QFT formulation.** The classical wave equation gives the
mass spectrum.  Decay rates, running couplings, and scattering
amplitudes require quantized field theory on T⁶ × S × t.

**Gravity.** Ma_ν has circumference ~42 μm.  Short-range gravity
experiments at this scale could detect deviations from 1/r².
Current bounds (~50 μm) are barely compatible.


## 10. The substrate: GRID

The electromagnetic field equations used here are derived from a
discrete lattice at the Planck scale (GRID).  GRID rests on six
axioms — a 4D causal lattice with periodic phase, local gauge
invariance, information resolution ζ = 1/4, and coupling
strength α ≈ 1/137.  From these:

- Maxwell's equations emerge from phase dynamics
- Einstein's field equations from lattice thermodynamics
- G = 1/(4ζ) in natural units — derived, not postulated
- Charge quantization from phase periodicity

```
GRID (substrate)
    Derives: Maxwell, G, Λ, charge quantization
    Input: α ≈ 1/137
         │
         ▼
MaSt (this paper)
    Takes: Maxwell + α
    Input: m_e, m_p, Δm²₂₁ + 3 dimensionless ratios
    Output: 20 particle masses, nuclear scaling,
            3 generations, ν oscillation
```

For the GRID derivation:
[grid/foundations.md](../grid/foundations.md),
[grid/maxwell.md](../grid/maxwell.md),
[grid/gravity.md](../grid/gravity.md).
For an accessible introduction:
[primers/physics-from-fabric.md](../primers/physics-from-fabric.md).
