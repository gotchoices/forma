# Chapter 4 — The closure condition

This chapter takes the closure condition stated axiomatically in [Chapter 1 §10](01-foundation.md) and works through which (m, n) modes actually satisfy it. Chapter 2 identified the three mode classes (light, single-axis, diagonal); chapter 3 partitioned the diagonal class further (weak-knot, genuine-knot, multi-component link). This chapter takes the **eligible** modes (both windings nonzero) and asks: which actually fire the closure rule? It also examines variants of the closure condition and what particle inventory each variant would select.

**Inheritance.**

- *From [Chapter 1 §10](01-foundation.md):* the closure condition stated in three equivalent views (phase-pattern, topological, metric-side preview).
- *From [Chapter 2 §4](02-modes-on-a-sheet.md):* the three mode classes, with eligibility = both windings nonzero.
- *From [Chapter 3 §7](03-knots-on-the-torus.md):* the five-row partition (light, single-axis, weak-knot diagonal, genuine-knot diagonal, multi-component link).

**Distinctive job.** Distinguish *eligibility* from *satisfaction*. Determine which eligible (m, n) values actually satisfy the standing-wave alignment requirement. Examine alternative closure rules and the particle inventories each selects. Hand off to chapter 5 for the metric-side equivalent and to chapter 6 for handedness/chirality structure within the satisfying inventory.

The chapter is **structural rather than computational**: the math is mostly about phase patterns and counting which (m, n) admit closure, not about computing energies or charges quantitatively. Quantitative energetics live in chapter 5 (gauge potentials), chapter 7 (aspect ratio), and metric-binding (multi-knot interactions).

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The closure condition restated — three equivalent views |
| 2 | Eligibility versus satisfaction |
| 3 | The standing-wave alignment requirement |
| 4 | Which (m, n) satisfy closure under the standard rule |
| 5 | Closure-rule variants and what each selects |
| 6 | The distinguished particle inventory |
| 7 | What's next |

---

## 1. The closure condition restated

[Chapter 1 §10](01-foundation.md) introduced the closure condition as an axiom and presented three equivalent views of it. We restate them here so the rest of the chapter has a precise target.

> **Closure condition (phase-pattern view).** A wave configuration on the 2D sheet promotes its mass mode to a charge mode when, during a single closed traversal of its phase pattern, **both** of the following are satisfied:
>
> 1. The phase completes a full **2π winding on w**.
> 2. The phase completes a **complete standing wave** (full period — node-to-antinode-to-node) on **both u and w**.

Two other formulations are equivalent. Each becomes the "natural" framing in different downstream contexts.

**Topological view** (used as a structural cross-check throughout this chapter). Per [grid-duality §7.5](../grid-duality/07-wrap-promotion-modeling.md) and [§8](../grid-duality/08-where-alpha-appears.md), the L3 2-torus has fundamental group π₁(T²) = ℤ², and integer winding numbers (w_α, w_β) ∈ ℤ² are the conserved topological invariants. The U(1) × U(1) cross-coupling structure that supports α and observable EM requires both winding directions to be active simultaneously. Closure-failed configurations have at most one active winding direction and reduce to L2 (mass without charge) embedded in an L3 substrate.

**Metric-side view** (developed in chapter 5; previewed in [Chapter 1 §10](01-foundation.md)). metric-mass Chapter 5 established that mass sources off-diagonal metric entries g_tu via linearized Einstein equations. On a 2D sheet, this generalizes to a richer set including g_tw, g_S₁u, g_S₂u, g_S₁w, g_S₂w. Under the standard Kaluza-Klein identification, these off-diagonals are gauge potentials A_μ and B_μ. The closure condition, in this view, is the rule under which the off-diagonals sourced by a given mode actually form a *valid* gauge-potential pattern — consistent with the gauge structure that makes them observable as EM in 4D. Closure-failed modes source off-diagonals too, but in patterns that don't satisfy gauge structure and remain internal.

This chapter operates **primarily on the phase-pattern view**. The topological view is invoked when we need to confirm that the phase-pattern judgment is consistent with conservation of integer windings; the metric-side view is referenced but its derivation is chapter 5's job.

---

## 2. Eligibility versus satisfaction

The closure condition naturally separates into two distinct requirements that earlier chapters conflated. Distinguishing them cleanly is the structural backbone of this chapter.

**Eligibility — the topological prerequisite.** A mode is eligible for closure if both its winding numbers are nonzero: m ≠ 0 and n ≠ 0. From [chapter 2 §4](02-modes-on-a-sheet.md) and [chapter 3 §7](03-knots-on-the-torus.md):

| Mode | Eligibility |
|---|---|
| Light (0, 0) | Not eligible (no winding) |
| Single-axis (m, 0) or (0, n) | Not eligible (one winding zero) |
| Weak-knot diagonal T(1, q), T(p, 1) | **Eligible** (both windings nonzero, even though topological unknot) |
| Genuine torus knot T(p, q), p,q ≥ 2, gcd = 1 | **Eligible** |
| Multi-component link T(km, kn), gcd > 1 | **Eligible** |

Eligibility is a *necessary* condition for closure. It is also the structural reason single-axis modes are candidates for neutrino-class neutrality: they fail closure not just dynamically but *structurally* — the closure condition has no path to fire on a configuration with one winding zero.

**Satisfaction — the standing-wave alignment requirement.** An eligible mode *satisfies* closure if its standing-wave structure on u and w is properly aligned to lock during one closed traversal of T(m, n). This is the additional dynamical condition beyond eligibility, and §3 develops it precisely.

The chapter's central question becomes: **which eligible modes actually satisfy?** The hypothesis at outline stage — to be tested through this chapter — is that under the standard closure rule of Chapter 1 §10, **all eligible modes can satisfy closure for an appropriate sub-(m, n) phase choice**. The phase choice is what §3 must pin down.

---

## 3. The standing-wave alignment requirement

What does "complete standing wave on both u and w during one closed traversal" mean precisely?

For a separable solution of the wave equation, the field factorizes:

<!-- φ(t, u, w) = T(t) · U(u) · W(w) -->
$$
\varphi(t, u, w) = T(t)\cdot U(u) \cdot W(w)
$$

with T(t) the temporal factor, U(u) and W(w) standing waves in their respective compact directions. For a (m, n) mode with both nonzero, we can write:

<!-- U(u) = A_u cos(2π m u/L_u + φ_u),  W(w) = A_w cos(2π n w/L_w + φ_w) -->
$$
U(u) = A_u\cos\!\left(\frac{2\pi m\,u}{L_u} + \phi_u\right),\qquad W(w) = A_w\cos\!\left(\frac{2\pi n\,w}{L_w} + \phi_w\right)
$$

The integer winding numbers m and n are fixed by the periodicity boundary conditions ([Chapter 2 §2](02-modes-on-a-sheet.md)). The phases φ_u and φ_w are *free continuous parameters* — sub-(m, n) labels that do not affect topology but can affect closure satisfaction.

### What "closed traversal" means

A torus knot T(m, n) is a closed curve on the (u, w) torus that wraps m times around the u-cycle and n times around the w-cycle before closing on itself. Parametrize the curve by s ∈ [0, 1]:

<!-- u(s) = m · s · L_u (mod L_u),  w(s) = n · s · L_w (mod L_w) -->
$$
u(s) = m\,s\,L_u \pmod{L_u}, \qquad w(s) = n\,s\,L_w \pmod{L_w}
$$

As s advances from 0 to 1, the curve wraps m times around u (u(s) cycles through L_u m times) and n times around w. At s = 1, the curve closes upon itself.

### The alignment requirement

Along the curve, U(u) and W(w) cycle through their standing-wave patterns:

- U(u(s)) cycles through m periods of cos(·) as s goes from 0 to 1.
- W(w(s)) cycles through n periods of cos(·) as s goes from 0 to 1.

Together, the product U(u(s)) · W(w(s)) is a function of s that has mn nodes/antinodes structure. The closure condition's "node-to-antinode-to-node" requirement on both u and w means: at each point of the closed traversal, the phases of U and W are consistent — they trace out a pattern that closes on itself in lockstep.

The alignment locks when:

<!-- φ_u + φ_w = 0 (mod π) -->
$$
\phi_u + \phi_w \;=\; 0 \pmod{\pi}
$$

This is the **centered alignment**. The phases are antinodal-to-antinodal; nodes coincide; the standing-wave product on T(m, n) traces a clean closed pattern. Any other choice of (φ_u, φ_w) corresponds to a *shifted alignment* where the closure pattern is offset.

### Centered vs shifted alignment

For the standard closure rule of Chapter 1 §10:

- **Centered alignment** (φ_u + φ_w = 0 mod π): closure satisfied. The mode produces a valid charged state.
- **Shifted alignment** (other phase choices): closure pattern does not lock. The mode is eligible (both windings nonzero) but does not fire closure. Chapter 5's metric-side picture will show that shifted alignments source off-diagonals that *don't* form a valid gauge potential — confirming the phase-pattern judgment from the metric side.

The sub-(m, n) phase label introduced in [Chapter 3 §4.3](03-knots-on-the-torus.md) is exactly this (φ_u + φ_w mod π) value. It is not a topological invariant — two modes with the same (m, n) but different phases trace the same knot type T(m, n) — but it determines closure satisfaction.

In practice, the wave equation does not pick a preferred phase; the choice is set by the field's preparation (initial conditions). The framework's claim is that *centered alignment is what produces observable EM in 4D*; other alignments produce internal modes that don't couple to spacetime EM and behave like additional mass-only states.

---

## 4. Which (m, n) satisfy closure (under the standard rule)

Walk through the three eligible classes from [Chapter 3 §7](03-knots-on-the-torus.md), determining which (m, n) values within each class satisfy closure at centered alignment.

### 4.1 Weak-knot diagonal — T(1, q) and T(p, 1) with both nonzero

This class consists of modes where one winding is exactly 1 and the other is any nonzero integer. Topologically, all such curves are the **unknot** in 3-space. But the modes are physically distinct — different (m, n), different masses, different compact-direction momenta.

For closure under the standard rule:

- **(1, q) with q ≠ 0:** m = 1, n = q. Both nonzero. Standing waves on both u (m = 1 period) and w (q periods). Closure: **satisfied** at centered alignment.
- **(p, 1) with p ≠ 0:** m = p, n = 1. Same analysis with cycles swapped. Closure: **satisfied** at centered alignment.

Notable members:

- **(1, 2)**: a closure-eligible weak-knot diagonal mode. MaSt model-F (per [matter-from-light §4](../../papers/matter-from-light.md)) has independently proposed identifying this mode with what standard physics calls the electron, via the geometric derivation of spin-1/2 from the 1:2 winding ratio: ℓ = E/ω = ℏ/2. The framework here treats that proposal as a candidate correspondence — a reference target to compare results against — not an axiomatic input. The mode itself is a topologically trivial unknot with conserved (m, n) = (1, 2) labels; whether the framework's predictions for this mode (mass, charge, spin, magnetic moment, ...) match what standard physics calls "the electron" under detailed property comparison is downstream MaSt-correspondence work.
- **(1, 3), (1, 4), ...**: closure-eligible weak-knot modes with progressively larger n. Heavier than (1, 2) by the rest-mass formula of [Chapter 2 §3](02-modes-on-a-sheet.md). Candidate states that *might* correspond to what standard physics calls further-generation leptons; the identification is open.
- **(2, 1), (3, 1), ...**: cycle-swapped versions. Topologically equivalent to the above (T(p, q) ≡ T(q, p)) but physically distinct in metric-charge per [Chapter 3 §3.2](03-knots-on-the-torus.md) — different (m, n) labels, conserved as different sectors. Whether they correspond to the same particles as their (1, q) counterparts is a chapter 5 / convention question.

### 4.2 Genuine-knot diagonal — T(p, q) with p, q ≥ 2, gcd(p, q) = 1

This class consists of modes where both windings are at least 2 and share no common factor. Topologically these are **genuine torus knots** in 3-space, with non-trivial crossing number.

For closure under the standard rule:

- All such (p, q) have m = p ≠ 0 and n = q ≠ 0. Standing waves on both directions cycle through p and q periods respectively during traversal.
- Closure: **satisfied** at centered alignment.

Notable members:

- **(2, 3) trefoil**: simplest genuine torus knot, crossing number 3.
- **(2, 5) cinquefoil**: c = 5.
- **(3, 4)**: c = 8.
- **(3, 5)**: c = 10.
- **(2, 7), (3, 7), (4, 5), ...**: increasingly complex genuine torus knots.

The candidate organization here is **crossing-number tiers**. Each tier is a class of torus knots at a fixed range of crossing numbers; particles in the inventory might organize by tier. Whether tier-organized states correspond to what standard physics calls particle generations is a question for chapter 7 (where aspect-ratio dependence selects which (m, n) dominate) and downstream MaSt-correspondence work. MaSt model-F has not yet proposed specific identifications for the genuine-knot diagonal class.

### 4.3 Multi-component link — T(km, kn) with gcd(m, n) = 1, k > 1

This class consists of modes whose winding numbers share a common factor k > 1. Topologically, T(km, kn) is **k disjoint copies** of the primitive T(m, n), arranged as a k-component link with each component shifted by 1/k of a cycle.

For closure under the standard rule:

- Each component has (km, kn) windings and is a phased copy of T(m, n).
- The full configuration consists of all k components together.
- Closure: **satisfied collectively**, with k-fold phase distribution along the shared cycle.

The closure-rule analysis on multi-component links is the substrate for **chapter 8's fractional-charge mechanism**. k phased copies of the same primitive knot produce a configuration where each phase slot carries 1/k of the primitive's charge. This is the structural origin of quark-like fractional charge on a single sheet.

Notable members:

- **(3, 6) = 3 × (1, 2)**: three phased copies of the (1, 2) primitive. Each component carries 1/3 of the primitive's charge. Candidate identification with what standard physics calls a quark — specifically, the down-flavor family, if MaSt model-F's proposed (1, 2) ↔ electron correspondence holds.
- **(2, 4) = 2 × (1, 2)**: two phased copies of (1, 2). Each carries 1/2 the primitive's charge. No clear standard-physics counterpart; whether such states are stable or transient is a chapter 8 question.
- **(4, 6) = 2 × (2, 3)**: two phased copies of the trefoil. Each carries 1/2 the trefoil's charge. Standard-physics correspondence open.

### 4.4 Summary table

The predicted charged-state inventory under the standard closure rule:

| Class | (m, n) example | Closure | Charge per component | External-identification proposals (model-F, exploratory) |
|---|---|---|---|---|
| Weak-knot diagonal | (1, 2) | ✓ | 1 | candidate electron (model-F per matter-from-light §4) |
| Weak-knot diagonal | (1, 3), (1, 4), … | ✓ | 1 | candidate further leptons; not yet specifically proposed |
| Genuine-knot diagonal | (2, 3) | ✓ | 1 | candidate hadronic state; no specific model-F proposal |
| Genuine-knot diagonal | (2, 5), (3, 4), … | ✓ | 1 | candidate heavier hadrons; no specific model-F proposal |
| Multi-component link | (3, 6) = 3 × (1, 2) | ✓ (3-fold) | 1/3 | candidate quark (down-flavor family if (1, 2) ↔ electron holds) |
| Multi-component link | (2, 4) = 2 × (1, 2) | ✓ (2-fold) | 1/2 | no clear standard-physics counterpart |

The external-identifications column is **exploratory and not an input to this project's derivations**. Chapter 4 establishes only that closure is satisfied; whether each predicted state corresponds to a particle in the standard-physics inventory requires:

- Aspect-ratio analysis (chapter 7) to determine which (m, n) values are stable on the sheet.
- Shear analysis (chapter 8) to determine which multi-component links produce three-phase structure.
- Multi-knot energetics (metric-binding) to determine binding and composition.
- MaSt-correspondence work (downstream) to compare metric-charge's inventory against MaSt model-F's identifications and against the standard-physics inventory.

The framework's job in this chapter is to **derive the inventory of states the closure condition produces**, not to assert which standard-physics particles those states correspond to. Identification is a comparison task that happens *after* the framework has predicted its own properties for each state.

---

## 5. Closure-rule variants

[Chapter 1 §10](01-foundation.md) flagged three open variants of the closure rule. Each gives a different particle inventory; examining each here helps identify what the standard rule actually buys us.

### 5.1 Variant — 2π winding on u instead of w

The standard rule singles out w as the direction whose 2π winding is required. The mirror version singles out u: closure requires 2π winding on u, with standing waves on both u and w.

**Topologically**, this gives the same particles as the standard rule — T(p, q) ≡ T(q, p) per [Chapter 3 §3.2](03-knots-on-the-torus.md). At the abstract knot level, the variant and the standard rule are equivalent.

**Physically**, the variant gives a *different* sub-family in metric-charge. The four conventions of [Chapter 3 §3.2](03-knots-on-the-torus.md) (closure asymmetry, aspect-ratio convention, shear, gauge convention) break the (u, w) ↔ (w, u) symmetry, so the variant's inventory is not metric-equivalent to the standard rule's.

Whether u and w roles are unified at a deeper level — making the two variants physically indistinguishable — is a chapter 5 / [grid-duality §8](../grid-duality/08-where-alpha-appears.md) question. At present, the framework treats them as distinct conventional choices that lead to mirror-image physics.

### 5.2 Variant — standing wave on only one direction

A weaker rule: closure requires only a *complete standing wave on one direction* (say w), without requiring it on the other. The 2π-winding-on-w requirement is preserved.

Under this variant:

- **Single-axis modes (0, n)** would satisfy closure: they have standing waves on w (n periods) and 2π winding on w; the absence of standing wave on u is no longer disqualifying.
- **All eligible diagonal modes** continue to satisfy.

Implication: the **L2-in-L3 structural neutrino-class candidate disappears**. Single-axis modes would carry observable charge under this rule. This is inconsistent with the framework's commitment to neutrino-class neutrality being a structural feature of single-axis modes.

The variant is therefore likely **incorrect as a model of observable physics**. Including it as a candidate at all is just a sanity check: the standard rule's requirement of standing waves on *both* directions is what makes single-axis modes structurally neutral. Without that requirement, the structural neutrality story collapses.

### 5.3 Variant — multi-knot collective closure

A different kind of variant: closure can be satisfied *collectively* by a configuration of multiple knots even when no single knot satisfies it. For example, a (1, 0) mode and a (0, 1) mode together cover both windings, even though neither single mode does.

This variant is not the closure rule of Chapter 1 §10, but it is structurally interesting:

- Two single-axis modes — each individually neutrino-class on its own — that collectively become charge-carrying when paired.
- The pair would have observable EM signatures even though each individual mode is internal.
- This is a candidate description of **bound states** like atoms — composite particles whose closure derives from the collective wrapping rather than from any individual constituent.

Variant 5.3 connects directly to [metric-binding](../metric-binding/)'s bound-state regimen. Chapter 5 of metric-charge will not pursue it (its job is the gauge-promotion analysis for individual mode closure); it is forwarded to metric-binding for full treatment.

The structural takeaway: variant 5.3 suggests a *second tier* of physical particles beyond the single-mode inventory — composites built from collectively-closing combinations of L2-in-L3 single-axis modes. Whether this corresponds to observed atomic / nuclear / hadronic bound states is a downstream MaSt-correspondence question.

---

## 6. The distinguished particle inventory

Under the standard closure rule of Chapter 1 §10, the predicted inventory partitions into two: charged states and neutral states.

### 6.1 Charged states

- **Weak-knot diagonal modes** T(1, q), T(p, 1) — single charged particles with topological-unknot structure but nonzero windings in both directions. Electron candidate at T(1, 2); further leptons or heavier-generation particles at T(1, 3), T(1, 4), etc.

- **Genuine torus knots** T(p, q) with p, q ≥ 2 — heavier charged particles with non-trivial topology. Trefoil T(2, 3) and the tower above it. The framework predicts a tower of charged states organized by crossing-number tier; whether they correspond to what standard physics calls hadrons / proton-class particles or to particle generations is a downstream MaSt-correspondence question, not a determination of this chapter.

- **Multi-component links** T(km, kn) with gcd > 1 — fractional-charge configurations. Three-phase distribution of T(km, kn) = k × T(m, n) gives 1/k charge per component. Quark candidate at T(3, 6); other multi-link configurations may correspond to less-observed exotic states.

### 6.2 Neutral / non-observable states

- **Light** — the (0, 0) zero mode. Massless, no compact-direction structure, ordinary EM in spacetime.

- **Single-axis modes** (m, 0), (0, n) — L2-in-L3 mass-only modes. Carry rest mass m_(m,n) per [Chapter 2 §3](02-modes-on-a-sheet.md), but no observable EM. **Structural neutrino-class candidates**: their failure of closure is structural (one winding zero) and not a matter of phase or alignment. They exist as massive states without EM coupling — exactly the structural property required of a neutrino-class particle.

### 6.3 What this inventory says

This is the **geometric particle inventory of metric-charge** under the standard closure rule. It produces, structurally:

- A massless EM field (light, the zero mode).
- A class of unit-charge particles (weak-knot diagonal).
- A class of higher-tier charged particles (genuine torus knots).
- A class of fractional-charge particles (multi-component links).
- A class of neutral massive states (single-axis modes).

These five categories form a structural pattern. Standard particle physics also organizes its inventory into five categories — photons, charged leptons, charged hadrons, quarks, and neutrinos. **Whether the framework's categories correspond to standard physics' categories — at the level of specific particles or only at the structural-pattern level — is downstream MaSt-correspondence work that this project does not undertake.** The framework's closure condition produces an inventory of the right *shape* to potentially map onto standard physics' organization; whether the map holds at the level of individual particle properties (masses, charges, magnetic moments, decay rates, ...) is open and depends on quantitative analysis well beyond chapter 4's scope.

The downstream chapters develop:

- Chapter 5: the metric-side picture of the gauge potentials (or whatever the off-diagonals turn out to be) these modes source.
- Chapter 6: handedness / matter-antimatter sign assignments within the inventory.
- Chapter 7: how aspect ratio ε determines which (m, n) dominate — possibly accounting for what standard physics observes as extreme-aspect-ratio sheets (per MaSt model-F, e.g., the electron sheet's high ε).
- Chapter 8: how shear σ_uw selects k = 3 cleanly for the multi-component link mechanism, producing the three-phase structure that MaSt model-F (and standard-physics quark organization) might correspond to.

---

## 7. What's next

[Chapter 5 — Metric self-consistency and gauge promotion](05-metric-self-consistency.md). The closure-satisfying modes from this chapter source off-diagonal metric entries (per metric-mass Chapter 5) that form valid Kaluza-Klein gauge potentials A_μ and B_μ. Closure-failing modes (single-axis, zero mode) source off-diagonals too, but in patterns that don't satisfy gauge structure and stay internal — confirming the L2-in-L3 framing for single-axis modes as structural neutrino-class candidates. Chapter 5 develops the metric-side equivalence and shows the three views of [Chapter 1 §10](01-foundation.md) are mutually consistent. It also provides the calculable mechanism for how mass bends spacetime and how charged matter creates EM fields, building on metric-mass Chapter 5 §6 and Chapter 6 §4.

---

## What this chapter does **not** do

- **Does not derive numerical α.** Cited from [grid-duality §8](../grid-duality/08-where-alpha-appears.md) (structural location at L3) and future grid alpha-derivation work (numerical value).
- **Does not develop the metric-side picture.** That is chapter 5's job.
- **Does not assign handedness / matter-antimatter signs** within the satisfying inventory. Chapter 6.
- **Does not vary aspect ratio ε.** Chapter 7.
- **Does not derive fractional charge from multi-component links.** Chapter 8 takes the link structure identified here and works through the energetics.
- **Does not analyze multi-knot energetics or bound states** beyond the closure-rule variant 5.3 mention. metric-binding territory.
- **Does not commit to MaSt-correspondence assignments.** The MaSt-analog column in §4.4 is exploratory; rigorous correspondence is downstream work.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Does the centered standing-wave alignment uniquely characterize closure-satisfaction, or are there shifted variants that also satisfy? | Chapter 5 (gauge structure constrains alignment) |
| Are closure-rule variants 5.1 (u-instead-of-w) and the standard rule physically distinct, or unified at a deeper level? | Chapter 5 / [grid-duality §8](../grid-duality/08-where-alpha-appears.md) |
| Does closure-rule variant 5.3 (multi-knot collective) describe atoms or other composite bound states? | metric-binding |
| Do crossing-number tiers (T(2, 3) → T(2, 5) → T(3, 4) → ...) organize particle generations? | Chapter 7 + downstream MaSt-correspondence |
| Why is the closure condition asymmetric in (u, w) — is it a convention or derivable? | Chapter 5 (gauge convention) + grid alpha-derivation |
| Is the unknot/genuine-knot distinction physically meaningful, or are weak-knot diagonal modes (T(1, q)) and genuine torus knots equally valid charged particles? | Chapter 7 (aspect-ratio dependence) |
| Does the metric-charge inventory of §6 quantitatively match observed masses and charges of standard-model particles? | Downstream MaSt-correspondence work |
