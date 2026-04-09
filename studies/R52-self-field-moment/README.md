# R52: Anomalous magnetic moment from torus self-field

**Status:** Framed — ready to compute
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

| Particle | Mode | Bare moment | Measured | Anomaly |
|----------|------|-------------|----------|---------|
| Electron | (1,2) | 2 μ_B | 2.00232 μ_B | **+0.12%** |
| Proton   | (1,3) | 3 μ_N | 2.793 μ_N   | **−6.9%** |

The electron anomaly is **additive** (moment larger than bare).
The proton anomaly is **subtractive** (moment smaller than bare).

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

## Tracks

### Track 1: Bare magnetic moment from torus-knot geometry

**Goal:** Verify that the 3D embedding of the (n₁, n₂) torus knot
current gives the expected bare magnetic moments: 2μ_B for the electron,
3μ_N for the proton.

**Computation:**
1. Construct `EmbeddedSheet` for electron and proton at their respective
   parameters (r_e, r_p, masses).
2. Generate the (1,2) and (1,3) geodesic current paths using
   `sheet.geodesic()`.
3. Compute the magnetic dipole moment μ_z = ½ ∮ (r × dl)_z × I, where
   I is the effective current from the circulating charge.
4. Compare μ with the topological prediction μ = n₂ × (eℏ/2m).
5. Scan across aspect ratio ε = a/R to verify the moment is topological
   (ε-independent in the intrinsic formula).

**Output:** bare μ_e, μ_p, and any ε-dependence of the 3D path integral.


### Track 2: Coulomb self-potential on the torus surface

**Goal:** Compute V(θ₁, θ₂) — the Coulomb potential at every point on
the torus surface due to the mode's own charge distribution.

**Computation:**
1. Distribute charge uniformly along the (n₁, n₂) geodesic using
   `charge_segments(N=2000)`.
2. For a grid of surface points (θ₁, θ₂), compute:
   V(θ₁, θ₂) = Σ dq_i / |r(θ₁, θ₂) − r_i|
   using `potential_at()` with softening ε > 0 to handle the
   self-potential singularity.
3. Decompose V into 2D Fourier components:
   V = Σ V_{k₁,k₂} exp(i(k₁θ₁ + k₂θ₂))
4. Identify the dominant harmonics.
5. Compute for both (1,2) on Ma_e and (1,3) on Ma_p.

**Key prediction:** The dominant perturbation is V_{1,0} (cos θ₁ from
inner/outer asymmetry), but the ring-dependent components V_{0,k₂} may
differ structurally between the two modes.

**Output:** Fourier spectrum of V(θ) for each mode and aspect ratio.


### Track 3: Perturbative moment correction — electron (1,2)

**Goal:** Compute the first-order correction to the magnetic moment from
the self-potential V.

**Computation:**
1. On the flat torus, modes are ψ_{n₁,n₂} = exp(i(n₁θ₁ + n₂θ₂))/(2π)
   with energies E_{n₁,n₂} = (ℏc/L)√(n₁²/r² + n₂²).
2. The perturbation Hamiltonian is H' = −eV(θ₁, θ₂).
3. First-order correction to the wavefunction:
   |δψ⟩ = Σ_{(m₁,m₂)≠(1,2)} ⟨m|H'|1,2⟩ / (E_{1,2} − E_{m₁,m₂}) × |m⟩
4. The perturbed state mixes in modes with winding numbers shifted by
   the Fourier components of V.
5. Compute the modified angular momentum:
   ⟨L₂⟩' = ⟨ψ + δψ | L̂₂ | ψ + δψ⟩
6. Extract δμ/μ = (⟨L₂⟩' − n₂ℏ) / (n₂ℏ).
7. Compare with α/(2π) = 0.001 161.

**Critical question:** does the perturbation give δg > 0 (correct sign)?

**Output:** δg(r_e) across the r_e family.  Target: δg ≈ +α/(2π).


### Track 4: Perturbative moment correction — proton (1,3)

**Goal:** Same computation as Track 3, but for the (1,3) proton mode
on Ma_p.

**Computation:**
1. Use proton sheet parameters (r_p = 8.906, mass 938.3 MeV).
2. Repeat the perturbation theory for (1,3).
3. The mode mixes with (0,3), (2,3), (1,2), (1,4), etc.
4. The three-fold ring symmetry means the Fourier structure of V differs
   from the (1,2) case — specifically, V_{0,3} and V_{0,6} components
   create inter-antinode self-coupling.
5. Extract δμ/μ.

**Critical question:** does the perturbation give δg < 0 (correct sign)?

**Caveat:** the proton is in the non-perturbative regime (Q103 §3).
First-order perturbation theory may underestimate the magnitude.  But
getting the correct **sign** from mode topology alone would be a
significant result.

**Output:** δg(r_p).  Target: δg < 0, ideally in the direction of
the measured −6.9%.


### Track 5: Phase-structure analysis and sign mechanism

**Goal:** Provide an analytical understanding of WHY (1,2) gives
additive and (1,3) gives subtractive corrections.

**Computation:**
1. Decompose the self-potential into mode-symmetric and mode-antisymmetric
   parts with respect to the n₂-fold rotational symmetry.
2. Analyze which mixing channels (which Fourier components of V)
   contribute to increasing vs decreasing the angular momentum.
3. For n₂ = 2: show that the dominant mixing preserves or increases
   L₂ → constructive.
4. For n₂ = 3: show that the three-fold cross-coupling between antinodes
   introduces destructive interference → subtractive.
5. Generalize: predict the sign for arbitrary (1, n₂) modes.
6. Check whether the sign rule matches the known magnetic moments of
   other particles (neutron as composite, muon as excited electron).

**Output:** analytical sign rule relating mode topology to moment
anomaly direction.

---

## What success looks like

| Outcome | Significance |
|---------|-------------|
| δg > 0 for (1,2), δg < 0 for (1,3) | **Sign confirmed** — phase structure determines anomaly direction |
| δg(1,2) ≈ α/(2π) at some r_e | **Magnitude match** — self-field is the right mechanism for the electron |
| δg(1,3) ≈ −0.07 at r_p = 8.906 | **Proton anomaly from geometry** — first non-QCD path to μ_p |
| Sign rule generalizes cleanly | **New selection criterion** — connects to R33 ghost selection |

## What failure looks like

| Outcome | What it means |
|---------|--------------|
| Wrong sign for either particle | Self-field mechanism is not the dominant effect; cross-sheet dressing (R45 Track 3) is likely responsible |
| Correct signs but wildly wrong magnitudes | Self-field sets the direction but not the scale; coupling strength enters through a different channel |
| V(θ₁, θ₂) is too uniform to perturb | The flat-torus limit kills the effect; curvature or shear is required |
| Perturbation theory diverges for proton | Expected (non-perturbative regime); signals need for full self-consistent solve (R45 Track 3) |

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
| `scripts/track1_bare_moment.py` | Bare magnetic moment from 3D torus-knot current |
| `scripts/track2_self_potential.py` | Coulomb self-potential V(θ₁,θ₂) on torus surface |
| `scripts/track3_electron_correction.py` | Perturbative moment correction for (1,2) |
| `scripts/track4_proton_correction.py` | Perturbative moment correction for (1,3) |
| `scripts/track5_phase_analysis.py` | Analytical sign rule from mode symmetry |
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
