# Charge emergence: from bending to Coulomb field

**Status:** Established — mechanism proven (sim-impedance Tracks 8–12),
magnitude still requires α as input.

**Prerequisite:** [fields.md](fields.md) (E on edges, B at junctions),
[foundations.md](foundations.md) (GRID axioms), [maxwell.md](maxwell.md)
(continuum Maxwell from lattice)

---

## Summary

Electric charge is the visible signature of a 2D electromagnetic
wave on a curved surface.  When a flat hexagonal lattice is bent
into a torus, the Y-junctions distort — the three edges are no
longer coplanar in 3D.  A circulating wave on this bent surface
produces a persistent electric field component normal to the
surface, which a 3D observer measures as electric charge.

This document explains the mechanism at the junction level,
connecting GRID's axiom A3 (2π phase winding = charge) to the
physical geometry of a bent lattice.

---

## The mechanism in five steps

### Step 1: Flat sheet — invisible to 3D

On a flat hexagonal lattice, every Y-junction has three edges
at 120° in the plane.  All edge directions are coplanar.  The
electromagnetic field (E along edges, B at junctions — see
[fields.md](fields.md)) is entirely tangential to the sheet.

A 3D observer looking at this flat sheet sees no electric field
emanating from it.  The sheet is electromagnetically invisible.
No charge.

### Step 2: Bend the sheet — junctions distort

Roll the flat sheet into a torus (tube circumference 2πa, ring
circumference 2πR).  The edge lengths and junction angles are
approximately preserved (the torus is intrinsically flat), but
the edge DIRECTIONS in 3D change — neighboring edges now point
along slightly different tangent planes.

At each Y-junction, the three edges are no longer coplanar.
The deviation from coplanarity depends on the local curvature:
- Outer equator (θ₁ = 0): mild curvature, slight deviation
- Inner equator (θ₁ = π): strong curvature, large deviation
- Top/bottom (θ₁ = π/2): curvature changes sign, minimal deviation

On an equal-edge lattice (where 3D edge lengths are equalized),
the hexagons distort differently at each latitude:
- Inner equator: tall and skinny (compressed in ring direction)
- Outer equator: short and wide (stretched in ring direction)

### Step 3: Edge fields acquire normal components

The electromagnetic field rides on the edges.  On the flat sheet,
all edge fields are in-plane.  On the bent sheet, each edge
points partly out of the local tangent plane.  The field on that
edge therefore has a component normal to the surface: E_n.

This normal component is the "leakage" — the fraction of the
2D field that is visible to the 3D ambient space.  At each
junction, the leakage depends on:
- How far the edges deviate from coplanar (curvature)
- The amplitude and direction of the wave at that junction

### Step 4: Circulation selects persistent charge

A **standing wave** on the torus has E_n components that change
sign around the ring.  At θ₂ = 0 the leakage might be positive;
at θ₂ = π it's negative.  The integral over the full ring
cancels — zero net charge.  (This is the orthogonality of
cos(nθ₂) over [0, 2π] for n ≠ 0.)

A **traveling wave** (circulating around the ring) has a phase
that advances continuously.  Time-averaging over one period
removes the oscillation.  The surviving (DC) component depends
on whether the tube rotation of the E-field matches the tube
rotation of the surface normal.

**The selection rule:**  The CP field rotates at rate n₁ around
the tube.  The cylindrical radial direction ρ̂ rotates at rate 1.
Only when n₁ = 1 are they synchronized:

- n₁ = 1: E · ρ̂ = cos(0) = 1 → constant → **net charge**
- n₁ = 0: E · ρ̂ = cos(−θ₁) → oscillates → zero
- n₁ = 2: E · ρ̂ = cos(θ₁) → oscillates → zero

This is **CP synchronization** — the circularly polarized wave's
rotation rate matches the geometric rotation rate of the surface.
One full 2π circulation of the tube = one full unit of charge.

(Derivation: sim-impedance Track 8, F1.)

### Step 5: Charge is the accumulated leakage

Summing the persistent (time-averaged) normal field over the
entire torus surface gives the Gauss flux — the total electric
charge.  For an n₁ = 1 traveling wave:

> ∮ E_n dA ≠ 0 → net charge Q = ±e

The sign depends on the circulation direction (matter vs
antimatter).  The magnitude depends on α — how strongly the
normal component couples to the 3D field.  The quantization
(integer Q) follows from the 2π periodicity of the tube: only
complete windings produce non-canceling leakage.

---

## What this explains

| Question | Answer | Source |
|----------|--------|--------|
| Why does bending produce charge? | Non-coplanar junctions create normal E components | Track 8 |
| Why is charge quantized? | Only complete 2π windings avoid cancellation | Track 8 F1 |
| Why n₁ = 1 only? | CP synchronization with tube curvature | Track 8 F1 |
| Why do standing waves have zero charge? | Half-cycle cancellation at each junction | Track 8 F2 |
| Does charge require a specific lattice? | No — any 2D lattice on a curved surface leaks | Tracks 11-12 |
| Is the coupling bidirectional? | Yes — same α for leakage (charge) and absorption (photon capture) | Reciprocity |
| Where does α enter? | Sets the per-junction coupling strength (leakage magnitude) | Tracks 11-12 |

---

## Fractional (ephemeral) charge

A photon passing through a small section of bent lattice produces
a momentary E_n disturbance at each junction.  This is a transient,
sub-quantized "charge" that exists for the duration of the passage.
It does not persist because the traveling wave moves on and the
normal component at that junction reverses on the next half-cycle.

Only a sustained circulating wave (a standing mode on the torus)
accumulates the junction leakages into a persistent DC charge.
The quantization into units of e is a consequence of the 2π
periodicity, not of any threshold effect.

This means:
- A photon interacting with a curved surface briefly produces
  transient sub-e charge disturbances at each junction
- These disturbances are real (they produce momentary E_n)
  but cancel over time without sustained circulation
- Charge quantization is a resonance condition (2π periodicity),
  not a discreteness of the underlying field

---

## The reverse coupling (photon absorption)

The same junction geometry that leaks energy from 2D to 3D
(charge) also absorbs energy from 3D to 2D (photon capture).
By time-reversal symmetry (reciprocity):

> Forward: 2D mode → junction leakage → 3D Coulomb field (rate α)
> Reverse: 3D photon → junction absorption → 2D surface mode (rate α)

The coupling constant is the same in both directions.  This is
relevant for:
- Photon absorption by a charged particle (the reverse of charge
  emission)
- L05: coupling THz radiation into the neutrino torus
- Any interaction where 3D electromagnetic energy enters a
  compact 2D structure

---

## What remains unknown

The **magnitude** of the coupling — α itself — is not derived
from the bending mechanism.  The geometry determines:
- Which modes couple (n₁ = 1)
- Where coupling is strongest (high-curvature junctions)
- The pattern of coupling (d₁ harmonic = inner/outer asymmetry)
- That coupling is bidirectional

But the coupling STRENGTH (how many units of e per unit of
bending) requires α as input through the GRID lattice action.
The sim-impedance study (Tracks 1–12) systematically tested
every geometric approach and confirmed that α cannot be derived
from junction geometry alone.

The remaining approaches to deriving α are:
1. The lattice action cost of a topological defect (GRID A6)
2. A consistency condition linking ζ = 1/4 to α
3. Information-theoretic arguments about the minimum coupling
   needed for observation

See [sim-impedance/README.md](sim-impedance/README.md) for the
full history.

---

## References

- [sim-impedance/F8-aperture-coupling.md](sim-impedance/F8-aperture-coupling.md)
  — CP synchronization and charge selection rule
- [sim-impedance/F11-vector-energy-deficit.md](sim-impedance/F11-vector-energy-deficit.md)
  — Leakage fractions and scattering models
- [sim-impedance/F12-charge-per-radian.md](sim-impedance/F12-charge-per-radian.md)
  — Top-down charge distribution and equal-edge lattice
- [fields.md](fields.md) — E on edges, B at junctions
- [foundations.md](foundations.md) — GRID axioms
- [../../primers/charge-from-energy.md](../../primers/charge-from-energy.md)
  — Continuum derivation of charge from torus geometry (R48)
