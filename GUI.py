# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Thu Apr 24 19:46:28 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(850, 650)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ikony/water.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.przycisk_klasyfikuj = QtGui.QPushButton(self.centralwidget)
        self.przycisk_klasyfikuj.setGeometry(QtCore.QRect(610, 540, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.przycisk_klasyfikuj.setFont(font)
        self.przycisk_klasyfikuj.setObjectName(_fromUtf8("przycisk_klasyfikuj"))
        self.label_46 = QtGui.QLabel(self.centralwidget)
        self.label_46.setGeometry(QtCore.QRect(510, 0, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(90, 0, 142, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 294, 571))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_18 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 4, 0, 1, 2)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 15, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 10, 0, 1, 2)
        self.line_4 = QtGui.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_2.addWidget(self.line_4, 9, 0, 1, 2)
        self.IOJ = QtGui.QLineEdit(self.layoutWidget)
        self.IOJ.setObjectName(_fromUtf8("IOJ"))
        self.gridLayout_2.addWidget(self.IOJ, 7, 1, 1, 1)
        self.line_5 = QtGui.QFrame(self.layoutWidget)
        self.line_5.setFrameShadow(QtGui.QFrame.Raised)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 11, 0, 1, 2)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 12, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 3, 0, 1, 2)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 13, 0, 1, 1)
        self.hydro1 = QtGui.QCheckBox(self.layoutWidget)
        self.hydro1.setEnabled(True)
        self.hydro1.setChecked(False)
        self.hydro1.setObjectName(_fromUtf8("hydro1"))
        self.gridLayout_2.addWidget(self.hydro1, 12, 1, 1, 1)
        self.chlorofil = QtGui.QLineEdit(self.layoutWidget)
        self.chlorofil.setObjectName(_fromUtf8("chlorofil"))
        self.gridLayout_2.addWidget(self.chlorofil, 6, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 7, 0, 1, 1)
        self.hydro3 = QtGui.QCheckBox(self.layoutWidget)
        self.hydro3.setEnabled(True)
        self.hydro3.setChecked(False)
        self.hydro3.setObjectName(_fromUtf8("hydro3"))
        self.gridLayout_2.addWidget(self.hydro3, 14, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 8, 0, 1, 1)
        self.MISE = QtGui.QLineEdit(self.layoutWidget)
        self.MISE.setObjectName(_fromUtf8("MISE"))
        self.gridLayout_2.addWidget(self.MISE, 8, 1, 1, 1)
        self.schindler = QtGui.QLineEdit(self.layoutWidget)
        self.schindler.setObjectName(_fromUtf8("schindler"))
        self.gridLayout_2.addWidget(self.schindler, 2, 1, 1, 1)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 5, 0, 1, 2)
        self.morf1 = QtGui.QCheckBox(self.layoutWidget)
        self.morf1.setEnabled(True)
        self.morf1.setChecked(False)
        self.morf1.setObjectName(_fromUtf8("morf1"))
        self.gridLayout_2.addWidget(self.morf1, 15, 1, 1, 1)
        self.hydro2 = QtGui.QCheckBox(self.layoutWidget)
        self.hydro2.setEnabled(True)
        self.hydro2.setChecked(False)
        self.hydro2.setObjectName(_fromUtf8("hydro2"))
        self.gridLayout_2.addWidget(self.hydro2, 13, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 14, 0, 1, 1)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 0, 0, 1, 2)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.typ = QtGui.QComboBox(self.layoutWidget)
        self.typ.setObjectName(_fromUtf8("typ"))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.typ.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.typ, 1, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.layoutWidget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 6, 0, 1, 1)
        self.line_7 = QtGui.QFrame(self.layoutWidget)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout_2.addWidget(self.line_7, 21, 0, 1, 2)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 16, 0, 1, 1)
        self.morf2 = QtGui.QCheckBox(self.layoutWidget)
        self.morf2.setEnabled(True)
        self.morf2.setChecked(False)
        self.morf2.setObjectName(_fromUtf8("morf2"))
        self.gridLayout_2.addWidget(self.morf2, 16, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 17, 0, 1, 1)
        self.morf3 = QtGui.QCheckBox(self.layoutWidget)
        self.morf3.setEnabled(True)
        self.morf3.setChecked(False)
        self.morf3.setObjectName(_fromUtf8("morf3"))
        self.gridLayout_2.addWidget(self.morf3, 17, 1, 1, 1)
        self.line_6 = QtGui.QFrame(self.layoutWidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout_2.addWidget(self.line_6, 18, 0, 1, 2)
        self.label_20 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_2.addWidget(self.label_20, 20, 0, 1, 2)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 22, 0, 1, 1)
        self.secchi = QtGui.QLineEdit(self.layoutWidget)
        self.secchi.setObjectName(_fromUtf8("secchi"))
        self.gridLayout_2.addWidget(self.secchi, 22, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 23, 0, 1, 1)
        self.tlen1 = QtGui.QLineEdit(self.layoutWidget)
        self.tlen1.setObjectName(_fromUtf8("tlen1"))
        self.gridLayout_2.addWidget(self.tlen1, 23, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 24, 0, 1, 1)
        self.tlen2 = QtGui.QLineEdit(self.layoutWidget)
        self.tlen2.setObjectName(_fromUtf8("tlen2"))
        self.gridLayout_2.addWidget(self.tlen2, 24, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 25, 0, 1, 1)
        self.przew = QtGui.QLineEdit(self.layoutWidget)
        self.przew.setObjectName(_fromUtf8("przew"))
        self.gridLayout_2.addWidget(self.przew, 25, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.layoutWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 26, 0, 1, 1)
        self.azot = QtGui.QLineEdit(self.layoutWidget)
        self.azot.setObjectName(_fromUtf8("azot"))
        self.gridLayout_2.addWidget(self.azot, 26, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 27, 0, 1, 1)
        self.fosfor = QtGui.QLineEdit(self.layoutWidget)
        self.fosfor.setObjectName(_fromUtf8("fosfor"))
        self.gridLayout_2.addWidget(self.fosfor, 27, 1, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(330, 30, 487, 351))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.srebro = QtGui.QLineEdit(self.layoutWidget1)
        self.srebro.setObjectName(_fromUtf8("srebro"))
        self.gridLayout_3.addWidget(self.srebro, 5, 4, 1, 1)
        self.molibden = QtGui.QLineEdit(self.layoutWidget1)
        self.molibden.setObjectName(_fromUtf8("molibden"))
        self.gridLayout_3.addWidget(self.molibden, 2, 4, 1, 1)
        self.glin = QtGui.QLineEdit(self.layoutWidget1)
        self.glin.setObjectName(_fromUtf8("glin"))
        self.gridLayout_3.addWidget(self.glin, 11, 2, 1, 1)
        self.IOM = QtGui.QLineEdit(self.layoutWidget1)
        self.IOM.setObjectName(_fromUtf8("IOM"))
        self.gridLayout_3.addWidget(self.IOM, 10, 2, 1, 1)
        self.label_31 = QtGui.QLabel(self.layoutWidget1)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_3.addWidget(self.label_31, 9, 0, 1, 2)
        self.label_27 = QtGui.QLabel(self.layoutWidget1)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_3.addWidget(self.label_27, 5, 0, 1, 2)
        self.selen = QtGui.QLineEdit(self.layoutWidget1)
        self.selen.setObjectName(_fromUtf8("selen"))
        self.gridLayout_3.addWidget(self.selen, 3, 4, 1, 1)
        self.label_38 = QtGui.QLabel(self.layoutWidget1)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_3.addWidget(self.label_38, 5, 3, 1, 1)
        self.label_41 = QtGui.QLabel(self.layoutWidget1)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_3.addWidget(self.label_41, 7, 3, 1, 1)
        self.label_35 = QtGui.QLabel(self.layoutWidget1)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout_3.addWidget(self.label_35, 1, 3, 1, 1)
        self.cynk = QtGui.QLineEdit(self.layoutWidget1)
        self.cynk.setObjectName(_fromUtf8("cynk"))
        self.gridLayout_3.addWidget(self.cynk, 7, 2, 1, 1)
        self.bor = QtGui.QLineEdit(self.layoutWidget1)
        self.bor.setObjectName(_fromUtf8("bor"))
        self.gridLayout_3.addWidget(self.bor, 4, 2, 1, 1)
        self.tal = QtGui.QLineEdit(self.layoutWidget1)
        self.tal.setObjectName(_fromUtf8("tal"))
        self.gridLayout_3.addWidget(self.tal, 4, 4, 1, 1)
        self.aldehyd = QtGui.QLineEdit(self.layoutWidget1)
        self.aldehyd.setObjectName(_fromUtf8("aldehyd"))
        self.gridLayout_3.addWidget(self.aldehyd, 1, 2, 1, 1)
        self.beryl = QtGui.QLineEdit(self.layoutWidget1)
        self.beryl.setObjectName(_fromUtf8("beryl"))
        self.gridLayout_3.addWidget(self.beryl, 10, 4, 1, 1)
        self.label_33 = QtGui.QLabel(self.layoutWidget1)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_3.addWidget(self.label_33, 11, 0, 1, 2)
        self.bar = QtGui.QLineEdit(self.layoutWidget1)
        self.bar.setObjectName(_fromUtf8("bar"))
        self.gridLayout_3.addWidget(self.bar, 3, 2, 1, 1)
        self.label_30 = QtGui.QLabel(self.layoutWidget1)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_3.addWidget(self.label_30, 8, 0, 1, 2)
        self.label_32 = QtGui.QLabel(self.layoutWidget1)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_3.addWidget(self.label_32, 10, 0, 1, 2)
        self.label_36 = QtGui.QLabel(self.layoutWidget1)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_3.addWidget(self.label_36, 2, 3, 1, 1)
        self.label_42 = QtGui.QLabel(self.layoutWidget1)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_3.addWidget(self.label_42, 8, 3, 1, 1)
        self.cyjankiz = QtGui.QLineEdit(self.layoutWidget1)
        self.cyjankiz.setObjectName(_fromUtf8("cyjankiz"))
        self.gridLayout_3.addWidget(self.cyjankiz, 1, 4, 1, 1)
        self.arsen = QtGui.QLineEdit(self.layoutWidget1)
        self.arsen.setObjectName(_fromUtf8("arsen"))
        self.gridLayout_3.addWidget(self.arsen, 2, 2, 1, 1)
        self.chrom = QtGui.QLineEdit(self.layoutWidget1)
        self.chrom.setObjectName(_fromUtf8("chrom"))
        self.gridLayout_3.addWidget(self.chrom, 6, 2, 1, 1)
        self.label_29 = QtGui.QLabel(self.layoutWidget1)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_3.addWidget(self.label_29, 7, 0, 1, 2)
        self.lineEdit_24 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_24.setEnabled(False)
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.gridLayout_3.addWidget(self.lineEdit_24, 12, 4, 1, 1)
        self.label_43 = QtGui.QLabel(self.layoutWidget1)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_3.addWidget(self.label_43, 9, 3, 1, 1)
        self.label_40 = QtGui.QLabel(self.layoutWidget1)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout_3.addWidget(self.label_40, 6, 3, 1, 1)
        self.label_23 = QtGui.QLabel(self.layoutWidget1)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_3.addWidget(self.label_23, 1, 0, 1, 2)
        self.label_28 = QtGui.QLabel(self.layoutWidget1)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_3.addWidget(self.label_28, 6, 0, 1, 2)
        self.miedz = QtGui.QLineEdit(self.layoutWidget1)
        self.miedz.setObjectName(_fromUtf8("miedz"))
        self.gridLayout_3.addWidget(self.miedz, 8, 2, 1, 1)
        self.label_39 = QtGui.QLabel(self.layoutWidget1)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_3.addWidget(self.label_39, 4, 3, 1, 1)
        self.label_24 = QtGui.QLabel(self.layoutWidget1)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_3.addWidget(self.label_24, 2, 0, 1, 2)
        self.tytan = QtGui.QLineEdit(self.layoutWidget1)
        self.tytan.setObjectName(_fromUtf8("tytan"))
        self.gridLayout_3.addWidget(self.tytan, 6, 4, 1, 1)
        self.label_44 = QtGui.QLabel(self.layoutWidget1)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_3.addWidget(self.label_44, 10, 3, 1, 1)
        self.wanad = QtGui.QLineEdit(self.layoutWidget1)
        self.wanad.setObjectName(_fromUtf8("wanad"))
        self.gridLayout_3.addWidget(self.wanad, 7, 4, 1, 1)
        self.label_45 = QtGui.QLabel(self.layoutWidget1)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.gridLayout_3.addWidget(self.label_45, 11, 3, 1, 1)
        self.fluorki = QtGui.QLineEdit(self.layoutWidget1)
        self.fluorki.setObjectName(_fromUtf8("fluorki"))
        self.gridLayout_3.addWidget(self.fluorki, 9, 4, 1, 1)
        self.label_25 = QtGui.QLabel(self.layoutWidget1)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_3.addWidget(self.label_25, 3, 0, 1, 2)
        self.label_37 = QtGui.QLabel(self.layoutWidget1)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout_3.addWidget(self.label_37, 3, 3, 1, 1)
        self.label_34 = QtGui.QLabel(self.layoutWidget1)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_3.addWidget(self.label_34, 12, 0, 1, 2)
        self.label_22 = QtGui.QLabel(self.layoutWidget1)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_3.addWidget(self.label_22, 12, 3, 1, 1)
        self.cyjankiw = QtGui.QLineEdit(self.layoutWidget1)
        self.cyjankiw.setObjectName(_fromUtf8("cyjankiw"))
        self.gridLayout_3.addWidget(self.cyjankiw, 12, 2, 1, 1)
        self.chrom6 = QtGui.QLineEdit(self.layoutWidget1)
        self.chrom6.setObjectName(_fromUtf8("chrom6"))
        self.gridLayout_3.addWidget(self.chrom6, 5, 2, 1, 1)
        self.label_26 = QtGui.QLabel(self.layoutWidget1)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_3.addWidget(self.label_26, 4, 0, 1, 2)
        self.kobalt = QtGui.QLineEdit(self.layoutWidget1)
        self.kobalt.setObjectName(_fromUtf8("kobalt"))
        self.gridLayout_3.addWidget(self.kobalt, 11, 4, 1, 1)
        self.I_F = QtGui.QLineEdit(self.layoutWidget1)
        self.I_F.setObjectName(_fromUtf8("I_F"))
        self.gridLayout_3.addWidget(self.I_F, 9, 2, 1, 1)
        self.antymon = QtGui.QLineEdit(self.layoutWidget1)
        self.antymon.setObjectName(_fromUtf8("antymon"))
        self.gridLayout_3.addWidget(self.antymon, 8, 4, 1, 1)
        self.line_8 = QtGui.QFrame(self.layoutWidget1)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout_3.addWidget(self.line_8, 0, 0, 1, 5)
        self.wyniki = QtGui.QTextEdit(self.centralwidget)
        self.wyniki.setGeometry(QtCore.QRect(330, 430, 271, 151))
        self.wyniki.setReadOnly(True)
        self.wyniki.setObjectName(_fromUtf8("wyniki"))
        self.label_47 = QtGui.QLabel(self.centralwidget)
        self.label_47.setGeometry(QtCore.QRect(390, 400, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuProgram = QtGui.QMenu(self.menubar)
        self.menuProgram.setObjectName(_fromUtf8("menuProgram"))
        self.menuPomoc = QtGui.QMenu(self.menubar)
        self.menuPomoc.setObjectName(_fromUtf8("menuPomoc"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_save = QtGui.QAction(MainWindow)
        self.action_save.setObjectName(_fromUtf8("action_save"))
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.action_author = QtGui.QAction(MainWindow)
        self.action_author.setObjectName(_fromUtf8("action_author"))
        self.action_quit = QtGui.QAction(MainWindow)
        self.action_quit.setObjectName(_fromUtf8("action_quit"))
        self.action_save_results = QtGui.QAction(MainWindow)
        self.action_save_results.setObjectName(_fromUtf8("action_save_results"))
        self.menuProgram.addAction(self.action_open)
        self.menuProgram.addAction(self.action_save)
        self.menuProgram.addAction(self.action_save_results)
        self.menuProgram.addAction(self.action_quit)
        self.menuPomoc.addAction(self.action_about)
        self.menuPomoc.addAction(self.action_author)
        self.menubar.addAction(self.menuProgram.menuAction())
        self.menubar.addAction(self.menuPomoc.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_quit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.typ, self.schindler)
        MainWindow.setTabOrder(self.schindler, self.chlorofil)
        MainWindow.setTabOrder(self.chlorofil, self.IOJ)
        MainWindow.setTabOrder(self.IOJ, self.MISE)
        MainWindow.setTabOrder(self.MISE, self.hydro1)
        MainWindow.setTabOrder(self.hydro1, self.hydro2)
        MainWindow.setTabOrder(self.hydro2, self.hydro3)
        MainWindow.setTabOrder(self.hydro3, self.morf1)
        MainWindow.setTabOrder(self.morf1, self.morf2)
        MainWindow.setTabOrder(self.morf2, self.morf3)
        MainWindow.setTabOrder(self.morf3, self.secchi)
        MainWindow.setTabOrder(self.secchi, self.tlen1)
        MainWindow.setTabOrder(self.tlen1, self.tlen2)
        MainWindow.setTabOrder(self.tlen2, self.przew)
        MainWindow.setTabOrder(self.przew, self.azot)
        MainWindow.setTabOrder(self.azot, self.fosfor)
        MainWindow.setTabOrder(self.fosfor, self.aldehyd)
        MainWindow.setTabOrder(self.aldehyd, self.arsen)
        MainWindow.setTabOrder(self.arsen, self.bar)
        MainWindow.setTabOrder(self.bar, self.bor)
        MainWindow.setTabOrder(self.bor, self.chrom6)
        MainWindow.setTabOrder(self.chrom6, self.chrom)
        MainWindow.setTabOrder(self.chrom, self.cynk)
        MainWindow.setTabOrder(self.cynk, self.miedz)
        MainWindow.setTabOrder(self.miedz, self.I_F)
        MainWindow.setTabOrder(self.I_F, self.IOM)
        MainWindow.setTabOrder(self.IOM, self.glin)
        MainWindow.setTabOrder(self.glin, self.cyjankiw)
        MainWindow.setTabOrder(self.cyjankiw, self.cyjankiz)
        MainWindow.setTabOrder(self.cyjankiz, self.molibden)
        MainWindow.setTabOrder(self.molibden, self.selen)
        MainWindow.setTabOrder(self.selen, self.tal)
        MainWindow.setTabOrder(self.tal, self.srebro)
        MainWindow.setTabOrder(self.srebro, self.tytan)
        MainWindow.setTabOrder(self.tytan, self.wanad)
        MainWindow.setTabOrder(self.wanad, self.antymon)
        MainWindow.setTabOrder(self.antymon, self.fluorki)
        MainWindow.setTabOrder(self.fluorki, self.beryl)
        MainWindow.setTabOrder(self.beryl, self.kobalt)
        MainWindow.setTabOrder(self.kobalt, self.lineEdit_24)
        MainWindow.setTabOrder(self.lineEdit_24, self.przycisk_klasyfikuj)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Klasyfikacja jezior", None))
        self.przycisk_klasyfikuj.setText(_translate("MainWindow", "Klasyfikuj", None))
        self.label_46.setText(_translate("MainWindow", "Zanieczyszczenia", None))
        self.label_17.setText(_translate("MainWindow", "Wskaźniki jakości wód", None))
        self.label_18.setText(_translate("MainWindow", "Wskaźniki biologiczne ", None))
        self.label_8.setText(_translate("MainWindow", "Zmienność głębokości", None))
        self.label_19.setText(_translate("MainWindow", " Elementy hydromorfologiczne", None))
        self.IOJ.setText(_translate("MainWindow", "0", None))
        self.label_5.setText(_translate("MainWindow", "Wielkość i dynamika przepływu wody", None))
        self.label_6.setText(_translate("MainWindow", "Połączenie z częściami wód podziemnych", None))
        self.hydro1.setText(_translate("MainWindow", "1 klasa", None))
        self.chlorofil.setText(_translate("MainWindow", "0", None))
        self.label_3.setText(_translate("MainWindow", "Multimetryczny indeks okrzemkowy", None))
        self.hydro3.setText(_translate("MainWindow", "1 klasa", None))
        self.label_4.setText(_translate("MainWindow", "Makrofitowy indeks stanu ekologicznego", None))
        self.MISE.setText(_translate("MainWindow", "0", None))
        self.schindler.setText(_translate("MainWindow", "0", None))
        self.morf1.setText(_translate("MainWindow", "1 klasa", None))
        self.hydro2.setText(_translate("MainWindow", "1 klasa", None))
        self.label_7.setText(_translate("MainWindow", "Czas retencji", None))
        self.label.setText(_translate("MainWindow", "Współczynnik Schindlera", None))
        self.label_2.setText(_translate("MainWindow", "Typ jeziora", None))
        self.typ.setItemText(0, _translate("MainWindow", "1a", None))
        self.typ.setItemText(1, _translate("MainWindow", "1b", None))
        self.typ.setItemText(2, _translate("MainWindow", "2a", None))
        self.typ.setItemText(3, _translate("MainWindow", "2b", None))
        self.typ.setItemText(4, _translate("MainWindow", "3a", None))
        self.typ.setItemText(5, _translate("MainWindow", "3b", None))
        self.typ.setItemText(6, _translate("MainWindow", "4", None))
        self.typ.setItemText(7, _translate("MainWindow", "5a", None))
        self.typ.setItemText(8, _translate("MainWindow", "5b", None))
        self.typ.setItemText(9, _translate("MainWindow", "6a", None))
        self.typ.setItemText(10, _translate("MainWindow", "6b", None))
        self.typ.setItemText(11, _translate("MainWindow", "7a", None))
        self.typ.setItemText(12, _translate("MainWindow", "7b", None))
        self.label_21.setText(_translate("MainWindow", "Chlorofil \"a\"", None))
        self.label_9.setText(_translate("MainWindow", "Struktura ilościowa i podłoże dna", None))
        self.morf2.setText(_translate("MainWindow", "1 klasa", None))
        self.label_10.setText(_translate("MainWindow", "Struktura brzegu jeziora", None))
        self.morf3.setText(_translate("MainWindow", "1 klasa", None))
        self.label_20.setText(_translate("MainWindow", " Elementy fizykochemiczne", None))
        self.label_11.setText(_translate("MainWindow", "Widzialność krążka Secchiego", None))
        self.secchi.setText(_translate("MainWindow", "0", None))
        self.label_12.setText(_translate("MainWindow", "Tlen rozpuszczony", None))
        self.tlen1.setText(_translate("MainWindow", "0", None))
        self.label_13.setText(_translate("MainWindow", "Nasycenie tlenem hypolimnionu", None))
        self.tlen2.setText(_translate("MainWindow", "0", None))
        self.label_14.setText(_translate("MainWindow", "Przewodność", None))
        self.przew.setText(_translate("MainWindow", "0", None))
        self.label_15.setText(_translate("MainWindow", "Azot całkowity", None))
        self.azot.setText(_translate("MainWindow", "0", None))
        self.label_16.setText(_translate("MainWindow", "Fosfor ogólny", None))
        self.fosfor.setText(_translate("MainWindow", "0", None))
        self.srebro.setText(_translate("MainWindow", "0", None))
        self.molibden.setText(_translate("MainWindow", "0", None))
        self.glin.setText(_translate("MainWindow", "0", None))
        self.IOM.setText(_translate("MainWindow", "0", None))
        self.label_31.setText(_translate("MainWindow", "Indeks fenolowy", None))
        self.label_27.setText(_translate("MainWindow", "Chrom VI", None))
        self.selen.setText(_translate("MainWindow", "0", None))
        self.label_38.setText(_translate("MainWindow", "Srebro", None))
        self.label_41.setText(_translate("MainWindow", "Wanad", None))
        self.label_35.setText(_translate("MainWindow", "Cyjanki związane", None))
        self.cynk.setText(_translate("MainWindow", "0", None))
        self.bor.setText(_translate("MainWindow", "0", None))
        self.tal.setText(_translate("MainWindow", "0", None))
        self.aldehyd.setText(_translate("MainWindow", "0", None))
        self.beryl.setText(_translate("MainWindow", "0", None))
        self.label_33.setText(_translate("MainWindow", "Glin", None))
        self.bar.setText(_translate("MainWindow", "0", None))
        self.label_30.setText(_translate("MainWindow", "Miedź", None))
        self.label_32.setText(_translate("MainWindow", "Indeks oleju mineralnego", None))
        self.label_36.setText(_translate("MainWindow", "Molibden", None))
        self.label_42.setText(_translate("MainWindow", "Antymon", None))
        self.cyjankiz.setText(_translate("MainWindow", "0", None))
        self.arsen.setText(_translate("MainWindow", "0", None))
        self.chrom.setText(_translate("MainWindow", "0", None))
        self.label_29.setText(_translate("MainWindow", "Cynk", None))
        self.lineEdit_24.setText(_translate("MainWindow", "Wskaźnik nieuwzględniony", None))
        self.label_43.setText(_translate("MainWindow", "Fluorki", None))
        self.label_40.setText(_translate("MainWindow", "Tytan", None))
        self.label_23.setText(_translate("MainWindow", "Aldehyd mrówkowy", None))
        self.label_28.setText(_translate("MainWindow", "Chrom ogólny", None))
        self.miedz.setText(_translate("MainWindow", "0", None))
        self.label_39.setText(_translate("MainWindow", "Tal", None))
        self.label_24.setText(_translate("MainWindow", "Arsen", None))
        self.tytan.setText(_translate("MainWindow", "0", None))
        self.label_44.setText(_translate("MainWindow", "Beryl", None))
        self.wanad.setText(_translate("MainWindow", "0", None))
        self.label_45.setText(_translate("MainWindow", "Kobalt", None))
        self.fluorki.setText(_translate("MainWindow", "0", None))
        self.label_25.setText(_translate("MainWindow", "Bar", None))
        self.label_37.setText(_translate("MainWindow", "Selen", None))
        self.label_34.setText(_translate("MainWindow", "Cyjanki wolne", None))
        self.label_22.setText(_translate("MainWindow", "Cyna", None))
        self.cyjankiw.setText(_translate("MainWindow", "0", None))
        self.chrom6.setText(_translate("MainWindow", "0", None))
        self.label_26.setText(_translate("MainWindow", "Bor", None))
        self.kobalt.setText(_translate("MainWindow", "0", None))
        self.I_F.setText(_translate("MainWindow", "0", None))
        self.antymon.setText(_translate("MainWindow", "0", None))
        self.label_47.setText(_translate("MainWindow", "Wyniki klasyfikacji", None))
        self.menuProgram.setTitle(_translate("MainWindow", "Program", None))
        self.menuPomoc.setTitle(_translate("MainWindow", "Pomoc", None))
        self.action_open.setText(_translate("MainWindow", "Otwórz raport", None))
        self.action_save.setText(_translate("MainWindow", "Zapisz raport", None))
        self.action_about.setText(_translate("MainWindow", "O programie...", None))
        self.action_author.setText(_translate("MainWindow", "O autorze...", None))
        self.action_quit.setText(_translate("MainWindow", "Wyjście", None))
        self.action_save_results.setText(_translate("MainWindow", "Zapisz wyniki", None))

import zasoby_rc
