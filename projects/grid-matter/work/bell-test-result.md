# Toy Bell test of the fiber model — structure confirmed, derivation owed

Sim: [`../scripts/bell_test.py`](../scripts/bell_test.py); figure
[`../outputs/bell_test.png`](../outputs/). Model: [measurement-and-bell.md](measurement-and-bell.md).

## Result

Two entangled particles share a fiber phase λ (fixed at creation); each measured at
a free setting. CHSH (classical bound 2, Tsirelson/quantum bound 2√2 ≈ 2.828):

| model | CHSH | no-signaling? |
|---|---|---|
| **local** (shared fiber phase, local outcomes A(a,λ), B(b,λ)) | **2.00** | yes |
| **non-local** (fiber = global condition; correlation depends on a−b) | **2.83** | yes |
| qm reference (E = cos(a−b)) | 2.828 | — |

Correlation curve: **local is a straight-line "triangle"** (the best a local hidden
variable can do); **non-local traces the cosine** and coincides with QM.

## What it establishes

1. **A shared *local* fiber phase is NOT enough** — CHSH = 2, the classical bound.
   The naive "both particles carry the same phase, each measured locally" is a
   *local hidden variable* and Bell caps it at 2. Confirms the worry: locality of
   the phase must be given up.
2. **A *non-local* fiber CAN reach exactly QM — with no signaling.** When the fiber
   is a **global condition** whose outcome correlation depends on *both* settings,
   CHSH = 2√2 and each marginal stays 50/50 (no usable FTL). So the model's
   **structure — non-local + no-signaling — is viable and lands precisely on QM.**
   The fiber is not ruled out; it is in the right class (Bohm-like non-locality).

## The honest limit (do not oversell)

The non-local rule here — P(B=A) = cos²((a−b)/2) — was **put in by hand**. The toy
shows the *structure* works (as, in fairness, any no-signaling non-local model like
Bohm or a PR-box partially does); it does **not derive** the cosine from the
fiber's self-consistency dynamics. That derivation — *why* the fiber's global
constraint yields exactly cos(a−b), no more (signaling) and no less (classical) —
**is the real make-or-break, and it is still open.**

## Net

- **Collapse:** dissolved (real lump = hidden variable).
- **Single-particle Born:** done as consistency — energy density ∝ |ψ|² + whole-
  quantum absorption + linear detection ([born-single-particle.md](born-single-particle.md)).
  It needs *no* non-locality.
- **Bell structure:** confirmed viable — a non-local, no-signaling fiber reaches
  QM exactly; a local one cannot. The model is in the right class.
- **Owed (the one hard core):** the derivation of cos(a−b) from a concrete non-local
  constraint (free settings, no superdeterminism). We need only **one feasible
  placeholder** (e.g. closed/periodic S — global self-consistency via periodic BCs),
  not a single asserted theory. Where forma's *entangled*-Bell claim is won or lost;
  plausibly its own project.
