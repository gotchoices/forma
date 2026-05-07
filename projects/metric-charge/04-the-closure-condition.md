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

[Chapter 1 §10](01-foundation.md) introduced the closure condition as an axiom in synchronization form. We restate it here precisely so the rest of the chapter has a clean target.

> **Closure condition (synchronization).** A wave configuration on the 2D sheet promotes a (massive) mode to a charged-state mode when, during a single closed traversal of T(m, n), every time the tube-direction phase crosses zero, the ring-direction phase also crosses zero.
>
> Operationally: parametrize the traversal by s ∈ [0, 1] with u(s) = m·s·L_u and w(s) = n·s·L_w. The tube crosses zero (modulo L_u) at s = j/m for j = 0, 1, ..., m. At each such s, the ring is at w(s) = n·j/m·L_w. For the ring to also cross zero (modulo L_w) at every such s, we need n·j/m to be an integer for every j ∈ {0, 1, ..., m}.
>
> **This holds iff m divides n (m | n), with both m and n nonzero.**

Two equivalent formulations:

**Phase-pattern view (the box above).** Direct geometric statement of the synchronization requirement.

**Topological view.** The synchronization condition has a clean topological reformulation. With m | n, write n = c·m for some positive integer c. Then T(m, n) = T(m, c·m) has gcd(m, n) = m and decomposes into **m disjoint copies** of the primitive T(1, c). So:

> *Closure-satisfying configurations are exactly the T(1, q) primitives and their k-component repetitions k × T(1, q).*

The two views are mathematically equivalent — both reduce to "m | n with both nonzero." The closure-satisfying inventory consists entirely of T(1, q) primitives and their multi-component repetitions; nothing else.

**Metric-side view** is developed in chapter 5. Whether the metric-side description (off-diagonals form valid Kaluza-Klein gauge potentials) is *equivalent to* synchronization or only *implied by* it is a question chapter 5 examines. If equivalent, the framework has three mutually consistent views; if the metric-side is broader, then synchronization-failing modes (genuine torus knots) might source locally-valid gauge potentials that nevertheless fail to combine into observable EM. Chapter 5 settles which.

This chapter operates **primarily on the phase-pattern / topological views** (which are equivalent for the operational rule m | n). The metric-side question is forwarded to chapter 5.

---

## 2. The closure-satisfying inventory

The synchronization condition is a single atomic requirement: m | n with both nonzero. Earlier chapters distinguished "eligibility" (a topological prerequisite) from "satisfaction" (a phase requirement); under the precise synchronization rule, the two collapse into one condition that's checkable per (m, n) pair.

The closure-satisfying inventory at the linearized wave-equation level:

| (m, n) form | Topology in 3-space | Closure status |
|---|---|---|
| Light (0, 0) | No curve | Trivially fails (no winding) |
| Single-axis (m, 0) or (0, n) | Unknot (one cycle wrapped) | Fails (one winding zero) |
| T(1, q) for q ≥ 1 (and the equivalent T(p, 1)) | Unknot in 3-space | **Satisfies** — m = 1 trivially divides any n |
| Genuine torus knot T(p, q), p, q ≥ 2, gcd(p, q) = 1 | Genuine torus knot in 3-space | **Fails** — m ∤ n under the synchronization rule |
| Multi-component link T(k, k·q) for k ≥ 2, q ≥ 1 | k-component link with primitive T(1, q) | **Satisfies** — m = k divides n = k·q |
| Multi-component link T(k·m', k·n') with gcd(m', n') = 1 and m' ≥ 2 | k-component link with primitive a genuine torus knot | **Fails** — primitive is itself synchronization-failing |

Two structural observations follow.

**(a) The closure-satisfying inventory is built from T(1, q) primitives.** Every closure-satisfying configuration is either a single T(1, q) primitive or a k-component repetition k × T(1, q). Genuine torus knots and their multi-component counterparts never satisfy closure. The framework's prediction: charged matter is built from T(1, q) primitives, period.

**(b) Genuine torus knots are a *third* mass-only category.** Single-axis modes fail closure because one winding is zero. Genuine torus knots (with both ≥ 2, gcd = 1) fail closure because the windings don't synchronize. These are two structurally distinct mass-only mechanisms, alongside the cancellation neutrality of [Chapter 6 §4](README.md#chapters). All three produce massive but EM-neutral states; the framework distinguishes them.

The synchronization rule is **operationally precise**: any (m, n) can be checked. There is no separate "phase alignment" requirement to derive — the geometric synchronization requirement is the rule, and m | n is its mathematical statement.

---

## 3. Synchronization at the wave level

The synchronization rule has a natural reading at the level of the separable wave-equation modes from [Chapter 2 §2](02-modes-on-a-sheet.md). For a mode at (m, n):

<!-- φ(t, u, w) = T(t) · U(u) · W(w) -->
$$
\varphi(t, u, w) = T(t)\cdot U(u) \cdot W(w)
$$

with U(u) ∝ cos(2π m u/L_u) and W(w) ∝ cos(2π n w/L_w) (or the analogous sin / complex-exponential basis).

Along the closed curve T(m, n) parametrized by s ∈ [0, 1], the wave's spatial pattern on the curve is:

<!-- φ_curve(s) ∝ cos(2π m² s) · cos(2π n m s · n/n) — show synchronization explicitly -->
$$
\varphi(\text{curve}; s) \;\propto\; \cos\!\left(2\pi\,m\,(m\,s)\right) \cdot \cos\!\left(2\pi\,n\,(n\,s)\right) = \cos(2\pi\,m^2\,s)\cdot\cos(2\pi\,n^2\,s)
$$

(Here m and n appear in the *winding* direction of the parametrization, so u(s) = m·s·L_u contributes a factor cos(2π m · m s) = cos(2π m² s), and similarly for w.)

The product traces a pattern with mn-related node structure. The closure-relevant question: at the s-values where U has a zero, does W also have a zero?

U(u(s)) = 0 when 2π m² s = π/2 + k·π for integer k, i.e., when m² s = (2k+1)/4. *Tube zero crossings of the carrier wave* on the curve happen at these s-values.

For W to simultaneously be zero, we need 2π n² s = π/2 + l·π for some integer l, i.e., n² s = (2l+1)/4 with the same s.

Solving for the rational s = (2k+1)/(4m²) to also satisfy n² s = (2l+1)/4: requires n² · (2k+1)/(4m²) = (2l+1)/4, i.e., **n²(2k+1) / m² = 2l+1**. This is satisfiable for integer l iff m² divides n² for all k — equivalently, **m | n**.

So the wave-level synchronization analysis gives the same condition as the geometric tube/ring-zero-crossing analysis from §1: **m | n**. The two analyses agree.

For an alternative wave basis (sin instead of cos, or a phase-shifted cos), the condition is the same — synchronization is a property of the wave's *winding* on the curve, not of any specific phase choice. There is no "centered alignment" requirement separate from m | n; the synchronization rule itself does not pick out a sub-(m, n) phase parameter.

This collapses what was previously a two-step "eligibility plus satisfaction" framing into a single atomic condition. Whether m | n holds depends only on the integer pair (m, n), not on continuous phase parameters.

---

## 4. Which (m, n) satisfy closure under synchronization

Walk through the configurations from [Chapter 3 §7](03-knots-on-the-torus.md), checking each against m | n.

### 4.1 T(1, q) primitives — closure-satisfying

Modes with m = 1 (or by convention symmetry the equivalent m = n form with the roles relabeled). Topologically, all such curves are the **unknot** in 3-space. Under synchronization: **m = 1 trivially divides any n**, so closure is satisfied for every q.

Notable members:

- **(1, 2)**: a closure-satisfying T(1, 2) primitive. MaSt model-F has independently proposed identifying this mode with what standard physics calls the electron. The metric-charge framework here treats that proposal as a candidate correspondence — a reference target to compare results against — not an axiomatic input. The framework does not commit to a specific spin-derivation for this mode; observed pattern is that the 2-torus substrate appears to carry spin-1/2-like structure (per [Chapter 3 §5](03-knots-on-the-torus.md)), with the geometric derivation of spin from substrate dimensionality left as open work. Whether the framework's predictions for this mode match what standard physics calls "the electron" under detailed property comparison is downstream MaSt-correspondence work.
- **(1, 3), (1, 4), ...**: closure-satisfying primitives with progressively larger n. Heavier than (1, 2) by the rest-mass formula of [Chapter 2 §3](02-modes-on-a-sheet.md). Candidate states that *might* correspond to what standard physics calls further-generation leptons; the identification is open.

These are the framework's primitive charged states. Every closure-satisfying configuration is built from T(1, q) primitives — either as a singleton (this section) or as a multi-component repetition (§4.3).

### 4.2 Genuine torus knots T(p, q), p, q ≥ 2, gcd(p, q) = 1 — closure-failing

Modes with both windings at least 2 and no common factor. Topologically these are genuine torus knots in 3-space, with non-trivial crossing number.

Under synchronization: **m = p does not divide n = q** (since gcd(p, q) = 1 and p ≥ 2 forces p ∤ q). So **closure fails** for every genuine torus knot.

Examples:

- **(2, 3) trefoil**: 2 ∤ 3, fails. The trefoil is mass-only.
- **(2, 5) cinquefoil**: 2 ∤ 5, fails. Mass-only.
- **(3, 4)**: 3 ∤ 4, fails. Mass-only.
- **(3, 5), (2, 7), (3, 7), (4, 5), ...**: all genuine torus knots fail synchronization. Mass-only.

Genuine torus knots are a **third category of mass-only modes**, structurally distinct from single-axis (which fail by missing a winding) and from cancellation pairs (which fail by internal sign-cancellation, [Chapter 6 §4](06-handedness-and-pairs.md)). These modes have both windings nonzero but don't synchronize — the off-diagonals they source under linearized Einstein equations may form locally-coherent gauge-potential patterns (the chapter-5 metric-side analysis examines this) but the configuration as a whole does not produce observable EM coupling.

This is a substantive framework prediction: **the entire genuine-torus-knot tower** (T(2, 3), T(2, 5), T(3, 4), T(3, 5), T(2, 7), ...) **carries mass but no charge.** Whether any of these correspond to standard physics' neutral massive states (neutrinos, neutral mesons, dark-matter candidates, the Higgs) is downstream MaSt-correspondence work. The framework provides multiple structural-neutrality mechanisms; standard physics has multiple categories of neutral massive states; how they map is open.

### 4.3 Multi-component links — closure-satisfying iff primitive is T(1, q)

Multi-component links T(k·m', k·n') decompose into k disjoint copies of the primitive T(m', n') with gcd(m', n') = 1. Two cases:

**4.3a Closure-satisfying: T(k, k·q) = k × T(1, q).** When the primitive is T(1, q) — i.e., m' = 1 — the multi-link has total winding (k, k·q) with m = k dividing n = k·q. Synchronization is satisfied.

These are the framework's **multi-link charged states**: k phased copies of a T(1, q) primitive, with each component carrying 1/k of the link's total charge (per the closure-rule analysis here, with the integer-quantization consistency argued in chapter 8).

Examples:

- **(3, 6) = 3 × T(1, 2)**: three phased copies of the (1, 2) primitive. Each component carries 1/3 of the primitive's charge. Candidate identification with what standard physics calls a quark — specifically, a flavor family proportional to model-F's proposed (1, 2) ↔ electron correspondence.
- **(2, 4) = 2 × T(1, 2)**: two phased copies of (1, 2). Each carries 1/2 of the primitive's charge. No obvious standard-physics counterpart; whether such states are stable or transient is a chapter 8 question.
- **(3, 9) = 3 × T(1, 3)**: three phased copies of the heavier (1, 3) primitive.

**4.3b Closure-failing: k × T(p, q) with primitive a genuine torus knot.** When the primitive is a genuine torus knot (p, q ≥ 2, gcd = 1), the multi-link has total winding (k·p, k·q) with m = k·p and n = k·q. Synchronization requires m | n, i.e., k·p | k·q, i.e., p | q — but gcd(p, q) = 1 and p ≥ 2 means p ∤ q. So synchronization **fails**.

Example: T(4, 6) = 2 × T(2, 3). Two phased copies of the trefoil. The link inherits the trefoil's synchronization-failure: 4 ∤ 6 (since 6/4 = 1.5). Mass-only.

So every multi-link configuration is closure-satisfying iff its primitive is T(1, q). Multi-links with genuine-torus-knot primitives are mass-only, in the same category as single genuine torus knots from §4.2.

### 4.4 Summary table

The full inventory at the linearized wave-equation level:

| (m, n) form | Closure | Charge per component | External-identification proposals (model-F, exploratory) |
|---|---|---|---|
| Light (0, 0) | Fails | — | photon |
| Single-axis (m, 0), (0, n) | Fails (one winding zero) | — | candidate neutral massive state |
| T(1, 2) primitive | ✓ | 1 | candidate electron (MaSt model-F reference target) |
| T(1, 3), T(1, 4), … primitives | ✓ | 1 | candidate further leptons; not yet specifically proposed |
| Genuine torus knot T(2, 3), T(2, 5), T(3, 4), … | **Fails (synchronization)** | — | candidate neutral massive state — distinct from single-axis category |
| Multi-link T(k, k·q) = k × T(1, q), k ≥ 2 | ✓ (k-fold) | 1/k | candidate quark (k = 3, q = 2) and other multi-link states |
| Multi-link with genuine-knot primitive | **Fails (synchronization)** | — | candidate neutral massive state — synchronization-failure category |

The external-identifications column is **exploratory and not an input to this project's derivations**. Chapter 4 establishes only the closure-satisfaction structure; whether each predicted state corresponds to a particle in the standard-physics inventory requires:

- Aspect-ratio analysis (chapter 7) to determine which (m, n) values are stable on the sheet.
- Shear analysis (chapter 8) to determine which multi-component links are favored under shear.
- Multi-knot energetics (metric-binding) to determine binding and composition.
- MaSt-correspondence work (downstream) to compare metric-charge's inventory against standard-physics inventory.

The framework's job in this chapter is to **derive the inventory of states the closure condition produces**. Identification is a comparison task that happens *after* the framework has predicted its own properties.

**Note on category richness.** The framework now has *three* mass-only categories (single-axis, genuine-torus-knot, cancellation-pair) and *two* charge-carrying categories (T(1, q) primitives, T(k, k·q) multi-links). Standard physics has multiple categories of charged particles (leptons, quarks, charged hadrons) and multiple categories of neutral massive states (neutrinos, neutral mesons, dark matter candidates, Higgs). The structural-shape correspondence is suggestive — the framework may have richer structural distinctions than a simpler "charged vs neutral" partition — but quantitative correspondence is downstream work.

---

## 5. Closure-rule variants

[Chapter 1 §10](01-foundation.md) flagged three open variants of the closure rule. Each gives a different particle inventory; examining each here helps identify what the standard rule actually buys us.

### 5.1 Variant — synchronization with cycles swapped

The standard rule treats w as tube (the direction whose synchronization defines closure). The mirror variant treats u as tube: closure requires **n | m** instead of m | n.

**Topologically** this gives the same set of particles modulo cycle-swap: T(p, q) under "n | m" is the same as T(q, p) under "m | n." But the two are physically distinct in metric-charge per [Chapter 3 §3.2](03-knots-on-the-torus.md), since the (u, w) ↔ (w, u) symmetry is broken by the wrap-order convention adopted in [Chapter 1 §10](01-foundation.md) and the downstream conventions that inherit from it.

The variant is the alternative wrap-order convention. As discussed in Ch 1 §10, whether the convention's match to observation is genuine or is itself a labeling choice the math fixes for self-consistency is open work for [grid-duality §8](../grid-duality/08-where-alpha-appears.md).

### 5.2 Variant — single-axis closure

A weaker rule: closure requires only that one specific winding be nonzero, without the synchronization condition. Equivalently: closure ≡ "n ≠ 0" alone.

Under this variant:

- **Single-axis modes (0, n)** would satisfy closure (one winding nonzero, no synchronization needed).
- **All other modes with n ≠ 0** would also satisfy.
- **Modes with n = 0** (light, single-axis (m, 0)) would fail.

Implication: the framework's structural-neutrality category for single-axis modes disappears partially — (0, n) would carry observable EM. This is inconsistent with the framework's prediction of structurally neutral mass-only modes. The variant is therefore likely incorrect; the synchronization rule's two-winding requirement is what produces the structural-neutrality category.

### 5.3 Variant — multi-knot collective synchronization

A different kind of variant: synchronization can be satisfied *collectively* by a configuration of multiple knots even when no single knot satisfies it. For example, a (1, 0) mode and a (0, 1) mode together have all the necessary windings collectively, even though neither single mode satisfies the closure condition individually.

Whether this collective form of closure is meaningful — and whether it would give the same physics as a single closure-satisfying mode — depends on the field-theoretic interactions between the components. At the linear level (this project's scope), modes superpose without interaction and the "collective closure" idea is not well-defined as a wave-equation concept.

The variant becomes meaningful in [metric-binding](../metric-binding/)'s territory, where multi-knot interactions are the explicit subject of analysis. As a candidate description of *bound states* like atoms — composite particles whose closure-like behavior derives from interactions between non-closure-satisfying components — this variant is forwarded to metric-binding for treatment.

The structural takeaway: variant 5.3 suggests a *second tier* of physical configurations beyond the single-mode inventory — composite structures built from interacting non-closure components. Standard physics' atomic / nuclear / hadronic bound states are candidates; whether the variant correctly describes any of them is a downstream MaSt-correspondence question.

---

## 6. The distinguished particle inventory

Under the synchronization closure rule, the predicted inventory partitions into two top-level categories: charged states and neutral massive states. The neutral category subdivides into three structurally distinct mechanisms.

### 6.1 Charged states (closure-satisfying)

- **T(1, q) primitives** — single charged particles built from the simplest closure-satisfying winding (m = 1 trivially divides any n). Topologically unknots in 3-space. (1, 2) is a candidate electron identification (MaSt model-F reference target); (1, 3), (1, 4), ... are candidate further generations.

- **Multi-link T(k, k·q) configurations = k × T(1, q)** — k phased copies of a T(1, q) primitive, with each component carrying 1/k of the link's total charge. (3, 6) = 3 × T(1, 2) at k = 3 is a candidate quark identification.

That's the entire charged inventory: T(1, q) primitives and their k-component repetitions. The framework predicts that **all charge-carrying configurations are built from T(1, q) primitives** — either as singletons or as multi-component links.

### 6.2 Neutral massive states (closure-failing) — three distinct mechanisms

- **Light** (the (0, 0) zero mode) — massless, no compact-direction structure, ordinary EM-field-quantum in spacetime.

- **Single-axis modes** (m, 0), (0, n) — fail closure because *one winding is zero*. The U(1) × U(1) cross-coupling structure is incomplete; one of the two compact-direction momenta is absent. Mass without observable EM by *structural* mechanism.

- **Genuine-torus-knot modes** T(p, q) with p, q ≥ 2 and gcd(p, q) = 1 — fail closure because the *windings don't synchronize*. Both compact-direction momenta are present, but tube and ring zero crossings don't coincide along the closed traversal. Mass without observable EM by *synchronization-failure* mechanism. Examples: trefoil T(2, 3), cinquefoil T(2, 5), T(3, 4), and the rest of the genuine-torus-knot tower.

- **Synchronization-failing multi-link modes** T(k·p, k·q) with primitive a genuine torus knot — the same synchronization-failure mechanism operating on multi-component links built from genuine-torus-knot primitives.

(A *fourth* neutrality mechanism — cancellation neutrality from opposite-handedness pairs in a single field — operates on top of these. See [Chapter 6 §4](06-handedness-and-pairs.md). The cancellation mechanism is independent of which (m, n) sector the components live in; it can produce additional neutral configurations from any closure-satisfying base.)

### 6.3 What this inventory says

The **geometric particle inventory of metric-charge** under synchronization closure has the following structural shape:

- A massless field (light / photon analog) — one category.
- Charged states built from T(1, q) primitives — singletons (candidate leptons) and multi-links (candidate quarks). Two charge-carrying sub-categories.
- Neutral massive states — at least three structurally distinct mechanisms (single-axis, synchronization-failure, cancellation pair). Possibly more.

Standard particle physics has multiple charge-carrying categories (charged leptons, quarks, charged hadrons-as-composites) and multiple neutral-massive categories (neutrinos in three flavors, neutral mesons, neutral baryons, dark matter candidates, the Higgs). The framework's category structure has the right *shape* to potentially map onto this, with the framework's *richer-than-binary* neutral structure suggesting multiple distinct neutral states rather than a single "neutrino" category.

**Whether the framework's categories correspond to standard physics' categories — at the level of specific particles or only at the structural-pattern level — is downstream MaSt-correspondence work that this project does not undertake.** The closure condition produces an inventory of the right shape; whether the map holds at the level of individual particle properties is open work.

A specific question worth flagging: **standard physics treats hadrons as composites** (3 quarks per baryon, 2 quarks for mesons), not as single fundamental particles. The framework's prediction that all *fundamental* charged states are T(1, q) primitives or k × T(1, q) multi-links — with no fundamental "hadron tier" of single torus knots — matches this composite-hadron view of standard physics better than the framework's earlier draft (which had a tower of single charged genuine torus knots as candidate hadrons). Hadrons in the framework would emerge as bound states of multiple T(k, k·q) multi-links — metric-binding's territory.

The downstream chapters develop:

- Chapter 5: the metric-side picture of off-diagonals sourced by closure-satisfying and closure-failing modes; consistency of the synchronization condition with the metric-side analysis.
- Chapter 6: handedness / matter-antimatter signs within the inventory, plus a fourth cancellation-neutrality mechanism.
- Chapter 7: how aspect ratio ε determines which (m, n) dominate at low energy.
- Chapter 8: how shear σ_uw favors specific k values for multi-link configurations — the optimization examines whether k = 3 emerges naturally.

---

## 7. What's next

[Chapter 5 — Metric self-consistency and gauge promotion](05-metric-self-consistency.md). The closure-satisfying modes from this chapter source off-diagonal metric entries (per metric-mass Chapter 5) that form valid Kaluza-Klein gauge potentials A_μ and B_μ. Closure-failing modes — both single-axis and synchronization-failing genuine torus knots — source off-diagonals too. Chapter 5's job is to determine whether the metric-side analysis confirms the synchronization rule by showing that off-diagonals from synchronization-failing modes do *not* form a valid gauge-potential pattern (in which case the three views are equivalent), or whether the metric-side picture is broader than synchronization (in which case genuine torus knots locally have valid gauge potentials but the configurations don't yield observable EM for some other reason). The chapter also provides the calculable mechanism for how mass bends spacetime and how charged matter creates EM fields, building on metric-mass Chapter 5 §6 and Chapter 6 §4.

---

## What this chapter does **not** do

- **Does not derive numerical α.** Cited from [grid-duality §8](../grid-duality/08-where-alpha-appears.md) (structural location at L3) and future grid alpha-derivation work (numerical value).
- **Does not develop the metric-side picture.** That is chapter 5's job — including whether the metric-side analysis is *equivalent to* synchronization or *broader than* it.
- **Does not assign handedness / matter-antimatter signs** within the satisfying inventory. Chapter 6.
- **Does not vary aspect ratio ε.** Chapter 7.
- **Does not optimize k for multi-component links.** Chapter 8 takes the multi-link structure identified here and works through the energetics under shear.
- **Does not analyze multi-knot energetics or bound states** beyond the closure-rule variant 5.3 mention. metric-binding territory.
- **Does not identify which standard-physics neutral states correspond to single-axis vs synchronization-failure mass-only categories.** Three structural mass-only mechanisms exist in the framework (single-axis, synchronization-failure, cancellation pair); their map to observed neutral-massive states (neutrinos, neutral mesons, dark matter, Higgs) is downstream MaSt-correspondence work.
- **Does not commit to MaSt-correspondence assignments.** The external-identifications column in §4.4 is exploratory; rigorous correspondence is downstream work.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Is the metric-side analysis (chapter 5) equivalent to synchronization, or is it broader (genuine torus knots have local gauge potentials that don't yield observable EM)? | Chapter 5 |
| Do the three structural mass-only mechanisms (single-axis, synchronization-failure, cancellation pair) correspond to distinct standard-physics neutral categories (neutrinos, neutral mesons, dark matter, etc.) or do some collapse together? | Downstream MaSt-correspondence work |
| Are closure-rule variants 5.1 (cycles-swapped) and the standard rule physically distinct, or are they the same physics with relabeled coordinates? | Chapter 5 / [grid-duality §8](../grid-duality/08-where-alpha-appears.md) |
| Does closure-rule variant 5.3 (multi-knot collective synchronization) describe atoms or other composite bound states? | metric-binding |
| What standard-physics state corresponds to the genuine-torus-knot tower of mass-only modes (T(2, 3), T(2, 5), T(3, 4), ...)? | Downstream MaSt-correspondence work |
| Why is the closure condition asymmetric in (u, w) — is it a convention or derivable? | Chapter 5 (gauge convention) + grid alpha-derivation |
| Does the metric-charge inventory of §6 quantitatively match observed masses and charges of standard-model particles? | Downstream MaSt-correspondence work |
