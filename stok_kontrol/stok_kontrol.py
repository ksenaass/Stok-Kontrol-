import tkinter as tk
from tkinter import messagebox
import urllib.request # İndirme gerektirmeyen dahili kütüphane

def stok_kontrol_et():
    url = url_girdi_alani.get()
    
    if not url:
        messagebox.showwarning("Uyarı", "Lütfen bir ürün linki yapıştırın!")
        return
        
    try:
        # Sitelerin engellememesi için tarayıcı gibi davranıyoruz
        istek = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        
        # Sayfaya bağlanıp içeriği okuyoruz
        with urllib.request.urlopen(istek) as cevap:
            sayfa_metni = cevap.read().decode('utf-8').lower()
            
            # Kelime araması yapıyoruz
            if "tükendi" in sayfa_metni or "stokta yok" in sayfa_metni or "out of stock" in sayfa_metni:
                sonuc_etiketi.config(text="Durum: Stokta YOK ❌", fg="red")
            else:
                sonuc_etiketi.config(text="Durum: Stokta OLABİLİR ✅", fg="green")
                
    except Exception as hata:
        messagebox.showerror("Hata", f"İşlem başarısız oldu: {hata}")

# 1. Ana Pencere
pencere = tk.Tk()
pencere.title("İnditex Stok Kontrolcüsü")
pencere.geometry("400x200")

# 2. Bilgi Etiketi
bilgi_etiketi = tk.Label(pencere, text="Ürün Linkini Aşağıya Yapıştırın:", font=("Arial", 10))
bilgi_etiketi.pack(pady=10)

# 3. Giriş Kutusu
url_girdi_alani = tk.Entry(pencere, width=45)
url_girdi_alani.pack(pady=5)

# 4. Kontrol Butonu
kontrol_butonu = tk.Button(pencere, text="Stok Durumunu Sorgula", command=stok_kontrol_et, bg="lightblue")
kontrol_butonu.pack(pady=10)

# 5. Sonuç Etiketi
sonuc_etiketi = tk.Label(pencere, text="Durum: Bekleniyor...", font=("Arial", 12, "bold"))
sonuc_etiketi.pack(pady=10)

pencere.mainloop()