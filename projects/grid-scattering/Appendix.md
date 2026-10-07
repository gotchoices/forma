# grid-scattering — Appendix

Reference material for [README.md](README.md): terms, the originating premises and which survived, obstructions, and the record of what has been discarded. Nothing here is load-bearing for the project's thesis; it is here so the README can stay short and so earlier reasoning is not lost.

---

## A. Glossary

- **Winding number** (also KK momentum) — the integer *n* counting how many wavelengths a wave fits around a compact dimension. In Kaluza–Klein theory and in forma this is the charge-like label. A mode with *n* = 0 does not wrap at all.
- **Equivariance** — a rule is equivariant under a symmetry when applying the symmetry and then the rule gives the same answer as applying the rule and then the symmetry. A state the symmetry leaves unchanged then stays unchanged. Picture a perfectly symmetric ring oscillator: nothing distinguishes one point from another, so nothing can grow.
- **Parametric instability** — a uniform oscillation that is unstable to the growth of a pair of waves with opposite wavenumbers (+k, −k). Any small disturbance grows exponentially until the nonlinearity caps it. Optical down-conversion is the standard example.
- **Rotation (Givens rotation)** — a lossless crossfade between two registers. Two amounts *a*, *b* become (a cos θ − b sin θ) and (a sin θ + b cos θ); since cos² + sin² = 1, the total a² + b² is exactly unchanged. Used here only as the arithmetically correct way to implement "move the overflow".
- **ZPE (zero-point energy)** — the residual field energy that remains when nothing has been deliberately excited; semiclassically, ½ℏω per mode.
- **Sargent's rule** — the observation that weak decay rates scale as the fifth power of the released energy Q.
- **B − L** — baryon number minus lepton number; the combination believed exactly conserved where B and L separately may not be.

## B. The originating premises, and what became of them

The project began from a set of premises in a notes file. Stated here with their current standing.

| | Premise | Standing |
|---|---|---|
| P1 | One grid; a node's edges are partitioned by sheet | **The project's central claim** (README §2). An intermediate draft dropped it, on the grounds that winding conservation follows from the uniform rule anyway — but that argued past the proposal rather than against it: the uniform rule keeps *modes* apart statistically, while P1 keeps *energy* out of an orthogonal sheet entirely. They are different models with different predictions, and P1 is the one being tested |
| P2 | Sheets are closed | **Kept, with the strictness relaxed.** Closed exactly in the ideal node (θ = 0); a physical node may leak weakly, and the junction rules form a continuous family in which that is available ([work/junction-geometry.md](work/junction-geometry.md)). The weak leak is what carries ordinary propagation of a made particle; saturation carries the bulk crossing. Radiation into space at ~α can then come from either regime, which an earlier strict reading forbade outright |
| P3 | Saturation opens the cross-sheet channel | **Reframed.** The nonlinearity is what makes transfer possible at all; the question is its *rate*, not whether it opens a gate |
| P4 | Transfer is pairwise, gated by fit | **Split.** The ±n pairing survives as winding conservation. The particle/antiparticle reading does **not**: metric-mass reads ±n as two halves of *one* particle. "Fit within a width" is dropped — the width of a decaying state is an output (ℏ/τ), not a gate |
| P5 | Background fluctuation is the trigger | **Kept, demoted from discovery.** Classically a seed is needed; it is the known semiclassical stand-in for quantum spontaneity, and its size is fixed at ½ℏω per mode, not free |
| P6 | Domains are ordered by state density, not energy | **Kept.** A decay releasing more energy leaves more kinetic energy for the products, hence more phase space |
| P7 | Conservation closes an exit, not lack of room | **Kept, with the fork relocated.** A translation-invariant rule conserves every translation label exactly. So the question is not "hard law or rare coincidence" but **whether baryon number is a symmetry label of the GRID rule**. If it is, the rate is exactly zero |

## C. Corrections carried over from the originating notes

Four claims in the first formulation did not survive and are recorded so they are not re-made.

| Original | Problem |
|---|---|
| Space is the "lowest", most economical state for energy | A 511 keV photon and an electron at rest are exactly energy-degenerate. Space is the **widest** state, not the lowest — the ordering is by state count |
| The proton is stable because "there is nothing lower" | False: p → e⁺ + π⁰ is far downhill in rest mass. What forbids it is baryon number, which [mode-stability.md §3](../ma-domain/work/mode-stability.md) flags as assumed rather than derived |
| Emitting in both directions explains particle/antiparticle **pairs** | Back-to-back emission gives linear-momentum balance only. It does not forbid emitting a single fermion, and metric-mass reads ±n as one particle regardless |
| In β decay the electron and neutrino energies "just fit" the mass gap | They do not. The gap is 1.293 MeV, the electron 0.511 MeV, the neutrino ≈ 0; the remaining 0.782 MeV is a *continuous* spectrum. A fit-based mechanism may gate a rate but must not imprint structure on the partition |

The threshold condition, stated fully, is m_n − m_p > m_e + m_ν.

## D. Known obstructions

- **Fermion pairs.** Linear-momentum balance does not force pairs. The argument that does is **angular momentum** — a spin-½ initial state cannot become an integer-spin final state — with fermion parity as a second route that additionally assumes Lorentz invariance, which a lattice has only approximately. Both run through **spin**, which forma has not settled: [conservation-as-momentum.md §5](../ma-domain/work/conservation-as-momentum.md) records two competing accounts and adopts neither.
- **Baryon and lepton number.** The intuition that these are momenta underneath is already forma's working hypothesis — see [conservation-as-momentum.md](../ma-domain/work/conservation-as-momentum.md) and [baryon-number.md](../ma-domain/work/baryon-number.md). Total lepton number has **not** been observed violated; it is the separate flavour numbers that oscillations violate. B − L remains the defensible target.
- **Real versus complex substrate.** A real field cannot carry the sign of a winding. Every result obtained on one is therefore silent about charge, and the ± balance such a field shows is Hermitian Fourier symmetry rather than physics.
- **Tracks.** Any decay picture in which a quantum is "stuck on its track" should note that [sheet-proton lb-mode-localization.md](../sheet-proton/work/lb-mode-localization.md) is a negative result: no low-lying eigenmode of the modulated clover localises on the tracks.

## E. Experiments considered and their standing

**The pump test (two pulses colliding on the cylinder).** Retained as the README's §5 simulation check. Its earlier form asked whether energy "persists" in the compact sector, which a lossy clipping rule cannot answer — such a rule destroys the zero-winding sector faster than the winding sector, so a ratio rises while the absolute content falls. Fixed by requiring an exactly conserving rule and a matched control.

**A staircase in retained energy against drive amplitude.** Dropped. In a classical field the compact dimension's modes form a ladder of *frequencies*, and each mode can hold any amount of energy. Nothing in the uniform scatter or the saturating rule quantises amplitude, so a smooth curve is what the setup predicts and seeing one would falsify nothing. The testable version is *which* modes populate — frequency selection, not energy quantisation.

**A zero-point-spectrum test (inject non-resonant energy into a compact dimension).** Parked, because its stated rationale was wrong. A periodic compact dimension has **no modes between zero and the fundamental**; periodicity *empties* that band rather than giving it the flat spectral density [zpe_derivation.md](../ma-domain/work/zpe_derivation.md)'s Postulate 2 needs. A linear lattice moves no energy between modes, and a nonlinear one relaxes toward equipartition, not toward a flat sub-fundamental band. Separately, "mean energy ½ℏω₁" and "mean frequency ½ω₁" are different quantities and the earlier framing conflated them. If a version of this survives it belongs to [grid-quantization](../grid-quantization/) and needs a new rationale first.

**Whether space is periodic.** An attractive side-question — zero-point energy as an artifact of a closed space — but out of reach here. Periodicity fixes a spectrum, not an occupation, and the step to ½ℏω runs through an action quantum per cycle, where ℏ enters as a unit. There is also an empirical bound: searches for matched circle pairs in the cosmic microwave background have found none, placing any fundamental domain at or beyond the observable universe.

## F. Numerics mentioned in earlier drafts

Several figures circulated during framing — exact winding conservation under a symmetric seed, an energy drift of ~10⁻¹⁴ under a rotation rule, a "2,500×" transfer against a linear control, and a clipping artifact in which the winding *fraction* rose 24-fold while the absolute amount fell. **None of these is published.** They live in no script and no work file, and at least one (the 2,500×) is a ratio of an end value against a flat baseline, which grows with run length and is not a rate. They are recorded here as indications only. Per [AGENTS.md](../AGENTS.md) they would need a script and a work file before anything is built on them, and the README deliberately builds on none of them.

## G. Methodological rules adopted

- **No transfer claim from a ratio** unless it is measured against an energy-conserving control, and unless the quantity is stable against run length.
- **Rates, not fractions.** A plateau is an end state; decay rates and cross-sections are probabilities per unit time. The observable is a growth rate.
- **Derivation before simulation** where a derivation is available.
- **Define terms on first use.** The audience rule in [CLAUDE.md](../../CLAUDE.md) applies to this project's files as much as to its chapters.

## H. Provenance of the per-sheet node

**Largely superseded by [work/junction-geometry.md](work/junction-geometry.md)**, which settles the question analytically. Two points that file does not repeat:

Nothing in the repo proposed grouping a node's edges before this project, and nothing ruled it out. The uniform form S = (2/N)·J − I over all of a node's registers is simply what has always been written, and [grid-duality ch. 6](../grid-duality/06-3d-extension-and-lattice-closures.md) generalises it without asking whether a node touching several sheets should pool them.

The cost arrives at the third dimension: sheets in ma-domain *share* dimensions ([leakage-rate.md §3](../ma-domain/work/leakage-rate.md) has the electron on Ma(m1, m2) and the muon on Ma(m1, m3)), so a node where both meet must carry two separate m1-edges. That changes its coordination, and coordination sets impedance and wave speed — to be checked against [grid-duality's test bench](../grid-duality/03-test-bench.md) before any physics is read off it. On the two-dimension arena of README §3 the question does not arise.

## I. Energy, amplitude and frequency on the GRID

A question worth settling, since it bears on how overflow is accounted.

For many waves, energy goes as **amplitude² × frequency²**, not amplitude² alone. A mass on a spring with displacement A·cos(ωt) has velocity Aω·sin(ωt) and energy ½mA²ω². So a 1 V peak-to-peak *displacement* at 1 kHz carries 10 000 times the energy of the same displacement at 10 Hz.

Whether the ω² appears depends entirely on what the stored variable *is*.

- If a register holds a **displacement**, energy carries the ω² factor.
- If a register holds a **travelling-wave amplitude in power-normalised units** — the forward and backward waves a± on a lossless transmission line — then power is |a±|² with no frequency factor at all, because the normalisation has already absorbed it.

GRID is the second kind, and this is forced rather than chosen: the scatter S = (2/N)·J − I is orthogonal, so the quantity it conserves exactly, tick after tick, is the plain sum of squared register values. That sum is what "energy" means on this substrate. No frequency factor enters, and none can without breaking the conservation the scatter already provides.

Two consequences. First, energy bookkeeping and amplitude bookkeeping are the *same* bookkeeping here, so an overflow rule that balances the sum of squares is not importing anything foreign. Second, the separate idea that **energy per cycle is ℏω** — Postulate 1 of [zpe_derivation.md](../ma-domain/work/zpe_derivation.md) — is a quantum statement layered on top of this classical ledger, not a competing account of it. The two live at different levels and do not conflict.

## J. The standard name for the mechanism

What §3 of the README describes has a name in ordinary physics: a **parametric process** — a driven oscillation decaying into a pair of counter-propagating partners with opposite wavenumber, +n and −n. Optical down-conversion and the Faraday ripple instability are the textbook cases.

The identification is worth recording for two reasons, and worth keeping out of the README for one.

*Why it is useful.* It says what quantity to compute. For a parametric process the meaningful observable is the **growth rate** of the pair — how fast the ring's content builds, which is what the README's objective 2 asks for in plain terms — and the standard method is to linearise about the driven state and ask which pairs are unstable. It also warns against a trap: such a process saturates at a level set by the nonlinearity, *independently of how small the initial nudge was*, so a final amount says nothing about how fast the process runs and a smaller seed only delays the plateau logarithmically.

*Why it stays here.* The name is a label, not an argument, and reaching for it early replaced a mechanical picture the project is built on with a formalism that obscured it. The README should be readable without it. Use it when the simulation produces something to analyse, not before.
