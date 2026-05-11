---
title: CCNA Notlarım | Bölüm 3 - Fiziksel Katman (Layer 1)
date: 2026-05-11
draft: false
summary: Fiziksel katmanda verilerin kablo veya frekanslar üzerinden nasıl iletildiğine bakıyoruz. Bakır kablolar, fiber optik yapıları ve kablosuz ağ bağlantılarının temel özelliklerini inceliyoruz.
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
Selamlar. [İkinci bölümde](/posts/bolum-2---protokoller-ve-modeller/) cihazların nasıl anlaştığını işlemiştik. 

Bu bölümde donanım kısmına, yani Fiziksel Katman'a (L1) geçiyoruz. Verilerin kablolar ve frekanslar üzerinden nasıl iletildiğini, bant genişliğini, bakır ve fiber kablo türlerini inceliyoruz. İyi okumalar.

## Fiziksel Katmanın Amacı
Fiziksel katman (L1); sinyalleşme, bit iletimi, kablolama, kablo sonlandırma (konektörler), arayüz (interface) ve NIC (Network Interface Card) işlemlerinin yapıldığı donanımsal katmandır. 

> 📝 **NOT**
> 
> Data Link Katmanının (L2) yarısından yukarısı yazılımsaldır ve IETF tarafından standartlaştırılır. 
> L2'nin alt kısmı ve L1 ise donanımsaldır; IEEE, ITU-T, EIA/TIA, ISO, ANSI gibi elektronik ve iletişim kurumları tarafından standartlaştırılır.

## Fiziksel Katman Özellikleri

### Kodlama (Encoding)
![354](/images/Pasted%20image%2020260425235741.png)
Bitlerin (0 ve 1) fiziksel ortama nasıl kodlanacağıdır. Bu kodlama, sonraki aygıt tarafından tanınabilir ve öngörülebilir desenler sağlar. 
* Örnek: 10 Mbps Ethernet, **Manchester Encoding** kullanır.

### Sinyalleme (Signaling)
Bit değerlerinin fiziksel ortamda nasıl temsil edildiğidir. Kullanılan ortamın türüne göre değişir:
* **Bakır Kablo:** Elektrik voltajı ile (Örn: +5V = 1, -5V = 0).
	* ![259](/images/Pasted%20image%2020260425235844.png)
* **Fiber Optik:** Işık darbeleri ile (Işık var = 1, Işık yok = 0).
	* ![348](/images/Pasted%20image%2020260425235916.png)
* **Kablosuz (Wireless):** Mikrodalga sinyallerindeki genlik, frekans veya faz değişiklikleri (modülasyon) ile.
	* ![272](/images/Pasted%20image%2020260425235925.png)

### Bant Genişliği ve Hız Kavramları
**Bant Genişliği (Bandwidth):** 1 saniyede iletilen bit sayısıdır. Birimi **bps** (bits per second)'dir. 

> 📝 **NOT**
> 
> Küçük "b" bit, büyük "B" Byte anlamına gelir. 1 Byte = 8 bittir.

| Bant Genişliği Birimi | Kısaltma | Denklik               |
| :-------------------- | :------- | :-------------------- |
| Saniyede bit          | bps      | 1 bps = Temel Birim   |
| Saniyede kilobit      | Kbps     | 1.000 bps             |
| Saniyede megabit      | Mbps     | 1.000.000 bps         |
| Saniyede gigabit      | Gbps     | 1.000.000.000 bps     |
| Saniyede terabit      | Tbps     | 1.000.000.000.000 bps |

**Örnek Hesaplama:** 100 Mbps bant genişliği olan bir hattan 100 MB'lık (Megabyte) bir dosya kaç saniyede iletilir?
* 100 MB = 800 Mb
* 800 Mb / 100 Mbps = 8 saniye. 
* Ham veriye yaklaşık %10 Header eklendiği için pratikte iletim **~9 saniye** sürer.

**Performans Terimleri:**
* **Throughput (Verim):** 
	* Hız testi yapıldığında çıkan anlık değerdir. 
	* Örneğin: İnternet taahhüdünüz 100 Mbps iken hız testinde 95 Mbps çıkması gibi.
* **Goodput:** 
	* Throughput eksi (-) trafik yükü (Header vb.). 95 Mbps throughput'un 3 Mbps'si Header ise Goodput = 92 Mbps'dir.
* **Latency (Gecikme):** 
	* Bir paketin A noktasından B noktasına ulaşması için geçen süredir.



## Bakır Kablolama
Bakır kabloların bazı sınırlamaları vardır:
1. **Zayıflama (Attenuation):** 
	- Belirli bir mesafeden sonra elektrik sinyalleri zayıflar. 
	- Bakır kabloda bu mesafe **100 metredir**. 
2. **EMI (Electromagnetic İnterference) ve RFI (Radio Frequency İnterference):** 
	- Yüksek akım geçen kablolar veya floresan lambalar elektrik sinyallerini bozabilir. 
	- Metalik koruma (Shield) ve topraklama ile bu etki azaltılır.
3. **Crosstalk:** 
	- Aynı kablodaki tellerin kendi aralarında oluşturduğu manyetik alanın birbirini etkilemesidir. 
	- Telleri birbirine bükmek (twisted pairs) crosstalku azaltır.
	- Aynı bükümdeki İki kablonun manyetik alanlarının ters yönlü olup (Tx+/Tx-, Rx+/Rx-) birbirini sönümlemesi (**Cancellation Effect**) de crosstalk'u azaltır.

### Bakır Kablo Çeşitleri
1. **UTP (Unshielded Twisted Pair):**
   ![219](/images/Pasted%20image%2020260426000959.png)
   * En yaygın ağ ortamıdır. 8 tel, 4 bükümden oluşur. 
   * RJ-45 konektörleri ile sonlandırılır.
        ![176](/images/Pasted%20image%2020260426001135.png)
1. **STP / FTP / SFTP (Shielded Twisted Pair):**
   ![204](/images/Pasted%20image%2020260426000947.png)
   * EMI/RFI'den korunmak için dışı veya iç bükümleri folyo ile kaplıdır. 
   * Folyo, dışarıdan gelen manyetik alanı toplar, bu nedenle topraklama yapılması için metal RJ-45 uçlar kullanılır. 
   * Daha pahalı ve kurulumu zordur.
1. **Coaxial (Koaksiyel) Kablo:**
   ![317](/images/Pasted%20image%2020260426000938.png)
   * Günümüzde veri haberleşmesinde çok kullanılmaz (Antenler, Kablo TV ve ev interneti altyapısında görülür). 
   * BNC veya F-tipi konektörler kullanılır.

> 📝 **NOT**
> 
>Günümüzde utp kablo çok sık kullanılır çünkü 100mt kuralına uyulup, kaliteli kablo kullanılıp sonlandırması iyi olduğu sürece herhangi bi sorun yaşanmaz.

## UTP Kablolama Standartları
UTP standartları TIA/EIA (Örn: TIA/EIA-568) tarafından belirlenir. Kabloların kategorisi arttıkça kalitesi ve taşıdığı veri miktarı artar, ancak mesafe genellikle 100 metre olarak sabittir.

* **Kategoriler:** 
	* ![551](/images/Pasted%20image%2020260426001833.png)
	* Cat8 maksimum mesafesi 30 metredir.

> ⚠️ **UYARI**
>  
> Kablolar geriye dönük uyumludur ve altyapı kablolaması her zaman ileriye dönük yapılmalıdır (Cihazları değiştirmek kolaydır ama kablolamayı değiştirmek masraflıdır).

### UTP Renk Standartları (T568A ve T568B)
![](/images/Pasted%20image%2020260426002152.png)
- T568A: 1-YB 2-Y 3-TB 4-M 5-MB 6-T 7-KhB 8-Kh
- T568B: 1-TB 2-T 3-YB 4-M 5-MB 6-Y 7-KhB 8-Kh
- 10 Mbps ve 100 Mbps haberleşmede 8 telin sadece 4'ü data haberleşmesinde kullanılır.
	- 1-Tx+, 2-Tx-, 3-Rx+, 6-Rx-, 
	- 4-5 Telefon
	- 7-8 PoE (Power over Ethernet)
- 1 Gbps'de ise 8 telin tamamı aynı anda hem Tx (Gönderme) hem Rx (Alma) için kullanılır.

### Kablo Türleri
* **Ethernet Düz Kablo (Straight-through):** 
  ![](/images/Pasted%20image%2020260426010630.png)
	* Kablonun iki ucu da aynı standartta (T568A-T568A veya T568B-T568B) sonlandırılır. 
	* Farklı tür cihazları bağlarken kullanılır.
	* Örn: PC -> Switch, Router -> Switch
	* Switch'ler çaprazlamayı (crossing) kendi içinde yapar. Bu özellik port numarasının yanındaki "x" işaretinden anlaşılabilir (1x, 2x). Bu yüzden pc veya Router, switch'e düz kablo ile bağlanır.
* **Ethernet Çapraz Kablo (Crossover):** 
  ![](/images/Pasted%20image%2020260426010637.png)
	* Bir ucu T568A, diğer ucu T568B olarak sonlandırılır. 
	* Aynı tür cihazları bağlarken kullanılır. 
	* Örn: Switch -> Switch, PC -> PC, Router -> Router, Hub -> Hub.
	* İki PC bağlanırken mantıken birinin Tx (gönderici) ucu diğerinin Rx (alıcı) ucuna denk gelmelidir.
	* İki switch neden çapraz kablo ile bağlanır?
		* Örneğin: A'dan giden Tx, sw1'de Rx çıkar. sw2'ye girip tekrar Tx olarak çıkar. 
		* B'ye: Tx, Tx gider. amaç B'ye Tx'i Rx götürmektir.

> 📝 **NOT**
> 
> Günümüzde, **Auto-MDIX** (Media Dependent Interface Crossover) özelliği sayesinde cihaza düz veya çapraz kablo takmanız fark etmez; cihaz portları otomatik olarak kendini ayarlar.

* **Console (Rollover) Kablo:** 
  ![206](/images/Pasted%20image%2020260426010849.png)
	* Ağ cihazlarına (Switch, Router) ilk yapılandırmayı (config) vermek için kullanılır. 
	* Bir ucubir ucu RJ-45, diğer ucu 9 pinli DB-9 seri porttur.
	- RJ-45 ağ cihazına, seri port pc'ye (günümüzde usb çeviriciyle) takılır..


### Yatay ve Dikey Kablolama (Patch Panel)
* **Patch Panel:** 
  ![209](/images/Pasted%20image%2020260426011754.png)
	* Kabloların düzenlenmesi için kullanılır, elektriksel bir cihaz değildir.

![446](/images/Pasted%20image%2020260426011401.png)
- **Yatay Kablolama (Horizontal Cabling):** 
	* Son kullanıcıya (duvar prizlerine) giden kablolamadır. 
	* Duvar içi maksimum 90m + Patch panelden Switch'e 5m + PC'den prize 5m = Toplam Maksimum 100 metredir.
* **Dikey Kablolama (Backbone Cabling):** 
	* Farklı katlar arası, panelden panele veya Switch'ten Router'a yapılan omurga kablolamasıdır.



## Fiber Optik Kablolama
* Verileri çok daha yüksek bant genişliğinde, ışık hızında ($3 \times 10^8 m/sn$) ve uzun mesafelerde taşır.
* Zayıflamaya daha az duyarlıdır ve EMI/RFI'ye karşı **tamamen bağışıktır**.
* SC, ST veya LC tipi konektörlerle sonlandırılır ve SFP (Small Form-factor Pluggable) modüller ile Switch'lere takılır. 
* UTP'den daha maliyetlidir.


### Fiber Kablonun Yapısı
![](/images/Pasted%20image%2020260426012318.png)
- **Core (Çekirdek):** 
	- Işığın taşındığı iç kısımdır.
	- Camdan yapılmıştır.
- **Cladding (Kaplama):** 
	- Çekirdeğin dış katmanıdır ve yine camdan üretilmiştir. 
	- Çekirdekten farklı bir yansıtma katsayısına sahip olması sayesinde ışığın dışarı kaçmasını önleyerek çekirdek içinde kalmasını sağlar. 

### Fiber Kablo Türleri
1. **Single-Mode Fiber (SMF - Tek Modlu):** 
   ![](/images/Pasted%20image%2020260426013221.png)
	- Sarı renklidir. 
	- Core 9 mikron, cladding 125 mikron boyutundadır.
	- Güçlü lazer kaynakları kullanır, ışık düz ilerler. 70 km'ye kadar veri taşıyabilir.
2. **Multimode Fiber (MMF - Çok Modlu):** 
   ![478](/images/Pasted%20image%2020260426013326.png)
	- Turuncu renklidir. 
	- Daha büyük bir core'a (50/62.5 mikron) sahiptir. 
	- Ucuz LED ışık kullanır ve aynı anda birden fazla ışık sinyali taşınabilir.
	- **Dağılım (Dispersion)**, Işığın çarpa çarpa ilerlerken enerjisini kaybetmesi, nedeniyle maksimum kablo mesafesi genelde 550 metredir (10 Gbps hıza kadar).

### Fiber Kullanım Alanları
1. **Kurumsal Ağlar:** Omurga (backbone) kablolama ve cihaz arası bağlantılarda.
2. **Eve Fiber (FTTH / GPON):** Ev ve küçük işletmelere geniş bant sağlamak için.
3. **Uzun Menzilli Ağlar:** ISS'ler tarafından şehirleri ve ülkeleri bağlamak için.
4. **Denizaltı Kablo Ağları:** Okyanus ötesi iletişim için.

#### Ekstra Bilgiler:
- 70 km'nin üzerindeki mesafelerde araya **tekrarlayıcı (repeater)** ve **kuvvetlendirici** cihazlar konulur.
- Fiber çekilirken en az **2 Core** (1 Transmit, 1 Receive) yeterlidir. Ama kazı ve işçilik maliyetleri daha yüksek olduğu için genellikle ihtiyaçtan çok daha fazla core içeren (Örn: 24, 48, 72 core) kablolar çekilir.
- Fiber Patch panele gelen kalın kablo core'lara ayrılıp, _füzyon teknolojisi_ ile pigtail/patch kabloyla birleştirilir.
- Switch'teki boş yerlere. uygun sfp (small form pluggable) modülü alınıp takılır (burda fiber sfp).
	- sfp/1Gbps, sfp+/10Gbps

## UTP vs Fiber

| **Özellik**                              | **UTP Kablo**                                | **Fiber Optik Kablo**                         |
| ---------------------------------------- | -------------------------------------------- | --------------------------------------------- |
| **Bant Genişliği**                       | 10 Mb/s - 10 Gb/s                            | 10 Mb/s - 100 Gb/s                            |
| **Mesafe**                               | Görece kısa (1 - 100 metre)                  | Görece uzun (1 - 100.000 metre)               |
| **EMI ve RFI Bağışıklığı**               | Düşük (Elektromanyetik girişimden etkilenir) | Yüksek (Hiç etkilenmez)                       |
| **Elektriksel Tehlikeler'den Etkilenme** | Yüksek                                       | Düşük (Tamamen yalıtkandır)                   |
| **Maliyet**                              | En düşük                                     | Yüksek                                        |
| **Kurulum Zorluğu**                      | En düşük                                     | Yüksek (Uzmanlık ve özel cihazlar gerektirir) |

## Kablosuz Medya (WLAN)
Radyo veya mikrodalga frekansları kullanılarak haberleşme yapılır. Access Point (AP) ve Kablosuz NIC'ler ile bağlantı sağlanır.

**Kablosuz Bağlantı Sınırlamaları:**
* **Kapsama Alanı:** 
	* Engellere göre değişir. Açık alanda genellikle 70 metre civarıdır.
* **Girişim (Interference):** 
	* örneğin: 2 AP aynı kanaldan yayın yaparsa girişim olur.
* **Güvenlik:** 
	* Dışardan biri gelip paketleri dinleyebilir.
* **Paylaşılan Ortam:** 
	* Temelde WLAN'lar Half-Duplex çalışır. Aynı anda sadece bir aygıt veri gönderip alabilir (Collision olmaması için). 
	* Ağa çok kişi bağlanırsa bant genişliği bölünür.

**Kablosuz Standartlar:**
* **Wi-Fi (IEEE 802.11):** 
	- **Wifi Alliance:** ieee802.11 demek yerine wlan adlandırması yapar. örn: wifi 6, wifi 5 gibi.
* **Bluetooth (IEEE 802.15):** 
	* PAN (Kişisel Alan Ağı) standardı.
* **WiMAX (IEEE 802.16):** 
	* Geniş bant noktadan çok noktaya erişim.
* **Zigbee (IEEE 802.15.4):** 
	* IoT (Nesnelerin İnterneti) için düşük hızlı ve düşük güç tüketimli sensör ağı.

