# R30. Minimal compact geometry — is T² necessary?

**Questions:** Q34 (what selects α), Q16 (mass spectrum)
**Type:** theoretical + compute  **Depends on:** R19, R26, R27
**Status:** Active


## Motivation

Each particle in the T⁶ model lives on a T² — a
two-dimensional torus.  But the physics seems to inhabit a
**curve**, not a surface.  The electron is the (1,2)
geodesic: a one-dimensional closed path that happens to
wrap around a two-dimensional torus.  The full T² provides
the *context* for how the curve wraps, but the particle
itself occupies a 1D path.

This raises a fundamental question: **does the T² structure
carry more dimensions than the physics requires?**

Several clues suggest it might:

1. **One-parameter families.**  Each T² has an aspect ratio
   r that is unconstrained (r_e completely free, r_ν ≥ 3.2,
   r_p pinned only because we have a second particle — the
   neutron — to anchor it).  A model with exactly the right
   number of degrees of freedom would have no free parameters.
   The persistent r-degeneracy may signal a redundant
   dimension.

2. **Curves, not surfaces.**  The (1,2) geodesic on a
   sheared torus is a 1D closed curve.  Its length, its
   wrapping pattern, and its charge all depend on the
   2D torus geometry — but the wave function lives *along*
   the curve, not across the surface.

3. **Ghost modes.**  The T⁶ predicts ~900 modes below
   2 GeV but nature shows ~40 particles.  The 20×
   over-prediction might reflect extra geometric structure
   that produces modes nature doesn't need.

4. **Photons are 1D.**  A photon is a transverse
   oscillation with one polarization degree of freedom.
   If a particle is "a photon on compact geometry," and
   the photon is intrinsically 1D, why does it need a
   2D space to live on?


## Core questions

1. **Can a single compact dimension (T¹) reproduce any
   of the particle properties (mass, charge, spin)?**
   What specifically requires a second dimension?

2. **Is the charge mechanism irreducibly 2D?**  Charge
   in R19 comes from shear between tube and ring
   directions.  Is there a 1D analogue — charge from
   curvature, twist, or non-uniform metric?

3. **What is the minimum compact geometry that produces
   quantized charge?**  T¹ (circle), T² (torus),
   Klein bottle, Möbius strip, or something else?

4. **What happens when one T² dimension shrinks to zero?**
   If the tube circumference L_tube → 0 (r → ∞), the T²
   degenerates toward T¹ (just the ring).  Does charge
   survive this limit?  Does it emerge gradually or
   vanish discontinuously?

5. **Can a non-orientable identification (Klein bottle)
   produce charge or spin effects that a torus cannot?**
   We have never investigated non-orientable compact spaces.

6. **If the tube is itself further compactified** (a circle
   of circles — hierarchical compactification), does this
   effectively reduce T² to T¹ at accessible energies,
   deferring the second dimension to a higher energy scale
   (possibly Planck)?

7. **Can a 1D space with non-uniform metric reproduce
   T²-like mode structure?**  A circle with g(x) = f(x)
   has a Mathieu-like spectrum with band gaps and avoided
   crossings.  Could this mimic the T² energy ladder?


## Context from prior studies

### What T² currently provides

Each T² sheet in the T⁶ model contributes:

- **Two length scales** (L_tube, L_ring) → mass + aspect ratio
- **Shear** (σ between directions) → charge (R19)
- **Two winding numbers** (n_tube, n_ring) → mode energy
- **Tube parity** (odd/even n_tube) → spin contribution

The charge formula Q = −n₁ + n₅ fundamentally needs two
independent winding numbers from different compact
directions.  On T¹, there is only one winding number.

### What T¹ provides

A single compact dimension (circle of circumference L):

- **One length scale** L → mass
- **One winding number** n → mode energy E_n = |n| ℏc/L
- **No shear** (only one direction) → no charge mechanism
- **Parity** (odd/even n) → possible spin contribution

E_n forms a simple harmonic ladder.  Setting E₁ = m_e c²
gives L = λ̄_e (Compton wavelength).  The spectrum is
regular: no band gaps, no avoided crossings, no structural
richness.

### What a 1D cavity (interval) provides

An interval [0, L] with boundary conditions:

- **Standing waves** sin(nπx/L) with E_n = nℏc/(2L)
- **Boundaries break translational symmetry** — different
  from T¹ (periodic) or T² (doubly periodic)
- Adding boundary conditions to a 1D space does NOT add
  a dimension — it constrains solutions within the
  existing 1D space

### Aspect ratio constraints (from prior studies)

| Parameter | Constraint | Source |
|-----------|-----------|--------|
| r_e | > ~0.26 (shear-charge lower bound) | R19 |
| r_e | unconstrained at MeV scale | R29 F22 |
| r_e | contradictory bounds from spectroscopy vs shear | atoms-from-geometry paper |
| r_ν | ≥ ~3.2 (cosmological Σm bound) | R26 F32 |
| r_p | = 8.906 (pinned by neutron + muon) | R27 F18 |

Only r_p is pinned, and only because a second observable
(neutron mass) constrains the proton sheet.  The electron
and neutrino aspect ratios are effectively free — a sign
of over-parameterization.

### Klein bottle and non-orientable spaces

**Never investigated.**  The only non-orientable reference
in the project is a metaphorical "Möbius-like" description
of the spin mechanism in the knot-zoo study (the E-field
picks up a phase of π per traversal → spin ½ from two
circuits).  This metaphor was never formalized as a study
of compact geometry with reversed identification.

A Klein bottle is formed by identifying opposite edges of
a rectangle with one pair reversed:

    T²:            (x, 0) ~ (x, L₂)  and  (0, y) ~ (L₁, y)
    Klein bottle:  (x, 0) ~ (x, L₂)  and  (0, y) ~ (L₁, L₂ − y)

The reversed identification breaks orientability and
changes the mode spectrum.  Whether this affects charge
or spin is unknown.


### Hierarchical compactification

**Never investigated.**  If the tube dimension has
circumference L_tube ≪ L_ring, then modes with n_tube ≥ 1
have energy ≫ ℏc/L_ring and decouple at low energies.
In the extreme limit L_tube → 0 (r → ∞):

- Only n_tube = 0 modes survive at low energy
- The effective geometry reduces to T¹ (the ring)
- Charge requires n_tube ≠ 0 (the (1,2) mode has
  n_tube = 1), so charge vanishes in this limit

The opposite limit r → 0 (ring shrinks, tube dominates)
has its own interesting structure: charged modes are at
minimal energy, but the mass spectrum degenerates.

An intermediate scenario: the tube circumference is at
a scale between Compton and Planck.  Low-energy physics
sees T¹; T²-effects appear only at high energies.  But
the electron IS a T²-effect (charge from winding) — so
this seems to require the tube at Compton scale.

Could there be a *third* level of compactification below
the tube?  A circle of circles of circles?  Each level
would add structure at a higher energy scale.  The tube
at Compton scale (~10⁻¹² m) is already far above the
Planck scale (~10⁻³⁵ m) — there is room for many levels.


## Approach — tracks

### Track 1 — T¹ electron: what works, what fails

Build a T¹ solver (circle of circumference L).  Check:
- Mass quantization: E_n = nℏc/L
- Spin: can parity of n give spin ½?
- Charge: what mechanism, if any, produces charge on T¹?
- g-factor: any analogue?

Compare the T¹ spectrum to T² at the same mass scale.
Document exactly what T² adds over T¹.

### Track 2 — Non-uniform T¹: can complexity replace dimensions?

A circle with position-dependent metric g(x) has a mode
equation that produces non-trivially spaced energies
(Mathieu-like).  Explore:
- Can a specific g(x) reproduce the electron's T² mode
  structure (mass ratios, spin)?
- Does the non-uniformity create an effective "second
  direction" that mimics shear?
- What is the minimal complexity of g(x) needed to
  get charge-like behavior?

### Track 3 — Klein bottle and non-orientable identifications

Replace the standard T² identification with the Klein
bottle identification (one edge reversed).  Compute:
- Mode spectrum: how does it differ from T²?
- Charge: does the reversed identification affect the
  Gauss flux integral?
- Spin: does the orientation-reversal change the phase
  accumulation?
- Does the Klein bottle produce fewer ghost modes?

### Track 4 — The r → ∞ limit: T² degenerating to T¹

Take the existing T² solver and examine the large-r limit:
- How do mode energies behave as r → ∞?
- At what r does the charge mechanism break down?
- Is there a smooth transition from "charged T²" to
  "uncharged T¹," or a sharp phase boundary?
- Does r_p = 8.906 (our pinned proton value) sit near
  any critical threshold?

### Track 5 — Minimum geometry for charge

Theoretical analysis: what is the simplest compact space
that produces quantized electric charge?

Candidates:
- T¹: no (only one winding number)
- T²: yes (shear between two directions)
- Klein bottle: unknown (Track 3)
- Möbius strip: has a boundary — not compact
- T¹ with twist: a circle with antiperiodic boundary
  conditions (ψ(x+L) = −ψ(x)) — changes mode spectrum
  but may not produce charge
- Lens space L(p,q): 3D analogue of T² — compact,
  orientable, with topological invariants

If T² is the minimum, that gives a structural reason
for 6 compact dimensions (3 sheets × 2 per sheet).
If something simpler works, it suggests the model can
be compressed.


### Track 6 — Shared-dimension T³: electron and proton on a common surface

**Motivation:**  The electron T² (dims 1,2) and proton T²
(dims 5,6) have no shared dimensions in T⁶ — they are
coupled only through the cross-shear σ_ep.  What if they
share a dimension, reducing T⁶ to T³ (plus the neutrino
sheet, treated separately)?

The user's key questions:
- Can the electron and proton ratios work in a shared T³?
- Does sharing a dimension eliminate one degree of freedom
  or just defer it?
- Could the neutrino sheet be folded in too, or is it
  too far off in scale?

**Preliminary analysis (diagonal T³, no shear):**

A T³ with circumferences (L_a, L_b, L_c) can accommodate:

    Electron (1, 2, 0):  E_e = m_e      Q = −1
    Proton   (0, 1, 1):  E_p = m_p      Q = +1
    Neutron  (1, n_b, 1): E_n = m_n     Q =  0

with charge Q = −n_a + n_c (analogous to T⁶'s Q = −n₁ + n₅).

Circumferences:
    L_a ≈ 419 fm  (electron tube scale)
    L_b ≈ free    (shared dimension, any L_b > 772 fm)
    L_c ≈ 0.21 fm (proton ring scale)

The neutron is mode (1, ~499, 1) — it bridges the 1.293 MeV
mass gap using a high winding on the shared dimension.
Preliminary result: m_n − m_p = 1.291 MeV (0.002 MeV off!).

This is encouraging but raises questions:
- The neutron's n_b ≈ 499 is a high winding.  In T⁶, the
  neutron has small quantum numbers on all dimensions.
  Is n_b = 499 physical or a sign that T³ needs shear?
- L_b is free — same r-degeneracy as T², just fewer copies.
- The neutrino scale is 10¹⁰× larger than L_a.  Sharing
  with the neutrino is almost certainly not viable.

**Computational plan:**
1. Build a T³ solver with metric, shear, and charge.
2. Pin L_a and L_c by electron and proton masses.
3. Sweep L_b and compute the full particle spectrum.
4. Check spin assignment from winding parities.
5. Compare ghost-mode count to T⁶ (fewer dimensions
   should mean fewer ghosts).
6. Test whether T³ with shear can reduce the neutron's
   n_b to a small value (as σ_ep does in T⁶).
7. Assess whether the muon, pion, kaon, and other
   particles find modes in the T³ spectrum.

**Success criterion:**  T³ reproduces at least the core
particles (e, p, n, μ, π, K) with comparable accuracy
to T⁶ but with fewer free parameters and fewer ghosts.
If it fails, that demonstrates T⁶'s extra dimensions
are structurally necessary.


## Infrastructure

New scripts in `minimal-geometry/scripts/`.  May use
`lib/t6.py` for comparison; new solvers for T¹ and
Klein bottle will be standalone.

## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R19   | Shear-charge mechanism — the thing we're testing |
| R26   | T⁶ framework being questioned |
| R27   | Particle spectrum — baseline for comparison |
| R28   | Ghost modes — possibly an over-counting signal |
| R15   | α problem — may dissolve if geometry simplifies |
