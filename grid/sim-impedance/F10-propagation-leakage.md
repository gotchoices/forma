# F10 — Propagation leakage: findings

**Track:** [T10-propagation-leakage.md](T10-propagation-leakage.md)
**Scripts:** [scripts/track10_propagation_leakage.py](scripts/track10_propagation_leakage.py),
[scripts/track9_10_equal_edge.py](scripts/track9_10_equal_edge.py) (corrected lattice)
**Status:** Complete — revised with equal-edge lattice and reflected wave

---

## Summary

We injected a unit signal at one edge of a hexagonal torus
lattice and propagated it junction-by-junction, tracking
the cumulative normal leakage at each step.

Initial computation used a conformal mapping with distorted
junction angles and unequal edge lengths (up to 4:1 ratio).
This was corrected using spring relaxation to equalize edges
(achieving ~1.5:1 ratio) and including the S-matrix reflected
wave.  All methods show resolution-dependent behavior: the
normal fraction depends on the lattice spacing N and does
not converge to α.

---

## Methods and results

### Method A — Raw geometric decomposition

At each junction, solve [ê_a | ê_b | n̂] · [a,b,n] = v_in
and propagate a, b directly.

**Result: non-physical.**  Amplitudes grow exponentially
(reaching 10^30+ after ~24 steps at N=8).  On a flat
hexagonal sheet with 120° angles, the decomposition gives
a = b = 1 for each outgoing edge — every junction DOUBLES
the total energy.  The cross term (2ab cos 120° = -1)
restores energy for the vector sum, but the branches
propagate independently, so the cross term is lost.

**Lesson:** the geometric decomposition coefficients are
NOT independent channel amplitudes.  A non-orthogonal
basis has coefficients > 1 that compensate via interference.
Propagating them independently destroys this cancellation.

### Method B — Energy-normalized decomposition

Same as A, but rescale (a, b, n) so a² + b² + n² = A² at
each step, forcing energy conservation.

**Result: nearly all energy leaks to normal at small N.**
At N=4 or 6, the normal fraction reaches 97–99% within
12–18 steps.  At larger N, the fraction decreases:

| ε   | N=4  | N=6  | N=8  | N=10 | N=14 |
|-----|------|------|------|------|------|
| 0.3 | 97%  | 96%  | 98%  | 22%  | 9%   |
| 0.5 | 98%  | 99%  | 39%  | 17%  | 9%   |
| 0.7 | 99%  | 99%  | 47%  | 16%  | 8%   |

The high percentages at small N reflect the large per-node
escape fraction on a coarse lattice.  As N increases, the
per-node escape shrinks and the wave propagates further
before losing its energy to leakage.

### Method C — S-matrix with direction tracking

Use the Y-junction S-matrix (transmitted = 2/3 each) for
scalar amplitudes.  Track the effective signal direction and
compute its surface-normal component.  This is the most
physically grounded approach.

**Result: normal fraction decreases with N.**

| ε   | N=4  frac/α | N=10 frac/α | N=14 frac/α |
|-----|-------------|-------------|-------------|
| 0.3 | 15.5        | 2.4         | 1.3         |
| 0.5 | 17.0        | 2.8         | 1.6         |
| 0.7 | 18.6        | 3.2         | 1.8         |

The ratio frac/α decreases roughly as N^(-1.9), passing
through 1 near N ≈ 15–20 and continuing toward 0.

The corrected computation includes the reflected wave
(-1/3 amplitude back along the input edge).  With all three
S-matrix outputs, the total active energy is conserved at
exactly 1.0.  The normal "leakage" is a diagnostic — the
squared projection of the signal direction onto the surface
normal, weighted by amplitude — not an actual energy loss
channel.  The S-matrix has no mechanism for energy to
physically leave the 2D surface.

---

## Key findings

### F1. Raw decomposition is non-physical for propagation

The 3×3 geometric decomposition gives coefficients that
reconstruct the input VECTOR but do not represent independent
channel energies.  For a non-orthogonal basis, |a|, |b| > 1
is typical, and propagating these independently creates
energy at each step.

This is not a flaw in the decomposition — it's a fundamental
property of non-orthogonal bases.  The decomposition is
correct for a single step (Track 9), but iterating it as
independent amplitude propagation violates energy conservation.

### F2. Energy normalization masks the physics

Method B forces energy conservation by rescaling, but this
changes the relative proportions of a, b, n in an ad hoc way.
The result is dominated by the normalization procedure, not
the underlying geometry.

### F3. S-matrix method conserves energy — normal fraction is a diagnostic

With the reflected wave included (corrected computation),
Method C conserves energy exactly (active energy = 1.0 at
all steps).  The "normal fraction" measures how much the
signal direction deviates from the tangent plane, not how
much energy actually leaves the surface.

The normal fraction decreases with N (equal-edge lattice):

| ε   | N=4  frac/α | N=10 frac/α | N=20 frac/α |
|-----|-------------|-------------|-------------|
| 0.3 | 73.7        | 53.2        | 33.1        |
| 0.5 | 78.6        | 69.8        | 47.1        |
| 0.7 | 80.8        | 67.9        | 49.2        |

The fraction does not converge to α.  It remains much
larger than α and decreases slowly, reaching zero as N → ∞.

### F4. Propagation does not change the scaling

The key hope was that iterative propagation would produce
an N-independent result — summing N copies of 1/N²-scale
leakage over N steps to get something finite.  Instead:

- Method A: amplitudes grow as ~2^K (non-physical — the
  geometric decomposition in a non-orthogonal basis gives
  coefficients > 1 that compound exponentially)
- Method B: almost all energy leaks within ~N steps (trivial)
- Method C: direction-tracking diagnostic scales as ~1/N,
  but does not represent actual energy leakage

The propagation adds steps but doesn't change the per-step
scaling.  The S-matrix conserves energy perfectly on the
2D surface and provides no mechanism for energy to escape
into the normal direction.

### F5. The S-matrix has no leakage channel

A deeper issue: the Y-junction S-matrix distributes SCALAR
amplitudes among edges.  It does not care about the 3D
directions of the edges — it operates purely on the 1D
graph topology.  Even though the 3D edge directions are
non-coplanar, the scalar wave propagation is unaffected.

For actual energy leakage, the lattice would need a
coupling mechanism between the 2D surface modes and
3D bulk modes — e.g., a modified S-matrix that includes
a fourth "normal" output channel.  The escape fraction
(Track 9) measures the geometric propensity for such
coupling, but doesn't provide its strength.

---

## Relation to prior tracks

| Track | What it adds | Outcome |
|-------|-------------|---------|
| 9     | Per-node escape (static) | f_esc ~ 1/N², Σ converges but ≠ α |
| 9b    | Total escape over all nodes | Converges to ~25–60, not α |
| **10** | **Iterative propagation** | **S-matrix conserves energy; no leakage** |

Track 10 reveals a deeper issue than simple resolution
dependence.  The Y-junction S-matrix is a scalar operation
on a 1D graph — it distributes amplitudes among edges
regardless of their 3D orientation.  There is no channel
for energy to leave the 2D surface.  The "normal fraction"
is a diagnostic measuring geometric misalignment, not a
physical energy loss.

---

## Conclusion

The iterative propagation approach is conceptually appealing
but reveals that the Y-junction S-matrix — the correct
scattering rule for scalar waves at a lattice node — has
no mechanism for energy to leave the 2D surface.  The
geometric decomposition (Method A) is non-physical because
it produces exponentially growing amplitudes.  The energy-
normalized version (Method B) is ad hoc.  Method C (S-matrix)
conserves energy perfectly and shows that direction tracking
is a diagnostic, not a loss channel.

**The junction escape mechanism (Tracks 8–10) shows WHERE
coupling occurs (junctions with curvature) and WHY some
modes couple preferentially (n₁=1, traveling waves), but
it cannot determine HOW MUCH couples.  The coupling
strength — α — requires a physical mechanism that connects
2D surface modes to 3D bulk modes, not just a geometric
overlap.**
