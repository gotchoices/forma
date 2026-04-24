# R63 Review — Tracks 1–8 and proposed next track

## The arc, one line per track

1. **T1 — Proton-sheet ghost audit at baseline.**  Applied R60 T16
   Z₃ discipline to the p-sheet; baseline came up clean — no
   light ghosts at `(ε_p, s_p) = (0.55, 0.162)`.
2. **T2 — Viable-region grid.**  Swept `(ε_p, s_p)`; confirmed
   the analytical ghost-free bound `μ(3, 6) ≤ 8.09` held across
   88% of the grid.
3. **T3 — Fitness heat map (Phase A flat / Phase B width-weighted).**
   Phase B's natural-line-width thresholds relocated the peak to
   `(0.80, 0.05)` with fitness 4.95/7 and a near-exact π⁰ match
   (0.038%).
4. **T4 — E-sheet ghost audit.**  Exposed a multi-event tower
   (`|n_et| = 2, 3, 4, …`) and the `(0, −1)` 104-MeV ghost that
   the strict R33 rule forbade.
5. **T5 — E-sheet under Q132 v2.**  Re-render after the
   promotion-chain rule was refined to bright/dark via gcd + ω-sum:
   0 ghosts across 2296 grid points, R53 Solution D confirmed as
   near-peak on a wide `ε_e` ridge.
6. **T6 — Q132 v2 compound-mode audit.**  14 of 19 baseline tuples
   pass v2 charge arithmetic unchanged; 5 (τ, Λ, Σ⁻, Ξ⁻, Ξ⁰)
   find v2-compatible replacements at comparable mass accuracy.
   Marginal ratio scans confirm model-F baseline as the joint
   inventory optimum; ν-sheet is passive for hadronic fit.
7. **T7 — Compound-mode vs. spatial separation, H→Pb.**  Walked
   the compound-mode miss-vs-binding curve up the stable chain;
   miss scales with binding and the compound mode remains the
   cheapest configuration through Fe, with a crossover against
   the separated-nucleons cost estimate in the heavy-A regime.
8. **T8 — Decay-conservation audit + additive-composition refinement.**
   β-decay identity pinned the neutron tuple to `(1, 2, −1, −1,
   3, 6)`; adopting it plus additive nuclear composition
   (`Z·p + (A−Z)·n`) improved 20 of 22 nuclei by a mean of
   0.37 pp.  Decay audit across 19 hadron decays: charge
   conserves universally under the ingredient-sum rule; winding
   conserves for β decay and has structured, meaningful
   residuals elsewhere (chiral anomaly, strong/weak hadronic,
   flavor-changing leptonic).  The residual nuclear miss (~0.87%
   at ⁵⁶Fe ≈ 453 MeV) is now a clean numerical target for the
   binding mechanism: observed B(⁵⁶Fe) = 492 MeV.

**Net at Track 8 close.**  R63 has delivered a refined rule set
(Q132 v2 + ingredient-sum composite charge + additive nuclear
composition + β-decay-consistent neutron), a clean inventory
mass match, and a sharp residual that *is* the nuclear binding
energy.  The next track's job is to close that residual from
first principles.

---

## Proposed Track 9 — Nuclear binding from Ma-state energy minimization

**Hypothesis** (carried forward from the Track 8 wrap-up
discussion): *Forces in S result from lowest-energy states in
Ma.*  Nuclear binding is the 4D projection of a Ma-domain cost
function: nuclei exist as stable configurations when the
compound-mode Ma energy is lower than the spatially-separated
nucleon configuration, and the difference — currently showing up
as T7+T8's ~0.87% residual at Fe — is the binding energy.

### What this track can accomplish

- **Derive nuclear binding from MaSt rather than insert it.**
  T8's additive residual is the right quantity to explain; the
  task is to find the Ma mechanism that produces it.
- **Pin the previously unconstrained cross-sheet σ parameters.**
  `σ_ep, σ_eν, σ_νp` have been pool item **h** since R60 T7.
  Nuclear binding gives ~250 mass data points against a small
  number of cross-shear parameters — a massive constraint
  upgrade over the particle inventory alone.
- **Convert BW-like phenomenology into structural MaSt
  statements.**  Each Bethe-Weizsäcker term (volume, surface,
  Coulomb, asymmetry, pairing) should map to a specific Ma
  feature if the hypothesis is right; mapping them is the
  substantive test.
- **Explain saturation and range.**  If the binding-per-nucleon
  plateau above Fe comes from cross-shears that decay in
  "compound-mode distance," the decay length is the
  compactification scale; extracting it and comparing to
  `L_p` is a clean independent check of the hypothesis.

### How to do it

**Phase 9a — Compound vs. separated energy under cross-shear
dressing.**  Write `E_Ma(compound)` and `E_Ma(separated)` for a
single (A, Z) including the derivation-10 F31 iterated
Schur-complement corrections.  At leading order
`μ(3A, 6A) = 3A · μ(1, 2)` gives zero binding (µ is linear in k);
binding has to live in the cross-shear dressing.  Single nucleus,
algebra only — establish that the difference can be nonzero and
identify which σ entries enter.

**Phase 9b — Binding curve across the chart, H → Pb.**  Evaluate
`E_Ma(compound) − Σ E_Ma(nucleon)` for the Track 7/Track 8
isotope chain under cross-shear dressing.  Plot against observed
`B(A, Z)`; if the shapes match with reasonable cross-shear
magnitudes, the hypothesis closes.  If they differ, the
deviation pattern says which BW term isn't captured and points
at what needs extending.

**Phase 9c — Decompose the match into BW-like terms.**  Fit the
MaSt prediction to the five-term Bethe-Weizsäcker decomposition.
Each term's cross-shear origin is recorded.  Cross-shears that
were unconstrained by R60 get specific numerical values pinned
by the binding curve, with residuals reported.

**Phase 9d (optional) — Magic numbers as Ma-cost-function
minima.**  Scan the tuple lattice for (A, Z)-tuples where the
cross-shear-dressed compound energy has a local minimum.  Check
whether the minima align with 2, 8, 20, 28, 50, 82, 126.  If
yes — a major positive result (magic numbers from first
principles).  If no — shell closure is orthogonal to Ma's
binding mechanism and belongs in a separate track.

### What to watch for

- **Don't over-fit.**  With five BW terms and multiple
  cross-shear parameters a match is almost guaranteed.  The test
  is whether each cross-shear gets a separately constrained
  value and still reproduces the full curve.  Compute the
  cross-shear from two or three nuclei; check it against the
  other ~247.
- **Coulomb is not a new prediction.**  `Z²α/R` is standard; it
  should fall out of e-sheet/p-sheet charge-and-radius structure
  but is not where the hypothesis is tested.  The asymmetry and
  pairing terms are the most informative — they couple N vs. Z
  and even/odd structure, respectively, and should pin specific
  Ma features.
- **Range ≈ saturation ≈ L_p.**  If the fit's exponential decay
  length in compound-mode distance matches the independently
  known p-sheet compact radius, that's independent confirmation.
  If the two values disagree materially, the hypothesis or the
  geometry needs adjustment.
- **T8 flagged `σ_ep` explicitly.**  FR-4 of Track 8's
  closeout suggested cross-sheet σ_ep as the candidate
  mechanism for the neutron p-n mass deficit (−1.3 MeV) and by
  extension the nuclear binding residual.  Track 9 should carry
  σ_ep as the first cross-shear to fit — it's structurally
  motivated and numerically consequential.

### Reusable assets

- Track 7's infrastructure for walking (A, Z) across the isotope
  chain.
- Track 8's additive-composition tuples and ingredient-sum
  charge rule — the correct composite representation for nuclei.
- Derivation-10's F30/F31 Schur-complement machinery — the
  vehicle for propagating cross-shear corrections into the
  compound mass formula.
- The binding-curve residual at ⁵⁶Fe (453 MeV predicted vs. 492
  MeV observed) as the sharp numerical benchmark.

### Scope boundaries

Track 9 is about **nuclear binding in model-F / Q132 v2 / T8's
refined framework**.  It does **not** re-open Q132 v2, does not
touch particle inventory tuples beyond nuclei, and does not
attempt the PMNS bookkeeping (T8 FR-2) or the chiral-anomaly
mechanism (T8 FR-3).  Those are separate tracks or successor
studies.  If Track 9 requires framework extension (e.g., S-space
overlap of T8 FR-4 second bullet), that's a finding, not a
default.

---

## Post-9a review: the falsification is narrower than advertised

### What 9a actually tested

Phase 9a ran cleanly and its algebra is correct.  It computed
`B = Σ E(nucleons) − E(compound)` under ten cross-shear
placements at five magnitudes each, and found `B ~ 10⁻⁴ MeV`
everywhere in the signature-preserving range.  The algebraic
cancellation is identified correctly at F9a.2: to first order
in σ, `ΔE_compound = ΔE_separated` because the A factor in the
compound's correction cancels against the A factor in the
compound's zeroth-order mass.

### What 9a did **not** test

The cancellation proof rests on three premises, *all of which
are assumptions of the specific test, not theorems of the
framework*:

1. **Linearity of the perturbation.**  `ΔE² = −σ · (bilinear in
   windings)`.  Valid for a rank-1 metric perturbation, but
   binding mechanisms that are bilinear in the tuple don't have
   to be rank-1 metric perturbations.
2. **Additive composition is the correct compound tuple.**
   T8's additive rule sets the nucleus tuple to `Z·p + (A−Z)·n`.
   9a's cancellation is specifically a theorem *about the
   additive tuple*.  If bound nuclei correspond to a different
   Ma-mode than the winding sum, the cancellation's premise
   fails at the outset.
3. **All nucleons carry identical p-sheet windings at leading
   order.**  9a's algebra uses `α_p(T_c) = A · α_p_unit`
   because every nucleon shares `(n_pt, n_pr) = (3, 6)`.  Any
   Z₃-compatible structure that differentiates protons from
   neutrons on the p-sheet — or that assigns multi-baryon
   compounds non-trivial p-sheet internal structure —
   invalidates this step.

The falsification F9a.1 is therefore precise:
*linear cross-shear dressing of additive-composition tuples
does not produce binding*.  It is **not** a falsification of
"binding in Ma" generally.  F9a.3's "two deeply-built-in
features of the framework" characterization overstates the
situation — feature (1) (additive composition) was adopted in
T8 as a modeling choice, not derived; feature (2) (linear
perturbation) is the choice to test cross-shears rather than
other mechanisms.  Both are legitimate targets for refinement
without leaving the Ma domain.

### Where binding can still live in Ma — three unexplored paths

**Path A: Z₃ representation structure for multi-baryon tuples.**
Under T8 additive composition, a nucleus of A nucleons is
`(3A, 6A)` on the p-sheet — gcd = 3A with primitive `(1, 2)`.
Q132 v2 reads this as 3A copies of the primitive.  **The
framework currently treats 3A copies as A independent Z₃
triplets**, because the binding factor `β_p(3A) = 1` and the
mass is `3A · K_p · μ(1,2)` identically.  That's the
additivity that F9a.2 exploits.

But Z₃ itself — the cyclic group of order 3 — has
representation-theoretic structure for k-fold tensor products
of the strand rep.  For k = 3 there is one way to form a
singlet (the three strands at phases 0, 2π/3, 4π/3).  For
k = 6 there are *three* distinct ways (three assignments of
six strands to two triplets).  For k = 9, ten.  If different
singlet channels have different Ma-level coherence energies,
then **the k = 3A Z₃-singlet isn't energetically equivalent
to A independent k = 3 singlets**, and the mass isn't
strictly `A · K_p · μ(1, 2)`.  The difference is structural
Z₃ content, entirely within the p-sheet.

Operationally this is pure group theory plus a phase-energy
accounting rule: how do the 3A strands' Z₃ phases arrange
themselves, and does a coherent arrangement have lower
effective ring-direction energy than 2A/3 independent triplets
would?  **Not tested in Track 9a.**

**Path B: The √-quadratic mass formula's validity range at
high n_pt.**  Derivations 3, 4 (the mass formulas) are
constructed in the low-winding limit where KK is well-behaved.
At n_pt = 168 (⁵⁶Fe), the compound winding is well outside
the regime where the derivations' approximations were
checked.  If the mass formula's actual form has
higher-than-quadratic corrections that kick in at large
windings, the additivity of μ(kn_t, kn_r) = k·μ(n_t, n_r)
breaks down and compound mass deviates from the linear sum.
**Not tested in Track 9a.**

**Path C: Non-additive bound tuples (Option A in F9a.4).**
The additive rule was adopted in T8 explicitly as a modeling
choice and is acknowledged there as not fully derived.
Bound-state nuclei might not be additive sums.  A brute-force
search of Ma tuples at fixed (A, Z) with lower mass than the
additive tuple would identify alternative representations.
If some observed nuclear (A, Z) has a Ma tuple *other than*
`Z·p + (A−Z)·n` at lower mass, that lower-mass tuple IS the
bound state and the additive tuple is the "reference"
separated configuration.  F9a.4 classifies this as a
framework extension outside R63; I think it belongs
inside R63.

### Why bound-neutron stability forces an Ma-level mechanism

A sharper empirical test than the binding curve: the
deuteron is stable, but the free neutron decays in 15
minutes.

Under T8's additive composition, m(deuteron) = m_p + m_n ≈
1877.8 MeV (by construction; additive at leading order).
For bound-n β-decay d → 2p + e + ν̄ to be forbidden, the
final rest-mass sum 2 m_p + m_e ≈ 1877.6 MeV must exceed
m(deuteron).  But T8's additive prediction gives 1877.8 >
1877.6, so **MaSt at this level incorrectly predicts the
deuteron is unstable**.

The observed deuteron mass 1875.6 MeV is 2.2 MeV lower than
the additive sum — that 2.2 MeV is the deuteron binding, and
without it, MaSt fails a discrete observable (deuteron
stability) not just a quantitative fit.

This means: **a binding mechanism in Ma is structurally
required by MaSt, not optional**.  Without one, MaSt
predicts most nuclei should β-decay promptly, contradicting
observation.  Track 9's question is not "can we improve
accuracy"; it's "what Ma mechanism keeps bound neutrons
stable?"  That's a sharp target and fully within Ma — no
S-space machinery is required to pose or test it.

### The user's Z₃-phase-overlap question, made precise

When two protons' worth of p-sheet windings overlap into
`(6, 12)`, does the structure change beyond "two independent
`(3, 6)` triplets"?

Yes, in principle.  A k = 6 p-sheet mode has six primitive
strands.  Z₃ singlet formation in a 6-strand system is not
unique: the six strands can be partitioned into two Z₃
triplets in three distinct ways (which two strands get phase
0, which get 2π/3, which get 4π/3), and the "phase-coherent"
singlet-of-singlets configuration is just one such
arrangement.  Whether these arrangements have different
ring-direction energy contributions depends on how the
Z₃ phases couple into the p-sheet's ring winding — which is
**exactly what the ω-sum construction of Q132 v2 is
bookkeeping for single modes, but hasn't been extended to
multi-baryon tuples**.

If the lowest-energy k = 6 configuration has ring-direction
coherence lower than two independent k = 3 triplets (the
ω-phases interfering constructively), *that* difference is
nuclear binding in Ma — produced by the same phase-lock
machinery Q132 v2 already uses at the single-baryon level,
just extended to Z₃ multi-copy groupings.

### The "why is bound-n stable" question, sharpened

In Ma, a free neutron with tuple `(1, 2, −1, −1, 3, 6)` β-decays
because its tuple can be decomposed as `p_tuple + e_tuple +
ν̄_tuple` and the decomposition is energetically allowed (F8b.1
showed decays conserve winding under the ingredient-sum rule,
and this one has positive Q-value in observation).

In a nucleus, the neutron's p-sheet windings `(3, 6)` are part
of a larger p-sheet compound `(3A, 6A)`.  For β decay of the
bound neutron to be forbidden, **decomposing the nuclear
compound tuple by removing one neutron's worth has to produce
a configuration with higher total energy than the parent
nucleus**.  Under T8 additive composition at leading order,
this is a wash (the `(3A, 6A)` primitive energy is 3A times
μ(1,2), and removing 3 strands gives `(3(A-1), 6(A-1))` at
3(A-1) times μ(1,2), exactly 3 μ(1,2) less — which is one
proton's worth, not "one proton + binding difference").

So the SAME cancellation that F9a.2 exposes for cross-shears
shows up here: under additive composition, bound-neutron β-
decay's Q-value equals free-neutron β-decay's Q-value.
Nothing differentiates them.

This is the same issue from a different angle: if MaSt's
compound-mode energy is strictly additive, then not only
does binding vanish, but *the very distinction between bound
and free becomes invisible in Ma*.  The framework needs a
mechanism — within Ma — that makes `(3A, 6A)` not exactly
equal to A copies of `(3, 6)`.  The Z₃ phase structure of
Path A above is the most economical candidate.

## My case for what the strong force is in Ma

Layered, and partly established, partly yet to extract:

**Layer 1 — Quark confinement (done).**  R60 T16's Z₃ selection
rule forces `n_pt ≡ 0 (mod 3)`; no free single `(1, 2)` strand
on the p-sheet.  This is quark confinement.  Fully in Ma.

**Layer 2 — Baryon formation (done, partly).**  Q132 v2 + T6
identify the proton as a k = 3 Z₃-singlet of primitive
`(1, 2)` strands.  Composite charge +e, mass 3·K_p·μ(1,2).
The three strands' Z₃ phase coherence is the baryon's
internal structure.  Fully in Ma.

**Layer 3 — Nucleon-nucleon binding (hypothesized, not yet
extracted).**  When multiple baryons share a compound p-sheet
tuple `(3A, 6A)`, the Z₃-phase arrangement of the 3A strands
can in principle have a lower-energy configuration than A
independent k = 3 triplets.  The energy difference is nuclear
binding.  **This is the Z₃-phase-overlap mechanism the user's
question points at**, and it's a natural extension of the
phase-lock machinery already carrying Q132 v2.  Not yet
tested; Track 9a's linear cross-shear test was a different
mechanism.

**Layer 4 — Range / saturation / BW shapes (mostly S-space).**
The spatial pattern of where nucleons sit, the short range of
the force, the A^(2/3) surface term — these are S-space
features that MaSt inherits from standard QM.  Outside the
strong-force-in-Ma question.

The net claim: *the strong force in Ma is Z₃ phase coherence
across 3A p-sheet strands.*  At k = 3 it's baryon formation
(R60 T16 / Q132 v2).  At k = 3A it's multi-baryon binding.
Track 9a correctly falsified a different mechanism (linear
cross-shear on additive tuples).  Track 9 as a whole is not
falsified.

## What remains to check (paths open for R63)

### P1. Z₃ representation theory for multi-baryon tuples

Pure group theory, no new framework.  For k = 3A, enumerate
the distinct Z₃-singlet channels and compute their effective
ring-direction phase-sum contributions.  If distinct channels
have distinct mass contributions, the lowest is the bound-
state mass; the difference between the lowest and the
"A-independent-triplet" configuration is nuclear binding.

Deliverable: a mass formula for `(3A, 6A)` as a function of A
that is **not** exactly `A · m_p`, parameter-free.  Testable
immediately against the T8 additive-composition residual.

### P2. Deuteron stability as diagnostic

Compute m(deuteron) under the P1 construction.  Compare to
observed 1875.61 MeV.  Observed − additive = 2.2 MeV; this is
the minimum binding Ma needs to supply.  Sharp numerical
target, one number.  If P1 gives close to 2.2 MeV, nuclear
binding is in fact Z₃-phase overlap.  If P1 gives essentially
zero, Path A is also falsified and the next candidate is
Path B (mass-formula validity range).

### P3. Validity range of the √-quadratic mass formula

Derivations 3/4 assume the KK low-winding regime.  At n_pt =
168 (⁵⁶Fe), corrections could matter.  Audit the derivations
for the range of validity statements; if corrections appear
at high n, they may supply binding.

### P4. Non-additive tuple search at fixed (A, Z)

Brute-force scan of Ma tuples at (A, Z) with the constraints
Z · Q_p + (A − Z) · Q_n = Q_observed (ingredient sum) and
mass within width-weighted tolerance.  If the search finds a
tuple lighter than the additive composition, that lighter
tuple is the bound state.

### Closing comment

Track 9 should not be marked closed, nor should R63 be closed.
9a did what it did cleanly; 9b (as originally framed) is
correctly mooted by 9a's cancellation; but the follow-up
phases **P1–P4 above are within R63 scope** and should run
before Track 9 is declared closed.  R63's net claim would
then be: "model-F refined to Q132 v2 + T8 additive
composition + T9 Z₃-phase nuclear binding" — which is a
stronger model than model-F on all three axes, not just two.

If P1 succeeds, Track 9 completes as a positive result.
If P1–P4 all fail, *then* the "binding requires framework
extension" conclusion in findings-9.md is earned.  The
current F9a findings are not enough to earn it.

---

## After Phase 9b

**What 9b settled.**  The ~94K-tuple search found no lighter
v2-compatible tuple for the deuteron at structural precision
(n_pt = 6 for the 2-baryon count).  Path A — "the deuteron is
a different Ma tuple than the additive sum" — is falsified for
the deuteron.  P4 in my earlier list is closed.

**What 9b did NOT settle.**  9b is a tuple search; it cannot
see internal phase structure.  The current mass formula reads
`(6, 12)` via `μ(6, 12) = 2·μ(3, 6)` by linearity, identical
whether the six strands are arranged as two Z₃ triplets or as
one Z₆ hexagon.  **Path C (phase coherence) is not a tuple
question and is untouched by 9b's result.**

### Does the neutrino sheet add a new direction?

Probably not productive:

1. **ν-sheet is structurally passive.**  R60 T18 zeroes ν-sheet
   charge; F9a's cross-shear test showed ν-sheet cross-terms
   don't break the compound-vs-separated cancellation; T6 Phase
   6c found ν-sheet variations don't move inventory fitness.
2. **More ν winding ⇒ higher mass.**  Additional ν content
   contributes a kinetic-like term to the quadratic form.
   Binding needs to *lower* mass, so ν extensions push the
   wrong way at leading order.
3. **9b already tested ν variations.**  The raw search scanned
   ν by Δ = 3; the n_pt = 6 constrained search by Δ = 2.  No
   lighter tuple surfaced from ν variation alone.

The Majorana question (is ν = ν̄?) is real but orthogonal — it
changes the independent-mode count on the ν-sheet, not the
sheet's mass contribution.  It doesn't create binding.

### Recommended order

1. **Phase 9c (mass-formula validity at high n_pt).**  Already
   announced; runs next per findings-9.  Likely a smaller
   effect but worth checking.
2. **Phase 9b-new (Z₆ vs. 2 × Z₃ phase coherence at k = 6).**
   The one untouched Ma-internal mechanism that is structurally
   motivated by extending Q132 v2's ω-sum to multi-strand
   composites.  Deuteron binding (2.2 MeV) as a one-number
   test; extend to ³He (7.7 MeV) and ⁴He (28.3 MeV) if the
   first number lands.

If both 9c and 9b-new fail, the "binding requires framework
extension" conclusion in F9a.6 is earned.  Until then, R63
stays open with a specific Ma-internal candidate in play.
