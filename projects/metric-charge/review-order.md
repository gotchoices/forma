# review-order.md — Review of wrap-order refactor pass

Review of the in-progress refactor described in [work-order.md](work-order.md): the agent has reordered `T(m, n)` tuples from `(ring, tube)` → `(tube, ring)` across chapters 1–9 and the working documents, and updated the mass formula, wavenumber formulas, and reflection-index labels. The math is clean where it has been touched.

The refactor has, however, been **narrowly targeted at formal-syntax instances** (the `T(a, b)` tuples, the mass formula, `k_u`/`k_w` formulas, `m_opt → n_opt`, and the `R_u`/`R_w` index-flip labels). It misses prose contexts where `m` and `n` are *named in words* as "ring winding" or "tube winding," or where the chapter narrates which letter corresponds to which compact direction. These prose pairings have not been consistently flipped to match the new convention, so the chapters now contain internal contradictions between the formal tuple convention (stated in Ch 1 §10 line 376) and the prose elsewhere that still describes m as the ring winding (the old convention).

This file enumerates the confirmed misses and the verification work the integration agent should add to a follow-up pass before declaring the refactor complete.

---

## Confirmed misses (specific lines)

### Ch 1 §3 line 150 — diagram caption uses old convention

> "A closed curve traversing T(m, n) — **m wraps in ring, n wraps in tube** — crosses the right edge m times (reappearing at the left) and the top edge n times (reappearing at the bottom)."

Under the new convention `m = tube`, `n = ring`. The sentence should read:

> "A closed curve traversing T(m, n) — **n wraps in ring, m wraps in tube** — crosses the right edge n times (reappearing at the left) and the top edge m times (reappearing at the bottom)."

This is the user-pointed example. It is doubly important because the surrounding ASCII diagram (lines 133–148) uses ring/tube vocabulary — readers will compare letter-to-direction here, and the contradiction with Ch 1 §10 line 376 (the formal convention statement) is jarring.

### Ch 5 §4.5 line 260 — KK-correspondence narration uses old convention

> "The **tube direction (w) plays the role of standard KK's single compact direction.** The natural particle has definite **n in the tube**, the wave is traveling in w, and h_μw = B_μ survives — standard KK applied to the tube."

Under new convention `m = tube`, this should read "**definite m in the tube**". The next bullet (line 261) currently says "the standing-wave structure cos(k_u u)" which is fine (k_u uses n in the new convention; the formula doesn't expose the letter).

### STATUS.md line 57 — TODO-L5 description uses old convention

> "Trace how the framework's (m, n) signs determine charge sign of each component (under the natural-particle R_u-symmetrized construction, this is the sign of the **tube-direction wavenumber n**)."

Under new convention, the tube-direction wavenumber is `k_w = 2πm/L_w` — tied to `m`, not `n`. Should read "tube-direction wavenumber m" or equivalently "the sign of m (the tube winding)".

---

## Files that have not been touched at all

Per file timestamps, these were not updated in the refactor pass and likely contain old-convention content:

- **README.md** (timestamp predates refactor). Contains at least the references at lines 87, 92, 99, 154 in chapter summaries — possibly (m, n)-form mode listings.
- **STATUS.md** (timestamp predates refactor). Contains TODO descriptions referencing (m, n) signs, the closure rule, and the R_u-symmetrization mechanism. Line 57 is one confirmed miss; line 156's "(k_u, k_w)" reference may also be fine but warrants reading-pass verification.
- **shear-ratio.md** (timestamp predates refactor). Small file; needs spot-check.
- **review-m2.md** and **review-ch9.md** (review artifacts). work-order's §"Files to update" lists these. Decision needed: update for consistency, or mark explicitly as historical artifacts that retain old-convention wording.

---

## General pattern: prose pairings missed by the syntax pass

The agent's pass updated tuples and formulas but did not consistently update prose that *narrates* the convention. The two confirmed misses above are instances of a broader pattern that warrants a grep-driven sweep. Run these patterns and review each match:

```
"m wraps"           — should become "n wraps" (m is now tube, not ring)
"n wraps"           — should become "m wraps" (n is now ring, not tube)
"ring winding m"    — should become "ring winding n"
"tube winding n"    — should become "tube winding m"
"m (ring"           — old binding
"n (tube"           — old binding
"m, the ring"       — old binding
"n, the tube"       — old binding
"definite n in the tube"   — Ch 5 line 260 instance
"definite m in the ring"   — possible inverse instance, check
"sign of m" + nearby "ring"   — context-check (sign of which letter picks which direction's chirality?)
"sign of n" + nearby "tube"   — context-check
"wavenumber n" / "wavenumber m"   — context-check (k_u uses n, k_w uses m under new convention)
```

Each match needs a read-pass to determine whether the prose still aligns with the new letter-to-direction binding. Some matches are fine (e.g., "R_w (sign of m, the tube winding)" at Ch 5 line 394 correctly states that R_w flips m, the tube winding under new convention). Others are misses (e.g., Ch 5 line 260). The distinction is whether the prose treats `m` as bound to tube (new) or to ring (old).

---

## Subtle items to verify

### Ch 5 §5.1 — the single-axis example switched directions

Pre-refactor: the section's worked example was `(m, 0)` which under old convention was "ring-only" (since old `m = ring`). After the literal letter-swap, `(m, 0)` is now "tube-only" (since new `m = tube`). The agent has correctly relabeled it as "tube-only: m ≠ 0, n = 0" at line 391.

This is mechanically consistent. But the *primary worked example* has changed character: pre-refactor it was the ring-only case, now it is the tube-only case. Read-pass should confirm:

- The §5.1 analysis (lines 391–398) reads cleanly with the tube-only example as primary.
- Any downstream references to "the §5.1 example" (in Ch 5, in later chapters) still track.
- If the choice of primary example matters narratively (e.g., it was deliberately the ring-only case because of an inheritance from metric-mass), consider swapping the example back by writing it as `(0, n)` (the ring-only case under new convention) — preserves the original narrative intent without breaking the convention.

### `m_opt` → `n_opt` rename — verify no straggling references

Confirmed updated in Ch 8 §2.3 (line 140) and Ch 9 (line 71). Verification grep:

```
m_opt
```

If any survive outside of `work-order.md` (which describes the rename), they are misses.

### Mirror-variant statement in Ch 4 §4.4 line 224

> "Closure under the mirror variant requires **n | m** instead of m | n."

This *is* correct under the new convention (the mirror variant swaps u and w roles, so the closure rule's letter pair flips), but the prose is now slightly counterintuitive — "n | m" under new convention is structurally the same rule as the *old convention's* standard closure. A short clarifying note may help the reader: "(the rule under the mirror is the algebraic mirror of the standard rule, equivalent to the old `(ring, tube)` tuple convention's standard rule)." Optional polish; not required.

### Stress-energy descriptive entries in Ch 5 §3.1 (around line 112)

The table entries describe sourcing conditions:

- `T_tu | −ω · k_u | any mode with k_u ≠ 0 (n ≠ 0, ring)`
- `T_S₁u | k_{S₁} · k_u | any mode with both k_{S₁} ≠ 0 and k_u ≠ 0`

Under new convention, `k_u = 2πn/L_u` with `n` = ring winding. The "n ≠ 0, ring" parenthetical is correct. The corresponding T_tw / T_S_iw rows should have "m ≠ 0, tube" parentheticals — verify these are present and correct in the table immediately following (a grep for `m \\u2260 0` or `m ≠ 0` will help).

### viz/ directory and any rendered diagrams

The user's exemplar miss (Ch 1 line 150) involves an ASCII diagram caption. Other diagrams or figure captions across chapters 1–9 may have similar issues. Grep targets:

```
ring (m)
tube (n)
m wraps
n wraps
m-direction
n-direction
m-winding
n-winding
```

Also: if `viz/` contains any captions or labels that bind letters to directions, those need a pass.

---

## Recommendation

A second pass is needed before the refactor can be declared complete. The pass should:

1. **Fix the confirmed misses** (Ch 1 line 150, Ch 5 line 260, STATUS.md line 57) — these are explicit contradictions with the new convention.
2. **Touch the untouched files** (README.md, STATUS.md, shear-ratio.md, and review-*.md) — apply the same convention transformations as the chapter pass.
3. **Run the grep patterns** under §"General pattern" above and review every match for letter-to-direction binding correctness.
4. **Verify the subtle items** (Ch 5 §5.1 example, m_opt cleanup, mirror-variant statement, stress-energy descriptive rows, viz/).
5. **Final smoke test:** pick a closure-satisfying mode (e.g., T(1, 2)) and trace it through every chapter. Confirm that descriptions like "the lightest closure-satisfying primitive" or "the electron-like mode" use the same (m, n) ordering and the same letter-to-direction interpretation throughout.

Estimated effort: a focused half-day pass. The misses are concentrated in prose seams rather than spread evenly; the grep-driven sweep should catch most of them quickly. The two-step pattern (fix-confirmed-misses + grep-sweep + smoke-test) is the path to a clean refactor.
