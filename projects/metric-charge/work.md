# work.md — preliminary derivations under the standing-wave reading

**Purpose.** Working file for preliminary derivations of how metric-mass's standing-wave-as-particle reading extends to 2D-compact metric-charge. Once derivations are vetted and an interpretation is accepted, content here moves into project chapters; what doesn't survive review gets pruned.

**Discipline:** math first, interpretation second. Do the algebra honestly, tabulate what falls out, only then ask what it might mean.

---

## 1. Inherited principle from metric-mass

A single traveling-wave Fourier mode φ ∝ cos(k·x − ωt) has a definite direction of phase advance around the compact loop. It sources off-diagonal stress-energy entries that are **odd** in the compact-direction wavenumber. Under the wave equation, the opposite-direction Fourier mode (negated wavenumber, same |ω|) is also a valid solution — equally valid, indistinguishable on grounds of physics.

The **standing wave** is the equal-amplitude superposition of both directions. Under this superposition:

- Entries **even** in compact-direction wavenumber **add**: energy density (T_tt), compact pressure (T_uu), etc.
- Entries **odd** in compact-direction wavenumber **cancel**: T_tu (gauge potential A_μ), T_Su (motion-coupled gauge potential).

The standing wave has rest mass (from the doubled diagonal entries) but zero off-diagonal sourcing (from the cancelled odd entries). It is the "particle" — directionless, standing in the compact direction, no KK gauge structure produced.

The single traveling-wave mode is a **per-component intermediate** — half of a particle. It has both rest mass and the "would-be" gauge structure that gets cancelled when the other half arrives.

This is the principle to extend.

---

## 2. The 2D-compact setting

[Chapter 1 §6](01-foundation.md) gives the manifold M = ℝ × ℝ³ × T² with two compact directions u, w and bare diagonal metric. The wave equation □φ = 0 on this manifold, with periodicity, gives Fourier modes labeled by (m, n) ∈ ℤ². The dispersion is

<!-- ω² = c²·(k_S² + k_u² + k_w²) -->
$$
\omega^2 = c^2\bigl(k_S^2 + k_u^2 + k_w^2\bigr),\qquad k_u = \tfrac{2\pi m}{L_u},\ k_w = \tfrac{2\pi n}{L_w}
$$

— even in (m, n). For fixed magnitudes (|m|, |n|), there are **four** distinct Fourier modes at the same |ω|:

| Mode | (m, n) | Phase advance per cycle |
|---|---|---|
| (++) | (+m, +n) | +k_u·u + k_w·w − ωt |
| (+−) | (+m, −n) | +k_u·u − k_w·w − ωt |
| (−+) | (−m, +n) | −k_u·u + k_w·w − ωt |
| (−−) | (−m, −n) | −k_u·u − k_w·w − ωt |

Each is a valid eigenmode of the wave equation. Various superpositions are also valid solutions; the question is which combinations correspond to physical particles.

A topological note: T(m, n) and T(−m, −n) describe the **same** unoriented closed curve on T² traversed in opposite directions. T(m, n) and T(m, −n) describe **different** closed curves — chiral mirror images of each other. The (++) and (−−) modes belong to one knot and orientation pair; (+−) and (−+) belong to the chirality-mirrored knot pair. We will use this distinction.

---

## 3. Single Fourier mode — stress-energy

Take φ = A·cos(k_u·u + k_w·w − ωt) (the (++) mode, at rest in 4D so k_S = 0). Compute:

- ∂_t φ = +A·ω·sin(k_u·u + k_w·w − ωt)
- ∂_u φ = −A·k_u·sin(k_u·u + k_w·w − ωt)
- ∂_w φ = −A·k_w·sin(k_u·u + k_w·w − ωt)

Stress-energy entries (relevant ones, time-and-space-averaged):

| Entry | Value | Average |
|---|---|---|
| T_tt | (∂_t φ)² + (1/2)·(...) | A²·ω²/2 (energy density, mass) |
| T_uu | (∂_u φ)² + (1/2)·(...) | A²·k_u²/2 (compact pressure u) |
| T_ww | (∂_w φ)² + (1/2)·(...) | A²·k_w²/2 (compact pressure w) |
| **T_tu** | ∂_t φ · ∂_u φ | **−A²·ω·k_u/2 (sources A_μ)** |
| **T_tw** | ∂_t φ · ∂_w φ | **−A²·ω·k_w/2 (sources B_μ)** |
| T_uw | ∂_u φ · ∂_w φ | A²·k_u·k_w/2 (compact-compact cross) |

The single Fourier mode sources both T_tu (A_μ gauge potential) and T_tw (B_μ gauge potential) and T_uw (compact-compact cross, related to σ_uw shear). It also sources the diagonal entries (mass).

Under the standing-wave principle, this is **not yet the particle** — it has a definite direction of traversal around T(m, n).

---

## 4. Sign-conjugate pair: standing wave on the same oriented knot

Combine (++) and (−−) at equal amplitude:

φ = A·cos(k_u·u + k_w·w − ωt) + A·cos(k_u·u + k_w·w + ωt)
  = 2A·cos(k_u·u + k_w·w)·cos(ωt)

This is the **standing wave along the knot T(m, n)** — light bouncing back and forth along the specific oriented closed curve. The +(++) and (−−) components are the two traversal directions of the same unoriented curve, summed.

Compute:

- ∂_t φ = −2A·ω·cos(k_u·u + k_w·w)·sin(ωt)
- ∂_u φ = −2A·k_u·sin(k_u·u + k_w·w)·cos(ωt)
- ∂_w φ = −2A·k_w·sin(k_u·u + k_w·w)·cos(ωt)

Stress-energy (time-and-space-averaged):

| Entry | Computation | Average |
|---|---|---|
| T_tt | proportional to cos²·sin² | 2A²·ω²·(1/2)·(1/2) = A²·ω²/2 (×2 from doubling) |
| T_tu | ∝ cos(k_u·u + k_w·w)·sin(k_u·u + k_w·w)·sin(ωt)·cos(ωt) | **0 (both factors average to 0)** |
| T_tw | same structure as T_tu | **0** |
| T_uw | ∝ sin²(k_u·u + k_w·w)·cos²(ωt) | **2A²·k_u·k_w·(1/2)·(1/2) = A²·k_u·k_w/2** |
| T_uu | ∝ sin²·cos² | doubled, non-zero |
| T_ww | similar | doubled, non-zero |

**Both T_tu and T_tw cancel exactly.** The standing wave on T(m, n) has:

- Doubled rest mass (T_tt × 2 across the two components)
- **No A_μ gauge potential** (T_tu cancels)
- **No B_μ gauge potential** (T_tw cancels)
- **Doubled T_uw** (compact-compact cross), which is even in joint sign flip and so adds rather than cancels

The particle is mass-only at the spacetime-extended-to-compact gauge level. But it sources a non-zero T_uw — a compact-compact cross-term that equals (in sign and magnitude) what σ_uw shear would source.

---

## 5. Chirality-conjugate pair: standing in one direction, traveling in the other

Combine (++) and (+−) at equal amplitude:

φ = A·cos(k_u·u + k_w·w − ωt) + A·cos(k_u·u − k_w·w − ωt)
  = 2A·cos(k_u·u − ωt)·cos(k_w·w)

(Using cos(A+B) + cos(A−B) = 2cos(A)cos(B) with A = k_u·u − ωt, B = k_w·w.)

This is **traveling in u, standing in w**. The two components are different chirality knots T(m, n) and T(m, −n), each traversed forward.

Compute:

- ∂_t φ = +2A·ω·sin(k_u·u − ωt)·cos(k_w·w)
- ∂_u φ = −2A·k_u·sin(k_u·u − ωt)·cos(k_w·w)
- ∂_w φ = −2A·k_w·cos(k_u·u − ωt)·sin(k_w·w)

Stress-energy:

| Entry | Computation | Average |
|---|---|---|
| **T_tu** | ∝ sin²(k_u·u − ωt)·cos²(k_w·w) | **−2A²·ω·k_u·(1/2)·(1/2) = −A²·ω·k_u/2 (non-zero — sources A_μ)** |
| **T_tw** | ∝ sin(k_u·u − ωt)·cos(k_u·u − ωt)·cos(k_w·w)·sin(k_w·w) | **0 (sin·cos in u-traveling factor averages to 0; also sin·cos in w-standing factor)** |
| T_uw | ∝ sin·cos in both factors | **0** |

**T_tu is non-zero (one U(1) charge under A_μ); T_tw cancels.** Mass + one EM charge — under A_μ specifically, since the wave is traveling in u and standing in w.

The chirality-conjugate pair (++) + (−+) gives the symmetric configuration: standing in u, traveling in w. T_tu cancels, T_tw is alive. Mass + one EM charge under B_μ.

---

## 6. Full four-mode standing wave

All four modes (++), (+−), (−+), (−−) at equal amplitude:

φ = 4A·cos(k_u·u)·cos(k_w·w)·cos(ωt)

(After combining all four.) Standing in both u and w.

All odd-in-sign-flip cross-terms cancel (T_tu, T_tw, T_uw — the latter cancels because sin(k_u·u)·cos(k_u·u) and sin(k_w·w)·cos(k_w·w) both average to zero). Only diagonal entries survive. Pure mass on T², no chirality information, no charge.

---

## 7. Summary table — what each configuration sources

Putting it all together. "Even" entries (under joint sign reflection (m, n) → (−m, −n)) involve squares of wavenumbers; "odd" entries involve linear-in-wavenumber products with ω.

| Configuration | T_tu (A_μ) | T_tw (B_μ) | T_uw (σ_uw) | Interpretation |
|---|---|---|---|---|
| **Single Fourier (++)** | −ωk_u/2 | −ωk_w/2 | +k_u k_w/2 | Per-component intermediate; not a particle |
| **Sign-conjugate** (++) + (−−) — standing on T(m, n) | **0** | **0** | +k_u k_w (doubled) | Mass + chirality-σ; **no EM charge** |
| **Chirality-conjugate** (++) + (+−) — travel u, stand w | −ωk_u (doubled) | **0** | **0** | Mass + **one charge under A_μ** |
| **Chirality-conjugate** (++) + (−+) — stand u, travel w | **0** | −ωk_w (doubled) | **0** | Mass + **one charge under B_μ** |
| **Full four-mode standing** | **0** | **0** | **0** | Pure mass, no chirality, no charge |

Plus four-mode superpositions with various sign patterns; one of interest:

| (++) − (+−) − (−+) + (−−) | 0 | 0 | doubled | Mass + chirality-σ only — equivalent to sign-conjugate above |

---

## 8. The user's knot-asymmetry observation as a constraint

The user's structural observation: in 1D-compact, the loop is rotationally symmetric; +n and −n are mirror-image solutions and *cannot* be physically distinguished. Combining them into a standing wave is the natural directionless particle.

In 2D-compact, **the knot T(m, n) is not rotationally symmetric** in general. Two physically distinguishable structural facts become available:

- **Knot orientation.** T(m, n) and T(−m, −n) trace the same unoriented curve in opposite directions. (Closer to the 1D case — these are mirror traversals of the same knot.)
- **Knot chirality.** T(m, n) and T(m, −n) are *different* knots — chiral mirror images in 3-space. (Genuinely distinct configurations.)

The user's principle: only modes corresponding to "the same knot, considered abstractly" should be combined into a standing wave. This is the **sign-conjugate pair** {(++), (−−)}. The chirality-conjugate components {(++), (+−)} or {(++), (−+)} belong to *different knots* and should not be combined unless the framework has a separate physical reason.

Under this principle:

- **The natural particle on knot T(m, n)** is the sign-conjugate standing wave {(++), (−−)}.
- This particle has **mass + chirality-encoded T_uw**, but **no EM charge** (T_tu and T_tw both cancel).

This is consistent with metric-mass's principle — the particle is directionless along its own oriented loop. But it contradicts the framework's previous claim that closure-satisfying modes carry observable EM charge — because *the standing wave on a closure-eligible knot has zero EM cross-terms*.

---

## 9. The central problem: where does EM charge come from?

The math gives a clean answer to "what mass-only configurations look like" (sign-conjugate standing waves on chiral knots). It does **not** give a clean answer to "what charged configurations look like" — at least not yet.

Three candidate readings, each with consequences:

### Reading A: Charged particles are chirality-conjugate pairs

**Configuration:** (++) + (+−), or (++) + (−+) — standing in one direction, traveling in the other.

**What it gives:** Mass + one U(1) gauge potential — A_μ alone or B_μ alone.

**Match with standard physics:** Single observed U(1) per particle. Matches.

**Tension with user's knot-asymmetry principle:** The chirality-conjugate pair is a superposition of two *different* knots (T(m, n) and T(m, −n)). It's not "a particle on one specific knot" — it's a coherent mixture of right-handed and left-handed knot traversals. The user's principle ("only one fits the specific knot solution") would resist this construction, since chiralities are physically distinguishable.

**Verdict:** Resolves the two-U(1)s puzzle but at the cost of saying particles are chirality-mixed.

### Reading B: Charged particles are single Fourier modes

**Configuration:** Single (++) mode — definite traversal of definite chiral knot.

**What it gives:** Mass + two U(1) gauge potentials (A_μ and B_μ both alive). The framework's current state.

**Match with standard physics:** Two U(1)s; standard physics has one. Doesn't match without additional reduction.

**Match with the standing-wave principle:** Inconsistent — single Fourier mode is *not* a standing wave; it has a definite traversal direction. metric-mass calls this a "per-component intermediate" not a particle.

**Verdict:** Contradicts the standing-wave principle. If we accept the principle, this reading must be rejected.

### Reading C: Mass-only on chiral knots; EM charge requires something more

**Configuration:** Sign-conjugate standing wave on T(m, n) (the user's preferred reading by the knot-asymmetry argument).

**What it gives:** Mass + chirality-σ in T_uw. **Zero EM cross-terms.**

**Match with standard physics:** This particle is *neutral* — no EM charge. So under this reading, *all* sign-conjugate standing-wave particles on knots are EM-neutral. Standard physics has neutrinos but also has charged leptons.

**Where charge would come from:** Outside the single-particle stress-energy. Candidate sources:

- *Asymmetric amplitudes* between (++) and (−−): if the two traversal directions are not at equal amplitude, the cancellation is partial and a residual T_tu, T_tw remains. This would mean charge ∝ amplitude asymmetry, similar to the unequal-cancellation case in [Ch 6 §4.3](06-handedness-and-pairs.md).
- *Substrate-level chirality* from grid-primitive: if the underlying lattice has an intrinsic preferred direction, sign-conjugate pairs may form with built-in amplitude bias rather than equal amplitudes. Charge would emerge from this substrate boundary condition.
- *Inter-particle interaction*: charge as a property that only manifests when two particles are present. In isolation, sign-conjugate pair cancels EM; in interaction, the cancellation is broken by the other particle's field.

**Verdict:** Cleanly consistent with the standing-wave principle and the user's knot-asymmetry principle, but leaves "where does EM come from?" as an open question requiring additional structure.

---

## 10. The user's hint: "EM cross-terms only in the assumption of the presence of the particle"

Re-read with the candidate readings in hand. The user's framing suggests:

> Charge production should produce EM cross-terms, but only in the assumption of the presence of the particle.

If "the particle" is a sign-conjugate standing wave (Reading C), the cross-terms cancel in the *isolated* particle. They emerge only when something perturbs the cancellation — i.e., when an amplitude asymmetry develops between the (++) and (−−) components.

What could perturb the (++) ↔ (−−) balance? **This is the central question, and my first attempt at it does not work.** Recording the failed attempt and what it reveals:

### 10.1 Failed candidate mechanism: σ_uw shear

My initial proposal: a sign-conjugate standing wave on T(m, n) sources a σ_uw shear of definite sign (+k_u·k_w). If this σ_uw shear were felt by another sign-conjugate particle in the neighborhood, perhaps it would break that particle's (++) ↔ (−−) balance and produce residual EM cross-terms.

**This mechanism does not work.** Per [Chapter 6 §6](06-handedness-and-pairs.md), σ_uw breaks (m, n) ↔ (m, −n) — the **chirality** reflection — and *preserves* (m, n) ↔ (−m, −n) — the **sign** reflection. The sign-conjugate pair {(++), (−−)} are sign-conjugate-related, so σ_uw does *not* lift them to different energies. σ_uw cannot break the (++) ↔ (−−) balance.

What σ_uw *would* break is the chirality-conjugate balance: the relative population of T(m, n) vs T(m, −n) chirality knots in thermal equilibrium. But that's a population question across different particles (different chiral species), not an internal-amplitude-asymmetry question within one particle's standing wave.

### 10.2 What this rules out and what remains

Ruled out: a σ_uw shear cannot, in this framework's current machinery, induce EM cross-terms in an isolated sign-conjugate standing-wave particle.

What this means structurally: **breaking the (++) ↔ (−−) balance requires a mechanism that is odd under sign reflection** (m, n) ↔ (−m, −n). Looking at what's available:

- σ_uw cross-term k_u·k_w → **even** in joint sign flip → cannot break the balance.
- Extended-compact shear σ_S₁u (cross-term k_S₁·k_u) → **odd** in (m → −m) and odd in (k_S₁ → −k_S₁) → could break the balance, but only if k_S₁ ≠ 0 (the particle is moving in space). Doesn't apply to a particle at rest.
- σ_S₁w (cross-term k_S₁·k_w) → similar, only applies to moving particles.
- Time-asymmetry in initial conditions or external fields that have a built-in arrow of time → would break the balance, but the framework has no such ingredient.
- Substrate-level T-violation from grid-primitive — possible but not currently part of the framework.

For a particle at rest in 4D (the canonical case), the framework as currently written has no mechanism that breaks (++) ↔ (−−). EM charge cannot emerge from the σ_uw machinery.

### 10.3 What this implies for the framework

Three possibilities:

(i) **Reading C is incomplete and needs a substrate-level ingredient.** The (++) ↔ (−−) balance break must come from substrate chirality (grid-primitive / grid-duality) or from initial conditions baked into the universe at preparation. The framework cannot derive this internally.

(ii) **Reading C is wrong; a different reading is needed.** Perhaps Reading B (single Fourier modes are particles, despite metric-mass's standing-wave principle), or some hybrid.

(iii) **The "particle" concept needs revising.** Perhaps charge isn't the residual of an asymmetry within a sign-conjugate standing wave. Perhaps charge is something else entirely — for example, an interaction property between two particles' standing waves where the chirality-mismatch produces something that wasn't there in either particle alone.

### 10.4 Open Derivation 1 — does chirality mixing produce EM cross-terms?

Consider a chirality-mixed configuration:

$$
\varphi = \alpha\cdot\cos(k_u u + k_w w)\cos(\omega t) + \beta\cdot\cos(k_u u - k_w w)\cos(\omega t)
$$

This is α-amplitude of "standing wave on T(m, n)" plus β-amplitude of "standing wave on T(m, −n)" — chirality-mixed sign-conjugate standing waves. Time-and-space derivatives:

- ∂_t φ = −[α·cos(K_+) + β·cos(K_-)] · ω·sin(ωt),  where K_± = k_u u ± k_w w
- ∂_u φ = −[α·sin(K_+) + β·sin(K_-)] · k_u·cos(ωt)
- ∂_w φ = −[α·sin(K_+) − β·sin(K_-)] · k_w·cos(ωt)

T_tu = ∂_t φ · ∂_u φ. Time factor: sin(ωt)·cos(ωt) → averages to 0. **T_tu = 0.**

T_tw = ∂_t φ · ∂_w φ. Same time factor: sin(ωt)·cos(ωt) → averages to 0. **T_tw = 0.**

T_uw = ∂_u φ · ∂_w φ. Time factor: cos²(ωt) → averages to 1/2. Spatial factor: [α·sin(K_+) + β·sin(K_-)]·[α·sin(K_+) − β·sin(K_-)] = α²·sin²(K_+) − β²·sin²(K_-). Spatially averaging both sin² to 1/2 gives **(α² − β²)·k_u·k_w/2 — non-zero when α ≠ β.**

**Result: chirality mixing produces no EM cross-terms.** T_tu and T_tw both average to zero regardless of α, β. Only T_uw (the σ_uw shear cross-term) responds to chirality asymmetry — its sign tracks (α² − β²), the chirality balance.

So the §10.4 mechanism does not produce EM charge. The same time-symmetry that suppresses cross-terms in a single sign-conjugate standing wave (the cos(ωt) factor producing sin·cos averaging to zero) also suppresses them in any chirality-mixed combination of sign-conjugate standing waves.

### 10.5 The deeper structural reason

The pattern is now clearer: **EM cross-terms (T_tu, T_tw) require the wave to be coupled with time in some compact direction.** Specifically:

- A wave of the form cos(K·u − ωt)·G(other) has time and u-direction coupled in a single phase argument — this gives non-zero T_tu (the wave is "traveling in u").
- A wave of the form cos(K·u)·cos(ωt)·G(other) has time and u-direction *separated* — this gives zero T_tu (time is "standing").

A single Fourier mode at (m, n) couples *both* compact directions with time: phase = k_u u + k_w w − ωt. Cross-terms in *both* T_tu and T_tw.

A sign-conjugate standing wave decouples both compact directions from time: phase = K·cos(ωt) factored. Both cross-terms vanish.

A "partial standing" (chirality-conjugate pair from §5) keeps one direction coupled with time while standing in the other: phase = (k_u u − ωt)·cos(k_w w). Cross-term only in the still-coupled direction.

The user's strict knot-asymmetry principle says: *combine the two traversal directions of T(m, n) into a sign-conjugate standing wave; don't combine different-chirality knots.* Under this principle, the particle has both compact directions decoupled from time. Both EM cross-terms vanish. **Pure mass.**

### 10.6 What this means

Under the strict standing-wave principle inherited from metric-mass and applied with the user's knot-asymmetry refinement, **the framework predicts only mass particles, not charged particles.** The math is forced: time-decoupled spatial structure gives zero EM cross-terms, and "directionless particle on a specific oriented knot" is exactly the time-decoupled case.

This is not a contradiction — it is a substantive prediction. Three readings of what to do with it:

(a) **The framework as currently structured cannot derive EM charge from internal mode structure on T².** EM charge must come from an *external* ingredient — most plausibly substrate-level chirality from [grid-primitive](../grid-primitive/), which would break the (++) ↔ (−−) balance through a non-σ_uw mechanism (e.g., chiral edges in the lattice that bias one direction of phase advance over the other).

(b) **Particles are not standing waves in time.** Reject the time-decoupling that comes with the "directionless" reading. Particles must have at least one compact direction coupled with time — i.e., they have a definite direction of propagation around at least one part of the knot. This brings back the possibility of charged single-Fourier-mode-like particles, with the question of how to interpret the resulting two U(1)s.

(c) **The "directionless" principle applies to spatial direction but not temporal direction.** A particle is sign-conjugate-symmetric in spatial reflection of (m, n) but can have a definite forward time direction. This would mean the standing wave is in time-evolved spatial pattern, not in time itself. Mathematically this is the case for any wave packet that has positive frequency only — a one-time-direction wave that's spatially symmetric.

Reading (c) is interesting. Let me check it.

### 10.7 Reading (c) — spatial symmetry, time-forward propagation

Consider a wave that's spatially symmetric in (m, n) ↔ (−m, −n) but time-forward only:

$$
\varphi = \alpha \cdot e^{i(k_u u + k_w w - \omega t)} + \alpha \cdot e^{i(-k_u u - k_w w - \omega t)} + \text{c.c.}
$$

Take real part (and pull out the complex amplitude α = |α|·e^{iδ}):

$$
\varphi_{\text{real}} = 2|\alpha|\cdot\bigl[\cos(K_+ - \omega t + \delta) + \cos(-K_+ - \omega t + \delta)\bigr] = 4|\alpha|\cdot\cos(K_+)\cos(\omega t - \delta)
$$

where K_+ = k_u u + k_w w. **This is the same as the sign-conjugate standing wave** — time-decoupled, T_tu = T_tw = 0. Reading (c) collapses to the sign-conjugate standing wave for a real field.

For a complex field, this would be different: a single-frequency spatially-symmetric wave can carry net momentum in time. But the framework uses real fields ([Ch 1 §6](01-foundation.md)), so reading (c) doesn't give a separate option.

### 10.8 The practical conclusion

Reading (a) appears to be the only consistent path. **The framework as currently structured cannot produce EM charge from internal T² mode structure on a real field under the standing-wave principle.** EM charge must come from a substrate-level ingredient — substrate-level chirality from grid-primitive that breaks (++) ↔ (−−) balance through a mechanism not captured by σ_uw or any other current metric ingredient.

This is a clean, math-derived conclusion. It says:

- **Mass** is intrinsic to the particle (sign-conjugate standing wave on a chiral knot).
- **Chirality** (the σ_uw signature) is intrinsic — encoded in the T_uw the particle sources.
- **EM charge** is *not* intrinsic to the standing-wave particle. It requires an external ingredient.

The user's earlier hypothesis about substrate-level chirality being the source of matter/antimatter asymmetry comes back into play here. It might be the same mechanism: substrate chirality breaks the (++) ↔ (−−) balance, producing particles with built-in amplitude asymmetry whose residual T_tu, T_tw is what we observe as EM charge.

The framework cannot derive this from its current ingredients. It can describe what would happen *given* substrate-induced amplitude asymmetry, and confirm the residual cross-terms have the form of EM gauge potentials. But the *origin* of the asymmetry is not in metric-charge — it's in the substrate.

This is consistent with the framework's project structure: charge at L3 (metric-charge) inherits from the wrap-promotion ladder, which inherits from grid-primitive's substrate. If grid-primitive's edges have chirality, that propagates upward and provides the boundary condition that breaks (++) ↔ (−−).

---

## 11. What this would mean for the framework

If Reading C with the σ_uw-mediated charge mechanism holds up, the framework restructures significantly:

- **Closure rule** is no longer "synchronization on a single Fourier mode." It becomes: *what kind of particle (sign-conjugate standing wave on what knot) produces what kind of σ_uw and what residual charge under interaction.*
- **Single-axis modes** (m, 0) or (0, n): sign-conjugate standing wave gives k_u·k_w = 0, so T_uw = 0. They source no σ_uw shear and produce no chirality field. They cannot induce charge in others. Genuinely neutrino-like.
- **Synchronization-failure** genuine torus knots T(p, q) with p, q ≥ 2: sign-conjugate pair sources T_uw = k_u·k_w ≠ 0 (some chirality field). They can induce charge in other particles. Possibly *not* mass-only after all — they're chirality-active.
- **The two-U(1)s puzzle:** dissolves naturally. There's no "second gauge field" — there's σ_uw (an intrinsic per-particle field) and EM (an induced residual under interaction). Single observable U(1) at the particle-level for charged particles.
- **Matter/antimatter:** plausibly tied to direction of (++) ↔ (−−) amplitude bias, controlled by substrate chirality. Genuinely a substrate-level phenomenon as the user hypothesised earlier.

This is a substantial reorganization. It needs careful checking. Specifically:

- **Open derivation 1:** make the σ_uw-mediated charge mechanism quantitative. Compute the amplitude bias induced by an external σ_uw shear, the resulting residual T_tu, T_tw, and confirm the induced "charge" has the structure (sign, magnitude scaling) of standard EM charge.
- **Open derivation 2:** check the static two-particle case. Particle A's σ_uw shear induces charge in particle B; B's residual charge produces an EM field that A responds to. The mutual interaction should yield a Coulomb-like force law in the appropriate limit.
- **Open derivation 3:** match with α (the fine-structure constant). If charge is residual asymmetry under σ_uw-mediated interaction, then α should be expressible in terms of the σ_uw field strength and the standing-wave amplitude bias coefficient. This is potentially the geometric origin of α the project flags as an open question.

---

## 12. Open questions / next steps

The math is sound for what's been derived (sections 3–6 are explicit and unambiguous). What remains open and substantive:

1. **Is the σ_uw-mediated charge mechanism quantitatively right?** Specifically, does an external σ_uw shear produce an amplitude bias in a sign-conjugate standing wave that yields a residual T_tu, T_tw with the right structure to be called "EM charge"? Worth working through the algebra explicitly.

2. **Does the framework's closure rule (m | n with both nonzero) survive in any form?** Under Reading C, the closure rule's significance shifts — the relevant condition might be "the particle's sign-conjugate standing wave has non-zero T_uw" (which is k_u·k_w ≠ 0, equivalent to both windings nonzero — but without the m | n synchronization piece). This needs revisiting.

3. **What is the chirality-conjugate cancellation pair under Reading C?** The (++) + (+−) configuration (Ch 6 §6.6's "fourth neutrality mechanism") is no longer a "particle" under the user's knot-asymmetry principle — it's a non-physical superposition of two different knots. Its existence might be a calculational artifact of having ignored the chirality-as-distinguishability constraint.

4. **What is the difference between particle and antiparticle under Reading C?** The (−−) component is the backward traversal, not antiparticle. If matter and antimatter are physically distinct, they correspond to *different chirality knots* (T(m, n) vs T(m, −n)) — not to forward/backward of the same knot. The matter/antimatter axis is then chirality, not orientation. This is a substantial reframing of [Ch 6 §2](06-handedness-and-pairs.md).

5. **Do the framework's existing four-mechanism neutrality table and closure rule need to be redesigned?** Likely yes. Sign-conjugate standing waves with k_u·k_w = 0 (single-axis) are neutrinos; with k_u·k_w ≠ 0 are chirality-active. Chirality-conjugate pairs are arguably non-physical under the user's principle. The current Ch 4–6 structure would need to absorb these revisions.

---

## 11. Reading C+: closure rule from chirality degeneracy

A revisit of §§7–10 with the user's knot-asymmetry principle as a hard constraint produces a substantively cleaner result than I gave in §10.

### 11.1 What the user's principle actually says

"Only one fits the specific knot solution" — combine *only* configurations that correspond to the same physical knot. Whether two configurations correspond to the same knot depends on **whether the knot is topologically distinguishable from its mirror** in 3-space.

- **T(m, n) and T(−m, −n):** same unoriented closed curve, opposite traversal direction. Always the same knot, regardless of chirality status. *Combining is always natural.*
- **T(m, n) and T(m, −n):** different oriented closed curves; mirror images. Whether they are the same *knot* depends on whether the underlying mirror knot is topologically distinct from the original.

For the topological side: a torus knot T(p, q) with both p, q ≥ 2 and gcd(p, q) = 1 is a *genuine* torus knot — the right-handed and left-handed versions are chirally distinct in 3-space (different knot types). For T(1, q), the curve is the *unknot* in 3-space, and mirrors of the unknot are the unknot — chirality is *degenerate* topologically.

### 11.2 The two cases produce two different "particles"

**Case A: Closure-satisfying knots (m | n with both nonzero, gcd-reduces to T(1, q)).** The knot is topologically the unknot (or k-component unlink for multi-link cases). Chirality is degenerate — the right-handed and left-handed versions are the same knot. Combining chirality-conjugates is therefore *also natural*; nothing topologically distinguishes them.

The natural particle is the **chirality-conjugate pair** — e.g., {(++), (−+)} for the (m, n) sector, giving (after the cos·cos identity)

$$
\varphi = 2A\cdot\cos(k_u u)\cdot\cos(k_w w - \omega t)
$$

— *standing in u, traveling in w*. From §5: T_tu = 0, T_tw = −A²·ω·k_w/4 (non-zero).

**Mass + one U(1) charge under B_μ.** Single observed gauge potential. Resolves the two-U(1)s puzzle.

**Case B: Closure-failing knots (m ∤ n with both m, n ≥ 2).** Genuine torus knots. Chirality is topologically distinguishing — T(p, q) and T(p, −q) are *different knots* in 3-space. Combining chirality-conjugates is *not* natural under the user's principle.

The only natural combination is the **sign-conjugate pair on a specific chirality** — {(++), (−−)} for one chirality, {(+−), (−+)} for the other. Each is a directionless standing wave on a specific chiral knot. From §4: T_tu = T_tw = 0; T_uw = +k_u·k_w (chirality signature) for the right-handed chirality, −k_u·k_w for the left-handed.

**Mass only, plus chirality-encoded T_uw.** No EM gauge potential.

### 11.3 The closure rule re-derived

The framework's closure rule "m | n with both nonzero" is exactly the condition for a knot to gcd-reduce to T(1, q). It is also exactly the condition for the knot to be topologically the unknot (or unlink) — i.e., for chirality to be degenerate. **The closure rule is the condition under which the chirality-conjugate pair is a natural particle construction.**

This is a substantively cleaner derivation of the closure rule than the original synchronization argument:

- *Original framing (Ch 1 §10, Ch 4):* "during traversal, every time the tube-direction phase crosses zero, the ring-direction phase also crosses zero — this gives synchronization, which gives observable EM."
- *Standing-wave framing (this section):* "the knot is topologically the unknot, so the chirality-conjugate pair is a natural particle construction; that pair is partial-standing in one direction and traveling in the other, giving one EM gauge potential."

Both framings select the same set of (m, n): m | n with both nonzero. But the standing-wave framing has clearer physical content — it tells us *what the particle is* (a partial-standing wave) and *why it has charge* (chirality-conjugate combination is natural for unknots and produces traveling-in-one-direction structure).

### 11.4 Single-axis modes under this framing

Single-axis modes T(m, 0) or T(0, n) — one winding zero. Sign-conjugate pair {(m, 0), (−m, 0)} combines into a standing wave on a single compact direction. By metric-mass §7's analysis (extended trivially to the 2D embedding), this is mass-only with no cross-terms. **Single-axis modes are mass-only**, consistent with the framework's existing characterization.

The chirality-conjugate combination doesn't apply for single-axis modes (there's no n to flip in (m, 0)). So the only natural particle on a single-axis configuration is the sign-conjugate standing wave — mass only.

### 11.5 The full inventory under standing-wave reading + knot-asymmetry constraint

| Knot class | Topologically | Natural particle construction | Cross-term sourced | Type |
|---|---|---|---|---|
| (0, 0) | nothing | — | — | Light, no compact structure |
| (m, 0), (0, n) — single-axis | trivial cycle | sign-conjugate standing wave | None (T_uw = 0 since one k vanishes) | **Mass-only** |
| T(1, q) primitive — closure-satisfying | unknot | chirality-conjugate (chirality is degenerate) | T_tu (or T_tw) — one U(1) | **Mass + one charge** |
| k × T(1, q) multi-link — closure-satisfying | k-component unlink | chirality-conjugate per component | T_tu (or T_tw) — one U(1), summed across k components | **Mass + 1/k charge per component** |
| T(p, q), p,q ≥ 2, gcd = 1 — closure-failing | genuine torus knot | sign-conjugate standing wave on a specific chirality | T_uw = ±k_u·k_w (chirality signature); no EM | **Mass + chirality field** |

The framework's closure rule and its mass-only / charged distinction emerge cleanly from the standing-wave principle plus the user's knot-asymmetry constraint. **No two-U(1)s puzzle. No σ_uw-as-Sakharov-CP. No matter/antimatter from σ_uw.**

### 11.6 Where matter/antimatter comes from under this reading

Two distinct asymmetries are now visible at the framework level:

- **Knot orientation** (sign reflection (m, n) ↔ (−m, −n)): same knot, reversed traversal. For closure-satisfying knots (T(1, q)), this is *both halves of the same chirality-conjugate pair particle* — they're not separate states, they're combined into one particle with one charge sign.
- **Knot chirality** (mirror reflection (m, n) ↔ (m, −n) for genuine torus knots, or for closure-satisfying knots, the choice of which chirality-conjugate pair to form): for genuine torus knots, two distinct mass-only particles (one per chirality). For closure-satisfying knots, the chirality-conjugate pair always combines both chiralities, so chirality is degenerate at the particle level.

Where does charge sign come from? The closure-satisfying chirality-conjugate pair has two natural variants:
- {(m, n), (−m, n)} — standing in u, traveling in w. T_tw with sign −ω·k_w → "+B_μ charge."
- {(m, n), (m, −n)} — traveling in u, standing in w. T_tu with sign −ω·k_u → "+A_μ charge."

These are different particles (one charge under A_μ, the other under B_μ). They are not particle/antiparticle — they are particles with different *which compact direction* they circulate in.

Where do +charge and −charge particles come from for the SAME compact direction?

The {(m, n), (−m, n)} chirality-conjugate sums two modes with k_w = +const. The corresponding "antiparticle" would have k_w = −const — i.e., the {(m, −n), (−m, −n)} pair. By similar math, this particle has T_tw = +ω·k_w/4 — opposite sign. So:

- Matter (charge under B_μ, sign −): {(m, n), (−m, n)}
- Antimatter (charge under B_μ, sign +): {(m, −n), (−m, −n)}

These are particle and antiparticle. They are *different chirality-conjugate pairs*: one combines positive-w-direction Fourier modes, the other combines negative-w-direction Fourier modes.

So matter/antimatter axis = sign of the w-direction circulation = sign of n in the chirality-conjugate pair construction. The asymmetry that distinguishes matter from antimatter is what populates one chirality-conjugate-pair structure over the other in the universe.

What populates one over the other? Some substrate-level mechanism that breaks the n ↔ −n symmetry. Candidates:
- σ_uw shear (since σ_uw breaks the chirality (m, n) ↔ (m, −n) reflection per [Ch 6 §6](06-handedness-and-pairs.md)) — exactly the right kind of symmetry breaking!
- Substrate chirality from grid-primitive
- Initial conditions

**σ_uw is the matter/antimatter mechanism after all** — but it works at the *population* level, not the *single-particle* level. σ_uw biases the population of {(m, n), (−m, n)} over {(m, −n), (−m, −n)} in thermal equilibrium, producing more matter than antimatter.

This is consistent with everything the framework already has, including [Ch 6 §6](projects/metric-charge/06-handedness-and-pairs.md) and [Ch 8 §3](projects/metric-charge/08-shear-and-fractional-charge.md) which derived that σ_uw breaks chirality. The chirality bias *is* the matter/antimatter bias under the standing-wave reading — they're the same axis. Earlier framings of those chapters identified them as different axes; the standing-wave reading unifies them.

### 11.7 Caveat — does this match the user's intuition?

The user's recent observation: *"In metric-mass… when it is standing, we can't tell the difference. Two solutions, both are true and so cancel. In the case of a charge-from-light, we have a 2D sheet. The knots are not rotationally symmetric. A trip around one way is different from a trip around the other way. … I don't think the two solutions (if there are two) cancel at the promotion level of charge. I think either they add, subtract, or we should be able to show that only one fits the specific knot solution."*

This points away from "the standing-wave principle applies the same way in 2D as in 1D" — and toward "the two traversal directions of T(m, n) in 2D are physically distinguishable (unlike in 1D) and therefore should *not* cancel into a standing wave."

§11 above argued that for closure-satisfying knots (unknots in 3-space), chirality is topologically degenerate, so chirality-conjugate combinations are natural — and that chirality-conjugate pair *is* the partial-standing-wave that gives one EM charge. **But §11 still uses the sign-conjugate cancellation for the directions of traversal of the same knot.**

If the user's intuition is that *neither* sign-conjugate *nor* chirality-conjugate combinations cancel in 2D — that the traversal directions on a 2D knot are physically distinct enough that the wave doesn't naturally combine into a standing wave at all — then the framework's particle in metric-charge would be a **single Fourier mode** at definite (m, n). This is **Reading B** from §9, with both T_tu and T_tw alive — two cross-terms.

To resolve "two cross-terms vs one observed U(1)" under Reading B without invoking the standing-wave principle: the framework would need the metric-mass interpretation that h_μu is "mass-related" (gravitational-flavored) and h_μw is the EM gauge potential, picked out by the wrap-order convention (w as tube). Then a single Fourier mode produces:

- Mass (from T_tt)
- "Mass-related cross-term" h_μu (gravitational-like effect, per metric-mass framing) — the calculable mass-bends-light mechanism
- EM gauge potential h_μw (KK-style) — the actual EM field

One observed U(1) per particle (the EM one). The other cross-term is reinterpreted as a gravitational-flavored mechanism, not a separate gauge field.

This **inherits the metric-mass framing** (h_μu = mass-related) rather than the standing-wave reading. Different choice; consistent with the user's "two directions in 2D don't cancel" observation.

### 11.8 Two candidate readings, side by side

| Question | Reading C+ (§11.1–§11.6) | Reading B+ (§11.7) |
|---|---|---|
| Particle on T(1, q) | Chirality-conjugate pair (partial standing wave) | Single Fourier mode (single direction of traversal) |
| Sign-conjugate cancellation | Applies (mass only on closure-failing knots) | Does *not* apply (closure-satisfying particles keep both cross-terms) |
| Chirality-conjugate combination | Natural for unknots (chirality degenerate); gives one EM charge | Not used; particle is single direction on a single chiral knot |
| Inheritance from metric-mass | Standing-wave principle applies | metric-mass framing of h_μu as mass-related applies |
| Number of cross-terms a charged particle sources | 1 (the traveling direction) | 2 (both u and w cross-terms) |
| How to interpret 2 cross-terms | Doesn't apply — only 1 sourced | One is mass-related (h_μu), one is EM (h_μw); convention picks |
| Closure rule | Re-derived from chirality-degeneracy condition | Inherited as-is from current Ch 4 (synchronization, not yet re-derived) |
| Two-U(1)s puzzle | Resolved structurally | Resolved interpretively (one U(1) is mass-related, not gauge) |
| Matter/antimatter source | σ_uw biases chirality-conjugate pair populations | Either σ_uw at population level, or substrate chirality from grid-primitive |
| User's "two directions don't cancel in 2D" | **Tension** — sign-conjugate pair still cancels | **Consistent** — single Fourier mode keeps both cross-terms |

The user's recent observation favors Reading B+. §11's earlier framing (Reading C+) inherits the standing-wave principle uniformly across metric-mass and metric-charge — internally clean but possibly contradicts the user's "knots are not rotationally symmetric" point.

The math of §§3–6 supports either reading. The choice is interpretive — the user's call.

### 11.9 Summary of the standing-wave reading

The picture that emerges:

| Concept | Standing-wave reading |
|---|---|
| Particle on closure-satisfying T(1, q) | Chirality-conjugate pair {(m, n), (−m, n)} — partial-standing wave |
| Charge | T_tw (or T_tu) sourced by the traveling direction — one U(1) per particle |
| Mass | Energy density T_tt — present for any particle |
| Particle on closure-failing T(p, q) | Sign-conjugate pair on a specific chirality — directionless standing wave |
| Mass-only category | T(p, q) sign-conjugate pairs (chirality matters, no charge) plus single-axis modes |
| Antiparticle | Same form as particle but with opposite-sign compact-direction circulation — different chirality-conjugate pair |
| σ_uw bias | Breaks chirality (m, n) ↔ (m, −n), which under this reading IS the matter/antimatter axis |
| Two U(1)s issue | Resolved — each particle uses only one U(1) (whichever direction it's circulating in); the other compact direction is in standing-wave mode |
| Closure rule | Re-derived from chirality-degeneracy condition — same set of (m, n) but cleaner physical content |

This is internally consistent, derived from the math of §§3–6 plus the user's knot-asymmetry principle, and matches standard physics' single-U(1)-per-particle and matter/antimatter axes.

## Recommendation

§§3–6 establish the math (cleanly, no controversy — pure algebra of Fourier-mode stress-energy on T²). §§7–10 explore the standing-wave reading and find that under strict application of the user's metric-mass principle plus a uniform sign-conjugate-cancellation rule, the framework predicts only mass particles. §11 offers two candidate resolutions and notes a tension between them.

The two candidate readings — Reading C+ (§11.1–§11.6) and Reading B+ (§11.7) — both produce one observed U(1) per charged particle and resolve the two-U(1)s puzzle, but they do so via different particle constructions:

- **Reading C+** keeps the standing-wave principle and uses sign-conjugate-cancellation for closure-failing knots, but uses chirality-conjugate-pair partial-standing-waves for closure-satisfying knots. Re-derives the closure rule from chirality-degeneracy.
- **Reading B+** drops the standing-wave principle for metric-charge (consistent with the user's "two directions don't cancel in 2D" observation) and uses single Fourier modes as particles. Inherits the metric-mass framing of h_μu as a mass-related cross-term to interpret the second cross-term.

The user's most recent observation favors B+ (knots not rotationally symmetric → traversal directions don't combine into standing waves like in 1D). C+ is internally cleaner but requires the standing-wave principle to apply uniformly across both projects, which the user's observation challenges.

**Suggested next steps, depending on which reading the user prefers:**

If **Reading B+**: write up the "two cross-terms, two interpretations (mass-related vs EM)" framing as the central derivation. Decide whether the wrap-order convention picks h_μu as mass-related and h_μw as EM, or the other way. Verify consistency with metric-mass's recent rewrite (which will need a small framing adjustment — metric-mass needs to acknowledge that under the 2D extension, the standing-wave reading doesn't carry over and the per-component mode IS the particle when there are two compact directions).

If **Reading C+**: verify the chirality-conjugate-pair particle inventory explicitly (walk through T(1, 2), T(2, 3), 3×T(1, 2) in detail with full T_μν computation), and check whether the closure rule re-derivation from chirality-degeneracy actually produces the same set of (m, n) as the synchronization rule (it should, but verify).

If **neither** matches the user's intent: the user can describe what they have in mind and we adjust.

The math through §6 is committed. §§7–11 are interpretive synthesis open to revision. The work file is ready for evaluation.
