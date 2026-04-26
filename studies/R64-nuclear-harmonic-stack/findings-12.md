# R64 Pool item u — Weak force from e-sheet → S coupling

**Status: complete.  Outcome C — V(r) profile not Yukawa.  Simple
e-sheet analog of strong-force activation does NOT deliver weak
force phenomenology.  Weak force is still open.**

---

## Method

Tested whether activating σ_eS_tube + an e-sheet H2 prescription
(`σ_aS = b_e · σ_eS_tube` with `b_e = +√α/k = +1.81892`,
sheet-substituted from Phase 11d's p-sheet derivation) delivers a
weak-force-like Yukawa profile for lepton-lepton systems.

Script:
[`scripts/track12_pool_u_weak_force.py`](scripts/track12_pool_u_weak_force.py) ·
Outputs:
[`outputs/track12_pool_u_weak_e_sheet.csv`](outputs/track12_pool_u_weak_e_sheet.csv) ·
[`outputs/track12_pool_u_weak_potential.png`](outputs/track12_pool_u_weak_potential.png)

The H2 coefficient sign-flips from p-sheet because of sheet sign
conventions: `sign_p = −1` gives `b_p = −1.819`; `sign_e = +1`
gives `b_e = +1.819`.  Magnitude identical.

---

## Results

### F12.1. The e-sheet architecture activates cleanly

Signature edge: **σ_eS_tube = 0.000150** (vs σ_pS_tube = 0.125 for
p-sheet — three orders of magnitude smaller, reflecting the
e-sheet's very different geometry).

| σ_eS_tube | σ_eff_eS_tube | A1 spread |
|:---:|:---:|:---:|
| 0.0 | 0 | 5 × 10⁻⁸ |
| 0.000075 | +61.5 | 2 × 10⁻⁷ |
| 0.000113 | +146 | 5 × 10⁻⁷ |
| 0.000142 (95% edge) | +506 | 2 × 10⁻⁶ |
| 0.000149 (99% edge) | +872 | 4 × 10⁻⁶ |
| 0.000150 (edge) | +1058 | 5 × 10⁻⁶ |

The Schur amplification (σ_eff_eS / σ_eS_tube ≈ 7 × 10⁶ at edge)
is much larger than the p-sheet's (~7 × 10³).  This reflects the
e-sheet's huge `g_er = k·(1+(s·ε)²) ≈ 29744` compared to the
p-sheet's `g_pr ≈ 0.047`.

A1 universality is preserved through the whole band.  Architecture
is structurally consistent.

### F12.2. V(r) for lepton systems does NOT match weak force

Computed V(r) at σ_eff_eS_tube = −506 (95% of edge, attractive
sign) for three two-body lepton compounds:

| Channel | tuple | n_et | r_min (fm) | V_min (MeV) |
|:---|:---|:---:|:---:|:---:|
| ee | (2, 4, 0, 0, 0, 0) | 2 | 0.39 | **+52 (repulsive!)** |
| eμ | (2, 3, −2, −2, 0, 0) | 2 | 0.39 | −68.2 |
| μμ | (2, 2, −4, −4, 0, 0) | 2 | 8.68 | −207 |

Three diagnostic problems:

1. **ee is repulsive at the trough.**  m² goes negative across
   most of the r range (the metric becomes "non-physical" — there's
   no real mass solution).  Only the small-r boundary survives,
   and there V is positive.  This is qualitatively different from
   any QED prediction for ee scattering.
2. **r_min implies a 506 MeV mass scale.**  ℏc / r_min ≈ 197 / 0.39
   ≈ 506 MeV.  This is 160× too small for the W± mass (80,400 MeV)
   and doesn't match any clean SM scale (not muon, not π, not
   constituent quark).
3. **Yukawa fit fails.**  The attractive segment isn't an
   exponential decay — it's a metric-edge artifact bounded by
   the m² → 0 boundary.  No clean `V(r) = −A·exp(−mr)/r` form.

### F12.3. Why p-sheet worked and e-sheet didn't

The asymmetry traces to **m_Ma differences**, not the H2 prescription:

| Quantity | p-sheet (proton system) | e-sheet (electron system) |
|:---|---:|---:|
| m_Ma at ε,s for two-body | ~1880 MeV (≈ 2·M_p) | ~1 MeV (≈ 2·M_e) |
| Cross-term scale at edge | ~−2300 MeV at r=1 fm | ~−400 MeV at r=1 fm |
| Net m² at trough | small positive (~m_Ma² scale) | negative (cross overwhelms m_Ma) |

On the p-sheet, the cross term carves a well *into* a substantial
m_Ma asymptote, giving a clean trough at r ≈ 1 fm.  On the e-sheet,
m_Ma is so small that the cross term **overshoots zero**, making
the metric non-physical in the trough region.  What's left is
edge-bounded shapes that aren't Yukawa.

### F12.4. The implied mass scale (~500 MeV) is suggestive

Although the V(r) doesn't fit Yukawa cleanly, the trough at 0.39 fm
implies a mass scale ~500 MeV.  This isn't W± (80 GeV) but it's
intriguingly close to:

- ρ meson (775 MeV) — but ρ is a multi-sheet compound, not directly
  related to e-sheet → S
- Constituent-quark mass scale (~340 MeV) — wrong sheet
- Some unidentified e-sheet resonance

The ~500 MeV scale is the result of edge methodology applied to
the e-sheet's K_e and signature-edge interplay, not a deliberate
prediction.  But it might correspond to *something*; flagging
without committing.

---

## Verdict

**Outcome C: e-sheet → S activation does not deliver weak force.**

The architectural template `sheet → S + sheet-H2 + edge
methodology` does not generalize from p-sheet to e-sheet to
produce SM-consistent weak phenomenology.

Three diagnoses:

1. **e-sheet geometry is too dilute** for the Phase 7c-style trough
   to land at a Yukawa-shaped potential.  The huge `s·ε ≈ 800`
   makes the e-sheet's m_Ma profile unsuitable for hosting a
   bound-state-like force at 80 GeV scale.
2. **Sign conventions don't help.**  Trying both signs of σ_eS_tube
   gives either repulsion or non-physical m² regions, but never a
   clean Yukawa at the right mass scale.
3. **The weak force may not live in σ_eS_tube specifically.**  Other
   e-sheet entries (σ_eS_ring) or cross-sheet routing (σ_eν via
   aleph) or a different formalism altogether may be needed.

---

## Implications

**The architecture is not invalidated.**  Pool item u tested one
specific hypothesis and ruled it out.  The metric still:
- Holds A1 universality across the inventory (Phase 11a/c) ✓
- Delivers strong force on p-sheet (Phase 11c) ✓
- Closed-form H2 derivation (Phase 11d) ✓
- All R64 single-sheet primitives match α at machine precision ✓

What's ruled out: the *naive symmetric* version of the
hub-and-spoke hypothesis (each sheet → S delivers its own force
via the same H2 template).

**What's still on the table for weak force:**

- **σ_eS_ring + companion**: ring is α-inert on p-sheet (Phase 10a);
  might give different V(r) shape on e-sheet.  Bounded test.
- **Cross-sheet routing through aleph**: weak charged current
  literally connects e ↔ ν, and the hub-and-spoke architecture
  routes cross-sheet through aleph naturally.  Test by activating
  σ_eS_tube simultaneously with σ_νS_tube and looking for joint
  effects in compound modes.
- **ν-sheet → S as the actual weak channel**: ν-sheet has yet
  again different geometry (ε_ν = 2.0, s_ν = 0.022).  Might
  produce a more Yukawa-like profile.  Bounded test (essentially
  re-run pool item u with ν-sheet substitution).
- **Composite-mode resonance**: weak might be a specific compound
  mode at ~80 GeV (W± / Z analogs), not a metric coupling.  This
  is R43's "transient reconfiguration" view.  More involved.
- **Non-metric (propagator)**: Pool item m revival.  Last resort.

---

## Status

**Pool item u: complete (outcome C).**

Recommended next pool items in priority order:

1. **u′ (variation): test σ_νS_tube + ν-sheet H2** — same script,
   sheet-substituted.  Cheapest next attempt.
2. **σ_eS_ring + companion** — different e-sheet entry; a
   one-script variation.
3. **t (symmetric three-sheet activation)** — broader test of
   whether multi-sheet activation produces qualitatively new
   V(r) shapes via cross-Schur paths.
4. **r (edge methodology interpretation)** — if the edge
   methodology is structural for p-sheet but not for e-sheet,
   that's an architectural distinction worth understanding.

Pool item u confirmed: **the architecture has room for sheet → S
activations on each sheet, but only the p-sheet activation
delivers a clean Phase 7c-class trough.  The other sheets behave
differently.**  This is information, not regression.
