# Chapter 4 — The closure condition

**Status:** Sparse outline. Each section is one to three sentences describing the derivation step that section will perform. To be expanded into full prose once the outline is approved.

This chapter takes the closure condition stated axiomatically in [Chapter 1 §10](01-foundation.md) and works through which (m, n) modes actually satisfy it. Chapter 2 identified the three mode classes (light, single-axis, diagonal); chapter 3 partitioned the diagonal class further (weak-knot, genuine-knot, multi-component link). This chapter takes the **eligible** modes (both windings nonzero) and asks: which actually fire the closure rule? It also examines variants of the closure condition and what particle inventory each variant would select.

**Inheritance.**

- *From [Chapter 1 §10](01-foundation.md):* the closure condition stated in three equivalent views (phase-pattern, topological, metric-side preview).
- *From [Chapter 2 §4](02-modes-on-a-sheet.md):* the three mode classes, with eligibility = both windings nonzero.
- *From [Chapter 3 §7](03-knots-on-the-torus.md):* the five-row partition (light, single-axis, weak-knot diagonal, genuine-knot diagonal, multi-component link).

**Distinctive job.** Distinguish eligibility from satisfaction. Determine which eligible (m, n) values actually satisfy the standing-wave alignment requirement. Examine alternative closure rules and the particle inventories each selects. Hand off to chapter 5 for the metric-side equivalent and to chapter 6 for handedness/chirality structure within the satisfying inventory.

---

## Bare outline

### 1. The closure condition restated

Bring forward [Chapter 1 §10](01-foundation.md)'s three views. State each cleanly so the rest of the chapter has a precise target:

- **Phase-pattern view:** the wave's phase completes a full 2π winding on w *and* a complete standing wave on both u and w during a single closed traversal.
- **Topological view:** both winding numbers (m, n) are nonzero, providing the U(1) × U(1) cross-coupling structure of [grid-duality §7.5–§8](../grid-duality/07-wrap-promotion-modeling.md) that charge requires.
- **Metric-side view:** the off-diagonal metric entries that mass sources (per metric-mass Chapter 5) form a valid Kaluza-Klein gauge potential pattern. Developed fully in chapter 5.

The chapter operates primarily on the phase-pattern view; the topological view is used as a structural cross-check; the metric-side view is referenced but its derivation is chapter 5's job.

### 2. Eligibility versus satisfaction

Two distinct conditions, conflated in earlier chapters and worth separating cleanly here:

- **Eligibility** — the topological prerequisite. A mode is eligible if both winding numbers (m, n) are nonzero. From chapters 2–3: light (0, 0) and single-axis modes (m, 0), (0, n) are not eligible; diagonal modes (both nonzero) are eligible.

- **Satisfaction** — the dynamical/phase requirement. An eligible mode *satisfies* closure if its standing-wave structure on u and w is properly aligned to lock during one closed traversal of T(m, n).

Most of this chapter examines satisfaction within the eligible class. The hypothesis at outline stage: under the standard closure rule of Chapter 1 §10, all eligible modes satisfy closure for *some* sub-(m, n) phase choice; the phase choice is what the chapter must pin down.

### 3. The standing-wave alignment requirement

What does "complete standing wave on both u and w during one closed traversal" mean precisely?

For a separable mode φ(t, u, w) ∝ e^{−iωt} · U(u) · W(w) with U, W standing waves:

- A closed traversal of T(m, n) traces a path (u(s), w(s)) where u and w advance in proportion m : n.
- As s advances, U(u) cycles through m periods of its standing wave; W(w) cycles through n periods.
- "Closure locks" when the standing-wave cycling is *aligned* — node-to-antinode-to-node correspondence between the U and W factors, integer-resolved during the traversal.

For separable modes with both (m, n) nonzero, closure-locking is automatic at the integer level (m periods × n periods = mn during traversal). The **sub-(m, n) phase alignment** (the relative phase between U(u) and W(w)) determines whether the locking is *centered* (node coincidence) or shifted. Chapter 5 will show the centered alignment is what produces a valid KK gauge potential.

Note for downstream chapters: phase alignment is a *sub-(m, n) label* — it does not affect topology but affects observability. This is the label that distinguishes closure-satisfying from closure-failing within the eligible class.

### 4. Which (m, n) satisfy closure (under the standard rule)

Walk through the three eligible classes from [Chapter 3 §7](03-knots-on-the-torus.md):

**4.1 Weak-knot diagonal** — T(1, q) and T(p, 1) with both nonzero.
- (1, q): m = 1, n = q ≠ 0. Standing waves on both directions. Closure: **satisfied** at centered alignment.
- T(1, 2) — [matter-from-light §4](../../papers/matter-from-light.md) identifies this with the electron via the 1:2 winding ratio.
- Topologically the unknot but physically a genuine charged-particle candidate.

**4.2 Genuine-knot diagonal** — T(p, q) with p, q ≥ 2 and gcd(p, q) = 1.
- T(2, 3) trefoil, T(2, 5) cinquefoil, T(3, 4), T(3, 5), ...
- Closure: **satisfied** for each at centered alignment.
- Candidate organization: crossing-number tiers correspond to particle generations or mass tiers? Open question, returned to in chapter 7.

**4.3 Multi-component link** — T(km, kn) with gcd(m, n) = 1, k > 1.
- k phased copies of primitive T(m, n).
- Closure: **satisfied** *collectively*, with k-fold phase distribution along the shared cycle.
- Each phase slot carries 1/k of the primitive charge — chapter 8's fractional-charge / quark mechanism.
- Example: T(3, 6) = three copies of T(1, 2) at 1/3 phase offsets. Each component carries 1/3 of the T(1, 2) charge.

**4.4 Summary table** of the predicted inventory:

| Class | (m, n) example | Closure | Charge per component | MaSt analog (speculative) |
|---|---|---|---|---|
| Weak-knot diagonal | (1, 2) | ✓ | 1 | electron |
| Weak-knot diagonal | (1, 3), (1, 4), … | ✓ | 1 | further leptons / generations? |
| Genuine-knot diagonal | (2, 3) | ✓ | 1 | hadronic? proton-class? |
| Multi-component link | (3, 6) = 3 × (1, 2) | ✓ (3-fold) | 1/3 | quark candidate |

Treat the MaSt-analog column as exploratory — chapter 4 establishes only that closure is satisfied; whether each predicted state corresponds to an observed particle is a downstream question.

### 5. Closure-rule variants

Chapter 1 §10 noted three open variants of the closure rule. Examine each briefly to see what particle inventory it would select.

**5.1 Variant: 2π winding on u instead of w** (mirror of the standard rule).
- Selects modes with m ≠ 0 instead of n ≠ 0.
- Topologically gives the same knots as the standard rule (T(p, q) ≡ T(q, p)), but physically gives a *different* sub-family due to the symmetry-breaking conventions of [Chapter 3 §3.2](03-knots-on-the-torus.md).
- Whether u and w roles are unified at a deeper level — making the two variants physically indistinguishable — is a chapter 5 / grid question.

**5.2 Variant: standing wave on only one direction** (weaker rule).
- Would allow single-axis modes (m, 0) or (0, n) to satisfy closure.
- Implication: neutrino-class structural neutrality disappears — single-axis modes would carry observable charge.
- Inconsistent with metric-charge's neutrino-class candidate framing. Likely to be ruled out empirically.

**5.3 Variant: multi-knot collective closure** (no single knot satisfies, but a collection does).
- Example: a (1, 0) mode and a (0, 1) mode together cover both windings.
- Not what Chapter 1 §10 stated, but worth considering as a description of *bound states* (two single-axis modes that collectively satisfy closure when interacting).
- This variant naturally connects to metric-binding's bound-state regimen: paired single-axis modes might be the structural origin of certain composite particles.

### 6. The distinguished particle inventory

Under the standard closure rule of Chapter 1 §10, the predicted charged-state inventory is:

- **Weak-knot diagonal** modes T(1, q), T(p, 1) — single charged particles with topological-unknot structure.
- **Genuine torus knots** T(p, q) with p, q ≥ 2 — heavier charged particles with non-trivial topology.
- **Multi-component links** T(km, kn) with gcd > 1 — fractional-charge configurations (chapter 8).

The neutral / non-observable inventory:

- **Light** — the (0, 0) zero mode, ordinary EM in spacetime.
- **Single-axis modes** (m, 0), (0, n) — L2-in-L3 mass-only modes; structural neutrino-class candidates.

This is the geometric particle inventory of metric-charge under the standard closure rule. The downstream questions — which inventory members correspond to which observed particles, and how they organize into generations / families — are addressed in chapters 5–8 and in follow-up MaSt-correspondence work.

### 7. What's next

[Chapter 5 — Metric self-consistency and gauge promotion](05-metric-self-consistency.md). The closure-satisfying modes from this chapter source off-diagonal metric entries (per metric-mass Chapter 5) that form valid Kaluza-Klein gauge potentials A_μ and B_μ. Closure-failing modes (single-axis, zero mode) source off-diagonals that don't satisfy gauge structure and stay internal — confirming the L2-in-L3 framing for single-axis modes as structural neutrino-class candidates. Chapter 5 develops the metric-side equivalence and shows the three views of Chapter 1 §10 are mutually consistent.

---

## What this chapter does **not** do

- **Does not derive numerical α.** Cited from grid-duality §8 (structural location at L3) and future grid alpha-derivation work (numerical value).
- **Does not develop the metric-side picture.** That is chapter 5's job.
- **Does not assign handedness / matter-antimatter signs** within the satisfying inventory. Chapter 6.
- **Does not vary aspect ratio ε.** Chapter 7.
- **Does not derive fractional charge from multi-component links.** Chapter 8 takes the link structure identified here and works through the energetics.
- **Does not analyze multi-knot energetics or bound states** beyond the closure-rule variant 5.3 mention. metric-binding territory.
- **Does not commit to MaSt-correspondence assignments.** The MaSt-analog column in §4.4 is exploratory; rigorous correspondence is downstream work.

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Does the centered standing-wave alignment uniquely characterize closure-satisfaction, or are there shifted variants that also satisfy? | Chapter 5 (gauge structure constrains alignment) |
| Are closure-rule variants 5.1 (u-instead-of-w) and the standard rule physically distinct, or unified at a deeper level? | Chapter 5 / grid alpha-derivation |
| Does closure-rule variant 5.3 (multi-knot collective) describe atoms or other composite bound states? | metric-binding |
| Do crossing-number tiers (T(2, 3) → T(2, 5) → T(3, 4) → ...) organize particle generations? | Chapter 7 + downstream MaSt-correspondence |
| Why is the closure condition asymmetric in (u, w) — is it a convention or derivable? | Chapter 5 (gauge convention) + grid alpha-derivation |
| Is the unknot/genuine-knot distinction physically meaningful, or are weak-knot diagonal modes (T(1, q)) and genuine torus knots equally valid charged particles? | Chapter 7 (aspect-ratio dependence) |
