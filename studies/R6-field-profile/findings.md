# R6. Guided-Wave Field Profile — Findings

## F1. The self-consistency problem

### Where R comes from (the path-length constraint)

The photon follows a (1,2) torus knot: it winds once around the
minor circle (circumference 2πa) for every two trips around the
major circle (circumference 2πR).  One full circuit traces a
helical path of total length:

    ℓ = √( (2 × 2πR)² + (1 × 2πa)² )
      = 2π √(4R² + a²)

For resonance (standing wave), this path must equal one Compton
wavelength: ℓ = λ_C.  Solving for R:

    R = λ_C / (2π√(4 + r²))                ... (1)

where r = a/R is the aspect ratio.

**In the thin-torus limit** (r → 0, i.e. a ≪ R), equation (1)
gives R → λ_C/(4π) ≈ 1.93 × 10⁻¹³ m.  This is the value WvM
used and S2 adopted.

**But S2 found r = 6.60**, which is far from zero.  Plugging
r = 6.60 into (1) gives R ≈ 5.60 × 10⁻¹⁴ m — about 3.4× smaller
than S2's assumed R.

### Why this matters

S2's charge formula (F2 below) depends on R.  S2 derived r from
that formula using R = λ_C/(4π), but the resulting r = 6.60
changes R via equation (1).  The two assumptions are circular:
S2 used a thin-torus R to derive a fat-torus r, without checking
that the fat torus still has that R.  It doesn't.


## F2. How WvM computes charge (and its limitations)

### The WvM energy-balance argument

WvM do not solve Maxwell's equations for the photon's field.
Instead, they use an energy-balance shortcut:

1. The photon has energy E = hc/λ_C.  Half is in the E-field:
   U_E = hc/(2λ_C).
2. Assume this energy fills a volume V with a uniform field.
   Energy density: u = U_E/V.  Field strength: E² = u/ε₀.
3. Match this average field to the Coulomb field at a radius R:
   E_avg = q/(4πε₀R²).
4. Solve for q.

WvM originally used a sphere of diameter λ_C (volume V_sphere),
giving q ≈ 0.91e.  S2 replaced this with a torus of volume
V = 2π²Ra² and found q = e when a/R = 1/√(πα).

### The formula

With torus volume V = 2π²Ra² and matching radius r_c = R:

    q² = 16π²ε₀ R⁴ hc / (λ_C V)
       = 16π²ε₀ R⁴ hc / (λ_C × 2π²Ra²)
       = 8 ε₀ R³ hc / (λ_C a²)             ... (2)

### What this is NOT

This is not a rigorous field calculation.  The proper way to
determine charge is Gauss's law: integrate the electric field
over any closed surface surrounding the particle:

    ∮ E · dA = q / ε₀

This is exact and independent of the field distribution inside.
WvM's approach instead asks: "what point charge would produce
a Coulomb field matching the average field strength at radius R?"
This is an estimate, not a derivation.  It depends on two
arbitrary choices:

- **V** — the volume over which the field is averaged
- **R** — the radius where the average is matched to Coulomb

A rigorous treatment would solve for the actual EM mode on the
torus, evaluate the far-field (r ≫ a), and extract the monopole
moment.  That far-field monopole moment IS the charge, with no
assumptions needed.  This remains an open problem (→ R6-next).

### Self-consistent equation

Despite its limitations, we can still ask: what geometry makes
the WvM formula give q = e self-consistently?

Setting q = e in (2) and writing a = rR:

    e² = 8 ε₀ R hc / (λ_C r²)
    r² = 4R / (α λ_C)                      ... (3)

Substituting the path constraint R = λ_C/(2π√(4 + r²)) from (1):

    r² = 4 / (α λ_C) × λ_C / (2π√(4 + r²))
    r² √(4 + r²) = 2/(πα) ≈ 87.24          ... (4)

This is a single equation in r with no free parameters.


## F3. The self-consistent solution

Solving (4) by Newton's method:

    r = a/R ≈ 4.292
    R ≈ 8.155 × 10⁻¹⁴ m
    a ≈ 3.500 × 10⁻¹³ m

Compare S2's values (using R = λ_C/(4π)):

| Quantity | S2 value       | Self-consistent | Ratio |
|----------|----------------|-----------------|-------|
| r = a/R  | 6.60           | 4.29            | 0.650 |
| R        | 1.931 × 10⁻¹³  | 8.155 × 10⁻¹⁴  | 0.422 |
| a        | 1.275 × 10⁻¹²  | 3.500 × 10⁻¹³  | 0.275 |

Verification: with these values, `q/e = 1.000000` and the
path length equals `λ_C` to machine precision.

S2's values are only valid in the thin-torus limit (`r → 0`,
`R → λ_C/(4π)`).  For a physical torus with `r > 0`, the
self-consistent solution gives a smaller R and a smaller a.


## F4. Spindle torus geometry

The self-consistent `r = a/R ≈ 4.29` means `a > R`, which is a
**spindle torus** — a self-intersecting surface in 3D Euclidean
space.  This is not a problem for the material-dimension picture:
the flat Ma_e (the electron sheet) (rectangle with opposite sides identified) has no
such restriction.  The spindle shape is an artifact of embedding
Ma_e into ℝ³ as a torus of revolution.

The 3D visualization shows a self-intersecting surface, but the
physics lives on the flat 2D manifold, where the photon simply
traverses a rectangle.  The ratios `r ≈ 4.29` or `r ≈ 6.60` both
correspond to tall, narrow rectangles — qualitatively similar.


## F5. Profile shape matters

The charge formula depends on the *effective volume* V_eff,
which in turn depends on the field profile shape.  For a
self-consistent R ≈ 8.155 × 10⁻¹⁴ m:

| Profile      | V_eff formula       | σ for q = e       | σ/R   |
|--------------|---------------------|-------------------|-------|
| Uniform      | 2π²Rσ²              | 3.500 × 10⁻¹³ m  | 4.29  |
| Gaussian     | πσ²λ_C              | 1.609 × 10⁻¹³ m  | 1.97  |
| Exponential  | (π/2)σ²λ_C          | 2.275 × 10⁻¹³ m  | 2.79  |

The profile width σ varies by a factor of ~2 depending on the
assumed shape.  All three yield `q = e` exactly — they just need
different σ values.  The uniform profile gives σ = a (by
construction); the others give narrower field extents.

This means the "correct" a/R depends on what the field actually
looks like.  The uniform-field assumption is convenient but not
necessarily physical.


## F6. Fresnel zone connection

The Fresnel zone radius — the transverse diffraction scale for a
wave curving along a path of radius R — is:

    σ_Fresnel = √(λ_C × R)                 ... (5)

With self-consistent R:

    σ_Fresnel = √(2.426 × 10⁻¹² × 8.155 × 10⁻¹⁴)
              = 4.448 × 10⁻¹³ m

This is 1.27× the self-consistent `a` (uniform profile) and
2.76× the Gaussian σ.  Same order of magnitude, but not an
exact match for any profile.

S2 noted that `a_S2/√(λ_C R_S2) = 1/(2π√α) ≈ 1.86` — close
to but not equal to 1.  This ratio is exact (analytically
`1/(2π√α)`), but the fact that it's not 1 means the Fresnel
zone is not the mechanism that sets `a`.

**Conclusion:** The Fresnel zone is in the right ballpark but
does not precisely predict the field extent for any of the
profiles tested.  The actual profile must come from solving the
wave equation.


## F7. What changed from S2 and R2

| Study | Assumed R            | r = a/R | a               |
|-------|----------------------|---------|-----------------|
| S2    | λ_C/(4π) (WvM limit) | 6.60    | 1.275 × 10⁻¹² m |
| R2    | From path constraint | 6.60    | 3.695 × 10⁻¹³ m |
| R6    | Self-consistent      | 4.29    | 3.500 × 10⁻¹³ m |

S2 and R2 used the same `r = 6.60` but different R values, so
they got different `a` values.  Neither was self-consistent: S2
used the wrong R, and R2 adopted S2's `r` without re-deriving it
with the actual R.

R6 solves both equations simultaneously, getting `r ≈ 4.29`.  The
resulting `a ≈ 3.50 × 10⁻¹³ m` is close to R2's value because
the `a = rR` product is less sensitive than the individual factors.


## F8. Implications and open questions

**What holds:**
- The electron still has zero free continuous parameters (given
  the (1,2) topology and the WvM charge mechanism)
- Spin ℏ/2 is topological and unaffected
- The g-factor depends on α, not geometry
- The path-length = λ_C resonance condition is exact

**What changes:**
- The aspect ratio shifts from 6.60 to 4.29
- R and a both get smaller
- The geometry is still a spindle torus (a > R)

**Open questions:**
1. The charge formula itself (uniform field matched to Coulomb at
   R) is a rough approximation.  What does the actual EM mode
   look like on this geometry?
2. Does the wave equation on a torus select a specific profile
   (Gaussian, Bessel, etc.) that would pin down σ/R independently?
3. Are there higher-order modes with different σ values that could
   correspond to fractional charges (quarks)?  → R11
4. Does solving the wave equation predict α rather than treating
   it as an input?  → R8


## Scripts

- [`scripts/field_profile.py`](scripts/field_profile.py): Self-
  consistency analysis, profile comparison, Fresnel zone check.
  Run: `python3 studies/R6-field-profile/scripts/field_profile.py`
