# STATUS — sheet-neutrino task queue

Living document. Queued and open tasks, highest priority first. Results go into the work files linked from the [README](README.md).

## 1. Lepton manifold: search for fits (priority)

Leptons might be hosted on **4 dimensions**: the 3 dimensions shared among the 3 2D electron sheets (the corners of ma-domain's K4 electron delta), plus a fourth neutrino line.

Or leptons might be hosted on **3 dimensions**, where neutrinos are the lightest (1, 0) mode, which produces mass but not charge.

We should search for fits in both possibilities.

**Results so far:** [work/lepton-manifold.md](work/lepton-manifold.md). In K4, 1b is blocked: at the neutrino scale m₁ is always the sheared direction of the e and μ sheets, so a single-axis mode on it is heavy. 1a is blocked for plain width steps by the delta's size ratios. Both are recorded as "not yet," with the specific obstruction.

### 1a. Four dimensions: delta corners + neutrino line

Neutrino segments pair the neutrino line with one dimension of each electron sheet; junction reflections come from width ∝ dimension size ([junction-fit.md](work/junction-fit.md), Test 3).

- [ ] Rerun [k4_widths.py](scripts/k4_widths.py) across **all four** of K4's discrete charge assignments (`ma-domain/outputs/cand_QY-ED-share3.txt`), not just the best one.
- [ ] Use K4's full continuous solution family (m₁, m₃ ranges) rather than a fixed m₃ ≈ 1 fm.
- [ ] Report whether any configuration fits the mass ratio and the CP-independent mixing entries. If none does, record the nearest misses and which size ratios block them.
- **Note (arithmetic, before any rerun):** with plain width steps (width ∝ size), the fits need two strong steps (ratios of tens to hundreds) and one of about 2. The delta corners offer only m₃/m₂ ≈ 136, m₁/m₃ ≥ 4,500, m₁/m₂ ≥ 6×10⁵, or 1 (same dimension), and nothing near 2. A plain-step search is therefore expected to fail for every assignment. 1a stays open only with an added junction parameter, such as tapered (cone) crimps, preferably bounded to short, plausible tapers.

### 1b. Three dimensions: neutrinos as the lightest (1, 0) mode

No separate neutrino line. The neutrino is a mode circulating in only one dimension of the delta. Per [metric-charge ch. 2 §4.2](../metric-charge/02-modes-on-a-sheet.md), single-axis modes carry mass without observable charge, because charge requires winding in both directions. This is the "tiny-tube" reading of [ma-domain neutrino-1D §5](../ma-domain/work/neutrino-1D.md). **Do this before 1a:** the spectrum is nearly analytic.

- [x] **Done (K4):** pinned m₁ = 4.24×10¹⁰ fm with ma-domain's solver (`--pin`). K4 still fits all nine masses, but in every surviving assignment m₁ is the sheared direction of the e and μ sheets, so no light single-axis mode exists on it. Pinning m₁ does not remove K4's free parameter.
- [ ] (Superseded for K4) Identify which delta dimension can carry it. K4's free dimension m₁ (4,505 fm to 2×10¹⁵ fm) includes the neutrino scale (≈ 3×10¹⁰ fm). If the neutrino line is m₁, the neutrino mass would fix K4's last free parameter.
- [ ] Compute the light mode spectrum on the delta's metric, including the sheets' cross terms, with m₁ at the neutrino scale. Check for a near-degenerate pair plus a third, and the ratio 33.6.
- [ ] Expected spectrum: single-axis modes on m₁ form a harmonic ladder (±1, ±2, …), so ν₁/ν₂ = the ±1 pair and ν₃ = n = 2, the ν₃ ≈ 2 ν₁ (Family A) point. Confirm with the full metric.
- [ ] Check what splits the ± winding pair. Sheet shear does not split sign partners ([metric-charge ch. 6 §6](../metric-charge/06-handedness-and-pairs.md)). If only the grid's direction bias would, record that, and bring it in only if needed.
- [ ] Check the electron's excited states when m₁ is at the neutrino scale (states just above the electron mass); metric-charge's closure rule should limit them.
- [ ] Address the τ problem: m₁ belongs to the e and μ sheets but not to τ = (m₂, m₃), so the three neutrino flavors do not map one-to-one onto sheets containing m₁.

### 1c. A massless or very light ν₁ (unexplored family)

The data allow m₁ = 0 (masses 0, 8.7, 50 meV; f₂ ≈ 2.1 THz, f₃ ≈ 12.1 THz; Σm ≈ 59 meV, the only family so far under the ≈ 70 meV cosmology figure). This needs no near-degenerate mass pair, but f₃/f₂ ≈ 5.8.

- [ ] Look for hosts where ν₁ is a zero-frequency (or nearly zero) mode and ν₂, ν₃ are the next two modes. Unflipped loops already have a zero mode, which earlier work excluded.

## 2. Deferred until §1 is settled

- [ ] **Junction mechanics:** crimp/pinch junctions approached by cones (taper length as the one new parameter), using the actual dimension sizes at the ends; abrupt vs. gradual transitions ([junction-fit.md](work/junction-fit.md), Tests 1 and 3).
- [ ] **GRID Stages 2–3** ([grid-circle.md](work/grid-circle.md)): flavor exchange inside the circle; propagation through space to check the L/E oscillation signature.
- [ ] **CP:** bring in the grid's direction bias only if experiments establish δ ≠ 0, π in normal ordering (DUNE, Hyper-K), or establish inverted ordering (JUNO) ([junction-fit.md](work/junction-fit.md), Test 2).

## 3. Open questions carried by every candidate

- [ ] Spin ½ relative to ordinary space: why a 360° rotation in space corresponds to one internal circuit ([mechanisms §4](work/mechanisms.md)).
- [ ] Magnetic moment of a standing-wave mode under MaSt's assignment of current to modes.
- [ ] Flavor coupling: where along the host a charged lepton couples (point vs. segment); both definitions agree so far.
- [ ] Klein tracks (host E3): selection rule for the extra stationary tracks, and a wave-localization check ([klein-tracks.md](work/klein-tracks.md)).

## 4. Chapters and housekeeping

- [ ] Draft chapter 2, "The twisted ring" (README chapter arc).
- [ ] Resolve the R61 mode-label and calibration inconsistencies ([prior-work.md](reference/prior-work.md)).
