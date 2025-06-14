import sqlite3


# Öğrenci bilgilerini ekle
import sqlite3

def ogrenci_ekle(kullanici_adi, ad, soyad, yas, hedefler):
    conn = sqlite3.connect("kocluk.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO ogrenciler (kullanici_adi, ad, soyad, yas, hedefler) VALUES (?, ?, ?, ?, ?)",
            (kullanici_adi, ad, soyad, yas, hedefler)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Bu kullanıcı adı zaten mevcuttur. Lütfen farklı bir kullanıcı adı seçin lan.")
    finally:
        conn.close()



# Seans bilgilerini ekle
def seans_ekle(kullanici_adi, seans_tarihi, hedefler, notlar):
    conn = sqlite3.connect("kocluk.db")
    cursor = conn.cursor()
    try:
        # Kullanıcı adına göre öğrenci ID'sini al
        cursor.execute("SELECT id FROM ogrenciler WHERE kullanici_adi = ?", (kullanici_adi,))
        ogrenci_id = cursor.fetchone()
        if not ogrenci_id:
            raise ValueError("Bu kullanıcı adına sahip bir öğrenci bulunamadı.")

        ogrenci_id = ogrenci_id[0]  # ID'yi al
        cursor.execute(
            "INSERT INTO seanslar (ogrenci_id, seans_tarihi, hedefler, notlar) VALUES (?, ?, ?, ?)",
            (ogrenci_id, seans_tarihi, hedefler, notlar)
        )
        conn.commit()
    finally:
        conn.close()



# Ders ve soru çözüm verisini ekle
def ders_soru_ekle(ogrenci_id, ders_adı, konu, soru_sayisi, dogru_sayisi, yanlis_sayisi):
    connection = sqlite3.connect('kocluk_veritabani.db')
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO ders_soru (ogrenci_id, ders_adı, konu, soru_sayisi, dogru_sayisi, yanlis_sayisi) VALUES (?, ?, ?, ?, ?, ?)",
        (ogrenci_id, ders_adı, konu, soru_sayisi, dogru_sayisi, yanlis_sayisi))
    connection.commit()
    print(f"Ders verisi {ders_adı} başarıyla eklendi.")

    connection.close()


# Öğrenci bilgilerini güncelle
def ogrenci_bilgilerini_guncelle(ogrenci_id, ad=None, soyad=None, yas=None, hedefler=None):
    connection = sqlite3.connect('kocluk_veritabani.db')
    cursor = connection.cursor()

    if ad:
        cursor.execute("UPDATE ogrenciler SET ad = ? WHERE id = ?", (ad, ogrenci_id))
    if soyad:
        cursor.execute("UPDATE ogrenciler SET soyad = ? WHERE id = ?", (soyad, ogrenci_id))
    if yas:
        cursor.execute("UPDATE ogrenciler SET yas = ? WHERE id = ?", (yas, ogrenci_id))
    if hedefler:
        cursor.execute("UPDATE ogrenciler SET hedefler = ? WHERE id = ?", (hedefler, ogrenci_id))

    connection.commit()
    connection.close()
    print(f"Öğrenci ID {ogrenci_id} bilgileri güncellendi.")


# Seans bilgilerini güncelle
def seans_bilgilerini_guncelle(seans_id, ogrenci_id=None, seans_tarihi=None, hedefler=None, notlar=None):
    connection = sqlite3.connect('kocluk_veritabani.db')
    cursor = connection.cursor()

    if ogrenci_id:
        cursor.execute("UPDATE seanslar SET ogrenci_id = ? WHERE id = ?", (ogrenci_id, seans_id))
    if seans_tarihi:
        cursor.execute("UPDATE seanslar SET seans_tarihi = ? WHERE id = ?", (seans_tarihi, seans_id))
    if hedefler:
        cursor.execute("UPDATE seanslar SET hedefler = ? WHERE id = ?", (hedefler, seans_id))
    if notlar:
        cursor.execute("UPDATE seanslar SET notlar = ? WHERE id = ?", (notlar, seans_id))

    connection.commit()
    connection.close()
    print(f"Seans ID {seans_id} bilgileri güncellendi.")


# Ders ve soru çözüm verisini güncelle
def ders_soru_guncelle(ders_id, ogrenci_id=None, ders_adı=None, konu=None, soru_sayisi=None, dogru_sayisi=None,
                       yanlis_sayisi=None):
    connection = sqlite3.connect('kocluk_veritabani.db')
    cursor = connection.cursor()

    if ogrenci_id:
        cursor.execute("UPDATE ders_soru SET ogrenci_id = ? WHERE id = ?", (ogrenci_id, ders_id))
    if ders_adı:
        cursor.execute("UPDATE ders_soru SET ders_adı = ? WHERE id = ?", (ders_adı, ders_id))
    if konu:
        cursor.execute("UPDATE ders_soru SET konu = ? WHERE id = ?", (konu, ders_id))
    if soru_sayisi:
        cursor.execute("UPDATE ders_soru SET soru_sayisi = ? WHERE id = ?", (soru_sayisi, ders_id))
    if dogru_sayisi:
        cursor.execute("UPDATE ders_soru SET dogru_sayisi = ? WHERE id = ?", (dogru_sayisi, ders_id))
    if yanlis_sayisi:
        cursor.execute("UPDATE ders_soru SET yanlis_sayisi = ? WHERE id = ?", (yanlis_sayisi, ders_id))

    connection.commit()
    connection.close()
    print(f"Ders ve soru çözüm verisi ID {ders_id} güncellendi.")


# Öğrenci bilgilerini getirme (Yeni Fonksiyon)
def ogrenci_bilgilerini_getir(ogrenci_id):
    connection = sqlite3.connect('kocluk_veritabani.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM ogrenciler WHERE id = ?", (ogrenci_id,))
    ogrenci = cursor.fetchone()

    if ogrenci:
        ogrenci_bilgileri = f"Ad: {ogrenci[1]}\nSoyad: {ogrenci[2]}\nYaş: {ogrenci[3]}\nHedefler: {ogrenci[4]}"
    else:
        ogrenci_bilgileri = "Öğrenci bulunamadı."

    connection.close()
    return ogrenci_bilgileri
