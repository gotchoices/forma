# Q&A Inbox

Capture queue for new questions. Add questions here as they arise.

**Workflow:**
- Add questions here as they come up.
- Quick answers: answer inline, mark `answered`.
- Needs real work or substantial write-up: create `Q<N>-slug.md` in this folder,
  add to [`README.md`](README.md) index, and remove the entry here.
- Needs computation: create a study entry in [`studies/STATUS.md`](../studies/STATUS.md).

Once a question has a Q file or is answered, it leaves this page.
[`README.md`](README.md) is the sole index of all Q files.

---

## Reducing free parameters (2026-04-15)

Context: Model-E has 4 dimensionless free parameters (α,
m_μ/m_e, m_τ/m_e, Δm² ratio) plus 3 dimensional scales
(m_e, m_p, Δm²₂₁).  These questions ask whether any of
them can be derived rather than measured.

1. **Metric positive-definiteness constraints.**  The 9×9
   metric has 45 entries.  How many are truly free after
   imposing: positive-definiteness, physical mode spectrum
   (no tachyons), correct spin-statistics?  Pure linear
   algebra — computable now.  Could dramatically shrink the
   design space.

2. **Cross-sheet consistency from single T⁶.**  The three
   sheets share one manifold.  Are the off-diagonal
   (cross-sheet) entries determined by the diagonal entries
   once you require a valid metric on one T⁶?  Related to #1
   but specifically targets the cross-sheet couplings.

3. **Effective net coupling to S = α.**  We have not fully
   resolved all 9×9 metric terms such that, after setting
   internal shears and aspect ratios, the effective net
   coupling from Ma to S lands at α = 1/137.  The R19
   formula works at the p-sheet (ε ~ O(1)) but not at the
   e-sheet (ε >> 1).  R55 is framed to address this but the
   path is uncertain.  The question is not "derive α from
   shears" but rather: once all internal metric terms are
   set, does the combined Ma-S coupling necessarily equal α?

4. **Shear rationality + α corrections.**  s_e ≈ 2.00420
   is very close to 2; s_ν ≈ 0.02199.  Are the exact shears
   topologically required to be rational (closed geodesics),
   with the deviation from the nearest integer ratio being an
   α-scale perturbative correction?  If s_e = 2 + f(α), that
   eliminates one free parameter.

5. **Sheet scale relationships.**  On a log scale, the
   electron sits at t = 0.6894 of the ν-to-p span — within
   0.55% of ln(2).  The ratio of log-gaps is a/b = 2.2191
   ≈ π/√2 to 0.10%.  Are the three sheet scales related by
   a simple rule?  If so, 3 scale inputs reduce to 2.  No
   theoretical basis yet — needs an idea.

6. **Variational principle on T⁶.**  Is there a functional
   (energy, action, entropy, mode count) whose unique minimum
   selects this T⁶ geometry?  Highest payoff (all parameters
   from one equation) but most speculative — needs a
   theoretical insight we don't currently have.

---

## Nested / warped compactification for sheet scale hierarchy (2026-04-18)

**Context:** The three Ma sheets have vastly different
scales: L_ν ~ μm, L_e ~ pm, L_p ~ fm — a span of roughly
10⁶.  Currently these are three independent scale inputs to
model-E (m_e, m_p, Δm²₂₁).  Could they instead be derived
from one base scale plus a warp factor, in the style of
Randall-Sundrum braneworld hierarchies?

**Proposal:** treat the three sheets as a nested fiber
tower:

    S  ⊃  Ma_ν  ⊃  Ma_e  ⊃  Ma_p

with each Ma factor a warped fiber over the one "above" it
in the tower.  A single warp factor k and one base scale
could, in principle, generate the ~10⁶ scale span.  This
would reduce model-E's dimensional inputs from 3 to 2.

**Empirical hint — adjacency and coupling strength:** The
proposed nesting order ν-e-p places e and p **adjacent** in
the tower and ν and p **non-adjacent**.  Observed cross-
shears: σ_ep = −0.091 is strong (sources the neutron);
σ_νp and σ_eν are weak or zero.  If coupling strength
tracks adjacency in the tower, this matches.  Not proof,
but the pattern is suggestive enough to test.

**Open questions:**

1. Can one base scale plus a single warp factor k
   reproduce L_ν, L_e, L_p to within a few percent?
   (Short arithmetic — feasibility check.)
2. Does warping preserve model-E's particle spectrum?
   Warped geometries lose separation of variables, so the
   spectrum would have to be rebuilt from scratch.
3. Could monodromy in a non-trivial warped bundle turn
   σ_ep into a topologically determined value instead of a
   free parameter?
4. Does non-trivial warping break the entanglement channel
   (see Q82 §2.5) in a detectable way?  If decoherence
   depends on the path particles travel through S, that
   would be a testable signature.

**Triage:** Promote to Q file or study once someone runs
the arithmetic check in (1).  If one warp factor cannot
reproduce the three scales, nesting is probably just a
relabel of the product structure.  If it can, the payoff
(eliminating 2 dimensional inputs) would justify a full
study.  Captured 2026-04-18 from R59-clifford-torus
discussion dialogue.
