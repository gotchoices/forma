# Q125: Could the spin rule act as a selector — disabling charge on modes that don't aggregate to a valid spin?

**Status:** Open — speculative working hypothesis.  Tenable and
productive-looking; no rigorous derivation yet.  Pool-item
derivation target.

**Related:**
  [Q124](Q124-spin-in-mast.md) (spin derivation — per-sheet Dirac–Kähler + SU(2) AM),
  [Q11](Q11-spin-statistics-filter.md) (earlier spin-statistics filter),
  [Q94](Q94-compton-window-and-dark-modes.md) (dark modes),
  [Q99](Q99-fourth-neutrino-mode.md) (fourth-neutrino suppression),
  [R60 Track 16](../studies/R60-metric-11/findings-16.md) (Z₃ confinement — a per-sheet example of this principle),
  [R60 Track 18](../studies/R60-metric-11/findings-18.md) (ν charge = 0 from conjugate-pair structure — another instance),
  [R62 derivation 7d](../studies/R62-derivations/derivation-7d.md) (per-sheet spin),
  [model-F](../models/model-F.md).

---

## 1. The question

MaSt's compactified architecture mathematically admits vastly
more compound modes than are observed as particles.  The KK
lattice on T⁶ × ℵ gives countably many (n_et, n_er, n_νt,
n_νr, n_pt, n_pr) modes at various masses, charges, and α
couplings.  Only a sparse subset corresponds to observed
particles.

The orthodox way to handle this is a series of filters —
waveguide cutoffs (R46), parity rules (R50), generation
resonances (R53), each tailored to a specific problem.  This
is ad hoc and leaves "why these filters and not others?" as an
open question.

**Could a single physical principle — that internal spin
alignment gates α-channel coupling — handle most of these at
once?**

## 2. The proposal

**Spin-gated charge principle (tentative):**

> A compound mode's coupling to the α channel is nonzero only
> if its tensor-product decomposition of per-sheet Dirac–Kähler
> spinors resolves to a **pure SU(2) spin eigenstate**.  Modes
> that don't internally align into a clean irreducible
> representation are dark — they exist geometrically (they have
> mass and obey the mass formula) but their α coupling
> vanishes.  As a consequence, such modes carry no observable
> electric charge (the metric-derived α_Coulomb is zero) and
> interact with spacetime only gravitationally.

Under this principle, MaSt's dense spectrum of KK modes is
filtered on observability by a single criterion: **does the
internal phase structure produce a pure spin state?**

- Pure-spin states: observable particles with their normal α
  coupling (electron, proton, mesons, baryons, etc.)
- Not-pure-spin states: geometrically exist, mass non-zero,
  α coupling zero — dark modes

## 3. Why this is tenable (alignment with existing MaSt pieces)

Several MaSt mechanisms already gesture at this principle in
specific contexts:

1. **Z₃ confinement on the p-sheet** (R60 Track 16).  Three
   (1, 2) quarks MUST align at 120° phase offsets to form a
   stable observable composite.  Without the Z₃ alignment,
   they're confined — no free-particle state.  This is a
   per-sheet instance of "internal phase alignment gates
   observability."

2. **ν charge = 0 from conjugate-pair superposition** (R60
   Track 18).  Real-field KK modes on the ν-sheet average the
   +n_t and −n_t components, giving ⟨n_νt⟩ = 0.  Without a
   symmetry-breaker (which the e-sheet has via extreme shear
   and the p-sheet has via Z₃), the tube charge averages to
   zero.  This is another instance of "internal alignment
   fails to break a specific symmetry → charge disabled."

3. **Spin-statistics theorem.**  Half-integer-spin states
   must be fermionic; integer-spin states must be bosonic.
   A state whose spin content is reducible doesn't
   transform cleanly under the Lorentz group as a single
   particle — it's a superposition of particle types.  The
   spin-gated charge principle generalizes: such reducible
   states don't couple to the gauge sector either.

4. **QCD color-singlet rule.**  Only color-singlet
   combinations are observable; colored quark states exist
   mathematically but don't propagate freely.  The
   mathematical structure is parallel: a specific
   internal-alignment condition gates observability.

The principle unifies these into one statement: **the same
internal-alignment condition that makes a mode a valid spin
eigenstate enables its α-channel coupling.  When the alignment
fails, both spin and charge fail together.**

## 4. What this would close

**Ghost modes.**  The persistent problem across every prior
MaSt model: the KK mode ladder is dense, but only a sparse
subset are observed.  Prior filters (R46 waveguide cutoff,
R50 spin-statistics filter, R53 generation resonance) were
each hand-crafted.  Under the spin-gated principle, these
collapse into one rule: modes without clean spin projection
have no α coupling and hence no electromagnetic observability.

**Dark matter.**  Modes that pass signature and mass formulas
but fail spin-alignment would gravitate (stress-energy nonzero)
but not interact electromagnetically.  That's the textbook
phenomenology of dark matter.  The principle would predict a
spectrum of such dark modes alongside the visible zoo — masses
from the KK formula, population from compactification geometry.
Testable in principle: are predicted dark modes consistent with
cosmological dark-matter mass bounds?

**Spin–charge coupling.**  For observed hadrons where spin and
charge are empirically correlated (all pseudoscalar mesons
have charge ±1 or 0 with spin 0; all vector mesons with spin
1; all baryons with half-integer spin), the principle naturally
ties them together.  Currently we treat spin and charge as
separate quantum numbers with independent filters.

## 5. What would need to be derived

The principle is a tentative working hypothesis, not a
derivation.  To elevate it to a derivation, the following
concrete problems need solution:

1. **Precise spin-projection condition.**  Under SU(2) ⊗ SU(2)
   for 2-sheet modes, both spin-0 and spin-1 are pure irreps
   — so the rule allows both.  The condition is "pure
   eigenstate of spin magnitude," not "spin equals a specific
   value."  Formalize this.

2. **Coupling-cancellation mechanism.**  Why does a reducible
   (mixed) spin state have vanishing α coupling?  Standard QM
   gives this at the matrix-element level (off-diagonal spin
   elements don't contribute to coherent gauge coupling), but
   translating this to MaSt's metric-derived α coupling needs
   explicit derivation.  Likely involves the Dirac spin
   projection's compatibility with the metric's σ_ta entry.

3. **Stability/lifetime story.**  Spin-1 mesons (ρ, φ) ARE
   observed but as short-lived resonances (width ~100 MeV).
   Under the principle, why are spin-0 mesons long-lived but
   spin-1 mesons broad?  The AM-allowed-set rule (R60 Track
   20, R62 7d) doesn't distinguish; additional dynamical input
   (symmetry of internal combination) must explain the
   lifetime gradient.

4. **Map to existing filters.**  Show explicitly that R46's
   waveguide cutoff, R50's spin-statistics filter, and R53's
   generation resonance are SPECIAL CASES of the spin-gated
   principle.  If the principle is right, each of these should
   reduce to it under the appropriate geometric limit.

## 6. Alignment with Track 20's empirical result

R60 Track 20's unit-per-sheet AM rule is the forward direction
of this principle: it predicts the allowed spin set per
sheet count.  The reverse direction — "modes that don't match
get no coupling" — is the new content proposed here.

Track 20's search already implicitly used both directions (as
a filter on tuples that don't match observed spin), but it
didn't formulate the physical mechanism (α coupling gating).
The spin-gated charge principle names that mechanism
explicitly.

## 7. Implications if true

- **Model-F ghost mode concerns** (R60 Track 17 Phase 4, R61
  ν-sheet (1, 0) ghost) become automatic under this principle.
  No external filter needed.
- **Pool item i** (alternative ghost-suppression mechanisms)
  could be resolved.
- **Dark matter candidate** at KK-mode mass scales; a testable
  prediction once the predicted dark spectrum is characterized.
- **The "why three generations?" question** gets a partial
  answer: the generation resonance is what SELECTS the
  spin-aligned modes from the sheet's ladder; other modes are
  dark.  The spin-gated principle tells us they still exist
  but are invisible.

## 8. Caveats

- The principle is **not yet derived**.  It's a structural
  proposal that aligns with several existing MaSt mechanisms,
  but the explicit "coupling-cancellation" derivation is
  needed.
- It may prove INSUFFICIENT alone — the spin-aligned subspace
  may still contain more modes than observed (e.g., infinitely
  many (n, 2n) excitations on e-sheet all giving spin ½).
  Additional physics (R53 resonance, R46 cutoff) may still be
  needed to select the specific observed spectrum from the
  spin-aligned subspace.
- The "dark mode" prediction is powerful but risks
  over-prediction.  If the principle predicts too many dark
  modes (exceeding cosmological dark-matter mass bounds), it
  would be ruled out.

## 8a. Complementary mechanism — least-cost energy routing

Spin-alignment is one filter on which modes form observable
particles.  A separate and equally important filter is
**energy routing between Ma compactification and S (3-space)
separation**.

R56 established that a mode's existence as a Ma compound is
not a foregone conclusion: if separating its content into
distinct S-space locations costs less energy than binding it
into a single Ma compound, the S-separated configuration is
preferred.  This is what produces atomic shell structure —
higher electron orbitals routed to larger r rather than
higher Ma harmonics, because spatial separation costs ~2.5×
less than promoting to the next angular harmonic.

This mechanism is **orthogonal to spin-alignment** and
operates alongside it:

- **Spin-alignment failure** → mode exists but has no α coupling
  → dark
- **Energy-routing failure** → mode doesn't form as an Ma
  compound at all → content exists as separated S-space
  entities (atoms, plasmas, free particles)

For example, a hypothetical Ma compound at winding
`(1, 2, 0, 0, 3, 6)` has:

- Topological charge Q = −1 + 3 = +2
- Composite α_sum = 1 − 1 + 0 = 0, so α_Coulomb = 0
- Mass ≈ 938 MeV (dominated by the p-sheet (3, 6) piece)
- 2 active sheets → spin-0 or spin-1

Under the spin-gated principle alone, this mode is
*geometrically admitted* but *α-decoupled* — potentially a
dark Q=+2 state at ~938 MeV.

But under energy-routing analysis, the same content
separated in S — a free proton at 938.272 MeV plus a free
electron at 0.511 MeV — has total energy 938.78 MeV.  The
difference is small (~0.5 MeV), but crucially, S-separation
is ENERGETICALLY PREFERRED because:

1. The separated configuration can form a hydrogen atom with
   additional 13.6 eV binding via the Coulomb potential in
   S.
2. The Ma compound lacks natural formation channels — on
   model-F's baseline with zero cross-sheet σ entries, the
   e-sheet and p-sheet are dynamically independent.  A mode
   with simultaneous windings on both sheets has no simple
   formation pathway.

So the (1, 2, 0, 0, 3, 6) mode is almost certainly **not
formed** in the first place, regardless of whether the
spin-gated principle would have made it dark.  Energy routing
suppresses it before the spin filter ever applies.

**The full picture: a mode is observable as a particle only
if it (a) forms as a Ma compound (energy-routing allows it),
AND (b) has proper spin-alignment (charge coupling enabled).**

Either filter can suppress observability; only modes passing
BOTH become observed particles.

## 8b. Implication for the ghost mode problem

This two-filter picture affects how we think about the ghost
problem:

- Most apparently "predicted but unobserved" Ma compound modes
  are likely suppressed by energy routing, NOT by
  spin-alignment.  Their content can form as cheaper
  S-separated states (atoms, ions, free particles, radiation).
- The spin-gated principle's primary value is in explaining
  why certain COMPOUND MODES that DO form have zero EM
  coupling — true dark-matter candidates that can't simply
  "route around" via S-separation because their constituents
  are already combined.
- Energy routing is the dominant suppressor for most of the
  infinite KK mode ladder; spin-gated charge is the
  dominant suppressor for the modes that survive energy
  routing but are still unobserved.

A rigorous analysis would require computing, for each
candidate compound mode, the Ma-compound cost vs.
S-separation cost — similar to R56's shell-structure
calculation but generalized to the full mode ladder.  This
is a SEPARATE derivation target, independent of Q125's
specific spin-gated principle.

## 9. Next steps if pursued

- Formalize in an R62 derivation track (tentatively derivation
  12) with explicit matrix-element calculation of α coupling
  under reducible vs irreducible spin states.
- Enumerate predicted dark modes in some range; compute their
  mass spectrum; compare to cosmological bounds on dark matter.
- Check whether the principle explicitly reproduces R46, R50,
  R53 filter behaviors as limits.

Until pursued, the principle is documented here as a
possibility.
