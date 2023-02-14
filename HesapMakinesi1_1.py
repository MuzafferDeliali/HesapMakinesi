from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Enum
hesaplandi = False
hafiza = "0"


class TusTip(Enum):
    RAKAM = 0
    ISLEM = 1
    RESET = 2
    NOKTA = 3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(361, 471)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 9999999))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(361, 537))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 341, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(341, 371))
        self.widget.setMaximumSize(QtCore.QSize(341, 371))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setAccessibleDescription("")
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.bir = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("1"))
        self.bir.setGeometry(QtCore.QRect(77, 229, 50, 50))
        self.bir.setMinimumSize(QtCore.QSize(50, 50))
        self.bir.setMaximumSize(QtCore.QSize(50, 50))
        self.bir.setObjectName("bir")
        self.arti = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("+"))
        self.arti.setGeometry(QtCore.QRect(275, 229, 50, 50))
        self.arti.setMinimumSize(QtCore.QSize(50, 50))
        self.arti.setMaximumSize(QtCore.QSize(50, 50))
        self.arti.setAccessibleDescription("")
        self.arti.setObjectName("arti")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setExclusive(False)  # izin vermemesi gerekiyor
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.arti)
        self.uc = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("3"))
        self.uc.setGeometry(QtCore.QRect(209, 229, 50, 50))
        self.uc.setMinimumSize(QtCore.QSize(50, 50))
        self.uc.setMaximumSize(QtCore.QSize(50, 50))
        self.uc.setObjectName("uc")
        self.iki = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("2"))
        self.iki.setGeometry(QtCore.QRect(143, 229, 50, 50))
        self.iki.setMinimumSize(QtCore.QSize(50, 50))
        self.iki.setMaximumSize(QtCore.QSize(50, 50))
        self.iki.setObjectName("iki")
        self.ac = QtWidgets.QPushButton(self.widget)
        self.ac.setGeometry(QtCore.QRect(11, 300, 50, 50))
        self.ac.setMinimumSize(QtCore.QSize(50, 50))
        self.ac.setMaximumSize(QtCore.QSize(50, 50))
        self.ac.setObjectName("ac")
        self.esittir = QtWidgets.QPushButton(self.widget, clicked=lambda: self.hesapla())
        self.esittir.setGeometry(QtCore.QRect(209, 300, 50, 50))
        self.esittir.setMinimumSize(QtCore.QSize(50, 50))
        self.esittir.setMaximumSize(QtCore.QSize(50, 50))
        self.esittir.setObjectName("esittir")
        self.sil = QtWidgets.QPushButton(self.widget, clicked=lambda: self.kaldir())
        self.sil.setGeometry(QtCore.QRect(275, 300, 50, 50))
        self.sil.setMinimumSize(QtCore.QSize(50, 50))
        self.sil.setMaximumSize(QtCore.QSize(50, 50))
        self.sil.setObjectName("sil")
        self.sifir = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("0"))
        self.sifir.setGeometry(QtCore.QRect(77, 300, 50, 50))
        self.sifir.setMinimumSize(QtCore.QSize(50, 50))
        self.sifir.setMaximumSize(QtCore.QSize(50, 50))
        self.sifir.setObjectName("sifir")
        self.nokta = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("."))
        self.nokta.setGeometry(QtCore.QRect(143, 300, 50, 50))
        self.nokta.setMinimumSize(QtCore.QSize(50, 50))
        self.nokta.setMaximumSize(QtCore.QSize(50, 50))
        self.nokta.setObjectName("nokta")
        self.mc = QtWidgets.QPushButton(self.widget, clicked=lambda: self.M_Clear())
        self.mc.setGeometry(QtCore.QRect(11, 16, 50, 50))
        self.mc.setMinimumSize(QtCore.QSize(50, 50))
        self.mc.setMaximumSize(QtCore.QSize(50, 50))
        self.mc.setObjectName("mc")
        self.artiVeEksi = QtWidgets.QPushButton(self.widget, clicked=lambda: self.artieksi())
        self.artiVeEksi.setGeometry(QtCore.QRect(11, 158, 50, 50))
        self.artiVeEksi.setMinimumSize(QtCore.QSize(50, 50))
        self.artiVeEksi.setMaximumSize(QtCore.QSize(50, 50))
        self.artiVeEksi.setObjectName("artiVeEksi")
        self.bolu = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("/"))
        self.bolu.setGeometry(QtCore.QRect(275, 16, 50, 50))
        self.bolu.setMinimumSize(QtCore.QSize(50, 50))
        self.bolu.setMaximumSize(QtCore.QSize(50, 50))
        self.bolu.setObjectName("bolu")
        self.buttonGroup.addButton(self.bolu)
        self.dort = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("4"))
        self.dort.setGeometry(QtCore.QRect(77, 158, 50, 50))
        self.dort.setMinimumSize(QtCore.QSize(50, 50))
        self.dort.setMaximumSize(QtCore.QSize(50, 50))
        self.dort.setObjectName("dort")
        self.alti = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("6"))
        self.alti.setGeometry(QtCore.QRect(209, 158, 50, 50))
        self.alti.setMinimumSize(QtCore.QSize(50, 50))
        self.alti.setMaximumSize(QtCore.QSize(50, 50))
        self.alti.setObjectName("alti")
        self.bes = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("5"))
        self.bes.setGeometry(QtCore.QRect(143, 158, 50, 50))
        self.bes.setMinimumSize(QtCore.QSize(50, 50))
        self.bes.setMaximumSize(QtCore.QSize(50, 50))
        self.bes.setObjectName("bes")
        self.eksi = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("-"))
        self.eksi.setGeometry(QtCore.QRect(275, 158, 50, 50))
        self.eksi.setMinimumSize(QtCore.QSize(50, 50))
        self.eksi.setMaximumSize(QtCore.QSize(50, 50))
        self.eksi.setObjectName("eksi")
        self.buttonGroup.addButton(self.eksi)
        self.c = QtWidgets.QPushButton(self.widget, clicked=lambda: self.ekran.setText("0"))
        self.c.setGeometry(QtCore.QRect(11, 229, 50, 50))
        self.c.setMinimumSize(QtCore.QSize(50, 50))
        self.c.setMaximumSize(QtCore.QSize(50, 50))
        self.c.setObjectName("c")
        self.carpi = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("*"))
        self.carpi.setGeometry(QtCore.QRect(275, 87, 50, 50))
        self.carpi.setMinimumSize(QtCore.QSize(50, 50))
        self.carpi.setMaximumSize(QtCore.QSize(50, 50))
        self.carpi.setObjectName("carpi")
        self.buttonGroup.addButton(self.carpi)
        self.yedi = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("7"))
        self.yedi.setGeometry(QtCore.QRect(77, 87, 50, 50))
        self.yedi.setMinimumSize(QtCore.QSize(50, 50))
        self.yedi.setMaximumSize(QtCore.QSize(50, 50))
        self.yedi.setObjectName("yedi")
        self.sekiz = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("8"))
        self.sekiz.setGeometry(QtCore.QRect(143, 87, 50, 50))
        self.sekiz.setMinimumSize(QtCore.QSize(50, 50))
        self.sekiz.setMaximumSize(QtCore.QSize(50, 50))
        self.sekiz.setObjectName("sekiz")
        self.yuzde = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("%"))
        self.yuzde.setGeometry(QtCore.QRect(11, 87, 50, 50))
        self.yuzde.setMinimumSize(QtCore.QSize(50, 50))
        self.yuzde.setMaximumSize(QtCore.QSize(50, 50))
        self.yuzde.setObjectName("yuzde")
        self.buttonGroup.addButton(self.yuzde)
        self.dokuz = QtWidgets.QPushButton(self.widget, clicked=lambda: self.tiklandi("9"))
        self.dokuz.setGeometry(QtCore.QRect(209, 87, 50, 50))
        self.dokuz.setMinimumSize(QtCore.QSize(50, 50))
        self.dokuz.setMaximumSize(QtCore.QSize(50, 50))
        self.dokuz.setObjectName("dokuz")
        self.meksi = QtWidgets.QPushButton(self.widget, clicked=lambda: self.M_Eksi())
        self.meksi.setGeometry(QtCore.QRect(143, 16, 50, 50))
        self.meksi.setMinimumSize(QtCore.QSize(50, 50))
        self.meksi.setMaximumSize(QtCore.QSize(50, 50))
        self.meksi.setObjectName("meksi")
        self.marti = QtWidgets.QPushButton(self.widget, clicked=lambda: self.M_Arti())
        self.marti.setGeometry(QtCore.QRect(209, 16, 50, 50))
        self.marti.setMinimumSize(QtCore.QSize(50, 50))
        self.marti.setMaximumSize(QtCore.QSize(50, 50))
        self.marti.setObjectName("marti")
        self.mr = QtWidgets.QPushButton(self.widget, clicked=lambda: self.M_Read())
        self.mr.setGeometry(QtCore.QRect(77, 16, 50, 50))
        self.mr.setMinimumSize(QtCore.QSize(50, 50))
        self.mr.setMaximumSize(QtCore.QSize(50, 50))
        self.mr.setObjectName("mr")
        self.ekran = QtWidgets.QLabel(self.centralwidget)
        self.ekran.setGeometry(QtCore.QRect(10, 10, 341, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ekran.sizePolicy().hasHeightForWidth())
        self.ekran.setSizePolicy(sizePolicy)
        self.ekran.setMaximumSize(QtCore.QSize(341, 588))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ekran.setFont(font)
        self.ekran.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ekran.setFrameShape(QtWidgets.QFrame.Panel)
        self.ekran.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ekran.setLineWidth(2)
        self.ekran.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ekran.setObjectName("ekran")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @staticmethod
    def gettustip(pressed):
        if pressed == "C":
            return TusTip.RESET
        elif pressed == "+" or pressed == "-" or pressed == "*" or pressed == "/":
            return TusTip.ISLEM
        elif pressed == ".":
            return TusTip.NOKTA
        else:
            return TusTip.RAKAM

    def tiklandi(self, pressed):
        global hesaplandi
        yenitip = self.gettustip(pressed)
        sonkar = self.ekran.text()[-1]
        sontip = self.gettustip(sonkar)

        if yenitip == TusTip.RESET:
            self.ekran.setText("0")
        elif yenitip == TusTip.ISLEM:
            if self.ekran.text() == "HATA":
                self.ekran.setText("0")
            elif sontip == TusTip.ISLEM:
                self.kaldir()
                self.ekran.setText(f'{self.ekran.text()}{pressed}')
            elif sontip == TusTip.RAKAM:
                self.ekran.setText(f'{self.ekran.text()}{pressed}')
        elif yenitip == TusTip.RAKAM:
            if hesaplandi or self.ekran.text() == "0" or self.ekran.text() == "HATA":
                self.ekran.setText("")
            self.ekran.setText(f'{self.ekran.text()}{pressed}')
        elif yenitip == TusTip.NOKTA:
            if sontip == TusTip.NOKTA:
                return
            elif sontip == TusTip.RAKAM:
                self.ekran.setText(f'{self.ekran.text()}{pressed}')
        hesaplandi = False

    def kaldir(self):
        s = self.ekran.text()
        if self.ekran.text() == "HATA" or self.ekran.text() == "0":
            self.ekran.setText("0")
        else:
            self.ekran.setText(s[:len(s) - 1])

    def M_Arti(self):
        global hafiza
        hafiza = hafiza + "+" + self.ekran.text()
        eval(hafiza)
        print(hafiza)

    def M_Eksi(self):
        global hafiza
        hafiza = hafiza + "-" + self.ekran.text()
        eval(hafiza)
        print(hafiza)

    def M_Clear(self):
        global hafiza
        hafiza = "0"
        eval(hafiza)
        print(hafiza)

    def M_Read(self):
        global hafiza
        self.ekran.setText(str(hafiza))

    def artieksi(self):
        ekran = self.ekran.text()
        try:
            sonuc = eval(ekran)  # 'evaluate' kısaltması
            ekran = sonuc * -1
            self.ekran.setText(str(ekran))
        except:
            self.ekran.setText(str(ekran))

    # Hesaplamalar
    def hesapla(self):
        global hesaplandi
        hesaplandi = True
        ekrantext = self.ekran.text()
        try:
            sonuc = eval(ekrantext)  # 'evaluate' kısaltması
            sonuc = str("{:.2f}".format(round(sonuc, 2)))
            if sonuc.endswith('.0'):  # bölümlerde tam sayı olmasına rağmen ondalıklı sayıya çevirir
                sonuc = sonuc.replace('.0', '')
                self.ekran.setText(str(sonuc))
            else:
                self.ekran.setText(str(sonuc))
        except:
            self.ekran.setText("HATA")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hesap Makinesi 1.1"))
        self.bir.setText(_translate("MainWindow", "1"))
        self.arti.setText(_translate("MainWindow", "+"))
        self.uc.setText(_translate("MainWindow", "3"))
        self.iki.setText(_translate("MainWindow", "2"))
        self.ac.setText(_translate("MainWindow", "AC"))
        self.esittir.setText(_translate("MainWindow", "="))
        self.sil.setText(_translate("MainWindow", "<-"))
        self.sifir.setText(_translate("MainWindow", "0"))
        self.nokta.setText(_translate("MainWindow", "."))
        self.mc.setText(_translate("MainWindow", "MC"))
        self.artiVeEksi.setText(_translate("MainWindow", "+/-"))
        self.bolu.setText(_translate("MainWindow", "/"))
        self.dort.setText(_translate("MainWindow", "4"))
        self.alti.setText(_translate("MainWindow", "6"))
        self.bes.setText(_translate("MainWindow", "5"))
        self.eksi.setText(_translate("MainWindow", "-"))
        self.c.setText(_translate("MainWindow", "C"))
        self.carpi.setText(_translate("MainWindow", "X"))
        self.yedi.setText(_translate("MainWindow", "7"))
        self.sekiz.setText(_translate("MainWindow", "8"))
        self.yuzde.setText(_translate("MainWindow", "%"))
        self.dokuz.setText(_translate("MainWindow", "9"))
        self.meksi.setText(_translate("MainWindow", "M-"))
        self.marti.setText(_translate("MainWindow", "M+"))
        self.mr.setText(_translate("MainWindow", "MR"))
        self.ekran.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
