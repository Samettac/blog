---
title: Adım Adım Windows Server 2022 Kurulumu ve Active Directory Yapılandırması
date: 2026-05-07
draft: false
summary: Vmware'da Windows Server 2022 Kurulumu ve Active Directory Yapılandırması
tags:
categories:
  - Lab
cover:
  image: <image path/url>
  alt: <alt text>
  caption: <text>
  relative: false
  hidden: true
---
---

Merhaba! Bu yazımda, sıfırdan Windows Server 2022 kurulumunu ve temel yapılandırma adımlarını adım adım anlatıyorum.

VMware üzerinde sanal makinemizi oluşturduktan sonra sunucumuzu bir Domain Controller'a dönüştürerek Active Directory (AD DS), DNS ve Web Server (IIS) rollerini kuracağız. Kendi test ortamınızı kurmak için hazırsanız, hemen başlayalım!

## Windows Server 2022 Kurulumu

Öncelikle aşağıdaki adresten isoyu indirdim. 
https://www.microsoft.com/en-us/evalcenter/download-windows-server-2022
![Pasted image 20260507171517.png](/images/Pasted%20image%2020260507171517.png)

Vmware üzerinden "Create a New Vm" diyorum.
	![Pasted image 20260507171642.png](/images/Pasted%20image%2020260507171642.png)

Açılan pencereden typical'ı seçip next diyorum.
	![Pasted image 20260507171747.png](/images/Pasted%20image%2020260507171747.png)

Bir sonraki pencerede iso dosyasını seçip next diyorum.
	![Pasted image 20260507171744.png](/images/Pasted%20image%2020260507171744.png)

Username yazıyorum ve version olarak Datacenter seçip next diyorum.
	![Pasted image 20260507171850.png](/images/Pasted%20image%2020260507171850.png)
- diğer kısımları boş bırakıyorum.

Verdiği uyarıya yes deyip next, next diyerek kurulumu tamamlıyorum.
	![Pasted image 20260507171855.png](/images/Pasted%20image%2020260507171855.png)

Kuruluma başlamadan hata veriyor. ok deyip vm'i kapatıyorum.
	![Pasted image 20260507171945.png](/images/Pasted%20image%2020260507171945.png)

Edit vm settings altından floppy'ye tıklayıp "connect at power on" özelliğini kapatıyorum.
	![Pasted image 20260507172204.png](/images/Pasted%20image%2020260507172204.png)

Vm'i yeniden açıyorum. Bu sefer kurulum ekranı geliyor. Klavyeyi "Turkish Q" yapıp next diyorum. Daha sonra install now'a tıklıyorum.
	![Pasted image 20260507172307.png](/images/Pasted%20image%2020260507172307.png)

Daha sonra "Windows Server 2022 Standard Evaluation (Desktop Experience)" seçip next diyorum.
	![Pasted image 20260507172505.png](/images/Pasted%20image%2020260507172505.png)

Şartları kabul edip next diyorum.
	![Pasted image 20260507172533.png](/images/Pasted%20image%2020260507172533.png)

Açılan pencereden custom'u seçiyorum.
![Pasted image 20260507172632.png](/images/Pasted%20image%2020260507172632.png)

Daha sonra next next diyerek kurulumu tamamlıyorum.

Yeniden başlattıktan sonra şifre belirlememi istiyor, şifreyi yazıp finish diyorum.
	![Pasted image 20260507214144.png](/images/Pasted%20image%2020260507214144.png)

Bu aşamada kurulum tamamlandı ama ekran kilidini açmak için ctrl+alt+del tuşlarına basmamı istiyor.
Vm menüsünden send ctrl+alt+del'e tıklıyorum ve ekran kilidi açılınca az önce belirlediğim şifreyi giriyorum.
	![Pasted image 20260507173547.png](/images/Pasted%20image%2020260507173547.png)

Ve Windows server açılıyor.
	![Pasted image 20260507173644.png](/images/Pasted%20image%2020260507173644.png)


### AD için Yapılması gereken Konfigürasyonlar
Sunucunun Domain Controller (DC) olması için yapılması gereken bazı ayarlar var önce onları yapmamız gerekiyor.
1. Statik ip verilmesi gerek.
2. Hostname verilmesi gerek.
3. Tüm güncellemelerin yapılması gerek.

Her şeyden önce masaüstü ikonlarını getirmek istiyorum.
- Sağ tık > Personalize
  ![Pasted image 20260507205314.png](/images/Pasted%20image%2020260507205314.png)

- Themes > Desktop icon settings'e tıkıyorum
  ![Pasted image 20260507205306.png](/images/Pasted%20image%2020260507205306.png)

- Açılan penceredeki desktop icon altından hepsini seçiyorum.
  ![Pasted image 20260507205615.png](/images/Pasted%20image%2020260507205615.png)


#### Statik IP Vermek
Ağ ayarlarından > Ethernet > Proporities > İnternet Protocol Version 4 altından ip'mi veriyorum.
![Pasted image 20260507210222.png](/images/Pasted%20image%2020260507210222.png)
- Daha sonra AD kurulumu sırasında dns server da kurulacağından dns server olarak kendisini verdim.

cmd'den baktığımda da değiştiğini gördüm.
`ipconfig /all`
	![Pasted image 20260507210551.png](/images/Pasted%20image%2020260507210551.png)

#### Host Name Vermek
AD kurmadan önce bi diğer yapmamız gereken şey hostname vermek.
- This pc'ye sağ tıklayıp properties'e tıklıyorum.
- Açılan pencerede Rename this PC'ye tıklayıp yeni hostname'i girip yeniden başlatıyorum.
  ![Pasted image 20260507210957.png](/images/Pasted%20image%2020260507210957.png)


#### Server'ı Güncelleme
Son olarak update'leri yapmamız gerekiyor.
- Windows update altından güncellemeleri yapıp yeniden başlatıyorum.
  ![Pasted image 20260507211452.png](/images/Pasted%20image%2020260507211452.png)


## AD Kurulumu

İlk olarak, Server Managerdaki Add roles and feaures tuşuna basıyorum.
	![Pasted image 20260508000325.png](/images/Pasted%20image%2020260508000325.png)

Açılan pencerede kurulum öncesi yapılması gerekenleri söylüyor, daha zaten yaptım için next diyorum.
	![Pasted image 20260508000539.png](/images/Pasted%20image%2020260508000539.png)

İnstalation Type olarak 1. seçeneği (Role based) seçip next diyorum.
	![Pasted image 20260508000650.png](/images/Pasted%20image%2020260508000650.png)

Daha sonra Server pool'dan şuanki server'ı seçip next diyorum.
	![Pasted image 20260508000645.png](/images/Pasted%20image%2020260508000645.png)

Sonraki sayfada server'a kurulacak rolleri seçiyorum.
- Active Directory Domain Services
- DNS Server
- Web Server
Bir özelliği seçtikten sonra açılan pencerede add features diyorum.
Bu şekilde 3'ünüde seçip next diyorum.
	![Pasted image 20260508001130.png](/images/Pasted%20image%2020260508001130.png)

Daha sonraki sayfalarda her hangi bir ayarı değiştirmeden next next diyorum.

Son sayfada install deyip kurulumun tamamlanmasını bekliyorum.
	![Pasted image 20260508001538.png](/images/Pasted%20image%2020260508001538.png)

Yükleme tamamlanınca ilgili sayfayı close diyip kapatıyorum ve server'ı restart ediyorum.
	![Pasted image 20260508001848.png](/images/Pasted%20image%2020260508001848.png)

Server yeniden başlayınca Server managerda sağ üstteki ünlem işareti olan bayrak ikonuna tıklıyorum ve açılan menüden "Promote this server to a domai controller'a" tıklıyorum.
	![Pasted image 20260508002400.png](/images/Pasted%20image%2020260508002400.png)

Açılan pencerede yeni bir AD kurduğumuz için "Add a new forest" deyip domain name'imi yazıp next dedim.
	![Pasted image 20260508002522.png](/images/Pasted%20image%2020260508002522.png)

Sonraki sayfada kurtarma parolamı belirleyip next diyorum.
	![Pasted image 20260508002942.png](/images/Pasted%20image%2020260508002942.png)

Daha sonraki sayfalarda herhangi bir şey değiştirmeden next next diyerek son sayfaya geliyorum.
Burada sarı uyarıları dikkate almıyorum ve install diyorum.
	![Pasted image 20260508003203.png](/images/Pasted%20image%2020260508003203.png)

Yeniden başlattıktan sonra login ekranında domain name'ini görüyorum.
	![Pasted image 20260508003706.png](/images/Pasted%20image%2020260508003706.png)

Server Managerda ise kurduğum özellikler gelmiş.
	![Pasted image 20260508003832.png](/images/Pasted%20image%2020260508003832.png)


## Sonuç

Tebrikler! kurulumu başarıyla tamamladık. Artık kullanıcıları, grupları ve bilgisayarları merkezi olarak yönetebileceğimiz bir Domain Controller sunucusuna sahibiz.

Gelecek yazılarda görüşmek üzere!



