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

**Next experiment (Stage 1b):** model the segments as GRID ribbons of different widths and repeat the spectrum and mixing analysis.
