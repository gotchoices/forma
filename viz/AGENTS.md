# viz/

Each visualizer is a single `.html` file using shared code (`totu-viz.css`, `totu-viz.js`). No build step. Three.js **0.163.0** — do not change the version without adjusting all viewers.

Read `README.md` for the full API reference, HTML skeleton, control patterns, and coordinate conventions.

New visualizers should start with a human-facing spec (<visualizer>.md) file explaining the features, methods, approach.
After creating a new visualizer, add a card to `index.html` and an entry to the tools table in `README.md`.

User can run the ./server file and preview/test viewers.
Ask before doing automated (agent-driven) testing.
