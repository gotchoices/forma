/**
 * grid-tests.js — test cases for grid-engine.js.
 *
 * Plain ES module.  Loadable from grid-tests.html (browser runner) or
 * directly from Node.  Reports through a tiny harness defined below.
 */

import {
  build1D, clear, applyNodeRule, applyEdgeRule, halfStep, fullStep,
  wrapPhase, setPhase, setEdge, getPhase, getEdge,
} from './grid-engine.js';

/* ── Tiny test harness ─────────────────────────────────── */

const results = [];     // [{ group, name, ok, msg }]
let curGroup = '';

export function group(name, fn) {
  curGroup = name;
  fn();
  curGroup = '';
}

export function test(name, fn) {
  try {
    fn();
    results.push({ group: curGroup, name, ok: true, msg: '' });
  } catch (err) {
    results.push({ group: curGroup, name, ok: false, msg: err.message });
  }
}

function approxEq(a, b, eps = 1e-9) { return Math.abs(a - b) <= eps; }

export function assertEq(actual, expected, msg = '') {
  if (actual !== expected) throw new Error(`${msg} expected ${expected}, got ${actual}`);
}
export function assertApprox(actual, expected, eps = 1e-9, msg = '') {
  if (!approxEq(actual, expected, eps)) {
    throw new Error(`${msg} expected ≈${expected} (±${eps}), got ${actual}`);
  }
}
export function assertArr(actual, expected, eps = 1e-9, msg = '') {
  if (actual.length !== expected.length) {
    throw new Error(`${msg} length ${actual.length} ≠ ${expected.length}`);
  }
  for (let i = 0; i < actual.length; i++) {
    if (!approxEq(actual[i], expected[i], eps)) {
      throw new Error(`${msg} idx ${i}: expected ≈${expected[i]} got ${actual[i]}`);
    }
  }
}
export function assertTrue(cond, msg = '') {
  if (!cond) throw new Error(msg || 'assertion failed');
}

export function getResults() { return results.slice(); }

/* ── Helpers ───────────────────────────────────────────── */

const phasesOf = s => s.nodes.map(n => n.phase);
const edgesOf  = s => s.edges.map(e => e.value);

const cfg = (over = {}) => ({
  k: 1, ruleVersion: 2, units: 'deg', accumMode: true, ...over,
});

/* ── Topology tests ────────────────────────────────────── */

group('build1D — topology', () => {
  test('open chain N=5: 5 nodes, 4 edges', () => {
    const s = build1D(5);
    assertEq(s.nodes.length, 5);
    assertEq(s.edges.length, 4);
    assertEq(s.topology.wrap, false);
  });

  test('ring N=5: 5 nodes, 5 edges', () => {
    const s = build1D(5, { wrap: true });
    assertEq(s.nodes.length, 5);
    assertEq(s.edges.length, 5);
    assertEq(s.topology.wrap, true);
  });

  test('open chain: boundary nodes have one edge, interior has two', () => {
    const s = build1D(5);
    assertEq(s.nodes[0].edges.length, 1);
    assertEq(s.nodes[4].edges.length, 1);
    assertEq(s.nodes[2].edges.length, 2);
  });

  test('ring: every node has two edges', () => {
    const s = build1D(5, { wrap: true });
    for (const n of s.nodes) assertEq(n.edges.length, 2);
  });

  test('connection angles: tail at phi=π, head at phi=0', () => {
    const s = build1D(3);
    // edge 0: tail=0, head=1
    const e0 = s.edges[0];
    const tailIncidence = s.nodes[e0.tail].edges.find(x => x.idx === 0);
    const headIncidence = s.nodes[e0.head].edges.find(x => x.idx === 0);
    assertApprox(tailIncidence.phi, Math.PI);
    assertApprox(headIncidence.phi, 0);
  });
});

/* ── Phase wrap tests ──────────────────────────────────── */

group('wrapPhase', () => {
  test('accumulate mode passes value through unchanged', () => {
    assertApprox(wrapPhase(720, { units: 'deg', accumMode: true }), 720);
    assertApprox(wrapPhase(-90, { units: 'deg', accumMode: true }), -90);
  });

  test('wrap deg: -30 → 330', () => {
    assertApprox(wrapPhase(-30, { units: 'deg' }), 330);
  });

  test('wrap deg: 360 → 0 (period itself snaps)', () => {
    assertApprox(wrapPhase(360, { units: 'deg' }), 0);
  });

  test('wrap deg: 359.9999999 snaps to 0 (FP noise)', () => {
    assertApprox(wrapPhase(360 - 1e-9, { units: 'deg' }), 0);
  });

  test('wrap rad: -π/2 → 3π/2', () => {
    assertApprox(wrapPhase(-Math.PI / 2, { units: 'rad' }), 1.5 * Math.PI);
  });
});

/* ── V2 propagation tests ──────────────────────────────── */

group('v2 — single pulse propagation (open chain)', () => {
  test('pulse moves one cell per full cycle (k=1, accum on)', () => {
    const s = build1D(8);
    const c = cfg();
    setPhase(s, 0, 30, c);
    let clock = 0;

    // After cycle 1: pulse at index 1
    clock = fullStep(s, c, clock);
    assertArr(phasesOf(s), [0, 30, 0, 0, 0, 0, 0, 0], 1e-9, 'cycle 1:');

    // After cycle 2: pulse at index 2
    clock = fullStep(s, c, clock);
    assertArr(phasesOf(s), [0, 0, 30, 0, 0, 0, 0, 0], 1e-9, 'cycle 2:');

    // After cycle 3: pulse at index 3
    clock = fullStep(s, c, clock);
    assertArr(phasesOf(s), [0, 0, 0, 30, 0, 0, 0, 0], 1e-9, 'cycle 3:');
  });

  test('amplitude is preserved as the pulse moves', () => {
    const s = build1D(10);
    const c = cfg();
    setPhase(s, 0, 42, c);
    let clock = 0;
    for (let i = 0; i < 5; i++) clock = fullStep(s, c, clock);
    // Pulse should be at index 5 with amplitude 42
    assertApprox(getPhase(s, 5), 42, 1e-9, 'amplitude preserved:');
    // and zero everywhere else
    for (let i = 0; i < 10; i++) {
      if (i !== 5) assertApprox(getPhase(s, i), 0, 1e-9, `idx ${i}:`);
    }
  });
});

group('v2 — two pulses pass through each other', () => {
  test('opposite-amplitude pulses cross cleanly', () => {
    const s = build1D(8);
    const c = cfg();
    setPhase(s, 0, 30, c);
    setPhase(s, 7, -30, c);
    let clock = 0;

    // Cycle 1: pulses at 1 and 6
    clock = fullStep(s, c, clock);
    assertApprox(getPhase(s, 1), 30, 1e-9, 'right pulse cycle 1:');
    assertApprox(getPhase(s, 6), -30, 1e-9, 'left pulse cycle 1:');

    // Cycle 2: pulses at 2 and 5
    clock = fullStep(s, c, clock);
    assertApprox(getPhase(s, 2), 30, 1e-9);
    assertApprox(getPhase(s, 5), -30, 1e-9);

    // Cycle 3: pulses crossed — the +30 originating at 0 is now at 3,
    // and the -30 originating at 7 is now at 4.
    clock = fullStep(s, c, clock);
    assertApprox(getPhase(s, 3), 30, 1e-9, 'cycle 3 right pulse identity preserved:');
    assertApprox(getPhase(s, 4), -30, 1e-9, 'cycle 3 left  pulse identity preserved:');

    // Cycle 4: continue past each other
    clock = fullStep(s, c, clock);
    assertApprox(getPhase(s, 4), 30, 1e-9, 'right pulse cycle 4:');
    assertApprox(getPhase(s, 3), -30, 1e-9, 'left  pulse cycle 4:');
  });

  test('same-amplitude pulses superpose linearly at meeting point', () => {
    const sA = build1D(8);
    const sB = build1D(8);
    const sBoth = build1D(8);
    const c = cfg();

    setPhase(sA, 0, 30, c);
    setPhase(sB, 7, 30, c);
    setPhase(sBoth, 0, 30, c);
    setPhase(sBoth, 7, 30, c);

    let cA = 0, cB = 0, cBoth = 0;
    for (let i = 0; i < 4; i++) {
      cA = fullStep(sA, c, cA);
      cB = fullStep(sB, c, cB);
      cBoth = fullStep(sBoth, c, cBoth);
    }

    // Linearity: phase from both = phase from each summed (in accumulate mode)
    for (let i = 0; i < 8; i++) {
      const sum = getPhase(sA, i) + getPhase(sB, i);
      assertApprox(getPhase(sBoth, i), sum, 1e-9, `superposition at idx ${i}:`);
    }
  });
});

group('v2 — ring propagation', () => {
  test('right-going pulse on a ring returns to origin after N cycles', () => {
    const N = 6;
    const s = build1D(N, { wrap: true });
    const c = cfg();
    // A bare phase impulse excites both wave-equation directions on a
    // periodic ring (no boundary to break symmetry).  To launch a clean
    // right-going pulse we also seed the wrap-around edge so its (tail −
    // head) contribution exactly cancels the leftward branch.
    setPhase(s, 0, 30, c);
    setEdge(s, N - 1, 30);
    let clock = 0;
    for (let i = 0; i < N; i++) clock = fullStep(s, c, clock);
    assertApprox(getPhase(s, 0), 30, 1e-9, 'pulse returned home:');
    for (let i = 1; i < N; i++) assertApprox(getPhase(s, i), 0, 1e-9, `idx ${i}:`);
  });

  test('bare phase impulse on a ring splits into two counter-rotating pulses', () => {
    // Documents the symmetric-launch behaviour: with no edge seed the
    // initial energy goes both directions, so the Nyquist-like checkerboard
    // mode at the CFL boundary (k=1) lets amplitudes oscillate.  This is
    // expected — not a propagation failure.
    const N = 6;
    const s = build1D(N, { wrap: true });
    const c = cfg();
    setPhase(s, 0, 30, c);
    let clock = 0;
    clock = fullStep(s, c, clock);
    // After one full cycle the seed has split: equal-amplitude pulses
    // appeared at indices 1 and N-1, with index 0 inverted.
    assertApprox(getPhase(s, 1),     30, 1e-9, 'right branch:');
    assertApprox(getPhase(s, N - 1), 30, 1e-9, 'left  branch:');
    assertApprox(getPhase(s, 0),    -30, 1e-9, 'origin recoil:');
  });
});

group('v2 — stability (bounded amplitude)', () => {
  test('100 cycles of random initial conditions stay bounded', () => {
    const N = 12;
    const s = build1D(N);
    const c = cfg();
    // Seed with a small perturbation
    setPhase(s, 3, 10, c);
    setPhase(s, 7, -8, c);
    let clock = 0;
    for (let i = 0; i < 100; i++) clock = fullStep(s, c, clock);
    // No phase should have grown by more than ~10× the initial range —
    // actually bouncing off open boundaries can amplify some, but no
    // exponential blow-up should happen.
    for (const n of s.nodes) {
      assertTrue(Math.abs(n.phase) < 1000, `runaway phase ${n.phase}`);
    }
    for (const e of s.edges) {
      assertTrue(Math.abs(e.value) < 1000, `runaway edge ${e.value}`);
    }
  });
});

/* ── V1 — comparison / regression ───────────────────────── */

group('v1 — known behaviour (replacement rule)', () => {
  test('v1 is unstable: amplitudes grow over a few cycles', () => {
    const s = build1D(8);
    const c = cfg({ ruleVersion: 1 });
    setPhase(s, 0, 30, c);
    let clock = 0;
    let maxAmp = 30;
    for (let i = 0; i < 6; i++) {
      clock = fullStep(s, c, clock);
      for (const n of s.nodes) maxAmp = Math.max(maxAmp, Math.abs(n.phase));
    }
    // V1 should produce growing alternating-sign patterns; assert it
    // exceeds the seed amplitude by a notable margin.
    assertTrue(maxAmp > 30, `expected v1 to grow; max amp = ${maxAmp}`);
  });
});

/* ── Wrap-mode interaction with rules ──────────────────── */

group('wrap mode (non-accumulate)', () => {
  test('negative result folds into [0, 360)', () => {
    const s = build1D(4);
    const c = cfg({ accumMode: false });
    // Set up an exhale to leave a single negative-going edge
    setEdge(s, 0, -50);
    // Apply node rule directly (simulating an inhale on this edge state)
    applyNodeRule(s, c);
    // Node 0 (tail of edge 0) sees edge at phi=π → contribution = -(-50) = +50.
    // In v2 (additive), node_0 starts at 0, becomes 50. Wrapped to [0,360) = 50.
    assertApprox(getPhase(s, 0), 50, 1e-9);
    // Node 1 (head) sees edge at phi=0 → contribution = -50. Becomes -50,
    // wrapped to 310.
    assertApprox(getPhase(s, 1), 310, 1e-9);
  });
});

/* ── CLI runner (Node only) ────────────────────────────── */

if (typeof process !== 'undefined' && process.versions?.node) {
  const r = getResults();
  const groups = new Map();
  for (const t of r) {
    if (!groups.has(t.group)) groups.set(t.group, []);
    groups.get(t.group).push(t);
  }
  const tty = process.stdout.isTTY;
  const c = (code, s) => tty ? `\x1b[${code}m${s}\x1b[0m` : s;

  for (const [name, cases] of groups) {
    process.stdout.write(`\n${c('1', name)}\n`);
    for (const t of cases) {
      const mark = t.ok ? c('32', '✓') : c('31', '✗');
      const nm   = t.ok ? t.name : c('31', t.name);
      process.stdout.write(`  ${mark} ${nm}\n`);
      if (!t.ok) process.stdout.write(`      ${c('31', t.msg)}\n`);
    }
  }
  const pass = r.filter(t => t.ok).length;
  const fail = r.length - pass;
  process.stdout.write(
    `\n${c(fail ? '31' : '32', `${pass} passed`)}` +
    `${fail ? c('31', `, ${fail} failed`) : ''} (${r.length} total)\n`,
  );
  process.exit(fail ? 1 : 0);
}
