# Junction fit: what the lepton-domain circle's junctions must do

Experiment for host G ([lepton-domain-circle.md](lepton-domain-circle.md)), following [grid-circle.md](grid-circle.md). Script: [../scripts/junction_fit.py](../scripts/junction_fit.py). Raw output: `../outputs/jf_*.txt`.

## Question

Stage 1b found that impedance steps (ribbon width changes) give the right mass ratio but the wrong mixing. Width changes can set only two of the three junction reflections, and no reflection phases. So instead of starting from a mechanism, start from the data: **if each junction could reflect any amount, what would the junctions have to do to reproduce neutrino behavior?** Then ask what physics could make them do it.

**Terms.** *CP* is the combination of C (swap particles for antiparticles) and P (mirror reflection). *CP violation* in oscillation means neutrinos and antineutrinos oscillate differently. It is controlled by a phase δ in the mixing matrix: δ = 0 or π means none, other values mean some. CP violation is equivalent to violation of time-reversal symmetry (T). Fuller definition: [experimental-constraints §5](../reference/experimental-constraints.md#5-oscillation-and-mixing).

## Model

- **Circle:** three segments of adjustable length, joined end to end.
- **Junction:** a general lossless two-way scatterer. It reflects a fraction r of the wave's amplitude and passes the rest (t = √(1 − r²)), optionally with an extra reflection phase α. A ribbon width change is the special case r = (w_a − w_b)/(w_a + w_b), α = 0.
- **Klein flips:** on or off. On, the circle closes with one net sign change.
- **Masses:** the three lowest modes; mass ∝ wavenumber k.
- **Flavor:** a neutrino is created and detected at a junction, where its charged lepton couples. The flavor state is what a coupling at that point excites. The three such states are made orthonormal with the least change (symmetric orthonormalization). A second definition, flavor = "the combination most concentrated on a segment," is reported separately.
- **Fit targets:** the mass ratio Δm²₃₁/Δm²₂₁ = 33.6 and the five mixing entries that do not depend on the poorly known CP phase δ: the electron row (0.678, 0.300, 0.022) and the ν₃ column (|U_μ3|² = |U_τ3|² = 0.489, taking sin²θ23 = 0.5).
- **Validation:** with no reflection the model gives a plain loop's modes (k = 1, 1, 2, or ½, ½, 3/2 with flips), and the impedance-step case matches Stage 1b.

**Counting.** Each row and column of the mixing matrix sums to 1, so the targets amount to four independent numbers: two from the electron row, one from the ν₃ column, and the mass ratio. The model has five free numbers (two length ratios, three reflections), plus three phases when allowed. Exact fits are therefore expected. The informative parts are the *shape* of the solutions and what they imply for entries that were not fitted.

## Results

Exact fits were found in every run: point flavors with flips off, with flips on, and with flips and phases (loss ≈ 10⁻¹²–10⁻¹⁴), and segment flavors with flips on (loss 3×10⁻⁷). With segment flavors, each flavor state is 99%, 80%, and 97% concentrated on its own segment: a neutrino of a given flavor "fits" mainly one segment, and only partly the other two. Representative fits:

| Run | Segment lengths (fraction of circle) | Junction reflections r | ν₃/ν₁ | Masses (meV), Σm |
|---|---|---|---|---|
| flips off | 0.49, 0.25, 0.26 | −0.992, −0.100, −1.000 | 2.95 | 18, 20, 53; 92 |
| flips off | 0.05, 0.44, 0.52 | −0.006, +0.993, +1.000 | 3.07 | |
| flips on | 0.50, 0.21, 0.28 | +0.889, +0.101, +0.942 | 3.01 | 18, 20, 53; 91 |
| flips on | 0.06, 0.58, 0.37 | +0.987, +0.990, −0.679 | 3.32 | |
| flips on, phases | 0.22, 0.51, 0.27 | −0.872, −0.564, +0.821 (α = −0.96, 0.11, −0.20) | 3.35 | 16, 18, 53; 86 |
| flips on, **segment flavors** | 0.49, 0.15, 0.36 | −0.910, −0.224, −0.876 | 3.01 | 18, 20, 54; 92 |

(An earlier version of this table came from a run with a normalization error, which overweighted short segments. The numbers above are from the corrected script.)

**Three findings hold across all fits:**

1. **Two junctions strongly reflecting, one weak.** In every fit, two junctions reflect strongly (|r| ≈ 0.82–1.000) and the third weakly or moderately (|r| ≈ 0.006–0.68). The circle behaves as coupled chambers, not as a uniform ring. Every fit also gives ν₃/ν₁ ≈ 3 (2.9–3.35) and Σm ≈ 86–92 meV, close to the ½ : ½ : 3/2 pattern of a half-wave cavity, even with the flips off.
2. **Width changes cannot do this.** The strongest reflections imply width ratios of hundreds to one, and the ratios' product around the circle is far from 1, which width changes alone require. The junctions need physics beyond a change of ribbon width (see the construction below).
3. **The mixing comes out CP-conserving.** The entries that were not fitted, the remaining μ- and τ-row values, come out exactly as δ = 0 or π requires: μ and τ rows (0.230, 0.281, 0.489) and (0.093, 0.418, 0.489), in either order. This is structural. These junctions are reciprocal (they treat the two travel directions alike), which for a single-channel wave is the same as time-reversal symmetry, and time-reversal symmetry forbids CP violation in oscillation. **Prediction:** with reciprocal junctions, neutrino oscillation conserves CP. A nonzero CP phase would need a non-reciprocal element. The one Forma has is the grid's direction bias χ_anti ([grid-primitive ch. 9](../../grid-primitive/09-chirality-asymmetry.md)), which ma-domain already proposed as the source of δ_CP. Current data mildly favor CP violation but still allow δ = π in normal ordering; DUNE and Hyper-Kamiokande will test it.

## A construction to visualize

**1. Three chambers in series.** The neutrino line is a long closed loop, divided into three stretches. Each stretch is a thin tube: the long direction is the neutrino line, and around it runs a tiny circle, the small dimension. In each stretch that small circle is a *different* material dimension: the electron's in the first stretch, the muon's in the second, the tau's in the third.

**2. Handing the small dimension from one stretch to the next.** At a junction the tube's cross-section must change from a circle in one dimension to a circle in another. A 3D analogy: an hourglass whose upper bulb is round in the horizontal plane, and whose lower bulb opens out in a vertical plane. The two bulbs meet at a narrow **neck**. Here the "bulbs" are the two tubes, and the neck is where the cross-section circle shrinks, then re-opens in a different dimension.

**3. Why a neck reflects.** A wave arriving at a narrow neck mostly bounces back, the way a waveguide reflects at a narrow iris or a pipe echoes at a sudden constriction. On a GRID ribbon, a wide ribbon narrowing to a single chain reflects (w − 1)/(w + 1) of the amplitude, which is close to 1 for a wide ribbon. A neck is short, so it does not count as a segment of its own, and it escapes the width-product rule.

**4. The fitted pattern in these terms.** Two of the hand-offs are tight necks (strong reflection). The third is a gentle hand-off: the cross-section rotates gradually from one dimension into the other, with only mild reflection. The result is a **coupled-cavity resonator**, the same structure as a microwave filter built from cavities joined by irises:
- the mass states are the resonances of the whole chain;
- a flavor is what you excite by driving the circle at one hand-off point;
- the mixing records how much each resonance is present at each driving point.

**5. Where the Klein flip sits.** Each stretch also carries the flip. Going along it reverses the orientation of its small circle. The flips change the resonances' closure (half-integer instead of integer) but are not what makes the fit work: fits exist with and without them.

Steps 2–4 are an interpretation that has not been derived. In particular, whether the neck physically has to be tight where two *different* dimensions hand off is an open question.

## Test 1: GRID necks as the junctions

**Question.** Can necks, narrow sections of ribbon, provide the junctions the fit asks for?

**Validation on the GRID graph.** A neck was built as a short narrow ribbon between wide ones, in the full ribbon graph and in the reduced model.
- Frequency ratios agree to about 1%. The residual is the 2D lattice's slight wave-speed variation.
- Two lattice details matter. A ribbon narrower than 3 chains has no cross-links and carries waves faster (by 1/0.686), so it is electrically shorter than its edge count. And each piece of the ribbon graph has one more edge in series than its nominal length.
- Neither changes the fit, because neck length is a free parameter (read it as electrical length).

**Model.** Each junction is a step from segment width down to neck width (ratio ρ), a neck of adjustable length, and a step back up. Its reflection grows with ρ and with neck length relative to the wavelength. For example, at ρ = 20:

| Neck length (fraction of circle) | \|R\| at ν₁ | \|R\| at ν₃ |
|---|---|---|
| 1% | 0.30 | 0.68 |
| 5% | 0.84 | 0.98 |
| 20% | 0.99 | 0.99 |

Unlike the free junctions, a neck reflects more at higher frequency.

**Results:**

| Run | Neck narrowness ρ | Neck lengths (% of circle) | \|R\| at ν₁ | ν₃/ν₁ | Loss |
|---|---|---|---|---|---|
| flips on | 84, 43, 78 | 1.6, 0.7, 1.2 | 0.72, 0.23, 0.59 | 3.03 | 2×10⁻¹⁴ (exact) |
| flips on | 157, 31, 8 | 0.8, 3.1, 3.4 | 0.69, 0.60, 0.21 | 3.24 | 1×10⁻¹³ (exact) |
| flips off | 1.6, 110, 1.3 | 3.5, 0.06, 3.1 | 0.10, 0.20, 0.05 | 2.02 | 6×10⁻⁴ (near miss) |
| flips on, segment flavors | 6258, 1123, 5693 | 2.8, 2.8, 2.3 | 1.00, 0.92, 1.00 | 3.63 | 3×10⁻⁴ (near miss) |

**Findings:**
1. **Necks work, with the Klein flips on.** Narrowness ratios of tens to about a hundred, over lengths of 1–3% of the circle, reproduce the mass ratio and the CP-independent mixing entries exactly. The unfitted entries again come out CP-conserving.
2. **The pattern softens.** At ν₁'s wavelength the neck reflections are moderate (two about 0.6–0.7, one about 0.2), not the near-total values the frequency-independent junctions needed. Because a neck reflects more strongly at higher frequency, it reaches the same spectrum and mixing with milder junctions.
3. **The segment-flavor search** (12 restarts) did not reach an exact fit either. Its best attempt drifted to necks thousands of times narrower than the segments, which nearly seals the chambers apart, so that result is inconclusive rather than informative. The exact fits above use the point-flavor definition.
4. **Without flips, the necks did not reach an exact fit** in 30 restarts. The best near miss puts 4% of ν₃ in ν_e (measured: 2%) and has ν₃/ν₁ ≈ 2. With necks, then, the Klein flip may be needed. A search is not a proof, so this is tentative.
5. **What a neck needs physically.** The neck must be much narrower than the segments in the dimension that carries the wave across the junction. In the construction above that is the pinch where the cross-section circle shrinks before re-opening in another dimension. Ratios of tens to a hundred mean the pinch is tight, but nothing in the fit requires an extreme value.

## Test 2: is the grid's direction bias needed?

The fits predict CP-conserving oscillation, because their junctions are reciprocal. CP violation would require a non-reciprocal element, and the candidate in Forma is the grid's direction bias. The policy is to bring it in only if the data require it. So the question is whether current data require CP violation.

**Current data (checked October 2026):**
- **NuFIT 6.0** (global fit, data to September 2024): in **normal ordering** the data are consistent with CP conservation within 1σ. In inverted ordering, CP-violating values near δ = 270° are favored over conservation at more than 3.6σ ([arXiv:2410.05380](https://arxiv.org/abs/2410.05380)).
- **T2K + NOvA joint analysis** (Nature, 2025): no preference yet between the orderings. If inverted ordering is assumed, the result is evidence for CP violation ([T2K announcement](https://t2k-experiment.org/2025/10/rival-neutrino-experiments-nova-and-t2k-publish-first-joint-analysis/)).

**Result: not needed now.** Every fit here has the near-degenerate pair as the two *lowest* states, which is normal ordering, and in normal ordering CP conservation is allowed. The model's two commitments, normal ordering and no CP violation, are consistent with each other and with current data. Inverted ordering has not been tried in this model.

**What would make it needed.** A measurement establishing δ ≠ 0, π in normal ordering (DUNE and Hyper-Kamiokande are designed to reach this). If inverted ordering were established instead, which JUNO is designed to settle, the model as fitted would fail on ordering first. CP violation would then be required as well.

## Status and next steps

- **Favorable but not decisive.** With arbitrary junctions the circle can host the measured masses and mixing, which is not surprising given the parameter count. It points to a specific structure (two tight necks, one gentle hand-off, ν₃ ≈ 3 × ν₁) and makes a structural prediction (CP conservation unless the grid's direction bias acts).
- **Next:**
  - map the family of solutions, since the fits differ widely in segment lengths and mass scale.
- Both flavor definitions give the same structure and the same unfitted (CP-conserving) entries, so the conclusions do not hinge on how flavor is defined.
