# R15. Forward Charge Calculation  *(open)*

Compute the electron's apparent charge from first principles —
energy and topology only — without using e as an input.  If
this gives Q such that Q²/(4πε₀ℏc) ≈ 1/137, we have derived α.

## Motivation: how R7 led to R8, and why R8 is a dead end

### The R7 result

R7 placed charge Q = e on a (1,2) geodesic at Compton scale and
computed the 3D Coulomb self-energy.  The result:

    U_Coulomb ≈ α × m_e c²     (all aspect ratios)

The target was U = m_e c²/2.  R7 found only ~1.5% of this —
a factor of ~1/α too small — and called it a failure.

But R7 also proved analytically why (F3):

    U_Coulomb / (m_e c²) = e²/(4πε₀ ℏc) = α

This is the *definition* of α.  For any charge e at any
Compton-scale distance, the Coulomb energy is α × m_e c².
The "shortfall" is not a failure — it is dimensional analysis.

### The R8 response

R8 demanded U_Coulomb = m_e c²/2 (all E-field energy in the
Coulomb pattern).  This required shrinking the torus from
Compton scale (~10⁻¹³ m) to the classical electron radius
r_e (~3 × 10⁻¹⁵ m).  The smaller torus needed q ≈ 137
major windings (with p = 68 minor windings) to fit path
length λ_C.  R8 produced several valuable results:

- Exact spin ½ from sheared T² with (68,137) winding
- R/r_e = 0.989 — stable across resolutions
- g = 2 from photon spin-1 / electron spin-½ topology
- δ ≈ αR — shear of electromagnetic origin (approximate)

### R13 kills multi-winding charge

R13 Track 3 showed that multi-winding (p = 68) *breaks* the
WvM charge mechanism.  WvM requires p = 1: one tube winding
per wavelength so that the circular polarization rotation
matches the geometric frame rotation, keeping E always normal
to the torus surface.  With p = 68, E oscillates 67 times
relative to the surface normal per circuit, integrating to
zero.  The monopole charge Q = 0 — exactly, analytically.

### The wrong assumption

The assumption that drove R7 → R8 was: **all the photon's
E-field energy should appear as far-field Coulomb energy.**
This led to the target U = m_e c²/2.

But in a model where a photon is confined to a compact space,
most of its energy naturally stays in near-field modes
localized near the compact boundary.  Only a fraction couples
to the 3D far field.  R7's Possibility A identified this
explicitly (F4):

| Component | Energy | Fraction |
|-----------|--------|----------|
| Near field (compact surface) | ~(1−2α) × m_e c²/2 | ~98.5% |
| Far field (Coulomb) | ~α × m_e c² | ~1.5% |

The fraction that leaks IS α — the electromagnetic coupling
constant.  R7 found this relationship and noted (F6) that
"α appears naturally" and that the question is whether the
model can *predict* α or must take it as input.

### The revived model

With multi-winding killed by R13, the surviving model is:

- **(1,2) torus knot at Compton scale**
- Path length = λ_C → mass = m_e (by construction)
- p = 1 → WvM commensurability → E always outward → charge
- 1:2 topology → spin ½
- Photon spin-1 / electron spin-½ → g = 2
- U_Coulomb = α × m_e c² → not a failure, a consistency check

Everything works EXCEPT: we don't yet know the *value* of the
apparent charge without putting it in by hand.

## Strategy: the forward calculation

R7 ran *backwards*: input Q = e, compute U, compare to target.
The result (U = α × m_e c²) was circular — α was already
embedded in the input e.

This study runs *forwards*: input energy = m_e c² and topology
= (1,2), compute the far-field Coulomb flux, read off Q.

R7's README (§"Looking ahead") identified this as the
non-circular version but noted that "nothing in the current
model selects a specific r" — so it was never attempted.
We now have a reason to attempt it: the (1,2) model at Compton
scale is the only surviving candidate after R13.

### Procedure

1. **Geometry.**  Fix a (1,2) torus knot at Compton scale.
   The path constraint ℓ = λ_C determines R(r) and a(r)
   for each aspect ratio r = a/R.  (Same as R7.)

2. **Field source.**  The photon is circularly polarized on
   the (1,2) geodesic.  WvM commensurability (p = 1): as
   the surface normal rotates by 2π, the polarization rotates
   by 2π in the opposite sense.  Result: E is always normal to
   the torus surface with amplitude E₀ at the photon's location.

3. **Energy constraint.**  Total electromagnetic energy = m_e c²
   (this is the photon's energy, hence the electron's mass).
   By equipartition, E-field energy = m_e c²/2.

       ½ε₀ ∫ E² dV = m_e c²/2

   This determines E₀ as a function of r.  The integral is
   the same one R7 computed — just inverted.

4. **Apparent charge.**  With E₀ determined, compute the total
   electric flux through a large sphere enclosing the torus:

       Q = ε₀ ∮ E · n̂ dA

   By Gauss's law, this equals the total enclosed charge.
   The flux integral at large distance depends on how the
   near-field E (always-outward along the torus surface)
   transitions to the far-field 1/r² pattern.

5. **Result.**

       α = Q²/(4πε₀ ℏc)

   If this gives ≈ 1/137, we have derived the fine-structure
   constant from energy, topology, and geometry alone.

### What's hard

Step 4 is the crux.  The near-field is localized on the torus
surface (E always radially outward from the (1,2) knot path).
The far-field is a 1/r² Coulomb pattern.  The transition
between these two regimes is the boundary-value problem:
how does an EM wave confined to a compact T² couple to 3D?

In waveguide language: the compact space is the guide, and the
Coulomb field is evanescent leakage into 3D.  The leakage
fraction is α.  Computing it requires solving Maxwell's
equations with the compact wave as a source term in 3D.

R7's existing scripts compute the 3D field of a line source
along the (1,2) geodesic — this is exactly the near-field
configuration.  The far-field flux is obtained by integrating
E · n̂ over a distant surface.  So the infrastructure exists;
what changes is the interpretation (E₀ from energy, not
from Q = e).

### Comparison with R7

| | R7 (backward) | R15 (forward) |
|---|--------------|---------------|
| **Input** | Q = e | U = m_e c² |
| **Compute** | U from E-field | Q from E-field |
| **Output** | U = α × m_e c² | Q = ? → α = ? |
| **Circular?** | Yes (e → α) | No |
| **Target** | U = m_e c²/2 | α ≈ 1/137 |

## Tracks

### Track 1. Invert R7 — line source forward calculation

Use R7's line-source model (charge distributed along the
(1,2) geodesic, E always outward).  Instead of fixing Q = e
and computing U:

1. Fix U_E = m_e c²/2
2. Invert: E₀(r) = √(m_e c² / (ε₀ × f(r)))
   where f(r) is R7's geometry-dependent energy integral
3. Compute the far-field flux: Q(r) = ε₀ ∮ E · n̂ dA
4. Plot α(r) = Q²/(4πε₀ ℏc) vs. r

If the forward calculation gives α ≈ 1/137 for any r, or
if it's constant across r (as R7's backward result suggests),
that is a strong signal.

**Expected difficulty:** Low — this reuses R7's scripts and
infrastructure.  The main work is computing the far-field
flux from the line-source E-field (which R7 already computes
in 3D) and inverting the energy normalization.

### Track 2. Gauss's law shortcut

For a static charge distribution, Gauss's law guarantees that
the flux through ANY closed surface equals Q/ε₀.  If R7's
line source produces an E-field that is everywhere outward
(WvM mechanism), then:

    Q = ε₀ ∮ E · n̂ dA = ε₀ × (average E_r) × (4πd²)

at any distance d > R.  This means Q is determined by the
field at any distance — no need to go to infinity.

Check: does Q from Gauss's law at distance d = 10R (well
outside the torus) match Q from the energy inversion?  If yes,
the near-to-far transition is clean.  If no, there's a
problem with the model (e.g., the "always outward" assumption
breaks down at intermediate distances).

**Expected difficulty:** Low — a diagnostic within Track 1.

### Track 3. Sensitivity to aspect ratio

R7 found that U_Coulomb/U_target ≈ 0.015 is nearly constant
across r ∈ [0.5, 10].  In the forward direction, this means
Q(r) should also be nearly constant — the apparent charge
is determined by the overall scale (λ_C), not the shape.

If confirmed, this is significant: it means α does not
depend on r, removing the "free parameter" concern from R7.
The (1,2) topology and the Compton path length alone would
determine α.

**Expected difficulty:** Trivial if Track 1 works — just
plot α(r) over the sweep.

### Track 4. Analytical prediction

The near-constancy of U_Coulomb/m_e c² across r (R7 F2)
suggests an analytical formula might exist.  The scaling is:

    U_Coulomb ~ Q² / (4πε₀ R)
    R ~ λ_C / (2π) × 1/√(4 + r²)
    U_total = m_e c²

Combining (forward direction):

    Q² = U_Coulomb × 4πε₀ R
    α = Q² / (4πε₀ ℏc)

If U_Coulomb/U_total = constant ≡ κ (a pure number from the
geometry of the coupling), then:

    α = κ × m_e c² × 4πε₀ R / (4πε₀ ℏc) = κ × R/(ℏ/m_e c) = κ

since R is of order ℏ/(m_e c).  So α ≈ κ — the coupling
fraction IS the fine-structure constant.

The task: derive κ analytically from the field equations of a
(1,2) line source on a torus.  This would be a closed-form
expression for α.

**Expected difficulty:** Medium-high.  The geometry-dependent
integral f(r) has no known closed form, but an asymptotic
expansion or a clever change of variables might yield one.

## Connections

- **R7** — provides the backward calculation, scripts, and the
  identification of Possibility A (near-field/far-field split).
- **R8** — provides the multi-winding model that this study
  argues was a detour.  R8's spin and g-factor results (Tracks
  2-3) carry over to the (1,2) model unchanged.
- **R13** — killed multi-winding charge, reviving (1,2) at
  Compton scale.
- **Q34** — this study pursues Path 7 of Q34.
- **Q18** — the master question: can α be derived from geometry?
- **Q48** — why does E (not B) point outward?  If answered,
  this constrains the WvM mechanism used in this study.

## References

- R7 findings: [`torus-capacitance/findings.md`](../torus-capacitance/findings.md)
- R7 README (forward calculation): [`torus-capacitance/README.md`](../torus-capacitance/README.md)
- R8 findings: [`multi-winding/findings.md`](../multi-winding/findings.md)
- R13 Track 3: [`kk-charge-t3/findings.md`](../kk-charge-t3/findings.md) (F18–F23)
- Q34 (charge mechanism): [`../../qa/INBOX.md`](../../qa/INBOX.md) (Path 7)
- Charge-from-energy primer: [`../../primers/charge-from-energy.md`](../../primers/charge-from-energy.md)
