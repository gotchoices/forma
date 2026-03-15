# R13. KK Charge from Flat T³

How does a photon on a flat compact T³ manifest as a charged
particle in 3+1D?  Compute the effective 4D charge using
Kaluza-Klein decomposition and map its dependence on the
compact geometry.

## Motivation

### The inconsistency in R8

R8 computed the electron's charge by placing a surface charge
on a 3D-embedded torus and integrating the Coulomb energy.
R12 showed this is internally inconsistent: the model uses
flat-T² physics for mass and spin (photon on a geodesic,
path = λ_C), but switches to the curved 3D embedding for
the charge calculation.

The photon experiences a flat compact space.  Its fields
should leak into 3+1D as projections of the compact-space
field configuration — not as though the photon "knows about"
the 3D torus shape.

### Why KK

Kaluza-Klein theory is the standard framework for connecting
compact-dimension physics to 4D observations.  A field on
M₄ × K (Minkowski × compact space K) decomposes into a tower
of 4D modes.  Each mode has a mass (from its compact-space
eigenvalue) and a coupling to other modes.  The zero-mode
produces the long-range 4D field (Coulomb potential).

What was disqualified (R1): KK *gravity* — the gravitational
coupling from compact dimensions is ~10⁻²² × e at the
electron scale.  Gravity cannot determine the compact geometry.

What was NOT disqualified: KK *electromagnetism* — the EM
field decomposition on a compact space.  This is exactly how
charge should emerge from geometry.

### Why T³ (not T²)

R14 Track 0 showed that topological linking of geodesics
requires at least 3 compact dimensions.  Three linking planes
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
   compact-space fields to 4D observables.

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

## Planned tracks

### Track 1: Mode spectrum and zero-mode coupling

Set up the KK expansion on T³.  Identify the mode spectrum.
Compute the coupling of the geodesic-mode to the zero-mode
(the 4D Coulomb potential).

Key deliverable: effective charge q_eff as a function of
(L₁, L₂, L₃) and winding numbers (p, q).

### Track 2: Self-energy from KK tower

The self-energy of the geodesic mode is the sum of its
couplings to all other modes.  In 4D, this appears as the
"Coulomb self-energy" of the particle.

Compute the self-energy as a function of the T³ geometry.
Compare to R8's result (U = m_e c²/2 at R ≈ r_e).

### Track 3: Parameter dependence

Map how q_eff and the self-energy depend on:
- The three circumferences L₁, L₂, L₃
- The winding numbers (p, q)
- Any shear parameters

Identify which combinations are constrained by requiring
q_eff = e and/or self-energy = m_e c²/2.

### Track 4: Consistency with electron model

Check whether the KK-derived charge reproduces the R8
solution curve.  If the KK result differs from R8's embedded-
torus Coulomb calculation, understand why and which is correct.

## Dependencies

- R8: electron solution curve, geometry parameters
- R12: inconsistency diagnosis (why KK is needed)
- R14 Track 0: T³ requirement (why not T²)

## What we abstract

- **Geometry:** Flat T³ with circumferences L₁, L₂, L₃
- **Field:** Start with scalar, promote to EM if warranted
- **Configuration:** Photon on (1,2) geodesic in (y¹, y²) plane
- **Observable:** Effective 4D charge and self-energy

## References

- R8: [`multi-winding/`](../multi-winding/)
- R12: [`self-consistent-fields/`](../self-consistent-fields/)
- R14: [`universal-geometry/`](../universal-geometry/)
- Standard KK: Kaluza (1921), Klein (1926)
- KK on torus: any string theory compactification textbook
