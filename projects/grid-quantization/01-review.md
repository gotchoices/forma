# Review: Ch. 1 — The substrate and the junction rule

Checked the draft against
[grid/foundations.md](../../grid/foundations.md),
[grid/hexagonal.md](../../grid/hexagonal.md), and `scripts/lib.py`.
Only logical errors, material omissions, and incorrect statements
below.

## Errors / incorrect statements

**1. A2 is misattributed.** §1.3 says "axiom A2 supplies discrete time
and the causal ordering." Per `foundations.md` line 33 ff., **A1**
("Four-dimensional causal lattice") is the axiom that supplies the
discrete lattice — including discrete time — and the length scale L;
**A2** is "Lorentzian signature (1,3)," which supplies the
timelike-vs-spacelike distinction (and from that, causal ordering).
The chapter has the discreteness coming from the wrong axiom.

**2. The full lattice is four-dimensional, not three.** §1.1 ends "the
full lattice is three-dimensional, but the account of light can be
developed on the sheet." A1 explicitly says four dimensions; with A2
giving (1,3), there are three *spatial* dimensions. As written this
reads as if the GRID lattice itself is 3D, contradicting A1.

**3. The per-edge state described and the rule shown are not the same
model.** §1.2 says "each edge carries one degree of freedom: a **phase
θ** … a position on a circle, with θ and θ + 2π denoting the same
state." §1.4 then states the rule

    outgoing = (2/3)·(sum of incoming) − incoming.

But that arithmetic — multiplying by 2/3, subtracting — is **not
defined on a compact phase**: a circle has no scalar multiplication that
respects 2π identification. The rule operates on real, unbounded
*amplitudes*, and the sim it cites (`scripts/lib.py:118 scatter_step`)
carries **two** real amplitudes per edge (`a_fwd`, `a_bwd`), not one
compact phase. So the chapter sets up the cell state as A3's compact
phase and then runs a continuous-amplitude rule on it, with no
acknowledgement that these are different models. This is exactly the
unresolved tension flagged in
[work/energy-and-coherence.md](work/energy-and-coherence.md) §5 ("the
continuous 2/3 rule is *not* the bit-conserving rule") and it surfaces
here as a load-bearing conflation, since chapter 5's U(1)↔ℤ route needs
the compact phase to be the genuine dynamical variable, not a
linearised amplitude. **This is the chapter's biggest material
problem.**

## Material omissions

**4. A1 is never cited.** A1 is the lattice axiom (4D discrete cells +
length scale L). It supplies the *stage* this chapter purports to set,
yet the Sources block lists only A2/A3/A4. Without A1 the discreteness,
dimensionality, and length scale are not anchored to any axiom in the
file.

**5. "Magnitude pinned" is missing.** The chapter outline
([work/chapter-outlines.md](work/chapter-outlines.md) §1.2) explicitly
calls for it — *point on a circle; only differences physical;
**magnitude pinned***. The draft has the "only differences physical"
half (gauge / A4) but drops magnitude pinning. That property is
load-bearing for chapter 5 (Planck scaling: pinned magnitude ⇒ E ∝ ω;
[energy-and-coherence.md](work/energy-and-coherence.md) §3); if it is
not introduced where the cell state is introduced, ch. 5 will have to
add it from scratch, breaking the arc's "introduce every concept before
use" rule.

**6. The sim's two-channel-per-edge state is not introduced.** The
chapter cites the rule and `scripts/lib.py` but never tells the reader
that the simulated edge carries `(a_fwd, a_bwd)` — a directed pair, not
a single scalar. A reader who follows the citation will find a state
model the chapter never described. This is the concrete face of issue 3.

## Imprecisions

**7. "The unique rule meeting both."** §1.4 calls the (2/N)·total − in
rule "the unique rule" meeting energy conservation + equal impedance.
It is unique under the additional (unstated) assumptions of real
coefficients (or no global phase) and time-reversal symmetry. With
complex amplitudes there is a phase freedom. Either name the
assumptions or soften "unique."

**8. "One edge per tick" conflates the causal limit with the wave
speed.** §1.3 says "nothing propagates faster than one edge per tick"
and "that ceiling … plays the role the speed of light plays in the
continuum." On this lattice these are *different* numbers: one edge per
tick is the causal limit (= L/τ), but the actual photon wavefront
travels at ≈ 0.41 (phase velocity, the small-k slope of the dispersive
band in `scripts/band_structure.py`; cf.
[work/energy-and-coherence.md](work/energy-and-coherence.md) §4 — "c ↔
L/τ holds only up to an O(1) lattice wave-speed factor"). The continuum
*c* is both at once; on the lattice they split, and this chapter
elides the split.

## Suggested fixes (compact)

- Re-cite the axioms: add A1 (4D discrete lattice, length L), correct
  A2 to (1,3) Lorentzian signature, keep A3/A4 as is.
- Change "three-dimensional" to "three *spatial* dimensions" and
  optionally note the +1 timelike per A2.
- Reconcile §1.2 ↔ §1.4: state explicitly that the dynamical variable
  in the sim is a real amplitude pair `(a_fwd, a_bwd)` per edge — a
  linearisation around the A3 compact phase — and flag that the
  relation between the phase and the amplitude model is itself an open
  item (the bit-conserving rule of energy-and-coherence §5–§6). Do not
  present the (2/3) rule as if it operates on the compact phase.
- Add "magnitude pinned" to §1.2.
- Soften "the unique rule" or name the real-coefficient assumption.
- In §1.3, distinguish the causal ceiling (one edge per tick) from the
  measured wave speed.

Want me to apply any of these to the chapter?

---

## Author response

Integrated all eight items. Notes on items where the integration is a
refinement rather than a literal acceptance:

- **#5 ("magnitude pinned" missing).** Integrated as the strengthened
  §1.2 sentence "only the angle matters — the cell has no separate
  amplitude or magnitude, only the phase." The explicit phrase
  "magnitude pinned" is held for ch. 5, where it is load-bearing for
  the binary-substrate E ∝ ω argument; ch. 1's job is to establish
  that A3 has only an angle, which is the property ch. 5 then names.
  Agree the content must be in ch. 1; partly disagree that it must
  be called "magnitude pinned" *here*.
- **#3 ("biggest material problem" — phase-vs-amplitude conflation)
  and #6 (two-channel state missing).** Addressed jointly in §1.4 by
  naming (a_fwd, a_bwd) as the simulated state, marking the
  real-amplitude form as a linearisation around A3's compact phase,
  and explicitly flagging the relation between the two as an open
  item (the bit-conserving rule of energy-and-coherence §5–§6). Not
  resolved — flagged. Agree this is the right honest move for ch. 1.
- **#7 ("unique rule").** Softened with the standard convention note
  (real, time-symmetric scattering) rather than enumerated.
- Everything else (items 1, 2, 4, 8) applied as written.

