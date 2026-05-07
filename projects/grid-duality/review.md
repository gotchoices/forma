# Review — projects/grid-duality

The original review was substantial and is now largely incorporated into the project (see [STATUS.md](STATUS.md) for the chunked execution plan). On a fresh re-read, the verdict (Scattering wins) is now well-grounded:

- The transmission-line / register / inhale-exhale reframing of Scattering ([models/scattering.md](models/scattering.md), [chapter 2 §7](02-candidate-models.md), [chapter 4 §5](04-model-comparison.md)) closes the "two-channel cheating" concern definitively. The two values per edge are at the edge's two physical ends; nodes are N-register processors enforcing voltage continuity and Kirchhoff's current law; the scattering matrix S = (2/N)·J − I is the unique solution to those constraints, not an arbitrary update rule.
- The new 2D coord-3 dispersion test (L1b) shows Scattering is *mildly* dispersive (0.35 ± 0.06) rather than perfectly non-dispersive — and that the perfect non-dispersion of L1a was a coord-2 artifact. Verdict survives, more honestly stated.
- The new free-wave superposition test (L3b) and dial-aware IC fair-shake (L4) decisively close the "is RelCos-both being treated fairly?" question — three independent failure modes, with L4 actually showing *worse* behavior under the model's natively preferred IC.
- The implementation-level issues (gauge non-invariance under v → v + c, edge-update verbal/code mismatch, v = 0 default IC's preferred direction) are now documented in [models/relcos-both.md](models/relcos-both.md).

What follows is the residual list — small inconsistencies of presentation that don't affect the verdict.

---

## Moderate

- **[ADDRESSED]** ~~**README's Scattering claim doesn't reflect L1b.**~~ The README §"The setup in brief" Scattering description now reads "non-dispersive at coord 2 (v_g = 1.000 at every k) and mildly dispersive at coord 3 (v_g = 0.35 ± 0.06 across the tested k range)."

- **[ADDRESSED]** ~~**README ground rule 3 vs chapter 1 §3/§5 on edge polarity.**~~ Ground rule 3 now reads: "Lattice geometry and the master clock concept are foundational. Edge polarity and common-direction orientation are labeling conventions the substrate makes available — used by the v-i paradigm (which reads s_e = ±1 from polarity) and inert under Scattering (whose registers are unordered). State structure, update rules, and clock-phase count are model-dependent."

---

## Light

- **[ADDRESSED]** ~~**Chapter 3 §3 IC translation uses (a_fwd, a_bwd) labels while chapter 2 §7 and [models/scattering.md](models/scattering.md) use the register language.**~~ Chapter 3 §3 now includes a bridging paragraph identifying a_fwd with the head-end register and a_bwd with the tail-end register, noting that the test code retains (a_fwd, a_bwd) for sim-maxwell compatibility.

- **[ADDRESSED]** ~~**Chapter 4 §2 results table L1a row**~~ now reads "1.000 (non-dispersive at every k; coord-2 swap-matrix artifact)" with the qualifier inline.

- **[ADDRESSED]** ~~**Chapter 4 §3 G2 narrative keeps "category error in the test" alongside the better wave-equation-vs-relaxation framing.**~~ The "category error" phrasing has been replaced with: "Scattering's update is unitary; under fixed-source pinning, it does not relax — it carries energy away as outgoing waves. The dynamic field around a pinned source therefore stays localized near the pin (force p ≈ −0.6 instead of −1). This is consistent with a wave equation, not a relaxation equation."

- **[OPEN — DEFERRED]** **Normalized's +11.6% energy drift in the Y-junction test is explained ("the way the 1/N factor interacts with non-uniform coordination") but not diagnostically confirmed.** A controlled experiment — longer arms (separates per-step drift from boundary effects), or eigenvalue analysis of the Y-tree update matrix — would either pin down the root cause or surface a different one. Marked optional in the original review; deferring as Normalized is not the chosen model and the chapter-4 wording is already qualified ("approximately matched-impedance...not exactly...non-trivial energy drift"). Can revisit if the project has reason to lean harder on Normalized later.

---

## Verdict on the verdict

Solid. The chapter-4 conclusion (Scattering is the winning model) is now grounded on three independent legs — metric performance, transmission-line-network naturalness, and bridge-to-grid as downstream consequence — rather than the original framing of "passes the tests we chose." The two-channel concern is closed by the register reading. RelCos-both's elimination is grounded after L3b and L4 in three independent failure modes (junction nonlinearity, Dirichlet-pinning instability, free-wave nonlinearity). [grid-quantizing.md](grid-quantizing.md) opens a clean follow-on direction (binary-substrate hypothesis) without disturbing the chapter-4 verdict.

The remaining items above are presentation polish; none threaten the project's substantive conclusions.
