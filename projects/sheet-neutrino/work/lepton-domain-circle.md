# Lepton-domain circle (host G)

Working file, **draft for review**. Host G in [host-candidates.md](host-candidates.md). The neutrino lives on a grand circle made of three segments, one per charged lepton. Each segment is a Klein-glued sheet built from a large neutrino dimension and a small dimension shared with that lepton's electron sheet. The construction builds on [ma-domain](../../ma-domain/README.md)'s architecture and supplies the neutrino–electron connection that ma-domain leaves open.

Script: [../scripts/lepton_circle.py](../scripts/lepton_circle.py).

## 1. The idea, step by step

1. **ma-domain's setting.** The material space has N compact dimensions. A particle sheet is a pair of dimensions; sheets that share a dimension are linked. This arrangement hosts the quarks and charged leptons well ([cand-QY-ED.md](../../ma-domain/work/cand-QY-ED.md)). The neutrino was left as a 1D loop attached to the three electron sheets in an unspecified way ([neutrino-1D.md §6.4](../../ma-domain/work/neutrino-1D.md)).
2. **A neutrino segment is a 2D sheet**, made of one large dimension (the neutrino line, micrometers long) and one small dimension **shared with an electron sheet** (picometer scale). The sharing ties the neutrino structurally to its charged lepton, forming a **lepton domain**.
3. **The segment is Klein-glued.** Going once along the large direction reflects the small one.
4. **Light travels only along the large direction.** A mode with momentum in the small dimension would be electron-scale heavy. The small dimension's only job is the flip.
5. **Three segments, one circle.** Each charged lepton (e, μ, τ) has its own segment. Joined end to end, the three form one large compact circle, and the neutrino is a standing wave on the whole circle.

## 2. Structural commitments

| ID | Commitment | Why it is needed |
|---|---|---|
| G1 | **Sheets are glued along shared circles**, not multiplied into one big product space. The neutrino segment has a y-circle attached at each point of its line; the electron sheet touches only one of those y-circles, at the junction. | In a product space the reflection of y would act on every field, including the electron sheet's modes, forcing them into standing waves (neutral, or mixing partners that shear splits). In the glued reading the flip is a relation *between* the two dimensions of the neutrino sheet and the electron sheet stays an ordinary torus. |
| G2 | **The flip acts on the wave's polarization.** A wave uniform across the small dimension does not notice y → −y. But MaSt particles are light, and the polarization component along the small dimension reverses. A mode polarized that way returns **inverted** after traversing a segment, at no cost in small-dimension momentum. | Supplies the spin-½-like sign flip while keeping the mode light. |
| G3 | **Mass states are modes of the whole circle; flavor states are packets on one segment.** A neutrino is created and detected on the segment attached to its charged lepton (ν_e, ν_μ, ν_τ). That packet is a fixed mixture of whole-circle modes (ν₁, ν₂, ν₃). In flight the mass components drift in phase and eventually separate, which is oscillation. | Without coupling between segments, flavor would equal mass and nothing would oscillate. |
| G4 | **Energy in the small dimension is an electron.** A mode with momentum along the shared dimension does not stay on the neutrino sheet, where the flip would force it into a neutral standing wave. At the junction it continues into the electron sheet, where it can circulate and carry charge. Such junction states split into an electron plus a neutrino, as in beta decay. Electron and neutrino masses differ by about 2×10⁷ (0.511 MeV vs ~0.03 eV), so a mode strongly prefers to be one or the other. | Disposes of the would-be tower of heavy neutral states on the neutrino sheet. |
| G5 | **Compton size ≠ gravitational size.** The neutrino line's *Compton size* is set by the mode's mass (≈ 25–35 μm total, §4). Its *gravitational size* is how far a static gravitational field spreads into it. Only the latter is constrained by short-range gravity tests (inverse-square law verified down to ~50 μm). | Keeps the gravity bound from being applied by assumption. |

## 3. What follows from the commitments

- **Neutrality.** The light mode has no momentum along the small dimension, so it has no charge winding (ma-domain's "no slot for charge," [mechanisms N1](mechanisms.md#1-neutrality)). Any small-dimension excitation on the Klein sheet is a standing wave (N2) and leaves for the electron sheet (G4).
- **Spin-½-like, not 3/2.** Each segment flips the sign once, and sign flips multiply: three segments give (−1)³ = −1 per grand circuit. The circle closes **antiperiodically**, the same signature as one flip. As for every candidate, the link between an internal sign flip and a 360° rotation in ordinary space is still open.
- **A protected pair plus a separated state.** With three identical segments, the circle's 3-fold symmetry keeps the lowest two modes **exactly degenerate**. The next level splits into a state at exactly k = 3/2 (nodes at all three junctions, so the junctions do not affect it) plus a state above it. The near-degenerate pair the data require comes **free from symmetry**.
- **The small split from generation differences.** The three segments attach to different charged leptons, so they need not be identical. A few percent difference in segment length splits the pair slightly. This replaces the grid-bias phase as the source of the ν₁/ν₂ split.
- **Mixing.** Flavor = segment, mass = whole-circle mode. With equal segments, 3-fold symmetry gives tribimaximal mixing (θ₁₂ ≈ 35.3°, θ₂₃ = 45°, θ₁₃ = 0; [neutrino-1D.md §6](../../ma-domain/work/neutrino-1D.md)). The segment asymmetry that splits the pair should also move θ₁₃ off zero. Not computed.
- **Majorana-like.** The Klein flip makes modes their own conjugates, as on the Klein bottle (host D). This bears on lepton number (§6).
- **Relation to other hosts.** Dynamically this is the near-antiperiodic 1D ring (host B), but its half-twist now has a geometric source (the flip) and its pair-splitting a structural one (generation asymmetry). Structurally it is ma-domain's NC curve plus Klein flips plus a concrete connection to the electron sheets.

## 4. Spectrum model and results

**Model:** a closed loop of three segments with lengths (1 − d, 1, 1 + d) × L/3, joined by three partially reflecting junctions of strength g, a stand-in for the coupling to the electron sheets. Antiperiodic closure. Mass ∝ wavenumber k (units: a plain antiperiodic loop has k = ½, ½, 3/2, 3/2, …).

**Equal segments (d = 0):**

| g | Lowest modes k |
|---|---|
| 0 | 0.50, 0.50, 1.50, 1.50 |
| 0.5 | 0.684, 0.684, 1.500, 1.644 |
| 1.0 | 0.806, 0.806, 1.500, 1.764 |
| 2.0 | 0.964, 0.964, 1.500, 1.952 |
| 4.0 | 1.135, 1.135, 1.500, 2.204 |

**Fitting the measured ratio (Δm²₃₁/Δm²₂₁ = 33.6),** taking ν₁, ν₂ as the split pair and ν₃ as the k = 3/2 state:

| g | Asymmetry d | Masses (meV) | Σm (meV) | m₃/m₁ | 4th state (meV) |
|---|---|---|---|---|---|
| 0.5 | 0.167 | 24.6, 26.1, 56.0 | 107 | 2.28 | 60.6 |
| 1.0 | 0.075 | 31.1, 32.2, 59.1 | 122 | 1.90 | 69.2 |
| 2.0 | 0.033 | 41.4, 42.3, 65.1 | 149 | 1.57 | 84.6 |
| 4.0 | 0.014 | 57.3, 58.0, 76.3 | 192 | 1.33 | 112.0 |

**Reading:**
- The ratio is reachable for any junction strength, with segment asymmetries from about 1% to 17%. Stronger junctions need less asymmetry.
- m₃/m₁ is not fixed at 2; it runs from about 2.3 to 1.3 as g grows, passing 2 near g ≈ 0.8.
- Total circle length is L = k·hc/m ≈ 25–35 μm, about 8–12 μm per segment.
- A fourth state sits just above ν₃ and must be sterile.
- **ν₃ coupling caveat:** the k = 3/2 state has nodes at the junctions. If flavor coupling happens *at* the junctions, this state couples to no flavor and would be sterile, so ν₃ would have to be the fourth state, changing the fit. If coupling happens *along* each segment (through the shared dimension along its whole length), the k = 3/2 state couples normally. This depends on G3's coupling model.

Two parameters (g, d) fit one ratio. As in ma-domain, this is a fit, not a prediction.

## 5. What is new relative to ma-domain

ma-domain already has:
- the "tiny-tube" reading, a neutrino on a 2D sheet whose small dimension is never excited, making it effectively 1D ([neutrino-1D.md §5](../../ma-domain/work/neutrino-1D.md)), but on the *same* sheet as the charged lepton and with no spin mechanism;
- the three-corner attachment with tribimaximal mixing (§6.4), with the form of the connection left open.

New here:
1. **The connection is a sheet:** each neutrino segment pairs the neutrino line with a shared electron dimension. That makes it an ordinary edge in ma-domain's dimension graph.
2. **Klein gluing,** used nowhere else in Forma before this project.
3. **Spin-½-like closure from the polarization flip,** in a light mode.
4. **One segment per flavor:** the pair-plus-singlet structure comes from the circle's symmetry, and the small split from differences between the generations.

## 6. Open questions and possible points of disagreement

1. **Glued sheets vs. product space (G1).** ma-domain draws dimensions as a graph but computes masses from one metric over all dimensions, which is product-space language. This candidate requires the glued reading. Can ma-domain's quark and charged-lepton fits be restated in it?
2. **Where flavor coupling happens (G3).** At the junctions or along the segments. This decides whether the k = 3/2 state is ν₃ or sterile (§4).
3. **What the junction is.** g stands in for a junction that has not been modeled: the geometry where a neutrino segment meets an electron sheet.
4. **Junction states (G4).** Do states with small-dimension energy leak promptly into electron plus neutrino? ma-domain's leakage machinery ([mode-stability.md](../../ma-domain/work/mode-stability.md), [leakage-rate.md](../../ma-domain/work/leakage-rate.md)) is the tool.
5. **Gravitational size (G5).** Does a static gravitational field spread into the neutrino line? grid-gravity's mechanism 3 describes gravity as "the steady part of the one field that carries light and matter," which, read literally, would let it spread wherever light goes. Open for grid-gravity.
6. **Lepton number.** The hope is that lepton number conservation falls out as momentum conservation in the lepton domain. ma-domain lists it as open, with a cycle-space invariant as candidate ([conservation-as-momentum.md](../../ma-domain/work/conservation-as-momentum.md)). The Klein flip makes the neutrino Majorana-like, which permits neutrinoless double-beta decay (lepton number changing by 2). So conservation can be at most approximate, unless the construction forbids that process, which would make it Dirac-like and testable either way. Lepton *flavor* is not conserved in any case (oscillation).
7. **Segment asymmetry.** Is there a reason the segments differ by the fitted amount, for example a dependence on the attached electron sheet's size? The charged-lepton mass ratios (1 : 207 : 3477) are far larger than the few-percent asymmetries needed, so any link must be weak or indirect.
8. **Spin relative to space.** Shared with every candidate ([mechanisms §4](mechanisms.md#4-spin-½)).
