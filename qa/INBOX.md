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
