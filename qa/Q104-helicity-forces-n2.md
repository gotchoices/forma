# Q104. Does circular polarization helicity force n₂ = 2?

**Status:** Open — calculable
**Related:**
  [Q103](Q103-anomalous-magnetic-moment-from-defect-cost.md) (anomalous moment),
  [Q102](Q102-neutrino-neutrality-from-sheet-size.md) (charge threshold),
  R46 Track 5 (ring-circumference filter),
  [`primers/charge-from-energy.md`](../primers/charge-from-energy.md) (charge mechanism)

---

## 1. The question

The electron is a (1,2) mode on its material sheet — one
winding around the tube, two around the ring.  The tube
winding n₁ = 1 produces charge (GRID topological argument).
But why n₂ = 2?  Is it an independent quantum number, or is
it forced by the polarization structure of the photon?

## 2. The observation

A circularly polarized photon has **helicity** — its E vector
traces a helix along the propagation direction, rotating by
2π per wavelength λ.  When this photon is confined to a (1,2)
geodesic on a torus:

- The geodesic wraps once around the tube and twice around
  the ring per Compton wavelength λ_C.
- As the photon traverses one tube circuit, the **surface
  normal** rotates by 2π (geometric property of the torus).
- If the helical E rotation syncs with this geometric
  rotation (opposite sense), the normal component of E
  points outward everywhere — this is charge.
- The **tangential component** of the helix projects onto
  the ring direction.

The hypothesis: the tangential projection of the helix onto
the ring axis naturally produces exactly 2 oscillations per
Compton cycle.  If so, n₂ = 2 is not an independent choice —
it is a consequence of the helicity mapped onto the torus
geometry.

## 3. Why this matters

If the helicity forces n₂ = 2, then:

- The electron's quantum numbers are not two independent
  integers — n₂ follows from n₁ and the polarization
  structure.
- The (1,2) mode is the **unique** mode where tube-synced
  circular polarization produces a stable ring standing wave.
- Other modes like (1,1) or (1,3) would NOT be compatible
  with the helical field pattern — explaining why (1,2) is
  special without invoking the ring-circumference filter.
- Spin = n₁/n₂ = 1/2 would be a consequence of helicity,
  not a separate topological fact.
- For the proton (if (3,6)): n₂ = 2 × n₁ would again be
  forced, with the factor of 2 coming from the same
  helicity argument at the third harmonic.

## 4. The calculation needed

Decompose a helical E-field pattern on a (p, q) geodesic
of a torus into normal and tangential components:

1. Parametrize the (p, q) geodesic on a torus with aspect
   ratio ε = a/R.
2. At each point along the geodesic, compute the surface
   normal n̂ and the tangent to the geodesic k̂.
3. A circularly polarized wave has E rotating in the plane
   perpendicular to k̂.  Decompose E into:
   - E_normal = E · n̂ (charge contribution)
   - E_tangential = E − E_normal (moment contribution)
4. Compute the Fourier spectrum of E_tangential projected
   onto the ring direction as a function of the ring angle φ.
5. Check: does the dominant Fourier component have frequency
   n₂ = 2p?  Or some other relationship?

This is a geometry calculation on the torus — no physics
input beyond the definition of circular polarization and the
torus metric.  It should be doable analytically for the
(1,2) case and numerically for general (p, q).

## 5. Expected outcomes

**If n₂ = 2n₁ is forced:** the mode quantum numbers are
not independent.  Every charged mode has n₂ = 2n₁, giving
spin = 1/2 universally for all charged particles.  The
harmonic series would be (1,2), (2,4), (3,6), ... — each
is a higher-energy version of the same helical pattern.

**If n₂ is independent:** the helicity constrains the
phase pattern but does not uniquely fix n₂.  Multiple
n₂ values are compatible with the helix, and mode selection
comes from some other mechanism (ring circumference, energy
minimization, or explicit filtering).

**If the normal component is NOT constant:** the
synchronization between polarization rotation and geometric
rotation is imperfect for certain (p, q) values.  This
would mean only specific modes produce clean charge — a
geometric selection rule stronger than just "n₁ = odd."

## 6. Connection to the ring-circumference filter

R46 Track 5 and R47 Track 7 test whether the ring
circumference acts as a half-wavelength filter.  Q104 asks
a prior question: does the helicity itself determine how
many ring oscillations the wave has?

If Q104 shows n₂ = 2n₁ is forced, then the ring filter is
redundant for charged modes (they always have even n₂).  The
filter would still matter for dark/ghost modes (which have
different polarization structure and could have any n₂).

If Q104 shows n₂ is free, then the ring filter is essential
for selecting (1,2) over (1,1) and other unwanted modes.
