# Exotic-particle catalog and sheet-classification

**Status:** Working catalog. Tabulates known hadrons by sheet
(generation), distinguishes long-lived closures from short-lived
resonances, and tests the framework's "1 sheet per quark generation"
hypothesis against observation. Built to support the chapter arc's
§What we don't predict and to set up the spectrum-completeness
question for the modulated-clover substrate.

The arc's working assumption (sheet-proton + ma-domain) is that
each quark generation lives on its own 2-D sheet, with proton/neutron
analogs as the two (1/2, ±1) baryon modes on each sheet. This
file checks that assumption against the observed hadron spectrum:
which hadrons are *single-generation* (live on one sheet) and which
require *multi-sheet coupling* (cross-generation), and which
particles fit the (1/2, 1) mode picture versus other mode classes.

---

## 1. Categorisation scheme

### 1.1 Lifetime category — closure vs resonance

The framework's natural time unit is the **cycle time** of a
particle's wave on its track:

<!-- τ_cycle = h / (m c²) = (4.14 × 10⁻²¹ s) · (1 MeV / m c²) -->
$$
\tau_{\text{cycle}} \;=\; \frac{h}{m c^2}
\;\approx\;
4.14 \times 10^{-21}\,\text{s} \cdot
\frac{1\,\text{MeV}}{m c^2}.
$$

A particle's **lifetime measured in cycles** is τ_lifetime / τ_cycle.

| Category | Cycle count | Reading in the framework |
|---|---|---|
| **stable** | ∞ | full closure-satisfying mode; no decay channel open |
| **closure-with-decay** | ≫ 1 (typically ≥ 10⁵) | full closure of the wave equation; finite lifetime via *external* coupling (weak interaction, EM) — substrate dynamics are stationary |
| **resonance** | ~ 1 (typically 0.5–10) | not a closure-satisfying mode; quasi-stationary "ringing" of the cavity, dissipating via strong-decay channel; complex eigenvalue |

The cycle count distinguishes **two structurally different kinds of
object**, which the arc's "closure-satisfying mode" picture covers
the first kind of and leaves the second as deferred *resonance
machinery*.

### 1.2 Sheet (generation) category

The framework's working assumption: each quark generation hosts
one 2-D sheet. The three sheets are:

| Sheet | Up-type | Down-type | Mass scale |
|---|---|---|---|
| ud | u (+2/3, ~2 MeV) | d (−1/3, ~5 MeV) | ~ 1 GeV |
| cs | c (+2/3, ~1.3 GeV) | s (−1/3, ~95 MeV) | ~ 1–3 GeV |
| tb | t (+2/3, ~173 GeV) | b (−1/3, ~4.2 GeV) | ~ 10–340 GeV |

Pure-generation particles use quarks from only one of the three
columns; cross-generation particles use quarks from two or three
columns.

### 1.3 Topology category

| Topology | Quark content | Framework reading |
|---|---|---|
| Baryon | qqq | one (1/2, 1) baryon track |
| Antibaryon | q̄q̄q̄ | (−1/2, −1) — C-conjugate |
| Meson | qq̄ | new closure mode (compound or different (m,n)); not yet derived |
| Tetraquark / pentaquark / exotic | qqq̄q̄, qqqqq̄ etc. | further-deferred multi-knot composition |

### 1.4 Observation status

| Flag | Meaning |
|---|---|
| **obs** | observed and well-established in PDG |
| **obs?** | observation reported but contested / not yet confirmed |
| **pred** | predicted by the standard model, not yet observed |

### 1.5 Spin and parity (J^P)

All tables carry a **J^P** column listing the particle's total
angular momentum J and parity P (intrinsic discrete quantum
numbers). The J^P values are empirical PDG values.

**Framework working hypothesis (untested):** spin in this
framework is **read off the winding numbers**, not imposed via a
spinor upgrade. The baryon ground-state modes are (m, n) =
(1/2, ±1) and have spin 1/2 — the framework reads spin from the
m winding (or possibly from the ratio m/n; (1/2, 1) does not
distinguish these). Exotic-spin particles are then expected to
emerge from:

- **Different (m, n) modes** on the same sheet (e.g. a (3/2, 1)
  candidate for the spin-3/2 Δ family — three half-twists in the
  tube direction per ring revolution).
- **Combinations of modes** across the same or different sheets,
  with spin angular-momentum adding by standard rules (e.g.
  qq̄ mesons as two (1/2, 1)-type modes combining: anti-aligned
  → 0⁻ pseudoscalar; aligned → 1⁻ vector).
- **Combinations across multiple sheets** for cross-generation
  hadrons and unusual J^P values.

This is the same kind of reasoning that worked well in
[model-F](../../models/model-F.md) for the charged-lepton sector;
it is untested for hadron spin and is the framework's working
*hypothesis*, not yet a derivation. The J^P column in the
tables is the **target** any future winding-combination analysis
must reproduce: every entry's J^P is a number the framework
must derive from the relevant mode structure.

A spin–cycle correlation is visible in the catalog *empirically*
(noted in §7) — spin-aligned configurations (3/2⁺ baryons,
broad 1⁻ mesons) tend to be ~1-cycle resonances, while
spin-antialigned configurations (1/2⁺ baryons, 0⁻ mesons) tend
to be long-lived closures. Whether the framework's
winding-combination reading explains this correlation is an
open question.

---

## 2. The ud sheet — single-generation hadrons

The construction's settled territory. Quark content from {u, d, ū, d̄}.

### 2.1 ud baryons

| Particle | Quarks | J^P | Charge | Mass (MeV) | Width / lifetime | Cycles | Category | Status |
|---|---|---|---|---|---|---|---|---|
| p | uud | 1/2⁺ | +1 | 938.27 | stable (> 10³⁴ yr) | ∞ | closure | obs |
| n | udd | 1/2⁺ | 0 | 939.57 | τ = 880 s | ~ 2 × 10²⁶ | closure-with-decay (weak) | obs |
| Δ⁺⁺ | uuu | 3/2⁺ | +2 | 1232 | Γ = 117 MeV | ~ 1.7 | resonance | obs |
| Δ⁺ | uud | 3/2⁺ | +1 | 1232 | Γ = 117 MeV | ~ 1.7 | resonance | obs |
| Δ⁰ | udd | 3/2⁺ | 0 | 1232 | Γ = 117 MeV | ~ 1.7 | resonance | obs |
| Δ⁻ | ddd | 3/2⁺ | −1 | 1232 | Γ = 117 MeV | ~ 1.7 | resonance | obs |
| N(1440) "Roper" | uud, udd | 1/2⁺ | +1, 0 | 1440 | Γ ≈ 350 MeV | ~ 0.7 | resonance | obs |

**Observations:**
- The proton/neutron pair *is* the (1/2, ±1) baryon doublet the
  construction commits to.
- The Δ baryons are spin-3/2 resonances with ~ 1 cycle lifetime.
  They are *not* closure-satisfying modes in the framework's
  current sense. Δ⁺⁺ (uuu) and Δ⁻ (ddd) additionally cannot be
  hosted by an (1/2, 1) track on the symmetric Z₂×Z₃ substrate
  (the track's lobe-saddle alternation forbids three-of-a-kind
  quark sequences). They need the resonance machinery *and* a
  topology that allows pure-flavor sequences.

### 2.2 ud mesons

| Particle | Quarks | J^P | Charge | Mass (MeV) | Width / lifetime | Cycles | Category | Status |
|---|---|---|---|---|---|---|---|---|
| π⁺ | ud̄ | 0⁻ | +1 | 139.57 | τ = 2.6 × 10⁻⁸ s | ~ 9 × 10¹⁴ | closure-with-decay (weak) | obs |
| π⁻ | dū | 0⁻ | −1 | 139.57 | τ = 2.6 × 10⁻⁸ s | ~ 9 × 10¹⁴ | closure-with-decay (weak) | obs |
| π⁰ | (uū − dd̄)/√2 | 0⁻ | 0 | 134.98 | τ = 8.4 × 10⁻¹⁷ s | ~ 3 × 10⁶ | closure-with-decay (EM) | obs |
| ρ⁺ | ud̄ | 1⁻ | +1 | 775 | Γ = 149 MeV | ~ 0.8 | resonance | obs |
| ρ⁰ | (uū − dd̄)/√2 | 1⁻ | 0 | 775 | Γ = 149 MeV | ~ 0.8 | resonance | obs |
| ρ⁻ | dū | 1⁻ | −1 | 775 | Γ = 149 MeV | ~ 0.8 | resonance | obs |
| ω | (uū + dd̄)/√2 | 1⁻ | 0 | 782.6 | Γ = 8.5 MeV | ~ 14 | borderline | obs |
| f₀(500) "σ" | (uū + dd̄) | 0⁺ | 0 | 400–550 | Γ = 400–700 MeV | ~ 0.5 | resonance (broad) | obs |

**Observations:**
- The pions live ~ 10⁶–10¹⁵ cycles — they are *full closures* with
  *external* (weak, EM) decay channels.
- The ρ mesons live ~ 1 cycle — they are *resonances* of the same
  quark content as the pions. Pion and ρ have the same flavor
  content but different *mass and lifetime class*; structurally
  these need different framework treatment (closure vs resonance).
- ω is borderline: 14 cycles, well above the resonance scale but
  short of the pion class. The framework might treat it as
  closure-with-strong-decay-channel — a true mode whose decay
  channel is strong rather than weak/EM.
- η (548 MeV) and η' (958 MeV) — flavor content mixes u, d, s
  quarks; listed under cross-generation (§5) below.

---

## 3. The cs sheet — single-generation hadrons

Quark content from {c, s, c̄, s̄}.

### 3.1 cs baryons

| Particle | Quarks | J^P | Charge | Mass (MeV) | Lifetime / width | Cycles | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| Ω_c⁰ | ssc | 1/2⁺ | 0 | 2695.2 | τ = 2.68 × 10⁻¹³ s | ~ 1.8 × 10¹¹ | obs | **"heavy neutron" analog of cs sheet** |
| Ω_cc⁺ | ccs | 1/2⁺ | +1 | ~3700 (pred) | predicted, weak decay | (pred ~ 10¹²) | **pred / obs?** | **"heavy proton" analog of cs sheet — search ongoing at LHCb** |
| Ω⁻ | sss | 3/2⁺ | −1 | 1672.5 | τ = 8.2 × 10⁻¹¹ s | ~ 3 × 10¹³ | obs | "all-s Δ analog"; stabilised against strong decay by being the lightest sss state |
| Ω_ccc⁺⁺ | ccc | 3/2⁺ | +2 | ~4800 (pred) | predicted | — | **pred** | triple-charm, never observed |

**The proton/neutron analogs on the cs sheet:**
- Ω_c⁰ (css) is the confirmed "heavy neutron" — observed, mass
  ~ 2.87× m_neutron, τ very short (weak decay via charm transition)
  but still **~ 10¹¹ cycles** in framework terms. A clean full
  closure.
- Ω_cc⁺ (ccs) is the predicted "heavy proton". Experimental status
  uncertain — LHCb has searched and reported candidates but
  confirmation is not yet at PDG-established level.

### 3.2 cs mesons

| Particle | Quarks | J^P | Charge | Mass (MeV) | Lifetime / width | Cycles | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| φ | ss̄ | 1⁻ | 0 | 1019.5 | Γ = 4.25 MeV | ~ 37 | obs | true closure with narrow strong decay |
| η_c (1S) | cc̄ | 0⁻ | 0 | 2983.9 | Γ = 32 MeV | ~ 31 | obs | charmonium pseudoscalar |
| J/ψ | cc̄ | 1⁻ | 0 | 3096.9 | Γ = 92.6 keV | ~ 5300 | obs | charmonium vector; long-lived narrow resonance |
| ψ(2S) | cc̄ | 1⁻ | 0 | 3686.1 | Γ = 294 keV | ~ 1700 | obs | charmonium 2S |
| χ_c0 | cc̄ | 0⁺ | 0 | 3414.7 | Γ = 10.8 MeV | ~ 38 | obs | charmonium scalar |
| χ_c1 | cc̄ | 1⁺ | 0 | 3510.7 | Γ = 0.84 MeV | ~ 470 | obs | charmonium axial-vector |
| χ_c2 | cc̄ | 2⁺ | 0 | 3556.2 | Γ = 1.97 MeV | ~ 200 | obs | charmonium tensor |
| D_s⁺ | cs̄ | 0⁻ | +1 | 1968.4 | τ = 5.0 × 10⁻¹³ s | ~ 7 × 10¹¹ | obs | charm-strange pseudoscalar |
| D_s⁻ | sc̄ | 0⁻ | −1 | 1968.4 | τ = 5.0 × 10⁻¹³ s | ~ 7 × 10¹¹ | obs | |
| D_s*⁺ | cs̄ | 1⁻ | +1 | 2112.2 | (narrow) | — | obs | vector excitation |

The cc̄ "charmonium" family (η_c, J/ψ, χ_c, ψ', etc.) is rich and
its narrow widths (J/ψ has τ ~ 5300 cycles) indicate the framework's
"closure" reading is the right one for these — not resonances.

---

## 4. The tb sheet — single-generation hadrons

Quark content from {t, b, t̄, b̄}.

### 4.1 tb baryons — none observed

**The framework predicts** (1/2, ±1) baryon doublets on every
quark sheet:

| Particle (predicted) | Quarks | J^P | Predicted mass | Status |
|---|---|---|---|---|
| "ttb" (heavy proton) | ttb | 1/2⁺ | ~ 350 GeV | **does not exist** |
| "tbb" (heavy neutron) | tbb | 1/2⁺ | ~ 180 GeV | **does not exist** |
| Ω_bbb | bbb | 3/2⁺ | ~ 14.3 GeV | **pred** (not observed) |

**Why nothing exists:** The top quark's intrinsic weak-decay
lifetime is **τ_t ≈ 5 × 10⁻²⁵ s**, *shorter* than the QCD binding
timescale Λ_QCD⁻¹ ≈ 10⁻²⁴ s. The top decays before any hadron can
form. There are *no observed top hadrons of any kind* — not just
no ttb / tbb baryons, but no T mesons (t-anything), no toponium
(tt̄). This is an empirical fact, established since the top quark's
1995 discovery.

The framework can in principle accommodate this: the (1/2, 1) mode
exists *in principle* on the tb sheet, but its formation requires
~ 1 hadron-cycle, while the t-quark dissipates faster than that.
The mode cannot stabilise.

### 4.2 tb mesons — bottomonium only

| Particle | Quarks | J^P | Charge | Mass (MeV) | Lifetime / width | Cycles | Status |
|---|---|---|---|---|---|---|---|
| η_b (1S) | bb̄ | 0⁻ | 0 | 9398.7 | Γ = 10 MeV | ~ 6 × 10² | obs |
| Υ(1S) | bb̄ | 1⁻ | 0 | 9460.3 | Γ = 54 keV | ~ 2.8 × 10⁴ | obs |
| Υ(2S) | bb̄ | 1⁻ | 0 | 10023.3 | Γ = 32 keV | ~ 4.5 × 10⁴ | obs |
| Υ(3S) | bb̄ | 1⁻ | 0 | 10355.2 | Γ = 20 keV | ~ 7 × 10⁴ | obs |
| Υ(4S) | bb̄ | 1⁻ | 0 | 10579.4 | Γ = 20.5 MeV | ~ 70 | obs |
| χ_b0(1P), χ_b1(1P), χ_b2(1P) | bb̄ | 0⁺, 1⁺, 2⁺ | 0 | ~ 9.85–9.91 GeV | narrow | various | obs |
| (no T mesons) | tx̄ | — | — | — | — | — | **does not exist** |

The bottomonium family is the only tb-sheet hadron sector
populated. The bb̄ binding is well-established and the Υ states
are extremely narrow (high Q resonances).

---

## 5. Cross-generation hadrons — multi-sheet coupling required

These hadrons require quarks from more than one generation. They
cannot be hosted by a single-generation sheet under the current
framework. Their existence and properties are *out of scope* for
sheet-proton and are deferred to ma-domain / metric-binding for
the cross-sheet coupling mechanism. Listed here so the *size* of
this category is visible.

### 5.1 Strange (u-d-s) hadrons

| Particle | Quarks | J^P | Charge | Mass (MeV) | Lifetime / width | Cycles | Status |
|---|---|---|---|---|---|---|---|
| K⁺ | us̄ | 0⁻ | +1 | 493.7 | τ = 1.24 × 10⁻⁸ s | ~ 1.5 × 10¹⁵ | obs |
| K⁻ | sū | 0⁻ | −1 | 493.7 | (same as K⁺) | ~ 1.5 × 10¹⁵ | obs |
| K⁰ | ds̄ | 0⁻ | 0 | 497.6 | (oscillates) | — | obs |
| K⁰_S | (ds̄ − sd̄)/√2 | 0⁻ | 0 | 497.6 | τ = 8.95 × 10⁻¹¹ s | ~ 1.1 × 10¹³ | obs |
| K⁰_L | (ds̄ + sd̄)/√2 | 0⁻ | 0 | 497.6 | τ = 5.1 × 10⁻⁸ s | ~ 6 × 10¹⁵ | obs |
| K*(892)⁺ | us̄ | 1⁻ | +1 | 891.7 | Γ = 51 MeV | ~ 2.6 | obs |
| η | (uū+dd̄−2ss̄)/√6 | 0⁻ | 0 | 547.9 | τ = 5.0 × 10⁻¹⁹ s | ~ 7 × 10⁴ | obs |
| η' | (uū+dd̄+ss̄)/√3 (approx) | 0⁻ | 0 | 957.8 | Γ = 0.19 MeV | ~ 22 × 10³ | obs |
| Λ | uds | 1/2⁺ | 0 | 1115.7 | τ = 2.63 × 10⁻¹⁰ s | ~ 7 × 10¹³ | obs |
| Σ⁺ | uus | 1/2⁺ | +1 | 1189.4 | τ = 8.0 × 10⁻¹¹ s | ~ 2 × 10¹³ | obs |
| Σ⁰ | uds | 1/2⁺ | 0 | 1192.6 | τ = 7.4 × 10⁻²⁰ s | ~ 24 | obs (EM decay to Λ) |
| Σ⁻ | dds | 1/2⁺ | −1 | 1197.4 | τ = 1.48 × 10⁻¹⁰ s | ~ 4 × 10¹³ | obs |
| Σ*(1385) | uus, uds, dds | 3/2⁺ | +1, 0, −1 | 1385 | Γ ≈ 36 MeV | ~ 3 | obs |
| Ξ⁰ | uss | 1/2⁺ | 0 | 1314.9 | τ = 2.9 × 10⁻¹⁰ s | ~ 9 × 10¹³ | obs |
| Ξ⁻ | dss | 1/2⁺ | −1 | 1321.7 | τ = 1.6 × 10⁻¹⁰ s | ~ 5 × 10¹³ | obs |

### 5.2 Charm (u/d - c) hadrons

| Particle | Quarks | J^P | Charge | Mass (MeV) | Lifetime / width | Cycles | Status |
|---|---|---|---|---|---|---|---|
| D⁰ | cū | 0⁻ | 0 | 1864.8 | τ = 4.1 × 10⁻¹³ s | ~ 5 × 10¹¹ | obs |
| D⁺ | cd̄ | 0⁻ | +1 | 1869.6 | τ = 1.04 × 10⁻¹² s | ~ 1.3 × 10¹² | obs |
| D*(2010)⁺ | cd̄ | 1⁻ | +1 | 2010.3 | Γ = 83 keV | ~ 1.5 × 10⁵ | obs |
| Λ_c⁺ | udc | 1/2⁺ | +1 | 2286.5 | τ = 2.0 × 10⁻¹³ s | ~ 3 × 10¹¹ | obs |
| Σ_c⁺⁺ / Σ_c⁺ / Σ_c⁰ | uuc / udc / ddc | 1/2⁺ | +2/+1/0 | ~ 2454 | Γ ≈ 1.9 MeV | ~ 1300 | obs |
| Σ_c*(2520) | uuc, udc, ddc | 3/2⁺ | +2/+1/0 | ~ 2518 | Γ ≈ 15 MeV | ~ 170 | obs |
| Ξ_c⁺ | usc | 1/2⁺ | +1 | 2467.7 | τ = 4.6 × 10⁻¹³ s | ~ 7 × 10¹¹ | obs |
| Ξ_cc⁺⁺ | ucc | 1/2⁺ | +2 | 3621.4 | τ = 2.6 × 10⁻¹³ s | ~ 6 × 10¹¹ | obs |

### 5.3 Bottom (u/d/c/s - b) hadrons

| Particle | Quarks | J^P | Charge | Mass (MeV) | Lifetime / width | Cycles | Status |
|---|---|---|---|---|---|---|---|
| B⁰ | db̄ | 0⁻ | 0 | 5279.7 | τ = 1.52 × 10⁻¹² s | ~ 5 × 10¹² | obs |
| B⁺ | ub̄ | 0⁻ | +1 | 5279.4 | τ = 1.64 × 10⁻¹² s | ~ 5 × 10¹² | obs |
| B_s⁰ | sb̄ | 0⁻ | 0 | 5366.9 | τ = 1.52 × 10⁻¹² s | ~ 5 × 10¹² | obs |
| B_c⁺ | cb̄ | 0⁻ | +1 | 6274.5 | τ = 5.1 × 10⁻¹³ s | ~ 2 × 10¹² | obs |
| B*⁰ | db̄ | 1⁻ | 0 | 5324.7 | (narrow) | — | obs |
| Λ_b⁰ | udb | 1/2⁺ | 0 | 5619.6 | τ = 1.47 × 10⁻¹² s | ~ 5 × 10¹² | obs |
| Σ_b± , Σ_b⁰ | uub / ddb / udb | 1/2⁺ | ±1 / 0 | ~ 5810 | Γ ≈ 4–10 MeV | ~ 300–700 | obs |
| Σ_b* | uub, ddb | 3/2⁺ | ±1 | ~ 5830 | Γ ≈ 9 MeV | ~ 250 | obs |
| Ξ_b | usb / dsb | 1/2⁺ | 0 / −1 | ~ 5800 | τ ~ 10⁻¹² s | ~ 4 × 10¹² | obs |

### 5.4 Exotic multiquark states

| Particle | Quarks | J^P | Status | Notes |
|---|---|---|---|---|
| X(3872) | (cc̄uū or cc̄dd̄?) tetraquark | 1⁺ | obs | controversial structure |
| Z_c(3900)± | cc̄ud̄ tetraquark | 1⁺ | obs | charged charmonium-like |
| T_cc⁺ (LHCb 2021) | ccūd̄ tetraquark | 1⁺ | obs | doubly-charmed |
| P_c(4380)⁺ | uudcc̄ pentaquark | (3/2⁻?) | obs | observed by LHCb 2015+; J^P uncertain |
| P_c(4450)⁺ | uudcc̄ pentaquark | (5/2⁺?) | obs | J^P uncertain |

Out-of-scope for both single-sheet and standard multi-sheet
treatments; would need a multi-knot framework beyond what
metric-binding currently supplies.

---

## 6. The "heavy proton/neutron analog" question

The framework's "1 sheet per quark generation" hypothesis predicts
(1/2, ±1) baryon doublets on each of the three sheets. The
prediction is empirically tested:

| Sheet | "Proton" analog | "Neutron" analog | Empirical status |
|---|---|---|---|
| ud | p (uud), 938 MeV | n (udd), 940 MeV | both observed; stable / quasi-stable |
| cs | Ω_cc⁺ (ccs), pred ~ 3700 MeV | Ω_c⁰ (ssc), 2695 MeV | "neutron" observed; "proton" predicted, search ongoing |
| tb | ttb, pred ~ 350 GeV | tbb, pred ~ 180 GeV | **neither exists** — top non-hadronisation |

### 6.1 The cs sheet — partial confirmation

The Ω_c⁰ (ssc) is the cs-sheet's "heavy neutron":
- Mass: 2695 MeV ≈ 2.87 × m_neutron
- Lifetime: 2.68 × 10⁻¹³ s — short by ordinary standards (the s and
  c quarks both decay weakly, so all three quarks contribute decay
  channels) but **~ 10¹¹ cycles** in framework terms — a clean
  closure-with-decay, not a resonance.
- Charge 0, spin 1/2, baryon number 1, strangeness −2, charm +1.

Mapped onto the framework's (1/2, ±1) baryon doublet picture, this
is the cs-sheet's neutron analog. The predicted "heavy proton" Ω_cc⁺
(ccs) at ~ 3700 MeV is the second member; LHCb has reported
candidates, full PDG-grade confirmation pending. *If the cs sheet
hosts a (1/2, 1) doublet, the masses of its two members are set by
that sheet's R_major (the cs-sheet's ring radius), and the doublet
splitting is set by its modulation amplitudes.*

The cs sheet's "heavy doublet" prediction is therefore
**substantially confirmed**, modulo experimental difficulty
finding the Ω_cc.

### 6.2 The tb sheet — empirically forbidden

No top hadron of any kind has ever been observed. The top quark's
intrinsic weak-decay lifetime,

<!-- τ_t ≈ ℏ / Γ_t ≈ ℏ / (1.4 GeV) ≈ 5 × 10⁻²⁵ s -->
$$
\tau_t \;\approx\; \frac{\hbar}{\Gamma_t}
\;\approx\; \frac{\hbar}{1.4\,\text{GeV}}
\;\approx\; 5 \times 10^{-25}\,\text{s},
$$

is *shorter* than the QCD binding timescale Λ_QCD⁻¹ ≈ 10⁻²⁴ s.
The top decays before strong forces can bind it into any composite
mode.

**Framework reading.** The tb sheet *would* support (1/2, 1) modes
in principle — the substrate's topology is the same as the ud and
cs sheets, just with a much smaller R_major (to give the high t
mass). But the (1/2, 1) mode requires ~ 1 cycle of formation time,
and the t quark's intrinsic decay rate (the equivalent of the
sheet's *external coupling* to the weak interaction) is faster
than that. The mode cannot stabilise. In framework terms: the
proton/neutron analogs on the tb sheet are *not ghosts* in the
sense of being substrate-level modes that should exist; they are
substrate-level modes whose intrinsic dissipation rate exceeds
their formation rate. They do not realise as physical states.

This is a structural prediction the framework should be ready to
accommodate: not every sheet's (1/2, 1) doublet realises in nature
— the formation-vs-dissipation balance is part of the empirical
test.

### 6.3 Predicted masses if they existed

For completeness, **if** the tb-sheet doublet were observable
(per the structural form of the construction), its masses would be
in the ~ 180–350 GeV range:

- Estimated by scaling: m_baryon ≈ (sum of constituent-quark masses)
  + (binding/cycle contribution).
- For ttb: ~ 2 × 173 + 4.2 ≈ 350 GeV.
- For tbb: ~ 173 + 2 × 4.2 ≈ 181 GeV.
- These would presumably be calculated more precisely from the
  framework's (1/2, 1) mode mass formula on a sheet with the
  appropriate R_major (much smaller than ud or cs sheets).

These values are quoted for reference, not because the framework
predicts the particles exist. The masses *would be the prediction*
if the top quark had a strong-coupling regime; nature's lack of
top hadrons is the empirical confirmation that it doesn't.

---

## 7. Framework implications

### 7.1 The closure / resonance dichotomy

A cycle-count threshold of ~ 10² cleanly separates two structurally
different particle classes:

- **Long-lived closures** (cycles ≫ 1): p, n, π, K, η, η', Λ, Σ, Ξ,
  Ω, D, D_s, B, B_s, B_c, Λ_c, Ξ_c, Λ_b, η_c, J/ψ, η_b, Υ, ... —
  full closure-satisfying modes; decay via external (weak, EM, or
  strong-but-narrow) channels.
- **Short-lived resonances** (cycles ≈ 1): Δ, ρ, Σ⁰ (EM), Σ*(1385),
  Σ_c*(2520), K*(892), N(1440), and many other N* baryon resonances —
  quasi-stationary ringing modes with complex eigenvalues,
  dissipating via strong channels.

The current chapter arc only models the first class. The second
class needs *resonance-theory machinery* added to the framework — a
real extension, not a refinement.

### 7.2 Spin–cycle correlation

A second pattern is visible in the catalog and correlates with the
first. Spin-aligned configurations cluster among the resonances;
spin-antialigned configurations cluster among the closures:

| Class | J^P | Typical cycle count |
|---|---|---|
| Octet baryons (ground-state qqq) | **1/2⁺** | 10¹¹–∞ (closures) |
| Decuplet baryons (qqq, spins aligned) | **3/2⁺** | ~ 1 (resonances), except Ω⁻ stabilised by being the lightest sss state |
| Pseudoscalar mesons (qq̄, spins anti-aligned) | **0⁻** | 10⁵–10¹⁵ (closures) |
| Scalar mesons (qq̄, internal orbital) | **0⁺** | ~ 1 (broad resonances, e.g. f₀(500)) |
| Vector mesons (qq̄, spins aligned) | **1⁻** | split: narrow ones (J/ψ, Υ, φ, ω) are closures; broad ones (ρ, K*, D*) are resonances |
| Tensor mesons (higher J) | **2⁺** | typically short-lived |

The pattern: spin-anti-aligned qq̄ and unaligned qqq tend to be
*long-lived closures*; spin-aligned configurations (3/2⁺ baryons,
many 1⁻ light mesons) tend to be *one-cycle resonances*. The
notable exceptions — Ω⁻, J/ψ, Υ — are spin-aligned states whose
strong-decay channels are blocked or suppressed by other quantum
numbers (Ω⁻ has no lighter sss state; J/ψ and Υ sit below their
respective open-charm and open-bottom thresholds).

This is consistent with the framework's working hypothesis (§1.5)
that spin emerges from winding numbers and that exotic spins
come from mode combinations: the spin-aligned configurations
correspond to higher-winding or compound modes, which are
expected to be heavier and less stable than the ground-state
spin-1/2 / spin-0 modes. The correlation is itself a *target*
the winding-combination analysis must reproduce.

### 7.3 The "1 sheet per generation" hypothesis is partially confirmed

- ud sheet: full doublet observed (proton + neutron). ✓
- cs sheet: half doublet observed (Ω_c⁰); other half (Ω_cc⁺) predicted, search ongoing. ✓ (mostly)
- tb sheet: doublet *forbidden* by top non-hadronisation. ✗ as observation; ✓ as framework prediction (if the framework can accommodate the formation-vs-dissipation balance).

### 7.4 Cross-generation hadrons dominate the observed spectrum

Of the roughly 40 well-established baryons and mesons in the
catalog above, only ~ 15 are pure single-generation (p, n, Δ, π, ρ,
ω, σ, N* on ud; Ω_c, Ω⁻, Ω_cc, D_s, J/ψ family, φ on cs; Υ family,
η_b, χ_b on tb). The remaining ~ 25+ are cross-generation. **The
single-sheet construction the sheet-proton arc develops covers
only a minority of the observed spectrum.** Multi-sheet coupling
— in metric-binding and/or ma-domain — is essential for the
framework to reach most observed hadrons.

### 7.5 Open work for the framework

Four named programs (extended from three by §7.2's spin findings):

1. **Spectrum-completeness on the ud sheet.** Enumerate the
   closure-satisfying modes the modulated-clover substrate
   supports beyond (1/2, ±1). Check whether the spectrum matches
   the observed pure-ud hadrons (π, ρ, ω, σ, p, n, Δ⁰⁺) or
   predicts unobserved modes.
2. **Winding-derived spin.** Test the working hypothesis (§1.5)
   that spin emerges from (m, n) winding numbers. Specifically:
   verify that (1/2, 1) modes give spin-1/2, find the (m, n)
   assignment that gives spin-3/2 (Δ family candidate), and work
   out how two-mode combinations yield spin-0 and spin-1 mesons.
   The J^P column in the catalog tables is the *target*.
3. **Resonance machinery.** Extend the framework to admit modes
   with complex eigenvalues (Δ, ρ, K*, etc.). Sketch how
   one-cycle ringing emerges from the substrate's wave equation.
   Likely related to (2): the spin-aligned high-J configurations
   are precisely the resonance class.
4. **Multi-sheet coupling.** Develop the cross-sheet bound-state
   mechanism in metric-binding / ma-domain. Required for ~ 60%
   of observed hadrons (anything with strange, charm, or bottom
   quarks mixed with light quarks).

The chapter arc as currently structured is honest about deferring
(2), (3), and (4); (1) is the most accessible next step and would
test the substrate's empirical correctness without requiring new
machinery. (2) is closely connected to both (1) and (3) — the
winding-derived-spin hypothesis is testable once the substrate's
full mode spectrum is enumerated, and the spin-aligned high-J
modes are likely the same objects as the resonance class.

---

## 8. Reference notes

- Particle masses, lifetimes, widths from the PDG (Particle Data
  Group, Review of Particle Physics).
- Cycle counts computed as τ_lifetime / (h / m c²); for resonances,
  Γ ≈ ℏ / τ so cycle count ≈ m c² / Γ.
- Quark content uses standard PDG notation (e.g., "uud" = one up
  and two down quarks for the proton; "cs̄" = one charm and one
  anti-strange).
- Top non-hadronisation: standard result; see Bigi & Sanda or any
  modern QCD textbook.
- "Heavy proton/neutron" terminology used here for the cs-sheet
  doublet (Ω_cc / Ω_c) is *non-standard* — these are
  conventionally called "doubly-charmed" and "charm-strange"
  baryons. The labels are used to emphasise the framework's
  (1/2, ±1) doublet structure.
