# R33. Ghost mode selection — why most T⁶ modes are dark

**Questions:** Q77 (coupling suppression), Q34 (charge mechanism)
**Type:** compute + theoretical  **Depends on:** R19, R27, R28, R31, R32
**Status:** Framed


## Motivation

The T⁶ spectrum contains ~900 modes below 2 GeV, but only
~40 correspond to observed particles (R28 Track 2).  The
remaining ~860 are "ghost modes" — valid solutions of the
wave equation on T⁶ with definite mass, charge, and spin,
but no observed counterpart.

Two independent calculations demand that ghost modes are
electromagnetically suppressed by a factor of ~10⁵:

- **R31 Track 4**: Naive KK Yukawa corrections to the
  hydrogen Lamb shift exceed observation by 10⁵.
- **R32 Track 1**: Naive vacuum polarization from the T⁶
  mode spectrum produces running of α that is 157,000×
  too fast, with a Landau pole at ~1 MeV.

Both results point to the same conclusion: ghost modes do
not couple to the electromagnetic field with the same
strength as known particles.  But neither explains WHY.

This study investigates the geometric mechanism behind ghost
mode suppression.


## Prior results

- **R19**: The shear-charge formula derives α from an
  integral over the torus surface.  The integral depends
  on the full mode shape, not just n₁.
- **R27 F37–F42**: Lifetime-gap correlation (r = −0.84)
  suggests observed particles are off-resonance
  excitations, not exact T⁶ eigenmodes.
- **R28 Track 2**: ~900 modes below 2 GeV, ~20× more than
  known particles.  Proton energy ladder (52 MeV steps)
  dominates the spectrum.
- **R31 Track 4**: KK massive mode coupling suppressed by
  ≥10⁵ (from Lamb shift).
- **R32 Track 1 F2**: 112 charged modes exist below the
  electron mass (0.511 MeV).  The lightest charged mode
  is at 39 keV — 13× lighter than the electron.


## Key questions

1. Does the R19 shear-charge integral naturally suppress
   modes with high winding numbers?
2. Do modes with n₂ = 0 (no ring winding) have zero
   effective electromagnetic coupling, even though the KK
   formula assigns them charge?
3. Is there a pattern distinguishing the ~40 "physical"
   modes from the ~860 ghosts?
4. Can the ~10⁵ suppression factor be derived from the
   geometry?
5. Do production selection rules (quantum number
   conservation) explain which modes are reachable from
   known-particle reactions?
6. Does the energy gap structure of the T⁶ spectrum
   (spacing between modes, pair-production ceilings,
   harmonic ladders) create natural stability islands
   that correlate with known particles?


## Approach: 5 tracks

### Track 1 — Charge integral per mode

The R19 shear-charge formula derives α from a surface
integral over the electron T².  The integral assumes the
(1,2) mode shape.  Generalize it:

For each mode (n₁, n₂), compute the charge integral:

    Q_eff(n₁, n₂) = ∫∫ [EM flux from mode (n₁,n₂)] dA

on the sheared T².  The KK formula says Q = −n₁ (for the
electron sheet), independent of n₂.  The WvM integral may
give a different (suppressed) result for modes other than
(1,2).

**Test**: Compute Q_eff for all modes with |n₁| ≤ 8,
|n₂| ≤ 8.  Does Q_eff → 0 for ghost modes?  Does the
suppression scale as ~10⁻⁵?

**Output**: Table of Q_eff / Q_KK for each mode.
Identification of which modes are electromagnetically
active vs dark.


### Track 2 — Quantum number reachability

Starting from the known stable particles (e, p, ν) and
their antiparticles, determine which T⁶ modes are
"reachable" — producible by collisions that conserve
charge, energy, and total winding numbers.

For example, e⁺ + e⁻ annihilation can produce any mode
with Q = 0 and total n₁ = 0, n₅ = 0, up to the
collision energy.  But can it produce a mode with
n₁ = 3, n₂ = 7?

Map the space of reachable modes under:
- e⁺e⁻ → X  (Q = 0)
- pp → X  (Q = +2 or Q = 0 with pair)
- ep → X  (Q = 0)

**Output**: Fraction of ghost modes that are reachable vs
unreachable from standard reactions.  If most ghosts are
unreachable, the production bottleneck explains their
absence.


### Track 3 — Decay lifetime estimation

For each ghost mode, estimate whether a lighter mode with
the same charge exists.  If yes, the ghost can decay
(assuming some coupling, however small).  If no, the ghost
is stable within its charge sector — a serious problem.

**Test**: For every ghost mode with Q ≠ 0 below 2 GeV,
is there a lighter mode with the same Q?  Are there
"stable ghosts" — charged modes lighter than the electron
in their charge sector?

The 112 charged modes below the electron mass (R32 F2)
are candidates for stable ghosts.  If they exist and are
truly stable, they should have been observed.  Their
absence constrains the model.

**Output**: Census of potentially stable ghosts.
Assessment of model tension.


### Track 4 — Winding number complexity and coupling

Investigate whether mode complexity (total |n| or number
of nonzero quantum numbers) correlates with coupling
suppression.

Hypothesis: simpler modes (fewer nonzero quantum numbers,
lower total |n|) couple more strongly.  Known particles
tend to have simple quantum numbers (electron = (1,2),
proton = (0,0,0,0,1,2)).  Ghosts tend to have complex
quantum numbers (many nonzero entries, high |n|).

**Test**: For all modes below 2 GeV, compute a complexity
metric (e.g., Σ|n_i|, or number of nonzero n_i) and
check whether known particles cluster at low complexity
while ghosts cluster at high complexity.

**Output**: Complexity distribution of physical modes vs
ghosts.  If there's a clean separation, the complexity
metric itself might BE the selection rule.


### Track 5 — Energy gap structure and pair-production ceilings

Each T⁶ mode has a fixed rest energy.  For fermions
(spin-½), Pauli exclusion limits occupancy to 1 particle
per quantum state.  At energy 2m, a particle–antiparticle
pair can be created — this is the pair-production ceiling.

Between m and 2m, additional energy goes to either R³
kinetic energy (momentum) or excitation of a DIFFERENT T⁶
mode.  The charge-preserving excitations (1, n₂) for
n₂ = 3, 4, 5, ... on the electron sheet keep charge = −1
while increasing mass.  These form the "harmonic ladder"
(see Q85).  Their spacing depends on the free parameter r.

The question is whether the gap structure of the T⁶
spectrum constrains which modes can absorb intermediate
energy and which are left isolated.

Compute:

a) For each mode below 2 GeV, find the nearest mode
   with compatible quantum numbers (same sheet, charge
   conservation).  Record the energy gap Δm.  Are gaps
   large (isolated modes, stable) or small (dense
   clusters, easy transitions)?

b) Build the "decay cascade" for each ghost mode: if it
   decays to the nearest lighter compatible mode + photon,
   does the cascade terminate at a known particle or at a
   sub-electron ghost?  This extends Track 3 with explicit
   cascade paths.

c) For each known particle, identify its pair-production
   threshold (2m).  Is there always a T⁶ mode near 2m
   with the right quantum numbers to absorb the pair?
   The pion at ~280 MeV should sit near 2 × m_π — does
   the mode spectrum cooperate?

d) "Charge-preserving ladder": for the electron (1,2),
   the modes (1,3), (1,4), (1,5)... preserve charge
   while increasing mass.  Energy ratios:

       E(1,n₂)/m_e = √[ (1/r² + n₂²) / (1/r² + 4) ]

   Compute as a function of r.  How many levels fit in
   the [m_e, 2m_e) window?  Also compute the proportional
   harmonics (2,4), (3,6)... which have energy exactly
   k × m_e (shear cancels) but charge = −k.  These are
   pair-production channels, not excitation channels.

   Build the same ladder for the proton: modes
   (0,0,0,0,1,n₆) for n₆ = 3, 4, 5, ...  Compare to
   the nuclear scaling law (n₅=A, n₆=2A) — are nuclei
   occupying the proton's harmonic ladder?

e) Count the modes accessible within each energy window
   [m, 2m] for every known particle.  If the window is
   empty (no other modes available), the particle is
   "isolated" — energy above m has nowhere to go except
   R³ kinetic energy.  If the window is crowded, the
   particle can easily transition.  Does "isolated"
   correlate with "stable" and "crowded" with "unstable"?

**Output**: Gap distribution histogram.  Cascade trees for
ghost modes.  Charge-preserving ladder table (parametric
in r) for electron and proton.  Isolation index per known
particle vs observed lifetime.


### Track 6 — Spin-statistics selection rule

The WvM confined-photon derivation assigns spin ℏ × n₁/n₂
to a mode (n₁, n₂).  Only integer and half-integer spin
values correspond to physical particles.  If this formula
is correct, most ghost modes have fractional spin and are
forbidden by the spin-statistics theorem.

**Compute:**

a) For every T⁶ mode below 2 GeV (from R28 mode catalog),
   compute Spin = n₁/n₂ for the dominant sheet winding.
   Classify as integer, half-integer, or fractional.
   Count: how many modes survive vs. are killed?

b) Derive the angular momentum of the confined EM field for
   modes (1,1), (1,2), (1,3) on a sheared T².  Method:
   solve Maxwell's equations on the (L₁, L₂, s) torus,
   compute the angular momentum density J = ε₀(E × B), and
   integrate over the T² cell.  Does the total J give spin
   = n₁/n₂?  Or does shear modify the result?

c) Alternative derivation: treat the mode as a pair of
   winding numbers on a T².  The spin is the ratio of
   orbital periods.  For (n₁, n₂) on T² with aspect ratio
   r, the tube circuit takes time t₁ = L₁/c = 2πrL₂/c,
   the ring circuit takes t₂ = L₂ n₂/c.  The ratio
   t₁/(n₂ t₂) = r/n₂.  Does this give a different spin
   formula (aspect-ratio-dependent)?

d) Compare to the field-theoretic assignment (spin ½ per
   active sheet, regardless of winding).  In the R27/R28
   mode tables, spin was assigned per sheet.  Which
   assignment reproduces the observed particle spins?

e) For multi-sheet modes: if mode (n₁, n₂, n₃, n₄, n₅, n₆)
   has nonzero windings on two sheets, does spin add?  E.g.,
   the neutron has windings on electron and proton sheets.
   Does spin = ½ + ½ = 1 (wrong) or ½ (correct)?  The
   WvM formula needs a multi-sheet generalization.

**Output**: Table of all modes below 2 GeV with spin
assignment from both formulas (WvM and field-theoretic).
Count of modes surviving the spin-statistics filter.
Angular momentum integral results for benchmark modes.
If WvM spin eliminates most ghosts, this is a STRONG result.


### Track 7 — Aspect ratio scan for the prediction minimum

The spin filter (Track 6) leaves a dangerous survivor:
mode (1, 1) on the electron sheet is spin-1 (valid boson),
charge −1 (at KK zeroth order), and lighter than the
electron.  No such particle is observed.

The R19 charge integral computes effective charge from the
mode shape on a sheared T².  Crucially, this integral
depends on the aspect ratio r_e.  If Q(1, 1, r_e) = 0 at
some specific r_e, the mode is uncharged and invisible —
eliminating the most dangerous ghost AND pinning r_e.

**Compute:**

a) Evaluate the R19 shear-charge integral Q(n₁, n₂, r, s)
   for modes (1,0), (1,1), (1,2), (1,3) on the electron
   sheet across a dense grid of r_e values from 0.1 to 100.
   At each r_e, s is determined by α (solve_shear_for_alpha).
   Plot Q vs r_e for each mode.

b) Find zeros: at which r_e does Q(1,1) = 0?  Does Q(1,2)
   remain at −1 at that same r_e?  If both conditions hold
   simultaneously, r_e is pinned.

c) Define a "tension score" T(r_e): for each r_e, count the
   number of modes on the electron sheet below 2 GeV that
   are (i) charged (|Q| > 0.01), (ii) have valid spin
   (integer or half-integer per Track 6), and (iii) do not
   correspond to a known particle.  Plot T(r_e).  Find the
   minimum — this is the "prediction minimum" r_e where the
   model makes the fewest unexplained predictions.

d) Repeat (a)–(c) for the proton sheet.  The proton is
   mode (1, 2) on its T².  Mode (1, 1) on the proton sheet
   would be a charged spin-1 boson at ~half the proton mass
   (~470 MeV).  Does Q(1, 1, r_p) = 0 at r_p ≈ 6.6?

e) Apply the same analysis to the neutrino sheet.  The
   neutrino is uncharged (n₁ = 0 on the electron sheet),
   but modes with n₃ ≠ 0 on the neutrino sheet could carry
   "neutrino charge" (weak interaction analog).  Does the
   charge integral on the neutrino T² constrain r_ν?

f) If the prediction minimum exists and gives a unique r_e:
   compute the full mode spectrum at that r_e.  List every
   surviving mode (valid spin, nonzero charge) below 2 GeV.
   These are firm predictions — the model says they exist.
   Compare to the R28 particle catalog.

**Output**: Q(r_e) curves for benchmark modes.  Zeros of
Q(1,1,r_e).  Tension score T(r_e) plot with minimum
identified.  If r_e is pinned, the full predicted spectrum
at that r_e.  Repeat for proton sheet.

**Why this matters**: r_e has been a free parameter since
R19.  If the charge integral's r-dependence pins it, the
T⁶ model loses a free parameter and gains predictive
power.  Combined with Track 6 (spin filter), this could
reduce the electron-sheet ghost population to zero and
turn r_e from a free parameter into a prediction.


## What success looks like

- **Strong result**: Track 1 shows the charge integral
  naturally suppresses ghost modes by ~10⁵, explaining
  both the Lamb shift and running constraints from a
  single geometric mechanism.  The KK charge formula
  Q = −n₁ + n₅ is a zeroth-order approximation; the
  full integral adds mode-shape-dependent corrections
  that kill most modes.

- **Moderate result**: Track 3 shows all sub-electron
  charged modes are unstable (can decay to lighter
  uncharged modes + photons), and Track 2 shows most
  ghosts are unreachable from known-particle reactions.
  The ghosts are "real but irrelevant" — valid modes
  that nature never excites and that decay instantly
  if excited.

- **Concerning result**: Track 3 finds stable charged
  ghosts lighter than the electron with no decay channel.
  This would be a genuine tension requiring either a
  new selection rule or a modification to the charge
  mechanism.

- **Track 5 bonus**: The "isolation index" (how empty the
  energy window [m, 2m] is for each mode) correlates with
  observed particle stability.  Known stable particles sit
  in gaps; known resonances sit in crowds.  Ghost modes
  cluster in dense regions where rapid cascade drains them
  to known particles.  The harmonic ladder is scrambled
  enough that "harmonics" are not a distinct excitation
  channel — energy above m goes to R³ kinetic energy, not
  internal harmonics.  This would confirm that pair
  production is the only internal energy-release mechanism
  and that the mode spectrum's gap structure is itself a
  selection rule.

- **Track 6 + 7 combined strong result**: The spin filter
  (Track 6) kills most modes via fractional spin.  The
  charge integral scan (Track 7) finds r_e where the
  remaining dangerous modes (especially (1,1)) lose their
  charge.  Together, they eliminate all electron-sheet
  ghosts AND pin r_e — converting a free parameter into a
  prediction.  The same mechanism applied to the proton
  sheet pins r_p (currently ~6.6 from neutron fitting).
  If the two methods give consistent r_p values, this is
  a cross-check of the entire ghost selection framework.
