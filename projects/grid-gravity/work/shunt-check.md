# The shunt check — does the back-reaction give Yukawa?

**Status:** Working note (the load-bearing calculation).
[update-rule.md](update-rule.md) §7 item 1: the candidate rule passes the
1/r condition only if its linearized steady state has **no term ∝ q** (no
mass/shunt). This note carries that check. The result is positive but
conditional, and the residual condition is exactly what the simulation
tests.

Grades: **[rigorous]** (follows from conservation), **[plausible]**
(leading-order / assumed constitutive form), **[open]**.

---

## 1. What a shunt is, physically

The two candidate steady-state equations are

<!-- ∇²q = −Sδ   (massless → 1/r)  vs  (∇² − m²)q = −Sδ  (Yukawa) -->
$$
\nabla^2 q = -S\,\delta(x-n) \quad\text{(1/r)} \qquad\text{vs}\qquad
(\nabla^2 - m^2)\,q = -S\,\delta(x-n) \quad\text{(Yukawa, } \xi = 1/m).
$$

The −m²q term is a **local sink**: in the time-dependent form
∂q/∂t = D∇²q − Dm²q + S, it relaxes q toward zero at rate Dm²
*everywhere*, not just at the source. So a shunt is a bulk process that
**removes q in proportion to q at each point.**

## 2. The conserved density, and the shunt ⟺ loss identity [rigorous]

The delay field is q = Q/μ, where Q is the edge **backlog** (signal
in-flight) and μ the bandwidth. Q is a density of signal, and signal is
**conserved** (the lossless commitment). Its balance is a continuity
equation:

<!-- ∂Q/∂t + ∇·J_Q = S − L -->
$$
\frac{\partial Q}{\partial t} + \nabla\cdot J_Q = S - L,
$$

with J_Q the backlog flux, S the source (the mass's persistent
consistency-traffic at n), and L any **loss** (backlog removed from the
conserved sector). In steady state ∂Q/∂t = 0, so ∇·J_Q = S − L.

The shunt term is exactly L: a bulk sink L = m²D·Q *is* a −m²q term in the
field equation. Therefore

> **a shunt exists ⟺ the backlog has a local loss channel.**

Losslessness means L = 0 by construction — backlog is never removed, only
passed to a neighbour. So **lossless ⇒ no shunt ⇒ massless ⇒ 1/r.** This
is airtight *given* that q tracks a conserved density, which it does in
the far field (μ constant there).

## 3. Do the nonlinear back-reactions manufacture a shunt? [plausible]

The worry ([update-rule.md](update-rule.md) §4) is that even with L = 0,
the nonlinear couplings could generate an *effective* q-term on
linearization. Three couplings, checked in turn:

**(a) Congestion-dependent transport, D = D(q).** A congested region
transports additional traffic differently, so the constitutive relation is
J_Q = −D(q)∇Q. Then ∇·(D(q)∇Q) = −S. Linearize about a background Q₀:

<!-- ∇·(D(Q₀)∇δQ) + ∇·(D'(Q₀) δQ ∇Q₀) = −δS -->
$$
\nabla\!\cdot\!\big(D(Q_0)\nabla\delta Q\big) + \nabla\!\cdot\!\big(D'(Q_0)\,\delta Q\,\nabla Q_0\big) = -\delta S.
$$

The extra piece is ∝ ∇Q₀. In the **far field** the background is uniform
(∇Q₀ → 0), so it vanishes and only D(Q₀)∇²δQ survives — a **renormalized
diffusion constant, no shunt.** Near the source ∇Q₀ ≠ 0 and this term
modifies the near field, but it is not a constant-m² sink and does not
touch the 1/r tail. **No shunt.** ✓

**(b) Dilation-dependent source, S = S(q_n).** The mass sits in its own
congested region, so it emits consistency-traffic at its *own* slowed
proper rate: S = S₀/(1+q_n). But q_n is the delay *at the single source
point n*, one number — it rescales the overall source strength, a
constant. It is not a field over all x, so it adds **no bulk q-term.** ✓
(It does make the source strength self-consistent, which matters for the
coefficient, not the falloff.)

**(c) Spatially-varying bandwidth, μ = μ(x).** The compact standing wave
lowers μ at and near n, so q = Q/μ(x) differs from Q there. But μ varies
only in the loaded neighbourhood; in the far field μ = μ₀ and q ∝ Q ∝ 1/r.
**Near-field modification only; 1/r tail robust.** ✓

None of the three produces a bulk term ∝ q. They renormalize D and S and
reshape the near field, exactly as expected for a conservative nonlinear
transport, and they leave the massless far-field 1/r intact.

## 4. The one genuine contingency [open]

The result rests on two things the numerics must still confirm:

1. **The congestion quantity is the conserved signal, not consumable
   messages.** If "consistency traffic" were information *consumed on
   receipt* (removed when read), that consumption would be a loss L ∝ Q — a
   shunt — and the field would be Yukawa. The lossless commitment says the
   traffic is conserved energy, not consumable messages, so L = 0. This is
   a commitment, and it is *where* a shunt would enter if the commitment
   failed. It is the physical crux, now isolated.
2. **The constitutive relation is diffusive**, J_Q = −D∇Q. This is the
   generic leading-order form for conservative transport, but it is assumed
   here, not derived from the FIFO microdynamics. A drift term (J_Q with a
   piece ∝ Q, not ∇Q) would change the falloff. The simulation's radial-
   falloff measurement is precisely the test of this.

## 5. Verdict

The shunt check **passes analytically, conditionally**: losslessness
forbids the bulk loss that a shunt requires, and the leading nonlinear
back-reactions renormalize coefficients and reshape the near field without
manufacturing a mass term. So the **1/r far-field survives the next-order
linearization.**

What remains is no longer "does a shunt appear from the algebra" — that is
answered (no, given losslessness) — but the two contingencies of §4, both
of which the **simulation** settles:

- confirm the congestion quantity is conserved (no consumable-message
  loss), and
- confirm the transport is diffusive (J_Q ∝ −∇Q), by measuring the radial
  falloff (1/r vs Yukawa vs anisotropic) directly.

So the gate's analytic leg is done and clean; the go/no-go is now the
minimal simulation.
