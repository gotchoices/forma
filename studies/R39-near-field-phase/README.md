# R39. Phase-dependent near-field interaction

**Status:** Complete — see `findings.md`
**Depends on:** R7 (torus field energy), R19 (shear-charge mechanism),
  R26–R28 (Ma metric, mode spectrum), R29 F6 (gauge boson nuclear
  force candidate)
**Motivates:** Q88 (phase-dependent nuclear force), Q82 (entanglement
  as phase locking)


## Question

Particles in MaSt are modes on an embedded compact geometry.
At distances much larger than the material circumferences
(r >> L), they look like point charges and interact via
Coulomb's law.  At distances comparable to L (r ~ L), the
internal mode structure matters.

**Does the interaction between two identical modes depend on
their relative phase?**  If so, how strong is the near-field
correction, and at what distance does it become significant?


## Why this matters

Q88 hypothesized that anti-phased modes (Δφ = 180°) have
their near-field multipoles anti-aligned, partially cancelling
the short-range repulsion.  If true:

- The nuclear force might partly arise from phase-dependent
  near-field structure, not only from a mediating boson (R29 F6)
- α might be constrained by the requirement that stable nuclei
  exist (the balance between far-field repulsion and near-field
  cancellation)
- Entanglement (Q82) has measurable force consequences —
  phase-locked particles interact differently than uncorrelated
  ones

None of this has been computed.  This study does the computation.


## Physical picture

A mode (n₁, n₂) on an embedded torus has a charge distribution
that is NOT a point.  In the WvM picture, the charge sits along
the (n₁, n₂) geodesic — a 1D curve wound around the torus
surface.  The 3D E-field of this line charge has monopole (Q),
dipole (d), quadrupole (Q_ij), and higher moments.

The monopole is phase-independent (it's the total charge, a
topological invariant).  The higher multipoles depend on the
orientation of the charge distribution on the torus, which is
determined by the mode phase φ.

For two particles at separation d with phases φ₁ and φ₂:

- The monopole-monopole interaction = Coulomb = Q²/d
  (phase-independent)
- The monopole-dipole, dipole-dipole, etc. interactions depend
  on Δφ = φ₂ − φ₁

The near-field correction is:

    δF(d, Δφ) = F_total(d, Δφ) − F_Coulomb(d)

Averaging δF over all Δφ should give zero (uncorrelated
particles see only Coulomb on average).  The phase-locked
correction δF(d, π) − ⟨δF⟩ is the entanglement force.


## Tracks

### Track 1. Single-mode field structure

Compute the 3D E-field and multipole decomposition of a single
Ma mode on an embedded torus.

**Method:**
1. From ma_model.py: get L₁, L₂ (electron sheet circumferences) at
   the standard geometry (r_e = 6.6).
2. Embed: R = L₂/(2π), a = L₁/(2π).  The (1,2) geodesic winds
   once around the tube and twice around the ring.
3. Distribute charge Q = e along the geodesic with phase-
   dependent modulation (parameterized by φ).
4. Compute the 3D E-field on a spherical grid centered on the
   torus.
5. Decompose into spherical harmonics Y_lm to get the multipole
   moments q_lm(φ).
6. Catalog which multipoles are nonzero and how they depend on φ.

**Deliverables:**
- Multipole spectrum (l = 0, 1, 2, ...) as a function of φ
- Ratio of dipole energy to monopole energy (= the "near-field
  fraction")
- Comparison with R7 F4's estimate (~α for far-field, ~1−2α
  for near-field)

**Tools:** Extend R7's `torus_charge.py` with multipole
decomposition.  This becomes the first component of
`lib/embedded.py` (new module).


### Track 2. Two-mode interaction energy

Compute the interaction between two identical modes at
separation d with relative phase Δφ.

**Method:**
1. Place two charge distributions (from Track 1) at separation
   d along the z-axis.
2. Compute the total electrostatic interaction energy by direct
   numerical integration:
   U_int = Σ_i Σ_j  dq_i × dq_j / (4πε₀ |r_i − r_j|)
   where i runs over segments of particle 1 and j over particle 2.
3. Sweep d from 0.1L to 100L.
4. At each d, sweep Δφ from 0 to 2π in steps of π/12.
5. Compare U_int(d, Δφ) to the point-charge Coulomb energy
   U_C = e²/(4πε₀ d).

**Deliverables:**
- Heat map of U_int(d, Δφ) / U_Coulomb(d)
- Force curves F(d) at Δφ = 0, π/2, π, 3π/2
- The separation d* where the near-field correction exceeds 1%
  of Coulomb
- Whether there exists any (d, Δφ) where the net force is
  attractive

**Tools:** Direct pairwise sum (O(N²) per configuration).  At
N = 500 segments per particle, this is 250K evaluations per
(d, Δφ) point — fast.


### Track 3. Near-field correction characterization

Extract the phase-dependent near-field correction and
characterize it.

**Method:**
1. From Track 2 data, compute:
   - ⟨U⟩_φ = average over Δφ at each d (the uncorrelated
     interaction)
   - δU(d, Δφ) = U(d, Δφ) − ⟨U⟩_φ (the phase-locked correction)
2. Verify ⟨U⟩_φ ≈ U_Coulomb (uncorrelated particles see only
   Coulomb on average).
3. Characterize δU(d, π) — the anti-phase correction:
   - Functional form (power law? exponential falloff?)
   - Crossover distance (where |δU| = U_Coulomb)
   - Sign (attractive or repulsive?)
4. If d* is at nuclear scale (~1 fm for proton-sheet modes),
   compute the effective barrier reduction factor F = U_eff/U_C
   at Δφ = π.

**Deliverables:**
- The "entanglement force" δF(d, π) as a function of d/L
- Falloff exponent (does it go as 1/d³ like a dipole, or
  faster?)
- Barrier reduction factor F at the proton scale
- Comparison with Q88's estimates


### Track 4. Proton-scale calculation

Repeat Tracks 1–3 for the proton sheet (L₅, L₆) instead of
the electron sheet.

**Method:**
1. Use proton-sheet circumferences (L₅ ~ 5.9 fm, L₆ ~ 0.66 fm).
2. Embed the (1,2) proton mode on a torus with R = L₆/(2π),
   a = L₅/(2π).
3. Compute the two-proton interaction energy as a function of
   d and Δφ.
4. The nuclear force scale (1–3 fm) is 1.5–4.5 × L₆.  Check
   whether the near-field correction is significant at this
   scale.

**Deliverables:**
- Two-proton interaction at nuclear distances (1–3 fm)
- Effective Coulomb barrier reduction at Δφ = π
- Comparison with actual nuclear binding (~2–8 MeV/nucleon)
- Assessment: can phase-dependent near-field interaction explain
  nuclear binding, partially explain it, or is it negligible?


## What we learn either way

**If the near-field correction is large (> 10% of Coulomb at
r ~ L):**
- Phase relationships between modes have force consequences
- Entanglement is not just correlations — it changes the physics
- Nuclear binding may have a geometric near-field component
- Worth pursuing the cold fusion line of inquiry (Q88 §5)

**If the correction is small (< 1% of Coulomb at r ~ L):**
- The WvM charge distribution is effectively a point charge
  beyond ~L
- Entanglement affects correlations but not forces
- Nuclear binding requires a separate mechanism (R29 gauge
  bosons, or something else)
- Q88's cold fusion scenario is ruled out

Either result is informative.


## Tools needed

### New: lib/embedded.py

Embedded torus geometry and near-field calculations.  First
module of the new library (see `lib/ma-model.md`).

| Function | Purpose |
|----------|---------|
| `torus_embed(L_tube, L_ring)` | Compute R, a from circumferences |
| `geodesic_points(R, a, n1, n2, N, phi)` | (n₁,n₂) geodesic with phase offset |
| `charge_distribution(R, a, n1, n2, N, phi, Q)` | Charge segments along geodesic |
| `field_at(charges, positions, point)` | E-field at a 3D point from charge distribution |
| `multipoles(charges, positions, l_max)` | Spherical harmonic decomposition |
| `interaction_energy(dist1, dist2)` | Pairwise interaction between two distributions |

These build on R7's `torus_charge.py` but are generalized and
reusable.

### Existing: lib/ma_model.py

Used to get circumferences L₁–L₆ and shears at the standard
geometry via `Ma(r_e=..., self_consistent=True).L`.  No changes
needed.


## Computational cost estimate

- Track 1: seconds (one charge distribution, one multipole
  decomposition)
- Track 2: ~30 min (sweep over ~24 Δφ values × ~50 d values
  × 250K pairwise sums)
- Track 3: analysis of Track 2 data, seconds
- Track 4: same as Track 2, different geometry parameters

Total: under an hour of compute.
