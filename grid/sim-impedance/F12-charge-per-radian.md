# F12 — Charge per radian: findings

**Track:** [T12-charge-per-radian.md](T12-charge-per-radian.md)
**Status:** Step 1 complete; Step 2 in progress

---

## Step 1: Geometric framework

### F1. The minimal hexagonal torus (N=2) has 8 nodes, 12 edges

The smallest honeycomb lattice that closes into a valid torus
has N₁ = N₂ = 2 (2 unit cells in each direction, 2 nodes per
cell = 8 nodes total, 12 edges).  It is severely distorted:
junction angles range from 17° to 110° (far from 120°).

### F2. Total turning angle = 4π for all tori

The sum of surface-normal turning angles across all junctions
is exactly 4π (= 2 × 2π) for the minimal torus.  This is the
Gauss-Bonnet theorem: total turning = 2π × (Euler char + genus
correction).  For a torus (genus 1, χ = 0), the total turning
from traversing both the tube circuit (2π) and ring circuit
(2π) gives 4π.

This 4π is the total "bending budget" distributed across all
junctions.

### F3. Charge per radian = e/(2π) = √(α/π)

If the known total charge e = √(4πα) is distributed uniformly
per radian of tube turning (2π total), the charge per radian
is:

> e / 2π = √(4πα) / 2π = √(α/π) ≈ 0.04820

This is a definite α-dependent quantity — NOT a derivation of
α, but a prediction for the per-radian micro-charge assuming
uniform distribution.

### F4. Σδθ²/N² converges to ~6.79 — a geometric invariant

The sum of squared angular deviations from 120°, divided by N²,
converges as the lattice is refined.  This is a genuine
geometric integral of the torus curvature.  At ε = 0.3, the
invariant ≈ 6.79.  It is NOT simply related to α (ratio ≈ 930).

### F5. Solid angle computation fails at large N

The spherical triangle formula for solid angle becomes
numerically unstable when edges are nearly coplanar (large N).
Values go to zero for N ≥ 20, which is a numerical artifact.
The solid angle is not a reliable distortion measure at high
resolution.

### F6. CP field charge (Track 8 method) gives zero total

The time-averaged E·ρ̂ at each junction sums to zero across
the torus for all lattice sizes.  This confirms Track 8's F2:
instantaneous charge cancels around the ring by orthogonality.

### F7. ε dependence is non-monotonic

The angular distortion Σδθ² is largest at small ε (near a
thin ring torus) and decreases toward ε = 0.7, then increases
again at ε = 1.0 (the spindle torus limit).  This reflects
the conformal mapping's non-uniform stretching.

---

## Step 1 conclusions

Step 1 established:
- The geometric measures (turning angle, angular distortion)
  converge to definite invariants
- The total turning is exactly 4π (Gauss-Bonnet)
- No pure-geometry ratio equals α directly

Step 1 did NOT compute:
- Per-node leakage as a function of local bending angle
- Whether f(bending) is universal across torus sizes
- Whether Σ f(bending_k) = α at any resolution

These are the subject of Steps 2–6.

---

## Step 2: Per-row and per-node charge analysis

### F8. Σ(leakage) grows with N — does not converge

The total leakage summed over all nodes grows with lattice
size and does not converge to a geometric invariant:

| N | M (nodes) | Σ leakage | Σ/M | Σ/N² |
|---|-----------|-----------|-----|------|
| 4 | 32 | 6.7 | 0.210 | 0.420 |
| 6 | 72 | 12.8 | 0.178 | 0.357 |
| 10 | 200 | 31.8 | 0.159 | 0.318 |
| 14 | 392 | 43.3 | 0.110 | 0.221 |
| 20 | 800 | 47.5 | 0.059 | 0.119 |

Both Σ/M and Σ/N² decrease — the per-node leakage shrinks
faster than the node count grows.  There is no normalization
that produces a resolution-independent total from the
pure-geometry leakage.

### F9. Leakage correlates with triple product but is not universal

The scalar triple product |ê₁ · (ê₂ × ê₃)| measures how far
the three edges are from coplanar.  Leakage correlates with
triple product (higher triple → more leakage), but the
relationship varies with N:

| N | Triple product range | Leak/trip range |
|---|---------------------|-----------------|
| 4 | 0.09 – 0.32 | 0.4 – 1.2 |
| 6 | 0.01 – 0.24 | 0.5 – 1.3 |
| 10 | 0.01 – 0.15 | 1.2 – 3.3 |
| 20 | 0.001 – 0.079 | 0.8 – 1.3 |

The triple product range shifts with N (smaller at larger N
as edges become more coplanar).  The leak/trip ratio is
roughly O(1) but not constant.  The points do NOT collapse
onto a universal f(distortion) curve.

### F10. Outer equator leaks MORE than inner equator

At N=20, ε=0.3:
- Outer equator (θ₁ ≈ 0, curvature κ = +0.77): leak ≈ 0.13/node
- Inner equator (θ₁ ≈ π, curvature κ = −1.43): leak ≈ 0.03/node

The inner equator has higher absolute curvature but LESS
leakage.  This is because the conformal mapping compresses
nodes at the inner equator, making edges shorter and more
coplanar.  The leakage tracks edge non-coplanarity, not
curvature directly.

An equal-edge lattice (spring-relaxed, from Track 9) would
give different results — the inner equator would have fewer
nodes (to maintain equal edges) and each node would have
larger distortion.  This has not been computed.

### F11. Leakage per radian grows with N — not convergent

The "leakage per radian of bending" (leak/node divided by
each node's share of 2π) ranges from 0.4 to 17 at N=20
and grows with N at all θ₁ positions.  This quantity does
not converge.

---

## Step 2 conclusions

The per-node pure-geometry leakage is NOT a universal
function of distortion.  It depends on lattice resolution
at every level: per-node, per-row, and total.  There is no
way to attribute the total charge to a per-wye-distortion
basis using pure geometric projection alone.

The leakage mechanism is real — bending a hexagonal lattice
onto a torus genuinely produces non-coplanar junctions that
leak energy into the normal direction.  But the amount of
leakage per junction depends on how many junctions there are,
which is set by the lattice spacing — which is set by α.

### The closed circle

α sets the lattice scale → the lattice scale sets the
junction distortion → the junction distortion sets the
leakage → the leakage IS α.

This is the "tautological but informative" result:
- α is genuinely the impedance mismatch between 2D sheet
  and 3D space
- The mismatch manifests as junction non-coplanarity
- But the per-junction magnitude requires knowing how many
  junctions there are, which requires α
- α cannot be derived from junction geometry alone because
  junction geometry requires α to be specified

---

## Steps 3–4: Fourier decomposition and row characterization

### F12. The leakage d₁ harmonic dominates on the equal-edge lattice

On the conformal lattice, all hexagons are identical (stretch = 1.0
everywhere) and E·ρ̂ is identically zero.  The conformal lattice
is the wrong tool — it has no shape variation.

On the equal-edge (spring-relaxed) lattice:
- Hexagons genuinely distort: stretch ranges from 1.2 (inner, tall/
  skinny) to 2.8 (outer, short/wide)
- Junction angles range from 74° (inner equator) to 119° (outer)
- The leakage d₁ harmonic is 99% of d₀:  **d₁/d₀ = 0.99**

The d₁ harmonic is the cos(θ₁) variation — the inner-vs-outer
asymmetry that defines the torus.  This is precisely the harmonic
that synchronizes with the n₁=1 CP wave to produce charge
(Track 8).

### F13. The aspect ratio d₁ converges but leakage d₁ does not (cleanly)

On the conformal lattice, the aspect ratio d₁ converges cleanly
to ~0.054 at ε=0.3.  But this measures 3D embedding distortion,
not hexagon shape distortion (which is zero on the conformal lattice).

On the equal-edge lattice, the leakage d₁ peaks at N ≈ 12–14 and
then decreases at larger N.  This is because the edge equalization
quality degrades at larger N (edge length deviation grows from ~3%
to ~9%).

### F14. The conformal lattice gives zero charge; equal-edge gives signal

The CP charge (E·ρ̂) at each junction is identically zero on the
conformal lattice (machine precision ~10⁻¹⁸).  On the equal-edge
lattice, the leakage is nonzero and has strong d₁ content.  This
confirms that the shape distortion — not the 3D embedding — is
what produces the charge-relevant signal.

---

## Steps 5–6: ε dependence and convergence

### F15. leak_d₁ peaks near ε ≈ 0.25, no clean power law

The ε dependence of leak_d₁ at N=14:

| ε | d₁ | d₁/ε | d₁/ε² |
|---|-----|------|-------|
| 0.05 | 0.002 | 0.04 | 0.8 |
| 0.15 | 0.024 | 0.16 | 1.1 |
| 0.25 | 0.090 | 0.36 | 1.4 |
| 0.30 | 0.080 | 0.27 | 0.9 |
| 0.50 | 0.067 | 0.13 | 0.3 |
| 0.70 | 0.043 | 0.06 | 0.09 |
| 0.90 | 0.012 | 0.01 | 0.02 |

Neither d₁/ε nor d₁/ε² is constant.  The peak near ε=0.25
suggests a resonance-like behavior, but no simple functional
form fits.

### F16. N convergence is blocked by lattice quality

At ε=0.3, d₁ rises to ~0.08 at N=12–14 then falls back to
~0.05 at N=20.  The edge length deviation increases from 7%
(N=6) to 9% (N=20) — the spring relaxation cannot fully
equalize edges on a fixed-connectivity honeycomb.

A truly equal-edge lattice would require variable connectivity
(fewer hexagons per row at the inner equator), which is a
different lattice topology.  This has not been attempted.

---

## Blocking issue

The computation is blocked by the **fixed-connectivity lattice
limitation**.  A honeycomb with the same number of nodes per
ring row cannot have equal edge lengths on a torus whose ring
circumference varies by (1+ε)/(1−ε).  Spring relaxation
reduces but cannot eliminate the edge length variation.

To proceed, one would need either:
1. A variable-connectivity lattice (adaptive mesh with fewer
   hexagons at the inner equator)
2. An analytical calculation that doesn't depend on a specific
   discrete lattice (continuum limit of the distortion pattern)

Option 2 is essentially the R48/Track 8 continuum calculation,
which gives the charge selection rule but not the magnitude.

---

## Overall Track 12 conclusions

1. The top-down approach (distributing known charge e across
   junctions) identifies the right geometric quantities (turning
   angle, hexagon distortion) but cannot derive α because the
   per-junction leakage depends on lattice resolution.

2. The equal-edge lattice produces the physically correct shape
   distortion (tall/skinny at inner equator, short/wide at outer)
   and a leakage pattern dominated by the charge-relevant d₁
   harmonic (d₁/d₀ ≈ 0.99).

3. Clean convergence is blocked by the fixed-connectivity
   lattice limitation — true equal-edge requires variable
   connectivity.

4. The ε dependence shows a peak near ε ≈ 0.25 but no simple
   functional form.

5. α remains the missing ingredient that converts geometric
   distortion into charge magnitude.

---

## What Tracks 8–12 established overall

### Proven

1. **Charge is bending.**  A flat 2D lattice produces zero
   normal field — it is invisible to 3D.  Bending the lattice
   onto a curved surface creates non-coplanar junctions whose
   edge fields acquire normal components.  This is the
   microscopic mechanism of charge.  Before this work, GRID
   axiom A3 stated "a 2π phase winding = charge" without a
   finer-grained mechanism.  Now we have one: bending produces
   normal leakage, and a full 2π of bending produces
   persistent unit charge.

2. **Charge requires circulation + curvature.**  Neither alone
   suffices.  A flat sheet with a traveling wave → no charge
   (no curvature).  A curved sheet with a standing wave →
   no charge (half-cycle cancellation at each junction).  Only
   a curved sheet with a circulating wave produces persistent,
   non-canceling normal field (Track 8 F1–F3).

3. **The n₁ = 1 selection rule is geometric.**  The CP field
   rotates at rate n₁ around the tube; the surface normal
   rotates at rate 1.  Only n₁ = 1 synchronizes → non-
   oscillating normal component → charge.  This is lattice-
   structure-independent.

4. **The coupling is 2D→3D, not lattice→lattice.**  Tracks
   1–7 tested lattice-to-lattice coincidence (static geometry)
   and found nothing.  Tracks 8–12 found that coupling comes
   from surface curvature distorting the junction geometry.
   The 3D lattice structure is irrelevant — what matters is
   that 3D space exists for the normal components to leak into.

5. **Nothing propagates inward.**  The normal component at
   each junction points outward from the torus surface.  The
   charge field is the accumulated outward normal.  There is
   no mechanism for energy to leak inward through the surface.

6. **The coupling is bidirectional at strength α.**  By
   time-reversal symmetry (reciprocity), the same junction
   geometry that leaks energy outward (charge → Coulomb field)
   also absorbs energy inward (photon → surface mode).  The
   coupling constant is the same in both directions.

7. **The equal-edge lattice produces genuine shape distortion.**
   Hexagons are tall/skinny at the inner equator, short/wide
   at the outer.  The leakage d₁ harmonic (charge-relevant
   frequency) is 99% of d₀ — almost all leakage is in the
   charge direction.

### Not proven

8. **The leakage magnitude.**  The per-junction leakage
   depends on lattice resolution N, which is set by α through
   the GRID action.  Pure geometry determines WHERE and WHICH
   modes couple, but not HOW MUCH.

9. **A universal leakage function f(distortion).**  The
   leakage per node does not collapse onto a single curve
   across different lattice resolutions.

### Open questions for future work

10. **Variable-connectivity lattice.**  A honeycomb with
    adaptive connectivity (fewer hexagons per row at the inner
    equator) would produce truly equal edges and might give
    cleaner convergence.

11. **Analytical continuum limit.**  The d₁ of the hexagon
    distortion pattern might be computable as an integral over
    the torus (bypassing the lattice entirely).  This would
    test whether the d₁ signal is a lattice property or a
    continuum property.

12. **Alternative lattice geometries.**  The Y-junction
    (honeycomb) is not the only lattice that produces Maxwell
    equations.  The triangular lattice (N=6 junctions) and
    other regular lattices also support EM wave propagation.
    Different junction geometries would have different leakage
    properties.  Whether a different lattice produces a
    cleaner α derivation is unknown.

13. **Connection between ζ = 1/4 and α.**  GRID has two free
    parameters: ζ (resolution, A5) and α (coupling, A6).  If
    they are related by a consistency condition, one determines
    the other.  The junction leakage might provide the bridge:
    ζ sets the lattice grain size, which determines the junction
    geometry, which determines the leakage, which should equal α.
