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