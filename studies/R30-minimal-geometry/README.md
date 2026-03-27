# R30. Minimal compact geometry — is a material sheet necessary?

**Questions:** Q34 (what selects α), Q16 (mass spectrum)
**Type:** theoretical + compute  **Depends on:** R19, R26, R27
**Status:** Active


## Motivation

Each particle in the Ma (the six-dimensional material space) model lives on a material sheet — a
two-dimensional torus.  But the physics seems to inhabit a
**curve**, not a surface.  The electron is the (1,2)
geodesic: a one-dimensional closed path that happens to
wrap around a two-dimensional torus.  The full material sheet provides
the *context* for how the curve wraps, but the particle
itself occupies a 1D path.

This raises a fundamental question: **does the material-sheet structure
carry more dimensions than the physics requires?**

Several clues suggest it might:

1. **One-parameter families.**  Each material sheet has an aspect ratio
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

3. **Ghost modes.**  Ma predicts ~900 modes below
   2 GeV but nature shows ~40 particles.  The 20×
   over-prediction might reflect extra geometric structure
   that produces modes nature doesn't need.

4. **Photons are 1D.**  A photon is a transverse
   oscillation with one polarization degree of freedom.
   If a particle is "a photon on compact geometry," and
   the photon is intrinsically 1D, why does it need a
   2D space to live on?


## Core questions

1. **Can a single material dimension (T¹) reproduce any
   of the particle properties (mass, charge, spin)?**
   What specifically requires a second dimension?

2. **Is the charge mechanism irreducibly 2D?**  Charge
   in R19 comes from shear between tube and ring
   directions.  Is there a 1D analogue — charge from
   curvature, twist, or non-uniform metric?

3. **What is the minimum compact geometry that produces
   quantized charge?**  T¹ (circle), material sheet (torus),
   Klein bottle, Möbius strip, or something else?

4. **What happens when one material-sheet dimension shrinks to zero?**
   If the tube circumference L_tube → 0 (r → ∞), the material sheet
   degenerates toward T¹ (just the ring).  Does charge
   survive this limit?  Does it emerge gradually or
   vanish discontinuously?

5. **Can a non-orientable identification (Klein bottle)
   produce charge or spin effects that a torus cannot?**
   We have never investigated non-orientable material spaces.

6. **If the tube is itself further compactified** (a circle
   of circles — hierarchical compactification), does this
   effectively reduce a material sheet to T¹ at accessible energies,
   deferring the second dimension to a higher energy scale
   (possibly Planck)?

7. **Can a 1D space with non-uniform metric reproduce
   material-sheet-like mode structure?**  A circle with g(x) = f(x)
   has a Mathieu-like spectrum with band gaps and avoided
   crossings.  Could this mimic the material-sheet energy ladder?


## Context from prior studies

### What a material sheet currently provides

Each material sheet in the Ma model contributes:

- **Two length scales** (L_tube, L_ring) → mass + aspect ratio
- **Shear** (σ between directions) → charge (R19)
- **Two winding numbers** (n_tube, n_ring) → mode energy
- **Tube parity** (odd/even n_tube) → spin contribution

The charge formula Q = −n₁ + n₅ fundamentally needs two
independent winding numbers from different material
directions.  On T¹, there is only one winding number.

### What T¹ provides

A single material dimension (circle of circumference L):

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
  from T¹ (periodic) or a material sheet (doubly periodic)
- Adding boundary conditions to a 1D space does NOT add
  a dimension — it constrains solutions within the
  existing 1D space

### Aspect ratio constraints (from prior studies)

| Parameter | Constraint | Source |
|-----------|-----------|--------|
| r_e | > ~0.26 (R19-shear-charge lower bound) | R19 |
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
of the spin mechanism in the S3-knot-zoo study (the E-field
picks up a phase of π per traversal → spin ½ from two
circuits).  This metaphor was never formalized as a study
of material geometry with reversed identification.

A Klein bottle is formed by identifying opposite edges of
a rectangle with one pair reversed:

    Material sheet: (x, 0) ~ (x, L₂)  and  (0, y) ~ (L₁, y)
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
sees T¹; material-sheet effects appear only at high energies.  But
the electron IS a material-sheet effect (charge from winding) — so
this seems to require the tube at Compton scale.

Could there be a *third* level of compactification below
the tube?  A circle of circles of circles?  Each level
would add structure at a higher energy scale.  The tube
at Compton scale (~10⁻¹² m) is already far above the
Planck scale (~10⁻³⁵ m) — there is room for many levels.


## Approach — tracks

### Track 1 — T¹ electron: what works, what fails  **Answered by Tracks 4 & 6**

T¹ provides mass quantization (E_n = nℏc/L) and spin
(odd/even parity), but cannot produce charge (requires
shear between two directions — Track 4 F11) and cannot
produce neutral spin-½ particles (requires three
independent tube dimensions — Track 6 F2, F7).
T¹ is structurally insufficient; no dedicated computation
needed beyond what Tracks 4 and 6 already demonstrate.

### Track 2 — Non-uniform T¹: can complexity replace dimensions?

A circle with position-dependent metric g(x) has a mode
equation that produces non-trivially spaced energies
(Mathieu-like).  Explore:
- Can a specific g(x) reproduce the electron's material-sheet mode
  structure (mass ratios, spin)?
- Does the non-uniformity create an effective "second
  direction" that mimics shear?
- What is the minimal complexity of g(x) needed to
  get charge-like behavior?

### Track 3 — Klein bottle and non-orientable identifications  **Complete**

Replace the standard material-sheet identification with the Klein
bottle identification (one edge reversed).
**Result:** Non-orientable spaces are structurally
incompatible with the model.  The Klein bottle kills
both charge (Gauss's law requires orientation; KK gauge
field becomes Z₂ not U(1)) and spin-½ (all closed
geodesics have even tube winding).  The material sheet is the unique
compact, orientable, 2D surface with winding numbers.
Also analyzed: r-degeneracy as a curve in (r,s) space,
and elastic/dynamic geometry.  Findings F15–F20.

### Track 4 — The r → ∞ limit: material sheet degenerating to T¹  **Complete**

Take the existing material-sheet solver and examine the large-r limit.
**Result:** No phase transition at any r.  Charge works for
all r > 0.26.  The tube becomes energetically negligible
(0.003% at r=100) but remains topologically essential.
r is free because charge is integer-quantized — the α
formula self-adjusts s(r) to maintain α = 1/137 at every r.
Findings F9–F14.

### Track 5 — Minimum geometry for charge  **Answered by Tracks 4 & 6**

The combined findings from Tracks 4 and 6 answer this:
- T¹: NO — only one winding number, no shear (Track 4 F11)
- Material sheet: YES — shear between two directions produces charge
- T³ shared: FAILS — loses neutral spin-½ (Track 6 F2)
- Klein bottle: investigated in Track 3

**Conclusion:** A material sheet is the minimum geometry for quantized
charge.  Each sheet needs a tube (for charge/spin via
topology) and a ring (for the energy scale).  3 sheets
× 2 dimensions = 6 is structurally minimum (Track 6 F7).
Track 3 tests whether a non-orientable material-sheet variant works.


### Track 6 — Shared-dimension T³: electron and proton on a common surface  **Complete**

**Motivation:**  Ma_e (dims 1,2) and Ma_p
(dims 5,6) have no shared dimensions in Ma — they are
coupled only through the cross-shear σ_ep.  What if they
share a dimension, reducing Ma to T³ (plus the neutrino
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

with charge Q = −n_a + n_c (analogous to Ma's Q = −n₁ + n₅).

Circumferences:
    L_a ≈ 419 fm  (electron tube scale)
    L_b ≈ free    (shared dimension, any L_b > 772 fm)
    L_c ≈ 0.21 fm (proton ring scale)

The neutron is mode (1, ~499, 1) — it bridges the 1.293 MeV
mass gap using a high winding on the shared dimension.
Preliminary result: m_n − m_p = 1.291 MeV (0.002 MeV off!).

This is encouraging but raises questions:
- The neutron's n_b ≈ 499 is a high winding.  In Ma, the
  neutron has small quantum numbers on all dimensions.
  Is n_b = 499 physical or a sign that T³ needs shear?
- L_b is free — same r-degeneracy as a material sheet, just fewer copies.
- The neutrino scale is 10¹⁰× larger than L_a.  Sharing
  with the neutrino is almost certainly not viable.

**Computational plan:**
1. Build a T³ solver with metric, shear, and charge.
2. Pin L_a and L_c by electron and proton masses.
3. Sweep L_b and compute the full particle spectrum.
4. Check spin assignment from winding parities.
5. Compare ghost-mode count to Ma (fewer dimensions
   should mean fewer ghosts).
6. Test whether T³ with shear can reduce the neutron's
   n_b to a small value (as σ_ep does in Ma).
7. Assess whether the muon, pion, kaon, and other
   particles find modes in the T³ spectrum.

**Success criterion:**  T³ reproduces at least the core
particles (e, p, n, μ, π, K) with comparable accuracy
to Ma but with fewer free parameters and fewer ghosts.
If it fails, that demonstrates Ma's extra dimensions
are structurally necessary.


## Infrastructure

New scripts in `R30-minimal-geometry/scripts/`.  May use
`lib/ma.py` for comparison; new solvers for T¹ and
Klein bottle will be standalone.

## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R19   | Shear-charge mechanism — the thing we're testing |
| R26   | Ma framework being questioned |
| R27   | Particle spectrum — baseline for comparison |
| R28   | Ghost modes — possibly an over-counting signal |
| R15   | α problem — may dissolve if geometry simplifies |
