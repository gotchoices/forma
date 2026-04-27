# R64 Track 13b — Point A unified-working-point validation, with QM gate

**Status: complete.  Verdict: BOTH Point A and Point B FAIL the
QM gate the same way.  Track 11's "strong force in metric" claim
is now formally walked back.**

This track addresses the review's Concern 1 directly: Phase 7d's
QM gate was never re-applied to Phase 11c's V(r).  Track 13b
applies it to both:

- (a) Phase 11c reproduction at Point B (control)
- (b) New computation at Point A under the metric (test)

Script:
[`scripts/track13b_point_a_with_qm_gate.py`](scripts/track13b_point_a_with_qm_gate.py)
Output:
[`outputs/track13b_point_a_qm_gate.png`](outputs/track13b_point_a_qm_gate.png)

---

## Method

1. At each working point, find the σ_pS_tube giving σ_eff_tube =
   −116 (Phase 7c calibration target) at the σ_pS_tube + H2
   signature edge.
2. Build V(r) for pn, pp, nn channels using the metric-derived
   σ_eff_tube, with R64 mass formula and Phase 7c kinematic
   prefactor `A = 4·(ℏc)²`.
3. Solve the radial Schrödinger equation (Phase 7d machinery):
   - Find bound-state spectrum for each channel
   - Compute scattering lengths a_t (pn triplet) and a_s (nn
     singlet analog)
4. Compare to observed: B(²H) = 2.224 MeV (1 bound state), nn
   and pp unbound, a_t = +5.42 fm, a_s = −23.7 fm.

---

## Results

### F13b.1.  Point B (Phase 11c reproduction) — FAIL

| Observable | Point B prediction | Observed | Status |
|---|---:|---:|:---:|
| pn bound states | **3** | 1 | ✗ |
| Ground-state binding above V(∞) | 12.6 MeV | 2.22 MeV | ✗ |
| Total binding from free-N threshold | **29.9 MeV** | 2.22 MeV | ✗ (13× too deep) |
| nn bound states | **3** | 0 | ✗ |
| pp bound states | **3** | 0 | ✗ |
| a_t (pn triplet) | +7.9 fm | +5.42 fm | ⚠ wrong magnitude |
| a_s (nn singlet) | +9.1 fm | −23.7 fm | ✗ wrong sign |

This reproduces (within numerical precision) Phase 7d's earlier
result on Phase 7c's V(r).  Phase 11c's V(r) is numerically
identical to Phase 7c's by construction; it inherits the same
failures.

### F13b.2.  Point A — also FAIL

| Observable | Point A prediction | Observed | Status |
|---|---:|---:|:---:|
| pn bound states | **3** | 1 | ✗ |
| Ground-state binding above V(∞) | 12.5 MeV | 2.22 MeV | ✗ |
| Total binding from free-N threshold | **14.6 MeV** | 2.22 MeV | ✗ (6.6× too deep) |
| nn bound states | **3** | 0 | ✗ |
| pp bound states | **3** | 0 | ✗ |
| a_t (pn triplet) | +8.9 fm | +5.42 fm | ⚠ wrong magnitude |
| a_s (nn singlet) | +9.1 fm | −23.7 fm | ✗ wrong sign |

Point A's only quantitative improvement is in the *total binding
from free-N threshold* (14.6 vs 29.9), which traces to Point A's
m_Ma(pn) = 1875.7 MeV being closer to (M_p + M_n) = 1877.8 MeV —
i.e. Point A's Ma-side asymptotic offset is smaller.  But the
*bound-state structure itself* is essentially identical to Point B:
same number of states (3), same energies above threshold (≈ −12.5,
−4.7, −2.2 MeV), same wrong-sign a_s.

### F13b.3.  Why both points fail similarly

The bound-state spectrum is determined by the V(r) trough shape,
which is set by:

- σ_eff_tube = −116 (signature-edge calibration; the same at both
  points by construction)
- Kinematic prefactor `A = 4·(ℏc)²` (Phase 7c convention;
  working-point-independent)
- Cross-term form `2·k_S·σ·n_pt·ℏc` (linear in σ and n_pt;
  working-point-independent)

The ε, s, K parameters affect the *m_Ma asymptote* but not the
shape of the V(r) well below it.  So both Point A and Point B
produce nearly identical V(r) trough geometry, leading to the
same bound-state count and similar energies.

Working-point shopping does not fix the QM failure.  The failure
is structural to the V(r) shape produced by σ_pS_tube + H2.

### F13b.4.  Why the metric V(r) supports too many bound states

The Phase 11c V(r) profile:

- Hard core at r ≲ 0.5 fm (V → +∞ as r → 0 from the kinematic
  4·(ℏc)²·k_S² term)
- Trough at r ≈ 1.1 fm with V_min ≈ −32 MeV
- Long polynomial tail V(r) ~ −1/r at large r (no exponential
  damping)

This is **not a Yukawa shape**.  Phase 7b documented this
explicitly: V(r) is polynomial in 1/r², 1/r — no exp(−mr)
factor.  A potential with this shape supports many bound states
because the long tail keeps the integrated attraction high.

A Yukawa with M_pion-equivalent range (~1.4 fm) and similar
trough depth supports exactly 1 weakly-bound pn state and no
bound nn/pp — matching nature.  The polynomial tail of our
metric-derived V(r) is the structural problem, not the depth or
trough location.

---

## Implications for the architecture

### What's now ruled out at the QM level

- Track 11's "strong force in metric" claim, in its 11c-style
  V(r) form.  Walked back.
- Pool item m (Yukawa propagator) being "unforced."  It is
  potentially needed; the metric-V(r) route fails the QM gate.
- "Working-point shopping" as a way to fix QM observables.
  Point A doesn't pass; no other point on the (ε_p, s_p) curves
  is likely to either, since the V(r) shape is working-point-
  independent.
- The premise that Point A unifies weak + strong at the
  observable level.  The G_F match still holds (independent of
  V(r)) but Point A doesn't deliver strong-force phenomenology
  on top of it.

### What's preserved

- **A1 charge attribution** `f = n_pt/6 + n_pr/4` (Phase 11a F11a.2):
  unchanged, pool item g closed.
- **H2 closed form** `b = −√α/k_p` (Phase 11d, no 2^(1/4)
  speculation): unchanged.
- **G_F = s_p · α² / m_p² match** (pool z step 1, 0.5% precision
  at Point A): independent of V(r) shape and QM gate; survives.
- **The metric-edge identification of σ_t = −116** (Phase 11c
  F11c.3): real connection, but its physical interpretation is
  more limited than the original phrasing — it relates Phase 7c's
  fitted σ_t to the metric Schur quantity, not "the strong force
  in the metric."

### Three paths forward

1. **Pool item m revival (Yukawa propagator).**  Build a
   propagator-mediated V(r) from a virtual mediator (pion-analog
   compound mode).  Yukawa shape would naturally give 1 bound
   pn state, no bound nn/pp.  Substantial new formalism but
   correctly shaped.
2. **Different kinematic prefactor or cross-term structure.**
   The `4·(ℏc)²·k_S²` and `σ·n_pt·k_S` form may not be the right
   way to embed metric couplings into V(r).  Investigate
   alternatives (e.g. exponential cutoff from compactification
   scale).
3. **Strong force as compound-mode binding rather than V(r)
   bound state.**  R29 found nuclei as Ma compound modes (n_5 =
   A, n_6 = 2A) directly.  Maybe the deuteron *is* the (6, 0)
   Ma compound mode at its m_Ma asymptote, not a V(r) bound
   state at all.  This would reframe what "strong force" means
   in MaSt: not a sustained continuous potential, but the
   energetics of compound-mode formation.

---

## Status

**Track 13b: complete.  Concern 1 from review.md confirmed.**

The metric architecture in its current form (σ_pS_tube + H2 +
edge methodology + Phase 7c-style V(r)) does not deliver
strong-force phenomenology at the QM level.  Working-point
shopping (Point B → Point A) doesn't help.

The findings that survive (A1 attribution, H2 closed form, G_F
structural match) are real and worth keeping, but the
architectural claim "metric formalism is complete for strong
force" is now formally walked back.

**Immediate consequences:**

- STATUS.md updated to reflect QM-gate failure at both points
- findings-11.md walked back per review (already done)
- Pool item m back on the active list (no longer marked obsolete)
- Pool item r (edge-methodology interpretation) becomes more
  important: was the edge methodology a regulator artifact all
  along?  Track 13b's results suggest yes.

**Recommended next pool items, in priority order:**

1. **m**.  Yukawa long-range extension (propagator-based) — was
   ruled obsolete; revive.
2. **Alternative**: revisit R29's compound-mode framework for
   nuclei.  If deuteron *is* a (6, 0) Ma mode at its m_Ma value,
   maybe the V(r) bound-state question is a category error.
3. **r**. Edge-methodology interpretation — Track 13b suggests
   the divergent σ_eff at signature edge is regulator artifact,
   not structure.  Symbolic analysis would confirm.
