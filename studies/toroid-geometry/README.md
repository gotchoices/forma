# Toroid Geometry  *(concluded)*

What effective geometry in the Williamson–van der Mark (WvM) electron
model reproduces the measured electron charge q = e?

## Result

**a/R = 1/√(πα) ≈ 6.60** — a degenerate torus whose tube radius is
1/√(πα) times the orbital radius reproduces q = e exactly.

The photon orbits at R = λ/(4π), but its field extends outward to
~0.6λ, filling a nearly spherical volume bounded by the rotation
horizon (r = λ/2). The topology (double-loop geodesic) gives spin ½
exactly; the extended field geometry gives charge; the analytical
ratio ties the geometry directly to the fine-structure constant α.

## Key Findings

1. WvM's sphere is the rotation horizon — a physically motivated
   boundary, not arbitrary (F1, F3).
2. A toroidal cavity (hard walls) gives q = 14–128× e; the sphere
   is what makes q ≈ e (F2).
3. The torus-to-sphere continuum is smooth; a/R ≈ 6.60 gives q = e (F4).
4. The (2,1) orbit produces ~2.5% quadrupole anisotropy (F5).
5. a/R = 1/√(πα) exactly — clean analytical form (F6).

## Spawned Questions

Whether a/R = 1/√(πα) can be derived independently (not just by
demanding q = e) remains open. See `findings.md` conclusion and
`../README.md` future study ideas.

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
