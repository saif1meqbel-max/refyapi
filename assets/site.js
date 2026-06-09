function setLang(l) {
  const base = document.body.dataset.base || '';
  document.body.className = (base ? base + ' ' : '') + (l === 'tr' ? '' : 'lang-' + l);
  document.querySelectorAll('.lbtn').forEach(b => b.classList.toggle('on', b.textContent.trim().toLowerCase() === l));
  document.documentElement.lang = l;
}

const nav = document.getElementById('mainNav');
if (nav && !nav.classList.contains('solid')) {
  window.addEventListener('scroll', () => nav.classList.toggle('sc', scrollY > 60), { passive: true });
}

const hbg = document.querySelector('.hbg');
if (nav && hbg) {
  hbg.addEventListener('click', e => {
    e.stopPropagation();
    nav.classList.toggle('menu-open');
  });
  nav.querySelectorAll('.nav-links a').forEach(a => {
    a.addEventListener('click', () => nav.classList.remove('menu-open'));
  });
  document.addEventListener('click', e => {
    if (nav.classList.contains('menu-open') && !nav.contains(e.target)) {
      nav.classList.remove('menu-open');
    }
  });
}

const bg = document.getElementById('heroBg');
if (bg) {
  window.addEventListener('scroll', () => { bg.style.transform = `scale(1.05) translateY(${scrollY * 0.28}px)`; }, { passive: true });
}

const obs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('on'); obs.unobserve(e.target); } });
}, { threshold: 0.1, rootMargin: '0px 0px -32px 0px' });
document.querySelectorAll('.rv,.rvl,.rvr').forEach(el => obs.observe(el));

const cObs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target, target = +el.dataset.target;
    let v = 0; const step = target / 90;
    const t = setInterval(() => {
      v = Math.min(v + step, target);
      el.textContent = Math.floor(v) + (target >= 100 ? '+' : '');
      if (v >= target) clearInterval(t);
    }, 16);
    cObs.unobserve(el);
  });
}, { threshold: 0.5 });
document.querySelectorAll('[data-target]').forEach(el => cObs.observe(el));

document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href'));
    if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
  });
});

const refsGrid = document.querySelector('.refs-grid');
const sortBtns = document.querySelectorAll('.sortbtn');
if (refsGrid && sortBtns.length) {
  const yearOf = card => {
    const y = card.querySelector('.ref-year');
    return y ? parseInt(y.textContent, 10) : 0;
  };
  const applySort = dir => {
    const cards = Array.from(refsGrid.children);
    cards.sort((a, b) => dir === 'asc' ? yearOf(a) - yearOf(b) : yearOf(b) - yearOf(a));
    cards.forEach(c => refsGrid.appendChild(c));
    sortBtns.forEach(b => b.classList.toggle('on', b.dataset.sort === dir));
  };
  sortBtns.forEach(b => b.addEventListener('click', () => applySort(b.dataset.sort)));
  applySort('desc');
}
