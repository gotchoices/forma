# R12. Self-Consistent Fields on Sheared T² — Findings

## Track 1: Spectral structure of the flat sheared T²

### F1. The Compton frequency sits in a spectral gap

The lowest eigenmode of the flat sheared T² is ω_min = c/R
(the mode n=0, m=1).  The Compton frequency is ω_C = c/λ̄_C.
Their ratio:

    ω_C / ω_min = R / λ̄_C = 2g(r) × α

This is **exactly** 2gα, verified numerically to machine
precision across the full R8 solution curve:

| r    | g(r)   | q     | ω_C / ω_min |
|------|--------|-------|-------------|
| 0.10 | 0.688  | 100   | 0.01004     |
| 0.31 | 0.497  | 136   | 0.00725     |
| 0.50 | 0.414  | 161   | 0.00604     |
| 1.00 | 0.283  | 217   | 0.00413     |
| 2.00 | 0.184  | 263   | 0.00269     |

Since g ranges from ~0.2 to ~0.7, the ratio is always
of order α ≈ 1/137.  **The Compton frequency is ~137×
below the lowest torus eigenmode.**

This is not a coincidence — it follows algebraically from
the charge constraint R = 2g r_e and the identity
r_e = α λ̄_C.  It is another manifestation of the
α-tautology identified in R11.


### F2. No eigenmode exists at ω_C

**For n ≥ 1:** The n²/a² term in the mode frequency
ω(n,m) = c√(n²/a² + (m − n/(2q))²/R²) already exceeds
ω_C²/c² by itself.  The ratio (c/a)/ω_C = λ̄_C/a =
1/(2grα) ranges from 186 to 996 across the solution curve.
Any mode with n ≥ 1 has ω > 186 × ω_C.

**For n = 0:** ω(0,m) = c|m|/R.  Setting this equal to ω_C
requires m = R/λ̄_C = 2gα ≈ 0.007.  Not an integer.

**No eigenmode of the flat sheared T² has frequency ω_C,
for any geometry on the R8 solution curve, for any value
of the shear δ.**

This was verified by sweeping δ/L_θ from 0 to 0.1 at
fixed r = 0.31: the nearest mode to ω_C is always (0, ±1)
with ω = c/R ≈ 138 × ω_C.  The shear has no effect on
this gap.


### F3. The geodesic mode has very high frequency

The torus eigenmode indexed by the geodesic's lattice
winding numbers (n₀, m₀) = ((q−1)/2, q) has frequency:

    ω_geo ≈ cq√(R² + 4a²) / (2aR) ≈ q²ω_C/2

At q = 137: ω_geo ≈ 35,600 × ω_C.  This is a mode with
~35,000 wavelengths along the torus — not the Compton
oscillation.

Moreover, the wavevector of this mode is NOT aligned with
the geodesic direction.  At r = 0.31:

    Geodesic direction:  (0.153, 0.988) in (θ, φ) space
    Wavevector direction: (0.849, 0.529) in (θ, φ) space
    Angle between them:   49°

The mode (n₀, m₀) is a plane wave whose phase fronts are
oblique to the geodesic path.  It is not "a wave
propagating along the geodesic."


### F4. Phase coherence ≡ mass condition (no new information)

The self-interference condition — the photon must
accumulate exactly 2π of phase after one Compton
wavelength — gives:

    k × ℓ = 2π  →  k = 2π/λ_C  →  ω = ck = ω_C

This is algebraically identical to the mass condition
(path = λ_C).  The phase coherence requirement adds NO
constraint beyond what the mass condition already imposes.

Phase per orbit = 2π/q ≈ 2πα — a restatement of the
mass + charge constraints.


### F5. The shear is unconstrained by the flat-T² wave equation

Five independent checks confirm that the scalar Helmholtz
equation on the flat sheared T² provides no constraint on
the shear δ:

1. The mode spectrum depends on δ only through 1/(2q),
   a continuous parameter — no discrete selection
2. No mode exists at ω_C for any δ
3. Phase coherence = mass condition (no new constraint)
4. Shear sweep shows no spectral features at any δ
5. The geodesic mode's frequency and direction are
   unrelated to the Compton frequency


---

## Conceptual implications

### F6. The photon is NOT a torus eigenmode

The spectral gap (ω_C ≪ ω_min) means the "electron" cannot
be described as a standing wave on the T².  The Compton
frequency has no corresponding eigenmode.

**What the photon IS:**  A propagating electromagnetic wave
traveling along the geodesic at speed c.  Its wavelength
(λ_C) spans the ENTIRE path — all q orbits.  It wraps
around the torus ~137 times per wavelength.  The field is
not localized; it permeates the entire compact space.

This is the deep-wave regime (λ ≫ L), not geometric optics
(λ ≪ L).  The photon "fills" the torus.


### F7. The correct self-consistency question

Track 1 shows that "find eigenmodes at ω_C" is the wrong
formulation.  The right question is:

**Can a propagating EM wave at frequency ω_C, traveling
along the (1,2) geodesic at speed c, maintain a
self-consistent field configuration on the compact T²?**

This is a 1D propagation problem along the geodesic, not
a 2D eigenvalue problem on the T².  The field at each
point on the geodesic is determined by the EM boundary
conditions and the photon's own past history (it passes
each point every q orbits).

The self-consistency condition is: after q orbits, the
returning field must match the departing field — not just
in phase (which is the mass condition) but in amplitude,
polarization, and transverse profile.

This requires solving **Maxwell's equations for a
propagating wave on a curved torus**, where the
(1 + r cos θ) metric factor modulates the field on each
passage.  The transverse profile evolves as the wave
spirals around the torus; self-consistency demands it
return to its starting profile after q orbits.


### F8. Why curvature alone won't bridge the gap

The curved torus metric (1 + r cos θ) modifies mode
frequencies by factors of order r ≈ 0.3.  The spectral
gap is a factor of ~137.  Curvature cannot bring modes
down to ω_C.

However, curvature DOES matter for the propagation
problem (F7): it modulates the wave on each orbit,
potentially causing amplitude and polarization changes
that constrain the geometry.


---

## Summary

| Finding | Result |
|---------|--------|
| Spectral gap | ω_C / ω_min = 2gα ≈ α ≈ 1/137 |
| Modes at ω_C | None (for any geometry, any shear) |
| Geodesic mode | ω_geo ≈ q²ω_C/2, oblique to geodesic |
| Phase coherence | = mass condition (no new info) |
| Shear constraint | None from flat-T² wave equation |

**The scalar wave equation on the flat T² cannot constrain
the shear.**  The Compton frequency sits in a spectral
gap where no eigenmodes exist.

**Reformulation needed:** The self-consistency question
is not about eigenmodes but about a propagating wave
maintaining its field profile over q orbits on the
curved torus.


---

## Track 2: Geodesics on the curved torus

### F9. The flat-torus geodesic is incompatible with the curved torus

On a surface of revolution, geodesics obey Clairaut's
relation: L = (R + a cos θ)² dφ/ds = const.  For the
geodesic to wrap around the minor circle (required for
spin ½), L must satisfy L < R − a.

The flat-torus (1,2) geodesic has angular momentum
L_flat = 2R²/√(a² + 4R²).  For all r > 0.05:

    L_flat > R − a

The flat-torus angular momentum EXCEEDS the wrapping
limit on the curved torus.  A geodesic with L = L_flat
would oscillate in θ (staying on the outer half) instead
of wrapping around the minor circle.

| r    | L_flat/R | (R−a)/R | L_flat > R−a? |
|------|----------|---------|---------------|
| 0.10 | 0.999    | 0.90    | YES           |
| 0.31 | 0.988    | 0.69    | YES           |
| 0.50 | 0.970    | 0.50    | YES           |
| 1.00 | 0.894    | 0.00    | YES           |

This means the flat-torus (1,2) geodesic cannot be
directly mapped to the curved torus.  The curved-torus
geodesic achieving 1:2 winding has a qualitatively
different angular momentum (L* ≈ R − a).


### F10. The curved geodesic concentrates near the inner equator

On the curved torus, the 1:2 geodesic has L* ≈ R − a
(the wrapping limit).  This geodesic spends most of its
time near θ = π (inner equator), where the effective
circumference is 2π(R − a).

At r = 0.31: dφ/dθ ranges from 0.15 (outer equator) to
77 (inner equator), compared to the flat-torus constant
dφ/dθ = 2.  The geodesic whips around quickly in φ near
the inner equator and barely advances in φ near the outer
equator.


### F11. Path length is SHORTER — q increases

Because the geodesic hugs the inner equator (smaller
circumference), the path per θ revolution is shorter than
the flat prediction:

| r    | ℓ_curv/ℓ_flat | q_flat | q_curved |
|------|---------------|--------|----------|
| 0.10 | 0.439         | 100    | 227      |
| 0.31 | 0.706         | 136    | 193      |
| 0.50 | 0.665         | 161    | 242      |
| 1.00 | 0.447         | 217    | 484      |

Notably, q_curved has a **minimum near r ≈ 0.31** with
q_min ≈ 193.  This is the same r where the flat model
gives q ≈ 137.  For both smaller and larger r, q_curved
increases.


### F12. Holonomy is zero (no constraint from polarization)

For a simple closed geodesic on a torus, Gauss-Bonnet
gives holonomy = 2πχ(enclosed region) = 0 (the enclosed
annular region has Euler characteristic 0).  Verified
numerically: total ∫K dA = 0 to machine precision.

The EM polarization automatically returns to its initial
orientation after any number of orbits.  No constraint
on the geometry from parallel transport.


### F13. The curved correction does not constrain r

The path-length correction shifts the q(r) curve but
does not introduce a discontinuity, selection rule, or
preferred value of r.  The free parameter r survives.

However, the QUALITATIVE finding that q_curved has a
minimum near r ≈ 0.31 is noteworthy: this is where the
flat and curved models agree most closely, and it
corresponds to the thinnest-practical torus geometry.


---

## Conceptual implications (Tracks 1 + 2)

### F14. The compact space is intrinsically flat; the embedding is physical

If the photon experienced the intrinsic curvature of a
3D-embedded torus (Gaussian curvature K = cos θ/(a(R+a cos θ))),
the (1,2) geodesic would concentrate near the inner equator,
giving q ≈ 193 instead of ~137.  This does NOT match α.

Since the model requires q ~ 1/α ≈ 137, the photon must
propagate through intrinsically flat space — a flat quotient
space R²/Λ with straight-line geodesics and periodic
boundaries.  This determines mass and spin correctly.

However, the compact space IS embedded in 3+1D with a
toroidal geometry.  The embedding is not "just a
visualization" — it is physical.  It determines how the
photon's fields project into 3D, which determines the
apparent charge (via WvM's polarization-rotation mechanism).

The correct picture has two domains:

| Domain      | Geometry          | Determines        |
|-------------|-------------------|--------------------|
| Internal    | Flat (Cartesian)  | Mass, spin         |
| External    | Embedded (toroidal)| Charge, mag. moment|

These are not inconsistent — they are two aspects of the
same physical object.  The photon propagates through flat
space internally, but its fields, when they leak into 3D,
encounter the embedding geometry.  The charge is an
external (projection) property, not an internal one.


### F15. The shear question remains open

Neither the wave equation (Track 1) nor geodesic structure
(Track 2) of the torus (flat or curved) constrains the
shear δ.  The free parameter r survives both analyses.

Five approaches have now been exhausted:
1. Energy minimization (R11): monotonic, no minimum
2. Primality (R11): invisible to linear analysis
3. Eigenmode matching (Track 1): spectral gap, no modes at ω_C
4. Geodesic closure (Track 2): always achievable
5. Polarization holonomy (Track 2): identically zero on torus

The shear must be determined by physics NOT captured by
the 2D compact geometry alone.  Candidates:
- 3D field structure (how compact fields project into 3+1D)
- Quantum effects (e.g., Casimir energy of the compact space)
- The full 6D Einstein-Maxwell system
- An external input (the shear as a property of the vacuum)


## Study conclusion

R12 Tracks 1–2 are **COMPLETE**.  Both gave negative
results for constraining the shear from the 2D compact
geometry alone: no eigenmode exists at ω_C, and the
geodesic structure provides no selection mechanism.

**Key clarification (revised):** R8's charge calculation
uses the flat T² for mass/spin and the 3D embedding for
charge.  This was initially diagnosed as an inconsistency,
but the correct interpretation is that these are two
aspects of the same physical object:

- **Mass and spin** are internal properties, determined by
  the photon's propagation through flat compact space.
- **Charge** is an external property, determined by how the
  compact-space fields project into 3+1D via the toroidal
  embedding.

The photon doesn't "know about" the embedding, but its
fields, when they extend beyond the compact space, DO
encounter the embedding geometry.  R8's approach — flat
for propagation, embedded for charge — is the physically
correct procedure, not an inconsistency.

**On Track 3 (self-consistent propagation):** F7 asked
whether a propagating EM wave at ω_C could maintain its
field profile over q = 137 orbits, hoping this might
constrain the geometry.  However, F7 was written before the
two-domain clarification and assumed the wave would
experience the (1 + r cos θ) metric modulation of the
embedded torus on each passage.

Under the corrected premises, the photon propagates through
*flat* space.  On flat T²:
- A traveling wave experiences no curvature modulation
- Parallel transport preserves polarization exactly
- Amplitude and transverse profile do not evolve
- The only self-consistency condition is the phase condition
  (total phase = 2π after path = λ_C), which is the mass
  condition — already satisfied by construction (F4)

Track 3 is therefore **trivially satisfied** for any
geometry (any r, any δ).  No constraint on the free
parameter arises from propagation self-consistency in
flat space.

The non-trivial version of this question — where the wave's
own field energy influences the geometry it propagates
through — is a gravitational self-consistency problem.
That question belongs to R13 Track 4 (what determines the
embedding).

R12 is **COMPLETE**.


## Scripts

- [`scripts/track1_spectral_structure.py`](scripts/track1_spectral_structure.py)
  — Spectral analysis: gap, mode search, geodesic mode,
  shear sweep, phase coherence
- [`scripts/track2_curved_geodesics.py`](scripts/track2_curved_geodesics.py)
  — Curved torus geodesics: angular momentum, path length,
  holonomy, trajectory comparison
