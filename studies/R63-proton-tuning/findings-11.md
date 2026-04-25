# R63 Track 11: Curved-torus eigenvalue audit

Track 11 audits R62 derivation 4's flat-torus commitment as the
suspected cause of Track 9/10's binding-deadness.  Phase 11a
re-evaluates the 13-particle inventory under a curved-donut p-sheet
metric (replacing the closed-form mass formula with the
Sturm-Liouville eigenvalue spectrum that 10a's solver returns).
Phase 11b tests whether curvature breaks the k-linearity that
Phase 9c verified for the flat formula, possibly supplying nuclear
binding.

**Both phases return cleanly negative.**  Curved-donut geometry is
*doubly falsified*: it shatters the inventory shape, and where it
breaks k-linearity, it does so in the **anti-binding** direction
(compound modes heavier than the linear sum, not lighter).
Configuration 1 from the geometric-configurations menu is
eliminated.

Scripts:
[`scripts/track11_phase11a_curved_inventory.py`](scripts/track11_phase11a_curved_inventory.py) ·
[`scripts/track11_phase11b_curved_compound.py`](scripts/track11_phase11b_curved_compound.py)
Outputs:
[`outputs/track11_phase11a_inventory.csv`](outputs/track11_phase11a_inventory.csv) ·
[`outputs/track11_phase11a_p_sheet_curvature.csv`](outputs/track11_phase11a_p_sheet_curvature.csv) ·
[`outputs/track11_phase11b_compound.csv`](outputs/track11_phase11b_compound.csv)

---

## Phase 11a — Inventory audit at curved-donut p-sheet

### Method

For each of 15 inventory particles, decompose the mass-squared
contribution per sheet via the block-diagonal sum

<!-- m² = Σ_sheets (2π ℏc/L_ring)² · μ²/k -->
$$
m^2 \;=\; \sum_{\text{sheets}} \bigl(2\pi \hbar c / L_{\text{ring}}\bigr)^2 \cdot
\mu^2 / k.
$$

Replace the **p-sheet** μ² with the Sturm-Liouville eigenvalue
on the donut metric `g = diag(1, (1 + ε cos θ_1)²)`:

<!-- λ_curved = SL eigenvalue of -∂_θ_1[(1+ε cos θ_1) f'] + ε² q²/(1+ε cos θ_1) f = λ (1+ε cos θ_1) f -->
$$
-\partial_{\theta_1}\bigl[(1+\varepsilon\cos\theta_1)\,f'\bigr]
+ \frac{\varepsilon^2 q_{\text{eff}}^2}{1+\varepsilon\cos\theta_1}\,f
= \lambda\,(1+\varepsilon\cos\theta_1)\,f
$$

with `q_eff = n_pr − s_p · n_pt`.  The e-sheet (ε_e = 397) and
ν-sheet (ε_ν = 2) are kept at the flat formula because the
donut-metric form is geometrically singular at ε > 1 and because
their typical mode contributions are far less sensitive to
curvature in any case.

Re-anchor `L_ring_p` so the proton matches `m_p_obs = 938.272 MeV`
under the curved spectrum.  Predict the rest of the inventory.

### F11a.1. Curvature shifts μ² by 38–60% — not uniformly

Per-particle p-sheet `μ²_curved / μ²_flat` ratios at the g-candidate
baseline:

| (n_pt, n_pr) | μ²_flat | μ²_curved | ratio | Δμ/μ |
|:-:|---:|---:|:-:|:-:|
| (3, 6)   | 60.16  | 23.07  | 0.384 | **−38.1%** ← proton anchor |
| (3, 5)   | 50.13  | 19.19  | 0.383 | −38.1% |
| (-3, -3) | 36.07  | 12.43  | 0.345 | −41.3% |
| (-3, 6)  | 71.82  | 27.02  | 0.376 | −38.7% |
| (0, -1)  | 1.00   | 0.293  | 0.293 | **−45.9%** (pion) |
| (0, -3)  | 9.00   | 1.737  | 0.193 | **−56.1%** (η) |
| (0, -4)  | 16.00  | 2.828  | 0.177 | **−58.0%** (kaon) |
| (0, -6)  | 36.00  | 5.767  | 0.160 | **−60.0%** (η′) |

Two distinct curvature-correction classes emerge:

- **Baryons (n_pt ≠ 0)**: 38–41% suppression — relatively uniform.
- **Mesons (n_pt = 0)**: 46–60% suppression — much larger, scaling
  with |n_pr|.

After proton anchoring (which absorbs the baryon class shift),
the **inventory ratios change** because mesons see a different
effective mass scaling than baryons.

### F11a.2. Inventory predictions: shape breaks beyond re-anchor

Predicted vs observed masses with re-anchored `L_ring_p`:

| Particle | Observed | Flat | Curved | Flat err | Curved err |
|:---|---:|---:|---:|---:|---:|
| electron | 0.511 | 0.511 | 0.511 | 0% | 0% |
| muon | 105.66 | 104.78 | 104.78 | −0.83% | −0.83% |
| **proton** | 938.27 | 938.27 | 938.27 | 0% | 0% (anchor) |
| neutron | 939.57 | 938.27 | 938.27 | −0.14% | −0.14% |
| Λ | 1115.68 | 1107.67 | 1083.24 | −0.72% | **−2.91%** |
| Σ⁺ | 1189.37 | 1189.60 | 1189.60 | 0.02% | 0.02% |
| Σ⁻ | 1197.45 | 1197.23 | 1196.68 | −0.02% | −0.06% |
| Ξ⁻ | 1321.71 | 1322.64 | 1315.00 | 0.07% | −0.51% |
| φ | 1019.46 | 1025.23 | 1015.35 | 0.57% | −0.40% |
| η′ | 957.78 | 958.55 | 782.30 | 0.08% | **−18.32%** |
| K⁰ | 497.61 | 495.02 | 344.65 | −0.52% | **−30.74%** |
| K± | 493.68 | 494.93 | 344.52 | 0.25% | **−30.21%** |
| η | 547.86 | 553.10 | 490.38 | 0.96% | **−10.49%** |
| π⁰ | 134.98 | 120.97 | 105.67 | −10.37% | **−21.71%** |
| π± | 139.57 | 120.98 | 105.67 | −13.32% | **−24.29%** |

**Summary**:

| Statistic | Flat baseline | Curved p-sheet |
|:---|:-:|:-:|
| max |error| | 13.3% (pion) | **30.7% (K⁰)** |
| mean |error| | 1.86% | 9.38% |

The kaon error grows from 0.5% (flat) to 30% (curved) — a factor
of ~60 worsening.  The η′ error grows from 0.1% to 18%.  The
inventory's coherent flat-baseline fit is destroyed.

### F11a.3. Why the shape breaks

The flat formula `μ² = (n_t/ε)² + (n_r − s·n_t)²` and the donut
SL eigenvalue have **structurally different scaling** as a function
of the mode quantum numbers.  In particular:

- For `n_t = 0` modes (mesons in the inventory), the flat formula
  gives `μ² = n_r²` while the SL eigenvalue at index 0 (ground
  state) gives a different, ε-dependent value with no clean
  closed form.
- For `n_t ≠ 0` modes (baryons), the SL spectrum's index-`n_t`
  eigenvalue is also ε-dependent and differs from the flat formula
  by curvature corrections.

The two classes shift by different amounts.  No single re-anchor
of `L_ring_p` (or any other single parameter) can absorb both
shifts simultaneously.  A full re-fit of `(ε_p, s_p, K_p,
L_ring_p)` might find a different working point under curved
geometry, but **the relative shift between meson and baryon classes
is structural** — it depends on the SL spectrum's qualitative
shape, not on parameters that can be tuned.

### F11a.4. What Phase 11a establishes

1. **Curved-donut p-sheet does not preserve the inventory.**  After
   proton anchoring, max error grows from 13% (flat baseline) to
   31% (curved); mean error grows from 1.9% to 9.4%.  Five
   particles drift > 10%; two drift > 30%.
2. **The break is in the SHAPE, not the scale.**  Mesons and
   baryons see different effective curvature corrections, so no
   single global re-anchor restores the fit.
3. **Curved-donut geometry is empirically distinguishable from
   flat geometry** by the meson-vs-baryon mass ratio.  Observation
   matches flat (within Track 5/6's ~1.8% precision), not curved.

This is a strong empirical argument that **R62 derivation 4's
flat-torus commitment is the correct physics**, not a simplifying
assumption to be lifted.

---

## Phase 11b — Curved-donut compound vs separated audit

### Method

Solve the SL eigenvalue problem at p-sheet primitives `(k·3, k·6)`
for k = 1, 2, 3, 4 at the g-candidate baseline.  Test whether
`λ(k·3, k·6) = k²·λ(3, 6)` holds (the flat formula's k²-linearity)
or breaks (curvature-induced compound effect).

### F11b.1. k-linearity breaks under curvature, in the wrong direction

| k | (n_t, n_r) | λ_curved | k²·λ(3, 6) | Deviation |
|:-:|:-:|---:|---:|:-:|
| 1 | (3, 6) | 23.080 | 23.080 | 0% (anchor) |
| 2 | (6, 12) | **96.854** | 92.319 | **+4.91%** |
| 3 | (9, 18) | **221.21** | 207.72 | **+6.49%** |
| 4 | (12, 24) | **395.96** | 369.28 | **+7.23%** |

The eigenvalue at compound primitives is **larger** than `k²·λ(3, 6)`,
not smaller.  Curvature **anti-binds** at compound modes, with the
deviation growing with `k`.

### F11b.2. Deuteron-mass prediction under curved p-sheet

| Quantity | Value | Comparison to observed |
|:---|---:|---:|
| 2 · m_p (observed sum) | 1876.54 MeV | exceeds m_d_obs by 0.93 MeV |
| m_compound (flat formula) | 1876.54 MeV | matches 2·m_p exactly (k-linear) |
| m_compound (curved donut) | **1922.08 MeV** | exceeds 2·m_p by **45.5 MeV** |
| m_d (observed) | 1875.61 MeV | binding 2.22 MeV below 2·m_p |

Curved-donut geometry would predict the deuteron is **45.5 MeV
heavier than two free protons** — an enormous anti-binding,
~20× the magnitude of the observed binding and in the wrong
direction.

### F11b.3. Why curvature anti-binds rather than binds

The donut metric `(1 + ε cos θ_1)` has variable curvature: positive
on the outer equator (θ_1 = 0) and negative on the inner equator
(θ_1 = π).  Higher-`n_t` modes are less localized (their density
profile spans a larger fraction of the poloidal direction) and
therefore *sample* the curvature more thoroughly.  The integrated
ε² q²/(1 + ε cos θ_1) term in the SL operator drives higher-mode
eigenvalues *up* relative to the flat formula at the same
quantum numbers, because the smaller-than-1 minimum of
(1 + ε cos θ_1) appears in the denominator of the q² term.

**Geometrically**: curvature concentrates the toroidal-direction
mass density on the inner equator, where the local circumference
is small.  Multi-strand compounds at high `n_t` average more of
this concentration, picking up extra mass.  This is the opposite
of what binding requires.

### F11b.4. What Phase 11b establishes

1. **Curvature breaks k-linearity, but anti-binds.**  λ(6, 12) =
   1.049 · 4·λ(3, 6); compound mode is ~5% heavier than `2·m_p`,
   not lighter.
2. **The break grows with `k`.**  k = 4 gives 7.2% deviation;
   the trend is monotonic.  Heavier nuclei would over-predict
   even more.
3. **Curved-donut geometry does not supply nuclear binding.**
   Even setting aside Phase 11a's inventory-shattering result,
   the deuteron compound under curved geometry is heavier than
   the separated nucleons by 45.5 MeV — wrong sign for binding,
   and ~20× the observed magnitude.

---

## Phase 11c — Not pursued (eliminated by 11b)

Phase 11c was framed as a heavier-nuclei extension conditional on
Phase 11b finding right-sign deuteron binding.  Phase 11b found
the wrong sign; 11c is moot.

---

## Synthesis: Configuration 1 doubly falsified

Track 11's audit answers **two independent questions** about whether
R62 derivation 4's flat-torus commitment is the binding-killer:

**Q1 — Does curvature preserve the inventory?**  No.  Mesons drift
30%; pions, kaons, and η′ all break.  The shape of the SL spectrum
on the donut differs structurally from the flat formula (different
n_t = 0 vs n_t > 0 scaling), and no single parameter re-anchor
restores the fit.

**Q2 — Does curvature supply binding?**  No, the opposite — it
**anti-binds**.  Compound `(6, 12)` gives a curved SL eigenvalue
4.9% larger than `4·λ(3, 6)`, predicting m_compound 45.5 MeV
*above* `2·m_p` rather than 2.2 MeV below.

Both results are independent and consistent: **the donut
metric is wrong physics for MaSt at every scale** — it neither
preserves inventory nor supplies binding.  R62 derivation 4's flat
commitment is correct.

### Implication for the user's premise

The premise *"all forces in S are geometric realities in Ma"* is
**not** rescuable by lifting R62 derivation 4's flat-torus
commitment to a curved donut.  The flat geometry is the right
geometry; curvature breaks both the existing inventory and the
binding direction.

This narrows the strong-force-in-Ma question.  If the premise
holds, the geometric reality producing the strong force is **not**
a curvature of the existing 2-torus sheets — it must be one of
the other configurations in the menu:

- **Configuration 2** — Wilson-line / U(1) holonomy on flat T².
  Single-particle inventory preserved by construction; binding
  lives in multi-strand pairwise interactions.  Most natural
  next configuration to test.
- **Configuration 3** — Higher-genus base for the p-sheet.
  Genus-2 surface provides additional 1-cycle structure that
  compound modes could exploit.  Larger framework change.
- **Configuration 4** — Inter-sheet topological connection
  (brane intersection or conifold).  The deuteron's non-trivial
  cross-sheet content `(1, 2, −1, −1, 6, 12)` could wrap the
  connection while free nucleons don't.
- **Configuration 5** — Dynamical compactification radius.
- **Configuration 6** — Non-Abelian gauge structure on T².

Configuration 2 is the natural Track 12 / next-track candidate
under inventory-preservation discipline — its inventory survival
is built into the construction (Wilson lines don't shift
single-strand mass), so the only test is whether the multi-strand
interaction can supply the deuteron's 2.22 MeV at a principled
parameter choice.

---

## Status

**Track 11 closes negatively.**  Configuration 1 (curved-donut
metric) is doubly falsified: inventory shatters and compound
anti-binds.  R62 derivation 4's flat-torus commitment is robust;
the binding-killer is not the geometric flatness assumption.

**R63's overall position**: Tracks 9–11 have falsified four
distinct families of Ma-internal binding mechanisms (cross-shear
dressing, non-additive tuples, high-n mass corrections, Pauli phase
coherence, Slater-determinant exchange, complementary-shear
compounds, **curved-donut geometry**).  Reading A from Track 10
remains earned: the strong force does not live in any of these
channels.

The user's premise is not yet refuted — it now points specifically
at Configurations 2–6 as the remaining geometric-configuration
candidates, with Configuration 2 as the lowest-cost next test.
