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

## ma_model.py

Immutable `Ma` class with static flat-torus model and dynamic
α-impedance model.  No dependency on legacy code.

### Static model (complete)

- [x] `Ma(r_e, r_nu, r_p, sigma_ep=, ...)` — construction from aspect ratios + shears
- [x] `energy()`, `energy_static()` — mode energy (MeV)
- [x] `charge()`, `spin()`, `spin_label()` — KK charge and tube-winding spin
- [x] `energy_decomp()` — E² decomposition by sheet and cross-coupling
- [x] `jacobian()` — analytical ∂E/∂params (r, σ) with implicit differentiation through α
- [x] `sensitivity()` — human-readable Jacobian report
- [x] `scan_modes()` — brute-force hypercube scan with charge/spin/energy filters
- [x] `fit()` — inverse solver (Levenberg-Marquardt with numerical Jacobian); given target masses + mode assignments, finds geometry parameters.  Reports covariance and null space.
- [x] Self-consistent iteration (`self_consistent=True`)
- [x] `with_params()` — immutable parameter sweep
- [x] `to_dict()` / `from_dict()` — serialization
- [x] `from_legacy()` / `to_legacy()` — interop with legacy ma.py
- [x] `summary()` — human-readable printout

### Dynamic model (complete, from R40)

The torus wall is the (1−α) energy contour of the mode.  Inside:
136/137 of the energy (confined).  Outside: 1/137 (the external
EM field).  The wall shape responds to the mode's radiation
pressure, balanced by elastic restoring force (1/k² per harmonic).

Two solver modes:

- **`dynamic='full'`** (or `True`): Iterative force-balance.
  Computes pressure on the current shape, derives the equilibrium
  deformation, updates the shape, and repeats until converged.
  Convergence is geometric with ratio ~α ≈ 0.007.  This is the
  self-consistent solve — no static baseline assumed.

- **`dynamic='shortcut'`**: One-shot perturbation on the circular
  cross-section.  Equivalent to iteration 0 of the full solve.
  ~0.3% less accurate than full, ~2× faster.

Both produce identical results to within 0.3% of the correction
(which is itself O(α²) ≈ 5×10⁻⁵ of the total energy).

Implemented:

- [x] `pressure_harmonics(n_tube, n_ring, r)` — 3D geodesic curvature → Fourier decomposition of radiation pressure.  Cached by (|n_tube|, |n_ring|, r).
- [x] `wall_shape(n_tube, n_ring, r)` — cross-section r(θ₁)/a from pressure harmonics
- [x] `dynamic_correction(n)` — per-sheet eigenvalue shifts weighted by E² fractions
- [x] `filter_factor(n)` — low-pass suppression relative to (1,2) fundamental
- [x] `energy()` with `dynamic='full'` or `'shortcut'` — force-balance energy
- [x] `energy_static()` — always returns flat-torus energy
- [x] `fit()` with `dynamic=True` — reverse solver using dynamic energies
- [x] `scan_modes()` respects dynamic flag; Mode namedtuple includes delta_E_MeV
- [x] `to_dict()` / `from_dict()` preserve dynamic flag
- [x] `summary()` reports dynamic corrections when enabled

### Remaining stubs

- [ ] `_fincke_pohst_enumerate()` — fast ellipsoid lattice enumeration (ma_model.md §Feature 2)
- [ ] `modes()` — Fincke-Pohst scan with CPT reduction
- [ ] `spectrum()`, `mode_count()`, `nearest()` — rich spectrum queries (§Feature 7)

---

## embedded.py — complete

Embedded torus geometry and near-field calculations.  No dependency
on legacy code — only lib/constants.py.

- [x] `EmbeddedSheet` — immutable, three constructors, geometry properties
- [x] `geodesic()`, `charge_segments()`, `charge_density()` — with optional custom weights
- [x] `monopole()`, `dipole()`, `quadrupole()`, `multipoles(l_max)` — spherical harmonic expansion
- [x] `field_at()`, `field_at_points()`, `potential_at()` — Coulomb with configurable softening
- [x] `field_energy()` — self-energy with required softening
- [x] `interaction_energy()` — pairwise sum, vectorized
- [x] `interaction_sweep()` — (d, Δφ) sweep with phase-reuse optimization
- [x] `interaction_force()` — finite-difference force along any axis
- [x] `near_field_correction()` — phase-averaged and anti-phase extraction

---

## Test summary

| Suite | Tests | Covers |
|-------|-------|--------|
| test_lib.py | 52 | Legacy: constants, series, wvm, ma.py, ma_solver.py |
| test_ma_model.py | 125 | Ma class: static, dynamic, decomp, Jacobian, fit, cross-validation, R40 validation |
| test_embedded.py | 39 | EmbeddedSheet, fields, sweeps, charge density |
| **Total** | **216** | |
