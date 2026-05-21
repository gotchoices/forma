# leakage-rate.md — the resonance-pole leakage rate, computed

**Status:** Prototype / working calculation. [mode-stability.md](mode-stability.md) is the standing *plan* — the leakage mechanism and the five-phase strategy; this file is the *calculation* that executes it. It is built smallest-first. When the calculation reproduces measured lifetimes it becomes the draft of arc **chapter E** ([../README.md](../README.md) §Derivation arc); until then it stays here in `work/`.

> **Foundational caveat (2026-05-20).** Everything from §3 onward rests on one assumption, inherited from [mode-stability.md](mode-stability.md) §2/§4: that leakage flows *only* between sheets that share a dimension. **That assumption is unverified and probably too strong.** The N-dim metric is a single object; off-diagonal shears give certain dim-pairs an *enhanced* relationship, not an *exclusive* one. Coupling without a shared dimension demonstrably exists — a charged closure mode radiates energy into macroscopic space S at rate ~α with no shared dimension and no Ma↔S shear. (mode-stability.md is itself inconsistent here: §2/§4 require a shared dim for decay, while §6's EM channel sheds energy into the photon field, which is not one.) So the leakage graph is richer than the metric-sharing graph. Consequently the §5 lepton-universality result is **contingent on this assumption and does NOT disqualify the QY-ED candidate.** §2's resonance-pole/FGR machinery and §4.1's m⁵ phase space are assumption-free and stand; §3.1–§5 are conditional and await a verified leakage law.

---

## 1. Purpose

[mode-stability.md §4](mode-stability.md) posits that a mode's decay rate is

  Γ = −2 Im(E_resonance) / ℏ

— the imaginary part of a complex pole of the connected manifold's Green's function — and that Fermi's golden rule (FGR) is the *weak-coupling limit* of that pole, not a separate axiom. Before that rate is evaluated on candidate geometry, the **machinery** has to be checked: a pole-finder and an FGR evaluator that agree on a model whose answer is already known.

This file builds the calculation in stages:

- **§2 — the machinery check** *(done)* — resonance pole vs FGR on the flat-band Friedrichs model, the minimal system where both methods apply.
- **§3 — the geometric two-sheet case** *(structure derived)* — the leakage rate factored; the shared-dim selection rule derived; the junction reduced to a figure-eight δ-vertex.
- **§4 — the lepton-lifetime test** *(contingent — see caveat)* — the phase-space factor is the Sargent m⁵; the shared-dim overlap factor surfaces an apparent lepton-universality problem.
- **§5 — family-wide universality scan** *(contingent — see caveat)* — *if* leakage is shared-dim-gated, the electron-delta topology fails universality family-wide; that premise is unverified, so this does not disqualify QY-ED.

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

So the form is derived now (§3.4–§3.5); the value is calibrated later. §4 develops the consequences.

### 3.4 The junction as a figure-eight quantum graph

The junction's form becomes concrete once the connected geometry is written out. Sheets A = `Ma(i, j)` and B = `Ma(i, k)` are the 2-tori S¹_i × S¹_j and S¹_i × S¹_k; sharing dimension i makes the S¹_i factor common, so the connected manifold is

  M = S¹_i × Y ,  with  Y = S¹_j ∨ S¹_k

— the shared circle times a **figure-eight** Y (two circles joined at one point, the junction). The two loops are the leaking sheets' *own* non-shared dimensions — circle-j and circle-k — and the crossing-point is where the two sheets meet; the figure-eight is part of the K4 compact architecture itself. It is **not** the neutrino reservoir (a separate macroscopic structure, §3.2, attached only later) and **not** a tube cross-section shape (the clover and ellipse of [tube-function.md](tube-function.md) are unrelated objects).

Because M is a product the wave operator separates: every mode is

  ψ(u_i, y) = e^{i k_i u_i} · φ(y) ,  k_i = 2π n_i / L_i ,

with φ a mode on the figure-eight and the shared-dim winding n_i a **conserved spectator**. That conservation *is* the §3.1 selection rule — now derived from the geometry rather than asserted: leakage cannot change n_i because n_i labels a product factor the junction never touches. (With twist the spectator is the helical k_θ; the structure is unchanged.)

So the two-sheet leakage problem reduces to a standard, well-studied object — a **figure-eight quantum graph coupled to a reservoir**. The reduction turned an ill-posed "two tori sharing a circle" into a concrete calculation; §3.5 takes its first step.

### 3.5 The vertex condition — the figure-eight secular equation

What vertex condition holds at the crossing-point of the figure-eight? The self-adjoint vertex conditions form a family; its natural minimal member — symmetric among the edges, reducing smoothly to the free case — is the **δ-vertex**: φ continuous at the vertex, and the summed outgoing derivative fixed by one parameter α,

  Σ φ′(V) = α · φ(V) .

With loop lengths a = L_j and b = L_k, imposing continuity and the δ-condition on φ = A cos κs + B sin κs on each loop gives the figure-eight's secular equation (for modes with φ ≠ 0 at the vertex):

  2κ [ tan(κa/2) + tan(κb/2) ] = α ,  κ = √E .

Its two limits bracket the junction physics:

- **α = 0** — standard Kirchhoff: tan(κa/2) + tan(κb/2) = 0, the two loops' modes hybridised. This is the literal reading of [mode-stability.md §8 Phase 1](mode-stability.md)'s "ψ and normal-derivative continuous."
- **α → ∞** — Dirichlet: κa/2 or κb/2 → π/2 + nπ; the spectrum becomes the *union of the two loops' independent Dirichlet spectra* — the sheets decoupled, leakage zero.

So the junction carries exactly **one parameter, α**, interpolating strong coupling (α = 0) to fully decoupled (α → ∞). This is §3.3's "form," now derived modulo the minimal-vertex choice: the form is the δ-vertex; the value is α.

Which α is physical — and so whether the observed long lifetimes are carried by the *vertex* (large α) or by the *geometric overlap* of modes spread thin on large sheets (§4.2) — is **not settled by the matching condition**; it is an output of the rate calculation. The closed figure-eight has a real spectrum (no decay, [mode-stability.md §5](mode-stability.md)); the width, and the mass-power p, appear once the reservoir is attached to this secular structure — the next step.

---

## 4. Phase 2 — the lepton-lifetime test

Built out, the ratio Γ_τ/Γ_μ is not a plug-in: it factors into a phase-space part and an overlap part, each of which must be *derived* from the geometry.

### 4.1 The phase-space factor — resolved

The rate factors as Γ = (junction coupling) × (phase space) × (overlap) ([mode-stability.md §6](mode-stability.md)). Take the phase-space factor.

What carries the decay's kinematic phase space? mode-stability.md is ambiguous: §5 names the 1D neutrino line as the reservoir — but a 1D two-body continuum scales only as ~m — while §6 attributes the m⁵ Sargent law to "phase-space integration over the byproducts." Observation settles it. Decay products are real particles propagating in macroscopic 3D space: they carry 3-momenta, recoil, the measured Michel energy spectrum. The decay is therefore the standard 3-body process in 3D, and its rate carries the **Sargent m⁵ law** — the framework inherits it because its byproducts *are* 3D-propagating particles. The neutrino line's role ([mode-stability.md §5](mode-stability.md)) is the *identity* of the Q = 0 carrier — that a charge-neutral byproduct exists — not the kinematic continuum. *(This re-reads mode-stability.md §5/§6; flagged for that file.)*

So the leptonic decay rate is ∝ m⁵. For the ratio Γ_τ/Γ_μ, a universal weak junction cancels the coupling's *value* (§3.5) and gives τ and μ a common matrix-element structure, so to leading order

  Γ_τ / Γ_μ = (m_τ / m_μ)⁵ × (geometric overlap ratio) .

The architecture's fitted masses give (m_τ/m_μ)⁵ = 1.345×10⁶; the measured leptonic partial-width ratio Γ(τ→eν̄ν)/Γ(μ→eν̄ν) = BR(τ→eν̄ν)·τ_μ/τ_τ = 1.35×10⁶. They agree to ~0.2%. So the §4 test reduces to one sharp question — **is the geometric overlap ratio ≈ 1?** If it is, the framework reproduces lepton universality and the m⁵ match becomes a genuine prediction; the overlap ratio is §4.2.

### 4.2 The geometric overlap — the naive estimate

The other factor is |O_τ|²/|O_μ|². All charged leptons are T(1, 2), so every lepton-to-lepton transition is k_θ-allowed at leading order (§3.1) — no σ-suppression — and the ratio is purely geometric.

With each lepton mode a Bloch state normalised over its sheet (|ψ|² = 1/area), the leakage matrix element on the shared dimension works out to

  O ~ 1 / √(L_a · L_b) ,  a, b = the two *non-shared* dimensions

— the shared dimension's length cancels in the integral; the overlap is set by the two non-shared dims. For the three K4 lepton transitions (Solution A: e on `Ma(m1,m2)`, μ on `Ma(m1,m3)`, τ on `Ma(m2,m3)`):

| Decay | shared dim | non-shared dims | naive O |
|---|---|---|---|
| μ → e | m1 | m3, m2 | 1 / √(L_m3·L_m2) |
| τ → e | m2 | m3, m1 | 1 / √(L_m3·L_m1) |
| τ → μ | m3 | m2, m1 | 1 / √(L_m2·L_m1) |

The μ → e overlap does *not* contain the huge u/d-spoke dimension m1 — m1 is its *shared* dim, and the shared length cancels. Both τ overlaps *do* contain m1. So O_{τ→e}/O_{μ→e} ~ √(L_m2/L_m1) and O_{τ→μ}/O_{μ→e} ~ √(L_m3/L_m1), both ≪ 1: the τ leptonic decays come out geometrically suppressed relative to μ → e. §4.3 weighs whether that survives a rigorous calculation.

### 4.3 The lepton-universality tension

The naive suppression is not a naive artefact — its *scaling* is robust. The 1/√(L_a·L_b) comes from **mode normalisation**: a closure mode spread over a region of size L has amplitude ~ 1/√L everywhere, so a *local* matrix element at the junction, between two such extended modes, unavoidably carries 1/√(L_a)·1/√(L_b). The vertex structure (§3.5) and the mode masses modulate this by O(1)–O(10²) factors; they do not change the 1/√(L) power.

And the suppression is **structural to K4**, not a feature of one assignment. The electron, the lightest lepton, must occupy the largest dimension to be light — the u/d-spoke m1 ([cand-QY-ED.md §4.1](cand-QY-ED.md): the electron needs L ≳ 2400 fm, and only the u/d spoke is that large). The τ, heaviest, must occupy the *only* m1-free sheet, `Ma(m2,m3)` — the one small enough to host a heavy mode. The two K4 solutions are the e↔μ swap on the two m1-sheets:

- **Solution A** — e on `Ma(m1,m2)`, μ on `Ma(m1,m3)`: τ→e shares m2, τ→μ shares m3.
- **Solution B** — e on `Ma(m1,m3)`, μ on `Ma(m1,m2)`: τ→e shares m3, τ→μ shares m2.

In *both*, μ→e shares m1 (it cancels — clean) and *both* τ decays carry m1 as a non-shared loop (it suppresses). The A↔B swap only exchanges which small dim each τ decay shares; the m1 suppression is identical. No K4 assignment escapes it — the τ cannot host m1 without becoming light, and these two are the only assignments consistent with the mass ordering.

Quantitatively: even at the *smallest* allowed L_m1 ≈ 3.9×10³ fm (the DOF floor), √(L_m1/L_m2) ≈ 60 — a suppression of ≳ 60 in amplitude, ≳ 3.6×10³ in rate; larger L_m1 makes it worse.

Observed lepton universality holds to < 1% — the τ and μ leptonic partial widths follow the pure Sargent m⁵, i.e. overlap ratio ≈ 1. K4's geometry gives an overlap ratio ≳ 10³ from 1. Reproducing universality would require the junction coupling g_J to be **non-universal** — larger for τ by exactly the compensating factor — which is per-transition fine-tuning, not a derivation.

**This is a serious tension, and a probable falsification of the K4 charged-lepton sector** — surfaced by the decay-rate program over-constraining the architecture, exactly the role decay rates were expected to play ([STATUS.md](STATUS.md) Phase 5). The hedge: a fully rigorous junction matrix element versus this normalisation-scaling argument. But the 1/√(L) scaling is hard to evade, and an O(1)–O(10²) vertex factor cannot close a ≳ 10³ gap.

*Superseded by §5.* §4.3 first read the suppression as K4-specific — the electron forced onto the u/d spoke — and pointed at the looser members as a possible escape. The family-wide scan (§5) shows that was wrong: share-1 and share-2 fail too. The failure is the electron-*delta* topology itself; the K4 analysis above is a correct special case of it.

### 4.4 Status and the next step

§4 is **derivation-grade** — the Phase-1 work [mode-stability.md §8](mode-stability.md) itself calls "mathematical-derivation work." The phase-space factor is resolved (§4.1, Sargent m⁵); the overlap factor (§4.2–4.3) has surfaced a probable falsification of K4's charged-lepton sector.

The overlap factor proved decisive on its own. §5's family-wide scan shows the electron-*delta* topology violates lepton universality structurally — every QY-ED member, not K4 alone. The rigorous junction matrix element (the figure-eight δ-vertex amplitudes, §3.5) would refine the O(1) factors but cannot close a 10³–10⁶ gap, so it is no longer the gating step. The next move is architecture-level — see §5.

---

## 5. Family-wide universality scan

> **Contingent — see the foundational caveat at the top of this file.** Everything below assumes leakage flows *only* through shared dimensions. That assumption is unverified, and the EM channel shows coupling without a shared dimension exists. If the leptonic decays run through a coupling that is not a shared-dim overlap — in particular a *universal baseline* coupling — the overlap structure below is the wrong model and this argument does not go through. §5 is a **conditional** result; it does **not** falsify QY-ED.

Running the overlap calculation across the whole QY-ED family — [scripts/leakage_overlap.py](../scripts/leakage_overlap.py), output [outputs/leakage_overlap.txt](../outputs/leakage_overlap.txt) — overturns §4.3's K4-specific reading: **if** leakage is shared-dim-gated, the universality failure is not K4-specific but structural to the electron-delta topology, and every QY-ED member has it.

**The structural argument.** The electron delta puts the three charged leptons on the three edges of a triangle whose nodes are three dimensions X, Y, Z. The three leptonic decays are the three edge-to-edge leakages, and by §4.2 each overlap is 1/√(product of the two non-shared dims):

  O(μ→e), O(τ→e), O(τ→μ)  ~  1/√(L_X·L_Z),  1/√(L_Y·L_Z),  1/√(L_X·L_Y)

— the three node-omitted pairwise products. Lepton universality requires the three overlaps **equal**; that holds ⟺ L_X·L_Z = L_Y·L_Z = L_X·L_Y ⟺ **L_X = L_Y = L_Z**. But three equal node dimensions make the three lepton sheets identical — three equal lepton masses. The observed masses span a factor ~3500. So the electron delta **cannot** carry the charged-lepton sector consistently with *both* the mass hierarchy and lepton universality: the hierarchy forces the nodes apart, universality needs them equal.

**The scan confirms it** — with each candidate's fitted dimension sizes:

| Candidate | overlap spread (max / min) | verdict |
|---|---:|---|
| QY-ED-share1 | 2.9×10³ | universality violated |
| QY-ED-share2 | 3.8×10⁴ | universality violated |
| QY-ED-share3 (K4) | 5.6×10⁵ | universality violated |

Universality requires spread ≈ 1; the family gives 10³–10⁶.

**Consequence.** The charged-lepton sector cannot be an electron delta. This un-supersedes [cand-QY-EL.md](cand-QY-EL.md) (the QY + electron-*path* candidate that [cand-QY-ED.md §7](cand-QY-ED.md) had set aside) and sends the electron topology back to [config-electron.md](config-electron.md). But a caution from the same overlap structure: an electron *wye* puts the three leptons on a triangle of spokes — the same equilateral requirement, the same failure; an electron *path* makes one decay (τ→e) a two-hop process, predicting τ→e ≪ τ→μ, which is also not observed. So the tension may be deeper than the delta — *any* "three leptons on three distinct sheets, decay = inter-sheet leakage" topology faces universality (equal overlaps) against the mass hierarchy (unequal sheets). Whether *any* topology resolves it is now an open architecture-level question — forced open by the decay-rate program, exactly its intended role ([STATUS.md](STATUS.md) Phase 5).

**Next.** [leakage_overlap.py](../scripts/leakage_overlap.py) is candidate-spec-driven, so scanning EL and EY is two more entries — but the structural argument already says they will not simply pass. The real question is architecture-level: whether the charged leptons should be three separate sheets at all.

---

## Cross-references

- [mode-stability.md](mode-stability.md) — the standing plan: the leakage mechanism, channel classes, the five-phase strategy this file executes
- [scripts/leakage_rate.py](../scripts/leakage_rate.py), [outputs/leakage_rate.txt](../outputs/leakage_rate.txt) — the §2 machinery check
- [cand-QY-ED.md](cand-QY-ED.md) — the K4 candidate whose fitted (L, σ_eff) the §4 test consumes
- [architecture.md](architecture.md) — the §3.4 pair-metric used to build the junction operator V_k (§3)
- [neutrino-1D.md](neutrino-1D.md) — the neutrino-line reservoir density of states for weak-channel rates (§4)
- [../README.md](../README.md) — the derivation arc; this file is the prototype of chapter E
