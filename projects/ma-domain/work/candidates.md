# candidates.md — candidate formation rules and index

**Status:** Rules for forming ma-domain topology candidates, plus the index of candidates under consideration. Per-candidate detail lives in the individual `cand-*.md` files; per-sector topology options live in the `config-*.md` files. This file holds only what is *general* — not specific to any one candidate.

---

## 1. What a candidate is

A **candidate** is a complete topology for the charged-fermion (and optionally neutrino) sectors of the Ma domain. It is specified by:

- one **quark-sector config** — from [config-quark.md](config-quark.md): QD or QY
- one **electron-sector config** — from [config-electron.md](config-electron.md): ED, EY, or EL
- optionally, one **neutrino-sector config** — from [config-neutrino.md](config-neutrino.md): NS, NC, ND, or NY
- a **mapping** of each config's abstract dims (m_a, m_b, …) onto globally-labelled, size-ordered dims m1..m_N, including any cross-sector dim sharing.

Each candidate is documented in a file named `cand-<Q>-<E>.md` — e.g. [cand-QY-ED.md](cand-QY-ED.md). The neutrino config is omitted from the filename while that sector is held open; it can be appended later. A `cand-*.md` file records the consolidated topology graph, the solved compact-dimension sizes, and the per-sheet mass fits.

---

## 2. Rules for forming a candidate

**R1 — one sheet per dim-pair.** At most one 2D sheet may occupy any dim-pair `Ma(i, j)`. Each pair carries exactly one (σ, τ, P) triplet per [architecture.md §3.4](architecture.md) — one shear, one twist, one cross-section shape — so a pair defines exactly one sheet. If two particles need different cross-sections (a quark clover vs. an electron ellipse, say), they must occupy two *different* dim-pairs. They cannot share one pair with two P-functions; the "P is a property of the mode" reading is not what §3.4 states (§3.4: "the clover is a property of the pair `Ma(i, j)`, not of either dim alone").

> **The R1 rule for QY + ED — share spokes, not the hub.** A quark wye's three sheets are exactly the three *spoke-hub* pairs. An electron delta that reuses a quark **spoke** forms only spoke-spoke or spoke-fresh pairs — none of which is a wye sheet, so R1 holds. An electron delta that reuses the **hub** forms hub-spoke pairs, which *are* wye sheets — collision. So every QY + ED candidate is R1-compliant iff its electron delta shares only spokes. The shareable-spoke count drives a clean family:
>
> | Shared nodes | Electron delta on | Dims | R1 | DOF |
> |---|---|---:|:---:|:---:|
> | 1 spoke | 1 spoke + 2 fresh | 6 | ✓ | 3 |
> | 2 spokes | 2 spokes + 1 fresh | 5 | ✓ | 2 |
> | 3 spokes | the 3 spokes (= complete graph K4) | 4 | ✓ | 1 |
>
> The earlier QY-ED shared the *hub* (m5) and so violated R1; that was a construction error, since corrected (it now shares two spokes).

*(R1 is the only formation rule identified so far. Others may be added as they surface — e.g. rules on which cross-sector dim sharing is admissible, or on closure consistency at shared dims per [architecture.md §3.4 open questions](architecture.md).)*

---

## 3. Notation

- **Dim labels** m1..m_N are size-ordered, smallest first. See [architecture.md §2.1](architecture.md).
- **A 2D sheet** is a dim-pair, written `Ma(i, j)` with i < j. A topology (set of pairs) is `Ma((i,j), (k,l), …)`.
- **Mode-windings** on a pair are `T(m_t, m_r)`. Per [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md) / [architecture.md §3.3.1](architecture.md), closure-satisfying modes are exactly T(1, n) for n ∈ ℤ \ {0}; the two lowest |m_t| = 1 modes per pair are **T(1, 1)** and **T(1, 2)**.
- **Per-pair tube/ring assignment is free** — not fixed by dim size. See [architecture.md §3.1](architecture.md).

---

## 4. Candidate index

All quark+electron fits are at machine precision; the entries below are R1 status, dim count, DOF, and the count of discrete (assignment + tube/ring) combinations that reach a compliant fit (fewer = more predictive). Neutrino sector open for all.

The three QY-ED rows are one **candidate family** — same configs (QY + ED), differing only in how many quark spokes the electron delta reuses — and are written up together in [cand-QY-ED.md](cand-QY-ED.md).

| Candidate | Quark | Electron | Dims | R1 | DOF | Status | File |
|---|:---:|:---:|:---:|:---:|:---:|---|---|
| **QY-ED-share1** | QY | ED (share 1 spoke) | 6 | ✓ | 3 | fit (101 combos) | [cand-QY-ED.md §2](cand-QY-ED.md) |
| **QY-ED** | QY | ED (share 2 spokes) | 5 | ✓ | 2 | fit (27 combos) | [cand-QY-ED.md §3](cand-QY-ED.md) |
| **QY-ED-share3** | QY | ED (share 3 spokes, K4) | **4** | ✓ | **1** | fit (4 combos) | [cand-QY-ED.md §4](cand-QY-ED.md) |
| **QY-EY** | QY | EY (electron wye) | 6 | ✓ | — | solve deferred | [cand-QY-EY.md](cand-QY-EY.md) |
| QY-EL | QY | EL (path) | 5 | ✓ | 2 | fit (23 combos); dominated by QY-ED | [cand-QY-EL.md](cand-QY-EL.md) |
| QD-EY | QD | EY (electron wye) | — | ✓ | — | **not viable** — QD quark sector falsified | [cand-QD-EY.md](cand-QD-EY.md) |

The three QY-ED rows are one **candidate family** (same configs, varying how many quark spokes the electron delta reuses), written up together in [cand-QY-ED.md](cand-QY-ED.md). Quark+electron fits, where run, are at machine precision; the "fit" status gives the count of discrete (assignment + tube/ring) combinations that reach a compliant fit — fewer = more predictive. Neutrino sector open for all.

**QY-ED-share3 (K4) is the standout** — the complete graph on 4 dims, fewest dims, tightest DOF, only 4 compliant combos.

**QY-EL is dominated** by corrected QY-ED (both R1-compliant, 5 dims; QY-ED has the clean delta). **QD-EY is not viable** — its QD quark sector cannot host the six quarks (see cand-QD-EY.md, which also records the compound-3D-mode falsification).

**Former Candidates A / B / C.** old **B** and **C** (QY + ED) → subsumed by the **QY-ED** family; old **A** (QY + EL) → **QY-EL**.

**Former ladder candidates.** "sym-ladder" → **QD-EY**; "wye-ladder" → **QY-EY**. Both are now in `cand-*.md` form; the standalone ladder files have been retired. Their surviving non-topology content — the stable-center / unstable-leg stability mechanism — lives in [mode-stability.md](mode-stability.md).

---

## 5. Cross-references

- [config-quark.md](config-quark.md), [config-electron.md](config-electron.md), [config-neutrino.md](config-neutrino.md) — per-sector topology configs
- [architecture.md §2.1, §3.1, §3.3.1, §3.4](architecture.md) — dim notation; per-pair tube/ring rule; closure-mode inventory; pair-triplet (σ, τ, P) hypothesis (basis for R1)
- [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md) — closure rule for valid (m_t, m_r) modes
- [scripts/cand_solver.py](../scripts/cand_solver.py), [scripts/cand_specs/](../scripts/cand_specs/) — general candidate solver and the per-candidate spec files; each solve writes a report to `outputs/cand_<name>.txt`
