# R59 Review

Review notes on the R59 Clifford‑torus study.  Sections may be added
later as further material is produced.

---

## Framing review

Review of [README.md](README.md) and [background.md](background.md)
as written at framing time.  Each item is tagged with a severity:

- **Serious** — substantive inconsistency, error of fact, or claim
  that is likely to mislead downstream work unless addressed.
- **Moderate** — real tension or overclaim that a careful reader
  will trip over; worth fixing but does not block the study.
- **Editorial** — wording, notation, or scope cleanup.  Cosmetic.

### Serious

**1. Tube/ring "pairs" contradict the T⁶ dimension count.**
[background.md:219](background.md) says:

> *"The tube circle lives in one pair; the ring circle lives in
> another.  The six compact dimensions of T⁶ provide exactly three
> pairs for the three sheets."*

These two sentences are mutually inconsistent.  A Clifford embedding
of one 2‑torus requires each S¹ to live in its own 2‑plane, i.e.
4 ambient dimensions per sheet → 12 dimensions for three sheets,
not 6.  Alternatively, if "pair" means a pair of compact dimensions,
then one sheet uses one pair (two coordinates, both circles of that
torus), which contradicts "tube circle in one pair, ring circle in
another."

The likely resolution is that Ma is *intrinsically* flat (T⁶ as a
Riemannian manifold) and the word "Clifford" is being used in the
flat‑torus sense — no R⁴ embedding is actually required.  The
background should state this explicitly.  The R⁴ picture is
pedagogical (a way to see why the 3D donut is distorted) and not
part of the physical geometry.

This matters because readers will try to square the dimension
count against Ma = T⁶ and either reject the framing or import a
wrong picture of the ambient space.

**2. "Model‑E metric IS the Clifford metric" undercuts Track 4's
premise.**  [README.md:48-49](README.md) asserts that the
model‑E flat‑torus metric has been the Clifford metric all along.
Track 4 then asks whether the R55 F8 metric saturation *disappears*
on the Clifford metric.  If the two metrics are identical, Track 4
has no lever: the saturation must originate in something R59 is
*not* changing (e.g. the ℵ mediator, the embedding‑motivated shear,
or a specific parameter choice in R55).

The study should state explicitly what R59 actually changes
numerically (vs. what it only reframes).  Otherwise Track 4 either
reduces to "rerun R55 and confirm the same number" or relies on a
difference that has not been identified.

### Moderate

**3. Internal tension on where α lives.**
[README.md:32-33](README.md) and [README.md:59-61](README.md) state
that α *is* the Ma–St off‑diagonal metric entry.
[README.md:94-99](README.md) then lists *"Where does α appear?  Is
it a single metric entry?"* as an open question.  These cannot both
be true in the same document.  Pick one — either frame the earlier
passages as the hypothesis to be tested, or remove the open
question.

**4. Velocity partition is an analogue, not an identity.**
[background.md:266-274](background.md) says:

> *"v²_Ma + v²_S = c² IS Einstein's energy–momentum relation
> E² = (mc²)² + (pc)²."*

This is an overclaim.  The velocity partition is Euclidean (sign +
on both terms); Einstein's relation is Lorentzian (sign − between
mass and momentum pieces).  The partition reproduces the Lorentz
factor γ = 1/√(1 − v²/c²) correctly and is a useful mnemonic, but
it is not the same equation.  Replace "IS" with "is the velocity
form of" or "is equivalent in interpretation to."

**5. Signed‑curvature mechanism stated as derived, not as
hypothesis.**  Both [README.md:25-28](README.md) and
[background.md:141-144](background.md) present

> opposite charges → fields cancel → St curvature *reduced* →
> geodesics converge → attraction

as a settled mechanism.  This is the opposite of the usual
gravitational intuition (more mass → more curvature → stronger
attraction), and in standard KK the sign of the force on a test
charge comes from the gradient of the gauge potential acting on
that charge's winding number — not from the magnitude of St
curvature.  The picture given may be correct for the right
definition of "curvature," but the derivation is exactly what
Tracks 2 and 5 are supposed to produce.  The framing sections
should present it as the hypothesis to be tested, not as already
established.

### Editorial

**6. "10 + 1 = 11 dimensions" notation.**  [README.md:149](README.md)
writes *"Total: 10+1 = 11 dimensions (or 10 without ℵ)."*  The
"D+1" convention in physics usually means "D space + 1 time."
Here "10" already includes time (6 Ma + 3 S + 1 t) and "+1" is ℵ.
Clarify, e.g., *"6 Ma + 3 S + 1 t (= 10), plus ℵ for 11."*

**7. Extrinsic curvature in the math list.**
[README.md:217-218](README.md) lists "extrinsic curvature" as a
concept to develop.  The Clifford torus has zero extrinsic
curvature in R⁴ by construction; the second fundamental form is
really only useful here as a *contrast* with the 3D donut
embedding.  Worth saying so in that bullet.

**8. Dependency list.**  `sim-impedance` appears in the dependency
list but is not an R‑numbered study in STATUS.md.  A pointer to
where `sim-impedance` lives in the repo would help future readers.

---

## Overall (framing)

None of the items above block starting Track 1.  Items **1** and
**2** should be addressed before the study leans on those claims
(Track 1 for item 1, Track 4 for item 2).  Items **3–5** are
worth a pass during the next edit of the framing documents to
prevent later readers from importing overclaimed statements as
settled results.

---

## Track 1 review

Review of [findings.md](findings.md) §Track 1 and
[scripts/track1_metric_with_time.py](scripts/track1_metric_with_time.py).
Severity tags as before.

### Writeup — structural

The findings list results but rarely tie them back to the
hypothesis under test.  Each F should end with a one‑line
"what this means for the hypothesis" — whether it confirms,
refines, or threatens it.  Specifics:

- **F1 (sanity check).**  *Editorial.*  Label it as such.  The
  non‑trivial part is that three independent methods agree in
  the decoupled limit; this matters later when F3 shows they
  disagree once coupling is on.  Stating the sanity‑check role
  prevents the reader from treating F1 as a surprising result.

- **F2 (tube catastrophe).**  *Moderate.*  The pivot from tube
  to ring coupling is reported as a numerical fact but the
  physics loose end is not named: the naive KK identification
  has charge = tube winding AND the coupling potential on the
  tube.  Track 1 shows the latter is unusable.  The findings
  should name the gap — *"if charge is tube topology and α is
  ring‑coupled, by what mechanism does a tube‑winding mode
  feel the ring‑mediated field?"* — as an open question for
  Track 3.

- **F3 (Schur vs mass‑shell).**  *Serious.*  The explanation
  given — *"Schur doesn't properly account for Lorentzian
  signature"* — is misleading.  The Schur code does use
  g_tt = −1 correctly.  The real issue is that Schur on time
  imposes the slice k_t = 0; for a massive mode k_t = E ≠ 0,
  so Schur‑on‑t is answering a different question (effective
  metric on the massless slice) than mass‑shell (null
  propagation in full 10D).  Because R55 integrated out a
  Euclidean ℵ (no conjugate energy), Schur was arguably the
  right tool there.  The 20× disagreement in F3 is therefore
  **not evidence that R55's numbers were wrong** — it is
  evidence that Schur‑on‑t is the wrong tool for Lorentzian
  mass extraction.  The findings text conflates these.

- **F4 (mass decrease).**  *Serious.*  Currently framed as an
  interpretation note.  It is in fact a **threat to the
  hypothesis**: the observed Coulomb self‑energy *raises* the
  rest mass of a charged particle (∝ +α m in magnitude).  A
  mechanism that *lowers* it goes the wrong way and must be
  explained before the Ma‑t picture is considered established.
  The writeup should name this directly.

- **F5 (1.9 % gap).**  *Editorial.*  Frame it as the primary
  positive test of the Track 1 hypothesis.

- **F6 (R55 vs R59).**  *Moderate.*  Given the F3 re‑reading,
  the comparison table is not apples‑to‑apples: R55 used Schur
  on a Euclidean ℵ; R59 uses mass‑shell on Lorentzian t.
  Before attributing the "halved gap" to the time dimension,
  recompute R55's mechanism under the mass‑shell condition (or
  R59's under Schur with matched assumptions) so the
  difference can be localized to the geometry, not the method.

- **F8 (ν coupling 1.035α).**  *Serious.*  See script flaw
  below — the neutrino's coupling was put in **by hand** in
  the b‑vector (+σ on ν‑ring, same magnitude as proton).  The
  "ν couples at 1.035α" result is a consequence of that
  assignment, not an emergent prediction.  It cannot be cited
  as support for EM‑like neutrino coupling (and therefore not
  for L05) without a physical argument for why ν‑ring should
  carry that entry.

### Script / interpretation flaws

- **α_eff ≡ |ΔE/E| is ad hoc.**  *Serious.*  This is a
  fractional rest‑mass correction, not the fine‑structure
  constant.  α governs Coulomb coupling / EM interaction
  strength.  Δm/m is a self‑energy‑like quantity.  Near‑equality
  of Δm/m across species is not the same as universal EM
  coupling.  The tuning "set σ so α_eff(e) = α" matches one
  quantity to another without justifying the identification.
  The findings treat α_eff as α throughout — this identification
  needs to be either derived (e.g. by showing that the Ma‑t
  coupling produces a Coulomb field in S of the standard
  strength) or explicitly flagged as an operational proxy.

- **Neutrino assigned nonzero ring coupling.**  *Serious.*
  [track1_metric_with_time.py:287,382](scripts/track1_metric_with_time.py#L287)
  sets `b = [0, −σ, 0, +σ, 0, +σ]` with ν‑ring at +σ.  Real
  neutrinos are electrically neutral.  Either the entry should
  be zero (and F8 drops out), or the physical meaning of that
  entry is not EM coupling.

- **Charge signs hand‑coded, not derived.**  *Moderate.*  The
  sign pattern in `b` is an ansatz chosen to echo observed
  charges (e −, p +).  A first‑principles coupling should have
  the signs emerge from the mode structure, not be pre‑inserted
  in the metric off‑diagonals.  Worth stating as a known
  limitation of Track 1's scope.

- **Quadratic root selection.**  *Moderate.*
  [track1_metric_with_time.py:204](scripts/track1_metric_with_time.py#L204)
  returns `min(E_plus, E_minus)`.  The two roots correspond to
  the two signs of ω and represent particle and antiparticle
  states; when b_coeff ≠ 0 the two magnitudes differ, and that
  splitting is physically meaningful (charge‑dependent energy
  offset).  Taking the minimum magnitude discards the
  particle/antiparticle mass splitting.  The script should at
  least report both roots and let the interpretation take the
  splitting into account — it may be directly relevant to the
  F4 sign puzzle.

- **One‑knob fit.**  *Moderate.*  With a single σ tuned to a
  single target (α_eff(e) = α), every other species' α_eff is
  determined by fixed geometric ratios (L₁…L₆ and the shears).
  The 1.9 % universality gap is then a property of those ratios,
  not independent evidence that the mechanism is correct.
  Worth stating explicitly.

### Net

Track 1 shows that ring Ma‑t coupling can be tuned to match α
for the electron and lands other species within 1.9 % — a
non‑trivial geometric result, but fundamentally a one‑parameter
fit with an operationally defined α_eff.  The findings writeup
overstates the result in several places (universality without
the one‑knob caveat; ν coupling as emergent; R55 comparison
without the method caveat; mass decrease as a minor puzzle
rather than a directional threat to the hypothesis).  The
corrections are mostly textual, but the ν‑coupling hand‑coding
and the α_eff / α identification are substantive and should be
addressed before Track 2 builds on them.

### Suggested Track 1b: ℵ‑mediated time coupling

Track 1 implicitly decided the ℵ‑vs‑t question by omission: the
metric has no ℵ, so t had to couple directly to Ma, which forced
the hand‑coded six‑entry `b_Ma_t` ansatz.  A cleaner architecture
worth testing:

- 11D metric = 6 Ma + 3 S + 1 t + 1 ℵ
- Keep R55's Ma‑ℵ block at its tuned values (don't re‑fit)
- Set all direct Ma‑t entries to zero
- Introduce a **single** off‑diagonal entry σ_{ℵt}
- Solve the mass‑shell condition for each mode

In this architecture the effective Ma‑t coupling emerges at
leading order as g(Ma,t)_{eff} ≈ g(Ma,ℵ) g(ℵ,t) / g(ℵℵ), so the
single σ_{ℵt} multiplies R55's existing Ma‑ℵ structure to produce
the whole family of induced Ma‑t entries.  Relative magnitudes
and signs across species are then **inherited** from R55's
geometry, not stipulated by hand — which addresses two of the
Track 1 script flaws directly (hand‑coded signs; ν‑ring coupling
chosen by the author rather than emerging).

Benefits:

- One knob (σ_{ℵt}), not six.
- Sign structure determined by geometry, not by ansatz.
- Matches the GRID picture of ℵ as the lattice substrate
  through which all couplings propagate.
- The ℵ block is Euclidean, so only the final ℵ–t link carries
  Lorentzian signature — R55's Schur machinery stays valid on
  the ℵ side, and mass‑shell is applied only to the one
  Lorentzian leg.

Caveats:

- Routing the gauge potential through ℵ is not textbook KK; the
  reduction to A_μ needs to be re‑derived on the 11D metric to
  confirm the induced object is the right one and that α comes
  out cleanly.
- If R55's Ma‑ℵ entries assign the ν‑ring a nonzero value, this
  architecture inherits the same neutrino coupling issue F8 has.
  Not worse than Track 1, but not automatically fixed either.
- Adds one parameter relative to Track 1's one knob; total
  parameters are R55's Ma‑ℵ entries plus σ_{ℵt}.  The trade‑off
  is buying physical structure (emergent signs, inherited
  universality) in exchange for the extra degree of freedom.

Pass criterion: σ_{ℵt} alone (with no direct Ma‑t) matches or
beats Track 1's 1.9 % universality gap with signs inherited from
R55 rather than hand‑coded.  A positive result would be stronger
than Track 1's current claim; a negative one would justify the
direct Ma‑t architecture on its merits.

---

## Tracks 1b, 1c, 1d review

Review of the ℵ‑mediated track (1b), the minimal single‑sheet
track (1c), and the two‑sheet track (1d) as reported in
[findings.md](findings.md) F9–F21.

### What's going well

- Writeup now routinely flags "one‑parameter fit," "hand‑coded
  signs," and "proxy α_eff" — a real improvement over the
  original Track 1 text.
- F4 (mass decrease) is named as a threat; F9 (mass increase
  through ℵ) partially resolves it.
- Structural decomposition via 1c/1d confirms that coupling
  entries don't touch the particle‑spectrum entries (F15) and
  that generation structure is preserved (F17).  These are
  genuinely reassuring.
- The R55 comparison is re‑framed honestly (F7) rather than
  claiming a straightforward "halved gap."

### What's concerning

- **Still tuning a proxy.**  *Serious.*  Every sub‑track tunes
  σ until α_eff ≡ |ΔE/E| matches α.  The F6 caveat that this
  identification needs Track 3 to validate is still
  outstanding.  The entire 1/1b/1c/1d family is optimizing
  against an objective function whose physical meaning is
  deferred.
- **Sign dichotomy is not a benign tradeoff.**  *Serious.*  F14
  frames D1 and D2 as complementary (D1 wins universality, D2
  wins sign), but a mechanism that produces the *wrong sign*
  of a self‑energy correction is not a variant of a right
  mechanism — it is a different mechanism.  That the α_eff
  quantity is insensitive to this distinction is another
  symptom that α_eff ≠ α.
- **Inherited signs in 1b are reversed.**  *Serious.*  F11
  reports e‑ring +, p‑ring − — backwards relative to observed
  charge — and waves it off as *"may differ from charge sign."*
  Inherited signs in Track 1b come from R55's *fit*, not from
  an independent derivation, so "emergent" oversells what is
  happening.
- **F21 non‑monotonicity is a red flag.**  *Moderate.*  α_eff
  passing through zero means the tuning surface has two
  branches with different physics; the 4.23 % gap depends on
  which branch.  A quantity with zero‑crossings is not a
  coupling strength but a residual of competing contributions.
- **1 % baseline shift from ℵ (F13) silently re‑tunes.**
  *Moderate.*  Model‑E was tuned with ℵ absent.  Turning ℵ on
  shifts masses 1 % before any σ_{ℵt} is applied.  The final
  gap attribution to the coupling is blurred by this baseline.
- **"Structural gap" claim only half established.**  *Editorial.*
  F20 asserts the gap is a geometric property of aspect ratios
  but doesn't test it by varying L_p/L_e etc.  Either show the
  gap tracks aspect ratios (confirming the ceiling), or drop
  the claim.

### Strategic advice

1. **Pause Track 1 variants; do Track 3.**  Track 3's KK
   reduction is what turns α_eff into an actual Coulomb
   coupling.  Each possible outcome of Track 3 (|ΔE/E| equals
   α, is proportional to α, or is unrelated) directly decides
   whether D1, D2, or neither is the physical architecture.
   Without that decision, more variants are moves on a board
   whose rules aren't fixed.

2. **If Track 3 has to wait, resolve F4 first.**  Three
   concrete diagnostics for the mass‑direction puzzle:
   - Decide whether F5's low root or high root is "the
     particle" under a consistent charge‑sign definition.
   - Compute standard KK Coulomb self‑energy for a (1,2)
     winding and compare magnitude to 0.7 %.
   - Flip the metric signature convention and see whether
     the sign of ΔE/E follows — if so, F4 is a signature
     artifact, not a physics failure.

3. **Hold Track 1e (neutrino sheet).**  F8 and F12 both
   depend on whether the ν‑ring Ma‑ℵ entry is 0 or nonzero.
   That is a framing choice, not something another numerical
   track can settle.  Adding a third sheet before the D1/D2
   question is decided multiplies parameter space without
   progress on the hypothesis.

### Net

Methodologically the work has improved.  Strategically the
Track 1 family is drifting — each sub‑track is a variation on
an objective that has not been validated.  One move toward
Track 3, or one hard push on F4, would produce more signal
than three more Track‑1 variants.

---

## Track 3 review

Review of [findings.md](findings.md) §Track 3 (F28–F31) and
[scripts/track3_coulomb_field.py](scripts/track3_coulomb_field.py).

**Track 3 was the critical next step.**  Its job, per
[README.md:184-188](README.md), was to perform the KK reduction
on the 10D/11D metric and show that the Ma‑t off‑diagonal
entries produce A_μ with gauge coupling α.  This would validate
Track 1's α_eff / α identification and close the proxy concern
that's been hanging over every prior track.

**It did not do that job.**  The track as written is a
narrative/analogy exercise, not a derivation.  Rebuilding it is
warranted.

### What went wrong

1. **Scope mismatch — narrative substituted for computation.**
   *Serious.*  The script computes ~4 scalar ratios (σ/√α,
   σ²/α, R/λ_C, U_Coulomb/mc²) and wraps them in several
   pages of prose.  There is no integration over Ma, no
   extraction of A_μ from the metric, no force computation
   between two charged modes.  The KK reduction named in the
   README was not performed.

2. **F28 is vacuous as evidence.**  *Serious.*  *"The 1/r
   spatial dependence is guaranteed by 3D geometry"* — true,
   but it's true for **any** localized source: Newtonian
   gravity, Yukawa at short range, heat flow, static pressure.
   The 1/r profile is a property of the 3D Laplacian's Green's
   function, not evidence that the mechanism is EM.  The
   **coefficient** (= α) is the entire content of Coulomb's
   law, and F28 does not produce it.

3. **F29 is a concession, not a resolution.**  *Serious.*  It
   correctly computes the classical Coulomb self‑energy on a
   ring (U/mc² ≈ α × λ_C/R ≈ 9.4 for the electron) and
   compares it to Track 1's ΔE/E ≈ α ≈ 0.0073 — a factor of
   ~1300× discrepancy.  It then concludes *"the Track 1 mass
   shift is NOT the Coulomb self‑energy — it's something else
   that happens to equal α."*  This is an admission that the
   α_eff / α identification was never physical; tuning one
   knob to α does not make that knob α.  The R59 status
   summary then lists F28–F30 as positive achievements without
   weighting the F29 concession — the scorecard is skewed.

4. **F30 ("correct sign structure") is imported, not
   derived.**  *Moderate.*  The claim *"positive winding
   produces positive Ma‑t perturbation"* is asserted from
   linearized gravity with a charge‑like sign stuck on by
   hand.  A proper KK reduction would derive the sign from
   the winding's phase structure.  Track 3 does not.

5. **The standing‑wave ↔ compact‑momentum gap is flagged and
   then dropped.**  *Serious.*  Part 4 of the script notes
   that textbook KK works for compact momentum p₅ = n/R,
   while MaSt uses standing waves.  The script says *"the
   question remains: does our δ = α produce the correct
   spatial field?"* and then moves on.  This is exactly the
   gap Track 3 was supposed to cross.

6. **Linearized gravity is invoked in a way that begs the
   question.**  *Moderate.*  The script writes
   *T_{Ma,t} ∝ σ × Mc²* and *δg_{Ma,t} ∝ σ × GM/(c²r)* as if
   these follow from linearized Einstein — but T_{Ma,t} is
   not a piece of the usual stress‑energy tensor.  To source
   an off‑diagonal metric perturbation you need an off‑diagonal
   stress‑energy, which in KK comes from a *current* on the
   compact dimension (∂_μ θ for a winding mode), not from a
   rest‑mass term.  The argument elides this and then claims
   the result (*"F = n₁ × σ² × GM/r²"*) matches Coulomb when
   *σ² × GM = α*.  That's dimensional juggling, not a
   derivation — GM has units of length (c = 1) but σ is
   dimensionless in Track 1, so the equation doesn't close
   without further assumptions.

### How to rebuild Track 3

The rebuild should be a **computation**, not a narrative.  Two
honest routes exist; I'd recommend running **both** in parallel
for cross‑validation, since they probe the same question from
different angles.

**Route A — Proper KK reduction for standing waves (analytical).**

Scope:
1. Start from the 10D action for a massless scalar (or the
   Ma-standing-wave mode) on the metric produced by Track 1
   (include the Ma‑t off‑diagonal).
2. Decompose the field into modes with winding **n** on Ma and
   spatial dependence in S: ψ(x, θ) = Σ_n ψ_n(x) e^(i n·θ).
3. Integrate the action over Ma (θ coordinates).  The off‑
   diagonal g(Ma, t) produces cross terms of the form
   A_μ(x) × ∂^μψ_n × (winding factor).
4. Identify A_μ(x) as the 4D gauge field.  Read off its
   normalization from the g_tt factor and the compact volumes.
5. Derive the effective 4D charge q_n of a mode with winding
   **n**.  Compute q_e² / (4π ε₀ ℏc) and check whether it
   equals α.

Expected output: a closed‑form expression q_n = f(**n**, L_i,
σ) and a numerical value for q_e²/(4π ε₀ ℏc).  A successful
rebuild either (a) produces α without further tuning — in
which case R59's central claim is validated — or (b) produces a
different number, which falsifies the α‑from‑σ hypothesis.
Either result is publishable.

This is the textbook move but adapted to windings, not
compact momenta.  References: Appelquist–Chodos, Overduin–
Wesson "Kaluza‑Klein Gravity" (Physics Reports 1997),
Polchinski Vol. 1 §8.1–8.4 on T‑duality for the
momentum↔winding exchange.

**Route B — Numerical 10D Green's function (computational).**

Scope:
1. Place a source mode (e.g. electron, n = (1,2,0,0,0,0)) at
   the origin in S.  Construct T_μν from the mode's energy
   distribution on Ma × S.
2. Solve the linearized 10D Einstein equations for δg_μν on
   the full 10D manifold.
3. Extract δg_{Ma,t}(r) in S at distances r from Compton scale
   out to 10² × L_ring.
4. Fit δg_{Ma,t}(r) to C/r and extract C.
5. Compute C / (α × m × some‑geometric‑factor) and report the
   coefficient.

Expected output: a numerical coefficient.  If ≈ 1 at large r,
the Coulomb identification holds.  If not, the discrepancy
tells you exactly how far off the σ‑to‑α map is.

This is heavier numerically but has no analytical pitfalls —
the sign, magnitude, and spatial dependence all come out of
one solve.

### Acceptance criteria for the rebuild

A rebuilt Track 3 should meet **all** of:

- Produces A_μ explicitly (Route A) or δg_{Ma,t}(r) on a
  grid (Route B).
- Extracts a **number** that plays the role of α from the
  geometry (not a ratio chosen to equal α by construction).
- States whether that number equals α, and by how much it
  deviates.
- Derives the charge sign from mode structure, not from hand
  insertion in `b`.
- If it fails to produce α, it diagnoses **which step**
  produces the wrong number — the normalization, the geometric
  factor, the standing‑wave kinematics, etc.

### Fallback if the rebuild also fails

If both Route A and Route B produce numbers that do not equal
α, that is a substantive negative result and worth reporting
cleanly.  It would mean:

- The Ma‑t off‑diagonal is *not* the seat of α.
- The α coupling lives in a different metric quantity — possibly
  a ratio of geometric scales (e.g. L_p / L_e as in R31/R36),
  or the compactification volume (as in standard KK), or some
  GRID‑lattice property.
- The Track 1 α_eff = α match is geometric coincidence from
  one‑parameter tuning, not physics.

That outcome would redirect the whole study but is itself
a valid scientific conclusion.  The worst outcome would be
another narrative track that neither derives α nor cleanly
rules out the mechanism.

### Net

Track 3 as delivered does not answer its framing question.
The failure is in scope and method, not in honesty — F29
correctly names the 1300× discrepancy.  A rebuild along
Route A or Route B (ideally both) is the next critical piece
of R59.  Until that rebuild lands, the Track 1 family's
"universality," "correct sign," and "Coulomb from geometry"
claims all rest on an unvalidated identification.
