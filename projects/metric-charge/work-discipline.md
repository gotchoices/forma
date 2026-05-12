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
| 3 | Shear — bare σ in the metric, s in the lattice form |
| 4 | Aspect ratio ε — one symbol, two homes |
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

## 3. Shear — bare σ in the metric, s in the lattice form

The framework's working symbol for shear is **bare σ** — the off-diagonal entry of the (u, w) sub-block of the metric. The R-track studies use **s** for the lattice-shear coefficient (per [shear-ratio.md](shear-ratio.md)'s dispersion formula μ² = (n_t/ε)² + (n_r − s·n_t)²). The two are different numbers, related by s = σ/ε.

This section names both forms, gives the transform, and warns about the second-order divergence that makes the names not interchangeable.

### 3.1 Metric-shear σ — the framework's working form

Coordinates have rectangular periodicity (u ~ u + L_u, w ~ w + L_w). The metric (u, w) sub-block is:

<!-- g_uw block = ((1, σ), (σ, 1)) -->
$$
g^{(u, w)}_{ab} \;=\; \begin{pmatrix} 1 & \sigma \\ \sigma & 1 \end{pmatrix}
$$

- **Bound:** |σ| < 1 (positive-definiteness of the (u, w) sub-block).
- **Dispersion:** for a mode at (m, n),

<!-- μ² = (1/(1−σ²)) (m²/ε² − 2σ·mn/ε + n²) -->
$$
\mu^2(m, n;\,\sigma, \varepsilon) \;=\; \frac{1}{1 - \sigma^2}\Bigl[\tfrac{m^2}{\varepsilon^2} - \tfrac{2\sigma\,m n}{\varepsilon} + n^2\Bigr]
$$

- **Picture:** "tilted yardstick" — local, in the metric. The (u, w) basis is non-orthogonal because the metric components make it so.

This is exactly what [Ch 1 §4](01-foundation.md) and [Ch 8](08-shear-and-fractional-charge.md) work with — no rename needed. Where chapters write σ_uw, that is the explicit form; where they write σ, that is the shorthand. Both refer to the same quantity, and either is acceptable.

**Forward-compatibility for multiple shears.** Within metric-charge (which has only the (u, w) shear) bare σ is unambiguous and we use it freely. If downstream work introduces additional shears (e.g., σ_Su for shear between extended and compact directions, per [metric-mass Ch 7](../metric-mass/07-shear-and-bias.md), which uses γ for that g_Su shear), direction subscripts (σ_uw, σ_Su, σ_Sw, ...) disambiguate. Within metric-charge's single-shear scope, bare σ ≡ σ_uw.

For multi-particle work in metric-binding, species subscripts (σ_e, σ_p, σ_ν, ...) name which sheet's shear is being referenced. These species subscripts compose with direction subscripts as needed (σ_e,uw if explicit), but in practice σ_e alone is unambiguous within metric-binding's (u, w)-only-shear scope.

### 3.2 Lattice-shear s — the studies' form

The R-track studies (R60, R63, R64) work in coordinates with flat (Euclidean) metric and sheared periodicity. Basis vectors:

<!-- e_1 = (L_u, 0), e_2 = (s · L_u, L_w^B) -->
$$
e_1 \;=\; (L_u, 0),\qquad e_2 \;=\; (s\,L_u,\; L_w^B)
$$

- **Bound:** none. s is a slope, unbounded.
- **Dispersion:** for a mode at (n_t, n_r) in this basis,

<!-- μ² = (n_t/ε_B)² + (n_r − s · n_t)² -->
$$
\mu^2(n_t, n_r;\,s, \varepsilon_B) \;=\; (n_t/\varepsilon_B)^2 + (n_r - s\,n_t)^2
$$

- **Picture:** "lattice basis skew" — global, in the periodicity. The (u, w) basis is non-orthogonal because the lattice basis vectors are skewed; the metric is plain Euclidean.

The studies use s as their shear parameter throughout. metric-charge adopts the same symbol when the lattice-form is being referenced.

### 3.3 The transform

For the same underlying torus expressed in both forms:

<!-- s = σ/ε,  L_w^B = √(1 − σ²) · L_w,  ε_B = ε / √(1 − σ²) -->
$$
s \;=\; \frac{\sigma}{\varepsilon},\qquad
L_w^B \;=\; \sqrt{1 - \sigma^2}\;L_w,\qquad
\varepsilon_B \;=\; \frac{\varepsilon}{\sqrt{1 - \sigma^2}}
$$

(Derivation: apply the coordinate change (u', w') = (u + σ·w, √(1 − σ²)·w) to the metric-shear form's metric; the result is flat Euclidean with the lattice basis above.)

The transform is **exact, invertible, and parametrization-only**. No physical information is lost or gained crossing between σ and s. The two values labeling the same torus are different numbers but encode the same intrinsic geometry.

### 3.4 Different numbers — why this matters

σ and s diverge non-trivially at second order in shear. Expanding the metric-shear physical mass formula in σ² and matching the linear cross-term gives s = σ/ε, but at order σ² the metric-form has an extra σ²·n² contribution that doesn't translate cleanly into the lattice-form's s²·m² term. A reader who reads "σ" in the chapters but plugs in a value reported as "s" in a study gets the wrong numbers.

So σ and s are not interchangeable labels for the same quantity. They're labels for two different quantities related by a non-trivial transform. The framework uses different letters (not subscripts) to make this distinction visually unmistakable.

### 3.5 Apparent paradox: |σ| < 1 vs |s| unbounded

The metric-shear bound |σ| < 1 is real (positive-definiteness of the (u, w) metric sub-block). The lattice-shear s has no analogous bound because the metric in lattice-shear coordinates is flat — automatically positive-definite.

These are consistent: s → ∞ at fixed L_u corresponds to L_w^B → 0 in the lattice-shear basis (the second basis vector flattens onto the first). This is the *same degenerate-torus limit* that σ → 1 approaches in the metric-shear basis. Different labels for the same wall.

For empirical correspondence: studies that report s on order unity at ε on order hundreds (e.g., s ≈ 2, ε ≈ 397) correspond to σ very close to 1 (within ~10⁻⁶). The lattice-shear basis is computationally convenient for sheets near the degenerate-torus limit; the metric-shear basis is computationally convenient for sheets away from it. Both are valid; neither is more "fundamental."

### 3.6 Which is primary?

The framework's primary parametrization is **metric-shear σ**, because:

- σ is already where [Ch 5 §4](05-metric-self-consistency.md) finds the surviving gauge potential. The shear lives in the same object (the metric) that produces all the framework's other structural results.
- The bound |σ| < 1 is a real geometric constraint (positive-definiteness), and naming it directly keeps the constraint visible.
- The dispersion form makes the (1 − σ²)⁻¹ rescaling factor explicit, which matters for the σ → 1 principal-axis suppression analysis ([work-m8a.md §7.3](work-m8a.md)).

s is a **secondary, derived label** for use when comparing to studies or when computing near the degenerate-torus limit. The framework's derivations are stated in σ; s appears as a convenience translation, primarily in passages that explicitly reference the R-track studies or the lattice-form display.

---

## 4. Aspect ratio ε

The aspect ratio is one number with two possible homes — sitting in the periodicities (default working form) or sitting in the metric diagonal (when the rescaled metric matrix is being displayed). Because the value is the same in both homes, no separate symbol is needed; **bare ε is used everywhere**.

### 4.1 Definition and default home

**ε ≡ L_u / L_w**. In the framework's working convention (dimensional periodicities u ~ u + L_u, w ~ w + L_w; metric diagonals unit), ε lives in the manifold-topology data, not the metric. This is what [Ch 1 §3](01-foundation.md) defines and what [Ch 7](07-aspect-ratio-and-character.md) sweeps over.

### 4.2 The metric-form display

When the metric is displayed in unit-period coordinates (rescaled u' = u/L_u, w' = w/L_w), the same number ε appears as the relative scale of the diagonal entries:

<!-- g̃ = ((ε², σ·ε), (σ·ε, 1)) = ((ε², s), (s, 1)) -->
$$
\tilde g \;=\; \begin{pmatrix} \varepsilon^2 & \sigma\,\varepsilon \\ \sigma\,\varepsilon & 1 \end{pmatrix}
\;=\; \begin{pmatrix} \varepsilon^2 & s \\ s & 1 \end{pmatrix}
$$

where σ is the metric-shear (§3) and s = σ/ε is the lattice-shear coefficient. In this display, ε sits in the (u, u) diagonal and the off-diagonal is exactly the studies' s — the metric makes the two structural quantities (ε, σ) directly readable, with s appearing naturally as the product σ·ε.

The same symbol ε is used in either home: bare in working contexts; bare in displays like the matrix above. There is no separate symbol for "ε in the metric." The matrix's structure tells the reader which home is being shown; the symbol does not need to.

### 4.3 Strategic value of the metric-form display

The metric-form display matters for the strategic stance of §1: it is the form in which **all structural information about the sheet sits inside the metric matrix** — diagonals carry the aspect ratio, off-diagonal carries the shear. For metric-binding's "derived metric" workflow, this is the form in which the framework's parameter values would be reported (as components of a metric matrix that downstream chapters can plug into geodesic equations, gauge-potential analyses, etc.).

The working convention with dimensional periodicities (§4.1) and the metric-form display (§4.2) are two ways of writing the same thing. The chapters work in the former; the latter appears where the metric matrix is the cleaner object to show.

---

## 5. The diagonal normalization choice

The current framework uses g_uu = g_ww = 1 in periodicity-form coordinates. This is a **convention**, not a forced choice.

### 5.1 Unit diagonals (current convention)

g_uu = g_ww = 1. Length scales live in the periodicities (L_u, L_w). Aspect ratio is bare ε = L_u/L_w in the periodicities.

Studies' R-track (R60, R63, R64) inherits this convention.

**Advantage:** dimensional coordinates match physical intuition.

**Disadvantage:** the diagonals carry no information about the sheet's character. All structural distinction lives in the off-diagonal and the periodicities.

### 5.2 Metric-form diagonals (ε in the diagonal)

g_uu = ε², g_ww = 1, with unit periodicities. Aspect ratio is read off the metric as ε = √(g_uu/g_ww). Equivalent to §4.2's metric-form display.

**Advantage:** all structural information lives in the metric matrix. The strategic goal of "express the sheet entirely in metric terms" is naturally realized.

**Disadvantage:** coordinates are dimensionless; physical lengths require an overall scale factor.

### 5.3 What to make explicit

[Ch 1 §2](01-foundation.md) writes the bare metric with g_uu = g_ww = 1 and treats this as the starting form. The convention works. But it is a choice — and the chapter should say so.

Suggested language for the chapter rewrite:

> *The diagonals are written here as g_uu = g_ww = 1 with the aspect ratio ε in the periodicities. An equivalent parametrization moves ε into the diagonal (g_uu = ε², g_ww = 1) and uses unit periodicities. Both describe the same sheet — the same ε in two homes; the choice is conventional. We adopt the periodicity-form throughout this project for working coordinates and use the metric-form display only when the rescaled metric matrix is the cleaner object to show.*

This single paragraph makes the choice explicit and prepares the framework to handle the alternative form when downstream work finds it convenient.

---

## 6. Light forward-pointer to multi-particle composition

When metric-binding considers two or more closure-satisfying species inhabiting the same setting, each species has its own (ε, σ) pair (with species-subscript labels σ_e, σ_p, σ_ν, ... naming which sheet). Three architectural questions will arise:

- **Substrate sharing.** One 2D compact bundle hosting multiple sheets, or separate compact bundles for each species?
- **Diagonal normalization across species.** Each species writes g_uu = g_ww = 1 in periodicity form, but the *common metric* the species inhabit may force species-specific diagonal scaling instead.
- **Shear composition.** Each species has its own σ. In a multi-species setting, do shears stay species-specific, average, or compose by some rule that depends on the species' relative orientations?

These are **metric-binding questions**. metric-charge does not need to resolve them, and this project's focus on charge generation in the general case is the right scope. The naming discipline of §§3–4 above is the metric-charge-side prerequisite: bare σ as the working metric-shear symbol, s as the lattice-shear name (matching R-track studies), bare ε as the aspect-ratio symbol in both periodicity- and metric-form contexts. With these names settled, metric-binding inherits a clean foundation and can make its own architectural commitments — including species subscripts (σ_e, σ_p, σ_ν, ...) for shear and ε per sheet — without backfilling conventions metric-charge silently assumed.

This is the entire forward-pointer. Specific multi-particle work belongs in metric-binding.

---

## 7. What the eventual chapter refactor would say

Once this document settles, a refactor pass would propagate the naming and framing as follows.

### 7.1 Ch 1 §3 (aspect ratio)

Add a short paragraph noting that ε has two homes — sitting in the periodicities (the framework's default working convention) and appearing in the metric diagonal when the rescaled metric matrix is displayed. The value is the same in both homes, so bare ε is used throughout; no separate symbol is needed.

No rename of existing ε references is required anywhere in the chapters or across the project tree.

### 7.2 Ch 1 §4 (shear)

No rename. The chapter's existing σ_uw / "σ" stays as the working symbol. Add a short paragraph introducing **s** as the lattice-shear coefficient (matching R-track studies' usage), with the transform s = σ/ε. State that σ and s are *different numbers* — same physical sheet, but the two forms diverge non-trivially at second order in shear — and that the framework's derivations use σ throughout while s appears for empirical correspondence with studies.

Add one paragraph stating the |σ| < 1 bound explicitly (positive-definiteness of the (u, w) sub-block) and noting it corresponds in lattice-shear to a degenerate-torus limit reached as L_w^B → 0 — same geometric wall, different labels.

### 7.3 Ch 1 §11 (non-assumptions)

Add to the non-assumptions list:

> *Multi-sheet composition. This project treats one compact sheet at a time. How two or more sheets share an extended-spacetime metric — whether they inhabit a common compact bundle or separate ones, whether their diagonal normalizations match, how their shears compose — is forwarded to [metric-binding](../metric-binding/).*

> *Diagonal normalization. The metric is written with g_uu = g_ww = 1 in periodicity-form coordinates. An equivalent parametrization with ε in the diagonal exists. The choice between them does not affect single-particle predictions and is left to downstream work to commit on for multi-species settings.*

### 7.4 Ch 1 §12 (summary)

Add a "parametrization classes" line to the summary of givens. Explicit mention of the two shear forms (bare σ for metric-shear in the working convention; s for lattice-shear in R-track-study correspondence; different numbers, transform s = σ/ε) and the aspect-ratio convention (bare ε used in both periodicity- and metric-form contexts, as the value is the same in both). State that no symbol renames are required anywhere in the chapters.

### 7.5 Ch 1 — single "Notation" block

Add a short Notation paragraph near the top of [Ch 1](01-foundation.md) (e.g., as §1.5 or as part of §2's setup), stating the conventions in one place so all subsequent references are unambiguous:

> *Notation. Aspect ratio is written ε ≡ L_u/L_w. The same symbol is used in both the framework's working convention (where ε lives in the periodicities and the metric diagonals are unit) and in the rescaled metric-form display (where ε sits in the (u, u) diagonal entry of the rescaled metric matrix). The value is identical; the home is identified by the surrounding equation, not by a subscript. Shear has two forms with distinct labels: **σ** is metric-shear (the off-diagonal entry of the (u, w) sub-block, with |σ| < 1), and **s** is lattice-shear (used by R-track studies, unbounded; transform s = σ/ε). σ and s are different numbers — same physical sheet, but they diverge non-trivially at second order in shear, so values reported in one form cannot be plugged directly into formulas written in the other. The framework's derivations use σ; s appears when referencing studies or displaying the lattice form. Within metric-charge's single-shear scope, bare σ ≡ σ_uw (the only shear present); downstream work with multiple species uses σ_e, σ_p, ... for species-specific shears.*

This single block establishes the working convention. After it, bare σ and bare ε are the working symbols throughout; s appears only where the lattice form is referenced; no renames are needed.

### 7.6 README

Add a paragraph to "Ground rules" or a new "Strategic stance" subsection:

> *The metric is the framework's primary structural object. For each closure-satisfying particle species, the framework should ultimately provide a metric prescription (specific values of the diagonals, ε, σ) derived from the species' structural properties. This project sets up the single-particle case and characterizes what charge looks like given a sheet; deriving the parameter values from species identity is downstream work, in metric-binding and beyond.*

### 7.7 Ch 7, Ch 8 light pass

No σ renames. The chapters' existing σ_uw / "σ" stays. Where the lattice-form is being discussed (mostly in passages that draw on work-m8a's §9.3 and work-ch9's §7 content), introduce **s** with the transform s = σ/ε and the L_w^B = √(1−σ²)·L_w correction. Bare ε requires no changes.

### 7.8 metric-binding's README

No changes required. The three σ_uw references stay valid under the new convention (bare σ ≡ σ_uw within single-shear scope).

### 7.9 STATUS

Add new todos:

- **TODO-Disc1**: Multi-sheet substrate-sharing question — resolved in metric-binding's framing.
- **TODO-Disc2**: Multi-species diagonal-normalization choice — resolved in metric-binding's framing.
- **TODO-Disc3**: Chapter refactor per §§7.1–7.8 above.

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
