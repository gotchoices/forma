# ma-domain

**Type:** Exploratory architectural project (see [../README.md](../README.md))
**Scope:** An N-dimensional compact Ma domain hosting the three fundamental particle classes (proton, electron, neutrino), with the apparent particle-sheet structure emerging from a sparse cross-term pattern in the N×N metric rather than imposed a priori. The current working assumption is N = 6, but the architecture is not bound to that count — 5 or 7 are allowed if the structure demands it.
**Status:** Early. Initial work files moved from [sheet-proton](../sheet-proton/) (3-torus.md, ma-share.md, the corresponding scripts and outputs). Active checklist + work plan in [work/STATUS.md](work/STATUS.md). The original sheet-proton project is on hold while this reframe is explored.

## Why this project exists

The current MaSt framework ([model-F](../../models/model-F.md)) builds three independent particle sheets (e, p, ν), each a 2-torus with its own (ε, s) parameters. Three different mechanisms — Z₃ confinement on the p-sheet, R53 shear-resonance on the e-sheet, low-shear modes on the ν-sheet — live on three separate compact structures. The architecture works but it is *plural*: three separate dim-pairs with three separate physical rules.

This project asks whether the three sheets are actually different *regions* of a single N-dimensional Ma domain, with the apparent sheet structure emerging from which dim-pairs have nonzero off-diagonal entries in a single N×N metric.

The reframe:

- **N compact dimensions** in one Ma domain (not three sheets each with two dims), with N = 6 as the working assumption.
- **Mostly diagonal N×N metric**, with a small number of non-zero off-diagonals (cross-terms).
- **Cross-term type determines particle class** at each dim-pair: three cross-terms carry τ = 1/3 twists (host the three quark generations via the clover-quarks mechanism); some carry shears (host charged leptons); the rest are zero (the dim-pair is orthogonal, no mode forms).
- **Sheets are emergent classifications** of dim-pairs by their cross-term type, not fundamental partitions.

## Inputs and guides

The project takes the following from [sheet-proton](../sheet-proton/) as a working input:

- **The clover-quarks 1/3-twist mechanism.** A 3-lobed cross-section with τ = 1/3 boundary identification gives Q_lobe = +2/3 (up quark) and Q_saddle = −1/3 (down quark) from per-arc geodesic curvature integration; baryon path-windings, Z₃ confinement, and proton/neutron structure all follow. See [sheet-proton clover-quarks.md](../sheet-proton/work/clover-quarks.md). Adopted as the project's quark-sector working mechanism.

The following are treated as **guides, not hard givens** — useful precedents whose mechanisms we may rederive from scratch as the architecture matures:

- **The R53 / model-F in-sheet shear-resonance.** Three charged-lepton masses fit at an extreme (ε, s) point via shear cancellation of the dominant kinetic term. See [R53-three-generations](../../studies/R53-three-generations) and [model-F.md](../../models/model-F.md). Useful for orientation on the e-sector mass scales; the project derives shears from scratch where the architecture allows it rather than inheriting model-F's specific (ε, s) values.

The project's job is to fit the fermion spectrum into the unified N-dim domain architecture using its own per-pair structure, with earlier models as orientation rather than hard constraints.

## Approach

See [work/STATUS.md](work/STATUS.md) for the phased work plan. Briefly:

1. **Phase 0** — naming convention for the Ma dims (reconciling with existing study notation where possible).
2. **Phase 1 (quark sector)** — pin the dims that host the quark structure; find the range of dim scales that works for all 3 quark generations.
3. **Phase 2 (electron sector)** — pin the e-dims; solve for the charged-lepton modes; decide whether electrons need clover-style internal structure and/or a twist of their own.
4. **Phase 3 (neutrino sector)** — find the best fit to match known neutrino behavior. May need to extend the dim count if necessary.
5. **Phase 4** — if preliminary results cohere across all three sectors, promote from exploratory `work/` files to a mathematical derivation in `ma-domain/` proper.

## Working assumptions

- The lowest modes that satisfy closure conditions (see [metric-charge](../metric-charge/)) are the observable particles.
- Higher unobserved modes are energy-unfavored and reduce to simpler degeneracies — dark modes, spatially separated states (cf. R56), or composite resonances.
- N = 6 total dims is the current working size; expansion to 7+ or contraction to 5 is allowed if the structural rules demand it.
- Pair notation: a dim-pair is written `Ma(i, j)` with `i < j` (size-ordered: `m_i` smaller than `m_j` per [work/architecture.md §1](work/architecture.md)). A set of pairs is written `Ma((i,j), (k,l), …)`.

## Relation to other projects

- [sheet-proton](../sheet-proton/) — on hold while this reframe is explored. Provides the inherited clover-quarks mechanism.
- [metric-binding](../metric-binding/), [metric-mass](../metric-mass/), [metric-charge](../metric-charge/) — foundational MaSt frameworks; this project extends the metric-binding architecture to a multi-dim compact domain.
- [studies/R53-three-generations](../../studies/R53-three-generations), [studies/R60-metric-11](../../studies/R60-metric-11) — empirical precedents that orient this project's reformulation; not hard constraints.
