# R32. The running of α and the high-energy coupling

**Questions:** Q77 (α as impedance), Q18 (deriving α), Q47 (running of α)
**Type:** compute + theoretical  **Depends on:** R19, R27, R28, R31
**Status:** Active


## Motivation

R31 tried to derive α = 1/137 by looking INSIDE T⁶ (Casimir
energy, moduli stabilization) and failed — no mechanism
within the compact space selects the shear.

Q77 reframes the problem: α might not be an internal T⁶
parameter.  It might be the **impedance mismatch** between
T⁶ and R³ — a refractive index measuring how efficiently
electromagnetic energy crosses from compact to spatial
dimensions.

If α is a refractive index, it should exhibit **dispersion**:
the coupling should change with probe energy, just as the
refractive index of glass depends on wavelength.  This is
the running of α, observed experimentally:

    α(0)    ≈ 1/137.036   (Thomson limit)
    α(m_Z)  ≈ 1/127.9     (LEP measurement at 91 GeV)

In the Standard Model, the running comes from vacuum
polarization — virtual charged particles screening the bare
charge.  In the T⁶ model, the running would come from
the KK mode spectrum: each charged T⁶ mode contributes to
the screening, and the T⁶ has ~900 modes below 2 GeV (R28).

The central question: if we sum the contributions of ALL
charged T⁶ modes, does α converge to a recognizable
geometric constant at the compact scale (the high-energy
limit, often called "UV" in physics — by analogy with the
electromagnetic spectrum, where ultraviolet = short
wavelength = high energy)?  In particular, does it
converge to **1/24**, the value where gauge couplings
unify in GUT physics?


## Prior results

- **R28 Track 2**: ~29,000 raw modes, ~900 distinct below
  2 GeV.  Full mode census available.
- **R28 Track 4**: Predictive horizon at ~2 GeV (band
  spacing < 5 MeV).
- **R31 Track 3**: Casimir energy has no minimum — cannot
  select α from within T⁶.
- **R31 Track 4**: Naive KK Yukawa ruled out by 10⁵ — the
  massive KK tower couples far more weakly than the zero
  mode.
- **Q77**: α as impedance mismatch / refractive index
  hypothesis.


## Key questions

1. Does the T⁶ mode spectrum reproduce the observed running
   of α between 0 and m_Z?
2. What value does α converge to at the compact scale
   (E ~ 467 MeV, the proton ring energy)?
3. Is that value geometrically recognizable (1/24, 1/4π,
   or a lattice constant of T⁶)?
4. Does the number 24 have a natural geometric relationship
   to toroidal compactification?
5. Can the T⁶/R³ interface be modeled as an impedance
   boundary with a computable transmission coefficient?


## Approach: 4 tracks

### Track 1 — KK mode running of α  **Complete**

Enumerate all charged (Q ≠ 0) T⁶ modes and compute their
one-loop vacuum polarization contribution.

**Result:** CATASTROPHIC.  78,608 charged modes produce
running ~157,000× faster than the SM.  Landau pole at
~1 MeV.  This independently confirms R31 Track 4: ghost
modes cannot couple to the electromagnetic field at full
strength.  Suppression factor ~10⁵ required, consistent
with the Lamb shift constraint.  Findings F1–F7.


### Track 2 — Volume dilution and the high-energy coupling  **Complete**

Compute the T⁶ sheet areas and KK volume dilution.

**Result:** The "bare" coupling α_bare = α × r × μ₁₂²
gives 1/α_bare ≈ 5.1 (electron sheet) and 3.8 (proton
sheet).  NOT 1/24.  The two sheets give different bare
couplings because they have different aspect ratios.
The neutrino sheet volume ratio does NOT explain weak
interaction strength (off by 11 orders of magnitude).
Findings F8–F12.


### Track 3 — Why 24?  Geometric relationships  **Complete**

Survey all known mathematical contexts where 24 appears
and assess connection to T⁶.

**Result:** Cataloged 8 contexts.  The Dedekind eta
function η(τ)²⁴ is the strongest candidate: it is the
unique modular-invariant cusp form, and modular
invariance of the T² partition function forces it to
appear.  However, the naive T⁶ scalar partition function
contains |η|⁶ (not |η|²⁴), and no combination of the
model's aspect ratios produces 24.  The most promising
path: compute the gauge coupling normalization from the
modular-invariant partition function and check for 1/24.
Findings F13–F17.


### Track 4 — Impedance at the T²/R³ interface  **Complete**

The central physical picture: a particle is a standing
wave on T².  That wave carries energy.  How much of that
energy couples out into R³ as observable interaction?
The answer should be α.

The framing is per-sheet (T² → R³⁺¹), not T⁶ → R³.
Each T² independently couples to the non-compact space.
If 24 enters, it may be 3 sheets × 8 channels/sheet,
where 8 = 2 compact × 4 non-compact dimensions.


#### Sub-track 4a — Energy partition by propagation channels

A source at a point in 10D radiates into all available
directions.  At the emission point, the source does not
know which dimensions are compact and which are open.
Energy divides among ALL propagation channels:

The 10D metric has 10×11/2 = 55 independent components:
- 10 diagonal (4 non-compact + 6 compact)
- 45 off-diagonal, decomposing into:
  - 6 within R³⁺¹ (gravity: g_{μν})
  - 3 within-sheet shears (s₁₂, s₃₄, s₅₆)
  - 3 cross-sheet shears (σ_ep, σ_eν, σ_νp)
  - 9 within-T⁶ cross-dimension (g_{ij}, i≠j, different sheets)
  - 24 gauge couplings (g_{μi}: 4 non-compact × 6 compact)

The electromagnetic field is ONE gauge field (4 components
out of 24 total gauge components).  Compute the fraction
of energy in the EM channel under various partition rules
(democratic, weighted by metric determinant, etc.).

Shears matter here: they are off-diagonal metric
components that redirect energy between dimensions.
A sheared torus has energy flowing in directions that
are tilted relative to the coordinate axes.  The shear
doesn't just create charge — it redirects propagation,
mixing compact and non-compact channels.


#### Sub-track 4b — Dimensional mismatch: 2D cavity → 3D space

When a 2D resonator (T²) radiates into 3D open space,
there is a fundamental dimensional mismatch:

- In T² (2D): the density of states is constant per unit
  energy (ρ₂D = A/(2πℏ²c²))
- In R³ (3D): the density of states grows as √E
  (ρ₃D ∝ V × E^{1/2})

The ratio ρ₂D/ρ₃D at a given energy E sets how well a
T² mode couples to the R³ continuum.  This is analogous
to a waveguide opening into free space: the transmission
coefficient depends on the ratio of confined to free
mode densities.

Compute the waveguide radiation resistance for a
rectangular cavity (dimensions L₁ × L₂) opening into
3D free space.  This is standard microwave engineering:
the coupling depends on L₁L₂/λ² (aperture area in
wavelength units).  For the electron T² at the (1,2)
mode frequency, this ratio is A_e/(2πλ_e)² ≈ 27
(from Track 2, F8).


#### Sub-track 4c — Solid angle in d dimensions

In d = 10 dimensions, a point source radiates into a
(d−1)-sphere with solid angle Ω_d = 2π^{d/2}/Γ(d/2).
The fraction going into any 3D subspace is related to
the ratio Ω₃/Ω₉ (or more precisely, the projection).

Compute this for d = 4 (non-compact), d = 6 (compact),
and d = 10 (total).  Also for the per-sheet case:
d_eff = 4 + 2 = 6 dimensions (one T² + R³⁺¹).


#### Sub-track 4d — Fresnel transmission at impedance boundary

The Fresnel equations give reflection/transmission at an
interface between media with different wave speeds.  If
c_T² ≠ c_R³, the transmission coefficient T depends on
the ratio n = c_R³/c_T².  Solve T = α for n and check
if n is geometrically meaningful.

Also compute: for a sheared torus, the effective wave
speed in the shear direction differs from the coordinate
directions.  The shear s creates an anisotropy.  This
anisotropy IS a refractive index.  What is c_shear/c_axis
as a function of s?


**Output**: Numerical coupling efficiency from each
sub-track.  Does any produce α = 1/137 from geometry?

**Result:** The 4π in the α formula IS the 3D solid angle.
The shear sin²(2πs) provides the dominant suppression
(~1/240 to ~1/435).  No simple geometric partition
(channel counting, solid angles, aperture ratios)
reproduces 1/137.  The weighted gauge field partition
(by 1/L²) gives 1/80, the closest match.  The question
"why α = 1/137?" reduces to "why s ≈ 0.01?"  The
aperture model gives 1/α ≈ r × μ² ≈ 27, close to 24
but dependent on unconstrained r_e.  Findings F18–F23.


## What success looks like

- **Strong result**: Track 1 reproduces α(m_Z) ≈ 1/128
  from the T⁶ mode spectrum, AND α converges to 1/24 at
  the compact scale, AND Track 3 identifies WHY 24 appears
  in torus geometry.  This would connect T⁶ to GUT
  unification and provide a geometric origin for the
  running.

- **Moderate result**: Track 1 gives a sensible running
  (monotonically increasing α with energy) but the UV
  value is not 1/24.  The UV value might still be a
  recognizable geometric constant, providing a new
  constraint.

- **Null result**: The running is pathological (wrong
  sign, divergent, or unreasonably fast) — which would
  mean the ghost modes don't contribute to vacuum
  polarization as assumed, constraining their physical
  status.

- **Track 4 payoff**: If the impedance calculation
  independently produces α = 1/137 from the T² geometry,
  this would be the derivation of α we've been looking
  for — not from within T⁶, but from the T⁶/R³ interface.


---

## Summary — R32 complete

### Outcome: Moderate-to-null result with one major structural insight

The study confirms that α cannot be derived from T⁶ geometry
at the current level of the model.  But it clarifies exactly
WHERE the derivation must come from.


### Track-by-track results

**Track 1 — KK mode running (null).**  If all ~78,000 charged
T⁶ modes contribute to vacuum polarization, α runs ~157,000×
faster than in the Standard Model, with a Landau pole at ~1 MeV.
This independently confirms that ghost modes must be
electromagnetically suppressed by ~10⁵ (consistent with the
Lamb shift constraint from R31 Track 4).

**Track 2 — Volume dilution (null).**  The "bare" higher-
dimensional coupling α_bare = α × r × μ₁₂² gives 1/α_bare
≈ 5 (electron) and 4 (proton) — not 1/24.  Different sheets
give different bare couplings.  The neutrino sheet volume
ratio does not explain weak interactions (off by 11 orders
of magnitude).

**Track 3 — Why 24 (moderate).**  Cataloged 8 mathematical
contexts where 24 appears.  The strongest connection to T⁶ is
the Dedekind eta function η(τ)²⁴, which is forced by modular
invariance on any torus.  But the naive T⁶ scalar partition
function contains |η|⁶, not |η|²⁴.  No combination of aspect
ratios produces 24.

**Track 4 — Impedance (structural insight).**  The 4π in the
α formula IS the 3D solid angle.  The shear sin²(2πs) provides
the dominant suppression (~1/240).  Simple geometric mechanisms
(solid angles, channel counting, Fresnel) give values of
order 1/3 to 1/11 — too large.  The weighted gauge field
partition (by 1/L²) gives 1/80, the closest match.


### The central finding

The α formula decomposes as:

    α = r²μ sin²(2πs) / (4π(2−s)²)

But the shear s is NOT independently determined.  It is
reverse-engineered from the requirement that α = 1/137
(via `solve_shear_for_alpha(r)` in lib/ma.py).  So the
formula is a tautology for computing α: it takes α as input
(through s) and returns α as output.

The formula IS valuable for separating α into physical
factors (shear leak, geometric amplification, angular
normalization), but it does not derive α from first
principles because s is a free parameter tuned to match.


### The question that remains

"Why is α = 1/137?" reduces to "why is s ≈ 0.01?"

Neither kinematic geometry (Tracks 2–4) nor spectral
self-consistency (R31 Tracks 3–6) constrains s.  The shear
requires DYNAMICS — a variational principle, modular
invariance condition, or stability requirement — to be
selected.

Possible next steps:
1. Modular invariance: does requiring the T² partition
   function to be modular-invariant constrain s?
   (η²⁴ connection from Track 3)
2. Self-consistent shear: does requiring the same α on all
   sheets constrain r and s jointly?
3. Stability: does minimizing some energy functional select s?
4. Running endpoint: the weighted gauge partition gives 1/80
   ≈ (137 + 24)/2 to 99.8%.  If α runs from 1/137 to 1/24,
   the "midpoint" coupling 1/80 might have geometric meaning
   as the scale-averaged coupling.


### Open questions promoted

- Q: Why is the weighted gauge partition 1/80 ≈ arithmetic
  mean of 1/137 and 1/24?  Is this coincidence or evidence
  that 137 and 24 are the IR and UV endpoints of a running
  whose midpoint is geometrically determined?

- Q: Can the shear be derived from modular invariance?
  The Dedekind eta function constrains which modular
  parameters τ = r + is are consistent.  Does requiring
  Δ(τ) ≠ 0 (no degenerate torus) select s?

- Q: Is the aperture ratio r × μ² (≈ 27 for electron,
  ≈ 36 for proton) related to 24 through a geometric
  correction factor?
