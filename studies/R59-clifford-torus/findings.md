# R59 Findings

## Track 1: Build the metric with time

### F1. The bare 10D Lorentzian metric reproduces model-E exactly

The 10D metric (6 Ma + 3 S + 1 t, with g_tt = -1) with no
off-diagonal coupling gives identical particle masses to
model-E.  All three computation methods (model-E library,
Schur complement on time, mass-shell condition) agree to
full numerical precision.  The time dimension, when decoupled,
is invisible to the particle spectrum.


### F2. Tube coupling is catastrophic; ring coupling is controllable

Ma-t coupling on TUBE dimensions (e-tube, p-tube) produces
wild mass distortions even at σ = 0.001 (−40% electron shift,
+28% proton shift).  This is the same tube saturation found
in R55 (the e-tube off-diagonal is at the PD boundary from
the internal shear s_e = 2.004).

Ring coupling (e-ring, ν-ring, p-ring) is well-behaved:
smooth, controllable mass shifts proportional to σ².


### F3. The Schur complement and mass-shell condition disagree

At σ = 0.1 (ring coupling), the Schur complement (integrate
out time, compute on effective spatial metric) gives a 0.35%
mass shift, while the mass-shell condition (solve the full
Lorentzian dispersion relation) gives a 7% shift — a factor
of 20× difference.

**The mass-shell condition is the correct physics for a
Lorentzian metric.**  The Schur complement, which R55 used,
does not properly account for the Lorentzian signature.  The
mass-shell approach solves the full dispersion relation:

> g^{ab} k_a k_b + g^{tt} ω² + 2 g^{at} k_a ω = 0

where k_a are the Ma winding numbers and ω is the frequency
(= energy / ℏ).  This is a quadratic in ω whose solutions
give the particle and antiparticle masses.

This means R55's Schur complement results, while qualitatively
correct, were quantitatively off by a large factor.  The
Lorentzian mass-shell is the right tool.


### F4. The Lorentzian sign DECREASES masses

In R55 (Euclidean, spatial-only metric), the ℵ-mediated
coupling INCREASED mode energies (the Schur complement
subtracted from the Ma metric, making G̃⁻¹ larger).

With Lorentzian signature, the Ma-t coupling DECREASES mode
energies.  The Schur complement on time ADDS to the Ma metric
(because g_tt = -1, division by -1 flips the sign), making
the effective G̃ larger and G̃⁻¹ smaller.

Physically: the Ma-t coupling allows the mode to "borrow"
energy from the time dimension, slightly reducing the rest
mass.  This is opposite to the Coulomb self-energy (which
adds to mass) — suggesting the physical interpretation may
need refinement.


### F5. Near-universal α with 1.9% gap — best result yet

At σ = 0.00863 (ring coupling):

| Mode | E_bare (MeV) | E_coupled | α_eff | α_eff/α | Δm% |
|------|-------------|-----------|-------|---------|-----|
| electron | 0.511 | 0.507 | 7.30×10⁻³ | 1.000 | -0.73 |
| proton | 938.3 | 931.6 | 7.16×10⁻³ | 0.981 | -0.72 |
| ν₁ | 2.9×10⁻⁵ | 2.9×10⁻⁵ | 7.55×10⁻³ | 1.035 | -0.76 |
| deuteron | 1876.5 | 1863.1 | 7.16×10⁻³ | 0.981 | -0.72 |

**Universality gap: 1.9%** (electron vs proton).
R55's best was 3.6%.  The time-based approach halves the gap.

The spectrum shift is only 0.7% — smaller than R55's 1.4%.


### F6. Comparison: R55 vs R59

| Property | R55 (ℵ, spatial) | R59 (time, Lorentzian) |
|----------|-----------------|----------------------|
| Metric | 10×10 (Ma+ℵ+S) | 10×10 (Ma+S+t) |
| Coupling parameter | σℵS = 0.290 | σ = 0.00863 |
| Coupling method | Schur complement | Mass-shell condition |
| α_eff(electron) | 1.000α | 1.000α |
| α_eff(proton) | 0.964α | 0.981α |
| α_eff(ν₁) | 1.069α | 1.035α |
| **Universality gap** | **3.6%** | **1.9%** |
| Spectrum shift | 1.4% | 0.7% |
| Ma-S entries | Zero (through ℵ) | Zero (through t) |
| Needs ℵ? | Yes | **No** |
| Free parameter | σℵS | σ (Ma-t) |

The time-based approach is simpler (no ℵ dimension), more
universal (1.9% vs 3.6%), and produces smaller spectrum
perturbation (0.7% vs 1.4%).


### F7. The coupling parameter σ ≈ 0.00863 ≈ 1.18α

The optimal Ma-t coupling is σ = 0.00863, which is close
to α = 0.00730 (ratio 1.18).  This is suggestive — the
coupling might BE α (or a simple function of it) rather
than an independent parameter.  If σ = α, the coupling
would be slightly below the optimum (α_eff ≈ 0.84α for
the electron).  If σ = α × (some geometric factor ≈ 1.18),
the coupling is exact.


### F8. The neutrino couples at 1.035α — nonzero

The ν-sheet couples to St through the ν-ring → t entry,
at α_eff = 1.035α.  This is nonzero and close to the
charged-particle coupling, supporting the L05 premise.
The ν-sheet is not electromagnetically dark — it couples
through time, even without electric charge.


## Track 1 status

**Complete.**  The 10D Lorentzian metric with Ma-t ring
coupling produces near-universal α (1.9% gap, best yet),
0.7% spectrum shift, and nonzero ν coupling.  The mass-shell
condition (not the Schur complement) is the correct
computation for Lorentzian signature.

## Open questions for Track 2

1. Can the 0.7% spectrum shift be absorbed by re-tuning
   ε_e, ε_p (as in R55 Track 4)?
2. Does the 1.9% gap close with a non-uniform Ma-t coupling?
3. What is the physical interpretation of the mass DECREASE?
   (Coulomb self-energy should increase mass, not decrease.)
4. Is σ = α × 1.18 exact, or does the geometric factor have
   a simpler form (like √(4π/3) ≈ 1.18)?
