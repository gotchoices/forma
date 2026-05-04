# Q139: Is the anomalous magnetic moment a measurement of the GRID primitive's chirality deviation from equipartition?

**Status:** Open — structural conjecture with matching qualitative
signs and a clean inversion handle.  Quantitative test requires
deriving the closed-form δχ̃ ↔ E/B-imbalance relation from
[`projects/grid-primitive/02-wave-on-a-primitive.md`](../projects/grid-primitive/02-wave-on-a-primitive.md)
and accounting for the magnitude gap between electron and
hadronic anomalies.  If validated, it converts the most
precisely measured number in physics (a_e to 12 digits) into a
direct measurement of the cylinder primitive's stiffness ratio.

**Related:**
  [Q132](Q132-promotion-chain-principle.md) (promotion chain — sheet sign conventions),
  [Q136](Q136-nature-of-aleph-dimensionality.md) (1D aleph; eddies as 1D circulation),
  [Q137](Q137-alpha-as-aleph-aspect-ratio.md) (α as substrate aspect ratio; light-current / light-voltage inversion in §10c),
  [`projects/grid-primitive/README.md`](../projects/grid-primitive/README.md) (cylinder primitive, theory 4 equipartition, open question 6 on E/B asymmetry),
  [`projects/grid-primitive/02-wave-on-a-primitive.md`](../projects/grid-primitive/02-wave-on-a-primitive.md) §7 (equipartition picks χ̃ = 1/√2),
  [`grid/foundations.md`](../grid/foundations.md) (axiom A6 — α as input),
  [R47 study](../studies/R47-proton-filter/) (SU(6) μ_p = 3, μ_n = −2 from torus topology).

---

## 1. The question

The cylinder primitive of [`projects/grid-primitive`](../projects/grid-primitive/)
has two coupled internal fields — longitudinal strain *e(x, t)*
and azimuthal phase *φ(x, t)* — connected by a shear stiffness
*K_eφ*.  The dimensionless shear ratio is:

<!-- χ̃ = K_eφ / √(K_ee · K_φφ) -->
$$
\tilde{\chi} \;=\; \frac{K_{e\varphi}}{\sqrt{K_{ee}\,K_{\varphi\varphi}}} \;\in\; (0, 1)
$$

Chapter 2 of `grid-primitive` establishes that **χ̃ = 1/√2** is
the equipartition value: at this χ̃, the strain channel
(E-like) and phase channel (B-like) carry equal time-averaged
energy.  The README's open question 6 flags the consequence:
*"the non-precise shear χ̃ ≠ 1/√2 may imply that the strain and
phase channels carry unequal shares of the wave content.  If
so, that asymmetry would land somewhere observable — possibly
in the relative roles of B and H."*

This question proposes a specific landing site:

> **Is the anomalous magnetic moment of charged particles
> (electron a_e, proton anomaly relative to SU(6), neutron
> anomaly) the macroscopic manifestation of the GRID primitive's
> chirality deviating slightly from the equipartition value
> 1/√2 — with the deviation direction set by each MaSt sheet's
> wrap chirality (sign convention)?**

If yes:

- Charge quantization remains exact (it comes from topological
  winding, independent of χ̃).
- Magnetic moment is *not* exactly quantized; its small
  deviation from the integer / SU(6) prediction tracks the E/B
  channel imbalance.
- The sheet sign conventions (sign_e = +1, sign_p = −1,
  sign_ν = +1 in R60 model-F) determine the direction of the
  channel-imbalance-induced deviation per sheet.
- The most precisely measured number in physics (a_e to 12
  digits) becomes a direct measurement of the cylinder
  primitive's stiffness ratio δχ̃ = χ̃ − 1/√2.

## 2. The structural argument

Three pieces converge.

### 2.1. Equipartition picks χ̃ = 1/√2 as the natural value

[`projects/grid-primitive/02-wave-on-a-primitive.md`](../projects/grid-primitive/02-wave-on-a-primitive.md) §7
derives this directly:

- Inside the stable range χ̃ ∈ (0, 1), no value is preferred on
  stability grounds alone.
- Equipartition between the strain and phase channel energies
  reduces to *K_eφ*² = (1/2) *K_ee K_φφ*, i.e. χ̃ = 1/√2.
- A parallel argument from thermodynamic equilibrium (equal
  populations of L-circular and R-circular natural modes) gives
  the same answer.

This is the *natural* value but not the *forced* value.  The
README §"Open questions" #1 leaves open whether matching the
lattice signal speed *c* fixes χ̃ uniquely or admits a family.
If χ̃ deviates from 1/√2 by a small δχ̃, the channels are
imbalanced — strain channel and phase channel carry slightly
different energy shares.

### 2.2. The strain ↔ E and phase ↔ B identification

The [`grid-primitive` README](../projects/grid-primitive/README.md)
theory 8 says: *"Maxwell's E and B emerge as the strain-channel
and phase-channel components of the wave."*  This is the
projection that connects the cylinder primitive's internal
fields (*e*, *φ*) to the macroscopic Maxwell fields (E, B) at
the lattice coarse-graining (handled in chapter 6 of the
project, which bridges to [`grid/maxwell.md`](../grid/maxwell.md)).

Under that identification, a deviation δχ̃ from equipartition
maps directly to an E ↔ B channel-energy imbalance at the
lattice scale, hence to an asymmetry between electric and
magnetic field magnitudes for any wave content carried by the
primitive lattice.

### 2.3. Sheet sign conventions break the symmetry directionally

R60 model-F uses sign conventions per sheet:

| Sheet | sign |
|---|:---:|
| Electron (e) | +1 |
| Proton (p) | **−1** |
| Neutrino (ν) | +1 |

The proton sheet's sign is opposite to the others.  These signs
appear in metric off-diagonals (σ_ta multiplied by sheet sign)
and represent the wrap chirality of each MaSt sheet.  Under the
hypothesis here, this sign — which already exists for entirely
independent reasons in R60's α-architecture — is also what sets
the *direction* of the χ̃-deviation-induced E/B imbalance per
sheet.

The chain:

1. The cylinder primitive has a fixed but slightly non-optimal
   χ̃ = 1/√2 + δ (where δ is the same magnitude on every
   primitive — substrate property).
2. A sheet wraps the primitives into a closed surface with
   chirality given by its sheet sign.
3. The interaction of the primitive's chirality with the sheet's
   wrap chirality determines whether the strain channel or
   phase channel is enhanced — opposite for opposite sheet
   signs.
4. e-sheet (sign +1): primitive chirality aligns with sheet
   wrap → phase channel slightly enhanced → B slightly larger
   → **a_e > 0** (observed).
5. p-sheet (sign −1): primitive chirality opposes sheet wrap →
   phase channel slightly diminished → B slightly smaller →
   **μ_p < 3 μ_N (SU(6))** (observed: 2.79 vs 3.00).

The observed signs of the anomalies match this prediction.  The
sign opposition (electron anomaly positive; proton deviation
from SU(6) negative) follows from the sign opposition of the
sheets in R60 — a structural feature already in the framework
for unrelated reasons.

## 3. What the hypothesis predicts

Under this reading:

- **Charge quantization is exact.**  Topological winding number
  on a closed compact dimension is integer-valued and unaffected
  by χ̃.  The elementary charge e is fixed regardless of where
  in (0, 1) the primitive's χ̃ sits.  This matches observation:
  charge is observed to be quantized to extreme precision.
- **Magnetic moment is not exactly quantized.**  It tracks the
  E/B channel balance, which varies continuously with χ̃.  Its
  deviation from the integer or SU(6) prediction reflects δχ̃.
- **The deviation has a fixed sign per sheet.**  Sheet sign
  conventions (sign_e, sign_p, sign_ν) determine direction.  All
  particles on the same sheet share the same anomaly sign.
- **The deviation magnitude is small.**  δχ̃ should be ≪ 1
  (otherwise other observables would notice); the resulting
  channel imbalance is correspondingly small.

Comparing to standard QED: a_e ≈ α/(2π) ≈ 1.16 × 10⁻³.  If this
emerges from δχ̃²-level effects (channel imbalance is quadratic
in deviation from equipartition), then δχ̃ ≈ √(α/2π) ≈ 0.027 —
a ~3.8% deviation from 1/√2.

That number is not derived here but is the back-calculation if
the hypothesis maps a_e directly to δχ̃² at the primitive level.
It is the quantitative test.

## 4. Quantitative obstacles

The hypothesis matches qualitatively but has open quantitative
issues that need closing before it can be considered validated.

### 4.1. Closed-form δχ̃ ↔ E/B imbalance relation

The structural claim "δχ̃ ≠ 0 imbalances E and B channels" is
correct from chapter 2 of `grid-primitive`, but the precise
relation has not been written down.  Specifically:

- At χ̃ = 1/√2, channels carry equal energy.  Define
  R_E = (E-channel energy) / (total energy) and R_B = (B-channel
  energy) / (total energy); at equipartition R_E = R_B = 1/2.
- For χ̃ = 1/√2 + δ, the imbalance ΔR = R_B − R_E should be a
  function of δ that vanishes at δ = 0 and grows as δ moves away
  from zero.
- Whether ΔR is linear, quadratic, or higher-order in δ
  determines the magnitude of the predicted anomaly per unit δχ̃.

Chapter 2 §5 has the eigenvector expressions
(**v**_+ = (cos θ, sin θ), **v**_− = (−sin θ, cos θ)) and notes
that the mixing angle θ rotates with χ̃.  Computing the
time-averaged energy in each channel for the natural mode
amplitudes and expanding around χ̃ = 1/√2 should give the
δχ̃ ↔ ΔR relation directly.

This is a paper-math calculation that has not yet been done in
`grid-primitive` and is the **first concrete deliverable** for
testing the hypothesis.

### 4.2. The magnitude gap between electron and hadronic anomalies

| Particle | Anomaly fraction | Order |
|---|---:|---:|
| Electron | a_e = 1.16 × 10⁻³ | 10⁻³ |
| Proton (vs SU(6) 3.00) | (3 − 2.79)/3 ≈ 0.07 | 10⁻¹ |
| Neutron (vs SU(6) −2.00) | (2 − 1.91)/2 ≈ 0.045 | 10⁻¹ |

The proton anomaly is ~60× larger than the electron's.  If
both are produced by the same δχ̃ at the primitive level,
something has to amplify the proton case.

Three candidate amplification mechanisms (need to choose
between them or combine):

1. **Composite-particle structure.**  The proton has 3 quark
   primitives; if each contributes a δχ̃-scale anomaly and they
   add coherently with the SU(6) flavor-spin combination, the
   net could be 3× to 9× the single-quark contribution.  Plus
   internal QCD-like correlations could amplify further.
   Standard hadronic physics says exactly this; the question is
   whether the same numerical amplification carries through in
   the cylinder primitive picture.
2. **Sheet-dependent δχ̃.**  If the cylinder primitive on the
   p-sheet has a different δχ̃ than on the e-sheet (because the
   different `(ε_p, s_p)` calibration imposes different
   geometric constraints), the magnitudes can naturally differ.
   This sacrifices the "single substrate property δχ̃" reading
   but keeps the sign-opposition story.
3. **Different contributing modes.**  The electron anomaly may
   only count the lowest mode (Schwinger-style one-loop), while
   the proton anomaly counts the full mode spectrum.  In MaSt,
   this could correspond to per-sheet differences in which
   harmonic modes dominate.

None of these is established; one of them needs to land for the
quantitative test to pass.

### 4.3. The neutron's separate magnitude

Proton anomaly is 7%; neutron is 4.5%.  Different magnitudes on
the *same* p-sheet means the simple hypothesis "p-sheet has one
δχ̃, applied uniformly" is incomplete — the n_pr quantum number
(which differs between proton +2 and neutron −2) must enter the
amplification.  This is consistent with the SU(6) picture (where
proton and neutron have different mode structure on the same
sheet), but the hypothesis needs to specify how n_pr couples to
the channel imbalance.

### 4.4. Reconciliation with Schwinger's QED result

Schwinger's a_e = α/(2π) is derived from a one-loop QED Feynman
diagram (electron emitting and reabsorbing a virtual photon).
This is a solid result of standard physics.  If Q139's hypothesis
is correct, then the *same* numerical answer must come out of
the cylinder-primitive picture via the δχ̃ mechanism — meaning
δχ̃ effectively encodes the one-loop QED correction at a
substrate level.

This is testable: derive the δχ̃ → a_e relation from the
primitive (per §4.1), back-calculate δχ̃ from observed a_e, and
check whether the resulting δχ̃ is consistent with other
substrate constraints (entropy bound from chapter 4, signal
speed from chapter 3, etc.).

## 5. The "edge shear from anomalies" inversion

If the hypothesis is right, the following inversion is feasible:

1. Measure a_e to high precision (already done; PDG value to 12
   digits).
2. Use the closed-form δχ̃ ↔ a_e relation (§4.1's deliverable)
   to back-calculate δχ̃.
3. Cross-check by computing δχ̃ from a_p (with the magnitude
   amplification of §4.2 accounted for) and confirming
   consistency.
4. Use δχ̃ as a constraint on the cylinder primitive's
   stiffness matrix entries.

This would be a remarkable result: the most precisely known
number in physics becoming a direct measurement of GRID
primitive geometry.  It would also tighten the framework's free
parameter count — δχ̃ goes from "presumed small" to "measured
at 0.027" (or whatever the calculation gives), removing one
degree of freedom from the substrate.

## 6. Distinction from existing α-related questions

This question is *complementary* to Q137 (α as aspect ratio),
not in tension with it:

- **Q137 asks**: what is α physically?  Answer: substrate aspect
  ratio (d/L) of the aleph thread, manifesting dynamically as
  per-junction retention κ ≈ 1 − ε(α).
- **Q139 asks**: what is the anomalous magnetic moment?  Answer:
  the deviation of the cylinder primitive's chirality from
  equipartition, projected through sheet wrap chirality.

Both treat α-related observables as *substrate properties*,
which is consistent with Q137's overall framing.  Q139 is more
specific: it picks out the *deviation from optimum* as the
source of a small correction, where Q137 picks out the *aspect
ratio itself* as the source of α.

The two could end up related — δχ̃ might itself be α-related, or
not — but at the level of the hypothesis, they are independent
claims.

## 7. Open issues

- **Can δχ̃ produce the right magnitude of a_e?**  §4.1 closure
  required.
- **Can the same δχ̃ (or sheet-dependent δχ̃) produce the
  hadronic anomalies?**  §4.2 closure required.
- **What sets δχ̃?**  If δχ̃ is structurally fixed (substrate
  property), it should be derivable from chapter 3 of
  grid-primitive (the lattice signal speed constraint).  If
  it's a free parameter, the framework gains a fit point.
- **Is δχ̃ correlated with α?**  If a_e ≈ α/(2π) and a_e ≈ f(δχ̃)
  for some function f, then δχ̃ is implicitly α-dependent.
  Whether this is an accident or structural is open.
- **Compatibility with R47's SU(6) result.**  R47 derived
  μ_p = 3 μ_N and μ_n = −2 μ_N from torus topology.  Q139's
  hypothesis would correct these by δχ̃-scale amounts.  The
  combined picture (R47 + Q139) needs to give the observed
  values; this requires the amplification calculation (§4.2)
  to come out right.

## 8. If validated

Significant consequences for the framework:

- **Anomalous magnetic moment is a substrate-geometry
  measurement.**  Standard QED's perturbative loop expansion is
  reframed as a coarse-grained effective theory; the actual
  mechanism is δχ̃ at the GRID-primitive level.
- **The cylinder primitive's free parameters tighten.**  δχ̃
  becomes constrained by precision measurement, removing one
  parameter from the substrate's parameter space.
- **Sheet sign conventions get a second physical role.**  They
  already determine α-architecture sign in σ_ta; they would now
  also determine anomaly direction per sheet.  This tightens the
  framework's structural connections.
- **A novel structural insight worth communicating.**  Coupling
  the precision of a_e to a geometric property of the lattice
  substrate would be a substantive new connection between
  precision QED and the GRID picture.

## 9. If falsified

If §4.1's closed-form derivation produces a magnitude
inconsistent with observed a_e, or if §4.2's amplification
cannot reconcile electron and proton anomalies, the hypothesis
fails — but the failure is informative:

- It would mean the cylinder primitive's chirality is fixed at
  exactly 1/√2 (no deviation), or that the deviation produces
  a different observable than the magnetic moment, or that the
  observable is saturated by other contributions (R47 SU(6) +
  QCD hadronic) and δχ̃ contributes negligibly.
- The grid-primitive project's open question 6 (E/B asymmetry
  landing somewhere observable) remains, with the magnetic
  moment ruled out — pushing the search to other candidates
  (susceptibility ratios, polarization asymmetries, etc.).

## 10. Recommended path forward

In priority order:

1. **§4.1 deliverable: derive δχ̃ ↔ E/B imbalance from
   chapter 2.**  Pure paper math, no simulation needed.  Should
   take a single careful sitting on the eigenvector / energy
   formulas in §5 of `02-wave-on-a-primitive.md`.
2. **Plug in observed a_e and extract δχ̃.**  Trivial once §1
   is done.
3. **Apply to a_p with composite-amplification estimate.**
   Either via SU(6)-based mode counting (R47 framework) or via
   sheet-dependent δχ̃ (sub-hypothesis to test separately).
4. **If both come out consistent, the hypothesis is validated
   and an entry to grid-primitive project chapter 4 or 5 is
   warranted.**
5. **If inconsistent, document the inconsistency and revise or
   abandon.**

A concrete first computation is bounded: a few hours of careful
algebra on the existing chapter-2 setup gives the §4.1
relation.  That's the cheapest decisive test.
