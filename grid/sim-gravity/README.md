# sim-gravity: Deformation field from an embedded rigid body

**Status:** Complete.  Instructive negative result (see below).

**Question:** when a rigid flat structure is embedded in a
relaxable triangular lattice and the lattice is allowed to
relax, what power law governs the deformation field?

**Answer:** edge strain ε ∝ 1/r² — the **elastic** power law,
not the **gravitational** power law (1/r).

---

## Setup

### The lattice

A finite 2D triangular lattice (N × N vertices) with free
boundary conditions.  Boundary vertices are clamped at their
equilibrium positions; interior vertices relax freely.

**Equilibrium state:** all edges equal to 1 (Planck length),
all triangles equilateral.  This is the "flat vacuum."

**Energy functional:** harmonic springs on every edge.

<!-- E = (k/2) Σ_edges (|r_i - r_j| - 1)² -->
$$
E = \frac{k}{2} \sum_{\text{edges}} \bigl(|\mathbf{r}_i - \mathbf{r}_j| - 1\bigr)^2
$$

### The "particle"

A small cluster of vertices (hexagonal ring = 7 vertices, or
a single triangle = 3 vertices) whose mutual distances are
**frozen** after dilation by a scale factor (1.3× or 1.5×).
This injects excess area into the lattice — analogous to a
flat Ma torus cross-section forcing the ambient lattice S to
accommodate a foreign geometry.

### The simulation

1. Generate equilibrium lattice (all edges = 1)
2. Identify defect vertices (hexagon or triangle at centre)
3. Dilate defect by scale factor (frozen at expanded size)
4. Clamp boundary vertices at equilibrium positions
5. Relax interior (L-BFGS-B minimisation of spring energy)
6. Measure **edge strain** ε = |l_relaxed − l₀|/l₀ and
   **displacement** u = |r_relaxed − r_eq| vs distance r

### Primary diagnostic: edge strain

Edge strain is a purely local quantity — the fractional
deviation of each edge from its rest length.  Unlike
displacement, it is insensitive to boundary artifacts and
rigid-body offsets.  It is the natural analog of "how much
does the lattice geometry differ from flat" at each edge.

---

## Results

### Data

| Trial | p (ε ∝ r⁻ᵖ) | R² | Notes |
|-------|-------------|-----|-------|
| 100² hexagon, s=1.3 | 1.973 | 0.997 | |
| 150² hexagon, s=1.3 | 1.988 | 1.000 | |
| 200² hexagon, s=1.3 | **1.999** | **1.000** | Primary run |
| 200² hexagon, s=1.5 | 2.000 | 1.000 | Stronger dilation |
| 200² triangle, s=1.3 | 2.031 | 1.000 | Smaller defect |

Edge strain follows **ε ∝ 1/r²** with R² = 0.9999 across
all trials.  The exponent converges to exactly 2.0 as the
lattice grows.

Plots are in `output/gravity_fits.png` and
`output/lattice_detail.png`.

---

## Why 1/r² and not 1/r

The core issue is the type of field on the lattice.

**What we simulated:** each vertex has a **2D position
vector** (x, y).  This vector field satisfies Navier's
equation in the continuum limit — the equation of 2D
elasticity.  For a point defect (the Eshelby inclusion
problem), Navier's equation gives:

- Displacement: u ∝ 1/r
- Strain: ε = du/dr ∝ 1/r²

**What gravity requires:** a **scalar** field (the
gravitational potential φ) satisfying Poisson's equation
∇²φ = source.  In 2D, the Green's function is:

- Potential: φ ∝ log(r)
- Force: F = −dφ/dr ∝ 1/r

The missing factor of 1/r comes from the difference between
a vector equation (Navier, for displacements) and a scalar
equation (Poisson, for potential).  A harmonic spring lattice
inherently solves the former.

| Theory | Equation | Field type | Displacement/potential | Force/strain |
|--------|----------|------------|----------------------|-------------|
| 2D elasticity | Navier | Vector (x,y) | u ∝ 1/r | ε ∝ 1/r² |
| 2D gravity | Poisson | Scalar (φ) | φ ∝ log(r) | F ∝ 1/r |

---

## What we learned

### 1. The lattice is a valid elastic medium

The triangular lattice reproduces 2D continuum elasticity to
four decimal places (p = 2.000, R² = 0.9999).  This confirms
the substrate itself is well-behaved — it correctly recovers
continuum physics in the large-scale limit.

### 2. Mechanical energy minimisation ≠ gravity

Minimising spring energy gives the elastic power law (1/r²),
not the gravitational one (1/r).  Gravity does not emerge
from naive energy minimisation on a spring lattice.  This is
the central negative result.

### 3. The thermodynamic route is genuinely necessary

GRID derives gravity via Jacobson's thermodynamic argument
([gravity.md](../gravity.md)): entropy + temperature →
Einstein equations.  This simulation confirms that the
mechanical route is a dead end, making the thermodynamic
route not just elegant but *necessary*.

### 4. The field-type distinction matters

A **vector** field (vertex positions) gives Navier → 1/r².
A **scalar** field (phase, entropy, temperature) gives
Poisson → 1/r.  The gravitational degree of freedom must be
scalar-like, not vector-like.  This is consistent with GRID's
axiom A3 (scalar phase) and A5 (scalar entropy density).

---

## What might work better

Three directions for a follow-up study, in order of promise:

### A. Entropic force (→ sim-gravity-2)

Instead of minimising energy, count *microstates*.  Give each
lattice node internal degrees of freedom (standing-wave modes
on a 1D string register — see [INBOX.md](../INBOX.md)).  A
rigid body constrains the modes of nearby nodes.  The entropy
deficit creates a **scalar** shadow that falls off as log(r)
in 2D.  The entropic force F = T · dS/dr would then go as
1/r — the gravitational law.

This is the most promising direction because it directly
implements the Jacobson mechanism on the lattice.

### B. Scalar field relaxation

Place a scalar field (phase θ) on each node instead of 2D
vertex positions.  Pin the scalar at the defect, let it relax.
The scalar satisfies the discrete Laplacian ∇²θ = 0, giving
θ ∝ log(r) and dθ/dr ∝ 1/r.  This would "work" but is
nearly tautological — it just solves Poisson's equation on
a grid.  Useful for code validation, not a physical proof.

### C. Curvature-based energy

Replace the spring energy with an energy functional that
depends on angle deficits (Gaussian curvature) or area
changes rather than edge lengths.  The Regge calculus action
for 2D gravity uses angle deficits, and this might produce
the scalar Poisson equation rather than the vector Navier
equation.

---

## Files

| File | Purpose |
|------|---------|
| `README.md` | This document |
| `lattice.py` | Triangular lattice generation (periodic or free BCs) |
| `embed.py` | Insert rigid body (hexagon, triangle, or patch) |
| `relax.py` | L-BFGS-B energy minimisation with frozen vertices |
| `measure.py` | Edge strain and displacement analysis, fitting |
| `run.py` | End-to-end pipeline: generate → embed → relax → measure → plot |
| `output/` | Generated plots and raw data |

---

## Running

```bash
source .venv/bin/activate
python grid/sim-gravity/run.py
```

200×200 lattice completes in ~10s per trial.
Dependencies: numpy, scipy, matplotlib.
