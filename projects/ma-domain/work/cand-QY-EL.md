# cand-QY-EL.md — consolidated candidate: quark wye + electron linear path

**Status:** Documented candidate, quark + electron sectors fully fit. Subsumes the quark + electron content of the former Candidate A ([candidates.md](candidates.md)). The neutrino sector is left open — see §6. The electron linear path is fit by the general solver — see §4.

**Composition:**
- Quark sector — **QY** (quark wye), per [config-quark.md](config-quark.md)
- Electron sector — **EL** (electron linear path), per [config-electron.md](config-electron.md)
- Neutrino sector — **open** (any of NS / NC / ND / NY from [config-neutrino.md](config-neutrino.md))

**Why this candidate is documented despite being awkward.** The electron path has no clean rotational shape. But it has one structural property the cleaner-looking QY-ED candidate lacks: it **satisfies rule R1** (one sheet per dim-pair — see [candidates.md §2](candidates.md)). All six of its dim-pairs are distinct. QY-ED, by contrast, places two sheets on `Ma(4, 5)`. The general solver fits QY-EL to machine precision (§4), so on fit quality it now ties QY-ED; the structural R1 difference is the live distinction. See §5.

**Notation.** Dim labels m1..m5 are size-ordered, smallest first. A 2D sheet is a dim-pair `Ma(i, j)`. Mode-windings are `T(m_t, m_r)` per [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md).

---

## 1. Consolidated topology

Five compact dimensions, six sheets. Node labels carry the dimension sizes; edges are coloured by particle class (red = quark generation, blue = charged lepton). Quark edges are drawn ring → tube (`==>`); the electron-path edges are undirected (`===`) because the path's tube/ring assignment has not been fit.

```mermaid
%%{init: { "flowchart": { "nodeSpacing": 30, "rankSpacing": 55, "curve": "basis" }, "themeVariables": { "fontSize": "12px" } } }%%
graph LR
    m1["m1<br/>0.007 fm"]
    m2["m2<br/>~0.7 fm (est.)"]
    m3["m3<br/>0.91 fm"]
    m4["m4<br/>181 fm"]
    m5["m5<br/>5740 fm"]

    %% --- quark wye (red): three rings → common hub m5 ---
    m1 ==>|tb| m5
    m3 ==>|cs| m5
    m4 ==>|ud| m5

    %% --- electron path (blue): chain m3 — m1 — m2 — m5 ---
    m3 ===|e| m1
    m1 ===|e| m2
    m2 ===|e| m5

    linkStyle 0,1,2 stroke:red,stroke-width:2px
    linkStyle 3,4,5 stroke:blue,stroke-width:2px
```

- **Quark wye:** hub m5, spokes m1, m3, m4. Three sheets `Ma((1,5), (3,5), (4,5))`.
- **Electron path:** chain m3 — m1 — m2 — m5. Three sheets `Ma((1,3), (1,2), (2,5))`.
- **Shared dims:** m1, m3, m5 appear in both sectors. m4 is quark-only; m2 is electron-only.
- **Shared sheets:** *none* — every dim-pair carries exactly one sheet (this is the R1 property; see §5).

---

## 2. Dimension table

| Dim | L | Sector role | Pinned by |
|---|---:|---|---|
| m1 | 0.007 fm | quark ring (t, b); electron-path dim | quark fit |
| m2 | ranged | electron-path dim | joint solve: free direction of the DOF = 2 manifold (§4) |
| m3 | 0.91 fm | quark ring (c, s); electron-path dim | quark fit |
| m4 | 181 fm | quark ring (u, d) | quark fit |
| m5 | 5740 fm | quark hub (common tube); electron-path dim | quark fit |

The sizes above are the canonical quark-wye layout (heaviest generation on the smallest ring). The full joint solve (§4) searches every generation/lepton-to-sheet assignment and is underdetermined at **DOF = 2**, so most dim sizes come out *ranged* rather than pinned — see [outputs/cand_QY-EL.txt](../outputs/cand_QY-EL.txt) for the pinned/ranged breakdown. This table is one reference point on that manifold, not the unique solution.

---

## 3. Quark sheets (QY)

Identical to the quark sector of [cand-QY-ED.md §3](cand-QY-ED.md) — the quark wye is the same in every current candidate.

| Sheet | Tube | Ring | σ_eff | Lighter T(1,2) | Heavier T(1,1) |
|---|---|---|---:|---|---|
| `Ma(1, 5)` | m5 | m1 (0.007 fm) | 1.976 | b — 4180 MeV | t — 1.73×10⁵ MeV |
| `Ma(3, 5)` | m5 | m3 (0.91 fm) | 1.932 | s — 93 MeV | c — 1270 MeV |
| `Ma(4, 5)` | m5 | m4 (181 fm) | 1.684 | u — 2.17 MeV | d — 4.68 MeV |

**Fit:** max |Δ%| = **0.499%** across all 6 quark masses (pure-ring estimate; the joint solve closes the quark sector to machine precision). Driver: [scripts/cand_solver.py](../scripts/cand_solver.py); report [outputs/cand_QY-EL.txt](../outputs/cand_QY-EL.txt).

---

## 4. Electron sheets (EL) — fit

The electron sector is the linear path m3 — m1 — m2 — m5, i.e., the three sheets `Ma(1,3)`, `Ma(1,2)`, `Ma(2,5)`. The general solver [scripts/cand_solver.py](../scripts/cand_solver.py) fits it as part of the joint QY-EL candidate — the chain topology needs no special handling; the solver searches every lepton-to-sheet assignment and tube/ring choice.

**Status: fit, machine precision.** The joint solve closes all 9 quark + lepton masses at **max |Δ%| = 0.0000%** (report [outputs/cand_QY-EL.txt](../outputs/cand_QY-EL.txt)). The path having no rotational symmetry is not an obstacle. The solver finds **23 distinct discrete (assignment + tube/ring) combinations** that each reach a compliant fit.

**Underdetermined at DOF = 2.** The joint candidate has 11 free continuous parameters (5 dim sizes + 6 σ_eff) against 9 mass constraints, so the solution is a 2-parameter family. Across the sampled manifold the solver finds only **one parameter pinned — the smallest quark ring, L ≈ 0.0072 fm** (it hosts the b/t generation); every other dim size and σ_eff ranges over the family. In particular **L[m2] is essentially unconstrained**, ranging over many orders of magnitude. So m2's size is a free direction of the manifold, not a pinned value — the §2 table is one reference point, not the solution.

---

## 5. Rule R1 compliance — the structural point of this candidate

[candidates.md §2](candidates.md) rule **R1** states: at most one 2D sheet per dim-pair.

This candidate's six sheets occupy six **distinct** dim-pairs:

| Sector | Pairs |
|---|---|
| Quark (QY) | `Ma(1,5)`, `Ma(3,5)`, `Ma(4,5)` |
| Electron (EL) | `Ma(1,3)`, `Ma(1,2)`, `Ma(2,5)` |

No pair appears twice. **Candidate QY-EL satisfies R1.**

Contrast with [cand-QY-ED.md](cand-QY-ED.md): the electron *delta* uses pairs `Ma((2,4), (2,5), (4,5))`, and `Ma(4,5)` is also a quark sheet — so QY-ED places two sheets on one pair and **violates R1**.

**Why the path is contorted — and why that is the price of R1.** The quark wye occupies every hub-spoke pair `Ma(i, 5)` for i ∈ {1, 3, 4}. An electron *delta* on three dims drawn from {m1, m3, m4, m5} would inevitably reuse one of those hub-spoke pairs (pigeonhole) — which is exactly what QY-ED's `Ma(4,5)` collision is. To avoid any collision, the electron sheets must use pairs the quark wye does not: ring-ring pairs (`Ma(1,3)`) and pairs involving the fresh dim m2 (`Ma(1,2)`, `Ma(2,5)`). Threading those three pairs into a connected sub-graph forces the linear-chain shape. **The awkward path is not a flaw of taste — it is the geometric consequence of demanding R1 while reusing quark-region dims.**

So the choice between QY-ED and QY-EL is a genuine structural trade:

- **QY-ED** — clean rotationally-symmetric electron delta, fits to machine precision, but violates R1 (one pair doubled).
- **QY-EL** — R1-compliant, fits to machine precision, but the electron sector has no clean rotational shape (the linear path).

Resolving this trade is an open architectural question (see §7).

---

## 6. Neutrino sector — open

As with [cand-QY-ED.md §6](cand-QY-ED.md), the neutrino sector is left open. Any of NS / NC / ND / NY from [config-neutrino.md](config-neutrino.md) can be attached on fresh macroscopic dims m6+, additively, without disturbing the m1..m5 layout above. R1 must be checked for the chosen neutrino config too — but since the ν dims are fresh and pair only among themselves, no ν config can collide with the quark or electron pairs here.

---

## 7. Relation to candidates.md and open questions

This file consolidates the quark + electron content of the former **Candidate A** (QY + EL + single-pair ν). Candidate A was previously deprioritized as "structurally awkward." That judgment stands on shape grounds — but R1 (§5) reframes it: A is the only one of the original three candidates whose quark + electron sectors satisfy the one-sheet-per-pair rule.

**Open questions this raises:**

1. **Is R1 binding?** If R1 is adopted as a hard rule, QY-ED is invalid as written and either (a) QY-EL becomes the working quark+electron candidate, or (b) QY-ED must be reworked so the electron sector avoids the `Ma(4,5)` collision. R1 follows from [architecture.md §3.4](architecture.md) (each pair has one (σ, τ, P) triplet, hence one shape, hence one sheet); the "P is per-mode" reading that would permit two sheets per pair is not what §3.4 states.
2. **QY-EL's electron path fits.** The general solver closes the joint QY-EL candidate at machine precision (DOF = 2, 23 compliant discrete combos; see [outputs/cand_QY-EL.txt](../outputs/cand_QY-EL.txt)). On fit quality QY-EL and QY-ED are now tied — both close exactly. The live distinction is purely structural: QY-EL satisfies R1, QY-ED does not.
3. **Is there an R1-compliant electron topology with a cleaner shape than the path?** A delta is impossible without a collision (pigeonhole, §5). A wye hub at a *fresh* dim might work — an electron wye whose hub is a new dim and whose spokes avoid the quark hub-spoke pairs. Worth checking as a third electron option.

---

## 8. Cross-references

- [config-quark.md](config-quark.md) — QY config definition
- [config-electron.md](config-electron.md) — EL config definition
- [config-neutrino.md](config-neutrino.md) — NS / NC / ND / NY options for the open neutrino sector
- [candidates.md](candidates.md) — candidate formation rules (R1) and the candidate index
- [cand-QY-ED.md](cand-QY-ED.md) — the sibling quark+electron candidate (QY + ED); violates R1
- [architecture.md §3.4](architecture.md) — pair-triplet (σ, τ, P) hypothesis; the basis for R1
- [scripts/cand_solver.py](../scripts/cand_solver.py), [scripts/cand_specs/QY-EL.json](../scripts/cand_specs/QY-EL.json) — general solver and the QY-EL spec
- [outputs/cand_QY-EL.txt](../outputs/cand_QY-EL.txt) — solver report for this candidate
