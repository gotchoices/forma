# metric-charge

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** Charge generation on a 2D compact sheet. Mass is already covered in [metric-mass](../metric-mass/).
**Method:** Mathematical derivation as discovery; minimal computation.
**Status:** Framing complete. Awaiting first chapter.

## Why this project exists

[metric-mass](../metric-mass/) established how a single compact dimension produces mass: standing-wave momentum along u, quantized by periodicity, behaves operationally as inertial mass. This project picks up the analogous question for charge.

The naive next step would be to add a second independent compact dimension w and treat it the way Kaluza-Klein treats charge — momentum on w → quantized as charge. That step is well covered in [`primers/kaluza-klein.md`](../../primers/kaluza-klein.md), and metric-mass deliberately did not take it. Repeating it here would just rehearse the standard KK story.

We jump instead to what MaSt's computational studies (R60–R64) suggest is the actual structure: **2D compact sheets** rather than pairs of independent 1D dimensions. The compact part of the manifold here is *one continuous 2D torus* with coordinates u and w, and charge is something the **geometry of the sheet** produces — not something a second independent CD provides.

The central question:

> *What does light alone on a manifold with one **2D compact sheet** produce, and under what conditions does the sheet's geometry promote a standing-wave mass mode into something that behaves like charge?*

### Underlying targets

The framework should illuminate, without explicitly hunting for any of them:

- **Quark-like three-phase structure** on a single sheet — how does the geometry produce three repeating phases? Where does fractional charge come from?
- **Aspect-ratio extremes** — what does a very fat or very thin sheet correspond to physically? Can the framework predict why one species would land at extreme ε while another sits near unity?
- **Apparent neutrality** — can a sheet produce mass with no observable charge? Is "no charge" structural (the wrap simply doesn't satisfy the closure condition), a diffuseness limit (charge is real but spread over a vast L_w), or a complementary-pair cancellation?
- **Bound-state behavior** — when do two knots on the same sheet stack as a harmonic in Ma, when do they separate in S, and is there a partial-separation regime that looks like a confining force?

The framework is not **on the hunt** for the proton, electron, or neutrino sheets specifically. It is in **discovery mode** — exploring how sheet shape (aspect ratio ε), shear (σ_uw), and multi-knot population sort modes into qualitatively different particle classes, including possible single-phase, three-phase, and dark behaviors.

## Coordinates and notation

| Symbol | Role | Type |
|---|---|---|
| **t** | Time | Extended, real (rendered along z) |
| **S₁** | First spatial extension | Extended, real (rendered along x) |
| **S₂** | Second spatial extension | Extended, real (rendered along y) |
| **u** | First compact coordinate on the 2D sheet | Compact: u ~ u + L_u |
| **w** | Second compact coordinate on the 2D sheet | Compact: w ~ w + L_w |

x, y, z are Cartesian *visualization* axes — not metric coordinates.

- **Aspect ratio:** ε ≡ L_u / L_w. Free parameter of each sheet.
- **Shear:** σ_uw is the off-diagonal metric entry coupling u and w. Tilts the compact directions away from orthogonality and breaks several symmetries we'll see come into play.

**Visualization disposition.** When rendered, the compact sheet sits in 3D space at roughly 45° to the (x, y, z) axes — u's normal points roughly (+y, +z), w's normal roughly (−y, +z). The intent is to keep the compact directions visibly distinct from S₁, S₂, and t while still inhabiting the same 3D space. Shear narrows the (otherwise 90°) angle between u and w as seen from above. With the compact dimensions exaggerated for visualization, knots through (S, t) can be drawn as spirals through space and time.

**Why two S dimensions** (whereas metric-mass had one): with two spatial dimensions, two knots on the same sheet can occupy different (S₁, S₂) positions. This opens up bound states, separation-dependent interaction energy, and the distinction between energy that stays bound in Ma (mass) vs. energy that leaves through S (radiation).

## Ground rules

1. **Discovery, not proof.** Where possible, do mathematics that *discovers* a result rather than confirms a prior one. We may know roughly what to expect from MaSt, but the chapter arc should let the math reveal it. (Acknowledged: this is not strictly possible when the result is already known — but the arc should still feel like discovery, not appeal-to-authority.)

2. **Don't re-derive metric-mass.** If a result was established there, cite it. Re-deriving content from `papers/derivations.md`, R62, etc. is fine where it serves the narrative.

3. **The closure condition is axiomatic, not derived.** This project takes "wraps satisfying condition X produce charge" as an *input* to be explored. The α-coupling-strength derivation belongs in [grid/](../../grid/) — we use the result here, we do not re-derive it.

4. **One topic per chapter.** Bundling defeats the discovery arc.

5. **Variables stay symbolic.** Don't pin numerical values until the algebra forces it (per the no-premature-pinning rule).

6. **Computation only when forced.** Paper math first; scripts only when algebra becomes intractable or visualization is the only way to see the geometry.

## Goals

### Theories to test

Claims to examine — derived where possible, stated explicitly when taken as input, and falsified explicitly if the math doesn't support them.

1. **Mass from a 2D standing wave.** A standing wave on a compact 2D surface of any shape produces mass — direct generalization of metric-mass.

2. **Knots as massive modes.** A *knot* — a closed curve that traverses the 2D surface — produces mass when its total path length equals the Compton wavelength of the relevant energy level.

3. **Knot families.** A 2D surface supports a *family* of knots labeled by winding pair (m, n) and possibly higher topological invariants. Goal: characterize the family — series, generations, exclusions.

4. **Topological invariants as quantum numbers.** Crossing number, genus, and linking number map to physical labels: lighter particles correspond to lower-crossing knots; generations to higher-crossing knots in the same isotopy class. Worth checking whether this organizes the spectrum cleanly.

5. **The closure condition (centerpiece).** A knot promotes mass to charge when, during a single traversal, it completes both:
   - a full 2π winding on w, and
   - a complete standing wave on both u and w.
   
   The mass produced by the u-mode is then "promoted" to a charge on w. Mini-step traversals are allowed; what matters is that the closure pattern locks.

6. **Closure failure → mass without charge.** A knot that winds the sheet but does *not* satisfy the closure condition produces mass without charge:
   - winds u but not w → mass only
   - winds w but not u → mass only
   - winds both but the SW conditions don't lock → mass only
   
   This is one structural origin of dark / neutrino-class behavior — geometric, not from pair cancellation.

7. **Knot handedness as the matter/antimatter axis.** A knot has two traversal directions. The handedness carries the matter/antimatter distinction (and possibly the sign of spin) — the analog of MaSt's ±n on a 2D sheet.

8. **Shear breaks symmetries.** σ_uw between u and w affects:
   - matter/antimatter preference (bias-breaking)
   - alignment of complementary nodes (proton-vs-neutron analog on a single sheet)
   - whatever else falls out of the algebra

9. **Multi-phase knots on w produce fractional charge (the quark mechanism).** N knots distributed evenly in w-phase, all sharing the same closure pattern, contribute fractional 1/N charge each. Three-phase populations give thirds-of-a-charge — the structural origin of quark-like behavior on a single sheet. The closure condition still applies per knot, but the *embedding pattern* of multiple knots around the w-cycle is what produces fractional contributions.

10. **Sheet character emerges from (ε, σ, population).** Varying sheet shape, shear, and how many knots populate the sheet sorts the admissible mode family into qualitatively different particle classes — single-phase, three-phase, and dark — without explicitly hunting for any of them. Single-sheet mini-universe: we cannot have a "proton" or "electron" by name (those require multi-sheet structure in MaSt), but we can characterize *what kinds of particles a single sheet supports* under varying conditions.

11. **Multi-knot superposition.** Two knots on the same sheet:
   - same handedness, same closure pattern → stack as a harmonic in Ma (or fail to stack)
   - opposite handedness → may cancel in w (neutral pair), pass through, or annihilate
   - shear-aligned complementary modes → proton/neutron-style splitting
   
   The math should classify which of these outcomes the sheet's geometry actually permits.

12. **Bound-state regimen (the strong-force model).** Two knots at finite (S₁, S₂) separation have an energy landscape that should support several regimes:
   - **Stack in Ma** — two similar knots fit together as a higher harmonic of the same compact pattern.
   - **Stack but not separable in S** — opposite-handedness knots that lock in Ma without flying apart in S (a candidate confined-pair state).
   - **Partial S-separation, bound** — knots separated in S₁/S₂ but unable to escape to infinity (Coulomb-bound or strong-force-bound).
   - **Free** — knots fully separated, energy-unbound.
   
   The promise: a geometric prediction of when each regime is the ground state, including a candidate strong-force mechanism without postulating one.

13. **Knot interaction at finite separation.** The energy of two knots at different (S₁, S₂) on the same compact surface is what the *force law* between charges has to come from. This is why we needed S₂.

### Open questions

To answer or sharpen along the way:

1. **What distinguishes matter from antimatter?** An energy-comparison regimen is needed: when does a knot's energy stay bound in Ma (mass) and when does it leak to S (radiation)?

2. **What does ε = L_u / L_w do?** Predict effects forward from the metric, not retroactively. Specifically: which ε regimes admit which knot families, and is there a structural reason for extreme aspect ratios (very fat / very thin) to appear?

3. **What does σ_uw select?** Which behaviors does shear pick out, and how cleanly? Three-phase population and proton/neutron-style splitting both should be examined here.

4. **What sets the particle inventory?** Is it the full enumeration of admissible knots up to some crossing number, or are there structural exclusions (Pauli-like) that forbid specific (m, n) pairs?

5. **Is the closure condition unique?** Does 2π-on-w + full-SW-on-both have alternatives that select different particle classes? Enumerating the variants would tell us whether all observable distinctions trace to one rule or several.

6. **Pass-through vs. annihilation of complementary pairs.** When two opposite-handedness knots that cancel in w superimpose, do they continue to exist as superimposed-but-distinct objects, or do they annihilate? The linear-superposition pass-through result of metric-mass Chapter 4 was a one-CD finding — it may or may not generalize here.

7. **Predicting harmonics-in-Ma vs. separation-in-S.** Develop a regimen for predicting, in advance from (ε, σ, knot quantum numbers), whether two knots will stack in Ma or split into two spatially separated objects in S.

8. **What does S₂ actually buy?** Be explicit at each chapter about which results require the second spatial dimension and which already work in S₁ alone.

9. **What carries momentum through S when a knot moves?** Rigid translation, internal deformation, or precession?

## Background reading

- [metric-mass/](../metric-mass/) — the immediate predecessor; mass-from-u
- [primers/kaluza-klein.md](../../primers/kaluza-klein.md) — standard KK (and why this project deliberately skips repeating it)
- [studies/R63-proton-tuning/](../../studies/R63-proton-tuning/) — proton sheet, three-phase structure
- [studies/R64-nuclear-harmonic-stack/](../../studies/R64-nuclear-harmonic-stack/) — quarks on the p-sheet
- [studies/R46-electron-filter/](../../studies/R46-electron-filter/) — electron sheet, fat aspect ratio
- [studies/R49-neutrino-filter/](../../studies/R49-neutrino-filter/) — neutrino sheet mode spectrum
- [grid/](../../grid/) — where the α-coupling derivation will live (taken as input here)

## Chapters

The arc below is a *sketch*. Early chapters are framed in detail; later chapters are framed as questions to examine. The project may redirect when a chapter's math reveals something unexpected.

1. **`01-foundation.md`** — Axioms and givens. The (S₁, S₂, t, u, w) manifold, the metric (with ε and σ_uw as parameters), the wave field, and the closure condition stated axiomatically. Visualization disposition (45° rendering) included.

2. **`02-modes-on-a-sheet.md`** — Solve the wave equation on the 2D compact sheet. Derive the mode family labeled by winding pairs (m, n), the dispersion relation, and the discrete mass spectrum. Confirm the (0, 0) zero mode behaves as light; non-trivial (m, n) modes carry rest mass. Establish the (m, 0) and (0, n) "single-axis" modes as candidates for closure-failure mass-only states.

### Tentative downstream arc

The chapters below are plausible follow-ups, not commitments.

3. **`03-knots-on-the-torus.md`** — Reframe non-trivial modes geometrically as knots traversing the sheet. Characterize the knot family: which (m, n) pairs admit non-self-intersecting closures? Establish the topological invariants (crossing number, genus, linking) and how they index the family.

4. **`04-the-closure-condition.md`** — When does a knot promote mass to charge? Work through the 2π-on-w + standing-wave-on-both rule explicitly. Identify which knots in the family satisfy it (charged modes) and which don't (mass-only modes — the closure-failure neutrino-class candidates from §6 of the goals).

5. **`05-handedness-and-pairs.md`** — Knot orientation as the matter/antimatter degree of freedom. Examine when complementary pairs cancel net charge (giving apparent neutrality through cancellation, distinct from the structural neutrality of chapter 4) and when they don't. Tackle the pass-through vs. annihilation question (Q6).

6. **`06-aspect-ratio-and-character.md`** — Sweep ε = L_u / L_w. Discover what knot families dominate at small ε (thin sheet), large ε (fat sheet), and ε ≈ 1. Look — without targeting it — for the conditions under which a sheet supports single-phase, three-phase, or dark behaviors. The "extreme aspect ratio" question for the electron-class and the "diffuse charge" question for the neutrino-class are examined here.

7. **`07-shear-and-fractional-charge.md`** — Turn on σ_uw. Which symmetries break? Test the prediction that shear biases matter over antimatter. Then derive the fractional-charge mechanism: N knots distributed in w-phase contribute 1/N charge each, and shear is what selects N = 3 cleanly. This is where the quark-like three-phase structure should emerge if the framework is right.

8. **`08-multi-knot-states.md`** — Two knots on the same sheet at the same (S₁, S₂) location. When do they stack as harmonics, when do they cancel, when do they refuse to coexist? Establish the bound/free distinction in the limit of zero spatial separation.

9. **`09-knot-interaction-and-binding.md`** — Two knots at *different* (S₁, S₂). Energy as a function of separation. Identify the regimes from goal §12 (stack-in-Ma, stack-but-bound-in-S, partially-separated-but-bound, free) and where each is the ground state. Candidate strong-force mechanism is examined here.

10. **`10-closing-summary.md`** — Consolidate what the project established, ruled out, and unexpectedly found. Hand off to follow-up projects.

Each chapter is added one at a time. The arc is a sketch, not a contract.
