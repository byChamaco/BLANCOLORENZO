import sys, var

class Eventos():
    def Salir(event):
        '''
        módulo para cerrar el programa
        '''
        try:
            var.avisoSalir.show()
            if var.avisoSalir.exec_():
                sys.exit()
            else:
                var.avisoSalir.hide()
                event.ignore()
        except Exception as error:
            print('Error %s' % str(error))

    def cargarProv():
        '''
        carga las provincias al iniciar el programa
        '''
        '''
        esta solución es provisional en su momento lo hremos de otra forna
        cargando los registros desde una base de datos
        '''
        try:
            prov = ['','A Coruña','Lugo','Ourense','Pontevedra']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error: %s ' % str(error))

    def selProv(prov):
        try:
            print('Has seleccinado la provincia de', prov)
            return prov
        except Exception as error:
            print('Error: %s' % str(error))