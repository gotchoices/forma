# R64 Track 2 — Quark generation primitive identification

Track 2 tests whether the magic point `(ε_p, s_p) = (0.07309, 0.19387)`
identified in Track 1 hosts the remaining quark generations as
primitive classes on the p-sheet.  Phase 2a takes up the strange
quark.

**Result: partial success with structural concerns.**

A primitive `(n_t, n_r) = (1, −20)` reproduces m_s = m_Ω/3 = 557.5 MeV
to 0.04% — Ω⁻ (sss) is then exactly predicted by construction.  But
the same primitive predicts other strangeness-bearing hadrons with
strangeness-dependent errors:

- Ω⁻ (sss): 0.01% (anchor)
- Ξ⁻ (dss): +2.3%, Ξ⁰ (uss): −2.1%
- Λ (uds): −5.9%
- Σ⁻ (dds): −8.6%, Σ⁺ (uus): −14.9%
- K⁺ (us̄): +1.8%, K⁰ (ds̄): −17%

The pattern: high-strangeness states fit well, low-strangeness mixed
states don't.  This reflects a structural mismatch between MaSt's
flat-formula mass scaling and the SM's near-degeneracy isospin
structure — Σ⁺ (uus) and Σ⁻ (dds) differ by only 8 MeV (0.7%) in
nature but by 80 MeV (7%) in MaSt's prediction.

The strange quark choice is also unsettling at the lattice level:
n_r_s = −20 is **ten times larger than n_r_u = +2**, with no
structural reason in the lattice for strange to live at that
specific n_r value (chosen to fit m_Ω, not derived).

Script:
[`scripts/track2_phase2a_strange_quark.py`](scripts/track2_phase2a_strange_quark.py)
Outputs:
[`outputs/track2_phase2a_strange_lattice.csv`](outputs/track2_phase2a_strange_lattice.csv)

---

## Phase 2a — Strange quark primitive search

### Method

At the magic point `(ε_p, s_p, K_p) = (0.07309, 0.19387, 22.847)`,
scan all primitives `(n_t, n_r)` with |n_t| ≤ 6, |n_r| ≤ 30 for
classes whose mass matches m_s ≈ 557 MeV.  Apply Z₃ confinement
constraint: for a baryon with one strange quark plus two u/d quarks
(Λ, Σ, K), Z₃ requires the baryon's total n_pt ≡ 0 (mod 3), giving
**n_t_s ≡ 1 (mod 3)** — allowed values {..., −5, −2, 1, 4, 7, ...}.

### F2a.1. Mass-shell structure dominates at small ε

The mass formula at small ε reduces to mass shells indexed by n_t:

| n_t | shell mass (MeV) | particle role | Z₃ for uds? |
|:-:|:-:|:-:|:-:|
| 1 | 313 | u, d (Track 1) | yes |
| 2 | 625 | — | NO |
| 3 | 938 | proton, neutron | NO |
| 4 | 1250 | — | yes |
| 5 | 1563 | — | NO |
| 6 | 1876 | (= 2·m_p, deuteron) | NO |
| 7 | 2188 | — | yes |

The constituent strange mass m_s ≈ 557 MeV **falls between shells 1
and 2** — there is no integer-n_t shell at strange-quark mass.
Within the n_t = 1 shell, only large |n_r| can push the mass up
toward 557 MeV (each unit of |n_r| past ~10 contributes ~10 MeV to
m_s).

### F2a.2. Best Z₃-compatible match: (1, −20) at 557.27 MeV

Sweeping n_r in the n_t = 1 shell:

| (n_t, n_r) | mass (MeV) | err vs m_s |
|:-:|:-:|:-:|
| (1, −17) | 502 | −9.95% |
| (1, −18) | 520 | −6.71% |
| (1, −19) | 539 | −3.40% |
| **(1, −20)** | **557.27** | **−0.04%** |
| (1, −21) | 576 | +3.38% |
| (1, +20) | 550 | −1.35% (parity-flipped, also viable) |

The primitive **(1, −20)** matches m_s = 557.5 MeV to 0.04%.  By
construction (3·m_s = m_Ω in the additive model), this gives
**Ω⁻ at exactly 1672.6 MeV** vs observed 1672.45 — a 0.01% match.

The n_r_s = −20 value is **10× larger** than n_r_u = +2, n_r_d = −2.
There is no structural reason within the lattice for strange to
sit at this specific n_r — it's chosen to fit Ω⁻'s mass, not
derived from a generation principle.

### F2a.3. Strangeness-bearing inventory at this candidate

Computing all strangeness-bearing baryons under additive winding at
the magic point with strange = (1, −20):

| Particle | Quark content | tuple | predicted | observed | err |
|:---|:---|:-:|:-:|:-:|:-:|
| Ω⁻ | sss | (3, −60) | 1672.6 | 1672.45 | +0.01% (anchor) |
| Ξ⁻ | dss | (3, −42) | 1352 | 1321.71 | **+2.3%** |
| Ξ⁰ | uss | (3, −38) | 1288 | 1314.86 | −2.1% |
| Λ | uds | (3, −20) | 1050 | 1115.68 | **−5.9%** |
| Σ⁻ | dds | (3, −24) | 1094 | 1197.45 | **−8.6%** |
| Σ⁺ | uus | (3, −16) | 1012 | 1189.37 | **−14.9%** |
| K⁺ | us̄ | (0, +22) | 503 | 493.68 | +1.8% |
| K⁰ | ds̄ | (0, +18) | 411 | 497.61 | **−17%** |

**Pattern**: high-strangeness states fit well (Ω, Ξ within 3%),
low-strangeness mixed states fit poorly (Σ at 9–15%, K⁰ at 17%).

### F2a.4. The structural problem: SM isospin doesn't fall out

In nature, **Σ⁺ (uus) and Σ⁻ (dds) differ in mass by 8 MeV** (0.7%) —
nearly degenerate, set by the small u/d quark mass split plus
electromagnetic effects.  In MaSt's harmonic stack at the magic
point, the same swap (replacing two u's with two d's) shifts
n_r by 8 units (from −16 to −24 + −8), giving an 80 MeV mass change
(7%) — **10× the observed split**.

Similarly, **K⁺ (us̄) and K⁰ (ds̄) differ by 4 MeV** in nature
(0.8%), but MaSt predicts a 92 MeV difference (18%).

The flat-formula mass scaling at small ε is **too sensitive** to
n_r differences for the SM's near-degenerate isospin structure to
emerge naturally.  The framework's natural flavor metric does not
match the SM's near-isospin-symmetric metric.

### F2a.5. Λ as anchor gives a different m_s — incompatible with Ω⁻

If we anchor strange to Λ (uds) instead of Ω⁻ (sss):
- Λ tuple = (3, n_r_s); m_Λ_pred matches 1115.68 at n_r_s ≈ ±27.
- This implies (1, ±27) for strange, with **m_s ≈ 696 MeV**
  (not 557).
- Predicted Ω⁻ = 3·m_s · (μ correction factor) ≈ 2086 MeV — off
  by **+25%** from observed 1672.

**No single (n_t, n_r) for strange fits both Ω⁻ and Λ
simultaneously.**  The strange quark is over-determined by the
existing strangeness inventory; there's no consistent primitive
choice.

### F2a.6. What Phase 2a establishes

1. **A primitive class hosting m_s ≈ 557 MeV exists at the magic
   point** — (1, ±20) — and Z₃ confinement allows it.
2. **Anchoring strange to Ω⁻ gives an exact Ω⁻ but progressively
   worse predictions for lower-strangeness states**, with up to
   17% error on K⁰ and 15% on Σ⁺.
3. **The harmonic-stack picture at the magic point does not
   reproduce the SM's near-isospin-symmetric mass structure**.
   MaSt's natural mass scaling at small ε is too n_r-sensitive
   for the SM's degenerate-isospin pattern.
4. **Strange quark identification is not unique**: anchoring to
   different observed strange particles gives different (n_t, n_r),
   and no single choice fits the full strangeness inventory.

### F2a.7. Reading

The Phase 2a result has the **same shape as R64 Track 1's deuteron
result combined with R63 Track 11's curved-donut result**:
- A specific anchor matches well by construction (Ω⁻ here, B(²H)
  in Track 1).
- Predictions for *other* observables drift in a structured but
  unsuccessful way (light-A nuclei in Track 1, mesons in 11a,
  Σ/K⁰ here).
- The framework's natural mass-scaling "shape" doesn't match the
  observed inventory's "shape" beyond the anchor.

Two readings of the result:

**Reading A — strange is not a single primitive on the p-sheet
under additive winding.**  The 14% Σ⁺ error and 17% K⁰ error are
beyond the 5% inventory-preservation gate.  At face value, the
harmonic-stack picture for the strange quark fails Phase 2a's
inventory-survival test.  R64 closes negative (or the picture
is restricted to first-generation only).

**Reading B — the composition rule for higher generations is
non-trivial.**  The user's own framing anticipated non-additivity
("there is a slight non-linearity ... it generally takes more
neutron windings to balance things out").  The Σ/K-mass errors
might be the same A ≥ 3 stacking problem from Track 1, manifesting
in the strangeness sector.  If a refined stacking rule fixes both
the ⁴He under-binding and the Σ over-prediction, R64 survives.

The strangeness sector is a **better test for the stacking rule**
than nuclei because it's a single-strand swap (replace one u with
one s), making any structural correction visible at smaller A.

### F2a.8. What this rules in vs out

**Ruled out at face value**: a 6-quark family on the p-sheet at
the magic point with strict additive winding composition.

**Not ruled out**: a refined composition rule that fixes the
A ≥ 3 / Σ-mass discrepancies simultaneously.  Whether such a
rule exists is the question for the next phase.

**Not yet tested**: charm, bottom, top.  But the structural concern
(generations don't fit naturally as integer (n_t, n_r) classes
because mass shells are at ~313·n_t MeV while observed quark
masses don't sit at those shell values) extends naturally to
heavier generations and is unlikely to vanish.

---

## Recommendation

The clean strangeness anchor on Ω⁻ vindicates the picture for
**strangeness-rich states** but fails it for **light-strangeness
mixed states**.  The honest read is that R64's *additive winding*
composition rule is too rigid — it produces a mass-formula scaling
that doesn't match SM's isospin symmetry.

Two paths from here:

**Path 1 — refine the composition rule (Phase 2b before charm).**
Test whether a non-additive stacking rule that fits the user's
"slight non-linearity" anticipation simultaneously fixes ⁴He's
under-binding and Σ's over-prediction.  Candidates:
- Multi-mode coherence (compound mass = SL eigenvalue at the
  combined tuple, not arithmetic of primitives).
- Shell-closure correction (extra binding when N=Z=2 or similar).
- Partition-dependent corrections (the way k strands distribute
  across u/d/s slots matters).

**Path 2 — accept partial success (first generation only).**
Restrict R64's claim to the proton/neutron/deuteron success of
Track 1.  Higher generations live cross-sheet (as in model-F)
or in geometric structures beyond the flat p-sheet alone.  The
h-candidate becomes a **first-generation theory** with the
strange/charm/bottom/top sectors handled as in R63's model.

I lean toward **Path 1**.  The Σ/K isospin problem is not
strange-specific — it's a property of the small-ε mass scaling.
Either the stacking rule needs structure that re-establishes
isospin near-symmetry, or the picture is fundamentally wrong.
Testing one principled refinement to the rule is cheap and
diagnostic.  If it fails, Path 2 is earned.

The natural Phase 2b: **"does shell-closure / coherence supply
the missing isospin near-symmetry, AND simultaneously fix the
light-A nuclear binding?"**  One refined rule, two empirical
gates.
