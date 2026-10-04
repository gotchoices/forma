# grid-scattering — framing review

**Scope:** The framing in [README.md](README.md) as of commit c7c5155, read against its originating notes in [../thoughts.md](../thoughts.md) and the files it cites. It covers logical and structural problems only. The project sitting outside accepted physics is not counted as a problem; reasoning that does not follow, or that contradicts the repo's own established results, is.

Items are numbered so later discussion can refer to them (F1, M3, …).

**Terms used below.**
- **Winding** (or KK momentum): the integer n counting how many wavelengths a mode fits around a compact dimension. In Kaluza–Klein (KK) theory, and in forma, this is the charge-like label.
- **Equivariance**: a rule is equivariant under a symmetry if applying the symmetry and then the rule gives the same result as applying the rule and then the symmetry. A state that the symmetry leaves unchanged then stays unchanged.
- **Parametric instability**: a uniform oscillation that is unstable to the growth of a pair of waves with opposite wavenumbers (+k, −k). Any small perturbation grows exponentially until the nonlinearity limits it. Optical parametric down-conversion and the Faraday ripple instability are standard examples.

---

## Fatal

### F1 — The project no longer has a single thesis; its central modification does no work

The README states its thesis three times, and the three versions disagree:

- **Title question and boxed proposal (§2):** the node treats dimensions uniformly, and that is the problem. The fix is to give edges sheet labels and close scattering within each sheet, then let *saturation open the channel* between sheets.
- **P2:** sheet closure is a *theorem of the uniform rule*. The numerical check was run on a periodic three-axis lattice with the ordinary uniform scatter, and no edge partition was needed. P1's sheet labelling is therefore not doing the closing.
- **P3:** saturation *does not* open the channel, it amplifies one that a seed has already opened.

The text that follows the boxed proposal has not been brought into line:
- §2.2 begins "If P1–P3 hold" and then (item 3) puts the weak coupling down to transfer happening "only on overflow". P3 contradicts that.
- P5 still has zero-point fluctuation "pushing nodes over the saturation threshold" as the trigger.
- Chapter 4 asks "what opens cross-sheet transfer". Under P2/P3 the answer has already been given as "the seed".
- The index entry in [../README.md](../README.md) still says scattering is "sheet-closed **by momentum**" and that saturation "opens the cross-sheet channel". The revision dropped both claims.

The structural result: §1 sets up the uniform rule as the obstacle and the sheet-labelled rule as the cure, but by the README's own P2 the uniform rule already gives the property the cure was meant to supply. What the project now actually asks is the question at the end of §2.1a: *what breaks the symmetry, and can seed plus amplification reach observed rates?* That question has nothing to do with the title question or P1. The title, the §2 box, §2.2, the chapter arc and the index entry all need to be rebuilt around the actual question. The alternative is to show a job that P1's partition does and the uniform rule cannot (see F2 and F4: it is not obvious that such a job exists).

### F2 — P2's "theorem" depends on the test geometry, contradicts the ma-domain architecture the project adopts, and claims more than it shows

There are three separate problems.

**(a) Sheets in ma-domain share dimensions, so "every edge of one sheet is orthogonal to every edge of every other" is false.** §2 takes on ma-domain's reading (a sheet is a dim-pair `Ma(i, j)`). In that reading, sheets meet along shared dimensions. In [leakage-rate.md §3](../ma-domain/work/leakage-rate.md) and the K4 candidates, the electron is on `Ma(m1, m2)` and the muon on `Ma(m1, m3)`, so the two sheets share m1. An edge along m1 belongs to both. The sheets therefore cannot be "partitioned" by labelling edges (P1) unless edges along shared dimensions are duplicated. The README does not mention duplication, and duplication would alter the scatter's coordination, impedance and wave speed, which feeds into ch. 1's test bench. The "every exit is a 90° turn" picture breaks down for exactly the sheet pairs where ma-domain expects the strongest leakage.

**(b) The closure follows from the product-torus test lattice, not from the physics.** On a lattice that is periodic and translation-invariant along every compact axis at every node, a linear rule separates into Fourier sectors. That is all "orthogonal sheets are orthogonal subspaces" amounts to. ma-domain's geometry is different. Two sheets sharing dimension i form S¹ᵢ × (figure-eight), with a junction where the non-shared loops meet ([leakage-rate.md §3.3](../ma-domain/work/leakage-rate.md)). The junction removes translation symmetry along the non-shared dimensions, and *linear* leakage between the sheets is then allowed. Only the shared-dimension winding is conserved, and leakage-rate.md has already derived this as a Bloch-orthogonality selection rule (§3.1: "charge conservation realised as a geometric selection rule"). So:
- what P2 legitimately shows (a translation label is conserved) is already in the repo, and does not justify calling it "the project's first real finding" (§9 step 2);
- what P2 adds beyond that ("no cross-sheet physics at all without a seed") comes from testing on a product torus. It is not a property of the architecture the project serves. This is the parameterization-artifact trap: a property of the provisional test setup reported as a structural result.

**(c) The theorem rules out the one coupling forma is surest of.** Taken literally (linear, translation-invariant along every compact axis), P2 stops a mode with compact winding n ≠ 0 from ever giving energy to the n = 0 sector. Ordinary light in S belongs to that sector. Yet the electromagnetic radiation of a charged mode into S at rate ~α is the coupling §1 quotes as "demonstrably" existing, and ch. 5 has to reproduce it. In KK theory that coupling is a *nonlinear* term (n) + (−n) → 0 that conserves total winding. It is not a symmetry breaking. The framing has to say which statement it means:
- **total winding (charge) is conserved:** a selection rule, which is desirable and already in the repo; or
- **sectors can never exchange energy:** this is false once any non-uniform state is present, and if it were true it would kill ch. 5.

The README's argument moves from the first statement to the second.

### F3 — The "symmetry problem" of §2.1a is a classical-field artifact, so the gating experiment (§9 step 1) asks the wrong question

The equivariance argument only applies to an initial state that is *exactly* uniform along the compact axis, as a classical field. Two consequences follow.

1. **In a quantum, or even a statistical, description the symmetric state can produce a pair.** A pair state with windings +n and −n has total winding 0 and is itself translation-invariant. γγ → e⁺e⁻ breaks no symmetry. The classical field has to "break" one only because a classical field cannot hold a correlated ±n pair with zero mean amplitude. This is the standard gap between classical and quantum parametric down-conversion. Classically it needs a seed. Quantum mechanically it happens spontaneously, and the semiclassical stand-in for "spontaneously" is a zero-point background of ½ℏω per mode. So P5's "vacuum seed" is not an extra ingredient the mechanism needs to search for. It is the known semiclassical substitute for quantum spontaneity, and **its amplitude is not a free parameter: it is ½ℏω per mode.**

2. **The 2,500× result looks like a saturated parametric instability, and the plateau height of such an instability does not depend on the seed.** A seeded instability grows exponentially at a rate set by the nonlinearity and the drive, and stops at a level set by energy conservation and the nonlinearity. A smaller seed only delays the plateau, by an amount that grows as the logarithm of 1/seed. Three things follow:
   - Step 1's kill criterion ("is the plateau capped near the seed?") cannot come out negative in the way it fears, and a positive result does not show that physical rates are reachable.
   - A plateau is a final *fraction*, not a *rate*. Decay rates and pair-production cross-sections are transition probabilities per unit time. The quantity that matters is the **linear growth rate** of the ±n pair about the uniform state, or its below-threshold equivalent, plus the seed level fixed by item 1. That pair maps directly onto Fermi's-golden-rule language, which [leakage-rate.md §2](../ma-domain/work/leakage-rate.md) already uses.
   - "2,500× the linear control" is a ratio of two end values, and the control is flat, so the number grows with run length and with the arbitrary parameters §2.1a admits to. It is not a gain in any stable sense. The project's own methodological rule (no claim from a ratio) should cover it.

The first experiment should be re-posed. Linearize about the driven uniform state, find which (+n, −n) pairs are unstable and at what growth rate, then see how that rate depends on drive amplitude, on nonlinear strength and on the geometry. This is a derivation, which is the method [AGENTS.md](../AGENTS.md) prefers, and simulation is only needed to check it.

### F4 — The "saturation-independent" fallback (chapters 2–3, the "Minimum" success criterion) cannot be reached by the proposed means

§6 and §7 present chapters 2 and 3 as standing on their own if the channel work fails. Neither follows from the rule being proposed.

- **Chapter 2 (1D tower).** The 1D-line modes are eigenmodes of the 3-torus Laplacian. Any node rule that passes grid-duality's fidelity test (ch. 1's requirement) reproduces the same continuum wave equation, and therefore the same spectrum and the same mode shapes. Whether a mode is *charged* is not a property of the mode's internal dynamics. It depends on how the mode sources a field in S, meaning which functional of ψ is the monopole moment. [3-torus.md](../ma-domain/work/3-torus.md) says what calculation decides it: re-running R19's monopole derivation on a 3-torus. A rule for scattering inside the compact space does not contain the coupling to S, so it cannot choose between Candidates I, II and III. The hoped-for argument ("a 1D mode never takes part in the two-edge split that defines a plane") also breaks under the README's own P1. A mode with winding only along dimension a still lives on every sheet that contains a, propagates on those edges, and splits at every node. The README admits the argument "cannot simply be 'it does not participate'" but gives no other candidate mechanism. The chapter has a target and no route to it.
- **Chapter 3 (plane over diagonal).** Equivariance protects *every* winding sector the same way. A 3D-mixed mode, with winding on all three axes, is just as stable under it as a 2D-planar mode. The theorem says sectors are kept apart. It says nothing about which sectors particles occupy. [architecture.md §3.3](../ma-domain/work/architecture.md) is about why 3D-mixed modes are *dark or unoccupied*, and dynamical closure does not touch that. §2.2 item 2 ("dynamically closed rather than merely expensive") and the ch. 3 row ("looks like the missing mechanism") are non-sequiturs.

If both chapters fail for these structural reasons rather than on the physics, §7's "Minimum" and "Also a result" criteria are not real fallbacks. A failure there would be a failure of the method, not an instructive negative about Candidate III.

---

## Moderate

### M1 — "Breaking the symmetry" mixes up breaking it in the rule with breaking it in the state, and only one of these keeps charge conserved

§2.1a asks "what breaks the symmetry?" as though any answer will do. They are not equivalent:
- If the *rule* breaks compact-axis translation symmetry (defects, inhomogeneous nodes, a pair of registers picked out by position), winding is no longer conserved. Since winding is charge, the mechanism then breaks charge conservation.
- If only the *state* breaks it (background fluctuations), total winding stays conserved, and the background has to supply the matching ±n content. That makes the vacuum a charge-neutral reservoir of winding, which is a substantive claim and should be stated as one.

The Givens-rotation test applied its rotation "between a chosen pair of registers". The framing should state that this choice was uniform along the compact axis (the symmetric-seed run returning 0 → 0 suggests it was) and should require it of every later rule.

### M2 — P7's "internal tension" is placed in the wrong spot

The README sets ma-domain's hard topological baryon number (option a) against "this project's mechanism", which it says naturally gives a tiny but non-zero rate (option b). By F2 and M1, though, a seed-plus-gain mechanism with a translation-invariant rule conserves every translation label *exactly*. If baryon number is such a label (a winding, or a cut-space invariant of the dim-graph), the mechanism gives (a), with no tension. The mechanism gives (b) only for quantities that symmetry does not protect. The real fork is therefore *whether baryon number is a symmetry label of the GRID rule*, and the 10⁻⁶⁵-per-cycle target only matters on one branch of it. Also, "cycle" in that figure needs defining: it matches the proton's Compton frequency, about 2.3 × 10²³ Hz.

### M3 — P4's "fit within a width" is either redundant or harmful

- If S always takes up the remainder continuously (correction 4), a channel opens exactly when the threshold is cleared (Q ≥ 0, with Q the released energy) and the conservation laws allow it. A width adds nothing to "whether". The width that matters physically belongs to the *decaying* state, and it is an output (ℏ/τ, with τ the lifetime), not a gate.
- "Less than a whole quantum merges into that sheet's background" describes an energy sink below threshold. Below 1.022 MeV, γγ collisions scatter elastically and lose no measurable energy into a hidden sector. Either the merged energy comes back exactly and reversibly, in which case it is not a channel, or the premise predicts missing energy that has not been seen.
- The same bullet still offers symmetric spill as "a candidate account of why particles arrive in particle/antiparticle pairs". Correction 3 in §3 retracted that account, and the caution paragraph further down P4 undercuts it as well.

### M4 — §5.1's "staircase" prediction confuses frequency spacing with energy quantization

In a classical field, the mode ladder of a compact dimension is a ladder of *frequencies*. Each mode can hold any amount of energy. Energy retained against drive amplitude would only show plateaus "at the sheet's mode spacing" if something in the rule fixed amplitudes to discrete values. Neither the uniform scatter nor the Givens rule does that, and the ℏω-per-quantum scale is set elsewhere (the principle-versus-scale rule cuts both ways here). Without an amplitude-quantizing mechanism, a smooth curve is what the setup predicts, and seeing one would falsify nothing. Either name the mechanism, or recast the prediction in terms of *which* modes are populated (frequency selection), which the classical setup can test.

### M5 — §5.2 rests on a misreading of what periodicity does to the low end of the spectrum

- A periodic compact dimension has **no modes between 0 and ω₁** (ω₁ being the fundamental frequency, the lowest non-zero mode). Any injected waveform, "non-resonant" or not, is exactly a sum of the harmonics that are allowed. Nothing has to "become self-consistent on returning to its starting point", and no energy can sit in a sub-fundamental band. Periodicity *empties* that band. It cannot give it the flat spectral density that Postulate 2 of [zpe_derivation.md](../ma-domain/work/zpe_derivation.md) needs. The "shape — plausibly derivable" bullet has the logic backwards.
- A linear lattice does not move energy between modes at all, so the final spectrum is just the injected spectrum. A nonlinear lattice relaxes toward equipartition (equal energy per mode, the classical Rayleigh–Jeans outcome), not toward a flat sub-fundamental band. Neither case gives the predicted shape.
- "A mean energy of ½ℏω₁" and "the ½ω₁ mean in units of the fundamental" are two different quantities: the first is an energy, the second a mean *frequency*. A flat band from 0 to ω₁ has mean frequency ½ω₁. That is a statement about where the spectrum sits, not a zero-point energy. The proposed falsification test (the mean must not depend on how much energy is injected) is pinned to the frequency reading, while the headline prediction uses the energy reading.

In its current form §5.2 would produce a result that cannot be interpreted.

### M6 — Load-bearing numerics have no provenance

P2's "exactly zero to machine precision", P3's 2,500×, the 1.4 × 10⁻¹⁴ energy drift, the clipping figures (25.4 → 5.4) and the Hermitian-symmetry pairing check all appear as results. The project folder holds only the README, and §9 says "a prototype already runs" without pointing to it. Under [AGENTS.md](../AGENTS.md) these belong in a script and a work file before the framing builds on them. That matters especially here, because F3 suggests a different reading of the main number.

### M7 — The motivating problem is cited from a superseded architecture, with conflicting terminology

[3-torus.md](../ma-domain/work/3-torus.md) describes itself as a *historical* investigation of per-sheet 3-tori, "predat[ing] the current candidate analysis in candidates.md, which adopts a dim-pool reading". §1 of the README describes "a sheet with three compact dimensions". §2 then defines a sheet as a *pair* of dimensions. The 1D-tower problem has to be restated in the dim-pool architecture before the project can claim to solve it: what a 1D-line mode is on a single pool dimension, and which sheets it touches. Without that restatement, ch. 2's target is not clearly the problem ma-domain actually has.

### M8 — No quantitative rate test apart from α and g_W

ch. 5 targets ~α and "the right smallness" of the weak coupling (g_W, the weak coupling constant). The repo already has a stronger and checkable target: [leakage-rate.md §4](../ma-domain/work/leakage-rate.md) recovers Sargent's rule (decay rate ∝ Q⁵ for weak decays) and lepton universality to about 0.2% from phase space alone. Whatever mechanism this project proposes has to reproduce the Q⁵ scaling, or show how its gating combines with phase space to give it. It should also land in the neutron's ~880 s lifetime range at the internal cycle rate. Neither appears as a pass/fail criterion. Also, P5's claim that a coincidence process gives the exponential decay law is true but does not discriminate, since any constant-rate (golden-rule) process gives the same law.

### M9 — Precursor ordering contradicts itself

The Status line and the §5 introduction say the two precursor experiments "should run **before** this project's own work starts". §9 says they "are **not** the place to start" and that §5.1 "is currently uninterpretable". §5.1's "If it fails" clause also says the project moves on to chapters 2–3, which F4 calls into question. Choose one ordering and state it everywhere.

### M10 — The complex-field re-test changes the substrate without saying so

§9 step 3 calls for re-running the pairing check "on a complex field". GRID edge registers in the uniform scatter are real. Two ways forward are available:
- move to two real degrees of freedom per edge, which [grid-primitive](../grid-primitive/README.md) already has as (e, φ) and which is the natural candidate;
- double every register.

Either way the primitive changes, and that change has to be checked against grid-duality's test bench before the pairing result can count. The framing should say which way it goes. It should also note the consequence for the real-field results quoted elsewhere in the README: a real field cannot carry the sign of a winding, so none of the real-field runs can say anything about charge.

---

## Light

- **L1 — Lepton number.** "Lepton number is not exactly conserved" is too strong. Neutrino oscillations violate the separate *flavor* lepton numbers (L_e, L_μ, L_τ). No violation of *total* L has been observed, since there is no neutrinoless double-β decay. B − L (baryon number minus lepton number) is still the right target, but the reason given should be corrected.
- **L2 — Fermion parity argument.** The "odd number of fermion fields cannot be a scalar" argument assumes Lorentz invariance, which a GRID lattice has only approximately. The angular-momentum version (spin-½ cannot become integer spin) relies on less and should come first.
- **L3 — "Momentum is conserved at the uniform scatter."** P2 does not define what momentum means for a scalar register scatter (for example, the sum of each edge direction times its energy flux). Without a definition, "conserved at every coordination tested" cannot be checked.
- **L4 — Node-level saturation under partitioned edges.** §4 requires saturation to act on the node's summed input T. Once edges are partitioned by sheet (P1), it is unclear whether T means each sheet's own sum or the whole node's sum. Only the whole-node sum couples sheets, so this choice *is* the coupling and should be stated.
- **L5 — P6 wording.** "Rest mass contributes no momentum" is loose. The real point is that a decay releasing more energy (a larger Q) leaves more kinetic energy for the products and therefore more phase space. The factor "ln(V/λ³)" in the §3 table appears with no explanation; it is the log of the number of positions available to a particle in volume V, at its wavelength λ.
- **L6 — Stale index entry.** [../README.md](../README.md)'s description of this project needs updating once F1 is settled (see F1).
- **L7 — Undefined terms for the target reader.** Equivariance, Givens rotation, Hermitian Fourier symmetry, GUT, B − L, FGR, Bloch label and ZPE are used without definition, which conflicts with the audience rule in [CLAUDE.md](../../CLAUDE.md). A short glossary at the top of the README would fix this.
- **L8 — Correction 4 threshold.** "The gap must exceed m_e" should read m_n − m_p > m_e + m_ν. The difference is negligible in size, but the full form keeps the conservation bookkeeping visible.
