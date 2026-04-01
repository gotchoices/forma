# R44: Anomalous magnetic moment from torus geometry

**Status:** Framed
**Questions:** Q53 (anomalous magnetic moment), Q34 (α derivation)
**Type:** compute
**Depends on:** R19 (shear-charge formula, charge density on torus),
R8 (g = 2 from topology, F8–F11), R40 (pressure profile, embedding curvature)

---

## Motivation

MaSt gives g = 2 from topology: the photon is spin-1 (ℏ), the electron
is spin-½ (ℏ/2), and their ratio is 2 (R8 F9).  This is geometry-independent.

The measured value is g ≈ 2.00232.  The anomalous part:

<!-- a_e = (g − 2)/2 ≈ α/(2π) ≈ 0.00116 -->
$$
a_e = \frac{g - 2}{2} \approx \frac{\alpha}{2\pi} \approx 0.001\,16
$$

is known experimentally to 0.24 ppb.  QED derives it from virtual
photon loops to 12 significant figures.

WvM attribute the anomalous moment to a "non-co-rotating field fraction"
but never computed it from the geometry.  R8 F8 showed the classical
current-loop approach fails — g is a quantum property, not derivable
from μ = IA.  So the topological argument gives g = 2 exactly, and
the anomalous part must come from something else.

**This study asks:** does the anomalous moment emerge from the
*geometry* of the (1,2) mode on the sheared, embedded torus — not
from virtual photon loops and not from a vague "field fraction," but
from two concrete, computable effects?

---

## Two mechanisms for g ≠ 2

### Mechanism 1: Charge-mass separation from shear

The topological g = 2 rests on the classical gyromagnetic relation
μ = (e/2m)L, which assumes charge and mass are co-located.  On
the sheared torus, they are NOT.

The R19 shear mechanism produces charge through a non-uniform
projection of the E-field into 3D.  The local charge density
σ(θ₁, θ₂) is concentrated where the shear-broken symmetry allows
the field to couple to 3D — it peaks at specific angular positions
on the torus surface.

Meanwhile, the energy density (mass) is *uniform* on the flat torus:
u(θ₁, θ₂) = const.

This charge-mass separation shifts the effective gyromagnetic ratio:

- **Magnetic moment** weights the charge distribution:
  μ_z ∝ ∫ ρ²(θ₁, θ₂) × σ(θ₁, θ₂) × v dA
  (where ρ is the distance from the symmetry axis)

- **Angular momentum** weights the energy distribution:
  L_z ∝ ∫ ρ(θ₁, θ₂) × u(θ₁, θ₂) × v dA

If σ is concentrated at larger radii (outer equator of the torus),
the charge-weighted moment gets a *boost* relative to the mass-weighted
angular momentum.  This gives g > 2.

**This is non-tautological:** the charge distribution was computed
in R19 to match one observable (total charge = e).  Now we use that
*same* distribution to compute a *different* observable (magnetic
moment).  If g − 2 ≈ α/π falls out, it is a genuine prediction.

### Mechanism 2: The (1,2) torus knot wobble

The (1,2) geodesic on the embedded torus is not a planar circle —
it is a torus knot that wobbles above and below the equatorial plane:

```
x(t) = (R + a cos t) cos 2t
y(t) = (R + a cos t) sin 2t
z(t) = a sin t
```

The pitch angle is arctan(r/2).  For r = 0.5 this is ~14°; for
r = 1 it is ~27°.  The 3D embedding curvature means the current
path samples different radii ρ = R + a cos θ₁ as it winds, and
the contribution to the magnetic moment scales as ρ² (not ρ),
giving a non-linear weighting.

R40 quantified the pressure non-uniformity from this embedding:
the k=2 (elliptical) Fourier component is 37% of the mean (F3).
This is a large geometric effect, though the actual shape deformation
is small (δr/a ≈ 7×10⁻⁴) because the restoring force is stiff.

The embedding correction is secondary to the shear mechanism but
provides a well-defined perturbative contribution.

---

## The computation

### What we compute

For a given point (r, s(r)) on the α-curve:

1. **Charge density** σ(θ₁, θ₂) from R19's Gauss's-law integral —
   the E-field normal component projected into 3D through the sheared
   torus surface.

2. **Energy density** u(θ₁, θ₂) — uniform on the flat torus (the
   mode ψ = exp(i(θ₁ + 2θ₂)) has |ψ|² = const).

3. **Mode velocity** v(θ₁, θ₂) — uniform on the flat torus, directed
   along the geodesic tangent (ê₁ + 2ê₂)/|ê₁ + 2ê₂|.

4. **3D embedding** — map (θ₁, θ₂) → (x, y, z) using the standard
   torus embedding with parameters R(r) and a(r) = r × R(r).

5. **Magnetic dipole moment:**

<!-- μ_z = (1/2) ∫ (r × K)_z dA, where K = σ × v -->
$$
\mu_z = \frac{1}{2} \int ({\bf r} \times {\bf K})_z \, dA
\qquad\text{where } {\bf K} = \sigma\, {\bf v}
$$

6. **Field angular momentum:**

<!-- L_z = ε₀ ∫ (r × (E × B))_z d³x -->
$$
L_z = \varepsilon_0 \int ({\bf r} \times ({\bf E} \times {\bf B}))_z \, d^3x
$$

   On the torus surface: L_z ∝ ∫ ρ × u × v dA.

7. **Extract g** from g = 2m_e μ_z / (e S_z) where S_z = L_z / 2
   (the spin is half the photon's angular momentum, from the 1:2
   winding topology).

### What we compare to

| Quantity | Value | Source |
|----------|-------|--------|
| a_e (experimental) | 0.001 159 652 181 28(18) | 2023 measurement |
| a_e (QED 1st order) | α/(2π) = 0.001 161 41... | Schwinger 1948 |
| a_e (QED 5th order) | 0.001 159 652 182 032(720) | Aoyama et al. 2019 |

---

## Tracks

### Track 1: Charge density on the sheared torus

Compute σ(θ₁, θ₂) from R19's charge mechanism.  The shear s breaks
the φ-symmetry of the (1,2) mode.  The E-field has a non-zero normal
component at the torus surface that varies with position.

Verify: ∫ σ dA = e (total charge).
Map σ(θ₁, θ₂) — where is charge concentrated?  Inner vs outer
equator, poles vs equator.

**Output:** charge density map and its Fourier decomposition.

### Track 2: Magnetic moment from charge-weighted current

Embed the torus in 3D.  Compute the surface current K = σ v and
the magnetic dipole moment μ_z = (1/2) ∫ (r × K)_z dA.

Separately compute L_z from the energy-weighted current.

Extract g(r) across the α-curve (r from 0.54 to ~10).

Three possible outcomes:

| Outcome | Implication |
|---------|-------------|
| g − 2 ≈ α/π, r-dependent | Pins r_e.  The shear that gives charge also gives the anomalous moment. |
| g − 2 ≈ α/π, r-independent | Valid derivation of Schwinger, but can't pin r_e.  Still major. |
| g − 2 ≠ α/π | Charge-mass separation is not the mechanism.  Informative negative. |

**Output:** g(r) plot across the α-curve.

### Track 3: Embedding curvature correction

Add the 3D embedding effects.  The embedded torus has non-uniform
curvature (R40 F1–F4): the radial coordinate ρ = R + a cos θ₁
varies around the tube.  The current at the outer equator
(ρ = R + a) encloses more area than the current at the inner
equator (ρ = R − a), and area enters μ as ρ².

Recompute g(r) with the full embedded geometry.  Compare the
embedding correction to QED's second-order coefficient:

<!-- a_e^(2) = −0.3285 (α/π)² -->
$$
a_e^{(2)} = -0.328\,478\,965\ldots\;\left(\frac{\alpha}{\pi}\right)^2
$$

**Output:** Δg from embedding vs QED 2nd order.

### Track 4: Shear scan — does g(r) pin r_e?

If Track 2 or 3 shows r-dependence, scan the α-curve to find
r* where g(r*) matches the experimental value.  Extract s(r*)
and compute α(r*, s*) from R19.

If r* exists and α comes out right, MaSt derives both g−2 and α
from geometry with zero free parameters.

**Output:** r* (if it exists), predicted α.

---

## Key formulas

**The R19 α-formula** (F1, F6, F13):

<!-- α = r² sin²(2πs) / (4π(2−s)² √(r²(1+2s)² + 4)) -->
$$
\alpha = \frac{r^2 \sin^2(2\pi s)}{4\pi\,(2 - s)^2\,\sqrt{r^2(1+2s)^2 + 4}}
$$

For each r > r_crit ≈ 0.54, a unique s(r) gives α = 1/137.036.

**The flat-torus metric** with shear s:

<!-- ds² = a²(dθ₁ + s dθ₂)² + R²dθ₂² -->
$$
ds^2 = a^2\,(d\theta_1 + s\,d\theta_2)^2 + R^2\,d\theta_2^2
$$

**The (1,2) torus knot** embedded in 3D:

```
r(t) = ((R + a cos t) cos 2t,  (R + a cos t) sin 2t,  a sin t)
```

Path length on flat torus: L = 2π√(a² + 4R²) = λ_C.

Embedded path length: L_3D = ∫₀²π √(a² + 4(R + a cos t)²) dt ≠ L.
The photon sees the flat metric (energy = hc/L), but the 3D observer
sees the embedded current distribution (moment from L_3D path).
This flat-vs-embedded mismatch is a source of g ≠ 2.

---

## What success looks like

| Outcome | Value |
|---------|-------|
| g − 2 ≈ α/π from charge-mass separation | First non-QED derivation of the Schwinger result |
| r-dependence that pins r_e | Eliminates MaSt's last free electron-sector parameter |
| Embedding correction matches (α/π)² | Connects torus curvature to QED's 2nd-order term |

## What failure looks like

| Outcome | What it means |
|---------|--------------|
| g = 2 exactly (no correction from shear) | Charge distribution too symmetric to shift the moment |
| g − 2 has wrong sign or wrong order of magnitude | Charge-mass separation is not the mechanism for the anomalous moment |
| g − 2 correct but r-independent | Still a valid result; r_e must be pinned by another observable |

Either way, the computation is well-defined, non-tautological, and
the result is informative.

---

## Files

| File | Description |
|------|-------------|
| `README.md` | This file — study design |
| `scripts/track1_charge_density.py` | Charge density σ(θ₁,θ₂) from R19 shear mechanism |
| `scripts/track2_magnetic_moment.py` | Charge-weighted vs mass-weighted moment; g(r) |
| `scripts/track3_embedding.py` | 3D curvature correction to g |
| `scripts/track4_pin_r.py` | Scan α-curve for r* matching experimental g−2 |
| `findings.md` | Results and interpretation |
