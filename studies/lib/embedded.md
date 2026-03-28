# embedded.py — Design Spec

Embedded torus geometry and near-field calculations.  Computes
how Ma modes project into 3D space: charge distributions,
E-fields, multipole moments, and interaction energies between
particles.

Lives alongside `ma.py` and `ma_model.py` in `lib/`.  Separate
module, not part of `ma_model.py`.


## Relationship to other modules

```
ma.py / ma_model.py          embedded.py
─────────────────────         ────────────────────
Intrinsic geometry            Extrinsic geometry
Flat torus (no embedding)     Torus embedded in 3D
Mode energies, charges        E-fields, multipoles
"What modes exist?"           "What do they look like?"

     L₁–L₆, s₁₂, s₅₆
     ─────────────────→
     (shared parameters)
```

`embedded.py` imports geometry parameters from `ma.py` (or
from a `Ma` object when `ma_model.py` exists) but adds the
embedding physics on top.  It does NOT depend on `ma_model.py`
— only on `ma.py` for `compute_scales` and constants.

The two modules answer different questions:

| Question | Module |
|----------|--------|
| What is the electron's energy? | ma.py / ma_model.py |
| What is the electron's 3D E-field? | embedded.py |
| How many modes below 10 GeV? | ma_model.py |
| What force does one electron exert on another at 1 fm? | embedded.py |
| What is ∂E/∂r_p for the neutron? | ma_model.py |
| Do anti-phased protons attract at nuclear distances? | embedded.py |


## Physical picture

A material sheet (e.g., Ma_e) is a flat 2-torus T² with
circumferences L_tube and L_ring.  In 3D, it embeds as a torus
with:

    R = L_ring / (2π)     major radius (ring)
    a = L_tube / (2π)     minor radius (tube)

A mode (n₁, n₂) traces a path on this surface — the (n₁, n₂)
torus knot.  **Important:** this module uses the *flat-torus
geodesic* (uniform angular velocity in θ₁, θ₂) projected onto
the embedded surface, NOT the true geodesic of the torus of
revolution (which follows Clairaut's relation and has non-uniform
angular velocity; see R12 Track 2).  On a flat torus the two
are identical; on the embedded torus they differ, with the
discrepancy growing with a/R.  At r_e = 6.6 (a >> R), the
deviation is significant.  This is a modeling choice: the flat
geodesic is the physically meaningful path (the photon sees flat
space internally), while the embedded surface is a visualization
aid.

In the WvM picture, charge is distributed along this path.
The phase φ determines the rotational offset of the charge
pattern on the torus surface.

The 3D E-field of this charge distribution has:
- A monopole moment Q (= total charge, phase-independent)
- Higher multipoles (dipole, quadrupole, ...) that depend on
  the mode quantum numbers and phase

At large distances (r >> R), only the monopole matters and the
particle looks like a point charge.  At short distances (r ~ R),
the multipole structure creates phase-dependent forces.


## Architecture

```
EmbeddedSheet
│
├── Construction
│   ├── from_circumferences(L_tube, L_ring)
│   ├── from_aspect_ratio(r, scale_MeV)
│   └── from_ma(L, sheet='e'|'p'|'nu')
│
├── Geometry
│   ├── R, a                    major/minor radii (fm)
│   ├── aspect_ratio            a/R
│   ├── surface_area            4π²Ra (fm²)
│   └── torus_point(theta1, theta2)  → (x, y, z)
│
├── Charge distribution
│   ├── geodesic(n1, n2, N, phi)     → positions (N×3)
│   ├── charge_segments(n1, n2, N, phi, Q)
│   │       → (positions, charges)   N charge elements
│   └── charge_density(n1, n2, phi)
│           → callable σ(θ₁, θ₂)    continuous form
│
└── Multipoles (methods — use torus center as origin)
    ├── multipoles(pos, dq, l_max)  → q_lm array
    ├── monopole(pos, dq)           → Q
    ├── dipole(pos, dq)             → (dx, dy, dz)
    └── quadrupole(pos, dq)         → Q_ij (3×3)

Free functions (work on any pos/dq arrays, including mixed sheets):

field_at(pos, dq, point, eps=0)        → (Ex, Ey, Ez)
potential_at(pos, dq, point, eps=0)    → V
field_energy(pos, dq, eps)             → U_E (self-energy)
interaction_energy(pos1, dq1, pos2, dq2)         → U_int
interaction_force(pos1, dq1, pos2, dq2, axis)    → F
interaction_sweep(sheet1, sheet2, n1, n2, N,
                  Q1, Q2, d_values, phi_values)
        → SweepResult(U, U_coulomb, ratio)
```


## Feature 1: EmbeddedSheet construction

### What

An `EmbeddedSheet` represents one material sheet (Ma_e, Ma_p,
or Ma_ν) embedded as a torus in 3D space.  It holds the
embedding geometry (R, a) and provides methods to create charge
distributions, compute fields, and measure interactions.

### Interface

```python
from lib.embedded import EmbeddedSheet
from lib.ma import compute_scales

L, s12, s34, s56 = compute_scales(r_e=6.6, r_nu=5.0, r_p=8.906)

# From full circumference array + sheet name
e_sheet = EmbeddedSheet.from_ma(L, sheet='e')   # uses L[0], L[1]
p_sheet = EmbeddedSheet.from_ma(L, sheet='p')   # uses L[4], L[5]

# Direct construction
e_sheet = EmbeddedSheet.from_circumferences(L_tube=4.396, L_ring=0.666)

# Access geometry
e_sheet.R          # major radius (fm)
e_sheet.a          # minor radius (fm)
e_sheet.aspect     # a/R
```

### Immutability

Like the planned `Ma` class, `EmbeddedSheet` is immutable after
construction.  Different geometries = different objects.


## Feature 2: Charge distribution

### What

Create a discrete charge distribution along the (n₁, n₂)
geodesic on the torus surface, with a specified phase offset.

### The geodesic

The (n₁, n₂) torus knot is parameterized as:

    θ₁(t) = n₁ · t + φ
    θ₂(t) = n₂ · t

for t ∈ [0, 2π).  In 3D Cartesian coordinates:

    x(t) = (R + a cos θ₁(t)) cos θ₂(t)
    y(t) = (R + a cos θ₁(t)) sin θ₂(t)
    z(t) = a sin θ₁(t)

The phase φ rotates the charge pattern on the torus surface.
At φ = 0, the geodesic starts at the outer equator.  At φ = π,
it starts at the inner equator.  The spatial distribution of
charge in 3D rotates accordingly.

### Interface

```python
# Discrete charge distribution: N segments along (1,2) geodesic
pos, dq = e_sheet.charge_segments(n1=1, n2=2, N=500, phi=0.0, Q=1.0)
# pos: ndarray (N, 3) — segment midpoints in fm
# dq:  ndarray (N,)   — charge per segment (units of e)

# Same mode, different phase
pos2, dq2 = e_sheet.charge_segments(n1=1, n2=2, N=500, phi=math.pi)
```

### Charge weighting convention

Charge is distributed with **uniform weight per parameter step
dt**, not per arc length on the embedded surface.  On the
embedded torus, arc length per dt varies as
ds/dt = √((n₁ a)² + (n₂(R + a cos(n₁t + φ)))²), so uniform-dt
sampling places more charge per unit 3D length on the inner
equator (where R + a cos θ₁ is small) than the outer.  This
matches the flat-torus convention (uniform energy density on
the intrinsic manifold).

If a different weighting is needed (e.g., uniform arc-length
distribution), pass a `weights` array to `charge_segments`.

### Charge conservation

Total charge Σ dq = Q regardless of φ, n₁, n₂, and weighting.
The phase changes WHERE the charge sits, not HOW MUCH.


## Feature 3: E-field and potential

### What

Compute the 3D electric field and potential at arbitrary points
from a charge distribution.

### Interface

```python
# E-field at a point
Ex, Ey, Ez = field_at(pos, dq, point=[10.0, 0.0, 0.0])

# Potential at a point
V = potential_at(pos, dq, point=[10.0, 0.0, 0.0])

# Vectorized: field at multiple points
E = field_at_points(pos, dq, points)  # (M, 3) array
```

### Implementation

Direct Coulomb summation:

    E(P) = Σ_i  dq_i (P − r_i) / (|P − r_i|² + ε²)^{3/2}

The softening parameter `eps` (default 0) regularizes the
self-energy divergence at source locations.  It should ONLY be
used for self-energy calculations (`field_energy`); for
inter-particle fields and interaction energies, set `eps = 0`
(no divergence when source and field points are on different
particles).

When needed, use eps ~ 0.01 × a (much smaller than torus
dimensions, large enough to smooth the point-charge singularity).

Units: E in e/(4πε₀ fm²), V in e/(4πε₀ fm).  Dimensionless
internally; physical units via constants.py when needed.


## Feature 4: Multipole decomposition

### What

Decompose a charge distribution into spherical multipole
moments about its center of charge.

### Interface

```python
qlm = e_sheet.multipoles(pos, dq, l_max=4)
# qlm: dict mapping (l, m) → complex coefficient

Q = e_sheet.monopole(pos, dq)             # scalar (total charge)
d = e_sheet.dipole(pos, dq)               # (3,) vector
Q_ij = e_sheet.quadrupole(pos, dq)        # (3,3) traceless tensor
```

### What we learn

For the electron mode (1,2) on a torus with r_e = 6.6:
- Q (monopole) = −1 — phase-independent
- d (dipole): nonzero if the charge distribution is
  asymmetric about the center.  Depends on φ.
- Q_ij (quadrupole): captures the elongation of the charge
  along the torus.  Depends on φ.

The multipole spectrum tells us how much "near-field structure"
the mode has beyond the point-charge approximation.


## Feature 5: Interaction energy and force

### What

Compute the electrostatic interaction energy between two charge
distributions at specified separation and relative phase.

### Interface

```python
# Two electron modes at separation d along z, phase offset Δφ
pos1, dq1 = e_sheet.charge_segments(1, 2, 500, phi=0.0)
pos2, dq2 = e_sheet.charge_segments(1, 2, 500, phi=math.pi)

# Shift particle 2 by distance d along z
pos2_shifted = pos2 + [0, 0, d]

# Interaction energy
U = interaction_energy(pos1, dq1, pos2_shifted, dq2)

# Compare to Coulomb
U_coulomb = Q1 * Q2 / d   # in natural units
ratio = U / U_coulomb
```

### Sweep interface

```python
# Full (d, Δφ) sweep — the main R39 computation
# Same-sheet (e-e):
result = interaction_sweep(
    sheet1=e_sheet, sheet2=e_sheet,
    n1=1, n2=2, N=500, Q1=-1.0, Q2=-1.0,
    d_values=np.linspace(0.1, 50.0, 100),   # fm
    phi_values=np.linspace(0, 2*np.pi, 24),
)

# Mixed sheets (e-p for hydrogen):
result_ep = interaction_sweep(
    sheet1=e_sheet, sheet2=p_sheet,
    n1=1, n2=2, N=500, Q1=-1.0, Q2=+1.0,
    d_values=np.linspace(0.1, 50.0, 100),
    phi_values=np.linspace(0, 2*np.pi, 24),
)

# result.U[i, j]  — interaction energy at d_values[i], phi_values[j]
# result.U_coulomb[i] — point-charge Coulomb at d_values[i]
# result.ratio[i, j]  — U / U_coulomb
```

### Implementation

Direct pairwise Coulomb sum:

    U = Σ_i Σ_j  dq1_i × dq2_j / |r1_i − r2_j|

This is O(N₁ × N₂) per configuration.  At N = 500, that's
250K evaluations — fast (milliseconds per (d, Δφ) point).

For the full sweep (100 d × 24 Δφ = 2400 configurations),
total cost is ~600M evaluations.  With NumPy vectorization
this should complete in seconds to minutes.

### Force

The force along the separation axis is:

    F(d) = −∂U/∂d ≈ −(U(d+ε) − U(d−ε)) / (2ε)

Computed by finite difference from the interaction energy.


## Feature 6: Near-field correction extraction

### What

Utilities to extract the phase-dependent near-field correction
from a sweep, for use by R39 Track 3.

### Interface

```python
# From a completed sweep:
nf = near_field_correction(result)

# nf.U_avg[i]       — ⟨U⟩_φ at each distance (phase-averaged)
# nf.delta_U[i, j]  — U(d, Δφ) − ⟨U⟩_φ(d)
# nf.delta_U_pi[i]  — delta_U at Δφ = π (anti-phase correction)
# nf.barrier_factor[i] — U(d, π) / U_coulomb(d) (barrier reduction)
```


## Dependencies

- `numpy` (vectorized computation)
- `lib.ma` (for `compute_scales`, constants)
- `lib.constants` (for physical constants when converting units)
- No new external dependencies


## Implementation plan

### Phase 1: Core geometry (for R39 Track 1)

1. `EmbeddedSheet` class with constructors.
2. `geodesic()` and `charge_segments()`.
3. `field_at()` and `potential_at()`.
4. Basic `multipoles()` (monopole, dipole, quadrupole).

### Phase 2: Interaction engine (for R39 Track 2)

5. `interaction_energy()` pairwise sum.
6. `interaction_sweep()` with NumPy vectorization.
7. `near_field_correction()` extraction.

### Phase 3: Performance (for R39 Track 4)

8. Vectorize the pairwise sum using broadcasting
   (pos1[:, None, :] − pos2[None, :, :]).
9. Phase-reuse optimization: compute the geodesic at φ = 0
   once, then for each new φ recompute positions via:

       x(t; φ) = (R + a cos(n₁t + φ)) cos(n₂t)
       y(t; φ) = (R + a cos(n₁t + φ)) sin(n₂t)
       z(t; φ) = a sin(n₁t + φ)

   This is NOT a rigid rotation of the full distribution — φ
   rotates the charge pattern around the tube at each θ₂ slice
   independently.  Precompute sin(n₁t), cos(n₁t), sin(n₂t),
   cos(n₂t) once (4 arrays of size N), then for each φ use
   angle-addition identities to get sin(n₁t + φ) and
   cos(n₁t + φ) with 2 multiplies + 1 add per element.
   Avoids recomputing N trig calls per phase step.


## Testing

1. **Monopole only:** At d >> R, interaction_energy must equal
   Q₁Q₂/d to better than 0.1%.

2. **Self-energy:** field_energy of a single charge distribution
   should approximately match R7's results for the same geometry.

3. **Symmetry:** interaction_energy(d, Δφ) = interaction_energy(d, −Δφ)
   and interaction_energy(d, Δφ) = interaction_energy(d, Δφ + 2π).

4. **Phase average:** ⟨U(d, Δφ)⟩_φ ≈ U_Coulomb(d) to within
   the multipole truncation error.

5. **Roundtrip:** charge_segments with Q=1 must sum to exactly 1.


## File layout after completion

```
lib/
  index.md          library guide (updated to include embedded.py)
  ma-model.md       ma_model.py design spec
  embedded.md       THIS FILE — embedded.py design spec
  constants.py      unchanged
  wvm.py            unchanged
  series.py         unchanged
  ma.py             unchanged
  ma_solver.py      unchanged
  ma_model.py       planned — flat torus spectrum engine
  embedded.py       NEW — embedded torus near-field calculations
```
