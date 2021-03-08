from PyQt5 import QtPrintSupport, QtCore
from ventana import *
from ventSalir import *
from ventavisos import *
from ventCalendar import *
from ventabout import *
from datetime import datetime, date
import sys, var, events, clients, conexion, printer, productos, ventas
import locale
# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-ES')

class DialogAbout(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAbout, self).__init__()
        var.dlgabout = Ui_dlgAbout()
        var.dlgabout.setupUi(self)
        var.dlgabout.btnCerrar.clicked.connect(events.Eventos.CerrarAbout)

class DialogAvisos(QtWidgets.QDialog):
    def __init__(self):
        '''

        Clase que instancia la ventana avisos

        '''
        super(DialogAvisos, self).__init__()
        var.dlgaviso = Ui_dlgAvisos()
        var.dlgaviso.setupUi(self)
        var.dlgaviso.btnAceptaviso.clicked.connect(events.Eventos.Confirmar)
        var.dlgaviso.btnCancelaviso.clicked.connect(events.Eventos.Anular)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        '''

        Clase que instancia la ventana de aviso salir

        '''
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_ventSalir()
        var.dlgsalir.setupUi(self)
        var.dlgsalir.btnAceptar.clicked.connect(events.Eventos.Salir)
        var.dlgsalir.btnCancelar.clicked.connect(events.Eventos.closeSalir)
        #var.dlgsalir.btnBoxSalir(var.dlgsalir.btnAceptar).clicked.connect(events.Eventos.Salir)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        '''

        Clase que instancia la ventana de calendario

        '''
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_ventCalendar()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(anoactual, mesactual, diaactual)))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)
        var.dlgcalendar.Calendar.clicked.connect(ventas.Ventas.cargarFechafac)

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        '''

        Clase que instancia la ventana de directorio

        '''
        super(FileDialogAbrir, self).__init__()
        self.setWindowTitle('Abrir Archivo')
        self.setModal(True)

class PrintDialogAbrir(QtPrintSupport.QPrintDialog):
    def __init__(self):
        '''

        Clase que instancia la ventana de impresión

        '''
        super(PrintDialogAbrir, self).__init__()

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        '''

        Clase main. Instancia todas las ventanas del programa.
        Genera y conecta todos los eventos de los botones, tablas y otros widgets.
        Cuando se lanza se conecta con la BBDD
        Cuando se lanza el programa carga todos los artículos, factura y clientes de la BBDD en las
        ventanas correspondientes.

        '''
        super(Main, self).__init__()

        '''
        
        Instancia de ventanas auxiliares
        
        '''
        var.ui = Ui_ventPrincipal()
        var.ui.setupUi(self)
        var.dlgsalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()
        var.filedlgabrir = FileDialogAbrir()
        var.dlgImprimir = PrintDialogAbrir()
        var.dlgaviso = DialogAvisos()
        var.dlgabout = DialogAbout()
        var.cmbventa = QtWidgets.QComboBox()
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
        var.ui.btnCalendar.clicked.connect(clients.Clientes.abrirCalendar)
        var.ui.btnAltaCli.clicked.connect(clients.Clientes.altaClientes)
        var.ui.btnLimpiarCli.clicked.connect(clients.Clientes.limpiarCli)
        var.ui.btnBajaCli.clicked.connect(events.Eventos.mostrarAviso)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCliente)
        var.ui.btnReloadCli.clicked.connect(clients.Clientes.reloadCli)
        var.ui.btnBuscarCli.clicked.connect(clients.Clientes.buscarCli)
        clients.Clientes.valoresSpin()
        var.ui.btnAltaPro.clicked.connect(productos.Products.altaProducto)
        var.ui.btnLimpiarPro.clicked.connect(productos.Products.limpiarPro)
        var.ui.btnBajaPro.clicked.connect(productos.Products.bajaProd)
        var.ui.btnModifPro.clicked.connect(productos.Products.modifPro)
        var.ui.btnSalirPro.clicked.connect(events.Eventos.Salir)
        var.ui.btnFac.clicked.connect(ventas.Ventas.altaFactura)
        var.ui.btnBuscafac.clicked.connect(conexion.Conexion.mostrarFacturascli)
        var.ui.btnReloadfac.clicked.connect(conexion.Conexion.mostrarFacturas)
        var.ui.btnCalendarfac.clicked.connect(ventas.Ventas.abrirCalendar)
        var.ui.btnFacdel.clicked.connect(ventas.Ventas.borrarFactura)
        var.ui.btnAceptarventa.clicked.connect(ventas.Ventas.procesoVenta)
        var.ui.btnAnularventa.clicked.connect(ventas.Ventas.anularVenta)
        var.ui.menubarImportarDatos.triggered.connect(events.Eventos.MercaEstadisticas)
        var.ui.menubarCrearBakup.triggered.connect(events.Eventos.Backup)
        var.ui.menubarRecuperarBackUp.triggered.connect(events.Eventos.restaurarBD)

        for i in var.rbtsex:
            i.toggled.connect(clients.Clientes.selSexo)
        for i in var.chkpago:
            i.stateChanged.connect(clients.Clientes.selPago)

        '''

            Conexión de eventos de las ventas de clientes, productos y facturas

        '''
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        var.ui.tablaCli.clicked.connect(clients.Clientes.cargarCli)
        var.ui.tablaCli.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tableProd.clicked.connect(productos.Products.cargarProd)
        var.ui.tableProd.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabFac.clicked.connect(ventas.Ventas.cargarFact)
        var.ui.tabFac.clicked.connect(ventas.Ventas.mostrarVentasfac)
        var.ui.tabFac.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabVenta.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        events.Eventos.cargarProv(self)
        var.ui.statusbar.addPermanentWidget(var.ui.lblstatus, 1)
        var.ui.statusbar.addPermanentWidget(var.ui.lblstatusdate, 2)
        var.ui.lblstatus.setStyleSheet('QLabel {color: red; font: bold;}')
        var.ui.lblstatus.setText('Bienvenido a 2º DAM')
        fecha = date.today()
        var.ui.lblstatusdate.setStyleSheet('QLabel {color: black; font: bold;}')
        var.ui.lblstatusdate.setText(fecha.strftime('%A %d de %B del %Y'))

        '''
        módulos de impresión
        '''
        var.ui.menubarReportCli.triggered.connect(printer.Printer.reportCli)
        var.ui.menubarReportPro.triggered.connect(printer.Printer.reportPro)
        var.ui.menubarReportFac.triggered.connect(printer.Printer.reportFac)
        var.ui.menubarFacxCli.triggered.connect(printer.Printer.facporCli)

        conexion.Conexion.db_connect(var.filebd)
        #conexion.Conexion()
        conexion.Conexion.mostrarClientes(self)
        conexion.Conexion.mostrarProducts()
        conexion.Conexion.mostrarFacturas(self)
        var.cmbventa = QtWidgets.QComboBox()
        var.ui.tabWidget.setCurrentIndex(0)

    def closeEvent(self, event):
        if event:
            events.Eventos.Salir(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())