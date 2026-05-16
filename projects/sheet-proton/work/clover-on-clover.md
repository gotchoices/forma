# clover-on-clover.md — Specification for the fractal clover construction

**Status:** Specification for the nested fractal clover construction proposed as the geometric substrate for [3-gen.md](3-gen.md) Mechanism E. Defines the construction precisely enough to be programmed and rendered, with explicit parametric flexibility for fitting observed inter-generation mass ratios. Companion to [clover-quarks.md](clover-quarks.md) (level-0 kissing-circle profile) and [tube-waveguide.md](tube-waveguide.md) (the 3D wave-guide framework the cross-section feeds into).

**Tone:** Mathematical specification. Geometric choices are recorded as defaults with named alternatives where applicable. Each free parameter is named and its role in mass-fitting identified.

---

## 1. Construction goal

A nested fractal cross-section profile for the corrugated torus that:

1. Preserves the **+2/3 / −1/3 per-arc charge fractions at every fractal level** (by maintaining 240° / 120° angular extents on circular arcs at every scale).
2. Provides **three distinct geometric length scales** (one per generation).
3. Allows **per-level parameters** (radii and proportions) to be tuned for fitting observed quark masses, in the Mechanism E style.
4. Closes to a **simple closed plane curve** at every finite recursion level (no self-intersections, no topology violations).
5. Maintains **C¹ continuity** (matching tangent directions at every junction; no corners).

The construction defines the **2D cross-section boundary** of the corrugated torus. The 2D region enclosed by this boundary is the domain on which [tube-waveguide.md](tube-waveguide.md)'s 2D Helmholtz eigenvalue problem is solved. The ring sweep is uniform (the fractal cross-section is extruded smoothly around the ring with the standard 1/3 twist from [clover-quarks.md](clover-quarks.md) §9–10).

---

## 2. Level 0 — the base clover

The level-0 clover is the kissing-circle profile of [clover-quarks.md](clover-quarks.md) §7. This specification adopts that geometry verbatim.

### 2.1 Composition

The profile consists of:

- **3 convex lobe arcs**, each a 240° arc of a circle of radius **r_lobe_0**.
- **3 concave saddle arcs**, each a 120° arc of a circle of radius **r_saddle_0**.
- Arranged alternately around the cross-section center with 3-fold rotational symmetry (D₃ group).

### 2.2 Center positions

Lobe-arc-circle centers (the centers of the kissing circles that contain the lobe arcs):

- Angular positions: θ_L = 90°, 210°, 330°
- Radial distance from cross-section center: **D_lobe** (free parameter — sets overall scale)

Saddle-arc-circle centers:

- Angular positions: θ_S = 30°, 150°, 270°
- Radial distance: **D_saddle** (determined by the kissing constraint below)

### 2.3 Kissing constraint

Each adjacent (lobe, saddle) pair shares a tangent point. With lobe and saddle centers 60° apart in angle (by 3-fold symmetry), the distance between an adjacent lobe center and saddle center is:

<!-- d = sqrt(D_lobe^2 + D_saddle^2 − 2·D_lobe·D_saddle·cos 60°) -->
$$
d \;=\; \sqrt{D_{\mathrm{lobe}}^2 + D_{\mathrm{saddle}}^2 - D_{\mathrm{lobe}}\, D_{\mathrm{saddle}}}
$$

Setting d = r_lobe_0 + r_saddle_0 (external tangency between the two kissing circles):

<!-- D_lobe^2 − D_lobe·D_saddle + D_saddle^2 = (r_lobe_0 + r_saddle_0)^2 -->
$$
D_{\mathrm{lobe}}^2 - D_{\mathrm{lobe}}\, D_{\mathrm{saddle}} + D_{\mathrm{saddle}}^2 \;=\; (r_{\mathrm{lobe}_0} + r_{\mathrm{saddle}_0})^2
$$

This gives D_saddle in terms of D_lobe, r_lobe_0, r_saddle_0. The construction has 3 free geometric parameters at level 0: D_lobe, r_lobe_0, r_saddle_0.

### 2.4 Tangent points

Each lobe-saddle junction sits on the line connecting the two circle centers, at distance r_lobe_0 from the lobe center and r_saddle_0 from the saddle center.

### 2.5 Charge fractions at level 0

By Gauss-Bonnet on individual arc segments:

  Q_lobe = (1/2π) ∫_arc κ ds = (1/2π) × (1/r_lobe_0) × (r_lobe_0 × 4π/3) = **+2/3**
  Q_saddle = (1/2π) × (−1/r_saddle_0) × (r_saddle_0 × 2π/3) = **−1/3**

Radii cancel — only the angular extents (240°, 120°) matter. These are the up and down quark charges.

---

## 3. Recursive rule: level n → level n+1

At each fractal level, every arc segment of the level-n profile (whether a lobe arc or a saddle arc) receives a **balanced sub-feature unit** inscribed on it.

### 3.1 The balanced unit

Per parent arc at level n, one inscribed unit at level n+1 consists of:

- **1 sub-lobe**: 240° arc of radius **r_lobe_{n+1}**
- **2 sub-saddles**: each a 120° arc of radius **r_saddle_{n+1}**

Curvature contribution of the unit:

<!-- ∫ κ ds = (4π/3) + 2 × (−2π/3) = 0 -->
$$
\sum_{\mathrm{unit}} \int \kappa\, ds \;=\; \frac{4\pi}{3} + 2 \cdot \left(-\frac{2\pi}{3}\right) \;=\; 0
$$

**The unit's net curvature contribution to the parent arc is zero.** Consequently the parent arc's ∫κ ds is preserved, and the parent-level closure-path charge (±2/3 or ∓1/3) is preserved at the parent's level.

The balanced unit applies uniformly to both parent lobes and parent saddles — the geometric arrangement differs (orientation depends on parent convexity) but the composition (1L + 2S) is identical.

### 3.2 Spatial arrangement along parent arc

The default placement is **single-unit, centered, symmetric**:

- One balanced unit per parent arc, centered on the parent arc's midpoint.
- Sub-lobe at the midpoint of the parent arc.
- Sub-saddle 1 and sub-saddle 2 symmetric about the midpoint, with sub-saddle 1 on the "incoming" side and sub-saddle 2 on the "outgoing" side along the parent arc's traversal direction.

Traversal order along the parent arc:

  [smooth parent arc segment] → [sub-saddle 1] → [sub-lobe] → [sub-saddle 2] → [smooth parent arc segment]

The two smooth-parent-segment portions at the start and end of the parent arc are mirror images of each other under reflection about the parent arc's midpoint.

**Alternative arrangements** (deferred unless mass-fitting requires more degrees of freedom):

- **Multi-unit**: place K balanced units uniformly along each parent arc (K = 2, 3, ...).
- **Type-asymmetric**: place units only on parent lobes, leaving parent saddles smooth (or vice versa). Halves the number of sub-features and may simplify the spectrum.
- **Off-center**: shift the unit position toward one end of the parent arc.

For now, the spec assumes single-unit centered placement on every parent arc.

### 3.3 C¹ continuity (tangency) constraints

Each junction between a parent arc and an inscribed sub-feature, and between adjacent sub-features within the unit, must have matching tangent directions.

**Junction type 1 — parent arc to sub-saddle**, where parent is a lobe (convex) and sub-saddle is concave:

The parent arc curves "outward" (convex toward cross-section interior), while the sub-saddle curves "inward" (concave). At the junction, tangent directions match but curvatures flip sign. The two kissing circles are on **opposite sides of the curve**: external tangency.

  distance(parent_circle_center, sub_saddle_center) = r_lobe_n + r_saddle_{n+1}

**Junction type 2 — sub-saddle to sub-lobe** within the unit:

Sub-saddle curves inward, sub-lobe curves outward. External tangency.

  distance(sub_saddle_center, sub_lobe_center) = r_lobe_{n+1} + r_saddle_{n+1}

**Junction type 3 — parent arc to sub-saddle**, where parent is a saddle (concave) and sub-saddle is also concave:

Both arcs concave, curving the same direction at the junction. Internal tangency.

  distance(parent_saddle_center, sub_saddle_center) = |r_saddle_n − r_saddle_{n+1}|

For the construction to be physically realizable: r_saddle_{n+1} < r_saddle_n in this case.

### 3.4 Constraints on sub-feature radii

The combination of tangency conditions and symmetric placement determines the geometric layout uniquely given the radii (r_lobe_{n+1}, r_saddle_{n+1}) and the parent arc geometry (r_n, parent arc length).

A balanced unit must fit within its parent arc. The total arc length occupied by the inscribed unit is:

<!-- L_unit = (4π/3) r_lobe_{n+1} + 2 × (2π/3) r_saddle_{n+1} = (4π/3)(r_lobe_{n+1} + r_saddle_{n+1}) -->
$$
L_{\mathrm{unit}} \;=\; \frac{4\pi}{3} r_{\mathrm{lobe}_{n+1}} + 2 \cdot \frac{2\pi}{3} r_{\mathrm{saddle}_{n+1}} \;=\; \frac{4\pi}{3}\bigl(r_{\mathrm{lobe}_{n+1}} + r_{\mathrm{saddle}_{n+1}}\bigr)
$$

This must be less than the parent arc length L_parent (which is (4π/3) r_lobe_n for a parent lobe or (2π/3) r_saddle_n for a parent saddle). The constraint:

  r_lobe_{n+1} + r_saddle_{n+1} < r_lobe_n   (for parent lobes)
  r_lobe_{n+1} + r_saddle_{n+1} < r_saddle_n / 2   (for parent saddles)

The second constraint is tighter (saddle parent arc is shorter). To keep sub-feature radii small enough for both parent types, use the saddle constraint as the binding one.

### 3.5 Charge derivation at level n+1

By the same Gauss-Bonnet computation as level 0:

  Q_sub_lobe = +2/3   (radius cancels — only the 240° angular extent matters)
  Q_sub_saddle = −1/3

These are the per-feature charges accumulated by a closure path that winds once around a single sub-feature at the sub-scale.

The parent arc's charge contribution to a closure path that winds at the parent scale (encircling the entire parent feature, not zooming into the sub-feature) is preserved exactly because the inscribed unit contributes zero net ∫κ ds.

**Result:** charges are preserved at every level: ±2/3 for lobes (and sub-lobes, and sub-sub-lobes), ∓1/3 for saddles (and sub-saddles, ...).

---

## 4. Parameter scheme for Mechanism E fitting

### 4.1 Per-level free parameters

For an N-level construction (levels 0 through N−1):

| Level | Geometric parameters | Physical role |
|---|---|---|
| 0 | r_lobe_0, r_saddle_0 (or χ_0 ≡ r_saddle_0/r_lobe_0) | Gen-1 quark masses (m_u, m_d) |
| 1 | r_lobe_1, r_saddle_1 (or ρ_1 ≡ r_lobe_1/r_lobe_0, χ_1) | Gen-2 quark masses (m_c, m_s) |
| 2 | r_lobe_2, r_saddle_2 (or ρ_2 ≡ r_lobe_2/r_lobe_1, χ_2) | Gen-3 quark masses (m_t, m_b) |

Plus one overall scale parameter D_lobe (or equivalently the cross-section's bounding radius), set by the proton-mass calibration.

Total: 2 free parameters per level × 3 levels + 1 scale = **7 parameters**.

### 4.2 Reparameterization for fitting

The natural Mechanism E parameterization uses dimensionless ratios:

- **ρ_n ≡ r_lobe_n / r_lobe_{n−1}** (inter-level shrinkage). Defined for n ≥ 1.
- **χ_n ≡ r_saddle_n / r_lobe_n** (per-level asymmetry between sub-lobe and sub-saddle radii at the same level). Defined for n ≥ 0.

Parameter list: D_lobe, r_lobe_0, χ_0, ρ_1, χ_1, ρ_2, χ_2 — 7 numbers.

### 4.3 Mass-scaling formulas

Modes resolving level n have eigenvalues scaling as:

  λ_up_n ~ 1 / r_lobe_n²    (mode localized to a level-n sub-lobe)
  λ_down_n ~ 1 / r_saddle_n² (mode localized to a level-n sub-saddle)

Generation assignment:

- Gen 1 (u, d): modes localized at level 0 (main lobes/saddles).
- Gen 2 (c, s): modes localized at level 1.
- Gen 3 (t, b): modes localized at level 2.

Mass ratios in terms of the dimensionless parameters:

  m_d / m_u = r_lobe_0 / r_saddle_0 = 1/χ_0
  m_c / m_u = r_lobe_0 / r_lobe_1 = 1/ρ_1
  m_s / m_d = r_saddle_0 / r_saddle_1 = 1/(ρ_1 · χ_1/χ_0)
  m_t / m_c = r_lobe_1 / r_lobe_2 = 1/ρ_2
  m_b / m_s = r_saddle_1 / r_saddle_2 = 1/(ρ_2 · χ_2/χ_1)

Observed ratios with target values for the fit:

| Ratio | Observed | Constraint |
|---|---|---|
| m_d/m_u | 2.13 | χ_0 ≈ 0.47 |
| m_c/m_u | 580 | ρ_1 ≈ 1/24.1 |
| m_s/m_c | 0.073 | χ_1 ≈ 0.073 (smaller than χ_0; sign of asymmetry "flipped" relative to gen 1) |
| m_t/m_c | 135 | ρ_2 ≈ 1/11.6 |
| m_b/m_t | 0.024 | χ_2 ≈ 0.024 |

(The numerical values are PDG current-quark masses. The χ-sign flip between level 0 and levels 1, 2 is the within-generation flavor-ordering anomaly — automatically accommodated by free per-level χ_n.)

### 4.4 Parameter parity

Six independent quark masses + one proton charge radius = 7 observables. Seven free parameters in the spec. **Parameter parity** — fitting is feasible but not predictive without additional substrate-level constraints on the ρ_n and χ_n sequences. The Mechanism E framework treats this as a fit, not a derivation; the predictive content depends on later structural arguments that would constrain the ratios.

---

## 5. Algorithmic specification

### 5.1 Data structures

Represent the cross-section as an ordered list of arc segments. Each arc segment is a tuple:

  Arc = (center_xy, radius, start_angle, end_angle, sign)

where:

- **center_xy** is the 2D position of the kissing circle's center
- **radius** is the kissing circle's radius
- **start_angle, end_angle** specify the arc's angular extent on the circle (degrees or radians)
- **sign** is +1 (convex / lobe-like, traversing CCW on the circle) or −1 (concave / saddle-like, traversing CW)

A complete cross-section is a list of arcs joined end-to-end forming a simple closed curve.

The recursion replaces each arc in the list with a new sublist of arcs (the smooth parent portions plus the inscribed unit's three sub-arcs):

```
Arc → [Arc_partial_parent_1, Sub_saddle_1, Sub_lobe, Sub_saddle_2, Arc_partial_parent_2]
```

After N levels of recursion, the cross-section has roughly 5^N arc segments (each parent splits into 5 children: 2 smooth parent portions + 3 sub-feature arcs).

### 5.2 Construction algorithm sketch

```
function build_clover_on_clover(D_lobe, r_lobe_0, χ_0, [ρ_1, χ_1], [ρ_2, χ_2], ...):
    # Level 0
    arcs = build_level_0_clover(D_lobe, r_lobe_0, r_saddle_0 = χ_0 · r_lobe_0)
    
    # Recursive levels
    for n in 1 .. N-1:
        r_lobe_n = ρ_n · r_lobe_{n-1}
        r_saddle_n = χ_n · r_lobe_n
        new_arcs = []
        for arc in arcs:
            inscribed_arcs = inscribe_balanced_unit(arc, r_lobe_n, r_saddle_n)
            new_arcs.extend(inscribed_arcs)
        arcs = new_arcs
    
    return arcs

function build_level_0_clover(D_lobe, r_lobe_0, r_saddle_0):
    # Solve D_saddle from kissing constraint
    D_saddle = solve_kissing(D_lobe, r_lobe_0, r_saddle_0)
    # Place 3 lobe circles at angles 90, 210, 330 and 3 saddle circles at 30, 150, 270
    # Compute tangent points
    # Return ordered list of 6 arcs (3 lobes + 3 saddles, alternating)
    return arcs

function inscribe_balanced_unit(parent_arc, r_sub_lobe, r_sub_saddle):
    # Split parent arc at the midpoint
    # Determine entry/exit points for the inscribed unit (positions where unit meets parent)
    # Compute sub-saddle centers (tangent to parent arc, on appropriate side based on parent convexity)
    # Compute sub-lobe center (tangent to both sub-saddles, on appropriate side)
    # Construct 5 child arcs: parent_partial_1, sub_saddle_1, sub_lobe, sub_saddle_2, parent_partial_2
    return list_of_5_arcs
```

### 5.3 Tangency solver

The core geometric primitive is "given parent arc and sub-feature radii, find the sub-feature center positions and the parent-arc partial-segment endpoints such that C¹ continuity holds at all junctions and the unit is centered on the parent arc midpoint."

This is a constrained geometric problem with closed-form solutions in each case (different formulas for lobe-vs-saddle parent and lobe-vs-saddle sub-feature). The solver should handle:

- Parent lobe (convex) + sub-saddle (concave): external tangency
- Sub-saddle + sub-lobe (within the unit): external tangency
- Parent saddle (concave) + sub-saddle (concave): internal tangency

Sign and side conventions need explicit treatment to ensure the inscribed unit lies on the **correct side** of the parent arc — outward bumps for parent lobes, inward bumps for parent saddles (or vice versa, depending on chosen convention).

### 5.4 Recommended convention

Within the cross-section's interior region:

- **Parent lobe** (curve bulges away from cross-section center): inscribed unit bumps **inward** (sub-lobe is a small inward indentation, sub-saddles are tiny outward bulges). This places the additional curvature variation on the interior side of the parent arc, preserving the cross-section's overall outline.
- **Parent saddle** (curve indents toward center): inscribed unit bumps **outward** (sub-lobe is a small outward bulge into the indented region, sub-saddles are tiny inward dips).

Alternative convention (opposite sign for all bumps) is equally valid and produces a mirror-image cross-section.

The choice affects the **2D region's shape** (the interior of the cross-section boundary) and therefore the eigenmode spectrum, but does not affect the per-arc charge derivations.

---

## 6. Implementation hooks

### 6.1 Sketch script (Python)

A minimal Python implementation should produce:

- A function `build_cross_section(params)` returning the arc list.
- A function `render(arcs, output_path)` producing a 2D plot (matplotlib or SVG) of the closed curve.
- A function `compute_charges(arcs)` integrating ∫κ ds over each arc and verifying ±2/3 / ∓1/3 fractions.
- A function `arc_length_total(arcs)` returning the total cross-section perimeter (for verification of the fractal length divergence).

### 6.2 Mesh generation for eigenvalue analysis

For input into [tube-waveguide.md](tube-waveguide.md)'s 2D Helmholtz solver:

- Discretize each arc into many short line segments (resolution sufficient to resolve the finest sub-features).
- Build a 2D mesh of the interior region using a standard mesh generator (e.g., `meshpy`, `gmsh`, or `pyvista`).
- Apply Dirichlet boundary conditions on the cross-section boundary.
- Solve the 2D Helmholtz eigenvalue problem to get λ_α and ψ_α(x_⊥).

The mesh refinement must be fine enough to resolve the level-N features (mesh size ≲ r_lobe_N / 10).

### 6.3 Eigenmode classification

For each eigenmode ψ_α, compute the spatial concentration measure:

  P_n(α) = ∫ |ψ_α|² · 𝟙_{level-n features} dA / ∫ |ψ_α|² dA

where 𝟙_{level-n features} is the indicator of the level-n sub-feature regions (lobes or saddles at scale r_n).

A mode α is classified as:

- **Level-n lobe-localized** if P_n^lobe is dominant for some n.
- **Level-n saddle-localized** if P_n^saddle is dominant.
- **Whole-cross-section** if no level dominates (delocalized).

This classification assigns each eigenmode to a (generation, flavor) pair for comparison with observed quark masses.

---

## 7. Test cases

### 7.1 Level 0 only (no recursion)

Run with N = 1 (level 0 only). The construction should reproduce the existing clover-quarks profile. Eigenvalues should match clover-mass / tube-waveguide results.

### 7.2 Level 0 + symmetric inscribed units (uniform ρ and χ)

Run with N = 2, ρ_1 = 0.5, χ_1 = χ_0 = 0.5. Verify:

- The construction closes to a simple closed curve.
- The C¹ continuity holds at all junctions (visual check via tangent rendering).
- The eigenvalue spectrum exhibits a new mode at λ ≈ 1/r_lobe_1² ≈ 4/r_lobe_0².

### 7.3 Mass-fit run

Run with N = 3 and the Mechanism E target parameters:

  D_lobe = (whatever calibrates m_proton)
  r_lobe_0 = 1.0 (set scale)
  χ_0 = 0.47
  ρ_1 = 1/24
  χ_1 = 0.073
  ρ_2 = 1/12
  χ_2 = 0.024

Verify the level-1 and level-2 eigenvalues match the observed gen-2 and gen-3 quark masses to within the numerical precision of the solver.

---

## 8. Open architectural questions

These are deferred until after the initial implementation produces results:

1. **Unit-per-arc count.** The default places one balanced unit per parent arc. If mass-fitting needs more flexibility, multi-unit placements (K units per parent) are a natural extension.

2. **Type-asymmetric inscription.** The spec inscribes units on both lobes and saddles uniformly. An asymmetric variant (units on lobes only, saddles smooth) would halve the sub-feature count and might still produce a full mode tower with simpler spectrum.

3. **Convention sign choice.** Inward-bumping vs outward-bumping unit orientation gives different cross-section interiors. Test both for which produces cleaner mode localization.

4. **Multi-unit periodic placement.** For a parent arc with K balanced units uniformly spaced, the sub-features form a regular array. This may give cleaner Bloch-band structure (analogous to a 1D periodic potential) at the sub-level.

5. **Different balanced units.** The (1, 2) unit is the minimal balanced unit. Larger balanced units exist: (2, 4), (3, 6), etc. These provide more sub-features per parent arc and potentially more mode-tower resolution.

6. **Closure-path identification across levels.** At each level, the path-winding closure conditions of clover-quarks §12 need to be re-evaluated. The simple closure for the level-0 proton (2 lobes + 1 saddle) generalizes to level-n closures that include sub-features; the exact closure rule is an open derivation.

---

## 9. Next actions

1. **Implement Section 5's algorithm** as a Python module under `sheet-proton/scripts/clover_on_clover.py`. Verify the level-0 construction matches existing rendering.

2. **Render the test cases** of §7. Visually inspect closure, smoothness, and feature placement. Sanity-check the charge integrals.

3. **Generate a 2D mesh** of the cross-section interior at each test case. Feed into the existing 2D Helmholtz solver (extended from [scripts/laplacian_spectrum.py](../scripts/laplacian_spectrum.py) or whatever the active solver is).

4. **Compute the eigenmode spectrum** and classify by localization level. Compare predicted gen-1, gen-2, gen-3 mass ratios to observed.

5. **If the predicted spectrum matches observation:** the Mechanism E hypothesis passes Phase 4 numerical verification, and the work file [3-gen.md](3-gen.md) §5.5's parameter-parity fit becomes a concrete construction.

6. **If it does not match:** investigate the open architectural questions of §8 (multi-unit, type-asymmetric, sign convention) before falling back to alternative mechanisms.

---

## 10. Cross-references

- [clover-quarks.md §7](clover-quarks.md) — kissing-circles construction of the level-0 clover.
- [clover-quarks.md §11](clover-quarks.md) — per-arc curvature charge derivation (+2/3, −1/3); the basis for the per-level charge preservation here.
- [3-gen.md §5.5](3-gen.md) — Mechanism E framework that this construction realizes geometrically.
- [tube-waveguide.md](tube-waveguide.md) — 2D Helmholtz eigenvalue framework that the cross-section feeds into.
- [primers/convex-integration.md](../../../primers/convex-integration.md) — background on the Hévéa-style nested corrugation construction this spec is structurally inspired by.
