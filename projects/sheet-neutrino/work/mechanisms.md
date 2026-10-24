# Mechanisms

Working file. A catalog of candidate mechanisms, organized by the job each one does: neutrality, the small ν₁/ν₂ split, the structure of ν₃, spin ½, matter/antimatter, and mixing. The hosts that combine these mechanisms are compared in [host-candidates.md](host-candidates.md). Numbers come from [../scripts/spectra.py](../scripts/spectra.py). Terms are introduced in [../reference/geometry-background.md](../reference/geometry-background.md).

Each entry carries a status:
- **math:** follows from the stated assumptions;
- **hypothesis:** a physical assumption not yet derived;
- **speculative:** an idea worth testing, with key steps missing.

## 0. Framing: charge is a property of closure

Charge, and promotion generally, arises from **closure**. Before a path closes, the values along it are free. Once it closes, they must be self-consistent around the loop, which correlates them more tightly. Charge is the net turning that this self-consistency locks in.

On this view, charge per unit arc length (G1, [metric-charge Ch 11](../../metric-charge/11-modeling-foundation.md)) is also a closure property. It is defined only as a part of a closed path, never as a free-standing local quantity. A partial arc, such as one lobe of a figure-8, carries no charge of its own. *Status: framing adopted for this project.*

**Open point:** within a closed path, per-arc values can still form a measurable distribution. The neutron's nonzero charge radius is one, presumably from per-arc values on its closed tracks. For a neutrino host, the cleanest reading is a **flat intrinsic geometry**. Its tracks are straight, so the per-arc values are zero everywhere as well as in total. The figure-8 is then how the closure looks when drawn in 3D, not a physical curvature.

## 1. Neutrality

| ID | Mechanism | Host | Status |
|---|---|---|---|
| N1 | **No slot for charge.** A 1D dimension has one winding number and no closure rule of the kind that carries a charge label ([ma-domain config-neutrino §NC.3](../../ma-domain/work/config-neutrino.md)). | 1D ring | math, given MaSt's charge rule |
| N2 | **Standing waves.** On a Klein bottle, every mode is a standing wave in the flipped direction, with zero net circulation, which carries zero charge ([R48 F5](../../../studies/R48-helicity-charge/findings.md)). | Klein | math |
| N3 | **Zero turning number.** The figure-8 closes with +2π on one lobe and −2π on the other: promotion (closure) with zero charge. Turning number cannot change under smooth deformation (Whitney–Graustein), so this neutrality is topologically protected: it cannot become ±2π without a cusp. | Klein (drawn as figure-8) | math |
| N4 | **No global orientation.** Signed turning (left vs. right) needs a consistent orientation, which a Klein bottle lacks. A charge defined by signed turning is carried into its negative by one trip around the ring, so Q = −Q, which forces Q = 0. | Klein | math |
| N5 | **Sign-conjugate pairing.** Neutrality from equal amplitudes of ±n partners ([R61 Track 4](../../../studies/R61-neutrino-tuning/findings.md)). Proof open (R61 pool item d). Conflicts with ν₁/ν₂ being those same partners ([host-candidates §4C](host-candidates.md#c-2d-torus-family-a-existing)). | torus | open |

N2–N4 are three views of one fact about the Klein bottle and need not be counted separately. N4 is the most basic.

**Excluded:** cancellation between *separated* charges, including nested + and − tori unless they coincide in position and motion ([chapter 1 §5](../01-host-requirements.md)).

## 2. The small ν₁/ν₂ split

The measured ratio Δm²₃₁/Δm²₂₁ ≈ 33.6 needs a near-degenerate pair plus a distant third. Evenly spaced harmonics give at most 4 ([host-candidates §3](host-candidates.md#3-a-general-limit-consecutive-modes-cannot-make-336)). Something must split a pair slightly.

| ID | Mechanism | Host | Status |
|---|---|---|---|
| S1 | **Shear** between the sheet's two directions; the ±n partners see different effective lengths. | torus (Family A) | math |
| S2 | **Grid direction bias as a loop phase.** A small direction asymmetry in the grid (χ_anti, [grid-primitive ch. 9](../../grid-primitive/09-chirality-asymmetry.md)) is undetectable in open space but adds a fixed phase per lap around any compact loop (a Wilson-loop phase), splitting the two circulation directions. | 1D ring; Klein (ring direction only) | math given χ_anti ≠ 0; χ_anti itself a hypothesis |
| S3 | **Different tracks, different geometry.** As the proton and neutron are distinct tracks on a modulated cross-section, ν₁ and ν₂ could be distinct tracks or channels split by shape. See host E; the track version (E3) fits the ratio with a ≈ 5% length split between two two-lap tracks ([klein-tracks.md](klein-tracks.md)). | lobed / modulated Klein | fit found; many parameters |

**On S2.** The bias is linear but direction-dependent (*non-reciprocal*), not non-linear. *Signals analogy:* the Sagnac effect in a ring-laser gyroscope, where rotation splits the clockwise and counterclockwise resonances. Required phase per lap, as a fraction f of a full turn: 1D ring f ≈ 0.022 (normal ordering) or ≈ 0.0075 (inverted); Klein ring f ≈ 0.029. If one bias acts on every sheet, it predicts tiny particle/antiparticle mass differences on the electron and proton sheets, scaling with sheet size (≈ 10⁻⁹ and ≈ 10⁻¹², just under current limits; [host-candidates §3a](host-candidates.md#a-cross-sheet-check-does-the-same-bias-split-particle-and-antiparticle)).

**On S3.** ma-domain found that a symmetric shape cannot split a pair protected by the loop's rotational symmetry ([config-neutrino §NC.5](../../ma-domain/work/config-neutrino.md)). Track pairs related by the Klein mirror are a different kind of pair, so that result may not apply, but this has to be checked.

## 3. The structure of ν₃

In the harmonic hosts, ν₃ ≈ 2 × ν₁. This is a feature of those models, not of the data, which fix only Δm². The lightest mass is unmeasured.

| ID | Idea | Status |
|---|---|---|
| T1 | **Next harmonic, flux included.** ν₃ is n = 2 with the same per-lap phase: mass ∝ 2 − f. The phase's relative effect shrinks with harmonic number (f/n) but never vanishes, because every circulating mode feels the loop's phase. | math |
| T2 | **Exactly double.** Hypothesis that ν₃ = 2 × the unsplit fundamental. It fixes the absolute scale: m ≈ 28.2, 29.5, 57.7 meV, Σm ≈ 115 meV. It differs from T1 by about 0.5 meV, below any planned experiment's reach. | hypothesis |
| T3 | **Merged ±2 doublet** (*excluded in equal-weight form; see issue 2*). ν₃ is the +2/−2 pair, unresolved and seen as one. The equal-weight average of (2 − f)² and (2 + f)² is 4 + f², so T3 *produces* T2 without the phase vanishing. Same masses as T2. In the literature such a near-degenerate pair is a *pseudo-Dirac* pair. | speculative |
| T4 | **Shape-protected standing wave.** On a loop with 4-fold shape symmetry, the shape couples +2 with −2 into standing waves, which feel the phase only at second order. The n = ±1 pair stays circulating and keeps its first-order split. A 3-fold shape does not do this. | math |
| T5 | **Lobe-peaked bias on a Klein bottle.** If the ring bias varies across the tube, concentrated at the lobe centers (allowed, since it is mirror-symmetric), the second tube harmonic has a node at each lobe center and feels less of it. | speculative (bias profile a new hypothesis) |

**T3 issues:**
1. With a uniform phase the ±2 pair is split *more* than ±1 in squared mass (Δm² = 2 × Δm²₂₁ ≈ 1.5×10⁻⁴ eV²). Merging therefore needs a reason other than small splitting, such as the weak interaction coupling only to one combination.
2. **Test, and result: excluded in its equal-weight form.** That splitting gives an extra oscillation with length ≈ 49 km at reactor energies (3 MeV), at the JUNO baseline (~53 km), and ≈ 16,500 km at 1 GeV. A pair of nearly equal-mass states that the weak interaction couples to equally is a **pseudo-Dirac** pair. For ν₃, a combined fit of atmospheric (Super-Kamiokande), reactor (Daya Bay), and long-baseline (MINOS, T2K) data limits its splitting to **δm₃² ≲ 1.2×10⁻⁵ eV²**, with a JUNO forecast of 6×10⁻⁵ eV² (Anamiati, Fonseca & Hirsch, [PRD 97, 095008 (2018)](https://arxiv.org/abs/1710.06249), Table 1). T3 needs 1.5×10⁻⁴ eV², about 12 times above the bound. A cosmological analysis gives \|δm₃²\| < 2×10⁻⁶ eV² ([Fong & Porto 2025](https://arxiv.org/abs/2512.19782)), which is model-dependent context only. **Loophole:** the bounds weaken or vanish if the weak interaction couples to only one member of the pair. But then the other member is fully sterile, ν₃ is a single state at 2 ± f, and the averaging that gave exact doubling is lost, so T3 reduces to T1. *Status of T3 as stated: excluded.*
3. **State count:** four or more light states. Only three flavor combinations may couple to the Z.
4. **Mixing:** if the rule that merges ±2 equally also applied to ±1, electron neutrinos would be a 50/50 mix of ν₁ and ν₂ (solar angle 45°). The measured angle is about 33–34°.

**T4 numbers** (phase f = 0.022, shape amplitude 0.4 in E² units): n = ±2 shift ±0.088 on a plain or 3-fold loop, ±0.018 on a 4-fold loop. The trade-off: the shape that suppresses the phase also splits n = 2 into two standing-wave states (≈ ±2.5% here), leaving ν₃ off exact doubling and adding a nearby partner state. Exact doubling and full suppression cannot both be achieved.

**T5 numbers.** For bias profile sin²ᵖ(qy), peaked at the lobe centers, the fraction felt by tube harmonic 2 relative to harmonic 1:

| p | Ratio (harmonic 2 / harmonic 1) |
|---|---|
| 1 | 0.67 |
| 2 | 0.50 |
| 4 | 0.33 |
| 16 | 0.11 |

The sharper the peak, the stronger the suppression. It is never exactly zero for a smooth profile.

Fitting ν₃ = merged (ring ±½, tube harmonic 2) with the phase fully suppressed: f ≲ 0.029 with tube/ring ratio r² ≈ 22f. Examples: f = 0.02 gives m ≈ 35.6, 36.6, 61.6 meV and ν₃/ν₁ ≈ 1.7. Two parameters fit one ratio, so this is less predictive than T1–T3.

**Bearing on the hosts:** a Klein bottle with a uniform ring phase gives ν₃ ≈ 3 × the pair (levels ½ and 3/2), not 2×. If doubling proves meaningful, it favors integer-harmonic hosts (1D ring, torus) or a Klein variant like T5.

## 4. Spin ½

| ID | Route | Host | Status |
|---|---|---|---|
| P1 | **Antiperiodic closure.** The wave returns inverted after one lap and restored after two, like a ring oscillator with an odd number of inverters. | 1D near-antiperiodic; Klein odd family | math; link to spatial rotation open |
| P2 | **Relationship to space.** Part of the half-integer character can reside in how the host is oriented within space (S), provided it travels with the neutrino ([chapter 1 §4](../01-host-requirements.md)). | any, especially 1D | hypothesis |
| P3 | **Opposite signs between the lobes.** On a Klein bottle, a mode always shares itself equally between the two lobes. If the two halves have the same sign, the mode returns unchanged after a lap; if they have opposite signs, it returns inverted. The fermion character lives in that antisymmetry between lobes. | Klein | math |
| P4 | **R49 fermion rule.** Modes with \|n_r\| ≥ 1 are spin-½ candidates, via R25's 1:2 winding-ratio mechanism. | torus | existing rule |

**Open for all routes:**
- Why a 360° rotation in space corresponds to one internal lap.
- On a Klein bottle, which has no global handedness, how definite helicity (left-handed neutrinos, right-handed antineutrinos) arises. If helicity is tied to the host's relationship with space (P2) rather than to the sheet's own orientation, there is no conflict, but this needs showing.

## 5. Matter and antimatter

- **Convex/concave and particle/antiparticle.** If particle-on-convex is equivalent to antiparticle-on-concave, the Klein bottle builds that equivalence in: each ring lap swaps the lobes, and with them convex and concave. In standard terms it is a geometric combination of charge conjugation and reflection, which is CP-like. *Status: speculative interpretation of a math fact.*
- **Grid bias as matter preference.** The direction bias of S2 splits particle and antiparticle masses only slightly, and precision measurements bound such splits on the electron and proton sheets. A small mass split alone yields almost no population difference. If the bias explains why matter dominates, it more likely acts through how particles are created. *Status: open* ([metric-charge ch. 6 §6.7](../../metric-charge/06-handedness-and-pairs.md)).

## 6. Mixing

| ID | Idea | Status |
|---|---|---|
| M1 | **3-fold symmetry gives tribimaximal mixing.** A 3-fold symmetric loop gives θ₁₂ ≈ 35.3°, θ₂₃ = 45°, θ₁₃ = 0 as its symmetric limit. Breaking the symmetry is expected to supply θ₁₃ and the CP phase ([ma-domain neutrino-1D §6](../../ma-domain/work/neutrino-1D.md)). Measured: 33–34°, 42–49°, 8.5°. | partial; PMNS not computed |
| M2 | **Flavor = lobe, mass = pattern across lobes.** If e, μ, τ are localized channels (lobes) and mass states are the patterns that spread across them, mixing is large by construction, as observed for neutrinos (unlike quarks). An exactly symmetric version mixes too evenly (large θ₁₃), so the deviation from symmetry must be what sets the small angle. See host E. | speculative |

## 7. Predictions and tests

| Consequence | Mechanism | How it would be tested |
|---|---|---|
| Lightest mass ≈ 28 meV, Σm ≈ 115 meV | T2/T3 (also T1: 116 meV) | future direct-mass experiments; cosmology as context |
| Σm ≈ 89 meV | 1D near-antiperiodic | same |
| Σm ≥ 130 meV | Klein + uniform ring phase | direct-mass experiments (still under the KATRIN limit) |
| Extra oscillation at Δm² ≈ 1.5×10⁻⁴ eV² | T3 | already excluded: δm₃² ≲ 1.2×10⁻⁵ eV² (atmospheric + reactor + long-baseline) |
| Electron/positron mass difference ~10⁻⁹; proton/antiproton ~10⁻¹² | S2 with one grid-wide bias | precision particle/antiparticle comparisons |
| Neutrino and antineutrino spectra differ slightly | S2 (if ±n are ν and ν̄) | comparing ν and ν̄ oscillation parameters |
| Neutrino is its own antiparticle | Klein (N2), mildly broken by S2 | neutrinoless double-beta decay searches |
| A state just above ν₃ that must not interact | Klein + phase; T4; 1D near-antiperiodic | Z-decay count; sterile-neutrino searches |
