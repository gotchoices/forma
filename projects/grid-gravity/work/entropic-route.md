# The entropic route — what "entropic" means, and where an entropic force stands

**Status:** Orientation note plus parked hypotheses. It (a) fixes the
vocabulary — energy, entropy, free energy — that the phrase "gravity is
entropic" depends on, (b) records the hypothesis that two particles attract
because being together is entropically favoured, with the one measurement the
repo has of it, and (c) records the corresponding hypothesis for charge. The
hypotheses are **parked, not dismissed**: each is recorded with the specific
obstruction it currently faces and what would reopen it.

Grades: **[standard]** (textbook physics), **[from the repo]**,
**[hypothesis]**, **[expectation]** (anticipated, not computed), **[open]**.

---

## 1. Three quantities that are easy to blur [standard]

- **Energy E.** "A system seeks low energy": a ball rolls downhill.
- **Entropy S.** The logarithm of the number of microscopic arrangements
  (microstates) consistent with what is observed. "A system maximizes entropy":
  it drifts toward the condition that can be realized in the most ways — *at
  fixed energy*.
- **Free energy F = E − T·S.** What a system in contact with surroundings at
  temperature T actually minimizes. At low T the energy term dominates (order);
  at high T the entropy term dominates (disorder).

"Seeks low energy" and "maximizes entropy" are therefore **not two phrasings
of one principle**. They are different, and frequently opposed; the free
energy is the compromise between them. Any argument of the form "the particles
move together because that state is preferred" has to say *which* quantity is
being extremized.

An **entropic force** is what results when the entropy term does the work:

<!-- F = T · dS/dx -->
$$
F \;=\; T\,\frac{dS}{dx} .
$$

The standard example is a stretched polymer: no spring pulls it back; there
are simply far more crumpled arrangements than straight ones, and thermal
agitation carries it toward them. Two signatures follow: an entropic force is
**proportional to temperature**, and it needs a **thermal bath** to act.

## 2. The two "entropic gravity" programmes [standard]

- **Jacobson (1995).** Apply the heat relation δQ = T·δS to small local
  horizons, take the entropy proportional to horizon *area*, take T to be the
  Unruh temperature seen by an accelerated observer — and the Einstein
  equations follow as an equation of state. Gravity is the thermodynamics of
  horizons.
- **Verlinde (2011).** Newton's law as an entropic force on a test mass near a
  "holographic screen": the screen holds a number of bits proportional to its
  area, each carrying ½kT, with T the Unruh temperature. The 1/r² arises
  entirely from the screen's area 4πr².

Both are about **entropy, not energy**. Verlinde's version in particular is
contested: a genuinely thermal force should disturb delicate quantum states
(the gravitational bound states of neutrons are the usual test case), and
whether the proposal survives that objection is debated.

**Where GRID stands [from the repo].** [grid/gravity.md](../../../grid/gravity.md)
is the Jacobson route: axiom A5 (S = ζ·A on any causal horizon) plus the
Clausius relation gives the Einstein equations with G = 1/(4ζ). The entropy in
that derivation is **horizon-area entropy**. It is *not* the entropy of two
particles at a given separation. The README of this project names the missing
piece: a mechanical account should *derive* the entropy law and the
microscopic dS/dt that the statistical route assumes
([grid/bounding-mechanisms.md](../../../grid/bounding-mechanisms.md)).

## 3. The inverse-square law is geometry [standard]

Newton's and Coulomb's *forces* both fall as 1/r²; their *potentials* fall as
1/r. The reason is the same in both cases and is not dynamical: a conserved
flux spreading through three-dimensional space is shared over a sphere of area
4πr². Any model in which a conserved quantity emanates from a source gets the
inverse square for free.

So the power law is not what distinguishes a good model of these forces. The
discriminating facts are:

- **sign** — gravity has one sign (always attractive); charge has two;
- **hierarchy** — gravity is weaker than electromagnetism by about 10³⁶
  between two protons;
- **couplings** — the dimensionless content of G and of α.

## 4. Hypothesis: two masses attract because "together" is entropically favoured [hypothesis]

**Statement.** Particles are standing waves on compact dimensions, located
along space. Two such particles far apart are "more organized" — take more
information to specify — than the same two close together. The lattice
therefore drifts toward bringing them together: a weak, long-range,
always-attractive tendency, identified with gravity.

**What the repo already has on this.**

- [grid/sim-gravity-2](../../../grid/sim-gravity-2/README.md) measured it
  directly. The scalar Laplace solve gives a clean 2D force exponent
  (p = 1.012). But the force computed from the **entropy profile** gave
  p = 0.17 with R² = 0.009 — no power law at all. The study's own conclusion:
  "the entropic force in Jacobson's derivation does not come from the static
  spatial gradient of local entropy." Its open item — "compute the total free
  energy as a function of defect position" — was never done. ([grid/STATUS.md](../../../grid/STATUS.md) summarizes it accordingly: the
  1/r law confirmed, a directly measured entropic force still open.)
- [grid-primitive ch. 4](../../grid-primitive/04-entropy-from-defects.md)
  derives a two-body force on the lattice, but from field *energy*
  (−dE_int/dr), and notes that it "does not depend … on temperature." The
  entropy content of that chapter is a separate object: a logarithmic
  "variance shadow" around a single pinned inclusion.

**The obstruction, as currently understood [expectation].** Forces that arise
from *fluctuations* between two inclusions in a field are second-order
effects: they go as the **square** of the field's Green's function G. In three
dimensions G ∝ 1/r, so such an interaction energy falls as 1/r² and its force
as 1/r³ — too fast. A 1/r *potential* is first-order: it needs a field that
the mass itself *sources*. That is consistent with the sim-gravity-2 null, and
it is why Jacobson's argument works where the two-body version stalls — his
entropy is attached to horizon area, not to the pair's configuration. This is
an expectation from standard results on fluctuation-induced forces; it has not
been computed for the GRID lattice.

**What would reopen it [open].** The free energy of two pinned inclusions as a
function of separation, in 3D, by Monte Carlo (the single-inclusion machinery
exists in grid-primitive's scripts). Either outcome is a clean result. A
second opening: an accounting in which separation changes a *horizon-like*
area rather than a pair configuration, which would reconnect to §2.

## 5. How this route meets the mechanical one

The two are levels of one stack (README, "Relationship to the statistical
account"): the README's first fail-fast option is *mechanical → entropy →
Jacobson* — a mechanism that does not itself produce a 1/r force field may
still produce entropy at the rate Jacobson's argument needs.

[Mechanism 3](sync-carrier-mechanism.md) offers a specific hook: in its
strong-field limit, the edges that lose lock with the surrounding lattice lie
on a *surface*, so their number scales with area — the form of S = ζ·A.
Whether counting those edges reproduces ζ, and whether their rate of change
supplies dS/dt, is **open**.

## 6. Hypothesis: charges attract or repel entropically [hypothesis]

**Statement.** Charge is the next order up from mass: a two-dimensional
standing wave, carrying mass *and* a signed, polarized winding
([metric-charge](../../metric-charge/)). Two opposite charges at a distance
are a low-entropy arrangement; annihilating (particle with antiparticle) or
sitting as close as possible (proton with electron) minimizes the information
needed to describe them, hence attraction. Two like charges are driven apart.

**Obstructions.**

- **Temperature.** An entropic force scales with T and needs a bath (§1). The
  Coulomb force between two charges in cold vacuum does neither.
- **Bookkeeping.** Erasing the information that distinguishes two particles
  *lowers* the entropy of that pair; by Landauer's principle the erasure costs
  energy and exports entropy to the surroundings. "Joining erases their
  information, therefore entropy rises" counts the wrong side of the ledger
  unless the surroundings are part of the model.
- **Assignment versus counting.** In the statement above, the entropies are
  *assigned* so as to reproduce the known directions (opposites attract, likes
  repel). A mechanism would *count* microstates as a function of separation
  and find those directions.
- **GRID already has the field.** Maxwell's equations follow from axiom A4,
  and Coulomb's law follows from Maxwell
  ([grid/maxwell.md](../../../grid/maxwell.md)). What is genuinely missing is
  at the level of *particles*: the energy E(r) of two knots at separation r,
  and what happens at r = 0 (pass through, annihilate, or stack) — exactly the
  unanswered questions of [metric-binding](../../metric-binding/) (theories
  2–3; open question 1).

**Fallback, and what would reopen it.** The energetic reading: opposite
windings co-locate because E(r) has its minimum there. That is
metric-binding's programme and does not need entropy. The entropic reading
reopens if a microstate count as a function of separation can be defined for
two windings on the lattice and yields a signed result.

For a different, non-entropic way of placing charge beside gravity — a signed
*additive* frequency offset against gravity's universal *fractional* one — see
[sync-carrier-mechanism.md](sync-carrier-mechanism.md) §12.

## 7. Note on atoms and bulk matter

The same line of thought extended to matter: a small positive core wrapped in
a much larger negative envelope; atoms aggregate; the electron envelopes keep
them apart. For the record:

- **Standard physics already fixes the scales [standard].** The atom's size is
  the Bohr radius, which is the electron's reduced Compton wavelength divided
  by α (about 137 times larger) — the factor α being the fingerprint of the
  electromagnetic coupling. The spacing of atoms in ordinary matter is set by
  electromagnetic bonding against Pauli and Coulomb repulsion. Gravity plays no
  part in cohesion below roughly asteroid scale. And electromagnetism is as
  long-range as gravity; it *appears* short-range only because signed charges
  neutralize each other — the shielding asymmetry of
  [sync-carrier-mechanism.md](sync-carrier-mechanism.md) §12.
- **"One quantum per mode" is not what GRID currently gives [from the repo].**
  [grid-quantization](../../grid-quantization/05-why-light-is-quantized.md)
  derives a *bosonic* ladder — 0, 1, 2, … quanta per mode.
  [studies/R56](../../../studies/R56-electron-shells/findings.md) (F3) found
  that Pauli exclusion "is not a geometric consequence of packing"; its
  [README](../../../studies/R56-electron-shells/README.md) lists an
  interference-based origin (two co-located tori with the same winding
  cancelling) as "theoretical, not yet attempted." Exclusion remains an input.
- Atoms in the framework: [qa/Q105](../../../qa/Q105-atoms-as-cross-sheet-modes.md)
  (partially negative) and [qa/Q107](../../../qa/Q107-wave-translation-of-atomic-physics.md)
  (retains the standard quantum treatment in a Coulomb potential).

## Grades summary

- **[standard]** §1–§3; the scales in §7.
- **[from the repo]** GRID's gravity is Jacobson's, with horizon-area entropy
  (§2); the sim-gravity-2 entropic measurement was null (§4); exclusion is an
  input (§7).
- **[hypothesis]** Two-body entropic gravity (§4); entropic charge force (§6).
  Both parked with named obstructions.
- **[expectation]** Fluctuation-induced forces scale as G² → 1/r³ in 3D (§4).
- **[open]** Free energy versus separation in 3D; area-count of slipped edges
  versus ζ and dS/dt (§5); a microstate count for two windings (§6).
