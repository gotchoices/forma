# Studies

Each subfolder contains a self-contained investigation with its own
documentation and computational work.

**Current priorities:** See [`STATUS.md`](STATUS.md).

## Workflow

```
1. CAPTURE    New idea or question → qa/INBOX.md

2. TRIAGE     Review qa/INBOX.md →
              Quick answer?  → answer inline, mark answered
              Substantial?   → write up as qa/Q<N>-slug.md
              Needs work?    → STATUS.md entry (R<N>) at correct priority
                               Tag question → R<N>
                               If enough substance → create draft study folder

3. PLAN       Flesh out draft study folders as thinking develops
              (README.md = the proposal; theory.md = the math)

4. EXECUTE    Pick top item from STATUS.md "Next" → move to "Active"
              Activate study folder (add findings.md, scripts/, tasks)
              Or write answer in qa/ for non-compute items

5. CLOSE      STATUS.md item → "Done" with link to result
              Study → *(concluded)* in its README.md title
              Spawned new questions? → step 1
```

## Project-Level Files

| File | Job |
|------|-----|
| [`STATUS.md`](./STATUS.md) | Priority-ordered work queue. What to work on next. |
| [`../qa/INBOX.md`](../qa/INBOX.md) | Raw capture log. Questions as they arise. |
| [`../qa/`](../qa/) | Q&A folder — answered and open questions written up individually. |
| `lib/` | Shared code — physical constants, common utilities. |

## Study Folder Convention

Study folders have a lifecycle: **draft → active → concluded**,
shown in the first line of their README.md:

```
# Study Name  *(draft)*
# Study Name  *(active)*
# Study Name  *(concluded)*
```

### Files by lifecycle stage

| File | Draft | Active | Concluded |
|------|-------|--------|-----------|
| `README.md` | Proposal: question, approach, expected outcomes | + Tasks section | + Result summary at top |
| `theory.md` | Framework, math (if ready) | Updated as needed | Final |
| `findings.md` | — | Running log (F1, F2, …) | Final |
| `scripts/` | — | Numbered (`01_`, `02_`, …) | Final |

### Guidelines

- **`theory.md` is slow-moving.** Revise when a finding forces a
  change to hypotheses, framework, or propositions.
- **`findings.md` is the running narrative.** Each entry gets a
  sequential ID (F1, F2, …), names the script, states the result,
  and notes implications.
- **Scripts are self-documenting.** Each script's docstring
  references the `theory.md` section and `findings.md` entry it
  bears on.

### STATUS.md entry format

Each item in `STATUS.md` follows this pattern:

```
### R<N>. <Title>
**Question:** Q<N>  **Type:** reason|research|compute  **Depends on:** —
**Study:** `<folder>/`

One to two sentences: what and why.
```

Resolution types:

| Type | Means | Produces |
|------|-------|----------|
| **research** | Read papers/references | Note in `answers/` or inline |
| **reason** | Algebra or logical derivation | Answer in `answers/` |
| **compute** | Scripts, numerical work | Study folder |

## Concluded Studies (chronological)

1. **`S1-toroid-series/`** — Can a geometric series of nested toroidal
   sub-dimensions correct WvM's ~9% charge deficit? **Null result:**
   the deficit is an artifact of geometric approximations, not a
   robust target for series correction. Spawned `S2-toroid-geometry/`.

2. **`S2-toroid-geometry/`** — What effective geometry reproduces q = e?
   **Algebraic result:** a/R = 1/√(πα) ≈ 6.60 (inverting the WvM
   charge formula). Whether this geometry is physically realized or
   can be derived independently remains open. Spawned `S3-knot-zoo/`.

3. **`S3-knot-zoo/`** — What torus knots model known particles?
   **Demonstrated:** in the Frenet frame model, only (1,2) produces
   charge. **Algebraic:** the WvM formula maps specific a/R values
   to fractional charges. **Hypothesized:** material dimensions,
   mass from photon energy. Raises foundational questions.
