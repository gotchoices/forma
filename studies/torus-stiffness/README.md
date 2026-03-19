# R18. Self-Consistent Geometry — Deriving α from Torus Stiffness  *(complete — negative)*

Can the photon's own electromagnetic field deform the compact
space, breaking the symmetry that protects zero charge and
thereby producing the electron's charge?  If so, α is determined
by the balance between EM pressure and the compact space's
resistance to deformation (its "stiffness").

This study works BACKWARDS from the known α = 1/137 to extract
the required stiffness, then checks whether it matches a known
physical constant.


## Motivation: what determines σ?

R15 showed that α = exp(−4σ²), where σ is the angular width
of the photon's wavepacket on the ring (F5).  The central open
question became: what determines σ ≈ 1.1 rad?

### Mechanisms ruled out

A systematic search ruled out all "internal dynamics" candidates:

**1. Coulomb soliton (R15 F9).**  The Coulomb self-energy of any
charge distribution is ∫ε₀E²/2 dV ≥ 0 — always positive, always
repulsive.  Both U_kinetic and U_Coulomb decrease as σ increases,
so U_total is monotonically decreasing toward σ = ∞.  No finite-σ
equilibrium exists.

**2. Centrifugal pressure (R17).**  The centrifugal force is
exactly perpendicular to velocity (no along-path component for
clumping).  Width breathing is conservative.  Two-pass cancellation
preserves φ-symmetry.  The centrifugal force is a consequence of
confinement, not a free mechanism.

**3. Magnetic self-interaction.**  Same issue as Coulomb:
∫B²/(2μ₀)dV ≥ 0, always positive.

**4. Gravitational self-interaction.**  Attractive (right sign!)
but U_grav ~ Gm²/R ~ 10⁻⁵⁷ J, which is 10⁻⁴³ times too weak.

### The φ-symmetry protection

The deeper issue is that on any AXISYMMETRIC torus, the charge
of a delocalized wave is exactly zero:

    Q = ε₀ ∫₀²π ∫₀²π cos(θ+2φ) × a(R + a cos θ) dθ dφ

The θ integral: ∫ cos(θ+2φ)(R + a cos θ)dθ = aπ cos(2φ)
Then: ∫ cos(2φ) dφ = 0

This zero is PROTECTED by the φ-translational symmetry of the
torus.  No amount of curvature-induced mode mixing can break it,
because the curvature depends only on θ (not φ).  This also
means R16's energy-partition approach (on a symmetric embedded
torus) cannot produce charge.

### Breaking the symmetry: geometric deformation

The only surviving mechanism: break the φ-symmetry of the torus
itself.  If the torus has a cos(2φ) modulation in its major
radius:

    R → R + δ cos(2φ)

then the metric acquires φ-dependence, modes with different q
values couple, and the charge integral can become nonzero.


## The mechanism: mode coupling through deformation

### How deformation produces charge

On the undeformed torus, the photon is in the (p,q) = (1,2)
mode: ψ = cos(θ + 2φ).  This mode has zero charge.

A cos(2φ) deformation of the major radius couples modes with
Δq = ±2.  The (1,2) mode couples to the (1,0) mode:

    ψ ≈ cos(θ + 2φ) + ε cos θ

where ε is the coupling amplitude, proportional to δ/R.

The (1,0) mode (cos θ) has NONZERO charge:

    Q_{1,0} = ε₀ E₀ ∫∫ cos θ × a(R + a cos θ) dθ dφ
            = ε₀ E₀ × a × aπ × 2π
            = 2π² ε₀ E₀ a²

So the mixed mode has charge:

    Q = 2π² ε₀ E₀ a² × ε

Setting Q = e determines ε, and from ε we get δ, and from δ
we get the stiffness κ.

### The self-consistency loop

    cos(2φ) deformation  →  (1,2)↔(1,0) mode coupling
           ↑                        ↓
       stiffness κ            cos(2φ) EM pressure
           ↑                        ↓
       restoring force  ←  energy density with cos(2φ)

If the EM pressure from the coupled mode REINFORCES the original
deformation (positive feedback), the symmetric torus is unstable
and the system flows to a finite-deformation equilibrium.  The
equilibrium amplitude determines the charge and hence α.


## Tracks

### Track 1. Backwards calculation — stiffness from known α

Work backwards from α = 1/137 to extract the required stiffness
of the compact space.

**Method:**

1. **Energy normalization.**  The photon has energy m_e c².
   ½ε₀∫E²dV = m_e c²/2 determines E₀.

2. **Required coupling.**  Q = e = 2π² ε₀ E₀ a² × ε.
   Solve for ε.

3. **Perturbation theory.**  The cos(2φ) deformation with
   amplitude δ produces coupling ε through the matrix element:
   ε = <ψ_{1,0}|ΔH|ψ_{1,2}> / (E_{1,2}² − E_{1,0}²) × δ
   Compute the matrix element from the torus Laplacian.
   Solve for δ.

4. **EM driving pressure.**  The mode perturbation creates a
   cos(2φ) energy density.  Compute the resulting radiation
   pressure P_drive on the torus surface.

5. **Stiffness.**  κ = P_drive / δ  (force balance at
   equilibrium).

6. **Identification.**  Express κ in terms of fundamental
   constants.  Check whether κ matches or involves ε₀, μ₀,
   ℏ, c, m_e, or simple combinations thereof.

**Expected difficulty:** Medium.  The main computation is the
perturbation matrix element, which requires discretizing the
Laplacian on the embedded torus.

### Track 2. Forward energy balance  *(complete — negative)*

Compute the total energy E_total(δ) = E_photon(δ) + E_Coulomb(δ)
to determine whether deformation is energetically favorable.

**Result:** NEGATIVE.  The Coulomb cost of the charge exceeds
the photon energy saving by ~96×.  The symmetric torus is the
energy minimum.  See findings F5–F7.

### Track 3. Self-consistent equilibrium  *(cancelled)*

Track 2's negative result makes this unnecessary.


## What could go wrong

- **Mode coupling gives zero charge.**  The perturbation theory
  might show that the (1,2)→(1,0) coupling vanishes due to a
  symmetry I haven't identified.  This would be a clean negative.

- **Wrong sign (stabilizing).**  The EM pressure from the mode
  coupling might OPPOSE the deformation (negative feedback).
  The symmetric torus is then the stable equilibrium → zero
  charge → negative result.

- **Right sign but wrong magnitude.**  The instability exists
  but the equilibrium δ gives α ≠ 1/137.  This would mean
  the mechanism is correct but the model needs refinement.

- **Stiffness is unrecognizable.**  The backwards calculation
  gives a stiffness that doesn't match any known constant or
  combination.  This isn't fatal — it could be a new prediction
  of the model — but it's less satisfying.


## What would success look like

- **Strong:** The backwards calculation gives κ expressible in
  terms of ε₀, μ₀, c, ℏ, or simple combinations.  This would
  identify the compact space's stiffness with a known vacuum
  property.  If the forward calculation (Track 2) also shows
  instability, this is a first-principles derivation of α.

- **Promising:** The stiffness is a clean function of the torus
  geometry (powers of a, R, r).  Even without matching a known
  constant, this constrains the model.

- **Negative:** The mechanism doesn't work (wrong sign, zero
  coupling, or no self-consistent solution).  This rules out
  geometric deformation as the σ-determining mechanism and
  sends us back to the drawing board.


## Connections

- **R15** — provides F5 (α = exp(−4σ²)) and the σ question
  (F8).  Track 5 ruled out the Coulomb soliton (F9).
- **R16** — the energy-partition approach.  R18 explains why
  R16 needs deformation: φ-symmetry protection kills charge
  on an axisymmetric torus.  If R18 succeeds, R16's question
  is answered through the mode-coupling mechanism.
- **R17** — ruled out centrifugal pressure.
- **R7** — U_Coulomb = α × m_e c² (the energy scale).
- **Q18** — master question: can α be derived from geometry?
- **Q52** — what determines the aspect ratio r?

## References

- R15 findings: [`forward-charge/findings.md`](../forward-charge/findings.md)
- R17 findings: [`radiation-pressure/findings.md`](../radiation-pressure/findings.md)
- R7 findings: [`torus-capacitance/findings.md`](../torus-capacitance/findings.md)
- R16 plan: [`harmonic-charge/README.md`](../harmonic-charge/README.md)
