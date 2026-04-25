# Q134: Nuclear structure as a harmonic stack on the p-sheet — the h-candidate working theory

**Status:** Open — working hypothesis from R64 Track 1 (positive on
foundational test).  Captures the provisional theory and ground rules
for proceeding.

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

R64 Track 1 lands a positive on the foundational test: a single
`(ε_p, s_p)` point reproduces three independent observables —
constituent up-quark mass, neutron-proton mass split, and deuteron
binding — within ~0.1% each.  That positive justifies capturing
the working theory and provisional ground rules now, while open
questions are pursued in subsequent tracks.

---

## 1. The working theory (h-candidate)

The "h-candidate" is the candidate model successor to the g-candidate
that R63 was developing.  Its core structural commitments are:

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

| Geometric label | Quantum role | μ at magic point |
|:---|:---|:-:|
| (+1, +2) | u | 315.3 MeV |
| (−1, −2) | ū | 315.3 MeV |
| (+1, −2) | d | 316.6 MeV |
| (−1, +2) | d̄ | 316.6 MeV |

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

### 1.6 The "magic point"

R64 Track 1 located **`ε_p ≈ 0.073, s_p ≈ 0.194`** as the candidate
magic point where three observables match simultaneously:

- m_u = 315.3 MeV (SM constituent ~315)
- m_n − m_p = 1.293 MeV (observed, by construction)
- B(²H) = 2.226 MeV (observed 2.224)

K_p (mass scale) at this point: 22.86 MeV/μ-unit.

This point is structurally distinct from R63's working point
`(ε_p, s_p) = (0.55, 0.162)` — different geometry, different shear
magnitude, different K_p.  Whether this point also preserves the
hadron inventory (mesons, hyperons) is the next test.

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

### 2.2 Composition rules (provisional, may need refinement)

1. **Baryons compose by additive winding sum** of constituent quarks.
   Verified working for proton (3, +2), neutron (3, −2), and the
   deuteron (6, 0) at the magic point.
2. **Mesons compose as quark-antiquark pairs.**  Examples to test:
   π⁰ as uū or dd̄ or mixed; K⁺ as us̄; etc.
3. **Nuclei may NOT strictly follow additive winding** for A ≥ 3.
   ³He under-binds 2.6× and ⁴He under-binds 6.3× under naive
   additive composition.  This indicates a composition-rule
   refinement is needed for A ≥ 3 — currently an open question.

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

### 3.1 Inventory survival audit

At the magic point ε_p ≈ 0.073, do the 13 hadrons of Track 5/6
(proton, neutron, π, K, η, η′, Λ, Σ, Ξ, φ) still fit observed
masses within 5% under flavor-aware composition?  Each meson and
hyperon needs its u/d/s tuple re-derived; charge attribution under
the provisional rule (§2.3) needs verification; mass predictions
compared to observed.

### 3.2 Refined harmonic-stacking rule for A ≥ 3

Naive additive winding under-binds ³He and ⁴He.  Candidate
mechanisms:

- **Shell closure**: at A = 4 with N = Z = 2, a closed-shell
  configuration on the p-sheet provides extra binding.  Geometric
  origin?
- **Multi-mode coherence**: the harmonic stack at higher A engages
  multiple SL eigenmodes simultaneously.  The composition rule is
  not strict winding addition but coherent mode superposition.
- **Pauli structure across the stack**: each strand carries
  (color, spin) labels (Pauli capacity = 6 per (n_t, n_r) class,
  per R63 Track 10).  At A = 4 with 12 strands on the p-sheet, the
  stack fills 2 Pauli shells; the closed-shell binding may be
  computable.

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

This Q file captures the **h-candidate working theory** that
supersedes the g-candidate's cross-sheet representation of the
nucleon.  It does NOT supersede:

- **Q132 v2** as the rule set on the e-sheet and ν-sheet (still
  applies; R64 doesn't change the lepton sector).
- **R60 T16** (Z₃ confinement) — the harmonic stack respects this
  by construction.
- **R62 derivation 4** (the closed-form mass formula) — R64 still
  uses the flat-torus formula; the magic point is a different
  parameter choice within the same formula.

What it does change:

- **Neutron representation**: cross-sheet `(1, 2, −1, −1, 3, 6)`
  → on-sheet `(0, 0, 0, 0, 3, −2)`.
- **Quark inventory**: single primitive `(1, 2)` → two primitives
  `u = (1, +2), d = (1, −2)`.
- **Working `(ε_p, s_p)`**: `(0.55, 0.162)` (R63) → `(0.073, 0.194)`
  (R64 magic point candidate).
- **Charge rule** (provisional): added u/d sign attribution at the
  primitive level.

---

## 5. Status

**Foundational test passed (R64 Track 1).**  Track 2 (inventory
survival audit) is the next gate.  If Track 2 passes, Tracks 3–7
test the harmonic-stack rule for A ≥ 3, charge derivation, higher-
generation quarks, and the heavier-nucleus binding curve through
Fe.

If Track 2 fails (inventory shatters at the magic point), the
h-candidate falls — same outcome shape as Configuration 1 in R63
Track 11.  The premise survives in principle (Configurations 2–6
of R63's geometric menu remain), but the harmonic-stack-on-p-sheet
specific implementation closes.
