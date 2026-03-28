# lib/ STATUS

Legacy code (ma.py, ma_solver.py, wvm.py, series.py) is frozen for
backward compatibility — existing studies import it as-is.  New
capabilities go into new modules (ma_model.py, embedded.py) which
can re-export legacy interfaces where useful.

---

## Bugs to fix in legacy code

These are correctness issues that should be patched in place since
they affect any script that hits them, old or new.

- [ ] **ma.py:361** — `mode_energy` silently clamps negative E² to zero (`max(E2, 0.0)`).  Should raise `ValueError` so metric bugs don't hide as zero-energy modes.
- [ ] **ma_solver.py:499-507** — `multi_target_optimize` rebuilds the metric and re-scans for each target at the end, even though the optimal-point metric is already in scope.  Wasted work; pass through the existing Gti/L instead.

### Done

- [x] series.py — `geometric_sum(1.0, n)` returned NaN; `infinite_sum(1.0)` crashed
- [x] ma.py — module docstring: tube/ring index labels were swapped
- [x] ma.py — `mode_charge` docstring described stale WvM parity rule; replaced with KK formula
- [x] ma.py — `build_scaled_metric` and module docstring: σ_ep updated from 0.038 to −0.0906
- [x] ma.py — `compute_scales` now raises `ValueError` when `solve_shear_for_alpha` returns None

---

## Unit tests

- [ ] Create `test_lib.py` — pin regression values for the standard geometry (r_e=6.6, r_ν=5.0, r_p=8.906, σ_ep=−0.0906) so that new modules can be validated against current outputs.  Use `unittest` (no pytest in venv).  Run with `python -m unittest lib.test_lib` from `studies/`.

---

## New modules

### ma_model.py — next-generation flat-torus engine

See [ma-model.md](ma-model.md) for the full spec.  Key design points:

- Stateful immutable `Ma` class with cached metric, Cholesky, inverse
- Fincke-Pohst lattice enumeration (replaces brute-force scan)
- Energy decomposition by sheet and cross-coupling
- Analytical Jacobian (∂E/∂params)
- Inverse solver (masses → geometry via Levenberg-Marquardt)
- Compatibility layer: `Ma.from_legacy(Gti, L)` and `m.to_legacy()` so old and new code interoperate

Design concerns to resolve during implementation:

- [ ] Energy decomposition uses blocks of G̃⁻¹, not G̃ — Schur complements mix sheets; caveat interpretation
- [ ] Jacobian chain: ∂E/∂r requires implicit differentiation through solve_shear_for_alpha
- [ ] Self-consistent fit: total derivative dE/dσ must include indirect path through L
- [ ] Fincke-Pohst + neutrino hierarchy: consider two-stage enumeration (heavy dims first, then bound neutrino dims analytically)
- [ ] CPT reduction (n → −n): halve enumeration, use symmetry as sanity check
- [ ] Spectrum caching on the immutable object
- [ ] Write tests (Phase 0) before new code — pin regression values first

### embedded.py — embedded torus near-field engine

See [embedded.md](embedded.md) for the full spec.  Computes how Ma modes
project into 3D: charge distributions, E-fields, multipoles, interaction
energies.  Primary consumer: R39.
