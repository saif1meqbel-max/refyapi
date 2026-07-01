#!/usr/bin/env python3
"""Regenerate homepage services grid, preview panels, and products showcase."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SERVICES = [
  {
    "id": "fire", "href": "fire-detection.html", "num": "01", "quote": "fire",
    "title": ("Yangın Alarm Sistemleri", "Fire Alarm Systems", "Системы пожарной сигнализации"),
    "desc": ("Orta ve büyük ölçekli projeler için akıllı adresli yangın algılama ve alarm sistemleri.", "Smart addressable fire detection and alarm systems for large and medium-sized projects.", "Интеллектуальные адресные системы пожарной сигнализации для проектов среднего и крупного масштаба."),
    "lead": ("Adresli ve konvansiyonel yangın algılama sistemlerini projelendiriyor, kuruyor ve devreye alıyoruz — duman ve ısı detektörlerinden ihbar panellerine, sesli-ışıklı uyarıcılardan tahliye senaryolarına kadar.", "We design, install and commission addressable and conventional fire detection — from smoke and heat detectors to alarm panels, sirens, beacons and full evacuation scenarios.", "Проектируем, монтируем и вводим в эксплуатацию адресные и конвенциональные системы — от датчиков до панелей, сирен и сценариев эвакуации."),
    "points": [
      ("Adresli panel, dedektör ve manuel buton kurulumu", "Addressable panels, detectors and manual call points", "Адресные панели, извещатели и ручные извещатели"),
      ("Yönetmeliklere uygun sistem tasarımı ve test", "Regulation-compliant design, testing and documentation", "Проектирование и испытания по нормам"),
      ("Bina otomasyonu ve acil anons ile entegrasyon", "Integration with BMS and voice alarm systems", "Интеграция с BMS и голосовой сигнализацией"),
      ("Periyodik bakım ve 7/24 teknik destek", "Periodic maintenance and 24/7 technical support", "Периодическое обслуживание и поддержка 24/7"),
    ],
    "tags": ("Honeywell · Morley", "Hastane · AVM · Havalimanı", "Honeywell · Morley", "Hospitals · Malls · Airports", "Honeywell · Morley", "Больницы · ТРЦ · Аэропорты"),
  },
  {
    "id": "access", "href": "security-systems.html#kartli-gecis", "num": "02", "quote": "security",
    "title": ("Erişim Kontrol ve Personel Takip", "Access Control & Staff Tracking", "Контроль доступа и учёт персонала"),
    "desc": ("Kısıtlı alanlara kontrollü erişim ve personel giriş-çıkış takip sistemleri.", "Controlled permission to restricted areas and personnel entry-exit tracking systems.", "Контролируемый доступ в ограниченные зоны и учёт входа/выхода персонала."),
    "lead": ("Kartlı geçiş, biyometrik okuyucular, turnike ve bariyer sistemleri ile personel ve ziyaretçi hareketlerini kayıt altına alıyor; yetkilendirme ve raporlama sağlıyoruz.", "We deploy card readers, biometrics, turnstiles and barriers to control access, track personnel and visitors, and deliver authorisation with full audit reporting.", "Устанавливаем считыватели, биометрию, турникеты и шлагбаумы для контроля доступа, учёта персонала и полной отчётности."),
    "points": [
      ("Kart, parmak izi ve yüz tanıma okuyucular", "Card, fingerprint and facial recognition readers", "Считыватели карт, отпечатков и лица"),
      ("Turnike, bariyer ve kapı kontrol entegrasyonu", "Turnstile, barrier and door control integration", "Интеграция с турникетами, шлагбаумами и дверями"),
      ("Personel devam ve ziyaretçi yönetimi", "Staff attendance and visitor management", "Учёт рабамочего времени и управление посетителями"),
      ("Merkezi yazılım ile bölge bazlı yetkilendirme", "Zone-based authorisation via central software", "Зональная авторизация через центральное ПО"),
    ],
    "tags": ("Honeywell · SALTO", "Ofis · Fabrika · Kamu", "Honeywell · SALTO", "Offices · Factories · Public sector", "Honeywell · SALTO", "Офисы · Заводы · Госсектор"),
  },
  {
    "id": "data", "href": "data-communications.html", "num": "03", "quote": "data",
    "title": ("Data ve Altyapı Sistemleri", "Data & Infrastructure Systems", "Data и инфраструктура"),
    "desc": ("Zayıf akım sistemlerinin vazgeçilmez unsuru olan data ve altyapı hizmetlerimizi inceleyin.", "See our data & infrastructure services, which are indispensable elements of weak current systems.", "Data и инфраструктурные услуги — неотъемлемая часть слаботочных систем."),
    "lead": ("Yapısal kablolama, fiber optik, data kabinetleri ve aktif network ekipmanlarını tüm zayıf akım sistemlerinin omurgası olarak tasarlıyor ve kuruyoruz.", "We design and install structured cabling, fibre optics, data cabinets and active network equipment as the backbone for all low-current systems.", "Проектируем и монтируем СКС, оптоволокно, шкафы и активное сетевое оборудование как основу всех слаботочных систем."),
    "points": [
      ("Cat6/Cat6A ve fiber optik altyapı", "Cat6/Cat6A and fibre optic infrastructure", "Инфраструктура Cat6/Cat6A и оптоволокно"),
      ("Data kabineti, patch panel ve etiketleme", "Data cabinets, patch panels and labelling", "Шкафы, патч-панели и маркировка"),
      ("Switch, router ve kablosuz erişim noktaları", "Switches, routers and wireless access points", "Коммутаторы, маршрутизаторы и Wi‑Fi"),
      ("Sertifikalı test, ölçüm ve devreye alma", "Certified testing, measurement and commissioning", "Сертифицированные испытания и ввод в эксплуатацию"),
    ],
    "tags": ("Cisco · Commscope", "Ofis · Otel · Kampüs", "Cisco · Commscope", "Offices · Hotels · Campuses", "Cisco · Commscope", "Офисы · Отели · Кампусы"),
  },
  {
    "id": "hotel-door", "href": "automation-systems.html#otel-kapi", "num": "04", "quote": "integrated",
    "title": ("Otel Kapı Sistemleri", "Hotel Door Systems", "Дверные системы для отелей"),
    "desc": ("Otel yönetimine güvenli hizmet sunarak misafirlere konforlu konaklama sağlar.", "Comfortable accommodation for guests by providing safe service to hotel administration.", "Безопасный сервис для администрации отеля и комфортное проживание гостей."),
    "lead": ("RFID kartlı elektronik kilitler, mobil anahtar ve bulut tabanlı erişim yönetimi ile otel kapı sistemlerinde güvenlik ve operasyonel verimliliği bir araya getiriyoruz.", "We combine security and operational efficiency in hotel door systems with RFID electronic locks, mobile keys and cloud-based access management.", "Объединяем безопасность и операционную эффективность с RFID-замками, мобильными ключами и облачным управлением доступом."),
    "points": [
      ("RFID kartlı oda kilitleri ve mobil anahtar", "RFID room locks and mobile key solutions", "RFID-замки и мобильные ключи"),
      ("PMS ve otel yönetim yazılımı entegrasyonu", "PMS and hotel management software integration", "Интеграция с PMS и отельным ПО"),
      ("Kablo gerektirmeyen kurulum ve hızlı devreye alma", "Wireless installation and rapid commissioning", "Беспроводной монтаж и быстрый ввод"),
      ("Acil çıkış ve yangın standartlarına uyum", "Compliance with emergency exit and fire standards", "Соответствие нормам эвакуации и пожарной безопасности"),
    ],
    "tags": ("SALTO · Honeywell", "Otel · Resort", "SALTO · Honeywell", "Hotels · Resorts", "SALTO · Honeywell", "Отели · Курорты"),
  },
  {
    "id": "pa", "href": "audio-visual-systems.html#genel-anons", "num": "05", "quote": "integrated",
    "title": ("Genel Anons ve Sesli Alarm", "Public Announcement & Voice Alarm", "Оповещение и голосовая сигнализация"),
    "desc": ("Fon müziği, alarm ve tahliye faaliyetleri için entegre çözümler.", "Solutions for background music, alarm and evacuation activities.", "Решения для фоновой музыки, сигнализации и эвакуации."),
    "lead": ("Acil anons, sesli alarm ve fon müziği sistemlerini tek platformda birleştiriyor; tahliye senaryolarını yangın algılama ile entegre ediyoruz.", "We unify emergency PA, voice alarm and background music on a single platform, integrating evacuation scenarios with fire detection.", "Объединяем оповещение, голосовую сигнализацию и фоновую музыку на одной платформе с интеграцией пожарной сигнализации."),
    "points": [
      ("Acil anons ve sesli tahliye senaryoları", "Emergency PA and voice evacuation scenarios", "Экстренное оповещение и голосовая эвакуация"),
      ("Bölge bazlı fon müziği ve zonal kontrol", "Zone-based background music and zonal control", "Зональная фоновая музыка и управление"),
      ("Mikser, amfi ve hoparlör sistemleri", "Mixer, amplifier and speaker systems", "Микшеры, усилители и акустика"),
      ("EN 54 ve ilgili standartlara uygun tasarım", "Design compliant with EN 54 and relevant standards", "Проектирование по EN 54 и нормам"),
    ],
    "tags": ("Honeywell · Bosch", "AVM · Havalimanı · Stadyum", "Honeywell · Bosch", "Malls · Airports · Stadiums", "Honeywell · Bosch", "ТРЦ · Аэропорты · Стадионы"),
  },
  {
    "id": "mechanical", "href": "automation-systems.html#mekanik", "num": "06", "quote": "integrated",
    "title": ("Mekanik Otomasyon Sistemleri", "Mechanical Automation Systems", "Механическая автоматизация"),
    "desc": ("Yürüyen merdiven, asansör, aydınlatma ve iklimlendirme gibi hizmetleri tek noktadan yönetin.", "Manage services such as escalators, elevators, lighting and air conditioning from a single point.", "Управление эскалаторами, лифтами, освещением и кондиционированием из одной точки."),
    "lead": ("Honeywell BMS ile asansör, yürüyen merdiven, HVAC ve enerji sistemlerini tek kontrol noktasından izleyip yönetmenizi sağlıyoruz.", "With Honeywell BMS we enable monitoring and control of lifts, escalators, HVAC and energy systems from a single control point.", "С Honeywell BMS обеспечиваем мониторинг и управление лифтами, эскалаторами, HVAC и энергосистемами из одной точки."),
    "points": [
      ("BMS kontrolörleri ve merkezi izleme yazılımı", "BMS controllers and central monitoring software", "Контроллеры BMS и центральное ПО мониторинга"),
      ("HVAC, iklimlendirme ve enerji optimizasyonu", "HVAC, climate control and energy optimisation", "HVAC, климат-контроль и оптимизация энергии"),
      ("Asansör ve yürüyen merdiven arayüzleri", "Lift and escalator interfaces", "Интерфейсы лифтов и эскалаторов"),
      ("Alarm, trend ve raporlama yetenekleri", "Alarm, trending and reporting capabilities", "Тревоги, тренды и отчётность"),
    ],
    "tags": ("Honeywell · KNX", "Gökdelen · Hastane", "Honeywell · KNX", "Skyscrapers · Hospitals", "Honeywell · KNX", "Небоскрёбы · Больницы"),
  },
  {
    "id": "phone", "href": "data-communications.html#telefon-voip", "num": "07", "quote": "data",
    "title": ("Telefon Sistemleri", "Phone Systems", "Телефонные системы"),
    "desc": ("VoIP ile telekomünikasyon maliyetlerinizi %50 ile %70 arasında azaltabilirsiniz.", "Through VoIP, it is possible to reduce your telecommunication costs between 50% and 70%.", "VoIP позволяет снизить затраты на телекоммуникации на 50–70%."),
    "lead": ("IP tabanlı telefon santralleri, softphone ve unified communications çözümleri ile kurumsal iletişimi modernize ediyor, maliyetleri düşürüyoruz.", "We modernise corporate communications and reduce costs with IP PBX, softphones and unified communications solutions.", "Модернизируем корпоративную связь и снижаем затраты с IP-АТС, softphone и UC-решениями."),
    "points": [
      ("IP PBX ve bulut tabanlı santral çözümleri", "IP PBX and cloud-based exchange solutions", "IP-АТС и облачные АТС"),
      ("Dahili, trunk ve mobil entegrasyon", "Extension, trunk and mobile integration", "Интеграция внутренних, транковых и мобильных линий"),
      ("Sesli mesaj, IVR ve çağrı yönlendirme", "Voicemail, IVR and call routing", "Голосовая почта, IVR и маршрутизация"),
      ("Mevcut altyapı ile uyumlu migrasyon", "Migration compatible with existing infrastructure", "Миграция с совместимостью с существующей инфраструктурой"),
    ],
    "tags": ("Cisco · Yealink", "Ofis · Otel · Call Center", "Cisco · Yealink", "Offices · Hotels · Call centres", "Cisco · Yealink", "Офисы · Отели · Колл-центры"),
  },
  {
    "id": "intercom", "href": "tv-video-systems.html#intercom", "num": "08", "quote": "tv",
    "title": ("IP İntercom Sistemleri", "IP Intercom Systems", "IP-домофонные системы"),
    "desc": ("Akıllı dijital teknolojilerin kullanıldığı IoT tabanlı IP intercom altyapısı.", "An IoT-based system in which smart digital technologies are used for IP intercom infrastructure.", "IoT-инфраструктура IP-домофона с использованием цифровых технологий."),
    "lead": ("Video interkom panelleri, daire içi monitörler ve mobil uygulama entegrasyonu ile apartman, site ve kurumsal binalarda güvenli iletişim sağlıyoruz.", "We deliver secure communication in residential and corporate buildings with video intercom panels, indoor monitors and mobile app integration.", "Обеспечиваем безопасную связь в жилых и корпоративных зданиях с видеодомофонами, мониторами и мобильным приложением."),
    "points": [
      ("IP video kapı panelleri ve iç üniteler", "IP video door panels and indoor stations", "IP-видеопанели и внутренние блоки"),
      ("Akıllı telefon uygulaması ile uzaktan erişim", "Remote access via smartphone app", "Удалённый доступ через смартфон"),
      ("Çok daireli site ve rezidans çözümleri", "Multi-unit residential and site solutions", "Решения для многоквартирных домов и посёлков"),
      ("Erişim kontrol ve CCTV entegrasyonu", "Access control and CCTV integration", "Интеграция с контролем доступа и CCTV"),
    ],
    "tags": ("2N · Hikvision", "Site · Rezidans · Ofis", "2N · Hikvision", "Sites · Residences · Offices", "2N · Hikvision", "Посёлки · Резиденции · Офисы"),
  },
  {
    "id": "cctv", "href": "security-systems.html#cctv", "num": "09", "quote": "security",
    "title": ("Kapalı Devre Kamera (CCTV)", "CCTV Systems", "Системы видеонаблюдения"),
    "desc": ("Güvenlik gereksinimleri için son teknoloji kamera sistemleri.", "Cutting-edge technology camera systems for security requirements.", "Камерные системы последнего поколения для задач безопасности."),
    "lead": ("IP ve analog kamera sistemleri, NVR/DVR kayıt, video analitik ve merkezi izleme ile kapsamlı güvenlik görüntüleme altyapısı kuruyoruz.", "We build comprehensive security video infrastructure with IP and analogue cameras, NVR/DVR recording, video analytics and central monitoring.", "Создаём инфраструктуру видеонаблюдения с IP и аналоговыми камерами, NVR/DVR, аналитикой и центральным мониторингом."),
    "points": [
      ("IP, PTZ ve dome kamera çözümleri", "IP, PTZ and dome camera solutions", "IP, PTZ и купольные камеры"),
      ("NVR/DVR ve merkezi video yönetimi", "NVR/DVR and central video management", "NVR/DVR и централизованное управление видео"),
      ("Gece görüşü ve akıllı video analitik", "Night vision and intelligent video analytics", "Ночное видение и видеоаналитика"),
      ("Erişim kontrol ve alarm entegrasyonu", "Access control and alarm integration", "Интеграция с контролем доступа и сигнализацией"),
    ],
    "tags": ("Hikvision · Honeywell", "AVM · Banka · Endüstri", "Hikvision · Honeywell", "Malls · Banks · Industry", "Hikvision · Honeywell", "ТРЦ · Банки · Промышленность"),
  },
  {
    "id": "lighting", "href": "automation-systems.html#aydinlatma", "num": "10", "quote": "integrated",
    "title": ("Bina ve Aydınlatma Otomasyonu", "Building & Lighting Automation", "Автоматизация зданий и освещения"),
    "desc": ("Aydınlatma, HVAC ve enerji yönetimini tek BMS platformundan kontrol edin.", "Manage building services such as lighting, HVAC and energy from a single platform.", "Управление освещением, HVAC и энергией с единой платформы BMS."),
    "lead": ("KNX ve BMS tabanlı aydınlatma otomasyonu ile enerji tüketimini azaltıyor, konfor ve güvenliği artırıyoruz — panjur, iklimlendirme ve senaryo kontrolü dahil.", "KNX and BMS-based lighting automation reduces energy consumption while improving comfort and safety — including blinds, HVAC and scene control.", "Автоматизация освещения на KNX и BMS снижает энергопотребление и повышает комфорт — шторы, HVAC и сценарии."),
    "points": [
      ("KNX aydınlatma ve perde/panjur kontrolü", "KNX lighting and blind/curtain control", "KNX-освещение и управление шторами"),
      ("Varlık sensörleri ile akıllı aydınlatma", "Smart lighting with occupancy sensors", "Умное освещение с датчиками присутствия"),
      ("Enerji izleme ve raporlama", "Energy monitoring and reporting", "Мониторинг и отчётность по энергии"),
      ("Merkezi görselleştirme ve uzaktan erişim", "Central visualisation and remote access", "Центральная визуализация и удалённый доступ"),
    ],
    "tags": ("KNX · Honeywell · Interra", "Ofis · Otel · Konut", "KNX · Honeywell · Interra", "Offices · Hotels · Residential", "KNX · Honeywell · Interra", "Офисы · Отели · Жильё"),
  },
  {
    "id": "nurse", "href": "automation-systems.html#hemsire", "num": "11", "quote": "integrated",
    "title": ("Hemşire Çağrı ve Mavi Kod", "Nurse Call & Code Blue", "Вызов медсестры и Code Blue"),
    "desc": ("Hasta ile sağlık personeli arasında IP teknolojisiyle kritik iletişim.", "An important function in communication between the patient and healthcare staff with IP technology.", "IP-связь между пациентом и медицинским персоналом."),
    "lead": ("IP tabanlı hemşire çağrı sistemleri ile hasta odasından hemşire istasyonuna sesli ve görsel iletişim kuruyor; mavi kod ve acil müdahale süreçlerini hızlandırıyoruz.", "IP-based nurse call systems enable voice and visual communication from patient rooms to nursing stations, accelerating code blue and emergency response.", "IP-системы вызова медсестры обеспечивают голосовую и визуальную связь от палаты до поста, ускоряя реагирование на Code Blue."),
    "points": [
      ("Yatak başı, WC ve koridor çağrı üniteleri", "Bedside, bathroom and corridor call units", "Прикроватные, санузловые и коридорные блоки"),
      ("Sesli iletişim ve ön bilgi alımı", "Voice communication and pre-assessment", "Голосовая связь и предварительная информация"),
      ("Mavi kod ve acil müdahale butonları", "Code blue and emergency call buttons", "Кнопки Code Blue и экстренного вызова"),
      ("Personel performans kaydı ve raporlama", "Staff response logging and reporting", "Учёт времени реагирования и отчётность"),
    ],
    "tags": ("Honeywell · ALCAD · Ackermann", "Hastane · Klinik", "Honeywell · ALCAD · Ackermann", "Hospitals · Clinics", "Honeywell · ALCAD · Ackermann", "Больницы · Клиники"),
  },
  {
    "id": "iptv", "href": "tv-video-systems.html#smatv", "num": "12", "quote": "tv",
    "title": ("IPTV Sistemleri", "IPTV Systems", "IPTV-системы"),
    "desc": ("Özellikle otellerde tercih edilen IPTV çözümleri — 4 ve 5 yıldızlı şehir otellerinde yaygın.", "Especially preferred by hotels, IPTV systems are frequently used in 4 and 5 star city hotels.", "IPTV-решения, особенно востребованные в отелях 4 и 5 звёзд."),
    "lead": ("Otel ve konut projelerinde IPTV ve SMATV headend sistemleri ile uydu/kablolu yayın dağıtımı, oda içi interaktif servisler ve merkezi yönetim sunuyoruz.", "We deliver satellite/cable distribution, in-room interactive services and central management with IPTV and SMATV headend systems for hotels and residential projects.", "Поставляем IPTV и SMATV headend для отелей и жилых проектов — распределение ТВ, интерактивные сервисы и центральное управление."),
    "points": [
      ("IPTV headend ve oda içi set-top box", "IPTV headend and in-room set-top boxes", "IPTV headend и приставки в номерах"),
      ("SMATV uydu dağıtım altyapısı", "SMATV satellite distribution infrastructure", "Инфраструктура спутникового SMATV"),
      ("Otel bilgi kanalları ve interaktif menüler", "Hotel information channels and interactive menus", "Информационные каналы и интерактивные меню"),
      ("Merkezi yönetim ve içerik güncelleme", "Central management and content updates", "Центральное управление и обновление контента"),
    ],
    "tags": ("Honeywell · Triax", "Otel · Rezidans", "Honeywell · Triax", "Hotels · Residences", "Honeywell · Triax", "Отели · Резиденции"),
  },
]

def lang_span(tr, en, ru):
    return f'<span data-lang="tr">{tr}</span><span data-lang="en">{en}</span><span data-lang="ru">{ru}</span>'

def load_icons():
    text = (ROOT / 'index.html').read_text(encoding='utf-8')
    icons = {}
    for m in re.finditer(r'<a href="([^"]+)" class="sc-card[^"]*">\s*<span class="sc-n">(\d+)</span>\s*(<svg class="sc-icon"[^>]*>.*?</svg>)', text, re.DOTALL):
        icons[m.group(1)] = m.group(3)
    return icons

def build_services(icons):
    cards = []
    panels = []
    for i, s in enumerate(SERVICES):
        d = f"d{(i % 3) + 1}"
        svg = icons.get(s['href'], '')
        active = ' is-active' if i == 0 else ''
        cards.append(f'''      <button type="button" class="sc-card rv {d}{active}" data-service="{s['id']}" aria-pressed="{"true" if i == 0 else "false"}">
        <span class="sc-n">{s['num']}</span>
        {svg}
        <h3 class="sc-title">{lang_span(*s['title'])}</h3>
        <p class="sc-desc">{lang_span(*s['desc'])}</p>
        <span class="sc-more"><span data-lang="tr">Detaylar</span><span data-lang="en">Details</span><span data-lang="ru">Подробнее</span><svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
      </button>''')
        tags = s['tags']
        points = ''.join(f'          <li>{lang_span(*p)}</li>\n' for p in s['points'])
        panels.append(f'''      <article class="svc-preview-panel{active}" data-service="{s['id']}" id="svc-{s['id']}">
        <div class="svc-preview-grid">
          <div class="svc-preview-main">
            <span class="svc-preview-num">{s['num']}</span>
            <h3 class="svc-preview-title">{lang_span(*s['title'])}</h3>
            <p class="svc-preview-lead">{lang_span(*s['lead'])}</p>
            <ul class="svc-preview-list">
{points.rstrip()}
            </ul>
          </div>
          <aside class="svc-preview-side">
            <p class="svc-preview-meta-label"><span data-lang="tr">Markalar</span><span data-lang="en">Brands</span><span data-lang="ru">Бренды</span></p>
            <p class="svc-preview-brands">{lang_span(tags[0], tags[2], tags[4])}</p>
            <p class="svc-preview-meta-label"><span data-lang="tr">Uygulama Alanları</span><span data-lang="en">Applications</span><span data-lang="ru">Применение</span></p>
            <p class="svc-preview-apps">{lang_span(tags[1], tags[3], tags[5])}</p>
            <div class="svc-preview-actions">
              <a href="{s['href']}" class="btn btn-outline svc-preview-link"><span data-lang="tr">Tam sayfayı gör</span><span data-lang="en">View full page</span><span data-lang="ru">Полная страница</span></a>
              <button type="button" class="btn btn-primary quote-trigger" data-quote-service="{s['quote']}"><span data-lang="tr">Teklif Al</span><span data-lang="en">Get Quote</span><span data-lang="ru">Смета</span></button>
            </div>
          </aside>
        </div>
      </article>''')
    grid = '    <div class="sg sg-12">\n' + '\n'.join(cards) + '\n    </div>'
    preview = '''    <div class="svc-preview" id="svcPreview" aria-live="polite">
      <div class="svc-preview-panels">
''' + '\n'.join(panels) + '''
      </div>
    </div>'''
    return grid + '\n\n' + preview

PRODUCTS = '''    <div class="prod-showcase">
      <div class="prod-partner-bar rv">
        <div class="prod-partner-badge">
          <span class="prod-partner-icon">◆</span>
          <span data-lang="tr">Honeywell Platinum İş Ortağı</span>
          <span data-lang="en">Honeywell Platinum Partner</span>
          <span data-lang="ru">Партнёр Honeywell Platinum</span>
        </div>
        <p class="prod-partner-note">
          <span data-lang="tr">12 hizmet alanında tasarım, tedarik, kurulum ve bakım — tek muhatap, uçtan uca çözüm.</span>
          <span data-lang="en">Design, supply, installation and maintenance across 12 service areas — one partner, end-to-end delivery.</span>
          <span data-lang="ru">Проектирование, поставка, монтаж и обслуживание в 12 областях — один партнёр, полный цикл.</span>
        </p>
      </div>

      <div class="prod-cat-grid">
        <a href="integrated-building-systems.html" class="prod-cat-card prod-cat-card--featured rv d1">
          <div class="prod-cat-head">
            <span class="prod-cat-label">Honeywell</span>
            <h3 class="prod-cat-title"><span data-lang="tr">Entegre Bina Sistemleri</span><span data-lang="en">Integrated Building Systems</span><span data-lang="ru">Интегрированные системы зданий</span></h3>
            <p class="prod-cat-desc"><span data-lang="tr">Yangın algılama, BMS otomasyon ve ses-ışık sistemlerini tek portföyde birleştiren Honeywell çözümleri.</span><span data-lang="en">Honeywell solutions combining fire detection, BMS automation and audio-visual systems in one portfolio.</span><span data-lang="ru">Решения Honeywell: пожарная сигнализация, BMS и аудио/свет в одном портфеле.</span></p>
          </div>
          <div class="prod-pillars">
            <div class="prod-pillar"><strong><span data-lang="tr">Yangın</span><span data-lang="en">Fire</span><span data-lang="ru">Пожарная</span></strong><span><span data-lang="tr">Paneller, dedektörler, MCP</span><span data-lang="en">Panels, detectors, MCPs</span><span data-lang="ru">Панели, извещатели</span></span></div>
            <div class="prod-pillar"><strong><span data-lang="tr">Otomasyon</span><span data-lang="en">Automation</span><span data-lang="ru">Автоматизация</span></strong><span><span data-lang="tr">BMS, HVAC, aydınlatma</span><span data-lang="en">BMS, HVAC, lighting</span><span data-lang="ru">BMS, HVAC, освещение</span></span></div>
            <div class="prod-pillar"><strong><span data-lang="tr">Ses &amp; Işık</span><span data-lang="en">Audio &amp; Visual</span><span data-lang="ru">Аудио и свет</span></strong><span><span data-lang="tr">PA, konferans, LED</span><span data-lang="en">PA, conference, LED</span><span data-lang="ru">PA, конференции, LED</span></span></div>
          </div>
          <div class="prod-svc-chips">
            <span class="prod-svc-chip">01</span><span class="prod-svc-chip">05</span><span class="prod-svc-chip">06</span><span class="prod-svc-chip">10</span><span class="prod-svc-chip">11</span>
          </div>
          <span class="prod-cat-cta"><span data-lang="tr">Ürünleri incele</span><span data-lang="en">Explore products</span><span data-lang="ru">Смотреть продукцию</span> →</span>
        </a>

        <a href="security-systems.html" class="prod-cat-card rv d2">
          <div class="prod-cat-head">
            <span class="prod-cat-label"><span data-lang="tr">Güvenlik</span><span data-lang="en">Security</span><span data-lang="ru">Безопасность</span></span>
            <h3 class="prod-cat-title"><span data-lang="tr">Güvenlik Ekipmanları</span><span data-lang="en">Security Equipment</span><span data-lang="ru">Охранное оборудование</span></h3>
            <p class="prod-cat-desc"><span data-lang="tr">CCTV, erişim kontrol, turnike ve bariyer sistemleri — entegre güvenlik altyapısı.</span><span data-lang="en">CCTV, access control, turnstiles and barriers — integrated security infrastructure.</span><span data-lang="ru">CCTV, контроль доступа, турникеты и шлагбаумы — интегрированная безопасность.</span></p>
          </div>
          <ul class="prod-cat-list">
            <li><span data-lang="tr">IP ve analog kameralar, NVR/DVR</span><span data-lang="en">IP &amp; analogue cameras, NVR/DVR</span><span data-lang="ru">IP и аналоговые камеры, NVR/DVR</span></li>
            <li><span data-lang="tr">Kart ve biyometrik okuyucular</span><span data-lang="en">Card &amp; biometric readers</span><span data-lang="ru">Считыватели карт и биометрии</span></li>
            <li><span data-lang="tr">Turnike ve bariyer sistemleri</span><span data-lang="en">Turnstile &amp; barrier systems</span><span data-lang="ru">Турникеты и шлагбаумы</span></li>
          </ul>
          <div class="prod-svc-chips"><span class="prod-svc-chip">02</span><span class="prod-svc-chip">09</span></div>
          <span class="prod-cat-cta"><span data-lang="tr">Ürünleri incele</span><span data-lang="en">Explore products</span><span data-lang="ru">Смотреть продукцию</span> →</span>
        </a>

        <a href="data-communications.html" class="prod-cat-card rv d3">
          <div class="prod-cat-head">
            <span class="prod-cat-label"><span data-lang="tr">Data &amp; İletişim</span><span data-lang="en">Data &amp; Comms</span><span data-lang="ru">Связь и данные</span></span>
            <h3 class="prod-cat-title"><span data-lang="tr">Ağ ve İletişim</span><span data-lang="en">Network &amp; Communications</span><span data-lang="ru">Сеть и связь</span></h3>
            <p class="prod-cat-desc"><span data-lang="tr">Yapısal kablolama, fiber, aktif network ve VoIP telefon altyapısı.</span><span data-lang="en">Structured cabling, fibre, active networking and VoIP telephony infrastructure.</span><span data-lang="ru">СКС, оптоволокно, активное оборудование и VoIP-телефония.</span></p>
          </div>
          <ul class="prod-cat-list">
            <li><span data-lang="tr">Cat6/Cat6A, fiber optik altyapı</span><span data-lang="en">Cat6/Cat6A, fibre infrastructure</span><span data-lang="ru">Cat6/Cat6A, оптоволокно</span></li>
            <li><span data-lang="tr">Switch, router, kablosuz AP</span><span data-lang="en">Switches, routers, wireless APs</span><span data-lang="ru">Коммутаторы, маршрутизаторы, Wi‑Fi</span></li>
            <li><span data-lang="tr">IP PBX ve VoIP telefon sistemleri</span><span data-lang="en">IP PBX and VoIP phone systems</span><span data-lang="ru">IP-АТС и VoIP-телефония</span></li>
          </ul>
          <div class="prod-svc-chips"><span class="prod-svc-chip">03</span><span class="prod-svc-chip">07</span></div>
          <span class="prod-cat-cta"><span data-lang="tr">Ürünleri incele</span><span data-lang="en">Explore products</span><span data-lang="ru">Смотреть продукцию</span> →</span>
        </a>

        <a href="tv-video-systems.html" class="prod-cat-card rv d1">
          <div class="prod-cat-head">
            <span class="prod-cat-label"><span data-lang="tr">TV &amp; Görüntü</span><span data-lang="en">TV &amp; Video</span><span data-lang="ru">ТВ и видео</span></span>
            <h3 class="prod-cat-title"><span data-lang="tr">Yayın ve Görüntü</span><span data-lang="en">Broadcast &amp; Video</span><span data-lang="ru">Вещание и видео</span></h3>
            <p class="prod-cat-desc"><span data-lang="tr">IPTV, SMATV headend, IP interkom ve otel TV çözümleri.</span><span data-lang="en">IPTV, SMATV headend, IP intercom and hotel TV solutions.</span><span data-lang="ru">IPTV, SMATV headend, IP-домофон и отельное ТВ.</span></p>
          </div>
          <ul class="prod-cat-list">
            <li><span data-lang="tr">IPTV headend ve oda içi servisler</span><span data-lang="en">IPTV headend and in-room services</span><span data-lang="ru">IPTV headend и сервисы в номерах</span></li>
            <li><span data-lang="tr">SMATV uydu dağıtım sistemleri</span><span data-lang="en">SMATV satellite distribution</span><span data-lang="ru">Спутниковое SMATV</span></li>
            <li><span data-lang="tr">IP video interkom panelleri</span><span data-lang="en">IP video intercom panels</span><span data-lang="ru">IP-видеодомофоны</span></li>
          </ul>
          <div class="prod-svc-chips"><span class="prod-svc-chip">08</span><span class="prod-svc-chip">12</span></div>
          <span class="prod-cat-cta"><span data-lang="tr">Ürünleri incele</span><span data-lang="en">Explore products</span><span data-lang="ru">Смотреть продукцию</span> →</span>
        </a>
      </div>

      <div class="prod-brands-strip rv d2">
        <span class="prod-brands-label"><span data-lang="tr">Tedarik ettiğimiz markalar</span><span data-lang="en">Brands we supply</span><span data-lang="ru">Поставляемые бренды</span></span>
        <div class="prod-brands-list">
          <span>Honeywell</span><span>Morley</span><span>SALTO</span><span>Hikvision</span><span>Cisco</span><span>KNX</span><span>2N</span><span>Bosch</span>
        </div>
      </div>

      <div class="prod-map rv d3">
        <p class="prod-map-label"><span data-lang="tr">Hizmet numaraları ürün kategorileriyle eşleşir — detay için hizmet kartına tıklayın.</span><span data-lang="en">Service numbers map to product categories — click a service card above for details.</span><span data-lang="ru">Номера услуг соответствуют категориям продукции — нажмите на карточку услуги выше.</span></p>
      </div>
    </div>'''

def main():
    icons = load_icons()
    if len(icons) != 12:
        raise SystemExit(f'Expected 12 icons, got {len(icons)}')
    text = (ROOT / 'index.html').read_text(encoding='utf-8')
    # services grid + preview
    start = text.index('    <div class="sg sg-12">')
    end = text.index('<!-- ════════════════════════════════════════ OUR PRODUCTS -->')
    text = text[:start] + build_services(icons) + '\n  </div>\n</section>\n\n' + text[end:]
    # products inner content
    pstart = text.index('    <div class="prod-grid prod-grid-4">')
    pend = text.index('    </div>\n  </div>\n</section>\n\n<!-- ════════════════════════════════════════ REFERENCES -->')
    text = text[:pstart] + PRODUCTS + text[pend:]
    text = text.replace('assets/site.css?v=37', 'assets/site.css?v=38')
    text = text.replace('assets/site.js?v=34', 'assets/site.js?v=38')
    (ROOT / 'index.html').write_text(text, encoding='utf-8')
    print('index.html updated')

if __name__ == '__main__':
    main()