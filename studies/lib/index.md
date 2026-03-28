# lib/ — MaSt model library

This folder contains the computational tools for the MaSt
(Material-Space-time) model.  Everything here is imported by
study scripts under `studies/R**/scripts/`.


## Files

### constants.py

Physical and mathematical constants (CODATA 2018, PDG 2022).
Provides `h`, `hbar`, `c`, `alpha`, `m_e`, etc.  Used by all
other modules.  No model logic.


### wvm.py — WvM charge model (historical)

The original Williamson–van der Mark charge formula:

    q = (1/2π) √(3 ε₀ ℏ c)

This predicts q/e ≈ 1.10 — close but not exact.  The WvM model
assumes the electron is a photon with circular polarization on
an embedded torus, so the E-field always points outward.  The
charge is the Gauss-law integral of this field over the torus
surface.

**Status:** Historical.  Superseded by the KK charge formula in
`ma.py`.  Still imported by early studies (R1–R13).  The WvM
integral is the basis for R19's shear-induced charge mechanism
and R33's ghost suppression via the |n₁| = 1 selection rule.


### series.py — Geometric series utilities (historical)

Simple geometric series functions used by early toroid-series
studies.  No connection to the Ma model.


### ma.py — Ma model (current)

The core model library.  All studies from R26 onward import this.
Provides:

| Function | Purpose |
|----------|---------|
| `alpha_ma(r, s)` | α from sheet geometry (R19 F35 formula) |
| `solve_shear_for_alpha(r)` | Invert α(r,s) to find s at a given r |
| `mu_12(r, s)` | Dimensionless (1,2) mode energy |
| `compute_scales(r_e, r_nu, r_p)` | Derive L₁–L₆ and shears from aspect ratios |
| `build_scaled_metric(...)` | Build the 6×6 dimensionless metric G̃ |
| `mode_energy(n, Gti, L)` | Energy of a mode (MeV) from the quadratic form |
| `mode_charge(n)` | Electric charge: Q = −n₁ + n₅ (KK formula) |
| `mode_spin(n)` | Spin-½ count from odd tube windings |
| `scan_modes(Gti, L, ...)` | Brute-force enumerate all modes |
| `is_positive_definite(Gt)` | Metric diagnostic |
| `epstein_zeta(...)` | Casimir/vacuum energy (Epstein zeta function) |

**Charge formula:** `mode_charge` uses the KK (Kaluza–Klein)
formula Q = −n₁ + n₅.  This is compact momentum on the flat
torus — a topological quantity.  It gives correct integer charges
for all R27/R28 particle matches.  Its weakness is the ghost
problem: every mode with the right quantum numbers carries integer
charge, producing ~14,000 levels where nature shows 3 charged
leptons.

**Energy formula:** E(n) = 2πℏc √(ñᵀ G̃⁻¹ ñ), where ñᵢ = nᵢ/Lᵢ.
This is a quadratic form on the integer lattice Z⁶.

**Metric:** The dimensionless metric G̃ is built from:
- Within-plane shears (s₁₂, s₃₄, s₅₆) via B = diag(L)(I + S)
- Cross-plane shears (σ_ep, etc.) added to off-diagonal blocks
- G̃_ij = G^phys_ij / (L_i L_j)

**Limitations:** Purely functional (no state), brute-force
enumeration (O(n⁶)), no energy decomposition, no Jacobian,
no inverse solver.  See `ma-model.md` for the planned upgrade.


### ma_solver.py — Discovery engine

Search and optimization tools built on `ma.py`.  Provides:

| Function | Purpose |
|----------|---------|
| `self_consistent_metric(...)` | Iteratively adjust L so m_e and m_p are exact at any σ_ep |
| `self_consistent_metric_asym(...)` | Same, with 12 independent cross-shear entries |
| `find_modes(...)` | Search for modes near a target (mass, charge, spin) |
| `multi_target_optimize(...)` | Optimize σ parameters to match multiple targets (uses differential_evolution) |

The self-consistent solver is a simple fixed-point iteration:
compute L → measure mass error → rescale L by the ratio →
repeat.  Converges in ~5–10 iterations.

`find_modes` and `multi_target_optimize` use brute-force
enumeration internally.  At n_max = 15, this is impractical
(31⁶ ≈ 900M modes).  The planned `ma_model.py` will replace
the inner loop with ellipsoid-based lattice enumeration.


### ma_model.py — Next-generation model (planned)

See [`ma-model.md`](ma-model.md) for the design spec.  Will
provide an object-oriented `Ma` class with efficient algorithms,
energy decomposition, Jacobian, and inverse solving — without
breaking any existing scripts.

**Scope:** Intrinsic geometry.  Mode spectrum on the flat torus.
"What modes exist and what are their energies?"


### embedded.py — Embedded torus near-field (planned)

See [`embedded.md`](embedded.md) for the design spec.  Computes
how Ma modes project into 3D space: charge distributions along
geodesics, E-fields, multipole decomposition, and interaction
energies between particles at specified separations and phase
offsets.  First use: R39 (phase-dependent near-field interaction).

**Scope:** Extrinsic geometry.  How modes look from outside.
"What forces do particles exert on each other at close range?"

**Relationship to ma_model.py:** Separate module.  Uses the
same geometry parameters (L₁–L₆) but adds the embedding
(R, a) and 3D field calculations.  Does not depend on
ma_model.py — only on ma.py for circumferences and constants.


## Charge formula history

The project has used two charge formulas.  Understanding both
is essential for reading findings across studies.

The transition between them reflects a deeper conceptual shift:
from a **ray-optics** picture (photon-as-particle circulating on
a torus) to a **wave-mechanics** picture (particle-as-standing-
wave on a flat compact manifold).

### WvM charge integral (R1–R19, R33)

**Physical picture:** A photon travels along a geodesic path on
an embedded torus.  The circular polarization keeps the E-field
pointing outward as the photon circulates.  Charge is the
Gauss-law surface integral of this field over the torus — it
measures how much net electric flux the circulating photon
produces when viewed from outside.

This is a **ray-optics / geometric-optics** model.  The photon
is a localized object moving on a path.  The embedding curvature
(how the torus surface curves through 3D space) is essential:
it rotates the polarization and creates the monopole moment.
R13 F6 confirmed that a photon on a *flat* torus (no embedding)
produces zero charge — the embedding is doing the work.

The integral selects |n_tube| = 1 per sheet due to Fourier
orthogonality against the (R + a cos θ) curvature factor:

    Q ∝ sin(2πs) / (n_ring − n_tube × s)

Strengths:
- Produces α from geometry (R19)
- The |n₁| = 1 selection rule kills most ghost modes (R33)
- Predicts electron is the lightest charged particle (R19 F31)

Weaknesses:
- Gives fractional charge for the muon (−0.40 instead of −1)
- Gives zero charge for kaons and most R27 matches
- Relies on embedding curvature (absent on a flat quotient torus)

### KK compact momentum (R26 onward, current)

**Physical picture:** A particle is a standing wave (eigenmode)
on the flat 6-torus Ma.  It is not something traveling on a
path — it is the mode itself.  Charge is the quantized compact
momentum: a topological quantum number of the wave function,
counting how many times the phase wraps around each compact
direction.

This is a **wave-mechanics** model.  No embedding is needed.
The flat torus wave equation directly yields integer-quantized
momenta in each compact dimension, and charge is a linear
combination of these:

    Q = −n₁ + n₅

Strengths:
- Correct integer charges for ALL matched particles (R27 F31)
- Naturally arises from the wave equation on a flat manifold
- No embedding assumptions

Weaknesses:
- Every mode with the right winding numbers has integer charge
- ~14,000 charge −1, spin ½ levels below 10 GeV (R38 F1)
- Ghost suppression requires an additional mechanism (open)

### Relationship

Each formula captures something the other misses.  KK gives
correct charges for all known particles; WvM gives a selection
rule that suppresses ghost modes.

One interpretation (speculative, untested): KK gives the true
topological charge, and the WvM integral describes a *coupling
form factor* — how strongly a mode's fields project into 3D
space.  Modes with weak WvM coupling would be "dark" (present
as geometric solutions but unobservable).  This would reconcile
the ghost problem with the KK spectrum.

See R38 findings and `scripts/track4_charge_integral_6d.py`
in R38 for the detailed numerical comparison.


## Model evolution

| Era | Studies | Picture | Charge | Metric | Key advance |
|-----|---------|---------|--------|--------|-------------|
| Single torus | R1–R13 | Ray optics | WvM | 2D embedded | Electron as photon circulating on torus |
| Sheared torus | R14–R19 | Ray optics | WvM + α | 2D/3D sheared | α from geometry, shear-induced charge |
| Three tori (Ma) | R20–R25 | Transitional | WvM | 6D product | Proton, neutrino, muon as modes |
| Ma + KK | R26–R38 | Wave mechanics | KK | 6D flat + σ | Particles as eigenmodes, full spectrum |
