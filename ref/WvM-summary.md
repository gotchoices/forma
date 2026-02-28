# WvM Paper Summary

**Paper:** Williamson, J.G. & van der Mark, M.B., "Is the electron a
photon with toroidal topology?", *Annales de la Fondation Louis de
Broglie*, Vol. 22 No. 2, 1997.

**Full text:** `WvM.pdf` in this folder.

This is a living summary. It records our current understanding of
what the paper claims, what it demonstrates, and where we have
previously misread it. Sections marked ⚠ contain corrections to
earlier interpretations.

---

## Notation

Throughout this project, **(p,q) torus knot** notation means:

| Symbol | Winds around | Axis | Coordinate | Visual test |
|--------|-------------|------|------------|-------------|
| **p** | tube (minor circle) | minor / meridional | θ | Sitting inside the tube, count rotations |
| **q** | ring (major circle) | major / longitudinal | φ | Looking through the hole, count loops |

The WvM electron is **(1,2)**: once around the tube, twice around
the ring. This convention is defined in `studies/knot-zoo/theory.md`
§1 and used consistently across all studies and scripts.

**Caution:** some mathematical references reverse p and q. Our
electron would be called (2,1) in those sources. When reading
external material, always check which convention is in use.

---

## 1. Core claim

A single photon confined to a toroidal topology, with periodic
boundary conditions of one wavelength, reproduces the known
properties of the electron: mass, charge, spin, magnetic moment,
and g-factor. The model is purely electromagnetic — no point
particle, no bare charge. The single postulate is that a
self-confined single-wavelength photon state exists.

## 2. The twisted strip model (§2, Fig. 1)

WvM visualize a single wavelength of a circularly polarised photon
as a **twisted strip of paper** (Fig. 1a):

- The strip's length represents the photon's propagation direction.
- **B is in the plane of the strip** (across the width).
- **E is perpendicular to the strip** (normal to the face).
- The twist represents the rotation of the field vectors — one full
  twist per wavelength corresponds to circular polarisation.

Applying periodic boundary conditions (joining the ends of the
strip so that exactly one full twist remains) naturally forms a
**double loop** (Fig. 1b). This is the key construction:

- One side of the strip always faces outward.
- Since E is perpendicular to the strip face, and the same face
  always points out, **E always points radially inward** (electron)
  or **always outward** (positron).
- The field rotation (twist) and the orbital rotation (going around
  the double loop) are **commensurate** — they track each other so
  that E doesn't flip direction as the photon orbits.
- **B points upward** (along the torus symmetry axis). For the
  idealized case where both loops overlap (tube radius → 0), this
  is exact. For paths with nonzero tube radius, B is tangential to
  the torus surface and oscillates as the path wraps around θ, but
  the net result is a vertical magnetic dipole.

It is the inward E that gives rise to **charge**, and the upward B
that gives rise to the **magnetic moment**.

## 3. The geometry (§2, Fig. 2)

- **Double loop = (1,2) topology.** The path goes once around the
  tube (p=1, minor axis θ) for every two loops around the ring
  (q=2, major axis φ). Looking through the hole you see two loops.
  This is what makes the spin half-integral.
- **Intrinsic length scale:** the special case where both loops
  overlap gives a loop radius r = λ_C / 4π, which is the mean
  radius of energy transport (the "eye of the torus").
- **Rotation horizon:** the maximum radius at which a valid path
  of length λ_C can exist is λ_C / 2. This sets the outer boundary
  of the object — a Compton wavelength in diameter.
- **Tube radius** a is not precisely specified by WvM. Our studies
  (toroid-geometry, knot-zoo) found that the effective ratio
  a/R = 1/√(πα) ≈ 6.60 is needed to reproduce q = e from the
  WvM charge formula.

## 4. Energy flow in the volume (§2, Fig. 2)

WvM note: "we are firmly in the diffractive limit, where it makes
little sense to talk about a specific photon 'path'." A single
photon confined to a region of its own wavelength is a wave, not a
particle on a track.

The consequence: "Any path which fulfils the constraint of having
length λ_C may contribute to the structure of the complete object."
Fig. 2 illustrates this — **streamlines of energy flow** (Poynting
vector) trace (1,2) geodesics on **a family of nested toroidal
surfaces**. The nested surfaces are not separate photons or separate
orbits. They represent the energy flow pattern of a single photon
whose field, as a wave, extends across the toroidal volume.

⚠ **Correction history:**
- v1: We modeled the photon as a single path on one torus surface
  (2D). This is the simplified visualization (Fig. 1b), not the
  full picture.
- v2: We then over-corrected, calling the radial direction a
  possible third compact dimension. This was wrong — individual
  streamlines stay at constant tube radius r. Nothing propagates
  radially. r is a transverse mode coordinate (like the radial
  intensity profile of a waveguide mode), not a compact dimension.
- **Current understanding:** The primary model is the twisted-strip
  path on the torus surface. The nested surfaces in Fig. 2
  represent energy flow distribution in the diffractive limit.
  The compact space (if one exists) is 2D (φ, θ). The radial
  field profile is the transverse mode structure, not a separate
  dimension.

**Open question: precession as an alternative to diffraction.**
WvM explain the volume-filling energy flow by appealing to the
diffractive limit. An alternative: if the (1,2) path **precesses**
(drifts on the torus surface between cycles), the time-averaged
field would sweep out the nested surfaces naturally. The (1,2)
geodesic is exactly closed (winding ratio 1:2 is rational), so
exact closure gives no precession — but any perturbation (self-field
interaction, geometric imperfection) would break exact closure.
The electron's key properties (charge, spin, mass, magnetic moment,
g-factor) all derive from the (1,2) topology and local
commensurability, not from exact path closure — so precession would
preserve them. WvM do not discuss this possibility. See
QUESTIONS.md Q22–Q23.

## 5. Charge derivation (§3)

WvM confine a photon of wavelength λ to a spherical volume of
diameter λ. The average E-field magnitude inside is
⟨E⟩ = √(6hc / πε₀λ⁴). Comparing this to the Coulomb field at
the mean energy transport radius r = λ/4π gives:

    q = (1/2π) √(3ε₀ℏc) ≈ 0.91e

The charge is independent of the photon's energy (and hence the
object's size) — it arises purely from the topology. The ~9%
deficit comes from assuming uniform field distribution in a
spherical cavity.

Our studies showed that adjusting the geometric ratio to
a/R = 1/√(πα) gives q = e exactly.

## 6. Spin (§4)

The photon has angular momentum ℏ. The confined photon must travel
around its path twice (double loop) to return to its starting
orientation. The internal rotational frequency is therefore ωs = 2ω,
and the angular momentum is:

    L = U / ωs = ℏω / 2ω = ℏ/2

This is spin ½, arising from the (1,2) topology. It holds for any
path length (any mass) — it is purely topological.

## 7. Magnetic moment and g-factor (§5)

A small fraction of the total energy resides in the non-rotating
external Coulomb field. This shifts the internal wavelength to
λ = aλ_C where a = 1 + α'/2π. The magnetic moment is then:

    μ = s g μ_q,  where  g = 2(1 + α'/2π) ≈ 2.0023

This matches the first-order QED anomalous magnetic moment. In the
WvM model, the anomaly comes from the energy in the external
(non-rotating) field, rather than from radiative corrections.

## 8. Point-like interaction (§6)

A moving confined photon is alternately red- and blue-shifted. The
blue-shifted region (which carries most of the energy-momentum) has
characteristic size λ_C / (4πγ), which is always smaller than the
de Broglie wavelength λ_B / 2. Therefore the internal structure is
never resolved in scattering, regardless of collision energy. The
interaction remains point-like.

## 9. Confinement (§7)

WvM postulate self-confinement but do not derive it. They discuss
possible mechanisms: Casimir forces (unstable for spheres, possibly
stable for tori), non-linear vacuum effects (relevant when E ∥ B),
and soliton solutions. The confinement question remains open.

A compact extra dimension (Kaluza-Klein) could provide confinement
by making the toroidal path a geodesic — see `studies/answers/A7`.

## 10. What the paper does NOT address

- **Confinement mechanism** — postulated, not derived.
- **Stability** — no perturbation analysis.
- **Quantization** — the model is semi-classical. No connection to
  full QED beyond the g-factor coincidence.
- **Other particles** — the paper focuses on the electron. §8
  speculates that quarks might be "partial loops" requiring qqq or
  qq̄ to close, but this is not developed.
- **Tube radius** — not determined from first principles.
- **Radial field profile** — the distribution of field intensity
  across the toroidal volume is not computed.
- **Path closure and precession** — the paper assumes the (1,2)
  path is exactly closed (retraces every cycle). It does not
  discuss whether exact closure is necessary, or whether a
  precessing orbit would produce the same properties. The
  constructive self-interference argument (§2) implicitly assumes
  exact closure, but in the diffractive limit small spatial shifts
  may not affect interference significantly.

## 11. Where WvM concepts appear in our studies

| Concept | Study | Finding |
|---------|-------|---------|
| Charge from a/R | toroid-geometry | F3: a/R = 1/√(πα) gives q = e |
| (1,2) orbit uniqueness | knot-zoo | F3: only (1,2) gives charge in Frenet model |
| Fractional charges | knot-zoo | F4: a/R values for 1/3e, 2/3e mapped |
| Compact dimension hypothesis | knot-zoo | F2: proposed, not demonstrated |
| Dimensionality | QUESTIONS.md | Q3/Q4: 2D (φ, θ) + transverse mode profile |
| Field extent vs orbit | knot-zoo | F1: a_field/R ≈ 6.6, distinct from orbit |

---

*Last updated after full re-read of the paper. Corrected
over-emphasis on the volume-filling aspect; restored primacy of the
twisted-strip model; added sections on spin, g-factor, point-like
interaction, and confinement.*
