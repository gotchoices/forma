# Two-slit: photon vs matter wave — the matter case runs (Ch 7, Q1 fix)

Sim: [`../scripts/dualslit.py`](../scripts/dualslit.py). Figures
[`../outputs/dualslit_photon.png`](../outputs/) and
[`../outputs/dualslit_matter.png`](../outputs/).

## Why this exists

The original two-slit sim was a **massless** 2D (x,y) field — the photon/Maxwell
sector GRID already has. Calling its interference a "matter wave / de Broglie λ"
was a category slip (review-5-10.md, Q1). This fix adds a **compact c-axis** (N=6,
c periodic) so the sim can excite a genuine **massive, compact-sector (n≥1) matter
wave** and interfere *that*, on the same lattice.

## Setup

Same two-slit geometry (sep 60, slit 10, barrier→detector L=175), driven on-band
(om=2.7 ⇒ physical Ω = π−om = 0.442). Compact axis nc=12.

- **photon baseline:** `--nc 12 --nmode 0` (c-uniform ⇒ massless).
- **matter wave:** `--nc 12 --nmode 1` (compact n=1 ⇒ rest freq ω₀=0.300, massive).

The de Broglie wavelength is computed **analytically** from the Bloch dispersion
cos Ω = (cos kx + cos ky + cos kc)/3 (on-axis ky=0): cos kx = 3cosΩ − 1 − cos kc.

## Result

| mode | rest freq ω₀ | de Broglie λ (analytic) | fringes? | fringe pattern |
|---|---|---|---|---|
| photon (n=0) | 0 (massless) | **8.07 nodes** | yes | finer (spacing ~5.9) |
| matter (n=1) | 0.300 (massive) | **11.18 nodes** | yes | coarser (spacing ~13.8) |

Two things established:

1. **A massive matter wave two-slit interferes** — fringes appear for the compact
   n=1 mode, on the same GRID lattice as the photon. Act 2's two-slit is now a
   genuine matter-wave demonstration, not only the Maxwell/photon sector. **[C]**
2. **The pattern is mass-dependent, in the de Broglie direction.** The massive mode
   has a **longer** in-plane (de Broglie) wavelength — 11.18 vs 8.07 nodes, exactly
   as the dispersion's cos kc term dictates (mass lowers kx) — and correspondingly
   **wider** fringes. **[C + D for the λ]**

## The honest limit

We do **not** fit the paraxial two-slit law Δ = λL/d: the slits are wide and the
lattice near the band edge is non-paraxial, so the *absolute* fringe spacing is not
λL/d (it isn't, by a factor ~3). The claim is the robust, directional one — matter
interferes, with a longer de Broglie wavelength and a coarser pattern than the
photon — plus the **exact analytic** de Broglie λ from the dispersion. The
interference itself is, as in the photon case, **classical linear-wave** behavior
(both modes are linear Bloch waves, Ch 4); what is new here is only that it is the
*matter* (compact-sector) wave, transferred by linearity. The distinctively-quantum
content is still Ch 8 (the click) and Ch 10 (Bell).
