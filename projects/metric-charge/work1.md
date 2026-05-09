# work1.md — competing derivation: one gauge field from wrap-order-asymmetric standing-wave construction

**Purpose.** Alternative derivation of how metric-mass's standing-wave-as-particle reading extends to 2D-compact metric-charge. Companion to [work.md](work.md), which arrived at "no gauge field" by applying the metric-mass principle uniformly across both compact directions. This file argues that uniformity is the wrong move: the **wrap-order convention** of [Chapter 1 §10](01-foundation.md) distinguishes the two compact directions (one is *ring*, the other is *tube*), and the standing-wave construction must respect that asymmetry. Doing so yields exactly one gauge field, on solid topological and wrap-order-level grounds.

**Terminology.** The asymmetry this file relies on is the **wrap-order asymmetry**: the substrate-level fact, fixed in [Chapter 1 §10](01-foundation.md) and inherited from grid-duality's wrap-promotion ladder, that one compact direction plays the *ring* role and the other plays the *tube* role. This is distinct from any other substrate-level asymmetry the broader framework may invoke (for example, a separate handedness in grid-primitive that biases matter populations over antimatter). Throughout this file, "wrap-order asymmetry" names *this specific* ring-vs-tube role assignment, and nothing else.

**Discipline:** math first, interpretation second. Sections 1–4 establish the algebra. Section 5 introduces the wrap-order asymmetry. Sections 6–9 derive the particle construction and verify its KK consistency. Section 10 covers closure-failing modes and matter/antimatter.

---

## 1. Inherited principle from metric-mass — restated precisely

[metric-mass Chapter 5 §7](../metric-mass/05-metric-self-consistency.md) constructs the rest-mass particle as the equal-amplitude superposition of the +n and −n traveling-wave components on a single compact direction:

<!-- φ = exp(i(k_S S - ωt + nu/R_u)) + exp(i(k_S S - ωt - nu/R_u)) -->
$$
\varphi = e^{i(k_S S - \omega t + n u/R_u)} + e^{i(k_S S - \omega t - n u/R_u)} \;=\; 2\cos(n u/R_u)\,e^{i(k_S S - \omega t)}
$$

The standing wave has T_tu = 0 (the n-linear cross-term cancels) but T_tt and T_uu doubled. Mass survives, the candidate gauge potential cancels. metric-mass produces *mass*, not charge.

**The principle this rests on, stated precisely:** A 1D compact loop has u → −u as a *topological symmetry* — it is an unoriented circle, and there is no internal feature picking out one direction of traversal. The physical particle should inherit this symmetry. Combining ±n is what enforces invariance under u → −u; the cross-term cancellation is the algebraic expression of that invariance.

The principle is *not* "uniformly standing-wave every compact direction." It is "symmetrize over each topological symmetry the configuration actually has."

This distinction is the entire content of work1.md.

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

- **R_J: (m, n) ↔ (−m, −n)** — joint sign reversal. Sends (++) ↔ (−−), (+−) ↔ (−+). On the closed curve T(m, n), this is *traversal reversal* — same unoriented curve, opposite direction. Always a topological symmetry (the curve is unoriented).
- **R_u: m ↔ −m** — sign of u-winding only. Sends (++) ↔ (−+), (+−) ↔ (−−). On T(m, n), this is reflection in u — sends T(m, n) → T(−m, n), the u-mirror of the curve.
- **R_w: n ↔ −n** — sign of w-winding only. Sends (++) ↔ (+−), (−+) ↔ (−−). On T(m, n), this is reflection in w — sends T(m, n) → T(m, −n), the w-mirror.

R_u and R_w are *chirality reflections*. Whether either is a topological symmetry of T(m, n) depends on whether the underlying knot is chirally distinct from its mirror in 3-space.

---

## 3. Stress-energy of a single traveling-wave mode — the per-component intermediate

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

Two cross-terms is one too many. The single-mode reading produces both A_μ (from h_μu) and B_μ (from h_μw); standard physics has one EM gauge potential.

The standing-wave principle from metric-mass should reduce this. The question is *how much*.

---

## 4. What each candidate symmetrization does to the cross-terms

For each of the three reflections, write down the equal-amplitude superposition that enforces invariance under that reflection, and compute what survives.

**Enforce R_J (joint reversal).** Combine (++) + (−−):

<!-- φ_J = 2 cos(k_u u + k_w w) cos(ωt) -->
$$
\varphi_J = A\bigl[\cos(k_u u + k_w w - \omega t) + \cos(-k_u u - k_w w - \omega t)\bigr] = 2A\cos(k_u u + k_w w)\cos(\omega t)
$$

This is the "directionless standing wave on the specific oriented curve T(m, n)" — the direct 2D analog of metric-mass's standing wave. Cross-terms:

- T_tu ∝ ⟨cos·sin in (k_u u + k_w w)⟩ × ⟨sin·cos in t⟩ → both factors average to 0. **T_tu = 0.**
- T_tw → same structure. **T_tw = 0.**
- T_uw ∝ ⟨sin² in (k_u u + k_w w)⟩ × ⟨cos² in t⟩ → both nonzero. **T_uw ≠ 0** (doubled vs single mode).

Mass + chirality-σ (in T_uw), no EM cross-terms. *Both* gauge potentials cancelled.

**Enforce R_u (chirality in u).** Combine (++) + (−+):

<!-- φ_u = 2 cos(k_u u) cos(k_w w - ωt) -->
$$
\varphi_u = A\bigl[\cos(k_u u + k_w w - \omega t) + \cos(-k_u u + k_w w - \omega t)\bigr] = 2A\cos(k_u u)\cos(k_w w - \omega t)
$$

*Standing in u, traveling in w.* The wave is "directionless in u" but carries definite phase advance in w. Cross-terms:

- T_tu ∝ ⟨cos·sin in k_u u⟩ × ⟨cos·sin in (k_w w − ωt)⟩ → first factor averages to 0. **T_tu = 0.**
- T_tw ∝ ⟨cos² in k_u u⟩ × ⟨sin² in (k_w w − ωt)⟩ → both nonzero. **T_tw ≠ 0**, equal to −A²·ω·k_w (after factor-counting).
- T_uw ∝ ⟨cos·sin in k_u u⟩ × ⟨cos·sin in (k_w w − ωt)⟩ → first factor averages to 0. **T_uw = 0.**

Mass + **one EM cross-term in w only**, ie. one gauge potential B_μ from h_μw.

**Enforce R_w (chirality in w).** Combine (++) + (+−):

<!-- φ_w = 2 cos(k_w w) cos(k_u u - ωt) -->
$$
\varphi_w = 2A\cos(k_w w)\cos(k_u u - \omega t)
$$

Standing in w, traveling in u. By the symmetric calculation: **T_tu ≠ 0, T_tw = 0, T_uw = 0.** Mass + one EM cross-term in u only, gauge potential A_μ from h_μu.

The three constructions and their cross-term inventories:

| Symmetry enforced | Modes combined | T_tu | T_tw | T_uw | Reading |
|---|---|---|---|---|---|
| R_J (joint reversal) | (++) + (−−) | 0 | 0 | nonzero | Mass + chirality, no charge |
| R_u (chirality in u) | (++) + (−+) | 0 | **nonzero** | 0 | **Mass + one charge under B_μ** |
| R_w (chirality in w) | (++) + (+−) | **nonzero** | 0 | 0 | Mass + one charge under A_μ |

Three constructions, three different physical particles. The math is unambiguous; what differs is *which symmetry to enforce*. work.md's mistake was to default to R_J uniformly (the metric-mass principle imported wholesale) and then conclude "the framework cannot produce charge." The answer is that R_J is not the right symmetry to enforce in the 2D case, because R_J is not the only topological symmetry available, and on closure-satisfying configurations it is not even the *correct* one.

---

## 5. The wrap-order asymmetry distinguishes u and w

The bare manifold T² is symmetric in (u, w): the metric is diagonal with no preferred direction, and the wave equation treats u and w identically. *On the bare manifold alone*, all three of R_J, R_u, R_w are equally available symmetries, and the framework would have to make an interpretive choice between them (which is where work.md got stuck).

The asymmetry comes from the wrap-order convention. Per [Chapter 1 §10](01-foundation.md), one direction is *adopted* as the **tube** (the 2π-winding direction whose modes carry charge) and the other as the **ring** (where mass arises from standing-wave structure). Per the convention adopted in [Chapter 1 §10 line 338](01-foundation.md):

> **u = ring** (mass-bearing, multi-wrap structure)
> **w = tube** (charge-bearing, single-wrap structure for primitives)

This is not a rendering choice or a labeling preference — it is inherited from [grid-duality](../grid-duality/)'s wrap-promotion ladder, where L0→L1 (which gives the ring direction) and L1→L2 (which gives the tube direction) are *structurally distinct* operations. Once the wrap-order is fixed, u and w are no longer interchangeable.

What the wrap-order asymmetry says about reflections:

- **R_u acts on the ring direction.** The ring is the "mass" direction — the direction analogous to metric-mass's single u-loop. Just as metric-mass's u-loop has u → −u as a topological symmetry (unoriented circle), so does our ring direction. R_u *is* a topological symmetry of the configuration the wrap-order distinguishes.
- **R_w acts on the tube direction.** The tube is the "charge promotion" direction — the direction analogous to KK's compact circle. KK's compact direction does *not* have w → −w as a particle symmetry, because the sign of compact-direction wavenumber is the charge sign and a charged particle has definite charge. R_w is *not* a topological symmetry of a charged particle's configuration.
- **R_J = R_u · R_w.** Since R_w is not a particle symmetry, R_J is also not (it is the product of a true symmetry and a non-symmetry). Enforcing R_J is enforcing more than the wrap-order warrants for a charged particle.

A useful framing of this asymmetry: *metric-mass has a single symmetric loop, where going one way is identical to the other; a knot in 2D is not symmetrical, so there are two candidates for which symmetry to enforce and one must be ruled out.* The "single symmetric loop" of metric-mass corresponds to our **ring direction** (u): symmetric, R_u is a particle symmetry. The "knot in 2D not being symmetrical" corresponds to our **tube direction** (w): not symmetric in the relevant sense, R_w is not a particle symmetry.

---

## 6. The natural particle on closure-satisfying T(m, 1)

Apply the wrap-order-aware principle to closure-satisfying T(m, 1) — the canonical primitive (m wraps in ring, 1 wrap in tube) per [Chapter 4 §2](04-the-closure-condition.md). Two facts about this curve:

**Fact A: T(m, 1) is the unknot in 3-space.** Per [Chapter 3 §7](03-knots-on-the-torus.md), any T(p, q) with one winding equal to ±1 is topologically trivial (the unknot). The unknot is *achiral* — it is isotopic to its mirror image in 3-space. So T(m, 1) and its u-mirror T(−m, 1) are the same knot in 3-space, just embedded with different orientation.

This validates the wrap-order's claim that R_u is a topological symmetry: the ring-direction reflection takes T(m, 1) to itself (as a knot in 3-space). For closure-satisfying modes specifically, the wrap-order's selection of R_u as the symmetrizer of the ring direction is *also* a topological claim — the underlying knot doesn't distinguish R_u-related configurations.

**Fact B: R_w is not a topological symmetry — even for the unknot — because of the wrap-order.** It is true that T(m, 1) and T(m, −1) are *both* unknots and therefore topologically equivalent as knots in 3-space. But they are *distinct oriented configurations* on T², and the wrap-order assigns charge to the sign of the tube-direction circulation. R_w flips that sign — it sends a "positive-charge" configuration to a "negative-charge" configuration. These are physically distinct (matter and antimatter), so R_w is not a particle symmetry.

The natural particle construction for closure-satisfying T(m, 1) is therefore the **R_u-symmetrized, definite-tube-direction** combination:

<!-- φ_+ = 2 cos(k_u u) cos(k_w w - ωt) -->
$$
\varphi_+ = (++) + (-+) \;=\; 2A\cos(k_u u)\cos(k_w w - \omega t)
$$

*Standing in u (ring), traveling in w (tube).*

This is the chirality-conjugate construction in u, with definite +n in w. By §4's table:

- T_tu = 0 (the cross-term in the ring direction cancels — metric-mass mechanism applies in u)
- **T_tw ≠ 0** (the cross-term in the tube direction survives — KK mechanism applies in w)
- T_uw = 0 (the ring-tube cross also cancels)
- T_tt, T_uu, T_ww all nonzero

**Exactly one gauge potential**, B_μ from h_μw, in the tube direction. Mass from the diagonal entries. The matter/antimatter axis is the sign of n (covered in §10).

The ruled-out alternative is **{(++), (+−)}** — chirality-conjugate in *w* (tube), keeping +m definite. This would standing-wave the tube and travel the ring, giving T_tu instead of T_tw. The wrap-order convention rules it out: it would invert the assignment "ring carries mass, tube carries charge" that the wrap-order has fixed. By inspection, it inverts the framework's own labels.

(The R_J construction (++) + (−−) is also ruled out, on a different ground: R_J = R_u · R_w, and enforcing R_w would force R_J to fix the tube-direction sign, which we have established is not a particle symmetry. R_J cancels both cross-terms and so produces the mass-only configuration that would describe an *uncharged* particle on the same closure-satisfying knot, which is not what we are constructing here.)

---

## 7. Stress-energy of the natural particle, explicitly

Compute T_μν for φ_+ = 2A cos(k_u u) cos(k_w w − ωt) at rest in 4D. Derivatives:

- ∂_t φ = +2A·ω·cos(k_u u)·sin(k_w w − ωt)
- ∂_u φ = −2A·k_u·sin(k_u u)·cos(k_w w − ωt)
- ∂_w φ = −2A·k_w·cos(k_u u)·sin(k_w w − ωt)

Spatial-temporal averages (using ⟨cos²⟩ = ⟨sin²⟩ = 1/2 and ⟨sin·cos⟩ = 0 over a full period in each variable):

| Entry | Computation | Average |
|---|---|---|
| T_tt | (∂_t φ)² ∝ 4A²ω²·cos²(k_u u)·sin²(k_w w − ωt) | A²·ω² |
| T_uu | (∂_u φ)² ∝ 4A²k_u²·sin²(k_u u)·cos²(k_w w − ωt) | A²·k_u² |
| T_ww | (∂_w φ)² ∝ 4A²k_w²·cos²(k_u u)·sin²(k_w w − ωt) | A²·k_w² |
| T_tu | ∂_t φ·∂_u φ ∝ −4A²k_u·ω·cos(k_u u)·sin(k_u u)·sin(k_w w − ωt)·cos(k_w w − ωt) | **0** (cos·sin in u → 0) |
| T_tw | ∂_t φ·∂_w φ ∝ −4A²k_w·ω·cos²(k_u u)·sin²(k_w w − ωt) | **−A²·ω·k_w** |
| T_uw | ∂_u φ·∂_w φ ∝ +4A²k_u k_w·cos(k_u u)·sin(k_u u)·cos(k_w w − ωt)·sin(k_w w − ωt) | **0** (cos·sin in u → 0) |

The three off-diagonals reduce to one nonzero entry: **T_tw = −A²·ω·k_w**, doubled relative to a single traveling-wave mode (which would give −A²·ω·k_w/2). The doubling reflects the two-component superposition; the survival of the tube-direction cross-term reflects the asymmetric application of standing-wave construction.

Diagonal entries are also doubled (factor 2 vs 1/2 on each), giving the rest-mass contribution

<!-- m² c² = (ℏk_u)² + (ℏk_w)² (rest mass from compact-direction wavenumbers) -->
$$
m_\text{rest}^2 c^2 \;=\; (\hbar k_u)^2 + (\hbar k_w)^2
$$

— the metric-mass mass formula extended to two compact directions, with both ring and tube contributing to rest energy (per [Chapter 2 §3](02-modes-on-a-sheet.md)).

---

## 8. Why this is a Kaluza-Klein derivation, not hand-waving

The case for a single gauge field term emerging on solid ground rather than by hand-waving rests on this: the construction above is a *direct* Kaluza-Klein derivation, with the 2D-compact extension respecting both the KK mechanism and the metric-mass mechanism in the directions where each properly applies.

**Mapping to standard KK.** Standard 5D KK ([primers/kaluza-klein.md](../../primers/kaluza-klein.md)) has 4D extended spacetime + 1 compact direction. It treats a particle with definite compact-direction wavenumber n; the cross-term g_μ5 = A_μ is the gauge potential, charge is q ∝ n, and Maxwell's equations follow from 5D Einstein equations. KK does *not* standing-wave the compact direction — the particle has definite n, and the cross-term survives precisely because it does.

In our 2D-compact construction, the **tube direction (w) plays the role of standard KK's single compact direction.** The natural particle has definite n (the sign of the w-direction circulation), the wave is traveling in w, and the cross-term h_μw = B_μ survives. This is standard KK applied to the tube — one compact direction, one gauge field, charge proportional to compact-direction wavenumber.

The **ring direction (u) plays the role of metric-mass's single compact direction.** The natural particle has the standing-wave structure cos(k_u u), the wave is *not* traveling in u (no definite ±m direction), and the would-be cross-term h_μu cancels by the same mechanism that cancels metric-mass's g_tu. This is metric-mass applied to the ring — one compact direction, no gauge field, mass contribution from compact-direction wavenumber via the dispersion relation.

**The 2D-compact T² is decomposed by the wrap-order into "1D-compact for KK + 1D-compact for mass-only."** The two mechanisms compose naturally; neither contradicts the other because they apply to different directions, with the wrap-order picking which is which.

**Why this isn't double-counting.** A single traveling-wave mode (the per-component intermediate of §3) would source two cross-terms. Combining (++) + (−+) cancels exactly the cross-term whose direction has the metric-mass-style standing-wave structure (the ring), and preserves exactly the cross-term whose direction has the KK-style traveling-wave structure (the tube). The math is forced by the choice of which symmetry to enforce; the choice is forced by the wrap-order.

**Why this isn't free choice.** The wrap-order is not a per-particle interpretive parameter. It is fixed once for the framework as a whole, and applies the same way to all modes. The "two candidates, rule one out" framing is settled by inspection of the wrap-order: travel in the tube (single wrap, charge), stand in the ring (multi-wrap, mass). The opposite choice would invert the framework's labels and force us to call the multi-wrap direction "tube" — which is what the convention forbids.

The argument is a Kaluza-Klein derivation in the strict sense: it uses standard KK machinery (5D metric ansatz, off-diagonal entries as gauge potentials, charge as compact-direction momentum), applied to the tube direction selected by the wrap-order, with the additional ring direction acting as a metric-mass-style mass source. No new principles, no interpretive moves beyond reading off the wrap-order.

---

## 9. Closure-failing modes — a structural distinction

For closure-failing configurations, the topological status of R_u and R_w changes, and the natural particle construction follows.

### 9.1 Single-axis modes — degenerate, mass-only

Modes (m, 0) or (0, n) — one winding zero. Take (m, 0):
- The wave has no w-dependence, so any reflection in w acts trivially.
- R_u (sign of m) is the only nontrivial reflection.
- The natural particle is the standing wave (++) + (−+) → 2A cos(k_u u)·cos(ωt). This is precisely metric-mass's standing wave restricted to the u-direction (with no w-structure at all).
- T_tu = 0 (metric-mass mechanism), T_tw = 0 (no k_w to source it), T_uw = 0. Mass only.

By symmetry the (0, n) case gives mass only via the w-direction's standing wave. Either way, single-axis modes are mass-only.

### 9.2 Genuine torus knots — chirality matters in both directions

For T(p, q) with p, q ≥ 2 and gcd(p, q) = 1, the curve is a *genuine* torus knot in 3-space — chirally distinct from its mirror. Specifically:

- **R_u changes the knot type.** T(p, q) and T(−p, q) are mirror-chirality torus knots, distinct in 3-space. R_u is *not* a topological symmetry.
- **R_w changes the knot type.** Similarly distinct. R_w is not a topological symmetry.
- **R_J = R_u · R_w preserves the knot type.** T(p, q) and T(−p, −q) are the same unoriented curve (just opposite traversal). R_J *is* a topological symmetry.

The only available symmetry is R_J. The natural particle is the joint-reversal-symmetrized standing wave (++) + (−−) = 2A cos(k_u u + k_w w)·cos(ωt). By §4's R_J row: **T_tu = 0, T_tw = 0, T_uw ≠ 0.**

Mass + chirality field (in T_uw, the σ_uw-style cross), no EM cross-terms. Genuine torus knots are mass-only at the EM level, with a chirality signature in T_uw.

This recovers the framework's existing prediction (chapter 4) that genuine torus knots are mass-only — and it derives the prediction from the same wrap-order-asymmetry mechanism that produces charged particles for closure-satisfying knots. Single mechanism, two outcomes depending on the knot's topological-chirality status.

### 9.3 Why closure-satisfying and closure-failing diverge

The wrap-order's claim that R_u is a particle symmetry holds for closure-satisfying T(m, 1) because the underlying knot is the unknot (achiral) — so R_u-related configurations are topologically equivalent. For genuine torus knots, the underlying knot *is* chiral, so R_u-related configurations are topologically distinct, and the wrap-order's claim no longer applies. Falling back to R_J (which is always a topological symmetry, since unoriented curves are unoriented) yields the mass-only configuration.

The closure rule (m | n with both nonzero, equivalent to "the gcd-reduced primitive is T(1, q) — an unknot") is precisely the condition under which R_u (acting on the ring direction) is a topological symmetry. It is therefore exactly the condition under which the natural particle has one gauge potential (charged) rather than zero (mass-only). **The closure rule and the gauge-promotion mechanism agree because they are descriptions of the same underlying fact:** the topological-chirality status of the curve, which controls which wrap-order-aligned symmetries the natural particle inherits.

---

## 10. Matter, antimatter, and the surviving cross-term

For closure-satisfying T(m, 1), there are two natural particles, distinguished by the sign of the tube-direction circulation:

| Particle | Modes | Wave | T_tw |
|---|---|---|---|
| Matter | (++) + (−+) | 2A cos(k_u u) cos(k_w w − ωt) | −A²·ω·k_w |
| Antimatter | (+−) + (−−) | 2A cos(k_u u) cos(k_w w + ωt) | +A²·ω·k_w |

Both are R_u-symmetrized in the ring (chirality degenerate for unknots). They differ in the sign of the tube-direction phase advance — equivalently, in the sign of n. The corresponding T_tw entries have opposite sign, which translates to opposite sign of the gauge potential B_μ — i.e., opposite charge.

Joint-reversal R_J relates the two: applying R_J to the matter particle's modes gives the antimatter particle's modes. R_J is therefore the matter/antimatter operation, *not* a particle symmetry. The framework correctly distinguishes "particle symmetry" (cancels cross-terms; mass-only outcome) from "matter/antimatter axis" (preserves the magnitude of cross-terms but flips their sign; opposite-charge particles).

This resolves a tension in metric-mass: there, the standing wave was constructed by enforcing R_J (over the only available compact direction), which had the side effect of identifying matter and antimatter as the same particle (metric-mass Ch5 §0 acknowledges this and leaves the matter/antimatter question open). In metric-charge with two compact directions, the wrap-order-asymmetric construction enforces R_u alone for the natural particle, leaving R_J free to act as the matter/antimatter operation. **Matter and antimatter become structurally distinct only in the 2D-compact case** — exactly when the wrap-order has two compact directions to assign differently asymmetric roles to. Note: this only renders matter and antimatter as *distinct* natural particles; what *populates* one over the other (the actual matter excess in the universe) is not addressed here, and remains forwarded to a separate substrate-level mechanism — for example, a chirality bias in the underlying lattice from grid-primitive, or σ_uw shear at the population level per [Chapter 6 §6](06-handedness-and-pairs.md). This is consistent with metric-mass's note that antimatter "requires additional structure (e.g., the second compact direction in metric-charge)" ([metric-mass Ch5 §0](../metric-mass/05-metric-self-consistency.md)).

---

## 11. Full inventory under this reading

| Configuration | Topological character | Particle symmetry | Cross-terms sourced | Type |
|---|---|---|---|---|
| Light (0, 0) | No curve | — | None (no compact wavenumber) | Light |
| Single-axis (m, 0) | Trivial cycle | R_u (only available) | None (T_tw = 0 from k_w = 0; T_tu = 0 from R_u) | Mass-only |
| Single-axis (0, n) | Trivial cycle | R_w (only available) | None (T_tu = 0 from k_u = 0; T_tw = 0 from R_w) | Mass-only |
| T(m, 1) primitive | Unknot in 3-space (achiral) | R_u (wrap-order-aligned with topology) | **T_tw alone** | **Mass + 1 gauge field B_μ** |
| Multi-link k × T(m, 1) | k-component unlink | R_u per component | T_tw per component, summing across k | Mass + charge (k components) |
| T(p, q), p, q ≥ 2, gcd = 1 | Genuine torus knot (chiral) | R_J (only available) | None EM (T_uw ≠ 0; chirality field) | Mass + chirality |

The closure-satisfying inventory (T(m, 1) primitives and their multi-links) carries one gauge potential apiece. The closure-failing inventory carries no EM gauge potential — single-axis by missing k_w or k_u, genuine torus knots by topological chirality forcing R_J (the most restrictive symmetry).

The "two-U(1)s puzzle" of the current [Chapter 5 §8](05-metric-self-consistency.md) dissolves: the single-mode reading produces two candidate U(1)s, but the natural particle (R_u-symmetrized) sources only one. The other compact direction's would-be gauge potential is cancelled by the metric-mass mechanism, exactly as in 1D-compact.

---

## 12. What this means for the framework

If the work1.md derivation holds up, [Chapter 5](05-metric-self-consistency.md) restructures as follows:

- **§§2–3 unchanged.** The single-mode stress-energy is a per-component intermediate, not a particle. Two cross-terms appear at this level.
- **§§4 reframed.** The four-property test of gauge-potential structure is applied to the *natural-particle* h_μν (after R_u-symmetrization), not to the per-component h_μν. Only one set of off-diagonals (h_μw for the convention u=ring, w=tube) survives the symmetrization, so only one U(1) is tested. It passes — gauge potential structure is recovered for one U(1), exactly matching standard physics.
- **§5 reframed.** Closure-failing modes are mass-only by the natural-particle construction (single-axis: degenerate; genuine torus knots: forced to R_J by topological chirality). The current §5's "two distinct mechanisms" become two flavors of the same underlying mechanism (wrap-order-asymmetric standing-wave construction) applied to different topological situations.
- **§6.5 simplified.** The four (now three) "asymmetric conventions" all derive from the wrap-order alone. Convention 4 (gauge identification) becomes a *consequence* of the construction rather than an independent stipulation: once the wrap-order fixes which direction is the ring, R_u (acting on the ring) is automatically the symmetry to enforce, and h_μw is automatically the surviving gauge potential.
- **§8 simplified.** The "two-U(1)s differ from standard physics" caveat goes away. The framework produces one U(1) for charged particles, matching standard EM.

Open work this reading does not address:

1. **The wrap-order itself.** Why u rather than w is the ring (or equivalently, why R_u rather than R_w is the wrap-order-aligned symmetry). This is downstream from grid-duality's L0→L1 vs L1→L2 asymmetry. Forwarded to the alpha-derivation track.
2. **The numerical strength of the gauge coupling (α).** Cited from grid-duality §8. Structural location settled here; numerical value is open.
3. **Higher-order corrections.** Linearized Einstein equations only; nonlinear backreaction is downstream.
4. **MaSt-correspondence for the three mass-only categories.** Single-axis modes, genuine torus knots, and chirality-conjugate-cancellation-pair (Chapter 6) are three structurally distinct mass-only mechanisms. How they map to neutrinos, dark matter candidates, neutral hadrons, etc., is downstream MaSt-correspondence work.

---

## 13. Comparison with work.md

Two derivations, same problem. work.md reaches "no gauge field" by enforcing the metric-mass principle (R_J) uniformly across both compact directions. work1.md reaches "exactly one gauge field" by enforcing only the wrap-order-aligned reflection (R_u for closure-satisfying configurations).

The core disagreement: work.md treats metric-mass's standing-wave principle as "always combine ±k for every compact direction." work1.md treats it as "combine ±k only in the directions where the wrap-order makes ±k a topological symmetry of the configuration." The first interpretation is uniform but wrong; the second respects the wrap-order asymmetry that the framework has built into its conventions.

work.md acknowledges in §11.7 that the "two directions don't cancel in 2D" observation points away from the uniform R_J reading — and offers a reading that drops the standing-wave principle entirely (Reading B+, two single-mode cross-terms) as the alternative. work1.md identifies a *third* path that work.md missed: keep the standing-wave principle but apply it asymmetrically, with the asymmetry sourced from the wrap-order convention. This produces one cross-term, matches the "two candidates, rule one out by inspection" framing, and is internally consistent with both metric-mass (as the ring-direction mechanism) and Kaluza-Klein (as the tube-direction mechanism).

The math of §§3–4 is shared with work.md §§3–6; the interpretive work of §§5–10 is what this file does differently.

---

## Recommendation

If the asymmetric-standing-wave reading holds up under further checks, [Chapter 5](05-metric-self-consistency.md) should be rewritten to:

1. Open with the per-component intermediate (§3 here) and acknowledge its two cross-terms.
2. Introduce the three candidate symmetrizations (§4 here) and their cross-term outcomes.
3. Bring in the wrap-order (§5 here) as the principle that selects R_u for closure-satisfying configurations.
4. Compute the natural particle's stress-energy explicitly (§7 here) and read off the single surviving gauge potential.
5. Cover closure-failing modes (§9 here) via the same principle, recovering mass-only outcomes for both single-axis and genuine torus knots.
6. Address matter/antimatter (§10 here) as the R_J operation that the natural particle does *not* enforce.

The current Chapter 5 still has useful content in §6.5 (the conventions reduction) and §7 (the holonomy mechanism); both survive the rewrite with minor adjustments.

The substantive scientific claim is that the framework predicts exactly one gauge potential for closure-satisfying particles, with that prediction inheriting from the wrap-order asymmetry between the ring (u) and tube (w) directions. This matches standard physics (one EM U(1) per charged particle) and is consistent with both the metric-mass mechanism (ring) and the Kaluza-Klein mechanism (tube). It is a clean derivation, not an interpretive choice.
