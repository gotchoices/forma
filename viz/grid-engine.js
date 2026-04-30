/**
 * grid-engine.js — pure data + rule application for the grid lattice.
 *
 * No DOM, no Three.js.  Importable from both the visualizer and a headless
 * test runner.  Higher-dimensional builders (build2D, build3D) will be
 * added later; the rule application code is already topology-agnostic.
 *
 * Conventions:
 *   - A *node* carries a periodic phase (real number, in degrees or radians).
 *   - An *edge* carries a signed magnitude (real number).
 *   - Each node knows its incident edges and the angular position phi at
 *     which each connects (in radians).  In a 1D chain the previous edge
 *     attaches at phi=0 and the next edge at phi=π, per the spec.
 *   - Each edge knows its tail node and head node (a directed segment).
 */

const TAU = Math.PI * 2;

/* ── Topology builders ────────────────────────────────── */

/** Build a 1D linear (or ring, if `wrap`) chain of N nodes. */
export function build1D(N, { wrap = false } = {}) {
  if (N < 2) throw new Error('build1D: N must be at least 2');
  const nodes = [];
  for (let i = 0; i < N; i++) nodes.push({ phase: 0, edges: [] });

  const edges = [];
  const M = wrap ? N : N - 1;
  for (let i = 0; i < M; i++) {
    const tail = i;
    const head = (i + 1) % N;
    edges.push({ value: 0, tail, head });
    // From the tail's perspective, the edge departs at phi=π (the +x point);
    // from the head's perspective it arrives at phi=0 (the -x point).
    nodes[tail].edges.push({ idx: i, phi: Math.PI });
    nodes[head].edges.push({ idx: i, phi: 0 });
  }
  return { nodes, edges, topology: { kind: '1D', N, wrap } };
}

/** Stub.  Will lay out a 2D rectangular lattice with optional periodicity. */
export function build2D(rows, cols, opts = {}) {
  throw new Error('build2D: not yet implemented');
}

/** Stub.  Will lay out a 3D cubic lattice. */
export function build3D(L, M, N, opts = {}) {
  throw new Error('build3D: not yet implemented');
}

/* ── State helpers ────────────────────────────────────── */

/** Reset every node and edge value to zero. */
export function clear(state) {
  for (const n of state.nodes) n.phase = 0;
  for (const e of state.edges) e.value = 0;
}

/** Wrap a phase into [0, period) per the spec's snap rule.  In accumulate
 *  mode, returns the value unchanged. */
export function wrapPhase(v, { units = 'deg', accumMode = false } = {}) {
  if (accumMode) return v;
  const fullTurn = units === 'deg' ? 360 : TAU;
  let p = ((v % fullTurn) + fullTurn) % fullTurn;
  if (fullTurn - p < 1e-6 * fullTurn) p = 0;
  return p;
}

/* ── Update rules ─────────────────────────────────────── */

/**
 * On inhale (clock 1→0): each node integrates the cosine-weighted sum
 * of its incident edge values.  For ruleVersion=2 (Yee additive), the
 * result is added to the current phase; for ruleVersion=1 (replacement),
 * it replaces the phase.  Mutates state.
 */
export function applyNodeRule(state, config) {
  const { k = 1, ruleVersion = 2, units = 'deg', accumMode = false } = config;
  const safeK = Math.max(1e-9, k);
  const next = state.nodes.map(node => {
    let sum = 0;
    for (const ei of node.edges) sum += state.edges[ei.idx].value * Math.cos(ei.phi);
    const inc = sum / safeK;
    const v = ruleVersion === 2 ? node.phase + inc : inc;
    return wrapPhase(v, { units, accumMode });
  });
  for (let i = 0; i < state.nodes.length; i++) state.nodes[i].phase = next[i];
}

/**
 * On exhale (clock 0→1): each edge updates from its endpoint phases.
 *   v1: edge ← (tail + head) · k                       (replacement, sum)
 *   v2: edge ← edge + (tail − head) · k                (Yee additive, gradient)
 * Mutates state.
 */
export function applyEdgeRule(state, config) {
  const { k = 1, ruleVersion = 2 } = config;
  const next = state.edges.map(edge => {
    const tail = state.nodes[edge.tail].phase;
    const head = state.nodes[edge.head].phase;
    if (ruleVersion === 2) return edge.value + (tail - head) * k;
    return (tail + head) * k;
  });
  for (let i = 0; i < state.edges.length; i++) state.edges[i].value = next[i];
}

/**
 * Advance the master clock by one half-step, applying the appropriate
 * rule.  Returns the new clock state.
 *   clock 0 → 1 fires the edge rule (exhale, yang)
 *   clock 1 → 0 fires the node rule (inhale, yin)
 */
export function halfStep(state, config, clock) {
  if (clock === 0) {
    applyEdgeRule(state, config);
    return 1;
  }
  applyNodeRule(state, config);
  return 0;
}

/** Advance two half-steps from `clock` (one full exhale+inhale cycle). */
export function fullStep(state, config, clock) {
  const c1 = halfStep(state, config, clock);
  return halfStep(state, config, c1);
}

/* ── Convenience accessors ────────────────────────────── */

export function getPhase(state, i)  { return state.nodes[i].phase; }
export function getEdge(state, i)   { return state.edges[i].value; }
export function setPhase(state, i, v, config = {}) {
  state.nodes[i].phase = wrapPhase(v, config);
}
export function setEdge(state, i, v) { state.edges[i].value = v; }
