from PyQt5 import QtWidgets, QtGui, QtCore, QtPrintSupport
from ventana import *
from ventSalir import *
from ventavisos import *
from ventCalendar import *
from datetime import datetime, date
import sys, var, events, clients, conexion, printer, productos
import locale
# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-ES')

class DialogAvisos(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAvisos, self).__init__()
        var.dlgaviso = Ui_dlgAvisos()
        var.dlgaviso.setupUi(self)
        var.dlgaviso.btnAceptaviso.clicked.connect(events.Eventos.Confirmar)
        var.dlgaviso.btnCancelaviso.clicked.connect(events.Eventos.Anular)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_ventSalir()
        var.dlgsalir.setupUi(self)
        var.dlgsalir.btnAceptar.clicked.connect(events.Eventos.Salir)
        var.dlgsalir.btnCancelar.clicked.connect(events.Eventos.closeSalir)
        #var.dlgsalir.btnBoxSalir(var.dlgsalir.btnAceptar).clicked.connect(events.Eventos.Salir)


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_ventCalendar()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(anoactual, mesactual, diaactual)))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
        self.setWindowTitle('Abrir Archivo')
        self.setModal(True)

class PrintDialogAbrir(QtPrintSupport.QPrintDialog):
    def __init__(self):
        super(PrintDialogAbrir, self).__init__()

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_ventPrincipal()
        var.ui.setupUi(self)
        var.dlgsalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()
        var.filedlgabrir = FileDialogAbrir()
        var.dlgImprimir = PrintDialogAbrir()
        var.dlgaviso = DialogAvisos()
        events.Eventos()
        '''
        colección de datos
        '''
        var.rbtsex = (var.ui.rbtFem, var.ui.rbtMasc)
        var.chkpago = (var.ui.chkEfec, var.ui.chkTarj, var.ui.chkTrans)
        '''
        conexión de eventos con los objetos
        estamos conectando el código con la interfaz gráfica
        botones formulario cliente
        '''
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.toolbarSalir.triggered.connect(events.Eventos.Salir)
        var.ui.toolbarBackup.triggered.connect(events.Eventos.Backup)
        var.ui.toolbarCarpeta.triggered.connect(events.Eventos.AbrirDir)
        var.ui.toolbarImpresora.triggered.connect(events.Eventos.AbrirPrinter)
        var.ui.editDni.editingFinished.connect(clients.Clientes.validoDni)
        # var.ui.editDni.editingFinished.connect(lambda: clients.Clientes.validoDni)
        var.ui.btnCalendar.clicked.connect(clients.Clientes.abrirCalendar)
        var.ui.btnAltaCli.clicked.connect(clients.Clientes.altaClientes)
        var.ui.btnLimpiarCli.clicked.connect(clients.Clientes.limpiarCli)
        var.ui.btnBajaCli.clicked.connect(events.Eventos.mostrarAviso)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCliente)
        var.ui.btnReloadCli.clicked.connect(clients.Clientes.reloadCli)
        var.ui.btnBuscarCli.clicked.connect(clients.Clientes.buscarCli)
        clients.Clientes.valoresSpin()

        for i in var.rbtsex:
            i.toggled.connect(clients.Clientes.selSexo)
        for i in var.chkpago:
            i.stateChanged.connect(clients.Clientes.selPago)

        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        var.ui.tablaCli.clicked.connect(clients.Clientes.cargarCli)
        var.ui.tablaCli.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        events.Eventos.cargarProv(self)
        var.ui.statusbar.addPermanentWidget(var.ui.lblstatus, 1)
        var.ui.statusbar.addPermanentWidget(var.ui.lblstatusdate, 2)
        var.ui.lblstatus.setStyleSheet('QLabel {color: red; font: bold;}')
        var.ui.lblstatus.setText('Bienvenido a 2º DAM')
        fecha = date.today()
        var.ui.lblstatusdate.setStyleSheet('QLabel {color: black; font: bold;}')
        var.ui.lblstatusdate.setText(fecha.strftime('%A %d de %B del %Y'))

        var.ui.menubarReportCli.triggered.connect(printer.Printer.reportCli)

        conexion.Conexion.db_connect(var.filebd)
        #conexion.Conexion()
        conexion.Conexion.mostrarClientes(self)

        '''
        conexión de los metodos con la iu
        '''
        conexion.Conexion.mostrarProductos(self)
        var.ui.btnAltaPro.clicked.connect(productos.Productos.altaProductos)
        var.ui.btnLimpiarPro.clicked.connect(productos.Productos.limpiarProd)
        var.ui.btnBajaPro.clicked.connect(productos.Productos.bajaProductos)
        var.ui.btnModifPro.clicked.connect(productos.Productos.modifProducto)
        var.ui.btnSalirPro.clicked.connect(events.Eventos.Salir)
        var.ui.tablaPro.clicked.connect(productos.Productos.cargarProd)
        var.ui.tablaPro.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

    def closeEvent(self, event):
        if event:
            events.Eventos.Salir(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())