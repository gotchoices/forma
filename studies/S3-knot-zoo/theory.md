# Theory: Torus Knot Particle Zoo

## 1. Torus Knots and the WvM Framework

A (p,q) torus knot winds p times around the tube cross-section and
q times around the major axis before closing. The path length on a
torus with major radius R and tube radius a is approximately:

    L = √((2πqR)² + (2πpa)²)

For the knot to represent a single photon of wavelength λ, we require
L = λ (or L = nλ for standing-wave resonances).

### Constraints for a valid knot

- p and q must be coprime (otherwise the path doesn't close as a
  single knot — it becomes multiple linked loops).
- The path must be traversed an integer number of times to return to
  the starting orientation. This determines the spin.

## 2. Spin from Topology

In the WvM model, the electron has spin ½ because the photon must
traverse the full path **twice** to return to its starting field
orientation (the E-field picks up a phase of π on each traversal
due to the Möbius-like topology).

For a general (p,q) torus knot, the spin depends on how the
polarization state transforms after one complete circuit:

- If the E-field returns to its starting orientation after 1 circuit:
  **integer spin** (boson).
- If it requires 2 circuits: **half-integer spin** (fermion).

The key parameter is p (windings around the tube):

- **p = 1** (odd): The path traverses the tube once, accumulating a
  π phase twist. After 1 circuit the E-field is inverted → needs 2
  circuits → **spin ½**.
- **p = 2** (even): The path traverses the tube twice, accumulating
  a 2π twist. After 1 circuit the E-field returns → **spin 1** (or 0).
- **p = 3** (odd): Similar to p = 1 — needs 2 circuits → **spin ½**
  (but with higher winding energy).

More generally:
- **Odd p → fermion** (spin ½, 3/2, ...)
- **Even p → boson** (spin 0, 1, 2, ...)

The exact spin quantum number may also depend on q:

    S = p / (2q)  ???

For (p=1, q=2): S = 1/4? No — WvM gets ½. The spin derivation in
WvM comes from angular momentum:

    L = R × (hν/c) = R × (h/(λc)) × c = Rh/λ

For the (1,2) path (WvM electron), q = 2 major loops, so the angular
momentum per major loop is L/q = Rh/(qλ). With R = λ/(4π):

    L_per_loop = h/(4πq)

Total angular momentum:

    L_total = L_per_loop = ℏ/(2q) × q = ℏ/2   [need to verify]

**This section needs careful rederivation for general (p,q).** The
computational study will verify by explicit calculation rather than
relying on this tentative analysis.

---

## 3. Charge from Geometry

From study 2 (S2-toroid-geometry), the WvM charge derivation gives:

    q_charge = (1/2π) √(3ε₀ℏc) ≈ 0.91e

This depends on the photon energy (hc/λ) and the confinement volume,
not directly on p or q. For a (p,q) knot:

- The path length is L ≈ 2π√((qR)² + (pa)²) instead of 4πR.
- The photon energy is hc/λ where λ = L.
- The confinement volume may differ (the field wraps differently).

Whether the charge changes with (p,q) — and whether fractional
charges can emerge — is a key question for this study.

---

## 4. Mass from Winding

In the WvM model, the electron mass is an input (m = hν/c² = h/(λc)).
But if different knots correspond to different particles, their masses
might relate to their winding numbers:

- More complex knots → longer path length → higher frequency → higher mass?
- Or: same path length, different R → different confinement → different mass?

The mass ratios of the charged leptons are:

    m_μ/m_e ≈ 206.8
    m_τ/m_e ≈ 3477

Can any (p,q) assignment reproduce these ratios?

---

## 5. Propositions to Test

### P1. Spin Classification

Enumerate (p,q) torus knots for small p,q. For each, determine the
spin quantum number from the topology. Classify which give fermions
(half-integer) and which give bosons (integer).

### P2. Charge Variation

For each (p,q), compute the predicted charge using the WvM derivation
(appropriately generalized). Do any knots give fractional charge?

### P3. Mass Ratios

If different knots share the same torus geometry (R, a) but have
different path lengths, compute the mass ratios. Compare to the
known lepton and hadron mass spectrum.

### P4. Particle Identification

Attempt to match (p,q) knots to known particles based on their
predicted spin, charge, and mass. How far does the correspondence
extend?

---

## 6. Scope

### In scope

- Torus knot enumeration and classification
- Spin, charge, and mass predictions for each (p,q)
- Comparison to known particle spectrum
- Fractional charge and baryon number from topology

### Out of scope

- Confinement mechanism
- Gravitational effects
- Detailed field calculations (see S2-toroid-geometry open questions)
- Strong/weak force interactions

---

## 7. Outcome

In the Frenet frame model, only the (1,2) knot produces electric
charge (F3). This is a computational result, not a general proof —
it assumes a specific polarization transport rule.

The WvM charge formula algebraically admits fractional charges
via different a/R values (F4), which is consistent with the
hypothesis that quarks might be (1,2) knots on compact dimensions
with different geometry. The compact dimension reframing (F2) is
an untested hypothesis that, if correct, would resolve the
confinement and mass problems simultaneously.

See findings.md for the full distinction between demonstrated
results, algebraic observations, and untested hypotheses.
