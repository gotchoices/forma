# Two-slit interference on a 2D GRID lab (Act 2, step 1: the wave half)

Sim: [`../scripts/dualslit.py`](../scripts/dualslit.py). Figures in
[`../outputs/`](../outputs/) (`dualslit_2slit.png`, `dualslit_1slit.png`).

**Invocation (convention-pinned 2026-09-18):**
`dualslit.py --nc 0 --omega 0.5 --slits {1,2} --scatter legacy`. The script's
default scatter is now `canonical`; this 2D run predates that and is pinned to
`legacy` so the results below reproduce exactly. In **two** axes the two
conventions have the same dispersion, but they place the propagating band
differently (Ω = ω vs Ω = π − ω), so the same `--omega` means a different
physical frequency in each — hence the pin.

> **⚠ Open item, logged 2026-09-18 — the λ ≈ 9 used in the λL/d check below is
> not this wave's wavelength.** Under the pinned (legacy) convention at ω = 0.5,
> the two-axis band condition cos ω = −(cos k_x + cos k_y)/2 has **no on-axis
> solution**: cos k_x would have to be −2.76. Propagation happens only through
> large-k **zone-corner** modes — the k_y = π branch gives λ_x = 2.59 nodes, and
> an FFT of the field measures **2.60 ± 0.03**, matching it to 0.4%. The "λ ≈ 9
> (from ω = 0.5, c ≈ 0.7)" figure in §Result is a *continuum* estimate 2πc/ω,
> and it does not apply to a mode sitting near the Brillouin zone corner.
>
> What this does and does not touch. The **interference claim stands**: the
> one-slit vs two-slit spacing discriminator (85.7 vs 28.7) is empirical and
> needs no wavelength. The **λL/d agreement does not stand** — with λ = 2.6 the
> textbook formula gives ≈7.6 nodes, not the ≈26 quoted, so the reported match
> to 28.7 is a coincidence. Ch 8's Born/click results rest on the |field|²
> pattern, not on λ, and are unaffected.
>
> This is a *different* defect from [../review.md](../review.md)'s (which
> concerned the three-axis dispersion relation) and was found while fixing it.
> A re-run at a drive that is genuinely in-band on-axis — e.g. the canonical
> convention at ω = 0.5, where λ = 8.79 analytic and 8.90 ± 0.29 measured, close
> to the ≈9 this file assumed — would settle it, at the cost of new fringe
> numbers for this chapter. Not yet done; deferred as its own decision.

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

## Step 2a done — single lumps rebuild the fringes (no collapse invoked)

`dualslit.py --clicks N` samples single-lump detections from the two-slit
|field|² pattern (each a whole quantum, per grid-quantization). Correlation of the
lump histogram with |field|²:

| single lumps | corr with |field|² |
|---|---|
| 30 | +0.44 |
| 300 | +0.73 |
| 3000 | **+0.97** |

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
