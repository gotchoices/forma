# R63 Track 9: Nuclear binding mechanism in Ma

Track 9 investigates where in the MaSt framework the nuclear
binding mechanism lives.  Phase 9a tested one specific candidate
(cross-shear dressing of additive-composition tuples) and
falsified it structurally.  Subsequent phases explore other
candidates that remain viable within Ma.

**The deuteron is the sharpest target.**  Under Phase 8a's
additive composition, the predicted deuteron mass is
1876.54 MeV (sum of proton + neutron).  The observed deuteron
is 1875.61 MeV — **2.2 MeV lighter than additive**.  Critically,
the daughter masses for β decay of the bound neutron
(2m_p + m_e) sum to 1877.6 MeV; for the deuteron to be stable
against β decay, **observed m(d) must be less than 1877.6 MeV,
which observation confirms and additive prediction barely
does**.  MaSt currently predicts m(d) ≈ 1877.8 MeV at additive
leading order, which would make the deuteron unstable against
β decay — contradicting observation.

Binding in Ma is therefore **structurally required**, not a
refinement.  The question is which Ma mechanism produces the
2.2 MeV gap for the deuteron (and proportional gaps for heavier
nuclei).

Phases adopted:

- **9a** — Cross-shear dressing hypothesis (EXECUTED).
  Falsified cleanly as a candidate, though the falsification
  is narrower than originally claimed.
- **9b** — Non-additive tuple search for the deuteron (NEXT).
  Does a lighter Ma tuple exist near the additive?
- **9c, 9d** — provisional numbers for mass-formula validity
  audit and Z₃ multi-baryon phase coherence.  Framed in the
  R63 README but not yet executed.

Script:
[`scripts/track9_phase9a_cross_shear_algebra.py`](scripts/track9_phase9a_cross_shear_algebra.py) ·
Output:
[`outputs/track9_phase9a_binding_scan.csv`](outputs/track9_phase9a_binding_scan.csv)

---

## Phase 9a — Cross-shear dressing and the binding question

**Hypothesis tested.**  Activating a cross-sheet σ coupling at
any position in the Ma-slice of the 11D metric — e.g., σ_ep
between e-tube and p-tube — produces a non-zero binding
`B = Σ E(nucleons) − E(compound)` for the additive nuclear
composition tuple adopted in Phase 8a.

**Method.**  At the g-candidate working parameter set, scan ten
distinct cross-shear placements (all e↔p pairs, all ν↔p pairs,
two e↔ν pairs) at σ ∈ {−1×10⁻⁵, −1×10⁻⁶, 0, +1×10⁻⁶, +1×10⁻⁵}.
At each, recompute the proton, neutron, ⁴He, and ⁵⁶Fe masses via
the full 11D metric, compute `Σ E(nucleons) − E(compound)` as the
predicted binding energy, and compare to observed.

### F9a.1. Falsification across all cross-shear placements

For **every** cross-shear placement and **every** σ magnitude
in the signature-preserving range, predicted binding stays at
the 10⁻⁴ MeV level:

| Observed binding | MaSt prediction (any σ, any placement) |
|:---|:---:|
| ⁴He B = 28.3 MeV | **+0.0001 MeV** |
| ⁵⁶Fe B = 492.3 MeV | **+0.002 MeV** |

The cross-shear changes the masses of individual particles — the
proton, the neutron, and the compound nucleus all shift together
— but the *difference* between `Σ E(nucleons)` and `E(compound)`
stays at numerical-noise level.

At `|σ| > ~10⁻⁵` the metric's signature breaks (two negative
eigenvalues instead of one), so cross-shear values larger than
that are disallowed by the framework.  Within the allowed range,
predicted binding is **five orders of magnitude too small**.

**Falsification:** linear cross-shear dressing of the additive
compound tuple does not produce nuclear binding.

### F9a.2. Algebraic origin of the cancellation

The first-order correction to `E²` from a cross-shear σ at
Ma-slice indices `(i, j)` is

<!-- ΔE²(n) = −σ · 2 · (ñ · G₀⁻¹[:, i]) · (ñ · G₀⁻¹[:, j]) -->
$$
\Delta E^2(n) \;=\; -\sigma \cdot 2 \cdot \bigl(\tilde{n}^\top G_0^{-1}[:,i]\bigr) \cdot \bigl(\tilde{n}^\top G_0^{-1}[:,j]\bigr)
$$

where `ñ = n/L` is the length-rescaled mode vector.  For a
block-diagonal baseline `G₀`, the two factors depend only on the
windings of the sheets containing indices i and j respectively.
Call them `α_e(n_e)` and `α_p(n_p)`.

For the additive compound tuple `T_c = Σ_k T_nucleon_k`, linearity
of dot-product gives

<!-- α_e(T_c) = Σ_k α_e(T_nuc_k);  α_p(T_c) = Σ_k α_p(T_nuc_k). -->
$$
\alpha_e(T_c) = \sum_k \alpha_e(T_{\text{nuc}_k}), \qquad
\alpha_p(T_c) = \sum_k \alpha_p(T_{\text{nuc}_k}).
$$

For nuclei, only neutrons have non-zero `α_e` (protons have
`n_et = 0`); all nucleons have equal `α_p` (both share
`(n_pt, n_pr) = (3, 6)`).  So for a nucleus of Z protons and
`(A−Z)` neutrons:

<!-- α_e(T_c) = (A−Z)·α_e_n;  α_p(T_c) = A·α_p_unit -->

- `α_e(T_c) = (A−Z) · α_e_n`
- `α_p(T_c) = A · α_p_unit`

Compound cross-correction:

<!-- ΔE²_c = -2σ · (A-Z)·α_e_n · A·α_p_unit = -2σ·A(A-Z)·α_e_n·α_p_unit -->
$$
\Delta E^2_c \;=\; -2\sigma\,A(A-Z)\,\alpha_e^{(n)}\,\alpha_p^{(\text{unit})}
$$

Separated-nucleons cross-correction (sum over nucleons):

<!-- ΔE²_sep_sum = -2σ · (A-Z) · α_e_n · α_p_unit -->

(each neutron gets its own `-2σ · α_e_n · α_p_unit`; protons
contribute 0 because their `α_e = 0`).  Compound is A times the
separated sum.

**But** the zeroth-order compound energy is also A times the
per-nucleon mass at leading order: `E_c⁰ ≈ A · m_p`.  When we
convert E² correction to E correction via
`ΔE ≈ ΔE²/(2E)`:

<!-- ΔE_c = ΔE²_c / (2·E_c⁰) = σ·(A-Z)·α·α / m_p -->
<!-- ΔE_sep = Σ ΔE_k = (A-Z)·σ·α·α/m_p -->

$$
\Delta E_c \;=\; \frac{-2\sigma\,A(A-Z)\,\alpha\alpha}{2\,A\,m_p}
\;=\; \frac{-\sigma\,(A-Z)\,\alpha\alpha}{m_p}, \qquad
\Delta E_{\text{sep}} \;=\; \frac{-\sigma\,(A-Z)\,\alpha\alpha}{m_p}.
$$

**The A factors cancel exactly.**  To first order in σ, the
compound's correction equals the separated sum's correction,
and the binding difference is zero.

Numerically, higher-order terms across the signature-preserving
σ range don't break the cancellation either: the structural
identity between `T_c` and the nucleon sum holds through the
quadratic form at every order tested.

### F9a.3. Scope of the falsification

The cancellation holds given two assumptions that are specific
to what Phase 9a tested, and are not theorems of the framework:

1. **Additive composition is the correct compound tuple.**
   Phase 8a adopted additivity as the modeling choice for
   composite nuclei; it was not derived.  The cancellation
   proof rests on `T_c = Σ T_nucleon`.  If bound nuclei
   correspond to a different Ma-mode, the cancellation's
   starting premise fails.
2. **Linearity of the perturbation.**  Cross-shear dressing
   adds a rank-1 symmetric entry to G.  Mechanisms that modify
   mass via non-linear coupling, validity-range corrections
   to the mass formula, or Z₃ multi-strand phase coherence
   are not of this form.

The falsification is therefore precise: **linear cross-shear
dressing of additive-composition tuples does not produce
binding**.  It is NOT a falsification of "binding in Ma"
generally.  The framework retains candidate mechanisms that
escape one or both assumptions.

### F9a.4. What remains viable for nuclear binding

Three Ma-internal candidates remain after 9a's narrow
falsification.  All are within R63 scope; none requires
leaving the Ma domain:

**Option A (→ Phase 9b) — Non-additive bound tuple.**  The
bound nucleus is a different Ma-mode from the winding sum of
its constituents.  A brute-force search of Ma tuples at fixed
(A, Z) for mass below the additive prediction identifies
alternative representations.  If found, that lighter tuple is
the bound state and the additive tuple is the "reference"
separated configuration.  Additive was adopted in T8 as a
modeling choice, not derived — revisiting it is a conservative
refinement.

**Option B (→ Phase 9c) — Mass-formula validity at high
n_pt.**  Derivations 3/4 construct the mass formula
`E = √(ñ · G⁻¹ · ñ)` in a low-winding KK regime.  At nucleus-
scale windings (n_pt up to ±168 for ⁵⁶Fe), corrections to the
approximation can kick in.  Auditing the derivations' validity
ranges and computing the leading corrections is a direct test:
if high-n corrections have the right sign and magnitude, they
produce binding without further posits.

**Option C (→ Phase 9d) — Z₃ multi-strand phase coherence.**
Under Q132 v2, the (3A, 6A) p-sheet tuple is 3A primitive
strands.  The framework currently treats 3A strands as A
independent Z₃ triplets — giving additivity.  But Z₃ itself
has representation-theoretic structure for k = 3A > 3 strand
groupings: different singlet channels could have different
effective ring-direction coherence energies.  A specific
ansatz for how Z₃ phase coherence enters the mass formula
would give a concrete test.

**Out of scope**: S-space configuration energy (Track 8 FR-4
second bullet) remains the framework-extension candidate for
*if* all of A, B, C fail.  R63's job is to determine whether
binding lives in Ma or requires S-space machinery.

### F9a.5. What Phase 9a establishes

1. **Linear cross-shear dressing is not the nuclear binding
   mechanism for additive-composition tuples.**  The structural
   cancellation identified in F9a.2 rules this out.
2. **The result is narrower than "binding requires framework
   extension."**  Three Ma-internal candidates remain viable
   (F9a.4); each avoids one or both of the cancellation's
   premises.
3. **Phase 9b is next** — a non-additive tuple search for the
   deuteron as the sharpest test.  If bound-state tuples lighter
   than additive exist within the g-candidate lattice, the
   additive rule was the wrong compound-mode representation
   and binding is in Ma.

---

## Phase 9b — Non-additive tuple search for the deuteron

**Hypothesis (Path A of F9a.4).**  The bound deuteron is a Ma
tuple *other than* the additive `(1, 2, −1, −1, 6, 12)` sum of
proton and neutron tuples.  If a lighter v2-compatible tuple
exists at (A=2, Z=1), that lighter tuple is the bound state and
the additive tuple is the "reference" separated configuration;
the mass difference is the binding energy.

**Sharp target.**  Observed m(d) = 1875.61 MeV.  Additive tuple
gives m = 1876.54 MeV.  Gap = 2.2 MeV to close (observed is
lighter by 0.93 MeV and observed binding is 2.22 MeV relative
to m_p + m_n).

Script:
[`scripts/track9_phase9b_deuteron_search.py`](scripts/track9_phase9b_deuteron_search.py) ·
Output:
[`outputs/track9_phase9b_deuteron_candidates.csv`](outputs/track9_phase9b_deuteron_candidates.csv)

### F9b.1. Lighter tuples exist — but at structurally different windings

The raw search envelope (Δ=3 on e and ν, Δ=3 on n_pt Z₃-stepped,
Δ=6 on n_pr) scanned 93,639 candidate tuples.  Results:

| Candidates within ±2% of observed | 4606 |
| Candidates LIGHTER than additive (1876.54 MeV) | 1617 |
| Candidates within 0.5 MeV of observed (1875.61 MeV) | 147 |
| Closest match | `(0, 0, −4, −4, 3, 15)` at **1875.70 MeV** (+0.10 MeV from observed) |

The best-matching tuple sits within 0.1 MeV of the observed
deuteron mass — better than any naïvely-additive prediction.

### F9b.2. But the candidates aren't deuterons

The best candidate `(0, 0, −4, −4, 3, 15)` has `n_pt = 3`, not
6.  Under Q132 v2, p-sheet gcd = 3 with primitive (1, 5) means
**one Z₃-bound baryon** (3 strands = 1 triplet), not two.  A
single baryon at 1875 MeV is some exotic excited state — perhaps
analogous to a D⁺ meson (1870 MeV, charged, similar mass) —
**not a deuteron**.

Every top candidate in the search has the same issue: `n_pt = 3`
(1 baryon) or other structures that don't represent two bound
nucleons.  The search finds "other charged particles at ~1875
MeV" rather than "the deuteron bound state."

### F9b.3. With the baryon-count filter, no improvement over additive

Imposing the correct structural constraint — **n_pt = 6** (2 Z₃
triplets = 2 baryons) — and letting the other windings vary by
±2 around the additive tuple:

| Constraint | Lighter than additive? |
|:---|:---:|
| `n_pt=6, n_pr=12` (canonical "2 nucleons" p-sheet), vary e and ν by ±2 | **0 lighter tuples** |
| `n_pt=6, n_pr ∈ [10, 14]` (allow small p-sheet ring variation) | 1200 lighter, but all at 1725–1805 MeV (70–150 MeV below observed) |

When the p-sheet structure is pinned to the canonical "2 nucleons
= 2 Z₃ triplets of primitive (1, 2)" form, **the additive tuple
is locally optimal**.  Nothing in the e/ν-sheet variations
improves on it.

Allowing the p-sheet ring winding to vary finds lighter tuples,
but they have **masses 70–150 MeV below observed** — not
deuteron candidates, but single-baryon or mesonic states at
different energies.

### F9b.4. Path A falsified for the deuteron under structural constraints

The cleanest reading:

- If the deuteron's Ma representation must contain 2 Z₃ baryon
  triplets with primitive (1, 2) windings (matching additive's
  structural interpretation of "2 nucleons"), **no tuple lighter
  than additive exists**.
- If the structural constraint is relaxed, lighter tuples exist
  but they don't represent deuterons — they represent different
  particles at similar masses.

Path A is therefore falsified for the deuteron at the honest
structural level.  There is no "non-additive deuteron tuple" in
the g-candidate lattice; the additive tuple is the g-candidate's
representation of the deuteron, and its 0.9 MeV overshoot vs.
observed is not curable by a different tuple choice.

### F9b.5. What Phase 9b establishes

1. **Lighter v2-compatible tuples exist near the deuteron mass**
   (1617 of them within ±2% of observed), but they represent
   other particles — single baryons or charmed-meson-like
   states — not bound nucleon pairs.
2. **Under the natural baryon-count constraint (n_pt = 6 for a
   2-nucleon compound), no lighter tuple exists in the local
   envelope of the additive.**  Additive is structurally
   optimal within its baryon class.
3. **Path A (non-additive bound tuples) is falsified for the
   deuteron at structural precision.**  Nuclear binding does
   not live in "different tuples at the same mass"; it must
   live in a different mechanism.
4. The remaining Ma-internal candidates are Path B (mass-formula
   validity at high n_pt) and Path C (Z₃ multi-strand phase
   coherence).  **Phase 9c (Path B) runs next**: audit the
   derivations of the mass formula for corrections at compound-
   scale windings.

---

## Status

**Phases 9a and 9b complete.**
- 9a: linear cross-shear dressing falsified (structural
  cancellation under additivity).
- 9b: non-additive deuteron tuple search falsified under the
  baryon-count structural filter.  Additive is locally optimal
  for its structural class.

Two Ma-internal candidates remain for the binding mechanism:
Path B (mass-formula validity at high n_pt) and Path C (Z₃
multi-strand phase coherence).  **Phase 9c runs next.**  If
both 9c and 9d fail, the conclusion that binding requires
framework extension is earned.
