# F9 — Junction escape fraction: findings

**Track:** [T9-junction-escape.md](T9-junction-escape.md)
**Script:** [scripts/track9_junction_escape.py](scripts/track9_junction_escape.py)
**Status:** Complete

---

## Summary

The escape fraction f_esc — the fraction of incoming signal
energy that cannot follow the outgoing edges at a curved
Y-junction — is a well-defined, nonzero quantity on a torus.
However, it does **not** yield a parameter-free derivation
of α.  The escape fraction depends on the lattice resolution
N (cells per direction) and decreases toward zero as N → ∞.
There is no distinguished value of N at which f_esc = α.

---

## Findings

### F1. The escape fraction is nonzero and computable

At every Y-junction on a curved torus, the three edge
directions are not coplanar in 3D.  The incoming unit vector
has a nonzero projection onto the normal of the outgoing
plane:

    f_esc = (ê_in · n̂_outgoing_plane)²

Typical values range from ~1% to ~25%, depending on the
curvature (ε = a/R) and lattice resolution (N).

### F2. f_esc decreases with N — it is a lattice-spacing effect

The central result.  Sample data (conformal mapping):

| ε   | N=4   | N=10  | N=20  | N=40  |
|-----|-------|-------|-------|-------|
| 0.1 | 0.099 | 0.029 | 0.017 | 0.009 |
| 0.3 | 0.166 | 0.098 | 0.032 | 0.008 |
| 0.5 | 0.223 | 0.108 | 0.030 | 0.008 |
| 0.7 | 0.250 | 0.142 | 0.036 | 0.009 |
| 1.0 | 0.258 | 0.178 | 0.053 | 0.014 |

As N increases (finer lattice), the edge directions approach
the continuum tangent vectors, the three edges become
coplanar with the surface tangent plane, and f_esc → 0.

**The escape fraction is NOT a geometric invariant of the
torus.  It depends on the lattice resolution.**

This is the same fundamental issue as the tolerance ε in
coincidence counting (Track 7): the quantity passes through
every positive value as the free parameter varies.  Selecting
the N that gives f_esc = α is circular.

### F3. The ratio f_esc/α passes through 1 — but not uniquely

For several ε values, the f_esc curve crosses α near N ≈ 40:

| ε   | N=40 f_esc/α |
|-----|-------------|
| 0.3 | 1.13        |
| 0.5 | 1.06        |
| 0.7 | 1.25        |
| 1.0 | 1.85        |

At ε = 0.5, N = 40, f_esc ≈ α to within 6%.  But this is
simply the curve f_esc(N) crossing through α on its way to
zero.  Every ε curve crosses α at some N.  There is no
reason to prefer one (ε, N) pair over another.

### F4. Methods A and B give identical results

Both lattice mapping methods (conformal and equal-edge) used
the same angular coordinates for node placement.  The 3D
positions differ by the torus metric, but the angular
separations between neighbors — and therefore the edge
directions — are identical.

A truly distinct "equal edge length" method would require
adjusting node coordinates so that all edges have the same
3D arc length.  This would distort the angular distribution,
placing nodes closer together angularly near the inner equator
(where curvature compresses space).  The escape fractions
would differ, but f_esc would still depend on N and go to
zero as N → ∞ for the same fundamental reason: finer
resolution → more coplanar edges.

### F5. Edge direction matters — junction symmetry is broken

On a flat hexagonal sheet, f_esc = 0 for all three incoming
edge choices.  On a curved torus, the three edges are
NOT equivalent.  For ε = 0.3, N = 10:

    Edge 0: mean f_esc = 0.124  (tube-direction edge)
    Edge 1: mean f_esc = 0.046  (ring-direction edge)
    Edge 2: mean f_esc = 0.124  (tube-direction edge)

Edges aligned with the tube direction (θ₁, higher curvature)
have ~3× larger escape than the ring-direction edge (θ₂,
lower curvature).  This is physically sensible: the tube
direction bends more sharply.

At higher curvature (ε = 0.7, N = 10), the asymmetry
increases:

    Edge 0: mean f_esc = 0.246
    Edge 1: mean f_esc = 0.052
    Edge 2: mean f_esc = 0.127

### F6. Spatial variation tracks local curvature

The escape fraction varies significantly across the torus:

- **Inner equator** (θ₁ ≈ π): highest curvature → largest f_esc
- **Outer equator** (θ₁ ≈ 0): lowest curvature → smallest f_esc
- **f_esc is nearly constant in θ₂** (around the ring)

This is consistent with the physical picture: the escape is
driven by how much the edge directions deviate from coplanar,
which is set by local Gaussian curvature.

For ε = 1.0 (spindle torus), some nodes have f_esc = 0 exactly
(the inner equator pinches to a point and the three edges
become coplanar in the degenerate limit).

### F7. f_esc does not scale as ε²/N²

If f_esc were controlled by a simple curvature-per-cell
quantity like κΔθ ∝ ε/N, we would expect f_esc ∝ ε²/N².
The data shows the ratio f_esc / (ε²/N²) is NOT constant:

| ε   | N=4 ratio | N=40 ratio |
|-----|-----------|------------|
| 0.1 | 158       | 1444       |
| 0.5 | 14.3      | 49.7       |
| 1.0 | 4.1       | 21.7       |

The ratio grows with N for all ε, and grows with decreasing ε.
This means f_esc falls slower than ε²/N² — there is a
significant contribution from the lattice geometry beyond
simple curvature scaling.

---

## Interpretation

### Why f_esc doesn't give α

The escape fraction is a **discretization artifact**.  It
measures how much the chord directions (node-to-node straight
lines) deviate from the tangent plane.  This deviation goes to
zero as the mesh is refined, because chord directions converge
to tangent directions.

For f_esc to yield α, there would need to be a **physical
lattice resolution** — a "correct" value of N set by the
physics.  In GRID, N is determined by the particle's
circumference in Planck lengths.  But the particle size is
itself a derived quantity (set by the mode number), so this
creates a circular dependency: the escape fraction depends
on the particle size, which depends on the mode structure,
which depends on the coupling, which is what we're trying
to derive.

### What f_esc does show

Despite not deriving α, the computation reveals several
physically meaningful features:

1. **Curvature breaks junction symmetry** — the three edges
   at a node are NOT equivalent on a curved surface.  Tube-
   direction edges couple more strongly to the 3D normal than
   ring-direction edges.

2. **Local curvature controls coupling** — the escape fraction
   tracks the local Gaussian curvature, being largest at the
   inner equator and smallest at the outer equator.

3. **The mechanism is real** — there IS a geometric pathway
   for energy to "escape" the 2D surface at a curved junction.
   The question is whether this pathway's strength is set by
   the lattice spacing (it is) or by a deeper geometric
   constant (it is not).

---

## Relation to prior tracks

| Track | Mechanism | Free parameter | Result |
|-------|-----------|----------------|--------|
| 1-7   | Coincidence counting / projection | Tolerance ε | Rate passes through 1/137 at some ε |
| 8     | CP field projection (global mode) | None | Confirms charge selection; doesn't give magnitude |
| **9** | **Junction escape (local geometry)** | **Lattice resolution N** | **f_esc passes through α at some N** |

Track 9 is the local-geometry counterpart of Track 7's
capstone result: the quantity depends on an arbitrary scale
parameter and passes through every positive value.

---

### F8. Total escape (Σ f_esc) converges — but not to α

Follow-up script: `scripts/track9b_total_escape.py`

Even though the per-node f_esc goes to zero, the total over
all M = 2N² nodes converges to a finite value because
f_esc ~ 1/N² and M ~ N²:

| ε   | Σ f_esc (N=60) |
|-----|----------------|
| 0.1 | 29.0           |
| 0.3 | 26.4           |
| 0.5 | 25.0           |
| 0.7 | 29.2           |
| 1.0 | 43.9           |

Convergence is clear: < 1% change between N=40 and N=60 for
all ε ≤ 0.7.

**However, these converged values are ~25–44, not α ≈ 0.0073.**
The total escape is a geometric integral of squared curvature
over the torus, of order 1, not order 1/137.  It depends on ε
(stronger curvature → more total escape), so it is not a
topological invariant either.

### F9. Escape is almost entirely surface-normal

At large N, the fraction of escape in the surface-normal
direction approaches 1.0:

| ε   | Normal fraction at N=60 |
|-----|------------------------|
| 0.1 | 0.81                   |
| 0.3 | 0.96                   |
| 0.5 | 0.97                   |
| 0.7 | 0.98                   |
| 1.0 | 0.95                   |

In the continuum limit, the outgoing-plane normal converges
to the torus surface normal.  The escape direction IS the
surface normal — the tangential component is a higher-order
lattice artifact.

---

## Conclusion

The junction escape fraction is a clean, intuitive measure
of how curvature couples a 2D lattice signal into 3D.  The
per-node escape goes to zero as the mesh is refined, but the
total escape over all nodes converges to a finite value —
a geometric integral of the squared curvature.  This total
is order-1 (≈ 25–44) and depends on the aspect ratio ε.
**It does not equal α.**

The escape mechanism is real and its direction is the surface
normal, but its magnitude is set by the total curvature of
the torus, not by a universal coupling constant.

**α cannot be derived from junction escape geometry alone.**
It requires a mechanism that is independent of both lattice
resolution and total curvature.

The remaining viable pathways for deriving α from GRID
geometry are:

1. **Topological defect energy** — the action cost of a
   minimal vortex, which counts lattice cells but in a
   resolution-independent way (the number of cells around
   a defect is fixed by topology, not by mesh refinement)

2. **Wave scattering amplitude** — the transmission
   coefficient at a 2D/3D interface, which is a ratio
   (dimensionless) and may converge to a fixed value as
   the lattice is refined

3. **Internal sheet geometry** — α from the winding number
   or wrapping angle of the triangular lattice on the torus,
   which is a topological invariant
