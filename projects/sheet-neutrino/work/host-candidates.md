# Host candidates

Working file. It compares candidate neutrino hosts against the requirements in [../reference/experimental-constraints.md](../reference/experimental-constraints.md). The numbers come from [../scripts/spectra.py](../scripts/spectra.py). The terms (twisted closure, Klein bottle, sheared torus) are introduced in [../reference/geometry-background.md](../reference/geometry-background.md). The mechanisms the hosts combine (neutrality N1–N5, splitting S1–S3, ν₃ structure T1–T5, spin P1–P4, mixing M1–M2) are cataloged in [mechanisms.md](mechanisms.md).

## 1. What a host must deliver

1. **Spectrum:** three fermion-class mass states with Δm²₃₁/Δm²₂₁ ≈ 33.6. That means a near-degenerate pair plus a distant third.
2. **Neutrality:** no charge density anywhere, not just zero net charge.
3. **Half-integer angular momentum,** behaving as spin ½ relative to space while traveling alone (rotation sign change, from which exclusion follows; observed helicity). The internal mechanism is open.
4. **Oscillation:** the produced flavor states must be mixtures of the three mass states. Ideally the host predicts the mixing angles.
5. **No extra light states that couple to weak interactions,** since the Z-decay width counts three.

## 2. Observation: Family A's splitting pattern is a 1D twisted-ring effect

Family A ([R49](../../../studies/R49-neutrino-filter/findings.md), [R61 F1](../../../studies/R61-neutrino-tuning/findings.md)) uses modes (1,1), (−1,1), (1,2) with mass formula µ² = (n_r·ε)² + (n_t − n_r·s)². The first term is the same, ε², for all three modes, so it cancels in every mass difference. Only the second term matters for the splittings:

<!-- n_t − n_r·s = 1 − s, 1 + s, 2 − s;  Δ₂₁ = 4s,  Δ₃₁ = 3 − 2s,  ratio = (3 − 2s)/(4s) -->
$$
\frac{\Delta m^2_{31}}{\Delta m^2_{21}} = \frac{(2-s)^2 - (1-s)^2}{(1+s)^2 - (1-s)^2} = \frac{3-2s}{4s} \approx 33.6 \quad\text{at } s = 0.022
$$

This is exactly the spectrum of a **1D ring with twisted closure δ = s** (geometry-background §6), using circulation modes n = +1, −1, +2:
- ν₁ and ν₂ are the two **circulation senses** of the same winding, split by the twist.
- ν₃ is the next winding up.

R49's published Family A masses (m₁ ≈ 29 meV, Σm = 117.8 meV) are within about 2% of the pure 1D ring calibrated the same way (28.6 / 29.9 / 57.9 meV, Σm = 116 meV). In R49's calibration, then, the second direction contributes only a small common offset to the absolute masses.

**What this does and does not show.** Oscillation data alone do not require a 2D host. The pattern they constrain is carried entirely by one twisted direction. This is a statement about the mass formula, not evidence that the host *is* 1D. In R49, the second direction does other work: it supplies the spin-½ assignment (fermion candidates need |n_r| ≥ 1) and the Majorana pairing.

## 3. A general limit: consecutive modes cannot make 33.6

For a 1D ring with any twist δ, taking three consecutive modes n = 0, 1, 2 (masses ∝ |n + δ|) gives a splitting ratio of at most **4**. For the lowest three fermion-class levels of a flat rectangular Klein bottle, the maximum is **3**. A ratio of 33.6 needs a pair split by a *small* parameter, so that Δm²₂₁ is much smaller than Δm²₃₁. In every viable fit so far, that pair is a ± circulation pair.

**Central question for any host: what physically sets the small splitting parameter?**

## 3a. A candidate source: substrate chirality as a Wilson-loop flux

[grid-primitive ch. 9](../../grid-primitive/09-chirality-asymmetry.md) shows that a small direction-asymmetry in the grid (antisymmetric chirality χ_anti) acts on waves exactly like a constant background gauge field A. Two properties follow:
- **In open space it is undetectable.** A constant A can be removed by redefining the wave's phase, so light still travels at c in every direction.
- **Around a compact loop it is physical.** The phase that can't be removed is the loop integral W = ∮A·dx = A·L, a gauge-invariant **Wilson-loop phase**. In closure terms, this is exactly the twist δ = W/2π of [geometry-background §6](../reference/geometry-background.md#6-twisted-and-antiperiodic-closure).

So a direction bias built into the grid is a natural physical source for the small parameter in §3. The asymmetry is linear but direction-dependent (non-reciprocal), not non-linear. ma-domain's NC configuration already uses this mechanism for a 1D curve ([config-neutrino.md §NC.5](../../ma-domain/work/config-neutrino.md)).

*Signals analogy:* the Sagnac effect in a ring-laser gyroscope. Rotating the ring adds a direction-dependent phase per lap, which splits the clockwise and counterclockwise resonances by a small, precise amount. ν₁/ν₂ would be the two circulation senses of the neutrino loop, split by the grid's built-in bias.

**Fit to the measured ratio (33.6):**

| Host | Modes | Flux f needed | Ordering |
|---|---|---|---|
| 1D ring | −1, +1, −2 | ≈ 0.022 | normal |
| 1D ring | 0, −1, +1 | ≈ 0.0075 | inverted |
| 1D ring, near-antiperiodic | ½ ± f, 3/2 − f | ≈ 0.029 | normal |
| Flat Klein bottle, flux around the ring | odd family: ±½ + f, 3/2 − f (tube n = 1) | ≈ 0.029 | normal |

**The Klein bottle is no longer blocked on the spectrum.** The Klein identification (x, y) ~ (x + L_ring, −y) forbids a constant A along the flipped tube direction but allows one along the ring. A flux there splits exactly the degeneracy the flip leaves behind, the ±k_ring pair. The tube contributes a common offset that cancels in differences, as ε does in Family A. Result: ratio 33.6 from the three lowest states at f ≈ 0.029, for any tube/ring ratio r ≳ 0.8 (checked at r = 1, 2, 5). Neutrality is unaffected, because the flux does not touch the tube-direction standing waves. Cost: the fourth state (3/2 + f) sits just above ν₃ and must be sterile. Unlike the 1D ring, the tube offset raises every absolute mass: at r ≈ 0.82 (the smallest r before a tube-n = 2 state intrudes) the masses are 34, 35, 61 meV (Σm ≈ 130 meV), rising to Σm ≈ 145 meV at r = 1 and 550 meV at r = 5. The direct mass limit caps r at roughly 12.

### A cross-sheet check: does the same bias split particle and antiparticle?

If χ_anti is a property of the grid, it acts on every compact loop, including the electron and proton sheets. Since W = A·L grows with loop length, a uniform A gives each sheet a flux proportional to its size: f_sheet ≈ f_ν · (L_sheet / L_ν). On a 2D sheet the phase shifts mode energies by an amount ∝ m·W_α + n·W_β, which flips sign between matter (m, n) and antimatter (−m, −n) (grid-primitive §8). That would make particle and antiparticle masses differ by a relative amount of order f_sheet.

Order-of-magnitude estimate, with f_ν = 0.022 and L_ν ≈ 40 μm (R61's scale):

| Sheet | Size L | Implied f_sheet | Measured particle/antiparticle equality |
|---|---|---|---|
| electron | ~2.4 pm | ~10⁻⁹ | electron/positron masses equal to < 8×10⁻⁹ |
| proton | ~1.3 fm | ~10⁻¹² | proton/antiproton charge-to-mass equal to ~1.6×10⁻¹¹ (BASE) |

Both implied values fall below current limits. The electron's is within about an order of magnitude of the limit. Taken at face value, this is a **falsifiable consequence** reachable by precision experiments. With ma-domain's larger loop (L_ν ≳ 4 cm) the implied values drop by about 10³ more.

**Caveats:** this assumes A has the same strength along every compact direction (the sheets occupy different dimensions, so A could have independent components on each, with no linkage), that the geometric projection factors are of order 1, and that the joint-sign partners on the 2D sheets are particle and antiparticle. The same question arises on the neutrino side: if ±n on the loop are neutrino and antineutrino, the flux makes their spectra differ, which oscillation experiments compare.

**On matter dominance:** a tiny mass split by itself gives at most a tiny population difference. If the grid's bias explains why matter is preferred, it more likely acts through how particles are *created* (a directional preference in the process) than through the mass split. That remains open ([metric-charge ch. 6 §6.7](../../metric-charge/06-handedness-and-pairs.md)).

## 4. Candidates

### A. 1D ring, near-periodic (δ ≈ 0.022)

- **Spectrum:** fits, with modes +1, −1, +2. Predicts m = 28.6, 29.9, 57.9 meV and Σm = 116 meV, above the cosmology-model bound of ~70 meV (context only, see [constraints §4](../reference/experimental-constraints.md#4-masses)). Normal ordering.
- **Problem:** the n = 0 mode, with mass ∝ δ ≈ 0.022, lies *below* the pair: a fourth, nearly massless state. It must be excluded by a rule or be sterile.
- **Neutrality:** a line has no surface, so there is no geodesic curvature and no G1 charge density. Whether a 1D winding carries charge at all is open, because MaSt's charge rule (R48: tube winding n₁ = ±1) is stated for a 2D sheet with distinct tube and ring directions.
- **Spin:** no internal route yet. Candidate external route: angular momentum handed off from the electron or proton sheet during beta decay (README pool).
- **Twist source:** unidentified. In the torus picture it is shear; in 1D it would need its own origin, such as an effective flux.

### B. 1D ring, near-antiperiodic (δ = ½ − e, e ≈ 0.029)

- **Spectrum:** fits, with modes n = 0, −1, +1, giving masses ∝ ½ − e, ½ + e, 3/2 − e. Predicts m = 17.0, 19.1, 53.1 meV and Σm = 89 meV, closer to the cosmology-model bound but still above it (context only). Normal ordering.
- **Better than A:** the three chosen states are exactly the three lowest. There is no stray lighter mode.
- **Spin:** the closure is almost antiperiodic, which is the ring-oscillator / spin-½ sign flip (geometry-background §6). The gap between an internal sign flip and spin under spatial rotation remains open.
- **New question:** why is the antiperiodicity broken by a small e ≈ 0.029? The pair ν₁, ν₂ would be exactly degenerate at e = 0.
- **Tower:** higher pairs follow at (n + ½) ± e. The next state, 3/2 + e, sits just above ν₃. It must be sterile or weakly mixed.
- **Neutrality:** same as A.

### C. 2D torus, Family A (existing)

- **Spectrum:** fits (§2). Σm ≈ 118 meV (R49).
- **Spin:** from R49's fermion rule (|n_r| ≥ 1).
- **Neutrality:** Majorana pairing of ±n partners. The cancellation proof is still open (R61 pool item d). Note that ν₁ and ν₂ *are* the ± partner pair, split by shear. Neutrality by superposing them would conflict with their being distinct mass states.
- **Zoo:** many other triplets also give 33.6 (R61 F3). This needs a selection rule.

### D. Flat Klein bottle

- **Geometry:** physically a flat Klein bottle. The figure-8 tube is how its closure looks when drawn in 3D, with lobes at +2π and −2π, not a physical curvature ([mechanisms §0](mechanisms.md#0-framing-charge-is-a-property-of-closure)). Self-crossing in the drawing is harmless if the grid passes through itself without interacting.
- **Neutrality:** forced by topology, in three equivalent views: standing waves (N2), zero turning number (N3), and no global orientation, so Q = −Q = 0 (N4). Every mode is also its own charge conjugate (Majorana).
- **Spin:** the fermion-class (odd) modes return inverted after one ring lap. The two lobes carry opposite-sign halves (P3).
- **Spectrum, no phase:** blocked. The lowest three fermion-class levels give a ratio of at most 3, and shear in the flipped direction has no physical effect.
- **Spectrum with a ring phase (D′, §3a):** fits at f ≈ 0.029. The tube offset makes Σm ≥ 130 meV, ν₃ ≈ 3 × the pair, and a fourth state sits just above ν₃. The variant with a lobe-peaked bias (T5) instead makes ν₃ the merged second tube harmonic, with ν₃/ν₁ ≈ 1.6–1.8.
- **Other fallbacks (not needed for the fit):** a skewed ("rhombic") lattice; non-lowest modes with a selection rule.
- **Open:**
  - Helicity on a surface with no global handedness (P2 may resolve it).
  - The magnetic moment of a standing-wave mode.
  - What "antineutrino" means once the ring phase breaks time-reversal symmetry.

### E. Lobed Klein bottle (multi-track)

The proton sheet hosts the proton and neutron as distinct tracks of similar but different mass on a modulated (clover) cross-section. The analog here puts ν₁, ν₂ (and possibly ν₃) on distinct tracks or channels of a Klein bottle, with the splitting set by geometry (S3) rather than, or alongside, the ring phase.

**E1. The two waist circles.** A Klein bottle has exactly two closed paths that close in a single ring lap: the circles at y = 0 and y = L_tube/2, which are the waist lines of the figure-8 drawing. Every other ring-parallel path needs two laps. If the cross-section is not symmetric under a half-turn, the two waist circles differ slightly, giving a natural near-degenerate pair. **Conflict:** the fermion-class (odd) modes vanish exactly on these circles, since sin(qy) = 0 there. Only the even modes live on them, so the track picture and the wave picture disagree here.

**E2. Lobed cross-section, localized channels.** A corrugated cross-section creates channels where waves localize in the high-curvature lobes ([sheet-proton lb-mode-localization](../../sheet-proton/work/lb-mode-localization.md)). N lobes give N channels of nearly equal energy, split by leakage between neighbors. The Klein mirror maps lobes onto lobes, and the fermion-class states are the mirror-antisymmetric combinations:

| Lobes | Mirror line | Mirror pairs | Fermion-class lobe states |
|---|---|---|---|
| 3 | through one lobe | 1 | 1 |
| 4 | between lobes | 2 | 2 |
| 6 | between lobes | 3 | **3** |
| 7 | through one lobe | 3 | **3** |

Three fermion-class states come most naturally from **six lobes with the mirror line between lobes**, which echoes sheet-proton's six-piece (3 major + 3 minor) cross-section. That is a counting coincidence, not a result.
- **Spectrum:** not computed. A uniform 6-lobe ring gives the wrong pattern, so the major/minor alternation and possibly the ring phase must produce the near-degenerate pair plus distant third.
- **Mixing:** flavor = lobe, mass = pattern across lobes (M2) makes mixing large by construction. This is the one candidate so far with a structural route to *predicting* mixing angles.
- **Costs:** more shape parameters; every unused lobe state must not interact; ma-domain's result that symmetric shapes cannot split a protected pair must be rechecked for mirror pairs.

**E3. Modulated tube with distinct tracks (the sheet-proton mechanism).** The cross-section changes shape around the ring and returns *mirrored* after one lap. A wave rides a closed track, with mass = 2πℏc / L_track as on the proton sheet. There are always two one-lap tracks (the mirror points t₀ = 0, π); every other track closes after two laps. Results ([klein-tracks.md](klein-tracks.md)):
- the geometry makes a one-lap track about **twice as heavy** as a two-lap track;
- two-lap tracks carry the spin-½-like sign flip, and every track is neutral;
- fits reach Δm²₃₁/Δm²₂₁ = 33.6 with reasonably round cross-sections, giving masses ≈ 25–28, 27–29, 56–57 meV and Σm ≈ 108–114 meV.

Open: a selection rule for the 1–4 extra stationary tracks, ν₃'s spin (its one-lap track returns unchanged each lap), a wave-localization check, and fewer parameters (the minimal fit, a plain tilted figure-8, uses three shape numbers for one ratio).

### G. Lepton-domain circle

Developed in [lepton-domain-circle.md](lepton-domain-circle.md) (draft for review). The neutrino lives on a grand circle of three segments, one per charged lepton. Each segment is a Klein-glued sheet pairing a large neutrino dimension with a small dimension **shared with that lepton's electron sheet**, which forms a lepton domain within [ma-domain](../../ma-domain/README.md)'s architecture.
- **Light mode:** travels only along the large direction. The flip reverses its polarization along the small dimension, so each segment inverts the wave; three segments give (−1)³ = −1 per circuit, which is spin-½-like and not 3/2.
- **Flavor and mass:** flavor = segment, mass = whole-circle mode.
- **Spectrum:** 3-fold symmetry gives an exactly degenerate lowest pair plus a separated state. A few percent difference between the segments (the generations) splits the pair. The measured ratio is reached for any junction strength, with Σm ≈ 107–192 meV.
- **Commitments:** sheets are glued along shared circles, not multiplied; energy in the small dimension becomes an electron at the junction; Compton size and gravitational size are distinct.
- **Open:** the glued-sheet reading for ma-domain; where flavor coupling happens (it decides whether the k = 3/2 state can be ν₃); the junction itself; lepton number vs. Majorana-like behavior.

### F. Pool (not yet examined)

- A 1D line coupled to the electron or proton sheet rather than standing alone
- Hosts where the three mass states come from different structures rather than one spectrum
- Non-flat 1D hosts: a line with variable "index," giving non-uniform mode spacing
- Real projective plane RP²: cannot be flat (χ = 1), so local curvature is forced; probably excluded by neutrality, not yet checked

## 5. Comparison

| Host | Ratio 33.6 | Small parameter | Σm (meV) | Extra light state | Neutrality mechanism | Spin route |
|---|---|---|---|---|---|---|
| A. 1D near-periodic | fits | δ ≈ 0.022 | 116 | yes (n = 0) | no surface; 1D charge rule open | external, open |
| B. 1D near-antiperiodic | fits | e ≈ 0.029 | 89 | no | no surface; 1D charge rule open | near-antiperiodic, gap open |
| C. 2D torus (Family A) | fits | shear s ≈ 0.022 | 118 | excluded by fermion rule | Majorana pairing, proof open | R49 fermion rule |
| D. Flat Klein bottle, no flux | blocked (≤ 3) | none available | — | — | forced by topology | antiperiodic, gap open |
| D′. Flat Klein bottle + ring flux (§3a) | fits | f ≈ 0.029 | ≥ 130 (rises with r) | 4th state just above ν₃ | forced by topology | antiperiodic, gap open |
| D″. Klein + lobe-peaked bias (T5) | fits, 2 parameters | f ≲ 0.029, r² ≈ 22f | ≈ 129–150 | (3/2 − f) states above ν₃ | forced by topology | antiperiodic, gap open |
| E2. Lobed Klein (channels) | not computed | shape (± phase) | — | unused lobe states | forced by topology | mirror-antisymmetric lobe states |
| E3. Modulated Klein tube (tracks) | fits (minimal: tilted figure-8, 3 shape numbers) | two-lap track length split ≈ 5% | 108–114 | 1 extra track (minimal fit) to 4 | per track: Q = −Q or 2π − 2π | ν₁, ν₂ inverted per lap; ν₃ not |
| G. Lepton-domain circle | fits (junction g, asymmetry d) | segment asymmetry 1–17% | 107–192 | 4th state above ν₃ | no small-dim winding; Klein flip | polarization flip, (−1)³ per circuit |
| 1D ring, ν₃ = merged ±2 (T3) | **excluded**: pair splitting 1.5×10⁻⁴ eV² vs bound 1.2×10⁻⁵ | f ≈ 0.023 | 115 | ±2 partner | as A | as A/B |

All fitting hosts use one tuned small parameter to fit one ratio. That is a fit, not a prediction. They differ in what they predict beyond it: Σm, the presence of extra light states, and Majorana versus Dirac. Those are the comparison points.

## 6. Open questions

1. What is charge on a 1D host? Does a single winding carry it, and if so, what makes the neutrino's winding neutral?
2. What sets the small splitting parameter (δ, e, or s)? Is there a reason it is ≈ 0.02–0.03?
3. How does a host receive half-integer angular momentum in beta decay and carry it away as spin ½ (§2.3 of the constraints file)?
4. Can any host predict the mixing angles? The near-maximal θ₂₃ ≈ 45° is suggestive of an equal mixture of two states.
5. Resolve the notation and calibration inconsistencies listed in [../reference/prior-work.md](../reference/prior-work.md#known-inconsistencies-to-resolve) before relying on Family A's absolute masses.
6. Under the closure framing ([mechanisms §0](mechanisms.md#0-framing-charge-is-a-property-of-closure)), what per-arc distribution does a closed track carry, and is it zero for every candidate host?
7. Does a standing-wave mode carry a magnetic moment under MaSt's assignment of current to modes?
8. ~~Merged-ν₃ (T3): do published data exclude a ν₃ doublet split by ≈ 1.5×10⁻⁴ eV²?~~ **Answered: yes**, by about a factor of 12 in its equal-weight form ([mechanisms.md](mechanisms.md) §3, T3 issue 2).
9. For the lobed Klein bottle (E2): do six mirror-paired lobes give a near-degenerate pair plus a distant third, and what mixing matrix follows?
