import sqlite3

sel = sqlite3.connect("dersler.db")

cursor = sel.cursor()

def tablo_olustur():
    cursor.execute('CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT,soyad TEXT,numara INT,ogrencinotu INT)')
    #IF NOT EXISTS = TABLOYU OLUSTUR ANCAK YOKSA ANLAMINDA KULLANILDI.
    #AKSİ HALDE 2.ÇALIŞTIRMADA ZATEN ogrenciler TABLOSU OLDUĞUNU VE OLUSTURAMAYACAĞINI HATA OLARAK VERDİ

def deger_ekle():
    cursor.execute("INSERT INTO ogrenciler VALUES('Murat İsmail','Akçay',27,75)")
    sel.commit()
    sel.close()

tablo_olustur()
deger_ekle()