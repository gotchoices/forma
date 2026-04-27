# R64 — Status

Concise snapshot.  Full narrative in
[README.md](README.md); detailed results in `findings-*.md`;
metric reference in [metric-terms.md](metric-terms.md);
particle inventory in [zoo.md](zoo.md).

---

## Where we are

Post-Track 11 + Pool item z (step 1), with [review.md](review.md)
critical-review walk-backs applied:

| Force | Scope | Status |
|---|---|:---:|
| Gravity | St + GRID (4D Minkowski, **outside Ma**) | ✓ (out of MaSt scope) |
| Electromagnetism (Coulomb + magnetic) | tube → aleph → t  +  aleph → S | ✓ R59 / R60 / Phase 8 |
| Strong (static potential trough) | p_t → S  (σ_pS_tube + H2 at signature edge) | **✗ — V(r) reproducible from metric, but QM gate FAILS** at both Point A and Point B (3 bound pn states vs 1; bound nn/pp; B(²H) 6.6× too deep at Point A, 13× at Point B; see [findings-13b.md](findings-13b.md)) |
| Weak (Fermi constant, scaling) | `G_F ≈ s_p · α² / m_p²`  (Point A) | ⚠ **0.5% numerical match; matrix-element derivation pending** |

**Important caveats** (from critical review, ack. April 2026):
- Track 11's "strong force in the metric" claim outpaces what was
  demonstrated.  Phase 11c reproduced Phase 7c's static V(r), but
  Phase 7d had already shown that V(r) fails the QM gate (3 bound
  pn states vs 1 deuteron observed; nn/pp bound vs unbound; B(²H)
  ≈ 30 MeV vs 2.22 MeV observed).  Track 11 didn't re-apply the
  QM gate; until it does, the strong-force claim must be hedged
  to "static-potential trough is metric-derivable."
- The "edge methodology" (σ_eff diverging at signature boundary)
  is a textbook singular limit; physical observables there are
  regulator-dependent, not structural.  Pool item r is needed to
  decide whether this is a real architectural feature or
  artefact.
- Phase 11e's "stable around Point B" claim is incompatible with
  the actual V_min(pn) spread (~470 MeV across 12% ε_p variation).
  Point B is fine-tuned, not robust.
- Pool item z step 1's G_F match is **independent of these
  concerns** — it's a dimensional relationship between calibrated
  parameters that doesn't depend on V(r) shape, edge methodology,
  or the QM gate.  This finding survives intact.

---

## What we've done

**Architecture (Track 11):**
- A1 charge attribution `f(n_pt, n_pr) = n_pt/6 + n_pr/4`
  resolves the factor-of-9 anomaly at the R64 proton (Phase 11a).
- Strong force lives in σ_pS_tube + H2 at the signature edge,
  reproducing Phase 7c's V(r) profile exactly: pp/nn at −32 MeV,
  pn at −50 MeV at r ≈ 1.135 fm (Phase 11c).
- H2 closed form: `σ_aS = −8π·√α·2^(−1/4) · σ_pS_tube` (Phase 11d).
- Point B `(ε_p, s_p, K_p) = (0.2052, 0.0250, 63.629)` confirmed
  stable under the new architecture (Phase 11e).
- A1 validates at machine precision on all R64 single-sheet
  primitives (Phase 11f).

**Inventory:**
- 22 of 24 particles within 2% mass match (zoo.md).
- Strong-force phenomenology charge-symmetric (V_min(pp) ≈ V_min(nn)).

**Variable count:**
- 11 free + α today.  6 with active range (sheet geometries on
  three Clifford-style embeddings); 4 calibration anchors;
  1 conjecturally edge-pinned.
- Realistic intermediate target: 3 free + α via Clifford
  embedding analysis + edge-methodology interpretation.

---

## What we have yet to do

All open work lives in the [README.md](README.md) track pool as
letter-keyed items; pull in any order.  Current priorities (per
recent discussion):

**Force completion (goal 1) — major progress:**
- **z step 1**. **[DONE — G_F = s_p·α²/m_p² matches PDG to 0.5%
  at Point A]**.  See [findings-13.md](findings-13.md).  The
  weak coupling emerges from the same structural ingredients
  that calibrate nucleon properties.
- **z step 2** (next). Full cross-sheet matrix-element
  derivation of τ_n from σ_eS + σ_νS + aleph mediations.
  Converts numerical match into structural derivation.
- ~~**u**~~. e-sheet → S Yukawa test. **[TRIED — outcome C]**.
  Reinterpreted: pool u activation is not "the weak force" —
  it's the cross-sheet matrix-element infrastructure that
  step z2 will compute through.
- **v**. Anomalous magnetic moments from H2 second-order
  leakage (potentially derives g-2 from same architecture).
- **t**. Symmetric three-sheet activation (cross-Schur paths).
- **w**. Magnetic-channel preservation under Track 11.
- **u′ / u′′**. ν-sheet variant, σ_eS_ring variant — now lower
  priority (z reframed weak as not requiring sheet-S Yukawa).

**Metric principle / accuracy (goal 2):**
- **r**. Edge-methodology physical interpretation.
- **s**. Clifford embedding analysis per sheet (collapses 6 sheet
  params to 3 effective DOFs).
- **p**. Meson α-attribution extension (multi-sheet A1).
- **x**. A1 closed-form derivation from first principles.
- **y**. R60 k recalibration to structural 2^(1/4)/(8π).
- **10f**. Ring-aleph parallel channel.

**Model-G integration (goal 3):**
- **q**. R64 L_ring recalibration.
- **k**. Strange family on a different generation.
- **o**. Z₃ and unit-per-sheet AM cross-check.
- **i**. Synthesis & promotion to model-G.

**Particle-physics extensions (follow-on):**
- **a, b, c, e, f, n** — light-A binding, quantum numbers,
  electron shells, c/b/t quarks, full inventory, nuclear
  reactions.

**Goal 4 (derive every metric term from first principles)** is
deferred to a separate study after model-G stabilizes.

**Outstanding gates before model-G can be drafted:**
- ~~Concern 1: re-apply Phase 7d Schrödinger gate to Phase 11c's
  V(r).~~  **[Track 13b complete — FAIL at both Point A and Point B.
  See [findings-13b.md](findings-13b.md).  Strong-force-in-metric
  claim formally walked back.]**
- Concern 6: edge methodology — physical observable or regulator
  artifact?  Track 13b strongly suggests artifact.
- Concern 4: re-do Phase 11f mass inventory using `K_p · μ`
  (R64 convention) instead of model-F L_ring.
- Pool item m revived: Yukawa long-range extension — propagator-
  based path.  Now back on the critical path since the metric-V(r)
  route failed the QM gate.
- Alternative: revisit R29's compound-mode framework — maybe the
  deuteron *is* a (6, 0) Ma mode and "strong force as V(r) bound
  state" was a category error.

Model-G draft cannot begin until the strong-force question is
re-resolved (currently: open, with metric-V(r) route eliminated).

---

## Snapshot

**Architecture date:** 2026-04-25
**Working metric:** R60 model-F + Track 11 σ_pS_tube + H2
**Working point:** R64 Point B `(ε_p, s_p, K_p) = (0.2052, 0.0250, 63.629)`
**Charge attribution:** A1 — `f(n_pt, n_pr) = n_pt/6 + n_pr/4`
**Strong-force calibration:** σ_pS_tube ≈ −0.12505 (signature edge), σ_eff_tube = −116
**Open critical pool item:** **u** (weak force from e-sheet → S)
