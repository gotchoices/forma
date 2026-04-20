# R60 Track 15: Sandboxed (3, 6) proton viability test

**Scope.**  Sandboxed empirical test of whether (3, 6) can
replace (1, 3) as the proton mode in model-F's architecture.
Motivated by R62 derivation 7b, which derives spin = n_t/n_r
(WvM ratio rule) from CP field rotation on the 2-torus.  Under
the ratio rule, (1, 3) has spin 1/3 (invalid for proton) and
(3, 6) has spin 1/2 (valid).

Also tested as a bonus: (1, 2) proton (simplest ratio-rule-
compliant alternative).

**No changes to model-F, R60 Tracks 1–14, or any prior scripts.**
All work in new scripts with `track15_` prefix.

Scripts:
- [track15_phase1_mass.py](scripts/track15_phase1_mass.py)
- [track15_phase2_alpha.py](scripts/track15_phase2_alpha.py)
- [track15_phase3_nuclear.py](scripts/track15_phase3_nuclear.py)
- [track15_phase4_12_alt.py](scripts/track15_phase4_12_alt.py)

---

## F82. Phase 1 — proton mass fit trivial for (3, 6)

Two routes to calibrate (3, 6) at m_p = 938.272 MeV:

**Route A (recalibrate L_ring_p only):**
Keep (ε_p, s_p) = (0.55, 0.162).  μ(3, 6) = 7.756 on this
geometry.  Setting L_ring_p = 47.29 fm (= 2.30× Track 12's
20.55 fm) gives (3, 6) exactly at 938.272 MeV.  Signature OK.

**Route B (magic shear for quark base):**
Set s_p = 2 for the (1, 2) quark base to sit at shear
cancellation (μ = 1/ε_p).  Pick ε_p such that quark mass =
m_p/3 = 312.76 MeV, giving (3, 6) = 3 × 312.76 = 938.27 MeV.
Many (ε_p, L_ring_p) pairs work: e.g. (0.33, 55.4), (0.55,
33.3), (1.0, 18.3).

Both routes are viable.  **Mass fitting is not a blocker for
(3, 6).**

## F83. Phase 2 — the composite α rule resolves the α = 9α problem

**The problem:** under model-F's bare α-sum rule
`α_sum = n_et − n_pt + n_νt`, bare (0, 0, 0, 0, 3, 6) gives
α_sum = −3 → α = 9α.  Wrong for proton (needs α = α).

**The fix — composite α rule:**

    α_sum_comp = n_et − n_pt/gcd(|n_pt|, |n_pr|) + n_νt

For gcd > 1 modes, the p-tube contribution is divided by the
gcd, representing "per-strand" charge in a composite.  For
gcd = 1 modes (almost all of model-F's inventory), composite =
bare rule.

Test results:

| Test | Result |
|------|--------|
| Bare (3, 6) proton | α_sum_comp = −1 → **α = α ✓** |
| Proton-gcd-1 inventory modes | Identical to bare rule for 17 of 18 model-E tuples ✓ |
| Σ⁻ at model-E tuple (−1, 2, −2, 2, −2, −2) | disagrees (bare = 1, composite = 4) — but R60-native Σ⁻ tuple has gcd = 1 so still works |
| Nuclear scaling (n_pt = 3A, n_pr = 6A) | α = Z² × α exactly for Z = 1, 2, 6, 26 ✓ |

**The composite rule works.**  Backward-compatible with R60-native
inventory and produces correct Z² α scaling for nuclei.

## F84. Phase 3 — nuclear scaling is RESOLVED (historical dealbreaker lifted)

Using the (3, 6) calibration (Route A: L_ring_p = 47.29 fm) and
the composite α rule, with new nuclear scaling law:

> `n_pt = 3A, n_pr = 6A, n_et = 1 − Z`

Gives α_sum_comp = −Z exactly (α = Z²α for any Z).

**Nuclear mass fits (decorated search, n_er and n_νr ∈ ±3):**

| Nucleus | Model-F (1, 3) Δ | **(3, 6) primary Δ** | **(3, 6) decorated Δ** |
|---------|:-:|:-:|:-:|
| d (²H) | 0.05% | 0.05% | **0.05%** (tied) |
| ⁴He | 0.73% | 0.85% | **0.69%** (**better**) |
| ¹²C | 1.08% | 1.16% | **0.94%** (**better**) |
| ⁵⁶Fe | 1.52% | 1.37% | **1.31%** (**better**) |

**Historical dealbreaker RESOLVED.**  Nuclear scaling under
(3, 6) base is *at least as good* as (1, 3) model-F across
every nucleus tested, and slightly better on the heavier
nuclei.  Model-D's concern about (3, 6) breaking the nuclear
charge formula is addressed by the composite α rule.

## F85. Phase 4 — (1, 2) proton alternative also viable

Bonus check: the simplest ratio-rule-compliant proton is just
(0, 0, 0, 0, 1, 2), same topology as the electron but on the
p-sheet with different geometry.

**Mass:** trivially fits at L_ring_p ≈ 15.76 fm (Route A).  Many
magic-shear configurations also work.

**α:** gcd(1, 2) = 1, so bare α-sum rule gives α_sum = −1 →
α = α directly.  No composite rule needed.

**Nuclear scaling (natural: n_pt = A, n_pr = 2A, n_et = A − Z):**

| Nucleus | Δ primary |
|---------|:-:|
| d | 0.67% |
| ⁴He | 1.31% |
| ¹²C | 1.35% |
| ⁵⁶Fe | 1.59% |

Without decoration optimization, (1, 2) nuclear scaling is
comparable to (1, 3) model-F but slightly worse on d and ⁴He.
Decorated search would likely close the gap but wasn't run.

## F86. Phase 5 — three-way verdict

Comparison across the three proton candidates:

| Criterion | (1, 3) [current] | **(3, 6)** | (1, 2) |
|-----------|:-:|:-:|:-:|
| Spin under ratio rule (7b) | 1/3 ✗ | **1/2 ✓** | 1/2 ✓ |
| Spin under parity rule (R50) | 1/2 ✓ | 1/2 ✓ | 1/2 ✓ |
| Spin under "always 1/2" (7c hypothetical) | 1/2 ✓ | 1/2 ✓ | 1/2 ✓ |
| Proton mass fit on model-F architecture | input | L_ring_p = 47.3 fm | L_ring_p = 15.8 fm |
| α_Coulomb = α | bare rule, gcd=1 | **composite rule, gcd=3** | bare rule, gcd=1 |
| Nuclear Z²α scaling | exact (bare) | exact (composite) | exact (bare) |
| Nuclear mass d | 0.05% | **0.05%** | 0.67% |
| Nuclear mass ⁴He | 0.73% | **0.69%** | 1.31% |
| Nuclear mass ¹²C | 1.08% | **0.94%** | 1.35% |
| Nuclear mass ⁵⁶Fe | 1.52% | **1.31%** | 1.59% |
| SU(6) magnetic moments (R47 T7) | bare μ = 1.000 μ_N (64% low) | **μ_p = 3.000 μ_N (+7.4%)** | no prediction |
| Proton charge radius (R47 T7) | R ≈ 0.19 fm (too small) | **R ≈ 1.09 fm (close to 0.84 obs)** | no prediction |
| Constituent quark mass | not applicable | **m_p/3 = 313 MeV ✓** | not applicable |
| Compatibility with model-F (architecture) | native | **requires composite α rule** | native |
| Compatibility with R60 inventory (16/18 matches) | native | recheck under composite rule | recheck |
| Requires rule outside R60 | parity rule (unproven) | composite α rule (this track) | bare rule only |

## F87. Viability verdict

**All three candidates are mechanically viable on model-F's
architecture.** None is ruled out.  Each has distinct trade-offs:

- **(1, 3) model-F current** — cleanest if parity rule or 7c's
  "always 1/2" is correct.  Fails if ratio rule is correct.
- **(3, 6)** — **best overall fit** if ratio rule is correct.
  Wins on nuclear mass fits, magnetic moments, charge radius,
  quark interpretation.  Requires the composite α rule (new, but
  backward-compatible).
- **(1, 2)** — simplest topology but worse nuclear fits and no
  quark/magnetic-moment improvements.  Viable fallback but not
  obviously better than (1, 3).

**Key architectural findings:**

1. The composite α rule `α_sum = n_et − n_pt/gcd + n_νt` is
   backward-compatible with R60-native inventory (the R60-native
   tuples all have gcd = 1 on the p-sheet).  It adds new behavior
   only for modes where gcd > 1 — i.e., composite/quark-like
   modes.  This is an **architectural extension, not a
   replacement**, of model-F's α rule.
2. Model-D's historical concern about (3, 6) (nuclear charge
   formula breaking) is resolved when the composite α rule is
   applied correctly — Z² α scaling holds exactly.
3. The single-k symmetry (k = 1.1803/(8π)) and σ_ra structural
   cancellation survive unchanged across all three proton
   candidates — those are p-sheet-choice-agnostic.

## F88. Implications for model-F

**If ratio rule is confirmed (derivation 7b):**
- (1, 3) proton invalid; switch to (3, 6) or (1, 2)
- (3, 6) is the recommended replacement (better physics match)
- Model-F update: add composite α rule, swap proton tuple and
  nuclear scaling, re-run inventory (compound modes touching
  p-sheet need re-checking)

**If "always 1/2 for emergent particles" is confirmed (7c):**
- (1, 3) stays as proton
- Model-F unchanged
- Track 15 remains as "we looked at the alternative, it's also
  viable, noting for future reference"

**Regardless of spin rule outcome:**
- (3, 6) is a **fully viable proton candidate** on model-F's
  11D architecture
- The composite α rule is a worthwhile extension to document
  (it's the structurally correct rule for any gcd > 1 composite
  mode that might arise in future work)
- Nuclear scaling works under either base (1, 3 or 3, 6)
- R60's core architectural discoveries (σ_ra, single-k, α-sum)
  are all spin-rule-agnostic and survive any choice

## Decision point

Track 15's job was to answer: "could we adopt (3, 6) if we had
to?"  **Answer: yes, cleanly.**  No catastrophic barriers; the
historical dealbreaker (nuclear scaling under model-D) is
addressable via the composite α rule.

**Recommendation:** keep model-F as-is (with (1, 3) proton) as
the working model.  Hold (3, 6) as a documented alternative.
Wait for derivation 7c's outcome on the spin rule.  If 7c rescues
(1, 3), nothing changes.  If ratio rule wins, Track 15 provides
the migration path.

## Status

Track 15 complete.  Sandboxed investigation done; no changes to
model-F.  Findings captured here for future reference if proton
mode assignment becomes active again.
