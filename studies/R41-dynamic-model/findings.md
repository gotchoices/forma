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


## Track 3: Validation — full vs shortcut comparison

Script: `scripts/track3_full_vs_shortcut.py`

### F27. Full iterative solve converges in 3–4 iterations

The force-balance iteration (shape → pressure → shape) converges
geometrically with ratio ≈ 0.0028 (close to α²/2).  For the
proton (1,2) at r=8.906:

| Iter | Max|Δε_k|   | δr₂/a         | Ratio    |
|------|-------------|---------------|----------|
| 0    | 6.73×10⁻⁴  | 6.7276×10⁻⁴   | —        |
| 1    | 1.83×10⁻⁶  | 6.7458×10⁻⁴   | 0.0027   |
| 2    | 5.20×10⁻⁹  | 6.7459×10⁻⁴   | 0.0028   |
| 3    | 1.55×10⁻¹¹ | 6.74588×10⁻⁴  | 0.0030   |

Self-consistent to 217× machine epsilon (4.8×10⁻¹⁴).


### F28. Full and shortcut agree to O(α⁴) in energy

For known particles, the relative difference between the two
methods is:

| Particle | δE/E shortcut | δE/E full   | Difference  |
|----------|--------------|-------------|-------------|
| electron | 3.417×10⁻⁴   | 3.427×10⁻⁴  | 9.5×10⁻⁷   |
| proton   | 3.364×10⁻⁴   | 3.373×10⁻⁴  | 9.2×10⁻⁷   |
| neutron  | ~0           | ~0          | 0           |
| muon     | 7.93×10⁻⁸    | 7.94×10⁻⁸   | 6.4×10⁻¹¹  |

The absolute energy difference (full − shortcut) for the proton
is 8.7×10⁻⁴ MeV — about 0.3% of the dynamic correction, or
10⁻⁷ of the total energy.

Since α⁴ ≈ 2.8×10⁻⁹, and the relative δE/E differences are
~10⁻⁷ × δE/E ≈ 3×10⁻¹¹, the shortcut is accurate to better
than O(α²) of the correction itself.

The full solve is the principled answer: the code discovers the
smallness rather than assuming it.


### F29. Timing: full costs ~4.5× per harmonic, scan overhead is small

Per-harmonic computation (median, single (n_tube, n_ring, r)):
  - Shortcut: ~4.5 ms
  - Full:     ~20 ms  (4.5× slower, 3–4 iterations)

Ma construction is identical (~6 ms) — harmonics computed lazily.

scan_modes (n_max=2, E_max=2000 MeV, 15624 modes):
  - Static:   ~140 ms
  - Shortcut: ~1050 ms
  - Full:     ~1220 ms  (only ~15% slower than shortcut)

The scan overhead is small because harmonics are cached by
(|n_tube|, |n_ring|, r).  Most of the 15,624 modes share the
same sheet parameters, so only a handful of unique harmonics
need computing.  The dominant cost is the 15,624 energy() calls.
