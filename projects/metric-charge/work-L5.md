# work-L5.md — TODO-L5: Fractional-charge sign assignments

This file frames [TODO-L5](STATUS.md): the framework's "1/k charge per component" prediction (Configuration Y, [Ch 8 §5](08-shear-and-fractional-charge.md)) gives uniform per-component fractional charge, which does not match the observed quark pattern (proton = u + u + d = +2/3 + 2/3 − 1/3 = +1).

The work falls into two layers, separated by metric-charge's structural scope (what the sheet supports) vs metric-binding's territory (what binds multi-component systems into observed particles):

- **Layer 1 (in scope for metric-charge):** Structural audit of what charge-sign configurations a single sheet supports. Sign-tracing per primitive (T(±1, ±n')), per-component charge in uniform-phase Configuration Y multi-links, and the existence-as-inventory-items of mixed-orientation compound configurations (e.g., 2 × T(1, n') + 1 × T(−1, n')) with their external charge given by tube-winding sum. All of this is "what mode configurations the framework's mode-language describes," independent of stability or empirical identification. Half-day editing pass.
- **Layer 2 (out of scope for metric-charge — forwarded to [metric-binding](../metric-binding/)):** Why specific compounds are stable as observed particles. Why the proton's quark mix is 2:1 rather than 3:0. What binds the components. How internal substructure manifests in scattering. The fractional vs integer per-component charge reading. The R-track studies (R53 / R54 / R63 / R64) and the R-track's mode-by-mode picture are the empirical inputs feeding this downstream resolution.

Conventions follow the rest of the project. M ≡ (ℏ/c)·(2π/L_w). σ ≡ σ_uw.

---

## Sections

| § | Topic |
|---|-------|
| 1 | Layer 1 — sign-tracing audit |
| 2 | Context: the R-track's mode-by-mode approach |
| 3 | Three structural hypotheses |
| 4 | Recommendation |

---

## 1. Layer 1 — sign-tracing audit

Under the single-Bloch-mode interpretation of [Ch 8 §2.2](08-shear-and-fractional-charge.md) and the wrap-order convention of [Ch 1 §10](01-foundation.md), the closure-satisfying primitive is T(1, n'). EM charge couples to tube-direction momentum p^w (per [Ch 5 §4.6.4](05-metric-self-consistency.md) Lorentz-force structure m_phys d²x^μ/dτ² = F^B^μ_ν v^ν p^w). Under the tuple convention, m is the tube winding label, so k_w = 2πm/L_w and:

<!-- p^w = ℏ k_w = ℏ (2π/L_w) m -->
$$
p^w \;=\; \hbar\, k_w \;=\; \hbar\,\frac{2\pi}{L_w}\, m
$$

For a Bloch mode at (m, n) = (±1, ±n'), the framework's natural charge-sign assignment organizes by the four discrete reflections of [Ch 8 §2.1](08-shear-and-fractional-charge.md):

| Mode | p^w sign | Charge sign | Mass at σ ≠ 0 | Role |
|---|---|---|---|---|
| T(+1, n') | + | +1 | μ²(1, n'; σ, ε) | "particle" (wrap-order picks n' sign for lower mass) |
| T(−1, n') | − | −1 | μ²(−1, n'; σ, ε) = μ²(1, n') + 4σn'/ε | R_w-conjugate — opposite charge, mass-split |
| T(+1, −n') | + | +1 | μ²(1, −n'; σ, ε) = μ²(1, n') + 4σn'/ε | R_u-conjugate — same charge, mass-split |
| T(−1, −n') | − | −1 | μ²(−1, −n'; σ, ε) = μ²(1, n') | R_J-conjugate — opposite charge, mass-degenerate |

The R_J pair T(+1, n') ↔ T(−1, −n') is the framework's matter/antimatter labeling per [Ch 6 §3](06-handedness-and-pairs.md) — mass-degenerate under shear, opposite charge.

For a uniform-phase Configuration Y k × T(1, n') multi-link: all k components share the same primitive (+1, n'), all carry charge +1/k of the link's integer total charge k, all phases at 2πj/k for j = 0, ..., k−1. **Per-component charge sign is uniform** — no mixed-sign structure from intra-link phasing.

**Mixed-orientation compounds as inventory items.** The framework's mode-language can also describe configurations with non-uniform per-component orientations on a single sheet — for example, 2 × T(+1, n') + 1 × T(−1, n'). Such a compound is just a sum of three independent Bloch modes; it sits in the framework's inventory by construction. Its external integer charge follows the same tube-winding-sum rule as a uniform multi-link:

| Compound | Per-component charges | External integer charge (tube-winding sum) |
|---|---|---|
| 3 × T(+1, n') (uniform) | +1, +1, +1 | +3 |
| 2 × T(+1, n') + 1 × T(−1, n') | +1, +1, −1 | +1 |
| 1 × T(+1, n') + 2 × T(−1, n') | +1, −1, −1 | −1 |
| 3 × T(−1, n') | −1, −1, −1 | −3 |

The R_J-conjugates (e.g., T(−1, −n') replacing T(+1, n')) give the antiparticle direction of each row at equal mass.

Metric-charge's structural commitment: such compounds *exist* in the mode-language inventory with the charge arithmetic above. Whether any of them is *stable as a bound multi-component object* — and which of them realizes any particular observed particle — is a binding-mechanism question and is forwarded.

**Audit conclusion:** the framework's existing prediction is uniform-sign per component within a uniform-phase Configuration Y multi-link, but the broader mode-language also supports mixed-orientation compounds with sum-based external charge. The framework therefore *can* describe configurations whose external charge is +1 with three internal components (e.g., 2 × T(+1, n') + 1 × T(−1, n')) — but does not say what makes such a configuration stable or whether it realizes a proton-like state. That belongs to [metric-binding](../metric-binding/).

---

## 2. Context: the R-track's mode-by-mode approach

The R-track studies after R60 — specifically [R53-three-generations](../../studies/R53-three-generations/), with refinements in [R54-compound-modes](../../studies/R54-compound-modes/), [R63-proton-tuning](../../studies/R63-proton-tuning/), and [R64-nuclear-harmonic-stack](../../studies/R64-nuclear-harmonic-stack/) — take a structurally different approach to quark identification than metric-charge's Configuration Y picture:

- **Each quark gets its own (m, n) mode on the proton sheet.** R53's assignments are u = (1, 19), c = (1, 18), t = (7, 3) at one ε and s; d = (5, 4), s = (1, 1), b = (5, −5) at a different ε and s.
- **Mass hierarchies emerge quantitatively from shear-resonance numerics** (R53 reports u : c : t = 1 : 588 : 80,000 and d : s : b = 1 : 20 : 889 to high precision).
- **Charge per mode comes from a separate phase-locking rule** (the R-track's "Q132 v2 promotion-chain") tied to gcd structure of the mode's winding numbers — not from intra-link phasing within a multi-link.
- **The proton is a compound of three independent mode-assignments**, not a single 3-component Configuration Y multi-link.

The R-track has its own unresolved issue: two different shear values (≈ 19 for up-types, ≈ 0.8 for down-types) on what should be one physical sheet (R53 finding F16). R54 and R64 are exploring resolutions (cross-sheet σ_ep coupling, ring-flipped u/d primitives at one geometry). Neither is finalized.

The R-track's picture suggests:

> The +2/3, +2/3, −1/3 asymmetric pattern within a baryon is **mode-identity-and-binding**, not intra-link phasing.

If this is the right framing, Configuration Y is not the place metric-charge should look for the up/down sign asymmetry. Configuration Y explains *fractional-charge magnitude per component of a single primitive multi-link* — structurally distinct from the composition of a baryon from multiple distinct primitives.

---

## 3. Three structural hypotheses

Three structural ideas worth recording as concrete hypotheses, with the existing framework's stance on each and what would close it.

### 3.1 H1 — 120° phase separation produces ring-position separation

> Phase rotation around the ring (e.g., 120° for k = 3) produces ring-position separation between components on the compact sheet — *not* spatial separation in extended S₁/S₂.

**Framework status:** Already in Configuration Y per [Ch 8 §5](08-shear-and-fractional-charge.md). The k × T(1, n') multi-link at relative phases 2πj/k for j = 0, ..., k−1 is exactly this construction. The 120° spacing is the k = 3 specialization; each component is a phase-shifted copy of the same primitive at the same wavevector, with the phase offset translating to a positional offset around the ring (u-cycle).

**Charge consequence:** Each component carries the same per-component charge magnitude (1/k of the link's integer charge) with uniform sign. The 120° phasing produces ring-position separation, not charge-sign asymmetry between components.

**Conclusion:** H1 is the existing Configuration Y picture. Accounts for the magnitude prediction (1/k per component) but not for the sign-mix. Confirms what the framework already has; does not by itself deliver mixed-sign per-component charge — that requires the mixed-orientation extension noted in §1.

### 3.2 H2 — "Upside-down" knot carries opposite charge

> A knot rotated to fill space not occupied by the original (an inverted embedding on the same torus) carries opposite charge from the reference.

**Framework status:** Geometrically, "upside-down" on T² admits several interpretations under the four discrete reflections of [Ch 8 §2.1](08-shear-and-fractional-charge.md):

- **R_w reflection** — (u, w) ↔ (u, −w). Maps T(m, n) → T(−m, n). Flips tube winding label m → flips p^w → flips charge. Mass differs at σ ≠ 0 (R_w-split).
- **R_J = R_u ∘ R_w** — (u, w) ↔ (−u, −w). Maps T(m, n) → T(−m, −n). Flips both windings → flips p^w → flips charge. Mass unchanged at any σ (R_J preserved).

The natural geometric interpretation of "rotated 180° around a diameter through the torus, filling complementary space" is closest to R_J: simultaneous flip of both ring and tube directions, mass-preserving, charge-flipping. This is the framework's existing matter/antimatter labeling.

**Charge consequence:** T(+1, n') (particle) and T(−1, −n') (antiparticle) form a mass-degenerate, opposite-charge pair under R_J. Confirms the H2 intuition directly.

**Conclusion:** H2 recovers the existing R_J = matter/antimatter symmetry from the visualizer-level "inverted embedding" intuition. Audit-completeness item: state this geometric interpretation explicitly in [Ch 6 §3](06-handedness-and-pairs.md)'s R_J discussion as supporting intuition. The framework already has the structural content.

### 3.3 H3 — Mixed-orientation compound as a candidate baryon

> A compound of 2 components in regular orientation + 1 inverted gives external integer charge +1 by tube-winding sum, with internal per-component charges (+1, +1, −1). The mass of the compound at small ε is approximately that of the single mode T(1, 3n'), since the windings sum to (1, 3n') and the masses of the components add. A candidate structural picture for the proton.

This hypothesis cleanly splits across the metric-charge / metric-binding boundary:

**H3a — Structural availability (in scope for metric-charge).** Does the framework's mode-language admit mixed-orientation compounds on a single sheet? *Yes, trivially* — see §1's "Mixed-orientation compounds as inventory items." Three independent Bloch modes at (±1, ±n') can be present simultaneously in the field configuration; their stress-energies superpose, their external integer charge is the tube-winding sum, and their mass at linearized level (σ = 0) is the sum of per-component masses. This is structurally available and does not require new mechanism.

**H3b — Stability and identification (out of scope for metric-charge — forwarded to [metric-binding](../metric-binding/)).** What metric-charge cannot decide:

- **Why the 2:1 orientation mix is the realized configuration for a baryon-like state**, rather than 3:0 (uniform) or 1:2 (antibaryon-like) or other compositions. Stability is a multi-knot binding question.
- **What holds the three components together as a single object** versus letting them fly apart as three independent primitives. This requires inter-component interaction energetics — explicitly nonlinear, explicitly forwarded per [Ch 1 §11](01-foundation.md).
- **Why the per-component charge reads as fractional (±2/3, ±1/3 in standard-model units)** rather than integer (±1 in framework units). Whether this is a units convention, a deep-inelastic-averaging artifact, or a genuine structural mechanism is a phenomenological reading downstream of the framework's structural primitives.
- **The neutron analog.** The compound 1 × T(+1, n') + 2 × T(−1, n') has external integer charge −1, which is the antiproton direction under framework-units, not neutron (charge 0). A neutral 3-component baryon structurally requires either zero tube-winding sum from a different mix, or a different mode-content reading entirely (e.g., the R-track's mode-by-mode picture). This is downstream architectural work.

**What metric-charge delivers via H3a:** the existence of mixed-orientation compounds as inventory items, with explicit charge arithmetic. This is what §1's table records.

**What metric-binding receives via H3b:** the candidate compound structures, the open stability question, the neutron-analog puzzle, and the fractional-vs-integer charge reading. These are the natural inputs for binding-energetics work.

The R-track studies ([R53](../../studies/R53-three-generations/), [R54](../../studies/R54-compound-modes/), [R63](../../studies/R63-proton-tuning/), [R64](../../studies/R64-nuclear-harmonic-stack/)) supply the empirical companion thread — their two-shear puzzle and mode-by-mode assignments are alternative candidate readings of the same downstream question.

---

## 4. Recommendation

### 4.1 In scope for metric-charge — half-day editing pass

The structural audit of §1 should be propagated into the chapters where charge-sign assignments and multi-component compounds are currently implicit:

- **Ch 6 §3** ([handedness-and-pairs §3](06-handedness-and-pairs.md)): R_J already identified as matter/antimatter. Add an explicit statement that charge sign flips under R_J via p^w → −p^w, and include the four-mode table of §1 above as the framework's natural charge-sign assignment. Add H2's visualizer-level "inverted embedding" interpretation as supporting intuition.
- **Ch 8 §6 or §7** ([shear-and-fractional-charge](08-shear-and-fractional-charge.md)): tighten the fractional-charge claim. State what uniform-phase Configuration Y predicts (uniform per-component sign at 1/k charge magnitude) and what it does *not* predict (mixed-sign baryon patterns). Note that the framework's mode-language *does* support mixed-orientation compounds as inventory items, with external integer charge given by tube-winding sum (per §1's table) — but their stability and any empirical identification is forwarded.
- **Ch 8 forward-pointer:** add an explicit reference to the R-track's mode-by-mode picture (§2 above) and to H3b (§3.3, the binding-stability and identification questions) as the downstream work needed to close baryon composition. The forward-pointer should be specific about what is being deferred, not a vague placeholder.

Estimate: half-day editing pass. Independent of TODO-N2 / TODO-P3 / Ch8a — can be done at any time.

### 4.2 Forwarded — concrete pointers

- **[metric-binding](../metric-binding/):** Stability of mixed-orientation compounds (H3b), inter-component binding mechanism, the neutron-analog question, and the fractional-vs-integer per-component charge reading. Receives §1's compound inventory table and the H3 picture as candidate input.
- **R-track ([R53](../../studies/R53-three-generations/), [R54](../../studies/R54-compound-modes/), [R63](../../studies/R63-proton-tuning/), [R64](../../studies/R64-nuclear-harmonic-stack/)):** Empirical mode-by-mode quark identification, including the two-shear puzzle and its in-progress resolution attempts. Alternative reading to the H3a compound-inventory picture; downstream work will need to reconcile or choose between them.
- **[grid-duality](../grid-duality/):** Substrate-level structure that might constrain which mixed-orientation compounds are realizable at the L2 promotion level. Open structural question.

### 4.3 What this work product delivers

- A clean statement of what charge signs metric-charge predicts per primitive and per uniform-phase Configuration Y multi-link.
- The structural existence of mixed-orientation compounds as inventory items, with explicit per-component and external-charge arithmetic.
- An honest scope boundary: what metric-charge can decide (mode-language support, structural inventory) vs what is binding-mechanism work (stability, identification, fractional-charge reading).
- Concrete forward-pointers naming H3b's open questions and the R-track's empirical thread as candidate inputs for metric-binding.

The audit's half-day editing pass is the actionable next step. H1 and H2 are recoveries of existing framework content; H3a is the new in-scope structural item (mixed-orientation compound inventory); H3b is the cleanly-bounded handoff to metric-binding.

---

## Notes

The R-track's two-shear puzzle (R53 F16) is the active barrier to a clean closed picture in downstream work. metric-charge does not need to resolve it; the forward-pointer should reflect that the downstream picture is still settling.

The H3a / H3b split clarifies what metric-charge can honestly deliver (mixed-orientation compound inventory + charge arithmetic) versus what is genuinely binding-mechanism work (stability, identification, the neutron-analog puzzle, the fractional-vs-integer reading). Metric-charge does not commit the framework to any specific compound being the proton; it supplies the structural building blocks and a clean handoff. If a downstream investigation produces a stable mixed-orientation reading of the proton, the result feeds back to metric-charge only as a citation; if a different reading wins (e.g., the R-track's mode-by-mode picture), the framework's compound-inventory table still stands as honest structural content.
