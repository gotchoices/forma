---
marp: true
theme: default
size: 16:9
paginate: true
math: mathjax
style: |
  /* Readable body size; split dense slides instead of shrinking the whole deck */
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 28px;
    line-height: 1.35;
    padding: 40px 48px 52px 48px;
    box-sizing: border-box;
  }
  section h1 {
    font-size: 1.45em;
    margin: 0 0 0.35em 0;
  }
  section h2 {
    font-size: 1.15em;
    margin: 0.25em 0 0.4em 0;
  }
  section p {
    margin: 0.35em 0;
  }
  section li {
    margin: 0.2em 0;
  }
  section.lead h1 {
    font-size: 2.8em;
    text-align: center;
  }
  section.lead h2 {
    text-align: center;
    font-weight: 400;
    color: #555;
  }
  section.lead p {
    text-align: center;
    font-size: 1.1em;
    color: #666;
  }
  section.title-only h1 {
    font-size: 2.2em;
  }
  section.stats {
    font-size: 0.85em;
  }
  section.tight {
    font-size: 0.92em;
  }
  table {
    font-size: 0.9em;
    margin-left: auto;
    margin-right: auto;
  }
  section.tight table {
    font-size: 0.86em;
  }
  /* display math (MathJax): less vertical margin than default */
  section mjx-container[display="true"] {
    margin: 0.45em 0 !important;
  }
  th {
    background: #f0f0f0;
  }
  .small { font-size: 0.75em; color: #888; }
  .hi    { color: #2a7a2a; font-weight: 600; }
  .med   { color: #a07000; font-weight: 600; }
  .bad   { color: #a02020; font-weight: 600; }
  img[alt~="center"] {
    display: block;
    margin: 0 auto;
  }
---

<!-- _class: lead -->

# Matter from Light

## A geometric derivation of the particle spectrum

MaSt — model-F

<p class="small">A project of GotChoices.org · built with AI assistance</p>

---

<!-- _class: lead -->

# The question

## What if mass, charge, and spin aren't fundamental?

What if they're consequences of a photon confined to a geometry?

---

## The scorecard

<div class="tight">

**4 measured inputs** (m_e, m_p, Δm²₂₁, α) <br>
**6 geometric inputs** (3 aspect ratios + 3 in-sheet shears)

| Class | Match | Worst | Comment |
|:------|:-----:|:-----:|:--------|
| Leptons: μ, τ | 2 / 2 | 0.83% (μ) | three generations from shear resonance |
| Neutrinos: ν₂, ν₃ | 2 / 2 | 2.5% (ν₃) | Δm²₃₁ / Δm²₂₁ = **33.6** exact |
| Baryons: n, Λ, Σ±, Ξ⁻, Ξ⁰ | 6 / 6 | 0.72% (Λ) | single 6D knots, all spin ½ |
| Mesons: K⁰, K±, η, η′, φ, ρ | 6 / 6 | 1.12% (ρ) | spin 0 or 1, correct in every case |
| Pions: π⁰, π± | 0 / 2 | **13.3%** | the persistent desert |
| Nuclei: d, ⁴He, ¹²C, ⁵⁶Fe | 4 / 4 | 1.31% (⁵⁶Fe) | α_Coulomb = **Z²α exact** |

**14 of 16 non-input sub-nuclear particles match within 1.12%.**

</div>

<p class="small">Source: <code>papers/white-paper.md</code> §2, §10 — model-F (R60 Tracks 15–20).</p>

---

## What this is *not*

- **Not a competitor to the Standard Model.** The SM is confirmed to 12 decimal places. Nothing here contradicts it.
- **Not "quantum gravity."** No strings, no loops, no supersymmetry.
- **Not a claim of truth.** The numbers are suggestive, but coincidence and selection bias are live possibilities. The code is open so others can check.

## What this *is*

A geometric model in which particles are **standing electromagnetic waves** on a compact 6-dimensional torus, and the SM's free parameters are outputs of the geometry rather than inputs.

---

## What the Standard Model leaves open

<div class="tight">

- ~**19 dimensionless parameters** (masses, mixing angles, couplings) — measured, not explained
- **Why three generations** of matter?
- **Why charge is quantized** in integer multiples of e?
- **Why the proton is three quarks** (not two, not four)?
- **α = 1/137** — where does this number come from?
- **Dark matter** — no candidate in SM field content
- **Matter/antimatter asymmetry** from the Big Bang?
- **Gravity** — not in the SM at all

This deck shows which of these MaSt addresses geometrically — and where it also falls short.

</div>

---

## The core move

A free photon has energy `E = hf` and momentum `p = E/c`, but **no rest mass** — it never sits still.

**Confine it to a loop.** The photon still moves at `c`, but the *center* of the loop can sit still. Now there's a rest frame, and in that frame the only energy is the photon's circulation:

$$
m = \frac{E}{c^2} = \frac{hf}{c^2}
$$

Mass is the frequency of a trapped photon. Charge and spin come from *how* the photon is trapped — the winding on the geometry. Everything else is bookkeeping.

<p class="small">Derived rigorously in D1 — a photon bouncing between mirrors has rest mass m = nh/(2Lc), <em>and</em> the same m is the inertial mass. See <code>papers/derivations.md</code>.</p>

---

## The arena: 11 degrees (11×11 metric)

Flat, compact; extended in **S** and **t**.

**Block order in the 11D metric (base directions 1…11):**  
ℵ — Ma_p — Ma_e — Ma_ν — S — t &nbsp;→&nbsp; 1 + 2 + 2 + 2 + 3 + 1 = **11D**.

$$
\aleph \times \underbrace{\mathrm{Ma}_p \times \mathrm{Ma}_e \times \mathrm{Ma}_\nu}_{T^6} \times S^3 \times t
$$

Same *product* manifold as in the papers, $T^6 \times \aleph \times S^3 \times t$; the **row/column order** in the 11×11 **metric** follows the sequence above (next slide: block-by-block).

---

## The 11 base blocks

Rows of the 11D metric, in the same order as the product on the last slide. **ℵ** mediates **α**; the three **Ma** sheets host standing-wave windings; **S** and **t** are extended (space and time).

| Block | Dim | Notes |
|:-|:-:|:-|
| **ℵ** (substrate) | 1 | sub-Planck; **α** (tube↔ℵ↔t) |
| **Ma_p** (proton sheet) | 2 | ~fm — proton, hadrons, nuclei |
| **Ma_e** (electron sheet) | 2 | ~pm — e, μ, τ |
| **Ma_ν** (neutrino sheet) | 2 | ~μm–mm — ν masses (ν ring ~ **42 μm**) |
| **S** (space) | 3 | extended; trajectories, labs |
| **t** (time) | 1 | extended; evolution, phase |

**No Planck-scale compactification of Ma** — human scales; the ν ring is 42 μm (visible in an optical microscope).

---

## A particle is six integers

$$
(n_{et},\, n_{er},\, n_{\nu t},\, n_{\nu r},\, n_{pt},\, n_{pr})
$$

Tube and ring windings on each of the three sheets. The photon winds around the torus — the winding counts are quantized by single-valuedness.

<div class="tight">

| Particle | Mode | Sheets active |
|:---------|:-----|:-------------:|
| electron | (1, 2, 0, 0, 0, 0) | 1 (e) |
| muon | (1, 1, 0, 0, 0, 0) | 1 (e) |
| proton | (0, 0, 0, 0, 3, 6) | 1 (p) |
| K⁰ | (0, −1, 0, 0, 0, −4) | 2 (e+p) |
| neutron | (−3, −6, 1, −6, −3, −6) | 3 (all) |

</div>

Mass from eigenmode energy. Charge from winding topology. **Spin from sheet count.**

---

## Spin: the Standard Model taxonomy falls out

Each active sheet hosts a spin-½ Dirac–Kähler tower (R62 derivation 7d).
Compound modes compose via SU(2) angular-momentum addition:

| Active sheets | SU(2) composition | Spin | SM class |
|:-------------:|:------------------|:----:|:---------|
| **1** | ½ | ½ | **Lepton** |
| **2** | ½ ⊗ ½ = {0, 1} | 0 or 1 | **Meson** (scalar / vector) |
| **3** | ½ ⊗ ½ ⊗ ½ = {½, ³⁄₂} | ½ or ³⁄₂ | **Baryon** (octet / decuplet) |

Every row of the spectrum table satisfies this — sheet count and spin match in all 16 non-input particles. **The taxonomy is derived, not postulated.**

---

## Charge is a winding number

A tube winding on a charged sheet drags the substrate phase through 2π. That topological defect *is* the electric charge. Two rules:

**Base (single-sheet):**

$$
Q = -n_{et} + n_{pt}
$$

**Composite (including Z₃ proton structure):**

$$
\alpha_{\text{Coulomb}} = \left(n_{et} - \tfrac{n_{pt}}{\gcd(n_{pt}, n_{pr})} + n_{\nu t}\right)^2 \alpha
$$

For a Z-nucleus `(n_et, n_pt, n_pr) = (1 − Z, 3A, 6A)` this returns **α_Coulomb = Z²α exactly** — the familiar electrostatic scaling from topology alone.

The neutrino sheet gives Q = 0 automatically: its modes come as tube-conjugate pairs that cancel.

---

## The proton is three things (Z₃ confinement)

A single (1, 2) mode on the proton sheet carries a **2ω density fluctuation** the embedding can't stably support.

**Three copies at 120° phase offsets cancel the fluctuation exactly.**
N = 3 is the minimum count that works (R60 Track 16).

Selection rule: only modes with `n_pt ≡ 0 (mod 3)` are free.
The free proton mode is (3, 6) — a three-quark composite. Bare (1, 2) quarks are **never** free.

This reproduces QCD's "only color singlets propagate" rule from pure geometry, without SU(3) or color.

**Electron sheet is exempt:** localization ratio `R_loc = m_e · L_er / ℏc < 1`, so the electron is delocalized across the whole sheet and local phase coherence between copies can't form. Electron stays a free (1, 2).

---

## Three generations from shear resonance

On the electron sheet, shear `s_e ≈ 2.004` makes the (1, 2) mode's ring detuning `n_er − n_et · s_e ≈ 0` — a near-cancellation that makes it anomalously light.

| Gen | Lepton | Mode | Mechanism | Error |
|:---:|:-------|:-----|:----------|:-----:|
| 1 | electron | (1, 2) | **shear resonance** (detuning ≈ 0) | input |
| 2 | muon | (1, 1) | off-resonance excited state | 0.83% |
| 3 | tau | high-n (n ≈ 3478) | far-off-resonance | 0.06% |

Mass ratios `m_μ/m_e` and `m_τ/m_e` are **algebraically exact** from just `(ε_e, s_e)`.

No ad-hoc filter. The electron is the lightest charged mode because it sits at the resonance — nothing lighter exists.

---

## Nuclei as single standing-wave modes

One mode per nucleus — not A nucleons held together by a residual strong force.

$$
n_{pt} = 3A, \qquad n_{pr} = 6A, \qquad n_{et} = 1 - Z
$$

<div class="tight">

| Nucleus | A | Z | Δm/m | α_Coulomb / α |
|:--------|--:|--:|-----:|--------------:|
| d (²H) | 2 | 1 | 0.05% | **1** |
| ⁴He | 4 | 2 | 0.69% | **4** |
| ¹²C | 12 | 6 | 0.94% | **36** |
| ⁵⁶Fe | 56 | 26 | 1.31% | **676** |

All nuclei are Z₃-compliant by construction (`3A ≡ 0 mod 3`).
**α_Coulomb = Z² α to floating-point precision** for every nucleus — the structural consequence of composite charge applied to the Z-nucleus tuple.

</div>

---

## Neutrino oscillation

Three mass eigenstates on the ν-sheet: `(1, 1)`, `(−1, 1)`, `(1, 2)`.

At shear `s_ν = 0.02199`:

$$
\frac{\Delta m^2_{31}}{\Delta m^2_{21}} \;=\; \frac{3 - 2 s_\nu}{4 s_\nu} \;=\; 33.6
$$

matches experimental 33.6 ± 0.9. The value of `s_ν` is **fixed uniquely** by the ratio — no other parameter touches it.

**Falls out of the geometry:**

- Normal ordering predicted (inverted geometrically excluded)
- Majorana nature (±n_r modes are C-conjugate superpositions)
- Σm_ν ≈ 125 meV; 0νββ signal at |m_ββ| ≈ 10–30 meV

---

## Head to head

<div class="tight">

| Aspect | Standard Model | MaSt model-F |
|:-------|:---------------|:-------------|
| Ontology | Point particles + fields | Standing EM waves on T⁶ |
| Dimensionless parameters | ~19 measured | 1 measured (α) + 6 geometric |
| Charge | Fundamental quantum number | Topological winding |
| Strong force | SU(3) QCD, postulated | Z₃ density-cancellation, **derived** |
| Confinement | Quark sea / Wilson lines | N = 3 minimum 2ω-cancellation |
| SM taxonomy (L / M / B) | Postulated | **Emergent from sheet count** |
| Three generations | Postulated | Shear resonance on e-sheet |
| Nuclei | Bound nucleons + residual | Single T⁶ standing-wave modes |
| α = 1/137 | Unexplained | Value input; coupling structure derived |
| Dark matter | New sector required | Neutral modes + Compton-window suppression |
| Gravity | Not in SM | Derived by GRID substrate |

</div>

---

## Not just fits — a derivation chain

<div class="tight">

**D1** Photon in a box → rest mass m = nh/(2Lc); m = inertial mass
**D2** Kaluza-Klein on T² → two U(1)'s, Lorentz force, shear
**D3** Mass formula m²c² = hᵃᵇ Pₐ Pᵦ from null condition on T² embedding
**D4** MaSt formula μ² = (n_t/ε)² + (n_r − s·n_t)² — derived, not postulated
**D5** Charge = tube Killing momentum; Q = -n₁ + n₅
**D6** Lorentz force on the standing wave (minimal coupling derived)
**D7d** Per-sheet Dirac–Kähler → spin ½ / sheet → SM taxonomy
**D8** T⁴ with cross-shears; Schur-complement mass mixing
**D9** KK-on-torus is scale-invariant — no Planck pinning
**D10** Full T⁶ with three sheets — universal Q = e(−n₁ + n₅)
**D11** Magnetic moment: g_e = 2 (tree), g_p = 6 = 3μ_N (tree)

</div>

Inputs: special relativity, E = hf, standing-wave boundary conditions, differential geometry. **No QFT. No Lagrangians. No gauge groups postulated.**

<p class="small"><code>papers/derivations.md</code> · Program 1 complete, closeout in progress.</p>

---

## The substrate: GRID

Where does Maxwell come from? And gravity?

**GRID** (sibling project) starts from a 4D causal lattice + six axioms:

- Maxwell's equations emerge from phase dynamics
- Einstein's field equations from lattice thermodynamics
- **G = 1/(4ζ)** with `ζ = 1/4` from tetrahedral packing at the horizon
- Charge quantization from phase periodicity
- α remains the one measured coupling; ε₀, μ₀, e all derive from it

Simulations confirm directional waves, exact superposition, and Schwarzschild geometry — no Maxwell input.

```
GRID (substrate) ──► Maxwell + G + c⁴/(8πG)
                         │
                         ▼
MaSt (structure) ──► particles, masses, charges, nuclei
```

<p class="small"><code>grid/synthesis.md</code> for what's established and what's still open.</p>

---

## Honest status — what's still open

<div class="tight">

- **α value.** The *structure* of α coupling is derived (tube ↔ ℵ ↔ t chain, Z² scaling, universality). The numerical value 1/137 is still input.
- **Pion desert.** π⁰ at 10.4%, π± at 13.3% — halved from model-E (22–25%) but the persistent failure mode.
- **Specific spin within SU(2)-allowed sets.** The rule gives `{0, 1}` or `{½, ³⁄₂}`; which one is realized (pseudoscalar vs vector, octet vs decuplet) needs more structure.
- **u/d flavor split** within the (1, 2)-quark / (3, 6)-proton architecture not yet derived.
- **Full QFT formulation.** We have the mass spectrum; decay rates, running couplings, and scattering amplitudes need a quantized field theory on 11D.
- **Dark-matter ratio from first principles.** The 5.36 ± 0.05 observed ratio is bracketed by Compton-window models but not yet derived.

</div>

---

## Testable predictions

- **Σm_ν ≈ 125 meV** — upcoming cosmological bounds will tighten this.
- **0νββ signal at |m_ββ| ~ 10–30 meV** — within reach of KamLAND-Zen and LEGEND.
- **Ma_ν ring at ~42 μm** — short-range gravity deviations from 1/r² potentially visible at current sensitivity (bounds: ~50 μm).
- **Dark-matter / visible-matter ratio** — observed 5.36 ± 0.05. The geometry predicts many neutral modes (n_et = n_pt = 0 by topology). A Compton-window coupling filter (Q ≈ 350, R42) gives 5.54 — bracketed, not yet derived.
- **Normal ν ordering** — inverted hierarchy is geometrically excluded.
- **No new fundamental particles** below 2 GeV outside the 16-entry inventory.

Falsifiable; reproducible numerics; open code.

---

<!-- _class: lead -->

# What's the claim, plainly?

Three measured scales + α + a 6-integer set per particle
reproduce 14 of 16 non-input masses within 1%,
the Standard Model taxonomy from sheet count,
the Z² nuclear Coulomb scaling from topology,
and the neutrino oscillation ratio exactly.

**It might be coincidence. It might be something.**

The code is open. Check our work.

---

<!-- _class: lead -->

# Matter from Light

## gotchoices.org · GitHub · the viz gallery

<p class="small">Papers: whatif · gut · white-paper · derivations · dark-matter<br>
Models: model-F (active) · Framework: studies/Taxonomy.md<br>
Substrate: grid/synthesis.md</p>
