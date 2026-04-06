# R50 Review Notes

Independent review of findings and methodology.
Organized by track, updated as tracks complete.

---

## Track 1: Build `ma_model_d.py`

**Verdict:** Sound. No fatal errors.

The model engine is clean, assumption-free, and validated.
Energy, charge, spin (topological), waveguide filtering,
mode scan, and near-miss finder all work correctly. The
alpha formula reproduces 1/137 on both sheets at different
ε values. The self-consistent L_ring derivation from G̃⁻¹
is an improvement over model-C's iterative scheme.

**One clarification on F4 (composite charge):** The gcd-based
formula Q = −n₁ + n₅/gcd(n₅,n₆) gives the right answer for
all modes in the survey. The physical mechanism (per-strand
CP synchronization from R48) is different from the mathematical
shortcut (dividing a bulk quantum number by gcd), but they
produce identical results for all modes where gcd divides n₅
evenly — which is guaranteed by the definition of gcd. No
action needed; the distinction is documented in R48 and Q105.

**The confinement problem (F3):** correctly identified and
honestly handled. The standalone (1,2) mode on Ma_p propagates
through the waveguide — predicting a Q = +1, spin-½ particle
at ~313 MeV that doesn't exist. This IS the quark confinement
problem. The decision to flag these modes and proceed (rather
than wait for confinement to be solved) is correct.


## Track 2: Cross-shear sweep — neutron

**Verdict:** Sound. Amended findings address all concerns.

The cross-shear mechanism (F14) is mathematically correct
and physically sensible. The Schur complement modifies the
proton block of G̃⁻¹, shifting proton-ring modes relative
to the reference mass when L_ring_p adjusts. The self-
consistent L_ring derivation keeps reference masses exact
to machine precision (F16). The methodology is clean.

### Neutron candidate assessment

Two candidates were found. The amended findings handle
them correctly:

**F12 (preferred): (0, 4, 1, −2, 0, 8) at σ_ep ≈ −0.13**
— spans all three sheets, has electron-sheet winding
(n₂ = 4), can decompose into proton + electron + neutrino
for beta decay. Mass residual 0.358 MeV, consistent with
the neutron being a near-miss (unstable, τ = 879 s).
Correctly identified as the physical neutron candidate.

**F11 (flagged): (0, 0, 2, 2, 0, −8) at σ_νp ≈ −0.13**
— better mass match (0.25 MeV) but no electron-sheet
winding. The amended findings correctly flag the
decomposition concern without disqualifying the mode
(the counter-argument about cross-sheet energy transfer
is noted). May be a dark or exotic neutral fermion.

The amended F12b (dark windings) is a good addition —
it explains how neutral massive modes carry their mass
through ring windings and neutrino-sheet windings that
enter the energy formula but not the charge formula.

### Items resolved by amendment

The original findings presented F11 as the primary
neutron candidate without noting the beta-decay
decomposition problem. The amended version:
- Raises the concern explicitly in F11
- Elevates F12 as the preferred candidate
- Adds the structural comparison table to model-C
- Adds F12a (σ_νp implications for fusion)
- Adds F12b (dark windings as mass carriers)
- Updates the Track 2 summary with confidence levels

All concerns from the initial review are addressed.
No remaining issues.

### Structural comparison to model-C neutron

| Property | Model-C neutron | F12 candidate |
|----------|----------------|---------------|
| Mode | (0, −2, 1, 0, 0, +2) | (0, 4, 1, −2, 0, 8) |
| Ma_e winding | n₂ = −2 | n₂ = 4 |
| Ma_ν winding | n₃ = 1 | n₃ = 1, n₄ = −2 |
| Ma_p winding | n₆ = +2 | n₆ = 8 |
| Spin source | Ma_ν (n₃ = 1) | Ma_ν (n₃ = 1) |
| Cross-shear | σ_ep = −0.091 | σ_ep = −0.130 |
| Mass residual | 0 (pinned) | 0.358 MeV |
| Beta decay | ✓ (has e winding) | ✓ (has e winding) |

Both get spin from Ma_ν (n₃ = 1). Both have electron-sheet
winding (enabling beta decay). The model-D candidate has
higher winding numbers throughout — n₂ = 4 vs −2, n₆ = 8
vs 2. This reflects the different geometry (proton as (3,6)
at ε_p = 0.55, vs proton as (1,2) at r_p = 8.906).

The n₆ = 8 proton-ring winding is high (compared to the
proton's n₆ = 6). The neutron winds the proton ring at a
higher harmonic than the proton itself. Whether this has
physical consequences should be investigated.

### σ_νp finding and fusion implications

F11 found σ_νp ≈ −0.13 produces a mode near the neutron
mass. While F11's specific candidate is not the neutron
(no electron winding), the fact that σ_νp must be nonzero
and ~0.13 in magnitude is important for Q89 (fusion).

The fusion bootstrap pathway (Q89 §12.2) requires σ_νp ≠ 0
so that every proton has a virtual neutrino-sheet
fluctuation that can be pumped by IR at 42 μm. Track 2
establishes that σ_νp ≈ 0.13 is needed for the neutron —
confirming that this cross-shear is physically nonzero and
of substantial magnitude.

However: the physical neutron candidate (F12) uses σ_ep,
not σ_νp. If the neutron is produced by σ_ep ≈ −0.13
rather than σ_νp, the σ_νp value remains unconstrained
by the neutron mass. Both cross-shears may be nonzero
(the F11 and F12 candidates come from different σ sweeps),
but only σ_ep is directly constrained by the neutron if
F12 is the correct identification.

### Notes for downstream tracks

- Track 5 should check whether the 0.358 MeV residual
  maps to 879 s under the off-resonance power law
  (τ ∝ |gap|^−2.7 from R27 F33).

- The F11 mode (0, 0, 2, 2, 0, −8) should be checked
  against the dark matter candidate list — it may be
  one of the ghost modes from R42.

- Future neutron searches should include "nonzero
  electron-sheet winding" as a physical plausibility
  filter (not a hard filter — F11 is still carried
  forward, but decomposition-viable candidates should
  be flagged separately).

### Other notes

- **F13 (σ_eν has zero effect)** is expected and correct.
  The electron and neutrino sheets are both too large to
  contribute significant energy at the proton scale.

- **F14 (indirect mechanism)** is the most important
  structural finding. The Schur complement mechanism is
  mathematically clean and physically motivated.

- **F15 (mode spacing limits resolution)** is an important
  structural insight. The neutron-proton mass difference
  (1.293 MeV) is only 1.08% of the proton mode spacing
  (~119 MeV). Cross-shear tuning of L_ring is required
  to land this close. This means σ is constrained by the
  neutron — the neutron's existence tells us something
  about the cross-coupling.


## Track 3

*(Not yet reviewed.)*


## Track 4

*(Not yet reviewed.)*


## Track 5

*(Not yet reviewed.)*
