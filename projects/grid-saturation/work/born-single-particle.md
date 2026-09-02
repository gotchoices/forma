# Single-particle Born from energy density (derivation-ready)

**Status: derivation-ready (consistency-level).** Single-particle Born follows
from GRID-native ingredients with **no hidden-variable steering** — it is the
semiclassical "detection ∝ intensity." This note is the scaffold for a formal
derivation; the one thing to make rigorous is the detection coupling on the
lattice (§4).

## Claim

For a single quantum described by a GRID field ψ, the probability of detecting it
at a detector element x is

    P(detect at x) ∝ |ψ(x)|²   —  the Born rule (position).

## Premises (all GRID-native)

1. **ψ evolves by the linear GRID dynamics.** ψ is the field / de Broglie guide
   wave; on open GRID it obeys the confirmed Maxwell/KG dynamics
   ([de-broglie-dispersion-result.md](de-broglie-dispersion-result.md)). In a
   two-slit apparatus, ψ(x) is the interference pattern
   ([dual-slit-result.md](dual-slit-result.md)).
2. **Energy density ∝ |ψ|².** A wave's energy density is ∝ amplitude² (for a mode
   ψ ∼ A e^{i(kx−ωt)}, the time-averaged density is ∝ ω²|ψ|²). At the detector's
   response frequency the ω² factor is a constant, so the **spatial** energy
   distribution is ρ_E(x) ∝ |ψ(x)|².
3. **Whole-quantum absorption (grid-quantization).** The bounded substrate holds
   and transfers energy in whole quanta ([grid-quantization](../../grid-quantization/));
   a detector fires by absorbing **one** whole quantum. This supplies the *unit*
   and the *singleness* of the click — the thing a classical wave lacks.
4. **Weak (linear) detection coupling.** The absorption rate at a detector element
   is proportional to the local energy available there (linear response / Fermi
   golden rule; the standard semiclassical photodetection assumption).

## Derivation

    P(detect at x)  ∝  (absorption rate at x)          [premise 4]
                    ∝  ρ_E(x)                           [linear in local energy]
                    ∝  |ψ(x)|² .                        [premise 2]

The single quantum (premise 3) is absorbed at *one* x, drawn with weight |ψ(x)|².
Over many identically-prepared quanta the clicks accumulate into |ψ(x)|² — the
Tonomura build-up, which we reproduced (single lumps → fringes, corr→0.97,
[dual-slit-result.md](dual-slit-result.md)). **No steering, no collapse: the click
is one whole quantum absorbed where the energy density is, and that density is
|ψ|².**

## What is assumed vs. derived

- **Derived:** the *shape* P ∝ |ψ|² — from energy density ∝ |ψ|² (a wave fact) plus
  linear detection.
- **Assumed:** (a) the detection coupling is linear in local energy (premise 4);
  (b) whole-quantum absorption (premise 3, but this is grid-quantization's result,
  not a free assumption). This is the **same footing as Bohm's single-particle
  Born**, which also rests on a coupling/equilibrium premise. It is a *consistency*
  result (Born reproduced, GRID-native), not a derivation from nothing — and that
  is honest and sufficient for the single-particle case.

## What to make rigorous (to promote to a formal derivation)

State premise 4 precisely on the lattice: a detector = absorbing/mass nodes
(as in [dualslit.py](../scripts/dualslit.py)); show the whole-quantum transfer
rate into a detector node is linear in the incident edge energy at that node. Then
P ∝ |ψ|² is a lattice theorem, not an assumption.

## Scope — and the one hard core that remains

This covers **single-particle** Born only. **Multi-particle / entangled Born** (the
correlations that violate Bell) is *not* reducible to local energy density — it
needs **non-local** hidden variables. We do **not** need to assert a single theory
for that. It is enough to exhibit **one feasible placeholder** — e.g. **S itself
closed/periodic** (which need not be 3D, and could be smaller than it looks), whose
**global self-consistency** (periodic boundary conditions on a closed manifold) is
a genuine non-local constraint — to show non-local hidden variables are *feasible*
on a GRID-compatible geometry. The toy Bell test ([bell-test-result.md](bell-test-result.md))
already showed such a non-local structure reaches QM with no signaling. Other
placeholders may work equally; the point is feasibility, not a unique mechanism.
Deriving the *exact* cos(a−b) from a specific closed-geometry constraint is the one
genuinely open core.
