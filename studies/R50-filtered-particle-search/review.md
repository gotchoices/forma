# R50 Review Notes

Independent review of findings and methodology.
Organized by track, updated as tracks complete.

---

## Track 1: Build `ma_model_d.py`

**Verdict:** Sound. No fatal errors.

The model engine is clean, assumption-free, and validated.
Energy, charge, spin (topological), waveguide filtering,
mode scan, and near-miss finder all work correctly. The
alpha formula reproduces 1/137 on both sheets at different
ε values. The self-consistent L_ring derivation from G̃⁻¹
is an improvement over model-C's iterative scheme.

**One clarification on F4 (composite charge):** The gcd-based
formula Q = −n₁ + n₅/gcd(n₅,n₆) gives the right answer for
all modes in the survey. The physical mechanism (per-strand
CP synchronization from R48) is different from the mathematical
shortcut (dividing a bulk quantum number by gcd), but they
produce identical results for all modes where gcd divides n₅
evenly — which is guaranteed by the definition of gcd. No
action needed; the distinction is documented in R48 and Q105.

**The confinement problem (F3):** correctly identified and
honestly handled. The standalone (1,2) mode on Ma_p propagates
through the waveguide — predicting a Q = +1, spin-½ particle
at ~313 MeV that doesn't exist. This IS the quark confinement
problem. The decision to flag these modes and proceed (rather
than wait for confinement to be solved) is correct.


## Track 2: Cross-shear sweep — neutron

**Verdict:** Sound. Amended findings address all concerns.

The cross-shear mechanism (F14) is mathematically correct
and physically sensible. The Schur complement modifies the
proton block of G̃⁻¹, shifting proton-ring modes relative
to the reference mass when L_ring_p adjusts. The self-
consistent L_ring derivation keeps reference masses exact
to machine precision (F16). The methodology is clean.

### Neutron candidate assessment

Two candidates were found. The amended findings handle
them correctly:

**F12 (preferred): (0, 4, 1, −2, 0, 8) at σ_ep ≈ −0.13**
— spans all three sheets, has electron-sheet winding
(n₂ = 4), can decompose into proton + electron + neutrino
for beta decay. Mass residual 0.358 MeV, consistent with
the neutron being a near-miss (unstable, τ = 879 s).
Correctly identified as the physical neutron candidate.

**F11 (flagged): (0, 0, 2, 2, 0, −8) at σ_νp ≈ −0.13**
— better mass match (0.25 MeV) but no electron-sheet
winding. The amended findings correctly flag the
decomposition concern without disqualifying the mode
(the counter-argument about cross-sheet energy transfer
is noted). May be a dark or exotic neutral fermion.

The amended F12b (dark windings) is a good addition —
it explains how neutral massive modes carry their mass
through ring windings and neutrino-sheet windings that
enter the energy formula but not the charge formula.

### Items resolved by amendment

The original findings presented F11 as the primary
neutron candidate without noting the beta-decay
decomposition problem. The amended version:
- Raises the concern explicitly in F11
- Elevates F12 as the preferred candidate
- Adds the structural comparison table to model-C
- Adds F12a (σ_νp implications for fusion)
- Adds F12b (dark windings as mass carriers)
- Updates the Track 2 summary with confidence levels

All concerns from the initial review are addressed.
No remaining issues.

### Structural comparison to model-C neutron

| Property | Model-C neutron | F12 candidate |
|----------|----------------|---------------|
| Mode | (0, −2, 1, 0, 0, +2) | (0, 4, 1, −2, 0, 8) |
| Ma_e winding | n₂ = −2 | n₂ = 4 |
| Ma_ν winding | n₃ = 1 | n₃ = 1, n₄ = −2 |
| Ma_p winding | n₆ = +2 | n₆ = 8 |
| Spin source | Ma_ν (n₃ = 1) | Ma_ν (n₃ = 1) |
| Cross-shear | σ_ep = −0.091 | σ_ep = −0.130 |
| Mass residual | 0 (pinned) | 0.358 MeV |
| Beta decay | ✓ (has e winding) | ✓ (has e winding) |

Both get spin from Ma_ν (n₃ = 1). Both have electron-sheet
winding (enabling beta decay). The model-D candidate has
higher winding numbers throughout — n₂ = 4 vs −2, n₆ = 8
vs 2. This reflects the different geometry (proton as (3,6)
at ε_p = 0.55, vs proton as (1,2) at r_p = 8.906).

The n₆ = 8 proton-ring winding is high (compared to the
proton's n₆ = 6). The neutron winds the proton ring at a
higher harmonic than the proton itself. Whether this has
physical consequences should be investigated.

### σ_νp finding and fusion implications

F11 found σ_νp ≈ −0.13 produces a mode near the neutron
mass. While F11's specific candidate is not the neutron
(no electron winding), the fact that σ_νp must be nonzero
and ~0.13 in magnitude is important for Q89 (fusion).

The fusion bootstrap pathway (Q89 §12.2) requires σ_νp ≠ 0
so that every proton has a virtual neutrino-sheet
fluctuation that can be pumped by IR at 42 μm. Track 2
establishes that σ_νp ≈ 0.13 is needed for the neutron —
confirming that this cross-shear is physically nonzero and
of substantial magnitude.

However: the physical neutron candidate (F12) uses σ_ep,
not σ_νp. If the neutron is produced by σ_ep ≈ −0.13
rather than σ_νp, the σ_νp value remains unconstrained
by the neutron mass. Both cross-shears may be nonzero
(the F11 and F12 candidates come from different σ sweeps),
but only σ_ep is directly constrained by the neutron if
F12 is the correct identification.

### Notes for downstream tracks

- Track 5 should check whether the 0.358 MeV residual
  maps to 879 s under the off-resonance power law
  (τ ∝ |gap|^−2.7 from R27 F33).

- The F11 mode (0, 0, 2, 2, 0, −8) should be checked
  against the dark matter candidate list — it may be
  one of the ghost modes from R42.

- Future neutron searches should include "nonzero
  electron-sheet winding" as a physical plausibility
  filter (not a hard filter — F11 is still carried
  forward, but decomposition-viable candidates should
  be flagged separately).

### Other notes

- **F13 (σ_eν has zero effect)** is expected and correct.
  The electron and neutrino sheets are both too large to
  contribute significant energy at the proton scale.

- **F14 (indirect mechanism)** is the most important
  structural finding. The Schur complement mechanism is
  mathematically clean and physically motivated.

- **F15 (mode spacing limits resolution)** is an important
  structural insight. The neutron-proton mass difference
  (1.293 MeV) is only 1.08% of the proton mode spacing
  (~119 MeV). Cross-shear tuning of L_ring is required
  to land this close. This means σ is constrained by the
  neutron — the neutron's existence tells us something
  about the cross-coupling.


## Track 3: Full joint mode sweep — particle spectrum

**Verdict:** Strong results with two significant structural
issues. No fatal errors in computation.

### Highlights

**The Ω⁻ (F22) is the standout result.** Model-C listed it
as "structurally forbidden." Model-D finds it at 0.04%
(0.6 MeV at 1672 MeV) through the composite electron-sheet
mechanism — n₁ = −2 with gcd = 2 gives a per-strand tube
of 1 (odd → spin ½) while raw charge contribution is even.
This breaks the simple parity argument and enables Q = −1
with J = 3/2. The mode structure is complex (composites on
all three sheets, n₆ = 13) and could not have been guessed
from simple scaling. A genuine prediction improvement over
model-C.

**Seven of twelve unstable targets within 2%** at a single
σ_ep = −0.13. The same cross-shear that produces the
neutron (Track 2) also produces Σ⁺ (0.19%), τ⁻ (0.18%),
Λ (1.1%), Ξ⁰ (1.8%), and Δ⁰ (0.41%). One parameter, many
outputs.

**The spin-charge parity rule (F17)** is a derived
structural constraint, not imposed. The discovery that J = 0
with odd Q is topologically forbidden is important — it
explains WHY charged pseudoscalar mesons are problematic,
rather than just noting they don't match.

### Significant issues

**Issue 1: Charged pseudoscalar mesons are topologically
forbidden.**

π± and K± — among the most common, well-measured particles
— cannot exist as single eigenmodes under the additive spin
rule. J = 0 requires all tube windings even, which forces
Q = even. This is not a mass miss or a parameter problem. It
is a structural impossibility.

The identified resolution — allowing antiparallel spin
alignment (two spin-½ combining to J = 0 via QM addition
rather than simple counting) — would fix it. But this is a
change to the spin rule. Whether the torus geometry supports
antiparallel alignment within a single mode is an open
question. It may require two strands on the same sheet with
opposite tube orientations, which is geometrically different
from the current picture of phase-separated identical
strands.

This is the most significant structural failure and should
be prioritized. If π± cannot be accommodated, the model has
a gap at the most basic level of the meson spectrum.

**Issue 2: The muon sits in a mass desert.**

The gap between the electron sheet energy scale (~0.2 MeV)
and the proton sheet energy scale (~116 MeV) contains no
eigenmodes. The muon (105.7 MeV) and pion (135-140 MeV)
both fall in this desert. The 10.9% muon residual is the
largest fermion miss.

This is structural, not parametric — it follows from the
electron-proton mass ratio (1:1836). No parameter
adjustment fixes it. The findings correctly identify four
possible resolutions (intermediate sheet, sub-harmonics,
aspect-ratio compression, composite states). None has been
tested.

In model-C, the muon was a calibration target (pinned
exactly), which hid this issue. Model-D's philosophy of
treating the muon as a prediction rather than an input
correctly exposes it.

### Continuing concerns

**The neutron decomposition problem persists (F24).** The
improved neutron candidate (0, 6, *, *, 0, 8) still has
n₁ = 0 — no electron tube winding. It has electron RING
winding (n₂ = 6), which is dark (no charge, no spin from
Ma_e). The electron in beta decay needs charge −1 (n₁ = 1)
and spin ½ (odd tube). Neither is present in the neutron's
electron-sheet component. The wider scan sharpened this
concern rather than resolving it.

The question remains: can a dark electron-ring winding
"unravel" into a physical charged electron during beta
decay? Or must the neutron mode contain an explicit charged
electron component (n₁ ≠ 0)?

**The off-resonance correlation weakened (F21).** Pearson
r = −0.40 (N = 9) vs model-C's r = −0.84. The sign is
correct (shorter lifetime → larger residual). The
weakening may reflect the different parameter set and
extended particle sample (including Δ and ρ, which are
extremely short-lived). The muon is an outlier — large
residual but relatively long lifetime — likely because it
sits in the mass desert where the nearest mode is far
away regardless.

If the correlation doesn't strengthen with parameter
optimization (Track 4), the off-resonance hypothesis may
need refinement — perhaps lifetime depends on something
beyond the mass gap alone (decay channel availability,
phase space, quantum number conservation).

**Mode overcounting (F20).** 567,470 propagating modes
below 2 GeV vs ~15 targets. Most is label degeneracy
(neutrino/electron dressings at negligible energy).
Physically distinct modes (~200-400) still overcount by
15-25×. Whether the excess modes are dark matter
candidates, mathematical artifacts, or a sign that the
search space is too unconstrained remains open.

### Notes for downstream tracks

- The charged meson problem (F17) is the top priority
  for Track 4. Can the spin rule be refined to permit
  antiparallel alignment?

- The muon problem (F19) may need a dedicated
  investigation — either an intermediate-scale sheet or
  a sub-harmonic mechanism.

- The neutron decomposition concern should be tested:
  compute what happens when a mode with dark electron-
  ring winding (n₁ = 0, n₂ ≠ 0) loses its cross-sheet
  coupling. Does the energy redistribute into a charged
  electron mode, or does it disperse?

- The off-resonance correlation should be recomputed at
  optimized parameters (if Track 4 produces them) and
  compared to R27's model-C result.


## Track 4: Decay rate ↔ near-miss correlation

**Verdict:** Honest negative. Not a fatal problem — an
improvement in understanding.

### What happened

The off-resonance correlation weakened from model-C's
r = −0.84 (N ≈ 7, p = 0.009) to model-D's r = −0.38
(N = 10, p = 0.28). No subset achieves significance at
p < 0.05. The R27 power law (τ ∝ |Δm/m|^−2.7) fails
quantitatively — RMS log₁₀ error of 13.1 when calibrated
to the neutron.

### Why this is not a fatal problem

**The weaker correlation is more honest, not worse.**
Model-C pinned the muon and neutron as fitted parameters,
giving them artificially small residuals and biasing the
correlation upward. Model-D treats both as genuine
predictions, exposing the muon's 11% mass desert residual
and the neutron's true position. The r = −0.84 was partly
an artifact of parameter pinning. The r = −0.38 is the
truth that was hidden.

**The direction is consistently right.** All eight subsets
tested show negative correlation (shorter lifetime →
larger residual). The sign is correct in every case. The
hypothesis is directionally valid even if it's not
quantitatively predictive from mass gap alone.

**The neutron–Ω⁻ paradox (F26) is the key structural
finding.** Two particles with |Δm/m| ≈ 0.035% and
lifetimes differing by 10¹³. This is an airtight proof
that mass gap alone cannot predict lifetime. The paradox
has a clean explanation: the neutron decays via weak β
(highly suppressed), while the Ω⁻ decays via weak ΔS
with much larger phase space (~530 MeV Q-value). The
missing variables are decay coupling strength and
available phase space — not a flaw in the model, but a
limitation of single-variable analysis.

### The stratified hypothesis (F28)

The refined off-resonance hypothesis is the right move:
within each decay-channel class (weak β, weak leptonic,
weak ΔS, EM, strong), the mass-gap correlation may hold
independently. Cross-class comparisons require a coupling-
strength prefactor. The current sample sizes (4-5 per
class) are too small to confirm, but the framework is
physically sound.

### Impact on the white paper

The white paper's "ephemeral particles" section presents
the off-resonance hypothesis as: "the model predicts both
the approximate mass AND the instability." Track 4 shows
this is half true — the model correctly identifies which
particles are unstable (near-misses to eigenmodes) but
cannot quantitatively predict HOW unstable (the lifetime)
from the mass gap alone. A note acknowledging that
lifetime prediction requires coupling-channel information
beyond the mass gap would be appropriate.

### The deeper opportunity

Can coupling strengths be derived from the Ma geometry?
In MaSt: strong = internal EM at torus overlap (Q95),
weak = cross-sheet coupling σ_ep, EM = 1/α junction.
If these can be computed from the mode's quantum numbers
and the metric, a two-variable model (|Δm/m| + geometric
coupling strength) might recover the full 30-decade
lifetime range. This is a future study, not a Track 4
failure.

### Assessment

The off-resonance hypothesis survives as a qualitative
principle: unstable particles are near-misses to
eigenmodes, and the mass gap is one factor in their
lifetime. It fails as a quantitative single-variable
predictor — coupling strength and phase space are the
other factors. The R27 result was partially an artifact
of model-C's parameter pinning. Model-D's honest
treatment is better science even if the numbers are
less impressive.


## Track 5

*(Not yet reviewed.)*
