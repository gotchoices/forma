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

## What this leaves

- If the neutrino cannot live on a delta dimension, it needs its own line, which brings the question back to 1a and its junctions.
- 1b could revive if some lepton layout has a large *unsheared* dimension shared with an electron sheet, or if the shear convention (which direction σ acts along) is revisited in ma-domain.
