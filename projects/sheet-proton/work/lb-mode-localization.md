# LB-mode localization test on the modulated-clover

**Status:** computational. Negative result. Sharpens
`work/derived-clover.md` gap (2) and the Reading α / Reading β
choice in `README.md`.

**Script:** [`scripts/track_localization.py`](../scripts/track_localization.py).

## The question

The Step-7 path-length formula

<!-- m = 2 π ℏ c / L_track -->
$$
m \;=\; \frac{2 \pi \, \hbar c}{L_\text{track}}
$$

treats each closed (1/2, 1) track as carrying a 1-D standing wave.
The Step-4 attempt to read the same mass from a 2-D
Laplace–Beltrami (LB) eigenvalue **failed**: no low-lying LB
eigenvalue lands on the proton / neutron mass.

This file asks the structural bridge question that connects them:
in the *semi-classical* (high-eigenvalue) regime, is there a
sequence of LB eigenmodes whose support concentrates on the
characteristic curves t(θ) = t₀ + θ/2 ?

A positive answer would say: the 2-D wave equation itself
produces 1-D-on-track wave packets in the WKB limit. The
path-length formula would then be a *consequence* of the 2-D
theory at high frequency, not a separate ansatz.

A negative answer would say: the 2-D theory does not reduce to a
1-D theory on the tracks. The path-length formula and the LB
spectrum then describe *different physics*, and the wave / track
reconciliation gap is **not** of the kind that closes under
semi-classical limits.

## Method

1. Build the Z₂ × Z₃-symmetric modulated-clover mesh using the
   Step-7 symmetric parameters
   (Ac₁ = -0.48765, As₁ = +0.65694, Bc₁ = -0.00038, Bs₁ = +0.00032,
   a₂ = 0.32994, b₂ = 0.03201, R_major = 36.17).

2. Compute K LB eigenmodes via `scipy.sparse.linalg.eigsh` using
   the cotangent-Laplacian L and lumped mass matrix M already
   used by Step 4. Solve L ψ = λ M ψ for the lowest K eigenpairs.

3. Build the characteristic-curve set: 6 t₀ values in [0, 2π)
   that are the (Z₂ × Z₃)-orbit of the proton seed t₀ = -π/6,
   each traced as t(θ) = t₀ + θ/2 for θ ∈ [0, 2π). Under the
   half-twist closure t₀ ~ t₀ + π these collapse to 3 distinct
   closed curves in 3-D.

4. Define a Gaussian tube weight in parameter space,
   w(v) = exp(-d(v)² / (2 σ²)), where d(v) is the (t, θ)-distance
   from vertex v to the nearest characteristic curve.

5. For each eigenmode ψᵢ compute the **enrichment**

   <!-- E_i = ⟨w⟩_{|ψ_i|²} / ⟨w⟩_uniform -->
   $$
   E_i \;=\; \frac{\langle w \rangle_{|\psi_i|^2}}{\langle w \rangle_\text{uniform}}
   \;=\; \frac{\sum_v m_v w_v \psi_{i,v}^2 / \sum_v m_v \psi_{i,v}^2}
              {\sum_v m_v w_v / \sum_v m_v}.
   $$

   E = 1 means a uniformly-spread mode; E > 1 means concentrated
   near the tracks; E equals the mode-resolved calibration value
   `E_perfect = ⟨w²⟩ / ⟨w⟩²` ≈ 3.0 (σ = 0.10) for a perfectly
   tube-confined mode (one with |ψ|² ∝ w).

## Numerical results

### Part A — individual-eigenmode enrichment

Runs (each from a clean execution of the script):

| K   | mesh (Nt × Nθ) | σ (rad) | tube fraction | max E | E_perfect | depth |
| --- | -------------- | ------- | ------------- | ----- | --------- | ----- |
| 60  | 80 × 80        | 0.10    | 0.235         | 1.025 | 3.0       | 0.012 |
| 300 | 120 × 120      | 0.08    | 0.188         | 1.046 | 4.4       | 0.014 |
| 400 | 120 × 150      | 0.10    | 0.235         | 1.035 | 3.0       | 0.017 |
| 600 | 120 × 180      | 0.08    | 0.188         | 1.072 | 4.4       | 0.026 |

The "depth" column is (E_max − 1) / (E_perfect − 1) and measures
the fraction of the way from uniform spread to perfect track
confinement.

Linear regression of E vs mode-index in the upper half of each
run gives slope in the range −10⁻⁴ … +10⁻⁴ — essentially flat.

Visualisation of |ψᵢ|² in (t, θ) parameter space for representative
modes (indices 1, 5, 100, 200, 358, 399 in the K=400 run; see
`outputs/track_localization_modes.png`) shows modes that look
like *stripes* running roughly along constant-t or constant-θ
lines, *not* like concentrations along the diagonal characteristic
curves.

The highest-enriched modes (E ≈ 1.04–1.07) occur in 3-fold
degenerate triples (e.g. K=600 idx ∈ {591, 592, 593} with
λ = 2.2609, E = 1.072), consistent with the Z₃-screw symmetry of
the surface — they are not stronger-localized modes, they are
modes whose Z₃-symmetric pattern *happens* to have somewhat more
weight near the tracks.

### Part B — best-localized superposition vs energy

Reading α posits the proton is a *superposition* of LB modes
(a single quantum on the substrate). The right diagnostic is
therefore: how localized can we make a normalised state in the
span of the first n_trunc modes, and what energy ⟨H⟩ = Σ cᵢ² λᵢ
does that best state carry?

The best superposition in a truncated subspace is the eigenvector
of W_ij = ⟨ψᵢ|w|ψⱼ⟩ with the largest eigenvalue; the energy is
read off directly.

K = 400 run (σ = 0.10, mesh 120 × 150, E_perfect ≈ 3.01):

| n_trunc | max E | depth   | ⟨H⟩         | √⟨H⟩  |
| ------- | ----- | ------- | ----------- | ----- |
| 5       | 1.015 | 0.75 %  | 2.10 × 10⁻³ | 0.046 |
| 10      | 1.098 | 4.86 %  | 9.06 × 10⁻³ | 0.095 |
| 20      | 1.145 | 7.20 %  | 1.90 × 10⁻² | 0.138 |
| 40      | 1.170 | 8.46 %  | 4.39 × 10⁻² | 0.209 |
| 80      | 1.176 | 8.76 %  | 6.40 × 10⁻² | 0.253 |
| 160     | 1.183 | 9.09 %  | 1.31 × 10⁻¹ | 0.361 |
| 400     | 1.781 | 38.79 % | 6.66 × 10⁻¹ | 0.816 |

For reference, the *proton* sits at √⟨H⟩ = 2π / L_track ≈ 0.028
(i.e. ⟨H⟩ ≈ 7.8 × 10⁻⁴) in these natural units. So:

- A proton-energy quantum (√⟨H⟩ = 0.028) lies *below* even the
  n_trunc = 5 row of the table — no meaningful track
  localisation is achievable at that energy on this surface
  (depth < 1 %).
- Modest localisation (depth ≳ 5 %) requires √⟨H⟩ ≳ 0.10, i.e. a
  state whose mass is ~3.4× the proton's.
- Substantial localisation (depth ≳ 30 %) requires √⟨H⟩ ≳ 0.8,
  i.e. a state whose mass is ~30× the proton's.

The trade-off has the expected Heisenberg-uncertainty shape:
localisation in space costs energy. The cost on *this* substrate
is much higher than the proton's energy.

## Finding

**No semi-classical track localization is observed in the LB
spectrum of the symmetric modulated-clover up to √λ ≈ 1.5**, and
**no low-energy superposition of LB modes can produce a
track-localized state at the proton energy** — depth < 1 % at
the proton wavenumber, rising only to ~9 % even at 5× the proton
energy.

This is the *negative* answer to the bridge question. The 2-D
wave equation on this surface does **not** reduce to a 1-D wave
equation on the characteristic curves in any obvious
semi-classical sense, and the obstruction is energetic, not just
about individual-mode geometry. The lowest LB eigenvalues
themselves do not match the path-length wavenumbers either (the
LB ground-state pair lies at √λ ≈ 0.055 while
2π / L_track ≈ 0.028 — different by a factor of 2).

## What is *not* shown

- The test reaches √λ ≈ 1.5; it does not reach the deep
  semi-classical regime √λ ≫ 1/ρ ≈ 1. A scarring-style result on
  closed geodesics would typically require √λ in the tens of
  units (i.e. K of order 10⁴ on this surface). The mesh and
  eigensolver used here are not large enough for that range
  without methodological changes. (Note: scarring at very high
  energy would not rescue Reading α for the *proton*, since the
  proton's energy is far below that range — but it would be
  relevant for higher-mass baryons.)

- The test does not rule out a *time-dependent* wave packet that
  is approximately track-localised over short time scales.
  Such a packet would not be a stationary state and would
  disperse; its mass would not be directly ⟨H⟩. Whether the
  framework needs such an interpretation is itself a question
  for Chapter 5.

- The test uses a Gaussian tube weight in (t, θ) parameter space,
  not surface-geodesic distance. A measure based on geodesic
  distance might give slightly different numbers, but the
  qualitative pattern (modes are stripes, not curve-localized)
  is visible in the raw mode plots and is metric-independent.

- The truncation sweep uses simple subspace truncation, not a
  proper Lagrange constraint. A Lagrange-constrained problem
  (max ⟨W⟩ subject to ⟨H⟩ ≤ E_max) would give the actual Pareto
  front and might smooth the jump between n_trunc = 160 and
  n_trunc = 400. The qualitative conclusion (no localisation at
  proton energy; significant localisation only at 30 × proton
  energy) is robust to that refinement.

## Implication for the project arc

For [`work/derived-clover.md`](derived-clover.md) gap (2): the gap
is now **structurally** open, not merely unfilled. The obvious
semi-classical route from the 2-D LB picture to the 1-D
path-length picture **does not work on this surface in the
computed range**. The chapter prose should not promise the
reduction; it should report this computation and either name a
specific further computation that could rescue it or move on.

For the chapter arc in [`../README.md`](../README.md): this
sharpens Reading α vs Reading β.

- **Reading α** (single quantum in 3-mode superposition,
  mass = E, bosonic). This reading needs the 2-D wave equation
  to produce the path-length mass. The present test shows it
  does not, at least via low-to-mid LB modes. Reading α is now
  **structurally blocked** along the obvious route.
- **Reading β** (three quanta, one per color mode, total mass
  3E with E ≈ m_constituent_quark, fermionic with spinor
  upgrade). Reading β does not depend on a 2-D → 1-D wave
  reduction at all — each quantum lives on its own track by
  Pauli, and the path-length formula applies to each track
  independently. The negative result above does not damage
  Reading β.

Chapter 5 should therefore present the negative LB-localization
result as a *finding*, not a residual gap, and shift the weight
of the reading discussion toward Reading β with the fermionic
spinor upgrade.

## Caveats kept open

- Going deeper into the semi-classical regime (K of order 10⁴,
  mesh refined accordingly) might reveal *scars* on closed
  geodesics that this test missed. That would partially
  rehabilitate Reading α as a high-frequency phenomenon, though
  the proton would still not sit at high frequency.
- A surface other than the modulated clover (e.g. one with
  isolated narrow tubes around each track) would show
  localization trivially. The question being asked here is
  whether *this* surface — the one the rest of the project is
  built on — has that property. It does not.
- The construction itself remains an open hypothesis. If the
  Z₂×Z₃-symmetric subspace turns out to be the wrong substrate
  family, the localization conclusion may not transfer.

## Reproducibility

```
python scripts/track_localization.py --K 600 --nt 120 --ntheta 180 --sigma 0.08
```

Outputs (under `outputs/`):

- `track_localization.csv`   — index, eigenvalue, √eigenvalue, E
- `track_localization.png`   — E vs index and E vs √λ
- `track_localization_modes.png` — |ψᵢ|² in (t, θ) for sample modes
- `track_localization.txt`   — summary
