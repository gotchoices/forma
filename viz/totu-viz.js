/**
 * totu-viz.js — shared utilities for totu visualizers.
 * ES module. Import what you need:
 *   import { createScene, buildTorusGeom, ... } from './totu-viz.js';
 */

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

export { THREE, OrbitControls };

export const THREE_VERSION = '0.163.0';

export const PALETTE = {
  bg:      0x0e0e12,
  surface: 0x4fc3f7,
  path:    0xff6e40,
  photon:  0xfdd835,
  green:   0x66bb6a,
  blue:    0x50b0e0,
  red:     0xe05050,
  purple:  0xab47bc,
};

/* ── Scene setup ──────────────────────────────────────── */

export function createScene(container, opts = {}) {
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(opts.bg ?? PALETTE.bg);

  const camera = new THREE.PerspectiveCamera(
    opts.fov ?? 45,
    container.clientWidth / container.clientHeight,
    opts.near ?? 0.01, opts.far ?? 200
  );
  camera.position.set(...(opts.camPos ?? [2.5, 1.8, 3.5]));

  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.setSize(container.clientWidth, container.clientHeight);
  container.appendChild(renderer.domElement);

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = opts.damping ?? 0.07;
  if (opts.maxDistance) controls.maxDistance = opts.maxDistance;

  scene.add(new THREE.AmbientLight(0x606070, 1.5));
  const sun = new THREE.DirectionalLight(0xffffff, 1.2);
  sun.position.set(4, 6, 5);
  scene.add(sun);
  if (opts.fillLight !== false) {
    const fill = new THREE.DirectionalLight(0x6688cc, 0.4);
    fill.position.set(-3, -2, -3);
    scene.add(fill);
  }

  return { scene, camera, renderer, controls, clock: new THREE.Clock() };
}

export function autoResize(renderer, camera, container) {
  const fn = () => {
    const w = container.clientWidth, h = container.clientHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  };
  window.addEventListener('resize', fn);
  fn();
  return () => window.removeEventListener('resize', fn);
}

export function animLoop(tick, { renderer, scene, camera, controls }) {
  let on = true;
  (function loop() {
    if (!on) return;
    requestAnimationFrame(loop);
    controls.update();
    tick();
    renderer.render(scene, camera);
  })();
  return () => { on = false; };
}

/* ── Torus geometry ───────────────────────────────────── */

export function buildTorusGeom(R, a, segU = 64, segV = 128) {
  const pos = [], idx = [];
  for (let i = 0; i <= segU; i++) {
    const th = (i / segU) * 2 * Math.PI;
    const ct = Math.cos(th), st = Math.sin(th);
    for (let j = 0; j <= segV; j++) {
      const ph = (j / segV) * 2 * Math.PI;
      const rr = R + a * ct;
      pos.push(rr * Math.cos(ph), a * st, rr * Math.sin(ph));
    }
  }
  for (let i = 0; i < segU; i++)
    for (let j = 0; j < segV; j++) {
      const a_ = i * (segV + 1) + j, b_ = a_ + segV + 1;
      idx.push(a_, b_, a_ + 1, b_, b_ + 1, a_ + 1);
    }
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setIndex(idx);
  g.computeVertexNormals();
  return g;
}

/** Point on the (p,q) geodesic at parameter t. Torus in XZ plane, axis Y. */
export function torusPt(t, R, a, p, q) {
  const th = p * t, ph = q * t;
  const rr = R + a * Math.cos(th);
  return new THREE.Vector3(rr * Math.cos(ph), a * Math.sin(th), rr * Math.sin(ph));
}

/** Tube geometry for a (p,q) geodesic path. */
export function torusPathGeom(R, a, p, q, opts = {}) {
  const n = opts.segments ?? 800;
  const tot = 2 * Math.PI * (opts.periods ?? q);
  const pts = [];
  for (let i = 0; i <= n; i++)
    pts.push(torusPt((i / n) * tot, R, a, p, q));
  const curve = new THREE.CatmullRomCurve3(pts, opts.closed ?? true);
  return new THREE.TubeGeometry(curve, n, opts.tubeR ?? 0.02, 6, opts.closed ?? true);
}

/* ── Common objects ───────────────────────────────────── */

export function createPhoton(opts = {}) {
  const mesh = new THREE.Mesh(
    new THREE.SphereGeometry(opts.r ?? 0.05, 16, 12),
    new THREE.MeshBasicMaterial({ color: opts.color ?? PALETTE.photon })
  );
  const glow = new THREE.PointLight(opts.color ?? PALETTE.photon, 2, 3);
  mesh.add(glow);
  return { mesh, glow };
}

export function torusMaterials(opts = {}) {
  const col = opts.color ?? PALETTE.surface;
  return {
    surface: new THREE.MeshPhongMaterial({
      color: col, transparent: true, opacity: opts.opacity ?? 0.35,
      side: THREE.DoubleSide, depthWrite: false, shininess: 60,
    }),
    wire: new THREE.MeshBasicMaterial({
      color: col, wireframe: true, transparent: true,
      opacity: opts.wireOpacity ?? 0.06, side: THREE.DoubleSide,
    }),
  };
}
