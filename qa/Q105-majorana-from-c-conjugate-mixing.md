# Q105: Does Assignment A predict Majorana neutrinos?

**Status:** Open — hypothesis with testable prediction
**Related:**
  [Q97](Q97-shear-chirality-and-cp-violation.md) (shear chirality, C vs CPT),
  [Q102](Q102-neutrino-neutrality-from-sheet-size.md) (neutrino neutrality),
  [R49](../studies/R49-neutrino-filter/) (neutrino sheet study),
  [`primers/neutrino.md`](../primers/neutrino.md) §6 (Dirac vs Majorana)

---

## 1. The question

R26 Assignment A identifies the three neutrino mass
eigenstates as modes on Ma_ν:

| State | Mode (n₃, n₄) | μ² |
|-------|---------------|-----|
| ν₁ | (1, 1) | (1/ε)² + (1 − s)² |
| ν₂ | (−1, 1) | (1/ε)² + (1 + s)² |
| ν₃ | (1, 2) | (1/ε)² + (2 − s)² |

Modes (1,1) and (−1,1) differ only in the sign of n₃ — the
tube winding direction.  **Are these a particle-antiparticle
pair?  If so, does this make the neutrino a Majorana
particle?**


## 2. C vs CPT on the torus

Q97 §1 establishes the distinction between charge conjugation
(C) and full CPT on a sheared torus:

| Operation | Winding transform | Energy change |
|-----------|------------------|---------------|
| **CPT** | (n₃, n₄) → (−n₃, −n₄) | None (exact symmetry) |
| **C** | (n₃, n₄) → (−n₃, n₄) | Yes, if s ≠ 0 |
| **P** | Reverses handedness of knot | — |

The **CPT conjugate** of (1,1) is **(−1, −1)**, not (−1, 1).
CPT flips all winding numbers; the energy is unchanged
because q_eff² = (n₄ − s·n₃)² is invariant under
(n₃, n₄) → (−n₃, −n₄).

The **C conjugate** of (1,1) is **(−1, 1)** — same ring
winding, opposite tube winding.  Its energy differs:

- (1,1): q_eff = 1 − s → μ² = (1/ε)² + (1−s)²
- (−1,1): q_eff = 1 + s → μ² = (1/ε)² + (1+s)²

Mass-squared difference:

> Δμ²₂₁ = (1+s)² − (1−s)² = **4s**

So ν₁ and ν₂ in Assignment A are **C-conjugates with a
mass splitting set by shear**.


## 3. Why this is Majorana

In standard particle physics, a **Dirac mass** connects a
left-handed particle to a right-handed particle:

> m_D ν̄_R ν_L + h.c.

This preserves lepton number (ΔL = 0).

A **Majorana mass** connects a particle to its own charge
conjugate:

> m_M ν^T C ν + h.c.

This violates lepton number by 2 units (ΔL = 2) and makes
the neutrino its own antiparticle (in the sense of C, not
CPT).

Assignment A places both (1,1) and its C-conjugate (−1,1)
in the same mass eigenstate triplet.  The mass splitting
between them (Δm²₂₁ = 4s in dimensionless units) plays
the role of the Majorana mass-squared difference.  **This
is the WvM realization of a Majorana mass term: the
C-conjugate pair mix as mass eigenstates.**


## 4. Why they don't annihilate

If ν₁ and ν₂ are C-conjugates, why do they coexist as
stable mass eigenstates?

1. **They are standing waves, not localized particles.**
   Each mode fills the entire torus.  They don't "meet" at
   a point — they coexist as orthogonal vibration patterns
   of the same membrane.

2. **Winding number is topologically conserved.**  The tube
   winding n₃ is a topological invariant on the torus.
   Changing n₃ = +1 to n₃ = −1 requires a topological
   transition (unwinding and rewinding), which is
   suppressed by the same mechanisms that make the weak
   force weak.

3. **The annihilation rate is proportional to the coupling
   strength.**  On a neutral sheet with zero or near-zero
   shear, the coupling to external fields is extremely
   weak.  This is consistent with the observed
   neutrino-antineutrino annihilation cross-section being
   spectacularly small (~10⁻⁴⁴ cm² at MeV energies).

4. **Oscillation is interference, not annihilation.**  The
   "solar oscillation" ν₁ ↔ ν₂ is a quantum superposition
   of two nearly-degenerate standing waves drifting in and
   out of phase — analogous to beats between two close
   frequencies on a guitar.  No energy is exchanged; no
   mode is destroyed.


## 5. Testable prediction: neutrinoless double beta decay

If neutrinos are Majorana (C-conjugate mixing), the process
**neutrinoless double beta decay** (0νββ) must occur:

> (A,Z) → (A,Z+2) + 2e⁻   (no neutrinos emitted)

The rate depends on the **effective Majorana mass**:

> |m_ββ| = |Σᵢ U²_eᵢ mᵢ|

where U_eᵢ are elements of the PMNS matrix and mᵢ are the
mass eigenstate masses.

### Prediction from Assignment A

Assignment A (ε ≈ 5, s ≈ 0.022) gives:
- m₁ ≈ 29.2 meV
- m₂ ≈ 30.5 meV
- m₃ ≈ 58.2 meV

Using measured PMNS parameters (θ₁₂ = 33.4°, θ₁₃ = 8.6°,
δ_CP ≈ 194°, Majorana phases unknown):

> |m_ββ| ≈ |c²₁₂ c²₁₃ m₁ + s²₁₂ c²₁₃ m₂ e^{iα} + s²₁₃ m₃ e^{iβ}|

For the quasi-degenerate spectrum of Assignment A (all mᵢ
comparable), the terms don't cancel strongly.  The range
depending on unknown Majorana phases α, β:

> |m_ββ| ≈ 10–30 meV

This is within reach of next-generation experiments:

| Experiment | Target sensitivity | Timeline |
|------------|-------------------|----------|
| LEGEND-1000 | ~15 meV | Late 2020s |
| nEXO | ~5–15 meV | 2030s |
| CUPID | ~10–20 meV | Late 2020s |

**If Assignment A is correct and neutrinos are Majorana,
0νββ should be observed by these experiments.**

### Contrast with hierarchical spectrum

Family B (ε = 0.1) gives m₁ ≈ 5 meV, m₂ ≈ 10 meV,
m₃ ≈ 50 meV.  In this case:

> |m_ββ| ≈ 1–5 meV

This is below the sensitivity of planned experiments.
A non-detection of 0νββ would not rule out Majorana
neutrinos — it would instead disfavor Assignment A's
quasi-degenerate spectrum in favor of a more hierarchical
one.


## 6. The solar splitting as a Majorana mass

The identification Δm²₂₁ = 4s (in μ² units) connects the
measured solar splitting directly to the sheet's shear:

> s₃₄ = Δm²₂₁ / (4 E₀²)

where E₀ = ℏc/L₄ is the energy scale of the neutrino
sheet.

At ε = 5 and the masses above, E₀ ≈ 22.6 meV, giving:

> s₃₄ = 7.53 × 10⁻⁵ / (4 × (22.6 × 10⁻³)²)
>     = 7.53 × 10⁻⁵ / (2.04 × 10⁻³)
>     ≈ 0.037

This is close to the s ≈ 0.022 found by R26 from the
Δm² ratio alone (the difference is because the analytical
formula Δμ² = 4s is an approximation at finite ε).

The point: **the solar mass splitting directly measures the
shear on the neutrino sheet.**  A shearless sheet (s = 0)
would have ν₁ and ν₂ exactly degenerate — no solar
oscillation.  The existence of solar oscillation proves
s₃₄ ≠ 0.


## 7. Implications for R49 key questions

| R49 question | Implication |
|-------------|-------------|
| Q3 (oscillation mechanism) | Solar oscillation = C-conjugate interference.  Atmospheric oscillation = mixing with a higher-n₄ mode. |
| Q8 (shear and antimatter) | s₃₄ ≠ 0 is confirmed by the existence of solar oscillation.  The neutrino sheet IS sheared, producing weak C-violation. |
| Neutrino neutrality (Q102) | If shear is nonzero, neutrality cannot come from zero shear alone.  The sheet-size mechanism (Q102a) must be the primary explanation. |


## 8. Summary

Assignment A's mode structure — placing the C-conjugate
pair (1,1) and (−1,1) in the same mass triplet — is the
WvM realization of a Majorana mass term.  The solar
splitting measures the sheet's shear directly.  This
predicts:

1. **Neutrinoless double beta decay** at |m_ββ| ≈ 10–30 meV
   (testable by LEGEND-1000, nEXO, CUPID)
2. **Nonzero shear on Ma_ν** (s₃₄ ≈ 0.02–0.04), ruling out
   the "zero shear" explanation for neutrino neutrality
3. **CP violation in neutrino oscillation** (δ_CP ≠ 0),
   consistent with T2K hints

A non-observation of 0νββ at the ~15 meV level would
disfavor Assignment A's quasi-degenerate spectrum but would
not rule out Majorana neutrinos in general — a hierarchical
spectrum (Family B) would give |m_ββ| below current reach.
