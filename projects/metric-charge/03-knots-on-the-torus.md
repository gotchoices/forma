# Chapter 3 — Knots on the torus

This chapter takes the (m, n) mode family from [Chapter 2](02-modes-on-a-sheet.md) and reframes it geometrically: each non-trivial mode corresponds to a *closed curve* — a torus knot — traversing the (u, w) sheet. The chapter characterizes **knot space** thoroughly, both for the immediate use of chapters 4–8 and for downstream uses in [metric-binding](../metric-binding/), where Pauli-like state-space questions and "how many knots in a particle" counting will become primary.

**Inheritance.**

- *From [grid-duality §7.5.1](../grid-duality/07-wrap-promotion-modeling.md):* the topological setup. Closed loops on T² fall into homotopy classes labeled by (m, n) ∈ ℤ², integer windings around the two cycles, π₁(T²) = ℤ². Used here, not re-derived.
- *From [Chapter 2](02-modes-on-a-sheet.md):* the (m, n) labels, the three mode classes, and the energy-momentum identification with topological windings.

**Distinctive job.** Establish *knot space* as a structured object — what labels distinguish knots, what equivalence relations identify them, what topological invariants serve as candidate quantum numbers. Build the framework with foresight for downstream uses: closure-eligibility ([Chapter 4](README.md#chapters)), multi-phase wraps producing fractional charge ([Chapter 8](README.md#chapters)), Pauli-like distribution of knots ([metric-binding](../metric-binding/)), and "how many knots in a particle" composition (metric-binding and beyond).

This chapter does **not** compute energetics, force laws, or any quantitative behavior of multi-knot configurations at finite separation. Those are the technical core of [metric-binding](../metric-binding/), specifically its [chapter 3](../metric-binding/README.md#chapters). Here we establish only the structural language — labels, equivalences, topological invariants — that the multi-knot energetics will operate on.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | From modes to curves — the geometric reframing |
| 2 | Torus knot basics |
| 3 | Knot space — distinguishing labels and equivalence relations |
| 4 | Topological invariants as candidate quantum numbers |
| 5 | State distinguishability and the energy landscape |
| 6 | Single-knot, multi-component, and multi-position configurations |
| 7 | The closure-eligibility partition (preview) |
| 8 | What's next |

---

## 1. From modes to curves — the geometric reframing

[Chapter 2](02-modes-on-a-sheet.md) labeled solutions of the wave equation by integer pairs (m, n) — winding numbers in u and w. Each non-trivial (m, n) corresponds to a wavefunction that varies sinusoidally with u and w in a specific pattern: m oscillations around the u-cycle and n around the w-cycle.

The geometric content is that **the wavefunction's nodes form a closed curve on the (u, w) sheet, and that curve wraps m times around the u-cycle and n times around the w-cycle as it closes upon itself.** A wave with winding (1, 2), for example, is a closed curve that goes once around u for every two times it goes around w — a particular path on the torus that is *itself* a topological object, the trefoil knot T(1, 2) [actually T(2, 3); see §2].

Reframing each (m, n) mode as a geometric curve:

| Mode label | Geometric object |
|---|---|
| (0, 0) | No curve at all; the wavefunction is constant on the sheet |
| (m, 0) with m ≠ 0 | A closed loop wrapping the u-cycle m times, no w-winding |
| (0, n) with n ≠ 0 | A closed loop wrapping the w-cycle n times, no u-winding |
| (m, n) with both nonzero | A *torus knot*, in the standard mathematical sense |

This reframing sets the language for the rest of the chapter and for chapter 4's closure analysis. The wave-equation modes of chapter 2 and the geometric closed curves of this chapter are the same underlying objects, viewed through different lenses. We will move back and forth between the two views as convenient.

The visualization is intuitive: imagine a small donut shape (the (u, w) torus) with a piece of string wrapped around it. The string goes around the donut hole m times (the u-cycle) and around the donut tube n times (the w-cycle) before closing on itself. For (m, n) = (1, 0), the string just goes once around the donut hole — a simple loop. For (m, n) = (1, 2), it spirals: once around the hole while twisting twice around the tube. The trefoil knot.

---

## 2. Torus knot basics

The standard mathematical notation for these curves is **T(p, q)** — the torus knot with windings p and q. Our (m, n) labels correspond directly: (m, n) = (p, q).

Several well-established facts from knot theory are imported here without re-derivation. References: any standard knot-theory textbook; the [Wikipedia article on torus knots](https://en.wikipedia.org/wiki/Torus_knot) is sufficient for our purposes.

**Closure structure (gcd matters):**

- If gcd(p, q) = 1, then T(p, q) is a *single closed curve* — one knot, one component.
- If gcd(p, q) = k > 1 with p = k·p', q = k·q', then T(p, q) is *k disjoint copies* of T(p', q') — a k-component link, not a single knot.

So gcd(p, q) tells us how many distinct closed loops the (p, q) winding produces.

**Topological equivalences in 3-space:**

These are equivalences at the level of *abstract knot type* — two curves that can be continuously deformed into each other in 3-space. They do not in general carry over to physical equivalence in metric-charge; see §3 for the proper distinction.

- **T(p, q) and T(q, p) are the same knot.** Swapping the cycles is a topological coordinate-relabel.
- **T(p, q) and T(−p, −q) are the same unoriented knot.** Reverse traversal direction; same closed curve in space.

**Trivial cases — the unknot:**

- **T(1, q) and T(p, 1) are the unknot for any p, q.** A curve that wraps one cycle exactly once can be slid off the torus surface entirely without crossing itself — it bounds a disc in 3-space and has no genuine knotting. T(1, 2), T(1, 3), T(1, 100) are all the unknot.
- **T(0, 0)** is the empty loop — no curve at all.

> **Topological triviality does not imply physical triviality.** This point is structurally important and easy to miss. T(1, 2) and T(1, 3) are both unknots topologically — but in metric-charge they are different *physical states* with different (m, n) labels, different rest masses, different compact-direction momenta, conserved as distinct sectors of the wave equation. The "unknot" label classifies the embedded curve in 3-space; the (m, n) label classifies the mode in this framework. They are different things, and physics in metric-charge cares about the latter. A topologically trivial unknot mode can still be closure-eligible (chapter 4), can carry observable charge, and can play a substantive role in the particle inventory. As an external reference: MaSt model-F (per [matter-from-light §4](../../papers/matter-from-light.md)) has independently proposed identifying (1, 2) — a topological unknot — with what standard physics calls the electron. The metric-charge framework here treats that proposal as a candidate correspondence to compare against, not an axiom of this project. §3 develops the topology-vs-physics distinction in full.

**Genuine knots:**

- **T(2, 3) is the trefoil**, the simplest non-trivial knot, crossing number 3.
- T(2, 5), T(3, 4), T(3, 5), ... — a tower of progressively complex torus knots, all with both p, q ≥ 2 and gcd(p, q) = 1.

**Crossing number formula:**

For T(p, q) with gcd(p, q) = 1 and p, q ≥ 2:

c(T(p, q)) = min(p(q − 1), q(p − 1))

So c(T(2, 3)) = min(4, 3) = 3 (trefoil); c(T(2, 5)) = min(8, 5) = 5 (cinquefoil); c(T(3, 4)) = min(9, 8) = 8; etc. For p = 1 or q = 1, c = 0 (unknot, no crossings).

The mapping (m, n) → T(m, n) is the bridge from mode label to standard knot terminology; we will use both notations as convenient for the rest of the chapter.

---

## 3. Primary labels and topological invariants

The primary state space of metric-charge's modes is **ℤ²** — each state is labeled by an integer pair (m, n). The wave equation conserves these labels exactly under unitary evolution ([grid-duality §7.5.2](../grid-duality/07-wrap-promotion-modeling.md)); distinct (m, n) values are distinct conserved sectors. **(m, n) is the framework's primary physical label.**

Topological knot type is a *derived* invariant. Each (m, n) traces a closed curve T(m, n) on the embedded 2-torus, and that curve has a knot type in 3-space. Different (m, n) values can map to the *same* knot type — for example, all of T(1, 2), T(1, 3), T(1, 100) are the unknot; T(2, 3) and T(3, 2) are the same trefoil. Topological knot type is therefore a *coarser* classification than (m, n) and does not by itself organize the state space.

The chapter's view: **(m, n) is the primary physical label; topological invariants are useful organizing tools but they do not reduce the state space.** Two modes with the same knot type but different (m, n) are different physical states. The "equivalences" of §2 (swap, reverse) operate at the *topological* level — they identify knot types but they do not identify modes.

### 3.1 The labels

Each mode carries multiple labels. (m, n) is primary; the others are derived from (m, n).

| Label | Source | Range | Status | Interpretation |
|---|---|---|---|---|
| **(m, n)** | wave-equation mode (Chapter 2) | ℤ² | **primary** | Winding numbers; conserved physical quantum numbers |
| gcd(m, n) | derived from (m, n) | ℕ | derived | Number of disjoint loops in the closure |
| sign(m), sign(n) | derived from (m, n) | {+, −} per integer | derived | Chirality / handedness components |
| crossing number c | T(m, n) topology | ℕ (zero for unknots) | derived | Topological complexity in 3-space |
| genus, polynomials, ... | T(m, n) topology | various | derived | Fine-grained topological fingerprint |

For torus knots specifically, all topological invariants (crossing number, genus, Alexander polynomial, etc.) are functions of (m, n) — they add no new information beyond what the integer pair already carries. They are useful for *organizing* the state space (e.g., grouping by crossing-number tier) but not for distinguishing states finer than (m, n) does.

### 3.2 Topological equivalences (do not reduce the physical state space)

The following equivalences hold *in topology* — they identify knot *types*. They do *not* generally correspond to physical equivalence in metric-charge, because they relate different (m, n) values which the framework treats as distinct conserved sectors.

- **Cycle swap:** T(p, q) ≡ T(q, p) topologically. Swapping cycles is a coordinate-relabel for *bare* topology. The (m, n) and (n, m) modes are nevertheless *different physical states* in metric-charge: the (u, w) ↔ (w, u) symmetry is broken by four conventions introduced downstream — the closure condition (Chapter 1 §10) singles out w-winding specifically, the aspect-ratio convention (Chapter 1 §3) labels one direction "tube" and the other "ring," shear (Chapter 8) sits asymmetrically in one off-diagonal entry, and the gauge convention (Chapter 5; see [R62 Derivation 5](../../studies/R62-derivations/derivation-5.md) for MaSt's version) selects one of the two U(1) potentials as the physical photon.

- **Sign reflection:** T(p, q) and T(−p, −q) are identical *unoriented* knots (orientation-reversed traversal of the same closed curve). Whether the orientation reversal is *physically* distinguishing — whether (m, n) and (−m, −n) are different particles — is the matter/antimatter question of [Chapter 6](README.md#chapters). The framework treats them as different states until proven otherwise.

- **Mirror reflection:** T(p, q) and T(p, −q) are *chirally distinct* — mirror images in 3-space. They are not topologically equivalent under orientation-preserving deformations. Whether physical chirality matters is the chirality question.

- **Trivial reductions:** T(1, q) ≡ T(p, 1) ≡ unknot for any p, q. **Even though all such curves are topologically the unknot, the modes (1, 2), (1, 3), (1, 100), ... are still distinct physical states** — they have different (m, n), different masses, different compact-direction momenta, and the wave equation conserves them in different sectors. The unknot label says only that the embedded curve has no crossings, not that the modes are physically identical.

- **Composite knots:** T(km, kn) with gcd(m, n) = 1 and k > 1 is a *k-component link* — k disjoint parallel loops, each topologically T(m, n) on its own (see §6). This is structurally distinct from k separate T(m, n) curves at different positions in S.

Bottom line: the integer pair (m, n) is what the framework uses to count states; topological equivalence at the abstract-knot level is a different (and weaker) classification that may or may not have physical relevance, examined case by case in chapters 4–8.

---

## 4. (m, n) as primary quantum number; derived invariants

The primary "quantum number" of a mode is its (m, n) label. It is conserved by the wave equation, distinguishes states discretely with no continuous interpolation between values, and is the substrate for all conservation laws in this framework. All other topological invariants are *derived* from (m, n) for torus knots. Some of those derived invariants are useful for organizing the state space; none of them refines the state space beyond what (m, n) already provides.

### 4.1 The primary label

- **(m, n) ∈ ℤ²** — winding numbers in u and w. Conserved exactly under unitary evolution ([grid-duality §7.5.2](../grid-duality/07-wrap-promotion-modeling.md)). Distinguishes states discretely; no continuous path connects different integer pairs. This is the fundamental quantum-number label of the framework.

### 4.2 Derived invariants (from (m, n) alone, for torus knots)

Useful for organization, but redundant with (m, n) for torus-knot states.

- **gcd(m, n).** Distinguishes single knots (gcd = 1) from k-component links (gcd = k > 1). Foresight: this is the natural label for "how many knots in a particle" when the particle is realized as a k-component link (per §6) rather than k separate knots at different positions.

- **sign(m), sign(n).** Chirality / handedness components. The (m, n) → (−m, −n) reflection is the simplest discrete symmetry in knot space; the full chirality structure also includes the mirror reflection (m, n) → (m, −n). Candidate matter/antimatter and chirality labels ([Chapter 6](README.md#chapters)).

- **Crossing number c(T(m, n)).** Counts how many crossings the embedded curve has in 3-space, in its minimal projection. Formula from §2: c = min(p(q − 1), q(p − 1)) for p, q ≥ 2 with gcd = 1; c = 0 for unknots. **Candidate organization for generation structure** — particle generations might correspond to crossing-number tiers. The trefoil T(2, 3) at c = 3 is the simplest non-trivial torus knot; T(2, 5) at c = 5, T(3, 4) at c = 8, T(3, 5) at c = 10, etc. form an ascending tower. Whether tier-m knots correspond to generation-m particles is open work for chapters downstream and follow-up projects.

- **Genus, Alexander polynomial, signature, Jones polynomial.** For *torus knots*, all of these are determined by (m, n) — closed-form expressions in p and q. (For example, g(T(p, q)) = ½(p − 1)(q − 1) for p, q ≥ 1 with gcd = 1.) They are useful for *naming* knots in standard mathematical terms but add no information beyond (m, n) for the framework's purposes.

### 4.3 Sub-(m, n) labels (not topological at all)

Two further labels are *not* topological invariants but may still be physically distinguishing:

- **Standing-wave phase alignment.** Two modes with identical (m, n) but different phase relationships between their u-mode and w-mode standing waves are not topologically distinct — they trace out the same knot type. They may still differ in whether they satisfy the closure condition. This is a chapter-4 question; flag here as a *sub-(m, n)* label that affects observability without affecting topology.

- **Position (S₁, S₂).** A mode's spatial location on the manifold. Trivially distinguishes multi-knot configurations from single-knot ones. metric-binding territory.

For torus knots specifically, **(m, n) is the most-fine label that the topology offers**; finer physical distinctions require sub-(m, n) labels (phase, position) that are not topological at all.

---

## 5. State distinguishability and the energy landscape

Forward-looking: at some point the framework will ask what happens when multiple knots inhabit a single sheet (or system). The structural ingredients for that question live in this chapter — the discrete labels of §3 and the topological invariants of §4 are precisely what distinguishes one knot configuration from another.

This chapter takes a stance on how multi-knot configurations relate to each other: the wave equation is linear, so two knots in arbitrary configurations *can* in principle coexist as a superposition. What determines whether a particular multi-knot configuration is physically realized is the **energy landscape**, not a postulated exclusion rule.

Three statements:

- **Two knots at *exactly* identical labels** — same (m, n), same chirality, same (S₁, S₂) position, same standing-wave phase — correspond to a doubled wavefunction at a single configuration. Linear theory permits this. Whether it is a ground state of any physical system is an *energetic* question, deferred to [metric-binding](../metric-binding/).

- **Knots that differ in at least one label** — different (m, n), different chirality, different position, different phase, different orientation — are distinguishable in some respect, and the energetic cost of their coexistence is typically lower. The prototype example is the multi-component link of §6: k copies sharing the same (m, n) but distributed in *phase* around the cycle they traverse. They do not overlap geometrically and do not pay an overlap penalty.

- **Expected outcome:** least-energy multi-knot configurations spread along the available distinguishability axes — phase, orientation, position, sub-(m, n) labels — rather than stack identically. This expectation does not require a new rule; it follows from the rich state space of §3 plus standard energy minimization.

The framing here is structurally similar to the standard Pauli exclusion principle but does not adopt it as a postulate. Pauli's discrete state-counting and the antisymmetry of identical-fermion wavefunctions are phenomena this framework should *derive* as emergent properties of the energy landscape on knot configuration space, not axioms imposed on it. metric-binding is where these energetics get worked out; chapter 3's job is only to establish that knot configurations have enough labels for distinguishable states to be built.

### Three additional structural facts

- **Knot space is rich.** With (m, n) ∈ ℤ², chirality, multi-component count, position (S₁, S₂), standing-wave phase, and (in principle) finer invariants, the label space allows many distinguishable configurations at any given energy tier. The discrete state space is, if anything, *richer* than spin-1/2 fermion state space.

- **Spin candidates.** MaSt model-F (per [matter-from-light §4](../../papers/matter-from-light.md)) proposes that what standard physics calls spin-1/2 arises geometrically for T(1, 2) from the 1:2 winding ratio via ℓ = E/ω = ℏ/2. Cited here as an external reference derivation; spin may itself be a label derived from (m, n) rather than an independent quantum number. (Note: T(1, 2) topologically is the unknot per §2, so the "1:2 ratio" is the sub-(m, n) phase relationship, not a topological knot — this nuance is part of why standing-wave phase alignment from §4 matters.)

- **Continuous unitary evolution preserves (m, n) and other topological invariants** ([grid-duality §7.5.2](../grid-duality/07-wrap-promotion-modeling.md)). Transitions between knot classes require non-unitary processes. The discrete-state condition is *structural*; whatever exclusion-like behavior emerges on top of it is *energetic*, not topological.

---

## 6. Single-knot, multi-component, and multi-position configurations

There are *three structurally distinct* ways to have "more than one knot" on a single sheet. Distinguishing them now sets up the language for chapters 4, 8, and metric-binding.

### Single (m, n) knot with gcd(m, n) = 1

One closed curve on T², wrapping m times around u and n times around w. Discussed in §1–§4 above.

This is the simplest configuration. All quantum-number labels apply directly. Chapter 4 examines whether this single-knot configuration satisfies the closure condition for a given (m, n).

### Multi-component link, T(km, kn) with gcd(m, n) = 1, k > 1

A *single topological object* that consists of k disjoint parallel loops, each topologically T(m, n). All k loops have the same shape, the same winding, the same chirality. They differ only by their *position* (phase offset) along the cycle they share.

Concretely: imagine a single trefoil T(2, 3). Now imagine k = 3 of them, all with the same (2, 3) winding, but starting at three equally spaced points around the u-cycle (or the w-cycle, or both). Each individual trefoil is shifted by 1/3 of a cycle from the previous one. Together they form a 3-component link T(6, 9).

**This is the structure used in [Chapter 8](README.md#chapters) for the multi-phase fractional-charge mechanism.** k phased copies of the same primitive knot give a k-component link, and the closure condition's behavior on it produces 1/k charge per phase. The "fractional charge of quarks" maps onto the number of phase slots in a k-component link.

Per §3's gcd structure, T(km, kn) is identified topologically as gcd · primitive = k copies of T(m, n). The component count k and the primitive (m, n) are both meaningful labels.

### Multi-knot configuration

k *distinct* closed curves, each a T(m_i, n_i) with potentially different (m_i, n_i), at potentially different (S₁, S₂) positions on the manifold. Each is its own knot; collectively they are not a single torus-knot label.

**This is the structure addressed in [metric-binding](../metric-binding/).** Two (or more) independent knots at finite spatial separation r in (S₁, S₂) form the basic configuration whose energetics metric-binding works out. Specifically, [metric-binding's chapter 3](../metric-binding/README.md#chapters) computes E(r) as a function of separation; subsequent chapters classify regimes (bound, free, partial-separation) and derive the candidate strong-force mechanism.

This chapter does **not** take on multi-knot energetics. It only establishes the language: each knot in the collection has its own quantum-number labels, and the position labels (S₁ᵢ, S₂ᵢ) are part of what distinguishes the configuration.

### Comparison

The three configurations have qualitatively different label structures:

| Configuration | (m, n) labels | Component count | Position labels |
|---|---|---|---|
| Single knot, gcd = 1 | one pair (m, n) | 1 | one (S₁, S₂) |
| k-component link | one pair (km, kn) | k | one (S₁, S₂); the components are phase-distributed in compact directions |
| k-knot configuration | k pairs (m_i, n_i) | depends per knot | k positions (S₁ᵢ, S₂ᵢ) |

The first two operate at a single (S₁, S₂); the third requires the second spatial dimension (S₂) to make sense. (Two knots at different S₁ but same S₂ are degenerate with two knots at different separations along a single line — but the framework keeps S₂ available to allow off-axis displacement, which becomes important for orbital configurations downstream.)

Chapters 4 and 8 of this project operate on the first two configurations: closure and fractional charge are single-position phenomena. Multi-knot energetics — the entire spatial-separation story — is metric-binding's territory.

---

## 7. The closure-eligibility partition (preview)

Carry forward the three mode classes of [Chapter 2 §4](02-modes-on-a-sheet.md) into geometric form. Note carefully: closure eligibility operates on the **(m, n) label** (both windings nonzero), not on the topological knot type. Some closure-eligible modes are topologically the unknot — that is fine, and worth flagging.

| Class | (m, n) | Topology in 3-space | Closure status | Role |
|---|---|---|---|---|
| Light | (0, 0) | No curve | Trivially fails (no winding) | Massless, no compact-direction structure |
| Single-axis | (m, 0) or (0, n), exactly one nonzero | Unknot (single cycle wrapped) | Fails (one winding zero) | L2-in-L3, structural neutrino-class candidate |
| "Weak knot" diagonal | (1, q) or (p, 1) with both nonzero | **Unknot** (no genuine knotting in 3-space, but both windings nonzero) | **Eligible** — both windings nonzero | Closure-eligible despite topological triviality; MaSt model-F (per matter-from-light §4) proposes T(1, 2) as a candidate identification with what standard physics calls the electron |
| Genuine-knot diagonal | (p, q) with both ≥ 2, gcd = 1 | Torus knot in 3-space | Eligible | L3 charged-state candidate; trefoil T(2, 3), cinquefoil T(2, 5), etc. |
| Multi-component link | (m, n) with gcd(m, n) > 1 | k-component link, k = gcd | Eligible | Chapter 8's fractional-charge mechanism |

The five rows give a finer breakdown than chapter 2's three mode classes. The two classes that are particularly worth distinguishing here:

- **The "weak knot" diagonal class** (T(1, q) and T(p, 1)) is topologically the unknot but has both windings nonzero. The closure condition operates on windings, not on knot type, so these modes are closure-eligible. They include T(1, 2) — the (1, 2) winding ratio that MaSt model-F (per [matter-from-light §4](../../papers/matter-from-light.md)) proposes as a candidate identification with what standard physics calls the electron. **A topologically trivial unknot can in principle realize a charged particle as substantive as anything in the standard inventory.** Worth highlighting because the topology-vs-physics distinction is most consequential here.

- **The single-axis class** (T(m, 0) and T(0, n)) is also topologically the unknot, but with one winding zero. The closure condition requires *both* windings nonzero, so these fail closure structurally (not just dynamically). These are the L2-in-L3 candidates from chapter 2.

The bare-topology characterization (unknot vs. genuine knot vs. multi-component link) is useful for naming and organizing modes in standard mathematical terms, but it does *not* directly determine closure eligibility. The relevant criterion is the (m, n) winding pair:

- Modes with no winding fail trivially.
- Modes with one winding zero fail structurally.
- Modes with both windings nonzero are eligible — regardless of whether they trace genuine knots or unknots in 3-space.
- gcd > 1 adds the k-component link structure that chapter 8 exploits.

This partition is the geometric face of the chapter-4 analysis. Chapter 4 examines which eligible (m, n) values actually satisfy the standing-wave alignment of [Chapter 1 §10](01-foundation.md), and what variants of the closure rule might select different sub-families.

---

## 8. What's next

[Chapter 4 — The closure condition](04-the-closure-condition.md). Take the diagonal-knot subset identified in §7 and work through which (m, n) actually satisfy the closure condition's standing-wave-alignment requirement. Examine variants of the closure rule (2π winding on u instead of w, standing wave on only one direction, multi-knot collective closure) and what particle classes each variant would select. Identify the distinguished sub-family of knots that carry observable charge in this framework.

The geometric and topological language built in this chapter — torus knots, winding pairs, gcd structure, knot-space labels, single-knot vs. multi-component vs. multi-knot configurations — is the substrate that chapters 4 through 8 operate on.

---

## What this chapter does **not** do

Five things are explicitly not in scope:

- **Does not derive the topology of T².** Cited from [grid-duality §7.5.1](../grid-duality/07-wrap-promotion-modeling.md). Standard mathematical setup; we use the result.
- **Does not derive crossing-number formulas, knot polynomials, or other topological invariants.** Cited from standard knot-theory references where used.
- **Does not commit to which topological invariants are physically distinguishing.** That is a downstream judgment based on what survives the closure condition (chapter 4) and what corresponds to observed particles.
- **Does not analyze multi-knot energetics or Pauli-like distribution.** Setup only; the analysis is in [metric-binding chapter 3 onwards](../metric-binding/README.md#chapters).
- **Does not derive spin from winding.** Cites [matter-from-light §4](../../papers/matter-from-light.md) where the geometric derivation lives.
- **Does not describe how a knot is dynamically created, destroyed, or transformed.** All processes in this project are linear unitary; topological transitions are forbidden at this level. Non-unitary processes are out of scope.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Are finer invariants (genus, polynomials) physically distinguishing for torus knots, or is (m, n) sufficient? | Chapter 4 + observed inventory; for torus knots specifically, (m, n) determines the others |
| Is the (m, n) → (−m, −n) reflection the matter/antimatter axis, or just orientation reversal of the same particle? | Chapter 6 (handedness and pairs) |
| Does the multi-component k-link give k distinct fractional charges, or one charge of magnitude 1/k per component? | Chapter 8 (fractional charge mechanism) |
| Does Pauli-like distribution of knots emerge from energy minimization on a single sheet? What does the multi-knot energy landscape look like? | metric-binding (multi-knot states) |
| How does one count "how many knots in a particle"? Is what standard physics calls a proton a 3-component link or 3 independent knots or 1 knot with (m, n) ∝ (3, ·)? | metric-binding + downstream MaSt-correspondence work |
| What organizes generation structure — crossing number tier? Specific (m, n) families? | Out of scope for metric-charge; flagged for follow-up |
| What is the relationship between torus-knot tiers and standard particle generations? | Out of scope for metric-charge; flagged for follow-up |
