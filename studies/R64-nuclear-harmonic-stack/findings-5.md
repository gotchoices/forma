# R64 Track 5 — Two-line nuclear binding model: Ma harmonic stack + S-Coulomb

Track 5 tests the user's two-line hypothesis for the Fe binding-curve
peak: that nuclear binding emerges from R64's Ma harmonic stack (Line
1, strong, internal) competing with Coulomb cost in S (Line 2, EM,
emergent from Ma charge geometry).  Embraces Coulomb as a real S-
energy without violating the "S-forces are Ma geometry" premise —
the geometric reality of charge IS in Ma; only the spatial-separation
*energy* is measured in S.

**Result: the two-line model is insufficient.  A third line (surface-
like, Ma-internal or Ma-boundary) is needed to produce the Fe peak.**

Without surface, R64-Ma + Coulomb gives a binding curve that **descends
monotonically** with A — the deuteron outlier has the highest predicted
B/A, and the curve falls from there.  No peak emerges.  The structural
issue is that R64-Ma already gives roughly constant per-nucleon binding
(~8.6 MeV/A), and adding Coulomb just subtracts a growing penalty —
yielding a falling curve, not a peaked one.

The peak in nature requires:
- A **rising** light-A side (surface deficit fading with A^(−1/3))
- A **falling** heavy-A side (Coulomb cost growing with A^(2/3))
- **Both** ingredients, crossing near Fe.

R64-Ma + Coulomb has only the second; the first is missing.

Scripts:
[`scripts/track5_phase5a_coulomb_added.py`](scripts/track5_phase5a_coulomb_added.py) ·
[`scripts/track5_phase5b_joint_refit.py`](scripts/track5_phase5b_joint_refit.py)
Outputs:
[`outputs/track5_phase5a_coulomb_added.csv`](outputs/track5_phase5a_coulomb_added.csv) ·
[`outputs/track5_phase5b_joint_refit.csv`](outputs/track5_phase5b_joint_refit.csv) ·
[`outputs/track5_phase5b_pointC_binding.csv`](outputs/track5_phase5b_pointC_binding.csv) ·
[`outputs/track5_phase5a_binding_curve.png`](outputs/track5_phase5a_binding_curve.png) ·
[`outputs/track5_phase5b_joint_refit.png`](outputs/track5_phase5b_joint_refit.png)

---

## Phase 5a — Adding Coulomb to fixed Point B (double-counting)

Test: keep Point B parameters fixed (ε_p=0.2052, s_p=0.0250,
K_p=63.629) and add explicit Bethe-Weizsäcker Coulomb energy
`a_C·Z(Z−1)/A^(1/3)` with `a_C = 0.71 MeV` to R64-Ma's prediction.

### F5a.1. Adding Coulomb at fixed Point B over-corrects strongly

| Nucleus | B_obs | B_R64-Ma | E_Coul | B_R64+C | ratio (R64+C / obs) |
|:---|:-:|:-:|:-:|:-:|:-:|
| ²H | 2.22 | 17.32 | 0 | 17.32 | 7.78 (anchor-hit) |
| ⁴He | 28.30 | 34.65 | 0.89 | 33.74 | 1.19 |
| ⁵⁶Fe | 492.26 | 482.65 | 120.63 | 361.71 | **0.735** |
| ²⁰⁸Pb | 1636.43 | 1720.77 | 795.92 | 923.68 | **0.564** |
| ²³⁸U | 1801.69 | 1955.00 | 959.17 | 994.50 | **0.552** |

Heavy nuclei ratio drops from 1.05 (Phase 3e Point B without Coulomb)
to 0.56 (with Coulomb).  Adding Coulomb has *over-subtracted* by
roughly the same amount Point B was over-fitting.

**Diagnosis**: Point B's chain-fit was implicitly capturing some of
the observed binding *that already includes Coulomb's effect* — the
fit minimized residuals against raw observed binding, so Coulomb's
cost was implicitly absorbed into Point B's parameter values.
Adding Coulomb back on top of Point B double-counts.

### F5a.2. The Fe peak does not emerge under Phase 5a's setup

Predicted B/A peak under R64-Ma + Coulomb at Point B: ²H at
A=2 with B/A = 8.66.  The curve descends monotonically from there,
just like the no-Coulomb prediction would, but with steeper decline
because Coulomb keeps subtracting more as A grows.

No peak shape emerges.

---

## Phase 5b — Joint refit of (ε_p, s_p) with explicit Coulomb

The honest test: re-fit (ε_p, s_p) to the chain *with* Coulomb
explicitly added.  This avoids the double-counting from 5a and finds
the Ma-only working point that, when combined with Coulomb, best
matches observation.

### F5b.1. Joint refit lands at Point C, structurally similar to Point B

Best constrained fit (Δ(m_n − m_p) within 5% of observed +1.293 MeV):

- **Point C: `(ε_p, s_p, K_p) = (0.2300, +0.0200, 71.152)`**
- RMS mass error: 0.226% (vs Point B's 0.182% without Coulomb)
- Slightly higher RMS — Coulomb's addition trades some chain-fit
  precision for explicit physical correctness.

The shift is modest: ε_p drops from 0.205 to 0.230, s_p reduced from
0.025 to 0.020, K_p increases from 63.6 to 71.2.  Point C and Point
B are in the same neighborhood structurally.

### F5b.2. Predicted binding at Point C still misses the Fe peak

Binding ratios (predicted/observed) at Point C under R64-Ma + Coulomb:

| Nucleus | B_obs | B_pred | ratio |
|:---|:-:|:-:|:-:|
| ²H | 2.22 | 21.69 | **9.75** (extreme outlier) |
| ⁴He | 28.30 | 42.49 | **1.50** (over) |
| ¹²C | 92.16 | 120.85 | **1.31** (over) |
| ¹⁶O | 127.62 | 157.75 | **1.24** (over) |
| ⁴⁰Ca | 342.05 | 354.94 | 1.04 (close) |
| **⁵⁶Fe** | 492.26 | 483.59 | **0.98** (close) |
| ⁹⁰Zr | 783.89 | 716.77 | 0.91 (under) |
| ¹²⁰Sn | 1020.54 | 912.32 | **0.89** (under) |
| ²⁰⁸Pb | 1636.43 | 1358.16 | **0.83** (under) |
| ²³⁸U | 1801.69 | 1488.10 | **0.83** (under) |

Pattern is informative:
- **Light nuclei over-bind** (⁴He at 50%, ¹²C at 31%)
- **Mid-chain matches well** (⁴⁰Ca through ⁵⁶Fe within 5%)
- **Heavy nuclei under-bind** (Pb, U at 17%)

R64-Ma + Coulomb produces a curve that is **too high at light A**,
**right around mid-chain**, and **too low at heavy A**.  The shape
is **reverse-Fe-peak**: descending throughout, with no rise on the
light side.

Predicted B/A peak: ²H at A=2 with B/A = 10.85.  Observed peak: ⁵⁶Fe
at A=56 with B/A = 8.79.

### F5b.3. Why the two-line model fails: missing surface contribution

In Bethe-Weizsäcker, the Fe peak's structure has three contributions
that vary with A (volume is constant per A, no shape contribution):

| BW term | Form | Per-nucleon | Sign on B/A |
|:---|:---|:---:|:---:|
| Volume | +a_V·A | constant | — |
| Surface | −a_S·A^(2/3) | ∝ −1/A^(1/3) | rises with A (less negative) |
| Coulomb | −a_C·Z(Z−1)/A^(1/3) | ∝ −A^(2/3)/4 (Z≈A/2) | falls with A |
| Asymmetry | −a_A·(N−Z)²/A | varies with N/Z | small |

The Fe peak emerges because **surface (rising) and Coulomb (falling)
have opposite sign-of-derivative-with-A**.  They cross near Fe.

R64-Ma + Coulomb captures volume + Coulomb + a partial asymmetry-like
term (R64's `(n_pr − 3sA)²` is asymmetry-like).  But it has **no
surface term** — no per-nucleon binding cost that fades as A grows.

Without surface, the predicted B/A is:
- High at light A (because nothing penalizes the boundary)
- Decreasing throughout (only Coulomb subtracts, monotonically)

This is exactly what Phase 5b shows.

### F5b.4. What R64 currently DOES capture

R64-Ma + Coulomb does capture:
- **Volume**: ~8.6 MeV/A baseline (the harmonic-stack rate at Point B/C)
- **Coulomb**: explicitly added with correct Z(Z−1)/A^(1/3) form
- **Asymmetry-like**: R64's `(n_pr − 3sA)²` term penalizes deviation
  from the (slightly proton-rich) optimum at Point C

What it doesn't capture:
- **Surface**: the per-nucleon binding deficit that fades as A grows.

### F5b.5. What Track 5 establishes

1. **Coulomb is structurally compatible with R64's framework**.
   Adding it as an S-emergent term with standard `a_C` form requires
   only modest parameter adjustment (Point B → Point C).
2. **The two-line (Ma + Coulomb) model is insufficient for the Fe
   peak**.  A third line (surface or equivalent A^(2/3)-decreasing
   contribution) is required.
3. **Surface in MaSt**: the natural Ma analog is **boundary effects
   on the harmonic stack** — nucleons at the spatial edge of the
   stack have fewer harmonic-stack neighbors, contributing less
   binding.  This is plausibly Ma-internal but isn't yet in R64's
   formula.

---

## Implications and next moves

The user's two-line hypothesis was structurally correct in spirit —
nuclear binding has multiple opposing trends — but **needs three
lines, not two**, to produce the Fe peak.  The third line (surface)
is missing from R64.

The natural follow-up: identify the Ma analog of surface.  Candidates:

1. **Spatial extent of the harmonic stack in S**.  R64 puts Z+N
   strands on the p-sheet, but those strands are also localized in
   the 4D spatial slice.  Boundary nucleons have effective binding
   reduced by a factor proportional to surface-area/volume = A^(−1/3).
   This is the most natural Ma-side mechanism.
2. **Non-additive correction at the harmonic-stack level**.  A
   refinement of the additive winding rule that introduces an
   A^(2/3) cost.  Less principled but computationally testable.
3. **Cross-sheet coupling**.  Parts of the e-sheet or ν-sheet
   structure might contribute a surface-like term.  Speculative
   without further development.

Before committing to any of (1)–(3), it's worth noting an
alternative reading: **maybe surface is also S-emergent**, like
Coulomb.  In SM, surface is the cost of nucleons being at the
boundary of the spatial nuclear droplet — definitely an S-coordinate
phenomenon.  If we accept Coulomb as S-emergent (Track 5's premise),
we should consider whether surface is too.  In which case the model
becomes "R64-Ma + S-Coulomb + S-surface" — three contributions, two
of them S-emergent, one Ma-internal.

This is consistent with the user's "embrace S-coordinate" framing
in Track 5.  The next phase would test this expanded model.

---

---

## Phase 5c — Three-line model with plugged BW surface

Tested user's Option 3 (hybrid): plug in standard BW surface
`a_S·A^(2/3)` with `a_S = 18.34 MeV` alongside Coulomb, re-fit
`(ε_p, s_p)` jointly, and check if the Fe peak emerges.

### F5c.1. Three-line model still fails to produce the Fe peak

Joint refit lands at **Point D = (ε_p, s_p, K_p) = (0.06, +0.30, 18.4)**
with RMS mass error 0.393% — *worse* than Track 3 Point B's 0.182%
(no Coulomb, no surface).  The optimizer was forced to extreme
parameter values to compensate for added terms.

Predicted binding at Point D:

| Nucleus | B_obs | B_pred | ratio |
|:---|:-:|:-:|:-:|
| ²H | 2.22 | 9.01 | 4.05 (over) |
| ⁴He | 28.30 | 29.13 | 1.03 (close, lucky) |
| ¹²C | 92.16 | 123.29 | 1.34 (over) |
| ⁴⁰Ca | 342.05 | 469.01 | **1.37** (over) |
| ⁵⁶Fe | 492.26 | 678.03 | **1.38** (over) |
| ¹²⁰Sn | 1020.54 | 1485.61 | **1.46** (over) |
| ²⁰⁸Pb | 1636.43 | 2517.25 | **1.54** (over) |
| ²³⁸U | 1801.69 | 2862.98 | **1.59** (over) |

Predicted B/A peak: **¹³⁰Te at A=130** with B/A = 12.55 MeV.
Observed: ⁵⁶Fe at A=56 with B/A = 8.79.  **Peak misplaced by 74
mass units.**

The three-line model with plugged BW values gives:
- *Over-binding everywhere* in the body of the chart (37–60% over)
- Peak at wrong A (130 vs 56)
- Worse RMS than R64-Ma alone

### F5c.2. Why the plugged hybrid fails: R64-Ma already implicitly absorbs surface and asymmetry effects

The diagnosis is structural.  R64's flat-formula mass

<!-- m² = K_p² · μ²(3A, 2(2Z-A)) -->
$$
m^2_\text{R64-Ma}(Z, A) \;=\; K_p^2\,\mu^2\bigl(3A,\; 2(2Z-A)\bigr)
$$

has TWO terms inside the square root:
- `(3A/ε)²` — A²-scaling (volume-like contribution)
- `(2(2Z−A) − 3sA)²` — Z-A asymmetry (asymmetry-like contribution)

Through the chain-fit at Point B, the optimizer found a balance
where these two terms (combined via the square root) **implicitly
match observed binding** — including effects that BW separately
attributes to Coulomb, surface, and asymmetry.  R64-Ma at Point B
isn't just "volume term"; it's an **integrated mass formula** that
already absorbs some of what BW splits across multiple terms.

Adding explicit BW Coulomb and surface on top **double-counts**:
- Some of what Point B was fitting was already including the
  Coulomb and surface effects from observed data.
- The "double-counting" forces the optimizer to other parameter
  regions where the explicit terms don't conflict — but those
  regions don't fit the observed data well.

The implication: **the two-line and three-line hybrid models are not
clean tests of R64's structure**, because R64-Ma's formula is not
cleanly factorable into "volume-only".

### F5c.3. What this tells us about R64's structure

R64-Ma's flat-formula mass is **a holistic mass formula**, not a
decomposition into independent BW terms.  The good chain-fit at
Point B (RMS 0.18%) is evidence that R64 captures the right *total*
nuclear binding shape — but it doesn't separate cleanly into BW
components, so we can't simply add BW corrections to it.

Two interpretations:

**Interpretation A — R64 captures the right total**.  The chain-fit
Point B already gives observed binding within ~5% across the body
of the chart.  This means R64's mass formula, taken as a *complete*
description (including all "BW-equivalent" contributions implicitly),
is correctly capturing the strong-force binding shape.  The Fe peak
isn't there because the formula's `μ²` form gives roughly constant
B/A, not a peaked shape.  **The peak is what R64 doesn't capture.**

**Interpretation B — R64 captures a coincidental fit**.  The
chain-fit Point B happens to match observed binding via a
fortunate parameter combination, but doesn't structurally
correspond to the underlying physics.  Adding BW corrections
breaks the fit because R64's formula isn't physically aligned
with the BW decomposition.

Both interpretations are honestly available.  Without deeper
structural understanding (mode stacking, quantum number decoding),
we can't distinguish them.

### F5c.4. The Fe peak shape requires structural Ma physics not in R64

If we want R64 to produce the Fe peak from first principles, we'd
need at least one of:

- A non-additive composition rule that introduces A-dependent
  curvature in `m_Ma(Z, A)`.
- Explicit cross-sheet content for nuclei (rejected by user
  reasoning that nuclei don't need electron shells to live).
- A spatial-distribution model in S that gives surface effects
  natively.
- Quantum-number-aware composition (mode stacking with shell
  closures).

None of these is in the current R64 framework.  Adding any of
them requires structural commitments we don't have evidence for.

---

## Track 5 verdict and recommendation

**Track 5 fails to produce the Fe peak under any of the three
phases attempted**:

- Phase 5a: adding Coulomb at fixed Point B over-corrects
  (double-counts).
- Phase 5b: joint refit Point C with explicit Coulomb shifts the
  problem but doesn't produce the peak.
- Phase 5c: adding plugged BW surface alongside makes things
  *worse* — over-binds everywhere, peak misplaced.

The structural lesson is **R64-Ma is a holistic formula that
implicitly absorbs BW-equivalent corrections at the chain-fit
parameter point**.  Decomposing it into BW components and adding
explicit Coulomb/surface terms breaks the implicit balance.

This means the user's intuition — that the Fe peak comes from
two opposing curves crossing — is structurally correct, but R64's
flat-formula structure doesn't cleanly decompose into those curves.

### Recommendation: pause Track 5; pursue user's Option 2 (mode stacking + shell decoding)

R64-Ma's mass formula needs deeper structural understanding before
the Fe peak can be derived.  The natural next move is the user's
Option 2 from the prior conversation: **decode mode stacking via
quantum numbers (n, l, m_l, m_s) on the e-sheet first** (where
atomic shells are well-quantified), then apply the same framework
to the p-sheet for nuclear shells.  At that point:

- We'll understand what "harmonic stacking" really means
  structurally.
- The Fe peak will likely emerge naturally as a consequence of
  shell-closure structure, not from an additive BW-style
  decomposition.
- R64's current chain-fit will be reinterpreted in the deeper
  framework.

Track 5 closes without producing the Fe peak.  The Track 5 work
is informative as a **falsification of the simple linear-decomposition
hypothesis**: nuclear binding is not cleanly Ma-volume + S-Coulomb +
S-surface.  It's deeper.

The Track 5 outputs (Point B, Point C, Point D candidate working
points) remain on file but none is yet a hard pin.  Q134 should be
updated to note that Track 5 didn't resolve the Fe peak, and the
working theory continues with Track 1's Point A and Track 3's
Point B as candidate data points pending deeper structural
understanding.

---

## Status

**Track 5 closes.  Three-phase audit (5a, 5b, 5c) shows the simple
two- and three-line decompositions don't produce the Fe peak when
combined with R64-Ma.**

The user's Option 2 (mode stacking and shell decoding) is now the
recommended next direction.  Pool item **b** (quantum-number
decoding) becomes the natural next track.
