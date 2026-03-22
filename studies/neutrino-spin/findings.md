# R25. Neutrino Spin and T³ Topology — Findings

## Track 1: Spin analysis of (0,0,n₃) modes

### F1. Mechanism A fails — shear does not redirect wavevectors

On a sheared T³, the lattice vector a₃ = (s₁₃L₁, s₂₃L₂, L₃) is
tilted, but the wavevector of mode (0,0,n₃) is determined by the
reciprocal lattice: **k = (0, 0, 2πn₃/L₃)** regardless of shear.

The effective quantum numbers for n₁ = n₂ = 0 are q₁ = 0, q₂ = 0,
q₃ = n₃ — no shear terms survive.  The mode propagates purely along
θ₃ with zero tube/ring winding.  No angular momentum about the
symmetry axis.  **Spin = 0.**

### F2. Mechanism B is inapplicable — spin structures affect spinors, not vectors

A flat T³ admits 2³ = 8 spin structures (periodic/anti-periodic
boundary conditions in each direction).  These affect spinor fields
(spin-½), not vector fields (spin-1).

The photon is a vector field.  The electron's spin-½ comes from a
dynamical mechanism (L = E/ωs where ωs = n_φ·ω), not from the
photon becoming a spinor.  The WvM model converts spin-1 → spin-½
through the (1,2) orbit topology.  Without that orbit (n₁ = n₂ = 0),
no conversion occurs.

### F3. Mechanism C fails — curvature mixing is perturbatively negligible

The embedded T² mixes θ₁ modes (R22), so a (0,0,n₃) mode could
mix with (m,0,n₃) modes acquiring a spin-½ component.

Mixing amplitude: V/ΔE ~ (ε × E_ν) / E_e ~ (0.2 × meV) / (0.5 MeV)
~ 4 × 10⁻¹⁰.  Spin contribution: c² × ℏ/2 ~ 10⁻¹⁹ ℏ.  Negligible.

Furthermore, on a product space T² × S¹, the curvature Hamiltonian
factorizes: it acts on the (θ₁,θ₂) wavefunction but leaves the θ₃
part as a spectator.  The mode's quantum numbers (0,0,n₃) are not
changed by curvature — only the T² eigenmodes are corrected.

### F4. The charge-spin linkage (structural result)

In the WvM framework, both charge and spin-½ are controlled by the
same quantum number n₁ (tube winding):

| n₁ | Charge (R19) | Spin (knot-zoo) | Example |
|----|-------------|----------------|---------|
| 0  | Q = 0       | integer (boson) | harmonics, θ₃ modes |
| ±1 | Q = ±e      | half-integer (fermion) | electron |

The conditions "uncharged" (n₁ = 0) and "fermion" (n₁ odd) are
**mutually exclusive**.  They are contradictory requirements on
the same quantum number.

An exhaustive search over all modes with |n₁|, |n₂| ≤ 5,
|n₃| ≤ 10 confirms: the intersection of {uncharged} and {fermion}
is empty (0 out of 1616 non-trivial modes).

Additionally, light mass (meV) requires n₂ = 0 (since q₂ = n₂ for
uncharged modes, and n₂ ≠ 0 gives E ~ m_e/r ~ 100 keV).  This
creates a closed trap:

    Light (meV)  →  n₂ = 0
    Uncharged    →  n₁ = 0
    Spin-½       →  n₁ odd  (contradicts uncharged)

### F5. T³ neutrino model fails at the spin gate

Despite remarkable kinematic success:
- Mass-squared ratio 33.63 from integers alone (0.03σ match)
- Σm = 72 meV (below cosmological bound)
- Over-determined system (4 observables vs 3 parameters)

...modes (0,0,n₃) are spin-0 bosons, not spin-½ fermions.
**They cannot be neutrinos.**

### F6. Scope: this is a structural limitation of the WvM spin mechanism

The charge-spin linkage (F4) is not specific to T³.  It applies to
**any** compact-dimension model that uses the WvM spin mechanism
(L = E/ωs with ωs from ring winding, fermion/boson from tube
parity).  The mechanism inherently links charge to spin: both
require tube traversal (n₁ ≠ 0).

The neutrino — an uncharged fermion — falls in a category that
this mechanism cannot produce.

### F7. Implications

The neutrino must exist (angular momentum conservation in beta
decay demands a fermion — see `../torus-dynamics/neutrinos.md`).
The WvM framework currently has no mechanism to produce it.

**Track 2 (PMNS from T³ geometry) is cancelled.**  Without
spin-½ neutrinos, the PMNS derivation has no target and the
r-selection path through neutrino mixing is closed.

Possible paths forward:

**(a) A different spin mechanism.**  If spin-½ could arise from
something other than tube winding — e.g., from the photon's
intrinsic angular momentum coupling to the compact geometry in
a way that doesn't require charge — the charge-spin linkage
would be broken.  This would require modifying a foundational
element of the WvM model.

**(b) Composite neutrinos.**  Three spin-½ particles can form a
spin-½ composite (e.g., ↑↑↓).  But the only available spin-½
particles are charged (electrons/positrons).  A neutral composite
of charged particles (e.g., eēe) would need a binding mechanism.

**(c) Beyond the WvM framework.**  The neutrino might arise from
a field type not currently in the model (e.g., a gravitational
mode, a topological defect, or a fundamentally different compact
structure).

---

## Status

| Track | Status | Key finding |
|-------|--------|-------------|
| Track 1 | **Complete** | Charge-spin linkage (F4): uncharged fermions impossible in WvM |
| Track 2 | **Cancelled** | Depends on Track 1 succeeding; it did not |
