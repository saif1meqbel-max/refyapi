/* Renders a project case-study from window.REF_PROJECTS using ?id=refNN.
   Uses only real catalogue data; sector copy describes REF YAPI's capability
   for that building type (not fabricated project-specific claims). */
(function () {
  var P = window.REF_PROJECTS || [];
  var params = new URLSearchParams(location.search);
  var id = params.get('id');
  var proj = P.find(function (p) { return p.id === id; });
  if (!proj) { location.replace('references.html'); return; }

  // country display names
  var COUNTRY = {
    turkey: { tr: 'Türkiye', en: 'Turkey', ru: 'Турция' },
    azerbaijan: { tr: 'Azerbaycan', en: 'Azerbaijan', ru: 'Азербайджан' },
    belarus: { tr: 'Belarus', en: 'Belarus', ru: 'Беларусь' },
    curacao: { tr: 'Curaçao', en: 'Curaçao', ru: 'Кюрасао' },
    'equatorial-guinea': { tr: 'Ekvator Ginesi', en: 'Equatorial Guinea', ru: 'Экваториальная Гвинея' },
    kyrgyzstan: { tr: 'Kırgızistan', en: 'Kyrgyzstan', ru: 'Кыргызстан' },
    nigeria: { tr: 'Nijerya', en: 'Nigeria', ru: 'Нигерия' },
    russia: { tr: 'Rusya', en: 'Russia', ru: 'Россия' },
    tajikistan: { tr: 'Tacikistan', en: 'Tajikistan', ru: 'Таджикистан' },
    turkmenistan: { tr: 'Türkmenistan', en: 'Turkmenistan', ru: 'Туркменистан' },
    uzbekistan: { tr: 'Özbekistan', en: 'Uzbekistan', ru: 'Узбекистан' }
  };

  // per-sector editorial statement + disciplines (capability, trilingual)
  var SECTORS = {
    Hospitality: {
      s: { tr: 'Otel ve tatil yapılarında misafir deneyimini destekleyen bir inşaat disiplini.', en: 'Construction that supports the guest experience across hotels and resorts.', ru: 'Строительство, поддерживающее гостевой опыт в отелях и курортах.' },
      d: [['Kaba ve ince yapı', 'Structural & finishing works', 'Каркас и отделка'], ['Cephe ve çatı sistemleri', 'Facade & roofing systems', 'Фасад и кровля'], ['Mekanik ve elektrik tesisat', 'MEP installation', 'Инженерные системы'], ['İç mekan ve peyzaj uygulaması', 'Interior fit-out & landscaping', 'Интерьер и ландшафт']]
    },
    Healthcare: {
      s: { tr: 'Sağlık yapılarında hijyen, süreklilik ve teknik altyapı odaklı uygulama.', en: 'Delivery focused on hygiene, continuity and technical infrastructure for healthcare buildings.', ru: 'Строительство медицинских объектов с упором на гигиену и инженерию.' },
      d: [['Kaba ve ince yapı', 'Structural & finishing works', 'Каркас и отделка'], ['Temiz oda ve hijyenik alanlar', 'Clean rooms & hygienic areas', 'Чистые помещения'], ['Medikal gaz ve HVAC sistemleri', 'Medical gas & HVAC systems', 'Медицинские газы и HVAC'], ['Elektrik ve zayıf akım altyapısı', 'Power & low-current infrastructure', 'Электрика и слаботочные сети']]
    },
    Education: {
      s: { tr: 'Eğitim yapılarında ölçek, güvenlik ve uzun ömürlü kullanım için inşaat.', en: 'Construction built for scale, safety and long service life in education facilities.', ru: 'Строительство образовательных объектов с акцентом на масштаб и безопасность.' },
      d: [['Kaba ve ince yapı', 'Structural & finishing works', 'Каркас и отделка'], ['Derslik ve laboratuvar uygulaması', 'Classroom & laboratory fit-out', 'Аудитории и лаборатории'], ['Mekanik ve elektrik tesisat', 'MEP installation', 'Инженерные системы'], ['Dış alan ve peyzaj', 'External works & landscaping', 'Благоустройство территории']]
    },
    Industrial: {
      s: { tr: 'Endüstriyel tesislerde üretim sürekliliğini önceleyen teknik inşaat.', en: 'Technical construction that puts production continuity first in industrial facilities.', ru: 'Техническое строительство промышленных объектов.' },
      d: [['Endüstriyel kaba yapı', 'Industrial structural works', 'Промышленный каркас'], ['Ağır ekipman altyapısı', 'Heavy-equipment foundations', 'Основания под оборудование'], ['Mekanik, elektrik ve enerji', 'Mechanical, electrical & power', 'Механика, электрика, энергия'], ['Yangın ve güvenlik sistemleri', 'Fire & safety systems', 'Пожарные и охранные системы']]
    },
    Commercial: {
      s: { tr: 'Ofis, plaza ve banka yapılarında işlev ve prestiji birleştiren inşaat.', en: 'Construction that combines function and prestige across offices, plazas and banks.', ru: 'Строительство офисов, бизнес-центров и банков.' },
      d: [['Kaba ve ince yapı', 'Structural & finishing works', 'Каркас и отделка'], ['Cephe ve çekirdek', 'Facade & building core', 'Фасад и ядро здания'], ['Mekanik ve elektrik tesisat', 'MEP installation', 'Инженерные системы'], ['Ortak alan ve iç mekan', 'Common areas & interiors', 'Общие зоны и интерьеры']]
    },
    Public: {
      s: { tr: 'Kamu ve idari yapılarda standartlara tam uyumlu, güvenilir uygulama.', en: 'Reliable delivery in full compliance with standards for public and government buildings.', ru: 'Надёжное строительство государственных объектов по стандартам.' },
      d: [['Kaba ve ince yapı', 'Structural & finishing works', 'Каркас и отделка'], ['Cephe ve dış uygulama', 'Facade & external works', 'Фасад и внешние работы'], ['Mekanik ve elektrik tesisat', 'MEP installation', 'Инженерные системы'], ['Güvenlik ve altyapı sistemleri', 'Security & infrastructure systems', 'Безопасность и инфраструктура']]
    },
    Residential: {
      s: { tr: 'Konut projelerinde yaşanabilirlik ve zamanında teslim odaklı inşaat.', en: 'Construction focused on liveability and on-time handover in residential projects.', ru: 'Жилищное строительство с акцентом на комфорт и сроки.' },
      d: [['Kaba ve ince yapı', 'Structural & finishing works', 'Каркас и отделка'], ['Cephe ve çatı', 'Facade & roofing', 'Фасад и кровля'], ['Mekanik ve elektrik tesisat', 'MEP installation', 'Инженерные системы'], ['Ortak alan ve peyzaj', 'Common areas & landscaping', 'Общие зоны и ландшафт']]
    },
    Infrastructure: {
      s: { tr: 'Havalimanı ve altyapı projelerinde ölçek isteyen teknik inşaat.', en: 'Technical construction at scale for airports and infrastructure projects.', ru: 'Масштабное строительство аэропортов и инфраструктуры.' },
      d: [['Büyük ölçekli kaba yapı', 'Large-scale structural works', 'Крупный каркас'], ['Özel mühendislik çözümleri', 'Specialist engineering solutions', 'Инженерные решения'], ['Mekanik, elektrik ve enerji', 'Mechanical, electrical & power', 'Механика, электрика, энергия'], ['Sistem entegrasyonu ve test', 'Systems integration & testing', 'Интеграция и испытания']]
    },
    Construction: {
      s: { tr: 'Anahtar teslim inşaatta uçtan uca uygulama ve saha yönetimi.', en: 'End-to-end delivery and site management in turnkey construction.', ru: 'Строительство «под ключ» с полным управлением площадкой.' },
      d: [['Kaba ve ince yapı', 'Structural & finishing works', 'Каркас и отделка'], ['Cephe ve dış uygulama', 'Facade & external works', 'Фасад и внешние работы'], ['Mekanik ve elektrik tesisat', 'MEP installation', 'Инженерные системы'], ['Saha yönetimi ve teslim', 'Site management & handover', 'Управление и сдача']]
    }
  };

  function span(o) {
    return '<span data-lang="tr">' + (o.tr || '') + '</span>' +
           '<span data-lang="en">' + (o.en || o.tr || '') + '</span>' +
           '<span data-lang="ru">' + (o.ru || o.en || o.tr || '') + '</span>';
  }
  function set(id, html) { var el = document.getElementById(id); if (el) el.innerHTML = html; }

  var sec = SECTORS[proj.sector.en] || SECTORS.Construction;
  var ctry = COUNTRY[proj.country] || { tr: proj.country, en: proj.country, ru: proj.country };

  // Hero
  var img = document.getElementById('csImg');
  img.src = proj.img; img.alt = proj.alt || (proj.title.en || proj.title.tr);
  set('csCrumb', span(proj.title));
  set('csSector', span(proj.sector));
  set('csTitle', span(proj.title));
  set('csPlace', span(proj.loc));

  // Overview
  set('csOverviewH', span(sec.s));
  set('csOverviewP', span({
    tr: proj.title.tr + ', ' + (proj.loc.tr || '') + ' konumunda yer alan bir ' + proj.sector.tr.toLowerCase() + ' projesidir. REF YAPI tarafından ' + proj.year + ' yılında tamamlanmıştır.',
    en: (proj.title.en || proj.title.tr) + ' is a ' + proj.sector.en.toLowerCase() + ' project in ' + (proj.loc.en || proj.loc.tr || '') + ', delivered by REF YAPI and completed in ' + proj.year + '.',
    ru: (proj.title.ru || proj.title.en || proj.title.tr) + ' — ' + proj.sector.ru.toLowerCase() + ' проект в ' + (proj.loc.ru || proj.loc.en || '') + ', реализован REF YAPI в ' + proj.year + ' году.'
  }));

  // Disciplines
  set('csDisc', sec.d.map(function (d) {
    return '<li>' + span({ tr: d[0], en: d[1], ru: d[2] }) + '</li>';
  }).join(''));

  // Facts
  var facts = [
    [{ tr: 'Konum', en: 'Location', ru: 'Локация' }, proj.loc],
    [{ tr: 'Sektör', en: 'Sector', ru: 'Сектор' }, proj.sector],
    [{ tr: 'Yıl', en: 'Year', ru: 'Год' }, { tr: proj.year, en: proj.year, ru: proj.year }],
    [{ tr: 'Bölge', en: 'Region', ru: 'Регион' }, ctry],
    [{ tr: 'Durum', en: 'Status', ru: 'Статус' }, { tr: 'Tamamlandı', en: 'Completed', ru: 'Завершён' }]
  ];
  set('csFacts', facts.map(function (f) {
    return '<div><dt>' + span(f[0]) + '</dt><dd>' + span(f[1]) + '</dd></div>';
  }).join(''));

  // Google Maps link for the project location (city-level search)
  var mapEl = document.getElementById('csMap');
  if (mapEl) {
    var locStr = proj.loc.en || proj.loc.tr || proj.loc.ru || '';
    if (locStr) {
      var q = encodeURIComponent(((proj.title.en || proj.title.tr) + ' ' + locStr).trim());
      mapEl.setAttribute('href', 'https://www.google.com/maps/search/?api=1&query=' + q);
      mapEl.hidden = false;
    }
  }

  // More projects — same sector first, then fill by recency
  var others = P.filter(function (p) { return p.id !== proj.id; });
  var same = others.filter(function (p) { return p.sector.en === proj.sector.en; });
  var rest = others.filter(function (p) { return p.sector.en !== proj.sector.en; })
                   .sort(function (a, b) { return (b.year || '').localeCompare(a.year || ''); });
  var more = same.concat(rest).slice(0, 3);
  set('csMore', more.map(function (p) {
    return '<a class="cs-card" href="project.html?id=' + p.id + '">' +
      '<span class="cs-card-media"><img src="' + p.img + '" alt="' + (p.alt || '') + '" loading="lazy" /></span>' +
      '<span class="cs-card-cap"><span class="cs-card-year">' + p.year + '</span>' +
      '<span class="cs-card-name">' + span(p.title) + '</span>' +
      '<span class="cs-card-loc">' + span(p.loc) + '</span></span></a>';
  }).join(''));

  // SEO: title + meta description (use current active language)
  var lang = document.documentElement.classList.contains('lang-en') ? 'en'
           : document.documentElement.classList.contains('lang-ru') ? 'ru' : 'tr';
  var t = proj.title[lang] || proj.title.tr;
  document.title = t + ' — REF YAPI';
  var md = document.getElementById('metaDesc');
  if (md) {
    var loc = proj.loc[lang] || proj.loc.tr || '';
    md.setAttribute('content', t + ' — ' + (proj.sector[lang] || proj.sector.tr) + ', ' + loc + ' (' + proj.year + '). REF YAPI.');
  }
})();
