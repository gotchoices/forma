# F11 — Vector energy deficit / leakage at curved Y-junctions

**Tracks:** 11a (vector deficit), 11b (proper leakage fraction),
11c (three scattering models), 11d (pure geometry, no S-matrix)

**Status:** Complete — convergent geometric invariants found,
but resolution-dependent.  α not derived.

---

## Summary

When a flat hexagonal lattice is bent onto a torus, the
Y-junctions distort: the three edges are no longer coplanar,
and the angles deviate from 120°.  A signal propagating on
the lattice encounters this distortion at every junction,
and a fraction of its energy projects out of the surface —
the "leakage."

Four scattering models were tested.  All give:
- Proper fractions (0 to 1) ✓
- Energy conservation ✓
- Mode-independent leakage (no n₁ selection rule in the
  per-junction quantity)
- Convergent geometric invariants (N²×f → constant)
- Per-junction leakage that scales as ~1/N² (resolution-dependent)

The geometric invariant N²×f differs by model but is a
definite constant for each:

| Model | Physics | N²×f | Notes |
|-------|---------|------|-------|
| A (GRID S-matrix) | Ampl 2/3 fwd, -1/3 reflect | 0.63 ≈ 2/π | Imported from quantum graph theory |
| B (Equal split) | 1/2 energy per outgoing, no reflect | 2.43 | User's physical intuition |
| C (Angle-weighted) | Coupling ∝ cos θ, forward only | ~2.2 | Vector projection model |
| D (Pure geometry) | Project onto outgoing plane, no S-matrix | ~25 ≈ 8π | No imported rules |

---

## Findings

### F1. Junction angles are NOT 120° on a curved torus

The conformal mapping preserves angles intrinsically, but the
3D chord directions (node-to-node) differ from the tangent
directions.  At ε = 0.3, N = 20:

- Mean angle: 119.1° (deviation from 120°: +0.89°)
- Std: 60.7° — enormous spread
- Range: [25.7°, 173.6°]

The deviation from 120° scales as 1/N² and converges:
N²×Δangle → 348 (a geometric integral of the curvature).

The angles at the inner equator (high curvature) differ from
the outer equator (low curvature).  The junction geometry is
severely distorted, especially on coarse lattices.


### F2. The GRID S-matrix is an import, not a GRID axiom

The junction scattering rule S_ij = 2/3 (transmit), S_ii = -1/3
(reflect) comes from quantum graph theory (Neumann/Kirchhoff
vertex conditions).  It is consistent with GRID but NOT derived
from GRID's axioms (A1–A6).

GRID's axioms specify the lattice structure, gauge invariance,
resolution ζ, and coupling α — but NOT the junction scattering
rule.  Different scattering models (B, C, D) are equally
consistent with GRID's axioms.

If the junction rule is derived from GRID's lattice action,
α enters through κ = 1/(4πα), making any α computation from
junction behavior tautological.

The purest approach (Model D) uses no scattering rule at all —
just vector projection onto available edge directions.


### F3. Per-junction leakage is resolution-dependent

All four models show per-junction leakage ∝ 1/N² where N is
the number of lattice cells per direction.  Finer lattices
have more coplanar edges, producing less per-junction leakage.

| Model | N=10 f_leak | N=20 f_leak | N=40 f_leak |
|-------|------------|------------|------------|
| A | 6.4×10⁻³ | 1.6×10⁻³ | 3.9×10⁻⁴ |
| B | 2.4×10⁻² | 6.1×10⁻³ | 1.5×10⁻³ |
| C | 1.8×10⁻² | 5.5×10⁻³ | 1.5×10⁻³ |
| D | 1.6×10⁻¹ | 5.9×10⁻² | 1.6×10⁻² |


### F4. Geometric invariants are convergent

The product N²×f_leak converges to a model-dependent constant.
This means the TOTAL curvature-weighted leakage over the torus
(summed over all ~N² junctions) is a geometric invariant.

| Model | N²×f limit | Close to |
|-------|-----------|----------|
| A | 0.628 | 2/π = 0.637 |
| B | 2.43 | — |
| C | ~2.2 | — |
| D | ~25 | 8π = 25.13 |

These are genuine geometric properties of a hexagonal lattice
on a torus — analogous to the Euler characteristic or total
Gaussian curvature.  They are NOT α.


### F5. Per-junction leakage is mode-independent

Unlike Track 8's E·ρ̂ projection (which selects n₁ = 1 for
charge), the per-junction vector leakage is the same for all
modes.  This makes sense: the junction geometry doesn't depend
on which wave passes through it.

Mode dependence enters through the GLOBAL integral (Track 8
showed that the integrated normal flux selects n₁ = 1 for
charge).  The per-junction quantity is a local geometric
property.


### F6. Iterative circuit walk on pure geometry drains all energy

With Model D (pure geometry), a signal walking along actual
hexagonal lattice edges loses ~6% per junction (at N=20).
After ~200 steps, all energy has leaked to the normal direction.
Cumulative leakage = 1.0, with perfect energy conservation.

The ratio 1.0/α = 137 is trivially 1/α and does not constitute
a derivation.  It simply means "all the energy leaks out" and
the number of steps to do so has no direct connection to α.


### F7. ε dependence in per-junction leakage (Model D)

Model D shows non-monotonic ε dependence:

| ε | f_leak (N=20) | f/ε² |
|---|--------------|------|
| 0.05 | 0.137 | 55 |
| 0.1 | 0.143 | 14 |
| 0.3 | 0.059 | 0.65 |
| 0.5 | 0.036 | 0.14 |
| 0.7 | 0.031 | 0.064 |

The leakage DECREASES with increasing ε for ε > 0.1.  This is
counterintuitive — more curvature should mean more leakage.
The explanation is that the conformal mapping compresses the
inner equator at high ε, making the junction angles more
uniform (closer to 120°) in the compressed region.

Models A–C show much weaker ε dependence, consistent with
their lower overall leakage.


### F8. Iterative circuit gives ε-independent results for Models A–C

The iterative circuit computation (Section 4 of Track 11c)
gives cumulative leakage independent of ε for Models A–C.
This is a bug: the iterative computation used smooth torus
parametrization for edge directions, not the actual hexagonal
lattice.  The smooth parametrization doesn't encode ε-dependent
junction distortion.

Track 11d's iterative walk on the actual lattice (Model D)
does show ε-dependence, confirming that actual lattice
geometry is needed.

---

## Interpretation

### What the leakage mechanism explains

1. **WHY bending produces coupling:** a flat 2D lattice has
   coplanar junctions → no normal leakage → no charge visible
   to 3D.  Bending breaks coplanarity → normal leakage exists
   → charge becomes visible.

2. **WHERE coupling occurs:** at every Y-junction, with
   strength proportional to local curvature.  The inner equator
   of the torus leaks more than the outer equator.

3. **WHAT the leakage depends on:** the junction geometry
   (edge directions, which depend on curvature and lattice
   resolution).

### What it does NOT explain

4. **HOW MUCH leaks:** the per-junction leakage depends on
   lattice resolution N.  Without a physical value of N, the
   leakage fraction is undetermined.

5. **The value of α:** no model produces 1/137 as a
   parameter-free geometric constant.  The convergent invariants
   (N²×f) are definite numbers (2/π, 2.43, 8π, etc.) but
   none equal α.

### The tautology question

If the junction scattering rule is derived from GRID's lattice
action (which contains α through κ = 1/4πα), then the junction
behavior inherently encodes α.  In this case:

- Computing α from junction leakage = tautology
- But the tautology is informative: it tells us exactly WHERE
  in the GRID framework α enters (the junction scattering rule)
  and HOW it manifests (as the coupling between 2D surface modes
  and 3D normal modes)

If the junction rule is derived from geometry alone (Model D),
then α does NOT appear, and the leakage is a generic curvature
effect with no special value.

**Conclusion:** α cannot be derived from the bending of a
hexagonal lattice onto a torus using any of the four scattering
models tested.  The junction leakage is real and convergent
but resolution-dependent.  The geometric invariants (N²×f)
are definite constants but are not α.

The remaining viable pathways for deriving α:
1. **Topological defect energy** — the lattice action cost
   of a minimal vortex (A6), which may be computable without
   circular dependence on α
2. **Wave scattering at a 2D/3D interface** — transmission
   coefficient across the Ma-S boundary
3. **The ℵ-line structure** — coupling between edge modes
   and the internal compact dimension

---

## Files

| File | Contents |
|------|---------|
| T11-vector-energy-deficit.md | Track 11 framing |
| F11-vector-energy-deficit.md | This findings document |
| scripts/track11_vector_deficit.py | 11a: vector deficit (wrong normalization) |
| scripts/track11b_proper_leakage.py | 11b: proper leakage fractions |
| scripts/track11c_angle_corrected.py | 11c: three scattering models compared |
| scripts/track11d_pure_geometry.py | 11d: pure geometry, no S-matrix |
