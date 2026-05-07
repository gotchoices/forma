/**
 * grid-engine.js — pure data + Scattering update for the GRID lattice.
 *
 * Implements the Scattering model from grid-duality (chapter 4). Each
 * edge has two ends; each end docks into a node, forming a register —
 * a single real-valued scalar at the meeting point of an edge end and
 * a node. All lattice state lives in registers.
 *
 * Reference: ../projects/grid-duality/models/scattering.md
 *            ../projects/grid-duality/scripts/models.py (class Scattering)
 *
 * No DOM, no Three.js. Importable from both the visualizer and a
 * headless test runner.
 *
 * State conventions:
 *   state = { nodes, edges, topology, positions }
 *   nodes[i] = { registers: number[] }   one register per incident edge end
 *   edges[k] = { tail, head, tailSlot, headSlot, displacement }
 *     tailSlot = index in nodes[tail].registers of this edge's tail-end value
 *     headSlot = index in nodes[head].registers of this edge's head-end value
 *     displacement = [dx, dy] — short-image direction tail→head in lattice
 *                    units (always unit length for hex/1D, irrespective of
 *                    whether the edge wraps around a periodic boundary).
 *   positions[i] = [x, y] — node position in lattice coords (unit cell size).
 *                  In 1D, [i, 0]; in 2D hex, the natural xz layout.
 *
 * Each register is owned by exactly one (edge, end) pair, so swapping two
 * edges' end values is safe in place.
 */

const TAU = Math.PI * 2;
const SQRT3 = Math.sqrt(3);

/* ── Topology builders ──────────────────────────────────── */

function makeEmptyState(N, topology) {
  const nodes = [];
  for (let i = 0; i < N; i++) nodes.push({ registers: [] });
  return { nodes, edges: [], topology, positions: new Array(N) };
}

function addEdge(state, tail, head, displacement) {
  const tailSlot = state.nodes[tail].registers.length;
  state.nodes[tail].registers.push(0);
  const headSlot = state.nodes[head].registers.length;
  state.nodes[head].registers.push(0);
  state.edges.push({ tail, head, tailSlot, headSlot, displacement });
}

/**
 * 1D chain of N nodes connected by edges.
 *   open      — N nodes, N-1 edges. Boundary nodes have coordination 1.
 *   periodic  — N nodes, N edges.   Wrap edge connects node N-1 → 0.
 */
export function build1D(N, { periodic = false } = {}) {
  if (N < 2) throw new Error('build1D: N must be at least 2');
  const state = makeEmptyState(N, { kind: '1D', N, periodic });
  for (let i = 0; i < N; i++) state.positions[i] = [i, 0];
  const nEdges = periodic ? N : N - 1;
  for (let i = 0; i < nEdges; i++) addEdge(state, i, (i + 1) % N, [1, 0]);
  return state;
}

/* Hex lattice basis chosen so every A→B edge has unit length. */
const HEX_A1  = [SQRT3, 0];
const HEX_A2  = [SQRT3 / 2, 1.5];
const HEX_DAB = [(HEX_A1[0] + HEX_A2[0]) / 3, (HEX_A1[1] + HEX_A2[1]) / 3];
// edge displacement classes (always unit length):
const HEX_E_SAME  = [HEX_DAB[0], HEX_DAB[1]];                          // A → B(i, j)        (= +d_AB)
const HEX_E_LEFT  = [HEX_DAB[0] - HEX_A1[0], HEX_DAB[1] - HEX_A1[1]];  // A → B(i-1, j)      (= -a₁ + d_AB)
const HEX_E_BELOW = [HEX_DAB[0] - HEX_A2[0], HEX_DAB[1] - HEX_A2[1]];  // A → B(i, j-1)      (= -a₂ + d_AB)

/**
 * 2D hex/wye sheet of nx × ny unit cells. Two sublattices A, B per cell;
 * each A connects to 3 B-neighbors (same cell, left cell, below cell)
 * via three lattice direction classes 120° apart.
 *
 * Independent periodicity per axis:
 *   periodic_x — wrap left↔right (i axis)
 *   periodic_y — wrap top↔bottom (j axis)
 *
 * Coordination is 3 for every interior node and (under full periodic) for
 * every node. Open boundaries reduce to coord 1 or 2 at edge cells.
 */
export function build2D(nx, ny, { periodic_x = false, periodic_y = false } = {}) {
  if (nx < 2 || ny < 2) throw new Error('build2D: nx and ny must be at least 2');
  const wrap = (k, n) => ((k % n) + n) % n;
  const A = (i, j) => 2 * (wrap(j, ny) * nx + wrap(i, nx));
  const B = (i, j) => A(i, j) + 1;

  const N = 2 * nx * ny;
  const state = makeEmptyState(N, { kind: '2D-hex', nx, ny, periodic_x, periodic_y });

  for (let j = 0; j < ny; j++) {
    for (let i = 0; i < nx; i++) {
      const ox = i * HEX_A1[0] + j * HEX_A2[0];
      const oy = i * HEX_A1[1] + j * HEX_A2[1];
      state.positions[A(i, j)] = [ox, oy];
      state.positions[B(i, j)] = [ox + HEX_DAB[0], oy + HEX_DAB[1]];
    }
  }

  for (let j = 0; j < ny; j++) {
    for (let i = 0; i < nx; i++) {
      const tail = A(i, j);
      addEdge(state, tail, B(i,     j),     HEX_E_SAME);
      if (i > 0 || periodic_x) addEdge(state, tail, B(i - 1, j),     HEX_E_LEFT);
      if (j > 0 || periodic_y) addEdge(state, tail, B(i,     j - 1), HEX_E_BELOW);
    }
  }

  return state;
}

/**
 * Y-tree: three linear arms of `armLength` nodes meeting at a central
 * coord-3 hub at index 0. Used for explicit reflection/transmission tests
 * on a single junction.
 */
export function buildYTree(armLength) {
  if (armLength < 1) throw new Error('buildYTree: armLength must be at least 1');
  const N = 3 * armLength + 1;
  const state = makeEmptyState(N, { kind: 'Y-tree', armLength });
  state.positions[0] = [0, 0];
  for (let arm = 0; arm < 3; arm++) {
    const theta = arm * (TAU / 3);
    const dx = Math.cos(theta), dy = Math.sin(theta);
    for (let k = 1; k <= armLength; k++) {
      state.positions[arm * armLength + k] = [k * dx, k * dy];
    }
    const first = arm * armLength + 1;
    const armDisp = [dx, dy];
    addEdge(state, 0, first, armDisp);
    for (let k = 1; k < armLength; k++) {
      addEdge(state, arm * armLength + k, arm * armLength + k + 1, armDisp);
    }
  }
  return state;
}

export function build3D(_nx, _ny, _nz, _opts = {}) {
  throw new Error('build3D: not yet implemented (Step 3 of refactor)');
}

/** True if the engine-coord distance between an edge's endpoints exceeds
 *  ~1.5 lattice units, indicating a wrap-around edge. */
export function isWrapEdge(state, edgeIdx) {
  const e = state.edges[edgeIdx];
  const tp = state.positions[e.tail];
  const hp = state.positions[e.head];
  const dx = hp[0] - tp[0], dy = hp[1] - tp[1];
  return Math.hypot(dx, dy) > 1.5;
}

/* ── State helpers ──────────────────────────────────────── */

export function clear(state) {
  for (const n of state.nodes) {
    for (let i = 0; i < n.registers.length; i++) n.registers[i] = 0;
  }
}

export function coordOf(state, nodeIdx) {
  return state.nodes[nodeIdx].registers.length;
}

/** [tailEndValue, headEndValue] for the given edge. */
export function getEdgeRegisters(state, edgeIdx) {
  const e = state.edges[edgeIdx];
  return [
    state.nodes[e.tail].registers[e.tailSlot],
    state.nodes[e.head].registers[e.headSlot],
  ];
}

export function setEdgeRegister(state, edgeIdx, end, value) {
  const e = state.edges[edgeIdx];
  if (end === 'tail') state.nodes[e.tail].registers[e.tailSlot] = value;
  else if (end === 'head') state.nodes[e.head].registers[e.headSlot] = value;
  else throw new Error(`setEdgeRegister: end must be 'tail' or 'head', got ${end}`);
}

export function setRegister(state, nodeIdx, slot, value) {
  state.nodes[nodeIdx].registers[slot] = value;
}

export function getRegister(state, nodeIdx, slot) {
  return state.nodes[nodeIdx].registers[slot];
}

/** Σ r² over every register. Conserved exactly per full cycle. */
export function totalEnergy(state) {
  let e = 0;
  for (const node of state.nodes) {
    for (const r of node.registers) e += r * r;
  }
  return e;
}

/* ── Update rules: Scattering ───────────────────────────── */

/**
 * Inhale (clock 1 → 0): at each node of coordination N apply
 *   r_i ← (2/N)·(Σ r_j) − r_i
 * the unitary scattering matrix S = (2/N)·J − I.
 */
export function applyInhale(state) {
  for (const node of state.nodes) {
    const N = node.registers.length;
    if (N === 0) continue;
    let total = 0;
    for (let i = 0; i < N; i++) total += node.registers[i];
    const factor = 2 / N;
    for (let i = 0; i < N; i++) {
      node.registers[i] = factor * total - node.registers[i];
    }
  }
}

/**
 * Exhale (clock 0 → 1): for each edge, swap the two register values.
 * Each register is owned by exactly one edge end, so an in-place swap
 * is safe — no register is touched by more than one edge.
 */
export function applyExhale(state) {
  for (const e of state.edges) {
    const t = state.nodes[e.tail].registers;
    const h = state.nodes[e.head].registers;
    const tmp = t[e.tailSlot];
    t[e.tailSlot] = h[e.headSlot];
    h[e.headSlot] = tmp;
  }
}

/**
 * Advance the master clock by one half-step.
 *   clock 0 → 1 fires the exhale (edge swap, yang).
 *   clock 1 → 0 fires the inhale (node scatter, yin).
 * Returns the new clock state.
 *
 * `_config` is accepted for API symmetry; the current model has no tunable
 * config. A future coupling factor will plug in here.
 */
export function halfStep(state, _config, clock) {
  if (clock === 0) { applyExhale(state); return 1; }
  applyInhale(state);
  return 0;
}

/** Advance one full cycle (two half-steps) starting from `clock`. */
export function fullStep(state, config, clock) {
  return halfStep(state, config, halfStep(state, config, clock));
}

/* ── 1D channel helpers ─────────────────────────────────── */

/** Edge whose tail is at this node, or null. (1D outgoing edge.) */
function outgoingEdgeAt(state, nodeIdx) {
  for (const e of state.edges) if (e.tail === nodeIdx) return e;
  return null;
}

/** Edge whose head is at this node, or null. (1D incoming edge.) */
function incomingEdgeAt(state, nodeIdx) {
  for (const e of state.edges) if (e.head === nodeIdx) return e;
  return null;
}

/* ── Presets ─────────────────────────────────────────────── */

/**
 * Delta L: rightward unit pulse seeded at the left end.
 * Sets the tail-end register of the outgoing edge from node 0
 * (= the rightward channel slot at node 0).
 */
function presetDeltaL(state, { amplitude = 30 } = {}) {
  clear(state);
  const e = outgoingEdgeAt(state, 0);
  if (e) state.nodes[e.tail].registers[e.tailSlot] = amplitude;
}

/**
 * Delta R: leftward unit pulse seeded at the right end.
 * Sets the head-end register of the incoming edge at node N-1
 * (= the leftward channel slot at node N-1).
 */
function presetDeltaR(state, { amplitude = 30 } = {}) {
  clear(state);
  const N = state.nodes.length;
  const e = incomingEdgeAt(state, N - 1);
  if (e) state.nodes[e.head].registers[e.headSlot] = amplitude;
}

/** Both Delta L and Delta R simultaneously — pulses meet and pass through. */
function presetDelta2(state, { amplitude = 30 } = {}) {
  clear(state);
  const N = state.nodes.length;
  const eL = outgoingEdgeAt(state, 0);
  if (eL) state.nodes[eL.tail].registers[eL.tailSlot] = amplitude;
  const eR = incomingEdgeAt(state, N - 1);
  if (eR) state.nodes[eR.head].registers[eR.headSlot] = amplitude;
}

/**
 * Sin: right-going traveling sinusoidal eigenmode on the rightward channel.
 * Each node n gets A·sin(2π·n/N) at its outgoing edge's tail-end.
 * On a periodic ring this is an exact eigenmode and propagates one cell
 * per cycle without distortion.
 */
function presetSin(state, { amplitude = 30 } = {}) {
  clear(state);
  const N = state.nodes.length;
  for (let n = 0; n < N; n++) {
    const e = outgoingEdgeAt(state, n);
    if (e) state.nodes[n].registers[e.tailSlot] = amplitude * Math.sin(TAU * n / N);
  }
}

const PRESETS = {
  'delta-L': presetDeltaL,
  'delta-R': presetDeltaR,
  'delta-2': presetDelta2,
  'sin':     presetSin,
};

export function applyPreset(state, name, opts = {}) {
  const fn = PRESETS[name];
  if (!fn) throw new Error(`Unknown preset: ${name}`);
  fn(state, opts);
}

export function listPresets() { return Object.keys(PRESETS); }
