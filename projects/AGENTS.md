# AGENTS.md
Rules for AI agents working in projects.

## General Organization
- Preferred approach for projects is a mathematical derivation
- If we lack insight into how to do that, we can divert to computational analysis first, then return to derivations
- If the roadmap is clear for a project:
  - start with a project arc in README, listing chapter roles
  - outline one chapter at a time
  - develop the chapter
  - submit to review, refinements
  - evaluate if the next chapters still follow as outlined
  - iterate
- If things are unclear, develop working hypotheses in a work folder
- If/when models need verification, scripts can be built
- When the roadmap is complex, track todo's in a project STATUS.md file

## Scripts and outputs
- Keep the folders tidy/clean:
  - Keep an 'outputs' folder for script artifacts
  - Not every script needs durable outputs
  - Retain data outputs that demonstrate material or conclusive findings
  - Generate visual graphs when the outputs are helpful for human review, understanding

- Principles for scripting
  - **One script per capability, not per experiment.** Augment scripts where possible to add new capabilities rather than leaving a trail of multiple, similar scripts.
  - **Parameterize via argparse.** Scripts accept their parameters via command-line. No hard-coded values in script bodies (use defaults in `argparse.add_argument(..., default=...)`).
  - **Document each script's purpose at the top.** Module docstring should state: what it does, what inputs it takes, what outputs it produces. A new agent reading the file should know in 30 seconds whether the script applies to their task.
  - **Delete superseded scripts.** When a script is replaced by a better version, delete the old one. Don't leave commented-out code blocks or "// TODO: remove" notes.
