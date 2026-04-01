# sim-schwarzschild: Event horizon from hexagonal lattice geometry

**Status:** Complete ✅

**Question:** at what radius does a hexagonal lattice with
fixed edge lengths fail to accommodate the Schwarzschild
geometry?  Does this critical radius match r_s = 2GM/c²?

**Motivation:** on a flexible hexagonal lattice with fixed
edges, the Schwarzschild metric demands increasing radial
elongation of hexagons as r → r_s.  The lattice can handle
this in two ways: (1) flexing hexagons to higher aspect
ratios, or (2) inserting pentagonal defects for curvature.
The question is where each mechanism hits its limit.

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

### Gaussian curvature

The 2D Schwarzschild spatial slice (Flamm's paraboloid) has
intrinsic Gaussian curvature:

<!-- K(r) = r_s / (2r³) -->
$$
K(r) = \frac{r_s}{2r^3}
$$

Key values:
- At r = r_s: K = 1/(2r_s²) — **maximum** curvature
- At r = 2r_s: K = 1/(16r_s²) — 8× less
- As r → ∞: K → 0 (flat space)

The curvature is strongest at the horizon and falls off
as 1/r³.

---

## Results

### Approach 1: Hexagon deformation limit

A single hexagon with all 6 edges = 1 can be flexed from
a regular shape (aspect ratio 1.0) to an elongated shape
by pivoting at vertices.

**Finding: the maximum aspect ratio is unbounded.**

The optimizer found R_max ≈ 33 at the edge of its search
range.  Mathematically, the aspect ratio R → ∞ as the
hexagon degenerates to a line (zero area).  Any finite
value is just a numerical artifact.

This means the Schwarzschild coordinate stretch factor
1/√(1 − r_s/r), which diverges at r_s, is ALWAYS within
the hexagon's deformation range.  The "critical radius"
r_crit → r_s trivially because any finite limit, no
matter how large, maps to r ≈ r_s.

**Why this is tautological:** the Schwarzschild stretch
diverges at r_s.  The hexagon can stretch to arbitrary
finite ratios.  So the lattice "fails" arbitrarily close
to r_s — this is just restating that the coordinate
diverges, not discovering anything new.

**The deeper issue:** in proper coordinates (proper
distance along the surface), the geometry near r_s is
smooth and locally flat (equivalence principle).  The
hexagons don't need extreme deformation at all — they
just tile the surface normally, with curvature handled by
pentagonal defects (Approach 2).  The "stretch" is a
coordinate artifact of Schwarzschild coordinates.

**Conclusion:** Approach 1 confirms that the event horizon
is a coordinate singularity, not a physical one.  The
hexagonal lattice has no trouble at r = r_s.

### Approach 2: Pentagon density (Gauss-Bonnet) ← main result

This is the physically meaningful approach.  Curvature on
a hexagonal lattice requires pentagonal defects:

- Regular hexagons: zero Gaussian curvature (flat)
- Each pentagon: deficit angle π/3 (= 60°)
- Gaussian curvature from one pentagon: K = (π/3) / A_face

The required pentagon fraction at radius r:

<!-- f(r) = K(r) × A_hex / (π/3) = 3A_hex r_s / (2π r³) -->
$$
f(r) = \frac{K(r) \cdot A_\text{hex}}{\pi/3}
     = \frac{3 A_\text{hex}}{2\pi} \cdot \frac{r_s}{r^3}
     \approx 1.24 \cdot \frac{r_s}{r^3}
$$

where A_hex = 3√3/2 ≈ 2.598 (regular hexagon, edge = 1).

**The lattice saturates when f = 1 (all faces are pentagons).**

| Quantity | Value |
|----------|-------|
| A_hex (regular, edge=1) | 2.598 |
| Pentagon deficit | π/3 = 60° |
| Coefficient | 3A_hex/(2π) = 1.240 |
| r_crit formula | r_crit = (1.240 × r_s)^(1/3) |

#### Results for various masses

| Mass | r_s (L_P) | r_crit (L_P) | r_crit / r_s |
|------|----------|-------------|-------------|
| 1 Planck mass | 2.0 | 1.35 | **0.68** |
| 10 m_P | 20 | 2.92 | 0.15 |
| 100 m_P | 200 | 6.28 | 0.031 |
| 10⁶ m_P | 2×10⁶ | 135 | 6.8×10⁻⁵ |
| electron | 8.4×10⁻²³ | 4.7×10⁻⁸ | 5.6×10¹⁴ |
| proton | 1.5×10⁻¹⁹ | 5.8×10⁻⁷ | 3.7×10¹² |

**Key observations:**

1. **For astrophysical black holes** (r_s >> 1): the
   pentagon saturation occurs DEEP INSIDE the horizon.
   The lattice comfortably tiles the Schwarzschild
   geometry all the way through the horizon and well
   beyond.  The physical singularity at r = 0 (where
   K → ∞) is where the lattice truly cannot exist.

2. **For Planck-mass objects** (r_s ≈ 2 L_P): the
   pentagon saturation is at 0.68 r_s — inside the
   horizon but close.  The lattice and the horizon are
   both at the Planck scale.

3. **For sub-Planck-mass objects** (electron, proton):
   r_crit >> r_s.  The curvature is so tiny that
   pentagons are not needed anywhere near the object.
   These objects are not black holes — their Compton
   wavelength vastly exceeds their Schwarzschild radius.

4. **Minimum black hole mass:** setting r_crit = r_s:

   <!-- r_s² = 3A_hex/(2π) ≈ 1.24 -->
   $$
   r_s^2 = \frac{3 A_\text{hex}}{2\pi} \approx 1.24
   $$

   → r_s = 1.11 L_P → **M_min ≈ 0.56 Planck masses**

   Below this mass, the lattice cannot produce enough
   curvature to form an event horizon.  This is a
   geometric prediction of the minimum black hole mass.

---

## Interpretation

### The event horizon is NOT a lattice failure

The hexagonal lattice accommodates the Schwarzschild
geometry through the horizon without difficulty:
- In proper coordinates, the geometry is smooth and
  locally flat (equivalence principle)
- Curvature is handled by occasional pentagonal defects
- For astrophysical BHs, the pentagon fraction at the
  horizon is tiny: f(r_s) = 1.24/r_s² ≈ 0 for large r_s

This is **consistent with GR**: the event horizon is a
coordinate singularity (an artifact of Schwarzschild
coordinates), not a physical one.  A freely-falling
lattice observer would not notice anything special at r_s.

### The physical singularity IS a lattice failure

At r = 0, K → ∞ and the required pentagon density
diverges.  The lattice literally cannot exist there.
This IS a physical singularity — consistent with GR's
prediction and with the expectation that quantum gravity
must modify the singularity.

On the hexagonal lattice, the singularity is the point
where the curvature exceeds the lattice's maximum
curvature capacity.  This maximum curvature is set by the
pentagon packing density — a purely geometric quantity.

### Minimum black hole mass ≈ Planck mass

The crossover where pentagon saturation reaches the
horizon is at M ≈ 0.56 m_P.  This is remarkably close
to the Planck mass — the expected scale for the
smallest possible black hole.

This is a genuinely geometric result: the minimum black
hole mass is determined by the hexagonal lattice's
curvature capacity (pentagon density), which depends
only on the edge length (= Planck length).

### Connection to Jacobson's thermodynamic derivation

The Jacobson argument (used in `gravity.md`) derives G
from the Bekenstein-Hawking entropy formula.  This
simulation provides a complementary perspective:

- **Jacobson:** entropy on horizons + thermodynamics → G
- **Pentagon density:** lattice curvature capacity →
  minimum mass for a black hole → G (through r_s = 2GM/c²)

Both give consistent results because both encode the
same physics: the Planck-scale discreteness of spacetime.
The pentagon approach is more geometric; the Jacobson
approach is more thermodynamic.

---

## Files

| File | Purpose |
|------|---------|
| `README.md` | This document |
| `run.py` | Both approaches + combined analysis ✅ |
| `output/hexagon_limit.png` | Approach 1 plots |
| `output/pentagon_density.png` | Approach 2 plots |
| `output/combined.png` | Comparison of both mechanisms |

---

## Dependencies

numpy, scipy, matplotlib (all in project `.venv`)
