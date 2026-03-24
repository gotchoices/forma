# R28 Findings


## Track 1. σ_eν and σ_νp exploration

Script: `scripts/track1_cross_shear_sweep.py`


### F1. Neutrino cross-shears do not improve the spectrum

Sweeping σ_eν from −0.20 to +0.20 (at σ_νp = 0) changes
the RMS fractional error by < 0.01%.  Sweeping σ_νp over
the same range changes it by < 0.5%.  The 2D grid search
over both confirms: **σ_eν = σ_νp = 0 is already optimal.**

The neutrino sheet decouples from the particle spectrum at
MeV scale.  This is the same insensitivity found for r_e in
R29 (F22): the neutrino dimensions are so large that their
cross-shear contributions to mode energies are negligible.


### F2. Individual particle responses to σ_νp

While the overall RMS doesn't improve, individual particles
shift slightly under σ_νp:

| σ_νp | τ⁻ | π⁺ | K⁺ | Λ | Σ⁺ |
|------|-----|-----|-----|-----|-----|
| −0.20 | 5.3% | 13.1% | 0.6% | 7.3% | 13.0% |
| −0.16 | 5.5% | 13.3% | **0.0%** | 7.6% | 13.4% |
| 0.00 | 5.6% | 13.5% | 1.2% | 5.8% | 11.6% |
| +0.16 | 5.5% | 13.3% | **0.0%** | 7.6% | 13.4% |
| +0.20 | 5.3% | 13.1% | 0.6% | 7.3% | 13.0% |

At σ_νp ≈ ±0.16, the kaon K⁺ matches exactly (0.00%).  But
this worsens Λ (5.8% → 7.6%) and Σ⁺ (11.6% → 13.4%).  The
trade-off is unfavorable — the kaon was already at 1.2%.


### F3. The problem particles are structural, not parametric

The large-gap particles are unchanged by cross-shear tuning:

| Particle | Gap at baseline | Gap at best σ_νp |
|----------|----------------|-----------------|
| π⁺ | 13.5% | 13.1% |
| τ⁻ | 5.6% | 5.3% |
| ρ⁰ | 20.9% | ~20% |
| ω | 19.9% | ~20% |
| Σ⁺ | 11.6% | 11.6% |
| Δ⁺⁺ | 14.2% | ~14% |

These gaps are structural — the particles don't sit near any
T⁶ eigenmode regardless of parameter values.  This is fully
consistent with R27's off-resonance hypothesis: these are
transient excitations, not exact eigenmodes.  Their gaps
from the nearest mode correlate with lifetime (R27 F37–F42).


### F4. Summary of Track 1

1. **σ_eν and σ_νp = 0 is optimal.** No improvement from
   the 2D grid search.

2. **The neutrino sheet decouples** from the particle
   spectrum at MeV scale — same as r_e and r_ν.

3. **Problem particles are structural,** not fixable by
   parameter tuning.  This strengthens the off-resonance
   interpretation.

4. **Free parameter status unchanged.**  σ_eν and σ_νp
   remain unconstrained but also irrelevant.
