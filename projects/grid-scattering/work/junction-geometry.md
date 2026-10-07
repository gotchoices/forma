# Junction geometry — what a node may do with edges that belong to different sheets

**Status:** Result. Replaces the "grouping" premise of README §2 with a geometric statement, and resolves the review's F1 (a particle cannot move) without weakening the project's thesis.

The question: a node touches edges belonging to S and edges belonging to a compact sheet. What is it allowed to do with them? The answer turns out to be sharply constrained, and the constraint is the useful part.

---

## 1. At a symmetric Y junction there is no freedom

Three edges at 120°. Two candidate rules, checked against both conservation laws:

| rule | unitary | momentum |
|---|---|---|
| uniform, S = (2/N)·J − I → (−1/3, 2/3, 2/3) | **yes** | yes |
| "reflection plus half to each outgoing edge" → (−1/2, 1/2, 1/2) | **no** | yes |

The intuitive reading — the two outgoing legs split the signal evenly — conserves momentum but loses a quarter of the energy. At a symmetric junction, symmetry together with unitarity and momentum conservation pins the rule uniquely.

**So the uniform rule is not momentum-preserving by accident.** It is the only symmetric rule that preserves both. There is no room at a Y junction to be "aware" of anything.

## 2. At an X junction there is freedom

Four edges at 90°, which is what a node looks like where one extended direction meets one compact one.

| rule | unitary | momentum |
|---|---|---|
| uniform, S = (2/N)·J − I | yes | yes |
| **straight-through** (a permutation: in on +x, out on +x) | **yes** | **yes** |

Pass-through is a perfectly legitimate scattering matrix. A signal travelling along x continues along x; a signal circulating in c keeps circulating; neither enters the other. This is the geometric content the project wanted, and it costs nothing in conservation terms.

## 3. But the freedom is discrete

Scanning every C4-symmetric real rule on the X junction that is both unitary and momentum-conserving gives **exactly four solutions**, and they are isolated points:

| reflection | perpendicular | forward | |
|---:|---:|---:|---|
| −1.00 | 0.00 | 0.00 | total reflection (a wall) |
| −0.50 | −0.50 | +0.50 | sign variant |
| −0.50 | +0.50 | +0.50 | uniform (2/N)·J − I |
| 0.00 | 0.00 | +1.00 | straight-through |

**There is no continuous knob.** One cannot write "the orthogonal edges receive a little, but not much" as a symmetric linear rule: either nothing crosses, or half of it does. Any weak-but-nonzero coupling has to break the symmetry, go complex, or **go nonlinear**.

This rules out the obvious patch — weak always-on linear coupling — and forces something better.

## 4. Consequence: the nonlinearity is what binds a moving particle

If weak coupling must be nonlinear, and the project's nonlinearity is saturation, then:

> **A moving particle is a soliton held together by saturation.** At its core the amplitude is above the ceiling, so the S-edges and the sheet-edges *do* exchange there, continuously. That exchange is what binds x-momentum and compact winding into a single object. In the tails, below the ceiling, there is no exchange — which is why sheets stay separate in ordinary propagation.

This answers the review's **F1**. Under straight-through alone, an x-travelling wave and a circulating wave simply coexist and shear apart; the X geometry *permits* both motions but does not *bind* them. The binding is the nonlinearity, and the particle is therefore permanently in the nonlinear regime at its centre.

Two things recommend this reading. It is how solitons work generally — a nonlinearity holding a mode together against dispersion. And it agrees with [grid-matter](../../grid-matter/02-why-simple-binding-fails.md), which found that binding a particle requires a nonlinearity and that the linear substrate cannot do it.

It also makes the saturation thesis load-bearing for **motion**, not only for creation and decay. One mechanism, three jobs.

## 5. Why Maxwell is not at risk

A hazard was raised and then dissolved: a pure permutation rule is ballistic transport, and [grid-duality](../../grid-duality/) set aside its lattice-gas candidate precisely because ballistic transport fails Maxwell and single-particle interference — no partial transmission at a junction means no diffraction.

That hazard applies only if **every dimension** is its own group. It is not the proposal. The partition is **S against a sheet**, not dimension against dimension:

- Within S, the ordinary uniform scatter applies — nodes mix their spatial edges exactly as before, and Maxwell is untouched because nothing about the spatial sector has changed.
- Within a compact sheet, likewise.
- Only **between** S and a sheet is the rule straight-through below the ceiling.

So space remains the GRID that was already shown to give Maxwell, with compact dimensions that do not participate until the dynamics goes nonlinear.

A note on the reduced arena: in the 1D × 1D testbed each group holds only two edges, so within-group scattering is trivially pass-through. That is a property of the reduction, not of the proposal, and it means the testbed cannot speak to Maxwell either way. It is not trying to.

## 6. On asynchrony

[grid-gravity](../../grid-gravity/work/ledger.md) carries "no clock and no synchronization: junctions scatter each arrival on their own" as posit **P1**, so an event-driven node is an existing idea in the repo rather than a new one.

But it does not by itself deliver angle-awareness. [requirements-and-dof.md §2](../../grid-gravity/work/requirements-and-dof.md) notes that summing over arrivals *recovers* the standard scatter exactly: the shared value is (2/N)·Σ arrivals. Per-arrival handling and synchronous handling give the same rule. What changes the rule is the rule — one of §3's four options — and that choice is available with or without a clock.

Dropping the master clock is a larger change with its own consequences ([grid-duality](../../grid-duality/README.md) treats the clock as foundational). This project does not need it.

## 7. What is still open

- **Does the bound helix actually form?** §4 is an argument, not a demonstration. The test is to inject into both groups at once and see whether the result translates as one object, with saturation on and with it off.
- **Does it have inertia?** If a helical state exists, its group velocity against winding number should reproduce ω² = c²k² + ω₀². That relation is what makes compact momentum act as mass, and [grid-matter ch. 4](../../grid-matter/04-matter-waves-and-de-broglie.md) already has it for the pooled scatter — so the comparison is direct.
- **How small is "essentially nothing"?** The ideal node never crosses below the ceiling. A physical system might leak slightly, whether from sub-threshold structure or from rare background-driven saturation events. Whether that residue is needed, and whether it is what α measures, is open.
