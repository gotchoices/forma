# R64 — Status

Concise snapshot.  Full narrative in
[README.md](README.md); detailed results in `findings-*.md`;
metric reference in [metric-terms.md](metric-terms.md);
particle inventory in [zoo.md](zoo.md).

Updated: 2026-04-25 — post comprehensive findings audit + user's
honest reframing of what's accounted for vs open.

---

## Where we are — honest assessment

| Force | Where it lives | What's accounted for | What's open |
|---|---|---|---|
| Gravity | St + GRID | ✓ outside MaSt scope | n/a |
| EM (Coulomb) | tube → aleph → t (R60) | ✓ structural (α exact, universality machine-precision under A1) | none |
| EM (magnetic baseline) | aleph → S (Phase 8) | ✓ structural at α magnitude | magnetic anomaly (g-2) — see "open" below |
| Strong (deuteron only) | (6, 0) Ma compound at Point A | ✓ ~96% — m_Ma deficit gives 2.13 MeV vs observed 2.22 | Last 4% within calibration noise |
| Strong (heavy nuclei) | unknown structural mechanism | ⚠ ~12% — Ma compound gives 1 MeV/n; observed ~8 MeV/n | **88% of binding unaccounted** |
| Weak (Fermi constant) | s_p · α² / m_p² at Point A | ✓ 0.5% dimensional match | Matrix element, parity violation, μ/π decay cross-checks |

**The user's reframing, accurate as stated:**
1. ✓ Weak force has a structural anchor in Ma (G_F dimensional match)
2. ⚠ Strong force is *partially* accounted for in Ma — fully for the
   deuteron via compound-mode mass deficit, but residually for heavier
   nuclei (~88% missing as A grows)
3. ⚠ The residual is *expected* to live in S as spatial-separation
   energy of nucleons (or compound-mode internal structure)
4. ✗ We don't yet know how to *quantify* that S residual structurally
5. ✗ We don't know if a metric off-diagonal is *needed* to produce
   the residual, or if S "handles itself" via mode internal structure
6. ✗ As a consequence, **we cannot yet derive the binding-curve
   structure (the Fe peak, magic numbers, saturation density) from
   MaSt** — those remain in the residual we haven't accounted for

---

## What's structurally established (won't be walked back)

These are the load-bearing structural results that survive the
walk-backs documented in review.md and the post-Track-11 audit:

- **R60 model-F architecture** (R59 F59 / R60 baseline)
  - Coulomb α via tube → aleph → t
  - σ_ta = √α, σ_at = 4πα, σ_ra = (s·ε)·σ_ta
  - Single-k symmetry across sheets (k = 1.1803/(8π) empirical)
- **Phase 8 magnetic activation at α magnitude** (R64)
- **A1 charge attribution** `f(n_pt, n_pr) = n_pt/6 + n_pr/4`
  (Phase 11a) — derives from u = (1, +2) → +2/3 and d = (1, −2) →
  −1/3
- **n_pr/4 = T_z** mapping (Phase 11a, Track 15) — exact
  isospin-third-component encoding
- **H2 closed form** `b = −√α/k_p` (Phase 11d) — first-order
  perturbation derivation, matches Phase 9b numerical to 6 sig figs
- **R64 u/d quark composition**: u = (1, +2), d = (1, −2) on
  p-sheet; proton = (3, +2), neutron = (3, −2)
- **Two viable working points**: Point A (nucleon properties +
  G_F) and Point B (nuclear chain Ca→Sn).  Neither satisfies both.
- **G_F = s_p · α² / m_p²** dimensional match (0.5% at Point A).
  The match itself is robust; full derivation pending.
- **Ma compound deuteron**: m_Ma(6, 0) at Point A = 1875.71 MeV vs
  observed 1875.61 MeV (4% match on binding, 0.005% on mass).
  No "force" needed for the deuteron.

---

## What's hypothesized (suggestive but not derived)

- The energy-budget framework: B_obs = −Δ_Ma + (energy in S).
  This is sound as **accounting** but not as **derivation**.
- The "S residual" represents spatial-separation energy.
- Track 15's SEMF-residual fit suggests the missing volume term
  has the right mathematical form (volume + surface + Coulomb +
  asymmetry) at literature-coefficient scale (within 15-20%) —
  indicating the binding-curve shape is consistent with standard
  nuclear physics, but not deriving the mechanism.
- Pool z step 2 (cross-sheet matrix element) would convert the
  G_F dimensional match into a structural derivation.

---

## What's been ruled out

- **Track 11's "strong force in metric" claim** at the singular
  edge: σ_pS_tube + H2 V(r) at σ_eff = −116 fails the QM gate
  (Track 13b: 3 bound pn states, bound nn/pp).
- **σ_pS_tube + H2 V(r) at moderate magnitudes**: produces no
  attractive trough at all (Track 17).  Kinetic-style term
  dominates; cross term too weak to compete.  **σ_pS_tube
  cannot be the volume-binding mechanism in any honest regime.**
- **The 2^(1/4) "structural form" for k_p**: a 0.75% match isn't
  a derivation; the supported form is the empirical k_p value.
- **The "edge methodology" as structural feature**: likely
  regulator artifact, per Concern 6 from review.md.
- **R29's compound-mode formula via direct substitution**: same
  ~88% gap for heavy nuclei as R64's u/d composition.
- **Pure pair-counting σ_pS_ring channel for strong force**:
  Phase 10a found α-inert and channel-asymmetric; can't deliver
  charge-symmetric force.

---

## What's left to close all forces

### A. Strong force (volume binding for A ≥ 3)

The 88% missing piece is the highest-priority architectural gap.
Three exclusive paths:

1. **Pool item m revival (Yukawa propagator with geometric reading)**.
   Replace particle-exchange interpretation with "exponential
   cutoff from compactification scale."  The form V(r) = −A·e^(−mr)/r
   would naturally give 1 deuteron bound state and unbound nn/pp.
   *Substantial new formalism; multi-day scope.*
2. **Compound-mode internal structure**.  Heavy nuclei may not be
   simple (3·A, n_pr) compounds — maybe sub-modes or harmonic
   stack contributions add to m_Ma in a non-linear way that
   captures saturation.  *Investigate via more careful mass
   formula at R64's tuples.*
3. **Standard nuclear physics overlay**.  Accept that V(r) is
   imported from data (Argonne v18 or chiral EFT); MaSt provides
   substrate (modes, masses, EM, weak); nuclear physics handles
   binding.  *Pragmatic; intellectually unsatisfying; minimal
   work to integrate.*

### B. Spatial-structure quantification (the user's open question)

Even with one of (A.1, A.2, A.3) chosen, we need to:
- Predict deuteron rms charge radius (~2 fm) from MaSt
- Predict ⁴He, ¹⁶O, ⁵⁶Fe charge radii
- Determine whether spatial extent of compound modes carries
  energy distinctly from the m_Ma value
- Address α scaling vs full strength of any S-coupling
  introduced (architectural inconsistency between EM α-scaling
  and Track 11's full-strength σ_pS)

### C. Weak force (full closure)

- **Pool item z step 2**: derive τ_n from cross-sheet matrix
  elements (σ_eS + σ_νS + aleph mediation).  Converts G_F
  dimensional match into structural derivation.
- **Cross-checks**: μ decay, π decay using same s_p · α² / m_p²
  structure.  G_F is universal in SM; if MaSt's structural
  account is right, all weak processes predict from one
  relationship.
- **Parity violation (V−A)**: separate structural account.  May
  come from sheet-sign conventions or ring-orientation
  asymmetry.  Not addressed by G_F.

### D. Magnetic anomaly (g-2)

- **Pool item v properly executed**: the opening scan (Track 16)
  showed σ activation does shift magnetic-sector G⁻¹ entries,
  but the proxy was too crude for anomaly extraction.  A
  proper magnetic-α formula (Schur reduction analogous to
  α-Coulomb) plus second-order perturbation analysis is needed.

### E. Metric architecture polish

- **Pool item s (Clifford embedding)**: derive (ε,s) curves
  analytically; could reduce free parameter count from 11 to ~5.
- **Pool item p (meson α-attribution)**: generalize A1 to
  multi-sheet compounds.
- **Pool item q (L_ring recalibration)**: fix Phase 11f mass-
  prediction methodology issue.
- **Pool item k (strange family on different generation)**: R64
  Track 4's open issue.
- **Pool item o (Z₃ and AM at R64 Point B)**: structural check
  owed before model-G integration.

---

## Working points (calibration status)

| Point | (ε_p, s_p, K_p) | Calibrated to | Matches | Doesn't match |
|---|---|---|---|---|
| A (Track 1) | (0.073, 0.194, 22.85) | m_u, Δm(n−p), B(²H) | nucleons, deuteron, **G_F** | nuclear chain (~12% Ma binding for heavies) |
| B (Track 3) | (0.205, 0.025, 63.63) | nuclear chain Ca→Sn | heavy-nuclei binding (1-2%) | deuteron (8× over-bound), G_F (8× off) |

**No single working point currently satisfies both ends of the
binding chain** while also matching G_F.  A unified working point
is one of the open architectural questions (pool item l revival,
or alternative mass-formula derivations).

---

## Variable count

11 free parameters + α as input.  Of the 11:
- 6 with active range (sheet geometries on three Clifford-style
  embeddings) — could compress to ~3 effective DOFs via Clifford
  embedding constraints (pool item s)
- 4 are determined points (anchor calibrations)
- 1 conjecturally edge-pinned (σ_pS_tube; status reduced after
  Tracks 13b/17 ruled it out as strong-force mechanism)

Realistic intermediate target: 3–5 free + α via:
- Clifford embedding (pool s): 6 → 3 effective
- Edge-methodology resolution (pool r): possibly 1 fewer
- Sheet-derivation tracks (pools k, e): collapse anchors

The "1 free var + α" goal requires deriving each sheet from
generation structure — major program, deferred to model-G follow-on.

---

## Snapshot

**Architecture date:** 2026-04-25
**Inherited base:** R60 model-F (R59 F59 architecture)
**Charge attribution:** A1 — `f(n_pt, n_pr) = n_pt/6 + n_pr/4`
**Quark composition:** u = (1, +2), d = (1, −2) on p-sheet
**Working points:** A (nucleon-anchored) and B (nuclear-chain-anchored), no unified point yet
**Strong-force mechanism:** **OPEN** — σ_pS_tube ruled out; pool item m or compound-mode reframing pending
**Weak-force mechanism:** **PARTIAL** — G_F dimensional match (0.5%); matrix-element derivation pending
**Open critical question:** how to derive heavy-nuclei volume binding (the 7-8 MeV/n missing per nucleon) from MaSt structure — or accept that it lives outside MaSt's scope.

**Model-G drafting prerequisite:** resolution of strong-force
mechanism (path A above) AND honest accounting of what MaSt
delivers vs what's deferred to nuclear-physics overlay.
