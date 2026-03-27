# R17. Radiation Pressure Self-Consistency — Findings


## Track 4: Centrifugal forces on the (1,2) helix

### F1. The forces are real, large, and harmonic-rich

The 3D curvature of the (1,2) helix varies strongly along
the path.  At the inner equator (closest to the ring center),
the curvature is tightest; at the outer equator, it is
gentlest.  For r = a/R = 0.5:

    κ_max / κ_min = 1.93  (curvature varies by nearly 2×)

The centrifugal force (F = p × v / ρ, where ρ is the local
radius of curvature) varies correspondingly.  The force has
three components:

| Component | Character | Dominant harmonic |
|-----------|-----------|-------------------|
| Radial (away from ring center) | Large DC + modulation | n = 0 (DC) |
| Vertical (z-direction) | Zero mean, oscillating | n = 1/2 |
| Azimuthal (along the ring) | Zero mean, oscillating | n = 1/2 |

All forces decompose into half-integer harmonics (n = 1/2,
1, 3/2, 2, ...) because the (1,2) path has period 4π in
the ring angle φ, not 2π.

The azimuthal force is the most interesting: it accelerates
and decelerates the photon around the ring.  At r = 0.5, its
amplitude is ~28% of the radial force.

| r = a/R | κ_max/κ_min | Azimuthal/Radial | n=1/2 (% of DC) |
|---------|-------------|------------------|-----------------|
| 0.25 | 1.43 | 13% | 6.8% |
| 0.50 | 1.93 | 29% | 17.7% |
| 1.00 | 4.04 | — | 57.1% |


### F2. Curvature harmonic series

The curvature κ(φ) along the path decomposes into a
characteristic series of half-integer harmonics.  For r = 0.5:

| Harmonic | Amplitude (% of DC) |
|----------|---------------------|
| DC | 100% |
| n = 1/2 | 31.9% |
| n = 1 | 3.3% |
| n = 3/2 | 5.7% |
| n = 2 | 3.4% |
| n = 5/2 | 1.6% |
| n = 3 | 0.7% |

The series falls off roughly geometrically.  The n = 1/2
fundamental (from the tube winding) dominates.  The
half-integer frequencies arise because the path closes
after TWO ring circuits (the spinor structure of the (1,2)
winding).


### F3. ALL static charge integrals give zero (negative result)

The charge integral for a cos(θ + 2φ) field on a symmetric
torus is exactly zero, regardless of:

| Modification | Q/e |
|-------------|-----|
| Perfect torus | ~10⁻²³ (numerical zero) |
| Deformed tube cross-section (ε = r/2) | ~10⁻²³ |
| Velocity-modulated field amplitude | ~10⁻²³ |
| Nonlinear metric coupling (1/(R+a cos θ)) | ~10⁻²³ |

The reason is fundamental: on a symmetric torus, the area
element (R + a cos θ) depends only on θ, not on φ.  The
charge integral factorizes:

    Q = [∫ f(θ) dθ] × [∫ cos(2φ) dφ]
                              ↑
                          always = 0

No θ-dependent modification (tube deformation, metric
coupling, velocity modulation) can produce a nonzero
φ-integral.  The azimuthal symmetry of the ring is an
exact protection.


### F4. The two-pass cancellation

The deeper reason F3 holds: the (1,2) winding visits every
ring position φ at two complementary tube positions:

    Pass 1: θ₁ = φ/2
    Pass 2: θ₂ = φ/2 + π

Any θ-dependent quantity (curvature, force, metric factor)
takes complementary values on the two passes:

    cos(θ₁) + cos(θ₂) = cos(φ/2) + cos(φ/2 + π) = 0

The two-pass cancellation is exact and holds for ALL
odd-order θ-dependent effects.  Even-order effects
(like cos²θ) produce a constant (n = 0) offset, not a
φ-dependent modulation.

This cancellation is a consequence of p = 1 (one tube
winding): the two passes are always diametrically opposite
on the tube.  For p ≠ 1, the passes would not be
diametrically opposite, and the cancellation would fail —
but p ≠ 1 also breaks the WvM charge mechanism (R13).


### F5. What the centrifugal mechanism CAN'T do

The centrifugal deformation of the tube cross-section
preserves the ring's rotational symmetry (φ-independence).
Therefore:

- It CANNOT produce a monopole (net charge) from a
  fully delocalized wave (σ = ∞).
- It CANNOT break the φ-symmetry of the torus.
- It CANNOT generate mode coupling from n = 2 to n = 0
  in the ring direction.

The original R17 chain of reasoning had a flawed step:

    tube deforms → "azimuthal symmetry broken" ← WRONG

The tube's circular symmetry (in θ) breaks, but the ring's
rotational symmetry (in φ) is preserved.  It is the
φ-symmetry that protects the zero charge, not the θ-symmetry.


### F6. What the centrifugal mechanism CAN do (open)

Although the static charge integral is zero, the centrifugal
forces could still determine σ (the localization width from
R15) through a DYNAMIC mechanism:

**The wavepacket compression/stretching effect.**

Consider a wavepacket of width σ traveling along the (1,2)
geodesic.  The centrifugal force has a GRADIENT across the
packet (because the curvature varies along the path).  This
gradient compresses the packet at some positions and stretches
it at others:

- Near the outer equator (θ ≈ 0): the force gradient is
  positive → the leading edge of the packet is decelerated
  relative to the trailing edge → COMPRESSION.
- Near the inner equator (θ ≈ π): the force gradient is
  negative → the leading edge is accelerated → STRETCHING.

Over one full circuit, the packet experiences alternating
compression and stretching.  If the compression and stretching
exactly cancel, there is no net effect.  But the centrifugal
force is nonlinear (F ∝ 1/ρ, where ρ = R + a cos θ), so
the compression at the inner equator (where ρ is small and
the curvature is strong) may be stronger than the stretching
at the outer equator (where ρ is large).

If there is a NET compression per circuit, the packet narrows
until the quantum pressure (uncertainty principle: narrower →
higher momentum spread → higher energy → spreading) balances
the centrifugal compression.  This equilibrium determines σ,
and hence α = exp(−4σ²).

This is Track 5 (see README).


## Track 5: Wavepacket evolution under centrifugal forces

### F7. F ⊥ v kills direct clumping (negative result)

The centrifugal force decomposes into three components on
the torus surface:

| Component | r = 0.25 | r = 0.50 |
|-----------|----------|----------|
| Normal to surface (into 3D) | 70% | 63% |
| Along the path (acceleration) | 0% | 0% |
| ⊥ to path on surface (deflection) | 72% | 77% |

(Percentages are of total RMS force; they add in quadrature.)

The along-path component is **exactly zero** because the
centrifugal force is always perpendicular to the velocity.
This is a geometric identity: F_centrifugal = −E × κ_vec,
and κ_vec ⊥ v̂ (curvature is always perpendicular to the
tangent).

This rigorously eliminates any direct acceleration or
deceleration of different parts of the wavepacket by the
centrifugal force.  The "clumping" idea — that the force
pushes energy volumes together or apart — fails because
the force cannot push along the direction of motion.

The force splits roughly equally between the normal direction
(which pushes the field into 3D) and the surface-perpendicular
direction (which would deflect the path).  The large surface-
perpendicular component (~72–77%) comes from the tube-winding
curvature: the helix curves around the tube (κ ~ 1/4a), and
this curvature lies on the torus surface.


### F8. Width breathing is exactly conservative (negative result)

The 3D wavepacket extent oscillates as the packet circulates
the helix.  The "breathing" occurs because the 3D arc length
per unit φ varies:

    S(φ) = ds_3D/dφ = √(a²/4 + (R + a cos φ/2)²)

The 3D width σ_3D(φ) = σ_φ × S(φ), where σ_φ is the angular
width in the flat sheet metric.

| Position | θ | σ_3D/σ_3D(outer), r=0.25 | r=0.50 |
|----------|---|--------------------------|--------|
| Outer equator | 0 | 1.00 | 1.00 |
| Top of tube | π/2 | 0.80 | 0.68 |
| Inner equator | π | 0.61 | 0.37 |
| Bottom of tube | 3π/2 | 0.80 | 0.68 |

The packet is 2.72× wider (in 3D) at the outer equator
than at the inner equator (for r = 0.5).  But the net
magnification per circuit is **exactly 1**:

    S(4π) / S(0) = 1.000000…

This is exact (not approximate) because S(φ) depends on
cos(φ/2), which has period 4π — the path period.  The
angular width σ_φ is a constant of the motion in the
flat-sheet metric.

The physical picture: the packet "breathes" (narrows and
widens in 3D) but returns to its original extent after each
circuit.  No energy is transferred between the width degree
of freedom and the propagation.  The compression and
stretching from the velocity gradient cancel exactly because
the velocity gradient is a conservative (Hamiltonian) effect.


### F9. Hypothetical deflection is enormous (context)

If the surface-perpendicular centrifugal force were applied
as an external perturbation (which it is NOT — see F10), the
path deflection would be enormous:

| Quantity | r = 0.25 | r = 0.50 |
|----------|----------|----------|
| ψ_max (angular deviation) | 2.29 rad (131°) | 2.68 rad (154°) |
| δ_max (3D displacement) | 16 tube radii | 8.1 tube radii |
| Δθ_max (tube-angle shift) | 15.9 rad (911°) | 7.9 rad (453°) |

The deflection is multiple full rotations around the tube.
It is dominated by the n = 1/2 harmonic (96–99%), meaning
the path would make one additional "wobble" per two ring
circuits.

The two passes would receive different Δθ values (asymmetry
of ~32 rad for r = 0.25, ~15 rad for r = 0.50), which would
break the two-pass cancellation (F4) — but this deflection
does not physically occur.


### F10. The centrifugal force is a consequence, not a cause (key insight)

The centrifugal force is the 3D INTERPRETATION of the photon's
confined motion.  It is not an external perturbation that can
modify the path.  The photon follows the flat-sheet geodesic
(θ = φ/2, a straight line on the unrolled rectangle), and the
3D curvature is what this straight-line motion LOOKS LIKE
from outside.

The enormous magnitude of the hypothetical deflection (F9)
confirms this: the centrifugal force and the confinement
force are the SAME force viewed from two frames.  The
centrifugal force equals the confinement force by
construction — they are Newton's third-law pair for the
material-sheet embedding.

Consequently:
- The force cannot cause clumping (F ⊥ v, F7)
- The force cannot cause net width change (σ_φ = const, F8)
- The force cannot deflect the path (it IS the path, F9)
- The force cannot determine σ at the classical level

To determine σ, we need a mechanism that creates a
σ-dependent potential in the flat-sheet dynamics.  The
centrifugal force, being σ-independent in the flat metric,
cannot provide this.  Possible mechanisms include:
- Self-interaction of the electromagnetic field (Coulomb +
  gradient energy, as in R15 F8)
- Quantum vacuum effects (Casimir-like)
- Radiation reaction from the accelerating charge

**This is a negative result for the centrifugal-force
mechanism as the σ-determining force**, but it clarifies
the physics and eliminates a plausible-sounding candidate.


## Summary

| Finding | Result |
|---------|--------|
| F1 | Centrifugal forces are real, large (~0.5 N), harmonic-rich |
| F2 | Curvature decomposes into half-integer harmonics; n = 1/2 dominates |
| F3 | Static charge integral = 0 for ALL θ-dependent modifications (exact) |
| F4 | Two-pass cancellation: p = 1 winding visits complementary θ values |
| F5 | Tube deformation cannot produce charge (preserves φ-symmetry) |
| F6 | Dynamic wavepacket compression could determine σ → Track 5 |
| F7 | F ⊥ v exactly: no direct clumping from centrifugal force (Track 5) |
| F8 | Width breathing is exactly conservative: σ_φ = const (Track 5) |
| F9 | Hypothetical deflection is enormous (~8–16 rad) but unphysical (Track 5) |
| F10 | Centrifugal force is a consequence of confinement, cannot determine σ (Track 5) |
