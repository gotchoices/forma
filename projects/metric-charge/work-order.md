# work-order.md — Notation refactor: (ring, tube) → (tube, ring) tuple ordering

## Goal

Bring metric-charge's tuple notation into alignment with the R-track studies' convention so that `T(m, n)` reads identically across studies, visualizations, and metric-charge.

**Current convention (metric-charge):** `T(m, n) = T(ring, tube)`. First index is ring winding; second is tube winding. Primitives are `T(m', 1)` (second index = 1 = tube).

**Target convention (matches studies):** `T(m, n) = T(tube, ring)`. First index is tube winding; second is ring winding. Primitives are `T(1, n')` (first index = 1 = tube).

The coordinate labels `u = ring` and `w = tube` are **unchanged**. Only the integer-winding letters `m` and `n` rebind to their compact directions: `m ↔ w (tube)` and `n ↔ u (ring)` after refactor.

The math is invariant under this relabeling. No derivations need to be redone. This is a mechanical notation refactor.

---

## Transformation rules

Apply these consistently across every affected file.

### Tuple ordering
- Every `T(a, b)` becomes `T(b, a)` — first/second index swap throughout.
- `k × T(m', 1)` becomes `k × T(1, n')` — the trivial-winding "1" moves to the first position.
- Multi-component compositions: `T(km', k)` becomes `T(k, kn')` (the gcd-reduced composite).

### Variable rebinding
| Symbol | Old binding | New binding |
|---|---|---|
| m (winding letter) | u (ring) | w (tube) |
| n (winding letter) | w (tube) | u (ring) |
| u (coordinate) | ring | ring (unchanged) |
| w (coordinate) | tube | tube (unchanged) |
| ε = L_u / L_w | (unchanged) | (unchanged) |

### Wavenumber formulas
- Old: `k_u = 2π m / L_u`, `k_w = 2π n / L_w`
- New: `k_u = 2π n / L_u`, `k_w = 2π m / L_w`

(The compact-direction wavenumber gets the index now bound to that direction.)

### Mass formula
- Old: `μ²(m, n; σ, ε) = m²/ε² − 2σmn/ε + n²`
- New: `μ²(m, n; σ, ε) = n²/ε² − 2σmn/ε + m²`

The 1/ε² scaling moves from the first-index square to the second-index square (because ε scales the ring-direction contribution, and ring is now the second index). The cross-term `σmn` is invariant under the relabeling.

### Discrete reflections (Ch 8 §2.1)
- Old: R_u maps `(m, n) → (−m, n)`. R_w maps `(m, n) → (m, −n)`. R_J = R_u ∘ R_w maps `(m, n) → (−m, −n)`.
- New: R_u maps `(m, n) → (m, −n)` (ring-direction reflection now flips the second index). R_w maps `(m, n) → (−m, n)` (tube-direction reflection now flips the first index). R_J unchanged: `(m, n) → (−m, −n)`.

### Closure rule (Ch 1 §10)
- Old: `T(m, n)` closure-satisfies iff gcd-reduced primitive is `T(m', 1)` for some integer m' ≥ 1. Equivalent: `n | m` with both nonzero.
- New: `T(m, n)` closure-satisfies iff gcd-reduced primitive is `T(1, n')` for some integer n' ≥ 1. Equivalent: `m | n` with both nonzero.

The synchronization test in Ch 1 §10 needs its parameterization swapped accordingly.

### Optimal-mode language
- Old: `m_opt = round(σε)` for the ring winding.
- New: `n_opt = round(σε)` (ring winding now labeled n). Update any chapter referencing `m_opt` to use `n_opt`.

### Wrap-order's chirality-sector pick (Ch 8 §2.2)
- Old: "the wrap-order picks the sign of m for which μ² is lower."
- New: "the wrap-order picks the sign of n for which μ² is lower." (Still picks the sign of the ring winding; the letter has changed.)

### R-track quark mode references (work-L5.md, and downstream pointers)
In work-L5.md §2 (R-track context), the quark mode assignments already use the studies' convention (e.g., `u = (1, 19)` meaning tube = 1, ring = 19). After refactor, these match the metric-charge convention directly — no change to the studies' tuples themselves, just to the surrounding metric-charge prose that compares them.

---

## Files to update

### Chapters (primary scope)
- `01-foundation.md` — closure rule statement, wrap-order convention, T(m, n) topological characterization, synchronization test.
- `02-*.md` through `09-ratio-and-shear.md` — every chapter that uses T(m, n) tuples, the mass formula, wavenumber formulas, or R_u/R_w/R_J reflections.
- Particularly heavy passes expected in: Ch 4 (closure condition), Ch 5 (gauge-potential derivation including the new §4.6.1–4.6.5), Ch 8 (shear and fractional charge — mass formula, single-Bloch-mode, multi-link, fractional charge), Ch 9 (lepton-like / hadronic-like / neutrino-like sheet mode assignments).

### Working documents (in current scope)
- `work-m2.md` — recently integrated; uses (m, n) tuples and mass formula in §3.1's stress-energy table.
- `work-L5.md` — just framed; uses (m, n) tuples and four-mode table in §1.
- `review-m2.md`, `review-ch9.md` — historical artifacts; update for consistency if they're kept as referenced documents.

### Status and bookkeeping
- `STATUS.md` — review for any (m, n) tuples in TODO descriptions.
- `README.md` — verify it does not contain T(m, n) references that would need updating.

### Visualizations
- `viz/` (if metric-charge has any) — spot-check that visualizations and their captions use the target convention. Likely already aligned with studies but worth confirming.

---

## Files NOT to update

- **`projects/metric-mass/`** — 1D-compact only; no (m, n) tuple notation applies.
- **`projects/grid-duality/`** — uses abstract `(w_α, w_β)` notation; no metric-charge-style ring/tube tuple convention to update.
- **`studies/`** (entire R-track) — already in target convention; no changes.
- **`projects/metric-binding/`** — not yet developed in detail; will inherit the target convention naturally.

If any of grid-duality's abstract pairs benefit from concrete (tube, ring) interpretation later, that is a separate downstream item, not part of this work order.

---

## Verification approach

After the chapter-by-chapter editing pass:

1. **Global grep verification.** Search the metric-charge directory for:
   - `T(` — confirm every tuple has tube winding in first position (1 in first position for primitives; small integer in first position for multi-component composites).
   - `m_opt` — confirm renamed to `n_opt` consistently.
   - `m^2/\varepsilon^2`, `m²/ε²` — confirm any surviving instance is intentional (e.g., quoting old text); after refactor the 1/ε² scaling should multiply `n²`.
   - `2σmn/ε`, `2\sigma mn/\varepsilon` — invariant; should still appear with same sign.

2. **Reading pass.** A full read-through of each chapter checking for:
   - Mismatched language ("ring winding m" should become "ring winding n", etc.).
   - Tables, diagrams, and captions: every tuple correctly ordered.
   - Cross-references to other chapters' (m, n) examples remain consistent.

3. **Smoke test.** Pick one or two specific mode references that appear across multiple chapters (e.g., the electron-like primitive, a quark mode from Ch 9 §5) and trace through every appearance to confirm consistency.

---

## Approach and sequencing

Work chapter-by-chapter to avoid mid-refactor inconsistency:

1. Start with `01-foundation.md` (sets the convention; downstream chapters cite it).
2. Proceed sequentially through chapters 2–9.
3. Update `work-m2.md` and `work-L5.md` after the chapters are done — they cite chapter content.
4. Update `STATUS.md`, `review-*.md`, and `README.md` last.
5. Run global grep verification.
6. Do the reading pass.

**Estimated effort:** 1–2 days for the editing pass, plus a half-day verification.

**Single coordinated pass recommended.** Do not split across multiple sessions if avoidable — partial refactor states are error-prone.

---

## Notes on aesthetic and reader experience

The current convention (ring first) has a minor visual advantage: the mass formula `m²/ε² − 2σmn/ε + n²` puts the 1/ε²-scaled term in the natural-looking first position. After refactor, `n²/ε² − 2σmn/ε + m²` puts the 1/ε²-scaled term second — slightly less natural-feeling at first glance, but mathematically identical and consistent with how the studies present the same formula.

Closure-satisfying primitives `T(1, n')` (the new form) have the "1" in front — readers familiar with torus-knot notation will recognize this as the more standard `T(p, q)` convention where `p = 1` indicates the trivial wrapping. The change is on net a readability improvement once readers acclimate.

A secondary typographic payoff: after the refactor, the letter shapes themselves hint at the pairing. The new `m ↔ w` binding pairs visual mirrors (m and w are vertically reflected forms of one another); likewise `n ↔ u` pairs the other vertical-mirror pair. Under the current convention the pairings are crossed — `m ↔ u` and `n ↔ w` — so each integer letter is paired with the coordinate that looks like its *opposite* number. The refactor brings the typography into alignment with the math: each integer winding's letter is shaped like the coordinate it parameterizes.

The refactor's primary payoff is consistency across the repo: a reader moving between a study, a visualization, and a metric-charge chapter will see the same tuple ordering everywhere. This compounds over time as the corpus grows.
