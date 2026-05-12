# work-discipline.md — Parametrization conventions and the derived-metric strategic stance

**Purpose.** Establish the discipline metric-charge needs in order to feed cleanly into [metric-binding](../metric-binding/) and downstream work. The math of shear and ratio is settled (cf. [Ch 1 §3, §4](01-foundation.md), [Ch 7](07-aspect-ratio-and-character.md), [Ch 8](08-shear-and-fractional-charge.md), [work-m8a.md](work-m8a.md)). What's missing is the **naming and framing** that makes the framework's parameters identifiable and translatable across conventions.

This file:

- Names the parametrization classes (metric-shear vs lattice-shear; periodicity-form ε vs metric-form ε).
- Documents the transforms between them.
- States the strategic stance: the metric is the framework's primary structural object, with parameter values that should eventually be *derived* from particle properties rather than imposed empirically.
- Addresses the diagonal-normalization choice as a choice.
- Forward-points lightly to multi-particle composition (deferred to metric-binding).

This file is preparatory. The mathematics it relies on is established; the work is conventional clarity, not new derivation. Once settled, a chapter refactor pass propagates the naming and framing into Ch 1, Ch 7, Ch 8, and the README.

---

## Sections

| § | Topic |
|---|---|
| 1 | The strategic stance — what "derived metric" means |
| 2 | The full parameter inventory for a single sheet |
| 3 | Metric-shear σ_m vs lattice-shear σ_L |
| 4 | Periodicity-form ε_p vs metric-form ε_g |
| 5 | The diagonal normalization choice |
| 6 | Light forward-pointer to multi-particle composition |
| 7 | What the eventual chapter refactor would say |

---

## 1. The strategic stance — what "derived metric" means

The metric is the framework's primary structural object. For each closure-satisfying particle species, the framework should ultimately provide:

- Diagonal entries (g_uu, g_ww) — the relative sizes of the compact directions in the chosen coordinate system.
- Off-diagonal entry (g_uw) — the shear that biases chirality and shapes the gauge-potential structure of [Ch 5](05-metric-self-consistency.md).
- Periodicities (L_u, L_w) — the manifold-topology data.

These quantities, taken together, specify the sheet. Each particle species corresponds to specific values of these parameters; the framework's eventual job is to derive those values from structural properties (mass, charge, generation, chirality bias) rather than fit them empirically.

The current chapters introduce ε and σ_uw as **inputs** ("we adopt this convention," "we introduce one optional off-diagonal entry"). For metric-charge in isolation, treating them as inputs is fine — the project's job is to characterize what charge looks like given a sheet, not to derive the sheet's parameter values. But for the framework's strategic arc (single-particle metric-charge → multi-particle metric-binding → species-specific MaSt-correspondence), the parameters must be:

- **Clearly named** so a downstream chapter knows which quantity it is plugging in.
- **Transformable across equivalent parametrizations** so values reported in one convention (e.g., the R-track studies' lattice-shear form) can be plugged into another (the framework's metric-shear form).
- **Marked as intrinsic vs labeling** so derivation work can target the intrinsic quantities without getting stuck on coordinate choices.

This document provides that scaffolding. metric-charge stays focused on charge generation in the general case; what's added is the discipline that makes the framework's parameter language survive the transition to multi-species derivation work.

---

## 2. The full parameter inventory for a single sheet

A 2D flat compact sheet is specified by:

| Quantity | Default form | Role |
|---|---|---|
| L_u | Length of u-cycle | Sets one compact length scale |
| L_w | Length of w-cycle | Sets the other compact length scale |
| g_uu | Metric (u, u) entry | Diagonal scaling of u |
| g_ww | Metric (w, w) entry | Diagonal scaling of w |
| g_uw | Metric (u, w) entry | Off-diagonal shear |

In the chapters' current default form: g_uu = g_ww = 1; the lengths L_u, L_w carry dimension; g_uw is the shear σ.

Up to an overall scale, a 2D flat torus has **two intrinsic degrees of freedom**:

- **Aspect ratio** — a measure of the relative sizes of the two compact directions.
- **Shear** — a measure of how non-orthogonal the (u, w) basis is.

The two intrinsic quantities can be expressed in several parametrization classes. The choice of class is a labeling choice; the underlying torus geometry is the same. §§3–4 below name the parametrization classes the framework uses and the transforms between them.

---

## 3. Metric-shear σ_m vs lattice-shear σ_L

Two parametrization classes for shear. Both describe the same underlying torus; they differ in whether the shear lives in the metric or in the lattice periodicity.

### 3.1 Metric-shear σ_m

The framework's default. Coordinates have rectangular periodicity (u ~ u + L_u, w ~ w + L_w). The metric (u, w) sub-block is:

<!-- g_uw block = ((1, σ_m), (σ_m, 1)) -->
$$
g^{(u, w)}_{ab} \;=\; \begin{pmatrix} 1 & \sigma_m \\ \sigma_m & 1 \end{pmatrix}
$$

- **Bound:** |σ_m| < 1 (positive-definiteness of the (u, w) sub-block).
- **Dispersion:** for a mode at (m, n),

<!-- μ²_m = (1/(1−σ_m²)) (m²/ε² − 2σ_m·mn/ε + n²) -->
$$
\mu^2_m(m, n;\,\sigma_m, \varepsilon) \;=\; \frac{1}{1 - \sigma_m^2}\Bigl[\tfrac{m^2}{\varepsilon^2} - \tfrac{2\sigma_m\,m n}{\varepsilon} + n^2\Bigr]
$$

- **Picture:** "tilted yardstick" — local, in the metric. The (u, w) basis is non-orthogonal because the metric components make it so.

This is what [Ch 1 §4](01-foundation.md) and [Ch 8](08-shear-and-fractional-charge.md) work with. The chapter rewrite will rename the off-diagonal entry from the bare "σ" or "σ_uw" of the current chapters to **σ_m** so the parametrization class is explicit at every reference.

### 3.2 Lattice-shear σ_L

Coordinates have flat (Euclidean) metric and sheared periodicity:

<!-- e_1 = (L_u, 0), e_2 = (σ_L · L_u, L_w^B) -->
$$
e_1 \;=\; (L_u, 0),\qquad e_2 \;=\; (\sigma_L\,L_u,\; L_w^B)
$$

- **Bound:** none. σ_L is a slope, unbounded.
- **Dispersion:** for a mode at (n_t, n_r) in this basis,

<!-- μ²_L = (n_t/ε_B)² + (n_r − σ_L · n_t)² -->
$$
\mu^2_L(n_t, n_r;\,\sigma_L, \varepsilon_B) \;=\; (n_t/\varepsilon_B)^2 + (n_r - \sigma_L\,n_t)^2
$$

- **Picture:** "lattice basis skew" — global, in the periodicity. The (u, w) basis is non-orthogonal because the lattice basis vectors are skewed; the metric is plain Euclidean.

This is the form used by the production R-track studies (R60, R63, R64). What those studies call "s" is **σ_L** in this convention.

### 3.3 The transform

For the same underlying torus expressed in both classes:

<!-- σ_L = σ_m/ε,  L_w^B = √(1 − σ_m²) · L_w,  ε_B = ε / √(1 − σ_m²) -->
$$
\sigma_L \;=\; \frac{\sigma_m}{\varepsilon},\qquad
L_w^B \;=\; \sqrt{1 - \sigma_m^2}\;L_w,\qquad
\varepsilon_B \;=\; \frac{\varepsilon}{\sqrt{1 - \sigma_m^2}}
$$

(Derivation: apply the coordinate change (u', w') = (u + σ_m·w, √(1 − σ_m²)·w) to View A's metric; the result is flat Euclidean with the lattice basis above.)

The transform is **exact, invertible, and parametrization-only**. No physical information is lost or gained crossing between σ_m and σ_L. The two values labeling the same torus are different numbers but encode the same intrinsic geometry.

### 3.4 Apparent paradox: |σ_m| < 1 vs |σ_L| unbounded

The metric-shear bound |σ_m| < 1 is real (positive-definiteness of the (u, w) metric sub-block). The lattice-shear σ_L has no analogous bound because the metric in lattice-shear coordinates is flat — automatically positive-definite.

These are consistent: σ_L → ∞ at fixed L_u corresponds to L_w^B → 0 in the lattice-shear basis (the second basis vector flattens onto the first). This is the *same degenerate-torus limit* that σ_m → 1 approaches in the metric-shear basis. Different labels for the same wall.

For empirical correspondence: studies that report σ_L on order unity at ε on order hundreds (e.g., σ_L ≈ 2, ε ≈ 397) correspond to σ_m very close to 1 (within ~10⁻⁶). The lattice-shear basis is computationally convenient for sheets near the degenerate-torus limit; the metric-shear basis is computationally convenient for sheets away from it. Both are valid; neither is more "fundamental."

### 3.5 Which is primary?

The framework's primary parametrization is **metric-shear σ_m**, because:

- The off-diagonal entry σ_m is already where [Ch 5 §4](05-metric-self-consistency.md) finds the surviving gauge potential. The shear lives in the same object (the metric) that produces all the framework's other structural results.
- The bound |σ_m| < 1 is a real geometric constraint (positive-definiteness), and naming it directly keeps the constraint visible.
- The dispersion form makes the (1 − σ_m²)⁻¹ rescaling factor explicit, which matters for the σ_m → 1 principal-axis suppression analysis ([work-m8a.md §7.3](work-m8a.md)).

σ_L is a **secondary, derived label** for use when comparing to studies or when computing near the degenerate-torus limit. The framework's derivations are stated in σ_m; σ_L appears as a convenience translation.

---

## 4. Periodicity-form ε_p vs metric-form ε_g

The aspect ratio ε can also be placed in two distinct positions in the parametrization. Like σ_m vs σ_L, the difference is *where* the same number lives, not what value it takes.

### 4.1 Periodicity-form ε_p

The current framework convention. Periodicities are dimensional (u ~ u + L_u, w ~ w + L_w); the metric diagonals are unit.

- **ε_p ≡ L_u / L_w** — a ratio of the periodicities.
- Lives in the manifold-topology data, not the metric.

This is what [Ch 1 §3](01-foundation.md) defines and what [Ch 7](07-aspect-ratio-and-character.md) sweeps over.

### 4.2 Metric-form ε_g

Alternative parametrization with unit periodicities and ε in the metric diagonal. Rescale to u' = u/L_u, w' = w/L_w (both unit-period). The metric becomes:

<!-- g̃ = ((ε², σ_m·ε), (σ_m·ε, 1)) -->
$$
\tilde g \;=\; \begin{pmatrix} \varepsilon_g^2 & \sigma_m\,\varepsilon_g \\ \sigma_m\,\varepsilon_g & 1 \end{pmatrix}
$$

- **ε_g** appears as the relative scale of the diagonal entries: g_uu / g_ww = ε_g².
- σ_m·ε_g (= σ_L) appears as the off-diagonal entry.
- Periodicities are now both unit (no structure in the boundary conditions).

Everything is in the metric.

### 4.3 The transform

ε_g and ε_p are numerically equal under the natural rescaling:

<!-- ε_g = ε_p = L_u / L_w -->
$$
\varepsilon_g \;=\; \varepsilon_p \;=\; L_u / L_w
$$

The naming distinguishes *where* the ratio lives, not *what value* it takes. The same number is called ε_p when it's in the periodicities and ε_g when it's in the metric.

### 4.4 Which is primary?

The framework's primary form is **periodicity-form ε_p**, because:

- The current chapters work in this form throughout.
- Dimensional coordinates (with L_u, L_w as the absolute length scales) match physical intuition more directly.

But the metric-form ε_g matters for the strategic stance of §1. The metric-form rescaled view

<!-- g̃ = ((ε², σ_m·ε), (σ_m·ε, 1)) -->
$$
\tilde g \;=\; \begin{pmatrix} \varepsilon^2 & \sigma_m \varepsilon \\ \sigma_m \varepsilon & 1 \end{pmatrix}
$$

makes manifest that **two structural quantities** (ε, σ_m) together specify a sheet, and **both can be read off the metric matrix** — no auxiliary periodicity data required. For metric-binding's "derived metric" workflow, this is the form in which the framework's parameter values would be reported (as components of a metric matrix that downstream chapters can plug into geodesic equations, gauge-potential analyses, etc.).

The chapter rewrite should keep ε_p as the working convention but note ε_g where it clarifies the structural picture.

---

## 5. The diagonal normalization choice

The current framework uses g_uu = g_ww = 1 in periodicity-form coordinates. This is a **convention**, not a forced choice.

### 5.1 Unit diagonals (current convention)

g_uu = g_ww = 1. Length scales live in the periodicities (L_u, L_w). Aspect ratio is ε_p = L_u/L_w in the periodicities.

Studies' R-track (R60, R63, R64) inherits this convention.

**Advantage:** dimensional coordinates match physical intuition.

**Disadvantage:** the diagonals carry no information about the sheet's character. All structural distinction lives in the off-diagonal and the periodicities.

### 5.2 Metric-form diagonals (ε in the diagonal)

g_uu = ε², g_ww = 1, with unit periodicities. Aspect ratio is ε_g = √(g_uu/g_ww). Equivalent to §4.2.

**Advantage:** all structural information lives in the metric matrix. The strategic goal of "express the sheet entirely in metric terms" is naturally realized.

**Disadvantage:** coordinates are dimensionless; physical lengths require an overall scale factor.

### 5.3 What to make explicit

[Ch 1 §2](01-foundation.md) writes the bare metric with g_uu = g_ww = 1 and treats this as the starting form. The convention works. But it is a choice — and the chapter should say so.

Suggested language for the chapter rewrite:

> *The diagonals are written here as g_uu = g_ww = 1 with the aspect ratio ε in the periodicities (periodicity-form ε_p). An equivalent parametrization moves ε into the diagonal (g_uu = ε², g_ww = 1) and uses unit periodicities (metric-form ε_g). Both describe the same sheet; the choice is conventional. We adopt the periodicity-form throughout this project for working coordinates and use metric-form when the rescaled metric matrix is the cleaner object to display.*

This single paragraph makes the choice explicit and prepares the framework to handle the alternative form when downstream work finds it convenient.

---

## 6. Light forward-pointer to multi-particle composition

When metric-binding considers two or more closure-satisfying species inhabiting the same setting, each species has its own (ε, σ_m) pair. Three architectural questions will arise:

- **Substrate sharing.** One 2D compact bundle hosting multiple sheets, or separate compact bundles for each species?
- **Diagonal normalization across species.** Each species writes g_uu = g_ww = 1 in periodicity form, but the *common metric* the species inhabit may force species-specific diagonal scaling instead.
- **Shear composition.** Each species has its own σ_m. In a multi-species setting, do shears stay species-specific, average, or compose by some rule that depends on the species' relative orientations?

These are **metric-binding questions**. metric-charge does not need to resolve them, and this project's focus on charge generation in the general case is the right scope. The naming discipline of §§3–4 above is the metric-charge-side prerequisite: with σ_m, σ_L, ε_p, ε_g named as distinct parametrization labels with explicit transforms, metric-binding inherits a clean foundation and can make its own architectural commitments without backfilling conventions metric-charge silently assumed.

This is the entire forward-pointer. Specific multi-particle work belongs in metric-binding.

---

## 7. What the eventual chapter refactor would say

Once this document settles, a refactor pass would propagate the naming and framing as follows.

### 7.1 Ch 1 §3 (aspect ratio)

Add a paragraph distinguishing ε_p (periodicity form) from ε_g (metric form), noting they are numerically equal but live in different positions in the parametrization. State that the framework adopts ε_p throughout but uses ε_g where structural compactness matters (notably in the rescaled metric matrix of §4.2).

### 7.2 Ch 1 §4 (shear)

Rename the off-diagonal entry from σ_uw / "σ" to **σ_m** (metric-shear). Introduce **σ_L** (lattice-shear) as the equivalent parameter under the transform σ_L = σ_m / ε. State that the framework's primary parametrization is σ_m and that σ_L will appear when comparing to study-track parameter values.

Add one paragraph stating the |σ_m| < 1 bound explicitly and noting it corresponds in σ_L to a degenerate-torus limit reached as L_w^B → 0 — same geometric wall, different labels.

### 7.3 Ch 1 §11 (non-assumptions)

Add to the non-assumptions list:

> *Multi-sheet composition. This project treats one compact sheet at a time. How two or more sheets share an extended-spacetime metric — whether they inhabit a common compact bundle or separate ones, whether their diagonal normalizations match, how their shears compose — is forwarded to [metric-binding](../metric-binding/).*

> *Diagonal normalization. The metric is written with g_uu = g_ww = 1 in periodicity-form coordinates. An equivalent parametrization with ε in the diagonal exists. The choice between them does not affect single-particle predictions and is left to downstream work to commit on for multi-species settings.*

### 7.4 Ch 1 §12 (summary)

Add a "parametrization classes" line to the summary of givens. Explicit mention of the two shear-parametrization classes (σ_m, σ_L) and two aspect-ratio classes (ε_p, ε_g), with the framework's primary form noted.

### 7.5 README

Add a paragraph to "Ground rules" or a new "Strategic stance" subsection:

> *The metric is the framework's primary structural object. For each closure-satisfying particle species, the framework should ultimately provide a metric prescription (specific values of the diagonals, ε, σ_m) derived from the species' structural properties. This project sets up the single-particle case and characterizes what charge looks like given a sheet; deriving the parameter values from species identity is downstream work, in metric-binding and beyond.*

### 7.6 Ch 7, Ch 8 light pass

Use the renamed parameters consistently. Where a result is computed in σ_m form but might be reported in σ_L form by the studies, add the σ_L equivalent in parentheses or footnote. The [work-m8a.md §9.3](work-m8a.md) discussion of metric-shear vs lattice-shear can be tightened around the σ_m/σ_L naming and the proper transform (including the L_w^B = √(1−σ_m²)·L_w correction that work-m8a.md §9.3 originally missed).

### 7.7 STATUS

Add new todos:

- **TODO-Disc1**: Multi-sheet substrate-sharing question — resolved in metric-binding's framing.
- **TODO-Disc2**: Multi-species diagonal-normalization choice — resolved in metric-binding's framing.
- **TODO-Disc3**: Chapter refactor per §§7.1–7.6 above.

Disc3 is smaller than TODO-M2, M8(a), L5, N2 and can be done in a single editing session.

---

## 8. What this document does not do

- Does not derive any new physical results. The math of shear and ratio is fully in [Ch 1](01-foundation.md), [Ch 7](07-aspect-ratio-and-character.md), [Ch 8](08-shear-and-fractional-charge.md), [work-m8a.md](work-m8a.md). This document is discipline.
- Does not commit to multi-sheet architectural choices. Forward-pointed only.
- Does not derive the metric values for any specific particle. That is the strategic goal; this document sets up the language for the eventual derivation.
- Does not resolve the diagonal-normalization choice. Names it as a choice, flags downstream implications, and leaves the resolution to metric-binding.
- Does not propose modifying the bare framework's mathematical content. Only naming, framing, and forward-pointing.

---

## Notes

This document is preparatory. The mathematics it relies on is established. The work is conventional clarity, not new derivation. Once approved, the chapter refactor (§7) can be executed cleanly in a single pass.

The motivation throughout is the strategic stance of §1: the framework should be set up such that facts about known particles can eventually be plugged into equations that live in the metric, with the chain from particle properties to metric values made explicit. The naming discipline is the prerequisite for that workflow to be runnable. metric-charge's job, in this regard, is to ensure that downstream work (metric-binding, MaSt-correspondence) inherits a clean language rather than a tangle of hidden conventions.
