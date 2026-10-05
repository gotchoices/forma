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
| P1 | One grid; a node's edges are partitioned by sheet | **Dropped.** It does no work — winding conservation follows from the uniform rule with no partition, and sheets in ma-domain *share* dimensions, so edges cannot be cleanly partitioned anyway |
| P2 | Sheets are closed | **Kept, narrowed.** True as a *selection rule* (winding is conserved), not as a barrier. Read as a barrier it would forbid radiation into space at rate ~α, which is the one cross-domain coupling forma is surest of |
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
