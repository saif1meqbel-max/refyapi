#!/usr/bin/env python3
"""Generate privacy-policy.html and return footer link snippet."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def L(tr, en, ru, block=False):
    tag = "div" if block else "span"
    return f'<{tag} data-lang="tr">{tr}</{tag}><{tag} data-lang="en">{en}</{tag}><{tag} data-lang="ru">{ru}</{tag}>'

SECTIONS = [
  ("intro", None, (
    "Fnv Elektronik ve Bilgisayar Ltd. Şti.'nin (\"FNV Elektronik\") kullanıcıların (\"Kullanıcı(lar)\") arzusuna bağlı olarak web sitesi (\"Web Sitesi\") üzerinden elde ettiği kişisel verileri toplarken ve kullanırken izlediği prensipler bu Gizlilik Politikası'nda düzenlenmektedir.",
    "This Privacy Policy sets out the principles followed by Fnv Elektronik ve Bilgisayar Ltd. Şti. (\"FNV Elektronik\") when collecting and using personal data obtained from users (\"User(s)\") through the website (\"Website\") at their discretion.",
    "Настоящая Политика конфиденциальности определяет принципы, которых придерживается Fnv Elektronik ve Bilgisayar Ltd. Şti. (\"FNV Elektronik\") при сборе и использовании персональных данных пользователей (\"Пользователь(и)\") через веб-сайт (\"Веб-сайт\") по их желанию.",
  )),
  ("collect", "Toplanabilecek Kişisel Veriler", (
    """FNV Elektronik, Web Sitesi üzerinde, Kullanıcıların Web Sitesi'ne erişimi ve yapacakları işlemlere bağlı olarak Kullanıcı'nın;

<ul class="legal-list">
<li>Kimlik Bilgisini</li>
<li>İşlem Güvenliği Bilgisini</li>
<li>IP Bilgisini</li>
<li>Hukuki İşlem ve Uyum Bilgisini</li>
<li>İletişim Bilgisini</li>
<li>Talep/Şikayet Yönetimi Bilgisini</li>
<li>Kullanıcı Bilgisini</li>
<li>Olay Yönetim Bilgisini</li>
<li>Kullanıcı İşlem Bilgisini</li>
</ul>

Web Sitesi'ne konu hizmetlerin ifa edilmesi için gerekli olabilecek ve Kişisel Verilerin Korunması Kanunu ve ilgili tüm mevzuat uyarınca kişisel veri sayılan sair bilgileri toplayabilecektir. Kullanıcı, kendi arzusu doğrultusunda FNV Elektronik ile paylaşabileceği verilerin işbu Gizlilik Politikası'nda belirtilen kapsamda, belirtilen amaçlarla işlenmesine açıkça muvafakat etmektedir.

<p>Kişisel Verilerin Korunması Kanunu'nun 3 ve 7. maddesi uyarınca, geri döndürülemeyecek şekilde anonim hale getirilen veriler, anılan kanun hükümleri uyarınca kişisel veri olarak kabul edilmeyecek ve bu verilere ilişkin işleme faaliyetleri işbu Gizlilik Politikası hükümleri ile bağlı olmaksızın gerçekleştirilecektir.</p>""",
    """On the Website, depending on Users' access and transactions, FNV Elektronik may collect the User's:

<ul class="legal-list">
<li>Identity information</li>
<li>Transaction security information</li>
<li>IP information</li>
<li>Legal process and compliance information</li>
<li>Contact information</li>
<li>Request/complaint management information</li>
<li>User information</li>
<li>Incident management information</li>
<li>User transaction information</li>
</ul>

and other data that may be required to provide Website services and that qualify as personal data under the Personal Data Protection Law and related legislation. The User expressly consents to the processing of data they may share with FNV Elektronik at their discretion within the scope and for the purposes set out in this Privacy Policy.

<p>Pursuant to Articles 3 and 7 of the Personal Data Protection Law, data irreversibly anonymised shall not be regarded as personal data, and processing of such data may be carried out without being bound by this Privacy Policy.</p>""",
    """На Веб-сайте, в зависимости от доступа и действий Пользователей, FNV Elektronik может собирать:

<ul class="legal-list">
<li>Идентификационные данные</li>
<li>Данные безопасности транзакций</li>
<li>IP-данные</li>
<li>Данные правовых процедур и соответствия</li>
<li>Контактные данные</li>
<li>Данные управления запросами/жалобами</li>
<li>Данные пользователя</li>
<li>Данные управления инцидентами</li>
<li>Данные пользовательских операций</li>
</ul>

и иные данные, необходимые для оказания услуг и относящиеся к персональным в соответствии с Законом о защите персональных данных. Пользователь даёт явное согласие на обработку данных в объёме и целях, указанных в настоящей Политике.

<p>В соответствии со ст. 3 и 7 Закона, необратимо анонимизированные данные не считаются персональными, и их обработка может осуществляться без ограничений настоящей Политики.</p>""",
  )),
  ("cookies", '"Cookie" Kullanımı', (
    """FNV Elektronik tarafından, Kullanıcılar'ın Web Sitesi'ndeki dolaşımları sırasında ziyaret edilen bölümler, tıklanan alanlar gibi veriler otomatik olarak toplanmaktadır. "Cookie" adlı teknoloji kullanılarak elde edilen bu veriler istatistiksel bilgilerdir. Bu teknoloji ile amaçlanan, Kullanıcılar'ın ziyaret ettikleri bölümlere ait içeriği, siteye ilk ziyaretlerinden itibaren Kullanıcı için daha kolay ulaşılır kılmaktır. Tarayıcıların pek çoğu başta teknik iletişim dosyası olan bu "cookie"leri kabul eder biçimde tasarlanmıştır, ancak Kullanıcılar dilerlerse teknik iletişim dosyasının gelmemesi veya teknik iletişim dosyasının gönderildiğinde ikaz verilmesini sağlayacak biçimde tarayıcı ayarlarını her zaman için değiştirebilirler.

<p>FNV Elektronik, online davranışsal reklamcılık ve pazarlama yapılabilmesi amacıyla Kullanıcılar'ın Web Sitesi'ndeki davranışlarını tarayıcıda bulunan bir "cookie" ile ilişkilendirme ve görüntülenen sayfa sayısı, ziyaret süresi ve hedef tamamlama sayısı gibi metrikleri temel alan yeniden pazarlama listeleri tanımlama hakkını haizdir. Sonrasında Kullanıcı'ya Web Sitesi'nde ya da görüntülü reklam ağındaki diğer sitelerde ilgi alanlarına göre hedefe yönelik reklam içeriği gösterilebilir.</p>""",
    """During Users' navigation on the Website, data such as sections visited and areas clicked are collected automatically by FNV Elektronik using "cookie" technology. This data is statistical. The purpose is to make content in visited sections more accessible from the User's first visit. Most browsers accept cookies by default; Users may change browser settings to block cookies or receive warnings when cookies are sent.

<p>FNV Elektronik may associate Users' Website behaviour with browser cookies and define remarketing lists based on metrics such as pages viewed, visit duration and goal completions for online behavioural advertising and marketing. Targeted advertising may then be shown on the Website or other sites in display networks according to interests.</p>""",
    """При навигации по Веб-сайту FNV Elektronik автоматически собирает данные о посещённых разделах и кликах с помощью технологии «cookie». Эти статистические данные делают контент более доступным с первого визита. Браузеры обычно принимают cookies по умолчанию; Пользователь может изменить настройки для блокировки или предупреждений.

<p>FNV Elektronik вправе связывать поведение на Веб-сайте с cookie и формировать списки ремаркетинга для поведенческой рекламы. Пользователю могут показываться таргетированные объявления на Веб-сайте или других площадках.</p>""",
  )),
  ("purpose", "Verilerin Kullanılma Amacı", (
    """FNV Elektronik, toplanan kişisel verileri Kullanıcı'nın Web Sitesi'nden faydalanabilmesi, Web Sitesi'ne üyelik söz konusu ise üyelik kaydının gerçekleştirilmesi, sunduğu hizmetlerin iyileştirilmesi, hizmetin geliştirilmesi, yeni hizmetlerin tanıtımı ve bilgilendirilmesi, bu kapsamda Kullanıcı'ya gerekli bilgilendirilmelerin yapılması, Kullanıcı ile temas kurulması ve sunduğu hizmetlerin doğasından kaynaklanan yükümlülüklerin yerine getirilmesi için işleyebilir.

<p>Söz konusu kişisel veriler FNV Elektronik raporlama ve iş geliştirme faaliyetleri kapsamında işlenebilecek, Kullanıcı'nın kimliği ifşa edilmeden çeşitli istatistiksel değerlendirmeler yapma, veri tabanı oluşturma ve pazar araştırmalarında bulunma amacıyla da kullanılabilecektir. Kullanıcı'nın ayrıca onay vermesi halinde söz konusu bilgiler FNV Elektronik ve işbirliğinde olduğu kişiler tarafından doğrudan pazarlama yapmak amacıyla işlenebilecek, saklanabilecek, üçüncü kişilere iletilebilecek ve söz konusu bilgiler üzerinden çeşitli uygulama, ürün ve hizmetlerin tanıtımı, bakım ve destek faaliyetlerine ilişkin bildirimlerde bulunma amacıyla Kullanıcı ile iletişime geçilebilecektir.</p>

<p>FNV Elektronik ayrıca, Kişisel Verilerin Korunması Kanunu'nun 5 ve 8. maddeleri uyarınca ve/veya ilgili mevzuattaki istisnaların varlığı halinde kişisel verileri Kullanıcı'nın ayrıca rızasını almaksızın işleyebilecek ve üçüncü kişilerle paylaşabilecektir. Bu durumların başlıcaları aşağıda belirtilmiştir:</p>

<ul class="legal-list">
<li>Kanunlarda açıkça öngörülmesi</li>
<li>Fiili imkansızlık nedeniyle rızasını açıklayamayacak durumda bulunan veya rızasına hukuki geçerlilik tanınmayan kişinin kendisinin ya da bir başkasının hayatı veya beden bütünlüğünün korunması için zorunlu olması</li>
<li>Kullanıcı ile FNV Elektronik arasında herhangi bir sözleşmenin kurulması veya ifasıyla doğrudan doğruya ilgili olması kaydıyla, kişisel verilerin işlenmesinin gerekli olması</li>
<li>Hukuki yükümlülüklerin yerine getirilebilmesi için zorunlu olması</li>
<li>Kullanıcı'nın kendisi tarafından alenileştirilmiş olması</li>
<li>Bir hakkın tesisi, kullanılması veya korunması için veri işlemenin zorunlu olması</li>
<li>Kullanıcı'nın temel hak ve özgürlüklerine zarar vermemek kaydıyla, FNV Elektronik'in meşru menfaatleri için veri işlenmesinin zorunlu olması</li>
</ul>""",
    """FNV Elektronik may process collected personal data so that the User can benefit from the Website, complete membership registration where applicable, improve and develop services, promote new services, provide necessary information, contact the User and fulfil obligations arising from the nature of its services.

<p>Such data may also be processed for reporting and business development, statistical evaluation without disclosing identity, database creation and market research. With additional User consent, information may be processed, stored, transferred to third parties and used for direct marketing and notifications regarding products, maintenance and support.</p>

<p>Under Articles 5 and 8 of the Personal Data Protection Law and applicable exceptions, FNV Elektronik may process and share personal data without separate consent, including where:</p>

<ul class="legal-list">
<li>Explicitly required by law</li>
<li>Necessary to protect life or physical integrity where consent cannot be given</li>
<li>Necessary for establishment or performance of a contract between User and FNV Elektronik</li>
<li>Necessary to fulfil legal obligations</li>
<li>Data has been made public by the User</li>
<li>Necessary to establish, exercise or defend a legal right</li>
<li>Necessary for legitimate interests of FNV Elektronik without harming fundamental rights and freedoms</li>
</ul>""",
    """FNV Elektronik обрабатывает персональные данные для использования Веб-сайта, регистрации (если применимо), улучшения услуг, информирования, связи с Пользователем и выполнения обязательств.

<p>Данные могут использоваться для отчётности, статистики без раскрытия личности, баз данных и маркетинговых исследований. При дополнительном согласии — для прямого маркетинга и уведомлений о продуктах и поддержке.</p>

<p>Согласно ст. 5 и 8 Закона и исключениям, обработка и передача возможны без отдельного согласия, в том числе когда это:</p>

<ul class="legal-list">
<li>прямо предусмотрено законом</li>
<li>необходимо для защиты жизни или здоровья</li>
<li>необходимо для заключения или исполнения договора</li>
<li>необходимо для исполнения юридических обязанностей</li>
<li>данные обнародованы Пользователем</li>
<li>необходимо для установления или защиты прав</li>
<li>необходимо для законных интересов FNV Elektronik</li>
</ul>""",
  )),
  ("sharing", "Verilerin Paylaşımı", (
    """FNV Elektronik, Kullanıcılar'a ait kişisel verileri ve bu kişisel verileri kullanarak elde ettiği yeni verileri Web Sitesi kapsamında Kullanıcı'ya sunulan hizmetlerin ifası amacıyla hizmetlerinden faydalandığı üçüncü kişilere, söz konusu hizmetlerin temini amacıyla sınırlı olmak üzere aktarabilecektir. Bu kapsamda FNV Elektronik, Kullanıcı deneyiminin geliştirilmesi (iyileştirme ve kişiselleştirme dahil), Kullanıcı'nın güvenliğini sağlamak, hileli ya da izinsiz kullanımları tespit etmek, operasyonel değerlendirme araştırılması, Web Sitesi veya FNV Elektronik hizmetlerine ilişkin hataların giderilmesi ve işbu Gizlilik Politikası'nda veya Kullanıcı'ya sunulan sair gizlilik metinlerinde yer alan amaçlardan herhangi birisini gerçekleştirebilmek için Kullanıcı verilerini dış kaynak hizmet sağlayıcıları, barındırma hizmet sağlayıcıları ("hosting" servisleri), hukuk büroları, araştırma şirketleri, çağrı merkezleri gibi üçüncü kişiler ile paylaşabilecektir.

<p>Kullanıcı, yukarıda belirtilen amaçlarla sınırlı olmak kaydı ile bahsi geçen üçüncü tarafların Kullanıcı'nın kişisel verilerini dünyanın herhangi bir yerinde bulunan sunucularında saklayabileceğini, bu hususa peşinen muvafakat ettiğini kabul eder.</p>""",
    """FNV Elektronik may transfer Users' personal data and derived data to third parties from whom it receives services, limited to providing Website services. Data may be shared with external service providers, hosting services, law firms, research companies and call centres to improve User experience, ensure security, detect fraud, conduct operational research, fix errors and fulfil purposes in this Privacy Policy or other privacy texts.

<p>The User accepts that such third parties may store personal data on servers anywhere in the world for the purposes stated above.</p>""",
    """FNV Elektronik может передавать персональные данные третьим лицам, оказывающим услуги, в объёме, необходимом для работы Веб-сайта — провайдерам, хостингу, юридическим и исследовательским компаниям, колл-центрам для улучшения опыта, безопасности, выявления мошенничества и иных целей Политики.

<p>Пользователь соглашается, что такие третьи лица могут хранить данные на серверах в любой точке мира в указанных целях.</p>""",
  )),
  ("rights", "Kullanıcı'nın Verilere Erişim Hakkı ve Düzeltme Talepleri", (
    """Kullanıcı, FNV Elektronik'e başvurarak kendisiyle ilgili:

<ul class="legal-list">
<li>Kişisel veri işlenip işlenmediğini öğrenme</li>
<li>Kişisel verileri işlenmişse buna ilişkin bilgi talep etme</li>
<li>Kişisel verilerin işlenme amacını ve bunların amacına uygun kullanılıp kullanılmadığını öğrenme</li>
<li>Yurt içinde veya yurt dışında kişisel verilerin aktarıldığı üçüncü kişileri bilme</li>
<li>Kişisel verilerin eksik veya yanlış işlenmiş olması halinde bunların düzeltilmesini isteme</li>
<li>İlgili mevzuatta öngörülen şartlar çerçevesinde kişisel verilerin silinmesini veya yok edilmesini isteme</li>
<li>İlgili mevzuat uyarınca yapılan düzeltme, silme ve yok edilme işlemlerinin, kişisel verilerin aktarıldığı üçüncü kişilere bildirilmesini isteme</li>
<li>İşlenen verilerin münhasıran otomatik sistemler vasıtasıyla analiz edilmesi suretiyle kişinin kendisi aleyhine bir sonucun ortaya çıkmasına itiraz etme</li>
<li>Kişisel verilerin kanuna aykırı olarak işlenmesi sebebiyle zarara uğraması halinde zararın giderilmesini talep etme</li>
</ul>

<p>haklarına sahiptir.</p>

<p>FNV Elektronik, yukarıda yer alan talepler uyarınca, gerekçeli olumlu/olumsuz yanıtını, yazılı veya dijital ortamdan gerçekleştirebilir. Taleplere ilişkin gerekli işlemler için ücret alınmaması esastır. Bununla birlikte, işlemlerin bir maliyet gerektirmesi halinde, Kişisel Verilerin Korunması Kurulu tarafından, Kişisel Verilerin Korunması Kanunu'nun 13. maddesine göre belirlenen tarife üzerinden ücret talep edilmesi mümkündür.</p>

<p>Kullanıcı, FNV Elektronik'e kendisi tarafından sağlanmış olan, işbu Gizlilik Politikası'na konu bilgilerin tam, doğru ve güncel olduğunu, bu bilgilerde herhangi bir değişiklik olması halinde bunları derhal güncelleyeceğini taahhüt eder. Kullanıcı'nın güncel bilgileri sağlamamış olması halinde FNV Elektronik'in herhangi bir sorumluluğu olmayacaktır.</p>

<p>Kullanıcı, herhangi bir kişisel verisinin FNV Elektronik tarafından kullanılamaması ile sonuçlanacak bir talepte bulunması halinde FNV Elektronik'in kendisine taahhüt ettiği hizmetlerden tam olarak faydalanamayabileceğini, bu kapsamda doğacak her türlü sorumluluğun kendisine ait olacağını kabul ve beyan eder.</p>""",
    """The User may apply to FNV Elektronik to:

<ul class="legal-list">
<li>Learn whether personal data is processed</li>
<li>Request information if data is processed</li>
<li>Learn the purpose of processing and whether use is consistent with that purpose</li>
<li>Know third parties to whom data is transferred domestically or abroad</li>
<li>Request correction of incomplete or inaccurate data</li>
<li>Request deletion or destruction under applicable law</li>
<li>Request notification of correction/deletion to third parties</li>
<li>Object to adverse results from solely automated analysis</li>
<li>Claim compensation for damage from unlawful processing</li>
</ul>

<p>FNV Elektronik may respond in writing or digitally with reasoned approval or rejection. Fees are generally not charged; where costs arise, fees may be requested per the tariff under Article 13 of the Personal Data Protection Law.</p>

<p>The User undertakes that information provided is complete, accurate and current and will update changes promptly. FNV Elektronik bears no liability if current information is not provided.</p>

<p>If a request results in data no longer being usable, the User accepts they may not fully benefit from promised services and bears resulting responsibility.</p>""",
    """Пользователь вправе обратиться в FNV Elektronik чтобы:

<ul class="legal-list">
<li>узнать, обрабатываются ли персональные данные</li>
<li>получить информацию об обработке</li>
<li>узнать цели и соответствие использования</li>
<li>узнать третьих лиц, которым данные передаются</li>
<li>требовать исправления неточных данных</li>
<li>требовать удаления в рамках закона</li>
<li>требовать уведомления третьих лиц об исправлении/удалении</li>
<li>возражать против неблагоприятных результатов автоматизированного анализа</li>
<li>требовать возмещения ущерба от незаконной обработки</li>
</ul>

<p>FNV Elektronik отвечает письменно или в цифровом виде. Плата обычно не взимается; при необходимости — по тарифу ст. 13 Закона.</p>

<p>Пользователь обязуется предоставлять полные и актуальные данные и обновлять их. FNV Elektronik не несёт ответственности при неактуальных данных.</p>

<p>Если запрос делает использование данных невозможным, Пользователь принимает ограничение услуг и ответственность за последствия.</p>""",
  )),
  ("retention", "Kişisel Verilerin Saklama Süresi", (
    """FNV Elektronik, Kullanıcı tarafından sağlanan kişisel verileri, sunduğu hizmetlerin mahiyetinden kaynaklanan yükümlülüklerin yerine getirilmesi amacıyla, hizmetlerin sağlandığı süre boyunca saklayacaktır.

<p>Buna ek olarak, FNV Elektronik, Kullanıcı ile arasında doğabilecek herhangi bir uyuşmazlık durumunda, uyuşmazlık kapsamında gerekli savunmaların gerçekleştirilebilmesi amacıyla sınırlı olmak üzere ve ilgili mevzuat uyarınca belirlenen zamanaşımı süreleri boyunca kişisel verileri saklayabilecektir.</p>""",
    """FNV Elektronik will retain personal data provided by the User for the duration of services to fulfil obligations arising from the nature of those services.

<p>Additionally, in the event of disputes, data may be retained for limitation periods under applicable law to enable necessary defences.</p>""",
    """FNV Elektronik хранит персональные данные в течение срока оказания услуг для выполнения связанных обязательств.

<p>Дополнительно при спорах данные могут храниться в пределах сроков исковой давности по закону.</p>""",
  )),
  ("security", "Veri Güvenliğine İlişkin Önlemler, Taahhütler ve Sorumluluk", (
    """FNV Elektronik, ilgili mevzuatta belirlenen veya işbu Gizlilik Politikası'nda ifade edilen şartlarda:

<ul class="legal-list">
<li>kişisel verilerin hukuka aykırı olarak işlenmemesini,</li>
<li>kişisel verilere hukuka aykırı olarak erişilmemesini ve</li>
<li>kişisel verilerin muhafazasını</li>
</ul>

<p>sağlamak amacıyla uygun güvenlik düzeyini temin etmeye yönelik gerekli teknik ve idari tedbirleri almayı, gerekli denetimleri yaptırmayı taahhüt eder.</p>

<p>Site üzerinde başka uygulamalara link verilmesi halinde, FNV Elektronik uygulamaların gizlilik politikaları ve içeriklerine yönelik bünyesinde herhangi bir sorumluluk taşımamaktadır.</p>

<p>FNV Elektronik kişisel verilerin yukarıdaki şartlar çerçevesinde kullanılması sonucu meydana gelebilecek zararlardan dolayı sorumluluk kabul etmez.</p>""",
    """FNV Elektronik undertakes to take necessary technical and administrative measures and conduct audits to ensure appropriate security so that personal data is not processed unlawfully, accessed unlawfully, or lost, under applicable law and this Privacy Policy.

<p>Where the Site links to other applications, FNV Elektronik accepts no responsibility for their privacy policies or content.</p>

<p>FNV Elektronik accepts no liability for damages that may arise from use of personal data within the above framework.</p>""",
    """FNV Elektronik обязуется принимать технические и организационные меры и проводить проверки для обеспечения надлежащей защиты персональных данных от незаконной обработки, доступа и утраты.

<p>На ссылки на другие приложения FNV Elektronik не несёт ответственности за их политики и контент.</p>

<p>FNV Elektronik не несёт ответственности за ущерб от использования данных в указанных рамках.</p>""",
  )),
  ("changes", "Gizlilik Politikası'ndaki Değişiklikler", (
    """Web Sitesi'nde sunulan hizmetlerden yararlananlar bütün bu şartları okumuş ve kabul etmiş sayılırlar. FNV Elektronik, Gizlilik Politikası hükümlerini önceden haber vermeksizin değiştirme hakkını saklı tutar. Güncel Gizlilik Politikası, Kullanıcı'ya herhangi bir yöntemle sunulduğu tarihte yürürlük kazanır.""",
    """Those who use services on the Website are deemed to have read and accepted all these terms. FNV Elektronik reserves the right to change this Privacy Policy without prior notice. The updated Privacy Policy takes effect on the date it is made available to the User by any means.""",
    "Пользователи услуг Веб-сайта считаются прочитавшими и принявшими все условия. FNV Elektronik вправе изменять Политику без предварительного уведомления. Обновлённая Политика вступает в силу с даты её предоставления Пользователю любым способом.",
  )),
]

TITLE_TR = {
  "collect": "Toplanabilecek Kişisel Veriler",
  "cookies": '"Cookie" Kullanımı',
  "purpose": "Verilerin Kullanılma Amacı",
  "sharing": "Verilerin Paylaşımı",
  "rights": "Kullanıcı'nın Verilere Erişim Hakkı ve Düzeltme Talepleri",
  "retention": "Kişisel Verilerin Saklama Süresi",
  "security": "Veri Güvenliğine İlişkin Önlemler, Taahhütler ve Sorumluluk",
  "changes": "Gizlilik Politikası'ndaki Değişiklikler",
}
TITLE_EN = {
  "collect": "Personal Data That May Be Collected",
  "cookies": "Use of Cookies",
  "purpose": "Purpose of Use of Data",
  "sharing": "Sharing of Data",
  "rights": "User Access Rights and Correction Requests",
  "retention": "Retention Period of Personal Data",
  "security": "Data Security Measures, Commitments and Liability",
  "changes": "Changes to the Privacy Policy",
}
TITLE_RU = {
  "collect": "Собираемые персональные данные",
  "cookies": "Использование cookie",
  "purpose": "Цели использования данных",
  "sharing": "Передача данных",
  "rights": "Права доступа и исправления",
  "retention": "Срок хранения персональных данных",
  "security": "Меры безопасности и ответственность",
  "changes": "Изменения Политики конфиденциальности",
}

def extract_nav_inner(path):
    text = open(path, encoding="utf-8").read()
    start = text.index("<nav")
    start = text.index(">", start) + 1
    end = text.index("</nav>", start)
    return text[start:end].strip()

NAV = extract_nav_inner(ROOT / "documents.html")
FOOTER = open(ROOT / "index.html", encoding="utf-8").read().split("<footer>")[1].split("</footer>")[0]

def section_html(key, title_key, bodies):
    tr, en, ru = bodies
    if title_key is None:
        return f'      <div class="legal-block">{L(tr, en, ru)}</div>\n'
    title = L(TITLE_TR[key], TITLE_EN[key], TITLE_RU[key])
    return f'''      <section class="legal-block">
        <h2 class="legal-h2">{title}</h2>
        <div class="legal-body">{L(tr, en, ru, block=True)}</div>
      </section>
'''

sections = ""
for item in SECTIONS:
    sections += section_html(item[0], item[1], item[2])

html = f'''<!DOCTYPE html>
<html lang="tr">
<head>
  <script>try{{var l=localStorage.getItem('fnv-lang');if(l==='en'||l==='ru')document.documentElement.classList.add('lang-'+l);}}catch(e){{}}</script>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="icon" href="assets/logo-mark.png" type="image/png" />
  <link rel="apple-touch-icon" href="assets/logo-mark.png" />
  <title>Gizlilik Politikası — FNV Elektronik</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/site.css?v=40" />
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
      <span class="cur">{L("Gizlilik Politikası", "Privacy Policy", "Политика конфиденциальности")}</span>
    </div>
    <span class="svc-hero-eyebrow">{L("Yasal", "Legal", "Правовая информация")}</span>
    <h1 class="svc-hero-title">{L("Gizlilik<br>Politikası", "Privacy<br>Policy", "Политика<br>конфиденциальности")}</h1>
  </div>
</section>

<section class="legal-page">
  <div class="legal-page-inner">
    <p class="legal-updated">{L("Güncellenme tarihi: 01.07.2026", "Last updated: 1 July 2026", "Дата обновления: 01.07.2026")}</p>
{sections}    <p class="legal-contact">{L("İlgili diğer belgeler: ", "Related documents: ", "Связанные документы: ")}<a href="cookie-policy.html">{L("Çerez Politikası", "Cookie Policy", "Политика cookie")}</a> · {L("Gizlilik talepleri: ", "Privacy requests: ", "Запросы по конфиденциальности: ")}<a href="mailto:info@fnvelektronik.com">info@fnvelektronik.com</a></p>
  </div>
</section>

<footer>{FOOTER}
</footer>

<script src="assets/site.js?v=40"></script>
</body>
</html>
'''

(ROOT / "privacy-policy.html").write_text(html, encoding="utf-8")
print("Wrote privacy-policy.html")
