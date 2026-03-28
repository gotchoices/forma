# R39. Phase-dependent near-field interaction — Findings

**Date:** 2026-03-28
**Scripts:** `track1_field_structure.py`, `track2_interaction_sweep.py`,
  `track3_near_field_analysis.py`
**Library:** `lib/ma_model.py` (v1), `lib/embedded.py`


## Geometry

The proton sheet geometry is fully determined by r_p = 8.906 (pinned
by the neutron + muon masses, R27 F18).  No other free parameters
enter this study.

The proton sheet's within-plane shear s₅₆ is derived from r_p via
the α formula (R19).  The circumferences follow from the proton
mass:

| Parameter | Value | Source |
|-----------|-------|--------|
| r_p       | 8.906 | Pinned: neutron + muon masses (R27 F18) |
| s₅₆      | 0.007635 | α formula: α(r_p, s₅₆) = 1/137.036 |
| L_tube    | 23.48 fm | m_p and μ₁₂(r_p, s₅₆) |
| L_ring    | 2.637 fm | m_p and μ₁₂(r_p, s₅₆) |
| a (tube radius) | 3.738 fm | L_tube / 2π |
| R (ring radius) | 0.420 fm | L_ring / 2π |
| a/R       | 8.906 | = r_p (self-intersecting torus: a >> R) |

The charge distribution extends to ±a ≈ ±3.7 fm from the torus
center, so **a is the relevant length scale**, not R.

Nuclear force range (1–3 fm) = 0.27–0.80 a.  At nuclear
distances, the separation is less than the charge extent.


## F1. Multipole structure (Track 1)

The (1,2) mode on the proton torus has:

| Multipole | Phase-dependent? | Magnitude (e·fm^l) |
|-----------|------------------|--------------------|
| Monopole q₀₀ | No (topological) | 0.282 |
| Dipole |d| | No (vanishes by symmetry) | ~10⁻¹⁶ |
| Quadrupole eigenvalues | No (tensor rotates, shape fixed) | 3.4, 10.0, 13.4 |
| Quadrupole m≠0 | Yes (oscillates with φ) | ~3.8 |
| Hexadecapole m≠0 | Yes | up to ~40 |

The dipole vanishes because the charge distribution is centered on
the torus origin.  The lowest phase-dependent moment is the
quadrupole (l=2, m≠0).

**Phase-independent moments:** (l, m=0) for even l: q₀₀, q₂₀, q₄₀.
**Phase-dependent moments:** all m≠0 components.

The quadrupole tensor eigenvalues are invariant under phase rotation
(the tensor rotates rigidly with φ, preserving its shape).


## F2. Phase symmetry (Track 1, confirmed Track 3)

The (n₁, n₂) geodesic θ₁ = n₁t + φ, θ₂ = n₂t has a symmetry:
substituting t → t + π gives θ₁ → n₁t + n₁π + φ, θ₂ → n₂t + n₂π.
For (1,2): this maps to θ₁ = t + (φ+π), θ₂ = 2t (since 2π is a
full revolution).

**The charge distribution is invariant under φ → φ + π.**

Consequence: the interaction depends on Δφ with period π, not 2π.
Δφ = 0 and Δφ = π give identical interactions.  The distinct phase
range is [0, π).

Verified numerically: U(d, Δφ) = U(d, Δφ+π) to machine precision
(~10⁻¹⁶ relative).

This contradicts the Q88 hypothesis that "anti-phase" (Δφ = π) modes
would have cancelling multipoles.  There is no distinction between
in-phase and anti-phase for the (1,2) mode.


## F3. Massive near-field suppression (Track 2, Track 3)

At nuclear distances (1–3 fm), the proton-proton interaction energy
is dramatically less than point-charge Coulomb:

| d (fm) | d/a   | ⟨U⟩/U_Coulomb | Suppression |
|--------|-------|---------------|-------------|
| 0.5    | 0.13  | 0.135         | 87%         |
| 1.0    | 0.27  | 0.261         | 74%         |
| 1.5    | 0.40  | 0.355         | 65%         |
| 2.0    | 0.53  | 0.449         | 55%         |
| 2.5    | 0.67  | 0.555         | 44%         |
| 3.0    | 0.81  | 0.644         | 36%         |

This is a **purely geometric effect**: the charge is spread over the
torus surface (extent ±a ≈ ±3.7 fm), so at separations d < a, the
particles' charge distributions interpenetrate.  Much of each
charge is farther from the other particle's center than d.

The suppression is phase-independent — it arises from the shape of
the torus, not from any alignment.

**In physical units** (αℏc = 1.440 MeV·fm):

| d (fm) | U_Coulomb (MeV) | U_eff (MeV) | Reduction |
|--------|-----------------|-------------|-----------|
| 0.5    | 2.88            | 0.39        | 87%       |
| 1.0    | 1.44            | 0.38        | 74%       |
| 2.0    | 0.72            | 0.32        | 55%       |
| 3.0    | 0.48            | 0.31        | 36%       |

The effective Coulomb barrier at nuclear distances is roughly constant
at ~0.3–0.4 MeV, much lower than the 1.44 MeV point-charge value
at 1 fm.


## F4. Phase dependence is real but secondary (Track 3)

The dominant Fourier mode of U(d, Δφ) in Δφ is cos(2Δφ), as expected
from the π-periodicity.  The amplitude:

| d (fm) | d/a  | |A₁|/A₀ |
|--------|------|---------|
| 0.1    | 0.03 | 17.4%   |
| 0.5    | 0.13 | 15.8%   |
| 1.0    | 0.27 | 11.4%   |
| 2.0    | 0.53 | 3.6%    |
| 3.0    | 0.81 | 1.3%    |
| 5.0    | 1.34 | 8.1%    |
| 8.0    | 2.14 | 3.5%    |

The phase modulation is ~3–17% of the mean interaction, depending on
distance.  The maximum modulation (~17%) occurs at the closest
separations.

**Direction of the effect**: at d < a, in-phase (Δφ=0) gives MORE
repulsion than quadrature (Δφ=π/2).  Above d ≈ a, this reverses.

At d = 2 fm: the in-phase/quadrature ratio is 1.13, meaning
in-phase modes repel 13% more than quadrature.


## F5. Crossover and overshoot (Track 3)

The phase-averaged interaction crosses Coulomb at d ≈ 5.5 fm (1.5a):

- d < 5.5 fm: ⟨U⟩ < U_Coulomb (suppressed)
- d ≈ 7.4 fm: ⟨U⟩ peaks at 1.23 × U_Coulomb (23% overshoot)
- d > 29 fm: ⟨U⟩ within 1% of U_Coulomb

The overshoot arises because at d ≈ 2a, the nearest lobes of the
charge distributions are very close while the far lobes are ~2d apart.
The 1/r dependence makes the near lobes dominate, producing a net
enhancement.


## F6. Power-law falloff (Track 3)

At large distances (d > 5a ≈ 19 fm):

    (⟨U⟩/U_C − 1) ∝ d^{−2.0}

This is **slower** than the d⁻⁵ expected from a quadrupole correction
to a monopole interaction.  The slow falloff likely reflects the
self-intersecting torus geometry (a >> R), where the multipole
expansion converges poorly.  The charge distribution extends to
r ~ a ≈ 3.7 fm, so the multipole expansion is only valid for
d >> a, and even at d = 20 fm the expansion is marginal.


## F7. No attraction (Track 2, Track 3)

At no sampled point (d, Δφ) does the proton-proton interaction
become attractive.  The near-field effect is exclusively a
**reduction of repulsion**, not a generation of attraction.

The minimum U/U_Coulomb found was ~0.03 (at d = 0.1 fm), still
positive.


## Implications

### For nuclear binding (Q88)

Q88 hypothesized that anti-phase (Δφ = π) modes would have cancelling
near-field multipoles, reducing repulsion and potentially enabling
nuclear binding.  This study found:

1. **Δφ = 0 and Δφ = π are identical** for the (1,2) mode (F2).
   The "anti-phase suppression" mechanism does not exist as described.

2. **The dominant effect is geometric suppression** (F3), not phase-
   dependent cancellation.  The Coulomb barrier is naturally reduced
   to ~0.3 MeV at nuclear distances, simply because the charge is
   spread over a torus of radius ~3.7 fm.

3. **Phase modulation is secondary** (F4): ~3–13% of the interaction,
   depending on distance.  Quadrature (Δφ = π/2) gives less repulsion
   than in-phase (Δφ = 0) at short range.

4. **No attraction** (F7): the near-field effect alone cannot bind
   nuclei.  An attractive mechanism (e.g., the R29 F6 gauge boson)
   is still needed.

### For α constraint (Q88 §4)

Q88 suggested α might be constrained by nuclear stability through
near-field balance.  The finding that the near-field suppression
is geometric (depending on the torus aspect ratio, not α) means
this particular constraint mechanism is weaker than hypothesized.
The suppression factor at d ≈ a is primarily a function of a/R.

### For entanglement (Q82)

The phase-dependent correction exists (F4) and is measurable
(~3–14%).  Phase-locked particles interact differently from
uncorrelated ones, with the effect depending on the specific
phase relationship.  But the effect is small enough that it
would be very difficult to detect experimentally.

### For cold fusion (Q88 §5)

The barrier reduction factor is ~0.26 at 1 fm (from geometric
suppression), not the ~0.015 from anti-phase cancellation that
Q88 estimated.  The geometric suppression is real and substantial
(~74%), but there is no additional large factor from phase
alignment.

The barrier in physical units is ~0.3 MeV at nuclear distances,
compared to ~1.4 MeV for point charges.  This reduction is
meaningful but does not by itself enable cold fusion — the
barrier is still positive and requires quantum tunneling.


## Open questions

1. **Other winding numbers**: The (1,2) mode has a special symmetry
   (Δφ=0 ≡ Δφ=π).  Do higher modes (2,3), (1,3), etc. break this
   symmetry and allow genuine phase-dependent effects?

2. **Mixed-mode interactions**: Two different modes (e.g., proton +
   proton with different quantum numbers) do not share the same
   torus symmetry and might have richer phase dependence.

3. **Self-intersecting torus validity**: The proton torus has a/R ≈ 9,
   meaning it self-intersects severely.  The 3D embedding is
   unphysical (the torus passes through itself).  Should we instead
   use the intrinsic flat-torus distance, bypassing 3D embedding?

4. **Multipole convergence**: The d⁻² power law (F6) instead of d⁻⁵
   suggests the multipole expansion is not converging well.  A
   different analytical approach may be needed for the self-
   intersecting regime.
