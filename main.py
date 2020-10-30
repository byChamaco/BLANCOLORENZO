from ventana import *
import sys, var, events, clients

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        var.ui = Ui_ventPrincipal()
        var.ui.setupUi(self)
        '''
        colección de datos
        '''
        var.rbtsex = (var.ui.rbtFem, var.ui.rbtMasc)
        var.chkPago = (var.ui.chkEfec, var.ui.chkTarj, var.ui.chkTrans)
        '''
        conexión de eventos con los objetos
        estamos conectando el código con la interfaz gráfica
        '''
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.editDni.editingFinished.connect(clients.Clientes.validoDni)
        for i in var.rbtsex:
            i.toggled.connect(clients.Clientes.selSexo)
        for i in var.chkPago:
            i.stateChanged.connect(clients.Clientes.selPago)
        events.Eventos.cargarProv()
        var.ui.cmbProv.activated[str].connect(events.Eventos.selProv)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())