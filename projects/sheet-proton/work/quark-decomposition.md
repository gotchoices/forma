# Quark substructure on a single track — first computational pass

**Status:** Work file. Records the first attempt to verify the
3-quarks-in-series reading of the per-arc charge integral on the
modulated-clover. **Mixed result:** the geometric arc-sequence
(lobe / saddle / lobe = uud for proton; saddle / lobe / saddle =
udd for neutron) holds by inspection, but the *simplest* track
integral (equal-θ-segment decomposition of Q_tube) does **not**
deliver per-quark fractional charges +2/3 and −1/3. The reading
needs a refined embodiment.

## The question

Per [`derived-clover.md`](derived-clover.md) §Quark substructure
and color and the README §Framing:

> A quark is one segment of the per-arc curvature integral along
> a closed (1/2, 1) track; convex (lobe) arcs at +2/3, concave
> (saddle) arcs at −1/3 under G1; the proton track (t₀ = −π/6)
> passes through lobe / saddle / lobe = uud (sum +1); the
> neutron track (t₀ = +π/6) passes through saddle / lobe /
> saddle = udd (sum 0).

The concrete check: split the existing `track_charge` integral
(over θ ∈ [0, 2π] with t(θ) = t₀ + θ/2) into 3 equal-θ
segments and verify the per-segment charges come out at
(+2/3, −1/3, +2/3) for the proton and (−1/3, +2/3, −1/3) for
the neutron.

## Method

Added `track_charge_segments(...)` to `scripts/modulated_clover.py`
(splits the existing dchi_dt integration into n_seg equal-θ
sub-intervals) and `run_step8(...)` (runs it on the Z₂ × Z₃-
symmetric Step-7 solution and reports). Ran also at n_seg = 6
(half-arc resolution) and on the unmodulated and cos-only-modulated
substrates for comparison.

Run:
```
python scripts/modulated_clover.py --step 8
```

## Results

### n_seg = 3 (one segment per arc)

| Particle | Track integration       | Segment 1 | Segment 2 | Segment 3 | Sum |
| -------- | ----------------------- | --------- | --------- | --------- | --- |
| Proton   | full symmetric Step-7   | +0.33333  | +0.33333  | +0.33333  | +1  |
| Proton   | unmodulated (a₁=b₁=0)   | +0.16667  | +0.16667  | +0.16667  | +½  |
| Proton   | cos-only (a₁ ≠ 0, b₁=0) | +0.21229  | +0.21229  | +0.21229  | ≈⅔  |
| Neutron  | full symmetric Step-7   |  0        |  0        |  0        |  0  |
| Neutron  | unmodulated             | +0.16667  | +0.16667  | +0.16667  | +½  |
| Neutron  | cos-only                | +0.21229  | +0.21229  | +0.21229  | ≈⅔  |

The Z₃ screw symmetry of the symmetric subspace **forces** the
three equal-θ segments to integrate identically. So:

- Proton segments equal +1/3 each (not +2/3, −1/3, +2/3).
- Neutron segments equal 0 each (not −1/3, +2/3, −1/3).
- The geometric distinction (proton lobe-saddle-lobe vs neutron
  saddle-lobe-saddle) does **not** translate into per-segment
  charge differences in this integral.

### n_seg = 6 (half-arc resolution)

| Particle | full symmetric Step-7 segments                                            |
| -------- | ------------------------------------------------------------------------- |
| Proton   | (+0.04062, +0.29271, +0.04062, +0.29271, +0.04062, +0.29271)             |
| Neutron  | (+0.24279, −0.24279, +0.24279, −0.24279, +0.24279, −0.24279)             |
| Both unmodulated | all six = +0.08333 = +1/12                                        |

The 6-segment pattern alternates *within* each arc (first half of
an arc gives one value, second half gives the other), **not**
*between* lobes and saddles. Pairing adjacent halves recovers the
n_seg = 3 result: each *arc* contributes 1/3 (proton) or 0 (neutron)
to the track integral, regardless of whether it is a lobe or saddle.

## Why the simplest reading fails

The (1/2, 1) track integration sweeps t and θ together — at each
θ, the track is at a *single* (t, θ) point, not along an arc at
fixed θ. The per-arc charge "+2/3 vs −1/3" comes from the
cross-section tangent winding *at fixed θ* — an integral over the
arc's t-range with θ held still. The (1/2, 1) track does not do
this integration; it traces a one-dimensional curve and integrates
the *parametric* tangent rate ∂_t χ along it.

Geometrically the proton track does pass through 2 lobes + 1
saddle and the neutron through 1 lobe + 2 saddles. The
*structure* of the arc-sequence is right. But the per-arc
*contribution to Q_tube* on the (1/2, 1) track is not what
distinguishes them — both arc-types contribute the same to the
track integral under the symmetric construction.

This is a structural fact about the (1/2, 1) integration, not a
numerical accident — the Z₃ screw symmetry of the symmetric
substrate forces it.

## Two reasonable repairs

**Repair A — quark charge is a cross-section integral, not a
track integral.** Identify each quark with one *arc* of the
cross-section the track passes through. The per-quark fractional
charge is the per-arc winding of the cross-section tangent at a
representative θ inside that arc's region — i.e. an integral over
the *cross-section curve* (at fixed θ), not the (1/2, 1) track.
On the unmodulated N = 3 clover the cross-section per-arc
winding is exactly +2/3 (lobe) and −1/3 (saddle); under modulation
these become θ-dependent. The track integral Q_tube = +1 (proton)
or 0 (neutron) is a *consistency check* on the full sum, not the
per-quark observable.

Pros: clean physical interpretation; matches the standard
fractional-charge reading of [`per-arc-curvature-as-charge.md`](../../metric-charge/work/per-arc-curvature-as-charge.md);
recovers the user's geometric picture.
Cons: per-quark charges are now θ-dependent under modulation;
need to define a canonical θ (mid-arc?) or average over θ for
each quark.

**Repair B — quarks are Z₃-irrep components of the wave-quantum.**
Decompose the wavefunction (or the integrand of the track
integral) into the three irreducible representations of the
Z₃ screw. Each irrep component is one quark; per-quark charges
are integrals of the irrep components against the per-arc
curvature. Under this reading the irrep components naturally
weight lobes and saddles differently because the irrep basis
phase-rotates around the cross-section.

Pros: representation-theoretic structure is rigorous; color
identification is automatic (irrep = color).
Cons: less geometric; requires the wavefunction explicitly,
not just the track parameterisation.

Both repairs preserve the user's framing in spirit — single
wave-quantum, three-quark substructure, color = phase-track
index — while refining the mathematical embodiment.

## What to do next

Before Chapter 5 prose, pick one of the repairs and verify it.
Repair A is the simpler test (compute the cross-section per-arc
winding at each θ along the track for the symmetric Step-7
solution; confirm the per-arc values are close to +2/3 / −1/3
and that the arc-sequence sums correctly). Repair B is more
machinery but more rigorous; it would be the natural follow-on
if Repair A turns out to have its own modulation-distortion
problem.

## Follow-up: Wannier-function construction

Both Repair A and a fuller "9 wave functions, 3×3 quarks × colors"
picture were pursued in [quark-wannier-decomposition.md](quark-wannier-decomposition.md).
Result: the Wannier construction passes structurally (3 localised
wave packets per track, sitting on the correct arc-sequence), but
neither the modulated nor the unmodulated Fourier cross-section
delivers per-arc charges close to ±2/3 / ∓1/3. The values
+2/3 / −1/3 are derived for *piecewise-circular* clover arcs
(constant κ = ±1/r over 240° / 120° arcs), not for the smooth
Fourier representation our scripts actually compute. See the
Wannier file for the three Chapter-5 readings this leaves open.

## Reproducibility

```
python scripts/modulated_clover.py --step 8
```
Outputs `outputs/modulated_clover_per_segment.txt`.
