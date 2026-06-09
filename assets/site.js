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

const mobileMq = window.matchMedia('(max-width: 1024px)');
const CONTACT_EMAIL = 'info@refyapi.com';
const CONTACT_PHONE = '+902164413350';

function initContactSheet() {
  let sheet = document.getElementById('contactSheet');
  if (!sheet) {
    sheet = document.createElement('div');
    sheet.id = 'contactSheet';
    sheet.className = 'contact-sheet';
    sheet.setAttribute('aria-hidden', 'true');
    sheet.innerHTML = `
      <div class="contact-sheet-backdrop"></div>
      <div class="contact-sheet-panel" role="dialog" aria-labelledby="contactSheetTitle">
        <p class="contact-sheet-title" id="contactSheetTitle">
          <span data-lang="tr">Nasıl iletişime geçmek istersiniz?</span>
          <span data-lang="en">How would you like to get in touch?</span>
          <span data-lang="ru">Как вы хотите связаться?</span>
        </p>
        <div class="contact-sheet-actions">
          <a href="mailto:${CONTACT_EMAIL}" class="contact-sheet-btn">
            <svg width="22" height="22" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="4" width="14" height="10" rx="1"/><path d="M2 5l7 5 7-5"/></svg>
            <div>
              <div class="contact-sheet-btn-label"><span data-lang="tr">E-posta</span><span data-lang="en">Email</span><span data-lang="ru">Эл. почта</span></div>
              <div class="contact-sheet-btn-value">${CONTACT_EMAIL}</div>
            </div>
          </a>
          <a href="tel:${CONTACT_PHONE}" class="contact-sheet-btn">
            <svg width="22" height="22" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3h3l1.5 3.5-2 1.2A11 11 0 0010.3 12.5l1.2-2L15 12v3a1 1 0 01-1 1C6.16 16 2 11.84 2 4a1 1 0 011-1z"/></svg>
            <div>
              <div class="contact-sheet-btn-label"><span data-lang="tr">Telefon</span><span data-lang="en">Call</span><span data-lang="ru">Позвонить</span></div>
              <div class="contact-sheet-btn-value">+90 216 441 33 50</div>
            </div>
          </a>
        </div>
        <button type="button" class="contact-sheet-cancel">
          <span data-lang="tr">İptal</span><span data-lang="en">Cancel</span><span data-lang="ru">Отмена</span>
        </button>
      </div>`;
    document.body.appendChild(sheet);
    sheet.querySelector('.contact-sheet-backdrop').addEventListener('click', closeContactSheet);
    sheet.querySelector('.contact-sheet-cancel').addEventListener('click', closeContactSheet);
  }
  return sheet;
}

function openContactSheet() {
  const sheet = initContactSheet();
  sheet.classList.add('open');
  sheet.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}

function closeContactSheet() {
  const sheet = document.getElementById('contactSheet');
  if (!sheet) return;
  sheet.classList.remove('open');
  sheet.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}

document.querySelectorAll('.contact-sheet-trigger').forEach(btn => {
  btn.addEventListener('click', e => {
    if (!mobileMq.matches) return;
    e.preventDefault();
    openContactSheet();
  });
});

document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    if (a.classList.contains('contact-sheet-trigger') && mobileMq.matches) return;
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
