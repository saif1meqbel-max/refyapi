#!/usr/bin/env python3
"""Patch footer services + company columns across HTML pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_SERVICES = """    <div>
      <p class="ft-col-head"><span data-lang="tr">Hizmetler</span><span data-lang="en">Services</span><span data-lang="ru">Услуги</span></p>
      <ul class="ft-links">
        <li><a href="integrated-building-systems.html"><span data-lang="tr">Entegre Bina Sistemleri</span><span data-lang="en">Integrated Building Systems</span><span data-lang="ru">Интегрированные системы</span></a></li>
        <li><a href="security-systems.html"><span data-lang="tr">Güvenlik Sistemleri</span><span data-lang="en">Security Systems</span><span data-lang="ru">Системы безопасности</span></a></li>
        <li><a href="data-communications.html"><span data-lang="tr">Data ve İletişim</span><span data-lang="en">Data &amp; Comms</span><span data-lang="ru">Связь и данные</span></a></li>
        <li><a href="tv-video-systems.html"><span data-lang="tr">TV ve Görüntü</span><span data-lang="en">TV &amp; Video</span><span data-lang="ru">ТВ и видео</span></a></li>
      </ul>
    </div>"""

SERVICE_LINKS_INDEX = [
    ("#svc-fire", "Yangın Alarm Sistemleri", "Fire Alarm Systems", "Пожарная сигнализация"),
    ("#svc-access", "Erişim Kontrol", "Access Control", "Контроль доступа"),
    ("#svc-data", "Data ve Altyapı", "Data & Infrastructure", "Data и инфраструктура"),
    ("#svc-hotel-door", "Otel Kapı Sistemleri", "Hotel Door Systems", "Дверные системы для отелей"),
    ("#svc-pa", "Genel Anons ve Sesli Alarm", "Public Announcement", "Оповещение"),
    ("#svc-mechanical", "Mekanik Otomasyon", "Mechanical Automation", "Механическая автоматизация"),
    ("#svc-phone", "Telefon Sistemleri", "Phone Systems", "Телефонные системы"),
    ("#svc-intercom", "IP İntercom", "IP Intercom", "IP-домофон"),
    ("#svc-cctv", "CCTV", "CCTV", "Видеонаблюдение"),
    ("#svc-lighting", "Bina ve Aydınlatma Otomasyonu", "Building & Lighting Automation", "Автоматизация зданий"),
    ("#svc-nurse", "Hemşire Çağrı ve Mavi Kod", "Nurse Call & Code Blue", "Вызов медсестры"),
    ("#svc-iptv", "IPTV Sistemleri", "IPTV Systems", "IPTV-системы"),
]

SERVICE_LINKS_PAGES = [
    ("fire-detection.html", "Yangın Alarm Sistemleri", "Fire Alarm Systems", "Пожарная сигнализация"),
    ("security-systems.html#kartli-gecis", "Erişim Kontrol", "Access Control", "Контроль доступа"),
    ("data-communications.html", "Data ve Altyapı", "Data & Infrastructure", "Data и инфраструктура"),
    ("automation-systems.html#otel-kapi", "Otel Kapı Sistemleri", "Hotel Door Systems", "Дверные системы для отелей"),
    ("audio-visual-systems.html#genel-anons", "Genel Anons ve Sesli Alarm", "Public Announcement", "Оповещение"),
    ("automation-systems.html#mekanik", "Mekanik Otomasyon", "Mechanical Automation", "Механическая автоматизация"),
    ("data-communications.html#telefon-voip", "Telefon Sistemleri", "Phone Systems", "Телефонные системы"),
    ("tv-video-systems.html#intercom", "IP İntercom", "IP Intercom", "IP-домофон"),
    ("security-systems.html#cctv", "CCTV", "CCTV", "Видеонаблюдение"),
    ("automation-systems.html#aydinlatma", "Bina ve Aydınlatma Otomasyonu", "Building & Lighting Automation", "Автоматизация зданий"),
    ("automation-systems.html#hemsire", "Hemşire Çağrı ve Mavi Kod", "Nurse Call & Code Blue", "Вызов медсестры"),
    ("tv-video-systems.html#smatv", "IPTV Sistemleri", "IPTV Systems", "IPTV-системы"),
]

PRODUCT_LINKS = [
    ("integrated-building-systems.html", "Entegre Bina Sistemleri", "Integrated Building Systems", "Интегрированные системы"),
    ("security-systems.html", "Güvenlik Sistemleri", "Security Systems", "Системы безопасности"),
    ("data-communications.html", "Data ve İletişim", "Data &amp; Comms", "Связь и данные"),
    ("tv-video-systems.html", "TV ve Görüntü", "TV &amp; Video", "ТВ и видео"),
]


def li(href: str, tr: str, en: str, ru: str) -> str:
    return (
        f'        <li><a href="{href}">'
        f'<span data-lang="tr">{tr}</span>'
        f'<span data-lang="en">{en}</span>'
        f'<span data-lang="ru">{ru}</span></a></li>'
    )


def services_block(links) -> str:
    items = "\n".join(li(h, tr, en, ru) for h, tr, en, ru in links)
    products = "\n".join(li(h, tr, en, ru) for h, tr, en, ru in PRODUCT_LINKS)
    return f"""    <div class="ft-col-services">
      <p class="ft-col-head"><span data-lang="tr">Hizmetler</span><span data-lang="en">Services</span><span data-lang="ru">Услуги</span></p>
      <ul class="ft-links ft-links--2col">
{items}
      </ul>
      <p class="ft-col-head ft-col-head--sub"><span data-lang="tr">Ürün Kategorileri</span><span data-lang="en">Product Categories</span><span data-lang="ru">Категории продуктов</span></p>
      <ul class="ft-links">
{products}
      </ul>
    </div>"""


OFFICES_BLOCK = """
        <li><a href="istanbul.html"><span data-lang="tr">İstanbul Ofisi</span><span data-lang="en">Istanbul Office</span><span data-lang="ru">Офис в Стамбуле</span></a></li>
        <li><a href="london.html"><span data-lang="tr">Londra Ofisi</span><span data-lang="en">London Office</span><span data-lang="ru">Офис в Лондоне</span></a></li>
        <li><a href="middle-east-asia.html"><span data-lang="tr">Orta Doğu ve Asya Ofisi</span><span data-lang="en">Middle East &amp; Asia Office</span><span data-lang="ru">Офис на Ближнем Востоке и в Азии</span></a></li>"""

def patch_company(text: str, is_index: bool) -> str:
    if 'ft-col-head--sub' in text and 'Hizmetlerimiz' in text.split('Şirket</span>')[1].split('</footer>')[0] if 'Şirket</span>' in text else '':
        return text

    about_fixed = (
        '        <li><a href="index.html#hakkimizda"><span data-lang="tr">Hakkımızda</span>'
        '<span data-lang="en">About Us</span><span data-lang="ru">О нас</span></a></li>\n'
        '        <li><a href="index.html#hizmetler"><span data-lang="tr">Hizmetlerimiz</span>'
        '<span data-lang="en">Our Services</span><span data-lang="ru">Услуги</span></a></li>'
    )
    about_index = (
        '        <li><a href="#hakkimizda"><span data-lang="tr">Hakkımızda</span>'
        '<span data-lang="en">About Us</span><span data-lang="ru">О нас</span></a></li>\n'
        '        <li><a href="#hizmetler"><span data-lang="tr">Hizmetlerimiz</span>'
        '<span data-lang="en">Our Services</span><span data-lang="ru">Услуги</span></a></li>'
    )

    if is_index:
        if 'href="#hizmetler"' not in text.split('Şirket</span>')[1].split('</ul>')[0]:
            text = text.replace(
                '        <li><a href="#hakkimizda"><span data-lang="tr">Hakkımızda</span>'
                '<span data-lang="en">About Us</span><span data-lang="ru">О нас</span></a></li>\n'
                '        <li><a href="#urunlerimiz">',
                about_index + '\n        <li><a href="#urunlerimiz">',
                1,
            )
    else:
        for bad in ('href="#hakkimizda"', 'href="#urunlerimiz"', 'href="#iletisim"'):
            text = text.replace(bad, bad.replace('#', 'index.html#'))

        company = text.split('Şirket</span>')[1].split('</ul>')[0] if 'Şirket</span>' in text else ''
        if 'index.html#hizmetler' not in company and 'index.html#hakkimizda' in company:
            text = text.replace(
                '        <li><a href="index.html#hakkimizda"><span data-lang="tr">Hakkımızda</span>'
                '<span data-lang="en">About Us</span><span data-lang="ru">О нас</span></a></li>',
                about_fixed,
                1,
            )

    footer = text.split('<footer>')[1].split('</footer>')[0] if '<footer>' in text else ''
    company = footer.split('Şirket</span>')[1].split('</ul>')[0] if 'Şirket</span>' in footer else ''
    if company and 'istanbul.html' not in company:
        text = text.replace(
            '        <li><a href="documents.html"><span data-lang="tr">Teknik Kitaplık</span>'
            '<span data-lang="en">Tech Library</span><span data-lang="ru">Библиотека</span></a></li>\n'
            '        <li><a href="privacy-policy.html">',
            '        <li><a href="documents.html"><span data-lang="tr">Teknik Kitaplık</span>'
            '<span data-lang="en">Tech Library</span><span data-lang="ru">Библиотека</span></a></li>'
            + OFFICES_BLOCK + '\n        <li><a href="privacy-policy.html">',
            1,
        )

    return text


def main() -> None:
    office_pages = {'istanbul.html', 'london.html', 'middle-east-asia.html'}

    for path in sorted(ROOT.glob('*.html')):
        text = path.read_text(encoding='utf-8')
        if OLD_SERVICES not in text:
            print(f'skip (no old services): {path.name}')
            continue

        is_index = path.name == 'index.html'
        is_office = path.name in office_pages

        text = text.replace(
            OLD_SERVICES,
            services_block(SERVICE_LINKS_INDEX if is_index else SERVICE_LINKS_PAGES),
        )

        if not is_office:
            text = patch_company(text, is_index)

        path.write_text(text, encoding='utf-8')
        print(f'patched: {path.name}')

    print('done')


if __name__ == '__main__':
    main()
