# R28. T⁶ spectrum refinement

**Questions:** Q16 (mass spectrum), Q32 (energy-geometry)
**Type:** compute  **Depends on:** R27
**Status:** Not started


## Motivation

R27 produced a zero-parameter particle catalog: 19 particles
searched, 5 within 1.5%, and a lifetime-gap correlation
(r = −0.84 for weak decays) supporting the off-resonance
hypothesis.  But several loose ends remain:

1. **σ_eν and σ_νp were zero throughout.**  These cross-shears
   couple the neutrino sheet to the electron and proton sheets.
   They were set to zero for simplicity.  Nonzero values might
   shift mode energies enough to improve the pion (14% off),
   the tau (5.6%), and the strange baryons (Λ, Σ⁺).

2. **Mode overcounting.**  R27 asked "for each known particle,
   what's the nearest T⁶ mode?"  The inverse question — "what
   T⁶ modes exist that don't correspond to any known particle?"
   — is equally important.  A model that predicts 200 particles
   where nature has 20 is not predictive.

3. **Strange baryon assignments.**  The Λ and Σ⁺ caused the
   only reaction-energy sign flips (F45).  Their mode
   assignments may need refinement with nonzero σ_eν/σ_νp.

4. **W, Z, and Higgs.**  R27 searched only up to ~1.7 GeV.
   The W (80.4 GeV), Z (91.2 GeV), and Higgs (125.3 GeV)
   are fundamental particles at much higher energy.  Can the
   T⁶ reach them?


## Core questions

1. Do σ_eν and σ_νp improve the spectrum?
2. How many T⁶ modes exist below 2 GeV, and how does this
   compare to the number of known particles?
3. Can the W/Z mass ratio (1.134) emerge from T⁶ geometry?
4. Is the Ω⁻ genuinely forbidden, or does it appear with
   nonzero neutrino-sector shears?


## Approach

### Track 1 — σ_eν and σ_νp exploration

Sweep σ_eν and σ_νp over their allowed ranges (maintaining
positive-definite metric).  At each point:
- Recompute the self-consistent metric
- Rerun the Track 5 particle catalog
- Record changes in mode energies, gap sizes, and match quality

**Key targets:**
- Does the pion gap (14%) shrink?
- Does the tau gap (5.6%) shrink?
- Do the Λ/Σ⁺ sign flips resolve?

**Deliverable:** Contour plots of match quality in the
(σ_eν, σ_νp) plane.


### Track 2 — Mode census below 2 GeV

Enumerate **all** T⁶ modes with E < 2000 MeV at the pinned
parameter point (and at the best point from Track 1).

For each mode, classify:
- Matched to a known particle (within some threshold)
- Unmatched — a "ghost mode" the model predicts but nature
  does not exhibit

**What to look for:**
- If ghost modes are few, the T⁶ spectrum is economical.
- If ghost modes are numerous, the model over-predicts and
  the single-mode picture may be too permissive.
- Ghost modes might correspond to particles not yet included
  in our catalog (e.g. D mesons, B mesons, other baryons).

**Deliverable:** Full mode census with matched/unmatched
classification.


### Track 3 — Strange baryon refinement

Focused search for better Λ (1115.7 MeV) and Σ⁺ (1189.4 MeV)
mode assignments using:
- Nonzero σ_eν and σ_νp from Track 1
- Larger quantum number ranges
- Asymmetric cross-shears

**Success criterion:** Λ and Σ⁺ decay reactions have
Q_mode > 0 (resolving the sign flips from R27 F45).


### Track 4 — High-energy modes (W, Z, Higgs)

Search for modes at 80–130 GeV.  These require large quantum
numbers (n ~ 80,000/938 ≈ 85 on the proton sheet), so the
search must be strategic rather than exhaustive.

**Method:** For each target, fix charge and spin constraints,
then solve for the ring winding n₆ (or n₂) that brings
E(n) closest to the target.

**What to look for:**
- m_Z / m_W ≈ 1.134 — does the T⁶ produce this ratio?
- Higgs (spin 0, charge 0) — is there a mode near 125.3 GeV?

**Deliverable:** Mode assignments for W, Z, H, or a finding
that the T⁶ does not naturally produce these masses.


## Infrastructure

Uses `lib/ma.py` and `lib/ma_solver.py` from R27.  May
require extensions to `ma_solver.py` for mode census and
high-energy search.

Scripts go in `R28-particle-spectrum/scripts/`.


## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R27   | Predecessor: particle catalog, lifetime correlation, parameter pinning |
| R26   | T⁶ framework, metric infrastructure |
| R19   | Shear-charge mechanism |
| R15   | The α problem — may connect to W/Z masses |
