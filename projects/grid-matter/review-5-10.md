# Outline review — Chapters 5–10

Scope: the **outlines** now in `05-…` through `10-…`. These are bullet outlines,
so this pass targets **logical/structural** issues that would propagate into the
prose — not prose-completeness. Structural/README findings live in
[work/review.md](work/review.md); the Ch 1–4 prose findings in
[review-1-4.md](review-1-4.md). Severity **critical / medium / light**, each tagged
**fatal?** and **fixable?**.

Overall the outlines are honest and well-flagged — Act 2 correctly presents itself
as a question, Ch 5 owns the 3D gap, Ch 10 owns the open core. The issues below are
mostly mis-labels and one false dichotomy, all fixable before in-filling.

---

## Q1 — Ch 7: the two-slit sim is a *massless extended-space wave*, but the chapter labels it a "matter wave / de Broglie λ"
**medium · not fatal to the arc · fixable (but needs a rerun or an explicit argument)**

The outline §2 says "**a matter wave** passes through both slits … fringe spacing
tracks the **de Broglie λ** (Ch 4)." But the sim behind it (`scripts/dualslit.py`)
launches a broad `cos(ω(t−t₀))` wavefront in ordinary **2D (x,y) extended space**
with **no compact dimension** — a massless scalar. Its wavelength is the field's
own `λ = 2πc/ω ≈ 9`, and the dual-slit-result file itself frames the transmitted
thing as **photons**. So what is demonstrated is **extended-space wave optics of a
massless field** — precisely the Maxwell sector GRID already had — and `Δ = λL/d`
is generic wave optics that holds for *any* wavelength, matter or light.

Two consequences:
1. **The de Broglie / matter framing is imported, not simulated.** A genuine matter
   wave is a **compact-sector (n≥1) massive mode** (Ch 4's `Ω²=c²k²+ω₀²`), whose λ
   is `h/p`. The sim never excites that sector; calling its λ "de Broglie" is a
   category slip.
2. **It weakens the Act 2 premise.** The point of "GRID makes QM *for matter*" is an
   *electron*-style two-slit, not a photon one (photon interference is already
   classical EM in-repo). As written, Ch 7 shows nothing beyond Maxwell.

This is defensible to *fix* cheaply, because Ch 4 established that massive modes are
**also linear waves** obeying the same Bloch dispersion — so the two-slit pattern
*transfers* to the compact sector by linearity. But that transfer must be **stated
as the argument**, or (better) the sim rerun on an `(x, y, compact-c)` slab exciting
an n≥1 mode. What is not acceptable is silently calling the massless-photon sim a
"matter wave."

**Fix:** either (a) rerun `dualslit.py` with a compact dimension and an n≥1 mode and
report the fringe spacing against the *de Broglie* λ; or (b) relabel §2 as a
massless-wave demonstration and add one sentence: "the compact-sector matter wave is
also a linear Bloch mode (Ch 4), so the same interference follows by linearity —
shown here for the massless mode." Carry the same caveat into Ch 8 §2 (below).

---

## Q2 — Ch 5 §4: the "topological vs Noether" fork is a false dichotomy — it omits the richer-target topological route the arc actually relies on
**medium · not fatal · fixable**

§4 frames the 3D-localization problem as a strict two-way fork: **topological**
charge (resolves C1, but §3 says a *single* compact phase can't localize in 3D — no
π₃) **vs Noether** charge (Q-ball localizes, but reopens C1). Stated that way, the
arc looks trapped.

But §5 immediately points at the escape — a GRID **sheet** with *multiple* compact
cycles — and the promotion-hierarchy work file explicitly invokes
**skyrmion/Hopfion** protection. A richer topological *target space* (two cycles →
a torus/sphere target that *does* carry π₂/π₃) can be **both** localized in 3D
**and** topological (C1-consistent). That is a genuine **third branch**, and it is
the arc's real hope — yet §4's binary framing hides it, making the situation read
more stuck than it is.

**Fix:** recast §4 as a trichotomy: (i) single-phase topological — localization
unproven [O]; (ii) Noether Q-ball — localizes but reopens C1; (iii) **richer
topological target on the sheet (multi-cycle → π₂/π₃)** — the candidate that gets
both, deferred to metric-charge. Name (iii) as the live resolution path, not an
afterthought in §5.

---

## Q3 — Ch 6 §3 makes "stability = protected winding" explicit, sharpening its conflict with Ch 3's "stable breather = neutral mass"
**medium · not fatal · fixable (cross-chapter reconciliation)**

§3 states the doctrine plainly: "what survives is what is **topologically
protected**." A breather is **winding-0**. So by Ch 6's own criterion the breather
— which Ch 3 §3 calls a *stable* neutral mass, and which Ch 5 §2 lists as "stable in
1 extended dimension" — is **not** topologically protected, and the
promotion-hierarchy file already calls the analogous unwound object "quasi-stable
… slowly radiates … ephemeral." The two chapters now assert opposite things about
neutral mass.

This is the P2 tension from the Ch 1–4 review, now visible *across* chapters: Ch 3
says neutral mass is stable; Ch 6 says only windings are protected. The arc needs a
single stated position. The physically honest one may be that **neutral mass is only
long-lived, not protected** (which matches reality — few stable neutral *fundamental*
particles), in which case Ch 3's flat "stable breather" is the overclaim to fix.

**Fix:** reconcile in one place — e.g. Ch 6 §3 adds "topological protection gives
*absolute* stability (charge); winding-0 mass is *dynamically* long-lived but not
protected — the neutral sector's lifetime is a separate question," and Ch 3/Ch 5
adopt the same qualifier. Do not leave "stable breather" and "only windings are
stable" both unqualified.

---

## Q4 — Ch 9 §1 asserts a "Compton-sized zone" for the single-click localization with no basis
**light–medium · not fatal · fixable**

§1 splits the unknown into "the envelope (which fringe) vs the specific draw (where
within a **Compton-sized zone** a given click lands)." The Compton length (h/mc) is
the *rest/internal* scale, whereas the fringe/envelope is set by the **de Broglie**
wavelength (h/p); introducing "Compton-sized" as the click's localization zone is a
specific, physical claim dropped in without derivation or citation, and it is not
obviously the right scale (the click localizes to a *detector*-set scale, not
manifestly a Compton one).

**Fix:** either justify the Compton scale (why the lump/zone is h/mc), cite where it
comes from, or soften to "a small zone set by the lump size" and leave the scale
open. Don't assert a specific physical length in an outline without a source.

---

## Q5 — Ch 8 §1: "ρ = |ψ|² is an identity, not a posit [D]" slides the field-energy identity toward the Born quantity
**light · not fatal · fixable**

§1 flags `ρ = |ψ|²` as "an **identity**, not a posit … **[D]**." True for
*field energy density* ∝ |field|². But the Born quantity is |ψ_quantum|² =
*probability* density, and the reused symbol ψ lets §1 read as if the Born
numerator is already derived. §3 correctly quarantines the real gap (energy →
probability is "Born's actual content … assumed"), so the outline is internally
honest — but §1's confident "[D]" on `ρ = |ψ|²` should not be read as delivering the
Born |ψ|². Keep the two |ψ|²'s distinct.

**Fix:** in §1, say "energy density ρ ∝ |field|² is an identity" and defer *the
identification of that with a probability density* explicitly to §3, so the [D] flag
attaches only to the field-energy identity.

---

## Q6 — Ch 8 §2 / Ch 7: "whole-quantum click (grid-quantization)" is a *photon* quantization result applied to matter
**light · not fatal · fixable**

§2 imports the whole-quantum click from grid-quantization "the genuinely quantum
ingredient." If grid-quantization established whole-quanta for **light** on the
bounded substrate, applying it to a **matter** detection needs a line of
justification (the same photon-vs-matter slip as Q1). Likely fine — the bounded-mode
quantization argument is substrate-generic — but it should be asserted, not assumed
to carry over.

**Fix:** one clause noting the quantization argument is substrate-generic (applies
to any bounded mode, compact-sector matter included), or cite where grid-quantization
covers the massive case.

---

## Q7 — Ch 6 §4: "charged ⟹ massive" is billed as a *prediction* but is built into the ladder's definition
**light · not fatal · framing**

The ladder *defines* charge as **captured mass** (L3 above L2), so "no massless
charged particle" is a structural consequence of the construction, not an
independent prediction that could have come out otherwise. It is still a genuine
*consistency-with-reality* check (electric charge obeys it; the gluon caveat is
honestly flagged) — but calling it a "prediction" oversells. Minor; matches how the
README phrases it, so fix both or neither.

**Fix:** call it "a consistency check the ladder passes for electric charge (and the
gluon tension it must later answer)," not a prediction.

---

## Q8 — Ch 10 §2: the toy "puts cos(a−b) in by hand," so 2√2 is trivial and "could host QM correlations" overstates it; no-signaling is asserted
**light · not fatal · already hedged**

§2 is admirably honest ("arithmetic consistency check, not a derivation"). Two
residual overstatements: (a) once cos(a−b) is inserted by hand, reaching Tsirelson's
2√2 is arithmetic tautology — it shows consistency, but "the geometry **could host**
QM correlations" claims slightly more than inserting-the-answer establishes; and
(b) **no-signaling** is asserted, not shown — a hand-inserted non-local correlation
does not automatically preserve the A-marginal's independence from B's setting.

**Fix:** in §2, state that no-signaling is *verified in the toy* (point to the check
in [work/bell-test-result.md](work/bell-test-result.md)), and downgrade "could host"
to "is arithmetically consistent with hosting." Keep §4's [O] as the real deliverable.

---

## Bottom line

No fatal flaw; the outlines' honesty is their strength. Priorities before
in-filling:

1. **Q1** — fix the Ch 7 matter-vs-photon slip (rerun on a compact slab, or argue
   the transfer explicitly). It is the one place Act 2's *premise* is undercut, and
   it also fixes Q6.
2. **Q2** — recast Ch 5's fork as a trichotomy so the arc's actual resolution path
   (sheet / richer target topology) is on the table.
3. **Q3** — pick one position on neutral-mass stability and make Ch 3 / Ch 5 / Ch 6
   agree.
4. Q4–Q8 are local clarity/labeling fixes.

---

# Post-prose review (Chapters 5–10 finished)

The outlines above were in-filled into finished prose, and Chapter 3 was updated in
the same pass (commit `03108b6`). This section audits the finished prose against the
Q1–Q8 items and records the new issues the prose surfaced.

## Q1–Q8: all adequately addressed

Verified against the finished chapters and the new sim
([work/dualslit-matter-result.md](work/dualslit-matter-result.md), numbers
independently re-checked: ω₀ = arccos((2+cos(π/6))/3) = 0.2996 ✓; photon λ = 8.07,
matter λ = 11.16 ✓ from the 3-axis dispersion).

| # | Resolution in the prose |
|---|---|
| Q1 | **Resolved, better than proposed.** Ch 7 adds a compact c-axis, excites the n=1 massive mode, computes the de Broglie λ analytically, and *drops* the old λL/d claim as non-paraxial (§3). It is now a genuine matter-wave demonstration. |
| Q2 | **Resolved, extra-honest.** Ch 5 §4 is now a trichotomy; §4(iii) correctly notes a torus of phases is aspherical (no π₂/π₃), so the sphere-target route is harder, not free. |
| Q3 | **Resolved.** Ch 6 §3 states one position (neutral mass = unprotected L2 rung, long-lived not protected); Ch 3 §3 and Ch 5 §2 now carry and cross-reference the same qualifier. |
| Q4 | **Resolved.** Ch 9 §1 softens the "Compton-sized zone" to plausible-but-detector-set, flagged **[O]**. |
| Q5 | **Resolved.** Ch 8 §1 quarantines the two \|·\|²; **[D]** attaches only to field-energy. |
| Q6 | **Addressed.** Ch 8 §2 adds a substrate-generic (U(1)↔ℤ) justification for carrying whole-quanta from light to matter (see N4). |
| Q7 | **Resolved.** Ch 6 §4 recast as structural consequence / consistency check, not a prediction. |
| Q8 | **Resolved.** Ch 10 §2 *verifies* no-signaling (marginals 50/50) and calls the toy "arithmetically consistent with hosting," not a derivation. |

## New issues surfaced by the prose

### N1 — "entirely local" single click pre-commits to the open ontology fork
**medium · not fatal · fixable**

Ch 8 §5 calls the single whole-quantum click account "**entirely local** … needs
[no] collapse," and Ch 10 §1 inherits this ("the single click is quantum but
**strictly local**"). But selecting *exactly one* click from a *delocalized* wave is
the non-local single-outcome constraint — anticorrelation — which the project's own
[work/thesis-wave-until-interaction.md](work/thesis-wave-until-interaction.md) says
"requires nonlocality … Bell forbids any local realist single-outcome theory." The
*distribution* ∝|ψ|² is local; the *exactly-one selection* is not. It is local only
under Ch 9's reading (ii) (a real localized lump was always there — one lump, one
click); under reading (i) the single click *is* the non-local collapse. So Ch 8 §5's
unconditional "entirely local" silently adopts (ii) — which frictions with Ch 9's
"assert neither branch" and with Ch 10's thesis that the non-locality is unsolved.

**Fix:** Ch 8 §5 should distinguish "local *distribution*" from "single-outcome
*enforcement* (non-local, deferred to Ch 9–10)"; Ch 10 §1 should not call Ch 8's
click "strictly local" — the exactly-one outcome is where Bell non-locality first
enters.

### N2 — Ch 5 §4(iii) ↔ §5 seam: the sheet is the torus §4 just excluded
**light–medium · not fatal · fixable**

§4(iii) correctly argues a torus (product of compact phases) is aspherical and so
does *not* supply the π₂/π₃ a localized 3D soliton needs. But §5 then says a GRID
**sheet** "plausibly localizes," and metric-charge's sheet is a two-cycle (m,n)
*torus* — exactly the aspherical case §4 excluded. Both defer to metric-charge
**[O]**, so it is acknowledged-open, but the seam needs one reconciling clause:
either the sheet supplies extra spherical/non-abelian structure, or it localizes by
a *non-topological* (fixed-size, Q-ball-like) mechanism that should be named. As
written §5 implies a torus-sheet resolves what §4 says a torus cannot.

### N3 — Ch 7 quietly changes the lattice from Ch 4's, then cites Ch 4
**light · not fatal · fixable**

The two-slit lab needs two extended dimensions (x,y) plus compact-c, so it runs on a
**3-axis, N=6** lattice: dispersion (cos kx+cos ky+cos kc)/3, lightspeed **c=1/√3**.
Chapter 4 derived the 2-axis cylinder (N=4, /2, **c=1/√2**). Ch 7 §2 reads the de
Broglie λ "exactly from … cos k_c (**Chapter 4**)," but that exact formula is not
Ch 4's, and a reader holding c=1/√2 will be wrong-footed. **Fix:** one clause noting
the lab adds a second extended dimension, so the dispersion is the 3-axis
generalization of Ch 4's (c=1/√3 here).

### N4 — Ch 8 §2's substrate-generic argument conflates two quantizations
**light · verify-only · fixable**

§2 carries whole-quantum detection from light to matter via "loop single-valuedness
→ integer winding (U(1)↔ℤ)." That yields quantized winding/number, but the
Born-relevant content is that a spread-out quantum yields *one indivisible click*
(anticorrelation), which integer-*total* alone does not force. Plausible and
backstopped by §3's honest **[assumed premise]** flag — worth one line confirming
grid-quantization's countability really is the loop/number-quantization mechanism,
or distinguishing "integer total" from "single localized click."

## Post-prose bottom line

Every original 5–10 concern is closed cleanly; the revisions are honest and, in
Q1/Q2, sharper than requested. The one new item worth acting on before calling this
done is **N1** — a genuine internal inconsistency (Ch 8 asserts local single-clicks;
Ch 9 keeps the fork open; Ch 10 says the non-locality is unsolved), where a careful
reader will notice "strictly local single click" has already picked a side. N2–N4
are one-clause clarity fixes. **No fatal flaw.**
