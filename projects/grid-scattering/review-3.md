# grid-scattering — framing review (4)

**Scope:** The project as of commit 69b08de: [README.md](README.md), [Appendix.md](Appendix.md), [work/junction-geometry.md](work/junction-geometry.md), [work/STATUS.md](work/STATUS.md), [work/first-run.md](work/first-run.md), [scripts/cylinder.py](scripts/cylinder.py), and the project index entry in [../README.md](../README.md). It covers logical and structural problems only. The project sitting outside accepted physics is not counted as a problem.

Checks run for this review (none committed):
- **Linear dispersion of the θ coupling.** One tick of `cylinder.py`'s rule, "rotate the (x, c) register pairs by θ, then propagate", is linear and translation-invariant. Its Bloch eigenphases can therefore be computed exactly for each (k_x, k_c), where k_x and k_c are the wavenumbers along x and around c. Each eigenphase is the frequency ω of a mode.
- **Seed sweep of the resonance.** `cylinder.py --cw` with default parameters (λ = 24, sat 0.8, gain 0.5, zpe 10⁻³, 900 steps), nc = 20–28, seeds 1–3, run with `--one-point` and with `--all-points`.

---

## Fatal

### F1 — The weak always-on coupling does not give Kaluza–Klein motion, and it gives light a mass

README §3 ("And it can move") and junction-geometry §3 claim: *"A weak but non-zero exchange gives one wave operator spanning both directions, hence the joint relation ω² = c²k² + ω₀²."* The rule actually implemented, a θ-rotation between the (+x, +c) and (−x, −c) register pairs at every node, does not do this. Exact Bloch eigenphases at θ = 0.1, in lattice units:

**Light (k_c = 0).**

| k_x | 0 | 0.02 | 0.05 | 0.1 | 0.3 |
|---|---|---|---|---|---|
| ω | 0.100 | 0.090 / 0.110 | 0.078 / 0.128 | 0.062 / 0.162 | 0.030 / 0.330 |

At k = 0 the frequency is ω = θ, not 0. Light has acquired a mass gap equal to θ. Massless light has an eigenvalue of 1 for the uniform k = 0 state. The pooled scatter has that eigenvalue (it maps the all-equal register vector to itself), and any local rotation mixing x and c registers loses it.

**The massive branch (k_c = 2π/24 = 0.262).**

| k_x | 0 | 0.05 | 0.1 | 0.2 |
|---|---|---|---|---|
| ω (upper branch) | 0.296 | 0.301 | 0.309 | 0.336 |
| KK target √(k_x² + k_c²) | 0.262 | 0.267 | 0.280 | 0.330 |

The group velocity (v_g = dω/dk, the speed at which a wave packet moves) of the compact-like mode in the (+x, +c) block is **+0.10 at k_x = 0** and +0.06 at k_x = −0.1. A mode "at rest" drifts, and its direction is fixed by which way it circulates, not by its x-momentum. The rule is non-reciprocal (S ≠ Sᵀ with directions reversed), so a ±n standing wave splits, half going +x and half −x.

The source of the failure is structural. KK dispersion comes from a **derivative** coupling, the shared Laplacian ∂²/∂x² + ∂²/∂c², which the pooled scatter supplies at full strength. A local rotation between register groups is a **non-derivative** mixing, like a mass term. Making it small does not approach KK behaviour. It gives two nearly independent one-way transport channels with an avoided crossing near k_x ≈ k_c. So:

- motion with v = p/E needs coupling of order 1 between the x and c sectors, while
- massless light needs that coupling to be zero, or at least to leave the photon's k = 0 state alone. The experimental bound on the photon mass (below about 10⁻¹⁸ eV) puts θ far below 10⁻⁴⁰ per tick if a tick is anywhere near the Planck time.

The motion problem from the previous review has therefore come back in a new form. Its core is now a tension between the project's posit (space and a sheet exchange little or nothing) and KK motion, which needs space and the compact direction joined in **one isotropic wave operator**. The STATUS entries "Junction rules form a continuous family … Weak always-on coupling is therefore available" and "restores motion by ordinary Kaluza–Klein dispersion" are not supported. A coupling that kept light massless and still gave hyperbolic dispersion would have to couple +x to −x movers through c (backscatter) with a strength that grows with k_c. Whether such a rule can still be called "weak" is the open question, and it should be framed as one.

### F2 — The frequency-threshold argument still rests on withdrawn numbers

The **Two conditions** paragraph in §3 is how the README handles the most serious physics check it faces: pair production depends on photon *energy*, not on field *amplitude*, and laser fields do not make pairs. It still reads "measured at ω = 2π/nc across four ring sizes, with 12–58× more energy retained than at 8% detuning", and says off-resonant energy "sloshes in and comes straight back". §3a repeats "sharp (12–58× over 8%)", and STATUS lists E6 as done with the same figures. All of these come from the lossy comb arena that first-run.md withdraws. What survives with the conserving rule is about 1.5×, against a background that wanders 0.25–0.31 (README "What has been measured"). The seed sweep reproduces that scale:

| one-point, n ≠ 0 content ÷ total | nc 20 | 22 | 24 | 26 | 28 |
|---|---|---|---|---|---|
| seeds 1–3 | 0.25–0.29 | 0.26–0.31 | 0.35–0.37 | 0.26–0.28 | 0.28–0.31 |

A 1.3× local maximum cannot carry "each sheet carries its own threshold… forced, not fitted", nor the account of why lasers make no pairs. The README presents the threshold story as established when its evidence has been withdrawn. Until a resonance strong enough to gate transfer is shown with the conserving rule, the amplitude-versus-frequency problem (first raised as F3 in the second review) is open again and should be listed as such in §3a.

M1 below gives a lead: the local all-points rule shows a much stronger resonance.

---

## Moderate

### M1 — The one-point rule is non-local, it is not needed, and it suppresses the resonance

`--one-point` lets only the c-position with the largest |T| at each x overflow. That is an `argmax` taken around the whole ring, so whether a node fires depends on the instantaneous state of nodes up to nc/2 away. GRID's node update is local, so this is a departure the README does not acknowledge. The README justifies the rule on the grounds that without it "the injection is uniform and the winding is zero". That holds only with **no** background. With the README's own background (zpe 10⁻³), the local `--all-points` rule gives:

| all-points, n ≠ 0 content ÷ total | nc 20 | 22 | 24 | 26 | 28 |
|---|---|---|---|---|---|
| seeds 1–3 | 0.10–0.13 | 0.11–0.13 | **0.55–1.62** | 0.19–0.38 | 0.13–0.19 |

With zpe = 0 the all-points winding is exactly 0, as equivariance requires. So the symmetry breaking really does come from the state, through local amplification of the background, and the resonance at nc = λ is **several times stronger** (roughly 2–10× over the neighbouring circumferences, depending on seed) than with the one-point rule. The non-local rule is both unneeded and counter-productive. The local rule is the natural one to adopt, and its seed-to-seed variability is the thing E0 should measure.

(The "content" in both tables is `cylinder.py`'s FFT power. It is not normalised energy, which is why ratios above 1 appear; see M5.)

### M2 — The overflow rule no longer has a ceiling

§2 and §3 justify saturation as a **bound**: "a register holds only so much". The implemented rule rotates the (x, c) pairs by gain × (|T| − sat). For excess 0.2 that is 0.1 rad, which moves about 1% of the energy and leaves the x registers above the "ceiling". Nothing bounds any register. What is implemented is a threshold-activated, intensity-dependent coupling, not a capacity limit. That may be the better model, but then "discrete and finite forces a bound" no longer motivates it. The "Honest footing" boundary between what is forced and what is posited has to be redrawn. A rotation through the angle that brings |T| back to sat would restore the bound and still conserve energy exactly.

### M3 — Saturation and linear coupling are not separated, and with θ > 0 the linear coupling is part of the model

The previous review's M1 (no linear-tap control) still applies. It is sharper now that the model *includes* a linear tap (θ). With θ > 0, energy crosses into c at every node on every tick, without saturation, and coherently at matching k (F1's avoided crossing). The claim that "saturation does the bulk crossing" needs a θ > 0, sat-off control arm. The STATUS question "does saturation still do its job at θ > 0?" is the right one, and it should be a gating experiment, not a footnote.

### M4 — The claim that winding is conserved is stated too strongly

The README says breaking the symmetry by the state "keeps winding conserved, and winding is charge once the field is complex". Equivariance guarantees that a translation-invariant state stays invariant. For a nonlinear, non-Hamiltonian map like the overflow rotation, it does **not** guarantee that a winding observable is conserved; that needs a Noether structure the rule has not been shown to have. On a real field the ±n balance is automatic (Hermitian symmetry) and proves nothing. The README also uses "winding" (the Bloch label k_c) and "circulation" (+c versus −c register flux) as if they were the same thing. A c-uniform +c flux circulates but has winding 0. "99.95% circulates rather than sitting in the non-circulating mode" should say which one is meant.

### M5 — The measurements have no provenance, and the metric is not energy

The new figures (99.95%, 0.370 / 0.252 / 0.250, "drift 0.0") live in README prose only. first-run.md says they were "re-measured … see README §3", but there is no work file, no output, and no command line. `cylinder.py`'s "compact content" is |FFT(f₊c + f₋c)|² summed. By Parseval's theorem that is nc times the register energy, which is why it can exceed the total energy (306 against 828 at nc = 24, and 1209 against 842 in all-points). Because it uses only the *sum* f₊c + f₋c, it also discards half of the compact state. "Winding fraction" needs a definition in energy terms (for example, the compact-register energy with k_c ≠ 0 divided by the total compact energy) and a recorded run.

### M6 — Review items from the previous round that are still open

- **Above threshold** (previous M2): at 2× and 3× the threshold frequency the ring takes up an n = 2 or 3 rest mode, not a moving pair.
- **Particle count and the photon-plus-nucleus case** (previous M3): two threshold photons make one ±n object; the Bethe–Heitler threshold is a single photon of 2mₑc².
- **Frame dependence** (previous M4): the resonance condition depends on lab-frame frequencies rather than the invariant √(ω₁ω₂).
- **Schwinger "prediction"** (previous M8): guaranteed by dimensional analysis, with an undetermined convention factor of about 16. The project index now advertises it as a prediction.

None of these appears in §3a, "What this arena cannot settle". They should either be answered or listed there.

### M7 — Stale and contradictory text

The README still contains several passages that the current model contradicts:
- **Status line:** "the crossing is resonant, and the junction geometry is settled analytically."
- **§3 "What the overflow does":** "half each way". The implemented rotation maps +x → +c and −x → −c, so it is "half each way" only for a symmetric collision. The paragraph also says x-momentum transfer "is not yet implemented … which by §2 it could never leave", but by the new §2, motion is supposed to come from θ.
- **§3 "Energy bookkeeping, honestly":** describes the withdrawn lossy rule ("the drift is reported and the repair is queued").
- **Objective 2:** "the direct test of §3's soliton claim". The soliton has been withdrawn.
- **§5 and §6:** still describe a rule "not yet written down" and "build the saturating rule" (flagged in the previous review, M7).
- **§7:** "its M1 run verified the cylinder as a faithful arena". M1 verified the *pooled* scatter. The arena is a cylinder again, but with a pass-through-plus-rotation rule M1 never tested.

STATUS has stale entries too:
- **E2's pre-registration:** "with saturation on, it should hold together … if it holds together with saturation off, §4 of junction-geometry.md is wrong". That is the withdrawn soliton logic, and §4 of junction-geometry.md is now about Maxwell.
- **E5:** "measured on the superseded product grid". The product grid is the current arena.
- **E7:** "amplitude is moved … the books will not balance".
- **E6:** still marked done (F2).
- **All three "Queued — writing" items** predate this revision.

Elsewhere:
- **Appendix B, P1:** keeps "the uniform rule keeps modes apart statistically", which is incorrect: on a periodic lattice the linear rule keeps them apart *exactly*.
- **junction-geometry §2:** describes the continuous family as S = exp(θA) with "A an antisymmetric circulant". `cylinder.py` implements a pair rotation that is not circulant. Which rule is meant?

---

## Light

- **L1 — Attribution in the STATUS header.** STATUS says the three fatal problems were "all in material added during earlier review rounds rather than in the project's own thesis". The amplitude-moving overflow rule was specified in the project's own framing before any review ("Energy conservation is to be measured, not engineered", README at ac895bc §3), and the second review's M1 flagged it as lossy. The record should be accurate.
- **L2 — Reciprocity.** The script's rotation couples +x → +c with +sin θ and −x → −c with +sin θ. Under direction reversal that is non-reciprocal; the reciprocal variant flips one sign. The two variants give different dispersion (F1's drift locked to circulation direction comes from the non-reciprocal one). Choose deliberately, and say why.
- **L3 — How the energy audit is done.** `cylinder.py` audits `step()` on a random probe state at start-up rather than on the run itself. That is adequate for a rule that is exactly orthogonal, but a running total of the drive's input against the sponge's absorption would also catch accounting errors outside `step()`.
- **L4 — "Light must pass" under θ > 0.** With θ > 0, light passes but changes: it gains a mass gap and partly mixes into c registers (F1). The calibration argument assumes θ = 0 and should say so.
