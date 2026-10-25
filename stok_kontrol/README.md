# İnditex Stok Kontrolcüsü

Bu proje, Zara, Pull&Bear, Bershka gibi İnditex grubu web sitelerindeki ürünlerin stok durumunu kontrol etmek için geliştirilmiş, arayüzlü (GUI) bir başlangıç seviyesi Python programıdır.

**Özellikler**
* Kullanıcı dostu Tkinter açılır pencere arayüzü.
* Dış kütüphane kurulumu (pip install) gerektirmez. Python'un dahili kütüphaneleriyle (`tkinter`, `urllib`) çalışır.
* Sayfa içeriğini analiz ederek "Tükendi" veya "Stokta Var" durumunu ekrana yansıtır.

**Kurulum ve Kullanım**
1. Bilgisayarınızda Python'un yüklü olduğundan emin olun.
2. Terminal veya komut istemcisinde (CMD) projenin bulunduğu klasöre gidin.
3. `python stok_kontrol.py` (veya `py stok_kontrol.py`) komutunu çalıştırarak arayüzü açın.
4. Kontrol etmek istediğiniz ürünün linkini kopyalayıp giriş kutusuna yapıştırın ve sorgula butonuna tıklayın.
