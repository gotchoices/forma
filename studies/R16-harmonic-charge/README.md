# R16. Harmonic Decomposition and the Charge-Producing Mode  *(open)*

If the confined photon's energy distributes across multiple
Fourier components of the compact space, and only the p = 1
component produces charge (via WvM commensurability), then:

    α = (energy in p = 1 mode) / (total energy)

This would derive α as an energy partition ratio — a purely
geometric property of the mode spectrum.

## Motivation

### The charge mechanism recap

WvM's charge requires p = 1: one tube winding per wavelength,
so the circular polarization rotation matches the geometric
frame rotation, keeping E always normal to the surface.  R13
proved that p ≠ 1 gives zero monopole charge (exactly).

### Why energy partition?

R7 found U_Coulomb = α × m_e c² at Compton scale.  R15 will
test whether the forward calculation (energy → field → charge)
reproduces this.  But even if R15 succeeds numerically, we need
a physical explanation for WHY only a fraction α of the energy
couples to the far field.

Path 5 of Q34 proposes the answer: the photon's field, when
decomposed into Fourier modes of the compact space, has its
energy spread across many (p, q) components.  Only the p = 1
component produces net charge.  The fraction of energy in that
component is α.

### What R12 Track 1 tells us

R12 found that flat T² at Compton scale has no eigenmodes at
ω_C — the spectral gap is ~137×.  The lowest eigenfrequency
is ~137 × ω_C.  This means:

- The electron is NOT a resonant eigenmode of the cavity.
  It is a **winding mode** (R13 confirmed this).
- A winding mode wraps around the compact space many times.
  Its field, expressed in compact-space coordinates (θ, φ),
  is NOT a single Fourier component — it has structure at
  multiple scales.
- The Fourier decomposition of this winding-mode field into
  the natural (p, q) basis of T² distributes energy across
  multiple components.

This is exactly the setup where Path 5 applies.  The question
is: what fraction lands in p = 1?

### Connection to the "two beating frequencies" idea

The user's original intuition was that multiple photons on a
small torus beat at the Compton frequency.  The pure two-photon
version is ruled out by energy conservation (each would need
frequency > ω_C, so total > 2 m_e c²).  But the viable version
is a single photon's field decomposing into many harmonics of
the compact space, with the p = 1 harmonic being the one that
produces charge.  This is NOT multiple photons — it is one
photon whose field has multiple Fourier components.

### Relationship to R15

R15 (forward charge calculation) and R16 are complementary:

| | R15 | R16 |
|---|-----|-----|
| **Approach** | Numerical: compute 3D field, measure flux | Analytical: decompose field, count energy |
| **Question** | What charge does the forward calc give? | Why does only fraction α couple to 3D? |
| **If succeeds** | Derives α numerically | Explains why R15 works |
| **If fails** | α is not from (1,2) forward calc | Mode decomposition may still give α |

If both succeed independently and agree, that is strong
confirmation.

## Tracks

### Track 1. Fourier decomposition of the (1,2) winding mode

On flat T² with coordinates (θ, φ), a photon on the (1,2)
geodesic has wave phase ψ = θ + 2φ.  As a pure plane wave,
this is a single Fourier component (p, q) = (1, 2).  All
the energy is in one mode, and p = 1 — so 100% of energy is
in the charge-producing mode.  This gives α = 1, which is
wrong.

**The resolution:** the pure plane wave on flat T² is NOT the
physical field configuration.  The physical field must satisfy
boundary conditions at the compact/3D interface — the
embedding.  When the compact T² is embedded in 3D as a torus,
the field is modified:

- The area element varies as (R + a cos θ), concentrating
  field energy on the outer equator (θ = 0) and diluting it
  on the inner equator (θ = π).
- The 3D Laplacian on the embedded surface mixes Fourier
  components: the (1, 2) component couples to (1±1, 2),
  (1±2, 2), etc.
- The physical field is a boundary-value solution, not a
  free plane wave.

**Calculation:**
1. Write the (1, 2) plane wave on flat T²
2. Embed on the torus in 3D
3. Apply the physical boundary condition: the field must
   satisfy Maxwell's equations both ON the torus surface
   and in the surrounding 3D space
4. Solve for the modified field (perturbation theory in
   a/R or numerical)
5. Decompose the result back into (p, q) Fourier components
6. Compute the energy fraction in p = 1

**Expected difficulty:** Medium.  The embedding modifies the
field, but the modification can be treated perturbatively
for thin tori (a ≪ R).  The key quantity is the coupling
coefficient between the (1, 2) mode and other (p, q) modes
induced by the curvature of the embedding.

### Track 2. Energy in the monopole-producing component

R13 Track 3 showed that the monopole integral (charge) is
determined by the (0, 0) Fourier component of
σ(θ, φ) × (R + a cos θ), where σ is the surface charge
density.  For a pure cos(pθ + qφ) wave, this is zero unless
q = 0.

But Track 1 will show that the physical field is NOT a pure
(p, q) mode — it is a superposition.  The question is whether
the superposition has a nonzero (0, 0) component.

**Calculation:**
1. Take the modified field from Track 1
2. Compute σ(θ, φ) × dA = σ(θ, φ) × (R + a cos θ)
3. Extract the (0, 0) Fourier component
4. This gives the net charge Q
5. Compute α = Q²/(4πε₀ ℏc)

This is the analytical version of R15's numerical calculation.
If both give the same α, the result is robust.

**Expected difficulty:** Medium — depends on Track 1 having
a tractable solution.

### Track 3. Mode spectrum and energy partition on T² with
embedding curvature

The flat T² Laplacian has eigenvalues
ω²_{p,q} = c²(p²/a² + q²/R²).  The embedding curvature
modifies these to coupled modes.  Compute:

1. The perturbed eigenvalues (mode splitting from curvature)
2. The overlap integrals between flat-space modes and
   curved-space modes
3. The energy distribution when a (1, 2) state is prepared
   on flat T² and then allowed to evolve on the embedded
   (curved) torus

If the curvature redistributes energy from (1, 2) to a broad
spectrum with the p = 1 sector retaining fraction α, that is
the derivation.

**Expected difficulty:** Medium-high.  This is a perturbation
theory / coupled oscillator problem.  The zeroth-order
spectrum is known (R12 Track 1).  The perturbation is the
difference between the flat and embedded Laplacians, which
is O(a/R).

### Track 4. The (0, 0) coupling coefficient as a function
of geometry

For a general torus with aspect ratio r = a/R, the coupling
between the (1, 2) mode and the (0, 0) component (charge)
is determined by an overlap integral involving the area
element (R + a cos θ).  This integral has a closed-form
expression.

If this coupling coefficient = α for all r (or for a
specific r determined by another constraint), the result
is a geometric identity.

**Calculation:**
1. Expand 1/(R + a cos θ) in Fourier series:
   1/(R + a cos θ) = (1/R) Σ_n c_n cos(nθ)
   where c_n depends on r = a/R
2. The coupling from (1, 2) to (0, 0) goes through the
   n = 1 coefficient: c₁ = −r/√(1 − r²) × (1/R) (exact)
3. The charge is proportional to c₁ × (amplitude of
   (1, 2) mode)
4. α = (c₁-mediated charge energy) / (total energy)

This might give α as a closed-form function of r.

**Expected difficulty:** Low-medium.  The Fourier expansion
of 1/(R + a cos θ) is a standard result.  The physics is
whether this coupling IS what determines the apparent charge.

## What would success look like?

A successful outcome is: α expressed as a function of the
torus aspect ratio r = a/R (or shown to be independent of r),
derived purely from the Fourier structure of the embedded
field.  This would:

1. Derive α from geometry alone
2. Explain R7's U_Coulomb = α × m_e c² (the Coulomb energy
   is the far-field energy of the p = 1 component)
3. Explain R15's forward calculation (if it succeeds)
4. Connect the charge mechanism to the mode structure of
   the compact space
5. Potentially determine the aspect ratio r if α(r) has a
   unique solution at 1/137

## Connections

- **R15** — numerical forward calculation (complementary)
- **R12** — flat-T² mode spectrum; spectral gap
- **R13** — monopole integral; winding mode identification
- **R7** — U_Coulomb = α × m_e c²; Possibility A
- **Q34 Path 5** — the originating idea
- **Q42, Q44** — wave-language versions of this question
- **Q43** — what selects the harmonic number

## References

- R12 Track 1: flat-T² spectrum, spectral gap
  [`R12-self-consistent-fields/findings.md`](../R12-self-consistent-fields/findings.md)
- R13 Track 3: monopole integral, Fourier analysis
  [`R13-kk-charge-t3/findings.md`](../R13-kk-charge-t3/findings.md) (F18–F23)
- R7 Possibility A: near-field/far-field split
  [`R7-torus-capacitance/findings.md`](../R7-torus-capacitance/findings.md) (F4)
