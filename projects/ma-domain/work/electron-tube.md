# electron-tube.md — convex-only tube profile with T(1, 2) as the favored mode

**Status:** Working hypothesis / how-to. Documents the geometric construction that makes T(1, 2) the lightest mode on a convex-only (lobe-only, no saddles) tube cross-section, and the project history that motivates favoring T(1, 2) over T(1, 1) as the electron candidate.

**Cross-references:**
- [candidates.md](candidates.md) — ma-domain's three topology candidates; charged leptons are already placed at T(1, 2) in B and C
- [sheet-proton clover-mass §4](../../sheet-proton/work/clover-mass.md) — mass formula μ² = (m_r − σ_eff m_t)² + (m_t/ε)² and σ_eff = σ + 2τ derivation
- [sheet-proton clover-quarks §11](../../sheet-proton/work/clover-quarks.md) — boundary identification k_θ = m_r − τ m_t
- [reference/WvM-summary.md](../../../reference/WvM-summary.md) — Williamson & van der Mark (1997): "the electron is a photon of (1, 2) toroidal topology"

---

## 1. Goal

Find the simplest *convex-only* tube cross-section (no concave/saddle regions, since concave regions induce fractional Z_n charge — undesired for an integer-charge lepton) for which the lowest-mass closure mode is **T(1, 2)** (one tube wind, two ring winds) rather than T(1, 1).

Why we want this:
- **WvM topology.** Williamson & van der Mark's 1997 hypothesis identifies the electron with a (1, 2) confined-photon double-loop. Their spin-½ argument depends *structurally* on the q = 2 ring winding — a (1, 1) topology cannot reproduce a fermion. (See §6 below.)
- **metric-charge closure rule.** Closure-satisfying modes are exactly T(1, n) for n ∈ ℤ \ {0}; T(1, 1) and T(1, 2) are the two lowest. We want a tube where T(1, 2) sits below T(1, 1) energetically — so the natural ground state of the integer-charge sector is the WvM electron.
- **ma-domain candidate consistency.** Candidates B and C in [candidates.md §1.2](candidates.md) place each of e, μ, τ at T(1, 2) on its host dim-pair, with per-pair σ_eff as a free parameter. This document supplies the geometric construction that makes T(1, 2) the natural lowest mode on those pairs.

---

## 2. Mass formula on a convex-only tube

The torus is parameterized by (θ, φ) with θ ∈ [0, 2π) the **ring** direction and φ ∈ [0, 2π) the **tube** direction. The embedding has two intrinsic parameters:
- **τ** — *twist rate*: the cross-section rotates by 2πτ as you traverse the ring once. Encoded in the off-diagonal metric component g_θφ and in the boundary identification.
- **σ** — *rolled-leaf shear*: a constant shear of the cross-section relative to the ring direction. Encoded in g_θφ only, not the boundary identification (per sheet-proton clover-quarks §10.5).

The flat-limit mass formula for Bloch wavemodes (m_t, m_r) ∈ ℤ × ℤ ([clover-mass §4](../../sheet-proton/work/clover-mass.md)):

<!-- μ² = (m_r − σ_eff · m_t)² + (m_t/ε)² -->
$$
\mu^2_{(m_t,\,m_r)} \;=\; \bigl(m_r - \sigma_{\text{eff}}\,m_t\bigr)^2 \;+\; \bigl(m_t/\varepsilon\bigr)^2
$$

where ε is the tube/ring size ratio and σ_eff is the effective cross-coupling. **σ_eff has two regimes**:

| Boundary identification | σ_eff | Why |
|---|---|---|
| Non-trivial monodromy (e.g., clover at τ = 1/3, ellipse at τ = 1/2) | **σ + 2τ** | τ enters twice — once in the boundary identification (k_θ = m_r − τ m_t) and once in the metric dispersion |
| Trivial monodromy (cross-section maps back to identity after one ring rev) | **σ + τ** | τ enters only via the metric; boundary identification gives k_θ ∈ ℤ |

For a convex-only profile aimed at integer-charge modes, we want **trivial monodromy** (so k_θ ∈ ℤ, no Z_n fragments). Then **σ_eff = σ + τ**.

---

## 3. The flip condition: σ_eff > 3/2

The cross-section term (m_t/ε)² is identical for T(1, 1) and T(1, 2) — both have m_t = 1. The ordering is fixed entirely by which |m_r − σ_eff| is smaller:

<!-- |2 − σ_eff| < |1 − σ_eff|  ⟺  σ_eff > 3/2 -->
$$
|2 - \sigma_{\text{eff}}| \;<\; |1 - \sigma_{\text{eff}}|
\;\;\Longleftrightarrow\;\;
\sigma_{\text{eff}} \;>\; 3/2
$$

The clean sweet spot is **σ_eff = 2**: at this value, T(1, 2) becomes a *zero-effective-ring-momentum* mode, m_r − σ_eff m_t = 0, with mass given purely by the cross-section term:

- T(1, 1): μ² = (1 − 2)² + 1/ε² = **1 + 1/ε²**
- **T(1, 2): μ² = (2 − 2)² + 1/ε² = 1/ε²**   ← lightest m_t = 1 mode
- T(1, 3): μ² = (3 − 2)² + 1/ε² = 1 + 1/ε²  (degenerate with T(1, 1))
- T(1, 0): μ² = (0 − 2)² + 1/ε² = 4 + 1/ε²  (heavier)

At σ_eff = 2 the mass of the electron mode is **μ_e = 1/ε** — set entirely by the cross-section size, with no ring-momentum contribution. This is structurally analogous to the clover's T(1, 1) at σ_eff = 2/3 (the proton's "zero-effective-ring-momentum" mode), but on a different sector.

---

## 4. Why a featureless circle won't do it

A perfectly circular cross-section has continuous rotational symmetry, so both τ and σ are pure gauge — you can re-parameterize φ to set them to zero. The metric appears non-trivial in any single chart, but the surface is intrinsically just an ordinary torus. So **circle + "twist" ≡ circle + nothing**. To make τ (or σ) physically meaningful the cross-section must break rotational symmetry — even an ellipse (C_2) is enough.

This is consistent with WvM's "twisted strip" picture (§2 of the paper): the strip *has a face*, which breaks rotational symmetry. A featureless circular tube would not.

---

## 5. Three working constructions

To achieve σ_eff = 2 with trivial monodromy (integer k_θ) and a convex-only profile, we have several geometric routes:

| # | Profile | τ | σ | σ_eff | Geometric picture |
|---|---|---|---|---:|---|
| **A** | Ellipse (C_2) | **2** | 0 | 2 | Major axis spins **2 full turns** per ring revolution |
| B | Ellipse (C_2) | 1 | 1 | 2 | One full spin **plus** rolled-leaf shear σ = 1 |
| C | Pentagon (C_5) or higher | 2 | 0 | 2 | High-symmetry convex bulge spins 2× per ring rev |

All three give σ_eff = 2 and put T(1, 2) at the floor. Construction A is the minimal choice — it uses the lowest-symmetry non-circular convex profile (an ellipse) and a single geometric parameter (τ = 2) to do the work.

### 5.1 Why τ = 2 for an ellipse?

On an ellipse (C_2 symmetry), the cross-section maps to itself under any 180° rotation. So allowed twist values are τ ∈ {0, 1/2, 1, 3/2, 2, ...} (half-integer multiples). Of these:

| τ | Monodromy after 1 ring rev | k_θ quantization | σ_eff (with σ = 0) | Lightest m_t = 1 mode |
|---:|---|---|---:|---|
| 0 | identity | integer | 0 | T(1, 0) |
| 1/2 | 180° rotation (Z_2) | half-integer | 1 | T(1, 1), *fractional charge* |
| 1 | 360° = identity | integer | 1 | T(1, 1), integer charge |
| 3/2 | 540° ≡ 180° (Z_2) | half-integer | 3/2 | T(1, 1) / T(1, 2) degenerate, fractional charge |
| **2** | **720° = identity** | **integer** | **2** | **T(1, 2), integer charge** |

τ = 2 is the **smallest twist** on an ellipse that:
1. Has trivial monodromy (cross-section back to identity → k_θ integer → integer charge), AND
2. Achieves σ_eff ≥ 2 (so T(1, 2) is the unique lightest m_t = 1 mode).

τ = 1 gets only σ_eff = 1 (T(1, 1) wins). τ = 1/2 gets σ_eff = 1 *and* fractional charge (wrong for an electron). τ = 3/2 sits right at the degeneracy with fractional charge. Only **τ = 2 cleanly delivers integer-charge T(1, 2)-lightest**.

---

## 6. Why T(1, 2) over T(1, 1): three independent reasons from prior work

Even setting aside the geometric question of which tube makes T(1, 2) lighter, **three independent threads in this project already favor T(1, 2) over T(1, 1) for the electron**:

### 6.1 WvM (1997): spin-½ requires the double loop

The Williamson & van der Mark paper postulates the electron as a single confined photon of (1, 2) toroidal topology. The spin-½ derivation is *structural* and depends specifically on q = 2 ring winds:

The photon carries angular momentum ℏ at frequency ω. The confined photon completes its closed orbit only after the field vectors rotate through **720°** — i.e., the closure path winds the ring **twice** for each tube wind. So the effective rotational frequency is ω_s = 2ω, and:

<!-- L = U / ω_s = ℏω / 2ω = ℏ/2 -->
$$
L \;=\; U/\omega_s \;=\; \hbar \omega / (2\omega) \;=\; \hbar/2
$$

By the spin-statistics theorem, "field vectors rotate through 720° before returning to the same orientation" → fermion. This is the topological origin of spin-½ in WvM.

**A (1, 1) topology fails this argument.** With q = 1, the closed orbit winds the ring once → the field returns to its orientation after 360°, not 720° → ω_s = ω, giving L = ℏ (boson-like spin 1), not ½. **T(1, 1) cannot be a fermion in the WvM framework**. (See [WvM-summary §7](../../../reference/WvM-summary.md#7-spin-4).)

### 6.2 WvM: the "twisted strip" charge mechanism requires (1, 2)

WvM model the electron as a twisted strip of paper representing one wavelength of a circularly polarized photon (Fig. 1a). When the strip's ends are joined with "exactly one full twist" preserved, the path naturally becomes a **double loop** (Fig. 1b) — this is the (1, 2) topology. The construction has the remarkable property:
- One side of the strip always faces outward
- E ⊥ strip face → E always points radially **inward** (electron) or always **outward** (positron)
- The (1, 2) topology is what makes the field-rotation and the orbital-rotation commensurate, so E doesn't flip sign as the photon orbits

WvM emphasize: "Exactly one full twist is required; a half twist or double twist would not give rise to a charge." A (1, 1) closure forces either zero or two twists of the strip — neither preserves the inward-pointing E that gives the electron its charge. **The geometric mechanism that produces ~0.91e from the (1, 2) topology does not function for (1, 1)**.

This is the "rotational polarization" you referenced — the field vectors complete *one rotation* (matching circular polarization of the constituent photon) over the closed (1, 2) path. The match between the photon's intrinsic spin-rotation and the orbital rotation is the *whole content* of WvM's electron model.

### 6.3 ma-domain candidates already place leptons at T(1, 2)

In [candidates.md §1.2](candidates.md), all three working topology candidates (A, B, C) carry electron-sector assignments to T(1, 2):

> "Each of the three pairs in the [electron] delta hosts one charged lepton at its lowest closure mode T(1, 2) — no within-pair doublet on leptons (Q = ±1 doesn't need the lobe/saddle split that quark fractional charges require)."

The fits in [outputs/candidate_fits.txt](../outputs/candidate_fits.txt) reach 0.000% error on (e, μ, τ) masses *using T(1, 2) modes only* with per-pair σ_eff values as free parameters. The values found by the fit need a structural reason — this document supplies that reason: **T(1, 2)-lightest is automatic on a convex-only ellipse-tube with twist τ = 2**.

### 6.4 metric-charge: closure rule admits both T(1, 1) and T(1, 2)

The closure-condition derivation in [metric-charge chapter 4](../../metric-charge/04-the-closure-condition.md) admits exactly T(1, n) for n ∈ ℤ \ {0}. So *both* T(1, 1) and T(1, 2) are admissible as closure modes — the closure rule alone does not select between them. The question of *which closure mode is the ground state* is a geometric question (set by σ_eff), and that's what the construction in §5 answers.

So: closure admits both; WvM requires (1, 2); ma-domain assumes (1, 2); the proposed geometry delivers (1, 2) as the natural ground state on a convex tube.

---

## 7. Recommendation

For an electron sheet in the ma-domain framework:

**Cross-section:** Ellipse (C_2 symmetry — the lowest-symmetry convex profile that admits non-trivial twist). Aspect ratio is a free parameter; the only requirement is that the cross-section is *not* a perfect circle.

**Embedding twist:** τ = 2 — the cross-section's major axis traces a double helix, completing two full revolutions per ring revolution.

**Rolled-leaf shear:** σ = 0 (none needed; the twist alone gets σ_eff = 2).

**Result:**
- Boundary identification: trivial monodromy → k_θ ∈ ℤ → all modes integer-charge ✓
- Mass formula: μ² = (m_r − 2 m_t)² + (m_t/ε)²
- Ground state of m_t = 1 sector: **T(1, 2)** with μ_e = 1/ε ✓
- Mass scale set by cross-section size 1/ε — a single geometric parameter, predictively tidy

This is the geometric realisation of the WvM electron postulate inside the ma-domain framework: a convex-only twisted ellipse tube where the WvM (1, 2) double-loop sits at the energetic floor.

---

## 8. Open questions

1. **Does the spin-½ derivation transfer cleanly?** WvM's spin argument uses a confined photon with fixed total angular momentum. The metric-charge / ma-domain framework treats wavemodes as Bloch states on a compact surface. The structural argument ("field vectors return to orientation after 720° → fermion") should carry over, but a clean derivation of L = ℏ/2 from T(1, 2) on the ellipse-tube has not been written down here.

2. **What sets ε (the cross-section size)?** The ground-state mass is μ_e = 1/ε, so the electron mass fixes ε. In WvM, the size is constrained to be approximately the Compton wavelength λ_C; here, ε would correspond to L_minor / L_major of the host dim-pair in the candidates.md fits. Are these consistent?

3. **Is τ = 2 stable against geometric fluctuations?** A small deviation in the twist (τ = 2 − δ) keeps σ_eff just below 2 and the cross term (m_r − σ_eff m_t)² becomes δ² for T(1, 2), so the ground state is perturbed but doesn't switch. The construction is robust at the leading order, but second-order corrections (analogous to clover-mass §6) have not been computed.

4. **Why ellipse rather than higher-C_n?** Aesthetic minimality. A C_5 or C_6 profile with τ = 2 also works (still σ_eff = 2), but adds rotational symmetry that the WvM strip picture does not require. The ellipse matches the WvM "strip with a face" most directly.

5. **Connection to per-pair σ_eff values in candidates.md.** The fits report σ_eff ∈ [1.684, 1.976] for quark pairs and presumably ≈ 2 for lepton pairs (since T(1, 2) is the ground state on each lepton pair). Confirming that the fitted σ_eff values are physical (i.e., correspond to realisable τ, σ combinations) is the natural next step.

---

## 9. Summary

A convex-only tube cross-section can be made to host T(1, 2) as its lightest m_t = 1 mode by twisting it. The simplest such construction is an **ellipse cross-section with twist rate τ = 2** per ring revolution. This gives:
- Trivial monodromy → integer charge (no fractional Z_n sectors)
- σ_eff = 2 → T(1, 2) is the unique zero-effective-ring-momentum mode
- Mass scale μ_e = 1/ε, set by cross-section size alone

The construction lands exactly where three independent project threads converge: WvM's (1, 2) electron, metric-charge's closure rule, and ma-domain's candidate fits. The "rotational polarization" of WvM — the photon's intrinsic field rotation commensurate with the orbital double-loop — is what makes the (1, 2) topology naturally a fermion and naturally charged; the geometric construction supplies the rest.
