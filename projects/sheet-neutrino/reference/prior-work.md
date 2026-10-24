# Prior work on the neutrino in Forma

Existing studies and projects that bear on the neutrino host, with what each contributes. Paths are relative to this file.

## Studies

| Study | Contribution |
|---|---|
| [R23 neutrino-beating](../../../studies/R23-neutrino-beating/README.md) | The neutrino cannot be a mode of the electron sheet: the lightest uncharged mode there is (0, ±1) at ~245 keV, about five orders of magnitude too heavy. This motivates a separate host. |
| [R25 neutrino-spin](../../../studies/R25-neutrino-spin/README.md) | The spin gate. In the WvM model, spin ½ comes from photon helicity projected along a (1, 2) path, the 1:2 winding ratio giving the factor ½. Modes without that structure fail the gate. |
| [R26 neutrino-t4](../../../studies/R26-neutrino-t4/README.md) | Each stable particle type on its own sheet at its Compton scale; the neutrino sheet at ~μm (θ₃, θ₄ of the six material dimensions). |
| [R48 helicity-charge](../../../studies/R48-helicity-charge/findings.md) | F1: the n₁ = ±1 charge selection rule derived from circular-polarization synchronization. F5: charge = net circulation = topological winding; **standing waves carry zero charge**. F6: under this rule a (3, 6) mode carries no charge directly. |
| [R49 neutrino-filter](../../../studies/R49-neutrino-filter/findings.md) | Family A: the three mass states as the three lowest spin-½ modes of an unfiltered torus at ε_ν = 5, s_ν = 0.022, matching Δm²₃₁/Δm²₂₁ = 33.6. Σm = 117.8 meV. Notes ±n_ring modes are charge conjugates (Majorana). |
| [R61 neutrino-tuning](../../../studies/R61-neutrino-tuning/findings.md) | A "zoo" of many triplets reproducing 33.6; charge-neutrality scoring using Majorana pairing and the R48 rule. Open: the Majorana charge-cancellation proof (pool item d) and the selection rule for the three observed modes (question 3). |

## Projects

| Project | Contribution |
|---|---|
| [metric-charge](../../metric-charge/README.md) | Charge as topological winding. Three structurally distinct ways to be massive but neutral (README item 6): single-axis modes, chirality-non-degenerate knots, sign-conjugate cancellation pairs. G1 (Ch 11 §6): local charge density ∝ geodesic curvature on a bent sheet. |
| [sheet-proton](../../sheet-proton/README.md) | The modulated-clover proton sheet. Neutron neutrality comes from cross-section modulation around the ring, which illustrates neutrality by cancellation (excluded for the neutrino; see [experimental-constraints §3](experimental-constraints.md#3-neutrality-limits-on-charge-and-charge-distribution)). |
| [grid-duality ch. 7](../../grid-duality/07-wrap-promotion-modeling.md) | The promotion ladder. Wrap 1 (close a line: light) is intrinsic periodicity with no ambient space; wrap 2 (bound a 1D loop in 2D: mass) is where an ambient direction enters. A 1D neutrino host would sit unusually low on this ladder for a massive particle, which needs examining. |
| [ma-domain](../../ma-domain/) | The multi-sheet architecture in which the neutrino sheet is one domain. |
| [ma-domain/work/config-neutrino.md](../../ma-domain/work/config-neutrino.md) | Catalog of neutrino host configurations: 2D sheet (NS), **1D curve (NC)**, and others. NC: Q = 0 because a 1D dimension has no slot for a charge label; ν₁/ν₂ split by a Wilson-loop flux f; mode-occupancy fork between normal ordering (modes −1, +1, −2; f ≈ 0.022) and inverted ordering (modes 0, −1, +1; f ≈ 0.0075). Its 1.5% fit (f ≈ 0.051) used working mass targets (30, 33, 60 meV) whose splitting ratio is ≈ 14, not the measured 33.6; its scope note says so. |
| [ma-domain/work/neutrino-1D.md](../../ma-domain/work/neutrino-1D.md) | Full development of the 1D curve: band structure on a C₃-shaped loop, the doublet split, and **tribimaximal mixing** (θ₁₂ ≈ 35.3°, θ₂₃ = 45°, θ₁₃ = 0) as the natural C₃-symmetric limit, with θ₁₃ and the CP phase expected from symmetry breaking. PMNS not yet computed. §5 gives the "tiny-tube" reading (2D sheet, effectively 1D); §6.4 attaches the loop to the three electron-delta corners. |
| [ma-domain/work/cand-QY-ED.md](../../ma-domain/work/cand-QY-ED.md) | ma-domain's adopted quark + charged-lepton architecture (quark wye + electron delta; the K4 share-3 member). Fits the 9 charged-fermion masses; leaves the neutrino sector open (§6). |
| [ma-domain/work/mode-stability.md](../../ma-domain/work/mode-stability.md), [conservation-as-momentum.md](../../ma-domain/work/conservation-as-momentum.md) | Leakage through shared dimensions as the decay mechanism (weak channels via the neutrino line); conservation laws as geometric momenta, with lepton number listed as open. |
| [grid-primitive ch. 9](../../grid-primitive/09-chirality-asymmetry.md) | **Substrate antisymmetric chirality χ_anti**: a small direction-asymmetry in the grid primitive is mathematically a constant background gauge field. It is undetectable in open space (pure gauge) but produces a gauge-invariant Wilson-loop phase around every compact loop. Proposed (speculatively, §8) as a source of matter/antimatter asymmetry and anomalous moments. |
| [metric-charge ch. 6 §6.7](../../metric-charge/06-handedness-and-pairs.md) | Sheet shear σ_uw splits chirality partners (m, n) ↔ (m, −n) but **cannot** split matter/antimatter partners (m, n) ↔ (−m, −n). Matter/antimatter bias is left open, with substrate-level chirality named as a candidate source. |
| [metric-mass ch. 7](../../metric-mass/07-shear-and-bias.md) | Shear between space and a compact direction breaks ±n degeneracy only for moving particles; at rest ±n stay equal. |

## Known inconsistencies to resolve

1. **Mode-label order.** R61 writes the mass formula as µ²(n_r, n_t) = (n_r·ε)² + (n_t − n_r·s)² (F1), but the summary legend labels triplets as (n_tube, n_ring) and defines L_tube = ε·L_ring. These disagree about which index multiplies ε. Taken literally, F1 also does not reproduce R49's published absolute masses (it gives Σm ≈ 456 meV at ε = 5, against R49's 117.8). The splitting ratio is unaffected, because ε cancels in mass differences.
2. **R48 rule as used in R61.** R61 Track 4 treats |n_tube| ≥ 2 modes as "inherently uncharged (R48)." R48 F6 shows that the same rule leaves a (3, 6) proton uncharged and says proton charge must then come from another mechanism. Whether the rule applies uniformly across sheets needs checking against sheet-proton's charge mechanism.
3. **Cosmological bound.** R49 compares Family A's Σm = 117.8 meV with a bound of ~120 meV. Recent analyses within the standard cosmological model put the bound near 70 meV ([experimental-constraints §4](experimental-constraints.md#4-masses)). This is model-dependent but should be noted.
