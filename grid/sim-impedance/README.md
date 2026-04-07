# sim-impedance: Lattice junction coincidences

**Status:** Track 1 complete.  See findings below.

**Question:** when two lattices of different orientation
intersect, how often can nodes from each lattice be
interconnected by an edge of exactly one lattice spacing?
Does the coincidence rate relate to the fine-structure
constant α ≈ 1/137?

**Motivation:** the [alpha-in-grid](../../primers/alpha-in-grid.md)
primer frames α as the impedance mismatch between the 2D
material sheet (Ma) and the 3D spatial lattice (S).  A
particle's Coulomb energy is α times its Compton (wave)
energy — only 1/137 of the internal standing-wave energy
couples through the junction into the ambient grid.  This
simulation asks whether that fraction has a geometric origin
in the lattice structures themselves.

The idea: two lattices at a relative angle will have occasional
**coincidence pairs** — nodes from lattice A that sit exactly
one edge-length from a node in lattice B.  If the coincidence
rate, compared to the fully-connected density of an intact
lattice, yields a ratio near α, that would give α a concrete
geometric meaning.

---

## Approach

### What we measure

For two lattices overlapping in the same region of space:

1. **Coincidence count** — the number of cross-lattice node
   pairs separated by distance L ± ε (where L is the lattice
   spacing and ε is a small tolerance).

2. **Coincidence rate** — coincidences per node of lattice A,
   normalized by the number of nearest neighbors in an intact
   lattice.  This gives a dimensionless ratio: "what fraction
   of a node's potential connections actually reach across to
   the other lattice?"

3. **Periodicity** — do the coincidences form a regular
   pattern (a superlattice)?  If so, what is the period
   relative to L?  This superlattice spacing, if it exists,
   is the characteristic scale of inter-grid coupling.

### The comparison baseline

In an intact 2D triangular lattice, every node has **6 nearest
neighbors**, all at distance exactly L.  The coincidence rate
is measured against this fully-connected baseline.  If a node
on lattice A finds, on average, 6/137 ≈ 0.044 valid cross-
connections to lattice B, that would be suggestive.

---

## Tracks

### Track 1: Two 2D triangular lattices, rotated

The simplest case.  Two triangular lattices in the same plane,
both with edge length L = 1, rotated by angle θ relative to
each other.  Sweep θ from 0° to 30° (the symmetry period of
the triangular lattice).

**What to look for:**
- Coincidence rate vs angle θ
- Whether specific angles produce sharp peaks (CSL angles)
- Whether any peak or characteristic rate lands near 1/137
- The spatial pattern of coincidences (superlattice structure)

Script: [`track1_planar_rotation.py`](track1_planar_rotation.py)

**Track 1 findings:** the coincidence rate settles into a flat
band around 1/20 to 1/25 of intact coordination for most angles,
well above 1/137.  The rate scales linearly with tolerance ε
(no exact coincidences at generic angles), meaning the result
is dominated by geometric probability (annular area × node
density), not lattice-specific commensurability.  The spatial
patterns DO show periodic superlattice structure (coincidence
site lattices), but the raw rate is too high by ~6× to match α.
Conclusion: a purely mechanical/geometric coincidence count in
2D-to-2D does not produce α.  See output/ for plots and data.

### Track 2: 2D hexagonal sheet in 3D truncated-octahedral lattice

**Status:** Framing

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

**What to compute:**

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

### The probability framing

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

### The torus is not random — it's a specific trajectory

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

### What the computation should determine

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

**Why this differs from Track 1:**

Track 1 (2D-in-2D) had no preferred angles — two copies of
the same lattice produce a smooth coincidence function with
no features.  This track has DISCRETE preferred angles (from
the 4 hexagonal face families of the truncated octahedron).
The integral-over-a-torus converts these discrete angles
into a continuous coupling fraction that depends on geometry.

**Why this might work:**

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


### Track 3: Discrete embedding — hexagonal rings on a 3D lattice

**Status:** Framing

Track 2 treats the lattice as a continuum with smooth
angular dependence.  Track 3 goes to the foundation:
everything is discrete at the Planck scale.  Every edge
is exactly L.  There is no tolerance δ — either two nodes
are one Planck length apart or they aren't connected.

The question: at what DISCRETE angles can a 2D hexagonal
structure share nodes with a 3D lattice, when all edges
are constrained to length exactly L?

#### The premise

In the 3D lattice (diamond cubic or truncated octahedral
vertex graph), each node has 4 edges at tetrahedral angles
(109.47° between any pair).  In the 2D hexagonal lattice,
each node has 3 edges at 120°.

These angles are DIFFERENT (109.47° vs 120°).  At "magic
angle 0" (a hexagonal face of the truncated octahedron),
the 2D and 3D hexagons align perfectly — all 6 nodes
coincide, all edges match.  An arbitrarily small rotation
away from this angle gives ZERO coupling — not "weak"
coupling, but exactly zero, because at the Planck scale
there is no "almost aligned."

But at some specific FINITE rotation, a new alignment
occurs: at least one edge in lattice A lies exactly on top
of an edge in lattice B.  This is the "first angle" —
the smallest rotation from magic angle 0 where any
coupling occurs.  It won't be a full 6-edge hexagonal
match — it might be just 1 or 2 shared nodes.  But it's
nonzero.

#### What the discrete picture predicts

A discrete staircase of coupling levels:

| Coupling level | Shared nodes | Description |
|---------------|-------------|-------------|
| 0 | 0 | Generic angle — zero coupling, the sheets are decoupled |
| 1 | 1 edge (2 nodes) | First angle — minimal partial coupling |
| 2 | 2 edges (3 nodes) | Second angle — partial coupling |
| 3 | 3 edges (forming a triangle) | Half-hexagon coupling |
| ... | ... | ... |
| 6 | Full hexagon (6 edges, 6 nodes) | Magic angle — perfect coupling |

The angles at which each level occurs are FIXED by the
lattice geometry.  They are not tunable.  And crucially:
the number of angles at each level and the energy cost
per level may determine α.

**The hypothesis:** α is the ratio of "partially coupled
angles" to "total possible angles" on the discrete lattice.
Or equivalently: α is the probability that a random
discrete orientation has at least one shared edge between
the 2D and 3D lattices.

#### Tracks 3a–3c

**Track 3a: Single hexagonal ring.**  Can a hexagonal ring
of 6 edges (length L each) embed in the 3D lattice?  At
how many orientations?

Method: enumerate all sets of 6 lattice nodes in the 3D
lattice that form a regular hexagon of edge length L.
Count the distinct orientations.  These are the magic
angles.

This is a pure combinatorial search on a small region of
the 3D lattice (~10³ nodes).  Hours of computation at most.

**Track 3b: Partial matches.**  For each possible relative
orientation of the two lattices (discretized by the 3D
lattice geometry), count how many node-node coincidences
exist within a patch of ~100 cells.

Record: at each discrete angle, how many nodes from the
2D hexagonal lattice coincide with 3D lattice nodes?
How many shared edges?  How many complete hexagons?

Map the "coupling staircase" — the discrete set of angles
and their coupling levels.  Identify:
- The first angle (minimum nonzero coupling — 1 shared edge)
- The spacing between successive coupling levels
- How many angles produce 1, 2, 3, 4, 5, 6 shared edges
- Whether the low-coupling angles (1-2 shared edges)
  outnumber the high-coupling angles (5-6 shared edges)
  by a factor related to α

**Track 3c: Small tori.**  Build the smallest possible
torus from discrete edges (a hexagonal tube ring +
connecting edges) and attempt to embed it in the 3D
lattice at each valid orientation from Track 3b.

At each torus size (measured in Planck edges), count:
- M(N) = number of valid embedding orientations
- T(N) = total number of discrete orientations attempted

The ratio M(N)/T(N) is a discrete approximation to the
coupling fraction.  As N grows (larger torus, more
possible angles), the discrete set grows denser and
M/T should converge to a limit.

**The prediction:** M(N)/T(N) → α = 1/137 as N → ∞.

If this converges, α is derived from the discrete
geometry of hexagonal structures embedded in the
3D truncated-octahedral (or diamond cubic) lattice.
No free parameters.  No measured inputs.  Pure
combinatorial geometry.

#### Why this might be the most fundamental computation

Track 1 failed because 2D-in-2D has no preferred angles.
Track 2 (continuum) introduces preferred angles from the
3D lattice but works in the smooth approximation.  Track 3
works at the actual Planck-discrete level where the lattice
lives.

If α emerges from Track 3, it is the MOST fundamental
derivation possible: a pure integer-geometry ratio from
the way hexagons fit into the 3D lattice.  No physics,
no dynamics, no fields — just counting.

#### The diamond lattice alternative

The truncated octahedron describes the CELLS.  But GRID
is defined by EDGES (links carrying the gauge connection).
The relevant structure may be the edge graph — the diamond
cubic lattice, where each node has 4 edges at tetrahedral
angles (109.47°) with all edges equal length.

The diamond lattice and the truncated-octahedral vertex
graph are closely related (both are 4-connected with all
edges equal).  Track 3a should test BOTH: embed hexagonal
rings in the diamond lattice and in the truncated-
octahedral vertex graph.  If they give different results,
the choice of 3D lattice matters.  If they agree, the
specific cell shape is irrelevant — only the vertex
connectivity counts.

**Script:** `track3_discrete_embedding.py` (planned)


### Track 4: Rational-angle coincidence site lattices (abandoned)

For specific rational rotation angles, exact coincidences
form a periodic superlattice (the CSL).  Enumerate the CSL
angles for the triangular lattice and compute their Σ values
(the ratio of superlattice cell area to original cell area).
Check whether Σ = 137 or a related value appears.

---

## What we learned

### The mechanical picture doesn't work

Track 1 tested the most direct version of the hypothesis:
count how often two lattices can physically interconnect, and
see if the rate is 1/137.  The answer is no — the coincidence
rate is ~1/20 of intact coordination, dominated by simple
geometric probability (how much annular area at distance L
contains nodes of the other lattice).  The rate scales linearly
with tolerance ε, has no special angle dependence, and carries
no lattice-specific signature beyond the node density.

A mechanical linkage — counting which nodes CAN connect — asks
the wrong question.  It measures geometric opportunity, not
physical cost.

### The right question is thermodynamic, not geometric

The phrase "defect cost" is thermodynamics language.  In
condensed matter physics, a defect cost is the **free energy
penalty** for introducing a topological defect (a vortex, a
dislocation) into an ordered medium.  It is not about how many
sites could geometrically hold a defect — it is about how much
energy the medium must store to accommodate one.

GRID already answers this question.  The Maxwell derivation
([maxwell.md](../maxwell.md), Step 5) gives the lattice action
with coupling constant κ = 1/(4πα) ≈ 1722.  The energy stored
in a minimal vortex — one 2π phase winding — is proportional
to κ, i.e. proportional to **1/α**.  This is the defect cost,
derived directly from the axioms.

### Alpha as energy partition

Consider a particle: a standing wave of energy mc² on the 2D
material sheet, whose phase winds through 2π (a topological
defect in the ambient 3D lattice).  The energy partitions
between two locations:

| Where | Energy | What it is |
|-------|--------|------------|
| On the sheet | mc² | The standing wave — the particle's mass |
| In the ambient lattice | αmc² | The Coulomb field — the energy cost of maintaining the 2π winding in the surrounding medium |

The fraction of total energy that radiates into the ambient
lattice as Coulomb field is:

<!-- α / (1 + α) ≈ α -->
$$
\frac{\alpha}{1 + \alpha} \approx \alpha
$$

This is exact.  The Coulomb self-energy of a charge e at the
Compton radius ƛ_C is e²/(4πε₀ƛ_C) = αmc².  The ratio
E_Coulomb / E_wave = α.

### What α is, physically

Alpha is not a geometric coincidence rate.  It is a
**thermodynamic partition ratio** — the fraction of a
topological defect's total energy that the ambient medium
must store to accommodate the twist.

In the GRID + MaSt picture:

- A particle is a 2π phase winding on a 2D sheet
- The winding is a topological defect in the ambient 3D lattice
- The lattice action (axiom A6) sets the energy cost of such
  a defect at κ = 1/(4πα) per unit of field strength squared
- The resulting Coulomb field carries energy αmc², while the
  wave itself carries mc²
- Alpha is the ratio: **how much energy does the defect leak
  into the surrounding medium, relative to the energy of the
  wave that created it?**

This reframes α from a mysterious measured constant to a
physically interpretable quantity: the energy tax that the
ambient lattice levies on a topological defect.  The value
1/137 is a free parameter — it is likely not derived from the lattice
geometry (as the compact-dimensions study and this simulation
both confirm).  But its *meaning* is clear: it is the coupling
efficiency between the 2D material sheet and the 3D spatial
lattice, expressed as an energy fraction.

The mechanical simulation was worth running because it ruled
out the simplest geometric explanation and pointed toward the
thermodynamic one.  The answer was already in the action
principle — we just needed to read it as a defect cost rather
than a coupling constant.

---

## Files

| File | Contents |
|------|----------|
| [track1_planar_rotation.py](track1_planar_rotation.py) | Track 1: sweep rotation angle, measure coincidence rate |
| [output/](output/) | Plots and data |
