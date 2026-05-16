# CLAUDE.md — ma-6
Rules for AI agents working in this project.

## Project shape

Mirror of [sheet-proton/CLAUDE.md](../sheet-proton/CLAUDE.md) — same script/output discipline applies. This project explores a unifying 6-dim architecture; sheet-proton developed the 2D-sheet clover machinery this project builds on.

## Scripts and outputs: cleanliness rules

```
ma-6/
├── scripts/                    # All production-quality scripts here
├── work/                       # Exploratory markdown work files
└── outputs/                    # All generated artifacts (CSV, PNG, TXT)
```

### Script rules

1. **One script per capability, not per experiment.** Variants go in via CLI flags, not new files.
2. **Parameterize via argparse.** No hard-coded values in script bodies.
3. **No `scripts/lib/` yet.** Most scripts in this project are standalone (e.g., `torus3d_modes.py`, `ma_share_6.py` work without any shared utilities). Create `scripts/lib/` only when a second script genuinely needs to import a non-trivial utility from the first.
4. **Augment, don't fork.** Extend existing scripts with new flags rather than creating `_v2.py`.
5. **No scratch scripts.** REPL or notebook for one-offs; `scripts/` is for reusable code.
6. **Module docstring at the top of every script.** New agents should know in 30 seconds whether the script applies to their task.

### Output rules

1. **Everything generated goes to `outputs/`** — never to `scripts/` or the project root.
2. **Filenames encode parameters.** Example: `ma_share_6_v2_tuned_GeV.csv`. Same script can produce many outputs without overwriting.
3. **No nested directories in `outputs/`.** Keep it flat.
4. **Outputs are disposable.** Regenerate by re-running scripts; don't commit cruft.

## Workflow

1. Develop ideas in `work/*.md`.
2. When numerics are needed, build/extend scripts in `scripts/`.
3. Generated artifacts go to `outputs/`.
4. When a work file's hypothesis converges, write up the result in its own §Results section (don't proliferate `findings*.md` files unless the work file gets too long).
5. The next milestone after coherent preliminary results in `work/` is a mathematical derivation in `ma-6/` proper (top level, not under `work/`) — at that point the file structure may expand.

## Cross-project references

- Inputs from [sheet-proton](../sheet-proton/) (the clover-quarks 1/3-twist mechanism, the R53 / model-F lepton fits) are taken as given.
- Cross-references to sheet-proton files use relative paths from `ma-6/work/`: `../../sheet-proton/work/clover-quarks.md` etc.
- The 9-line-per-entry index `MEMORY.md` convention from sheet-proton/STATUS.md is not used here yet; revisit if the work-file count grows past 5.
