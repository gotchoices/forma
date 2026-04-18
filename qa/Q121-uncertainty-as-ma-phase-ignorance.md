# Q121. Quantum uncertainty as ignorance of Ma circulation phase

**Status:** Open — speculative; sits in the Hestenes / zitterbewegung tradition
**Related:**
  [Q82](Q82-entanglement-as-ma-geometry.md) (entanglement as Ma geometry),
  [Q41](Q41-wave-language-12-geodesic.md) (wave-language of the (1,2) geodesic),
  [Q42](Q42-compton-scale-beat-envelope.md) (Compton-scale beat envelope)

---

## 1. The question

Quantum mechanics treats the wavefunction as a probability
amplitude: |ψ|² gives the probability density of finding a
particle in a region.  The probabilistic content is taken as
fundamental — a feature of nature, not an expression of
ignorance about some underlying state.  Einstein spent
decades arguing the opposite: "God does not play dice."
He suspected the probabilities hide a deterministic
substrate we haven't found.

MaSt treats particles as real physical objects — standing
electromagnetic waves circulating on Ma.  If that
circulation is real, its phase is a real dynamical variable.
The question:

**Could the probabilistic content of QM simply be ignorance
of the instantaneous phase of Ma circulation?**

## 2. The conjecture

In model-E's picture, the photon in an electron mode
circulates on the (1,2) geodesic of Ma_e at speed c,
completing a cycle every Compton period (~10⁻²¹ s for the
electron).  At any given instant, the photon is *somewhere*
on its trajectory — definite position, definite phase — but
the observer cannot resolve that without a measurement that
perturbs the system.

Probability enters because:

- Before measurement, the instantaneous phase is **definite
  but unknown**.
- Measurement interacts with the photon at whatever phase
  it happens to be in.
- Over many repetitions, the outcome distribution follows
  |ψ|².

In this picture, ψ is an *amplitude envelope* over phase.
Born probabilities come from integrating this envelope
against a uniform phase distribution.  The randomness is
epistemic, not ontic.

## 3. Standard-physics anchor: Hestenes and zitterbewegung

This is the core move of David Hestenes' **zitterbewegung
interpretation** of the Dirac equation.  Schrödinger (1930)
noticed the Dirac equation contains a term describing a
particle trembling at frequency 2mc²/ℏ — "zitterbewegung."
Hestenes argued this trembling is a real circular motion at
the Compton scale, and the Dirac equation's probabilism
arises from ignorance of its phase.  His geometric-algebra
reformulation makes spin and the Dirac wavefunction
expressions of a rotating local frame.

MaSt is a natural home for this tradition.  In MaSt, the
zitterbewegung **is** the photon's circulation on the (1,2)
geodesic of Ma_e.  The electron is a real rotating object;
we just cannot resolve its instantaneous phase with any
laboratory measurement — the Compton period is 11 orders of
magnitude faster than our best clocks.

## 4. The hard obstacle: standing waves have no observable phase

A pure stationary mode

<!-- psi(theta, t) = phi(theta) exp(-i E t / hbar) -->
$$
\psi(\theta, t) = \phi(\theta)\, e^{-iEt/\hbar}
$$

has only an overall time-phase.  In standard quantum
mechanics, the overall phase of a single eigenstate is
**not observable** — only phase *differences* between
superposed eigenstates matter.  A system in a single energy
eigenstate has no meaningful dynamical phase; it sits there.
That is what "stationary state" means.

If MaSt modes are taken as fundamental, the phase-ignorance
story fails at the starting line: there is no phase to be
ignorant of.

**The loophole** — which the MaSt framework must invoke —
is that the **circulating photon is more fundamental than
the mode description**.  A standing wave is a superposition
of two counter-propagating components (one photon going
around the torus one way, plus the same photon going the
other way).  The photon has a real, instantaneous position
on its orbit; the mode description averages over that
position and hides it.

If physics is done at the level of the circulating photon
rather than the mode, phase becomes a real dynamical
variable again.  This is a non-trivial commitment:

- Model-E's quantitative successes (particle spectrum,
  winding-number structure, 18/20 spin-correct modes) come
  from the mode picture.
- Reconciling mode-based spectrum predictions with a
  photon-based dynamical picture is an open program, not a
  solved problem.

The Williamson-van der Mark (1997) starting point
[`reference/WvM-summary.md`](../reference/WvM-summary.md)
already treats the electron as a confined photon — a
dynamical object with instantaneous position on a closed
path.  So the MaSt lineage naturally favors the photon-as-
fundamental side.  The mode description is then a
calculational tool, not ontology.

## 5. What a working version would need to demonstrate

A hypothesis becomes a theory when it reproduces what is
measured.  For phase-ignorance to actually replace QM's
probabilistic postulate, the Ma dynamics must produce:

1. **Born rule.**  A uniform distribution over phase must
   reproduce |ψ|² for projection observables.  In simple
   cases (harmonic oscillator, free particle) this works —
   the squared amplitude envelope IS the probability
   density.  It must be verified mode-by-mode on the full
   T⁶ structure.

2. **Interference.**  Double-slit patterns must fall out
   from phase distributions plus constructive/destructive
   addition of mode amplitudes.  This is not automatic —
   naive hidden-variable models typically get single-slit
   distributions but fail interference.

3. **Contextuality.**  Kochen-Specker (1967) proves that
   quantum observables cannot have values pre-assigned
   independent of measurement basis.  A phase-ignorance
   model must have the "hidden phase" itself depend on
   context — the phase meaningful for one measurement
   must not be commensurate with the phase meaningful for
   another.  Hestenes argues this is exactly what the
   Clifford-algebra structure of spin provides.  Whether
   MaSt's T⁶ phase structure does the same has not been
   shown.

4. **Entanglement.**  Two particles sharing a phase
   relationship on Ma should reproduce Bell correlations.
   This is the same calculation Q82 §4 flags as the major
   open problem.  A phase-ignorance picture and a shared-
   Ma-wave picture stand or fall together on this test.

5. **Measurement dynamics.**  A projection operation must
   emerge from the interaction of the photon's circulation
   with a detector, not be added as a separate postulate.
   This is the deepest demand and the one no realist
   interpretation has fully met.

## 5a. Geometric motivation: shear and projection

Why is **projection** the right operation for measurement?
A simple geometric picture scales directly from R² to
Hilbert space:

- **Orthogonal axes carry independent coordinates.**
  Motion in x is silent along y.  Any state decomposes
  cleanly as an x-component times a y-component.
- **Sheared axes (non-orthogonal) couple.**  Motion in y
  has a component along x and vice versa.  A state cannot
  be split into independent x and y parts; it must be
  described jointly.  To ask "what is the x-component of
  this state?" is to **project** onto the x-axis — and the
  projection necessarily discards some of the original
  content.

Quantum observables translate this one-for-one:

- Two **commuting** observables have aligned eigenbases —
  orthogonal, independent axes in Hilbert space.  No
  projection loss between them.
- Two **non-commuting** observables have misaligned
  eigenbases — a shear in Hilbert space.  The commutator
  [A, B] ≠ 0 quantifies the misalignment (Heisenberg's
  uncertainty relation is a bound on this misalignment).
- Measuring A projects the state onto A's eigenbasis.
  That basis does not align with B's, so the state's
  B-component is not preserved — post-measurement,
  B is newly uncertain.

In MaSt, the off-diagonal metric entries (s_e, s_p, σ_ep,
and the Ma–S KK couplings) are literal metric shears.  The
quantum projection operation is the Hilbert-space analog
of taking components along these sheared axes.  One slogan
captures the full chain:

**Shear couples axes.  Coupled axes produce non-separable
modes.  Non-separable modes require joint projection for
measurement.  Projection is what actualizes individual
outcomes.  Ignorance of the instantaneous pre-projection
phase is what makes outcomes probabilistic.**

If phase-ignorance is what produces Born probabilities
(§2), projection is what actualizes outcomes (Q82 §4.2),
and shear is the common geometric root that makes both
necessary.  Q82 §2.6 develops the same unification from the
entanglement side; here it closes the loop on the
uncertainty side.

## 6. Why this is tied to Q82 (entanglement)

Q82 argues entanglement is shared phase structure on Ma.
Q121 argues quantum uncertainty is ignorance of instantaneous
phase on Ma.  These are **two sides of one proposal**:

- The substrate is the same (the Ma wave / photon
  circulation).
- If the phase is a real hidden variable (Q121), then
  pairs of particles with locked phase relationships
  naturally produce correlated measurement outcomes (Q82).
- If the shared structure projects under measurement (Q82
  §4.2), then the individual outcomes are probabilistic
  because the joint phase of the shared state is unresolved
  until measurement (Q121).

They must be solved together.  A realist geometric
interpretation of QM that explained entanglement but left
single-particle probabilities mysterious (or vice versa)
would be incomplete.

## 7. Relationship to standard interpretations

| Interpretation | What is probabilistic | Compatible with MaSt phase-ignorance? |
|----------------|----------------------|--------------------------------------|
| **Copenhagen** | Measurement outcomes (fundamental) | No — denies deterministic substrate |
| **Many-worlds** | Branch selection (epistemic) | Partly — but MaSt has single-world framing |
| **Bohmian** | Position (hidden, nonlocal) | Yes — close kin; Ma replaces configuration space |
| **Hestenes/zitterbewegung** | Phase of real rotation (hidden) | **Yes — this is the natural partner** |
| **GRW / objective collapse** | Collapse events (physical) | No — collapse is added dynamics |

MaSt's geometric substrate + phase-ignorance interpretation
sits closest to the Hestenes line, with Bohmian mechanics as
a more-established mathematical cousin.

## 8. Open sub-questions

1. **Can the photon-fundamental picture reproduce model-E's
   eigenspectrum?**  The mode picture produces correct
   masses via winding numbers.  Does a dynamical photon on
   the (1,2) geodesic reproduce the same spectrum as a
   resonance condition?  If not, the two pictures
   disagree on something measurable.

2. **How does measurement couple to phase?**  A detector
   must be modeled as a coupling term that catches the
   photon at its instantaneous phase.  What is the
   geometric form of that coupling?

3. **Does phase decoherence give the observed decoherence
   rates?**  The decoherence timescale for real quantum
   systems is well measured.  A phase-ignorance picture
   must predict comparable rates from environment-mode
   scrambling of the Ma phase.

4. **Does the photon's phase traverse all of Ma, or only a
   geodesic?**  The (1,2) geodesic is a specific closed
   loop.  The "phase" could mean where on this loop the
   photon is, or it could be a richer higher-dimensional
   object.  This affects what "phase distribution" means
   quantitatively.

## 9. Caution

This is a philosophical interpretation at a high speculative
level.  Historically, every attempt to reduce QM's
probabilism to ignorance of hidden variables has stalled on
contextuality, Bell violations, or measurement mechanics.
Hestenes' program is the most developed and has not yet
produced a complete, uncontroversial derivation of QM from
zitterbewegung.

MaSt inherits the same risks.  Phase-ignorance is a
suggestive geometric story for *why* QM is probabilistic,
but it is not a theorem that the probabilities match.
Until someone computes Born statistics + Bell correlations +
interference + contextuality from MaSt phase dynamics, the
hypothesis is recorded as a direction, not a result.

The value of the framing is that it turns vague
philosophical disputes into concrete mathematical tasks
set on a specific geometry.  Q82 and Q121 together define
a research program, not a claim of success.
