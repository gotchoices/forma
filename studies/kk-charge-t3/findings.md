# R13. Charge from the Embedding — Findings

## Track 1: KK mode spectrum and the electron's identity

**Script:** [`scripts/track1_kk_charge.py`](scripts/track1_kk_charge.py)

### F1. The electron is NOT a KK momentum mode

The KK mode (n₁, n₂, n₃) on T³ with circumferences L₁, L₂, L₃
has mass:

    m_KK c² = 2πℏc × √((n₁/L₁)² + (n₂/L₂)² + (n₃/L₃)²)

The electron wraps 68 times around the minor circle and 137
times around the major circle.  Its KK mode would be (68, 137, 0),
with mass:

    m_KK(68,137,0) ≈ 18 GeV

This is ~36,000 times the electron mass (0.511 MeV).

Even the simplest non-trivial KK mode has mass far above the
electron:

| Mode     | KK mass    | Ratio to m_e |
|----------|------------|--------------|
| (0,1,0)  | 71 MeV     | 139          |
| (1,0,0)  | 229 MeV    | 449          |
| (1,2,0)  | 270 MeV    | 528          |
| (68,137,0)| ~18 GeV   | ~36,000      |

The electron sits in the spectral gap between the zero mode
(massless, the 4D photon) and the first excited KK mode
(~71 MeV).  This is the same gap identified in R12 Track 1:
ω_C / ω_min ~ α.


### F2. KK mass ≠ Compton mass

The KK mass and the Compton mass are DIFFERENT formulas:

    E_KK = 2πℏc × √(Σ (n_a/L_a)²)   [√ of sum of squares]
    E_C  = 2πℏc / √(Σ (n_a L_a)²)    [1/√ of sum of squares]

For the electron geometry (L₁ = 2πa, L₂ = 2πR):

    E_KK(1,2,0)  = 270 MeV
    E_Compton     = 0.511 MeV

The Compton formula (path length = wavelength) gives the
correct electron mass.  The KK formula gives the mass of a
heavy mode that is NOT the electron.

The two formulas agree only when all circumferences are equal
(L₁ = L₂ = L₃).  For the electron's aspect ratio r ≈ 0.31
(L₁ ≈ 0.31 × L₂), they differ by orders of magnitude.


### F3. The electron is a WINDING mode

In string theory, states on compact spaces are characterized
by two types of quantum numbers:
- **Momentum** quantum numbers n_a: how many wavelengths fit
  around each circle.  KK modes.
- **Winding** quantum numbers w_a: how many times the string
  wraps around each circle.  Topological.

These have OPPOSITE scaling with the circumference L:
- Momentum mode mass ∝ n/L  (lighter at large L)
- Winding mode mass  ∝ wL   (lighter at small L)

The electron's compact space is very small (L ~ 10⁻¹⁵ m).
In this regime, winding modes are light and momentum modes
are heavy.  The electron is a winding mode:
- Winding numbers: (p, q) = (68, 137) on T²
- Effective compact momentum: ~zero (n_eff ~ 10⁻³)
- Mass from Compton condition: ℏc/(path length) = m_e c²

The key distinction: the electron's mass comes from the TOTAL
PATH LENGTH (how far the wave travels before closing), not
from its compact momentum (how many wavelengths fit on one
circumference).


### F4. Standard KK charge does NOT apply

In standard KK theory, the 4D electric charge of a particle
comes from its compact momentum:

    e_KK = g₄ × 2πn/L

where g₄ = g_D/√V is the 4D gauge coupling, n is the compact
momentum quantum number, and L is the circumference.

The electron has effectively zero compact momentum (n ~ 10⁻³).
The standard KK charge formula gives ~zero charge.

This is NOT a failure — it correctly tells us that the electron
is not a momentum-charged particle.  Its charge comes from a
different mechanism.


### F5. Charge from field configuration (WvM mechanism)

The electron's charge comes from the EM FIELD CONFIGURATION,
not from compact momentum.  Specifically:

The photon propagating along the geodesic has a polarization
vector (E-field direction) transverse to the propagation
direction.  As the photon winds around the compact space, the
polarization rotates relative to the 3+1D coordinate axes.
The time-averaged field has a net monopole moment — this IS
the charge.

In WvM's original derivation (on an embedded torus), the
curvature of the embedding causes the polarization to rotate.
The net radial E-field, integrated over the torus surface,
gives charge e.


### F6. Flat T³ alone gives zero charge — the embedding provides it

On a flat T³, geodesics are straight lines in the covering
space.  Parallel transport along a straight line on a flat
manifold preserves vectors exactly — there is NO rotation.
Therefore, a photon propagating on flat T³ with no embedding
information develops no monopole moment and no charge.

This was initially framed as a "tension" with the WvM model.
It is not.  The correct physical picture (see R12 F14
revised) has two domains:

- **Internal (flat T³):** The photon propagates through
  flat space.  This determines mass and spin.  No charge
  arises here — and none should.
- **External (embedding):** The compact space is embedded
  in 3+1D with a toroidal geometry.  The photon's fields,
  when they extend beyond the compact space, encounter
  this embedding.  The curvature of the embedding rotates
  the polarization, creating the net monopole moment = charge
  (the WvM mechanism).

The flat-T³ zero-charge result is therefore expected, not
problematic.  Charge is a projection property — it arises
from how compact-space fields appear in 3D, not from the
internal geometry.

**The open question is not "how does charge arise" (answer:
the embedding) but "what determines the embedding geometry"
(equivalently: what determines α).**


---

## Conceptual implications

### F7. Winding vs momentum — a fundamental distinction

The KK framework assumes particles are momentum modes of
compact dimensions.  The WvM electron is a winding mode.
These are qualitatively different:

| Property       | Momentum mode     | Winding mode       |
|---------------|-------------------|---------------------|
| Mass           | ∝ n/L (heavy at small L) | ∝ wL/ℓ (light at small L) |
| Charge         | ∝ n/L (KK charge) | From field topology  |
| Quantization   | n = integer        | w = integer          |
| Light when     | L is large         | L is small           |

The electron is light because the compact space is small —
exactly the winding-mode regime.  This is why the electron
mass (0.511 MeV) is far below the KK gap (~71 MeV).

String theory's T-duality relates the two: momentum modes on
a circle of radius R ↔ winding modes on a circle of radius
α'/R.  This suggests there may be a dual description of the
electron as a momentum mode on a LARGE dual circle — but this
introduces the string tension α' as a new parameter.


### F8. What the correct calculation requires

To compute the electron's charge from first principles on T³,
we need to:

1. Write the full EM field of a photon propagating along the
   (68,137) geodesic on flat T³
2. Specify the embedding: how the compact dimensions map into
   3+1D spatial directions
3. Project the compact-space field into 3+1D using the
   embedding geometry
4. Extract the monopole moment = apparent charge

Step 2 is the crux — and it IS determined by the model.
The WvM model specifies a toroidal embedding where the
compact T² (or T³) sits inside 3+1D as a torus of major
radius R and minor radius a.  This is the embedding that
produces charge via polarization rotation.

In KK language, the embedding information lives in the
metric's off-diagonal components (the gauge connection
A^a_μ).  In the WvM picture, it is the 3D torus geometry.
These are likely equivalent descriptions — the KK gauge
connection encodes the same information as the embedding map.

**The remaining open question:** the embedding has free
parameters (R, a, and hence r = a/R).  What determines the
specific embedding geometry?  This is the α problem:
different embeddings would give different effective charges,
and only one matches the measured e.


## Track 1 Summary

| Finding | Result |
|---------|--------|
| Electron as KK mode | NO — mass is ~36,000× too high |
| Standard KK charge | Does not apply (zero compact momentum) |
| Electron identity | Winding mode (topological, not dynamical) |
| Charge mechanism | Field projection via embedding (WvM), not KK momentum |
| Flat T³ alone | ZERO charge (expected — charge is a projection property) |
| Embedding role | Provides the polarization rotation → monopole moment |

**The electron's charge comes from the embedding of the compact
space in 3+1D** — the toroidal geometry that the photon's fields
encounter when they extend beyond the compact dimensions.  This
is the WvM mechanism, now understood as a projection property
rather than an internal property of the flat compact space.

The open question is not how charge arises (the embedding
provides it) but what determines the specific embedding geometry
(which determines α).


---

## Track 2: Four candidate charge mechanisms

**Script:** [`scripts/track2_charge_mechanisms.py`](scripts/track2_charge_mechanisms.py)

### F9. 7D cross-terms cannot generate charge on flat T³

The 7D Maxwell equations on flat T³ give zero volume-averaged
4D current: ∫_T³ ∂_a F^aν d³y = 0 by periodicity.  A winding
mode on flat T³ produces NO long-range Coulomb field.  This
independently confirms F6: charge cannot arise from the flat
interior alone.  (Under the corrected picture, this is expected
— charge comes from the embedding, not the interior.)


### F10–F13. What determines the embedding geometry?

The charge mechanism is understood: the toroidal embedding
provides the polarization rotation that creates the monopole
moment (WvM mechanism, see F6 revised).  The open question
is: **what determines the specific embedding geometry?**  The
embedding has free parameters (R, a, hence r = a/R), and
different embeddings give different effective charges.  Only
one matches e.  This is the α problem.

Four candidate answers were analyzed for what could constrain
the embedding:

**Candidate 1: Gravitational curvature.**
Einstein gravity gives compact curvature ~10⁻¹⁶ m⁻².  The
embedded torus has curvature ~10²⁹ m⁻².  The ratio is ~10⁴⁵
— standard gravity is hopelessly weak to determine the
embedding.  However, this ratio IS the hierarchy problem.
If some mechanism makes gravity stronger at the compact
scale, it could determine the embedding and hence α — which
would unify EM and gravity through 7D geometry.

**Candidate 2: KK gauge connection (off-diagonal metric).**
In KK theory, off-diagonal metric terms encode how compact
dimensions connect to spatial dimensions.  This is the formal
description of the embedding.  It explains charge quantization
(integer winding → integer charge) but doesn't explain what
determines the off-diagonal terms themselves.  It describes
the embedding rather than determining it.

**Candidate 3: Topological constraint.**
If a mathematical theorem guarantees that any winding-w field
configuration on T³ embedded in 3+1D has monopole moment ∝ w,
then the existence of charge is topologically forced.  This
would make charge quantization and conservation automatic.
However, the "charge per winding" (i.e., α) would still
depend on the embedding geometry.

**Candidate 4: 7D field equation cross-terms.**
ELIMINATED (F9).  Periodicity forces zero net 4D current.

**Assessment:** Candidates 1–3 are complementary, not
competing.  Topology (Cand. 3) guarantees THAT the winding
mode is charged.  The embedding geometry (described by
Cand. 2) determines HOW MUCH charge.  And the deepest
question — what fixes the embedding — connects to gravity
(Cand. 1) and the hierarchy problem.

The α problem reduces to: **what determines the toroidal
embedding of the compact space in 3+1D?**


### F15. What the model already unifies (and what it doesn't)

The model achieves conceptual unification: all particles are
photon configurations on compact geometry.  Mass, charge, spin,
magnetic moment are emergent from energy + topology.

The emergent-gravity picture is consistent with GR but not
derived from it:
- The photon has energy → confined momentum = mass
- Mass curves spacetime (GR) → every electron creates gravity
- This gravity is real, measurable, and exactly what GR predicts
- But this gravity is ~10⁴⁵× too weak to produce the compact
  curvature needed for charge

Three levels of unification:

| Level | Claim | Status |
|-------|-------|--------|
| Conceptual | All particles = photons on geometry | YES |
| Framework | 7D metric → gravity + EM | Partial (KK structure exists, not derived) |
| Dynamical | Both forces from one equation, one coupling | NO (hierarchy problem unsolved) |

To claim a true unification theory, the model needs Level 2:
the 7D metric must produce both the gravitational and EM
fields from a single geometric object.  The missing piece is
what determines the T³ geometry.  If the geometry is derived
(e.g., as the unique self-consistent solution of 7D Einstein
equations), that's unification.  If it's an input, it's a
framework.


### F16. The key unknown

What determines the toroidal embedding geometry?  Candidates:
- Gravitational self-consistency (confined energy curves space)
- Casimir energy of the compact space (may have a minimum)
- Topological stability constraint on winding modes
- Energy minimization (photon + field total energy)

The α problem = the embedding problem.


### F17. Both forces as photon-photon interactions

A clarifying observation: both gravity and EM can be understood as
photon-photon interactions, distinguished by what property of the
photon they couple to.

**Gravity** comes from the photon's energy.  Two photons
gravitationally attract (a GR result, not Newtonian).  Anti-parallel
photons attract with effective mass 2E/c² (Tolman-Ehrenfest-Podolsky);
co-propagating photons have zero gravitational interaction (exact
pp-wave result).  The interaction is always attractive or zero, never
repulsive — because energy is always positive.  This IS gravity.

**Electromagnetism** comes from the photon's winding direction on the
compact space.  A free photon has no net charge (linear Maxwell: no
photon-photon EM interaction).  But a confined photon with winding +q
produces a time-averaged field pattern that looks like positive charge;
winding −q looks like negative charge.  Two confined photons with
same-sign winding repel; opposite-sign attract.  The sign of the
interaction is purely topological.

| Force | Couples to     | Source         | Sign         |
|-------|----------------|----------------|--------------|
| Gravity | Energy (T_μν) | Always positive | Universal +  |
| EM      | Winding (topology) | ±q         | Sign-carrying |

Gravity = force between energies.
Electromagnetism = force between topologies.

This is arguably the sharpest expression of the guiding principle
"energy and geometry are the only fundamentals" at the force level.


---

## Track 3: Charge from the embedding

**Script:** [`scripts/track3_charge_from_embedding.py`](scripts/track3_charge_from_embedding.py)

### F18. The multi-winding model breaks WvM's charge mechanism

WvM's charge mechanism relies on **commensurability**: the
circular polarization rotates E by one full cycle per
wavelength, and the tube winding (p = 1) rotates the local
frame by one full cycle per wavelength.  These match, so E
always points radially outward — producing a net monopole.

For the multi-winding (68, 137) electron:

    E rotation (circular pol.):    1 cycle per wavelength
    Frame rotation (tube winding): 68 cycles per wavelength
    Relative rotation:             67 cycles → E oscillates

The polarization twist is no longer commensurate with the
tube winding.  The E-field's normal component oscillates 67
times over the full path, and its integral is zero.

More precisely, the normal component at each point on the
embedded torus surface is:

    E_n(θ, φ) = E₀ cos(pθ + qφ)

The monopole moment (total charge) is proportional to:

    Q ∝ ∫₀²π ∫₀²π cos(pθ + qφ) · (R + a cos θ) dθ dφ

Since q ≥ 1:  ∫₀²π cos(qφ) dφ = 0.

**Therefore Q = 0, exactly, for any (p, q) with q ≥ 1 and
any torus geometry (R, a).**

This is not a methodological error — it reflects a real
physical difference between (1, 2) and (68, 137):

| Property       | WvM (1, 2)      | Multi-winding (68, 137) |
|---------------|-----------------|--------------------------|
| Tube windings  | 1               | 68                       |
| Pol. rotation  | 1 cycle         | 1 cycle                  |
| Commensurability | YES (1 = 1)  | NO (68 ≠ 1)             |
| E_n            | Constant (outward) | Oscillates 67×        |
| Monopole       | Nonzero         | Zero                     |

Numerical verification at 200×200 grid: |integral|/area < 10⁻¹⁶.


### F19. Geometric phase correction also gives zero

The torus embedding rotates the surface normal by 2π per
tube circuit (one θ revolution).  Over the full (p, q)
geodesic, the frame rotates p times.  The effective normal
component with this geometric phase correction:

    E_n^eff(θ, φ) = E₀ cos((p−1)θ + qφ)

The φ integral is still ∫cos(qφ)dφ = 0 for q ≥ 1.

**The geometric phase changes the θ structure but cannot
affect the φ integral.  Q = 0 regardless of p.**


### F20. Fourier analysis of the monopole condition

The monopole requires a (0, 0) Fourier component of the
integrand.  The area element (R + a cos θ) introduces
cos(θ) coupling, which shifts the θ mode number by ±1:

    cos(mθ + nφ) × (R + a cos θ)
      = R cos(mθ + nφ)
      + (a/2) cos((m+1)θ + nφ)
      + (a/2) cos((m−1)θ + nφ)

A (0, 0) component requires n = 0.  Since n = q ≥ 1 in
all physical cases, **no torus-knot winding produces a
monopole from a uniform-amplitude wave.**

Amplitude modulation in θ alone (e.g., E₀ ∝ 1/(R + a cos θ))
cannot help either: it introduces θ harmonics but cannot
create a φ = 0 component.  The φ integral of cos(qφ) is
zero regardless of what multiplies it, as long as the
multiplier has no φ dependence.


### F21. The multi-winding charge problem

R8 computed the (68, 137) electron geometry by assuming
charge e as input — it placed charge e on the torus surface
and found the geometry where the Coulomb self-energy equals
m_e c²/2.  It did not derive charge from the field.

Track 3 now shows that the WvM mechanism (E always outward)
does NOT apply to the (68, 137) knot.  Moving from (1, 2)
to (68, 137) solved the mass/size problem (R ≈ r_e instead
of R ≈ λ_C/4π) but broke the charge mechanism (p went
from 1 to 68, destroying commensurability).

| Gain from multi-winding | Loss from multi-winding |
|-------------------------|-------------------------|
| Correct torus size (R ≈ r_e) | Commensurability (p = 1 → 68) |
| Coulomb energy matches mass  | WvM charge mechanism broken |
| Spin ½ preserved             | Charge must come from elsewhere |

For charge to emerge from the (68, 137) configuration,
the field distribution must be non-uniform on the torus —
the embedding must affect the field amplitude, not just
its direction.  This is a fundamentally different mechanism
from WvM's commensurability argument.


### F22. Three paths to non-uniform amplitude

For charge to emerge, the field must have a non-trivial
amplitude profile that breaks the φ-averaging to zero.
Three mechanisms could produce this:

**Path A — Mode mixing on the embedded torus.**
The curved-torus wave equation couples the (p, q) mode to
other Fourier modes, including (0, 0).  The (0, 0) mode IS
the monopole = charge.  The coupling strength is determined
by the embedding curvature (the (1 + r cos θ) factor in the
metric).  This is a perturbation theory problem: treat the
embedded metric as the flat metric plus a curvature
perturbation, and compute the (0,0) amplitude induced by
the (p, q) source.

**Path B — Boundary-value problem.**
WvM's charge calculation treats the photon as confined to a
torus-shaped cavity, not as a plane wave on flat T².  Inside
the cavity, the field satisfies Maxwell's equations with
boundary conditions set by the torus surface.  The resulting
field is NOT a plane wave — it has nodes and amplitude
variations imposed by the boundary shape.  This non-uniformity
is what produces the net radial E-field.

**Path C — Self-consistent field modification.**
The photon's own electromagnetic field, when projected into
3D via the embedding, creates a Coulomb-like field that acts
back on the field distribution in the compact space.  This
self-interaction breaks the uniform-amplitude assumption.

All three paths point to the same physics: **the field
distribution on the compact space is shaped by the boundary
(embedding geometry), not just by the flat interior metric.**
The flat-interior picture is correct for the phase (and hence
mass, spin), but the amplitude requires knowledge of the
boundary.

### F23. Connection to prior results

This finding is consistent with all prior work:

- **R8** computed charge by assuming uniform surface charge on
  the embedded torus (not a plane wave) — an implicit
  boundary-value assumption.
- **R12 Track 1** showed no eigenmodes at ω_C on flat T² —
  the photon is not a standing wave on the flat space.
- **R12 F6** noted the photon "fills" the torus (λ ≫ L) — in
  the deep-wave regime, the field is shaped by the boundary,
  not by geometric optics.
- **WvM** used a cavity model (energy confined in a torus
  volume) — inherently a boundary-value approach.

The two-domain picture needs refinement: the photon's PHASE
is set by the flat metric, but its AMPLITUDE PROFILE is set
by the embedding boundary.  This is not a contradiction — it
is how waves behave in bounded geometry (compare: a waveguide
has propagation speed set by the medium, but mode shape set by
the boundary).


## Study conclusion

R13 is **COMPLETE**.

The central result is Track 3's finding that the multi-winding
(68, 137) electron model breaks the WvM charge mechanism.
WvM's charge arises from commensurability: p = 1 tube winding
matches the 1 cycle of circular polarization, so E always
points radially outward.  When R8 shrank the torus to R ≈ r_e
(to fix the Coulomb energy problem from R7), the winding
number jumped to p = 68, destroying this commensurability.

The underlying tension is the smallness of α.  At the Compton
scale, U_Coulomb = α × m_e c² — a factor of ~137 below the
target.  If α were ~1, the (1, 2) torus at Compton scale would
produce correct mass, charge, Coulomb energy, and spin
simultaneously.  The existence of α ≈ 1/137 forces the model
into a dilemma: keep (1, 2) with correct charge but wrong
Coulomb energy, or go multi-winding with correct Coulomb energy
but broken charge mechanism.

**What R13 establishes:**

1. The electron is a winding mode, not a KK momentum mode
2. Charge is a projection property of the embedding
3. The WvM charge mechanism (commensurability) requires p = 1
4. The multi-winding model (p = 68) does not produce charge
5. R8's charge was assumed as input, never derived
6. The α problem is equivalent to the charge mechanism problem

**What remains open:** resolving the charge-vs-Coulomb-energy
tension.  Eight candidate paths are captured in
[`qa/INBOX.md`](../../qa/INBOX.md) (Q34).


## Summary (all tracks)

| Finding | Result |
|---------|--------|
| Electron as KK mode | NO — winding mode, not momentum mode |
| Standard KK charge | Does not apply (zero compact momentum) |
| WvM charge mechanism | Works for (1,2): p = 1 → E always outward |
| Multi-winding charge | BROKEN for (68,137): p = 68 ≠ 1 → E oscillates 67× |
| Monopole integral | ZERO (exact, analytical, any q ≥ 1) |
| Root cause | Commensurability lost when p went from 1 to 68 |
| Underlying tension | α ≈ 1/137 forces Coulomb energy vs charge tradeoff |
| R8 assumption | Used charge e as input — never derived it |
| Both forces | Gravity = energy-energy; EM = topology-topology |


## Scripts

- [`scripts/track1_kk_charge.py`](scripts/track1_kk_charge.py)
  — KK mode spectrum, geodesic wave analysis, winding vs
  momentum identification
- [`scripts/track2_charge_mechanisms.py`](scripts/track2_charge_mechanisms.py)
  — Four charge mechanisms: curvature, gauge connection,
  topological, cross-terms
- [`scripts/track3_charge_from_embedding.py`](scripts/track3_charge_from_embedding.py)
  — Monopole integral of embedded plane wave: analytical proof
  of zero charge, Fourier analysis, paths forward
