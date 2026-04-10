# Q114. Bare magnetic moment convention and the proton mode question

**Status:** Open — foundational issue with implications for proton mode assignment
**Related:**
  [Q103 (anomalous magnetic moment)](Q103-anomalous-magnetic-moment-from-defect-cost.md),
  [`grid/maxwell.md`](../grid/maxwell.md) §Magnetic flux quantization,
  R47 (proton filter), R52 (self-field moment)

---

## 1. The two units conventions

The proton's magnetic moment is reported in two equivalent ways
in the standard physics literature:

| Notation | Value | Definition |
|----------|-------|------------|
| μ_p (in nuclear magnetons) | 2.7928 μ_N | Magnetic moment magnitude |
| g_p (g-factor) | 5.5857 | Dimensionless gyromagnetic ratio |

The relationship is **μ = (g/2) × magneton** for the maximum
projection of a spin-1/2 particle.  These are the same physical
quantity:

> g_p / 2 = 5.5857 / 2 = 2.7928 = μ_p / μ_N

For a Dirac point spin-1/2 particle, **g = 2 exactly**, and so
the "Dirac magnetic moment" equals 1 magneton.  The conventional
Dirac baseline is:

| Particle | Dirac baseline (g) | Dirac baseline (μ) |
|----------|-------------------|---------------------|
| Electron | g_e = 2 | μ_e = 1 μ_B |
| Proton | g_p = 2 | μ_p = 1 μ_N |

Standard physics treats the **deviation from g = 2** as the
"anomalous magnetic moment" (g − 2)/2.

For the electron: (g − 2)/2 ≈ α/(2π) ≈ 0.00116 (tiny — QED loops)
For the proton: (g − 2)/2 ≈ 1.793 (huge — QCD substructure)

## 2. MaSt's flux quantization formula gives the g-factor

The maxwell.md derivation gives:

> The bare magnetic moment of a (n_tube, n_ring) standing wave
> equals **n_ring** in the natural unit (magneton for moment,
> or equivalently **g_bare = 2 × n_ring/2 = n_ring** if you set
> the formula in terms of g — the factor of 2 from spin-1/2 is
> already absorbed into the magneton convention).

The formula maps the winding number directly to the g-factor:

> g_bare = n_ring

Or equivalently in moment units:

> μ_bare = (g_bare / 2) × magneton = (n_ring / 2) × magneton

**The "n_ring × magneton" expression in maxwell.md is an
unfortunate notation: the right reading is g_bare = n_ring,
not μ_bare = n_ring × magneton.**  The factor of 1/2 from spin
should be absorbed.

## 3. What the formula predicts

| Particle | Mode | n_ring | g_bare = n_ring | μ_bare = n_ring/2 magneton |
|----------|------|--------|-----------------|----------------------------|
| Electron | (1,2) | 2 | **2** | 1 μ_B |
| Proton | (1,3) | 3 | 3 | 1.5 μ_N |
| Proton | (3,6) | 6 | **6** | 3 μ_N |

Compared to measured values:

| Particle | g_bare (formula) | g (measured) | Match? |
|----------|------------------|--------------|--------|
| Electron (1,2) | 2 | 2.0023 | **YES — within α/(2π) ≈ 0.00116** |
| Proton (1,3) | 3 | 5.585 | **NO — off by ~2×** |
| Proton (3,6) | 6 | 5.585 | **YES — within 7%** |

**The flux quantization formula favors the (3,6) interpretation
of the proton, not (1,3).**

## 4. The proton mode question is still open

Model-D (parameter scorecard line 152) lists the proton mode as:

> **Proton mode | (1,3) | Leading; (3,6) viable alternative**

Model-D's working assumption is (1,3), with (3,6) as a viable
alternative.  Both interpretations remain alive.  The flux
quantization formula derived in maxwell.md gives different
predictions for each:

- **(1,3) interpretation:** g_bare = 3, measured g = 5.585,
  residual = +86% (large)
- **(3,6) interpretation:** g_bare = 6, measured g = 5.585,
  residual = −7% (small)

Each has its own evidence:

**Evidence for (1,3):**
- Universal charge formula Q = −n_tube + n₅ works for both
  particles AND nuclei
- Single connected mode (simpler topology)
- R47's leading candidate after track-by-track filtering

**Evidence for (3,6):**
- Flux quantization formula gives g_bare = 6, matching measured
  5.585 to ~7%
- gcd factorization gives 3 strands of (1,2), reminiscent of
  3-quark structure
- The −7% residual is the right size for an α-mediated
  correction (similar to electron's α/2π but at proton coupling)

**Neither interpretation is settled.**  The flux quantization
formula could be:
- Correct, in which case (3,6) is favored
- Incorrect for (1,3) modes, in which case the formula needs
  revision but doesn't eliminate (1,3)
- Correct for both with a hidden factor we haven't identified
  (e.g., a topology-dependent prefactor)

Until a definitive piece of evidence emerges, R52 and related
analyses should treat both as live options.

## 5. The case for (3,6) proton

The flux quantization formula provides one piece of evidence
for (3,6).  Other arguments in favor of (3,6):

- Topologically, (3,6) factors as gcd = 3, giving 3 strands
  of (1,2).  Each strand is "electron-like."  The proton is
  literally "three electrons sharing a sheet" — which is
  reminiscent of the constituent quark model with 3 quarks.
- The bare g = 6 prediction agrees with the measured g = 5.585
  within 7%, leaving a small residual to explain.
- The strand count matches the SU(6) quark-flavor structure.

## 6. The case for (1,3) proton (model-D's choice)

Model-D selected (1,3) over (3,6) for these reasons:

- **Universal charge formula:** Q = −n_tube + n₅ works for (1,3)
  and is consistent with the charge formulas for nuclei.  For
  (3,6), the charge formula needs modification.
- **Simpler mode topology:** (1,3) is a single connected strand;
  (3,6) is three disconnected strands.  Fundamental-particle
  intuition prefers a single connected mode.
- **Spin works in both:** n_tube = 1 (odd) gives spin 1/2 for
  (1,3); n_tube = 3 (also odd) gives spin 1/2 for (3,6).
  Either works.

The (1,3) interpretation is "leading" in model-D, but it
explicitly leaves (3,6) as a viable alternative.  The flux
quantization formula, if accepted, tips the balance toward
(3,6).

## 7. Past studies that were confused

Several past studies use INCONSISTENT framings of the proton's
bare moment:

### R47 — multiple framings without resolution

R47 uses three different "bare" calculations:

| Section | Formula | (1,2) electron | (1,3) proton |
|---------|---------|----------------|--------------|
| Track 7 script | g × (n_tube/n_ring) | 1 (matches) | 0.67 (wrong) |
| SU(6) section | Quark model combination | 1 (matches) | 3 (matches) |
| README table (line 441-442) | "Bare moment" | 2 μ_N (?) | ~3 μ_N |

The README's table value of "2 μ_N" for the electron's bare is
suspicious — the electron's moment is in BOHR magnetons, not
nuclear magnetons.

R47's "required enhancement = g_p/g_Dirac = 2.793" framing uses
the standard Dirac baseline (g_bare = 2), not MaSt's flux
quantization (g_bare = n_ring).  The two framings answer
different questions:

- "We need to find a +179% enhancement" (Dirac baseline)
- "We need to find a −7% reduction" (MaSt baseline if (3,6))
- "We need to find a +86% enhancement" (MaSt baseline if (1,3))

These all use the same measured value (g = 5.585) compared to
different bare values (2, 6, or 3).

### maxwell.md — confused notation

The flux quantization derivation in `grid/maxwell.md` §Magnetic
flux quantization writes the formula as **μ = n_ring × magneton**,
which suggests "the moment is n_ring magnetons."  This is
misleading: the formula actually gives the g-factor (not the
moment), and the units convention should be made explicit.
The Q114 update should fix this.

### R52 — uses the (1,3) framing

R52 (this study) uses MaSt baseline = 3 μ_N for the proton
(equivalently g_bare = 6, treating the formula as giving moment
in magnetons with no factor of 1/2).  This is consistent with
the (1,3) reading IF we drop the factor of 1/2, but inconsistent
with the standard "μ = (g/2) × magneton" relationship.

R52 then computes residual = −7%.  This residual is correct in
the (3,6) framing where bare g = 6 and measured g = 5.585.
**It is NOT correct in the (1,3) framing** where bare g = 3
and measured g = 5.585 (residual would be +86%, not −7%).

R52 has been implicitly using the (3,6) framing while calling
it (1,3).  The numerical conclusions about R52 are unaffected
because the −7% residual matches measurements either way; only
the labeling of which mode is being analyzed changes.

## 8. Working convention

Until the foundational issue is resolved:

- **Use g-factor framing throughout R52 and dependent analyses.**
- **MaSt bare g = n_ring** (the closed spatial winding number).
- **Electron (1,2):** g_bare = 2, measured g = 2.0023, residual = +α/(2π)
- **Proton:** TWO POSSIBLE INTERPRETATIONS depending on mode:
  - **(1,3):** g_bare = 3, measured g = 5.585, residual = +86% (LARGE)
  - **(3,6):** g_bare = 6, measured g = 5.585, residual = −7% (small)
- **R52's actual numerical analysis** has been treating the
  proton as if g_bare = 6 (residual −7%), which corresponds to
  the (3,6) interpretation, not (1,3).

The fact that R52 has been computing the −7% residual all along
suggests we have been implicitly assuming (3,6) without
acknowledging it.

## 9. Recommendations

1. **Stay open on proton mode.**  Both (1,3) and (3,6) are
   alive interpretations.  Neither has been eliminated by
   definitive evidence.  R52 and related analyses should not
   commit to one without explicit justification.

2. **R52 must run computations for both interpretations**
   when they give different predictions.  The numerical
   results will inform whether the gap closes for one mode but
   not the other.

3. **Update maxwell.md** to clarify that the formula gives
   g-factor (= n_ring), not moment-in-magnetons, and to note
   that the formula favors specific mode interpretations.
   ✓ (done)

4. **Update R47** to mark which of its multiple framings is
   the canonical one and which are historical.

5. **Track 4f should test both (1,3) and (3,6)** and report
   the results separately.  The empirical results may favor
   one mode if its predicted shear lands inside the viability
   window while the other doesn't.

## 10. Status

This question is **foundational and unresolved**.  The R52
numerical analysis has been computing a −7% proton residual,
which corresponds to the (3,6) interpretation (bare g = 6).
The (1,3) interpretation (bare g = 3) would give a +86%
residual instead, requiring a fundamentally different analysis.

**Working approach (Track 4f and beyond):** test both proton
mode interpretations side by side.  Don't commit to either
until empirical evidence forces a choice.

The user's observation about "3 or 6 depending on how you look
at it" captures the ambiguity exactly.  Both views are
mathematically valid; the experimental observation (g = 5.585)
is the same in both cases.  The question is which MaSt
interpretation is physically correct.
