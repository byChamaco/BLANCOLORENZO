import var, conexion, events
from ventavisos import *


class Productos():

    def altaProductos(self):
        try:
            newprod = []
            prodtab = []
            prod = [var.ui.editNomPro, var.ui.editPreUni, var.ui.editStock]
            k = 0
            for i in prod:
                newprod.append(i.text())
                if k < 2:
                    prodtab.append(i.text())
                    k += 1
            if prod:
                row = 0
                column = 0
                var.ui.tablaPro.insertRow(row)
                for registro in prodtab:
                    cell = QtWidgets.QTableWidgetItem(registro)
                    var.ui.tablaPro.setItem(row, column, cell)
                    column +=1
                conexion.Conexion.altaPro(newprod)
            else:
                print('Faltan Datos')
                conexion.Conexion.mostrarProductos(None)
                Productos.limpiarProd()
        except Exception as error:
            print('Error show Productos: %s ' % str(error))

    def limpiarProd():
        try:
            prod = [var.ui.editNomPro, var.ui.editPreUni, var.ui.edi]
            for i in range(len(prod)):
                prod[i].setText('')
            var.ui.lblCodPro.setText('')
        except Exception as error:
            print('Error limpiar widgets productos: %s ' % str(error))

    def cargarProd():
        try:
            fila = var.ui.tablaPro.selectedItems()
            prod = [var.ui.editNomPro, var.ui.editPreUni]
            if fila:
                fila = [dato.text() for dato in fila]
            i = 0
            for i, dato in enumerate(prod):
                dato.setText(fila[i])
            conexion.Conexion.cargarProducto()
        except Exception as error:
            print('Error cargar producto: %s ' % str(error))

    def bajaProductos():
        try:
            nombre = var.ui.editNomPro.text()
            conexion.Conexion.bajaProd(nombre)
            Productos.limpiarProd()
            conexion.Conexion.mostrarProductos()
        except Exception as error:
            print('Error ventana baja producto: %s ' % str(error))

    def modifProducto(self):
        try:
            newdataprod = []
            prod = [var.ui.editNomPro, var.ui.editPreUni]
            for i in prod:
                newdataprod.append(i.text())
            codprod = var.ui.lblCodPro.text()
            conexion.Conexion.modifProd(codprod, newdataprod)
            conexion.Conexion.mostrarProductos(self)

        except Exception as error:
            print('Error cargar productos: %s ' % str(error))