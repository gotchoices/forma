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

## Files

| File | Contents |
|------|----------|
| `theory.md` | Framework: topology vs geometry, rotation horizon, degenerate torus |
| `findings.md` | Results F1–F4 and open questions |
| `STATUS.md` | Task checklist |
| `scripts/01–02` | Sensitivity analysis, toroidal cavity modes |
| `torus_viz.html` | Interactive 3D visualization (Three.js) |
