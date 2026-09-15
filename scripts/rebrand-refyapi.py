#!/usr/bin/env python3
"""Rebrand FNV Elektronik site to REF YAPI construction company."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC_LOGO = Path(
    "/Users/saifalmeqbel/.cursor/projects/Users-saifalmeqbel-Desktop-refyapi-website"
    "/assets/image-b0cf828e-e3ff-476c-b041-71b85db70cb0.png"
)
ASSETS = ROOT / "assets"


def is_orange(r: int, g: int, b: int) -> bool:
    return r >= 160 and g <= 170 and b <= 110 and r > g and r > b + 40


def process_logos() -> None:
    im = Image.open(SRC_LOGO).convert("RGBA")
    w, h = im.size
    px = im.load()

    dark = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    light = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    dp, lp = dark.load(), light.load()

    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a < 8:
                continue
            dp[x, y] = (r, g, b, a)
            if is_orange(r, g, b):
                lp[x, y] = (r, g, b, a)
            else:
                lp[x, y] = (255, 255, 255, a)

    def trim(img: Image.Image, pad: int = 8) -> Image.Image:
        bbox = img.getbbox()
        if not bbox:
            return img
        l, t, r, b = bbox
        l, t = max(0, l - pad), max(0, t - pad)
        r, b = min(img.width, r + pad), min(img.height, b + pad)
        return img.crop((l, t, r, b))

    dark = trim(dark)
    light = trim(light)
    mark = trim(dark.crop((0, 0, int(dark.width * 0.28), dark.height)), pad=4)

    shutil.copy(SRC_LOGO, ASSETS / "logo-refyapi.png")
    dark.save(ASSETS / "logo-mark.png", "PNG")
    light.save(ASSETS / "logo-white.png", "PNG")
    mark.save(ASSETS / "logo-icon.png", "PNG")
    print("logos written", dark.size, light.size, mark.size)


NAV_PRODUCTS_RE = re.compile(
    r"[ \t]*<li>\s*<a href=\"(?:index\.html)?#urunlerimiz\">[\s\S]*?</ul>\s*</li>\n?",
    re.M,
)

NAV_HIZMET_INDEX = """    <li>
      <a href="#hizmetler">
        <span data-lang="tr">Hizmetlerimiz</span>
        <span data-lang="en">Our Services</span>
        <span data-lang="ru">Услуги</span>
      </a>
    </li>
"""

NAV_HIZMET_OTHER = """    <li>
      <a href="index.html#hizmetler">
        <span data-lang="tr">Hizmetlerimiz</span>
        <span data-lang="en">Our Services</span>
        <span data-lang="ru">Услуги</span>
      </a>
    </li>
"""

FOOTER_SERVICES_RE = re.compile(
    r'<div class="ft-col-services">[\s\S]*?</div>\n    <div>',
    re.M,
)

FOOTER_SERVICES_INDEX = """<div class="ft-col-services">
      <p class="ft-col-head"><span data-lang="tr">Hizmetler</span><span data-lang="en">Services</span><span data-lang="ru">Услуги</span></p>
      <ul class="ft-links">
        <li><a href="#svc-residential"><span data-lang="tr">Konut İnşaatı</span><span data-lang="en">Residential Construction</span><span data-lang="ru">Жилищное строительство</span></a></li>
        <li><a href="#svc-commercial"><span data-lang="tr">Ticari Yapılar</span><span data-lang="en">Commercial Buildings</span><span data-lang="ru">Коммерческие здания</span></a></li>
        <li><a href="#svc-industrial"><span data-lang="tr">Endüstriyel Tesisler</span><span data-lang="en">Industrial Facilities</span><span data-lang="ru">Промышленные объекты</span></a></li>
        <li><a href="#svc-turnkey"><span data-lang="tr">Anahtar Teslim Projeler</span><span data-lang="en">Turnkey Projects</span><span data-lang="ru">Проекты «под ключ»</span></a></li>
        <li><a href="#svc-renovation"><span data-lang="tr">Tadilat ve Restorasyon</span><span data-lang="en">Renovation &amp; Restoration</span><span data-lang="ru">Реконструкция</span></a></li>
        <li><a href="#svc-management"><span data-lang="tr">Proje Yönetimi</span><span data-lang="en">Project Management</span><span data-lang="ru">Управление проектами</span></a></li>
      </ul>
    </div>
    <div>"""

FOOTER_SERVICES_OTHER = """<div class="ft-col-services">
      <p class="ft-col-head"><span data-lang="tr">Hizmetler</span><span data-lang="en">Services</span><span data-lang="ru">Услуги</span></p>
      <ul class="ft-links">
        <li><a href="index.html#svc-residential"><span data-lang="tr">Konut İnşaatı</span><span data-lang="en">Residential Construction</span><span data-lang="ru">Жилищное строительство</span></a></li>
        <li><a href="index.html#svc-commercial"><span data-lang="tr">Ticari Yapılar</span><span data-lang="en">Commercial Buildings</span><span data-lang="ru">Коммерческие здания</span></a></li>
        <li><a href="index.html#svc-industrial"><span data-lang="tr">Endüstriyel Tesisler</span><span data-lang="en">Industrial Facilities</span><span data-lang="ru">Промышленные объекты</span></a></li>
        <li><a href="index.html#svc-turnkey"><span data-lang="tr">Anahtar Teslim Projeler</span><span data-lang="en">Turnkey Projects</span><span data-lang="ru">Проекты «под ключ»</span></a></li>
        <li><a href="index.html#svc-renovation"><span data-lang="tr">Tadilat ve Restorasyon</span><span data-lang="en">Renovation &amp; Restoration</span><span data-lang="ru">Реконструкция</span></a></li>
        <li><a href="index.html#svc-management"><span data-lang="tr">Proje Yönetimi</span><span data-lang="en">Project Management</span><span data-lang="ru">Управление проектами</span></a></li>
      </ul>
    </div>
    <div>"""

BRAND_SUB_TR = "İnşaat ve yapı alanında güvenilir çözüm ortağınız. 2005'ten bu yana hizmetinizdeyiz."
BRAND_SUB_EN = "Your trusted partner in construction and building. Serving you since 2005."
BRAND_SUB_RU = "Надёжный партнёр в строительстве. Работаем с 2005 года."

NEW_HERO = """  <div class="hero-content">
    <div class="hero-tag">
      <span data-lang="tr">İnşaat ve Yapı — 2005'ten Beri</span>
      <span data-lang="en">Construction &amp; Building — Since 2005</span>
      <span data-lang="ru">Строительство — с 2005 года</span>
    </div>
    <h1 class="hero-h1">
      <span data-lang="tr">Sağlam ve Kalıcı<br><em>Yapılar İnşa Ediyoruz</em></span>
      <span data-lang="en">Building Solid &amp;<br><em>Lasting Structures</em></span>
      <span data-lang="ru">Возводим прочные и<br><em>долговечные здания</em></span>
    </h1>
    <p class="hero-p">
      <span data-lang="tr">Konuttan ticari tesislere, endüstriyel yapılardan tadilata — anahtar teslim inşaat çözümleri.</span>
      <span data-lang="en">From residential to commercial and industrial buildings — turnkey construction solutions.</span>
      <span data-lang="ru">От жилья до коммерческих и промышленных объектов — строительство «под ключ».</span>
    </p>
"""

NEW_ABOUT_P = """      <p class="sec-p">
        <span data-lang="tr">REF YAPI, 2005 yılında Türkiye'de kurulmuş; konut, ticari ve endüstriyel yapılarda anahtar teslim inşaat çözümleri sunmaktadır. Sağlam, işlevsel ve kalıcı yapılar inşa etmek için deneyimli kadromuzla yanınızdayız.</span>
        <span data-lang="en">Founded in Turkey in 2005, REF YAPI delivers turnkey construction solutions for residential, commercial and industrial buildings. Our experienced team builds solid, functional and lasting structures.</span>
        <span data-lang="ru">Основанная в Турции в 2005 году, REF YAPI реализует строительные проекты «под ключ» — жилые, коммерческие и промышленные объекты. Мы возводим прочные и функциональные здания.</span>
      </p>
      <ul class="about-list">
        <li><span data-lang="tr">İstanbul, Londra ve Taşkent ofisleriyle Türkiye, Birleşik Krallık, Özbekistan, Türkmenistan, Kazakistan ve daha birçok ülkede hizmet</span><span data-lang="en">Serving Turkey, the United Kingdom, Uzbekistan, Turkmenistan, Kazakhstan and more from our offices in Istanbul, London and Tashkent</span><span data-lang="ru">Обслуживание Турции, Великобритании, Узбекистана, Туркменистана, Казахстана и других стран через офисы в Стамбуле, Лондоне и Ташкенте</span></li>
        <li><span data-lang="tr">Konut, ticari, endüstriyel ve tadilat projelerinde uçtan uca uygulama</span><span data-lang="en">End-to-end delivery across residential, commercial, industrial and renovation projects</span><span data-lang="ru">Полный цикл работ: жильё, коммерция, промышленность и реконструкция</span></li>
        <li><span data-lang="tr">Anahtar teslim inşaat, proje yönetimi ve saha uygulaması</span><span data-lang="en">Turnkey construction, project management and on-site execution</span><span data-lang="ru">Строительство «под ключ», управление проектами и работы на площадке</span></li>
        <li><span data-lang="tr">Teslim sonrası destek ve bakım hizmetleri</span><span data-lang="en">Post-handover support and maintenance services</span><span data-lang="ru">Поддержка и обслуживание после сдачи объекта</span></li>
      </ul>"""

SERVICES = [
    {
        "id": "residential",
        "n": "01",
        "tr": "Konut İnşaatı",
        "en": "Residential Construction",
        "ru": "Жилищное строительство",
        "dtr": "Apartman, villa ve konut sitelerinde anahtar teslim inşaat.",
        "den": "Turnkey construction for apartments, villas and residential complexes.",
        "dru": "Строительство квартир, вилл и жилых комплексов «под ключ».",
        "ltr": "Yaşanabilir, sağlam ve zamanında teslim edilen konut projeleri — arsa hazırlığından teslimata kadar.",
        "len": "Liveable, solid homes delivered on time — from site preparation to handover.",
        "lru": "Надёжное жильё в срок — от подготовки площадки до сдачи.",
        "items": [
            ("Konut, villa ve site inşaatı", "Apartment, villa and residential complex construction", "Строительство жилья, вилл и комплексов"),
            ("İç ve dış mimari uygulama", "Interior and exterior architectural fit-out", "Внутренняя и внешняя отделка"),
            ("Şantiye yönetimi ve kalite kontrol", "Site management and quality control", "Управление площадкой и контроль качества"),
            ("Teslim ve iskan süreçleri", "Handover and occupancy processes", "Сдача и ввод в эксплуатацию"),
        ],
        "scope_tr": "Villa · Apartman · Site",
        "scope_en": "Villas · Apartments · Residences",
        "scope_ru": "Виллы · Квартиры · ЖК",
        "svg": '<svg class="sc-icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 30 32 12l22 18"/><path d="M16 28v24h32V28"/><path d="M26 52V36h12v16"/><path d="M22 24v-8h8"/></svg>',
    },
    {
        "id": "commercial",
        "n": "02",
        "tr": "Ticari ve Ofis Yapıları",
        "en": "Commercial Buildings",
        "ru": "Коммерческие здания",
        "dtr": "Ofis, AVM, otel ve kamu yapılarında inşaat ve uygulama.",
        "den": "Construction for offices, malls, hotels and public buildings.",
        "dru": "Строительство офисов, ТРЦ, отелей и общественных зданий.",
        "ltr": "Ticari yapılarda işlev, estetik ve işletme ihtiyaçlarını bir arada karşılayan inşaat çözümleri.",
        "len": "Construction that balances function, design and operations for commercial buildings.",
        "lru": "Строительные решения, сочетающие функцию, эстетику и эксплуатацию.",
        "items": [
            ("Ofis, AVM ve otel inşaatı", "Office, mall and hotel construction", "Офисы, ТРЦ и отели"),
            ("Cephe, çekirdek ve kaba yapı", "Facade, core and structural works", "Фасад, ядро и несущие конструкции"),
            ("İç mekân ve ortak alan uygulaması", "Interior and common-area fit-out", "Отделка интерьеров и общих зон"),
            ("İşletmeye alma ve teslim", "Commissioning and handover", "Ввод в эксплуатацию и сдача"),
        ],
        "scope_tr": "Ofis · Otel · AVM",
        "scope_en": "Offices · Hotels · Malls",
        "scope_ru": "Офисы · Отели · ТРЦ",
        "svg": '<svg class="sc-icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 52V18h18v34"/><path d="M30 52V10h22v42"/><path d="M16 24h10M16 32h10M16 40h10"/><path d="M36 18h10M36 26h10M36 34h10M36 42h10"/><path d="M8 52h48"/></svg>',
    },
    {
        "id": "industrial",
        "n": "03",
        "tr": "Endüstriyel Tesisler",
        "en": "Industrial Facilities",
        "ru": "Промышленные объекты",
        "dtr": "Fabrika, depo ve üretim tesislerinde ağır inşaat.",
        "den": "Heavy construction for factories, warehouses and production plants.",
        "dru": "Строительство заводов, складов и производственных объектов.",
        "ltr": "Üretim ve lojistik ihtiyaçlarına göre planlanan, dayanıklı endüstriyel yapılar.",
        "len": "Durable industrial buildings planned around production and logistics needs.",
        "lru": "Прочные промышленные здания под задачи производства и логистики.",
        "items": [
            ("Fabrika ve depo inşaatı", "Factory and warehouse construction", "Заводы и склады"),
            ("Çelik konstrüksiyon ve betonarme", "Steel structure and reinforced concrete", "Металлоконструкции и железобетон"),
            ("Altyapı, zemin ve rampa işleri", "Infrastructure, flooring and ramp works", "Инфраструктура, полы и рампы"),
            ("Tesis teslimi ve saha düzeni", "Facility handover and site layout", "Сдача объекта и организация площадки"),
        ],
        "scope_tr": "Fabrika · Depo · Üretim",
        "scope_en": "Factories · Warehouses · Plants",
        "scope_ru": "Заводы · Склады · Производство",
        "svg": '<svg class="sc-icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 52V28l16-8v8l16-8v32"/><path d="M40 52V24h16v28"/><path d="M44 32h8M44 40h8"/><path d="M14 36h6M14 44h6"/><path d="M8 52h48"/></svg>',
    },
    {
        "id": "turnkey",
        "n": "04",
        "tr": "Anahtar Teslim Projeler",
        "en": "Turnkey Projects",
        "ru": "Проекты «под ключ»",
        "dtr": "Tasarım, ruhsat, inşaat ve teslim — tek muhatap.",
        "den": "Design, permits, construction and handover — one partner.",
        "dru": "Проектирование, разрешения, строительство и сдача — один партнёр.",
        "ltr": "Projenizin tüm aşamalarını tek çatı altında yönetiyor; taahhüt, süre ve kaliteyi birlikte teslim ediyoruz.",
        "len": "We manage every stage under one roof — commitment, schedule and quality delivered together.",
        "lru": "Ведём все этапы под одной крышей — сроки, качество и обязательства вместе.",
        "items": [
            ("Keşif, fizibilite ve planlama", "Survey, feasibility and planning", "Изыскания, ТЭО и планирование"),
            ("Ruhsat ve resmi süreç takibi", "Permits and official process tracking", "Разрешения и официальные процедуры"),
            ("İnşaat, taşeron ve malzeme yönetimi", "Construction, subcontractor and materials management", "Строительство, подрядчики и материалы"),
            ("Tam teslim ve garanti", "Full handover and warranty", "Полная сдача и гарантия"),
        ],
        "scope_tr": "Konut · Ticari · Kamu",
        "scope_en": "Residential · Commercial · Public",
        "scope_ru": "Жильё · Коммерция · Госсектор",
        "svg": '<svg class="sc-icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h28v32H12z"/><path d="M20 20v-6a8 8 0 0 1 16 0v6"/><circle cx="26" cy="36" r="2.2"/><path d="M44 28h8l4 8v16H44"/></svg>',
    },
    {
        "id": "renovation",
        "n": "05",
        "tr": "Tadilat ve Restorasyon",
        "en": "Renovation & Restoration",
        "ru": "Реконструкция и реставрация",
        "dtr": "Mevcut yapıların yenilenmesi, güçlendirme ve restorasyon.",
        "den": "Renewal, strengthening and restoration of existing buildings.",
        "dru": "Обновление, усиление и реставрация существующих зданий.",
        "ltr": "Mevcut yapı stoğunu güçlendiriyor, yeniliyor ve çağdaş kullanıma hazırlıyoruz.",
        "len": "We strengthen, renew and prepare existing buildings for contemporary use.",
        "lru": "Усиливаем, обновляем и готовим существующие здания к современной эксплуатации.",
        "items": [
            ("İç ve dış tadilat", "Interior and exterior renovation", "Внутренняя и внешняя реконструкция"),
            ("Güçlendirme ve yapısal onarım", "Strengthening and structural repair", "Усиление и ремонт конструкций"),
            ("Cephe yenileme", "Facade renewal", "Обновление фасадов"),
            ("Kullanım dönüşümü", "Change-of-use conversions", "Смена назначения здания"),
        ],
        "scope_tr": "Konut · Ofis · Tarihi yapı",
        "scope_en": "Homes · Offices · Heritage",
        "scope_ru": "Жильё · Офисы · Наследие",
        "svg": '<svg class="sc-icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 44 36 22l8 8-22 22H14z"/><path d="M32 26l8 8"/><path d="M44 14c4 4 4 10 0 14"/><path d="M48 10c6 6 6 16 0 22"/></svg>',
    },
    {
        "id": "management",
        "n": "06",
        "tr": "Proje Yönetimi",
        "en": "Project Management",
        "ru": "Управление проектами",
        "dtr": "Süre, maliyet ve kaliteyi saha ve ofisten birlikte yönetiyoruz.",
        "den": "Schedule, cost and quality managed from site and office together.",
        "dru": "Сроки, бюджет и качество — с площадки и из офиса.",
        "ltr": "İnşaat sürecini planlıyor, koordineliyor ve raporluyoruz — sürprizsiz teslim için.",
        "len": "We plan, coordinate and report the build — for handover without surprises.",
        "lru": "Планируем, координируем и отчитываемся — сдача без сюрпризов.",
        "items": [
            ("İş programı ve bütçe kontrolü", "Programme and budget control", "График и контроль бюджета"),
            ("Taşeron ve tedarik koordinasyonu", "Subcontractor and supply coordination", "Координация подрядчиков и поставок"),
            ("Şantiye denetimi ve İSG", "Site supervision and HSE", "Надзор на площадке и охрана труда"),
            ("Hakediş, raporlama ve teslim", "Progress billing, reporting and handover", "Акты, отчётность и сдача"),
        ],
        "scope_tr": "Tüm proje tipleri",
        "scope_en": "All project types",
        "scope_ru": "Все типы проектов",
        "svg": '<svg class="sc-icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="12" y="12" width="40" height="40" rx="3"/><path d="M20 24h24M20 32h24M20 40h14"/><path d="M40 38l4 4 8-10"/></svg>',
    },
]


def lang(tr: str, en: str, ru: str) -> str:
    return (
        f'<span data-lang="tr">{tr}</span>'
        f'<span data-lang="en">{en}</span>'
        f'<span data-lang="ru">{ru}</span>'
    )


def build_services_html() -> str:
    cards = []
    panels = []
    for i, s in enumerate(SERVICES):
        delay = f"d{(i % 3) + 1}"
        active = " is-active" if i == 0 else ""
        pressed = "true" if i == 0 else "false"
        cards.append(
            f'''      <button type="button" class="sc-card rv {delay}{active}" data-service="{s["id"]}" aria-pressed="{pressed}">
        <span class="sc-n">{s["n"]}</span>
        {s["svg"]}
        <h3 class="sc-title">{lang(s["tr"], s["en"], s["ru"])}</h3>
        <p class="sc-desc">{lang(s["dtr"], s["den"], s["dru"])}</p>
        <span class="sc-more">{lang("Detaylar", "Details", "Подробнее")}<svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
      </button>'''
        )
        lis = "\n".join(
            f'          <li>{lang(tr, en, ru)}</li>' for tr, en, ru in s["items"]
        )
        panel_active = " is-active" if i == 0 else ""
        panels.append(
            f'''      <article class="svc-preview-panel{panel_active}" data-service="{s["id"]}" id="svc-{s["id"]}">
        <div class="svc-preview-grid">
          <div class="svc-preview-main">
            <span class="svc-preview-num">{s["n"]}</span>
            <h3 class="svc-preview-title">{lang(s["tr"], s["en"], s["ru"])}</h3>
            <p class="svc-preview-lead">{lang(s["ltr"], s["len"], s["lru"])}</p>
            <ul class="svc-preview-list">
{lis}
            </ul>
          </div>
          <aside class="svc-preview-side">
            <p class="svc-preview-meta-label">{lang("Kapsam", "Scope", "Охват")}</p>
            <p class="svc-preview-brands">{lang(s["scope_tr"], s["scope_en"], s["scope_ru"])}</p>
            <p class="svc-preview-meta-label">{lang("Teslim", "Delivery", "Сдача")}</p>
            <p class="svc-preview-apps">{lang("Anahtar teslim uygulama", "Turnkey execution", "Реализация «под ключ»")}</p>
            <div class="svc-preview-actions">
              <button type="button" class="btn btn-primary quote-trigger" data-service="{s["id"]}">{lang("Teklif Al", "Get Quote", "Смета")}</button>
            </div>
          </aside>
        </div>
      </article>'''
        )

    return f'''<!-- ═══════════════════════════════════════════ SERVICES -->
<section class="services" id="hizmetler">
  <div class="services-inner">
    <div class="services-top">
      <div>
        <span class="sec-eyebrow rv">{lang("Hizmetlerimiz", "Our Services", "Услуги")}</span>
        <h2 class="sec-h2 rv d1">
          <span data-lang="tr">Kapsamlı İnşaat<br><em>ve Yapı Çözümleri</em></span>
          <span data-lang="en">Comprehensive Construction<br><em>&amp; Building Solutions</em></span>
          <span data-lang="ru">Комплексное<br><em>строительство</em></span>
        </h2>
      </div>
      <p class="services-top-right rv d2">
        {lang(
            "Projenizin her aşamasında yanınızdayız — konuttan endüstriye, tadilattan anahtar teslime. Bir karta tıklayarak detayları görün.",
            "We are with you at every stage — from homes to industry, renovation to turnkey delivery. Click a card for details.",
            "Мы рядом на каждом этапе — от жилья до промышленности. Нажмите на карточку для подробностей.",
        )}
      </p>
    </div>

    <div class="sg sg-12">
{chr(10).join(cards)}
    </div>

    <div class="svc-preview" id="svcPreview" aria-live="polite">
      <div class="svc-preview-panels">
{chr(10).join(panels)}
      </div>
    </div>
  </div>
</section>
'''


def replace_hero(text: str) -> str:
    return re.sub(
        r'  <div class="hero-content">[\s\S]*?<p class="hero-p">[\s\S]*?</p>\n',
        NEW_HERO,
        text,
        count=1,
    )


def replace_about(text: str) -> str:
    text = text.replace(
        'src="assets/logo-mark.png?v=2"',
        'src="assets/logo-mark.png?v=3"',
    )
    text = re.sub(
        r'      <p class="sec-p">\s*<span data-lang="tr">FNV Elektronik, 2005[\s\S]*?</ul>',
        NEW_ABOUT_P,
        text,
        count=1,
    )
    text = text.replace(
        '<span data-lang="tr">Yaşam Kalitesini<br><em>Yükseltiyoruz</em></span>\n        <span data-lang="en">Elevating the<br><em>Quality of Life</em></span>\n        <span data-lang="ru">Повышаем<br><em>качество жизни</em></span>',
        '<span data-lang="tr">Kalıcı Yapılar<br><em>İnşa Ediyoruz</em></span>\n        <span data-lang="en">Building<br><em>Lasting Structures</em></span>\n        <span data-lang="ru">Возводим<br><em>долговечные здания</em></span>',
    )
    return text


def replace_services(text: str) -> str:
    return re.sub(
        r'<!-- ═══════════════════════════════════════════ SERVICES -->\n<section class="services" id="hizmetler">[\s\S]*?</section>\n\n<!-- ════════════════════════════════════════ OUR PRODUCTS -->',
        build_services_html() + "\n<!-- ════════════════════════════════════════ OUR PRODUCTS -->",
        text,
        count=1,
    )


def strip_products(text: str) -> str:
    return re.sub(
        r'\n<!-- ════════════════════════════════════════ OUR PRODUCTS -->\n<section class="products" id="urunlerimiz">[\s\S]*?</section>\n',
        "\n",
        text,
        count=1,
    )


def global_renames(text: str) -> str:
    reps = [
        ("Fnv Elektronik ve Bilgisayar Ltd. Şti.", "REF YAPI"),
        ("FNV Elektronik'in", "REF YAPI'nin"),
        ("FNV Elektronik's", "REF YAPI's"),
        ("офис FNV Elektronik", "офис REF YAPI"),
        ("Офис FNV Elektronik", "Офис REF YAPI"),
        ("FNV Elektronik", "REF YAPI"),
        ("info@fnvelektronik.com", "info@refyapi.com"),
        ("www.fnvelektronik.com", "www.refyapi.com"),
        ("https://www.fnvelektronik.com", "https://www.refyapi.com"),
        ("fnv-lang", "refyapi-lang"),
        ("assets/logo-white.png?v=2", "assets/logo-white.png?v=3"),
        ("assets/logo-mark.png?v=2", "assets/logo-mark.png?v=3"),
        ('href="assets/logo-mark.png"', 'href="assets/logo-icon.png"'),
        ("site.css?v=48", "site.css?v=49"),
        ("site.js?v=45", "site.js?v=46"),
        ("Elektrik Zayıf Akım Sistemleri", "İnşaat ve Yapı"),
        ("low-current electrical system solutions", "construction and building solutions"),
        ("low-current systems", "construction and building"),
        ("Low-Current Electrical Systems", "Construction &amp; Building"),
        ("слаботочных систем", "строительстве"),
        ("слаботочных системах", "строительстве"),
        ("Your trusted partner for low-current systems.", BRAND_SUB_EN),
        ("Надёжный партнёр в слаботочных системах. Работаем с 2005 года.", BRAND_SUB_RU),
        (
            "Elektrik Zayıf Akım Sistemleri alanında güvenilir çözüm ortağınız. 2005'ten bu yana hizmetinizdeyiz.",
            BRAND_SUB_TR,
        ),
        (
            "Elektrik Zayıf Akım Sistemleri alanında güvenilir çözüm ortağınız. Türkiye ve Londra.",
            "İnşaat ve yapı alanında güvenilir çözüm ortağınız. Türkiye ve Londra.",
        ),
        (
            "Elektrik Zayıf Akım Sistemleri alanında güvenilir çözüm ortağınız. Türkiye, Londra ve Orta Doğu/Asya.",
            "İnşaat ve yapı alanında güvenilir çözüm ortağınız. Türkiye, Londra ve Orta Doğu/Asya.",
        ),
        ("FNV Quote Request", "REF YAPI Quote Request"),
        ('alt="FNV Elektronik"', 'alt="REF YAPI"'),
        ("FNV Elektronik digital business card", "REF YAPI digital business card"),
        ("FNV Elektronik international project locations", "REF YAPI international project locations"),
        ("FNV Elektronik Istanbul office map", "REF YAPI Istanbul office map"),
        ("FNV Elektronik London office map", "REF YAPI London office map"),
        ("FNV Elektronik Middle East and Asia office map", "REF YAPI Middle East and Asia office map"),
        ("FNV Elektronik İstanbul ofisi", "REF YAPI İstanbul ofisi"),
        ("title>FNV Elektronik — İnşaat ve Yapı</title>", "title>REF YAPI — İnşaat ve Yapı</title>"),
    ]
    for a, b in reps:
        text = text.replace(a, b)
    text = text.replace(
        "https://www.instagram.com/fnvelektronik/",
        "#",
    )
    text = text.replace(
        "https://www.facebook.com/p/FNV-Elektronik-100063649779411/",
        "#",
    )
    return text


def strip_social_and_qr(text: str) -> str:
    text = re.sub(r'\n      <div class="ft-social">[\s\S]*?</div>\n', "\n", text)
    text = re.sub(r'\n      <div class="ft-qr">[\s\S]*?</div>\n', "\n", text)
    return text


def patch_nav_footer(text: str, is_index: bool) -> str:
    nav = NAV_HIZMET_INDEX if is_index else NAV_HIZMET_OTHER
    text, n = NAV_PRODUCTS_RE.subn(nav, text, count=1)
    if n == 0:
        print("  warn: no products nav found")
    services = FOOTER_SERVICES_INDEX if is_index else FOOTER_SERVICES_OTHER
    text, n = FOOTER_SERVICES_RE.subn(services, text, count=1)
    if n == 0:
        print("  warn: no footer services found")
    text = re.sub(
        r'\s*<li><a href="(?:index\.html)?#urunlerimiz">.*?</li>\n',
        "\n",
        text,
    )
    return text


def patch_office_copy(name: str, text: str) -> str:
    reps = {
        "istanbul.html": [
            (
                "2005'ten bu yana Türkiye'deki merkez ofisimiz; yangın algılama, güvenlik, otomasyon ve zayıf akım sistemlerinde anahtar teslim çözümler sunuyoruz.",
                "2005'ten bu yana Türkiye'deki merkez ofisimiz; konut, ticari ve endüstriyel yapılarda anahtar teslim inşaat çözümleri sunuyoruz.",
            ),
            (
                "Our headquarters in Turkey since 2005 — delivering turnkey fire detection, security, automation and low-current system solutions nationwide.",
                "Our headquarters in Turkey since 2005 — delivering turnkey construction for residential, commercial and industrial buildings nationwide.",
            ),
            (
                "Наш главный офис в Турции с 2005 года — комплексные решения в области слаботочных систем.",
                "Наш главный офис в Турции с 2005 года — комплексные строительные решения.",
            ),
            (
                "Maltepe'deki ofisimizden proje, kurulum, devreye alma ve bakım hizmetlerini yürütüyoruz. Türkiye genelinde otel, AVM, hastane ve endüstriyel tesislere hizmet veriyoruz.",
                "Maltepe'deki ofisimizden proje, inşaat, uygulama ve teslim süreçlerini yürütüyoruz. Türkiye genelinde konut, otel, ticari ve endüstriyel tesislere hizmet veriyoruz.",
            ),
            (
                "From our Maltepe office we manage design, installation, commissioning and maintenance — serving hotels, malls, hospitals and industrial facilities across Turkey.",
                "From our Maltepe office we manage design, construction and handover — serving residential, hotel, commercial and industrial facilities across Turkey.",
            ),
            (
                "Из офиса в Малтепе мы ведём проектирование, монтаж, пусконаладку и обслуживание объектов по всей Турции.",
                "Из офиса в Малтепе мы ведём проектирование, строительство и сдачу объектов по всей Турции.",
            ),
            (
                "7/24 teknik destek ve periyodik bakım",
                "Teslim sonrası destek ve bakım",
            ),
            (
                "24/7 technical support and periodic maintenance",
                "Post-handover support and maintenance",
            ),
            (
                "Техподдержка 24/7 и периодическое обслуживание",
                "Поддержка и обслуживание после сдачи",
            ),
        ],
        "london.html": [
            (
                "Birleşik Krallık'taki yeni temsilciliğimizle Avrupa pazarına adım atıyoruz. Londra ofisimiz yakında hizmetinizde olacak.",
                "Birleşik Krallık'taki yeni temsilciliğimizle Avrupa'daki inşaat projelerine yakından hizmet vereceğiz. Londra ofisimiz yakında hizmetinizde olacak.",
            ),
            (
                "We are expanding into the UK with a new London base — bringing FNV Elektronik's low-current expertise closer to European clients.",
                "We are expanding into the UK with a new London base — bringing REF YAPI's construction expertise closer to European clients.",
            ),
            (
                "Türkiye ve Birleşik Krallık'taki deneyimimizi yangın algılama, güvenlik, otomasyon ve zayıf akım sistemlerinde aynı anahtar teslim kaliteyle sunuyoruz.",
                "Türkiye ve Birleşik Krallık'taki deneyimimizi inşaat ve yapı projelerinde aynı anahtar teslim kaliteyle sunuyoruz.",
            ),
            (
                "We deliver the same turnkey quality in fire detection, security, automation and low-current systems across Turkey and the United Kingdom.",
                "We deliver the same turnkey quality in construction and building projects across Turkey and the United Kingdom.",
            ),
            (
                "Мы обеспечиваем то же качество комплексных решений в области пожарной сигнализации, безопасности, автоматизации и слаботочных систем в Турции и Великобритании.",
                "Мы обеспечиваем то же качество комплексных строительных решений в Турции и Великобритании.",
            ),
            (
                "Keşif, proje ve devreye alma desteği",
                "Keşif, proje ve inşaat desteği",
            ),
            (
                "Survey, design and commissioning support",
                "Survey, design and construction support",
            ),
        ],
        "middle-east-asia.html": [
            (
                "Taşkent merkezli ofisimizden Özbekistan, Türkmenistan, Kazakistan, Kırgızistan, Tacikistan ve daha birçok ülkede yangın algılama, güvenlik, otomasyon ve zayıf akım projeleri yürütüyoruz.",
                "Taşkent merkezli ofisimizden Özbekistan, Türkmenistan, Kazakistan, Kırgızistan, Tacikistan ve daha birçok ülkede inşaat ve yapı projeleri yürütüyoruz.",
            ),
            (
                "From our Tashkent hub we deliver fire detection, security, automation and low-current projects across Uzbekistan, Turkmenistan, Kazakhstan, Kyrgyzstan, Tajikistan and many more countries.",
                "From our Tashkent hub we deliver construction and building projects across Uzbekistan, Turkmenistan, Kazakhstan, Kyrgyzstan, Tajikistan and many more countries.",
            ),
            (
                "Из нашего центра в Ташкенте мы реализуем проекты пожарной сигнализации, безопасности, автоматизации и слаботочных систем в Узбекистане, Туркменистане, Казахстане, Киргизии, Таджикистане и многих других странах.",
                "Из нашего центра в Ташкенте мы реализуем строительные проекты в Узбекистане, Туркменистане, Казахстане, Киргизии, Таджикистане и многих других странах.",
            ),
            (
                "Keşif, proje, kurulum ve devreye alma",
                "Keşif, proje, inşaat ve teslim",
            ),
            (
                "Survey, design, installation and commissioning",
                "Survey, design, construction and handover",
            ),
        ],
    }
    for a, b in reps.get(name, []):
        if a not in text:
            print(f"  warn missing office string in {name}: {a[:60]}...")
        text = text.replace(a, b)
    return text


def soften_ref_tags(text: str) -> str:
    return re.sub(
        r'<div class="ref-tag">[\s\S]*?</div>',
        '<div class="ref-tag">'
        '<span data-lang="tr">İnşaat projesi</span>'
        '<span data-lang="en">Construction project</span>'
        '<span data-lang="ru">Строительный проект</span>'
        "</div>",
        text,
    )


def patch_index_extras(text: str) -> str:
    text = text.replace(
        "<title>REF YAPI — İnşaat ve Yapı</title>",
        "<title>REF YAPI — İnşaat ve Yapı</title>",
    )
    text = text.replace(
        "Teknik belgelerimiz, ürün katalogları, sertifikalar ve sistem şemalarına buradan ulaşabilirsiniz.",
        "Teknik belgelerimiz, kataloglar ve sertifikalara buradan ulaşabilirsiniz.",
    )
    text = text.replace(
        "Access our technical documents, product catalogues, certificates and system diagrams here.",
        "Access our technical documents, catalogues and certificates here.",
    )
    text = text.replace(
        "Здесь вы найдёте наши технические документы, каталоги, сертификаты и схемы систем.",
        "Здесь вы найдёте наши технические документы, каталоги и сертификаты.",
    )
    text = text.replace(
        "Ürün Kataloğu",
        "Şirket Kataloğu",
    )
    text = text.replace(
        "Product Catalogue",
        "Company Catalogue",
    )
    text = text.replace(
        "Каталог продукции",
        "Каталог компании",
    )
    text = text.replace(
        "Tüm ürün ve sistem çözümlerimizin detaylı kataloğu",
        "İnşaat ve yapı çözümlerimizin detaylı kataloğu",
    )
    text = text.replace(
        "Detailed catalogue of all our products and solutions",
        "Detailed catalogue of our construction and building solutions",
    )
    text = text.replace(
        "Подробный каталог продукции",
        "Подробный каталог строительных решений",
    )
    text = text.replace(
        "Ürün ve şirket sertifikaları",
        "Şirket sertifikaları",
    )
    text = text.replace(
        "Product and company certificates",
        "Company certificates",
    )
    text = text.replace(
        "Сертификаты продукции и компании",
        "Сертификаты компании",
    )
    text = text.replace(
        "Tüm Çözümleri Keşfedin",
        "Projelerimizi Keşfedin",
    )
    text = text.replace(
        "Explore All Solutions",
        "Explore Our Projects",
    )
    text = text.replace(
        "Изучить все решения",
        "Изучить наши проекты",
    )
    text = text.replace(
        "Tüm ürün ve sistem çözümlerimizi içeren dijital kataloğumuzu indirin.",
        "İnşaat ve yapı çözümlerimizi içeren dijital kataloğumuzu indirin.",
    )
    text = text.replace(
        "Download our digital catalogue covering all products and system solutions.",
        "Download our digital catalogue covering our construction and building solutions.",
    )
    text = text.replace(
        "Скачайте наш цифровой каталог со всеми продуктами и решениями.",
        "Скачайте наш цифровой каталог строительных решений.",
    )
    text = text.replace(
        '<div class="stat-n" data-target="6">0</div>',
        '<div class="stat-n" data-target="6">0</div>',
    )
    return text


def patch_js(text: str) -> str:
    text = text.replace("fnv-lang", "refyapi-lang")
    text = text.replace("info@fnvelektronik.com", "info@refyapi.com")
    text = text.replace("FNV Quote Request", "REF YAPI Quote Request")
    old = """const SERVICE_OPTIONS = [
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
];"""
    new = """const SERVICE_OPTIONS = [
  { v: 'residential', tr: 'Konut İnşaatı', en: 'Residential Construction', ru: 'Жилищное строительство' },
  { v: 'commercial', tr: 'Ticari ve Ofis Yapıları', en: 'Commercial Buildings', ru: 'Коммерческие здания' },
  { v: 'industrial', tr: 'Endüstriyel Tesisler', en: 'Industrial Facilities', ru: 'Промышленные объекты' },
  { v: 'turnkey', tr: 'Anahtar Teslim Projeler', en: 'Turnkey Projects', ru: 'Проекты «под ключ»' },
  { v: 'renovation', tr: 'Tadilat ve Restorasyon', en: 'Renovation & Restoration', ru: 'Реконструкция' },
  { v: 'management', tr: 'Proje Yönetimi', en: 'Project Management', ru: 'Управление проектами' },
  { v: 'general', tr: 'Genel / Diğer', en: 'General / Other', ru: 'Общий / Другое' },
];"""
    if old not in text:
        raise SystemExit("SERVICE_OPTIONS block not found")
    text = text.replace(old, new)
    text = re.sub(
        r"  document\.querySelectorAll\('\.prod-svc-chip'\)[\s\S]*?\n  \}\);\n\n  const hash",
        "  const hash",
        text,
        count=1,
    )
    return text


KEEP_PAGES = {
    "index.html",
    "documents.html",
    "references.html",
    "istanbul.html",
    "london.html",
    "middle-east-asia.html",
    "privacy-policy.html",
    "cookie-policy.html",
}

DELETE_PAGES = [
    "integrated-building-systems.html",
    "security-systems.html",
    "data-communications.html",
    "tv-video-systems.html",
    "fire-detection.html",
    "audio-visual-systems.html",
    "automation-systems.html",
]


def patch_css(text: str) -> str:
    text = text.replace(
        ".nav-logo img { height: 42px; object-fit: contain; transition: opacity .4s; }",
        ".nav-logo img { height: 46px; width: auto; max-width: 220px; object-fit: contain; transition: opacity .4s; }",
    )
    text = text.replace(
        ".about-logo { max-width: 220px; width: 100%; height: auto; display: block; }",
        ".about-logo { max-width: 380px; width: 100%; height: auto; display: block; }",
    )
    text = text.replace(
        ".ft-brand-logo { height: 38px; margin-bottom: 18px; opacity: .9; }",
        ".ft-brand-logo { height: 44px; width: auto; max-width: 220px; margin-bottom: 18px; opacity: .9; object-fit: contain; }",
    )
    return text


def main() -> None:
    process_logos()

    js_path = ASSETS / "site.js"
    js_path.write_text(patch_js(js_path.read_text(encoding="utf-8")), encoding="utf-8")
    print("patched site.js")

    css_path = ASSETS / "site.css"
    css_path.write_text(patch_css(css_path.read_text(encoding="utf-8")), encoding="utf-8")
    print("patched site.css")

    for path in sorted(ROOT.glob("*.html")):
        if path.name not in KEEP_PAGES:
            continue
        text = path.read_text(encoding="utf-8")
        is_index = path.name == "index.html"
        if is_index:
            text = replace_hero(text)
            text = replace_about(text)
            text = replace_services(text)
            text = strip_products(text)
            text = patch_index_extras(text)
        if path.name in {"istanbul.html", "london.html", "middle-east-asia.html"}:
            text = patch_office_copy(path.name, text)
        if path.name in {"index.html", "references.html"}:
            text = soften_ref_tags(text)
        text = patch_nav_footer(text, is_index)
        text = global_renames(text)
        text = strip_social_and_qr(text)
        path.write_text(text, encoding="utf-8")
        print("patched", path.name)

    for name in DELETE_PAGES:
        p = ROOT / name
        if p.exists():
            p.unlink()
            print("deleted", name)

    leftover = []
    for p in ROOT.rglob("*"):
        if p.suffix.lower() not in {".html", ".js", ".py", ".css"}:
            continue
        if "scripts/rebrand-refyapi.py" in str(p):
            continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"FNV|fnvelektronik|Ürünlerimiz|#urunlerimiz|Honeywell", t):
            leftover.append(p.relative_to(ROOT))
    print("leftover mentions:", leftover)


if __name__ == "__main__":
    main()
