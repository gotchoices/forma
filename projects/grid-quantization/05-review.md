# Review: Ch. 5 — Why light is quantized

Checked against [work/countability-from-information.md](work/countability-from-information.md),
[work/energy-and-coherence.md](work/energy-and-coherence.md),
[foundations.md](../../grid/foundations.md) (A3, A5), and chs. 1–4.

Up front: §5.3 ("the integer needs the complex ψ"; "distinct from
charge"), §5.4 ("complementary, not independent"), §5.6 ("where the
energy route stops"), and the Status line ("the grade is final only
once chapter 6's import is settled") together address all four
high-severity items from
[work/chapter-outline-review.md](work/chapter-outline-review.md). Real
progress. Remaining items are new, at the prose / state-model level.

## Errors / incorrect statements

**1. §5.0 uses the amplitude ladder that
[energy-and-coherence.md](work/energy-and-coherence.md) §1 explicitly
forbids.** §5.0 introduces "Base n (general bounded): each cell takes
one of n equally-spaced values centred on zero, for example
{−2, −1, 0, +1, +2} for n = 5" and argues "no amplitude knob." But
energy-and-coherence §1 says, verbatim: *"What must be avoided is an
**amplitude** ladder (levels like {−1, 0, +1} read as magnitudes),
which re-introduces a magnitude degree of freedom and breaks the
pinned-magnitude argument; a phase dial of any size does not."* The
chapter is using exactly the model the source forbids, then asserting
the property ("no amplitude knob") the source says that model breaks.
The right object is a *phase* dial on a circle (the n positions are
angles, not magnitudes), where magnitude is automatically pinned. As
written, §5.0 contradicts its source and undercuts its own central
claim. (The base-2 ±1 case happens to coincide with both readings,
which is why nothing breaks visibly there.)

**2. The "compact phase" of §5.2 and the "ℵ-line of A3" of §5.7 are
different objects.**
[countability-from-information.md](work/countability-from-information.md)
§0 is careful to distinguish:
(i) the per-mode **oscillation phase** φ = ωt (a circle in phase
space — *generic to any harmonic oscillator*, GRID or not), whose
integer dual is **occupation**;
(ii) a phase wound around a *spatial* loop (charge); and
(iii) the per-edge A3 ℵ-line (an *internal* compact dimension of each
edge — a third object).
§5.2 uses (i) — the mode's temporal oscillation phase — to get the
Fourier integer. §5.7 then says "the substrate has a compact phase
(the ℵ-line of A3)" and treats that as the source of the §5.2
result. This silently identifies (i) with (iii). They are not the same
circle, and §5.2's argument is the generic-harmonic-oscillator one
(would hold for any oscillator anywhere), not a GRID-specific
consequence of A3. The chapter inherits GRID-specificity for what is
actually a universal HO fact — and the only way to genuinely connect
A3 to (i) is to argue that A3 *gives rise to* the per-mode oscillation
phase, which §5.7 asserts without showing.

**3. §5.3 elides the photon-number vs all-integer issue.** The chapter
states "the eigenvalues of N̂ = −i ∂/∂φ are exactly the integers from
§5.2." Strictly, the spectrum of −i ∂/∂φ on the circle is all of
**ℤ** (positive *and* negative); photon occupation is **ℤ_{≥0}**. The
mapping N̂ ↔ occupation matches only on the non-negative half. This is
the Susskind–Glogower / Carruthers–Nieto number–phase delicacy, and
[countability-from-information.md](work/countability-from-information.md)
§1 honestly flags it ("the phase operator is not quite self-adjoint").
Ch. 5 §5.3 does not, and as written it identifies n ∈ ℤ with photon
number without explaining how the negatives are excluded.

**4. §5.4 overstates the shared hinge.** The chapter says both routes
"rest on the *same* compact-phase structure plus the substrate's grain
bounds." The topological route does rest on the complex amplitude on
the compact phase. The energetic route, in
[energy-and-coherence.md](work/energy-and-coherence.md) §3, rests on
**boundedness** (pinned magnitude + fixed dW-per-transition) — it does
*not* require complex amplitudes or the U(1) Fourier structure of
§5.2. So the two share *boundedness* and *the substrate's grain
bounds*, not "the same compact-phase structure." Conflating them lets
§5.4's honest "share a hinge" point become "share a hinge they don't
actually share."

## Material omissions

**5. The per-cell A3 phase vs the per-mode oscillation phase is never
distinguished.** Item 2 above as a structural omission: the chapter
slides between three different "compact phases" — the bounded dial
(per cell), the temporal oscillation phase φ = ωt (per mode), and the
ℵ-line (per edge) — without flagging the difference. The whole "this
is *GRID*'s mechanism for quantisation" claim depends on which phase
is being invoked at each step, and the chapter never says.

**6. The transition-cost model is unspecified.** §5.0's energy
arithmetic — "two transitions of size 2A" vs "four small transitions"
giving "the same per-cycle figure" — implicitly assumes per-transition
cost is *linear in transition size* (2 × 2A·dW = 4 × A·dW). But
energy-and-coherence §1 says *"a transition (one step of the dial)
costs a fixed quantum of work dW"* — i.e., **constant per dial step**,
not linear in size. Under "fixed dW per step", the n = 3 staircase
(more steps per cycle) costs *more* per cycle than the stretched
square, and the "shape differs; scaling does not" claim fails. The
chapter needs to state and justify which cost model it uses.

## Imprecisions

**7. §5.0 "ℏ falls out, in natural units" mixes two different
statements.** "The substrate's smallest action ... is dW · τ. In
natural units this is ℏ = 1" is the *dimensional* statement from
ch. 4 (ℏ as a unit). It is **not** the load-bearing Bohr–Sommerfeld
statement "action per cycle = h" that §5.2 / §5.6 later invokes. The
chapter slides from one to the other, lending the latter the
dimensional inevitability of the former.

**8. §5.7 "discreteness gives the scaling, periodicity gives the
ladder."** Memorable framing, but the §5.0 scaling actually depends
on *boundedness* (the pinned-magnitude / no-amplitude-knob property),
not on "discreteness" per se — a *continuous* but bounded phase circle
delivers the same scaling. Using "discreteness" for boundedness blurs
the distinction the chapter is otherwise careful about (cf. §5.5,
where "finite dial" vs "continuous compact phase" is exactly the
discreteness axis, and only the *ladder cap* — not the *scaling* —
depends on it).

**9. Tension with ch. 1 over what ch. 1 said.** §5.7 attributes
"bounded (a finite dial)" to **chapter 1**, but ch. 1 §1.2 introduces
the per-edge state as a *continuous* compact phase θ on a circle, not
a finite dial. The finite-dial reading is energy-and-coherence's, not
ch. 1's. Ch. 5 either needs ch. 1 to introduce the finite dial too
(see [01-review.md §5](01-review.md) on the missing "magnitude
pinned" + the linear-amplitude-vs-compact-phase conflation), or §5.7
should cite the finite-dial reading to its actual source.

---

## Author response

Integrated items 1, 2, 3, 4, 6, 7, 9. Item 8 is partially rejected
(see below). Item 5 was structurally addressed by item 2's fix.

- **Item 1 (amplitude ladder vs phase dial).** Genuine source
  contradiction with energy-and-coherence §1, accepted. Fixed by
  adding a "Two technical notes on the model" paragraph in §5.0 that
  names the amplitude-ladder reading as the visual / intuitive
  framing, the phase-dial reading as the formal anchor, and the
  binary coincidence between the two. The §5.0 prose continues to use
  amplitude-ladder language for the user's original framing; the
  technical claim is now explicitly anchored on the phase dial.
- **Item 2 (three different "compact phases").** Real structural
  issue. Added a flagging parenthetical in §5.2 that distinguishes
  the per-mode oscillation phase φ (the Fourier-series argument's
  object) from A3's per-edge ℵ-line. The aggregation step from
  per-edge to per-mode is now explicitly named as part of chapter 6's
  import burden.
- **Item 3 (number-phase subtlety).** Accepted. Added a parenthetical
  in §5.3 acknowledging the all-of-ℤ vs ℤ_{≥0} issue, with a pointer
  to the Susskind-Glogower / Carruthers-Nieto delicacy that
  countability-from-information §1 flags. Robust part of the argument
  carries the load.
- **Item 4 (routes don't share what §5.4 implied).** Genuine
  overstatement, fixed. §5.4 now says explicitly that the scaling
  part of the energetic route rests on the *grain bounds alone* and
  does *not* need the compact-phase structure; only the *integer
  ladder* part shares chapter 6's hinge. Cleaner accounting of what
  the two routes actually agree on.
- **Item 6 (cost model unspecified).** Accepted. Added a second
  technical note in §5.0 explicitly flagging the cost-model
  dependency. The robust claim (scaling power ∝ ω) holds under any
  well-defined cost model for the stretched-square pattern; the
  prefactor is cost-model-dependent.
- **Item 7 (dimensional vs Bohr-Sommerfeld).** Accepted. §5.0's
  "ℏ falls out" paragraph now explicitly tags itself as the
  *dimensional* identity from chapter 4 and distinguishes it from
  the Bohr-Sommerfeld "action per cycle = h" that §5.6 / chapter 6
  will need separately.
- **Item 8 (discreteness vs boundedness).** **Partially rejected.**
  The reviewer says boundedness alone gives the scaling. I don't
  think this is right: a continuous bounded compact phase (S¹) gives
  power ∝ ω² (gradient-squared energy at fixed amplitude), not power
  ∝ ω. The §5.0 ω-scaling specifically needs the **discreteness** —
  fixed cost per discrete transition — *combined with* boundedness. I
  did however revise §5.7 to say "Bounded discreteness gives the
  scaling" (rather than just "discreteness"), making the conjunction
  explicit. The reviewer's framing item 8 isolated would suggest
  weakening this to "boundedness" alone, which would be incorrect.
- **Item 9 (finite dial sourcing).** Accepted. §5.7 now explicitly
  attributes the finite-dial reading to [A5](../../grid/foundations.md)
  and notes that chapter 1's compact phase is *continuous*; the
  discretisation is A5's contribution at the substrate scale.
