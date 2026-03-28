# lib/ STATUS

## Bugs to fix in existing code

### ma.py

- [ ] `mode_energy` silently clamps negative E² to zero (`max(E2, 0.0)` line 361) — masks metric bugs that should raise an error
- [ ] Cross-shear loop in `build_scaled_metric` (lines 310-314) overwrites G̃ entries without asserting they belong to a cross-block — safe today because blocks don't overlap, but fragile

### ma_solver.py

- [ ] `find_modes` at end of `multi_target_optimize` (lines 499-507) rebuilds the metric and re-scans for each target — the optimal-point metric is already available
- [ ] `self_consistent_metric` returns no convergence diagnostics — no final mass errors or iteration trajectory, hard to debug slow convergence
- [ ] `_best_match_error` uses greedy assignment (not optimal Hungarian); fine for small target lists but will break with >5 targets

### series.py

- [x] `geometric_sum(1.0, n)` returned NaN — fixed (r = 1 guard)
- [x] `infinite_sum(1.0)` raised ZeroDivisionError — fixed (returns inf)

---

## Documentation fixes done

- [x] ma.py module docstring: "odd index: 0, 2, 4" → "even index: 0, 2, 4" (tube/ring label)
- [x] ma.py `mode_charge` docstring: replaced stale WvM parity description with KK formula `Q = −n₁ + n₅`
- [x] ma.py `build_scaled_metric` docstring: σ_ep ≈ 0.038 → σ_ep ≈ −0.0906 (R27 value)
- [x] ma.py module docstring: σ_ep ≈ 0.038 → σ_ep ≈ −0.0906
- [x] ma.py `compute_scales`: added guard for `solve_shear_for_alpha` returning None

---

## No unit tests

- [ ] No test file exists for any lib module
- [ ] Regression values not pinned (electron, proton, neutron energies at standard geometry)
- [ ] The ma-model.md spec describes a testing strategy (regression, known particles, self-consistency, roundtrip, speed) — implement it as `test_ma.py` before or alongside the new module

---

## Performance

- [ ] `scan_modes` is O((2n+1)^6) brute force — 1.8M at n_max=5, 350M at n_max=10
- [ ] `multi_target_optimize` calls the brute-force scan ~1000× via differential_evolution — effectively O(10^12) at n_max=5
- [ ] No CPT/symmetry reduction (n → −n gives same energy, opposite charge) — enumeration could be halved
- [ ] Neutrino scale hierarchy (L_ν/L_e ~ 10^8) makes the energy ellipsoid extremely elongated — Fincke-Pohst enumeration (planned in ma-model.md) would visit only modes inside the ellipsoid

---

## ma-model.md design — review comments

The spec is well-structured (8 features, 5 phases).  Items below are design concerns to resolve before or during implementation.

- [ ] **Energy decomposition (Feature 3):** The blocks of G̃⁻¹ are NOT the inverses of the blocks of G̃ — Schur complements mix all sheets.  "97% proton-sheet" is a statement about the inverse-metric partition, not about physical sheet contributions.  Caveat the interpretation or derive a decomposition of G̃ itself.
- [ ] **Jacobian chain (Feature 4):** ∂E/∂r requires implicit differentiation through `solve_shear_for_alpha`: ∂s/∂r = −(∂α/∂r)/(∂α/∂s).  Both partials are analytical but the spec doesn't document this chain.  Similarly ∂L/∂r involves ∂s/∂r through the Compton constraint.
- [ ] **Self-consistency + fit (Feature 5):** When self_consistent=True, L depends on σ through the fixed-point iteration.  The LM solver needs the *total* derivative dE/dσ (including indirect path through L), not just ∂E/∂σ at fixed L.
- [ ] **Mode provenance:** The Mode namedtuple stores (n, E, Q, spin) but not which geometry produced it.  Collecting modes from different Ma instances during a sweep loses provenance.  Consider an optional geometry hash.
- [ ] **Fincke-Pohst + neutrino hierarchy (Feature 2):** L_ν directions extend to n ~ 10^8 while e/p directions are O(1).  Consider a two-stage approach: enumerate heavy directions at small n_max, then analytically bound neutrino quantum numbers per heavy assignment.
- [ ] **CPT reduction:** n → −n has identical energy and opposite charge.  Halve the enumeration; use as sanity check that mode_count by charge is symmetric.
- [ ] **Spectrum caching:** If Ma is immutable and modes() is expensive, cache the result on first call.  Spec mentions caching for the metric but not the spectrum.
- [ ] **Phase 0 — write tests first:** Pin regression values against current ma.py before any new code.  Every subsequent phase validates against these.
