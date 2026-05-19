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

> **Current R1 status.** [cand-QY-EL.md](cand-QY-EL.md) satisfies R1 (six distinct pairs). [cand-QY-ED.md](cand-QY-ED.md) **violates** R1 — its electron delta reuses the quark sheet `Ma(4, 5)`. Resolving this is an open architectural question (see cand-QY-EL.md §7).

*(R1 is the only formation rule identified so far. Others may be added as they surface — e.g. rules on which cross-sector dim sharing is admissible, or on closure consistency at shared dims per [architecture.md §3.4 open questions](architecture.md).)*

---

## 3. Notation

- **Dim labels** m1..m_N are size-ordered, smallest first. See [architecture.md §2.1](architecture.md).
- **A 2D sheet** is a dim-pair, written `Ma(i, j)` with i < j. A topology (set of pairs) is `Ma((i,j), (k,l), …)`.
- **Mode-windings** on a pair are `T(m_t, m_r)`. Per [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md) / [architecture.md §3.3.1](architecture.md), closure-satisfying modes are exactly T(1, n) for n ∈ ℤ \ {0}; the two lowest |m_t| = 1 modes per pair are **T(1, 1)** and **T(1, 2)**.
- **Per-pair tube/ring assignment is free** — not fixed by dim size. See [architecture.md §3.1](architecture.md).

---

## 4. Candidate index

| Candidate | Quark | Electron | Neutrino | File | R1 | Status |
|---|:---:|:---:|:---:|---|:---:|---|
| **QY-ED** | QY | ED | open | [cand-QY-ED.md](cand-QY-ED.md) | ✗ violates (`Ma(4,5)` doubled) | quark + electron fit; ν open |
| **QY-EL** | QY | EL | open | [cand-QY-EL.md](cand-QY-EL.md) | ✓ satisfies | quark fit; electron path unfit; ν open |

**Former Candidates A / B / C.** The three candidates previously compared in this file map onto the index above:
- old **B** and **C** were identical in quark + electron (QY + ED) → both subsumed by **QY-ED**; they differed only in the neutrino config (NS vs ND), now an open per-candidate choice.
- old **A** (QY + EL) → **QY-EL**.

**Ladder candidates.** [wye-ladder.md](wye-ladder.md) (QY + EY) and [sym-ladder.md](sym-ladder.md) (QD + EY) are also under consideration but have not yet been converted to the `cand-*.md` format. They will become `cand-QY-EY.md` and `cand-QD-EY.md` when converted; R1 should be checked for each at that time.

---

## 5. Cross-references

- [config-quark.md](config-quark.md), [config-electron.md](config-electron.md), [config-neutrino.md](config-neutrino.md) — per-sector topology configs
- [architecture.md §2.1, §3.1, §3.3.1, §3.4](architecture.md) — dim notation; per-pair tube/ring rule; closure-mode inventory; pair-triplet (σ, τ, P) hypothesis (basis for R1)
- [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md) — closure rule for valid (m_t, m_r) modes
- [scripts/candidate_fits.py](../scripts/candidate_fits.py), [outputs/candidate_fits.txt](../outputs/candidate_fits.txt) — fit driver and numerical output
