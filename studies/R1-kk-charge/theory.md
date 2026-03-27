# From S¹ to T²: Two Material Dimensions and the Electron

**Prerequisite:** [`primers/kaluza-klein.md`](../../primers/kaluza-klein.md)
— Kaluza-Klein theory from the ground up.

This paper argues that the Williamson–van der Mark (WvM) electron
model maps naturally onto a Kaluza-Klein theory with **two**
material dimensions (a flat torus T²) rather than one (a circle S¹).
It sets up the propositions that this study will test.

---

## 1. What KK with one dimension gives you — and what it doesn't

Standard KK (see the prerequisite) adds one compact dimension
w ~ w + L to spacetime. The results are powerful:

- Charge is momentum in w → quantized, conserved
- Maxwell's equations fall out of the 5D Einstein equations
- The Lorentz force falls out of the 5D geodesic equation

But one compact dimension gives only one type of closed path: the
circle, traversed n times. Every particle with the same |n| has
the same topology. The only quantum number S¹ provides is the
winding number n, which maps to charge.

**What S¹ does not give:**
- **Spin variation.** All paths on S¹ have the same topology (a
  circle). There is no mechanism for different spins to emerge
  from different path topologies.
- **Multiple particle types.** The only distinction between
  particles on S¹ is how many times they wind around (n = 1, 2,
  ...). All n = 1 particles are topologically identical.
- **Half-integer spin.** A single traversal of S¹ returns to the
  starting point with the same orientation. There is no
  720°-to-return property that characterizes fermions.

The WvM electron has spin ½ from its (1,2) double-loop topology —
the photon must traverse the path **twice** to return to its
starting orientation. This topological property requires two
independent wrapping directions. It cannot exist on S¹.


## 2. Two material dimensions: the flat torus T²

Add two material dimensions instead of one:

    w₁ ~ w₁ + L₁
    w₂ ~ w₂ + L₂

Two independent periodic coordinates. The material space is
T² = S¹ × S¹ — a flat torus. "Flat" means zero intrinsic
curvature: a straight line in this space is genuinely straight, not
curved. The "torus" (donut) shape is an artifact of embedding this
flat space in 3D for visualization.

The flat torus is just a rectangle with opposite edges identified:

    +--------+--------+
    |        |        |
    |   →  → | →  →   |   ← top edge = bottom edge
    |  ↗     |  ↗     |
    | ↗      | ↗      |
    +--------+--------+
       ↑                    ← left edge = right edge
    (wraps)

A straight line drawn at an angle across this rectangle wraps
around both directions. After enough traversals, it closes on
itself. The slope of the line determines how many times it wraps
in each direction before closing.


## 3. Geodesics on T² are torus knots

A straight line on the flat rectangle with slope L₂/L₁ × (q/p)
wraps p times vertically (w₂ direction) per q times horizontally
(w₁ direction) before closing. This is a **(p,q) torus knot** in
our convention (see `reference/WvM-summary.md` Notation).

Different coprime (p,q) pairs give **topologically distinct**
geodesics on the same T²:

| Path | Wraps in w₁ | Wraps in w₂ | Topology |
|------|-------------|-------------|----------|
| (1,1) | 1 | 1 | Simple loop |
| (1,2) | 2 | 1 | Double loop — the WvM electron |
| (3,2) | 2 | 3 | Trefoil-like |
| (2,1) | 1 | 2 | Different double loop |

Each path is a straight line — a geodesic. No force is needed to
maintain it. The path topology is determined by the direction of
travel, not by confinement.

**Key contrast with S¹:** on S¹, all geodesics are the same
circle (traversed n times). On T², different directions give
different topologies. The material space itself determines what
particle types are possible.


## 4. Where spin comes from

On T², a (1,q) geodesic wraps q times around w₁ per once around
w₂. An observer watching the w₁ direction sees q full loops before
the path returns to its starting point and orientation.

For q = 2: the path must traverse twice to return. The WvM
argument gives spin:

    s = ℏ / q = ℏ / 2

The half-integer spin is a direct consequence of the double-loop
topology, which is only possible with two wrapping directions.

For q = 1: the path returns after one traversal → spin 1 (boson).
For q ≥ 3: non-standard spins, ruled out by spin-statistics.

This is the central advantage of T² over S¹: the second dimension
provides the topological structure needed for fermions.


## 5. Where charge comes from

This is the central question of this study.

**In standard KK (S¹):** charge = momentum in the compact
direction. Quantized by periodicity. Clear, exact, proven.

**In WvM:** charge arises from the topology of the confined
photon's E-field. The inward-pointing electric field of the (1,2)
path, combined with the photon's energy density, gives:

    q_WvM = (1/2π) √(3ε₀ℏc) ≈ 0.91e

**In KK with T²:** momentum in each material direction is
independently quantized:

    p₁ = n₁ ℏ / R₁
    p₂ = n₂ ℏ / R₂

These two momenta correspond to two independent conserved charges
(the gauge group is U(1) × U(1), not U(1)). For the (1,2)
geodesic, the winding numbers are n₁ = 2 and n₂ = 1. What charge
do these produce? How does it relate to the WvM charge?

**The question this study answers:** are these two charge
derivations (WvM cavity field vs. KK compact momentum) the same
mechanism with different names, or different mechanisms that happen
to give similar answers?


## 6. The WvM electron as a geodesic on the material sheet

The mapping between the WvM model and the material sheet (T²):

| WvM concept | Material-sheet concept |
|-------------|------------|
| Photon confined to toroidal path | Photon following a geodesic on the material sheet |
| (1,2) double loop | Straight line at slope 1:2 on the rectangle |
| Path length = λ_C | Geodesic circumference = λ_C |
| Confinement by unknown force | No force needed — geodesic on material space |
| Charge from E-field topology | Charge from momentum in material directions |
| Spin ½ from double loop | Spin ½ from q = 2 winding |
| Rotation horizon at λ_C/2 | (No direct analog — see §8) |
| Nested toroidal surfaces (Fig. 2) | Transverse field profile in non-compact directions |

If this mapping is valid, the WvM model IS a 6D KK theory
(3 space + 1 time + 2 material), with the specific material space
T² and a (1,2) geodesic.


## 7. What the material sheet predicts that S¹ doesn't

If the electron is a (1,2) geodesic on T², the same material space
supports other geodesics. This makes predictions:

| Geodesic | Spin | Charge (Frenet model) | Candidate |
|----------|------|----------------------|-----------|
| (1,2) | ½ | e | Electron |
| (3,2) | ½ | 0 | Neutrino? |
| (5,2) | ½ | 0 | (unknown) |
| (1,1) | 1 | ? | Boson? |

S3 (S3-knot-zoo) showed that in the Frenet frame
model, only (1,2) gives nonzero charge. All other (p,2) knots
give exactly zero by symmetry cancellation. Whether this holds
under a different polarization transport rule, or in the full KK
framework (where charge comes from compact momentum, not E-field
direction), is an open question.


## 8. Open issues with the material-sheet mapping

### Gravitational vs electromagnetic coupling

Standard KK derives electromagnetism from 5D gravity. The charge
formula involves the gravitational constant G:

    q_KK = √(16πG/c⁴) × nℏc / R_KK

(The exact prefactor depends on normalization conventions, but √G
always appears.) This gives R_KK ~ 10⁻³⁴ m for q = e — the
Planck scale.

WvM's model is purely electromagnetic. The structures are at the
Compton scale (~10⁻¹² m). This 10²¹ discrepancy means WvM is
NOT standard gravitational KK.

However, one can do KK-like analysis without gravity: study
Maxwell's equations on a space with compact dimensions, without
embedding in a gravitational metric. In this "electromagnetic KK,"
the charge mechanism would be the same (quantized momentum in
the compact direction) but the coupling constant would be
electromagnetic, not gravitational. Whether this gives a different
charge formula — and whether it matches WvM — is the central
question of this study (P1).

### The field in non-compact directions

In WvM, the photon's electromagnetic field extends into 3D space
out to the rotation horizon (λ_C/2). The nested toroidal surfaces
of Fig. 2 are the field's transverse profile in xyz.

In the material-sheet picture, the photon moves in the material dimensions
(w₁, w₂). Its field extends into the non-compact dimensions
(x, y, z). How the material-dimension motion produces 3D fields
is governed by the 6D field equations — the higher-dimensional
analog of how KK produces Maxwell's equations from 5D gravity.

Whether WvM's "rotation horizon" and "spherical cavity" have
natural material-sheet analogs, or whether they're artifacts of the 3D
visualization, is unclear.

### The gauge group

The material sheet gives U(1) × U(1) — two independent gauge symmetries. We
observe only one electromagnetism. Either:
- One of the U(1)'s is electromagnetism and the other is something
  else (a hidden or broken symmetry)
- The two U(1)'s combine in a specific way for the (1,2) geodesic
- The material-sheet structure breaks U(1) × U(1) to a single U(1) through
  some mechanism

This is a genuine theoretical question that the study should
address.

### The path length constraint

WvM requires the path length to be exactly one Compton wavelength
λ_C (periodic boundary conditions for the photon). On T²:

    L_path = √( (2 L₁)² + L₂² ) = λ_C

This gives a constraint relating L₁ and L₂ to the electron mass.
But it's one equation with two unknowns. A second constraint is
needed — perhaps the charge quantization condition, or a geometric
condition on the ratio L₂/L₁.


## 9. Propositions to test

### P1. Algebraic equivalence of WvM and KK charge

**Claim:** the WvM charge formula q = (1/2π)√(3ε₀ℏc) is
algebraically equivalent to the KK charge quantum q = nℏ/(Rc)
for a specific identification of the compact radius R with the
WvM geometric parameters.

**Test:** Set q_WvM = q_KK and solve for R. Does R correspond to
a WvM length scale (λ_C/4π, λ_C/2, the path length)?

### P2. Charge from compact momentum

**Claim:** the (1,2) geodesic on T² has winding numbers (n₁, n₂)
= (2, 1). The momentum in each material direction is quantized.
The net charge is a specific function of n₁, n₂, R₁, R₂.

**Test:** Write down the KK charge formula for T² (two compact
radii). Evaluate for (1,2) winding. Does it give q ≈ e for
reasonable dimension sizes?

### P3. Single effective charge from two U(1)'s

**Claim:** although the material sheet gives U(1) × U(1), the physical charge of
the (1,2) geodesic is a single effective charge (the electron has
one charge, not two independent charges).

**Test:** How do the two KK charges combine for a geodesic that
winds in both directions? Is there a natural projection to a
single effective charge?

### P4. Unification of α

**Claim:** the a/R = 1/√(πα) relationship from S2 and the
KK compact radius R_KK = ℏ/(ec) are two expressions of the same
geometric quantity.

**Test:** Express both in terms of the material-sheet parameters (L₁, L₂).
Do they unify?

---

*This paper sets up the framework. The study proceeds by testing
P1 first (pure algebra), then P2–P4 if P1 succeeds. See
`README.md` for the study plan and `../../primers/kaluza-klein.md`
for the KK prerequisite.*
