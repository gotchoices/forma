# sim-gravity: Deformation field from an embedded rigid body

**Status:** Planned — not yet started.

**Question:** when a rigid flat structure is embedded in a
relaxable lattice, does the resulting deformation field fall
off as 1/r (2D) or 1/r² (3D)?

If yes, this demonstrates that the "flat grid, warped
embedding" mechanism from [dual-bubbles.md](../dual-bubbles.md)
reproduces Newtonian gravity without importing GR.

---

## Setup

### The lattice

A finite 2D triangular lattice with N × N cells, periodic
boundary conditions (torus topology to avoid edge effects).
Each vertex has a 2D position (x, y).

**Equilibrium state:** all edges equal to 1 (Planck length),
all triangles equilateral.  This is the "flat vacuum."

**Energy functional:** elastic energy penalizing deviations
from the rest length.  Simplest model: harmonic springs on
every edge.

<!-- E = (k/2) Σ_edges (|r_i - r_j| - 1)² -->
$$
E = \frac{k}{2} \sum_{\text{edges}} \bigl(|\mathbf{r}_i - \mathbf{r}_j| - 1\bigr)^2
$$

### The "particle"

A closed ring of vertices whose mutual distances are
**frozen** — they form a rigid polygon embedded in the
lattice.  This represents a flat compact sub-structure
(the Ma torus cross-section in 2D).

Options for the rigid body:
- A single frozen triangle (3 vertices, simplest)
- A hexagonal ring (6 vertices, more symmetric)
- A larger rigid patch (N_p vertices)

The rigid body has a characteristic size R_particle
(analogous to the Compton wavelength).

### The simulation

1. Start with the equilibrium lattice (all edges = 1)
2. Insert the rigid body by fixing the positions of its
   vertices
3. Relax the remaining vertices to minimize E (gradient
   descent, conjugate gradient, or similar)
4. Measure the displacement field u(r) = |r_relaxed - r_eq|
   as a function of distance r from the rigid body's center
5. Fit u(r) to a power law: u ∝ r^(−p)

### What to look for

| Outcome | Meaning |
|---------|---------|
| p ≈ 1 (2D) | Deformation falls off as 1/r — consistent with 2D Newtonian gravity |
| p ≈ 0 | Deformation is uniform — no localized gravity |
| p ≈ 2 | Falls off too fast — wrong power law |
| Oscillatory | Lattice artifacts dominate |

**2D expectation:** in 2D continuum elasticity, a point
defect in an elastic sheet produces a displacement field
that falls off as 1/r (logarithmic potential, 1/r force).
This is the 2D analog of Newtonian gravity's 1/r² in 3D.

### Extensions

- **3D version:** stack triangular layers into a 3D
  simplicial lattice, embed a rigid torus, check for 1/r².
  Much more expensive computationally.

- **Entropy measurement:** instead of elastic energy, count
  the number of lattice configurations (microstates) as a
  function of the deformation.  This would directly test
  whether δS = ζ δA holds.

- **Multiple particles:** embed two rigid bodies, relax,
  measure the force between them (energy vs separation).
  Check for 1/r (2D) or 1/r² (3D) force law.

---

## Files (planned)

| File | Purpose |
|------|---------|
| `README.md` | This design document |
| `lattice.py` | Triangular lattice generation, equilibrium positions |
| `embed.py` | Insert rigid body, set up constraints |
| `relax.py` | Energy minimization with frozen vertices |
| `measure.py` | Displacement field analysis, power-law fit |
| `run.py` | End-to-end: generate → embed → relax → measure → plot |

---

## Estimated scale

- **Minimum viable lattice:** 50 × 50 (~2500 vertices,
  ~7500 edges).  Should run in seconds.
- **Production lattice:** 200 × 200 (~40,000 vertices).
  Should run in under a minute.
- **Particle size:** 3–20 vertices (rigid body should be
  small relative to the lattice).
- **Dependencies:** numpy, scipy (for minimization), matplotlib
