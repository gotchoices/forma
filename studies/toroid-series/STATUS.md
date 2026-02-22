# Toroid Series — Status

## Completed

- [x] Reproduce WvM charge baseline — `01_wvm_baseline.py` → F1
- [x] Geometric series scan — `02_series_scan.py` → F2
- [x] Dimensional scaling analysis — `03_scaling_dimensions.py` → F3
- [x] Dialog claim verification — `04_dialog_claims.py` → F4
- [x] Extract shared library — `studies/lib/`
- [x] Unconstrained series decomposition — `05_free_series.py` → F5

- [x] WvM geometric sensitivity analysis — `06_wvm_sensitivity.py` → F6

- [x] Toroidal cavity EM modes (Maxwell's equations) — `07_toroidal_modes.py` → F7

## In Progress

(none)

## Planned

- [ ] QED expansion parameters (α/π, α/(2π)) with rational coefficients
- [ ] Mixed-scale hybrid decomposition

## Reassessment (after F7 + F8)

F7 showed the toroidal cavity gives q = 14–128× e (not 0.91e), but
F8 clarifies this: WvM's sphere is the *rotation horizon* — a
physically motivated boundary, not an arbitrary choice. The photon
orbits at R = λ/(4π), but its field fills the horizon sphere (r = λ/2)
because a charge circulating at c produces a nearly spherically
symmetric time-averaged field.

F8 also shows a smooth continuum: a "degenerate torus" with tube
radius a ≈ 6.6R reproduces q = e exactly. The 9% deficit may
reflect non-uniform field density within the horizon sphere, which
could bring the series hypothesis back into play — now as a
correction for field non-uniformity rather than literal sub-tori.

**Next steps** should focus on modeling the field falloff from the
toroidal orbit and determining whether the non-uniformity naturally
produces a ~10% correction.
