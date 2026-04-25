# R64 Track 4 — Hadron inventory audit at the chain-fit Point B

Track 4 tests whether the chain-fit candidate working point
identified in Track 3 (Point B at `(ε_p, s_p, K_p) =
(0.2052, +0.0250, 63.629)`) preserves the 13-particle hadron
inventory under R64's flavor-aware composition rule.

**Result: structurally informative partial failure.**

The strange-bearing hadron inventory (Ω⁻, Ξ, Σ, Λ, K) does **not**
identify with a single strange-quark primitive `(n_t_s, n_r_s)` at
Point B.  Each particle picks its own best-fit strange primitive,
and the per-particle fits are excellent (most within ~1%) — but
the choices are inconsistent across the strange family.  Forcing
a single global `(n_t_s, n_r_s)` for all strange hadrons gives
RMS error 18%, well outside the 5% inventory gate.

This is the same structural issue that surfaced in Track 2 Phase
2a at Point A: R64's flat-formula additive winding does not
naturally reproduce the SM's near-isospin-symmetric structure for
light hadrons, regardless of which `(ε_p, s_p)` point is chosen.
Σ⁺ and Σ⁻ in nature differ by 0.7% (nearly degenerate via isospin
symmetry); in R64 with additive winding the same swap (replace
two u's with two d's) shifts n_r by 8 units, giving very different
predicted masses.

But there's an important nuance: the body of the nuclear chart
(many nucleons, large n_t) is captured well at Point B because
the (1/ε)² term dominates the mass formula at large n_t and
washes out fine n_r differences.  For light hadrons (Σ, K, deuteron)
where n_t is small and n_r differences matter, R64's formula
predicts large mass splits that nature doesn't show.

Script:
[`scripts/track4_inventory_at_point_B.py`](scripts/track4_inventory_at_point_B.py)
Outputs:
[`outputs/track4_phase4a_strange_search.csv`](outputs/track4_phase4a_strange_search.csv)

---

## Phase 4a — Strange-bearing hadron inventory at Point B

### Method

For each strangeness-bearing hadron, scan the `(n_t_s, n_r_s)`
lattice for the best-fit strange primitive given R64's additive
winding composition.  Then test whether a single `(n_t_s, n_r_s)`
fits all strange hadrons simultaneously (the "single strange
quark" requirement of SM flavor physics).

### F4a.1. Per-particle fits at Point B are excellent

Each particle finds a primitive within ~2.5% of observed:

| Particle | Observed | Best (n_t_s, n_r_s) | Predicted | Err | Z₃ for baryon |
|:---|:-:|:-:|:-:|:-:|:-:|
| Ω⁻ (sss) | 1672.45 | (−1, 7) | 1632.05 | −2.42% | ✓ |
| Ξ⁻ (dss) | 1321.71 | (−1, 11) | 1311.36 | −0.78% | ✗ |
| Ξ⁰ (uss) | 1314.86 | (−1, 9) | 1311.36 | −0.27% | ✗ |
| Λ (uds) | 1115.68 | (−5, −10) | 1124.36 | +0.78% | ✓ |
| Σ⁺ (uus) | 1189.37 | (0, 12) | 1189.37 | 0.00% | ✗ |
| Σ⁻ (dds) | 1197.45 | (0, −12) | 1194.80 | −0.22% | ✗ |
| Σ⁰ (uds) | 1192.64 | (−5, −12) | 1200.46 | +0.66% | ✓ |
| K⁺ (us̄) | 493.68 | (0, 8) | 493.07 | −0.12% | ✗ |
| K⁰ (ds̄) | 497.61 | (0, 4) | 493.07 | −0.91% | ✗ |

The per-particle search finds excellent matches (8 of 9 within
1%; worst case Ω⁻ at 2.4%).  **Mass-wise, the lattice contains the
right values.**

But the chosen `(n_t_s, n_r_s)` values are wildly inconsistent:

- n_t_s ranges over `{−5, −1, 0}`
- n_r_s ranges over `{−12, −10, 4, 7, 8, 9, 11, 12}`

There is no single `(n_t_s, n_r_s)` shared across the strange
family.  Each particle gets its own strange primitive.

### F4a.2. Many per-particle fits violate Z₃ at the baryon level

Z₃ confinement (R60 T16) requires baryon `n_pt ≡ 0 (mod 3)`.  But
the per-particle best-fits give baryon n_pt values like:

- Ξ⁻ at n_pt = −1 (not Z₃-compatible)
- Σ⁺ at n_pt = 2 (not Z₃-compatible)
- K⁰, K⁺ at n_pt = 1 (mesons need n_pt = 0 for color singlet
  via q-q̄)

So even at the per-particle level, MaSt's lattice can produce
the right masses but the assignments break the framework's
internal selection rules.  This is structurally significant —
it suggests the "particle-by-particle mass fit" found at Point
B is NOT a coherent flavor model, just a numerology coincidence
from the lattice's density.

### F4a.3. Single global (n_t_s, n_r_s) fails the inventory gate

Forcing a single `(n_t_s, n_r_s)` for all strange-bearing hadrons
and minimizing RMS error: best at `(n_t_s, n_r_s) = (2, 3)` with
**RMS error 17.97%**.

Particle-by-particle results at this best global fit:

| Particle | Observed | Predicted | Err |
|:---|:-:|:-:|:-:|
| Ω⁻ | 1672.45 | 1943.85 | +16.23% |
| Ξ⁻ | 1321.71 | 1569.90 | +18.78% |
| Ξ⁰ | 1314.86 | 1629.38 | **+23.92%** |
| Λ | 1115.68 | 1253.98 | +12.40% |
| Σ⁺ | 1189.37 | 1315.74 | +10.63% |
| Σ⁻ | 1197.45 | 1242.31 | +3.75% |
| Σ⁰ | 1192.64 | 1253.98 | +5.14% |
| K⁺ | 493.68 | 316.23 | **−35.94%** |
| K⁰ | 497.61 | 443.12 | −10.95% |

8 of 9 particles outside the 5% gate; K⁺ off by 36% and Ξ⁰ off
by 24%.  **The inventory gate fails at Point B under a coherent
SM-style flavor identification.**

### F4a.4. Why the inventory fails: the SM isospin near-symmetry doesn't fall out

The structural issue, same as Track 2 Phase 2a at Point A:

- In nature, **Σ⁺ (uus) and Σ⁻ (dds) differ by 0.7%** (8 MeV) —
  near-degeneracy from SU(2) isospin symmetry.
- In R64 additive winding, the same swap (uu→dd) changes `n_r`
  by 8 units (from +4 to −4).  At Point B with `s_p = 0.025`,
  this gives a mass change of order
  `K_p · 2 · 8 / |n_r typical| ≈ 30 MeV` — much larger than the
  observed 8 MeV split.
- Same for K⁺ vs K⁰.

The mass formula's natural metric in (n_t, n_r) is **linear in
n_r differences** for small n_t, which is incompatible with the
SM's near-degenerate u/d isospin structure.

This problem is **independent of the magic point choice** — it's
structural to the additive-winding rule.  Point A had it (Track
2 Phase 2a); Point B has it too.

### F4a.5. The bulk-vs-fine-flavor distinction

Why does Point B work for ⁵⁶Fe (within 2%) but fail for Σ
(off by 10–15%)?  Different sensitivity to n_r vs n_t:

- **⁵⁶Fe**: n_t = 168 dominates.  The `(n_t/ε)²` term is
  ~671,000; the `(n_r − sn_t)²` term is at most ~150 (for n_r
  up to 8).  Mass is essentially `K_p · n_t/ε`, near-linear in
  A.  Different Z values shift n_r by O(few) but mass changes
  by O(0.1%).  **Mass is largely n_t-driven for heavy nuclei.**
- **Σ⁺ vs Σ⁻**: n_t = 2 (small).  `(n_t/ε)²` is ~95; `(n_r − sn_t)²`
  is ~20–50 (comparable scale).  Different Z assignments
  (uus vs dds) shift n_r by 8 units, changing the second term
  by ~30%.  **Mass is sensitive to flavor composition for
  light hadrons.**

So R64 works for the **bulk** of nuclear physics (heavy nuclei,
nucleons) but fails for **fine flavor structure** (light
hadrons, isospin partners).  This is informative — it tells us
where R64's harmonic-stack model has structural validity and
where it doesn't.

### F4a.6. What Phase 4a establishes

1. **The hadron inventory does NOT cleanly fit at Point B**
   under strict additive winding with a single strange-quark
   primitive.  RMS error is 18%, well outside the 5% gate.
2. **The lattice contains the right mass values** (per-particle
   fits within ~2%), but the SM-style flavor identification
   (one strange quark for all strange hadrons) doesn't map
   onto a single primitive.
3. **The structural problem is independent of the magic-point
   choice**: same isospin near-symmetry issue at both Point A
   (deuteron-anchored) and Point B (chain-anchored).
4. **R64's harmonic-stack works for bulk nuclear structure**
   (heavy nuclei, n_t-dominated) but **fails for fine flavor
   structure** (light hadrons, n_r-sensitive).

### F4a.7. What this means for R64

The full picture across Tracks 1–4:

- **Foundational masses (m_p, m_n, m_d at Point A)**: ✓ exact
  by construction (3-parameter, 3-observable anchor).
- **Body of nuclear chart at Point B (Ca → Sn)**: ✓ within 1–2%.
- **Heavy nuclei at Point B (Pb, U)**: ~5–9% (likely Coulomb-
  related).
- **Deuteron at Point B**: ✗ outlier (predicted 7.8× too bound).
- **Light hadron inventory (Σ, K) at either point**: ✗ SM
  isospin near-symmetry breaks (errors 10–35%).

R64 captures the **strong force binding curve** in the body of
the nuclear chart but does **not** capture the SM's flavor
structure at light hadrons.  The "strong force is geometric on
the p-sheet" hypothesis survives partially: it works for nuclear
binding but doesn't reach the light-flavor sector under strict
additive winding.

Two readings:

**Reading A — partial success.**  R64 is a working theory of
nuclear binding (its narrowest claim), but does not extend to
light-flavor structure.  R63's cross-sheet model handled light
hadrons differently and may still apply there.  R64 supersedes
R63 for nuclei but not for the meson/hyperon inventory.  This
is a coexistence — neither candidate "wins" at the model-G
promotion level until both questions are resolved.

**Reading B — composition rule needs revision.**  Strict
additive winding is wrong; some other rule (multi-mode coherence,
non-additive winding, group-theoretic structure on the
generations) might preserve both nuclear binding AND SM flavor
near-symmetry.  Worth searching for, but no specific candidate
has been identified.

---

## Status

**Phase 4a complete.  Inventory gate fails at Point B under
strict additive winding.**

R64 currently has:
- A nuclear-binding success at Point B (body of chart within
  1–2%).
- A foundational success at Point A (anchor coincidence).
- An inventory failure at both points (light-hadron SM flavor
  structure).
- A deuteron-outlier puzzle at Point B.

R64 is **not falsified** but is also **not pinning** to a single
working point yet.  The chain-fit Point B remains the best
candidate for nuclear binding; the light-hadron sector requires
either a different mechanism or a different model entirely.

Next-track candidates:

- **Track 5 — investigate the deuteron outlier and light-A
  binding shape.**  Why does R64 over-predict B(²H) at Point
  B by 8× while reproducing heavy nuclei within a few percent?
  The structural answer might illuminate Reading B.
- **Track 6 — Coulomb-coupling audit.**  Why does R64 at Point
  B match raw observed binding rather than Coulomb-subtracted?
  Diagnostic for what physics R64 implicitly captures.
- **Track 7 — alternative composition rules.**  Test multi-mode
  coherence or non-additive winding as a rule that might fix
  both the deuteron and the isospin near-symmetry.
- **Continue with quark generations (Track 2 redo at Point B).**
  Charm and bottom searches; they may fail similarly to strange,
  confirming the structural limit; or one of them might land
  cleanly, distinguishing the bulk vs fine sectors more sharply.

User direction needed.
