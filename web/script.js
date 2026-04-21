const PAGES = ['home', 'read', 'about'];
const DEFAULT_PAGE = 'home';
const TITLE_PREFIX = 'Forma';
const LEGACY_PAGE_MAP = {
  idea: 'home',
  architecture: 'home',
  results: 'home',
  start: 'read'
};

const hamburger = document.getElementById('hamburger-button');
const navMenu = document.getElementById('nav-menu');
const content = document.getElementById('content');

function titleCase(slug) {
  const titles = {
    home: 'The Shape of Things',
    read: 'Start Here',
    about: 'About'
  };
  return titles[slug] || slug.charAt(0).toUpperCase() + slug.slice(1);
}

function resolvePage(page) {
  return LEGACY_PAGE_MAP[page] || page;
}

function setupPageLinks() {
  document.querySelectorAll('a[data-page]').forEach(link => {
    if (link.dataset.bound === '1') return;
    link.dataset.bound = '1';
    link.addEventListener('click', event => {
      event.preventDefault();
      const page = event.currentTarget.getAttribute('data-page');
      if (!page) return;
      if (window.location.hash.slice(1) === page) {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } else {
        window.location.hash = page;
      }
      closeMenu();
    });
  });
}

function updateActiveNav(page) {
  document.querySelectorAll('.nav-links a[data-page]').forEach(a => {
    if (a.getAttribute('data-page') === page) {
      a.classList.add('active');
    } else {
      a.classList.remove('active');
    }
  });
}

function closeMenu() {
  if (navMenu) navMenu.classList.remove('open');
  if (hamburger) hamburger.classList.remove('open');
}

function loadContent(page) {
  page = resolvePage(page);
  if (!PAGES.includes(page)) page = DEFAULT_PAGE;

  fetch(`${page}.html`, { cache: 'no-cache' })
    .then(resp => {
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      return resp.text();
    })
    .then(html => {
      content.innerHTML = html;
      document.title = `${TITLE_PREFIX} — ${titleCase(page)}`;
      setupPageLinks();
      updateActiveNav(page);
      window.scrollTo(0, 0);
      content.focus({ preventScroll: true });

      if (window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise([content]).catch(() => {});
      }
    })
    .catch(err => {
      content.innerHTML = `
        <section class="prose">
          <h1 class="page-title">Page not found</h1>
          <p>We couldn’t load <code>${page}.html</code>.</p>
          <p><a href="#home" data-page="home">Return home →</a></p>
        </section>
      `;
      document.title = `${TITLE_PREFIX} — Not Found`;
      setupPageLinks();
      console.warn('Page load failed:', err);
    });
}

function handleHashChange() {
  const page = resolvePage((window.location.hash.slice(1) || DEFAULT_PAGE).split('?')[0]);
  loadContent(page);
}

document.addEventListener('DOMContentLoaded', () => {
  window.addEventListener('hashchange', handleHashChange);
  handleHashChange();
  setupPageLinks();

  if (hamburger) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('open');
      navMenu.classList.toggle('open');
    });
  }
});
