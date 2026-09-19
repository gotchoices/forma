# Analytic dispersion of the (x,c) scatter (Ch 3) — closed form, derivation-ready

**Result: the dispersion is closed-form and everything Ch 3 claims falls out
exactly.** No fit needed. Ch 3 is **fully derivation-ready.**

## The eigenvalue condition

Per tick a plane wave e^{i(kx·x + kc·c − ω t)} evolves by M = P·S, with
S = ½J − I (N=4) and P = diag(e^{iα}, e^{−iα}, e^{iβ}, e^{−iβ}), α≡kx, β≡kc.
Write a state a=(a₀..a₃), σ=Σa_d. Then S a = ½σ𝟙 − a, so the eigenproblem
M a = λ a is (P+λI)a = ½σ P𝟙, giving a = ½σ (P+λI)⁻¹P𝟙 and the scalar condition

    1 = ½ 𝟙ᵀ(P+λI)⁻¹ P𝟙  ⇔  λ Σ_d 1/(phase_d+λ) = 2.

Pairing the ±α and ±β terms and substituting λ = e^{−iω} (|λ|=1, M unitary), each
pair simplifies: λ(λ+cosα)/(λ²+2λcosα+1) = ½ − i sinω / [2(cosω+cosα)] (and
likewise for β). The condition 1 = (½ − i…) + (½ − i…) forces the imaginary part to
vanish:

> **cos ω = −(cos kx + cos kc)/2.**    ← the exact GRID dispersion

## Everything Ch 3 claims, derived

The propagating modes sit at the band edge ω≈π; the physical frequency is
**Ω = π − ω**, so cos ω = −cos Ω and the relation is **cos Ω = (cos kx + cos kc)/2**.

- **Photon (kc=0):** cos Ω = (cos kx + 1)/2. Small kx: 1 − Ω²/2 ≈ 1 − kx²/4 ⇒
  **Ω = kx/√2** — massless, with **lattice light-speed c = 1/√2 ≈ 0.7071.**
  (Measured fit: 0.7007 — a windowed slope of a curving band; and at kx=0.394 the
  formula gives Ω=0.2766 vs the time-FFT's 0.2765. Exact.)
- **Massive (kc=2πn/nc):** small kx,kc: 1 − Ω²/2 ≈ 1 − (kx²+kc²)/4 ⇒
  **Ω² = c²kx² + ω₀²**, with **c = 1/√2** and the **KK mass tower**
  **ω₀(n) = c·kc = n·(2π/nc)/√2.** (n=1, nc=24 → 0.1851; measured 0.1849. Exact.)
- **Relativistic + de Broglie:** Ω² = c²k² + ω₀² is the relativistic dispersion;
  hence v_phase·v_group = (Ω/k)(c²k/Ω) = **c²** — de Broglie phase harmony, and
  **λ = h/p** — with **no** posit beyond the linear scatter and a compact
  *coordinate* (KK). (Unlike Ch 2, this needs no phase premise.)

## The d-axis generalization — and the trap inside it

The scalar condition above was written for N = 4 registers, i.e. **two** lattice
axes. The derivation never used that number, so it generalizes directly: for **d**
axes (N = 2d registers) the same steps give λ Σ_d 1/(phase_d + λ) = N/2 = **d**.

Pairing the ±k_a registers of each axis and substituting λ = e^{−iω} turns each
pair into (cos k_a + λ)/(cos k_a + cos ω), so the condition reads
Σ_a (cos k_a + λ)/(cos k_a + cos ω) = d. Subtracting d from both sides leaves
(λ − cos ω)·Σ_a 1/(cos k_a + cos ω) = 0, and since λ − cos ω = −i sin ω, every
propagating mode (sin ω ≠ 0) obeys

<!-- sum_a 1/(cos k_a + cos omega) = 0 -->
$$
\sum_{a=1}^{d} \frac{1}{\cos k_a + \cos\omega} \;=\; 0
$$

**This is the exact relation for any d — and it is *not* a mean of cosines.** For
d = 2 it happens to reduce to one: 1/A + 1/B = 0 forces A + B = 0, which is
cos ω = −(cos k₁ + cos k₂)/2, the result above. That reduction is a **d = 2
accident**. For d = 3 the relation is a quadratic in cos ω with two branches, and
the lattice is **anisotropic** — c² = 2/3 along an axis, and 1/2 *and* 1/6 along a
face diagonal (two propagating branches: the medium is birefringent off-axis).

**Consequence for any future three-axis work.** Writing
cos Ω = (Σ_a cos k_a)/d for d ≥ 3 under this register labeling is wrong. A
three-axis run in [dualslit-matter-result.md](dualslit-matter-result.md) made
exactly that generalization and had to be corrected; see
[../review.md](../review.md).

### Two register conventions

The repo carries two update rules that coincide at d = 2 and diverge beyond it:

| | rule | exact dispersion | band | d ≥ 3 |
|---|---|---|---|---|
| **legacy** (this file, [cylinder.py](../scripts/cylinder.py), [grid_dispersion.py](../scripts/grid_dispersion.py)) | registers labelled by direction of travel, out[d] = V − in[d] | Σ_a 1/(cos k_a + cos ω) = 0 | ω ≈ π, so Ω = π − ω | anisotropic, birefringent |
| **canonical** ([grid-duality/models/scattering.md](../../grid-duality/models/scattering.md)) | registers are edge end-registers, out[d] = V − in[−d], then each edge swaps ends | cos ω = (Σ_a cos k_a)/d | ω ≈ 0, so Ω = ω | isotropic, one branch |

At d = 2 the two give the same *dispersion*, related by Ω ↔ π − ω. **Every
two-axis relation in this project is therefore convention-independent** —
including everything on this page: the light speed c = 1/√2, the KK mass tower,
the relativistic form, and de Broglie. Only the three-axis two-slit lab of Ch 7
has a convention-sensitive *relation*, and it now runs on the canonical rule.

**One trap survives at d = 2, though: the band placement differs.** The legacy
band sits at ω ≈ π and the canonical band at ω ≈ 0, so the same numerical drive
frequency selects a *different physical Ω* under each rule — and a drive that is
comfortably in-band for one can be off-band, or reachable only through large-k
zone-corner modes, for the other. Any run must therefore state which convention
it used, even in two axes. A live instance is logged in
[dual-slit-result.md](dual-slit-result.md): its 2D lab at ω = 0.5 has **no
on-axis propagating mode** under the legacy rule, and the wavelength assumed
there does not describe the wave that actually propagates.

## Status

**Ch 3 is fully derivation-ready** and stronger-footed than Ch 2: the exact
dispersion cos ω = −(cos kx+cos kc)/2 follows from the bare scatter; the light
speed 1/√2, the KK mass tower, the relativistic form, and de Broglie are all exact
consequences, confirmed to the digit by the numerics. **[D]**
