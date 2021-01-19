from PyQt5 import QtSql
import pymongo, var, ventas
from ventana import *

class Conexion():
    def db_connect(filename):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(str(filename))
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexión, \n'
                                           'Haz click para Cancelar', QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexión establecida')
        return True

    def altaCli(cliente):
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into clientes (dni, apellidos, nombre, fechalta, direccion, provincia, sexo, formaspago, edad)'
            'VALUES (:dni, :apellidos, :nombre, :fechalta, :direccion, :provincia, :sexo, :formaspago, :edad)')
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apellidos', str(cliente[1]))
        query.bindValue(':nombre', str(cliente[2]))
        query.bindValue(':fechalta', str(cliente[3]))
        query.bindValue(':direccion', str(cliente[4]))
        query.bindValue(':provincia', str(cliente[5]))
        query.bindValue(':sexo', str(cliente[6]))
        # pagos = ' '.join(cliente[7]) si quiesesemos un texto, pero nos viene mejor meterlo como una lista
        query.bindValue(':formaspago', str(cliente[7]))
        query.bindValue(':edad', int(cliente[8]))
        if query.exec_():
            print("Inserción Correcta")
            var.ui.lblstatus.setText('Alta Cliente con dni ' + str(cliente[0]))
            Conexion.mostrarClientes(None)
        else:
            print("Error: ", query.lastError().text())

    def cargarCliente():
        '''
        Módulo que carga el resto de widgets con los datos del cliente dni
        :return: None
        '''
        dni = var.ui.editDni.text()
        query = QtSql.QSqlQuery()
        query.prepare('select * from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            while query.next():
                var.ui.lblCodcli.setText(str(query.value(0)))
                var.ui.editClialta.setText( query.value(4))
                var.ui.editDir.setText(query.value(5))
                var.ui.cmbProv.setCurrentText(str(query.value(6)))
                if str(query.value(7)) == 'Mujer':
                    var.ui.rbtFem.setChecked(True)
                    var.ui.rbtMasc.setChecked(False)
                else:
                    var.ui.rbtMasc.setChecked(True)
                    var.ui.rbtFem.setChecked(False)
                for data in var.chkpago:
                    data.setChecked(False)
                if 'Efectivo' in query.value(8):
                    var.chkpago[0].setChecked(True)
                if 'Tarjeta' in query.value(8):
                    var.chkpago[1].setChecked(True)
                if 'Transferencia' in query.value(8):
                    var.chkpago[2].setChecked(True)
                var.ui.spinEdad.setValue(int(query.value(9)))

    def mostrarClientes(self):
        '''
        Carga los datos principales del cliente en la tabla
        se ejecuta cuando lanzamos el programa, actualizamos, insertamos y borramos un cliente
        :return: None
        '''
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes')
        if query.exec_():
            while query.next():
                #cojo los valores
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                # crea la fila
                var.ui.tablaCli.setRowCount(index+1)
                #voy metiendo los datos en cada celda de la fila
                var.ui.tablaCli.setItem(index,0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tablaCli.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tablaCli.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                index += 1
        else:
            print("Error mostrar clientes: ", query.lastError().text())

    def bajaCli(dni):
        ''''
        modulo para eliminar cliente. se llama desde fichero clientes.py
        :return None
        '''
        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            print('Baja cliente')
            var.ui.lblstatus.setText('Cliente con dni '+ dni + ' dado de baja')
        else:
            print("Error mostrar clientes: ", query.lastError().text())


    def modifCli(codigo, newdata):
           ''''
           modulo para modificar cliente. se llama desde fichero clientes.py
           :return None
           '''
           query = QtSql.QSqlQuery()
           codigo = int(codigo)
           query.prepare('update clientes set dni=:dni, apellidos=:apellidos, nombre=:nombre, fechalta=:fechalta, '
                         'direccion=:direccion, provincia=:provincia, sexo=:sexo, formaspago=:formaspago, edad=:edad where codigo=:codigo')
           query.bindValue(':codigo', int(codigo))
           query.bindValue(':dni', str(newdata[0]))
           query.bindValue(':apellidos', str(newdata[1]))
           query.bindValue(':nombre', str(newdata[2]))
           query.bindValue(':fechalta', str(newdata[3]))
           query.bindValue(':direccion', str(newdata[4]))
           query.bindValue(':provincia', str(newdata[5]))
           query.bindValue(':sexo', str(newdata[6]))
           query.bindValue(':formaspago', str(newdata[7]))
           query.bindValue(':edad', int(newdata[8]))

           if query.exec_():
               print('Cliente modificado')
               var.ui.lblstatus.setText('Cliente con dni '+ str(newdata[0]) + ' modificado')
           else:
               print("Error modificar cliente: ", query.lastError().text())

    def buscaCli(dni):
        """
        select un cliente a partir de su dni.
        :return:
        """
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select * from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            while query.next():
                var.ui.lblCodcli.setText(str(query.value(0)))
                var.ui.editApel.setText(str(query.value(1)))
                var.ui.editNombre.setText(str(query.value(2)))
                var.ui.editClialta.setText(query.value(4))
                var.ui.editDir.setText(query.value(5))
                var.ui.cmbProv.setCurrentText(str(query.value(6)))
                if str(query.value(7)) == 'Mujer':
                    var.ui.rbtFem.setChecked(True)
                    var.ui.rbtMasc.setChecked(False)
                else:
                    var.ui.rbtMasc.setChecked(True)
                    var.ui.rbtFem.setChecked(False)
                for data in var.chkpago:
                    data.setChecked(False)
                if 'Efectivo' in query.value(8):
                    var.chkpago[0].setChecked(True)
                if 'Tarjeta' in query.value(8):
                    var.chkpago[1].setChecked(True)
                if 'Transferencia' in query.value(8):
                    var.chkpago[2].setChecked(True)
                var.ui.spinEdad.setValue(query.value(9))

                var.ui.tablaCli.setRowCount(index + 1)
                    # voy metiendo los datos en cada celda de la fila
                var.ui.tablaCli.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(1))))
                var.ui.tablaCli.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(2))))
                var.ui.tablaCli.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(3))))


    #Conexión de los PRODUCTOS con la base de datos

    def altaPro(producto):
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into articulos (nombre, precio_unidad,stock)'
            'VALUES (:nombre, :precio_unidad, :stock)')
        query.bindValue(':nombre', str(producto[0]))
        producto[1] = producto[1].replace(',',',')
        query.bindValue(':precio_unidad', round(float(producto[1]),2))
        query.bindValue(':stock', int(producto[2]))
        if query.exec_():
            print("Inserción Correcta")
            var.ui.lblstatus.setText('Alta Producto con nombre ' + str(producto[0]))
            Conexion.mostrarProductos(None)
        else:
            print("Error conexion alta: ", query.lastError().text())

    def cargarProducto(cod):

        query = QtSql.QSqlQuery()
        query.prepare('select nombre, precio-unidad, stock from articulos where codigo = :cod')
        query.bindValue(':cod', cod)
        if query.exec_():
            while query.next():
                var.ui.lblCodPro.setText(str(cod))
                var.ui.editNomPro.setText(str(query.value(0)))
                var.ui.editPreUni.setText(str(query.value(1)))
                var.ui.editStock.setText(str(query.value(2)))

    def mostrarProductos():
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select codigo, nombre, precio_unidad from articulos')
        if query.exec_():
            while query.next():
                codigo = query.value(0)
                nombre = query.value(1)
                precio_unidad = query.value(2)
                var.ui.tablaPro.setRowCount(index+1)
                var.ui.tablaPro.setItem(index, 0, QtWidgets.QTableWidgetItem(codigo))
                var.ui.tablaPro.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                var.ui.tablaPro.setItem(index, 2, QtWidgets.QTableWidgetItem(precio_unidad))
                index += 1
        else:
            print("Error mostrar productos: ", query.lastError().text())

    def bajaProd(cod):
        query = QtSql.QSqlQuery()
        query.prepare('delete from articulos where codigo = :cod')
        query.bindValue(':cod', cod)
        if query.exec_():
            print('Baja producto')
            var.ui.lblstatus.setText('Producto con nombre '+ cod + ' dado de baja')
        else:
            print("Error baja conexion productos: ", query.lastError().text())
        Conexion.mostrarProductos()

    def modifProd(cod, newdataprod):
        cod = int(cod)
        query = QtSql.QSqlQuery()
        query.prepare('update articulos set nombre=:nombre, precio_unidad=:precio_unidad, stock=:stock where codigo=:cod')
        query.bindValue(':cod', int(cod))
        query.bindValue(':nombre', str(newdataprod[0]))
        newdataprod[1] = newdataprod[1].replace(',',',')
        query.bindValue(':precio_unidad', round(float(newdataprod(1)),2))
        query.bindValue(':stock', int(newdataprod[2]))
        if query.exec_():
            print('Producto modificado')
            var.ui.lblstatus.setText('Producto con código '+ str(cod) + ' modificado')
        else:
            print("Error modificar producto: ", query.lastError().text())

    # Conexión de la FACTURA con la base de datos

    def altaFac(dni, fecha, apel):
        query = QtSql.QSqlQuery()
        query.prepare('insert into facturas (dni, fecha, apellidos) VALUES (:dni, :fecha, :apellidos )')
        query.bindValue(':dni', str(dni))
        query.bindValue(':fecha', str(fecha))
        query.bindValue(':apellidos', str(apel))
        if query.exec_():
            var.ui.lblstatus.setText('Factura Creada')
        else:
            print("Error alta factura: ", query.lastError().text())
        query1 = QtSql.QSqlQuery()
        query1.prepare('select max(codfac) from facturas')
        if query1.exec_():
            while query1.next():
                var.ui.lblNumFac.setText(str(query1.value(0)))

    def mostrarFacturas(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select codfac, fecha from facturas order by codfac desc')
        if query.exec_():
            while query.next():
                # crea la fila
                var.ui.tabFac.setRowCount(index + 1)
                # voy metiendo los datos en cada celda de la fila
                var.ui.tabFac.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(0))))
                var.ui.tabFac.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(1))))
                index += 1
            Conexion.limpiarFac(self)
            var.ui.tabFac.selectRow(0)
            var.ui.tabFac.setFocus()
        else:
            print("Error mostrar facturas: ", query.lastError().text())
        if index == 0:
            var.ui.tabFac.clearContents()

    def mostrarFacturascli(self):
        index = 0
        cont = 0
        dni = var.ui.editDniclifac.text()
        query = QtSql.QSqlQuery()
        query.prepare('select codfac, fecha from facturas where dni = :dni order by codfac desc')
        query.bindValue(':dni', str(dni))
        if query.exec_():
            while query.next():
                # cojo los valores
                cont = cont + 1
                codfac = query.value(0)
                fecha = query.value(1)
                # crea la fila
                var.ui.tabFac.setRowCount(index + 1)
                # voy metiendo los datos en cada celda de la fila
                var.ui.tabFac.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codfac)))
                var.ui.tabFac.setItem(index, 1, QtWidgets.QTableWidgetItem(str(fecha)))
                index += 1
            if cont == 0:
                var.ui.tabFac.setRowCount(0)
                var.ui.lblstatus.setText('Cliente sin Facturas')
        else:
            print("Error mostrar facturas cliente: ", query.lastError().text())

    def limpiarFac(self):
        datosfac = [var.ui.editDniclifac, var.ui.editDatafac, var.ui.lblNumFac, var.ui.editApelclifac]
        for i, data in enumerate(datosfac):
            datosfac[i].setText('')

    def cargarFac(cod):
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos from facturas where codfac = :codfac')
        query.bindValue(':codfac', int(cod))
        if query.exec_():
            while query.next():
                var.ui.editDniclifac.setText(str(query.value(0)))
                var.ui.editApelclifac.setText(str(query.value(1)))

    def cargarFac2(self):
        query = QtSql.QSqlQuery()
        query.prepare('select codfac, dni, fecha, apellidos from facturas ORDER BY codfac DESC LIMIT 1')
        if query.exec_():
            while query.next():
                var.ui.lblNumFac.setText(str(query.value(0)))
                var.ui.editDniclifac.setText(str(query.value(1)))
                var.ui.editDatafac.setText(str(query.value(2)))
                var.ui.editApelclifac.setText(str(query.value(3)))

    def cargarCmbventa(cmbventa):
        var.cmbventa.clear()
        query = QtSql.QSqlQuery()
        var.cmbventa.addItem('')
        query.prepare('select codigo, producto from productos order by producto')
        if query.exec_():
            while query.next():
                var.cmbventa.addItem(str(query.value(1)))
        # articulo = var.cmbventa.currentText()
        # return articulo

    def obtenCodPrec(articulo):
        dato = []
        query = QtSql.QSqlQuery()
        query.prepare('select codigo, precio from productos where producto = :articulo')
        query.bindValue(':articulo', str(articulo))
        if query.exec_():
            while query.next():
                dato = [str(query.value(0)), str(query.value(1))]
        return dato

    def altaVenta():
        query = QtSql.QSqlQuery()
        query.prepare('insert into ventas (codfacventa, codarticventa, cantidad, precio) VALUES (:codfacventa, :codarticventa,'
                      ' :cantidad, :precio )')
        query.bindValue(':codfacventa', int(var.venta[0]))
        query.bindValue(':codarticventa', int(var.venta[1]))
        query.bindValue(':cantidad', int(var.venta[3]))
        query.bindValue(':precio', float(var.venta[4]))
        row = var.ui.tabVenta.currentRow()
        if query.exec_():
            var.ui.lblstatus.setText('Venta Realizada')
            var.ui.tabVenta.setItem(row, 1, QtWidgets.QTableWidgetItem(str(var.venta[2])))
            var.ui.tabVenta.setItem(row, 2, QtWidgets.QTableWidgetItem(str(var.venta[3])))
            var.ui.tabVenta.setItem(row, 3, QtWidgets.QTableWidgetItem(str(var.venta[4])))
            var.ui.tabVenta.setItem(row, 4, QtWidgets.QTableWidgetItem(str(var.venta[5])))
            row = row + 1
            var.ui.tabVenta.insertRow(row)
            var.ui.tabVenta.setCellWidget(row, 1, var.cmbventa)
            var.ui.tabVenta.scrollToBottom()
            Conexion.cargarCmbventa(var.cmbventa)
        else:
            print("Error alta venta: ", query.lastError().text())

    def anulaVenta(codVenta):
        query = QtSql.QSqlQuery()
        query.prepare('delete from ventas where codventa = :codVenta')
        query.bindValue(':codVenta', codVenta)
        if query.exec_():
            var.ui.lblstatus.setText('Venta Anulada')
        else:
            print("Error baja venta: ", query.lastError().text())

    def borraFac(self,codfac):
        query = QtSql.QSqlQuery()
        query.prepare('delete from facturas where codfac = :codfac')
        query.bindValue(':codfac', int(codfac))
        if query.exec_():
            var.ui.lblstatus.setText('Factura Anulada')
            Conexion.mostrarFacturas(self)
        else:
            print("Error anular factura en borrafac: ", query.lastError().text())

        query1 = QtSql.QSqlQuery()
        query1.prepare('delete from ventas where codfacventa = :codfac')
        query1.bindValue(':codfac', int(codfac))
        if query1.exec_():
            var.ui.lblstatus.setText('Factura Anulada')

        # query1 = QtSql.QSqlQuery()
        # query1.prepare('delete from ventas where codfacventa = :codfac')
        # query1.bindValue(':codfacventa', int(codfac))
        # if query1.exec_():
        #     var.ui.lblstatus.setText('Factura Anulada')
        # else:
        #     print("Error anular factura en borrafac: ", query.lastError().text())


    def listadoVentasfac(codfac):
        """

        Módulo que lista las ventas contenidaa en una factura
        :param codfac: valor factura a la que se incluirán las líneas de venta
        :type codfac: int

        Recibe el código de la factura para seleccionar los datos de las ventas cargadas a esta.
        De la BB.DD toma el nombre del producto y su precio para cada línea de venta. El precio lo multiplica
        por las unidades y se obtiene el subtotal de cada línea. Después en cada línea de la tabla irá
        el código de la venta, el nombre del producto, las unidades y dicho subotal.
        Finalmente, va sumando el subfact, que es la suma de todas las ventas de esa factura, le aplica el IVA y
        el importe total de la factura. Los tres valores, subfact, iva y fac los muestra en los label asignados.

        En excepciones se recoge cualquier error que se produzca en la ejecución del módulo.

        """
        try:

            var.subfac = 0.00
            query = QtSql.QSqlQuery()
            query1 = QtSql.QSqlQuery()
            query.prepare('select codventa, codarticventa, cantidad from ventas where codfacventa = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                index = 0
                while query.next():
                    codventa = query.value(0)
                    codarticventa = query.value(1)
                    cantidad = query.value(2)
                    var.ui.tabVenta.setRowCount(index + 1)
                    var.ui.tabVenta.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codventa)))
                    query1.prepare('select producto, precio from productos where codigo = :codarticventa')
                    query1.bindValue(':codarticventa', int(codarticventa))
                    if query1.exec_():
                        while query1.next():
                            articulo = query1.value(0)
                            precio = query1.value(1)
                            var.ui.tabVenta.setItem(index, 1, QtWidgets.QTableWidgetItem(str(articulo)))
                            var.ui.tabVenta.setItem(index, 2, QtWidgets.QTableWidgetItem(str(cantidad)))
                            subtotal = round(float(cantidad) * float(precio), 2)
                            var.ui.tabVenta.setItem(index, 3, QtWidgets.QTableWidgetItem(str(precio)))
                            var.ui.tabVenta.setItem(index, 4, QtWidgets.QTableWidgetItem(str(subtotal)))
                    index += 1
                    var.subfac = round(float(subtotal) + float(var.subfac), 2)
                #ventas.Ven tas.prepararTablaventas(index)
            if int(index) > 0:
                ventas.Ventas.prepararTablaventas(index)
            else:
                print(index)
                var.ui.tabVenta.setRowCount(0)
                ventas.Ventas.prepararTablaventas(0)
            var.ui.lblSubtotal.setText(str(var.subfac))
            var.iva = round(float(var.subfac) * 0.21, 2)
            var.ui.lblIva.setText(str(var.iva))
            var.fac = round(float(var.iva) + float(var.subfac), 2)
            var.ui.lblTotal.setText(str(var.fac))
        except Exception as error:
            print('Error Listado de la tabla de ventas: %s ' % str(error))

'''
conexión base de datos MongoDB
'''
# class Conexion():
#     HOST = 'localhost'
#     PORT =  '27017'
#     URI_CONNECTION = 'mongodb://' + HOST + ':' + PORT + '/'
#     var.DATABASE = 'empresa'
#     try:
#         print('Conexion realizada al servidor %s' %HOST)
#     except:
#         print('Error conexión')