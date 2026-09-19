# Two-slit interference on a 2D GRID lab (Act 2, step 1: the wave half)

Sim: [`../scripts/dualslit.py`](../scripts/dualslit.py). Figures in
[`../outputs/`](../outputs/) (`dualslit_2slit.png`, `dualslit_1slit.png`,
`dualslit_2slit_clicks.png`).

**Invocation:** `dualslit.py --nc 0 --omega 0.5 --slits {1,2} [--clicks 3000]`,
on the default **canonical** scatter.

**Revised 2026-09-18.** This run previously used the direction-of-travel
(`legacy`) register labeling, under which a drive of ω = 0.5 is **off-band on
axis**: the two-axis condition cos ω = −(cos k_x + cos k_y)/2 would need
cos k_x = −2.76. Propagation happened only through large-k **zone-corner** modes
(the k_y = π branch, λ_x = 2.59 nodes; an FFT of the field measured 2.60 ± 0.03),
so the "λ ≈ 9" used in the λL/d check below was a *continuum* estimate 2πc/ω that
did not describe the wave actually propagating. On the canonical scatter the band
sits at Ω ≈ 0, the same ω = 0.5 is squarely in-band on axis, and λ = 8.79 analytic
/ **8.90 ± 0.29 measured** — so the wavelength this file always assumed is now
the real one. Details in §Revision record.

## The GRID reading of the apparatus (Kyle's framing, realized)

- The lab is **continuous GRID** — a 2D (x,y) S-space with the impedance scatter.
- A **barrier** = nodes **blocked by mass** → they absorb (field forced to 0).
- A **slit** = **open GRID** → photons transmit freely.
- A two-slit barrier is therefore continuous GRID everywhere except two open
  channels. A broad coherent wavefront is launched from the left; only the two
  slits transmit.

## Result: genuine two-slit interference

| config | detector pattern |
|---|---|
| **2 slits** | **fringes**, period **28.8 ± 3.6 nodes** (FFT of the backdrop), 6 maxima |
| 1 slit | **single lobe**, no fringes (1 maximum) |

The **one-slit control is a clean single lobe**, so the structure in the two-slit
case is interference and not single-slit diffraction ripple: the wave passes
through **both** open-grid slits and the two transmitted waves interfere —
**information from both slits reaches every detector point.** The GRID slit-model
works.

The fringe period is also **consistent with the textbook paraxial formula**
Δ ≈ λL/d: with L = 285−110 = 175 (barrier→detector), d = 60 (slit separation) and
the measured λ = 8.90 ± 0.29, it predicts 26.0 nodes against 28.8 ± 3.6 observed.
Consistent — but see the limit below before reading that as precision.

*(Two measurement cautions, both learned the hard way. **Fringe period**: this is
now taken from an FFT of the backdrop, not from the mean gap between maxima
clearing a threshold. That older statistic measures span ÷ peak count, so it
tracks the envelope as much as the fringes, and it misread this very run's
28.8-node period as 34.6 in one configuration. **Regime**: with d = 60, L = 175,
λ ≈ 8.9 the Fresnel number d²/λL ≈ 2.3 — the near field — and Δ = λL/d is a
far-field formula. It is being checked against here, not tested. The FFT period
is itself bin-limited to about ±3.6 nodes. So "consistent" is the right word and
"matches" is not.)*

## What this is and isn't

- **Is:** the **wave** half of the dual slit — delocalized transmission through
  both slits, interference in |field|². This is the easy, linear, expected half,
  and it confirms the apparatus and the GRID slit ontology.
- **Is not:** the **particle** half — a single, localized **click** (a lump) at
  the backdrop, built up over many trials into the fringe pattern. That is the
  measurement problem, and it is the hard core (Act 2, step 2).

## Step 2 — the particle half (the amazing thing to show)

Goal: a **breather/quantum arrives as a single localized lump** at the backdrop,
**even though the GRID nodes at both slits transmitted the information**. Two
ingredients, and one honors an existing result:

1. **Whole-quantum detection (honor [grid-quantization](../../grid-quantization/)).**
   grid-quantization established that light is **quantized** on the bounded
   substrate — energy comes in whole quanta. The detection must be a **single whole
   quantum**, not a fraction. We build the click *on* that result, not around it.
2. **Born placement.** The single quantum instantiates where the interfering field
   supports it — P(click at y) ∝ |field(y)|² — so single clicks, accumulated over
   many trials, **rebuild the fringe pattern**. That is the M4 Born test, now on a
   genuinely interfering 2-slit field.

## Step 2a done — single lumps rebuild the fringes (no collapse invoked)

`dualslit.py --clicks N` samples single-lump detections from the two-slit
|field|² pattern (each a whole quantum, per grid-quantization). Correlation of the
lump histogram with |field|²:

| single lumps | corr with |field|² |
|---|---|
| 30 | +0.40 |
| 300 | +0.87 |
| 3000 | **+0.99** |

Single lumps **rebuild the two-slit fringes** — the Tonomura single-particle
build-up, on the GRID lab. **Reframed (Kyle):** each lump is a *revealed
hidden-variable centre* (the breather's focal point), distributed ∝ |field|² —
**not** a collapse. The wave (de Broglie, through both slits) sets the pattern; the
lump was localized all along; detection reveals it. "Many nodes transmit, one lump
detected" — shown.

## What 2a settles, and the two things still owed

- **Settles (consistency):** whole-quantum lumps distributed ∝ |field|² reproduce
  the two-slit interference. Collapse is *not needed* if the lump is a real
  hidden-variable centre (double-solution / de Broglie pilot). The moving
  breather's **de Broglie wave** (phase harmony, λ = h/p) is the extended pilot
  that passes both slits; its wavelength sets the measured fringe spacing.
- **Owed 1 — Born from a mechanism.** 2a *assumes* P(centre) ∝ |field|² and
  *samples* it. Deriving that distribution (quantum equilibrium) and the
  **guidance dynamics** (does the lump actually get steered to those positions by
  its own de Broglie wave? — the untested bulk⟷pilot coupling) is the real work.
- **Owed 2 — Bell.** The hidden variable (centre/phase) evades Bell only if it is
  **non-locally correlated through the compact dimension** — and that correlation
  must reproduce the *exact* Bell violations, with no signaling. This is the
  sharpened core (collapse dissolved → Bell-correct non-locality remains). The
  compact **fiber** / phase harmony is the candidate carrier
  ([thesis-wave-until-interaction.md](thesis-wave-until-interaction.md)).

So Act 2's score: **collapse — dissolved** (real lump = hidden variable);
**Born-from-mechanism and Bell-correct non-locality — the frontier.**

## Revision record (2026-09-18)

- **Scatter convention.** Moved from `legacy` (direction-of-travel registers) to
  the default `canonical` (edge end-registers). In two axes the two have the same
  *dispersion*, but they place the propagating band differently — legacy at
  ω ≈ π, canonical at ω ≈ 0 — so the same `--omega` selects a different physical
  Ω under each. At ω = 0.5 that is the difference between an off-axis zone-corner
  mode (λ = 2.6) and a clean on-axis band mode (λ = 8.9). See
  [dispersion-analytic.md](dispersion-analytic.md) §Two register conventions.
- **λ is now real, and measured.** 8.79 analytic, 8.90 ± 0.29 by FFT — vindicating
  the ≈9 this file had assumed on continuum grounds, which under the old
  convention was not the propagating wavelength.
- **Fringe period essentially unchanged**: 28.7 (old peak-count) → 28.8 ± 3.6
  (FFT). The observable that carried the interference claim did not move.
- **One-slit control improved**: 4 maxima (over-labelled as "fringes" by the old
  peak counter) → a clean single lobe, 1 maximum. The discriminator no longer
  needs the spacing caveat the previous draft carried.
- **Clicks**: correlations 30 / 300 / 3000 lumps move from +0.44 / +0.73 / +0.97
  to +0.40 / +0.87 / +0.99. The Born/click result rests on the |field|² backdrop,
  which is why it is insensitive to all of the above.
- **Ch 8 is unaffected in substance** — it uses these fringes qualitatively and
  makes no numerical use of λ or the fringe period.

Found while fixing [../review.md](../review.md)'s three-axis finding; logged as an
open item there, and now closed.
