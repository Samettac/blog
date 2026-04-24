---
title: Bölüm 1 - Günümüzde Ağlar
date: 2026-04-24
draft: false
summary: günümüzdeki ağ yapıları, modelleri, cihazları hakkında.
tags:
  - CCNA
  - "#network"
cover:
  image: <image path/url>
  alt: <alt text>
  caption: <text>
  relative: false
  hidden: true
---
---
## Ağın Gelişimi

Dünyamızdaki dijital dönüşüm, ağ teknolojilerinin evrimiyle doğrudan ilişkilidir:
![Pasted image 20260424185907.png](/images/Pasted%20image%2020260424185907.png)
**Kaynak:** https://www.researchgate.net/publication/279068905_Next_Generation_M2M_Cellular_Networks_Challenges_and_Practical_Considerations

1. **Web 1.0 (HTTP/WWW):** Statik içerik dönemi.
2. **Web 2.0 (İnternet 2.0):** Etkileşimli ve sosyal içerik.
3. **Mobil Cihazlar:** Her yerden erişim.
4. **IoT (Nesnelerin İnterneti):** Akıllı cihazların ağa dahil olması.
5. **Pandemi Süreci:** Uzaktan çalışma ve eğitimin standartlaşması.


## Network Nedir?
Network (Ağ), iki veya daha fazla cihazın birbiriyle haberleştiği ortamdır.

### Neden Network Kurulur?
Temel amaç, bir tarafın hizmet almak, diğer tarafın ise hizmet vermek istemesidir:
- **Server (Sunucu):** Hizmet veren cihaz.
- **Client (İstemci):** Hizmet alan cihaz.

> 📌 **NOT**
> 
>Eskiden kurumlarda son kullanıcıların hard diski bulunmadığı için veriler merkezi bir "Mainframe" sunucusuna yazılırdı.

### İletişim Modelleri

>Yukarda bahsettiğim model: Client-Server (istemci-sunucu) modelidir.

![Pasted image 20260424215431.png](/images/Pasted%20image%2020260424215431.png)
**Kaynak:** https://systemdesignschool.io/blog/peer-to-peer-architecture

**Peer-to-Peer (P2P):** Cihazların hem istemci hem de sunucu görevi görmesidir. Kurumsal yapılarda merkezi yönetim olmadığı için tercih edilmez ve güvenlik riskleri barındırabilir.
- Örnek: **Torrent**
- ![Pasted image 20260424214711.png](/images/Pasted%20image%2020260424214711.png)

| **Avatajları**                                                               | **Dezavantajları**            |
| ---------------------------------------------------------------------------- | ----------------------------- |
| Kurulumu kolay                                                               | Merkezi yönetim yok           |
| Daha az karmaşık                                                             | Güvenlik riski oluşturabilir. |
| Daha düşük maliyet                                                           | Ölçeklenebilir değil          |
| Basit görevler için kullanılır: dosya aktarma<br>ve yazıcı paylaşımı vs gibi | Daha yavaş performans         |


## Network Bileşenleri

Bir ağı oluşturan üç temel parça vardır: Cihazlar, Medya ve Servisler.

### 1. End Devices (Uç Cihazlar / Host)
Networklerin kurulma amacı olan bu cihazlar hem hizmet alabilir hem de verebilir.
- **Örnekler:** PC, IP Telefon, Sunucu, Yazıcı, El terminali.
- Uç cihazlar, **NIC (Network Interface Card)** sayesinde network'e dahil olur.
- Uç cihazın arkasında (genellikle) bir başka cihaz daha yoktur. 

> 📝 **NOT**
> 
> End device **sadece client** demek **değildir**.

### 2. Intermediary Network Devices (Ara Ağ Cihazları)
Uç cihazları birbirine bağlayan ve veriyi hedefe taşıyan cihazlardır. En temel 2 cihaz: router ve switch'dir. Diğer cihazlar, bunların birer varyantıdır.

1. **Switch:** 
	- ![Pasted image 20260226144708.png](/images/Pasted%20image%2020260226144708.png)
	- ![Pasted image 20260226145029.png](/images/Pasted%20image%2020260226145029.png)
	- Aynı lokasyondaki cihazları kablolu olarak networke bağlar. 
	- Üzerinde bir sürü giriş vardır. Bu girişlere: **interface** ya da **port** denir.
	- Switch'in ilkeli hub'dır. Günümüzde kullanılmaz.
	- Dikdörtgen içinde iki ok ile sembolize edilir.

2. **Access Point:** 
	- ![Pasted image 20260424212516.png](/images/Pasted%20image%2020260424212516.png)
	- Kablosuz cihazları bağlar ve sinyali kablolu ağa aktarır.

3. **Router:** 
	- ![Pasted image 20260226145140.png](/images/Pasted%20image%2020260226145140.png)
	- Farklı networkleri birbirine bağlar ve en iyi yol seçimini yapar. 
	- Daire içinde çapraz ok (X) ile sembolize edilir.

4. **Firewall (Güvenlik Duvarı):** 
	- ![Pasted image 20260226145239.png](/images/Pasted%20image%2020260226145239.png)
	- Temelde Router'ın Güvenlik özellikleri artırılmış hâlidir. Paketleri güvenlik kriterlerine göre filtreler.

5. **Multilayer Switch (L3 Switch):** 
	- ![Pasted image 20260226145304.png](/images/Pasted%20image%2020260226145304.png)
	- Hem Switch hem Router özelliklerini barındıran cihazdır.

### 3. Ağ Ortamı (İletişim Medyası)
Verinin iletildiği fiziksel ortamdır.
- **Bakır Kablo (Copper):** Elektriksel sinyaller (örn: UTP).
- **Fiber Optik:** Işık ile iletim (Single Mode ve Multi Mode).
- **Wireless (Kablosuz):** Elektromanyetik dalgalar.


## Network Türleri

Ağlar coğrafi büyüklüklerine ve sahiplik durumlarına göre ayrılır. En temelde 2 çeşittir: **LAN** ve **WAN**.

### LAN ve WAN
![Pasted image 20260424190042.png](/images/Pasted%20image%2020260424190042.png)
- **Local Area Network (LAN):** 
	- Aynı lokasyondaki (kurum, ev, kampüs) cihazların oluşturduğu ağdır.
- **Wide Area Network (WAN):** 
	- LAN'ları servis sağlayıcılar aracılığıyla birbirine bağlayan geniş ağlardır.

> 📝 **NOT**
> 
> Eğer aradaki arazinin tapusu size aitse mesafe ne olursa olsun bu bir LAN'dır; ancak kamusal alan geçiliyorsa (servis sağlayıcı gerekiyorsa) WAN olur.


### İnternet, İntranet ve Extranet

![Pasted image 20260424190202.png](/images/Pasted%20image%2020260424190202.png)
- **Internet:** Küresel LAN ve WAN koleksiyonudur.
	- ![Pasted image 20260424190128.png](/images/Pasted%20image%2020260424190128.png)
- **Intranet:** Sadece kurum içine açık, internet erişimi olmayan özel ağ.
	- Örneğin, TSK'nın iç ağı **KARANET**.
- **Extranet:** Kurum içi ağın belirli iş ortaklarına özel olarak açılmış hali.
    

## Güvenilir Bir Ağın Temelleri (Ekstra Detaylar)

Ağ tasarımında profesyonel standartları sağlamak için şu dört özellik kritik önem taşır:
1. **Hata Toleransı (Fault Tolerance):** 
	- Bir bileşen arızalandığında ağın çalışmaya devam edebilmesi (Yedeklilik).
2. **Ölçeklenebilirlik (Scalability):** 
	- Mevcut performansı bozmadan ağa yeni kullanıcı ve(ya) cihaz eklenebilmesi.
3. **Hizmet Kalitesi (QoS):** 
	- Ses ve video gibi gecikmeye duyarlı paketlerin önceliklendirilmesi.
4. **Güvenlik (Security):** 
	- Verinin Gizliliği (Confidentiality), Bütünlüğü (Integrity) ve Erişilebilirliğinin (Availability) korunması (CIA Triad).


## Kaynaklar
- Cisco Netacad
- Ağ Yöneticileri Derneği (**AYD**)





