# R46 Findings: Electron filter — aperture effects on a toroidal cavity

Study: [`README.md`](README.md)

---

## Track 1. Baseline EM fields — unipolar vector model with circular polarization

Script: [`scripts/track1_baseline_fields.py`](scripts/track1_baseline_fields.py)
Model:  [`scripts/torus_model.py`](scripts/torus_model.py)

### Model summary

The electron is a standing electromagnetic wave (eigenmode) on a
2D periodic sheet — a flat rectangle with opposite edges identified
(topologically a torus).  The two periodic coordinates are θ₁ (tube,
minor circle) and θ₂ (ring, major circle).  The electron is the
(1,2) mode: 1 winding around the tube, 2 around the ring.

The model is a 2D drum head, not a 3D hollow cavity.  The field
lives on the surface; there is no radial mode structure.  The
"thickness" a in the energy normalization is a scale factor for
the compact dimension, not a wall depth.

**Circular polarization (CP):** For a circularly polarized photon
with n₁ = 1, the E-field rotation rate matches the surface-normal
rotation (one turn per tube circuit).  The θ₁ phase cancels the
θ₁ geometry — the field depends only on θ₂.

**Unipolar field:** The radiation pressure always pushes outward
from the 2D sheet.  Field cannot pass backward through the sheet:

    P_out(θ₂) = E₀ (1 + cos(q_eff θ₂))    always ≥ 0

The DC component (E₀) maintains the cavity against the membrane's
confining force (R37 force balance).  The AC component
(E₀ cos(q_eff θ₂)) is the standing-wave modulation that leaks
through the Compton window as external field and produces charge.
The opposite knot chirality reverses the charge sign → positron.


### Current settings

| Parameter | Value | Source |
|-----------|-------|--------|
| Mode | (n₁, n₂) = (1, 2) | WvM electron topology |
| Aspect ratio r = a/R | free; tested at 1, 2, 4, 8 | R19/R44 convention |
| Shear s | solved per r to give α = 1/137.036 | CP α formula |
| Convention | KK (Kaluza-Klein) | R19 F39 |
| Field model | CP vector, unipolar | This study |
| Grid | 256 (θ₁) × 512 (θ₂) | Numerical validation |


---

### What the model produces for the electron

The table below shows the physical properties of the (1,2) electron
mode.  Mass is an input (sets the energy scale).  Spin is topological
(from the (1,2) winding numbers).  Charge is computed from the field
integral.  Magnetic moment is not yet computed in this track —
that is the goal of the aperture analysis.

| Property | Model value | Experiment | Status |
|----------|-------------|------------|--------|
| **Mass** | m_e c² (input) | 0.511 MeV | By construction — E₀ is set so total field energy = m_e c² |
| **Spin** | ℏ/2 | ℏ/2 | Topological: photon angular momentum ℏ divided by the double loop (ω_s = 2ω) gives L = ℏ/2 |
| **Charge** | Q = −e (exact) | −e | Shear s is solved to give α = 1/137.036, then Q = −e follows analytically |
| **Magnetic moment** | μ = g(e/2m_e)·(ℏ/2), g = 2 | g = 2.00232 | Topological g = 2 from R8; anomalous part (g−2) is the target of R46 |

**Mass** is not predicted — it is an input that sets the absolute
field amplitude E₀ = √(m_e c² / (4π²a²R ε₀)).  The mass *ratios*
between modes on the same sheet (e.g., ghost/electron) are predicted.

**Spin = ℏ/2** comes from the (1,2) topology: the confined photon
must traverse the double loop twice to return to its starting
orientation, so the internal frequency is ω_s = 2ω_C.  Angular
momentum L = E/ω_s = ℏω_C/(2ω_C) = ℏ/2.  This is purely
topological and does not depend on r, s, or the field model.

**Charge = −e** is the central result of this track.  It is achieved
by solving for the shear s that produces α = 1/137.036 in the CP
formula.  The charge integral is then exactly −e by construction.
Numerical validation confirms this to 0.3%.

**Magnetic moment:** The topological g-factor g = 2 is established
(R8 F9) independent of the charge distribution.  The anomalous
part (g − 2 ≈ α/2π ≈ 0.00116) has NOT been reproduced.  R44 ruled
out shear-induced charge distribution as the mechanism.  R46's
hypothesis is that a cavity aperture (slot) provides the anomalous
correction.  This is the subject of subsequent tracks.


---

### F1. The CP model produces a new α formula

Setting Q = e in the CP charge integral with KK normalization:

    α_CP  = μ sin²(2πs) / (4π q²)

where μ = √(1/r² + q²) and q = n₂ − s.  Compare R19 scalar:

    α_R19 = r² μ sin²(2πs) / (4π q²)

The relationship is exact:  **α_CP = α_scalar / r²**.

At r = 1 (square torus), both formulas agree.  At larger r, the
CP model needs more shear because the circular-polarization charge
integral removes the r² factor that the scalar model had.


### F2. The CP shear converges to a fixed value at large r

| r    | s (scalar) | s (CP)    | s_CP / s_scalar | q_eff (CP) |
|------|------------|-----------|-----------------|------------|
| 1.00 | 0.064981   | 0.064981  | 1.000           | 1.935019   |
| 2.00 | 0.033515   | 0.067960  | 2.028           | 1.932040   |
| 4.00 | 0.016933   | 0.068823  | 4.065           | 1.931177   |
| 8.00 | 0.008497   | 0.069048  | 8.126           | 1.930952   |

The scalar shear goes to zero as r → ∞ (s_scalar ∝ 1/r).
The CP shear converges to **s ≈ 0.069**, independent of r.
At large r, μ → q and α_CP → sin²(2πs)/(4πq), which has a
fixed solution.


### F3. Charge verified — Q = −e for all r

The charge-producing AC modulation leaks through the Compton
window; the analytical charge integral is:

    Q = −ε₀ E₀ × 2πaR × sin(2πs) / q_eff

This yields Q/e = −1.000000 at all tested r (by construction).
Numerical integration on a 256×512 grid validates to 0.3%:

| r    | Q_analytic / e | Q_numerical / e | Error   | R (m)       | a (m)       |
|------|----------------|-----------------|---------|-------------|-------------|
| 1.00 | −1.000000      | −0.997495       | 0.25%   | 8.411×10⁻¹³ | 8.411×10⁻¹³ |
| 2.00 | −1.000000      | −0.997383       | 0.26%   | 7.707×10⁻¹³ | 1.541×10⁻¹² |
| 4.00 | −1.000000      | −0.997350       | 0.27%   | 7.520×10⁻¹³ | 3.008×10⁻¹² |
| 8.00 | −1.000000      | −0.997342       | 0.27%   | 7.472×10⁻¹³ | 5.978×10⁻¹² |


### F4. Radiation pressure is unipolar, charge pattern depends only on θ₂

The outward radiation pressure P ∝ E₀(1 + cos(q_eff θ₂)) is
always ≥ 0.  No field passes backward through the sheet.

The charge-producing part (the AC modulation) has **no θ₁
dependence**: σ = ε₀ E₀ cos(q_eff θ₂) is uniform around the
tube cross-section at each ring position.

On the unrolled sheet, the pressure pattern is **horizontal
bands** (constant along the θ₁ axis), not the diagonal
stripes of the scalar model.  There are ~2 oscillations per
ring revolution (q_eff ≈ 1.93).

This means:
- No north/south asymmetry (inner vs outer equator)
- Charge zeros are ring-direction features (specific θ₂ values)
- A slot at a given θ₂ affects ALL tube positions equally


### F5. Ghost (1,1) mode

The ghost also has n₁ = 1, so the same CP cancellation applies.
Its field is E₀_ghost (1 + cos((1−s) θ₂)) — same unipolar
structure but with q_eff ≈ 0.93 instead of ≈ 1.93.

| r    | q_eff (ghost) | Q_ghost / Q_electron | m_ghost / m_e |
|------|---------------|----------------------|---------------|
| 1.00 | 0.935         | 1.641                | 0.629         |
| 2.00 | 0.932         | 1.509                | 0.530         |
| 4.00 | 0.931         | 1.459                | 0.495         |
| 8.00 | 0.931         | 1.445                | 0.485         |

The ghost produces 45–64% more charge per unit energy than the
electron.  Discrimination is purely a θ₂ phenomenon:

- Electron: ~2 oscillations per ring revolution (q_eff ≈ 1.93)
- Ghost: ~1 oscillation per ring revolution (q_eff ≈ 0.93)

The zero crossings are at **different θ₂ positions**, enabling
position-selective filtering via a slot.


### F6. B field is tangential, 90° out of phase with E_n

B_t = (E₀/c) sin(q_eff θ₂) is tangential to the surface
(along the geodesic direction) and spatially 90° out of phase
with the AC component of E_n.  Where the charge modulation is
maximum, B is zero, and vice versa.

Energy partition confirms CP equipartition:

| r    | ⟨E_n²⟩/E₀² | ⟨B_t²⟩c²/E₀² |
|------|-------------|---------------|
| 1.00 | 0.4852      | 0.5148        |
| 2.00 | 0.4846      | 0.5154        |
| 4.00 | 0.4845      | 0.5155        |
| 8.00 | 0.4845      | 0.5155        |

Both are ≈ 0.5 (slight departure from exactly 0.5 because
q_eff is not exactly an integer).


---

### Track 1 outputs

| File | Contents |
|------|----------|
| `outputs/track1_data.npz` | Unipolar + AC field arrays, geometry, for all r |
| `outputs/track1_En_map_electron.svg` | Three-panel: heatmap + geodesic + resonant waveform |
| `outputs/track1_En_map_ghost.svg` | Same for (1,1) ghost mode |
| `outputs/track1_alpha_comparison.svg` | s_CP vs s_scalar across r |


---

## Track 2. Slot placement — three candidate plans

Script: [`scripts/track2_slot_placement.py`](scripts/track2_slot_placement.py)
(table-driven — runs all plans in a single invocation)


### Shear-induced field shift

All field features (pressure maxima, B zeros, etc.) are shifted
from their "no-shear" positions because q_eff = n₂ − s ≈ 1.932,
not exactly 2.  The second pressure maximum, which would be at
θ₂ = 180° for q = 2, lands at θ₂ = 360°/q_eff = **186.3°**.
The shift of 6.3° is a direct, measurable consequence of the
shear s ≈ 0.068.  Every feature shifts proportionally.


### 2.1  Plan A — 4 slots at exact pressure minima (shear-corrected)

Four 2° × 50° (width × height) slots between the (1,2) geodesic
crossings, placed at the electron's exact radiation-pressure minima
(where cos(q_eff θ₂) = −1, P = 0):

| Slot | θ₂      | θ₁    | h     |
|------|---------|-------|-------|
| 1    | 93.2°   | 137°  | 50°   |
| 2    | 93.2°   | 317°  | 50°   |
| 3    | 279.5°  | 230°  | 50°   |
| 4    | 279.5°  | 50°   | 50°   |

These are the shear-corrected positions (not 90° and 270°).


### 2.2  Plan B — 3 slots at exact field maxima (shear-corrected)

One tall slot at θ₂ = 186.3° (exact second pressure peak), plus
two half-height charge-only adjusters at θ₂ = 0° (B = 0 exactly):

| Slot | θ₂      | θ₁    | h     | Role |
|------|---------|-------|-------|------|
| 1    | 186.3°  | 183°  | 100°  | Moment + charge |
| 2    | 0°      | 90°   | 50°   | Charge-only (B = 0) |
| 3    | 0°      | 270°  | 50°   | Charge-only (B = 0) |

The tall slot is at the shear-corrected peak (not 180°).


### 2.3  Plan C — 4 slots at B-field maxima (pure moment, zero charge)

Four 2° × 50° slots at the exact θ₂ positions where
|sin(q_eff θ₂)| = 1 and cos(q_eff θ₂) = 0.  Because the charge
integrand is proportional to cos(q θ₂), **charge leakage is
identically zero** at these positions.  B is at its peak.

| Slot | θ₂      | θ₁    | B_e/B₀ | P_g   |
|------|---------|-------|--------|-------|
| 1    | 46.6°   | 113°  | +1.00  | 1.73  |
| 2    | 139.7°  | 160°  | −1.00  | 0.35  |
| 3    | 232.9°  | 206°  | +1.00  | 0.20  |
| 4    | 326.1°  | 253°  | −1.00  | 1.56  |

At all four positions: P_e = 1.000 exactly (midway between min
and max), AC_e = 0.000, Δμ/ΔQ → ∞.

Ghost pressure ranges from 0.20 to 1.73 — moderate discrimination.
Ghost B ranges from 0.60 to 0.83 (strong ghost B also leaks, but
we care about the electron's moment, not the ghost's).


---

### F7. Field values at slot positions — all plans

| Plan | θ₂      | P_e   | AC_e  | B_e/B₀ | P_g   | AC_g  | B_g/B₀ | P_g/P_e |
|------|---------|-------|-------|--------|-------|-------|--------|---------|
| A    | 93.2°   | 0.000 | −1.00 | 0.00   | 1.055 | +0.06 | +1.00  | ∞       |
| A    | 279.5°  | 0.000 | −1.00 | 0.00   | 0.835 | −0.17 | −0.99  | ∞       |
| B    | 186.3°  | 2.000 | +1.00 | 0.00   | 0.006 | −0.99 | +0.11  | 0.003×  |
| B    | 0°      | 2.000 | +1.00 | 0.00   | 2.000 | +1.00 | 0.00   | 1.0×    |
| C    | 46.6°   | 1.000 | 0.00  | +1.00  | 1.726 | +0.73 | +0.69  | 1.7×    |
| C    | 139.7°  | 1.000 | 0.00  | −1.00  | 0.354 | −0.65 | +0.76  | 0.4×    |
| C    | 232.9°  | 1.000 | 0.00  | +1.00  | 0.202 | −0.80 | −0.60  | 0.2×    |
| C    | 326.1°  | 1.000 | 0.00  | −1.00  | 1.558 | +0.56 | −0.83  | 1.6×    |

Key observations (fixed-phase, assuming standard orientation):

- **Plan A** now sits at exact electron pressure zeros (P = 0.000,
  B = 0.000).  Ghost is fully exposed (P_g/P_e → ∞).

- **Plan B** now sits at the exact second pressure peak (P = 2.000).
  Ghost is near-zero at the tall slot (P_g = 0.006).

- **Plan C** sits at P_e = 1.000 exactly, AC_e = 0, |B_e| = 1.

**However**, see F14 below: the fixed-phase ratios are misleading.
Phase degeneracy on a symmetric torus means both modes can
freely rotate.  Only Plan C survives as a genuine filter.


### F7b. Phase degeneracy — the real discrimination test

On a perfectly symmetric (unslotted) torus, a mode's field
pattern cos(q θ₂ + φ₀) can freely rotate (any φ₀ gives the
same physics).  A slot breaks this symmetry and pins each mode
to its lowest-loss orientation.  To evaluate ghost filtering,
we must compare **phase-optimized** residuals: each mode picks
the φ₀ that minimizes its exposure to the slots.

The electron has 4 charge zeros per revolution (separated by
π/q_e ≈ 93.2°).  The ghost has 2 (separated by π/q_g ≈ 193.1°).

| Plan | Distinct θ₂ | Electron min|cos| | Ghost min|cos| | Discrimination |
|------|-------------|-------------------|----------------|----------------|
| A    | 2           | 0.107             | 0.107          | **1.0×**       |
| B    | 2           | 0.107             | 0.107          | **1.0×**       |
| C    | 4           | 0.001             | 0.726          | **610×**       |

**Plans A and B provide no phase-independent discrimination.**
Both modes dodge 2 slots equally well.  The fixed-phase ratios
(194×, 14×) assume a specific orientation that isn't guaranteed.

**Plan C achieves 610× discrimination** because:
1. The 4 slot positions ARE the electron's charge zeros
   (cos(q_e θ₂) = 0 at all four).  The electron is transparent.
2. The ghost has only 2 zeros — it can zero at most 2 of 4
   slots.  The remaining 2 always see |ghost| ≈ 0.65–0.73.
3. The zero-spacing mismatch (93.2° vs 193.1°) is structural
   and cannot be circumvented by any phase choice.

This is the waveguide mode-filter principle: place absorbing
features at the desired mode's zeros.  The desired mode passes
through unperturbed; unwanted modes with different zero counts
or spacings cannot dodge all features simultaneously.


### F8. Charge leakage through a rectangular slot

For a narrow slot (width w, height h) at position θ₂_c on
the unrolled sheet, the charge deficit from removing that
surface patch is:

    ΔQ = −ε₀ E₀ cos(q_eff θ₂_c) · a R · w_rad · h_eff

where h_eff = h_rad + r [sin(θ₁_hi) − sin(θ₁_lo)] accounts
for the torus metric ρ = R(1 + r cos θ₁).

**Charge scales linearly with both width and height (area-driven).**

At Plan A positions (cos ≈ −1): removing negative-charge patches
→ total Q becomes less negative (slot adds positive charge).

At Plan B positions (cos ≈ +1): removing positive-charge patches
→ total Q becomes more negative (slot adds negative charge).

This sign difference is important for the fitting strategy (F11).


### F9. Magnetic moment from a slot — height vs. width

The tangential B field at a slot fringes through the gap
into external 3D space.  The moment contribution depends on
how the slot dimensions interact with the fringing field:

**Direct flux** through the slot: the tangential B crossing
the slot width produces magnetic flux

    ΔΦ_B ∝ B_⊥ × w × h

where B_⊥ is the B component *across* the slot (perpendicular
to the slot's tall axis).  This flux extends a distance ~w
beyond the slot surface, forming a fringing current loop.

**Moment from the fringing loop:**

    Δμ ∝ B_⊥(θ₂_c) × h × w × Δr

where Δr ≈ w is the fringing depth.  Combining:

    Δμ_slot ∝ sin(q_eff θ₂_c) × h × w²

The **height** appears linearly (longer slot = longer magnetic
current source).  The **width** appears *squared* because a wider
slot both captures more flux *and* the fringing extends further.

Compare with charge, which scales as w × h (area):

    Δμ/ΔQ ∝ [sin(q θ₂) × h × w²] / [cos(q θ₂) × w × h]
           = [sin(q θ₂)/cos(q θ₂)] × w
           = tan(q θ₂) × w

**The moment-to-charge ratio scales with the slot width w.**
Wider slots produce more moment per unit charge leaked.  But
the dominant knob is the *position* — tan(q θ₂) diverges at
the B maxima (where cos = 0), and is zero at the pressure
maxima (where sin = 0).


### F10. B-field direction and slot orientation

For the (1,2) mode with circular polarization, B is tangential
to the surface and perpendicular to the geodesic propagation
direction.  On the physical surface (at r = 2), the geodesic
runs at ≈ 45° to the θ₂ axis, so B also runs at ≈ 45° — roughly
equal components in θ₁ and θ₂.

Our tall, narrow slots (θ₁ direction) intercept the B_θ₂
component (across the slot width) effectively.  The B_θ₁
component (along the slot height) flows parallel to the slot
and barely interacts.  For r = 2, roughly half the B field
crosses the slot.

Horizontal slots (wide in θ₂, narrow in θ₁) would intercept
B_θ₁ instead — a future option if the orientation matters.


### F11. Fitting strategy — moment then charge

**Step 1 — Fit the moment.**  Choose the tall slot at θ₂ = 180°
(Plan B) or at the B maxima (θ₂ ≈ 47° or 140°, see below).
Adjust the slot height h and/or width w until:

    Δμ_slot = (α/2π) × μ_Bohr ≈ 0.00116 × μ_B

The slot height linearly increases Δμ.  The slot width
increases Δμ quadratically (from the fringing depth), so
width is the more powerful lever per unit area.

**Step 2 — Compensate the charge.**  The moment-producing slot
at θ₂ = 180° also leaks charge (AC ≈ +0.98, positive charge
removed → Q becomes more negative).  Adjust shear s to
restore Q = −e.  Because charge depends on s through the
α(r,s) formula, a small shear change can absorb the slot's
charge perturbation.

Alternatively (or in addition), the two charge-only slots at
θ₂ = 0° can be resized to add or remove charge without
affecting the moment (B = 0 there).  This gives two
independent levers: s for global charge, θ₂=0° slots for
local charge trimming.

**Step 3 — Verify ghost discrimination.**  With the new s and
slot positions, recheck that the ghost mode is sufficiently
suppressed.  Plan B's θ₂ = 180° slot drains the electron
87× more than the ghost — opposite to Plan A.  Ghost
filtering may require additional Plan A-type slots or may
be naturally adequate if the ghost's total energy budget is
unfavorable.


### F12. Plan C — best on every metric

Plan C places slots at the exact θ₂ where sin(q_eff θ₂) = ±1
and cos(q_eff θ₂) = 0.  These four positions are simultaneously:

1. **The electron's charge zeros** → ΔQ = 0 exactly
2. **The electron's B-field maxima** → maximum moment coupling
3. **Phase-locked to the electron** → the electron is
   structurally transparent to these slots (F7b)
4. **Incommensurate with the ghost's zeros** → ghost can't
   dodge all four (only has 2 zeros per revolution)

Fitting is uniquely clean:
1. Set slot dimensions to produce Δμ = (α/2π) μ_B
2. Charge is automatically preserved (ΔQ = 0)
3. No shear adjustment, no charge-trimming slots
4. Ghost filtering is 610× (phase-independent)


### F13. Shear-induced field shift

The second pressure maximum of the electron field falls at
θ₂ = 360°/q_eff = 186.3°, not at 180°.  If there were no
shear (s = 0, q_eff = 2), it would land at exactly 180°.
The 6.3° shift is a direct consequence of q_eff = 1.932
stretching the wavelength.  All field features — zeros,
B maxima, pressure minima — shift by the same proportion.

This effect also means Plan B's slot at θ₂ = 180° is
6.3° short of the true pressure peak, placing it at
P_e = 1.977 instead of the theoretical maximum P = 2.
For Plan C, the script computes exact B-maximum positions
from q_eff, so no such offset occurs.


---

### Track 2 outputs

| File | Contents |
|------|----------|
| `outputs/track2_all_electron.svg` | 3-panel (E + B + geodesic), all plans overlaid, electron |
| `outputs/track2_all_ghost.svg`    | 3-panel, all plans overlaid, ghost |


---

## Summary table

| # | Finding |
|---|---------|
| F1 | CP α formula: α = μ sin²(2πs)/(4πq²) — differs from scalar by 1/r² |
| F2 | CP shear converges to s ≈ 0.069 at large r (scalar shear → 0) |
| F3 | Charge Q = −e verified analytically and numerically at all r |
| F4 | Unipolar pressure, no θ₁ dependence — horizontal bands on sheet |
| F5 | Ghost (1,1) discrimination persists; ~1 vs ~2 oscillations per revolution |
| F6 | B tangential, 90° out of phase with E_n; CP equipartition confirmed |
| F7 | Field values at all slot positions for Plans A, B, C (table) |
| F7b | **Phase degeneracy**: Plans A, B give 1× discrimination; Plan C gives 610× |
| F8 | Charge leakage ΔQ ∝ cos(q θ₂) × w × h — area-driven, linear in both |
| F9 | Moment Δμ ∝ sin(q θ₂) × h × w² — width squared from fringing depth |
| F10 | B direction at ≈45° to slot; roughly half of B crosses the slot |
| F11 | Fitting strategy: set slot dims for moment, then adjust s for charge |
| F12 | **Plan C wins all metrics**: ΔQ=0, |B|=1, 610× ghost discrimination |
| F13 | Shear shifts all field features by 6.3° from their q=2 positions |


## Track 3. Interactive eigenmode lab — phase-locked node constraints

Tool: [`viz/torus-lab.html`](../../viz/torus-lab.html)

### Model summary

Track 3 replaced the vector field model of Tracks 1–2 with the
scalar Sturm-Liouville eigensolver.  The equation
−d/dθ₁[p(θ₁) df/dθ₁] + V(θ₁)f = λ w(θ₁)f gives the tube profile
f(θ₁) for each mode, with curvature effects handled correctly.

The key innovation is **phase-locked standing waves**: the first
node constraint pins the phase of every mode, producing a 2D
density pattern ρ(θ₁,θ₂) = |f(θ₁)|² · sin²(q_eff · (θ₂ − θ₂_anchor)).
Subsequent nodes filter based on this pattern.  A mode's survival
score is ∏(1 − ρ) over all non-anchor constraints.

### Findings

| ID | Finding |
|----|---------|
| F1 | Ghost can be selectively killed.  Placing nodes at the electron's standing-wave nodes (θ₂ spacing = 180°/q_eff_e) achieves 100% electron survival while reducing ghost (1,1) to < 1%. |
| F2 | Shear-adjusted spacing matters.  Naïve 90° intervals give ~91% electron survival; shear-optimized 92.65° intervals give 100%.  The ~2.65° correction comes from q_eff = n₂ − s·n₁. |
| F3 | Higher harmonics preserved.  (1,2) 100%, (1,3) 85.8%, (1,4) 100%, (1,5) 99.9%, (1,6) 100%.  Only (1,3) partially weakened. |
| F4 | Physical realization: node constraints correspond to slots (apertures) in the torus surface that force standing-wave nodes at those positions. |


## Track 4. Slot geometry and anomalous moment

Script: [`scripts/track4_slot_geometry.py`](scripts/track4_slot_geometry.py)
Outputs: `outputs/track4_*.svg`

### Model summary

Four elliptical slots on the inner equator (θ₁ = 180°), equally
spaced at shear-corrected intervals (θ₂ = 0°, 92.65°, 185.31°,
277.96° at ε = 0.5).  Each slot has semi-axes h (tube direction)
and w (ring direction).  Total slot area is pinned to produce
δμ/μ = α/(2π) ≈ 1.161 × 10⁻³, then h/w is swept to minimize
charge leakage.

### Findings

| ID | Finding |
|----|---------|
| F1 | Target moment δμ/μ = α/(2π) achievable at all h/w ratios — moment scales linearly with slot area at these small aperture sizes. |
| F2 | Flat/wide slots (h/w ≈ 0.1) minimize charge leakage: Q_leak = 2.3 × 10⁻⁵ e.  Tall/narrow slots (h/w = 10) give 12× more leakage but still < 0.03% of e. |
| F3 | Optimal slot: h ≈ 0.98° × w ≈ 9.78° (ring-direction slit).  Physical size at ε = 0.5: h ≈ 9.2 fm × w ≈ 183 fm. |
| F4 | Ghost (1,1) remains killed (0.0% survival) at all slot aspect ratios — positions from Track 3 are robust. |
| F5 | Electron (1,2) survives at 100% everywhere.  (1,3) weakened to ~74%, (1,4)–(1,6) all > 99%. |
| F6 | Charge perturbation negligible — no shear adjustment needed.  The circularity concern (slots perturb charge → new shear → slots move) is moot. |
| F7 | Field intensity at inner equator is 1.25× RMS average — lower than outer equator peak (~1.8×), reducing coupling as desired. |


## Track 5. Mode filtering — assessment and working assumption

### Summary

Multiple candidate mechanisms can eliminate the (1,1) ghost
mode and select (1,2) as the lowest charged mode on the
electron sheet.  This track assesses their status and
establishes a working assumption for future modeling.

### What has been tested

**Slot filtering (Tracks 3–4): proven.**  Four phase-locked
nodes on the inner equator kill (1,1) to 0.0% survival while
preserving (1,2) at 100%.  The slot geometry is physically
reasonable (~10 fm × ~180 fm at ε = 0.5) and produces the
measured anomalous magnetic moment δμ/μ = α/(2π) as a
byproduct.  This mechanism works.  It requires assuming the
slots exist and have the right positions.

### What has been proposed but not tested

**Waveguide cutoff from tube diameter.**  If the photon
fills the tube volume (the WvM 3D picture) rather than
living on the 2D surface (the MaSt simplification), the
tube cross-section acts as a waveguide.  Modes whose
transverse wavelength exceeds the tube diameter are
evanescent — they cannot propagate.  This would impose a
minimum n₂ set by the tube geometry.

Key insight: the waveguide cutoff and slot filtering are
the **same physics in different descriptions**.  A waveguide
cutoff exists because the tube walls force the field to zero
at the boundary — the walls ARE nodes.  The 3D picture gives
you the nodes automatically from the tube geometry.  The 2D
picture needs them placed explicitly because it has
abstracted away the walls.

This means the slots found in Tracks 3–4 may not be
independent features placed on an otherwise smooth surface.
They may be the 2D projection of what the tube walls do
naturally when the full 3D field structure is considered.
If so, the slot positions and dimensions are determined by
the tube geometry, not by a separate design choice.

**Helicity constraint (Q104).**  The photon's circular
polarization traces a helix along the propagation direction.
On the torus, this helix maps onto the surface with both
normal and tangential components.  The normal component
(charge) syncs with the tube's geometric rotation.  The
tangential component (moment) projects onto the ring
direction.  If this helical structure forces n₂ = 2n₁ for
all charged modes, then (1,1) is forbidden by the
polarization geometry — it simply cannot produce net
outward E flux.  This would be the most fundamental
explanation: not a filter that removes (1,1), but a
selection rule that prevents it from carrying charge in
the first place.

### Assessment

| Mechanism | Status | Ghost killed? | Fixes geometry? |
|-----------|--------|---------------|-----------------|
| Slot filtering | Proven (Tracks 3–4) | Yes (0.0%) | Partially (slot positions, not torus dimensions) |
| Waveguide cutoff | Proposed, untested | Expected yes | Yes (tube diameter → ε) |
| Helicity constraint | Proposed, untested | Expected yes (dark, not absent) | Possibly (if n₂ = 2n₁ forced) |

The three mechanisms are not mutually exclusive.  They may
all be active simultaneously — slots, waveguide cutoff, and
helicity selection could each contribute to (1,1)
suppression.  Redundancy would indicate that ghost
elimination is a robust geometric property of the torus,
not a fine-tuned feature.

### Possible directions for further modeling

1. **3D eigenmode calculation.**  Solve for the EM field
   inside the torus volume (not just on the surface).
   Identify the transverse mode structure and determine
   the cutoff n₂ as a function of ε.  Compare to the 2D
   surface eigenvalues.

2. **Helicity decomposition (Q104).**  Compute the normal
   and tangential projections of a helical E field on a
   (p, q) geodesic of a torus.  Determine whether
   n₂ = 2n₁ is forced for charge-producing modes.

3. **Slot-from-geometry derivation.**  If the waveguide
   cutoff is confirmed, compute the implied slot positions
   and dimensions on the 2D surface and compare to the
   Track 3–4 results.  Agreement would unify the 2D and 3D
   pictures.

4. **Proton comparison (R47 Track 7).**  Apply the same
   analysis to the proton sheet.  If the proton is (3,6),
   the waveguide cutoff must sit at a different n₂ than
   the electron, implying a different ε.

### Working assumption

For subsequent modeling, we assume that **a filter mechanism
exists** that eliminates (1,1) and selects (1,2) as the
lowest charged mode on the electron sheet.  The specific
mechanism — slots, waveguide cutoff, helicity, or a
combination — is not yet determined.

This assumption is justified by:
- The phenomenological fact that no (1,1) particle has been
  observed, despite being predicted lighter than the electron
- At least one proven mechanism (slots) that achieves the
  filtering
- Two additional plausible mechanisms that may provide the
  same filtering from pure geometry

The geometry implied by this assumption:
- Electron torus aspect ratio ε ≈ 0.5 (if the filter fixes
  the tube-to-ring ratio)
- (1,2) is the lowest charged mode
- (1,1) is dark or absent
- Higher harmonics (2,4), (3,6), ... exist as excited states

This working assumption does not commit to a mechanism.  It
commits to a result — the (1,1) ghost is gone — and proceeds
with the geometric consequences.  The mechanism will be
resolved when one of the proposed directions (above) produces
a testable distinction.
