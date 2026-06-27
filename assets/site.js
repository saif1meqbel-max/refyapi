const LANG_KEY = 'fnv-lang';
const VALID_LANGS = new Set(['tr', 'en', 'ru']);

function setLang(l) {
  if (!VALID_LANGS.has(l)) l = 'tr';
  try { localStorage.setItem(LANG_KEY, l); } catch (_) {}
  const base = document.body.dataset.base || '';
  document.body.className = (base ? base + ' ' : '') + (l === 'tr' ? '' : 'lang-' + l);
  document.documentElement.lang = l;
  document.documentElement.classList.remove('lang-en', 'lang-ru');
  if (l !== 'tr') document.documentElement.classList.add('lang-' + l);
  document.querySelectorAll('.lbtn').forEach(b => b.classList.toggle('on', b.textContent.trim().toLowerCase() === l));
}

(function initLang() {
  let l = 'tr';
  try {
    const stored = localStorage.getItem(LANG_KEY);
    if (stored && VALID_LANGS.has(stored)) l = stored;
  } catch (_) {}
  setLang(l);
})();

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
const CONTACT_EMAIL = 'info@fnvelektronik.com';
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

const QUOTE_EMAIL = 'info@fnvelektronik.com';
const SERVICE_OPTIONS = [
  { v: 'fire', tr: 'Yangın Algılama', en: 'Fire Detection', ru: 'Пожарная сигнализация' },
  { v: 'security', tr: 'Güvenlik Sistemleri', en: 'Security Systems', ru: 'Системы безопасности' },
  { v: 'automation', tr: 'Otomasyon Sistemleri', en: 'Automation Systems', ru: 'Автоматизация' },
  { v: 'audio', tr: 'Ses ve Işık', en: 'Audio & Visual', ru: 'Аудио и свет' },
  { v: 'data', tr: 'Data ve İletişim', en: 'Data & Communications', ru: 'Связь и данные' },
  { v: 'tv', tr: 'TV ve Görüntü', en: 'TV & Video', ru: 'ТВ и видео' },
  { v: 'general', tr: 'Genel / Diğer', en: 'General / Other', ru: 'Общий / Другое' },
];

function serviceOptionsHtml() {
  const lang = document.documentElement.lang || 'tr';
  const key = lang === 'en' ? 'en' : lang === 'ru' ? 'ru' : 'tr';
  return SERVICE_OPTIONS.map(o => `<option value="${o.v}">${o[key]}</option>`).join('');
}

function initQuoteModal() {
  let modal = document.getElementById('quoteModal');
  if (modal) return modal;
  modal = document.createElement('div');
  modal.id = 'quoteModal';
  modal.className = 'quote-modal';
  modal.setAttribute('aria-hidden', 'true');
  modal.innerHTML = `
    <div class="quote-modal-backdrop"></div>
    <div class="quote-modal-panel" role="dialog" aria-labelledby="quoteModalTitle">
      <div class="quote-modal-head">
        <div>
          <h2 class="quote-modal-title" id="quoteModalTitle">
            <span data-lang="tr">Teklif Talep Formu</span>
            <span data-lang="en">Request a Quote</span>
            <span data-lang="ru">Запрос сметы</span>
          </h2>
          <p class="quote-modal-sub">
            <span data-lang="tr">Projeniz hakkında kısa bilgi verin — en kısa sürede size dönüş yapalım.</span>
            <span data-lang="en">Tell us briefly about your project and we will get back to you shortly.</span>
            <span data-lang="ru">Кратко опишите проект — мы свяжемся с вами в ближайшее время.</span>
          </p>
        </div>
        <button type="button" class="quote-modal-close" aria-label="Close">
          <svg width="22" height="22" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 4l10 10M14 4L4 14"/></svg>
        </button>
      </div>
      <form class="quote-form" id="quoteForm" novalidate>
        <div class="quote-field-row">
          <div class="quote-field">
            <label class="quote-label" for="quoteName"><span data-lang="tr">Ad Soyad *</span><span data-lang="en">Full Name *</span><span data-lang="ru">Имя *</span></label>
            <input class="quote-input" id="quoteName" name="name" type="text" required autocomplete="name" />
          </div>
          <div class="quote-field">
            <label class="quote-label" for="quoteCompany"><span data-lang="tr">Şirket</span><span data-lang="en">Company</span><span data-lang="ru">Компания</span></label>
            <input class="quote-input" id="quoteCompany" name="company" type="text" autocomplete="organization" />
          </div>
        </div>
        <div class="quote-field-row">
          <div class="quote-field">
            <label class="quote-label" for="quoteEmail"><span data-lang="tr">E-posta *</span><span data-lang="en">Email *</span><span data-lang="ru">Эл. почта *</span></label>
            <input class="quote-input" id="quoteEmail" name="email" type="email" required autocomplete="email" />
          </div>
          <div class="quote-field">
            <label class="quote-label" for="quotePhone"><span data-lang="tr">Telefon</span><span data-lang="en">Phone</span><span data-lang="ru">Телефон</span></label>
            <input class="quote-input" id="quotePhone" name="phone" type="tel" autocomplete="tel" />
          </div>
        </div>
        <div class="quote-field-row">
          <div class="quote-field">
            <label class="quote-label" for="quoteCountry"><span data-lang="tr">Ülke</span><span data-lang="en">Country</span><span data-lang="ru">Страна</span></label>
            <select class="quote-select" id="quoteCountry" name="country">
              <option value="Turkey">Turkey</option>
              <option value="Uzbekistan">Uzbekistan</option>
              <option value="United Kingdom">United Kingdom</option>
              <option value="Other">Other</option>
            </select>
          </div>
          <div class="quote-field">
            <label class="quote-label" for="quoteService"><span data-lang="tr">Hizmet</span><span data-lang="en">Service</span><span data-lang="ru">Услуга</span></label>
            <select class="quote-select" id="quoteService" name="service">${serviceOptionsHtml()}</select>
          </div>
        </div>
        <div class="quote-field">
          <label class="quote-label" for="quoteSize"><span data-lang="tr">Proje Ölçeği</span><span data-lang="en">Project Size</span><span data-lang="ru">Масштаб проекта</span></label>
          <select class="quote-select" id="quoteSize" name="project_size">
            <option value="small">Small (&lt; 1,000 m²)</option>
            <option value="medium">Medium (1,000–10,000 m²)</option>
            <option value="large">Large (&gt; 10,000 m²)</option>
            <option value="unknown">Not sure yet</option>
          </select>
        </div>
        <div class="quote-field">
          <label class="quote-label" for="quoteMessage"><span data-lang="tr">Proje Detayları</span><span data-lang="en">Project Details</span><span data-lang="ru">Детали проекта</span></label>
          <textarea class="quote-textarea" id="quoteMessage" name="message" rows="4"></textarea>
        </div>
        <button type="submit" class="quote-submit">
          <span data-lang="tr">Teklif Talebini Gönder</span>
          <span data-lang="en">Send Quote Request</span>
          <span data-lang="ru">Отправить запрос</span>
        </button>
      </form>
      <div class="quote-success" id="quoteSuccess">
        <div class="quote-success-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
        </div>
        <h3><span data-lang="tr">Talebiniz Alındı</span><span data-lang="en">Request Received</span><span data-lang="ru">Запрос получен</span></h3>
        <p><span data-lang="tr">Ekibimiz en kısa sürede sizinle iletişime geçecektir.</span><span data-lang="en">Our team will contact you as soon as possible.</span><span data-lang="ru">Наша команда свяжется с вами в ближайшее время.</span></p>
      </div>
    </div>`;
  document.body.appendChild(modal);

  modal.querySelector('.quote-modal-backdrop').addEventListener('click', closeQuoteModal);
  modal.querySelector('.quote-modal-close').addEventListener('click', closeQuoteModal);
  modal.querySelector('#quoteForm').addEventListener('submit', submitQuoteForm);
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && modal.classList.contains('open')) closeQuoteModal();
  });
  return modal;
}

function openQuoteModal(presetService) {
  const modal = initQuoteModal();
  const form = modal.querySelector('#quoteForm');
  const success = modal.querySelector('#quoteSuccess');
  form.reset();
  form.style.display = '';
  success.classList.remove('on');
  if (presetService) {
    const sel = modal.querySelector('#quoteService');
    if (sel) sel.value = presetService;
  }
  modal.classList.add('open');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
  if (nav) nav.classList.remove('menu-open');
  setTimeout(() => modal.querySelector('#quoteName')?.focus(), 100);
}

function closeQuoteModal() {
  const modal = document.getElementById('quoteModal');
  if (!modal) return;
  modal.classList.remove('open');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}

async function submitQuoteForm(e) {
  e.preventDefault();
  const form = e.target;
  const btn = form.querySelector('.quote-submit');
  const fd = new FormData(form);
  const payload = Object.fromEntries(fd.entries());
  if (!payload.name?.trim() || !payload.email?.trim()) {
    form.querySelector('#quoteName').reportValidity();
    form.querySelector('#quoteEmail').reportValidity();
    return;
  }

  btn.disabled = true;
  const serviceLabel = SERVICE_OPTIONS.find(s => s.v === payload.service);
  const lang = document.documentElement.lang || 'tr';
  const sk = lang === 'en' ? 'en' : lang === 'ru' ? 'ru' : 'tr';
  const bodyText = [
    `Name: ${payload.name}`,
    `Company: ${payload.company || '—'}`,
    `Email: ${payload.email}`,
    `Phone: ${payload.phone || '—'}`,
    `Country: ${payload.country}`,
    `Service: ${serviceLabel ? serviceLabel[sk] : payload.service}`,
    `Project size: ${payload.project_size}`,
    '',
    payload.message || ''
  ].join('\n');

  try {
    const res = await fetch(`https://formsubmit.co/ajax/${encodeURIComponent(QUOTE_EMAIL)}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({
        name: payload.name,
        email: payload.email,
        company: payload.company,
        phone: payload.phone,
        country: payload.country,
        service: serviceLabel ? serviceLabel.en : payload.service,
        project_size: payload.project_size,
        message: payload.message,
        _subject: `FNV Quote Request — ${payload.name}`,
        _template: 'table'
      })
    });
    if (!res.ok) throw new Error('submit failed');
    form.style.display = 'none';
    document.getElementById('quoteSuccess').classList.add('on');
  } catch (_) {
    const subject = encodeURIComponent(`FNV Quote Request — ${payload.name}`);
    const body = encodeURIComponent(bodyText);
    window.location.href = `mailto:${QUOTE_EMAIL}?subject=${subject}&body=${body}`;
    closeQuoteModal();
  } finally {
    btn.disabled = false;
  }
}

document.addEventListener('click', e => {
  const trigger = e.target.closest('.quote-trigger');
  if (!trigger) return;
  e.preventDefault();
  openQuoteModal(trigger.dataset.service || '');
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
    const cards = Array.from(refsGrid.querySelectorAll(':scope > .ref-card'));
    cards.sort((a, b) => dir === 'asc' ? yearOf(a) - yearOf(b) : yearOf(b) - yearOf(a));
    cards.forEach(c => refsGrid.appendChild(c));
    sortBtns.forEach(b => b.classList.toggle('on', b.dataset.sort === dir));
  };
  sortBtns.forEach(b => b.addEventListener('click', () => applySort(b.dataset.sort)));
  applySort('desc');
}

(function initNavActive() {
  const navEl = document.getElementById('mainNav');
  if (!navEl) return;

  const items = navEl.querySelectorAll('.nav-links > li');
  const page = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  const SERVICE_PAGES = new Set([
    'fire-detection.html', 'security-systems.html', 'automation-systems.html',
    'audio-visual-systems.html', 'data-communications.html', 'tv-video-systems.html',
  ]);
  const OFFICE_PAGES = new Set(['istanbul.html', 'tashkent.html', 'london.html']);

  const setActive = li => {
    items.forEach(i => i.classList.remove('nav-active'));
    if (li) li.classList.add('nav-active');
  };

  const liFor = pred => {
    for (const li of items) {
      const a = li.querySelector(':scope > a');
      if (a && pred(a, li)) return li;
    }
    return null;
  };

  const hrefOf = a => (a.getAttribute('href') || '').split('#')[0].split('?')[0];

  if (page === 'references.html') {
    setActive(liFor(a => hrefOf(a).endsWith('references.html')));
    return;
  }
  if (page === 'documents.html') {
    setActive(liFor(a => hrefOf(a).endsWith('documents.html')));
    return;
  }
  if (SERVICE_PAGES.has(page)) {
    setActive(liFor(a => (a.getAttribute('href') || '').includes('urunlerimiz')));
    return;
  }
  if (OFFICE_PAGES.has(page)) {
    setActive(liFor((_, li) => li.classList.contains('nav-offices')));
    return;
  }

  const isHome = page === 'index.html' || page === '' || page.endsWith('/');
  if (!isHome) return;

  const sections = [
    { id: 'hakkimizda', match: a => (a.getAttribute('href') || '').includes('hakkimizda') },
    { id: 'urunlerimiz', match: a => (a.getAttribute('href') || '').includes('urunlerimiz') },
    { id: 'referanslar', match: a => hrefOf(a).endsWith('references.html') },
    {
      id: 'iletisim',
      match: (a, li) => (a.getAttribute('href') || '').includes('iletisim') && !li.classList.contains('nav-offices'),
    },
  ].map(s => ({ ...s, el: document.getElementById(s.id) })).filter(s => s.el);

  const update = () => {
    const offset = 120;
    let current = sections[0];
    for (const s of sections) {
      if (s.el.getBoundingClientRect().top <= offset) current = s;
    }
    setActive(liFor(current.match));
  };

  window.addEventListener('scroll', update, { passive: true });
  update();
})();
