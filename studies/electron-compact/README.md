# Electron from Compact Dimensions  *(concluded)*

Assemble all established results into a single framework and
verify: a photon of specific energy, on a specific geodesic, in
a periodic geometry, produces an electron with all measured
properties. Identify what inputs are required and whether any
parameters are free.

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

## Result

The initial hypothesis was that r = L_θ/L_φ would be a free
parameter. This was wrong: since a = L_θ/(2π) and R = L_φ/(2π),
the charge condition a/R = 1/√(πα) directly fixes r = 1/√(πα).
The mass constraint then fixes the absolute scale.

**The electron has zero free continuous parameters.** Given
the (1,2) topology, photon energy E = m_e c², and α ≈ 1/137,
everything is determined:

    r = 1/√(πα) ≈ 6.60
    L_φ = λ_C / √(4 + 1/(πα)) ≈ 3.52 × 10⁻¹³ m
    L_θ = r L_φ ≈ 2.32 × 10⁻¹² m
    R = L_φ/(2π) ≈ 5.60 × 10⁻¹⁴ m
    a = L_θ/(2π) ≈ 3.70 × 10⁻¹³ m

The photon resonates at the Compton frequency f = m_e c²/h.

See [`findings.md`](findings.md) for full derivation and
[`scripts/verify.py`](scripts/verify.py) for numerical
verification.

## What this does NOT address

- Why α has the value it does
- Whether other particles (muon, quarks) fit this framework
- The guided-wave field profile (R6)
- The spindle torus self-intersection (a/R ≈ 6.6 > 1)

## References

- S2 (charge geometry): [`toroid-geometry/findings.md`](../toroid-geometry/findings.md)
- S3 (knot classification): [`knot-zoo/findings.md`](../knot-zoo/findings.md)
- R1 (KK comparison): [`kk-charge/findings.md`](../kk-charge/findings.md)
- WvM paper: [`ref/WvM.pdf`](../../ref/WvM.pdf)
- WvM summary: [`ref/WvM-summary.md`](../../ref/WvM-summary.md)
