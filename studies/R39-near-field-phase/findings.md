# R39. Phase-dependent near-field interaction — Findings

**Date:** 2026-03-28
**Scripts:** `track1_field_structure.py`, `track2_interaction_sweep.py`,
  `track3_near_field_analysis.py`, `track5_charge_models.py`,
  `track6_electromagnetic.py`
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


## F7. No electrostatic attraction (Track 2, Track 3)

At no sampled point (d, Δφ) does the proton-proton electrostatic
interaction become attractive.  The near-field effect is exclusively
a **reduction of repulsion**, not a generation of attraction.

The minimum U/U_Coulomb found was ~0.03 (at d = 0.1 fm), still
positive.

**Caveat**: this finding applies to the electrostatic sector only.
The magnetic interaction (F8) is not included and could change this
conclusion.


## F8. Charge distribution model is secondary (Track 5)

Track 5 compared three charge models to test whether the Tracks 1–4
results depend on the assumed charge distribution:

**Model A** — Uniform line charge along the (1,2) geodesic
(traveling wave / WvM picture).  This is what Tracks 1–4 used.

**Model B** — Standing-wave modulated line charge (cos² along the
geodesic).  The charge has nodes and antinodes, creating
concentrated lumps whose positions depend on phase.

**Model C** — Uniform charge on the full 2D torus surface (KK wave
mechanics: |ψ|² = 1 everywhere).  No geodesic, no phase parameter.

Results at nuclear distances (U/U_Coulomb):

| d (fm) | Model A (avg) | Model B (avg) | Model C | A spread | B spread |
|--------|---------------|---------------|---------|----------|----------|
| 0.5    | 0.136         | 0.129         | 0.121   | 0.047    | 0.056    |
| 1.0    | 0.253         | 0.246         | 0.231   | 0.063    | 0.068    |
| 2.0    | 0.460         | 0.462         | 0.430   | 0.054    | 0.059    |
| 3.0    | 0.641         | 0.647         | 0.598   | 0.045    | 0.091    |
| 5.0    | 0.937         | 0.854         | 0.845   | 0.134    | 0.136    |

Key findings:

1. **All three models agree on the geometric suppression** to
   within ~20%.  The ~70% barrier reduction at 1 fm is robust
   and model-independent.

2. **Phase spread is comparable** between Models A and B.  The
   standing-wave modulation does not dramatically amplify phase
   effects at nuclear distances.

3. **Model C has zero phase dependence** by construction.  In
   the KK wave mechanics picture, the charge density |ψ|² = 1
   is uniform on the surface, and no phase parameter exists.

4. **The overshoot at d ≈ 7 fm** (F5) appears only in Model A.
   Models B and C stay at or below U_Coulomb at all distances.
   The overshoot was an artifact of concentrating all charge on
   a 1D geodesic.

5. **At large d, all models converge** to U/U_Coulomb → 1.0.


## F9. Magnetic interaction is same order as electric (Track 6)

The charge circulating on the geodesic at speed c is a current loop.
For a photon (v = c), the magnetic energy is not a small correction
— it is the **same order** as the electric energy.

The total electromagnetic interaction per segment pair reduces to:

    U_EM = Σ dq₁ dq₂ (1 − dl̂₁·dl̂₂) / |r₁ − r₂|

where dl̂ is the unit tangent to the geodesic.  The combined factor
(1 − cos θ) ranges from 0 (parallel currents, complete E/M
cancellation) to 2 (anti-parallel, double repulsion).

Track 6 computed U_EM for four relative orientations of two
proton (1,2) modes:

| d (fm) | d/a  | Aligned-z | Aligned-x | Flipped-z | Tilted-90 | Elec-only |
|--------|------|-----------|-----------|-----------|-----------|-----------|
| 0.2    | 0.05 | 0.049     | 0.049     | 0.103     | 0.055     | 0.076     |
| 0.5    | 0.13 | 0.113     | 0.115     | 0.199     | 0.128     | 0.156     |
| 1.0    | 0.27 | 0.223     | 0.236     | 0.334     | 0.239     | 0.278     |
| 2.0    | 0.53 | 0.412     | 0.475     | 0.529     | 0.432     | 0.471     |
| 3.0    | 0.79 | 0.573     | 0.611     | 0.684     | 0.604     | 0.628     |
| 5.0    | 1.34 | 0.849     | 0.869     | 0.953     | 0.886     | 0.901     |

All values are U_EM / U_Coulomb (point charge).

Key findings:

1. **The magnetic contribution is 20–36% of the electric** at
   nuclear distances, not a perturbative correction.  This is a
   direct consequence of v = c.

2. **Aligned tori (pole-to-pole) get the most suppression.**
   At 1 fm, U_EM/U_C = 0.22 (78% suppression) vs 0.28 for
   electric-only — magnetism adds 6 percentage points.

3. **Flipped tori (anti-parallel currents) get the least
   suppression.**  At 1 fm, U_EM/U_C = 0.33 (67% suppression).
   Both electric and magnetic are repulsive.

4. **Orientation matters: factor of ~2 between best and worst**
   at d = 0.2 fm (0.049 vs 0.103).  The spinning-top intuition
   is confirmed — orientation is physically meaningful.

5. **No attraction at any orientation or distance.**  Even with
   the magnetic interaction, U_EM > 0 everywhere.  The
   "spin-aligned" N-S attraction from the current loop is real
   but not strong enough to overcome the (already suppressed)
   Coulomb repulsion.

6. **At large d, all orientations converge** to U_EM/U_C → 1.0.

**NOTE**: v = c (photon speed) is assumed.  If the mode propagates
at a different speed v, the magnetic contribution scales as (v/c)²
and shrinks accordingly.


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
   spread over a torus of radius ~3.7 fm.  This result is robust
   across all three charge distribution models (F8).

3. **Phase modulation is secondary** (F4): ~3–13% of the interaction,
   depending on distance.  Quadrature (Δφ = π/2) gives less repulsion
   than in-phase (Δφ = 0) at short range.

4. **No electromagnetic attraction** (F7, F9): even with the magnetic
   interaction at v = c, no orientation produces a net attractive
   potential.  The magnetic N-S attraction from aligned current loops
   adds ~6 percentage points of suppression (bringing 1 fm from 74%
   to 78%) but does not flip the sign.

5. **Orientation is physically meaningful** (F9): aligned tori
   (pole-to-pole) repel 50% less than flipped tori at close range.
   This creates a strong orientational preference that could influence
   nuclear structure.

6. **An attractive mechanism beyond classical EM is still needed.**
   The R29 F6 gauge boson remains the leading candidate for nuclear
   binding.  The geometric + magnetic suppression (~78%) lowers the
   Coulomb barrier to ~0.3 MeV at 1 fm, which the gauge boson only
   needs to overcome — not the full 1.4 MeV.

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
electrostatic barrier is still positive.

Track 6 computed the full electromagnetic interaction (electric +
magnetic at v = c).  The magnetic attraction from aligned current
loops adds ~6 percentage points of additional suppression at 1 fm,
bringing the total barrier to ~0.3 MeV.  This is still positive —
no classical EM cold-fusion mechanism exists at the (1,2) mode
level.  However, the 78% barrier reduction is substantial and
would lower the threshold for any non-EM binding mechanism.


## Open questions

1. **Full orientation sweep**: Track 6 tested four discrete
   orientations.  A systematic sweep over Euler angles (θ, ψ)
   could find the true minimum-energy configuration and determine
   whether there are orientations not yet tested that produce
   stronger suppression or attraction.

2. **Non-photon speed**: If the mode propagation speed is v < c,
   the magnetic contribution scales as (v/c)² and diminishes.
   What speed is physical for the proton mode?

3. **Other winding numbers**: The (1,2) mode has a special symmetry
   (Δφ=0 ≡ Δφ=π).  Do higher modes (2,3), (1,3), etc. break this
   symmetry and allow genuine phase-dependent effects?

4. **Self-intersecting torus validity**: The proton torus has a/R ≈ 9,
   meaning it self-intersects severely.  The 3D embedding is
   unphysical (the torus passes through itself).  Should we instead
   use the intrinsic flat-torus distance, bypassing 3D embedding?

5. **Multipole convergence**: The d⁻² power law (F6) instead of d⁻⁵
   suggests the multipole expansion is not converging well.  A
   different analytical approach may be needed for the self-
   intersecting regime.
