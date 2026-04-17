# Track 12: Charge per radian — top-down α from the minimal torus

**Status:** Framed — ready to compute.

**Premise:** Tracks 8–11 worked bottom-up: assume a junction
scattering rule, compute leakage, hope it gives α.  They
failed because the per-junction rule is unknown and the
result depends on which rule you import.

This track works **top-down**.  GRID tells us two things:

1. A 2π phase winding (topological defect) produces exactly
   one unit of charge: e = √(4πα) ≈ 0.303  (GRID A3 + A6)
2. A torus IS a 2π defect — the tube sweeps a full circle

The total charge is known.  The total geometric distortion is
computable (Track 11 found convergent invariants).  The ratio
constrains the per-junction coupling — and therefore α.

**Key idea:** define **charge per radian of distortion**.
Each Y-junction on a curved torus is distorted from its flat
configuration (120° angles, coplanar edges).  The distortion
is computable from pure geometry.  The total distortion around
the tube sums to 2π (Gauss-Bonnet).  If charge is proportional
to distortion, then:

> e = (charge per radian) × 2π

> charge per radian = e / 2π = √(4πα) / 2π = √(α/π)

This is a definite prediction: the "micro-charge" per radian of
bending is √(α/π) ≈ 0.0482.

The question is whether the lattice geometry produces this
specific value, or whether it's just a restatement of α.

---

## Why the minimal torus matters

The minimal torus — the smallest hexagonal lattice that closes
into a valid 2-torus — has:
- The fewest junctions (small N)
- The most distortion per junction (angles far from 120°)
- The most visible per-junction physics

In the continuum limit (large N), the per-junction distortion
becomes infinitesimal and the junction mechanics are hidden.
On the minimal torus, each junction carries a large, discrete
chunk of the 2π total.  The per-junction charge is not
infinitesimal — it's a substantial fraction of e.

If we can compute the charge at each junction of the minimal
torus from first principles (without assuming α), we derive α.
If we can't, we at least learn exactly where α enters the
minimal lattice.

---

## The minimal hexagonal torus

### What "minimal" means

A hexagonal (honeycomb) lattice on a torus requires:
1. The lattice vectors close periodically in both directions
2. Every node has exactly 3 neighbors (honeycomb connectivity)
3. The lattice is orientable (consistent inside/outside)

The minimal torus is the one with the fewest unit cells that
satisfies all three conditions.

### Construction

A honeycomb lattice on a flat torus is defined by two lattice
vectors **a₁** and **a₂** that identify opposite edges of a
parallelogram.  The honeycomb has a 2-atom basis within each
unit cell.

The smallest valid tori:
- (N₁, N₂) = (1, 1): 2 nodes, 3 edges — degenerate (all
  edges connect the same two nodes)
- (N₁, N₂) = (2, 2): 8 nodes, 12 edges — first non-degenerate
- (N₁, N₂) = (3, 3): 18 nodes, 27 edges — more room for
  non-trivial wave modes
- (N₁, N₂) = (2, 3) or (3, 2): 12 nodes — intermediate

The computation should test all small tori and determine which
is the first to support a (1,2) mode (one tube winding, two
ring windings) — the electron mode.

### 3D embedding

Once the minimal flat torus is identified, embed it on a 3D
torus with aspect ratio ε = a/R.  This maps each node to a 3D
position and each edge to a 3D chord.  The junction angles and
edge directions follow from the embedding.

For the minimal torus, the distortions are large — the
"hexagons" are highly non-planar, with angles far from 120°.

---

## The computation

### Step 1: Build minimal hexagonal tori

For N₁ = 2..6, N₂ = 2..6:
1. Construct the honeycomb lattice on a flat torus
2. Embed on a 3D torus at several ε values (0.3, 0.5, 1.0)
3. Compute all junction angles in 3D
4. Verify: does the total angular defect (Σ |angle - 120°|)
   relate to 2π in a simple way?

### Step 2: Compute per-junction distortion

At each junction, the distortion from the flat configuration
can be measured several ways:

a. **Angular deficiency:** Σ_angles - 360° for the three
   angles at the junction.  On a flat junction, this is 0.
   On a curved junction, it's related to the local Gaussian
   curvature (Descartes' theorem: Σ angular_deficiency = 4π
   for a closed surface with Euler characteristic 0 for a torus...
   actually for a torus χ = 0, so Σ = 0.  Hmm — this needs
   care.)

b. **Non-coplanarity measure:** the solid angle subtended by
   the three edge directions.  Zero when coplanar, nonzero
   when the edges leave the plane.

c. **Normal component of bending:** how much each edge deviates
   from the local tangent plane (the Track 11 measure).

d. **Turning angle:** the angle through which the surface
   normal rotates from one junction to the next.  Summing
   around the tube gives exactly 2π.

The turning angle (d) is the most natural "radian" measure:
each junction contributes a definite fraction of the total
2π rotation.  On the minimal torus, each junction contributes
a large fraction (2π / N_junctions_per_circuit).

### Step 3: Compute charge at each junction

Two approaches:

**Approach A — Assign charge proportional to turning angle.**

If charge_per_radian = e / 2π, then the charge at junction k is:

> q_k = (turning_angle_k / 2π) × e

Verify: Σ q_k = e.  (This is guaranteed by construction.)

This is NOT a derivation of α — it's a distribution of the
known total charge across junctions proportionally.  But it
gives a prediction: the charge is concentrated at junctions
with large turning angles (high curvature = inner equator).

**Approach B — Compute charge from Track 8 field projection.**

Use the CP field (Track 8, E·ρ̂ projection) at each junction:

> q_k ∝ E_ρ(θ₁_k) × dA_k

This is the microscopic charge from the actual field, not from
a proportionality assumption.  Compare with Approach A: do
they agree?

If yes: the field naturally distributes charge proportional to
turning angle, which means the "charge per radian" concept is
physical.

If no: the field has its own distribution that differs from
geometric turning angle.

**Approach C — Compute energy cost of distortion.**

For each junction on the minimal torus:
1. The flat configuration has 3 edges at 120°, energy E_flat
2. The curved configuration has distorted angles, energy E_curved
3. The energy cost δE = E_curved - E_flat

This energy cost is NOT the charge — it's the elastic cost of
bending.  But in GRID, the energy of a topological defect IS
the charge (via e² = 4πα).  If:

> Σ δE_k = e² / (4π) = α    (the Coulomb self-energy)

then the elastic cost of bending the minimal torus into 3D
equals the electromagnetic self-energy of the charge it
produces.  This would be a self-consistency condition that
constrains α from geometry.

### Step 4: The self-consistency equation

The dream result:

> (total distortion energy) = α × (total mode energy)

where total distortion energy is computed from junction
geometry (no α input) and total mode energy is the Compton
energy (mc²).  If this holds, then:

> α = (distortion energy) / (mode energy)

This would derive α from the ratio of two energies: the cost
of bending the lattice (geometric) vs the energy of the wave
living on it (dynamical).

### Step 5: Test on multiple torus sizes

If Step 4 produces a self-consistency equation, test whether
the same α emerges from N₁ = N₂ = 2, 3, 4, 5, 10, 20.
If α is a geometric constant (independent of lattice size),
this confirms it's a property of the lattice structure, not
of the specific torus.

---

## What we're looking for

### Strong success

The distortion energy / mode energy ratio is a definite
constant (independent of N and ε) that equals α = 1/137.
This derives α from pure lattice geometry.

### Partial success

The ratio is a definite constant but NOT α.  It might be a
simple function of α (like α², or α/2π) — which would
constrain α but not fully determine it.

### Informative result

The ratio depends on N (lattice size), reproducing the Track
11 finding that the junction mechanics are resolution-dependent.
But the minimal torus (smallest N) gives a specific number
that may have geometric significance — even if it doesn't
extrapolate to the continuum.

### Connection to GRID A6

If the computation requires α as an input (through the lattice
action κ = 1/4πα) to compute the distortion energy, then:
- We identify exactly where α enters the minimal torus
- We characterize how the Y-junction behaves as a function of α
- We establish that α governs the coupling between 2D bending
  and 3D charge emission — the impedance mismatch of the title

Even this "tautological" result is valuable: it pins down
α's role in GRID at the junction level, which no prior track
has achieved.

---

## Relationship to prior tracks

| Track | What it computed | Why it couldn't derive α |
|-------|-----------------|------------------------|
| 8 | E·ρ̂ selection rule | Determines WHICH modes, not HOW MUCH |
| 9 | Per-junction geometric escape | Resolution-dependent (1/N²) |
| 10 | Iterative scalar propagation | S-matrix has no leakage channel |
| 11 | Vector energy deficit, 4 models | Convergent invariants ≠ α |
| **12** | **Top-down: total charge / total distortion** | **Uses GRID's known total to constrain per-junction behavior** |

Track 12 inverts the logic: instead of computing the total
from the parts, it uses the known total to learn about the
parts.

---

## Dependencies

- numpy (lattice construction, geometry)
- Track 11 lattice code (reuse build_hex_torus)
- Track 8 CP field code (for Approach B)

---

## Files

| File | Purpose |
|------|---------|
| T12-charge-per-radian.md | This framing document |
| scripts/track12_minimal_torus.py | Main computation |
| F12-charge-per-radian.md | Findings (after computation) |
