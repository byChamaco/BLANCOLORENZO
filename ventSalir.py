# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventSalir.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventSalir(object):
    def setupUi(self, ventSalir):
        ventSalir.setObjectName("ventSalir")
        ventSalir.resize(415, 167)
        ventSalir.setModal(True)
        self.lblMensalir = QtWidgets.QLabel(ventSalir)
        self.lblMensalir.setGeometry(QtCore.QRect(100, 40, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblMensalir.setFont(font)
        self.lblMensalir.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblMensalir.setObjectName("lblMensalir")
        self.lblImgSalir = QtWidgets.QLabel(ventSalir)
        self.lblImgSalir.setGeometry(QtCore.QRect(-10, 30, 111, 51))
        self.lblImgSalir.setText("")
        self.lblImgSalir.setPixmap(QtGui.QPixmap(":/avisoSalir/iconoAviso.png"))
        self.lblImgSalir.setScaledContents(True)
        self.lblImgSalir.setAlignment(QtCore.Qt.AlignCenter)
        self.lblImgSalir.setObjectName("lblImgSalir")
        self.btnAceptar = QtWidgets.QPushButton(ventSalir)
        self.btnAceptar.setGeometry(QtCore.QRect(150, 100, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnBoxSalir = QtWidgets.QButtonGroup(ventSalir)
        self.btnBoxSalir.setObjectName("btnBoxSalir")
        self.btnBoxSalir.addButton(self.btnAceptar)
        self.btnCancelar = QtWidgets.QPushButton(ventSalir)
        self.btnCancelar.setGeometry(QtCore.QRect(250, 100, 75, 23))
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnBoxSalir.addButton(self.btnCancelar)

        self.retranslateUi(ventSalir)
        QtCore.QMetaObject.connectSlotsByName(ventSalir)

    def retranslateUi(self, ventSalir):
        _translate = QtCore.QCoreApplication.translate
        ventSalir.setWindowTitle(_translate("ventSalir", "Salir"))
        self.lblMensalir.setText(_translate("ventSalir", "¿Está seguro que desea salir de la aplicación?"))
        self.btnAceptar.setText(_translate("ventSalir", "Aceptar"))
        self.btnCancelar.setText(_translate("ventSalir", "Cancelar"))
import avisoSalir_rc
