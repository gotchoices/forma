# Review: Ch. 4 — ℏ is a unit, not a target

Checked against [energy-and-coherence.md](work/energy-and-coherence.md)
§3–§4, [tier2-design.md](work/tier2-design.md) §4b, and
[foundations.md](../../grid/foundations.md) (A5, A6).

This chapter is the cleanest in the arc — the category-error argument,
the grain-combinations, and the Planck-units identification are stated
honestly and the consistency-vs-theorem distinction in §4.4 is sharp.
Items below are residual imprecisions and one omission, not structural
problems.

## Imprecisions

**1. §4.3 vs §4.4 tension on c = L/τ.** §4.3 presents c = L/τ as clean
and dimensionally forced. §4.4 then caveats it: "c = L / τ itself holds
only up to an O(1) lattice factor — the *causal* limit is one edge per
tick, but actual wave packets move slower." Both are right; the
clearer presentation flags the O(1) factor in §4.3 the first time
c = L/τ is asserted, rather than walking it back in §4.4. (Same issue
shows up in ch. 1 §1.3 and ch. 2 §2.3.)

**2. §4.3 "ℏ = dW · τ … the area of one phase-space cell."** The
phase-space cell of Bohr–Sommerfeld / WKB quantisation has area **h**,
not ℏ — i.e. there is a 2π convention floating in the identification.
Conventional but worth either using "h" for the cell-area statement or
adding a one-clause note ("up to the 2π between h and ℏ"); as written
a careful reader notices the factor.

## Material omissions

**3. The universality of ℏ across fields is left implicit.** A real
strength of the grain framing is that the *same* ℏ governs every
interaction simply because everything is built from the same substrate
grains — the universality of action across fields is automatic, not a
separate assumption. The chapter argues ℏ = dW · τ as a *unit*; it does
not say "and this is why ℏ is universal across all fields, which would
otherwise be a non-trivial empirical input." That payoff is one
sentence and would strengthen §4.3.

**4. The ω = π flat band of ch. 3 is never engaged.** With ℏω as the
energy quantum, ω = π reads as a sharp maximum energy ≈ π · ℏ/τ = π · dW
— either a Nyquist/aliasing artifact or a genuine UV cutoff implied by
the grain. This chapter is the natural place to say which (it owns the
energy–grain identification), but it doesn't. Could be deferred to
ch. 5 if explicitly handed off; as written it just drops.

## Cross-chapter / scope notes (not chapter errors, but worth noting)

**5. The chapter's α-related claim is correct (§4.5: a pure number
cannot fix a dimensionful quantity) but the README's "Scope" still
asks "whether h and α can be **derived** … from lattice recirculation."**
Ch. 4's honest conclusion — h is a unit; α is an A6 input — retires
that scope. Not a chapter problem, but the chapter and the README
top-of-file should agree, and currently the README scope line is the
laggard.

**6. The ζ-from-A5 / G = 1/(4ζ) chain is asserted without sketch.**
§4.4 cites the identification "from axiom A5 the gravitational coupling
is G = 1 / (4ζ)" with foundations.md / gravity.md as the home. That is
fine as a citation, but the chapter is the first place in the arc this
appears and it does load-bearing work (pinning the absolute scale). A
half-sentence saying *why* G = 1/(4ζ) follows from A5 (the entropy /
Jacobson route, per gravity.md) would let the reader follow the chain
without leaving the chapter.

---

## Author response

Integrated items 1, 2, 3, 4, 6. Item 5 (README scope) is being
addressed as a separate cleanup outside the chapter.

- **Item 1** (c = L/τ O(1) caveat at first mention). The caveat now
  appears in §4.3 where c = L/τ is introduced, with a forward pointer
  to §4.4 — no walk-back.
- **Item 2** (ℏ vs h, 2π convention on "phase-space cell"). Added the
  one-clause note in §4.3 distinguishing h-area cells from ℏ-area cells
  and stating the grain identification is good to that conventional
  2π factor.
- **Item 3** (universality of ℏ across fields). Added as a short
  payoff paragraph after the grain-combination argument in §4.3: same
  grains → same ℏ for every interaction, automatically. This is the
  kind of payoff worth landing in the [reduced] register; thank the
  reviewer.
- **Item 4** (ω = π flat band as UV cutoff). Added a short paragraph
  in §4.3 reading ω = π · ℏ/τ = π · dW as both the Nyquist limit
  (discrete clock) and the single-mode UV cutoff — two readings of
  one number, fixed by the grain.
- **Item 5** (README scope still asks "derive h and α"). Not a chapter
  problem, as the review notes. Being addressed as the next item on
  the integration todo list.
- **Item 6** (G = 1/(4ζ) brief sketch). Added the half-clause in §4.4:
  "derived from A5's horizon entropy density ζA fed into Jacobson's
  thermodynamic recovery of Einstein's equations (gravity.md)."
  Reader can now follow the chain without leaving the chapter.
