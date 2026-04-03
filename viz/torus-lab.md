# Torus Lab — Spec

Interactive workbench for exploring the resonant mode spectrum of
a toroidal cavity, placing aperture slot groups, and evaluating
how slots filter modes and modify charge and magnetic moment.
Supports arbitrary particle mass (electron now, proton later).
Single HTML file, no build step.

Context: R46 (electron filter), R21 (curved-torus eigenmodes),
torus-modes (eigensolver reference implementation).

---

## 1. Physics Model

### 1.1. Core assumptions

1. **Scalar eigenmode on a 2D sheet** — the mode is a standing
   wave ψ = f(θ₁) × e^{iq_eff θ₂} on the torus surface T².
   The tube profile f(θ₁) is obtained by solving the
   Sturm-Liouville equation with full torus metric.  Since
   |e^{iq θ₂}|² = 1, energy density depends only on θ₁.

2. **Medium-as-polarizer** — the 2D material sheet enforces:
   - E is always normal to the surface (pointing outward)
   - B is always tangential to the surface (perpendicular to
     the geodesic direction)
   - This is a physical property of the sheet, not derived from
     a vector wave equation.

3. **Random phase** — the phase of the e^{iq θ₂} factor
   fluctuates.  Time-averaged field magnitudes are uniform in
   θ₂.  Only the θ₁ profile matters for observable quantities.

4. **Surface coupling** — the sheet transmits some fraction of
   the internal field to the external world.  The coupling may
   be a combination of surface impedance, shear, and slot
   geometry.  Initially we treat it as ~1/α, but this is a
   working assumption — the actual coupling will be refined as
   we fit charge to observation.

### 1.2. Sturm-Liouville equation

```
d/dθ₁ [(1 + ε cos θ₁) df/dθ₁]
  + [λ(1 + ε cos θ₁) − ε²q²/(1 + ε cos θ₁)] f = 0
```

where ε = a/R (aspect ratio), q = q_eff = n₂ − s·n₁.

Eigenfunctions have definite parity under θ₁ → 2π − θ₁:
- **Even** (cos-like): peaks at outer/inner equator
- **Odd** (sin-like): peaks at top/bottom of tube

On the curved torus (ε > 0), the potential well ε²q²/(1+ε cos θ₁)
pulls even-mode amplitude toward the outer equator.  This
localization increases with ε and q.

### 1.3. Cavity mode sweep

Rather than selecting individual modes, the tool sweeps all
plausible (n₁, n₂) combinations up to a cutoff and solves the
eigenvalue problem for each.  This gives the full resonant
spectrum of the cavity — what rings, at what energy, and with
what tube profile.

For each mode (n₁, n₂, parity):
1. Compute q_eff = n₂ − s·n₁.
2. Solve the Sturm-Liouville eigenproblem → eigenvalue λ and
   tube profile f(θ₁).
3. Compute the charge overlap integral C.
4. Compute the mode's effective mass from the eigenvalue.

The eigensolver is the same Fourier-Galerkin method from
torus-modes.html (N = 16, Cholesky + Jacobi, ~1 ms per mode).
Sweeping ~50 modes is still < 100 ms — instant for the user.

### 1.4. Slot coupling and mode damping

Slots are not cosmetic overlays — they modify the cavity's
effective Q for each mode.  A slot at tube position θ₁_c with
height h lets energy escape proportional to the mode's field
density at that location.

**Coupling strength per slot for mode m:**
```
γ_m ∝ f_m(θ₁_c)² × w × h_eff
```

where h_eff accounts for the torus metric:
```
h_eff = h_rad + ε [sin(θ₁_hi) − sin(θ₁_lo)]
```

A slot group with N copies equally spaced around the ring at the
same θ₁ multiplies the coupling by N (the θ₂ positions are
irrelevant to the magnitude since |e^{iq θ₂}|² = 1, but they
do affect the visual rendering).

**Mode damping:** each mode's Q factor drops in proportion to
its total slot coupling.  Modes with high f(θ₁)² at the slot
position are heavily damped; modes with low density there survive.
The relative damping between modes is the discrimination metric.

**Charge leakage from one slot:**
```
ΔQ ∝ f(θ₁_c)² × cos(θ₁_c) × w × h_eff
```

The cos(θ₁_c) factor projects the outward surface normal onto
the 3D radial direction: at the outer equator (θ₁ = 0) E points
radially outward, at the inner equator (θ₁ = π) it points
radially inward.

**Moment leakage from one slot:**
```
Δμ ∝ f(θ₁_c)² × w² × h_eff
```

The w² factor is from magnetic fringing (Bethe scaling for
tangential B crossing a narrow slot).

### 1.5. Derived quantities

| Quantity | Formula | Notes |
|----------|---------|-------|
| q_eff | n₂ − s·n₁ | Effective ring winding |
| λ (eigenvalue) | from eigensolver | Dimensionless mode energy² |
| f(θ₁) density | \|f(θ₁)\|² (256 samples) | Normalized, max = 1 |
| Charge overlap C | ∫ f(θ₁) cos θ₁ (1+ε cos θ₁) dθ₁ | Net outward flux |
| μ (KK mass) | √(1/ε² + q²) | Dimensionless mass parameter |
| R (ring radius) | λ̄_C × μ | From particle mass |
| a (tube radius) | ε × R | |
| Shear s | free slider, or solve α = 1/137 | User controls |
| α(ε,s) | μ sin²(2πs) / (4π q²) | CP vector formula |

### 1.6. Ghost discrimination

The electron (1,2 even, q_eff ≈ 1.93) and ghost (1,1 even,
q_eff ≈ 0.93) have different f(θ₁) profiles.  The electron's
stronger q_eff creates a deeper potential well, concentrating
its wave function more toward the outer equator.  The ghost
is more spread around the tube.

Discrimination metric:
```
D = f_ghost(θ₁_slot)² / f_electron(θ₁_slot)²
```

A slot at a θ₁ where D > 1 drains the ghost more than the
electron.  Optimal discrimination comes from placing slots
where the ghost is strong but the electron is weak (near the
inner equator, θ₁ close to π).


## 2. User Interface Layout

```
┌────────────────────────────────────────────────────────┐
│  TOP BAR: title, ε slider, shear slider + [Solve], ... │
├───────────────────┬────────────────────────────────────┤
│                   │                                    │
│  LEFT PANEL       │         MAIN VIEW                  │
│  (~300 px)        │                                    │
│                   │  ┌──────────────────────────────┐  │
│  ┌─────────────┐  │  │                              │  │
│  │ Particle    │  │  │   3D Torus                   │  │
│  │ selector    │  │  │   Density glow, geodesics    │  │
│  │             │  │  │   Slots as dark patches      │  │
│  │ Derived     │  │  │                              │  │
│  │ values      │  │  └──────────────────────────────┘  │
│  │             │  │                                    │
│  │ ─────────── │  │  ┌──────────────────────────────┐  │
│  │ Slot groups │  │  │                              │  │
│  │ [+ Add Grp] │  │  │   2D Unrolled Sheet          │  │
│  │             │  │  │   Density heatmap, geodesics  │  │
│  │ ─────────── │  │  │   Slot groups as rectangles  │  │
│  │ Profiles    │  │  │   Draggable / resizable      │  │
│  │ [Save] [Load│  │  │                              │  │
│  │             │  │  └──────────────────────────────┘  │
│  │ ─────────── │  │                                    │
│  │ Metrics     │  │  ┌──────────────────────────────┐  │
│  │ panel       │  │  │  Mode Spectrum               │  │
│  │             │  │  │  eigenvalue vs (n₁,n₂)       │  │
│  └─────────────┘  │  │  known particles marked      │  │
│                   │  │  slot-damped modes dimmed     │  │
│                   │  └──────────────────────────────┘  │
│                   │                                    │
│                   │  ┌──────────────────────────────┐  │
│                   │  │  1D Profile: f(θ₁)²          │  │
│                   │  │  per mode, slot positions     │  │
│                   │  └──────────────────────────────┘  │
│                   │                                    │
├───────────────────┴────────────────────────────────────┤
│  STATUS BAR: α validation, warnings                    │
└────────────────────────────────────────────────────────┘
```

### 2.1. Top bar

Standard totu-viz top bar with:

| Control | Type | Default | Range |
|---------|------|---------|-------|
| a/R (= ε) | slider + readout | 2.0 | 0.01 – 10 (non-linear) |
| Shear s | slider + readout | 0.068 | 0 – 0.5 |
| [Solve] | button | — | Sets s to satisfy α = 1/137 |

a/R is a free variable.  Dragging the slider rescales the torus
in real time and recomputes the full mode spectrum.

Shear is a free slider.  The user adjusts slots and observes how
charge changes, then clicks [Solve] to find the shear that
restores α = 1/137.036 (or the desired charge).  This lets the
user see the interplay between slot effects and shear correction.

Preset buttons for a/R: Ring (0.50), Horn (1.00), r=2.

### 2.2. Left panel — Particle selector

| Control | Type | Notes |
|---------|------|-------|
| Particle | dropdown | Electron / Proton / Custom |
| Mass (custom) | numeric input | Editable when "Custom" |

Selecting a particle sets the mass, which scales R and a via the
Compton wavelength.  Also determines which (n₁, n₂) mode is
"this particle" for the spectrum display.

### 2.3. Left panel — Derived values

Read-only display, updated live:

- Shear s and computed α
- R, a (with SI prefix, e.g. "0.77 fm")
- Total Q/e (from coupling model)

### 2.4. Left panel — Slot groups

Slots are managed as **groups**.  Each group defines a slot shape
and a clone count — the number of copies equally spaced around
the ring (in θ₂).  This is the primary editing interface.

Each slot group row:

| Field | Type | Default | Notes |
|-------|------|---------|-------|
| Name | text | "Group 1" | User-editable label |
| θ₁ center | numeric, 0–360° | 0° | Tube position |
| Height h | numeric, 1–180° | 50° | Tube span |
| Width w | numeric, 1–90° | 2° | Ring span per slot |
| Count | integer, 1–12 | 2 | Copies equally spaced in θ₂ |
| Color | swatch | per-group | For rendering |
| ✕ | delete button | — | |

The individual slot θ₂ positions are computed automatically:
θ₂_k = k × 360° / count, for k = 0, 1, …, count−1.

**[+ Add Group]** button.

Typical configurations:
- Electron: 1 group with count = 2 (two slots 180° apart)
- Proton: 1 group with count = 3 (three slots 120° apart)
- Multiple groups for mixed filtering strategies

### 2.5. Left panel — Profiles (save/load)

Named configurations stored in localStorage:

- **[Save]** button: prompts for a name, saves current state
  (ε, s, particle, all slot groups) under that name.
- **Profile list**: dropdown of saved profiles.  Select to load.
- **[Delete]** button: removes the selected profile.

This lets the user experiment freely and return to known-good
configurations.

### 2.6. Left panel — Metrics

Computed live for the current slot group configuration:

| Metric | Description |
|--------|-------------|
| Per-mode coupling | f(θ₁)² at each group's slot position |
| Relative damping | How much each mode is damped vs the target |
| Ghost/target D | Discrimination ratio per mode pair |
| Total ΔQ/e | Net charge modification from all slots |
| Total Δμ/μ_B | Net moment modification from all slots |


## 3. Main View Panels

### 3.1. 3D Torus (top)

Three.js scene (adopted from torus-modes.html architecture):
- Torus mesh with per-vertex color from |f(θ₁)|² (additive glow)
  for the dominant mode (selected particle's mode).
- Translucent dark shell for depth.
- Geodesic tube overlays for the dominant and ghost modes.
- **Slots rendered as dark patches** on the surface (vertex
  darkening in the slot regions).
- OrbitControls for rotation.

### 3.2. 2D Unrolled sheet (middle)

Canvas rendering of the (θ₂, θ₁) sheet:

- **Background**: density heatmap — |f(θ₁)|² shows as horizontal
  bands of varying intensity (uniform in θ₂).  Color from the
  dominant mode.
- **Geodesics**: wrapped line segments for the dominant mode's
  (n₁, n₂) path and the ghost mode.  Straight lines on the flat
  sheet: θ₁ = n₁·t·360°, θ₂ = n₂·t·360°.
- **Slot groups**: filled rectangles with colored borders.  Each
  group's cloned copies shown at their computed θ₂ positions.
  - **Draggable**: click and drag to reposition (updates θ₁ for
    the whole group — all clones share the same tube position).
  - **Resizable**: drag top/bottom edges to change h, left/right
    to change w.
- Axis labels: θ₂ (horizontal, 0–360°), θ₁ (vertical, 0–360°).

### 3.3. Mode spectrum (below sheet)

Canvas plot showing the full resonant spectrum of the cavity:

- **Horizontal axis**: mode identity, ordered by eigenvalue
  (ascending energy/mass).
- **Vertical axis**: eigenvalue λ (or equivalent mass in eV/c²
  or as a ratio to the electron mass).
- **Each mode drawn as a bar or dot**, labeled (n₁, n₂).
- **Known particle masses marked** as horizontal reference lines:
  - Electron (me), muon (mμ), tau (mτ) — three generations
  - Proton (mp), if different sheet
  - Neutrino masses (if applicable)
- **Slot-damped modes dimmed**: modes with high slot coupling
  shown at reduced opacity or crossed out, indicating they would
  be filtered.  Modes that survive the slots shown at full
  brightness.
- **Clicking a mode** in the spectrum selects it for detailed
  display in the 1D profile and 3D view.

This panel answers: "what rings in this cavity, and what survives
the slots?"

### 3.4. 1D profile plot (bottom)

Canvas line plot, θ₁ on horizontal axis (0–360°):

- **Solid line**: |f(θ₁)|² for the selected mode (from spectrum
  click or the dominant particle mode).
- **Dashed line**: |f(θ₁)|² for the ghost mode, for comparison.
- **Vertical bars**: one per slot group, at the group's θ₁
  center, spanning the height range.  Colored to match the group.
- **Annotations**: at each slot, show the density value for the
  selected mode and ghost, and the discrimination ratio D.

This panel shows directly where the slot sits relative to the
mode profiles — the key to understanding filtering.


## 4. Interactions

### 4.1. Parameter changes

Any change to ε, s, or particle mass triggers:
1. Re-solve the eigenproblem for all modes in the sweep.
2. Update eigenvalue spectrum, density arrays, charge overlaps.
3. Rebuild 3D mesh colors and geodesics.
4. Redraw 2D sheet, spectrum, and 1D profile.
5. Recompute slot coupling metrics.

Eigensolver: ~1 ms per mode × ~50 modes = ~50 ms.  Acceptable
for slider interaction.  Can throttle to recompute on mouseup
for ε slider if needed.

### 4.2. Slot group management

- **Add**: click [+ Add Group].  New group appears with defaults.
- **Edit**: type values in the group row, or drag/resize on the
  2D sheet.  Dragging moves the group's θ₁ (all clones move
  together).  Resizing adjusts h or w.
- **Clone count**: change the count spinner.  Clones appear/
  disappear on the 2D sheet instantly.
- **Delete**: click ✕ in the group row.

### 4.3. Slot dragging on 2D sheet

- **Click on a slot rectangle**: selects the group (all clones
  highlight).
- **Drag any clone**: moves the group's θ₁ center (vertical
  only — θ₂ positions are computed from the count).
- **Drag top/bottom edge**: resizes height for the whole group.
- **Drag left/right edge**: resizes width for the whole group.

### 4.4. Profile save/load

- **Save**: click [Save], enter name in a prompt.  Current state
  (ε, s, particle, slot groups) serialized to localStorage under
  a namespaced key.
- **Load**: select from dropdown.  State restored.
- **Delete**: select + click [Delete].  Removed from storage.

### 4.5. Spectrum interaction

- **Click a mode bar/dot**: selects that mode.  Its f(θ₁)² is
  shown in the 1D profile.  Its density colors the 3D torus.
- **Hover**: tooltip with (n₁, n₂), λ, mass, C, slot coupling.


## 5. Rendering Details

### 5.1. Technology

- 3D: Three.js 0.163.0 (via totu-viz.js shared infrastructure)
- 2D sheet, spectrum, and 1D profile: Canvas 2D context
- Single HTML file, no build step
- ES module imports via importmap

### 5.2. Color palettes

- Mode density on 3D: selected mode's color, intensity modulated
  by |f(θ₁)|².
- 2D heatmap: same color as 3D surface.
- Slot groups on 2D: semi-transparent fill with 2px colored
  border, per-group color.
- Spectrum: active modes bright, slot-damped modes dimmed.
  Known particle reference lines in distinct muted colors.
- 1D profiles: selected mode solid, ghost dashed, slot bars in
  group colors.

### 5.3. Performance

The field depends only on θ₁ (not θ₂), so the 2D heatmap is
computed as a 1D array and replicated horizontally — essentially
free.  The eigensolver runs ~1 ms per mode.  Full sweep of ~50
modes: ~50 ms.  Slot metrics are trivial lookups into the density
array.

Use `requestAnimationFrame` for smooth drag updates.  Throttle
full spectrum recomputation during slider drag if needed
(recompute on mouseup).

### 5.4. 3D slot visualization

Vertex darkening: for each vertex whose (θ₁, θ₂) falls inside
any slot, set color to zero.  The slot appears as a dark band on
the glowing surface.

### 5.5. Validation

On startup, compute α from default parameters (ε = 2.0, solved
shear) and verify it matches 1/137.036 to 6 significant figures.
Show result in status bar.


## 6. File

```
viz/
  torus-lab.md       ← this spec
  torus-lab.html     ← the application
```

After creation, add a card to `index.html` and an entry to the
tools table in `README.md`.


## 7. Future extensions (out of scope for v1)

- 3D slot cutouts (geometry removal instead of vertex darkening)
- Animated phase rotation
- Export slot configurations to JSON
- Cross-section polar plot inset (|f(θ₁)|² as polar)
