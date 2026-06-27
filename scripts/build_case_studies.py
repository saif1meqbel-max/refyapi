#!/usr/bin/env python3
"""Generate case study pages and patch reference cards."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROJECTS = [
    {
        "slug": "project-bera-otel",
        "file": "project-bera-otel.html",
        "img": "ref01-bera-otel.png",
        "year": "2007",
        "sector_tr": "Otel", "sector_en": "Hotel", "sector_ru": "Отель",
        "area_tr": "—", "area_en": "—", "area_ru": "—",
        "loc_tr": "Antalya, Türkiye", "loc_en": "Antalya, Turkey", "loc_ru": "Анталья, Турция",
        "title": "Bera Otel",
        "systems": [
            ("Acil Anons", "PA", "Оповещение"),
            ("CCTV", "CCTV", "CCTV"),
            ("Kartlı Geçiş", "Access Control", "Контроль доступа"),
            ("TV", "TV", "ТВ"),
        ],
        "desc_tr": "Antalya'daki Bera Otel için acil anons, CCTV, kartlı geçiş ve TV altyapısı projelendirildi, kuruldu ve devreye alındı. Konuk güvenliği ve operasyonel verimlilik için entegre zayıf akım çözümleri sunuldu.",
        "desc_en": "For Bera Hotel in Antalya, we designed, installed and commissioned integrated PA, CCTV, access control and TV infrastructure — delivering low-current solutions for guest safety and operational efficiency.",
        "desc_ru": "Для отеля Bera в Анталье мы спроектировали и смонтировали интегрированные системы оповещения, CCTV, контроля доступа и телевидения.",
        "scope_tr": ["PA ve ses yayın altyapısı", "IP/analog kamera ve izleme", "Kartlı geçiş ve turnike entegrasyonu", "Oda TV dağıtım sistemi", "Saha testi ve kullanıcı eğitimi"],
        "scope_en": ["PA and broadcast infrastructure", "IP/analog camera and monitoring", "Access control integration", "In-room TV distribution", "Site testing and user training"],
        "scope_ru": ["Система оповещения", "CCTV и мониторинг", "Контроль доступа", "Телевизионная сеть", "Пусконаладка и обучение"],
        "related": ["project-devlet-sahil-evleri", "project-mega-rostov"],
    },
    {
        "slug": "project-devlet-sahil-evleri",
        "file": "project-devlet-sahil-evleri.html",
        "img": "ref02-devlet-sahil-evleri.png",
        "year": "2008",
        "sector_tr": "Konut / Tesis", "sector_en": "Residential", "sector_ru": "Жилой комплекс",
        "area_tr": "23.000 m²", "area_en": "23,000 m²", "area_ru": "23 000 м²",
        "loc_tr": "Azerbaycan", "loc_en": "Azerbaijan", "loc_ru": "Азербайджан",
        "title": "Devlet Sahil Evleri Tesisleri",
        "systems": [
            ("Yangın Algılama", "Fire Detection", "Пожарная сигнализация"),
            ("CCTV", "CCTV", "CCTV"),
        ],
        "desc_tr": "Azerbaycan'daki 23.000 m²'lik Devlet Sahil Evleri tesislerinde yangın algılama ve CCTV sistemleri kuruldu. Geniş saha alanında erken uyarı ve güvenlik izlemesi sağlandı.",
        "desc_en": "Fire detection and CCTV systems were delivered across the 23,000 m² Devlet Sahil Evleri site in Azerbaijan, providing early warning and security monitoring at scale.",
        "desc_ru": "На объекте Devlet Sahil Evleri площадью 23 000 м² в Азербайджане установлены пожарная сигнализация и CCTV.",
        "scope_tr": ["Adresli yangın algılama paneli ve dedektörler", "CCTV kamera ağı ve kayıt", "Yangın senaryoları ve alarm entegrasyonu", "Merkezi izleme odası altyapısı", "Periyodik bakım planı"],
        "scope_en": ["Addressable fire panels and detectors", "CCTV network and recording", "Alarm scenarios and integration", "Central monitoring infrastructure", "Maintenance planning"],
        "scope_ru": ["Адресная пожарная сигнализация", "Сеть CCTV", "Интеграция сигнализации", "Центральный мониторинг", "План обслуживания"],
        "related": ["project-bera-otel", "project-mega-rostov"],
    },
    {
        "slug": "project-mega-rostov",
        "file": "project-mega-rostov.html",
        "img": "ref03-mega-rostov.png",
        "year": "2008",
        "sector_tr": "AVM", "sector_en": "Shopping Mall", "sector_ru": "Торговый центр",
        "area_tr": "253.861 m²", "area_en": "253,861 m²", "area_ru": "253 861 м²",
        "loc_tr": "Rusya", "loc_en": "Russia", "loc_ru": "Россия",
        "title": "Mega Rostov Alışveriş Merkezi",
        "systems": [
            ("CCTV", "CCTV", "CCTV"),
            ("Kartlı Geçiş", "Access Control", "Контроль доступа"),
        ],
        "desc_tr": "253.861 m² alana sahip Mega Rostov AVM'de kapsamlı CCTV ve kartlı geçiş sistemleri kuruldu. Yüksek trafikli perakende ortamında güvenlik ve erişim yönetimi sağlandı.",
        "desc_en": "Comprehensive CCTV and access control were installed at the 253,861 m² Mega Rostov shopping centre — securing high-traffic retail environments and managing staff access.",
        "desc_ru": "В торговом центре Mega Rostov площадью 253 861 м² установлены CCTV и контроль доступа.",
        "scope_tr": ["Yüzlerce kamera noktası ve NVR altyapısı", "Personel ve servis alanı erişim kontrolü", "Merkezi güvenlik odası", "Kayıt saklama ve arşivleme", "7/24 teknik destek"],
        "scope_en": ["Large-scale camera and NVR infrastructure", "Staff and service area access control", "Central security room", "Recording and archiving", "24/7 technical support"],
        "scope_ru": ["Масштабная CCTV", "Контроль доступа персонала", "Центр безопасности", "Архивирование", "Поддержка 24/7"],
        "related": ["project-devlet-sahil-evleri", "project-savunma-bakanligi"],
    },
    {
        "slug": "project-savunma-bakanligi",
        "file": "project-savunma-bakanligi.html",
        "img": "ref04-savunma-bakanligi.png",
        "year": "2011",
        "sector_tr": "Kamu", "sector_en": "Government", "sector_ru": "Госсектор",
        "area_tr": "—", "area_en": "—", "area_ru": "—",
        "loc_tr": "Türkmenistan", "loc_en": "Turkmenistan", "loc_ru": "Туркменистан",
        "title": "Savunma Bakanlığı Olağanüstü Hal Bakanlığı",
        "systems": [
            ("Yangın Algılama", "Fire Detection", "Пожарная сигнализация"),
            ("Acil Anons", "PA", "Оповещение"),
            ("CCTV", "CCTV", "CCTV"),
            ("Kartlı Geçiş", "Access Control", "Контроль доступа"),
        ],
        "desc_tr": "Türkmenistan'daki bakanlık binasında yangın algılama, acil anons, CCTV ve kartlı geçiş sistemlerinin entegre kurulumu gerçekleştirildi. Kritik kamu altyapısı için uçtan uca güvenlik çözümü sunuldu.",
        "desc_en": "Integrated fire detection, PA, CCTV and access control were delivered for this ministry building in Turkmenistan — an end-to-end security solution for critical government infrastructure.",
        "desc_ru": "В здании министерства в Туркменистане установлены интегрированные системы пожарной сигнализации, оповещения, CCTV и контроля доступа.",
        "scope_tr": ["Çok bölgeli yangın algılama", "Sesli tahliye ve anons", "Perimeter ve iç CCTV", "Zonal erişim kontrolü", "Entegrasyon ve devreye alma"],
        "scope_en": ["Multi-zone fire detection", "Voice evacuation and PA", "Perimeter and internal CCTV", "Zoned access control", "Integration and commissioning"],
        "scope_ru": ["Многозонная пожарная сигнализация", "Голосовое оповещение", "CCTV", "Контроль доступа", "Пусконаладка"],
        "related": ["project-buz-kosku", "project-mega-rostov"],
    },
    {
        "slug": "project-buz-kosku",
        "file": "project-buz-kosku.html",
        "img": "ref05-buz-kosku.png",
        "year": "2011",
        "sector_tr": "Kültürel Tesis", "sector_en": "Cultural Venue", "sector_ru": "Культурный объект",
        "area_tr": "72.400 m²", "area_en": "72,400 m²", "area_ru": "72 400 м²",
        "loc_tr": "Türkmenistan", "loc_en": "Turkmenistan", "loc_ru": "Туркmenistan",
        "title": "Buz Köşkü",
        "systems": [("Yangın Algılama", "Fire Detection", "Пожарная сигнализация")],
        "desc_tr": "72.400 m²'lik Buz Köşkü kompleksinde adresli yangın algılama sistemi kuruldu. Büyük hacimli yapıda hızlı müdahale için erken uyarı altyapısı oluşturuldu.",
        "desc_en": "Addressable fire detection was installed across the 72,400 m² Buz Köşkü complex, creating early-warning infrastructure for rapid response in a large-volume building.",
        "desc_ru": "В комплексе Buz Köşkü площадью 72 400 м² установлена адресная пожарная сигнализация.",
        "scope_tr": ["Adresli yangın paneli", "Duman ve ısı dedektörleri", "Manuel çağrı noktaları", "Sesli/ışıklı uyarıcılar", "Test ve bakım prosedürleri"],
        "scope_en": ["Addressable fire panel", "Smoke and heat detectors", "Manual call points", "Sounders and beacons", "Testing and maintenance"],
        "scope_ru": ["Адресная панель", "Датчики дыма и тепла", "Ручные извещатели", "Сирены и маяки", "Обслуживание"],
        "related": ["project-pamukyagi-fabrikasi", "project-savunma-bakanligi"],
    },
    {
        "slug": "project-pamukyagi-fabrikasi",
        "file": "project-pamukyagi-fabrikasi.html",
        "img": "ref06-pamukyagi-fabrikasi.png",
        "year": "2011",
        "sector_tr": "Endüstriyel", "sector_en": "Industrial", "sector_ru": "Промышленность",
        "area_tr": "22.000 m²", "area_en": "22,000 m²", "area_ru": "22 000 м²",
        "loc_tr": "Türkmenistan", "loc_en": "Turkmenistan", "loc_ru": "Туркменistan",
        "title": "Pamukyağı Fabrikası",
        "systems": [("Yangın Algılama", "Fire Detection", "Пожарная сигнализация")],
        "desc_tr": "22.000 m²'lik pamukyağı fabrikasında endüstriyel yangın algılama sistemi kuruldu. Toz ve yüksek sıcaklık ortamına uygun dedektör seçimi ve zonlama yapıldı.",
        "desc_en": "Industrial fire detection was installed at the 22,000 m² cotton oil factory, with detector selection and zoning suited to dust and high-temperature environments.",
        "desc_ru": "На фабрике хлопкового масла площадью 22 000 м² установлена промышленная пожарная сигнализация.",
        "scope_tr": ["Endüstriyel yangın paneli", "Ortama uygun dedektörler", "Zon bazlı alarm yönetimi", "Fabrika otomasyon entegrasyonu", "Periyodik test programı"],
        "scope_en": ["Industrial fire panel", "Environment-suited detectors", "Zone-based alarm management", "Factory automation integration", "Periodic test programme"],
        "scope_ru": ["Промышленная панель", "Специальные датчики", "Зональная сигнализация", "Интеграция с автоматизацией", "План испытаний"],
        "related": ["project-buz-kosku", "project-bera-otel"],
    },
]

BY_SLUG = {p["slug"]: p for p in PROJECTS}

NAV_QUOTE = '''    <button type="button" class="btn-nav-quote quote-trigger">
      <span data-lang="tr">Teklif Al</span><span data-lang="en">Get Quote</span><span data-lang="ru">Смета</span>
    </button>
'''

HEAD = '''<!DOCTYPE html>
<html lang="tr">
<head>
  <script>try{{var l=localStorage.getItem('fnv-lang');if(l==='en'||l==='ru')document.documentElement.classList.add('lang-'+l);}}catch(e){{}}</script>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="icon" href="assets/logo-mark.png" type="image/png" />
  <link rel="apple-touch-icon" href="assets/logo-mark.png" />
  <title>{title} — FNV Elektronik</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/site.css?v=19" />
</head>
<body>
'''

NAV = '''
<nav class="nav solid" id="mainNav">
  <a href="index.html" class="nav-logo">
    <img class="logo-light" src="assets/logo-white.png?v=2" alt="FNV Elektronik">
    <img class="logo-dark" src="assets/logo-mark.png" alt="FNV Elektronik">
  </a>
  <ul class="nav-links">
    <li><a href="index.html#hakkimizda"><span data-lang="tr">Hakkımızda</span><span data-lang="en">About Us</span><span data-lang="ru">О нас</span></a></li>
    <li>
      <a href="index.html#urunlerimiz"><span data-lang="tr">Ürünlerimiz</span><span data-lang="en">Our Products</span><span data-lang="ru">Продукты</span><span class="dd-arrow">▾</span></a>
      <ul class="dd">
        <li><a href="fire-detection.html"><span data-lang="tr">Yangın Algılama ve Uyarı Sistemleri</span><span data-lang="en">Fire Detection &amp; Alarm</span><span data-lang="ru">Пожарная сигнализация</span></a></li>
        <li><a href="security-systems.html"><span data-lang="tr">Güvenlik Sistemleri</span><span data-lang="en">Security Systems</span><span data-lang="ru">Системы безопасности</span></a></li>
        <li><a href="automation-systems.html"><span data-lang="tr">Otomasyon Sistemleri</span><span data-lang="en">Automation Systems</span><span data-lang="ru">Автоматизация</span></a></li>
        <li><a href="audio-visual-systems.html"><span data-lang="tr">Ses ve Işık Sistemleri</span><span data-lang="en">Audio &amp; Visual Systems</span><span data-lang="ru">Аудио и свет</span></a></li>
        <li><a href="data-communications.html"><span data-lang="tr">Data ve İletişim Sistemleri</span><span data-lang="en">Data &amp; Communications</span><span data-lang="ru">Связь и данные</span></a></li>
        <li><a href="tv-video-systems.html"><span data-lang="tr">TV ve Görüntü Sistemleri</span><span data-lang="en">TV &amp; Video Systems</span><span data-lang="ru">ТВ и видео</span></a></li>
      </ul>
    </li>
    <li><a href="documents.html"><span data-lang="tr">Teknik Kitaplık</span><span data-lang="en">Tech Library</span><span data-lang="ru">Библиотека</span></a></li>
    <li><a href="references.html"><span data-lang="tr">Referanslarımız</span><span data-lang="en">References</span><span data-lang="ru">Референции</span></a></li>
    <li class="nav-offices">
      <a href="index.html#iletisim"><span data-lang="tr">Ofisler</span><span data-lang="en">Offices</span><span data-lang="ru">Офисы</span><span class="dd-arrow">▾</span></a>
      <ul class="dd">
        <li><a href="istanbul.html"><span data-lang="tr">İstanbul Ofisi</span><span data-lang="en">Istanbul Office</span><span data-lang="ru">Офис в Стамбуле</span></a></li>
        <li><a href="tashkent.html"><span data-lang="tr">Taşkent Ofisi</span><span data-lang="en">Tashkent Office</span><span data-lang="ru">Офис в Ташкенте</span></a></li>
        <li><a href="london.html"><span data-lang="tr">Londra Ofisi</span><span data-lang="en">London Office</span><span data-lang="ru">Офис в Лондоне</span></a></li>
      </ul>
    </li>
    <li><a href="index.html#iletisim"><span data-lang="tr">İletişim</span><span data-lang="en">Contact</span><span data-lang="ru">Контакт</span></a></li>
  </ul>
  <div class="nav-right">
''' + NAV_QUOTE + '''    <button class="lbtn on" onclick="setLang('tr')">TR</button>
    <button class="lbtn" onclick="setLang('en')">EN</button>
    <button class="lbtn" onclick="setLang('ru')">RU</button>
    <button class="hbg" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</nav>
'''

FOOTER = '''
<footer>
  <div class="ft-top">
    <div>
      <img class="ft-brand-logo" src="assets/logo-white.png?v=2" alt="FNV Elektronik">
      <p class="ft-brand-sub">
        <span data-lang="tr">Elektrik Zayıf Akım Sistemleri alanında güvenilir çözüm ortağınız.</span>
        <span data-lang="en">Your trusted partner for low-current electrical systems.</span>
        <span data-lang="ru">Надёжный партнёр в слаботочных системах.</span>
      </p>
    </div>
    <div>
      <p class="ft-col-head"><span data-lang="tr">Hizmetler</span><span data-lang="en">Services</span><span data-lang="ru">Услуги</span></p>
      <ul class="ft-links">
        <li><a href="fire-detection.html"><span data-lang="tr">Yangın Sistemleri</span><span data-lang="en">Fire Systems</span><span data-lang="ru">Пожарные системы</span></a></li>
        <li><a href="security-systems.html"><span data-lang="tr">Güvenlik Sistemleri</span><span data-lang="en">Security Systems</span><span data-lang="ru">Системы безопасности</span></a></li>
        <li><a href="references.html"><span data-lang="tr">Referanslarımız</span><span data-lang="en">References</span><span data-lang="ru">Референции</span></a></li>
      </ul>
    </div>
    <div>
      <p class="ft-col-head"><span data-lang="tr">Şirket</span><span data-lang="en">Company</span><span data-lang="ru">Компания</span></p>
      <ul class="ft-links">
        <li><a href="index.html#hakkimizda"><span data-lang="tr">Hakkımızda</span><span data-lang="en">About Us</span><span data-lang="ru">О нас</span></a></li>
        <li><a href="references.html"><span data-lang="tr">Referanslarımız</span><span data-lang="en">References</span><span data-lang="ru">Референции</span></a></li>
        <li><a href="index.html#iletisim"><span data-lang="tr">İletişim</span><span data-lang="en">Contact</span><span data-lang="ru">Контакт</span></a></li>
      </ul>
    </div>
    <div>
      <p class="ft-col-head"><span data-lang="tr">İletişim</span><span data-lang="en">Contact</span><span data-lang="ru">Контакт</span></p>
      <ul class="ft-links">
        <li><a href="tel:+902164413350">+90 216 441 33 50</a></li>
        <li><a href="mailto:info@fnvelektronik.com">info@fnvelektronik.com</a></li>
      </ul>
    </div>
  </div>
  <div class="ft-bottom">
    <span>© 2024 FNV Elektronik · <span data-lang="tr">Tüm Hakları Saklıdır</span><span data-lang="en">All Rights Reserved</span><span data-lang="ru">Все права защищены</span></span>
    <span>İstanbul · Taşkent · London</span>
  </div>
</footer>
<script src="assets/site.js?v=19"></script>
</body>
</html>
'''


def pills(p):
    return "\n".join(
        f'          <span class="case-system-pill"><span data-lang="tr">{tr}</span><span data-lang="en">{en}</span><span data-lang="ru">{ru}</span></span>'
        for tr, en, ru in p["systems"]
    )


def scope_items(p, lang_key):
    key = {"tr": "scope_tr", "en": "scope_en", "ru": "scope_ru"}[lang_key]
    items = p[key]
    return "\n".join(f"        <li>{item}</li>" for item in items)


def related_cards(p):
    out = []
    for slug in p["related"]:
        r = BY_SLUG[slug]
        out.append(f'''      <a href="{r["file"]}" class="case-related-card">
        <img src="assets/projects/{r["img"]}" alt="{r["title"]}" loading="lazy" />
        <div class="case-related-card-body">
          <div class="case-related-card-title">{r["title"]}</div>
          <div class="case-related-card-year">{r["year"]}</div>
        </div>
      </a>''')
    return "\n".join(out)


def render_page(p):
    scope_tr = scope_items(p, "tr")
    scope_en = scope_items(p, "en")
    scope_ru = scope_items(p, "ru")
    # unified scope with trilingual spans per item
    scope_html = ""
    for tr, en, ru in zip(p["scope_tr"], p["scope_en"], p["scope_ru"]):
        scope_html += f"        <li><span data-lang=\"tr\">{tr}</span><span data-lang=\"en\">{en}</span><span data-lang=\"ru\">{ru}</span></li>\n"

    return HEAD.format(title=p["title"]) + NAV + f'''
<section class="svc-hero office-hero" style="min-height:320px;padding-bottom:0">
  <div class="svc-hero-content" style="padding-bottom:32px">
    <div class="crumb">
      <a href="index.html"><span data-lang="tr">Ana Sayfa</span><span data-lang="en">Home</span><span data-lang="ru">Главная</span></a>
      <span class="sep">/</span>
      <a href="references.html"><span data-lang="tr">Referanslar</span><span data-lang="en">References</span><span data-lang="ru">Референции</span></a>
      <span class="sep">/</span>
      <span class="cur">{p["title"]}</span>
    </div>
    <span class="svc-hero-eyebrow"><span data-lang="tr">Proje Vaka Çalışması</span><span data-lang="en">Project Case Study</span><span data-lang="ru">Кейс проекта</span></span>
    <h1 class="svc-hero-title">{p["title"]}</h1>
  </div>
</section>
<img class="case-hero-img" src="assets/projects/{p["img"]}" alt="{p["title"]}" />

<div class="case-meta-bar">
  <div class="case-meta-inner">
    <div class="case-meta-item">
      <div class="case-meta-label"><span data-lang="tr">Yıl</span><span data-lang="en">Year</span><span data-lang="ru">Год</span></div>
      <div class="case-meta-value">{p["year"]}</div>
    </div>
    <div class="case-meta-item">
      <div class="case-meta-label"><span data-lang="tr">Konum</span><span data-lang="en">Location</span><span data-lang="ru">Локация</span></div>
      <div class="case-meta-value"><span data-lang="tr">{p["loc_tr"]}</span><span data-lang="en">{p["loc_en"]}</span><span data-lang="ru">{p["loc_ru"]}</span></div>
    </div>
    <div class="case-meta-item">
      <div class="case-meta-label"><span data-lang="tr">Alan</span><span data-lang="en">Area</span><span data-lang="ru">Площадь</span></div>
      <div class="case-meta-value"><span data-lang="tr">{p["area_tr"]}</span><span data-lang="en">{p["area_en"]}</span><span data-lang="ru">{p["area_ru"]}</span></div>
    </div>
    <div class="case-meta-item">
      <div class="case-meta-label"><span data-lang="tr">Sektör</span><span data-lang="en">Sector</span><span data-lang="ru">Сектор</span></div>
      <div class="case-meta-value"><span data-lang="tr">{p["sector_tr"]}</span><span data-lang="en">{p["sector_en"]}</span><span data-lang="ru">{p["sector_ru"]}</span></div>
    </div>
  </div>
</div>

<section class="case-body">
  <div class="case-body-inner">
    <div>
      <span class="sec-eyebrow"><span data-lang="tr">Proje Özeti</span><span data-lang="en">Project Overview</span><span data-lang="ru">Обзор проекта</span></span>
      <h2 class="sec-h2"><span data-lang="tr">Kapsam ve <em>Çözümler</em></span><span data-lang="en">Scope &amp; <em>Solutions</em></span><span data-lang="ru">Объём и <em>решения</em></span></h2>
      <div class="rule"></div>
      <p class="sec-p">
        <span data-lang="tr">{p["desc_tr"]}</span>
        <span data-lang="en">{p["desc_en"]}</span>
        <span data-lang="ru">{p["desc_ru"]}</span>
      </p>
      <div class="case-systems">
{pills(p)}
      </div>
    </div>
    <aside class="case-sidebar">
      <h3><span data-lang="tr">Teslim Edilenler</span><span data-lang="en">Deliverables</span><span data-lang="ru">Результаты</span></h3>
      <ul class="case-sidebar-list">
{scope_html}      </ul>
      <button type="button" class="btn-primary quote-trigger" style="width:100%;margin-top:24px;justify-content:center;border:none;cursor:pointer">
        <span data-lang="tr">Benzer Proje İçin Teklif Al</span>
        <span data-lang="en">Get Quote for Similar Project</span>
        <span data-lang="ru">Запросить смету</span>
      </button>
    </aside>
  </div>
</section>

<section class="case-related">
  <div class="case-related-inner">
    <span class="sec-eyebrow"><span data-lang="tr">Diğer Projeler</span><span data-lang="en">More Projects</span><span data-lang="ru">Другие проекты</span></span>
    <h2 class="sec-h2"><span data-lang="tr">İlgili <em>Referanslar</em></span><span data-lang="en">Related <em>References</em></span><span data-lang="ru">Похожие <em>проекты</em></span></h2>
    <div class="case-related-grid">
{related_cards(p)}
    </div>
  </div>
</section>

<section class="catalog">
  <div class="catalog-inner">
    <div class="catalog-left">
      <div class="catalog-tag"><span data-lang="tr">Teklif Alın</span><span data-lang="en">Request a Quote</span><span data-lang="ru">Запросить смету</span></div>
      <h2><span data-lang="tr">Projenizi Bizimle Planlayın</span><span data-lang="en">Plan Your Project With Us</span><span data-lang="ru">Спланируйте проект с нами</span></h2>
      <p><span data-lang="tr">Ücretsiz keşif ve detaylı teklif için formu doldurun.</span><span data-lang="en">Fill in the form for a free survey and detailed quote.</span><span data-lang="ru">Заполните форму для бесплатного осмотра и сметы.</span></p>
    </div>
    <button type="button" class="btn-white quote-trigger">
      <span data-lang="tr">Teklif Formu</span><span data-lang="en">Quote Form</span><span data-lang="ru">Форма запроса</span>
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </button>
  </div>
</section>
''' + FOOTER


REF_MAP = [
    ("ref01-bera-otel", "project-bera-otel.html"),
    ("ref02-devlet-sahil-evleri", "project-devlet-sahil-evleri.html"),
    ("ref03-mega-rostov", "project-mega-rostov.html"),
    ("ref04-savunma-bakanligi", "project-savunma-bakanligi.html"),
    ("ref05-buz-kosku", "project-buz-kosku.html"),
    ("ref06-pamukyagi-fabrikasi", "project-pamukyagi-fabrikasi.html"),
]

HINT = '''        <span class="ref-card-hint"><span data-lang="tr">Projeyi Gör</span><span data-lang="en">View Project</span><span data-lang="ru">Смотреть</span><svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
'''


def patch_ref_cards(html: str) -> str:
    import re
    for img_slug, href in REF_MAP:
        pattern = rf'(<div class="ref-card[^"]*">\s*<div class="ref-imgwrap">\s*<img class="ref-img" src="assets/projects/{img_slug}\.png"[^/]*/>\s*<span class="ref-year">[^<]+</span>\s*</div>\s*<div class="ref-body">.*?</div>\s*)</div>'
        def repl(m):
            inner = m.group(1)
            if "ref-card-hint" in inner:
                return m.group(0)
            inner = inner.replace("<div class=\"ref-card", "<a href=\"" + href + "\" class=\"ref-card ref-card-link", 1)
            inner = inner.rstrip() + "\n" + HINT + "\n      "
            return inner + "</a>"
        html = re.sub(pattern, repl, html, count=1, flags=re.S)
    return html


def add_nav_quote(html: str) -> str:
    if "btn-nav-quote" in html:
        return html
    return html.replace(
        "  <div class=\"nav-right\">\n    <button class=\"lbtn on\"",
        "  <div class=\"nav-right\">\n" + NAV_QUOTE + "    <button class=\"lbtn on\"",
    )


def patch_quote_triggers(html: str) -> str:
    html = html.replace(
        'href="index.html#iletisim" class="btn-white rv d2 contact-sheet-trigger"',
        'type="button" class="btn-white rv d2 quote-trigger"',
    )
    html = html.replace(
        'href="#iletisim" class="btn-white rv d2 contact-sheet-trigger"',
        'type="button" class="btn-white rv d2 quote-trigger"',
    )
    # service pages with data-service
    service_map = {
        "fire-detection.html": "fire",
        "security-systems.html": "security",
        "automation-systems.html": "automation",
        "audio-visual-systems.html": "audio",
        "data-communications.html": "data",
        "tv-video-systems.html": "tv",
    }
    for fname, svc in service_map.items():
        if fname in html or True:
            pass
    import re
    for fname, svc in service_map.items():
        html = re.sub(
            rf'(<button type="button" class="btn-white rv d2 quote-trigger">)(?=.*?{re.escape(fname)}|' + ")",
            rf'\1'.replace("quote-trigger", f'quote-trigger" data-service="{svc}"'),
            html,
            count=0,
        )
    # simpler: add data-service per file when processing each file
    return html


def main():
    for p in PROJECTS:
        out = ROOT / p["file"]
        out.write_text(render_page(p))
        print("wrote", out.name)

    ref_links = {k: v for k, v in REF_MAP}
    for path in ROOT.glob("*.html"):
        if path.name.startswith("project-"):
            continue
        text = path.read_text()
        text = add_nav_quote(text)
        if path.name in ("index.html", "references.html"):
            text = patch_ref_cards(text)
        # service-specific quote data
        svc = {
            "fire-detection.html": "fire",
            "security-systems.html": "security",
            "automation-systems.html": "automation",
            "audio-visual-systems.html": "audio",
            "data-communications.html": "data",
            "tv-video-systems.html": "tv",
        }.get(path.name)
        if svc:
            text = text.replace(
                'class="btn-white rv d2 quote-trigger"',
                f'class="btn-white rv d2 quote-trigger" data-service="{svc}"',
            )
        else:
            text = text.replace(
                'href="index.html#iletisim" class="btn-white rv d2 contact-sheet-trigger"',
                'type="button" class="btn-white rv d2 quote-trigger"',
            )
            text = text.replace(
                'href="index.html#iletisim" class="btn-white contact-sheet-trigger"',
                'type="button" class="btn-white quote-trigger"',
            )
        text = text.replace('site.css?v=18', 'site.css?v=19')
        text = text.replace('site.css?v=17', 'site.css?v=19')
        text = text.replace('site.js?v=17', 'site.js?v=19')
        text = text.replace('site.js?v=18', 'site.js?v=19')
        path.write_text(text)
        print("patched", path.name)


if __name__ == "__main__":
    main()
