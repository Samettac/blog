---
title: Adım Adım Windows 10'u Domain'e Ekleme ve AD Kullanıcısı Oluşturma
date: 2026-05-14
draft: false
summary: Bu yazıda, DNS yapılandırmasını tamamlayarak bir Windows cihazını Active Directory domain'ine nasıl dahil edeceğimizi adım adım inceliyoruz. Ayrıca AD üzerinde yeni bir kullanıcı oluşturup yetkilendirerek, bu hesapla bilgisayarımızda nasıl oturum açacağımızı da detaylarıyla görebilirsiniz.
tags:
  - Active-Directory
categories:
  - Home Lab
cover:
  image: <image path/url>
  alt: <alt text>
  caption: <text>
  relative: false
  hidden: true
---
---
Selam. [Bir önceki yazımızda](/posts/windows-server-2022-ve-ad-kurma/) Windows Server kurulumunu ve Active Directory yapılandırmasını tamamlamıştık. Şimdi sıra bu yapıya bir Windows Client cihazı dahil etmekte.

Bu rehberde, Domain Controller (DC) sunucumuz üzerinde DNS Reverse Lookup Zone oluşturarak başlayacağız. Ardından, Windows client makinemizin DNS ayarlarını yapılandırıp , cihazımızı domain'e bağlayacağız. Ayrıca bir de Kullanıcı hesabı oluşturacağız.
İyi Okumalar.

## Active Directory DNS Kurulumu

Öncelikle Domain Controller sunucumuzda Server Manager'ı açıyorum ve Tools menüsünden DNS'e tıklıyorum.
![Pasted image 20260509202225.png](/images/Pasted%20image%2020260509202225.png)

Forward lookup zaten kayıtlı olduğu için herhangi bir şey yapmıyorum.
![Pasted image 20260509202342.png](/images/Pasted%20image%2020260509202342.png)

Ama Reverse lookup zone olmadığı için "Reverse Lookup Zones" klasörünün üzerine sağ tıklayıp "New Zone" diyorum.
![Pasted image 20260509202454.png](/images/Pasted%20image%2020260509202454.png)

Açılan kurulum sihirbazında next next diyerek ilerliyorum.
![Pasted image 20260509202536.png](/images/Pasted%20image%2020260509202536.png)

![Pasted image 20260509202603.png](/images/Pasted%20image%2020260509202603.png)

![Pasted image 20260509202637.png](/images/Pasted%20image%2020260509202637.png)

![Pasted image 20260509202640.png](/images/Pasted%20image%2020260509202640.png)

Bu kısımda server'ımın ip adresinin ilk 3 oktetini yani network adresimi gireceğim. Network adresini girince reverse lookup zone name kendiliğinden otomatik olarak doluyor. İşim bitince next diyorum
![Pasted image 20260509202940.png](/images/Pasted%20image%2020260509202940.png)

Kurulum tamamlanıyor ve reverse lookup zone'a server'ım ekleniyor.
![Pasted image 20260509202944.png](/images/Pasted%20image%2020260509202944.png)



## Windows'u AD'ye Bağlama

### Hostname Değiştirme
İlk olarak  hostname'i değiştirmek istiyorum.
Bu bilgisayar'a sağ tıklayıp özellikler diyorum ve açılan pencereden ayarları değiştire tıklıyorum.
![Pasted image 20260509203422.png](/images/Pasted%20image%2020260509203422.png)

Açılan pencereden değiştire tıklıyorum.
![Pasted image 20260509203456.png](/images/Pasted%20image%2020260509203456.png)

Daha sonra açılan pencerede "Bilgisayar Adı" kısmına yeni hostname'ini giriyorum. Tamam'a tıklıyorum ve bilgisayarı yeniden başlatıyor.
![Pasted image 20260509203609.png](/images/Pasted%20image%2020260509203609.png)

Yeniden başladıktan sonra Bu bilgisayar'a sağ tıklayıp özelliklerden hostname'i kontrol ediyorum. Ve işlem tamam.
![Pasted image 20260509204218.png](/images/Pasted%20image%2020260509204218.png)

### Windows Client'da DNS Server Ayarı

İlk olarak windows'tan domain controller'a ping atıyorum.
![Pasted image 20260509204425.png](/images/Pasted%20image%2020260509204425.png)
- ping'e cevap alabiliyorum. herhangi bir sorun yok.

> 📝 **NOT**
> 
>Windows host'um ve Domain Controller server'ım farklı subnetteler. Arada bir Fortigate firewall var. İlerleyen bölümlerde Fortigate ile ilgili de yazılar yayınlayacağım.

Ping'de sorun olmadığına göre bilgisayarımın dns server'ına dc'nin ip'sini veriyorum.
![Pasted image 20260509204628.png](/images/Pasted%20image%2020260509204628.png)

DNS server'ı ekledikten sonra dc'ye domain adresinden ping atmayı deniyorum.
![Pasted image 20260509205134.png](/images/Pasted%20image%2020260509205134.png)
- Herhangi bir sorun olmadan ping'e cevap alabildim.

### PC'yi Domain'e Ekleme

İlk olarak hostname'i değiştirdiğimiz yerden domain name'imi yazıp tamam diyorum.
![Pasted image 20260509205422.png](/images/Pasted%20image%2020260509205422.png)

Daha sonra ilgili domain'den yetkili bir user'ın bilgilerini istiyor. Administrator ile giriş yapıyorum.
![Pasted image 20260509205533.png](/images/Pasted%20image%2020260509205533.png)

Domain'e hoşgeldin mesajı veriyor. Tamam diyorum ve yeniden başlıyor.
![Pasted image 20260509205538.png](/images/Pasted%20image%2020260509205538.png)

Server'da "Active Directory Users and Computers" penceresinden "Computers'a" baktığımda az önce eklediğim makineyi görüyorum.  
![Pasted image 20260509205657.png](/images/Pasted%20image%2020260509205657.png)

### Active Directory User Oluşturma

Cihazı AD'ye ekledim bir de user oluşturmak istiyorum.
Users'a sağ tık > new > User
![Pasted image 20260509210911.png](/images/Pasted%20image%2020260509210911.png)

Açılan pencerede oluşturacağım kullanıcının bilgilerini yazıp next diyorum.
![Pasted image 20260509210942.png](/images/Pasted%20image%2020260509210942.png)
- First name, last name doldurunca full name'i kendisi dolduruyor.
- User logon name: Giriş yaparken kullanılacak kullanıcı adı.

Şifre belirliyorum.
![Pasted image 20260509211044.png](/images/Pasted%20image%2020260509211044.png)
- User change must password at next logon: Kullanıcının belirtilen bu şifreyle giriş yaptıktan sonra şifresini değiştirmesini zorunlu kılar. VM olduğu için bunu açmıyorum.
- Password never expires: Belirlediğim şifre süresiz geçerli olur. Vm olduğu için bunu açtım.

Next next diyerek kurulumu bitiriyorum.

Kullanıcı oluştuktan sonra çift tıklayıp açılan pencerede "Member of" sekmesinde kullanıcıyı bir gruba dahil edeceğim.
![Pasted image 20260509211420.png](/images/Pasted%20image%2020260509211420.png)
- Add diyorum.

Açılan pencerede Advanced'e tıklıyorum
![Pasted image 20260509211424.png](/images/Pasted%20image%2020260509211424.png)

Find now'a tıklıyorum ve domain'deki tüm kullanıcı grupları gözüküyor. Oluşturduğum kullanıcının Admin yetkilerine sahip olması için "Domain Admin" grubunu seçip tamam diyerek çıkıyorum.
![Pasted image 20260509211539.png](/images/Pasted%20image%2020260509211539.png)

Her şey tamamlandı artık windows makineme domaindeki yeni oluşturduğum kullanıcıyla giriş yapabilirim.
![Pasted image 20260509205757.png](/images/Pasted%20image%2020260509205757.png)
- Other user seçiyorum ve kullanıcı adımı `DomainName\username` formatında giriyorum. 


## Sonuç

Bilgisayarımızın adını değiştirdik , domain'e başarıyla dahil ettik ve Active Directory üzerinde oluşturduğumuz "Domain Admins" yetkisine sahip kullanıcımızla oturum açtık. Artık client makinemiz tamamen Domain Controller'ın yönetimi altında.

Yazı içerisinde de belirttiğim gibi, bu yapıda subnet'ler arası iletişimi sağlayan bir Fortigate firewall bulunuyor. İlerleyen yazılarımda bu Fortigate yapılandırmasının detaylarına, kurallarımıza ve güvenlik politikalarına da değineceğim. Bir sonraki rehberde görüşmek üzere!

