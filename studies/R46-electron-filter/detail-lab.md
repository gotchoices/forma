# Track 3: Interactive Eigenmode Lab — Specification

## 1. Purpose

A single-page HTML/JavaScript application for exploring EM
eigenmodes on a torus surface in real time.  The user can:

- Select a particle mass (electron, proton, or custom) to fix the
  physical scale.
- Choose mode quantum numbers (n₁, n₂) and view the resulting
  field patterns.
- Place, move, resize, and delete aperture slots on the torus.
- Observe how each slot configuration affects ghost filtering,
  charge leakage, and magnetic moment — updated live.

This tool replaces static SVG generation with an interactive lab
for rapid hypothesis testing.  It will be used for the electron
study now and extended to the proton later.

**File:** `outputs/eigenmode-lab.html` (self-contained, no build step).


## 2. Physics Model

All formulas come directly from `scripts/torus_model.py`.  The
HTML app reimplements them in JavaScript.  The key equations are:

### 2.1. Geometry (KK Compton constraint)

```
q_eff   = n₂ − s
μ       = √(1/r² + q_eff²)
R       = λ̄_C × μ          (ring radius, from particle mass)
a       = r × R              (tube radius)
A       = 4π² a R            (surface area)
```

where λ̄_C = ℏ/(mc) is the reduced Compton wavelength for the
selected particle mass m.

### 2.2. Shear from α

The shear s is determined by solving:

```
α = μ sin²(2πs) / (4π q_eff²)
```

for s, given r and α = 1/137.036.  Use bisection on s ∈ (0, 0.5).

### 2.3. Field functions

All fields depend on θ₂ only (θ₁ independence from CP n₁ = 1):

| Quantity | Formula | Range |
|----------|---------|-------|
| Radiation pressure (unipolar) | P(θ₂) = 1 + cos(q_eff θ₂) | [0, 2] |
| Charge modulation (AC) | E_AC(θ₂) = cos(q_eff θ₂) | [−1, +1] |
| Tangential B field | B_t(θ₂) = sin(q_eff θ₂) | [−1, +1] |

Field amplitude E₀ from energy normalization:

```
E₀ = √(m c² / (4π² a² R ε₀))
```

### 2.4. Ghost mode

The ghost (1,1) mode uses q_eff_g = 1 − s with the same geometry.
Mass ratio: m_ghost/m_e = μ_g/μ_e.

### 2.5. Slot coupling (linear regime)

For a slot of width w (ring direction) and height h (tube
direction) centered at (θ₂_c, θ₁_c):

```
ΔQ  ∝  cos(q_eff θ₂_c) × w × h_eff
Δμ  ∝  sin(q_eff θ₂_c) × w² × h_eff
```

where h_eff accounts for the torus metric:
```
h_eff = h_rad + r [sin(θ₁_hi) − sin(θ₁_lo)]
```

### 2.6. Phase-optimized discrimination

For a set of N slots at ring positions {θ₂_i}, each mode can pick
a phase φ₀ to minimize its exposure.  The residual field for a
mode with winding q at phase φ₀ is:

```
exposure(φ₀) = max_i |cos(q θ₂_i + φ₀)|
```

The mode picks the φ₀ that minimizes this.  Discrimination ratio
is the ghost's optimized exposure divided by the electron's.


## 3. User Interface Layout

The app is a single full-viewport page with three main regions:

```
┌───────────────────────────────────────────────────────┐
│  HEADER: "Eigenmode Lab — R46"                        │
├────────────────────┬──────────────────────────────────┤
│                    │                                  │
│   CONTROL PANEL    │          VISUALIZATION           │
│   (left sidebar)   │          (main area)             │
│                    │                                  │
│   ┌──────────────┐ │  ┌────────────────────────────┐  │
│   │ Particle     │ │  │  E-field heatmap (top)     │  │
│   │ Geometry     │ │  │  (unrolled sheet)          │  │
│   │ Mode select  │ │  │                            │  │
│   │ Derived vals │ │  │                            │  │
│   │ ──────────── │ │  ├────────────────────────────┤  │
│   │ Slot list    │ │  │  B-field heatmap (middle)  │  │
│   │ [+ Add Slot] │ │  │                            │  │
│   │ ──────────── │ │  ├────────────────────────────┤  │
│   │ Metrics      │ │  │  Geodesic + slots (bottom) │  │
│   │              │ │  │                            │  │
│   └──────────────┘ │  └────────────────────────────┘  │
│                    │                                  │
│                    │  ┌────────────────────────────┐  │
│                    │  │  1D profiles (below)       │  │
│                    │  │  P(θ₂), B(θ₂), ghost       │  │
│                    │  └────────────────────────────┘  │
│                    │                                  │
├────────────────────┴──────────────────────────────────┤
│  STATUS BAR: computed values, warnings                │
└───────────────────────────────────────────────────────┘
```

### 3.1. Control Panel (left sidebar, ~280 px)

#### Particle selector

- **Dropdown:** Electron / Proton / Custom
- Electron: m = 9.109 × 10⁻³¹ kg
- Proton: m = 1.673 × 10⁻²⁷ kg
- Custom: editable mass field (kg), for other particles

#### Geometry inputs

| Control | Type | Default | Range |
|---------|------|---------|-------|
| Aspect ratio r | slider + numeric | 2.0 | 0.1 – 10.0 |

#### Mode selector

| Control | Type | Default |
|---------|------|---------|
| n₁ (tube) | integer stepper | 1 |
| n₂ (ring) | integer stepper | 2 |
| Show ghost | checkbox | checked |
| Ghost n₂ | integer stepper | 1 |

#### Derived values (read-only display)

Updated live as inputs change:

- Shear s
- q_eff (electron), q_eff (ghost)
- R, a (meters, with SI prefix)
- E₀ (V/m)
- Mass ratio m_ghost/m_e
- Total charge Q/e
- Pressure min/max θ₂ positions
- B-field max θ₂ positions

#### Slot list

- Each slot is a row showing: θ₂, θ₁, width, height.
- Each field is editable inline (click to type, or drag on the
  visualization to reposition).
- Delete button (×) per slot.
- **[+ Add Slot]** button: adds a new slot at a default position
  (θ₂ = 90°, θ₁ = 180°, w = 2°, h = 50°).
- Drag handle for reordering (optional, low priority).

#### Metrics panel (below slot list)

Updated live after any slot or parameter change:

| Metric | Description |
|--------|-------------|
| Total ΔQ/e | Sum of charge leakage from all slots |
| Total Δμ/μ_B | Sum of moment contribution from all slots |
| Ghost discrimination | Phase-optimized ratio |
| Electron exposure | Phase-optimized residual |
| Ghost exposure | Phase-optimized residual |

### 3.2. Visualization (main area)

Four vertically stacked panels, all sharing the same horizontal
axis (θ₂ = 0° to 360°) and vertical axis (θ₁ = 0° to 360°) for
the top three:

#### Panel 1: E-field pressure heatmap

- Color-mapped P(θ₂) = 1 + cos(q_eff θ₂) using an "inferno"
  colormap (or similar warm palette).
- Range: [0, 2], always non-negative.
- Slots rendered as semi-transparent rectangles with colored
  borders.

#### Panel 2: B-field heatmap

- Color-mapped |sin(q_eff θ₂)| using a diverging colormap
  (blue-white-red or similar), with sign indicated by hue.
- Range: [−1, +1].
- Same slot overlays as Panel 1.

#### Panel 3: Geodesic + slot map

- Background: light grid.
- Geodesic paths drawn as wrapped line segments for the primary
  mode (n₁, n₂) in one color and the ghost mode in another.
- Slots drawn as filled rectangles with colored borders matching
  the slot list.
- Slots are **draggable** on this panel: click and drag to
  reposition (updates θ₂, θ₁ in the slot list).
- Drag edges/corners to resize (updates width, height).

#### Panel 4: 1D field profiles

- Line plots of P(θ₂) and B(θ₂) vs θ₂ (0° to 360°).
- Electron mode: solid lines.
- Ghost mode: dashed lines.
- Vertical lines at each slot's θ₂ position (colored to match
  slot list).
- Annotations at slot positions showing field values.


## 4. Interactions

### 4.1. Adding a slot

1. Click **[+ Add Slot]** in the control panel.
2. A new slot appears at default position with default size.
3. The slot appears in the slot list and on all visualization
   panels.
4. Metrics update immediately.

### 4.2. Editing a slot

- **In the slot list:** click any numeric field (θ₂, θ₁, w, h)
  and type a new value.  Pressing Enter or clicking away commits.
- **On the geodesic panel:** drag the slot rectangle to change
  (θ₂, θ₁).  Drag edges to change width or height.  The slot
  list updates to match.
- Both methods update all visualizations and metrics in real time.

### 4.3. Deleting a slot

- Click the × button in the slot list row.
- Slot disappears from all panels.  Metrics update.

### 4.4. Changing particle / geometry / mode

- Any change to r, n₁, n₂, or particle mass triggers a full
  recomputation: shear, derived values, field arrays, and metrics.
- Slot positions (in degrees) are preserved across parameter
  changes.

### 4.5. Preset configurations

A small dropdown or button group for quickly loading slot plans:

| Preset | Description |
|--------|-------------|
| Clear all | Remove all slots |
| Plan A | 4 slots at pressure minima |
| Plan B | 3 slots at field maxima |
| Plan C | 4 slots at B-field maxima |

Slot positions are computed from the current q_eff (shear-
corrected), not hardcoded.


## 5. Rendering Technology

- **Canvas (2D context)** for heatmaps and geodesic panels.
  Heatmaps rendered as horizontal bands (field depends only on
  θ₂ for CP n₁ = 1, but the full 2D grid should still be drawn
  to show slot placement in both coordinates).
- **SVG or Canvas** for the 1D profile plot (Canvas preferred
  for consistency).
- All rendering is done client-side.  No server, no build step.
- Target resolution: heatmaps at ~512 × 256 pixels (θ₂ × θ₁).
- Use `requestAnimationFrame` for smooth updates during drag
  operations.

### Color palettes

- E-field (unipolar): warm sequential (black → red → orange →
  yellow → white), similar to matplotlib "inferno".
- B-field: diverging (blue → white → red) centered at zero.
- Geodesics: cyan (primary mode), red-orange (ghost mode).
- Slots: distinct colors per slot (rotate through a palette).


## 6. Computational Notes

### 6.1. Performance

- The field depends only on θ₂ (not θ₁), so heatmaps can be
  computed as a 1D array and replicated across the θ₁ axis.
  This makes recomputation essentially instantaneous (~512
  trig evaluations).
- Phase-optimized discrimination requires a 1D optimization
  over φ₀ ∈ [0°, 360°).  Evaluate at ~360 points and take the
  minimum — negligible cost.
- Total recomputation on any parameter change should be < 1 ms.

### 6.2. Shear solver

Implement bisection in JavaScript, matching `solve_shear` from
`torus_model.py`.  The search range is s ∈ (0.001, 0.499) with
~60 bisection steps (sufficient for double precision).

### 6.3. Validation

On startup, compute α from the default parameters and verify it
matches 1/137.036 to at least 6 significant figures.  Display a
warning in the status bar if validation fails.


## 7. File Organization

```
studies/R46-electron-filter/
  outputs/
    eigenmode-lab.html     ← the application (single file)
```

All JavaScript, CSS, and HTML in one file.  External CDN imports
are acceptable for a colormap library if needed, but the app
should work offline with a basic fallback palette.


## 8. Future Extensions (out of scope for initial build)

- 3D torus rendering (Three.js) showing field intensity on the
  surface with slots cut out.
- Frequency response curves (Q-factor vs. mode number).
- Multi-mode superposition visualization.
- Export slot configurations to JSON for use in Python scripts.
- Proton-specific mode sets (n₁ = 1, n₂ = 3 and beyond).
