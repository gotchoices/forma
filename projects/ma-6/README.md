# ma-6

**Type:** Exploratory architectural project (see [../README.md](../README.md))
**Scope:** A six-dimensional compact Ma domain hosting all Standard Model fermions, with the apparent particle-sheet structure emerging from a sparse cross-term pattern in the 6×6 metric rather than imposed a priori.
**Status:** Early. Initial work files moved from [sheet-proton](../sheet-proton/) (3-torus.md, ma-share-6.md, the corresponding scripts and outputs). Active checklist + work plan in [work/STATUS.md](work/STATUS.md). The original sheet-proton project is on hold while this reframe is explored.

## Why this project exists

The current MaSt framework ([model-F](../../models/model-F.md)) builds three independent particle sheets (e, p, ν), each a 2-torus with its own (ε, s) parameters. Three different mechanisms — Z₃ confinement on the p-sheet, R53 shear-resonance on the e-sheet, low-shear modes on the ν-sheet — live on three separate compact structures. The architecture works but it is *plural*: three separate dim-pairs with three separate physical rules.

This project asks whether the three sheets are actually different *regions* of a single six-dimensional Ma domain, with the apparent sheet structure emerging from which dim-pairs have nonzero off-diagonal entries in a single 6×6 metric.

The reframe:

- **Six compact dimensions** in one Ma domain (not three sheets each with two dims).
- **Mostly diagonal 6×6 metric**, with a small number of non-zero off-diagonals (cross-terms).
- **Cross-term type determines particle class** at each dim-pair: three cross-terms carry τ = 1/3 twists (host the three quark generations via the clover-quarks mechanism); some carry R53-style shears (host charged leptons); the rest are zero (the dim-pair is orthogonal, no mode forms).
- **Sheets are emergent classifications** of dim-pairs by their cross-term type, not fundamental partitions.

## What is inherited as a working result

The project takes the following from [sheet-proton](../sheet-proton/) as inputs:

- **The clover-quarks 1/3-twist mechanism.** A 3-lobed cross-section with τ = 1/3 boundary identification gives Q_lobe = +2/3 (up quark) and Q_saddle = −1/3 (down quark) from per-arc geodesic curvature integration; baryon path-windings, Z₃ confinement, and proton/neutron structure all follow. See [sheet-proton clover-quarks.md](../sheet-proton/work/clover-quarks.md).

- **The R53 / model-F in-sheet shear-resonance.** Three charged-lepton masses fit at an extreme (ε, s) point via shear cancellation of the dominant kinetic term. See [R53-three-generations](../../studies/R53-three-generations) and [model-F.md](../../models/model-F.md).

Both are taken as given here; this project's job is to fit them — and the rest of the fermion spectrum — into the unified 6-dim domain architecture.

## Approach

See [work/STATUS.md](work/STATUS.md) for the phased work plan. Briefly:

1. **Phase 0** — naming convention for the 6 Ma dims (reconciling with existing study notation where possible).
2. **Phase 1 (quark sector)** — pin the 3 mutually-twisted dims that host the quark structure; find the range of dim scales that works for all 3 quark generations.
3. **Phase 2 (electron sector)** — pin the 3 e-dims; solve for the charged-lepton modes; decide whether electrons need clover-style internal structure and/or a twist of their own.
4. **Phase 3 (neutrino sector)** — keep the ν-sheet at its existing 2-dim (R49 / R61) picture; extend only if forced.
5. **Phase 4** — if preliminary results cohere across all three sectors, promote from exploratory `work/` files to a mathematical derivation in `ma-6/` proper.

## Working assumptions

- The lowest modes that satisfy closure conditions are the observable particles.
- Higher unobserved modes are energy-unfavored and reduce to simpler degeneracies — dark modes, spatially separated states (cf. R56), or composite resonances.
- 6 total dims is the working size; expansion to 7+ or contraction to 5 is allowed if the structural rules demand it.
- The neutrino sector stays minimal (the existing R49 / R61 2-dim picture) until evidence forces an extension.

## Relation to other projects

- [sheet-proton](../sheet-proton/) — on hold while this reframe is explored. Provides the inherited clover-quarks mechanism.
- [metric-binding](../metric-binding/), [metric-mass](../metric-mass/), [metric-charge](../metric-charge/) — foundational MaSt frameworks; this project extends the metric-binding architecture but to a 6-dim compact domain.
- [studies/R53-three-generations](../../studies/R53-three-generations), [studies/R60-metric-11](../../studies/R60-metric-11) — the empirical fits and architectural commitments the present project is trying to reorganise into the unified 6-dim picture.
