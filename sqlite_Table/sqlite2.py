import sqlite3
import random
import time
import datetime

sel = sqlite3.connect("dersler.db")

cursor = sel.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 (zaman REAL,tarih TEXT,anahtarkelime TEXT,deger REAL)")

def random_ekle():
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime='Python SQLite3'
    deger=random.randrange(0,100)
    cursor.execute("INSERT INTO Tablo1 (zaman,tarih,anahtarkelime,deger) VALUES (?,?,?,?)",
    (zaman,tarih,anahtarkelime,deger))
    sel.commit()
tablo_olustur()
i=0
while(i<10):
    random_ekle()
    i+=1
sel.close()