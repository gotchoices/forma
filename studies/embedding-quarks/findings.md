# R21 Findings

## Track 1: Eigenmodes on the embedded torus

**Script:** [`scripts/track1_curved_eigenmodes.py`](scripts/track1_curved_eigenmodes.py)


### F1. Curvature creates an effective potential well at the outer equator

The eigenvalue equation on the curved torus is Schrödinger-like,
with an effective potential:

    V(θ₁) = ε²n₂² / (1 + ε cos θ₁)²

This potential is minimum at the outer equator (θ₁ = 0) and
maximum at the inner equator (θ₁ = π).  The inner/outer
potential ratio grows rapidly with ε:

| ε | r = 1/ε | V_inner/V_outer | Comment |
|---|---------|-----------------|---------|
| 0.1 | 10 | 1.5 | mild |
| 0.3 | 3.3 | 3.4 | moderate |
| 0.5 | 2.0 | 9.0 | strong |
| 0.9 | 1.1 | 361 | extreme |

For n₂ ≠ 0 modes, the curvature pushes amplitude toward the
outer equator.  This is the dominant localization mechanism.


### F2. The n₁ = 0 mode localizes strongly at the outer equator

The "ground state" in the poloidal direction (n₁ = 0, n₂ = 2)
is no longer uniform on the curved torus.  Its probability
distribution |f(θ₁)|² concentrates at the outer equator:

| ε | outer/inner |f|² ratio | IPR |
|---|--------------------------|-----|
| 0.1 | 1.03 | 1.00 |
| 0.3 | 2.47 | 1.09 |
| 0.5 | 40.7 | 1.62 |
| 0.9 | >1000 | 2.03 |

At ε = 0.5 (r = 2), the mode is 40× more probable at the outer
equator than the inner.  This is NOT a perturbative correction —
it is a qualitative change in mode structure.


### F3. The ±n₁ degeneracy is lifted

On flat T², modes (n₁, n₂) and (-n₁, n₂) have the same energy.
On the curved torus, this degeneracy breaks.  The eigenmodes
become standing waves (cos n₁θ₁ and sin n₁θ₁ in the flat limit),
with different eigenvalues:

| ε | λ(cos-like) | λ(sin-like) | Splitting |
|---|-------------|-------------|-----------|
| 0.1 | 1.039 | 1.045 | 0.6% |
| 0.3 | 1.368 | 1.530 | 12% |
| 0.5 | 2.041 | 3.175 | 56% |

The cos θ₁ mode (peaks at outer and inner equator) has lower
energy than the sin θ₁ mode (peaks at sides).

**Key implication:** The electron on the curved torus is NOT a
traveling wave.  The degeneracy between e^{+iθ₁} and e^{-iθ₁}
is broken, so the eigenstates are standing waves with non-uniform
|f(θ₁)|² distributions.  Each standing wave sits at a different
angular position and would experience a different effective
geometry for the charge integral.


### F4. Eigenvalue shifts grow with curvature

| ε | Electron (1,2) shift | Regime |
|---|---------------------|--------|
| 0.01 | −0.001% | negligible |
| 0.1 | −0.06% | perturbative |
| 0.3 | +0.6% | perturbative |
| 0.5 | +2.0% | moderate |
| 0.9 | −14.8% | non-perturbative |

Corrections are perturbative for ε < 0.3 (r > 3.3) and
significant for ε > 0.5 (r < 2).  The flat-T² approximation
is good for thin tori but breaks down for fat ones.


### F5. Implications for quarks

The curvature produces three distinct effects that could enable
fractional charges:

1. **Mode localization:** The n₁ = 0, ±1 modes have different
   spatial distributions (peaked at different θ₁ positions).
   Three such modes in a proton would be three scattering
   centers at different positions.

2. **Different effective geometry:** Each standing wave samples
   a different average of the curvature-varying metric.  This
   means each mode sees a different effective a/R ratio for the
   charge integral.

3. **Charge redistribution:** On flat T², only |n₁| = 1 modes
   carry charge (R19 F30).  On the curved torus, the n₁ = 0
   mode has non-uniform |f(θ₁)|² — the charge integral may
   become nonzero.  Track 2 will test this.

The curved torus naturally provides position-dependent geometry,
which is the key ingredient missing from all previous flat-space
quark attempts (R14, R19 T4–6).


### Note: Relation to R15's σ and the derivation of α

R15 showed that α = exp(−4σ²), where σ is the angular width
of a localized wavepacket in the **toroidal** (φ / θ₂) direction.
The open question (R15 F8) was: what determines σ?

Track 1's localization is in the **poloidal** (θ₁) direction —
perpendicular to the direction R15 needed.  The embedded torus
metric preserves full θ₂ axial symmetry, so curvature alone
cannot break the φ-integral that kills charge (R15 F3).
**Shear is still required** as the charge-generating mechanism
(R19 candidate 8).

However, curvature **modifies** the charge that shear produces.
On flat T², the R19 charge formula uses plane-wave eigenmodes.
On the curved torus, the eigenmodes are standing waves with
non-uniform |f(θ₁)|² distributions (F2–F3).  These modified
profiles enter the charge integral, changing it to:

    α = α(r, s, ε)    where ε = a/R

Different modes (n₁ = 0, ±1) have different f(θ₁), so they get
**different charges from the same shear** — one shear parameter,
multiple charge values.  This is the new ingredient for quarks.

**Path to deriving α:** On flat T², α(r, s) = 1/137 is one
equation in two unknowns — it fixes s at each r, but r is free.
Adding curvature gives three unknowns (r, s, ε).  But if three
modes carry charges Q₁ = e, Q₂ = 2e/3, Q₃ = e/3, that gives
three constraints on three unknowns.  A consistent solution would
fix the geometry uniquely, deriving α from the requirement that
integer and fractional charges coexist on the same torus.


---

## Track 2: Position-dependent charge

**Script:** [`scripts/track2_position_charge.py`](scripts/track2_position_charge.py)


### F6. Odd modes carry zero charge by symmetry

The Sturm-Liouville equation is invariant under θ₁ → 2π − θ₁.
Eigenmodes are either even (f(2π−θ) = f(θ)) or odd
(f(2π−θ) = −f(θ)).  The charge overlap integral:

    C = ∫ f(θ₁) cos(θ₁) (1 + ε cos θ₁) dθ₁

vanishes exactly for odd modes (odd × even × even = odd).
**Only even modes carry charge on the curved torus**, regardless
of ε.  This is the curved-space generalization of R19's n₁ = ±1
selection rule: on the curved torus, the rule becomes "even
modes only."

Consequence: of the three modes (n₁ = 0, cos-like n₁ = 1,
sin-like n₁ = 1), only TWO carry charge (the ground state and
the cos-like mode).  The sin-like mode is always uncharged.


### F7. The ground state acquires charge on the curved torus

On flat T², the n₁ = 0 ground state has C = 0 (constant
wavefunction has zero cos θ₁ projection).  On the curved
torus, the ground state localizes at the outer equator
(where cos θ₁ = 1), acquiring nonzero charge overlap:

| ε | C(ground)/C(electron) | Comment |
|---|-----------------------|---------|
| 0.01 | 0.007 | negligible |
| 0.1 | 0.077 | small |
| 0.2 | 0.190 | growing |
| 0.3 | 0.373 | ≈ 1/3 |
| 0.5 | 0.939 | ≈ 1 |
| 0.7 | 1.000 | overtakes electron |

The charge ratio is a smooth, monotonically increasing
function of ε.  At ε ≈ 0.65, the ground state's charge
overlap EXCEEDS the cos-like n₁ = 1 mode.  Above this
crossover, the "electron" (mode with largest charge) is
the ground state, not the cos-like mode.


### F8. Charge ratios pass through 1/3 and 2/3 — but not simultaneously

Scanning ε from 0.01 to 0.95, the charge ratio C(mode)/C(electron)
passes through the target quark values:

**Ratio ≈ 1/3:**
- ε ≈ 0.28: ground state (idx=0) gives 0.33
- ε ≈ 0.52: mode idx=4 gives 0.33
- ε ≈ 0.70: mode idx=4 gives 0.33
- ε ≈ 0.84: mode idx=2 gives 0.33

**Ratio ≈ 2/3:**
- ε ≈ 0.41: ground state (idx=0) gives 0.66
- ε ≈ 0.61: mode idx=2 gives 0.68

**Critical negative result:** No single ε value gives BOTH
1/3 AND 2/3 from two different modes simultaneously.  The
ratios pass through the targets at different ε values, so a
single torus geometry cannot produce both quark charges.


### F9. Charge ratio is continuous, not quantized

The charge ratio C(mode)/C(electron) varies smoothly with ε.
It is not pinned to rational values by any topological or
algebraic mechanism.  The values 1/3 and 2/3 appear as generic
crossings, not special fixed points.

This contrasts with the S3 algebraic prediction (a/R ratios
6.60, 9.91, 19.81 mapping to e, 2e/3, e/3), which suggested
discrete fractional charges.  The curved-torus eigenmodes
produce a continuous spectrum of charge ratios with no
preferred fractionalization.


### F10. The charge overlap integral is a single integral, not the full 2D charge

**Caveat:** The calculation used a simplified charge integral
(zeroth order in shear):

    Q ∝ C(mode) × sin(2πs)/q_eff

where C(mode) = ∫ f(θ₁) cos θ₁ (1+ε cos θ₁) dθ₁ replaces the
flat-space value aπ.  The full shear-curvature coupling
(sheared curved torus with metric depending on BOTH θ₁ and θ₂)
was not computed.  The full calculation could in principle:

1. Mix modes with different n₂ (the shear breaks θ₂ symmetry)
2. Change the effective q_eff (curvature modifies the winding)
3. Introduce interference terms between modes

However, the parity selection (F6) and the continuous ratio
behavior (F9) are robust — they follow from symmetry and
smoothness, not from the perturbative approximation.


### What Track 2 establishes

**Positive:**
- Curvature DOES make charge position-dependent (F7)
- The mechanism works: different modes carry different charges
- Charge ratios CAN reach 1/3 and 2/3 at specific ε (F8)

**Negative:**
- No single ε gives both quark charges simultaneously (F8)
- Ratios are continuous, not quantized (F9)
- Only two (not three) modes carry charge (F6)
- The simplified integral (F10) may miss coupling effects

**Implication for Track 3 (three-quark proton):**  The
single-torus mechanism tested here cannot produce a proton
with two distinct fractional charges.  Either:

(a) The full shear-curvature coupling (not computed) changes
    the picture qualitatively — possible but speculative.
(b) Quarks require a DIFFERENT mechanism than position on a
    single embedded torus — e.g., modes on different T² planes
    within T³ (each plane having its own ε), or a non-WvM
    charge formula.
(c) The S3 algebraic ratios (which DO give exact fractions)
    operate through a mechanism not captured by the curved-torus
    eigenmode picture.


---

## Summary table

| # | Finding |
|---|---------|
| F1 | Curvature creates potential well at outer equator; V_inner/V_outer = 9 at ε = 0.5 |
| F2 | n₁ = 0 mode localizes: outer/inner ratio = 40:1 at ε = 0.5 |
| F3 | ±n₁ degeneracy lifts: 56% splitting at ε = 0.5; modes become standing waves |
| F4 | Eigenvalue shifts: perturbative for ε < 0.3, significant for ε > 0.5 |
| F5 | Three implications for quarks: localization, effective geometry, charge redistribution |
| F6 | Odd modes carry zero charge by symmetry; only even modes contribute |
| F7 | Ground state acquires charge on curved torus; ratio grows monotonically with ε |
| F8 | Charge ratios pass through 1/3 and 2/3 — but at different ε, never simultaneously |
| F9 | Charge ratio is continuous (not quantized); no preferred fractionalization |
| F10 | Calculation used simplified (zeroth-order shear) integral; full coupling not computed |


## Scripts

- [`scripts/track1_curved_eigenmodes.py`](scripts/track1_curved_eigenmodes.py)
  — Eigenvalues, eigenfunctions, localization on the curved embedded torus
- [`scripts/track2_position_charge.py`](scripts/track2_position_charge.py)
  — Charge overlap integrals, charge ratios, quark ratio scan
