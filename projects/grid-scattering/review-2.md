# grid-scattering — framing review (3)

**Scope:** The retooled project as of commit b2663b3: [README.md](README.md), [Appendix.md](Appendix.md), [work/junction-geometry.md](work/junction-geometry.md), [work/first-run.md](work/first-run.md), [work/STATUS.md](work/STATUS.md) and [scripts/line_and_ring.py](scripts/line_and_ring.py). The question is whether the framing is a sound basis for the goals in [../thoughts.md](../thoughts.md). It covers logical and structural problems only. The project sitting outside accepted physics is not counted as a problem.

Two checks were run for this review. Neither is committed.
- **Energy audit.** The arena was run with `--cw` (default parameters) for 1,500 ticks, recording the change in total register energy caused by `step()` alone. Propagation is a permutation and conserves energy, so the recorded change comes only from the overflow rule.
- **Junction algebra.** An algebraic parameterization of the X-junction rules, verified numerically.

Items are numbered for reference.

---

## Fatal

### F1 — The arena does not implement the junction the README is built on, and cannot test the README's main objective

README §2 and junction-geometry.md analyse an **X junction**: one node with two space edges and two compact edges, where the rule between the groups is straight-through. Objective 2, the soliton claim in §3, and E2–E4 in STATUS all need that geometry. A moving particle is described as a helix whose x-part and c-part are tied together by exchange at nodes they *share*.

The arena that was built and measured has no such node. It is a **comb**: one x-line, with a ring hung from each x position at a single point (ring node 0), joined only during overflow. Ring nodes 1 … nc−1 have no x-edges at all. A ring excitation at x₀ has no path to x₀ + 1 except through two overflow events (ring → line → next ring), and the line holds no compact phase to carry the winding along. The helix of junction-geometry §4 cannot even be represented in this geometry. E2a ("overflow carries its x-momentum") has nowhere to put that momentum, because a ring has no x-direction.

The geometry that *does* have X junctions at every node, the (nx × nc) product grid, was rejected in first-run.md because a photon spread over it is uniform in c and therefore injects winding 0. That is the result anticipated in the earlier reviews: on a product geometry with a symmetric rule, a c-uniform photon cannot produce winding. The comb gets around it by giving each compact circle a **privileged point** where space attaches. That is a new geometric posit, not a cut-down version of the old one:
- it is neither S × c nor the cylinder of metric-mass or grid-matter;
- it breaks translation symmetry along c, the symmetry whose conservation law is winding, which is charge once the field is complex (Appendix D).

The framing currently describes two different geometries as one: the X junction for motion and mass, and the comb for creation and resonance. It needs to pick one, or explain how the comb's results carry over to the X-junction geometry. Until it does, objective 2 cannot be tested on the arena as built, and §7's description ("the (x, c) cylinder testbed; its M1 run verified the cylinder as a faithful arena") is wrong twice over: the comb is not that cylinder, and M1 tested the pooled scatter.

### F2 — Calibrating the ceiling so that "light must pass" puts a free electron below the ceiling, so the soliton binding cannot happen

§3 calibrates the ceiling with "a lone photon never saturates", and §3a's bridge sets amplitude per quantum by energy and localisation volume (ℏω in about one wavelength, so amplitude ∝ ω²). Apply that same bridge to the electron the arena is supposed to make:
- A threshold photon has ℏω = mₑc² and is localised over about λ_C = h/(mₑc), the electron's Compton wavelength.
- An electron at rest is a ring standing wave with energy mₑc², on a ring whose circumference *is* λ_C (that is how the ring size fixes the mass), and it cannot be localised in space more tightly than about λ_C without becoming relativistic.

So the electron has about the same amplitude as one threshold photon. Split into two counter-propagating halves, it has less. By the calibration, one such photon sits below the ceiling, so a free electron's core is below the ceiling too. junction-geometry §4 needs exactly the reverse: "at its core the amplitude is above the ceiling, so the groups exchange there, continuously". Without that exchange, junction-geometry's own argument says the x-part and c-part shear apart.

The two posits that carry objective 2, the ceiling calibration and the saturation-bound soliton, contradict each other for the lightest charged particle. Escaping this needs either a particle core much more compact than λ_C (which would need its own justification), or a binding mechanism other than saturation.

### F3 — The "settled" measurements were taken with a rule that destroys more energy than the system contains

Energy audit, CW drive, 1,500 ticks:

| nc | nc/λ | energy destroyed by the overflow rule | energy in all rings at end |
|---:|---:|---:|---:|
| 12 | 1.0 | 81.7 | 33.5 |
| 13 | 1.08 | 144.6 | 0.09 |
| 18 | 1.5 | 144.7 | 0.01 |
| 24 | 2.0 | 98.8 | 41.8 |
| 36 | 3.0 | 112.4 | 32.3 |

For comparison, the line holds about 32–40 units at the end. On every run the rule destroys more energy than the rings and the line hold together, and it destroys **most where there is no resonance**. Off resonance the ring → line count is **zero**. The energy does not "slosh in and come straight back" as §3 says; the rule wipes it out. Two mechanisms produce this:
- clipping the x registers removes energy e·sat + e²/2 (e the excess over the ceiling) while the ring receives e²/2;
- injection *adds amplitude* to whatever the ring already holds, so out-of-phase injection cancels existing ring content and that energy disappears.

The second mechanism is why the off-resonance arm is where the losses concentrate.

So the headline numbers, "50–100× at resonance" and "12–58× over 8% detuning", are end-state ratios taken across a lossy rule whose losses differ between the arms being compared. They are also fixed-run-length ratios. Appendix G names both of these as conditions under which a ratio is not evidence, and this is the same selective-dissipation pattern the Appendix records from the earlier clipping test. STATUS lists "transfer is resonant", "resonance selects the predicted mode" and "reverse channel exists" as **Settled**. Under the project's own rules they are unverified until they are repeated with a conserving rule. Two smaller errors sit alongside this:
- Both the README and the script docstring say the drift "is reported". The script does not report it.
- The README's explanation of the e/√2 runaway is wrong. Splitting a fresh e as e/√2 each way still loses energy whenever e < 2·sat. The runaway comes from the same cross-term, coherent amplitude added to existing content. That points to the repair: an exchange (rotation) that accounts for what the ring already holds, not a different split factor.

---

## Moderate

### M1 — The resonance comes from the ring, not from saturation, and there is no control that could tell them apart

A lossless delay line with round-trip time nc, fed periodically at one point, builds up at ω = 2πm/nc and takes up mode m. That holds whatever the injection mechanism is: a weak linear tap gives the same comb of resonances. The only control run so far, "clipping off", removes the coupling altogether, so it cannot separate *saturation* from *coupling in general*. Results 2 and 3 in first-run.md, and E6, describe how a ring behaves, and nothing in them needs saturation. The README's "two conditions" framing is fine. Saturation's role, though, is now limited to setting *whether* coupling happens at all, and so far there is no measurement of that beyond the observation that the collision overflows and a single pulse does not. A linear-tap control arm would make the distinction explicit.

### M2 — Above threshold, the resonance mechanism predicts the wrong products

Real γγ → e⁺e⁻ has a *threshold*. Above it, the extra energy turns into kinetic energy of the pair, continuously. In the arena, nothing happens between resonances (nc/λ = 1.5 gives nothing), and at 2× and 3× the threshold frequency the ring takes up a single **n = 2 or n = 3 standing mode**, which is a heavier object at rest, not an n = 1 pair in motion. Under the arena's rule, a 1.022 MeV photon pair would make one n = 2 electron-ring excitation of mass 2mₑ rather than an electron and a positron with kinetic energy. At high energies the harmonics sit close together, so almost any hard photon would find a high-n electron-ring mode. That is a tower of products at multiples of mₑ, which is not observed. E8's plan to broaden the resonance would produce a peak with tails, not a threshold followed by a continuum. Getting a continuum needs the products to carry kinetic energy, which takes objective 2. So the threshold claims in §3 depend on F1 being resolved.

### M3 — The particle count and the single-photon threshold are inconsistent

- **γγ.** Two photons, each at ω_e = mₑc²/ℏ, drive a single ring standing wave. The README adopts metric-mass's reading that the ±n superposition is *one* particle. So the arena turns 2mₑc² of photon energy into one object whose natural frequency is that of a single electron. The observed process makes two particles. thoughts.md read the bidirectional spill as the *pair*, and Appendix B rejected that reading. Whichever reading is kept, the count has to come out as two.
- **Photon plus nucleus.** §3 says a nucleus's field "stands in for the second photon". The observed Bethe–Heitler threshold is a single photon of **2**mₑc², not mₑc². A static field has ω = 0, so the resonance condition would have to be met by the photon alone, at ω_e or at 2ω_e (the n = 2 mode). Neither gives one consistent account of both processes.

### M4 — The frequency threshold depends on the reference frame

In the arena both drives have the same frequency, which corresponds to the centre-of-momentum frame. In general, two photons ω₁ ≠ ω₂ meeting head-on make pairs when the invariant √(ω₁ω₂) reaches threshold (in units where ℏ = 1), which happens, for example, with a 10 MeV photon on a 30 keV one. A ring fixed at a lattice position sees ω₁, ω₂ and their intermodulation products, none of them near ω_e. The interference pattern itself drifts at the centre-of-momentum velocity. A ring that moved with it would see √(ω₁ω₂), the correct invariant. So a frame-independent threshold needs the product to move with the centre of momentum, which again comes back to objective 2 and F1. As the arena stands, whether pairs form depends on the lab frame.

### M5 — "No continuous knob" depends on an unstated assumption, and the conservation law in the scan is misnamed

**The constraint is not momentum.** junction-geometry §3's constraint passes a **total reflector** (−1, 0, 0) as momentum-conserving, but a wall reverses momentum. Worked through, the constraint is that the quantity (out + in) is equal on both arms of each axis. That is continuity of a node potential along each axis, a Kirchhoff-type condition. Under a physical momentum (weighted by energy flux, so ∝ amplitude²), the uniform rule *fails*: the forward minus backward energy is ¼ − ¼ = 0. The README's statement that the uniform rule is "the only symmetric rule that conserves both energy and momentum" therefore depends on a mislabelled constraint. The Y-junction uniqueness claim should be restated in terms of what is actually conserved.

**The knob exists once x and c are allowed to differ.** The four isolated solutions come from imposing full **C4** symmetry (90° rotations), which treats x and c as interchangeable. The project's own premise is that space and a sheet are different kinds of thing. With only the mirror symmetries x ↔ −x and c ↔ −c, the unitary rules satisfying the same constraint are S = −I + V·K·Vᵀ, where V picks out each axis's arm pair and K = (I + R)/2 for any 2 × 2 orthogonal R. That gives continuous families:
- R a reflection: reciprocal (S = Sᵀ), but near straight-through the c arms become a wall.
- R = rotation(θ): straight-through at θ = 0. At θ = 0.1, an incoming +x pulse leaves as 0.998 forward, **0.05 to each of ±c**, and −0.002 reflected. It is exactly unitary and obeys the per-axis continuity. Its cost is that it is **non-reciprocal** (S ≠ Sᵀ).

The C4 case recovers exactly junction-geometry's four rules, which cross-checks the parameterization. So weak, always-on linear coupling, split symmetrically both ways round the ring, is available at the price of reciprocity. It is not excluded. "Weak coupling must be nonlinear" holds only if reciprocity is required, and that requirement should be stated and argued. Non-reciprocity is not obviously off the table here: [grid-primitive](../grid-primitive/README.md) already carries a chirality parameter.

### M6 — Ring saturation is only tested at one node

The script checks the ring's ceiling only at the junction node (ring node 0). Elsewhere a ring can exceed the ceiling with no effect. That makes the ring rule non-uniform around the circle, which is a second explicit break of c-symmetry on top of F1's privileged point. It also gives a sequence-dependent cap on build-up, which feeds into the resonance measurements. Either check every ring node, or state this as a posit (saturation happens only where a sheet meets space).

### M7 — Parts of the framing are stale and contradict the new material

- **§5** still says the overflow rule "is not yet written down concretely enough to analyse", and it still offers "Does it stay? … a fit should persist, a misfit decay" as a test. first-run.md says persistence is automatic on a lossless ring and "says nothing".
- **§6** step 1 ("build the saturating rule and run §5") is done.
- **§7** still calls the arena grid-matter's cylinder (F1).
- **The script docstring and the README** both say the drift is reported (F3).
- **The project index** in [../README.md](../README.md) still describes the earlier framing: a derivation as first work item, the parametric-process label, and winding conservation of the linear substrate as the argument. STATUS lists this as queued.
- **The STATUS header** says junction geometry "settles" F1 of the previous review. Given F1 and F2 here, it changes F1's form but does not settle it.

### M8 — The Schwinger "prediction" follows from dimensional analysis, and its convention is undetermined

Put one quantum ℏω_e into a volume ƛ_C³ (ƛ_C = ℏ/(mₑc), the reduced Compton wavelength). The resulting field is (8πα)^(−½)·E_S ≈ 0.43 E_S, where E_S = mₑ²c³/(eℏ) ≈ 1.3 × 10¹⁸ V/m. Two such quanta in phase give about 0.86 E_S. If λ_C³ is used instead of ƛ_C³, the field is (2π)^(3/2) ≈ 16 times smaller (two quanta then give about 7 × 10¹⁶ V/m). Agreement to within a factor of order one is guaranteed, because mₑ, c and ℏ are the only scales in play. The factor-of-16 spread depends on a localisation convention the framing has not fixed. Until the localisation volume is derived, "the Schwinger limit becomes a prediction" amounts to a consistency check at best.

---

## Light

- **L1 — "Only the collision saturates."** Under a CW drive the whole overlap region is a standing wave with antinodes about every λ/2. The audit shows about 25,300 line → ring events in 1,500 ticks, roughly 17 nodes per tick, each feeding its own ring. "The collision and only the collision saturates" is true for the single-pulse case only. The mid-ring figures in first-run.md are one ring out of many.
- **L2 — Vacuum nonlinearity.** A hard clip predicts vacuum nonlinearity that is *exactly zero* below the ceiling and abrupt above it. QED's (Euler–Heisenberg) is analytic: small at all fields, scaling as (E/E_S)². Bright crossing beams that the §3a bridge places near the ceiling would separate the two. Worth recording as a prediction, and as a constraint on any softened ceiling.
- **L3 — Losses from crossing beams.** With the current lossy rule, two crossing beams that saturate without resonance lose energy for good. That would show up as anomalous attenuation where intense beams cross. A conserving rule removes this, which is one more reason the conserving repair comes first (F3).
- **L4 — Single pulses and coherence.** first-run.md finds no selection at all for a single pulse that is about one cycle long. The resonance needs many coherent cycles, so the predicted pair yield depends on the photons' coherence length. Real gamma photons are many cycles long, so this is not an objection, but the dependence is a prediction and should be written down.
- **L5 — Index of terms.** New terms (comb, X junction, reciprocity, Bethe–Heitler, Breit–Wheeler, Schwinger limit, intermodulation) should go into Appendix A, per the audience rule in [CLAUDE.md](../../CLAUDE.md).
