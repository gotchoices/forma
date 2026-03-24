# R28. Unstable particle spectrum from T⁶  *(draft)*

**Questions:** Q16 (mass spectrum), Q32 (energy-geometry)
**Type:** compute  **Depends on:** R26

## Motivation

R26 established the T⁶ framework and discovered the emergent
neutron — a cross-sheet mode that was not designed into the model.
The neutron is the simplest cross-sheet vibration.  But the T⁶
has an infinite spectrum of modes at higher quantum numbers.

Every unstable particle ever observed — the muon, the tau, the W
and Z bosons, pions, kaons, and hundreds of hadronic resonances —
eventually decays to the stable T⁶ residents: electrons, protons,
and neutrinos.  These particles are not permanent features of
nature; they are transient excitations that ring unstably before
cascading down to the ground-state modes.

In the T⁶ picture, an unstable particle is a higher mode of the
geometry: energy temporarily occupying a non-fundamental quantum
number configuration.  The decay is the wave relaxing to lower
modes — the T⁶ equivalent of a guitar string settling from an
overtone to its fundamental.

**The opportunity:** Every particle with measured mass, charge,
and spin is a potential T⁶ mode match.  Each match adds a mass
equation constraining the 15 free parameters of the metric.  With
enough matches, the system becomes over-determined — the geometry
is fully pinned, and every subsequent prediction is parameter-free.

This study is the most direct path from "compatible" to
"predictive."


## Core hypothesis

**Unstable particles are excited T⁶ modes — higher quantum
number vibrations of the same geometry that hosts the electron,
neutrino, and proton.  Their masses, charges, and spins are
determined by mode quantum numbers (n₁, ..., n₆) and the T⁶
metric.**


## The particle catalog

### Fundamental particles (not composite in the standard model)

| Particle | Mass (MeV) | Q/e | Spin | Lifetime | T⁶ signature |
|----------|-----------|-----|------|----------|---------------|
| μ⁻       | 105.66    | −1  | ½    | 2.2 μs   | Odd n₁ (charged), one odd tube winding (spin ½) |
| τ⁻       | 1776.9    | −1  | ½    | 0.29 ps  | Odd n₁, one odd tube winding |
| W⁻       | 80,377    | −1  | 1    | ~3×10⁻²⁵ s | Odd n₁ + one other odd tube winding |
| Z⁰       | 91,188    |  0  | 1    | ~3×10⁻²⁵ s | Even n₁, two odd tube windings |
| H⁰       | 125,250   |  0  | 0    | ~1.6×10⁻²² s | All tube windings even |

### Composite particles (quark-antiquark or three-quark)

Whether composite particles map to single T⁶ modes or to
multi-mode bound states is an open question.  However, each has
a definite mass, charge, and spin — if a T⁶ mode matches, the
match is still a valid constraint.

| Particle | Mass (MeV) | Q/e | Spin | Lifetime |
|----------|-----------|-----|------|----------|
| π⁺       | 139.6     | +1  | 0    | 26 ns    |
| π⁰       | 135.0     |  0  | 0    | 8.5×10⁻¹⁷ s |
| K⁺       | 493.7     | +1  | 0    | 12.4 ns  |
| η        | 547.9     |  0  | 0    | 5×10⁻¹⁹ s |
| ρ⁰       | 775.3     |  0  | 1    | 4.5×10⁻²⁴ s |
| ω        | 782.7     |  0  | 1    | 7.7×10⁻²³ s |
| Δ⁺⁺      | 1232      | +2  | 3/2  | 5.6×10⁻²⁴ s |

The Δ⁺⁺ (charge +2e) is particularly interesting: in the T⁶,
charge +2e requires the mode to wind the electron tube AND the
proton tube, both contributing +e.  The quantum number constraints
are very specific.


## Quantum number selection rules

In the T⁶, charge and spin are determined by mode quantum numbers
(n₁, n₃, n₅ = tube windings; n₂, n₄, n₆ = ring windings):

| Property | Rule | Mechanism |
|----------|------|-----------|
| Charge −e | n₁ odd | Electron tube winding |
| Charge +e | n₅ odd | Proton tube winding |
| Charge 0 | n₁ even AND n₅ even, or both odd (cancel) | |
| Spin ½ | Odd number of odd tube windings (n₁, n₃, n₅) | |
| Spin 0 | Even number of odd tube windings (0 or 2) | |
| Spin 1 | Two odd tube windings (vector-like) | |

These rules constrain which mode quantum numbers can correspond
to which particles.  A charged spin-0 particle (like π⁺) requires
odd n₁ or n₅ (for charge) but an even count of odd tube windings
(for spin 0).  This means exactly one of (n₁, n₃, n₅) is odd
and the particle must also have another odd tube winding — or
the spin-0 assignment requires a different mechanism.  These
tensions are themselves diagnostics: if no T⁶ mode can match
a particle's quantum numbers, that particle may genuinely be
composite (not a single mode).


## Approach

### Track 1 — Extended spectral scan

Extend the R26 Track 4d spectral scan from |n_i| ≤ 3 to
|n_i| ≤ 15–20.

**Method:** For each mode (n₁, ..., n₆) in this range, compute:
- Mass: E(n) from the scaled metric G̃
- Charge: from n₁, n₅ parities
- Spin: from tube winding parities (n₁, n₃, n₅)

Catalog all modes below 200 GeV.  The number of modes grows as
~n_max⁶, so at n_max = 15 this is ~10⁷ modes — large but
computationally tractable (each mode energy is a single matrix
multiplication).

**Deliverable:** Full T⁶ mode catalog as a function of the free
parameters (3 aspect ratios + cross-shears), stored in a
searchable format.


### Track 2 — Match score function

Build an objective function that measures how well a given T⁶
geometry matches the known particle spectrum.

**Method:** For each known particle p with mass m_p, charge Q_p,
spin s_p:

1. Find all T⁶ modes with charge = Q_p and spin = s_p.
2. Among those, find the mode closest in mass to m_p.
3. Compute the fractional mass error: |E(n) − m_p| / m_p.

The match score is the product (or sum of log) of mass errors
across all particles.  Low score = good match.

**Subtlety:** Must avoid double-counting — each T⁶ mode can
match at most one particle.  Use a bipartite matching algorithm
(Hungarian method) to find the optimal mode-to-particle
assignment.

**Deliverable:** Match score function S(r_e, r_ν, r_p, σ_ij)
that can be evaluated at any point in parameter space.


### Track 3 — Parameter optimization

Minimize the match score over the 15 free parameters.

**Method:** The parameter space is 15-dimensional but heavily
constrained:
- Positivity bounds restrict σ_ij (R26 F70)
- Aspect ratios r > 0
- Neutron mass fixes σ_ep ≈ 0.038 (R26 F67)
- Neutrino mass ratio constrains s₃₄ = 0.022 (R26 F1)

With these pre-constraints, the effective search space is
~10-dimensional.  Use a combination of:
1. Coarse grid scan to identify promising regions
2. Gradient-free optimizer (Nelder-Mead or differential
   evolution) to refine
3. Local gradient descent to find precise minimum

**Deliverable:** The optimal parameter set(s) and the list of
which T⁶ modes match which particles.  If multiple distinct
minima exist, report all.


### Track 4 — Muon and tau identification

Focus specifically on the muon (105.66 MeV, Q = −e, spin ½)
and tau (1776.9 MeV, Q = −e, spin ½).

**Why separate:** These are the highest-confidence matches.
Both are fundamental (not composite), have the same quantum
numbers as the electron, and their masses are precisely known.
They are "excited electrons" — higher modes on or involving the
electron T² sheet.

**Method:**
1. Enumerate all modes with Q = −e, spin = ½, mass in
   [100, 120] MeV (muon) and [1750, 1800] MeV (tau).
2. For each candidate mode, determine how the aspect ratios
   and cross-shears must be set to achieve the target mass.
3. Check whether the muon constraint and tau constraint can
   be satisfied simultaneously.

**What to look for:** A parameter region where a single T⁶
geometry produces modes at 0.511 MeV (electron), 105.66 MeV
(muon), AND 1776.9 MeV (tau), all with charge −e and spin ½.
If this exists, it pins at least two free parameters.

**Deliverable:** The quantum numbers of the muon and tau
modes, or a finding that no single-mode assignment works (in
which case they might be multi-mode states or require a
different mechanism).


### Track 5 — W and Z identification

The W (80.4 GeV, Q = −e, spin 1) and Z (91.2 GeV, Q = 0,
spin 1) are the heaviest fundamental particles after the Higgs.

**Method:** Similar to Track 4 but at much higher mass.  At
80 GeV, the quantum numbers must be large (since the electron
T² has Compton energy 0.511 MeV).  Search for modes with:
- W: Q = −e, spin 1, E ≈ 80,377 MeV
- Z: Q = 0, spin 1, E ≈ 91,188 MeV

**What to look for:** Whether the W/Z mass ratio m_Z/m_W ≈ 1.134
is naturally produced by the T⁶ spectrum.  In the standard model,
this ratio involves the Weinberg angle.  If the T⁶ produces it
geometrically, it would connect the Weinberg angle to compact
geometry.

**Deliverable:** Mode assignments for W and Z, or a finding that
these masses require quantum numbers too high for the scan range.


### Track 6 — Lifetime correlations

A mode's instability (decay rate) should correlate with how
"far" it is from the fundamental modes in quantum number space.

**Method:** For each matched particle, compute a "distance"
metric in the 6D quantum number space between the particle's mode
and the nearest fundamental mode it can decay to.  Plot this
distance against the measured lifetime.

**What to look for:** A monotonic relationship — modes closer to
the fundamentals live longer.  The muon (long-lived, low quantum
numbers) should be "close" and the W/Z (extremely short-lived,
high quantum numbers) should be "far."

**Deliverable:** Distance-vs-lifetime plot.  If monotonic, this
provides a geometric interpretation of particle lifetimes.


## What this study could determine

### Free parameters eliminated

The T⁶ has 15 free parameters.  6 are already constrained
(m_e, m_p, α, Δm²₂₁, Δm² ratio, s₅₆).

Each particle match adds one mass equation:

| Matches | Free parameters remaining |
|---------|--------------------------|
| 0 (current) | 15 − 6 = 9 free |
| + neutron (σ_ep) | 8 free |
| + muon | 7 free |
| + tau | 6 free |
| + W | 5 free |
| + Z | 4 free |
| + PMNS angles (3) | 1 free |
| + any one more | 0 free (fully determined) |

With 5 particle matches beyond the neutron, plus the 3 PMNS
angles (from R26 N3 / cross-shear structure), the T⁶ geometry
is fully determined.  Every additional observable is then a
**pure prediction** that can confirm or falsify the model.


### Possible outcomes

**Best case:** A single parameter point matches 5+ particles
with correct mass, charge, and spin.  The geometry is determined.
The remaining spectrum (pions, kaons, etc.) is either confirmed
or reveals the boundary between single-mode and composite
particles.

**Partial success:** Muon and tau are found as T⁶ modes,
constraining 2 parameters.  Heavier particles require larger
quantum number scans or composite-mode treatment.  The model's
scope is clarified.

**Null result:** No T⁶ mode matches the muon at 105.66 MeV
with correct quantum numbers, for any parameter values.  This
would mean the muon is not a simple excitation of the T⁶ ground
state — it might require a mechanism not captured by the
single-mode approximation.

**Diagnostic value of failure:** Even a null result is
informative.  If charged spin-½ modes at 105.66 MeV exist only
at extreme aspect ratios (r → ∞ or r → 0), that constrains the
geometry.  If no modes exist at that mass at all, the model's
mode-counting (single-particle T⁶ modes) is too simple and
multi-mode or nonlinear effects are needed.


## Infrastructure

All tracks use the shared `lib/t6.py` module for:
- Metric construction (`build_scaled_metric`)
- Mode energies (`mode_energy`)
- Charge and spin (`mode_charge`, `mode_spin`)
- Spectral scanning (`scan_modes`)
- Positivity checks (`is_positive_definite`)

Track-specific scripts go in `particle-spectrum/scripts/`.


## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R26 | T⁶ framework, metric infrastructure, neutron discovery, parameter census, spectral scan at low quantum numbers |
| R26 N6 | Detailed proposal for this study, including quantum number selection rules and match-score approach |
| R20 F17 | First mention of muon/tau as "hot electrons" — excited states of the electron |
| R19 | Shear-charge mechanism — determines which modes are charged |
| R27 | Companion study: atoms and nuclei as T⁶ oscillation patterns; uses same infrastructure |


## What this study does NOT address

- **Forces and bound states.**  That is R27.  This study finds
  single-mode matches, not multi-mode composites.
- **Quarks.**  Quarks are confined and never observed as free
  particles.  Matching their masses (2–175 GeV) against T⁶ modes
  is problematic because the "quark mass" is scheme-dependent.
- **The gravitational bound** (R26 N7).  The neutrino T²'s mm
  scale versus sub-mm gravity tests is a separate concern.
- **Why the geometry is what it is.**  This study determines the
  geometry empirically (by fitting).  Why those particular values
  emerge from a deeper principle is a separate question (R26 N5).
