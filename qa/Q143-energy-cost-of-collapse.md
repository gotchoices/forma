# Q143. If |ψ|² is an energy density, what does collapse cost?

**Status:** Open — a framework-level commitment, unresolved. The
cost is forced and has exactly two payment options, which are
mutually exclusive.
**Related:**
  [`projects/grid-fields/`](../projects/grid-fields/) (where the fork is catalogued as V3/V4),
  [`projects/grid-matter/work/born-detection-theorem.md`](../projects/grid-matter/work/born-detection-theorem.md) (the derivation that creates the debt),
  [`projects/grid-matter/work/thesis-wave-until-interaction.md`](../projects/grid-matter/work/thesis-wave-until-interaction.md),
  [Q135](Q135-free-information-and-decoherence.md) (decoherence as promotion event),
  [Q121](Q121-uncertainty-as-ma-phase-ignorance.md) (uncertainty as phase ignorance),
  [Q110](Q110-entanglement-via-aleph-fiber.md) (entanglement via the ℵ fibre)

---

## 1. The question

Forma does not postulate the Born rule. It **derives** it, from the
identification

> |ψ|² = energy density

together with whole-quantum absorption. That is a genuine result
and one of the framework's better ones.

It also incurs a debt that no other interpretation of quantum
mechanics carries. In the standard account, the wavefunction spread
across a region is **probability**, and nothing physical is out
there to move when a detector fires. In forma, something physical
*is* out there: energy. A photon from a distant star arrives as a
wave wide enough to cover both arms of a stellar interferometer —
in practice, metres to kilometres, and for the coherence argument,
far more. When one atom absorbs it, that atom gains the whole ℏω in
femtoseconds.

**So: where was the energy, and how did it get to the atom?**

This entry records the structure of the problem and the proof that
one tempting escape is closed.

## 2. The tempting escape: let it cancel

The intuitive rescue is interference. Two sine waves of equal
frequency and opposite phase sum to nothing. If the photon's remote
tail could be made to cancel against the detecting electron's own
wave, no energy would have to travel anywhere — it would simply
cease to be present where it is not wanted, and be present where it
is.

The underlying intuition needs testing first, because it contains a
question worth answering in its own right: **in a real destructive
interference, where does the energy go?**

## 3. Where the energy goes in a real cancellation

Energy is never destroyed by interference. A laboratory realises
destructive interference in exactly two ways, and they have
different answers.

**Case 1 — the waves are already in flight.** Tune a Michelson
interferometer to a dark output. The two beams cancel there. The
light leaves by the **other port**. A beam splitter has two
outputs; darkening one necessarily brightens the other, and no
setting of the mirrors darkens both. That is forced by the splitter
being lossless, not by alignment. The energy was **redistributed**.

**Case 2 — the waves are still attached to their sources.** Drive
two antennas a small fraction of a wavelength apart in antiphase.
The radiated field genuinely cancels in every direction. Here the
energy was **never emitted**: each antenna's *radiation resistance*
(the effective resistance representing power leaving as radiation)
is modified by the other's presence, the mutual term cancels the
self term, and the transmitters draw less power from their
supplies. In circuit terms: two sources in antiphase across a load
pass no current, deliver no power, and do not drain.

## 4. Why "cancel everywhere" is structurally unavailable

Energy density goes as |ψ|², which is quadratic, while the wave
equation is linear. So the energy of a sum is not the sum of the
energies:

> |A + B|² = |A|² + |B|² + 2·Re(A*B)

The last term is the interference. Integrate over all space: for
any two wave solutions that are **orthogonal** — different
wavevector, direction, or frequency — that integral is exactly
zero. Total energy is additive even though local energy density is
not. This is a theorem, not a bookkeeping convention.

Cancelling everywhere would require the cross term to consume both
energies, which forces B = −A exactly: same frequency, same
wavevector, same direction, same envelope. Which gives:

> **Two waves that cancel everywhere are the same mode, and so can
> never have been separate and then met.** Co-propagating waves
> travel together at the same speed and never approach each other.
> To superpose them they had to be created that way — Case 2 — and
> then the energy was never in the field at all.

There is no third case. Energy that *was* distributed in the field
does not become absent; it either moves elsewhere in the field, or
it never left the source. **The escape in §2 is closed.**

## 5. What survives: concentrate, at finite speed

Interference can still *redistribute*. Cancelling on the tails and
adding at the locus is Case 1 — perfectly allowed, no objection in
principle. But interference buys the **pattern**, not the
**speed**. Energy density obeys a continuity equation:

> ∂u/∂t + ∇·S = 0

with u the energy density and S the energy flux. Energy cannot
vanish here and appear there; it must **flow**, bounded by the wave
speed. Concentrating a wave of extent L onto its locus takes a time
of order L/c.

This is a sharper statement of the objection than *"collapse would
be superluminal."* The obstruction is not an imported relativistic
prohibition that one might hope to negotiate with. **Locality of
energy transport is a theorem of the wave equation itself**, and it
arrives with the dynamics. A framework that keeps the wave equation
keeps the obstruction.

## 6. The escape that looks like it survives, and does not

If nearly all of the energy already sat at the locus — a sharply
peaked profile with faint side lobes — then collapse would have
almost nothing to gather, and L/c would be small.

The two-slit experiment closes this. **Fringe visibility** measures
how deep the dark bands of an interference pattern run, on a scale
where 1 is perfect:

<!-- V = 2 sqrt(I1 I2) / (I1 + I2) -->
$$
V = \frac{2\sqrt{I_1 I_2}}{I_1 + I_2}
$$

with I₁ and I₂ the intensities arriving from the two slits.
Single-photon two-slit experiments routinely measure V > 0.9, which
requires I₁ ≈ I₂ to within roughly a factor of 1.5. The energy must
be split near 50/50 between two macroscopically separated places.

**The experiment that motivates the spread wave is the same
experiment that forbids the energy from being mostly
concentrated.** This is worth stating plainly because it removes
the most appealing engineering fix.

## 7. The other shape: relabelling instead of moving

A different proposal: nothing moves, and the remote tail is
**relabelled** — the former photon tail simply becomes part of the
excited electron's own field, in place. This is closer to standard
absorption, where the photon mode is depopulated as the atom's mode
is populated.

It fails two tests.

*The second detector.* If the energy is still physically out there,
another atom can absorb it. That is exactly what never happens —
one photon, one click. Committing the remote energy to the first
absorber is a non-local correlation, and correlations carry no
energy; entanglement does not move joules.

*Local accounting.* Detectors measure whole-quantum absorption, so
the absorbing atom must gain the entire ℏω. If part of that energy
remains located far away, then |ψ|² is no longer the **local**
energy density — which is the identity the Born derivation runs on.
The proposal saves the energy by dissolving the premise that made
the derivation work.

## 8. The fork, stated as one trade

Collecting §4–§7: the two positions in
[grid-fields V4](../projects/grid-fields/) are not two independent
options with different price tags. They are **one trade seen from
two sides.**

| | Position | What it keeps | What it costs |
|---|---|---|---|
| **A** | Energy is genuinely spread | The Born derivation stands as written | The framework must declare non-local energy transport as a real feature — no local mechanism remains, since §4 removes cancellation and §5 bounds flux |
| **B** | Wheeler–Feynman / transactional: nothing is in flight | Strict locality; no re-gathering problem | \|ψ\|² is not an energy density for a photon in flight, and the Born derivation must be rebuilt from something else |

Every other reading of quantum mechanics escapes this problem by
denying the premise: in the standard account the remote energy was
never there, only probability was. **Forma gave that escape up
deliberately, in order to derive Born rather than postulate it.**

So the derivation and the collapse problem are the same commitment
seen from two sides. The energy problem is the **price** of the
Born-rule result, not an incidental difficulty standing beside it.
Any future collapse proposal in forma has to declare which side of
this it is on.

## 9. What would settle it

- **For A:** a mechanism that transports energy faster than c
  *without* producing a signalling channel — i.e. one whose
  observable consequences are confined to correlations. This is a
  tall order but not obviously impossible; quantum mechanics
  already has non-signalling non-locality, and the question is
  whether forma can have a non-signalling *energetic* version.
  Alternatively, A can simply be adopted with the cost declared.
- **For B:** an alternative route to the Born rule that does not
  pass through energy density — for example from the geometry of
  whole-quantum absorption alone, or from the statistics of
  threshold-crossing in the detector. Note that forma's own
  [threshold-theory primer](../primers/threshold-theory.md) is
  adjacent to this.
- **Discriminating measurement:** none yet identified. The two
  positions are, so far as this entry can tell, empirically
  equivalent — which is itself worth recording, since it makes the
  choice a matter of framework coherence rather than evidence.

---

*Appeal classification: §3, §4, §5, §6, §7 are **standard
physics** — interferometer energy balance, mutual radiation
resistance, the orthogonality theorem, the continuity equation, and
fringe visibility are all textbook. §1, §8 and §9 are
**forma-specific**: the debt exists only because forma identifies
|ψ|² with energy density rather than probability.*

*Connects to: grid-fields (V3, V4), grid-matter's Born derivation,
Q135 (decoherence), Q121, Q110*
