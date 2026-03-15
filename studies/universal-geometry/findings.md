# R14. Universal Geometry — Findings

## Track 0: Feasibility check

**Script:** [`scripts/track0_feasibility.py`](scripts/track0_feasibility.py)

### F1. Geodesics on T² cannot be topologically linked

Linking is a 3D concept — one curve passing through the
interior of another.  On a 2D surface, this is impossible.

Two closed geodesics on T² with winding numbers (p₁, q₁) and
(p₂, q₂) have intersection number I = |p₁q₂ − p₂q₁|.  For
geodesics in the same winding class (e.g., three (1,2)
geodesics), I = 0 — they are parallel and don't even cross.

**This is a negative result for the original R14 hypothesis.**
Three (1,2) photons on T² have no topological interaction.
They can be smoothly deformed to non-intersecting parallel
paths.  There is no mechanism for confinement or forced
binding from T² topology alone.


### F2. T³ supports topological linking

On T³ = S¹ × S¹ × S¹ (three compact dimensions), closed
curves CAN form genuine 3D links.  A curve on T³ has three
winding numbers (n₁, n₂, n₃).  Two curves that wind around
different pairs of dimensions can be topologically linked.

Three compact dimensions provide three distinct linking planes:
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
the Borromean property: remove any one curve and the other two
can separate.

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

### F5. The compact space should be T³, not T²

Track 0 establishes:
1. T² cannot support topological linking (F1)
2. T³ can, with natural three-color structure (F2)
3. S3 previously found three distinct a/R values for the three
   charge quanta (e, 2e/3, e/3) — consistent with three compact
   dimensions (Q13)

The upgrade from T² to T³ has specific consequences:
- Total spacetime dimensions: 3+1+3 = 7 (or 6+1)
- The electron uses a 2D subspace of T³ for its (1,2) geodesic
- Quarks use all three dimensions, with linking providing
  confinement
- Each compact dimension has its own circumference (L₁, L₂, L₃)
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
  on T² (three quantum numbers instead of two)
- R14 (universal geometry): linking topology becomes possible
- The electron model (R8): needs re-verification on T³, but
  if the electron uses only 2 of 3 dimensions, the results
  should carry over with the third dimension adding a tower
  of modes that don't affect the (1,2) sector


## Scripts

- [`scripts/track0_feasibility.py`](scripts/track0_feasibility.py)
  — Topology on T² and T³, proton mass arithmetic, harmonic
  spectrum
