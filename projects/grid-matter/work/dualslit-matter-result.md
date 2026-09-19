# Two-slit: photon vs matter wave — the matter case runs (Ch 7, Q1 fix)

Sim: [`../scripts/dualslit.py`](../scripts/dualslit.py). Figures
[`../outputs/dualslit_photon.png`](../outputs/) and
[`../outputs/dualslit_matter.png`](../outputs/), with the one-slit controls
[`../outputs/dualslit_photon_1slit.png`](../outputs/) and
[`../outputs/dualslit_matter_1slit.png`](../outputs/).

**Revised 2026-09-18** after [`../review.md`](../review.md) found that the
original three-axis run used an assumed dispersion relation that is not the one
its update rule obeys. The lab now runs on the **canonical** scatter, which *is*
isotropic in three axes and for which the mean-of-cosines relation is exact. The
wavelengths are additionally **measured**, not only predicted. §Revision record
below says what moved.

## Why this exists

The original two-slit sim was a **massless** 2D (x,y) field — the photon/Maxwell
sector GRID already has. Calling its interference a "matter wave / de Broglie λ"
was a category slip (review-5-10.md, Q1). This fix adds a **compact c-axis** (N=6,
c periodic) so the sim can excite a genuine **massive, compact-sector (n≥1) matter
wave** and interfere *that*, on the same lattice.

## Setup

Same two-slit geometry (sep 60, slit 10, barrier→detector L=175). Compact axis
nc=12. **Canonical scatter** (`--scatter canonical`, the default): registers are
edge end-registers, out[d] = V − in[−d] with an end-swap per edge. Its dispersion
in any number of axes d is the mean of cosines,

  cos Ω = (cos k_x + cos k_y + cos k_c)/3,

it is **isotropic**, and its propagating band sits at Ω ≈ 0, so the drive maps
straight through: Ω = ω_drive. Driven at `--omega 0.4416`, i.e. Ω = 0.4416.

- **photon baseline:** `--nc 12 --nmode 0` (c-uniform ⇒ massless).
- **matter wave:** `--nc 12 --nmode 1` (compact n=1 ⇒ rest freq ω₀ = 0.300, massive).

The drive sits **47% above the mass gap**, so the in-plane wavelength is
well-conditioned (a ±1% shift in Ω moves λ by ∓1.9%).

The de Broglie wavelength is obtained **two independent ways**: analytically, by
solving the dispersion for k_x at k_y = 0; and **empirically**, by FFT along x of
the field in a separate barrier-free CW pass. The measured value depends on no
convention and is the check on the analytic one.

## Result

| mode | rest freq ω₀ | λ analytic | λ **measured** | 1 slit | 2 slits | fringe spacing |
|---|---|---|---|---|---|---|
| photon (n=0) | 0 (massless) | **8.07** | **8.13 ± 0.25** | single lobe (1 max) | 7 maxima | ~26.2 |
| matter (n=1) | 0.300 (massive) | **11.18** | **11.35 ± 0.48** | single lobe (0 max) | 7 maxima | ~32.8 |

Four things established:

1. **A massive matter wave two-slit interferes** — fringes appear for the compact
   n=1 mode, on the same GRID lattice as the photon. The one-slit control is a
   clean single lobe for *both* modes, so the fringes are two-slit interference,
   not single-slit diffraction ripple. **[C]**
2. **The pattern is mass-dependent, in the de Broglie direction.** The massive
   mode has a **longer** in-plane wavelength — 11.18 vs 8.07 nodes, the ratio 1.385
   following from the dispersion's cos k_c term (mass lowers k_x) — and
   correspondingly **wider** fringes. **[C + D for the λ]**
3. **The analytic λ is confirmed by measurement** — to 0.7% (photon) and 1.5%
   (matter), within the FFT's own resolution. This is the check the earlier pass
   claimed but did not perform. **[C]**
4. **The paraxial law now roughly holds.** With the lab isotropic, Δ = λL/d
   predicts 23.5 (photon) and 32.6 (matter) against observed 26.2 and 32.8 —
   **+11% and +0.6%**. The earlier anisotropic run missed it by a factor ~3.

## The honest limit

The photon's 11% departure from λL/d is real: the slits are wide (10 nodes) and
the pattern is only marginally paraxial, so the *absolute* spacing is still not a
precision observable. The robust claims are the directional one (matter
interferes, coarser than the photon), the analytic λ, and now its measured
confirmation.

The interference itself remains **classical linear-wave** behavior (both modes are
linear Bloch waves, Ch 4); what is new here is only that it is the *matter*
(compact-sector) wave, transferred by linearity. The distinctively-quantum content
is still Ch 8 (the click) and Ch 10 (Bell).

## Revision record (2026-09-18)

What changed, and what did not:

- **Scatter convention.** The run used a direction-of-travel register labeling
  (out[d] = V − in[d]) whose exact dispersion is Σ_a 1/(cos k_a + cos ω) = 0. That
  reduces to a mean of cosines only at d = 2; at d = 3 it is a quadratic, giving
  c² = 2/3 on-axis and both 1/2 and 1/6 on a face diagonal — anisotropic and
  birefringent. The three-axis lab has been moved to the canonical rule, which is
  isotropic. See [dispersion-analytic.md](dispersion-analytic.md) §d-axis
  generalization. The old rule remains available as `--scatter legacy`.
- **Drive.** The canonical band sits at Ω ≈ 0 rather than ω ≈ π, so the same
  physical Ω = 0.4416 is now requested as `--omega 0.4416` instead of `--omega 2.7`.
- **The numbers 8.07 and 11.18 are unchanged** — the mean-of-cosines relation that
  produced them is *correct* for the canonical scatter, so the published
  wavelengths turned out right for the lab as now constituted, and are confirmed
  by measurement. What was wrong was pairing that relation with the legacy rule.
- **Rest frequency ω₀ = 0.300 is unchanged**, for the same reason.
- **Fringe spacings changed** (photon 5.9 → 26.2; matter 13.8 → 32.8): the medium
  itself changed, from anisotropic to isotropic. The *ordering* — matter coarser
  than photon — is unchanged, and the agreement with λL/d improved sharply.
- **Two sim defects fixed alongside.** (i) The snapshot summed over the compact
  axis, which annihilates any n ≥ 1 mode exactly (Σ_c cos(2πc/12) = 0); the
  published matter figure was rendering float noise at ~10⁻¹⁵. It is now projected
  onto the compact mode. The detector pattern was never affected — it sums
  squares. (ii) The module docstring claimed the script measured λ by FFT; it did
  not. The measurement is now implemented.
- **Peak counting.** The script no longer labels ≥3 maxima "INTERFERENCE FRINGES";
  that heuristic cannot separate diffraction from interference. The one-slit
  control does, and is now run and reported.
