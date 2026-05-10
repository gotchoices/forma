# work1.md — competing derivation: one gauge field from wrap-order-asymmetric standing-wave construction

**Purpose.** Alternative derivation of how metric-mass's standing-wave-as-particle reading extends to 2D-compact metric-charge. Companion to [work.md](work.md), which arrived at "no gauge field" by applying the metric-mass principle uniformly across both compact directions. This file argues that uniformity is the wrong move: the **wrap-order convention** of [Chapter 1 §10](01-foundation.md) distinguishes the two compact directions (one is *ring*, the other is *tube*), and the standing-wave construction must respect that asymmetry. Doing so yields exactly one gauge field.

**Terminology.** "Wrap-order asymmetry" names *only* the ring-vs-tube role assignment fixed in [Chapter 1 §10](01-foundation.md), inherited from grid-duality's wrap-promotion ladder. It does not refer to any other substrate-level asymmetry the broader framework may invoke (for example, a separate handedness in grid-primitive that might bias matter populations).

**Scope.** The mission is to derive *one* gauge field rather than zero or two. Sections 1–4 establish the algebra. Section 5 introduces the wrap-order asymmetry. Sections 6–8 derive the single gauge field. Section 9 confirms the same principle gives mass-only outcomes for closure-failing modes. Section 10 inventories the result. Interpretive questions outside this mission (matter/antimatter populations, integration with downstream chapters, etc.) are not addressed.

---

## 1. Inherited principle from metric-mass

[metric-mass Chapter 5 §7](../metric-mass/05-metric-self-consistency.md) constructs the rest-mass particle as the equal-amplitude superposition of the +n and −n traveling-wave components on a single compact direction:

<!-- φ = exp(i(k_S S - ωt + nu/R_u)) + exp(i(k_S S - ωt - nu/R_u)) -->
$$
\varphi = e^{i(k_S S - \omega t + n u/R_u)} + e^{i(k_S S - \omega t - n u/R_u)} \;=\; 2\cos(n u/R_u)\,e^{i(k_S S - \omega t)}
$$

The standing wave has T_tu = 0 (the n-linear cross-term cancels) but T_tt and T_uu doubled. Mass survives, the candidate gauge potential cancels.

**The principle this rests on, stated precisely:** A 1D compact loop has u → −u as a *topological symmetry* — it is an unoriented circle, with no internal feature picking out one direction of traversal. The physical particle should inherit this symmetry. Combining ±n is what enforces invariance under u → −u; the cross-term cancellation is the algebraic expression of that invariance.

The principle is *not* "uniformly standing-wave every compact direction." It is "symmetrize over each topological symmetry the configuration actually has."

---

## 2. The 2D-compact setting: four modes per (|m|, |n|)

[Chapter 1 §6](01-foundation.md) gives the manifold M = ℝ × ℝ³ × T² with two compact directions u, w and bare diagonal metric. The wave equation □φ = 0 admits separable traveling-wave modes labeled by signed integers (m, n) ∈ ℤ², with dispersion

<!-- ω² = c²(k_S² + k_u² + k_w²) -->
$$
\omega^2 = c^2\bigl(k_{S}^2 + k_u^2 + k_w^2\bigr),\qquad k_u = \tfrac{2\pi m}{L_u},\;\; k_w = \tfrac{2\pi n}{L_w}
$$

For each pair (|m|, |n|) with both nonzero, four modes share the same |ω|:

| Label | (m, n) | Phase argument |
|---|---|---|
| (++) | (+m, +n) | +k_u u + k_w w − ωt |
| (+−) | (+m, −n) | +k_u u − k_w w − ωt |
| (−+) | (−m, +n) | −k_u u + k_w w − ωt |
| (−−) | (−m, −n) | −k_u u − k_w w − ωt |

Three independent reflections act on this set:

- **R_J: (m, n) ↔ (−m, −n)** — joint sign reversal. Sends (++) ↔ (−−), (+−) ↔ (−+). On the closed curve T(m, n), this is *traversal reversal* — same unoriented curve, opposite direction.
- **R_u: m ↔ −m** — sign of u-winding only. Sends (++) ↔ (−+), (+−) ↔ (−−). On T(m, n), sends T(m, n) → T(−m, n), the u-mirror.
- **R_w: n ↔ −n** — sign of w-winding only. Sends (++) ↔ (+−), (−+) ↔ (−−). On T(m, n), sends T(m, n) → T(m, −n), the w-mirror.

R_u and R_w are *chirality reflections*. Whether each is a topological symmetry of T(m, n) depends on whether the underlying knot is chirally distinct from its mirror in 3-space.

---

## 3. Stress-energy of a single traveling-wave mode

For the (++) mode at rest in 4D (k_S = 0), φ = A·cos(k_u u + k_w w − ωt). Using T_μν = 2|φ|²·k_μ k_ν per metric-mass Ch5 §2 (extended trivially to one more compact direction), with k_μ = (−ω, k_u, k_w):

| Entry | Spatial-temporal-averaged value |
|---|---|
| T_tt | A²·ω²/2 |
| T_uu | A²·k_u²/2 |
| T_ww | A²·k_w²/2 |
| **T_tu** | **−A²·ω·k_u/2** |
| **T_tw** | **−A²·ω·k_w/2** |
| T_uw | A²·k_u·k_w/2 |

Two spacetime↔compact off-diagonals are sourced — T_tu and T_tw. Under linearized Einstein equations these become h_μu and h_μw, satisfying the four standard-physics gauge-potential properties for two independent U(1)s (per current [Chapter 5 §4](05-metric-self-consistency.md)).

Two cross-terms is one too many. The single-mode reading produces both A_μ (from h_μu) and B_μ (from h_μw); standard physics has one EM gauge potential. The standing-wave principle from metric-mass should reduce this. The question is *how much*.

---

## 4. What each candidate symmetrization does

For each of the three reflections, write down the equal-amplitude superposition that enforces invariance under that reflection, and compute what survives.

**Enforce R_J (joint reversal).** Combine (++) + (−−) = 2A·cos(k_u u + k_w w)·cos(ωt). "Directionless standing wave on the specific oriented curve T(m, n)" — the direct 2D analog of metric-mass's standing wave.

- T_tu ∝ ⟨cos·sin in (k_u u + k_w w)⟩ × ⟨sin·cos in t⟩ → both factors average to 0. **T_tu = 0.**
- T_tw → same structure. **T_tw = 0.**
- T_uw ∝ ⟨sin² in (k_u u + k_w w)⟩ × ⟨cos² in t⟩ → both nonzero. **T_uw ≠ 0** (doubled vs single mode).

Mass + chirality-σ (in T_uw), no EM cross-terms. *Both* gauge potentials cancelled.

**Enforce R_u (chirality in u).** Combine (++) + (−+) = 2A·cos(k_u u)·cos(k_w w − ωt). *Standing in u, traveling in w.*

- T_tu ∝ ⟨cos·sin in k_u u⟩ × ⟨cos·sin in (k_w w − ωt)⟩ → first factor averages to 0. **T_tu = 0.**
- T_tw ∝ ⟨cos² in k_u u⟩ × ⟨sin² in (k_w w − ωt)⟩ → both nonzero. **T_tw ≠ 0**, equal to −A²·ω·k_w.
- T_uw → first factor averages to 0. **T_uw = 0.**

Mass + **one EM cross-term in w only**, gauge potential B_μ from h_μw.

**Enforce R_w (chirality in w).** Combine (++) + (+−) = 2A·cos(k_w w)·cos(k_u u − ωt). Standing in w, traveling in u. By the symmetric calculation: **T_tu ≠ 0, T_tw = 0, T_uw = 0.** Mass + one EM cross-term in u only, gauge potential A_μ from h_μu.

Summary:

| Symmetry enforced | Modes combined | T_tu | T_tw | T_uw | Outcome |
|---|---|---|---|---|---|
| R_J | (++) + (−−) | 0 | 0 | nonzero | No EM cross-terms |
| R_u | (++) + (−+) | 0 | **nonzero** | 0 | **One cross-term, in w** |
| R_w | (++) + (+−) | **nonzero** | 0 | 0 | One cross-term, in u |

Three constructions, three different cross-term inventories. The math is unambiguous; what differs is *which symmetry to enforce*. work.md's mistake was to default to R_J uniformly (the metric-mass principle imported wholesale) and conclude that the framework cannot produce charge. The correct question is which of the three reflections is a topological symmetry the configuration actually has — and that depends on the wrap-order.

---

## 5. The wrap-order asymmetry selects R_u

The bare manifold T² is symmetric in (u, w): the metric is diagonal with no preferred direction, and the wave equation treats u and w identically. *On the bare manifold alone*, all three reflections are equally available, and the framework would have to make an interpretive choice between them.

The asymmetry comes from the wrap-order convention. Per [Chapter 1 §10](01-foundation.md):

> **u = ring** (mass-bearing, multi-wrap structure)
> **w = tube** (charge-bearing, single-wrap structure for primitives)

This is not a labeling preference — it is inherited from [grid-duality](../grid-duality/)'s wrap-promotion ladder, where L0→L1 (which gives the ring direction) and L1→L2 (which gives the tube direction) are *structurally distinct* operations. Once the wrap-order is fixed, u and w are no longer interchangeable.

What the wrap-order asymmetry says about the three reflections requires distinguishing two notions of symmetry:

- **Topological symmetry of the curve.** Whether R takes T(m, n) to itself as a knot in 3-space.
- **Particle symmetry of the construction.** Whether R is enforced as a symmetrization in the natural-particle definition (i.e., whether modes are combined in equal amplitude under R).

For closure-satisfying T(m, 1) — the unknot — *both* R_u and R_w are topological symmetries of the curve in 3-space (the unknot is achiral; reflecting it in either compact direction takes it to itself up to ambient isotopy). Topology alone does not distinguish them. The wrap-order's role is to single out *which* of the two chirality reflections gets enforced as a particle symmetry:

- **R_u (chirality reflection of the ring) — particle symmetry.** The wrap-order assigns the ring direction the metric-mass-style symmetric role: standing-wave construction in the ring, with the ring's chirality treated as a particle symmetry. Ring-direction wavenumber sign carries no observable.
- **R_w (chirality reflection of the tube) — *not* a particle symmetry.** The wrap-order assigns the tube direction the KK-style charge-bearing role: the sign of compact-direction wavenumber is a physical observable (charge). R_w would flip that sign and so cannot be enforced as a symmetrization, even though it remains a topological symmetry of the unknot.
- **R_J = R_u · R_w — *not* a particle symmetry.** Since R_w is not a particle symmetry, R_J is also not. Enforcing R_J overshoots — it cancels both cross-terms, including the one the wrap-order says should survive.

The distinction is sourced from the wrap-order, not from topology alone. The "two candidates, rule one out" framing is settled here: R_u is the wrap-order-aligned reflection (ring direction has no observable sign → standing-wave construction is natural); R_w is the alternative ruled out (tube direction has definite charge sign → cannot be symmetrized away); R_J is ruled out as overshoot.

---

## 6. The natural particle on closure-satisfying T(m, 1)

Closure-satisfying primitives are T(m, 1) — m wraps in ring, 1 wrap in tube — per [Chapter 4 §2](04-the-closure-condition.md). One topological fact about these curves matters here:

**Fact: T(m, 1) is the unknot in 3-space.** Per [Chapter 3 §7](03-knots-on-the-torus.md), any T(p, q) with one winding equal to ±1 is topologically trivial (the unknot). The unknot is *achiral* — isotopic to its mirror image in 3-space. So T(m, 1) and its u-mirror T(−m, 1) are the same knot in 3-space.

This validates the wrap-order's claim that R_u is a topological symmetry: the ring-direction reflection takes T(m, 1) to itself as a knot in 3-space. For closure-satisfying modes specifically, the wrap-order's selection of R_u as the symmetrizer of the ring is also a topological claim — the underlying knot doesn't distinguish R_u-related configurations.

The natural particle construction for closure-satisfying T(m, 1) is the **R_u-symmetrized** combination:

<!-- φ_+ = 2 cos(k_u u) cos(k_w w - ωt) -->
$$
\varphi = (++) + (-+) \;=\; 2A\cos(k_u u)\cos(k_w w - \omega t)
$$

*Standing in u (ring), traveling in w (tube).* By §4: T_tu = 0, T_tw ≠ 0, T_uw = 0. **Exactly one gauge potential**, B_μ from h_μw.

The ruled-out alternative is **(++) + (+−)** — chirality-conjugate in *w* (tube), keeping +m definite. This would standing-wave the tube and travel the ring, giving T_tu instead of T_tw. The wrap-order convention rules it out: it would invert the ring/tube role assignment. By inspection, it inverts the framework's own labels.

(The R_u-symmetrized construction has a sign-of-n sibling — namely (+−) + (−−), which has definite −k_w and produces T_tw with opposite sign. The math admits both as valid R_u-symmetrized constructions on the same knot. Whether and how this pair structure should be interpreted physically is outside the scope of this derivation.)

---

## 7. Stress-energy of the natural particle, explicitly

Compute T_μν for φ = 2A cos(k_u u) cos(k_w w − ωt) at rest in 4D. Derivatives:

- ∂_t φ = +2A·ω·cos(k_u u)·sin(k_w w − ωt)
- ∂_u φ = −2A·k_u·sin(k_u u)·cos(k_w w − ωt)
- ∂_w φ = −2A·k_w·cos(k_u u)·sin(k_w w − ωt)

Spatial-temporal averages (using ⟨cos²⟩ = ⟨sin²⟩ = 1/2 and ⟨sin·cos⟩ = 0 over a full period):

| Entry | Average |
|---|---|
| T_tt | A²·ω² |
| T_uu | A²·k_u² |
| T_ww | A²·k_w² |
| T_tu | **0** (cos·sin in u → 0) |
| T_tw | **−A²·ω·k_w** |
| T_uw | **0** (cos·sin in u → 0) |

The three off-diagonals reduce to one nonzero entry: **T_tw = −A²·ω·k_w**, doubled relative to a single traveling-wave mode (which would give −A²·ω·k_w/2). Diagonal entries are also doubled, giving the rest-mass contribution

<!-- m² c² = (ℏk_u)² + (ℏk_w)² -->
$$
m_\text{rest}^2 c^2 \;=\; (\hbar k_u)^2 + (\hbar k_w)^2
$$

— the metric-mass mass formula extended to two compact directions, with both ring and tube contributing to rest energy.

---

## 8. KK consistency

Standard 5D KK ([primers/kaluza-klein.md](../../primers/kaluza-klein.md)) has 4D extended spacetime + 1 compact direction. It treats a particle with definite compact-direction wavenumber n; the cross-term g_μ5 = A_μ is the gauge potential, charge is q ∝ n, Maxwell's equations follow from 5D Einstein equations. KK does *not* standing-wave the compact direction — the particle has definite n, and the cross-term survives precisely because it does.

In our 2D-compact construction, the **tube direction (w) plays the role of standard KK's single compact direction.** The natural particle has definite n, the wave is traveling in w, and the cross-term h_μw = B_μ survives — standard KK applied to the tube.

The **ring direction (u) plays the role of metric-mass's single compact direction.** The natural particle has the standing-wave structure cos(k_u u), the wave is *not* traveling in u, and the would-be cross-term h_μu cancels — metric-mass applied to the ring.

The 2D-compact T² is decomposed by the wrap-order into "1D-compact for KK + 1D-compact for mass-only." Neither mechanism contradicts the other because they apply to different directions. The choice of which direction is which is forced by the wrap-order, which is fixed once for the framework as a whole and applies the same way to all modes. No new principles, no per-particle interpretive moves — standard KK on the tube, metric-mass on the ring.

---

## 9. Closure-failing modes — confirming the principle

For closure-failing configurations, the topological status of R_u and R_w changes, and the natural particle construction follows the same principle (enforce only the topological symmetries the configuration actually has). Both yield mass-only outcomes, confirming the construction isn't ad hoc.

### 9.1 Single-axis modes

Modes (m, 0) or (0, n) — one winding zero. Take (m, 0):
- The wave has no w-dependence; reflections in w act trivially.
- R_u (sign of m) is the only nontrivial reflection.
- Natural particle: (++) + (−+) → 2A·cos(k_u u)·cos(ωt). Metric-mass's standing wave restricted to u, with no w-structure.
- T_tu = 0 (R_u cancellation), T_tw = 0 (k_w = 0), T_uw = 0. **Mass only.**

(0, n) gives mass-only by the symmetric calculation in w.

### 9.2 Genuine torus knots

For T(p, q) with p, q ≥ 2 and gcd(p, q) = 1, the curve is a *genuine* torus knot — chirally distinct from its mirror.

- **R_u changes the knot type.** T(p, q) and T(−p, q) are mirror-chirality torus knots, distinct in 3-space. R_u is *not* a topological symmetry.
- **R_w changes the knot type.** Similarly distinct. R_w is *not* a topological symmetry.
- **R_J = R_u · R_w preserves the knot type.** T(p, q) and T(−p, −q) are the same unoriented curve. R_J *is* a topological symmetry.

The only available symmetry is R_J. Natural particle: (++) + (−−). By §4's R_J row: **T_tu = 0, T_tw = 0, T_uw ≠ 0.** Mass + chirality field (in T_uw), no EM cross-terms.

### 9.3 Why closure-satisfying and closure-failing diverge

For closure-satisfying T(m, 1), the underlying curve is achiral in 3-space, so its chirality reflections (both R_u and R_w) are topological symmetries; R_u in particular is among them, and the wrap-order's selection of R_u as the particle symmetry is consistent with topology. For genuine torus knots, the underlying curve is chiral, so neither R_u nor R_w is a topological symmetry; R_u cannot be enforced as a particle symmetry without combining topologically distinct configurations. The construction falls back to R_J (the only remaining topological symmetry — joint reversal preserves the unoriented curve), yielding the mass-only configuration.

The closure rule, properly stated, has two parts:

> T(m, n) is closure-satisfying iff
>
> (i) the curve is *achiral* in 3-space — its chirality reflections are topological symmetries of the curve — *and*
>
> (ii) the wrap-order's ring-direction reflection R_u is among those topological symmetries.
>
> For genuine torus knots, (i) fails. For unknots and their multi-links, (i) holds and (ii) is automatic (R_u is one of the two chirality reflections, and if all of them are topological symmetries, R_u is among them).

Within the torus-knot family that T² admits, the criterion reduces to "the gcd-reduced primitive has tube winding 1," producing the same partition the synchronization rule produces. The unknot status is a *consequence* of (i) in our specific manifold setting, not the criterion itself — the same achirality test would extend naturally to other manifolds where non-torus closed curves could be embedded (e.g., the amphicheiral figure-eight knot would qualify on (i) grounds if it could be embedded), with the wrap-order's role in (ii) selecting which particle symmetry to enforce.

**The closure rule and the gauge-promotion mechanism agree because they are descriptions of the same underlying fact:** the curve's achirality permits the wrap-order's R_u to be enforced as a particle symmetry, which is what produces the single surviving cross-term.

---

## 10. Inventory under this reading

| Configuration | Topological character | Particle symmetry | Cross-terms sourced | Type |
|---|---|---|---|---|
| Light (0, 0) | No curve | — | None | Light |
| Single-axis (m, 0) or (0, n) | Trivial cycle | R_u or R_w (only one available) | None | Mass-only |
| T(m, 1) primitive | Achiral closed curve in 3-space (unknot, in our setting) | R_u (wrap-order-aligned with chirality) | **T_tw alone** | **Mass + 1 gauge field B_μ** |
| Multi-link k × T(m, 1) | k components, each achiral | R_u per component | T_tw per component | Mass + charge (k components) |
| T(p, q), p, q ≥ 2, gcd = 1 | Chirally-distinct closed curve (genuine torus knot) | R_J only | T_uw only (no EM) | Mass + chirality |

Closure-satisfying configurations carry one gauge potential apiece; closure-failing carry none. The "two-U(1)s puzzle" of the current [Chapter 5 §8](05-metric-self-consistency.md) dissolves: the single-mode reading produces two candidate U(1)s, but the natural particle (R_u-symmetrized) sources only one. The other compact direction's would-be gauge potential is cancelled by the metric-mass mechanism, exactly as in 1D-compact.

The mission — derive *one* gauge field rather than zero or two — is complete. The construction rests on the wrap-order asymmetry alone (no new principles), produces standard KK structure on the tube and standard metric-mass structure on the ring, and matches the closure rule's own partition of (m, n) modes by the same topological criterion.

---

## 11. Consequential changes to the rest of the project

Adopting this derivation as the canonical chapter-5 mechanism implies a coordinated set of changes elsewhere in the project. The goal is a smooth, cohesive presentation in which the chapters reference each other through a single consistent framing — not a hodgepodge of layered modifications. The changes below are organized by chapter and identified as either *content* changes (the math or partition shifts), *framing* changes (the rationale shifts but the conclusions stand), or *editorial* changes (terminology and consistency fixes).

### 11.1 Chapter 1 §10 — closure condition

Two changes, both substantive: a content-touching convention swap and a framing reframe.

**Content: convention swap.** The current text has line 330's closure formula treating u as the tube (the formula reads "tube crosses zero (modulo L_u) at s = j/m"), while line 338's convention statement says u = ring. Adopt line 338's convention consistently — u is the ring (mass-bearing, multi-wrap), w is the tube (charge-bearing, single-wrap). This matches metric-mass's use of u as mass generator and resolves the internal contradiction.

Under this convention, the closure formula is restated with ring (u) carrying m wraps and tube (w) carrying n wraps; the closure rule reads **n | m** (tube wraps divide ring wraps, with both nonzero), and the closure-satisfying primitives are **T(m, 1)** rather than T(1, q).

This is a labeling change that propagates through every chapter's examples and inventory tables — mechanical but not local. The partition of *physical configurations* into charged-vs-neutral is preserved; the (m, n) integer labels naming each configuration change. A configuration formerly labeled (1, q) — one wrap in the formerly-tube, q wraps in the formerly-ring — is the same physical configuration now labeled (q, 1) under the new convention (q wraps in the new ring u, one wrap in the new tube w). Each (m, n)-labeled example in Chapters 1, 3, 4, 6, 8, and the README must be updated. See §11.2 for Chapter 4's relabeling load specifically — that chapter has the most examples.

**Framing: rationale is a chirality condition.** The current §10 grounds the closure rule in *phase synchronization*. The deeper grounding is in *chirality of the closed curve*: the closure rule selects exactly those (m, n) for which the chirality reflection of the ring direction (R_u) is a topological symmetry of the curve in 3-space. The synchronization view becomes an equivalent operational test (within the torus-knot family); the chirality view becomes the primary explanation because it ties directly to why one gauge field emerges (rather than zero or two) — see §§5–8 above.

Reframed statement of the closure rule:

> A configuration T(m, n) is closure-satisfying if and only if the chirality reflection of the ring direction (R_u: m ↔ −m) is a topological symmetry of the closed curve T(m, n) in 3-space.
>
> Within the torus-knot family realizable on T², this reduces to: T(m, n) is closure-satisfying iff its gcd-reduced primitive has tube winding 1 (T(m', 1) form). The synchronization condition n | m is an equivalent operational test.

The chirality framing makes clear that the rule is not fundamentally about "unknot status" — it is a symmetry condition that, applied to any T(m, n), produces a definite yes/no answer. For the torus knots that T² admits, the criterion happens to select unknots and their multi-links. The criterion itself is general.

### 11.2 Chapter 4 — the closure condition

**Structural rewrite of the central argument plus convention-swap relabeling.** Not "framing only" — the chapter's prose flow shifts to lead with the chirality view, and every (m, n)-labeled example in §§4.1–4.4 needs the convention-swap relabeling per §11.1.

**Preserve at the partition level.** The five-row partition (light, single-axis, weak-knot diagonal, genuine-knot diagonal, multi-component link), the inventory of closure-satisfying primitives and their multi-links, and the identification of genuine torus knots and single-axis modes as closure-failing. Physical content unchanged.

**Promote chirality to primary.** Chapter 4 currently builds its central argument around the synchronization framing — the phase-pattern view as the load-bearing derivation. Under the rewrite, the chirality view becomes primary: closure-satisfying iff the curve is achiral in 3-space and the wrap-order's R_u is among its topological symmetries (per §9.3 here). The synchronization condition becomes a *derived equivalent test* — an operational way to check the chirality criterion in concrete cases. The topological view (gcd-reduced primitive form) remains a structural description. This is a rewrite of the chapter's argument flow, not an additive third view alongside two existing ones.

**Relabel every example.** Per §11.1, each (m, n) example in Chapter 4 requires the convention swap. The closure-satisfying primitive form changes from T(1, q) throughout to T(m, 1), and "m | n" becomes "n | m." The §§4.1–4.4 inventory tables and worked examples are mechanically updated.

**Resolve §6.3's open question.** The chapter currently flags an open question about whether the metric-side analysis is "broader than" or "equivalent to" the synchronization rule. Under work1, this is resolved: the metric-side analysis under the wrap-order-asymmetric construction is exactly equivalent to the closure rule, because both are descriptions of the same chirality condition. The §6.3 hedging is removed; the equivalence is asserted.

### 11.3 Chapter 5 — metric self-consistency and gauge promotion

Major content rewrite — this is where the work1 derivation lives.

**Replace.** The current §§4–8 build up two U(1) gauge potentials (A_μ from h_μu, B_μ from h_μw) and acknowledge the resulting "two-U(1)s puzzle" against standard physics. work1 derives a single gauge field via the wrap-order-asymmetric standing-wave construction. The current §§4–8 should be replaced with the work1 derivation, restructured for chapter pacing but preserving the algebra of work1 §§3–4 (single-mode stress-energy and the three candidate symmetrizations).

**Preserve.** §§1–3 (introduction, single-mode stress-energy, off-diagonal sourcing under linearized Einstein equations) are largely unchanged at the math level. The framing shifts from "two cross-terms is the *result*" toward "two cross-terms is the per-component intermediate that the standing-wave construction reduces to one." §7 (the holonomy mechanism) survives the rewrite with minor adjustments — the chain operates on the single surviving gauge potential rather than on two.

**Fold §6.5 into the new derivation.** §6.5 (the four conventions reduce) was added in a previous editing pass to resolve review item M1. Under work1, the §6.5 demonstration is implicit in the derivation itself: convention 4 (gauge identification) is a direct *consequence* of the wrap-order's selection of R_u — once the wrap-order fixes which direction is the ring, the surviving cross-term is automatically in the tube. A standalone §6.5 alongside the new derivation would be redundant. Fold its content in: the work1 derivation makes the alignment of the wrap-order's three faces (closure rule, aspect-ratio labels, gauge identification) explicit at the construction stage, replacing the freestanding §6.5 demonstration.

§8 (what the framework reproduces) drops the "two-U(1)s differ from standard physics" caveat. The framework now produces one U(1) per charged particle, matching standard EM at the structural level. The remaining open issues (numerical α, nonlinear backreaction) are unaffected.

### 11.4 Chapter 6 — handedness and pairs

Framing sharpening; preserve content.

The chapter develops handedness via σ_uw shear breaking a chirality reflection. Under work1, the σ_uw cross-term k_u·k_w transforms under the three reflections as:

- **Invariant under R_J** (joint sign flip) — both k_u and k_w flip, product unchanged.
- **Flips sign under R_u** (u-only) — k_u flips, k_w fixed.
- **Flips sign under R_w** (w-only) — k_w flips, k_u fixed.

This sharpens the existing Ch 6 §6 / Ch 8 §3 finding that σ_uw breaks chirality (not sign reflection) into a pair of definite claims under work1's framing:

- **σ_uw does not bias matter/antimatter populations.** Since σ_uw is invariant under R_J, and R_J is the matter/antimatter operation under work1's natural-particle construction, σ_uw shifts matter and antimatter rest energies *equally*. It cannot bias their populations at the dispersion level. Whatever produces the universe's matter excess, it is not σ_uw.
- **σ_uw biases chirality within particles.** Since σ_uw flips sign under R_u, it shifts the energies of the (++) and (−+) components of an R_u-symmetrized natural particle in opposite directions, biasing their internal amplitude balance. Within an antimatter particle, σ_uw biases (+−) vs (−−) similarly. This is *intra-particle chirality bias*, not a population mechanism.

**Update.** The chapter currently leaves σ_uw's role partly hedged ("a candidate matter/antimatter mechanism"). Under work1, the math is sharper than the hedging suggests: σ_uw is *clearly* a chirality-bias mechanism within particles, not a matter/antimatter-bias mechanism. The candidate-mechanism language is removed; the role is committed to.

**Preserve.** The chapter's §4 (the four neutrality mechanisms) — including the cancellation-pair mechanism, which under work1 is a special case of the natural-particle construction where two R_u-symmetrized configurations of opposite tube-direction sign form a bound pair with cross-terms summing to zero net charge.

**Do not commit on matter/antimatter origin.** What does bias matter over antimatter populations is not addressed by σ_uw under work1, and work1 itself does not derive it. The matter/antimatter origin question is recorded as open and forwarded to a separate substrate-level mechanism (e.g., handedness in grid-primitive). The sign-of-n alternative within R_u-symmetrized pairs is a structural feature of the construction; whether it corresponds to physical matter and antimatter, and what populates one over the other, remain outside the scope of this derivation.

### 11.5 Chapters 2, 3, 7, 8

These chapters are largely independent of the gauge-field count, but several need the convention-swap relabeling per §11.1.

**Chapter 2 (modes on a sheet).** No content changes. The mode structure (separable traveling-wave modes labeled by (m, n)) is the foundation work1 builds on. Convention-swap impact is minimal — Chapter 2 doesn't pin specific (m, n) configurations as charged-vs-neutral.

**Chapter 3 (knots on the torus).** Mechanical relabeling of every (m, n) example. The knot inventory and topological partition (genuine torus knots vs unknots vs links) is unchanged; the (m, n) labels naming each row of the inventory tables are swapped per §11.1. This is straightforward but extensive — every figure caption and example T(p, q) needs the convention applied.

**Chapter 7 (aspect ratio).** Verify the energetics of closure-satisfying primitives (now T(m, 1) form) under the new convention. Aspect-ratio analysis itself is preserved; example labels updated.

**Chapter 8 (shear and fractional charge).** σ_uw analysis is preserved and sharpened per §11.4 (chirality-bias not matter/antimatter-bias). Fractional-charge predictions (1/3, 2/3 fractions for k-component multi-links) survive at the numeric level — they emerge from the R_u-symmetrized construction applied per component of a k×T(m, 1) link. Multi-link example labels updated.

### 11.6 README, STATUS, review.md

**README, STATUS.** Update the headline framing: replace the previous "framework structurally has two U(1)s, one observed" caveat with "framework produces one U(1) per charged particle, matching standard physics." Update example (m, n) configurations per §11.1's convention swap. The status of the alpha-derivation track is unchanged.

**review.md — explicit finding-by-finding mapping under adoption of work1:**

- **M1 (four conventions reduce).** Folded into the work1 derivation per §11.3 — convention 4 (gauge identification) becomes a consequence of the wrap-order's R_u selection rather than an independent stipulation. The standalone §6.5 demonstration is removed.
- **M2 (gauge-property test).** The four-property test of standard-physics gauge-potential structure now applies to the *single* surviving gauge potential h_μw, not to two. Test is simpler and more directly defensible. Whether to actually carry out the explicit Property-4 geodesic expansion is a scope question unchanged by work1.
- **M3 (two U(1)s).** Resolved by adopting work1. The framework now produces one gauge potential per closure-satisfying particle.
- **σ_uw chirality finding (formerly TODO-S4 / Ch 6 §6 rewrite).** Already implemented in the existing Ch 6 / Ch 8 rewrites; under work1 it becomes the natural reading rather than a flagged correction. Sharpened per §11.4 — σ_uw is a chirality-bias mechanism within particles, not a matter/antimatter-bias mechanism.
- **M7 (residual promotion language).** Unaffected by work1.
- **M8 (chapter 8 outline status).** Unaffected by work1.
- **N2 (infinite tower of mass-only torus knot states).** Unaffected by work1; the genuine-torus-knot mass-only category remains and continues to predict an infinite tower of mass-only states.
- **L5 (charge-sign assignments for fractional charges).** Unaffected by work1; the fractional-charge predictions for k-component multi-links survive numerically per §11.5.

### 11.7 Cohesion target

Applied as a coordinated edit pass, the project should read as a single arc:

1. **Chapter 1** establishes the manifold, the wrap-order convention (u = ring, w = tube), and a *chirality-based* closure condition.
2. **Chapter 2** develops the mode structure on T².
3. **Chapter 3** classifies the resulting closed curves as torus knots and links.
4. **Chapter 4** identifies which mode classes are closure-satisfying, with three equivalent views (chirality, topological, synchronization).
5. **Chapter 5** derives the single gauge field via wrap-order-asymmetric standing-wave construction, with the chirality condition serving as the structural reason.
6. **Chapter 6** develops handedness, σ_uw shear, and the four neutrality mechanisms — all consistent with the wrap-order framing.
7. **Chapter 7** examines aspect-ratio dependence.
8. **Chapter 8** addresses shear and fractional charge for multi-component links.

Each chapter's local content is largely preserved; the connecting tissue is rewritten so the chapters reference each other through the chirality framing rather than through the older synchronization-only framing. The overall progression — from manifold to modes to knots to closure to gauge to handedness to fractional charge — remains intact, and the "two-U(1)s puzzle" disappears from the framework's self-presentation.
