# grid-gravity — critical review

Scope: mechanism 2 (detour/refractive), which the [README](README.md) presents
as clearing the gate "in structure" on all four conditions, and the framing of
the chapter arc. Only disagreements are recorded; positives are omitted by
request. Severity is marked **[deal-breaker]**, **[substantial]**, **[minor]**.

---

## 1. The clock sector — the thesis itself — lives where the non-dispersive derivation fails. **[deal-breaker / must-resolve]**

Non-dispersivity is the keystone: [local-time.md](work/local-time.md)
Commitment 3 says the slowing is *time dilation* rather than an *optical medium*
**only if** it rescales all frequencies uniformly. The derivation delivers this
only asymptotically. The Lorentz form
([energy-coupling.md](work/energy-coupling.md) §2)

<!-- n^2(omega) = 1 + rho G^2 / (omega_0^2 - omega^2) -->
$$
n^2(\omega) = 1 + \frac{\rho\,G^2}{\omega_0^2 - \omega^2}
$$

is the textbook *dispersive* medium; it is flat only for ω ≪ ω₀, with
corrections at O((ω/ω₀)²). The problem: the object whose rate defines proper
time is, by this project's own premise, **confined light at ω₀ = ω_Compton** —
i.e. it sits at or near the resonance, exactly where the ω ≪ ω₀ expansion and
the Kapitza time-average both break down and dispersion is maximal. So the
mechanism is cleanest for the sector it does *not* need (low-ω passing light →
bending) and least controlled for the sector the whole thesis rests on (clock
rates → time dilation). "It is time dilation, not an optical medium" (Ch. 5) is
derived in a limit that structurally excludes the Compton clock it invokes.

Universality is affected too: two same-species particles have ω_probe ≈ ω_source
(resonant), so mutual gravitational time dilation between them is in the failure
regime. Most *practical* clocks (atomic transitions ~eV, sources ~GeV) sit safely
in ω ≪ ω₀, so the numerical deviation is tiny — but the equivalence-principle
claim is *exact universality for every clock*, and that is not what the
derivation gives. This is the argument's load-bearing gap, not a coefficient
detail; it should be confronted head-on in Ch. 5, not asserted.

## 2. The core softening is derived for the compact-mode stiffness; its transfer to the *spatial* wave speed is asserted. **[substantial]**

[aleph-grounding.md](work/aleph-grounding.md) §3 derives that a resident
standing wave softens the **compact-direction** stiffness,
⟨U''⟩ = ω₀²(1 − A²/4). It then writes "softer stiffness → lower wave speed for
the **photon** → n > 1" (§4) in one step. But the photon is the n=0 mode whose
spatial propagation speed is set by the lattice scatter, not by the compact
phase's restoring force. That a softened *compact* stiffness lowers the *spatial*
c_eff is the entire content of the mechanism — it is the moduli/geometry →
4D-coupling link — and it is exactly what is skipped. Without it, the derivation
establishes a modified compact oscillator, not a refractive index for passing
light. This is the crux step and it is currently a hand-wave.

## 3. "Grounded in the substrate" overstates a premise that contradicts forma's established default. **[substantial]**

The README repeatedly upgrades the mechanism from "assume a coupling" to
"grounded in a core, established feature — GRID's boundedness" (Why-it-exists,
Next-step, Ch. 1). But the derivation needs a **smooth, symmetric, lossless
(reactive)** bound, while forma's actual axiom-A3 wrap is **lossy/hard** — the
opposite flavor, as the notes themselves admit
([aleph-grounding.md](work/aleph-grounding.md) §6, ground rule 8). "Boundedness
is established" is true; "the reactive-lossless bound we need is established" is
false. The top-line language rounds the first into the second. The proposed
rescue (sigma-delta coarse-graining smooths the hard bound) is speculative and
unproven. Honest framing: gravity is derived *given a premise that departs from
the project's own foundation* — which is closer to mechanism 1's "awkward
demand" than the writeup concedes. This matters because the claimed advance over
mechanism 1 is precisely that mechanism 2 is "grounded, not posited."

## 4. Condition (0) is not independent of condition (1); its "clean pass" is bookkeeping. **[substantial]**

Mechanism 2's advertised structural advantage is that the vacuum field is "met —
a refractive index is a medium property" without an active broadcast
([detour-refractive.md](work/detour-refractive.md) §2). But δn ∝ A² is nonzero
only where the standing-wave amplitude reaches; for n(x) to exist *at range r*
(which is what gravity-in-vacuum requires), the softening must still propagate
outward — which *is* the range question (condition 1) and the same
source-must-reach-vacuum problem [micro-to-macro.md](work/micro-to-macro.md)
forced on mechanism 1. Splitting these into "(0) met cleanly / (1) the
make-or-break" double-counts one physical question and inflates the "met in
structure" tally.

## 5. The 1/r simulation confirms an assumption, not the mechanism. **[substantial]**

[loops-and-range.md](work/loops-and-range.md): a scalar point source on a
massless graph Laplacian yields the Laplacian Green's function (log r, R² =
1.00000, isotropic). This is near-tautological — a massless linear operator
*must* give a scale-free power-law Green's function; the R² = 1.00000 tests
linear algebra, not the detour rule. The two genuine questions — (a) does the
detour present a **scalar-energy** source rather than a winding or a
mass-generating nonlinearity, and (b) is the operator still massless in the
*loaded/nonlinear* regime — are both assumed by the setup, and the note says so
(§5). The simplified-model note then declares the source-character question
"retired in the model's favour" by appeal to MaSt structure
([simplified-model-and-mast.md](work/simplified-model-and-mast.md) §3) — an
appeal to another project, not a derivation from the rule. So "all four
conditions met in structure" rests, for condition (1), on a tautological sim
plus a deferred assumption. The work notes are honest about this; the README's
confidence does not fully inherit their caveats.

## 6. The Lorentz-oscillator identity is cited as a strength but cuts the other way. **[minor–substantial]**

[energy-coupling.md](work/energy-coupling.md) §2 celebrates that the mechanism
"*is* the Lorentz dielectric that underlies" optical-metric gravity. But a
Lorentz oscillator is the paradigm of a *dispersive* medium; polarizable-vacuum
gravity works only because it *assumes* a frequency-independent n(r). A
microscopic Lorentz derivation cannot deliver an exactly non-dispersive index —
so the mechanism does not actually reproduce the PV premise it claims to justify;
it reproduces it only to O((ω/ω₀)²). Same fact as §1, from the medium side: the
identity that is presented as the win is also the source of the dispersion
problem.

## 7. Minor / consistency

- **Coefficient dismissal may over-apply "G is a unit."** The scale of G is a
  unit (agreed — cf. the principle-vs-scale distinction). But the *dimensionless*
  content G = 1/(4ζ) — gravitational strength per unit substrate resolution — is
  physics, not units. The project has shown only a proportionality ∝ 1/κ ~ 1/ζ
  ([micro-to-macro.md](work/micro-to-macro.md) §4), never the O(1) factor. Waving
  the whole coefficient away as "optional bonus" (repeated ~8× in the README)
  risks giving condition (3) too easy a pass on its dimensionless part. Recommend
  stating explicitly that the *direction* is shown and the *dimensionless factor*
  is untested — not folding the latter into "just a unit."
- **Factor-of-2 confidence is inconsistent between notes.**
  [local-time.md](work/local-time.md) flags the light-bending factor of 2 as
  **[open]** (compact-vs-spatial congestion split), while
  [detour-refractive.md](work/detour-refractive.md) §5 treats it as inherited
  free from PV. For a single scalar n(r) the PV inheritance is likely correct and
  the local-time flag is a mechanism-1 residue — but the two should be
  reconciled before Ch. 6 claims light-bending.

---

## Net

No error found that kills the *thesis* (mass → local-time gradient → gravity).
But the README's headline — "mechanism 2's shape clears the gate on all four
conditions" and is "grounded in the substrate" — is stronger than the notes
support. Two items are load-bearing and currently unmet, not merely deferred:
the **compact-stiffness → spatial-speed transfer** (§2) and the **clock-sector
non-dispersivity at ω ≈ ω₀** (§1). Both sit inside the "met" conditions, not in
the acknowledged "non-gating residual." Recommend demoting the status from "all
four met in structure" to "two met, two conditional on an unresolved crux," and
writing Ch. 1 only after §1–§2 are confronted — a chapter built on the current
framing would overclaim.
