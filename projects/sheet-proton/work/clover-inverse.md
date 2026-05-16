# clover-inverse.md — V2 cross-section geometry

**Status:** Geometric specification for a SECOND clover-style cross-section variant. Built and verified to close (∫κ ds = 2π) by `scripts/clover_inverse.py`. Parallel to [clover-on-clover.md](clover-on-clover.md) (the V1 "lobe + saddle" clover); intended as an alternative substrate for the proton-sheet mass-mechanism work.

**Naming convention (proposed):**

- **V1 = "clover"** — the canonical 3-lobe + 3-saddle profile, with 240° convex lobe arcs and 120° concave saddle arcs. Per-arc charges +2/3 and −1/3. Documented in [clover-on-clover.md](clover-on-clover.md). Implemented in `scripts/clover_on_clover.py`.
- **V2 = "clover-inverse"** — the structure described in this file: 3 outer convex lobes + 3 inner concave lobes + 6 short connectors. Per-arc charges +2/3, −2/3, and +1/6. Implemented in `scripts/clover_inverse.py`.

The two variants are distinct geometric models, not refinements of each other. Both will be candidates for the eigenmode analysis once a unified solver is built.

---

## 1. Construction

### 1.1 Primitives

Three feature types arranged with 3-fold rotational symmetry (D₃):

| Feature | Count | Type | Angular extent | Per-arc charge Q |
|---|---|---|---|---|
| Outer lobe | 3 | convex (sign +1) | 240° | +2/3 |
| Inner lobe | 3 | concave (sign −1) | 240° | −2/3 |
| Connector | 6 | convex (sign +1) | 60° | +1/6 |

Total ∫κ ds: 3·(+240°) + 3·(−240°) + 6·(+60°) = **+360° = 2π** ✓ simple closed plane curve.

### 1.2 Placement and radii

Lobe and connector kissing-circle centers sit on 3-fold-symmetric rays from the cross-section center.

- **Outer lobes** at angular positions {0°, 120°, 240°}, radial distance D_outer from origin.
- **Inner lobes** at angular positions {60°, 180°, 300°}, radial distance D_inner from origin.
- **Connectors** at intermediate angular positions between each adjacent outer-inner pair, with kissing-circle centers determined by tangency.

Solving the tangent-matching constraints (outer ↔ connector: convex-convex same-side tangency; connector ↔ inner: convex-concave external tangency), the radial distances are forced:

  **D_outer = r_outer + r_inner**
  **D_inner = r_outer − r_conn**

So the **three radii** (r_outer, r_inner, r_conn) are the free parameters; the placement geometry follows.

### 1.3 Per-arc geometry

For outer lobe k (k = 0, 1, 2) at angular position α_k = 2πk/3:

- Kissing circle center: D_outer · (cos α_k, sin α_k).
- 240° convex CCW arc spanning from angle (α_k − 2π/3) to (α_k + 2π/3) on the kissing circle.
- Outermost point at α_k on the kissing circle, distance D_outer + r_outer from origin.

For inner lobe at angular position α_k + π/3 (between outer-k and outer-(k+1)):

- Kissing circle center: D_inner · (cos(α_k + π/3), sin(α_k + π/3)).
- 240° concave CW arc spanning from angle (α_k + π/3 − π/3) = α_k to (α_k + π/3 + π/3 − 4π/3) = (α_k − 2π/3) on the kissing circle.
- Innermost point at (α_k + π/3 + π) on the kissing circle, distance D_inner − r_inner from origin.

For connector "up" from outer-k to inner at α_k + π/3:

- Kissing circle center: C_outer-k + (r_outer − r_conn) · (cos(α_k + 2π/3), sin(α_k + 2π/3)).
- 60° convex CCW arc spanning from angle (α_k + 2π/3) to (α_k + 2π/3 + π/3) on the kissing circle.

For connector "down" from inner at α_k + π/3 to outer-(k+1):

- Mirror of the "up" connector across the inner-lobe's axis. Same radius r_conn, kissing-circle center determined by external tangency with the inner-lobe at the inner-lobe's exit junction.

---

## 2. Free parameters and bounds

### 2.1 The three free radii

| Parameter | Role | Bounds |
|---|---|---|
| r_outer | overall scale of outer lobes | r_outer > 0 |
| r_conn | width of connector arcs | 0 < r_conn < r_outer |
| r_inner | depth of inner-lobe inward bulge | 0 < r_inner < (r_outer − r_conn) · √3/2 |

The r_outer parameter sets overall scale (analogous to V1's r_lobe). r_conn and r_inner can both be tuned independently subject to their bounds.

### 2.2 Where the bounds come from

**Inner-lobe doesn't cross origin** (innermost point at distance D_inner − r_inner > 0):

  r_inner < r_outer − r_conn

**Adjacent inner-lobes don't overlap** (distance between adjacent inner-lobe kissing centers > 2 r_inner):

  D_inner · √3 > 2 r_inner   ⟹   r_inner < (r_outer − r_conn) · √3/2

The second bound is tighter than the first, so it's the binding constraint on r_inner.

### 2.3 Parameter count comparison

| Construction | Free parameters at base level |
|---|---|
| V1 (clover) | 2 (r_lobe, r_saddle) |
| V2 (clover-inverse) | 3 (r_outer, r_inner, r_conn) |

V2 has one more degree of freedom than V1 at the base. This may translate into more flexibility for mass-fitting if extended with fractal recursion.

---

## 3. Per-arc charge analysis

The per-arc charges Q = (1/2π) ∫_arc κ ds depend only on the angular extent (radius cancels), inheriting the [clover-quarks.md §11](clover-quarks.md) machinery:

  Q_outer = (1/2π) × (1/r_outer) × (240° · r_outer / 180° · π) = **+240°/360° = +2/3**
  Q_inner = (1/2π) × (−1/r_inner) × (240° · r_inner / 180° · π) = **−240°/360° = −2/3**
  Q_conn  = (1/2π) × (1/r_conn) × (60° · r_conn / 180° · π) = **+60°/360° = +1/6**

**Comparison with V1:**

| Feature | V1 charge | V2 charge | Standard model? |
|---|---|---|---|
| Outer lobe | +2/3 (V1 lobe) | +2/3 | matches up-type |
| Inner lobe | −1/3 (V1 saddle) | **−2/3** | matches up-type anti, not down |
| Connector | n/a | +1/6 | non-standard |

V2's inner lobe carries charge **−2/3**, which doesn't directly map to a Standard Model quark (down-type quarks have −1/3, anti-up-type have −2/3). Interpretations to consider:

- **Anti-up reading.** Inner lobe = anti-quark of an up-type quark. Combined with the +2/3 outer lobe, V2 might represent a meson-like substrate (uū pair) rather than a quark-content substrate.
- **Half-arc decomposition.** If each 240° inner lobe is read as two 120° half-arcs, each half contributes −1/3 — recovering the V1 down-quark assignment. Then a "down quark" is half of an inner lobe.
- **Connector ambiguity.** The +1/6 connector charge doesn't fit any quark fraction. Could be a feature requiring physical reinterpretation, or an artifact of the geometric construction not corresponding to a particle.

These interpretations are open; this file does not commit to one.

---

## 4. Optional level-2 fractal recursion (sketch)

A V2 fractal recursion analogous to [clover-on-clover.md](clover-on-clover.md) §3:

- For each outer lobe (parent A = 240°): bisect, remove central 120°, insert primitive with sub-lobes of A/2 = 120° each and sub-saddles of A/4 = 60° each. Net primitive rotation +120° matches removed parent rotation. Preserves closure.
- For each inner lobe (parent A = 240°, concave): bisect, remove central 120°. Insert *inverted* primitive: sub-lobes concave 120° and sub-saddles convex 60°. Net rotation −120° matches removed concave rotation.
- Connectors are not bisected (only lobes are).

Closure constraint for level-2 primitives, parameterized by parent's angular extent A:

  r_p = 2 r_L_new · cos(A/4) + r_S_new · (2 cos(A/4) − 1)

Same form as V1. For A = 240° (parent extent here), this gives a per-level shrinkage cap analogous to V1's; the exact bound depends on the parent type (outer vs inner lobe).

Level-2 recursion is implemented as a sketch in `scripts/clover_inverse.py` (deferred from initial implementation; see file's docstring for the build_clover_inverse_arcs function which currently builds level 1 only).

---

## 5. Where this fits in the toolkit

Two cross-section variants now exist; both are candidates for the eigenmode-based mass-mechanism work.

### 5.1 Forward solver

[scripts/fractal_eigenmodes.py](../scripts/fractal_eigenmodes.py) currently dispatches to V1 only. A `--variant` flag should be added that selects between `clover` (V1, default) and `clover-inverse` (V2). The grid-based 2D Helmholtz solver is variant-agnostic — it only needs a boundary polygon, which both variants provide. Mode-classification feature groups would change (V2 has outer/inner lobes + connectors instead of lobes/saddles).

### 5.2 Visualization

[viz/proton-lab.html](../../../viz/proton-lab.html) currently visualizes V1 with a fractal-level dropdown (1/2/3) and per-level sliders. To support V2, the UI would add a "variant" dropdown (clover / clover-inverse) and replace the V1 (r_lobe, r_saddle) sliders with V2's (r_outer, r_inner, r_conn) when V2 is selected. Three-radius sliders + the bound display for r_inner. Deferred until V2's role is clearer.

### 5.3 Test/render script

`scripts/clover_inverse.py` renders V2 at level 1 with adjustable radii. Variant-panel mode (`--variants r_outer:r_inner:r_conn,...`) shows the geometry's response to parameter changes.

---

## 6. Open questions

1. **Charge interpretation.** Does the −2/3 inner-lobe correspond to a standard particle, or does it require a non-standard interpretation? (See §3.)
2. **Mass-mechanism test.** Does the V2 cross-section's 2D Helmholtz spectrum show structure that V1's doesn't (e.g., natural separation into 6-flavor bands)? Requires extending `fractal_eigenmodes.py` to dispatch on variant.
3. **Fractal extension.** Does the level-2 recursion (§4 sketch) close cleanly for V2? Analogous to V1, the bounds will exist but their numerical values differ.
4. **Free-parameter advantage.** V2 has 3 base parameters vs V1's 2. Does this extra degree of freedom help reach observed mass ratios that V1 cannot? (V1's failure to reach inter-generation ratios is documented in [fractal_eigenmodes.py](../scripts/fractal_eigenmodes.py)'s output for the canonical clover.)

---

## 7. Cross-references

- [clover-on-clover.md](clover-on-clover.md) — V1 spec.
- [scripts/clover_on_clover.py](../scripts/clover_on_clover.py) — V1 implementation.
- [scripts/clover_inverse.py](../scripts/clover_inverse.py) — V2 implementation (this file's geometry).
- [scripts/fractal_eigenmodes.py](../scripts/fractal_eigenmodes.py) — eigenmode solver (V1 only currently).
- [3-gen.md](3-gen.md) — three-generations open question; V1 found insufficient to reach observed ratios.
