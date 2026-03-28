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

A mode (n₁, n₂) traces a geodesic on this surface — the
(n₁, n₂) torus knot.  In the WvM picture, charge is
distributed along this geodesic.  The phase φ determines the
rotational offset of the charge pattern on the torus surface.

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
├── Fields
│   ├── field_at(charges, point)     → (Ex, Ey, Ez)
│   ├── potential_at(charges, point) → V
│   └── field_energy(charges, grid)  → U_E (total field energy)
│
├── Multipoles
│   ├── multipoles(charges, l_max)   → q_lm array
│   ├── monopole(charges)            → Q
│   ├── dipole(charges)              → (dx, dy, dz)
│   └── quadrupole(charges)          → Q_ij (3×3)
│
└── Interaction
    ├── interaction_energy(dist1, dist2)           → U_int
    ├── interaction_force(dist1, dist2, axis)      → F
    └── interaction_sweep(dist1, dist2, d_range, phi_range)
            → 2D array of U_int(d, Δφ)
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

### Charge conservation

Total charge Σ dq = Q regardless of φ, n₁, n₂.  The phase
changes WHERE the charge sits, not HOW MUCH.


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

    E(P) = Σ_i  dq_i (P − r_i) / |P − r_i|³

with a softening parameter ε to avoid self-energy divergence
at the source locations.  The softening scale should be much
smaller than the torus dimensions (~0.01 × a).

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
result = interaction_sweep(
    sheet=e_sheet, n1=1, n2=2, N=500, Q=1.0,
    d_values=np.linspace(0.1, 50.0, 100),   # fm
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
9. Optional: precompute charge distribution once, reuse for
   all Δφ by rotating the phase analytically.


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
