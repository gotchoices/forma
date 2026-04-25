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

## Status

**Phase 5a, 5b complete.  Two-line model insufficient.**

Track 5's contribution to R64:
- Identified Point C `(ε_p, s_p) = (0.230, +0.020)` as a refined
  working point that explicitly incorporates Coulomb.
- Established that R64-Ma alone cannot produce the Fe peak.
- Documented the missing surface-like contribution.

The natural next move is **Phase 5c — surface mechanism diagnosis**,
testing the hypothesis that adding a surface term (Ma-side or
S-emergent) to R64-Ma + Coulomb produces the Fe peak.  This is a
straightforward 3-line model audit.

Track 5 doesn't close yet — Phase 5c is still pending.  But the
two-line hypothesis is decisively shown to be incomplete.
