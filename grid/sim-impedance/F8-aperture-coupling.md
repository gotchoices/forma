# Track 8 Findings: Aperture coupling

**Status:** Complete — partially positive, partially negative.

---

## F1. The n₁ = 1 charge selection rule is geometric

The CP field on the torus has E · ρ̂ = cos((n₁−1)θ₁) × ring_factor.

- **n₁ = 1:** tube factor = cos(0) = 1 → constant → nonzero integral
- **n₁ ≠ 1:** tube factor oscillates → integrates to zero (dominant term)

This is confirmed on the discrete hexagonal lattice.  The
selection rule is a consequence of **CP synchronization** with
the tube geometry: the E-field rotates at rate n₁ around the
tube while the cylindrical radial direction ρ̂ rotates at rate
1.  Only when n₁ = 1 are they synchronized, producing a
constant (non-oscillating) ρ̂ component.

| n₁ | Q (traveling, ε=0.3) | Interpretation |
|----|----------------------|----------------|
| 0  | 1.78 (∝ ε)          | Subdominant correction |
| 1  | **11.84**            | Dominant charge — synced with tube |
| 2  | 1.78 (∝ ε)          | Subdominant correction |
| 3  | ~0                   | Zero to leading and subleading order |
| 4  | ~0                   | Zero |

The n₂ dependence cancels entirely for traveling waves: Q is
the same for (1,1), (1,2), (1,3), (1,5).  Standing waves give
zero for all modes with n₂ ≠ 0.

**This matches R48 exactly and provides the discrete-lattice
confirmation of the charge selection rule.**

---

## F2. Instantaneous junction leakage integrates to zero

The junction scattering computation — projecting the CP field
onto each edge, then projecting each edge onto ρ̂, and
integrating — gives exactly zero for ALL modes, ALL lattice
sizes, and ALL aspect ratios.

**Why:** at any fixed instant, the field E · ρ̂ at each junction
has a phase that depends on θ₂ through cos(n₁θ₁ + n₂θ₂).  When
summed around the full ring (over θ₂), the oscillation
integrates to zero.  The leakage at each junction is real and
nonzero, but the leakages at different azimuthal positions
have different signs and cancel in the integral.

This is not a numerical artifact — it follows from the
**orthogonality** of cos(nθ₂) over [0, 2π] for n ≠ 0.  The
same orthogonality killed the standing-wave result in R48
Track 1.

---

## F3. Charge is a time-averaged property

The resolution between F1 (nonzero Q) and F2 (zero Q) lies in
the distinction between **instantaneous** and **time-averaged**
fields.

For a traveling wave e^{i(n₁θ₁ + n₂θ₂ − ωt)}:
- **Instantaneous field** at any fixed t: oscillates in θ₂ →
  integrates to zero
- **Time-averaged intensity** |E|² at each point: constant
  in θ₂ → integrates to nonzero value

Charge is a time-averaged property.  The instantaneous Gauss
flux oscillates (the "charge" appears to move around the ring
with the wave), but the time-averaged flux is constant and
gives net charge.

R48 captured this by using the **magnitude** of the traveling
wave (|e^{in₂θ₂}| = 1), which is the time-averaged envelope.
The junction scattering computation used the instantaneous
real part, which averages to zero.

**Implication:** the "aperture" at each junction is real, but
it produces charge only through time-averaged leakage of a
**circulating** wave.  A standing wave (which doesn't
circulate) has zero time-averaged leakage because the positive
and negative half-cycles cancel at each junction.

This is consistent with the established result: **charge
requires net circulation** (a traveling-wave component).

---

## F4. What the geometry determines vs what it doesn't

| Question | Answered by geometry? | Answer |
|----------|----------------------|--------|
| Which modes carry charge? | **Yes** | n₁ = 1 (CP synchronization with tube) |
| Does charge require circulation? | **Yes** | Traveling wave needed (standing → 0) |
| Is charge independent of n₂? | **Yes** | Q same for (1,1), (1,2), (1,3), ... |
| What is the VALUE of the charge? | **No** | Requires α (the 2D→3D coupling constant) |

The geometry of the torus + CP field determines the **selection
rules** for charge but not the **magnitude**.  The magnitude
involves α — how strongly the 2D surface field couples to the
3D ambient field.  This is the same conclusion as sim-impedance
Tracks 1–7: the geometry determines WHICH configurations couple,
but the coupling STRENGTH requires additional physics.

---

## F5. Comparison with the original hypothesis

The original hypothesis (T8 framing) proposed that bending a
flat hexagonal lattice into a torus would cause junction
leakage that converges to a value related to α.

**What was confirmed:**
- The E-field on edges does acquire a ρ̂ component on a curved
  surface (the tangent plane tilts relative to cylindrical
  radial)
- The n₁ = 1 selection rule emerges from CP synchronization
- The total turning angle is geometric (2π from Gauss-Bonnet)

**What was not confirmed:**
- The instantaneous junction leakage does not produce net charge
  (it oscillates and cancels around the ring)
- The time-averaged leakage reproduces the charge selection rule
  but does not yield a specific value related to α
- The coupling ratio Q/Q_abs does not converge to α or 1/α

**The "aperture" is real but the value of α remains undetermined
by the lattice geometry alone.**

---

## F6. What this teaches about the mechanism of charge

Despite the negative result for deriving α, Track 8 clarifies
the physical mechanism of charge in the GRID/MaSt picture:

1. **Charge is a projection effect.**  The 2D CP field is purely
   tangential (E · n̂_surface = 0), but it has a nonzero ρ̂
   component because the tangent plane is tilted relative to the
   cylindrical radial direction.  A 3D observer "sees" charge
   not because energy escapes the surface, but because the
   surface field has a component that projects outward.

2. **Charge requires both curvature and circulation.**  A flat
   sheet has no ρ̂ component (no tilt).  A curved sheet with a
   standing wave has oscillating ρ̂ components that cancel.  Only
   a curved sheet with a circulating (traveling) wave produces
   persistent, time-averaged outward projection → charge.

3. **The n₁ = 1 rule is geometric.**  The synchronization between
   the CP field's rotation rate (n₁) and the geometric rotation
   rate of ρ̂ (= 1) selects n₁ = 1 as the charged mode.  This
   is not a dynamical calculation — it's a kinematic matching
   condition.

4. **α enters through the coupling, not the selection.**  The
   geometry selects which modes are charged and which are neutral.
   The coupling strength α determines how much of the projected
   field actually manifests as 3D charge.  This remains the
   open problem.

---

## Files

| File | Contents |
|------|----------|
| [T8-aperture-coupling.md](T8-aperture-coupling.md) | Framing |
| [F8-aperture-coupling.md](F8-aperture-coupling.md) | This findings document |
| [scripts/track8_aperture_coupling.py](scripts/track8_aperture_coupling.py) | Computation script |
| [output/track8_Erho_distribution.png](output/track8_Erho_distribution.png) | E·ρ̂ field patterns |
| [output/track8_convergence.png](output/track8_convergence.png) | Convergence plots |
