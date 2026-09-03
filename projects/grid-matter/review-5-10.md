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
