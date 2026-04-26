# R64 — Status

Concise snapshot.  Full narrative in
[README.md](README.md); detailed results in `findings-*.md`;
metric reference in [metric-terms.md](metric-terms.md);
particle inventory in [zoo.md](zoo.md).

---

## Where we are

Post-Track 11, R64 has a **complete 11D metric architecture** for
the three forces that MaSt is responsible for, with one gap:

| Force | Scope | Status |
|---|---|:---:|
| Gravity | St + GRID (4D Minkowski, **outside Ma**) | ✓ (out of MaSt scope) |
| Electromagnetism (Coulomb + magnetic) | tube → aleph → t  +  aleph → S | ✓ R59 / R60 / Phase 8 |
| Strong | p_t → S  (σ_pS_tube + H2 at signature edge) | ✓ Phase 11c |
| **Weak** | open — e-sheet → S coupling is the candidate | **✗** |

So MaSt is **2 of 3** on its internal-force responsibility.  Weak
force is the remaining gap.

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

**Force completion (goal 1):**
- ~~**u**~~. Weak force from e-sheet → S coupling. **[TRIED — outcome C]**
  σ_eS_tube + e-H2 activation works architecturally but V(r) is
  not Yukawa-shaped; mass scale comes out at ~500 MeV vs
  W± at 80 GeV.  See [findings-12.md](findings-12.md).  Weak still open.
- **u′** (next). Same template applied to **ν-sheet → S** (different
  geometry; cheapest next attempt).
- **u′′**. σ_eS_ring + companion (different e-sheet entry).
- **t**. Symmetric three-sheet → S activation (test cross-Schur
  paths for qualitatively new shapes).
- **v**. Anomalous magnetic moments from H2 second-order
  leakage (potentially derives g-2 from same architecture).
- **w**. Magnetic-channel preservation under Track 11 (sanity check).

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

**No active blockers.**  The architecture is complete enough to
draft model-G; remaining items are refinements and extensions.

---

## Snapshot

**Architecture date:** 2026-04-25
**Working metric:** R60 model-F + Track 11 σ_pS_tube + H2
**Working point:** R64 Point B `(ε_p, s_p, K_p) = (0.2052, 0.0250, 63.629)`
**Charge attribution:** A1 — `f(n_pt, n_pr) = n_pt/6 + n_pr/4`
**Strong-force calibration:** σ_pS_tube ≈ −0.12505 (signature edge), σ_eff_tube = −116
**Open critical pool item:** **u** (weak force from e-sheet → S)
