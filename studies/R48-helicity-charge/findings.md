# R48 Findings: Helicity and charge on a torus

Study: [`README.md`](README.md)

---

## Track 1. Gauss flux integral for CP modes

Script: [`scripts/track1_gauss_flux.py`](scripts/track1_gauss_flux.py)

### Model

A circularly polarized standing wave on a torus with aspect
ratio ε = a/R.  Mode (n₁, n₂) has the normal component of
E given by:

> E · n̂ = E₀ cos(n₁θ₁ + n₂θ₂)

The Gauss flux integral is:

> Q = ∮ E · n̂ dA = ∫∫ cos(n₁θ₁ + n₂θ₂) × (1 + ε cos θ₁) dθ₁ dθ₂

### Findings

| ID | Finding |
|----|---------|
| F1 | **Q = 0 for ALL modes with n₂ ≠ 0.**  This is exact (analytic): the θ₂ integral of cos(n₁θ₁ + n₂θ₂) vanishes by orthogonality for any nonzero n₂.  The torus metric weighting (1 + ε cos θ₁) does not rescue it — it only affects the θ₁ integral, and the θ₂ integral kills the integrand first.  Verified numerically to machine precision (~10⁻¹⁶) across all tested modes and aspect ratios. |
| F2 | **Q ≠ 0 for modes with n₂ = 0 and n₁ ≠ 0.**  The (1,0) mode gives Q = επ × 4π = 4π²ε, scaling linearly with ε.  This is the only class of modes that produces charge under the naive CP model — but (n₁, 0) modes have no ring winding and don't correspond to any physical particle. |
| F3 | **The naive CP model does not produce charge for (1,2).**  This is the central negative result.  The standing-wave pattern cos(θ₁ + 2θ₂) has equal positive and negative regions that cancel exactly over the torus surface, regardless of the metric weighting.  The WvM "E always outward" picture does not emerge from a standing wave with phase cos(n₁θ₁ + n₂θ₂). |
| F4 | **Q104 cannot be answered by this method.**  The question "does helicity select (1,2) over (1,1)?" is moot when neither mode produces charge under the naive CP decomposition.  The Gauss integral approach does not discriminate between modes because it gives zero for all of them. |

### Interpretation

The naive model assumes E · n̂ = cos(phase), where the phase
is the standing-wave pattern on the surface.  This is a
scalar standing wave projected onto the surface normal.
It necessarily integrates to zero over any direction with
periodic boundary conditions.

The WvM charge mechanism is different.  WvM describes a
**traveling** (circulating) wave on the torus, not a standing
wave.  For a traveling CP wave going around the tube, the
E-field rotation is synchronized with the surface-normal
rotation at every instant — E · n̂ is constant, not
oscillating.  This produces constant outward flux and
nonzero charge.

The distinction:

| | Standing wave | Traveling wave |
|--|--------------|----------------|
| E · n̂ | cos(n₁θ₁ + n₂θ₂) — oscillates | E₀ — constant |
| Gauss integral | Zero (exact) | Nonzero |
| Physical picture | Drum head vibrating | Photon circulating |

A particle may be a **circulating** wave (energy flowing
around the geodesic) rather than a pure standing wave (energy
sloshing back and forth).  Or it may be a standing wave whose
charge comes from topology (GRID: 2π phase winding), not from
the field integral.

### Three possible resolutions

**Resolution A: Circulating wave.**  The WvM picture is
correct — the photon travels around the (1,2) geodesic as a
circulating wave, not a standing wave.  The CP
synchronization produces constant E · n̂ = E₀ for a traveling
wave.  A standing wave is the superposition of two
counter-circulating waves; charge is the net circulation
(clockwise minus counterclockwise).  If one direction
dominates (broken symmetry from shear chirality), the net
circulation produces charge.  This connects to §10 of
charge-from-energy: the shear embedding angle determines the
preferred circulation direction.

**Resolution B: Topology, not field integral.**  Charge comes
from the 2π phase winding (GRID axiom A3), not from the Gauss
integral of the field pattern.  The topological winding
produces charge regardless of the field distribution.  The
Gauss integral must be consistent with the topological charge
(it cannot be zero if the winding exists), which means the
actual field pattern is not cos(n₁θ₁ + n₂θ₂) — the topology
forces a more complex distribution with nonzero net flux.

**Resolution C: Both.**  Circulating waves carry the topology.
A traveling wave going once around the tube advances its phase
by 2π — that IS the topological winding.  The CP
synchronization (E always outward) is the field-level
manifestation of the winding.  Standing waves (equal
superposition of both directions) have zero net winding and
zero charge.  Charge requires net circulation = net winding
= broken symmetry between the two directions.

Resolution C is the most complete: it unifies WvM
(circulating CP wave), GRID (topological winding), and the
shear mechanism (broken circulation symmetry) into a single
picture.

### Status of Q104

Q104 asked: does helicity force n₂ = 2n₁?  This track
shows that the question cannot be answered by a standing-wave
Gauss integral — it gives zero for all modes.  The question
remains open but needs to be reformulated:

- If charge requires net circulation (Resolution A/C), then
  Q104 becomes: "does the circulating CP wave produce nonzero
  charge only for certain (n₁, n₂) combinations?"  This
  requires computing the Gauss integral for a TRAVELING wave,
  not a standing wave.

- If charge is topological (Resolution B), then Q104 becomes:
  "which modes can carry a 2π winding?"  This is a topological
  question, not a field-integral question.

A follow-up track could compute the Gauss integral for a
traveling (circulating) CP wave on the torus, which should
give nonzero Q for the circulating direction and test whether
the result depends on n₂.


## Track 2. Traveling-wave CP — corrected ρ̂ projection

Script: [`scripts/track2_traveling_wave.py`](scripts/track2_traveling_wave.py)

### Correction from Track 1

Track 1 computed E · n̂_surface (normal to the torus surface).
The WvM charge argument uses E · ρ̂ (cylindrical radial,
outward from the torus axis).  These are different: n̂_surface
rotates with θ₁ (it's the local surface normal), while ρ̂ is
fixed in the xy-plane at each θ₂.  The WvM synchronization
gives constant E · ρ̂, not constant E · n̂_surface.

### Model

For a CP wave synchronized with the tube geometry, the
E · ρ̂ component factorizes:

> E · ρ̂ = cos((n₁ − 1)θ₁) × ring_factor

The **tube factor** cos((n₁ − 1)θ₁) comes from the
interference between the CP rotation rate (n₁ per tube
circuit) and the geometric rotation rate (1 per tube circuit).
When n₁ = 1, these cancel and the tube factor is constant.

The **ring factor** depends on the wave type:
- Standing wave: cos(n₂θ₂) — oscillates, integrates to zero
- Traveling wave: |e^(in₂θ₂)| = 1 — constant magnitude

### Findings

| ID | Finding |
|----|---------|
| F1 | **The n₁ = ±1 selection rule is derived from CP synchronization.**  Only n₁ = 1 gives a non-oscillating tube factor: cos((1−1)θ₁) = 1.  For n₁ = 0, 2, 3, ..., the tube factor oscillates and integrates to zero.  This is the charge selection rule, emerging from the geometry of circular polarization on a torus — not postulated. |
| F2 | **The charge does NOT depend on n₂.**  For traveling (circulating) waves with n₁ = 1, the Gauss flux is identical for n₂ = 0, 1, 2, 3, 4, 5, 6 — all give Q = 4π² = 39.478 (in normalized units).  The ring winding number is invisible to the charge mechanism. |
| F3 | **Q104 is answered: NEGATIVE.**  Helicity does not force n₂ = 2n₁.  The CP synchronization selects n₁ = 1 (tube) but is completely blind to n₂ (ring).  Both (1,1) and (1,2) produce identical charge.  The (1,1) ghost is NOT eliminated by the polarization geometry. |
| F4 | **Standing waves carry zero charge.**  For any mode with n₂ ≠ 0, the standing-wave Gauss integral is exactly zero (confirmed analytically and numerically in Track 1).  Charge requires net circulation — a traveling-wave component. |
| F5 | **Charge = net circulation = topological winding.**  A traveling wave going once around the tube advances its phase by 2π.  This IS the GRID topological winding.  The CP synchronization (E · ρ̂ = constant) is the field-level manifestation.  Standing waves have zero net circulation, zero winding, zero charge.  A charged particle must have a circulation imbalance — more energy going one way than the other — which is provided by shear chirality (the embedding angle). |
| F6 | **The proton (3,6) question.**  For n₁ = 3, the tube factor is cos(2θ₁), which oscillates and integrates to zero.  In this model, (3,6) does NOT carry charge directly.  If the proton is (3,6), charge must come from a different mechanism — perhaps from the three (1,2) sub-strands, each of which individually satisfies n₁ = 1 and carries charge. |

### Implications

**For ghost elimination:** helicity cannot kill (1,1).  The
only proven mechanism remains slot filtering (R46 Tracks 3–4).
The waveguide cutoff hypothesis (R46 Track 5) is still viable
but untested.

**For the proton:** if (3,6) doesn't carry charge directly
(F6), but each of its three (1,2) sub-strands does, this
strengthens the quark picture — the proton's charge comes
from three individually charged sub-modes, not from the
composite (3,6) topology.  The composite has gcd(3,6) = 3,
meaning it decomposes into three (1,2) strands at 120°.
Each strand has n₁ = 1 → charge 1/3 of e (by the strand's
share of the total energy).  Total: 3 × e/3 = e.

**For the charge mechanism:** charge requires circulation,
not just topology.  A pure standing wave on a torus has zero
charge regardless of winding numbers.  The shear chirality
(embedding angle) breaks the circulation symmetry, giving
net traveling-wave character and therefore charge.  This
connects directly to the matter/antimatter asymmetry: the
preferred circulation direction IS the matter direction.

### Update to Q104

Q104 is **closed — negative result**.  Helicity selects
n₁ = 1 (the tube selection rule) but does not constrain n₂.
The (1,1) ghost must be eliminated by another mechanism.

However, the study produced two positive results not
originally anticipated:
1. A clean derivation of the n₁ = ±1 charge selection rule
   from CP geometry
2. The proof that charge requires circulation (traveling
   wave), connecting charge to the shear chirality mechanism
