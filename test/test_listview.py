# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_listview.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import matplotlib
matplotlib.use('Qt5Agg')


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, QAbstractTableModel, Qt
import random
import compute
from datetime import datetime
from skyfield.api import utc
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 600)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 150, 130, 400))
        self.listWidget.setObjectName("listWidget")
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setGeometry(QtCore.QRect(235, 20, 75, 25))
        self.testButton.setObjectName("testButton")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 20, 210, 25))
        self.label1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(150, 130, 770, 420))
        self.groupBox.setObjectName("groupBox")

        self.frame_grafik = QtWidgets.QFrame(self.groupBox)
        self.frame_grafik.setGeometry(QtCore.QRect(260, 20, 500, 390))
        self.frame_grafik.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grafik.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grafik.setObjectName("frame_grafik")

        self.lineEdit_konjungsi = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_konjungsi.setGeometry(QtCore.QRect(100, 50, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_konjungsi.setFont(font)
        self.lineEdit_konjungsi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_konjungsi.setText("")
        self.lineEdit_konjungsi.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_konjungsi.setReadOnly(True)
        self.lineEdit_konjungsi.setObjectName("lineEdit_konjungsi")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_2.setMouseTracking(False)
        self.label_2.setTabletTracking(False)
        self.label_2.setAcceptDrops(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_3.setMouseTracking(False)
        self.label_3.setTabletTracking(False)
        self.label_3.setAcceptDrops(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.lineEdit_sunset = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_sunset.setGeometry(QtCore.QRect(100, 80, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_sunset.setFont(font)
        self.lineEdit_sunset.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_sunset.setText("")
        self.lineEdit_sunset.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_sunset.setReadOnly(True)
        self.lineEdit_sunset.setObjectName("lineEdit_sunset")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_4.setMouseTracking(False)
        self.label_4.setTabletTracking(False)
        self.label_4.setAcceptDrops(False)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_5.setMouseTracking(False)
        self.label_5.setTabletTracking(False)
        self.label_5.setAcceptDrops(False)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_6.setMouseTracking(False)
        self.label_6.setTabletTracking(False)
        self.label_6.setAcceptDrops(False)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_7.setMouseTracking(False)
        self.label_7.setTabletTracking(False)
        self.label_7.setAcceptDrops(False)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 230, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_8.setMouseTracking(False)
        self.label_8.setTabletTracking(False)
        self.label_8.setAcceptDrops(False)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_9.setMouseTracking(False)
        self.label_9.setTabletTracking(False)
        self.label_9.setAcceptDrops(False)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 290, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_10.setMouseTracking(False)
        self.label_10.setTabletTracking(False)
        self.label_10.setAcceptDrops(False)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 320, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_11.setMouseTracking(False)
        self.label_11.setTabletTracking(False)
        self.label_11.setAcceptDrops(False)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 380, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_12.setMouseTracking(False)
        self.label_12.setTabletTracking(False)
        self.label_12.setAcceptDrops(False)
        self.label_12.setWordWrap(False)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 350, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_13.setMouseTracking(False)
        self.label_13.setTabletTracking(False)
        self.label_13.setAcceptDrops(False)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.lineEdit_altBulan = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_altBulan.setGeometry(QtCore.QRect(100, 110, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_altBulan.setFont(font)
        self.lineEdit_altBulan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_altBulan.setText("")
        self.lineEdit_altBulan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_altBulan.setReadOnly(True)
        self.lineEdit_altBulan.setObjectName("lineEdit_altBulan")
        self.lineEdit_azBulan = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_azBulan.setGeometry(QtCore.QRect(100, 140, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_azBulan.setFont(font)
        self.lineEdit_azBulan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_azBulan.setText("")
        self.lineEdit_azBulan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_azBulan.setReadOnly(True)
        self.lineEdit_azBulan.setObjectName("lineEdit_azBulan")
        self.lineEdit_altMatahari = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_altMatahari.setGeometry(QtCore.QRect(100, 170, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_altMatahari.setFont(font)
        self.lineEdit_altMatahari.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_altMatahari.setText("")
        self.lineEdit_altMatahari.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_altMatahari.setReadOnly(True)
        self.lineEdit_altMatahari.setObjectName("lineEdit_altMatahari")
        self.lineEdit_azMatahari = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_azMatahari.setGeometry(QtCore.QRect(100, 200, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_azMatahari.setFont(font)
        self.lineEdit_azMatahari.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_azMatahari.setText("")
        self.lineEdit_azMatahari.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_azMatahari.setReadOnly(True)
        self.lineEdit_azMatahari.setObjectName("lineEdit_azMatahari")
        self.lineEdit_elongasi = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_elongasi.setGeometry(QtCore.QRect(100, 230, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_elongasi.setFont(font)
        self.lineEdit_elongasi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_elongasi.setText("")
        self.lineEdit_elongasi.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_elongasi.setReadOnly(True)
        self.lineEdit_elongasi.setObjectName("lineEdit_elongasi")
        self.lineEdit_usiaBulan = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_usiaBulan.setGeometry(QtCore.QRect(100, 260, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_usiaBulan.setFont(font)
        self.lineEdit_usiaBulan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_usiaBulan.setText("")
        self.lineEdit_usiaBulan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_usiaBulan.setReadOnly(True)
        self.lineEdit_usiaBulan.setObjectName("lineEdit_usiaBulan")
        self.lineEdit_moonset = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_moonset.setGeometry(QtCore.QRect(100, 290, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_moonset.setFont(font)
        self.lineEdit_moonset.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_moonset.setText("")
        self.lineEdit_moonset.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_moonset.setReadOnly(True)
        self.lineEdit_moonset.setObjectName("lineEdit_moonset")
        self.lineEdit_lagTime = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_lagTime.setGeometry(QtCore.QRect(100, 320, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_lagTime.setFont(font)
        self.lineEdit_lagTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_lagTime.setText("")
        self.lineEdit_lagTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_lagTime.setReadOnly(True)
        self.lineEdit_lagTime.setObjectName("lineEdit_lagTime")
        self.lineEdit_wujudulHilal = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_wujudulHilal.setGeometry(QtCore.QRect(100, 350, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_wujudulHilal.setFont(font)
        self.lineEdit_wujudulHilal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_wujudulHilal.setText("")
        self.lineEdit_wujudulHilal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_wujudulHilal.setReadOnly(True)
        self.lineEdit_wujudulHilal.setObjectName("lineEdit_wujudulHilal")
        self.lineEdit_imkanRukyat = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_imkanRukyat.setGeometry(QtCore.QRect(100, 380, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_imkanRukyat.setFont(font)
        self.lineEdit_imkanRukyat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_imkanRukyat.setText("")
        self.lineEdit_imkanRukyat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_imkanRukyat.setReadOnly(True)
        self.lineEdit_imkanRukyat.setObjectName("lineEdit_imkanRukyat")
        self.groupBox.raise_()
        self.listWidget.raise_()
        self.testButton.raise_()
        self.label1.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.listWidget.itemClicked.connect(self.selectedList)
        self.testButton.clicked.connect(self.test)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.testButton.setText(_translate("MainWindow", "Test"))
        self.label.setText(_translate("MainWindow", "Konjungsi"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_2.setText(_translate("MainWindow", "Konjungsi"))
        self.label_3.setText(_translate("MainWindow", "Sunset"))
        self.label_4.setText(_translate("MainWindow", "Alt Bulan"))
        self.label_5.setText(_translate("MainWindow", "Az Bulan"))
        self.label_6.setText(_translate("MainWindow", "Alt Matahari"))
        self.label_7.setText(_translate("MainWindow", "Az Matahari"))
        self.label_8.setText(_translate("MainWindow", "Elongasi"))
        self.label_9.setText(_translate("MainWindow", "Usia Bulan"))
        self.label_10.setText(_translate("MainWindow", "Moonset"))
        self.label_11.setText(_translate("MainWindow", "Lag Time"))
        self.label_12.setText(_translate("MainWindow", "Imkan Rukyat"))
        self.label_13.setText(_translate("MainWindow", "Wujudul Hilal"))

    
        # self.listWidget.itemClicked.connect(self.selectedList)
        # self.testButton.clicked.connect(self.test)
        # canvas = Canvas(self.frame_grafik, width = 5, height=4)

    def test(self):
        self.listWidget.clear()
        lat = '7.83305556 S'
        long = '110.38305556 E'
        t0 = datetime(2021, 1, 1, tzinfo=utc)
        t1 = datetime(2022, 1, 1, tzinfo=utc)
        compute.result(lat, long, t0, t1)
        self.data = compute.var.df
        sunset = self.data['Waktu Sunset (UTC+07)'].tolist()
        sunset = [str(i) for i in sunset]
        self.listWidget.addItems(sunset)

    def selectedList(self, item):
        row = self.listWidget.currentRow()
        print(row)
        data = self.data.iloc[row]
        konjungsi = data[0]
        sunset = data[1]
        alt_bulan = data[2]
        az_bulan = data[3]
        alt_matahari = data[4]
        az_matahari = data[5]
        elongasi = data[6]
        usia_bulan = data[7]
        moonset = data[8]
        lag_time = data[9]
        wujudul_hilal = []
        imkan_rukyat = data[10]



        self.lineEdit_konjungsi.setText(str(konjungsi))
        self.lineEdit_sunset.setText(str(sunset))
        self.lineEdit_altBulan.setText(str(alt_bulan))
        self.lineEdit_azBulan.setText(str(az_bulan))
        self.lineEdit_altMatahari.setText(str(alt_matahari))
        
        self.lineEdit_azMatahari.setText(str(az_matahari))
        self.lineEdit_elongasi.setText(str(elongasi))
        self.lineEdit_usiaBulan.setText(str(usia_bulan))
        self.lineEdit_moonset.setText(str(moonset))
        self.lineEdit_lagTime.setText(str(lag_time))
        
        self.lineEdit_imkanRukyat.setText(str(imkan_rukyat))

        canvas = Canvas(self.frame_grafik, moon_az=data[12], moon_alt=data[11], moon_appdia=data[15], sun_az=data[14], sun_alt=data[13], sun_appdia=data[16])
        # sc = MplCanvas(parent=self.frame_grafik, width=5, height=4, dpi=100)
        # sc.show()
        # self.setCentralWidget(sc)

        # self.show()

    # def plot_hilal(moon_az, moon_alt, moon_appdia, sun_az, sun_alt, sun_appdia):
    #     N = 1
    #     x = [moon_az, sun_az] # Azimuth
    #     y = [moon_alt, sun_alt] # Altitude
    #     r = [moon_appdia, sun_appdia] # Diameter Tampak

    #     moon = plt.Circle((x[0], y[0]), r[0], color='k')
    #     sun = plt.Circle((x[1], y[1]), r[1], color='y')
    #     plt.figure()
    #     ax = plt.subplot(aspect=1)
    #     ax.add_patch(moon)
    #     ax.add_patch(sun)
    #     plt.xlim(x[0]-2, x[1]+2)
    #     plt.ylim(y[1]-2, y[0]+2)

class pandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]
        # return 1

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Canvas(FigureCanvasQTAgg):
    # N = 1
    # x = [moon_az, sun_az] # Azimuth
    # y = [moon_alt, sun_alt] # Altitude
    # r = [moon_appdia, sun_appdia] # Diameter Tampak

    # moon = plt.Circle((x[0], y[0]), r[0], color='k')
    # sun = plt.Circle((x[1], y[1]), r[1], color='y')
    # plt.figure()
    # ax = plt.subplot(aspect=1)
    # ax.add_patch(moon)
    # ax.add_patch(sun)
    # plt.xlim(x[0]-2, x[1]+2)
    # plt.ylim(y[1]-2, y[0]+2)
    
    def __init__(self, parent = None,
                moon_az=0.1,
                moon_alt=0.1,
                moon_appdia=0.1, 
                sun_az=0.2, 
                sun_alt=0.1, 
                sun_appdia=0.1, 
                width = 5, 
                height = 4, 
                dpi = 100):
        fig = Figure(figsize=(width, height), dpi = dpi)
        fig.tight_layout()
        # fig = plt.subplot()
        # self.axes = fig.add_subplot(111)
        self.moon_az = moon_az
        self.moon_alt = moon_alt
        self.moon_appDia = moon_appdia
        self.sun_alt = sun_alt
        self.sun_az = sun_az
        self.sun_appDia = sun_appdia

        FigureCanvasQTAgg.__init__(self, fig)
        self.setParent(parent)
        
        
        self.plot()
        
    def plot(self):
        # x = np.array([50, 30, 40])
        # labels = ['A', 'B', 'C']
        # ax = self.figure.subplots()
        # ax.pie(x, labels=labels)

        x = [self.moon_az, self.sun_az] # Azimuth
        y = [self.moon_alt, self.sun_alt] # Altitude
        r = [self.moon_appDia, self.sun_appDia] # Diameter Tampak
        print(x)
        print(y)

        
        ax = self.figure.add_subplot()
        ax.axis('equal')

        ax.plot(x[0], y[0])
        ax.plot(x[1], y[1])

        moon = matplotlib.patches.Circle((x[0], y[0]), r[0], color='k', alpha=0.5)
        sun = matplotlib.patches.Circle((x[1], y[1]), r[1], color='y')
        
        # plt.figure()
        # ax.add_artist(moon)
        # ax.add_patch(sun)
        # plt.xlim(x[0]-2, x[1]+2)
        # plt.ylim(y[1]-2, y[0]+2)
        # ax.plot(x[0], y[0], 'o')
        # ax.plot(x[1], y[1], 'o')
        
        # circle = matplotlib.patches.Circle((0,0), 0.1, color="r")
        # circle2 = matplotlib.patches.Circle((0,1), 0.1, color="r")
        ax.add_artist(moon)
        ax.add_artist(sun)
        if(x[0] > x[1]):
            left = x[0] - 0.7
            right = x[1] + 0.7
        else:
            left = x[1] - 0.7
            right = x[0] + 0.7

        bottom = y[1] - 1
        top = y[0] + 1

        ax.plot([0, 360], [0, 0], 'k', label='Horizon')
        ax.text(x[0], y[0], 'Bulan', color='black')
        ax.text(x[1], y[1], 'Matahari')

        ax.axis([left, right, bottom, top])
        ax.set_xlabel('Azimuth')
        ax.set_ylabel('Altitude')
        ax.legend()

        self.show()

# class MplCanvas(FigureCanvasQTAgg):

#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super(MplCanvas, self).__init__(fig)

#     def plot(self):
#         ax = self.figure.add_subplot(111)
#         ax.plot([0,1,2,3,4], [10,1,20,3,40])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())