# Electron from Compact Dimensions  *(draft)*

Assemble all established results into a single framework and
verify: a photon of specific energy, on a specific geodesic, in
a periodic geometry, produces an electron with all measured
properties. Identify what inputs are required and what is free.

## Motivation

If the universe is built from geometry — dimensions and how they
relate to each other — then particles should emerge from energy
on geodesics in that geometry. The electron is the simplest test
case. Prior studies established each property separately (spin
from S3, charge from S2, mass from WvM, g-factor from WvM). This
study checks them all simultaneously and asks: what is the
minimal specification that produces an electron?

## What we know

| Property | Value | How it arises | Source |
|----------|-------|---------------|--------|
| Spin ½ | L = ℏ/2 | (1,2) topology: double loop | WvM, S3 |
| Charge | q = e | a/R = 1/√(πα): field extent geometry | S2 |
| Mass | m_e | Path length = λ_C: photon energy | WvM |
| g-factor | g ≈ 2(1 + α/(2π)) | External field energy fraction | WvM |
| Only (1,2) has charge | All other knots cancel | Symmetry | S3 |
| KK gravity not involved | q_KK ~ 10⁻²² e at this scale | Scale separation | R1 |

## The recipe (hypothesis)

**Inputs:**
- A flat torus T² with circumferences L_φ, L_θ
- A (1,2) geodesic (topology choice)
- A photon of energy E = m_e c²

**Outputs (to verify):**
- Mass: m = E/c² = m_e (by construction)
- Spin: ½ (from double winding — any T² with a (1,2) path)
- Charge: e (from field extent a/R = 1/√(πα))
- g-factor: ≈ 2.0023 (from external field fraction α/(2π))

## Expected result

The system is under-determined. Specifically:

- Path length constraint: √(4L_φ² + L_θ²) = λ_C — one equation
  relating L_φ and L_θ, parameterized by r = L_θ/L_φ.
- Spin: topological, independent of r.
- Charge: fixes a/R = 1/√(πα), where R = L_φ/(2π). This
  determines a in terms of r, but does not constrain r itself.
- g-factor: depends on α = e²/(4πε₀ℏc), not on the compact
  geometry. Independent of r.

**Prediction: r is free.** The electron works on any T² whose
(1,2) geodesic has path length λ_C. The compact dimensions are a
property of the universe, not of the electron.

The study should confirm or refute this prediction.

## Approach

### Part A: Algebra (findings.md)

1. Write all four property formulas explicitly as functions of
   (L_φ, L_θ, a, E) and the (1,2) winding numbers.
2. Substitute constraints (path length, charge, g-factor).
3. Count free parameters. Confirm r is free (or discover it isn't).
4. State the result: the minimal specification for an electron.

### Part B: Numerical verification (scripts/)

A Python script that:
- Takes r as input (or sweeps a range)
- Computes L_φ(r), L_θ(r), R(r), a(r)
- Evaluates all four properties and compares to experiment
- Prints a table showing everything works (or doesn't) for each r
- Produces the "recipe card" — the explicit inputs and outputs

## What success looks like

A verified statement: "A photon of energy m_e c² on a (1,2)
geodesic in any T² with path length λ_C produces a particle with
q = e, s = ½, g ≈ 2.0023. The aspect ratio r = L_θ/L_φ is a
free parameter — a property of the universe, not the electron."

Plus: a clear list of what would constrain r (other particles,
field profile calculations, self-consistency conditions) pointing
to future work.

## What this does NOT address

- Why α has the value it does (S2 demands a/R = 1/√(πα) but
  doesn't derive it)
- What determines r (deferred to future studies)
- Whether other particles (muon, quarks) live on the same T²
- The guided-wave field profile that should derive a/R from first
  principles (deferred to R6)

## References

- S2 (charge geometry): [`toroid-geometry/findings.md`](../toroid-geometry/findings.md)
- S3 (knot classification): [`knot-zoo/findings.md`](../knot-zoo/findings.md)
- R1 (KK comparison): [`kk-charge/findings.md`](../kk-charge/findings.md)
- WvM paper: [`ref/WvM.pdf`](../../ref/WvM.pdf)
- WvM summary: [`ref/WvM-summary.md`](../../ref/WvM-summary.md)
