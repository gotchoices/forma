# R60 Metric Terms — variables and definitions

Brief reference for the 11D metric parameterization.  The full
entry-by-entry grid (current values, role, constraint status) is
in [metric-terms.csv](metric-terms.csv).

## Index ordering

| Index | Symbol | Kind | Scale |
|------:|:-------|:-----|:------|
| 0 | ℵ | compact, sub-Planck | smallest (GRID edge) |
| 1 | p_t | compact (proton tube) | ~fm |
| 2 | p_r | compact (proton ring) | ~fm |
| 3 | e_t | compact (electron tube) | ~pm |
| 4 | e_r | compact (electron ring) | ~pm |
| 5 | ν_t | compact (neutrino tube) | ~μm to mm |
| 6 | ν_r | compact (neutrino ring) | ~μm to mm |
| 7 | S_x | extended (space) | macroscopic |
| 8 | S_y | extended (space) | macroscopic |
| 9 | S_z | extended (space) | macroscopic |
| 10 | t | extended (time, Lorentzian) | macroscopic |

The 7-dim **Material** block spans indices 0–6 (ℵ + 6 Ma).
The 4-dim **Spacetime** block spans indices 7–10 (3 S + 1 t).
Within each sheet, **tube index comes before ring index** to
match the MaSt mode notation `(n_tube, n_ring)`.

## Per-sheet metric block (dimensionless)

Each sheet x ∈ {e, p, ν} is a 2×2 block in the Ma subspace:

    G̃_sheet = k_x · [[1, s_x · ε_x], [s_x · ε_x, 1 + (s_x · ε_x)²]]

- **ε_x** — aspect ratio, ratio of tube to ring circumference
- **s_x** — in-sheet shear, the (tube, ring) off-diagonal
- **k_x** — per-sheet diagonal scale (R60 addition to R59 F59's single global k)

Mode energy on a sheet (model-E formula):
`E_mode = (2π ℏc / L_ring) · √((n_t/ε)² + (n_r − s·n_t)²)`.

## α-architecture coefficients

| Symbol | Between | Current value | Role |
|:-------|:--------|:--------------|:-----|
| g_aa | ℵ ↔ ℵ (diagonal) | 1 | ℵ self-scale |
| σ_ta_x | Ma_tube_x ↔ ℵ | sign_x · √α | tube's α channel; signs (+, −, +) for (e, p, ν) |
| σ_ra_x | Ma_ring_x ↔ ℵ | **(s_x · ε_x) · σ_ta_x** (derived, Track 7) | cancels shear-induced ring-to-t leakage, restoring mode-independent α within a sheet |
| σ_at | ℵ ↔ t | 4πα | ℵ delivers coupling to time |

**Derived rule** (Track 7+7b): `σ_ra_x = (s·ε)_x · σ_ta_x`.  Not
a free knob — pinned by the geometry.  When s_x = 0 this entry
is zero (shearless sheet needs no cancellation).

## α extraction formula

`Q(n_11) = (n_Ma · G⁻¹[Ma, t]) · (−G⁻¹[t, t])`, then
`α_Coulomb = Q² / (4π)`.  On the ring↔ℵ-augmented metric, Q is
mode-independent up to the `n_t` factor: for any mode with
`|n_tube| = 1` on a sheet with architectural σ_ta coupling,
`Q = σ_ta · n_t` (modulo signature and signs).

## Signature condition

The 11D metric must have exactly **one negative eigenvalue** (the
t direction) for the full Lorentzian signature to hold.  Bounds
on the in-sheet shear product s·ε (empirical, for the R59 F59
architecture at fixed σ_ta = √α, σ_at = 4πα, g_aa = 1):

- Single-sheet active: `(s·ε)² ≤ 9/2` (exact — see Track 2 F7)
- Two-sheet active: `(s·ε_1)² + (s·ε_2)² ≤ 7/2` (Track 4 F14)
- Three-sheet predicted: `Σ (s·ε_x)² ≤ 5/2` (not yet verified)
  — each active tube costs one unit of the 9/2 budget.

## Length scales

| Sheet | L_ring (fm) at Track 7b baseline | Physical scale |
|:------|---:|:---|
| Proton | 19.28 | ~fm |
| Electron | 25,035 | ~2.5 × 10⁻¹¹ m (Compton range) |
| Neutrino | 1.96 × 10¹¹ | ~0.2 mm |
| ℵ | (not directly fit) | sub-Planck, exact scale open |

## α-decoupling locus (Track 5 F22)

For a single-sheet mode (n_t, n_r), the α extraction Q = 0 iff

    n_r / n_t = s·ε + 1/(s·ε)

i.e. `s·ε ∈ {(n_r ± √(n_r² − 4n_t²)) / (2n_t)}` (real roots iff
n_r² ≥ 4n_t²).  Practical rule:

- (1, 1) mode: never decouples (ν₁, ν₂ are α-safe everywhere)
- (1, 2) mode: decouples at s·ε = 1 (electron, ν₃)
- (1, 3) mode: decouples at s·ε ≈ 0.382 or 2.618 (proton)

This locus is *independent of all α-architecture knobs* (k, σ_ta,
σ_at, g_aa).  Adding ring↔ℵ entries (Track 7) does not remove the
locus — at the locus the mode has zero α regardless, and this
persists under the augmentation.  **The locus is a structural
feature of the mode itself, not of the metric we put around it.**

## Reserved zeros (candidates for future activation)

The 11×11 symmetric metric has 66 independent entries.  We use
~21 of them (11 diagonals + 10 off-diagonals).  The rest are
zero, several intentionally and several just unexplored:

- `Ma_ring_x ↔ S_*` (9 entries): zero by default (see Track 3 F40
  analog in R59; frame-dragging / rotation on spatial directions
  not expected).  Not tested in R60.
- `Ma_x ↔ Ma_y` cross-sheet (12 entries): two used in R54
  (σ₄₅, σ₄₆ for the neutron region), the rest zero.  Candidates
  for compound-mode fine-tuning (Track 8).
- `S_x ↔ t` (3 entries): zero by Minkowski flatness in R60's
  static picture.
- `ℵ ↔ S_*` (3 entries): R55 explored these; R59 replaced them
  with ℵ ↔ t.  Currently zero; could be revived.

See [metric-terms.csv](metric-terms.csv) for the full entry-by-entry grid.
