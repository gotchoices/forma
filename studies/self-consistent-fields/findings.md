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


## Next steps

1. **Track 2 (revised): Propagating wave on curved torus.**
   Solve Maxwell's equations for a wave propagating along
   the (1,2) geodesic on the curved torus.  Track how the
   transverse profile evolves orbit-by-orbit.  Determine
   which geometries (r values) allow the profile to return
   to itself after q orbits.

2. **Track 3: Transverse mode structure.**  On the curved
   torus, the (1 + r cos θ) factor creates an effective
   waveguide.  Compute the transverse modes of this
   waveguide and determine whether they constrain the
   allowed aspect ratios.


## Scripts

- [`scripts/track1_spectral_structure.py`](scripts/track1_spectral_structure.py)
  — Spectral analysis: gap, mode search, geodesic mode,
  shear sweep, phase coherence
