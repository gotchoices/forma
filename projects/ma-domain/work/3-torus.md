# 3-torus.md — Three generations from three compact dimensions

**Status:** Two-test investigation of the hypothesis that each particle sheet is a *3-torus* (three compact dimensions with dramatically different circumferences L₁ ≪ L₂ ≪ L₃) rather than a 2-torus, with the three Standard Model generations corresponding to modes living in the three coordinate planes (12, 13, 23).

**Why this is worth testing.** Phase 3 / Phase 4 of the corrugated-clover work ([sheet-proton 3-gen.md §12–§13](../../sheet-proton/work/3-gen.md)) ruled out the multi-generation mass hierarchy from a 2D-surface picture, both with the bisect-and-insert fractal recursion ([sheet-proton clover-on-clover.md](../../sheet-proton/work/clover-on-clover.md)) and with the alternative three-radius cross-section ([sheet-proton clover-inverse.md](../../sheet-proton/work/clover-inverse.md)). The 3D wave-guide extension recovers the hierarchy qualitatively but with no quantitative discriminator. This file tests a structurally different reframing: instead of fitting hierarchy by extreme ε or fractal nesting on a 2D sheet, let *each sheet itself* be 3D and let the three coordinate planes carry the three generations directly.

---

## 1. The hypothesis

A particle sheet has three compact dimensions with circumferences (L₁, L₂, L₃) where L₁ ≪ L₂ ≪ L₃. A mode established between two of these dimensions has:

- **Smaller dim = charge generator** (analog of MaSt 2D's "tube" — the small circumference carries the winding that integrates to non-zero EM monopole charge per [R19](../../../studies/R19-charge-from-shear)).
- **Larger dim = mass generator** (analog of "ring" — the larger circumference sets the energy scale of the mode).
- **Third dim plays no role** for that mode (winding number = 0 along the spectator dimension).

The three pairwise combinations give three generations:

| Generation | Active pair | Smaller (charge) | Larger (mass) | Mass scale |
|---|---|---|---|---|
| heaviest | (L₁, L₂) | L₁ | L₂ | tied to 1/L_min-of-pair |
| middle | (L₁, L₃) | L₁ | L₃ | tied to 1/L_min-of-pair |
| lightest | (L₂, L₃) | L₂ | L₃ | tied to 1/L_min-of-pair |

The cyclic Z₃ permutation (1 → 2 → 3 → 1) of dimensions naturally enumerates the three pairs.

**Mass-hierarchy reach.** For m_t/m_u ≈ 78,000 and m_c/m_u ≈ 580 (current-quark masses):

- L₃/L₁ ≈ 78,000 (heaviest-vs-lightest ratio of the smallest in each generation's pair)
- L₂/L₁ ≈ 580

This redistributes the magnitude problem from a single ε ~ 78,000 (R53 e-sheet extreme) across three lengths spanning roughly 1 : 580 : 78,000 — extreme but no more so than what is already attested.

---

## 2. The two structural questions

If the bare 3-torus Laplacian is just sorted by eigenvalue, what kinds of modes dominate the low-energy spectrum?

- **1D-line modes** (only one n ≠ 0): pure excitations of a single compact direction. Lowest is (0, 0, ±1) at ω = 2π/L₃, then (0, 0, ±2) at 4π/L₃, etc. — a *dense* tower below the first 2D mode.
- **2D-planar modes** (two n ≠ 0): the hypothesized "three generations" class. Lowest is (0, ±1, ±1) at ω = 2π·√(1/L₂² + 1/L₃²) ≈ 2π/L₂.
- **3D-mixed modes** (all three n ≠ 0): cross-plane excitations. Lowest is (±1, ±1, ±1) at ω = 2π·√(1/L₁² + 1/L₂² + 1/L₃²) ≈ 2π/L₁.

For L₁ ≪ L₂ ≪ L₃, the bare ordering is:

1. **1D modes along L₃** are dense at the bottom.
2. **2D-planar modes** (the generation candidates) sit at significantly higher energy.
3. **3D-mixed modes** are even higher.

This is *bad* for the hypothesis: if all mode classes show up as physical particles, the low-energy spectrum is dominated by an infinite tower of 1D modes (~L₃/L₂ of them before the first 2D mode), which we don't observe.

**The hypothesis only works if 1D-line modes are systematically dark** — predicted but not coupled to the ambient EM. The 2D analog (R19) says EM monopole charge requires *tube winding*. The 3D extension would say: **EM monopole charge requires winding in at least two of the three dimensions**, with 1D-line modes naturally dark for the same reason that uncharged 2D modes are dark.

The hypothesis stands or falls on this selection rule.

---

## 3. The two tests

### 3.1 Test A — Spectrum classification

Build the eigenvalue spectrum of the bare 3-torus Laplacian at L₁:L₂:L₃ = 1:580:78,000 (the natural-quark-mass-ratio operating point) and at a few cleaner intermediate ratios. Sort modes by energy. Classify each as 1D-line, 2D-planar, or 3D-mixed. Confirm the qualitative expectation that the low-energy ladder is dense in 1D modes, sparse in 2D, very sparse in 3D.

The expected outcome (from §2's bare-Laplacian analysis):

- The lowest ~(L₃/L₂) modes are 1D-line modes along L₃.
- The lowest 2D-planar mode lives in the (L₂, L₃)-plane at ω ≈ 2π/L₂.
- The lowest 3D-mixed mode lives at ω ≈ 2π/L₁.

If the spectrum confirms this layout, Test A passes its sanity check. The picture's viability then rests entirely on Test B.

### 3.2 Test B — Per-tube-cycle EM-coupling integral (R19 in 3D)

R19's 2D argument: integrate the EM potential's spatial component around one tube cycle. The result is proportional to the tube winding n_t — non-zero iff the mode winds the tube direction.

The 3D analog has three natural extensions. The script computes all three and reports which kills 1D modes:

**Candidate I — Per-direction 1-cycle integral.** Integrate the gradient component around the cycle in each direction:

<!-- Q_i = (1/L_i) ∮_{L_i-cycle} ∂_i ψ du_i ∝ n_i -->
$$
Q_i \;=\; \frac{1}{L_i} \oint_{L_i\text{-cycle}} (\partial_i \psi) \, du_i \;\propto\; n_i
$$

This picks out each winding number individually. **Does not kill 1D modes** — gives them one non-zero charge each.

**Candidate II — Per-plane 2-cycle flux integral.** For each coordinate 2-plane (ij), integrate the (perpendicular component of the) gradient through the 2-cycle:

<!-- Φ_{ij} = ∫∫_{L_i×L_j} (∂_k ψ) du_i du_j -->
$$
\Phi_{ij} \;=\; \int\!\!\!\int_{L_i \times L_j} (\partial_k \psi) \, du_i \, du_j
$$

(with k the index not in {i, j}). For ψ a plane wave, the only nonzero result comes from n_i = n_j = 0, leaving only n_k ≠ 0. So Φ_{ij} ≠ 0 precisely when the mode is 1D-line along k.

This is the *opposite* of what we want — it kills 2D modes and selects 1D modes.

**Candidate III — Per-plane curl-coupling integral.** The integrand that natively couples to a 2D EM observation is the curl-like quantity. For a mode pattern ψ on the 3-torus, the per-plane "circulation" of the gradient is

<!-- C_{ij} = ∮_{∂(L_i×L_j-cell)} (∂_i ψ) du_j − (∂_j ψ) du_i -->
$$
C_{ij} \;=\; \oint_{\partial(L_i \times L_j)\text{-cell}} \bigl[ (\partial_i \psi) du_j \;-\; (\partial_j \psi) du_i \bigr]
$$

For a plane-wave ψ = exp(i 2π (n_1 u_1/L_1 + n_2 u_2/L_2 + n_3 u_3/L_3)) on a unit cell of the (i, j)-plane, this gives a winding-product-like quantity ∝ n_i · n_j: non-zero iff *both* n_i and n_j are non-zero, killing 1D-line modes and surviving for 2D-planar and 3D-mixed.

Candidate III is the candidate that *implements* the hypothesis's selection rule. The script reports all three to make the comparison explicit.

### 3.3 Verdict criterion

The picture survives if and only if **Candidate III (or some equivalent integral) is the physically correct R19 extension** — i.e., the right EM coupling rule on a 3-torus has the form "winding in at least two dimensions." The script does not derive which candidate is physical; it only confirms whether each candidate has the structural property the hypothesis needs.

If Candidate I (per-direction 1-cycle, the *direct* 2D-analog) is the right one, the picture is dead — 1D modes carry charge too, the spectrum's 1D tower is an unobserved ghost flood, and the three-coordinate-pairs idea fails the same way model-D's (1,1) ghost did.

---

## 4. Implementation

Script: [scripts/torus3d_modes.py](../scripts/torus3d_modes.py). Standalone — no dependencies on `lib/geometry.py` (which is clover-profile-specific). Builds the mode spectrum, classifies, and evaluates all three EM-coupling-integral candidates analytically (closed-form on plane waves — no quadrature needed).

CLI:

    python scripts/torus3d_modes.py [--L1 L1] [--L2 L2] [--L3 L3]
                                     [--n-max N] [--n-report N_REPORT]
                                     [--ratios "label:l1:l2:l3,..."]

Outputs to `outputs/`:

- `torus3d_spectrum_L<L1>_<L2>_<L3>.csv` — sorted mode spectrum with class and three coupling values.
- `torus3d_spectrum_summary.csv` — across-ratios summary (class counts in the lowest N_REPORT modes, lowest 2D vs lowest 1D ratio).
- `torus3d_coupling_report.txt` — coupling-integral verdict on representative 1D/2D/3D modes.

---

## 5. Results

### 5.1 Test A — spectrum classification

Script run with default L = (1, 580, 78,000) and n-max = 4 (enumerates 728 modes; |n_i| ≤ 4 per direction).

**Class leaders (lowest energy of each class):**

| Class | Lowest mode | ω | ω-ratio to lowest 1D | Prediction from §2 |
|---|---|---:|---:|---|
| 1D-line | (0, 0, ±1) | 8.0554 × 10⁻⁵ | 1 (reference) | along L₃, ω = 2π/L₃ ≈ 8.06 × 10⁻⁵ ✓ |
| 2D-planar | (0, ±1, ±1) in (23)-plane | 0.01083 | **134.5** | should be L₃/L₂ = 134.48 ✓ |
| 3D-mixed | (±1, ±1, ±1) | 6.283 | **78,000** | should be L₃/L₁ = 78,000 ✓ |

The ω-ratios *exactly* match the predicted L₃/L₂ and L₃/L₁ to 4 significant digits — confirming that the bare-Laplacian analysis of §2 holds and the script is correct.

**Class counts in the lowest 30 modes:**

| Ratio label | (L₁, L₂, L₃) | count 1D | count 2D | count 3D | ω(2D_low)/ω(1D_low) | ω(3D_low)/ω(1D_low) |
|---|---|---:|---:|---:|---:|---:|
| **natural-quark** | (1, 580, 78,000) | 12 | 18 | 0 | 134.5 | 78,000 |
| uniform | (1, 1, 1) | 10 | 12 | 8 | 1.414 | 1.732 |
| mild | (1, 10, 100) | 12 | 18 | 0 | 10.05 | 100.5 |
| moderate | (1, 20, 400) | 12 | 18 | 0 | 20.03 | 400.5 |
| gen-2-only | (1, 580, 5,800) | 12 | 18 | 0 | 10.05 | 5,800 |

At any non-uniform ratio, the lowest 30 modes contain *no* 3D-mixed modes — those sit at ω ≈ 2π/L₁, way above the lowest 2D modes at ω ≈ 2π/L₂. The 1D-line tower is *dense* below the first 2D mode: the script's n-max = 4 cap only captures the lowest 4 1D modes per direction (12 total), but the *true* count of 1D-line modes between ω = 0 and the first 2D mode is roughly L₃/L₂ ≈ 134 (every (0, 0, n₃) mode with |n₃| < 134 lies below the first (0, ±1, ±1) 2D mode at the natural-quark ratio).

So **at the natural-quark ratio, the bare spectrum has ~134 1D-line modes below the lightest 2D-planar mode** (the gen-1 candidate). Without a selection rule, every one of these is a predicted observable particle — a dramatic ghost flood compared to the observed inventory's 12-ish fundamental fermions.

The uniform-L case (L₁ = L₂ = L₃ = 1) is the only one in the table where all three classes appear together at comparable energies — the symmetry-broken hypothesis is the price of admission to the picture; symmetric L's give no hierarchy.

**Conclusion of Test A.** The 2D-planar mode tower exists and forms a separable class above the 1D tower, with the predicted L₃/L₂ separation. But the 1D tower below it is dense (~L₃/L₂ modes per (n₃, 0, 0) ladder), so the picture *cannot* survive without a selection rule that darkens the 1D class.

### 5.2 Test B — EM-coupling integrals

Three candidate per-mode EM-coupling magnitudes were computed analytically on plane waves; full per-class evaluations are in [`outputs/torus3d_coupling_report.txt`](../outputs/torus3d_coupling_report.txt). Summary at the natural-quark ratio (L = 1, 580, 78,000):

| Representative mode | Class | ΣQ_I (Cand I) | ΣΦ_II (Cand II) | ΣC_III (Cand III) |
|---|---|---:|---:|---:|
| (0, 0, 1) — 1D along L₃ | 1D-line | 1.64 × 10⁻¹⁰ | 5.53 × 10⁻⁵ | **0** |
| (0, 1, 0) — 1D along L₂ | 1D-line | 2.97 × 10⁻⁶ | 1.81 × 10⁴ | **0** |
| (1, 0, 0) — 1D along L₁ | 1D-line | 1.00 | 2.05 × 10¹⁵ | **0** |
| (0, 1, 1) — 2D in (23) | 2D-planar | 2.97 × 10⁻⁶ | **0** | 4.89 × 10⁻¹⁶ |
| (1, 0, 1) — 2D in (13) | 2D-planar | 1.00 | **0** | 1.64 × 10⁻¹⁰ |
| (1, 1, 0) — 2D in (12) | 2D-planar | 1.00 | **0** | 2.97 × 10⁻⁶ |
| (1, 1, 1) — 3D-mixed | 3D-mixed | 1.00 | **0** | 2.97 × 10⁻⁶ |

Reading down each candidate column:

- **Candidate I (per-direction 1-cycle).** Every mode with any nonzero winding has nonzero ΣQ_I — including all 1D-line modes. **Does not dark out 1D.** If this is the physical R19 extension, the picture is killed by 1D ghost flood.
- **Candidate II (per-plane perpendicular flux).** Nonzero *only* for 1D-line modes (specifically, the integral selects the direction perpendicular to a coordinate plane). **Inverts the desired structure** — 2D and 3D modes are dark, 1D modes shine. Also kills the hypothesis (the "three generations" would be the dark ones).
- **Candidate III (per-plane bilinear circulation).** ΣC_III = exactly 0 for all three 1D-line modes; nonzero for all 2D-planar and 3D-mixed modes. **Implements the hypothesis's selection rule exactly.** Under Cand III, 1D modes are dark and the 2D-planar tower carries observable EM charge.

The relative magnitudes of ΣC_III across the three 2D-planar mode classes are themselves informative: ~10⁻¹⁶ for the (23)-plane (lightest, contains only larger L's), ~10⁻¹⁰ for (13)-plane, ~10⁻⁶ for (12)-plane (heaviest, contains the smallest L₁). The numerical value scales as 1/(L_i L_j)² — the *bare* coupling magnitude per unit mode amplitude. After normalising by α (the observed coupling strength of any charged particle), these factors get absorbed into the mode's amplitude; what matters is the qualitative dark-or-bright distinction.

**Conclusion of Test B.** Of the three natural extensions of R19's integral to a 3-torus, only one (Candidate III, the per-plane bilinear circulation) implements the rule the hypothesis needs. The other two either preserve charge for 1D-line modes (Cand I) or invert the picture entirely (Cand II). Whether Cand III *is* the physically correct extension cannot be determined from this calculation — it requires re-running R19's full 2D derivation on the 3-torus and identifying which topological integral measures the asymptotic monopole moment.

### 5.3 Verdict

The 3-torus three-generations hypothesis has a **clean structural form** but its viability turns on a single open question:

1. ✓ **Mode counting works.** Three pairs (12, 13, 23) give three distinct 2D-planar mode towers; mass scales follow L₃/L₂ and L₃/L₁ as the user proposed.

2. ✓ **Hierarchy is achievable.** Setting L₂/L₁ ≈ 580 and L₃/L₁ ≈ 78,000 puts the three 2D-planar mode classes at the right relative energies for the three observed quark generations. The magnitude problem hasn't disappeared — it's just been redistributed across three lengths instead of one extreme ε — but the redistribution gives the *right* structural answer (three families, naturally) rather than a single parameter fitted post-hoc.

3. ✗ **A selection rule is required.** The bare Laplacian spectrum has ~L₃/L₂ ≈ 134 1D-line modes below the lightest 2D-planar mode. Without a rule that darkens the 1D class, the picture predicts ~134 unobserved particles (per (n, 0, 0) ladder direction) below the lightest charged fermion. This is a *worse* ghost problem than the model-D / R53 charged-ghost census (78 lepton-like ghosts above the electron).

4. ⚠ **The needed selection rule has one natural candidate** but its derivation has not been done. Candidate III (per-plane bilinear circulation, |C_{ij}|² ∝ (n_i n_j)²) has the structural property the hypothesis needs: 1D-line modes have zero coupling, 2D-planar modes have nonzero coupling. This is the 3D analog of R19's tube-circle integral generalised from "winding requires the cycle direction" to "winding requires *two* cycle directions for net EM flux." Whether this is the *physically correct* extension is a finite analytical question that would require re-running R19's monopole-moment derivation on a 3-torus, not yet attempted.

**If Cand III turns out to be the correct R19 extension**, the 3-torus picture is a clean and quantitatively viable structural reframing — it gives three generations from coordinate-plane Z₃ structure, explains the mass hierarchy from three compact-length ratios in the 1 : 580 : 78,000 range, and naturally makes the 1D-tower a dark-matter candidate (cf. [Q94 Compton-window / dark-modes](../../../qa/Q94-compton-window-and-dark-modes.md)).

**If Cand I (the direct 2D analog) turns out to be the correct extension**, the picture is killed in exactly the same way the 2D-sheet (1, 1)-ghost killed model-D: predicted modes show up that nature does not.

**Recommended next step.** Re-run the R19 derivation symbolically on a 3-torus: compute the asymptotic Coulomb monopole moment of a plane-wave mode ψ_n on a 3-torus embedded in ambient D-dimensional S, and identify which combination of (n₁, n₂, n₃) determines the monopole's magnitude. The bilinear (n_i n_j) form of Cand III suggests an underlying *flux through a 2-cycle* (Stokes-like) calculation; the per-cycle form of Cand I corresponds to a *line integral around a 1-cycle*. The choice between them is set by the dimensionality of the relevant surface integral in the embedding, which R19 fixes for the 2D case but is open for 3D. A focused one-or-two-page calculation should settle it.

Until that calculation is done, the 3-torus three-generations hypothesis sits at the same architectural level as Q94's Compton-window dark-modes proposal: structurally clean, computationally testable, but resting on an open selection-rule derivation.

---

## 6. Cross-references

- [sheet-proton 3-gen.md §12–§13](../../sheet-proton/work/3-gen.md) — Phase 3 / Phase 4 multi-generation analyses (the negative results that motivate this file).
- [sheet-proton clover-on-clover.md](../../sheet-proton/work/clover-on-clover.md) — fractal-recursion attempt (V1), failed.
- [sheet-proton clover-inverse.md](../../sheet-proton/work/clover-inverse.md) — three-radius cross-section attempt (V2), also failed.
- [sheet-proton clover-quarks.md §11](../../sheet-proton/work/clover-quarks.md) — per-arc curvature charges (the one-generation result that is preserved across both 2D and 3D pictures).
- [studies/R19-charge-from-shear](../../../studies/R19-charge-from-shear) — original 2D-MaSt derivation of "charge requires tube winding" (the rule whose 3D extension is the linchpin of this file's hypothesis).
- [studies/R46-electron-filter](../../../studies/R46-electron-filter) — 2D-MaSt analysis of (1, 1) ghost-filtering mechanisms (waveguide cutoff, helicity selection); analogs would extend to the 3D case.
- [studies/Q94-compton-window-and-dark-modes](../../../qa/Q94-compton-window-and-dark-modes.md) — the dark-modes-as-dark-matter hypothesis; relevant if Test B confirms the selection rule, since the 1D-line tower would then be a dark-matter candidate.
