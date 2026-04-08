# R33. Ghost mode selection — why most Ma modes are dark

**Questions:** Q77 (coupling suppression), Q34 (charge mechanism)
**Type:** compute + theoretical  **Depends on:** R19, R27, R28, R31, R32
**Status:** Paused (3 tracks complete, 1 dead, 5 deferred)


## Motivation

The Ma (the six-dimensional material space) spectrum contains ~900 modes below 2 GeV, but only
~40 correspond to observed particles (R28 Track 2).  The
remaining ~860 are "ghost modes" — valid solutions of the
wave equation on Ma with definite mass, charge, and spin,
but no observed counterpart.

Two independent calculations demand that ghost modes are
electromagnetically suppressed by a factor of ~10⁵:

- **R31 Track 4**: Naive KK Yukawa corrections to the
  hydrogen Lamb shift exceed observation by 10⁵.
- **R32 Track 1**: Naive vacuum polarization from the Ma
  mode spectrum produces running of α that is 157,000×
  too fast, with a Landau pole at ~1 MeV.

Both results point to the same conclusion: ghost modes do
not couple to the electromagnetic field with the same
strength as known particles.  But neither explains WHY.

This study investigates the geometric mechanism behind ghost
mode suppression.

### Sheet-by-sheet focus

The three material sheets have different roles:

**Electron sheet (L₁ ~ fm, L₂ ~ fm):** The electron is
mode (1,2).  The question is why this mode dominates — why
don't other modes on this sheet appear as stable charged
particles?  The spin filter (Track 6) and charge integral
(Track 1) should explain this.

**Proton sheet (L₅ ~ fm, L₆ ~ fm):** The proton is mode
(1,2).  Same question: why does the fundamental dominate?
The proton sheet's shear and aspect ratio (r_p ≈ 6.6) are
pinned by the neutron mass, so the computation is more
constrained.

**Neutrino sheet (L₃ ~ 42 μm, L₄ ~ 210+ μm):** The
neutrino is mode (1,2).  Ghost modes on this sheet are
NOT a problem — they are the hypothesized storage medium
(Q85 §8, §12–13).  The neutrino sheet should have many
modes.  The question is only whether the fundamental
(1,2) is preferred as the ground state, not whether other
modes are suppressed.

This study focuses primarily on the electron and proton
sheets.  Neutrino-sheet modes are investigated only in
Tracks 5 and 7(e), and there the goal is characterization
(what modes exist) rather than elimination.


## Prior results

- **R19**: The R19-shear-charge formula derives α from an
  integral over the torus surface.  The integral depends
  on the full mode shape, not just n₁.
- **R27 F37–F42**: Lifetime-gap correlation (r = −0.84)
  suggests observed particles are off-resonance
  excitations, not exact Ma eigenmodes.
- **R28 Track 2**: ~900 modes below 2 GeV, ~20× more than
  known particles.  Proton energy ladder (52 MeV steps)
  dominates the spectrum.
- **R31 Track 4**: KK massive mode coupling suppressed by
  ≥10⁵ (from Lamb shift).
- **R32 Track 1 F2**: 112 charged modes exist below the
  electron mass (0.511 MeV).  The lightest charged mode
  is at 39 keV — 13× lighter than the electron.


## Key questions

1. Does the R19-shear-charge integral naturally suppress
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
6. Does the energy gap structure of the Ma spectrum
   (spacing between modes, pair-production ceilings,
   harmonic ladders) create natural stability islands
   that correlate with known particles?


## Approach: 8 tracks

### Track 1 — Charge integral per mode (electron and proton sheets)

The R19-shear-charge formula derives α from a surface
integral over the electron sheet.  The integral assumes the
(1,2) mode shape.  Generalize it to all modes on both the
electron and proton sheets.

For each mode (n₁, n₂) on Ma_e:

    Q_eff(n₁, n₂) = ∫∫ [EM flux from mode (n₁,n₂)] dA

The KK formula says Q = −n₁, independent of n₂.  The WvM
integral may give a different (suppressed) result for
modes other than (1,2).

**Compute separately for each sheet:**

a) **Electron sheet:** Q_eff(n₁, n₂) for |n₁| ≤ 8,
   |n₂| ≤ 8.  Use r_e = 6.6 (default) and s₁₂ from
   solve_shear_for_alpha(r_e).  Does Q_eff select (1,2)?
   What about (1,1) — the dangerous spin-1 mode?

b) **Proton sheet:** Q_eff(n₅, n₆) for |n₅| ≤ 8,
   |n₆| ≤ 8.  Use r_p = 6.6 and s₅₆ from the proton
   self-consistent metric.  Does the same mechanism that
   selects the electron also select the proton?

c) **Cross-sheet modes** (e.g., neutron (1,2,0,0,1,2)):
   how does the charge integral behave when both sheets
   are active?  The neutron has Q = 0 by n₁ − n₅ = 0.
   Do cross-sheet ghosts have anomalous charge?

The question is not whether all ghosts have zero charge,
but whether the fundamental (1,2) is PREFERRED — does it
have the largest |Q_eff| among all modes?  A preference
hierarchy (strong fundamental, weakly coupled ghosts)
explains both the dominance of known particles and the
~10⁵ suppression.

**Output**: Table of Q_eff / Q_KK for each mode on each
sheet.  Rank ordering by |Q_eff|.  Identification of the
preference hierarchy.

**Result (Complete):**  The n₁ = ±1 selection rule kills 88%
of modes.  Among survivors, coupling scales as 1/(n₂-s)²,
ENHANCING low-n₂ modes (not suppressing them).  Combined
with the spin filter (Track 6 preview: spin = n₁/n₂), only
4 modes survive per sheet: (1,±1) spin-1 bosons and (1,±2)
spin-½ fermions.  The (1,1) boson has 2× electron coupling
at half the mass — the critical remaining ghost.  The charge
integral CANNOT pin r_e: Q(1,1) is nonzero for all s ≠ 0.
See findings F1–F8.


### Track 2 — Quantum number reachability

Starting from the known stable particles (e, p, ν) and
their antiparticles, determine which Ma modes are
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

Each Ma mode has a fixed rest energy.  For fermions
(spin-½), Pauli exclusion limits occupancy to 1 particle
per quantum state.  At energy 2m, a particle–antiparticle
pair can be created — this is the pair-production ceiling.

Between m and 2m, additional energy goes to either S (the three spatial dimensions)
kinetic energy (momentum) or excitation of a DIFFERENT Ma
mode.  The charge-preserving excitations (1, n₂) for
n₂ = 3, 4, 5, ... on the electron sheet keep charge = −1
while increasing mass.  These form the "harmonic ladder"
(see Q85).  Their spacing depends on the free parameter r.

The question is whether the gap structure of the Ma
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
   threshold (2m).  Is there always a Ma mode near 2m
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
   S kinetic energy.  If the window is crowded, the
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

a) For every Ma mode below 2 GeV (from R28 mode catalog),
   compute Spin = n₁/n₂ for the dominant sheet winding.
   Classify as integer, half-integer, or fractional.
   Count: how many modes survive vs. are killed?

b) Derive the angular momentum of the confined EM field for
   modes (1,1), (1,2), (1,3) on a sheared material sheet.  Method:
   solve Maxwell's equations on the (L₁, L₂, s) torus,
   compute the angular momentum density J = ε₀(E × B), and
   integrate over the material sheet cell.  Does the total J give spin
   = n₁/n₂?  Or does shear modify the result?

c) Alternative derivation: treat the mode as a pair of
   winding numbers on a material sheet.  The spin is the ratio of
   orbital periods.  For (n₁, n₂) on a material sheet with aspect ratio
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


### Track 8 — Wave-optics coupling through the shear aperture

Track 1 uses a geometric (Fourier) charge integral that
gives coupling ∝ 1/(n₂ − s)².  This ENHANCES the (1,1)
ghost relative to the electron.  But the shear creates a
physical aperture of width δ = s × L₂ ≈ 0.01 L₂, and all
modes are deeply sub-wavelength relative to this aperture:

    (1,1): ring wavelength = L₂,   aperture/λ = 0.01
    (1,2): ring wavelength = L₂/2, aperture/λ = 0.02

In sub-wavelength optics (Bethe's theory), transmission
through an aperture scales as (d/λ)⁴.  Under this scaling,
the (1,1) ghost couples 16× WEAKER than the electron —
flipping the hierarchy found in Track 1.

The question is whether the Bethe scaling applies to the
Ma/S coupling, or whether the geometric charge integral
is the correct physics.

**Compute:**

a) Model the shear as a sub-wavelength slit of width
   δ = s × L₂ connecting a 2D cavity (a material sheet) to a 3D space
   (S).  Solve Maxwell's equations for the radiation
   emitted by mode (1, n₂) through this slit.  Compute the
   transmitted power as a function of n₂.

b) Compare the transmitted power scaling to:
   - Geometric integral: P ∝ 1/(n₂ − s)²
   - Bethe (aperture): P ∝ (s × n₂)⁴ ∝ n₂⁴
   - Intermediate: some power law P ∝ n₂^β

   What is the actual exponent β?

c) If β > 0 (Bethe-like), compute the coupling ratio for
   the critical modes:

       α_eff(1,1) / α_eff(1,2) = ?

   If < 1, the (1,1) ghost is suppressed.  How much
   suppression?  Is it enough to explain non-observation?

d) Extend to the proton sheet.  Same shear, different
   circumferences.  Does the proton's (1,1) ghost at
   ~470 MeV get suppressed by the same mechanism?

e) Physical picture: the shear aperture acts as a high-pass
   filter on the ring wavelength.  Modes with long ring
   wavelength (low n₂) are "too big to fit through the
   gap."  Modes with short ring wavelength (high n₂) pass
   easily.  The electron (n₂ = 2) is the lowest mode that
   couples efficiently.  (1,1) is below the cutoff.

   Compute the effective cutoff n₂* where the Bethe
   suppression equals 10⁻⁵ (the empirical ghost
   suppression factor from R31/R32).  Is n₂* ≈ 1?

**Output**: Transmitted power vs n₂ for both geometric and
wave-optics treatments.  Coupling ratio α(1,1)/α(1,2).
Effective cutoff frequency.  If the aperture mechanism
suppresses (1,1), this resolves the last remaining ghost
tension on the charged sheets.

**Why this matters**: The geometric charge integral is a
zeroth-order calculation that ignores the wave nature of
the coupling.  The shear aperture is ~100× smaller than the
mode wavelength — deeply in the regime where wave optics
dominates.  A Bethe-like suppression would naturally explain
why only n₂ ≥ 2 modes are observed, without needing the
spin filter at all.  It would also explain the ~10⁵ ghost
suppression factor from a single geometric parameter (s).

**Result (Complete):** The aperture sinc effect is negligible
(all modes are equally sub-wavelength).  BUT the ω⁴ Larmor
radiation factor provides 16× suppression of (1,1) relative
to (1,2): lower-energy modes radiate less efficiently.  Three
of four models tested show low-n₂ suppression; the geometric
integral is the outlier.  The net observable coupling
(charge × radiation) gives (1,1) at ~1/8× the electron.
Critical caveat: ω⁴ is classical Larmor — whether it applies
to the Ma/S coupling requires a QFT vertex calculation.
See findings F9–F14.


### Track 9 — Coulomb fission of harmonic electron modes

**Note:** Track 9 was added after R51 (atoms as compound
tori modes), where the question of multi-electron mode
stability arose naturally from the atomic shell discussion.

Tracks 1–8 address modes with different winding ratios:
(1,1), (1,3), etc.  Track 9 asks a complementary question
about the *harmonic series* — modes (n, 2n) for n ≥ 2 that
have the same tube-to-ring ratio as the electron but at
higher winding numbers.  These are "(2,4) = two electrons
wound together," "(3,6) = three," etc.

**Why they don't exist as free particles:**

1. **Coulomb fission:**
   A (n, 2n) mode carries n quanta of electron energy.
   Under KK charge (Q = -n), the Coulomb self-energy of n
   like charges confined to the mode's Compton radius makes
   the composite strictly higher-energy than n separated
   (1,2) modes.  No confining force exists on Ma_e (only EM
   at strength α ≈ 1/137), so the composite fissions into
   individual electrons.

2. **Reducibility (the deeper reason):**
   The (n, 2n) mode has gcd(n, 2n) = n, so it decomposes
   into n copies of the (1,2) electron at different phases
   (strands).  Each strand is a valid, independently
   propagating mode.  There is nothing to prevent separation
   — and Coulomb repulsion actively drives it.

**Note on the charge formula (F16):**
The WvM integral (F1) gives Q = 0 for |n₁| ≥ 2, which would
make these modes dark.  But the KK formula gives Q = -n, and
the R29 nuclear scaling law uses modes with n₅ >> 1 on Ma_p
(nuclei) that clearly carry charge.  The charge formula for
multi-quantum modes is not settled.  The Coulomb fission
argument does not depend on this — it applies under either
charge assignment.

**Contrast with the proton (1,3) on Ma_p:**
The proton mode (1,3) has gcd(1, 3) = 1 — it is irreducible.
Its three-fold structure (three antinodes at 0°, 120°, 240°)
consists of features of one standing wave, not independent
sub-modes.  You cannot peel an antinode off a wave.  This
is why confinement is automatic for (1,3): there are no
strands to separate.

Additionally, the proton sheet's internal coupling is at the
full EM field strength (~1), not the α-attenuated coupling
(~1/137) seen through the Compton window in S (Q95).  The
"strong force" is the internal Ma field seen at torus-overlap
distance — Ma-physics, not S-physics.

| | Electron harmonics | Proton (1,3) |
|:---|:---:|:---:|
| Mode | (n, 2n), n ≥ 2 | (1, 3) |
| gcd | n (reducible) | 1 (irreducible) |
| Sub-parts | n strands of (1,2) | 3 antinodes |
| Strands separable? | YES | NO (not modes) |
| Internal coupling | α ≈ 1/137 (repulsive) | ~1 (Q95, attractive) |
| Fission? | Always (Coulomb wins) | Never (no strands) |

**Contrast with atoms:**
Multi-electron configurations exist in atoms because the
nucleus provides external Coulomb confinement.  Remove the
nucleus and the electrons fly apart.  This is precisely the
3D spatial physics of the "two-tier picture": Ma defines
particle identity, S defines spatial binding.

**Compute:**

a) Mode mass of (n, 2n) harmonics: verify E(n,2n) = n × m_e
   (exact for proportional windings on a sheared torus).

b) Coulomb self-energy at the reduced Compton wavelength
   ƛ_C/n: E_self = n(n-1)/2 × α ℏc / (ƛ_C/n).

c) Energy balance: ΔE = E_self > 0 for all n ≥ 2 (separated
   state is always lower energy).

d) Proton contrast: irreducibility argument + internal coupling
   strength (Q95: strong force = internal Ma field).

e) Atomic contrast: measured total ionization energies vs
   electron self-repulsion at Bohr radius.

**Output**: Tables of mode mass, self-energy, energy balance.
Mode reducibility analysis.  Atomic confinement ratios.

**Result (Complete):** Both mechanisms independently prevent
free (n, 2n) harmonics.  Coulomb fission energy grows as
~n³ × α m_e — from 7.5 keV at n=2 to 1.7 MeV at n=10.
The proton (1,3) is stable because it is irreducible (gcd = 1)
and its internal coupling is at the full Ma field strength, not
the α-attenuated Coulomb.  Atoms are stable because nuclear
attraction exceeds electron self-repulsion by 2.5–5×.
See findings F15–F20.


### Track 7 — Aspect ratio scan for the prediction minimum  **DEAD (F8)**

The spin filter (Track 6) leaves a dangerous survivor:
mode (1, 1) on the electron sheet is spin-1 (valid boson),
charge −1 (at KK zeroth order), and lighter than the
electron.  No such particle is observed.

The R19 charge integral computes effective charge from the
mode shape on a sheared material sheet.  Crucially, this integral
depends on the aspect ratio r_e.  If Q(1, 1, r_e) = 0 at
some specific r_e, the mode is uncharged and invisible —
eliminating the most dangerous ghost AND pinning r_e.

**Compute:**

a) Evaluate the R19-shear-charge integral Q(n₁, n₂, r, s)
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
   mode (1, 2) on Ma_p.  Mode (1, 1) on the proton sheet
   would be a charged spin-1 boson at ~half the proton mass
   (~470 MeV).  Does Q(1, 1, r_p) = 0 at r_p ≈ 6.6?

e) Apply the same analysis to the neutrino sheet.  The
   neutrino is uncharged (n₁ = 0 on the electron sheet),
   but modes with n₃ ≠ 0 on the neutrino sheet could carry
   "neutrino charge" (weak interaction analog).  Does the
   charge integral on Ma_ν constrain r_ν?

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
Ma model loses a free parameter and gains predictive
power.  Combined with Track 6 (spin filter), this could
reduce the electron-sheet ghost population to zero and
turn r_e from a free parameter into a prediction.


## What success looks like

- **Strong result**: Track 1 shows the charge integral
  gives a clear preference hierarchy: (1,2) has the
  largest |Q_eff| on both the electron and proton sheets.
  Other modes are suppressed by ~10⁵, explaining both
  the Lamb shift and running constraints from a single
  geometric mechanism.  The KK formula Q = −n₁ is a
  zeroth-order approximation; the full integral adds
  mode-shape-dependent corrections that suppress ghosts.
  The same hierarchy appears independently on both sheets,
  explaining why one particle dominates per sheet.

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
  to known particles.

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

- **Neutrino sheet (not a problem)**: Dense neutrino-sheet
  modes in [m_ν, 2m_ν] are a FEATURE, not a bug — they
  are the hypothesized information storage medium (Q85).
  Success here means confirming that the fundamental
  (1,2) neutrino is the ground state (lowest-energy
  spin-½ mode) while many higher modes exist.  If the
  neutrino sheet has only a few modes, storage capacity
  is limited and the Reiter model may need to be a
  hybrid of continuous + quantum mechanisms.


## Current status — Paused

### Completed
- **Track 1** (charge integral): 8 findings (F1–F8).
  n₁ = ±1 kills 88%.  Spin filter → 4 survivors per sheet.
  (1,1) ghost has 2× charge — tension.
- **Track 8** (wave-optics): 6 findings (F9–F14).
  ω⁴ Larmor suppression gives (1,1) ~1/8× electron coupling.
  Classical caveat remains.
- **Track 9** (harmonic fission): 6 findings (F15–F20).
  (n, 2n) harmonics are both dark (by F1) and Coulomb-unstable.
  No free multi-electron modes.  Proton (1,3) stable by
  irreducibility (gcd = 1) + full Ma coupling (Q95).

### Dead
- **Track 7** (r_e scan): killed by F8.  Q(1,1) ≠ 0 for all s.

### Deferred
- **Track 6** (spin derivation): highest-value remaining track.
  If spin ≠ n₁/n₂, the entire ghost landscape changes.
- **Tracks 2–5**: cleanup tracks, reduced urgency given the
  strong results from Tracks 1 + 8.

### Key open question
Does the ω⁴ radiation efficiency survive a QFT vertex
calculation?  If yes, (1,1) is suppressed 8× and the ghost
problem is essentially solved for charged sheets.  If no,
(1,1) remains a genuine tension at 2× electron coupling.
