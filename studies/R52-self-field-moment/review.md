# R52 Review: Anomalous magnetic moment from torus self-field

**Reviewed:** 2026-04-08
**Status at review:** Track 1 complete, Tracks 2–5 pending

---

## 1. What R52 is trying to do

R52 asks: can the deviation between a particle's measured
magnetic moment and MaSt's bare prediction (n₂ × magneton)
be explained by the Coulomb self-field of the torus mode
acting back on the wave?

The two test cases:

| Particle | Mode | MaSt bare | Measured | Residual |
|----------|------|-----------|----------|----------|
| Electron | (1,2) | 2 μ_B | 2.00232 μ_B | +0.116% |
| Proton | (1,3) | 3 μ_N | 2.793 μ_N | −6.9% |

The central hypothesis: the sign of the residual (additive
for electron, subtractive for proton) is determined by the
mode's phase structure — (1,2) two-phase vs (1,3) three-phase.

## 2. What Track 1 established

Track 1 produced a genuine result: the classical 3D
current-loop integral does NOT give the bare moment.  It
gives values 8–800× too large, scaling as R² instead of ℏ.
The bare moment is purely quantum (μ = eℏn₂/2m),
independent of the 3D embedding geometry.

This falsified the original physical picture described in
the README — the one where the 3D Coulomb field of the
embedded charge distribution acts back on the current.
The bare moment doesn't come from a 3D current, so a 3D
self-field correction to a 3D current is the wrong
calculation.

The findings pivoted to quantum perturbation theory as the
correct approach for Tracks 3–4.  This pivot is significant
and the README has not been updated to reflect it.

## 3. Problem: the MaSt baseline needs flagging

MaSt's "bare moment = n₂ × magneton" is a framework-
specific prediction, not a standard physics result.  For the
electron, it happens to agree with the Dirac value (g = 2),
so MaSt and standard physics share the same baseline and
the same anomaly.  For the proton, they diverge:

| Framework | Proton bare | Measured | Deviation |
|-----------|------------|----------|-----------|
| Standard (Dirac) | 1 μ_N | 2.793 μ_N | +179% |
| MaSt (n₂=3) | 3 μ_N | 2.793 μ_N | −6.9% |

These are computing residuals from different baselines.
R52 is internally consistent within MaSt, but the README
should state this explicitly.  A reader familiar with
standard physics will otherwise assume R52 is trying to
explain the standard proton anomaly (+179%), which it is
not.

A recommended addition to the README: "The MaSt bare
moment for the proton is 3 μ_N (from n₂ = 3), not the
Dirac value 1 μ_N.  The residual R52 computes is the
deviation from MaSt's own prediction."

## 4. Problem: perturbation theory doesn't test MaSt

This is the most fundamental issue with Tracks 3–4 as
currently framed.

The planned computation: expand the torus mode in
flat-torus eigenstates, compute ⟨m|H'|n⟩ matrix elements
for the self-potential V, sum the first-order corrections
to the angular momentum expectation value.

This is standard quantum perturbation theory applied to
MaSt's geometry.  The torus shape is the only MaSt input;
everything else (the Hamiltonian, the perturbation
expansion, the eigenstate basis, the expectation values) is
borrowed from standard QM.

The problem: if MaSt is trying to DERIVE quantum mechanics
from lattice physics (GRID), then using quantum perturbation
theory to compute a MaSt prediction is circular.  You are
borrowing the framework you are trying to replace.

**What this computation actually tests:** "is the MaSt torus
geometry consistent with the known anomalous moment, when
analyzed with standard QM tools?"  This is a consistency
check, not a derivation from first principles.

**What a genuine MaSt derivation would look like:** the GRID
lattice has a scattering rule at each node.  A charged
standing wave on the torus creates a phase defect (Coulomb
field) in the ambient lattice.  The defect back-reacts on
the wave through the scattering rule.  The back-reaction
shifts the effective angular momentum of the mode.  The
shift IS the anomalous moment.

This would be a lattice-native computation: propagate a wave
on the discrete torus embedded in the discrete lattice,
with the wave interacting self-consistently with its own
radiated field, and measure the resulting moment.  No
perturbation theory, no borrowed QM formalism.  The lattice
action and scattering rule are the only inputs.

This computation is substantially harder than perturbation
theory.  No existing simulation in the project (including
sim-maxwell) has computed a self-consistent standing wave on
an embedded torus interacting with its own field.

## 5. Problem: F5's "reservoir" argument

F5 interprets the failed classical formula as a "reservoir
of 3D field angular momentum" that the perturbation couples
to.  The argument: classical/quantum ratio ≈ 100, and
α × 100 ≈ 1, matching the proton's −7%.

This is post-hoc dimensional analysis using the output of
a wrong calculation.  F2 established that the classical
current-loop integral computes a "different physical
quantity" that doesn't describe the standing wave.  It
cannot then be repurposed as a reservoir whose magnitude
is physically meaningful.

Recommendation: remove F5 or replace it with a clear
statement that the magnitude prediction for the proton is
not yet derived.

## 6. The (1,3) presupposition

The central hypothesis — sign of anomaly correlates with
phase structure — depends entirely on the proton being a
(1,3) mode.  If the proton is (1,2), both particles are
two-phase and the sign difference needs a different
explanation.  If (3,6), the phase structure is different
again.

R52 should note this dependency explicitly and state what
each alternative assignment would predict.

## 7. Recommendations

### 7.1 Rewrite the README physical picture

The current README describes the pre-Track-1 picture (3D
Coulomb back-reaction on the current loop).  Track 1
falsified this.  The README should be updated to reflect the
post-pivot framing: quantum perturbation theory of the
self-potential on the flat torus.

### 7.2 Frame Tracks 3–4 honestly

Label them as consistency checks, not derivations.  The
question they answer is: "does standard QM applied to the
MaSt torus geometry reproduce the known anomaly?"

- If yes (correct sign and magnitude): the MaSt geometry is
  consistent with observation.  Encouraging, but not proof
  that MaSt produces the anomaly — standard QED also
  produces it through a different mechanism.

- If no (wrong sign or magnitude): the MaSt geometry is
  inconsistent with observation at this level.  This would
  be a genuine negative result.

Either outcome is informative.  But the framing should not
claim "MaSt derives the anomalous moment" when the
derivation uses standard QM machinery.

### 7.3 Note the lattice-native computation as the real goal

The computation that would genuinely test MaSt is the
lattice self-consistent solve described in §4 above.  This
should be noted as a future goal (possibly a separate study)
that would supersede the perturbation-theory approach.

### 7.4 Decouple electron and proton

The electron calculation is cleaner: same baseline as
standard physics, perturbative regime, textbook QED answer
to compare against.  Run it first.  If it works, the proton
calculation (non-perturbative, different baseline, (1,3)
presupposition) has a stronger foundation.

### 7.5 Drop or revise F5

Replace the "reservoir" interpretation with an honest
statement that the proton anomaly magnitude is not yet
predicted.  Getting the sign right would be a meaningful
result on its own.

### 7.6 Add baseline clarification

Add a short section to the README explaining that MaSt's
bare moment differs from Dirac's for the proton, and that
R52 computes the residual from MaSt's baseline.

---

## 8. Net assessment

The core question is worth investigating.  The technical
approach (Tracks 2–4) is computationally sound even if it
doesn't constitute a first-principles MaSt test.  Track 1
produced a genuine result.

The main issues are framing, not substance:

- The README describes a picture that Track 1 invalidated
- The computation borrows standard QM without acknowledging
  the circularity
- F5 uses a wrong result as evidence
- The MaSt-specific baseline is not flagged for readers

A revised README that honestly frames Tracks 3–4 as
consistency checks (not derivations), flags the baseline
difference, and notes the lattice-native computation as the
eventual goal would put R52 on solid footing.

The study should proceed — but with clear eyes about what
it can and cannot establish.
