# Detection theorem for single-particle Born (Ch 7)

**Question:** are Ch 7's two premises — "energy density ∝ |ψ|²" and "linear
whole-quantum detection" — GRID-native, or assumed? **Verdict: the GRID-native
parts close cleanly; one standard photodetection premise remains, and it is the
*same* premise all of physics uses. Ch 7 derives the Born *distribution* at
standard footing.**

## (a) The energy density *is* |ψ|² — clean

The orthogonal scatter conserves **ρ(x) = Σ_d inn_d(x)²** (sum of squared edge
amplitudes). This *is* the physical energy density, and it *is* what the
interference pattern plots ([dual-slit-result.md](dual-slit-result.md)). Define the
intensity **|ψ(x)|² := ρ(x)** — this is the natural, conserved, gauge-invariant
field intensity. (The alternative |Σ_d inn_d|² differs only by coherence-dependent
cross terms and gives the *same spatial pattern*; the fringe distribution is ρ.)
So "energy density ∝ |ψ|²" is **an identity, not an assumption.**

## (b) A detector is an absorbing node → capture rate is *automatically* linear

A detector element at x is an **absorbing node** (as in the two-slit barrier:
field forced to 0). Each tick it removes the incident field, so the energy it
captures is exactly the **incident energy density ρ(x)** arriving there. Capture
∝ ρ(x) is therefore **not an added coupling assumption — it is what "absorbing"
means.** Combined with **whole-quantum transfer** (grid-quantization: energy moves
and is absorbed in whole quanta, giving *one* click, not a fraction —
[grid-quantization](../../grid-quantization/)), the single quantum is captured at
x at a rate ∝ ρ(x).

## The chain

    P(click at x)  ∝  capture rate at x   [detector = absorbing node]
                   ∝  ρ(x)                 [absorbs incident energy density]
                   =  |ψ(x)|² .            [ρ is the intensity, by (a)]

⇒ **P(x) ∝ |ψ(x)|²** — the Born rule for position. Whole-quantum (grid-quantization)
gives the *single* click; ρ ∝ |ψ|² gives the *distribution*.

## The one residual premise — and it is not GRID-specific

The step "P(click) ∝ capture *rate*" treats the whole-quantum capture as a
**probabilistic** event with probability ∝ local energy (the golden-rule / Poisson
detector). In a *deterministic* substrate one must say where that randomness comes
from — and there are exactly two honest readings, both standard:

- **Phenomenological (semiclassical):** model the whole-quantum capture as
  stochastic with rate ∝ local energy. This is how *all* photodetection theory
  works; given it, Born follows. Standard and physically motivated — real detectors
  are weak-linear — but a *detection model*, not derived from S.
- **Hidden-variable:** the capture point is fixed by the ℵ-phase (Ch 8); over the
  trial ensemble of phases, capture positions distribute ∝ ρ *if* the phase
  distribution is equilibrium. This *derives* the randomness but needs the
  equilibrium (∝ρ) — the deeper, **shared** measurement question (links to Ch 9).

Either way the **Born distribution P ∝ |ψ|² is the result**; "which" is the origin
of quantum randomness — a question *every* framework carries, not a GRID-specific
gap.

## Status

**Ch 7 is derivation-ready** for the Born *distribution*, at the same footing as
standard semiclassical photodetection. The GRID-native content is solid and
identity-level: **energy density = ρ = |ψ|²** (from scatter unitarity), **linear
capture** (from "absorbing node"), **single click** (from grid-quantization). The
one input — probabilistic capture ∝ local energy — is the universal photodetection
premise, with its deterministic origin flagged as the shared measurement question.
**[D, modulo the standard detection premise]**
