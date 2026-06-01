# Review: Ch. 3 — The modes of light

Checked against `scripts/band_structure.py`,
`scripts/run_recirculation.py` (`bound`, `circ`),
`scripts/mode_projection.py`, `scripts/scale_invariance.py`,
`scripts/loop_scaling.py`, and ch. 2.

Note up front: §3.3 cleanly incorporates the two corrections from
[work/chapter-outline-review.md](work/chapter-outline-review.md) — the
ω = 0 bound state is *not* "mass-like," and the ~½ is *not* the ZPE ½.
Those are no longer issues; remaining items below.

## Errors / overstatement

**1. §3.2 "the dispersive bands are the free photons" overstates.** The
chapter identifies all **four** dispersive bands with "free light," but
a photon has **two** transverse polarisations, not four. The honeycomb
unit cell has two sites, so a natural decomposition is
2 helicities × 2 sublattices = 4, giving doubled photon branches — but
the chapter doesn't say so, nor does it address whether any of the 4
are longitudinal/gauge modes (as in continuum QED). Specify which of
the 4 dispersive bands carry the 2 photon polarisations and what the
others are, or refer to [fields.md](../../grid/fields.md) if that
settles it.

## Cross-chapter consistency

**2. Contradicts ch. 2 §2.1 on persistence.** Ch. 2 argues a static
disturbance "cannot persist" (driven toward its own inversion by −1/3).
This chapter's §3.3 makes the ω = 0 flat-band CLS a load-bearing
*persistent* static mode. The reconciliation — non-symmetric
disturbances oscillate; the symmetric (breathing) mode is the static
exception, exactly the ω = 0 flat band — is mathematically simple, but
neither chapter says it. Ch. 3 §3.3 should at least note that the
demonstrated CLS is exactly the exception ch. 2's argument elided. (See
[02-review.md §1](02-review.md).)

**3. Inconsistent with ch. 2 §2.4 on "the photon."** Ch. 2 identifies
the per-junction helical eigenmodes (1, ω, ω²), (1, ω², ω) with "the
photon" that "oscillates and propagates." Those modes are at **ω = π**
— the *other* flat band, not propagating. This chapter rightly puts
the photon in the dispersive bands. The two chapters use "photon" for
two different objects; the helical decomposition is the polarisation
*basis* of the dispersive bands, not the modes themselves. Ch. 3
inherits the conflict without resolving it. (See
[02-review.md §2](02-review.md).)

## Material omissions

**4. §3.4 "every mode is an exact harmonic oscillator (P2)" — classical,
not quantum.** Linear dynamics ⇒ each mode evolves as a sinusoid with
*continuous* amplitude — a *classical* harmonic oscillator. A reader
who knows QM can read "harmonic oscillator" as the quantised ladder
(which is P3, ch. 5). One sentence — "classical, continuous-amplitude
oscillator; the quantum ladder is P3" — fixes it and protects the next
chapter from being misread as already-quantum here.

**5. Missing connection: ω = 0 flat band ↔ ch. 2's symmetric (1, 1, 1)
breathing mode.** They are the same kind of object (a static symmetric
configuration that is an eigenmode of the rule with eigenvalue +1). The
chapter introduces the flat band only via the density-of-states detector
and never names the junction-level origin from ch. 2's cube-root basis.
A single sentence linking "the ω = 0 flat band is the lattice version
of ch. 2's symmetric breathing mode" would unify the narrative and also
do half the work of fixing item 2 above.

## Imprecisions

**6. §3.3 "a static excitation carries zero energy (E = ℏω = 0)" is
correct under the ω-as-frequency reading, but quietly invokes ℏω before
ℏ has been introduced (ch. 4) and before quantisation has been argued
(ch. 5).** Reads as a slight forward reference. A neutral phrasing —
"carries no oscillatory energy" or "the wave-energy measure vanishes
for a static field" — avoids leaning on ℏω here.

**7. §3.5 "real light has wavelengths vastly longer than a lattice
cell, so across any observable range the dispersion is scale-free."**
True under the standard "cell = Planck length" identification (ch. 4
§4.4), but that identification is itself "a consistency, not a proof"
per ch. 4 §4.4. The chapter quietly assumes it. Worth one clause
("under the Planck-cell identification of ch. 4 §4.4") to make the
dependency visible.

---

## Author response

Integrated all seven items. Notes:

- **Item 1 (4 dispersive bands vs 2 polarisations).** Identified the
  *lowest acoustic* band as the photon (the one whose 0.41 slope ties
  back to ch. 2) and named the other three as "additional propagating
  modes" with interpretation flagged as open (longitudinal / gauge /
  sublattice-doubled), rather than committing to the review's
  2-helicities × 2-sublattices hypothesis without checking it.
  Honest-uncertain rather than overcommitted; this is the most
  defensible move until fields.md or a separate computation pins it
  down.
- **Items 2 and 5** (contradiction with ch. 2; missing ω=0 ↔ symmetric
  breathing link). Handled together: §3.3 now says the ω = 0 flat band
  *is* the lattice form of ch. 2's (1, 1, 1) breathing mode and is
  "exactly the static exception §2.1's 'cannot persist' argument set
  aside." Half does the work of fixing item 2 as the review predicted.
- **Item 3** (inconsistent with ch. 2 on "the photon"). Resolved upstream
  in ch. 2 (helical eigenmodes are the polarisation basis, not the
  propagating photons themselves); ch. 3 is now consistent.
- **Item 4** (classical vs quantum harmonic oscillator). Inserted
  "classical, continuous-amplitude" and the explicit "the *quantum*
  ladder of integer occupation is a separate piece (P3), addressed
  later in the arc."
- **Item 6** (E = ℏω forward reference). Replaced with "carries no
  oscillatory energy (its wave-energy measure vanishes)."
- **Item 7** (cell = Planck identification implicit). Now explicit:
  "Under Chapter 4 §4.4's identification of the lattice cell with the
  Planck length (a *consistency* of the framework, not a theorem)…"
  — preserves the chain of dependency and the honest grading.
