# Theory: Effective Geometry of the WvM Electron Model

## 1. Starting Point

The Williamson–van der Mark (WvM) model describes the electron as a
photon of wavelength λ_C confined to a double-loop geodesic on a torus
with transport radius R = λ_C/(4π). From this topology they derive:

| Property | Derivation type | Result |
|----------|----------------|--------|
| Spin | Topological (path length + double loop) | ½ℏ — exact |
| g-factor | Energy partition (rotating vs external) | 2(1 + α'/2π) — matches 1st-order QED |
| Charge | Geometric (field in cavity, Coulomb match) | 0.91e — approximate |

The critical observation: **spin and g-factor are topological** (they
depend on the path structure, not on how the field is distributed in
space), while **charge is geometric** (it depends on the confinement
volume and the comparison radius).

This study focuses exclusively on the charge — the model's weakest and
most geometry-dependent prediction.

---

## 2. WvM's Charge Derivation

WvM confine one photon's energy hc/λ in a spherical volume
V = (4/3)π(λ/2)³. The average energy density gives an E-field
magnitude, which is matched to the Coulomb field at the transport
radius r̄ = λ/(4π):

    q = 4πε₀ r̄² × √(hc / (ε₀ λ V))

With V = V_sphere this yields q = (1/2π)√(3ε₀ℏc) ≈ 0.91e.

The general relation q ∝ r_c²/√V means the charge depends on two
free geometric parameters:

- **V** — the volume containing the field
- **r_c** — the radius at which the field is compared to a Coulomb field

Neither is fixed by the topology. Both are acknowledged approximations
in WvM §3.

---

## 3. Why the Sphere Is Not Arbitrary

WvM's sphere of diameter λ is not a random guess — it corresponds to
the **rotation horizon**: the maximum distance from the torus center
at which a closed path of length λ can exist. Beyond r = λ/2, no path
can close in one wavelength, so no energy flow can circulate.

The photon orbits at R ≈ 0.08λ, but its electromagnetic field extends
outward. At distances ≫ R, the time-averaged field of a charge
circulating at speed c is nearly spherically symmetric — the toroidal
structure is smeared by ultra-relativistic circulation. This is the
same physics that makes the time-averaged potential of a classical
orbiting charge approach a point-charge field at large distances.

The sphere of diameter λ therefore represents the **effective
confinement volume**: the region where the photon's field has
non-negligible amplitude, bounded by the rotation horizon.

---

## 4. The Torus-to-Sphere Continuum

The "tube radius" a in the WvM model is not a hard wall — there is
no physical tube surface. It describes the spatial extent of the field
around the geodesic orbit. The charge prediction depends on this
effective extent:

### Ring torus (a < R)

The field is concentrated near the orbit. The region of significant
field strength is toroidal with a visible hole. The volume is small,
the energy density is high, and q ≫ e.

### Horn torus (a = R)

The field just reaches the symmetry axis. The hole closes. Still q ≫ e.

### Spindle / degenerate torus (a > R)

The field extends past the axis. As a geometric *surface*, the torus
self-intersects. As a *field distribution*, this is perfectly physical —
the field fills a blob that looks increasingly spherical. No blowup or
discontinuity occurs at a = R.

The geodesic orbit is unchanged (it depends on R, not a). In the
spindle regime, the orbit passes through the center of the blob, but
the photon still follows the same (2,1) double-loop path at radius R.

### Key a/R values (using uniform-field approximation, r_c = R)

| a/R  | Geometry           | Outer edge | q/e  |
|------|--------------------|------------|------|
| 0.50 | Thin ring          | 0.12 λ     | 13.2 |
| 1.00 | Horn (hole closes) | 0.16 λ     |  6.6 |
| 5.28 | Outer = horizon    | 0.50 λ     |  1.25|
| 6.60 | q = e exactly      | 0.61 λ     |  1.00|
| 7.26 | V = V_sphere (WvM) | 0.66 λ     |  0.91|

The charge sweeps smoothly from q ≫ e (tight torus) to q = 0.91e
(WvM sphere) as the field extent grows. At a/R ≈ 6.60, q = e
exactly — this is the "natural" geometry for the elementary charge.

---

## 5. Propositions to Test

### P1. Rotation Horizon Justification

WvM's sphere of diameter λ is the physically correct effective volume
because the rotation horizon at r = λ/2 is the natural boundary of
the self-confined photon's field. The charge at this volume (0.91e)
is the correct leading-order estimate.

### P2. Field Falloff Profile

The field of a photon propagating along the toroidal geodesic decays
with distance from the orbit. The decay profile determines the
effective volume. If the field fills the rotation horizon sphere
approximately uniformly, V_sphere is justified and q ≈ 0.91e.

### P3. Non-Uniform Distribution Correction

If the field is denser near the orbit and sparser near the horizon
edge, the effective charge is modified. The correction factor may be
close to e/q_WvM ≈ 1.099 (a ~10% effect), which would recover q = e
from the rotation-horizon picture.

### P4. Self-Consistency Condition

There may exist a self-consistency condition (e.g., the field at the
horizon boundary matches the external Coulomb field, or the energy
density vanishes at the boundary) that fixes the effective volume
uniquely and selects q = e.

---

## 6. Scope

### In scope

- Geometric sensitivity of the WvM charge formula
- Toroidal cavity EM modes (Maxwell's equations)
- The torus-to-sphere continuum and the degenerate torus
- Field falloff modeling from the geodesic orbit
- Self-consistency conditions for the effective volume

### Out of scope

- Series corrections (see `../S1-toroid-series/`)
- Mass spectrum (electron/muon/tau)
- Confinement mechanism
- Gravitational or cosmological implications
