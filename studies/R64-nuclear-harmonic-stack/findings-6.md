# R64 Track 6 — Flexible slot-configuration tool for nuclear shell hypotheses

Track 6 builds a computational framework for testing nuclear-shell-
structure hypotheses against observed nuclear physics, with no
commitment to a specific MaSt interpretation.  Each hypothesis is a
"slot configuration" specifying:

1. Which MaSt primitives serve as slots
2. The order in which slots fill
3. The per-slot capacity per isospin
4. Whether to add S-emergent Coulomb energy
5. Optional shell-closure binding bonuses

The tool reports fitness metrics: magic-A alignment (cumulative slot
counts at observed magic numbers), binding-curve shape (peak position,
residuals), and valley of stability (predicted Z/A vs observed).
This lets us experiment cleanly with various configurations.

**Note on previous Track 6**: the original Phase 6a (mass-ordered
cumulative-baryon analysis) was based on a wrong premise — it
assumed "shells = mass-ordered groupings" rather than "shells =
spatial separations forced by Pauli saturation."  That work has been
moved to `OBSOLETE_*` and is not part of the current Track 6.

Working under interpretation **B3**: each slot holds nucleons of
ONE isospin (proton or neutron), with Pauli capacity 2 per slot
(spin up/down).  Protons fill positive-n_r primitives; neutrons fill
negative-n_r primitives.  Magic numbers are per-isospin.

Script:
[`scripts/track6_phase6a_slot_tool.py`](scripts/track6_phase6a_slot_tool.py)
Outputs: per-hypothesis CSV files in [`outputs/`](outputs/).

---

## Phase 6a — Tool framework and baseline hypothesis tests

### Method

Built a `SlotConfig` dataclass parameterizing a nuclear-shell-
structure hypothesis.  For each config, the tool computes:

- **Magic-A alignment**: which slot is at each observed magic-A
  boundary, and what's its mass.
- **Binding curve**: predicted nuclear masses across the chain (84
  stable isotopes), residuals against AME2020.
- **Valley of stability**: for each A in the observed range, the Z
  that minimizes predicted mass.

Three hypotheses tested at R64's chain-fit Point B parameters
`(ε_p, s_p, K_p) = (0.2052, 0.025, 63.629)`:

- **H1 (baseline)**: mass-ordered slots (gcd=1 primitives), B3
  capacity, no Coulomb.  Pure R64-Ma binding.
- **H2 (+ Coulomb)**: H1 plus explicit S-Coulomb `0.71·Z(Z−1)/A^(1/3)`.
- **H4 (+ closure bonuses)**: H2 plus shell-closure binding bonuses
  at observed magic numbers (10, 5, 3, 2, 1, 1, 1 MeV).

### F6a.1. The mass-ordered slot list (gcd=1) at Point B

The first 20 proton slots in mass order:

| Slot | (n_t, n_r) | Mass (MeV) |
|:-:|:-:|:-:|
| 1 | (1, +1) | 316.2 |
| 2 | (1, +2) | 334.6 (u quark) |
| 3 | (1, +3) | 363.3 |
| 4 | (1, +4) | 400.2 |
| 5 | (1, +5) | 443.1 |
| 6 | (1, +6) | 490.6 |
| 7 | (1, +7) | 541.4 |
| 8 | (1, +8) | 594.7 |
| 9 | (2, +1) | 623.1 |
| 10 | (2, +3) | 647.9 |
| 11 | (1, +9) | 649.8 |
| 12 | (2, +5) | 695.6 |
| 13 | (1, +10) | 706.4 |
| 14 | (2, +7) | 761.7 |
| ... | ... | ... |

Mass ordering interleaves n_t=1 and n_t=2 modes.  (1, +1) is the
lightest by mass, but the user's hint suggested it might be
shear-ruled-out.  The tool can exclude it; we'll test that variant
in Phase 6b.

### F6a.2. H1 — Mass-ordered, no Coulomb (baseline)

| Metric | Value | Notes |
|:---|:-:|:---|
| Mean B/A error | 18.1% | dominated by deuteron outlier |
| Max B/A error | 678% | the deuteron |
| Predicted B/A peak | ¹⁴N (A=14) | observed ⁵⁶Fe |
| Fe binding ratio | **0.98** | very close |
| Pb binding ratio | **1.05** | close |

Valley of stability prediction (without Coulomb):

| A | Predicted Z | Observed Z | Δ |
|:-:|:-:|:-:|:-:|
| 4 | 2 | 2 | 0 ✓ |
| 16 | 8 | 8 | 0 ✓ |
| 40 | 21 | 18 | +3 |
| 56 | 29 | 26 | **+3** |
| 120 | 62 | 50 | **+12** |
| 208 | 108 | 82 | **+26** |
| 238 | 123 | 92 | **+31** |

H1 predicts roughly Z/A ≈ 0.52 (constant) for all nuclei — proton-
rich, the wrong direction.  Light nuclei happen to have Z/A ≈ 0.5
naturally so the prediction matches observed there; heavy nuclei
diverge significantly.

H1's binding curve happens to be fairly close to observed because
Point B's chain-fit IMPLICITLY fits raw observation (which already
includes Coulomb's effect).  The "good fit" without Coulomb is
deceptive — it's coincident, not structural.

### F6a.3. H2 — Mass-ordered + S-Coulomb (the right physics direction, wrong magnitude)

| Metric | Value | Notes |
|:---|:-:|:---|
| Mean B/A error | 42.1% | Coulomb double-counts at Point B |
| Max B/A error | 678% | deuteron |
| Predicted B/A peak | ²H (A=2) | observed Fe |
| Fe binding ratio | 0.74 | under-binds |
| Pb binding ratio | 0.56 | under-binds |

Valley of stability (with Coulomb):

| A | Predicted Z | Observed Z | Δ |
|:-:|:-:|:-:|:-:|
| 4 | 2 | 2 | 0 ✓ |
| 16 | 7 | 8 | −1 |
| 40 | 17 | 18 | −1 |
| 56 | 22 | 26 | **−4** |
| 120 | 42 | 50 | **−8** |
| 208 | 63 | 82 | **−19** |
| 238 | 69 | 92 | **−23** |

**This is structurally important.**  Adding Coulomb gives the
RIGHT DIRECTION on the valley of stability: predicted Z/A drops
from 0.50 to 0.29 with A, vs observed 0.50 to 0.39.  Coulomb
pushes the optimum toward neutron-rich nuclei naturally.

The valley is **qualitatively correct** — H2 captures that heavy
nuclei prefer N > Z.  The magnitude is too aggressive (Z drops
too far at heavy A), suggesting Coulomb's strength relative to
R64-Ma's contribution needs adjustment.  This is consistent with
Track 5's diagnosis: at Point B, adding Coulomb double-counts
because Point B implicitly absorbed it during chain-fit.

The CORRECT approach: refit `(ε_p, s_p)` jointly with explicit
Coulomb (= Point C from Track 5: ε=0.230, s=0.020) and re-run.
Phase 6a's tool supports this by configuring per-hypothesis
parameters (deferred to Phase 6b).

### F6a.4. H4 — Add shell-closure binding bonuses

Bonuses applied (per isospin, magic): 2:10, 8:5, 20:3, 28:2, 50:1,
82:1, 126:1 MeV.

| Metric | Value |
|:---|:-:|
| Mean B/A error | 45.9% (slightly worse than H2) |
| Predicted B/A peak | ⁴He (A=4) at 13.4 MeV/nucleon (over-bound by alpha bonus) |
| Fe binding ratio | 0.74 (essentially unchanged) |

The 10 MeV bonus at magic-2 over-stabilizes ⁴He (predicted B/A
13.4 vs observed 7.07).  The smaller bonuses at higher magics
don't shift the curve materially.

Conclusion: shell-closure binding bonuses are **subleading**
relative to R64-Ma + Coulomb's bulk.  They produce small
local-stability bumps but don't shift the curve's overall shape.
For the bulk shape, the dominant physics is R64-Ma's volume term
(plus Coulomb).  Shell closures only add ~1–10 MeV per magic
number, not the ~hundreds of MeV needed to shift the binding-curve
peak.

### F6a.5. What the tool reveals

The three hypotheses together give a clear structural picture:

1. **R64-Ma alone (H1)** captures the bulk binding curve roughly
   well at Point B, but with the *wrong valley of stability*
   (Z/A ≈ 0.52 constant, predicting proton-rich heavy nuclei
   that don't exist).
2. **R64-Ma + Coulomb (H2)** gives the **correct valley direction**
   (Z/A drops from 0.5 to 0.29 with A) — the right physics — but
   double-counts at Point B's chain-fit, breaking the binding
   magnitude.
3. **Adding shell-closure bonuses (H4)** is a small effect; doesn't
   fix the H2 magnitude problem.

The path to a correct model:
- **Joint refit of Point B with Coulomb** (Track 5's Point C
  approach) to avoid double-counting.
- **Possibly a surface-like S-side term** to capture light-nucleus
  binding deficit.
- **Shell-closure bonuses** as fine corrections after the bulk is
  right.

This is *exactly* what Track 5 already established.  Track 6's
contribution: the framework lets us experiment with these
modifications cleanly and check fitness systematically.

### F6a.6. The Fe peak is NOT in any tested hypothesis

None of H1, H2, H4 predicts the B/A peak at ⁵⁶Fe:

- H1 peaks at ¹⁴N (A=14)
- H2 peaks at ²H (A=2)
- H4 peaks at ⁴He (A=4) due to alpha closure bonus

To produce a Fe-region peak, the model needs:
- Light-A binding deficit (rises with A initially)
- Heavy-A binding deficit (Coulomb growing)
- These to cross near A=56

Coulomb alone provides the heavy-A drop.  Light-A rise requires
**surface** or another mechanism.  Without it, the curve descends
monotonically from the deuteron after Coulomb is added.

---

## Implications and next steps

### What Phase 6a establishes

1. **The tool framework works** — flexible hypothesis testing is
   possible; the tool reports diagnostic metrics across magic-A
   alignment, binding curve, and valley of stability.
2. **The valley of stability requires Coulomb**.  Without it,
   R64-Ma predicts proton-rich heavy nuclei that don't match
   observation.  With it (even imperfectly), the right direction
   emerges.
3. **Shell-closure bonuses are subleading** to bulk binding.  They
   refine the curve but don't shift its overall shape.
4. **The Fe peak still isn't produced** under any baseline
   hypothesis — surface (or equivalent) is missing.

### What Phase 6a does NOT establish

- The shell sequence is "right" — we used mass-ordering, but the
  user's intuition is that shells reflect spatial-packing, not mass.
- (1, ±1) is or isn't shear-ruled-out — the user hinted it might
  be excluded; we kept it for now.
- The TRUE structural origin of magic numbers in MaSt — we don't
  yet have a derivation of why specific cardinalities (1, 3, 6, 4,
  11, 16, 22) emerge.

### Recommended Phase 6b experiments

Now that the framework exists, several refinements are possible:

1. **Refit Point B → Point C with explicit Coulomb** in the slot
   tool's mass evaluation, then re-run all hypotheses.
2. **Test (1, ±1) exclusion** per user hint — see if removing it
   shifts the binding curve or valley.
3. **Test SOC nuclear-shell sequence** as a user-provided slot
   ordering instead of mass-ordering.  See if the explicit SOC
   ordering gives different binding-curve fitness.
4. **Add surface term** (plugged BW form) and see if Fe peak
   emerges with H2 + surface.
5. **Sweep shell-closure bonus values** to find the magnitudes
   that maximize binding-curve fit (essentially a fit of the BW
   parameters within R64's framework).

The framework supports all of these as straightforward
configuration changes.

---

## Status

**Phase 6a complete.  Track 6 PAUSED.**

After review with the user (referencing
[primers/nuclear-scaling.md](../../primers/nuclear-scaling.md)
for the standard-physics view of nuclear shell structure):

Track 6's tool is **structurally a re-derivation of SM nuclear
shell physics with MaSt labels** — not novel.  Magic numbers,
SOC shell structure, and the Fe peak's smooth-curve mechanism
are well understood in standard physics.  R64 doesn't need to
re-derive them.

**What Track 6's tool can do** (saved for potential later use):
- Test arbitrary slot configurations (orderings, capacities) for
  cumulative magic-A alignment.
- Compute predicted nuclear binding curves under R64-Ma + optional
  Coulomb + optional shell-closure bonuses.
- Compute predicted valley of stability (Z/A vs A) at any
  configuration.

**When to come back to it**: if downstream MaSt work produces
specific shell-structure predictions that need to be tested
against observed magic numbers, the framework is ready.  Until
then, Track 6 stays paused.

The natural successor work — what's NOVEL for MaSt — is to
derive the strong force itself (its strength and r-dependence)
from MaSt's geometric structure.  This is taken up in Track 7.
