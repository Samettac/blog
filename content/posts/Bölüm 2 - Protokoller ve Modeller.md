---
title: Protokoller ve Modeller
date: 2026-04-25
draft: false
summary: Protokoller, OSI ve TCP/IP Modelleri.
tags:
  - CCNA
  - osi
  - tcp-ip
  - protokol
  - encapsulation
cover:
  image: <image path/url>
  alt: <alt text>
  caption: <text>
  relative: false
  hidden: true
---
---
## Ağ İletişiminin Temelleri
Ağ haberleşmesi, tıpkı mektup haberleşmesine benzer. 
İletişimin gerçekleşebilmesi için temel olarak 3 unsura ihtiyaç vardır:
1. **Gönderici (Sender)**
2. **Alıcı (Receiver)**
3. **Ortam (Media)**

### Protokol Nedir?
Protokol, iletişimin başarılı bir şekilde gerçekleşmesi için tanımlanan kurallar dizisidir. 
Ağ haberleşmesinde protokoller aşağıdaki ihtiyaçlara çözüm sağlar:
* **Mesaj Kodlama (Encoding):** 
	* Data'nın, iletim ortamına göre elektrik dalgasına, ışığa veya radyo frekansına çevrilmesidir (çevirmen gibi).
* **Mesaj Biçimlendirme ve Kapsülleme (Formatting & Encapsulation):** 
	* Data iletilirken başlık (header) ve kuyruk (trailer) bilgileri eklenir. 
	* Hedefte bu bilgiler atılıp data'ya ulaşılır. 
	* Aynı mektup haberleşmesi gibi, zarf yırtılır ve mektuba ulaşılır.
* **Mesaj Boyutu (Size):** 
	* Data büyük bir bütün halinde gönderilmek yerine küçük parçalara bölünerek gönderilir. 
	* Bu sayede bir hata olursa bütün data çöp olmamış olur.
	* Ayrıca aynı data yolu aynı anda farklı işlemler için de kullanılabilir.
		* Örneğin: Biri video izlerken başka birisi internette gezebilir.
* **Mesaj Zamanlaması (Timing):** 
	* **Flow Control:** paketin hızının ayarlanması. 
		* Örneğin: Yaşlı biriyle konuşurken daha yavaş, genç birisiyle daha hızlı konuşmak gibi.
	* **Responce Timeout:** amca duymadı ne kadar bekleyip tekrar seslenicen.
	* **Access Method:** Çakışmaları önlemek için kullanılan algoritmalar.
		* Örneğin: CSMA/CD, CSMA/CA

### Mesaj Teslim Seçenekleri
![Pasted image 20260425005413.png](/images/Pasted%20image%2020260425005413.png)
* **Unicast (Tekil Yayın):** Birebir iletişimdir (Örn: A cihazından B cihazına).
* **Multicast (Çoklu Yayın):** Belirli bir gruba iletimdir. 
	* Örneğin bir radyo yayınını sadece dinlemek isteyen bilgisayarlara göndermek.
* **Broadcast (Genel Yayın):** Aynı yerel ağdaki herkese iletimdir. 

> 📝 **NOT**
> 
> **Router**, broadcast trafiğini geçirmez.


## Protokoller
Her protokolün işlevi, biçimi ve kuralları vardır.

### Protokol Tipleri
* **Ağ İletişim Protokolleri:** 
	* PC'den server'a giderken kullanılan protokollerdir. 
	* Örneğin: Ethernet, IP, TCP, HTTP vb.
* **Ağ Güvenliği Protokolleri:** 
	* Kimlik doğrulama, veri bütünlüğü (integrity) ve veri şifreleme (encryption) için kullanılır. 
	* Örneğin: TLS, SSL, SSH vb.
* **Yönlendirme (Routing) Protokolleri:** 
	* Router'ların birbirlerinden yolları öğrenmesi içindir ("Bende NetA var, bende NetB var" tarzı). 
	* Örneğin: OSPF, BGP, RIP, EIGRP vb.
* **Servis Bulma Protokolleri:** 
	* Cihazların veya servislerin otomatik olarak algılanması için kullanılır.
	* Örneğin: DHCP, DNS vb.

### Protokol Kümeleri
Veri haberleşmesinin ilk dönemlerinde herkes kendi protokol kümesini oluşturmuştur (1983 Novell Netware SPX/IPX, 1985 Apple AppleTalk, 1980 DoD TCP/IP).
* **Sorun:** Farklı cihazlar birbiriyle konuşamıyordu.
* **Çözüm:** Hepsi açık standart olan TCP/IP'ye geçiş yaptı.

TCP/IP Protokol Örneği (Web Sayfası Açılırken):
* **Application:** HTTP
* **Transport:** TCP
* **Internet:** IP
* **Network Access:** Ethernet


## Referans Modelleri
### OSI Modeli (Open Systems Interconnection)
Protokollerin sınırları bellidir. Genel olarak ağ iletişimini modellediğinden herhangi bir protokol mimarisini (örn: TCP/IP) tanımlayabilir.
* **Katmanlı Modelin Faydaları:** Protokol tasarımına yardım eder, bir katmanda sorun olursa diğerleri etkilenmez, rekabetçi ürünler geliştirilir, ortak dil sayesinde tüm cihazlar haberleşebilir.

**OSI Katmanları:**
* **L7 - Application:** 
	* Son kullanıcıya arayüz sağlar.
	* Örneğin: Firefox.
* **L6 - Presentation:** 
	* Data formatı (HTML, JPG, PDF vb.), 
	* Sıkıştırma (Compression) (.gzip),
	* Encryption.
* **L5 - Session:** 
	* İstemci ve sunucu arasındaki oturum yönetimi 
	* Örneğin: Tarayıcıda farklı sekmelerde aynı oturumun açık kalması.
* **L4 - Transport:** 
	* Datayı küçük parçalara böler (Segmentation). 
	* Kaynak ve hedef Port numaraları, Sequence Number (Sıra no) ve Ack Number eklenir. Transport Header eklenir.
* **L3 - Network:** 
	* IP adresleri eklenir, Packet Header eklenir. 
* **L2 - Data Link:**
	* MAC adresleri eklenir, Frame Header ve Trailer eklenir. 
	* Hata kontrolü yapılır. 
	* L1 ve L2 işlemleri donanımsal olarak NIC üzerinde yapılır.
- **L1 - Physical:** 
	* Bitlerin iletimi.


> 🎯 **İPUCU**
> 
> Akılda tutmak için: **Please Do Not Throw Sausage Pizza Away**

![Pasted image 20260425002242.png](/images/Pasted%20image%2020260425002242.png)
**Encapsulation:**
* L7-6-5'te, uygulama datası oluşur.
* L4 datayı parçalara böler, Segment Header ekler.
* L3 Packet Header ve IP adresini ekler.
* L2 Frame Header ve Trailer ekler.
* L1 bitlerin iletimini yapar.

**De-Encapsulation:**
- Alıcıda ise L1'den L7'ye çıkarken Header'lar atılır, 
- L4'ten sonra ilgili port numarasından uygulama katmanına çıkar

#### Encapsulation Örnekleri
![Pasted image 20260425005030.png](/images/Pasted%20image%2020260425005030.png)
* **İç Ağda A'dan B'ye Paket Gönderildiğinde:** 
	* İlgili başlıklara ek olarak: 
		- s.port, d.port, sec no, ack no eklenir.
		* s.ip: ipA, d.ip: ipB
		- s.mac: macA, d.mac MacB
	* Switch paketi alır (L1), L2 başlığına bakar, MAC tablosundan hedef MAC'in (macB) bulunduğu porta paketi yollar.
* **Dış Ağdaki Server'a Paket Gönderildiğinde:** 
	* İlgili başlıklara ek olarak: 
		* s.port, d.port, sec no, ack no eklenir.
		* s.ip: ipA, d.ip: ipServer
	* Hedef MAC adresi olarak aradaki Router'ın (def. gw) MAC adresi yazılır. 
		* s.mac: macA, d.mac macROUTER
	* Switch paketi Router'a yollar. 
	* Router paketi alır, hedefin IP adresine bakar ve en uygun yolu seçer. 
	* Eski L2 başlığını atıp yeni bir L2 başlığı ekler.
		* s.mac: Router, d.mac: Server
	* Ve paketi iletir.

### TCP/IP Modeli
Günümüzde internet haberleşmesinde kullanılan modeldir. 
Katman numaraları kullanılmaz.
![Pasted image 20260425004535.png](/images/Pasted%20image%2020260425004535.png)
1. **Application:** 
	- OSI'nin L7, L6, L5 katmanlarını tek katmanda birleştirir.
2. **Transport:** TCP veya UDP protokolleri kullanılır.
    * **TCP:** Garantili ve eksiksiz teslimat sağlar. Sıra numarası (Seq No) verir.
    * **UDP:** Hızlı ama güvensiz iletimdir. Sıra numarası vermez.
3. **Internet:** 
	- IP adresleri ile paketleri ağa yönlendirir.
4. **Network Access:** 
	- Ağ ortamına erişimi sağlar (Ethernet, WLAN).

### OSI ve TCP/IP Karşılaştırmalı Görsel
![Pasted image 20260425004429.png](/images/Pasted%20image%2020260425004429.png)

## Veri Kapsülleme Detayları
* **Segmentation (Bölümleme):** 
	* Mesajları daha küçük birimlere ayırma işlemidir. 
	* İletişim hızını artırır ve hatada yalnızca hedefe ulaşamayan küçük parçanın yeniden iletilmesini sağlar. 
	* TCP bu segmentlerin sıralanmasından sorumludur.
* **Multiplexing (Çoklama):** 
	* Birden fazla veri akışının (Video, Web, E-posta) aynı iletim ortamından eşzamanlı taşınmasıdır.

### PDU (Protocol Data Unit)
Katman datasının aldığı özel isimlerdir:
* **L7, L6, L5:** Data
* **L4:** 
	* TCP: Segment
	* UDP: Datagram
* **L3:** Packet
* **L2:** Frame
* **L1:** Bit


## Standart Organizasyonları
Açık standartlar; birlikte çalışabilirliği, rekabeti ve yeniliği teşvik eder. Standart organizasyonları satıcıdan bağımsız ve kâr amacı gütmeyen kuruluşlardır.

### İnternet Standartları

![Pasted image 20260425000427.png](/images/Pasted%20image%2020260425000427.png)
* **ISOC (Internet Society):** 
	* İnternetin açık gelişimini destekler.
* **IAB (Internet Architecture Board):** 
	* Standartların yönetiminden sorumludur. 
	* Mühendislerden oluşur, networkler arası büyük sorun olduğunda ISS'lere destek verebilir.
* **IETF (Internet Engineering Task Force):** 
	* TCP/IP teknolojilerini geliştirir, günceller. 
	* Çalışmalarını RFC (Request for Comments) olarak yayınlar.
* **IRTF (Internet Research Task Force):** 
	* İnternet ve TCP/IP protokolleri ile ilgili uzun vadeli araştırmalara odaklanır.

![Pasted image 20260425000524.png](/images/Pasted%20image%2020260425000524.png)
* **ICANN (Internet Corporation for Assigned Names and Numbers):** 
	* IP adresi, port numaraları tahsisini ve domain name yönetimini koordine eder.
* **IANA (Internet Assigned Numbers Authority):** 
	* ICANN için bu yönetimleri denetler. 

### Elektronik ve İletişim Standartları
* **IEEE:** 
	* Elektrik ve elektronik standartlarını belirler.
	* Örneğin: IEEE 802.3 Ethernet, IEEE 802.11 WLAN.
* **EIA/TIA:** 
	* Kablolama standartlarını belirler.
	* Örneğin: EIA/TIA-568A, 568B
* **ITU-T:** 
	* DSL standartlarını belirler.


## Kaynaklar
- Cisco Netacad
- Ağ Yöneticileri Derneği (**AYD**)