# Track 9: Junction escape fraction

**Status:** Complete.  See [F9-junction-escape.md](F9-junction-escape.md).

**Premise:** at a single Y-junction on a curved torus, the
three edges are not coplanar.  A unit signal arriving on one
edge cannot be fully decomposed into the two outgoing edge
directions — there is a geometric residual that escapes the
plane of the outgoing edges.  This "escape fraction" is a
pure geometric quantity: no wave model, no global mode, no
integration.  Just one junction, one impulse, one number.

**Key distinction from Track 8:**

| Track 8 | Track 9 |
|---------|---------|
| Global CP mode on full torus | Single junction, one node |
| Integrates over surface (θ₂ kills it) | No integral — local computation |
| Requires wave model (CP field) | No wave model — unit impulse |
| Result: zero (orthogonality) | Result: a definite nonzero number |

---

## Physical picture

On a flat hexagonal sheet, three edges at a Y-junction are
coplanar (all in the 2D plane).  An incoming vector along ê₁
can be fully decomposed into the plane spanned by ê₂ and ê₃:

    ê₁ = a₂ê₂ + a₃ê₃ + 0    (escape = 0)

On a curved torus, the three edges connect to neighbors at
different points on the curved surface.  The edge directions
in 3D are NOT coplanar — ê₁ has a component perpendicular to
the plane spanned by ê₂ and ê₃:

    ê₁ = a₂ê₂ + a₃ê₃ + e_esc    (escape ≠ 0)

The escape component is:

    e_esc = (ê₁ · n̂₂₃) × n̂₂₃

where n̂₂₃ = (ê₂ × ê₃) / |ê₂ × ê₃| is the normal to the
plane of the outgoing edges.

The **escape fraction** is:

    f_esc = |e_esc|² = (ê₁ · n̂₂₃)²

This is the fraction of the incoming signal energy that
geometrically cannot follow the outgoing edges.

---

## Two lattice mappings

### Method A: Equal edge lengths (physical)

All edges have the same length L.  When wrapped onto the torus,
the hexagons must distort — angles change, hexagons squish in
the regions of higher curvature (inner equator).  This is more
physical: in GRID, all lattice edges are one Planck length.

### Method B: Conformal mapping (stretched)

Keep the 2D hexagons regular.  Map coordinates (θ₁, θ₂) onto
the torus surface.  Edges on the outer half of the tube are
longer (stretched) and edges on the inner half are shorter
(compressed).  Edge lengths vary by the metric factor
p = 1 + ε cos θ₁.

Both methods should be tested.  If the escape fraction is
the same for both, it's a topological quantity.  If different,
it depends on the embedding details.

---

## Algorithm

For each node on the torus:

1. Compute the 3D positions of the node and its 3 neighbors
2. Compute the 3D unit edge directions: ê₁, ê₂, ê₃
3. For each choice of "incoming" edge (3 choices):
   a. Compute the normal to the outgoing plane:
      n̂_out = (ê_out1 × ê_out2) / |ê_out1 × ê_out2|
   b. Compute the escape fraction:
      f_esc = (ê_in · n̂_out)²
4. Also compute:
   - The normal component: e_esc · n̂_surface
   - The tangential residual: e_esc − (e_esc · n̂_surface) n̂_surface
5. Record f_esc, the normal component magnitude, and position

### Sweeps

| Parameter | Range | Purpose |
|-----------|-------|---------|
| N₁ (cells around tube) | 4, 6, 8, 10, 20, 40 | Resolution dependence |
| N₂ (cells around ring) | = N₁ | Keep aspect ratio fixed |
| ε = a/R | 0.1, 0.3, 0.5, 0.7, 1.0 | Curvature dependence |
| Node position | All nodes | Spatial variation |
| Incoming edge | All 3 | Directional dependence |
| Mapping method | A (equal edges), B (conformal) | Embedding dependence |

### What we're looking for

| Outcome | Interpretation |
|---------|----------------|
| f_esc ≈ α for some (N, ε) | The lattice resolution that gives α is physical |
| f_esc = constant × ε² / N² | The escape fraction is set by curvature/resolution ratio |
| f_esc varies around torus | Coupling depends on local curvature |
| f_esc is same for all edges | Junction symmetry preserved on curved surface |
| f_esc differs for methods A vs B | The escape is embedding-dependent, not topological |

---

## Dependencies

numpy, matplotlib

---

## Files (planned)

| File | Purpose |
|------|---------|
| T9-junction-escape.md | This framing document |
| scripts/track9_junction_escape.py | Main computation |
| F9-junction-escape.md | Findings |
| output/track9_*.png | Visualizations |
