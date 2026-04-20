# Derivation 7b — Spin from field polarization on the 2-torus

**Program 1, Track 7 (alternative to 7a).**  Derive the spin
of a standing-wave photon mode on a 2-torus from the rotation
of its circularly polarized (CP) electric field vector
relative to the laboratory frame.  The result is that the spin
quantum number is

$$
s \;=\; \frac{n_t}{n_r}
$$

where n_t is the tube winding number and n_r is the ring
winding number.  This follows the Williamson–van der Mark
(1997) approach, adapted here to the standing-wave setting
of derivations 1–6.

**A note on competing approaches.**  Derivation 7a attempted
to derive spin from the metric structure of the 2-torus
(Killing vectors, holonomy) and found that the flat T² metric
cannot produce spin-½ by those mechanisms.  That result is
mathematically correct but may be asking the wrong question:
MaSt's particles are CP-polarized photon modes, not scalar
fields, and the spin may reside in the field's polarization
rather than in the manifold's metric structure.

This derivation takes the field-polarization approach.  It
arrives at a definite answer (s = n_t/n_r) that differs from
the parity rule currently used in the codebase.  However, the
WvM model is a single-particle picture — it treats the photon
as a classical entity circulating on the torus — and a true
standing wave may have subtleties that modify the classical
rotation-counting argument.  This derivation presents its case
and states its conclusions, while recognizing that a complete
treatment (e.g., from the full vector wave equation on the
torus, or from the multi-sheet T⁶ structure) could refine or
revise the result.

---

## Inputs

1. **F2** (derivation-1 B.5): a photon orbiting a 1D ring of
   circumference L has quantized angular momentum L_z = nℏ
   about the ring axis.  The angular momentum is constant in
   time (independent of the photon's position on the ring).

2. **F7** (derivation-3): a photon on a 2-torus with winding
   numbers (n_t, n_r) has 4D rest mass m²c² = h^ab P_a P_b.

3. **The CP polarization structure** (R48 Track 1, F1–F5;
   charge-from-energy primer §4; GRID fields.md): the photon
   on the torus is circularly polarized.  Its electric field
   vector E rotates in the plane perpendicular to the direction
   of propagation at rate ω = 2πf, where f is the photon's
   frequency.  On a torus, the propagation direction is
   tangent to the surface, so E rotates in the plane formed
   by the surface normal and the perpendicular tangent
   direction.

4. **Special relativity** (Lorentz invariance, angular momentum
   as a conserved quantity).

5. **The Planck–Einstein relation** E = hf (already used in F1
   and F7; no new quantum input).

No Killing vectors, no holonomy, no spinor representations.
The derivation uses only the geometry of a rotating vector on
a doubly-periodic surface.

---

## Section A — Angular momentum of a CP wave on a ring (recap)

### A.1 — The single-ring case

> *Purpose: recall F2 in the form needed here, and introduce
> the concept of "rotations per circuit."*

From derivation-1 Part B: a photon orbiting a 1D ring of
circumference L completes one circuit in time T = L/c.  Its
angular momentum about the ring axis is

$$
L_z \;=\; n\,\hbar, \qquad n \in \mathbb{Z}^+,
$$

where n is the standing-wave mode number (the number of
wavelengths fitting around the ring: L = nλ).

The E-field vector of a CP photon rotates once (2π radians)
per wavelength of propagation.  In one complete circuit of
the ring, the photon traverses n wavelengths, so E rotates
through

$$
\Delta\phi_{\text{ring}} \;=\; n \times 2\pi
\;=\; 2\pi n.
$$

The number of **full rotations** of E per ring circuit is n.
This is also the angular momentum quantum number.  On a
single ring, the spin is always an integer: s = n.

### A.2 — Why the rotation count gives the spin

> *Purpose: connect the E-vector rotation count to the
> standard definition of spin.*

A spin-s object requires a rotation of 2π/s to return to its
original orientation (more precisely: the wavefunction acquires
a phase e^{i 2π s} under a 2π spatial rotation, which equals
+1 for integer s and −1 for half-integer s).

Equivalently: if an object's internal structure completes
exactly s full rotations during one 2π circuit of the ring,
the object has spin s.  For the single-ring photon, the CP
field completes n rotations per circuit → spin = n (integer).

The key observation: on a 2-torus, the "circuit" that defines
the particle's spatial rotation is the **ring circuit** (the
large loop that the external observer sees as the particle's
orbital motion).  The tube circuit is internal.  The number of
E-field rotations per RING circuit determines the spin — and
this number need not be an integer, because the tube winding
introduces a sub-harmonic.

---

## Section B — The 2-torus: two competing periods

### B.1 — Geometric setup

> *Purpose: define the two circuits and their relationship.*

The 2-torus has two independent closed loops:

- The **ring** (circumference L_r = 2πR): the large loop
  visible to the external observer.  One ring circuit = 2π
  rotation of the particle's position in the lab frame.
- The **tube** (circumference L_t = 2πa): the small loop
  internal to the particle.  The tube circuit is not directly
  visible as spatial rotation — it is internal structure.

A (n_t, n_r) mode has n_t windings around the tube for every
n_r windings around the ring.  The photon's path on the torus
is a helix that wraps n_t times in the tube direction while
wrapping n_r times in the ring direction before closing.

### B.2 — How many tube circuits per ring circuit?

> *Purpose: compute the fraction of a tube circuit completed
> per ring circuit.*

One complete ring circuit corresponds to Δθ_ring = 2π (one
full trip around the large loop).  During this ring circuit,
the photon advances in the tube direction by

$$
\Delta\theta_{\text{tube per ring circuit}}
\;=\; \frac{n_t}{n_r} \times 2\pi.
$$

This is because the photon's path has slope n_t/n_r on the
(θ_tube, θ_ring) coordinate plane: for every n_r ring
windings, there are n_t tube windings.  Per single ring
circuit (Δθ_ring = 2π), the tube advances by
(n_t/n_r) × 2π.

When n_t/n_r is an integer (e.g., n_t = 2, n_r = 1), the
tube completes a whole number of circuits per ring circuit.
When n_t/n_r is a fraction (e.g., n_t = 1, n_r = 2), the
tube completes only a FRACTION of a circuit per ring circuit.
The path does not close after one ring circuit — it takes n_r
ring circuits for the path to return to its starting point.

### B.3 — The E-field rotation per ring circuit

> *Purpose: this is the central calculation.*

The CP photon's E-field vector rotates at a rate locked to the
photon's propagation.  On the torus, the photon propagates
along BOTH the tube and ring directions simultaneously.  The
E-vector rotation has two components:

1. **Ring contribution:** the ring curvature (the fact that the
   ring is a circle in 3D space) causes the photon's
   propagation direction to rotate by 2π per ring circuit.
   The E-vector, being perpendicular to the propagation
   direction, co-rotates.  This contributes one full rotation
   (2π) per ring circuit — the same as the single-ring case.

2. **Tube contribution:** the tube is ALSO circular.  The
   photon's propagation along the tube causes the E-vector to
   rotate in the tube plane.  Per ring circuit, the tube
   advances by (n_t/n_r) × 2π (from B.2).  Each 2π of tube
   advance contributes one full E-vector rotation in the tube
   plane.  So the tube contributes n_t/n_r rotations per ring
   circuit.

But these two rotations are in DIFFERENT planes (ring plane vs
tube plane).  The net rotation visible to the lab observer
depends on how they compose.  The key geometric fact: the tube
rotation is in the plane perpendicular to the ring — it is the
**internal** rotation of the field, while the ring rotation is
the **orbital** rotation around the lab axis.

The orbital angular momentum (from the ring) is L_orbital =
n_r ℏ per ring circuit — this is the extrinsic orbital
motion, identical to a point particle orbiting at radius R.

The **intrinsic** angular momentum — what we call spin — is
the tube rotation as seen from the lab frame.  Per ring
circuit, the tube contributes n_t/n_r rotations of the
E-vector in the internal plane.  The angular momentum from
this internal rotation is:

$$
\boxed{\;s \;=\; \frac{n_t}{n_r}\;}
$$

This is the **spin quantum number** of the (n_t, n_r) mode.

### B.4 — Why n_t/n_r and not n_t

> *Purpose: address the subtlety that distinguishes the ratio
> from the tube number alone.*

One might ask: why isn't the spin just n_t (the total tube
winding)?  After all, the tube winding determines how many
times the E-field rotates in the tube plane over the entire
closed path.

The answer: spin is defined per **one spatial rotation** (one
ring circuit = 2π), not per the entire closed path.  The
entire path has n_r ring circuits and n_t tube circuits.  The
total E-vector rotation in the tube plane over the entire path
is n_t × 2π.  But the number of spatial rotations is n_r.  So
the rotation per spatial rotation is:

$$
\frac{n_t \times 2\pi}{n_r \times 2\pi} \;=\; \frac{n_t}{n_r}.
$$

This distinction matters precisely when n_r > 1.  For (1,1)
modes: s = 1/1 = 1 (spin 1).  For (1,2) modes: s = 1/2
(spin ½).  For (2,4) modes: s = 2/4 = 1/2 (spin ½ — same
ratio, higher harmonics).  For (1,3) modes: s = 1/3 (not a
standard spin value — see Section D).

---

## Section C — Verification against known cases

### C.1 — The electron: (1,2) → spin ½

The electron mode on the e-sheet has n_t = 1, n_r = 2.

$$
s \;=\; \frac{1}{2}.
$$

The photon goes around the tube once while going around the
ring twice.  After one ring circuit (one 2π spatial rotation),
the E-vector has rotated by only π (half a turn) in the tube
plane.  After TWO ring circuits (720° spatial rotation), the
E-vector returns to its starting orientation.  This 720°
requirement is the defining property of spin ½ — the Dirac
belt trick, the Möbius-strip-like double covering of SO(3).

This matches Williamson and van der Mark's original (1997)
derivation exactly.  They identified the (1,2) topology as
the reason the electron requires 720° rotation, and connected
this to spin ½ through the same rotation-counting argument.

### C.2 — The photon: (0,0) → spin 1

A free 4D photon has no compact winding: n_t = 0, n_r = 0.
The ratio 0/0 is undefined, but the photon is known to have
spin 1 from its vector nature (it is a 1-form on spacetime,
as derived in D7a §C for the (0,0) sector of the KK
reduction).  The spin = n_t/n_r formula applies to CONFINED
photons with both n_t ≠ 0 and n_r ≠ 0.  The free photon is
the n_t = n_r = 0 case where the formula doesn't apply and
spin is determined instead by the field's Lorentz
representation (spin 1 for a vector field).

### C.3 — Spin-1 modes: (n, n) → spin 1

Any mode with n_t = n_r = n has s = n/n = 1.  These are
spin-1 massive particles — the KK tower of massive vector
bosons.  This matches the spin-1 result derived in D7a §C
from the 1-form KK reduction.

### C.4 — Higher harmonics preserve spin

Modes proportional to the electron — (2,4), (3,6), (4,8), ...
— all have s = 1/2.  They are excited states of the same
spin-½ topology.  The spin is a property of the RATIO, not
of the individual winding numbers.

---

## Section D — Allowed and forbidden spin values

### D.1 — Which spins are possible?

The spin s = n_t/n_r is a rational number (ratio of two
integers).  The possible values are:

| n_t/n_r | s | Classification |
|---------|---|---------------|
| 0/n_r | 0 | Scalar (no tube winding) |
| 1/1 | 1 | Vector boson |
| 1/2 | 1/2 | Fermion (electron-like) |
| 1/3 | 1/3 | Not a standard particle spin |
| 1/4 | 1/4 | Not standard |
| 2/3 | 2/3 | Not standard |
| 3/2 | 3/2 | Fermion (Δ-baryon-like) |
| 2/1 | 2 | Tensor (graviton-like) |

Standard physics allows only integer and half-integer spins
(from the representation theory of the rotation group SO(3)
and its double cover SU(2)).  The ratio rule allows arbitrary
rational spins.  This means:

- **Modes with s = integer or half-integer** are physically
  allowed: (1,2), (1,1), (2,4), (3,6), (2,1), (3,2), etc.
- **Modes with other rational s** (like 1/3, 2/3, 1/4) are
  geometrically possible on the torus but correspond to no
  known particle.  These modes exist as standing waves but may
  be unstable, unobservable, or excluded by additional
  physics (e.g., they might not couple consistently to 4D
  Lorentz symmetry).

### D.2 — Implication for the proton

The proton has spin ½.  If the ratio rule holds, the proton
mode must satisfy n_t/n_r = 1/2.  On the proton sheet, viable
candidates would include:

- **(1,2):** the simplest.  Same ratio as the electron,
  different sheet (different ε_p, s_p → different mass).
- **(3,6):** the first harmonic.  Same ratio, higher energy.
  This was identified in R46 as a viable proton candidate with
  gcd(3,6) = 3, decomposable into three (1,2) sub-strands.

The mode **(1,3)**, which model-E currently uses for the
proton, has s = 1/3 under the ratio rule — not spin ½.
If the ratio rule is correct, (1,3) would not be a valid
proton mode.  However, this conclusion depends on the ratio
rule being the complete story for standing waves on the
torus; see Section E for the history, the competing rules,
and the implications.

---

## Section E — The spin problem: competing rules and their history

### E.1 — The original WvM rule (1997–R47)

Williamson and van der Mark (1997) derived spin ½ for the
electron from the (1,2) topology: one tube winding per two
ring windings requires 720° rotation to return the field
orientation.  The spin quantum number is the ratio n_t/n_r.

This rule was used throughout MaSt studies R1–R47.  The
electron was assigned mode (1,2) with spin = 1/2 = n_t/n_r.
The proton was explored as both (1,2) and (3,6), both of
which give spin ½ by the ratio rule.

### E.2 — The pivot (R47–R50)

Between R47 and R50, the proton mode assignment was changed
to (1,3).  This was motivated by the nuclear charge formula
Q = −n₁ + n₅: with the proton as (1,3), the charge is
Q = 0 + 1 = +1 (using the convention that proton-sheet tube
is index 5).  The (1,3) assignment also gave a better fit to
the neutron mass through cross-sheet shears.

However, (1,3) has ratio 1/3, which is not spin ½.  To
rescue the proton's spin, a new rule was introduced:

> **Parity rule (R50):** odd tube winding → spin ½;
> even tube winding → spin 0 or 1.

This rule was asserted in R50 without formal derivation and
attributed to "topological" considerations.  R47's review
document explicitly states: "Model-D established that physical
spin is topological: odd tube winding → spin ½.  The WvM
ratio formula has been superseded."

### E.3 — The parity rule's consequences

The parity rule was implemented in the `spin_half_count`
function (lib/metric.py) and used throughout R50–R62:

```python
def spin_half_count(n):
    return sum(1 for i in (0, 2, 4) if abs(n[i]) % 2 == 1)
```

This counts odd tube windings across all three sheets.  It
was used to classify the 18/20 particle inventory in model-E
and to validate compound modes in R54.

The parity rule gives different answers from the ratio rule
for many modes:

| Mode | WvM ratio s = n_t/n_r | Parity rule |
|------|----------------------|-------------|
| (1,2) | 1/2 ✓ | 1/2 ✓ (n_t odd) |
| (1,3) | 1/3 ✗ | 1/2 ✓ (n_t odd) |
| (2,4) | 1/2 ✓ | 0 ✗ (n_t even) |
| (3,6) | 1/2 ✓ | 1/2 ✓ (n_t odd) |

The two rules agree on (1,2) and (3,6) but disagree on
(1,3) and (2,4).  The parity rule was introduced specifically
to make (1,3) viable as a spin-½ proton — but in doing so,
it broke (2,4), which should be spin ½ (it's proportional to
the electron mode).

### E.4 — R62 derivation 7a: the metric approach

Derivation 7a (the predecessor of this file) attempted to
derive spin-½ from the metric structure of the flat 2-torus
using Killing vectors and holonomy.  It correctly showed that
neither mechanism works on a flat T² — the Killing algebra
is abelian and the holonomy is trivial.

Derivation 7a's conclusion is mathematically sound: the
flat-torus METRIC alone cannot produce spin-½.  But this
leaves open whether the FIELD on the torus can.  A CP-
polarized electromagnetic wave has structure (polarization
direction, rotation rate) that goes beyond what a scalar
field on the same manifold has.  Derivation 7b (this file)
explores that field-based route.

### E.5 — The ratio rule: spin = n_t/n_r

The derivation in Sections A–D of this file recovers the WvM
ratio rule from the CP field's rotation rate on the 2-torus.
The spin quantum number under this approach is

$$
s \;=\; \frac{n_t}{n_r},
$$

which is a half-integer for the electron (1,2) and for all
modes proportional to (1,2): the (2,4), (3,6), (4,8), ...
tower.

This rule is derived from the same CP polarization structure
that D5 and R48 used for charge.  It does not require Killing
vectors, holonomy, or any structure beyond the geometry of a
rotating vector on a doubly-periodic surface.

**Caveat:** the rotation-counting argument treats the photon
as a classical circulating entity.  A true standing wave on
the torus is a superposition of clockwise and counterclockwise
modes, and the spin of such a superposition may have
subtleties not captured by the single-particle rotation
count.  Whether the ratio rule holds exactly for standing
waves, or whether corrections arise from the wave structure,
is an open question that a full vector-wave-equation treatment
could address.

### E.6 — Documents and studies potentially affected

If the ratio rule is adopted in place of the parity rule, the
following documents would need review.  This list is provided
for reference; the decision on whether to adopt the ratio rule
project-wide is separate from this derivation.

| Document | How affected |
|----------|-------------|
| **model-E.md** | Particle inventory uses `spin_half_count` for spin assignments.  Proton at (1,3) has s=1/3 by ratio rule. |
| **lib/metric.py** | `spin_half_count` function implements parity rule.  Needs replacement with ratio function. |
| **R50 (filtered mode search)** | Introduced the parity rule.  Mode assignments may change. |
| **R54 (compound modes)** | Used `spin_half_count` for the 18/20 inventory.  Some spin assignments change. |
| **R47 (proton filter)** | Compared (1,2) and (3,6) proton candidates — both valid under ratio rule.  The (1,3) candidate is invalidated. |
| **R53 (three generations)** | Generation structure depends on the reference mode.  If proton is (1,2) instead of (1,3), s_p changes. |
| **Taxonomy.md** | §4.2 defines spin via parity rule.  Needs update to ratio rule. |
| **papers/white-paper.md** | References model-E inventory including (1,3) proton. |
| **papers/matter-from-light.md** | Describes spin mechanism.  Needs update. |
| **derivation-7a.md** | Superseded by this file. |

### E.7 — The proton mode question (open)

If the ratio rule holds and the proton is not (1,3), what
would it be?  The proton must have s = 1/2, requiring
n_t/n_r = 1/2.  Candidates explored earlier in the project:

- **(1,2) on the p-sheet:** same ratio as the electron.
  Different mass because the p-sheet has different (ε_p, s_p).
  Simplest option.  R47 explored this extensively.
- **(3,6) on the p-sheet:** first harmonic of (1,2).
  gcd(3,6) = 3, so the mode decomposes into three (1,2)
  sub-strands — the quark picture (R48 F6).  Each sub-strand
  individually carries charge (n_t = 1 satisfies the CP
  synchronization rule).  Total charge = 3 × e/3 = e.

The choice between (1,2), (3,6), or retaining (1,3) under a
revised understanding of spin, is outside the scope of this
derivation.  What the ratio rule establishes, if correct, is
a **constraint**: the proton mode should satisfy n_t/n_r = 1/2.
Whether this constraint holds for actual standing waves on the
proton sheet is the question to resolve.

---

## Lemma (Track 7b result)

We have shown:

> **(F20) Spin from CP field rotation.**  A circularly
> polarized photon on a (n_t, n_r) 2-torus has its E-field
> vector completing n_t/n_r full rotations in the tube plane
> per ring circuit (one 2π spatial rotation).  The spin
> quantum number is therefore
>
> $$
> s \;=\; \frac{n_t}{n_r}.
> $$
>
> This is the Williamson–van der Mark (1997) ratio rule,
> derived from the CP polarization structure already
> established in R48 and derivation-5.  The derivation uses
> no Killing vectors, no holonomy, and no spinor
> representations — only the geometry of a rotating vector
> on a doubly-periodic surface.
>
> **(F21) Spin-½ requires n_t/n_r = 1/2.**  The electron
> mode (1,2) has spin ½.  All modes proportional to (1,2) —
> including (2,4), (3,6), (4,8), ... — also have spin ½.
> Mode (1,3) has spin 1/3 and is NOT spin ½.
>
> **(F22) The parity rule and the ratio rule disagree.**
> The empirical rule "odd tube winding → spin ½" (introduced
> in R50, implemented as `spin_half_count` in the codebase)
> and the ratio rule s = n_t/n_r give different answers for
> modes like (1,3) (parity → ½, ratio → 1/3) and (2,4)
> (parity → 0, ratio → ½).  Neither rule has been derived
> from a full vector wave equation on the torus.  This
> derivation argues for the ratio rule on physical grounds
> (CP field rotation counting) and on historical grounds
> (alignment with WvM's original framework).  The parity
> rule was introduced without formal derivation to
> accommodate a specific proton mode assignment.  Resolution
> requires either a definitive wave-equation calculation or
> experimental discrimination between the competing mode
> assignments.

F20–F22 present the ratio rule's case for the spin portion
of the "electron from light" program.  If adopted, the
single-sheet electron has all four classical quantum numbers
— mass (F7), charge (F14), Lorentz force (F17), and spin
(F20) — derived from the same 6D null trajectory.  The
magnetic moment (gated by spin) would be the remaining item.
If the parity rule is retained instead, derivation 7a's
negative result stands and spin-½ remains an empirical
postulate awaiting a different derivation mechanism.
