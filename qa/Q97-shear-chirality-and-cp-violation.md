# Q97: Does shear chirality bias matter over antimatter?

**Status:** Open — conceptual, connects to baryogenesis
**Related:**
  Q32 (energy and geometry as fundamentals — baryogenesis argument),
  Q58 (shear breaks φ-symmetry, produces charge),
  R19 (shear-charge formula derived and validated),
  R14 (universal geometry, baryogenesis without antimatter),
  R42 (dark matter — charge cancellation symmetry),
  Q94 (Compton window — dark mode annihilation suppression)

---

## The question

The material sheet has a definite shear direction (s > 0).
This is a geometric chirality — a handedness.  Does it
create a preference for matter over antimatter?


## Glossary: C, P, T, and CPT

Three operations you can perform on a particle (in your head):

- **C (charge conjugation)** — flip the electric charge.
  Electron (−1) → positron (+1).  Everything else stays the same.

- **P (parity)** — look at the particle in a mirror.
  Left-handed → right-handed.  Like swapping your left and
  right gloves.

- **T (time reversal)** — run the movie backwards.
  A particle flying left becomes a particle flying right
  (with spin reversed).

**CPT** means doing all three at once: flip the charge, mirror
the spatial configuration, AND reverse the direction of time.
The result is the true antiparticle.

Why it matters: the CPT theorem says that every quantum field
theory must be invariant under CPT — meaning the antiparticle
always has exactly the same mass and lifetime as the particle.
You can violate C alone (the weak force does), violate P alone
(the weak force does that too), even violate CP together — but
CPT as a package is sacred.

In MaSt terms: CPT corresponds to flipping ALL winding numbers
(n₁, n₂) → (−n₁, −n₂).  Because the energy depends on
q_eff² = (n₂ − s·n₁)², and flipping both signs gives
(−n₂ + s·n₁)² = (n₂ − s·n₁)², the energy is unchanged.
CPT is exact by construction.


## 1. What shear does to the mode spectrum

On a sheared electron sheet, the effective winding of mode
(n₁, n₂) is q_eff = n₂ − s·n₁.

The electron (1, 2) has q_eff = 2 − s ≈ 1.84.

Three related modes:

| Mode | q_eff | Charge | E² ∝ | Relation |
|------|-------|--------|------|----------|
| (1, 2) | 2 − s | −1 (electron) | 1/a² + (2−s)²/R² | particle |
| (−1, −2) | −2 + s = −(2−s) | +1 (positron) | 1/a² + (2−s)²/R² | CPT conjugate |
| (−1, 2) | 2 + s | +1 | 1/a² + (2+s)²/R² | charge conjugate |
| (1, −2) | −2 − s = −(2+s) | −1 | 1/a² + (2+s)²/R² | CPT of charge conj. |

Key observations:

1. **CPT is preserved.**  The electron (1,2) and positron
   (−1,−2) have identical energy.  For every mode at energy E
   with charge Q, the mode with all signs flipped has energy E
   and charge −Q.  No thermodynamic bias.

2. **Charge conjugation is broken.**  The charge conjugate
   (−1, 2) has energy ∝ (2+s)², which is HIGHER than (2−s)².
   Flipping only the charge (not the spin) changes the mass.

3. **The spectrum is CPT-symmetric but C-asymmetric.**
   This is exactly what the Standard Model also exhibits:
   CPT is an exact symmetry; C and P are violated individually.


## 2. No thermodynamic bias (in equilibrium)

Since CPT is exact, the Boltzmann weight exp(−E/kT) is
identical for every particle and its antiparticle.  In thermal
equilibrium at any temperature, the populations are exactly
equal.  Shear does not create a static matter excess.

This is consistent with R42 F1–F3: the Ma spectrum has exact
charge symmetry for particle-antiparticle pairs.


## 3. Kinetic bias (out of equilibrium)

Thermodynamic equality does not imply kinetic equality.
The RATES of topological transitions depend on the geometry
of the transition state, not just the endpoint energies.

On a chiral sheet (s ≠ 0), the topology of the path from
"free photons" to "wound mode" differs for left-wound vs
right-wound configurations.  Specifically:

- The transition 4γ → H (Q32) requires photons to wind into
  specific topological configurations on the sheet.
- The transition 4γ → H̄ requires the MIRROR configurations.
- On a chiral sheet, the mirror configuration is not
  geometrically equivalent — the transition amplitudes differ.

This is a kinetic CP violation: the rate of matter creation
differs from the rate of antimatter creation, even though
the equilibrium populations would be equal.


## 4. The Sakharov conditions

Baryogenesis requires three conditions (Sakharov, 1967).
MaSt provides all three from geometry:

| Condition | Standard Model source | MaSt source |
|-----------|----------------------|-------------|
| Baryon number violation | Sphaleron processes, GUT bosons | Q32: B and L are topological counts, not conserved charges.  Only total winding (electric charge) is conserved.  4γ → H is allowed. |
| C and CP violation | CKM matrix phase (a fitted parameter) | Shear chirality: the material sheet has a definite handedness s > 0.  This is a geometric property, not a coupling constant. |
| Departure from equilibrium | Electroweak phase transition | Standard cosmology: expanding, cooling universe.  Same as SM. |

The Standard Model struggles with condition 2: the CKM phase
provides too little CP violation for the observed asymmetry
(by ~10 orders of magnitude).  This is an open problem.

MaSt offers a different source: the chirality is a GEOMETRIC
property of the material sheet, not a perturbative coupling.
The asymmetry could be large — it's set by the shear angle,
not by a loop correction.


## 5. Why the sheet has a definite handedness

On an unsheared sheet (s = 0), charge is zero for all modes
(R19 F1: sin(2πs) vanishes).  The universe would have no
charged particles, no atoms, no chemistry.

The sheet MUST be sheared for the observed universe to exist.
But the physics of +s and −s are identical — a universe built
on −s would have the same particles, forces, and structures.
We would just swap the labels "matter" and "antimatter."
Neither direction is preferred; neither is special.

This is a spontaneous symmetry breaking: the shear angle
must be nonzero, but its sign is arbitrary.  Analogous to
the Higgs mechanism selecting a vacuum direction, but simpler
— a geometric parameter, not a field expectation value.

The situation is similar to other "free" parameters in MaSt.
The fine-structure constant α likely works within a range
of geometries (Q18, Q29); the shear magnitude s ≈ 0.16 is
constrained by requiring realistic charge values (R19); but
the shear SIGN is entirely unconstrained.  The universe
could have gone either way.  Once the choice was made
(presumably when the material sheet first formed), it froze
into the geometry and every subsequent particle inherited
the same convention.

This means the question "is our shear in the direction
that favors matter?" is circular.  The shear creates a
kinetic bias for one winding direction over the other
(§3).  Whichever direction wins, we call "matter."  The
word is a name for the winner, not a pre-existing category
that the shear either matches or doesn't.


## 6. Implications for dark matter

From Q94 and R42: dark modes can't annihilate efficiently
because they don't couple well to S (the Compton window
suppresses the radiation channel).

The shear chirality adds another layer: even for dark modes,
the C-asymmetry in transition rates means slightly more dark
"matter" than dark "antimatter" is produced during the
chiral epoch.  The dark matter gas is charge-neutral
(R42 F1–F3) but could carry a net "matter number" —
an excess of one winding direction over the other.

Whether this excess is observable depends on whether dark
mode self-interactions are sensitive to relative winding
direction.  This has not been computed.


## 7. What's computable

1. **Transition amplitude asymmetry.**  Compute the WKB
   amplitude for a topological winding transition (photon →
   wound mode) on a sheared vs unsheared sheet.  The ratio
   A(+winding)/A(−winding) on a sheet with shear s gives
   the CP asymmetry parameter.

2. **Comparison to CKM.**  The Standard Model's CP violation
   comes from the CKM phase δ ≈ 1.2 rad.  The MaSt prediction
   is that CP violation comes from the shear angle
   δ_lattice ≈ 9° (R19 F4).  These are different numbers
   measuring different things, but the magnitudes should be
   relatable.

3. **Baryon-to-photon ratio.**  The observed η ≈ 6 × 10⁻¹⁰
   (baryons per photon) must emerge from the combination of
   the shear-induced rate asymmetry and the Q32 condensation
   mechanism.  This is a quantitative prediction once the
   transition amplitudes are computed.

4. **Dark matter excess.**  Compute whether dark modes inherit
   the same winding-direction excess as visible modes, and
   whether this has observable consequences.


## 8. Summary

Shear does not create a thermodynamic bias (CPT is exact).
But it creates a geometric chirality that breaks C and CP,
providing the kinetic asymmetry needed for baryogenesis.
Combined with Q32's baryon number non-conservation and
standard cosmological non-equilibrium, all three Sakharov
conditions are met — from geometry alone, with no fitted
CP-violating parameters.

The matter-antimatter asymmetry, in this picture, is not a
puzzle to be solved — it is a consequence of the material
sheet having a definite shape.
