# Klein tracks: ν₁, ν₂, ν₃ as closed tracks on a modulated Klein tube

Working file for host **E3** in [host-candidates.md](host-candidates.md). It transplants sheet-proton's working mechanism to a Klein bottle:
- a tube whose cross-section changes shape around the ring;
- distinct closed tracks a wave can ride;
- mass set by track length, **m = 2πℏc / L_track**, one wavelength per closed track ([sheet-proton modulated-clover §6, Step 7](../../sheet-proton/work/modulated-clover.md)).

Script: [../scripts/klein_tracks.py](../scripts/klein_tracks.py). Figure: [../outputs/klein_tracks_fit.png](../outputs/klein_tracks_fit.png).

## 1. Geometry

A point on the tube is X(t, θ) = ((R + u) cos θ, (R + u) sin θ, v), with:
- θ: angle around the ring;
- R: ring radius;
- (u, v): the cross-section point c(t; θ), rotated by θ/2, where t runs once around the cross-section.

The Klein closure rule says that one lap brings each cross-section point to its mirror partner: X(t, θ + 2π) = X(−t, θ). With the θ/2 rotation, that becomes a condition on the cross-section:

<!-- c(t; θ+2π) = −c(−t; θ) -->
$$
c(t;\,\theta + 2\pi) \;=\; -\,c(-t;\,\theta)
$$

Two kinds of shape terms satisfy it:

| Term | Form | Around the ring |
|---|---|---|
| **odd** | (A_k, B_k) · sin(kt) | unchanged every lap |
| **morph** | (C_k, D_k) · cos(kt) · cos(θ/2) | flips sign every lap |

The morph terms let the lobes change into one another as the wave travels around the ring, the Klein analog of sheet-proton's major↔minor swap. On the proton sheet, a lap returns the cross-section *rotated* (a torus). Here it returns *mirrored* (a Klein bottle).

Any purely odd cross-section passes through its center at t = 0 and t = π, so it crosses itself there. That is the figure-8 waist, forced by the closure rule. The 3D surface therefore crosses itself, which is taken to be harmless: the grid passes through itself without interacting.

## 2. Track bookkeeping

A track rides a fixed cross-section position t₀. After one lap it arrives at −t₀.

- **One-lap tracks:** t₀ = 0 and t₀ = π, the two mirror points. A mirror reflection of a closed loop always has exactly two fixed points, so there are **always two** one-lap tracks.
- **Two-lap tracks:** every other t₀ pairs with −t₀ into a single track that closes after two laps.

Of the continuum of tracks, the ones taken to host a wave are the **stationary** ones: local maxima or minima of track length as t₀ varies, by analogy with light following stationary paths.

## 3. Structural results (math)

1. **One-lap length is fixed.** With no morph terms, both one-lap tracks run along the waist, where c = 0, so both have length exactly 2πR and coincide in 3D. Morph terms separate them slightly.
2. **The factor of 2 comes from geometry.** On a two-lap track, the outward offset u at position t₀ on the first lap is exactly reversed at −t₀ on the second, so first-order effects cancel. Two-lap length = 2 × 2πR × (1 + a correction of order (cross-section size / R)²). With mass ∝ 1/L, a one-lap track is **about twice as heavy** as a two-lap track. That is the ν₃ ≈ 2 × ν₁ pattern from lap count, not from harmonics.
3. **Two-lap tracks carry the spin-½-like sign flip.** One wavelength spread over two laps means the wave is half a wavelength along after one lap, so it returns **inverted**: the ring-oscillator signature. One-lap tracks return **unchanged**.
4. **Every track is neutral:**
   - *one-lap:* going once around the ring reverses orientation, so a charge defined by signed turning satisfies Q = −Q = 0 ([mechanisms N4](mechanisms.md#1-neutrality));
   - *two-lap:* lap 2 is the mirror image of lap 1, so its signed turning is opposite and the closure totals 2π − 2π = 0. In the orientable double cover, the map between the two laps reverses orientation.

## 4. Fit results

Target: Δm²₃₁/Δm²₂₁ = 33.6, with ν₃ = the shorter one-lap track and ν₁, ν₂ = two stationary two-lap tracks. The search used 4 odd harmonics and 3 morph harmonics, and required:
- R ≥ 1.1 × the largest cross-section radius;
- a minimum cross-section "thickness" (smallest/largest spread, where 1 = round and 0 = flat).

| Thickness ≥ | ν₁, ν₂ from | Ratio | Masses (meV) | Σm (meV) | m₃/m₁ | Two-lap split | Other stationary tracks (meV) |
|---|---|---|---|---|---|---|---|
| 0.3 | any | 33.58 | 27.8, 29.1, 57.4 | 114 | 2.07 | 4.8% | 25.6, 28.7, 28.7, 55.8 |
| 0.3 | maxima only | 33.62 | 25.8, 27.2, 56.5 | 110 | 2.19 | 5.5% | 27.4, 28.3, 53.7 |
| 0.5 | any | 33.60 | 26.7, 28.0, 56.9 | 112 | 2.14 | 5.2% | 26.7, 56.9 |
| 0.5 | maxima only | 33.59 | 25.2, 26.6, 56.2 | 108 | 2.23 | 5.8% | 26.6, 53.3 |
| 0.5 | any, **figure-8 only** (k = 1, 2; no morph) | 33.60 | 26.6, 27.9, 56.9 | 111 | 2.14 | 5.2% | 27.9 |

**The minimal shape suffices.** The cleanest result needs no morph terms and no higher harmonics: a slightly tilted figure-8, x = 0.60 sin t, y = 0.34 sin t + 0.69 sin 2t, with R = 1.56 (in units where the cross-section is of order 1). The overall size is absorbed by the mass calibration, so this is **three shape numbers** (size relative to R, tilt, aspect) fitting one ratio. Two consequences:
- with no morph terms, the two one-lap tracks run along the same waist curve in 3D, so there is arguably a **single ν₃ track**;
- only one extra stationary track remains, a near-copy of ν₂ about 0.3% longer.

The figure shows this case: ν₁ sits at the tall peak of the track-length curve (the large lobe's tip), and ν₂ and its copy are the shallow dip and shallow peak beside each other. Because those two are a nearly merged dip-peak pair, small shape changes can create or remove them together. That makes ν₂'s existence sensitive to shape, which a selection rule would need to address.

An earlier search with a coarser size limit (cross-section extent measured as the sum of coefficients) could not reach the target with thickness ≥ 0.3, stalling at ratios of 45–59. The target needs a tube that is fat relative to R, because the two-lap tracks must differ by about 5% in length and that difference is second order in (cross-section size / R).

## 5. Assessment

**What works:**
- The measured splitting ratio is reachable with reasonably round cross-sections.
- The masses land consistently near 25–28, 27–29, and 56–57 meV (Σm ≈ 108–114 meV).
- The factor of 2, the spin-½-like flip for ν₁ and ν₂, and neutrality all come from the geometry rather than from fitting.

**What it does not show:**
1. **No prediction yet.** Even the minimal figure-8 has three shape numbers for one ratio (the general search used fifteen), so a fit is only an existence proof. The mass values are not an independent prediction either: any host with "near-degenerate pair + third at about 2×" gives similar numbers once fitted to the measured ratio (compare the 1D ring's 28.6, 29.9, 57.9 meV).
2. **Extra tracks.** Every fit has at least one extra stationary track (one in the minimal figure-8, up to four in richer shapes): near-copies of ν₁/ν₂ from the cross-section's near-symmetry, and the second one-lap track as a near-copy of ν₃. All must be sterile. The proton sheet picks its tracks by charge; the neutrino sheet has no charge to pick by, so a **selection rule** is needed. Should the copies couple and be split, the ν₃ copy runs into the pseudo-Dirac bound (δm₃² ≲ 1.2×10⁻⁵ eV²; [mechanisms §3](mechanisms.md), T3).
3. **ν₃'s spin.** The one-lap track returns unchanged each lap, so ν₃ lacks the sign flip ν₁ and ν₂ have. It also runs along a mirror line, where the sign-flipping wave modes are zero. ν₃ needs spin from its relationship to space ([mechanisms P2](mechanisms.md#4-spin-½)) or a different assignment.
4. **Track picture vs. wave picture.** The path-length rule assumes waves localize on stationary tracks. sheet-proton tested that for its surface ([track_localization.py](../../sheet-proton/scripts/track_localization.py)); it has not been tested here.
5. **Curvature.** Unequal track lengths need a non-flat surface. Every track's *net* charge is zero (§3.4), but the per-arc distribution along a closed track is still open ([host-candidates](host-candidates.md) open question 6).

## 6. Next steps

- **A selection rule** that picks three tracks and silences the rest, possibly through stability: which stationary tracks hold a localized wave.
- **A wave calculation** on the fitted surface (the analog of sheet-proton's track localization) to check that ν₁, ν₂, ν₃ correspond to real localized modes.
- **Fewer parameters:** the plain tilted figure-8 already reaches 33.6 with three shape numbers. Next, find what fixes them, for example a requirement that the waves localize, or a link to the electron or proton sheet, so that the remaining freedom becomes predictions.
- **ν₃ spin:** whether the "relationship to space" route supplies it, or whether an assignment exists in which all three are two-lap tracks.
