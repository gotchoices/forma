# Toroid Geometry

What effective geometry in the Williamson–van der Mark (WvM) electron
model reproduces the measured electron charge q = e?

## Background

The predecessor study (`../toroid-series/`) attempted to correct WvM's
~9% charge deficit via a geometric series of nested sub-tori. That study
blocked when geometric sensitivity analysis and a toroidal cavity mode
calculation revealed that the deficit is not a robust physical number —
it depends entirely on WvM's choice of a spherical cavity of diameter λ.

This study investigates the geometry itself: why does WvM's sphere work,
what does the continuum from torus to sphere look like, and can we
identify the physically correct effective volume?

## Key Questions

1. Why does WvM's sphere of diameter λ give q ≈ 0.91e, while an actual
   toroidal cavity gives q = 14–128× e?
2. Is the "rotation horizon" at r = λ/2 the physically correct boundary
   for the field?
3. A degenerate torus (tube radius a ≫ major radius R) bridges the gap
   between torus and sphere. At a/R ≈ 6.60, q = e exactly. Is there a
   self-consistency condition that selects this value?
4. Can the field falloff from the geodesic orbit be modeled to determine
   the actual effective volume?

## Scripts

All scripts require the project virtual environment (`.venv` at the
repo root) and the shared library (`../lib/`). Run from the repo root:

    source .venv/bin/activate
    python studies/toroid-geometry/scripts/01_wvm_sensitivity.py

| Script | Findings | Description |
|--------|----------|-------------|
| `01_wvm_sensitivity.py` | F1 | Sweeps cavity shape (sphere vs torus), charge radius, and E-B energy partition. Shows the 9% deficit is within WvM's geometric uncertainty (~5% shift in r_c eliminates it). |
| `02_toroidal_modes.py` | F2 | Solves the Helmholtz equation for the lowest EM mode of a hard-walled toroidal cavity using finite differences and `scipy.sparse.linalg.eigsh`. Shows q = 14–128× e for all tube radii. Requires `scipy` and `numpy`. |

## Visualizer

`torus_viz.html` — Interactive 3D visualization of the torus-to-sphere
continuum. Open directly in any modern browser (no server required):

    open studies/toroid-geometry/torus_viz.html

**Controls:**
- **a/R slider** — Tube-to-ring radius ratio (0.05 to 12). The key
  parameter: watch the torus degenerate from a thin ring through
  the horn torus (a/R = 1) into a sphere-like blob.
- **Preset buttons** — Jump to notable values:
  Ring (0.5), Horn (1.0), Horizon (5.28, outer edge = rotation
  horizon), q = e (6.60), WvM sphere (7.26, same volume as WvM's
  sphere).
- **Opacity slider** — Surface transparency (0 = invisible, 1 = solid).
- **Toggles:**
  - *Wireframe* — overlay showing the mesh structure
  - *Geodesic* — the (2,1) spin-½ double-loop path (orange tube)
  - *Photon* — animated yellow dot tracing the geodesic at constant speed
  - *Rotation horizon* — wireframe sphere at r = λ/2 = 2πR
  - *Symmetry axis* — the torus axis of rotation
  - *Auto-fit scale* — keeps the outer extent at constant screen size
    so internal structure is visible without zooming
- **Mouse:** drag to rotate, scroll to zoom, right-drag to pan.

**Info panel** (upper right) shows torus type (Ring/Horn/Spindle),
outer edge in units of λ, volume ratio V_torus/V_sphere, and the
predicted q/e under the uniform-field approximation.

## Other Files

| File | Contents |
|------|----------|
| `theory.md` | Framework: topology vs geometry, rotation horizon, degenerate torus, propositions P1–P4 |
| `findings.md` | Results F1–F5 and open questions |
| `STATUS.md` | Task checklist |
