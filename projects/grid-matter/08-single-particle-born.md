# Chapter 8 — Single-particle Born

The two-slit fringes of Chapter 7 are a wave phenomenon. What makes the experiment
*quantum* is that the wave is detected as a sequence of single, whole clicks whose
positions are distributed as the intensity — the Born rule. This chapter shows how
far that follows from GRID and names precisely the one step that is assumed rather
than derived.

## §1 The energy density is |field|²

The starting quantity is not a posit but an **identity**: the conserved energy
density of the field is proportional to |field|², a direct consequence of the
scatter's unitarity (energy is conserved because the scatter is orthogonal). So the
spatial profile that Chapter 7 plotted as "intensity" is the field-energy density,
already in hand. **[D; forma]**

It is worth keeping two |·|² quantities distinct from the outset. This one is the
**field-energy** density. Its identification with a **probability** density — the
Born |ψ|² — is a further step, and that step is quarantined to §3. The [D] flag
here attaches only to the energy identity, not to the Born interpretation of it.

## §2 The whole-quantum single click

A detection deposits **one whole quantum**, never a fraction: the wave may be spread
across the backdrop, but it is absorbed as a single lump of fixed action. This is
the genuinely quantum ingredient, and it is imported from
[grid-quantization](../grid-quantization/) rather than re-derived. It is what turns
a smooth wave arriving everywhere into a particle landing *somewhere*. **[cite
grid-quantization]**

That import needs one line of justification, because grid-quantization developed
the whole-quantum result for **light**. Its mechanism, however, is
**substrate-generic**: countability follows from loop single-valuedness — the
mathematical fact that a U(1) phase must come back to itself around a loop, giving
integer winding (U(1)↔ℤ). That argument applies to *any* bounded or compact U(1)
mode, so it carries to a compact-sector (n≥1) matter mode by the same reasoning.
The matter case therefore rides on the mechanism being generic; it does not rest on
a separate proof supplied there. **[cite grid-quantization; mechanism-generic]**

One distinction matters for what follows. This counting argument fixes the *number*
of quanta — an integer total — not the further fact that a quantum spread across the
screen registers as a single *localized* click. That single-outcome content is the
measurement question of §5 and Chapters 9–10; it is not part of, nor delivered by,
the counting.

## §3 Born's distribution, and its assumed step

Put the pieces together. The field-energy density is |field|² (§1); each detection
removes one whole quantum (§2); and if the probability of a click at a node is
proportional to the local energy density there, then the clicks are distributed as

<!-- P(click at x) ∝ |ψ(x)|² -->
$$
P(\text{click at } x) \;\propto\; |\psi(x)|^2,
$$

which is the Born rule. The distribution follows — but the load-bearing step is the
"if" clause: **that detection probability is proportional to local energy density**.
That proportionality is exactly Born's physical content, and it is the *universal*
semiclassical premise of photodetection theory — not something special to GRID, and
not derived here. So the honest status is a **derived distribution, modulo one
assumed detection premise**. **[D distribution, modulo the assumed premise]**

## §4 Confirmation

Accumulating single whole-quantum lumps, each placed by the rule above, rebuilds
the Chapter 7 fringes: the interference pattern reappears click by click, as it does
in the laboratory. **[C]**

## §5 Scope

This is a single-particle result, and its locality must be stated with care. The
**distribution** is local: P(click) ∝ local energy density invokes no state-steering
and needs no collapse. But selecting *exactly one* click from a wave spread across
the whole screen is a **single-outcome** constraint, and that piece is not local in
general. It is local only under Chapter 9's reading (ii), where a real localized
lump was present all along — one lump, one click; under reading (i) the exactly-one
selection *is* the non-local collapse. So Chapter 8 delivers the Born *distribution*
while leaving the single-outcome *enforcement* — the collapse question — open to
Chapters 9–10, which is also where the per-click randomness is left described rather
than explained. **[honest]**

## Attribution / dependencies

The whole quantum is [grid-quantization](../grid-quantization/)'s; the fringes are
Chapter 7's; the detailed argument is in
[work/born-detection-theorem.md](work/born-detection-theorem.md). The assumed
proportionality is standard photodetection theory.
