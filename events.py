import sys, var, clients, conexion, zipfile, os, shutil, xlrd
from datetime import  datetime
from PyQt5 import QtWidgets, QtSql


class Eventos():
    def Salir(event):
        '''
        Módulo para cerrar el programa

        :return: None

        Muestra ventana de aviso
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
        '''

            Módulo que cierra las ventana

            :param: event que es el evento de la ventana
            :type: None
            :return: None
            :rtype: None

        '''
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
        Módulo que se ejecuta al principio para cargar las provincias. En versión posterior cargaremos
        y municipios desde la BBDD.
        :return: None
        :rtype: None
        """
        try:
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra', 'Vigo']
            for i in prov:
                var.ui.cmbProv.addItem(i)

        except Exception as error:
            print('Error: %s' % str(error))

    def Backup():
        '''

            Módulo que realizar el backup de la BBDD
            :return: None
            :rtype: None

            Utiliza la librería zipfile, añade la fecha y hora de la copia al nombre de esta y tras realizar la copia
            la mueve al directorio deseado por el cliente. Para ello abre una ventana de diálogo

        '''
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
        '''

            Módulo que abre una ventana de diálogo
            :return: None
            :rtype: None
        '''
        try:
            var.filedlgabrir.show()
        except Exception as error:
            print('Error abrir explorador: %s ' % str(error))

    def AbrirPrinter(self):
        '''

            Módulo que abre la ventana de diálogo de la impresora

            :return: None
            :rtype: None

        '''
        try:
            var.dlgImprimir.setWindowTitle('Imprimir')
            var.dlgImprimir.setModal(True)
            var.dlgImprimir.show()
        except Exception as error:
            print('Error abrir imprimr: %s ' % str(error))

    def AbrirAviso(men):
        '''

            Módulo que abre ventana de aviso

            :param: men Mensaje de aviso
            :type: string
            :return: None
            :rtype: None

        '''
        try:
            var.lblMensaviso.setText(men)
            var.dlgaviso.show()
        except Exception as error:
            print('Error abrir ventana aviso: %s ' % str(error))

    def Confirmar():
        '''

            Ventana de confirmación

            :return: None
            :rtype: None

        '''
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
        '''

            Ventana de anulación

            :return: None
            :rtype: None

       '''
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

    def restaurarBD(self):
        '''

        Módulo que restaura la BBDD

        :return: None
        :rtype: None

        Abre ventana de diálogo para buscar el directorio donde está copia de la BBDD y la restaura haciendo suo
        de la librería zipfile
        Muestra mensaje de confirmación

        '''
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.filedlgabrir.getOpenFileName(None, 'Restaurar Copia de Seguridade','','*.zip;;All Files', options= option)
            if var.filedlgabrir.Accepted and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            conexion.Conexion.db_connect(var.filebd)
            conexion.Conexion.mostrarClientes(self)
            conexion.Conexion.mostrarProducts()
            conexion.Conexion.mostrarFacturas(self)
            var.ui.lblstatus.setText('COPIA DE SEGURIDAD RESTAURADA')
        except Exception as error:
            print('Error restaurar base de datos: %s '  % str(error))

    def MercaEstadisticas(self):
        """
            Modulo que carga los datos de un excel en una base de datos

            :return: none
            :rtype: none
        """
        documento = xlrd.open_workbook("MercaEstadisticas.xls")

        productos = documento.sheet_by_index(0)

        for i in range(1, productos.nrows):
            nombre = productos.cell_value(i, 0)
            precio = productos.cell_value(i, 1)
            stock = productos.cell_value(i, 2)

            query = QtSql.QSqlQuery()

            query.prepare('insert into productos (producto, precio, stock) values (:producto, :precio, :stock)')
            query.bindValue(':producto', str(nombre))
            query.bindValue(':precio', float(precio))
            query.bindValue(':stock', int(stock))
            if query.exec_():
                query.finish()
            else:
                print("Error baja ventasFact: ", query.lastError().text())
            query.finish()
            print('nuevo creado')

        print("---------")