# R58: Phonon material search for neutrino frequency matching

**Status:** Active — Track 1 in progress
**Questions:** Q119 (PdD phonon / neutrino coincidence)
**Type:** compute
**Depends on:** R49 (neutrino families), L05 (optical beat lab)

---

## Motivation

Q119 identified that the optical phonon modes of deuterated
palladium (PdD at 8.3, 15.3 THz) overlap with MaSt's predicted
neutrino frequencies (ν₁ = 7.06, ν₃ = 14.07 THz for Family A).
The Letts-Cravens-Hagelstein dual-laser LENR experiments saw
excess heat at exactly the PdD phonon frequencies.

If a material could be found whose phonon frequency matches
a neutrino frequency EXACTLY (not the 15% near-miss of PdD),
it would serve as a precision resonant filter: converting an
optical beat into a real phonon oscillation at exactly the
neutrino coupling frequency.

This study systematically searches for such materials across
all four neutrino families.


## Target frequencies

From R49 / L04:

| Family | ν₁ (THz) | ν₂ (THz) | ν₃ (THz) |
|--------|---------|---------|---------|
| A | 7.06 | 7.37 | 14.07 |
| B | 1.23 | 2.44 | 12.11 |
| C | 0.82 | 2.25 | 12.28 |
| D | 7.16 | 7.45 | 14.00 |

12 distinct frequencies spanning 0.82–14.07 THz.


## Approach

### Track 1: Systematic binary compound survey

Compute the estimated optical phonon frequency for every
binary compound A-B where A and B are drawn from a pool
of ~50 common elements.  Score each by proximity to each
of the 12 target frequencies.

The TO phonon frequency of a binary crystal scales as:

> f_TO ∝ √(k / μ)

where k is the bond stiffness and μ = m₁m₂/(m₁+m₂) is
the reduced mass.  For compounds with SIMILAR bond types
(e.g., all III-V or all II-VI), k is approximately constant
and f scales as 1/√μ.

**Method:**
1. Use known phonon frequencies as calibration points
   (GaAs at 8.0 THz, etc.)
2. For each bond-type family, derive k from the calibrator
3. Estimate f_TO for every compound in that family
4. Score against the 12 target frequencies
5. Report all matches within ±5%

### Track 2: Metal hydride / deuteride survey

Separately search metal-hydrogen and metal-deuterium
compounds, since these have a different bond-type family
(metal-H bond vs covalent or ionic).

### Track 3: Molecular vibration survey

Extend beyond binary crystals to molecular vibrations
(e.g., organometallics, metal-organic frameworks, molecular
crystals) where the vibrational frequency can be tuned by
substitution.

### Track 4: DFT validation candidates

For the top candidates from Tracks 1–3, note which ones
have been measured experimentally and which would benefit
from density functional theory (DFT) calculations to confirm
the estimated frequency.


## Deliverables

- A ranked table of materials per target frequency
- Separate tables for each neutrino family
- Identification of materials that match MULTIPLE targets
  (e.g., one material for ν₁ and a different one for ν₃)
- Practical notes: availability, toxicity, crystal form,
  hydrogen compatibility
