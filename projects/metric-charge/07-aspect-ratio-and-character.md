# Chapter 7 — Aspect ratio and character

This chapter turns on the aspect ratio ε ≡ L_u / L_w as a free parameter and asks what changes about the closure-satisfying inventory as ε varies. So far the framework has treated ε as a symbolic label without examining its consequences. This chapter examines them.

The chapter is in **discovery mode**: it does not pre-commit to which (m, n) modes "should" dominate at which ε regimes. Instead it works out what the math says about mode masses, dispersion, closure-satisfaction, and stability across the ε parameter space, and reports what emerges. MaSt model-F's identifications (electron sheet at large ε, neutrino sheet at very large ε, proton sheet near ε ≈ 1) serve as **reference targets** — patterns the framework's predictions can be compared against — not as identifications this chapter pre-commits to.

**Inheritance.**

- *From [Chapter 1 §3](01-foundation.md):* the aspect ratio definition ε ≡ L_u / L_w and its parameter status.
- *From [Chapter 2 §3](02-modes-on-a-sheet.md):* the rest-mass formula m_(m,n) = (ℏ/c)·√((2πm/L_u)² + (2πn/L_w)²) — explicitly ε-dependent.
- *From [Chapter 4 §6](04-the-closure-condition.md):* the closure-satisfying inventory.
- *From [Chapter 5](05-metric-self-consistency.md):* the gauge-potential structure for closure-satisfying modes; structural neutrality of single-axis modes.
- *From [Chapter 6](06-handedness-and-pairs.md):* the handedness structure within each (m, n) sector; the distinction between *structural* neutrality (single-axis modes, missing one of two U(1)s) and *cancellation* neutrality (single field with both (m, n) and (−m, −n)).

**Distinctive job.** Determine how varying ε across (0, ∞) changes the mode mass spectrum, the closure-eligibility partition, and which modes are energetically accessible / stable. Identify any qualitatively different regimes (small ε "thin sheet," large ε "fat sheet," ε ≈ 1 symmetric). Connect (without committing) to MaSt model-F's identifications of electron / proton / neutrino sheets at specific ε values.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | Setting up the ε sweep — explicit ε-dependence of mass formula |
| 2 | Mass spectrum across the ε sweep |
| 3 | Closure-eligibility under varying ε |
| 4 | Three regime characters — small ε, ε ≈ 1, large ε |
| 5 | The "diffuse charge" question |
| 6 | Three-phase character — does it emerge from ε alone? |
| 7 | Summary — sheet character from ε |
| 8 | What's next |

---

## 1. Setting up the ε sweep

The rest-mass formula from [Chapter 2 §3](02-modes-on-a-sheet.md) is:

<!-- m_(m,n) = (ℏ/c) · √((2πm/L_u)² + (2πn/L_w)²) -->
$$
m_{(m,n)} \;=\; \frac{\hbar}{c}\sqrt{\left(\frac{2\pi m}{L_u}\right)^2 + \left(\frac{2\pi n}{L_w}\right)^2}
$$

Substitute L_u = ε · L_w and factor out (ℏ/c)·(2π/L_w):

<!-- m_(m,n) = (ℏ/c) · (2π/L_w) · √((m/ε)² + n²) -->
$$
m_{(m,n)} \;=\; \frac{\hbar}{c}\cdot\frac{2\pi}{L_w}\cdot\sqrt{\bigl(m/\varepsilon\bigr)^2 + n^2}
$$

This rephrasing exposes ε's structural role: it tilts the relative cost of u-windings vs w-windings. The factor (ℏ/c)·(2π/L_w) sets the absolute mass scale; the square root sets the *relative* masses across the (m, n) family at given ε.

Three limits:

- **ε → 0** (thin sheet, L_u ≪ L_w): the (m/ε)² term dominates whenever m ≠ 0. Modes with m ≠ 0 become very heavy; modes with m = 0 are unaffected.
- **ε → ∞** (fat sheet, L_u ≫ L_w): the (m/ε)² term vanishes. Modes with m ≠ 0 lose their u-contribution to mass; the n² term dominates relatively.
- **ε = 1** (symmetric Clifford torus, L_u = L_w): both directions contribute equally, m_(m,n) ∝ √(m² + n²).

This is the structural lens for the rest of the chapter: ε determines which subset of the (m, n) inventory has low energy.

**Sweep convention.** Throughout this chapter, we hold L_w fixed and vary L_u. So ε varies by changing L_u, with L_w as the reference scale. Other conventions (holding L_u fixed; holding sheet area L_u·L_w fixed) would give equivalent structural conclusions but different numerical scaling.

---

## 2. Mass spectrum across the ε sweep

For each closure-satisfying class from [Chapter 4 §6](04-the-closure-condition.md), we examine how the mass depends on ε.

### 2.1 The lightest closure-eligible mode at each ε

The lightest mode satisfying closure (both windings nonzero) at given ε is determined by minimizing √((m/ε)² + n²) over (m, n) with both nonzero. The candidates:

- **(1, 1):** mass scales as √(1/ε² + 1)·(ℏ/c)·(2π/L_w). Light when ε is moderate; rises as 1/ε at small ε; saturates at (ℏ/c)·(2π/L_w) for large ε.
- **(1, 2):** mass scales as √(1/ε² + 4)·(ℏ/c)·(2π/L_w). Heavier than (1, 1) for any ε > 0.
- **(2, 1):** mass scales as √(4/ε² + 1)·(ℏ/c)·(2π/L_w). Heavier than (1, 1) for any ε > 0.
- General (m, n) with both ≥ 1: mass increases as either |m| or |n| grows.

So **(1, 1) is the lightest closure-eligible mode at every ε > 0**.

How m_(1,1) varies with ε:

| ε | m_(1,1) (in units of (ℏ/c)·(2π/L_w)) |
|---|---|
| ε → 0 | √(1/ε² + 1) → 1/ε → ∞ |
| ε = 1 | √2 ≈ 1.41 |
| ε → ∞ | √(0 + 1) = 1 |

The lightest closure-satisfying mode goes from infinitely heavy (at small ε) to a finite limit (≈ (ℏ/c)·(2π/L_w)) at large ε. The sweep is asymmetric: small ε pushes closure-satisfying modes to high mass, large ε saturates them at a finite minimum.

### 2.2 Mass tower above the ground state

The mode tower's organization changes with ε:

- **ε ≪ 1:** the (m/ε)² term dominates. Mass tower ordered primarily by |m|, with n contributing weakly. (1, 1), (1, 2), (1, 3), ... are the lightest closure-satisfying levels (heavy but ordered by n at fixed m = 1); (2, q), (3, q), ... are very heavy.
- **ε = 1:** mass tower ordered by √(m² + n²); roughly equal contributions from m and n.
- **ε ≫ 1:** the n² term dominates. Mass tower ordered primarily by |n|. (1, 1), (2, 1), (3, 1), ... are the lightest closure-satisfying levels; modes with n = 2, 3, ... are heavier.

The *organization* of the mass tower reorganizes as ε changes. At small ε, modes are organized by their u-winding. At large ε, by their w-winding. At ε = 1, by their total winding magnitude.

### 2.3 Order changes

Different (m, n) modes are conserved sectors and don't actually "cross" in the dynamical sense — they're independent solutions, not eigenvalues of one operator. But there are *order changes* in the spectrum: at small ε, (1, 2) is lighter than (2, 1); at large ε, (2, 1) is lighter than (1, 2). The crossover happens at ε² = 4, i.e., ε = 1/2 (where (1, 2) and (2, 1) have equal mass).

The order-change structure means the *organization* of the mode spectrum reorganizes as ε varies, even though specific (m, n) labels are conserved. A sheet at small ε has different "lowest-energy excitations" than the same sheet at large ε.

---

## 3. Closure-eligibility under varying ε

Closure eligibility is *topological* — both windings nonzero — and does not depend on ε directly. A mode at (1, 1) is closure-eligible at every ε ∈ (0, ∞).

But which (m, n) modes are *energetically accessible* depends on ε strongly. A sheet at given ε that is energetically constrained (say, by thermal equilibrium at some temperature, or by being the ground state of some embedded system) populates only modes with mass ≲ the available energy budget. Which closure-eligible modes meet this constraint depends on ε.

Specifically:

- At small ε, the energy gap between the lightest closure-eligible mode (1, 1) and the lower-mass closure-failing single-axis modes (0, q) is large in absolute terms (m_(1,1) ~ 1/ε vs m_(0, q) ~ q, so the gap grows as 1/ε). A sheet at low temperature populates the (0, q) modes preferentially — single-axis dominates the low-energy spectrum.
- At large ε, the gap between closure-eligible (1, 1) and closure-failing single-axis (m, 0) is also large (m_(1,1) ~ √(0 + 1) = 1 saturates while m_(m, 0) ~ m/ε → 0). Single-axis again dominates at low energy.
- At ε ≈ 1, all (m, n) ≥ 1 combinations have comparable masses; closure-eligible (1, 1) is the lightest closure-satisfying mode and is competitive with single-axis modes at the same energy.

The qualitative observation: **whether a sheet at given ε hosts predominantly closure-satisfying modes or predominantly single-axis modes depends on ε's relationship to the framework's energy scale.** A sheet's "character" is determined by which modes dominate at low energy, and that depends on ε.

---

## 4. Three regime characters

The ε sweep produces three qualitatively different regimes based on which mode classes dominate at low energy.

**Important clarification on neutrality.** The neutrality that emerges from single-axis modes dominating at low energy is **structural neutrality** in the sense developed in [Chapters 4 and 5](04-the-closure-condition.md) — single-axis modes have one of the two winding numbers exactly zero, so they source only one of the two U(1) gauge potentials and lack the U(1) × U(1) cross-coupling that produces observable EM. This is *not* the **cancellation neutrality** of [Chapter 6 §4](06-handedness-and-pairs.md), where a single field configuration contains both (m, n) and (−m, −n) at equal amplitude and the off-diagonals cancel.

Both are mechanisms for "massive but EM-neutral" states; this chapter's regimes distinguish themselves through *which mode class is energetically accessible*, which is a structural-neutrality question. Cancellation neutrality is independent of ε and operates in any regime where opposite-handedness pair configurations are populated.

### 4.1 Small ε regime — "single-axis-dominated character"

At small ε (thin sheet, L_u ≪ L_w), the lightest modes are (0, n) single-axis. These are *closure-failing structurally*: they have exactly one winding number nonzero, and per [Chapter 4](04-the-closure-condition.md) they cannot satisfy the closure condition regardless of phase or amplitude — one of the two U(1) gauge potentials is structurally absent. The closure-eligible modes (1, q), (1, 1), etc. are heavier by a factor scaling as 1/ε.

A sheet at small ε that is energetically constrained to its lightest modes is dominated by **mass-without-charge** states via the structural mechanism. The sheet's character at low energy is "massive but EM-neutral by missing a U(1)."

This matches a structural pattern that MaSt model-F's neutrino-sheet identification ascribes: a sheet whose dominant low-energy modes are massive but EM-neutral. Whether the framework's small-ε regime corresponds quantitatively to standard physics' neutrinos is downstream MaSt-correspondence work; the structural pattern (mass-only modes dominating low energy via the structural mechanism) matches.

### 4.2 Symmetric ε ≈ 1 regime — "single-phase charge character"

At ε ≈ 1 (symmetric Clifford torus, L_u ≈ L_w), the lightest closure-satisfying mode is (1, 1) with mass m_(1,1) = √2·(ℏ/c)·(2π/L_w) — comparable to the lightest single-axis modes m_(0, 1) = m_(1, 0) = (ℏ/c)·(2π/L_w). The sheet supports charged states as low-mass excitations — closure-eligible (m, n) modes are not particularly suppressed relative to single-axis modes at this ε.

A sheet at ε ≈ 1 hosts both single-axis (mass-only) and closure-satisfying (charged) states at similar energies. From a low-temperature equilibrium perspective, both are populated, with charged states comparable in abundance to single-axis modes.

This regime supports what could be called "single-phase charge character" — single charged states (gcd = 1 in (m, n)) as the dominant closure-satisfying configuration. Whether this corresponds to what standard physics calls leptonic / single-charged-particle behavior is a downstream identification question.

### 4.3 Large ε regime — "extreme-asymmetry character"

At very large ε (fat sheet, L_u ≫ L_w), the situation is structurally similar to the small-ε regime but with u and w swapped. The lightest modes are (m, 0) single-axis — closure-failing, with the m-winding alone. The lightest closure-eligible mode (1, 1) saturates at finite mass (ℏ/c)·(2π/L_w), but the single-axis modes (m, 0) become correspondingly lighter (mass ∝ m/ε → 0 for fixed m as ε → ∞).

So the large-ε regime is again dominated by mass-only single-axis modes at low energy, with closure-satisfying modes accessible only at energies above the saturation scale (ℏ/c)·(2π/L_w). The structural pattern is mirror to the small-ε regime under cycle-swap u ↔ w.

**Apparent disagreement with MaSt model-F.** Model-F places the electron sheet at very large ε (ε ≈ 397 — a "fat sheet"). Under the framework's analysis here, large ε is a *mass-only-dominated regime*, not a charged-particle regime. This is a structural discrepancy that the chapter cannot resolve without additional work.

Possible resolutions:

- **Convention mismatch.** Model-F's ε might be defined with the opposite sign convention from this chapter's (e.g., ε = L_w/L_u rather than L_u/L_w). Under that convention, model-F's ε ≈ 397 maps to this chapter's ε ≈ 0.0025 — small ε, also a mass-only-dominated regime under the framework's analysis. Either way, the framework's prediction does not place electron-class behavior at extreme ε.

- **Mechanism not captured by linearized analysis.** At very large (or very small) ε, perhaps some nonlinear effect, dynamical mechanism, or substructure makes (1, q) closure-eligible modes the relevant low-energy excitations despite the linearized mass formula. The framework's analysis here is linear; a deeper analysis might find the "right" mode emerges from corrections.

- **Model-F identification is provisional.** The model's identification of electron-sheet ε ≈ 397 may be specific to the model's choice of overall scale and aspect ratio convention; it may not be a robust prediction across alternative conventions.

The chapter does not resolve the discrepancy. It flags it as an honest open question — the framework here predicts ε ≈ 1 as the natural charged-particle regime; model-F places the electron at extreme ε. The two are compared as reference targets; resolving the difference is downstream MaSt-correspondence work.

---

## 5. The "diffuse charge" question

For very large ε (fat sheet) under the convention L_u ≫ L_w, the compact direction whose winding produces "charge" (the w-cycle, per the closure rule's asymmetric preference) is geometrically tiny. What does this look like physically?

Two interpretations:

**Concentrated charge.** A closure-satisfying mode at large ε has its w-direction structure concentrated in a small geometric volume. From a coarse-grained view, the charge is geometrically concentrated in a tiny region of the compact structure.

**Diffuse charge.** Alternatively, the small L_w means the w-mode's standing wave has high spatial frequency in w. From a coarser perspective, this looks like a finely-textured pattern over the whole sheet.

The framework's view at the linearized level: this depends on what "diffuse" means at the metric level. The off-diagonal sourcing analysis of [Chapter 5](05-metric-self-consistency.md) effectively averages over compact-direction details — the gauge potentials A_μ, B_μ that emerge are functions of the extended-spacetime coordinates only, with the compact-direction structure integrated out. So at the gauge-potential level, the w-direction's small size doesn't translate to "diffuse charge" — it translates to a definite gauge potential in S regardless of L_w.

Where the L_w-smallness *does* matter is in:

- The mode's resolution/granularity within (u, w). High-frequency standing waves on a small w-cycle resolve fine substructure that low-frequency ones don't.
- The mode's coupling to higher-order corrections that depend on compact-direction structure (e.g., higher-derivative terms in a more complete action).
- The mode's response to perturbations that couple to compact-direction wavelength specifically (e.g., very high-energy scattering).

At the linearized level relevant to chapters 4–7, "diffuse charge" is not a substantive distinction. At higher levels of analysis, it might become one.

MaSt model-F's neutrino-sheet identification interprets neutrino "diffuseness" as coming from a very large compact-direction length scale. Under the convention mapping discussed in §4.3, this might correspond to either large or small ε in the framework's conventions — convention-dependent. The framework treats the small-ε regime (or the large-ε regime, depending on convention) as a candidate identification for what model-F calls the neutrino sheet, contingent on resolving the convention mapping.

---

## 6. Three-phase character — does it emerge from ε alone?

[Chapter 4 §4.3](04-the-closure-condition.md) identified multi-component links T(km, kn) as the structure for fractional-charge configurations: k phased copies of a primitive T(m, n), with each phase slot carrying 1/k of the primitive's charge. The closure condition is satisfied collectively across the k components.

Does the multi-component structure emerge naturally at any specific ε regime — i.e., does ε alone select multi-component links over single-component closure-satisfying modes?

The mass formula says no. At any ε, the lightest closure-satisfying mode is (1, 1) — single-component, gcd = 1. Multi-component links require larger (m, n) values (specifically, (m, n) with gcd > 1) and are correspondingly heavier:

- **(2, 2) = 2 × (1, 1)** has mass m_(2,2) = √2 · m_(1,1) at any ε. Heavier; not favored.
- **(3, 3) = 3 × (1, 1)** has mass √3 · m_(1,1). Even heavier.
- **(2, 4) = 2 × (1, 2)** has mass 2·m_(1,2). Heavier than (1, 2) which is already heavier than (1, 1).

Energetic minimization at any ε prefers single-component closure-satisfying modes over multi-component links. The (m, n) with gcd > 1 are systematically heavier than equivalent (m, n) with gcd = 1.

At each ε regime:

- **Small ε:** the dominant closure-eligible modes are heavy single-component types. Multi-component links are heavier still. ε does not favor them.
- **ε ≈ 1:** lightest closure-satisfying is (1, 1) = single-component. Multi-component (2, 2) = 2 × (1, 1) is heavier. Not favored.
- **Large ε:** symmetric to small ε. Same conclusion.

The chapter's tentative finding: **ε alone does not select multi-component (3-component) structure.** Some additional mechanism is needed.

[Chapter 8](08-shear-and-fractional-charge.md) provides the candidate mechanism: shear σ_uw breaks the symmetry between equal-mass configurations, and *specifically* selects k = 3 cleanly via a structural argument tied to the metric's anti-symmetry. The three-phase character that MaSt model-F identifies with quark organization plausibly emerges from shear, not from aspect ratio.

This is a substantive finding of chapter 7: ε is not the parameter that produces the three-phase structure. ε produces three structural regimes (mass-only-dominated at extreme ε, charge-friendly at ε ≈ 1) but doesn't differentiate among the closure-satisfying *sub-classes* (single-component vs k-component link). That differentiation comes from shear in chapter 8.

---

## 7. Summary — sheet character from ε

The ε sweep produces a structural map of the closure-eligible inventory at each regime:

| ε regime | Lightest closure-satisfying class | Single-axis mass relative to (1, 1) | Sheet character |
|---|---|---|---|
| ε ≪ 1 | (1, 1) but heavy (1/ε² dominant) | (0, n) much lighter | Heavier closure-satisfying tier above light single-axis modes; mass-only-dominated low-energy spectrum |
| ε ≈ 1 | (1, 1), mass ≈ √2 · (ℏ/c)·(2π/L_w) | (0, 1) and (1, 0) at comparable mass | Single-phase charge regime; charged states accessible at low energy |
| ε ≫ 1 | (1, 1), saturating at (ℏ/c)·(2π/L_w) | (m, 0) much lighter (mass ∝ m/ε) | Heavier closure-satisfying tier; mass-only-dominated low-energy spectrum (mirror of ε ≪ 1) |

The framework predicts **three structural regimes**, with the symmetric ε ≈ 1 case being the "charge-friendly" one and the asymmetric extremes being "single-axis-dominated" (i.e., mass-only states dominate at low energy via the structural-neutrality mechanism of [Chapters 4–5](04-the-closure-condition.md)).

How this maps onto MaSt model-F's three sheets (electron, proton, neutrino) is an open MaSt-correspondence question. The framework's structural prediction does not obviously match model-F's quantitative ε assignments (model-F's electron sheet at ε ≈ 397 is, under the framework's analysis, a single-axis-dominated regime, not a charged-particle regime). The discrepancy is flagged for downstream examination; the chapter does not resolve it.

What the chapter does establish:

- The framework predicts a **three-regime structure** based on ε.
- The **central regime** (ε ≈ 1) is the closure-friendly / charge-friendly regime.
- The **asymmetric extremes** are single-axis-dominated regimes — mass-only via structural neutrality.
- **ε alone does not select multi-component structure** — chapter 8's shear is needed for the three-phase mechanism that might correspond to standard physics' quark organization.
- Cancellation neutrality (Chapter 6) operates independently of ε; this chapter's mechanism is exclusively structural neutrality.

---

## 8. What's next

[Chapter 8 — Shear and fractional charge](08-shear-and-fractional-charge.md). Turn on σ_uw and examine its effects. Test the prediction (Chapter 6 §6) that shear biases matter over antimatter. Then derive the fractional-charge mechanism: N phased wraps distributed in w contribute 1/N charge each, and shear is what selects N = 3 cleanly. This is where the multi-component link structure of [Chapter 4 §4.3](04-the-closure-condition.md) connects to the three-phase structure that MaSt model-F (and standard physics' quark organization) might correspond to.

Chapter 8 changes the parameter focus from sheet shape (ε, this chapter) to sheet skew (σ_uw). Together, chapters 7 and 8 cover the two metric-sheet parameters that shape the inventory at the linear level.

---

## What this chapter does **not** do

- **Does not commit to specific MaSt model-F identifications.** The framework's small-ε / large-ε / symmetric-ε regimes are described as structural patterns; whether they correspond specifically to model-F's electron / proton / neutrino sheets requires quantitative comparison and is downstream MaSt-correspondence work.
- **Does not resolve the discrepancy** between the framework's symmetric-ε charge prediction and model-F's large-ε electron-sheet identification. Flagged as an open question, with three candidate resolutions identified (convention, missing mechanism, model-F revision).
- **Does not derive the fractional-charge mechanism.** Chapter 8.
- **Does not analyze nonlinear effects of large ε** (where the linearized treatment may break down). Out of scope for chapter 7; possibly worth flagging in chapter 8 or downstream.
- **Does not predict a specific mechanism for sheet ε to take a specific value.** The framework treats ε as a free parameter; whether ε is dynamically determined by some deeper principle is open. metric-binding might provide insight (multi-knot energetics may favor specific ε values for stable bound states).
- **Does not commit to what "diffuse charge" actually means.** Multiple interpretations are flagged in §5; the chapter does not select one and leaves the question for higher-level analysis.
- **Does not analyze cancellation neutrality** (Chapter 6's mechanism). That mechanism is independent of ε and is treated separately.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Why does MaSt model-F place the electron at ε ≈ 397 when the framework's ε ≈ 1 regime is the natural charged-particle regime? | Open MaSt-correspondence question; possibly resolves via convention-mapping or via mechanism not in chapter 7's scope |
| Does ε alone select the three-phase character, or does it require shear? | Answered in §6: requires shear (chapter 8) |
| Is there a mechanism that dynamically determines ε? Or is ε a free parameter set by the embedding cosmology? | Out of scope for metric-charge; possibly metric-binding or downstream |
| Does the framework's small-ε regime correspond to standard-physics neutrinos quantitatively, or only structurally? | Downstream MaSt-correspondence work |
| At very large ε, does the linearized treatment of the closure-eligibility partition still hold, or do nonlinear effects dominate? | Out of scope; possibly relevant for chapter 8 or follow-up projects |
| What "diffuse charge" actually means physically — concentrated in small w-cycle, spread over wave structure, or something else? | Open; depends on how the chapter 5 gauge-potential identification handles compact-direction averaging at higher orders |
| Are the convention mappings between this chapter's ε and MaSt model-F's ε well-defined, or do they introduce ambiguity in the comparison? | Downstream MaSt-correspondence work |
