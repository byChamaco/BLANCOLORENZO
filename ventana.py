# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventPrincipal(object):
    def setupUi(self, ventPrincipal):
        ventPrincipal.setObjectName("ventPrincipal")
        ventPrincipal.resize(1106, 815)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ventPrincipal.sizePolicy().hasHeightForWidth())
        ventPrincipal.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ventPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lblstatus = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblstatus.sizePolicy().hasHeightForWidth())
        self.lblstatus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblstatus.setFont(font)
        self.lblstatus.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblstatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblstatus.setObjectName("lblstatus")
        self.gridLayout_9.addWidget(self.lblstatus, 4, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.btnLimpiarCli = QtWidgets.QPushButton(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLimpiarCli.sizePolicy().hasHeightForWidth())
        self.btnLimpiarCli.setSizePolicy(sizePolicy)
        self.btnLimpiarCli.setObjectName("btnLimpiarCli")
        self.gridLayout_8.addWidget(self.btnLimpiarCli, 0, 2, 1, 1)
        self.btnModifCli = QtWidgets.QPushButton(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnModifCli.sizePolicy().hasHeightForWidth())
        self.btnModifCli.setSizePolicy(sizePolicy)
        self.btnModifCli.setObjectName("btnModifCli")
        self.gridLayout_8.addWidget(self.btnModifCli, 0, 1, 1, 1)
        self.btnBajaCli = QtWidgets.QPushButton(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBajaCli.sizePolicy().hasHeightForWidth())
        self.btnBajaCli.setSizePolicy(sizePolicy)
        self.btnBajaCli.setObjectName("btnBajaCli")
        self.gridLayout_8.addWidget(self.btnBajaCli, 0, 3, 1, 1)
        self.btnSalir = QtWidgets.QPushButton(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSalir.sizePolicy().hasHeightForWidth())
        self.btnSalir.setSizePolicy(sizePolicy)
        self.btnSalir.setObjectName("btnSalir")
        self.gridLayout_8.addWidget(self.btnSalir, 0, 4, 1, 1)
        self.btnAltaCli = QtWidgets.QPushButton(self.tab_11)
        self.btnAltaCli.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAltaCli.sizePolicy().hasHeightForWidth())
        self.btnAltaCli.setSizePolicy(sizePolicy)
        self.btnAltaCli.setObjectName("btnAltaCli")
        self.gridLayout_8.addWidget(self.btnAltaCli, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_8, 8, 0, 1, 2)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lblApellidos = QtWidgets.QLabel(self.tab_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblApellidos.setFont(font)
        self.lblApellidos.setObjectName("lblApellidos")
        self.gridLayout_7.addWidget(self.lblApellidos, 0, 0, 1, 1)
        self.lblNombre = QtWidgets.QLabel(self.tab_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lblNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.gridLayout_7.addWidget(self.lblNombre, 0, 3, 1, 1)
        self.editApel = QtWidgets.QLineEdit(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editApel.sizePolicy().hasHeightForWidth())
        self.editApel.setSizePolicy(sizePolicy)
        self.editApel.setStyleSheet("background-color: rgb(203, 253, 255);")
        self.editApel.setObjectName("editApel")
        self.gridLayout_7.addWidget(self.editApel, 0, 1, 1, 1)
        self.editNombre = QtWidgets.QLineEdit(self.tab_11)
        self.editNombre.setStyleSheet("background-color: rgb(203, 253, 255);")
        self.editNombre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.editNombre.setObjectName("editNombre")
        self.gridLayout_7.addWidget(self.editNombre, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 3, 0, 1, 2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.editDir = QtWidgets.QLineEdit(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDir.sizePolicy().hasHeightForWidth())
        self.editDir.setSizePolicy(sizePolicy)
        self.editDir.setStyleSheet("background-color: rgb(203, 253, 255);")
        self.editDir.setObjectName("editDir")
        self.gridLayout_5.addWidget(self.editDir, 0, 1, 1, 1)
        self.lblProv = QtWidgets.QLabel(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblProv.sizePolicy().hasHeightForWidth())
        self.lblProv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblProv.setFont(font)
        self.lblProv.setObjectName("lblProv")
        self.gridLayout_5.addWidget(self.lblProv, 0, 3, 1, 1)
        self.cmbProv = QtWidgets.QComboBox(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProv.sizePolicy().hasHeightForWidth())
        self.cmbProv.setSizePolicy(sizePolicy)
        self.cmbProv.setObjectName("cmbProv")
        self.gridLayout_5.addWidget(self.cmbProv, 0, 4, 1, 1)
        self.lblDireccion = QtWidgets.QLabel(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDireccion.sizePolicy().hasHeightForWidth())
        self.lblDireccion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setObjectName("lblDireccion")
        self.gridLayout_5.addWidget(self.lblDireccion, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 4, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblXesCli = QtWidgets.QLabel(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblXesCli.sizePolicy().hasHeightForWidth())
        self.lblXesCli.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblXesCli.setFont(font)
        self.lblXesCli.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblXesCli.setAutoFillBackground(False)
        self.lblXesCli.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.545, y1:0.482955, x2:0.534091, y2:1, stop:0 rgba(38, 78, 203, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lblXesCli.setAlignment(QtCore.Qt.AlignCenter)
        self.lblXesCli.setObjectName("lblXesCli")
        self.gridLayout_2.addWidget(self.lblXesCli, 0, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.tab_11)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblFecha = QtWidgets.QLabel(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFecha.sizePolicy().hasHeightForWidth())
        self.lblFecha.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblFecha.setFont(font)
        self.lblFecha.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFecha.setObjectName("lblFecha")
        self.gridLayout.addWidget(self.lblFecha, 0, 8, 1, 1)
        self.editClialta = QtWidgets.QLineEdit(self.tab_11)
        self.editClialta.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editClialta.sizePolicy().hasHeightForWidth())
        self.editClialta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.editClialta.setFont(font)
        self.editClialta.setStyleSheet("background-color: rgb(203, 253, 255);")
        self.editClialta.setAlignment(QtCore.Qt.AlignCenter)
        self.editClialta.setObjectName("editClialta")
        self.gridLayout.addWidget(self.editClialta, 0, 9, 1, 1)
        self.btnReloadCli = QtWidgets.QPushButton(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReloadCli.sizePolicy().hasHeightForWidth())
        self.btnReloadCli.setSizePolicy(sizePolicy)
        self.btnReloadCli.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReloadCli.setIcon(icon)
        self.btnReloadCli.setIconSize(QtCore.QSize(24, 24))
        self.btnReloadCli.setObjectName("btnReloadCli")
        self.gridLayout.addWidget(self.btnReloadCli, 0, 5, 1, 1)
        self.btnCalendar = QtWidgets.QPushButton(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCalendar.sizePolicy().hasHeightForWidth())
        self.btnCalendar.setSizePolicy(sizePolicy)
        self.btnCalendar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon1)
        self.btnCalendar.setIconSize(QtCore.QSize(24, 24))
        self.btnCalendar.setObjectName("btnCalendar")
        self.gridLayout.addWidget(self.btnCalendar, 0, 10, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 7, 1, 1)
        self.editDni = QtWidgets.QLineEdit(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDni.sizePolicy().hasHeightForWidth())
        self.editDni.setSizePolicy(sizePolicy)
        self.editDni.setBaseSize(QtCore.QSize(0, 0))
        self.editDni.setStyleSheet("background-color: rgb(203, 253, 255);")
        self.editDni.setAlignment(QtCore.Qt.AlignCenter)
        self.editDni.setObjectName("editDni")
        self.gridLayout.addWidget(self.editDni, 0, 2, 1, 1)
        self.lblValidar = QtWidgets.QLabel(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblValidar.sizePolicy().hasHeightForWidth())
        self.lblValidar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblValidar.setFont(font)
        self.lblValidar.setText("")
        self.lblValidar.setObjectName("lblValidar")
        self.gridLayout.addWidget(self.lblValidar, 0, 3, 1, 1)
        self.lblCodcli = QtWidgets.QLabel(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(25)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCodcli.sizePolicy().hasHeightForWidth())
        self.lblCodcli.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCodcli.setFont(font)
        self.lblCodcli.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lblCodcli.setText("")
        self.lblCodcli.setObjectName("lblCodcli")
        self.gridLayout.addWidget(self.lblCodcli, 0, 0, 1, 1)
        self.btnBuscarCli = QtWidgets.QPushButton(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBuscarCli.sizePolicy().hasHeightForWidth())
        self.btnBuscarCli.setSizePolicy(sizePolicy)
        self.btnBuscarCli.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarCli.setIcon(icon2)
        self.btnBuscarCli.setIconSize(QtCore.QSize(24, 24))
        self.btnBuscarCli.setObjectName("btnBuscarCli")
        self.gridLayout.addWidget(self.btnBuscarCli, 0, 4, 1, 1)
        self.lblDni = QtWidgets.QLabel(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDni.sizePolicy().hasHeightForWidth())
        self.lblDni.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblDni.setFont(font)
        self.lblDni.setObjectName("lblDni")
        self.gridLayout.addWidget(self.lblDni, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 1, 0, 2, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line_6 = QtWidgets.QFrame(self.tab_11)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_3.addWidget(self.line_6, 0, 0, 1, 1)
        self.lblXesCli_2 = QtWidgets.QLabel(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblXesCli_2.sizePolicy().hasHeightForWidth())
        self.lblXesCli_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblXesCli_2.setFont(font)
        self.lblXesCli_2.setAutoFillBackground(False)
        self.lblXesCli_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.545, y1:0.482955, x2:0.534091, y2:1, stop:0 rgba(38, 78, 203, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lblXesCli_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblXesCli_2.setObjectName("lblXesCli_2")
        self.gridLayout_3.addWidget(self.lblXesCli_2, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 6, 0, 1, 2)
        self.tablaCli = QtWidgets.QTableWidget(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablaCli.sizePolicy().hasHeightForWidth())
        self.tablaCli.setSizePolicy(sizePolicy)
        self.tablaCli.setStyleSheet("background-color: rgb(203, 253, 255);")
        self.tablaCli.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tablaCli.setObjectName("tablaCli")
        self.tablaCli.setColumnCount(3)
        self.tablaCli.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaCli.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaCli.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaCli.setHorizontalHeaderItem(2, item)
        self.tablaCli.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaCli.horizontalHeader().setDefaultSectionSize(259)
        self.tablaCli.horizontalHeader().setHighlightSections(True)
        self.gridLayout_6.addWidget(self.tablaCli, 7, 0, 1, 2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblEdad = QtWidgets.QLabel(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblEdad.sizePolicy().hasHeightForWidth())
        self.lblEdad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblEdad.setFont(font)
        self.lblEdad.setObjectName("lblEdad")
        self.gridLayout_4.addWidget(self.lblEdad, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 3, 1, 1)
        self.lblSexo = QtWidgets.QLabel(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSexo.sizePolicy().hasHeightForWidth())
        self.lblSexo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblSexo.setFont(font)
        self.lblSexo.setObjectName("lblSexo")
        self.gridLayout_4.addWidget(self.lblSexo, 0, 0, 1, 1)
        self.rbtFem = QtWidgets.QRadioButton(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbtFem.sizePolicy().hasHeightForWidth())
        self.rbtFem.setSizePolicy(sizePolicy)
        self.rbtFem.setObjectName("rbtFem")
        self.grpbtnSex = QtWidgets.QButtonGroup(ventPrincipal)
        self.grpbtnSex.setObjectName("grpbtnSex")
        self.grpbtnSex.addButton(self.rbtFem)
        self.gridLayout_4.addWidget(self.rbtFem, 0, 1, 1, 1)
        self.rbtMasc = QtWidgets.QRadioButton(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbtMasc.sizePolicy().hasHeightForWidth())
        self.rbtMasc.setSizePolicy(sizePolicy)
        self.rbtMasc.setObjectName("rbtMasc")
        self.grpbtnSex.addButton(self.rbtMasc)
        self.gridLayout_4.addWidget(self.rbtMasc, 0, 2, 1, 1)
        self.lblPago = QtWidgets.QLabel(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPago.sizePolicy().hasHeightForWidth())
        self.lblPago.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblPago.setFont(font)
        self.lblPago.setObjectName("lblPago")
        self.gridLayout_4.addWidget(self.lblPago, 0, 7, 1, 1)
        self.spinEdad = QtWidgets.QSpinBox(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinEdad.sizePolicy().hasHeightForWidth())
        self.spinEdad.setSizePolicy(sizePolicy)
        self.spinEdad.setObjectName("spinEdad")
        self.gridLayout_4.addWidget(self.spinEdad, 0, 5, 1, 1)
        self.chkTrans = QtWidgets.QCheckBox(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkTrans.sizePolicy().hasHeightForWidth())
        self.chkTrans.setSizePolicy(sizePolicy)
        self.chkTrans.setObjectName("chkTrans")
        self.grpbtnPay = QtWidgets.QButtonGroup(ventPrincipal)
        self.grpbtnPay.setObjectName("grpbtnPay")
        self.grpbtnPay.setExclusive(False)
        self.grpbtnPay.addButton(self.chkTrans)
        self.gridLayout_4.addWidget(self.chkTrans, 0, 10, 1, 1)
        self.chkEfec = QtWidgets.QCheckBox(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkEfec.sizePolicy().hasHeightForWidth())
        self.chkEfec.setSizePolicy(sizePolicy)
        self.chkEfec.setObjectName("chkEfec")
        self.grpbtnPay.addButton(self.chkEfec)
        self.gridLayout_4.addWidget(self.chkEfec, 0, 8, 1, 1)
        self.chkTarj = QtWidgets.QCheckBox(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkTarj.sizePolicy().hasHeightForWidth())
        self.chkTarj.setSizePolicy(sizePolicy)
        self.chkTarj.setObjectName("chkTarj")
        self.grpbtnPay.addButton(self.chkTarj)
        self.gridLayout_4.addWidget(self.chkTarj, 0, 9, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 6, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 5, 0, 1, 2)
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget.addTab(self.tab_13, "")
        self.gridLayout_9.addWidget(self.tabWidget, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(17, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(17, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem6, 2, 0, 1, 1)
        self.lblstatusdate = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblstatusdate.sizePolicy().hasHeightForWidth())
        self.lblstatusdate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblstatusdate.setFont(font)
        self.lblstatusdate.setStyleSheet("")
        self.lblstatusdate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblstatusdate.setObjectName("lblstatusdate")
        self.gridLayout_9.addWidget(self.lblstatusdate, 3, 0, 1, 1)
        ventPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1106, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        ventPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventPrincipal)
        self.statusbar.setObjectName("statusbar")
        ventPrincipal.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(ventPrincipal)
        self.toolBar.setStyleSheet("")
        self.toolBar.setObjectName("toolBar")
        ventPrincipal.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSalir = QtWidgets.QAction(ventPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.toolbarBackup = QtWidgets.QAction(ventPrincipal)
        self.toolbarBackup.setCheckable(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/BackUp/backup.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarBackup.setIcon(icon3)
        self.toolbarBackup.setObjectName("toolbarBackup")
        self.toolbarSalir = QtWidgets.QAction(ventPrincipal)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/toolbarSalir/iconsalir.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarSalir.setIcon(icon4)
        self.toolbarSalir.setObjectName("toolbarSalir")
        self.toolbarCarpeta = QtWidgets.QAction(ventPrincipal)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/iconcarpeta/iconcarpeta.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarCarpeta.setIcon(icon5)
        self.toolbarCarpeta.setObjectName("toolbarCarpeta")
        self.toolbarImpresora = QtWidgets.QAction(ventPrincipal)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/iconImpres/iconImpres.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarImpresora.setIcon(icon6)
        self.toolbarImpresora.setObjectName("toolbarImpresora")
        self.actionAbrir = QtWidgets.QAction(ventPrincipal)
        self.actionAbrir.setObjectName("actionAbrir")
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.toolBar.addAction(self.toolbarCarpeta)
        self.toolBar.addAction(self.toolbarImpresora)
        self.toolBar.addAction(self.toolbarBackup)
        self.toolBar.addAction(self.toolbarSalir)

        self.retranslateUi(ventPrincipal)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ventPrincipal)

    def retranslateUi(self, ventPrincipal):
        _translate = QtCore.QCoreApplication.translate
        ventPrincipal.setWindowTitle(_translate("ventPrincipal", "Proyecto Uno"))
        self.lblstatus.setText(_translate("ventPrincipal", "TextLabel"))
        self.btnLimpiarCli.setText(_translate("ventPrincipal", "Limpiar"))
        self.btnModifCli.setText(_translate("ventPrincipal", "Modificar"))
        self.btnBajaCli.setText(_translate("ventPrincipal", "Borrar"))
        self.btnSalir.setText(_translate("ventPrincipal", "Salir"))
        self.btnAltaCli.setText(_translate("ventPrincipal", "Grabar"))
        self.lblApellidos.setText(_translate("ventPrincipal", "Apellidos:"))
        self.lblNombre.setText(_translate("ventPrincipal", "Nombre:"))
        self.lblProv.setText(_translate("ventPrincipal", "Provincia:"))
        self.lblDireccion.setText(_translate("ventPrincipal", "Dirección:"))
        self.lblXesCli.setText(_translate("ventPrincipal", "GESTIÓN CLIENTES"))
        self.lblFecha.setText(_translate("ventPrincipal", "Fecha de alta:"))
        self.lblDni.setText(_translate("ventPrincipal", "DNI:"))
        self.lblXesCli_2.setText(_translate("ventPrincipal", "Lista de clientes"))
        item = self.tablaCli.horizontalHeaderItem(0)
        item.setText(_translate("ventPrincipal", "DNI"))
        item = self.tablaCli.horizontalHeaderItem(1)
        item.setText(_translate("ventPrincipal", "APELLIDOS"))
        item = self.tablaCli.horizontalHeaderItem(2)
        item.setText(_translate("ventPrincipal", "NOMBRE"))
        self.lblEdad.setText(_translate("ventPrincipal", "Edad:"))
        self.lblSexo.setText(_translate("ventPrincipal", "Sexo:"))
        self.rbtFem.setText(_translate("ventPrincipal", "Femenino"))
        self.rbtMasc.setText(_translate("ventPrincipal", "Masculino"))
        self.lblPago.setText(_translate("ventPrincipal", "Métodos de Pago:"))
        self.chkTrans.setText(_translate("ventPrincipal", "Transferencia"))
        self.chkEfec.setText(_translate("ventPrincipal", "Efectivo"))
        self.chkTarj.setText(_translate("ventPrincipal", "Tarjeta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("ventPrincipal", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("ventPrincipal", "Facturación"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("ventPrincipal", "Productos"))
        self.lblstatusdate.setText(_translate("ventPrincipal", "TextLabel"))
        self.menuArchivo.setTitle(_translate("ventPrincipal", "Archivo"))
        self.toolBar.setWindowTitle(_translate("ventPrincipal", "toolBar"))
        self.actionSalir.setText(_translate("ventPrincipal", "Salir"))
        self.actionSalir.setShortcut(_translate("ventPrincipal", "Alt+S"))
        self.toolbarBackup.setText(_translate("ventPrincipal", "ToolBar"))
        self.toolbarBackup.setToolTip(_translate("ventPrincipal", "<html><head/><body><p><img src=\":/BackUp/backup.png\"/></p></body></html>"))
        self.toolbarSalir.setText(_translate("ventPrincipal", "ToolbarSalir"))
        self.toolbarSalir.setToolTip(_translate("ventPrincipal", "<html><head/><body><p><img src=\":/toolbarSalir/iconsalir.png\"/></p></body></html>"))
        self.toolbarCarpeta.setText(_translate("ventPrincipal", "toolbarCarpeta"))
        self.toolbarCarpeta.setToolTip(_translate("ventPrincipal", "<html><head/><body><p><img src=\":/iconcarpeta/iconcarpeta.png\"/></p></body></html>"))
        self.toolbarImpresora.setText(_translate("ventPrincipal", "toolbarImpresora"))
        self.toolbarImpresora.setToolTip(_translate("ventPrincipal", "<html><head/><body><p><img src=\":/iconImpres/iconImpres.png\"/></p></body></html>"))
        self.actionAbrir.setText(_translate("ventPrincipal", "Abrir"))
import avisoSalir_rc
import backUp_rc
import iconImpres_rc
import iconcarpeta_rc
import toolbarSalir_rc
