# Q111: Does the neutrino sheet have its own coupling constant?

**Status:** Open — numerical result from known geometry; interpretation speculative
**Related:**
  [Q77](Q77-alpha-as-impedance.md) (α as impedance mismatch),
  [Q18](Q18-deriving-alpha.md) (deriving α),
  [Q102](Q102-neutrino-neutrality-from-sheet-size.md) (neutrino neutrality),
  [R49](../studies/R49-neutrino-filter/findings.md) (neutrino mode families, F26–F28),
  [R26](../studies/R26-neutrino-t4/findings.md) (Assignment A),
  [`model-D.md`](../models/model-D.md) (sheet parameters)

---

## 1. Background

The R19 formula derives the fine-structure constant α from
two geometric parameters of a sheared torus — the aspect
ratio ε (tube circumference / ring circumference) and the
within-plane shear s:

<!-- α(ε, s) = ε² μ sin²(2πs) / (4π(2−s)²),  μ = √(1/ε² + (2−s)²) -->
$$
\alpha(\varepsilon, s) = \frac{\varepsilon^2\,\mu\,\sin^2(2\pi s)}{4\pi\,(2-s)^2},
\qquad \mu = \sqrt{\frac{1}{\varepsilon^2} + (2-s)^2}
$$

On the electron and proton sheets, the shear is *derived*
by setting α(ε, s) = 1/137.036 and solving for s at each
sheet's known aspect ratio.  Different ε values yield
different shear values, but the output is the same: α = 1/137.
This makes physical sense — both sheets carry electric charge
and couple to the same electromagnetic field in spacetime S.

| Sheet | ε | s | α(ε, s) |
|-------|---|---|---------|
| Ma_e (electron) | 0.65 | 0.09594 | 1/137.0 |
| Ma_p (proton) | 0.55 | 0.11101 | 1/137.0 |

The neutrino sheet is different.  Its shear is not derived
from α; it is derived from the neutrino oscillation mass
ratio (Δm²₃₁/Δm²₂₁ = 33.6).  R26 showed that for
Assignment A the ratio depends only on shear — the aspect
ratio cancels completely:

<!-- R = (3 − 2s) / (4s)  →  s = 3 / (4R + 2) -->
$$
R = \frac{3 - 2s}{4s}
\qquad\Longrightarrow\qquad
s = \frac{3}{4R + 2}
$$

This is an exact analytical result.  At the project
reference value R = 33.5989, it gives **s_ν = 0.021995**.

## 2. The question

What happens if we evaluate the same geometric formula
on the neutrino sheet using its known parameters?

## 3. The conditional chain

### If:

1. **The three lowest spin-½ modes on the neutrino torus
   are the three neutrino mass eigenstates** — i.e.,
   Family A of R49 is correct: (1,1), (−1,1), (1,2)
   at ε_ν = 5.

2. **The shear s_ν = 0.022 that reproduces the oscillation
   ratio 33.6 is the physical neutrino shear** — not an
   artefact of the fitting procedure.

3. **The R19 geometric formula α(ε, s) characterises the
   impedance mismatch between any material sheet and
   spacetime S** — not just the electromagnetic coupling of
   charged sheets.

### Then:

The neutrino sheet has a **different coupling constant**
than the charged sheets:

| Sheet | ε | s | α(ε, s) | 1/α |
|-------|---|---|---------|-----|
| Ma_e | 0.65 | 0.09594 | 0.007297 | 137.0 |
| Ma_p | 0.55 | 0.11101 | 0.007297 | 137.0 |
| **Ma_ν** | **5.0** | **0.021995** | **0.019184** | **52.13** |

The neutrino's geometric coupling α_ν ≈ 1/52 is **2.63×
stronger** than the electromagnetic α ≈ 1/137.

For reference: if the neutrino sheet were to reproduce
α = 1/137, it would need s_ν ≈ 0.01357.  The oscillation
data force the shear 1.62× above this value.

### Precision and significant figures

The shear s_ν = 3/(4R + 2) is mathematically exact for
any R.  The physical precision of α_ν is limited entirely
by the experimental oscillation data:

| Input | Value | Uncertainty |
|-------|-------|-------------|
| Δm²₂₁ | 7.53 × 10⁻⁵ eV² | ±2.4% |
| Δm²₃₁ | 2.530 × 10⁻³ eV² | ±1.3% |
| R = Δm²₃₁/Δm²₂₁ | 33.60 | ±2.7% |
| s_ν = 3/(4R + 2) | 0.021995 | ±2.7% |
| α_ν = α(5, s_ν) | 0.01918 | ±5.4% |
| 1/α_ν | **52.1 ± 2.8** | (range 49–55) |

Since α_ν ∝ s² for small s and s ∝ 1/R, the fractional
uncertainty doubles: δα_ν/α_ν ≈ 2 × δR/R.  This gives
roughly **1.3 significant figures** — enough to say "52"
but not to distinguish 52.0 from 52.1.

Future oscillation experiments (JUNO, DUNE, Hyper-K) will
tighten R to ~±1%, yielding 1/α_ν to ±2% (~±1 unit) —
enough to test whether it lands on a clean number.

**Notable near-miss:** 4R + 2 = 136.40, which is 0.47%
below 1/α = 137.04.  If they were equal, s_ν would be
exactly 3α.  Within current error bars, but probably
coincidental.

**Interesting candidate:** The repeating decimal
19/990 = 0.019191919... falls 0.04% from the central
value of α_ν and well within the ±5.4% uncertainty
window.  No derivation of 19 or 990 from the neutrino
sheet parameters is known; noted here in case a
connection surfaces later.

## 4. Constraint vs knob

On the charged sheets, the shear is *derived* from α —
the geometry has no choice.  Both sheets independently
converge on α = 1/137.  This looks like a mechanical
constraint: the coupling to spacetime S forces a
specific shear for each geometry.

On the neutrino sheet, the shear is set by *different*
physics entirely (the oscillation mass ratio), and the
resulting "α" is 1/52, not 1/137.  This opens a
fundamental question:

**Is the coupling constant a constraint or a parameter?**

- **Constraint (mechanical):** Each sheet's shear is
  forced by its boundary conditions.  The charged sheets
  happen to share α = 1/137 because they couple to the
  same EM field.  The neutrino couples differently
  (weakly, gravitationally) and its geometry produces a
  different constant.  No freedom — just different
  physics on different sheets.

- **Parameter (designer's knob):** Nothing in the
  geometry *forces* the shear.  Each sheet has an
  independent tuning parameter.  On Ma_e and Ma_p,
  the knob is turned to produce α = 1/137.  On Ma_ν,
  it is turned to produce the oscillation ratio.  The
  values are inputs, not outputs.

The current model cannot distinguish these.  Deriving
α from first principles (the unsolved problem of
Q18/Q29/Q77) would resolve the question.  If α is
derivable, then α_ν ≈ 1/52 becomes a **prediction** —
the neutrino's coupling to S, determined by the same
principle that sets 1/137 on the charged sheets.  If α
is a free parameter, then the values of the knobs become
the central mystery.

## 5. What α_ν might represent

On charged sheets, α(ε, s) = 1/137 measures how much
of the internal standing-wave energy "leaks" into spacetime
S as an observable electromagnetic field (Q77).  On the
neutrino sheet, the same geometric formula measures the
same kind of energy leakage — but the neutrino carries no
electric charge, so the leakage channel is not
electromagnetic.

Possible interpretations:

**A. Weak coupling geometry.**  The neutrino interacts
via the weak force.  If α_ν characterises the geometric
strength of the neutrino–S coupling, the weak interaction
might inherit its strength partly from α_ν rather than
(or in addition to) from the Fermi constant G_F.  For
comparison:

| Constant | Value | 1/value |
|----------|-------|---------|
| α_em | 0.00730 | 137.0 |
| α_ν (this result) | 0.01919 | 52.1 |
| sin²θ_W (Weinberg angle) | 0.2312 | 4.3 |
| α_W = α_em/sin²θ_W | 0.03156 | 31.7 |

α_ν does not match any known weak-sector constant cleanly.
It sits between α_em and α_W — roughly 61% of the weak
coupling.

**B. Gravitational or topological coupling.**  The
neutrino's coupling to S could be gravitational (all
massive particles gravitate) or topological (the torus
knot interacts with the embedding space regardless of
charge).  α_ν would then measure this non-EM channel.

**C. No physical meaning on the neutral sheet.**  The R19
formula was derived from the radiation impedance of a
charged mode.  On an uncharged sheet, the formula may
compute a geometric quantity that has no direct physical
interpretation — a coincidence of form rather than
substance.

## 6. What this observation constrains

Even if interpretation C is correct, the numerical
result constrains the model:

- **Shear is not universal.**  The three sheets do not
  share a single shear value.  The charged sheets share
  a common *output* (α = 1/137) at different shears; the
  neutrino sheet has a shear set by entirely different
  physics (mass ratios), landing at a different output.

- **The neutrino sheet's shear is larger than "electromagnetic
  equilibrium."**  If s_ν were free, α = 1/137 would select
  s ≈ 0.01357.  The oscillation data push s_ν to 0.022 —
  62% above this.  The neutrino sheet is "over-sheared"
  relative to the electromagnetic standard.

- **Neutrino neutrality is not from zero shear.**  Q102
  considers two mechanisms for neutrino neutrality: (a)
  sheet too large for the lattice to detect winding, or
  (b) zero or near-zero shear.  The fact that s_ν = 0.022
  is comparable in magnitude to s_e = 0.096 and s_p = 0.111
  strongly disfavors mechanism (b).  The neutrino sheet IS
  sheared; it simply doesn't couple electromagnetically for
  some other reason (likely related to sheet size, per Q102
  mechanism (a)).

## 7. Open questions

1. Does the R19 formula have a valid physical interpretation
   on an uncharged sheet, or is it purely geometric?

2. Is there a relationship between α_ν ≈ 1/52 and any
   measured weak-sector observable?

3. If all three sheets are sheared but only two produce
   electromagnetic coupling, what distinguishes the charged
   sheets from the neutral one at the level of the
   impedance formula?

4. Could α_ν play a role in cross-sheet coupling?  The
   cross-shear σ_ep characterises how the electron and proton
   sheets influence each other's metric.  If each sheet's
   self-coupling (α) is different, the cross-coupling
   strength might depend on the geometric mean or product
   of the two sheets' α values.

5. As oscillation data improve (JUNO target: Δm²₂₁ to
   ~0.5%, Δm²₃₁ to ~0.3%), 1/α_ν will be determined to
   ±1 unit.  Does it converge on a clean value — integer,
   simple fraction, or expression involving α, π, or
   mode quantum numbers?

---

*Connects to: Q77 (α as impedance), Q18 (deriving α),
Q102 (neutrino neutrality — mechanism (b) now disfavored),
R49 F26–F28 (ground-floor neutrino modes), R26 (Assignment A
and 33.6 ratio)*
