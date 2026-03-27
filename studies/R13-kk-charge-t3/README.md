# R13. Charge from the Embedding  *(complete)*

How does a photon on a flat T³, embedded in 3+1D
as a torus, manifest as a charged particle?  The photon
propagates through flat space internally (mass, spin).  Its
fields project into 3D through the toroidal embedding,
producing apparent charge (WvM mechanism).  This study
computes the effective 4D charge from the embedding and
investigates what determines the embedding geometry.

## Motivation

### Two domains in R8

R8 computed mass and spin using the flat material space
(photon on a geodesic, path = λ_C), and charge using the
3D-embedded torus (Coulomb self-energy).

This was initially diagnosed as an inconsistency (R12), but
it is actually the correct physical picture: the photon
propagates through intrinsically flat material space (setting
mass and spin), while its fields project into 3+1D through
the toroidal embedding (producing apparent charge).  These
are two aspects of the same geometry — internal vs external.

The remaining question: R8 used the measured charge e as
input to determine the embedding size (R = r_e).  Can the
embedding be determined from geometry alone?

### Why KK

Kaluza-Klein theory is the standard framework for connecting
material-dimension physics to 4D observations.  A field on
M₄ × K (Minkowski × material space K) decomposes into a tower
of 4D modes.  Each mode has a mass (from its material-space
eigenvalue) and a coupling to other modes.  The zero-mode
produces the long-range 4D field (Coulomb potential).

What was disqualified (R1): KK *gravity* — the gravitational
coupling from material dimensions is ~10⁻²² × e at the
electron scale.  Gravity cannot determine the material geometry.

What was NOT disqualified: KK *electromagnetism* — the EM
field decomposition on a material space.  This is exactly how
charge should emerge from geometry.

### Why T³ (not a single sheet)

R14 Track 0 showed that topological linking of geodesics
requires at least 3 material dimensions.  Three linking planes
on T³ map naturally to three color charges.  The electron
uses 2 of 3 dimensions; hadrons use all 3.

### Exploratory framing

This study is a mapping expedition, not a pass/fail test.
Possible outcomes and what they mean:

1. **KK reproduces charge e from geometry** — framework
   validated; check if the geometry is constrained.
2. **KK gives charge but wrong magnitude** — the mechanism is
   right but we're missing physics (corrections, interactions).
   The parameter dependence still narrows the geometry search.
3. **KK gives no charge** — the KK projection doesn't capture
   the WvM mechanism.  Need a different way to connect
   material-space fields to 4D observables.

All three outcomes advance the project.  Even outcome 3 tells
us something important about what the correct framework is.

## The setup

### Spacetime

7D spacetime: M₄ × T³

    ds² = η_μν dx^μ dx^ν + δ_ab dy^a dy^b

where x^μ = (t, x, y, z) and y^a = (y¹, y², y³) are
coordinates on the flat T³ with periodicities L₁, L₂, L₃.

### The field

A massless scalar field Φ(x, y) on M₄ × T³, as a proxy
for the full EM field.  (Start scalar, promote to Maxwell
if the scalar result is promising.)

The 7D wave equation:

    □₇ Φ = (□₄ + Δ_T³) Φ = 0

where □₄ is the 4D d'Alembertian and Δ_T³ is the Laplacian
on T³.

### KK mode expansion

Expand in Fourier modes of T³:

    Φ(x, y) = Σ_{n₁,n₂,n₃} φ_{n}(x) × exp(2πi n_a y^a / L_a)

Each mode φ_n(x) satisfies a 4D equation:

    (□₄ - m_n²) φ_n = 0

with KK mass:

    m_n² = (2π)² Σ_a (n_a / L_a)²

The zero-mode (n = 0,0,0) is massless — it's the 4D photon
(or scalar analogue).

### The photon-on-geodesic

The "electron" is a specific field configuration on T³:
a photon propagating along a (1,2) geodesic in, say, the
(y¹, y²) subspace, with y³ trivial.

In KK language, this corresponds to a specific superposition
of modes — NOT a single mode, but a coherent combination
whose spatial profile matches the geodesic wave.

The key question: what is the coupling of this specific
configuration to the zero-mode?  That coupling determines the
effective 4D charge.

## Tracks

### Track 1: Mode spectrum and electron identity ✓

Set up the KK expansion on T³.  Identify the mode spectrum.
Determine whether the electron is a KK momentum mode or a
winding mode.

**Result:** The electron is a winding mode, not a KK momentum
mode (mass mismatch ~36,000×).  Standard KK charge formula
gives zero for winding modes.  Flat T³ alone gives zero
charge — which is expected, since charge is a projection
property of the embedding.  See findings F1–F8.

### Track 2: What determines the embedding? ✓

Analyze candidate mechanisms for what fixes the toroidal
embedding geometry (and hence α).

**Result:** Four candidates analyzed.  7D cross-terms
eliminated.  Gravitational curvature, KK gauge connection,
and topological quantization are complementary aspects of
the same question: what determines the embedding.  The α
problem = the embedding problem = (possibly) the hierarchy
problem.  See findings F9–F13.

### Track 3: Charge from the embedding ✓

Computed the monopole moment of a circularly polarized plane
wave on a flat material sheet, embedded on a torus.

**Result:** Q = 0, exactly, for any (p, q) with q ≥ 1.
The R8-multi-winding model (p = 68) breaks the WvM charge
mechanism.  WvM's charge requires commensurability: p = 1
tube winding matching the 1 cycle of circular polarization.
With p = 68, E oscillates 67 times relative to the surface
normal and the integral vanishes.

This is the critical finding of R13: moving from (1, 2) to
(68, 137) solved the Coulomb energy problem (R7) but broke
the charge mechanism.  The underlying tension is α ≈ 1/137.

### Track 4: not pursued

Track 4 was predicated on Track 3 producing a charge that
depends on the embedding parameters (R, a).  Since Track 3
gives zero charge, Track 4 as framed has no starting point.

The question of resolving the charge-vs-Coulomb-energy
tension is captured as Q34 in the INBOX for future work.

## Dependencies

- R8: electron solution curve, geometry parameters
- R12: internal vs external domain clarification
- R14 Track 0: T³ requirement (why not a single sheet)

## What we abstract

- **Geometry:** Flat T³ with circumferences L₁, L₂, L₃
- **Field:** Start with scalar, promote to EM if warranted
- **Configuration:** Photon on (1,2) geodesic in (y¹, y²) plane
- **Observable:** Effective 4D charge and self-energy

## References

- R8: [`R8-multi-winding/`](../R8-multi-winding/)
- R12: [`R12-self-consistent-fields/`](../R12-self-consistent-fields/)
- R14: [`R14-universal-geometry/`](../R14-universal-geometry/)
- Standard KK: Kaluza (1921), Klein (1926)
- KK on torus: any string theory compactification textbook
