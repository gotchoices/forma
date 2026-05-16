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
| Outer lobe | 3 | convex (sign +1) | θ_lobe | +θ_lobe/360° |
| Inner lobe | 3 | concave (sign −1) | θ_lobe | −θ_lobe/360° |
| Connector | 6 | convex (sign +1) | 60° | +1/6 |

The outer- and inner-lobe extents are **equal in V2 by construction** (otherwise their geodesic-curvature contributions wouldn't cancel and the connectors couldn't carry the full closure budget). Because their contributions to ∫κ ds cancel exactly, the 6 connectors must together sum to the full 360° — i.e. each connector is **60° independent of θ_lobe**:

  ∫κ ds = 3·(+θ_lobe) + 3·(−θ_lobe) + 6·(+60°) = **+360° = 2π** ✓

This leaves θ_lobe ∈ (0°, 360°) as the one free angular parameter. Notable values:

| θ_lobe | Construction reads as |
|---|---|
| ≈ 360° | outer arcs wrap nearly-full circles; geometry becomes singular (lobes nearly-closed loops touching only at connectors). |
| 240° | the **canonical V2** as documented in §1.3 (outer and inner lobes are 240° each; saddle complex = inner + 2 connectors = −240° + 120° = −120° → Q = −1/3, matching V1's saddle). |
| 120° | each inner lobe is a 120° concave arc — geometrically *identical* to a V1 simple saddle. But the 6 × 60° connectors are still present, so the construction is *not* identical to V1: V1 has zero-extent connectors, V2 at θ_lobe = 120° has six. The per-feature charges also change (Q_outer = +1/3, Q_saddle_complex = 0), so this is a distinct geometry with a different charge pattern. |

The canonical V2 in the rest of this file uses θ_lobe = 240°. The angle is fixed there because the saddle-complex charge analysis of §3.1 requires it. Other θ_lobe values give different per-feature charges and would represent different physics. Implementations of θ_lobe ≠ 240° additionally require regenerating the tangency math in §1.2 — the radii constraints change with the angle.

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

### 3.1 The "saddle complex" reading: inner lobe + 2 flanking connectors

The natural V2 grouping is not "each arc one charge" but "each contiguous concave region one charge." A V2 saddle complex consists of one inner-lobe arc flanked by two connectors (one on each side, since 6 connectors pair off between 3 inner-lobes). The complex's net angular sweep:

  Q_saddle_complex = Q_inner + 2 · Q_conn = (−240° + 2 · 60°) / 360° = **−120°/360° = −1/3**

This matches the V1 saddle's charge exactly. Under this grouping the V2 cross-section has three +2/3 outer lobes alternating with three −1/3 saddle complexes — the same charge structure as V1, just with three independently-tuneable radii instead of two.

| Feature | V1 charge | V2 charge (grouped) | Standard model |
|---|---|---|---|
| Outer lobe | +2/3 (V1 lobe) | +2/3 | up-type quark |
| Saddle complex | −1/3 (V1 saddle) | −1/3 (= inner + 2 connectors) | down-type quark |

The +1/6 per-connector charge is not a separate particle assignment; it is a fragment of the saddle complex's −1/3 winding that happens to be visible at the per-arc level. Half-arc decompositions of the V1 saddle have the same property.

### 3.2 Implication for V2's role

V2 is *charge-equivalent* to V1 under the saddle-complex grouping. The extra degree of freedom is geometric (three radii instead of two), not topological. V2 differs from V1 in *what cross-section shapes are admissible*, not in what fractional charges appear.

---

## 4. Optional level-2 fractal recursion (sketch)

A V2 fractal recursion analogous to [clover-on-clover.md](clover-on-clover.md) §3:

- For each outer lobe (parent A = θ_lobe): bisect, remove a central wedge, insert primitive with sub-lobes and sub-saddles matching the V1 recursion algebra. Preserves closure.
- For each inner lobe (parent A = θ_lobe, concave): bisect; insert *inverted* primitive (sub-lobes concave, sub-saddles convex). Net rotation matches removed concave rotation.
- Connectors are not bisected (only lobes are).

Closure constraint for level-2 primitives, parameterized by parent's angular extent A:

  r_p = 2 r_L_new · cos(A/4) + r_S_new · (2 cos(A/4) − 1)

Same form as V1. For A = 240° this gives the same level-1→2 shrinkage cap as V1's outermost level (r_p / r_L_new ≤ 4 cos(60°) − 1 = 1, so the recursion is *degenerate* at A = 240°: no shrinkage possible). For A = 120° (the V1-like saddle case), the cap is r_p / r_L_new ≤ 4 cos(30°) − 1 ≈ 2.46 — same as V1 level-1→2.

### 4.1 Match-to-connector-angle recursion

A more interesting recursion: choose the level-1 sub-arc angles to match the connector angle θ_conn. Under this match, the sub-lobes of an inner-lobe become indistinguishable in angle from the existing connectors, and the recursion adds new features at a *third* radius scale without introducing a new angular feature. The sub-lobe shrinkage cap then becomes r_p / r_L_new ≤ 4 cos(θ_conn / 4) − 1, which for θ_conn = 20° (canonical V2) is large (≈ 2.97) but for θ_conn = 60° (canonical V1) is again ≈ 2.46. This is the most natural site for a "heaviest generation" feature if recursion is to be added at all.

Level-2 recursion is implemented as a sketch in `scripts/clover_inverse.py` (deferred from initial implementation; the `build_clover_inverse_arcs` function currently builds level 1 only).

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

## 7. Eigenmode test results (Phase 4)

After the V1 verdict (see [3-gen.md](3-gen.md) §13), V2 was tested as a candidate to escape V1's closure-constraint cap by providing three radii at level 1 (no fractal recursion required).

**Reader's guide.** This section reports two distinct findings, both negative for the original V2 hypothesis:

- **§7.2–§7.4 (Problem A — structural-identification failure).** The hoped-for "three radii → three cavity-mode bands" picture does not survive numerical test. Even at 10:1 ratios between adjacent feature scales, the cross-section spectrum gives only ~3.5× dynamic range, and all low-lying modes localize on the outer lobes.
- **§7.5 (Problem B — wave-guide tower over-supplies states).** Once ring excitations are turned on, the (n_θ, α) tower contains states at arbitrary mass ratios — including all observed quark ratios — but with no rule for picking which six cells correspond to the six quarks.

Problem A is V2-specific (it asks whether V2's geometric structure encodes a band pattern). Problem B is universal to any wave-guide construction (it asks whether the ring tower can predict a finite spectrum). Either one alone would block the picture from working; both must be addressed.

### 7.1 Setup

The forward solver [scripts/fractal_eigenmodes.py](../scripts/fractal_eigenmodes.py) was extended with a `--variant clover-inverse` dispatch that builds the V2 cross-section via `clover_inverse.build_clover_inverse_arcs(r_outer, r_inner, r_conn)` and feeds the resulting boundary polygon into the existing 2D Helmholtz solver. The hypothesis under test (the original V2 motivation):

> Three independent radii host three distinct mode bands, with cavity-mode mass scaling m ~ 1/r giving mass scales at 1/r_outer, 1/r_inner, 1/r_conn. The three bands correspond to three generations.

### 7.2 Results: moderate ratios

Two parameter sets were tested (both well within the radius bounds):

| Test | r_outer | r_inner | r_conn | r_outer/r_inner | r_inner/r_conn | n_modes | Spectrum range (m) |
|---|---|---|---|---|---|---|---|
| A | 1.0 | 0.30 | 0.10 | 3.33 | 3.00 | 60 | 2.33 – 9.80 |
| B | 1.0 | 0.15 | 0.05 | 6.67 | 3.00 | 40 | 1.94 – 7.95 |

**Predicted bands** (1/r scaling) for test A: m ≈ {1.00, 3.33, 10.0}.
**Actual spectrum**: smooth, continuous, no gaps separating three bands. Ground state at m = 2.33 (not at 1.00 as predicted). Highest computed mode at m ≈ 9.8 — just barely reaches the predicted band-3 frequency but with no visible band gap.

**Predicted bands** for test B: m ≈ {1.00, 6.67, 20.0}.
**Actual spectrum**: still continuous, m = 1.94 to 7.95. The predicted band-3 at m = 20 lies above the lowest 40 modes.

### 7.3 What the spectrum is doing

The cavity modes are governed by the **overall cavity size** (~ r_outer), not by the three feature scales. Specifically:

- The lowest mode's eigenvalue corresponds to the cavity's coarsest "size mode" — analogous to the ground state of a disc of radius ~r_outer.
- Higher modes are excitations on the SAME overall cavity, with progressively shorter wavelengths.
- The smaller features (inner lobes, connectors) are **tangentially connected** to the outer-lobes — there are no barriers to confine modes inside the smaller features. So modes spread across the whole cavity.

This is the same fundamental issue as V1: features need *barriers* (deep saddles, narrow throats with steep curvature transitions) to localize modes. V2's geometry has *thin* features but no barriers. Modes don't localize at the small scales until very high frequency (where wavelength ≲ feature size), which falls above the lowest ~60 modes.

### 7.4 Extreme-tuning test

A second test pushed the radii to extreme ratios (r_outer = 1.0, r_inner = 0.1, r_conn = 0.01, predicted bands at m ≈ 1, 10, 100). Across the lowest 25 cross-section modes:

- Cross-section spectrum spans m ≈ 1.78 → 6.38, a factor of 3.59.
- All 25 modes classify as `lobe_L1` (outer-lobe-localized). None localize at the inner lobes or connectors.
- Predicted bands at m = 10 and m = 100 do **not** appear in this window.

This confirms §7.3: even at 10:1 ratios between adjacent feature scales, the cavity spectrum is dominated by the largest feature (the outer lobe). Smaller features are passively connected to the bulk and do not host separate bands of low-lying modes.

### 7.5 Ring-excitation (wave-guide tower) test

Per [tube-waveguide.md §1](tube-waveguide.md), the full mass spectrum on the 3D wave-guide is μ²(n_θ, α) = ε² · n_θ² + λ_α with ring-direction winding n_θ. The solver was extended with `--epsilon` and `--n-theta-max` flags to build this tower and report the lowest few hundred (n_θ, α) states.

Findings for V2 (canonical and extreme tunings, ε = 1.0, n_θ_max up to 1000):

1. **The tower contains states at any ratio,** including m_s/m_d ≈ 19.89 (hit at n_θ = 35, α = 21 for the extreme tuning), but reaching m_c/m_u ≈ 589 requires n_θ ≳ 1000 and reaching m_t/m_u ≈ 78,000 requires n_θ ≳ 1.3 × 10⁵.
2. **No identification rule.** Whichever six (n_θ, α) cells one picks to be the six quarks, no structural principle distinguishes them from neighbouring cells with similar masses. ε and n_θ are not independent: ε → ε/k, n_θ → k·n_θ produces the same spectrum. The natural quantity ε·n_θ has no ceiling.
3. **Same identification problem as V1.** The wave-guide tower neither helps nor hurts V2 relative to V1; both share the lack of a substrate-level rule for selecting cells.

### 7.6 V2 verdict — two distinct obstructions

V2 fails as a predictive three-generation cross-section. The failure has **two independent components**, and only one is V2-specific:

**Problem A (V2-specific, §7.2–§7.4) — structural identification doesn't hold.** The original hypothesis ("three radii host three bands") is wrong. V2's cross-section spectrum behaves like one big cavity dominated by its largest feature, regardless of how small r_inner and r_conn are made. Compare to V1's analogous obstruction: V1 has a *geometric* cap on inter-generation cross-section ratios (closure constraint pins shrinkage at ≤ 2.5×); V2 has *no* geometric cap, but the wave equation refuses to localize at the small scales. The V2 failure is more fundamental in a sense — V1's cap is at least quantitative ("how much shrinkage you get per level"); V2's failure is qualitative ("the bands you want don't exist").

**Problem B (universal to any wave-guide, §7.5) — ring tower over-supplies states.** Once n_θ excitations are admitted, the (n_θ, α) spectrum contains arbitrary mass ratios. The six observed quark masses are *all present* somewhere in the tower, but no principle picks them out: the tower has too many modes, not too few. This problem applies identically to V1 and V2; choosing a different cross-section doesn't help.

The two problems are independent in the sense that solving one without solving the other still leaves the picture broken:

- If Problem A is solved (some V2 variant produces three clean cavity bands) but Problem B is not, the bands exist but ring excitations dilute them into an undifferentiated mass continuum.
- If Problem B is solved (a substrate-level rule pins n_θ as a function of α) but Problem A is not, the selection rule has nothing meaningful to select among in the V2 cross-section spectrum.

Either route requires substantive additional work; the current V2 specification addresses neither.

### 7.7 What this leaves open for V2

Routes that would address Problem A (cross-section identification):

1. **Barrier-amplified modes.** Deepening the indentation between adjacent outer-lobes (making the inner-lobe "tunnel-barrier-like") would let modes localize at smaller scales with exponentially-amplified frequency gaps. This requires extending V2 with an amplitude/depth parameter beyond the current radii, and a corresponding update to the closure analysis.

2. **Lobe-angle generalization.** The variable θ_lobe (see §1.1) lets V2 interpolate between the canonical 240° geometry and other angles. Whether the connectors at intermediate θ_lobe contribute separate localization sites in the cross-section spectrum has not been tested. (Likely no, since the underlying obstruction is "no barriers", not "wrong angle" — but worth checking.)

3. **Match-to-connector-angle recursion.** The recursion sketched in §4.1 (sub-lobe angle = connector angle = 60°) is the natural site for adding a third scale to V2 without introducing a new angular feature. Same caveat: adds a scale, not a barrier; likely won't fix Problem A on its own.

Route that would address Problem B (ring-tower over-supply):

4. **A selection rule on (n_θ, α).** Any substrate-level rule pinning n_θ as a function of α — Z₃-allowed cells, a winding-charge constraint, a coupling-to-substrate condition — would convert the tower from "everything in there somewhere" into a finite prediction. This is independent of which cross-section is chosen, and would help V1 equally.

### 7.8 Cross-link to V1 verdict

The combined V1+V2 verdict (including the wave-guide tower analysis) and its implications are documented in [3-gen.md](3-gen.md) §13.5–§13.8.

---

## 8. Cross-references

- [clover-on-clover.md](clover-on-clover.md) — V1 spec.
- [scripts/clover_on_clover.py](../scripts/clover_on_clover.py) — V1 implementation.
- [scripts/clover_inverse.py](../scripts/clover_inverse.py) — V2 implementation (this file's geometry).
- [scripts/fractal_eigenmodes.py](../scripts/fractal_eigenmodes.py) — eigenmode solver (V1 only currently).
- [3-gen.md](3-gen.md) — three-generations open question; V1 found insufficient to reach observed ratios.
