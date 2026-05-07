/**
 * grid-tests.js — test cases for grid-engine.js (Scattering model).
 *
 * Loadable from grid-tests.html (browser) or directly from Node. Reports
 * through a tiny harness defined below.
 */

import {
  build1D, build2D, buildYTree,
  clear, halfStep, fullStep,
  applyInhale, applyExhale,
  totalEnergy, coordOf, isWrapEdge,
  getEdgeRegisters, setEdgeRegister, setRegister, getRegister,
  applyPreset, listPresets,
} from './grid-engine.js';

/* ── Harness ─────────────────────────────────────────────── */

const results = [];
let curGroup = '';

export function group(name, fn) { curGroup = name; fn(); curGroup = ''; }
export function test(name, fn) {
  try { fn(); results.push({ group: curGroup, name, ok: true,  msg: '' }); }
  catch (err) { results.push({ group: curGroup, name, ok: false, msg: err.message }); }
}
export function getResults() { return results.slice(); }

const approxEq = (a, b, eps = 1e-9) => Math.abs(a - b) <= eps;

export function assertEq(actual, expected, msg = '') {
  if (actual !== expected) throw new Error(`${msg} expected ${expected}, got ${actual}`);
}
export function assertApprox(actual, expected, eps = 1e-9, msg = '') {
  if (!approxEq(actual, expected, eps))
    throw new Error(`${msg} expected ≈${expected} (±${eps}), got ${actual}`);
}
export function assertArr(actual, expected, eps = 1e-9, msg = '') {
  if (actual.length !== expected.length)
    throw new Error(`${msg} length ${actual.length} ≠ ${expected.length}`);
  for (let i = 0; i < actual.length; i++) {
    if (!approxEq(actual[i], expected[i], eps))
      throw new Error(`${msg} idx ${i}: expected ≈${expected[i]} got ${actual[i]}`);
  }
}
export function assertTrue(cond, msg = '') {
  if (!cond) throw new Error(msg || 'assertion failed');
}

/* ── Helpers ─────────────────────────────────────────────── */

const totalRegCount = s =>
  s.nodes.reduce((acc, n) => acc + n.registers.length, 0);

// Run T full cycles. Each cycle = two half-steps. Returns the final clock.
function runCycles(state, T, startClock = 0) {
  let clock = startClock;
  for (let t = 0; t < T; t++) clock = fullStep(state, null, clock);
  return clock;
}

/* ── Topology ────────────────────────────────────────────── */

group('build1D — topology', () => {
  test('open N=5: 5 nodes, 4 edges, no dangling', () => {
    const s = build1D(5);
    assertEq(s.nodes.length, 5);
    assertEq(s.edges.length, 4);
    assertEq(s.topology.periodic, false);
    // Every edge connects two real nodes (no NO_HEAD sentinel).
    for (const e of s.edges) {
      assertTrue(e.tail >= 0 && e.tail < 5, 'tail in range');
      assertTrue(e.head >= 0 && e.head < 5, 'head in range');
    }
  });

  test('periodic N=5: 5 nodes, 5 edges, last wraps', () => {
    const s = build1D(5, { periodic: true });
    assertEq(s.nodes.length, 5);
    assertEq(s.edges.length, 5);
    assertEq(s.topology.periodic, true);
    assertEq(s.edges[4].tail, 4);
    assertEq(s.edges[4].head, 0);
  });

  test('open: boundary nodes have coord 1, interior coord 2', () => {
    const s = build1D(5);
    assertEq(coordOf(s, 0), 1);
    assertEq(coordOf(s, 4), 1);
    for (let i = 1; i < 4; i++) assertEq(coordOf(s, i), 2, `interior ${i}`);
  });

  test('periodic: every node has coord 2', () => {
    const s = build1D(5, { periodic: true });
    for (let i = 0; i < 5; i++) assertEq(coordOf(s, i), 2, `node ${i}`);
  });

  test('total register count = 2 × edges', () => {
    const open = build1D(5);
    assertEq(totalRegCount(open), 2 * open.edges.length);
    const ring = build1D(5, { periodic: true });
    assertEq(totalRegCount(ring), 2 * ring.edges.length);
  });

  test('every (edge, end) maps to a unique (node, slot)', () => {
    const s = build1D(6, { periodic: true });
    const seen = new Set();
    for (const e of s.edges) {
      const tk = `${e.tail}:${e.tailSlot}`;
      const hk = `${e.head}:${e.headSlot}`;
      assertTrue(!seen.has(tk), `duplicate slot ${tk}`);
      assertTrue(!seen.has(hk), `duplicate slot ${hk}`);
      seen.add(tk); seen.add(hk);
    }
    assertEq(seen.size, 2 * s.edges.length);
  });
});

/* ── Update rules ────────────────────────────────────────── */

group('inhale (scatter) S = (2/N)·J − I', () => {
  test('coord 1: S = identity (boundary reflects with no inversion)', () => {
    // Synthetic 1-node lattice with one self-loop-like register (no edge).
    // Easier: build1D(2) open and look at boundary node 0 (coord 1).
    const s = build1D(2);
    s.nodes[0].registers[0] = 7;
    s.nodes[1].registers[0] = -3;
    applyInhale(s);
    // node 0 (coord 1): S=I → unchanged.
    assertApprox(s.nodes[0].registers[0], 7);
    // node 1 (coord 1): unchanged.
    assertApprox(s.nodes[1].registers[0], -3);
  });

  test('coord 2: S = swap', () => {
    const s = build1D(3, { periodic: true });
    // Set node 1 (coord 2) to (a, b)
    s.nodes[1].registers[0] = 5;
    s.nodes[1].registers[1] = 2;
    applyInhale(s);
    // After S = (2/2)J − I = J − I, [a,b] → [b,a].
    assertApprox(s.nodes[1].registers[0], 2);
    assertApprox(s.nodes[1].registers[1], 5);
  });

  test('coord 3: diagonal -1/3, off-diagonal +2/3', () => {
    // Hand-build a coord-3 node and apply inhale directly.
    const node = { registers: [3, 0, 0] };
    const N = 3, total = 3, factor = 2 / N;
    const expected = [factor * total - 3, factor * total - 0, factor * total - 0];
    // = [-1, 2, 2] but those are 3·(diag, off, off) = [-1, 2, 2] ✓
    const s = { nodes: [node], edges: [], topology: { kind: 'synthetic' } };
    applyInhale(s);
    assertArr(s.nodes[0].registers, expected, 1e-12);
    // Verify the canonical diagonal/off-diagonal values directly.
    assertApprox(expected[0], -1);  // 3 · (-1/3)
    assertApprox(expected[1], 2);   // 3 · (2/3)
    assertApprox(expected[2], 2);
  });

  test('coord 4: diagonal -1/2, off-diagonal +1/2', () => {
    const node = { registers: [4, 0, 0, 0] };
    const s = { nodes: [node], edges: [], topology: { kind: 'synthetic' } };
    applyInhale(s);
    assertArr(s.nodes[0].registers, [-2, 2, 2, 2], 1e-12);
  });

  test('inhale is unitary: Σ r² preserved at every node', () => {
    const s = build1D(8, { periodic: true });
    // Random-ish values
    const seed = [3, -1, 2, 0.5, -2.5, 1.1, 4, -0.7];
    for (let i = 0; i < s.nodes.length; i++) {
      s.nodes[i].registers[0] = seed[i];
      s.nodes[i].registers[1] = seed[(i + 3) % 8];
    }
    const before = totalEnergy(s);
    applyInhale(s);
    assertApprox(totalEnergy(s), before, 1e-12, 'energy after inhale:');
  });
});

group('exhale (edge swap)', () => {
  test('exhale swaps the two register values across each edge', () => {
    const s = build1D(3, { periodic: true });
    setEdgeRegister(s, 0, 'tail', 5);
    setEdgeRegister(s, 0, 'head', 11);
    applyExhale(s);
    const [t, h] = getEdgeRegisters(s, 0);
    assertApprox(t, 11);
    assertApprox(h, 5);
  });

  test('exhale is unitary: Σ r² preserved (relabeling only)', () => {
    const s = build1D(6, { periodic: true });
    for (let i = 0; i < s.edges.length; i++) {
      setEdgeRegister(s, i, 'tail', i + 1);
      setEdgeRegister(s, i, 'head', -(i + 1) * 0.5);
    }
    const before = totalEnergy(s);
    applyExhale(s);
    assertApprox(totalEnergy(s), before, 1e-12, 'energy after exhale:');
  });

  test('two exhales = identity', () => {
    const s = build1D(4, { periodic: true });
    s.nodes[0].registers[0] = 7;
    s.nodes[2].registers[1] = -3;
    const snapshot = s.nodes.map(n => [...n.registers]);
    applyExhale(s); applyExhale(s);
    for (let i = 0; i < s.nodes.length; i++) assertArr(s.nodes[i].registers, snapshot[i]);
  });
});

/* ── Energy conservation ─────────────────────────────────── */

group('global energy conservation', () => {
  test('open chain N=8: energy preserved over 50 cycles', () => {
    const s = build1D(8);
    s.nodes[0].registers[0] = 1.7;     // a single seed
    const E0 = totalEnergy(s);
    runCycles(s, 50);
    assertApprox(totalEnergy(s), E0, 1e-10);
  });

  test('periodic ring N=12: energy preserved over 100 cycles', () => {
    const s = build1D(12, { periodic: true });
    applyPreset(s, 'sin', { amplitude: 5 });
    const E0 = totalEnergy(s);
    runCycles(s, 100);
    assertApprox(totalEnergy(s), E0, 1e-9);
  });
});

/* ── 1D pulse propagation (periodic) ─────────────────────── */

group('rightward pulse on periodic ring (delta-L)', () => {
  test('pulse moves one cell per cycle and returns home after N', () => {
    const N = 8;
    const s = build1D(N, { periodic: true });
    applyPreset(s, 'delta-L', { amplitude: 1 });
    const E0 = totalEnergy(s);
    assertApprox(E0, 1, 1e-12, 'unit amplitude → unit energy');
    runCycles(s, N);
    // After N cycles, the rightward channel should be back at node 0's
    // outgoing-tail register. By assertion: presetDeltaL puts the value
    // there, so applying delta-L again and comparing register-by-register
    // gives the cleanest check.
    const ref = build1D(N, { periodic: true });
    applyPreset(ref, 'delta-L', { amplitude: 1 });
    for (let i = 0; i < s.nodes.length; i++) {
      assertArr(s.nodes[i].registers, ref.nodes[i].registers, 1e-12, `node ${i} after N cycles:`);
    }
  });

  test('after T cycles the pulse is on edge T-1 or T (1 cell/cycle)', () => {
    const N = 8;
    const s = build1D(N, { periodic: true });
    applyPreset(s, 'delta-L', { amplitude: 1 });
    runCycles(s, 3);
    // After 3 full cycles, energy should be concentrated near edge 2 (index).
    // We verify by integrating |register|² over each "edge-half" pair and
    // confirming the maximum is at some edge between 2 and 3.
    let maxIdx = -1, maxE = -1;
    for (let i = 0; i < s.edges.length; i++) {
      const [t, h] = getEdgeRegisters(s, i);
      const e = t * t + h * h;
      if (e > maxE) { maxE = e; maxIdx = i; }
    }
    // For a pulse at "node 3 slot 1 (= tail-of-e3)" (cycle 3 ending state),
    // the most energetic edge is e3 (= edge index 3).
    // Slight off-by-one possible depending on which edge holds the parking
    // register; accept either 2 or 3.
    assertTrue(maxIdx === 2 || maxIdx === 3, `expected pulse near edge 2/3, found at ${maxIdx}`);
  });
});

group('leftward pulse on periodic ring (delta-R)', () => {
  test('pulse returns home after N cycles', () => {
    const N = 6;
    const s = build1D(N, { periodic: true });
    applyPreset(s, 'delta-R', { amplitude: 1 });
    runCycles(s, N);
    const ref = build1D(N, { periodic: true });
    applyPreset(ref, 'delta-R', { amplitude: 1 });
    for (let i = 0; i < N; i++) {
      assertArr(s.nodes[i].registers, ref.nodes[i].registers, 1e-12, `node ${i}:`);
    }
  });
});

group('two pulses pass through each other (delta-2)', () => {
  test('amplitudes preserved through the crossing', () => {
    const N = 8;
    const s = build1D(N, { periodic: true });
    applyPreset(s, 'delta-2', { amplitude: 1 });
    const E0 = totalEnergy(s);
    assertApprox(E0, 2, 1e-12, 'two unit pulses → energy 2');
    runCycles(s, 6);   // past the meeting point
    assertApprox(totalEnergy(s), 2, 1e-10, 'energy preserved across crossing');
  });

  test('linearity: delta-2 = delta-L + delta-R after T cycles', () => {
    const N = 8, T = 5;
    const sL = build1D(N, { periodic: true });
    const sR = build1D(N, { periodic: true });
    const sBoth = build1D(N, { periodic: true });
    applyPreset(sL, 'delta-L', { amplitude: 1 });
    applyPreset(sR, 'delta-R', { amplitude: 1 });
    applyPreset(sBoth, 'delta-2', { amplitude: 1 });
    runCycles(sL, T); runCycles(sR, T); runCycles(sBoth, T);
    for (let n = 0; n < N; n++) {
      const a = sL.nodes[n].registers;
      const b = sR.nodes[n].registers;
      const c = sBoth.nodes[n].registers;
      for (let s = 0; s < a.length; s++) {
        assertApprox(c[s], a[s] + b[s], 1e-12, `node ${n} slot ${s}:`);
      }
    }
  });
});

group('sin preset eigenmode', () => {
  test('periodic ring: shape preserved after N cycles', () => {
    const N = 8;
    const s = build1D(N, { periodic: true });
    applyPreset(s, 'sin', { amplitude: 3 });
    const snapshot = s.nodes.map(n => [...n.registers]);
    runCycles(s, N);
    for (let n = 0; n < N; n++) {
      assertArr(s.nodes[n].registers, snapshot[n], 1e-9, `node ${n}:`);
    }
  });

  test('one-cell shift after one cycle', () => {
    const N = 8;
    const s = build1D(N, { periodic: true });
    applyPreset(s, 'sin', { amplitude: 1 });
    const before = s.nodes.map(n => [...n.registers]);
    runCycles(s, 1);
    // After one cycle, the value previously at node n's rightward slot is
    // now at node (n+1) % N's rightward slot. The "rightward slot" at node n
    // is the tailSlot of the edge with tail = n.
    const slotOf = n => {
      for (const e of s.edges) if (e.tail === n) return e.tailSlot;
      return -1;
    };
    for (let n = 0; n < N; n++) {
      const next = (n + 1) % N;
      assertApprox(
        s.nodes[next].registers[slotOf(next)],
        before[n][slotOf(n)],
        1e-9,
        `right channel at node ${next} after shift from ${n}:`,
      );
    }
  });
});

/* ── Open-chain reflection ───────────────────────────────── */

group('open-chain boundary reflection', () => {
  test('right pulse hits coord-1 boundary and reflects (no inversion)', () => {
    const N = 6;
    const s = build1D(N);   // open chain
    applyPreset(s, 'delta-L', { amplitude: 1 });
    // After N-1 cycles the pulse should have reached node N-1.
    // S=identity at coord 1 means it sits there for one inhale, then reflects.
    // After 2(N-1) cycles it should be back at node 0.
    const E0 = totalEnergy(s);
    runCycles(s, 2 * (N - 1));
    assertApprox(totalEnergy(s), E0, 1e-10, 'energy preserved during reflection');
    // The reflected pulse should now be at node 0 with positive sign
    // (no inversion, since S diag at coord 1 = +1).
    const e0 = s.edges[0];
    const tailEnd = s.nodes[e0.tail].registers[e0.tailSlot];
    assertApprox(tailEnd, 1, 1e-10, 'returned amplitude (no sign flip):');
  });
});

/* ── Presets sanity ──────────────────────────────────────── */

group('presets', () => {
  test('listPresets returns the four documented names', () => {
    const names = listPresets();
    assertTrue(names.includes('delta-L'));
    assertTrue(names.includes('delta-R'));
    assertTrue(names.includes('delta-2'));
    assertTrue(names.includes('sin'));
  });

  test('clear zeros every register', () => {
    const s = build1D(6, { periodic: true });
    applyPreset(s, 'sin', { amplitude: 5 });
    clear(s);
    for (const n of s.nodes) for (const r of n.registers) assertApprox(r, 0);
  });
});

/* ── 2D hex/wye topology ─────────────────────────────────── */

group('build2D — hex/wye topology', () => {
  test('2×2 fully periodic: 8 nodes, 12 edges, all coord 3', () => {
    const s = build2D(2, 2, { periodic_x: true, periodic_y: true });
    assertEq(s.nodes.length, 8);
    assertEq(s.edges.length, 12);
    for (let i = 0; i < 8; i++) assertEq(coordOf(s, i), 3, `node ${i}:`);
  });

  test('3×3 fully periodic: 18 nodes, 27 edges', () => {
    const s = build2D(3, 3, { periodic_x: true, periodic_y: true });
    assertEq(s.nodes.length, 18);
    assertEq(s.edges.length, 27);   // 3 edges per cell × 9 cells
  });

  test('2×2 open: 8 nodes, 8 edges; boundary nodes have lower coord', () => {
    const s = build2D(2, 2);
    assertEq(s.nodes.length, 8);
    // Same-cell A→B: 4 edges (one per cell, always present).
    // Left A→B (i>0): i=1 only, j=0,1 → 2 edges.
    // Below A→B (j>0): j=1 only, i=0,1 → 2 edges.
    // Total 8.
    assertEq(s.edges.length, 8);
    // At least one node should have coord < 3 (boundary effect).
    let minCoord = 99;
    for (let i = 0; i < s.nodes.length; i++) minCoord = Math.min(minCoord, coordOf(s, i));
    assertTrue(minCoord < 3, `expected some boundary node coord < 3, got minCoord ${minCoord}`);
  });

  test('every edge has unit displacement length (hex)', () => {
    const s = build2D(3, 3, { periodic_x: true, periodic_y: true });
    for (const e of s.edges) {
      const len = Math.hypot(e.displacement[0], e.displacement[1]);
      assertApprox(len, 1.0, 1e-12, `edge displacement:`);
    }
  });

  test('isWrapEdge detects wraps correctly', () => {
    const s = build2D(3, 3, { periodic_x: true, periodic_y: true });
    let wrapCount = 0;
    for (let i = 0; i < s.edges.length; i++) if (isWrapEdge(s, i)) wrapCount++;
    // Each periodic axis contributes wraps along its boundary cells.
    // For 3×3 with both axes periodic, expect wrapCount > 0.
    assertTrue(wrapCount > 0, 'no wrap edges detected on fully periodic 3×3');
    // For non-wrap edges, the engine-position distance equals the
    // displacement length (1.0).
    for (let i = 0; i < s.edges.length; i++) {
      if (isWrapEdge(s, i)) continue;
      const e = s.edges[i];
      const tp = s.positions[e.tail], hp = s.positions[e.head];
      const dist = Math.hypot(hp[0] - tp[0], hp[1] - tp[1]);
      assertApprox(dist, 1.0, 1e-12, `non-wrap edge ${i}:`);
    }
  });

  test('partial periodic: y-only wraps along j axis', () => {
    const s = build2D(3, 3, { periodic_x: false, periodic_y: true });
    // A(0, j) has no left-cell edge for any j (x not periodic).
    // A(i, 0) has a below-cell edge that wraps to j = ny-1 (y is periodic).
    // Expected edges: same-cell 9 + left-cell (i>=1, j=0,1,2) = 6 + below-cell (j>=1 OR periodic_y) = 9 = 24.
    assertEq(s.edges.length, 24);
  });
});

/* ── Y-junction scattering at coord 3 ────────────────────── */

group('Y-junction scattering S = (2/3)·J − I', () => {
  test('hub register {1, 0, 0} after inhale → {−1/3, +2/3, +2/3}', () => {
    const s = buildYTree(2);
    s.nodes[0].registers[0] = 1.0;
    applyInhale(s);
    assertApprox(s.nodes[0].registers[0], -1/3, 1e-12, 'reflection R:');
    assertApprox(s.nodes[0].registers[1],  2/3, 1e-12, 'T arm 1:');
    assertApprox(s.nodes[0].registers[2],  2/3, 1e-12, 'T arm 2:');
    // Energy preservation: R² + 2T² = 1/9 + 8/9 = 1
    const E = s.nodes[0].registers.reduce((acc, r) => acc + r*r, 0);
    assertApprox(E, 1.0, 1e-12, 'scattered energy:');
  });

  test('inhale-then-exhale: scattered values land at first arm nodes', () => {
    // Seed arrives at the hub (in the arm-0 register) and then scatters.
    // The natural order is inhale-first (scatter), then exhale (propagate
    // the scattered values out along each arm). fullStep() starts with
    // exhale, so we drive inhale + exhale directly here.
    const armLength = 3;
    const s = buildYTree(armLength);
    s.nodes[0].registers[0] = 1.0;
    applyInhale(s);
    applyExhale(s);
    // After scattering: hub is all zero, first nodes of each arm hold
    // R = −1/3 (arm 0) and T = +2/3 (arms 1, 2).
    assertApprox(s.nodes[1].registers[0], -1/3, 1e-12, 'arm 0 first node:');
    const arm1First = 1 + armLength;
    const arm2First = 1 + 2 * armLength;
    assertApprox(s.nodes[arm1First].registers[0], 2/3, 1e-12, 'arm 1 first node:');
    assertApprox(s.nodes[arm2First].registers[0], 2/3, 1e-12, 'arm 2 first node:');
    // Hub fully evacuated.
    for (let k = 0; k < 3; k++) assertApprox(s.nodes[0].registers[k], 0, 1e-12);
  });
});

/* ── 2D energy conservation ──────────────────────────────── */

group('2D energy conservation', () => {
  test('hex torus 3×3: energy preserved over 50 cycles', () => {
    const s = build2D(3, 3, { periodic_x: true, periodic_y: true });
    // Seed every register with a deterministic-ish nonzero pattern.
    let seed = 0;
    for (const n of s.nodes) {
      for (let k = 0; k < n.registers.length; k++) {
        n.registers[k] = Math.sin(0.7 * (++seed)) * 2.0;
      }
    }
    const E0 = totalEnergy(s);
    let clock = 0;
    for (let t = 0; t < 50; t++) clock = fullStep(s, null, clock);
    assertApprox(totalEnergy(s), E0, 1e-9);
  });

  test('open hex 3×3: energy preserved over 50 cycles (mixed coordinations)', () => {
    const s = build2D(3, 3);
    let seed = 0;
    for (const n of s.nodes) {
      for (let k = 0; k < n.registers.length; k++) {
        n.registers[k] = Math.cos(0.5 * (++seed));
      }
    }
    const E0 = totalEnergy(s);
    let clock = 0;
    for (let t = 0; t < 50; t++) clock = fullStep(s, null, clock);
    assertApprox(totalEnergy(s), E0, 1e-9);
  });
});

/* ── 2D linearity ────────────────────────────────────────── */

group('2D linearity', () => {
  test('hex torus 3×3: A + B = AB after 5 cycles', () => {
    const mkLat = () => build2D(3, 3, { periodic_x: true, periodic_y: true });
    const sA = mkLat(), sB = mkLat(), sAB = mkLat();
    sA.nodes[0].registers[0] = 1.0;
    sB.nodes[5].registers[1] = -2.0;   // separate non-overlapping seed
    sAB.nodes[0].registers[0] = 1.0;
    sAB.nodes[5].registers[1] = -2.0;
    let cA = 0, cB = 0, cAB = 0;
    for (let t = 0; t < 5; t++) {
      cA  = fullStep(sA, null, cA);
      cB  = fullStep(sB, null, cB);
      cAB = fullStep(sAB, null, cAB);
    }
    for (let n = 0; n < sA.nodes.length; n++) {
      const ra = sA.nodes[n].registers, rb = sB.nodes[n].registers, rab = sAB.nodes[n].registers;
      for (let s = 0; s < ra.length; s++) {
        assertApprox(rab[s], ra[s] + rb[s], 1e-12, `node ${n} slot ${s}:`);
      }
    }
  });
});

/* ── CLI runner (Node only) ──────────────────────────────── */

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
