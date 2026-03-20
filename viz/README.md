# Visualizations

Interactive browser-based tools for exploring the geometry of the photon-knot
electron model. Each file is self-contained — open directly in any modern
browser, no server required.

## Tools

| File | Study | Description |
|------|-------|-------------|
| [`dual-torus.html`](dual-torus.html) | R3 | Side-by-side 3D torus and 2D flat rectangle with a synchronized photon moving along a (1,2) geodesic. Shows that the winding knot is a straight line on the flat T². |
| [`torus-explorer.html`](torus-explorer.html) | S2 | Interactive 3D torus with a/R slider. Watch the torus morph from a thin ring through the horn torus (a/R=1) to a sphere-like blob. Presets jump to notable values including the WvM charge-matching ratio. |
| [`multi-winding.html`](multi-winding.html) | R8 | Multi-winding electron geometry. Visualizes the compact torus with many-orbit photon paths and the relationship between winding number, torus size, and the Compton scale. |
| [`geodesic-curvature.html`](geodesic-curvature.html) | GR | Geodesic curvature around a spherical or toroidal Compton-zone boundary. 3D spatial mode shows intrinsic curvature of a Cartesian grid (Schwarzschild for sphere, Brill-Lindquist multi-source for torus); 2D+T mode shows worldlines tilting toward the mass. Toggle between geodesics and field lines, sphere and torus zone shapes. |
| [`shear-torus.html`](shear-torus.html) | R19 | Shear deformation on the flat T². Ring lines twist into helices as shear increases, showing how the lattice vectors tilt from orthogonal. Geodesic path follows q_eff = m − ns under shear. Presets for the α-matching shear s ≈ 0.157. |

## Shared code

`totu-viz.css` and `totu-viz.js` provide the common dark-theme stylesheet and
Three.js utilities (scene setup, torus geometry, photon, materials).
New visualizers import these modules; existing visualizers will be migrated
incrementally. See [`STATUS.md`](STATUS.md) for the refactor plan.

## Launch

Open the browser index for point-and-click access:

    open viz/index.html

Or open any tool directly:

    open viz/dual-torus.html
    open viz/torus-explorer.html
    open viz/multi-winding.html
