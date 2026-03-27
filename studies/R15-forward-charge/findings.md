# R15. Forward Charge Calculation — Findings

## Terminology

Throughout this document:

- **θ (theta):** angle around the tube (minor circle) of the
  torus.  One full loop around the tube = 2π radians.
- **φ (phi):** angle around the ring (major circle) of the
  torus.  One full loop around the ring = 2π radians.
- **R:** major radius — distance from the center of the
  torus to the center of the tube.
- **a:** minor radius — radius of the tube itself.
- **r = a/R:** aspect ratio of the torus.
- **(1,2) torus knot:** a path that winds once around the
  tube (p = 1) for every two times around the ring (q = 2).
  This is the WvM electron model.
- **Fourier mode number:** when we decompose a wave on the
  torus into components, each component oscillates a certain
  number of times around the ring.  That number is the
  "mode number in φ."  A mode-2 wave completes 2 full
  oscillations per circuit around the ring.
- **Monopole:** the net charge.  A positive charge surrounded
  by a negative charge can have zero monopole (they cancel).
  The monopole is what a distant observer measures as "the
  charge."
- **σ (sigma):** the angular width of the photon's wavepacket
  on the torus (in radians), specifically in the φ direction
  (around the ring).
- **Localized vs delocalized:** a "localized" wave is
  concentrated at one spot (like a particle); a "delocalized"
  wave is spread evenly around the ring (like a standing wave
  in a circular waveguide).


## Track 1: Forward calculation and localization

### F1. The forward calculation gives Q ≈ 8e, not e

R7 placed charge Q = e along the (1,2) geodesic at Compton
scale and computed the Coulomb self-energy: U ≈ α × m_e c².
This was ~100× less than the target U = m_e c²/2.

R15 inverts this: if the target energy is U = m_e c²/2 (half
the electron's mass-energy), what charge would produce it?

    Q_forward = e × √(1/(2α)) ≈ 8.3e

The model predicts a charge about 8× too large.  In terms
of the coupling constant:

    α_forward ≈ 0.4–0.7    (should be 1/137 ≈ 0.0073)

| r = a/R | Q_fwd / e | α_forward | α / α_forward |
|---------|-----------|-----------|----------------|
| 0.50 | 7.45 | 0.41 | 0.011 |
| 1.00 | 7.91 | 0.46 | 0.010 |
| 2.00 | 8.17 | 0.49 | 0.010 |
| 4.29 | 9.13 | 0.61 | 0.008 |


### F2. The coupling fraction κ = α

The ratio κ = α / α_forward measures what fraction of the
photon's total energy ends up in the far-field Coulomb
pattern (the 1/r² electric field that a distant observer
would measure).

    κ ≈ 0.007–0.013 ≈ α

This is R7's result (F3) stated differently: the
fine-structure constant IS the fraction of the photon's
energy that appears as Coulomb energy.  The forward
calculation confirms this but does not derive it.


### F3. Why a smooth wave on a torus has zero charge

This is the central finding.  Consider any wave pattern
on the torus surface of the form:

    σ(θ, φ) = f(θ) × cos(n × φ)

where n is the number of oscillations around the ring.
For our (1,2) electron, n = 2 (two oscillations per ring
circuit).

The total charge is the integral of σ over the torus surface:

    Q = ∫∫ σ(θ, φ) × (area element) dθ dφ

The area element on a torus is (R + a cos θ) × a.  Crucially,
it depends only on θ (where you are on the tube), not on φ
(where you are around the ring).  So the integral separates:

    Q = [∫ f(θ) × (R + a cos θ) × a dθ] × [∫ cos(n φ) dφ]

The second factor — the integral of cos(nφ) around a full
circle — is exactly zero for any n ≥ 1.  The positive and
negative half-cycles cancel perfectly.

**This is exact and inescapable.** No matter how we modify
the θ-dependent part (the tube profile), the ring integral
kills the charge.  A wave that oscillates even once around
the ring has zero net charge.

The deeper reason: the torus is rotationally symmetric
around its central axis.  Spinning the torus around the
z-axis is a symmetry — it doesn't change the shape.  This
symmetry forces the mode number n to be conserved.  A wave
with n = 2 on the surface produces a 3D field that also has
n = 2 angular dependence.  The net charge (the n = 0
component) is exactly zero — it can never be generated from
an n = 2 wave on a symmetric torus.


### F4. Charge requires localization

If the wave is NOT spread evenly around the ring, but
instead concentrated in a patch (like a pulse), the
situation changes.  A localized pulse contains many
different mode numbers, including n = 0 — the one that
produces net charge.

Think of it by analogy with sound:
- A pure tone (single frequency) spread around a ring:
  zero average pressure.
- A sharp click (localized pulse): positive average
  pressure at the click location.

The WvM model's "particle picture" — a photon at one
specific point on the torus, with E pointing outward at
that point — corresponds to the fully localized case (a
delta function).  This gives maximum charge.

The "wave picture" — a smooth cos(θ + 2φ) pattern spread
over the entire surface — is the fully delocalized case.
This gives exactly zero charge.

The real electron must be somewhere between these extremes:
a wavepacket of finite width.

| Field configuration | Charge |
|---------------------|--------|
| Perfectly localized (one point) | Maximum |
| Wavepacket of width σ | Intermediate |
| Smooth wave (spread everywhere) | Zero |


### F5. The localization formula: α = exp(−4σ²)

If the photon's wavepacket has a Gaussian (bell-curve)
shape in the φ direction with angular width σ (in radians),
the fraction of energy that produces charge can be computed
exactly.

The key is the Fourier transform of a Gaussian.  A Gaussian
in position space of width σ corresponds to a Gaussian in
frequency space of width 1/σ.  Our wavepacket is centered
at mode number n = 2.  The amplitude at n = 0 (the
charge-producing component) is:

    amplitude at n = 0 = exp(−2σ²)

This is just the value of a Gaussian centered at n = 2,
evaluated at n = 0 — it's 2 standard deviations away in
frequency space, where the standard deviation is 1/σ.

The apparent charge is proportional to this amplitude:

    Q = exp(−2σ²) × Q_max

where Q_max is the charge of a fully localized photon.
The Coulomb energy scales as Q², and the coupling constant
α is the ratio of Coulomb energy to total energy:

    **α = exp(−4σ²)**

Solving for σ:

    **σ = √(ln(1/α) / 4) = 1.109 radians ≈ 63.5°**

This says the photon is concentrated in about **1/6 of the
ring circumference** — not at a single point, but not spread
uniformly either.

Verified both analytically and by numerical integration.


### F6. What this means physically

The fine-structure constant α ≈ 1/137 is the energy in the
n = 0 (charge-producing) Fourier component of the photon's
wavepacket.  It is small because the wavepacket is NEARLY
a pure n = 2 wave — but not quite.  The small n = 0 tail
is what produces the electron's charge.

In the language of our model:
- The photon IS the electron.
- The photon is mostly a wave (delocalized → mass, spin).
- But it is slightly localized (wavepacket → charge).
- The degree of localization determines α.


### F7. Is σ well-defined?

Yes.  For a quantum system in a definite state, the
wavefunction has a definite shape — just as the hydrogen
atom's ground state has a definite Bohr radius a₀.  Any
single measurement of the electron's position gives a random
result, but the shape of the probability cloud is as definite
as the mass of the electron.

If the photon on the torus is in its ground state (the
lowest-energy configuration for the (1,2) topology), that
state has a definite wavefunction ψ(φ) with a definite
width σ.  The value of σ is a property of the state, not a
measurement uncertainty.

The key question is: which state?  On flat Ma_e (the electron sheet) with no
interactions, the eigenstates are pure modes (fully
delocalized, σ = ∞, charge = 0).  But the photon interacts
with its own field — it creates a Coulomb field that acts
back on it.  This self-interaction can localize the wave,
like a ball sitting in a depression it created in a mattress.
The balance between spreading (dispersion) and self-attraction
determines σ.  This is how solitons work: waves that maintain
a definite shape because of nonlinear self-interaction.


### F8. What determines σ? (Open)

The formula α = exp(−4σ²) is exact for a Gaussian
wavepacket.  But what physics forces the photon to have
σ ≈ 1.1 radians, rather than some other value?

Candidates:

1. **Self-interaction (soliton balance).** The photon's own
   Coulomb field modifies the effective potential on the
   torus.  A more localized packet creates a stronger
   Coulomb field, which in turn squeezes or spreads the
   packet.  The self-consistent balance may select a
   specific σ — analogous to how a soliton's width is
   determined by the balance between dispersion and
   nonlinearity.

2. **Mode structure of the material space.**  R12 found that
   the lowest resonant frequency of the flat Ma_e is ~137×
   higher than the Compton frequency.  The wavepacket's
   width σ depends on how many modes participate in the
   superposition.  If only 2–3 adjacent modes contribute,
   σ ~ 1 radian naturally.

3. **Quantum uncertainty.** The photon can't be perfectly
   localized (that would require infinite energy in high
   modes) or perfectly delocalized (that's a single mode
   with zero charge).  Some balance between position
   uncertainty and momentum uncertainty may fix σ.

4. **Topology of the (1,2) knot.**  The path winds twice
   around the ring.  Perhaps the natural wavepacket width
   is set by the winding: one lobe per major loop, giving
   σ ~ π/2 ≈ 1.57 rad.  This gives α ≈ exp(−π²) ≈ 0.08
   — wrong by 10×, but in the right ballpark.

5. **Breaking the torus symmetry.**  On a PERFECT torus
   (circular cross-section, rotationally symmetric), the
   mode number n is strictly conserved, and only
   localization can produce charge.  But if the embedding
   is NOT a perfect torus — for instance an elliptical
   cross-section, a D-shaped tube, or a knotted ring —
   the rotational symmetry is broken.  Different mode
   numbers CAN then couple to each other, potentially
   allowing n = 2 to generate an n = 0 (charge) component
   directly, without needing wavepacket localization at
   all.  In this case, α would be determined by the
   GEOMETRY OF THE DEFORMATION — how far the shape departs
   from a perfect torus.  See Q51.

6. **Dipole radiation pattern as natural deformation.**
   A circularly polarized photon (WvM's model) radiates
   with a non-isotropic pattern: power ∝ (1 + cos²θ)/2.
   If the field leaking from the material space into 3D
   follows this pattern, and if the field energy shapes the
   tube cross-section (self-consistency), the tube is NOT
   circular — it is deformed by the radiation pattern
   itself.  The deformation is not arbitrary; it comes from
   Maxwell's equations.  The chain would be:

     CP photon → non-isotropic radiation → non-circular tube
     → broken symmetry → n=2 couples to n=0 → charge → α

   This is the strongest version of candidate 5 because the
   deformation has a known, computable shape.  See Q51.

7. **Centrifugal radiation pressure (R17).** The photon has
   momentum p = E/c.  On the curved (1,2) helix, centrifugal
   force creates non-uniform radiation pressure on the tube
   wall: stronger at the inner equator (tighter curvature,
   R − a from ring center), weaker at the outer equator
   (R + a).  This deforms the tube cross-section even on a
   perfect torus — no external asymmetry needed.  A balance-
   of-forces argument (spreading from quantum pressure vs.
   concentration from the centrifugal potential well) could
   yield σ directly.  More likely, the deformation route
   applies: the non-circular cross-section breaks azimuthal
   symmetry, enabling n = 2 → n = 0 mode coupling.  This
   is the physical mechanism behind candidate 5, and it
   reinforces candidate 6.  → R17.

None of candidates 1–4 immediately gives σ = 1.109 rad.
Candidates 5–7 are qualitatively different: they bypass the
localization mechanism entirely and make α a geometric
property of the embedding shape.

**Update (R17 complete):** Candidate 7 (centrifugal radiation
pressure) has been ruled out.  R17 Track 4 showed tube
deformation preserves φ-symmetry (charge = 0).  Track 5
showed F ⊥ v (no clumping), σ_φ = const (breathing is
conservative), and the centrifugal force is a consequence
of confinement, not a separate mechanism.

**Update (R18 complete):** Candidate 5 (geometric deformation
of the torus) has been ruled out.  R18 Track 2 showed the
Coulomb cost of the charge exceeds the photon energy saving
by ~96×.  The symmetric torus is energetically stable.
Furthermore, R18 F7 showed the charge integral of cos(θ+2φ)
vanishes on ANY smooth torus — deformed or not.

Candidate 6 (dipole radiation pattern) is likely ruled out
by the same φ-symmetry protection (the radiation pattern
rotates with the mode, so it depends on θ+2φ — the same
combination the charge integral kills).  Not yet directly
computed (see Q54).

**Update (shear analysis):** A new candidate has emerged:

8. **Shear of Ma_e.**  On a sheared Ma_e (lattice
   vectors non-orthogonal, shear displacement δ), the (1,2)
   mode has q_eff = 2 − δ/a (non-integer for δ ≠ 0).  The
   charge integral sin(πq_eff)/q_eff is NONZERO — bypassing
   the φ-symmetry protection entirely.  No wavepacket
   localization needed (σ can be ∞).  R12 F5 showed shear is
   unconstrained internally; the constraint must come from
   outside (T³ geometry, topology).  The question "what
   determines σ?" becomes "what determines δ?"  → R19.

**Remaining viable candidates: 2, 3, 4, 8** (mode structure,
quantum uncertainty, topology of the (1,2) knot, shear).
Candidate 8 is qualitatively different from 2–4: it replaces
the quantum-state parameter σ with the geometric parameter δ.


### F9. Coulomb soliton mechanism fails (Track 5)

**Setup:** Can the Coulomb self-energy of the charge
distribution determine σ?  A Gaussian wavepacket with width σ
produces a charge distribution with cos(θ + 2φ) × Gaussian
modulation.  This distribution has Coulomb self-energy
U_C(σ) and localization kinetic energy U_K(σ).  If the total
U_total(σ) = U_K + U_C has a minimum at finite σ, the soliton
mechanism works.

**Result: negative.**  Both energy contributions DECREASE
monotonically as σ increases:

| σ (rad) | Q/e   | U_K / m_e c²  | U_C / m_e c²  |
|---------|-------|---------------|---------------|
| 0.32    | 1.69  | 0.73          | 4.3 × 10⁻²   |
| 0.57    | 2.11  | 0.12          | 6.7 × 10⁻²   |
| 1.06    | 1.12  | 1.8 × 10⁻³   | 1.9 × 10⁻²   |
| 2.05    | 0.02  | ~0            | 5.0 × 10⁻⁶   |
| 4.02    | ~0    | ~0            | ~0            |

Since U_total is monotonically decreasing, the minimum is
at σ → ∞ (fully delocalized, zero charge).  No finite-σ
equilibrium exists.

**Why it fails — two independent reasons:**

1. **Both energies favor delocalization.**  U_K decreases
   because a wider packet has less localization cost.  U_C
   decreases because a wider packet has less charge (the
   cos(5φ/2) oscillations cancel).  Nothing pulls the system
   toward finite σ.

2. **Self-energy is always positive.**  The Coulomb self-energy
   of ANY charge distribution is ∫ ε₀E²/2 dV ≥ 0.  It is
   always a COST, never a benefit.  A soliton requires an
   attractive self-interaction (negative energy contribution
   from localization), but no such attraction exists for the
   Coulomb field.

**Energy scales:**
- U_K at σ ~ 1 is of order 10⁻³ m_e c²
- U_C at σ ~ 1 is of order 10⁻² m_e c²
- Both are tiny compared to m_e c² = 8.19 × 10⁻¹⁴ J
- The mode spacing equals m_e c² (by construction), so
  one mode of localization costs the entire photon energy

**Implication:** R15 F8 candidate 1 (self-interaction /
soliton balance) is ruled out.  The Coulomb self-energy is
a small perturbation on the system, not the mechanism that
selects σ.  Script: `scripts/track5_self_energy.py`.


## Summary

| Finding | Result |
|---------|--------|
| F1 | Forward calculation gives Q ≈ 8e (too large by √(1/2α)) |
| F2 | Coupling fraction κ = α (Coulomb energy / total energy) |
| F3 | Smooth wave on a symmetric torus → zero charge (exact) |
| F4 | Charge requires the photon to be partially localized |
| F5 | α = exp(−4σ²); σ ≈ 1.1 rad (63°) for α = 1/137 |
| F6 | α = energy fraction in the charge-producing mode |
| F7 | σ is well-defined (like Bohr radius); soliton analogy |
| F8 | What determines σ? Seven candidates; #7 (centrifugal, R17) ruled out; #5–6 (embedding shape) most promising |
| F9 | Coulomb soliton fails — both U_K and U_C decrease with σ; self-energy always positive (repulsive); candidate 1 ruled out |

The chain of reasoning:

    Photon with energy m_e c²
    → confined on a (1,2) torus knot at Compton scale
    → forms a wavepacket of angular width σ around the ring
    → the charge-producing component has amplitude exp(−2σ²)
    → apparent charge Q = exp(−2σ²) × Q_max
    → coupling constant α = Q²/Q_max² = exp(−4σ²)

**Deriving α is equivalent to deriving σ** (the wavepacket
width).

**Ruled-out mechanisms for σ:**
- Candidate 1: Coulomb soliton (F9 — self-energy is repulsive)
- Candidate 7: Centrifugal pressure (R17 — no component along
  path; two-pass cancellation preserves symmetry)

**Surviving candidates:**
- #2: Mode structure of the material space
- #3: Quantum uncertainty (possibly equivalent to #2)
- #4: Topology of the (1,2) knot

**Ruled out:**
- #1: Coulomb soliton (R15 F9)
- #5: Geometric deformation (R18 — Coulomb cost 96× too large; F7)
- #6: Dipole radiation pattern (likely, same φ-symmetry protection — Q54)
- #7: Centrifugal pressure (R17)
