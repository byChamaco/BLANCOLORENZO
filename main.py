from ventana import *
from ventSalir import *
from ventCalendar import *
from datetime import datetime
import sys, var, events, clients


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisoSalir = Ui_ventSalir()
        var.avisoSalir.setupUi(self)
        var.avisoSalir.btnBoxSalir.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir)
        #var.avisoSalir.btnBoxSalir.button(QtWidgets.QDialogButtonBox.No).clicked.connect(events.Eventos.Salir)


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_ventCalendar()
        var.dlgcalendar.setupUi(self)
        diactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate(QtCore.QDate(anoactual, mesactual, diactual))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_ventPrincipal()
        var.ui.setupUi(self)
        '''
        colección de datos
        '''
        var.rbtsex = (var.ui.rbtFem, var.ui.rbtMasc)
        var.chkPago = (var.ui.chkEfec, var.ui.chkTarj, var.ui.chkTrans)
        var.avisoSalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()
        '''
        conexión de eventos con los objetos
        estamos conectando el código con la interfaz gráfica
        '''
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.editDni.editingFinished.connect(clients.Clientes.validoDni)
        var.ui.btnCalendar.clicked.connect(clients.Clientes.abrirCalendar)
        for i in var.rbtsex:
            i.toggled.connect(clients.Clientes.selSexo)
        for i in var.chkPago:
            i.stateChanged.connect(clients.Clientes.selPago)
        events.Eventos.cargarProv()
        var.ui.cmbProv.activated[str].connect(events.Eventos.selProv)

    def closeEvent(self, event):
        events.Eventos.Salir(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())