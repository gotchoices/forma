# Q51. Non-torus embeddings and the mode-coupling route to α

**Status:** open — → R17 (radiation pressure self-consistency)
**Source:** R15 F7 candidate 5, user question, dipole radiation
pattern observation, centrifugal force analysis
**Connects to:** Q34 Paths 4 and 8, R15, R16, R17, Q48, Q52

---

## The idea

The material space (flat Ma_e) can be embedded in 3D as shapes
other than a standard torus.  A perfect torus has rotational
symmetry around its central axis, which forces the angular
mode number to be conserved — an n = 2 wave can never produce
the n = 0 component needed for net charge (R15 F3).

But other embeddings of the same flat Ma_e break this symmetry:
- **Elliptical torus** — tube cross-section is an ellipse
- **D-shaped cross-section** — like a tokamak
- **Knotted ring** — the tube tied in a knot (trefoil, etc.)
- **Asymmetric deformation** — any smooth deformation that
  removes the rotational symmetry

On any of these shapes, the angular mode number is NOT
conserved.  The 3D field equations couple n = 2 directly to
n = 0, producing net charge without needing the photon to be
localized as a wavepacket.  The coupling strength depends on
the geometry of the deformation.

If α = (coupling coefficient from n = 2 to n = 0), then α
is determined by the embedding shape.  This could be computed
from the overlap integrals of the deformed geometry.

## Questions

- What is the simplest deformation that gives nonzero coupling?
- Does the coupling coefficient have a nice form?
- Can we recover α ≈ 1/137 from a specific deformation?
- Is the deformation determined by something physical (e.g.,
  the photon's own field backreacting on the embedding)?

## Key lead: the dipole radiation pattern

A circularly polarized wave (which is what WvM uses) has a
non-isotropic radiation pattern in 3D: intensity
∝ (1 + cos²θ)/2.  If the photon's field leaks from the
material space into 3D with this pattern, and if the field
energy shapes the tube cross-section (self-consistency), then
the tube is NOT circular — it is elongated or D-shaped,
determined by Maxwell's equations.  This chain:

    CP wave → non-isotropic radiation → non-circular tube
    → broken symmetry → n=2 couples to n=0 → charge
    → α = coupling strength = f(deformation)
    → deformation from Maxwell → α derived

would give α from Maxwell's equations and topology alone,
with no free parameters.  The deformation shape is not
arbitrary — it IS the dipole radiation pattern, which is
fundamental.

This may be the most direct path to deriving α: not "what
localizes the photon" but "what shape is the embedding,
given that the photon's own radiation pattern is
non-isotropic."

## Dimensional assignment (see also Q52)

The assignment of which flat-Ma_e dimension becomes the tube (a)
vs. the ring (R) is forced by physics: the WvM charge
mechanism requires p = 1 in the tube (where the surface
normal rotates).  This means L₁ → tube, L₂ → ring, and
the two directions are physically distinct.  If a second
constraint fixes the aspect ratio r = a/R (e.g., equal
distance per winding → r = 1/2, or the radiation pattern
determining the tube shape), the entire geometry is fixed
with zero free parameters.

## Centrifugal radiation pressure

The dipole radiation pattern is one source of tube deformation,
but there is a more fundamental one: the photon has momentum
(p = E/c), and on the curved (1,2) helix, centrifugal force
pushes the field outward from the center of curvature.  The
radiation pressure on the tube wall is stronger at the inner
equator (tighter curvature, R − a from ring center) and weaker
at the outer equator (R + a).  This non-uniform pressure
deforms the tube cross-section even on a perfect torus —
no external asymmetry is needed.

Both effects (centrifugal pressure + dipole radiation pattern)
contribute to the deformation and may reinforce each other.
→ **R17** [`studies/R17-radiation-pressure/`](../studies/R17-radiation-pressure/).
