# Q134: Nuclear structure as a harmonic stack on the p-sheet — R64's g-candidate working theory

**Status:** Open — working hypothesis under R64.  R64 Track 1 landed
positive on a deuteron-anchored magic point; R64 Track 3 demonstrated
that the deuteron anchor was premature and re-fitted to the body of
the nuclear chart, landing on a different candidate working point.
Captures the provisional theory and ground rules for proceeding.

**Note on terminology:** R63 and R64 are **parallel candidates** for
becoming model-G when promoted.  Each produces its own *g-candidate*
parameter set and rule set.  R63's g-candidate uses cross-sheet
neutron representation and falsified Ma-internal binding within
that representation; R64's g-candidate uses on-p-sheet neutron with
flavor-aware u/d primitives and is currently passing nuclear-chain
binding within ~5% across the body of the chart.  Whichever (if
either) demonstrates clear superiority across multiple criteria
becomes the basis for **model-G** when the project promotes a
candidate.

**Related:**
  [Q132](Q132-promotion-chain-principle.md) (Z₃ confinement / promotion-chain rule),
  [Q86](Q86-three-generations.md) (quark generations),
  [Q98](Q98-quark-generations-vs-lepton-generations.md) (quark-lepton generation parallels),
  [Q88](Q88-phase-dependent-nuclear-force.md) (nuclear force from MaSt geometry),
  [Q89](Q89-fusion-as-mode-transition.md) (fusion as Ma mode transition),
  [Q95](Q95-strong-force-as-internal-em.md) (strong force as internal EM),
  [R63](../studies/R63-proton-tuning/) (cross-sheet model — falsified for nuclear binding),
  [R64](../studies/R64-nuclear-harmonic-stack/) (this study, harmonic-stack model).

---

## 0. The premise

> All forces in spacetime (S) are geometric realities in the compact
> manifold (Ma).

R63 closed negatively on this premise for the strong force *under
the cross-sheet model*: six Ma-internal binding mechanisms were
falsified, plus the curved-donut geometry alternative.  R64 reframes
the question by changing the proton/neutron representation and
testing whether the strong force can live geometrically on the
p-sheet alone.

**Track 1 (Phase 1a–1c)** landed a positive on a foundational test:
a single `(ε_p, s_p)` point — labeled the "magic point" at
`(0.07309, 0.19387)` — reproduces three independent observables
(constituent up-quark mass, neutron-proton mass split, and deuteron
binding) within ~0.1% each.

**Track 3 (Phase 3a–3e)** revealed that the magic point was
deuteron-anchored and structurally non-representative.  At a
different candidate working point obtained by global least-squares
re-fit on the nuclear chain — `(ε_p, s_p) = (0.2052, +0.0250)` — the
harmonic-stack model fits the body of the nuclear chart (Ca through
Sn) within 1–2%, with the deuteron remaining as a visible outlier.

Two candidate working points are therefore on the table within R64,
and a Track 4 audit is needed before either is treated as a hard
pin.

---

## 1. The R64 g-candidate working theory

R64's g-candidate is the alternative to R63's g-candidate.  Its
core structural commitments are:

### 1.1 Two flavors as ring-direction primitives

The p-sheet hosts two flavor primitives, distinguished by ring
direction:

- **u quark** = `(n_pt, n_pr) = (1, +2)` on the p-sheet.
- **d quark** = `(n_pt, n_pr) = (1, −2)` on the p-sheet.

Their masses differ via the shear's interaction with the ring
direction:

<!-- m_u² − m_d² ∝ shear-coupling -->
$$
\mu^2(1, +2) = (1/\varepsilon_p)^2 + (2 - s_p)^2, \qquad
\mu^2(1, -2) = (1/\varepsilon_p)^2 + (2 + s_p)^2.
$$

The (n_pr → −n_pr) flip is the unique Z₃-compatible flavor operation
on the p-sheet (tube flip would break confinement; this was checked
in R63 close-out discussion).

### 1.2 Antimatter via full sign reversal

The four sign combinations on `(n_pt, n_pr) = (±1, ±2)` decompose
naturally:

| Geometric label | Quantum role | μ at chain-fit point | μ at magic point |
|:---|:---|:-:|:-:|
| (+1, +2) | u | 334.8 MeV | 315.3 MeV |
| (−1, −2) | ū | 334.8 MeV | 315.3 MeV |
| (+1, −2) | d | 336.0 MeV | 316.6 MeV |
| (−1, +2) | d̄ | 336.0 MeV | 316.6 MeV |

Antimatter is full reversal `(n_t, n_r) → (−n_t, −n_r)`; flavor is
ring reversal alone.

### 1.3 Baryons as Z₃-coherent triplets of u/d quarks

- **Proton (uud)** → additive winding sum on p-sheet: `(3, +2)`.
- **Neutron (udd)** → `(3, −2)`.
- **Anti-proton (ūūd̄)** → `(−3, −2)`.
- **Anti-neutron (ūd̄d̄)** → `(−3, +2)`.

R60 T16's Z₃ confinement (`n_pt ≡ 0 mod 3`) is preserved
automatically: every uud, udd, uds, ... combination has `n_pt = ±3`
or larger Z₃-divisible values.

### 1.4 Nuclei as harmonic stacks on the p-sheet

A nucleus with `Z` protons and `A − Z` neutrons has p-sheet windings
under additive composition:

<!-- (n_pt, n_pr) = (3A, 2·(2Z − A)) -->
$$
(n_{pt}, n_{pr})_{\text{nucleus}} \;=\; \bigl(3A,\; 2(2Z - A)\bigr).
$$

For ²H (A=2, Z=1): `(6, 0)`.  For ⁴He (A=4, Z=2): `(12, 0)`.  For
⁵⁶Fe (A=56, Z=26): `(168, −8)`.

**The neutron lives entirely on the p-sheet** in this picture.  The
cross-sheet `(1, 2, −1, −1, 3, 6)` from R63 Track 8 is what the
on-sheet neutron *degenerates to* during β decay; the e-sheet (1, 2)
and ν-sheet (−1, −1) are the emitted lepton pair, not constituents
of the bound neutron.

### 1.5 The shear is the proton/neutron asymmetry generator

Under flat formula `μ² = (n_t/ε)² + (n_r − s·n_t)²`, the proton
`(3, +2)` and neutron `(3, −2)` are mass-degenerate when `s = 0`.
The shear breaks this degeneracy, with magnitude

<!-- Δμ² = μ²(3, -2) − μ²(3, +2) = 24·s -->
$$
\mu^2(3, -2) - \mu^2(3, +2) \;=\; 24\,s_p.
$$

Solving for the observed mass ratio gives the viable curve `s_p(ε_p)`
along which proton/neutron mass split matches observation.

### 1.6 Two candidate working points (both PROVISIONAL)

R64 currently has two distinct candidate working points for `(ε_p,
s_p, K_p)`.  Neither is yet a hard pin — both are provisional until
broader validation passes.

**Point A — Magic point (Track 1, deuteron-anchored):**

- `ε_p = 0.07309, s_p = +0.19387, K_p = 22.847 MeV/μ`
- Reproduces m_u = 315.3 MeV, m_n − m_p = 1.293, B(²H) = 2.226
  simultaneously.
- α-pinning hypothesis tested and rejected (Phase 1c): ε_p ≠ 10·α
  exactly.
- **Heavy-nucleus binding under-predicts by ~7×** (Phase 3a).
- **Valley of stability strongly proton-rich** (Phase 3b).

**Point B — Chain-fit point (Track 3, body-of-chart-anchored):**

- `ε_p = 0.2052, s_p = +0.0250, K_p = 63.629 MeV/μ`
- m_u = 334.8 MeV, m_d = 336.0 MeV (latter near-exactly matches
  SM constituent value).
- m_n − m_p = +1.293 MeV (by construction).
- **Body of nuclear chart (Ca through Sn) fits within 1–2%**;
  ⁵⁶Fe within 2%, ¹²⁰Sn within 1%.
- Light end (⁴He, ¹²C) over-binds by 10–22%.
- Heavy end (Pb, U) over-binds by 5–9%.
- **Deuteron is an outlier**: predicted B(²H) = 17.3 vs observed
  2.22 MeV.
- Valley of stability: Z/A_optimum = 0.519 (still slightly proton-
  rich; observed trends 0.50 → 0.39 with A).

**Status of the two candidates:**

The chain-fit Point B is the better fit for the body of the nuclear
chart and is the current preferred candidate, BUT:

1. The deuteron's outlier status under Point B is unexplained
   (whereas Point A captures it exactly).
2. The hadron inventory (Λ, Σ, Ξ, K, π, η, etc.) has not been
   re-audited at Point B — Track 4 is the gate before treating
   Point B as a hard pin.
3. The valley-of-stability direction is still slightly off at
   Point B; whether this is Coulomb-explained (R64 missing EM)
   or structural is unresolved.
4. The Coulomb-interpretation puzzle: at Point B, R64's prediction
   sits closer to *raw* observed binding than to Coulomb-subtracted
   binding, suggesting R64's mass formula implicitly encodes
   something Coulomb-like.  Diagnostic of what physics R64
   captures.

**The lesson from Track 3**: pinning to a single observable
(deuteron in Track 1) gave a structurally non-representative
working point.  Don't pin Point B prematurely either — keep it
provisional through Track 4 validation.

---

## 2. Provisional ground rules for R64

### 2.1 Discipline

1. **The neutron lives on the p-sheet.**  Cross-sheet representations
   are degeneration products, not fundamental.
2. **Z₃ confinement (R60 T16) is retained as default.**  Re-evaluated
   only if a specific test exposes a structural conflict.
3. **Observable anchoring is allowed** for foundational masses
   (proton, neutron, deuteron, eventually ⁴He).  This is different
   from R63's "no observable-anchored sweeps" rule.
4. **Inventory preservation is the hard gate.**  The magic point
   must keep the 13-particle hadron inventory within 5% under
   u/d-aware composition.  If it fails, R64 fails.
5. **S-stability is hypothesized, not computed.**  Where the theory
   says "the neutron is stable in a nucleus, unstable in isolation,"
   that's a hypothesis pending S-stability tooling.
6. **Heavy-nucleus instability (Z = 137) is deferred.**  Focus on
   H → Fe range.
7. **Higher-generation quarks (s, c, b, t)** identified as separate
   primitive classes on the p-sheet.  Candidates: `(2, ±1)`,
   `(1, ±3)`, `(2, ±3)`, ... .  To be pinned by inventory and
   observed flavor masses.

### 2.2 Composition rules (provisional)

1. **Baryons compose by additive winding sum** of constituent quarks.
   Verified working for proton (3, +2), neutron (3, −2), and the
   deuteron (6, 0).
2. **Nuclei compose by extended additive winding**: nucleus (Z, A)
   has p-sheet content `(3A, 2(2Z − A))`.  At the chain-fit
   point (Point B), this rule reproduces the body of the nuclear
   chart within 1–2% (Phase 3e).  At the magic point (Point A),
   it under-predicts by 7×.
3. **Mesons compose as quark-antiquark pairs.**  Examples to test:
   π⁰ as uū or dd̄ or mixed; K⁺ as us̄; etc.  Not yet validated.
4. **The deuteron is an outlier.**  Under Point B's rule, B(²H)
   = 17 MeV vs observed 2.22 MeV.  Either a special structural
   feature of the 2-body system needs to be identified, or
   Point B is wrong (and Point A's deuteron-anchored picture
   is right after all).  This is the central tension under R64.

### 2.3 Charge attribution (provisional)

Q132 v2's compound-charge rule (ω-sum cancellation) currently does
not distinguish (1, +2) from (1, −2) at the rule level.  The
provisional R64 extension is:

- **u** (1, +2) carries charge **+2/3**.
- **d** (1, −2) carries charge **−1/3**.
- Compound charges sum: proton (uud) = +2/3 + +2/3 + (−1/3) = +1 ✓.
  Neutron (udd) = +2/3 + (−1/3) + (−1/3) = 0 ✓.

Whether this assignment can be derived from a refined Q132 v3
rule (e.g., the sign of n_pr at the primitive level mapping to the
fractional-charge sign) is an R62-style derivation target.

---

## 3. Open questions (for next tracks)

### 3.1 Inventory survival audit at the chain-fit point (Point B)

The 13 hadrons of R63 Tracks 5/6 (π, K, η, η′, Λ, Σ, Ξ, φ, …) need
to be tested at Point B's parameter set.  Each meson and hyperon
needs its u/d/s tuple re-derived under flavor-aware composition,
charge attribution under the provisional rule (§2.3), and mass
predictions compared to observation.  This is the **Track 4 hard
gate** — Point B becomes a candidate for promotion to model-G only
if the inventory survives within ~5% per particle.

Track 2 Phase 2a's strange-quark search was done at Point A and
gave structural problems (Σ⁺ off by 15%, K⁰ off by 17%).  Worth
re-running at Point B before treating those as final negatives.

### 3.2 The deuteron's outlier status

Under Point B, B(²H) = 17 MeV vs observed 2.22.  Two readings:

- **The 2-body system is special.**  In QCD, the deuteron is
  loosely bound by ~2 MeV — far below the per-nucleon binding of
  heavier nuclei.  The harmonic-stack rule may require a 2-body
  correction that doesn't apply to A ≥ 3.  Identifying this
  correction is a research target.
- **Point B is wrong.**  If no principled correction explains
  the deuteron under Point B, the deuteron-anchored Point A may
  be right after all — and the heavy-chain fit at Point B is a
  numerical accident.

### 3.3 The Coulomb-interpretation puzzle

At Point B, R64's prediction sits closer to *raw* observed binding
than to Coulomb-subtracted binding.  In standard nuclear physics,
the strong force should match the Coulomb-subtracted residual.
Possible readings:

- R64's mass formula implicitly encodes a Coulomb-like attraction
  through its harmonic-stack structure.
- The fit at Point B is coincidental in a way we haven't
  understood.

A clean diagnostic: predict the binding curve for several Z at
fixed A; the Z-dependence should match Coulomb's `Z(Z−1)/A^(1/3)`
shape if R64 captures Coulomb implicitly.

### 3.3 Z = 137 impedance limit

Deferred to a later track.  The qualitative argument (137 protons
in Ma exceeds 1 proton's worth of S-energy) is plausible but not
quantified.  S-stability tooling required.

### 3.4 Higher-generation quarks

Strange, charm, bottom, top quarks need primitive-class
identification.  Candidates: `(2, ±1)` (e.g., for s), `(1, ±3)`,
etc.  Audit of meson and hyperon inventory under R64's u/d
composition will indicate which class hosts s.

### 3.5 Electron-shell harmonic stack on the e-sheet

Optional R64 track or a separate study (R65).  Test whether
1s, 2s, 2p, 3s, 3p, 3d levels appear as harmonic modes on the
e-sheet at appropriate `(ε_e, s_e)`.  R63's e-sheet work was
done under cross-sheet inventory; the harmonic-stack picture
may shift the e-sheet's working point.

### 3.6 Q132 v2 charge-rule extension

The provisional charge attribution (§2.3) needs derivation from a
refined Q132 rule.  Likely candidate: the sign of the primitive's
n_pr maps to the fractional-charge sign at the +2/3 vs −1/3 level.

---

## 4. What this question replaces / extends

R64's g-candidate is an **alternative** to R63's g-candidate.  Both
are candidates for promotion to model-G, distinguished by how the
neutron is represented and where the strong force lives.

**R64 retains** without modification:
- **Q132 v2** as the rule set on the e-sheet and ν-sheet (R64
  doesn't change the lepton sector).
- **R60 T16** (Z₃ confinement) — the harmonic stack respects this
  by construction.
- **R62 derivation 4** (the closed-form mass formula on a flat
  2-torus).  R64 uses the same formula; only the working
  parameters and the proton/neutron representation change.

**R64 changes** relative to R63:
- **Neutron representation**: cross-sheet `(1, 2, −1, −1, 3, 6)`
  → on-sheet `(0, 0, 0, 0, 3, −2)`.
- **Quark inventory**: single primitive `(1, 2)` → two primitives
  `u = (1, +2), d = (1, −2)`.
- **Working `(ε_p, s_p, K_p)`**: R63 used `(0.55, 0.162, K_MODELF)`.
  R64 has two candidate points:
  - Point A (deuteron-anchored): `(0.07309, +0.19387, 22.847)`
  - Point B (chain-anchored, current preferred): `(0.2052, +0.0250,
    63.629)`
- **Charge rule** (provisional): added u/d sign attribution at the
  primitive level.
- **Composition rule for nuclei**: extended additive winding
  `(Z, A) → (3A, 2(2Z−A))`.

---

## 5. Status

**R64 Track 1 (positive at Point A).**  The deuteron-anchored magic
point reproduces three foundational observables (m_u, m_n−m_p,
B(²H)) within ~0.1%.

**R64 Track 2 Phase 2a (partial at Point A).**  Strange-quark search
at Point A located a primitive `(1, −20)` matching m_s = m_Ω/3 by
construction, but Σ over-predicts by 9–15% and K⁰ by 17%.
Inconclusive at Point A; not yet redone at Point B.

**R64 Track 3 (reframing).**  Heavy-element binding curve at
Point A under-predicts by ~7×.  Phase 3d's global re-fit located
Point B as a candidate that fits the body of the chart within
1–2%.  Deuteron is an outlier under Point B.

**Next gate — Track 4 inventory audit at Point B.**  The 13-particle
hadron inventory needs to be re-tested at Point B's parameters
under flavor-aware composition.  Inventory preservation within ~5%
is the gate before Point B is treated as a hard pin.

**Promotion to model-G is deferred.**  Both R63's g-candidate and
R64's g-candidate would need to demonstrate clear superiority
across multiple criteria (inventory accuracy, binding curve, charge
attribution, decay structure, heavy nuclei) before the project
promotes either to model-G.  R64's chain-fit is a promising
candidate but explicitly provisional pending Track 4.
