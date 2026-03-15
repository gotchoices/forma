# R14. Universal Geometry  *(draft)*

Can a single compact space host all known particles — electrons,
quarks, protons, neutrons — with particle identity determined
by topology (winding, linking) and energy (harmonics), not by
geometry?

**Track 0 result:** T² cannot support topological linking of
geodesics (2D surfaces lack the dimensionality).  **T³** (three
compact dimensions) can, and naturally maps three linking
planes to three color charges.  The proton mass fits as
3 × 612 × m_e to 0.008%.  See [`findings.md`](findings.md).

## Motivation

### The free parameter problem

R8 found a continuous family of electron geometries: every odd
q from ~100 to ~287 has a valid (r, R, a).  The aspect ratio
r = a/R is the sole remaining free parameter.  R11 and R12
exhaustively tested energy cost, primality, wave equations, and
geodesic structure — none constrain r.

### Why shared geometry matters

Current approaches treat the electron in isolation.  But the
Standard Model has many particles — and in the WvM framework,
they're ALL photons on compact geometry.  If each particle type
has its own T², the free parameters multiply (r_electron,
r_up, r_down, ...).  If all particles share ONE T², the
constraint is massive: one (r, R, a) must simultaneously
produce the electron, up quark, down quark, proton, and
neutron with correct charges, spins, and masses.

This is the strongest potential constraint on r.

### The deeper principle (Q32)

Energy and geometry are the only fundamentals.  Mass, charge,
spin, and magnetic moment are all emergent:

- Mass = photon energy confined in periodic geometry
- Charge = field winding on T², projected into 3+1D
- Spin = winding ratio of geodesic
- Confinement = topology (linked paths can't separate)

If this is correct, the particle zoo is just the catalog of
distinct topological configurations of photons on a single
compact space.  The "Standard Model" becomes a theorem about
the topology of T².

## The hypothesis

**All particles are photon configurations on a single flat T³.**

(Originally proposed for T², revised to T³ after Track 0
showed that topological linking requires 3 compact dimensions.)

- **Electron:** One photon on a (1,2) geodesic in a 2D
  subspace of T³, fundamental mode (n = 1).  Third dimension
  inert.  Charge e from the field's monopole projection.
- **Positron:** Same, opposite winding direction.  Charge −e.
- **Quarks:** Each quark is one photon in a three-photon
  linked state on T³.  Each photon winds in a different pair
  of dimensions (→ three "colors").  The linking constrains
  each photon's field to project as fractional charge.
- **Proton:** Three photons, topologically linked (Borromean
  or similar) on T³, with total charge +e and spin ½.
  Each photon at harmonic n ≈ 612, giving m_p ≈ 3 × 612 m_e.
- **Neutron:** Three photons, differently linked, total
  charge 0 and spin ½.  m_n ≈ 3 × 613 m_e.
- **Neutrino:** Unknown topology — possibly a geodesic with
  zero charge projection but nearly zero mass.

### How fractional charges could arise on T³

S3 showed that on T², only (1,2) gives nonzero charge (higher
knots cancel by symmetry), and different charges seem to
require different a/R.

But on T³, there are three dimensions for winding.  Three
photons winding in different dimensional planes have
fundamentally different field configurations than three
parallel photons on T².  Mechanisms for fractional charge:

1. **Different winding planes:** A photon winding in the (1,2)
   plane has a different field projection into 3+1D than one
   winding in the (2,3) plane.  The charge depends on WHICH
   dimensions the photon winds around, not just the a/R ratio.

2. **Topological linking:** On T³, three geodesics in different
   planes are genuinely linked.  The linking constrains each
   photon's field, potentially forcing each to project as
   fractional charge even though a free photon would give
   integer charge.

3. **Winding number fractionalization:** In condensed matter
   physics, topological linking fractionalizes quantum numbers
   (fractional quantum Hall effect, anyons).  The same
   mechanism on T³ could produce fractional charges from
   integer-winding photons.

### How mass works on a shared geometry

On a fixed T³, the allowed path lengths are:

    ℓ_n = ℓ_fundamental / n     (harmonics)

giving masses:

    m_n = n × m_fundamental = n × h/(ℓ c)

The electron (lightest charged lepton) would be n = 1.
Higher harmonics give heavier particles with the same quantum
numbers — candidates for muon (n = 207?) and tau (n = 3477?).

For quarks in a three-photon state, each photon has its own
energy.  The proton mass (938 MeV) split among three photons
gives ~313 MeV each.  As a harmonic:

    n_quark = m_quark / m_electron ≈ 313 / 0.511 ≈ 612

The total: 3 × 612 × m_e = 1836 m_e.  The measured m_p/m_e =
1836.15.  This is striking but may be coincidental — the
calculation assumes equal energy per photon, which is unlikely
for asymmetric quark masses (m_u ≠ m_d).

### What determines the absolute scale

The photon energy is an input — the model does not predict WHY
the electron has mass 0.511 MeV (Q16).  Given the energy E:

    Path length: ℓ = hc/E = λ_C
    Major radius: R = λ_C / (2πq√(1 + r²/4))

So the absolute size (R in meters) follows from the energy and
the shape (r).  The shape is what this study aims to determine.

If charge is emergent (not input), the charge constraint
R = 2g(r) r_e becomes a PREDICTION: compute the apparent
charge from the KK field projection, then verify it matches e.

## What shared geometry constrains

If electrons and hadrons share one T³, the geometry must
simultaneously satisfy:

1. **Electron:** single (1,2) photon at n = 1 gives charge e,
   spin ½, mass m_e
2. **Proton:** three linked photons give total charge +e
   (= 2/3 + 2/3 − 1/3), spin ½, mass 938 MeV
3. **Neutron:** three linked photons give total charge 0
   (= 2/3 − 1/3 − 1/3), spin ½, mass 940 MeV
4. **Quark confinement:** linked photons cannot be separated
   (topological, not dynamical)
5. **Deep inelastic scattering:** three distinct scattering
   centers within the proton

These are severe constraints on one (L₁, L₂, L₃) triple.
If they can be satisfied simultaneously, the geometry is
determined — and so is everything else.

## Planned approach

### Track 0: Feasibility check ✓

**Result:** T² cannot support linking (negative).  T³ can,
with three linking planes mapping to three color charges
(positive).  Proton mass = 3 × 612 × m_e to 0.008%
(suggestive).  See [`findings.md`](findings.md).

### Track 1: Multi-photon field on T³ (prerequisite: R13)

Extend R13's single-photon KK analysis to T³ and to two and
three photons.  Compute the total EM field of multiple linked
geodesics on flat T³, project into 3+1D, extract the
monopole charge.

Key question: does topological linking produce fractional
charges from integer-winding photons?

### Track 2: Linking topologies on T³

Classify the possible topological links of two and three
closed geodesics on T³.  Which configurations are Borromean
(no pair linked, but triple linked)?  Which give spin ½ for
the composite?

### Track 3: Proton mass from three-photon state

For each candidate linking from Track 2, compute the total
energy (including interaction energy between the photons'
fields).  Does the energy of the lowest three-photon linked
state match m_p c² on the same T² that gives the electron?

### Track 4: Consistency check

Does the geometry determined by Tracks 1–3 satisfy:
- R ≈ r_e (R8 electron constraint)
- α ≈ 1/137 (or bare α ≈ 1/128, see Q31)
- Correct neutron-proton mass difference (~1.3 MeV)
- Correct magnetic moments (μ_p, μ_n)

## Dependencies

- **R13 (prerequisite):** KK charge from flat T² — how one
  photon's field projects into 3+1D
- R8: electron solution curve (geometry_search.py)
- S3: fractional charge algebra (knot-zoo F3, F4)

## Key questions this study would answer

1. Can three photons linked on T² produce fractional charges?
2. Does requiring electron + proton on one T² fix r?
3. Is quark confinement automatic from the linking topology?
4. Does the proton-to-electron mass ratio emerge?

## Consequence: baryogenesis without antimatter

If all particles share one T², the only fundamental
conservation law involving "charge-like" quantities is total
winding number conservation (= total charge conservation).
"Baryon number" and "lepton number" are not fundamental —
they count topological configurations, not conserved charges.

A charge-neutral atom (e.g. hydrogen) has total winding = 0,
the same as the vacuum.  This means:

**Neutral atoms can form directly from photons.**

The reaction 4γ → H (three photons link into a proton, one
winds into an electron) conserves energy, momentum, and total
winding.  No antimatter is required.

This dissolves the baryogenesis puzzle: in the early universe
(T > 10¹² K), energetic photons could condense directly into
neutral matter.  The observed matter-antimatter "asymmetry" is
not an asymmetry — it's the natural outcome of photon
condensation into charge-neutral topological states.

**Testable prediction: proton decay.**  Since baryon number is
not fundamental, the proton's three-photon linked state can in
principle unlink.  The rate depends on the topological barrier
height — expected to be extremely suppressed but nonzero.
Current bound: τ_p > 10³⁴ years (Super-Kamiokande).

This prediction is shared by Grand Unified Theories but arises
from a completely different mechanism: topological unlinking
vs. gauge boson exchange.

## Relation to other questions

- Q12: multi-photon and color charge
- Q13: three compact dimensions (alternative to shared geometry)
- Q16: what sets the photon energy / mass spectrum
- Q26: multi-photon hadrons and knot confinement
- Q27: foundational axioms
- Q31: discrete T² / digital counter hypothesis
- Q32: energy and geometry as only fundamentals

## Risk assessment

**High risk, high reward.**

- The multi-photon field calculation is substantially harder
  than the single-photon case (R13).
- Topological linking on T² is well-studied mathematically
  (braid groups, mapping class groups) but connecting it to
  EM field projections is novel.
- If it works — even partially (e.g., fractional charges
  emerge from linking) — it would be a major result.
- If it fails, it would push toward Model A (separate T² per
  particle type), which has more free parameters but might
  still be tractable.
