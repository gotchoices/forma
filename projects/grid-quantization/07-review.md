# Review: Ch. 7 — The honest ledger

Checked against chs. 1–6, the reviews of those chapters (in particular
the integrations recorded in [05-review.md](05-review.md) and
[06-review.md](06-review.md)), `README.md`, and the work files
referenced.

Ch. 7 is an accounting chapter: it does not introduce new claims, it
consolidates what the arc has graded. As such, most of its content is
inherited and faithful. The ledger has visibly absorbed several of the
prior chapter-review items — the **"classical" qualifier on P2** (cf.
[03-review.md §4](03-review.md)), the **universality-of-ℏ-as-automatic**
remark (cf. [04-review.md §3](04-review.md)), the **phase-dial as
formal anchor for §5.0** (cf. [05-review.md §1](05-review.md)), the
**zigzag-cancellation caveat on (2/3)¹²** (cf.
[06-review.md §4](06-review.md)), the **"shared input" qualifier on
"shared root"** (cf. [06-review.md §5](06-review.md)), and the
**per-edge→per-mode bridge as named open work** (cf.
[06-review.md §1](06-review.md)).

Items below are what the ledger still misses or mis-inherits.

## Material omissions

**1. The state-model question is not in the open-probes list.** The
prior reviews — [01-review.md §5–6](01-review.md),
[05-review.md §1, §9](05-review.md),
[06-review.md §2](06-review.md) — all converge on a single
unresolved question: is the canonical substrate the **continuous
compact phase θ ∈ S¹** ch. 1 §1.2 introduces, or the **finite-alphabet
ℤ_d dial** ch. 5 §5.0 and ch. 6 §6.6 actually use? It is load-bearing
for the bounded-substrate scaling (chapter 5), the 1/3-obstruction
motivation for sigma-delta (chapter 6 §6.6), and the bounded-ladder
prediction (§7.3). §7.5 lists three open probes but not this one. It
should be the *first* item: until it is settled, several of the
"derived" entries above (notably "Planck scaling, power ∝ ω") are
graded for one model and arguably mis-graded for the other.

**2. The ℤ vs ℤ_{≥0} bridge for occupation is missing.** §7.2's last
bullet — *"integer Fourier index ⇒ integer occupation. Given the
complex-amplitude state, by Fourier-series"* — inherits the elision
flagged in [05-review.md §3](05-review.md). The Fourier integer is all
of ℤ (positive and negative); photon occupation is ℤ_{≥0}. The ledger
quietly identifies them. As a fully-graded accounting chapter, it
should either name this restriction as something the import covers, or
list it as a residual gap inside the [interpretive] step.

**3. The screening / running-coupling thread from
[work/loop-recirculation-attempt.md §5](work/loop-recirculation-attempt.md)
is missing from §7.5.** That aside argues screening is intrinsically
nonlinear and would live in the bit-conserving substrate, and frames
the loop-coupling's actual relevance to α as a *forward-looking probe
of that substrate*. §7.3 acknowledges the zigzag-cancellation caveat
for (2/3)¹², which closes the backward-looking honesty side; the
forward-looking probe (whether the bit-conserving substrate exhibits
the right kind of nonlinear running) is a natural fourth open item
that the ledger drops.

## Inherited issues to verify against the chapter they came from

**4. "spin / polarisation: derived" inherits the unresolved
helical-vs-dispersive issue of ch. 2.** §7.1's status caveat reads
*"derived (modulo the why/how complementarity flagged in ch. 2 §2.4a)"*
— which covers the KK route vs junction route equivalence, but **not**
the misidentification of per-junction helical eigenmodes with
"the photon" flagged in [02-review.md §2](02-review.md) (those
eigenmodes sit at ω = π, not on a dispersive band). If ch. 2 has been
revised to clarify "helical = polarisation *basis* of the dispersive
bands, not the propagating modes themselves," the ledger's caveat is
fine. If it has not, then §7.1 and §7.2's first bullet over-grade
spin/polarisation. The status of the ch. 2 fix is not visible from the
ledger; please confirm.

**5. "Spin … the same KK mechanism MaSt uses for spin" plus
"`lib.py` doesn't carry helicity" (per
[02-review.md §5](02-review.md)).** The spin-by-helical-modes story
relies on **complex** (phasor) amplitudes; `scripts/lib.py` uses
real-only `(a_fwd, a_bwd)`. So the sim cited as evidence does not
realise the helicity story. The ledger grades the row "derived" with
no caveat about the sim's coverage. Either a footnote here, or a fix
in ch. 2 that the ledger then inherits, would close it.

## Sync issue, not a chapter error

**6. The §7.1 table is now richer than the README's "what each
phenomenon is" table the Sources line cites as canonical.** The ch. 7
row for α carries the *"property of a forced single pulse … not of a
free propagating wave"* clause and the zigzag-cancellation language;
the row for light quantisation carries the *"not a cheaper stochastic
claim"* hedge. The README's version (lines ~74–86 at last reading)
does not. One should be promoted to canonical and the other brought
into line — currently a reader following the Sources pointer will find
the canonical table missing material the ledger considers part of the
honest accounting.

## Smaller note

**7. §7.2 "scale-invariance of the photon band" — the
Planck-cell-identification dependency from
[03-review.md §7](03-review.md) is not flagged.** "Real light has
wavelengths vastly longer than a lattice cell" holds *under* ch. 4
§4.4's "cell = Planck length" identification, which §4.4 itself marks
as a posit. The ledger should reference §4.4's posit when leaning on
it for the scale-invariance bullet, otherwise the bullet quietly
upgrades a posit into a fact.
