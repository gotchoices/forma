# Review: errors and reachable strengthenings — the quantization arc

Checked the arc (README §"Presentation arc") and [chapter-outlines.md](chapter-outlines.md)
against the derivations and code they rest on:
[countability-from-information.md](countability-from-information.md),
[energy-and-coherence.md](energy-and-coherence.md),
[tier2-design.md](tier2-design.md), `../scripts/band_structure.py`,
`../scripts/run_recirculation.py`. Only logical errors and
within-reach strengthenings below.

## Logical errors

**1. Countability does not follow from a *real* distribution, and photon number is not charge-like winding.** (Ch.5.2–5.3, Ch.6.4; countability §0, §3.)
U(1)↔ℤ is fine; its application is not. Integer occupation is the
spectrum of N̂ = −i∂/∂φ on a *single-valued complex amplitude* ψ(φ) —
the single-valuedness is the quantum content. A *real* probability
distribution over φ also has an integer Fourier index, but that is mere
periodicity; its classical conjugate (action / angular momentum) is
**continuous**. So "countability needs only the statistical state, not
complex amplitudes" (§3) is wrong — integer occupation *is* a
complex-amplitude feature. The doc's own §8 lists "real vs complex" as
open, contradicting §3. The "same fact as charge quantization" (§0)
also conflates two different integers: charge is a **topological**
winding of a classical field around a **spatial** loop (integer with no
QM); occupation is a **spectral** quantum quantity on the time
oscillation phase. ⇒ The arc's headline — "countability without the
rest of QM, periodicity not discreteness" — is not established; the
integer-ness it claims is the quantum amplitude structure it says it
avoids.

**2. The energy route gives a classical scaling, not the quantum ℏω.** (Ch.5.6; energy-and-coherence §3, §7.)
Flip-counting gives power ∝ ω, but per *cycle* the energy is fixed
(2 flips × dW) — frequency-**independent**. The step "(action per
cycle) = E·T = h ⇒ E = ℏω" assumes the per-cycle action is the
universal constant h — the de Broglie relation the route set out to
remove — and still needs the unbuilt per-cell→per-mode lock (§5.2). So
§7's **[rigorous]** grade on "energy quantum = ℏω" overstates; only the
classical scaling (a pinned-magnitude wave cannot hide energy in
amplitude) is rigorous.

**3. The bound state shown is zero-energy, not "mass-like."** (Ch.3.3; tier2 §2–§3, energy-and-coherence §2.)
The demonstrated CLS sits on the **ω=0** flat band — static (U|ψ⟩=|ψ⟩),
and a static configuration carries zero energy (E = ℏω = 0, by the
file's own energy measure). A massive particle is a localized mode at
finite (Compton) frequency, not a zero-frequency one. Identifying the
static CLS with "the mass-like / standing-particle limit" is incorrect.
Flat bands occur **only** at ω=0 and ω=π — there is no localized mode at
generic finite ω.

**4. The "resonant loop per frequency" mechanism is falsified by the band structure.** (README "mechanism in one paragraph"; `band_structure.py`.)
The quantization premise — "a dense tower of loop sizes… every
frequency finds a resonant loop" (virtual compact dimensions per ω) —
contradicts the computed bands (flat/bound modes only at ω=0,π, not a
frequency-matched tower). Quantization cannot rest on resonant loops;
only the per-mode oscillation phase survives — and see error 1 for why
that alone is not enough.

**5. "Two independent routes" overstates corroboration.** (arc intro, Ch.5.4.)
The files call the topological and energetic routes "one fact seen two
ways" (energy §6); both rest on the *single* A5 hinge, and they deliver
*different* sub-claims (topological → the integer label; energetic →
the ω-scaling). Co-dependent and complementary — not independent
confirmation.

**6. README self-contradiction.** Ch.4 retracts "derive/measure h," but
the "Two tiers" table and the Q1 cross-reference still present
h-universality (RG fixed point) as the pending Tier 2 plan ("Not
started"). One of the two framings is wrong and must go.

## Strengthenings within reach

**A. Build the two named simulations (energy §8) — the project's actual lever.**
(i) a bit-conserving sigma-delta scatter rule: does energy stay an exact
integer count under genuinely discrete dynamics (the continuous 2/3 rule
does not)? (ii) a vertex / height-model test for discrete loop-winding
sectors: does a per-mode topological lock exist? These directly test the
energy route's two unbuilt gates and bear on errors 1–2. Computation is
this project's strength; these are the highest-value moves.

**B. Map the bound modes across the Brillouin zone / construct the CLS tower** (already in Next steps).
Confirm whether any localized mode exists at finite ω, using the
existing `band_structure.py` machinery. Either outcome settles errors
3–4 decisively.

**C. Settle §8 (real distribution vs complex amplitude) before Ch.5 claims P3.**
This is a known result — integer angular momentum requires a
single-valued complex ψ — and it decides whether countability is
derived at all (error 1). Resolve it before grading Ch.5 **[reduced]**.
