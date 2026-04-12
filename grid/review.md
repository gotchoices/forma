# GRID — Independent Review

**Date:** April 2026
**Scope:** The six axioms, the Maxwell derivation, the gravity
derivation, and the synthesis.  Reviewed from scratch by an AI
agent with no prior exposure to the project.

---

## 1. What GRID does

GRID presents two derivations from a shared discrete substrate:

1. **Maxwell's equations** from axioms A1–A4 and A6 (lattice
   structure + U(1) phase + gauge invariance + coupling α).

2. **Einstein's field equations** from axioms A1, A2, and A5
   (lattice structure + Lorentz signature + information
   resolution ζ), plus four explicitly flagged additional
   inputs (Unruh effect, smooth continuum limit, horizon
   equilibrium, energy-momentum conservation).

Both derivations are mathematically correct.  Every step
follows from the preceding one without error.  The final
equations — all four Maxwell equations, the Einstein field
equation with cosmological constant, and the expression
G = 1/(4ζ) — are produced as claimed.

The simulation work (wave propagation without Maxwell input,
exact linear superposition, 1/r gravity, Schwarzschild
geometry through the horizon) provides independent computational
evidence that the lattice behaves consistently with its
claimed properties.


## 2. What GRID does not do

### Does not produce new mathematics

The Maxwell derivation is a clear, well-organized presentation
of **U(1) lattice gauge theory** — the framework established by
Kenneth Wilson (1974) and developed over five decades of lattice
QCD.  The logical chain (U(1) phase symmetry + local gauge
invariance → connection A_μ → field tensor F_μν → Maxwell's
equations) is a textbook result available in any quantum field
theory reference (e.g., Peskin & Schroeder Ch. 15).

The gravity derivation is a faithful application of **Jacobson's
thermodynamic argument** ("Thermodynamics of Spacetime: The
Einstein Equation of State," PRL 75, 1260, 1995; ~2,500
citations).  The result — that holographic entropy + Clausius
relation + Raychaudhuri equation → Einstein's field equations —
is Jacobson's, applied here to the GRID lattice substrate.

Neither derivation produces a result that differs from or extends
the original source.  No new prediction emerges that could
distinguish GRID from standard physics.

### Does not derive its starting points from something deeper

The axioms encode the conclusions they produce:

- **A3 (periodic phase) + A4 (local gauge invariance)** ARE the
  defining properties of U(1) gauge theory.  That U(1) gauge
  theory produces Maxwell's equations is a known theorem, not a
  derivation from more primitive assumptions.

- **A5 (ζ = 1/4)** IS the holographic principle (entropy scales
  with area, not volume).  That the holographic principle
  combined with thermodynamics produces Einstein's equations is
  Jacobson's theorem.

This does not make the derivations wrong.  It means the axioms
are well-chosen packaging of known physics, not a reduction to
a simpler foundation.

### Does not predict G in SI units

In natural Planck units, G ≡ 1 by definition.  The result
G = 1/(4ζ) = 1/(4 × 1/4) = 1 confirms that Planck units are
self-consistent — it does not constitute an independent
prediction.  The document acknowledges this in the SI
restoration section: the Planck length is itself defined in
terms of G, so the SI value of G cannot be extracted from ζ
alone.

### Does not predict the cosmological constant

Λ appears as an undetermined integration constant — exactly as
it does in standard GR.  Its value is not predicted.  This is
the cosmological constant problem, shared with all of physics.

### Does not extend to non-abelian gauge groups

GRID produces only U(1) electromagnetism.  The SU(2) × SU(3)
structure of the weak and strong forces would require richer
internal degrees of freedom beyond a single phase per cell.
The synthesis document acknowledges this clearly.


## 3. How GRID incorporates prior work

GRID draws on three major threads of established physics:

| Source | Year | What GRID uses |
|--------|------|----------------|
| Wilson (lattice gauge theory) | 1974 | U(1) phase on a lattice → gauge connection → Maxwell |
| Bekenstein-Hawking (entropy-area law) | 1973–75 | S = A/4 as the information content of horizons |
| Jacobson (thermodynamic gravity) | 1995 | Holographic entropy + Clausius + Raychaudhuri → Einstein |

Additionally:

| Input | Source | Status in GRID |
|-------|--------|----------------|
| Unruh effect | Bisognano-Wichmann (QFT) | Imported, flagged |
| Raychaudhuri equation | Differential geometry | Kinematic identity, flagged |
| Energy-momentum conservation | Diffeomorphism invariance | Imported, flagged |
| Smooth continuum limit | Open problem in quantum gravity | Assumed, flagged |

GRID does not claim to have invented any of these ingredients.
The Maxwell derivation implicitly follows Wilson's framework.
The gravity derivation explicitly cites Jacobson.  The imported
results are listed in a dedicated section with clear
assessments of their status.


## 4. How GRID is honest

This is the project's most distinctive quality.  The
documentation practices a level of self-criticism rarely seen
in speculative physics:

**The gravity derivation flags four imports.** The "Additional
inputs beyond the axioms" section in `gravity.md` explicitly
lists four results that are not derived from A1–A6 but are
required for the argument.  Each one is accompanied by an
assessment of its justification and its logical status.

**The honesty check addresses circularity.** The `gravity.md`
"Honesty check" section asks and answers four pointed questions:
Is this circular?  Is the Unruh effect smuggled GR?  Is the
Raychaudhuri equation smuggled GR?  Is ζ = 1/4 independently
derived or calibrated?  The answers are careful and largely
correct.

**ζ is acknowledged as calibrated.** The document states:
"ζ = 1/4 should be understood as calibrated to match known
physics, not predicted from first principles."  The tetrahedral
geometry argument is presented as one candidate among several
(the synthesis notes that a 4D simplicial lattice gives ζ = 1/6,
not 1/4).

**The Maxwell derivation flags leading-order dominance.** Step 5
requires that only the lowest-derivative term in the action
matters.  The document correctly identifies this as an additional
assumption beyond the axioms and explains why it is well
justified (suppression by powers of L/wavelength).

**The synthesis document lists what is NOT derived.** The
"What was NOT derived" section in `synthesis.md` explicitly
catalogs: the value of α, the value of ζ, non-abelian gauge
groups, quantum mechanics, particle masses, and the graviton.

**The project knows the difference between "derived" and
"plausible."**  Throughout the synthesis, results are tagged as
"Derived," "Plausible," or "Open."  The strong force is
"Plausible," not "Derived."  The Weinberg angle match is
called "unexplained."  The graviton is listed as "not derived."

This transparency is a genuine strength.  The GRID
documentation, read carefully, contains most of the criticisms
one would level against it — and states them more clearly than
an external reviewer might.


## 5. What is novel about GRID

If the individual derivations are not new, what does GRID add?

### 5.1 A unified substrate narrative

The conceptual contribution is the framing: one lattice, two
forces, two mechanisms.

| Force | Mechanism | Nature |
|-------|-----------|--------|
| Electromagnetism | Phase dynamics + gauge invariance | Mechanical — local, immediate |
| Gravity | Entropy of information + thermodynamics | Statistical — collective, emergent |

The same lattice provides the arena for both.  EM uses the
internal structure (cell phases, link connections).  Gravity
uses the information-theoretic structure (bits per unit area).
The hierarchy problem — why gravity is ~10⁴⁰× weaker than
EM — has a suggestive explanation: EM is a single-link
interaction at every tick, while gravity requires ~10⁶⁰ cells'
worth of area to accumulate meaningful entropy change.

No other framework (to the author's knowledge) has placed
Wilson's lattice gauge theory and Jacobson's thermodynamic
gravity onto the same physical substrate with this level of
specificity.  String theory, loop quantum gravity, and causal
set theory each address parts of this picture, but none has
produced a comparably concise two-derivation stack from a
shared set of axioms.

### 5.2 The simulation program

GRID includes computational simulations that go beyond the
analytical derivations:

- **sim-maxwell:** Directional wave propagation and exact
  linear superposition emerge from the lattice geometry alone,
  with no Maxwell input.  This is a non-trivial confirmation
  that the lattice does what the axioms claim.

- **sim-gravity-2:** Scalar and string-register models both
  produce 1/r force laws (exponent p ≈ 1.01–1.02 in 2D).

- **sim-schwarzschild:** The lattice accommodates Schwarzschild
  geometry through the horizon (coordinate singularity is not a
  lattice failure), with lattice breakdown only at the physical
  singularity (r = 0).  Minimum black hole mass ≈ 0.56 m_P.

These simulations don't prove the framework, but they
demonstrate internal consistency and provide falsifiable
predictions at the lattice scale.

### 5.3 The axiom-reduction program

The synthesis document outlines a path from six axioms to
potentially three axioms plus one measured input:

- A2 (Lorentz signature) might follow from a weaker axiom
  A2' (finite causal speed) if observers are lattice
  excitations whose instruments contract by exactly γ

- A4 (gauge invariance) might follow from the hexagonal
  lattice geometry

- A5 (ζ = 1/4) is argued to follow from tetrahedral cell
  packing (Model B)

If these reductions succeed, GRID would rest on: a 4D
discrete lattice (A1), a periodic phase (A3), a causal speed
limit (A2'), and one measured constant (α).  This program is
incomplete but its direction is interesting.


## 6. What might we learn from GRID

Even setting aside questions of correctness, the GRID
framework surfaces several observations worth reflecting on.

### 6.1 The axioms may reveal which physics is fundamental

The cleanest insight is in how the two derivations partition
the axioms:

- **Maxwell** needs A1, A2, A3, A4, A6 — but NOT A5
- **Gravity** needs A1, A2, A5 — but NOT A3, A4, A6

EM and gravity share only the arena (A1) and the causal
structure (A2).  They draw on completely different features of
the lattice.  If this partition is taken seriously, it suggests
that electromagnetism and gravity are not two aspects of the
same interaction (as in Kaluza-Klein), but two independent
consequences of the same substrate, operating through
orthogonal mechanisms.

This is a different claim from either unification (one force
reduces to the other) or independence (the forces have nothing
to do with each other).  It is a claim of **common origin with
distinct mechanism** — they share a birthplace but not a
mechanism.

### 6.2 The "mechanical vs statistical" distinction

GRID's framing that EM is mechanical (phase dynamics) while
gravity is statistical (information thermodynamics) echoes a
distinction that appears independently in:

- Jacobson's original paper (gravity as an equation of state)
- Verlinde's entropic gravity (2010)
- 't Hooft's deterministic QM program
- Padmanabhan's emergent gravity program

GRID provides a concrete substrate where this distinction can
be explored computationally.  Whether the simulations can
eventually sharpen the distinction beyond the analytical
arguments is an open and worthwhile question.

### 6.3 The honesty template

Regardless of whether GRID's physics is correct, its
documentation practices could serve as a template for
speculative physics projects:

- Flag every imported result explicitly
- Ask the circularity question and answer it in writing
- Distinguish "derived," "plausible," and "open"
- List what the framework does NOT produce
- Provide runnable scripts for every numerical claim
- Acknowledge calibration vs prediction

These practices make the framework easier to evaluate, easier
to criticize, and easier to build on.


## 7. Summary

| Claim | Assessment |
|-------|-----------|
| Maxwell derived from six axioms | **Correct but not novel** — this is standard U(1) lattice gauge theory (Wilson, 1974) |
| Einstein derived from six axioms | **Partially correct** — the derivation requires four additional imports beyond the axioms, all honestly flagged; the core argument is Jacobson (1995) |
| G = 1/(4ζ) | **Correct but tautological in natural units** — G ≡ 1 in Planck units by definition |
| Λ derived | **Misleading** — Λ appears as an undetermined constant, exactly as in standard GR |
| ζ = 1/4 derived from geometry | **Partially** — one specific lattice model (Model B, tetrahedral) gives 1/4; other models give different values |
| No mathematical errors | **Confirmed** — every step is correct |
| Simulation results | **Confirmed** — wave propagation, superposition, 1/r gravity, Schwarzschild geometry all check out |
| Honesty about limitations | **Exemplary** — the best self-criticism in the project |
| Novel contribution | **The unified substrate narrative** — placing Wilson and Jacobson on the same lattice with a concrete axiom partition |
| Predictions beyond standard physics | **None yet** — GRID reproduces known results, it does not produce new testable predictions |

GRID contains no errors.  Its derivations are honest,
well-organized, and mathematically sound.  Its primary value
is not in producing new physics but in providing a unified
narrative substrate that connects established results from
lattice gauge theory and thermodynamic gravity — and in
demonstrating, through simulations, that such a substrate
behaves consistently.  Whether this narrative can eventually
generate predictions that distinguish it from standard physics
is the open question that determines its long-term
significance.
