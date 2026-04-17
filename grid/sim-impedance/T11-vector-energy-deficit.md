# Track 11: Vector energy deficit at curved Y-junctions

**Status:** Framed — ready to compute.

**Premise:** On a flat hexagonal lattice, the Y-junction
scattering matrix conserves energy exactly.  An incoming
vector amplitude E on edge ê₁ scatters to outgoing edges
ê₂ and ê₃ (amplitude 2/3 each) plus a reflection back on
ê₁ (amplitude −1/3).  Because the three edges are coplanar
at 120°, the squared vector sum of outgoing amplitudes equals
the incoming energy.

On a **curved** torus, the three edges are no longer coplanar.
The S-matrix still distributes scalar amplitude by the same
2/3, −1/3 rule — but the outgoing amplitudes ride on edge
vectors that point in different 3D directions.  When you
reconstruct the total outgoing vector energy (|Σ aᵢ êᵢ|²),
the non-coplanarity means the cross terms don't cancel the
same way.  There is an **energy deficit**: the outgoing vector
energy doesn't quite equal the incoming vector energy.

This deficit is:
- Purely geometric (depends on edge directions, set by torus
  curvature and lattice embedding)
- Uses no coupling constant (the S-matrix weights 2/3, −1/3
  come from energy conservation, not from α)
- Has no free parameter (no tolerance, no lattice resolution
  in the formula — the deficit at each junction is a definite
  number once the edge directions are known)
- Computable per junction, summable over the torus

**The question:** does the total vector energy deficit per
circuit, summed over all junctions for a circulating CP wave,
converge to a value related to α ≈ 1/137?

---

## Why this is different from Tracks 8–10

| Track | What was computed | Free parameter? | Issue |
|-------|-------------------|-----------------|-------|
| 8 | E·ρ̂ field projection → charge selection | None | Determines WHICH modes couple, not HOW MUCH |
| 9 | Geometric escape fraction (ê₁ · n̂₂₃)² | Lattice resolution N | Goes to zero as N → ∞ |
| 10 | Iterative scalar propagation with S-matrix | N | S-matrix conserves scalar energy; no leakage channel |
| **11** | **Vector energy deficit using S-matrix weights** | **None** | **Energy deficit from non-coplanarity at fixed S-matrix** |

The critical distinction from Track 9: Track 9 computed
(ê₁ · n̂₂₃)² — the projection of the incoming edge onto the
outgoing plane's normal.  This measures how much of the
incoming DIRECTION is out-of-plane.  It depends on the lattice
resolution because finer meshes make the edges more coplanar.

Track 11 computes a different quantity: the energy that
doesn't reconstruct when you apply the S-matrix weights (2/3,
−1/3) to the actual 3D edge vectors.  This includes the
S-matrix weights, the CP wave phase, and the time averaging.
The per-junction deficit is resolution-dependent, but the
total over a full circuit may converge — because the number
of junctions grows as N while the per-junction deficit shrinks
as 1/N², and the intermediate cross terms may contribute.

The critical distinction from Track 10: Track 10 propagated
scalar amplitudes.  The S-matrix operates on scalars, so it
has no mechanism for energy to leave the surface.  Track 11
propagates **vector** amplitudes.  The S-matrix distributes
scalar weights, but the vectors those weights ride on are
non-coplanar.  The vector energy deficit is the physical
quantity — it represents the energy that cannot be accounted
for by in-surface vector fields alone.

---

## Physical picture

1. A CP wave circulates on a hexagonal torus.  At each node,
   the field arrives as a 3D vector along one edge.

2. The S-matrix scatters: 2/3 of the amplitude to each of the
   two forward edges, −1/3 reflected.  These are scalar
   weights derived from energy conservation on a flat junction.

3. On a flat sheet, the three vectors (weighted by 2/3, 2/3,
   −1/3) reconstruct the original vector exactly.  No deficit.

4. On a curved sheet, the edges aren't coplanar.  The weighted
   vector sum has a slightly different magnitude than the
   original.  The deficit is:

   δE² = |E_in|² − |Σᵢ Sᵢ (E_in · êᵢ) êᵢ|²

   where Sᵢ are the S-matrix weights and êᵢ are the 3D unit
   edge vectors.

5. For a CP wave, the incoming vector rotates around the tube
   as the wave circulates.  The deficit depends on the angle
   between E_in and the junction plane — which depends on θ₁
   (position around the tube cross-section).

6. Time-averaging over one wave period selects the persistent
   (DC) component of the deficit, suppressing oscillating terms
   (the same mechanism that Track 8 identified for charge).

7. Summing the time-averaged deficit over all junctions on
   the torus gives the **total vector energy deficit per
   circuit** — the fraction of the wave's vector energy that
   "doesn't fit" on the curved surface.

---

## The computation

### Step 1: Build the hexagonal torus lattice

Same as Track 8: N₁ × N₂ honeycomb cells, mapped to a torus
with major radius R, minor radius a.  Aspect ratio ε = a/R.

Use the equal-edge relaxed lattice from Track 9 (spring
relaxation to minimize edge length variance).

### Step 2: At each junction, compute the vector energy deficit

For each node with 3 connected edges (unit vectors ê₁, ê₂, ê₃):

1. The incoming CP field at this node:
   **E** = cos(φ) t̂₁ − sin(φ) t̂₂
   where φ = n₁θ₁ + n₂θ₂ and t̂₁, t̂₂ are the local tangent
   vectors on the torus surface.

2. Project E onto each edge to get incoming amplitude per edge:
   aᵢ = **E** · êᵢ

3. Apply S-matrix scattering: each edge receives
   - From its own incoming signal: Sᵢᵢ aᵢ = −(1/3) aᵢ
   - From each neighbor j: Sⱼᵢ aⱼ = (2/3) aⱼ

4. The outgoing vector at each edge:
   **E**_out,i = [−(1/3) aᵢ + (2/3) aⱼ + (2/3) aₖ] × êᵢ

5. Total outgoing vector energy:
   E²_out = Σᵢ |**E**_out,i|²

   Wait — this double counts. The proper energy balance:
   E²_in is the incoming vector energy at this node.
   E²_out is the energy carried away on the three outgoing
   edges.

   Actually, the right quantity is simpler. The incoming
   vector **E** can be decomposed into:
   - Component in the span of {ê₁, ê₂, ê₃}: reconstructible
   - Component orthogonal to the span: the deficit

   On a flat junction, span{ê₁, ê₂, ê₃} = the 2D plane,
   so the deficit = E · n̂ = 0 (the field is tangential).
   On a curved junction, the span is still 2D (three vectors
   in 3D span at most a 2D subspace plus corrections from
   non-coplanarity), but the subspace is tilted relative to
   the surface tangent plane.

6. **Simplest formulation:**

   The vector reconstruction error is:

   **E**_recon = Σᵢ (E · êᵢ) × êᵢ    [projection onto edges]
   **E**_deficit = **E** − **E**_recon

   But this is just the component of E perpendicular to the
   span of the three edges — which ON A FLAT JUNCTION is zero
   (the edges span the tangent plane), and ON A CURVED
   JUNCTION is nonzero.

   Actually, for three non-orthogonal vectors, the projection
   Σᵢ (E · êᵢ) êᵢ is NOT the orthogonal projection unless
   the êᵢ are orthonormal.  For non-orthogonal edges, we
   need the dual basis.

   **Better formulation:** use the S-matrix directly.

   The S-matrix maps 3 incoming scalar amplitudes to 3
   outgoing scalar amplitudes.  But if the incoming amplitudes
   are the projections of a 3D vector onto non-coplanar edges,
   the outgoing scalars (when multiplied by their edge
   directions) may not reconstruct a vector in the surface
   tangent plane.

   The deficit is the normal component of the reconstructed
   vector:

   **V**_recon = Σᵢ bᵢ êᵢ    where bᵢ = Σⱼ Sⱼᵢ aⱼ
   deficit_n = **V**_recon · n̂_surface
   deficit_ρ = **V**_recon · ρ̂

   And the energy deficit:
   δE² = |**V**_recon|² − |**V**_recon − (deficit_n) n̂|²
       = deficit_n²

### Step 3: Time-average over the wave phase

The CP wave has phase φ = n₁θ₁ + n₂θ₂ − ωt.  At each node:
- Compute the deficit for multiple values of ωt (or compute
  analytically by averaging over the phase)
- The time-averaged deficit ⟨δE²⟩ extracts the persistent
  leakage, suppressing oscillating terms

### Step 4: Sum over all junctions

Total deficit = Σ_nodes ⟨δE²⟩ × (area weight)

Normalize by the total wave energy on the surface.

### Step 5: Check convergence and parameter dependence

| Parameter | Sweep | Purpose |
|-----------|-------|---------|
| N (lattice resolution) | 10 → 100 | Does the total converge? |
| ε (aspect ratio) | 0.1 → 1.0 | ε dependence |
| (n₁, n₂) mode | (1,2), (1,3), (0,1), (2,4) | Mode dependence / selection rule |

---

## What we're looking for

### Strong success

The total vector energy deficit per circuit converges to
a value of order α ≈ 1/137 (or α², or some simple function
of α), independent of lattice resolution N.  This would
derive the coupling constant from pure lattice geometry.

### Partial success

The deficit converges to a definite geometric constant
(like 1/4π or similar) that is NOT α, but is
resolution-independent and mode-independent.  This would
show that the curved junction mechanism produces a genuine
coupling — the missing link to α would be a normalization
factor.

### Informative negative

The deficit is resolution-dependent (scales as 1/N² like
Track 9), meaning the vector formulation doesn't add
convergence.  This would definitively close the
"junction distortion → α" pathway.

### Charge confirmation

The deficit is nonzero only for n₁ = 1 traveling waves
(same selection rule as Track 8).  Even without deriving
α, this would confirm that the vector energy deficit
mechanism is consistent with charge physics.

---

## Why this might work when Track 9 didn't

Track 9 computed a purely geometric quantity (projection
onto the outgoing normal plane) that decreases with N
because finer meshes → more coplanar edges.

Track 11 computes an **amplitude-weighted** quantity using
the S-matrix.  The S-matrix weights (2/3, −1/3) are fixed
and don't scale with N.  The per-junction deficit scales as
the square of the angular deviation (~1/N²), but there are
~N² junctions, so the sum might converge to:

> Total ≈ N² × (angular deviation)² / N² → finite

if the angular deviation scales as 1/N.  This is exactly
what curvature does: the angle subtended by each edge is
Δθ = 2π/N, and the deviation from coplanarity at each
junction is proportional to Δθ² ∝ 1/N².  So:

> Total ≈ N² × (1/N²)² × N² = 1

Wait — that gives N²-dependent scaling.  Let me be more
careful:

- Junctions per tube circumference: ~N₁
- Junctions per ring circumference: ~N₂
- Total junctions: ~2 N₁ N₂
- Angular deviation per junction: ~ε/N₁ (for tube direction)
- Deficit per junction: ~(ε/N₁)²
- Sum over tube circuit (N₁ junctions): N₁ × (ε/N₁)² = ε²/N₁

This STILL decreases with N₁.  The deficit per circuit
→ 0 as the lattice is refined.

BUT: this counts only the leading-order geometric deficit.
The S-matrix cross terms (the interference between the 2/3
and −1/3 channels) may produce a contribution that doesn't
scale with N.  This is the key thing to compute — whether
the interference terms survive.

The computation will resolve this definitively.

---

## Dependencies

- numpy (lattice construction, linear algebra)
- matplotlib (visualization)
- Track 9's equal-edge relaxation code (reuse)

---

## Files

| File | Purpose |
|------|---------|
| T11-vector-energy-deficit.md | This framing document |
| scripts/track11_vector_deficit.py | Main computation |
| F11-vector-energy-deficit.md | Findings (after computation) |
