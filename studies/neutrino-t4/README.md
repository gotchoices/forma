# R26. Neutrino on T⁴ — two-scale compact geometry

**Questions:** Q14 (neutrino), Q18 (α / r-selection), Q32 (energy-geometry)
**Type:** compute/analytical  **Depends on:** R25, R24, R19, R20

## The problem

The neutrino is the hardest open problem in the compact-dimension model.
Twenty-five studies have established:

1. The electron is a (1,2) photon on a sheared T² at pm scale.  Spin ½
   from the 1:2 winding ratio, charge e from shear (R19).
2. The proton/neutron are the electron fundamental plus uncharged
   harmonics on the same T² (R20).
3. The neutrino must exist — angular momentum conservation in beta
   decay requires a spin-½ fermion (see `../torus-dynamics/neutrinos.md`).
4. No mode on the electron's T² can be a neutrino: the lightest
   uncharged mode is 245 keV, five orders of magnitude too heavy (R20 F14).
5. On T³ (three compact dimensions), pure θ₃ modes (0,0,n₃) have the
   right mass scale and reproduce the mass-squared ratio to 0.03σ
   (R24 F3).  But they are spin-0 — the WvM mechanism cannot give them
   spin ½ (R25 F4–F5).
6. The structural barrier (R25 F4): in the WvM framework, spin ½
   requires tube winding (n₁ = 1), and tube winding produces charge.
   "Uncharged fermion" appears impossible — charge and spin are
   controlled by the same quantum number.

The root cause of the T³ failure: there is only one large compact
dimension (L₃ ~ μm).  A standing wave along a single direction has
no winding ratio — it cannot carry spin ½.  The neutrino needs a
(1,2) winding for spin, and that requires **two** large dimensions.

## The proposal: T⁴

Upgrade the compact space from T³ to T⁴ = S¹ × S¹ × S¹ × S¹ with
four compact dimensions arranged in a two-scale hierarchy:

| Dimension | Label | Scale | Role |
|-----------|-------|-------|------|
| θ₁ | tube | ~pm | electron charge/spin (small) |
| θ₂ | ring | ~pm | electron mass (small) |
| θ₃ | ν-tube | ~μm | neutrino spin (large) |
| θ₄ | ν-ring | ~μm | neutrino mass (large) |

The electron lives on the (θ₁, θ₂) subplane — unchanged from the
existing model.  The neutrino lives on the (θ₃, θ₄) subplane — a
second T² at a vastly larger scale.

### Neutrino mode: (0, 0, 1, 2)

A photon with winding numbers (n₁, n₂, n₃, n₄) = (0, 0, 1, 2):

- **Spin ½:** The 1:2 winding ratio on the (θ₃, θ₄) plane gives
  spin ½ through the same WvM mechanism as the electron.  No new
  spin mechanism is needed.

- **Charge 0:** n₁ = 0 means no winding on the electron's tube.
  The R19 charge formula requires n₁ = 1 (F30).  With n₁ = 0,
  charge is exactly zero regardless of shear.

- **Mass ~ meV:** Both L₃ and L₄ are μm-scale.  The mode energy is
  E = ℏc √((1/L₃)² + (2/L₄)²), which is in the meV range.  For
  comparison, on T³ with only one μm dimension, the (0,0,n₃) mode
  has mass ~ meV but no winding ratio — hence no spin.

This is the first candidate that satisfies all three neutrino
requirements (spin ½, charge 0, mass ~ meV) using the existing WvM
spin mechanism.

### Why T⁴ is not just "two separate T²s"

Two independent T² spaces (one for electrons, one for neutrinos)
would give the same single-particle spectrum.  The critical
difference is **coupling**.

On a general T⁴, the lattice has six shear parameters:

| Shear | Planes | Role |
|-------|--------|------|
| s₁₂ | (θ₁, θ₂) | electron charge (≈ 0.165, from α) |
| s₃₄ | (θ₃, θ₄) | neutrino charge (= 0 for Q = 0) |
| s₁₃, s₁₄, s₂₃, s₂₄ | cross-plane | **coupling between sectors** |

Without cross-shear (all s_{ij} = 0 between planes), the T⁴
factorizes as T²_small × T²_large.  Modes separate completely.
There is no mechanism for neutrino production in beta decay — the
electron sector and neutrino sector are disconnected.  This is
physically identical to two independent T²s.

With nonzero cross-shear, the sectors couple:

1. **Neutrino production:** During neutron decay, energy in the
   (θ₁, θ₂) sector can flow into the (θ₃, θ₄) sector through
   cross-shear coupling.  The neutrino is produced geometrically,
   not by fiat.

2. **Mixing angles:** Cross-shear determines how neutrino mass
   eigenstates (modes on the large T²) couple to charged leptons
   (modes on the small T²).  The PMNS matrix should emerge from
   the four cross-shear parameters.

3. **Constraints:** Four cross-shear parameters are constrained by
   four PMNS observables (θ₁₂, θ₂₃, θ₁₃, δ_CP).  The system is
   exactly determined — or over-determined if additional observables
   (mass ratios, Majorana phases) provide further constraints.

### Three neutrino flavors

On the neutrino T² (θ₃, θ₄), the (p, 2p) family of modes all have
spin ½ (winding ratio p:2p = 1:2).  Three flavors correspond to
three such modes with different masses:

    ν₁ = (0, 0, n_a, 2n_a)     lightest
    ν₂ = (0, 0, n_b, 2n_b)     middle
    ν₃ = (0, 0, n_c, 2n_c)     heaviest

The mass of mode (0, 0, p, 2p) on the neutrino T² depends on p,
the aspect ratio r_ν = L₃/L₄, and the shear s₃₄ (which must be
zero for charge neutrality):

    m(p) = (ℏc/L₃) × p × √(1 + 4/r_ν²)

Masses scale linearly with p: m(p) = p × m(1).

The mass-squared ratio is then:

    Δm²₃₁/Δm²₂₁ = (n_c² − n_a²) / (n_b² − n_a²)

This is the same integer-ratio formula as R24 F3 — parameter-free.
The kinematic success of T³ carries over exactly.  The (7, 10, 42)
assignment matches 33.63 (0.03σ).  But now the modes ALSO have
spin ½.

### Charge neutrality constraint on s₃₄

On the electron's T², shear s₁₂ ≈ 0.165 breaks symmetry and
produces charge.  On the neutrino's T², s₃₄ must be zero (or
integer) to keep neutrinos uncharged.

The R19 charge formula extends to the neutrino plane:

    Q_ν ∝ sin(2π s₃₄)

At s₃₄ = 0: Q_ν = 0 exactly.  This is not fine-tuned — it is the
natural unsheared state.  Shear is what's special (the electron's
T² is sheared); the absence of shear is the default.

### Scale hierarchy

The electron T² has circumferences L₁, L₂ ~ pm (set by m_e c²).
The neutrino T² has circumferences L₃, L₄ ~ μm (set by neutrino
masses ~ meV).  The ratio is:

    L_ν / L_e ~ m_e / m_ν ~ 10⁶

This hierarchy is large but not unprecedented — it mirrors the
observed mass hierarchy between electrons and neutrinos.  The model
does not explain the hierarchy, but it localizes it: the ratio of
compact-dimension scales IS the mass ratio, directly.

### Total spacetime

    3 (spatial) + 1 (time) + 4 (compact) = 8 dimensions

or equivalently 7+1.  This is within the range of string theory
compactifications (10 or 11 total), though the model does not
invoke string theory.

### What R25 F4 actually says — and what it missed

R25's charge-spin linkage concluded that "uncharged fermion" is
impossible because n₁ = 0 → spin integer and n₁ = 1 → charged.

This is correct **on the electron's T²**.  But on T⁴, spin can
arise from winding on a *different* subplane.  Mode (0, 0, 1, 2)
has n₁ = 0 (uncharged on the electron plane) and winding ratio 1:2
on the (θ₃, θ₄) plane (spin ½).  The charge-spin linkage is broken
by having two independent winding planes — charge is generated by
the sheared plane, spin by whichever plane has a 1:2 winding.

R25 was correct within its scope (T³, where only one large dimension
exists).  T⁴ evades the structural barrier by providing a second
large dimension for the neutrino's winding.

## Tracks

### Track 1 — Mode spectrum and mass predictions

Enumerate modes on T⁴ with the two-scale hierarchy.  Compute
energies for all (n₁, n₂, n₃, n₄) modes with small quantum numbers.
Verify:

1. Electron (1, 2, 0, 0) has E = m_e c² with appropriate L₁, L₂
2. Neutrino (0, 0, 1, 2) has E ~ meV with appropriate L₃, L₄
3. Mass-squared ratios for the (0, 0, p, 2p) family match
   experimental neutrino oscillation data
4. No unexpected light charged modes appear

Determine L₃, L₄ (or equivalently r_ν = L₃/L₄) from the neutrino
mass data.

### Track 2 — Cross-shear and PMNS mixing

Derive how cross-shear (s₁₃, s₁₄, s₂₃, s₂₄) couples the electron
and neutrino sectors.  Compute the effective mixing matrix:

    (s₁₃, s₁₄, s₂₃, s₂₄) → (θ₁₂, θ₂₃, θ₁₃, δ_CP)

If the mapping is invertible, the four PMNS observables uniquely
determine the four cross-shear parameters.  Check consistency:
do the resulting shear values produce the correct coupling strength
for beta decay rates?

### Track 3 — r-selection from over-determination

With the neutrino sector providing additional constraints, revisit
the r-selection problem.  The electron's aspect ratio r = L₁/L₂
has been free throughout all studies.  On T⁴:

- s₁₂(r) is fixed by α (R19)
- L₃, L₄ are fixed by neutrino masses
- Cross-shears are fixed by PMNS angles (Track 2)
- Any remaining constraint (e.g., a geometric consistency condition
  on the T⁴ lattice, or a quantization condition from modular
  invariance) would determine r

If r is predicted, m_e follows, and the model becomes fully
predictive.

### Track 4 — Sterile neutrino suppression

On the neutrino T², modes (0, 0, p, 2p) with p between the three
active flavors exist and could behave as sterile neutrinos.  For the
(1, 2, 10) assignment: p = 3–9 are intermediate.  For (7, 10, 42):
p = 8–41 are intermediate.

Determine whether cross-shear coupling suppresses these modes'
interaction with the charged sector.  If the coupling to charged
leptons depends on the mode number p, heavy modes might decouple
naturally.  Compare predicted N_eff with CMB constraint
(N_eff = 2.99 ± 0.17).

## Risk assessment

- **Track 1:** Low risk.  Straightforward mode enumeration.  The
  mass-squared ratio is inherited from R24 and is already a strong
  match.  Main risk: unexpected light modes with problematic quantum
  numbers.

- **Track 2:** Medium risk.  The cross-shear → PMNS mapping requires
  understanding how modes on different T² subplanes couple through
  the weak interaction analog in this framework.  The weak interaction
  has not yet been addressed in the model — this track may need to
  define it.

- **Track 3:** High risk, high reward.  Requires Track 2 to succeed
  AND produce an additional constraint beyond the four PMNS angles.
  If it works, the model becomes fully predictive.

- **Track 4:** Medium risk.  Sterile neutrino suppression is the same
  challenge as R24 Q2, now potentially solvable through cross-shear
  selectivity.

## Dependencies

| Study | What it provides |
|-------|-----------------|
| R19 | Charge formula, s₁₂ from α, n₁ = 1 selection rule, s₁₃ = 0 |
| R20 | Harmonic proton model, neutrino mass floor on T² (245 keV) |
| R24 | T³ kinematics: mass-squared ratio, L₃ scale, parameter counting |
| R25 | Spin gate: T³ fails, charge-spin linkage on single T² |
| R21 | Curvature effects on embedded torus (parity selection rule) |

## Relation to prior neutrino attempts

| Study | Mechanism | Result | What T⁴ inherits |
|-------|-----------|--------|-----------------|
| R20 F14 | Eigenmode on electron's T² | Mass too high (245 keV floor) | Electron sector unchanged |
| R23 | Beating between near-degenerate modes | Not selective; phonon blocked | — |
| R24 T1 | Pure θ₃ modes on T³ | Kinematics perfect, spin = 0 | Mass-squared ratio formula |
| R25 | Spin analysis of T³ modes | Structural failure: n₁ controls both charge and spin | Evaded: spin from second T² |
| **R26** | **(0,0,1,2) on T⁴** | **Spin ½ ✓, Q = 0 ✓, m ~ meV ✓** | **All three requirements met** |

## What this study does NOT address

- **Why four compact dimensions?**  The model does not derive the
  number of compact dimensions from first principles.  T⁴ is
  motivated by the requirements (spin + charge + mass), not by a
  deeper geometric principle.  String theory requires 6 or 7 compact
  dimensions; this model uses 4.

- **The mass hierarchy.**  Why L₃, L₄ ~ μm while L₁, L₂ ~ pm is
  not explained.  The hierarchy is equivalent to the observed
  electron-neutrino mass ratio and is taken as input.

- **Quarks and confinement.**  The quark problem (fractional charges,
  DIS structure, confinement) remains open.  T⁴ provides more
  geometric room than T³ but this study does not address quarks.

- **Gravity.**  If gravity propagates in all compact dimensions,
  L₃, L₄ ~ μm would modify gravity at sub-millimeter scales.
  Current experimental bounds constrain extra dimensions to
  < ~50 μm.  This is compatible with the (1, 2, 10) assignment
  (L₃ ~ 250 μm is marginal) but may exclude (7, 10, 42)
  (L₃ ~ 1 mm).  A gravity-confining mechanism may be needed.
