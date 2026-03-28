# lib/ STATUS

Legacy code (ma.py, ma_solver.py, wvm.py, series.py) is frozen for
backward compatibility — existing studies import it as-is.  New
capabilities go into new modules (ma_model.py, embedded.py) which
re-export legacy interfaces where useful.

Run all tests from `studies/`:

    python -m unittest lib.test_lib lib.test_ma_model lib.test_embedded

---

## Legacy code — bugs fixed, now frozen

- [x] series.py — `geometric_sum(1.0, n)` returned NaN; `infinite_sum(1.0)` crashed
- [x] ma.py — module docstring: tube/ring index labels were swapped
- [x] ma.py — `mode_charge` docstring described stale WvM parity rule; replaced with KK formula
- [x] ma.py — `build_scaled_metric` and module docstring: σ_ep updated from 0.038 to −0.0906
- [x] ma.py — `compute_scales` now raises `ValueError` when `solve_shear_for_alpha` returns None
- [x] ma.py — `mode_energy` silently clamped negative E² to zero; now raises `ValueError`
- [x] ma_solver.py — `multi_target_optimize` rebuilt the metric per target at the end; now reuses the already-computed Gti/L

---

## ma_model.py — Phase 1 complete

Replaces all ma.py + ma_solver.py functionality with an immutable
stateful `Ma` class.  No dependency on legacy ma.py — all physics
reimplemented from first principles, validated by cross-comparison.

**Implemented:**
- [x] `Ma` class with construction from aspect ratios + shears
- [x] `energy()`, `charge()`, `spin()`, `spin_label()` — static where possible
- [x] `scan_modes()` — brute-force hypercube scan with charge/spin filters
- [x] Self-consistent iteration (`self_consistent=True`)
- [x] `with_params()` — immutable parameter updates
- [x] `to_dict()` / `from_dict()` — serialization
- [x] `from_legacy()` / `to_legacy()` — interop with legacy ma.py
- [x] `summary()` — human-readable printout
- [x] Guard rails: positive-definite check at construction, clear ValueError messages
- [x] 47 regression tests (`test_ma_model.py`) including cross-validation against legacy

**Phase 2 stubs (documented, raise NotImplementedError):**
- [ ] `_fincke_pohst_enumerate()` — fast ellipsoid lattice enumeration (see ma-model.md §Feature 2)
- [ ] `modes()` — Fincke-Pohst scan with CPT reduction (n → −n symmetry)
- [ ] `energy_decomp()` — sheet/cross-coupling decomposition of E² (§Feature 3; caveat: blocks of G̃⁻¹ mix sheets via Schur complement)
- [ ] `jacobian()` — analytical ∂E/∂params (§Feature 4; needs implicit diff through solve_shear_for_alpha)
- [ ] `sensitivity()` — human-readable Jacobian report (§Feature 6)
- [ ] `fit()` — inverse solver, masses → geometry via LM (§Feature 5; self-consistent path complicates total derivative)
- [ ] `spectrum()`, `mode_count()`, `nearest()` — rich spectrum queries (§Feature 7)

---

## embedded.py — Phases 1-3 complete

Embedded torus geometry and near-field calculations.  No dependency
on legacy ma.py — only lib/constants.py.

**Implemented:**
- [x] `EmbeddedSheet` class — immutable, three constructors, geometry properties
- [x] `geodesic()`, `charge_segments()` — with optional custom weights
- [x] `monopole()`, `dipole()`, `quadrupole()`, `multipoles(l_max)` — full spherical harmonic expansion
- [x] `field_at()`, `field_at_points()`, `potential_at()` — Coulomb with configurable softening
- [x] `field_energy()` — self-energy with required softening
- [x] `interaction_energy()` — pairwise sum, vectorized
- [x] `interaction_sweep()` — (d, Δφ) sweep with phase-reuse trig optimization
- [x] `interaction_force()` — finite-difference force along any axis
- [x] `near_field_correction()` — phase-averaged and anti-phase extraction
- [x] 36 regression tests (`test_embedded.py`)

---

## Test summary

| Suite | Tests | Covers |
|-------|-------|--------|
| test_lib.py | 52 | Legacy: constants, series, wvm, ma.py, ma_solver.py |
| test_ma_model.py | 47 | New: Ma class, cross-validation vs legacy |
| test_embedded.py | 36 | New: EmbeddedSheet, fields, sweeps |
| **Total** | **135** | |
