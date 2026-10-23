# sheet-neutrino

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** How the neutrino might be hosted in the MaSt framework: on what kind of compact structure, with what mode content, and by what mechanism it is massive, electrically neutral, spin-½, and oscillating. The neutrino counterpart to [sheet-proton](../sheet-proton/).
**Status:** Framed (2026-10-23). No host geometry is committed.

## The question

> *What compact structure can host a particle that is massive but extremely light, carries no detectable charge or charge distribution, carries half-integer angular momentum, and comes in three mass states whose interference produces oscillation?*

The electron and proton each live on a 2D compact sheet in MaSt. The neutrino has been treated the same way (a third sheet at micrometer scale; see [R26](../../studies/R26-neutrino-t4/README.md), [R49](../../studies/R49-neutrino-filter/findings.md), [R61](../../studies/R61-neutrino-tuning/findings.md)). That work fits the observed mass splittings, but it leaves the neutrality and spin mechanisms only partly derived. This project steps back and asks which kinds of host are viable at all.

## Ground rules

1. **The host is open.** A 1D compact line, a 2D torus, a Klein bottle, and other options are all live candidates. None is assumed.
2. **External behavior is fixed by data; internal mechanism is not.** The neutrino must *behave* as spin-½ when viewed from ordinary space: it carries away half-integer angular momentum, has the spin-½ rotation behavior, and obeys Fermi statistics. *How* a host stores that angular momentum internally may look nothing like spin-½ on a 2D sheet. See [reference/experimental-constraints.md §2](reference/experimental-constraints.md#2-spin-what-is-measured-and-what-is-inferred).
3. **Intrinsic before extrinsic.** Properties that something living on the host can measure are preferred over properties that depend on how the host is drawn in a larger space. An extrinsic feature counts only if something physically couples to it. See [reference/geometry-background.md](reference/geometry-background.md).
4. **Fits are not predictions.** A host that reproduces one ratio with one tuned parameter has fit it. Predictions are what it says about quantities it was not tuned to: absolute masses, the sum Σm, mixing angles, and whether the neutrino is Majorana.
5. **Negative results are recorded as "not yet."** A blocked host is recorded with the specific form that failed, and stays open to revival.

## Reference files

Background distilled from the discussion that framed this project:

| File | Contents |
|---|---|
| [reference/experimental-constraints.md](reference/experimental-constraints.md) | What is measured about neutrinos and how firmly: spin, charge radius, magnetic moment, masses, mixing, Majorana status |
| [reference/geometry-background.md](reference/geometry-background.md) | Embedding vs. intrinsic geometry, how periodicity is perceived from inside, curvature and turning number, the Klein bottle, antiperiodic closure |
| [reference/prior-work.md](reference/prior-work.md) | Map of existing neutrino-related studies and projects, plus known inconsistencies to resolve |

## Work files

| File | Contents |
|---|---|
| [work/host-candidates.md](work/host-candidates.md) | The candidate hosts side by side, with spectrum checks |
| [scripts/spectra.py](scripts/spectra.py) | Splitting ratio and absolute masses for ring, torus, and Klein-bottle hosts |

## Phases

**Phase 1: constraints.** Settle what any host must do, stated without reference to a host: the external spin-½ requirements, the neutrality bounds, and the spectrum pattern (a near-degenerate pair plus a distant third state).

**Phase 2: candidate hosts.** For each candidate, work out its mode spectrum, its neutrality mechanism, and its route to half-integer angular momentum. Record where each one succeeds and where it is blocked.

**Pool (later, order open):**
- Angular-momentum hand-off: how a neutrino host receives and releases angular momentum when it couples to the electron and proton sheets in beta decay
- Mixing angles: whether any host predicts the three observed mixing angles
- Majorana or Dirac: what each host predicts, and the link to neutrinoless double-beta decay
- Selection: why three modes are "loud" and the rest sterile (R61's open question 3)
- Absolute mass scale and the cosmological bound on Σm

## What success looks like

A clear mental model of what the neutrino requires of its host, and an honest ranking of the candidate hosts against those requirements. Finding that one host is clearly preferred would be a bonus, not the goal.

## Related material

- [sheet-proton](../sheet-proton/): the proton-sheet counterpart
- [metric-charge](../metric-charge/README.md): charge as winding, and three mechanisms for mass without charge
- [grid-duality ch. 7](../grid-duality/07-wrap-promotion-modeling.md): the promotion ladder, where closing a line (wrap 1) and bounding a loop in 2D (wrap 2) are separate steps
- [primers/bloch-band-structure.md](../../primers/bloch-band-structure.md): modes on periodic lattices
