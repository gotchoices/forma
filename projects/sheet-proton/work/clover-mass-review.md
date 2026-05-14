# clover-mass-review.md — Review of work/clover-mass.md

Review of [clover-mass.md](clover-mass.md), which derives the mass spectrum on the corrugated torus surface of [clover-quarks.md](clover-quarks.md), reduces the 2D eigenvalue problem to a 1D Hill equation via the helical symmetry, and attempts an inversion to extract (ε, χ) from m_p and m_n.

Material concerns enumerated below. The file's §§1–5 derivations and §6.6 self-correction were verified before writing this review; the analytical content is sound.

---

## 1. Mode-particle identification is not pinned

The file explicitly acknowledges this in §7 and again in §8.1. Two candidate identifications are on the table:

- **Identification I** — semiclassical path windings, using clover-quarks §12.2's (n_θ, n_φ) = (2, 1) for proton and (1, 1) for neutron. The file says "this route is not yet closed; it gives one equation between ε and the (n, m) of each particle, requiring more information."
- **Identification II** — lowest matching modes. The file works this through (§§8–8.1) and finds a 372-element family of compatible (n_p, m_p) → (n_n, m_n) pairings clustering at several distinct ε values.

§8.1 honestly summarises the state: *"The leading-order constraint produces a family of solutions, not a unique answer. To collapse the family we need additional input: a third observable, the χ-dependent second-order correction, or a first-principles argument for the (n, m) → particle map."*

Until the identification is pinned, the inversion produces a parameter family, not a unique prediction.

**Note on dependency:** Identification I depends on clover-quarks §12.2's path-winding count (n_θ, n_φ) = (2, 1) for the proton. The clover-quarks-review flagged a §3.3 vs §12.2 inconsistency on this count; Identification I inherits that inconsistency until it is reconciled upstream.

---

## 2. Embedding B is not analyzed

§1 commits to Embedding A (parameter-shift, with metric from clover-quarks §10) and notes *"the same machinery applies to embedding B with extra cross-section-rotation terms; we'll note where the two embeddings diverge."* The promised B-analysis is not carried out anywhere in the file. §6.7's "next steps" lists "Redo for embedding B (rotation). Embedding B has a different metric and hence different δ²μ². The structural conclusion (whether the geometry can or cannot produce m_n/m_p) might depend on the embedding."

This is the same open item as in clover-quarks-review §2 — Phase C numerics on either Embedding A or B can be done, but the mass-spectrum predictions are sensitive to the choice and the choice is not yet made. The spectrum derived in this file is Embedding A's.

---

## 3. The §6.6 zeroth-order fit has a 0.03% residual

The file's revised post-§6.6 finding is that pairs like (n_p, m_p) → (n_n, m_n) = (1, 2) → (2, 2) at ε ≈ 0.2 give m_n/m_p ≈ 1.00168 against the observed 1.00138. Verified: at ε = 0.2 with these labels, the zeroth-order formula gives m_n/m_p = 1.00166 — a residual of 0.03% relative to target.

The file says: *"The error of 0.03% can plausibly be closed by fine-tuning (ε, χ) or by going to slightly higher (n, m) labels."* That is plausible — the residual is small enough that χ-corrections at O(η²) could plausibly close it. But the fine-tuning has not been done, and "plausibly close" is not "closed."

A definite mass-ratio prediction requires actually running the fine-tune (which §6.7 lists as a next step). Until then the file should be read as "the framework qualitatively reaches the right order of magnitude on the proton-neutron mass split with low-(n, m) identifications," not as "the framework reproduces m_n/m_p quantitatively."

---

## 4. R_major underpredicts the proton charge radius

§8.1's survey gives clusters of compatible identifications with R_major spanning 0.16 fm to 4.0 fm. The "robust cluster" at ε ≈ 0.5 gives R_major ≈ 0.42 fm; the Identification II inversion at ε ≈ 3 gives R_major ≈ 0.16 fm. Observed proton charge radius is R_p ≈ 0.84 fm.

The file addresses this in §8.1 honestly: *"R_major is not R_p. R_p is the RMS electromagnetic radius — for our torus, R_p² ≈ R_major² + (cross-section RMS)² + (charge-distribution-shape corrections). A back-of-envelope estimate gives R_RMS_torus ≈ 0.44 fm at this point, comparable to R_major but well below R_p = 0.84 fm."*

So even with the cross-section contribution to the RMS radius, the predicted size comes out roughly half of what's observed. The file conservatively reads this as "not yet a prediction" rather than "a successful match" — appropriate, but it should be carried forward as an open quantitative concern, not just an aside in §8.1.

---

## 5. The 372 compatible identifications span a wide parameter range

§8.1's survey over |n|, |m| ≤ 3 produces 372 compatible identifications, clustered at several distinct ε values: 0.16, 0.18, 0.51, 0.53, 0.65, 3.0 (and others). Different clusters give different R_major values (0.16 fm to 4.0 fm). The file notes this and concludes that *"the leading-order constraint produces a family of solutions, not a unique answer."*

This is a real limitation, not a technical detail. Without a first-principles argument for which (n, m) is which particle, the framework predicts only a *family* of (ε, R_major) values consistent with m_n/m_p — and the family spans more than an order of magnitude in R_major.

The file lists in §8.1 three ways to collapse the family: a third observable, the χ-corrections, or a first-principles identification argument. None of these has been done.

---

## Verdict

Material items requiring attention, in rough order of urgency:

1. **Pin the (n, m) → particle identification** — until done, the inversion produces a family of (ε, R_major) values spanning more than an order of magnitude, not a unique prediction.
2. **Complete the §6.7 fine-tune** — close the 0.03% residual on m_n/m_p quantitatively (or determine it can't be closed within physically reasonable (ε, χ)).
3. **Analyze Embedding B** — confirm that the spectrum's qualitative behaviour does not depend on the embedding choice, or determine which embedding is physical.
4. **Reconcile with clover-quarks-review §1's §3.3-vs-§12.2 closure count** — Identification I depends on this resolution.
5. **Address the R_major vs R_p ≈ 0.84 fm gap** — even with the best-fitting cluster, the predicted size is ≈ half the observed charge radius. Either the cross-section contribution to ⟨r²⟩ is much larger than the §8.1 estimate, or there is a systematic gap to be explained.

**Positive observations** (the file's math is sound where it claims correctness):

- The helical-coordinate diagonalisation of the metric (§2) is correct.
- The Bloch BC derivation giving k_v = q/3 (§3) is correct.
- The zeroth-order mass formula μ² = (n − 2m/3)² + (m/ε)² (§4) is correct, with the σ_eff = 2τ structural observation (twist contributes once via the boundary identification and once via the metric inverse) being a clean finding.
- The first-order PT vanishing via ∫ P_x du = 0 (§5) is correct.
- §6.6's self-correction of §6.3's PT formula is the right call — the §6.3 derivation summed over couplings outside the physical Bloch sector; the corrected statement is that intra-sector couplings vanish at first order in η (because P_x has no Fourier support on κ ≡ 0 mod 3) and the leading O(η²) correction comes from diagonal matrix elements of the second-order operator L_2, not from second-order PT on L_1. This is technically right.
- The reduction of the 2D PDE eigenvalue problem to a 1D Hill ODE is a real simplification and makes Phase C numerically cheap.

The file is in an honest mid-state: the analytical machinery is in place, an independent numerical solver validates the zeroth-order formula and reveals candidate identifications, the §6.4 negative result has been correctly overturned, but the identification problem is unresolved and the fine-tuning is undone. Reading the file as "we have the spectrum" overstates it; reading as "we have a candidate spectrum and a tractable inversion problem" is right.
