from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os, var
from datetime import datetime
from PyQt5 import QtSql

class Printer():
    def cabecera(self):
        '''

            Módulo que carga la cabecera de todos los informes de la empresa, datos fiscales...

            :return: None
            :rtype: None

        '''
        try:
            logo = '.\img\logo.jpg'
            var.rep.drawImage(logo,450,752)
            var.rep.setTitle('INFORMES')
            var.rep.setAuthor('Administración Teis')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45,820,525,820)
            var.rep.line(45,750,525,750)
            textcif = 'CIF: A0000000H'
            textnom = 'IMPORTACIONES Y EXPORTACIONES TEIS S.L.'
            textdir = 'Avda. de Galicia, 101 - Vigo C.P.:36216'
            texttlfo = 'Teléfono: 886 12 04 64'
            var.rep.drawString(50, 805, textcif)
            var.rep.drawString(50, 790, textnom)
            var.rep.drawString(50, 775, textdir)
            var.rep.drawString(50, 760, texttlfo)
        except Exception as error:
            print('Error en la cabecera de informe: %s' % str(error))

    def pie(textlistado):
        '''

            Módulo que carga el pié del inforem. Es igual para todos excepto el nombre del informe
            que se pasa con la variable textlistado

            :param textlistado: según el contenido del informe
            :type: string
            :return: None
            :rtype: None

        '''
        try:
            var.rep.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique', size=7)
            var.rep.drawString(460, 40, str(fecha))
            var.rep.drawString(270, 40, str('Página %s' % var.rep.getPageNumber()))
            var.rep.drawString(50, 40, str(textlistado))
        except Exception as error:
            print('Error en el pie de informe: %s' % str(error))

    def cabeceracli(self):
        '''

            Módulo que carga la cabecera de página del informe cliente

            :return: None
            :rtype: None

        '''
        try:
            var.rep.setFont('Helvetica-Bold', size=9)
            textlistado = 'LISTADO DE CLIENTES'
            var.rep.drawString(255, 735, textlistado)
            var.rep.line(45, 730, 525, 730)
            intemcli = ['Cod', 'DNI', 'APELLIDOS', 'NOMBRE', 'FECHA ALTA']
            var.rep.drawString(45, 710, intemcli[0])
            var.rep.drawString(90, 710, intemcli[1])
            var.rep.drawString(180, 710, intemcli[2])
            var.rep.drawString(325, 710, intemcli[3])
            var.rep.drawString(465, 710, intemcli[4])
            var.rep.line(45, 703, 525, 703)
        except Exception as error:
            print('Error en cabecera 2 de clientes: %s' % str(error))

    def reportCli(self):
        '''

            Módulo que llama a la BBDD captura datos de lso clientes ordenados alfabéticamente y los va mostrando
            en el informe.

            :return: None
            :rtype: None

            la variable i represnta los valores del eje X,
            la variable j representa los valores del eje Y
            Los informes se guardan en la capreta informe y al mismo tiempo se muestran con el lector pdf que existe
            por defecto en el sistema.

        '''
        try:
            textlistado = 'LISTADO DE CLIENTES'
            var.rep = canvas.Canvas('informes/listadoclientes.pdf', pagesize=A4)
            Printer.cabecera(self)
            Printer.cabeceracli(self)
            Printer.pie(textlistado)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, dni, apellidos, nombre, fechalta from clientes order by apellidos, nombre')
            var.rep.setFont('Helvetica', size=10)
            if query.exec_():
                i = 50 #valores del eje x
                j = 690 #valores del eje y
                while query.next():
                    if j <= 80:
                        var.rep.drawString(440, 70, 'Página siguiente...')
                        var.rep.showPage()
                        Printer.cabecera(self)
                        Printer.pie(textlistado)
                        Printer.cabeceracli(self)
                        i = 55
                        j = 690
                    var.rep.setFont('Helvetica', size=10)
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawString(i+30, j, str(query.value(1)))
                    var.rep.drawString(i+130, j, str(query.value(2)))
                    var.rep.drawString(i+280, j, str(query.value(3)))
                    var.rep.drawRightString(i+470, j, str(query.value(4)))
                    j=j-25
            var.rep.save()
            rootPath = ".\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('listadoclientes.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error reporcli %s' % str(error))

    def cabecerapro(self):
        '''

            Módulo que carga la cabecera de página del informe productos

            :return: None
            :rtype: None

        '''
        try:
            var.rep.setFont('Helvetica-Bold', size=9)
            textlistado = 'LISTADO DE PRODUCTOS'
            var.rep.drawString(255, 735, textlistado)
            var.rep.line(45, 730, 525, 730)
            intempro = ['Código', 'NOMBRE', 'PRECIO(€/kg)', 'STOCK(kg)']
            var.rep.drawString(45, 710, intempro[0])
            var.rep.drawString(170, 710, intempro[1])
            var.rep.drawString(350, 710, intempro[2])
            var.rep.drawString(475, 710, intempro[3])
            var.rep.line(45, 730, 525, 730)
        except Exception as error:
            print('Error en cabecera 2 de productos: %s' % str(error))

    def reportPro(self):
        '''

            Módulo que llama a la BBDD captura datos de los productos ordenados alfabéticamente y los va mostrando
            en el informe.

            :return: None
            :rtype: None

            la variable i represnta los valores del eje X,
            la variable j representa los valores del eje Y
            Los informes se guardan en la capreta informe y al mismo tiempo se muestran con el lector pdf que existe
            por defecto en el sistema.

        '''
        try:
            textlistado = 'LISTADO DE PRODUCTOS'
            var.rep = canvas.Canvas('informes/listadoproductos.pdf', pagesize=A4)
            Printer.cabecera(self)
            Printer.cabecerapro(self)
            Printer.pie(textlistado)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, producto, precio, stock from productos order by producto')
            var.rep.setFont('Helvetica', size=10)
            if query.exec_():
                i = 50 #valores del eje x
                j = 690 #valores del eje y
                while query.next():
                    if j <= 80:
                        var.rep.drawString(400, 75, 'Página siguiente ====>')
                        var.rep.showPage()
                        Printer.cabecera(self)
                        Printer.pie(textlistado)
                        Printer.cabecerapro(self)
                        i = 50
                        j = 690
                    var.rep.setFont('Helvetica', size=10)
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawString(i+150, j, str(query.value(1)))
                    var.rep.drawRightString(i+325, j, str(query.value(2)) + ' €')
                    var.rep.drawRightString(i+450, j, str(query.value(3)))
                    j=j-25
            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('listadoproductos.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error reporcli %s' % str(error))

    def cabecerafac(codfac):
        '''

            Módulo que carga la cabecera de página del informe factura

            :param codfac: el código de la factura
            :type: int
            :return: None
            :rtype: None

            Toma datos de dos tablas. Los del cliente a la que está asociado el código factura y la de la tabla
            facturas para tomar los datos de dni y fecha.

        '''
        try:
            var.rep.setFont('Helvetica-Bold', size=11)
            var.rep.drawString(55, 725, 'Cliente: ')
            var.rep.setFont('Helvetica', size=10)
            var.rep.drawString(50, 650, 'Factura nº : %s' % str(codfac))
            var.rep.line(45, 665, 525, 665)
            var.rep.line(45, 640, 525, 640)
            var.rep.setFont('Helvetica', size=10)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, fecha from facturas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                while query.next():
                    dni = str(query.value(0))
                    var.rep.drawString(55, 710, 'DNI: %s' % str(query.value(0)))
                    var.rep.drawString(420, 650, 'Fecha: %s' % str(query.value(1)))
            query1 = QtSql.QSqlQuery()
            query1.prepare('select apellidos, nombre, direccion, provincia, formaspago from clientes where dni = :dni')
            query1.bindValue(':dni', str(dni))
            if query1.exec_():
                while query1.next():
                    var.rep.drawString(55, 695, str(query1.value(0)) + ', ' + str(query1.value(1)))
                    var.rep.drawString(300, 695, 'Formas de Pago: ')
                    var.rep.drawString(55, 680, str(query1.value(2)) + ' - ' + str(query1.value(3)))
                    var.rep.drawString(300, 680, str(query1.value(4).strip('[]').replace('\'', '').replace(',', ' -')))  #\ caracter escape indica que lo siguiente tiene un significado especial
            var.rep.line(45, 625, 525, 625)
            var.rep.setFont('Helvetica-Bold', size=10)
            temven = ['CodVenta', 'Artículo', 'Cantidad', 'Precio-Unidad(€)', 'Subtotal(€)']
            var.rep.drawString(50, 630, temven[0])
            var.rep.drawString(140, 630, temven[1])
            var.rep.drawString(275, 630, temven[2])
            var.rep.drawString(360, 630, temven[3])
            var.rep.drawString(470, 630, temven[4])
            var.rep.setFont('Helvetica-Bold', size=12)
            var.rep.drawRightString(500, 160, 'Subtotal:   ' + "{0:.2f}".format(float(
                var.ui.lblSubtotal.text())) + ' €')
            var.rep.drawRightString(500, 140, 'IVA:     ' + "{0:.2f}".format(float(var.ui.lblIva.text())) + ' €')
            var.rep.drawRightString(500, 115, 'Total Factura: ' + "{0:.2f}".format(float(
                var.ui.lblTotal.text())) + ' €')
        except Exception as error:
            print('Error cabecfac %s' % str(error))

    def reportFac(self):
        '''

            Módulo que carga el cuerpo del informe de la factura

            :return: None
            :rtype: None

            Selecciona todas las ventas de esa factura y las va anotando línea a línea:
            la variable i represnta los valores del eje X,
            la variable j representa los valores del eje Y
            Además tiene un pié de informe para mostrar los subtotales, iva y total

        '''
        try:
            textlistado = 'FACTURA'
            var.rep = canvas.Canvas('informes/factura.pdf', pagesize=A4)
            Printer.cabecera(self)
            Printer.pie(textlistado)
            codfac = var.ui.lblNumFac.text()
            Printer.cabecerafac(codfac)
            query = QtSql.QSqlQuery()
            query.prepare('select codventa, codarticventa, cantidad, precio from ventas where codfacventa = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                i = 55
                j = 600
                while query.next():
                    if j <= 100:
                        var.rep.drawString(440, 110, 'Página siguiente...')
                        var.rep.showPage()
                        Printer.cabecera(self)
                        Printer.pie(textlistado)
                        Printer.cabecerafac(self)
                        i = 50
                        j = 600
                    var.rep.setFont('Helvetica', size=10)
                    var.rep.drawString(i, j, str(query.value(0)))
                    articulo = Printer.artLinVenta(str(query.value(1)))
                    var.rep.drawString(i + 85, j, str(articulo))
                    var.rep.drawRightString(i + 245, j, str(query.value(2)))
                    var.rep.drawRightString(i + 355, j, "{0:.2f}".format(float(query.value(3))))
                    subtotal = round(float(query.value(2)) * float(query.value(3)),2)
                    var.rep.drawRightString(i + 450, j, "{0:.2f}".format(float(subtotal)) + ' €')
                    j = j - 20

            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('factura.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1

        except Exception as error:
            print('Error reporfac %s' % str(error))

    def artLinVenta(codigo):
        '''

            Módulo que toma el nombre del artículo a partir de su código

            :param: codigo código del artículo
            :type: int

            :return: artículo
            :rtype: string

            Este módulo permite en el cuerpo de la factura que se muestre el nombre del artículo y no su código

        '''
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select producto from productos where codigo = :codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec_():
                while query.next():
                    articulo = query.value(0)
            return articulo

        except Exception as error:
            print('Error artículo según código:  %s ' % str(error))

    def facporCli(self):
        '''

            Modulo que muestras informes de facturas por cliente

            :return: None
            :rtype: None

            Muestra las facturas por orden de fecha incluyendo al final el total

        '''
        try:
            textlistado = 'FACTURAS POR CLIENTE'
            var.rep = canvas.Canvas('informes/facturasporcliente.pdf', pagesize=A4)
            Printer.cabecera(self)
            Printer.pie(textlistado)
            dni = var.ui.editDniclifac.text()
            nombre = var.ui.editApelclifac.text()
            var.rep.drawString(230, 720, textlistado)
            var.rep.line(45, 710, 525, 710)
            var.rep.drawString(45,730, 'Cliente: %s '  % str(nombre) + '       DNI: %s' % str(dni))
            itempro = ['Nº Factura', 'FECHA FACTURA', 'Total (€)']
            var.rep.line(45, 680, 525, 680)
            var.rep.drawString(45, 690, itempro[0])
            var.rep.drawString(245, 690, itempro[1])
            var.rep.drawString(470, 690, itempro[2])
            query = QtSql.QSqlQuery()
            query.prepare('select codfac, fecha from facturas where dni = :dni')
            query.bindValue(':dni', str(dni))
            total = 0.00
            if query.exec_():
                i = 55
                j = 650
                while query.next():
                    if j <= 100:
                        var.rep.drawString(440, 110, 'Página siguiente...')
                        var.rep.showPage()
                        Printer.cabecera(self)
                        Printer.pie(textlistado)
                        Printer.cabecerafac(self)
                        i = 50
                        j = 600
                    var.rep.setFont('Helvetica', size=10)
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawRightString(i + 240, j, str(query.value(1)))

                    query1 = QtSql.QSqlQuery()
                    query1.prepare('select cantidad, precio from ventas where codfacventa = :codfacventa')
                    query1.bindValue(':codfacventa', int(query.value(0)))
                    subtotal = 0.00
                    if query1.exec_():
                        while query1.next():
                            subtotal = subtotal + float(query1.value(0))*float(query1.value(1))
                        var.rep.drawRightString(i + 440, j, "{0:.2f}".format(float(subtotal)*1.21)+ ' €')
                        total = total + subtotal
                    # var.rep.drawRightString(i + 355, j, "{0:.2f}".format(float(query.value(3))))
                    # subtotal = round(float(query.value(2)) * float(query.value(3)),2)
                    j = j - 20

            var.rep.drawRightString(i + 430, 120, 'Total Facturación Cliente:   ' + "{0:.2f}".format(float(total)*1.21) + ' €')

            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('facturasporcliente.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error informe facturas por cliente:  %s ' % str(error))