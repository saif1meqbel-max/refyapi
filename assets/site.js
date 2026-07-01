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
  { v: 'fire', tr: 'Yangın Alarm Sistemleri', en: 'Fire Alarm Systems', ru: 'Пожарная сигнализация' },
  { v: 'access', tr: 'Erişim Kontrol ve Personel Takip', en: 'Access Control & Staff Tracking', ru: 'Контроль доступа' },
  { v: 'data', tr: 'Data ve Altyapı Sistemleri', en: 'Data & Infrastructure', ru: 'Data и инфраструктура' },
  { v: 'hotel-door', tr: 'Otel Kapı Sistemleri', en: 'Hotel Door Systems', ru: 'Дверные системы для отелей' },
  { v: 'pa', tr: 'Genel Anons ve Sesli Alarm', en: 'Public Announcement & Voice Alarm', ru: 'Оповещение и сигнализация' },
  { v: 'mechanical', tr: 'Mekanik Otomasyon', en: 'Mechanical Automation', ru: 'Механическая автоматизация' },
  { v: 'phone', tr: 'Telefon / VoIP Sistemleri', en: 'Phone / VoIP Systems', ru: 'Телефония / VoIP' },
  { v: 'intercom', tr: 'IP İntercom Sistemleri', en: 'IP Intercom Systems', ru: 'IP-домофон' },
  { v: 'cctv', tr: 'CCTV Sistemleri', en: 'CCTV Systems', ru: 'Видеонаблюдение' },
  { v: 'lighting', tr: 'Bina ve Aydınlatma Otomasyonu', en: 'Building & Lighting Automation', ru: 'Автоматизация зданий' },
  { v: 'nurse', tr: 'Hemşire Çağrı ve Mavi Kod', en: 'Nurse Call & Code Blue', ru: 'Вызов медсестры' },
  { v: 'iptv', tr: 'IPTV Sistemleri', en: 'IPTV Systems', ru: 'IPTV' },
  { v: 'integrated', tr: 'Honeywell · Entegre Bina Sistemleri', en: 'Honeywell · Integrated Building Systems', ru: 'Honeywell · Интегрированные системы' },
  { v: 'security', tr: 'Güvenlik Sistemleri', en: 'Security Systems', ru: 'Системы безопасности' },
  { v: 'tv', tr: 'TV ve Görüntü', en: 'TV & Video', ru: 'ТВ и видео' },
  { v: 'general', tr: 'Genel / Diğer', en: 'General / Other', ru: 'Общий / Другое' },
];

const COUNTRY_CODES = (
  'AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ BL BM BN BO BQ BR BS BT BV BW BY BZ ' +
  'CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ DK DM DO DZ EC EE EG EH ER ES ET FI FJ FK FM FO FR ' +
  'GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO JP ' +
  'KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS MT ' +
  'MU MV MW MX MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS RU RW ' +
  'SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TL TM TN TO TR TT TV TW TZ UA UG ' +
  'UM US UY UZ VA VC VE VG VI VN VU WF WS YE YT ZA ZM ZW'
).split(' ');

const COUNTRY_PRIORITY = ['TR', 'UZ', 'GB'];
const countryNameEn = new Intl.DisplayNames(['en'], { type: 'region' });

function countryOptionsHtml() {
  const lang = document.documentElement.lang || 'tr';
  const locale = lang === 'ru' ? 'ru' : lang === 'tr' ? 'tr' : 'en';
  let dn;
  try {
    dn = new Intl.DisplayNames([locale], { type: 'region' });
  } catch {
    dn = countryNameEn;
  }

  const all = COUNTRY_CODES
    .map(code => ({ code, label: dn.of(code) || countryNameEn.of(code) || code }))
    .filter(c => c.label)
    .sort((a, b) => a.label.localeCompare(b.label, locale));

  const pinned = COUNTRY_PRIORITY.map(code => all.find(c => c.code === code)).filter(Boolean);
  const rest = all.filter(c => !COUNTRY_PRIORITY.includes(c.code));
  const placeholder = locale === 'tr' ? 'Ülke seçin' : locale === 'ru' ? 'Выберите страну' : 'Select country';

  let html = `<option value="" disabled selected>${placeholder}</option>`;
  pinned.forEach(c => { html += `<option value="${c.code}">${c.label}</option>`; });
  html += '<option disabled>──────────</option>';
  rest.forEach(c => { html += `<option value="${c.code}">${c.label}</option>`; });
  return html;
}

function countryLabel(code) {
  if (!code) return '—';
  return countryNameEn.of(code) || code;
}

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
              ${countryOptionsHtml()}
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
  const countrySel = modal.querySelector('#quoteCountry');
  if (countrySel) countrySel.value = 'TR';
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
    `Country: ${countryLabel(payload.country)}`,
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
        country: countryLabel(payload.country),
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
  openQuoteModal(trigger.dataset.service || trigger.dataset.quoteService || '');
});

function selectHomeService(id, scroll = true) {
  const cards = document.querySelectorAll('.sg.sg-12 .sc-card[data-service]');
  const panels = document.querySelectorAll('.svc-preview-panel[data-service]');
  const preview = document.getElementById('svcPreview');
  if (!cards.length || !panels.length) return;
  cards.forEach(c => {
    const on = c.dataset.service === id;
    c.classList.toggle('is-active', on);
    c.setAttribute('aria-pressed', on ? 'true' : 'false');
  });
  panels.forEach(p => p.classList.toggle('is-active', p.dataset.service === id));
  if (scroll && preview) {
    preview.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}

function initHomeServices() {
  const grid = document.querySelector('.sg.sg-12');
  if (!grid) return;

  grid.querySelectorAll('.sc-card[data-service]').forEach(card => {
    card.addEventListener('click', () => selectHomeService(card.dataset.service));
  });

  document.querySelectorAll('.prod-svc-chip').forEach(chip => {
    const num = chip.textContent.trim().padStart(2, '0');
    const map = {
      '01': 'fire', '02': 'access', '03': 'data', '04': 'hotel-door', '05': 'pa',
      '06': 'mechanical', '07': 'phone', '08': 'intercom', '09': 'cctv',
      '10': 'lighting', '11': 'nurse', '12': 'iptv'
    };
    const id = map[num];
    if (!id) return;
    chip.style.cursor = 'pointer';
    chip.setAttribute('role', 'button');
    chip.setAttribute('tabindex', '0');
    chip.addEventListener('click', e => {
      e.preventDefault();
      e.stopPropagation();
      document.getElementById('hizmetler')?.scrollIntoView({ behavior: 'smooth' });
      setTimeout(() => selectHomeService(id), 400);
    });
    chip.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        chip.click();
      }
    });
  });

  const hash = location.hash.replace('#', '');
  if (hash.startsWith('svc-')) {
    selectHomeService(hash.replace('svc-', ''), false);
  }
}

initHomeServices();

document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    if (a.classList.contains('contact-sheet-trigger') && mobileMq.matches) return;
    const t = document.querySelector(a.getAttribute('href'));
    if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
  });
});

const refsGrid = document.querySelector('.refs-grid');
const sortBtns = document.querySelectorAll('.sortbtn');
const refsCountryDd = document.getElementById('refsCountryDd');
const refsCountryBtn = document.getElementById('refsCountryBtn');
const refsCountryMenu = document.getElementById('refsCountryMenu');
const refsCountryBtnLabel = document.querySelector('.refs-country-btn-label');
const refsEmpty = document.getElementById('refsEmpty');

const REF_COUNTRY_LABELS = {
  turkey: { tr: 'Türkiye', en: 'Turkey', ru: 'Турция' },
  azerbaijan: { tr: 'Azerbaycan', en: 'Azerbaijan', ru: 'Азербайджан' },
  russia: { tr: 'Rusya', en: 'Russia', ru: 'Россия' },
  turkmenistan: { tr: 'Türkmenistan', en: 'Turkmenistan', ru: 'Туркменистан' },
  belarus: { tr: 'Beyaz Rusya', en: 'Belarus', ru: 'Беларусь' },
  'equatorial-guinea': { tr: 'Ekvator Ginesi', en: 'Equatorial Guinea', ru: 'Экваториальная Гвинея' },
  curacao: { tr: 'Curaçao', en: 'Curaçao', ru: 'Кюрасао' },
  nigeria: { tr: 'Nijerya', en: 'Nigeria', ru: 'Нигерия' },
  fiji: { tr: 'Fiji', en: 'Fiji', ru: 'Фиджи' },
  kyrgyzstan: { tr: 'Kırgızistan', en: 'Kyrgyzstan', ru: 'Киргизия' },
  tajikistan: { tr: 'Tacikistan', en: 'Tajikistan', ru: 'Таджикистан' },
  uzbekistan: { tr: 'Özbekistan', en: 'Uzbekistan', ru: 'Узбекистан' },
};

const REF_ALL_COUNTRIES_LABEL = {
  tr: 'Tüm Ülkeler', en: 'All Countries', ru: 'Все страны',
};

if (refsGrid && sortBtns.length) {
  const yearOf = card => {
    const y = card.querySelector('.ref-year');
    return y ? parseInt(y.textContent, 10) : 0;
  };

  let sortDir = 'desc';
  let countryFilter = 'all';

  const allCards = () => Array.from(refsGrid.querySelectorAll(':scope > .ref-card'));

  const countryLabelHtml = slug => {
    if (slug === 'all') {
      return ['tr', 'en', 'ru'].map(l =>
        `<span data-lang="${l}">${REF_ALL_COUNTRIES_LABEL[l]}</span>`
      ).join('');
    }
    const labels = REF_COUNTRY_LABELS[slug];
    if (!labels) return slug;
    return ['tr', 'en', 'ru'].map(l =>
      `<span data-lang="${l}">${labels[l]}</span>`
    ).join('');
  };

  const applyRefsView = () => {
    const cards = allCards();
    let visibleCount = 0;
    cards.forEach(card => {
      const match = countryFilter === 'all' || card.dataset.country === countryFilter;
      card.hidden = !match;
      if (match) visibleCount++;
    });
    const visible = cards.filter(c => !c.hidden);
    visible.sort((a, b) => sortDir === 'asc' ? yearOf(a) - yearOf(b) : yearOf(b) - yearOf(a));
    visible.forEach(c => refsGrid.appendChild(c));
    cards.filter(c => c.hidden).forEach(c => refsGrid.appendChild(c));
    if (refsEmpty) {
      refsEmpty.hidden = visibleCount > 0;
      refsEmpty.classList.toggle('show', visibleCount === 0);
      if (visibleCount === 0) refsGrid.insertBefore(refsEmpty, refsGrid.firstChild);
    }
    sortBtns.forEach(b => b.classList.toggle('on', b.dataset.sort === sortDir));
    if (refsCountryMenu) {
      refsCountryMenu.querySelectorAll('.refs-country-option').forEach(opt => {
        opt.classList.toggle('on', opt.dataset.country === countryFilter);
      });
    }
  };

  sortBtns.forEach(b => {
    b.addEventListener('click', () => {
      sortDir = b.dataset.sort;
      applyRefsView();
    });
  });

  if (refsCountryMenu && refsCountryBtn && refsCountryDd) {
    const countries = [...new Set(allCards().map(c => c.dataset.country).filter(Boolean))]
      .sort((a, b) => (REF_COUNTRY_LABELS[a]?.en || a).localeCompare(REF_COUNTRY_LABELS[b]?.en || b));

    const allItem = document.createElement('li');
    allItem.innerHTML = `<button type="button" class="refs-country-option on" data-country="all" role="option">${countryLabelHtml('all')}</button>`;
    refsCountryMenu.appendChild(allItem);

    countries.forEach(slug => {
      const li = document.createElement('li');
      li.innerHTML = `<button type="button" class="refs-country-option" data-country="${slug}" role="option">${countryLabelHtml(slug)}</button>`;
      refsCountryMenu.appendChild(li);
    });

    const setCountry = slug => {
      countryFilter = slug;
      if (refsCountryBtnLabel) refsCountryBtnLabel.innerHTML = countryLabelHtml(slug);
      closeCountryMenu();
      applyRefsView();
    };

    const openCountryMenu = () => {
      refsCountryDd.classList.add('open');
      refsCountryBtn.setAttribute('aria-expanded', 'true');
      refsCountryMenu.hidden = false;
    };

    const closeCountryMenu = () => {
      refsCountryDd.classList.remove('open');
      refsCountryBtn.setAttribute('aria-expanded', 'false');
      refsCountryMenu.hidden = true;
    };

    refsCountryBtn.addEventListener('click', () => {
      if (refsCountryDd.classList.contains('open')) closeCountryMenu();
      else openCountryMenu();
    });

    refsCountryMenu.addEventListener('click', e => {
      const opt = e.target.closest('.refs-country-option');
      if (!opt) return;
      setCountry(opt.dataset.country);
    });

    document.addEventListener('click', e => {
      if (!refsCountryDd.contains(e.target)) closeCountryMenu();
    });

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeCountryMenu();
    });
  }

  applyRefsView();
}

(function initNavActive() {
  const navEl = document.getElementById('mainNav');
  if (!navEl) return;

  const items = navEl.querySelectorAll('.nav-links > li');
  const page = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  const SERVICE_PAGES = new Set([
    'integrated-building-systems.html', 'fire-detection.html', 'security-systems.html',
    'automation-systems.html', 'audio-visual-systems.html', 'data-communications.html',
    'tv-video-systems.html',
  ]);
  const OFFICE_PAGES = new Set(['istanbul.html', 'london.html', 'middle-east-asia.html']);

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
