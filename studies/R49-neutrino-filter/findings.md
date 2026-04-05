# R49 Findings

Study: [`README.md`](README.md)

---

## Track 1: Constraints on ε_ν

Script: [`scripts/track1_epsilon_constraints.py`](scripts/track1_epsilon_constraints.py)

### Summary

The (ε_ν, s₃₄) parameter space is **broadly viable** — not
tightly constrained.  257 fully viable solutions found across
ε from 0.1 to 5.0 and s from 0.001 to 0.4, with 22 unique
mode triplets.  The data does NOT uniquely select a neutrino
mode assignment.  The main discriminator is the **sterile
count**: small ε gives hundreds of intermediate modes, while
large ε gives tens.

### What the data actually constrain

Individual neutrino masses have never been directly measured.
Oscillation experiments measure two mass-squared *differences*:

- Δm²₂₁ = 7.53 × 10⁻⁵ eV² (solar)
- Δm²₃₁ = 2.530 × 10⁻³ eV² (atmospheric)

The absolute mass of the lightest state (m₁) is unknown and
could be anywhere from ~0 to ~40 meV.  The cosmological bound
constrains only the sum: Σm < 120 meV.

The sweep procedure: (1) find mode triplets whose dimensionless
μ² values reproduce the *ratio* Δm²₃₁/Δm²₂₁ = 33.6, then
(2) set the energy scale E₀ so that Δm²₂₁ matches the measured
value exactly.  This fixes all three masses as **predictions**,
not fits.  Different families predict different m₁ values:
Family A → m₁ ≈ 29 meV, Family B → m₁ ≈ 5 meV.  Both are
currently allowed; KATRIN or CMB-S4 will discriminate.

Each mode (n₃, n₄) at a given (ε, s) has a unique mass — so
if ε were known, each measured mass would map to exactly one
mode (up to n₃ → −n₃ symmetry).  The 22 candidate triplets
arise because we don't know ε: the same physical mass can be
different modes at different geometries.

### Sweep parameters

- ε_ν: 15 values from 0.1 to 100 (logarithmic)
- s₃₄: 16 values from 0.001 to 0.4
- Modes: |n₃| ≤ 10, n₄ ≤ 6
- Constraints: Δm²₃₁/Δm²₂₁ = 33.6 ± 0.9, Σm < 120 meV,
  normal ordering, spin ½ (|L_z/ℏ − 0.5| < 0.15)

### Results by phase

| Phase | Count |
|-------|-------|
| Mass-viable triplets (ratio + Σm + ordering) | 297,693 |
| Fully viable (+ spin ½) | 257 |
| Near-miss (spin within 0.25 of ½) | 3,443 |

### Three structural families of solutions

The 22 unique triplets cluster into three families:

**Family A: R26 Assignment A**
- Triplet: **(1,1), (−1,1), (1,2)**
- Viable at: ε = 5.0, s = 0.022
- Masses: m₁ = 29.2, m₂ = 30.5, m₃ = 58.2 meV
- Σm = 117.8 meV (tight against 120 meV bound)
- Spins: [0.36, 0.36, 0.37] — marginal (just inside tolerance)
- Sterile count: 26
- Sheet dimensions: L₃ ≈ 34 μm, L₄ ≈ 6.7 μm
- **Note:** Only 1 solution at this point in the grid.
  The modes have the lowest n₃ values of any family — the
  simplest topology.  But the spin values are 26–28% below
  the nominal ½, and Σm is only 2 meV below the cosmological
  bound.

**Family B: R24-like (thin torus)**
- Triplet pattern: **(±1,2), (±2,2), (±10,1 or ±10,2)**
- Viable at: ε = 0.1, all sampled s values
- Masses: m₁ ≈ 5.1, m₂ ≈ 10.1, m₃ ≈ 50.1 meV
- Σm ≈ 65 meV (well below bound)
- Spins: [0.50, 0.50, 0.50 or 0.40] — near-perfect
- **Sterile count: 120–128** (major problem)
- Sheet dimensions: L₃ ≈ 39 μm, L₄ ≈ 394 μm
- **Note:** Dominates the viable count (most of the 257).
  Clean spins and comfortable Σm, but the ν₃ mode has
  |n₃| = 10 — a very high tube winding.  At ε = 0.1,
  (10,1) has p²ε² = 1 which is the precise geometry where
  L_z/ℏ crosses ½.  The 120+ sterile modes would violate
  N_eff = 3 if they couple to weak interactions.

**Family C: Mixed**
- Triplet pattern: **(0,2), (−1,2), (±6,1 or ±6,2)**
- Viable at: ε = 0.2, s = 0.3–0.4
- Masses: m₁ ≈ 3.4, m₂ ≈ 9.3, m₃ ≈ 50.4 meV
- Σm ≈ 63 meV
- Spins: [0.35, 0.50, 0.42 or 0.37]
- Sterile count: 73–82
- Sheet dimensions: L₃ ≈ 23 μm, L₄ ≈ 117 μm
- **Note:** The (0,2) mode has zero tube winding — it
  could not carry charge even on a charged sheet.  This
  mode has L_z/ℏ = 0.35, which is marginal for spin ½.

Also found: **(1,2), (−1,2), (−2,2)** at ε = 0.2, s = 0.3,
with Σm = 118.3 meV (very tight) and 15 steriles.

### Waveguide cutoff landscape

The waveguide cutoff (open boundary: n₄ > |n₃|/ε) strongly
depends on ε:

| ε | (1,1) | (1,2) | (1,3) | (3,2) | (3,6) |
|---|-------|-------|-------|-------|-------|
| 0.1 | ✗ | ✗ | ✗ | ✗ | ✗ |
| 0.2 | ✗ | ✗ | ✗ | ✗ | ✗ |
| 0.5 | ✗ | ✗ | ✓ | ✗ | ✗ |
| 1.0 | ✗ | ✓ | ✓ | ✗ | ✓ |
| 2.0 | ✓ | ✓ | ✓ | ✓ | ✓ |
| 5.0 | ✓ | ✓ | ✓ | ✓ | ✓ |

At ε ≤ 0.2, **nothing propagates**.  Family B lives at ε = 0.1
where the waveguide kills all modes — suggesting either the
waveguide model doesn't apply to Ma_ν, or Family B is
unphysical.

At ε ≥ 2, nearly everything propagates.  Family A (ε = 5)
has no waveguide filtering at all — consistent with the
"less filtering on Ma_ν" instinct.

### Mode density (storage capacity)

At s = 0.022, with |n₃| ≤ 50, n₄ ≤ 10: approximately
1,110 modes total.  At ε ≥ 0.3, all modes are below 1 eV.
The mode density is very high at all ε — the storage
hypothesis (Q85) has ample substrate regardless of ε.

### Key tensions

1. **Spin vs ε.**  At small ε (thin torus), spins for low-n
   modes are near-perfect (0.50).  At large ε (Family A,
   ε = 5), spins drift to ~0.36.  The WvM spin formula at
   finite ε is a classical orbital calculation — quantum
   corrections or a different spin mechanism could rescue
   large-ε solutions.

2. **Steriles vs ε.**  Small ε gives 100+ sterile modes
   between ν₁ and ν₃.  Large ε gives 26.  The N_eff = 3
   constraint is hard to enforce at small ε unless sterile
   modes don't couple to weak interactions.

3. **Σm vs ε.**  Family A has Σm = 117.8 meV, 2 meV below
   the bound — very tight.  Family B has Σm ≈ 65 meV — 
   comfortable.  CMB-S4 will measure Σm to ~20 meV
   precision, which would strongly discriminate.

4. **Waveguide vs ε.**  At ε = 0.1, the waveguide kills
   everything, including the triplet modes themselves.
   This either rules out small ε or rules out the waveguide
   model for Ma_ν.

5. **Uniqueness.**  22 triplets match — the data does not
   uniquely select a mode assignment.  Additional physics
   (production mechanism, topological constraints, weak
   charge) is needed to narrow the field.

### Findings table

| ID | Finding |
|----|---------|
| F1 | The (ε_ν, s₃₄) parameter space is broadly viable: ε from 0.1 to 5.0, s from 0.001 to 0.4.  No narrow constraint region emerges from mass + Σm + spin alone. |
| F2 | 22 unique mode triplets match the experimental Δm² ratio to within 1σ.  The neutrino mode assignment is not uniquely determined by oscillation data. |
| F3 | Solutions cluster into three structural families: (A) low-n₃ modes at large ε with marginal spin, (B) high-n₃ modes at small ε with perfect spin but huge sterile count, (C) mixed modes at intermediate ε. |
| F4 | The sterile count is the strongest discriminator: 26 (Family A) vs 120+ (Family B) vs 73–82 (Family C).  N_eff = 3 strongly disfavors Family B unless sterile modes decouple from weak interactions. |
| F5 | Waveguide cutoff eliminates ALL modes at ε ≤ 0.2.  Family B (ε = 0.1) is incompatible with waveguide filtering.  Family A (ε = 5) has no waveguide filtering — all modes propagate. |
| F6 | Family A (R26 Assignment A) gives Σm = 117.8 meV — only 2 meV below the cosmological bound.  CMB-S4 (~20 meV precision) will be a definitive test. |
| F7 | Spin at finite ε is a significant concern: Family A modes have L_z/ℏ ≈ 0.36–0.37 at ε = 5, substantially below the nominal ½.  The WvM spin formula may need quantum corrections at large ε. |
| F8 | Mode density is high (~1,100 modes below 1 eV) at all ε ≥ 0.3, providing ample substrate for the information storage hypothesis regardless of ε. |
| F9 | The s₃₄ dependence is weak: most families match the ratio at many s values.  Family A uniquely requires s ≈ 0.022, but Families B and C work across the full s range. |
| F10 | Additional physics (production mechanism, weak charge, topology) is needed to select among the 22 candidate triplets.  The oscillation data alone does not pin the neutrino mode assignment. |

---

## Track 1a: Can many modes mimic three-flavor oscillations?

Script: [`scripts/track1a_multimode_oscillation.py`](scripts/track1a_multimode_oscillation.py)

### Question

Track 1 found 26–125 modes between ν₁ and ν₃.  If many of
them participate in oscillations (not just the 3 "neutrino"
modes), would experiments still see a clean 3-flavor signal?
Or would the extra frequencies be detectable?

### Method

For each Track 1 family (A: 29 modes, B: 125 modes, C: 77
modes), compute the multi-mode oscillation probability
P(ν_e → ν_μ) vs L/E using three coupling scenarios:

- **dominant3** — only the 3 neutrino modes carry weight
  (control: should reproduce the 3-mode signal exactly)
- **exp_decay** — coupling falls off exponentially with
  distance from the 3 neutrino modes (nearest-neighbor
  modes carry ~37% of neutrino coupling)
- **uniform** — all modes in the window carry equal weight

Then compare to the 3-mode-only signal and fit with a
standard 3-flavor PMNS model.

### Results

| Scenario | N_modes | Multi vs 3-mode RMS | Character |
|----------|---------|---------------------|-----------|
| Any family / dominant3 | — | 0.00% | Exact match (by construction) |
| Family A / exp_decay | 29 | 89.8% | Massive distortion |
| Family B / exp_decay | 125 | 64.0% | Massive distortion |
| Family C / exp_decay | 77 | 72.4% | Massive distortion |
| Any family / uniform | — | 290–375% | Completely different signal |

### Interpretation

The result is **unambiguous**: if extra modes carry any
significant fraction of the weak coupling, the oscillation
signal is drastically different from a clean 3-flavor pattern.
Even the "gentle" exponential-decay scenario (where neighboring
modes carry ~1/e of the neutrino coupling) produces residuals
of 64–90% of the signal amplitude — vastly above any
experimental noise level.

This means one of two things must be true:

1. **Only 3 modes couple to weak interactions.**  Some
   selection rule — topological, symmetry-based, or related
   to the waveguide/filtering structure — picks out exactly
   3 modes and suppresses all others.  The "sterile" modes
   truly are sterile (they exist on the sheet but don't
   interact weakly).

2. **The extra modes don't exist in the mass window.**
   If ε is large enough that few modes fit between ν₁ and
   ν₃, the problem vanishes.  Family A (ε = 5, 26 modes)
   is better than Family B (ε = 0.1, 125 modes) in this
   regard, but even 26 extra modes would be catastrophic
   if they all coupled.

The fact that experiments see a clean 3-flavor pattern is
itself a strong constraint: **whatever selection mechanism
operates on Ma_ν must be sharp enough to suppress coupling
of all intermediate modes to the weak sector.**  This is a
filtering requirement, even if it operates differently from
the waveguide cutoff on Ma_e and Ma_p.

### Findings table

| ID | Finding |
|----|---------|
| F11 | If extra modes carry even ~37% of the neutrino's weak coupling, the oscillation signal deviates by 64–90% from the 3-flavor pattern — far above experimental sensitivity.  The observed clean 3-flavor oscillations require sharp mode selection. |
| F12 | The "sterile count" problem (F4) is more severe than N_eff alone suggests: even modes that don't contribute to N_eff would distort oscillation patterns if they carry any weak coupling.  The selection mechanism must be nearly complete. |
| F13 | This result favors geometries with fewer intermediate modes (larger ε), since the selection mechanism has less work to do.  Family A (26 modes to suppress) is more plausible than Family B (125 modes). |

---

## Track 1b: First-above-cutoff triplet

Script: [`scripts/track1b_first_above_cutoff.py`](scripts/track1b_first_above_cutoff.py)

### Question

If the waveguide cutoff is the neutrino's mode selection
mechanism, the simplest scenario is that the first 3
propagating modes above cutoff ARE the neutrino triplet.
Does this work?

### Result: the literal first 3 never match

The Δm² ratio for the first 3 propagating modes was
computed across a fine (ε, s) grid.  **No solution was
found** — the first 3 modes above cutoff never produce a
ratio near 33.6.

Why?  At every ε, the first few propagating modes are
too closely spaced in mass.  At s = 0, the pattern is:

| ε range | First 5 propagating modes |
|---------|--------------------------|
| 0.3–0.5 | (0,1), (0,2), (0,3), ... — all n₃ = 0 |
| 0.7–1.0 | (0,1), (0,2), (±1,2), ... |
| 1.2–2.0 | (0,1), (±1,1), (0,2), (±1,2), ... |
| 2.5–10  | (0,1), (±1,1), (±2,1), ... |

The first 3 modes are always too close in mass — the
Δm²₂₁ is too large relative to Δm²₃₁, giving ratios
of ~2–5 instead of the needed 33.6.

### But: modes 0, 1, 5 DO match

When the search extends to the first 6 propagating modes
and tries all triplet combinations, 14 solutions appear.
The best matches:

| ε | s | Triplet | Ratio | Σm (meV) |
|---|---|---------|-------|----------|
| 2.50 | 0.036 | (0,1), (1,1), (0,2) | 33.60 | 117 |
| 3.00 | 0.011 | (0,1), (1,1), (0,2) | 33.62 | 117 |
| 2.00 | 0.085 | (0,1), (1,1), (1,2) | 33.44 | 118 |
| 2.80 | 0.280 | (1,1), (2,1), (2,2) | 33.50 | 117 |

These use modes at indices (0, 1, 5) — the 1st, 2nd, and
6th propagating modes.  Between the 2nd and 6th sit three
intermediate modes (typically the degenerate partners ±n₃
and higher-winding modes).

### Why modes 2–4 don't participate

At ε ≈ 2.5 with s ≈ 0.036, the first 6 modes are:

    (0,1), (1,1), (-1,1), (2,1), (-2,1), (0,2)

Modes 2–4 are the ±n₃ partners of modes already counted.
The pairs (1,1)/(−1,1) and (2,1)/(−2,1) are nearly
degenerate at small s.  If ±n₃ modes are identified as
particle/antiparticle pairs (same physical state, opposite
circulation), then the distinct mode count is:

    (0,1), (1,1), (0,2) — which IS the first 3 distinct modes.

This interpretation would rescue the "first above cutoff"
hypothesis, but requires that ±n₃ degeneracy be physical
(CPT conjugates) rather than coincidental.

### Tension: the (0,1) mode

The lightest mode in all solutions is (0,1) — zero tube
winding, pure ring circulation.  This mode has:

- Spin: L_z/ℏ = S(0,1)/1 = 1 at any ε (no tube winding
  means all angular momentum is orbital in the ring).
  **This is spin 1, not spin ½.**

- No helicity structure in the tube direction.

The (0,1) mode fails the spin-½ criterion.  To get
spin ½ for ν₁, we need n₃ ≠ 0.  This rules out the
(0,1), (1,1), (0,2) triplet and the (0,1), (1,1), (1,2)
triplet.

The one surviving solution uses **(1,1), (2,1), (2,2)** at
ε ≈ 2.8, s ≈ 0.28 — but this would need spin checks at
this ε.

### Key insight

The "first above cutoff" idea is on the right track but
needs a refinement: modes with n₃ = 0 must be excluded
(they have the wrong spin).  The effective selection rule
would be:

> **Keep only modes with |n₃| ≥ 1 that propagate
> above the waveguide cutoff.**

With this rule, the first few modes at ε ≈ 2.5 would be
(1,1), (−1,1), (2,1), (−2,1), (1,2), ... and the
question becomes whether any triplet from these matches
the ratio.  The (1,1), (−1,1), (1,2) Assignment A is
present at index (0, 1, 4) — again not the literal
first 3, but close.

### Findings table

| ID | Finding |
|----|---------|
| F14 | The literal first 3 propagating modes above waveguide cutoff never match the Δm² ratio at any (ε, s).  The mass spacing of the lowest modes is too uniform. |
| F15 | Matches at indices (0,1,5) exist at ε ≈ 2–3 with (0,1),(1,1),(0,2) — but ν₁ = (0,1) has spin 1, not spin ½, ruling out this assignment. |
| F16 | After excluding n₃ = 0 modes (wrong spin) and identifying ±n₃ as particle/antiparticle pairs, the "first distinct modes above cutoff" concept becomes viable but has not yet been confirmed quantitatively.  R26 Assignment A (1,1),(−1,1),(1,2) sits near the cutoff floor at ε ≈ 2–5. |
| F17 | The waveguide cutoff floor is at ε ≈ 1 for (1,1) and ε ≈ 0.5 for (1,2).  Below ε ≈ 1, no n₃ = ±1 modes propagate — setting a firm lower bound on ε if these modes are to exist. |
