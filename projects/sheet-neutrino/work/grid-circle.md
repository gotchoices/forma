# GRID circle, Stage 1: the lepton-domain circle on a GRID lattice

Experiment for host G ([lepton-domain-circle.md](lepton-domain-circle.md)). Script: [../scripts/grid_circle.py](../scripts/grid_circle.py).

## Question

Does the lepton-domain circle, built as an actual GRID graph rather than with a free junction strength, give:
1. a near-degenerate ν₁/ν₂ pair plus a separated ν₃, with Δm²₃₁/Δm²₂₁ ≈ 33.6;
2. mixing weights resembling the measured ones?

## Setup

- **Graph:**
  - the neutrino line: a ring of three segments with l₁, l₂, l₃ edges;
  - the shared electron circle: at each junction, a small closed loop of ℓ edges, which makes the junction a 4-edge node;
  - optionally, the Klein flip: one sign-flipping edge per segment.
- **Dynamics:** the grid-duality Scattering model. Each edge carries two registers, one per direction. At every node with N edges the scattering is S = (2/N)·J − I, which is lossless, and a flipped edge negates what crosses it. The one-step update is a fixed orthogonal matrix, whose eigenvalues e^{iω} give the exact mode frequencies. Mass ∝ ω.
- **Fit fractions:** the share of a mode's energy on each segment.
- **Mixing:** for each segment, the combination of the three lowest modes most concentrated there, which serves as that segment's flavor state. |U|² is then each mode's weight in each flavor.
- **Validation:** the update is orthogonal; a plain ring gives ω = 2πn/N, each value a degenerate pair; one flip gives the half-integer set π(2n+1)/N.

## Results

**1. Equal segments give an exactly degenerate pair** (to 10⁻¹⁴), as the 3-fold symmetry predicts. ν₃ sits at ω₃/ω₁ ≈ 2.0 without flips and ≈ 2.7–2.9 with them.

**2. Small loops barely scatter.** A loop much smaller than the wavelength is nearly transparent. Every mode spreads almost evenly over the three segments (fit fractions ≈ ⅓ each), and the most-concentrated flavor states have localization 0.5–0.6, where ⅓ means none.

**3. The junction's effect scales as loop size / ring size:**

| Loop / ring | Shift of ω₁ | Pair split, segments (b − 8, b, b + 8) |
|---|---|---|
| 0.133 | 0.180 | 7.4×10⁻² |
| 0.067 | 0.095 | 4.5×10⁻² |
| 0.017 | 0.025 | 1.3×10⁻² |
| 0.004 | 0.006 | 8.6×10⁻⁴ |

The shift is ≈ 1.45 × (loop/ring) at every lattice size tested.

**4. The measured ratio is reachable only with large loops.** Scanning segment lengths around 40 edges:

| Loops | Flips | Closest ratio |
|---|---|---|
| 2 edges | off | 77.5 |
| 2 edges | on | 393 |
| 8 edges | on | 101 |
| 8 edges | off | **33.5** at segments (34, 40, 51) |

In the one case that reaches 33.5, the loop is about 1/15 of the ring and the segments differ by up to 50%. The mixing there is large, but its rows do not resemble the measured ones; for example, the largest ν₃ content in a flavor dominated by ν₁ is 0.22, against 0.02 for ν_e.

## Conclusion

**The small-loop junction is obstructed at physical scale.** The electron circle is about 10⁷ times smaller than the neutrino line. By the scaling in result 3, such a junction is essentially transparent, so the three segments behave as one uniform ring:
- segment lengths cannot split the pair, and the ratio stays far above 33.6;
- flavor states cannot localize on their segments.

What is obstructed is this specific junction, a small loop attached at a node. The circle itself is not ruled out. The degenerate pair from symmetry (result 1) and the factor of about 2 or 3 for ν₃ hold in every case.

## What a working junction needs, and a candidate

The junction must scatter strongly, and its strength must not shrink with the electron circle's size. One GRID-native way, using the lepton-domain idea itself:

- **Impedance steps between segments.** Each segment is a ribbon whose width is set by its shared electron dimension, and the e, μ, τ dimensions differ in size. Where ribbons of different width meet, a wave sees an impedance step and partly reflects, as at the joint between two transmission lines of different impedance. The reflection depends on the *ratio* of widths, not on how small they are.

## Stage 1b: ribbons of different widths

**Model.** Each segment is a GRID ribbon of w parallel chains, closed transversely by rungs. Each junction is one node joining the chain ends of two segments. For a wave uniform across the ribbon, GRID's node rule gives exactly the transmission-line impedance-step reflection, **R = (w_a − w_b)/(w_a + w_b)**, so the long-wavelength physics reduces to a ring with those reflections at its junctions.

**Validation.** The full ribbon graph and the reduced ring give the same frequency ratios to four digits. The frequencies themselves differ by one constant factor (0.686), because the ribbon carries waves more slowly. Run with `--lens … --widths … [--ribbon]`.

**Scan.** Width ratios w₂/w₁, w₃/w₁ ∈ {1, 1.25, 1.5, 2, 3, 5}, segment lengths 40 ± 10 edges, Klein flips off and on (`--width-scan`, ≈ 45 min). Configurations within 2% of the measured ratio were scored against the measured mixing matrix (rms difference of |U|², best row ordering).

| Flips | Hits | Best mixing distance | ω₃/ω₁ | Width contrast in hits |
|---|---|---|---|---|
| off | 18 | 0.19 | ≈ 2.0 | 1 to 1.25 |
| on | 337 | 0.14 | ≈ 3.2 | 1 to 1.25 |

Best case (flips on, segments 32/40/48, widths 1/1.25/1):

| Flavor | ν₁ | ν₂ | ν₃ |
|---|---|---|---|
| 1 | 0.54 | 0.25 | 0.20 |
| 2 | 0.01 | 0.57 | 0.42 |
| 3 | 0.44 | 0.18 | 0.38 |
| *measured ν_e* | *0.68* | *0.30* | *0.02* |

**Findings:**
1. **The impedance step works as a junction,** and its strength is independent of how small the electron dimension is: the Stage 1 obstruction is removed.
2. **The mass ratio needs only a small width contrast,** about 25%. Larger contrasts split the pair too much.
3. **At that contrast the modes stay spread over the whole circle.** Fit fractions are at most about 0.44 per segment, nothing like 80%, and flavor localization is 0.4–0.7.
4. **The mixing has the wrong structure.** ν₃ makes up 20–40% of *every* flavor, while the measured ν_e contains only 2% ν₃ (the small angle θ₁₃). A mode spread evenly over all three segments cannot be nearly absent from one of them.

**Status:** the ring-with-impedance-steps form of host G reproduces the mass ratio but not the mixing. Two possible ways forward:
- the mixing result depends on defining a flavor as "the combination most concentrated on a segment"; coupling at specific points (the junctions) might behave differently;
- a small θ₁₃ needs ν₃ to have a node, or near-node, on one flavor's site. That could come from structure beyond three uniform segments.
