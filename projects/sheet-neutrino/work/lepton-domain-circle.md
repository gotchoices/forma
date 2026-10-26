# Lepton-domain circle (host G)

Working file, **draft for review**. Host G in [host-candidates.md](host-candidates.md). Script: [../scripts/lepton_circle.py](../scripts/lepton_circle.py).

**Terms.** The *leptons* are six particles: the three **charged leptons**, the electron (e), muon (μ), and tau (τ), each with charge −1, and their three neutral **neutrinos**. In [ma-domain](../../ma-domain/README.md), each charged lepton has its own sheet (the three "electron sheets"). A neutrino's **flavor** (ν_e, ν_μ, ν_τ) names the charged lepton it is created or detected with. Its **mass states** (ν₁, ν₂, ν₃) are the states of definite frequency. Each flavor is a mixture of mass states, and oscillation is the beat between their frequencies.

## 1. The idea

1. **Setting.** In ma-domain a particle sheet is a pair of compact dimensions, and sheets sharing a dimension are linked. The neutrino was left as a 1D loop attached to the three electron sheets in an unspecified way ([neutrino-1D.md §6.4](../../ma-domain/work/neutrino-1D.md)).
2. **A neutrino segment is a ribbon:** one large dimension (micrometers) paired with one small dimension **shared with an electron sheet** (picometers). The sharing ties each neutrino segment to one charged lepton, forming a **lepton domain**.
3. **The segment is Klein-glued.** Going along the large dimension flips the small one. The small dimension's role is to provide the degree of freedom in which a half-integer (sign-flipping) closure can exist.
4. **Light prefers the large dimension.** Exciting the small dimension costs energy on the electron scale, about 10⁷ times the neutrino's. Below that threshold only motion along the large dimension is available, as in a waveguide below cutoff, where only the fundamental mode propagates.
5. **Three segments, one circle.** One segment per charged lepton; joined end to end they form a single large compact circle, and the neutrino is a standing wave on the whole circle.

## 2. Assumptions

| ID | Assumption |
|---|---|
| G1 | **The flip belongs to the neutrino sheet.** It is a relationship between the neutrino line and the small dimension, and it does not act on the electron sheet that shares the small dimension. |
| G2 | **Flavor = segment; mass state = whole-circle mode.** A neutrino is created and detected on the segment attached to its charged lepton. That packet is a mixture of whole-circle modes, whose frequencies beat in flight (oscillation). |
| G3 | **The large-dimension mode is preferred.** Energy enough to excite the small dimension may instead form an electron, on the small dimension and its companion dimension in that electron sheet. To be shown. |
| G4 | **Compton size is not a gravitational size.** Compton size is a wavelength, shrinking as energy grows (λ = h/mc); gravitational size is a mass concept. The neutrino line's length is set by its Compton wavelength (≈ 25–35 μm, §4). Short-range gravity tests constrain it only if gravity propagates into the line, which is open. |

## 3. Consequences

- **Neutrality.** The fundamental mode travels only along the large dimension, with no circulation around the small one, so it carries no charge.
- **Spin-½-like closure.** Each segment flips the sign once, and sign flips multiply: (−1)³ = −1 per circuit. The circle closes with one net sign flip, not with spin 3/2.
- **Majorana-like.** As on any 1D ring, the two circulation directions are indistinguishable, and a standing wave goes both ways at once ([neutrino-1D.md §3.3](../../ma-domain/work/neutrino-1D.md)).
- **The near-degenerate pair.** The masses are modes of the whole circle, not of individual segments. With segment lengths l₁, l₂, l₃ nearly equal, the circle's 3-fold symmetry keeps the two lowest modes nearly degenerate. The measured small split then needs the lengths to differ by a few percent (§4).
- **Mixing.** With equal segments, the 3-fold symmetry gives tribimaximal mixing ([neutrino-1D.md §6](../../ma-domain/work/neutrino-1D.md)). Unequal segments modify it. Not computed.

## 4. Spectrum model

**Model:** a closed loop of three segments joined by three partially reflecting junctions of strength g, a stand-in for the coupling to the electron sheets, closing with one net sign flip. Mass ∝ wavenumber k. In these units a plain loop has k = ½, ½, 3/2, 3/2, …

**Equal segments.** The lowest pair stays exactly degenerate for any g, and the next level splits into a state at exactly k = 3/2 and one above it:

| g | Lowest modes k |
|---|---|
| 0 | 0.50, 0.50, 1.50, 1.50 |
| 1.0 | 0.806, 0.806, 1.500, 1.764 |
| 4.0 | 1.135, 1.135, 1.500, 2.204 |

**Unequal segments.** For a one-parameter scan the lengths were taken as (1 − d, 1, 1 + d) × L/3. This is a convenience; in general l₁, l₂, l₃ are independent. Fitting Δm²₃₁/Δm²₂₁ = 33.6 with ν₃ the k = 3/2 state:

| g | d | Masses (meV) | Σm (meV) | m₃/m₁ |
|---|---|---|---|---|
| 0.5 | 0.167 | 24.6, 26.1, 56.0 | 107 | 2.28 |
| 1.0 | 0.075 | 31.1, 32.2, 59.1 | 122 | 1.90 |
| 2.0 | 0.033 | 41.4, 42.3, 65.1 | 149 | 1.57 |
| 4.0 | 0.014 | 57.3, 58.0, 76.3 | 192 | 1.33 |

The ratio is reachable at any junction strength. Circle length ≈ 25–35 μm. A fourth state lies just above ν₃. This is a fit (two parameters, one ratio).

## 5. New relative to ma-domain

ma-domain has the effectively-1D "tiny-tube" reading of a 2D sheet ([neutrino-1D.md §5](../../ma-domain/work/neutrino-1D.md)) and the three-corner attachment (§6.4). New here: the connection is a sheet that shares an electron dimension; Klein gluing as the source of the half-integer closure; and one segment per charged lepton.

## 6. Open questions

1. **G1 in ma-domain's terms.** ma-domain computes masses from one metric over all its dimensions. Does a flip that belongs to one pair of dimensions sit consistently in that description?
2. **How the flip reaches the fundamental mode.** That mode is uniform across the small dimension, which a flip by itself leaves unchanged, so the flip must act on some internal orientation of the wave. Polarization is the natural candidate.
3. **Where flavor coupling happens.** The k = 3/2 state has nodes at the junctions. If coupling happens at the junctions, it couples to no flavor and ν₃ must be another state. If coupling happens along the segments, it couples normally.
4. **What sets l₁, l₂, l₃,** and what the junction is.
5. **G3:** does small-dimension energy form an electron?
6. **Lepton number:** whether it emerges as a conserved momentum of the lepton domain, given the Majorana-like modes ([conservation-as-momentum.md](../../ma-domain/work/conservation-as-momentum.md)).
7. **Spin relative to space,** shared with every candidate ([mechanisms §4](mechanisms.md#4-spin-½)).
