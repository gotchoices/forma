# STATUS

Working status of grid-couplet. Tracks where the project stands, what's drifted from the original brainstorm, what to keep, what to rebuild, and ranked priorities for the path forward. Updated as work progresses.

---

## Snapshot

- **README**: in place. Framing accurate but does not yet name the across/through variable distinction. Should be revised once Tier 1 is settled.
- **Chapter 1 (`01-foundation.md`)**: drafted as prose. The cos-weighted update rule it adopts (from grid-lab) fails 2D stability per the dial-comparison test (`sim-dial-comparison.py`). Needs a foundation revisit.
- **Chapter 2 (`02-closure-and-bounding.md`)**: drafted as prose. Argument is honest but paradigm-dependent — the entropic bounding only makes sense if phase is a state variable. If Tier 1 changes the paradigm, chapter 2 needs to be rewritten or repurposed.
- **2D verification**: not yet done. Everything tested so far is 1D (couplet chains, closed loops). The project's substantive claims live at 2D.
- **Bridge to grid**: harder than originally framed. sim-maxwell uses traveling-wave amplitudes on edges with vertex scattering and no node state — a different paradigm from chapter 1. Bridge needs a duality argument, not a notational substitution.
- **Scripts directory**: contains exploratory work that should be triaged. See [Cleanup](#cleanup).

---

## Strategic decision pending

The original brainstorm ([b9d3f3d](../../.git)) framed two primitives — edge (linear, unbounded) and node (periodic, bounded) — and asked whether nodes can be derived from edges. The chapters to date attempted this without first pinning down the *physical* role of each primitive, which led to repeated terminology revisions and a chapter 2 derivation that almost reached the wrong conclusion.

The across/through-variable framing (proposed in conversation) supplies what was missing: edges naturally hold a *through* variable (flow, current-like), nodes naturally hold an *across* variable (potential, voltage-like), and the two-phase clock follows from physical conservation laws. The pending decision is whether to adopt this framing as the project's foundation before any further chapter work.

This decision should be made before continuing.

---

## Tier 1 — foundation must be solid before going further

These are the gates. Tier 2 work has been done partially without them; that work may need redo.

1. **Physical interpretation of edge and node.** Adopt across/through (or an equivalent physically-grounded distinction). Edges and nodes must have *different* physical roles, derivable from a small set of conservation laws, not abstract "magnitude vs phase."

2. **A stable update rule that works at 2D hex coordination (3-edge junctions).** The current chapter 1 §7 cos-weighted rule is unstable at coord 3 (`sim-dial-comparison.py`). Whatever rule the across/through framing produces must be verified stable in 2D, not just in 1D linear arrays.

3. **Two-phase vs. single-phase clock — pick deliberately.** Yee-style staggered (chapter 1's choice) and one-shot scattering (sim-maxwell's choice) are both viable. The choice should follow from the across/through structure, not be inherited from grid-lab without thought.

4. **Couplet as building block, verified in 2D.** Build a small 2D hex sheet of couplets, perturb, watch wave propagation. Confirm the discrete wave equation emerges. This is the simplest sanity check we have not yet done.

---

## Tier 2 — substantive deliverables

These deliver on what the brainstorm promised. They depend on Tier 1 being clean.

5. **Couplet exact-tiling theorem for the 2D hex sheet.** Either a clean proof or a demonstration on a finite torus that the (edge, node) couplet tiles without orphans under the recursive 120°/240° split rule.

6. **Wrap-promotion ladder definition, level by level.** What is L0, L1, L2, L3 *physically*? What emerges at each level? What stays the same? Right now the ladder is sketched but each level's content is loose.

7. **Node-from-edges question.** The brainstorm's central derivation. Currently chapter 2's main content. Whether and how a node emerges from a 2π wrap of edges. The chapter 2 result needs to be re-derived under whatever framing Tier 1 settles.

---

## Tier 3 — ambitious finishes

These depend on Tier 1 and Tier 2 being clean.

8. **Where in the ladder does α appear?** Currently framed as a second-order-wrap phenomenon (theory 7). Verify or revise.

9. **Bridge to grid.** Now informed by what grid's sim code actually uses (sim-maxwell: traveling waves on edges, vertex scatterers, no node state). A duality / coarse-graining argument is needed.

10. **Closing summary, comparison with grid-primitive.** Where the analog-first cylinder and digital-first couplet models converge / diverge.

---

## Cleanup

### Delete (exploratory, superseded)

- `scripts/output/A-closed-N6-random.png`
- `scripts/output/B-closed-N6-delta.png`
- `scripts/output/C-open-M6-random.png`
- `scripts/output/D-open-M6-pinned.png`
- `scripts/output/E-closed-vs-node-driven.png`
- `scripts/output/notes.txt`
- `scripts/sim-couplet-collective.py` — early orientation, results superseded; the Nyquist-at-even-N finding is captured in conversation but not used downstream.

### Keep (still load-bearing)

- `scripts/render-configs.py` and `scripts/output/configs.png` — the chapter 2 §2 figure.
- `scripts/sim-dial-comparison.py` and `scripts/output/dial-comparison*.{png,txt}` — the cos-weighted instability finding is the evidence behind the Tier 1 update-rule problem. We'll cite it.

### Rewrite (after Tier 1 decision)

- `01-foundation.md` §7 (the update rule) — and possibly §2, §3 (point/edge definitions) if the across/through framing changes them.
- `02-closure-and-bounding.md` — the closure argument depends on phase being a state variable; if the paradigm changes, chapter 2 either needs rewriting or moving to "open question."

### README revision

- Add an across/through-variable section to the model description (or move that to chapter 1 and reference it).
- Update theory 7 (α) once we know whether the chapter 2 closure-and-bounding argument survives Tier 1.
- Soften any claims that depend on the cos-weighted rule until that's resolved.

---

## Open issues raised but not settled

- The cos-weighted update rule from grid-lab is structurally unstable at 3-coordinated geometry. Either grid-lab's rule was intended only for 2-coordinated linear arrays, or it needs normalization/damping at higher coordination, or our adoption of it was wrong.
- sim-maxwell uses an entirely different paradigm: edges carry `(a_fwd, a_bwd)` traveling-wave amplitudes, vertices apply a scattering matrix, no per-vertex state. Single-phase clock. This should inform Tier 1.
- The "node = dial at the lattice scale" macro convention is justified by encapsulation (chapter 2 §8). The justification holds, but only because the dial's externally-visible state is one connecting point's value at a time. If Tier 1 changes the dial's structure, this convention may need revisiting.
- The "winding number" derived in chapter 2 §5 is a topological invariant of the closed-loop phase pattern. It only exists if phase is a state variable. If Tier 1 drops phase, the winding number disappears with it.
- The chapter 2 information-capacity asymmetry argument (§7) compares continuous-unbounded to discrete-bounded. Solid in its own paradigm, but contingent on Tier 1.

---

## Things we know now that we didn't on day 1

- The cos-weighted node update at 3-coord is unstable at unit time-step.
- The Nyquist mode k = π is a defective eigenvalue of the Yee-style update on closed loops with even N — odd N stays stable.
- sim-maxwell does not store phase. Phase is implicit in time-history of amplitudes.
- The original brainstorm's hunch that "bounding has entropy" can be derived under a phase-on-vertices paradigm but doesn't transfer cleanly to other paradigms.
- The point / dial / node taxonomy (with "node" as the genus and "dial" as the lattice-scale species) is a clean naming convention but it took several iterations to land.
- The fractal-recursion language we initially imported from grid-primitive is not necessary here — points are 0D, edges are 1D, no sub-scale recursion is required by the model.

---

## Recommended next move

Resolve the Tier 1 decision: pick a physical interpretation (across/through or alternative) and a stable 2D-coordination update rule. This may mean rewriting chapter 1 §7 and parts of §2-§3. Once Tier 1 is solid, the chapter 2 closure argument can be revisited under the new framing — and the rest of the chapter arc gets clearer.

The next conversational step planned: discuss options for the physical-interpretation framing of edges and nodes (across/through and alternatives), pick one, and rewrite Tier 1 around it.
