# Repository Index

Terse map of the repo for quick navigation. See `README.md` for project background.

## Top-level files

| File | Purpose |
|------|---------|
| `README.md` | Project background, goals, guiding principles |
| `AGENTS.md` | Agent ground rules: mission, audience, conventions |
| `STATUS.md` | High-level objectives, results summary, open problems |

## Folders

| Folder | What's in it | Key entry point |
|--------|-------------|-----------------|
| `studies/` | Computational investigations (R1–R37, S1–S3), each self-contained | `studies/STATUS.md` (work queue), `studies/README.md` (workflow) |
| `studies/lib/` | Shared Python code: constants, Ma solver, utilities | `studies/lib/t6.py`, `studies/lib/t6_solver.py` |
| `qa/` | Physics Q&A — answered and open questions (Q05–Q85) | `qa/README.md` (index), `qa/INBOX.md` (capture queue) |
| `papers/` | Authored theory documents (drafts and outlines) | `papers/README.md` |
| `primers/` | Tutorials: matrix notation, Maxwell, KK theory, charge-from-energy | `primers/README.md` |
| `reference/` | External source material and saved conversations | `reference/README.md` |
| `labs/` | Proposed physical experiments to test predictions | `labs/README.md` |
| `viz/` | Interactive browser visualizations | `viz/index.html` |
| `dialogs/` | Saved conversations that informed the project | `dialogs/README.md` |
| `tess/` | Ticket management system (external, git subtree) | `tess/README.md` |
| `tickets/` | Tess ticket pipeline: fix → plan → implement → review → complete | `tess/agent-rules/tickets.md` |
