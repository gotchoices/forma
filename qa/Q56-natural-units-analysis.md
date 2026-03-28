# Q56. Natural-units analysis of the photon-knot model

**Status:** open — variational approach not yet attempted
**Source:** user question
**Connects to:** Q49 (natural units parallel), Q29 (variational α),
R15 F5 (α = exp(−4σ²))

---

## Setup

In natural units (ℏ = c = 1), all physical quantities reduce
to powers of length and energy (or equivalently mass).  In the
photon-knot model, these correspond to:
- **Length** = material geometry (R, a, σ)
- **Energy** = confined photon (m_ec²)

The model's dimensionless parameters:
- r = a/R (aspect ratio) — still free, plausibly 1/2 from Q52
- σ (wavepacket width in radians) — the unknown that determines α
- α = exp(−4σ²) — the fine-structure constant

In natural units:
- R ≈ 0.485/m_e (about half the reduced Compton wavelength)
- a ≈ 0.243/m_e (for r = 1/2)
- e²/(4π) = α ≈ 1/137 (the coupling constant)
- All torus dimensions are O(1/m_e) — the Compton scale

## The energy budget (in units of m_e)

- Total: m_ec² = 1 (the photon)
- Kinetic localization: ~exp(−4σ²) ≈ α (from σ ≈ 1.1)
- Coulomb self-energy: α × 1 = α (from R7)
- Magnetic moment: g ≈ 2(1 + α/(2π))

## The pattern

Every deviation from the "natural" value appears with
coefficient α.  The kinetic localization cost is α × m_ec².
The Coulomb energy is α × m_ec².  The g−2 correction is
α/(2π).  This suggests α is the single parameter controlling
ALL perturbative effects in the model.

## The question

Does this pattern constrain σ?  If σ is determined by minimizing
the total energy including all O(α) corrections, the equilibrium
might fix α self-consistently.  This would be a variational
approach to the α problem (see Q29).
