# R36 findings — Geometric tilt


## Definitions

**Gauge field (gauge potential):** A field that mediates a
force.  The electromagnetic potential A is the classic
example.  In KK theory, the gauge potential arises from
off-diagonal metric components between compact and non-
compact dimensions (g_{xa}).  The electric and magnetic
fields are derivatives of A — they measure how A changes
from place to place.  If A is constant everywhere, the
electric and magnetic fields are zero, and there is no force.

**Field strength:** F = dA, i.e. how much the gauge potential
varies in space and time.  A constant A has F = 0 (no force).
A varying A has F ≠ 0 (force exists).  In electromagnetism,
F is the electric and magnetic field.

**Wilson line:** On a compact (periodic) space, a constant
gauge potential cannot be removed by a coordinate change.
It is physically real — it shifts the allowed momenta of
modes.  But it still has F = 0: it shifts everything equally,
so nothing pushes on anything else.

**Within-plane shear (s):** A deformation of the T² lattice
that tilts one compact axis relative to the other compact
axis on the same sheet.  It changes the SHAPE of the torus.
An un-sheared T² is a rectangle (with opposite sides glued).
A sheared T² is a parallelogram.

**R-T tilt (θ):** A rotation of the T² as a whole relative
to R³.  It does not change the T² shape — it changes its
ORIENTATION in the full 10D space.

**Inter-sheet shear (σ):** A shear between compact axes on
DIFFERENT T² sheets (e.g., between the electron and proton
planes).  Controls whether modes can have quantum numbers
on both sheets simultaneously (e.g., the neutron).


---

## Track 1 — Tilt-angle formalism and mode projection


### F1. Tilt preserves the mass spectrum exactly

On a tilted T² × R¹ (tilt angle θ between the z₁ axis
and R), the rest mass of every mode at its energy minimum
is identical to the un-tilted case:

    m² = (2πn₁/L₁)² + (2πn₂/L₂)²

The tilt is a rotation of the T² in the embedding space.
It cannot change the T²'s intrinsic geometry, so mode
energies are unchanged.  This holds for ALL θ, not just
small θ.  Mass spectrum preservation is automatic.


### F2. The R-projection is a momentum shift, not a coupling

Each mode (n₁, n₂) on the tilted T² acquires a spatial
momentum:

    k₀ = (2πn₁ sinθ) / L₁

This is the "R-projection of compact momentum."

If both T² axes are tilted (by θ₁ and θ₂):

    k₀ = (2πn₁ sinθ₁)/L₁ + (2πn₂ sinθ₂)/L₂

This k₀ shifts every mode's momentum by the same rule.
It does NOT cause modes to push or pull on each other.
Two electrons on a tilted T² both get the same k₀ shift
— their relative motion is unaffected.


### F3. The tilt is equivalent to a constant gauge potential

When you rewrite the tilted metric in standard coordinates,
the tilt appears as an off-diagonal metric term g_{x,φ₁}
between R and T.  This IS a gauge potential (in KK
language), but it is CONSTANT — the same everywhere.

A constant gauge potential has zero field strength: the
electric and magnetic fields are both zero.  There is no
force.  The potential shifts all momenta uniformly, like
a steady wind that pushes everything the same direction —
nothing moves relative to anything else.

On a compact space, this constant potential is called a
Wilson line.  It is physically real (it shifts the allowed
momenta) but still produces no interaction.


### F4. No interaction without spatially varying tilt

A uniform tilt shifts momenta but produces no force.
Two modes on a uniformly tilted T² do not interact
electromagnetically.

For modes to exert forces on each other, the tilt must
VARY from place to place: θ(x) ≠ const.  A spatially
varying potential A(x) produces nonzero field strength
F = dA ≠ 0 — an actual electric/magnetic field.

But a spatially varying metric cross-term that propagates
through space IS a dynamical gauge field.  This is
exactly what KK theory describes.

**Bottom line:** to get electromagnetic interactions from
geometry, you need the R-T metric cross-terms to fluctuate.
Those fluctuations are gauge fields.  KK is the name for
this mathematical fact.


### F5. Ghost mode suppression is absent in the tilt picture

In the tilt picture, charge is a simple linear function
of winding numbers:

    Q ∝ n₁ sinθ₁ + n₂ sinθ₂ × (L₁/L₂)

Every mode with any nonzero winding is charged.  There
are no cancellations.  Modes like (3,2) have Q/Q_e ≈ 1.1,
and (2,4) has Q/Q_e = 2.0.

In the within-plane shear picture (KK), charge arises
from an integral over the mode's wavefunction on the
DEFORMED T².  On a sheared parallelogram, some
wavefunctions have net asymmetry (charged) and others
cancel out (neutral).  This is how the shear naturally
suppresses ghost modes — their wavefunctions integrate to
zero on the deformed surface.

The tilt cannot do this because it doesn't deform the T².
It only rotates the T² as a whole, which shifts all modes
equally per unit winding number.


### F6. Shear and tilt are structurally different

| Property | Shear s (T-T) | Tilt θ (T-R) |
|----------|---------------|---------------|
| What it does | Deforms the T² shape | Rotates the T² orientation |
| Metric component | g_{ab} (compact-compact) | g_{xa} (space-compact) |
| Effect on mass | Small shift (O(s)) | None |
| Charge structure | Mode-dependent — some modes neutral | All modes charged |
| Produces interactions | Yes | No (constant → F = 0) |

The shear determines WHICH modes are charged and by how
much.  The tilt determines the background gauge potential,
which shifts momenta but creates no forces.


### F7. Charge requires T² deformation (within-plane shear), not just tilt

This answers the central question of the study.

**With tilt only (θ ≠ 0, s = 0):** Masses preserved.
Modes get a momentum shift proportional to their winding
number.  But no mode interacts with any other mode.  The
"charge" is a label with no physical consequence — there
is no electric field, no Coulomb force.

**With shear only (s ≠ 0, θ = 0):** The T² shape is
deformed from rectangle to parallelogram.  Mode
wavefunctions become asymmetric.  When the wave equation
is solved, some modes naturally couple to the R-T metric
fluctuations (the gauge field) and others don't.  The
modes that couple are "charged."  The coupling strength
is α, determined by sin²(2πs).

**Why does shear produce charge but tilt does not?**

The shear changes what happens INSIDE the T².  On a
rectangle, a wave going around the tube sees the same
geometry regardless of where it is on the ring.  On a
parallelogram, the tube's position shifts as you move
along the ring.  This creates an asymmetry in the mode's
wavefunction that doesn't average to zero — and that
net asymmetry is charge.

The tilt doesn't change anything inside the T².  It only
changes how the T² sits inside the larger space.  Since
the wave equation on the T² is unchanged, the mode
wavefunctions are unchanged, and their charge integrals
are unchanged (zero on an un-sheared T², regardless of
tilt).


### F8. Inter-sheet shear and within-sheet shear are independent

The 6×6 compact metric has two types of shear:

**Within-sheet shears** (s₁₂, s₃₄, s₅₆): deform each T²
individually.  These determine the electromagnetic charge
of modes on each sheet.  The electron and proton sheets
each have their own s, and both are solved to give the
same α = 1/137.

**Inter-sheet shears** (σ_ep, σ_eν, σ_νp): couple axes
on different T² planes.  These determine which modes can
span multiple sheets.  The neutron exists because σ_ep ≠ 0
allows a mode with both electron-sheet and proton-sheet
quantum numbers.

These are separate, independent entries in the metric.
Setting σ_ep ≠ 0 does not force s₁₂ or s₅₆ to be nonzero,
or vice versa.  You could in principle have inter-sheet
coupling (neutron exists) without within-sheet shear
(no electromagnetic charge) — though that would be
physically pathological.

In the actual model: both types are present and serve
different roles.  Within-sheet shear → charge and α.
Inter-sheet shear → particle mixing and the neutron.


### F9. KK is not an external assumption — it emerges from the geometry

KK gauge field theory is not something we chose to bolt
onto the T⁶ model.  It is what the wave equation produces
when you solve it on a space with compact and non-compact
dimensions.

The 10D metric necessarily has components g_{xa} between
R and T dimensions.  These components can be static
(constant gauge potential, no force) or they can fluctuate
in space and time (dynamical gauge field, electromagnetic
force).  The fluctuations propagate at the speed of light
and obey Maxwell's equations.  This is not an assumption
— it is a mathematical consequence of ∇²ψ = 0 on the
full space.

What IS a choice is the value of the within-plane shear s.
This determines α.  Whether s is a free "designer's choice"
or determined by some deeper principle remains the open
question.


### F10. Summary of what each geometric parameter does

| Parameter | Type | Controls | Example |
|-----------|------|----------|---------|
| r (aspect ratio) | T² shape | Mode mass spectrum | r_p = 8.906 → proton mass |
| s (within-plane shear) | T² shape | Electromagnetic charge, α | s_e ≈ 0.010 → α = 1/137 |
| σ (inter-sheet shear) | T²-T² coupling | Multi-sheet modes | σ_ep ≈ −0.091 → neutron |
| θ (R-T tilt) | T²/R³ orientation | Background gauge potential | Shifts momenta, no force |
| L (circumferences) | T² size | Energy scale | L₂ → electron mass |

The mass spectrum depends on r, L, s, and σ.
Electromagnetic coupling depends on s alone.
Inter-sheet mixing depends on σ.
The tilt θ has no effect on either masses or interactions.
