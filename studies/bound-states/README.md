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

R26 showed that the T⁶ produces an emergent neutron — a cross-
sheet mode with zero charge and mass near m_n.  R27 Track 1
showed that the naive mode identification needed revision, and
Track 3 found the correct self-consistent neutron mode.  The
neutron + muon together pin two parameters (r_p and σ_ep).

This study now pursues two parallel goals:

1. **Particle spectrum** — find T⁶ modes matching known unstable
   particles (tau, pions, W, Z, ...).  Each match pins more
   parameters.  Enough matches fully determine the geometry.

2. **Bound states** — find T⁶ oscillation patterns with the
   properties of atoms and nuclei (hydrogen, deuteron).


## Core hypothesis

**The T⁶ supports oscillation patterns — single modes or compound
configurations — with the observed properties of known particles,
atoms, and nuclei.  These patterns are discoverable by systematic
search over quantum numbers and metric parameters.**


## Approach

### Track 1 — Self-consistent neutron mass  ✔

**Status:** Complete.  See findings F1–F8.

Key results:
- The naive (1,2,0,0,1,2) mode with symmetric σ_ep is
  quantitatively insufficient (max m_n − m_p ≈ 0.50 MeV).
- Negative σ_ep gives the correct sign (m_n > m_p).
- Alternative modes (0, −3, n₃, n₄, 0, 2) achieve 0.93 MeV.
- The qualitative neutron picture is intact; the quantitative
  mode identification is open.


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
- Tau: nearest mode at 1876.4 MeV (+5.6%).


### Track 4 — Asymmetric cross-shears and the tau

The tau mass (1776.9 MeV) falls between rungs of the proton-
scale energy ladder.  Symmetric cross-shears cannot reach it.

**Method:** Extend the solver to use all 12 independent σ_ij
entries instead of 3 collective values.  Search for parameter
combinations where:
- Neutron mass remains exact
- Muon mass remains exact
- A charge −1, spin ½ mode appears at 1776.9 MeV

The 12-parameter space is large but heavily constrained by the
neutron and muon requirements.

**Deliverable:** Tau mode identification and constrained σ_ij
values, or a determination that the tau requires mechanisms
beyond single-mode KK physics.


### Track 5 — Extended particle spectrum

With parameters pinned by neutron + muon + (hopefully) tau,
search for additional known particles:

**Fundamental particles:**

| Particle | Full name | Mass (MeV) | Charge | Spin |
|----------|-----------|-----------|--------|------|
| μ⁻       | muon      | 105.66    | −1     | ½    |
| τ⁻       | tau       | 1776.9    | −1     | ½    |
| W⁻       | W boson   | 80,377    | −1     | 1    |
| Z⁰       | Z boson   | 91,188    |  0     | 1    |
| H⁰       | Higgs     | 125,250   |  0     | 0    |

**Composite particles (mesons and baryons):**

| Particle | Full name    | Mass (MeV) | Charge | Spin |
|----------|-------------|-----------|--------|------|
| π⁺       | pion (plus)  | 139.6     | +1     | 0    |
| π⁰       | pion (zero)  | 135.0     |  0     | 0    |
| K⁺       | kaon (plus)  | 493.7     | +1     | 0    |
| η        | eta meson    | 547.9     |  0     | 0    |
| ρ⁰       | rho meson    | 775.3     |  0     | 1    |
| Δ⁺⁺      | delta baryon | 1232      | +2     | 3/2  |

Each match adds a constraint equation on the free parameters.

**Deliverable:** Mode assignments for matched particles, or
identification of which particles are genuinely composite
(not single T⁶ modes).


### Track 6 — Lifetime correlations

A mode's instability should correlate with its "distance" from
fundamental modes in quantum number space.

**Method:** For each matched particle, compute a distance metric
between its mode and the nearest fundamental mode.  Plot against
measured lifetime.

**Deliverable:** Distance-vs-lifetime plot.  If monotonic, this
provides a geometric interpretation of particle lifetimes.


### Track 7 — Nuclear stability criterion

A neutron in a nucleus is stable.  A free neutron decays.

**Hypothesis:** The neutron mode's energy depends on what other
modes are simultaneously present.  In isolation, E_n > m_p + m_e
(decay allowed).  With a proton mode present, the compound
pattern has lower energy (neutron trapped).

**Deliverable:** Whether the T⁶ produces different effective
neutron masses in isolation vs in a nuclear environment.


### Track 8 — Hydrogen-like patterns

Search for T⁶ oscillation patterns with hydrogen properties:
    charge = 0
    mass ≈ m_p + m_e − 13.6 eV
    discrete excited states at −13.6/n² eV

Requires the geometry to be well-determined first (from particle
spectrum tracks), since the 13.6 eV binding energy is 10⁸ times
smaller than the rest masses.

**Deliverable:** Hydrogen-like T⁶ pattern, or identification of
what prevents it.


### Track 9 — Deuteron-like patterns

Search for a proton-neutron bound state:
    charge = +1e
    mass = m_p + m_n − 2.224 MeV
    spin = 1

**Deliverable:** Deuteron-like T⁶ pattern, or diagnosis of why
the simplest nucleus doesn't emerge.


## Infrastructure

### `lib/t6.py` — low-level T⁶ model

- Metric construction (`build_scaled_metric`)
- Mode energies (`mode_energy`)
- Charge and spin (`mode_charge`, `mode_spin`)
- Spectral scanning (`scan_modes`)

### `lib/t6_solver.py` — discovery engine

- `find_modes(target, ...)` — search for modes matching targets
- `self_consistent_metric(sigmas, ...)` — self-consistent metric
- `multi_target_optimize(targets, ...)` — multi-target search

Track-specific scripts go in `bound-states/scripts/`.


## What this study could determine

### Free parameters constrained

| Source | Constraint |
|--------|-----------|
| m_n − m_p = 1.293 MeV | **Done:** pins σ_ep = −0.0906 |
| m_μ = 105.658 MeV | **Done:** pins r_p = 8.906 |
| m_τ = 1776.9 MeV | Expected: pins asymmetric σ_ij entries |
| Each additional particle | One more constraint equation |
| Hydrogen binding 13.6 eV | Constrains cross-shear strength |
| α from binding energy | Relates r_e to shears |

### Possible outcomes

**Best case:** Asymmetric shears close the tau gap, 3+ more
particles match, the geometry is fully determined, and hydrogen
emerges as a compound pattern.

**Partial success:** Neutron and muon are matched (done), tau
and a few more particles constrain most parameters, but atoms
require mechanisms beyond single-mode T⁶ physics.

**Null result (informative):** The tau requires mechanisms not
in the current model.  This would point to specific extensions
(nonlinear coupling, backreaction on the metric, etc.).


## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R26 | T⁶ framework, initial neutron discovery, metric infrastructure |
| R19 | Shear-charge mechanism — origin of the EM field on T² |
| R15 | The α problem — hydrogen binding could solve it |
| R20 F17 | First mention of muon/tau as "hot electrons" |
