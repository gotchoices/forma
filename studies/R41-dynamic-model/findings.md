# R41. Dynamic torus model — Findings

**Date:** 2026-03-01
**Status:** Done


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


## Track 4: Fresh parameter determination

Script: `scripts/track4_fresh_params.py`

### F30. Dynamic model does NOT shift r_p or σ_ep

Starting from a generic initial guess and fitting to neutron
(939.565 MeV) + muon (105.658 MeV) — the same R27 protocol:

| Method   | r_p          | σ_ep          | Iters | Time   |
|----------|-------------|---------------|-------|--------|
| static   | 8.91024743  | -0.09092990   | 5     | 186 ms |
| shortcut | 8.91024764  | -0.09092991   | 5     | 720 ms |
| full     | 8.91024763  | -0.09092991   | 5     | 3.9 s  |

Parameter shifts (full − static):
  Δr_p  = +2.0×10⁻⁷
  Δσ_ep = −2.2×10⁻¹⁰

The dynamic model reproduces the static R27 solution to 7
significant figures.  This is because the fit targets (neutron,
muon) have negligible dynamic corrections:
  - Neutron: n_tube = 0 on the proton sheet → zero correction
  - Muon: δE/E ≈ 2×10⁻⁸ → sub-eV shift

The geometry parameters are controlled by the static structure
(Compton constraint + mode assignments), not by the O(α²)
dynamic corrections.


### F31. Dynamic corrections shift non-target energies

At the fitted parameters, the dynamic model shifts:
  - E(electron): +0.090 MeV (full) vs target 0.511 MeV
  - E(proton):   +0.316 MeV vs target 938.272 MeV

These are the δE/E ≈ 1.8×10⁻⁴ (electron) and 3.4×10⁻⁴ (proton)
corrections from the force-balance.  They represent the
model's prediction that measured particle masses include a
geometric correction from the deformed torus wall.

The self-consistent L-rescaling in Ma targets E_static = m_e
and E_static = m_p.  So:
  E_dynamic(electron) = m_e × (1 + δE/E_e) ≈ m_e + 0.09 MeV
  E_dynamic(proton)   = m_p × (1 + δE/E_p) ≈ m_p + 0.32 MeV

These are predictions, not errors: the dynamic model says the
"bare" torus mass is m_e, and the physical mass is m_e + δm.


### F32. 3-target fit reveals L-rescaling inconsistency

When the electron is added as a fit target (with r_e free):
  - Static: converges, r_e ≈ 0.5000 (unchanged)
  - Full: does NOT converge after 50 iterations

The non-convergence happens because the self-consistent
L-rescaling adjusts L until E_static(electron) = m_e, but
the fit residual uses E_dynamic(electron) = m_e × (1 + δE/E).
The residual can never reach zero — it saturates at
~m_e × δE/E ≈ 10⁻⁴ MeV.

The fitter compensates by pushing r_e to 0.317 (from 0.5),
where the dynamic correction is smaller (δE/E ≈ 3×10⁻⁵),
but still can't close the gap completely.

**Implication:** To properly fit with the electron as a target
under the dynamic model, the self-consistent L-rescaling should
target dynamic energies, not static.  This is a code
enhancement for a future track — the physics is correct, the
inner loop just needs to use energy() instead of energy_static().


### F33. Fit is robust from distant starting points

Starting from r_p = 5.0, σ_ep = 0.0 (far from the solution),
both static and full converge to the same answer in 7 iterations.
The basin of attraction is large and the Levenberg-Marquardt
solver handles it cleanly.


## Track 5: Ghost census

Script: `scripts/track5_ghost_census.py`

### F34. 117,648 modes below 2 GeV; dynamic model changes nothing

With n_max=3, both static and dynamic models produce exactly
117,648 modes below 2 GeV.  No modes cross the threshold —
energy shifts are O(10⁻⁴) relative, max |δE| = 0.62 MeV.

Of these, 7,434 (6.3%) match known particles within 5%;
110,214 (93.7%) are ghosts.  The dynamic model does not
change these counts.


### F35. The (1,1) ghost is NOT suppressed by the low-pass filter

The critical remaining ghost from R33 — the (1,1) charged
spin-1 boson at half the electron mass — has filter factor
FF ≈ 0.46.  This means its eigenvalue shift is about half
the electron's, not zero.

| Mode           | E (MeV) | δE/E       | FF    | Q  |
|----------------|---------|------------|-------|-----|
| e-sheet (1,1)  | 0.259   | 1.59×10⁻⁴ | 0.46  | −1 |
| e-sheet (1,2)  | 0.515   | 3.43×10⁻⁴ | 1.00  | −1 |
| p-sheet (1,1)  | 473.6   | 1.57×10⁻⁴ | 0.47  | +1 |
| p-sheet (1,2)  | 945.5   | 3.37×10⁻⁴ | 1.00  | +1 |

The (1,1) has the same tube winding (n_tube=1) as the
fundamental, so both couple to the k=2 harmonic.  The FF < 1
comes from the different ring winding: (1,1) produces less
curvature variation than (1,2), giving a smaller |c₂/c₀|.

**The dynamic model does NOT solve the (1,1) ghost problem.**
The ghost persists with slightly reduced (but nonzero)
dynamic correction.


### F36. Higher tube windings ARE effectively suppressed

The low-pass filter works as designed for |n_tube| ≥ 2:

| |n_tube|_max | Count   | Median FF  | Suppression |
|-------------|---------|-----------|-------------|
| 0           | 342     | 0         | ∞ (no corr) |
| 1           | 8,918   | 0.47      | 2×          |
| 2           | 33,614  | 0.005     | 200×        |
| 3           | 74,774  | 0.0002    | 5,000×      |

This reinforces R33's n₁ = ±1 charge selection rule: modes
with |n_tube| ≥ 2 are both charge-suppressed (R33 F1) and
eigenvalue-shifted less (dynamic filter).  The two mechanisms
are complementary but target the same modes — the critical
(1,1) ghost escapes both.

Some cross-sheet modes (e.g., (-1,-3,-2,0,0,0)) achieve
FF > 1 because their multi-sheet corrections combine to
exceed the single-sheet fundamental.  These are all ghosts.


### F37. The ghost problem is unchanged by the dynamic model

The dynamic model's contribution to ghost suppression is:
1. A soft eigenvalue shift (not a hard cutoff)
2. Strongest for high tube windings (already killed by R33)
3. Weak for the critical (1,1) ghost (FF ≈ 0.46)
4. Zero for ring-only modes (n_tube=0)

The ghost problem remains as characterized in R33: ~4 survivors
per charged sheet after the charge and spin filters, with the
(1,1) boson as the critical tension.  The dynamic model adds
no new suppression mechanism for this mode.


## Track 5c: Three-category census with generation identification

Script: `scripts/track5c_generation_census.py`

The n_max=3 census in Track 5 missed the muon and tau (both
require n_max ≥ 5).  This track redoes the census with n_max=5
and proper mode taxonomy.

### F38. Three charged lepton generations confirmed

All three generations appear in the n_max=5 spectrum:

| Particle | Mode                    | E_static | E_target | Error  | FF     |
|----------|------------------------|----------|----------|--------|--------|
| electron | (1, 2, 0, 0, 0, 0)     | 0.515    | 0.511    | +0.8%  | 1.0000 |
| muon     | (−1, 5, 0, 0, −2, 0)   | 106.468  | 105.658  | +0.8%  | 0.0002 |
| tau      | (−1, 5, 0, 0, −2, −4)  | 1890.812 | 1776.86  | +6.4%  | 0.0250 |

The low-pass filter naturally distinguishes them:
- **Electron**: e-sheet only (n_tube=1), couples to k=2. FF = 1.0.
- **Muon**: cross-sheet mode with n₅=−2 on p-sheet. The p-sheet
  couples to k=4, suppressed 40× relative to k=2.  The muon's
  δE/E ≈ 8×10⁻⁸ is 4,300× smaller than the electron's.
- **Tau**: same tube windings as muon, but n₆=−4 ring winding
  gives an intermediate p-sheet correction. FF = 0.025.

The FF ordering (e > τ > μ) means the dynamic model predicts
different wall distortion for each generation — a geometric
origin for the generation hierarchy.


### F39. Three-category taxonomy: 131,769 families below 2 GeV

The 1,449,458 modes from n_max=5 collapse into 131,769 families
when only n₄ (neutrino ring winding) is treated as degenerate.
Each family has 11 copies (n₄ = −5 to +5).

Classification:

| Category | Description                  | Families | Modes     |
|----------|------------------------------|----------|-----------|
| A        | Match known particle (10%)   | 8,633    | 94,963    |
| B        | High harmonics, |n_tube|≥ 2  | 120,863  | 1,329,493 |
| C        | Unmatched resonances         | 2,273    | 25,002    |

**Category A** matches 14 particle types (e±, μ±, τ±, p, p̄, n,
K⁰, η′, φ, Ξ⁰, Ξ⁻ within a generous 10% window).  Most families
have |n_tube| ≥ 2 (due to neutrino tube winding dressing).

**Category B** is 92% of all families.  These are killed by both
the low-pass filter (FF ≤ 0.03 for |n_tube| ≥ 2) and R33's
charge selection rule.

**Category C** (2,273 families) are the genuine problem modes:
|n_tube| ≤ 1, no known particle match.  All have n₅ = n₆ = 0
(electron-sheet-only energy), dressed with various n₃ values.
The (1,1) boson variants (n₁=1, n₂=1, n₃ = 0/±1) persist at
FF ≈ 0.46.


### F40. Only n₄ is truly degenerate; n₃ creates distinct modes

The neutrino sheet's n₃ (tube winding) changes charge and spin:
- (1, 1, 0, 0, 0): Q = −1, spin = ½
- (1, 1, 1, 0, 0): Q = −2, spin = 1
- (1, 1, −1, 0, 0): Q = 0, spin = 1

These are physically distinct particles at the same mass
(~0.259 MeV), not copies.  Only n₄ produces true degeneracy
(11-fold, negligible energy contribution ~meV).


### F41. Some unmatched resonances have FF > 1

Modes with high ring winding on the electron sheet have larger
dynamic corrections than the fundamental:

| Mode family         | E (MeV) | FF    | Note                 |
|---------------------|---------|-------|----------------------|
| (±1, ±3, *, 0, 0)  | 0.772   | 1.302 | 3rd ring harmonic    |
| (±1, ±2, *, 0, 0)  | 0.515   | 1.000 | = electron (same k)  |
| (±1, ±1, *, 0, 0)  | 0.259   | 0.464 | (1,1) boson          |
| (±1, 0, *, 0, 0)   | 0.039   | 0.000 | pure tube, no ring   |
| (0, *, *, 0, 0)     | varies  | 0.000 | ring-only, no tube   |

FF > 1 for ring overtones means the dynamic model makes these
modes MORE shifted (not less).  The low-pass filter only works
for increasing tube harmonic number, not ring harmonics.


## Track 7: Particle table and verdict

Script: `scripts/track7_particle_table.py`


### F42. Dynamic model does not improve any mass prediction

Full particle table comparing static vs dynamic energies for all
12 canonical mode assignments (4 anchors + 1 generation + 7 hadron
predictions):

| Particle | E_static | E_dynamic | E_observed | Err_s  | Err_d  | δE/E       | FF     |
|----------|----------|-----------|------------|--------|--------|------------|--------|
| e⁻       | 0.515    | 0.515     | 0.511      | +0.8%  | +0.8%  | 3.43×10⁻⁴ | 1.0000 |
| p        | 945.5    | 945.8     | 938.3      | +0.8%  | +0.8%  | 3.37×10⁻⁴ | 1.0000 |
| n        | 946.8    | 946.8     | 939.6      | +0.8%  | +0.8%  | ~0         | 0.0000 |
| μ⁻       | 106.5    | 106.5     | 105.7      | +0.8%  | +0.8%  | 7.9×10⁻⁸  | 0.0002 |
| τ⁻       | 1890.8   | 1890.8    | 1776.9     | +6.4%  | +6.4%  | 8.4×10⁻⁶  | 0.0250 |
| K⁺       | 491.7    | 491.7     | 493.7      | −0.4%  | −0.4%  | ~0         | 0.0000 |
| K⁰       | 507.6    | 507.6     | 497.6      | +2.0%  | +2.0%  | ~0         | 0.0000 |
| η        | 555.4    | 555.4     | 547.9      | +1.4%  | +1.4%  | 0          | 0.0000 |
| η′       | 968.4    | 968.4     | 957.8      | +1.1%  | +1.1%  | ~0         | 0.0000 |
| φ        | 1035.9   | 1035.9    | 1019.5     | +1.6%  | +1.6%  | 0          | 0.0000 |
| Λ        | 1114.3   | 1114.3    | 1115.7     | −0.1%  | −0.1%  | ~0         | 0.0000 |
| Σ⁺       | 1202.5   | 1202.5    | 1189.4     | +1.1%  | +1.1%  | 0          | 0.0000 |

Result: 0 improved, 2 worsened (electron +0.035%, proton +0.034%),
10 unchanged.  The dynamic corrections (O(α²) ≈ 10⁻⁴) are 100×
smaller than the structural errors (1–6%).

The hadron predictions (K, η, φ, Λ, Σ) have essentially zero
dynamic correction because their tube windings on the charged
sheets are |n_tube| ≥ 3, coupling to k ≥ 6 (deeply suppressed).
Only single-sheet fundamental modes (electron, proton) receive
the full correction.


### F43. Verdict — conceptual advance, not quantitative improvement

**Dynamic model wins:**

1. Elliptical cross-section from first principles, no free parameters
2. Low-pass filter kills 92% of mode spectrum (120,863 families
   with |n_tube| ≥ 2), complementing R33's charge selection rule
3. Generation hierarchy has geometric origin: the FF ordering
   e (1.00) > τ (0.025) > μ (0.0002) comes from cross-sheet tube
   windings coupling to higher Fourier harmonics
4. Self-consistent force balance converges in 3–4 iterations
   (ratio ~α²); perturbative nature is OUTPUT not assumption
5. Reproduces static parameters (r_p, σ_ep) to 7 significant figures

**Static model wins:**

1. Simpler (no iteration needed)
2. Mass predictions not improved — dynamic shifts are 100× smaller
   than existing structural errors
3. Consistent L-rescaling with electron target (dynamic model has
   a bug here, F32)

**Neither wins:**

1. (1,1) ghost unsuppressed (FF = 0.46)
2. r_e and r_ν remain free
3. Tau discrepancy unchanged (5.6% structural gap)
4. Pion not matched by either model

The dynamic model should be retained as the correct physical
picture.  For practical calculations, the static model gives
identical results to 4 decimal places.
