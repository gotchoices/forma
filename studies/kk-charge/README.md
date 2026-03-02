# KK Charge Comparison  *(draft)*

Does WvM's charge derivation relate to the Kaluza-Klein charge
mechanism? If so, how? If not, what framework should we use?

## Why this is first

Every study after this depends on the answer. It determines
whether we can use established KK mathematics as our framework,
or whether we need something different.

## The sharpened questions

Our preliminary analysis (see `theory.md` and discussions in
`ref/kaluza-klein.md`) revealed that this is not a simple yes/no
comparison. Three structural issues must be addressed:

**1. Gravitational vs electromagnetic coupling.** Standard KK
derives charge from 5D gravity — the factor √G appears in the
charge formula, giving a compact radius of ~10⁻³⁴ m (Planck
scale). WvM is purely electromagnetic, with structures at
~10⁻¹² m (Compton scale). These differ by 10²¹. The question is
whether a non-gravitational version of KK (electromagnetic fields
on a compact space, no gravity) gives a different charge formula
with a different natural scale.

**2. Two U(1) charges from T².** A 6D theory with T² compact
space gives U(1) × U(1) — two independent gauge fields. The
(1,2) geodesic winds in both compact directions, so it carries
two charges. How these combine into the single electric charge we
observe is non-trivial.

**3. Two different charge mechanisms.** KK: charge = quantized
momentum in the compact direction (exact, from Noether's theorem).
WvM: charge = electromagnetic field topology (approximate, from
average E-field in a cavity). These might be the same thing
viewed differently, or genuinely different physics.

## Approach

The study has two parts.

### Part A: Algebraic derivation (findings.md)

A step-by-step mathematical paper, written so each step can be
independently verified. Covers:

- F1. The standard KK charge formula (with √G) and what compact
  radius it implies for q = e.
- F2. The electromagnetic KK formula — what happens when we do
  KK without gravity (Maxwell on a compact space). Does the charge
  formula change?
- F3. Direct comparison: WvM charge formula vs KK charge formula.
  Express both in terms of the same variables. Are they
  structurally the same, proportional, or unrelated?
- F4. The T² extension: how two compact momenta combine for a
  (1,2) geodesic. What is the effective single charge?
- F5. The α connection: do a/R = 1/√(πα) and the KK compact
  radius unify?

### Part B: Numerical verification (scripts/)

A Python script that:
- Evaluates both charge formulas with physical constants
- Computes implied compact dimensions for each formula
- Explores the T² parameter space (L₁, L₂) for a (1,2) path
  of length λ_C, checking which combinations give q = e
- Produces a clear numerical summary for verification

## Propositions (from theory.md)

- **P1.** WvM and KK charge are algebraically related
- **P2.** T² compact momentum gives q ≈ e for the (1,2) geodesic
- **P3.** Two U(1) charges combine into a single effective charge
- **P4.** The α appearances unify

## Expected outcomes

The outcome is likely not "WvM = KK exactly" (the gravitational
coupling makes this improbable). More likely outcomes:

- **WvM ≈ electromagnetic KK:** same mechanism, different from
  standard gravitational KK, at a much larger scale.
- **WvM is structurally different:** charge from field topology is
  a genuinely different mechanism from charge as compact momentum.
  The compact-dimension framework is useful for confinement and
  spin but the charge derivation is WvM's own.
- **Hybrid:** the T² topology provides spin and confinement; the
  charge mechanism is electromagnetic (WvM-like) rather than
  gravitational (KK-like); the two are complementary.

Any of these outcomes tells us what framework to use for R2
(solving for electron properties).

## References

- WvM paper §3 (charge derivation): `ref/WvM.pdf`
- KK primer: `ref/kaluza-klein.md`
- Maxwell primer: `ref/maxwell-primer.md`
- A7 (compact dimensions): `answers/A7-flat-compact-dimensions.md`
- Propositions and framework: `theory.md`
