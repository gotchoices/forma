# Studies

## Audience
- Assume the reader may not remember facts, figures, conclusions from prior sources, studies

## Framing
- Stay focused on the purpose of the project (../README.md) and the particular study (./README.md)
- Explain how we got here (reference past studies outcomes, findings, open questions, etc)
- Design and lay out the approach of the study (what we hope to do)
- Break the study into separate tracks, phases as appropriate
- Clearly identify and state:
  - Goals: what we are trying to accomplish (theories)
  - Strategy: how we expect to accomplish the goals (equations, models, approaches)
  - Tactics: computational approach to the strategy (scripts, functions, mathematics)

## Findings
- When a study is complete, perform the writeup:
- State the bare results
- Review meaning of variables, terminology where appropriate
- Interpret the results as best possible
- Don't rely on the reader to remember all meanings, implications
- Keep an open mind about possible errors:
  - The study was framed incorrectly
  - The approach was wrong
  - The implementation was wrong
- This means to not be overconfidence about either positive or negative results
- Summarize results in plain language: What does this mean for the study
- Project next possible steps: Where do we go from here

## Repo Management
- The user will typically want to commit at regular milestones:
  - When a new study is framed
  - When a track has be completed or a study is closed
  - New entries entered to the INBOX

## Tracking
- Studies are tracked in ./STATUS.md
- Maintain the file structure as studies progress
  - Acive studies: Short summary
  - Backlog: Intended future studies
  - Done: studies concluded whether positively or negatively
- Inbox tracked in qa/INBOX.md
  - Any questions we can think of that might spawn future studies or analyses
  - Questions that can be answered easily are addressed in a qa/Q*.md
  - More extensive projects become a study
- Scan the INBOX at the end of each study when evaluating possible next subjects to pursue

## Scripts
- Python scripts should use the lib/*.py resources where helpful
- Numpy and others available in the virtual environment

## Nomenclature
- See ./Taxonomy.md
