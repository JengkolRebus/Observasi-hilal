# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_listview.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDate, QTime, QDateTime, QAbstractTableModel, Qt
import random
import compute
from datetime import datetime
from skyfield.api import utc
import pandas as pd

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 690)
        MainWindow.setMinimumSize(QtCore.QSize(930, 690))
        MainWindow.setMaximumSize(QtCore.QSize(930, 690))
        MainWindow.setStatusTip("")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 220, 150, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignRight)
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 200, 80, 20))
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
        self.groupBox.setGeometry(QtCore.QRect(170, 200, 751, 420))
        self.groupBox.setObjectName("groupBox")
        self.frame_grafik = QtWidgets.QFrame(self.groupBox)
        self.frame_grafik.setGeometry(QtCore.QRect(260, 20, 480, 390))
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
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 220, 190))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_14.setMouseTracking(False)
        self.label_14.setTabletTracking(False)
        self.label_14.setAcceptDrops(False)
        self.label_14.setWordWrap(False)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(10, 50, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_15.setMouseTracking(False)
        self.label_15.setTabletTracking(False)
        self.label_15.setAcceptDrops(False)
        self.label_15.setWordWrap(False)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(10, 80, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_16.setMouseTracking(False)
        self.label_16.setTabletTracking(False)
        self.label_16.setAcceptDrops(False)
        self.label_16.setWordWrap(False)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(10, 110, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_17.setMouseTracking(False)
        self.label_17.setTabletTracking(False)
        self.label_17.setAcceptDrops(False)
        self.label_17.setWordWrap(False)
        self.label_17.setObjectName("label_17")
        self.button_hitung = QtWidgets.QPushButton(self.groupBox_2)
        self.button_hitung.setGeometry(QtCore.QRect(130, 150, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_hitung.setFont(font)
        self.button_hitung.setObjectName("button_hitung")

        # Latitude
        self.latitude = QtWidgets.QLineEdit(self.groupBox_2)
        self.latitude.setGeometry(QtCore.QRect(80, 20, 130, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.latitude.setFont(font)
        self.latitude.setAccessibleDescription("")
        self.latitude.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.latitude.setObjectName("latitude")
        self.latitude.setText('7.83305556 S')

        # Longitude
        self.longitude = QtWidgets.QLineEdit(self.groupBox_2)
        self.longitude.setGeometry(QtCore.QRect(80, 50, 130, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.longitude.setFont(font)
        self.longitude.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.longitude.setObjectName("longitude")
        self.longitude.setText('110.38305556 E')

        # Waktu t0
        t0 = QtCore.QDate.currentDate()
        self.dateEdit_dari = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit_dari.setGeometry(QtCore.QRect(80, 80, 130, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_dari.setFont(font)
        self.dateEdit_dari.setObjectName("dateEdit_dari")
        self.dateEdit_dari.setDate(t0)

        # Waktu t1
        t1 = t0.addMonths(1)
        self.dateEdit_sampai = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit_sampai.setGeometry(QtCore.QRect(80, 110, 130, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_sampai.setFont(font)
        self.dateEdit_sampai.setObjectName("dateEdit_sampai")
        self.dateEdit_sampai.setDate(t1)

        # self.label_18 = QtWidgets.QLabel(self.centralwidget)
        # self.label_18.setGeometry(QtCore.QRect(250, 50, 51, 25))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.label_18.setFont(font)
        # self.label_18.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        # self.label_18.setMouseTracking(False)
        # self.label_18.setTabletTracking(False)
        # self.label_18.setAcceptDrops(False)
        # self.label_18.setWordWrap(False)
        # self.label_18.setObjectName("label_18")
        # self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        # self.groupBox_3.setGeometry(QtCore.QRect(240, 0, 160, 190))
        # self.groupBox_3.setObjectName("groupBox_3")
        # self.lineEdit_elevasi = QtWidgets.QLineEdit(self.groupBox_3)
        # self.lineEdit_elevasi.setGeometry(QtCore.QRect(60, 50, 61, 25))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.lineEdit_elevasi.setFont(font)
        # self.lineEdit_elevasi.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # self.lineEdit_elevasi.setObjectName("lineEdit_elevasi")
        # self.checkBox_elevasi = QtWidgets.QCheckBox(self.groupBox_3)
        # self.checkBox_elevasi.setGeometry(QtCore.QRect(10, 20, 141, 25))
        # self.checkBox_elevasi.setObjectName("checkBox_elevasi")
        # self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        # self.label_19.setGeometry(QtCore.QRect(125, 50, 15, 25))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.label_19.setFont(font)
        # self.label_19.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        # self.label_19.setMouseTracking(False)
        # self.label_19.setTabletTracking(False)
        # self.label_19.setAcceptDrops(False)
        # self.label_19.setWordWrap(False)
        # self.label_19.setObjectName("label_19")
        # self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        # self.groupBox_4.setGeometry(QtCore.QRect(410, 0, 510, 190))
        # self.groupBox_4.setObjectName("groupBox_4")
        # self.line = QtWidgets.QFrame(self.centralwidget)
        # self.line.setGeometry(QtCore.QRect(9, 190, 910, 20))
        # self.line.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line.setObjectName("line")
        self.credit = QtWidgets.QLabel(self.centralwidget)
        self.credit.setGeometry(QtCore.QRect(839, 620, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.credit.setFont(font)
        self.credit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.credit.setMouseTracking(False)
        self.credit.setTabletTracking(False)
        self.credit.setAcceptDrops(False)
        self.credit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.credit.setWordWrap(False)
        self.credit.setObjectName("credit")
        self.button_simpan = QtWidgets.QPushButton(self.centralwidget)
        self.button_simpan.setGeometry(QtCore.QRect(80, 620, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_simpan.setFont(font)
        self.button_simpan.setObjectName("button_simpan")
        # self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.listWidget.raise_()
        self.label.raise_()
        self.groupBox_2.raise_()
        # self.label_18.raise_()
        # self.groupBox_4.raise_()
        # self.line.raise_()
        self.credit.raise_()
        self.button_simpan.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.listWidget.itemClicked.connect(self.selectedList)
        self.button_hitung.clicked.connect(self.hitung)
        self.button_simpan.clicked.connect(self.save_file)

        # self.checkBox_elevasi.isChecked

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hilal"))
        self.label.setText(_translate("MainWindow", "Sunset"))
        self.groupBox.setTitle(_translate("MainWindow", "Data"))
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
        self.groupBox_2.setTitle(_translate("MainWindow", "Setting"))
        self.label_14.setText(_translate("MainWindow", "Latitude"))
        self.label_15.setText(_translate("MainWindow", "Longitude"))
        self.label_16.setText(_translate("MainWindow", "Dari"))
        self.label_17.setText(_translate("MainWindow", "Sampai"))
        self.button_hitung.setText(_translate("MainWindow", "Hitung"))
        # self.label_18.setText(_translate("MainWindow", "Elevasi"))
        # self.groupBox_3.setTitle(_translate("MainWindow", "ELevasi"))
        # self.lineEdit_elevasi.setText(_translate("MainWindow", "0"))
        # self.checkBox_elevasi.setText(_translate("MainWindow", "Gunakan Elevasi"))
        # self.label_19.setText(_translate("MainWindow", "m"))
        # self.groupBox_4.setTitle(_translate("MainWindow", "Keterangan"))
        self.credit.setText(_translate("MainWindow", "@_jengkolrebus"))
        self.button_simpan.setText(_translate("MainWindow", "Simpan"))

    def hitung(self):
        self.listWidget.clear()
        lat = self.latitude.text()
        long = self.longitude.text()
        t0 = self.dateEdit_dari.date().toPyDate()
        t1 = self.dateEdit_sampai.date().toPyDate()
        
        # if (self.checkBox_elevasi.isChecked()):
        #     elev = int(self.lineEdit_elevasi.text())
        # else:
        #     elev = 0

        # tampilkan sedang menghitung
        self.statusbar.showMessage("Sedang menghitung...")

        # menghitung
        start_time = time.time()
        compute.result(lat, long, t0, t1)
        end_time = time.time()
        print('Runtime:', round((end_time-start_time), 2))
        # compute.result(lat, long, t0, t1, elev=elev)

        # hapus tampilan status bar
        # self.statusbar.clearMessage()

        self.data = compute.var.df
        sunset = self.data['Waktu Sunset (UTC+07)'].tolist()
        sunset = [str(i) for i in sunset]
        self.listWidget.addItems(sunset)
        
        self.statusbar.clearMessage()

    # def save_file():
    #     filetype = (("Excel Document", "*.xlsx"),)
    #     f = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=filetype)
    #     compute.var.df.to_excel(f)
    #     print("File Saved")

    def save_file(self):
        option = QFileDialog.Options()
        # option |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(None,"Save File", "", "Excel Document (*.xlsx)", options=option)
        if filename:
            compute.var.df.to_excel(filename)
            print(filename)
            print('Save')

    def selectedList(self, item):
        row = self.listWidget.currentRow()
        # print(row)
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
        x = [self.moon_az, self.sun_az] # Azimuth
        y = [self.moon_alt, self.sun_alt] # Altitude
        r = [self.moon_appDia, self.sun_appDia] # Diameter Tampak

        ax = self.figure.add_subplot()
        ax.axis('equal')

        ax.plot(x[0], y[0])
        ax.plot(x[1], y[1])

        moon = matplotlib.patches.Circle((x[0], y[0]), r[0], color='k', alpha=0.5)
        sun = matplotlib.patches.Circle((x[1], y[1]), r[1], color='y')
        
        ax.add_artist(moon)
        ax.add_artist(sun)
        if(x[0] > x[1]):
            left = x[1] - 0.7
            right = x[0] + 0.7
        else:
            left = x[0] - 0.7
            right = x[1] + 0.7

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
