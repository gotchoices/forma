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

  const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
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

  if (opts.capture !== false) _initCapturePanel(container, renderer);
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

/* ── Capture panel (auto-injected by createScene) ─────── */

function _initCapturePanel(container, renderer) {
  const panel = document.createElement('div');
  panel.className = 'totu-cap';
  panel.innerHTML = `
    <div class="totu-cap-rec" hidden>REC</div>
    <button class="totu-cap-btn" title="Capture screenshot / recording">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
           stroke-linecap="round" stroke-linejoin="round">
        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/>
        <circle cx="12" cy="13" r="4"/>
      </svg>
    </button>
    <div class="totu-cap-menu" hidden>
      <button class="totu-cap-item" id="_tcap-png">PNG</button>
      <button class="totu-cap-item" id="_tcap-gif">GIF  ●</button>
      <button class="totu-cap-item" id="_tcap-webm">WebM ●</button>
    </div>`;
  container.appendChild(panel);

  const capBtn   = panel.querySelector('.totu-cap-btn');
  const menu     = panel.querySelector('.totu-cap-menu');
  const recBadge = panel.querySelector('.totu-cap-rec');
  const pngBtn   = panel.querySelector('#_tcap-png');
  const gifBtn   = panel.querySelector('#_tcap-gif');
  const webmBtn  = panel.querySelector('#_tcap-webm');

  capBtn.onclick  = e => { e.stopPropagation(); menu.hidden = !menu.hidden; };
  menu.onclick    = e => e.stopPropagation();
  document.addEventListener('click', () => { menu.hidden = true; });

  /* ── PNG ────────────────────────────────────────────── */
  pngBtn.onclick = () => {
    menu.hidden = true;
    _dlURL(renderer.domElement.toDataURL('image/png'), `totu-${_ts()}.png`);
  };

  /* ── GIF (gifenc, pure-JS encoder, no worker needed) ── */
  const GIF_FPS = 12, GIF_MAX_W = 640;
  let gifActive = false, gifFrames = [], gifTimer = null;

  gifBtn.onclick = async () => {
    if (!gifActive) {
      gifActive = true;
      gifFrames = [];
      gifBtn.textContent = '⏹ Stop (GIF)';
      gifBtn.classList.add('totu-active');
      recBadge.hidden = false;
      menu.hidden = true;
      gifTimer = setInterval(() => {
        const f = _grabFrame(renderer.domElement, GIF_MAX_W);
        if (f) gifFrames.push(f);
      }, 1000 / GIF_FPS);
    } else {
      clearInterval(gifTimer);
      gifActive = false;
      recBadge.hidden = true;
      gifBtn.textContent = '⏳ Encoding…';
      gifBtn.disabled = true;
      try {
        const blob = await _encodeGif(gifFrames, GIF_FPS);
        _dlURL(URL.createObjectURL(blob), `totu-${_ts()}.gif`, true);
      } catch (err) {
        console.error('GIF encode failed', err);
        alert('GIF encoding failed:\n' + err.message);
      }
      gifBtn.textContent = 'GIF  ●';
      gifBtn.disabled = false;
      gifBtn.classList.remove('totu-active');
    }
  };

  /* ── WebM (native MediaRecorder, no deps) ───────────── */
  let recorder = null, recChunks = [];

  webmBtn.onclick = () => {
    if (!recorder) {
      const stream = renderer.domElement.captureStream(30);
      const mime = MediaRecorder.isTypeSupported('video/webm;codecs=vp9')
        ? 'video/webm;codecs=vp9' : 'video/webm';
      recorder = new MediaRecorder(stream, { mimeType: mime });
      recChunks = [];
      recorder.ondataavailable = e => { if (e.data.size > 0) recChunks.push(e.data); };
      recorder.onstop = () => {
        _dlURL(URL.createObjectURL(new Blob(recChunks, { type: 'video/webm' })),
               `totu-${_ts()}.webm`, true);
        recorder = null;
      };
      recorder.start();
      webmBtn.textContent = '⏹ Stop (WebM)';
      webmBtn.classList.add('totu-active');
      recBadge.hidden = false;
      menu.hidden = true;
    } else {
      recorder.stop();
      webmBtn.textContent = 'WebM ●';
      webmBtn.classList.remove('totu-active');
      recBadge.hidden = true;
    }
  };
}

function _grabFrame(canvas, maxW) {
  const scale = Math.min(1, maxW / canvas.width);
  const w = Math.max(2, Math.round(canvas.width  * scale));
  const h = Math.max(2, Math.round(canvas.height * scale));
  const tmp = document.createElement('canvas');
  tmp.width = w; tmp.height = h;
  tmp.getContext('2d').drawImage(canvas, 0, 0, w, h);
  return { data: tmp.getContext('2d').getImageData(0, 0, w, h), w, h };
}

async function _encodeGif(frames, fps) {
  // gifenc: pure-JS GIF encoder, no worker required.
  // Delay unit in GIF spec is centiseconds (1/100 s).
  const { GIFEncoder, quantize, applyPalette } =
    await import('https://esm.sh/gifenc@0.1.3');
  const delay = Math.round(100 / fps);   // centiseconds per frame
  const { w, h } = frames[0];
  const enc = GIFEncoder();
  for (const { data, w: fw, h: fh } of frames) {
    const rgba    = data.data;
    const palette = quantize(rgba, 256);
    const index   = applyPalette(rgba, palette);
    enc.writeFrame(index, fw, fh, { palette, delay });
  }
  enc.finish();
  return new Blob([enc.bytesView()], { type: 'image/gif' });
}

function _dlURL(url, name, revoke = false) {
  const a = document.createElement('a');
  a.href = url; a.download = name; a.click();
  if (revoke) setTimeout(() => URL.revokeObjectURL(url), 8000);
}

function _ts() {
  return new Date().toISOString().slice(0, 19).replace(/[T:]/g, '-');
}
