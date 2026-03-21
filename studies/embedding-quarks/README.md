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

### Track 1: Eigenmodes on the embedded torus  ✓

**Result (F1–F5):** The curvature creates an effective potential
V(θ₁) = ε²n₂²/(1+ε cos θ₁)² that concentrates modes at the
outer equator.  At ε = 0.5 (r = 2), the n₁ = 0 ground state
has 40:1 outer/inner amplitude ratio — strongly localized.
The ±n₁ degeneracy lifts (56% splitting at ε = 0.5), making
eigenstates into standing waves with distinct spatial profiles.
Three modes (n₁ = −1, 0, +1) sit at different angular positions,
seeing different effective geometry — the key ingredient for
position-dependent charge.

### Track 2: Position-dependent charge  ✓

**Result (F6–F10):** Odd modes carry zero charge by symmetry;
only even modes contribute (F6).  The ground state acquires
charge on the curved torus — its ratio to the electron grows
monotonically from 0 to 1 as ε increases (F7).  Charge ratios
pass through 1/3 and 2/3 at specific ε values, but NEVER both
at the same ε (F8).  Ratios are continuous, not quantized —
no preferred fractionalization (F9).  The single-torus
position-dependent mechanism cannot produce a proton with two
distinct fractional charges.  Either the full shear-curvature
coupling or a multi-plane mechanism is needed.

### Track 3: Three-quark proton  ✗ (dead)

**Premise failed:** Track 2 showed that (a) only even modes
carry charge (odd modes are zero by symmetry → only two charged
modes, not three), and (b) no single ε gives both 1/3 and 2/3
simultaneously (ratios are continuous, not quantized).

The single-torus position-dependent mechanism cannot produce a
proton with two distinct fractional charges.  The quark question
remains open — see "Status of the quark program" below.


### Track 4: Curvature-corrected α and self-consistent geometry

Track 2 showed that the R19 charge overlap integral changes on
the curved torus: the eigenfunction f(θ₁) replaces cos θ₁ in
the charge integral, modifying α.  Since ε = 1/r, the curvature
correction couples the charge formula to the aspect ratio:

    α_curved(r, s) = (C(1/r)/C_flat)² × α_flat(r, s)

At each r, the required shear s shifts.  This gives the
corrected geometry (r, s) consistent with α = 1/137 on the
curved (not flat) torus.

Key questions:
1. How large is the curvature correction to α at each r?
2. Does the self-consistent (r, s) differ significantly from
   the flat-T² values?
3. Does the IPR of the curved eigenfunction relate to R15's
   localization parameter σ?


### Track 5: Muon charge constraint on the aspect ratio

Track 2 (F7) showed that uncharged modes (n₁ ≥ 2, uncharged on
flat T²) acquire small charges on the curved torus.  In R20's
"hot electron" model, the muon is the fundamental + harmonics.
If the harmonics carry small charges, the muon's total charge
deviates from exactly −e.

Experimentally, Q_muon/Q_electron = 1 to ~10⁻¹² precision.
This constrains:

1. The harmonic charge contributions: C(n₁=2)/C(n₁=1) ≈ 0.03
   at ε = 0.2 (Track 2, Section 1).
2. The occupation of charged harmonics in the muon.
3. The aspect ratio r (through ε = 1/r): larger r = smaller ε
   = smaller harmonic charges = weaker constraint.

If the constraint forces ε < ε_max, this gives a LOWER BOUND
on r — the first physical constraint on the free parameter.


### Track 6: Mode-mode coupling and harmonic spectrum

Compute the electromagnetic coupling between modes on the
curved torus.  On the embedded torus, modes with different
spatial profiles (Track 1) have different Coulomb overlap
integrals.  The coupling matrix:

    V_{mn} = ∫∫ ρ_m(x) ρ_n(x') / |x-x'| dV dV'

determines which harmonic combinations minimize total energy.

Key questions:
1. Does the coupling select a unique harmonic spectrum?
2. If unique: does it predict m_p = 1836 m_e?
3. Does the coupling provide a binding mechanism for composites?


### Status of the quark program

Track 2 tested the most natural embedding-curvature mechanism
for quarks: position-dependent charge from curved eigenmodes.
It failed (F8–F9).  Combined with previous failures:

| Study | Mechanism | Result |
|-------|-----------|--------|
| R19 T4–6 | Shear on flat T²/T³ | F31: gives lighter charged modes |
| R14 | Topological linking on T³ | F18: charge is mode-number, not position |
| R21 T2 | Position on curved T² | F8: ratios are continuous, not quantized |

**What's common:** Every mechanism produces CONTINUOUS charge
ratios.  None yields charge QUANTIZATION at 1/3 and 2/3.  The
standard model postulates fractional charges; GUTs derive them
from group theory (SU(5) representations).  The torus model has
no equivalent algebraic constraint.

**What would be needed:** A topological or algebraic condition
that forces charges on a torus to take specific rational values.
Possible directions (not yet explored):
- Multi-torus models (each quark on its own T²)
- Non-abelian structure (higher gauge symmetry on T²)
- Charge quantization from global T³ consistency conditions

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

## Risk assessment (updated after Track 2)

**Quarks: dead end for now.**  The single-torus mechanism doesn't
produce quantized fractional charges.  The quark program needs a
new idea (multi-torus, non-abelian, or topological quantization).

**Remaining tracks: medium risk, concrete value.**

- **Track 4 (curvature-corrected α):** Low risk.  The computation
  is well-defined.  Even if the correction is small, it gives
  the corrected self-consistent geometry.
- **Track 5 (muon charge constraint):** Low risk, high
  discriminating power.  A quick calculation using Track 2
  results.  Could give the first physical constraint on r.
- **Track 6 (harmonic spectrum):** Medium risk, highest reward.
  If mode coupling selects a unique spectrum, this predicts
  the proton mass.  If not, the spectrum remains free.
