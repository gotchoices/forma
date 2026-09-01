# Two-slit interference on a 2D GRID lab (Act 2, step 1: the wave half)

Sim: [`../scripts/dualslit.py`](../scripts/dualslit.py). Figures in
[`../outputs/`](../outputs/) (`dualslit_2slit.png`, `dualslit_1slit.png`).

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
| **2 slits** | **fine fringes**, spacing **~28.7 nodes**, ~10 maxima |
| 1 slit | broad single-slit diffraction lobe (spacing ~85.7, no fine fringes) |

The double-slit fringe spacing matches the **textbook** formula: Δ ≈ λL/d with
L = 285−110 = 175 (barrier→detector), d = 60 (slit separation), λ ≈ 9 (from ω=0.5,
c≈0.7) → **≈ 26 nodes**, vs. measured **28.7**. So this is real interference, not an
artifact: the wave passes through **both** open-grid slits and the two transmitted
waves interfere — **information from both slits reaches every detector point.** The
GRID slit-model works.

*(The script's peak-counter over-labels the single-slit case as "fringes"; the true
discriminator is the **spacing** — 28.7 (two paths interfering) vs 85.7 (one broad
diffraction lobe). Fringe count alone is not the signal.)*

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

The open, hard question (the measurement problem): what in GRID selects **one**
click and forbids the rest while conserving the single quantum — and does it need
the compact **fiber** as the non-local channel (the [Bell/collapse thread](thesis-wave-until-interaction.md))?
This step is where grid-saturation's original thesis (M3/M4) finally gets tested.
