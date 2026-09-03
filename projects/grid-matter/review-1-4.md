# Prose review — Chapters 1–4

Scope: the *drafted prose* now in `01-foundation.md` … `04-matter-waves-and-de-broglie.md`,
read against the README arc and the underlying math. This is a fresh pass for
issues **introduced or exposed by the prose**; the structural/README findings are
in [work/review.md](work/review.md) and not repeated. Severity: **critical /
medium / light**; each tagged **fatal?** (to the chapter's claim) and
**fixable?**.

The math checks out: the dispersion `cos ω = −(cos kx + cos kc)/2`, `c = 1/√2`,
the photon and small-k relativistic forms, the sine-Gordon Taylor signs
(−m²/24 focusing, +m²/720 saturating), and `v_p·v_g = c²` are all correct as
written. **Resolved since the last review:** Ch 4 §6 now says "~4 significant
figures" (was the unsupported "6 digits") — good.

Five prose-level issues remain.

---

## P1 — Ch 4 §3: the KK mass tower is presented as exact/linear, but ω₀ ∝ n is only a small-kc approximation
**medium · not fatal · fixable**

§3 gives the tower as `ω₀(n) = c·kc = n·(2π/nc)/√2 ∝ 1/R` and flags the whole line
**[D]** ("derived, exact"). But `ω₀ = c·kc` is the *small-kc linearization* of the
exact rest frequency `Ω₀ = arccos((1+cos kc)/2)`. The two agree only near the
bottom of the tower:

| kc | exact ω₀ | c·kc | error |
|---|---|---|---|
| 0.3 | 0.2117 | 0.2121 | +0.2% |
| 0.5 | 0.3517 | 0.3536 | +0.5% |
| 1.0 | 0.6917 | 0.7071 | +2.2% |
| 1.5 | 1.0059 | 1.0607 | +5.4% |
| 2.0 | 1.2746 | 1.4142 | +11.0% |

So the *relativistic* form `Ω² = c²k² + ω₀²` **and** the linear tower `ω₀ ∝ n`
share the *same* small-k limitation — but §5's honesty caveat is written only about
**kx** ("emergent at small k … within ~2% for kx < 0.4π"). The compact/tower
direction (large n ⇒ large kc ⇒ non-linear, non-relativistic) is never flagged,
and the blanket **[D]** on §3 reads as "exact for all n," which it is not.

This is mitigated in practice — real particles sit on large sheets (nc huge,
kc = 2π/nc tiny), where the approximation is excellent — so the *physics* is fine.
It is the *exactness claim* that overstates.

**Fix:** downgrade §3's flag to **[D small-kc]** (matching §5's `[D small-k + C]`
spirit), and add one clause: "linear in n only for the low rungs; ω₀ = c·kc is the
small-kc limit of Ω₀ = arccos((1+cos kc)/2), so the upper tower bends sub-linear
(≈5% by kc≈1.5)." One sentence closes it.

---

## P2 — Ch 3 §3: the breather is called "stable," but the project's own stability principle says only a *protected winding* is stable
**medium · not fatal · fixable**

§3 reads `breather = neutral mass` and asserts "the breather is **stable**, mobile,
and energy-conserving." But the breather is **winding-0** — it carries no
topological charge. The project's stability doctrine
([work/promotion-hierarchy.md](work/promotion-hierarchy.md), "Stable vs. ephemeral")
is explicit that **stability = protection by a conserved winding**, and that the
un-wound object (the oscillon there) is only "**quasi-stable and slowly radiates**
— an ephemeral particle." So Ch 3's flat "stable breather = neutral mass" is in
direct tension with the arc's own criterion: a winding-0 lump should be, by that
criterion, *not* topologically protected.

Two things are being conflated: continuum sine-Gordon breathers are exactly stable
(integrability), whereas on the **discrete lattice** — which is exactly what §3
invokes with Peierls–Nabarro — they radiate and are at best long-lived. Calling
that "stable" without qualification both overstates the numerics and collides with
the promotion-ladder claim that neutral (unwound) modes are the *ephemeral* ones.

There is a real physics question hiding here (does the arc predict stable neutral
massive particles, and if so what protects them?), but the *prose* fix is smaller.

**Fix:** qualify to "long-lived (continuum-integrable; on the lattice it radiates
slowly but crosses Peierls–Nabarro rather than pinning)," and add a half-sentence
acknowledging that a winding-0 breather is not topologically protected — its
persistence is dynamical, not the winding-protection of Ch 6 — so the two
stability notions don't appear to contradict.

---

## P3 — Ch 1 §5: the status-flag legend omits [C], which Chapters 3 and 4 then use
**light · not fatal · fixable**

§5 defines the conventions as "**[D]** derived, **[P]** posited …, **[O]** open" —
but drops **[C]** (computationally demonstrated), which the README's arc section
defines and which the prose then uses in Ch 3 §3 (`**[C]**`) and Ch 4 §5
(`**[C — quantified, honest]**`). A reader meeting `[C]` in Ch 3 has not been told
what it means.

**Fix:** add "**[C]** computationally demonstrated" to the Ch 1 §5 list.

---

## P4 — Ch 3 §4–§5: the cosine's m² is silently identified with Ch 4's KK *coordinate* mass — the load-bearing synthesis is stated only in passing
**light · not fatal · fixable**

§4's clean split — "the scatter supplies the kinetic term; a compact **coordinate**
supplies the mass m² (Chapter 4); the compact **field-value** phase supplies the
periodic form" — is the crux of the whole matter half, and it is correct and
elegant. But it quietly requires the **same field to carry both compact structures
at once**: to be KK-massive on a compact *coordinate* (giving the m²φ²/2 term)
*and* valued in a compact *phase* (completing m²φ²/2 → m²(1−cos φ)). Chapter 1 §4
is at pains to keep "compact coordinate" and "compact field value" *distinct*; Ch 3
§4 then *composes* them into one object without flagging that this is the move. A
reader who internalized §4-of-Ch1 will not see where the m² in `U = m²(1−cos φ)`
comes from.

**Fix:** one explicit sentence in Ch 3 §4: "Note this posits a field that is
*both* — a mode on a compact coordinate (so KK-massive, §Ch4) *and* one whose value
is a compact phase (so periodic); the coordinate fixes the coefficient m², the
field-value topology fixes the completion to a cosine." Turns an implicit
composite into a stated premise.

---

## P5 — Ch 3 §3: "kink = charge … the two kinds of particle" invites over-reading a 1D kink as a 3D charged particle
**light · not fatal · fixable**

§3 presents "breather = neutral mass, kink = charge" and reads them "as the two
kinds of **particle**." Within Ch 3's strictly 1D (x,c) setting this is fine, and
§5 does defer the localized-3D construction to metric-charge with **[O]**. But the
word "particle" at §3, unqualified, lets a reader carry away "a kink *is* a charged
particle," which Ch 5 then has to walk back (a kink is a domain wall, a winding is a
vortex line — neither is a localized 3D particle). The correction lives two chapters
away.

**Fix:** a parenthetical at §3 — "(these are the 1D solitons; whether either
localizes as a 3D *particle* is deferred to Ch 5, and is [O])" — inoculates the
reader at the point of first claim.

---

## Bottom line

No fatal flaw in the Ch 1–4 prose; the derivations are sound and honestly flagged.
The one worth doing before anything else is **P1** — it is a genuine
exactness-overclaim (the `[D]` tower is a small-kc linearization, off by 5–11% on
the upper rungs), and the arc's credibility rests on its precision claims being
exactly calibrated. **P2** is next: it is not wrong so much as internally
inconsistent with the project's own stability principle, and a careful reader will
catch the collision. P3–P5 are one-sentence clarity fixes.
