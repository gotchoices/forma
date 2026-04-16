# Fields from lattice geometry

**Status:** Conceptual — extends sim-maxwell analysis.

How the E and B fields emerge from the junction geometry of the
GRID lattice, and why E + iB is the natural field variable.

**Prerequisite context:**
- [sim-maxwell/README.md](sim-maxwell/README.md) — directional
  wave propagation from junction scattering
- [hexagonal.md](hexagonal.md) — Y-junction (N=3) vs triangular
  (N=6) lattice comparison
- [maxwell.md](maxwell.md) — continuum derivation of Maxwell's
  equations from GRID axioms

---

## 2D: the Y-junction

### Setup

On the honeycomb lattice, each vertex has 3 edges meeting at
120° — a **Y-junction**.  The junction scattering matrix (from
energy conservation + equal impedance, no Maxwell input) is:

$$
S_{ij} = \frac{2}{N} \quad (i \neq j), \qquad
S_{ii} = \frac{2}{N} - 1
$$

For N = 3: reflection amplitude = −1/3, transmission to each
outgoing edge = 2/3.

When a wave arrives on one edge, the two outgoing edges are at
±60° from the forward direction (the continuation of propagation).
There is no edge pointing straight forward — the lattice forces
an angular split.

```
        outgoing (+60°)
         ╱
        ╱
   ────•         → forward direction (no edge here)
        ╲
         ╲
        outgoing (−60°)
```

### The forward/perpendicular decomposition

Each outgoing edge carries both a forward and a perpendicular
component relative to the propagation direction:

| Outgoing edge | Forward component | Perpendicular component |
|---------------|-------------------|-------------------------|
| At +60° | cos 60° = 1/2 | +sin 60° = +√3/2 |
| At −60° | cos 60° = 1/2 | −sin 60° = −√3/2 |

If both edges carry amplitude a with the same phase, the
forward components add (1/2 + 1/2 = 1) and the perpendicular
components cancel (+√3/2 − √3/2 = 0).  Result: pure forward
propagation, no transverse field.  This is a linearly polarized
wave — the sim-maxwell result.

If the edges carry amplitudes with a **90° phase difference**
(a₁ = A, a₂ = Ae^{iπ/2} = iA), the perpendicular components
no longer cancel:

| Component | Value |
|-----------|-------|
| Forward | A(1 + i)/2 |
| Perpendicular | A(1 − i) × √3/2 |

The forward and perpendicular components have **equal magnitude**
but differ by a 90° phase — this is the definition of circular
polarization.

### E and B from the decomposition

The symmetric (sum) and antisymmetric (difference) combinations
of the two outgoing edge amplitudes separate cleanly:

- **Sum** (a₁ + a₂): proportional to the **forward** component
  → the **E-like** field (the part that propagates)
- **Difference** (a₁ − a₂): proportional to the
  **perpendicular** component → the **B-like** field (the part
  that circulates)

The E and B components are not carried by individual edges.
Every edge carries a mixture of both.  The separation into E
and B exists only as a combination — which is precisely why the
complex number E + iB is the natural field variable.

### Why E and B cannot decouple

On a **square** (Cartesian) lattice, two outgoing edges would be
at 0° (forward) and 90° (perpendicular).  One edge would carry
pure E, the other pure B.  They could propagate independently
without mixing.

On the **triangular/honeycomb** lattice, no two edges are
perpendicular.  Every outgoing edge carries both E and B
projections.  At every junction, the scattering rule re-mixes
the two.  A pure-E or pure-B disturbance cannot propagate — it
is immediately contaminated by the other component at the first
junction it encounters.

This forced mixing is Maxwell's equations.  The lattice geometry
**requires** that any propagating disturbance carry both E and B,
coupled together with a definite phase relationship.

### Fourier modes of the Y-junction

The 3 edges at a node sit at angles 0°, 120°, 240° — the three
**cube roots of unity** in the complex plane (ω = e^{i2π/3}).
The natural decomposition of a 3-component vector over these
directions is a discrete Fourier transform with three modes:

| Mode | Phase pattern (edges 1,2,3) | Physical identity |
|------|----------------------------|-------------------|
| 0 | (1, 1, 1) | Scalar — all edges in phase → charge-like / breathing |
| 1 | (1, ω, ω²) | Left circular polarization → E + iB |
| 2 | (1, ω², ω⁴ = ω) | Right circular polarization → E − iB |

Mode 0 is the symmetric mode: all edges carry the same amplitude
and phase.  This is a charge/monopole excitation — energy that
pools at the node rather than propagating as a wave.

Modes 1 and 2 are the two helicities.  They represent waves where
the phase advances progressively around the junction — clockwise
for one, counterclockwise for the other.  These are the two
circular polarization states, and they correspond to E + iB and
E − iB (or equivalently, particle and antiparticle in the quantum
picture).

The Y-junction doesn't just *permit* circular polarization.  Its
3-fold symmetry **naturally produces** CP as the fundamental
eigenmode.  Linearly polarized waves are superpositions of the
two CP modes — they are derived, not fundamental on this lattice.

---

## 3D: the tetrahedral junction

### Setup

The GRID 3D lattice is simplicial — tiled by tetrahedra
([lattice-geometry.md](lattice-geometry.md)).  At the junction
level, the minimal vertex coordination is N = 4 (the diamond
lattice — the 3D dual of the honeycomb, just as the honeycomb
is the 2D dual of the triangular lattice).

At a tetrahedral junction, 4 edges meet.  The angle between any
two edges is the tetrahedral angle:

$$
\theta_{\text{tet}} = \arccos\!\left(-\frac{1}{3}\right)
\approx 109.47°
$$

When a wave arrives on one edge, it scatters to the 3 outgoing
edges.  The scattering matrix (N = 4):

| Property | Value |
|----------|-------|
| Reflection | −1/2 |
| Transmission (each of 3) | 1/2 |

### The transverse cross-section IS a Y-junction

The 3 outgoing edges make equal angles with the forward direction.
The angle between forward and each outgoing edge is:

$$
\theta_{\text{fwd}} = 180° - 109.47° = 70.53°
$$

Each outgoing edge has:
- Forward projection: cos(70.53°) = **1/3**
- Perpendicular projection: sin(70.53°) = **2√2/3** ≈ 0.943

The 3 outgoing edges are related by a 3-fold rotation around
the forward axis (the C₃ symmetry of the tetrahedron about any
vertex-to-centroid axis).  Their projections into the transverse
plane are equally spaced at **120°** — exactly a Y-junction
pattern.

```
    Transverse plane (perpendicular to propagation)

              e₁ (0°)
              ╱
             ╱
            •
           ╱ ╲
          ╱   ╲
    e₂ (120°)  e₃ (240°)
```

This is the crucial geometric fact: **the transverse cross-section
of a tetrahedral junction is a Y-junction**.  Everything derived
in the 2D section carries over to the transverse plane.

### Two polarizations from one junction

The 3 transverse components decompose by the same Fourier
transform as the 2D case — the cube roots of unity on the
3 outgoing edges:

| Mode | Transverse pattern | Physical identity |
|------|-------------------|-------------------|
| 0 | (1, 1, 1) | Forward / longitudinal |
| 1 | (1, ω, ω²) | Left circular polarization |
| 2 | (1, ω², ω) | Right circular polarization |

But now the transverse plane is 2D (not 1D as in the 2D case),
so each CP mode sweeps out a **rotating** E + iB vector in the
two transverse dimensions.  The two modes are the two independent
polarization states of light — left-handed and right-handed CP.

### Degree-of-freedom counting

| Counting | N | Modes |
|----------|---|-------|
| Total edge amplitudes | 4 | 1 incoming + 3 outgoing |
| Subtract scalar (charge-like) | 1 | Mode 0 |
| Remaining vector modes | 3 | |
| → Longitudinal (gauge / unphysical) | 1 | Along propagation |
| → Transverse (physical polarizations) | **2** | LCP + RCP |

This matches exactly: a photon has **2 physical polarization
states**.  The tetrahedral junction produces them through the
same 3-fold symmetry that the Y-junction uses in 2D.

### Forced E/B mixing in 3D

In 3D, E lives on edges (1-forms) and B lives on faces (2-forms)
of the simplicial lattice.  A regular tetrahedron has 6 edges and
4 faces.

On a **cubic** lattice, each edge is perpendicular to exactly one
face (the face whose normal aligns with the edge direction).  This
means E_x (the x-edge) is geometrically aligned with B_x (the
face perpendicular to x̂).  The components can decouple.

On a **tetrahedral** lattice, no edge is perpendicular to any
non-adjacent face.  (An edge lies *in* its two adjacent faces, so
it is trivially perpendicular to those face normals.  But the two
non-adjacent faces have normals at oblique angles to the edge.)

Concretely, for a regular tetrahedron with vertices at
(1,1,1), (1,−1,−1), (−1,1,−1), (−1,−1,1):

| Edge | Non-adjacent face normal | Angle between them |
|------|-------------------------|--------------------|
| v₁→v₂: (0,−1,−1) | face v₁v₃v₄: (−1,1,1) | arccos(0) ≠ 90° ... dot = +2 |
| v₁→v₂: (0,−1,−1) | face v₂v₃v₄: (1,1,1) | dot = −2 |

Neither dot product is zero.  Edges and non-adjacent face normals
are **never perpendicular** in the tetrahedron.

This is the 3D version of the forced-mixing argument: E (edges)
and B (faces) are geometrically entangled by the simplicial
lattice.  They cannot propagate independently.  Every junction
scattering event re-mixes them, just as in 2D.

By contrast, a cubic lattice would allow clean E/B separation —
and would not naturally produce Maxwell-like coupled field
equations.

---

## Why the simplicial lattice produces Maxwell

Combining the 2D and 3D analyses:

| Property | Simplicial (tri/tet) | Cartesian (square/cube) |
|----------|---------------------|------------------------|
| E and B axes | Oblique (never ⊥) | Orthogonal |
| E/B mixing at junctions | **Forced** | Can decouple |
| Natural field variable | E + iB (complex) | E, B separately |
| CP polarization | **Eigenmode** of junction | Superposition (derived) |
| Maxwell coupling (∂B/∂t ↔ ∇×E) | **Required** by geometry | Must be imposed |

The simplicial lattice doesn't just *permit* Maxwell's equations
— its geometry **requires** that any propagating disturbance
carry coupled E and B fields.  The coupling is not an axiom; it
emerges from the fact that the lattice has no orthogonal axes.

### Connection to the ℵ-line

In 2D, the B-field component (the antisymmetric / circulation
mode at the junction) is perpendicular to E.  But in the 2D
lattice, there is no spatial direction perpendicular to the
plane.  When the lattice is embedded in 3D, B needs a place
to "point."

The **ℵ-line** (the compact 1D internal dimension on each edge —
see [foundations.md](foundations.md)) provides this: E lives
along the in-plane edge direction, and B lives along the
ℵ-line direction on that edge.  The complex field E + iB
naturally decomposes into "real = in-plane (E)" and
"imaginary = internal (B)."

This remains a hypothesis (the ℵ-line's role as B's physical
carrier is suggestive but not derived from the axioms).

---

## Relation to existing results

### sim-maxwell (completed)

The simulation confirmed directional propagation from junction
scattering with no Maxwell input.  It identified E with edge
amplitudes and B with plaquette circulation.  The analysis here
provides the **mechanism**: the junction's 3-fold symmetry forces
E/B coupling and produces CP as the natural eigenmode.

The sim-maxwell analysis identified **polarization** as a
remaining item to test (specifically: "Are edge amplitudes ⊥ to
propagation?  Is plaquette circulation the B field?").  The
analysis here answers this at the structural level: yes, because
the Fourier decomposition of the junction requires it.  A
simulation test would confirm the prediction numerically.

### maxwell.md (continuum derivation)

The continuum derivation obtains E and B from the field tensor
F_μν, which splits into time-space (E) and space-space (B)
components under the Lorentzian signature (A2).  This is a
**top-down** derivation: it starts from the action principle
and arrives at the field equations.

The analysis here is **bottom-up**: it starts from the lattice
junction geometry and shows that E/B coupling is forced by the
lack of orthogonal axes.  The two approaches should converge
in the continuum limit — the junction-level forced coupling IS
the microscopic origin of the continuum F_μν structure.

### hexagonal.md (Y-junction substrate)

The Y-junction (N=3) produces the cleanest E/B decomposition
because there is no forward-aligned edge — every outgoing path
is oblique.  The triangular lattice (N=6) has an edge pointing
straight forward (0°), which carries pure forward projection
at that particular junction, but the overall wave dynamics still
mix E and B through multi-step propagation.

The honeycomb lattice's advantage for E/B coupling is the same
as its advantage for single-photon propagation: the minimal
junction (N=3) is the most constrained, leaving the least room
for E and B to avoid mixing.

---

## Open questions

1. **Simulation verification:** Run the existing sim-maxwell
   infrastructure with explicit E/B tracking — decompose edge
   amplitudes into sum (E) and difference (B) at each junction
   and verify that propagating waves carry both components with
   a 90° phase relationship.

2. **3D simulation:** Extend sim-maxwell to a 3D diamond lattice
   (N=4 junctions) and verify that both CP polarizations
   propagate as predicted by the tetrahedral junction analysis.

3. **Dispersion and anisotropy:** The junction analysis is exact
   at a single vertex.  Over many vertices, lattice anisotropy
   may introduce dispersion differences between the two CP modes.
   How isotropic is the 3D tetrahedral lattice for wave
   propagation?

4. **Connection to α:** The junction scattering matrix is fixed
   by energy conservation and has no free parameters.  Where does
   α enter?  The coupling strength α appears in the *action*
   (Step 5 of maxwell.md), not in the junction rule.  The
   junction produces the wave structure (coupled E and B); α sets
   the energy scale of those waves relative to charges.

---

## References within project

- [foundations.md](foundations.md) — GRID axioms, ℵ-line
- [maxwell.md](maxwell.md) — continuum Maxwell derivation
- [hexagonal.md](hexagonal.md) — Y-junction analysis, N=3 vs N=6
- [lattice-geometry.md](lattice-geometry.md) — 3D simplicial lattice, Model B
- [sim-maxwell/README.md](sim-maxwell/README.md) — simulation results
- [sim-impedance/](sim-impedance/) — α from coupling between lattices
