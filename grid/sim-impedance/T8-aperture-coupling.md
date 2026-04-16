# Track 8: Aperture coupling — E-field leakage from bending

**Status:** Framed — ready to compute.

**Premise:** when a flat 2D hexagonal lattice is bent into a
torus, the edge directions change in 3D even though the intrinsic
geometry is preserved.  A wave propagating on the edges produces
a local E-field vector along each edge.  On a flat sheet, all
E vectors lie in-plane.  On a bent sheet, neighboring edges point
in slightly different 3D directions, and the scattered field at
each junction acquires a small component normal to the surface.

Summing these normal components over the full torus gives the
**Gauss flux** — the charge seen by a 3D observer.  This
computes the 2D→3D coupling from lattice dynamics, not from
static geometric coincidence (Tracks 1–7) or continuum field
models (R48).

**Key distinction from prior tracks:**

| Prior tracks (1–7) | This track (8) |
|---------------------|----------------|
| Static geometry: do lattice nodes coincide? | Dynamic: what happens to waves on a bent lattice? |
| Free parameter ε (tolerance) — no geometric justification | No free parameter — bending angle fixed by torus geometry |
| Coupling rate is smooth function of ε | Coupling is deterministic projection |
| Result: no non-trivial coupling found | Result: TBD |

**Key distinction from R48 (helicity-charge):**

| R48 | This track |
|-----|------------|
| Continuum E-field model (CP wave formula assumed) | Discrete lattice with junction scattering |
| α enters through field normalization | Wave normalized in 2D; leakage computed from geometry |
| Computes the charge given the field | Explains WHY charge exists (junction leakage from bending) |
| Top-down: field → integral → charge | Bottom-up: lattice → bend → leak → charge |

---

## Physical picture

1. On a flat hexagonal sheet, each Y-junction has 3 edges at
   120° in-plane.  A wave scatters according to the standard
   junction rule (S_ij = 2/3, S_ii = -1/3).  All E vectors
   lie in the plane.  No normal component.  No charge visible
   from outside.

2. Roll the sheet into a torus (major radius R, minor radius a).
   The edge lengths and junction angles are preserved (the torus
   is intrinsically flat).  But the edge **directions in 3D**
   change — neighboring edges now point along slightly different
   tangent planes.

3. At each junction, the scattered amplitudes ride on edges
   pointing in different 3D directions.  The vector sum of the
   outgoing E fields has a small component normal to the local
   surface.  This is the **aperture** — the opening through
   which the 2D field leaks into 3D.

4. The normal leakage at each junction is proportional to the
   local extrinsic curvature κ times the edge length L:
   δE_n ∝ κ · L · E_tangential

5. The number of junctions around any closed loop on the torus
   scales as (loop circumference) / L.  The product
   (leakage per junction) × (number of junctions) converges
   to a finite geometric integral as L → 0:
   ∫ κ · E_tangential dℓ

6. For a closed loop, the total turning angle is 2π
   (Gauss-Bonnet).  The integral converges to a value that is
   independent of L — a pure geometric coupling constant.

---

## The sign question

Whether the normal components **add** or **cancel** around the
torus depends on the wave structure:

**Standing wave** (symmetric in θ₂):
- Outer half of tube (θ₁ ≈ 0): curvature κ > 0, normals point
  outward → positive normal E
- Inner half (θ₁ ≈ π): curvature κ < 0, normals point inward
  → negative normal E
- By symmetry, the integral over the full tube cross-section
  cancels → **zero net charge**
- This matches R48 Track 1 (standing waves → zero Gauss flux)

**Traveling wave** (phase progression e^{in₂θ₂}):
- The phase breaks the inner/outer symmetry
- The wave amplitude weights the inner and outer halves
  differently at each azimuthal position
- The cancellation is incomplete → **net charge**
- This matches R48 Track 2 (traveling waves → Q = n₁ × e)

The computation must verify this explicitly and determine
whether the net flux depends on the mode numbers (n₁, n₂)
in the expected way.

---

## Inner vs outer half

The extrinsic curvature of the torus tube varies around the
minor circle:

| Position | θ₁ | Curvature κ | Node density | Normal direction |
|----------|-----|-------------|--------------|------------------|
| Outer equator | 0 | 1/(R + a) | Lower (stretched) | Outward from ring |
| Top/bottom | π/2 | 0 | Medium | Tangent to ring plane |
| Inner equator | π | −1/(R − a) | Higher (compressed) | Inward toward ring axis |

The metric factor p = 1 + ε cos θ₁ (where ε = a/R) controls
both the local circumference and the node spacing.  On a
discrete lattice with uniform edge lengths, the node COUNT is
fixed — it's the same as the flat sheet.  What changes is the
3D spacing and the edge directions.

The computation should track both effects:
1. The angular deviation of edges (curvature-dependent)
2. The density of junctions (curvature-dependent)
3. Whether their product converges independently of ε

---

## Algorithm

### Step 1: Build discrete hexagonal torus

1. Create a flat hexagonal lattice with N₁ × N₂ unit cells
2. Assign 2D coordinates (θ₁, θ₂) to each node
3. Map to 3D torus coordinates:
   - x = (R + a cos θ₁) cos θ₂
   - y = a sin θ₁
   - z = (R + a cos θ₁) sin θ₂
4. Each edge becomes a 3D vector from node to node
5. Compute the unit tangent vector along each edge: ê_edge
6. Compute the local surface normal n̂ at each node (from the
   cross product of two edge directions, or analytically)

### Step 2: Assign wave amplitudes

For mode (n₁, n₂), assign a **traveling wave** amplitude to
each edge:

- Compute the wave phase at each node:
  φ(θ₁, θ₂) = n₁θ₁ + n₂θ₂
- The amplitude on each edge is the phase gradient projected
  along the edge: a_edge ∝ ∇φ · ê_edge
- For a CP (circularly polarized) traveling wave, use the
  complex phase: a_edge = exp(i(n₁θ₁ + n₂θ₂))

(Multiple wave models can be tested — the simplest is a
scalar plane wave; the most physical is a CP mode.)

### Step 3: Compute normal leakage at each junction

At each node (junction), collect the 3 edge vectors and their
amplitudes:

1. Compute the local E vector:
   **E** = Σᵢ aᵢ × ê_edge,ᵢ  (vector sum of amplitude × direction)
2. Project onto local surface normal:
   E_n = **E** · n̂
3. Record E_n at each junction

### Step 4: Integrate

1. **Gauss flux:** sum E_n over all junctions (weighted by
   local area element if needed):
   Q_lattice = Σ_junctions E_n × A_junction
2. **Tangential energy:** sum |E_tangential|² over all junctions
   as a normalization reference
3. **Coupling ratio:** Q_lattice / E_tangential_total

### Step 5: Sweep parameters

| Parameter | Range | Purpose |
|-----------|-------|---------|
| ε = a/R | 0.01 → 1.0 | Aspect ratio dependence |
| N (lattice size) | 20×20 → 200×200 | Convergence check |
| (n₁, n₂) | (1,2), (1,3), (0,1), (2,4) | Mode dependence |
| Wave model | Scalar, CP | Model sensitivity |

---

## What we're looking for

### Minimum success (confirmation)

The lattice computation reproduces R48's results:
- Standing waves → zero net charge
- Traveling waves → charge ∝ n₁
- The charge formula matches Q = n₁ × e

This would validate the mechanism (junction leakage from
bending) as the microscopic explanation for charge, even
if it doesn't derive α.

### Strong success (α from geometry)

The coupling ratio (normal flux / tangential energy) converges
to a value related to α ≈ 1/137, with no free parameters.

This would mean: the fraction of 2D energy that leaks into
3D through bending is determined by pure lattice geometry,
and that fraction IS the fine-structure constant.

### Informative negative

The coupling ratio converges to a pure geometric constant
(like 2π or 4π) that is NOT α.  This would tell us:
- The bending mechanism explains WHY charge exists
- But the VALUE of charge (and hence α) comes from elsewhere
  (the action normalization, the ℵ-line structure, etc.)

Even this outcome advances understanding by separating the
"mechanism of charge" question from the "value of α" question.

---

## Connection to fields.md

The newly documented [fields.md](../fields.md) establishes that
E lives on edges and B lives as the antisymmetric combination
at Y-junctions.  Track 8 takes this literally: if E is carried
by edge directions, then bending the lattice changes those
directions in 3D, producing normal leakage.

The fields.md argument that E/B coupling is "forced" by the
triangular lattice geometry applies to the tangential
propagation.  Track 8 asks the complementary question: what
about the normal direction?  The tangential coupling gives
Maxwell's equations on the surface; the normal leakage gives
charge visible to 3D observers.

---

## Dependencies

- numpy (lattice construction, linear algebra)
- matplotlib (visualization)

No scipy needed — this is geometry + linear algebra.

---

## Files (planned)

| File | Purpose |
|------|---------|
| T8-aperture-coupling.md | This framing document |
| scripts/track8_aperture_coupling.py | Main computation |
| F8-aperture-coupling.md | Findings (after computation) |
| output/track8_*.png | Visualizations |
