# R32. Findings

## Track 1 — KK mode running of α

### F1. Ma (the six-dimensional material space) has ~78,000 charged modes below 1000 TeV

With n_max = 8 for the electron/proton sheets (neutrino
excluded — correctly, since neutrino-only modes have Q = 0),
the Ma spectrum contains 78,608 charged modes.  Of these:

- 41,616 below 2 GeV  (vs ~40 known particles in this range)
- 78,608 below 1000 TeV

Classification by spin:
- 20,808 bosons (spin 0)
- 41,616 fermions (spin ½)
- 16,184 ambiguous (2×½ → spin 0 or 1)


### F2. The lightest charged Ma mode is 39 keV — not the electron

The mode (−1, 0, 0, 0, 0, 0) has charge −1 and mass
~39 keV (from the electron tube, L₁ ≈ 32,000 fm).  This
is 13× lighter than the electron.  There are 112 charged
modes below the electron mass (0.511 MeV).

These sub-electron charged modes are not observed in
nature.  The electron IS the lightest charged particle.
This is a known structural issue: on Ma_e,
modes with n₂ = 0 (no ring winding) are lighter than
(1,2) but carry charge.  The WvM spin mechanism
requires n₂ = 2 for spin ½, which is why the electron
is the lightest charged FERMION — but charged bosons
with n₂ = 0 exist at lower masses in the Ma spectrum.

These modes might be excluded by a selection rule not
yet identified (spin-statistics, stability, coupling).


### F3. Naive KK running is catastrophically fast

If all charged modes contribute to vacuum polarization
as independent quantum fields (standard one-loop QFT),
the running of 1/α is ~157,000× faster than the SM:

| Energy | SM 1/α | Ma 1/α (naive) |
|--------|--------|-----------------|
| 0 (input) | 137.0 | 137.0 |
| 0.5 MeV | 137.0 | 86 |
| 1 MeV | 137.0 | **−33** (Landau pole) |
| m_Z (91 GeV) | 127.9 | **−1,427,752** |

The Landau pole (1/α → 0) occurs at approximately 1 MeV.
This is completely incompatible with observation.

**The SM running**: Δ(1/α) = −9.1 from 0 to m_Z, from
~12 charged species (e, μ, τ, u, d, s, c, b quarks, W).

**The Ma running**: Δ(1/α) = −1,427,752 from 0 to m_Z,
from ~78,000 charged modes.


### F4. Ghost modes CANNOT contribute as independent quantum fields

This is the central finding.  The catastrophic running
provides independent confirmation of R31 Track 4:

- **R31 Track 4**: Naive KK Yukawa corrections to the
  Lamb shift exceed observation by 10⁵ → massive KK mode
  coupling must be suppressed by ≥10⁵.

- **R32 Track 1**: Naive KK vacuum polarization from the
  mode spectrum exceeds observation by ~10⁵ → massive KK
  mode contribution to running must be suppressed by a
  comparable factor.

Both results point to the same conclusion: the massive
modes of Ma do not couple to the electromagnetic field
with the same strength as the zero mode (photon).  The
ghost modes are geometrically present (they are valid
solutions of the wave equation on Ma) but electromagnetically
suppressed.


### F5. Suppression factor estimate

If each ghost mode's contribution is suppressed by a factor
κ, the total running from 0 to m_Z would be:

    Δ(1/α) = κ × (−1,427,752) ≈ −9.1  (SM value)

This gives κ ≈ 6.4 × 10⁻⁶, or suppression by a factor of
~160,000.  This is consistent with the R31 Track 4 estimate
of ≥10⁵ suppression for KK massive mode coupling.

The agreement between two independent observables (Lamb
shift and running of α) both requiring ~10⁵ suppression
is suggestive of a common geometric origin.


### F6. 1/α passes through 24 at ~1 MeV (but not as convergence)

In the naive (unsuppressed) running, 1/α drops through
~24 at approximately 1 MeV.  This is on the steep descent
to the Landau pole — not a stable convergence point.

The fact that the crossing energy (~1 MeV) is close to
the electron mass scale is notable but likely coincidental
given the catastrophic nature of the unsuppressed running.

Whether the SUPPRESSED running converges to 1/24 at some
higher energy depends on the spectrum of suppression
factors, which is not yet known.


### F7. The charge formula produces sub-electron charged modes

The charge formula Q = −n₁ + n₅ allows modes with n₁ = ±1
and all other quantum numbers zero.  These have charge ±1
and mass ~39 keV (from the electron tube circumference).
Their existence is a structural consequence of the charge
mechanism: charge requires only a single tube winding, but
the electron's mass requires both n₁ = 1 AND n₂ = 2.

Possible resolutions:
1. A selection rule (spin-statistics) excludes charged
   bosons from propagating
2. These modes are produced but instantly decay (lifetime
   ≪ any measurement)
3. They couple too weakly to be produced in any reaction
   (consistent with F4)

This is an open issue for the model.


---

## Track 2 — Volume dilution and the high-energy coupling

### F8. The dimensionless volume is r × μ₁₂²

The dimensionless area of each material sheet (area divided by
the natural unit (2πλ_C)²) reduces to a simple geometric
formula:

    A / (2πλ_C)² = r × μ₁₂(r, s)²

where r is the aspect ratio and μ₁₂ ≈ 2.01 is the
dimensionless (1,2) mode energy.  Values:

| Sheet | r | A/(2πλ)² | α_bare = α × A/(2πλ)² | 1/α_bare |
|-------|---|----------|------------------------|----------|
| Electron | 6.6 | 26.7 | 0.195 | 5.1 |
| Proton | 8.906 | 36.0 | 0.263 | 3.8 |

The "bare" coupling is approximately 1/5 (electron) and
1/4 (proton) — not 1/24 and not the same for both sheets.


### F9. Naive volume dilution does not produce 1/24

The KK volume dilution α₄ = α_D / V_dimensionless gives
α_bare values of 0.195 and 0.263 for the two sheets.
Neither is close to 1/24 (= 0.042).  The bare coupling
is approximately 5× larger than 1/24.

The two sheets give different bare couplings because they
have different aspect ratios (r_e = 6.6 vs r_p = 8.906).
In a unified theory the bare coupling should be universal.
The discrepancy means either:
1. The simple volume dilution picture is incomplete
2. The "true" higher-dimensional coupling involves
   cross-sheet geometry, not individual sheets
3. The bare coupling is not a simple volume ratio


### F10. The ring ratio L₂/L₆ = m_p/m_e (by construction)

The ratio of electron to proton ring circumferences is
L₂/L₆ = 1836.6, matching the proton-electron mass ratio
to 0.03%.  This is by construction (L ∝ 1/mass) but
confirms internal consistency.


### F11. The neutrino volume ratio does not explain weak interactions

Ma_ν is 5.7 × 10¹³ times larger than
Ma_e.  If weak interaction strength were simply
α × A_e/A_ν (volume dilution), the effective weak coupling
would be ~10⁻¹⁶ — eleven orders of magnitude too small
compared to the measured Fermi constant (G_F m_p² ≈ 10⁻⁵).

The weak interaction scale cannot be explained by simple
area-ratio dilution.  The coupling mechanism between sheets
must involve cross-shears or other geometry, not just
relative volumes.


### F12. The bare coupling depends on the aspect ratio r

Since α_bare = α × r × μ₁₂², and r_e is unconstrained,
the "bare" coupling is not uniquely determined.  At r_e = 1,
α_bare would be ≈ 0.030 (1/α_bare ≈ 34); at r_e = 6.6 it
is 0.195; at r_e = 24/μ₁₂² ≈ 5.94 it would be
α × 24 = 0.175 (1/α_bare = 5.7).

No value of r_e makes α_bare exactly 1/24.  To get
α_bare = 1/24, one would need r × μ₁₂² = 1/(24α) ≈ 5.71,
giving r ≈ 1.41.  This is within the allowed range
(r > 0.26) but has no independent motivation.


---

## Track 3 — Why 24?  Geometric relationships


### F13. Eight contexts where 24 appears in torus mathematics

A systematic survey cataloged 24 in eight mathematical
contexts.  Ranked by strength of connection to Ma:

| Context | Why 24? | Ma connection | Strength |
|---------|---------|----------------|----------|
| Dedekind η²⁴ | Modular invariance of material sheet | Each sheet has τ = r | STRONG |
| D₄ kissing number | 4D lattice geometry | 4 non-compact dims | MODERATE |
| ζ(−1) = −1/12 | Regularized sum → 24 = −2/ζ | String dimension formula | MODERATE |
| χ(K3) = 24 | 24 independent 2-cycles | T⁴ → K3 orbifold | WEAK |
| 4! = 24 | Permutations of (x,y,z,t) | Euclidean Weyl group | WEAK |
| 4 × 6 | Non-compact × material dims | Dimension counting | WEAK |
| Bosonic string c = 24 | 24 transverse dimensions | 10D vs 26D gap | WEAK |
| Torus curvature | ∫K dA = 0 by Gauss-Bonnet | No 24 emerges | NONE |


### F14. The Dedekind eta function is the strongest candidate

η(τ)²⁴ is the discriminant modular form Δ(τ), the unique
cusp form of lowest weight on SL(2,ℤ).  The exponent 24
is uniquely determined: it is the smallest power of η that
transforms without phase ambiguity under modular
transformations (τ → τ+1 gives e^(iπ/12), needing 24
copies to return to unity).

Each material sheet has a modular parameter τ_i = r_i + is_i.
If the Ma partition function must be modular-invariant
(a natural physical requirement for consistency of the
material space), factors of η²⁴ are forced to appear.
The gauge coupling normalization in string theory derives
from precisely this kind of partition function.

Concrete claim: if the Ma gauge coupling is computed
from the modular-invariant partition function, the
leading normalization should contain 1/24, making this
the origin of 1/α → 24 at high energies.


### F15. No combination of aspect ratios produces 24

Direct numerical search over simple functions of
(r_e, r_ν, r_p):

    r_e + r_ν + r_p = 20.5  (15% off)
    r_e + r_p = 15.5
    r_e × r_p = 58.8
    r × μ₁₂² = 26.5 (electron), 35.7 (proton)

No algebraic combination of the model's geometric
parameters equals 24.  If 24 enters the theory, it
does so through modular invariance or number theory,
not through the specific values of the aspect ratios.


### F16. 1/α decomposes as 24 × 5.71 or 4π × 10.9

The decomposition 1/α = 137.036 into "nice" factors:

    1/α ≈ 4π × 10.9   (10.9 ≈ 11, off by 0.9%)
    1/α ≈ 24 × 5.71   (5.71 ≈ 2π × 0.91, off 9% from 2π)
    1/α ≈ 4π² × 3.47  (3.47 ≈ π, off 10%)

None of these decompositions is exact enough to be
convincing.  The 4π × 11 approximation (= 138.23) is
the closest, off by 0.9%.  This is the well-known
"1/α ≈ 4π × 11" observation from the literature.


### F17. The Ma partition function contains |η|⁶, not |η|²⁴

For a scalar field on Ma = (material sheet)³, the partition
function is Z ∝ 1/|η(τ₁) η(τ₂) η(τ₃)|², involving
|η|⁶.  To get |η|²⁴ would require either:
- 12 scalar fields (12 × 2 = 24 powers)
- 8 transverse dimensions × 3 sheets = 24 indices
- The full gravitational partition function (21 moduli
  ≈ but not quite 24)

The gap between 6 and 24 means the simple scalar
counting does not produce η²⁴.  A more sophisticated
treatment — perhaps involving the gravitational
degrees of freedom or a worldsheet formulation — would
be needed to connect Ma directly to the discriminant
modular form.


---

## Track 4 — Impedance at the material-sheet/S (the three spatial dimensions) interface


### F18. Energy partitions by channel count are too large

The 10D metric has 55 independent components, of which
45 are off-diagonal.  These decompose into:

| Category | Count | 4D interpretation |
|----------|-------|-------------------|
| g_{μν} (non-compact, μ≠ν) | 6 | Gravity |
| g_{μi} (non-compact × compact) | 24 | Gauge fields |
| g_{ij} (within-sheet, i≠j) | 3 | Shears |
| g_{ij} (cross-sheet, i≠j) | 12 | Cross-sheet couplings |

The 24 gauge components are 3 sheets × 8 per sheet
(= 4 non-compact × 2 compact).  The EM field is ONE
gauge field (4 components out of 24).

Democratic partition: 4/45 = 1/11 (too large by ~12×).
Weighted by 1/L²: EM fraction = 0.0125 = 1/80 (still
too large by ~1.7×, but closest of any simple model).

No simple channel-counting rule reproduces α = 1/137.


### F19. The 4π in the α formula IS the 3D solid angle

The R19 formula decomposes as:

    α = r²μ sin²(2πs) / (4π(2−s)²)

With the correct shears (s_e = 0.01029, s_p = 0.00764):

| Factor | Electron | Proton | Role |
|--------|----------|--------|------|
| r² | 43.56 | 79.32 | Geometric amplification |
| μ₁₂ | 1.995 | 1.996 | Mode energy factor |
| sin²(2πs) | 4.18×10⁻³ | 2.30×10⁻³ | Shear leak (1/239, 1/435) |
| 4π(2−s)² | 49.75 | 49.88 | 3D normalization |
| **Product** | **0.00730** | **0.00730** | **= α** |

The numerator r²μ sin²(2πs) ≈ 0.363 is nearly identical
for both sheets — this must be so because both must produce
the same α, and the denominator 4π(2−s)² ≈ 4π×4 ≈ 50 is
also nearly sheet-independent.

The 4π is the solid angle of a sphere in S: energy
radiates isotropically into 3D space, and 4π is the
normalization.  This is NOT 24 or 8 — it is the
standard 3D angular factor.


### F20. Solid angle fractions are far too large to explain α

For isotropic radiation in d = 10 dimensions, the
fraction going into a k-dimensional subspace is k/d:

    S in 10D: 3/10 = 0.30  (vs α = 0.0073)
    S⁺¹ in 10D: 4/10 = 0.40

These are ~40–50× too large.  Dimensional geometry
alone cannot explain α.  The factor-of-137 suppression
comes from the shear sin²(2πs), not from how many
dimensions the energy can propagate into.


### F21. The aperture model gives 1/α ≈ 27 (close to 24)

The waveguide aperture model treats a material sheet as a 2D cavity:
the coupling depends on the area in wavelength units:

    α_aperture ≈ λ²/A = 1/(r × μ₁₂²)

For the electron sheet: 1/α_aperture ≈ 27 (= r_e × μ²).
This is tantalizingly close to 24 but depends on the
unconstrained aspect ratio r_e.  At r_e ≈ 5.94, it
would give exactly 24.  But the aperture model misses
the shear physics entirely.


### F22. The shear IS the impedance mismatch — confirmed

α is dominated by sin²(2πs), which provides a
suppression of ~1/240 (electron) or ~1/435 (proton).
The geometric factors (r², μ, 4π) modulate the coupling
but do not set its order of magnitude.

An unsheared torus (s = 0) has α = 0 regardless of
its size, shape, or the number of dimensions.  The
shear tilts the internal standing wave, breaking the
perfect cancellation of positive and negative half-cycles.
This is geometrically identical to an impedance mismatch:
the shear makes the material vacuum anisotropic, and
only the anisotropic component couples to S.

The question "why is α = 1/137?" reduces to "why is
s ≈ 0.01?"  — what selects this particular shear.


### F23. Weighted gauge field partition is closest match

When gauge field channels are weighted by 1/L_i² (energy
per unit winding), the proton sheet dominates completely
(shortest circumference → strongest gauge field).  The
EM fraction (tubes θ₁ and θ₅) is 0.0125 = 1/80.

This is within 1.7× of α = 1/137.  The remaining
discrepancy could come from the mode structure
normalization ((2−s)² factor) or wavefunction overlap.
This is the closest any simple partition model comes
to reproducing α.
