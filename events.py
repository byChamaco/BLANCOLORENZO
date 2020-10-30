import sys, var

class Eventos():
    def Salir(self):
        '''
        módulo para cerrar el programa
        :return:
        '''
        try:
            sys.exit()
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