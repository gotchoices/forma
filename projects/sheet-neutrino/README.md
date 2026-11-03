# sheet-neutrino

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** How the neutrino might be hosted in the MaSt framework: on what kind of compact structure, with what mode content, and by what mechanism it is massive, electrically neutral, spin-½, and oscillating. The neutrino counterpart to [sheet-proton](../sheet-proton/).
**Status:** Paused as an open question (2026-11-03). No host geometry is committed; see [Where things stand](#where-things-stand).

## The question

> *What compact structure can host a particle that is massive but extremely light, carries no detectable charge or charge distribution, carries half-integer angular momentum, and comes in three mass states whose interference produces oscillation?*

The electron and proton each live on a 2D compact sheet in MaSt. The neutrino has been treated the same way (a third sheet at micrometer scale; see [R26](../../studies/R26-neutrino-t4/README.md), [R49](../../studies/R49-neutrino-filter/findings.md), [R61](../../studies/R61-neutrino-tuning/findings.md)). That work fits the observed mass splittings, but it leaves the neutrality and spin mechanisms only partly derived. This project steps back and asks which kinds of host are viable at all.

## Where things stand

*Paused 2026-11-03, open to revival.* The task index is [STATUS.md](STATUS.md); details are in the work files below.

**Established, independent of any host:**
- **Requirements from measurement** ([chapter 1](01-host-requirements.md)): half-integer angular momentum carried away; spin-½ behavior relative to space; no charge density anywhere; the two squared-mass splittings (ratio ≈ 33.6) with the lightest mass free; three neutrinos that couple to the Z.
- **The solution set:** all allowed masses lie on one curve fixed by the lightest mass, or equivalently by ν₃/ν₁ ([host-candidates §5a](work/host-candidates.md)).
- **Structural predictions shared by every working host:** normal ordering; CP-conserving oscillation unless something direction-dependent acts; a neutrino magnetic moment of essentially zero.

**The main lesson.** A flat compact manifold cannot mix its modes, so it cannot produce oscillation by itself. Every host that fitted needed a coupling between flavors that was supplied rather than derived: junction strengths, a free ring size, or per-channel hub couplings. Oscillation must come from somewhere non-flat (shape or curvature) or from connections between sheets.

**The open question this leaves.** Glued sheets or one torus ([lepton-manifold.md](work/lepton-manifold.md)):
- read as separate sheets joined through shared circles, ma-domain's fits hold, but the flavor couplings must be supplied by the connections;
- read as one torus, the whole manifold could do the mixing, but ma-domain's sheet assignments do not survive, and the charge of modes circulating in three or more dimensions becomes central.

**Candidates explored** ([host-candidates.md](work/host-candidates.md), [mechanisms.md](work/mechanisms.md)):

| Host | Outcome |
|---|---|
| 1D twisted ring; 2D torus (Family A) | fit the splittings with one small parameter; Family A's ν₃ = second harmonic of ν₁ |
| Klein bottle (flat, flipped, tracks) | neutral by topology; fits with a ring phase or a tilted figure-8; extra tracks to explain |
| Lepton-domain neutrino circle (host G) | free junctions fit masses and mixing exactly (under-determined); GRID necks fit with Klein flips; plain width steps fit without them |
| On ma-domain's K4 dimensions | fails: no light neutral mode on a K4 dimension, and K4's size ratios give no usable junctions |
| Charged wye + neutrino circle | near-fit, but a look-elsewhere check shows it is not significant |
| Half-twisted neutrino sheets | exact splittings, but charged states at m_μ/2 and other half-integer multiples |
| Quark hub as flavor coupler | symmetric coupling fails; per-channel couplings fit (under-determined: e weak, μ and τ strong and opposite in sign) |

**Most promising places to resume** ([STATUS.md](STATUS.md), open-directions index):
- **A massless or very light ν₁** (0, 8.7, 50 meV): the one allowed region not yet tested, and the only family under the cosmology figure.
- **Deriving flavor couplings from geometry,** for example through the clover's lobes and saddles or the tube/ring roles at the hub and in the electron triangle, so that a host becomes predictive.
- **The glued-sheets vs. single-torus choice,** possibly through a full single-torus lepton search.
- **Spin ½ relative to ordinary space,** which no candidate has addressed and which likely needs a new idea.

## Ground rules

1. **The host is open.** A 1D compact line, a 2D torus, a Klein bottle, and other options are all live candidates. None is assumed.
2. **External behavior is fixed by data; internal mechanism is not.** The neutrino must *behave* as spin-½ when viewed from ordinary space: it carries away half-integer angular momentum, has the spin-½ rotation behavior, and obeys Fermi statistics. *How* a host stores that angular momentum internally may look nothing like spin-½ on a 2D sheet. See [reference/experimental-constraints.md §2](reference/experimental-constraints.md#2-spin-what-is-measured-and-what-is-inferred).
3. **Intrinsic before extrinsic.** Properties that something living on the host can measure are preferred over properties that depend on how the host is drawn in a larger space. An extrinsic feature counts only if something physically couples to it. See [reference/geometry-background.md](reference/geometry-background.md).
4. **Data, not prior fits, is the target.** Hosts must agree with measurements: the mass splittings, the absolute mass bounds, the count of light states, and the neutrality limits. Earlier solutions such as R49's Family A are one candidate each, not constraints.
5. **Fits are not predictions.** A host that reproduces one ratio with one tuned parameter has fit it. Predictions are what it says about quantities it was not tuned to: absolute masses, the sum Σm, mixing angles, and whether the neutrino is Majorana.
6. **Negative results are recorded as "not yet."** A blocked host is recorded with the specific form that failed, and stays open to revival.

**Task queue:** [STATUS.md](STATUS.md).

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
| [work/host-candidates.md](work/host-candidates.md) | The candidate hosts side by side (1D rings, torus, Klein bottle variants, lobed Klein), with spectrum checks |
| [work/klein-tracks.md](work/klein-tracks.md) | ν₁, ν₂, ν₃ as closed tracks on a modulated Klein tube (the sheet-proton mechanism transplanted): geometry, structural results, fits |
| [work/lepton-domain-circle.md](work/lepton-domain-circle.md) | Host G (draft): a grand neutrino circle of three Klein-glued segments, each sharing a small dimension with one charged lepton's sheet |
| [work/grid-circle.md](work/grid-circle.md) | Stage 1 GRID simulation of host G: exact modes and mixing of the circle as a GRID graph; the small-loop junction is too weak at physical scale |
| [work/junction-fit.md](work/junction-fit.md) | Host G, inverse design: what the three junctions must do to reproduce the masses and mixing, a construction to visualize, and a CP prediction |
| [work/lepton-manifold.md](work/lepton-manifold.md) | Can the leptons share one set of dimensions? K4 tests, spectrum-based torus searches, wye + circle, half-twisted sheets, the hub, the electron triangle, glued vs. single torus |
| [work/mechanisms.md](work/mechanisms.md) | Catalog of candidate mechanisms by role: neutrality, the small ν₁/ν₂ split, ν₃ structure, spin ½, matter/antimatter, mixing; plus predictions and tests |
| [scripts/spectra.py](scripts/spectra.py) | Splitting ratio and absolute masses for ring, torus, and Klein-bottle hosts; merged-ν₃, shaped-loop, and lobe-bias checks |
| [scripts/junction_fit.py](scripts/junction_fit.py) | Continuum three-segment circle with general junctions; fits the junctions to the mass ratio and mixing |
| [scripts/grid_circle.py](scripts/grid_circle.py) | GRID (Scattering-model) graph of the lepton-domain circle: exact mode frequencies, fit fractions, mixing |
| [scripts/lepton_circle.py](scripts/lepton_circle.py) | Modes of the three-segment lepton-domain circle; segment asymmetry needed for the measured ratio |
| [scripts/klein_tracks.py](scripts/klein_tracks.py) | Closed tracks and track-length masses on a modulated Klein tube; shape search for the measured ratio |
| [scripts/k4_widths.py](scripts/k4_widths.py), [scripts/triangle_circle.py](scripts/triangle_circle.py) | Neutrino circle with junctions from K4's dimension sizes; electron-triangle bookkeeping and junction rules |
| [scripts/lepton_search.py](scripts/lepton_search.py) | Spectrum-based search of flat tori for all six leptons (strict and loose identification rules) |
| [scripts/wye_theta13.py](scripts/wye_theta13.py), [scripts/wye_generic_check.py](scripts/wye_generic_check.py), [scripts/wye_lookelsewhere.py](scripts/wye_lookelsewhere.py) | Charged wye + neutrino circle: tube/ring sharing variants, genericity and look-elsewhere checks |
| [scripts/halftwist_check.py](scripts/halftwist_check.py) | Charged wye + half-twisted neutrino sheets on one large tube |
| [scripts/hub_coupling.py](scripts/hub_coupling.py) | Three flavor channels coupled through a common hub (star coupling) |
| [scripts/k5_census.py](scripts/k5_census.py) | Light modes of ma-domain's K5 read as a single 5-torus |

## Phases

**Phase 1: constraints.** Settle what any host must do, stated without reference to a host: the external spin-½ requirements, the neutrality bounds, and the spectrum pattern (a near-degenerate pair plus a distant third state).

**Phase 2: candidate hosts.** For each candidate, work out its mode spectrum, its neutrality mechanism, and its route to half-integer angular momentum. Record where each one succeeds and where it is blocked.

**Pool (later, order open):**
- Angular-momentum hand-off: how a neutrino host receives and releases angular momentum when it couples to the electron and proton sheets in beta decay
- Mixing angles: whether any host predicts the three observed mixing angles
- Majorana or Dirac: what each host predicts, and the link to neutrinoless double-beta decay
- Selection: why three modes are "loud" and the rest sterile (R61's open question 3)
- Absolute mass scale

## Chapter arc

Only the introductory chapters are fixed. Later chapters will be decided as the work develops.

1. [**What any host must do**](01-host-requirements.md): the requirements set by measurement, stated without reference to any particular host.
2. **The twisted ring**: modes on a closed loop, the effect of a twist in its closure, and how one small parameter produces the observed splitting pattern.
3. *Open.*

## What success looks like

A clear mental model of what the neutrino requires of its host, and an honest ranking of the candidate hosts against those requirements. Finding that one host is clearly preferred would be a bonus, not the goal.

## Related material

- [sheet-proton](../sheet-proton/): the proton-sheet counterpart
- [metric-charge](../metric-charge/README.md): charge as winding, and three mechanisms for mass without charge
- [grid-duality ch. 7](../grid-duality/07-wrap-promotion-modeling.md): the promotion ladder, where closing a line (wrap 1) and bounding a loop in 2D (wrap 2) are separate steps
- [primers/bloch-band-structure.md](../../primers/bloch-band-structure.md): modes on periodic lattices
