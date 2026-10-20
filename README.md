# VASHLEe Crypt

**VASHLEe Crypt**, Python ile geliştirilmiş; dosya şifreleme ve parola yönetimi özelliklerini bir araya getiren masaüstü uygulamasıdır. Dosyaları şifrelemek için Fernet simetrik şifreleme algoritmasını kullanır.

## Özellikler

- **Dosya Şifreleme:** Uygulamanın depolama klasöründeki dosyaları şifreler.
- **Dosya Şifre Çözme:** Doğru şifreleme anahtarıyla dosyaların şifresini çözer.
- **Parola Yöneticisi:** Başlık, e-posta veya kullanıcı adı, parola ve açıklama bilgilerini kaydetmeyi sağlar.
- **Anahtar Oluşturma:** İlk kurulumda Fernet şifreleme anahtarı oluşturur.
- **Panoya Kopyalama:** Oluşturulan şifreleme anahtarını panoya kopyalar.
- **Dosya Yöneticisi:** Uygulamanın depolama klasörünü doğrudan açar.
- **Anahtar Kontrolü:** Uygulamanın ana ekranına erişmeden önce şifreleme anahtarını ister.

## Proje Bilgileri

- **Proje Adı:** VASHLEe Crypt
- **Proje Başlangıç Yılı:** 2023
- **Geliştirici:** Nyoxs
- **Yayınlanma Tarihi:** 23.02.2026
- **GitHub:** [NYOXS](https://github.com/code-088)

## Kullanılan Teknolojiler

- Python
- CustomTkinter
- Cryptography (Fernet)
- Pyperclip
- Tkinter
- Python standart kütüphaneleri: `os`, `time` ve `sys`

## Gereksinimler

- Windows işletim sistemi
- Python 3.12 veya uyumlu bir sürüm
- `requirements.txt` dosyasında belirtilen kütüphaneler

## Kurulum

1. Projeyi indir veya GitHub üzerinden klonla.
2. Terminali proje klasöründe aç.
3. Gerekli kütüphaneleri yükle:

   ```bash
   pip install -r requirements.txt
   ```

4. Uygulamayı çalıştır:

   ```bash
   python main.py
   ```

> Ana Python dosyanın adı `main.py` değilse komutu kendi dosya adına göre değiştir.

## Kullanım

### 1. İlk Kurulum

Uygulama ilk kez çalıştırıldığında Windows kullanıcı profilinde `Kasa` klasörünü oluşturur. Bu klasörün içine `pass.txt` dosyasını ekler ve bir şifreleme anahtarı üretir.

### 2. Dosya Şifreleme

Uygulama, `Kasa` klasörü ve alt klasörlerinde bulunan dosyaları Fernet kullanarak şifreler. Oluşturulan anahtar panoya kopyalanır.

### 3. Giriş Yapma

Sonraki açılışlarda uygulama şifreleme anahtarını ister. Anahtar doğruysa dosyaların şifresi çözülür ve ana menü açılır.

### 4. Parola Yönetimi

Parola yöneticisi üzerinden aşağıdaki bilgiler kaydedilebilir:

- Başlık
- E-posta veya kullanıcı adı
- Parola
- Açıklama

Bu bilgiler `Kasa` klasöründeki `pass.txt` dosyasında saklanır.

## Güvenlik Uyarısı

**Şifreleme anahtarınızı güvenli bir yerde saklayın.** Fernet ile şifrelenen dosyaların şifresini çözmek için doğru anahtar gereklidir.

- Anahtarınızı kimseyle paylaşmayın.
- Anahtarınızın güvenli bir yedeğini alın.
- Dosyaların şifresini çözmeden anahtarı silmeyin veya değiştirmeyin.
- Önemli dosyalarınızı yedeksiz şekilde şifrelemeyin.

**Önemli:** Mevcut kodda uygulama kapanırken yeni bir anahtar oluşturulup dosyalar yeniden şifreleniyor. Eski anahtar kaybolursa dosyalar kurtarılamayabilir. Ayrıca parola kayıtları dosyaya önce düz metin olarak yazılıyor. Gerçek parolalarınızı saklamadan önce bu noktaların düzeltilmesi önerilir.

## Lisans

Bu proje için henüz bir lisans belirtilmemiştir.
