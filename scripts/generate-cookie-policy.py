#!/usr/bin/env python3
"""Generate cookie-policy.html."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def L(tr, en, ru, block=False):
    tag = "div" if block else "span"
    return f'<{tag} data-lang="tr">{tr}</{tag}><{tag} data-lang="en">{en}</{tag}><{tag} data-lang="ru">{ru}</{tag}>'

BROWSER_LINKS = """
<ul class="legal-list legal-links">
<li><a href="https://support.google.com/chrome/answer/95647" target="_blank" rel="noopener noreferrer">Google Chrome</a></li>
<li><a href="https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop" target="_blank" rel="noopener noreferrer">Mozilla Firefox</a></li>
<li><a href="https://support.microsoft.com/help/17442/windows-internet-explorer-delete-manage-cookies" target="_blank" rel="noopener noreferrer">Internet Explorer</a></li>
<li><a href="https://support.apple.com/guide/safari/manage-cookies-sfri11471/mac" target="_blank" rel="noopener noreferrer">Safari</a></li>
<li><a href="https://help.opera.com/en/latest/web-preferences/#cookies" target="_blank" rel="noopener noreferrer">Opera</a></li>
</ul>"""

SECTIONS = [
  ("intro", "1. Giriş", (
    """İnternet sitemizin (www.fnvelektronik.com) düzgün çalışmasını sağlamak, ziyaretçi ve üyelerimize ("kullanıcı(lar)" veya "siz") en alakalı hizmetleri sunmak amacıyla birtakım çerezler kullanmaktayız.

<p>İşbu Çerez Politikası, size çerezler ve çerezlerin nasıl kontrol edileceği hakkında bilgi vermek amacıyla hazırlanmıştır.</p>""",
    """We use certain cookies to ensure our website (www.fnvelektronik.com) works properly and to offer visitors and members ("user(s)" or "you") the most relevant services.

<p>This Cookie Policy is prepared to inform you about cookies and how to control them.</p>""",
    """Мы используем файлы cookie для корректной работы нашего сайта (www.fnvelektronik.com) и предоставления посетителям и пользователям («пользователь(и)» или «вы») наиболее релевантных услуг.

<p>Настоящая Политика cookie подготовлена для информирования о cookie и способах их управления.</p>""",
  )),
  ("what", "2. Çerez nedir?", (
    """Çerezler, internet sitemizi ziyaret ettiğinizde bilgisayarınıza ya da mobil cihazınıza kaydedilen küçük metin dosyalarıdır. Bu metin dosyaları ile beraber web işaretçileri, pikseller veya etiketler gibi diğer takipçiler de işbu Çerez Politikası kapsamında çerez olarak kabul edilecektir.""",
    """Cookies are small text files saved to your computer or mobile device when you visit our website. Together with these text files, other trackers such as web beacons, pixels or tags are also regarded as cookies under this Cookie Policy.""",
    """Cookie — это небольшие текстовые файлы, сохраняемые на вашем компьютере или мобильном устройстве при посещении сайта. Вместе с ними веб-маяки, пиксели и теги также считаются cookie в рамках настоящей Политики.""",
  )),
  ("purposes", "3. Çerezlerin kullanım amaçları nelerdir?", (
    """Çerezleri aşağıdaki amaçlarla kullanmaktayız:

<ul class="legal-list">
<li>Sitemizin güvenli bir şekilde çalışmasını sağlamak</li>
<li>Sitemizde gezinmenizi ve sitemizdeki hizmet ve özelliklerden yararlanmanızı sağlamak</li>
<li>Sizlere daha iyi bir deneyim sunmak</li>
<li>Sitemizin performansını artırmak ve internet sitemizi daha kullanıcı dostu hale getirmek</li>
<li>Kullanıcılar (kullanıcı cihazları ve tarayıcı önbellekleri üzerinden) ve site kullanımı hakkında bilgi toplamak</li>
<li>Sitemizi daha fonksiyonel hale getirmek</li>
<li>Kullanıcı davranışlarınızı analiz etmek ve sitemiz üzerindeki genel kullanıcı eğilimini tespit etmek</li>
<li>Ziyaret edilen her sayfanın görüntülenme sayısı dikkate alınarak bir değer belirlemek</li>
<li>Reklam ve pazarlama faaliyetlerimizi geliştirmek</li>
<li>Mevcut ve potansiyel kullanıcılarımızın sitemize eklenen içerikleri sosyal medya ağlarında paylaşmasına imkan vermek</li>
<li>Sitemizin farklı sürümlerinin performansını ölçmek ve Kullanıcılar'ın devamlı aynı sürümü görüntülemesini sağlamak</li>
</ul>""",
    """We use cookies for the following purposes:

<ul class="legal-list">
<li>Ensuring our site operates securely</li>
<li>Enabling navigation and use of services and features</li>
<li>Providing a better experience</li>
<li>Improving performance and user-friendliness</li>
<li>Collecting information about users and site usage via devices and browser caches</li>
<li>Making the site more functional</li>
<li>Analysing user behaviour and identifying general trends</li>
<li>Determining value based on page view counts</li>
<li>Improving advertising and marketing activities</li>
<li>Enabling sharing of content on social networks</li>
<li>Measuring performance of different site versions and ensuring consistent display</li>
</ul>""",
    """Мы используем cookie для следующих целей:

<ul class="legal-list">
<li>Обеспечение безопасной работы сайта</li>
<li>Навигация и использование услуг и функций</li>
<li>Улучшение пользовательского опыта</li>
<li>Повышение производительности и удобства</li>
<li>Сбор информации об использовании сайта</li>
<li>Расширение функциональности</li>
<li>Анализ поведения и выявление трендов</li>
<li>Оценка на основе просмотров страниц</li>
<li>Развитие рекламы и маркетинга</li>
<li>Возможность делиться контентом в соцсетях</li>
<li>Измерение производительности версий сайта</li>
</ul>""",
  )),
  ("general", "4. Çerezlerin genel özellikleri", (
    """Çerezler, internet sitemizde ve mobil uygulamamızda oturum çerezleri ve kalıcı çerezler olarak işlev göstermektedir. Oturum çerezleri, tarayıcınızı kapatmanız ile birlikte çalışmayı durdurmaktadır. Kalıcı çerezler ise, internet tarayıcınızdaki ayarlara bağlı olarak, hard diskinizde uzun süre boyunca kalabilmektedir.""",
    """On our website and mobile application, cookies function as session cookies and persistent cookies. Session cookies stop working when you close your browser. Persistent cookies may remain on your hard drive for a long time depending on your browser settings.""",
    """На сайте и в мобильном приложении используются сессионные и постоянные cookie. Сессионные cookie удаляются при закрытии браузера. Постоянные cookie могут долго храниться на диске в зависимости от настроек браузера.""",
  )),
  ("types", "5. Kullanılan çerezlerin türleri", (
    """İnternet sitemizde kullanılan çerezlerin türleri aşağıda listelenmiştir. Bu çerezler aracılığıyla topladığımız verilerin kişisel veri niteliğinde olması halinde, işbu Çerez Politikası'nı tamamlar nitelikteki Aydınlatma Metni uygulanacaktır.

<h3 class="legal-h3">5.1 Gerekli Çerezler</h3>
<p>Bu tür çerezler, internet sitemizin güvenli bir şekilde çalışabilmesi ve kullanıcıların internet sitemiz üzerinde hareket edebilmesi ve sağlanan hizmetlerden ve özelliklerden faydalanabilmesi için kesinlikle gerekli olan çerezlerdir. Bu tür çerezler, internet sitemizin çalışabilmesi için gereklidir ve kullanıcılar tarafından devre dışı bırakılamazlar.</p>

<h3 class="legal-h3">5.2 Tercih ve İşlevsellik Çerezleri</h3>
<p>Tercih çerezleri, kullanıcıların tercihlerine ilişkin bilgileri toplar ve dil veya kullanıcıların diğer yerel ayarlarını hatırlamamızı ve sitemizi kullanıcılara uygun şekilde kişiselleştirmemizi sağlar. Bu tür çerezler, tarafımızca veya sayfalarınıza hizmetlerini eklediğiniz üçüncü taraf sağlayıcılar tarafından koyulabilir. Kullanıcılar bu tür çerezleri devre dışı bıraktığı takdirde, bu işlevlerin bazıları veya tümü düzgün çalışmayabilir.</p>

<h3 class="legal-h3">5.3 Analitik Çerezler</h3>
<p>Analitik çerezler, kullanıcıların internet sitemizi nasıl kullandıklarını anlamamızı sağlar. Bu çerezler, toplu bir şekilde bilgi toplayarak sitemizin nasıl kullanıldığına dair bize fikir vermekte ve internet sitemizi geliştirmemize yardımcı olmaktadır. Örneğin, bu tip çerezler, site üzerinde en çok hangi sayfaların ziyaret edildiğini göstermekte ve site içinde yaşanılan zorlukların kaydedilmesine yardımcı olmaktadır.</p>

<h3 class="legal-h3">5.4 Reklam/Pazarlama Çerezleri</h3>
<p>Reklam/pazarlama çerezleri reklam ve pazarlama amaçları ile kullanılmaktadır. Bu çerezler, kullanıcıların tarayıcılarını ve cihazlarını tanımlayarak çalışırlar. Bu çerezleri, kullanıcıların ilgi alanlarının profillerini oluşturmak ve kullanıcılara diğer internet sitelerinde ürünümüzle alakalı reklamlar göstermek amacıyla kullanabilmekteyiz. Kullanıcılar, bu çerezlere izin vermedikleri takdirde, kullanıcılara hedefli reklamlar gösterilemeyecektir.</p>""",
    """The types of cookies used on our website are listed below. Where data collected through these cookies constitutes personal data, the Privacy Notice complementing this Cookie Policy shall apply.

<h3 class="legal-h3">5.1 Strictly Necessary Cookies</h3>
<p>These cookies are essential for our website to operate securely and for users to navigate and use services and features. They are required for the site to function and cannot be disabled by users.</p>

<h3 class="legal-h3">5.2 Preference and Functionality Cookies</h3>
<p>Preference cookies collect information about user preferences and allow us to remember language and other local settings to personalise the site. They may be set by us or third-party providers. Disabling them may cause some or all related functions to work improperly.</p>

<h3 class="legal-h3">5.3 Analytics Cookies</h3>
<p>Analytics cookies help us understand how users use our website. They collect information in aggregate to show how the site is used and help us improve it — for example, which pages are visited most and where users encounter difficulties.</p>

<h3 class="legal-h3">5.4 Advertising/Marketing Cookies</h3>
<p>Advertising/marketing cookies are used for advertising and marketing purposes. They identify users' browsers and devices. We may use them to build interest profiles and show product-related ads on other websites. Without consent, targeted ads will not be shown.</p>""",
    """Типы cookie, используемые на сайте, перечислены ниже. Если собранные данные являются персональными, применяется Уведомление о конфиденциальности, дополняющее настоящую Политику.

<h3 class="legal-h3">5.1 Необходимые cookie</h3>
<p>Эти cookie необходимы для безопасной работы сайта, навигации и использования функций. Их нельзя отключить.</p>

<h3 class="legal-h3">5.2 Cookie предпочтений и функциональности</h3>
<p>Cookie предпочтений запоминают язык и локальные настройки для персонализации. Их могут устанавливать мы или третьи лица. Отключение может нарушить работу функций.</p>

<h3 class="legal-h3">5.3 Аналитические cookie</h3>
<p>Аналитические cookie помогают понять, как используется сайт, показывают популярные страницы и затруднения пользователей.</p>

<h3 class="legal-h3">5.4 Рекламные/маркетинговые cookie</h3>
<p>Рекламные cookie используются для маркетинга, профилирования интересов и показа релевантной рекламы на других сайтах. Без согласия таргетированная реклама не показывается.</p>""",
  )),
  ("thirdparty", "6. Üçüncü taraf (Third Party) çerezleri", (
    """Üçüncü parti çerezler, bu çerezleri sağlayan ilgili üçüncü parti tarafından değiştirilebilecektir. Bu çerezlerle ilgili daha güncel bilgi almak için, ilgili üçüncü parti çerez sağlayıcıları ile iletişime geçebilirsiniz.""",
    """Third-party cookies may be modified by the relevant third-party provider. For up-to-date information about these cookies, you may contact the relevant third-party cookie providers.""",
    """Сторонние cookie могут изменяться соответствующими поставщиками. Актуальную информацию можно получить у них напрямую.""",
  )),
  ("disable", "7. Çerezler nasıl devre dışı bırakılır?", (
    f"""Çerez tercihlerinizi, tarayıcı ayarlarınızı değiştirerek isteğinize göre uyarlayabilirsiniz. Tarayıcınızın sunmuş olduğu imkanlara göre, çerezlerin kullanılmasını engelleyebilir, çerez kullanılmadan önce uyarı alabilir veya sadece bazı çerezleri devre dışı bırakabilir ya da silebilirsiniz. Çerezlerle alakalı tercihlerin, sitemize erişim sağladığınız her bir cihaz (tarayıcı ayarları) özelinde ayrı olarak silinmesi gerekmektedir.

<p>Çerezleri nasıl etkinleştireceğiniz, devre dışı bırakacağınız ya da kaldıracağınıza ilişkin bilgiler, internet tarayıcı sağlayıcısının sitesindeki 'Yardım' ekranında yer almaktadır. Aşağıdaki bağlantılar yardımıyla ilgili sayfalara ulaşabilirsiniz:</p>
{BROWSER_LINKS}
<p>Bazı çerezleri devre dışı bırakmanız halinde sitemizin çeşitli fonksiyonlarının çalışmayabileceğini hatırlatmak isteriz.</p>""",
    f"""You can adjust your cookie preferences by changing your browser settings. Depending on your browser, you may block cookies, receive warnings before cookies are used, or disable or delete only some cookies. Cookie preferences must be cleared separately on each device and browser you use to access our site.

<p>Information on enabling, disabling or removing cookies is available in the 'Help' section of your browser provider's website. You can reach the relevant pages via the links below:</p>
{BROWSER_LINKS}
<p>Please note that disabling some cookies may cause certain functions of our site not to work.</p>""",
    f"""Вы можете настроить cookie через параметры браузера: блокировать, получать предупреждения или удалять отдельные cookie. Настройки нужно менять на каждом устройстве отдельно.

<p>Информация об управлении cookie доступна в разделе «Справка» сайта браузера. Ссылки:</p>
{BROWSER_LINKS}
<p>Отключение некоторых cookie может нарушить работу функций сайта.</p>""",
  )),
  ("contact", "8. Bize ulaşın", (
    """FNV Elektronik, Çerez Politikası'nın hükümlerini dilediği zaman değiştirebilecektir. Çerez Politikasında yaptığımız değişikliklerden veya güncellemelerden haberdar olabilmek için aralıklı olarak bu sayfayı kontrol edebilirsiniz.

<p>Çerez Politikası veya internet sitemizdeki çerez kullanımı hakkında soru, görüş ve önerileriniz için bizimle <a href="mailto:info@fnvelektronik.com">info@fnvelektronik.com</a> adresi üzerinden iletişime geçebilirsiniz.</p>""",
    """FNV Elektronik may change the provisions of this Cookie Policy at any time. You may check this page periodically to stay informed of changes or updates.

<p>For questions, comments or suggestions about this Cookie Policy or cookie use on our website, contact us at <a href="mailto:info@fnvelektronik.com">info@fnvelektronik.com</a>.</p>""",
    """FNV Elektronik вправе изменять настоящую Политику cookie в любое время. Периодически проверяйте эту страницу для актуальной информации.

<p>По вопросам использования cookie на сайте: <a href="mailto:info@fnvelektronik.com">info@fnvelektronik.com</a>.</p>""",
  )),
]

TITLE_TR = {s[0]: s[1] for s in SECTIONS}
TITLE_EN = {
  "intro": "1. Introduction",
  "what": "2. What is a cookie?",
  "purposes": "3. Purposes of cookie use",
  "general": "4. General characteristics of cookies",
  "types": "5. Types of cookies used",
  "thirdparty": "6. Third-party cookies",
  "disable": "7. How to disable cookies",
  "contact": "8. Contact us",
}
TITLE_RU = {
  "intro": "1. Введение",
  "what": "2. Что такое cookie?",
  "purposes": "3. Цели использования cookie",
  "general": "4. Общие характеристики cookie",
  "types": "5. Типы используемых cookie",
  "thirdparty": "6. Сторонние cookie",
  "disable": "7. Как отключить cookie",
  "contact": "8. Связаться с нами",
}

def extract_nav_inner(path):
    text = open(path, encoding="utf-8").read()
    start = text.index("<nav")
    start = text.index(">", start) + 1
    end = text.index("</nav>", start)
    return text[start:end].strip()

NAV = extract_nav_inner(ROOT / "documents.html")
FOOTER = open(ROOT / "index.html", encoding="utf-8").read().split("<footer>")[1].split("</footer>")[0]

sections = ""
for key, title_tr, bodies in SECTIONS:
    tr, en, ru = bodies
    title = L(title_tr, TITLE_EN[key], TITLE_RU[key])
    sections += f'''      <section class="legal-block">
        <h2 class="legal-h2">{title}</h2>
        <div class="legal-body">{L(tr, en, ru, block=True)}</div>
      </section>
'''

html = f'''<!DOCTYPE html>
<html lang="tr">
<head>
  <script>try{{var l=localStorage.getItem('fnv-lang');if(l==='en'||l==='ru')document.documentElement.classList.add('lang-'+l);}}catch(e){{}}</script>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="icon" href="assets/logo-mark.png" type="image/png" />
  <link rel="apple-touch-icon" href="assets/logo-mark.png" />
  <title>Çerez Politikası — FNV Elektronik</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/site.css?v=41" />
</head>
<body>

<nav class="nav solid" id="mainNav">
{NAV}
</nav>

<section class="svc-hero">
  <div class="svc-hero-bg" style="background-image:url('assets/istanbul-skyline.png')"></div>
  <div class="svc-hero-content">
    <div class="crumb">
      <a href="index.html">{L("Ana Sayfa", "Home", "Главная")}</a>
      <span class="sep">/</span>
      <span class="cur">{L("Çerez Politikası", "Cookie Policy", "Политика cookie")}</span>
    </div>
    <span class="svc-hero-eyebrow">{L("Yasal", "Legal", "Правовая информация")}</span>
    <h1 class="svc-hero-title">{L("Çerez<br>Politikası", "Cookie<br>Policy", "Политика<br>cookie")}</h1>
  </div>
</section>

<section class="legal-page">
  <div class="legal-page-inner">
    <p class="legal-updated">{L("Güncellenme tarihi: 01.07.2026", "Last updated: 1 July 2026", "Дата обновления: 01.07.2026")}</p>
{sections}    <p class="legal-contact">{L("İlgili diğer belgeler: ", "Related documents: ", "Связанные документы: ")}<a href="privacy-policy.html">{L("Gizlilik Politikası", "Privacy Policy", "Политика конфиденциальности")}</a></p>
  </div>
</section>

<footer>{FOOTER}
</footer>

<script src="assets/site.js?v=41"></script>
</body>
</html>
'''

(ROOT / "cookie-policy.html").write_text(html, encoding="utf-8")
print("Wrote cookie-policy.html")
