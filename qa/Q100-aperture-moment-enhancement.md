# Q100: Can a cavity aperture increase the magnetic moment?

**Status:** Open — hypothesis (simulatable on grid)
**Related:**
  [Q53](Q53-anomalous-magnetic-moment.md) (g − 2, prior approaches),
  [Q77](Q77-alpha-as-impedance.md) (α as Ma-S impedance mismatch),
  [Q94](Q94-compton-window-and-dark-modes.md) (Compton window as resonant aperture),
  [Q96](Q96-force-carriers-in-mast.md) §4 (vacuum elasticity),
  R44 (single-sheet g − 2 ruled out — charge-mass separation is order 1),
  R45 (cross-sheet magnetic moments — in progress),
  R8 Track 3 (topological g = 2)

---


## 1. The problem

The electron's magnetic moment is slightly larger than the
topological prediction:

    g_measured = 2.00231930436256
    g_topology = 2.000000

The anomaly (g − 2)/2 ≈ α/(2π) ≈ 0.00116 is a 0.1%
enhancement.  In QED, this comes from the Schwinger vertex
correction — the electron emitting and reabsorbing a virtual
photon, which effectively enlarges its current loop.

R44 showed that the obvious MaSt mechanism (charge-mass
separation from shear) gives an order-1 correction with the
wrong sign.  It is the wrong approach entirely.

This file explores a different idea: the anomaly comes from
the cavity's coupling aperture.  A discontinuity in the
cavity wall can **increase** the effective magnetic moment
by allowing the mode's field to extend beyond the geometric
boundary.


## 2. The thought experiment

Start with concrete cavity physics:

- A toroidal waveguide or cavity, built from the grid lattice
- A standing EM wave resonating inside (the confined photon)
- The cavity wall is a perfect conductor — the field is
  completely confined

The magnetic dipole moment μ comes from the circulating
Poynting vector (energy flux going around the ring).
It points along the torus symmetry axis ẑ, with magnitude:

    μ = (circulating power) × (area of current loop) / c²

On a perfect cavity, μ is determined entirely by the mode's
energy and the geometric area of the torus ring.

Now introduce a discontinuity in the wall.


## 3. What a hole does (and why it's not enough)

A simple hole in the cavity wall leaks energy.  The mode's
Q factor drops.  If the hole is not in the path of the
fundamental (i.e., near a field node), the fundamental barely
notices while higher modes with field maxima at the hole
drain rapidly.  This is a mode filter — useful for the ghost
problem (§7) — but it **decreases** the moment by reducing
stored energy.

A hole alone cannot explain g > 2.  Something must give back
more moment than it costs.


## 4. Four hypotheses for moment enhancement

### Hypothesis A: Fringing field bulge

A hole doesn't just leak — it also lets the **E field bulge
outward** through the aperture (E is the field component
normal to the cavity wall).  The fringing E field extends
beyond the cavity wall, and together with the H field at
the slot edges, produces a Poynting vector that circulates
in the same sense as the internal mode.

The moment is (current) × (area).  The fringing field adds
area to the effective current loop:

    μ_eff = μ_bare + μ_fringe

The fringe contribution is additive because the external
field circulates in the same direction.  You lose a little
energy (reducing "current"), but you gain loop area.  If the
area gain wins, μ_eff > μ_bare.

The magnitude depends on how far the fringe extends.  Bethe's
small-aperture theory: power through a hole of radius *a*
scales as (a/λ)⁴.  But the field displacement (not power)
scales as (a/λ)² — weaker suppression.  If the effective
aperture size is set by α (the Ma-S coupling), the moment
enhancement could be of order α × (geometric factor).


### Hypothesis B: Shear-tilted current loop

The shear deformation that creates charge also tilts the
torus geometry — the rectangle becomes a parallelogram.
On a sheared surface, the photon's geodesic is tilted
relative to the principal axes.

A tilted current loop sweeps a different effective area
than an untilted one.  If the tilt increases the projected
area along the spin axis ẑ, the moment increases with no
change in circulating energy.

This would unify charge and the anomalous moment: both
arise from the same shear parameter.  The charge is the
E-field asymmetry from shear; the anomaly is the B-field
loop area change from shear.

Note: this is **not** the mechanism R44 tested.  R44
computed the moment from the oscillating charge distribution,
which is an order-1 effect.  Hypothesis B is about the
geometric loop area, which is a much smaller (order-α)
correction to the topology-derived g = 2.


### Hypothesis C: Evanescent penetration (soft wall)

Instead of a literal hole, the cavity wall has finite
impedance (Q77: α is the Ma-S impedance mismatch).  A
finite-impedance wall allows an evanescent tail — the
field doesn't terminate at the wall but penetrates a skin
depth into the exterior.

This penetration extends the effective current loop in
every direction, uniformly.  The effective torus is slightly
larger than the geometric torus:

    A_eff = A_geometric × (1 + δ/R)²

where δ is the skin depth and R the relevant torus radius.
If δ/R ~ α/(2π), the moment enhancement is:

    (g − 2)/2 ~ α/(2π)

which is the Schwinger result.

The physical picture is nearly identical to QED's vertex
correction: the electron's field extends slightly beyond
its "bare" radius due to vacuum fluctuations.  In the
cavity picture, the field extends beyond the wall due to
finite-impedance penetration.  Same enlargement of the
current loop, different language.


### Hypothesis D: Single slot on the unrolled sheet

This is the most concrete and most simulatable hypothesis.


#### Field orientation at the cavity wall

At a conducting cavity wall, the boundary conditions are:

- **E field** points **out from the surface** (normal
  component).  This induces surface charge and is the
  field that extends through any opening.
- **B field** runs **along the surface** (tangential
  component).  This drives surface currents.  B_normal = 0
  at a perfect conductor.

When you cut a slot, it is the **E field** that bulges
outward through the opening.  The B field (surface current)
is interrupted at the slot edges.


#### The slot geometry

Unroll the torus into a flat rectangle:

- Horizontal axis: θ₂ (ring direction)
- Vertical axis: θ₁ (tube direction)

The (1,2) fundamental is a standing wave with field
amplitude ~ cos(θ₁ + 2θ₂).  It fills the entire sheet
as diagonal stripes of alternating field intensity:

```
  θ₁ (tube)
  ↑
  │╲    ╲    ╲
  │ ╲    ╲    ╲   ← fundamental field
  │  ╲  ┃ ╲    ╲       (diagonal stripes)
  │   ╲ ┃  ╲    ╲
  │    ╲┃   ╲    ╲
  └─────╂──────────→ θ₂ (ring)
        ┃
    single vertical slot
```

The slot is a single narrow cut running in the θ₁
direction (tube direction), at one θ₂ position.  On the
3D torus, this is a cut around the tube cross-section at
one point along the ring — like slicing through the donut
wall perpendicular to the ring, at one spot.


#### Why the fundamental leaks through it

The fundamental is spread across the entire sheet.  Its
amplitude varies as cos(θ₁ + 2θ₂), so along the slot
(at fixed θ₂) the field varies sinusoidally in θ₁.  The
field is NOT zero everywhere along the slot — it passes
through regions of both strong and weak intensity.

The slot height (extent in the θ₁ direction) controls how
much fundamental field it captures.  A slot spanning the
full tube height intercepts a complete sinusoidal cycle.
A shorter slot intercepts a fraction.

The E field at the slot location bulges outward through the
opening.  The Poynting vector (S = E × H, which circulates
in the ring direction) arches outward at the slot — the
effective current loop extends slightly beyond the cavity
wall at that point.


#### How the slot increases the moment

The magnetic moment is μ = I × A_eff.  At the slot, the
current loop bulges outward by a small amount.  The
effective area increases:

    A_eff = A_geometric + δA_fringe

The energy loss from the slot is small if the slot is
narrow: power leakage scales as (w/λ)⁴ where w is the
slot width (Bethe).  But the field extension (which sets
the area gain) scales as (w/λ)² — it dominates at small
aperture size.

For a narrow enough slot, **the area gain outweighs the
energy loss**.  The net moment increases.


#### The slot also filters ghosts

Different modes have different field patterns on the sheet.
A mode with winding numbers (n₁, n₂) has amplitude
~ cos(n₁θ₁ + n₂θ₂).  At the slot's θ₂ position, different
modes present different field intensities.

- The (1,2) fundamental: moderate field at most locations
  → small leakage → small moment enhancement
- A ghost mode with an antinode at the slot: strong field
  → heavy leakage → the mode drains away
- A ghost mode with a node at the slot: no field → no
  leakage → but also no coupling to S (invisible)

The slot simultaneously:
1. Enhances the fundamental's moment by a tiny amount
2. Selectively drains ghost modes whose field patterns
   expose them at the slot location

The **ratio** of fundamental enhancement to ghost drainage
depends on the slot geometry (height, width, position).
This is the tunability that could match α/(2π) for the
moment while producing the right Compton window selectivity
for mode filtering.


## 5. What these hypotheses have in common

All four predict:

1. The anomaly scales with α (the coupling strength through
   the boundary or aperture)
2. The anomaly is positive (moment INCREASES)
3. The geometric prefactor depends on the torus shape
   (aspect ratio r)
4. The mechanism is perturbative (order α, not order 1) —
   consistent with R44 F7's requirement

All four are physically distinct from what R44 tested.
R44 computed the moment from the shear-induced charge
distribution — an order-1 restructuring of the surface
current.  These hypotheses are about the cavity boundary's
effect on the spatial extent of the field.


## 6. Connection to QED

The QED vertex correction (Schwinger's α/(2π)) has a
standard physical interpretation: the electron's charge
cloud is slightly more spread out than the Dirac prediction
due to virtual photon emission/reabsorption.  This larger
effective radius gives a larger current loop and thus
a larger moment.

In the cavity picture:

| QED concept | Cavity analog |
|-------------|--------------|
| Virtual photon emission | Field leaking through aperture |
| Reabsorption | Fringing field re-entering cavity |
| Larger charge cloud | Current loop extended by fringing |
| α coupling | Aperture transmission coefficient |
| 1/(2π) prefactor | Geometric factor from torus shape |

The cavity aperture literally IS the physical mechanism
behind the "virtual photon loop."  The photon doesn't
leave and come back — its field extends continuously
through the aperture, enlarging the effective loop.


## 7. Mode filtering as a side effect

An aperture that enhances the fundamental's moment also
acts as a mode-selective filter:

- **Modes with field maxima at the aperture** lose energy
  through it.  If the aperture location is at a node of
  the fundamental but an antinode of a ghost mode, the
  ghost is preferentially drained.

- **Bethe scaling:** Power through a small aperture goes
  as (a/λ)⁴.  Higher harmonics (shorter λ) leak more
  efficiently.  The aperture is a **low-pass filter** —
  it preferentially kills high-frequency ghosts while
  barely affecting the fundamental.

- **Combined effect:** The fundamental gets a small moment
  boost (the anomaly) while ghosts get drained (the
  Compton window filtering, Q94).

This connects two apparently unrelated problems — the
anomalous moment and the ghost problem — through the same
physical mechanism: the cavity aperture.


## 8. What's needed

1. **Grid simulation (most direct test):**  Build a toroidal
   cavity on the grid lattice.  Excite the fundamental.
   Introduce a small aperture.  Measure the mode's
   effective magnetic moment (Poynting vector circulation ×
   effective area).  Compare with and without aperture.
   Vary aperture size, location, and shape.

2. **Analytical fringing field calculation:**  For a slot
   in a toroidal cavity wall, compute the fringing B field
   and its contribution to the ẑ-projected current loop
   area.  Compare the fractional enhancement to α/(2π).

3. **Skin depth on the Ma-S boundary:**  If hypothesis C
   is correct, the evanescent penetration depth δ must
   equal α/(2π) × R (torus radius) to reproduce the
   Schwinger result.  Is this consistent with Q77's
   impedance picture?

4. **Shear loop area (hypothesis B):**  Compute the
   projected area of the (1,2) geodesic current loop on a
   sheared torus as a function of shear s.  Does the area
   change at order s (which is order α)?

5. **Mode-dependent filtering:**  For each of the first
   ~20 modes, compute the field strength at the aperture
   location.  Predict which modes are enhanced, which are
   drained, and whether the surviving spectrum matches
   observation.
