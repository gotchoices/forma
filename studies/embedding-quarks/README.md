# R21. Quarks from Embedding Curvature

Can the position-dependent curvature of the embedded torus produce
fractional charges, binding, and a preferred harmonic spectrum?

## Background

### The two-domain picture (R12)

The photon propagates through flat compact space (T²), but its
fields project into 3D through the toroidal embedding.  Mass and
spin are internal properties (flat T²).  Charge is an external
property (embedded torus in 3D).  These are two aspects of the
same object (R12 F14).

### The embedding is not uniform

An embedded torus has position-dependent Gaussian curvature:

    K(θ₁) = cos(θ₁) / (a(R + a cos(θ₁)))

At the outer equator (θ₁ = 0): K > 0 (positive curvature).
At the inner equator (θ₁ = π): K < 0 (saddle-like).
The effective geometry varies around the torus.

### Fractional charges from geometry (S3 F4)

S3 showed that the WvM charge formula gives fractional charges
at specific aspect ratios:

| Particle | Charge | Required a/R | Ratio to electron |
|----------|--------|-------------|-------------------|
| Electron | e | 1/√(πα) ≈ 6.60 | 1.0× |
| Up quark | 2e/3 | (3/2)/√(πα) ≈ 9.91 | 1.5× |
| Down quark | e/3 | 3/√(πα) ≈ 19.81 | 3.0× |

The ratios are clean integers: 1 : 3/2 : 3.  This is algebraic —
never physically implemented.

### Previous quark attempts (all on flat space)

| Study | Mechanism | Why it failed |
|-------|-----------|---------------|
| R19 T4–6 | Shear variations on flat T²/T³ | Charges or masses wrong |
| R14 | Three linked photons on flat T³ | Charge depends on mode numbers, not arrangement |

All operated on flat compact space.  None tested the embedding.

### What R20 established

Proton = fundamental + uncharged harmonics.  Neutron = two
opposite-charge fundamentals + harmonics.  The model is
descriptive (correct kinematics) but underdetermined (harmonic
spectrum is free).  Three open questions feed into R21:

1. **DIS:** Three charged scattering centers inside the proton.
2. **Binding:** What couples eigenmodes into composites?
3. **Spectrum:** What selects the harmonic distribution?

All three involve physics beyond flat T².

## Core idea

The embedded torus has curvature that varies with position θ₁.
Modes localized at different angular positions experience different
effective geometry — different effective a/R.  If these effective
ratios match the S3 values (6.60, 9.91, 19.81), then modes at
specific positions carry fractional charges.

Three fundamentals at angular positions where the effective a/R
gives 2e/3, 2e/3, and −e/3 would be quarks:

    proton = u(2e/3) + u(2e/3) + d(−e/3) = +e
    neutron = u(2e/3) + d(−e/3) + d(−e/3) = 0

This also provides:
- **Binding:** curvature-induced mode-mode coupling holds
  the composite together.
- **Spectrum selection:** the equilibrium between curvature
  coupling and mode energy selects the harmonic distribution.
- **DIS compatibility:** three localized charge centers with
  fractional charges.

## What this study does NOT attempt (yet)

- **Color charge and confinement.**  Why quarks cannot exist
  as free particles.  In this model, "confinement" might mean
  modes at fractional-charge positions are unstable unless
  balanced by other modes.

- **Gluons and the strong force.**  The interaction between
  quarks.  If modes at different positions couple through the
  embedding curvature, this coupling IS the strong interaction.
  But deriving its properties is a stretch goal.

- **Strange, charm, bottom, top quarks.**  Higher generations.
  These may correspond to higher harmonics at the same angular
  positions, analogous to muon/tau as "hot electrons" (R20 F17).

## Planned approach

### Track 1: Eigenmodes on the embedded torus

Solve the wave equation on the embedded (curved) torus:

    ∇²ψ + ω²ψ = 0

where ∇² uses the induced metric:

    ds² = a²dθ₁² + (R + a cos θ₁)²dθ₂²

The eigenmodes are still periodic in θ₂ (axial symmetry), so
ψ(θ₁, θ₂) = f_n(θ₁) × e^(in₂θ₂).  The equation for f_n
is a Hill/Mathieu-type ODE in θ₁.

Key questions:
1. How do the eigenfrequencies differ from flat T²?
2. Do modes localize in θ₁ (concentrate at specific positions)?
3. What is the mode structure for the electron's (1,2) winding?

### Track 2: Position-dependent charge

Compute the R19 charge integral using the curved-space
eigenmodes from Track 1 instead of flat-space plane waves.

Key questions:
1. Does the effective charge depend on where a mode is
   concentrated in θ₁?
2. If modes localize near the outer equator (θ₁ ≈ 0) vs the
   inner equator (θ₁ ≈ π), do they carry different charges?
3. Do the effective charges match the S3 ratios (e, 2e/3, e/3)?

### Track 3: Three-quark proton

If Tracks 1–2 give position-dependent fractional charges,
construct a proton from three fundamentals at the appropriate
positions.

Key questions:
1. Do three localized modes at specific θ₁ positions give
   charges summing to +e?
2. Is ΣQ² consistent with DIS cross sections?
3. Is the proton stable (no decay channel with lower energy)?

### Track 4: Natural harmonic spectrum

Compute mode-mode coupling coefficients from the curvature.
On the curved torus, modes are NOT orthogonal — they couple.
The coupling matrix determines:

1. Which harmonic combinations have lowest total energy.
2. Whether the equilibrium spectrum is unique (predictive)
   or degenerate (still underdetermined).
3. If unique: does it predict m_p = 1836 m_e?

## Dependencies

- **R20 (complete):** Harmonic proton model, mode catalog,
  neutrino constraints, free parameter summary.
- **R19 (complete):** Charge formula, shear s₁₂, the n₁ = 1
  selection rule.
- **R12 (complete):** Two-domain picture (flat for mass,
  embedded for charge).
- **S3 (complete):** Fractional charges at a/R = 9.91, 19.81.

## Relation to other questions

- Q26: hadrons from photon knots (DIS test)
- Q13: three compact dimensions (quarks in a different plane?)
- Q16: what sets the photon energy / mass spectrum
- Q32: energy and geometry as only fundamentals

## Risk assessment

**High risk, high reward.**

- The foundational calculation (Track 1) is well-defined:
  solve the wave equation on a curved torus.  This will
  produce concrete numbers regardless of outcome.
- The critical test is Track 2: does curvature make charge
  position-dependent?  If not, the approach fails cleanly.
- The S3 ratios (1 : 3/2 : 3) are specific targets.  A match
  would be striking; a miss rules out the mechanism.
- Mode localization (Track 1) may not occur if the curvature
  is too weak — modes might remain delocalized.  The ratio
  a/R determines the curvature strength.
- Track 4 (natural spectrum) is the highest-value outcome
  but depends on Tracks 1–2 succeeding.
