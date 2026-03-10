# R7. Charge from Torus Geometry — Findings

## F1. Setup

We modeled the electron as a circularly polarized photon on a
(1,2) geodesic of a torus with major radius R and minor radius a.
The synchronized circular polarization mechanism (see
[`ref/charge-from-energy.md`](../../ref/charge-from-energy.md) §2)
produces E always pointing outward along the local surface normal.

We distributed total charge Q = e uniformly along the geodesic
path (a line source on the torus knot) and computed the
resulting 3D Coulomb field by summing contributions from all
path segments.  The total E-field energy was computed by
numerical integration of ½ε₀E² over a 3D cylindrical grid.

The path constraint fixes the geometry for each aspect ratio:

    R(r) = λ_C / (2π√(4 + r²))
    a(r) = r × R(r)

We swept r from 0.5 to 10, looking for the value where the
computed field energy U_E equals m_e c²/2 (half the rest mass).


## F2. Result

The computed field energy is roughly **1–2% of the target** for
all aspect ratios tested.  There is no crossing — no geometry
in the range r ∈ [0.5, 10] produces U_E = m_e c²/2 with Q = e.

| r | R (m) | a (m) | U_E (J) | U_E / U_target |
|---|-------|-------|---------|----------------|
| 0.50 | 1.87 × 10⁻¹³ | 9.37 × 10⁻¹⁴ | 7.38 × 10⁻¹⁶ | 0.018 |
| 1.00 | 1.73 × 10⁻¹³ | 1.73 × 10⁻¹³ | 6.45 × 10⁻¹⁶ | 0.016 |
| 2.00 | 1.37 × 10⁻¹³ | 2.73 × 10⁻¹³ | 6.29 × 10⁻¹⁶ | 0.015 |
| 3.00 | 1.07 × 10⁻¹³ | 3.21 × 10⁻¹³ | 4.57 × 10⁻¹⁶ | 0.011 |
| 4.29 | 8.16 × 10⁻¹⁴ | 3.50 × 10⁻¹³ | 5.00 × 10⁻¹⁶ | 0.012 |
| 6.60 | 5.60 × 10⁻¹⁴ | 3.70 × 10⁻¹³ | 4.41 × 10⁻¹⁶ | 0.011 |
| 10.0 | 3.79 × 10⁻¹⁴ | 3.79 × 10⁻¹³ | 4.37 × 10⁻¹⁶ | 0.011 |

The ratio U_E/U_target ≈ 0.01 is remarkably stable across a
20× range of aspect ratios.


## F3. An analytical cross-check

For a charge e distributed over a region of characteristic
size R, the Coulomb self-energy scales as:

    U_Coulomb ~ e² / (4πε₀ R)

At the Compton scale R ~ ℏ/(m_e c) = λ_C/(2π):

    U_Coulomb / (m_e c²) ~ e²/(4πε₀ ℏc) = α ≈ 1/137

So U_Coulomb ≈ α × m_e c², and:

    U_Coulomb / U_target = 2α ≈ 0.015

This matches the numerical results.  The 1–2% ratio is not a
numerical artifact — it is the expected Coulomb energy of
charge e at Compton wavelength scales.


## F4. Why the energy falls short

The computed energy is ~100× smaller than the target.  Several
explanations are possible; we list them without claiming to
know which (if any) is correct.

### Possibility A: The energy budget is different than assumed

Perhaps the photon's E-field energy (m_e c²/2) is NOT entirely
stored in the far-field Coulomb pattern.  Most of the energy
might remain in near-field modes confined to the compact surface
and its immediate vicinity, with only a fraction α leaking out
as the long-range 1/r² field.  In this picture:

| Component | Energy | Fraction |
|-----------|--------|----------|
| Near field (compact surface) | ~(1−2α) × m_e c²/2 | ~98.5% |
| Far field (Coulomb) | ~α × m_e c² | ~1.5% |

This would be consistent with α being the EM coupling constant:
it measures how strongly the compact-dimension fields couple to
the non-compact (3D) space.

### Possibility B: The synchronized CP picture is incomplete

We assumed E is constant and always outward (from synchronized
circular polarization).  If the actual field configuration is
different — for example, if the wave has multiple oscillations
per circuit (as the mode structure on flat T² suggests) — the
effective charge could be different.  The oscillation problem
(see README §"Open question: mode structure") remains unresolved
and could change the result.

### ~~Possibility C: The line-source model is too simple~~ ELIMINATED

Track B repeated the computation with Q = e distributed
uniformly over the torus SURFACE (not the geodesic path).
Results:

| r | Line U/U_target | Surface U/U_target |
|---|-----------------|-------------------|
| 0.50 | 0.018 | 0.012 |
| 1.00 | 0.016 | 0.008 |
| 4.29 | 0.012 | 0.007 |
| 6.60 | 0.011 | 0.008 |
| 10.0 | 0.011 | 0.010 |

Both methods give ~1% of target.  The surface method gives
slightly lower values (charge more spread out → less energy),
but both are in the same range and both match the analytical
prediction 2α ≈ 0.015.  The charge distribution model is not
the source of the shortfall.

### Possibility D: The torus dimensions are wrong

The path constraint ℓ = λ_C gives torus dimensions of order
10⁻¹³ m.  If the actual compact dimensions were much smaller
(closer to the classical electron radius r_e ≈ 2.8 × 10⁻¹⁵ m),
the Coulomb energy would be correspondingly larger.  This would
require abandoning the ℓ = λ_C resonance condition, which is
central to WvM.

### Possibility E: The charge mechanism is not Coulombic

Perhaps the "charge" of the electron does not arise from a
Coulomb-like 1/r² field at all, but from a topological or
KK-type mechanism (compact momentum, winding number).  In that
case, computing the Coulomb field energy is the wrong approach
entirely — the charge would be determined by the topology and
coupling constants, not by field energy.

### ~~Possibility F: We made a computational error~~ ELIMINATED

Two independent scripts (line source and surface charge) with
different discretizations, different source models, and
different code paths produce consistent results.  Both also
match the analytical estimate (F3).  A shared bug is unlikely.


## F5. What this tells us

Regardless of which explanation is correct, the result
establishes a clear fact:

**The Coulomb field energy of charge e at Compton wavelength
scale is approximately α × m_e c², not m_e c²/2.**

This means the WvM energy-balance argument — which equates all
of U_E with the energy of a Coulomb field matched at some
radius — overestimates the Coulomb energy by a factor of ~1/α.
S2 and R6, which refined the WvM approach with better geometry,
inherit the same overestimate.

The "magic ratios" from those studies (r ≈ 6.60 and r ≈ 4.29)
were artifacts of the energy-balance assumption.  The correct
relationship between charge, energy, and geometry is different
from what WvM assumed, and determining it remains open.


## F6. Implications for next steps

1. **The energy-balance approach to charge is closed.**  Further
   refinements of the WvM volume/matching method won't help —
   the fundamental assumption (U_E = Coulomb energy) is off by
   ~1/α.

2. **The charge mechanism needs rethinking.**  Whether it's
   topological (KK compact momentum), a near-field/far-field
   coupling, or something else, the connection between photon
   energy and observed charge is more subtle than WvM proposed.

3. **α appears naturally.**  The ratio U_Coulomb/(m_e c²) = α
   is not a coincidence — it IS the definition of α (the
   strength of EM coupling).  Any model that produces the
   electron must reproduce this relationship.  The question is
   whether the model can predict α or must take it as input.

4. **The q(r) curve is nearly flat.**  The Coulomb energy
   varies only weakly with aspect ratio (0.011 to 0.018 over
   r = 0.5 to 10).  This suggests the far-field charge is
   largely determined by the total charge and the overall scale
   (set by λ_C), not by the detailed shape.


## Scripts

- [`scripts/torus_charge.py`](scripts/torus_charge.py) — Track A:
  line source along (1,2) geodesic
- [`scripts/torus_surface_charge.py`](scripts/torus_surface_charge.py) —
  Track B: uniform surface charge on torus
