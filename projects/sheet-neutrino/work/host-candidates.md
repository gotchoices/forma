# Host candidates

Working file. It compares candidate neutrino hosts against the requirements in [../reference/experimental-constraints.md](../reference/experimental-constraints.md). The numbers come from [../scripts/spectra.py](../scripts/spectra.py). The terms (twisted closure, Klein bottle, sheared torus) are introduced in [../reference/geometry-background.md](../reference/geometry-background.md).

## 1. What a host must deliver

1. **Spectrum:** three fermion-class mass states with Δm²₃₁/Δm²₂₁ ≈ 33.6. That means a near-degenerate pair plus a distant third.
2. **Neutrality:** no charge density anywhere, not just zero net charge.
3. **Half-integer angular momentum,** behaving as spin ½ from outside (rotation sign change, Fermi statistics, observed helicity). The internal mechanism is open.
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

## 4. Candidates

### A. 1D ring, near-periodic (δ ≈ 0.022)

- **Spectrum:** fits, with modes +1, −1, +2. Predicts m = 28.6, 29.9, 57.9 meV and Σm = 116 meV, in tension with recent cosmological bounds (~70 meV, model-dependent). Normal ordering.
- **Problem:** the n = 0 mode, with mass ∝ δ ≈ 0.022, lies *below* the pair: a fourth, nearly massless state. It must be excluded by a rule or be sterile.
- **Neutrality:** a line has no surface, so there is no geodesic curvature and no G1 charge density. Whether a 1D winding carries charge at all is open, because MaSt's charge rule (R48: tube winding n₁ = ±1) is stated for a 2D sheet with distinct tube and ring directions.
- **Spin:** no internal route yet. Candidate external route: angular momentum handed off from the electron or proton sheet during beta decay (README pool).
- **Twist source:** unidentified. In the torus picture it is shear; in 1D it would need its own origin, such as an effective flux.

### B. 1D ring, near-antiperiodic (δ = ½ − e, e ≈ 0.029)

- **Spectrum:** fits, with modes n = 0, −1, +1, giving masses ∝ ½ − e, ½ + e, 3/2 − e. Predicts m = 17.0, 19.1, 53.1 meV and Σm = 89 meV, closer to the cosmological bound but still above it. Normal ordering.
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

- **Neutrality:** forced by topology. Every mode is a standing wave in the flipped direction (zero net winding, R48 F5), and is its own charge conjugate (Majorana).
- **Spin:** the fermion-class (odd) modes are antiperiodic around the ring.
- **Spectrum:** blocked in its simplest form. The lowest three fermion-class levels give a ratio of at most 3. The ± pair that Family A relies on is merged into one standing wave, and shear in the flipped direction is not physical.
- **Fallbacks:**
  - a skewed ("rhombic") lattice that might split the surviving ±k_ring pair;
  - slight curvature, which reintroduces G1 charge density and so conflicts with neutrality;
  - non-lowest modes with a selection rule.
- **Chirality:** the space has no global handedness. Compatibility with the neutrino's definite helicity is unchecked.

### E. Pool (not yet examined)

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
| D. Flat Klein bottle | blocked (≤ 3) | none available | — | — | forced by topology | antiperiodic, gap open |

All fitting hosts use one tuned small parameter to fit one ratio. That is a fit, not a prediction. They differ in what they predict beyond it: Σm, the presence of extra light states, and Majorana versus Dirac. Those are the comparison points.

## 6. Open questions

1. What is charge on a 1D host? Does a single winding carry it, and if so, what makes the neutrino's winding neutral?
2. What sets the small splitting parameter (δ, e, or s)? Is there a reason it is ≈ 0.02–0.03?
3. How does a host receive half-integer angular momentum in beta decay and carry it away as spin ½ (§2.3 of the constraints file)?
4. Can any host predict the mixing angles? The near-maximal θ₂₃ ≈ 45° is suggestive of an equal mixture of two states.
5. Resolve the notation and calibration inconsistencies listed in [../reference/prior-work.md](../reference/prior-work.md#known-inconsistencies-to-resolve) before relying on Family A's absolute masses.
