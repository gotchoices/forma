# R52: Anomalous magnetic moment from torus self-field

**Status:** Reopened — Track 4d positive (partial).  Tracks 1, 2, 4a, 4b, 4c (no shear) failed; Track 4d (with shear) shows mode-dependent sign-flip behavior in (1,3) at s ≳ 0.020 (resolution-converged).  The (1,2) mode does not flip.  Whether the proton's actual effective shear reaches this threshold is the open question.  Track 4e (vector + shear) and a deeper investigation of proton effective shear are the natural next steps.

**Physical principle (per discussion):**
- Charge is an artifact of trips around the **tube** (poloidal n_tube): integer-quantized in clean steps, no fractional adjustment.
- Magnetic moment is an artifact of trips around the **ring** (toroidal n_ring): can be modified by **shear** (a non-integer non-linearity) that introduces small additive or subtractive corrections.
**Questions:** Q53 (anomalous magnetic moment), Q103 (defect-cost back-reaction)
**Type:** compute
**Depends on:** R44 (negative result — charge-mass separation wrong sign/order),
R45 (magnetic moments — cross-sheet dressing viable), R46/R47 (slot mechanism,
proton filter), R33 Track 9 (mode stability / irreducibility)

---

## Motivation

Q103 identifies the anomalous magnetic moment as the **back-reaction of the
Coulomb self-field on the circulating wave**.  The particle's own charge
creates an electric field that acts back on the current, distorting it.
For the electron this gives g − 2 ≈ α/π.  Q103 provides the physical
picture but no computation.

R44 tested a specific mechanism — the R19 shear-induced charge density
σ(θ₁, θ₂) — and found it wrong sign, order 1.  That mechanism was about
the *non-uniform projection* of charge into 3D, not about the self-field
back-reaction.  **The direct Coulomb self-interaction of a charged torus
mode has never been computed in this project.**

Meanwhile, a striking observation about the (1,3) proton hypothesis:

| Particle | Mode | MaSt bare | Measured | Residual |
|----------|------|-----------|----------|----------|
| Electron | (1,2) | 2 μ_B | 2.00232 μ_B | **+0.12%** |
| Proton   | (1,3) | 3 μ_N | 2.793 μ_N   | **−6.9%** |

The electron residual is **additive** (moment larger than bare).
The proton residual is **subtractive** (moment smaller than bare).

> **Baseline note.**  The MaSt bare moment is μ = n₂ × magneton —
> a framework-specific prediction from angular momentum
> quantization on the torus.  For the electron this happens to
> match the Dirac value (g = 2), so MaSt and standard physics
> agree on the baseline AND on the anomaly to explain.  For the
> proton, MaSt predicts 3 μ_N (from n₂ = 3) while standard physics
> predicts 1 μ_N (Dirac for a point particle).  The standard
> proton "anomaly" relative to Dirac is +179%; the MaSt residual
> relative to 3 μ_N is −6.9%.  R52 is computing the deviation
> from MaSt's own baseline, not the standard anomaly.

**Hypothesis:** the sign of the anomaly is determined by the mode's
**phase structure**:

- **(1,2) — single phase:** two antinodes 180° apart (positive and
  negative halves of one cycle).  The self-field back-reaction is
  constructive — it "puffs out" the effective current loop, increasing
  the moment.

- **(1,3) — three phase:** three antinodes at 120° spacing.  The
  self-fields from the three antinodes partially cancel at each other's
  locations (analogous to zero neutral current in a balanced three-phase
  system).  The inter-antinode repulsion smears the charge distribution,
  reducing peak-to-valley contrast and decreasing the moment.

If the same self-field mechanism produces **+α/(2π) for the electron**
and **≈ −7% for the proton**, from nothing but the mode numbers and
torus geometry, that would be a powerful confirmation that the anomalous
moment is geometric.

---

## What R44 ruled out (and what this study does differently)

R44 computed the magnetic moment from R19's shear-induced charge density
σ(θ₁, θ₂) on the flat torus.  The local charge pattern from the shear
mechanism is an oscillating cos() function — an order-1 distortion, not
a small perturbation.  This gave μ_actual/μ_uniform − 1 ≈ −1.6 to −2.4:
wrong sign, ~1400× too large.

**This study takes a different approach:** it computes the 3D Coulomb
self-potential of a charged torus mode — the physical self-interaction
of the embedded charge distribution in 3D space — and uses it as a
perturbation to the wave equation on the torus.

The key difference:
- R44's charge distribution comes from the R19 shear formula (flat-torus
  intrinsic effect, order 1).
- R52's perturbation comes from the Coulomb self-energy of the 3D
  embedding (external field effect, order α).

We already have the infrastructure: `lib/embedded.py` provides
`EmbeddedSheet`, `charge_segments`, `field_energy`, and `potential_at`.

---

## Physical picture

A (n₁, n₂) mode on a torus carries charge Q distributed along the
(n₁, n₂) geodesic.  When embedded in 3D as a torus of revolution
(major radius R, minor radius a = r × R), this charge distribution
creates a Coulomb field in the surrounding space.

The Coulomb field has energy U_C = α × mc² (the defect cost).  It also
generates a potential V(θ₁, θ₂) on the torus surface itself.  This
potential is NOT uniform because the 3D distances between surface
elements depend on where you are on the torus:

- **Outer equator** (θ₁ = 0): farther from most of the torus → lower V
- **Inner equator** (θ₁ = π): closer to opposite side → higher V

The dominant Fourier component of V(θ₁) is cos(θ₁), which mixes the
(n₁, n₂) mode with (n₁ ± 1, n₂) modes.  This changes the angular
momentum composition, and hence the magnetic moment.

For a **(1,2) mode**: mixing with (0,2) and (2,2).  The (0,2) mode is
uncharged (n₁ = 0) and carries pure ring angular momentum.  Mixing in
(0,2) adds angular momentum without subtracting charge → increases μ/S.

For a **(1,3) mode**: mixing with (0,3) and (2,3).  The three-fold ring
symmetry creates cross-coupling between the antinodes' self-fields,
partially cancelling the constructive effect → net subtractive.

---

## Bare moment — what is known

The bare magnetic moment is a quantum result from angular momentum
quantization: μ = eℏn₂/(2m) = n₂ × magneton.  For the electron,
g = 2 (from the Dirac equation / WvM spin-statistics); for the (1,3)
proton, μ = 3μ_N (from the three-fold ring winding).  These values
are topological — they depend only on the winding numbers and
charge-to-mass ratio, not on the torus geometry.

No surface integral or B-field computation is needed for the bare
moment.  (Track 1 attempted this and confirmed that classical
current-loop integrals on the embedded torus give geometry-dependent
answers 10–100× larger than the quantum prediction.  See findings.)


## Tracks

### Track 1: Classical current-loop integral — MISGUIDED

Script: `scripts/track1_bare_moment.py` (kept for reference)

Attempted to verify bare moments from the 3D current-loop integral
∮ r × dl.  Found this integral scales as R² (torus area), giving
results 8–800× larger than the quantum prediction.  This confirmed
that the bare moment is purely quantum (angular momentum quantization),
not derivable from a classical field integral on the embedded torus.
See findings F1–F2.

**The computation was valid but the goal was misguided** — there is
no non-trivial "bare moment computation" to perform.  The bare values
(g = 2 for electron, 3μ_N for proton) are axiomatic inputs from the
Dirac equation / winding-number quantization.  The interesting physics
is the self-field CORRECTION, which is the subject of Tracks 2–4.


### Track 2: B-field surface integral — NEGATIVE RESULT

Script: `scripts/track2_bfield_distribution.py`

Adapted the R48 E-field charge integral technique to the B field,
computing B at every point on the torus surface for both traveling-
wave and standing-wave CP models.

**Result: NEGATIVE.**  Both formulations give corrections that are
the same sign (positive/additive) for all (1, n₂) modes:

- Traveling wave: B_z = −n₂ρ/|k| is constant in θ₂ (no +/−
  cancellation).  The Poynting angular momentum integral gives
  δμ/μ ≈ +ε²(1 − 1/n₂²)/2 — always positive.

- Standing wave: B has +/− regions from sin(q_eff θ₂), but the
  θ₂ integral is killed by orthogonality except for a shear
  residual ∝ s²/n₂.  The residual is positive for both modes
  (2.2×10⁻⁴ for (1,2), 1.7×10⁻⁴ for (1,3) at s = 0.01).

The sign difference between g − 2 > 0 (electron) and μ − 3μ_N < 0
(proton) does NOT emerge from the single-sheet B-field integral.
See findings F3–F6.


### Track 3: Perturbative moment correction — ABANDONED

**Goal (original):** Compute first-order correction to the magnetic
moment from the self-potential V via standard quantum perturbation
theory.

**Why abandoned:** Tracks 1 and 2 together demonstrate that the
problem is structural, not computational:

1. Track 1 showed that the bare moment is purely topological
   (μ = n₂ × magneton from flux quantization), with no role for
   classical 3D current loops.
2. Track 2 showed that quadratic field measures (|B|² over the
   surface) cannot produce sign-dependence between (1,2) and (1,3).
3. Standard quantum perturbation theory of "particle in its own
   self-potential" is not how QED computes g − 2 — that
   calculation uses loop diagrams, not self-potential
   perturbations, and the naive perturbation approach
   double-counts the self-interaction.

Track 3 would have been a borrowed application of standard QM
machinery to MaSt's geometry — a consistency check that, even if
positive, would not constitute a genuine MaSt derivation.  Given
that Track 2 has already shown the fundamental obstacle (quadratic
measures can't produce sign-dependence), running Track 3 would
burn computational effort on a calculation that cannot test the
central hypothesis.

**Replacement:** the central question (does the sign of the
residual anomaly correlate with mode topology?) is moved to
Track 4, which uses a coherent (non-quadratic) field calculation
specifically designed to be sensitive to the predicted phase
structure.


### Track 4: Sign rule test (multiple sub-experiments)

**Goal:** Find any consistent set of assumptions under which
the self-interaction calculation reproduces the sign pattern
observed in nature: additive correction for n₂ = 2 (electron)
and subtractive correction for n₂ = 3 (proton).

**Hypothesis under test (from Q103 §7):**

> The sign of the residual anomaly is determined by the
> n₂-fold spatial winding structure of the mode:
>
> - **n₂ = 2 (two-phase):** two-fold winding → constructive
>   self-field overlap → additive correction (δμ > 0)
>
> - **n₂ = 3 (three-phase):** three-fold winding → 120°-offset
>   self-field overlap → destructive interference → subtractive
>   correction (δμ < 0)

**Scope statement.**

We are NOT trying to derive the exact magnitude of the
anomalous moment.  That is an S-domain calculation (textbook
QED for the electron, lattice QCD for the proton) and MaSt is
unlikely to add value to those existing computations.

We ARE trying to show that **the sign of the correction is
predictable from the mode's tube-winding topology** — a
structurally new piece of physics that has no analog in
standard QED+QCD.  If we can demonstrate this with a simple,
defensible calculation, that alone is a significant result.
Magnitudes and exact derivations can come later.

**Why sub-experiments.**

The self-interaction of a torus mode can be modeled in
several inequivalent ways.  Each makes different assumptions
about what the "self-interaction function" is and how the
antinodes contribute.  We don't know in advance which model
is the physically correct one for MaSt — and the simpler
models may or may not produce the predicted sign pattern.

Rather than guessing, Track 4 runs multiple sub-experiments,
each with a clearly stated set of assumptions, and checks
whether any of them reproduces the sign pattern.  A positive
result in ANY sub-experiment is informative; a negative
result in ALL of them effectively falsifies the three-phase
rule.

**Common assumptions across all sub-experiments:**

1. **Standing wave basis.** ψ(θ₁, θ₂) = cos(n₁θ₁) × cos(n₂θ₂),
   real-valued.  This is a basis choice — the flat torus has
   a 4-dimensional eigenspace (cos·cos, cos·sin, sin·cos,
   sin·sin) that is degenerate in energy.  We pick cos·cos
   and document it.  An "antinode" at θ_k means a maximum
   of |ψ| at that location; adjacent antinodes alternate
   sign.

2. **Antinode positions.** For the (1, n₂) mode, the antinodes
   in the tube direction are at θ₂_k = k × π/n₂ for
   k = 0, 1, ..., 2n₂ − 1.  Adjacent antinodes have signs
   s_k = (−1)^k.  So a (1,2) mode has 4 antinodes with
   signs ++−− around the tube; a (1,3) mode has 6 antinodes
   with signs +−+−+−.

3. **Embedded geometry.** The torus is embedded in 3D with
   major radius R, minor radius a = r × R.  Inter-antinode
   distances are computed as **chord distances** through 3D
   space, not along the surface (the field from one antinode
   to another propagates through space).

4. **Aspect ratio.** For the electron, scan r_e ∈ [0.5, 20].
   For the proton, use r_p = 8.906 (pinned by R27).

5. **Output format.** For each sub-experiment, report:
   - Total self-interaction quantity for n₂ = 2 and n₂ = 3
   - SIGN of each
   - Whether the sign pattern matches the prediction (+ for
     n₂ = 2, − for n₂ = 3)
   - Optionally: same calculation for n₂ = 1, 4, 5, 6 to
     test generalization

#### Sub-track 4a: Pairwise antinode Coulomb energy

**Hypothesis.** The antinode self-interaction is captured by
treating each antinode as a point charge with sign equal to
the local sign of ψ, and summing pairwise Coulomb energies.

**Computation:**

1. Place 2n₂ point charges at antinode positions
   θ₂_k = k × π/n₂, on a representative tube cross-section
   (θ₁ = 0).
2. Assign each charge sign s_k = (−1)^k.
3. Compute pairwise Coulomb sum:

   > U = ½ Σ_{i ≠ j} (s_i × s_j) / d_{ij}

   where d_{ij} is the chord distance through 3D space.
4. Compare U(n₂ = 2) and U(n₂ = 3).

**Estimated complexity:** very low (~50 lines, runs in seconds).

**Risk:** the simplest pairwise picture is dominated by
nearest-neighbor opposite-sign pairs, which gives same-sign
(negative) U for both modes.  This sub-track may need
refinement (weighting pairs by 1/d^k for different k) before
it differentiates them.

#### Sub-track 4b: Coaxial tube-loop mutual inductance

**Hypothesis.** Each "tube winding" is a current loop in 3D
space.  The n₂ loops sit at different positions around the
ring direction.  The mutual inductance between loops
determines whether their fields reinforce (additive) or
oppose (subtractive).

**Computation:**

1. Treat the n₂ tube loops as closed circular current loops
   in 3D, each at a different ring angle θ₁_k = k × 2π/n₂.
2. All loops carry the same current direction (they all
   contribute to the bare angular momentum in the same sense).
3. Compute the n₂ × n₂ mutual inductance matrix using
   Neumann's formula:

   > M_{ij} = (μ₀ / 4π) ∮∮ (dl_i · dl_j) / |r_i − r_j|

4. Total inductance is L = Σ_i M_{ii} + Σ_{i ≠ j} M_{ij}.
   The off-diagonal sum is the inter-loop interaction.
5. Compute the ratio of off-diagonal to diagonal contribution
   for n₂ = 2 and n₂ = 3.

**Estimated complexity:** low (~100 lines, scipy elliptic
integrals for loop-loop inductance).

**Risk:** mutual inductance of identical co-circulating loops
is always positive, so this sub-track will likely give
same-sign for both modes unless circulation directions
encode mode parity.  Useful as a baseline showing what the
naive classical picture predicts.

#### Sub-track 4c: Continuous standing-wave self-energy

**Hypothesis.** The self-interaction is captured by treating
ψ(θ₁, θ₂) as a real-valued classical charge density (with
SIGNED values, not |ψ|²) and computing its Coulomb self-
energy by integration over the torus surface.

**Computation:**

1. Charge density: ρ(θ₁, θ₂) = q × cos(n₁θ₁) × cos(n₂θ₂),
   normalized so ∫|ρ| dA = total charge.
2. Compute self-energy by double integral over the embedded
   torus:

   > U_self = (1/2) ∫∫ ρ(r) ρ(r′) / |r − r′| dA dA′

   where r and r′ are 3D positions on the embedded surface,
   |r − r′| is the chord distance, and the integration is
   over both surface elements.
3. Use a softening length ε ~ 0.01a to handle the diagonal
   singularity at r = r′.
4. Compute U_self for (1,2) and (1,3) modes.

**Why this is different from 4a.** Instead of n discrete
antinodes, the entire continuous wave contributes.  The sign
comes from the cos·cos structure, which has + regions and
− regions of differing sizes for different n₂.

**Caveat.** "ρ = signed wavefunction" is a non-standard
choice — in QM, the charge density is |ψ|² × q (always
non-negative).  This sub-track is implicitly treating ψ as a
classical real field, not a quantum wavefunction.  The
verbal "function with + and − halves" argument implicitly
uses this picture.

**Estimated complexity:** moderate (~200 lines, double
integral over (θ₁, θ₂, θ₁′, θ₂′); can use Monte Carlo or
quadrature).

#### Sub-track 4d: Coherent vector-potential back-reaction (most ambitious)

**Hypothesis.** The back-reaction on the magnetic moment
comes from the angular momentum imparted by the self vector
potential A_self acting on the wavefunction.  This is the
closest classical analog to QED's vertex correction.

**Computation:**

1. Compute the polarization current ∂P/∂t for the standing
   wave ψ(θ₁, θ₂) cos(ωt).  A standing wave has zero net DC
   current, but its time-derivative has nonzero spatial
   structure with antinodes at the same locations as the
   charge density.
2. Compute A_self via Biot-Savart from the polarization
   current.
3. Compute the back-reaction angular momentum:

   > δL = ∫ ψ*(r) (r × A_self(r)) ψ(r) dA

4. Time-average over the oscillation cycle.
5. Moment correction: δμ = (e / 2m) × δL.
6. Compute δμ for (1,2) and (1,3).

**Why most ambitious.** It most closely tracks what a real
QED-like calculation would do.  But it requires careful
handling of the time-averaging and the curved-surface
Biot-Savart integral.

**Run only if 4a–4c are inconclusive.**

**Estimated complexity:** high (~500 lines; numerical
integration of vector fields on a curved surface).

#### Track 4 success criteria

The sub-experiments should be run in order of complexity:
4a → 4b → 4c → 4d (4d only if needed).  After each, evaluate:

| Outcome | Meaning |
|---------|---------|
| **Strong success:** any sub-experiment shows predicted sign pattern (+ for n₂=2, − for n₂=3) | Document the assumptions, stop sub-experiments.  This is the meaningful result. |
| **Weak success:** opposite signs but reversed (+ for n₂=3, − for n₂=2) | Topology determines sign with opposite convention.  Investigate basis-choice variants. |
| **Failure:** all sub-experiments give same-sign for both | Three-phase rule does not hold under simple classical models.  Either the rule is wrong, or it requires the lattice-native Track 5 to demonstrate.  Close R52. |


### Track 5: Lattice-native back-reaction (future)

**Status:** Not yet attempted; deferred to a possible follow-up
study.

If Track 4 produces the correct sign rule, the natural next
step is the lattice-native computation: propagate a (1, n₂)
mode on a discrete torus embedded in the GRID 4D Lorentzian
lattice, allow the wave to interact with its own radiated phase
field through the scattering rule, and measure the resulting
moment correction.  This would be a genuine first-principles
MaSt+GRID derivation, with no borrowed QM machinery.

This is a major computational project (likely more than R52
itself) and would constitute a separate study.  Track 4 is the
preliminary test that would justify undertaking it.

---

## What success looks like

| Outcome | Significance |
|---------|-------------|
| Any sub-experiment gives δg > 0 for (1,2) and δg < 0 for (1,3) | **Sign rule demonstrated** — phase structure determines anomaly direction.  Document the assumptions and stop. |
| Sign rule reproduced AND generalizes to n₂ = 4, 5, 6 | **Topological selection rule** for anomaly signs; predicts sign for any future particle from its mode topology |
| Bonus: magnitude of δg(1,2) is in the same order as α/(2π) | Suggests the classical model captures the right physics, not just the sign |

> **What MaSt is and is not claiming.**  MaSt does not need to
> reproduce the EXACT magnitude of g − 2 from first principles —
> standard QED already does that for the electron, and lattice
> QCD does it for the proton.  MaSt's contribution is to predict
> the SIGN of the residual anomaly from the mode's spatial
> topology, which neither QED nor QCD does.  If MaSt can supply
> a clean topological sign rule, the magnitude can be computed
> using existing S-domain tools (with MaSt providing the
> baseline μ = n₂ × magneton via flux quantization).  This is
> the structural division of labor: MaSt provides bare moment
> + sign rule from topology; S provides exact magnitudes from
> dynamics.

## What failure looks like

| Outcome | What it means |
|---------|--------------|
| All sub-experiments give same-sign δμ for n₂ = 2 and n₂ = 3 | Three-phase rule does not hold under simple classical models; either the rule is wrong, or it requires the lattice-native Track 5; close R52 |
| Sign rule holds for n₂ ∈ {2,3} but breaks for n₂ ∈ {4,5,6} | Two-particle coincidence rather than a general topological rule; weakly informative |
| Sign rule reverses (+ for n₂=3, − for n₂=2) | Sign convention is opposite expected; investigate basis-choice variants before declaring failure |

---

## Parameter strategy

**Electron sheet:**
- r_e: free parameter (scan range 0.5–20)
- s_e: determined by α(r_e, s_e) = 1/137.036 (from `ma.solve_shear_for_alpha`)
- Scale: L_ring from m_e = 0.511 MeV

**Proton sheet:**
- r_p = 8.906 (pinned by R27 F18, neutron + muon masses)
- s_p: determined by α(r_p, s_p) = 1/137.036
- Scale: L_ring from m_p = 938.3 MeV

**Coupling constants:**
- Electron: α ≈ 1/137 (perturbative regime)
- Proton: α_eff ~ 1/128 at GeV scale; internal coupling much stronger
  (Q95 — strong force as internal EM on Ma_p)

**Softening parameter (ε):**
- For Coulomb self-potential: scan ε from 0.1a to 0.01a to verify
  convergence.  The physical cutoff is the lattice spacing.

---

## Relationship to prior work

| Study | What it did | How R52 differs |
|-------|-------------|-----------------|
| R44 | Charge-mass separation from R19 shear → wrong sign, order 1 | Self-field of 3D embedding, not flat-torus shear distortion |
| R45 | Cross-sheet dressing (Track 3, viable but unexecuted) | Single-sheet self-interaction, no cross-sheet coupling |
| R46 | Slot/aperture mechanism → δμ/μ = α/(2π) for electron | Slots are geometric holes; R52 is electromagnetic back-reaction |
| Q103 | Physical picture (defect-cost back-reaction) | R52 computes what Q103 describes qualitatively |

**R52 is complementary to R45 Track 3.** If successful, it explains the
electron's anomaly (perturbative) and the sign of the proton's anomaly.
R45 Track 3 (full multi-sheet dressing) would be needed for the proton's
magnitude (non-perturbative regime).

---

## Files

| File | Description |
|------|-------------|
| `README.md` | This file — study design |
| `scripts/track1_bare_moment.py` | Track 1 (misguided) — classical current-loop integral |
| `scripts/track2_bfield_distribution.py` | Track 2 (negative) — B-field surface integral |
| `scripts/track4a_pairwise_coulomb.py` | Track 4a (negative) — pairwise antinode Coulomb energy |
| `scripts/track4b_loop_inductance.py` | Track 4b (negative) — coaxial tube-loop mutual inductance |
| `scripts/track4c_continuous_self_energy.py` | Track 4c (negative without shear) — continuous standing-wave self-energy |
| `scripts/track4d_continuous_with_shear.py` | Track 4d (positive) — continuous self-energy WITH shear; sign flip at s ≈ 0.020 |
| `scripts/track4e_vector_backreaction.py` | Track 4e (planned) — vector A_self back-reaction with shear |
| `findings.md` | Results and interpretation |

---

## Infrastructure

Uses existing `lib/` modules:
- `lib/embedded.py`: `EmbeddedSheet`, `charge_segments`, `field_energy`,
  `potential_at`, `field_at`
- `lib/ma.py`: `alpha_ma`, `solve_shear_for_alpha`, `mu_12`, `compute_scales`
- `lib/constants.py`: fundamental constants

No new library code anticipated — the existing embedded torus tools
provide everything needed.
