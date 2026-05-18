---
title: "CCNA Notlarım | Bölüm 4 - L2 Data Link Katmanı: MAC Algoritmaları, Topolojiler ve Frame Yapısı"
date: 2026-05-18
draft: false
summary: Data Link katmanının işlevlerini ve ağ topolojilerini inceliyoruz. MAC algoritmaları (CSMA/CD, CSMA/CA) ve L2 çerçeve (frame) yapısı hakkında temel bilgileri içeriyor.
tags:
  - CCNA
categories:
  - Networking
cover:
  image: <image path/url>
  alt: <alt text>
  caption: <text>
  relative: false
  hidden: true
---
---
Selamlar. [Bir önceki bölümde](/posts/bolum-3-l1-fiziksel-katman/) verilerin fiziksel ortamda nasıl taşındığına bakmıştık. 
Bu bölümde Data Link (L2) katmanına geçiyoruz. Ağ cihazlarının ortamı nasıl paylaştığını, fiziksel ve mantıksal topolojileri, MAC algoritmalarını ve verinin bu katmanda nasıl paketlendiğini (frame) inceliyoruz.
İyi okumalar.

## Data Link Katmanının Amacı
Data Link katmanı emel görevleri:
- Üst katman protokollerinin fiziksel katmana erişmesine izin verir.
- Network katmanından (L3) gelen paketleri alıp 2. Katman **Frame** yapısını oluşturur, uygun başlık (header) ve kuyruk (trailer) bilgisini ekler.
- Kuyrukta **Hata Tespiti (FCS - Frame Check Sequence)** yapar. Eğer bir hata olmuşsa bozuk çerçeveyi (frame) çöpe atar.
- **Media Access Control (MAC)** ile fiziksel ortama geçişi kontrol eder. Hangi cihazın paketi göndereceği, kimin bekleyeceği vs gibi. (trafik polisi gibi.)

## Data Link Alt Katmanları
 L2 iki alt katmandan oluşur:
![388](/images/Pasted%20image%2020260426174259.png)
1. **LLC Sublayer (Logical Link Control - IEEE 802.2):** 
	- Üst katmanda (L3-Network) hangi protokolün kullanıldığını belirtmek için kullanılır.
	- Network katmanındaki adresler mantıksal (Logical) adrestir. Adını buradan alır.
	- Günümüzde Ethernet başlığındaki Type alanı da aynı işi yaptığından ayrıca LLC başlığı eklenmez.
2. **MAC Sublayer (Media Access Control):** 
	- L1'e geçişi sağlayan ara katmandır. 
	- Veri kapsülleme (MAC adreslemesi ve hata kontrolü) ve fiziksel ortam erişim kontrolünü (MAC Algoritması) yönetir.


> ⚠️ **UYARI**
> 
> MAC Adresi ile MAC Algoritması farklıdır.


> 💡 **BİLGİ**
> 
> Katman 3 (L3) IP adresleri, paketin kaynaktan son hedefe gitmesini sağlayan **Mantıksal Adreslerdir**. 
> Katman 2 (L2) MAC adresleri ise paketin **aynı ağ (network) içinde**, bir NIC'ten diğer bir NIC'e gitmesini sağlayan **Fiziksel Adreslerdir**.



## Topolojiler

Topoloji, bir ağın (network) haritasıdır. İkiye ayrılır:
1. **Fiziksel Topoloji:** 
   ![411](/images/Pasted%20image%2020260426180622.png)
	- Cihazların bulunduğu oda, kabinet (rack) veya kablolama yapısı gibi fiziksel kurulumu gösterir.
2. **Mantıksal Topoloji:** 
   ![437](/images/Pasted%20image%2020260426180607.png)
	- Cihazların IP adresleri, ait oldukları Subnet veya VLAN yapıları gibi mantıksal ağ düzenini gösterir.

### WAN Topolojileri (Router Bazlı)
1. **Point-to-Point:** 
   ![](/images/Pasted%20image%2020260426181742.png)
	- En basit WAN topolojisidir.
	- İki node'u (şube) doğrudan birbirine bağlar. İki node da aynı protokolü kullanmalıdır.
	- Örneğin: iki şubeyi kiralık hat üzerinden birbirine bağlamak.
	- PPP ve HDLC protokolleri p2p bağlantı için kullanılır.
2. **Hub and Spoke:** 
   ![](/images/Pasted%20image%2020260426181748.png)
	- Merkezi bir site (Hub) ve bu merkeze bağlanan şubelerden (Spoke) oluşur.
	- MPLS, FrameRelay, SD-WAN teknolojileri kullanır.
3. **Mesh:** 
   ![](/images/Pasted%20image%2020260426181753.png)
	- Yüksek erişilebilirlik (yedeklilik) için her şubenin diğer tüm şubelere bağlandığı yapıdır. 
	- Daha maliyetlidir.
	- **Full mesh:** Tüm node'lar birbirine bağlanır. 
	- **Partial mesh:** Her node birbirine bağlanmaz, bir node sadece önemli node'lara bağlanır.
	- Full mesh formülü: `n*(n-1)/2`.

### LAN Topolojileri (Endpoint Bazlı)
1. **Bus:** 
   ![](/images/Pasted%20image%2020260426183900.png)
	- Eski Ethernet topolojisidir. 
	- Ethernet ilk çıktığında A'dan B'ye koaksiyel (coaxial) bir kablo geçer, PC'ler o kabloya bağlanır (BNC konektör ile). UTP bile daha yokken.
2. **Star (Yıldız):** 
   ![](/images/Pasted%20image%2020260426183852.png)
	- Merkezde bir Hub veya Switch bulunur, cihazlar merkeze bağlanır.
3. **Extended Star:** 
   ![](/images/Pasted%20image%2020260426183846.png)
	- İki Switch birbirine bağlanır. 
	- Günümüzde Ethernet, star yada extended star olarak çalışır.
	- Hibrit topoloji olarak da bilinir.
4. **Ring (Halka):** 
   ![](/images/Pasted%20image%2020260426183837.png)
	- Eski Token Ring teknolojisidir. 
	- Ağda dönen bir Token vardır. Gönderim yapacak cihaz token'ı alır, verisini ekler. Token tüm cihazları sırayla gezer, verinin gönderildiği cihaz token geldiğinde veriyi okur. Token tekrar gönderen cihaza geldiğinde cihaz veriyi atar ve boş token'i sıradaki cihaza gönderir.
	- Sıralı iletim. herkes sırasını bekler.

#### Ethernet vs Token Ring
- ilk çıktıklarında: Token Ring 16mbps, Ethernet 10mbps ile çalışıyordu.
- Daha sonra hub ve switch cihazları geliştikçe, Ethernet 100mbps ve 1Gbps hızlara ulaşmış.
- Günümüze gelindiğinde, Ethernet bu savaşı kazanmış.



## Half Duplex ve Full Duplex

* **Half-Duplex (Yarı-Çift Yönlü):** 
	* Paylaşılan bir ortamda (Hub, AP), aynı anda sadece bir cihaz veri gönderip alabilir. 
	* Aynı anda bir cihaz  yapılırsa **Collision (Çarpışma)** oluşur ve paket çöp olur. Çarpışmaları engellemek için MAC algoritmalarına (CSMA) ihtiyaç duyulur.
* **Full-Duplex (Tam-Çift Yönlü):** 
	* Transmit (Tx) ve Recieve (Rx) yolları ayrıdır. 
	* Cihaz aynı anda hem veri gönderebilir hem de alabilir. 
	* Ethernet Switch'ler full duplex çalışır ve çarpışma oluşmadığı için özel bir çarpışma tespit algoritmasına ihtiyaç duyulmaz.




## MAC Algoritmaları
2 tür MAC Algoritması vardır:
1. **Controlled Access (Kontrollü Erişim):** 
	- Sıralı iletimdir (Token Ring gibi). 
	- Kimse kimsenin sırasını alamaz.
2. **Contention-based Access (Çekişmeli Erişim):** 
	- Kimsede öncelik yoktur. Hattı boş bulan veriyi gönderir.
	- Ethernette, CSMA/CD kullanılır.
	- WLAN'de, CSMA/CA kullanılır.


### CSMA/CD (Carrier Sense Multiple Access with Collision Detection)
- Eski paylaşımlı Ethernet (Hub) ağlarında kullanılır.
* **Çalışma Mantığı:** Cihaz hattı dinler; boşsa frame'i iletir. İletim sırasında hattı dinlemeye devam eder. 
 - Eğer aynı anda başka bir cihaz da iletim yaparsa **Collision** tespit edilir. 
 * Çarpışma tespit edildiğinde: 
	 * Cihaz veri iletimini hemen keser.
	 * Ağdaki diğer cihazları uyarmak için **Jam (Bozucu) Sinyal** yollar. 
 * Ardından rastgele bir sayaç (Timer) başlatılır. Sayacı ilk biten cihaz hattı dinleyerek tekrar iletime başlar.


### CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)
- Kablosuz ağlarda kullanılır. 
- Kablosuz ortam Half-Duplex çalıştığı için çarpışmaları **önlemek (avoidance)** üzerine kuruludur.
* **Çalışma Mantığı:** 
	* Hattı dinle, hat doluysa bekle.
	- Hat boşsa rastgele bir sayaç (Timer) başlat. (Collision'ı önlemek için sayaç önceden başlatılır.)
	- Sayaç dolunca frame'i ilet. Access Point frame'i alınca ack gönderir.
	- Yani, hatı boş bulan sayaç başlatır önce kiminki dolarsa o frame'ini iletir.
	- 2 sayaçta aynı seçilirse collision oluşur. AP, ack göndermeyeceğinden frame tekrar gönderilir.

* Cihazlar birbirlerinin menzili dışında olabileceğinden daha kontrollü bir yapı geliştirilmiş ve onay paketleri kullanılmış:
  ![](/images/Pasted%20image%2020260426215632.png)
  * Cihaz, Access Point'e (AP) **RTS (Ready to Send - Göndermeye Hazırım)** mesajı yollar.
  * AP uygunsa **CTS (Clear to Send - Gönderebilirsin)** döner.
  * Cihaz ancak CTS aldıktan sonra veriyi yollar ve işlem bitince AP'den ACK (Onay) mesajı bekler.


## Data Link Frame Yapısı
Layer 3 PDU'suna **Frame** denir. Bir Frame 3 ana alandan oluşur:
1. **Başlık (Header)**
2. **Data (Paket)**
3. **Artbilgi (Trailer / Frame Stop)**

### Frame Alanları
![](/images/Pasted%20image%2020260426220812.png)
- **Frame Start/Stop:** Frame'in nerede başlayıp nerede bittiğini tanımlar.
- **Addressing:** Kaynak ve hedef cihazların fiziksel adresleri.
	- Ethernette MAC adresleri kullanılır.
	- P2P teknolojilerde kullanılmaz.
- **Type:** Üst katman protokolü belirtir. (örneğin IPv4 veya IPv6)
- **Control:** Akış kontrolü ve paket önceliklendirme gibi ağ hizmetlerini tanımlar.
	- Örneğin: Router paketleri işleyemedi yavaş ol demek için. 
	- Ethernette yok.
- **Data:** Payload
- **Error Detection:** Hata kontrolü.

> 📝 **NOT**
> 
> Ethernet Bölümünde, Header'ı ve adreslemeyi daha ayrıntılı ele alacağım.

### LAN ve WAN Frame Farkları
Data Link katmanında kullanılan protokol, kullanılan ortama göre değişir.
* **LAN Teknolojileri:** 
	* Frame yapısında yönlendirme için **MAC Adreslerini** kullanır.
	* Örn: IEEE 802.3 Ethernet, IEEE 802.11 WLAN.
* **WAN Teknolojileri:** 
	* PPP (Point-to-Point) gibi kiralık hat bağlantılarında iki nokta arasında başka bir cihaz olmadığı için MAC adresine ihtiyaç duyulmaz. Frame yapısı farklıdır ve adres alanı sadece bağlantı durumunu kontrol eden basit bir bit dizisinden (Örn: 11111111) oluşur.
