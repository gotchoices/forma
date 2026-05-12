# Chapter 4 — The closure condition

This chapter takes the closure condition stated axiomatically in [Chapter 1 §10](01-foundation.md) and works through which (m, n) modes actually satisfy it. Chapter 2 identified the three mode classes (light, single-axis, diagonal); chapter 3 partitioned the diagonal class further (weak-knot, genuine-knot, multi-component link). This chapter takes the **eligible** modes (both windings nonzero) and asks: which actually fire the closure rule? It also examines variants of the closure condition and what particle inventory each variant would select.

**Inheritance.**

- *From [Chapter 1 §10](01-foundation.md):* the closure condition stated as a chirality criterion, with equivalent operational (synchronization), topological, and metric-side (chapter 5) formulations.
- *From [Chapter 2 §4](02-modes-on-a-sheet.md):* the three mode classes, with eligibility = both windings nonzero.
- *From [Chapter 3 §7](03-knots-on-the-torus.md):* the five-row partition (light, single-axis, weak-knot diagonal, genuine-knot diagonal, multi-component link).

**Distinctive job.** Walk through which (m, n) satisfy the closure rule under each of the three equivalent views (chirality, synchronization, topological), enumerate the closure-satisfying inventory, and examine alternative closure-rule variants. Hand off to chapter 5 for the metric-side derivation of the single gauge field and to chapter 6 for handedness / matter-antimatter structure.

The chapter is **structural rather than computational**: the math is mostly about which (m, n) admit closure, not about computing energies or charges quantitatively. Quantitative energetics live in chapter 5 (gauge potential), chapter 7 (aspect ratio), and metric-binding (multi-knot interactions).

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The closure condition restated — chirality, synchronization, topological, metric-side views |
| 2 | The closure-satisfying inventory |
| 3 | Synchronization at the wave level |
| 4 | Which (m, n) satisfy closure |
| 5 | Closure-rule variants and what each selects |
| 6 | The distinguished particle inventory |
| 7 | What's next |

---

## 1. The closure condition restated

[Chapter 1 §10](01-foundation.md) introduced the closure condition as an axiom in chirality form, with equivalent operational, topological, and metric-side formulations. We restate it here precisely so the rest of the chapter has a clean target.

### 1.1 Chirality view (primary)

> **Closure condition (chirality form).** A configuration T(m, n) is closure-satisfying — i.e., a (massive) mode also carries observable EM charge — if and only if:
>
> (i) the closed curve T(m, n) is **achiral** in 3-space — its chirality reflections are topological symmetries of the curve up to ambient isotopy — *and*
>
> (ii) the wrap-order's ring-direction reflection R_u (m ↔ −m) is among those topological symmetries.

The chirality view is the framework's *primary* explanation. It ties directly to chapter 5's derivation: under the wrap-order-asymmetric standing-wave construction, R_u (acting on the ring direction) is what produces the single surviving cross-term, and the chirality criterion is exactly the condition under which R_u can be enforced as a particle symmetry.

### 1.2 Synchronization view (operational test)

The chirality criterion has a clean operational test in terms of phase synchronization during closed-curve traversal:

> **Synchronization test.** Parametrize the traversal of T(m, n) by s ∈ [0, 1] with u(s) = m·s·L_u and w(s) = n·s·L_w. The tube phase crosses zero (modulo L_w) at s = j/n for j = 0, 1, ..., n. At each such s, the ring is at u(s) = (m·j/n)·L_u. For the ring to also cross zero (modulo L_u) at every such s, we need m·j/n to be an integer for every j.
>
> **This holds iff n divides m (n | m), with both m and n nonzero.**

The synchronization test selects the same set of (m, n) as the chirality criterion. It is operationally simpler — given a specific (m, n) integer pair, just check whether n | m — but the criterion's *meaning* is the chirality view.

### 1.3 Topological view

> **Topological form.** T(m, n) closure-satisfies iff its gcd-reduced primitive is **T(m', 1)** for some integer m' ≥ 1.

With n | m, write m = c·n for some positive integer c. Then T(m, n) = T(c·n, n) has gcd(m, n) = n and decomposes into **n disjoint copies** of the primitive T(c, 1). So:

> *Closure-satisfying configurations are exactly the T(m, 1) primitives and their k-component repetitions k × T(m, 1).*

The three views are mathematically equivalent. The closure-satisfying inventory consists entirely of T(m, 1) primitives and their multi-component repetitions; nothing else.

### 1.4 Metric-side view (chapter 5)

Chapter 5 develops the metric-side derivation: under the wrap-order-asymmetric standing-wave construction, closure-satisfying modes source one off-diagonal metric entry h_μw that forms a single Kaluza-Klein gauge potential B_μ, while closure-failing modes source no EM gauge potential. The metric-side view is **exactly equivalent** to the chirality criterion of §1.1 — both are descriptions of the same underlying fact: the curve's chirality status, which controls whether the wrap-order's R_u can be enforced as a particle symmetry.

The four views (chirality, synchronization, topological, metric-side) are all mutually consistent within the torus-knot family realizable on T². This chapter operates primarily on the chirality and synchronization views; chapter 5 carries the metric-side derivation.

---

## 2. The closure-satisfying inventory

The closure rule is a single atomic requirement at the operational level: n | m with both nonzero (equivalently, the chirality criterion (i)+(ii) of §1.1). The closure-satisfying inventory at the linearized wave-equation level:

| (m, n) form | Topology in 3-space | Closure status |
|---|---|---|
| Light (0, 0) | No curve | Trivially fails (no winding) |
| Single-axis (m, 0) or (0, n) | Unknot (one cycle wrapped) | Fails (one winding zero — no chirality structure to test) |
| T(m, 1) for m ≥ 1 | Unknot in 3-space | **Satisfies** — n = 1 trivially divides any m |
| Genuine torus knot T(p, q), p, q ≥ 2, gcd(p, q) = 1 | Genuine torus knot in 3-space | **Fails** — chirality criterion (i) fails (curve is chirally distinct from its mirror) |
| Multi-component link T(k·m', k) for k ≥ 2, m' ≥ 1 | k-component unlink with primitive T(m', 1) | **Satisfies** — n = k divides m = k·m' |
| Multi-component link T(k·p, k·q) with gcd(p, q) = 1 and p, q ≥ 2 | k-component link with primitive a genuine torus knot | **Fails** — primitive is itself closure-failing |

Two structural observations follow.

**(a) The closure-satisfying inventory is built from T(m, 1) primitives.** Every closure-satisfying configuration is either a single T(m, 1) primitive or a k-component repetition k × T(m, 1). Genuine torus knots and their multi-component counterparts never satisfy closure. The framework's prediction: charged matter is built from T(m, 1) primitives, period.

**(b) Genuine torus knots are a *separate* mass-only category from single-axis modes.** Single-axis modes fail closure because one winding is zero, leaving no chirality structure to test. Genuine torus knots fail closure because they are chirally distinct from their mirrors in 3-space — the achirality criterion (i) of §1.1 fails. These are two structurally distinct mass-only mechanisms, alongside the cancellation neutrality of [Chapter 6 §4](06-handedness-and-pairs.md). All three produce massive but EM-neutral states; the framework distinguishes them by mechanism.

The closure rule is **operationally precise**: any (m, n) can be checked against n | m. The chirality criterion is its structural meaning.

---

## 3. Synchronization at the wave level

The synchronization test (§1.2) has a natural reading at the level of the separable wave-equation modes from [Chapter 2 §2](02-modes-on-a-sheet.md). For a mode at (m, n):

<!-- φ(t, u, w) = T(t) · U(u) · W(w) -->
$$
\varphi(t, u, w) = T(t)\cdot U(u) \cdot W(w)
$$

with U(u) ∝ cos(2π m u/L_u) and W(w) ∝ cos(2π n w/L_w) (or the analogous sin / complex-exponential basis).

Along the closed curve T(m, n) parametrized by s ∈ [0, 1], the wave's spatial pattern on the curve is:

<!-- φ_curve(s) ∝ cos(2π m² s) · cos(2π n² s) -->
$$
\varphi(\text{curve}; s) \;\propto\; \cos\!\left(2\pi\,m\,(m\,s)\right) \cdot \cos\!\left(2\pi\,n\,(n\,s)\right) = \cos(2\pi\,m^2\,s)\cdot\cos(2\pi\,n^2\,s)
$$

(Here m and n appear in the *winding* direction of the parametrization, so u(s) = m·s·L_u contributes a factor cos(2π m · m s) = cos(2π m² s), and similarly for w.)

The closure-relevant question: at the s-values where the *tube* factor W has a zero, does the *ring* factor U also have a zero?

W(w(s)) = 0 when 2π n² s = π/2 + l·π for integer l, i.e., when n² s = (2l+1)/4. *Tube zero crossings of the carrier wave* on the curve happen at these s-values.

For U to simultaneously be zero, we need 2π m² s = π/2 + k·π for some integer k, i.e., m² s = (2k+1)/4 with the same s.

Solving for the rational s = (2l+1)/(4n²) to also satisfy m² s = (2k+1)/4: requires m²(2l+1) / n² = 2k+1, satisfiable for integer k iff n² divides m² for all l — equivalently, **n | m**.

So the wave-level synchronization analysis gives the same condition as the geometric tube/ring-zero-crossing analysis from §1.2: **n | m**. The two analyses agree.

For an alternative wave basis (sin instead of cos, or a phase-shifted cos), the condition is the same — synchronization is a property of the wave's *winding* on the curve, not of any specific phase choice. There is no "centered alignment" requirement separate from n | m; the synchronization test depends only on the integer pair (m, n), not on continuous phase parameters.

---

## 4. Which (m, n) satisfy closure

Walk through the configurations from [Chapter 3 §7](03-knots-on-the-torus.md), checking each against the chirality criterion (i)+(ii) of §1.1, with the synchronization test n | m as the operational equivalent.

### 4.1 T(m, 1) primitives — closure-satisfying

Modes with n = 1. Topologically, all such curves are the **unknot** in 3-space (per [Chapter 3 §2](03-knots-on-the-torus.md)). The unknot is *achiral* — isotopic to its mirror image — so criterion (i) of §1.1 holds. The wrap-order's R_u is among its topological symmetries, so criterion (ii) holds automatically. Operationally: **n = 1 trivially divides any m**.

Notable members:

- **T(2, 1)**: a closure-satisfying primitive. MaSt model-F has independently proposed identifying this mode with what standard physics calls the electron. The metric-charge framework here treats that proposal as a candidate correspondence — a reference target to compare results against — not an axiomatic input. The framework does not commit to a specific spin-derivation for this mode; observed pattern is that the 2-torus substrate appears to carry spin-1/2-like structure (per [Chapter 3 §5](03-knots-on-the-torus.md)), with the geometric derivation of spin from substrate dimensionality left as open work. Whether the framework's predictions for this mode match what standard physics calls "the electron" under detailed property comparison is downstream MaSt-correspondence work.
- **T(3, 1), T(4, 1), ...**: closure-satisfying primitives with progressively larger m. Heavier than T(2, 1) by the rest-mass formula of [Chapter 2 §3](02-modes-on-a-sheet.md). Candidate states that *might* correspond to what standard physics calls further-generation leptons; the identification is open.

These are the framework's primitive charged states. Every closure-satisfying configuration is built from T(m, 1) primitives — either as a singleton (this section) or as a multi-component repetition (§4.3).

### 4.2 Genuine torus knots T(p, q), p, q ≥ 2, gcd(p, q) = 1 — closure-failing

Modes with both windings at least 2 and no common factor. Topologically these are genuine torus knots in 3-space, with non-trivial crossing number, and **chirally distinct from their mirrors** — T(p, q) and T(p, −q) are different knots, not isotopic to each other under orientation-preserving deformations.

Under the chirality criterion (§1.1): the chirality reflections of a genuine torus knot are *not* topological symmetries of the curve, so criterion (i) fails. **Closure fails for every genuine torus knot.** Operationally (the synchronization test): n = q does not divide m = p (since gcd(p, q) = 1 and p ≥ 2 forces q ∤ p in general). The two views agree.

Examples:

- **T(2, 3) trefoil**: 3 ∤ 2, fails synchronization; chirally distinct from its mirror T(2, −3), so criterion (i) fails. Mass-only.
- **T(2, 5) cinquefoil**: 5 ∤ 2, fails. Mass-only.
- **T(3, 4)**: 4 ∤ 3, fails. Mass-only.
- **T(3, 5), T(2, 7), T(3, 7), T(4, 5), ...**: all genuine torus knots are chirally distinct from their mirrors — closure-failing. Mass-only.

Genuine torus knots are a **separate mass-only category** from single-axis modes, with a different structural reason for failure: chirality is non-degenerate (genuine torus knots are not isotopic to their mirrors), so the wrap-order's R_u cannot be enforced as a particle symmetry without combining topologically distinct configurations. Per chapter 5's metric-side analysis (chapter 5 §6), the natural particle on a genuine torus knot falls back to the joint-reversal R_J symmetrization — yielding a mass-only configuration with no spacetime-extended-to-compact gauge potential, plus a chirality-encoded compact-compact cross-term that records which chirality of knot is present.

This is a substantive framework prediction: **the entire genuine-torus-knot tower** (T(2, 3), T(2, 5), T(3, 4), T(3, 5), T(2, 7), ...) **carries mass but no observable EM charge.** Whether any of these correspond to standard physics' neutral massive states (neutrinos, neutral mesons, dark-matter candidates, the Higgs) is downstream MaSt-correspondence work. The framework provides multiple structural-neutrality mechanisms; standard physics has multiple categories of neutral massive states; how they map is open.

**The tower is large; what selects which members populate.** Standard physics observes only a small number of stable neutral massive species; the framework's tower (T(2, 3), T(2, 5), T(3, 4), T(3, 5), T(2, 7), T(3, 7), T(4, 5), …) is much larger. This is not a contradiction — it is a distinction between what the framework *predicts as possible* (every closure-failing genuine torus knot configuration is structurally allowed) and what *gets populated* (which depends on energetics and stability mechanisms not derivable at this project's linear-theory scope). Candidate selection mechanisms operating on the tower:

- **Mass cost.** Heavier modes (larger √((m/ε)² + n²) in the dispersion of [Chapter 2 §3](02-modes-on-a-sheet.md)) are energetically more costly to populate; thermal/equilibrium occupation suppresses high-(m, n) members.
- **Aspect-ratio dependence.** Per [Chapter 7](07-aspect-ratio-and-character.md), the relative mass of (m, n) modes shifts with ε; at extreme ε, only specific (m, n) values are competitive at low energy, so the tower is not uniformly populated even before energetics is considered.
- **Multi-knot decay.** Heavier members of the tower may decay into multi-link configurations of T(m, 1) primitives via energetics not captured at this project's linear-theory level — forwarded to [metric-binding](../metric-binding/) for the multi-knot energetics treatment.
- **Predictive content distinction.** What the framework predicts is *which configurations are possible* under the closure rule; what is *populated* (and how stable each is) depends on energetics outside metric-charge's scope.

The framework's commitment is therefore: the tower is part of the predicted structural inventory; specific selection among its members is downstream work. This is consistent with the framework being a structural classifier of closure-eligible configurations rather than a populated-state predictor.

### 4.3 Multi-component links — closure-satisfying iff primitive is T(m, 1)

Multi-component links T(k·m', k·n') decompose into k disjoint copies of the primitive T(m', n') with gcd(m', n') = 1. Two cases:

**4.3a Closure-satisfying: T(k·m', k) = k × T(m', 1).** When the primitive is T(m', 1) — i.e., n' = 1 — the multi-link has total winding (k·m', k) with n = k dividing m = k·m'. Each component is achiral (an unknot), so the chirality criterion holds for the link. Closure is satisfied.

These are the framework's **multi-link charged states**: **k phased copies of a T(m', 1) primitive** (the framework's Configuration Y reading — see [Ch 8 §5](08-shear-and-fractional-charge.md) for the X-vs-Y distinction and the commitment), with each component carrying 1/k of the link's total charge. Under Configuration Y, the link sources k surviving h_μw cross-terms — one per component — not a single cross-term for the link as a whole. The per-component fractional-charge structure follows from the link's geometry plus integer total quantization, consistent with [grid-duality §7.5.4](../grid-duality/07-wrap-promotion-modeling.md) (the link's integer total is preserved; the 1/k per component is a *fractional association* across the k structural components, not a fractional value of a single quantity).

Examples:

- **T(6, 3) = 3 × T(2, 1)**: three phased copies of the (2, 1) primitive. Each component carries 1/3 of the primitive's charge. *If* [Chapter 8](08-shear-and-fractional-charge.md)'s k-optimization yields k_opt = 3, this configuration is the candidate identification with what standard physics calls a quark (specifically, a flavor family proportional to model-F's proposed T(2, 1) ↔ electron correspondence). Whether k_opt = 3 is the actual optimization result is the chapter-8 question, not a presupposition here.
- **T(4, 2) = 2 × T(2, 1)**: two phased copies of T(2, 1). Each carries 1/2 of the primitive's charge. Another closure-satisfying multi-link; whether T(4, 2) or T(6, 3) (or some other k × T(m', 1)) is energetically favored under shear is the chapter-8 optimization question. The framework does not pre-commit to which k matches observed structure.
- **T(9, 3) = 3 × T(3, 1)**: three phased copies of the heavier T(3, 1) primitive. Same k = 3 structure as T(6, 3) but with a heavier primitive; one of the candidate configurations the chapter-8 optimization examines across (k, m').

**4.3b Closure-failing: k × T(p, q) with primitive a genuine torus knot.** When the primitive is a genuine torus knot (p, q ≥ 2, gcd = 1), the multi-link has total winding (k·p, k·q). Each component is chirally distinct from its mirror, so the chirality criterion fails for the link. Operationally: n = k·q does not divide m = k·p (since q ∤ p with gcd = 1 and p, q ≥ 2). Closure **fails**.

Example: T(6, 4) = 2 × T(3, 2). Two phased copies of a trefoil-class knot. The link inherits its primitive's chirality non-degeneracy: 4 ∤ 6 (since 6/4 = 1.5). Mass-only.

So every multi-link configuration is closure-satisfying iff its primitive is T(m, 1). Multi-links with genuine-torus-knot primitives are mass-only, in the same category as single genuine torus knots from §4.2.

### 4.4 Summary table

The full inventory at the linearized wave-equation level:

| (m, n) form | Closure | Charge per component | External-identification proposals (model-F, exploratory) |
|---|---|---|---|
| Light (0, 0) | Fails | — | photon |
| Single-axis (m, 0), (0, n) | Fails (one winding zero) | — | candidate neutral massive state |
| T(2, 1) primitive | ✓ | 1 | candidate electron (MaSt model-F reference target) |
| T(3, 1), T(4, 1), … primitives | ✓ | 1 | candidate further leptons; not yet specifically proposed |
| Genuine torus knot T(2, 3), T(2, 5), T(3, 4), … | **Fails (chirality criterion)** | — | candidate neutral massive state — distinct from single-axis category |
| Multi-link T(k·m', k) = k × T(m', 1), k ≥ 2 | ✓ (k-fold) | 1/k | candidate fractional-charge composite — specific k_opt set by [chapter 8](08-shear-and-fractional-charge.md)'s optimization; *if* k_opt = 3 emerges, the T(6, 3) = 3 × T(2, 1) case matches standard physics' quark structure |
| Multi-link with genuine-knot primitive | **Fails (chirality criterion)** | — | candidate neutral massive state — chirality-non-degenerate category |

The external-identifications column is **exploratory and not an input to this project's derivations**. Chapter 4 establishes only the closure-satisfaction structure; whether each predicted state corresponds to a particle in the standard-physics inventory requires:

- Aspect-ratio analysis (chapter 7) to determine which (m, n) values are stable on the sheet.
- Shear analysis (chapter 8) to determine which multi-component links are favored under shear.
- Multi-knot energetics (metric-binding) to determine binding and composition.
- MaSt-correspondence work (downstream) to compare metric-charge's inventory against standard-physics inventory.

The framework's job in this chapter is to **derive the inventory of states the closure condition produces**. Identification is a comparison task that happens *after* the framework has predicted its own properties.

**Note on category richness.** The framework has *three* mass-only categories (single-axis, genuine-torus-knot via chirality non-degeneracy, cancellation-pair) and *two* charge-carrying categories (T(m, 1) primitives, k × T(m, 1) multi-links). Standard physics has multiple categories of charged particles (leptons, quarks, charged hadrons) and multiple categories of neutral massive states (neutrinos, neutral mesons, dark matter candidates, Higgs). The structural-shape correspondence is suggestive — the framework may have richer structural distinctions than a simpler "charged vs neutral" partition — but quantitative correspondence is downstream work.

---

## 5. Closure-rule variants

[Chapter 1 §10](01-foundation.md) flagged variants of the closure rule. Each gives a different particle inventory; examining each here helps identify what the standard rule actually buys us.

### 5.1 Variant — opposite wrap-order

The standard rule treats u as ring and w as tube (the convention adopted in [Chapter 1 §10](01-foundation.md)). The mirror variant flips this: u as tube, w as ring. Closure under the mirror variant requires **m | n** instead of n | m.

**Topologically** this gives the same set of particles modulo cycle-swap: T(p, q) under "m | n" is the same as T(q, p) under "n | m." But the two are physically distinct in metric-charge per [Chapter 3 §3.2](03-knots-on-the-torus.md), since the (u, w) ↔ (w, u) symmetry is broken by the wrap-order convention and the downstream conventions that inherit from it.

The variant is just the alternative wrap-order convention. As discussed in Ch 1 §10, whether the convention's match to observation is genuine or is itself a labeling choice the math fixes for self-consistency is open work for [grid-duality §8](../grid-duality/08-where-alpha-appears.md).

### 5.2 Variant — single-axis closure

A weaker rule: closure requires only that one specific winding be nonzero, without the chirality criterion. Equivalently: closure ≡ "m ≠ 0" alone.

Under this variant:

- **Single-axis modes (m, 0)** would satisfy closure (one winding nonzero, no chirality test needed).
- **All other modes with m ≠ 0** would also satisfy.
- **Modes with m = 0** (light, single-axis (0, n)) would fail.

Implication: the framework's structural-neutrality category for single-axis modes disappears partially — (m, 0) would carry observable EM. This is inconsistent with the framework's prediction of structurally neutral mass-only modes. The variant is therefore likely incorrect; the closure rule's two-winding requirement is what produces the structural-neutrality category.

### 5.3 Variant — multi-knot collective closure

A different kind of variant: the closure condition can be satisfied *collectively* by a configuration of multiple knots even when no single knot satisfies it. For example, a (1, 0) mode and a (0, 1) mode together have both windings collectively, even though neither single mode satisfies the closure condition individually.

Whether this collective form of closure is meaningful — and whether it would give the same physics as a single closure-satisfying mode — depends on the field-theoretic interactions between the components. At the linear level (this project's scope), modes superpose without interaction and the "collective closure" idea is not well-defined as a wave-equation concept.

The variant becomes meaningful in [metric-binding](../metric-binding/)'s territory, where multi-knot interactions are the explicit subject of analysis. As a candidate description of *bound states* like atoms — composite particles whose closure-like behavior derives from interactions between non-closure-satisfying components — this variant is forwarded to metric-binding for treatment.

The structural takeaway: variant 5.3 suggests a *second tier* of physical configurations beyond the single-mode inventory — composite structures built from interacting non-closure components. Standard physics' atomic / nuclear / hadronic bound states are candidates; whether the variant correctly describes any of them is a downstream MaSt-correspondence question.

---

## 6. The distinguished particle inventory

Under the chirality closure rule, the predicted inventory partitions into two top-level categories: charged states and neutral massive states. The neutral category subdivides into three structurally distinct mechanisms.

### 6.1 Charged states (closure-satisfying)

- **T(m, 1) primitives** — single charged particles built from the simplest closure-satisfying form (n = 1 trivially divides any m, achiral curve in 3-space). Topologically unknots. T(2, 1) is a candidate electron identification (MaSt model-F reference target); T(3, 1), T(4, 1), ... are candidate further generations.

- **Multi-link T(k·m', k) configurations = k × T(m', 1)** — k phased copies of a T(m', 1) primitive, with each component carrying 1/k of the link's total charge. T(6, 3) = 3 × T(2, 1) at k = 3 is a candidate quark identification (subject to chapter 8's k-optimization confirming k_opt = 3).

That's the entire charged inventory: T(m, 1) primitives and their k-component repetitions. The framework predicts that **all charge-carrying configurations are built from T(m, 1) primitives** — either as singletons or as multi-component links.

### 6.2 Neutral massive states (closure-failing) — three distinct mechanisms

- **Light** (the (0, 0) zero mode) — massless, no compact-direction structure, ordinary EM-field-quantum in spacetime.

- **Single-axis modes** (m, 0), (0, n) — fail closure because *one winding is zero* and there is no chirality structure to test. The natural particle reduces to the metric-mass standing wave on a single compact direction; no spacetime-extended-to-compact off-diagonal is sourced. Mass without observable EM by *structural-degeneracy* mechanism.

- **Genuine-torus-knot modes** T(p, q) with p, q ≥ 2 and gcd(p, q) = 1 — fail closure because the *curve is chirally distinct from its mirror in 3-space*. The chirality criterion (i) of [Ch 1 §10](01-foundation.md) fails — the wrap-order's R_u cannot be enforced as a particle symmetry without combining topologically distinct knot types. The natural particle falls back to joint-reversal R_J symmetrization, yielding mass + chirality field but no observable EM gauge potential. Examples: trefoil T(2, 3), cinquefoil T(2, 5), T(3, 4), and the rest of the genuine-torus-knot tower.

- **Multi-link modes with genuine-torus-knot primitives** T(k·p, k·q) — the same chirality-non-degeneracy mechanism operating on multi-component links built from genuine-torus-knot primitives.

(A *fourth* neutrality mechanism — cancellation neutrality from opposite-handedness pairs in a single field — operates on top of these. See [Chapter 6 §4](06-handedness-and-pairs.md). The cancellation mechanism is independent of which (m, n) sector the components live in; it can produce additional neutral configurations from any closure-satisfying base.)

### 6.3 What this inventory says

The **geometric particle inventory of metric-charge** under chirality closure has the following structural shape:

- A massless field (light / photon analog) — one category.
- Charged states built from T(m, 1) primitives — singletons (candidate leptons) and multi-links (candidate quarks). Two charge-carrying sub-categories.
- Neutral massive states — at least three structurally distinct mechanisms (single-axis, chirality-non-degenerate genuine torus knots, cancellation pair). Possibly more.

Standard particle physics has multiple charge-carrying categories (charged leptons, quarks, charged hadrons-as-composites) and multiple neutral-massive categories (neutrinos in three flavors, neutral mesons, neutral baryons, dark matter candidates, the Higgs). The framework's category structure has the right *shape* to potentially map onto this, with the framework's *richer-than-binary* neutral structure suggesting multiple distinct neutral states rather than a single "neutrino" category.

**Whether the framework's categories correspond to standard physics' categories — at the level of specific particles or only at the structural-pattern level — is downstream MaSt-correspondence work that this project does not undertake.** The closure condition produces an inventory of the right shape; whether the map holds at the level of individual particle properties is open work.

A specific question worth flagging: **standard physics treats hadrons as composites** (3 quarks per baryon, 2 quarks for mesons), not as single fundamental particles. The framework's prediction that all *fundamental* charged states are T(m, 1) primitives or k × T(m, 1) multi-links — with no fundamental "hadron tier" of single torus knots — matches this composite-hadron view of standard physics better than the framework's earlier draft (which had a tower of single charged genuine torus knots as candidate hadrons). Hadrons in the framework would emerge as bound states of multiple k × T(m, 1) multi-links — metric-binding's territory.

The downstream chapters develop:

- Chapter 5: the metric-side derivation of the single gauge field B_μ from h_μw via the wrap-order-asymmetric standing-wave construction; mass-only outcomes for closure-failing modes via R_J fallback.
- Chapter 6: handedness / matter-antimatter signs within the inventory, plus a fourth cancellation-neutrality mechanism.
- Chapter 7: how aspect ratio ε determines which (m, n) dominate at low energy.
- Chapter 8: how shear σ_uw biases chirality within particles and favors specific k values for multi-link configurations — the optimization examines whether k = 3 emerges naturally.

---

## 7. What's next

[Chapter 5 — Metric self-consistency and gauge promotion](05-metric-self-consistency.md). The closure-satisfying modes from this chapter source off-diagonal metric entries (per metric-mass Chapter 5) under the wrap-order-asymmetric standing-wave construction. Chapter 5 derives that closure-satisfying modes produce **a single gauge potential B_μ** (from the tube-direction off-diagonal h_μw); the ring-direction would-be cross-term cancels by the metric-mass mechanism. Closure-failing modes — both single-axis and chirality-non-degenerate genuine torus knots — source no spacetime-extended-to-compact off-diagonal under the natural-particle construction, yielding mass-only outcomes (with a chirality-encoded compact-compact cross-term in the genuine-torus-knot case). The chapter also provides the calculable mechanism for how mass bends spacetime and how charged matter creates EM fields, building on metric-mass Chapter 5 §6 and Chapter 6 §4.

---

## What this chapter does **not** do

- **Does not derive numerical α.** Cited from [grid-duality §8](../grid-duality/08-where-alpha-appears.md) (structural location at L3) and future grid alpha-derivation work (numerical value).
- **Does not develop the metric-side derivation.** That is chapter 5's job — the wrap-order-asymmetric standing-wave construction that produces a single gauge field per closure-satisfying particle.
- **Does not assign handedness / matter-antimatter signs** within the satisfying inventory. Chapter 6.
- **Does not vary aspect ratio ε.** Chapter 7.
- **Does not optimize k for multi-component links.** Chapter 8 takes the multi-link structure identified here and works through the energetics under shear.
- **Does not analyze multi-knot energetics or bound states** beyond the closure-rule variant 5.3 mention. metric-binding territory.
- **Does not identify which standard-physics neutral states correspond to single-axis vs chirality-non-degenerate mass-only categories.** Three structural mass-only mechanisms exist in the framework (single-axis, chirality-non-degenerate, cancellation pair); their map to observed neutral-massive states (neutrinos, neutral mesons, dark matter, Higgs) is downstream MaSt-correspondence work.
- **Does not commit to MaSt-correspondence assignments.** The external-identifications column in §4.4 is exploratory; rigorous correspondence is downstream work.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Do the three structural mass-only mechanisms (single-axis, chirality-non-degenerate, cancellation pair) correspond to distinct standard-physics neutral categories (neutrinos, neutral mesons, dark matter, etc.) or do some collapse together? | Downstream MaSt-correspondence work |
| Are closure-rule variants 5.1 (opposite wrap-order) and the standard rule physically distinct, or are they the same physics with relabeled coordinates? | Chapter 5 / [grid-duality §8](../grid-duality/08-where-alpha-appears.md) |
| Does closure-rule variant 5.3 (multi-knot collective closure) describe atoms or other composite bound states? | metric-binding |
| What standard-physics state corresponds to the genuine-torus-knot tower of mass-only modes (T(2, 3), T(2, 5), T(3, 4), ...)? | Downstream MaSt-correspondence work |
| Why is the wrap-order convention asymmetric in (u, w) — is it adopted or derivable? | [grid-duality §8](../grid-duality/08-where-alpha-appears.md) + grid alpha-derivation |
| Does the metric-charge inventory of §6 quantitatively match observed masses and charges of standard-model particles? | Downstream MaSt-correspondence work |
