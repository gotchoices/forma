# R27. T⁶ oscillation patterns — particles, atoms, and nuclei  *(active)*

**Questions:** Q16 (mass spectrum), Q28 (photon absorption / energy levels), Q32 (energy-geometry)
**Type:** compute/analytical  **Depends on:** R26, R19, R15


## Background and definitions

### The T⁶ model

The T⁶ is a six-dimensional compact torus composed of three
T² subplanes — one each for the electron, neutrino, and proton.
A quantum field on this geometry has modes (standing waves)
labeled by six integer quantum numbers (n₁, n₂, n₃, n₄, n₅, n₆).
Each mode has a definite mass, charge, and spin determined by
its quantum numbers and the geometry.

### Dimensions and circumferences

Each T² has two compact dimensions: a "ring" and a "tube."

| Index | Dimension | Circumference | Physical scale | Role |
|-------|-----------|---------------|---------------|------|
| 1     | Electron ring  | L₁ | ~3.2 × 10⁴ fm (nm) | Electron Compton ring |
| 2     | Electron tube  | L₂ | ~4.9 × 10³ fm (nm) | Electron tube |
| 3     | Neutrino ring  | L₃ | ~2.1 × 10¹¹ fm (mm) | Neutrino Compton ring |
| 4     | Neutrino tube  | L₄ | ~4.2 × 10¹⁰ fm (mm) | Neutrino tube |
| 5     | Proton ring    | L₅ | ~2.4 × 10¹ fm (fm) | Proton Compton ring |
| 6     | Proton tube    | L₆ | ~2.7 fm | Proton tube |

### Aspect ratios

Each T² has an aspect ratio r = L_ring / L_tube:

| Symbol | Definition | Status |
|--------|-----------|--------|
| r_e    | L₁ / L₂  | Free (invisible at MeV scale) |
| r_ν    | L₃ / L₄  | Free (invisible at MeV scale) |
| r_p    | L₅ / L₆  | **Determined: r_p = 8.906** (from neutron + muon masses) |

### Within-plane shear parameters

Each T² can be sheared (the tube tilted relative to the ring).
These parameters are determined by measured constants:

| Symbol | Plane | Value | Determined by |
|--------|-------|-------|--------------|
| s₁₂    | Electron (T²_e) | Depends on r_e via α formula | Fine structure constant α |
| s₃₄    | Neutrino (T²_ν) | 0.022 | Neutrino mass ratio Δm²₃₁/Δm²₂₁ |
| s₅₆    | Proton (T²_p)   | Depends on r_p via α formula | Fine structure constant α |

### Cross-plane shear parameters (σ)

Cross-shears couple different T² subplanes.  They are the
mechanism that produces cross-sheet modes (like the neutron)
and determines the particle spectrum beyond the three inputs.

**Symmetric (collective) parameterization** — 3 parameters:

| Symbol | Coupling | Status |
|--------|---------|--------|
| σ_ep   | Electron ↔ Proton  | **Determined: σ_ep = −0.0906** (from neutron mass) |
| σ_eν   | Electron ↔ Neutrino | Free (zero for now) |
| σ_νp   | Neutrino ↔ Proton   | Free (zero for now) |

Each collective σ sets all 4 entries in its cross-block to the
same value.  For example, σ_ep sets σ₁₅ = σ₁₆ = σ₂₅ = σ₂₆.

**Asymmetric (full) parameterization** — 12 parameters:

Each cross-block has 4 independent entries:
- e-p block: σ₁₅, σ₁₆, σ₂₅, σ₂₆
- e-ν block: σ₁₃, σ₁₄, σ₂₃, σ₂₄
- ν-p block: σ₃₅, σ₃₆, σ₄₅, σ₄₆

Asymmetric shears can create intermediate energy levels that
symmetric shears cannot reach.

### Metric tensor

The dimensionless scaled metric G̃ (6×6 matrix) encodes all
the geometry:

    G̃_ij = G_ij / (L_i × L_j)

where G is the physical metric.  Mode energies are:

    E(n) = ℏc × √( (n/L)ᵀ · G̃⁻¹ · (n/L) )

The metric must be positive-definite for the geometry to be
physical.  This constrains the shear parameters.

### Mode properties

| Property | Rule | Example |
|----------|------|---------|
| Charge   | Q = −n₁ + n₅ (units of e) | Electron (1,2,0,0,0,0): Q = −1 |
| Spin     | Count of odd ring windings (n₁, n₃, n₅) | 1 odd → spin ½; 0 or 2 → boson |
| Mass     | E(n) from metric formula | Depends on all parameters |

### Self-consistent treatment

When cross-shears are nonzero, the input particle masses shift.
The self-consistent solver iteratively adjusts L₂ and L₆ so
that E(electron) = m_e and E(proton) = m_p exactly at every
parameter point.  All results in this study use self-consistent
circumferences.


## Motivation

R26 showed that the T⁶ produces an emergent neutron.  R27
Tracks 1–3 found the correct self-consistent neutron mode
and simultaneously matched the muon, pinning two parameters
(r_p = 8.906 and σ_ep = −0.0906).

Track 4 showed that the tau mass falls in a structural gap
of the proton-scale energy ladder — no single T⁶ mode exists
at 1776.9 MeV.  Preliminary Track 5 work found the kaon at
1.2% error and the pion at 13.6% — both parameter-free
predictions.

**Key reframing (from findings discussion):**

Stable particles (electron, proton, neutrinos) are **exact
eigenmodes** of the T⁶ — perfect standing waves.  Unstable
particles need not be exact eigenmodes.  They are **transient,
off-resonance excitations** — energy temporarily in a
configuration close to but not exactly on a mode.  The gap
between the observed mass and the nearest mode energy is
physically meaningful:

- Particles close to a mode resonate longer (longer lifetime).
- Particles far from a mode decay quickly (shorter lifetime).
- Particles always appear in reactions where total energy
  and quantum numbers are conserved.  The energy of the
  transient pattern is determined by the reaction kinematics,
  not by the nearest mode.

This changes the question from "does a mode exist at exactly
this mass?" to "is there a nearby mode, and does the gap
correlate with the particle's lifetime and production context?"


## Core hypothesis

**The T⁶ has a discrete spectrum of eigenmodes.  Stable
particles are exact eigenmodes.  Unstable particles are
off-resonance excitations whose lifetimes correlate with their
distance from the nearest eigenmode.  The full spectrum of
observed particles — stable and unstable — is explained by
the eigenmode structure plus reaction kinematics.**


## Approach

### Track 1 — Self-consistent neutron mass  ✔

**Status:** Complete.  See findings F1–F8.

Key results:
- The naive (1,2,0,0,1,2) mode with symmetric σ_ep is
  quantitatively insufficient (max m_n − m_p ≈ 0.50 MeV).
- Negative σ_ep gives the correct sign (m_n > m_p).
- The qualitative neutron picture is intact; the quantitative
  mode identification required the discovery engine (Track 2).


### Track 2 — T⁶ mode solver (discovery engine)  ✔

**Status:** Complete.  See findings F9.

Built `lib/t6_solver.py` on top of `lib/t6.py`:
- `find_modes()` — search for modes matching target properties
- `self_consistent_metric()` — metric with exact input masses
- `multi_target_optimize()` — match multiple targets at once


### Track 3 — Neutron and muon identification  ✔

**Status:** Complete.  See findings F10–F21.

Key results:
- Neutron: mode (0, −2, n₃_odd, n₄, 0, +2),
  σ_ep = −0.0906 gives m_n − m_p = 1.293 MeV exactly.
- Muon: mode (−1, +5, 0, 0, −2, 0),
  r_p = 8.906 gives m_μ = 105.658 MeV exactly.
- Both matched simultaneously.  Two parameters determined.


### Track 4 — Asymmetric cross-shears and the tau  ✔

**Status:** Complete.  See findings F22–F26.

Key results:
- The tau mass falls in a structural gap of the proton-scale
  energy ladder (between n₆ = ±3 at ~1408 MeV and n₆ = ±4
  at ~1877 MeV).
- Asymmetric cross-shears shift energies by at most ±2 MeV.
- No single T⁶ mode exists at 1776.9 MeV.
- This motivates the off-resonance reframing.


### Track 5 — Systematic particle catalog  ✔

**Status:** Complete.  See findings F31–F36.

Key results: 19 particles searched, 5 within 1.5% (kaons, η, η′, φ),
Ω⁻ structurally forbidden (spin-3/2 + odd charge impossible).

For **every well-measured unstable particle**, compute:

1. Nearest T⁶ mode with matching charge and spin
2. Mode energy (parameter-free, since r_p and σ_ep are pinned)
3. Gap = observed mass − nearest mode energy
4. Gap direction (above or below the mode)
5. Fractional gap = |gap| / observed mass

**Particle catalog** (targets):

| Particle | Full name       | Mass (MeV) | Q  | Spin | Lifetime |
|----------|----------------|-----------|-----|------|----------|
| μ⁻       | muon           | 105.66    | −1  | ½    | 2.20 μs  |
| π⁺       | pion (charged) | 139.57    | +1  | 0    | 26.0 ns  |
| π⁰       | pion (neutral) | 135.0     |  0  | 0    | 8.5×10⁻¹⁷ s |
| K⁺       | kaon (charged) | 493.68    | +1  | 0    | 12.4 ns  |
| K⁰       | kaon (neutral) | 497.61    |  0  | 0    | varies   |
| η        | eta meson      | 547.86    |  0  | 0    | 5.0×10⁻¹⁹ s |
| ρ⁰       | rho meson      | 775.3     |  0  | 1    | 4.5×10⁻²⁴ s |
| ω        | omega meson    | 782.7     |  0  | 1    | 7.7×10⁻²³ s |
| n        | neutron        | 939.565   |  0  | ½    | 878 s    |
| Δ⁺⁺      | delta baryon   | 1232      | +2  | 3/2  | 5.6×10⁻²⁴ s |
| τ⁻       | tau            | 1776.9    | −1  | ½    | 2.9×10⁻¹³ s |

Also include the stable particles (electron, proton) with
gap = 0 and lifetime = ∞ as reference points.

**Deliverable:** A complete table: particle, observed mass,
nearest mode, mode energy, gap, lifetime.


### Track 6 — Lifetime-gap correlation  ✔

**Status:** Complete.  See findings F37–F42.

Key results: r = −0.84 (p = 0.009) for weak decays.  Two-factor
model: interaction strength sets baseline, gap modulates within class.

The central test of the off-resonance hypothesis.

**Method:**

1. From the Track 5 catalog, extract (gap, lifetime) pairs.
2. Plot log(lifetime) vs log(|gap|) or |gap|/mass.
3. Test for correlation: do short-lived particles have large
   gaps?  Do long-lived ones have small gaps?
4. The stable particles (e, p, ν) should be at gap = 0,
   lifetime = ∞.  The neutron should be at a very small gap
   and the longest finite lifetime.

**What to look for:**

- Monotonic relationship → strong support for the off-resonance
  picture.
- Clustering → groups of particles may share a decay mechanism.
- Outliers → particles that break the trend may be composites
  or require different mechanisms.

**Deliverable:** Correlation plot and statistical analysis.


### Track 7 — Reaction energetics  ✔

**Status:** Complete.  See findings F43–F49.

Key results: 21 reactions tested, 17/21 sign-consistent.  All
leptonic/meson decays pass.  4 sign flips in strange baryon decays.

Do reaction conservation laws work at the T⁶ mode level?

**Method:** For well-measured reactions, check whether the
total nearest-mode energies balance:

| Reaction | Input modes | Output modes |
|----------|-------------|-------------|
| π⁻ → μ⁻ + ν̄_μ | E(π mode) | E(μ mode) + E(ν) |
| K⁺ → μ⁺ + ν_μ | E(K mode) | E(μ mode) + E(ν) |
| n → p + e⁻ + ν̄_e | E(n mode) | E(p) + E(e) + E(ν) |
| τ⁻ → μ⁻ + ν̄_μ + ν_τ | E(τ mode?) | E(μ mode) + 2E(ν) |

If particle masses don't exactly equal mode energies, does
the mismatch cancel when you look at complete reactions?
For example: if the pion's mass is 19 MeV below its mode
energy, does that 19 MeV appear as extra kinetic energy in
the decay products?

**Deliverable:** Mode-energy balance table for common decays.


### Track 8 — Nuclear stability criterion  *(deferred)*

Why a neutron in a nucleus doesn't decay.  Requires multi-mode
formalism.  Deferred until the single-particle picture is clear.


### Track 9 — Hydrogen-like patterns  *(deferred)*

Requires well-determined geometry.  Deferred until the particle
spectrum constrains enough parameters.


### Track 10 — Deuteron-like patterns  *(deferred)*

Deferred with Track 9.


## Infrastructure

### `lib/t6.py` — low-level T⁶ model

- Metric construction (`build_scaled_metric`)
- Mode energies (`mode_energy`)
- Charge and spin (`mode_charge`, `mode_spin`)
- Spectral scanning (`scan_modes`)

### `lib/t6_solver.py` — discovery engine

- `find_modes(target, ...)` — search for modes matching targets
- `self_consistent_metric(sigmas, ...)` — self-consistent metric
- `self_consistent_metric_asym(...)` — asymmetric cross-shears
- `multi_target_optimize(targets, ...)` — multi-target search

Track-specific scripts go in `bound-states/scripts/`.


## What this study could determine

### Free parameters constrained

| Source | Constraint |
|--------|-----------|
| m_n − m_p = 1.293 MeV | **Done:** pins σ_ep = −0.0906 |
| m_μ = 105.658 MeV | **Done:** pins r_p = 8.906 |
| Lifetime-gap correlation | Tests off-resonance hypothesis |
| Reaction energy balance | Tests mode-energy conservation |
| Hydrogen binding 13.6 eV | Constrains cross-shear strength |

### Possible outcomes

**Best case:** The lifetime-gap correlation is strong, reaction
energetics balance, and the T⁶ mode spectrum explains both
stable and unstable particles through the off-resonance
mechanism.  The model transitions from "fitting masses" to
"predicting lifetimes."

**Partial success:** Some particles fit the off-resonance
picture but others (especially short-lived resonances like ρ,
Δ) require multi-mode or nonlinear effects.  The boundary
between single-mode and composite physics is identified.

**Null result:** No correlation between gap and lifetime.  The
T⁶ mode spectrum is not sufficient to explain unstable
particles even as off-resonance excitations.


## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R26 | T⁶ framework, initial neutron discovery, metric infrastructure |
| R19 | Shear-charge mechanism — origin of the EM field on T² |
| R15 | The α problem — hydrogen binding could solve it |
| R20 F17 | First mention of muon/tau as "hot electrons" |
