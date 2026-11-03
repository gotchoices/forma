# Lepton manifold: can the leptons share one set of dimensions?

Working file for [STATUS.md §1](../STATUS.md). Two hypotheses, tested against ma-domain's K4 candidate ([cand-QY-ED.md](../../ma-domain/work/cand-QY-ED.md)): its electron delta is e = (m₁, m₂), μ = (m₁, m₃), τ = (m₂, m₃), with m₂ ≈ 0.007 fm, m₃ ≈ 1 fm, and m₁ unconstrained above about 4,500 fm.

## 1a. Four dimensions: delta corners + a neutrino line

Neutrino segments pair a separate neutrino line with one delta dimension each; junction reflections come from ribbon width ∝ dimension size.

- **Arithmetic:** the neutrino fits need two strong width steps (ratios of tens to hundreds) and one of about 2 ([junction-fit.md](junction-fit.md), Test 3). The delta offers only m₃/m₂ ≈ 136, m₁/m₃ ≥ 4,500, m₁/m₂ ≥ 6×10⁵, or 1 (two segments on the same dimension). Nothing near 2.
- **Direct test** ([k4_widths.py](../scripts/k4_widths.py), one K4 assignment): no combination fits; best mixing errors about 0.1.
- **Status: not yet**, for plain width steps. Open only with a richer junction (tapered crimps) or a different width-to-size mapping.

## 1b. Three dimensions: the neutrino as a single-axis mode

No separate line. The neutrino circulates in only one delta dimension, which gives mass without charge ([metric-charge ch. 2 §4.2](../../metric-charge/02-modes-on-a-sheet.md)). Only m₁ can be large enough for the meV scale.

**A condition from shear.** In ma-domain's sheet mass formula, m = C·√((m_t/L_T)² + (δ/L_R)²) with δ = m_r − σ·m_t, every lepton sheet has σ ≈ 2:
- a mode circulating only the *unsheared* direction (m_t = 0) has m = C·n/L_R, which is light if that dimension is large;
- a mode circulating only the *sheared* direction (m_r = 0) has δ = −σn, so it carries forced momentum around the other, fm-scale dimension and is very heavy.

So 1b needs m₁ to be the unsheared direction of a lepton sheet. Among K4's four fitted assignments, only one has that (m₁ unsheared on the e sheet).

**Run:** ma-domain's candidate solver with m₁ pinned at 4.24×10¹⁰ fm, the size that gives one circulation ≈ 29 meV. This used a new `--pin` option; report: [cand_QY-ED-share3_pin-m1-nu.txt](../../ma-domain/outputs/cand_QY-ED-share3_pin-m1-nu.txt).

**Results:**
- K4 still fits all nine quark and charged-lepton masses exactly, in 4 discrete assignments.
- **In all 4, m₁ is the sheared direction of both the e and μ sheets.** The assignment with m₁ unsheared stops fitting at this size.
- A mode circulating only around m₁ is therefore heavy (≈ 2n·C/L(m₂) ≈ 300 GeV·n), not a neutrino.
- Pinning m₁ does not remove K4's free parameter. The remaining freedom is in m₃, m₄, and the quark shears; m₁ was unconstrained only because the masses are insensitive to it once it is large.

**Status: not yet**, in K4 with ma-domain's sheared mass formula. The obstruction is specific: at the neutrino scale, m₁ is always a sheared direction of the e and μ sheets.

## A spectrum-based search (leptons only, no assigned modes)

> **Formula correction (2026-11-02).** The first runs below applied every sheet's shear to every mode (a product-space reading). The search treats modes as living on single sheets, so it now matches ma-domain's solver: a sheet mode feels only its own sheet's shear, and a single-axis mode feels the shear of every sheet whose tube is its dimension. The N = 3 and N = 4 runs were repeated with the corrected formula and **the conclusions stand**: no fit at N = 3 (strict, loss ≈ 268; loose, ≈ 84) or N = 4 (loose, ≈ 34). As before, the neutral side fits easily, at N = 4 landing on the massless-ν₁ pattern (≈ 0.1, 8.7, 50.1 meV), while the charged leptons cannot be placed. Numbers quoted below are from the first runs; the reasons given are unchanged.

[../scripts/lepton_search.py](../scripts/lepton_search.py) searches flat 3-dimensional tori (sizes plus shears on any subset of dimension pairs, with each sheet's orientation and the closure rule in both its as-written and symmetrized forms). It requires that the **three lightest charged states are e, μ, τ** and the **three lightest neutral states match the neutrino splittings**, with no particle assigned to a mode by hand. Harmonics (non-primitive circulations) are not counted as new particles. Output: [../outputs/lepton_search_N3.txt](../outputs/lepton_search_N3.txt).

**Result: no 3-dimensional topology fits.**
- The neutral side fits easily. The best runs give 7.4, 11.7, 50 meV, close to the light-ν₁ family.
- The charged side fails, with the lightest charged states at tens of MeV in degenerate pairs and evenly spaced ladders.
- **Why:** every charged sheet carries a tower of charged states (1, n), spaced by about C/(ring size). Keeping all of them above the τ needs every charged sheet's ring under about 0.7 fm. On three dimensions joined as a triangle of sheets, each dimension is one sheet's tube and another's ring, so the rings cannot all be small while the electron's tube is about 2,400 fm. A neutrino-scale dimension (about 10¹² fm) used as any sheet's ring would add charged states at meV spacing.

**Loose rule (also run).** The electron must be the lightest charged state and the neutrinos the three lightest neutral states, both required by stability; μ and τ need only match some charged mode, with extra charged states allowed and listed ([../outputs/lepton_search_N3_loose.txt](../outputs/lepton_search_N3_loose.txt)). **Still no fit** (best loss 88: electron at 0.8 keV with a ladder above it; neutrinos near 300 eV). The reason:
- a dimension large enough for meV neutrinos, on any charge-capable sheet (as tube or ring), produces charged states lighter than the electron;
- isolated, it gives only a 1 : 2 : 3 neutral ladder, which cannot reach the ratio 33.6.

*Loophole for N ≥ 4:* a sheet with the large dimension as its tube, a small ring, and shear σ ≈ ½ has only heavy charged modes and exactly one light neutral mode, (2, 1), at 2C/L_tube. Three such sheets could supply three tunable neutrino masses.

**N = 4, loose rule** ([../outputs/lepton_search_N4_loose.txt](../outputs/lepton_search_N4_loose.txt)): **no fit** (best loss ≈ 13). The neutral side again fits easily and lands, unprompted, on the massless-ν₁ family (≈ 0.03, 8.68, 50.1 meV). The charged side fails (electron ≈ 7 MeV, with towers).

*What the charged side needs:* three tube dimensions (≈ 2,400, 12, 0.7 fm) sharing **one tiny ring dimension** (< 0.7 fm), an electron *wye* (ma-domain's EY layout). This keeps every charged sibling above the τ even under the strict rule, but uses all four dimensions. The neutrinos then need at least one more, large dimension kept off the charged sheets, so the minimal lepton torus has **five or more dimensions**.

*A rule that decides the neutral side: are harmonics new particles?* The search excludes non-primitive circulations (a mode going twice around counts as the same particle).
- Excluded: each large dimension gives exactly one light neutral state, so three large dimensions fit any neutrino masses, trivially (about 7 dimensions, no prediction).
- Included: each gives a 1 : 2 : 3 ladder, which constrains the spectrum and matches the earlier ring hosts, where ν₃ was the n = 2 mode.

**Identification rules adopted (user decision).** Start loose and tighten later. Harmonics are *multiple particles in one place*, not new particles, so non-primitive circulations are excluded. Heavier extra charged modes are tolerated; a charged mode *below* a target particle is a problem (absolute for the electron), though shear or tube twist may remove it.

Consequences:
- In a pure torus each large dimension then yields exactly one light neutrino, so three neutrinos need about three extra dimensions (≈ 7 in all) and fit trivially, without prediction.
- Identifying ν₃ as the n = 2 harmonic of ν₁ (Family A, 1D ring) counts as two ν₁ quanta, not a third neutrino. The neutrino circle with junctions avoids this, because its modes are not harmonics of one another.

## Charged wye + neutrino circle: widths from the charged-lepton masses

The economical combination is the charged **wye** (three tubes, one shared tiny ring: 4 dimensions) plus **one neutrino circle** (host G): about 5 dimensions. At resonance each charged lepton's tube size is L = C/m (2,426 fm for e, 11.73 fm for μ, 0.698 fm for τ). Taking each neutrino segment's width proportional to its lepton's tube size fixes all three junction reflections **from the charged-lepton masses alone**. Only the two segment lengths are fitted, against four independent data numbers.

| Segment order | Flips | Loss | Masses (meV) | ν_e row (ν₁, ν₂, ν₃) | \|U_μ3\|², \|U_τ3\|² |
|---|---|---|---|---|---|
| e, τ, μ | off | 8.5×10⁻⁴ | 27.9, 29.2, 57.5 (Σ 115) | 0.688, 0.310, **0.001** | 0.500, 0.498 |
| e, μ, τ | off | 9.0×10⁻⁴ | 27.8, 29.1, 57.5 (Σ 114) | 0.688, 0.311, **0.001** | 0.498, 0.501 |
| either | on | ≈ 0.73 | — | — | — |
| *measured* | | | | *0.678, 0.300, 0.022* | *0.489, 0.489* |

**Reading:**
- The mass ratio comes out exact, and the ν_e row and ν₃ column come out within about 0.01.
- The one real miss is **θ₁₃**: the model's ν_e contains 0.1% ν₃ (θ₁₃ ≈ 2°) against the measured 2.2% (8.5°), which is measured precisely. The result is close to tribimaximal mixing.
- Two lengths against four numbers makes this a near-prediction, not a fit.
- **Genericity check** ([../scripts/wye_generic_check.py](../scripts/wye_generic_check.py), [output](../outputs/wye_generic_check.txt)): 20 random width sets spanning the same range, fitted the same way. Three did as well or better (6.6–8.3×10⁻⁴), three more came within about 3×, and the rest were worse (4×10⁻³ to 0.24). The good sets share a strong **hierarchy**: one very wide segment, one very narrow, and a middle ratio of roughly 15–40, such as (1913 : 1 : 21) or (820 : 1 : 37), alongside the lepton masses' (3477 : 1 : 17). **So the near-fit is not specific to the lepton masses.** They fall in a favorable region that covers roughly 15–30% of random hierarchical width sets: a pass, not a striking coincidence.
- **Assumptions:** width ∝ tube size; each segment shares its lepton's *tube* dimension; flavor couples at a point (the junction); flips off. ν₃/ν₁ ≈ 2.06 here, although the modes are not harmonics.

### Lifting θ₁₃: segments sharing the wye's ring

[../scripts/wye_theta13.py](../scripts/wye_theta13.py), [output](../outputs/wye_theta13.txt). Each segment shares either its lepton's tube (width C/m) or the wye's shared tiny ring (width r, the wye's own unconstrained size, r ≤ 0.7 fm). All 8 tube/ring choices × 2 segment orders × 2 flavor definitions were tried; the fitted parameters are the 2 segment lengths, plus r when used.

**Best case:** point flavor, order e–τ–μ, the **electron's segment shares the ring** (τ, μ share tubes), with **r = 0.47 fm** (interior). Loss 4.8×10⁻⁵ with 3 parameters against 4 data numbers.

| | ν_e row (ν₁, ν₂, ν₃) | \|U_μ3\|², \|U_τ3\|² | θ₁₃ |
|---|---|---|---|
| model | 0.679, 0.302, 0.019 | 0.494, 0.486 | ≈ 7.9° |
| measured | 0.678, 0.300, 0.022 | 0.489, 0.489 | 8.5° |

Mass ratio exact; masses ≈ 28.0, 29.3, 57.6 meV. If this holds, the neutrino data **pin the wye's ring at ≈ 0.47 fm**, a charged-lepton dimension the charged-lepton fit leaves free.

**Cautions:**
- It is the best of 32 discrete combinations (look-elsewhere effect).
- It depends on the flavor definition: with segment-concentrated flavors the same layout gives θ₁₃ ≈ 0 (loss 9×10⁻⁴). Earlier results held under both definitions; this one does not.
- It treats the electron's segment differently from μ's and τ's (ring vs. tube) without a structural reason, contrary to the preference for treating the three sheets alike.

**Look-elsewhere check: not significant** ([../scripts/wye_lookelsewhere.py](../scripts/wye_lookelsewhere.py); outputs `wye_le_real.txt`, `wye_le_s1–4.txt`). The same search (8 sharing choices × 2 orders, free ring size bounded by the smallest tube) was repeated with random hierarchical tube sizes spanning the same range. **5 of 12 random trials beat the real-mass result** (best losses 5×10⁻⁸ to 2.2×10⁻⁵ against 4.8×10⁻⁵), even with weaker search settings, under which the real masses reached only 8.5×10⁻⁴. With one free ring size the model fits nearly any strong hierarchy, so the θ₁₃ ≈ 7.9° fit and the "pinned" r ≈ 0.47 fm carry **no evidence** for a link to the charged-lepton masses.

## (1, 2) electrons and (2, 1) neutrinos on different twists

**Question (user).** Can sheets that share a large and a small dimension give charged (1, 2) electrons and, through a Klein seam, (2, 1) neutrinos?

**On one sheet, no:**
- A Klein seam mirrors one direction, which turns every mode circulating in it into a standing wave. That neutralizes (1, 2) and (2, 1) alike, the electron included.
- One sheet has one shift twist, and only one of (1, 2) (σ_eff = 2) or (2, 1) (σ_eff = ½) can be at resonance.
- If one sheet held both a meV mode ν and the electron e, the combinations e ± ν would also be modes within meV of the electron. For e = (1, 2), ν = (2, 1), the mode e − ν = (1, −1) is charged. *Provisional reading:* a charged state that close to the electron would act as a second electron species, which atomic structure (exactly two electron states per orbital) appears to rule out. Keep this open: such a partner might not behave as an independent electron state.

**On different sheets, yes.** Electron sheets with a common shift (σ_e = 2) put the charged (1, 2) mode at resonance. Neutrino sheets with a common **half twist** (σ_ν = ½ + ε) on one large tube B put the (2, 1) mode near resonance, and it is neutral under the closure rule as written (2 does not divide 1). This *relies on the asymmetric closure rule*; with a symmetric rule (2, 1) would be charged.

**Test** ([../scripts/halftwist_check.py](../scripts/halftwist_check.py)): five dimensions, the charged wye (tubes C/m_e, C/m_μ, C/m_τ on a shared ring r) plus one large tube B carrying three half-twisted neutrino sheets.
- Each neutrino mass is m² = (2C/B)² + (2εC/ring)². The splittings are fixed by the rings, so the ratio 33.6 pins r.
- Using the three lepton tubes as rings predicts a splitting ratio of (m_τ² − m_e²)/(m_μ² − m_e²) ≈ 283 (fails), and a neutrino sheet ringed by the electron tube carries a charged state at m_e/2, below the electron (fails).
- **Rings (T_μ, T_τ, r) work:** **r ≈ 0.12 fm** (second solution 3.83 fm); neutrinos 20, 21.8, 54.1 meV for a chosen lightest mass of 20 meV; both splittings exact; the electron is the lightest charged state.
- **Cost:** extra charged states at half-integer multiples of the μ and τ masses, from the half-twisted sheets' (1, n) modes: m_μ/2 ≈ 52.8 MeV (below the muon), 3m_μ/2 ≈ 158.5 MeV, …, and m_τ/2 ≈ 888 MeV. Taken literally, a 53 MeV charged particle would have been observed. Whether these modes are free particles is open.

## The quark hub as the flavor coupler (star instead of ring)

**Idea (user).** The manifold is a collection of n-dimensional sub-manifolds, not only 2D sheets; ma-domain's K5 already frames it this way, as one 5-torus with modes on any subset of dimensions ([k5-manifold.md](../../ma-domain/work/k5-manifold.md)). Could the small dimension at the center of the quark wye, the hub (≈ 180–490 fm), take part in neutrino oscillation?

**How it could.** A neutrino cannot circulate around the hub (that costs about 2.5 MeV or more), but each flavor channel can couple *through* it, as a brief virtual excursion. That couples every channel to every other: a **star** pattern, in place of the ring of junctions in the circle model. The coupling strength is set by the hub's size and mode overlaps rather than by fit, and the structure resembles the seesaw mechanism (light scale ≈ coupling²/heavy scale).

**Test** ([../scripts/hub_coupling.py](../scripts/hub_coupling.py)). Light mass² matrix M² = diag(a_e, a_μ, a_τ) + hub term, with flavor = channel (e row fixed; μ and τ may swap). Real matrix, so the mixing is CP-conserving.

| Hub term | Parameters vs. data | Result |
|---|---|---|
| common coupling, c·J (all-to-all, equal) | 4 vs 5 | **fails** (loss ≈ 0.18): sin²θ₁₃ ≈ 0.32 vs 0.022 |
| one coupling per channel, g gᵀ | 6 vs 5 | exact (under-determined); couplings e : μ : τ ≈ 0.19 : −1 : +0.83; masses 14.3, 16.7, 52.1 meV |

**Why the common coupling fails.** An equal all-to-all term pushes the equal-weight combination *away* from the others, making it the outlying state ν₃ with about ⅓ in every flavor, hence a large θ₁₃. A trimaximal (TM2) pattern would need the equal-weight state to be ν₂, inside the close pair, which a uniform hub term cannot arrange.

**What the unequal fit suggests.** The electron channel couples weakly to the hub, while μ and τ couple strongly with **opposite signs**, the structure associated with near-maximal μ–τ mixing. If something geometric gave the μ and τ spokes opposite orientations relative to the hub, the pattern would have a reason. That is speculative, and with 6 parameters against 5 numbers the fit itself proves nothing.

## Neutrino circle around the electron triangle

**Idea (user).** Each neutrino segment *is* one electron sheet and each junction is the spoke two neighboring sheets share, so the circle traces K4's electron triangle. Junction types then follow from the spokes' tube/ring roles.

**Bookkeeping** ([../scripts/triangle_circle.py](../scripts/triangle_circle.py), [output](../outputs/triangle_circle.txt)). In all five of K4's distinct fitted assignments:
- the electron triangle has exactly **one tube–tube spoke, one ring–ring spoke, and one mixed spoke**;
- the hub is the **ring of the u/d quark sheet** and the tube of the other two.

Both asymmetries are built in.

**Test.** Junction reflections come from rules fixed in advance, r = (w_A − w_B)/(w_A + w_B), with each sheet's w taken as its non-shared dimension ("other"), its tube ("tube"), or its ring ("ring"). Fitted: two segment lengths, m₁ within K4's range, m₃ within 0.91–1.05 fm. Five assignments × three rules × flips off/on, point flavors.

**Result: no rule fits.** The best (ring rule, flips off) has loss 0.099: mass ratio right (33.65), mixing wrong by 0.2–0.5. **Why:** K4's spoke sizes differ by enormous factors (0.007 fm, ≈ 1 fm, ≥ 4,500 fm), so any size-ratio rule yields junctions that are either near-total mirrors or fully transparent, never the moderate strengths the fits need. Same obstruction as the K4 width test. **Status: not yet** for size-ratio junction rules. The triangle mapping itself is not refuted; a junction rule that does not depend on raw size ratios (role-based strengths, tapers, curvature) remains open.

## Glued sheets vs. one torus: K5 read as a single 5-torus

[../scripts/k5_census.py](../scripts/k5_census.py), [output](../outputs/k5_census.txt). ma-domain's K5 (K4 plus a neutrino dimension) is fitted with ma-domain's per-sheet formula, in which each sheet's shear acts only on that sheet's modes. Read instead as **one 5-torus**, a lap of a dimension that is the tube of several sheets shifts *all* of those sheets' rings at once. In K5, d₄ is the tube of the e, μ, and u/d sheets.

**Census** (every primitive circulation vector with |nᵢ| ≤ 3; ranged sizes at representative values; shears rounded, so individual per-sheet masses are not accurate, but the conclusions depend only on the shears being ≈ 2):
- **The electron's mode** (once around d₄, twice around d₁) is forced to carry momentum around d₂ (0.007 fm) and lands near **1 TeV** rather than 0.511 MeV.
- **The muon's mode** is dragged likewise and lands near **2.5 GeV**.
- **The lightest states** in the single-torus reading circulate in **three or more dimensions** (≈ 12, 25, 37 MeV, …; four- and five-dimension modes near the τ mass). None of it resembles the lepton spectrum.

**What follows:**
- **K4/K5's fits hold in the glued-sheets reading** (G1: sheets joined only through shared circles), not in a single-torus reading as they stand.
- **The whole-manifold picture is a real fork:**

| Reading | K4/K5 fits | Source of mixing | Charge rule for 3+-dimension modes |
|---|---|---|---|
| Glued sheets | valid | connections between sheets (junctions, hub) | rarely matters |
| Single torus | would need a new fit in which particles are multi-dimension modes | the manifold itself | central |

- A consistent single-torus search would enumerate *all* circulation patterns with the full shifts, plus a charge rule (decision A) for each. The first version of `lepton_search` mixed the two readings, applying single-torus shifts to single-sheet modes only, which is why it was corrected to the glued reading.
- This is recorded here only; ma-domain is left unchanged.

**The assumption this exposes.** "The lightest states are the observed particles" is stricter than ma-domain's working assumption, which allows unobserved higher modes that decay away ([ma-domain README](../../ma-domain/README.md), working assumptions). By the strict rule ma-domain's K4 would also fail: its μ sheet has an fm-scale ring, which places sibling charged states near 1.2 GeV, below the τ. A decision is needed: keep the strict rule (and look for geometries that satisfy it), or adopt ma-domain's looser rule (and specify which extra states are tolerated, and why they are not seen).

## What this leaves

- If the neutrino cannot live on a delta dimension, it needs its own line, which brings the question back to 1a and its junctions.
- 1b could revive if some lepton layout has a large *unsheared* dimension shared with an electron sheet, or if the shear convention (which direction σ acts along) is revisited in ma-domain.
