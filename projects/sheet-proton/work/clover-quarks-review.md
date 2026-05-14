# clover-quarks-review.md — Review of work/clover-quarks.md

Review of [clover-quarks.md](clover-quarks.md), which proposes a corrugated 3-lobed torus geometry with a 1/3 twist as the proton-sheet substrate and identifies lobe and saddle arcs with up and down quarks.

Material concerns enumerated below.

---

## 1. Closure-revolution count is inconsistent between §3.3 and §12.2

**§3.3 (under Choice B literal-arc parameterization):** the up-quark path closes after **3 ring revolutions**; the proton-as-three-precessing-up-quarks reading is the user's "1/3 precession" picture.

**§12.2 (recomputed under the relabeled quark identification):** the proton path (2 lobes + 1 saddle) closes after **n_θ = 2 ring revolutions** with n_φ = 1 full profile traversal. The neutron path closes after n_θ = 1 revolution.

The §12.2 recomputation is internally consistent with the equation (Δφ = n_θ · 2π/3 + n_φ · 2π), but it directly contradicts §3.3's "3 revolutions" claim. The file's §12.2 reconciliation paragraph is a partial fix — it says "the user's '3 revolutions' may have been about lobe-label rotation, not path closure" — but does not retract the §3.3 framing.

**The issue:** the two derivations cannot both be right under the same set of assumptions. Either §3.3's "up-quark precesses 120° per revolution, closes after 3" or §12.2's "proton path closes after 2 revolutions" — and the §12.2 result depends on identifying the proton with the *composite* path rather than with three separately-precessing constituents. The Phase A "headline" (proton = 2 lobes + 1 saddle path) is incompatible with the Phase A "1/3 precession of three constituents."

**What would close this:** retract §3.3's "3-revolution" framing and replace it with §12.2's "proton path closes in 2 revolutions, composite of 2 lobes + 1 saddle," with the lobe-label-rotation observation properly demoted to a side note about how the wave's lobe-position-label cycles after 3 revolutions while the path itself closes after 2.

---

## 2. Embedding A vs Embedding B — Phase C requires choosing one

The file presents two embedding choices in §9.3:

- **Embedding A (parameter-shift):** under the change of coordinates ψ = φ + τθ, the surface is an untwisted corrugated torus carrying the twist purely in its boundary identification — a standard T² with a clover-shaped cross-section.
- **Embedding B (rotation):** the cross-section physically rotates by τθ as θ advances. The embedded surface genuinely carries the twist; no reparameterisation makes it untwisted.

§10 derives the metric for Embedding A only; §9.5 notes that Embedding B's metric is "structurally similar but produces additional g_θφ contributions from the cross-section rotation; it is deferred until §9.5's open question is resolved." The two embeddings agree on topology and path windings but disagree on the induced metric, the Laplace-Beltrami spectrum, and therefore on any mass predictions.

**What needs to happen:** before Phase C's numerical eigenvalue work, a choice between A and B must be made (or both worked out and compared). The metric for Embedding B is undone; the file should either commit to A, or complete B's derivation. The mass-spectrum predictions depend on this choice.

---

## 3. Three parameters where metric-charge has two

The clover surface has three free parameters: (R_major, r_lobe, r_saddle), equivalently (R_major, ε, χ) where ε = (2r_lobe + r_saddle)/R_major and χ = r_saddle/r_lobe. Metric-charge has two: ε and σ_uw.

The file maps (ε, χ) onto (L_u/L_w, σ_uw) but acknowledges in §8.2 that "χ is analogous to σ_uw in spirit (a deformation parameter beyond the bare aspect ratio) but with a *geometric* origin (corrugation depth) rather than a metric-shear origin (off-diagonal metric term)." That is — χ and σ_uw are not the same thing; the analogy is loose.

R_major is an additional overall length scale with no direct metric-charge analog (metric-charge's overall scale is set by L_w; the framework has one length scale, the clover surface has effectively two: R_major and the cross-section scale).

**The issue:** clover-quarks is not a reparametrization of metric-charge; it is a *richer parameter space*. That is fine as a research direction, but the file's framing implies a closer correspondence than the structure actually supports. Empirical fits (R64 Point A vs Point B) on a 2-parameter (ε, σ_uw) sheet would need to be reinterpreted on a 3-parameter (R_major, ε, χ) clover-corrugated sheet, with no obvious reduction.

**What would close this:** state the parameter count cleanly. Note that the clover framework extends metric-charge's parameter space rather than mapping onto it, and that empirical (ε, σ_uw) fits from R-track studies do not translate directly into (R_major, ε, χ) values on the corrugated surface.

---

## 4. Plane waves are not eigenmodes of the corrugated Laplacian

**§11 derivation:** modes are taken as exp(i k_θ θ + i k_φ φ), single-valuedness gives k_θ = q − p/3, k_φ = p.

**§13 (Phase C, deferred):** the actual Laplacian on the corrugated metric of §10 has position-dependent coefficients (through P_x(φ + τθ)); the eigenvalue problem is a 1D Hill equation after using helical translation symmetry. Plane waves are not eigenfunctions; the true eigenmodes have non-trivial Φ-dependence.

**The issue:** §11's k_θ = q − p/3 is a single-valuedness statement on test functions, not an eigenvalue statement. The actual mode spectrum requires solving the Hill equation. Whether the actual eigenvalues organize cleanly into the labeling §11 anticipates is what Phase C must determine, and Phase C is deferred.

**What would close this:** clearly mark §11 as labeling the admissible boundary conditions for plane-wave test functions, useful for organizing the Hilbert space but not yet a spectrum result. Phase C is required to convert the labeling into mass predictions.

---

## 5. The proton-neutron mass split is not derived

**§12.5:** under the topology-alone hypothesis, m_n − m_p ≈ E_S − E_L, where E_L and E_S are per-lobe and per-saddle energy contributions. The file notes "the neutron being heavier means E_S > E_L (saddles cost more energy than lobes)" and offers an intuitive "saddles are compressed, higher momentum" argument.

**The issue:** the hypothesis E_S > E_L is consistent with observation but is not derived from the geometry. Phase C numerical work is needed to compute E_L and E_S from the corrugated Laplacian's eigenvalues. The file's confidence in the result currently rests on a coincidence (the sign is right under the hand-wavy "saddles are compressed" argument).

Additionally, in actual QCD, the proton-neutron mass split (≈1.3 MeV) comes from a delicate combination of electromagnetic effects, the up-down bare-mass difference, and chiral-symmetry-breaking dynamics. None of this is in the clover construction.

**What would close this:** Phase C numerics for E_L and E_S, with explicit sensitivity analysis to the (ε, χ) parameters. Until then, the mass-split discussion in §12.5 is structural framing only, not a prediction.

---

## Verdict

Material items requiring attention, in rough order of urgency:

1. **Reconciliation of §3.3 vs §12.2** — pick one closure-count story and retract the other.
2. **Commit to Embedding A or B (or work out both)** — Phase C numerics require a metric, and Embedding B's metric is currently deferred.
3. **State the parameter count cleanly** — three parameters (R_major, ε, χ), not a reparametrization of metric-charge's two.
4. **Mark §11 as boundary-condition labeling, not a spectrum result** — Phase C is required to convert it into mass predictions.
5. **Phase C numerics** — until done, mass and mass-split predictions are structural framing only.

The file is well-organized and the geometry is real. The remaining concerns are about internal consistency and computational completion, not about the framework's structural claims.
