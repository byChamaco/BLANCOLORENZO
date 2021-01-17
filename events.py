import sys, var, clients, conexion, zipfile, os, shutil
from datetime import  datetime
from PyQt5 import  QtWidgets

class Eventos():
    def Salir(event):
        '''
        módulo para cerrar el programa
        '''
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec_():
                sys.exit()
            else:
                var.dlgsalir.hide()
                #event.ignore()
        except Exception as error:
            print('Error %s' % str(error))

    def closeSalir(event):
        try:
            if var.dlgsalir.exec_():
                var.dlgsalir.hide()
               #necesario para que ignore X de la ventana
        except Exception as error:
            print('Error %s' % str(error))

    def CerrarAbout(event):
        try:
            if var.dlgabout.exec_():
                var.dlgabout.hide()
        except Exception as error:
            print('Error %s' % str(error))

    def abrirAbout(self):
        try:
            var.dlgabout.show()
        except Exception as error:
            print('Error abrir About: %s ' % str(error))

    def cargarProv(self):
        """
        carga las provincias al iniciar el programa
        :return:
        """
        try:
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra', 'Vigo']
            for i in prov:
                var.ui.cmbProv.addItem(i)

        except Exception as error:
            print('Error: %s' % str(error))

    def Backup():
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.filedlgabrir.getSaveFileName(None, 'Guardar Copia', var.copia, '.zip', options=option)
            if var.filedlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filebd, os.path.basename(var.filebd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                var.ui.lblstatus.setText('COPIA DE SEGURIDAD DE BASE DE DATOS CREADA')
                shutil.move(str(var.copia), str(directorio))
        except Exception as error:
            print('Error: %s' % str(error))

    def AbrirDir(self):
        try:
            var.filedlgabrir.show()
        except Exception as error:
            print('Error abrir explorador: %s ' % str(error))

    def AbrirPrinter(self):
        try:
            var.dlgImprimir.setWindowTitle('Imprimir')
            var.dlgImprimir.setModal(True)
            var.dlgImprimir.show()
        except Exception as error:
            print('Error abrir imprimr: %s ' % str(error))

    def AbrirAviso(men):
        try:
            var.lblMensaviso.setText(men)
            var.dlgaviso.show()
        except Exception as error:
            print('Error abrir ventana aviso: %s ' % str(error))

    def Confirmar():
        try:
            if var.cliente:
                clients.Clientes.bajaCliente()
                var.dlgaviso.hide()
                var.cliente = False
                conexion.Conexion.mostrarClientes(None)
            if var.backup:
                var.backup = False
                var.dlgaviso.hide()
        except Exception as error:
            print('Error botón confirma: %s ' % str(error))

    def Anular():
        try:
            var.dlgaviso.hide()
        except Exception as error:
            print('Error botón anula: %s ' % str(error))

    def mostrarAviso():
        try:
            var.cliente = True
            var.lblMensaviso.setText('¿Desea eliminar el cliente?')
            var.dlgaviso.show()
        except Exception as error:
            print('Error mostrar aviso: %s ' % str(error))

    # def mostrarAvisoProd():
    #     try:
    #         var.producto = True
    #         var.lblMensaviso.setText('¿Desea eliminar el producto?')
    #         var.dlgaviso.show()
    #     except Exception as error:
    #         print('Error mostrar aviso producto: %s ' % str(error))
    #
    # def ConfirmarAvisoProd():
    #     try:
    #         productos.Productos.bajaProductos()
    #         var.dlgaviso.hide()
    #     except Exception as error:
    #         print('Error botón confirmar eliminar producto: %s ' % str(error))