# R41. Dynamic torus model — Findings

**Date:** 2026-03-01
**Status:** Active


## Track 1: Design spec update

Updated `lib/ma-model.md` with Feature 10 (Dynamic model).

Key design decisions:

1. **Single class, flag-gated.**  `Ma(..., dynamic=True)` extends
   the existing class rather than creating a separate `DynamicMa`.
   The dynamic model IS the static model + perturbative corrections;
   a separate class would create unnecessary duplication.

2. **Mode-dependent cross-section.**  The wall shape r(θ₁)/a depends
   on the specific mode's winding numbers (n_tube, n_ring) and the
   sheet's aspect ratio r.  The dominant harmonic is always k=2
   (elliptical, from the cos 2θ₁ torus curvature), but the amplitude
   varies:
   - Ring-dominated modes (high n₂/n₁): larger ellipticity
   - Tube-dominated modes (high n₁/n₂): nearly circular
   - Ring-only modes (n_tube = 0): no deformation (no coupling)

3. **Per-sheet corrections for cross-sheet modes.**  A mode like
   the neutron (0, −2, 1, 0, 0, 2) has tube winding on the neutrino
   sheet only.  The dynamic correction is weighted by E² fractions
   from energy_decomp():
     δE/E = Σ_S  (E²_S / E²_total) × ε_{2|n_tube,S|} / 2

4. **Harmonic caching.**  pressure_harmonics(n_tube, n_ring, r)
   depends only on these three arguments.  Results are cached in
   a dict keyed by this triple.  For a 14,000-mode scan, most
   modes share sheets (same r), giving high cache hit rate.

5. **Jacobian extension.**  The dynamic correction depends on r
   through the pressure harmonics, so ∂E_dynamic/∂r includes
   a new term E_static × ∂δ/∂r.  The finite-difference Jacobian
   in fit() handles this automatically; the analytical Jacobian
   needs the chain rule extended.

6. **Self-consistency with dynamic energies.**  When both
   dynamic=True and self_consistent=True, the L-rescaling loop
   targets dynamic m_e and m_p, not static values.

Spec location: `lib/ma-model.md` §Feature 10, §Phase 6.
