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
the ring. This convention is defined in `studies/S3-knot-zoo/theory.md`
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

The primary motivation is the experimentally well-established
electron-positron annihilation/creation process e⁺e⁻ ↔ γγ. The
left side has two charged spin-½ leptons; the right has uncharged
helicity-1 bosons. WvM take this to suggest that leptons and
photons may be different states of the same object, and use the
photon itself — which already has E and B field components — as
the precursor of both electron and positron.

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
**double loop** (Fig. 1b). This is the simplest of many possible
paths fulfilling the boundary conditions. The construction has
the remarkable property that:

- One side of the strip always faces outward.
- Since E is perpendicular to the strip face, and the same face
  always points out, **E always points radially inward** (electron)
  or **always outward** (positron), depending on the sense of path
  closure (whether the ends are brought together into or out of the
  plane of the paper).
- The field rotation (twist) and the orbital rotation (going around
  the double loop) are **commensurate** — they track each other so
  that E doesn't flip direction as the photon orbits.
- **B points upward** (along the torus symmetry axis), giving rise
  to a magnetic dipole.

Exactly one full twist is required; a half twist or double twist
would not give rise to a charge. WvM emphasize that the photon
remains uncharged — it is the confinement, the topology, and the
commensurability that produce the apparent charge.

The special case where both loops overlap gives a loop radius
r = λ_C / 4π. WvM note that the circulation repeats with a period
of half a wavelength; in flat space this would cause total
destructive interference, but in the curved space of the model the
interference is always constructive. The state is not a standing
wave but a stationary wave propagating around a double loop, and
therefore carries angular momentum.

## 3. The geometry (§2, Fig. 2)

- **Double loop = (1,2) topology.** The path goes once around the
  tube (p=1, minor axis θ) for every two loops around the ring
  (q=2, major axis φ). Looking through the hole you see two loops.
  This is what makes the spin half-integral.
- **Intrinsic length scale:** the special case where both loops
  overlap gives a loop radius r = λ_C / 4π, which is the mean
  radius of energy transport (the "eye of the torus").
- **Rotation horizon:** the maximum radius at which a valid path
  of length λ_C can exist is λ_C / 2. This sets an upper limit on
  the size of the object equal to a Compton wavelength in diameter.
  A lower limit comes from the impossibility of confining a wave
  into a box smaller than half its wavelength (and the minimum
  diameter of a spherically symmetric dielectric cavity is one
  wavelength). The effective size is therefore close to λ_C.
- **Tube radius** is not specified by WvM. The charge derivation
  depends on the internal field distribution and the effective
  charge radius, but these are left as approximations.

## 4. Energy flow in the volume (§2, Fig. 2)

WvM note: "we are firmly in the diffractive limit, where it makes
little sense to talk about a specific photon 'path'." A single
photon confined to a region of its own wavelength is a wave, not a
particle on a track.

The consequence: "Any path which fulfils the constraint of having
length λ_C may contribute to the structure of the complete object."
Fig. 2 illustrates this — **streamlines of energy flow** (Poynting
vector) trace (1,2) geodesics on **a family of nested toroidal
surfaces**. The paths in this family must not cross each other. The
nested surfaces are not separate photons or separate orbits. They
represent the energy flow pattern of a single photon whose field,
as a wave, extends across the toroidal volume.

WvM emphasize that the toroidal topology arising from the double
loop is "the simplest and most natural" of many topologies (knots)
consistent with the initial postulate.

## 5. Zitterbewegung analogy (§2)

WvM draw an explicit analogy to the Dirac electron's
Zitterbewegung. Dirac showed that electron motion decomposes into
bulk (relativistic) motion plus a light-speed oscillatory part at
twice the Compton frequency (2ω_C), and that any instantaneous
velocity measurement yields ±c. These are also features of the
double-looped confined photon.

The analogy deepens via Hestenes' geometrical "Zitterbewegung
interpretation of quantum mechanics," which shows that the
trajectory of a moving Dirac electron can be viewed as a series of
light-like helices of radius λ_C / 4π, defined by the rotation of
the energy-momentum flux perpendicular to the spin axis. This is
precisely the trajectory of the eye of the torus in the WvM model.
The difference: WvM arrive at the same geometry from a postulated
photon self-interaction, and their Zitterbewegung is that of the
electromagnetic field of a confined photon rather than of an
electron wavefunction.

## 6. Charge derivation (§3)

WvM confine a photon of wavelength λ to a spherical volume of
diameter λ. The average E-field magnitude inside is
⟨E⟩ = √(6hc / πε₀λ⁴). Comparing this to the Coulomb field at
the mean energy transport radius r = λ/4π gives:

    q = (1/2π) √(3ε₀ℏc) ≈ 0.91e

The charge is independent of the photon's energy (and hence the
object's size) — it arises purely from the topology. The ~9%
deficit comes from assuming a homogeneous field distribution in a
spherical cavity. WvM note that the result depends on the detailed
distribution of internal fields and the precise value chosen for
the effective charge radius, but that "any reasonable variation of
these parameters will still yield a finite value close to that of
the elementary charge."

## 7. Spin (§4)

The photon has angular momentum ℏ. The confined photon must travel
around its path twice (double loop) to return to its starting
orientation. The internal rotational frequency is therefore ωs = 2ω,
and the angular momentum is:

    L = U / ωs = ℏω / 2ω = ℏ/2

This is spin ½, arising from the (1,2) topology. It holds for any
path length (any mass) — it is purely topological. The field
vectors must rotate through 720° before returning to the same
orientation, so (by the spin-statistics theorem) the object should
be a fermion.

### Spin structure and SU(2)

The spin configuration differs fundamentally from a rigid body.
At any instant, a field element rotates both around the z-axis
(orbital spin, at the mean energy transport radius) and about a
perpendicular axis tangential to the eye of the torus (intrinsic
photon angular momentum). These two rotation axes are separated
by λ_C / 4π, so no single instantaneous rotation axis can be
defined.

The tangential spin axis performs a rotation in the x,y-plane about
the z-axis with frequency 2ω_C and radius λ_C / 4π. Its projection
on z is always zero, so the z-component of angular momentum remains
the sharp value L_z = ±ℏ/2. WvM note that for the model to fully
match the electron, the average angular momentum around both x and
y should also be ±ℏ/2 (giving L² = ℓ(ℓ+1)ℏ²), but they find no
simple argument for this distribution.

Thomas precession provides a partial resolution: the relativistic
orbital velocity of the bound photon causes an apparent
counter-rotation of the photon frame (as seen externally), equal in
magnitude but opposite in sense to the orbital rotation. Any
initial spin distribution therefore appears to remain fixed.

The two possible states of the intrinsic photon angular momentum
(right or left circular polarisation) are interpreted as
corresponding to the **SU(2) of electron spin**. The energy flow
around the torus axis is always left-handed relative to the
magnetic moment direction (right-handed for the positron). The
mirror image of an electron is an electron in the other spin state.

## 8. Magnetic moment and g-factor (§5)

A small fraction of the total energy resides in the non-rotating
external Coulomb field (≈ α'/2π of the total). This reduces the
internal photon frequency and shifts the internal wavelength to
λ = aλ_C where a = 1 + α'/2π, with α' ≡ (q/e)²α being the
fine-structure constant for the model's charge q. The magnetic
moment is:

    μ = s g μ_q,  where  g = 2(1 + α'/2π)

Since q ≈ 0.91e, α' is close to but not exactly α. WvM note that
g is "very nearly the same" as the QED first-order result
g = 2(1 + α/2π) ≈ 2.0023. In the WvM model, the anomaly arises
from the energy in the external (non-rotating) field, rather than
from radiative corrections.

## 9. Point-like interaction and the "harmony of phases" (§6)

### Point-like interaction

A moving confined photon is alternately red- and blue-shifted
(Fig. 4). In a head-on collision between two confined photons, the
interaction is between the blue-shifted regions (which are
converging and carry most of the energy-momentum), with
characteristic size λ_C / (4πγ). The maximum resolving power of
one object for the other is λ_B / 2 in their centre-of-mass frame.
The relation γ⁻¹λ_C = (v/c)λ_B ensures that λ_C / (4πγ) < λ_B / 2,
so the internal structure is never resolved regardless of
scattering energy. The interaction remains point-like.

This follows from the model being purely electromagnetic: at
relativistic energies the effective size scales in exactly the same
way as a free-space photon. Since only one constituent is present,
there is no internal particle or field to absorb excess
four-momentum.

### De Broglie wavelength and harmony of phases

WvM derive the de Broglie wavelength from first principles within
the model. Integrating the Doppler-shifted internal frequency over
the closed path gives U = γU₀, hence m = γm₀. Angular momentum L
is conserved, so the effective radius shrinks as 1/⟨ω̂⟩.

In the rest frame, both the internal photon frequency and the
orbital frequency equal ω_C. In a moving frame these diverge: the
mean internal frequency increases to γω (blue shift), while the
orbital frequency slows to ω/γ (time dilation). Yet at any point
in space-time the two oscillations remain in phase. This provides
a physical origin for de Broglie's postulated "harmony of phases."

The internal phase φ = ω_C t₀ = ω_C γ(t − vx/c²) describes a wave
with phase velocity v_p = c²/v and spatial period:

    λ_B = h / (γm₀v)

which is the de Broglie wavelength. The total energy can be
expressed as ℏ⟨ω̂⟩ = ℏ√(ω²_C + ω²_B), decomposing into a
time-like component (Compton frequency, defined in the rest frame)
and a space-like component (de Broglie frequency, arising from
the relativistic transformation).

## 10. Confinement (§7)

WvM postulate self-confinement but do not derive it. The photon
must confine itself — any other constituent would compromise the
point-like interaction. The kind of curvature envisaged "need only
apply to the self-confined photon, and will not necessarily affect
any other object in the vicinity"; it cannot arise from gravitation,
which is far too weak. Although circulating solutions of the linear
Maxwell equations exist, the electron's definite mass implies some
nonlinear effect must also play a role.

Possible mechanisms discussed:

- **Casimir forces:** proposed by Casimir for a charged conducting
  shell bound by vacuum fluctuations. Shown to be unstable for a
  spherical shell, but possibly stable for flatter geometries such
  as a torus.
- **Non-linear vacuum effects:** the vacuum is known to be
  nonlinear (pair creation occurs only above a threshold). Nonlinear
  effects arise when E and B are not perpendicular or when E ≠ cB.
  However, photons with energy far above m_e exist without
  self-confining, so high energy density alone is not sufficient —
  the field geometry matters.
- **Soliton solutions:** solitary-wave solutions in nonlinear media
  can exhibit particle-like behaviour; some have been shown to obey
  the "harmony of phases."

### Pair creation mechanism

WvM propose that pair creation arises from a specific intermediate
state. When two identical-helicity photons collide head-on (each
with λ ≤ λ_C), their interference produces a **twisted-mode
standing wave** in which E ∥ B everywhere and at every instant.
The Poynting vector is identically zero — the mode is everywhere
non-propagating. This is precisely the configuration where vacuum
nonlinearity becomes relevant, and it is the threshold condition
for pair creation. The state may then decay back into two photons
or into an electron-positron pair. WvM note that if a confined
photon state with toroidal topology is formed, it will be stable
provided it is the lightest such object with that topology.

## 11. Other particles and magnetic monopoles (§8)

### Other particles

WvM speculate that quarks might be confined photon states that are
insufficient to complete a closed loop individually, but transform
a photon from one spatial direction to another. Closed
three-dimensional loops could then only be built from qqq and qq̄
combinations. This is not developed.

### Magnetic monopole exclusion

A 90° internal rotation of the fields would produce an object with
a magnetic monopole and an electric dipole instead of the reverse.
However, Dirac showed that the magnetic monopole field strength is
1/(2α) times the electric monopole strength. In the WvM model,
this would require the mean radius of energy transport to exceed
the rotation horizon, which is impossible. WvM conclude that a
stable magnetic monopole cannot form within this framework.

## 12. What the paper does NOT address

- **Confinement mechanism** — postulated, not derived.
- **Stability** — no perturbation analysis.
- **Quantization** — the model is semi-classical. No connection to
  full QED beyond the g-factor parallel.
- **Other particles** — briefly speculated (§8), not developed.
- **Tube radius** — not determined from first principles.
- **Radial field profile** — the distribution of field intensity
  across the toroidal volume is not computed.
- **Absolute mass scale** — the model does not fix the electron
  mass; it only relates the size to the Compton wavelength.
- **Full spin projection properties** — L_z = ±ℏ/2 is derived,
  but L_x and L_y projections are not shown to match quantum
  mechanical expectations.

## Cross-references

The following studies build on or investigate WvM concepts:

- [`studies/S2-toroid-geometry/`](../studies/S2-toroid-geometry/) — charge from geometric ratios
- [`studies/S3-knot-zoo/`](../studies/S3-knot-zoo/) — orbit uniqueness, fractional charges, field extent
- [`qa/Q07-flat-compact-dimensions.md`](../qa/Q07-flat-compact-dimensions.md) — compact dimension hypothesis
- [`qa/INBOX.md`](../qa/INBOX.md) — open questions (esp. Q3/Q4 on dimensionality, Q22/Q23 on precession)

---

## Reading notes

These record corrections to earlier misreadings of the paper.
They are not part of the paper's content.

⚠ **Energy flow (§4 above):** Earlier versions of this summary
(v1) modeled the photon as a single path on one torus surface.
This is the simplified visualization (Fig. 1b), not the full
picture. A subsequent version (v2) over-corrected, treating the
radial direction as a possible third compact dimension. Individual
streamlines stay at constant tube radius; nothing propagates
radially. The radial field profile is transverse mode structure,
not a separate dimension. The compact space (if one exists) is 2D
(φ, θ).

*Last updated: revised to separate paper content from study
results; added Zitterbewegung analogy, harmony of phases, magnetic
monopole exclusion, pair creation mechanism, and spin structure.*
