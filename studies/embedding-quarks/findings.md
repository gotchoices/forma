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


---

## Summary table

| # | Finding |
|---|---------|
| F1 | Curvature creates potential well at outer equator; V_inner/V_outer = 9 at ε = 0.5 |
| F2 | n₁ = 0 mode localizes: outer/inner ratio = 40:1 at ε = 0.5 |
| F3 | ±n₁ degeneracy lifts: 56% splitting at ε = 0.5; modes become standing waves |
| F4 | Eigenvalue shifts: perturbative for ε < 0.3, significant for ε > 0.5 |
| F5 | Three implications for quarks: localization, effective geometry, charge redistribution |


## Scripts

- [`scripts/track1_curved_eigenmodes.py`](scripts/track1_curved_eigenmodes.py)
  — Eigenvalues, eigenfunctions, localization on the curved embedded torus
