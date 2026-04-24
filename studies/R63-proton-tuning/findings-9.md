# R63 Track 9: Nuclear binding from Ma-state energy minimization

Track 9 tests the hypothesis that nuclear binding energy — the
energy difference between a bound compound nucleus and its
separated constituent nucleons — can be produced by turning on
previously-unactivated cross-sheet σ couplings in the 11D MaSt
metric.  **Phase 9a reports a clean falsification.**

The result is structural, not parametric: the falsification
stems from the algebra of how the additive-composition tuple
relates to its nucleon constituents, and it holds across every
cross-shear placement at every magnitude tested.

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

### F9a.3. Why this is a structural result, not a bug

The cancellation isn't an artifact of a specific cross-shear or
of the approximation `ΔE ≈ ΔE²/(2E)`.  It comes from the
interplay of two deeply-built-in features of the framework:

1. **Additive composition** (Phase 8a): the compound nucleus
   tuple is the winding sum of its nucleons.  The corresponding
   Ma-winding vectors add linearly.
2. **Linear metric perturbation**: cross-shear dressing is a
   rank-1 perturbation of G₀.  The first-order correction to
   any quadratic form of the windings is bilinear in the
   windings, and its effect on the energy eigenvalue is linear
   after the mass-extraction normalization.

Linearity in both places means the compound result equals the
sum of nucleon results identically.  Any mechanism that breaks
the cancellation must break **one** of these two structural
properties.  Cross-shear dressing alone breaks neither.

### F9a.4. What remains viable for nuclear binding

Four options survive after Phase 9a's falsification.  None is
implementable inside the original Track 9 scope ("cross-shear
dressing at fixed parameters"); each is a framework-extension
candidate for a successor study:

**Option A — Non-additive compound tuple.**  The bound nucleus
is a different Ma-mode from the winding sum of its constituent
nucleons.  The "right" tuple has different windings that give
lower mass.  This was the original Track 8 direction, withdrawn
at the user's request.  Reactivating it requires comparing
bound-state tuples to additive tuples and interpreting the
difference as "nucleons rearrange when close in S."  It's a
conservative extension — keeps the metric, changes the tuple
assignment.

**Option B — S-space configuration energy.**  The cost of
placing two nucleons at nearby S-locations isn't zero; MaSt
currently doesn't model it.  Binding = 4D projection of an
S-space interaction that hasn't been added to the framework.
Track 8 FR-4 second bullet.  Most physically motivated but
requires new machinery for handling S-space.

**Option C — Non-linear mass formula.**  Currently
`E = √(ñ · G⁻¹ · ñ)`.  The sqrt structure is what makes
`E(compound) ≈ Σ E(nucleons)` hold at σ = 0.  A modified mass
formula that's non-trivially non-quadratic in ñ could break
additivity and produce binding.  Speculative; no current basis
in the framework.

**Option D — Dynamical L_ring.**  If ring circumferences shift
with compound-mode density (e.g., `L_ring_p` smaller for
high-`n_pt` tuples), the compound gets a different effective
scale than its constituents.  No current basis in the framework
either.

### F9a.5. What Phase 9a establishes

1. **Cross-shear dressing is not the nuclear binding mechanism
   in MaSt.**  The falsification is clean and structural.
2. **The falsification generalizes.**  Any rank-1 or multi-
   rank linear perturbation of the Ma metric will exhibit the
   same cancellation, because the cancellation comes from the
   additivity of the compound tuple, not from the specific σ
   values.
3. **Phase 9b, 9c, 9d do not run.**  Without cross-shear
   dressing producing binding, there is nothing to fit the
   chart-wide B(A,Z) curve against; the BW decomposition and
   magic-number scans are moot.
4. **The residual ~0.87% binding gap at ⁵⁶Fe is still the
   target**, but a framework extension is now the path to it,
   not an in-g-candidate parameter sweep.

### F9a.6. Implications for R63 and for model-G

Track 9 is closed.  Its outcome sharpens the picture without
improving the g-candidate itself: we now know explicitly that
nuclear binding in MaSt needs framework extension and cannot be
produced by parameter activation alone.

The four remaining options (A–D above) are all genuinely
outside R63's scope — model-G, as a refinement of model-F's
metric + v2 rule set, does not address nuclear binding.  A
**model-H** or a **successor study** targeting binding physics
(with S-space machinery, non-additive tuple interpretations, or
one of the other options) would be the natural future direction.

This is not a failure of R63; it's a clean determination of
R63's boundary.  The g-candidate is a principled refinement of
model-F on discipline (Q132 v2), inventory (Track 6), and
nuclear mass composition (Track 8).  Nuclear binding as an
emergent mechanism is a separate program.

---

## Status — Track 9 closed with structural falsification

**Phase 9a complete.**  Linear cross-shear dressing of the
additive compound tuple does not produce nuclear binding at any
placement or magnitude in the signature-preserving range.  The
cancellation is structural, from additivity + linear
perturbation.

**Phases 9b, 9c, 9d do not run** — there is nothing for them to
fit.

**Four framework-extension options** (non-additive tuples, S-space
machinery, non-linear mass formula, dynamical L_ring) remain
viable for the binding mechanism but all fall outside R63's
refinement scope.  Each is a candidate for successor study.

**R63 closes** with Tracks 1–9 complete, the g-candidate
refined as documented in findings-1 … findings-8, and nuclear
binding identified as a boundary of the framework rather than a
parameter-fit problem.
