# R48: Does circular polarization helicity select charged modes?

**Status:** Complete — Tracks 1-2.  Q104 answered: negative.
**Questions:** [Q104](../../qa/Q104-helicity-forces-n2.md) (helicity forces n₂)
**Type:** compute
**Depends on:** R46 Track 5 (mode filtering assessment)

---

## Motivation

The (1,1) ghost mode — lighter than the electron, charged by
the n₁ = ±1 selection rule, never observed — has been the most
persistent problem in the MaSt mode spectrum.  R46 proved that
explicit slots can kill it, but the question remains: is there
a more fundamental reason it doesn't carry charge?

Q104 proposes that the photon's **circular polarization
helicity** may discriminate between modes.  On a torus, a
circularly polarized standing wave has its E-field rotation
synchronized with the tube's geometric rotation of the surface
normal.  This synchronization produces a constant outward E
component — charge.  But the synchronization depends on the
mode numbers (n₁, n₂), the aspect ratio ε, and the torus
geometry.

**The question:** does the Gauss's law integral ∮ E · n̂ dA
vanish for (1,1) but not for (1,2)?  If so, the helicity
itself selects which modes carry charge — no slots, no
waveguide cutoff, no external filtering needed.

## Strategy

Compute the Gauss's law flux integral for circularly polarized
standing waves on a torus, sweeping across mode numbers and
aspect ratios.  Pure geometry — no free parameters beyond ε
and (n₁, n₂).

## Tracks

### Track 1: Gauss flux integral for CP modes on a torus

**Goal:** For each mode (n₁, n₂), compute the total outward
E-field flux through the torus surface when the wave is
circularly polarized.  Determine which modes produce nonzero
charge.

**Method:**

1. Parametrize the torus surface:
   - Position: r(θ₁, θ₂) = ((R + a cos θ₁) cos θ₂,
     (R + a cos θ₁) sin θ₂, a sin θ₁)
   - Surface normal: n̂(θ₁, θ₂)
   - Area element: dA = (R + a cos θ₁) dθ₁ dθ₂

2. For mode (n₁, n₂), the geodesic direction on the flat
   sheet is k̂ ∝ (n₁/L₁, n₂/L₂).  At each point (θ₁, θ₂),
   construct the local propagation direction, the surface
   normal, and the in-surface transverse direction.

3. Circular polarization: E rotates in the plane perpendicular
   to k̂.  Decompose into normal and tangential components:
   - E_n = E · n̂ (the charge-producing component)
   - E_t = E − E_n n̂ (the moment-producing component)

4. The standing wave fills the full surface.  At each point
   (θ₁, θ₂), the phase of the wave is φ = n₁θ₁ + n₂θ₂.
   The CP field rotates as a function of φ.

5. Integrate E_n × dA over the full torus surface:
   Q = ε₀ ∮ E_n dA

6. Sweep:
   - Modes: (1,1), (1,2), (1,3), (2,1), (2,2), (2,4), (3,6)
   - Aspect ratios: ε = 0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.5

**Key outputs:**
- Table of Q(n₁, n₂, ε) — which modes have nonzero charge
- Whether (1,1) has zero charge for all ε
- Whether (1,2) has nonzero charge for all ε
- Whether n₂ = 2n₁ is special or just one of many charged modes

**Success criteria:**
- If Q(1,1) = 0 and Q(1,2) ≠ 0: Q104 confirmed — helicity
  selects (1,2).  Ghost eliminated by polarization geometry.
- If Q(1,1) ≠ 0 and Q(1,2) ≠ 0: Q104 fails — helicity does
  not discriminate.  Ghost elimination requires a different
  mechanism (slots, waveguide, or something else).
- If Q depends continuously on ε: there may be a critical ε
  where modes switch between charged and dark — geometrically
  interesting regardless of the Q104 outcome.

**Script:** [`scripts/track1_gauss_flux.py`](scripts/track1_gauss_flux.py)

---

## Files

| File | Contents |
|------|----------|
| [scripts/track1_gauss_flux.py](scripts/track1_gauss_flux.py) | Track 1: Gauss flux integral for CP modes |
| [findings.md](findings.md) | Results and interpretation |
