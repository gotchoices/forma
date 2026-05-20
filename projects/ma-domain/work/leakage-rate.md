# leakage-rate.md — the resonance-pole leakage rate, computed

**Status:** Prototype / working calculation. [mode-stability.md](mode-stability.md) is the standing *plan* — the leakage mechanism and the five-phase strategy; this file is the *calculation* that executes it. It is built smallest-first. When the calculation reproduces measured lifetimes it becomes the draft of arc **chapter E** ([../README.md](../README.md) §Derivation arc); until then it stays here in `work/`.

---

## 1. Purpose

[mode-stability.md §4](mode-stability.md) posits that a mode's decay rate is

  Γ = −2 Im(E_resonance) / ℏ

— the imaginary part of a complex pole of the connected manifold's Green's function — and that Fermi's golden rule (FGR) is the *weak-coupling limit* of that pole, not a separate axiom. Before that rate is evaluated on candidate geometry, the **machinery** has to be checked: a pole-finder and an FGR evaluator that agree on a model whose answer is already known.

This file builds the calculation in three steps:

- **§2 — the machinery check** *(done)* — resonance pole vs FGR on the flat-band Friedrichs model, the minimal system where both methods apply.
- **§3 — the geometric two-sheet case** *(structure derived)* — the leakage rate factored; the shared-dim selection rule derived; the junction strength flagged as an open modelling decision.
- **§4 — the lepton-lifetime test** *(structure derived; derivation-grade)* — Γ_τ/Γ_μ factors into a phase-space power and an overlap ratio; the power is junction-determined, so the §3.3 model feeds in here too.

---

## 2. The machinery check — resonance pole vs Fermi's golden rule

**Done.** Script [scripts/leakage_rate.py](../scripts/leakage_rate.py); output [outputs/leakage_rate.txt](../outputs/leakage_rate.txt).

**The model.** The minimal system in which both rate methods apply is the **flat-band Friedrichs model**: one discrete state |0⟩ at energy ε₀, coupled with uniform amplitude to a flat continuum band [E_lo, E_hi]. The single dimensionless coupling is γ = v²ρ (coupling amplitude squared × band density of states). It maps onto the leakage picture as: |0⟩ is the source-sheet mode, the band is the reservoir continuum ([mode-stability.md §5](mode-stability.md)), γ is the junction strength. Two *discrete* sheets with no continuum would exchange energy reversibly and never decay — a continuum is what makes the rate non-zero.

**The two methods.**

- **Method A — resonance pole.** The discrete state's Green's function is G(E) = 1 / (E − ε₀ − Σ(E)), with self-energy Σ. Its complex pole on the second Riemann sheet, E_pole, gives Γ = −2 Im(E_pole). For the flat band Σ_II(E) = γ[ln(E − E_lo) − ln(E − E_hi)] − 2πiγ; the pole is found by complex Newton iteration.
- **Method B — Fermi's golden rule.** Γ_FGR = 2πγ.

**Result.** Sweeping γ from 10⁻⁵ to 0.3, with ε₀ at the band centre:

| γ | Γ_FGR (B) | Γ_pole (A) | A / B |
|---:|---:|---:|---:|
| 10⁻⁵ | 6.2832×10⁻⁵ | 6.2833×10⁻⁵ | 1.000020 |
| 10⁻³ | 6.2832×10⁻³ | 6.2958×10⁻³ | 1.002004 |
| 10⁻² | 6.2832×10⁻² | 6.4114×10⁻² | 1.020401 |
| 0.1 | 0.62832 | 0.77644 | 1.235748 |
| 0.3 | 1.88496 | 3.07855 | 1.633222 |

The two methods **agree as γ → 0 and separate as the coupling grows**. The approach is linear: A/B = 1 + c·γ with **c = 2.0000**, stable across the low-γ rows. So FGR is the *leading term* of the rate; the resonance pole supplies the O(γ) and higher corrections. (The level shift Re(E_pole) − ε₀ is exactly zero here — a symmetry of the band-centred ε₀, not a general feature.)

**What this confirms.** Exactly the relation [mode-stability.md §4](mode-stability.md) posits: **FGR is the weak-coupling limit of the resonance pole, not a separate axiom.** The pole-finder and the FGR evaluator are mutually consistent on a model with a known answer — the machinery is sound. Candidate-specific junction operators and densities of states can now be substituted into the same machinery (§3).

---

## 3. The geometric two-sheet case

The §2 machinery carries over unchanged; only the self-energy becomes geometry-specific. For two sheets A, B sharing dimension i, the decay rate factors (per [mode-stability.md §6](mode-stability.md)) as

  Γ_{A→B} = (2π/ℏ) · |g_J|² · |O_i|² · ρ_res(E_A) ,

three factors — two derivable now, one an open modelling decision.

### 3.1 The shared-dim overlap O_i — a selection rule *(derived)*

A closure mode on sheet A = `Ma(i, j)` is a Bloch state on the (u_i, u_j) 2-torus; along the shared dimension i it carries a winding, and the conserved Bloch label is k_θ = m_r − τ·m_t — the topological charge ([metric-charge ch. 4](../metric-charge/04-the-closure-condition.md), [mode-stability.md §3](mode-stability.md)). The leakage matrix element integrates ψ_A and ψ_B over the shared circle:

  O_i ∝ ∫₀^{L_i} ψ_B*(u_i) · J(u_i) · ψ_A(u_i) du_i ,

with J the junction profile along the circle. For a uniform junction this is exact Bloch orthogonality — O_i = L_i·δ(k_θ^A, k_θ^B): **leakage through a shared dimension is allowed, at leading order, only between modes of equal k_θ along that dimension.** Since k_θ *is* the topological charge, this is charge conservation realised as a geometric selection rule.

Winding-/sector-changing transitions (Δm_t ≠ 0) are not forbidden but **suppressed by σ^|Δm_t|** — one factor of the off-diagonal shear per sector hop ([mode-stability.md §4](mode-stability.md)) — equivalently, by the Fourier content of a non-uniform junction profile at the winding mismatch. This is the "small parameters" deliverable of [mode-stability.md §8 Phase 1](mode-stability.md). It is pure Bloch-state orthogonality — no modelling choice enters.

### 3.2 The reservoir density of states ρ_res *(partially in hand)*

A decay needs a continuum ([mode-stability.md §5](mode-stability.md)) — the target sheet's own discrete spectrum is not one. For weak-channel decays the reservoir is the neutrino line: a 1D quasi-continuum of density ρ_res ≈ L_ν / (2πℏc), with L_ν the line length from [neutrino-1D.md](neutrino-1D.md). Roughly in hand; it sharpens once the neutrino line's length and topology settle (neutrino-1D §10).

### 3.3 The junction g_J *(open — and it splits in two)*

[mode-stability.md §8 Phase 1](mode-stability.md) specifies the junction "from the Laplacian's matching condition — ψ and normal derivative continuous." But two 2-tori sharing a coordinate circle form a *quantum graph of surfaces*: the admissible junction conditions are a family (as for the vertex conditions of an ordinary quantum graph), and "ψ and normal derivative continuous" is the natural — but not the unique — member.

The §4 work shows this fork separates cleanly into two questions:

- **The junction operator's form** — its structure, and hence its dimension. This sets the mass-power p of the rate (§4.1) and **cannot be deferred**: the ratio test reads p. It must be derived — by committing to a junction condition (the natural choice: ψ and normal derivative continuous).
- **The value of g_J** — its magnitude. This cancels in lifetime *ratios* and can be deferred, calibrated later from a measured lifetime as one universal channel coupling (the G_F analogue).

So the form is derived now; the value is calibrated later. §4 develops the consequences.

---

## 4. Phase 2 — the lepton-lifetime test

Built out, the ratio Γ_τ/Γ_μ is not a plug-in: it factors into a phase-space part and an overlap part, each of which must be *derived* from the geometry.

### 4.1 The phase-space power — and a correction

Write Γ = |g_J|² · F(m, geometry). The rate has dimension [energy]; the decaying-mode mass m is the energy scale, so F carries a power — Γ ∝ |g_J|² · m^p. The power p is fixed by the *dimensional structure* of the rate, and the junction coupling's dimension is decisive: β-decay's Sargent law Γ ∝ G_F²·m⁵ has p = 5 precisely because [G_F] = [energy]⁻².

This corrects the earlier framing. The ratio Γ_τ/Γ_μ cancels the *value* of g_J — but **not its dimensional structure.** The power p is junction-determined, and the ratio test reads (m_τ/m_μ)^p, so it sees p. The §3.3 junction model therefore cannot be wholly deferred: its dimensional content feeds the ratio.

If p = 5, the architecture's fitted masses give a phase-space factor (m_τ/m_μ)⁵ = 1.345×10⁶, against the measured partial-width ratio Γ(τ→eν̄ν)/Γ(μ→eν̄ν) = 1.35×10⁶ (= BR(τ→eν̄ν)·τ_μ/τ_τ) — agreement to ~0.2%, the Standard Model's lepton-universality result. But that arithmetic uses *fitted* masses and an *assumed* p = 5: it is a consistency target, not yet a test. The test is whether the geometry *yields* p = 5.

### 4.2 The geometric overlap ratio

The other factor is |O_τ|²/|O_μ|². All charged leptons are T(1, 2), so every lepton-to-lepton transition is k_θ-allowed at leading order (§3.1) — no σ-suppression — and the ratio is purely geometric. A naive O ~ L_shared fails by orders of magnitude: K4's shared dims span fifteen decades (m1 ≈ 10³–10¹⁵ fm, m2 ≈ 1 fm, m3 ≈ 0.007 fm), which no few-fold residual can absorb. The overlap needs the *normalised* Bloch wavefunctions and the junction profile worked out properly — a derivation, not a plug-in.

### 4.3 Status and the next step

§4 is **derivation-grade**, not a prototype script — the Phase-1 work [mode-stability.md §8](mode-stability.md) itself calls "mathematical-derivation work." The §2 machinery check was clean because it was a textbook model; the geometric rate is the real physics, and from here the leakage program is the arc's chapter E — derived, not scripted.

The next concrete step is the **phase-space derivation**: what power p the geometry yields, from the byproducts' propagation in macroscopic space S (the neutrino line is the energy-conservation reservoir of [mode-stability.md §5](mode-stability.md) — a distinct role, not the phase-space source). Because p is junction-determined (§4.1), this is the point at which the §3.3 junction model must be chosen.

If the eventual ratio reproduces the measurement, §1–4 promote to arc chapter E; if not, the result re-cuts the arc ([../README.md](../README.md) §Derivation arc).

---

## Cross-references

- [mode-stability.md](mode-stability.md) — the standing plan: the leakage mechanism, channel classes, the five-phase strategy this file executes
- [scripts/leakage_rate.py](../scripts/leakage_rate.py), [outputs/leakage_rate.txt](../outputs/leakage_rate.txt) — the §2 machinery check
- [cand-QY-ED.md](cand-QY-ED.md) — the K4 candidate whose fitted (L, σ_eff) the §4 test consumes
- [architecture.md](architecture.md) — the §3.4 pair-metric used to build the junction operator V_k (§3)
- [neutrino-1D.md](neutrino-1D.md) — the neutrino-line reservoir density of states for weak-channel rates (§4)
- [../README.md](../README.md) — the derivation arc; this file is the prototype of chapter E
