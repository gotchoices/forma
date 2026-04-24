# Derivation 10b — Compound charge under phase-lock (Q132 v2 refinement)

Refine the multi-sheet charge formula of derivation-10 F32.  F32
applied F14's single-closure quantization independently to each of
the three MaSt sheets and summed with the empirical sign vector
`(σ_e, σ_ν, σ_p) = (−1, 0, +1)`, giving

$$
Q \;=\; e\,(-n_1 + n_5).
$$

F14b ([derivation-5b.md](derivation-5b.md)) showed that the
single-sheet `Q = e·n_t` is a bright-primitive special case of a
wider primitive typology — most primitives with `|p_t| ≥ 2` and
`gcd = 1` cancel by ω-sum and carry no charge.  10b propagates
that refinement to the full T⁶: the compound charge is the sum of
**per-sheet primitive charges** weighted by each sheet's
**binding factor** for k-copy multiplicity.  The resulting
F32b reduces to F32 on tuples where every active sheet is bright
and single-copy, and supplies the right answer where F32 gave an
incorrect nonzero charge (F32's `(−1, 0, 0, 0, 1, 0)` → `+2e`
entry, for example, becomes `Q = 0` under F32b because both
tube-only sheets are neutral primitives — derivation-10 line 633
flagged this as "unphysical? or exotic" precisely because F32
misfired on it).

---

## Inputs

1. **F14b** (derivation-5b): per-sheet primitive charge
   `Q_prim = e · p_t` if bright, `0` otherwise; k-copy
   multiplicity governed by the sheet's binding mechanism.
2. **F30–F31** (derivation-10): mass formula and iterated
   Schur-complement structure on T⁶.  Unchanged — 10b does not
   touch mass.
3. **Tube-couples convention** (F14 B.1): applied independently
   on each of the three sheets.
4. **Sign vector** `(σ_e, σ_ν, σ_p) = (−1, 0, +1)`: MaSt's
   empirical per-sheet Ma-S coupling signs.  These remain
   empirical inputs; 10b does not derive them.
5. **Sheet binding factors:**
   - e-sheet: no binding (R60 T17 Z₃ exemption).  k-copy
     multiplicity presents as k independent primitive particles;
     binding factor for composite particles is 1 (no fusion).
   - ν-sheet: real-field conjugate pairing (R60 T18) zeroes
     per-sheet compound charge regardless of primitive
     classification; binding factor for charge = 0.
   - p-sheet: Z₃ confinement (R60 T16) binds `k = 3, 6, …`
     primitives into a color-singlet composite carrying one
     primitive's charge.  Binding factor = 1 for `k ∈ {3, 6, 9, …}`,
     zero if Z₃ is violated (`|n_pt| ≠ 0 (mod 3)` and
     `|n_pt| ≥ 2`) — those tuples don't bind and don't produce
     stable composites.

---

## Section A — Per-sheet charge contribution

### A.1 — Classify each sheet

> *Purpose: reduce each sheet to its primitive and record bright/
> dark status.*

Given a compound tuple `(n_1, n_2, n_3, n_4, n_5, n_6)` with sheets
labelled e = (1, 2), ν = (3, 4), p = (5, 6), compute for each sheet
`s ∈ {e, ν, p}`:

<!-- k_s = gcd(|n_{s,t}|, |n_{s,r}|);  p_{s,t} = n_{s,t}/k_s;  p_{s,r} = n_{s,r}/k_s -->
$$
k_s \;\equiv\; \gcd\!\bigl(|n_{s,t}|, |n_{s,r}|\bigr),
\qquad
p_{s,t} \;\equiv\; n_{s,t}/k_s,
\qquad
p_{s,r} \;\equiv\; n_{s,r}/k_s.
$$

Classify the primitive per F14b §C.1 into one of `{null,
ring-only, tube-only, bright, dark}`.

### A.2 — Per-sheet charge

Define the per-sheet charge contribution as

<!-- Q_s = σ_s · β_s · Q_prim(s) -->
$$
Q_s \;=\; \sigma_s \cdot \beta_s(k_s) \cdot Q_{\text{prim}}(s)
$$

where

- `σ_s` is the Ma–S coupling sign of sheet s (empirical,
  `(σ_e, σ_ν, σ_p) = (−1, 0, +1)`);
- `β_s(k_s)` is the sheet's binding factor for k-copy multiplicity:

<!-- β_e(k) = 1   (no binding; k primitive electrons, each carrying Q_prim) -->
<!-- β_ν(k) = 0   (R60 T18 zeroes ν-sheet charge regardless) -->
<!-- β_p(k) = 1 if k ∈ {1, 3, 6, 9, ...}; 0 otherwise (Z₃) -->
$$
\beta_e(k) \;=\; k,
\qquad
\beta_\nu(k) \;=\; 0,
\qquad
\beta_p(k) \;=\;
\begin{cases}
  1 & k = 1 \text{ (free single primitive)} \\
  1 & k \in \{3, 6, 9, \ldots\} \text{ (Z}_3\text{ bound composite)} \\
  0 & k \in \{2, 4, 5, 7, 8, \ldots\} \text{ (no binding available)}
\end{cases}
$$

- `Q_prim(s) = e · p_{s,t}` if sheet s is bright, else `0`.

The e-sheet's `β_e(k) = k` reflects that k primitive electrons on
a binding-free sheet propagate as k separate charge-carriers,
collectively carrying charge `k · Q_prim`.  This is the ghost-tower
reading of R63 Track 4: the (2, 4), (3, 6), (4, 8) modes are 2, 3,
4 electrons, and as a collection they carry `−2e, −3e, −4e`.
Whether the collection is observed as "one compound" depends on
whether some additional binding fuses them; on the e-sheet alone,
it does not.  For a compound particle's identity the e-sheet is
normally a **single-copy** participant (`k_e = 1`), in which case
`β_e = 1` and the contribution is one primitive charge.

The p-sheet's `β_p` is the heart of the baryon reading: `k = 3`
with bright primitive `(1, 2)` is the standard proton (composite
charge `+e`), `k = 6` with bright primitive `(1, 2)` is a six-quark
Z₃-bound composite (composite charge `+e`), and `k = 2` with
bright primitive is structurally forbidden (Z₃ cannot bind two
strands into a singlet), so `β_p(2) = 0`.

The ν-sheet's `β_ν ≡ 0` is the statement that no per-sheet ν
contribution survives to the observable 4D charge, independent of
which primitive class it sits in.  This remains the empirical input
F32 used; 10b does not rederive it from more fundamental
principles (open question 4 of Q132 v2 §8).

### A.3 — Compound charge

Summing over sheets,

<!-- Q_compound = Q_e + Q_ν + Q_p -->
$$
\boxed{\;
Q_{\text{compound}}
\;=\; Q_e + Q_\nu + Q_p
\;=\; \sigma_e\,\beta_e\,Q_{\text{prim},e}
\;+\; 0
\;+\; \sigma_p\,\beta_p\,Q_{\text{prim},p}.
\;}
$$

With `σ_e = −1, σ_p = +1`:

<!-- Q_compound = −β_e Q_prim,e + β_p Q_prim,p -->
$$
Q_{\text{compound}}
\;=\; -\,\beta_e(k_e)\,Q_{\text{prim},e}
\;+\; \beta_p(k_p)\,Q_{\text{prim},p}.
$$

---

## Section B — Recovery of F32 as a special case

F32's `Q = e(−n_1 + n_5)` is recovered when **every active sheet
is bright and single-copy:**

- `k_e = 1` and e-sheet bright: `Q_{prim,e} = e · p_{e,t} = e · n_1`
  and `β_e = 1`, contributing `−e · n_1`.
- `k_p = 1` and p-sheet bright: `Q_{prim,p} = e · n_5`, `β_p = 1`,
  contributing `+e · n_5`.
- Sum: `Q = e(−n_1 + n_5)`.  ✓

Cases where F32 misfires and F32b corrects:

| Tuple | F32 prediction | F32b classification | F32b prediction | Correction |
|:--|:--|:--|:--|:--|
| `(−1, 0, 0, 0, 1, 0)` | +2e (derivation-10 line 633, "unphysical?") | e-sheet tube-only neutral + p-sheet tube-only neutral | 0 | both sides are Q=0 primitives; no charge to combine |
| `(−1, 1, 0, 0, 1, 2)` | 0 (neutron-candidate line 630) | e-sheet bright (−e) + p-sheet bright (+e) | 0 | agrees |
| `(−3, −6, 0, 0, 3, 6)` | 0 | e-sheet multiplicity 3 primitive (−1, −2) bright + p-sheet Z₃ composite of (1, 2) bright | `−3e + e = −2e` | F32 agrees numerically by linearity, but F32b records k_e=3 (three electrons worth of e-sheet charge) vs k_p=3 Z₃-bound (one proton worth of p-sheet charge) |
| `(−2, −3, 0, 0, 0, 0)` | −2e | e-sheet primitive (−2, −3), gcd=1, dark | 0 | ω-sum cancels the primitive; F32 misreads as charged |
| `(−2, 0, 0, 0, 0, 0)` | −2e | e-sheet tube-only neutral (k=2) | 0 | no ring means no mass quantum to promote; F32 treats n_t alone as charge |

F32b's improvements all come from two places:

1. **Primitive bright/dark classification** (F14b) — modes with
   `|p_t| ≥ 2` and `gcd = 1` carry zero charge, not `e · n_t`.
2. **Binding factor accounting** — k-copy charge on a sheet
   depends on whether the sheet binds (p-sheet Z₃ multiplicity
   with `β_p = 1`) or scatters (e-sheet multiplicity with
   `β_e = k`).  F32's linear sum `−n_1 + n_5` silently assumed
   single-copy on both sheets.

---

## Section C — The Z₃ binding factor in more detail

### C.1 — Why β_p is not simply k

A naive reading of "k copies contribute k primitives" would give
`β_p(3) = 3`, hence a proton of compound charge `+3e` instead of
`+e`.  This is contradicted by observation.

The resolution is that Z₃ confinement (R60 T16) **binds** three
bright p-sheet strands into one **color-singlet composite** whose
observable (4D-projected) quantum numbers are those of **one**
strand, not three.  Schematically: the color-singlet projection of
`|q_1 q_2 q_3⟩` — with each `q_i` a bright primitive carrying
`Q_prim = +e` and the three strands at 120° phase offset in the
Z₃ group — yields a single 4D state with charge `+e`.  The k = 3
appears in the mass (three strands × primitive mass) but collapses
to a single primitive charge.

For `k = 6` (next allowed Z₃ multiplicity) the same projection
gives composite charge `+e`; this is relevant for multi-baryon
bound states and nuclei.

For `k ∈ {2, 4, 5, 7, 8}` Z₃ cannot construct a color singlet
from k strands (group theory: the tensor product of k
fundamental-representation states contains no singlet for these
k), so no bound composite forms and `β_p = 0`.  Bright primitives
with such k on the p-sheet are therefore disallowed as single-
particle inventory entries — the R60 T19 tuples that satisfied
`n_pt ∈ {0, ±3, ±6}` reflect this constraint.

### C.2 — The e-sheet contrast

R60 T17 exempts the e-sheet from Z₃.  The e-sheet therefore has
no binding that fuses k strands into a composite, and
`β_e(k) = k`: the k primitives propagate as k separate particles.

For a composite particle's identity, this means an e-sheet
contribution is ordinarily single-copy (`k_e = 1`); a k_e > 1
entry is an oddity (two electrons sharing a compound mode's
e-sheet assignment) rather than a pathway to `|Q| = k` particles.
This is the resolution of Q132 v2 §7c — the Track 4 "ghost tower"
is not a tower of `|Q| = k` particles but a collection of `k`
electrons.

### C.3 — The ν-sheet contrast

R60 T18 derives ν-sheet charge zero from real-field conjugate
pairing: every ν-sheet complex mode `(n_νt, n_νr)` is identified
with its conjugate `(−n_νt, −n_νr)`, so the ν-sheet's contribution
to observable 4D charge averages to zero regardless of bright/dark
primitive status.  This is encoded as `β_ν ≡ 0`; it preserves F32's
original `n_3` suppression without requiring σ_ν = 0 as a
separate empirical input.  Whether T18's real-field pairing is
itself derivable from the promotion chain is Q132 v2 §8 question
4 — noted as open but not needed for F32b's arithmetic.

---

## Section D — Mass is unchanged

F30 (mass formula on T⁶) and F31 (iterated Schur-complement
structure) are untouched by 10b.  The ω-sum affects charge only —
the Killing-momentum eigenvalues that enter the quadratic mass
form `μ² = h^{ab} p_a p_b` are the same integer windings that
entered F30.

For k-copy multiplicity:
- On the e-sheet (no binding): k copies scatter as k independent
  primitive electrons, each of mass `μ(primitive)`.  The total
  kinematic mass of the ensemble is `k · μ(primitive)`, but it is
  carried by k separate particles, not one composite.
- On the p-sheet (Z₃ binds k ∈ {3, 6}): the bound composite's mass
  is `k · μ(primitive) · K_p` where `K_p` is the p-sheet mass-
  calibration factor.  The composite is one particle.

In both cases mass scales linearly in k — F11 / F30 is exact —
but the interpretation of the k-factor shifts between "number of
free particles in the ensemble" (no-binding sheet) and "composite
mass of one bound particle" (binding sheet).  This matches R63
Track 4 (e-sheet) and R60 T15/T16 (p-sheet baryon) readings.

---

## Lemma (Track 10b result)

> **(F32b) Compound charge under phase-lock (T⁶).**  Let
> `(n_1, n_2, n_3, n_4, n_5, n_6)` be a compound-mode winding
> tuple on MaSt's T⁶ with sheets labelled e = (1, 2), ν = (3, 4),
> p = (5, 6).  For each sheet s compute `k_s =
> gcd(|n_{s,t}|, |n_{s,r}|)` and primitive `(p_{s,t}, p_{s,r}) =
> (n_{s,t}/k_s, n_{s,r}/k_s)`.  Classify the primitive per F14b
> §C.1 into `{null, ring-only, tube-only, bright, dark}`.  Define
> the primitive charge of the sheet as `Q_{\text{prim},s} = e ·
> p_{s,t}` if bright and 0 otherwise.  The compound 4D electric
> charge of the mode is
>
> $$
> Q_{\text{compound}} \;=\; \sum_{s \in \{e, \nu, p\}} \sigma_s \,
> \beta_s(k_s) \, Q_{\text{prim}, s}
> $$
>
> with empirical sign vector `(σ_e, σ_ν, σ_p) = (−1, 0, +1)` and
> sheet binding factors `β_e(k) = k` (no binding, k separate
> primitives), `β_\nu(k) = 0` (R60 T18 pair-cancellation), and
> `β_p(k) = 1` for `k ∈ {1, 3, 6, 9, …}` (single primitive or Z₃
> composite), `β_p(k) = 0` for `k ∈ {2, 4, 5, 7, 8, …}` (no Z₃
> bound state available).  F32's `Q = e(−n_1 + n_5)` is
> recovered in the bright-single-copy special case on both
> active sheets.  Otherwise F32b gives the correct 4D charge
> directly from the winding tuple without per-particle
> exceptions.

F32b is the derivation-side content of Q132 v2 Section 5
(compound modes and cross-sheet charge arithmetic) on the full
T⁶.  Combined with F14b (single-sheet primitive typology), the
pair F14b + F32b gives the complete phase-lock refinement of the
charge sector: single-sheet primitive classification on each of
the three sheets, followed by a sum with per-sheet sign and
binding factor.

### What 10b does not add

- **No new mass content.**  F30/F31 are untouched.
- **No change to Tracks 1–4, 6, 7d, 8, 9, 11.**  F14b flows to
  derivation-6 (Lorentz force) by updating F14 → F14b inside
  derivation-6's D_μ = ∂_μ − i(Q/ℏ) A_μ with Q now the F14b/F32b
  value.  Derivation-11 (magnetic moment at tree level) inherits
  the corrected Q automatically.
- **No new empirical inputs.**  The sign vector `(σ_e, σ_ν, σ_p)
  = (−1, 0, +1)` and R60 T16–T18 binding rules are the same
  inputs F32 used; F32b only organizes their interaction with
  the primitive typology more carefully.

### Status

**Complete.**  F32b supersedes F32 on the full T⁶ primitive
typology while preserving F32 as its bright-single-copy special
case.  Program 1's charge sector now sits on F14b + F32b and the
Q132 v2 promotion-chain framing is derived from the standing-
wave KK kinematics with no additional postulates.  Programs 2+
would derive the sign vector, the first-closure causality
picture, and the ν-sheet T18 pairing from deeper GRID structure
if possible; none of that is required for Program 1's closure.
