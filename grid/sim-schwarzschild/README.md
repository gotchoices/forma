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

## Anatomy of the gravity well

### Terminology

The Schwarzschild radius r_s = 2GM/c² is the radius of
the event horizon.  These are the **same thing** — the
horizon is at r = r_s, which is a sphere of diameter 2r_s.
The gravity well, visualized as Flamm's paraboloid, is a
funnel-shaped surface.  Moving "down" the funnel means
decreasing r toward r_s and then to r = 0.

The shells from outside in:

```
  far away       ~flat, hexagons regular
       ↓
  r ≈ 4 r_s     first detectable deformation (w = √3 L_P)
       ↓
  r ≈ 1.72 r_s  moderate deformation (w = 1.5 L_P)
       ↓
  r ≈ 1.15 r_s  DECOMPOSITION POINT (w = 1 L_P)  ← hexagon
       ↓           loses hexagonal character
  r ≈ 1.03 r_s  NYQUIST POINT (w = 0.5 L_P) ← no circumferential
       ↓           waves possible
  r = r_s        EVENT HORIZON (coordinate singularity)
       ↓           locally smooth in proper coords
  r < r_s        inside the horizon (r and t swap roles)
       ↓           lattice still works
  r = r_crit     PENTAGON SATURATION (lattice curvature limit)
       ↓           deep inside for large BH
  r = 0           SINGULARITY (K → ∞, lattice fails)
```

### Hexagon shape vs position in the gravity well

The Schwarzschild metric stretches hexagons radially by a
factor 1/√(1 − r_s/r).  A hexagon with 6 rigid edges of
length 1 L_P deforms by pivoting at vertices: it gets
taller (radially) and narrower (circumferentially).

The circumferential width w is the key measure:

<!-- w = 2√(1 − (h − ½)²), R = 2h/w -->

| Width w | Stretch R | r / r_s | % outside | Well diam | Character |
|---------|-----------|---------|-----------|-----------|-----------|
| 1.822 (regular) | 1.0 | ≫ 1 | ∞ | — | flat space |
| √3 = 1.732 | 1.15 | 4.00 | 300% | 8.0 r_s | barely deformed |
| 1.5 | 1.55 | 1.72 | 72% | 3.4 r_s | visibly elongated |
| **1.0** | **2.73** | **1.155** | **15.5%** | **2.31 r_s** | **decomposition** |
| 0.5 | 5.87 | 1.030 | 3.0% | 2.06 r_s | Nyquist limit |
| 0.25 | 11.9 | 1.007 | 0.7% | 2.01 r_s | thin sliver |
| 0.1 | 30.0 | 1.001 | 0.1% | 2.00 r_s | effectively 1D |
| → 0 | → ∞ | → 1.0 | 0 | 2.0 r_s | degenerate line |

For a 1-Planck-mass BH (r_s = 2 L_P), the well diameter
in Planck lengths is 2× the r_s values in the last column.

### The decomposition point: w = 1 L_P

At r = (2/√3) r_s ≈ 1.155 r_s (15.5% outside the
horizon), the hexagon's circumferential width equals
one edge length.  Its six edges form:

```
      /\           equilateral triangle (tip = 60°)
     /  \
    /    \
    |    |         unit square (1 × 1)
    |    |
    \    /
     \  /          equilateral triangle
      \/
```

Metrics at this point:
- Area = 1.37 L_P² (72% of regular hexagon)
- Tip angle = 60° (equilateral)
- Aspect ratio R = 1 + √3 ≈ 2.73

This is where the hexagon loses its hexagonal character.
You can't fit another edge across it — one edge spans the
full width.  Below this point, the cell is narrower than
its own edges and transitions to effectively 1D.

For a Planck-mass BH, this occurs at r = 2.31 L_P with
about 15 hexagons around the circumference.  The lattice
is a thin ring of barely-2D cells.

### The Nyquist point: w = 0.5 L_P

At r ≈ 1.03 r_s (3% outside the horizon), two adjacent
cells together span one Planck length.  The shortest
possible circumferential wave (λ = 2 L_P) no longer fits
across two cells.  The lattice cannot support
circumferential oscillations below this point.

For a Planck-mass BH, this is at r = 2.06 L_P — only
0.06 L_P outside the event horizon, with about 26
slivers around the circumference, each half a Planck
length wide.

### Hypothesized "magic" points (none found)

We looked for special behavior at several points that
might have had geometric significance:

| Point | Why we checked | What happened |
|-------|---------------|---------------|
| w = 2 L_P (across-vertices of regular hex) | Naive Nyquist | Not reachable — regular hex already has w = 1.822.  The hexagon is ALWAYS below 2 L_P wide. |
| w = √3 ≈ 1.73 (across-flats of regular hex) | Natural scale | Just mild deformation at r = 4 r_s.  Nothing special. |
| w = r_s | Schwarzschild diameter matching | Would require r_s-dependent analysis; not a universal geometric point. |

No discrete "snap" was found — the deformation is smooth
and continuous from regular hexagon down to degenerate
line.  The decomposition (w = 1) and Nyquist (w = 0.5)
points are the most physically meaningful thresholds.

### The hexagon as a low-pass filter

A regular hexagonal cell in flat space is already at its
own resolution limit: its width (1.822 L_P) is less than
2 edge lengths.  There is nothing finer in the lattice to
"see" the hexagon's internal structure.

This means the hexagonal cell is a **built-in low-pass
filter**.  Each edge carries an internal string with
standing-wave modes (the phase, gauge connection, and
higher harmonics from the string-register model in
[sim-gravity-2](../sim-gravity-2/)).  Those internal
modes have structure at scales much finer than L_P — the
internal string length L_compact can be enormously larger
than L_P (it is the Compton wavelength, which for an
electron is 10¹⁹ L_P).

But the grid-scale physics — wave propagation, curvature,
scattering — cannot resolve any of that internal structure.
The hexagonal cell hides the string accounting from the
macroscopic lattice, just as a pixel hides its subpixel
circuitry from the image.

This separation of scales is not imposed — it follows
from the lattice geometry.  The hexagon's width-to-edge
ratio (1.822:1) is close to but less than 2:1 (Nyquist).
The lattice is operating at the edge of its own resolution
even in flat space.  Under Schwarzschild deformation, the
cells get narrower and the filtering gets stronger until,
at w = 0.5 L_P, even two cells together can't resolve a
wavelength.

### Is the Planck length fundamental or a knob?

In the GRID framework, the Planck length enters through
the gravity derivation (Jacobson's argument): the
Bekenstein-Hawking entropy formula S = A/(4L_P²) fixes
the lattice spacing at L_P.  This connects the Planck
length to information content — specifically to ζ = 1/4
(bits per Planck cell from 3D tetrahedral packing).

But the hexagon deformation analysis reveals that the
Planck length sets a **scale**, not a hard boundary.  The
thresholds at w = 1 L_P and w = 0.5 L_P are smooth
transitions, not walls.  The hexagon doesn't "break" at
any point — it smoothly degenerates from a 2D cell to a
1D sliver to a line.

If the Planck length were changed (equivalently, if ζ
were changed), all the thresholds would move proportionally
but the structure would be the same.  The Planck length is
the knob that sets where the 2D → 1D transition occurs
relative to the Schwarzschild radius, but the transition
itself is a smooth geometric consequence, not a
fundamental discontinuity.

This is consistent with the general GRID picture: the
Planck length is a derived quantity (from ζ and G), not a
built-in minimum length.  The lattice is discrete, but the
discreteness scale is a consequence of the information
content of spacetime, not a postulate.

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
