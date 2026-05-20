# cand-QY-ED.md — the QY + ED candidate family (quark wye + electron delta)

**Status:** Active candidate family. Three members, all **R1-compliant**, all fitting the 9 quark + charged-lepton masses at machine precision. Subsumes the quark + electron content of the former Candidates B and C. The neutrino sector is left open for all three — see §6.

**Composition.** Every member is the same config pair: quark sector **QY** (quark wye, [config-quark.md](config-quark.md)) + electron sector **ED** (electron delta, [config-electron.md](config-electron.md)). The members differ in one parameter only:

> **the share count** — how many of the quark wye's three spokes the electron delta reuses as its own nodes.

| Member | Shares | Electron delta on | Dims | DOF |
|---|---|---|---:|---:|
| **QY-ED-share1** | 1 spoke | 1 spoke + 2 fresh dims | 6 | 3 |
| **QY-ED** (canonical) | 2 spokes | 2 spokes + 1 fresh dim | 5 | 2 |
| **QY-ED-share3** | 3 spokes | the 3 spokes (= complete graph K4) | 4 | 1 |

"QY-ED" unqualified means the **share-2** member — the canonical one. Specs: [QY-ED-share1.json](../scripts/cand_specs/QY-ED-share1.json), [QY-ED.json](../scripts/cand_specs/QY-ED.json), [QY-ED-share3.json](../scripts/cand_specs/QY-ED-share3.json). Solver: [scripts/cand_solver.py](../scripts/cand_solver.py); reports `outputs/cand_QY-ED*.txt`.

**Notation.** Dim labels are identifiers, not size-ordered (which dim takes which size is a fit output). A 2D sheet is a dim-pair `Ma(i, j)`. Mode-windings are `T(m_t, m_r)` per [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md): a quark generation puts its lighter quark at T(1, 2) and heavier at T(1, 1); a charged lepton sits at T(1, 2).

---

## 1. The family — shared structure

### 1.1 The quark wye is identical in all three

Every member uses the same quark sector: a wye with a hub dim and three spoke dims, hub plays tube in all three sheets, each spoke plays ring (the fat-torus regime, [config-quark.md](config-quark.md) QY). The three sheets are the three **spoke-hub** pairs; each hosts one quark generation. All six quark masses fit at machine precision.

### 1.2 The electron delta reuses spokes — the family parameter

The electron sector is always a delta (3 nodes, 3 sheets = all pairs among the 3 nodes), each sheet hosting one charged lepton at T(1, 2). What varies is how many of the delta's 3 nodes are quark-wye **spokes** (the rest being fresh electron-only dims): 1, 2, or 3. That share count is the only thing separating the three members.

### 1.3 Why all three satisfy R1 — share spokes, never the hub

[Rule R1](candidates.md) forbids two sheets on one dim-pair. The quark wye's sheets are *exactly* the three spoke-hub pairs. An electron delta built on quark **spokes** forms only spoke-spoke and spoke-fresh pairs — never a spoke-hub pair — so it can never collide with a wye sheet. Hence **every member that shares only spokes is R1-compliant**, for any share count. (Sharing the *hub* instead would force a hub-spoke pair that *is* a wye sheet — that was the bug in the original QY-ED, now corrected.)

### 1.4 The share-count trade

As the share count rises, the electron delta folds more tightly into the quark wye: fewer fresh dims, fewer total dims, tighter DOF, fewer compliant discrete assignments — i.e. **more predictive**. The far end (share 3) is the complete graph K4 on just 4 dims. §5 collects the trend.

---

## 2. QY-ED-share1 — electron delta shares 1 spoke (6 dims)

The electron delta reuses one quark spoke and adds two fresh dims. 6 dims, 6 sheets.

```mermaid
%%{init: { "flowchart": { "nodeSpacing": 28, "rankSpacing": 50, "curve": "basis" }, "themeVariables": { "fontSize": "12px" } } }%%
graph LR
    m1["m1<br/>quark spoke"]
    m3["m3<br/>quark spoke"]
    m4["m4<br/>shared spoke"]
    m5["m5<br/>quark hub"]
    m2["m2<br/>electron dim"]
    m6["m6<br/>electron dim"]

    m1 ==>|u/d| m5
    m3 ==>|b/t| m5
    m4 ==>|s/c| m5
    m2 ===|μ| m4
    m2 ===|e| m6
    m4 ===|τ| m6

    linkStyle 0,1,2 stroke:red,stroke-width:2px
    linkStyle 3,4,5 stroke:blue,stroke-width:2px
```

Quark wye `Ma((1,5),(3,5),(4,5))`; electron delta `Ma((2,4),(2,6),(4,6))`. Only m4 is shared. Edge labels are the solver's best (lowest-error) assignment — **representative**, since 101 discrete combinations reach a compliant fit.

**Result:** R1 satisfied; fit machine-precision; **DOF = 3** (loosest of the family — a 3-parameter solution family). Only one parameter is pinned across the manifold (the smallest quark ring, the b/t ring, ≈ 0.0073 fm); every other dim size and σ_eff ranges. With 101 compliant combos the particle→sheet assignment is barely constrained. Report: [outputs/cand_QY-ED-share1.txt](../outputs/cand_QY-ED-share1.txt).

**Dimension sizes** (solver's best discrete combo; ranges are *sampled* across the solution manifold — indicative, not rigorous bounds):

| Dim | Role in best combo | Solved L |
|---|---|---|
| m1 | u/d quark spoke | ranged [594, 2×10¹⁵] fm |
| m2 | electron dim | ranged [2.4×10³, 2.8×10¹⁰] fm |
| m3 | b/t quark spoke | **pinned ≈ 0.0073 fm** |
| m4 | s/c quark spoke (shared) | ranged [0.91, 1.05] fm |
| m5 | quark hub | ranged [181, 493] fm |
| m6 | electron dim | ranged [0.93, 9.5×10¹⁰] fm |

---

## 3. QY-ED — electron delta shares 2 spokes (5 dims) — the canonical member

The electron delta reuses two quark spokes and adds one fresh dim. 5 dims, 6 sheets. This is "QY-ED" unqualified.

```mermaid
%%{init: { "flowchart": { "nodeSpacing": 28, "rankSpacing": 50, "curve": "basis" }, "themeVariables": { "fontSize": "12px" } } }%%
graph LR
    m1["m1<br/>quark spoke"]
    m5["m5<br/>quark hub"]
    m3["m3<br/>shared spoke"]
    m4["m4<br/>shared spoke"]
    m2["m2<br/>electron dim"]

    m1 ==>|s/c| m5
    m3 ==>|u/d| m5
    m4 ==>|b/t| m5
    m2 ===|e| m3
    m2 ===|τ| m4
    m3 ===|μ| m4

    linkStyle 0,1,2 stroke:red,stroke-width:2px
    linkStyle 3,4,5 stroke:blue,stroke-width:2px
```

Quark wye `Ma((1,5),(3,5),(4,5))`; electron delta `Ma((2,3),(2,4),(3,4))`. Spokes m3, m4 are shared. Edge labels are the solver's best assignment — **representative**, since 27 discrete combinations reach a compliant fit.

**Result:** R1 satisfied; fit machine-precision; **DOF = 2** (a 2-parameter solution family). Three parameters pin across the manifold — the b/t ring (≈ 0.0073 fm) and **two of the three electron σ_eff, both at ≈ 2** (the R53 magic-shear value); the rest range. The R53 σ_eff = 2 pinning is starting to appear here and becomes complete at share 3 (§4). Report: [outputs/cand_QY-ED.txt](../outputs/cand_QY-ED.txt).

**Dimension sizes** (solver's best discrete combo; ranges *sampled* across the manifold — indicative, not rigorous):

| Dim | Role in best combo | Solved L |
|---|---|---|
| m1 | s/c quark spoke | ranged [0.91, 1.05] fm |
| m2 | electron dim | ranged [2.4×10³, 4.4×10¹⁰] fm |
| m3 | u/d quark spoke (shared) | ranged ≳ 578 fm (unbounded above) |
| m4 | b/t quark spoke (shared) | **pinned ≈ 0.0073 fm** |
| m5 | quark hub | ranged [181, 494] fm |

---

## 4. QY-ED-share3 — electron delta shares 3 spokes = the complete graph K4 (4 dims)

The electron delta reuses *all three* quark spokes; no fresh electron dim is needed. 4 dims, 6 sheets. The quark wye is the three spoke-hub edges; the electron delta is the three spoke-spoke edges; together they are **every edge of the complete graph K4** on the 4 dims.

```mermaid
%%{init: { "flowchart": { "nodeSpacing": 30, "rankSpacing": 55, "curve": "basis" }, "themeVariables": { "fontSize": "12px" } } }%%
graph LR
    m1["m1<br/>shared spoke"]
    m2["m2<br/>shared spoke"]
    m3["m3<br/>shared spoke"]
    m4["m4<br/>quark hub"]

    m1 ==>|q| m4
    m2 ==>|q| m4
    m3 ==>|q| m4
    m1 ===|ℓ| m2
    m1 ===|ℓ| m3
    m2 ===|ℓ| m3

    linkStyle 0,1,2 stroke:red,stroke-width:2px
    linkStyle 3,4,5 stroke:blue,stroke-width:2px
```

Quark wye `Ma((1,4),(2,4),(3,4))` (red `q` legs, spoke→hub); electron delta `Ma((1,2),(1,3),(2,3))` (blue `ℓ` legs, spoke–spoke). All three spokes shared. The particle→leg assignment is nearly determined — only 4 discrete combinations fit, collapsing to **two** physically distinct solutions, both graphed in §4.1.

**Result — the standout of the family:**

- R1-compliant **by construction** (K4: each of the 6 dim-pairs carries exactly one sheet).
- Fewest dims (**4**), tightest **DOF = 1** — the most predictive member.
- Only **4 compliant discrete combos** — the topology nearly pins the particle→leg assignment.
- **All three electron σ_eff pin to ≈ 2.0** — the R53 magic-shear value — across the *entire* 1-parameter solution manifold. This is a *structural* output, forced by the topology, not a value the fit was free to choose. It is the "unified R53 mechanism" the wye-ladder analysis hoped for and could not get from an underdetermined fit; K4 produces it because it is so tightly constrained.

Report: [outputs/cand_QY-ED-share3.txt](../outputs/cand_QY-ED-share3.txt).

**Dimension sizes** (solver's best discrete combo; ranges *sampled* across the 1-parameter manifold — indicative, not rigorous):

| Dim | Role in best combo | Solved L |
|---|---|---|
| m1 | u/d quark spoke | ranged [3.9×10³, 1.3×10¹⁵] fm |
| m2 | s/c quark spoke | ranged [0.91, 1.05] fm |
| m3 | b/t quark spoke | **pinned ≈ 0.0073 fm** |
| m4 | quark hub | ranged [181, 493] fm |

(All three electron-leg σ_eff are *pinned* at ≈ 2.0 — the structural result of §4. The three quark-leg σ_eff range.)

### 4.1 The two solutions, and why e sits next to u/d

K4 has exactly **two physically distinct compliant solutions**. The solver's 4 combos are these two, each appearing once more as a spoke-relabelled twin (the three spokes are interchangeable). All fit at exactly machine precision — **the solver does not discriminate between them**.

**The leg geometry.** u/d sits on a quark (wye) leg, which touches one spoke — the *u/d spoke*. The three electron (delta) legs divide by their relation to it:

- **two** delta legs *touch* the u/d spoke — **adjacent** to u/d;
- **one** delta leg connects the *other two* spokes — **opposite** u/d (it shares no dim with u/d's leg).

In every solution **τ occupies the opposite leg** and **e occupies an adjacent leg**. The two solutions are just the two choices of *which* adjacent leg e takes — equivalently, an e ↔ μ swap:

**Solution A** — e on the leg shared with the s/c spoke:

```mermaid
%%{init: { "flowchart": { "nodeSpacing": 30, "rankSpacing": 55, "curve": "basis" }, "themeVariables": { "fontSize": "12px" } } }%%
graph LR
    m1["m1 · u/d spoke"]
    m2["m2 · s/c spoke"]
    m3["m3 · b/t spoke"]
    m4["m4 · hub"]
    m1 ==>|u/d| m4
    m2 ==>|s/c| m4
    m3 ==>|b/t| m4
    m1 ===|e| m2
    m1 ===|μ| m3
    m2 ===|τ| m3
    linkStyle 0,1,2 stroke:red,stroke-width:2px
    linkStyle 3,4,5 stroke:blue,stroke-width:2px
```

**Solution B** — e ↔ μ swapped, e now on the leg shared with the b/t spoke:

```mermaid
%%{init: { "flowchart": { "nodeSpacing": 30, "rankSpacing": 55, "curve": "basis" }, "themeVariables": { "fontSize": "12px" } } }%%
graph LR
    m1["m1 · u/d spoke"]
    m2["m2 · s/c spoke"]
    m3["m3 · b/t spoke"]
    m4["m4 · hub"]
    m1 ==>|u/d| m4
    m2 ==>|s/c| m4
    m3 ==>|b/t| m4
    m1 ===|μ| m2
    m1 ===|e| m3
    m2 ===|τ| m3
    linkStyle 0,1,2 stroke:red,stroke-width:2px
    linkStyle 3,4,5 stroke:blue,stroke-width:2px
```

In both, u/d is on `Ma(m1,m4)` and τ on `Ma(m2,m3)` — the delta leg **opposite** u/d's wye leg. The e ↔ μ swap moves e between the two **adjacent** legs (`Ma(m1,m2)` ↔ `Ma(m1,m3)`); it never reaches the opposite leg.

**Why e cannot take the opposite leg.** A mode of mass *m* needs a hosting dimension L ≳ 2πℏc/m; for the electron (0.511 MeV) that is **L ≳ 2400 fm**. The only dimension that large is the **u/d spoke** — large precisely because u/d is the lightest quark generation. So e's leg *must* touch the u/d spoke. The opposite leg connects the s/c and b/t spokes — both small (heavy quark generations, ~1 fm and ~0.007 fm) — so any lepton there is ≳ 1 GeV. Only τ fits. This holds across the entire DOF = 1 manifold: **"e opposite u/d" has no valid K4 assignment.**

The structural symmetry K4 *does* produce:

> **τ (heaviest lepton) sits opposite u/d (lightest quark generation); e (lightest lepton) is forced adjacent, sharing u/d's large dimension.**

K4 binds the lightest lepton and the lightest quark generation to the same large compact dimension. Discriminating Solution A from Solution B needs an input beyond the charged-fermion masses — the neutrino sector, or decay rates.

### 4.2 Metric-consistency check at the shared spokes

When several sheets share a dimension, what must they agree on? This is the [architecture.md §3.4–§4](architecture.md) open question, and K4 — sharing every spoke across three sheets — is where to test it.

**A dimension carries no shape.** A single compact dimension is a circle; its only geometry is its size L. "Clover" and "ellipse" are not properties of a dimension — shape is curvature, and curvature is a 2-D quantity. A shape belongs to a **sheet**: it is the sectional curvature of that sheet's 2-torus. Twist τ and shear σ, by contrast, are the *constant* part of the pair metric (a flat twisted torus); shape is the position-varying part.

**Shapes of distinct sheets are independent.** Where two sheets meet at a shared dimension — say the quark sheet `Ma(spoke, hub)` and an electron sheet `Ma(spoke, spoke′)` — their shapes are different components of the curvature tensor: the sectional curvatures of two different 2-planes. One geometry carries a clover on the first and an ellipse on the second with no contradiction. The shared dimension contributes only its length L to each sheet.

**So the consistency requirement is just: one size L per dimension.** Every sheet through a dimension winds the same physical circle, so all must use the same L; the twist, shear, and shape are per-sheet. The solver already enforces this — it fits one L per dimension across every sheet that dimension appears in.

**K4 passes.** Its four dimensions each carry a single solved size, used consistently by all sheets through them (§4, §5). Tube vs ring stays a per-sheet label, set by the closure condition ([architecture.md §3.2](architecture.md)); it carries no shape-sharing constraint.

---

## 5. Family comparison

| Property | QY-ED-share1 | QY-ED (share 2) | QY-ED-share3 (K4) |
|---|:---:|:---:|:---:|
| Spokes shared | 1 | 2 | 3 |
| Fresh electron dims | 2 | 1 | 0 |
| Total dims | 6 | 5 | **4** |
| Sheets | 6 | 6 | 6 |
| R1 | ✓ | ✓ | ✓ |
| DOF | 3 | 2 | **1** |
| Compliant discrete combos | 101 | 27 | **4** |
| Quark + lepton fit | machine precision | machine precision | machine precision |
| Electron σ_eff pinned to ≈ 2 | 0 of 3 | 2 of 3 | **3 of 3** |

The family is a clean monotonic ladder: **more sharing → fewer dims → tighter DOF → fewer compliant assignments → more of the electron σ_eff forced to the R53 value**. QY-ED-share3 (K4) sits at the predictive extreme — minimal dims, near-determined assignment, and the R53 σ_eff = 2 mechanism falling out as a structural consequence. It is the most attractive member by every economy / predictivity measure; QY-ED (share 2) is the moderate middle; QY-ED-share1 is the loosest. All three pass the shared-dimension metric-consistency check (§4.2).

---

## 6. Neutrino sector — open (all members)

None of the three fixes the neutrino sector. Any [config-neutrino.md](config-neutrino.md) config — NS, NC, ND, NY — attaches additively on fresh macroscopic dims (the meV ν scale needs dims ≳ 4 cm, incompatible with the fm-scale dims here, so no ν config can collide with the quark or electron pairs). The full topology name, once a ν config is chosen, would be e.g. `cand-QY-ED-share3-Nx`.

---

## 7. Relation to QY-EL and candidates.md

- **Former Candidates B and C** (QY + ED) → subsumed by this family; they differed only in the neutrino config, now open.
- **QY-EL** ([cand-QY-EL.md](cand-QY-EL.md)) is the QY + electron-*path* candidate. It was once "the only R1-compliant quark+electron candidate" — but only against the *broken* hub-sharing QY-ED. Every member of the corrected QY + ED family is R1-compliant with a clean rotationally-symmetric delta, so **the QY-ED family supersedes QY-EL**.
- [candidates.md](candidates.md) holds the candidate-formation rules (R1) and the index.

---

## 8. Cross-references

- [config-quark.md](config-quark.md) — QY config definition
- [config-electron.md](config-electron.md) — ED config definition
- [config-neutrino.md](config-neutrino.md) — NS / NC / ND / NY options for the open neutrino sector
- [candidates.md](candidates.md) — candidate-formation rules (R1) and the candidate index
- [cand-QY-EL.md](cand-QY-EL.md) — the QY + electron-path candidate, superseded by this family
- [architecture.md §2.1, §3.4](architecture.md) — `Ma(i, j)` notation; pair-triplet (σ, τ, P) hypothesis (basis for R1)
- [scripts/cand_solver.py](../scripts/cand_solver.py), [scripts/cand_specs/](../scripts/cand_specs/) — general solver and the three QY-ED spec files
- [outputs/cand_QY-ED-share1.txt](../outputs/cand_QY-ED-share1.txt), [outputs/cand_QY-ED.txt](../outputs/cand_QY-ED.txt), [outputs/cand_QY-ED-share3.txt](../outputs/cand_QY-ED-share3.txt) — solver reports
