# Hexagonal vs triangular lattice: the wye substrate

**Status:** Conceptual — emerged from sim-maxwell analysis.

---

## The observation

When you draw the triangular lattice on paper, two distinct
tilings emerge from "3 connections per node":

### Delta configuration (triangular lattice)

The primary unit is a **triangle**.  Three edges form a
closed face.  The result is:

- **Face:** triangle (3 edges)
- **Vertex coordination:** N = 6 (six triangles meet at
  each vertex)
- **Property:** RIGID — a triangle cannot deform with
  fixed edge lengths (the triangle inequality locks it)
- **To bend:** must shear and rewire (break/reform edges)

```
    ╱╲╱╲╱╲╱╲
   ╱╲╱╲╱╲╱╲╱
  ╱╲╱╲╱╲╱╲╱╲
```

### Wye configuration (hexagonal/honeycomb lattice)

The primary unit is a **Y-junction** — three edges meeting
at 120°.  No triangular face.  The result is:

- **Face:** hexagon (6 edges)
- **Vertex coordination:** N = 3 (three edges meet at
  each vertex)
- **Property:** FLEXIBLE — hexagons can shear, stretch,
  and bend with fixed edge lengths
- **To bend:** just deform the angles (edges stay intact)

```
   ╱ ╲ ╱ ╲ ╱
  │   │   │
   ╲ ╱ ╲ ╱ ╲
    │   │   │
   ╱ ╲ ╱ ╲ ╱
```

These two are **duals** of each other.  The triangular
lattice's faces are the hexagonal lattice's vertices, and
vice versa.  Same topology, different emphasis.

---

## Why hexagonal might be the right substrate

### 1. Flexibility with fixed edges

The triangular lattice is a rigid truss — it resists
deformation.  This is why sim-gravity's spring lattice gave
elastic behavior (1/r² strain), not gravitational behavior
(1/r force).

The hexagonal lattice is flexible.  With fixed edge lengths,
you can:
- Shear individual hexagons (change angles without
  changing lengths)
- Roll the sheet into a cylinder (carbon nanotube)
- Introduce curvature by replacing hexagons with pentagons
  (fullerene/buckyball)
- Stretch into a funnel shape (gravity well)
- Compress into a bubble (compact dimension)

This is exactly the structural vocabulary needed for:
- **Gravity wells** tapering down to the Schwarzschild
  radius (funnel embedding)
- **Compton bubbles** — compact surfaces perpendicular to
  the well, at the Compton wavelength scale

The dual-bubble conservation law λ_C × r_s = 2L_P²
(see [dual-bubbles.md](dual-bubbles.md)) links these two
shapes.  A flexible lattice that can assume both shapes
from the same substrate is suggestive.

### 2. True nanotube geometry

Carbon nanotubes are rolled hexagonal lattices (graphene
sheets).  This is not a coincidence of analogy — it's the
same geometry.  If the Planck-scale substrate is hexagonal,
then MaSt's compact dimensions (2D material sheets rolled
into tubes) are literally Planck-scale nanotubes.

The wrapping analysis in
[compact-dimensions.md](compact-dimensions.md) used
triangular lattices.  With a hexagonal lattice, the
wrapping vectors and discrete α spectrum would be
different.  Worth investigating.

### 3. Better scattering for wave propagation

The junction scattering matrix for N equal-impedance strings
at a vertex is:

<!-- S_ij = 2/N (i≠j),  S_ii = 2/N - 1 -->
$$
S_{ij} = \frac{2}{N} \quad (i \neq j), \qquad
S_{ii} = \frac{2}{N} - 1
$$

| Property | Triangular (N=6) | Hexagonal (N=3) |
|----------|-----------------|-----------------|
| Reflection amplitude | −2/3 | **−1/3** |
| Transmission (each) | 1/3 | **2/3** |
| Energy reflected | 44% | **11%** |
| Energy transmitted | 56% (split 5 ways) | **89%** (split 2 ways) |
| Energy per transmitted edge | 11% | **44%** |

The hexagonal junction transmits **4× more energy** per
outgoing edge than the triangular junction.  Waves should
propagate much more cleanly with less scattering loss.

The zigzag-circulation hypothesis (from
[sim-maxwell/README.md](sim-maxwell/README.md)) changes too:
- Triangular: circulation is around 3-edge triangular
  plaquettes; 5 outgoing paths; complex interference
- Hexagonal: no triangular plaquettes; circulation is
  around 6-edge hexagonal faces; only 2 outgoing paths
  at each vertex (forward-left or forward-right); the
  zigzag is more direct

With only 2 choices at each junction, the wave propagation
becomes simpler and more directional — energy has fewer
paths to scatter into.

### 4. Curvature from topological defects

A flat hexagonal lattice tiles the plane.  Curvature comes
from **topological defects**:

- **Pentagon (5 edges):** positive curvature (convex).
  Twelve pentagons close a sphere (C₆₀ fullerene /
  soccer ball pattern).
- **Heptagon (7 edges):** negative curvature (saddle).
  Heptagons create hyperbolic surfaces.

This is exactly how Regge calculus encodes spacetime
curvature — deficit angles at vertices/edges.  In the
hexagonal picture, curvature is discrete and topological:
the number and distribution of pentagonal/heptagonal defects
determines the geometry.

**Gravity as pentagonal defects:** a mass creates a
concentration of pentagonal defects in the hexagonal
lattice, curving spacetime inward.  The Schwarzschild
geometry is a funnel of increasing pentagonal density
toward the center.

**Compact dimensions as closed hexagonal surfaces:** a
Compton-scale torus is a rolled hexagonal sheet.  Its Euler
characteristic (V − E + F = 0 for a torus) constrains the
defect count.  A sphere (V − E + F = 2) requires exactly
12 pentagonal defects (Euler's theorem) — the minimum
curvature configuration.

### 5. Three edges = ζ connection

In the wye picture, each vertex has 3 edges.  Under Model B
(cell = its edges, no self), a vertex's state is carried by
its 3 edge strings:

- 3 edges → 3 neighbors → **ζ = 1/3** (2D hexagonal)

For a 3D analog (tetrahedrally coordinated vertices, like
diamond crystal structure): 4 edges → **ζ = 1/4**
(Bekenstein-Hawking).

This recovers the same ζ values as the simplex counting but
from the vertex-coordination perspective instead of the
face-counting perspective.

---

## Triangular vs hexagonal: what changes?

| Aspect | Triangular | Hexagonal |
|--------|-----------|-----------|
| Vertex coordination | 6 | **3** |
| Smallest face | Triangle (3) | Hexagon (6) |
| Rigidity (fixed edges) | Rigid | **Flexible** |
| Curvature mechanism | Edge removal? | **Pentagonal defects** |
| Scattering reflection | 44% energy | **11% energy** |
| Wave propagation | Works (sim-maxwell) | Should be cleaner |
| Carbon analog | — | **Graphene / nanotubes** |
| Model B: ζ (2D) | 1/3 (from face count) | 1/3 (from vertex coordination) |
| Rolling into tubes | Possible | **Natural** (actual nanotube geometry) |

---

## Simulation results: hexagonal vs triangular

Ran sim-maxwell on the honeycomb lattice (N=3) with the same
junction scattering rule.  See `sim-maxwell/run_hex.py`.

### Single-edge pulse — the key result

| | Hexagonal (N=3) | Triangular (N=6) | Isotropic |
|---|---|---|---|
| **Directionality** | **0.532** | 0.235 | 0.333 |

On the hexagonal lattice, even a **single edge pulse**
propagates forward (directionality > isotropic).  On the
triangular lattice, single pulses scatter backward.  This is
a qualitative difference: with N=3, each junction transmits
2/3 to each of 2 outgoing edges — the forward path gets
most of the energy.  With N=6, each junction transmits 1/3
to each of 5 edges — energy is diluted.

### Wavefront propagation

| Quantity | Hexagonal | Triangular |
|----------|----------|-----------|
| Speed (width=5) | 0.73 | 0.71 |
| Directionality (width=5) | 0.46 | 0.03* |
| Energy conservation | 1.00000000 | 1.00000000 |

*Triangular's low wavefront directionality is a metric
artifact for wide wavefronts; its narrow-pulse directionality
is 0.94.

### Width dependence

| Width | Hex dir | Hex speed | Tri dir | Tri speed |
|-------|---------|----------|---------|----------|
| 1 | 0.48 | 0.56 | 0.94 | 0.69 |
| 5 | 0.49 | 0.59 | 0.85 | 0.70 |
| 20 | 0.43 | 0.59 | 0.56 | 0.70 |

The hexagonal lattice has **more consistent** directionality
across widths (~0.43–0.50) while the triangular drops from
0.94 to 0.56.  The triangular is more directional for narrow
pulses; the hexagonal is more uniform.

### Interpretation

Both lattices support directional wave propagation.  The
hexagonal lattice's main advantage is **single-pulse forward
propagation** — individual wavelets transmit forward, not
backward.  This is more physical: a photon (single quantum)
should propagate, not scatter backward.

The triangular lattice achieves higher directionality for
coherent wavefronts (Huygens' principle), but individual
wavelets scatter backward.  The hexagonal lattice doesn't
need Huygens' principle as strongly because each individual
junction favors forward transmission.

---

## What this suggests

1. **The hexagonal lattice is the better substrate for single
   quanta.**  A photon is a localized excitation, not an
   infinite wavefront.  The hexagonal junction naturally
   propagates single excitations forward.

2. **Investigate hexagonal lattice for compact-dimensions.**
   The wrapping vectors for a hexagonal lattice are
   different from a triangular lattice.  The discrete α
   spectrum may change.

3. **Model gravity as pentagonal defect density.**  This
   could bridge the gap between the Jacobson thermodynamic
   argument (which works on any smooth manifold) and the
   discrete lattice (where curvature is topological).

4. **The dual-bubble embedding.**  A hexagonal sheet that
   can flex into both a funnel (gravity well) and a tube
   (compact dimension) from the same substrate, connected
   at the Planck scale — this is the geometric realization
   of λ_C × r_s = 2L_P².

---

## Intrinsic invisibility of curvature

### The key insight

The junction scattering rule depends ONLY on:
1. **N** — the number of edges at the vertex (topological)
2. **The amplitudes** — the current state on each edge

It does NOT depend on:
- The angles between edges
- The curvature of the surface
- The embedding in higher dimensions
- Whether the sheet is flat, rolled, or stretched

A wave propagating on a hexagonal lattice **cannot detect**
whether the surface is flat, rolled into a tube, or pulled
into a funnel.  The bending is perpendicular to the 1D
strings — in a direction they have no degree of freedom to
measure.

### What the wave CAN detect

1. **Topology (global):**  if the wave goes around a loop
   and meets itself, it detects the periodicity.  On a
   torus, this creates quantized wavelengths — the discrete
   spectrum of standing waves on a finite loop.  This is
   exactly how MaSt generates particle properties (mass from
   compactification, charge from winding).

2. **Topological defects (local):**  if a vertex has N ≠ 3
   (a pentagonal or heptagonal face), the scattering changes.
   The wave sees a different junction rule at that vertex.
   These defects carry curvature and ARE detectable.

### What the wave CANNOT detect

Smooth bending — the kind that rolls a flat sheet into a
tube or stretches it into a funnel — is invisible, provided
the connectivity is unchanged (no defects introduced).  The
hexagons flex, the embedding angles change, but the junction
rule is unaffected.

### Consequence for compactification

**Compactification is free.**  Rolling a hexagonal sheet into
a torus costs no energy and produces no detectable
deformation inside the torus.  The "tube" shape is an
artifact of the 3D embedding.  From inside, the torus is
just a flat hexagonal lattice that happens to be periodic in
two directions.

This gives a clean separation of physics:

| Domain | What the wave sees |
|--------|-------------------|
| **Inside the torus (Ma)** | Flat hexagonal lattice, periodic BCs → quantized spectrum → particle properties |
| **Outside in 3D (S)** | Hexagonal lattice with pentagonal defects → curvature → gravity |

Inside the Ma torus, there is no deformation the energy can
detect.  The compact dimensions are intrinsically flat — all
curvature effects are in the embedding (the ambient S
lattice).

### Consequence for gravity

The ambient 3D lattice must accommodate the topological
object (the torus).  This forces the surrounding hexagonal
lattice to deform.  Since the lattice is flexible (hexagons
can flex with fixed edges), the deformation is smooth far
from the torus.  But close to the torus, pentagonal defects
appear — vertices where N drops from 3 to 2 (or faces
change from hexagons to pentagons).

These defects create positive curvature.  Their distribution
IS the Schwarzschild geometry:
- Far from the mass: mostly hexagons (flat space)
- Near the mass: increasing pentagon density (curvature)
- At the Schwarzschild radius: maximum defect density

The gravity well is not a deformation of the torus — it's a
deformation of the **surrounding lattice** to accommodate the
torus's topological presence.

### The equivalence principle on the lattice

Every vertex with N = 3 has the same scattering rule.  The
wave at any single vertex cannot tell whether it's in flat
space or in a gravity well.  Gravity is not a local property
— it's the global pattern of how vertices connect and where
defects appear.

This is Einstein's equivalence principle: locally, physics is
the same everywhere.  Only by measuring the distribution of
defects (geodesic deviation on the lattice) can you detect
curvature.

---

## Schwarzschild shearing: the event horizon as lattice failure

### The asymmetry

The Compton torus (Ma) is intrinsically flat.  Rolling a
hexagonal sheet into a torus doesn't strain the lattice
because the bending is extrinsic — invisible to the waves
propagating on it.  The torus is topology, not strain.

The Schwarzschild funnel (the gravity well in the
surrounding S lattice) is different.  The Schwarzschild
metric demands increasing radial stretching as r → r_s:

<!-- g_rr = 1/(1 − r_s/r) -->
$$
g_{rr} = \frac{1}{1 - r_s / r}
$$

As r → r_s, g_rr → ∞.  The metric demands infinite
proper distance per unit coordinate distance in the
radial direction.

### The lattice limit

On a hexagonal lattice with fixed edge lengths L = L_P,
infinite stretching is impossible.  The hexagons become
increasingly elongated radially, but with fixed edges,
there's a maximum aspect ratio a hexagon can achieve.

The critical point: when the Schwarzschild geometry demands
more radial elongation than the hexagonal lattice can
provide, **the lattice fails**.  Edges must disconnect and
reconnect — a topological shear.

This shearing IS the event horizon.  It's not a coordinate
artifact (as in GR, where the horizon is regular in free-fall
coordinates) — it's a genuine **topological phase transition**
where the lattice connectivity changes.

### What shearing produces

When the lattice shears:
- Edges disconnect radially (no more hexagons spanning
  across the critical radius)
- The interior lattice disconnects from the exterior
- Information cannot cross the shear boundary (the lattice
  doesn't connect through it)
- This is a discrete, physical event horizon

Inside the shear, the lattice may reconnect in a different
topology (a closed interior lattice — perhaps another torus,
or a structure collapsing to the central Ma torus).

### Connection to G

If the shearing occurs at a computable critical curvature
K_max, set by the geometry of the hexagonal lattice (the
maximum Gaussian curvature a hexagonal mesh with unit edges
can sustain), then:

- K_max is a geometric constant (derivable from the lattice)
- The Schwarzschild curvature at radius r is
  K(r) ∝ M / r³ (Kretschner invariant)
- The shearing radius r_shear satisfies K(r_shear) = K_max
- This gives r_shear ∝ M^(1/3) × (something depending on
  K_max)

But the Schwarzschild radius is r_s = 2GM/c².  Matching
r_shear to r_s would give a relationship between G and
K_max — potentially deriving G from lattice geometry in a
way that doesn't rely on the Jacobson thermodynamic argument.

**Status:** this is speculative.  The critical step is
computing K_max for the hexagonal lattice.  The Kretschner
curvature also involves more complex tensor structure in 3D+1
than just Gaussian curvature.  But the geometric intuition
is sound: the lattice has a maximum curvature, and that
maximum determines where gravity becomes "too strong" for
the lattice to hold.

### Testing periodicity of space

The hexagonal lattice picture raises the question: is all
space periodic?  If the 3D S lattice is itself a large torus,
this would be consistent with the framework.

**Observable signatures of a toroidal universe:**

1. **Matched circles in the CMB:**  light from the big bang
   arriving via different topological routes creates matching
   patterns.  Searched by Planck satellite — no matches found.
   Lower bound: periodic dimension > ~90 billion light-years
   (if it exists).

2. **Suppressed large-scale power:**  a finite universe
   can't support wavelengths larger than itself.  The CMB
   does show anomalously low power at the largest scales
   (the "quadrupole anomaly") — suggestive but inconclusive.

3. **No local test.**  A torus is seamless — no edges, no
   boundaries.  The local geometry is identical to infinite
   flat space everywhere.  The only detection method is
   finding copies (the same object seen from different
   topological routes).  For cosmological-scale periodicity,
   this requires observations spanning the entire universe.

**At the Planck scale:**  the compact dimensions of MaSt
ARE periodic, and their signature is the quantized particle
spectrum (masses, charges).  This is the "local test" for
Planck-scale periodicity — the discreteness of particle
properties.

**At the cosmological scale:**  currently unresolved.  The
framework is compatible with a toroidal 3D universe but does
not require it.

---

## Relationship to existing GRID documents

- **[lattice-geometry.md](lattice-geometry.md):** discusses
  simplicial (triangular/tetrahedral) lattices.  The
  hexagonal lattice is the dual — same topology, different
  tiling.  Both should be tracked as candidates.

- **[compact-dimensions.md](compact-dimensions.md):** the
  wrapping analysis used triangular lattices.  A hexagonal
  version would change the discrete α spectrum.

- **[dual-bubbles.md](dual-bubbles.md):** the gravity-well /
  Compton-bubble duality could be realized as deformations
  of a flexible hexagonal sheet.

- **[sim-maxwell/](sim-maxwell/):** the current simulation
  uses triangular lattice (N=6).  A hexagonal version (N=3)
  is a natural follow-up.

- **[INBOX.md](INBOX.md):** the graphene analogy and
  nanotube connection were noted there; this document
  develops them further.
