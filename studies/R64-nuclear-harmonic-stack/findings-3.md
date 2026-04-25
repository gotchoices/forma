# R64 Track 3 — Nuclear progression audit, H to U

Track 3 tests R64's harmonic-stack model against the observed nuclear
mass and binding curve across 84 representative stable isotopes from
¹H to ²³⁸U.

**Result: clean structural failure on two independent observables.**

The harmonic-stack with strict additive-winding composition reproduces
the deuteron exactly (it's the anchor) but fails at heavier nuclei in
two unmistakable ways:

1. **Binding magnitude is ~7× too small.**  Observed binding peaks at
   ⁵⁶Fe at 8.79 MeV/A; R64 predicts a near-constant 1.1 MeV/A across
   the entire chain.  The ratio of predicted to observed binding stays
   between 0.13–0.16 from ⁴He through ²⁰⁸Pb.
2. **Valley of stability is in the WRONG DIRECTION.**  Observed nuclei
   have Z/A decreasing from 0.5 (light) to 0.39 (heavy) — they're
   neutron-rich, increasingly so.  R64 predicts Z/A = 0.6454 constant
   across the chain — proton-rich, opposite to nature.

The user's anticipated "slight non-linearity between protons and
neutrons" is now characterized: it is **large**, **structured**, and
**of the opposite sign** from R64's flat-formula additive prediction.
The harmonic-stack rule needs major refinement (or replacement) to
match observation, not minor tuning.

Script:
[`scripts/track3_phase3a_nuclear_progression.py`](scripts/track3_phase3a_nuclear_progression.py)
Outputs:
[`outputs/track3_phase3a_nuclei.csv`](outputs/track3_phase3a_nuclei.csv) ·
[`outputs/track3_phase3a_binding_curve.png`](outputs/track3_phase3a_binding_curve.png) ·
[`outputs/track3_phase3b_valley_of_stability.csv`](outputs/track3_phase3b_valley_of_stability.csv) ·
[`outputs/track3_phase3b_valley_of_stability.png`](outputs/track3_phase3b_valley_of_stability.png)

---

## Phase 3a — Mass and binding curve, 84 nuclei

### Method

Each stable nucleus (Z, A) is assigned the additive-winding tuple

<!-- (n_pt, n_pr) = (3·A, 2·(2Z − A)) -->
$$
(n_{pt}, n_{pr}) \;=\; \bigl(3 A,\; 2(2Z - A)\bigr)
$$

derived from `Z` protons (each `(3, +2)`) plus `A−Z` neutrons (each
`(3, −2)`) under flavor-aware composition.  Mass predicted via flat
formula at the magic point `(ε_p = 0.07309, s_p = 0.19387, K_p =
22.847)`.  Predicted binding `B_pred = Z·m_p + (A−Z)·m_n − m_pred`
compared to observed binding from AME2020 atomic masses.

### F3a.1. Predicted binding magnitude is ~7× too small across the chain

| Nucleus | B_observed (MeV) | B_R64 (MeV) | ratio (pred/obs) |
|:---|:-:|:-:|:-:|
| ²H | 2.224 | 2.225 | 1.000 (anchor) |
| ⁴He | 28.30 | 4.45 | **0.157** |
| ¹²C | 92.16 | 13.18 | 0.143 |
| ¹⁶O | 127.62 | 17.78 | 0.139 |
| ⁴⁰Ca | 342.05 | 44.16 | 0.129 |
| ⁵⁶Fe | 492.26 | 61.97 | **0.126** |
| ⁹⁰Zr | 783.90 | 101.5 | 0.130 |
| ¹²⁰Sn | 1020.55 | 132.4 | 0.130 |
| ²⁰⁸Pb | 1636.43 | 220.97 | **0.135** |
| ²³⁸U | 1801.69 | 256.2 | 0.142 |

The ratio stays remarkably constant at 0.13–0.16 across the entire
stable-nucleus chain.  Translated to **predicted binding per
nucleon**:

- Observed B/A peaks at ~8.8 MeV/A around ⁵⁶Fe.
- R64 predicts ~1.1 MeV/A roughly constant across A.

The R64 model produces a **flat binding curve at ~1 MeV/A** —
correct order of magnitude only at the deuteron (where it's
anchored).  It does NOT capture the rise from ²H through ⁵⁶Fe
that defines the strong-force binding peak.

### F3a.2. Mass predictions are within ~1% but binding error is ~85%

| Nucleus | Δm/m | Mass error |
|:---|:-:|:-:|
| ²H | 0.000% | anchor |
| ⁴He | +0.005% | +0.18 MeV |
| ⁵⁶Fe | +0.022% | +11.5 MeV |
| ²⁰⁸Pb | +0.066% | +127.7 MeV |
| ²³⁸U | +0.073% | +163 MeV |

Max |Δm/m| is 0.83% at ²³⁸U; mean is 0.73%.  By itself, this looks
small.  But because nuclear binding is only ~1% of the nuclear mass,
**a 0.7% mass error is an 80%+ binding error**.  The mass formula
must agree with observation to better than ~0.05% to capture
binding correctly — and R64's predictions exceed that gap by a
factor of 10.

### F3a.3. The deuteron's exact match is the only good fit

Phase 1b/1c established the magic point by solving for B(²H) =
2.224 MeV exactly.  This is the **unique** binding-anchor
coincidence — the deuteron is fit by construction, not predicted.
Every other nucleus is a prediction, and all of them under-bind
by 7–8×.

If we re-cast Phase 3a as "what does the model predict given
only the anchor on m_p, m_n, and observed proton/neutron mass
split," the answer is: a binding curve at 1.1 MeV/A roughly
constant — which fits ²H by anchor and fails everywhere else.

---

## Phase 3b — Valley of stability

### Method

For each A, find Z minimizing predicted nuclear mass
`m(Z, A) = K_p · √((3A/ε_p)² + (2(2Z−A) − 3·s_p·A)²)`.

Closed-form: `Z_optimal/A = (2 + 3·s_p)/4 = 0.6454` — independent
of A.  The model predicts a **constant** Z/A ratio across the
entire chart.

### F3b.1. R64 predicts proton-rich nuclei; nature has neutron-rich

| Nucleus | Z observed | Z predicted | ΔZ |
|:---|:-:|:-:|:-:|
| ⁴He | 2 | 2.58 | +0.6 |
| ¹⁶O | 8 | 10.33 | +2.3 |
| ⁴⁰Ca | 20 | 25.82 | +5.8 |
| ⁵⁶Fe | 26 | **36.14** | **+10.1** |
| ¹²⁰Sn | 50 | 77.45 | +27.4 |
| ²⁰⁸Pb | 82 | **134.24** | **+52.2** |
| ²³⁸U | 92 | 153.61 | +61.6 |

The R64 prediction misplaces the valley of stability by 10 protons
at ⁵⁶Fe and 52 protons at ²⁰⁸Pb.  The model does not host nature's
neutron-rich heavy nuclei at all — it would predict them as
unstable proton-rich states.

### F3b.2. The Z/A ratio: opposite slope from observation

Observed Z/A (from the data):
- A ≈ 4: Z/A = 0.50
- A ≈ 56: Z/A = 0.46
- A ≈ 120: Z/A = 0.42
- A ≈ 208: Z/A = 0.39
- A ≈ 238: Z/A = 0.39

R64 prediction: Z/A = 0.6454 for ALL A.

The observed slope is `dZ/dA ≈ −5×10⁻⁴` (decreasing with A); R64
predicts zero slope at the wrong intercept.  Both the slope and
the intercept are wrong.

### F3b.3. Why: the shear's sign produces this failure

Algebraic origin.  At the mass minimum for fixed A:

<!-- 2·(2Z − A) = 3·s_p·A  ⇒  Z/A = (2 + 3·s_p)/4 -->
$$
2 \cdot (2Z - A) \;=\; 3 \cdot s_p \cdot A
\quad\Longrightarrow\quad
\frac{Z}{A} \;=\; \frac{2 + 3 \cdot s_p}{4}.
$$

With `s_p > 0` (required by the proton/neutron mass split — see
Track 1), Z/A > 0.5.  With `s_p < 0`, Z/A < 0.5 — but then m_n
< m_p, contradicting observation.

**The two observables are structurally tied to opposite signs of
s_p.**  No choice of (ε_p, s_p) can satisfy both simultaneously
under additive winding alone.  The harmonic-stack rule with strict
additivity is **logically incompatible** with the SM's nuclear
chart at this level.

---

## Synthesis: what Track 3 reveals about R64

### F3.1. The deuteron success was anchor-driven, not predictive

Track 1's exact match on B(²H) = 2.224 MeV looked like a 3-observable
landing at 2 parameters.  Track 3 reveals it was actually 3
observables landing at 3 parameters (ε_p, s_p, K_p), with the
deuteron specifically anchoring the third.  Once we pass beyond the
anchored values, the model does not predict heavier nuclei
correctly.

### F3.2. The harmonic-stack rule is missing major physics

Compared to observation, R64's flat-formula additive prediction is
missing two contributions of roughly equal severity:

- **A binding-magnitude factor of ~7×** — predicted B/A is ~1
  MeV/A; observed peaks at ~9 MeV/A.  Even subtracting Coulomb
  (which the SM treats as ~0.7·Z²/A^(1/3) ≈ 0.5–4 MeV/A through the
  chain), R64 still under-binds by ~5–6×.
- **An N/Z asymmetry direction** — observed neutron-rich; R64
  predicts proton-rich.  The direction is wrong, not just the
  magnitude.

These are not subtle corrections.  R64 captures only the
deuteron, and only because it's the anchor.

### F3.3. The "non-linearity" is not slight

The user's anticipated "slight non-linearity between protons and
neutrons" turns out to be a major structural mismatch:

- Observed nuclear binding has a peaked rise-and-fall shape
  (Bethe-Weizsäcker volume + surface + Coulomb + asymmetry).
- R64 prediction is essentially flat at 1 MeV/A.
- The N/Z slope of observation is reversed in R64.

The "slight" qualifier is incorrect — observed nuclear physics
deviates from R64's additive prediction by factors of 7+ in
magnitude and reverses sign in N/Z direction.

### F3.4. What this means for the premise

The user's premise — "all forces in S are geometric realities in
Ma" — is not falsified by R64 Track 3, but it IS narrowed:

- The strong force is NOT in additive-winding harmonic-stack
  composition on the p-sheet at the magic point.  This is the
  fourth Ma-internal mechanism we've tested and the fourth to
  fail (after R63's cross-shear, non-additive tuples, high-n
  corrections, and Pauli phase coherence).
- The composition rule on the p-sheet must produce binding
  ~7× larger and N/Z direction reversed from the additive
  prediction.  No principled rule we've considered does this.

Two readings remain on the table:

**Reading A — the harmonic-stack picture is wrong.**  The proton
+ neutron + deuteron success at the magic point is a 3-observable,
3-parameter coincidence, not evidence for a deeper theory.  R64
closes negative; the strong force lives elsewhere (S-space
configuration energy, non-Abelian gauge structure, or framework
extension).

**Reading B — the picture is right but the composition rule needs
fundamental revision.**  Strict additive winding is too rigid.  A
non-trivial rule (multi-mode coherence, shell-closure structure,
non-Abelian effects, or a curvature-corrected metric *combined with*
flavor-aware primitives) might preserve the deuteron success and
recover the heavy-nucleus binding shape.

### F3.5. What can still be tested cheaply

Three cheap follow-up audits that would discriminate Reading A vs B:

1. **Subtract Coulomb from observed; compare residual shape.**
   The "Coulomb-subtracted" binding curve is what MaSt's
   non-electromagnetic mechanism would need to reproduce.  If the
   shape after Coulomb subtraction is substantially flatter
   (closer to R64's prediction), then Coulomb explains most of
   the gap and R64 is closer than it looks.  If the shape is
   still strongly peaked, R64's missing the strong force itself.
2. **Test alternative composition rules.**  Multi-mode coherence
   or non-additive winding.  A single principled refinement
   tested against ²H, ⁴He, ⁵⁶Fe, ²⁰⁸Pb simultaneously.  If one
   rule fits all four, R64 survives; if not, Reading A.
3. **Ask whether ε_p ≠ magic-point values give better heavy fits.**
   If a different (ε_p, s_p) gives the right binding curve at the
   cost of a wrong proton/neutron split, that signals the magic
   point is nuclear-binding-incompatible by construction.

I lean toward audit 1 (Coulomb subtraction) as the next phase —
it's structurally cheap (one analytical computation, no new fits),
and it tells us whether R64 is just missing electromagnetism or
missing the strong force itself.

---

## Status

**Phase 3a + 3b complete; Phase 3c pending decision.**

R64's foundational success on the proton/neutron/deuteron triad
(Track 1) does not extend to the heavy-nucleus chain (Track 3).
The harmonic-stack with strict additive winding is incompatible
with the observed binding curve and with the valley of stability
direction.

The next phase (3c) should isolate whether the gap is
"electromagnetism (S-side, expected)" or "strong force (Ma-side,
the actual question)" by Coulomb-subtracting observation and
comparing the residual shape to R64's prediction.
