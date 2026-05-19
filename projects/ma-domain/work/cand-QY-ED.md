# cand-QY-ED.md — consolidated candidate: quark wye + electron delta

**Status:** Active consolidated candidate. Subsumes the quark + electron content of the former Candidates B and C ([candidates.md](candidates.md)), which were identical in those two sectors. The neutrino sector is deliberately left open — see §6.

**Composition:**
- Quark sector — **QY** (quark wye), per [config-quark.md](config-quark.md)
- Electron sector — **ED** (electron delta), per [config-electron.md](config-electron.md)
- Neutrino sector — **open** (any of NS / NC / ND / NY from [config-neutrino.md](config-neutrino.md))

**Goal of this file:** record a single set of compact-dimension sizes on which the required quark and charged-lepton masses all come out in range, with one consolidated topology graph. Fits are computed by [scripts/candidate_fits.py](../scripts/candidate_fits.py); numerical output in [outputs/candidate_fits.txt](../outputs/candidate_fits.txt).

**Notation.** Dim labels m1..m5 are size-ordered, smallest first. A 2D sheet is a dim-pair `Ma(i, j)`. Mode-windings are `T(m_t, m_r)` per [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md): closure-valid modes are T(1, n) for n ∈ ℤ\{0}; the two lowest |m_t|=1 modes per pair are T(1, 1) and T(1, 2).

---

## 1. Consolidated topology

Five compact dimensions, six sheets. Node labels carry the solved dimension sizes; edges are coloured and labelled by the particle class they host (red = quark generation, blue = charged lepton).

```mermaid
%%{init: { "flowchart": { "nodeSpacing": 30, "rankSpacing": 55, "curve": "basis" }, "themeVariables": { "fontSize": "12px" } } }%%
graph LR
    m1["m1<br/>0.007 fm"]
    m2["m2<br/>0.70 fm"]
    m3["m3<br/>0.91 fm"]
    m4["m4<br/>181 fm"]
    m5["m5<br/>5740 fm"]

    %% --- quark wye (red): three rings → common hub m5 ---
    m1 ==>|tb| m5
    m3 ==>|cs| m5
    m4 ==>|ud| m5

    %% --- electron delta (blue): triangle on m2, m4, m5 ---
    m2 ==>|τ| m4
    m2 ==>|μ| m5
    m4 ==>|e| m5

    linkStyle 0,1,2 stroke:red,stroke-width:2px
    linkStyle 3,4,5 stroke:blue,stroke-width:2px
```

Convention: thick `==>` arrows for 2D-torus sheets, drawn ring → tube. The pair `Ma(4, 5)` carries **two** edges — a red `ud` (quark) edge and a blue `e` (electron) edge — because the same dim-pair geometry hosts two different modes (see §5).

- **Quark wye:** hub m5, spokes m1, m3, m4. Three sheets `Ma((1,5), (3,5), (4,5))`.
- **Electron delta:** triangle on m2, m4, m5. Three sheets `Ma((2,4), (2,5), (4,5))`.
- **Shared dims:** m4 and m5 appear in both sectors. m1, m3 are quark-only; m2 is electron-only.

---

## 2. Dimension table

The solved compact-dimension sizes. Five dims total for the quark + electron sectors.

| Dim | L | Sector role | Pinned by |
|---|---:|---|---|
| m1 | 0.007 fm | quark ring — hosts (t, b) | quark fit (t/b within-pair ratio) |
| m2 | 0.70 fm | electron ring — sets τ Compton scale | electron fit (m_τ) |
| m3 | 0.91 fm | quark ring — hosts (c, s) | quark fit (c/s within-pair ratio) |
| m4 | 181 fm | quark ring (u, d) **and** electron tube (τ) / ring (e) | quark fit; reused by electron sector |
| m5 | 5740 fm | quark hub (common tube) **and** electron tube (μ, e) | quark fit (pure-ring floor); reused by electron sector |

Size hierarchy spans ~10⁶ — from m1 at the top-quark Compton scale (0.007 fm) to m5 the "fat" common tube (≳ 5740 fm). The electron sector adds **only one new dim** (m2); it inherits m4 and m5 from the quark wye.

---

## 3. Quark sheets (QY)

The quark wye: hub m5 plays tube in all three sheets, each spoke plays ring. Each sheet hosts one generation — lighter quark at T(1, 2), heavier at T(1, 1) — with the within-pair mass ratio fixing σ_eff via σ_eff = (2R + 1)/(R + 1), R = m_heavier/m_lighter.

| Sheet | Tube | Ring | σ_eff | Lighter T(1,2) | Heavier T(1,1) |
|---|---|---|---:|---|---|
| `Ma(1, 5)` | m5 | m1 (0.007 fm) | 1.976 | b — 4180 MeV | t — 1.73×10⁵ MeV |
| `Ma(3, 5)` | m5 | m3 (0.91 fm) | 1.932 | s — 93 MeV | c — 1270 MeV |
| `Ma(4, 5)` | m5 | m4 (181 fm) | 1.684 | u — 2.17 MeV | d — 4.68 MeV |

**Fit:** max |Δ%| = **0.499%** across all 6 quark masses (u carries nearly all the residual; d, s, c, b, t fit at < 0.2%). Within-generation ratios reproduced: m_d/m_u = 2.17, m_c/m_s = 13.7, m_t/m_b = 41.4. Driver: [scripts/quark_search_wye.py](../scripts/quark_search_wye.py).

The quark sector is self-contained: its four dim sizes and three σ_eff values are fixed by the six quark masses alone, with one residual free parameter (L_5 above its floor).

---

## 4. Electron sheets (ED)

The electron delta: triangle on m2, m4, m5. Each sheet hosts one charged lepton at T(1, 2). The two larger dims m4, m5 are inherited from the quark wye; only m2 is new.

| Sheet | Lepton | Tube | Ring | σ_eff | Mode | Mass |
|---|---|---|---|---:|---|---|
| `Ma(2, 4)` | τ | m4 (181 fm) | m2 (0.70 fm) | 1.000 | T(1, 2) | 1777 MeV |
| `Ma(2, 5)` | μ | m5 (5740 fm) | m2 (0.70 fm) | 1.941 | T(1, 2) | 105.7 MeV |
| `Ma(4, 5)` | e | m5 (5740 fm) | m4 (181 fm) | 1.932 | T(1, 2) | 0.511 MeV |

**Fit:** max |Δ%| = **0.000%** (machine precision on all three lepton masses). Driver: [scripts/candidate_fits.py:electron_delta_fit()](../scripts/candidate_fits.py).

**Residual freedom.** With m4 and m5 inherited from the quark sector, the electron delta has four free continuous parameters (L_2 + three σ_eff) against three lepton masses — **1 residual DOF**. The values above are one self-consistent solution: a uniform "larger-as-tube" convention with τ landing cleanly at σ_eff = 1.000. A different point on the 1-DOF manifold (e.g., τ with m2-as-tube and σ_eff ≈ 1.21) fits equally well; [scripts/candidate_fits.py](../scripts/candidate_fits.py)'s current optimizer run returns one such alternative. The dimension size L_2 ≈ 0.70 fm is robust across the manifold — it is the genuine deliverable; the per-pair σ_eff/tube-ring split is not yet uniquely pinned.

---

## 5. The shared sheet Ma(4, 5)

The dim-pair `Ma(4, 5)` carries **two distinct modes**:

- **Quark `ud`** — u/d generation, T(1, 2)/T(1, 1), σ_eff = 1.684, clover cross-section (lobe/saddle, fractional charge per [sheet-proton clover-quarks](../../sheet-proton/work/clover-quarks.md)).
- **Electron `e`** — electron, T(1, 2), σ_eff = 1.932, ellipse cross-section (convex-only, integer charge per [electron-tube.md](electron-tube.md)).

Same dim sizes (L_4, L_5), same pair geometry — two different cross-section shapes P, two different σ_eff. This is the pair-triplet (σ, τ, P) hypothesis of [architecture.md §3.4](architecture.md) in action: the cross-section shape function P is a property of the *mode*, not of the *pair geometry*. One geometric pair can host modes from different particle classes.

This is the only doubly-occupied sheet in the candidate. m4 and m5 are the two dims shared between the sectors; the sheet that pairs them is the one place a quark mode and a lepton mode coexist on identical geometry.

---

## 6. Neutrino sector — open

This candidate deliberately fixes only the quark and electron sectors. The neutrino sector is left open; any of the configs in [config-neutrino.md](config-neutrino.md) can be attached:

| Option | Adds | Notes |
|---|---|---|
| **NS** — neutrino sheet (2D pair) | 2 fresh dims | sign-flipped modes, ~1% fit; most parsimonious |
| **NC** — neutrino curve (1D substrate) | 1 fresh dim | Q = 0 and Majorana structural; intrinsic-operator fit hits a 6% wall (see config-neutrino.md NC.5–6) |
| **ND** — neutrino delta | 3 fresh dims | machine-precision fit but de-emphasized |
| **NY** — neutrino wye | 4 fresh dims | placeholder, not pursued |

None of the neutrino configs shares dims with the quark or electron sectors (the meV mass scale needs macroscopic dims ≳ 4 cm, incompatible with the fm-scale dims here). So attaching a neutrino config is additive — it appends fresh dims m6+ without disturbing the m1..m5 solution above. The full topology name, once a neutrino config is chosen, would be `cand-QY-ED-Nx.md` (or this file extended with a §-block).

---

## 7. Relation to candidates.md

This file consolidates and replaces the quark + electron content of [candidates.md](candidates.md):

- **Candidate B** (QY + ED + NS) and **Candidate C** (QY + ED + ND) are *identical* in their quark and electron sectors — both are exactly the QY + ED content of this file. They differed only in the neutrino sector, which this file leaves open. So B and C both collapse into `cand-QY-ED.md` + a neutrino choice.
- **Candidate A** (QY + EL + NS) used the electron *linear path* (EL) instead of the delta. EL was never fit and is structurally awkward ([config-electron.md](config-electron.md) EL). A is not carried forward.

candidates.md is retained for now as the historical comparison record; it is slated for deletion once the cand-* files cover all the topologies under consideration.

---

## 8. Cross-references

- [config-quark.md](config-quark.md) — QY config definition (sector-pure topology + DOF)
- [config-electron.md](config-electron.md) — ED config definition
- [config-neutrino.md](config-neutrino.md) — NS / NC / ND / NY options for the open neutrino sector
- [architecture.md §2.1, §3.4](architecture.md) — `Ma(i, j)` notation; pair-triplet (σ, τ, P) hypothesis
- [quark-search.md §9](quark-search.md) — full quark-wye derivation
- [electron-tube.md](electron-tube.md) — the τ = 2 ellipse that puts T(1, 2) at the floor on a lepton sheet
- [scripts/candidate_fits.py](../scripts/candidate_fits.py), [outputs/candidate_fits.txt](../outputs/candidate_fits.txt) — fit driver and numerical output
- [candidates.md](candidates.md) — superseded comparison record (to be deleted)
