# R28 Findings


## Track 1. σ_eν and σ_νp exploration

Script: `scripts/track1_cross_shear_sweep.py`


### F1. Neutrino cross-shears do not improve the spectrum

Sweeping σ_eν from −0.20 to +0.20 (at σ_νp = 0) changes
the RMS fractional error by < 0.01%.  Sweeping σ_νp over
the same range changes it by < 0.5%.  The 2D grid search
over both confirms: **σ_eν = σ_νp = 0 is already optimal.**

The neutrino sheet decouples from the particle spectrum at
MeV scale.  This is the same insensitivity found for r_e in
R29 (F22): the neutrino dimensions are so large that their
cross-shear contributions to mode energies are negligible.


### F2. Individual particle responses to σ_νp

While the overall RMS doesn't improve, individual particles
shift slightly under σ_νp:

| σ_νp | τ⁻ | π⁺ | K⁺ | Λ | Σ⁺ |
|------|-----|-----|-----|-----|-----|
| −0.20 | 5.3% | 13.1% | 0.6% | 7.3% | 13.0% |
| −0.16 | 5.5% | 13.3% | **0.0%** | 7.6% | 13.4% |
| 0.00 | 5.6% | 13.5% | 1.2% | 5.8% | 11.6% |
| +0.16 | 5.5% | 13.3% | **0.0%** | 7.6% | 13.4% |
| +0.20 | 5.3% | 13.1% | 0.6% | 7.3% | 13.0% |

At σ_νp ≈ ±0.16, the kaon K⁺ matches exactly (0.00%).  But
this worsens Λ (5.8% → 7.6%) and Σ⁺ (11.6% → 13.4%).  The
trade-off is unfavorable — the kaon was already at 1.2%.


### F3. The problem particles are structural, not parametric

The large-gap particles are unchanged by cross-shear tuning:

| Particle | Gap at baseline | Gap at best σ_νp |
|----------|----------------|-----------------|
| π⁺ | 13.5% | 13.1% |
| τ⁻ | 5.6% | 5.3% |
| ρ⁰ | 20.9% | ~20% |
| ω | 19.9% | ~20% |
| Σ⁺ | 11.6% | 11.6% |
| Δ⁺⁺ | 14.2% | ~14% |

These gaps are structural — the particles don't sit near any
Ma (the six-dimensional material space) eigenmode regardless of parameter values.  This is fully
consistent with R27's off-resonance hypothesis: these are
transient excitations, not exact eigenmodes.  Their gaps
from the nearest mode correlate with lifetime (R27 F37–F42).

**Note (updated by Track 3):** The Λ and Σ⁺ entries above
used n_max = 8.  Track 3 found that extending to n_max = 15
reveals much closer modes: Λ drops to 0.9%, Σ⁺ to 0.3%.
These two are NOT structurally off-resonance — they were
limited by search range.  The other particles in this table
(π⁺, τ⁻, ρ⁰, ω, Δ⁺⁺) remain genuinely off-resonance.


### F4. Summary of Track 1

1. **σ_eν and σ_νp = 0 is optimal.** No improvement from
   the 2D grid search.

2. **The neutrino sheet decouples** from the particle
   spectrum at MeV scale — same as r_e and r_ν.

3. **Problem particles are structural,** not fixable by
   parameter tuning.  This strengthens the off-resonance
   interpretation.

4. **Free parameter status unchanged.**  σ_eν and σ_νp
   remain unconstrained but also irrelevant.


---

## Track 2. Mode census below 2 GeV

Script: `scripts/track2_mode_census.py`


### F5. The Ma spectrum has ~48 energy bands below 2 GeV

Removing the near-degenerate n₂ dimension (which shifts
energy by only ~0.02 MeV per step), the Ma spectrum below
2 GeV consists of approximately **48 energy bands** spaced
by the proton-tube scale (~53 MeV) and proton-ring scale
(~470 MeV).

The main bands correspond to proton-sheet harmonics:
- 0, 53, 106, 159, 212, 264, 317, 370, 423 MeV  (tube)
- 470, 940, 1409, 1877 MeV  (ring)
- And all combinations thereof

Above ~470 MeV, the bands densify as tube and ring
combinations fill the spectrum more closely.


### F6. Each energy band contains all charges and spins

At every energy band, the Ma geometry produces modes at
all charge values Q = −2 to +2 (for |Q| ≤ 2) and all
spin values (0, 1/2, 1, 3/2).

Total modes with |Q| ≤ 2 below 2 GeV: **~900**
(ignoring n₂ degeneracy).

Known particles below 2 GeV: **~40**.

The model predicts ~20× more physically-charged modes
than observed particles.  This is the "ghost mode"
problem — most Ma modes have no observed counterpart.


### F7. The ghost problem is consistent with off-resonance

The ghost modes are not a flaw — they are the
off-resonance excitations from R27.  The interpretation:

- Every energy band supports oscillation patterns at all
  (Q, S) combinations.
- Most are transient excitations that decay instantly.
- The few that are observed as particles are either:
  (a) exact eigenmodes (stable particles)
  (b) near-resonance excitations (long-lived particles)
  (c) broad resonances measured in scattering experiments
      (many of the "ghosts" may correspond to known
      resonances we did not include in our catalog)

The R27 lifetime-gap correlation (r = −0.84 for weak decays)
supports this: particles closer to eigenmodes live longer.
Ghost modes far from any eigenmode would be unobservably
short-lived.

Note: our catalog included only ~40 well-established
particles.  The PDG lists hundreds of resonances below
2 GeV (N*, Δ*, Λ*, Σ*, meson excitations).  Many "ghost"
modes likely correspond to these measured but short-lived
states.


### F8. The proton-sheet energy ladder is rigid

The energy bands are determined by the proton-sheet
geometry (L₅ = 23.7 fm, L₆ = 2.66 fm), which is fixed
by the proton mass and r_p = 8.906.  The band structure
is insensitive to all other parameters.

This means:
- The particle mass spectrum has a **fixed scaffold** set
  by the proton sheet
- Particles can only exist near these energy bands
- The electron and neutrino sheets contribute charge and
  spin variety within each band, but not new energy levels


### F9. Summary of Track 2

1. **~48 energy bands** below 2 GeV from the proton-sheet
   energy ladder.

2. **~900 modes** at physical charges (|Q| ≤ 2), vs ~40
   known particles.  The model over-predicts by ~20×.

3. **Not a flaw:** Most ghost modes likely correspond to
   short-lived resonances (hundreds in the PDG) or to
   excitations too brief to observe.

4. **The spectrum is a scaffold:** The proton sheet sets
   rigid energy bands.  Particles must live near these bands.
   The electron/neutrino sheets contribute charge and spin
   variety within each band.


---

## Track 3. Strange baryon refinement

Script: `scripts/track3_strange_baryons.py`


### F10. R27's sign flips were a search-range artifact

R27 used n_max = 8, restricting quantum numbers to |n| ≤ 8.
This limited the search to proton-sheet harmonics with
|n₅| ≤ 8.  The nearest Q = 0, S = ½ mode below |n₅| ≤ 8
falls at 1050.9 MeV — 65 MeV below the Λ mass and below
the p + π decay threshold (1096.8 MeV), causing sign flips.

Extending to n_max = 15 reveals proton-sheet harmonics at
higher energies that were inaccessible in R27's search:

| Particle | R27 mode (n_max=8) | New mode (n_max=15) |
|----------|-------------------|---------------------|
| Λ (1115.7 MeV) | 1050.9 MeV (+5.8%) | 1105.9 MeV (+0.9%) |
| Σ⁺ (1189.4 MeV) | 1050.9 MeV (+11.6%) | 1193.4 MeV (−0.3%) |

The new modes are above the decay threshold, resolving all
four sign flips.


### F11. All four sign flips resolved

With the extended mode assignments:

| Reaction | Q_mode (R27) | Q_mode (new) |
|----------|-------------|-------------|
| Λ → p + π⁻ | −45.8 (FLIP) | +9.2 (OK) |
| Λ → n + π⁰ | −47.1 (FLIP) | +7.9 (OK) |
| Σ⁺ → p + π⁰ | −45.8 (FLIP) | +96.7 (OK) |
| Σ⁺ → n + π⁺ | −47.1 (FLIP) | +95.4 (OK) |

The R27 reaction scorecard improves from 17/21 to **21/21** —
every tested decay reaction is now mode-level sign-consistent.


### F12. Energy is dominated by proton-sheet harmonics

The new Λ mode n = (−12,−15,1,0,−12,−2) has:
- Proton dimensions (n₅,n₆): contribute 1105 MeV
- Electron dimensions (n₁,n₂): contribute 4 MeV
- Cross-term (σ_ep coupling): −3 MeV

The high |n₁| = 12 and |n₂| = 15 values are cosmetic: L₁
and L₂ are so large (32,000 and 4,900 fm) that each n-step
adds < 0.04 MeV.  The physical mode lives on the proton
sheet at harmonics (n₅ = −12, n₆ = −2).

Similarly, the Σ⁺ mode n = (−14,−15,0,0,−13,2) is
determined by its proton harmonics (n₅ = −13, n₆ = 2).


### F13. The energy band landscape near Λ and Σ⁺

Between 1000–1300 MeV, Ma produces 9 energy bands at
Q = 0, S = ½ and 18 bands at Q = +1, S = ½.  The bands
are spaced by ~25–55 MeV (proton-tube harmonics).

For Λ (1115.7 MeV): the two nearest bands sit at 1105 and
1161 MeV — the Λ mass falls between them at +10.7 and
−45.7 MeV respectively.  The 1105 band is the best match
at 0.9%.

For Σ⁺ (1189.4 MeV): a band exists at 1193.4 MeV — almost
exactly at the observed mass (−0.3%).  This is a remarkable
match, better than many "well-behaved" particles.


### F14. Σ⁺ joins the sub-1% club

With the extended assignment, Σ⁺ achieves a 0.3% gap,
placing it among the best-matched particles in the catalog
alongside the proton (0.0%), neutron (0.0%), muon (0.5%),
kaon (1.2%), and phi (0.8%).

The Λ at 0.9% also improves dramatically from 5.8%.

These were R27's two worst-performing baryons.  Their poor
showing was not a structural failing of the model but a
consequence of the limited search range.


### F15. Updated R27 scorecard

With the extended mode assignments, the full R27 particle
catalog is updated:

| Category | R27 within 1.5% | Updated within 1.5% |
|----------|----------------|---------------------|
| Stable/long-lived | 5 of 19 | 7 of 19 |
| Reaction sign flips | 4 of 21 | 0 of 21 |

The Λ (0.9%) and Σ⁺ (0.3%) join the sub-1.5% group.  The
remaining large-gap particles (π⁺ at 13.5%, τ⁻ at 5.6%,
ρ⁰ at 20.9%, etc.) are genuinely off-resonance — their
gaps correlate with lifetime (R27 F37–F42).


### F16. Summary of Track 3

1. **R27's sign flips were a search artifact**, not a model
   defect.  Extending n_max from 8 to 15 reveals better
   modes for both Λ and Σ⁺.

2. **All 4 sign flips resolved.**  Every tested decay is
   now mode-level sign-consistent (21/21).

3. **Λ gap: 5.8% → 0.9%.  Σ⁺ gap: 11.6% → 0.3%.**
   Both particles move from "problem cases" to among the
   best matches in the catalog.

4. **The energy is physical.**  High electron-dimension
   quantum numbers are cosmetic (< 4 MeV); the real physics
   is proton-sheet harmonics at |n₅| ~ 12–14.

5. **Strange baryons are not structurally problematic.**
   The model accommodates them well once the search range
   includes the relevant proton harmonics.


---

## Track 4. High-energy modes (W, Z, Higgs)

Script: `scripts/track4_high_energy.py`


### F17. W, Z, and Higgs all have nearby Ma modes

| Particle | Observed (MeV) | Mode (MeV) | Gap |
|----------|---------------|-----------|------|
| W± | 80,379 | 80,379.1 | 0.0002% |
| Z⁰ | 91,188 | 91,188.5 | 0.0006% |
| H⁰ | 125,250 | 125,250.1 | 0.0001% |

All three match to < 1 MeV.  The quantum numbers are
large: n₅ ~ 14–283, n₆ ~ 171–263.


### F18. The matches are trivially easy

Fake particles at arbitrary high-energy masses match
equally well:

| Target | Mass (MeV) | Gap | Real? |
|--------|-----------|------|-------|
| Fake-C | 110,000 | 0.0001% | no |
| W± | 80,379 | 0.0002% | yes |
| Z⁰ | 91,188 | 0.0006% | yes |
| Fake-D | 75,000 | 0.0006% | no |
| Fake-B | 97,500 | 0.0014% | no |
| Fake-A | 83,000 | 0.0018% | no |
| H⁰ | 125,250 | 0.0001% | yes |

Real and fake particles are indistinguishable.  The Ma
spectrum is so dense above ~5 GeV that any mass can be
matched to < 0.01%.


### F19. Band density grows linearly with energy

| Energy | Modes in ±500 MeV | Avg spacing |
|--------|-------------------|------------|
| 500 MeV | 33 | 29.3 MeV |
| 1 GeV | 66 | 15.3 MeV |
| 2 GeV | 126 | 7.9 MeV |
| 5 GeV | 313 | 3.2 MeV |
| 10 GeV | 629 | 1.6 MeV |
| 80 GeV | 527 | 1.9 MeV |
| 125 GeV | 1,748 | 0.6 MeV |

The mode count in a fixed window scales roughly as E
(2D lattice point counting on the proton sheet).
Above ~2 GeV the spacing drops below the typical
particle mass uncertainty, making all matches trivial.


### F20. The W/Z ratio is not geometrically special

The observed ratio m_Z/m_W = 1.1345 is reproduced by
72,621 mode pairs within ±200 MeV of the W and Z masses.
The spectrum is so dense that any ratio near 1.1 is
achievable by multiple pairs.  The W/Z ratio carries no
geometric content in this model.


### F21. Ma has a predictive horizon at ~2 GeV

Below ~2 GeV, the average band spacing (~8–30 MeV) is
comparable to particle mass differences, so matching a
specific mass is non-trivial.  The model can distinguish
a proton (938) from a neutron (940), a pion (140) from
a kaon (494), etc.

Above ~2 GeV, the spacing drops below ~5 MeV and any
target mass matches to < 0.1%.  The model loses all
discriminating power.

This boundary roughly coincides with the transition from
hadronic physics (QCD scale, ~1 GeV) to electroweak
physics (~80–125 GeV) in the standard model.  The Ma
model's natural domain is the particle spectrum below
~2 GeV — which is also where all its structural
predictions (eigenmodes, off-resonance gaps, lifetime
correlations) operate.


### F22. Summary of Track 4

1. **W, Z, Higgs all match** to < 0.001% — but so does
   any arbitrary mass above ~5 GeV.

2. **The W/Z mass ratio is not special** in Ma geometry.
   Tens of thousands of mode pairs reproduce it.

3. **Ma has a predictive horizon at ~2 GeV.**  Below
   this, the proton-sheet energy ladder is sparse enough
   to make mass predictions non-trivial.  Above it, the
   spectrum is a continuum.

4. **Implication for W/Z/Higgs:** The Ma model says
   nothing about electroweak physics.  These particles
   are not structural predictions of the geometry — they
   live in a regime where the model has no discriminating
   power.  Whether the Higgs is "real" or not is beyond
   the model's reach.
