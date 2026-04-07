# Track 2: 2D hexagonal sheet in 3D truncated-octahedral lattice

**Status:** Framing

---

## The 3D lattice

The 3D GRID lattice is hypothesized to be the truncated
octahedral honeycomb — the Voronoi tessellation of the BCC
lattice.  It is the only Archimedean solid that tiles 3D by
itself, with all edges constant length.  Each cell has 14
faces (8 regular hexagons + 6 squares), **36 edges**, and
24 vertices.  Each vertex has 4 edges meeting.

The hexagonal faces are oriented perpendicular to the four
⟨111⟩ body diagonals of the underlying cube.  These define
**four discrete face families** — four preferred orientations
for hexagonal cross-sections through the 3D lattice.

A 2D hexagonal material sheet (Ma_e, Ma_p, or Ma_ν)
embedded in this lattice at an arbitrary orientation will
align with the 3D hexagonal faces at specific "magic angles"
and misalign at all other angles.

---

## What to compute

1. **Coincidence rate vs orientation.**  Generate the 3D
   truncated-octahedral lattice vertices.  Generate a 2D
   hexagonal lattice on a plane at orientation (θ, φ).  For
   each hexagonal face in the 3D lattice, check if its 6
   vertices coincide with 2D lattice vertices within δ.
   Sweep (θ, φ) over the full sphere.

2. **Identify the magic angles.**  The perfect-coupling
   orientations are where the 2D sheet lies exactly on a
   ⟨111⟩ hexagonal face family:
   - 4 tilt directions (the ⟨111⟩ normals)
   - 6 twist angles each (hexagonal rotational symmetry)
   - 24 magic orientations (reduced by symmetry)

   At magic angles: every hexagon on the sheet corresponds
   to a hexagonal face of the 3D lattice (perfect coupling).
   Away from magic angles: coincidence drops (partial or
   zero coupling).

3. **The torus integral.**  A torus embedded in the 3D
   lattice has a curved surface.  Different patches face
   different directions.  As you go around the torus, the
   surface normal sweeps continuously through orientations.
   Some patches pass near magic angles (strong coupling),
   most don't (weak or zero coupling).

   The total coupling is the integral over the torus surface:

   > α_eff = (1/A) ∮ C(θ(s), φ(s)) dA

   where C(θ, φ) is the local coincidence rate and the
   integral runs over the torus surface A.

   If C(θ, φ) has sharp peaks at the 24 magic angles and
   is near-zero elsewhere, α_eff measures the fraction of
   torus surface area that passes near a magic angle.  This
   fraction depends on the torus geometry (aspect ratio ε
   and embedding orientation).

   **The hypothesis:** there exists an ε where α_eff = 1/137.
   If so, the fine-structure constant is determined by the
   torus geometry fitting into the 3D lattice — a purely
   geometric origin for α.

---

## The probability framing

For exact coincidence (δ → 0), C(θ,φ) is zero everywhere
EXCEPT at the magic angles, where it's 1.  There is no
intermediate coupling — a hexagonal face either aligns or
it doesn't.  C(θ,φ) is a sum of delta functions on the
orientation sphere.

At finite tolerance δ_angle (the angular width within
which we count as "coupled"), each magic angle becomes a
small cap on the unit sphere.  The 24 magic caps cover a
total solid angle:

> Ω_magic = 24 × π(δ_angle)²

The probability that a random surface element has its
normal within a magic cap is:

> P_magic = Ω_magic / (4π) = 6 × (δ_angle)²

For P_magic = α = 1/137:

> **δ_angle ≈ 0.035 radians ≈ 2.0°**

This is a specific geometric statement: if "good coupling"
means the surface normal is within ~2° of a ⟨111⟩
direction, the probability of coupling at any random
surface point is 1/137.

---

## The torus is not random — it's a specific trajectory

A torus embedded in the 3D lattice has a normal vector
that traces a specific closed curve on the unit sphere
as you go around the tube.  The curve depends on:

- **ε (aspect ratio):** a thin torus (ε → 0) traces a
  narrow band on the sphere.  A fat torus (ε → 1) traces
  a wide band covering more orientations.
- **Embedding orientation:** how the torus axis is aligned
  relative to the ⟨111⟩ directions.

The torus normal crosses through some number of magic caps
as it sweeps around.  The **number of crossings** is an
integer (0, 1, 2, 3, or 4 — one per ⟨111⟩ direction the
trajectory passes near).  The **dwell time** at each
crossing (how long the normal stays inside the cap) is a
smooth function of ε.

This gives α a structure:

> **α = N_crossings × f(ε)**

where N_crossings is discrete (integer: which magic angles
the torus trajectory crosses) and f(ε) is continuous (how
long the normal dwells near each magic angle).

The angles between the four ⟨111⟩ directions are fixed by
the cubic geometry:
- Between any two ⟨111⟩ directions: 70.53° or 109.47°
  (the tetrahedral angle and its supplement)
- These are NOT adjustable — they are set by the truncated
  octahedral lattice geometry

For a torus whose axis is near a ⟨111⟩ direction, the
tube normal sweeps a great circle that passes near the
other three ⟨111⟩ directions at specific angular distances.
Whether it enters their magic caps depends on ε (which sets
the sweep width).

---

## What the computation should determine

1. **Map C(θ,φ)** on the orientation sphere.  Confirm the
   24 magic peaks and measure their angular width (the
   intrinsic δ_angle from the lattice geometry, not a
   chosen tolerance).

2. **Compute the torus normal trajectory** for various ε
   and embedding orientations.

3. **Count crossings and dwell times.**  For each (ε,
   orientation), how many magic caps does the trajectory
   enter?  What fraction of the circumference is inside
   a cap?

4. **Find the ε where the magic fraction = 1/137.**  If
   it exists, α is a geometric output.  If it exists at
   an ε consistent with the electron sheet (~0.5–0.65)
   or the proton sheet (~0.33–0.55), the connection to
   particle physics is direct.

---

## Why this differs from Track 1

Track 1 (2D-in-2D) had no preferred angles — two copies of
the same lattice produce a smooth coincidence function with
no features.  This track has DISCRETE preferred angles (from
the 4 hexagonal face families of the truncated octahedron).
The integral-over-a-torus converts these discrete angles
into a continuous coupling fraction that depends on geometry.

## Why this might work

- The coincidence peaks at magic angles are sharp (exact
  crystallographic alignment), not broad (geometric
  probability)
- The torus sweeps through many orientations, sampling the
  peaks in proportion to its surface area at each angle
- The result is geometry-dependent (different ε gives
  different surface-angle distribution) but not tunable
  (the magic angles are fixed by the lattice)
- If α = 1/137 falls out at a specific ε, that ε is a
  PREDICTION, not an input

**Script:** `track2_3d_lattice.py` (planned)
