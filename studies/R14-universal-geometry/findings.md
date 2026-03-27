# R14. Universal Geometry — Findings

## Track 0: Feasibility check

**Script:** [`scripts/track0_feasibility.py`](scripts/track0_feasibility.py)

### F1. Geodesics on a material sheet cannot be topologically linked

Linking is a 3D concept — one curve passing through the
interior of another.  On a 2D surface, this is impossible.

Two closed geodesics on a material sheet with winding numbers (p₁, q₁) and
(p₂, q₂) have intersection number I = |p₁q₂ − p₂q₁|.  For
geodesics in the same winding class (e.g., three (1,2)
geodesics), I = 0 — they are parallel and don't even cross.

**This is a negative result for the original R14 hypothesis.**
Three (1,2) photons on a material sheet have no topological interaction.
They can be smoothly deformed to non-intersecting parallel
paths.  There is no mechanism for confinement or forced
binding from material sheet topology alone.


### F2. T³ supports topological linking

On T³ = S¹ × S¹ × S¹ (three material dimensions), closed
curves CAN form genuine 3D links.  A curve on T³ has three
winding numbers (n₁, n₂, n₃).  Two curves that wind around
different pairs of dimensions can be topologically linked.

Three material dimensions provide three distinct linking planes:
(1,2), (2,3), and (1,3).  Three curves, each winding in a
different plane, form a three-component link.

**This maps naturally to three color charges:**

| Color   | Linking plane | Winding       |
|---------|---------------|---------------|
| Red     | (1,2)         | (p, q, 0)     |
| Green   | (2,3)         | (0, p, q)     |
| Blue    | (1,3)         | (p, 0, q)     |

Color neutrality (confinement) would correspond to the
three-component link being topologically trivial as a whole —
the Borromean property (a link where no two components are
linked pairwise, but the triple is inseparable): remove any
one curve and the other two can separate.

**Implication:** If T³ is required for hadrons, the electron
also lives on T³.  It would use 2 of the 3 dimensions for its
(1,2) winding, with the third dimension inert for single-photon
states but essential for multi-photon states.


### F3. Proton mass = 3 × 612 × m_e (to 0.008%)

The proton-to-electron mass ratio is:

    m_p / m_e = 1836.1527

And 1836 = 3 × 612 exactly.

If the proton is three equal-energy photons on the same compact
geometry, each at the 612th harmonic:

    3 × 612 × m_e = 938.194 MeV
    m_p            = 938.272 MeV
    Discrepancy:     0.078 MeV (0.008%)

The factorization 1836 = 2² × 3³ × 17 is naturally divisible
by 3, which the three-photon model requires.

**Neutron:**

    m_n / m_e = 1838.684
    Nearest 3-divisible integer: 1839 = 3 × 613

    3 × 613 × m_e = 939.216 MeV
    m_n            = 939.565 MeV
    Discrepancy:     0.349 MeV (0.037%)

The neutron is less clean than the proton but still suggestive.
The n-p mass difference:

    m_n − m_p = 1.293 MeV = 2.531 m_e
    3 × (613 − 612) × m_e = 3 × m_e = 1.533 MeV

The predicted difference (1.533 MeV) overshoots the measured
value (1.293 MeV) by 19%.  This could indicate unequal photon
energies or interaction corrections.


### F4. Lepton mass ratios are near-integer

| Particle | m / m_e    | Nearest n | Fractional offset |
|----------|-----------|-----------|-------------------|
| Muon     | 206.768   | 207       | −0.11%            |
| Tau      | 3477.228  | 3477      | +0.007%           |
| Proton   | 1836.153  | 1836      | +0.008%           |

The tau ratio is remarkably close to an integer (7 parts per
million).  The muon is close but less precise (0.1%).  If the
mass spectrum comes from harmonics on a fixed geometry, the
non-integer offsets might reflect:
- Binding/interaction energy corrections
- Slightly different geometry for each generation
- Radiative corrections (self-energy shifts)


---

## Conceptual implications

### F5. The material space should be T³, not a single material sheet

Track 0 establishes:
1. A material sheet cannot support topological linking (F1)
2. T³ can, with natural three-color structure (F2)
3. S3 previously found three distinct a/R values for the three
   charge quanta (e, 2e/3, e/3) — consistent with three material
   dimensions (Q13)

The upgrade from a material sheet to T³ has specific consequences:
- Total spacetime dimensions: 3+1+3 = 7 (or 6+1)
- The electron uses a 2D subspace of T³ for its (1,2) geodesic
- Quarks use all three dimensions, with linking providing
  confinement
- Each material dimension has its own circumference (L₁, L₂, L₃)
  and the three aspect ratios (L₁/L₂, L₂/L₃, L₁/L₃) determine
  the three charge values
- The number of free geometric parameters increases (from one r
  to three circumferences), but multi-particle consistency
  provides more constraints

### F6. The three-photon proton mass is not trivially wrong

The 3 × 612 coincidence (F3) is striking.  In standard QCD,
99% of the proton mass comes from gluon field energy, not
quark masses.  In the WvM framework, there are no gluons —
the photon energies ARE the mass.  The fact that m_p/m_e is
divisible by 3 to within 0.008% is consistent with (but does
not prove) a three-photon model.

### F7. R13 and R14 both need T³

The upgrade to T³ affects the entire project:
- R13 (KK charge): the mode decomposition on T³ is richer than
  on a material sheet (three quantum numbers instead of two)
- R14 (universal geometry): linking topology becomes possible
- The electron model (R8): needs re-verification on T³, but
  if the electron uses only 2 of 3 dimensions, the results
  should carry over with the third dimension adding a tower
  of modes that don't affect the (1,2) sector


---

## Track 1: Charge of linked photons on T³

**Script:** [`scripts/track1_linked_charge.py`](scripts/track1_linked_charge.py)

Using R19's charge formula (F29–F34), compute the charge of three
photons — one in each linking plane — as a candidate proton model.

### F8. Three linked photons give total charge +e

Consider three photons, one in each linking plane of T³:

| Plane | Photon winding | Charge mechanism     | Charge |
|-------|----------------|----------------------|--------|
| (1,2) | (1, 2, 0)     | n₁ = 1, n₃ = 0 → e  | **e**  |
| (2,3) | (0, p, q)     | n₁ = 0 → 0 (F30)    | **0**  |
| (1,3) | (1, 0, q)     | n₃ ≠ 0, s₁₃=0 → 0   | **0**  |

Total charge = e + 0 + 0 = **+e**.

This result is **robust**: it holds for ANY winding numbers in
the (2,3) and (1,3) planes.  At s₁₃ = 0, charge is completely
determined by the (1,2)-plane photon.  Two independent mechanisms
silence the other two photons:
- The (2,3) photon has n₁ = 0, killed by the n₁ = 1 rule (F30)
- The (1,3) photon has n₃ ≠ 0, killed by the s₁₃ = 0 rule (F31)


### F9. Neutron charge = 0 from n₁ ≠ 1

Since the (2,3) and (1,3) photons always contribute zero charge,
the total charge depends only on the (1,2)-plane photon.  For a
neutron (total charge = 0), this photon must have n₁ ≠ 1.

Candidates preserving spin 1/2:
- (2, 4, 0): n₁ = 2 → zero charge; spin = 2/4 = 1/2 ✓
- (2, 1, 0): n₁ = 2 → zero charge; spin = 2/1 = 2 (boson)

The (2,4,0) mode is the simplest spin-1/2 neutron candidate.
Its geodesic is twice the electron's length, giving energy m_e/2.
The neutron's mass must then come from the other photons.


### F10. Spin quantization forbids lighter charged modes

At s₁₃ = 0, all (1, n₂, 0) modes carry charge (n₁ = 1, n₃ = 0).
Modes with n₂ > 2 are lighter than the electron and charged.  If
they existed as physical particles, this would be a severe problem.

However, the winding ratio p/q = 1/n₂ determines the spin:

| n₂ | Spin   | Phase per 2π rotation | Statistics        | Physical?  |
|----|--------|----------------------|-------------------|------------|
| 1  | 1      | e^{i2π} = +1         | Boson             | **YES**    |
| 2  | 1/2    | e^{iπ}  = −1         | Fermion           | **YES**    |
| 3  | 1/3    | e^{i2π/3}            | Anyonic (exotic)  | **NO**     |
| 4  | 1/4    | e^{iπ/2}             | Exotic            | **NO**     |
| ≥3 | 1/n₂   | e^{i2π/n₂}           | Exotic            | **NO**     |

In 3+1D spacetime, the spin-statistics theorem (which links a
particle's spin to its exchange symmetry) allows only bosons
(integer spin, symmetric under exchange) and fermions (half-integer
spin, antisymmetric).  A (1, q) geodesic closes after q revolutions
of the ring direction, giving the wavefunction a phase of exp(i2π/q)
per revolution.  For q > 2, this phase is neither +1 nor −1: the
mode is neither bosonic nor fermionic and is **topologically
forbidden** in 3+1D.  (Such exotic phases are possible only in
2+1D, where they describe "anyons" — relevant to the quantum
Hall effect but not to free 3D particles.)

Consequence: the physical charged particle spectrum is:

| Mode     | Spin | E/m_e | Q/Q_e  | Identity          |
|----------|------|-------|--------|-------------------|
| (1,1,0)  | 1    | 1.56  | +2.75  | Charged boson     |
| (1,2,0)  | 1/2  | 1.00  | +1.00  | Electron          |

The electron is the **lightest charged fermion** — protected by
spin quantization, not just by the s₁₃ = 0 selection rule (F31).
The only charged mode lighter than (1,1,0) is the electron itself.

The (1,1,0) mode is a charged spin-1 boson at E ≈ 0.80 MeV.  Its
charge-to-mass ratio Q/Q_e ≈ 2.75 is large.  No such particle is
observed.  However, its spin-1 nature means it could decay rapidly
(bosons are not protected by fermion number conservation), or the
spin argument may need refinement.

**Note:** Modes with negative n₂ also have physical spin if |n₂| ∈ {1, 2}.
The (1, −2, 0) mode has spin 1/2, charge ≈ −0.90e, and E ≈ 1.14 m_e.
The (1, −1, 0) mode has spin 1, charge ≈ −2.14e, and E ≈ 1.84 m_e.
These may correspond to antiparticles or exotic states.


### F11. Charge-mass tension: proton requires uncharged mass carriers

The n₁ = 1 rule (F30) constrains all charged modes on the
electron's T³ to energies of order m_e.  Proton-scale energy
(938 MeV = 1836 m_e) cannot come from charged photons alone.

The resolution: the proton's mass comes from **uncharged photons**
winding in direction 3 of T³:

| Component       | Winding   | Energy  | Charge |
|-----------------|-----------|---------|--------|
| Charge carrier  | (1,2,0)   | m_e     | e      |
| Mass carrier ×N | (0,0,1)   | varies  | 0      |

For L₃ = λ_C/612 ≈ 3.97 fm, a (0,0,1) photon has energy
612 m_e.  Three such photons give 1836 m_e ≈ m_p.  Adding one
(1,2,0) electron-type photon:
  Total mass = 1 + 3×612 = 1837 m_e ≈ m_p ✓
  Total charge = e ✓

This is a **four-photon proton**, not three.  Alternatively,
a three-photon proton could have two uncharged mass carriers
at ~918 m_e each, plus one charged carrier at m_e:
  Total = 1 + 2×918 = 1837 m_e ≈ m_p ✓

In either case, the proton's mass is dominated (>99.9%) by
uncharged photons in the third dimension — analogous to how
QCD has >99% of the proton mass from gluon field energy.


### F12. DIS requires charge redistribution from linking

DIS (deep inelastic scattering: firing high-energy electrons at
protons and observing how they bounce off internal constituents)
reveals three scattering centers in the proton, each coupling
to the EM field:

| Model     | Charges           | Σ e_i²    | Scattering centers |
|-----------|-------------------|-----------|-------------------|
| SM (uud)  | 2/3, 2/3, −1/3   | 1         | 3                 |
| Naive T³  | 1, 0, 0           | 1         | 1                 |

Both models give Σ e_i² = 1 (total charge conservation), but
the SM distributes charge across three partons (constituent
particles inside the proton) while our model — applying R19's
delocalized-mode formula to each photon independently —
concentrates it in one.  DIS clearly resolves three centers,
contradicting the independent-mode result.

**This is the central open problem for R14.**

The R19 charge formula applies to **delocalized** single-photon
modes.  For a multi-photon linked state, the photons must be
**localized** (wavepackets) — a delocalized mode uniformly
filling T³ cannot be meaningfully "linked" with another mode.
Localization introduces a parameter σ (wavepacket width), and
the charge becomes Q(σ, s₁₂, topology).

Linking imposes boundary conditions at the crossing points of
the geodesics, potentially modifying each photon's effective
mode structure and hence its charge.  Whether this redistribution
produces the fractional charges 2/3 and 1/3 is the question
for Track 1, Step 2.


### F13. Two paths forward

**(A) Localized photon charge.**  Compute Q(σ) for a wavepacket
on sheared T³, then determine whether the boundary conditions
imposed by linking produce fractional charges.  This is the
natural extension of R19's charge formula to multi-photon states.

**(B) Multi-component electromagnetism.**  In standard KK on T³,
each compact direction generates its own U(1) gauge field.  If
the physical photon is a linear combination of all three U(1)s,
then photons in all three planes contribute to the EM charge,
and the charge formula changes fundamentally.  This would require
revisiting R19's derivation with the generalized gauge field.


---

## Track 1b: Localized photon charge on sheared T³

**Script:** [`scripts/track1b_localized_charge.py`](scripts/track1b_localized_charge.py)

Track 1 (F12) identified two paths for charge redistribution.
Track 1b tests both.  Both fail.


### F14. Localization cannot charge the (2,3)-plane photon

The (0,1,2) photon's field is uniform in the tube (θ₁) direction,
because its geodesic lies entirely in the (θ₂, θ₃) plane (n₁ = 0).
The charge integral projects the field onto cos(θ₁):

    Q ∝ ∫ψ(θ₁,θ₂,θ₃) cos(θ₁) dθ₁ dθ₂ dθ₃

Since ψ does not depend on θ₁:

    ∫₀²π 1 × cos(θ₁) dθ₁ = 0

This vanishes **independent of the wavepacket envelope** A(θ₂,θ₃).
Localizing the photon to an arbitrarily narrow wavepacket along
its geodesic does not create any θ₁ dependence.  The charge is
exactly zero for any localization width σ.

Verified numerically: Q/Q_e < 10⁻⁶ for all σ tested (0.2 to 10 rad).


### F15. Localization does not enhance the (1,2,0) photon's charge

The (1,2,0) photon's charge depends on its wavepacket width σ.
For a traveling wavepacket (energy-normalized), the charge is
the Fourier transform of the envelope evaluated at frequency
q_eff = 2 − s₁₂ ≈ 1.835:

    Q(σ) ∝ Ã(q_eff)

As σ → ∞ (delocalized): Q → Q_electron (the R19 result).
As σ → 0 (point-like): Q → 0 (too narrow to sustain a monopole).

The delocalized electron has the **maximum stable charge** for
the (1,2) mode.  Localization (as would be imposed by linking)
can only decrease the time-averaged charge.


### F16. Classical EM linking is inert

On a flat T³, Maxwell's equations are linear.  Two EM waves
superpose without interaction.  The total field of three photons
is the sum of their individual fields, and the total charge is
the sum of their individual charges — regardless of whether
their geodesics are topologically linked.

Linking is a property of the **paths** (geodesics), but the
charge formula depends on the **field structure** (mode numbers
and shear).  In linear EM, one photon's field does not affect
another's.

Quantum corrections (photon-photon scattering via QED box
diagrams, a process where four photons interact through virtual
electron-positron pairs) are of order α² ≈ 5 × 10⁻⁵ — far
too small to produce O(1) charge redistribution.


### F17. KK multi-component EM is incompatible with (1,2) electron

In Kaluza-Klein theory (which derives gauge forces from extra
dimensions), each compact direction of T³ generates its own
U(1) gauge field.  If the physical EM field is a linear
combination A_EM = a₁A₁ + a₂A₂ + a₃A₃, then a mode's charge
is Q = a₁n₁ + a₂n₂ + a₃n₃.

Solving for coefficients that give the standard quark charges
(2/3, 2/3, −1/3) for the proton photons yields a₁ = −4/9,
a₂ = 5/9, a₃ = 1/18.  Under these coefficients, the electron
(1,2,0) has charge 2/3 e — it IS a quark.

The problem: the electron and the proton's (1,2)-plane photon
have **identical winding numbers** (1,2,0).  In any scheme
where charge depends only on winding numbers, they must have
the same charge.  No choice of (a₁, a₂, a₃) can simultaneously
give the electron charge e and the proton's (1,2) photon
charge 2/3 e.


### F18. The charge mechanism has a structural limitation

All four mechanisms tested in Track 1b fail:

| Mechanism                | Why it fails                              |
|--------------------------|------------------------------------------|
| Localize (2,3) photon   | Field uniform in θ₁ → charge = 0 always  |
| Localize (1,2) photon   | Localization reduces charge, not enhances |
| Classical EM linking     | Linear Maxwell → no photon interaction    |
| KK gauge mixing          | Same winding = same charge → no e vs 2/3 |

The root cause: the R19 charge formula depends on the **mode
structure** (winding numbers + shear), not on the spatial
arrangement of photons.  The θ₁ integral selects n₁ = 1, and
nothing within the (θ₂, θ₃) plane can change this.  A photon
with n₁ = 0 has zero charge, period.

This is not a technical obstacle but a **structural limitation**
of the current charge mechanism.


### F19. Possible exits

The three-photon proton model requires going beyond the current
framework.  Three possibilities:

**(A) Reinterpret DIS.**  Deep inelastic scattering (firing
high-energy electrons at protons to probe internal structure)
reveals three scattering centers.  But "scattering center" means
"localized energy concentration that couples to the EM probe" —
not necessarily "carrier of fractional charge."  The three linked
photons ARE three energy concentrations.  Their EM scattering
cross-sections could differ from their monopole charges if the
probe sees field amplitude rather than total flux.

**(B) Beyond linear EM.**  R19's charge formula assumes free
(non-interacting) photons on flat T³.  If the photons are
topological solitons (stable, localized field configurations
like vortices), the linking topology imposes O(1) boundary
conditions that modify the mode structure.  This goes beyond
the WvM picture of "photons as ordinary EM waves."

**(C) Beyond flat T³.**  If the material space has curvature
(like a Calabi-Yau manifold, the kind of space used in string
theory compactifications), the mode structure and charge
projections could be fundamentally different.  Curvature could
couple the θ₁ direction to the others, allowing modes with
n₁ = 0 in the flat limit to acquire effective n₁ ≠ 0 charge.


---

## Summary table

| # | Finding |
|---|---------|
| F1 | Geodesics on a material sheet cannot be topologically linked |
| F2 | T³ supports linking; three planes → three color charges |
| F3 | Proton mass = 3 × 612 × m_e to 0.008% |
| F4 | Lepton mass ratios are near-integer (tau: 7 ppm) |
| F5 | The material space should be T³, not a single material sheet |
| F6 | The three-photon proton mass is not trivially wrong |
| F7 | R13 and R14 both need T³ |
| F8 | Three linked photons give total charge +e (robust at s₁₃ = 0) |
| F9 | Neutron charge = 0 when (1,2)-plane photon has n₁ ≠ 1 |
| F10 | Spin quantization forbids (1,n₂>2,0) modes → electron is lightest charged fermion |
| F11 | Proton mass requires uncharged photons in direction 3 (charge-mass tension) |
| F12 | Deep inelastic scattering requires three charged constituents, not one |
| F13 | Two paths tested: (A) localized wavepacket, (B) multi-component EM |
| F14 | Localization cannot charge the (2,3)-plane photon — field uniform in θ₁ |
| F15 | Localization reduces (1,2,0) photon's charge — delocalized = maximum |
| F16 | Classical EM linking is inert — linear Maxwell, no photon interaction |
| F17 | KK gauge mixing gives same charge to electron and quark — incompatible |
| F18 | Structural limitation: charge depends on mode numbers, not spatial arrangement |
| F19 | Possible exits: (A) reinterpret DIS, (B) beyond linear EM, (C) beyond flat T³ |


## Scripts

- [`scripts/track0_feasibility.py`](scripts/track0_feasibility.py)
  — Topology on a material sheet and T³, proton mass arithmetic, harmonic
  spectrum
- [`scripts/track1_linked_charge.py`](scripts/track1_linked_charge.py)
  — Charge of linked photons: R19 formula applied to three-photon
  proton/neutron candidates; spin analysis; DIS constraints
- [`scripts/track1b_localized_charge.py`](scripts/track1b_localized_charge.py)
  — Localized photon charge: wavepacket analysis, KK gauge mixing,
  structural limitation of the charge mechanism
