# Studies Registry

See [`../STATUS.md`](../STATUS.md) for project-level snapshot and model-F summary.
See [`../qa/`](../qa/) for open questions (`INBOX.md`) and detailed analyses.

**Status tags.** `Active` = currently producing findings · `Paused` = real work done, blocked or deferred · `Done` = closed (positive or negative result) · `Backlog` = not yet promoted.

Entries within each section are listed newest first (highest R-number). Each
Active entry is a 3–5-line pointer; full narrative lives in the study's own
`README.md` / `findings.md`.

---

## Active

### R63. Proton-sheet tuning — disciplined audit and sweep  **Active — Track 2 framed**
[`R63-proton-tuning/`](R63-proton-tuning/) · theoretical + compute · depends on R60, R59, R53, R49, R61, model-F
Apply the e-sheet tuning discipline to the p-sheet. **Track 1** tested two
`(ε_p, s_p)` points: baseline `(0.55, 0.162)` passes cleanly (zero
sub-observed ghosts, 7 observed matches including proton, π⁰, η′, Δ⁺, Ξ⁻,
Ξ⁰, Ω⁻); Track 21's extreme `(0.15, 0.05)` fails (sub-π⁰ ghosts at 45 and
90 MeV). Structural bound `μ(3, 6) ≤ 8.09` identified but the full viable
region remains uncharacterized. **Track 2 (framed, ready to execute)**:
sweep `(ε_p, s_p)` over a 2D grid to map the viable region and produce a
shortlist of candidate points for downstream observable-anchored tracks.

### R62. Derivations — analytical proofs  **Active**
[`R62-derivations/`](R62-derivations/) · theoretical · depends on KK primer, R59, model-E
Home for first-principles derivations, organized as programs. Program 1
(Electron from light) complete: all four electron quantum numbers + proton's
derived via generalized KK. D7d fixes spin via per-sheet Dirac–Kähler;
D11 gives g_e = 2, g_p = 6 at tree level. Further programs added on demand.

### R61. Neutrino-sheet tuning — paired-mode zoo  **Active — Tracks 1–4 complete**
[`R61-neutrino-tuning/`](R61-neutrino-tuning/) · compute + analytical · depends on R49, R26, R57, R60
Enumerates ±n_r-paired fermion triplets matching Δm² ratio 33.6. Charge-
neutrality-scored shortlist available (top candidate: ε_ν = 2.0, s_ν = 0.022,
Family A modes). Next-track pool includes comb-vs-anomalies match, small-ε
waveguide regime, and R60 handoff once the ν-sheet geometry settles.

### R60. Metric-11 — particle spectrum on R59's α-derivable 11D architecture  **Active — model-F promoted**
[`R60-metric-11/`](R60-metric-11/) · theoretical + compute · depends on R59, R53, R49, R54, R61, model-E
Can a single metric implement R59's α architecture and reproduce the model-E
spectrum? Yes — joint e+p+ν solver converges at g_aa = 1 with α universality.
Single-k symmetry k = 1.1803/(8π) holds across sheets. Z₃ confinement and
(3,6) proton drop out; 14 of 16 compound particles within 1.12% (Tracks 15–20).
Track 21 showed the residual pion gap is resolvable by proton-sheet
re-optimization (R19 legacy vacated under σ_ra). **Promoted to model-F** as
active model.

### R58. Phonon material search for neutrino frequency matching  **Active — Track 1 complete**
[`R58-phonon-material-search/`](R58-phonon-material-search/) · compute · depends on R49, L05, Q119
Systematic search for materials whose optical phonon frequencies match MaSt-
predicted ν frequencies. Sub-1% matches found for 8 of 12 targets (best: BaS
7.45 THz, DCl 13.99 THz, CaSe 7.36 THz). Candidates for L05 resonant filters.
Tracks 2–4 (deuterides, molecular vibrations, DFT validation) pending.

### R54. Compound modes on the full T⁶  **Active — Tracks 1–3 complete**
[`R54-compound-modes/`](R54-compound-modes/) · compute / theoretical · depends on R53, R50, R49
Full particle inventory on the 6D torus with individual cross entries.
18 of 20 spin-correct modes; stable particles (proton, electron) are exact
eigenmodes; 17 of 18 unstable particles within 2%. Pions 23–25% off.
Neutron as e+ν+p 6D knot at 0.07% — decay decomposes the knot.

### R53. Three generations from in-sheet shear  **Active — Tracks 1, 4 complete**
[`R53-three-generations/`](R53-three-generations/) · compute / theoretical · depends on R50, R49, R19
Tests whether e/μ/τ masses emerge from three low-order modes on the electron
sheet when s_e is freed from the α = 1/137 constraint. Tracks 5–7 pending
(ghost count, α check, extension to proton sheet). Motivated by R50 T11's
(1, 506) muon match-with-ghost-bloom.

### R52. Anomalous moment from torus self-field  **Active — framed, ready to compute**
[`R52-self-field-moment/`](R52-self-field-moment/) · compute · depends on R44, R45, R46, R47, R33
Computes Coulomb self-potential of a charged mode embedded in 3D and
perturbatively corrects μ. Sign hypothesis: single-phase (1,2) additive
(g > 2), three-phase (1,3) subtractive (μ < 3μ_N). Five tracks queued.

### R50. Filtered multi-sheet mode search  **Active — Track 8 complete**
[`R50-filtered-particle-search/`](R50-filtered-particle-search/) · compute · depends on R29, R46, R47, R49
Joint 6D search on coupled three-sheet metric. Track 8: 16 of 20 particles
viable, 9 excellent, tau at 0.656% on ν+p mode. **Muon not viable** (97.98%
off — structural mass desert); π±/K± topologically forbidden as single
6-tuples. Motivates a compound back-reaction engine as follow-up.

### R47. Proton geometry — mode, slots, and anomalous moment  **Active — Track 7**
[`R47-proton-filter/`](R47-proton-filter/) · compute / interactive · depends on R46
(3,6) proton wins 8 of 11 criteria vs (1,2): SU(6) moments μ_p = 3.000 μ_N,
μ_n = −2.000 μ_N, constituent mass 313 MeV, geometric confinement all follow
from the mode topology. Accepted into model-F as the canonical proton.
Key surprise: WvM charge integral exactly zero for n₁ = 3.

### R46. Electron filter — aperture effects on a toroidal cavity  **Active — Track 3 primary**
[`R46-electron-filter/`](R46-electron-filter/) · compute / grid simulation · depends on R44, R33, R40
Track 1 (geodesic tilting): negative — moment on a static flat torus is a
topological invariant (L = ℏn). Track 3 (self-consistent dressed particles)
remains the primary path: dressed proton as (3,6) plus cross-sheet
excitations with independent winding numbers.

### R30. Minimal material geometry — is a material sheet necessary?  **Active**
[`R30-minimal-geometry/`](R30-minimal-geometry/) · theoretical + compute · depends on R19, R26, R27
Persistent r-degeneracy and 20× ghost over-prediction suggest over-
parameterization. Tests whether a circle (not an area) can reproduce particle
properties. Five tracks: circle sheet, irreducibly 2D charge, Klein bottle
identification, hierarchical compactification, non-uniform circle.

### R15. Forward charge calculation — deriving α  **Active**
[`R15-forward-charge/`](R15-forward-charge/) · compute · depends on R7, R13
Runs R7's calculation forward: input m_e c² and (1,2) topology, compute
far-field Coulomb flux, read off Q, check Q²/(4πε₀ℏc) ≈ 1/137. Open
sub-problem: α(r,s) is a one-parameter family — nothing pins r. R44 closed
the g − 2 route; candidate routes are Casimir/vacuum, τ-mass, energy partition.

---

## Paused / On hold

### R55. α consistency — Ma-S coupling derivation  **Paused — Tracks 1, 3 done**
[`R55-alpha-consistency/`](R55-alpha-consistency/) · theoretical + compute · depends on R54, R19, R48, GRID
Track 1 (direct Schur): 30%+ α spread on e-sheet. Track 3 (ℵ-mediated
10×10): 3.6% e-p gap, 0.4% spectrum shift. Track 4 (self-consistent
re-derivation) paused.

### R51. Hydrogen as compound torus mode  **Paused — all bilinear pathways closed**
[`R51-hydrogen-mode/`](R51-hydrogen-mode/) · compute / theoretical · depends on R29, R50
Tracks 1, 1a, 1b, 1c all fail: σ_ep, σ_eν, and multi-mode metric pathways
cannot produce 13.6 eV at the right scale. Two-tier physics (R29) appears
structurally necessary. Paused pending a non-bilinear mechanism.

### R49. Neutrino sheet — filtering, oscillation, mode spectrum  **Paused — Tracks 1–2a done**
[`R49-neutrino-filter/`](R49-neutrino-filter/) · compute / theoretical · depends on R24, R25, R26, R46, R47
ε broadly viable (0.1–5+); 3 solution families; waveguide cutoff sets floor
but doesn't uniquely select 3 modes. Q105 implies Majorana via C-conjugate
mixing; predicts 0νββ at |m_ββ| ≈ 10–30 meV. Remaining tracks (2–6) on hold
pending weak-coupling model.

### R45. Magnetic moments from cross-sheet coupling  **Paused**
[`R45-magnetic-moments/`](R45-magnetic-moments/) · compute · depends on R19, R27, R28, R33, R44
Framed, awaiting R44 follow-up and cross-sheet coupling framework.

### R33. Ghost mode selection — why most Ma modes are dark  **Paused — Tracks 2 done, 5 deferred**
[`R33-ghost-selection/`](R33-ghost-selection/) · compute + theoretical · depends on R19, R27, R28, R31, R32
n₁ = ±1 rule (F1) kills 88%; spin-statistics (F3) kills most of the rest.
Residual (1,1) boson at ½ m_e remains the critical tension — wave-optics
ω⁴ suppression gives ~1/16× radiation but is model-dependent. Track 6
(spin derivation) could reshape the landscape; Tracks 2–5 cleanup.

---

## Backlog

Candidate studies, roughly in priority order. Assign R-numbers when promoted.

### B1. KK gauge coupling on the sheared torus — resolve Yukawa tension  *(R29 F11–F13)*
Compute overlap integral of electron mode profile with each KK gauge mode on
the sheared Ma_e metric, sum the series, compare to hydrogen spectroscopy.
r_e that matches spectroscopy pins it independent of g − 2.

### B2. W-barrier height from mode reconfiguration dynamics  *(R43 F7, Q96)*
Variational path from neutron (1,2,0,0,1,2) to proton + electron + neutrino;
saddle energy should equal M_W = 80.4 GeV.

### B3. Flat-space → curved appearance  *(Q2)*
Explicit field projection from flat Ma into 3+1D. R12 F14 revised picture;
computation is R13 Track 3.

### B4. Quadrupole correction  *(Q10, after R6)*
~2.5% (1,2) field anisotropy at the rotation horizon; shifts q/e by ~few %.

### B5. Precession of torus axis  *(Q19)*
What drives axis precession, does it restore approximate spherical symmetry?

### B6. Orbit precession and volume-filling  *(Q23)*
Does a precessing (1,2) orbit reproduce WvM's Fig. 2 volume-filling pattern?

### B7. Photon absorption and excited electrons  *(Q28)*
Material-dimension picture of absorption: higher harmonic, reshaped geometry,
or discrete allowed increments reproducing atomic spectra.

### B8. String-theory parallels  *(Q24, Q25)*
MaSt vs torus-compactified string theory: modular invariance, T-duality.

---

## Done

Newest first. Key result only — see each study's `findings.md` for the record.

| # | Study | Key result |
|---|-------|------------|
| 59 | **R59. Self-consistent metric with time** [`R59-clifford-torus/`](R59-clifford-torus/) | Tube↔ℵ↔t on clean Ma gives exact α structural universality + magnitude at k = 1/(8π), within 60 ppm (F59). Ten tracks; foundation for R60/model-F. |
| 58 | **R57. Energy routing between Ma and S** [`R57-energy-routing/`](R57-energy-routing/) | Generalized routing engine: Ma pathway (dark modes) vs S pathway (Coulomb barrier). Theoretical mechanism for LENR via ν-sheet dark mode accumulation. |
| 57 | **R56. Electron shell structure** [`R56-electron-shells/`](R56-electron-shells/) | Shell capacities 2n² reproduced from mode capacity n² × tube-winding factor 2. Ghost suppression follows from the same routing. Classical packing failed; mode capacity succeeded. |
| 56 | **R48. Helicity and charge — Q104** [`R48-helicity-charge/`](R48-helicity-charge/) | Negative. Naive CP flux integral gives Q = 0 for all (n₁, n₂ ≠ 0). Helicity does not select (1,2) over (1,1); ghost elimination needs a different mechanism. |
| 55 | **R44. Anomalous magnetic moment from torus geometry** [`R44-g-minus-2/`](R44-g-minus-2/) | Negative. Charge density is oscillating cos() pattern; μ correction is order −1.6 to −2.4 (wrong sign, ~1400× too large). Charge-mass shear separation ruled out as g − 2 mechanism. |
| 54 | **R43. Weinberg angle** [`R43-weinberg-angle/`](R43-weinberg-angle/) | sin²θ_W matches 3/13 to −0.19%; 2/9 predicts M_W = 80.420 GeV (+0.051%). 3/13 not derivable from Ma trace — numerical match, not derivation. W/Z are transient reconfigurations. |
| 53 | **R42. Dark matter from ghost modes** [`R42-dark-matter/`](R42-dark-matter/) | Ghost modes exactly charge-symmetric. DM/visible mass ratio spans 2.4–12.4; Planck 5.36 lands in the middle. Viable; next step is projection integral W(n). |
| 52 | **R41. Dynamic model (full)** [`R41-dynamic-model/`](R41-dynamic-model/) | Refactored `lib/ma_model.py`. Conceptual advance (elliptical cross-section, 92% mode elimination) but corrections 100× smaller than structural errors. 125 unit tests pass. |
| 51 | **R40. Dynamic torus** [`R40-dynamic-torus/`](R40-dynamic-torus/) | GR bulk stiffness gives 10⁻⁴⁰ deformation. α-impedance model: wall is (1−α) contour; elastic 1/k² response gives 40× suppression per n₁ step. Dynamic Ma is perturbative (∝ α²). |
| 50 | **R39. Near-field phase** [`R39-near-field-phase/`](R39-near-field-phase/) | Proton's extended charge reduces Coulomb barrier by 74% at 1 fm; phase modulation +3–14%. Anti-phase cancellation falsified for (1,2). Nuclear binding requires non-EM mechanism. |
| 49 | **R38. Fourth generation** [`R38-fourth-generation/`](R38-fourth-generation/) | MaSt accommodates, doesn't predict, exactly three generations. Resonance capture (Q ≈ 30 excludes 4th gen) viable but underdetermined. |
| 48 | **R37. Membrane mechanics** [`R37-membrane-mechanics/`](R37-membrane-mechanics/) | Constrained energy minimization gives r ≈ 0.50 — first mechanism preferring a specific r region; rules out thin-torus (r = 6.6 is 91% worse). Gravity "derivation" tautological. |
| 47 | **R36. Geometric tilt** [`R36-geometric-tilt/`](R36-geometric-tilt/) | Drops KK. Ma_e plane tilted vs S by angle θ; α = f(θ). EM emerges from S-projection of material-dimension momentum. α may be a free "designer" parameter. |
| 46 | **R35. Threshold detection** [`R35-threshold-coupling/`](R35-threshold-coupling/) | Threshold "continuity" is mode-hopping on ν-sheet's dense ladder. Cd-109 Re/Rc = 33 reproduced via SCA. Storage 10–324 bits/cell; writing requires metabolic energy. |
| 45 | **R34. Midpoint coupling** [`R34-midpoint-coupling/`](R34-midpoint-coupling/) | Weighted gauge partition gives 1/80 = (137+24)/2 to 99.8%. Ma modes as absorption resonances modulate α upward (IR → 137) and downward (UV → 24). |
| 44 | **R32. Running of α** [`R32-alpha-running/`](R32-alpha-running/) | Naive KK running catastrophic (157,000× SM), confirming ~10⁵ ghost suppression. Volume dilution gives α_bare ≈ 1/5. "Why α = 1/137?" → "why s ≈ 0.01?" |
| 43 | **R31. Origin of α** [`R31-alpha-derivation/`](R31-alpha-derivation/) | Hydrogen not a Ma mode (spectrum 2,830× too coarse). Casimir cannot select α. Naive KK Yukawa 10³–10⁶× too large. α remains input; moduli potential needed. |
| 42 | **R29. Atoms and nuclei** [`R29-atoms-and-nuclei/`](R29-atoms-and-nuclei/) | Coulomb derived from Ma × S (α = 1/137, H E₁ = −13.6 eV). Nuclei ARE Ma modes: n₅ = A, n₆ = 2A matches d→⁵⁶Fe to < 1%. Deuteron 0.02%. Two-tier physics: Ma (MeV) / S (eV). |
| 41 | **R28. Ma spectrum refinement** [`R28-particle-spectrum/`](R28-particle-spectrum/) | ~48 bands below 2 GeV, ~900 modes vs ~40 particles — consistent with off-resonance hypothesis. Strange-baryon sign flips resolved at n_max = 15. Predictive horizon ~2 GeV. |
| 40 | **R27. Ma oscillation patterns** [`R27-bound-states/`](R27-bound-states/) | Discovery engine finds Ma modes matching particles. Neutron and muon pin r_p = 8.906, σ_ep = −0.0906 — zero free parameters at MeV. Parameter-free predictions: K (1.2%), η (0.6%), η′ (0.3%), φ (0.8%). |
| 39 | **R26. Three tori — Ma** [`R26-neutrino-t4/`](R26-neutrino-t4/) | Ma = three material sheets (e, ν, p). ν mass ratio 33.6 from shear s₃₄ = 0.022 (exact). Charge-neutral neutron mode reproduces m_n at σ_ep = −0.091. Parameter census: 21 total, 15 free. |
| 38 | **R25. Neutrino spin** [`R25-neutrino-spin/`](R25-neutrino-spin/) | Charge-spin linkage: both controlled by n₁. "Uncharged" and "fermion" mutually exclusive — WvM cannot produce neutrinos. 3-torus R24 T1 blocked at spin gate. |
| 37 | **R24. Torus dynamics** [`R24-torus-dynamics/`](R24-torus-dynamics/) | 3-torus neutrinos: (0,0,n₃) uncharged; mass ratio 33.63 from integers alone (0.03σ); Σm = 72 meV. Wave dynamics does not select modes. Critical open: spin of (0,0,n₃) → R25. |
| 36 | **R23. Neutrino from harmonic beating** [`R23-neutrino-beating/`](R23-neutrino-beating/) | Δm² ratio 33.6 not selective. θ₂-momentum conservation blocks phonon mechanism. Single-sheet neutrino ruled out. |
| 35 | **R22. Mode coupling** [`R22-mode-coupling/`](R22-mode-coupling/) | Curvature makes harmonics heavier; proton mass decreases slightly. Correction monotonic in r — does not select r. θ₂ symmetry preserved by backreaction — phonon neutrino ruled out. |
| 34 | **R21. Quarks from embedding curvature** [`R21-embedding-quarks/`](R21-embedding-quarks/) | Curvature concentrates modes, lifts ±n₁ degeneracy. Charge ratios continuous, not quantized — single-torus quarks insufficient. Parity rule: cos-like electron is unique charged mode. |
| 33 | **R20. Harmonic proton** [`R20-harmonic-proton/`](R20-harmonic-proton/) | Proton/neutron as fundamental + uncharged harmonics. Harmonics exactly uncharged; decay energetics match; stability explained; μ/τ as "hot electrons"; ν excluded from e-sheet. |
| 32 | **R19. Shear-induced charge** [`R19-shear-charge/`](R19-shear-charge/) | First mechanism producing charge from delocalized wave. α(r, s) formula derived. Quark program ruled out (F24, F33). Track 8: KK reconciliation — α formula re-derived under KK Compton constraint. |
| 31 | **R18. Torus stiffness** [`R18-torus-stiffness/`](R18-torus-stiffness/) | Geometric deformation cannot produce charge. Backwards stiffness α-independent at linear order; Coulomb cost exceeds photon saving by 96×. Charge integral of cos(θ + 2φ) vanishes on any smooth torus. |
| 30 | **R17. Radiation pressure** [`R17-radiation-pressure/`](R17-radiation-pressure/) | Centrifugal force from confined photon cannot determine α. F ⊥ v (no clumping); σ_φ const (breathing conservative). Positive: force decomposition quantified. |
| 29 | **R16. Harmonic charge** [`R16-harmonic-charge/`](R16-harmonic-charge/) | Paused indefinitely. R18 showed axisymmetric curvature cannot mix modes into charge. Superseded by R19. |
| 28 | **R14. Universal geometry** [`R14-universal-geometry/`](R14-universal-geometry/) | Three-photon linking model for hadrons ruled out. Charge depends on mode numbers, not spatial arrangement. Spin quantization protects electron; uncharged modes can add mass. |
| 27 | **R13. Charge from the embedding** [`R13-kk-charge-t3/`](R13-kk-charge-t3/) | Electron is winding mode (not KK). Multi-winding (68,137) breaks WvM charge: monopole = 0 exactly. α ≡ tradeoff between correct Coulomb energy and correct charge. → Q34. |
| 26 | **R12. Self-consistent fields** [`R12-self-consistent-fields/`](R12-self-consistent-fields/) | Flat Ma_e has no eigenmodes at ω_C (gap ~137×). Curved geodesics give q ≈ 193 — photon sees flat space internally. Flat-for-mass / embedded-for-charge is correct two-domain picture. |
| 25 | **R11. Prime resonance** [`R11-prime-resonance/`](R11-prime-resonance/) | No mechanism selects q = 137 from energy cost or primality. q ~ 1/α is partly tautological. Real free parameter is r (aspect ratio), not q. |
| 24 | **R8. Multi-winding electron** [`R8-multi-winding/`](R8-multi-winding/) | (68,137) on sheared Ma_e: mass ✓, spin ½ ✓, g = 2 ✓. **Charge mechanism invalidated by R13.** Spin/g carry over to any (1,2)-local model. |
| 23 | **R7. Charge from torus geometry** [`R7-torus-capacitance/`](R7-torus-capacitance/) | Coulomb field energy ~α × target for all aspect ratios at Compton scale. WvM energy balance overestimates by ~1/α. "Magic ratios" were artifacts. |
| 22 | **R6. Guided-wave field profile** [`R6-field-profile/`](R6-field-profile/) | S2's r = 6.60 not self-consistent. Self-consistent: r ≈ 4.29, R ≈ 8.2 × 10⁻¹⁴ m. All profile shapes give q = e; actual profile requires solving the wave equation on Ma_e. |
| 21 | **R2. Electron from geometry** [`R2-electron-compact/`](R2-electron-compact/) | Photon of energy m_e c² on (1,2) geodesic on Ma_e gives q = e, s = ½, g ≈ 2.0023 with zero free continuous parameters. Framework sound. |
| 20 | **R1. KK charge comparison** [`R1-kk-charge/`](R1-kk-charge/) | KK gravitational charge ~10⁻²² × e at Compton scale — ruled out. WvM mechanism structurally different. 6D decomposition documented. |
| 19 | **S3. Knot zoo** [`S3-knot-zoo/`](S3-knot-zoo/) | Only (1,2) produces nonzero charge. Fractional charges (e/3, 2e/3) map to a/R multiples. Material-dimension hypothesis proposed. |
| 18 | **S2. Toroid geometry** [`S2-toroid-geometry/`](S2-toroid-geometry/) | a/R = 1/√(πα) ≈ 6.60 gives q = e in WvM's formula. Key algebraic result — not self-consistent (see R6). |
| 17 | **S1. Toroid series** [`S1-toroid-series/`](S1-toroid-series/) | Null. 9% charge deficit is an artifact of geometric approximations, not a real target. |

**Retired numbers:** R3 (visualizer, now [`viz/dual-torus.html`](../viz/dual-torus.html));
R4 (subsumed by R2); R5 (subsumed by R13); R9, R10 (never started — live in Backlog B6, B7).
