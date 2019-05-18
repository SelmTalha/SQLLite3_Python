from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys

sozluk = {"Aklıselim":"Sağduyu sahibi olan","Namütenahi":"Sonsuz,ucu bucağı ve nihayeti olmayan",
"Zevahir":"Dış görünüm","Feriştah":"İşin ehli,uzmanı ve en yetkili kimse.","Sirayet":"Bulaşma,başkalarına geçme,yayılma",
"Canhıraş":"Yürek parçalayan,iç tırmalayan","Mukadderat":"Yazgı,kadar.Meydana gelmesi kaçınılmaz olan durum."}



dosya="pencere.ui"
class BenimEkranim(QMainWindow):
    def __init__(self):
        super(BenimEkranim,self).__init__()
        uic.loadUi(dosya,self)
        self.aramabutonu.clicked.connect(self.kelime_bul)

    def kelime_bul(self):
        kelime=self.kelimegirisi.text()
        yazi=sozluk[kelime]
        yazi=str(yazi)
        self.sonuc.setText(yazi)

app=QApplication(sys.argv)
selim=BenimEkranim()
selim.show()
sys.exit(app.exec_())