# mast-intro images

Visuals referenced by `../deck.md`. Mermaid sources (`.mmd`) build to SVG
via `make diagrams`. Raster screenshots (`.png`) are captured manually
from the viz gallery and checked in as-is.

None of these are present yet — the deck reads fine as a text-only
outline. Add them incrementally; update the deck to reference each as
it lands.

## Priority (add in this order)

### 1. Hero — `hero-torus.png`

Opens slide 1 and closes the deck. Screenshot from `viz/torus-studio.html`:

- Preset: electron (R8 ratio, shear ≈ 2)
- (1, 2) winding visible as a glowing photon trail
- Dark background, centered, 1600 × 900 or larger
- Ideally rendered so the photon tracks a full period

### 2. Mirror-box → rest-mass — `mirror-box.svg`

Illustrates the core move (slide 6, "confine a photon"). Side-by-side:

- Left: free photon, arrow labeled `E = hf, p = E/c, m = 0`
- Right: photon bouncing between two mirrors of separation L, labeled
  `m = nh/(2Lc)`
- Optional: a small "boost" arrow showing the box gaining velocity to
  reinforce that inertial mass = rest mass

Draw in Mermaid (`graph LR`) or hand-produced SVG.

### 3. Arena diagram — `arena-11d.svg`

**Two slides in the deck:** (1) product / ordering + display equation, (2) full-width
**Block | Dim | Notes** table. Do not make the on-slide text smaller than the rest of
the deck; split art the same way if needed.

Match **metric block order** (11 base directions):

`ℵ` → `Ma_p` → `Ma_e` → `Ma_ν` → `S` → `t`

- **ℵ** (1D) — sub-Planck; α coupling (tube ↔ ℵ ↔ t)
- **Ma_p, Ma_e, Ma_ν** (2D each) — three 2-tori with scales ~fm, ~pm, ~μm
- **S** (3D) — extended space
- **t** (1D) — time

Mermaid flowchart or hand-drawn SVG — left-to-right in that order; optional
arrows S³ and “× t” to echo the product $\aleph \times T^6 \times S^3 \times t$.

### 4. Sheet-count → SM taxonomy — `spin-taxonomy.svg`

Slide 9. Three columns (1 sheet, 2 sheets, 3 sheets) → SU(2) product →
spin set → SM class (lepton / meson / baryon). Small torus icons for
each active sheet.

### 5. Z₃ cancellation — `z3-cancel.svg`

Slide 11. Three (1, 2) constituents at 120° phase offsets on the proton
sheet; their 2ω density fluctuations summed to zero. A phasor-style
diagram works well (three arrows rotated 120° → sum = 0).

### 6. Scorecard bar chart — `scorecard.svg` *(optional)*

Slide 3. Horizontal bar chart of |Δm/m| for each of the 16 particles,
grouped by class, sorted ascending. Highlight the pion outliers in red.
Export from a small matplotlib script or Observable notebook; commit
both the script and the resulting SVG.

### 7. GRID block diagram — `grid-stack.svg` *(optional)*

Slide 16. The two-layer stack:

```
GRID lattice ──► Maxwell + G
             │
             ▼
MaSt T⁶ ──► particles
```

Could be a Mermaid `flowchart TD`.

## Capture tips

- Viz screenshots: run `cd viz && python3 -m http.server 8765`, open
  the tool, hide controls where possible, capture at 2× DPI.
- Keep raster images to PNG and vector to SVG. Avoid JPEG.
- Commit source (.mmd, .py, etc.) alongside the final asset so the
  figure can be regenerated.
