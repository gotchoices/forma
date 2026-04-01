# sim-schwarzschild: Event horizon from hexagonal lattice shearing

**Status:** Framed — ready to build.

**Question:** at what radius does a hexagonal lattice with
fixed edge lengths fail to accommodate the Schwarzschild
geometry?  Does this critical radius match r_s = 2GM/c²?

**Motivation:** on a flexible hexagonal lattice with fixed
edges, the Schwarzschild metric demands increasing radial
elongation of hexagons as r → r_s.  At some critical
deformation, the hexagons can no longer accommodate the
curvature — the lattice must shear (edges disconnect).
This shearing IS the event horizon, arising as a geometric
limit rather than a coordinate singularity.

If the critical radius is computable from lattice geometry
alone, it may provide a geometric derivation of G
independent of the Jacobson thermodynamic argument.

---

## The geometry

### Schwarzschild in 2D (spatial slice)

For a central mass M, the spatial metric at fixed time on
the equatorial plane is:

<!-- dl² = dr²/(1 − r_s/r) + r² dθ² -->
$$
dl^2 = \frac{dr^2}{1 - r_s/r} + r^2 \, d\theta^2
$$

where r_s = 2GM/c² (= 2M in natural units with G = 1).

This means:
- **Circumferential direction:** proper length = r dθ
  (same as flat space — no stretching)
- **Radial direction:** proper length = dr / √(1 − r_s/r)
  (stretched by a factor 1/√(1 − r_s/r))

The stretch factor diverges as r → r_s.

### Embedding in flat 2D

To visualize: take a flat 2D hexagonal lattice and try to
map it onto the Schwarzschild spatial geometry (Flamm's
paraboloid in 3D, but we work in the intrinsic 2D metric).

At each radius r, the lattice must accommodate:
- **Circumferential:** 2πr / L edges around the ring
  (L = edge length = 1 Planck unit)
- **Radial:** edges spanning dr with proper length
  dr / √(1 − r_s/r)

The ratio of radial to circumferential edge density is:
stretch(r) = 1 / √(1 − r_s/r)

At r = 2r_s: stretch = √2 ≈ 1.41
At r = 1.5r_s: stretch = √3 ≈ 1.73
At r = 1.1r_s: stretch = √10 ≈ 3.16
At r → r_s: stretch → ∞

### The hexagonal limit

A hexagon with 6 equal edges of length L can be deformed
(flexed) to various aspect ratios while keeping all edges
at length L.  The maximum radial-to-circumferential aspect
ratio is bounded by geometry.

**The simulation computes this bound** by:
1. Building a hexagonal lattice in annular (ring) geometry
2. Applying the Schwarzschild stretch at each radial ring
3. Relaxing the lattice to minimize deformation energy
   while keeping all edge lengths = L
4. Finding the innermost radius where a valid hexagonal
   tiling exists

---

## Simulation design

### Approach 1: Analytic (hexagon deformation limit)

Compute the maximum aspect ratio of a single hexagon with
all edges = 1:

1. Parameterize a hexagon by its 6 vertex positions
2. Constrain all edge lengths = 1
3. Maximize the ratio height/width (or radial/circumferential
   extent)
4. The maximum aspect ratio = the critical stretch factor
5. The critical radius: 1/√(1 − r_s/r_crit) = max_stretch
   → r_crit = r_s / (1 − 1/max_stretch²)

This gives a closed-form answer if the single-hexagon limit
controls the lattice limit.

### Approach 2: Lattice relaxation

Build a hexagonal lattice in annular geometry and deform it:

1. Create a flat hexagonal annulus (inner radius R_in,
   outer radius R_out)
2. Apply the Schwarzschild radial stretch: move vertices
   radially to match the proper-distance embedding
3. Relax the lattice to restore edge lengths = L while
   respecting the Schwarzschild circumferential constraint
4. Measure the residual strain (edge length deviation from L)
   as a function of radius
5. The radius where strain exceeds a critical threshold
   (or where the relaxation fails to converge) is the
   shearing radius

### Approach 3: Pentagon insertion

Instead of stretching hexagons, insert pentagonal defects
to create curvature:

1. Start with a flat hexagonal lattice
2. At each radial ring, compute the required Gaussian
   curvature from the Schwarzschild metric
3. Insert the number of pentagons needed to produce that
   curvature (each pentagon contributes π/3 of deficit angle)
4. Find the radius where the required pentagon density
   exceeds 100% (all faces are pentagons — no hexagons left)
5. This is the maximum-curvature radius

---

## Expected results

### What would be a strong result

If any of the three approaches gives r_crit ≈ r_s (or a
simple multiple of r_s), this means the event horizon is a
geometric consequence of fixed-edge hexagonal lattice
failure.  The relationship r_crit = f(r_s) combined with
r_s = 2GM/c² would give G in terms of the lattice's
geometric limit f.

### What would be informative but weaker

If r_crit = C × r_s where C ≠ 1 (but is a simple
geometric constant like √3 or 2), this still connects the
horizon to the lattice geometry, but with a correction
factor that needs explanation.

### What would be a negative result

If r_crit has no clean relationship to r_s (depends on
lattice size, boundary conditions, or other non-universal
quantities), the geometric shearing idea doesn't produce
a clean horizon.  Gravity would remain purely thermodynamic
(Jacobson), not geometric.

---

## Key quantities to compute

| Quantity | Definition | How |
|----------|-----------|-----|
| max_stretch | Maximum radial/circumferential aspect ratio of a hexagon with unit edges | Analytic geometry |
| r_crit | Innermost radius where hexagonal tiling is valid | r_s / (1 − 1/max_stretch²) |
| K_max | Maximum Gaussian curvature from pentagon packing | 2π / (3 × A_pent) |
| n_pent(r) | Required pentagon density at radius r | From Schwarzschild curvature |

---

## Files (planned)

| File | Purpose |
|------|---------|
| `README.md` | This document |
| `hexagon_limit.py` | Approach 1: analytic hexagon deformation |
| `annular_lattice.py` | Approach 2: lattice relaxation on Schwarzschild |
| `pentagon_density.py` | Approach 3: curvature from pentagonal defects |
| `run.py` | All three approaches + comparison |
| `output/` | Plots and data |

---

## Dependencies

numpy, scipy, matplotlib (all in project `.venv`)
