# Chapter 4 — Self-consistency of the bare metric

**Status:** Bare outline. Each section is one sentence describing
the work that section will perform. To be filled out once the
outline is approved.

[Chapter 1](01-foundation.md) posited a bare diagonal metric on M
as the *starting* condition, with the understanding (Chapter 1 §3)
that whether the metric stays diagonal is an open question.
[Chapter 2](02-mass-from-u.md) found a family of solutions to the
wave equation on that bare metric, and [Chapter 3](03-examining-the-modes.md)
examined what those solutions look like.

This chapter asks the metric question: given the modes Chapter 3
made concrete, **does the bare diagonal metric of Chapter 1 hold
up?** Or do the solutions force the metric to develop something
new — position dependence, off-diagonal terms, or some other
modification?

This is a different kind of question from Chapter 2's. Chapter 2
solved a wave equation on a fixed metric. Chapter 4 takes the
solutions and asks whether the metric they live on remains
internally consistent. The ground rules are still derivation
first; we let the math say what it says.

---

## Bare outline

### 1. What "self-consistent" means here

State precisely what is being asked. The bare metric was assumed,
not derived. Self-consistency means: does the field configuration
we now have respect the assumption, or does it source something
that would modify the metric? Distinguish the two relevant
sources of modification: (a) back-reaction (does φ's stress-
energy curve M?) and (b) emergent structure (do the modes
themselves require off-diagonal or position-dependent metric
components to be described accurately?).

### 2. Stress-energy of the wave field

Compute the stress-energy tensor T_μν associated with φ on M.
For a free massless scalar field this is a standard calculation;
the result is a 3×3 symmetric tensor whose components depend on
derivatives of φ. Examine which entries are nonzero for our
modes.

### 3. Would Einstein's equations modify the metric?

The bare metric of Chapter 1 was assumed without sourcing — we
did not require it to satisfy Einstein's equations. Now ask:
*if* we did require it, would the stress-energy of §2 source any
modification of g_μν? Note that 1+1+1D vacuum gravity is trivial
([Chapter 1 §9](01-foundation.md) non-assumption on gravity), so
this is more an exercise in seeing what the source structure
*looks like* than a literal Einstein-equation solve.

### 4. Off-diagonal entries: do any get sourced?

Examine specifically whether any g_tu, g_Su cross terms would be
forced by the field configuration. If yes, identify which
configurations and what physical role the cross term plays. If
no, confirm that the diagonal metric remains consistent with the
mode structure we found.

### 5. Position dependence: does g_uu need to depend on S?

Examine whether the dilaton-style possibility from
[Chapter 1 §3](01-foundation.md) — g_uu becoming a function of
S — is forced or merely allowed. This question matters because
position-dependent g_uu would mean the mass spectrum varies in
space, which has obvious implications.

### 6. The verdict

Summarize what the math says. Three possibilities (matching
[Chapter 1 §3](01-foundation.md)'s framing of the open question):
the diagonal metric is fully consistent; some off-diagonals or
position dependence are forced; or the constraint is more
elaborate than either case anticipated.

### 7. End of Chapter 4

State, in plain language, what Chapter 4 has established about
the metric, and what (if anything) it requires of subsequent
chapters. If the bare metric is consistent, chapters 5–6
(position-dependent g_uu, off-diagonals) become unnecessary and
the project closes with chapter 7's summary. If the bare metric
breaks, the next chapter to write is determined by which
direction of breakage the math points toward.

---

## What's next

For the next chapter and the rest of the project arc, see the
project [README's table of contents](README.md#chapters). Which
chapter follows depends on Chapter 4's verdict.
